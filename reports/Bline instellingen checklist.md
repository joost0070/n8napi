# Bline: instellingen checklist (stand 7 oktober 2026)

Zie voor de stand vóór advertenties ook `reports/Bline klaar voor advertenties 2026-10-07.md`.

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
| Wachtwoord | uit sinds 06-10, winkel is open |
| Betaaliconen | iDEAL (via Mollie) staat vooraan bij de knop en in de footer |
| Contact | geen telefoonnummer meer: overal mail@blinesleep.nl of de contactpagina (06-10) |
| Klaviyo | 3 flows live (checkout, bekeken/winkelwagen, welkom 10%), eigen aanmeldpop-up op de site; zie `mockups/blinesleep/klaviyo/LEESMIJ.md` |
| n8n | voorraadsync ChannelDock → Shopify (ma 07:15) en weekrapport naar tabblad "📊 Bline week" in Shop4You_CEO_Workbook (ma 08:00) |

## Joost: in de Shopify-admin

| Nr | Waar | Wat | Advies |
|---|---|---|---|
| 1 | Instellingen > Domeinen | **blinesleep.nl gekoppeld en hoofddomein (07-10)**. DNS bij Cloud86: `@` A 23.227.38.65, `www` CNAME shops.myshopify.com; mail blijft bij Cloud86 via `mail`, `smtp` en `ftp` als A-record naar 45.82.188.190, MX `mail.blinesleep.nl`, SPF met `include:shops.shopify.com`. Nog: uwleeskussen.nl en blinesleep.com laten doorsturen | gedaan |
| 2 | Mollie (app in Shopify) | iDEAL via Mollie gekoppeld (06-10). Testbestelling #1001 met iDEAL gelukt en daarna geannuleerd, voorraad teruggezet. **Mollie staat nog in testmodus: meteen op live zetten**, anders "betalen" klanten zonder dat er geld binnenkomt. Op de Mollie-betaalpagina staat nu "Shop4you": websiteprofiel "Bline" (blinesleep.nl, categorie meubels) **aangevraagd 07-10**; pas na goedkeuring en met iDEAL actief de Shopify-app omzetten, tot dan op "Shop4you" laten. iDEAL staat in de checkout als laatste en Klarna staat vooraf gekozen; de volgorde regelt Shopify | **nu** |
| 3 | Instellingen > Betalingen | Klarna staat al aan (live gezien 06-10) | gedaan |
| 4 | Instellingen > Checkout | marketing-vinkje vooraf aangevinkt: **opgelost 06-10** (live gecontroleerd: alleen "Bezorgadres en factuuradres zijn hetzelfde" staat nog aan). Gastcheckout aan, telefoon optioneel | gedaan |
| 5 | Instellingen > Klantprivacy | cookiebanner aan voor de EU; automatisch privacybeheer uit (zoals afgesproken) | ja |
| 5b | Instellingen > Winkelgegevens | **telefoonnummer weghalen**: het is van de site, pagina's, contactbeleid en mails gehaald (06-10), maar het automatische privacybeleid van Shopify haalt het nog uit de winkelgegevens | nu |
| 6 | Instellingen > Meldingen | afzender mail@blinesleep.nl; e-maildomein **geauthenticeerd (07-10)** met 6 CNAME-records bij Cloud86 (mailer4u4, mailerw0e en 4 DKIM-regels); DMARC stond al (`p=quarantine`). TLS-certificaat actief, www en myshopify sturen door naar blinesleep.nl | gedaan |
| 6a | Plesk (Cloud86) | Let's Encrypt-certificaat opnieuw aanvragen voor alleen mail.blinesleep.nl en webmail.blinesleep.nl (blinesleep.nl en www uitvinken), anders mislukt de verlenging omdat die nu naar Shopify wijzen; domein in Plesk niet verwijderen (mailbox) | gedaan 07-10 |
| 6c | Instellingen > Checkout > Aanpassen | logo, kleuren (#1F2A37, overzicht #FBF8F4) en Poppins: **gedaan 07-10** door Joost (via de API kan dit alleen op Shopify Plus) | gedaan |
| 6b | Klaviyo > Instellingen > Account | website `https://blinesleep.nl`, tijdzone Europe/Amsterdam, valuta EUR: **gedaan 07-10** (via API gecontroleerd) | gedaan |
| 7 | Onlinewinkel > Voorkeuren | afbeelding voor delen op sociale media: `bline-leeskussen-beige-01.jpg` | ja |
| 8 | Producten > hoezen | gewicht van een losse hoes invullen (staat op 0 kg) | het echte gewicht is nodig voor verzendlabels |
| 9 | Apps | Google & YouTube en Facebook & Instagram koppelen; Judge.me (Nederlands, de 5 kussens als één productgroep, reviewverzoek 14 dagen na verzending); Collabs | voor de advertenties |
| 10 | Apps | ChannelDock koppelen voor de bestellingen en het retouradres vastleggen. Voorraad: n8n-flow "Bline voorraad ChannelDock → Shopify (wekelijks)" zet elke maandag 07:15 de beschikbare ChannelDock-voorraad in Shopify (op EAN; eerste keer gedaan op 06-10). Zet bij het koppelen van de ChannelDock-app de voorraadsync daar uit, of zet deze flow uit: niet allebei | voor livegang |
| 11 | Marketing > Automatiseringen | de mails uit `reports/bijlagen/Bline mails funnel.md` zetten | na livegang |
| 12 | Belastingen | btw voor België nagaan met de boekhouder (OSS zodra de EU-drempel van €10.000 per jaar wordt overschreden) | navragen |
| 13 | Beslissingen | 30 dagen proberen: **gedaan 06-10** (beleid, voorwaarden, site, advertenties, mails); "voor ... besteld, vandaag verzonden" als ChannelDock dat haalt | open |
| 14 | Onlinewinkel > Voorkeuren | wachtwoord uit: **Joost besloot op 06-10 live te gaan**; kan alleen in de admin (Shopify heeft hier geen API voor). Afrekenen werkt (creditcard, Apple Pay, Google Pay, Klarna, PayPal, Bancontact); iDEAL volgt later | nu |

## Advertenties (stand 7 oktober 2026)

| Onderdeel | Stand |
|---|---|
| Google Ads | managementaccount "Bline Beheer" (561-758-3392) met Bline (860-535-9447) eronder; API-sleutels in de omgeving (`GOOGLE_ADS_*`); basistoegang voor de developer token aangevraagd |
| Meta | systeemgebruiker "Claude API" met volledige toegang tot pagina Bline (372306072632771), advertentieaccount Bline (414180534444868), app Joost en Pixel 1 (488144327490376); sleutels in de omgeving (`META_*`); Shopify-app Facebook & Instagram gekoppeld aan Pixel 1 met uitgebreid delen |
| Meta betalen | **vooraf betalen (optie A):** bij de eerste campagne €150 saldo via iDEAL, automatisch opwaarderen uit. Na de testweken eventueel naar automatisch betalen met bestedingslimiet |
| Campagnes | worden in een nieuwe sessie klaargezet, allemaal op pauze; niets gaat aan zonder akkoord van Joost per campagne |
| Voor livegang | cookiebanner aan in Shopify (Klantprivacy); oude Meta-catalogus en dataset van de vorige winkel pas verwijderen als de nieuwe werken |

