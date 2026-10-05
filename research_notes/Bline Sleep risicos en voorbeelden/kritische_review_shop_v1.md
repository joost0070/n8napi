# Kritische review Bline-shop v1 tegen de ENV-stores

Datum 05-10-2026. Bekeken: de mobiele en desktop-testpagina's van sessie 6 (`mockups/blinesleep/screenshots/shop/mobiel/`) naast de screenshots van Tofvel, Piedi Nudi, Lazamani, Sockwell en HEYDUDE (`env_screens/`). Maatstaf: zou dit naast die shops staan zonder op te vallen als template of AI-site? Antwoord nu: **nog niet helemaal**. Het oogt schoon, maar nog te veel als standaard-Dawn.

## Wat al goed is

- Wit, inktblauw, één schreefloze letter: rustig en geloofwaardig.
- Grote echte foto, score met bron, vinkjes onder de knop, uitklapblokken: dezelfde opbouw als Tofvel en Piedi Nudi.
- Geen pop-ups en geen zwevende widgets. Daarin is Bline al beter dan Lazamani, Sockwell en HEYDUDE.

## Wat nog als template oogt, met de oplossing

| Nr | Probleem | Hoe de ENV-stores het doen | Oplossing voor Bline |
|---|---|---|---|
| 1 | Prijs klein (circa 18 px) onder een hele grote titel: verkeerde rangorde | Tofvel en Lazamani: prijs vet en duidelijk, titel kleiner | Titel 26 tot 28 px desktop en 22 tot 24 px mobiel, gewicht 700. Prijs 22 tot 24 px, gewicht 700 |
| 2 | Geen ondertitel onder de productnaam | Tofvel "Handgemaakte Nepalese sloffen", Lazamani "Zwarte leren teensandalen", Piedi Nudi "Leren enkellaarsjes met comfortabele pasvorm" | Ondertitel: "Met vak voor je boek, 65 x 50 x 45 cm" |
| 3 | "Inclusief belasting." (letterlijke standaardtekst van Dawn) | niet getoond, of "incl. btw" | "Incl. btw" klein en grijs, of weg |
| 4 | Label "Kleur" zonder de gekozen kleur | Tofvel "KLEUR/PRINT: Zwart" | "Kleur: Wit", met de naam die meeverandert |
| 5 | Afgeronde hoeken om de productfoto's (standaard-Dawn) | rechte hoeken bij alle shops | Hoekafronding van beelden en kaarten op 0 |
| 6 | Lichtgrijze lopende tekst met veel regelafstand en inspringing | bijna zwarte tekst, compact | Tekst #1A1A1A, regelafstand 1,5, geen inspringing in de uitklapblokken |
| 7 | Balk met 16 px vette hoofdletters: zwaar en druk | 11 tot 13 px hoofdletters met wat letterafstand | Balk 13 px, gewicht 600, letterafstand 0,06 em. De 16 px-regel geldt voor lees- en invoertekst, niet voor de balk |
| 8 | Desktop: alleen een hamburgermenu | Tofvel, Lazamani, Sockwell: menu uitgeschreven in de header | Desktop: "Leeskussen", "Losse hoes", "Over Bline", "Vragen" in de header. Mobiel blijft hamburger |
| 9 | Geen betaalmethoden in beeld bij de knop | betaaliconen in de voettekst, Lazamani ook "kopersbescherming" bij de knop | Rij kleine iconen onder de vinkjes: iDEAL, Bancontact, Apple Pay, Visa, Mastercard (de standaardiconen van Shopify) |
| 10 | Witte vlakken tussen blokken zijn groot en gelijk (template-ritme) | strakker, met afwisseling van wit en een licht vlak | Sectieruimte omlaag (desktop 48 px, mobiel 32 px); "Goed om te weten" in het lichte vlak houden |
| 11 | Knoppen en kleurvlakken met dunne grijze rand en zachte hoeken: standaard | knoppen met rechte of licht afgeronde hoeken, vet | Hoeken 4 px, rand van kleurvlakken 1 px #1A1A1A bij hover en geselecteerd 2 px |
| 12 | Homepage nog niet beoordeeld | foto met mensen, korte kop, één knop, daarna producten en vertrouwen | Testpagina-screenshots van de homepage maken en dezelfde lat leggen |

## Werkwijze voor elke volgende ronde

1. Na elke wijziging een testpagina-screenshot op 390 x 844 en op 1366 x 800, van product, homepage en lade.
2. Leg elke screenshot naast de ENV-screenshot van hetzelfde type (`env_screens/productpaginas_mobiel.jpg`, `env_screens/homepages_env_stores.jpg`) en loop de tabel hierboven af.
3. Pas als alle 12 punten "ja" zijn, is de ronde klaar. Onzeker? Kies wat de meerderheid van de ENV-stores doet.
