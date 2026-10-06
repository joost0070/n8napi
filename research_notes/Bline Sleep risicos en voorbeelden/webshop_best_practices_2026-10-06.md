# Webshop best practices voor Bline (06-10-2026)

Onderzoek naar de best presterende aanpak per facet voor een Shopify-shop met één hoofdproduct (leeskussen, €69,99 tot €79,99, vijf kleuren, losse hoezen als upsell), 90% mobiel verkeer, markt Nederland en België.

## Hoe je dit rapport leest

Elke bevinding heeft een label:

- **[A/B-test]**: gemeten in een gecontroleerde test. Let op: de meeste openbare A/B-cases komen van bureaus en apps. Ze noemen vaak geen steekproef of significantie. Dat staat er dan bij.
- **[groot onderzoek]**: enquête of data van veel winkels of mensen. Laat zien wat mensen zeggen of wat samen voorkomt, niet altijd oorzaak en gevolg.
- **[usability-onderzoek]**: geobserveerde gebruikerstests (vooral Baymard en Nielsen Norman Group). Sterk in het vinden van problemen, zegt weinig over de grootte van het effect op omzet.
- **[regel]**: wet, toezichthouder of richtlijn van een platform. Geen keuze.
- **[mening]**: blog, leverancier of expert zonder openbare meting.

Een algemene waarschuwing vooraf. GoodUI verzamelde 644 A/B-tests op bekende ontwerppatronen. Daarvan waren er 169 winnaars en 43 verliezers. De rest was niet significant ([groot onderzoek], https://goodui.org/patterns/). De meeste "bewezen" trucs doen dus in een gewone test niets meetbaars. De grootste winst zit meestal in vertrouwen, duidelijkheid en de basis.

Bline heeft een duidelijk nadeel tegenover Ella Sleeps: hogere prijs (€69,99 tegen €49,95), geen eigen reviews, geen achteraf betalen, retour op eigen kosten en geen cut-off-tijd. De adviezen hieronder zijn daarop gerangschikt.

---

## Samenvatting: de 15 belangrijkste adviezen (op verwachte impact)

1. **Verzamel vanaf de eerste order eigen reviews** (met foto's) en toon sterren met aantal bij de titel en een verdeling met balkjes. De bol.com-score mag blijven, met duidelijke bron, maar niet als sterren in de structuurdata. Bewijs: 95% van de testers gebruikte reviews (Baymard); vijf reviews hingen samen met 270% hogere aankoopkans (Spiegel, observatie).
2. **Maak retour gratis en bied een proefperiode** ("30 nachten proberen, gratis retour" in NL en BE). Zet die belofte in de vinkjes bij de knop. Ella Sleeps biedt dit al. Ruimere retourvoorwaarden verhogen aankopen en een langere termijn verlaagt retouren (meta-analyse van 21 studies).
3. **Toon een leverdatum met besteltijd bij de knop**, bijvoorbeeld "Voor 16:00 besteld, morgen in huis". Alleen als het klopt. Baymard ziet dat mensen vastlopen op "1 tot 2 werkdagen"; meerdere A/B-tests laten winst zien (wel zwak gedocumenteerd).
4. **Zet de betaalmethoden goed**: iDEAL bovenaan voor NL, Bancontact voor BE, Apple Pay en Google Pay als expressknop. Zet Klarna aan via Shopify Payments en meet het aandeel en de conversie 6 tot 8 weken. iDEAL is 72% van de online aankopen in NL; Klarna 4% (Thuiswinkel Markt Monitor Q1 2026).
5. **Vink de extra hoes niet vooraf aan** en zet bundelvoordelen in euro direct naast de prijs. Een vooraf aangevinkt betaald extraatje is volgens de ACM niet toegestaan. Doorgestreepte "van"-prijzen alleen als dat de laagste prijs van de afgelopen 30 dagen was.
6. **Galerij op mobiel: kleine duimnagels in plaats van alleen stippen**, eerste beeld het kussen helder en herkenbaar, met minstens één beeld dat de maat laat zien en één uitlegbeeld met tekst (vulling, maat). 76% van de mobiele sites gebruikt geen duimnagels en dat kost vindbaarheid (Baymard).
7. **Snelheid**: eerste galerijbeeld niet lazy-loaden en met `fetchpriority="high"`, video pas laden bij afspelen, zo min mogelijk apps. Meet de Core Web Vitals in het Shopify-rapport. Google/Deloitte vonden dat 0,1 seconde sneller samenhing met 8,4% meer conversie in retail.
8. **Winkelwagenlade houden**, met expressknoppen (Apple Pay, Shop Pay, Google Pay) en precies één relevante upsell (hoes in dezelfde kleur, als die nog niet in de wagen zit). Geen gratis-verzending-balk: verzending is al gratis, dus zet "Gratis verzending" als regel in het overzicht.
9. **Meelopende knop onderaan behouden** (verschijnt als de grote knop uit beeld is), volle breedte, met gekozen kleur en prijs. Geen zwevende WhatsApp-bubbel er overheen. Het bewijs is gemengd: tests variëren van +10% tot -7,7% conversie.
10. **Checkout-instellingen**: één-pagina-checkout, gastcheckout, telefoon optioneel, adres automatisch aanvullen aan, geen kortingscodes adverteren zolang er geen actie is. Bewijs: 19% haakt af bij verplicht account, 14% bij een verplicht telefoonveld zonder uitleg (Baymard, VS).
11. **Copy die het prijsverschil uitlegt**: kop met de belofte, daarna 3 tot 5 voordelen met concrete cijfers, feitelijk geschreven. Een eerlijke vergelijking met losse kussens en vragen die bezwaren wegnemen (prijs, wassen, maat, retour). Feitelijke, korte, scanbare tekst scoorde 124% beter in bruikbaarheid (NN/g, oud onderzoek).
12. **Vertrouwen en verplichtingen**: KvK-nummer, btw-id, adres en e-mail in de footer (verplicht). WhatsApp als link, niet als zwevende bubbel. Keurmerk pas na de eerste reviews; WebwinkelKeur is goedkoop, Thuiswinkel Waarborg wordt het best herkend (96% herkenning in een Consumentenbond-panel).
13. **Google Merchant Center en structuurdata**: gratis productvermeldingen aan, retour- en verzendbeleid in Merchant Center, Product-structuurdata op de productpagina (niet op de homepage dubbel), eigen reviews pas als ze er zijn. Voor AI-zoekmachines zegt Google dat er geen extra trucs nodig zijn; vermeldingen elders (bol, YouTube, artikelen) hangen het sterkst samen met zichtbaarheid.
14. **E-mail**: verlaten checkout opvolgen met 2 tot 3 mails (eerste na ongeveer een uur). Reviewverzoek pas na levering. Geen welkomstkorting als standaard: het kost marge en er is geen openbaar bewijs dat het netto winst oplevert.
15. **Eerst meten, dan pas testen**: trechter in Shopify (sessies, in winkelwagen, checkout bereikt, gekocht), gedrag met Microsoft Clarity na toestemming. Met de huidige aantallen zijn A/B-tests op kleine wijzigingen niet betrouwbaar: bij 2% conversie en 20% verwachte winst zijn ruim 21.000 bezoekers per variant nodig (eigen berekening, zie facet 14).

---

## 1. Meelopende knop (sticky add-to-cart) en sticky header

### Beste praktijk
Op mobiel scrolt de koper ver weg van de koopknop. Een balk onderaan die verschijnt als de grote knop uit beeld is, is gangbaar. De balk moet groot genoeg zijn, de gekozen variant en prijs tonen, en niets anders bedekken. De kop bovenaan klein houden of alleen tonen bij omhoog scrollen.

### Bewijs
- [A/B-test] AFTCO: meelopende knop op mobiel met prijs en icoon gaf +6,2% conversie en +3,6% omzet per bezoeker. Geen steekproef of significantie gemeld. https://cleancommit.io/ab-tests/sticky-mobile-add-to-cart-button/
- [A/B-test] Andere winkel: +6,8% tot +8,7% in winkelwagen, maar -7,7% conversie en -22,1% omzet per bezoeker. Uitkomst "niet beslissend". https://cleancommit.io/ab-tests/mobile-bottom-sticky-add-to-cart-button/
- [A/B-test] PerTronix: +10% conversie, maar niet significant. https://blendcommerce.com/blogs/ab-tests-shopify/10-increase-in-conversion-rate
- [A/B-test] Little Bible Stories: balk onderaan op mobiel beter dan bovenaan, +7% conversie, omzet per bezoeker gelijk. Significantie niet gemeld. https://blendcommerce.com/blogs/ab-tests-shopify/better-placed-sticky-add-to-cart-product-page-conversion
- [mening, kritisch] Een veel gedeelde claim dat "Baymard 7,9% gemiddelde winst" mat, vond ik niet terug bij Baymard zelf. Behandel zulke cijfers als onbetrouwbaar.
- [usability-onderzoek] Mensen tikken het nauwkeurigst in het midden van het scherm; aan de randen is de afwijking groter (7 mm in het midden tegen 12 mm in de hoeken). https://www.uxmatters.com/mt/archives/2017/07/design-for-fingers-touch-and-people-part-3.php
- [usability-onderzoek] Sticky headers helpen alleen als ze klein zijn en weinig bewegen. Een kop die alleen bij omhoog scrollen terugkomt is een goed compromis op mobiel. https://www.nngroup.com/articles/sticky-headers/

### Advies voor Bline
- De huidige balk houden zoals hij werkt (verschijnt als de grote knop weg is). Onderaan laten staan.
- Inhoud: klein kleurbolletje met naam ("Beige"), prijs van de gekozen optie, knop "In winkelwagen". Knop minstens 48 px hoog, volle breedte min marges, vanwege de minder nauwkeurige rand.
- Tik op de balk voegt direct toe met de gekozen opties. Opent de lade.
- Kop bovenaan: klein, alleen logo, menu en winkelwagen met aantal. Bij voorkeur alleen tonen bij omhoog scrollen, zodat kop en balk samen niet te veel scherm innemen.
- Geen chatbubbel of cookie-knopje dat over de balk valt.

---

## 2. Winkelwagen: lade, pagina of direct naar checkout

### Beste praktijk
Een lade (drawer) met duidelijke bevestiging, het totaal, verzendkosten, de knop naar afrekenen en expressknoppen. Eén relevante aanvulling, geen rij aanbevelingen. Een gratis-verzending-balk heeft alleen zin als er een drempel is.

### Bewijs
- [usability-onderzoek] Na toevoegen willen mensen verder kijken, de wagen controleren of afrekenen. Een overlay werkt goed als hij het product en het totaal toont en de vervolgstappen duidelijk zijn. https://www.baymard.com/ecommerce-design-examples/added-to-cart-confirmation
- [usability-onderzoek] NN/g zag dat mensen in de war raakten als niet duidelijk was of iets was toegevoegd. https://www.nngroup.com/articles/ecommerce-product-pages/
- [A/B-test] Singular Sound: expressknoppen (Shop Pay, PayPal, Google Pay) in de lade gaven +35,44% conversie en +56,77% omzet per bezoeker, 13 dagen, 95,89% significantie, steekproef niet gemeld. https://blendcommerce.com/en-gb/blogs/ab-tests-shopify/adding-express-checkout-in-the-cart-drawer
- [A/B-test] Gratis-verzending-balk in de minicart: +9,2% gemiddelde orderwaarde, -5,9% conversie, +3,2% omzet per bezoeker. https://cleancommit.io/ab-tests/visual-free-shipping-progress-indicator
- [mening] Lade tegen pagina: blogs noemen de lade beter op mobiel, maar ik vond geen openbare test met steekproef. https://cartylabs.com/blog/shopify-cart-page-vs-cart-drawer/
- [usability-onderzoek] Baymard raadt aan zowel alternatieven als aanvullende producten aan te bieden; slechts 42% doet het goed. https://baymard.com/product-page/articles

### Advies voor Bline
- Lade houden. Direct naar checkout is te riskant: mensen willen hun keuze (kleur, aantal, hoes) nog zien.
- In de lade, van boven naar onder: "Toegevoegd" met foto in de gekozen kleur, aantal aanpasbaar, subtotaal, regel "Verzending: gratis", knop "Afrekenen", daaronder de expressknoppen (Shopify toont die via de accelerated checkout buttons).
- Eén upsell: "Extra hoes in Beige, €X". Alleen tonen als die nog niet in de wagen zit. Niet vooraf aanvinken.
- Geen gratis-verzending-balk. Een voortgangsbalk naar "2 kussens" kan, maar dat is een test voor later.
- Expressknoppen in de lade zijn de best onderbouwde aanpassing hier. Let op dat de lade daardoor niet onrustig wordt: maximaal één rij.

---

## 3. Productafbeeldingen

### Beste praktijk
Minstens 3 tot 5 beelden per variant, waarvan één met schaal (het kussen bij een persoon), één met uitleg in tekst, voldoende resolutie en inzoomen met twee vingers. Op mobiel duimnagels of een duidelijk teken dat er meer beelden zijn. Kleurwissel wisselt de hele galerij. Video mag, maar niet als eerste beeld.

### Bewijs
- [usability-onderzoek] 100% van de desktopsites gebruikt duimnagels, maar maar 24% van de mobiele sites. Bij alleen stippen of tekst vonden gebruikers extra beelden slechter; de helft van de desktopgebruikers had moeite. https://baymard.com/blog/always-use-thumbnails-additional-images
- [usability-onderzoek] 42% van de gebruikers probeert de maat uit de foto's af te leiden; 28% van de sites heeft geen beeld op schaal. https://baymard.com/blog/in-scale-product-images
- [usability-onderzoek] 52% van de sites zet geen uitleg of tekst bij beelden waar dat nodig is; 25% heeft te weinig resolutie of zoom. https://baymard.com/product-page/articles
- [usability-onderzoek] Baymard noemt 3 tot 5 beelden als minimum. https://baymard.com/learn/ecommerce-ux-best-practices
- [usability-onderzoek] NN/g: 360-graden en andere "fancy" functies alleen als ze foutloos werken; meerdere beelden en video zijn "nice to have". https://www.nngroup.com/articles/ecommerce-product-pages/
- [mening] Sfeerbeeld of productbeeld eerst: claims van "15 tot 30%" winst voor sfeerbeelden komen uit blogs zonder test. Er is geen algemene winnaar. https://nightjar.so/blog/how-to-ab-test-product-images-and-what-weve-learned
- [A/B-test, zwak] Video op de productpagina: leveranciers melden winst (bijvoorbeeld +11,8% en +45%), maar dit zijn eigen cases van videoapps. https://www.whatmore.ai/blog/is-your-shoppable-video-lift-real/
- [mening] Verhouding 4:5 tegen 1:1: 4:5 vult meer van een telefoonscherm. Geen onafhankelijke test gevonden. Wel belangrijk: één vaste verhouding voorkomt verspringen bij laden.
- [usability-onderzoek] Hover op kaarten (desktop): Baymard adviseerde eerst één extra beeld bij hover; nieuwere tests laten zien dat mensen meer beelden in de lijst willen zien. https://baymard.com/blog/Secondary-hover-information
- [regel] Google Merchant Center meet onder meer het aandeel beelden groter dan 1048 pixels en het aantal beelden per product voor het "Top Quality Store"-label. https://support.google.com/merchants/answer/14261098?hl=en

### Advies voor Bline
- Volgorde per kleur (de huidige opbouw is goed): 1) kussen op bed met boek, helder en herkenbaar, 2) iemand die erin leest (schaal), 3) andere persoon en kamer, 4) vulling met korte tekst ("Vulling: ...", uitleg), 5) maattekening met cm, 6) hoes los en wasbaar, 7) label. 7 tot 9 beelden is genoeg; meer is vermoeiend vegen.
- Begin niet met een mens waarvan het kussen klein in beeld is. Het eerste beeld moet in één blik zeggen: dit is een leeskussen in deze kleur.
- Mobiel: onder het grote beeld een rij kleine duimnagels (horizontaal scrolbaar), of minstens de teller "1/9" groot genoeg. Alleen stippen is het zwakst onderbouwde patroon.
- Verhouding: kies 4:5 voor alle galerijbeelden op mobiel, met vaste breedte en hoogte in de HTML (tegen verspringen).
- Zoom: inzoomen met twee vingers in een volledig scherm.
- Kleurwissel zonder te laden: goed. Laat de wissel ook de duimnagels en het eerste beeld van de meelopende balk aanpassen.
- Video: als 2e of 3e item, met stilstaand voorbeeldbeeld, pas laden bij tikken. Geen 360-graden.
- Desktop: het raster van 2 kolommen is prima. Hover met tweede beeld alleen bij de hoezenkaarten (hoes los, daarna hoes om kussen).

---

## 4. Opbouw van de productpagina

### Beste praktijk
Boven de vouw op mobiel: beeld, titel met korte ondertitel, sterren met aantal, prijs met eventueel voordeel, kleurkeuze met naam, aantal of bundel, knop, en direct daaronder levering, retour en betaalmethoden. Daarna uitklapblokken (geen tabbladen), korte beschrijving met highlights, specificaties in een tabel, reviews met verdeling.

### Bewijs
- [usability-onderzoek] Horizontale tabbladen zorgen dat mensen inhoud missen. Op mobiel werkten ingeklapte secties (accordeons) het best. https://baymard.com/research-articles/avoid-horizontal-tabs
- [usability-onderzoek] 64% van de gebruikers zoekt verzendkosten al op de productpagina; 43% van de sites toont ze daar niet. https://baymard.com/research-articles/show-shipping-costs-on-product-pages
- [usability-onderzoek] "Gratis verzending" alleen in een balk bovenaan wordt over het hoofd gezien (32% van de sites doet het zo). https://baymard.com/product-page/articles
- [usability-onderzoek] 41% van de sites geeft geen leverdatum; mensen stoppen dan om te rekenen of te gokken. https://baymard.com/blog/shipping-speed-vs-delivery-date
- [A/B-test] Best Heating: duidelijkere levertekst per kleur, 28.352 sessies, 8 dagen, +9,06% transacties, significantie niet gemeld. https://fabric-analytics.com/case-study/best-heating-cro
- [A/B-test, zwak] Rylee + Cru: leverdatum op productpagina, wagen en checkout, +22,4% conversie; geen steekproef of significantie. https://www.shoplift.ai/success-stories/how-fenix-commerce-helped-rylee-cru-increase-conversion-rate
- [usability-onderzoek] Beschrijving opgebouwd uit highlights met beeld of icoon maakt mensen enthousiaster; 78% van de sites doet dit niet. https://baymard.com/research-articles/structure-descriptions-by-highlights
- [usability-onderzoek] 95% van de testers gebruikte reviews; de verdeling van sterren was het meest gebruikte onderdeel; 43% van de grote sites toont geen verdeling. https://baymard.com/blog/user-ratings-distribution-summary
- [groot onderzoek, observatie] Spiegel Research Center (data van een cadeauwinkel, 15,5 miljoen paginaweergaven, 1.800 producten): aankoopkans bij vijf reviews 270% hoger dan bij nul; bij duurdere producten +380%, bij goedkopere +190%; aankoopkans piekt bij 4,0 tot 4,7 sterren en daalt richting 5,0. Dit is samenhang, geen A/B-test. https://spiegel.medill.northwestern.edu/how-online-reviews-influence-sales/
- [usability-onderzoek] Reviewfoto's: 34% van de sites laat klanten geen foto's uploaden; 87% reageert niet op negatieve reviews, terwijl gebruikers een reactie zien als teken van goede service. https://baymard.com/product-page/articles
- [usability-onderzoek] Kleurnamen zijn makkelijker te begrijpen met een beeld of bolletje ernaast. https://baymard.com/blog/color-and-variation-searches
- [usability-onderzoek] Prijs en kortingen: prijs groot en duidelijk, voordeel direct bij de prijs, elk voordeel één keer noemen, besparing in euro of procent tonen. https://baymard.com/research-articles/product-page-price-discounts
- [usability-onderzoek, vertrouwen] Bekende betaalmerken (Visa, Mastercard, PayPal) gaven in een enquête van ongeveer 2.100 Amerikanen het meeste vertrouwen. https://cxl.com/research-study/trust-seals/
- [usability-onderzoek] Bekende merken hebben minder vertrouwenssignalen nodig; onbekende winkels juist meer. Elk zichtbaar keurmerk scoorde beter dan geen. https://baymard.com/blog/perceived-security-of-payment-form
- [A/B-test, zwak] Vertrouwensbadges: de meeste openbare cases zijn oud en klein (bijvoorbeeld +1,27% bij Uptowork). Badge-enquêtes overschatten het effect vaak. https://static.wingify.com/vwo/uploads/2019/06/how-uptowork-focused-visitor-trust-improved-conversions_2019-06-27-12-10-49.pdf

### Advies voor Bline
Volgorde boven de vouw op mobiel:
1. Galerij.
2. Titel "Bline leeskussen" met ondertitel ("Met vak voor je boek, 65 x 50 x 45 cm").
3. Sterren met aantal, zodra er eigen reviews zijn. Tot die tijd: "4,5 van 5 op bol.com (13 reviews)" met link naar de bron.
4. Prijs van de gekozen optie, groot. Bij 2 kussens: totaalprijs met daaronder "Je bespaart €9,99".
5. "Kleur: Beige" met vijf bolletjes. Wit en beige lijken op een klein scherm op elkaar: overweeg beeld-bolletjes (klein fotootje van het kussen) of een dunne rand rond het witte bolletje.
6. Keuze 1 of 2 kussens als twee grote knoppen met per stuk-prijs.
7. Vinkje "Extra hoes in Beige (+€X, je bespaart €9,99)". Niet vooraf aangevinkt (zie facet 8).
8. Knop "In winkelwagen, €69,99".
9. Direct onder de knop vier vinkjes: "Voor 16:00 besteld, morgen in huis" (alleen als het klopt; zie facet 6), "Gratis verzending en retour in NL en BE", "30 nachten proberen", "Hoes wasbaar op 30 °C".
10. Rij betaaliconen: iDEAL, Bancontact, Apple Pay, Visa, Mastercard (en Klarna als dat aan staat).

Daarna:
- Uitklapblokken, geen tabbladen: "Wat krijg je", "Maat en vulling", "Wassen", "Verzending en retour", "Garantie". Belangrijke punten (verzending, retour) staan óók zichtbaar bij de knop, niet alleen in een blok.
- Beschrijving: 3 tot 5 highlights met icoon of beeld (rugsteun, armleuningen, vak voor boek of telefoon, wasbare hoes, vulling die vorm houdt). Daarna een korte specificatietabel: maat, gewicht, vulling, materiaal hoes, wasvoorschrift, garantie.
- Reviews: sterren bij de titel (ankerlink naar de reviews), verdeling met balkjes, foto-reviews eerst te filteren, reageer zichtbaar op elke kritische review.
- Trust badges: geen nep-zegels of "100% veilig"-plaatjes. Wel betaaliconen en, als je het hebt, één echt keurmerk.
- Garantie: noem een concrete termijn als je die kunt waarmaken.

---

## 5. Homepage voor een shop met één product

### Beste praktijk
Er is geen openbaar onderzoek dat een aparte homepage vergelijkt met een homepage die zelf de productpagina is. Wat wel vaststaat: mensen moeten op elke instappagina binnen een paar seconden kunnen kopen, en content die automatisch beweegt werkt slecht.

### Bewijs
- [mening] Shopify-community en blogs: veel single-product shops sturen bezoekers direct naar het product. Geen gepubliceerde test met steekproef gevonden. https://community.shopify.com/t/can-i-set-a-product-page-as-the-homepage-on-my-online-store/133546
- [usability-onderzoek] 52% van de mobiele sites heeft een automatisch draaiende carrousel; testers scrolden er voorbij of raakten afgeleid. Baymard adviseert vaste secties of een carrousel zonder automatisch draaien. https://baymard.com/blog/homepage-carousel
- [regel] WCAG 2.2.2: inhoud die vanzelf beweegt, langer dan 5 seconden, naast andere inhoud, moet te pauzeren of te stoppen zijn. https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html
- [regel] De Europese toegankelijkheidswet geldt sinds 28 juni 2025 ook voor webshops, maar micro-ondernemingen (minder dan 10 medewerkers en maximaal €2 miljoen omzet) zijn uitgezonderd. https://www.taylorwessing.com/en/insights-and-events/insights/2025/09/european-accessibility-act-requirements-for-e-commerce-services
- [usability-onderzoek] Verborgen navigatie (hamburger) gaf 20% minder vindbaarheid en was op mobiel 15% trager dan zichtbare navigatie (179 deelnemers, 2015). https://www.nngroup.com/articles/hidden-navigation-methodology/

### Advies voor Bline
- Homepage als productpagina houden. Het past bij één product en betaald verkeer.
- Let op dubbele inhoud: de productpagina bestaat ook op `/products/...`. Laat Google Shopping, advertenties en de Product-structuurdata naar die productpagina wijzen, en zet op de homepage alleen Organization-structuurdata (zie facet 13).
- Hero is hier de galerij met koopblok. Geen aparte banner met slogan erboven: dat duwt de knop naar beneden.
- De bewegende band met beloftes: laat hem stoppen bij aanraken, of maak hem stilstaand. Hij draait langer dan 5 seconden, dus WCAG 2.2.2 is van toepassing. Bline valt waarschijnlijk onder de uitzondering voor micro-ondernemingen, maar het is een kleine moeite.
- Menu mobiel: hamburger is prima bij een shop met één product, maar houd het kort: "Leeskussen", "Losse hoezen", "Vragen", "Over Bline", "Contact". Winkelwagen altijd zichtbaar. Desktop: dezelfde 4 tot 5 items uitgeschreven in de kop.

---

## 6. Vertrouwen en NL-specifiek

### Beste praktijk
Betaalmethoden die mensen kennen, een duidelijk en ruim retourbeleid, een concrete levertijd, bereikbare klantenservice, verplichte bedrijfsgegevens en echte reviews. Een keurmerk helpt vooral als het wordt herkend.

### Bewijs: betalen
- [groot onderzoek] Thuiswinkel Markt Monitor Q1 2026: iDEAL 58% van de bestedingen en 72% van de aankopen; creditcard 16% en 8%; Klarna 4% en 4%; machtiging 11% en 5%. https://www.betaalvereniging.nl/wp-content/uploads/2026/06/TMM-Q1-2026-NL.pdf
- [mening, leverancier] Bancontact is volgens Adyen ongeveer 65% van de Belgische e-commerce; andere bronnen noemen 78%. Precies cijfer onzeker, dominantie niet. https://www.adyen.com/en_GB/payment-methods/bancontact
- [regel] Shopify Payments in NL ondersteunt iDEAL, Bancontact en Klarna; iDEAL komt bovenaan voor Nederlandse kopers. https://changelog.shopify.com/posts/shopify-payments-now-supports-more-payment-methods
- [groot onderzoek] Berg, Burg, Keil en Puri (Journal of Financial Economics, 2025): achteraf betalen verhoogde de verkoop met 20%, vooral bij klanten met minder kredietruimte. Dit is één onderzoek op data van een webwinkel; het effect in NL, waar iDEAL domineert, is onbekend. https://ideas.repec.org/p/nbr/nberwo/33152.html
- [mening, leverancier] Cijfers als "Klarna verlaagt verlaten winkelwagens met 35%" komen van Klarna of partners zonder onafhankelijke controle.
- [regel] Achteraf betalen valt onder de nieuwe EU-richtlijn consumentenkrediet (2023/2225), die uiterlijk 20 november 2026 van toepassing is. De aanbieder moet dan kredietwaardigheid toetsen. De Nederlandse implementatiewet was in 2026 in behandeling. https://zoek.officielebekendmakingen.nl/kst-36924-3.html

### Bewijs: retour en levering
- [groot onderzoek] Baymard (VS): redenen om af te haken (zonder "alleen kijken"): 40% te hoge extra kosten, 20% te trage levering, 19% geen vertrouwen met kaartgegevens, 18% verplicht account, 13% retourbeleid niet goed, 9% te weinig betaalmethoden. https://baymard.com/lists/cart-abandonment-rate
- [groot onderzoek] Sendcloud/Nielsen (augustus 2022, 1.000 Nederlanders): 84% checkt de retourvoorwaarden vóór bestellen; 63% haakt af als retourinformatie onduidelijk is; 65% bestelt vaker bij gratis retour (jaar ervoor 71%); 1 op 4 is bereid retourkosten te betalen. https://www.emerce.nl/wire/gratis-retourneren-retour-1-4-consumenten-betaalt-zonder-mokken-retourkosten
- [groot onderzoek] Sendcloud 2025 (8.000 consumenten in 8 landen): 59,4% van de Nederlanders annuleert bij hoge verzendkosten; 78,7% kiest liever gratis dan snel. https://www.sendcloud.com/nl/blog/meerderheid-nederlandse-online-shoppers-haakt-af-bij-hoge-verzendkosten/
- [groot onderzoek] Meta-analyse van 21 studies (Janakiraman, Syrdal en Freling, Journal of Retailing 2016): ruimere retourvoorwaarden verhogen aankopen; een langere termijn verlaagt het aantal retouren (mensen hechten zich aan wat ze langer hebben). https://news.utdallas.edu/?p=11491
- [regel] Bedenktijd is wettelijk minimaal 14 dagen. Retourkosten mogen bij de klant liggen als dat vooraf is gemeld.

### Bewijs: keurmerken, reviews en contact
- [groot onderzoek] Consumentenbond 2022 (panel van 8.000): herkenning Thuiswinkel Waarborg 96%, Webshop Keurmerk 59%, WebwinkelKeur 40%, Trusted Shops 19%. Veel vertrouwen: Thuiswinkel 49%, Webshop Keurmerk 30%, Trusted Shops 21%, WebwinkelKeur 20%. https://www.consumentenbond.nl/online-kopen/keurmerken-webwinkels
- [groot onderzoek, oud] TNS NIPO en Thuiswinkel.org meldden in 2010 dat 72% zegt eerder te kopen bij een winkel met Thuiswinkel Waarborg (2009: 66%). Onderzoek in opdracht van de keurmerkhouder, gaat over wat mensen zeggen, en is oud. https://id.nl/huis-en-entertainment/computer-en-gaming/desktops-en-monitoren/consument-vindt-webwinkel-met-keurmerk-betrouwbaar
- [regel] Webwinkels moeten op een logische plek tonen: naam zoals bij de KvK, KvK-nummer, adres, e-mail plus een tweede contactmogelijkheid, en btw-id. https://ondernemersplein.overheid.nl/regels-voor-bedrijfscorrespondentie/
- [regel] ACM: wie reviews toont (ook ingebedde reviews van een andere site), moet uitleggen waar ze vandaan komen en welke controles er zijn. Niet alleen negatieve reviews weghalen. Vraag pas om een review als de klant het product heeft kunnen gebruiken. ACM Leidraad Bescherming Online Consument, mei 2024, p. 19 en 20. https://www.acm.nl/system/files/documents/leidraad-bescherming-online-consument-2024.pdf
- [usability-onderzoek] Chat die zelf opspringt of altijd zichtbaar zweeft, stoort, zeker op mobiel. Chat die de klant zelf opent via kop, footer of hulppagina werkt goed. https://baymard.com/blog/live-chat-usability-issues
- [mening] Voor WhatsApp als klantenservicekanaal in NL vond ik geen recent, onafhankelijk en controleerbaar cijfer. Oudere peilingen laten een kleine maar groeiende groep zien die WhatsApp het liefst gebruikt. Behandel het als gemak, niet als bewezen conversiefactor.

### Advies voor Bline
- **Betalen**: iDEAL (vanzelf bovenaan voor NL), Bancontact, Apple Pay, Google Pay, creditcard. Klarna aanzetten via Shopify Payments als proef. Meet 6 tot 8 weken het aandeel Klarna-orders en de conversie van de checkout, vergeleken met de 6 tot 8 weken ervoor. Dat is geen echte test, dus kijk ook naar retouren en kosten. Toon Klarna alleen als icoon en eventueel één regel onder de knop; geen grote "betaal in 3 termijnen"-blokken (kredietregels worden strenger).
- **Retour**: gratis retour in NL en BE, en "30 nachten proberen". Dit is het grootste verschil met Ella Sleeps. Wil je de kosten beperken, begin dan met gratis retour binnen 30 dagen en meet het retourpercentage per maand.
- **Levering**: noem een echte besteltijd en dag ("Voor 16:00 besteld, morgen in huis" of "vandaag verzonden"). Pas het tijdstip aan op wat je magazijn echt haalt. Een belofte die je niet waarmaakt kost reviews.
- **Keurmerk**: nu nog niet. Eerst eigen reviews. Daarna kiezen: WebwinkelKeur (goedkoper, minder herkend) of Thuiswinkel Waarborg (best herkend, duurder en strengere eisen). Kosten zijn per jaar wisselend; vraag een offerte.
- **Reviewplatform**: kies één winkelreviewplatform (Trustpilot of Kiyoh) naast productreviews op de site (bijvoorbeeld Judge.me). Niet beide.
- **Contact**: WhatsApp als tekstlink bij de vinkjes en in de footer ("Vraag? App ons"), geen zwevende bubbel. E-mail en reactietijd noemen.
- **Bedrijfsgegevens**: KvK, btw-id, adres en e-mail in de footer en op een contactpagina.
- **bol.com-score**: alleen met bronvermelding en link, plus één zin over hoe bol reviews verzamelt. Geen bol-reviewteksten kopiëren (afspraak).

---

## 7. Checkout

### Beste praktijk
Gastcheckout als standaard, zo weinig velden als mogelijk, expressknoppen bovenaan, adres automatisch aanvullen, kortingsveld niet uitnodigend, en de lokale betaalmethode bovenaan.

### Bewijs
- [groot onderzoek] 19% van 1.026 Amerikaanse online shoppers brak een bestelling af omdat een account verplicht was; 62% van de sites maakt gastcheckout niet de meest opvallende optie. https://baymard.com/blog/checkout-flow-ux-optimization
- [groot onderzoek] 14% haakt af als het telefoonveld verplicht is zonder uitleg; 39% van de sites legt het niet uit. https://baymard.com/blog/checkout-form-optimization
- [usability-onderzoek] Een zichtbaar kortingsveld laat sommige testers de site verlaten om een code te zoeken. Baymard adviseert het veld in te klappen achter een link. https://baymard.com/guidelines/615-how-to-display-promotional-fields
- [mening, Shopify zelf] Shopify claimt dat Shop Pay de conversie "tot 50%" verhoogt tegenover gastcheckout en dat alleen al de aanwezigheid 5% oplevert, op basis van een onderzoek van een niet genoemd adviesbureau zonder openbare methode. Behandel dit als marketing. https://www.shopify.com/enterprise/blog/shopify-checkout
- [mening] Eén-pagina-checkout zou ongeveer 7,5% beter converteren dan drie pagina's. Dit cijfer komt van een app-bouwer, niet van Shopify. Beide opties zijn in de instellingen te kiezen. https://www.charleagency.com/articles/shopify-one-page-checkout/
- [regel] Expressknoppen staan in een "Express checkout"-blok bovenaan de checkout en kunnen ook op de productpagina. Shopify ordent ze dynamisch. https://help.shopify.com/manual/payments/accelerated-checkouts
- [regel] Adres automatisch aanvullen is in Nederland standaard actief bij Shopify. https://help.shopify.com/en/manual/checkout-settings/address-collection-preferences

### Advies voor Bline (Shopify-instellingen)
- Instellingen > Checkout: één-pagina-layout. Klantaccounts: optioneel (gast standaard). Telefoonnummer: optioneel of verborgen. Bedrijfsnaam: verborgen. Adresregel 2: optioneel. Adresaanvulling: aan.
- Marketingtoestemming: niet vooraf aangevinkt (regel, zie facet 12).
- Fooi: uit. Bestelnotities: uit.
- Expressknoppen: aan laten staan bovenaan de checkout (Shopify-standaard). Geen extra "Nu kopen"-knop op de productpagina: die naast "In winkelwagen" maakt de keuze lastiger, en er is geen goede test die hem steunt. Expressknoppen wél in de lade (facet 2).
- Kortingsveld: in de Shopify-checkout niet te verbergen. Maak geen reclame met codes zolang er geen actie is, zodat mensen niet gaan zoeken.
- Verzendkosten: "Gratis" als enige optie in NL en BE, met levertijd in dagen of datum.
- Checkout-huisstijl: rustig. Logo, één knopkleur. Shopify adviseert zelf eenvoud. https://help.shopify.com/en/manual/checkout-settings/customize-checkout-configurations/checkout-style

---

## 8. Prijspresentatie

### Beste praktijk
Prijs incl. btw, groot, direct bij de knop. Voordeel één keer, in euro, vlak bij de prijs. Doorgestreepte prijzen alleen volgens de 30-dagenregel. Geen "vanaf" op de productpagina zelf: toon de prijs van wat gekozen is.

### Bewijs
- [regel] De "van"-prijs bij een prijsverlaging moet de laagste prijs zijn die je in de 30 dagen ervoor vroeg. Uitzonderingen: bederfelijke waar, producten korter dan 30 dagen op de markt, en opeenvolgende kortingen. ACM handhaaft sinds 1 januari 2023. https://www.acm.nl/nl/publicaties/acm-wil-einde-aan-nepkortingen-na-komst-strengere-regels
- [regel] Aanbiedingen als "30% korting bij drie stuks" vallen volgens de Europese Commissie buiten deze 30-dagenregel, maar moeten wel waar en niet misleidend zijn. https://commission.europa.eu/law/law-topic/consumer-protection-law/unfair-commercial-practices-law/price-indication-directive_en
- [regel] ACM Leidraad (p. 14): prijzen tonen inclusief verplichte kosten zoals btw; kosten niet verstoppen onder een "i"-icoon; betaalde extra opties niet vooraf aanvinken. https://www.acm.nl/system/files/documents/leidraad-bescherming-online-consument-2024.pdf
- [usability-onderzoek] Vier valkuilen bij kortingen: prijs valt weg, korting staat ver van de prijs, hetzelfde voordeel staat er meerdere keren, besparing niet in euro of procent. https://baymard.com/research-articles/product-page-price-discounts

### Advies voor Bline
- Prijs: "€69,99" groot, met klein "incl. btw" of helemaal geen label (verplicht is de prijs incl. btw, niet het label).
- Verschillen de kleuren in prijs, toon dan bij elke kleurkeuze de juiste prijs. "Vanaf €69,99" alleen in advertenties, de footer of de hoezenkaarten.
- 2 kussens: "2 kussens €129,99, je bespaart €9,99" (vul de echte bedragen in). Toon ook de prijs per kussen.
- Extra hoes: "+€X (je bespaart €9,99 tegenover los kopen)". Dat voordeel moet kloppen met de echte losse prijs van de hoes.
- Doorgestreepte prijzen: alleen bij een echte actie, met als "van"-prijs de laagste prijs van de 30 dagen ervoor. Geen permanente "van/voor".
- Prijsverschil met Ella Sleeps (€49,95): niet verstoppen. Leg het uit met feiten (zie facet 11).

---

## 9. Snelheid en techniek

### Beste praktijk
Het grootste beeld boven de vouw snel laden, de rest pas laden als het nodig is. Weinig scripts van apps. Lettertypen beperkt. Meten op echte gebruikers.

### Bewijs
- [regel] Core Web Vitals "goed": LCP maximaal 2,5 s, INP maximaal 200 ms, CLS maximaal 0,1, gemeten op het 75e percentiel per apparaat. https://web.dev/articles/vitals
- [groot onderzoek, samenhang] Google/Deloitte (2019, 37 merken, meer dan 30 miljoen sessies): 0,1 s sneller hing samen met 8,4% meer conversie in retail en 9,1% meer stap van productpagina naar winkelwagen. Geen gecontroleerd experiment. https://web.dev/case-studies/milliseconds-make-millions
- [regel] Shopify: het LCP-beeld nooit lazy-loaden, `fetchpriority="high"` op dat beeld, breedte en hoogte opgeven, scripts van apps uitstellen of verwijderen, tikdoelen minstens 48 x 48 px. https://shopify.dev/docs/themes/best-practices/performance
- [regel] Google: beelden die bij laden in beeld zijn niet lazy-loaden. https://web.dev/articles/browser-level-image-lazy-loading
- [regel] Shopify-CDN levert automatisch WebP of AVIF als de browser dat aankan, via de filters `image_url` en `image_tag`. https://shopify.dev/docs/storefronts/themes/best-practices/performance/use-filter-chains
- [regel] Lettertypen: alleen WOFF2, zo weinig mogelijk families, `font-display: swap` of `optional`, `size-adjust` tegen verspringen. https://web.dev/articles/font-best-practices
- [groot onderzoek, leverancier] Analyse van 1.166 Shopify-winkels: gemiddelde PageSpeed-score 30; scripts van apps zijn de grootste kostenpost. https://hyperspeed.me/blog/why-the-average-pagespeed-score-is-only-30/
- [regel, kritisch] Het web-performancerapport in Shopify gebruikt echte gebruikersdata uit Chromium-browsers en Firefox. Safari (iPhone) zit er dus niet in. https://help.shopify.com/en/manual/online-store/web-performance/overview

### Advies voor Bline
- Eerste galerijbeeld van de gekozen kleur: `loading="eager"` en `fetchpriority="high"`. Alle andere beelden en de andere kleuren: lazy. Bij kleurwissel pas de beelden van die kleur laden.
- Beelden altijd via `image_url`/`image_tag` met `widths` en `sizes`, nooit zelf URL's bouwen.
- Video: nooit automatisch laden. Eerst een stilstaand beeld, pas bij tikken de video laden.
- Lettertype: één familie, twee gewichten, WOFF2. Of een systeemletter.
- Apps: per app nagaan of hij op elke pagina een script laadt. Reviewapp en e-mailapp zijn nodig; pop-up-, timer- en "x mensen kijken"-apps niet.
- Geen fade-in-animatie op het eerste beeld (vertraagt LCP).
- Meten: het Shopify-rapport voor Chrome-gebruikers, plus wekelijks PageSpeed Insights met mobiel profiel. Test zelf op een iPhone via Safari, omdat het rapport iPhones mist.

---

## 10. Mobiele UX

### Beste praktijk
Grote tikdoelen, belangrijke acties binnen bereik, geen pop-ups bij binnenkomst, leesbare tekst, formulieren die het juiste toetsenbord tonen. Cookiebanner volgens de regels.

### Bewijs
- [usability-onderzoek] NN/g: tikdoelen minstens 1 x 1 cm. https://www.nngroup.com/articles/touch-target-size/
- [regel] Shopify: minstens 48 x 48 px. https://shopify.dev/docs/themes/best-practices/performance
- [groot onderzoek] Hoober (2013, ruim 1.300 waarnemingen): 49% gebruikt de telefoon met één hand. Latere metingen: het midden is het makkelijkst en het nauwkeurigst. https://www.uxmatters.com/mt/archives/2013/02/how-do-users-really-hold-mobile-devices.php
- [groot onderzoek] NN/g (enquête onder 452 Amerikanen): de nieuwsbrief-pop-up die de pagina blokkeert is de meest gehate vorm. https://www.nngroup.com/articles/overlay-overload/
- [regel] Google raadt pop-ups die de inhoud afdekken af, omdat ze gebruikers hinderen en de zoekprestaties kunnen schaden. Advies: een kleine banner in plaats van een scherm-vullende laag. Verplichte lagen (zoals een leeftijdscheck) worden erkend; een cookiebanner noemt Google niet apart. https://developers.google.com/search/docs/appearance/avoid-intrusive-interstitials
- [regel] Autoriteit Persoonsgegevens: "weigeren" en "accepteren" op dezelfde laag, even zichtbaar, geen vooraf aangevinkte vakjes. Sinds april 2025 controleert de AP actief; ruim 200 sites kregen een waarschuwing. https://www.autoriteitpersoonsgegevens.nl/actueel/ap-pakt-misleidende-cookiebanners-aan
- [mening, leverancier] Pop-ups converteren gemiddeld een paar procent van de bezoekers naar inschrijving (Wisepops en Omnisend, eigen data). Wat dat netto doet voor de verkoop meten ze niet. https://www.omnisend.com/blog/email-popup-statistics/
- [mening, gangbare praktijk] Invoervelden kleiner dan 16 px laten Safari op iPhone inzoomen. Shopify's checkout regelt dat zelf; let er op in eigen formulieren.

### Advies voor Bline
- Geen pop-up bij binnenkomst. Geen "spin het wiel". Inschrijven voor e-mail in de footer en na aankoop.
- Cookiebanner: de ingebouwde Shopify-banner, met "Weigeren" en "Accepteren" even groot en op de eerste laag. Banner onderaan, niet over de koopknop of de meelopende balk.
- Tikdoelen: kleurbolletjes minstens 44 tot 48 px (eventueel met onzichtbare marge), uitklapblokken over de volle breedte tikbaar.
- Lettergrootte: lopende tekst 16 px, regelafstand ongeveer 1,5, bijna zwart.
- Belangrijke knoppen (kleur, aantal, "In winkelwagen") liggen nu in het midden van het scherm na het beeld. Dat is goed.
- Formulieren (e-mail in de footer): `type="email"`, `autocomplete="email"`, 16 px.

---

## 11. Copy en inhoud

### Beste praktijk
Korte, scanbare, feitelijke tekst. Voordelen eerst, onderbouwd met kenmerken en getallen. Bezwaren beantwoorden in vragen. Sociale bewijskracht alleen als die echt is. Urgentie en schaarste alleen als ze waar zijn.

### Bewijs
- [usability-onderzoek, oud] NN/g (Morkes en Nielsen, 1997): beknopte tekst +58%, scanbare +47%, feitelijke (niet wervende) +27%, alle drie samen +124% gemeten bruikbaarheid. Oud, maar het principe is later vaak bevestigd. https://www.nngroup.com/articles/concise-scannable-and-objective-how-to-write-for-the-web/
- [usability-onderzoek] NN/g: mensen zoeken geen marketingpraat maar een goede beschrijving: wat het is, hoe je het gebruikt, hoe het eruitziet. Onvolledige informatie leidt tot afhaken en verkeerde aankopen. https://www.nngroup.com/articles/ecommerce-product-pages/
- [usability-onderzoek] Vergelijkingstabellen moeten scanbaar zijn: kenmerken op één regel, verschillen opvallend. https://baymard.com/guidelines/2142-scanability-of-comparison-tables
- [regel] ACM: schaarste ("nog 3 op voorraad") en urgentie (aftelklok) alleen als het waar is. Een timer mag niet doorlopen of opnieuw starten als de actie gewoon doorgaat. "Nu bekijken 12 mensen dit" alleen als het precies over dit product en dit moment gaat. Niet steeds "uitverkoop" roepen. ACM Leidraad, p. 23, 24, 62 en 63. https://www.acm.nl/system/files/documents/leidraad-bescherming-online-consument-2024.pdf
- [regel] Een echte besteltijd ("voor 22:00 besteld, vandaag verzonden", zoals Ella Sleeps) is wel toegestaan, mits waar.

### Advies voor Bline
- Kop boven de vouw: de productnaam met ondertitel (zie facet 4). Lager op de pagina koppen met één belofte per blok: "Lekker rechtop lezen in bed", "Je boek of telefoon altijd binnen handbereik", "Hoes eraf, in de was op 30 °C".
- Elk voordeel met een kenmerk erbij: "Steunt je rug en armen" en daaronder "Hoogte 45 cm, armleuningen van 50 cm" (gebruik de echte maten).
- Vergelijking "Bline tegen losse kussens": houden. Maak het een tabel met 4 tot 6 regels: blijft op zijn plek, steun voor armen, vak voor boek, wasbare hoes, prijs per jaar gebruik. Noem Ella Sleeps niet bij naam: vergelijkende reclame mag, maar moet objectief en controleerbaar zijn, en dat is lastig.
- Uitleggen waarom €69,99 en niet €49,95: vulling, maat, hoes los te koop, retourbelofte. Feitelijk, zonder superlatieven.
- Vragen: prijs, verschil tussen kleuren, wassen, maat in bed, voor wie het past, retour, levering, garantie. Elk antwoord 2 tot 3 zinnen.
- Sociale bewijskracht: bol.com-score met bron nu; eigen reviews met foto's zodra ze er zijn. Geen "x mensen kochten dit vandaag" zonder echte data.
- Geen aftelklokken en geen "bijna uitverkocht" tenzij het echt zo is.

---

## 12. E-mail en retentie

### Beste praktijk
Een korte reeks voor verlaten checkout. Een welkomstreeks zonder automatische korting. Na aankoop: verzendinformatie, gebruikstips, reviewverzoek na gebruik, en later de hoes als aanvulling.

### Bewijs
- [groot onderzoek, leverancier] Klaviyo (meer dan 110.000 klanten): verlaten-winkelwagen-mails leveren gemiddeld $6,77 omzet per ontvanger op (top 10%: $13,70); klikratio gemiddeld 6%. https://www.klaviyo.com/blog/abandoned-cart-benchmarks
- [mening, leverancier] Omnisend adviseert 3 mails en de eerste na 30 tot 60 minuten; in hun data over 2025 leidde 1,51% van de afgeleverde verlaten-winkelwagen-mails tot een aankoop. Het vaak geciteerde cijfer "3 mails geven 69% meer orders dan 1" (Omnisend, data 2016 tot 2017) kon ik niet terugvinden op hun huidige pagina's. https://www.omnisend.com/blog/cart-abandonment-emails/
- [mening] Kortingspop-ups: 10% korting scoort in leveranciersdata vaak even goed of beter dan hogere kortingen op inschrijvingen. Over netto winst na korting is geen openbaar onderzoek. https://community.shopify.com/t/raising-the-discount-from-10-to-20-dropped-signup-rates-in-our-client-data/666659
- [regel] Marketingmail vereist toestemming, behalve aan bestaande klanten voor vergelijkbare producten. Of een verlaten-checkout-mail zonder toestemming mag, is niet helemaal duidelijk; vaak wordt "gerechtvaardigd belang" gebruikt, afhankelijk van aantal en timing. https://help.klaviyo.com/hc/nl-nl/articles/360003211651
- [regel] ACM: vraag pas om een review als de klant het product heeft ontvangen en kunnen gebruiken; geen beloning voor positieve reviews. https://www.acm.nl/system/files/documents/leidraad-bescherming-online-consument-2024.pdf

### Advies voor Bline
- Verlaten checkout (Shopify Email of Klaviyo):
  - Mail 1 na ongeveer 1 uur: "Je Bline in Beige ligt nog klaar", beeld van de gekozen kleur, knop terug naar de checkout, de vinkjes (gratis verzending, retour, levering). Geen korting.
  - Mail 2 na ongeveer 24 uur: antwoord op de drie meest gestelde vragen, bol-score met bron, WhatsApp-link.
  - Mail 3 na 48 tot 72 uur: alleen aan mensen met marketingtoestemming. Eventueel een kleine bonus (bijvoorbeeld gratis extra hoes bij 2 kussens), geen procentkorting.
  - Zonder toestemming: alleen mail 1.
- Welkomstkorting: niet standaard. Begin met inschrijven zonder korting ("tips en nieuwe kleuren"). Test later een bonus in natura (hoes) tegen geen bonus, als het verkeer het toelaat.
- Na aankoop: bevestiging met levering en wasinstructies; 7 tot 14 dagen na levering een reviewverzoek met foto-optie; na 6 tot 8 weken een mail over een extra hoes in een andere kleur. Deze termijnen zijn een redelijke inschatting, niet gemeten.
- Inschrijfvakje voor marketing in de checkout: niet vooraf aangevinkt.

---

## 13. SEO en GEO (AI-zoekmachines)

### Beste praktijk
Goede productstructuurdata op de echte productpagina, Merchant Center met verzend- en retourbeleid, eigen reviews, nuttige inhoud die vragen beantwoordt, en vooral vermeldingen op andere sites.

### Bewijs
- [regel] Merchant-listing-structuurdata: verplicht `name`, `image`, `offers` met `price` en `priceCurrency`; aanbevolen `brand`, `gtin`, `availability`, `aggregateRating`, `review`. Verzend- en retourbeleid bij voorkeur op organisatieniveau. https://developers.google.com/search/docs/appearance/structured-data/merchant-listing
- [regel] Review-structuurdata: geen reviews van andere sites samenvoegen; beoordelingen moeten direct van gebruikers komen en zichtbaar zijn op de pagina. https://developers.google.com/search/docs/appearance/structured-data/review-snippet
- [regel] Sinds augustus 2023 toont Google FAQ-uitklappers in de zoekresultaten alleen nog voor bekende overheids- en zorgsites. Bestaande FAQ-structuurdata hoeft niet weg. https://developers.google.com/search/blog/2023/08/howto-faq-changes
- [regel] Google: voor AI Overviews en AI Mode zijn geen extra maatregelen, bestanden of markeringen nodig; de gewone SEO-basis volstaat, plus actuele Merchant Center-gegevens. https://developers.google.com/search/docs/appearance/ai-features
- [regel] Merchant Center: retourbeleid instellen kan labels als "gratis retour" of "30 dagen retour" in Shopping-vermeldingen opleveren. https://support.google.com/merchants/answer/14232691
- [regel] "Top Quality Store"-label kijkt naar levering, retour, snelheid van de site, beeldresolutie en reviews. https://support.google.com/merchants/answer/14261098?hl=en
- [regel] Winkelbeoordelingen van Google vragen genoeg unieke reviews per land in de laatste 12 maanden (Google noemt in de regel 100). https://support.google.com/merchants/answer/190657?hl=en
- [regel] OpenAI: voor Shopify-winkels zijn productgegevens via Shopify Catalog al gekoppeld aan ChatGPT; productresultaten zijn geen advertenties. https://help.openai.com/en/articles/11128490-shopping-with-chatgpt
- [mening] Shopify Agentic Storefronts (Winter '26) zet producten in ChatGPT, Copilot, Perplexity en Google AI Mode. Beschikbaarheid voor NL en BE moet je in de admin nagaan. https://www.ringly.io/blog/agentic-storefront-shopify
- [groot onderzoek, labo] GEO-studie (Princeton en anderen, KDD 2024): tekst met statistieken, citaten en bronvermeldingen werd tot ongeveer 40% vaker zichtbaar in antwoorden van generatieve zoekmachines. Gemeten in een testomgeving, niet in ChatGPT zelf. https://arxiv.org/html/2311.09735v3
- [groot onderzoek, samenhang] Ahrefs (75.000 merken): merkvermeldingen op het web hingen sterker samen met zichtbaarheid in AI-antwoorden (correlatie 0,664) dan backlinks (0,218); YouTube-vermeldingen het sterkst (ongeveer 0,737). Samenhang, geen oorzaak. https://ahrefs.com/blog/ai-brand-visibility-correlations
- [mening, kritisch] Welke bronnen ChatGPT aanhaalt verschuift sterk per update (Reddit-aandeel ging volgens meerdere trackers flink omlaag in 2025). Bouw niet op één kanaal.

### Advies voor Bline
- Product-structuurdata (Dawn doet dit standaard) op `/products/...` laten staan. Controleer met de Rich Results Test: prijs, valuta, beschikbaarheid, merk, en per kleur een variant met eigen beeld.
- Homepage: Organization-structuurdata met logo, contact, retourbeleid. Geen tweede Product-blok, of zorg dat de canonical van de productinhoud naar `/products/...` wijst.
- `aggregateRating` alleen met eigen reviews op de site, nooit met de bol.com-score.
- Merchant Center via de Google & YouTube-app: gratis vermeldingen aan, verzending (gratis, levertijd) en retourbeleid invullen, beelden van minstens 1200 px.
- FAQ: houden op de pagina voor mensen en voor AI. FAQ-structuurdata mag, maar levert geen extra weergave in Google op.
- Blog of gidsen: 3 tot 5 echt nuttige artikelen ("Rechtop lezen in bed zonder rugpijn", "Leeskussen of losse kussens", "Hoe was je een kussenhoes zonder krimp"), met eigen maten en getallen, interne link naar het product. Niet veel dunne artikelen.
- Vermeldingen elders: bol-listing goed houden, reviews op een winkelplatform, een paar YouTube- of TikTok-video's van echte gebruikers, en pers of gidsen in NL en BE. Dit is volgens de beschikbare data de grootste hefboom voor AI-zichtbaarheid, maar het bewijs is samenhang.
- In Shopify nagaan of Agentic Storefronts voor NL beschikbaar is en zo ja aanzetten.

---

## 14. Meten en testen

### Beste praktijk
Eerst een betrouwbare trechter en gedragsdata. Duidelijke fouten direct oplossen zonder test. Alleen grote wijzigingen testen, met een vooraf bepaalde steekproef en hele weken.

### Bewijs
- [mening, CXL] Minstens 250 tot 350 conversies per variant (per segment), test in hele weken en minstens twee bedrijfscycli, steekproef vooraf vastleggen, niet vroeg stoppen. https://cxl.com/blog/ab-testing-statistics/
- [regel] Shopify Rollouts (Markets > Rollouts): A/B-test van thema- en checkoutinstellingen zonder app, standaard 50/50 en maximaal 90 dagen. https://help.shopify.com/en/manual/markets/rollouts
- [regel] Microsoft Clarity (gratis heatmaps en opnames) mag pas laden na toestemming. https://www.consentmo.com/blog-posts/how-to-add-microsoft-clarity-to-your-shopify-store-the-gdpr-compliant-way
- [mening] Gemiddelde conversie verschilt sterk per branche; Shopify noemt voor "home & furniture" 1,29% en mobiel lager dan desktop. Gebruik dit alleen als grove richting. https://www.shopify.com/blog/ecommerce-conversion-rate

**Eigen berekening** (standaardformule voor twee proporties, tweezijdig, 95% betrouwbaarheid, 80% power; controleer met https://www.evanmiller.org/ab-testing/sample-size.html):

| Basisconversie | Verwachte winst (relatief) | Bezoekers per variant | Conversies per variant (ongeveer) |
|---|---|---|---|
| 1% | 20% | 42.693 | 427 |
| 1% | 50% | 7.750 | 77 |
| 2% | 10% | 80.681 | 1.614 |
| 2% | 20% | 21.108 | 422 |
| 2% | 30% | 9.797 | 196 |
| 2% | 50% | 3.825 | 77 |
| 3% | 20% | 13.914 | 417 |

Conclusie: met een paar duizend bezoekers per maand kun je alleen hele grote verschillen meten. Kleine wijzigingen (kleur van een knop, tekst van een vinkje) zijn niet te testen.

### Advies voor Bline
1. **Nu instellen**: Shopify Analytics trechter (sessies, in winkelwagen, checkout bereikt, gekocht) per apparaat en per bron. GA4 met consent mode. Clarity na toestemming.
2. **Wekelijks kijken**: conversie mobiel, percentage dat de kleur wisselt, gebruik van de meelopende balk (via een event), lade naar checkout, checkout naar aankoop, retourpercentage.
3. **Clarity-opnames**: 20 tot 30 mobiele sessies per week bekijken met de vraag: waar twijfelen mensen, wat tikken ze aan dat niet werkt?
4. **Zonder test invoeren** (sterk onderbouwd of wettelijk): vinkje niet vooraf aangevinkt, duimnagels, leverdatum, gratis retour, bedrijfsgegevens, expressknoppen in de lade, LCP-beeld.
5. **Pas testen als er ongeveer 400 aankopen per variant haalbaar zijn binnen 4 tot 8 weken**. Dan eerst de grote vragen via Rollouts: gratis retour plus 30 nachten tegen alleen gratis retour; Klarna aan tegen uit (als Rollouts dat in de checkout toelaat).
6. **Tot die tijd**: voor/na vergelijken over minstens 4 hele weken, en bijhouden wat er verder veranderde (advertenties, seizoen, acties).

---

## Waar het bewijs zwak of tegenstrijdig is

- **Meelopende knop**: tests wijzen beide kanten op; de meeste zijn niet significant of zonder steekproef.
- **Lade tegen pagina**: geen openbare test met steekproef gevonden.
- **Eerste beeld sfeer of product, 4:5 tegen 1:1, video**: vooral meningen en cases van leveranciers.
- **Shop Pay "+50%" en "één pagina +7,5%"**: marketingclaims zonder openbare methode.
- **Achteraf betalen**: één sterk academisch onderzoek (+20% verkoop), maar in NL is Klarna maar 4% van de aankopen. Effect voor Bline onbekend.
- **Keurmerken**: veel herkenning, maar het enige conversiecijfer komt van de keurmerkhouder zelf en is oud.
- **Welkomstkorting**: alleen data over inschrijvingen, niet over winst.
- **GEO**: één labstudie en correlaties; het gedrag van AI-zoekmachines verandert snel.
- **Baymard-cijfers over afhaken** komen vooral uit de VS; NL kan afwijken (bijvoorbeeld minder creditcards, meer iDEAL).

## Bronnenlijst (hoofdbronnen)

- Baymard: https://baymard.com/lists/cart-abandonment-rate, https://baymard.com/product-page/articles, https://baymard.com/blog/always-use-thumbnails-additional-images, https://baymard.com/blog/shipping-speed-vs-delivery-date, https://baymard.com/research-articles/show-shipping-costs-on-product-pages, https://baymard.com/blog/user-ratings-distribution-summary, https://baymard.com/blog/checkout-flow-ux-optimization, https://baymard.com/guidelines/615-how-to-display-promotional-fields, https://baymard.com/blog/live-chat-usability-issues, https://baymard.com/blog/homepage-carousel
- Nielsen Norman Group: https://www.nngroup.com/articles/ecommerce-product-pages/, https://www.nngroup.com/articles/hidden-navigation-methodology/, https://www.nngroup.com/articles/touch-target-size/, https://www.nngroup.com/articles/overlay-overload/, https://www.nngroup.com/articles/sticky-headers/
- Google: https://web.dev/articles/vitals, https://web.dev/case-studies/milliseconds-make-millions, https://developers.google.com/search/docs/appearance/ai-features, https://developers.google.com/search/docs/appearance/structured-data/merchant-listing
- Shopify: https://shopify.dev/docs/themes/best-practices/performance, https://help.shopify.com/manual/payments/accelerated-checkouts, https://help.shopify.com/en/manual/markets/rollouts, https://help.shopify.com/en/manual/online-store/web-performance/overview
- NL en EU: https://www.acm.nl/system/files/documents/leidraad-bescherming-online-consument-2024.pdf, https://www.acm.nl/nl/publicaties/acm-wil-einde-aan-nepkortingen-na-komst-strengere-regels, https://www.autoriteitpersoonsgegevens.nl/actueel/ap-pakt-misleidende-cookiebanners-aan, https://www.betaalvereniging.nl/wp-content/uploads/2026/06/TMM-Q1-2026-NL.pdf, https://www.consumentenbond.nl/online-kopen/keurmerken-webwinkels, https://ondernemersplein.overheid.nl/regels-voor-bedrijfscorrespondentie/
- Onderzoek: https://spiegel.medill.northwestern.edu/how-online-reviews-influence-sales/, https://ideas.repec.org/p/nbr/nberwo/33152.html, https://news.utdallas.edu/?p=11491, https://arxiv.org/html/2311.09735v3, https://cxl.com/blog/ab-testing-statistics/
