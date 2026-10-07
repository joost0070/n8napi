# Bline Meta testset v6 (7 oktober 2026)

Alle advertenties gebruiken de echte productfoto's (originelen uit `beelden_higgsfield/`, niet uitgesneden en niet verkleurd), 1080x1350 (4:5). Bron: `ads_v6.html`, beelden: `uit/v6/`, overzicht: `overzicht_v6.jpg`. Alles staat als concept; niets gaat live zonder akkoord van Joost.

## De 8 advertenties

| Code | Richting | Beeld | Kop in beeld | Landing |
|---|---|---|---|---|
| A1 | A product op kleur | blauw kussen met boek, terracotta vlak | Blijft staan. Ook na hoofdstuk 12. · €79,99 · gratis verzending · 30 dagen proberen | /products/leeskussen-blauw |
| A2 | A product op kleur | zwart kussen met boek, zandkleurig vlak | Rechtop lezen in bed. Zonder kussenstapel. · €79,99 · 5 kleuren | /products/leeskussen-zwart |
| B1 | B rustig premium | vrouw leest in bed, beige | Nog één hoofdstuk. | /products/leeskussen-beige |
| B2 | B rustig premium | vrouw leest op de bank, wit | Ook op de bank. | /products/leeskussen-wit |
| C1 | C bewijs | binnenkant met traagschuim | Daarom blijft hij staan. · 3,8 kg traagschuim in stukjes · katoenen hoes, wasbaar | /products/leeskussen-beige |
| C2 | C omgekeerd | man leest 's avonds, blauw | Niet kopen als je graag plat ligt. Wel als je elke avond leest, kijkt of scrolt. | /products/leeskussen-blauw |
| D1 | D native | chatbericht over foto, grijs | Wat is dat voor kussen achter je? / Leeskussen van Bline. Blijft echt staan, en mijn telefoon zit in het vakje | /products/leeskussen-grijs |
| D2 | D native | storytekst over foto, wit | eindelijk een kussen dat niet wegzakt | /products/leeskussen-wit |

## Teksten bij de advertentie

Kop (onder het beeld) en primaire tekst, kort en zonder uitroeptekens.

- **A1** · Kop: Leeskussen dat blijft staan · Tekst: Eén wigkussen in plaats van drie kussens die wegzakken. Vak voor je telefoon, hoes in de was, 30 dagen proberen.
- **A2** · Kop: Rechtop lezen, zonder stapel · Tekst: Bline houdt je rug recht terwijl je leest of kijkt. Vijf kleuren, gratis verzending in Nederland en België.
- **B1** · Kop: Bline leeskussen · Tekst: Voor wie elke avond nog één hoofdstuk leest.
- **B2** · Kop: Bline leeskussen · Tekst: In bed of op de bank: een kussen dat je rug steunt en blijft staan.
- **C1** · Kop: 3,8 kg traagschuim · Tekst: Gewone kussens zakken weg. Bline is gevuld met traagschuim in stukjes, zodat hij blijft staan als je leunt. De katoenen hoes gaat met een rits eraf en in de was.
- **C2** · Kop: Voor de avondlezer · Tekst: Lig je graag plat, dan heb je dit niet nodig. Lees, kijk of scrol je elke avond rechtop, dan wel. 30 dagen proberen.
- **D1** · Kop: Het kussen achter je · Tekst: Leeskussen met een vak voor je telefoon. Blijft staan, ook na een uur leunen.
- **D2** · Kop: Blijft staan · Tekst: Geen gefrommel met kussens meer. Eén leeskussen, in vijf kleuren.

Knop: **Nu kopen**. UTM volgens `reports/Bline meetplan.md`.

## Testplan

| Onderdeel | Keuze |
|---|---|
| Campagne | `bl_meta_test_nlbe`, doel Verkopen, geoptimaliseerd op Aankoop (Pixel 1) |
| Opbouw | 4 advertentiesets, één per richting (A, B, C, D), elk met hun 2 advertenties; budget per advertentieset zodat elke richting gelijk kansen krijgt |
| Doelgroep | Nederland en België, 30 tot 65+, breed (geen interesses), Advantage+ plaatsingen |
| Budget | €5 per dag per richting, 7 dagen = **€140** (past in het vooraf betaalde saldo van €150) |
| Pas aan na | 7 dagen, of eerder als een advertentie na 2.000 vertoningen onder 0,7% klikratio zit (die zetten we uit) |
| Meten | klikratio (link) en kosten per klik als eerste signaal; dan winkelwagen en aankoop. Winnaar = laagste kosten per winkelwagen of aankoop, niet alleen de meeste klikken |
| Daarna | de beste 1 of 2 richtingen houden, daarvan nieuwe varianten maken (andere kleur, andere kop), de rest uit |

Voorwaarde vooraf: de testprocedure uit het meetplan (Purchase komt binnen in Meta) is gedaan.
