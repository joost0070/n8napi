# Bline Meta-advertenties: statische set (stand 7 oktober 2026)

Deze set vervangt de afgekeurde set van 5 oktober volledig. Alles is statisch, er is geen video. Elke advertentie is er in 4:5 (feed) en 9:16 (Stories/Reels), plus één carrousel. De beelden staan in `uit/` en het overzicht in `overzicht_statisch.jpg`. Opnieuw maken: `python3 render.py ads.html` en `python3 render.py ads_v5.html`.

**Waar het op gebaseerd is:** echte, actieve advertenties van Cloudpillo, Emma, Auping, Beter Bed, Swiss Sense, Ten Cate, Walra en Sleeptight in de Meta Advertentiebibliotheek (bekeken op 7-10-2026), plus `research_notes/Bline advertenties/` (Meta-strategie, concurrentie en review-klachten).

| Wat werkt bij hen | Hoe we het gebruiken |
|---|---|
| Cloudpillo: "Koop deze toppers NIET!" (omgekeerde psychologie) | B1 "Koop dit leeskussen niet als je…" |
| Cloudpillo: "Kies 2, betaal 1" als nagebootst bestelscherm | B2 productkaart met kleurrondjes, prijs en knop |
| Emma: prijs groot in beeld, rij vertrouwenspictogrammen | B3 "Eén kussen. Blijft staan." met prijs en een rij van 4 pictogrammen |
| Beter Bed en Auping: donker vlak met één vraag naast een foto | B4 "Lezen in bed, zonder kussenstapel?" |
| Felle, eigen merkkleuren en een sticker (Cloudpillo, Emma) | Nacht, terracotta en salie; terracotta sticker alleen bij echte voordelen |
| Gaten in de markt (concurrentieonderzoek) | B6 "Koel katoen. Geen fluweel." en B7 "Geen armleuningen. Past op elk bed." |

**Regels die overal gelden:**
- Geen medische woorden, geen "beste", geen doorgestreepte prijzen en geen nepkorting.
- Prijs altijd van de kleur die in beeld is.
- De bol-score staat er alleen met het aantal reviews erbij.
- Knop bij elke advertentie: **Nu kopen**.
- UTM: `utm_source={{site_source_name}}&utm_medium=paid_social&utm_campaign={{campaign.name}}&utm_content={{ad.name}}`

## Campagne-opzet (alles op pauze tot Joost akkoord geeft)

| Niveau | Instelling |
|---|---|
| Campagne `bl_meta_sales_nlbe` | Advantage+ verkoopcampagne, doel Verkoop, €10 per dag (vooraf betaald saldo €150) |
| Advertentieset | Conversie-event **Aankoop** op Pixel 1, Nederland + Vlaanderen, 25+, taal Nederlands, Advantage+ doelgroep en plaatsingen (zonder Audience Network) |
| Advantage+ creatief | Alleen "aanpassen aan plaatsing" aan. Uit: tekstvarianten genereren, tekst in beelden herschrijven, achtergrond genereren, muziek |
| Golf 1 (start) | B1, B2, A02, B3, B6, A06 (carrousel) |
| Golf 2 (na 10-14 dagen) | B4, B7, B11, A03, A04, A05: vervangen wat na €8 onder 0,6% klikratio zit |
| Later | Catalogusadvertenties (Advantage+ catalogus) uit de Shopify-catalogus, zodra de catalogus van de nieuwe winkel synchroniseert |

Stopregels uit het funnelplan:
- **Advertentie vervangen:** na €8 uitgave met een klikratio onder 0,6%.
- **Advertentie pauzeren:** na €20 uitgave zonder winkelwagen.
- **Hele campagne:** €150 zonder aankoop is stoppen en de trechter nalopen.
- **Opschalen:** onder €25 per aankoop met 4 of meer aankopen is +20% budget.

---

## De advertenties

### B1 `bl_b1_niet`: "Koop dit leeskussen niet als je…"
Bestanden: `bline-meta-b1-niet-45.jpg`, `-916.jpg` · Landing: `https://www.blinesleep.nl/products/leeskussen-blauw`
- **Primaire tekst A:** Koop dit leeskussen niet als je het fijn vindt om elke avond je kussens opnieuw op te bouwen.
  Bline is één wigvormig kussen van 3,8 kg traagschuim. Het blijft staan als je leunt, je telefoon past in het vak aan de zijkant en de hoes gaat in de was. Probeer hem 30 dagen in je eigen bed.
- **Primaire tekst B:** Drie kussens achter je rug en na tien minuten lig je weer half? Dan is dit je kussen. Blauw leeskussen €79,99, gratis verzending in Nederland en België.
- **Kop:** 30 dagen proberen in je eigen bed · **Beschrijving:** Blauw, €79,99

### B2 `bl_b2_kleur`: "Welke kleur wordt het?" (productkaart)
Bestanden: `bline-meta-b2-kleur-45.jpg`, `-916.jpg` · Landing: `https://www.blinesleep.nl/products/leeskussen-blauw`
- **Primaire tekst A:** Wit, beige, blauw, grijs of zwart: welke past bij jouw bed?
  Elk Bline-kussen heeft 3,8 kg traagschuim, een vak voor je telefoon en een katoenen hoes met rits die in de was kan.
- **Primaire tekst B:** Zelfde kussen, vijf kleuren. Kies er één die bij je dekbed past, wij versturen hem binnen 1-2 werkdagen, gratis.
- **Kop:** Kies je kleur · **Beschrijving:** Blauw €79,99 · gratis verzending

### A02 `bl_a02_stapel`: "Drie kussens of één die blijft staan?"
Bestanden: `bline-meta-a02-stapel-45.jpg`, `-916.jpg` · Landing: `https://www.blinesleep.nl/products/leeskussen-blauw`
- **Primaire tekst A:** Drie kussens achter je rug en na tien minuten lig je weer half plat.
  Bline is één wigvormig kussen van 3,8 kg traagschuim. Het blijft staan als je leunt, heeft een vak voor je telefoon en een hoes die in de was kan.
- **Primaire tekst B:** Elke avond je kussens opbouwen, elke avond schuiven ze weer weg. Eén Bline leeskussen en je zit rechtop tot het laatste hoofdstuk.
- **Kop:** Eén kussen in plaats van drie · **Beschrijving:** Gratis verzending NL en BE

### B3 `bl_b3_prijs`: "Eén kussen. Blijft staan." (prijs en vertrouwen)
Bestanden: `bline-meta-b3-prijs-45.jpg`, `-916.jpg` · Landing: `https://www.blinesleep.nl/products/leeskussen-wit`
- **Primaire tekst A:** Eén kussen dat blijft staan als je ertegenaan leunt. Wit leeskussen €69,99, inclusief katoenen hoes die in de was kan.
  Gratis verzending in Nederland en België, binnen 1-2 werkdagen in huis, 30 dagen proberen.
- **Primaire tekst B:** Lezen, een serie of nog even mailen: met Bline zit je rechtop in bed zonder kussenstapel. Wit, €69,99.
- **Kop:** Wit leeskussen, €69,99 · **Beschrijving:** 30 dagen proberen

### B6 `bl_b6_katoen`: "Koel katoen. Geen fluweel."
Bestanden: `bline-meta-b6-katoen-45.jpg`, `-916.jpg` · Landing: `https://www.blinesleep.nl/products/leeskussen-grijs`
- **Primaire tekst A:** De meeste leeskussens hebben een fluwelen hoes. Bline niet: katoen van 400 TC, koel aan je rug en met een rits in een paar tellen eraf. Wassen op 30 °C en weer om het kussen.
- **Primaire tekst B:** Koel katoen in plaats van fluweel, en 3,8 kg traagschuim dat blijft staan. Grijs leeskussen €79,99, gratis verzending.
- **Kop:** Katoenen hoes, gewoon in de was · **Beschrijving:** Grijs, €79,99

### A06 `bl_a06_carrousel`: "Kies je kleur, kies je moment"
Bestanden: `bline-meta-a06-kaart1-beige.jpg` t/m `kaart6-kleuren.jpg` (1:1)
- **Primaire tekst:** Zelfde kussen, vijf kleuren. Welke past bij jouw bed? Elk Bline-kussen heeft 3,8 kg traagschuim, een vak voor je telefoon en een katoenen hoes met rits die in de was kan. Wit €69,99, de andere kleuren €79,99.
- **Kaarten:**

| Kaart | Kop | Beschrijving | Link |
|---|---|---|---|
| 1 | Beige | €79,99 | `/products/leeskussen-beige` |
| 2 | Blauw | €79,99 | `/products/leeskussen-blauw` |
| 3 | Grijs | €79,99 | `/products/leeskussen-grijs` |
| 4 | Zwart | €79,99 | `/products/leeskussen-zwart` |
| 5 | Wit | €69,99 | `/products/leeskussen-wit` |
| 6 | Vergelijk de kleuren | Gratis verzending | `/products/leeskussen-beige` |

### B4 `bl_b4_vraag`: "Lezen in bed, zonder kussenstapel?"
Bestanden: `bline-meta-b4-vraag-45.jpg`, `-916.jpg` · Landing: `https://www.blinesleep.nl/products/leeskussen-beige`
- **Primaire tekst A:** Lezen in bed zonder dat er steeds een kussen wegglijdt. Bline is één leeskussen van 3,8 kg traagschuim dat blijft staan, met een vak voor je telefoon of bril.
- **Primaire tekst B:** Je bed heeft geen rugleuning. Dit is er één. Beige leeskussen €79,99, gratis verzending in Nederland en België.
- **Kop:** Rechtop in bed, zonder kussenberg · **Beschrijving:** Beige, €79,99

### B7 `bl_b7_maat`: "Geen armleuningen. Past op elk bed."
Bestanden: `bline-meta-b7-maat-45.jpg`, `-916.jpg` · Landing: `https://www.blinesleep.nl/products/leeskussen-wit`
- **Primaire tekst A:** Geen armleuningen, dus je armen zijn vrij voor je boek en je houdt je bed. 65 cm breed, 50 cm hoog, 45 cm diep: twee passen naast elkaar op een bed vanaf 140 cm.
- **Primaire tekst B:** Twijfel je over de maat? 65 cm breed: ruim genoeg om tegen te leunen, smal genoeg om naast elkaar te lezen.
- **Kop:** 65 cm breed, past op elk bed · **Beschrijving:** Wit, €69,99

### B11 `bl_b11_hoes`: "Eén in de was, één om het kussen."
Bestanden: `bline-meta-b11-hoes-45.jpg`, `-916.jpg` · Landing: `https://www.blinesleep.nl/products/leeskussen-wit?hoes=1`
- **Primaire tekst A:** Eén hoes in de was, één om het kussen. Neem bij je leeskussen een tweede hoes en je krijgt €9,99 korting op die hoes. In alle vijf kleuren.
- **Primaire tekst B:** Je leeskussen altijd fris: een tweede katoenen hoes met €9,99 korting, bij elk Bline leeskussen.
- **Kop:** Tweede hoes €9,99 korting · **Beschrijving:** Bij een leeskussen

### A03 `bl_a03_uitleg`: "Een rugleuning voor je bed."
Bestanden: `bline-meta-a03-uitleg-45.jpg`, `-916.jpg` · Landing: `https://www.blinesleep.nl/products/leeskussen-beige`
- **Primaire tekst:** Je bed heeft geen rugleuning. Dit is er één. Wat je krijgt voor €79,99: 3,8 kg traagschuim in stukjes zodat hij blijft staan, een vak voor je telefoon, een katoenen hoes (400 TC) met rits, wasbaar op 30 °C. 65 x 50 x 45 cm.
- **Kop:** Wat zit erin, wat krijg je · **Beschrijving:** Beige, €79,99

### A04 `bl_a04_werken`: "thuiswerken vanuit bed, maar dan rechtop"
Bestanden: `bline-meta-a04-werken-45.jpg`, `-916.jpg` · Landing: `https://www.blinesleep.nl/products/leeskussen-wit`
- **Primaire tekst:** Laptop op schoot, rug tegen iets stevigs. Voor de avonden dat je nog even iets afmaakt in bed: Bline blijft staan, je telefoon zit in het vak en de hoes gaat in de was. Wit leeskussen €69,99.
- **Kop:** Rechtop in bed, zonder kussenberg · **Beschrijving:** Wit, €69,99

### A05 `bl_a05_bank`: "Niet alleen voor in bed."
Bestanden: `bline-meta-a05-bank-45.jpg`, `-916.jpg` · Landing: `https://www.blinesleep.nl/products/leeskussen-zwart`
- **Primaire tekst:** Niet alleen voor in bed: ook op de bank. Zet Bline tegen de leuning en je zit rechtop met je boek, zonder dat er kussens wegglijden. Zwart leeskussen €79,99.
- **Kop:** In bed en op de bank · **Beschrijving:** Zwart, €79,99

---

## Nog te beslissen of te checken (Joost)

1. **Bundel in Black Week:** het concurrentieonderzoek adviseert "kussen + tweede hoes voor €99,99" in plaats van een procentkorting. Nu is het €104,99 (€9,99 korting op de hoes). Een prijswijziging alleen met jouw akkoord.
2. **Kleur grijs:** controleer of het grijs op de sfeerfoto's overeenkomt met het echte kussen. De carrousel gebruikt daarom de foto met de man en de laptop.
3. **Sinterklaas en Kerst:** cadeau-advertenties maak ik zodra de uiterste besteldatum met ChannelDock is afgesproken.
