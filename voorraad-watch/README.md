# Voorraad Watch

Wekelijkse signalering per merk en maat: van welke maten ligt er te veel voor het
seizoen, en van welke te weinig. Gebouwd op ChannelEngine, met Shopify als
noodzakelijke aanvulling.

Eerste analyse: **14 sep 2026 (wk 38)** — 78.246 artikelen uit ChannelEngine,
124.020 webshoporders uit 17 Shopify-shops en 10.474 marktplaatsorders.
171.250 paar vraag over 26 maanden.

93% van de vraag loopt via de webshops, 7% via de marktplaatsen.

---

## 1. Wat er beschikbaar is

Getest tegen de live ChannelEngine Merchant API (`hooijerfootwear.channelengine.net`).

| Endpoint | Levert | Status |
|---|---|---|
| `/v2/products` | 78.246 SKU's: merk, maat, kleur, EAN, voorraad, verkoopprijs, **inkoopprijs**, seizoen, seizoensjaar, model, Shopify-id per shop | werkt — 783 pagina's à 100 |
| `/v2/orders` | orderregels met EAN, aantal, datum, kanaal, fee | werkt — 10.474 orders / 13 mnd |
| `/v2/returns` | retourregels per EAN | werkt — 2.980 retouren |
| `/v2/stocklocations` | 11 locaties: eigen magazijn + FBA/LVB/FBK | werkt |
| `/v2/offer/stock` | voorraad per locatie **plus datum laatste mutatie** (69.917 offers) | werkt — `stockLocationIds` verplicht, en pagineert op `pageIndex`, niet op `page` |
| `/v2/shipments` | doorlooptijd verzending | **403 — API-sleutel mist rechten** |

Bruikbare velden voor deze analyse (uit `ExtraData`): `merk`, `seizoen_NL`,
`Seizoensjaar`, `model`, `groep`, `geslacht_NL`, `Doelgroep_NL`,
`shopify_id_NL` / `_DE` / `_EN`.

De Shopify-koppeling is dus al gelegd — elk artikel draagt zijn Shopify-id.
Alleen de **verkoopcijfers** uit die shops ontbreken.

### De mutatiedatum vangt het gat

`/v2/offer/stock` geeft per artikel een `UpdatedAt`: wanneer de voorraadstand voor
het laatst veranderde. Omdat de voorraad centraal gevoed wordt (`ManageStock` staat
in ChannelEngine op `false`), zakt die stand óók bij een webshopverkoop. Beweging is
daarmee meetbaar zonder de webshopcijfers zelf — alleen het *aantal* verkochte paren
blijft onzichtbaar.

Dat verandert de conclusie wezenlijk. Op de ruwe verkoopcijfers lijkt €1,93 mln stil
te staan. Uitgesplitst naar laatste mutatie:

| | Waarde | SKU's |
|---|---|---|
| Bewoog binnen 90 dagen, geen marktplaatsverkoop | € 1.580.351 | 3.853 |
| Geen verkoop én geen mutatie in 90+ dagen | € 345.077 | 1.785 |
| Waarvan 180+ dagen stil | € 257.841 | — |

87% van de voorraadwaarde bewoog in de laatste 90 dagen. De echte opruimlijst is
€345k, niet €1,93 mln.

## 2. De kentallen die berekend worden

Per maat-SKU, elke maandag:

| Kental | Formule | Waarvoor |
|---|---|---|
| Vraag per week | `0,6 × (13wk/13) + 0,4 × (4wk/4)` | recente vraag weegt zwaarder dan oude |
| Weken dekking (WoC) | `voorraad / vraag per week` | de kernmaat voor "te veel / te weinig" |
| Signaalhorizon | `levertijd/7 + veiligheidsmarge` | dekking hieronder = bijbestellen |
| Weken tot seizoenseinde | uit merk-config | dekking hierboven = blijft liggen |
| Maatcurve-afwijking | `aandeel voorraad% − aandeel verkoop%` | waar de scheefheid zit binnen een merk |
| Gebroken maatreeks | kernmaat op 0 terwijl model verkoopt | duurste vorm van nee-verkopen |
| Retourpercentage | `retouren / verkocht` | scheidt pasvormprobleem van vraagprobleem |
| Dagen sinds mutatie | `vandaag − UpdatedAt` | enige signaal dat webshopverkoop meeneemt |

Daaruit rolt per SKU één signaal: `OK`, `TE-WEINIG`, `NEE-VERKOOP`,
`TE-VEEL`, `TE-VEEL-SEIZOEN` of `STIL`, met een prioriteit in euro's zodat de
lijst op geld gesorteerd kan worden in plaats van op aantal.

## 3. Wat er per merk ingevuld moet worden

Zie [`config/VELDEN.md`](config/VELDEN.md) voor de uitleg per veld en
[`config/merk-config.template.csv`](config/merk-config.template.csv) als startpunt.

De vier die het meest uitmaken:

1. **`levertijd_dagen` + `veiligheidsvoorraad_weken`** — bepalen hoeveel weken
   vooruit gewaarschuwd wordt. Dit is het antwoord op "hoeveel tijd van tevoren".
2. **`nabestellen_mogelijk`** — bij `nee` (voorseizoensinkoop) is een tekort geen
   bestelactie maar een herverdeel- of afprijsactie.
3. **`fw_eind_week` / `ss_eind_week`** — "te veel" is geen absoluut getal maar de
   vraag of de voorraad nog past in de weken die het seizoen nog heeft.
4. **`kernmaten`** — een gat in 39 kost omzet over het hele model, een gat in 47 niet.

## 4. De wekelijkse workflow

[`workflows/voorraad-watch-wekelijks.json`](workflows/voorraad-watch-wekelijks.json)
— importeren in n8n, daarna instellen:

- `CE_API_KEY` als environment variable
- Google Sheet-id op de twee Sheets-nodes (tabbladen `merk-config` en `snapshots`)
- ontvanger op de Gmail-node
- Shopify-node inschakelen zodra de credentials er zijn

Loop: maandag 07:00 → CE producten + orders + retouren + merk-config ophalen →
kentallen berekenen → snapshot wegschrijven → weekrapport mailen.

De snapshot is niet optioneel: ChannelEngine bewaart geen voorraadhistorie. Zonder
wekelijks wegschrijven heb je altijd alleen het nu en nooit een trend.


---

## 7. Vooruitkijken in plaats van terugkijken

Weken dekking is een achteruitkijkspiegel. De vraag die telt is: *haal ik het
einde van dit seizoen met wat er ligt?*

```
jaarvraag(SKU)  = verkoop laatste 26 wk / aandeel van de jaarcurve in die 26 wk
restvraag(SKU)  = jaarvraag x aandeel van de jaarcurve tussen nu en het seizoensdal
projectie       = voorraad - restvraag
```

Het seizoensdal is de week waarin het merk structureel het minst verkoopt; dat is
het natuurlijke einde van zijn seizoen. Voor NOOS-artikelen bestaat dat dal niet,
dus die worden tegen een vaste horizon van 26 weken gemeten.

De projectie alleen is nog geen besluit. Dat volgt uit de combinatie met het
prijsregime van het merk:

| Projectie | Prijsregime | Actie |
|---|---|---|
| Tekort | Volle prijs | Bijbestellen |
| Tekort | Sale loopt | Niet bijbestellen — vraag naar een lopend model sturen |
| Overschot | Volle prijs | **Nu afprijzen** — vroeg klein kost minder marge dan straks groot |
| Overschot | Sale loopt | Korting verdiepen of spreiden |
| NOOS onder bestelpunt | Elk | Aanvullen op levertijd + marge |
| NOOS boven 26 wk vraag | Elk | Inkoop stoppen, afbouwen |
| Geen verkoop, 90+ dgn geen mutatie | Elk | Uitfaseren |

## 8. Seizoen en sale-periode uit de data

Beide worden afgeleid, niet opgegeven.

**Seizoensvenster** — per merk en seizoenstype de weekcurve over 26 maanden,
gladgestreken, met het dal als draaipunt. Levert start, piek en einde.

**Sale-periode** — een afprijzing in Shopify is meestal een lagere prijs, geen
kortingscode. `total_discount` vangt dat dus niet. In plaats daarvan: per artikel
de hoogste prijs die er ooit voor betaald is, en het aandeel paren dat onder 92%
daarvan wegging. Dat aandeel per week over twee jaar geeft het afprijspatroon.

Wat dat oplevert (wk 38, 2026):

| Merk | Basisniveau | Normale sale-weken | Deze week | Live in de shop |
|---|---|---|---|---|
| Toni Pons | 29% | wk 2–6 · wk 29–33 | 11% | 43% |
| Tofvel | 55% | wk 42–44 | 3% | 9% |
| Keen | 21% | wk 22–25 | 11% | 48% |
| Lazamani | 57% | wk 3–5 | 66% | 69% |
| HEYDUDE | 53% | wk 2–5 | 54% | 52% |
| Hunter | 23% | wk 8–9 | 1% | 29% |
| Sockwell | 11% | wk 48–49 | 14% | 1% |

Twee dingen springen eruit. Tofvel prijst af in wk 42–44, vlak vóór zijn piek in
wk 48 — dat is marge weggeven in de weken dat de vraag juist aantrekt. En bij
Lazamani en HEYDUDE ligt het basisniveau boven de 50%: daar is afprijzen geen
seizoen maar de normale gang van zaken.

## 9. Controle tegen de webshop

Elk advies is zo goed als de voorraadstand eronder. Daarom telt het systeem
wekelijks de stand in ChannelEngine naast die in Shopify. Bij de eerste run:
6.635 van 6.779 SKU's gelijk, 45 afwijkend, 99 niet in een webshop. Die 45 zijn
een synchronisatieprobleem en horen op een aparte lijst, niet in een inkoopadvies.

## 10. Wat er nog ontbreekt

1. **Levertijd, naleverbaarheid en order-cutoff per merk.** De enige invoer die nog
   nodig is. Zonder levertijd weet het systeem niet hoe ver vooruit het moet
   waarschuwen; zonder cutoff niet of bijbestellen nog kan.
1. **Geox NL** — het token geeft 401, die shop ontbreekt in de vraagcijfers.
2. **Openstaande inkooporders** — er is geen ERP-koppeling, en die komt er niet.
   Opgelost via de snapshots: een voorraad die tussen twee maandagen *stijgt* is een
   binnengekomen levering. Na een paar weken kent het systeem per merk het leverritme
   en de typische levergrootte, na een paar maanden de werkelijke levertijd — gemeten
   in plaats van opgegeven. Dat vult `levertijd_dagen` en `nabestellen_mogelijk`
   vanzelf in.
3. **Seizoenslabels** — op ruim €1,2 mln aan voorraad ontbreekt `seizoen_NL`.
4. **Rechten op `/v2/shipments`** — nu 403.

## 11. Scripts

`scripts/` bevat de Python-prototypes waarmee de eerste analyse gedraaid is
(`analyse.py` → basis, `analyse2.py` → maatcurve/overstock, `stockage.py` → laatste
mutatie en de opruimlijst, `export.py` → dashboard-data). De productieversie is de n8n-workflow; deze
scripts zijn handig om ad-hoc een merk uit te pluizen.

---

## 12. Correctie: vraag meten, niet verkopen tellen

De eerste versie van de bijbestel-analyse mat de verkeerde grootheid, op twee
manieren tegelijk.

**Verkochte aantallen zijn gecensureerd.** Een maat die na drie weken uitverkocht
raakte verkocht minder stuks dan een maat die een jaar stond te druppelen. In de
data ziet de eerste er dus uit als de slechtste. Voorbeeld uit de eigen cijfers:
Sockwell Heartlink Klasse 2 Light 39-43 verkocht 19 paar — in twaalf dagen, en
staat sindsdien leeg. Dat is 11,1 paar per week, de op één na hardste loper in
de hele Sockwell-range.

**En de lijst filterde op `voorraad > 0`.** Alle 1.005 maten die nu op nul staan
met recente vraag — precies de nee-verkopen — stonden er niet in. Van de
oorspronkelijke 205 regels overlapten er 3 met de gecorrigeerde lijst.

### Wat er nu gemeten wordt

```
tempo(SKU)   = stuks verkocht / dagen dat het artikel daadwerkelijk verkocht  x 7
```

Dat tempo heeft zijn eigen valkuil: een artikel dat één paar in een week verkocht
en daarna leegstond krijgt "1 per week". Drie correcties houden dat in toom:

1. **Krimp naar modelniveau** — `w = n / (n + 8)`. Pas bij acht verkochte stuks
   weegt de eigen meting van een maat vol mee; daaronder telt het tempo van het
   model als geheel, verdeeld over de maatcurve.
2. **Plafond op modelniveau** — de maten samen mogen nooit sneller lopen dan het
   model zelf ooit liep.
3. **Bewijsdrempel** — minimaal 10 stuks per maat of 30 per model. Daaronder gaat
   het op een aparte lijst "te weinig data" en leidt het niet tot een bestelling.

Zonder deze drie kwam er 11,8 miljoen euro aan "te redden omzet" uit. Met alle
drie: 2.518 maten, 35.664 paar, en een bovengrens van 1,67 miljoen over het
resterende seizoen — een prioriteringsscore, geen begrotingsregel. De top-50 is
190k en dat is het deel dat deze week telt.

Daarbovenop geldt de prijsregel nog steeds, nu per artikel in plaats van per merk:
staat er een streepprijs op, dan gaat het niet op de bestellijst. Dat haalde de
helft van de top-150 eruit.

## 13. Wat Shopify zelf kan

Alle 17 shops draaien op het Grow-plan (intern `professional`).

**Ingebouwde voorraadrapporten** (Analytics → Reports → Inventory): *Products by
sell-through rate*, *Inventory remaining per product* (dagen tot leeg op basis van
verkoopsnelheid), *Inventory sold daily by product*, *ABC product analysis*,
*Products by percentage sold*, *Month-end inventory snapshot*. Dat laatste is
waardevol: Shopify bewaart wél een maandelijkse voorraadfoto, ChannelEngine niet.

**Shopify Flow** zit op dit plan. Bruikbare automatiseringen:

| Trigger | Conditie | Actie |
|---|---|---|
| Product variant inventory quantity changed | voorraad < drempel | mail/Slack naar inkoop, tag `bijbestellen` |
| Product variant out of stock | — | tag `nee-verkoop`, datum vastleggen in metafield |
| Product variant back in stock | — | tag verwijderen, leverdatum vastleggen |

Die laatste twee zijn precies het halverwege-inzicht: door uit-voorraad en
terug-op-voorraad te loggen, weet je per maat hoeveel dagen hij écht leverbaar
was. Dat is de teller waar het tempo op gebaseerd hoort te zijn, in plaats van
op de benadering die nu gebruikt wordt.

**Wat Shopify niet kan**, en waarom de n8n-job blijft: de rapporten zijn per shop.
Met 17 shops plus de marktplaatsen op één centrale voorraad geeft geen enkele
shop het juiste beeld — Sockwell NL ziet niet wat Sockwell DE verkoopt, en geen
van beide ziet bol.com. Ook seizoensvensters, afprijsregimes en de maatcurve over
alle kanalen heen zitten niet in Shopify.

**Verdeling van het werk:**

- *Shopify Flow, per shop* — signaleren op het moment zelf: drempelalarm,
  out/back-in-stock loggen. Snel, realtime, geen bouwwerk.
- *n8n, centraal, wekelijks* — de vraag over alle kanalen optellen, tempo
  schatten, seizoen en prijsregime wegen, en één bestellijst produceren.

---

## 14. Correctie: seizoen per model, niet per merk

Drie fouten, alle drie gevonden doordat iemand met kennis van de collectie naar
de uitkomst keek.

### De jaarcurve telde twee ongelijke jaren bij elkaar op

De index werd gebouwd door weeknummers over 26 maanden te sommeren. 2026 loopt
harder dan 2025, en het lopende jaar is onvolledig — dus voor de weken vóór nu
telden twee jaren mee en voor de weken erna één. Gevolg: **elk merk leek precies
deze week zijn seizoen af te sluiten**, wat "nu afprijzen" massaal onterecht
aanzette.

Hunter is het voorbeeld: het oude model zette de piek op wk 37 met een aflopend
seizoen, terwijl het seizoen net begonnen was. Na de correctie — twee volledige
cycli van 52 weken (sep–aug), elk afzonderlijk genormaliseerd, dan gemiddeld —
staat Hunter FW op piek wk 34, dal wk 14, en **57% van de jaarvraag nog te gaan
over 29 weken**.

### Eén curve per merk deugt niet als een merk twee seizoenen heeft

HEYDUDE Wally Braided doet 74% van zijn jaar in dertien zomerweken en **2% in
wk 38-52**. HEYDUDE Bradley Leather piekt in wk 48 met 45% in diezelfde weken.
Een merkcurve middelt die twee tot iets wat voor geen van beide klopt, en zette
zomermodellen op de bestellijst terwijl hun seizoen voorbij was.

De curve wordt nu gekozen op het fijnste niveau met genoeg historie:
kleurvariant (`parent`) → modelfamilie → merk×seizoenstype. Van de gebruikte
curves zit het overgrote deel op kleurvariant-niveau.

Daar bovenop een harde regel: een artikel komt alleen op de bestellijst als
**minstens 12% van zijn jaarvraag nog in wk 38-52 valt**. Dat weerde 651 maten,
waaronder 273 HEYDUDE-zomermaten. HEYDUDE ging van 80 naar 13 maten op de lijst.

### Het NOOS-label in ChannelEngine is niet betrouwbaar

Wally Braided staat daar als NOOS en werd daardoor als doorlopend behandeld —
en doorlopende artikelen kennen geen seizoenseinde, dus glipte het langs de
seizoensfilter. De gemeten curve gaat nu vóór op het label: doorlopend is wat
minder dan 33% van zijn jaar in de beste dertien weken doet, ongeacht wat er in
het veld staat.

### Verder aangescherpt

- **Levenscyclus** — geen besteladvies voor artikelen die niet meer in een
  webshop gepubliceerd staan (148), zelf al afgeprijsd zijn (4.787), of 120
  dagen geen verkoop hadden (4.825). Oude collectie wordt niet opnieuw ingekocht.
- **Volledige artikelnaam inclusief kleur** in elke regel. De afgekapte naam
  "Circulator Heren Compressiekousen Klasse 1 Bla" was niet te controleren: de
  regel gaat over *Black Stripe* (860 paar, 54 verkocht per jaar), niet over
  *Black* (273 paar, 195 per jaar). Zonder kleur is geen enkele regel te toetsen.
- **Mojibake** in maten (`48â50`) hersteld.

### Wat het met de cijfers deed

| | Voor | Na |
|---|---|---|
| Bijbestellen | 2.518 maten · 35.664 paar | 313 maten · 6.410 paar |
| Nu afprijzen | 763 maten | 541 maten |

De lijst is een zesde van wat hij was. Dat is het punt: de eerdere versie
bestelde zomerschoenen bij in september.

---

## 15. Spiegelcontrole: één voorraad, achttien verkoopkanalen

Een paar schoenen ligt één keer in het magazijn, maar wordt getoond in tot vijf
webshops én op bol.com, Amazon, Kaufland en ANWB.

**Shopify deelt die voorraad niet.** Elke shop heeft een eigen
`inventory_item_id` met een eigen teller, allemaal op `management: shopify`.
Circulator Heren Klasse 1 Black Stripe 39-43 (EAN 0845028010323) staat in vijf
shops, met vijf verschillende product- en variant-id's, en overal op 860. Dat
komt niet van Shopify maar van een extern systeem dat hetzelfde getal rondstuurt.

Optellen is dus fout:

| | |
|---|---|
| Voorraad, per SKU één keer geteld | 104.058 paar |
| Voorraad, alle shops opgeteld | 357.795 paar |

### Wat de controle meet

`scripts/spiegel.py` legt per EAN alle webshopstanden naast die van
ChannelEngine. Eerste meting:

| | |
|---|---|
| SKU's in meer dan één shop | 38.448 |
| Shops onderling gelijk | 38.421 (99,9%) |
| Shops lopen uiteen | 27 — waarvan **16 met 10 stuks of minder** |
| ChannelEngine wijkt af van de webshops | 210 |

De 27 afwijkingen zijn klein (1 à 2 stuks) maar zitten bijna allemaal op lage
voorraad. Dat is precies waar synchronisatievertraging geld kost: twee kanalen
verkopen hetzelfde laatste paar. In ChannelEngine staan over dertien maanden
107 MANCO-orders, waarvan 71 op bol.com. Niet bewezen dat die hieruit
voortkomen, maar het is de eerste plek om te kijken.

De 210 afwijkingen tussen ChannelEngine en de webshops lopen twee kanten op.
HEYDUDE Wally Braided Off White 43: CE 0, webshops 93 — de marktplaatsen
verkopen dan voorraad die er wel is. Lazamani Belle Mocassins Navy 39: CE 37,
webshops 0 — omgekeerd, en dat is het risico.

Daarom neemt de motor nu de **hoogste** stand van ChannelEngine en de webshops
als fysieke voorraad. Op de huidige bestellijst scheelde dat één regel van de
200 (20 paar), maar op een advieslijst hoort geen enkele regel op een verkeerde
voorraadstand te staan.

## 16. Hoe lang ligt een artikel er al?

Niet te achterhalen via de API's. Getest en afgevallen:

- Shopify Admin REST en GraphQL geven alleen de **huidige** voorraad.
  `inventoryItem.createdAt` is de aanmaakdatum van het artikel (2021-08-03 voor
  de Circulator), niet van de levering.
- `shopifyqlQuery` bestaat op het Grow-plan en kent een `inventory`-dataset,
  maar geen kolom die maandstanden teruggeeft.
- ChannelEngine geeft `UpdatedAt` per artikel — de laatste mutatie, zonder
  onderscheid tussen een verkoop en een levering.

Wat wél bruikbaar is: `quantities` in de Shopify GraphQL geeft
`available`, `on_hand`, `committed` en `incoming`. Voor de Circulator:
on_hand 864, committed 4, available 860, **incoming 0**.

`incoming` zou de openstaande inkooporders zijn. Over 2.953 gescande varianten
in drie shops staat die op nul — het veld wordt niet gevuld. `committed` wél
(312, 96 en 82 varianten), en dat is bruikbaar voor de spiegelcontrole.

**Conclusie voor het beoordelen van een artikel:** de ouderdom van de voorraad
is niet te meten tot de wekelijkse snapshots lopen. De maandelijkse
voorraadfoto's die Shopify zelf bewaart (*Month-end inventory snapshot* in de
admin) gaan wel terug — die zijn alleen niet via de API te lezen.

Voor de Circulator maakt het voor het oordeel niet uit: bij 54 paar per jaar en
860 op voorraad is het zestien jaar dekking, of die stapel er nu een dag ligt of
drie jaar. Als hij gisteren binnenkwam is dat geen reden om hem te houden, maar
een inkoopfout om bij de bron aan te pakken.

---

## 17. De voorraadhistorie is er wél — via ShopifyQL

In hoofdstuk 16 stond dat de ouderdom van voorraad niet te achterhalen was. Dat
klopte niet. De `inventory`-dataset van ShopifyQL is in augustus 2023 uit
ShopifyQL Notebooks gehaald, maar werkt via de Admin GraphQL API nog steeds —
en de tokens hebben de benodigde scope `read_analytics`.

```
FROM inventory
SHOW ending_inventory_units, inventory_units_sold
GROUP BY month, product_variant_sku
WHERE product_variant_sku = '<ean>'
SINCE -400d UNTIL today
```

Dat is de month-end snapshot, per artikel, per maand. `scripts/ql_voorraad.py`
haalt hem op, zowel voor één artikel als in bulk (1.000 regels per query).

### Wat dat oplevert

**1. Ouderdom van de voorraad.** Circulator Heren Klasse 1 Black Stripe 39-43:

| | | | | | | |
|---|---|---|---|---|---|---|
| 2025-08 | 1.074 | 2025-12 | 944 | 2026-04 | 978 | 2026-08 · 834 |
| 2025-09 | 945 | 2026-01 | 971 | 2026-05 | 924 | 2026-09 · **860** |
| 2025-10 | 1.023 | 2026-02 | 907 | 2026-06 | 921 | |
| 2025-11 | 949 | 2026-03 | 940 | 2026-07 | 845 | |

Dertien maanden tussen 834 en 1.074, `days_out_of_stock = 0`. Niet vandaag
bijgevuld — deze stapel ligt er al meer dan een jaar en zakt met ongeveer 15
paar per maand. Bij dat tempo duurt het bijna vijftig jaar.

**2. `days_out_of_stock` per artikel.** Dit is de juiste noemer voor het
verkooptempo. Tot nu toe werd "dagen leverbaar" benaderd met eerste tot laatste
verkoopdatum; nu is het meetbaar. Van 999 gescande Sockwell-artikelen waren er
**750 ooit uit voorraad** in de afgelopen 365 dagen.

**3. Leveringen.** Een stijging van de maandeindstand is een binnengekomen
levering. Daarmee zijn levertijd en leverritme per merk achteraf af te leiden,
zonder ERP-export en zonder te wachten op wekelijkse snapshots.

### Wat dit nog niet is

De cijfers komen per shop. Omdat de voorraad gespiegeld wordt, geeft één shop de
centrale stand — maar `inventory_units_sold` is wél alleen die shop
(22 stuks voor de Circulator in sockwell.nl, tegen 54 over alle kanalen). Voor
voorraadstanden één shop nemen; voor vraag de bestaande optelling over alle
kanalen aanhouden.
