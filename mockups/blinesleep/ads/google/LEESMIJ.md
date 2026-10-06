# Bline Google Ads: klaar om te importeren

Voor het nieuwe Google Ads-account van Bline (aan te maken via de Google & YouTube-app in Shopify, niet het oude account van uwleeskussen.nl). Alles staat op **Gepauzeerd**; aanzetten pas na de testbestelling en "live".

## Bestanden (Google Ads Editor, Account > Importeren > Uit bestand)

| Bestand | Inhoud |
|---|---|
| `bline-google-1_campagnes.csv` | 00 Search Merk (NL+BE, €1/dag, max. klikken, CPC-plafond €0,40) en 02 Search Generiek (NL, €3/dag, CPC-plafond €0,70). Alleen Google Zoeken, taal Nederlands |
| `bline-google-2_advertentiegroepen.csv` | Merk; Leeskussen algemeen (landt op `/products/leeskussen-beige`, de productpagina met alle kleuren); Merk landt op de homepage; per kleur een groep die landt op `/products/leeskussen-<kleur>` |
| `bline-google-3_zoekwoorden.csv` | 44 zoekwoorden, exact en woordgroep; 13 erbij uit de echte bol-zoektermen (aug-sep 2026), zoals rugsteun bed en rugkussen bank |
| `bline-google-4_advertenties.csv` | 7 responsieve zoekadvertenties, 15 koppen en 4 beschrijvingen elk; lengte automatisch gecontroleerd (koppen ≤ 30, beschrijvingen ≤ 90 tekens) |
| `bline-google-5_uitsluitingen.csv` | 35 uitsluitingen als gedeelde lijst "Bline uitsluitingen" (baby, zwangerschap, hond, rugpijn, hernia, gratis, marktplaats, ikea, puzzel, kussensloop, elektrisch ...) |
| `bline-google-6_extensies.csv` | 4 sitelinks, 6 highlights, 1 snippet (stijlen: de vijf kleuren) |

Kolomnamen kunnen per versie van Editor iets verschillen; Editor laat bij het importeren zien welke kolom bij welk veld hoort.

## Shopping (de belangrijkste campagne, pas na koppeling Merchant Center)

| Campagne | Budget | Bieden week 1 t/m 3 | Daarna |
|---|---|---|---|
| 01 Shopping \| Leeskussen \| NL | €8/dag | max. klikken, CPC-plafond €0,60 | doel-ROAS 300% na 15 tot 30 aankopen |
| 01 Shopping \| Leeskussen \| BE | €3/dag | idem | idem |

- Feed komt uit Shopify (Google & YouTube-app). Per kleur een eigen product met EAN, dus vijf kussens en vijf hoezen.
- **Titel in de feed** (veld "Google: titel" in de app, prijs en kleur blijven gelijk): `Leeskussen Bline Beige met vak voor telefoon, 3,8 kg traagschuim, wasbare katoenen hoes, 65 x 50 x 45 cm`. Zelfde opbouw per kleur. Langere titels met de zoekwoorden scoren beter in Shopping; de grootste concurrent (Ella) zet zelfs het aanbod in de titel.
- **Sterren in Shopping:** pas met eigen reviews (Google Klantenreviews in Merchant Center of een productreviewfeed van Judge.me). Dat is de snelste winst na de eerste bestellingen.
- Hoofdbeeld in de feed: beeld 01 (kussen op bed met boek), zonder tekst. Dat is nu het eerste beeld van elk kussen.
- Productgroepen: kussens en hoezen apart; hoezen eerst uitsluiten (alleen upsell).

## Performance Max (later)

Pas bij 30+ aankopen per maand (les uit het MCC). Assetgroep staat dan klaar:
- Koppen: Leeskussen dat blijft staan · Geen kussenfort meer · Bline leeskussen · Hoes wasbaar op 30 °C · Gratis verzending NL en BE
- Lange koppen: Het leeskussen dat blijft staan, met vak voor je telefoon · In vijf kleuren, met een hoes die zo in de was kan
- Beelden: de vijf 01-beelden, de gebruiksbeelden per kleur, de mozaïek en de video (1:1, 25 s)
- Zoekthema's: leeskussen, leeskussen bed, rugkussen bed, kussen rechtop zitten bed
