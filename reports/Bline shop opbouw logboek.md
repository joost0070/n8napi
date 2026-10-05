# Bline shop opbouw logboek

Werkwijze volgens `prompts/bline-shop-opbouwen-masterprompt.md` (versie 1.1). Geheimen en de winkeldomeinnaam staan niet in dit logboek.

## 4 oktober 2026, sessie 1

### Stap 0: omgevingsvariabelen

| Variabele | Aanwezig |
|---|---|
| BLINE_SHOPIFY_STORE | ja |
| BLINE_SHOPIFY_CLIENT_ID | ja |
| BLINE_SHOPIFY_CLIENT_SECRET | ja |

Alleen de namen gecontroleerd, geen waarden getoond. De SHOPIFY_*- en BOL_*-variabelen zijn niet gebruikt.

### Werkpakket A: sleutel ophalen

**Resultaat: mislukt. Werk gestopt volgens hoofdstuk 5 van de masterprompt.**

- Aanvraag: `POST https://<BLINE_SHOPIFY_STORE>/admin/oauth/access_token` met `grant_type=client_credentials`, client id en secret (form-encoded).
- Antwoord: **HTTP 404**, Shopify-pagina "Store unavailable". Er is dus geen sleutel opgehaald en geen enkele API-call gedaan.

Nader onderzocht (zonder sleutel, alleen openbare adressen):

| Controle | Uitkomst |
|---|---|
| Vorm van BLINE_SHOPIFY_STORE | 24 tekens, eindigt op `.myshopify.com`, geen `https://`, geen slash, geen spaties. De vorm klopt. |
| Winkelpagina `/` | 404 "Store unavailable" |
| `/password` | 404 "Store unavailable" |
| `/admin` | doorverwijzing naar inlogpagina |
| Proxy van de sessie | werkt normaal |
| Vergelijking met een verzonnen, niet-bestaande `.myshopify.com`-naam | precies hetzelfde gedrag (404 "Store unavailable", `/admin` naar inlog) |

Conclusie: Shopify kent de winkel onder deze `.myshopify.com`-naam niet als actieve winkel. Een winkel die nog in de proefperiode zit of achter een wachtwoord staat, toont normaal de wachtwoordpagina, geen "Store unavailable". De fout ligt dus niet bij de app-rechten (dat zou een 400 of 401 geven), maar bij de winkelnaam of de status van de winkel.

Meest waarschijnlijke oorzaken, in volgorde:

1. **Verkeerde winkelnaam in de variabele.** De vaste `.myshopify.com`-naam wijkt vaak af van de winkelnaam die je zelf kiest (Shopify maakt soms een naam als `abc123-x1.myshopify.com`). Te vinden in Shopify admin onder Instellingen > Domeinen, of in de adresbalk van de admin (`admin.shopify.com/store/<naam>`; de variabele is dan `<naam>.myshopify.com`).
2. **Winkel gesloten, gepauzeerd of proefperiode verlopen zonder abonnement.** Te zien in Instellingen > Abonnement.
3. **Winkel nog niet aangemaakt** in dezelfde organisatie als de Dev Dashboard-app.

### Wat ontbreekt (stand nulmeting)

De nulmeting (thema's, producten, pagina's, menu's, markten, verzendprofielen, beleid, betaalinstellingen, rechten) kon niet worden gedaan. Alles uit werkpakket A staat nog open, net als B tot en met L.

### Niet gedaan, bewust

- Niets aangemaakt, niets gepubliceerd, geen prijzen gezet.
- Geen mails verstuurd, geen beelden laten maken.
- Geen regel in het Systeemregister gezet (dat hoort bij de afronding van de opbouw).

### Wacht op Joost

1. Controleer de `.myshopify.com`-naam van de Bline-winkel en zet die in `BLINE_SHOPIFY_STORE` (zonder `https://`).
2. Controleer of de winkel actief is (abonnement of proefperiode loopt).
3. Controleer of de Dev Dashboard-app in dezelfde organisatie zit, is vrijgegeven en op deze winkel is geïnstalleerd.
4. Start daarna opnieuw met "Bline shop opbouwen".

### Aanvulling: env nagekeken na melding "het is blinesleep.nl"

- `BLINE_SHOPIFY_STORE` staat op `blinesleep.myshopify.com`. Shopify kent die winkelnaam niet (404 "Store unavailable").
- `blinesleep.nl` en `www.blinesleep.nl` draaien nu op een eigen webserver (LiteSpeed, antwoord 401 "Authorization Required"), niet op Shopify. Het domein is dus nog niet aan een Shopify-winkel gekoppeld en verraadt de `.myshopify.com`-naam niet.
- Voor de sleutel is altijd de vaste `.myshopify.com`-naam nodig; het eigen domein werkt niet voor de API.
- Een paar voor de hand liggende namen geprobeerd (bline-sleep, blinesleep-nl, blinesleepnl, bline, bline-nl en enkele varianten): geen daarvan is een actieve winkel van Bline.
- Nodig van Joost: de naam uit de adresbalk van de Shopify-admin (`admin.shopify.com/store/<naam>`). De variabele wordt dan `<naam>.myshopify.com`.

## 5 oktober 2026, sessie 2

### Stap 0: winkelnaam en variabelen

- Joost gaf op 05-10 de juiste vaste `.myshopify.com`-naam door. De waarde in `BLINE_SHOPIFY_STORE` klopt niet en is in deze sessie niet gebruikt; de juiste naam staat alleen in het script, niet in dit logboek.
- `BLINE_SHOPIFY_CLIENT_ID` en `BLINE_SHOPIFY_CLIENT_SECRET`: aanwezig (alleen de namen gecontroleerd). SHOPIFY_*- en BOL_*-variabelen niet gebruikt.

### Werkpakket A: sleutel ophalen

**Resultaat: gelukt.** `POST /admin/oauth/access_token` met client credentials gaf HTTP 200, sleutel geldig 24 uur, alleen in het geheugen van het script.

Rechten (94 scopes): lezen en schrijven voor producten, voorraad, locaties, bestanden, thema's, content, pagina's, navigatie, metaobjecten, vertalingen, talen, markten, verzending, beleidsteksten, privacy-instellingen, kortingen, orders, conceptorders, fulfilment, retouren, klanten, pixels, kanalen, publicaties en productfeeds. Plus lezen van analytics, klantgebeurtenissen en Shopify Payments-uitbetalingen en -geschillen.

Ontbreekt: `read_shopify_payments_accounts` (of `read_shopify_payments`). Daardoor kan ik niet zien of Shopify Payments actief is. Niet nodig voor de bouw; Joost kijkt dit na in de admin (werkpakket G).

### Werkpakket A: nulmeting (alleen gelezen)

| Onderdeel | Stand 05-10 |
|---|---|
| Winkel | naam "BlineSleep.nl", abonnement Basic, valuta EUR, tijdzone Europe/Amsterdam, kilogram, prijzen incl. btw, contactadres mail@blinesleep.nl, factuuradres Borne |
| Wachtwoord | aan: de winkel stuurt door naar de wachtwoordpagina (302 naar /password) |
| Hoofddomein | nog de `.myshopify.com`-naam; blinesleep.nl is niet gekoppeld |
| Thema's | Horizon (gepubliceerd, achter wachtwoord) en Dawn (niet gepubliceerd, toegevoegd op 04-10) |
| Producten | 0 |
| Collecties | alleen "Homepage" (frontpage) |
| Pagina's | alleen "Contact" (gepubliceerd) |
| Blog | "Nieuws", leeg |
| Menu's | Hoofdmenu: Home, Assortiment (/collections/all), Contact. Voettekst: Zoeken |
| Talen | alleen Nederlands |
| Markten | Nederland (actief). België ontbrak |
| Verzending | één profiel. NL: twee tarieven "Standaard", €6,95 en €0 (vermoedelijk gratis boven een grens). EU (26 landen, ook BE): €12,95. Internationaal (14 landen, o.a. VS, VK, Japan): €19,95 |
| Locatie | "Brasem 7623KS-Borne", verstuurt online orders. De voorraad ligt in werkelijkheid bij eFreight in Vianen |
| Fulfilment | alleen handmatig, ChannelDock nog niet gekoppeld |
| Beleid | alleen een privacybeleid (Shopify-sjabloon, 18.825 tekens). Geen voorwaarden, retour-, verzend- of contactbeleid |
| Betalen | niet leesbaar (recht ontbreekt, zie boven) |
| Pixels, apps | geen pixel van deze app; Google- en Meta-app nog niet zichtbaar gekoppeld |
| Orders, kortingen, doorverwijzingen, bestanden | alle 0 |
| Metafield-definities | geen |

### Wat ontbreekt (na de nulmeting)

1. Domein blinesleep.nl koppelen (DNS bij Joost), plus uwleeskussen.nl en blinesleep.com als doorverwijzing.
2. Dawn inrichten (logo, kleuren, eigen secties). Dawn staat er al, installeren is niet meer nodig.
3. Beelden uploaden en per kleur ordenen.
4. Alle teksten: homepage, productpagina, Over Bline, Verzending, Retourneren, Veelgestelde vragen, aankondigingsbalk, e-mailmeldingen.
5. Beleidsteksten: voorwaarden, retour met modelformulier, verzending, contactgegevens.
6. Verzending: NL en BE gratis, overige landen uit (akkoordpunt 4).
7. Markt België activeren (staat nu als concept, zie hieronder).
8. Menu: "Assortiment" wijst naar /collections/all; wordt de productpagina of de collectie Leeskussens.
9. ChannelDock-koppeling, Shopify Payments, Google- en Meta-app (Joost).
10. Locatie: de naam "Borne" klopt niet met het magazijn in Vianen; voorstel hieronder.

### Werkpakket C: wat er nu staat (alles als concept, niets gepubliceerd)

**Metafield-definities**, namespace `bline`, eigenaar product, bruikbaar voor dons, lyocell en zijde: afmetingen, vulling, hoesstof, wasvoorschrift, gewicht, inhoud_doos, certificaten.

**Collecties** (handmatig, op geen enkel verkoopkanaal): "Leeskussens" met beide producten, "Slapen" leeg voor later.

**Product "Leeskussen Bline"**, status concept, handle `leeskussen`, merk Bline, optie Kleur:

| Kleur | SKU | EAN | Prijs | Voorraad | Gewicht |
|---|---|---|---|---|---|
| Wit | BLINE-LK-WIT | 8720892179074 | €69,99 | 241 | 3,9 kg |
| Beige | BLINE-LK-BEIGE | 8720892687241 | €79,99 | 39 | 3,9 kg |
| Blauw | BLINE-LK-BLAUW | 8720892687258 | €79,99 | 86 | 3,9 kg |
| Grijs | BLINE-LK-GRIJS | 8720892687265 | €79,99 | 78 | 3,9 kg |
| Zwart | BLINE-LK-ZWART | 8720892687272 | €79,99 | 80 | 3,9 kg |

**Product "Hoes voor leeskussen Bline"**, status concept, handle `hoes-leeskussen`:

| Kleur | SKU | EAN | Prijs | Voorraad |
|---|---|---|---|---|
| Wit | BLINE-HOES-WIT | 8720892179098 | €29,99 | 27 |
| Beige | BLINE-HOES-BEIGE | 8720892687203 | €34,99 | 38 |
| Blauw | BLINE-HOES-BLAUW | 8720892687210 | €34,99 | 85 |
| Grijs | BLINE-HOES-GRIJS | 8720892687227 | €34,99 | 77 |
| Zwart | BLINE-HOES-ZWART | 8720892687234 | €34,99 | 80 |

Gevulde metafields: afmetingen, vulling, hoesstof, wasvoorschrift, gewicht en inhoud doos, alleen met de feiten uit hoofdstuk 3a. Certificaten bewust leeg tot Joost een OEKO-TEX-nummer heeft. Gewicht van de losse hoes is onbekend: `[NAVRAGEN]`, niet ingevuld.

Opmerkingen:
- Prijzen zijn de bol-prijzen van 04-10 (akkoord Joost). De actuele bol-prijs kon ik vandaag niet nalezen: bol.com geeft vanuit deze sessie 403 en de Bline bol-koppeling in n8n is niet aangesproken. Voor livegang nog één keer per EAN controleren.
- Voorraad is de ChannelDock-stand van 04-10. Een kleurbundel gebruikt in werkelijkheid een wit kussen plus een hoes; Shopify telt dat los. ChannelDock blijft de bron en zet de voorraad na de koppeling goed.
- Shopify zette het leeskussen automatisch ook in de collectie "Homepage". Onschuldig zolang het product concept is.
- Nog geen beelden en geen productomschrijving (volgt bij werkpakket C-beelden en D).

### Werkpakket E: markten

- Markt **België** aangemaakt (handle `be`), status **concept**, dus nog niet actief. Activeren samen met de verzendregels.
- Btw: prijzen zijn incl. btw, 21% in NL en BE. Let op: verkopen naar België gaan via de OSS-aangifte; in Shopify is daarvoor niets extra nodig.

**Voorstel verzending (akkoordpunt 4, nog niet gewijzigd):**
- Zone Nederland: één tarief "Gratis verzending", €0, met als tekst "Binnen 1-2 werkdagen in huis". Het tarief van €6,95 eruit.
- Nieuwe zone België: zelfde gratis tarief.
- Zones EU (overige landen) en Internationaal: uitzetten. Fase 1 is alleen NL en BE.

**Voorstel locatie:** de locatie hernoemen naar "eFreight Vianen" met het magazijnadres, of laten zoals hij is als ChannelDock een eigen fulfilmentlocatie aanmaakt. Beslist bij de ChannelDock-koppeling.

### Niet gedaan, bewust

- Niets gepubliceerd. Wachtwoord blijft aan. Horizon blijft het gepubliceerde thema; Dawn is niet gepubliceerd.
- Verzendtarieven niet aangepast (akkoordpunt 4).
- Geen mails verstuurd, geen nieuwe beelden laten maken, geen Higgsfield-generaties.
- Geen regel in het Systeemregister (hoort bij de afronding).

### Volgende sessie (zonder Joost mogelijk)

1. Beelden: bestaande Higgsfield-originelen downloaden volgens `koppeling.json`, omzetten naar JPG 2048px, kleurcontrole naast de bol-foto, uploaden en per kleur ordenen met alt-teksten.
2. Dawn inrichten: logo, kleuren, lettertypes, eigen secties (kleurbolletjes, meelopende knop, specificatietabel uit metafields, levertijdregel, vergelijkingsblok, vragen).
3. Teksten (werkpakket D) als concept, met de controle op schrapwoorden.
4. Doorverwijzingen voor uwleeskussen.nl klaarzetten.

### Wacht op Joost

1. Akkoord op het verzendvoorstel (NL en BE gratis, rest uit).
2. Recht `read_shopify_payments_accounts` toevoegen aan de app (optioneel), of zelf in de admin nakijken of Shopify Payments actief is.
3. OEKO-TEX-certificaatnummer, als dat er is.
4. Gewicht van de losse hoes.
5. DNS van blinesleep.nl (A-record en CNAME www naar Shopify), en uwleeskussen.nl en blinesleep.com.
6. ChannelDock aan Shopify koppelen.
7. Shopify Payments activeren, daarna Google- en Meta-app koppelen.
8. Retouradres bevestigen.

## 5 oktober 2026, sessie 3

Joost gaf akkoord op het verzendvoorstel en vroeg door te gaan met beelden en Dawn.

### Werkpakket E: verzending en markten (akkoord Joost 05-10)

- Zone Nederland: de twee oude tarieven (€6,95 en gratis vanaf €55) vervangen door één tarief "Gratis verzending", €0, met de tekst "Binnen 1-2 werkdagen in huis".
- Zone België aangemaakt met hetzelfde gratis tarief.
- Zones EU (26 landen) en Internationaal (14 landen) verwijderd. De winkel verstuurt nu alleen naar NL en BE (gecontroleerd).
- Markt België van concept naar **actief** gezet. Dit is niet zichtbaar zolang het wachtwoord aan staat.

### Werkpakket C: beelden

Bron: de 24 bestaande Higgsfield-originelen (2048 px, gedownload via de rawUrl uit `koppeling.json`, geen nieuwe generaties) en de echte foto's van bol (`wit_05, 07, 09, 10, 11`, `blauw_08`, `grijs_08`, 1200 px). Omgezet naar JPG, sRGB, kwaliteit 85, maximaal 2048 px, bestandsnaam `bline-leeskussen-<kleur>-<nr>.jpg`.

Kleurcontrole: elk beeld naast de bol-foto gelegd; ze komen overeen (het zijn dezelfde generaties). De extra zwart-kandidaat (645857df) is **niet gebruikt**: daarop is het kussen donkergrijs, niet zwart. Voor zwart is `zwart_05` het hoofdbeeld.

Leeskussen Bline, 31 beelden:

| Kleur | Volgorde |
|---|---|
| Wit (8) | wit_05 (hoofdbeeld, echte foto), wit_02, wit_06, wit_03, wit_07, wit_10 (vulling), wit_09 (label), wit_04 |
| Beige (5) | beige_07 (hoofdbeeld), beige_04, beige_03, beige_06 (rits en vulling), beige_02 |
| Blauw (6) | blauw_05 (hoofdbeeld), blauw_03, blauw_04, blauw_06 (rits en vulling), blauw_02, blauw_08 |
| Grijs (6) | grijs_05 (hoofdbeeld), grijs_03, grijs_04, grijs_07 (rits en vulling), grijs_02, grijs_08 |
| Zwart (5) | zwart_05 (hoofdbeeld), zwart_02, zwart_04, zwart_07 (rits en vulling), zwart_03 |
| Alle kleuren | maattekening (wit_11) |

- Elke variant heeft zijn hoofdbeeld als variantbeeld.
- Alt-teksten in gewoon Nederlands, met daarin "kleur Wit", "kleur Beige" enzovoort. Het thema gebruikt dat om bij een kleurkeuze alleen de beelden van die kleur te tonen. De maattekening heeft geen kleur in de alt-tekst en staat dus bij elke kleur.
- Hoes voor leeskussen Bline: 10 beelden (per kleur het hoofdbeeld en het rits-detail), variantbeelden gekoppeld.
- Geen beelden met tekst gebruikt, behalve de maattekening.
- Ontbreekt nog: een tekstloos packshot per kleur op een lichte achtergrond. Dat vraagt nieuwe beelden: akkoordpunt 2, niet gedaan.

Logo (`bline-logo.png`), witte variant en icoon (`bline-icoon.png`) staan als bestanden in Shopify.

### Werkpakket B: Dawn (versie 16.0.0, **niet gepubliceerd**)

Instellingen:
- Kleuren uit `mockups/blinesleep/styles.css`: achtergrond #F7F4EF, tekst en knoppen #1F2A37, zand #F1EBE1 als tweede schema, donker schema #1F2A37, salie #5F6E58.
- Lettertypes uit de Shopify-bibliotheek: Cormorant (koppen, gewicht 500) en Inter (tekst).
- Logo en favicon ingesteld. Afgeronde knoppen en beelden, geen animaties bij scrollen, winkelwagen als lade.
- Geen pop-ups en geen aftelklokken. De nieuwsbriefaanmelding en de knop "Volgen in Shop" in de voettekst staan uit, net als de keuze voor land en taal.
- Aankondigingsbalk: "Gratis verzending in Nederland en België" (gelijk aan de verzendinstelling).

Zelf gebouwd:
1. **Kleurbolletjes**: in de keuzeknoppen van de optie Kleur staat een gekleurd bolletje voor de naam. De kleurcodes staan in thema-instellingen > Bline en zijn aan te passen. Wijziging in `snippets/product-variant-options.liquid`.
2. **Beelden per kleur**: `assets/bline.js` verbergt bij een kleurkeuze de beelden van andere kleuren (op basis van de alt-tekst).
3. **Meelopende knop "In winkelwagen"**: sectie `bline-sticky-atc`. Verschijnt onderaan het scherm, op mobiel en desktop, zodra de hoofdknop uit beeld is gescrold. Toont titel en prijs van de gekozen variant.
4. **Specificatietabel**: sectie `bline-specificaties`, gevuld uit de metafields in namespace `bline`. Lege velden worden overgeslagen. Werkt ook voor latere producten.
5. **Levertijdregel**: snippet `bline-levertijd`, tekst in thema-instellingen (standaard "Binnen 1-2 werkdagen in huis"). De datumregel met werkdagen, Nederlandse feestdagen 2026 en 2027 en een instelbare cut-off staat klaar maar **uit**, tot eFreight de cut-off bevestigt en Joost akkoord geeft (akkoordpunt 5).
6. **Vergelijkingsblok "Waarom dit kussen"**: sectie `bline-waarom` met vier punten, elk met een feit uit 3a: stevigheid (3,8 kg traagschuim, laten luchten), wasbare hoes (30 °C, losse hoes te koop), maat (65 x 50 x 45 cm, eerst meten), kleur (14 dagen bedenktijd).
7. **Veelgestelde vragen**: Dawn-sectie met uitklapblokken, zes vragen (levertijd, wassen, stevigheid, losse hoes, inhoud doos, terugsturen).

Productpagina: titel, prijs, levertijdregel, kleurkeuze, knop, twee regels onder de knop (gratis verzending NL en BE, 14 dagen bedenktijd), omschrijving, daarna specificaties, "Waarom dit kussen", vragen en de meelopende knop. Galerij met miniaturen, ook op mobiel. "Kopen met"-knoppen en "Delen" weggehaald; "You may also like" verwijderd (er is maar één product).

Homepage (concept): grote foto (beige, vrouw met boek) met kop "Lezen in bed, zonder kussenfort.", het leeskussen als uitgelicht product, "Waarom dit kussen" en de vragen. Een reviewscore staat er niet in: het bol-cijfer moet nog met bron worden opgehaald.

Alle teksten nagelopen op het lange streepje, op "u" en "uw", op de schrapwoorden en op gezondheidswoorden: geen treffers. Er staat geen tijdstip in een levertijdbelofte.

Controle door Shopify: alle bestanden zijn zonder fouten opgeslagen (één instelling op de homepage gecorrigeerd). Het thema is nog steeds **niet gepubliceerd**, Horizon blijft het actieve thema.

### Nog niet gedaan, en waarom

- **Screenshots, Lighthouse en de controle op "Translation missing"** kon ik niet doen. De winkel staat achter een wachtwoord en de producten zijn concept. Daardoor is de voorbeeldweergave van het thema alleen te zien in de admin van Joost. Het wachtwoord van de winkel heb ik niet en ik heb het ook niet uitgezet.
- **Product niet op het verkoopkanaal Online Store gezet.** Het product blijft concept. Bij de livegang moeten product en collectie "Leeskussens" nog op het kanaal.
- **Productomschrijving** volgt bij werkpakket D.

### Wacht op Joost

1. De voorbeeldweergave van Dawn bekijken in de admin (Online Store > Thema's > Dawn > Aanpassen), op mobiel en desktop. Of het winkelwachtwoord als omgevingsvariabele geven, dan maak ik zelf screenshots en draai ik Lighthouse.
2. Eventueel nieuwe tekstloze packshots per kleur (akkoordpunt 2).
3. De overige punten uit sessie 2 (Payments, certificaat, gewicht hoes, DNS, ChannelDock, retouradres).
