# Samenvatting masterprompt bol.com v1.1

Volledige prompt: `prompts/bol-masterprompt-account-verbeteren.md`. Stand 30-09-2026.

## Scope

- **Wel:** zoekwoorden, titels en afbeeldingen. De beschrijving en specificaties alleen voor zover ze zoekwoorden dragen of titel en foto's bevestigen.
- **Niet:** ads, e-mailmarketing, reviews of om reviews vragen, prijzen, voorraad en levertijden.

## 0. Harde regels (gaan altijd voor)

1. **Exacte match of niets.** EAN, merk, model, kleur en maat moeten gelijk zijn aan de bron. Wijkt er één af, dan wordt er niets gewijzigd en gaat het product naar de controlelijst.
2. **Kleur, model en maat zijn heilig.** Ze worden nooit overgenomen van een andere variant of van "de familie".
3. **Foto's alleen van exact deze variant.** Bij twijfel over de kleur wordt de foto niet gebruikt.
4. **Bij twijfel niets doen.** Een ontbrekend kenmerk is minder schade dan een fout kenmerk.
5. **Werkvolgorde:** eerst een proefrun, dan één EAN, dan batches van maximaal 25, en alleen na akkoord.
6. **Accounts strikt gescheiden, geen geheimen in de output.**
7. **Alleen toegestane bol-content.** Geen "gratis", "actie", prijzen, eco-claims of symbolen.
8. **Per ronde één onderdeel tegelijk** en alles loggen, zodat het effect meetbaar is.

## Bronnen, in deze volgorde

1. **Merkstore (Shopify):** Bartogi, Lazamani, Tofvel, Sockwell, Heydude, Hunter, Jan Jansen, Keen, Piedi Nudi, Toni Pons en Geox. Zoeken op EAN, en als dat niets oplevert op SKU.
2. **Bartogi (NL, daarna DE)** als het product niet op de merksite staat.
3. **Geen bron:** niets aanvullen, alleen rapporteren.

Kleuren worden genormaliseerd voor de vergelijking: "Black" en "Zwart" tellen als gelijk, "Taupe" en "Beige" als een mismatch.

## Zoekwoordstrategie

**Zo werkt bol:**

- Er is geen verborgen zoekwoordveld. Alleen titel, beschrijving en specificaties tellen.
- bol koppelt zelf synoniemen, meervouden en spelfouten. Die voeg je dus niet toe.
- De juiste productgroep is stap één, want die bepaalt welke zoektermen bol koppelt.

**Opbouw in 4 lagen:**

| Laag | Voorbeeld | Waar |
|---|---|---|
| 1. Hoofdterm | sneakers, leeskussen | titel |
| 2. Merk en model | Bartogi Loafer Milano | titel |
| 3. Kenmerken | kleur, maat of afmeting, materiaal, doelgroep | titel (1 of 2), specificaties (alle) |
| 4. Gebruik en long tail | "voor in bed", "voor op kantoor" | beschrijving, één keer per term |

- **Bronnen voor de termen:** bol product-ranks, bol search-terms (104 weken, NL en BE apart), merkstore en Bartogi (titels, tags, SEO), titels van concurrenten op pagina 1, Google Trends.
- **Kansen:** termen waarop het product wel vertoond wordt maar op positie 21 of lager staat, en termen met veel volume waarop het product nog niet vertoond wordt.
- **Frans (BE)** apart controleren en met de hand herschrijven.

## Titel

- Het sjabloon van bol per productgroep, altijd met het merk vooraan.
  - Schoenen: `Merk - Model - Geslacht - Productgroep - Kleur`
  - Kussens: `Merk Model productgroep - Afmeting - Kleur`
- Doel 70 tekens, maximaal 150. Scheiding " - ", nooit "|".
- Bij schoenen en mode geen maat in de titel (volgens bol-data 10% meer conversie).
- Modelnaam, kleurnaam en materiaal controleren tegen merkstore en Bartogi.
- Titels zelden wijzigen, want de url komt uit de titel.

## Afbeeldingen

- **Hoofdfoto:** witte achtergrond, alleen het product, zonder tekst of logo's, 1500x1500 pixels.
- 6 tot 9 foto's met labels (SIDE, BACK, DETAIL, IN SITU, USP).
- Geen stickers, claims, "gratis verzending" of reviews op de foto's.
- Verwijderen kan niet via de API: alleen vervangen, of bij grote lijsten via Partnerservice.

## Fotovergelijking bol tegen Bartogi en de merkstore

- Bronfoto's tellen alleen als ze aan exact deze variant gekoppeld zijn.
- Vergelijken met een foto-vingerafdruk (hash) en een kleurprofiel.
- **Oordeel per foto:**
  - **Klopt**
  - **Ontbreekt op bol:** kandidaat om toe te voegen.
  - **Verdacht:** nooit automatisch weg, naast elkaar op de controlelijst.
  - **Hoofdfoto fout:** hoogste prioriteit.

## Werkwijze

**Prioriteit:**

1. Fouten in kleur, model of maat, en foute hoofdfoto's
2. Productgroep en lege filterkenmerken
3. Titels
4. Foto's
5. Zoekwoorden in de beschrijving en de Franse teksten

**Proefrunrapport** (nog niets wijzigen):

- samenvatting
- controlelijst
- zoekwoordplan per product
- tabel met huidig, nieuw, bron, bol-regel en zekerheid
- uitkomst van de fotovergelijking

**Uitvoeren na akkoord:**

- Eerst één EAN.
- Na 1 uur het uploadrapport controleren, na 8 uur de content, na 1 dag de productpagina.
- Daarna batches van 25.

**Meten:** nulmeting op de dag van wijzigen, en na 14 en 28 dagen vergelijken met producten die niet gewijzigd zijn.

## Nodig om te starten

- De myshopify-domeinnamen van de stores (Bartogi eerst).
- De scope: een lijst EAN's of een merk.
