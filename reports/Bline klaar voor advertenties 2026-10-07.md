# Bline: klaar voor advertenties? (stand 7 oktober 2026)

Op basis van drie onderzoeken op 7 oktober: een vergelijking met goed presterende webshops en openbare benchmarks, ervaringen van vergelijkbare Nederlandse webshops (alleen in de privéversie), en een volledige controle van blinesleep.nl. Daarna is alles wat zonder Joost kon direct opgelost en live getest.

## 1. In het kort

- De winkel draait op blinesleep.nl met slotje, eigen maildomein (Shopify en Klaviyo) en werkende checkout.
- Er staan nog **7 punten bij Joost** voordat er advertentiegeld uitgaat (hoofdstuk 5). Zonder die punten meten we niet goed of komen mails niet aan.
- Daarna: testbestelling volgens het meetplan, en dan kan de Meta-campagne (10 advertenties, 14 beelden, op pauze klaar) aan.

## 2. Wat het onderzoek zegt

| Vraag | Antwoord |
|---|---|
| Is de pop-up te snel? | Nee, de timing (25 s) was eerder te laat. Het probleem was dat hij bij halverwege scrollen opende, tegelijk met de cookiebanner, en op mobiel het halve scherm bedekte. Openbare benchmarks (Wisepops, Omnisend): 6 tot 15 s werkt het best, 21 tot 30 s het slechtst. |
| Korting in de pop-up? | 10% is goed: pop-ups met korting halen duidelijk meer aanmeldingen dan zonder (Omnisend 2026). |
| Waar landen de advertenties? | Op de productpagina in de kleur van de advertentie. Een aparte landingspagina is met €10 per dag niet betrouwbaar te testen. Google Shopping en zoeken converteren per bezoek meestal beter dan social, dus Google zo snel mogelijk aanzetten. |
| Mobiel of desktop? | Mobiel: vrijwel al het advertentieverkeer van Meta is mobiel, en het eerste bezoek moet meteen kloppen. |
| Mails | De eerste welkomstmail met code is de belangrijkste; de mail over een verlaten checkout gaat na 1 uur (zo staat hij). |
| Juridisch | Nieuw sinds 2026: verplichte online ontbindknop, EU-kennisgeving wettelijke garantie, productveiligheid (GPSR). Alle drie staan nu op de site. |

## 3. Doelen (ROAS)

Bline houdt ongeveer €34 per kussen over vóór advertenties. Break-even ROAS (op omzet incl. btw) is dus **2,35**.

| Fase | Doel ROAS | Max. advertentiekosten per verkoop |
|---|---|---|
| Test (2 tot 4 weken) | minimaal 2,4 | €34 |
| Daarna | 3,0 | ongeveer €27 |
| Opschalen (budget +20%) | 3,5 tot 4,0 | €20 tot €23 |

Beoordelen op Shopify-omzet gedeeld door alle advertentie-uitgaven, niet alleen op Meta's eigen cijfer (door de cookiebanner ziet Meta 40 tot 70% van de aankopen). Gevestigde merken sturen vaak op veel hogere ROAS; dat komt door merkzoekverkeer, retargeting en vaste klanten en is voor een nieuw merk niet het juiste doel.

### Fasedoelen (afgesproken 7 oktober, puur performance)

| Fase | Doel | Bijsturen |
|---|---|---|
| Test (dag 1-14) | leren welke 2-3 advertenties en zoekwoorden verkopen; blended ROAS ≥ 1,5 | advertentie of zoekwoord uit na €35 zonder verkoop |
| Optimaliseren (week 3-6) | blended ROAS ≥ 2,35 (break-even), Google ≥ 2,4 | budget van verliezers naar winnaars |
| Opschalen | ROAS 3,0+, dan budget +20% per week | alleen na 2 weken boven 3,0 |

Blended = Shopify-omzet gedeeld door alle advertentiekosten. Verwachting test: 5-12 verkopen in 14 dagen bij €20 per dag; Google Shopping en Merk boven break-even, Meta koud eerst eronder.

## 4. Wat er is opgelost (7 oktober, live getest)

**Eerste indruk en conversie**
- Cookiebanner in Bline-stijl (compacte kaart, Accepteren en Weigeren even groot, kortere tekst), link "Cookie-instellingen" in de footer.
- Pop-up: pas na de cookiekeuze; desktop bij verlaten (en na 12 s buiten productpagina's); mobiel pas vanaf de tweede pagina, als compacte balk; nooit na "in winkelwagen". Code komt direct (enkele aanmelding). Nieuw: tabje "10% korting" aan de zijkant.
- Footer-nieuwsbrief geeft nu ook de 10%-code; "Powered by Shopify" weg; alleen de relevante betaallogo's.
- Homepage: sterkste foto bovenaan (vrouw leest in bed, beige), geen dubbele foto's meer; galerijen per kleur met de beste sfeerfoto op plek 2.
- Winkelwagenlade: knoppen netjes onder elkaar, snelle betaalknoppen zichtbaar, upsell "Extra hoes" alleen bij precies 1 kussen (waar de korting ook echt geldt).

**Klopt alle informatie**
- "30 dagen proberen, gratis retour" overal gelijk: productpagina's, USP-balk, FAQ, retourpagina, retourbeleid, voorwaarden, blogs. Losse hoes: 30 dagen, retour voor eigen rekening.
- 14 dagen-resten weg, maatgids-rekenfout opgelost, lege collecties offline, "sets" uit teksten, bol-score met aantal reviews (13) en halve ster, "voor dezelfde prijs als bol" alleen voor het kussen.
- Vulling overal "3,8 kg traagschuim in stukjes"; hoespagina met eigen vragen.

**Juridisch**
- Pagina "Retour aanmelden" (de verplichte ontbindknop, in gewone taal) met directe bevestigingsmail met datum en tijd, kopie naar mail@blinesleep.nl.
- Pagina "Wettelijke garantie" met de officiële EU-kennisgeving, gelinkt in footer en productpagina's.
- Blok "Productveiligheid" op alle productpagina's (importeur Shop4You, EAN, veilig gebruik).
- Privacyverklaring aangevuld met Klaviyo, Meta, nieuwsbrief, herinneringsmails en retouren.

**Techniek**
- Klaviyo verstuurt via eigen domein send.blinesleep.nl (daarvoor kwamen mails niet aan bij Gmail-adressen).
- 2.000 unieke kortingscodes per code in Shopify en Klaviyo, waarschuwing bij 200.
- Kortingen kunnen samen met de welkomstcode worden gebruikt.
- Lettertype-preloads en Judge.me-scripts (nog 0 reviews) weg: sneller laden.

## 5. Actielijst Joost

**Vóór de eerste advertentie-euro**

| # | Waar | Wat |
|---|---|---|
| 1 | PostNL Zakelijk (chat/contactformulier) | Toegang tot Mijn PostNL herstellen (klantnummer 10845331), Smart Returns en API-sleutel aanvragen. Tekst staat klaar in de chat. Tot die tijd: bij een retouraanmelding het label met de hand maken en mailen. |
| 2 | Shopify > Instellingen > Winkelgegevens | Telefoonnummer weghalen, adres "Brasem 12" invullen. |
| 3 | Shopify > Instellingen > Klantprivacy | Automatisch privacybeleid uit, dan zet ik de eigen privacytekst erin (nu staat in het Shopify-beleid nog het telefoonnummer en een onvolledig adres). |
| 4 | Klaviyo > Instellingen > Account | Organisatieadres: "Shop4You (Bline), Brasem 12, 7623 KS Borne" (staat onder elke mail). |
| 5 | Shopify > Marketing > Automatiseringen | Shopify's eigen mail voor verlaten checkouts uit (Klaviyo doet dat al). |
| 6 | Meta Events Manager > Pixel 1 > Instellingen | "Automatische events" uit (vervuilen de data), "Automatische geavanceerde matching" aan. |
| 7 | Testbestelling | Volgens `reports/Bline meetplan.md`: iDEAL via Mollie (profiel Bline), Purchase moet in Meta binnenkomen; in een NL-incognitovenster controleren dat er vóór "Accepteren" geen Meta-cookies zijn. |

**Kort daarna**

| # | Wat |
|---|---|
| 8 | Shopify-app Google & YouTube installeren (Merchant Center, aankoopconversie, Enhanced Conversions); Google Ads API-toegang loopt nog. |
| 9 | Gewicht losse hoezen invullen (staat op 0 kg). |
| 10 | Deelbeeld voor social (Onlinewinkel > Voorkeuren): bijvoorbeeld de beige leesfoto. |
| 11 | Naam en adres van de fabrikant van het leeskussen (voor productveiligheid). |
| 12 | In de Shopify-orderbevestiging een regel toevoegen met links naar Retour aanmelden en Wettelijke garantie (tekst lever ik). |
| 13 | Reviews: na de eerste bestellingen Judge.me weer aanzetten en reviews laten vragen. |

## 6. Wat ik doe zodra het kan

- PostNL-sleutel binnen: retourlabel met QR-code automatisch mailen na een retouraanmelding.
- Na punt 3: eigen privacytekst in het Shopify-privacybeleid.
- Na de testbestelling: Meta-campagne als concept in het advertentieaccount zetten (op pauze), Google-campagnes zodra de API-toegang er is.
- Na 7 en 14 dagen advertenties: rapport op kosten per winkelwagen en aankoop, winnaars uitbreiden.
