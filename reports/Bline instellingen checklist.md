# Bline: instellingen checklist (stand 6 oktober 2026)

Gecontroleerd via de Shopify Admin API. **Staat goed** = gecontroleerd of door Claude ingesteld. **Joost** = kan alleen in de Shopify-admin of vraagt een beslissing.

## Staat goed

| Onderdeel | Stand |
|---|---|
| Winkel | naam BlineSleep.nl, e-mail mail@blinesleep.nl, euro, tijdzone Amsterdam, kilogram, prijzen incl. btw |
| Markten | Nederland (hoofdmarkt) en België, allebei aan |
| Taal | Nederlands |
| Verzending | gratis in Nederland en België |
| Beleid | contact, privacy, retour (14 dagen), verzending en algemene voorwaarden: allemaal in het Nederlands |
| Producten | 5 kussens en 5 hoezen actief, met SEO-titel en -omschrijving, Google-productcategorie, EAN en voorraad; kussens 3,9 kg |
| Galerijen | per kleur afwisselend, alleen originele beelden |
| Sets | uit de webwinkel gehaald (de bundels zitten nu op de productpagina); oude adressen sturen door naar de productpagina met de keuze al ingevuld |
| Files | 95 bestanden weg (dubbele, afgekeurde en mijn eigen bewerkingen); collecties hebben originele beelden |
| Thema | favicon, logo, winkelwagen als lade, zoeken met prijs, SEO-titel homepage "Leeskussen dat blijft staan, met telefoonvak \| Bline" |
| Menu en footer | Leeskussen, Kleuren, Hoezen, Vragen, Over Bline; footer zonder oude pagina's |
| Wachtwoord | staat aan (tot "live") |

## Joost: in de Shopify-admin

| Nr | Waar | Wat | Advies |
|---|---|---|---|
| 1 | Instellingen > Domeinen | blinesleep.nl koppelen als hoofddomein; uwleeskussen.nl en blinesleep.com laten doorsturen | eerst |
| 2 | Instellingen > Betalingen | **iDEAL staat nog uit** (live getest 06-10: checkout toont alleen Klarna, creditcard en PayPal; Bancontact staat aan voor België). iDEAL aanzetten in Shopify Payments | **eerst, voor het wachtwoord eraf gaat** |
| 3 | Instellingen > Betalingen | Klarna staat al aan (live gezien 06-10) | gedaan |
| 4 | Instellingen > Checkout | **marketing-vinkje "Stuur mij een e-mail met nieuws en aanbiedingen" staat vooraf aangevinkt** (live gezien 06-10); dat mag niet, uitzetten bij Marketingopties. Verder: gastcheckout aan (staat), telefoon optioneel (staat), fooi uit | **eerst, voor het wachtwoord eraf gaat** |
| 5 | Instellingen > Klantprivacy | cookiebanner aan voor de EU; automatisch privacybeheer uit (zoals afgesproken) | ja |
| 6 | Instellingen > Meldingen | afzender mail@blinesleep.nl, na het domein het e-maildomein verifiëren (SPF en DKIM) | na stap 1 |
| 7 | Onlinewinkel > Voorkeuren | afbeelding voor delen op sociale media: `bline-leeskussen-beige-01.jpg` | ja |
| 8 | Producten > hoezen | gewicht van een losse hoes invullen (staat op 0 kg) | het echte gewicht is nodig voor verzendlabels |
| 9 | Apps | Google & YouTube en Facebook & Instagram koppelen; Judge.me (Nederlands, de 5 kussens als één productgroep, reviewverzoek 14 dagen na verzending); Collabs | voor de advertenties |
| 10 | Apps | ChannelDock koppelen en het retouradres vastleggen | voor livegang |
| 11 | Marketing > Automatiseringen | de mails uit `reports/bijlagen/Bline mails funnel.md` zetten | na livegang |
| 12 | Belastingen | btw voor België nagaan met de boekhouder (OSS zodra de EU-drempel van €10.000 per jaar wordt overschreden) | navragen |
| 13 | Beslissingen | 30 dagen proberen: **gedaan 06-10** (beleid, voorwaarden, site, advertenties, mails); "voor ... besteld, vandaag verzonden" als ChannelDock dat haalt | open |
| 14 | Onlinewinkel > Voorkeuren | wachtwoord uit: **Joost besloot op 06-10 live te gaan**; kan alleen in de admin (Shopify heeft hier geen API voor). Eerst stap 2 (betalingen), anders kan niemand afrekenen | nu |
