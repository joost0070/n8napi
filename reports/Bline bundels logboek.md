# Bline bundels logboek

5 oktober 2026. Twee bundels uit `reports/Bline groeiplan webshop.md` hoofdstuk 1 als automatische korting in Shopify gezet, na akkoord van Joost op 5 oktober.

## Werkwijze

- Admin GraphQL API, versie 2026-10.
- Sleutel via client credentials met BLINE_SHOPIFY_CLIENT_ID en BLINE_SHOPIFY_CLIENT_SECRET, alleen in het geheugen van het script.
- Niet aangeraakt: thema, blog, pagina's, productprijzen, wachtwoord, mails, apps.
- Vooraf gecontroleerd: er stonden nog geen kortingen in de winkel.

## Prijzen in de winkel (ongewijzigd)

| Product | Wit | Kleur (beige, blauw, grijs, zwart) |
|---|---|---|
| Leeskussen Bline | €69,99 | €79,99 |
| Hoes voor leeskussen Bline | €29,99 | €34,99 |

## Aangemaakte kortingen

| | Extra hoes | Twee kussens |
|---|---|---|
| Titel voor de klant | Extra hoes: €9,99 korting | Twee leeskussens: €9,99 korting |
| Soort | automatisch, Buy X Get Y | automatisch, bedrag van de producten |
| Voorwaarde | koop 1 Leeskussen Bline (elke kleur) | minimaal 2 stuks Leeskussen Bline (elke kleur) |
| Korting | €9,99 op 1 Hoes voor leeskussen Bline (elke kleur) | €9,99 in totaal, verdeeld over de kussens |
| Limiet | 1 keer per order | 1 keer per order (vast bedrag) |
| Combineren | niet met product-, order- of verzendkortingen | niet met product-, order- of verzendkortingen |
| Start | 5 oktober 2026 | 5 oktober 2026 |
| Einde | geen | geen |
| Status | actief | actief |
| ID | gid://shopify/DiscountAutomaticNode/1843926008147 | gid://shopify/DiscountAutomaticNode/1843926040915 |

Gratis verzending is een verzendtarief en geen korting, dus die blijft gewoon gelden. In alle controles hieronder kwam "Gratis verzending" voor €0,00 terug.

## Controle met draftOrderCalculate

Alleen berekend, geen conceptorder of echte order aangemaakt. Bezorgadres een testadres in Utrecht, automatische kortingen toegestaan.

| Scenario | Losse prijs | Toegepaste korting | Totaal | Verwacht | Klopt |
|---|---|---|---|---|---|
| Beige kussen + blauwe hoes | €114,98 | Extra hoes: €9,99 korting (hoes €34,99 naar €25,00) | €104,99 | €104,99 | ja |
| Wit kussen + blauwe hoes | €104,98 | Extra hoes: €9,99 korting (hoes €34,99 naar €25,00) | €94,99 | €94,99 | ja |
| 2 beige kussens | €159,98 | Twee leeskussens: €9,99 korting | €149,99 | €149,99 | ja |
| 1 beige kussen zonder hoes | €79,99 | geen | €79,99 | geen korting | ja |
| Extra: 2 beige kussens + 2 blauwe hoezen | €229,96 | Twee leeskussens: €9,99 korting | €219,97 | één korting, niet stapelen | ja |

Het extra scenario laat zien dat de kortingen niet stapelen: als beide kunnen, past Shopify er één toe (beide zijn €9,99). Aanpassingen na de controle waren niet nodig.

## Aanvulling 5 oktober 2026 (shopsessie 8): elke kleur een eigen product

De twee kortingen wijzen nu naar collecties in plaats van naar de oude producten (die staan op concept):

| | Extra hoes | Twee kussens |
|---|---|---|
| Voorwaarde | koop 1 product uit collectie **Leeskussens** | minimaal 2 stuks uit collectie **Leeskussens** |
| Korting | €9,99 op 1 product uit collectie **Hoezen** | €9,99 in totaal over de kussens |

Titels, limieten, combineren, start en ID's zijn gelijk gebleven. Opnieuw nagerekend met draftOrderCalculate (alleen berekend, geen order; testadres Utrecht; `acceptAutomaticDiscounts` aan):

| Scenario | Losse prijs | Toegepaste korting | Totaal | Verwacht | Klopt |
|---|---|---|---|---|---|
| Beige kussen + blauwe hoes | €114,98 | Extra hoes (hoes €34,99 naar €25,00) | €104,99 | €104,99 | ja |
| Wit kussen + blauwe hoes | €104,98 | Extra hoes (hoes €34,99 naar €25,00) | €94,99 | €94,99 | ja |
| 2 beige kussens | €159,98 | Twee leeskussens | €149,99 | €149,99 | ja |
| 1 beige kussen zonder hoes | €79,99 | geen | €79,99 | geen korting | ja |
| Extra: 2 beige kussens + 2 blauwe hoezen | €229,96 | Twee leeskussens (één korting) | €219,97 | niet stapelen | ja |
| Extra: beige kussen + grijs kussen (twee verschillende producten) | €159,98 | Twee leeskussens (€74,99 + €75,00) | €149,99 | €149,99 | ja |
| Extra: alleen een blauwe hoes | €34,99 | geen | €34,99 | geen korting | ja |

Verzending kwam in alle gevallen terug als "Gratis verzending", €0,00.
