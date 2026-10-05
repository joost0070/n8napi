# Bline blogs en GEO-content: logboek

Sessie 5 oktober 2026. Doel: zes blogartikelen uit hoofdstuk 4 van het groeiplan, een vergelijkingspagina en extra vragen klaarzetten in Shopify, als concept. Volledige teksten in `reports/bijlagen/Bline blogteksten.md`.

## Toegang

- Sleutel via client credentials met `BLINE_SHOPIFY_CLIENT_ID` en `BLINE_SHOPIFY_CLIENT_SECRET` (alleen de namen gecontroleerd, waarden niet getoond). Winkel opgegeven in de opdracht, niet de waarde uit `BLINE_SHOPIFY_STORE`.
- Geen `SHOPIFY_*`- of `BOL_*`-variabelen gebruikt.
- Admin GraphQL, versie 2026-10. De sleutel stond alleen in het geheugen van het script.

## Gelezen vooraf

Groeiplan (hoofdstuk 4 en 6), taalregels in `look_and_feel_env_stores.md`, schrijfstijlgids (hoofdstuk 7 van `webshop_themas_en_schrijfstijl.md`), feiten uit hoofdstuk 3a van de masterprompt en `reports/bijlagen/Bline shop teksten.md`.

## Wat er nu staat

### Blog

- "Nieuws" (`nieuws`) heet nu **"Blog"** met handle **`blog`**. Shopify heeft zelf een doorverwijzing `/blogs/nieuws` naar `/blogs/blog` gemaakt.
- Gecontroleerd vooraf: geen menu en geen themasjabloon verwijst naar de blog of naar `nieuws`. Het hernoemen vroeg dus geen thema-aanpassing. Reacties blijven uit.

### Zes artikelen (alle zes concept, niet gepubliceerd)

| # | Titel | Handle | Woorden | Uitgelichte afbeelding |
|---|---|---|---|---|
| 1 | Leeskussen kopen: waar let je op? | leeskussen-kopen-waar-let-je-op | 734 | beige-03 |
| 2 | Leeskussen of extra kussens: wat werkt beter? | leeskussen-of-extra-kussens | 643 | blauw-02 |
| 3 | Zo was je de hoes van een leeskussen (en het traagschuim niet) | hoes-leeskussen-wassen | 640 | wit-06 |
| 4 | Welk formaat leeskussen past op jouw bed? | formaat-leeskussen-bed | 652 | grijs-01 |
| 5 | Cadeau voor iemand die veel leest: 7 ideeën | cadeau-voor-iemand-die-veel-leest | 629 | wit-08 |
| 6 | Tv kijken of werken in bed zonder kussenberg | tv-kijken-of-werken-in-bed | 641 | grijs-05 |

Per artikel ingevuld: titel, samenvatting, SEO-titel en metabeschrijving (118 tot 138 tekens), uitgelichte afbeelding met alt-tekst, tags, auteur "Bline".

- **Opbouw voor GEO**: elk artikel begint met een antwoord van twee zinnen op de hoofdvraag en eindigt met "In het kort" (4 of 5 feiten).
- **Link**: precies één link per artikel, naar `/products/leeskussen`. Geen andere links (de vergelijkingspagina is nog niet gepubliceerd, dus daar linkt niets naartoe).
- **Beelden**: alleen bestaande productfoto's van het leeskussen. Shopify slaat een artikelbeeld als kopie op in de map `articles` van de CDN. Het is dezelfde foto, geen nieuw beeld.
- **Feiten**: maten, gewicht, vulling, hoes, wasvoorschrift, zijvak, kleuren, luchten, verzending en bedenktijd uit hoofdstuk 3a en de shopteksten. Geen prijzen, geen OEKO-TEX, geen garantie buiten de wettelijke.
- **Algemene kennis** (geen productfeit, wel in de tekst): standaard bedmaten en de rekensommen daarmee (artikel 4), de betekenis van TC (artikel 1), dat katoen in de droger kan krimpen en traagschuim veel water opneemt (artikel 3), en de minimale bedenktijd van 14 dagen in de EU (artikel 1).
- **Artikel 5** noemt andere productsoorten (boekenlegger, leesdagboek, cadeaukaart van een boekhandel, leeslampje met klem, bedtafeltje) zonder merken of prijzen. Bewust "cadeaukaart van een boekhandel" en niet "boekenbon": dat is een merknaam.
- Geen concurrenten genoemd.

### Pagina "Leeskussen of losse kussens"

- Handle `leeskussen-of-losse-kussens`, **niet gepubliceerd**, in geen enkel menu.
- Standaard paginasjabloon, dus geen thema-aanpassing. Tabel met 12 regels (aantal, opbouwen, vulling, stevigheid, vorm, vak, hoes, wassen, gewicht, slapen, ruimte, kleuren), daarna "Wanneer kies je wat" en één link naar `/products/leeskussen`.
- SEO-titel "Leeskussen of losse kussens: de verschillen | Bline", metabeschrijving 130 tekens.
- Let op: de tabel gebruikt de standaardopmaak van Dawn. Hoe die er op mobiel uitziet, kon ik niet zien (wachtwoord).

### Pagina Veelgestelde vragen: vijf nieuwe vragen

De elf bestaande vragen staan als uitklapblokken in het themasjabloon `page.veelgestelde-vragen.json`. Dat is een themabestand, en dat mocht ik in deze sessie niet aanraken. Daarom staan de nieuwe vragen in de **paginatekst**, onder de bestaande zin "Staat je vraag er niet bij?", met het kopje "Over het kussen en de hoes". Ze verschijnen boven de uitklapblokken. Bestaande vragen en antwoorden zijn niet veranderd.

1. Kan het traagschuim in de wasmachine? Nee. Alleen de hoes gaat in de was, op 30 °C. Het kussen zelf laat je luchten.
2. Hoeveel leeskussens passen er op een tweepersoonsbed? Op een bed van 140 cm passen er twee naast elkaar. Elk kussen is 65 cm breed.
3. Hoe zwaar is het kussen? 3,9 kg, waarvan 3,8 kg traagschuim.
4. Heeft het kussen een vak voor mijn telefoon? Ja. Opzij in de hoes zit een vak voor je boek, bril of telefoon.
5. Wat betekent 400 TC? TC staat voor thread count: het aantal draden per vierkante inch stof. De hoes is van 100% katoen met 400 draden per vierkante inch.

De pagina was al gepubliceerd (achter het wachtwoord). Terugdraaien: de oude paginatekst was alleen `<p>Staat je vraag er niet bij? Mail naar <a href="mailto:mail@blinesleep.nl">mail@blinesleep.nl</a>.</p>`.

**Voorstel voor de themasessie**: zet deze vijf als `vraag_12` tot `vraag_16` in de uitklapblokken en haal ze daarna uit de paginatekst. Dan staat alles in één lijst.

## Stijlcontrole

Script over alle nieuwe teksten zoals ze in Shopify zijn opgeslagen: titels, samenvattingen, artikelteksten, SEO-titels, metabeschrijvingen, alt-teksten, tags, de vergelijkingspagina en de vragenpagina. Gezocht op:

- de schrapwoorden uit regel 4 van de gids (ontdek, ervaar, til, hoger niveau, stap in de wereld, ultiem, perfect, optimaal, naadloos, moeiteloos, tijdloos, essentieel, onmisbaar, toonbeeld, must-have, dé, "niet alleen ... maar ook", "of je nu", "Kortom", "Welkom bij");
- de AI-zinnen uit de taalregels ("Je kent het", handbagage, "van een mens", "klinkt gezellig", kussenfort, "eerlijk");
- gedachtestreepjes (lang en half, en een los streepje tussen spaties);
- "u" en "uw";
- gezondheidswoorden: pijn, klacht, ergonom, rug (ook als begin van een woord, zoals rugleuning), nek, houding, gezond, medisch;
- superlatieven (beste, meest, grootste, hoogste, ideaal), uitroeptekens en prijzen (€, euro).

| Tekst | Treffers |
|---|---|
| Artikel 1 tot en met 6 (alle velden) | 0 |
| Pagina Leeskussen of losse kussens | 0 |
| Pagina Veelgestelde vragen (hele paginatekst) | 0 |

Tijdens het schrijven gevonden en aangepast: "het grootste deel van de breedte" werd "bijna driekwart van de breedte". Het woord "meestal" gaf een valse treffer op "meest"; de zoekterm is daarna aangescherpt. Ook bewust vermeden: "rugleuning" (staat wel in de gids als goed woord, maar valt onder de zoekterm rug), "comfortabel", en een zijvak voor de afstandsbediening (3a noemt alleen boek, bril en telefoon).

## Gecontroleerd na afloop

- Alle zes artikelen: `isPublished` false, geen publicatiedatum.
- Vergelijkingspagina: `isPublished` false.
- Wachtwoord staat aan: `/blogs/blog` stuurt door naar `/password`.
- Geen themabestanden gewijzigd (alleen gelezen: het artikel-, blog-, pagina- en vragensjabloon, om te zien wat er getoond wordt).

## Niet gedaan, bewust

- Niets gepubliceerd. Geen prijzen, geen mails, geen apps, geen nieuwe beelden, geen themabestanden, geen menu-aanpassing.
- Het shoplogboek is niet aangepast.

## Wat Joost moet goedkeuren om te publiceren

1. **De zes artikelen lezen**, in Online Store > Blogberichten. Vooral de algemene tips die geen productfeit zijn (zie "Algemene kennis" hierboven) en de rekensommen in artikel 4.
2. **Twee zinnen die een belofte doen**: "Is er iets op het kussen zelf gekomen? Mail ons dan even" (artikel 3) en de uitleg over de bedenktijd bij een cadeau (artikel 5, gelijk aan het retourbeleid).
3. **De vijf nieuwe vragen** op de vragenpagina (staan al zichtbaar achter het wachtwoord), en of ze in de uitklapblokken moeten (themasessie).
4. **De vergelijkingspagina** lezen en zeggen of hij gepubliceerd mag worden, en of er vanuit artikel 2 naartoe gelinkt mag worden.
5. **Volgorde van publiceren**: voorstel uit het groeiplan is alle zes klaar, daarna één per twee weken. Publiceren pas als de winkel live is, anders staan ze achter het wachtwoord.
6. Optioneel: de blog in het menu of de voettekst zetten (nu nergens gelinkt).

## Aanvulling 5 oktober 2026 (shopsessie 7)

- Alle zes artikelen en de pagina "Leeskussen of losse kussens" zijn **gepubliceerd** (akkoord Joost 05-10). Het winkelwachtwoord staat nog aan, dus niemand buiten de admin ziet ze (gecontroleerd: `/blogs/blog` en de vergelijkingspagina sturen door naar `/password`).
- Artikel 2 linkt nu ook naar de vergelijkingspagina, met één zin onder de tabel. Het artikel heeft daarmee twee links: product en vergelijkingspagina.
- "Blog" staat in het voettekstmenu Klantenservice.
- De vijf nieuwe vragen staan nu in de uitklapblokken (vraag 12 tot 16) en zijn uit de paginatekst gehaald.
