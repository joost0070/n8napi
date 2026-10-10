# Opdracht: elke kleur als eigen product (besluit Joost 05-10-2026)

Joost koos "Elke kleur als eigen product", zoals de Hooijer-shops het doen: 5 losse leeskussen-producten en 5 losse hoezen, onderling gekoppeld met kleurbolletjes. Reden: per kleur vindbaar in Google en Shopping, eigen landingspagina per kleur voor advertenties, collectie oogt als een echte winkel met 5 kaarten.

## Wat er moet staan

**Producten (nieuw, actief, kanaal Online Store, wachtwoord blijft aan)**

| Product | Handle | Variant (1 per product) |
|---|---|---|
| Leeskussen Bline Wit | leeskussen-wit | SKU BLINE-LK-WIT, EAN 8720892179074, €69,99 |
| Leeskussen Bline Beige | leeskussen-beige | SKU BLINE-LK-BEIGE, EAN 8720892687241, €79,99 |
| Leeskussen Bline Blauw | leeskussen-blauw | SKU BLINE-LK-BLAUW, EAN 8720892687258, €79,99 |
| Leeskussen Bline Grijs | leeskussen-grijs | SKU BLINE-LK-GRIJS, EAN 8720892687265, €79,99 |
| Leeskussen Bline Zwart | leeskussen-zwart | SKU BLINE-LK-ZWART, EAN 8720892687272, €79,99 |
| Losse hoes Wit voor leeskussen Bline | hoes-wit | SKU BLINE-HOES-WIT, EAN 8720892179098, €29,99 |
| Losse hoes Beige voor leeskussen Bline | hoes-beige | SKU BLINE-HOES-BEIGE, EAN 8720892687203, €34,99 |
| Losse hoes Blauw voor leeskussen Bline | hoes-blauw | SKU BLINE-HOES-BLAUW, EAN 8720892687210, €34,99 |
| Losse hoes Grijs voor leeskussen Bline | hoes-grijs | SKU BLINE-HOES-GRIJS, EAN 8720892687227, €34,99 |
| Losse hoes Zwart voor leeskussen Bline | hoes-zwart | SKU BLINE-HOES-ZWART, EAN 8720892687234, €34,99 |

Per product: dezelfde beschrijving, metafields (`bline.*`), Google-productcategorie, merk, gewicht en voorraad als de huidige variant; de beelden van die kleur plus de maattekening (bij de hoes: hoofdbeeld en rits-detail van die kleur), alt-teksten; eigen SEO-titel en metabeschrijving met de kleur erin; metafield voor de kleurcode (`bline.kleur_hex`) en de kleurnaam. Prijzen exact zoals in de tabel (gelijk aan bol). Ontbreken beelden, maak het product toch aan; beelden kunnen later.

**Koppeling tussen de kleuren**
- Metafield `bline.kleuren` (lijst met productreferenties) op elk product met de 5 producten van dezelfde soort, in de volgorde Wit, Beige, Blauw, Grijs, Zwart.
- Op de productpagina: kleurbolletjes als links naar het product in die kleur (huidige kleur gemarkeerd), "Kleur: Beige" erboven, tikvlak minimaal 44 px. Geen variantkeuze meer.

**Oude producten**
- "Leeskussen Bline" (handle leeskussen) en "Hoes voor leeskussen Bline" (handle hoes-leeskussen) op concept zetten en van het kanaal halen, niet verwijderen.
- Doorverwijzingen: /products/leeskussen naar /products/leeskussen-beige (best verkochte kleur), /products/hoes-leeskussen naar /products/hoes-beige. De bestaande 22 doorverwijzingen van uwleeskussen.nl laten wijzen naar het product in de juiste kleur.

**Collecties en menu**
- Collectie "Leeskussens" (5 kussens, volgorde Beige, Wit, Grijs, Blauw, Zwart) en nieuwe collectie "Hoezen" (5 hoezen).
- Homepage: in plaats van één uitgelicht product een raster met de 5 leeskussens (2 kolommen op mobiel), daaronder de hoezen.
- Menu: "Leeskussens" naar de collectie, "Losse hoezen" naar de collectie Hoezen.

**Alles wat naar de oude producten wees**
- Bundelkortingen (`reports/Bline bundels logboek.md`): ombouwen naar de collecties Leeskussens en Hoezen, opnieuw narekenen met draftOrderCalculate (zelfde vier scenario's).
- Upsell in de winkelwagen: hoes in een andere kleur dan het kussen, nu als ander product.
- Links in blogs en pagina's naar /products/leeskussen: vervangen door /collections/leeskussens of het juiste kleurproduct.
- Judge.me: noteer voor Joost hoe hij de 5 kussens als één productgroep instelt (reviews gedeeld), zodat reviews niet per kleur versnipperen.
- Funnel- en advertentieplan: landingspagina per kleur in de tekst bijwerken.

## Grenzen
Wachtwoord blijft aan, prijzen exact zoals in de tabel, geen mails, geen betaalinstellingen, geen nieuwe apps, geen nieuwe beelden. Nederlands, zonder gedachtestreepjes. Testpagina-screenshots (zoals sessie 6) van collectie en productpagina op mobiel en desktop, en de 12 review-punten uit `research_notes/Bline Sleep risicos en voorbeelden/kritische_review_shop_v1.md` blijven gelden.
