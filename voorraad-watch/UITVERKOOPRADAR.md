# Uitverkoopradar

Doel: automatisch signaleren wanneer een best verkopend artikel uit voorraad gaat
lopen, op een moment dat bijbestellen nog op tijd landt.

Dit vervangt niet de rest van de Voorraad Watch, maar zet één vraag voorop:
**op welke dag is deze maat op, en is dat vóór of na het moment dat nieuwe
voorraad binnen kan zijn?**

---

## Waarom "dagen voorraad" alleen niet genoeg is

De gebruikelijke rekensom is `voorraad / gemiddelde verkoop per dag`. Die gaat bij
schoenen op drie manieren mis:

1. **Het seizoen.** 100 paar winterlaarzen in week 40 gaan niet even snel als in
   week 48. Een vlak gemiddelde zegt "ruim voldoende" terwijl de piek nog moet
   komen, en in maart het omgekeerde.
2. **Uitverkochte weken.** Een maat die de helft van de maand leeg stond,
   verkocht de helft minder — niet omdat de vraag lager was, maar omdat er niets
   te verkopen viel. Dan lijkt de vraag laag en komt het signaal te laat.
3. **Kleine aantallen per maat.** Een maat met twee verkopen in vier weken geeft
   geen betrouwbaar eigen tempo.

## De methode

Per **model** (artikel + kleur), daarna verdeeld over de maten.

### 1. Recent tempo, gecorrigeerd voor leegstand

```
verkocht laatste 28 dagen, alle kanalen
------------------------------------------   x 7  =  tempo per week
dagen dat het model leverbaar was
```

"Leverbaar" komt uit ShopifyQL (`days_out_of_stock` per maat), gewogen naar hoe
belangrijk de maat is: als maat 39 leeg stond telt dat zwaarder dan maat 46.

### 2. Ontseizoenen

Het tempo van de afgelopen vier weken wordt gedeeld door het seizoensgewicht van
die vier weken. Dat geeft het **jaarniveau** van het model: hoeveel het zou
verkopen als het het hele jaar leverbaar was.

Omdat dit uit de *recente* weken komt, zit de groei of krimp van het merk er al
in. Een aparte momentumfactor is niet meer nodig.

### 3. Herseizoenen en afboeken

Week voor week vooruit: verwachte vraag = jaarniveau × seizoensgewicht van die
week × aandeel van de maat. Dat wordt van de voorraad afgehaald tot die op is.
**Die dag is de verwachte uitverkoopdatum.**

Het seizoensgewicht komt van het model zelf (kleurvariant), anders van de
modelfamilie, anders van merk × seizoen — twee volledige jaarcycli, elk apart
genormaliseerd.

**Niveausprong aan het eind van de cyclus.** Hunter verkocht eind augustus 2026
ineens 2,5 à 3× zoveel als een jaar eerder (week 34: 297 paar tegen 61). Die
weken vallen nog in de laatste cyclus. Zonder correctie leest de curve die sprong
als seizoenspiek, en lijkt het seizoen voorbij terwijl het net begint. De laatste
acht weken van de cyclus worden daarom teruggerekend naar het niveau van de rest,
met de gemeten merkgroei (laatste 6 weken tegen dezelfde 6 weken vorig jaar),
zodra die buiten 0,77–1,3× valt. Ook wordt niet meer gladgestreken over de naad
tussen eind augustus en begin september.

**Plafond.** Het jaarniveau mag hoogstens 2,5× het gemeten 12-maandstempo zijn,
vermenigvuldigd met de merkgroei. Zonder die vermenigvuldiging zou een merk dat
echt verdrievoudigt worden afgeknepen.

### 4. Maatverdeling

Uit de eigen verkoophistorie van het model, waarbij de laatste 28 dagen drie
keer zo zwaar tellen, en de maatcurve van het merk als achtergrond voor maten met
weinig waarneming. Een nieuw model zonder historie krijgt zo toch een
realistische verdeling.

### 5. Signaal

| Status | Wanneer | Betekenis |
|---|---|---|
| **Leeg** | voorraad 0, er is vraag | er wordt nu omzet gemist |
| **Te laat** | leeg vóór de hersteltijd voorbij is | ook een bestelling van vandaag komt na het gat |
| **Bestel nu** | leeg binnen hersteltijd + 2 weken marge | nu bestellen landt precies op tijd |
| **Volgende week** | leeg binnen hersteltijd + 4 weken | in de gaten houden |
| OK | later | — |

Een model krijgt de status van zijn slechtste **kernmaat**: de maten die samen
80% van de vraag dragen. Een lege randmaat maakt het model niet rood.

**Volgorde in het rapport.** Leeg en te laat samen, gesorteerd op de omzet die
binnen de hersteltijd misloopt; daarna bestel-nu op volume. Eerder stonden alle
lege artikelen bovenaan, ook met drie verkopen, en de best verkochte laars die
over vijf dagen op is daaronder.

**Controle naast elk voorstel.** Bij elk signaal staat wat er vorig jaar in
dezelfde weken verkocht werd (de komende hersteltijd + 8 weken) naast wat er nu
verwacht wordt. Twee markeringen:

- **Sprong**: de laatste 28 dagen verkochten minstens 4× zoveel als dezelfde 28
  dagen vorig jaar. Dat kan echte groei zijn (Hunter), een lancering of een actie.
  Eerst bevestigen, dan bestellen.
- **Weinig historie**: minder dan 30 stuks in 12 maanden, of minder dan 20 vorig
  jaar in dezelfde weken. Voorzichtig bestellen.

### 6. Hersteltijd per merk — gemeten, niet aangenomen

Uit de weekhistorie in ShopifyQL: hoe lang stond een uitverkochte maat leeg
voordat hij terugkwam? De mediaan per merk is de **werkelijke hersteltijd**:
reactietijd plus levertijd samen. Dat is wat telt voor een signaal — niet wat de
leverancier belooft, maar hoe lang het bij jullie in de praktijk duurt.

Leegstand die langer dan twintig weken duurde telt apart: dat artikel is binnen
het seizoen nooit meer aangevuld.

Zodra een leverancier een echte levertijd opgeeft, gaat die voor.

Gemeten in september 2026 (voorgevuld in `config/merk-config.template.csv`,
kolom `hersteltijd_weken`):

| Merk | Hersteltijd | Leegstanden | Niet terug binnen 20 wk |
|---|---|---|---|
| Tofvel | 2 wk | 216 | 91 |
| Lazamani | 2 wk | 213 | 24 |
| Hunter | 4 wk | 140 | 17 |
| Keen | 4 wk | 25 | 2 |
| HEYDUDE | 7 wk | 383 | 33 |
| Sockwell | 7 wk | 89 | 9 |
| Toni Pons | 9 wk | 19 | 9 |

Tofvel valt op: als een maat terugkomt is dat snel, maar bijna één op de drie
lege maten kwam helemaal niet terug.

---

## Collectie, seizoen en afprijzen

### Welke collectie loopt nu

| Collectie | In week 40 van 2026 | Signaal |
|---|---|---|
| **Lopend** | FW 2026 | volledig: bestellen als het op dreigt te raken |
| **Doorlopend** | NOOS, of een vlakke jaarcurve | volledig |
| **Net voorbij** | SS 2026 | geen besteladvies, wel restvoorraad bij seizoenseinde |
| **Vorig jaar** | FW 2025 | geen besteladvies |
| **Ouder** | alles daarvoor | geen besteladvies |
| **Doorloper** | ouder label, maar nu op volle prijs en verkoopt (≥ 8 in 28 dagen) | volledig |
| Geen label | seizoensjaar ontbreekt | wel signaal, gemarkeerd |

Het seizoensjaar is het **introductiejaar**, niet "zit nog in de collectie". Hunter
Downpour Tall staat als FW 2025, maar is in september 2026 de best verkochte laars
op volle prijs. Zo'n artikel is een doorloper en krijgt gewoon een besteladvies.

Het NOOS-label is niet heilig: een artikel dat als NOOS staat maar 74% van zijn
jaar in dertien weken verkoopt wordt als seizoensartikel behandeld.

**De prijs van het model zelf beslist.** Staat de helft of meer van de online maten
met een van-prijs, dan geen besteladvies: er is een korting gestart, dus niet
bijkopen. Voorbeeld: Toni Pons Mona-FR verkoopt 10× vorig jaar, maar staat op €27,97
van €40; die sprong komt van de korting.

Eerder besliste de collectie: lag 45% of meer van de collectie in de sale, dan
geen advies. Dat blokkeerde Hunter Women's Original Tall (NOOS), terwijl geen maat
daarvan is afgeprijsd en het model 16× vorig jaar verkoopt. De collectievlag gaat
nu alleen als informatie mee.

### Wanneer piekt het seizoen, wanneer afprijzen

Per model uit zijn eigen curve:

- **Piek** — de week met de meeste vraag
- **Seizoensvenster** — van 8% tot 92% van de jaarvraag, gerekend vanaf het dal
- **Afprijzen vanaf** — de week waarin 70% van de seizoensvraag achter de rug is.
  Vanaf dan loopt de vraag terug en kost wachten meer dan een korting.
- **Restvoorraad bij het dal** — wat er bij het huidige tempo overblijft als het
  seizoen afloopt. Is dat meer dan nul, dan hoort afprijzen niet te wachten tot
  het vaste sale-moment.

## Kanalen

Er is **één voorraad**. Die wordt gespiegeld naar de eigen merkshop, de brede
shops (bartogi.nl / .de) en de marktplaatsen. Dus:

- **Vraag** wordt over alle kanalen opgeteld.
- **Voorraad** wordt één keer geteld, nooit per kanaal opgeteld.
- De radar toont per model de **verdeling van de vraag** over merkshop, brede
  shop en marktplaats.

Bij krapte zijn de kanalen niet gelijk. Een marktplaatsverkoop kost een fee en
komt vaker retour (27% tegen 2–11% in de eigen shops). Wanneer een kernmaat op
"te laat" staat, zijn de laatste paren daarom meer waard in de eigen shops. De
radar markeert dat; het afknijpen van de marktplaatsvoorraad zelf is een
instelling in ChannelEngine.

Op modelniveau beantwoordt de radar de vraag "verkopen de eigen shops dit
seizoen alles zelf uit?". Per maat zet hij de verwachte vraag van alleen de
eigen shops (merkshop + Bartogi) tot het einde van het verkoopseizoen (FW t/m
week 9, SS t/m week 35) af tegen voorraad plus onderweg:

- `eigen_seizoen_st` / `mp_seizoen_st`: verwachte verkoop eigen shops en
  marktplaatsen tot het seizoenseinde;
- `eigen_dekt_pct`: deel van de voorraad dat de eigen shops zelf verkopen
  (per maat begrensd op de voorraad). Rond 100% voegt een marktplaats niets
  toe en kost hij alleen fee en paren;
- `dagen_eigen`: dagen tot het model op is als alleen de eigen shops verkopen.

Een model met een laag percentage maar krappe kleine maten (Downpour Tall
Black: 37–38 op, 40+ overvol) haal je per maat van de marktplaatsen, niet als
geheel.

## Terugblik: hoe groot is het probleem

Voor de vijftig best verkopende modellen van het afgelopen jaar: welk deel van
het jaar waren ze volledig leverbaar, en hoeveel verkoop is er naar schatting
gemist in de dagen dat een kernmaat leeg stond. Dat laatste is een indicatie: het
rekent met het gemiddelde jaartempo, dus het overschat als de leegstand buiten
het seizoen viel en onderschat als het in de piek was.

### Koppeling en verwachting (september 2026)

- **Artikelkoppeling.** Shopify geeft soms een UPC-12-barcode waar ChannelEngine
  een EAN-13 met voorloopnul heeft, en Keenfootwear.nl gebruikt eigen SKU's
  ("1004347-7"). De radar koppelt nu op artikelnummer, EAN, EAN zonder
  voorloopnullen en via de Shopify-barcode (`scripts/pull_barcode.py`; in n8n uit
  de node *Shopify: producten*). Daarvoor telde de Keen-shop niet mee.
- **Buiten het seizoen, maar het verkoopt.** Zegt de curve "buiten seizoen" en
  verkoopt een model toch ≥ 8 in 28 dagen, dan wordt het huidige tempo vlak
  doorgetrokken in plaats van naar nul.
- **Lang leeg gestaan.** Het 12-maandstempo per leverbare dag wordt begrensd op
  2× de werkelijk verkochte stuks.
- **Rest van het jaar per merk.** Per model de verwachte vraag tot week 52 en wat
  de voorraad daarvan kan leveren. Modellen zonder besteladvies tellen alleen mee
  met wat er ligt. Op merkniveau is de optelsom van modellen minder betrouwbaar
  dan "vorig jaar × huidige groei" (merken met een lange staart, zoals HEYDUDE,
  verschuiven vraag naar wat er ligt); gebruik dat voor de vergelijking met het doel.

## Seizoen per merk (omzet per week, dec 2025 – dec 2026)

De weektargets in de MT-rapportage volgen hetzelfde patroon als de curves die de radar gebruikt:

| Merk | Wanneer | Radar |
|---|---|---|
| Lazamani, HEYDUDE, Keen, Toni Pons | zomer: mei–aug, piek eind juni | afprijsmoment valt in juli/aug |
| Bartogi (breed + marktplaatsen) | zomerpiek, tweede top rond Black Friday | — |
| Tofvel | okt–jan, piek nov/dec; lente en zomer bijna nul | piek wk 46–51; een lege maat in oktober kost de hele piek |
| Sockwell | vlak door het jaar, Black Friday 3–5× | doorlopend; Black Friday is geen seizoen, wel een piekweek |
| Hunter | herfst/winter; 2026 is een uitzondering (~2,5–3× vorig jaar) | niveaucorrectie, zie hierboven |

Acties staan niet in de verkoophistorie van vorig jaar als ze toen niet
plaatsvonden (zoals de HEYDUDE-top begin oktober in de weekgrafiek, als dat een
actie is). Die moeten
als geplande actie in de merk-config komen, anders ziet de radar de piek pas als
hij al begonnen is.

## Bekende beperkingen

- Vraag is bruto: retouren worden niet afgetrokken. Voor een waarschuwing is dat
  de veilige kant, het signaal komt eerder.
- De seizoenscurve zelf is nog gebouwd op verkopen, dus ook gedrukt door
  leegstand in vorige jaren. Het jaarniveau is wel gecorrigeerd, de vorm nog
  niet.
- Prijzen en publicatiestatus komen uit de laatste volledige export; de voorraad
  en verkopen uit de radarrun zelf.
- Een merk met maar één eerder seizoen (Hunter: geen 2024) heeft een curve op
  één cyclus. De vorm is dan minder zeker; de controle "vorig jaar zelfde weken"
  staat daarom bij elk voorstel.
- De n8n-versie leest de hersteltijd uit de merk-config en meet hem niet zelf;
  de meting (`scripts/pull_wk.py` + `scripts/uitverkoop.py`) moet eens per
  kwartaal opnieuw.

## Dagelijkse run en overzichtspagina

Elke ochtend om 05:52 draait een Claude-routine in een lege sessie (klaar vóór 07:00):

```
bash voorraad-watch/scripts/dagelijks.sh
```

1. `scripts/ophalen.py` haalt alles vers op in een lege datamap: ChannelEngine-artikelstam
   en orders (400 dagen), Shopify-orders (800 dagen) en producten per shop, ShopifyQL
   (365 en 28 dagen) en de SKU→barcode-koppeling. Sleutels: ChannelEngine via de proxy,
   Shopify via `SHOPIFY_TOKEN_*`.
2. `scripts/uitverkoop.py` rekent per model en maat de dagen tot leeg, de status en de
   **bestel-uiterlijk-datum** (dag waarop de maat op is, min de hersteltijd van het merk).
   De hersteltijd komt uit `config/merk-config.template.csv`: een opgegeven levertijd van
   de leverancier gaat voor, anders de gemeten hersteltijd, anders 6 weken.
3. `scripts/pagina.py` zet het resultaat in `pagina/voorraadradar.html`; de routine
   publiceert die pagina op dezelfde vaste link.

De pagina heeft drie weergaven: **Bestellen** (alles wat leeg of te laat is, daarna op
besteldatum), **Top 25 verkocht** en **Alle artikelen**. Per artikel: verkocht 28 dagen,
voorraad, hoe lang die meegaat (dagen, weken of maanden), welke kernmaat als eerste op is
en de uiterste besteldatum. Klik een regel open voor dezelfde cijfers per maat.

Er gaat geen verkoop- of voorraaddata de repository in: de datamap staat buiten de repo.
