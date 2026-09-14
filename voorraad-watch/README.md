# Voorraad Watch

Wekelijkse signalering per merk en maat: van welke maten ligt er te veel voor het
seizoen, en van welke te weinig. Gebouwd op ChannelEngine, met Shopify als
noodzakelijke aanvulling.

Eerste analyse: **14 sep 2026 (wk 38)** — 78.246 artikelen, 10.474 orders,
2.980 retouren uit ChannelEngine.

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

## 5. Wat er nog ontbreekt

1. **Shopify: de shopadressen.** De toegangstokens staan al in de omgeving — 19 stuks,
   per merk en per land (Keen NL, Lazamani NL/DE/EN, Tofvel NL/DE/EN, Sockwell NL/DE/EN,
   Hunter NL, HeyDude NL, Toni Pons NL, Jan Jansen NL, Bartogi NL/DE, Piedi Nudi NL).
   Wat ontbreekt is de lijst `.myshopify.com`-adressen die erbij hoort. Zonder die
   adressen blijft het aantal verkochte paren per maat onzichtbaar buiten de marktplaatsen.
2. **Openstaande inkooporders** — er is geen ERP-koppeling, en die komt er niet.
   Opgelost via de snapshots: een voorraad die tussen twee maandagen *stijgt* is een
   binnengekomen levering. Na een paar weken kent het systeem per merk het leverritme
   en de typische levergrootte, na een paar maanden de werkelijke levertijd — gemeten
   in plaats van opgegeven. Dat vult `levertijd_dagen` en `nabestellen_mogelijk`
   vanzelf in.
3. **Seizoenslabels** — op ruim €1,2 mln aan voorraad ontbreekt `seizoen_NL`.
4. **Rechten op `/v2/shipments`** — nu 403.

## 6. Scripts

`scripts/` bevat de Python-prototypes waarmee de eerste analyse gedraaid is
(`analyse.py` → basis, `analyse2.py` → maatcurve/overstock, `stockage.py` → laatste
mutatie en de opruimlijst, `export.py` → dashboard-data). De productieversie is de n8n-workflow; deze
scripts zijn handig om ad-hoc een merk uit te pluizen.
