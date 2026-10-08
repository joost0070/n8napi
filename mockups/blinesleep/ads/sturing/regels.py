"""Bline advertentiesturing: KPI's en beslisregels (vaste rekenregels, geen taalmodel).

Model: gamma-Poisson op uitgave. Orders per euro ~ Gamma(a0 + orders, b0 + uitgave), met als startpunt
break-even (b0 = bijdrage per order, a0 = 1 order). De kans dat de echte ROAS boven een drempel r ligt is
P(lambda > r / AOV), en voor een gehele vormparameter is dat een Poisson-som.
Zie reports/Bline AI advertentiesysteem en budgetplan.md (hoofdstuk "Vier beslismomenten").
"""
import datetime as dt
import math


def kans_roas_boven(orders, uitgave, drempel, aov, b0, a0=1):
    a = a0 + int(round(orders))
    x = (b0 + uitgave) * drempel / aov
    term, som = math.exp(-x), 0.0
    for i in range(a):
        som += term
        term *= x / (i + 1)
    return min(1.0, som)


def _getal(v, standaard=0.0):
    if v in (None, ''):
        return standaard
    try:
        return float(str(v).replace(',', '.'))
    except ValueError:
        return standaard


def lees_config(rijen):
    """Config-tabblad (Sleutel, Waarde, ...) naar een dict met getallen waar mogelijk."""
    c = {}
    for r in rijen[1:]:
        if not r or not r[0]:
            continue
        v = r[1] if len(r) > 1 else ''
        try:
            c[r[0]] = float(str(v).replace(',', '.'))
        except ValueError:
            c[r[0]] = str(v).strip()
    return c


def _dagen(d, van, tot):
    return {k: v for k, v in d.items() if van <= k <= tot}


def _som(dagen, veld):
    return sum(v.get(veld, 0) for v in dagen.values())


class Beslisser:
    """Maakt KPI's en voorstellen. `vandaag` is de rapportdag; 'gisteren' is de laatste volle dag."""

    def __init__(self, cfg, data, vandaag, logboek=(), open_voorstellen=()):
        self.c, self.d = cfg, data
        self.vandaag = vandaag
        self.gisteren = (dt.date.fromisoformat(vandaag) - dt.timedelta(days=1)).isoformat()
        self.start = str(cfg.get('start_verliesteller') or cfg.get('start_fase0'))
        self.voorstellen, self.vlaggen, self.notities = [], [], []
        self.logboek = list(logboek)
        self.open = {(v.get('object'), v.get('actie')) for v in open_voorstellen}
        self.bijdrage = cfg['bijdrage_per_order']
        orders = [o for o in data['shopify']['orders'] if o['datum'] >= self.start]
        echt = [o['omzet'] for o in orders]
        self.aov = (sum(echt) / len(echt)) if len(echt) >= 10 else cfg['gem_orderwaarde']

    # ---------- hulpfuncties ----------

    def _dag(self, n):
        return (dt.date.fromisoformat(self.gisteren) - dt.timedelta(days=n - 1)).isoformat()

    def _orders(self, kanaal=None, campagne=None, van=None, tot=None):
        van, tot = van or self.start, tot or self.gisteren
        uit = []
        for o in self.d['shopify']['orders']:
            if not (van <= o['datum'] <= tot):
                continue
            if kanaal and o['kanaal'] != kanaal:
                continue
            if campagne and str(o.get('campagne') or '') != str(campagne):
                continue
            uit.append(o)
        return uit

    def _kans(self, orders, uitgave, drempel):
        return kans_roas_boven(orders, uitgave, drempel, self.aov, self.bijdrage)

    def _laatste_wijziging(self, object_id):
        datums = [r['tijd'][:10] for r in self.logboek
                  if r.get('object') == object_id and r.get('status') == 'uitgevoerd']
        return max(datums) if datums else None

    def _mag_wijzigen(self, object_id):
        laatste = self._laatste_wijziging(object_id)
        if not laatste:
            return True
        dagen = (dt.date.fromisoformat(self.vandaag) - dt.date.fromisoformat(laatste)).days
        return dagen >= self.c.get('min_dagen_tussen_wijzigingen', 3)

    def stel_voor(self, kanaal, niveau, wat, object_id, actie, van, naar, reden, kans=''):
        if (object_id, actie) in self.open:
            return
        self.open.add((object_id, actie))
        self.voorstellen.append({'kanaal': kanaal, 'niveau': niveau, 'wat': wat, 'object': object_id,
                                 'actie': actie, 'van': van, 'naar': naar, 'reden': reden,
                                 'kans': '' if kans == '' else f'{kans:.0%}'})

    # ---------- KPI's ----------

    def kpi(self):
        g, m = self.d['google'], self.d['meta']

        def kosten(van, tot):
            k = sum(_som(_dagen(c['dagen'], van, tot), 'kosten') for c in g['campagnes'])
            return k + sum(_som(_dagen(a['dagen'], van, tot), 'kosten') for a in m['ads'])

        uit = {}
        for naam, van in (('gisteren', self.gisteren), ('7 dagen', self._dag(7)), ('14 dagen', self._dag(14)),
                          ('totaal', self.start)):
            van = max(van, self.start)
            k = kosten(van, self.gisteren)
            alle = self._orders(van=van)
            omzet = sum(o['omzet'] for o in alle)
            betaald = [o for o in alle if o['kanaal'] in ('google', 'meta')]
            uit[naam] = {
                'kosten': round(k, 2), 'orders': len(alle), 'betaald': len(betaald), 'omzet': round(omzet, 2),
                'mer': round(omzet / k, 2) if k else None,
                'cpa': round(k / len(alle), 2) if alle else None,
                'bijdrage_na_ads': round(len(alle) * self.bijdrage - k, 2),
                'kans_test': round(self._kans(len(alle), k, self.c['test_roas']), 3),
                'kans_breakeven': round(self._kans(len(alle), k, self.c['breakeven_roas']), 3)}
        return uit

    # ---------- regels ----------

    def regels(self):
        k = self.kpi()
        self._verliesgrenzen(k)
        self._kanalen()
        self._google_campagnes()
        self._google_zoekwoorden_producten()
        self._meta_ads()
        self._signalen()
        return k

    def _verliesgrenzen(self, k):
        totaal_verlies = -k['totaal']['bijdrage_na_ads']
        week_verlies = -k['7 dagen']['bijdrage_na_ads']
        if totaal_verlies > self.c['verlies_totaal']:
            self.vlaggen.append(f"Cumulatief verlies €{totaal_verlies:.0f} boven de grens van "
                                f"€{self.c['verlies_totaal']:.0f}: alles pauzeren behalve wat zelf onder break-even zit.")
            for c in self.d['google']['campagnes']:
                if c['status'] == 'ENABLED' and not self._onder_breakeven_google(c):
                    self.stel_voor('Google', 'campagne', c['naam'], c['id'], 'pauze', 'aan', 'pauze',
                                   'Verliesgrens totaal bereikt (€300).')
            for s in self.d['meta']['adsets']:
                if s['status'] == 'ACTIVE':
                    self.stel_voor('Meta', 'advertentieset', s['naam'], s['id'], 'pauze', 'aan', 'pauze',
                                   'Verliesgrens totaal bereikt (€300).')
        if week_verlies > self.c['verlies_week']:
            vorige = self._weekverlies_vorige_week()
            tekst = f"Weekverlies €{week_verlies:.0f} boven €{self.c['verlies_week']:.0f}."
            if vorige is not None and vorige > self.c['verlies_week']:
                tekst += ' Twee weken op rij: Meta terug naar €2 tot €3 per dag of pauze.'
                for s in self.d['meta']['adsets']:
                    if s['status'] == 'ACTIVE' and s['budget'] > 3:
                        naar = max(round(s['budget'] * (1 - self.c['max_stap_omlaag']), 2), 3)
                        self.stel_voor('Meta', 'advertentieset', s['naam'], s['id'], 'budget', s['budget'], naar,
                                       'Weekverlies twee weken op rij boven €75.')
            self.vlaggen.append(tekst)

    def _weekverlies_vorige_week(self):
        van, tot = self._dag(14), self._dag(8)
        if van < self.start:
            return None
        k = sum(_som(_dagen(c['dagen'], van, tot), 'kosten') for c in self.d['google']['campagnes'])
        k += sum(_som(_dagen(a['dagen'], van, tot), 'kosten') for a in self.d['meta']['ads'])
        return k - len(self._orders(van=van, tot=tot)) * self.bijdrage

    def _onder_breakeven_google(self, c):
        kosten = _som(_dagen(c['dagen'], self.start, self.gisteren), 'kosten')
        n = max(len(self._orders('google', c['id'])), _som(_dagen(c['dagen'], self.start, self.gisteren), 'conv'))
        return n > 0 and kosten / n <= self.bijdrage

    def _kanalen(self):
        grens = self.c['kanaal_zonder_aankoop']
        g_kosten = sum(_som(_dagen(c['dagen'], self.start, self.gisteren), 'kosten')
                       for c in self.d['google']['campagnes'])
        g_conv = sum(_som(_dagen(c['dagen'], self.start, self.gisteren), 'conv') for c in self.d['google']['campagnes'])
        if g_kosten >= grens and not self._orders('google') and g_conv == 0:
            for c in self.d['google']['campagnes']:
                if c['status'] == 'ENABLED':
                    self.stel_voor('Google', 'campagne', c['naam'], c['id'], 'pauze', 'aan', 'pauze',
                                   f'Google heeft €{g_kosten:.0f} uitgegeven zonder één aankoop (grens €{grens:.0f}).')
        m_kosten = sum(_som(_dagen(a['dagen'], self.start, self.gisteren), 'kosten') for a in self.d['meta']['ads'])
        m_conv = sum(_som(_dagen(a['dagen'], self.start, self.gisteren), 'conv') for a in self.d['meta']['ads'])
        if m_kosten >= grens and not self._orders('meta') and m_conv == 0:
            wagens = sum(_som(_dagen(a['dagen'], self.start, self.gisteren), 'winkelwagen') for a in self.d['meta']['ads'])
            for s in self.d['meta']['adsets']:
                if s['status'] == 'ACTIVE':
                    if wagens >= 8:
                        self.notities.append('Meta: €125 zonder aankoop maar 8+ winkelwagens. Volgens het plan '
                                             'één keer overstappen op optimaliseren voor Toevoegen aan winkelwagen '
                                             '(Joost beslist, 14 dagen laten staan).')
                    else:
                        self.stel_voor('Meta', 'advertentieset', s['naam'], s['id'], 'pauze', 'aan', 'pauze',
                                       f'Meta heeft €{m_kosten:.0f} uitgegeven zonder één aankoop (grens €{grens:.0f}).')

    def _google_campagnes(self):
        totaal_budget = self._totaal_budget()
        for c in self.d['google']['campagnes']:
            if c['status'] != 'ENABLED':
                continue
            alle = _dagen(c['dagen'], self.start, self.gisteren)
            kosten = _som(alle, 'kosten')
            shop = len(self._orders('google', c['id']))
            platform = _som(alle, 'conv')
            # pauzeren met het voordeel van de twijfel (hoogste telling), opschalen alleen op Shopify
            k_pauze = max(shop, platform)
            p_test = self._kans(k_pauze, kosten, self.c['test_roas'])
            if kosten >= 2 * self.bijdrage and p_test < self.c['kans_pauze']:
                self.stel_voor('Google', 'campagne', c['naam'], c['id'], 'pauze', 'aan', 'pauze',
                               f'€{kosten:.0f} uitgegeven, {k_pauze:.0f} aankopen: kans op ROAS > '
                               f"{self.c['test_roas']} is {p_test:.0%}.", p_test)
                continue
            d14 = _dagen(c['dagen'], max(self._dag(14), self.start), self.gisteren)
            k14 = _som(d14, 'kosten')
            o14 = self._orders('google', c['id'], van=max(self._dag(14), self.start))
            omzet14 = sum(o['omzet'] for o in o14)
            roas14 = omzet14 / k14 if k14 else 0
            p_be = self._kans(len(o14), k14, self.c['breakeven_roas'])
            verloren = max((v.get('verlies_budget', 0) for v in _dagen(c['dagen'], self._dag(7), self.gisteren).values()),
                           default=0)
            if (len(o14) >= self.c['opschaal_min_orders_14d'] and roas14 >= self.c['opschaal_roas']
                    and p_be >= self.c['kans_opschalen'] and verloren > 0.2 and self._mag_wijzigen(c['id'])):
                naar = round(c['budget'] * (1 + self.c['max_stap_omhoog']), 2)
                ruimte = self.c['plafond_dagbudget_totaal'] - totaal_budget
                naar = min(naar, round(c['budget'] + max(ruimte, 0), 2))
                if naar > c['budget']:
                    self.stel_voor('Google', 'campagne', c['naam'], c['id'], 'budget', c['budget'], naar,
                                   f'{len(o14)} orders en ROAS {roas14:.1f} in 14 dagen; {verloren:.0%} vertoningen '
                                   f'verloren door budget.', p_be)

    def _totaal_budget(self):
        g = sum(c['budget'] for c in self.d['google']['campagnes'] if c['status'] == 'ENABLED')
        m = sum(s['budget'] for s in self.d['meta']['adsets'] if s['status'] == 'ACTIVE')
        m += sum(c['budget'] for c in self.d['meta']['campagnes'] if c['status'] == 'ACTIVE')
        return g + m

    def _google_zoekwoorden_producten(self):
        omlaag, pauze, klikken = (self.c['zoekwoord_bod_omlaag'], self.c['zoekwoord_pauze'],
                                  self.c['zoekwoord_pauze_klikken'])
        items = [('zoekwoord', z, f"[{z['match'].lower()}] {z['tekst']}") for z in self.d['google']['zoekwoorden']]
        items += [('product', p, p.get('titel') or p['item']) for p in self.d['google']['producten']
                  if p.get('rn') and p.get('status') == 'ENABLED']
        for niveau, z, naam in items:
            if z['conv'] > 0:
                continue
            if z['kosten'] >= pauze or z['klik'] >= klikken:
                self.stel_voor('Google', niveau, naam, z['rn'], 'pauze', 'aan', 'pauze',
                               f"€{z['kosten']:.2f} en {z['klik']:.0f} klikken zonder aankoop.")
            elif z['kosten'] >= omlaag and self._mag_wijzigen(z['rn']):
                bod = z.get('bod') or 0
                if bod:
                    self.stel_voor('Google', niveau, naam, z['rn'], 'bod', bod, round(bod * 0.7, 2),
                                   f"€{z['kosten']:.2f} zonder aankoop: bod −30%.")

    def _meta_ads(self):
        c = self.c
        for a in self.d['meta']['ads']:
            if a.get('status') != 'ACTIVE':
                continue
            alle = _dagen(a['dagen'], self.start, self.gisteren)
            kosten, vert, klik = _som(alle, 'kosten'), _som(alle, 'vert'), _som(alle, 'klik')
            conv, wagens, v3 = _som(alle, 'conv'), _som(alle, 'winkelwagen'), _som(alle, 'video3s')
            shop = len([o for o in self._orders('meta') if o.get('content') == a['naam']])
            aankopen = max(conv, shop)
            ctr = klik / vert if vert else 0
            cpc = kosten / klik if klik else None
            reden = None
            if kosten >= c['meta_plafond_euro'] and shop == 0 and conv == 0:
                reden = f'€{kosten:.0f} zonder aankoop in Shopify (plafond 3 × CPA).'
            elif kosten >= c['meta_aankoop_euro'] and aankopen == 0 and wagens < 2:
                reden = f'€{kosten:.0f}, geen aankoop en {wagens:.0f} winkelwagens.'
            elif kosten >= c['meta_klik_euro'] and cpc and cpc > c['meta_max_cpc'] and ctr < 0.008:
                reden = f'CPC €{cpc:.2f} en link-CTR {ctr:.2%}.'
            elif kosten >= c['meta_aandacht_euro'] or vert >= 1000:
                if ctr < c['meta_min_ctr']:
                    reden = f'link-CTR {ctr:.2%} onder {c["meta_min_ctr"]:.1%}.'
                elif a.get('video') and vert and v3 / vert < c['meta_min_hookrate']:
                    reden = f'3-secondenratio {v3 / vert:.0%} onder {c["meta_min_hookrate"]:.0%}.'
            if reden:
                self.stel_voor('Meta', 'advertentie', a['naam'], a['id'], 'pauze', 'aan', 'pauze', reden)

    def _signalen(self):
        g = self.d['google']
        for x in g.get('afgekeurd', []):
            self.vlaggen.append(f"Google-advertentie {x['ad']} in {x['campagne']} heeft status {x['status']}.")
        # budgettempo deze maand
        maand = self.gisteren[:8] + '01'
        for c in g['campagnes']:
            if c['status'] != 'ENABLED':
                continue
            k = _som(_dagen(c['dagen'], maand, self.gisteren), 'kosten')
            dagen = (dt.date.fromisoformat(self.gisteren) - dt.date.fromisoformat(max(maand, self.start))).days + 1
            if dagen > 0 and k > c['budget'] * dagen * 1.15:
                self.vlaggen.append(f"{c['naam']}: €{k:.2f} uitgegeven, meer dan budget × {dagen} dagen.")
        # site: sessies zonder verkoop
        s7 = _dagen(self.d['shopify']['sessies'], self._dag(7), self.gisteren)
        sessies = sum(v['sessies'] for v in s7.values())
        if sessies >= 150 and not self._orders(van=self._dag(7)):
            self.vlaggen.append(f'{sessies} sessies in 7 dagen zonder bestelling: productpagina en checkout nalopen.')
        cl = self.d.get('clarity') or {}
        for sleutel, naam in (('RageClickCount', 'woedeklikken'), ('ScriptErrorCount', 'scriptfouten'),
                              ('DeadClickCount', 'dode klikken')):
            if (cl.get('sessies') or 0) >= 20 and (cl.get(sleutel) or 0) >= 10:
                self.vlaggen.append(f'Clarity: {cl[sleutel]:.0f}% van de sessies heeft {naam}.')
        # zoektermen voor de agent om te beoordelen (passend of uitsluiten)
        self.te_beoordelen = sorted(
            [t for t in g['zoektermen'] if t['klik'] > 0 and t['conv'] == 0 and t.get('status') not in ('EXCLUDED',)],
            key=lambda t: -t['kosten'])[:40]


def mijlpaal(cfg, vandaag, orders, uitgave):
    """Oordeel volgens de beslistabel op dag 7, 14 en 28 na de start van fase 1."""
    start = cfg.get('start_fase1')
    if not start:
        return None
    dag = (dt.date.fromisoformat(vandaag) - dt.date.fromisoformat(str(start))).days
    if dag not in (7, 14, 28):
        return None
    if dag == 7:
        oordeel = ('rode vlag: meting, productpagina en checkout nalopen' if orders <= 1 else
                   'goed teken, wachten op dag 14' if orders >= 8 else 'niets wijzigen, te weinig data')
    elif dag == 14:
        oordeel = ('stoppen: Meta uit, Google terug naar €10' if orders <= 3 else
                   'afschalen: Meta naar €3 of pauze' if orders <= 7 else
                   'doorgaan op €20, verliezers eruit' if orders <= 14 else 'opschalen naar €25 (stap 2)')
    else:
        oordeel = ('stoppen en aannames herzien' if orders <= 9 else
                   'afschalen naar Google-only €10 tot €15' if orders <= 16 else
                   'doorgaan, Q4 op €20 tot €25' if orders <= 27 else 'opschalen volgens de stappen')
    return f'Dag {dag} van fase 1: {orders} orders bij €{uitgave:.0f} uitgave. Beslistabel: {oordeel}.'
