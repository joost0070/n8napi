# Masterprompt: Bline-webshop opbouwen (blinesleep.nl, fase 1 leeskussen)

Versie 1.0, 4 oktober 2026. Eigenaar: Joost Kuiphuis. Startzin in een nieuwe sessie: **"Bline shop opbouwen"**. Lees eerst deze prompt helemaal, daarna de bronnen hieronder, en werk dan de werkpakketten af. Alles wat kan zonder Joost doe je meteen en parallel; alles achter een akkoordpunt zet je klaar en leg je voor.

---

## 1. Doel

Een eigen Shopify-winkel op **blinesleep.nl** voor het Bline leeskussen, NL en BE, die er zo goed staat dat een advertentietest eerlijk iets zegt. Concreet: een betrouwbare, menselijke productpagina met de beste beelden, kloppende beloftes, juiste instellingen en meting die alleen echte aankopen telt. Daarna pas adverteren. Later komen dons, lyocell en zijde erbij; bouw daar nu al rekening mee (navigatie, metafields), maar zet ze niet online.

Waarom zo: uwleeskussen.nl verkocht niets door een stapel fouten, niet door het product. PMax leerde op nep-conversies van €1, advertenties gingen naar /collections/all en de homepage, merk en domein pasten niet bij elkaar, er stonden medische claims in en de site is nu offline. Die fouten maken we hier niet opnieuw.

## 2. Bronnen (eerst lezen)

| Wat | Bestand |
|---|---|
| Thema's ENV-stores, schrijfstijlgids, 23:59-onderzoek, vragen eFreight | `research_notes/Bline Sleep risicos en voorbeelden/webshop_themas_en_schrijfstijl.md` |
| Lessen Google Ads MCC (blauwdruk campagnes, break-even) | `research_notes/Bline Sleep risicos en voorbeelden/google_ads_mcc_lessen.md` |
| Bol-cijfers leeskussen: prijzen, kostprijs, kleurmix, klachten concurrenten | `reports/Bol leeskussens Q4 strategie.md` |
| Beelden van bol (41 stuks) | `mockups/blinesleep/beelden_bol/` |
| Koppeling bol-beeld naar Higgsfield-origineel (24 stuks, 2048px) | `mockups/blinesleep/beelden_higgsfield/OVERZICHT.md` en `koppeling.json` |
| Eerdere mockups (stijl, tabellen) | `mockups/blinesleep/*.html`, `styles.css` |
| Merkstrategie en vaste uitgangspunten | `prompts/bline-sleep-masterprompt.md`, `reports/Strategie premium slaapmerk.md` |

## 3. Vastgelegde besluiten (niet opnieuw ter discussie)

- **Thema: Dawn** (gratis, Shopify). Basis onder 8 van de 10 ENV-stores, ook onder de best converterende. Geen Hooijer-fork (eigendom Hooijer/Bartogi). Ontbrekende functies bouwen we zelf als secties of blokken.
- **Domein: blinesleep.nl** als hoofddomein. uwleeskussen.nl en blinesleep.com sturen door met een 301.
- **Eén product met kleurkeuze** (Wit, Beige, Blauw, Grijs, Zwart), niet vijf losse producten.
- **Beloftes alleen als ze kloppen.** Tot eFreight schriftelijk cut-off en ophaaltijden bevestigt: "Binnen 1-2 werkdagen in huis". Geen "vandaag verzonden" bij een cut-off van 23:59.
- **Meting telt alleen aankopen.** Geen micro-conversies als primair doel, nooit een conversie met vaste waarde.
- **Geen Performance Max bij de start.** Pas bij 30+ aankopen per maand.

## 4. Harde regels

1. **Toegang.** Gebruik alleen `BLINE_SHOPIFY_STORE`, `BLINE_SHOPIFY_CLIENT_ID`, `BLINE_SHOPIFY_CLIENT_SECRET`. De variabelen `SHOPIFY_*`, `BOL_NL_*`, `BOL_BE_*`, `BOL_ADS_*` horen bij een **ander** verkopersaccount (Hooijer): nooit gebruiken voor Bline, nooit waarden tonen. Bol-gegevens van Bline alleen via de bestaande n8n-koppeling van het Bline-account of de publieke bol-pagina.
2. **Geheimen** nooit in output, bestanden, commits, sheets of chat. Een toegangssleutel alleen in het geheugen van het script.
3. **Akkoord van Joost per actie** (zie hoofdstuk 8) voor alles wat live gaat, geld kost, prijzen zet of klanten raakt. Het wachtwoord van de winkel blijft aan tot Joost "live" zegt.
4. **Prijzen** zet je pas na bevestiging per artikel. Voorstel: gelijk aan bol (wit €69,99, kleur €79,99).
5. **Teksten** volgens de schrijfstijlgids (hoofdstuk 7 van het themabestand): je-vorm, beginnen bij een moment, getallen in plaats van bijvoeglijke naamwoorden, geen rijtjes van drie, geen gedachtestreepjes, geen gezondheidsclaims, geen superlatieven zonder bewijs. Woordenlijst om te schrappen staat in regel 4 van de gids.
6. **Geen feiten verzinnen.** Afmetingen, wastemperatuur, stof, gewicht en vulling komen uit de bol-listing van Bline of van Joost. Onbekend? Zet `[NAVRAGEN]` en neem het op in de vragenlijst, publiceer het niet.
7. **Geen em-dash** (het lange streepje), nergens.
8. **Geen mail** naar leveranciers of dienstverleners (ook niet eFreight) zonder akkoord per bericht; concepten mogen.
9. **Geen reviews vragen** aan bol-klanten. Bol-score alleen tonen als getal met bron, geen reviewteksten kopiëren.
10. **Thema's van derden**: niets kopiëren uit ENV-stores (code, teksten, beelden). Leren mag, overnemen niet.

## 5. Techniek

- **Sleutel ophalen** (client credentials, Dev Dashboard-app in dezelfde organisatie):
  `POST https://$BLINE_SHOPIFY_STORE/admin/oauth/access_token` met `grant_type=client_credentials`, `client_id`, `client_secret` (form-encoded). De sleutel is circa 24 uur geldig; bij een 401 opnieuw ophalen. Lukt dit niet: stop, meld de foutcode aan Joost (meestal: app niet vrijgegeven of niet geïnstalleerd).
- **API**: Admin GraphQL, versie `2026-10`, `https://$BLINE_SHOPIFY_STORE/admin/api/2026-10/graphql.json`, header `X-Shopify-Access-Token`.
- **Eerste call**: `shop { name myshopifyDomain primaryDomain { host } currencyCode plan { displayName } }` plus `currentAppInstallation { accessScopes { handle } }`. Leg vast welke rechten er zijn; ontbreekt er een, meld het.
- **Bestanden**: grote beelden via `stagedUploadsCreate` en `fileCreate`; thema-bestanden via `themeFilesUpsert`.
- **Beelden uit Higgsfield**: originelen ophalen met `show_generation_by_ids` (rawUrl) voor de id's in `koppeling.json`. Omzetten naar JPG 2048px, kwaliteit 85, sRGB, bestandsnaam `bline-leeskussen-<kleur>-<nr>.jpg`.
- **Logboek**: elke stap met resultaat in `reports/Bline shop opbouw logboek.md`; aan het eind één regel in de sheet "🧭 Systeemregister" (spreadsheet 1dy1WZ...).

## 6. Werkpakketten

Volgorde: A eerst. Daarna B, C, D, E en K tegelijk. F, G en H zodra de input van Joost er is. I en J als laatste. L als slotcontrole.

### A. Verbinding en nulmeting
- Sleutel ophalen, shop-query, rechten vastleggen.
- Lees wat er al staat: thema's, producten, pagina's, menu's, markten, verzendprofielen, beleidsteksten, betaalinstellingen (alleen lezen).
- **Klaar als:** logboek bevat de uitgangssituatie en een lijst met wat ontbreekt.

### B. Thema (Dawn)
- Installeer de nieuwste Dawn als **niet-gepubliceerd** thema met `themeCreate` (bron: release-zip van Shopify/dawn). Lukt dat niet: vraag Joost om Dawn met één klik toe te voegen via de Theme Store.
- Instellingen: lettertypes en kleuren uit `mockups/blinesleep/styles.css`, logo (van Joost), favicon, rustige witruimte, geen pop-ups, geen aftelklokken.
- Zelf toevoegen als secties of blokken:
  1. **Kleurbolletjes** gekoppeld aan de optie Kleur; bij kleurkeuze alleen beelden van die kleur.
  2. **Meelopende knop "In winkelwagen"** op mobiel en desktop, verschijnt als de hoofdknop uit beeld is.
  3. **Specificatietabel** uit metafields (afmetingen, vulling, hoesstof, wasvoorschrift, gewicht, inhoud doos).
  4. **Levertijdregel** met instelbare tekst en cut-off in thema-instellingen. Standaard: "Binnen 1-2 werkdagen in huis". De dynamische datumregel (werkdagen, feestdagen) staat klaar maar uit tot eFreight bevestigt.
  5. **Vergelijkingsblok** "Waarom dit kussen" op basis van de klachten bij concurrenten (te hard, kleur wijkt af van foto, hoes niet wasbaar, te breed): elk punt met een feit, niet met een claim.
  6. **Veelgestelde vragen** als uitklapblokken.
- Controle: geen enkele "Translation missing" (alle NL-taalsleutels gevuld), Lighthouse mobiel prestaties 80+, toegankelijkheid 90+.
- **Klaar als:** voorbeeldlink van het ongepubliceerde thema werkt op mobiel en desktop, screenshots in `mockups/blinesleep/screenshots/shop/`.

### C. Producten en beelden
- **Leeskussen Bline**: optie Kleur met 5 varianten. Per variant: SKU en EAN (barcode) gelijk aan bol, gewicht, prijs (na akkoord), voorraad volgen aan.
- **Losse hoes** per kleur als tweede product (prijs na akkoord).
- **Beeldvolgorde per kleur**: hoofdbeeld zonder tekst, sfeer met persoon, zijkant met boekenvak, detail hoes en rits, schaalbeeld op een bed, maattekening (`wit_11`). Bronnen: de 24 Higgsfield-originelen, de echte witte foto's (`wit_05, 07, 09, 10`) en `blauw_08`, `grijs_08` van bol. Geen beelden met tekst behalve de maattekening.
- **Ontbrekend**: een hoofdbeeld zonder tekst per kleur. Zet een Higgsfield-opdracht klaar (tekst en rondje verwijderen uit `*_00`, of nieuw packshot op lichte achtergrond) en vraag akkoord vanwege credits. Kleurcontrole: elke kleur naast de bol-foto leggen; wijkt hij af, niet gebruiken.
- **Alt-teksten** in gewoon Nederlands per beeld.
- **Metafields** aanmaken (namespace `bline`): afmetingen, vulling, hoesstof, wasvoorschrift, gewicht, inhoud_doos, certificaten. Definities zo dat dons, lyocell en zijde later dezelfde velden gebruiken.
- Collectie "Leeskussens" (handmatig) en een lege, verborgen collectie "Slapen" voor later.
- **Klaar als:** product in concept, alle beelden geladen, metafields gevuld of `[NAVRAGEN]`.

### D. Teksten
Schrijf in de stijl van de gids, lees elke tekst hardop en schrap 20%:
- Homepage: kop, ondertitel, drie korte blokken (moment, wat het kussen doet, wat je krijgt), beelden, reviewscore met bron, veelgestelde vragen.
- Productpagina: intro van 80 tot 120 woorden, regels onder de knop, specificaties, vragen.
- Pagina's: Over Bline (eerlijk, met "we", alleen ware details), Verzending, Retourneren, Contact, Veelgestelde vragen.
- Aankondigingsbalk: één regel die nooit meer belooft dan de verzendpagina.
- E-mailmeldingen van Shopify (bevestiging, verzending, terugbetaling) in de je-vorm.
- Eindcontrole met een script: zoek op de schrapwoorden, op het lange streepje, op "u " en "uw ", op gezondheidswoorden (pijn, klachten, ergonomisch, rug, nek, houding). Elke treffer toelichten of herschrijven.
- **Klaar als:** alle teksten in concept in Shopify en als overzicht in het logboek.

### E. Markten, belasting en verzending
- Markten: Nederland (hoofd) en België, beide EUR, taal Nederlands. Frans voor België staat klaar als later besluit.
- Prijzen incl. btw, 21% NL en BE. Meld aan Joost dat BE-verkopen via OSS gaan (aangifte, geen actie in Shopify behalve juiste btw).
- Verzendprofiel voorstel: gratis verzending NL en BE (gelijk aan bol). Vervoerder en tarieven na eFreight.
- Checkout: telefoonnummer optioneel, bedrijfsnaam optioneel, adresaanvulling aan, bestelstatuspagina in NL.
- **Klaar als:** markten en verzendregels staan, voorstel in logboek.

### F. Juridisch (input Joost nodig)
- Algemene voorwaarden, privacybeleid, retourbeleid met modelformulier voor herroeping (14 dagen bedenktijd, termijn van 14 dagen voor terugbetalen), verzendbeleid, contactgegevens (KvK, btw-nummer, vestigingsadres, e-mail, telefoon) volgens art. 6:230m BW.
- Basis: Shopify-generator, dan herschrijven in gewone taal; juridische kern niet afzwakken.
- Cookiemelding: Shopify Customer Privacy-banner aan voor EU, toestemming vóór marketingcookies.
- **Klaar als:** alle beleidspagina's staan, gekoppeld in de voettekst en de checkout.

### G. Betalen (Joost moet zelf activeren)
- Shopify Payments met iDEAL | Wero, Bancontact, kaarten, Apple Pay, Google Pay. PayPal als tweede. Klarna later.
- **Klaar als:** testbestelling met de testmodus slaagt, daarna echte bestelling van Joost (zie L).

### H. Meting en feeds (Joost logt één keer in)
- Apps: **Google & YouTube** (Merchant Center plus Google Ads-koppeling) en **Facebook & Instagram** (pixel plus Conversions API). Joost koppelt; jij controleert.
- Toestemmingsmodus v2 via de Shopify-banner. Primaire conversie Google Ads: alleen **Aankoop** met de echte orderwaarde. Overige acties secundair.
- Merchant Center: GTIN = EAN, merk Bline, Google-productcategorie, verzending en retour ingesteld, gratis productvermeldingen aan.
- Controle: testbestelling zichtbaar als één aankoop met juiste waarde in Google Ads (na verwerking) en Meta Events Manager, geen dubbele telling.
- **Klaar als:** feed goedgekeurd zonder afkeuringen, aankoop gemeten.

### I. Concurrenten en bundels
- Werk de vergelijking bij met Ella, Ten Cate, Soft & Silky, Q-Living (prijs, vulling, hoes, wasbaar, afmetingen, reviews); alleen publieke pagina's.
- Bundelvoorstel met marge per bundel: kussen plus extra hoes, twee kussens (voor stellen). Bouw als automatische korting, niet als nepprijs met doorstreping. Prijzen na akkoord.
- **Klaar als:** tabel en voorstel in het logboek, kortingen in concept.

### J. Advertentieplan (klaarzetten, niet starten)
Volgens de MCC-lessen:
- Nummering en per land apart: `01. Shopping | Alle producten | NL`, `02. Search | Generiek | NL`, `00. Search | Merk | NL`, idem BE.
- Zoeken generiek alleen op koopwoorden (leeskussen, leeskussen bed, rugkussen bed, leeskussen met armleuning); landingspagina altijd de productpagina, nooit de homepage of /collections/all.
- Biedstrategie eerst Max. klikken met CPC-plafond of Max. conversiewaarde zonder doel; doel-ROAS van ongeveer 300% pas na 15 tot 30 aankopen. Break-even ROAS ongeveer 2,3.
- Meta: één videotest naar de productpagina, uitgebreide doelgroep NL/BE.
- Startbudget en stopregels als voorstel.
- **Klaar als:** plan in het logboek, campagnes alleen als concept (gepauzeerd) en pas na akkoord aan.

### K. Domeinen en doorverwijzingen
- blinesleep.nl als hoofddomein koppelen (DNS bij Joost: A-record naar Shopify en CNAME www).
- uwleeskussen.nl en blinesleep.com toevoegen als doorverwijzende domeinen.
- Doorverwijzingen voor oude paden van uwleeskussen.nl (producten, collecties, pagina's) naar de juiste nieuwe pagina met `urlRedirectCreate`.
- **Klaar als:** alle drie domeinen geven een 301 naar blinesleep.nl met SSL.

### L. Oplevering
- Controlelijst: mobiel en desktop screenshots van home, product (elke kleur), winkelwagen, checkout, beleidspagina's; geen dode links; geen "Translation missing"; geen lange streepjes; alle beloftes gelijk aan de verzendpagina; meting getest.
- Testbestelling door Joost met echte betaling, daarna terugbetalen door Joost.
- Lijst met openstaande punten en `[NAVRAGEN]`-velden.
- **Joost zegt "live"**: thema publiceren, wachtwoord uit, Merchant Center aan. Pas daarna advertenties, met apart akkoord.

## 7. Wat je zonder Joost mag doen

Lezen; thema installeren en aanpassen zolang het niet gepubliceerd is; producten, collecties, pagina's, menu's, metafields en beelden als concept; markten en belasting instellen; teksten schrijven; doorverwijzingen klaarzetten; concepten voor mails en advertenties.

## 8. Akkoordpunten (altijd eerst vragen)

1. Prijzen per artikel en bundel.
2. Higgsfield-opdrachten die credits kosten.
3. Thema publiceren of wachtwoord uitzetten.
4. Verzendtarieven en de gratis-verzendgrens.
5. Elke levertijdbelofte met een tijdstip.
6. Elk bericht naar eFreight of een andere partij.
7. Advertenties aanzetten of budget wijzigen.
8. Terugbetalen, annuleren of bestellingen wijzigen.
9. Elke app die geld kost.

## 9. Afsluiting

Sluit af met: wat staat er (met links naar voorbeeld en screenshots), wat wacht op Joost (per punt één regel), en het voorstel voor de eerste twee weken advertenties met budget en stopregels.
