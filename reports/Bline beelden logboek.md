# Bline beelden logboek

## 5 oktober 2026, sessie 9b: beelden van Joost verwerkt

Opdracht van Joost (05-10, via de hoofdsessie): "Alles staat in shopify van bestanden pas natuurlijk aan waar nodig. logische naam, utm etc.." en eerder: "alleen de goedgekeurde afbeeldingen gebruiken de anderen zitten fouten in!". Gelezen vooraf: beeld- en vertrouwensplan (hoofdstuk 1 en 3), funnel- en advertentieplan (hoofdstuk 9, naamafspraak), shoplogboek sessie 8 en 9, `beelden_higgsfield/OVERZICHT.md`.

Toegang: de vaste winkelnaam die Joost doorgaf (niet de waarde in `BLINE_SHOPIFY_STORE`), sleutel via client credentials met `BLINE_SHOPIFY_CLIENT_ID` en `BLINE_SHOPIFY_CLIENT_SECRET`. Alleen de namen gecontroleerd. Geen SHOPIFY_*- of BOL_*-variabelen gebruikt. Admin GraphQL, versie 2026-10.

Wachten op sessie 9: bij de eerste pull stond het kopje "sessie 9" al in het shoplogboek, dus stap 4 kon direct na stap 3.

### 1. Inventaris

Shopify Files bevat 150 bestanden. De opbouwsessies uploadden er 44 (05-10, 10:05 tot 10:08: 31 kussenbeelden, maattekening, 10 hoesbeelden, logo, wit logo, icoon). Alle 106 bestanden van 16:46 tot 16:48 zijn van Joost: 105 beelden en 1 video.

- 28 daarvan zijn dubbel geüpload (zelfde inhoud, Shopify zette er een code achter, bijvoorbeeld `2_0d10094c-....png` naast `2.png`, en `DSC01348.jpg` naast `DSC01348_1.jpg`). Over: **78 unieke bestanden** (77 beelden, 1 video).
- Contactblad met alle 106 en de oorspronkelijke bestandsnaam: `mockups/blinesleep/beelden_joost/overzicht.jpg`.
- Elk uniek beeld zelf bekeken (verkleind tot 600 px, twijfelgevallen op 1000 px), de video per 3 seconden.

Herkomst, voor zover te zien:
- **Echte fotoshoot** (wit kussen, `DSC01320_1`, `DSC01331`, `DSC01348_1`, `DSC01452`, 6000 x 4000) en de **video** (25 s, 1080 x 1080, wit kussen: lezen, hoes, label, zijvak met telefoon).
- **Ingekleurde versies van de shoot** (`1.png` tot `27.png`, 1361 x 1361): dezelfde vrouw in alle vijf kleuren, plus de losse hoezen als gedrapeerde doek met label.
- **bol-set** (`*_Anthracite`, `*_Gray/Grey`, `*_sand`, `*_Black`): bij bol heet blauw "Anthracite" en beige "sand". Beelden met tekst (hoofdbeeld, kenmerken, "Berg je boek eenvoudig op!", "Voorzien van rits") en kleine versies (500 px) van de ingekleurde beelden.
- **Gemini en ChatGPT** (`Gemini_Generated_Image_*`, `ChatGPT_Image_25_sep_2025_*`, `unnamed*`, `1.jpg`).

### 2. Indeling en kwaliteit

Kleur vergeleken met de bestaande kussenbeelden en de kleurcodes uit sessie 8. Blauw is bij Joost en bol een leiblauw (de oude bol-beelden zijn donkerder); beide staan op bol, dus beide goedgekeurd. Zwart is op een deel van de beelden antraciet (`9.png`, `11.png`, bol "Black"); dat past bij de kleurcode #2B2B2D en is niet afgekeurd. Waar hetzelfde beeld in zwart en antraciet bestond, is het zwartste gekozen (`7.png`).

Status: **goedgekeurd** (gebruikt), **reserve** (goed, niet nodig of bijna gelijk aan een gekozen beeld), **niet gebruikt** (geen fout, maar tekst in beeld, te klein of ander product), **afgekeurd** (zichtbare fout).

| Nr | Was | Nu | Product | Kleur | Soort | Pixels | Status | Waarom |
|---|---|---|---|---|---|---|---|---|
| 01 | bline.png | bline-merk-logo-01-niet.png | merk | - | logo | 500 x 250 | niet gebruikt | oud logo, 500 x 250 px; logo staat al als bline-logo.png |
| 02 | nieuw_logo_bline.jpg | bline-merk-logo-02-afgekeurd.jpg | merk | - | logo | 1024 x 1024 | **afgekeurd** | tekst onder het logo is "BLNE": de i ontbreekt |
| 03 | photoshoot_bijgesneden.png | bline-leeskussen-wit-gebruik-08-niet.png | leeskussen | wit | gebruik | 600 x 300 | niet gebruikt | uitsnede van DSC01320, maar 600 x 300 px: te klein |
| 04 | video leeskussen.mp4 | (naam kan niet wijzigen) | leeskussen | wit | video | 1080 x 1080 | goedgekeurd, gebruikt | echte video (25 s, 1080 x 1080): lezen, hoes, label, zijvak met telefoon |
| 05 | 2.png | bline-hoes-blauw-packshot-01.png | hoes | blauw | packshot | 1361 x 1361 | goedgekeurd, gebruikt | losse hoes, gedrapeerd, met label, lichte achtergrond |
| 06 | unnamed_1.png | bline-leeskussen-wit-gebruik-09-afgekeurd.png | leeskussen | wit | gebruik | 1024 x 683 | **afgekeurd** | watermerk (Gemini-ster) rechtsonder |
| 07 | 4.png | bline-leeskussen-blauw-gebruik-03.png | leeskussen | blauw | gebruik | 1361 x 1361 | goedgekeurd, gebruikt | vrouw met laptop |
| 08 | 6.png | bline-hoes-wit-packshot-01.png | hoes | wit | packshot | 1361 x 1361 | goedgekeurd, gebruikt | losse hoes, gedrapeerd, met label |
| 09 | Gemini_Generated_Image_j66vq3j66vq3j66v.png | bline-leeskussen-wit-gebruik-10-afgekeurd.png | leeskussen | wit | gebruik | 1248 x 832 | **afgekeurd** | watermerk (Gemini-ster) rechtsonder |
| 10 | 8.png | bline-hoes-zwart-packshot-01.png | hoes | zwart | packshot | 1361 x 1361 | goedgekeurd, gebruikt | losse hoes, gedrapeerd, met label |
| 11 | 20.png | bline-leeskussen-grijs-gebruik-03.png | leeskussen | grijs | gebruik | 1361 x 1361 | goedgekeurd, gebruikt | vrouw met laptop |
| 12 | 12.png | bline-hoes-beige-packshot-01.png | hoes | beige | packshot | 1361 x 1361 | goedgekeurd, gebruikt | losse hoes, gedrapeerd, met label |
| 13 | 14.png | bline-leeskussen-beige-gebruik-01.png | leeskussen | beige | gebruik | 1361 x 1361 | goedgekeurd, gebruikt | vrouw leest, telefoon in het zijvak |
| 14 | 9.png | bline-leeskussen-zwart-gebruik-03.png | leeskussen | zwart | gebruik | 1361 x 1361 | goedgekeurd, reserve | zelfde beeld als 7.png, maar antraciet; 7.png gekozen |
| 15 | 18.png | bline-leeskussen-grijs-gebruik-01.png | leeskussen | grijs | gebruik | 1361 x 1361 | goedgekeurd, gebruikt | vrouw leest, telefoon in het zijvak |
| 16 | 19.png | bline-leeskussen-grijs-gebruik-07-afgekeurd.png | leeskussen | grijs | gebruik | 1361 x 1361 | **afgekeurd** | zijvak is een plat grijs blok, harde rand langs het haar (inkleurfout) |
| 17 | 10.png | bline-leeskussen-zwart-gebruik-06-afgekeurd.png | leeskussen | zwart | gebruik | 1361 x 1361 | **afgekeurd** | zijvak is een plat blok, rafelige rand langs haar en kussen (inkleurfout) |
| 18 | 15.png | bline-leeskussen-beige-gebruik-08-afgekeurd.png | leeskussen | beige | gebruik | 1361 x 1361 | **afgekeurd** | zijvak is een plat blok, harde rand langs het haar (inkleurfout) |
| 19 | 3.png | bline-leeskussen-blauw-gebruik-01.png | leeskussen | blauw | gebruik | 1361 x 1361 | goedgekeurd, gebruikt | vrouw leest, telefoon in het zijvak |
| 20 | 17.png | bline-hoes-grijs-packshot-01.png | hoes | grijs | packshot | 1361 x 1361 | goedgekeurd, gebruikt | losse hoes, gedrapeerd, met label |
| 21 | 21.png | bline-leeskussen-grijs-gebruik-02.png | leeskussen | grijs | gebruik | 1361 x 1361 | goedgekeurd, gebruikt | vrouw leunt tegen het kussen |
| 22 | 16.png | bline-leeskussen-beige-gebruik-02.png | leeskussen | beige | gebruik | 1361 x 1361 | goedgekeurd, gebruikt | vrouw leunt tegen het kussen |
| 23 | 11.png | bline-leeskussen-zwart-gebruik-02.png | leeskussen | zwart | gebruik | 1361 x 1361 | goedgekeurd, gebruikt | vrouw leunt tegen het kussen |
| 24 | 5.png | bline-leeskussen-blauw-gebruik-02.png | leeskussen | blauw | gebruik | 1361 x 1361 | goedgekeurd, gebruikt | vrouw leunt tegen het kussen |
| 25 | 7.png | bline-leeskussen-zwart-gebruik-01.png | leeskussen | zwart | gebruik | 1361 x 1361 | goedgekeurd, gebruikt | vrouw leest, telefoon in het zijvak |
| 26 | 25.png | bline-leeskussen-wit-gebruik-11-afgekeurd.png | leeskussen | wit | gebruik | 1361 x 1361 | **afgekeurd** | vorm wijkt af: geen zijvak en geen label, lijkt een gewoon kussen |
| 27 | 1.png | bline-leeskussen-grijs-gebruik-08-afgekeurd.png | leeskussen | grijs | gebruik | 1361 x 1361 | **afgekeurd** | watermerk (Gemini-ster) en gemeleerde stof die niet bij de katoenen hoes past |
| 28 | 26.png | bline-leeskussen-wit-packshot-02.png | leeskussen | wit | packshot | 1361 x 1361 | goedgekeurd, reserve | bewerkte versie van DSC01452; de echte foto gekozen |
| 29 | 22.png | bline-leeskussen-wit-gebruik-04.png | leeskussen | wit | gebruik | 1361 x 1361 | goedgekeurd, gebruikt | vrouw met laptop, stapel hoezen in vijf kleuren |
| 30 | 27.png | bline-leeskussen-wit-gebruik-05.png | leeskussen | wit | gebruik | 1361 x 1361 | goedgekeurd, reserve | goed, maar genoeg witte gebruiksbeelden |
| 31 | 23.png | bline-leeskussen-wit-gebruik-06.png | leeskussen | wit | gebruik | 1361 x 1361 | goedgekeurd, reserve | goed, maar genoeg witte gebruiksbeelden |
| 32 | 13.png | bline-leeskussen-beige-gebruik-04.png | leeskussen | beige | gebruik | 1361 x 1361 | goedgekeurd, reserve | bijna gelijk aan 16.png |
| 33 | 24.png | bline-leeskussen-wit-gebruik-07.png | leeskussen | wit | gebruik | 1361 x 1361 | goedgekeurd, reserve | goed, maar genoeg witte gebruiksbeelden |
| 34 | Bline_leeskussen_rode_gloed_test.png | bline-leeskussen-wit-packshot-03-niet.png | leeskussen | wit | packshot | 3000 x 3000 | niet gebruikt | tekst in beeld ("Bline leeskussen, Het ideale leeskussen") en rode vlek |
| 35 | DSC01320_1.jpg | bline-leeskussen-wit-gebruik-01.jpg | leeskussen | wit | gebruik | 6000 x 4000 | goedgekeurd, gebruikt | echte foto (6000 x 4000): vrouw met laptop; homepage |
| 36 | DSC01331.jpg | bline-leeskussen-wit-gebruik-03.jpg | leeskussen | wit | gebruik | 5590 x 3785 | goedgekeurd, gebruikt | echte foto: vrouw met laptop, telefoon in het zijvak |
| 37 | DSC01348_1.jpg | bline-leeskussen-wit-gebruik-02.jpg | leeskussen | wit | gebruik | 6000 x 4000 | goedgekeurd, gebruikt | echte foto: vrouw leest, telefoon in het zijvak |
| 38 | DSC01452.jpg | bline-leeskussen-wit-packshot-01.jpg | leeskussen | wit | packshot | 6000 x 4000 | goedgekeurd, gebruikt | echte foto: kussen op bed met open boek |
| 39 | Bline_bamboe_kussen.png | bline-overig-bamboekussen-01-niet.png | overig | - | overig | 3000 x 3000 | niet gebruikt | ander product (bamboe hoofdkussen), met tekst |
| 40 | 2_1____Anthracite.jpg | bline-leeskussen-blauw-packshot-01-niet.jpg | leeskussen | blauw | packshot | 1000 x 1000 | niet gebruikt | bol-hoofdbeeld met tekst en rondje |
| 41 | 4___Anthracite.jpg | bline-leeskussen-blauw-gebruik-05-niet.jpg | leeskussen | blauw | gebruik | 500 x 500 | niet gebruikt | bol-versie van 3.png, 500 px: te klein |
| 42 | 2___Anthracite.jpg | bline-leeskussen-blauw-gebruik-06-niet.jpg | leeskussen | blauw | gebruik | 500 x 500 | niet gebruikt | bol-versie van 4.png, 500 px: te klein |
| 43 | 1___Anthracite.jpg | bline-leeskussen-blauw-gebruik-07-niet.jpg | leeskussen | blauw | gebruik | 500 x 500 | niet gebruikt | bol-versie van 5.png, 500 px: te klein |
| 44 | 1_1___Anthracite.jpg | bline-leeskussen-blauw-packshot-02-niet.jpg | leeskussen | blauw | packshot | 1000 x 1000 | niet gebruikt | tekst in beeld (kenmerken) |
| 45 | 17___Anthracite.jpg | bline-leeskussen-blauw-overig-01-niet.jpg | leeskussen | blauw | overig | 3000 x 3000 | niet gebruikt | tekst in beeld ("Voorzien van rits"), rits niet te zien |
| 46 | Gemini_Generated_Image_a51bira51bira51b.png | bline-hoes-blauw-packshot-02-afgekeurd.png | hoes | blauw | packshot | 1408 x 736 | **afgekeurd** | watermerk (Gemini-ster) en logo-blokje, liggend |
| 47 | 16___Anthracite.jpg | bline-leeskussen-blauw-zijvak-01-niet.jpg | leeskussen | blauw | zijvak | 3000 x 3000 | niet gebruikt | tekst in beeld ("Berg je boek eenvoudig op!") |
| 48 | ca8c30b1-aa40-4bc3-87ec-3c3f4492fab1.png | bline-hoes-blauw-packshot-03-afgekeurd.png | hoes | blauw | packshot | 1536 x 1024 | **afgekeurd** | watermerk (Gemini-ster), donkere achtergrond |
| 49 | ChatGPT_Image_25_sep_2025_13_44_13.png | bline-leeskussen-blauw-gebruik-04.png | leeskussen | blauw | gebruik | 1536 x 1024 | goedgekeurd, gebruikt | vrouw leest (liggend formaat) |
| 50 | 2_1____Grey.jpg | bline-leeskussen-grijs-packshot-01-niet.jpg | leeskussen | grijs | packshot | 1000 x 1000 | niet gebruikt | bol-hoofdbeeld met tekst en rondje |
| 51 | 4___Gray.jpg | bline-leeskussen-grijs-gebruik-04-niet.jpg | leeskussen | grijs | gebruik | 500 x 500 | niet gebruikt | bol-versie van 18.png, 500 px: te klein |
| 52 | 1.jpg | bline-leeskussen-grijs-gebruik-09-afgekeurd.jpg | leeskussen | grijs | gebruik | 1024 x 1024 | **afgekeurd** | watermerk (Gemini-ster) en gemeleerde stof |
| 53 | 2___Gray.jpg | bline-leeskussen-grijs-gebruik-05-niet.jpg | leeskussen | grijs | gebruik | 500 x 500 | niet gebruikt | bol-versie van 20.png, 500 px: te klein |
| 54 | 1__Grey.jpg | bline-leeskussen-grijs-gebruik-06-niet.jpg | leeskussen | grijs | gebruik | 500 x 500 | niet gebruikt | bol-versie van 21.png, 500 px: te klein |
| 55 | 3___Gray.jpg | bline-leeskussen-grijs-gebruik-10-afgekeurd.jpg | leeskussen | grijs | gebruik | 500 x 500 | **afgekeurd** | zelfde inkleurfout als 19.png (zijvak als blok), 500 px |
| 56 | unnamed.png | bline-hoes-grijs-packshot-02-afgekeurd.png | hoes | grijs | packshot | 1024 x 535 | **afgekeurd** | watermerk (Gemini-ster) en logo-blokje, liggend |
| 57 | 16___Gray.jpg | bline-leeskussen-grijs-zijvak-01-niet.jpg | leeskussen | grijs | zijvak | 3000 x 3000 | niet gebruikt | tekst in beeld ("Berg je boek eenvoudig op!") |
| 58 | 17___Gray.jpg | bline-leeskussen-grijs-overig-01-niet.jpg | leeskussen | grijs | overig | 3000 x 3000 | niet gebruikt | tekst in beeld ("Voorzien van rits") |
| 59 | 1_sand.jpg | bline-leeskussen-beige-gebruik-06-niet.jpg | leeskussen | beige | gebruik | 500 x 500 | niet gebruikt | bol-versie van 13.png, 500 px: te klein |
| 60 | 2_1____sand.jpg | bline-leeskussen-beige-packshot-01-niet.jpg | leeskussen | beige | packshot | 1000 x 1000 | niet gebruikt | bol-hoofdbeeld met tekst en rondje |
| 61 | 3___sand.jpg | bline-leeskussen-beige-gebruik-09-afgekeurd.jpg | leeskussen | beige | gebruik | 500 x 500 | **afgekeurd** | zelfde inkleurfout als 15.png (zijvak als blok), 500 px |
| 62 | 1_1____sand.jpg | bline-leeskussen-beige-packshot-02-niet.jpg | leeskussen | beige | packshot | 1000 x 1000 | niet gebruikt | tekst in beeld (kenmerken) |
| 63 | 4___sand.jpg | bline-leeskussen-beige-gebruik-07-niet.jpg | leeskussen | beige | gebruik | 500 x 500 | niet gebruikt | bol-versie van 14.png, 500 px: te klein |
| 64 | 16___sand.jpg | bline-leeskussen-beige-zijvak-01-niet.jpg | leeskussen | beige | zijvak | 3000 x 3000 | niet gebruikt | tekst in beeld ("Berg je boek eenvoudig op!") |
| 65 | 17___sand.jpg | bline-leeskussen-beige-overig-01-niet.jpg | leeskussen | beige | overig | 3000 x 3000 | niet gebruikt | tekst in beeld ("Voorzien van rits") |
| 66 | Gemini_Generated_Image_39yni539yni539yn.png | bline-hoes-beige-packshot-02-afgekeurd.png | hoes | beige | packshot | 1408 x 736 | **afgekeurd** | watermerk (Gemini-ster) en logo-blokje, liggend |
| 67 | ChatGPT_Image_25_sep_2025_13_50_47.png | bline-leeskussen-beige-gebruik-03.png | leeskussen | beige | gebruik | 1536 x 1024 | goedgekeurd, gebruikt | vrouw met laptop (liggend formaat) |
| 68 | ChatGPT_Image_25_sep_2025_14_23_19.png | bline-leeskussen-beige-gebruik-05.png | leeskussen | beige | gebruik | 1536 x 1024 | goedgekeurd, reserve | zelfde houding als 16.png |
| 69 | Gemini_Generated_Image_34ghkw34ghkw34gh.png | bline-hoes-wit-packshot-02-afgekeurd.png | hoes | wit | packshot | 1408 x 736 | **afgekeurd** | watermerk (Gemini-ster) en logo-blokje, liggend |
| 70 | 3___Black.jpg | bline-leeskussen-zwart-gebruik-07-afgekeurd.jpg | leeskussen | zwart | gebruik | 500 x 500 | **afgekeurd** | zelfde inkleurfout als 10.png (zijvak als blok), 500 px |
| 71 | 1_5e520a5d-2114-4292-bd27-c80cc3396432.jpg | bline-leeskussen-zwart-gebruik-08-afgekeurd.jpg | leeskussen | zwart | gebruik | 1024 x 1024 | **afgekeurd** | watermerk (Gemini-ster) rechtsonder |
| 72 | 1_1____Black.jpg | bline-leeskussen-zwart-packshot-01-niet.jpg | leeskussen | zwart | packshot | 1000 x 1000 | niet gebruikt | tekst in beeld (kenmerken) |
| 73 | 1___Black_1.jpg | bline-leeskussen-zwart-gebruik-04-niet.jpg | leeskussen | zwart | gebruik | 500 x 500 | niet gebruikt | bol-versie van 11.png, 500 px: te klein |
| 74 | 2_1____Black.jpg | bline-leeskussen-zwart-packshot-02-niet.jpg | leeskussen | zwart | packshot | 1000 x 1000 | niet gebruikt | bol-hoofdbeeld met tekst en rondje |
| 75 | 4___Black.jpg | bline-leeskussen-zwart-gebruik-05-niet.jpg | leeskussen | zwart | gebruik | 500 x 500 | niet gebruikt | bol-versie van 9.png, 500 px: te klein |
| 76 | 17___Black.jpg | bline-leeskussen-zwart-overig-01-niet.jpg | leeskussen | zwart | overig | 3000 x 3000 | niet gebruikt | tekst in beeld ("Voorzien van rits") |
| 77 | Gemini_Generated_Image_igoiszigoiszigoi.png | bline-hoes-zwart-packshot-02-afgekeurd.png | hoes | zwart | packshot | 1408 x 736 | **afgekeurd** | watermerk (Gemini-ster) en logo-blokje, liggend |
| 78 | 16___Black.jpg | bline-leeskussen-zwart-zijvak-01-niet.jpg | leeskussen | zwart | zijvak | 3000 x 3000 | niet gebruikt | tekst in beeld ("Berg je boek eenvoudig op!") |
De 28 dubbele uploads hebben hun oude naam gehouden en geen alt-tekst; ze hangen nergens aan. Ze mogen weg, maar alleen met akkoord van Joost (niets uit Files verwijderd).

**Afgekeurd (19), samengevat**
- Watermerk (de Gemini-ster rechtsonder): 11 beelden, waaronder alle zes liggende hoesbeelden met logo-blokje en de twee grijze beelden met gemeleerde stof.
- Inkleurfout: 6 beelden van de laptopscène in grijs, zwart en beige (`19.png`, `10.png`, `15.png` en de bol-versies): het zijvak met telefoon is een plat blok geworden en langs het haar loopt een harde of rafelige rand. De witte originelen (`27.png`, `DSC01331`) zijn wel goed.
- Vorm: `25.png`, wit kussen zonder zijvak en zonder label, lijkt een gewoon kussen.
- Tekst: het nieuwe logo-ontwerp heeft "BLNE" onder het beeldmerk (de i ontbreekt).

**Niet gebruikt (29)**: 17 met tekst in beeld (bol-hoofdbeelden en infographics, de "rode gloed"-test en het bamboekussen), 10 bol-versies van 500 px (de 1361 px-versie staat er al), het oude logo (500 x 250) en een uitsnede van 600 x 300.

### 3. Hernoemen en alt-teksten

- `fileUpdate` met `filename` werkt voor beelden: alle 77 hernoemd volgens `bline-<product>-<kleur>-<soort>-<nr>`. Niet gebruikte en afgekeurde beelden kregen `-niet` of `-afgekeurd` achter de naam, zodat ze later niet per ongeluk worden gekozen. Merk en overig: `bline-merk-logo-01-niet.png`, `bline-overig-bamboekussen-01-niet.png`.
- De extensie blijft wat het bestand is: Shopify verandert het formaat niet bij hernoemen, dus de pngs heten `.png` (afwijking van `.jpg` in de afspraak).
- **De video kan niet hernoemd worden** (Shopify: "Updating the filename is only supported on images and generic files"). Hij heet in Files "video leeskussen.mp4". Wel een alt-tekst.
- Alt-tekst per bestand in gewoon Nederlands met de kleur ("kleur Wit"), bijvoorbeeld "Vrouw leest een boek tegen het leeskussen Bline, kleur Beige, met haar telefoon in het zijvak" en "Losse hoes voor het leeskussen Bline, kleur Blauw, los neergezet met het Bline-label".
- Vooraf gecontroleerd dat het thema, de pagina's en de artikelen naar geen enkel bestand van Joost verwezen (het thema verwijst op naam, `shopify://shop_images/...`); hernoemen brak dus niets.

### 4. Toewijzen

Koppelen met `fileUpdate` (`referencesToAdd`, 23 bestanden, geen fouten), volgorde met `productReorderMedia`, daarna opnieuw opgehaald: alle 10 producten precies in de bedoelde volgorde. De varianten hebben geen eigen beeld, dus het eerste beeld is het hoofdbeeld en de collectiekaart.

Oude beelden: alle 41 bestaande beelden op de producten zijn door bol goedgekeurd (sessie 3: de 24 Higgsfield-originelen die op bol staan en de echte bol-foto's). Er hoefde dus niets af; ze staan nu achter de beelden van Joost. Er is geen packshot zonder tekst van Joost in beige, blauw, grijs en zwart; daar blijft het tekstloze bol-packshot (kussen op bed met boek) het hoofdbeeld.

| Product | Volgorde (B = bestaand bol-beeld) | Aantal |
|---|---|---|
| Leeskussen Wit | packshot-01 (echte foto), video, gebruik-01, 02, 03 (echte foto's), gebruik-04; B: wit-01, 02, 03, 04, 05, 08, wit-06 (rits en vulling), maattekening, wit-07 (label) | 15 |
| Leeskussen Beige | B: beige-01 (packshot); gebruik-01, 02, 03; B: beige-02, 03, 05, beige-04 (rits), maattekening | 9 |
| Leeskussen Blauw | B: blauw-01; gebruik-01, 02, 03, 04; B: blauw-02, 03, 05, 06, blauw-04 (rits), maattekening | 11 |
| Leeskussen Grijs | B: grijs-01; gebruik-01, 02, 03; B: grijs-02, 03, 05, 06, grijs-04 (rits), maattekening | 10 |
| Leeskussen Zwart | B: zwart-01; gebruik-01, 02; B: zwart-02, 03, 05, zwart-04 (rits), maattekening | 8 |
| Losse hoes (5 kleuren) | hoes-<kleur>-packshot-01 (gedrapeerde hoes), B: rits en vulling, B: kussen op bed | 3 per hoes |

- **Video** alleen bij Wit: het is het witte kussen, bij een andere kleur zou hij verwarren.
- **Hoezen**: de gedrapeerde hoes met label staat nu eerst, dus de hoezenkaarten zien er anders uit dan de kussenkaarten.
- **Homepage**: de grote foto is nu `bline-leeskussen-wit-gebruik-01.jpg` (echte foto, vrouw met laptop), in plaats van `bline-leeskussen-beige-02.jpg`. Alleen die ene instelling in `templates/index.json` aangepast (vooraf opgehaald, daarna gecontroleerd). De wachtwoordpagina houdt het oude beeld.
- **Over Bline**: er zit geen foto van Joost bij de bestanden (de vrouw op de foto's is een model). Niets gekozen; de sectie "Bline foto" blijft leeg.
- **Collectiekaarten**: packshot (het eerste beeld): Wit de echte foto, de andere kleuren het bol-packshot, hoezen de gedrapeerde hoes.

### 5. Testpagina-screenshots (werkwijze sessie 6 tot 9, benadering)

Thema (370 bestanden) en data opnieuw opgehaald, lokaal gerenderd met `render.js`, Chromium op 390 x 844 (2x) en 1366 x 800. In `mockups/blinesleep/screenshots/shop/ronde5/`: homepage, collectie Leeskussens, collectie Hoezen, Leeskussen Beige en extra Leeskussen Wit, elk eerste scherm en volledig, plus `metingen.json`. Script `testpagina/shoot5.py`; in `render.js` de maten van de nieuwe homepagefoto toegevoegd (6000 x 4000).

| Pagina | Gemeten |
|---|---|
| Homepage | grote foto `wit-gebruik-01`, mobiel 390 x 390 (kop en knop onderin, gezicht vrij), desktop 1366 x 720; kaarten Leeskussens met packshots, kaarten Hoezen met de gedrapeerde hoezen |
| Collectie Leeskussens | 5 packshots, volgorde Beige, Wit, Grijs, Blauw, Zwart |
| Collectie Hoezen | 5 gedrapeerde hoezen, duidelijk anders dan de kussens |
| Leeskussen Beige | teller 1/9, packshot eerst, dan de drie beelden van Joost |
| Leeskussen Wit | teller 1/14 op de testpagina: de renderer toont alleen beelden, de video (positie 2) ontbreekt daar. In de winkel zijn het 15 media |

Beperkingen als eerder: Judge.me nagebootst, betaaliconen als plaatsvervangers, winkelwagen niet echt gevuld, en nu ook: geen video op de testpagina.

### Niet gedaan, bewust

Wachtwoord blijft aan, geen prijzen, geen mails, geen betaalinstellingen, geen apps, geen nieuwe beelden gegenereerd, geen niet-goedgekeurde Higgsfield-beelden, niets uit Files verwijderd. Producttekst en UTM's niet aangeraakt (er waren geen links bij de beelden).

### Stand per kleur en soort (op de producten)

| Kleur | Packshot | Video | Gebruik (Joost + bol) | Zijvak | Rits | Maat | Label |
|---|---|---|---|---|---|---|---|
| Wit | 1 Joost (+ 1 bol) | 1 | 4 + 5 | 0 | 1 bol | 1 | 1 bol |
| Beige | 1 bol | 0 | 3 + 3 | 0 | 1 bol | 1 | 0 |
| Blauw | 1 bol | 0 | 4 + 4 | 0 | 1 bol | 1 | 0 |
| Grijs | 1 bol | 0 | 3 + 4 | 0 | 1 bol | 1 | 0 |
| Zwart | 1 bol | 0 | 2 + 3 | 0 | 1 bol | 1 | 0 |
| Hoes, elke kleur | 1 Joost | 0 | 0 (+ 1 bol kussenbeeld) | 0 | 1 bol | 0 | 0 |

Reserve (goed, nu niet op een product): wit 4 (`wit-packshot-02`, `wit-gebruik-05` tot `07`), beige 2, zwart 1.

### Wat nog ontbreekt

1. **Zijvak zonder tekst** (boek of telefoon in het vak, van dichtbij), alle kleuren. Alleen de bol-beelden met "Berg je boek eenvoudig op!" bestaan.
2. **Packshot zonder tekst van Joost** in beige, blauw, grijs en zwart (nu het bol-packshot).
3. **Label en naden** in beige, blauw, grijs en zwart (alleen wit heeft het label).
4. **Rits half open van dichtbij**, echt gefotografeerd (nu het bol-beeld met de vulling) en een rits-detail van de losse hoes.
5. **Maat op een gewoon tweepersoonsbed** (nu alleen de maattekening).
6. **Video** in een andere kleur dan wit.
7. **Foto van Joost** voor Over Bline en "Gemaakt door Bline uit Borne".
8. Beslissen over de 28 dubbele uploads en de afgekeurde bestanden in Files (verwijderen kan, met akkoord).

## Akkoord Joost 05-10: opruimen in Files

Joost gaf op 05-10 akkoord ("Ja") om de 28 dubbele uploads en de afgekeurde bestanden uit Shopify Files te verwijderen. Uitvoeren nadat sessie 14 (v2) klaar is, zodat er niets verdwijnt dat v2 gebruikt. Voor verwijderen per bestand controleren: niet gekoppeld aan een product, niet gebruikt in het thema (settings_data, templates), niet in pagina's of artikelen. Video en echte DSC-foto's nooit verwijderen.


## 5 oktober 2026, sessie 11: beelden bewerkt voor shop v2

Opdracht: `prompts/bline-shop-v2-merkwereld.md`, hoofdstuk "Beelden bewerken mag". Alleen goedgekeurde originelen uit Shopify Files (de 74 bestanden zonder `-niet` of `-afgekeurd`, plus de video). Lokaal bewerkt met Python (Pillow, numpy) en ffmpeg voor één stilstaand beeld uit de video. Geen generatieve AI, geen nieuwe scènes, geen afgekeurde of niet-gebruikte beelden.

### Werkwijze

- Bronnen eerst op volle grootte bekeken. De echte fotoshoot (`wit-gebruik-01`, `-02`, `-03`, `wit-packshot-01`, 6000 x 4000) is de basis voor hero, banners en macro's. De video (1080 x 1080) is per 0,4 s doorgelopen en op scherpte gemeten; het beeld op 22,0 s (zijvak, telefoon, bies en label) is gekozen.
- Bewerkingen: uitsnijden, verkleinen (Lanczos), licht verscherpen (onscherp masker), helderheid gelijktrekken binnen de set kleurtegels (alleen helderheid, factor tussen 0,94 en 1,06, gemeten op de muur; de stofkleur zelf is niet verschoven), naast elkaar zetten met 12 px wit, en voor de maatgids een eigen tekening op schaal. Op de cadeaubon staat een witte kaart met het logo en tekst.
- Eén poging is weggegooid: een 21:9-banner waarbij links een effen vlak in de muurkleur werd bijgeplakt. Op ware grootte zag de overgang er grijs en onecht uit. Vervangen door een zuivere uitsnede; de rustige ruimte voor de kop komt nu uit de opbouw van de pagina (tekst naast de foto), niet uit het beeld.
- Vier vulling-uitsneden in beige, blauw, grijs en zwart zijn gemaakt maar niet geüpload: ze waren bijna gelijk aan die in wit. Ook een tweede zijvak-uitsnede (haar aan de rand) is niet gebruikt.
- Elk beeld zelf gecontroleerd op contactbladen en op ware grootte: vorm van het kussen, kleur naast het origineel, naden en bies, label, randen van uitsneden, gezichten en handen niet afgesneden. Gecorrigeerd na controle: de maattekening (bed van 180 cm viel buiten beeld, decimaalpunt werd komma) en de cadeaubon (kussen was bovenaan afgesneden).
- Geüpload met `stagedUploadsCreate` en `fileCreate`, bestandsnaam volgens de afspraak (`bline-<soort>-<onderwerp>-<nr>.jpg`), alt-tekst in gewoon Nederlands. Alle 38 hebben status READY en behouden hun naam. Kopieën in `mockups/blinesleep/beelden_bewerkt/`, script in `mockups/blinesleep/testpagina/v2/edit.py`.

### Bewerkte beelden (38)

| Nr | Nieuw bestand | Bron | Bewerking | Pixels | Gebruikt op | Controle |
|---|---|---|---|---|---|---|
| 1 | `bline-banner-lezen-21x9.jpg` | bline-leeskussen-wit-gebruik-02.jpg (echte foto) | uitsnede 21:9 over de volle breedte, 3200 x 1371, licht verscherpt | 3200 x 1371 | paginakop Lezen in bed (desktop) | ok |
| 2 | `bline-banner-lezen-4x3.jpg` | bline-leeskussen-wit-gebruik-02.jpg (echte foto) | uitsnede 4:3 met kussen, zijvak, gezicht en boek, 2400 x 1800, licht verscherpt | 2400 x 1800 | hero homepage (desktop) | ok |
| 3 | `bline-banner-lezen-16x9.jpg` | bline-leeskussen-wit-gebruik-02.jpg (echte foto) | uitsnede 16:9, verkleind naar 2400 x 1350, licht verscherpt | 2400 x 1350 | banner collecties Bestsellers en Lezen in bed | ok |
| 4 | `bline-banner-lezen-4x5.jpg` | bline-leeskussen-wit-gebruik-02.jpg (echte foto) | uitsnede 4:5 rond gezicht, boek en kussen, 1600 x 2000, licht verscherpt | 1600 x 2000 | hero homepage en Lezen in bed (mobiel), megamenu, menutegel, ingang collectie | ok |
| 5 | `bline-banner-werken-16x9.jpg` | bline-leeskussen-wit-gebruik-01.jpg (echte foto) | uitsnede 16:9, 2400 x 1350, licht verscherpt | 2400 x 1350 | banner collectie Sets en bundels | ok |
| 6 | `bline-banner-werken-4x5.jpg` | bline-leeskussen-wit-gebruik-01.jpg (echte foto) | uitsnede 4:5, 1600 x 2000 | 1600 x 2000 | ingang Werken in bed (collectie), reserve voor de video | ok |
| 7 | `bline-sfeer-wit-4x5.jpg` | bline-leeskussen-wit-gebruik-03.jpg (echte foto) | uitsnede 4:5, 1600 x 2000 | 1600 x 2000 | reserve | ok |
| 8 | `bline-banner-kussen-16x9.jpg` | bline-leeskussen-wit-packshot-01.jpg (echte foto) | uitsnede 16:9, 2400 x 1350 | 2400 x 1350 | banner Cadeau, paginakop Materialen, Maatgids en Bline Sleep | ok |
| 9 | `bline-banner-kussen-4x5.jpg` | bline-leeskussen-wit-packshot-01.jpg (echte foto) | uitsnede 4:5, 1600 x 2000 | 1600 x 2000 | Over Bline (home), ingang Cadeau, menutegel Cadeau, mobiel Maatgids en Bline Sleep | ok |
| 10 | `bline-detail-zijvak-01.jpg` | bline-leeskussen-wit-gebruik-02.jpg (echte foto) | uitsnede van het zijvak met telefoon en het label, 1600 x 1422, verscherpt | 1600 x 1422 | detailtegel home, galerij Leeskussen Wit, blok Materialen op collectie | ok |
| 11 | `bline-detail-stof-01.jpg` | bline-leeskussen-wit-packshot-01.jpg (echte foto) | vierkante uitsnede van stof, bies en rits, 1600 x 1600, verscherpt | 1600 x 1600 | detailtegel home, Materialen, galerij Wit en hoes Wit, uitklapblok Materialen, megamenu, menutegel | ok |
| 12 | `bline-detail-label-01.jpg` | bline-leeskussen-wit-07.jpg (bol-foto) | licht verscherpt, verder gelijk | 1200 x 1200 | detailtegel home, galerij hoes Wit | ok |
| 13 | `bline-detail-zijvak-03.jpg` | video leeskussen.mp4 (echte video, beeld op 22,0 s) | stilstaand beeld uit de video, 1080 x 1080, verscherpt | 1080 x 1080 | Materialen (rits en zijvak) | ok |
| 14 | `bline-detail-vulling-wit.jpg` | bline-leeskussen-wit-06.jpg (bol-foto) | vierkante uitsnede van de open rits met traagschuim, 1200 x 1200 | 1200 x 1200 | materialentegel home, Materialen (vulling) | ok |
| 15 | `bline-tegel-wit-sfeer.jpg` | bline-leeskussen-wit-gebruik-02.jpg (echte foto) | uitsnede 4:5 in dezelfde kader voor alle vijf kleuren, 1088 x 1360, helderheid x0.99 gelijkgetrokken op de muur, licht verscherpt | 1088 x 1360 | kleurtegel homepage, Kleurengids, kleurcollectie, tweede beeld setkaart | ok |
| 16 | `bline-tegel-beige-sfeer.jpg` | bline-leeskussen-beige-gebruik-01.png | uitsnede 4:5 in dezelfde kader voor alle vijf kleuren, 1088 x 1360, helderheid x1.00 gelijkgetrokken op de muur, licht verscherpt | 1088 x 1360 | kleurtegel homepage, Kleurengids, kleurcollectie, tweede beeld setkaart | ok |
| 17 | `bline-tegel-blauw-sfeer.jpg` | bline-leeskussen-blauw-gebruik-01.png | uitsnede 4:5 in dezelfde kader voor alle vijf kleuren, 1088 x 1360, helderheid x1.00 gelijkgetrokken op de muur, licht verscherpt | 1088 x 1360 | kleurtegel homepage, Kleurengids, kleurcollectie, tweede beeld setkaart | ok |
| 18 | `bline-tegel-grijs-sfeer.jpg` | bline-leeskussen-grijs-gebruik-01.png | uitsnede 4:5 in dezelfde kader voor alle vijf kleuren, 1088 x 1360, helderheid x1.00 gelijkgetrokken op de muur, licht verscherpt | 1088 x 1360 | kleurtegel homepage, Kleurengids, kleurcollectie, tweede beeld setkaart | ok |
| 19 | `bline-tegel-zwart-sfeer.jpg` | bline-leeskussen-zwart-gebruik-01.png | uitsnede 4:5 in dezelfde kader voor alle vijf kleuren, 1088 x 1360, helderheid x1.00 gelijkgetrokken op de muur, licht verscherpt | 1088 x 1360 | kleurtegel homepage, Kleurengids, kleurcollectie, tweede beeld setkaart | ok |
| 20 | `bline-tegel-wit-packshot.jpg` | bline-leeskussen-wit-01.jpg (bol-beeld) | uitsnede 4:5 uit het midden, 1088 x 1360 | 1088 x 1360 | kleurtegel homepage (bij hover), setkaart | ok |
| 21 | `bline-tegel-beige-packshot.jpg` | bline-leeskussen-beige-01.jpg (bol-beeld) | uitsnede 4:5 uit het midden, 1088 x 1360 | 1088 x 1360 | kleurtegel homepage (bij hover), setkaart | ok |
| 22 | `bline-tegel-blauw-packshot.jpg` | bline-leeskussen-blauw-01.jpg (bol-beeld) | uitsnede 4:5 uit het midden, 1088 x 1360 | 1088 x 1360 | kleurtegel homepage (bij hover), setkaart | ok |
| 23 | `bline-tegel-grijs-packshot.jpg` | bline-leeskussen-grijs-01.jpg (bol-beeld) | uitsnede 4:5 uit het midden, 1088 x 1360 | 1088 x 1360 | kleurtegel homepage (bij hover), setkaart | ok |
| 24 | `bline-tegel-zwart-packshot.jpg` | bline-leeskussen-zwart-01.jpg (bol-beeld) | uitsnede 4:5 uit het midden, 1088 x 1360 | 1088 x 1360 | kleurtegel homepage (bij hover), setkaart | ok |
| 25 | `bline-kleuren-strip-01.jpg` | bline-leeskussen-wit-01.jpg, -beige-01, -blauw-01, -grijs-01, -zwart-01 (bol-beelden, zelfde scène) | vijf smalle uitsneden naast elkaar met 12 px wit ertussen, 3000 x 1481 | 3000 x 1481 | banner collectie Leeskussens, paginakop Kleurengids | ok |
| 26 | `bline-hoezen-strip-01.jpg` | bline-hoes-<kleur>-packshot-01.png (vijf kleuren) | vijf uitsneden uit het midden naast elkaar met 12 px wit ertussen, 3448 x 1361 | 3448 x 1361 | banner Hoezen en Hoezen en sets, menutegel | ok |
| 27 | `bline-banner-bank-16x9.jpg` | bline-leeskussen-wit-03.jpg (bol-beeld) | uitsnede 16:9, 2048 x 1152 | 2048 x 1152 | banner Ontspannen op de bank | ok |
| 28 | `bline-sfeer-bank-zwart-4x5.jpg` | bline-leeskussen-zwart-02.jpg (bol-beeld) | uitsnede 4:5, 1600 x 2000 | 1600 x 2000 | ingang en menutegel Ontspannen op de bank | ok |
| 29 | `bline-set-wit-hoes-beige.jpg` | bline-leeskussen-wit-01.jpg en bline-hoes-beige-packshot-01.png | twee helften naast elkaar op 2048 x 2048 met 12 px wit ertussen | 2048 x 2048 | hoofdbeeld van de set | ok |
| 30 | `bline-set-beige-hoes-wit.jpg` | bline-leeskussen-beige-01.jpg en bline-hoes-wit-packshot-01.png | twee helften naast elkaar op 2048 x 2048 met 12 px wit ertussen | 2048 x 2048 | hoofdbeeld van de set | ok |
| 31 | `bline-set-blauw-hoes-grijs.jpg` | bline-leeskussen-blauw-01.jpg en bline-hoes-grijs-packshot-01.png | twee helften naast elkaar op 2048 x 2048 met 12 px wit ertussen | 2048 x 2048 | hoofdbeeld van de set | ok |
| 32 | `bline-set-grijs-hoes-blauw.jpg` | bline-leeskussen-grijs-01.jpg en bline-hoes-blauw-packshot-01.png | twee helften naast elkaar op 2048 x 2048 met 12 px wit ertussen | 2048 x 2048 | hoofdbeeld van de set | ok |
| 33 | `bline-set-zwart-hoes-grijs.jpg` | bline-leeskussen-zwart-01.jpg en bline-hoes-grijs-packshot-01.png | twee helften naast elkaar op 2048 x 2048 met 12 px wit ertussen | 2048 x 2048 | hoofdbeeld van de set | ok |
| 34 | `bline-set-twee-wit.jpg` | bline-leeskussen-wit-01.jpg en bline-tegel-wit-sfeer.jpg | twee helften naast elkaar op 2048 x 2048 met 12 px wit ertussen | 2048 x 2048 | hoofdbeeld van de set | ok |
| 35 | `bline-set-twee-beige.jpg` | bline-leeskussen-beige-01.jpg en bline-tegel-beige-sfeer.jpg | twee helften naast elkaar op 2048 x 2048 met 12 px wit ertussen | 2048 x 2048 | hoofdbeeld van de set | ok |
| 36 | `bline-set-twee-zwart.jpg` | bline-leeskussen-zwart-01.jpg en bline-tegel-zwart-sfeer.jpg | twee helften naast elkaar op 2048 x 2048 met 12 px wit ertussen | 2048 x 2048 | hoofdbeeld van de set | ok |
| 37 | `bline-cadeaubon-01.jpg` | bline-leeskussen-wit-packshot-01.jpg (echte foto) en bline-logo.png | vierkante uitsnede over de volle hoogte, 2048 x 2048, met een witte kaart (logo, CADEAUBON en de bedragen) eroverheen | 2048 x 2048 | klaar voor de cadeaubon (nog niet in gebruik, zie Wacht op Joost) | ok |
| 38 | `bline-maatgids-bedden-01.jpg` | eigen tekening (geen foto), maten uit de productgegevens | bovenaanzicht van drie bedden (140, 160 en 180 x 200 cm) met het kussen van 65 x 45 cm op schaal, 2400 x 1500 | 2400 x 1260 | Maatgids, galerij van de vijf kussens | ok |

### Bestaande goedgekeurde beelden die nu ook op inhoudspagina's staan

Lookbook (homepage en Lezen in bed): `wit-gebruik-01` en `-03` (echte foto's), `wit-02`, `-03`, `-04`, `blauw-03`, `-05`, `-06`, `beige-02`, `-03`, `grijs-02`, `-03`, `-05`, `zwart-02`, `-03`, `-05` (bol-beelden). Materialen: `bline-hoes-beige-packshot-01.png`, `bline-leeskussen-blauw-04.jpg`. Kleurengids: `bline-leeskussen-wit-gebruik-04.png`. Maatgids: `bline-leeskussen-maattekening.jpg`. Homepage: de video `video leeskussen.mp4` (automatisch, zonder geluid, in een lus).

### Nieuw op de producten

| Product | Toegevoegd |
|---|---|
| Leeskussen Wit | `bline-detail-zijvak-01` en `bline-detail-stof-01` op plek 5 en 6 (na packshot, video en twee echte foto's), `bline-maatgids-bedden-01` na de maattekening |
| Leeskussen Beige, Blauw, Grijs, Zwart | `bline-maatgids-bedden-01` na de maattekening |
| Losse hoes Wit | `bline-detail-stof-01` en `bline-detail-label-01` op plek 2 en 3 |
| 8 sets (nieuw) | setcollage, sfeertegel van het kussen, packshot van de hoes of het kussen |

Niets uit Files verwijderd. De witte macro's staan alleen bij Wit; bij de andere kleuren zou een wit detail verwarren.

## 5 oktober 2026, sessie 12: Files opgeruimd en eigen bewerkingen uit de winkel

Akkoord Joost (05-10): "ruim de bestanden op". Werkwijze: alle bestanden opgehaald en op inhoud vergeleken (SHA-1). Per bestand gecontroleerd: niet aan een product gekoppeld, niet genoemd in het thema (alle bestanden), pagina's, artikelen of collecties.

- **Verwijderd (57):** 27 dubbele uploads (`1.png` tot `27.png` met code), `DSC01348.jpg` (identieke kopie van `bline-leeskussen-wit-gebruik-02.jpg`, die blijft), 19 afgekeurde beelden, en 10 kopieën met code (`bline-leeskussen-<kleur>-01_…`, `-04_…`, `wit-06_…`). Die laatste hingen aan de hoezen; de hoezen wijzen nu naar het basisbestand op dezelfde plek (beeld vrijwel identiek, gecontroleerd).
- **Blijft:** de video, alle echte DSC-foto's, alle goedgekeurde beelden, de `-niet`-bestanden (geen akkoord om die te verwijderen) en mijn eigen bewerkingen (banners, tegels, stroken, sets, details). Die laatste worden nergens meer in de winkel gebruikt (behalve de sets, die niet in de webwinkel staan) en kunnen weg zodra Joost dat wil.
- Files: van 188 naar 131 bestanden, geen dubbele en geen afgekeurde meer.

## 6 oktober 2026: eigen bewerkingen verwijderd

Akkoord Joost (06-10): "je eigen bewerkte beelden mogen ook weg". Verwijderd: 38 bestanden (banners, tegels, stroken, details, setcollages, cadeaubon, sfeer-uitsneden, maatgids-tekening). Vooraf: de enige thema-verwijzing (`snippets/bline-uitklap.liquid`, klein stofbeeld) weggehaald; de 8 sets (die de collages als beeld hadden) uit de webwinkel gehaald met doorverwijzing naar de productpagina; hoes Wit verloor zijn twee bewerkte details. De 13 collecties kregen een origineel beeld (Shopify houdt de oude bestandsnaam aan, de inhoud is vervangen; gecontroleerd op afmetingen). Files telt nu 93 bestanden: alleen originelen, de video, logo's en de `-niet`-bestanden.

## 09-10-2026: bijgekleurde gebruiksbeelden uit de galerijen

Op verzoek van Joost (stof te glad, geen bies, kussen lijkt opgeblazen, zelfde beeld in vijf kleuren) zijn `gebruik-01` en `gebruik-02` van beige, blauw, grijs en zwart (8 beelden) losgekoppeld van de productgalerijen. Ze staan nog in Files. Wit `gebruik-05` en `-06` en `wit-gebruik-02.jpg` blijven: echte stof, bies en zijvak zichtbaar (Joost akkoord). Op de pagina Materialen (blok "Rits en zijvak") is `beige-gebruik-01.png` vervangen door `beige-03.jpg`. Per kleur staan nu 5 echte foto's in de galerij, bij wit 9.
