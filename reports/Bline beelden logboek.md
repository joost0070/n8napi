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
