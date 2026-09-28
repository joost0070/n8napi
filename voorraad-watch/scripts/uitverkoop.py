"""Uitverkoopradar: wanneer raakt een maat op, en moet je nog bijschakelen?

Methode, per model en daarna verdeeld over de maten:
  1. Recent tempo   verkoop laatste 28 dagen, alle kanalen, gedeeld door de dagen
                    dat er voorraad was (days_out_of_stock uit ShopifyQL).
  2. Ontseizoenen   dat tempo gedeeld door het seizoensgewicht van die 4 weken
                    geeft het jaarniveau. Recente weken bevatten de groei al, dus
                    er is geen aparte momentumfactor nodig.
  3. Herseizoenen   week voor week vooruit de verwachte vraag van de voorraad
                    afhalen tot die op is: de verwachte uitverkoopdatum.
  4. Signaal        leeg binnen de hersteltijd = te laat, binnen hersteltijd +
                    marge = bestel nu. Alleen voor de lopende collectie en
                    doorlopende artikelen; oudere collecties krijgen geen
                    besteladvies maar een afprijsbeeld.

Vraag is bewust bruto (retouren niet afgetrokken): voor een waarschuwing is dat
de veilige kant, het signaal komt eerder in plaats van later.
"""
import json, glob, os, re, statistics, datetime as dt
from collections import defaultdict

B = os.path.dirname(os.path.abspath(__file__))
TODAY = dt.date.today()
JAAR, NU, _ = TODAY.isocalendar()
RECENT = sorted({(TODAY - dt.timedelta(days=d)).isocalendar()[1] for d in range(1, 29)})
LEVERTIJD_STD = 6       # weken, tot er per merk een gemeten of opgegeven waarde is
VEILIG = 2              # weken marge bovenop de hersteltijd
DEKKING = 8             # weken voorraad die een bestelling moet dekken
C1 = (dt.date(2024, 9, 2), dt.date(2025, 8, 31))
C2 = (dt.date(2025, 9, 1), dt.date(2026, 8, 30))

MERKSHOP = {'keen-nl', 'jan-jansen-nl', 'heydude-nl', 'rge9fj-je', 'lazamani-nl', 'lazamani-de',
            'lazamani-en', 'toni-pons-nl', 'tofvel-nl', 'tofvel-de', 'tofvel-en',
            'sockwell-b2c-nl', 'sockwell-b2c-de', 'sockwell-b2c-en', 'ns3a4j-i1'}
BREED = {'bartogi-nl', 'bartogi-de'}

ce = json.load(open(f'{B}/rows.json'))
info = {r['mpn']: r for r in ce}
ean2 = {r['ean']: r['mpn'] for r in ce if r.get('ean')}
def naar(s): return s if s in info else ean2.get(s)
def model(r): return r['parent'] or r['name']
def stype(r): return 'NOOS' if str(r.get('season_year') or '').upper() == 'NOOS' else r['season_code']
def familie(r):
    w = re.sub(r'\s+', ' ', str(r['name'] or '')).split()
    return f"{r['brand']}|{' '.join(w[:2]).lower()}" if w else f"{r['brand']}|?"
def fix(s):
    s = str(s or '')
    try: return s.encode('latin-1').decode('utf-8')
    except Exception: return s
def volgende(w): return w % 53 + 1

# =============================================================================
# 1. Seizoenscurves: kleurvariant -> modelfamilie -> merk x seizoen
#    twee volledige cycli, elk apart genormaliseerd, licht gladgestreken
# =============================================================================
cyc = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(int))))
merkdag = defaultdict(lambda: defaultdict(int))   # merk -> datum -> stuks (voor de groei)
modeldag = defaultdict(lambda: defaultdict(int))  # model -> datum -> stuks (vorig jaar zelfde weken)
def tel(m, d, q):
    r = info.get(m)
    if not r or q <= 0: return
    merkdag[r['brand']][d] += q
    modeldag[model(r)][d] += q
    c = 'c1' if C1[0] <= d <= C1[1] else 'c2' if C2[0] <= d <= C2[1] else None
    if not c: return
    w = d.isocalendar()[1]
    staart = c == 'c2' and d > C2[1] - dt.timedelta(days=56)
    for niv, k in (('parent', model(r)), ('familie', familie(r)), ('merktype', f"{r['brand']}|{stype(r)}")):
        cyc[niv][k][c][w] += q
        if staart: laatst[(niv, k, w)] = (r['brand'], laatst.get((niv, k, w), (None, 0))[1] + q)
laatst = {}
for f in glob.glob(f'{B}/shop/*_orders.json'):
    for r in json.load(open(f)):
        m = naar(r.get('sku'))
        if m: tel(m, dt.date.fromisoformat(r['d']), r.get('q') or 0)
for f in glob.glob(f'{B}/ord/o*.json'):
    try: d = json.load(open(f))
    except Exception: continue
    for o in d.get('Content') or []:
        try: od = dt.datetime.fromisoformat(o['OrderDate']).date()
        except Exception: continue
        for l in o.get('Lines') or []:
            if l.get('Status') != 'CANCELED':
                tel(l.get('MerchantProductNo'), od, l.get('Quantity') or 0)

# Merkgroei: laatste 6 weken met orderdata tegen dezelfde 6 weken een jaar eerder.
# Alleen gebruikt om de bovengrens op het jaarniveau op te rekken, niet als voorspeller:
# het recente tempo bevat de groei al. Hunter liep in sep 2026 ~3x vorig jaar.
DMAX = max(d for dd in merkdag.values() for d in dd)
def groei(merk):
    dd = merkdag.get(merk, {})
    nu = sum(q for d, q in dd.items() if DMAX - dt.timedelta(days=42) < d <= DMAX)
    vj = sum(q for d, q in dd.items() if DMAX - dt.timedelta(days=42 + 364) < d <= DMAX - dt.timedelta(days=364))
    return (nu / vj) if vj >= 30 else None
GROEI = {m: groei(m) for m in merkdag}

# Niveausprong aan het eind van de cyclus terugrekenen naar het niveau van de rest van
# de cyclus. Anders leest een merk dat net 2,5x groeit (Hunter, eind aug 2026) die sprong
# als seizoenspiek, en lijkt het seizoen voorbij terwijl het net begint.
for (niv, k, w), (merk, q) in laatst.items():
    g = GROEI.get(merk)
    if g and (g > 1.3 or g < 0.77):
        cyc[niv][k]['c2'][w] -= q * (1 - 1 / g)
WRAP = C2[0].isocalendar()[1]      # eerste week van de cyclus: niet over deze naad gladstrijken

def maakidx(cycli):
    delen, tot = [], 0
    for c in ('c1', 'c2'):
        cc = cycli.get(c, {}); t = sum(cc.values()); tot += t
        if t >= 60: delen.append({w: cc.get(w, 0) / t for w in range(1, 54)})
    if not delen or tot < 150: return None
    i = {w: sum(d[w] for d in delen) / len(delen) for w in range(1, 54)}
    def glad(w):
        vorige, na = ((w - 2) % 53) + 1, volgende(w)
        buren = [i[w]] + ([i[vorige]] if w != WRAP else []) + ([i[na]] if na != WRAP else [])
        return sum(buren) / len(buren)
    g = {w: glad(w) for w in range(1, 54)}
    s = sum(g.values()); g = {w: v / s for w, v in g.items()}
    vec = [g[w] for w in range(1, 53)]
    top13 = max(sum(vec[(k + j) % 52] for j in range(13)) for k in range(52))
    dal = min(g, key=lambda w: sum(g[((w - 1 + k) % 53) + 1] for k in (-1, 0, 1)))
    # seizoensvenster: van het dal af cumulatief 8% en 92%
    cum, start, eind, w = 0.0, None, None, dal
    for _ in range(53):
        cum += g[w]
        if start is None and cum >= 0.08: start = w
        if eind is None and cum >= 0.92: eind = w
        w = volgende(w)
    # afprijsmoment volgens de curve: 70% van de seizoensvraag is dan verkocht
    cum, afpr, w = 0.0, None, dal
    for _ in range(53):
        cum += g[w]
        if cum >= 0.70: afpr = w; break
        w = volgende(w)
    return {'idx': g, 'stuks': tot, 'top13': top13, 'dal': dal, 'start': start, 'eind': eind,
            'piek': max(g, key=g.get), 'afprijs': afpr}
IDX = {niv: {k: v for k, v in ((k, maakidx(c)) for k, c in cyc[niv].items()) if v} for niv in cyc}
def curve_voor(r):
    for niv, k in (('parent', model(r)), ('familie', familie(r)),
                   ('merktype', f"{r['brand']}|{stype(r)}")):
        v = IDX.get(niv, {}).get(k)
        if v: return niv, v
    return None, None

# =============================================================================
# 2. Collectie: lopend, net voorbij, ouder, doorlopend
# =============================================================================
HUIDIG_SZ = 'FW' if (NU >= 30 or NU <= 5) else 'SS'
HUIDIG_JR = JAAR if not (HUIDIG_SZ == 'FW' and NU <= 5) else JAAR - 1
VORIG_SZ = 'SS' if HUIDIG_SZ == 'FW' else 'FW'
VORIG_JR = HUIDIG_JR if HUIDIG_SZ == 'FW' else HUIDIG_JR - 1
def collectie(r, cv):
    jr = str(r.get('season_year') or '').upper()
    sz = r['season_code']
    if (cv and cv['top13'] < 0.33) or jr == 'NOOS':
        # de gemeten curve gaat voor het label: NOOS bleek niet altijd te kloppen
        return 'doorlopend' if not cv or cv['top13'] < 0.45 else 'lopend?'
    if not jr.isdigit():
        return 'geen label'
    j = int(jr)
    if sz == HUIDIG_SZ and j == HUIDIG_JR: return 'lopend'
    if sz == VORIG_SZ and j == VORIG_JR: return 'net voorbij'
    if sz == HUIDIG_SZ and j == HUIDIG_JR - 1: return 'vorig jaar'
    return 'ouder'
BESTELBAAR = {'lopend', 'doorlopend', 'lopend?', 'geen label', 'doorloper'}
# Het seizoensjaar is het introductiejaar, niet 'nog in de collectie'. Een artikel uit een
# ouder seizoen dat nu op volle prijs goed verkoopt, is een doorloper (bv. Hunter Downpour
# Tall, label FW 2025, nu de best verkochte laars).
OUD = {'vorig jaar', 'ouder', 'net voorbij'}
def doorloper(col, verk28, n_live, n_sale):
    return col in OUD and verk28 >= 8 and n_live > 0 and n_sale / n_live < 0.5

# =============================================================================
# 3. Data inlezen
# =============================================================================
tempo12 = {x['mpn']: x for x in json.load(open(f'{B}/tempo_ql.json'))}

q28 = defaultdict(list)                       # mpn -> [(shop, eindstand, verkocht, dagen leeg)]
for f in glob.glob(f'{B}/ql28/*.json'):
    dom = os.path.basename(f)[:-5]
    for r in json.load(open(f)):
        m = naar(r['product_variant_sku'])
        if not m: continue
        def i(x):
            try: return int(float(x or 0))
            except Exception: return 0
        q28[m].append((dom, max(i(r['ending_inventory_units']), 0), max(i(r['inventory_units_sold']), 0),
                       min(max(i(r['days_out_of_stock']), 0), 28)))

mp28 = defaultdict(int); fee_s = defaultdict(float); omzet_s = defaultdict(float)
for f in glob.glob(f'{B}/ord28/o*.json'):
    d = json.load(open(f))
    for o in d.get('Content') or []:
        kan = o.get('ChannelName') or '?'
        for l in o.get('Lines') or []:
            if l.get('Status') == 'CANCELED': continue
            m = l.get('MerchantProductNo'); q = l.get('Quantity') or 0
            if m in info: mp28[m] += q
            tot = float(l.get('LineTotalInclVat') or 0)
            fee = float(l.get('FeeFixed') or 0) + tot * float(l.get('FeeRate') or 0) / 100
            fee_s[kan] += fee; omzet_s[kan] += tot
mp_fee = sum(fee_s.values()) / max(sum(omzet_s.values()), 1)

live, prijs_live = {}, {}
for f in glob.glob(f'{B}/shop/*_products.json'):
    for v in json.load(open(f)):
        m = naar(v.get('sku'))
        if not m: continue
        if v.get('gepubliceerd'): live[m] = True
        prijs_live[m] = (v['prijs'], v.get('vanaf'))
def afgeprijsd(m):
    p = prijs_live.get(m)
    return bool(p and p[1] and p[1] > p[0] * 1.02)

# prijsregime per collectie (merk x seizoen x jaar)
colsale = defaultdict(lambda: [0, 0])
for m, (p, v) in prijs_live.items():
    r = info[m]; k = (r['brand'], r['season_code'], str(r['season_year'] or '?'))
    colsale[k][1] += 1
    if v and v > p * 1.02: colsale[k][0] += 1
def col_in_sale(r):
    a, b = colsale.get((r['brand'], r['season_code'], str(r['season_year'] or '?')), (0, 0))
    return b >= 40 and a / b >= 0.45

ratio = json.load(open(f'{B}/kostprijs_ratio.json')) if os.path.exists(f'{B}/kostprijs_ratio.json') else {}
def kostprijs(r):
    ink = r.get('purchase') or 0
    return ink / ratio.get(r['brand'], 1.6) if ink else (r.get('price') or 0) * 0.3

# =============================================================================
# 4. Hersteltijd per merk uit de weekhistorie: hoe lang stond een bestseller leeg?
# =============================================================================
wk = defaultdict(dict)                        # mpn -> {weekdatum: (eindstand, dagen leeg, verkocht)}
for f in glob.glob(f'{B}/wk/*.json'):
    for r in json.load(open(f)):
        m = naar(r['product_variant_sku'])
        if not m: continue
        try:
            wk[m][r['week']] = (int(float(r['ending_inventory_units'] or 0)),
                                int(float(r['days_out_of_stock'] or 0)),
                                int(float(r['inventory_units_sold'] or 0)))
        except Exception: pass
episodes = defaultdict(list); nooit = defaultdict(int)
for m, serie in wk.items():
    weken = sorted(serie)
    leeg = [serie[w][1] >= 5 for w in weken]
    i = 0
    while i < len(weken):
        if leeg[i] and i >= 2 and not leeg[i - 1] and not leeg[i - 2]:
            j = i
            while j < len(weken) and leeg[j]: j += 1
            if j < len(weken):
                lengte = j - i
                if lengte <= 20: episodes[info[m]['brand']].append(lengte)
                else: nooit[info[m]['brand']] += 1
            else:
                nooit[info[m]['brand']] += 1
            i = j
        else:
            i += 1
herstel = {}
for merk, e in episodes.items():
    if len(e) >= 5:
        herstel[merk] = {'weken': max(2, min(12, round(statistics.median(e)))),
                         'n': len(e), 'nooit': nooit.get(merk, 0), 'bron': 'gemeten'}
def levertijd(merk):
    return herstel.get(merk, {}).get('weken', LEVERTIJD_STD)

# =============================================================================
# 5. Per model: recent tempo, jaarniveau, per maat de uitverkoopdatum
# =============================================================================
modellen = defaultdict(list)
for m in set(q28) | set(tempo12) | set(mp28):
    if m in info: modellen[model(info[m])].append(m)

merkmaat = defaultdict(lambda: defaultdict(float))
for m, t in tempo12.items():
    r = info.get(m)
    if r and r['size']: merkmaat[r['brand']][str(r['size'])] += t['stuks_jaar']

def uitverkoop(voorraad, jaarvraag, idx, start):
    """dagen tot de voorraad op is, seizoensgewogen; None als dat langer dan een jaar duurt"""
    if voorraad <= 0: return 0.0
    rest, dagen, w = voorraad, 0.0, start
    for _ in range(52):
        vraag = jaarvraag * idx[w]
        if vraag >= rest: return dagen + 7 * rest / vraag
        rest -= vraag; dagen += 7; w = volgende(w)
    return None

def vraag_over(jaarvraag, idx, start, weken):
    s, w = 0.0, start
    for _ in range(int(weken)): s += jaarvraag * idx[w]; w = volgende(w)
    return s

def rest_seizoen(voorraad, jaarvraag, cv, start):
    """wat blijft er over als het seizoensdal bereikt is"""
    rest, w, n = voorraad, start, 0
    while w != cv['dal'] and n < 53:
        rest -= jaarvraag * cv['idx'][w]; w = volgende(w); n += 1
    return max(rest, 0), n

STATUS = [('LEEG', 0), ('TE LAAT', 1), ('BESTEL NU', 2), ('VOLGENDE WEEK', 3), ('OK', 4), ('GEEN VRAAG', 5)]
RANG = dict(STATUS)

uit_modellen = []
for p, mpns in modellen.items():
    rs = [info[m] for m in mpns]
    r0 = max(rs, key=lambda r: tempo12.get(r['mpn'], {}).get('stuks_jaar', 0))
    niv, cv = curve_voor(r0)
    if not cv: continue
    col = collectie(r0, cv)
    merk = r0['brand']

    rij = []
    for m in mpns:
        r = info[m]; t = tempo12.get(m, {})
        s28 = q28.get(m, [])
        vrd = max((x[1] for x in s28), default=r['stock'] or 0)
        verk = sum(x[2] for x in s28) + mp28.get(m, 0)
        leeg28 = statistics.median([x[3] for x in s28]) if s28 else (0 if vrd > 0 else 28)
        kanaal = {'merkshop': sum(x[2] for x in s28 if x[0] in MERKSHOP),
                  'breed': sum(x[2] for x in s28 if x[0] in BREED),
                  'marktplaats': mp28.get(m, 0)}
        rij.append({'m': m, 'maat': fix(r['size']), 'vrd': vrd, 'verk28': verk, 'leeg28': leeg28,
                    'n12': t.get('stuks_jaar', 0), 't12': t.get('tempo_wk', 0) or 0,
                    'kanaal': kanaal, 'live': live.get(m, False), 'sale': afgeprijsd(m),
                    'prijs': r['price'] or 0, 'kost': kostprijs(r)})
    if not any(x['verk28'] or x['n12'] or x['vrd'] for x in rij): continue

    # maatverdeling: eigen historie, recente verkoop telt zwaarder, merkcurve als prior
    mm = merkmaat.get(merk, {}); mtot = sum(mm.get(x['maat'], 0) for x in rij) or 0
    K = 10
    gew = {x['m']: x['n12'] + 3 * x['verk28'] for x in rij}
    gtot = sum(gew.values())
    for x in rij:
        prior = (mm.get(x['maat'], 0) / mtot) if mtot else 1 / len(rij)
        x['aandeel'] = (gew[x['m']] + K * prior) / (gtot + K)
    s = sum(x['aandeel'] for x in rij) or 1
    for x in rij: x['aandeel'] /= s

    # recent tempo op modelniveau, gecorrigeerd voor de dagen dat maten leeg stonden
    verk28 = sum(x['verk28'] for x in rij)
    begrensd = False
    beschikbaar = sum(x['aandeel'] * (28 - x['leeg28']) for x in rij)
    idx_recent = sum(cv['idx'][w] for w in RECENT) / len(RECENT)
    j12 = sum(x['t12'] for x in rij) * 52
    n12 = sum(x['n12'] for x in rij)
    if verk28 >= 8 and beschikbaar >= 5 and idx_recent >= 0.5 / 52:
        wekelijks = verk28 / beschikbaar * 7
        jaarvraag = wekelijks / idx_recent
        if n12 >= 30 and j12 > 0:
            plafond = 2.5 * j12 * max(1.0, GROEI.get(merk) or 1.0)
            begrensd = jaarvraag > plafond
            jaarvraag = min(max(jaarvraag, 0.4 * j12), plafond)
        bron = 'recent'
    elif j12 > 0:
        jaarvraag, bron = j12, '12 mnd'
    else:
        continue

    lt = levertijd(merk)
    for x in rij:
        jv = jaarvraag * x['aandeel']
        x['jaarvraag'] = jv
        x['per_week'] = jv * cv['idx'][NU]
        x['dagen'] = uitverkoop(x['vrd'], jv, cv['idx'], NU)
        x['dagen_vlak'] = (x['vrd'] / (x['verk28'] / max(28 - x['leeg28'], 1))) if x['verk28'] else None
        horizon = vraag_over(jv, cv['idx'], NU, lt + VEILIG + DEKKING)
        x['bestel'] = max(0, round(vraag_over(jv, cv['idx'], NU, lt + DEKKING) - x['vrd']))
        if horizon < 2 and x['vrd'] == 0:
            x['status'] = 'GEEN VRAAG'
        elif x['vrd'] == 0:
            x['status'] = 'LEEG'
        elif x['dagen'] is None:
            x['status'] = 'OK'
        elif x['dagen'] < lt * 7:
            x['status'] = 'TE LAAT'
        elif x['dagen'] < (lt + VEILIG) * 7:
            x['status'] = 'BESTEL NU'
        elif x['dagen'] < (lt + VEILIG + 2) * 7:
            x['status'] = 'VOLGENDE WEEK'
        else:
            x['status'] = 'OK'

    # kernmaten: samen 80% van de vraag. Een lege randmaat maakt het model niet rood.
    kern, cum = set(), 0.0
    for x in sorted(rij, key=lambda x: -x['aandeel']):
        if cum >= 0.80: break
        kern.add(x['m']); cum += x['aandeel']
    kernrij = [x for x in rij if x['m'] in kern and x['status'] != 'GEEN VRAAG']
    status = min((x['status'] for x in kernrij), key=lambda s: RANG[s], default='OK')
    eerste = min((x['dagen'] for x in kernrij if x['dagen'] is not None), default=None)
    totaal_vrd = sum(x['vrd'] for x in rij)
    dagen_totaal = uitverkoop(totaal_vrd, jaarvraag, cv['idx'], NU)
    over, weken_rest = rest_seizoen(totaal_vrd, jaarvraag, cv, NU)

    # vorig jaar dezelfde weken: stond het model toen leeg?
    vj_leeg = None
    vj = []
    for x in rij:
        for wd, (e, lg, v) in wk.get(x['m'], {}).items():
            d = dt.date.fromisoformat(wd)
            if d.year == JAAR - 1 and NU <= d.isocalendar()[1] <= min(NU + 12, 52):
                vj.append((x['aandeel'], lg / 7))
    if vj:
        vj_leeg = sum(a * f for a, f in vj) / max(sum(a for a, _ in vj), 1e-9)

    # Controle: wat ging er vorig jaar in dezelfde weken weg? (28 dagen terug en de komende
    # hersteltijd + dekking). Zo is een voorstel van 378 naast 'vorig jaar 41' meteen te wegen.
    vjd = TODAY - dt.timedelta(days=364); md = modeldag.get(p, {})
    vj_28 = sum(q for d, q in md.items() if vjd - dt.timedelta(days=28) <= d < vjd)
    vj_hor = sum(q for d, q in md.items() if vjd <= d < vjd + dt.timedelta(weeks=lt + DEKKING))
    hor_nu = sum(vraag_over(x['jaarvraag'], cv['idx'], NU, lt + DEKKING) for x in rij)
    weinig_historie = n12 < 30 or vj_hor < 20
    # sprong: nu veel meer dan vorig jaar in dezelfde weken. Kan echt zijn (Hunter), kan een
    # actie of lancering zijn. Het rapport vraagt dan om bevestiging voor je bestelt.
    sprong = round(verk28 / vj_28, 1) if vj_28 >= 3 and verk28 >= 4 * vj_28 else None
    kanaal = {k: sum(x['kanaal'][k] for x in rij) for k in ('merkshop', 'breed', 'marktplaats')}
    n_live = sum(1 for x in rij if x['live']); n_sale = sum(1 for x in rij if x['live'] and x['sale'])
    label = col
    if doorloper(col, verk28, n_live, n_sale): col = 'doorloper'
    # De prijs van het model zelf beslist, niet die van de collectie: een model op volle prijs
    # in een collectie die grotendeels in de sale ligt, is bewust vastgehouden (bv. Hunter
    # Women's Original Tall, 16x vorig jaar). De collectievlag gaat als info mee.
    bestelbaar = (col in BESTELBAAR and n_live > 0 and n_sale / n_live < 0.5)
    uit_modellen.append({
        'model': p, 'merk': merk, 'naam': fix(r0['name']), 'collectie': col, 'label': label,
        'begrensd': begrensd, 'vj_28': vj_28, 'vj_horizon': vj_hor, 'verwacht_horizon': round(hor_nu),
        'weinig_historie': weinig_historie, 'sprong': sprong,
        'seizoen': f"{r0['season_code']} {r0['season_year'] or ''}".strip(),
        'curve': niv, 'piek': cv['piek'], 'start': cv['start'], 'eind': cv['eind'], 'dal': cv['dal'],
        'afprijs_wk': cv['afprijs'], 'nog_te_gaan': round(100 * sum(
            cv['idx'][((NU - 1 + k) % 53) + 1] for k in range(weken_rest)), 0),
        'verk28': verk28, 'kanaal': kanaal, 'voorraad': totaal_vrd,
        'jaarvraag': round(jaarvraag), 'bron': bron, 'levertijd': lt,
        'levertijd_bron': herstel.get(merk, {}).get('bron', 'aanname'),
        'status': status, 'eerste_leeg': None if eerste is None else round(eerste),
        'dagen_totaal': None if dagen_totaal is None else round(dagen_totaal),
        'over_bij_dal': round(over), 'weken_tot_dal': weken_rest,
        'vorig_jaar_leeg': None if vj_leeg is None else round(100 * vj_leeg),
        'bestelbaar': bestelbaar, 'col_sale': col_in_sale(r0),
        'prijs': r0['price'] or 0,
        'maten': sorted([{k: (round(v, 2) if isinstance(v, float) else v) for k, v in x.items()
                          if k in ('maat', 'vrd', 'verk28', 'leeg28', 'aandeel', 'per_week', 'dagen',
                                   'dagen_vlak', 'status', 'bestel', 'sale')} | {'kern': x['m'] in kern}
                         for x in rij if x['status'] != 'GEEN VRAAG' or x['vrd'] > 0],
                        key=lambda x: (float(re.sub(r'[^0-9.]', '', x['maat'].split('-')[0].split('/')[0]) or 999)
                                       if re.match(r'^\d', x['maat'] or '') else 999, x['maat'])),
        'bestel_totaal': sum(x['bestel'] for x in rij if x['m'] in kern),
        'mis_eur': round(sum(vraag_over(x['jaarvraag'], cv['idx'], NU, lt) * x['prijs']
                             for x in rij if x['status'] in ('LEEG', 'TE LAAT') and x['m'] in kern)),
    })

# =============================================================================
# 6. Rapportage
# =============================================================================
top10 = sorted([u for u in uit_modellen if u['verk28'] > 0], key=lambda u: -u['verk28'])[:10]
signalen = sorted([u for u in uit_modellen if u['bestelbaar'] and u['status'] in ('LEEG', 'TE LAAT', 'BESTEL NU')
                   and u['verk28'] >= 3],
                  # leeg en te laat samen, gesorteerd op wat het kost (omzet die binnen de hersteltijd
                  # misloopt); daarna bestel-nu op volume. Een leeg randartikel met 3 verkopen hoort
                  # niet boven de best verkochte laars die over 5 dagen op is.
                  key=lambda u: (0 if u['status'] in ('LEEG', 'TE LAAT') else 1, -u['mis_eur'], -u['verk28']))

per_col = defaultdict(int)
for u in uit_modellen: per_col[u['collectie']] += u['verk28']
kan_tot = {k: sum(u['kanaal'][k] for u in uit_modellen) for k in ('merkshop', 'breed', 'marktplaats')}

# terugblik: hoe vaak stonden de 50 best verkopende modellen (deels) leeg?
q365 = defaultdict(list)
for f in glob.glob(f'{B}/ql/*.json'):
    for r in json.load(open(f)):
        m = naar(r['product_variant_sku'])
        if m:
            try: q365[m].append(int(float(r['days_out_of_stock'] or 0)))
            except Exception: pass
terug = []
for p, mpns in modellen.items():
    n = sum(tempo12.get(m, {}).get('stuks_jaar', 0) for m in mpns)
    if n < 20: continue
    aand = {m: tempo12.get(m, {}).get('stuks_jaar', 0) / n for m in mpns}
    leeg = sum(aand[m] * statistics.median(q365[m]) for m in mpns if q365.get(m))
    beschikbaar = max(365 - leeg, 30)
    gemist = n * leeg / beschikbaar
    r0 = info[mpns[0]]
    prijs = statistics.median([info[m]['price'] or 0 for m in mpns])
    kost = statistics.median([kostprijs(info[m]) for m in mpns])
    terug.append({'model': p, 'merk': r0['brand'], 'naam': fix(r0['name']), 'verkocht': n,
                  'leverbaar_pct': round(100 * (1 - leeg / 365)), 'dagen_leeg': round(leeg),
                  'gemist_st': round(gemist), 'gemist_omzet': round(gemist * prijs),
                  'gemist_marge': round(gemist * max(prijs - kost, 0))})
terug.sort(key=lambda t: -t['verkocht'])
top50 = terug[:50]

uit = {
    'peildatum': TODAY.isoformat(), 'week': NU, 'recent_weken': RECENT,
    'huidige_collectie': f"{HUIDIG_SZ} {HUIDIG_JR}",
    'instellingen': {'levertijd_std': LEVERTIJD_STD, 'veilig': VEILIG, 'dekking': DEKKING},
    'herstel': herstel, 'nooit_hersteld': dict(nooit),
    'groei': {m: round(g, 2) for m, g in GROEI.items() if g}, 'groei_tot': DMAX.isoformat(),
    'marktplaats_fee_pct': round(100 * mp_fee, 1),
    'fee_per_kanaal': {k: round(100 * fee_s[k] / omzet_s[k], 1) for k in fee_s if omzet_s[k] > 500},
    'verkoop_per_collectie': dict(per_col), 'kanalen': kan_tot,
    'top10': top10, 'signalen': signalen[:40], 'n_signalen': len(signalen),
    'signalen_per_status': {s: sum(1 for u in signalen if u['status'] == s) for s, _ in STATUS[:3]},
    'terugblik': {
        'modellen': len(top50),
        'gem_leverbaar': round(statistics.mean(t['leverbaar_pct'] for t in top50)) if top50 else None,
        'nooit_leeg': sum(1 for t in top50 if t['dagen_leeg'] < 3),
        'gemist_st': sum(t['gemist_st'] for t in top50),
        'gemist_omzet': sum(t['gemist_omzet'] for t in top50),
        'gemist_marge': sum(t['gemist_marge'] for t in top50),
        'slechtst': sorted(top50, key=lambda t: t['leverbaar_pct'])[:10],
    },
}
json.dump(uit, open(f'{B}/uitverkoop.json', 'w'), ensure_ascii=False, indent=1)

# ---- samenvatting op het scherm ----
print(f"peildatum {TODAY} (wk {NU}) | lopende collectie {HUIDIG_SZ} {HUIDIG_JR} | recente weken {RECENT}")
print(f"modellen beoordeeld: {len(uit_modellen):,} | signalen: {len(signalen)} {uit['signalen_per_status']}")
hs = ', '.join('%s %swk (n=%s)' % (k, v['weken'], v['n']) for k, v in herstel.items()) or 'geen'
print("hersteltijd gemeten voor: " + hs)
print("merkgroei (6 wk t/m %s vs vorig jaar): " % DMAX + ', '.join(f"{m} {g:.2f}x" for m, g in sorted(GROEI.items(), key=lambda x: -(x[1] or 0)) if g))
print("begrensd door plafond: " + ', '.join(u['naam'][:30] for u in uit_modellen if u['begrensd']) )
print(f"marktplaats-fee gemiddeld: {uit['marktplaats_fee_pct']}%  per kanaal: {uit['fee_per_kanaal']}")
tv = sum(per_col.values()) or 1
print("verkoop laatste 28 dagen per collectie: " +
      ', '.join(f"{k} {100*v/tv:.0f}%" for k, v in sorted(per_col.items(), key=lambda x: -x[1])))
tk = sum(kan_tot.values()) or 1
print("per kanaal: " + ', '.join(f"{k} {100*v/tk:.0f}%" for k, v in kan_tot.items()))
print()
print(f"{'#':>2s} {'merk':9s} {'model':40s} {'coll':11s} {'28d':>4s} {'vrd':>5s} {'1e kernmaat leeg':>16s} {'status':13s}")
for i, u in enumerate(top10, 1):
    e = '—' if u['eerste_leeg'] is None else f"{u['eerste_leeg']} d"
    print(f"{i:2d} {u['merk'][:9]:9s} {u['naam'][:40]:40s} {u['collectie'][:11]:11s} {u['verk28']:4d} "
          f"{u['voorraad']:5d} {e:>16s} {u['status']:13s}")
t = uit['terugblik']
print(f"\nterugblik top-50 modellen: gemiddeld {t['gem_leverbaar']}% leverbaar, "
      f"{t['nooit_leeg']} nooit leeg, geschat gemist {t['gemist_st']:,} st / EUR {t['gemist_omzet']:,} omzet")
