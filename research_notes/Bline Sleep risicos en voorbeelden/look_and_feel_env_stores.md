# Look and feel van de ENV-stores, en wat Bline daarvan overneemt

Onderzoek 05-10-2026. Homepages van tien shops uit de omgeving bekeken (publieke pagina's, screenshots in `env_screens/homepages_env_stores.jpg`), met de berekende stijl van achtergrond, tekst, koppen en knoppen. Doel: Bline mag niet ogen als een standaard AI-site.

## Wat de echte shops doen (gemeten)

| Shop | Achtergrond | Tekst | Lettertype | Accent (balk of knop) | Kop op de homepage |
|---|---|---|---|---|---|
| Tofvel | wit | zwart | azo-sans, 700, hoofdletters | donkerblauw #1D3040 met oranje knop #F0A327 | "Handgemaakte Premium Pantoffels uit Nepal" |
| Piedi Nudi | wit | #080808 | DM Sans 500 | zwart, ronde knop | "HERFST / WINTER", knop "Ontdek de collectie" |
| Sockwell | wit | #080808 | Poppins 700 | bordeauxbalk, roze knop #D69896 | foto's, "Nieuwe collectie" |
| Lazamani | wit | #080808 | Poppins 700, hoofdletters | aubergine balk, zandknop #D3BC9C | "WINTER '26", "SHOP COLLECTIE" |
| HEYDUDE | gebroken wit #F2F0EB | zwart | Arial 700, hoofdletters | bijna zwart #2C282C | "WARNING! You can never get enough comfort" |
| KEEN | wit | zwart 75% | Raleway 700 | zwart | "NEW IN: Jouw nieuwe favorieten", "Shop nu" |
| Jan Jansen | wit | #262626 | Agenda 700, hoofdletters | rood (sale) | "SALE" |
| Toni Pons | #ECE6E4 | #080808 | Bodoni Moda 700, hoofdletters | bordeaux #932036 | "NEW COLLECTION", "SHOP NU" |

## Patronen

1. **Wit of bijna wit**, zwarte tekst. De kleur komt uit de foto's, niet uit de achtergrond.
2. **Eén merkkleur**, sterk en donker, in de aankondigingsbalk en soms de header (donkerblauw, bordeaux, aubergine, zwart). Knoppen in die kleur of in één tweede accent.
3. **Schreefloos en vet** (Poppins, DM Sans, Raleway, Arial), vaak hoofdletters voor korte koppen. Alleen het modemerk Toni Pons gebruikt een schreefletter.
4. **Grote echte foto met mensen**, korte kop van 2 tot 5 woorden, één knop.
5. **Vertrouwen zichtbaar**: Trusted Shops-score in beeld, chatknop "Hulp", score in de balk ("Uitstekend beoordeeld").
6. **Knoppen en labels die iedereen kent**: "Shop nu", "Bekijk alle", "Alle sokken", "Ons verhaal", "In winkelwagen", "Afrekenen".

## Wat als AI oogt (en Bline nu nog had)

- Crème achtergrond (#F7F4EF) met dunne schreefletter (Cormorant), saliegroen en goud: de standaard "premium wellness"-look die generatoren maken. Geen enkele ENV-shop gebruikt die combinatie.
- Inter als enige letter: de standaardletter van gegenereerde sites.
- Teksten met vetgedrukte drieluiken ("Zondagochtend. / Het blijft staan. / Wat je krijgt."), "Je kent het.", grapjes op commando ("past niet in je handbagage"), "antwoord van een mens", "X klinkt gezellig. Tot je ...".

## Besluit voor Bline

| Onderdeel | Was | Wordt |
|---|---|---|
| Achtergrond | crème #F7F4EF | wit #FFFFFF, tweede vlak lichtgrijs #F4F4F2 |
| Tekst | #1F2A37 | #1A1A1A |
| Merkkleur | salie en goud | inktblauw #1F2A37 (uit het logo): balk, knoppen, voettekst |
| Lettertype | Cormorant (koppen) en Inter | één schreefloze letter met ronde vorm die bij het logo past: Nunito Sans (anders DM Sans), koppen 700, korte koppen in hoofdletters |
| Knoppen | rond | 6 px hoeken, effen inktblauw, witte tekst |
| Hero | lange zin | foto (beige, vrouw met boek), kop van 2 tot 4 woorden, knop "Shop nu" |
| Balk | lange zin | hoofdletters met strepen: GRATIS VERZENDING NL EN BE \| BINNEN 1-2 WERKDAGEN IN HUIS \| 4,5 UIT 5 OP BOL.COM |
| Onder de knop | twee regels | vier vinkjes (zoals Tofvel en Toni Pons): gratis verzending, 1-2 werkdagen, hoes wasbaar op 30 °C, 14 dagen bedenktijd |
| Productinfo | lopende tekst | korte beschrijving (3 tot 5 zinnen) en daaronder "Kenmerken" als lijst |

## Taal: aanvulling op de schrijfstijlgids

1. Kort en zakelijk-vriendelijk, zoals een winkel praat. Koppen van 2 tot 5 woorden.
2. Gangbare winkelwoorden mogen: "Shop nu", "In winkelwagen", "Bekijk", "Kenmerken", "Beschrijving", "Gratis verzending".
3. Geen vetgedrukte drieluiken, geen "Je kent het", geen geforceerde grapjes, geen zinnen over "een mens" of "eerlijk".
4. Feiten in lijstjes met vinkjes, niet in verhaaltjes.
5. Een beetje verkoop mag ("Rechtop lezen zonder gedoe"), superlatieven blijven verboden.

## Mobiel (90% van het verkeer, Joost 05-10)

Bekeken: productpagina's van Tofvel, Lazamani, Piedi Nudi, Sockwell en HEYDUDE op 390 px breed (`env_screens/productpaginas_mobiel.jpg`).

**Wat werkt bij hen**
- Eerste scherm: balk, compacte header (logo, zoeken, account, winkelwagen, menu), grote productfoto over de volle breedte met pijltjes of teller ("1 / 4"), dan titel, sterren met aantal, korte ondertitel en prijs.
- Kleurkeuze als kleine productfoto's (Tofvel), maatknoppen groot genoeg voor een duim.
- Knop over de volle breedte, groot en in één kleur ("Bestel Nu!", "Toevoegen aan winkelmand"), direct daaronder vinkjes met voordelen (Tofvel).
- Beschrijving en kenmerken als uitklapblokken.

**Wat stoort bij hen (niet doen)**
- Een pop-up met "10% korting" die bij binnenkomst de hele productpagina bedekt (Lazamani, Sockwell, HEYDUDE).
- Zwevende knopjes over de inhoud: Trusted Shops-badge, chatknop "Hulp" en een cookie-icoon die tegelijk tekst en knoppen afdekken.
- De balk op twee regels (Tofvel), waardoor het eerste scherm kleiner wordt.

**Checklist mobiel voor Bline**
1. Balk op één regel: op mobiel wisselende berichten (één tegelijk), niet de lange regel met strepen.
2. Header maximaal ongeveer 60 px hoog; winkelwagen met aantal altijd zichtbaar.
3. Galerij als veegslider over de volle breedte met teller ("1 / 8") of puntjes, geen raster met miniaturen op mobiel. Eerste foto direct laden, de rest later.
4. In het eerste scherm (390 x 844): foto, titel, "4,5 uit 5 op bol.com (13)", prijs. De knop mag net onder de vouw staan, de meelopende knop vangt dat op.
5. Kleurkeuze met vlakken of foto's van minimaal 44 x 44 px, met de kleurnaam erbij.
6. Knop "In winkelwagen" over de volle breedte, minimaal 48 px hoog.
7. Vier vinkjes direct onder de knop.
8. Beschrijving, Kenmerken, Verzending en retour, Vragen: uitklapblokken, Beschrijving standaard open.
9. Meelopende knop onderaan: volle breedte, prijs plus knop, maximaal 64 px hoog, niets anders dat zweeft (geen chatknop, geen badge). De cookiemelding mag de knop niet blijvend afdekken.
10. Geen pop-ups.
11. Tekst minimaal 16 px (invoervelden ook, anders zoomt iPhone in), tikdoelen minimaal 44 px, genoeg ruimte tussen links in de voettekst.
12. Snelheid: één lettertype in twee gewichten, foto's via Shopify-CDN met srcset, eerste foto niet lazy, geen zware apps. Doel Lighthouse mobiel 80+ (te meten zodra het wachtwoord beschikbaar is).
13. Winkelwagenlade op mobiel over de volle breedte, knop "Afrekenen" onderaan altijd zichtbaar.
