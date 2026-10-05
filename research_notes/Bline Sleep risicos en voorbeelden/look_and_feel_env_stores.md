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
