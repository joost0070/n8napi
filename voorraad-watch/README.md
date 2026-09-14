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
| `/v2/offer/stock` | voorraad per locatie (70.017 offers) | werkt, `stockLocationIds` verplicht |
| `/v2/shipments` | doorlooptijd verzending | **403 — API-sleutel mist rechten** |

Bruikbare velden voor deze analyse (uit `ExtraData`): `merk`, `seizoen_NL`,
`Seizoensjaar`, `model`, `groep`, `geslacht_NL`, `Doelgroep_NL`,
`shopify_id_NL` / `_DE` / `_EN`.

De Shopify-koppeling is dus al gelegd — elk artikel draagt zijn Shopify-id.
Alleen de **verkoopcijfers** uit die shops ontbreken.

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

Daaruit rolt per SKU één signaal: `OK`, `TE-WEINIG`, `NEE-VERKOOP`,
`TE-VEEL`, `TE-VEEL-SEIZOEN` of `DEAD`, met een prioriteit in euro's zodat de
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

1. **Shopify-toegang (NL/DE/EN)** — blokkerend. Zonder webshopverkoop is de
   vraagkant incompleet en staan alle dekkingscijfers te hoog.
2. **Openstaande inkooporders** — zit niet in ChannelEngine. Een maat op nul
   waarvan volgende week 200 paar binnenkomt is geen tekort.
3. **Seizoenslabels** — op ruim €1,2 mln aan voorraad ontbreekt `seizoen_NL`.
4. **Rechten op `/v2/shipments`** — nu 403.

## 6. Scripts

`scripts/` bevat de Python-prototypes waarmee de eerste analyse gedraaid is
(`analyse.py` → basis, `analyse2.py` → maatcurve/overstock/dead stock,
`export.py` → dashboard-data). De productieversie is de n8n-workflow; deze
scripts zijn handig om ad-hoc een merk uit te pluizen.
