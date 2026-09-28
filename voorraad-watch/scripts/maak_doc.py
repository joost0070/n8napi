import json, html
u = json.load(open('uitverkoop.json'))
e = lambda s: html.escape(str(s if s is not None else ''))
eur = lambda n: '€ ' + f"{round(n):,}".replace(',', '.')
KL = {'LEEG': '#9B1C1C', 'TE LAAT': '#B42318', 'BESTEL NU': '#B54708', 'VOLGENDE WEEK': '#8A6D00', 'OK': '#2E6B45'}
st = lambda s: f'<b style="color:{KL.get(s,"#333")}">{e(s)}</b>'
dg = lambda d, v=None: 'leeg' if v == 0 else ('> 1 jaar' if d is None else f"{round(d)} d")
TH = 'style="background:#eeeeee;text-align:left"'
def tabel(kop, rijen):
    h = '<table border="1" cellpadding="4" style="border-collapse:collapse;width:100%">'
    h += '<tr>' + ''.join(f'<th {TH}>{k}</th>' for k in kop) + '</tr>'
    for r in rijen: h += '<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>'
    return h + '</table>'

H = []
H.append(f"""<h1>Voorraad Watch – week {u['week']} (peildatum 28 september 2026)</h1>
<p><i>Hooijer Footwear Group. Alle 17 webshops plus marktplaatsen via ChannelEngine. Verkoop = laatste 28 dagen, voorraad = stand van vandaag.
Eenmalig document; de wekelijkse versie komt per mail uit n8n zodra de workflow is geïmporteerd.</i></p>""")

# 1. deze week doen
sig = u['signalen']
H.append("<h2>1. Wat moet er deze week gebeuren</h2><ol>")
H.append("""<li><b>Hunter bijbestellen, nu.</b> Downpour Tall Black (maat 36 is leeg, 37 over ~5 dagen, 38 over ~16 dagen; alleen 36–39 nabestellen), Women's Original Tall Black
en Gloss Military Red. Hunter verkoopt ~2,5–3× vorig jaar; bij deze modellen zelfs 11–16× dezelfde weken vorig jaar.
Gemeten hersteltijd Hunter: 4 weken. Alles wat nu leeg gaat, is dat tot eind oktober.</li>""")
H.append("""<li><b>Tofvel Mula vóór de piek aanvullen.</b> Het Tofvel-seizoen piekt in november/december (week 46–51). Marbled Brown is in de kernmaten
38–40 over ~5 dagen leeg en was het afgelopen jaar maar 27% van de tijd volledig leverbaar (geschat ~€ 81.000 omzet gemist).
Mula Black en Olive Green volgen binnen 2–5 weken.</li>""")
H.append("""<li><b>Bevestig de "sprongen".</b> Bij modellen die nu ≥ 4× vorig jaar verkopen staat in de lijst hieronder een oranje markering. Is het echte
groei, dan bestellen; is het een actie of lancering, dan voorzichtiger.</li>""")
H.append("""<li><b>Laatste paren naar de eigen shops.</b> 18% van de verkoop liep de afgelopen 28 dagen via marktplaatsen (fee gemiddeld 13,9%, Amazon 18%).
Bij een kernmaat op "te laat": marktplaatsvoorraad in ChannelEngine afknijpen.</li></ol>""")
H.append(f"<p>Totaal: <b>{u['n_signalen']} modellen met een signaal</b> – {u['signalen_per_status'].get('LEEG',0)} leeg, "
         f"{u['signalen_per_status'].get('TE LAAT',0)} te laat, {u['signalen_per_status'].get('BESTEL NU',0)} bestel nu. Alleen modellen die zelf op volle prijs staan.</p>")

# 2. top 10
H.append("<h2>2. Top 10 best verkocht – resterende dagen voorraad per kernmaat</h2>")
H.append("<p>Kernmaten = de maten die samen 80% van de vraag dragen. Dagen = verwachte dagen tot die maat op is, langs de seizoenscurve van het model.</p>")
rij = []
for i, t in enumerate(u['top10'], 1):
    km = ' · '.join(f"{e(m['maat'])}: {dg(m['dagen'], m['vrd'])}" for m in t['maten'] if m['kern'])
    kan = t['kanaal']; tot = sum(kan.values()) or 1
    col = e(t['collectie']) + (' <i>(label ' + e(t['seizoen']) + ', volle prijs)</i>' if t['collectie'] == 'doorloper' else '')
    rij.append([i, f"<b>{e(t['merk'])}</b> {e(t['naam'])}", col, t['verk28'], t['voorraad'], km,
                f"{st(t['status'])}<br>hersteltijd {t['levertijd']} wk",
                f"{round(100*kan['merkshop']/tot)}% / {round(100*kan['breed']/tot)}% / {round(100*kan['marktplaats']/tot)}%"])
H.append(tabel(['#', 'Artikel', 'Collectie', 'Verkocht 28 d', 'Voorraad', 'Kernmaten: dagen tot leeg', 'Status', 'Merkshop / breed / marktplaats'], rij))

# 3. signalen
H.append("<h2>3. Bijschakelen – de 25 belangrijkste signalen</h2>")
H.append("""<p>Volgorde: leeg en te laat eerst, gesorteerd op de omzet die binnen de hersteltijd misloopt. "Voorstel" dekt hersteltijd + 8 weken
voor de kernmaten die krap zijn. "Controle" zet dat naast wat vorig jaar in dezelfde weken verkocht werd.</p>""")
rij = []
for s in sig[:25]:
    krap = [m for m in s['maten'] if m['kern'] and m['status'] in ('LEEG', 'TE LAAT', 'BESTEL NU')]
    ctl = f"vorig jaar {s['vj_horizon']} · nu verwacht {s['verwacht_horizon']}"
    if s['sprong']: ctl += f"<br><b style='color:#B54708'>{str(s['sprong']).replace('.', ',')}× vorig jaar – eerst bevestigen</b>"
    elif s['weinig_historie']: ctl += "<br><span style='color:#8A6D00'>weinig historie</span>"
    rij.append([st(s['status']), f"<b>{e(s['merk'])}</b> {e(s['naam'])}<br><i>{e(s['collectie'])}</i>",
                '<br>'.join(f"{e(m['maat'])}: {dg(m['dagen'], m['vrd'])}" for m in krap), s['verk28'],
                '<br>'.join(f"{e(m['maat'])}: {m['bestel']}" for m in krap) + f"<br><i>totaal {s['bestel_totaal']}</i>",
                ctl, eur(s['mis_eur'])])
H.append(tabel(['Status', 'Artikel', 'Krappe maten', 'Verkocht 28 d', 'Voorstel', 'Controle', 'Mist binnen hersteltijd'], rij))

# 4. Hunter
H.append("""<h2>4. Hunter is dit jaar uitzonderlijk</h2>
<p>Paren per week, alle kanalen samen:</p>""")
H.append(tabel(['Week', '34', '35', '36', '37'], [['2025', 61, 112, 97, 128], ['2026', 297, 228, 314, 367]]))
H.append("""<p>De Hunter-shop deed in de eerste twee septemberweken 488 paar (€ 50.300 incl. btw), tegen 138 paar een jaar eerder.
Hunter heeft maar één eerder seizoen (2025, geen 2024), dus alles wat op "vorig jaar" leunt, schiet tekort. Wat de radar daarvoor doet:</p>
<ul><li>Het tempo komt uit de laatste 28 dagen, niet uit vorig jaar. De groei zit er dus al in.</li>
<li>De sprong eind augustus wordt niet meer als seizoenspiek gelezen. Zonder die correctie leek het Hunter-seizoen voorbij, terwijl het net begint.</li>
<li>Het plafond op de verwachte vraag schaalt mee met de gemeten merkgroei (Hunter 2,6×, Keen 2,6×, Tofvel 2,4×, HEYDUDE 1,9×).</li></ul>
<p><b>Correctie op 14 september:</b> het dashboard adviseerde Downpour Tall in maat 40/41 "nu afprijzen". Het overschot klopt: 40 en 41 hebben
elk ~180 paar, ruim een jaar voorraad, terwijl 36 al leeg is en 37/38 binnen drie weken volgen. Het middel was fout. Het rekende met het
12-maandstempo en miste de sprong van eind augustus. Een korting op de nummer 1 kost marge op paren die je toch verkoopt.
Beter: niet afprijzen, bij de nabestelling alleen 36–39, en 40/41 laten lopen (eventueel via de marktplaatsen).</p>""")

# 5. seizoen per merk
H.append("""<h2>5. Seizoen per merk – wanneer piekt het, wanneer afprijzen</h2>""")
H.append(tabel(['Merk', 'Verkoopseizoen', 'Piek', 'Wat het nu betekent (week 40)'], [
    ['Tofvel', 'okt – jan; lente en zomer bijna nul', 'nov/dec (wk 46–51)', 'Voorraad moet nú staan: een lege maat in oktober kost de hele piek. Groei 2,4×.'],
    ['Hunter', 'sep – dec', 'okt (wk 40–41 in 2025)', 'Loopt al 2,5–3× vorig jaar. Bijbestellen met 4 weken hersteltijd.'],
    ['Sockwell', 'vlak door het jaar', 'Black Friday (wk 48): 3–5× een normale week', 'Doorlopend. Kernmaten van bestsellers op Black Friday voorbereiden.'],
    ['HEYDUDE', 'zomer, mei – aug', 'eind juni / juli', 'Zomer voorbij; alleen doorlopers en de wintermodellen (Wally GripR Warmth) bijbestellen.'],
    ['Lazamani', 'zomer, apr – aug', 'eind juni / juli', 'Seizoen voorbij; restvoorraad afprijzen, niet bijkopen.'],
    ['Keen', 'lente en zomer, najaar tweede golf', 'mei/juni', 'Groei 2,6× in de laatste 6 weken: winterschoenen in de gaten houden.'],
    ['Toni Pons', 'zomer (espadrilles) + winter (pantoffels)', 'juni/juli, nov/dec', 'Mona-FR/Neo-FR pantoffels lopen, maar staan in de korting: niet bijkopen.'],
    ['Bartogi (breed + marktplaatsen)', 'volgt de merken', 'zomer, tweede top rond Black Friday', '—'],
]))
H.append("""<p><b>Afprijzen</b>: per model begint dat in de week waarin 70% van de seizoensvraag achter de rug is. Een collectie
(merk × seizoen × jaar) waarvan minstens 45% van de maten al een van-prijs heeft, wordt als "in de sale" gemarkeerd. Of er bijbesteld wordt,
beslist de prijs van het model zelf: staat de helft van de maten in de korting, dan geen voorstel.</p>
<p><b>Acties</b> die vorig jaar niet plaatsvonden, staan niet in de historie. Een geplande actie (Black Friday-aanbod, merkactie) moet
daarom als input in de merk-config, anders ziet de radar de piek pas als hij al begonnen is.</p>""")

# 6. collectie
tv = sum(u['verkoop_per_collectie'].values())
pc = {k: round(100 * v / tv) for k, v in u['verkoop_per_collectie'].items()}
H.append("<h2>6. Ouder seizoen of dit seizoen? Waar de verkoop nu vandaan komt</h2>")
H.append(tabel(['Collectie', 'Aandeel verkoop laatste 28 d', 'Besteladvies'], [
    ['Lopend (FW 2026)', f"{pc.get('lopend',0)}%", 'ja'],
    ['Doorlopend (NOOS of vlakke jaarcurve)', f"{pc.get('doorlopend',0)+pc.get('lopend?',0)}%", 'ja'],
    ['Doorloper (ouder label, volle prijs, verkoopt)', f"{pc.get('doorloper',0)}%", 'ja – nieuw deze week'],
    ['Vorig jaar / net voorbij / ouder', f"{pc.get('vorig jaar',0)+pc.get('net voorbij',0)+pc.get('ouder',0)}%", 'nee – afprijsbeeld'],
    ['Geen seizoenslabel', f"{pc.get('geen label',0)}%", 'ja, gemarkeerd'],
]))
H.append("""<p>Maar 6% van de verkoop komt uit de "lopende" collectie FW 2026. Het seizoensjaar in de artikelstam is het introductiejaar, niet
of een artikel nog loopt. Bijna de helft van de verkoop heeft helemaal geen seizoenslabel: vooral Sockwell (~70% daarvan), Tofvel (~15%) en Hunter (~10%).
<b>Actie:</b> seizoensjaar en NOOS aanvullen in ChannelEngine, te beginnen bij Sockwell. Tot die tijd beslist het verkooppatroon van het artikel zelf.</p>""")

# 7. kanalen
k = u['kanalen']; kt = sum(k.values())
H.append("<h2>7. Kanalen: eigen merkshop, Bartogi en marktplaatsen</h2>")
H.append(f"""<p>Er is één voorraad, gespiegeld naar alle shops. Die telt de radar één keer; de vraag telt hij over alle kanalen op.
Laatste 28 dagen: merkshops {round(100*k['merkshop']/kt)}%, Bartogi.nl/.de {round(100*k['breed']/kt)}%, marktplaatsen {round(100*k['marktplaats']/kt)}%.</p>""")
H.append(tabel(['Kanaal', 'Fee'], [[e(a), f"{b}%".replace('.', ',')] for a, b in sorted(u['fee_per_kanaal'].items(), key=lambda x: -x[1]) if b > 0]))
H.append("<p>Bij krapte zijn de laatste paren in de eigen shop meer waard: geen fee, en minder retour.</p>")

# 8. hersteltijd
H.append("<h2>8. Hersteltijd per merk – gemeten</h2>")
H.append("<p>Hoe lang stond een lege maat van een bestseller leeg voordat hij terugkwam (mediaan, uit de weekhistorie in Shopify). Dit is de horizon van het signaal, zolang de leverancier geen levertijd opgeeft.</p>")
H.append(tabel(['Merk', 'Hersteltijd', 'Leegstanden gemeten', 'Niet terug binnen 20 weken'],
    [[e(m), f"{v['weken']} wk", v['n'], u['nooit_hersteld'].get(m, 0)] for m, v in sorted(u['herstel'].items(), key=lambda x: x[1]['weken']) if v['n'] >= 15]))
H.append("<p>Tofvel valt op: als een maat terugkomt, is dat snel (2 weken), maar bijna één op de drie lege maten kwam helemaal niet terug.</p>")

# 9. terugblik
tb = u['terugblik']
H.append("<h2>9. Terugblik: hoe groot is de valkuil</h2>")
H.append(f"""<p>De 50 best verkopende modellen van het afgelopen jaar waren gemiddeld {tb['gem_leverbaar']}% van de tijd volledig leverbaar;
{tb['nooit_leeg']} stonden nooit leeg. Geschat gemist: <b>{f"{tb['gemist_st']:,}".replace(',', '.')} stuks, {eur(tb['gemist_omzet'])} omzet</b>
(bruto, bij het jaargemiddelde tempo; indicatie, geen boekhouding).</p>""")
H.append(tabel(['Model', 'Verkocht 12 mnd', 'Leverbaar', 'Geschat gemist'],
    [[f"<b>{e(t['merk'])}</b> {e(t['naam'])}", t['verkocht'], f"{t['leverbaar_pct']}%", eur(t['gemist_omzet'])] for t in tb['slechtst'][:8]]))

# 10. methode + nodig
H.append("""<h2>10. Hoe de radar rekent (kort)</h2><ol>
<li><b>Tempo</b>: verkoop laatste 28 dagen over alle kanalen, gedeeld door de dagen dat het model leverbaar was.</li>
<li><b>Ontseizoenen</b>: gedeeld door het seizoensgewicht van die 4 weken → jaarniveau. De groei van het merk zit er zo al in.</li>
<li><b>Vooruit afboeken</b>: week voor week de verwachte vraag (jaarniveau × seizoensgewicht × maataandeel) van de voorraad af → de dag dat de maat op is.</li>
<li><b>Signaal</b>: leeg vóór de hersteltijd = te laat; binnen hersteltijd + 2 weken = bestel nu. Een model krijgt de status van zijn slechtste kernmaat.</li>
<li><b>Controle</b>: elk voorstel naast vorig jaar dezelfde weken; sprongen en weinig historie worden gemarkeerd.</li></ol>
<p>Beperkingen: vraag is bruto (retouren niet afgetrokken, dus het signaal komt eerder, niet later). Merken met één eerder seizoen (Hunter) hebben een
minder zekere curve. Prijzen komen uit de export van 14 september.</p>
<h2>11. Wat ik van jullie nodig heb</h2><ol>
<li><b>Levertijd en nabestelbaarheid per merk</b> (de leveranciersvraag staat klaar). Tot die tijd rekent de radar met de gemeten hersteltijd.</li>
<li><b>Geplande acties</b> per merk en week (Black Friday, merkacties): die staan niet in de historie van vorig jaar.</li>
<li><b>Seizoensjaar en NOOS aanvullen</b> in ChannelEngine, vooral Sockwell, Tofvel en Hunter.</li>
<li><b>Akkoord om de n8n-workflow te importeren</b> als nieuwe, losse workflow. Bestaande workflows worden niet aangeraakt.
Daarna komt dit rapport elke maandag, en op andere dagen alleen als een bestseller leeg of te laat dreigt.</li></ol>""")
open('doc_week40.html', 'w').write('<html><head><meta charset="utf-8"></head><body style="font-family:Arial">' + ''.join(H) + '</body></html>')
print(len(''.join(H)))
