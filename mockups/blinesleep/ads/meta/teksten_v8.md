# Bline Meta testset v8 (7 oktober 2026)

Joost vond B1, B2 en C2 uit v7 goed; die blijven ongewijzigd. De overige 5 zijn vervangen door nieuwe advertenties in dezelfde stijl:
- een echte sfeerfoto die het hele beeld vult;
- één zin;
- een klein logo;
- geen prijsbalk, labels, chat of storytekst in het beeld.

Er zitten 8 verschillende taferelen in en alle 5 kleuren komen voor.

Bron: `ads_v8.html`, beelden: `uit/v8/`, overzicht: `overzicht_v8.jpg`. Schrijfregels en onderzoek: `teksten_v7.md`. Alles staat als concept; niets gaat live zonder akkoord van Joost.

## Twee stijlen

- **Rustig (B):** serifletter, één zin over het moment. B1 t/m B5.
- **Kwalificerend (C):** strakke letter, zegt voor wie het kussen is, met één ondersteunende regel. C2 t/m C4.

## De 8 advertenties

### B1 `bl_b1_lekkerzitten` · beige · /products/leeskussen-beige
**In beeld:** Eindelijk lekker zitten in je eigen bed.
**Tekst:**
> Voor wie elke avond leest, maar nooit echt goed zit.
>
> Dit leeskussen houdt je rechtop: 3,8 kg traagschuim dat niet wegzakt, met een zachte katoenen hoes van 400 TC.
>
> In beige en nog 4 kleuren. €79,99, gratis verzonden.
> 👉 30 dagen proberen in je eigen bed.

**Kop:** Rechtop lezen in bed

### B2 `bl_b2_bank` · wit · /products/leeskussen-wit
**In beeld:** Te diepe bank? Zo zit je wél rechtop.
**Tekst:**
> Zak je op de bank altijd een beetje onderuit als je leest?
>
> Zet dit leeskussen achter je rug. 3,8 kg traagschuim, het blijft staan. Met een vakje voor je bril, boek of telefoon.
>
> Wit €69,99 · gratis verzonden · 30 dagen proberen.

**Kop:** Vanaf €69,99, gratis verzonden

### B3 `bl_b3_avondbed` · grijs · /products/leeskussen-grijs
**In beeld:** Je avond, je bed, rechtop.
**Tekst:**
> Laptop op schoot, serie aan, en na een kwartier zit je toch weer onderuitgezakt?
>
> Dit leeskussen houdt je rechtop: 3,8 kg traagschuim dat niet wegzakt. Je telefoon zit in het zijvak.
>
> In grijs en nog 4 kleuren. €79,99, gratis verzonden.
> 👉 30 dagen proberen in je eigen bed.

**Kop:** Rechtop in bed, de hele avond

### B4 `bl_b4_eenuur` · blauw · /products/leeskussen-blauw
**In beeld:** Zakt niet weg. Ook niet na een uur.
**Tekst:**
> Gewone kussens worden plat zodra je erop leunt. Na een uur lig je weer half.
>
> Dit leeskussen is gevuld met 3,8 kg traagschuim in stukjes en zakt niet weg.
>
> ✅ Vakje voor je telefoon
> ✅ Hoes met rits, wasbaar op 30 °C
>
> €79,99, gratis verzonden.
> 👉 Probeer 'm 30 dagen.

**Kop:** Leeskussen dat niet wegzakt

### B5 `bl_b5_doorlezen` · beige · /products/leeskussen-beige
**In beeld:** Nog even lezen. Maar dan rechtop.
**Tekst:**
> Nog één hoofdstuk, en dan nog één. En ondertussen steeds je kussens opnieuw goed leggen?
>
> Eén leeskussen in plaats van een stapel: 3,8 kg traagschuim, blijft staan. Zachte katoenen hoes van 400 TC.
>
> In beeld beige, er zijn 5 kleuren. Gratis verzonden.
> 👉 30 dagen proberen.

**Kop:** Eén kussen in plaats van vier

### C2 `bl_c2_echtlezen` · blauw · /products/leeskussen-blauw
**In beeld:** Alleen voor wie echt in bed leest.
**Tekst:**
> Lees je één keer per maand een bladzijde? Dan heb je dit niet nodig.
>
> Lees je elke avond, en zit je na tien minuten onderuitgezakt tegen het hoofdbord? Dan wel.
>
> Groot (50 x 65 x 45 cm) en stevig: 3,8 kg traagschuim.
> Twijfel je? 30 dagen proberen, gratis verzonden.

**Kop:** Voor wie elke avond leest

### C3 `bl_c3_nietslapen` · zwart · /products/leeskussen-zwart
**In beeld:** Niet voor wie meteen gaat slapen.
**Tekst:**
> Val je om half elf als een blok in slaap? Dan heb je dit kussen niet nodig.
>
> Lig je nog een uur te lezen, kijken of scrollen? Dan wel. 3,8 kg traagschuim houdt je rechtop en je telefoon zit in het zijvak.
>
> €79,99, gratis verzonden. Twijfel je? 30 dagen proberen.

**Kop:** Voor de avondmens

### C4 `bl_c4_werkbed` · grijs · /products/leeskussen-grijs
**In beeld:** Werk je vaak vanuit bed? Zo zit je wél rechtop. · 3,8 kg traagschuim dat niet wegzakt.
**Tekst:**
> Werken vanuit bed klinkt lekker, tot je na tien minuten tegen het hoofdbord hangt.
>
> Dit leeskussen heeft 3,8 kg traagschuim en blijft staan, ook met je laptop op schoot.
>
> ✅ Zijvak voor je telefoon
> ✅ 50 x 65 x 45 cm
> ✅ Hoes met rits, gaat in de was
>
> Gratis verzonden.
> 👉 30 dagen proberen.

**Kop:** Werken vanuit bed, maar rechtop

Knop bij alle advertenties: **Nu kopen**. UTM volgens `reports/Bline meetplan.md`. Meta's eigen AI-tekstvarianten en het herschrijven van tekst in beelden uitzetten.

## Testplan

| Onderdeel | Keuze |
|---|---|
| Campagne | `bl_meta_sales_nlbe`, doel Verkopen, optimaliseren op Aankoop (Pixel 1) |
| Opbouw | 1 advertentieset met alle 8 advertenties. Met €150 budget is splitsen per stijl te dun; Meta verdeelt zelf over de advertenties en we lezen per advertentie af |
| Doelgroep | Nederland en België, 30 tot 65+, breed, Advantage+ plaatsingen |
| Budget | €10 per dag, 14 dagen (€140, past in het vooraf betaalde saldo van €150) |
| Uitzetten | advertentie na €8 uitgave met link-klikratio onder 0,6%; na 7 dagen advertenties zonder winkelwagen |
| Afrekenen | na 14 dagen: welke stijl (rustig of kwalificerend) en welke zinnen de laagste kosten per winkelwagen en aankoop hebben. Daarvan nieuwe varianten maken, de rest uit |

Voorwaarde vooraf: de testprocedure uit het meetplan is gedaan (Purchase komt binnen in Meta).
