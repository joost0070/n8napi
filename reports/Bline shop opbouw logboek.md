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

## 5 oktober 2026, sessie 4

Joost (05-10): "geef gas op de volledige shop zodat alles er correct inkomt." Nieuwe akkoorden: verzending gelijk aan bol (gratis NL en BE, rest uit), Dawn mag gepubliceerd worden zolang het wachtwoord aan blijft, producten mogen op actief en op het kanaal Online Store, retour 14 dagen met retourkosten voor de klant.

Toegang: de vaste winkelnaam die Joost doorgaf (niet de waarde in `BLINE_SHOPIFY_STORE`), sleutel via client credentials met `BLINE_SHOPIFY_CLIENT_ID` en `BLINE_SHOPIFY_CLIENT_SECRET`. Alleen de namen gecontroleerd. Geen SHOPIFY_*- of BOL_*-variabelen gebruikt.

### Eerst nagekeken wat sessie 3 al deed

| Onderdeel | Stand |
|---|---|
| Beelden | Leeskussen 31 beelden, hoes 10. Alle met alt-tekst, allemaal verwerkt, breedte 2048 px (Higgsfield) of 1200 px (bol). Elke variant heeft zijn hoofdbeeld. Niets opnieuw gedaan. |
| Verzending | Zone Nederland en zone België, elk één tarief "Gratis verzending", €0, "Binnen 1-2 werkdagen in huis". Geen andere zones, geen €6,95. |
| Markten | Nederland en België, allebei actief. |
| Vertalingen | Alle sleutels uit het Engelse taalbestand van Dawn staan ook in het Nederlandse. Alle vertaalsleutels die de eigen secties gebruiken, bestaan. |

### Wat er nu staat

**Thema**
- Dawn is het **gepubliceerde thema**. Horizon staat erachter als reserve. Het wachtwoord staat **aan** (gecontroleerd: elke pagina stuurt door naar /password).
- Voettekst: twee menu's ("Klantenservice" en "Voorwaarden en beleid") en een blok met de bedrijfsgegevens. De losse beleidsregel onderaan staat uit, want de links staan al in het menu.
- Homepage: tussen de grote foto en het product drie korte blokken (moment, wat het kussen doet, wat je krijgt).
- Aparte productsjabloon voor de hoes (zonder "Waarom dit kussen", dat gaat over het kussen).
- Sjabloon voor de pagina Veelgestelde vragen met uitklapblokken (11 vragen).
- Paginatitel: Dawn zette er "&ndash; BlineSleep.nl" achter, dus een gedachtestreepje in elke titel. Nu "| Bline", en alleen als "Bline" er nog niet in staat.
- Paginatitel en metabeschrijving van de homepage staan in thema-instellingen > Bline (de API heeft daar geen andere plek voor).
- Wachtwoordpagina: was Engels ("Opening soon", "Be the first to know") met een aanmeldveld voor mail. Nu Nederlands, zonder aanmeldveld, met de beige foto.
- Eén gedachtestreepje in het Nederlandse taalbestand (alt-tekst van de QR-code op een cadeaubon) vervangen door een dubbele punt.
- Aankondigingsbalk: "Gratis verzending in Nederland en België. Binnen 1-2 werkdagen in huis." Gelijk aan de verzendpagina en de verzendinstelling.

**Producten**
- Leeskussen Bline en Hoes voor leeskussen Bline: status **actief**, op het kanaal **Online Store**. Niet op Point of Sale of Shop.
- Productomschrijving geschreven (leeskussen 112 woorden, binnen 80 tot 120).
- Collectie Leeskussens op Online Store, met omschrijving. Collectie Slapen blijft leeg en verborgen.

**SEO en productfeed**
| Product | Paginatitel | Shopify-categorie | Google-productcategorie |
|---|---|---|---|
| Leeskussen | Leeskussen met vak voor je boek \| Bline | Pillows > Wedge Pillows | 4456 Huis en tuin > Decoratie > Rugkussens |
| Hoes | Losse hoes voor het leeskussen \| Bline | Pillowcases | 2927 Huis en tuin > Linnengoed > Beddengoed > Kussenhoezen |

- Merk (vendor) Bline, GTIN is de EAN in het streepjescodeveld (stond er al), conditie nieuw.
- Elke pagina, de collectie en beide producten hebben een eigen paginatitel en metabeschrijving van hooguit 160 tekens.
- De Google-ID's komen uit de officiële Google-taxonomie (nl-NL). "Rugkussens" past beter dan "Kussens": de ID staat in het metafield `mm-google-shopping.google_product_category`, dat de Google-app leest.

**Pagina's** (alle gepubliceerd, achter het wachtwoord): Over Bline, Verzending, Retourneren (met modelformulier), Contact (met formulier en bedrijfsgegevens), Veelgestelde vragen, Privacy. Volledige teksten in `reports/bijlagen/Bline shop teksten.md`.

**Beleid** (Instellingen > Beleid)
- Algemene voorwaarden, retourbeleid met modelformulier, verzendbeleid en contactgegevens: geschreven en opgeslagen.
- Privacybeleid: **niet** te vervangen via de API. Shopify beheert dat beleid automatisch ("Automatic management for Privacy Policy must be turned off"). De herschreven tekst staat daarom als pagina "Privacy" en die staat in het voettekstmenu. De checkout linkt nog naar de tekst van Shopify tot Joost het automatisch beheer uitzet.
- Bedrijfsgegevens uit 3a: Shop4You, Brasem 12, 7623 KS Borne, KvK 88099865, btw NL004542189B52, mail@blinesleep.nl. Geen telefoonnummer (onbekend, zie Joost-lijst).
- Retouradres staat nergens. De klant mailt en krijgt het adres van ons (zoals 3a voorschrijft). Op het modelformulier staat het vestigingsadres in Borne, want dat is waar de melding heen gaat, niet het pakket.
- Het Europese ODR-platform wordt niet genoemd: dat is in juli 2025 gesloten.

**Menu's**
- Hoofdmenu: Leeskussen (productpagina), Losse hoes, Alle leeskussens (collectie), Over Bline, Vragen, Contact. "Assortiment" naar /collections/all is weg.
- Klantenservice: Verzending, Retourneren, Veelgestelde vragen, Contact, Over Bline.
- Voorwaarden en beleid: Algemene voorwaarden, Retourbeleid, Verzendbeleid, Privacy, Contactgegevens.

**Doorverwijzingen** (22 stuks, werken zodra uwleeskussen.nl als domein aan deze winkel hangt)
- Zeker: `/products/leeskussen-beige` (bekend uit eerder onderzoek) naar het leeskussen met kleur Beige gekozen.
- Waarschijnlijk, zelfde patroon: `/products/leeskussen-wit`, `-blauw`, `-grijs`, `-zwart` naar de juiste kleur; `/products/hoes-<kleur>` naar de hoes in die kleur.
- Voor de zekerheid: `/products/leeskussen-met-hoes`, `/products/hoes`, `/collections/leeskussen`, `/collections/hoezen`, `/pages/over-ons`, `/pages/faq`, `/pages/veelgestelde-vragen-faq`, `/pages/verzenden`, `/pages/verzending-en-levering`, `/pages/retour`, `/pages/retourbeleid`, `/pages/klantenservice`.
- De echte oude paden kon ik niet ophalen: uwleeskussen.nl geeft een foutmelding (409) en het Internet Archive was vanuit deze sessie niet bereikbaar. Heeft Joost een export van de oude winkel of de Search Console van uwleeskussen.nl, dan vul ik de lijst aan.

### Stijlcontrole

Script over alle nieuwe teksten (producten, pagina's, beleid, homepage, balk, vragen, mailconcepten) en over de thema-bestanden met tekst. Gezocht op de schrapwoorden uit regel 4 van de gids, op gedachtestreepjes (lang en half), op "u" en "uw", en op pijn, klacht, ergonomisch, rug, nek, houding, gezond, medisch.

| Treffer | Besluit |
|---|---|
| "boekhouding" (privacy) | Valse treffer op "houding". Blijft. |
| "Klachten" (voorwaarden, art. 9) | Blijft. De wet vraagt informatie over klachtenafhandeling (art. 6:230m BW). Gaat over bestellingen, niet over gezondheid. |
| "klacht" (privacy, 2 keer) | Blijft. Een retour of klacht afhandelen, en het recht om een klacht in te dienen bij de Autoriteit Persoonsgegevens (AVG). |

Verder geen treffers. Geen levertijdbelofte met een tijdstip. Geen reviewscore: er is nog geen bol-cijfer met bron.

### E-mailmeldingen

Shopify heeft geen API voor de meldingen. De standaard Nederlandse meldingen gebruiken al "je". Concepten voor de openingszin van orderbevestiging, verzendbevestiging en terugbetaling staan in `reports/bijlagen/Bline shop teksten.md`; Joost plakt ze in Instellingen > Meldingen (of geeft akkoord dat het zo blijft).

### Screenshots

- Gemaakt: `mockups/blinesleep/screenshots/shop/wachtwoordpagina_desktop.png` en `wachtwoordpagina_mobiel.png`. Daarop zijn logo, kleuren en lettertypes van Dawn te zien. Geen "Translation missing", geen gedachtestreepjes.
- **Niet gemaakt**: home, product per kleur, winkelwagen en beleidspagina's. Alles, ook /policies/, stuurt door naar de wachtwoordpagina. Een themavoorbeeld via `preview_theme_id` zit ook achter het wachtwoord, en de Admin API kan geen pagina's tonen of het wachtwoord uitlezen. Het wachtwoord heb ik niet uitgezet (harde grens). Met het winkelwachtwoord als omgevingsvariabele maak ik de screenshots en draai ik Lighthouse in een paar minuten.

### Niet gedaan, bewust

- Wachtwoord niet uit, geen prijzen gewijzigd, geen betaalinstellingen, geen mails, geen apps, geen nieuwe beelden.
- Geen regel in het Systeemregister: de spreadsheet-ID in de masterprompt is afgekort ("1dy1WZ...").

### Wacht op Joost

1. **Privacybeleid**: Instellingen > Beleid > Privacybeleid, automatisch beheer uitzetten en de tekst van de pagina "Privacy" erin plakken (of mij vragen het te doen).
2. **Winkelwachtwoord** als omgevingsvariabele, voor screenshots, Lighthouse en de controle op dode links. Of zelf in Online Store > Thema's > Dawn > Aanpassen kijken, mobiel en desktop.
3. **Telefoonnummer** voor de contactgegevens (de wet vraagt het als je er een hebt) en het **retouradres**.
4. **E-mailmeldingen**: concepten plakken of akkoord dat de standaard blijft.
5. **Domeinen**: DNS van blinesleep.nl naar Shopify, uwleeskussen.nl en blinesleep.com als doorverwijzing toevoegen. De paddoorverwijzingen staan al klaar.
6. **Shopify Payments** activeren, daarna testbestelling.
7. **ChannelDock** aan Shopify koppelen, testorder (bundel = kussen plus hoes).
8. **Google- en Meta-app** koppelen; de productdata (GTIN, merk, categorie) staat klaar.
9. **Cookiemelding**: Shopify Customer Privacy-banner voor de EU aanzetten (Instellingen > Klantprivacy).
10. OEKO-TEX-nummer, gewicht van de losse hoes, bol-reviewscore met bron (voor de homepage).
11. **"Live"**: wachtwoord uit. Pas daarna Merchant Center en advertenties, met apart akkoord.

## 5 oktober 2026, sessie 5: restyle naar de stijl van echte webshops

Opdracht: de tabel "Besluit voor Bline" uit `research_notes/Bline Sleep risicos en voorbeelden/look_and_feel_env_stores.md` volledig uitvoeren in het gepubliceerde Dawn-thema, en de teksten herschrijven volgens "Taal: aanvulling op de schrijfstijlgids".

Toegang: de vaste winkelnaam die Joost doorgaf (niet de waarde in `BLINE_SHOPIFY_STORE`), sleutel via client credentials met `BLINE_SHOPIFY_CLIENT_ID` en `BLINE_SHOPIFY_CLIENT_SECRET`. Alleen de namen gecontroleerd. Geen SHOPIFY_*- of BOL_*-variabelen gebruikt. Vooraf een kopie gemaakt van alle thema-bestanden die zijn aangepast.

### Kleuren en letter (Dawn, thema-instellingen)

| Kleurschema | Achtergrond | Tekst | Knop | Gebruikt voor |
|---|---|---|---|---|
| scheme-1 | #FFFFFF | #1A1A1A | #1F2A37, witte tekst | standaard, product, header |
| scheme-2 | #F4F4F2 | #1A1A1A | #1F2A37, witte tekst | tweede vlak (vinkjes, "Goed om te weten", vragen) |
| scheme-3 | #1F2A37 | #FFFFFF | wit | aankondigingsbalk en voettekst |
| scheme-4 | #FFFFFF | #1A1A1A | #1F2A37 | kaarten, meelopende knop |
| scheme-5 | #1F2A37 | #FFFFFF | wit | labels (was salie #5F6E58) |
| scheme-6 (nieuw) | #1F2A37 | #FFFFFF | #1F2A37, witte tekst | grote foto op de homepage: witte kop op de foto, inktblauwe knop |

- Crème (#F7F4EF, #FCFAF6), zand (#F1EBE1) en salie (#5F6E58) staan nergens meer, ook niet in `bline.css` of de eigen secties (gecontroleerd met een zoekopdracht over alle thema-bestanden). Goud kwam in het thema niet voor. De kleurcodes van de kleurbolletjes (Wit, Beige, Blauw, Grijs, Zwart) zijn productkleuren en blijven.
- Letter: **Nunito Sans** uit de Shopify-bibliotheek (bestaat, gecontroleerd op de wachtwoordpagina). Koppen `nunito_sans_n7` (700), tekst `nunito_sans_n4`. Cormorant en Inter zijn weg.
- Korte koppen in hoofdletters met wat letterafstand: de kop op de foto, sectiekoppen (Kenmerken, Veelgestelde vragen, Goed om te weten, Beschrijving), koppen in de voettekst en de balk.
- Knoppen: 6 px hoeken, effen inktblauw met witte tekst, geen rand. Kleurkeuze-knoppen, invoervelden, kaarten, beelden en labels ook 6 px (was 14 en 40).

### Homepage

Volgorde nu: grote foto, product, vier vinkjes, kenmerken, vragen.

- Grote foto (beige, vrouw met boek) met kop **RECHTOP LEZEN IN BED** en één knop **Shop nu** naar de productpagina. Ondertitel weg. Witte tekst op de foto (30% donkere laag), ook op mobiel.
- De drie vetgedrukte blokken (Zondagochtend / Het blijft staan / Wat je krijgt) zijn weg, net als "Waarom dit kussen".
- Het leeskussen als uitgelicht product, daarna een grijze balk met de vier vinkjes, daarna "Kenmerken" (nieuwe sectie `bline-kenmerken`, leest de metafields) en zes korte vragen.
- Paginatitel "Leeskussen met vak voor je boek | Bline" (was "... zonder kussenfort").

### Aankondigingsbalk

`GRATIS VERZENDING NL EN BE | BINNEN 1-2 WERKDAGEN IN HUIS | 4,5 UIT 5 OP BOL.COM`, in hoofdletters, vet, op inktblauw.

**Bron van de score:** bol Ratings API, opgevraagd 05-10-2026: 13 reviews op de productfamilie van het Bline leeskussen. Verdeling 9 x 5 sterren, 3 x 4, 1 x 2. Gemiddeld 4,54, afgerond 4,5 uit 5. Geen reviewteksten overgenomen. Bij elke nieuwe stand van de reviews opnieuw nalezen.

### Productpagina (leeskussen en hoes)

- Volgorde: titel, prijs, kleurkeuze, knop, **vier vinkjes** (Gratis verzending in NL en BE / Binnen 1-2 werkdagen in huis / Hoes wasbaar op 30 °C / 14 dagen bedenktijd), **Beschrijving** (5 korte zinnen), **Kenmerken** als lijst uit de metafields.
- De losse levertijdregel met vrachtwagen boven de kleurkeuze is weg, want hij herhaalde het tweede vinkje. Het tweede vinkje leest dezelfde instelling (thema-instellingen > Bline > levertijdtekst). De snippet `bline-levertijd` met de datumregel blijft bestaan, maar staat nergens meer. Gaat de datumregel later aan (akkoordpunt 5), dan komt hij in de plaats van het tweede vinkje.
- De aparte tabel "Specificaties" is vervangen door de lijst "Kenmerken" in de productkolom. De oude sectie `bline-specificaties` is verwijderd.
- "Waarom dit kussen" heet nu "Goed om te weten", met korte koppen (Stevig, Wasbare hoes, Maat, Kleur) en één of twee zinnen per punt.
- Vragen ingekort tot één of twee zinnen. De hoes toont dezelfde zes vragen.

### Teksten

Herschreven (alleen toon, zie `reports/bijlagen/Bline shop teksten.md`):

| Waar | Weg | Nu |
|---|---|---|
| Beschrijving leeskussen | "Je kent het. Twee kussens achter je...", "Hij past niet in je handbagage. Wel achter je in bed." | 5 korte zinnen met de feiten |
| Beschrijving hoes | 3 alinea's | 5 korte zinnen |
| Over Bline | "Lezen in bed klinkt gezellig. Tot je...", "Je krijgt antwoord van een mens." | wie we zijn, vier vinkjes als lijst, "We antwoorden op werkdagen." |
| Verzending | openingszin | lijstje (gratis NL en BE, 1-2 werkdagen, track & trace); "Dan lossen we het op" wordt "We zoeken dan samen een oplossing" |
| Retourneren | "Valt het kussen thuis anders uit dan je dacht?" | "Je hebt 14 dagen bedenktijd, vanaf de dag dat je het kussen ontvangt." |
| Homepage | drieluik, ondertitel, "kussenfort" | kop van 4 woorden en "Shop nu" |

Juridische inhoud niet aangeraakt: algemene voorwaarden, retourbeleid, verzendbeleid, contactgegevens, privacy, het modelformulier en de alinea's "Kosten", "Je geld terug", "Uitproberen mag" en "Goed om te weten" (levertermijn 30 dagen) zijn gelijk gebleven.

### Stijlcontrole (opnieuw)

Script over producten (titel, beschrijving, SEO), pagina's, collecties, beleid, de homepage- en productsjablonen, de vragenpagina, de wachtwoordpagina, balk, voettekst, thema-instellingen, de eigen secties en snippets en het Nederlandse taalbestand. Gezocht op de schrapwoorden uit regel 4 van de gids, op de AI-zinnen uit het besluit ("Je kent het", handbagage, "van een mens", "klinkt gezellig", kussenfort, "eerlijk"), op gedachtestreepjes (lang en half), op "u" en "uw", en op pijn, klacht, ergonomisch, rug, nek, houding, gezond, medisch.

| Treffer | Besluit |
|---|---|
| "klacht" en "boekhouding" (pagina Privacy) | Blijft, zelfde toelichting als sessie 4. |
| "Klachten" (voorwaarden, art. 9) | Blijft, wettelijk verplicht (art. 6:230m BW). |
| "perfect", "ontdekkingen", "klachten" (privacybeleid in Instellingen > Beleid) | Dat is nog de automatische Shopify-tekst; Joost moet het automatisch beheer uitzetten (zie sessie 4, punt 1). Niet onze tekst. |

Verder geen treffers. Geen "Translation missing": de nieuwe secties en snippets gebruiken geen vertaalsleutels, het taalbestand is niet gewijzigd, en de wachtwoordpagina bevat de tekst niet.

### Screenshots

`mockups/blinesleep/screenshots/shop/wachtwoordpagina_desktop.png` en `_mobiel.png` opnieuw gemaakt: witte achtergrond, Nunito Sans 700, geen crème meer. Home en productpagina kon ik weer niet fotograferen: alles staat achter het wachtwoord (zie sessie 4). Shopify heeft alle bestanden zonder fouten opgeslagen.

### Niet gedaan, bewust

- Wachtwoord blijft aan, geen prijzen gewijzigd, geen mails, geen betaalinstellingen, geen apps, geen nieuwe beelden.

### Wacht op Joost

1. Home en productpagina bekijken in Online Store > Thema's > Dawn > Aanpassen (mobiel en desktop), of het winkelwachtwoord als omgevingsvariabele geven voor screenshots en Lighthouse.
2. De overige punten uit sessie 4 blijven open (privacybeleid, telefoonnummer en retouradres, e-mailmeldingen, domeinen, Payments, ChannelDock, Google- en Meta-app, cookiemelding, "live").

## 5 oktober 2026, sessie 6: mobiel

Opdracht van Joost (05-10): 90% van het verkeer is mobiel, de shop moet op een telefoon perfect werken. Leidend: de checklist van 13 punten onder "Mobiel" in `research_notes/Bline Sleep risicos en voorbeelden/look_and_feel_env_stores.md`.

Toegang: de vaste winkelnaam die Joost doorgaf (niet de waarde in `BLINE_SHOPIFY_STORE`), sleutel via client credentials met `BLINE_SHOPIFY_CLIENT_ID` en `BLINE_SHOPIFY_CLIENT_SECRET`. Alleen de namen gecontroleerd. Geen SHOPIFY_*- of BOL_*-variabelen gebruikt. Vooraf een kopie gemaakt van alle thema-bestanden van Dawn.

### Wat er in Dawn is veranderd

| Bestand | Wijziging |
|---|---|
| `sections/header-group.json` | Balk: drie losse berichten (GRATIS VERZENDING NL EN BE / BINNEN 1-2 WERKDAGEN IN HUIS / 4,5 UIT 5 OP BOL.COM), wisselen om de 5 seconden. Header: ruimte boven en onder van 20 naar 8 px, header blijft altijd bovenaan staan (was: alleen bij omhoog scrollen). |
| `templates/product.json` | Score onder de titel. Beschrijving, Kenmerken, Verzending en retour en Vragen als uitklapblokken. Galerij op mobiel zonder miniaturen (veegslider met teller). De losse sectie "Veelgestelde vragen" onder de productpagina is weg: de zes vragen staan nu in het uitklapblok "Vragen". "Goed om te weten" blijft. |
| `templates/product.hoes.json` | Zelfde, maar zonder score (die hoort bij het leeskussen). |
| `snippets/bline-score.liquid` (nieuw) | Sterren en "4,5 uit 5 op bol.com (13)". Bron in de code en hieronder. |
| `snippets/bline-uitklap.liquid` (nieuw) | De vier uitklapblokken, in dezelfde opbouw als de uitklapblokken van Dawn. Beschrijving staat open. |
| `snippets/product-thumbnail.liquid` | Het eerste beeld laadt direct en met voorrang (`loading="eager"`, `fetchpriority="high"`), de rest later. |
| `sections/bline-sticky-atc.liquid` | Meelopende knop: op mobiel alleen prijs plus knop. |
| `assets/bline.js` | Teller van de veegslider telt opnieuw na een kleurkeuze (alleen de beelden van die kleur). Meelopende knop verschijnt op mobiel ook als de hoofdknop nog onder de vouw staat. |
| `assets/bline.css` | Een blok met mobiele regels (tot 749 px breed), zie de checklist hieronder. Op desktop staan de drie balkberichten naast elkaar op één regel. |

Shopify heeft alle negen bestanden zonder fouten opgeslagen. Daarna elk bestand opnieuw opgehaald en vergeleken met wat ik verstuurde: alle negen gelijk. Dawn blijft het gepubliceerde thema. Het wachtwoord staat nog aan (gecontroleerd: de productpagina stuurt door naar /password).

**Bron van de score:** bol Ratings API, opgevraagd 05-10-2026: 13 reviews op de productfamilie van het Bline leeskussen, 9 x 5 sterren, 3 x 4, 1 x 2, gemiddeld 4,54, afgerond 4,5 uit 5 (zie sessie 5). Bij een nieuwe stand van de reviews bijwerken in `snippets/bline-score.liquid` en in de balk.

### Hoe getest, en wat dat waard is

**Dit is een benadering. De echte test op de live winkel moet nog.** Het winkelwachtwoord heb ik niet, dus de echte pagina's kon ik niet openen. Daarom een statische testpagina gebouwd met:
- de echte CSS- en JavaScript-bestanden van het gepubliceerde Dawn-thema (zoals ze nu in Shopify staan, inclusief `bline.css` en `bline.js`);
- de kleurvariabelen en lettergroottes die `theme.liquid` uit de thema-instellingen maakt, met de hand nagerekend;
- dezelfde HTML-opbouw als de Liquid van Dawn en de eigen snippets oplevert, met de echte productgegevens (titel, prijs, beschrijving, kenmerken en de beelden van kleur Wit van de Shopify-CDN);
- Nunito Sans 400 en 700.

Screenshots op 390 x 844 (Chromium via Playwright, mobiele weergave) in `mockups/blinesleep/screenshots/shop/mobiel/`, met de metingen in `metingen.json`:

| Bestand | Wat je ziet |
|---|---|
| `01_eerste_scherm.png` | Balk, header, foto, teller, titel, score, prijs, kleurkeuze, meelopende knop |
| `02_balk_wisselend_bericht.png` | Balk na 6 seconden: tweede bericht |
| `03_galerij_tweede_beeld.png` | Na één keer vegen: teller 2/9 |
| `04_kleurkeuze_knop_vinkjes.png` | Kleurkeuze, knop, vier vinkjes, Beschrijving open |
| `05_uitklapblokken.png`, `06_kenmerken_open.png` | De vier uitklapblokken, Kenmerken open |
| `07_meelopende_knop.png` | Meelopende knop onderaan bij "Goed om te weten" |
| `08_voettekst.png` | Voettekst met tikdoelen van 44 px |
| `09_winkelwagenlade.png` | Lade over de volle breedte, Afrekenen onderaan in beeld |
| `10_desktop_controle.png` | Controle op desktop (1366 px): balk op één regel |

Wat de testpagina niet laat zien: het echte gedrag van Shopify (winkelwagen vullen, variant wisselen via de server, de cookiemelding van Shopify, apps of scripts die Shopify zelf toevoegt), andere pagina's dan de productpagina, en de echte laadtijd. De tekst in de lade onder het totaal is een benadering van de standaardtekst van Dawn.

### Checklist mobiel, per punt

| Nr | Punt | Stand | Gemeten op de testpagina |
|---|---|---|---|
| 1 | Balk op één regel, wisselende berichten | Gedaan | 37 px hoog, één regel, 16 px, bericht 2 na 6 s. Geen pijltjes op mobiel. |
| 2 | Header max ongeveer 60 px, winkelwagen altijd zichtbaar | Gedaan | 60 px. Header staat altijd bovenaan; het winkelwagen-icoon (44 x 44) toont het aantal zodra er iets in ligt (zo werkt Dawn). |
| 3 | Veegslider over de volle breedte met teller, geen miniaturen, eerste foto direct | Gedaan | Foto 390 px breed, teller "1/9", na vegen "2/9", pijltjes 44 x 44. Eerste beeld `eager` en `fetchpriority="high"`, de rest `lazy`. |
| 4 | Eerste scherm: foto, titel, score, prijs | Gedaan | Foto tot 499 px, titel 553, score 592, prijs 622 tot 674. De hoofdknop staat net onder de vouw (846); de meelopende knop staat dan al onderaan. |
| 5 | Kleurkeuze minimaal 44 x 44 met kleurnaam | Gedaan | Vlakken met kleurbolletje en naam, 44 px hoog en 88 tot 109 px breed. Geen productfoto's als keuze: dat vraagt tekstloze packshots (akkoordpunt 2). |
| 6 | Knop volle breedte, minimaal 48 px | Gedaan | 360 x 50 px. Ook Afrekenen in de lade 50 px. |
| 7 | Vier vinkjes direct onder de knop | Gedaan | Stonden er al, nu 16 px. |
| 8 | Uitklapblokken, Beschrijving open | Gedaan | Beschrijving (open), Kenmerken, Verzending en retour, Vragen; elke kop 51 px hoog. |
| 9 | Meelopende knop: volle breedte, prijs plus knop, max 64 px, niets anders dat zweeft | Gedaan, cookiemelding nog te testen | 390 x 64 px, knop 48 px. Ligt met z-index 20 onder de winkelwagenlade (1000) en verdwijnt zodra de lade, het menu of het zoekvenster open is. Houdt rekening met de onderrand van de iPhone. Er zweeft verder niets (geen chat, geen badge). De cookiemelding van Shopify staat nog uit (punt 9 van de Joost-lijst, sessie 4); zet Joost die aan, dan nakijken of de melding boven de knop ligt en weggaat na een keuze. |
| 10 | Geen pop-ups | Gedaan (gecontroleerd) | Geen app-embeds in het thema, geen nieuwsbrief-pop-up, geen apps toegevoegd. |
| 11 | Tekst en invoervelden 16 px, tikdoelen 44 px, ruimte in de voettekst | Gedaan | Op productpagina, balk, lade en voettekst geen enkele tekst onder 16 px. Invoervelden (aantal, zoeken, notitie) 16 px. Links in de voettekst 44 px hoog. Andere pagina's dan de productpagina niet gemeten; de regels gelden wel voor de hele winkel. |
| 12 | Snelheid, Lighthouse 80+ | Deels | Eén letter in twee gewichten (Nunito Sans 400 en 700), foto's via de Shopify-CDN met srcset (deed Dawn al), eerste foto niet lazy, geen apps. **Lighthouse niet gemeten**: kan pas met het winkelwachtwoord. |
| 13 | Winkelwagenlade volle breedte, Afrekenen altijd zichtbaar | Gedaan | Lade 390 px breed, Afrekenen op 778 tot 828 px, dus in beeld; het onderste deel van de lade blijft staan terwijl de producten scrollen. |

### Stijlcontrole

Nieuwe teksten (score, uitklapblokken Verzending en retour en Vragen, balkberichten) nagelopen op gedachtestreepjes, "u" en "uw", de schrapwoorden en gezondheidswoorden: geen treffers. De vragen zijn dezelfde als in sessie 5. Tekstenbestand bijgewerkt: `reports/bijlagen/Bline shop teksten.md`.

### Niet gedaan, bewust

- Wachtwoord blijft aan, geen prijzen gewijzigd, geen mails, geen betaalinstellingen, geen apps, geen nieuwe beelden, geen pop-ups.

### Wacht op Joost

1. **De echte test op een telefoon**: het winkelwachtwoord als omgevingsvariabele, of zelf de productpagina op je telefoon openen via Online Store > Thema's > Dawn > Voorbeeld. Daarna maak ik de echte screenshots en draai ik Lighthouse mobiel.
2. **Cookiemelding** aanzetten (Instellingen > Klantprivacy), daarna controleer ik punt 9 opnieuw.
3. Tekstloze packshots per kleur blijven nodig als we de kleurkeuze met foto's willen (akkoordpunt 2).
4. De overige punten uit sessie 4 en 5 blijven open.

## 5 oktober 2026, sessie 7: de 12 reviewpunten en de nieuwe functies

Opdracht van Joost (05-10), met akkoord op bundels, review-app en Collabs: de 12 punten uit `research_notes/Bline Sleep risicos en voorbeelden/kritische_review_shop_v1.md` uitvoeren, plus reviews, upsell, bundelregel, kruimelpad, blogs en de Collabs-tekst. "Kritisch zijn dat de webshop er echt goed uit komt te zien."

Toegang: de vaste winkelnaam die Joost doorgaf (niet de waarde in `BLINE_SHOPIFY_STORE`), sleutel via client credentials met `BLINE_SHOPIFY_CLIENT_ID` en `BLINE_SHOPIFY_CLIENT_SECRET`. Alleen de namen gecontroleerd. Geen SHOPIFY_*- of BOL_*-variabelen gebruikt. Vooraf een kopie gemaakt van alle 359 bestanden van Dawn (lokaal, map `backup_voor_s7`).

### Eerst gevonden

- **Judge.me stond al in het thema**: de app-embed (judgeme_core) en **twee** reviewblokken onderaan de productpagina, allebei met voorbeelddata. Het dubbele blok is weg.
- **De testpagina van sessie 6 week af van de echte winkel.** Die was met de hand nagebouwd. Nu rendert een lokale Liquid-renderer (liquidjs) de echte themabestanden met de echte productdata. Daardoor bleek: de knop heette in de winkel "Aan winkelwagen toevoegen" (niet "In winkelwagen"), onder de prijs stond "Belastingen inbegrepen. Verzendkosten worden berekend bij de checkout." (twee regels), en op desktop stond het menu wel uitgeschreven (de hamburger op de oude screenshot kwam door de testpagina, niet door het thema). Ook de teller toonde in werkelijkheid alle 31 beelden tot de alt-teksten werden gelezen; dat werkt nu wel (1/9 bij Wit).

### Werkwijze screenshots (benadering, lees dit)

De winkel staat achter het wachtwoord, dus de echte pagina's kon ik niet openen. Werkwijze: thema ophalen via de Admin API, lokaal renderen met de echte Liquid, CSS en JavaScript van Dawn en de echte producten, blogs, menu's en beelden van de Shopify-CDN; daarna Chromium via Playwright op 390 x 844 (mobiel, 2x) en 1366 x 800. Scripts in `mockups/blinesleep/testpagina/`.

Benaderd, dus niet echt: de Shopify-filters (nagebouwd), het reviewblok van Judge.me (nagebootst met dezelfde klassen, want app-blokken worden door Shopify zelf gevuld), de betaaliconen (grijze plaatsvervangers met de naam erin; Shopify zet de echte iconen), de winkelwagen (gevuld met testregels) en de datumnotatie op de blog.

Screenshots in `mockups/blinesleep/screenshots/shop/ronde2/`: product, homepage, lade (met en zonder hoes), hoes, collectie, blog, artikel, vergelijkingspagina en vragen, elk mobiel en desktop. Stand vóór deze sessie in `ronde2/voor/`. Naast de ENV-screenshots: `vergelijk_product_mobiel_env.jpg` en `vergelijk_home_env.jpg`. Metingen in `ronde2/metingen.json`.

Gewerkt in drie rondes (wijzigen, renderen, screenshots, punten aflopen). Ronde 1 liet zien: geselecteerd kleurvlak nog zwart gevuld (Dawn won), uitklapteksten nog ingesprongen, witruimte tussen product en reviews 64 tot 80 px, kop op de foto over het gezicht op mobiel, blog als collage met een enorm eerste beeld, Engelse knop "Share" onder artikelen, "Filteren en sorteren" bij 2 producten. Allemaal opgelost in ronde 2 en 3.

### De 12 punten

| Nr | Punt | Gedaan | Meting op de testpagina (mobiel / desktop) |
|---|---|---|---|
| 1 | Rangorde titel en prijs | ja | Titel 24 / 28 px, gewicht 700. Prijs 24 / 24 px, gewicht 700 (was 18 px, 400). |
| 2 | Ondertitel | ja | "Met vak voor je boek, 65 x 50 x 45 cm", 16 px, grijs, onder de score. Hoes: "Katoen 400 TC, met rits en zijvak". Ook op de homepage. |
| 3 | Geen Dawn-belastingtekst | ja | "Incl. btw", 14 px, grijs (60%), op dezelfde regel als de prijs. De zin over verzendkosten is weg (verzending is gratis). Ook in het uitgelichte product op de homepage. |
| 4 | "Kleur: Wit" | ja | Label "Kleur: **Wit**", de kleurnaam wisselt mee bij een andere keuze (Shopify ververst het label, `bline.js` doet het meteen). |
| 5 | Rechte hoeken beelden en kaarten | ja | Afronding beelden, productkaarten, collectiekaarten en blogkaarten 0 px (was 6). |
| 6 | Bijna zwarte, compacte tekst | ja | Lopende tekst rgb(26,26,26) (was 75%), regelafstand 1,5 (24 px bij 16 px), letterafstand 0, inspringing in de uitklapblokken 0 px (was 10). |
| 7 | Rustige balk | ja | 13 px, gewicht 600, letterafstand 0,06 em, mobiel en desktop. Balk 35 px hoog op mobiel (was 37). |
| 8 | Menu uitgeschreven op desktop | ja | Leeskussen, Losse hoes, Over Bline, Vragen naast het logo, 15 px vet; geen hamburger op desktop (gemeten: 0 px). Mobiel hamburger 44 x 44. "Alle leeskussens" en "Contact" uit het hoofdmenu (Contact staat in de voettekst). |
| 9 | Betaaliconen bij de knop | ja | Rij onder de vinkjes en de bundelregel: iDEAL, Bancontact, Apple Pay, Visa, Mastercard (`payment_type_svg_tag`, standaard Shopify), 38 x 24 px. |
| 10 | Minder witruimte | ja | Tussen blokken mobiel 32 px, desktop 48 px (gemeten: uitklapblokken naar reviews 32 / 48, foto homepage naar product 32 / 48, kenmerken naar vragen 40 / 48). "Goed om te weten" en de vinkjesbalk blijven in het lichte vlak. |
| 11 | Knoppen en kleurvlakken | ja | Hoeken 4 px (knoppen, kleurvlakken, invoer). Kleurvlak: rand 1 px 25% grijs, bij hover 1 px #1A1A1A, gekozen 2 px #1A1A1A op wit met vette naam (niet meer zwart gevuld). Mobiel 44 px hoog, 16 px tekst. |
| 12 | Homepage op dezelfde lat | ja | Foto met mens, kop van 4 woorden onderaan de foto (mobiel niet meer over het gezicht), één knop "Shop nu", daarna product met score en ondertitel, vinkjesbalk, kenmerken, vragen. Geen pop-ups en geen zwevende knoppen (gemeten: alleen de lade en de meelopende knop). |

Alle 12 op "ja", gemeten op de testpagina. De echte test op een telefoon blijft nodig zodra het wachtwoord eraf mag.

### Functies

**1. Reviews (Judge.me).** Eigen sectie `bline-reviews` met alleen het reviewblok van de app, direct onder het product (dus onder Kenmerken) en boven "Goed om te weten". Geen sterrenbadge, geen zwevende tab, geen carrousel, geen pop-up; in `bline.css` staan die onderdelen van Judge.me ook nog eens op verborgen. Huisstijl via CSS: Nunito Sans, kop in hoofdletters, sterren en knop in inktblauw, knop 4 px hoeken en 44 px hoog. De bol-score onder de titel blijft. Let op: de instelling "review_data: sample_data" is volgens Judge.me alleen de voorbeeldweergave in de themaeditor; in de winkel toont het blok altijd de echte reviews (nu nog geen). Shopify controleert de waarden van app-instellingen niet, dus ik heb hem laten staan in plaats van een gok te doen.

**2. Upsell in de lade.** Onder het eerste leeskussen, zolang er geen hoes in de winkelwagen ligt: "Extra hoes erbij? **€9,99 korting**" met een knop (86 x 44 px op mobiel). Hoeskleur: Wit naar Beige, Beige naar Wit, Blauw naar Grijs, Grijs naar Blauw, Zwart naar Grijs; is die uitverkocht, dan een andere beschikbare kleur. De knop voegt de hoes toe via `/cart/add.js` en ververst de lade. Getest: het verzoek vraagt de beige hoes (juiste variant), daarna staan kussen en hoes in de lade, de upsellregel is weg en het totaal is €94,99 (de automatische korting uit het bundellogboek). Snippet `bline-upsell`.

**3. Bundelregel** onder de vinkjes (alleen leeskussen): "Extra hoes of tweede leeskussen erbij? Dan krijg je €9,99 korting." Kort gemaakt uit de twee bundelteksten.

**4. Kruimelpad** met BreadcrumbList (schema.org) op product (Home / Leeskussens / product, boven de titel, op mobiel onder de foto zoals Tofvel), collectie, blog, artikel en pagina's (boven de inhoud). Gecontroleerd in de gerenderde HTML: geldige JSON, posities 1 tot 3, volledige adressen.

**5. Lade.** "Kleur: Wit" met spatie (de spatie staat nu vast in de code), totaal zonder "EUR" (ook op de winkelwagenpagina), en onder het totaal "Incl. btw. Gratis verzending in NL en BE." in plaats van "Kortingen en verzending worden bij de checkout berekend".

**6. Blog en pagina's.** Zes artikelen en de pagina "Leeskussen of losse kussens" gepubliceerd. Artikel 2 linkt onder de tabel naar die pagina. "Blog" in het voettekstmenu Klantenservice. De vijf nieuwe vragen staan als uitklapblok 12 tot 16 op de vragenpagina en zijn uit de paginatekst gehaald. Blog als raster in plaats van collage, de Engelse deelknop onder artikelen weg, het artikelbeeld middelhoog. Filter en sortering op de collectiepagina uit (2 producten). Paginatitels rustiger (32 / 40 px).

**7. Collabs.** Aanmeldtekst (108 woorden) in `reports/bijlagen/Bline collabs aanmeldtekst.md`.

### Gewijzigde themabestanden

`assets/bline.css`, `assets/bline.js`, `config/settings_data.json` (hoeken en sectieruimte), `layout/theme.liquid` (kruimelpad), `locales/nl.json` (knop, "Incl. btw", tekst onder het totaal), `sections/main-product.liquid` en `sections/featured-product.liquid` (regel over verzendkosten weg), `sections/main-cart-footer.liquid` en `snippets/cart-drawer.liquid` (totaal, spatie, upsell), `snippets/product-variant-picker.liquid` (Kleur: Wit), de sjablonen `product`, `product.hoes`, `index`, `collection`, `blog`, `article`, `page.veelgestelde-vragen`. Nieuw: `sections/bline-reviews.liquid`, `snippets/bline-kruimel.liquid`, `bline-upsell.liquid`, `bline-bundelregel.liquid`, `bline-betaal.liquid`.

Controle met de Admin API: elke upload gaf nul fouten; daarna het hele thema opnieuw opgehaald en vergeleken met wat ik verstuurde: alle bestanden gelijk. Geen "Translation missing" in de gerenderde pagina's. Ook via de API: hoofdmenu en voettekstmenu, artikelen en twee pagina's.

### Stijlcontrole

Script over alle nieuwe teksten (ondertitels, btw, knop, lade, bundelregel, upsell, kruimelpad, link in artikel 2, vragen 12 tot 16, Collabs-tekst): schrapwoorden uit de gids, AI-zinnen, gedachtestreepjes (lang, half, los streepje), "u" en "uw", uitroeptekens, superlatieven en gezondheidswoorden. 0 treffers. Het woord "gezondheid" in de Collabs-tekst is bewust: het is de regel voor creators ("zonder beloftes over gezondheid"), geen claim.

### Niet gedaan, bewust

- Wachtwoord blijft aan (gecontroleerd na afloop: home, product, blog en de vergelijkingspagina sturen door naar `/password`). Geen prijzen gewijzigd, geen mails, geen betaalinstellingen, geen nieuwe apps, geen nieuwe beelden.

### Wacht op Joost

**Judge.me** (in de Judge.me-app, niet in het thema):
1. Instellingen > Widgets > Review Widget > Thema: kies **Default** of **Align**, niet **Slider** (dat is een carrousel).
2. Zet uit: zwevende reviewtab (Floating Reviews Tab), pop-up (Reviews Pop-up), carrousel (Reviews Carousel), en "Verified Reviews Count Badge" als zwevend element. Het thema verbergt ze ook, maar uit is beter.
3. Instellingen > Taal: Nederlands. Controleer dat de kop "Klantreviews" is en de knop "Schrijf een review".
4. Kleuren: sterren en knop #1F2A37 (inktblauw), knoptekst wit.
5. Reviewverzoek na bezorging: aan, één mail, 14 dagen na fulfilment (past bij funnelstap 5 in het groeiplan). Geen korting als beloning.
6. Optioneel in de themaeditor (Online Store > Thema's > Dawn > Aanpassen > Leeskussen > sectie "Bline reviews" > blok Review Widget): "(Preview only)" op **Real data** zetten; dit verandert alleen de voorbeeldweergave.

**Shopify Collabs** (Apps > Shopify Collabs):
1. Programma aanmaken, aanmeldpagina aan, de tekst uit `reports/bijlagen/Bline collabs aanmeldtekst.md` plakken.
2. Commissie 10%, producten Leeskussen Bline en de losse hoes.
3. Kortingscode voor volgers: **uit**.
4. Gratis product: ja, handmatig goedkeuren per creator.
5. Aanmeldingen handmatig goedkeuren.

**Verder**
1. Betaaliconen in de voettekst verschijnen pas als Shopify Payments of een andere betaalprovider actief is (Shopify vult ze zelf). De rij bij de knop staat vast in het thema.
2. De echte test op de telefoon en Lighthouse zodra het wachtwoord eraf mag (zie sessie 6).
3. De overige punten uit sessie 4 tot en met 6 blijven open.

## 5 oktober 2026, sessie 8: elke kleur een eigen product

Opdracht: `prompts/bline-kleur-als-product.md`. Besluit Joost (05-10): "Elke kleur als eigen product", eerder "je moet ook alle producten natuurlijk aanmaken dan kan je later nog wel de afbeeldingen toevoegen" en "top ga door".

Toegang: de vaste winkelnaam die Joost doorgaf (niet de waarde in `BLINE_SHOPIFY_STORE`), sleutel via client credentials met `BLINE_SHOPIFY_CLIENT_ID` en `BLINE_SHOPIFY_CLIENT_SECRET`. Alleen de namen gecontroleerd. Geen SHOPIFY_*- of BOL_*-variabelen gebruikt. Admin GraphQL, versie 2026-10.

Vooraf: export van de twee oude producten (alle velden, varianten, voorraad, beelden, metafields, kanalen) in `reports/bijlagen/Bline export oude producten 2026-10-05.json`; kopie van alle 364 themabestanden van Dawn (lokaal, map `backup_voor_s8`); kopie van menu, doorverwijzingen, kortingen en de artikel- en paginateksten (lokaal).

### De 10 producten (alle actief, kanaal Online Store, wachtwoord aan)

| Product | Handle | SKU | EAN | Prijs | Voorraad | Beelden | Status |
|---|---|---|---|---|---|---|---|
| Leeskussen Bline Wit | leeskussen-wit | BLINE-LK-WIT | 8720892179074 | €69,99 | 241 | 9 | actief |
| Leeskussen Bline Beige | leeskussen-beige | BLINE-LK-BEIGE | 8720892687241 | €79,99 | 39 | 6 | actief |
| Leeskussen Bline Blauw | leeskussen-blauw | BLINE-LK-BLAUW | 8720892687258 | €79,99 | 86 | 7 | actief |
| Leeskussen Bline Grijs | leeskussen-grijs | BLINE-LK-GRIJS | 8720892687265 | €79,99 | 78 | 7 | actief |
| Leeskussen Bline Zwart | leeskussen-zwart | BLINE-LK-ZWART | 8720892687272 | €79,99 | 80 | 6 | actief |
| Losse hoes Wit voor leeskussen Bline | hoes-wit | BLINE-HOES-WIT | 8720892179098 | €29,99 | 27 | 2 | actief |
| Losse hoes Beige voor leeskussen Bline | hoes-beige | BLINE-HOES-BEIGE | 8720892687203 | €34,99 | 38 | 2 | actief |
| Losse hoes Blauw voor leeskussen Bline | hoes-blauw | BLINE-HOES-BLAUW | 8720892687210 | €34,99 | 85 | 2 | actief |
| Losse hoes Grijs voor leeskussen Bline | hoes-grijs | BLINE-HOES-GRIJS | 8720892687227 | €34,99 | 77 | 2 | actief |
| Losse hoes Zwart voor leeskussen Bline | hoes-zwart | BLINE-HOES-ZWART | 8720892687234 | €34,99 | 80 | 2 | actief |

Prijzen gelijk aan de tabel in de opdracht (en aan bol). Per product overgenomen van de oude variant: beschrijving, metafields `bline.*` (afmetingen, vulling, hoesstof, wasvoorschrift, gewicht, inhoud doos), Google-productcategorie (4456 voor het kussen, 2927 voor de hoes) en conditie, Shopify-categorie, merk Bline, producttype, gewicht (kussen 3,9 kg; hoes 0, gewicht nog onbekend), voorraad op de locatie, belasting, voorraadbeleid en het sjabloon (hoezen op `product.hoes`). Eén variant per product (geen optie meer).

- **Beelden**: de bestaande bestanden zijn aan het nieuwe product gekoppeld, niet opnieuw geüpload. Kussen: de beelden van die kleur in de volgorde van sessie 3, met de maattekening als laatste. Hoes: hoofdbeeld en rits-detail van die kleur. Alt-teksten staan op het bestand en zijn dus gelijk gebleven (met "kleur Beige" enzovoort). De oude producten houden hun beelden (31 en 10).
- **SEO**: kussen "Leeskussen Beige met vak voor je boek | Bline", metabeschrijving "Leeskussen in beige van 65 x 50 x 45 cm met 3,8 kg traagschuim en een katoenen hoes die in de was kan. Gratis verzending in NL en BE." (131 tot 133 tekens). Hoes "Losse hoes Beige voor het leeskussen | Bline", "Katoenen hoes (400 TC) in beige met onzichtbare rits voor het Bline leeskussen. Wasbaar op 30 °C. Gratis verzending in NL en BE." (126 tot 128 tekens).
- **Nieuwe metafield-definities** (namespace `bline`, product): `kleur_naam` (tekst), `kleur_hex` (kleur; Wit #F1EFEC, Beige #CDBFA9, Blauw #4A5878, Grijs #9A9690, Zwart #2B2B2D, gelijk aan de kleurcodes in de thema-instellingen) en `kleuren` (lijst met productreferenties). `kleuren` staat op elk product met de 5 producten van dezelfde soort, volgorde Wit, Beige, Blauw, Grijs, Zwart.

### Oude producten

- "Leeskussen Bline" (`leeskussen`) en "Hoes voor leeskussen Bline" (`hoes-leeskussen`): status **concept**, van het kanaal Online Store gehaald. Niet verwijderd.
- Let op: ze houden hun SKU's, EAN's en voorraad. Shopify staat dubbele SKU's toe en de producten zijn niet zichtbaar, maar bij het koppelen van ChannelDock alleen de 10 nieuwe producten koppelen (of de oude dan verwijderen, met akkoord).

### Collecties en menu

- **Leeskussens**: de 5 kussens, handmatige volgorde Beige, Wit, Grijs, Blauw, Zwart. De oude producten eruit. Nieuwe omschrijving: "Het Bline leeskussen in vijf kleuren: beige, wit, grijs, blauw en zwart. Een losse hoes vind je bij Hoezen." Metabeschrijving aangepast.
- **Hoezen** (nieuw, `hoezen`, op Online Store): de 5 hoezen in dezelfde volgorde, met omschrijving, SEO-titel "Losse hoezen voor het leeskussen | Bline" en metabeschrijving.
- **Hoofdmenu**: Leeskussens (collectie), Losse hoezen (collectie Hoezen), Over Bline, Vragen.

### Doorverwijzingen

| Pad | Was | Nu |
|---|---|---|
| /products/leeskussen | (product) | nieuw: /products/leeskussen-beige |
| /products/hoes-leeskussen | (product) | nieuw: /products/hoes-beige |
| /products/leeskussen-wit, -beige, -blauw, -grijs, -zwart | oude product met kleur gekozen | verwijderd: op dat pad staat nu het product in die kleur zelf |
| /products/hoes-wit, -beige, -blauw, -grijs, -zwart | oude hoes met kleur gekozen | verwijderd, zelfde reden |
| /collections/hoezen | oude hoes | door Shopify zelf verwijderd bij het aanmaken van de collectie Hoezen (het pad is nu de collectie) |
| /products/leeskussen-met-hoes | oude product | /products/leeskussen-beige |
| /products/hoes | oude hoes | /collections/hoezen |
| /collections/leeskussen en de 9 paginapaden | ongewijzigd | ongewijzigd |

Daarmee wijzen alle 22 oude paden van uwleeskussen.nl naar de juiste kleur, de juiste collectie of de pagina; 11 ervan zijn nu een echte pagina in plaats van een doorverwijzing.

### Thema (Dawn, gepubliceerd)

| Bestand | Wijziging |
|---|---|
| `snippets/bline-kleurkeuze.liquid` (nieuw) | "Kleur: **Beige**" en vijf kleurvlakken met bolletje en naam, als links naar het product in die kleur. Leest `bline.kleuren`, `kleur_naam` en `kleur_hex`. Huidige kleur gemarkeerd (rand 2 px, vet, `aria-current`). Uitverkochte kleur: grijs en doorgestreept, met "(uitverkocht)" voor schermlezers. |
| `templates/product.json` en `product.hoes.json` | Blok variantkeuze vervangen door de kleurkeuze, op dezelfde plek (onder de prijs, boven de knop). De rest is gelijk: kruimelpad, titel, score (alleen kussen), ondertitel, prijs, knop, vinkjes, bundelregel (alleen kussen), betaaliconen, uitklapblokken, reviewblok, "Goed om te weten", meelopende knop. |
| `snippets/bline-upsell.liquid` | Kiest de hoes als ander product: Wit naar hoes-beige, Beige naar hoes-wit, Blauw naar hoes-grijs, Grijs naar hoes-blauw, Zwart naar hoes-grijs; is die uitverkocht, dan een andere beschikbare kleur (niet de eigen kleur). Geen upsell als er al een hoes in de winkelwagen ligt. |
| `snippets/cart-drawer.liquid` | Upsell onder het eerste kussen (handle begint met `leeskussen-`). |
| `snippets/bline-kruimel.liquid` | Hoes: Home / Hoezen / product (kussen blijft Home / Leeskussens / product). |
| `templates/index.json` | Uitgelicht product vervangen door twee rasters: Leeskussens (5 kaarten) en Losse hoezen (5 kaarten), 2 kolommen op mobiel, 5 op desktop, vierkante foto's. Knop "Shop nu" naar de collectie Leeskussens. Kenmerken lezen nu leeskussen-beige. |
| `templates/collection.json` | 5 kolommen op desktop (alle kaarten op één rij), vierkante foto's. |
| `assets/bline.css` | Stijl van de kleurvlakken (zelfde maten als punt 5 en 11) en kaarttitels 16 px op mobiel. |

Controle met de Admin API: `themeFilesUpsert` gaf nul fouten voor alle 9 bestanden. Daarna het hele thema (365 bestanden) opnieuw opgehaald en vergeleken met wat ik verstuurde: alles gelijk. Geen "Translation missing" in de gerenderde pagina's.

### Links in blogs en pagina's

Zes artikelen en de pagina "Leeskussen of losse kussens" linkten naar `/products/leeskussen`. Nu: vijf artikelen naar `/collections/leeskussens`, het wasartikel en de vergelijkingspagina naar `/products/leeskussen-beige` (daar gaat het om maten en wasvoorschrift). Linkteksten niet veranderd. Details in `reports/Bline blogs logboek.md`. In het thema, de menu's en de andere pagina's stond geen link meer naar een oud product (gecontroleerd).

### Bundelkortingen herrekend

Beide kortingen wijzen nu naar de collecties Leeskussens en Hoezen. draftOrderCalculate (alleen berekend, geen order):

| Scenario | Totaal | Verwacht | Klopt |
|---|---|---|---|
| Beige kussen + blauwe hoes | €104,99 | €104,99 | ja |
| Wit kussen + blauwe hoes | €94,99 | €94,99 | ja |
| 2 beige kussens | €149,99 | €149,99 | ja |
| 1 beige kussen zonder hoes | €79,99 | geen korting | ja |
| Extra: 2 beige kussens + 2 blauwe hoezen | €219,97 | één korting | ja |
| Extra: beige + grijs kussen (twee producten) | €149,99 | €149,99 | ja |
| Extra: alleen een blauwe hoes | €34,99 | geen korting | ja |

Details in `reports/Bline bundels logboek.md`.

### Testpagina-screenshots (werkwijze sessie 6 en 7, benadering)

Thema en data opnieuw opgehaald, lokaal gerenderd met de echte Liquid, CSS en JavaScript en de 10 nieuwe producten, daarna Chromium op 390 x 844 en 1366 x 800. Screenshots en metingen in `mockups/blinesleep/screenshots/shop/ronde3/`. Scripts bijgewerkt in `mockups/blinesleep/testpagina/`. Dezelfde beperkingen als in sessie 7: Judge.me nagebootst, betaaliconen als plaatsvervangers, winkelwagen niet echt gevuld.

| Pagina | Mobiel / desktop |
|---|---|
| Collectie Leeskussens | 5 kaarten, mobiel 2 kolommen (178 px breed), desktop 5 op één rij; volgorde Beige, Wit, Grijs, Blauw, Zwart; kaarttitel 16 px op mobiel |
| Leeskussen Beige | eerste scherm gelijk aan ronde 2 (foto, teller 1/6, kruimelpad, titel, score, ondertitel, prijs, meelopende knop); "Kleur: Beige" 16 px; kleurvlakken 44 px hoog, 85 tot 106 px breed; gekozen vlak rand 1 px plus 1 px binnenrand = 2 px, vet; knop 360 x 50 |
| Hoes Blauw | kruimelpad Home / Hoezen / product, "Kleur: Blauw", teller 1/2, geen score en geen bundelregel (zoals bij de oude hoes) |
| Lade met upsell | Leeskussen Bline Beige, upsell "Extra hoes erbij? €9,99 korting" met knop "+ Wit" (44 px hoog), Afrekenen 50 px in beeld. Klik getest: het verzoek vraagt de variant van hoes-wit, daarna staan kussen en hoes in de lade, de upsell is weg, totaal €99,99 |
| Homepage | foto, kop, "Shop nu", raster Leeskussens, raster Losse hoezen, vinkjes, kenmerken, vragen |

**De 12 reviewpunten op de nieuwe pagina's**

| Nr | Punt | Stand |
|---|---|---|
| 1 | Rangorde titel en prijs | ja: titel 24 / 28 px, prijs 24 px, beide 700 |
| 2 | Ondertitel | ja, kussen en hoes |
| 3 | "Incl. btw" | ja, 14 px grijs naast de prijs |
| 4 | "Kleur: Beige" | ja, nu vast per product (de kleur hoort bij de pagina) |
| 5 | Rechte hoeken beelden en kaarten | ja, ook de nieuwe kaarten op home en collectie |
| 6 | Bijna zwarte, compacte tekst | ja, ongewijzigd |
| 7 | Rustige balk | ja, ongewijzigd |
| 8 | Menu uitgeschreven op desktop | ja: Leeskussens, Losse hoezen, Over Bline, Vragen |
| 9 | Betaaliconen bij de knop | ja |
| 10 | Minder witruimte | ja, rasters 48 / 24 px boven en onder |
| 11 | Knoppen en kleurvlakken | ja: 4 px hoeken, rand 1 px 25% grijs, hover 1 px #1A1A1A, gekozen 2 px |
| 12 | Homepage | ja, met één verschil: de score stond onder het uitgelichte product en staat nu alleen in de balk en op de productpagina's |

Ook nagelopen: geen tekst onder 16 px op mobiel (behalve kruimelpad 14 px en "Incl. btw" 14 px, zoals in sessie 7); niets zwevends behalve lade en meelopende knop. Op de hoespagina loopt het kruimelpad op mobiel over twee regels door de lange titel; leesbaar, laten staan.

### Stijlcontrole

Script over alle nieuwe teksten (10 titels, SEO-titels en metabeschrijvingen, twee collectieteksten met SEO, de rasterteksten op de homepage, het label "Kleur:", de metafield-omschrijvingen): schrapwoorden, AI-zinnen, gedachtestreepjes (lang, half, los streepje), "u" en "uw", uitroeptekens, superlatieven en gezondheidswoorden. 0 treffers. Het funnel- en advertentieplan is bijgewerkt met een landingspagina per kleur.

### Gecontroleerd na afloop

- Wachtwoord staat aan: home, `/products/leeskussen-beige`, `/collections/leeskussens` en `/collections/hoezen` sturen door naar `/password`.
- Geen prijzen anders dan de tabel, geen mails, geen betaalinstellingen, geen nieuwe apps, geen nieuwe beelden.

### Wacht op Joost

**Judge.me: de vijf kussens als één productgroep** (zodat reviews niet per kleur versnipperen):
1. Judge.me > Settings > **Product Groups** (soms onder "Reviews" > "Product groups").
2. **Create group**, naam "Leeskussen Bline". Voeg toe: Leeskussen Bline Wit, Beige, Blauw, Grijs en Zwart. Sla op. Elke kleur toont dan alle reviews van de groep en dezelfde score.
3. Optioneel een tweede groep "Losse hoes" met de 5 hoezen.
4. Controleer of reviews die eventueel nog op het oude "Leeskussen Bline" (concept) staan, worden overgezet: in Judge.me > Reviews filteren op dat product en met "Move reviews" naar Leeskussen Bline Beige verplaatsen (nu zijn er nog geen reviews).
5. Zet bij de bol-import (als je die later gebruikt) alle kleuren in dezelfde groep.

**Verder**
1. ChannelDock: alleen de 10 nieuwe producten koppelen (de oude op concept hebben dezelfde SKU en EAN).
2. Google- en Meta-app: na het koppelen controleren dat de feed 10 producten toont en de 2 oude niet.
3. Gewicht van de losse hoes (staat nog op 0).
4. De echte test op de telefoon zodra het wachtwoord eraf mag, en de overige punten uit sessie 4 tot en met 7.

## 5 oktober 2026, sessie 9: oude producten weg, telefoon en vertrouwensblokken

Opdracht van Joost (05-10, via de hoofdsessie): "ja verwijder de oude producten, ga door" en "telefoonnummer mag erop". Uitvoering van hoofdstuk 2 en 4 van `reports/Bline beeld- en vertrouwensplan.md` (zonder de nieuwe beelden).

Toegang: de vaste winkelnaam die Joost doorgaf (niet de waarde in `BLINE_SHOPIFY_STORE`), sleutel via client credentials met `BLINE_SHOPIFY_CLIENT_ID` en `BLINE_SHOPIFY_CLIENT_SECRET`. Alleen de namen gecontroleerd. Geen SHOPIFY_*- of BOL_*-variabelen gebruikt. Admin GraphQL, versie 2026-10. Vooraf een kopie van alle 365 themabestanden van Dawn (lokaal, map `backup_voor_s9`) en van de pagina's, het beleid, de collecties, kortingen, menu's en doorverwijzingen.

### 1. Oude producten verwijderd

**Vooraf gecontroleerd**
- Export `reports/bijlagen/Bline export oude producten 2026-10-05.json` bestaat en is compleet: per product beschrijving, SEO, alle metafields (10 en 8), alle beelden (31 en 10), vijf varianten met SKU, EAN, prijs, gewicht en voorraad per locatie. Vergeleken met de live producten: alles gelijk.
- Beide producten op **concept**, op **0** verkoopkanalen.
- Geen verwijzingen meer in: collecties Leeskussens en Hoezen, beide bundelkortingen, hoofd- en voettekstmenu, het thema (alle 365 bestanden doorzocht), de pagina's, artikelen en beleidsteksten, en de metafields `bline.kleuren` van de 10 producten. Alleen de oude collectie "Homepage" (`frontpage`, niet gebruikt in het thema) bevatte het oude kussen nog; die koppeling verdween met het verwijderen.
- **Beelden**: de 41 beeldbestanden van de oude producten zijn dezelfde bestanden als die van de 10 nieuwe producten (gedeeld, sessie 8). Om ze niet mee te verwijderen eerst de koppeling met de oude producten losgemaakt (`fileUpdate`, `referencesToRemove`), gecontroleerd dat de 10 nieuwe producten nog precies dezelfde beelden hadden, en pas daarna verwijderd.

**Verwijderd** (`productDelete`, geen fouten): "Leeskussen Bline" (`leeskussen`) en "Hoes voor leeskussen Bline" (`hoes-leeskussen`).

**Gecontroleerd na afloop**
- 10 producten, elk met dezelfde beelden als vooraf (alle beelden status READY).
- 10 varianten; elke SKU en elke EAN komt precies één keer voor.
- Doorverwijzingen staan nog: `/products/leeskussen` naar `/products/leeskussen-beige`, `/products/hoes-leeskussen` naar `/products/hoes-beige`. (Zelf openen kan pas als het wachtwoord eraf is; nu sturen beide paden door naar `/password`.)
- Opmerking voor ChannelDock (sessie 8): de dubbele SKU's zijn weg, dus koppelen kan zonder op te letten.

### 2. Telefoonnummer

Tekst overal: "Bel of app ons: 06 38 66 28 33", met een link `tel:+31638662833`.

| Plek | Wat |
|---|---|
| Voettekst (blok Bline, bedrijfsgegevens) | eigen regel onder het mailadres |
| Pagina Contact | onder de eerste alinea, en bij Gegevens tussen e-mail en KvK |
| Beleid Contactgegevens (Instellingen > Beleid) | tussen e-mail en KvK |
| Pagina Verzending | onder "Pakket beschadigd?" (na de mailzin) |
| Pagina Retourneren | stap 1: "Liever eerst even overleggen? Bel of app ons: 06 38 66 28 33." en bij "Iets kapot of niet goed?" na "Mail ons, met een foto." |
| Pagina Over Bline | onderaan, onder de mailzin |

**Winkelinstellingen**: het telefoonnummer staat al in het winkeladres (Instellingen > Algemeen), als 31638662833. De Admin API heeft geen mutatie om het winkeladres of de winkeltelefoon te wijzigen, dus de schrijfwijze heb ik niet aangepast. Wil Joost hem als "+31 6 38 66 28 33" zien: in Instellingen > Algemeen > Winkeladres aanpassen.

### 3. "Ook te koop bij bol.com"

Eén rustige regel, 16 px, grijs (75%), zonder logo en zonder link: "Ook te koop bij bol.com. 4,5 uit 5 op basis van 13 reviews." Bron gelijk aan de score (bol Ratings API, 05-10-2026, 13 reviews, gemiddeld 4,54).
- **Homepage**: eigen sectie `bline-bol` direct onder het raster Leeskussens, boven Losse hoezen.
- **Productpagina's van de 5 kussens** (`templates/product.json`): direct onder de betaaliconen (gemeten: het element direct na de betaalrij). Niet op de hoezen (die hebben ook geen score).

### 4. Over Bline en "Gemaakt door Bline uit Borne"

- **Over Bline** heeft een eigen sjabloon `page.over-bline` met bovenaan de sectie "Bline foto". Die toont niets zolang er geen beeld is gekozen (geen plaatsvervanger; gemeten: 0 beelden op de pagina). Foto kiezen: Online Store > Thema's > Dawn > Aanpassen > pagina Over Bline > "Bline foto".
- **Tekst** in de vorm van het plan: wie (Joost, klein bedrijf), waar (Borne, Brasem), waarom dit kussen (wat het doet: blijft staan, 3,8 kg traagschuim, vak opzij, hoes in de was), al verkocht via bol.com (4,5 uit 5, 13 reviews), magazijn Vianen, de vier beloftes, mail en telefoon. Alleen feiten uit de productgegevens, het masterprompt en de bol-score. Joosts eigen reden om met dit kussen te beginnen staat nergens: **[NAVRAGEN]**, dan zet ik er één zin bij. Alleen de voornaam gebruikt; de achternaam kan erbij als Joost dat wil.
- **Productpagina's van de kussens**, onderaan (na "Goed om te weten"): sectie `bline-gemaakt`, "Gemaakt door Bline uit Borne" (vet, 16 px) en de link "Over Bline" (16 px, tikdoel 44 px hoog). Er kan in de themaeditor dezelfde foto bij (96 x 96 px); zonder foto toont het blok alleen tekst.

### Gewijzigde themabestanden

Nieuw: `snippets/bline-bol.liquid`, `sections/bline-bol.liquid`, `sections/bline-foto.liquid`, `sections/bline-gemaakt.liquid`, `templates/page.over-bline.json`. Gewijzigd: `templates/index.json`, `templates/product.json`, `sections/footer-group.json`, `assets/bline.css`. Ook gewijzigd via de API: pagina's Contact, Over Bline (tekst en sjabloon), Verzending, Retourneren en het beleid Contactgegevens.

Controle met de Admin API: `themeFilesUpsert` gaf nul fouten voor alle uploads. Daarna het hele thema (370 bestanden) opnieuw opgehaald en vergeleken: alles gelijk aan wat ik verstuurde (JSON-bestanden inhoudelijk gelijk; Shopify zet er alleen een kopcommentaar boven). Pagina's en beleid opnieuw opgehaald: tekst gelijk. Geen "Translation missing" in de gerenderde pagina's.

### Testpagina-screenshots (werkwijze sessie 6 tot 8, benadering)

Thema en data opnieuw opgehaald na alle wijzigingen, lokaal gerenderd met de echte Liquid, CSS en JavaScript, Chromium op 390 x 844 en 1366 x 800. Screenshots en metingen in `mockups/blinesleep/screenshots/shop/ronde4/`: homepage en Leeskussen Beige (eerste scherm en volledig), lade, plus uitsneden van de bol-regel onder het raster en onder de betaaliconen, het blok "Gemaakt door", de voettekst met telefoon en de pagina Over Bline. Dezelfde beperkingen als eerder: Judge.me nagebootst, betaaliconen als plaatsvervangers, winkelwagen niet echt gevuld.

| Meting | Mobiel | Desktop |
|---|---|---|
| Bol-regel productpagina | 16 px, direct onder de betaalrij, geen link, geen beeld | idem |
| Bol-regel homepage | 16 px, tussen raster Leeskussens en Losse hoezen | idem, één regel |
| "Gemaakt door" | kop 16 px vet #1A1A1A, link 16 px, 44 px hoog | idem |
| Telefoon in voettekst | 16 px, tel:-link | idem |
| Over Bline | geen beeld zolang er geen foto is; telefoon onderaan | idem |

**De 12 reviewpunten**

| Nr | Punt | Stand |
|---|---|---|
| 1 | Rangorde titel en prijs | ja: titel 24 / 28 px, prijs 24 px, beide 700 |
| 2 | Ondertitel | ja |
| 3 | "Incl. btw" | ja |
| 4 | "Kleur: Beige" | ja |
| 5 | Rechte hoeken beelden en kaarten | ja, 0 px |
| 6 | Bijna zwarte, compacte tekst | ja, ongewijzigd |
| 7 | Rustige balk | ja: 13 px, 600 |
| 8 | Menu uitgeschreven op desktop | ja (mobiel hamburger 44 x 44) |
| 9 | Betaaliconen bij de knop | ja, met de bol-regel er direct onder |
| 10 | Minder witruimte | ja: de bol-regel zit tussen de rasters zonder extra ruimte boven, 24 px onder |
| 11 | Knoppen en kleurvlakken | ja: 4 px hoeken, gekozen vlak 2 px |
| 12 | Homepage | ja: foto, kop, "Shop nu", raster Leeskussens, bol-regel, raster Losse hoezen, vinkjes, kenmerken, vragen. Niets zwevends behalve lade en meelopende knop |

Ook nagelopen: op mobiel geen zichtbare tekst onder 16 px behalve kruimelpad en "Incl. btw" (14 px, zoals eerder) en de knop "Shop nu" (15 px, Dawn).

### Stijlcontrole

Script over alle nieuwe teksten (Over Bline, de telefoonregels op Contact, Verzending, Retourneren en het beleid, de bol-regel, "Gemaakt door Bline uit Borne"): schrapwoorden, gedachtestreepjes (lang, half, los streepje), "u" en "uw", uitroeptekens, superlatieven en gezondheidswoorden. 0 echte treffers (het script vond "beste" in "bestelling" en "bestellen"). Tekstenbestand bijgewerkt: `reports/bijlagen/Bline shop teksten.md`.

### Niet gedaan, bewust

- Wachtwoord blijft aan (gecontroleerd: de oude productpaden sturen door naar `/password`). Geen prijzen gewijzigd, geen mails, geen betaalinstellingen, geen nieuwe apps, geen nieuwe beelden, geen Higgsfield-beelden.

### Wacht op Joost

1. **Foto van Joost**: uploaden en kiezen in de sectie "Bline foto" op Over Bline (en eventueel dezelfde in "Bline gemaakt door" op de productpagina). Liever stuur je hem door, dan zet ik hem erop.
2. **Waarom dit kussen, in je eigen woorden** [NAVRAGEN]: één of twee zinnen, dan voeg ik ze toe aan Over Bline.
3. **"Gemaakt door"**: het kussen wordt niet in Borne gemaakt. De zin zegt "door Bline uit Borne", niet "in Borne", dus hij klopt; wil je het voorzichtiger, dan wordt het "Van Bline uit Borne".
4. Achternaam op Over Bline: ja of nee.
5. Schrijfwijze telefoon in de winkelinstellingen (staat als 31638662833), zie punt 2.
6. Overige punten uit sessie 4 tot en met 8 blijven open (Judge.me-productgroep, echte telefoontest, gewicht losse hoes).

## 5 oktober 2026, sessie 10: geen persoonsnaam op de site

Opdracht van Joost (05-10, via de hoofdsessie): geen naam noemen op de site. Toegang zoals sessie 9 (vaste winkelnaam, client credentials met `BLINE_SHOPIFY_CLIENT_ID` en `BLINE_SHOPIFY_CLIENT_SECRET`, alleen namen gecontroleerd, geen SHOPIFY_*- of BOL_*-variabelen). Alleen tekst aangeraakt; beelden horen bij sessie 12. Vooraf een lokale kopie van alles (map `backup_voor_s10`).

**Gezocht** op "Joost" en "Kuiphuis" in: pagina's (met SEO-metafields), beleid, blogs en artikelen, producten (beschrijving, SEO, metafields, alt-teksten, varianten), collecties, menu's, winkel-metafields, metaobjecten, bestanden (alt en naam), doorverwijzingen, kortingen, alle themabestanden van Dawn en Horizon (dus ook `config/settings_data.json`, templates, secties en `locales/nl.json`) en de wachtwoordpagina. Enige taal is nl.

**Gevonden en aangepast**
- Pagina Over Bline: "Bline is een klein bedrijf uit Borne, in Overijssel. Achter het merk staat Joost." wordt "Bline is een klein Nederlands merk uit Borne, in Overijssel." Rest van de tekst ongewijzigd.
- Sectie "Bline foto" op Over Bline staat uit (`templates/page.over-bline.json`, `"disabled": true`). Er was geen beeld gekozen. Het blok "Gemaakt door Bline uit Borne" op de productpagina's blijft, zonder naam en zonder foto.
- Repo: `reports/bijlagen/Bline shop teksten.md` gelijkgetrokken. De Collabs-tekst bevatte de naam alleen in interne notities, niet in de tekst voor Collabs.

**Controle:** alles opnieuw opgehaald en doorzocht: 0 treffers. Alleen `templates/page.over-bline.json` is in het thema veranderd; `pageUpdate` en `themeFilesUpsert` zonder fouten.

**Niet gedaan, bewust:** wachtwoord blijft aan; geen prijzen, mails, betaalinstellingen, apps of beelden.

**Vervalt uit sessie 9, Wacht op Joost:** punt 1 (foto) en punt 4 (achternaam).
