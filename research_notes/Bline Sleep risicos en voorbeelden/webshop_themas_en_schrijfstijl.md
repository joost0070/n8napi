# Webshop-thema's en schrijfstijl voor Bline Sleep

Onderzoeksdatum: 4 oktober 2026. Methode: alleen publieke storefront-pagina's (homepage, een productpagina, verzend- en retourpagina) opgehaald met curl en een browser-user-agent, plus publieke documentatie (Shopify Theme Store, themaleveranciers, ACM, bol Partnerplatform, DHL). Geen API-tokens of omgevingsvariabelen gebruikt.

Labels: **[FEIT]** = letterlijk gezien in bron of HTML. **[INFERENTIE]** = mijn interpretatie of afleiding. **[NIET GEVONDEN]** = gezocht, niet publiek te vinden.

Let op: prijzen in de HTML van Tofvel en Jan Jansen stonden in USD, omdat de server ons als bezoeker uit de VS zag (proxy). Dat zegt niets over de Nederlandse ervaring.

---

## 0. De belangrijkste vondst vooraf

**[FEIT]** Bijna alle onderzochte shops zijn van één partij. Hooijer Group (familiebedrijf uit Oldenzaal, Hanzepoort 26) noemt op zijn site als merken: Crocs, Georgia Boot, HEYDUDE, Hunter, Jan Jansen, KEEN, Lazamani, GEOX, Piedi Nudi, Sockwell, Tofvel en Toni Pons; eigen merken zijn Piedi Nudi, Tofvel, Jan Jansen en Lazamani. De HEYDUDE-footer zegt: "Deze website is onafhankelijk eigendom van en wordt beheerd door Bartogi B.V., een geautoriseerde distributeur van Crocs Europe B.V." Bron: https://hooijerfootwear.com/ , https://heydude.nl/

**[INFERENTIE]** Je kijkt dus niet naar elf losse merken met elk een eigen aanpak, maar naar één e-commerceteam met één techniekstapel (Trusted Shops, Gorgias, ProfitMetrics, Hello Retail, DHL, Re:turnista) en één basis-thema ("Hooijer", afgeleid van Dawn). Dat verklaart waarom verzendteksten woord voor woord gelijk zijn. Voor Bline is dat nuttig: het laat zien wat een professioneel team als minimum neerzet, en waar ook zij generiek worden.

---

## 1. Domeinen en thema's

| Shop | Publiek domein (geverifieerd) | `Shopify.theme` uit de HTML | theme_store_id | Oordeel |
|---|---|---|---|---|
| Bartogi | bartogi.nl (Cloudflare-check blokkeerde curl), bartogi.de | `"name":"Hooijer 1.9.4 SS'26 + HelloRetail","schema_name":"Hooijer","schema_version":"1.9.0"` (bartogi.de) | null | Maatwerk, Dawn-basis |
| Lazamani | lazamani.nl | `"name":"Copy of Lazamani Copy","schema_name":"Hooijer"` | null | Maatwerk (Hooijer) |
| Tofvel | tofvel.com (tofvel.nl stuurt door) | `"name":"Tofvel 2.3.0","schema_name":"Tofvel"` | null | Maatwerk, Dawn-basis |
| Sockwell NL | sockwell.nl | `"name":"Hooijer 1.9.5 Herfst 2026","schema_name":"Hooijer"` | null | Maatwerk (Hooijer) |
| HEYDUDE NL | heydude.nl | `"name":"HEYDUDE (Hooijer Footwear 1.12.3) FW26","schema_name":"Hooijer","schema_version":"1.12.3"` | null | Maatwerk (Hooijer) |
| Hunter Boots NL | hunterboots.nl | `"name":"Copy of SS'26","schema_name":"Quickfire","schema_version":"1.0.0"` | null | Volledig maatwerk, geen Dawn-bestanden |
| Jan Jansen | nl.janjansen.com (janjansen.nl gaf een SSL-fout) | `"name":"Copy of Lost in Paris & TRCE","schema_name":"Jan Jansen","schema_version":"1.4.0"` | **887** | 887 = Dawn (gratis Shopify-thema), hernoemd en aangepast |
| KEEN NL | keenfootwear.nl | `"name":"SS'26","schema_name":"Keen","schema_version":"1.0.2"` | null | Dawn-kloon (Dawn-secties: image_banner, multicolumn, collage, image_with_text) |
| Piedi Nudi | piedinudi.com (piedinudi.nl stuurt door) | `"name":"Soleway (gekocht)","schema_name":"Local","schema_version":"3.2.1"` | **1651** | 1651 = **Local** van Krown Themes, preset "Soleway". Enige gekochte Theme Store-thema in de set |
| Toni Pons NL | tonipons.nl | `"name":"SS'26","schema_name":"Footwear"` | null | Maatwerk, Dawn-basis |
| Geox NL | geox.com/nl-NL | Geen Shopify. HTML bevat `on/demandware.static` en `Sites-xcom-uk-Site` | n.v.t. | Salesforce Commerce Cloud (wereldwijde Geox-site) |

Mapping theme_store_id: 887 = Dawn, 1651 = Local, 1190 = Impact, 855 = Prestige, 1356 = **Sense** (dus niet Impact). Bron: https://platmart.io/blog/shopify-theme-ids/ ; Local als Krown-thema met preset Soleway: https://themes.shopify.com/themes/local/presets/local

**[FEIT]** Tofvel, Toni Pons, Jan Jansen, KEEN en alle Hooijer-shops laden Dawn-bestandsnamen (`component-cart-drawer.css`, `cart-drawer.js`, `cart-notification.js`, `collapsible.js`). Hunter laadt alleen eigen `.min`-bestanden met "v2-"-secties.

**[INFERENTIE]** "Quickfire" is waarschijnlijk de naam van het bureau achter het wereldwijde Hunter-thema (er bestaat een Shopify-bureau Quickfire Digital); niet bevestigd.

**[FEIT, losse fouten]** Op Sockwell en Bartogi.de staat zichtbaar "Translation missing: nl.sections.footer.carrier_options"; op Jan Jansen "Translation missing: nl.accessibility.toggle_search_modal" en "Translation missing: nl.layout.footer.payment_methods". Les: een Dawn-fork die niet wordt bijgehouden lekt vertaalsleutels.

---

## 2. Opbouw per shop

### 2.1 Hooijer-thema (Bartogi, Lazamani, Sockwell, HEYDUDE)

Aankondigingsbalk **[FEIT]**:
- Sockwell: "Gratis verzending vanaf €60 / Uitstekend beoordeeld / Premium kwaliteit"
- Lazamani: "Gratis verzending / Vandaag besteld, binnen 1-2 werkdagen thuis!"
- Bartogi.nl (via WebFetch): "Gratis verzending vanaf € 75 / Uitstekend beoordeeld"
- Bartogi.de: "Kostenloser Versand ab 75 € / Lieferzeit: ca. 1-3 Arbeitstage"
- HEYDUDE: "Gratis verzending vanaf €75" (in een marquee-sectie)

Header: taalwissel (NL/DE/EN), zoeken, account, favorieten (wishlist-app), mandje. Megamenu met veel subcategorieën; Sockwell heeft een menu dat vooral op gebruik en klacht is ingedeeld (Vliegtuigsokken, Diabetessokken, Hielspoorsokken).

Homepagevolgorde **[FEIT, uit de section-id's]**:
- Sockwell: hero, productslider (Dames/Heren/Wandelsokken), uitgelichte collecties, "trustbuttons" (drie USP-blokjes), Trusted Shops bedrijfsreviews, tekst met beeld, uitklapbare SEO-tekst, blogslider, nieuwsbrief.
- Lazamani: slideshow ("winter '26"), Hello Retail "recent bekeken", collectietegels (TREND: FRANJES, HOGE LAARZEN, INSTAPPERS), tekstblok, Hello Retail nieuw binnen, Instagram ("Hey you, Let's get social!"), merktekst, blogslider, nieuwsbrief met 10% welkomstvoucher.
- Bartogi.de: hero, Hello Retail retargeting, "Spotted", nieuw binnen, twee beelden met tekst, Trusted Shops reviews, SEO-tekst, nieuwsbrief.
- HEYDUDE: hero, marquee, collecties, slider, tweede hero, slider, productweergave, kolommen, blog, "images with video thumbnail", nieuwsbrief, logobalk.

Productpagina **[FEIT]**:
- Galerij: Swiper-slider met zoom; kleuren als aparte producten met kleurbolletjes ("Kleur/Print:").
- Titel, korte ondertitel (Lazamani: "Zwarte leren teensandalen"), prijs met kortingspercentage.
- Maatknoppen. Sockwell nummert de stappen: "Stap 1: Kies je maat" en "Stap 2: Kies het aantal en voeg het toe aan je winkelwagen". Duidelijk en menselijk.
- Onder de knop: leveringsregel. Lazamani: "Gratis verzending / Vandaag besteld, binnen 1-2 werkdagen thuis / Trusted Shops kopersbescherming tot € 100". Sockwell en HEYDUDE tonen in plaats daarvan USP-iconen (HEYDUDE in het Engels: "Easy-on, Lightweight, Comfortable, Travel shoe, Breathable").
- "Beschrijving" (één alinea), daarna "Kenmerken" als specificatielijst (materiaal, pasvorm, hakhoogte, artikelnummer). Dit is in feite de spec-tabel.
- "Wat anderen zeggen" (reviewsectie), "Anderen bekeken ook" / "Misschien vind je dit ook leuk".
- Sticky add-to-cart: **[NIET GEVONDEN]** in de server-HTML; alleen een sticky header.

Winkelwagen: drawer met melding "Artikel toegevoegd aan jouw winkelwagen", "Subtotaal (incl. BTW)", "Verzendkosten berekend in checkout". Lazamani toont "Gratis verzending" in de drawer. Geen voortgangsbalk naar gratis verzending gevonden.

Vertrouwen: Trusted Shops-app op alle Hooijer-shops (script `tseish-app.connect.trustedshops.com`), "Uitstekend beoordeeld" in de balk, Trusted Shops kopersbescherming op de productpagina. Betaaliconen in de footer (bestandsnamen): iDEAL, Bancontact, PayPal, Visa, Mastercard, Maestro, Apple Pay, Google Pay, Shop Pay. **Geen Klarna, Riverty of in3** op enige onderzochte shop.

### 2.2 Tofvel (tofvel.com)
- Balk: "Premium pantoffels | Gratis verzending vanaf €75 | Uitstekend beoordeeld".
- Productpagina: knop "Bestel nu!", direct daaronder vijf regels met vinkjes: "Gratis verzending vanaf €75 / 100% natuurlijke wolvilt / Voorkomt zweetvoeten & geurtjes / Antibacterieel & zelfreinigend / Our Planet-keurmerk". Beschrijving met vetgedrukte kernwoorden, dan "Kenmerken", dan een video-sectie "Onze makers" (enige productpagina in de set met eigen video, `<video>` in de HTML).
- Trusted Shops, Gorgias-chat.

### 2.3 Hunter Boots NL
- Volledig eigen thema. Zijcart met "Vaak samen gekocht" (Rubber Boot Care Kit €35,00, Waterproof Spray €15,00) en een voortgangsbalk in de cart-HTML.
- Homepage: drie grote hero-sliders afgewisseld met productsliders (campagne 170 jaar met Kate Moss, GANNI x Hunter).
- Productpagina: Swiper met lightbox, "Maat/Pasvorm Samenvatting: Valt normaal, normale pasvorm", een laarzenkeuzehulp in het Engels ("What will they be used for?"), "Specificaties" (deels Engels: "Lining material") en "Kenmerken".
- Verzending: "€ 3,95; vanaf een orderbedrag van € 100,00 verzenden wij gratis." Reviews.io-verwijzing en Trusted Shops-script.

### 2.4 Jan Jansen
- Dawn (887). Productpagina: "Wat is mijn maat? Bekijk maattabel", "Bestel nu!", "Add to Wishlist" (Engels), "Gratis verzending / Vandaag besteld, binnen 1-2 werkdagen thuis". Kenmerken half Engels ("Upper", "Lining", "Heel Height").
- Geen reviewplatform gevonden.

### 2.5 KEEN NL
- Dawn-kloon. Balk: "Gratis verzending vanaf €125 | Originele stijlen". Galerij met 16 media en thumbnails, maat plus breedte ("WIDTH: Regular"), "Bestel nu", kenmerkenlijst als bullets.
- Sterke contentsectie (blog over likdoorns, stinkende schoenen, pasvorm) en een serviceregel: "Wij zijn hier om je te helpen de juiste pasvorm te vinden en je vragen te beantwoorden. Van maandag t/m vrijdag, via e-mail of telefoon."
- Betaaliconen (Shopify-standaard SVG): iDEAL | Wero, Bancontact, Apple Pay, Google Pay, Maestro, Mastercard, PayPal, Shop Pay, UnionPay, Visa.

### 2.6 Piedi Nudi (Local, preset Soleway)
- Balk: "Gratis verzending binnen NL". Galerij met thumbnails en zoom, ondertitel "Leren enkellaarsjes met comfortabele pasvorm", "Prijs: €225,00", "Toevoegen aan winkelmand". Popups: exit-intent en winkelkiezer.
- Betaaliconen: iDEAL | Wero, Bancontact, Apple Pay, Google Pay, Maestro, Mastercard, PayPal, Shop Pay, Visa. Trusted Shops-script.

### 2.7 Toni Pons NL
- Balk: "Gratis verzending". Onder de knop drie USP's: "Gratis verzending / Levertijd 1-2 werkdagen / Spaans vakmanschap". Homepage met een citaatblok ("biography"-sectie). Geen reviewplatform gevonden.

### 2.8 Geox NL
- Salesforce Commerce Cloud. "GRATIS STANDAARDLEVERING VOOR BESTELLINGEN BOVEN € 89,00", anders € 8,90; "tot 30 dagen ... kosteloos te retourneren" via UPS. Mengt u en je ("trek uw schoenen aan" naast "Schrijf je in voor de nieuwsbrief").

---

## 3. Verzend- en servicebeloftes (letterlijk)

| Shop | Op de site (balk of productpagina) | Op de verzendpagina |
|---|---|---|
| Lazamani | "Vandaag besteld, binnen 1-2 werkdagen thuis!" | "Wanneer je op werkdagen vóór 12.00 uur bestelt, streven wij ernaar om jouw bestelling nog dezelfde dag te verzenden." ... "Er kunnen geen rechten worden ontleend aan deze bezorgtermijn." DHL. |
| Hunter, Tofvel, KEEN | (geen tijd in de balk) | Zelfde tekst: vóór 12.00 uur, "streven wij ernaar", DHL. |
| Piedi Nudi | "Gratis verzending binnen NL" | "Bestel je op een werkdag vóór 12.00 uur? Dan doen we ons best om je bestelling nog dezelfde dag te verzenden." |
| Jan Jansen | "Vandaag besteld, binnen 1-2 werkdagen thuis" | (pagina leeg in HTML) |
| Toni Pons | "Levertijd 1-2 werkdagen" | (niet gevonden) |
| Bartogi.de | "Lieferzeit: ca. 1-3 Arbeitstage" | |
| Geox | "GRATIS STANDAARDLEVERING ... BOVEN € 89,00" | "De levertijd wordt berekend vanaf het moment dat de bestelling aan de koerier wordt overhandigd." |

Retour **[FEIT]**: Lazamani: 14 dagen bedenktijd, verwerking via Re:turnista, "de verzendkosten van de retourzending voor jouw eigen rekening". Hunter, KEEN, Tofvel, Piedi Nudi: retour voor eigen rekening. Alleen Geox biedt gratis retour (30 dagen, UPS). Niemand belooft "gratis retour" in de balk.

**[INFERENTIE]** Een groot schoenenbedrijf met een eigen magazijn houdt als interne cut-off **12:00** aan, met "streven" en "geen rechten". In de balk staat echter het ruimere "Vandaag besteld, binnen 1-2 werkdagen thuis". Dat verschil (balk belooft meer dan de voorwaarden) is precies wat Bline moet vermijden.

Bronnen: https://lazamani.nl/pages/verzending , https://lazamani.nl/pages/ruilen-of-retourneren , https://hunterboots.nl/pages/verzending , https://keenfootwear.nl/pages/verzending , https://www.tofvel.com/pages/verzending , https://www.piedinudi.com/pages/verzending , https://www.geox.com/nl-NL/

---

## 4. Schrijfstijl per shop

| Shop | Aanspreekvorm | Zinslengte | Humor | Specifiek? | Oordeel |
|---|---|---|---|---|---|
| HEYDUDE | je | kort tot middel | ja, droog | middel | Het menselijkste van de set |
| KEEN | je | wisselend | ja (bijnamen) | hoog in blog, laag in productteksten | Blog top, productteksten vertaald en generiek |
| Tofvel | je | lang | licht | hoog (Nepal, maker, schuur) | Warm, wat langdradig, één gezondheidsachtige claim |
| Piedi Nudi | je | middel | nee, wel warm | hoog (H- en K-wijdte) | Beste servicetoon |
| Lazamani | je | middel | licht ("Hey you") | hoog in productteksten | Goede productteksten, merktekst generiek |
| Sockwell | je | lang | nee | middel | Gezondheidsclaims, "Dé perfecte sokken" |
| Jan Jansen | je | lang | nee | laag | Meest "AI-achtig" (zie hieronder) |
| Toni Pons | je | middel | nee | middel | Vakantieclichés |
| Hunter | je | middel | nee | middel | Vertaald, veel Engels |
| Geox | u en je door elkaar | lang | nee | laag | Vertaald, inconsistent |

### Voorbeelden die menselijk en goed zijn [FEIT, letterlijk]
1. HEYDUDE: "Instappers die zó comfortabel zijn, dat het waarschijnlijk niet bij een eerste paar blijft. De stijl, het lichte gewicht en aantrekgemak, fijn draagcomfort... je bent gewaarschuwd."
2. KEEN (blog): "Je bent lekker onderweg en dan begint dat ene plekje op je teen steeds meer aandacht te vragen. Eerst een beetje irritant, een paar kilometer later behoorlijk pijnlijk."
3. Tofvel: "Ideaal om even mee naar de schuur of afvalcontainer te lopen." en "De sloffen zijn verkrijgbaar in verschillende kleuren, zodat ieder gezinslid een eigen kleur kan kiezen."
4. Piedi Nudi (verzendpagina): "Je nieuwe Piedi Nudi's besteld? Dan wil je ze natuurlijk het liefst zo snel mogelijk in huis hebben." en "Ben je niet thuis? Geen zorgen."
5. Lazamani (product): "Een loopzool van rubber zorgt voor grip en stabiliteit en is uitgevoerd met een klein hakje van een centimeter hoog." en de kop "Deze schoenen wil je aan je voeten".
6. Toni Pons: "Je kunt deze sneakers het hele jaar door dragen, van werkdag tot weekendje weg."
7. KEEN: "Bekijk 14 praktische tips van 'KEENesioloog' Kenny" en "Van maandag t/m vrijdag, via e-mail of telefoon."

Waarom deze werken **[INFERENTIE]**: ze beginnen bij een herkenbaar moment (de schuur, die ene plek op je teen), noemen een getal of detail (een centimeter, 14 tips, wijdte H), of geven toe dat iets een beetje overdreven is ("je bent gewaarschuwd").

### Voorbeelden die generiek of AI-achtig voelen [FEIT, letterlijk]
- Jan Jansen: "Stap in de wereld van gedurfde elegantie" ... "Ze zijn een toonbeeld van mode en gedurfde elegantie, waarmee je een onuitwisbare indruk achterlaat bij elke gelegenheid."
- KEEN (product): "ontworpen voor ultiem comfort en prestaties" ... "perfect voor iedereen met een actieve levensstijl."
- Lazamani (merktekst): "Onze schoenen ... bieden niet alleen comfort, maar ook een gevoel van luxe." en "Kies Lazamani voor een statement van stijl en kwaliteit."
- Toni Pons: "elke stap voelt als vakantie" en "Of je nu kiest voor een klassieke sleehak, een comfortabele platte espadrille of een speelse variant met bandjes".
- Sockwell: "Dé perfecte sokken voor thuis, op het werk en elke (sport)activiteit." en de USP "Verbetert de bloedcirculatie en geeft ondersteuning".
- Hunter: "Maak kennis met de nieuwste toevoeging aan de Hunter-familie" en de paginatitel "Ontdek Hunter Boots".
- Geox: "Ervaar de nieuwe technologie Fast In System".

Patronen om te herkennen: "stap in de wereld van", "ontdek/ervaar", "niet alleen ... maar ook", "of je nu ... of ...", "perfect voor iedereen", "ultiem", "toonbeeld", drie bijvoeglijke naamwoorden op een rij, zinnen die op elk merk passen, gezondheidsbeloftes.

---

## 5. Reviewplatforms

| Shop | Platform [FEIT tenzij anders] |
|---|---|
| Bartogi, Lazamani, Sockwell, HEYDUDE, Tofvel, Hunter, Piedi Nudi | Trusted Shops (app-script `tseish-app.connect.trustedshops.com`; Sockwell en Bartogi hebben een sectie "trusted_shops_company_reviews"; Lazamani toont "Trusted Shops kopersbescherming tot € 100") |
| Hunter | ook reviews.io-verwijzingen in de HTML |
| KEEN, Jan Jansen, Toni Pons | geen reviewwidget gevonden |
| Geox | niet onderzocht (andere stack) |

Geen Kiyoh, Trustpilot, Judge.me of WebwinkelKeur gevonden. Let op: elke Shopify-pagina noemt Loox, Okendo en Yotpo in een standaard Shopify-script (overal precies 7/17/7 keer); dat zijn geen geïnstalleerde apps.

Overige stack **[FEIT]**: Gorgias (chat), ProfitMetrics (winstgebaseerde tracking), Klaviyo (Lazamani, Bartogi, Jan Jansen), Hello Retail (aanbevelingen), Getsitecontrol (popups).

---

## 6. (a) Thema-advies voor Bline Sleep

Eisen: één heldenproduct, 5 kleuren, veel sfeerbeelden plus witte packshots, één video, specificatietabel, sticky add-to-cart, leverdatumregel, later uitbreiding naar dekbedden, lyocell beddengoed en zijden kussenslopen.

### Rangschikking

**1. Prestige (Maestrooo), $400 eenmalig**
- **[FEIT]** 91% positief uit 869 reviews; presets Prestige, Couture, Vogue, Strass, Signature; kenmerken: sticky cart, slide-out cart, color swatches, product videos, product tabs, image zoom, image rollover, lookbooks, stock counter, size chart, usage information, EU-vertalingen. Bron: https://themes.shopify.com/themes/prestige/presets/allure
- **[FEIT]** Sticky add-to-cart staat standaard aan in Prestige, Impact en Focal ("Show sticky add to cart"). Bron: https://support.maestrooo.com/article/806-sticky-add-to-cart
- **[INFERENTIE]** Rustig, redactioneel, veel witruimte. Past bij een premium leeskussen en bij latere dons en zijde. Grote sfeerbeelden komen het best tot hun recht. Minder "schreeuwerig" dan Impact, dus beter bij een warme, menselijke toon.

**2. Impact (Maestrooo), $400 eenmalig**
- **[FEIT]** 85% positief uit 200 reviews; versie 7.2.0 van 6 juli 2026; presets Impact, Cocoon, Balance; sticky cart, color swatches, product videos, product tabs, before/after slider, image hotspot, trust badges, shipping/delivery information, size chart. Bron: https://themes.shopify.com/themes/impact/presets/impact
- **[INFERENTIE]** Sterk voor één heldenproduct met veel conversieblokken (iconen met tekst, vergelijkingen, video). Grafisch zwaarder; je moet bewust temperen om niet op een dropshipshop te lijken.

**3. Sleek (FoxEcom), $350 eenmalig**
- **[FEIT]** 100% positief uit 616 reviews; presets Sleek, Wildpeak, Jumped, Modiva, Glint; aparte "Sticky add to cart bar" die verschijnt zodra de hoofdknop uit beeld is; productblokken o.a. variant picker, icon with text, collapsible row, inventory status, shipping information, custom liquid. Het verzendblok toont een tekst plus aantal dagen, maar rekent geen datum uit en kent geen cut-off. Bronnen: https://themes.shopify.com/themes/sleek/presets/sleek , https://docs.foxecom.com/sleek-theme/collections-and-products/product-page/sticky-add-to-cart-bar , https://docs.foxecom.com/sleek-theme/collections-and-products/product-page/product-information
- **[INFERENTIE]** Goedkoopste serieuze optie, beste reviewscore. Gericht op beauty, dus iets "glanzender" van uitstraling.

Alternatieven die afvielen:
- **Local (Krown Themes), $380**: 98% positief (96 reviews), wordt gebruikt door Piedi Nudi, heeft sticky cart, swatches, video, tabs, shipping/delivery information. Prima, maar meer gericht op winkels en assortimenten dan op één heldenproduct. https://themes.shopify.com/themes/local/presets/local
- **Be Yours (RoarTheme), $350**: 98% positief (692 reviews), sterk voor beauty. https://themes.shopify.com/themes/be-yours/presets/be-yours
- **Horizon (Shopify), gratis**: 35% positief (208 reviews); sticky add-to-cart staat niet in de lijst. Alleen als budget echt nul is. https://themes.shopify.com/themes/horizon/presets/horizon
- **Een Dawn-fork zoals Hooijer**: werkt voor een team met developers, niet voor een kleine start. De vertaalfouten hierboven laten zien wat er gebeurt als niemand het bijhoudt.

### Licentie
- **[FEIT]** "A theme license can only be used on one single store." en "If you create two distinct Shopify stores for each market, then you must purchase two licenses." Een met wachtwoord beveiligde development store zonder echte betalingen mag het thema gratis gebruiken. Overzetten kan alleen als de oude winkel helemaal sluit. Bron: https://support.maestrooo.com/article/687-theme-licensing-and-transfers ; FoxEcom vergelijkbaar: https://docs.foxecom.com/sleek-theme/getting-started/theme-license-and-transfer
- **[FEIT]** Eenmalige betaling, levenslange licentie voor die winkel, inclusief updates (Impact-pagina).
- Advies: koop een **eigen** licentie op de Bline-winkel. Gebruik geen thema dat via iemand anders, een "nulled" download of een andere winkel is verkregen. Probeer eerst gratis in de theme editor (de Theme Store biedt "Try theme").

### Inrichting met jullie beeldmateriaal [INFERENTIE]
- Collectiekaart: witte packshot als eerste beeld, sfeerbeeld als tweede (image rollover zit in alle drie).
- Productpagina: één product met 5 kleurvarianten (niet 5 losse producten zoals Hooijer), swatches gekoppeld aan een kleur-metafield. Beeldvolgorde per kleur: sfeer, packshot voor, packshot zij (boekenvak), detail hoes, schaalfoto met persoon. Controleer in de demo of het thema bij kleurkeuze alleen de beelden van die kleur toont; dat is per thema verschillend en niet geverifieerd.
- Video: in de galerij als tweede of derde item, en nog een keer als losse sectie verderop (zoals Tofvel "Onze makers").
- Specificatietabel: collapsible rows of tabs gevuld met metafields: afmetingen in cm, gewicht, vulling, hoesstof, wasvoorschrift, wat er in de doos zit.
- Leverdatum: zie hoofdstuk 8. Bouw dit als klein custom-Liquid- of app-blok dat werkdagen en de echte cut-off van eFreight kent. Geen van de drie thema's rekent dit zelf uit.
- Betaalmethoden: iDEAL | Wero, Bancontact, Apple Pay, PayPal, kaarten zijn voldoende; geen enkele vergelijkbare shop biedt Klarna.

---

## 7. (b) Schrijfstijlgids Bline Sleep

Doel: klinkt als een Nederlander die het kussen zelf gebruikt en er trots op is. Niet als een vertaling, niet als een advertentiemachine.

**1. Je, altijd en overal.**
Doe: "Je hoes kan op 30 graden in de wasmachine."
Niet: "Uw hoes is wasbaar." en zeker niet je en u door elkaar (Geox doet dat).

**2. Begin bij een moment, niet bij het product.**
Doe: "Zondagochtend, koffie erbij, boek open. En dan zakt je kussen weer achter je rug weg."
Niet: "Ontdek het ultieme leescomfort met ons premium leeskussen."

**3. Noem een getal of detail in plaats van een bijvoeglijk naamwoord.**
Doe: "De rugleuning is [xx] cm hoog. Hoog genoeg voor je schouders, laag genoeg om over het hoofdeinde te kijken."
Niet: "Een perfect ergonomisch ontwerp voor optimaal comfort."
Voorbeeld uit de praktijk: Lazamani's "klein hakje van een centimeter hoog".

**4. Deze woorden en wendingen schrappen we.**
ontdek, ervaar, til ... naar een hoger niveau, stap in de wereld van, ultiem, perfect, optimaal, naadloos, moeiteloos, tijdloos, essentieel, onmisbaar, toonbeeld, een must-have, dé ..., "niet alleen ... maar ook", "of je nu ... of ...", "Kortom,", "Welkom bij".
Toets: zou de zin ook op de site van een ander merk kunnen staan? Dan eruit. "Kies Lazamani voor een statement van stijl en kwaliteit" past op elk merk.

**5. Geen rijtjes van drie.**
Doe: "Zacht aan de voorkant. Stevig waar je rug leunt."
Niet: "Zacht, stevig en stijlvol."
Twee is genoeg. Of één, met een reden erbij.

**6. Korte zinnen, wisselend ritme.**
Richtlijn: gemiddeld 8 tot 14 woorden. Af en toe een zin van drie woorden. Een productbeschrijving is hooguit 80 tot 120 woorden; de rest gaat in de specificatietabel.

**7. Geen gedachtestreepjes.**
Gebruik een punt, komma of dubbele punt. Doe: "Het boekenvak zit opzij: telefoon, bril, boek." Niet: een zin met een lang streepje in het midden.

**8. Humor mag, klein en droog.**
Doe: "Hij past niet in je handbagage. Wel achter je rug." of "Waarschuwing: je partner gaat hem ook willen." (HEYDUDE doet dit met "je bent gewaarschuwd".)
Niet: woordgrappen in elke kop, of uitroeptekens om enthousiasme te faken.

**9. Geen gezondheidsclaims.**
Niet: "tegen nekpijn", "voorkomt rugklachten", "ergonomisch verantwoord", "aanbevolen door fysiotherapeuten" (tenzij aantoonbaar waar en dan nog voorzichtig), "verbetert je nachtrust".
Doe: beschrijf wat je voelt en ziet: "Je zit rechtop zonder steeds je kussens op te schudden." "Je hoeft niet meer met drie losse kussens te bouwen."
Waarom: onder de Europese MDR bepaalt het "beoogde doel" uit label, advertentie en verkoopmateriaal of iets een medisch hulpmiddel is (art. 2 lid 12). Een medische claim maakt van een kussen juridisch een ander product, met andere plichten. Bronnen: https://qualitybs.wordpress.com/2021/08/03/het-beoogde-doel-en-de-indicatie-voor-gebruik-van-medische-hulpmiddelen/ , https://www.igj.nl/zorgsectoren/medische-technologie/toezicht-op-producten/verkoop-en-distributie-van-medische-hulpmiddelen . Sockwell ("Verbetert de bloedcirculatie") verkoopt compressiekousen met klasse-indeling; dat is een andere productcategorie, niet kopiëren.

**10. Superlatieven alleen als je ze kunt bewijzen.**
Niet: "het beste leeskussen van Nederland", "Dé perfecte ...", "Uitstekend beoordeeld" zonder zichtbare score.
Doe: "4,8 uit 5 bij 213 reviews op bol" (alleen met echt getal en bron), of gewoon niets.

**11. Eerlijke beloftes, ook in de balk.**
De aankondigingsbalk mag nooit meer beloven dan de verzendpagina (zie Lazamani in hoofdstuk 3). Geen nep-aftelklokken of "nog maar 2 op voorraad" als dat niet klopt (ACM).

**12. Nederlandse woorden, Engels alleen als het echt gangbaar is.**
Doe: leeskussen, hoes, boekenvak, rugleuning, wasvoorschrift.
Niet: "reading pillow", "Easy-on", "Lightweight" (HEYDUDE), "Add to Wishlist" (Jan Jansen), "Lining material" (Hunter).

**13. Praat als maker, met "we".**
Doe: "We hebben de hoes eerst in ribstof gemaakt. Mooi, maar hij pakte haar van de kat. Daarom is het nu [stof]." (Alleen als het waar is.)
Tofvel laat zien hoe dat werkt: "Elk paar Tofvel wordt voorzien van een unieke handtekening van de maker."

**14. Servicepagina's in de Piedi Nudi-toon.**
Doe: "Niet thuis? Geen zorgen. Via de track & trace kies je een ander moment of een afhaalpunt."
Niet: "Er kunnen geen rechten worden ontleend aan deze bezorgtermijn." als eerste wat de klant leest. (Juridisch voorbehoud mag, maar onderaan en in gewone taal.)

**15. Lees hardop en schrap.**
Lees elke tekst hardop. Struikel je, of zou je dit nooit tegen een vriend zeggen? Herschrijven. Schrap daarna nog 20%.

### Voorbeeldteksten in deze stijl [INFERENTIE, concept]
- Kop homepage: "Lezen in bed, zonder kussenfort."
- Ondertitel: "Een leeskussen met rugleuning, armsteunen en een vak voor je boek. In vijf kleuren."
- Productintro: "Je kent het. Twee kussens achter je rug, eentje onder je arm, en na tien minuten lig je weer half. Dit kussen blijft staan. De hoes rits je eraf en gaat in de was. Opzij zit een vak voor je boek, je bril of je telefoon."
- USP-regels onder de knop: "Hoes afneembaar en wasbaar op [xx] graden" / "Boekenvak aan de zijkant" / "Op werkdagen voor [cut-off] besteld, morgen in huis" (zie hoofdstuk 8).
- Kleurkeuze: "Twijfel je over de kleur? Op de foto's zie je elke kleur bij daglicht, op een gewoon bed."

---

## 8. (c) "Op werkdagen voor 23:59 besteld, vandaag verzonden": klopt dat?

### Wat eFreight publiek zegt
- **[FEIT]** E-Freight Forwarding, Lindeboomseweg 57, 3825 AL Amersfoort. De e-commercepagina belooft "kosteneffectieve, veilige en snelle verzendoplossingen" en "Binnen 24 uur antwoord op jouw offerteaanvraag". Openingstijden kantoor: maandag tot en met vrijdag 9:00 tot 17:00, zaterdag en zondag gesloten. Bronnen: https://www.efreightforwarding.com/e-commerce , https://www.efreightforwarding.com/warehousing
- **[FEIT]** Uitbreiding met circa 20.000 m2 aan de Vanadiumweg in Amersfoort (september 2026). Bron: https://www.nt.nl/logistiek/2026/09/23/e-freight-forwarding-huurt-20-000-m%C2%B2-logistieke-ruimte-in-amersfoort/
- **[NIET GEVONDEN]** Geen cut-off-tijd, geen ophaaltijden van PostNL of DHL, geen avond- of weekendploeg. Het domein efreight.nl reageerde niet; de juiste site is efreightforwarding.com.

### Hoe het bij vervoerders werkt
- **[FEIT]** DHL: "Binnen Nederland bezorgen we je pakket in principe de volgende dag, mits je pakket op tijd is afgeleverd." https://www.dhlecommerce.nl/nl/consument/faq/verzenden/bezorgduur-dhl
- **[FEIT]** DHL For You Vandaag: "Bestellen consumenten 's avonds, dan ontvangen ze hun order de dag erna, zonder dat u tot laat door hoeft te werken." en "Als u pakketten de volgende ochtend verzendklaar maakt en bij ons aflevert, bezorgen we ze 's avonds tussen 17.30 en 22.00 uur." Afgeven bij een sorteercentrum vóór 13.30 uur. (In de bron staat een gedachtestreepje; hier vervangen door een komma.) https://www.dhlecommerce.nl/nl/zakelijk/dhl-for-you-vandaag , https://www.dhlecommerce.nl/nl/zakelijk/snel-versturen
- **[FEIT]** bol, Verzenden via bol Compleet: belofte "voor 23.59 uur besteld, morgen in huis". Ophalen 16.00 tot 18.00 uur (cut-off 15.00) of 18.00 tot 20.00 uur (cut-off 17.00). Bestellingen daarna en vóór 23:59 worden **de volgende ochtend tussen 09.30 en 11.45 uur opgehaald** en "diezelfde avond nog bij de klant" bezorgd. https://partnerplatform.bol.com/nl/cdp/verzenden-via-bol-com-compleet
- **[FEIT]** PostNL haalservice: vaste dagen of een afspraak met tijdvak tussen 14:00 en 18:00; standaard bezorging de volgende werkdag na aanbieden. Late aanlevering bij hubs tot in de nacht bestaat, maar vraagt eigen vervoer (bron: Webwinkel Forum, zwakke bron). https://www.postnl.nl/zakelijk/post-versturen/verzendopties/haalservice/ (pagina gaf tijdens onderzoek een 503; inhoud via zoekresultaat), https://www.webwinkelforum.nl/viewtopic.php?t=14215

### Conclusie
**[INFERENTIE]** "Voor 23:59 besteld, vandaag verzonden" is voor een bestelling van 22:30 vrijwel nooit waar. De vervoerder haalt 's middags of vroeg in de avond op; een late bestelling gaat de volgende ochtend het magazijn uit. Zelfs bol zegt dat letterlijk over zijn eigen 23:59-belofte. De belofte die wél kan kloppen is **"voor 23:59 besteld, morgen in huis"**, maar alleen als eFreight voor webshoporders hetzelfde mechanisme heeft als bol: ochtendophaling en bezorging dezelfde avond (zoals DHL For You Vandaag).

**[INFERENTIE]** De 23:59 die jullie bij bol zien, komt waarschijnlijk uit de bol-verzendinstelling, niet uit de Offer API zelf. De Retailer API v11 noemt voor `ultimateOrderTime` alleen de waarden "12:00 ... 23:00"; 23:59 staat er niet tussen. https://api.bol.com/retailer/public/Retailer-API/v11/functional/offer-api/offer-api.html . Ook belangrijk, nog te controleren: Verzenden via bol-labels zijn bedoeld voor bol-orders. Voor Shopify-orders moet eFreight met een eigen vervoerderscontract werken, met mogelijk andere ophaaltijden. Hoe bol het voor jullie regelt, zegt dus niets over wat er voor de eigen webshop kan.

### Wat de wet en de ACM zeggen
- **[FEIT]** ACM: "Producten moet u binnen 30 dagen leveren. Behalve als u een andere levertijd afspreekt" en "Voorkom misleiding: zorg dat u beloftes als 'vandaag besteld, morgen in huis' kunt waarmaken." Ook: "U bent verantwoordelijk voor bezorging totdat de consument uw product ontvangt." https://www.acm.nl/nl/verkoop-aan-consumenten/leveren-en-bezorgen
- **[FEIT]** Art. 7:9a BW: zonder afspraak levering binnen 30 dagen. Art. 6:230m BW: informatieplicht over de termijn van levering bij koop op afstand. https://wetten-overheid.nl/wet/BWBR0005289/artikel/230m
- **[FEIT]** ICTRecht: "morgen in huis" bindt de webshop aan de bezorgdag, ook al heeft de vervoerder het in handen; "vandaag verzonden" zegt alleen iets over verzending en bindt niet aan een bezorgdag. Veiliger: "binnen twee werkdagen in huis". https://www.ictrecht.nl/blog/levertijd-van-een-webwinkel-de-dos-en-donts
- **[FEIT]** Thuiswinkel.org: de klant moet vóór de bestelknop weten wanneer geleverd wordt; vage termen mogen niet. https://www.thuiswinkel.org/kennisbank/kennisartikelen/vage-levertermijn-bij-product-plaatsen-mag-niet/

**[INFERENTIE]** Dus: "vandaag verzonden" is juridisch lichter dan "morgen in huis", maar moet nog steeds feitelijk kloppen. Als het pakket bij een bestelling om 23:00 pas de volgende ochtend vertrekt, is "vandaag verzonden" gewoon onjuist en dus misleidend.

### Hoe Nederlandse shops het formuleren [FEIT]
- Coolblue: "Voor 23.59 uur besteld? Morgen in huis. Of wanneer het jou uitkomt." (eigen bezorgdienst)
- Dekbed Discounter: "Voor 23:59 besteld volgende werkdag op je bed" (leuk: het product in de belofte)
- Yumeko: "Voor 17.00 besteld, morgen in huis" en "Gratis retourneren binnen 30 dagen"
- Lazamani, Jan Jansen: "Vandaag besteld, binnen 1-2 werkdagen thuis", met in de voorwaarden een cut-off van 12:00
- Piedi Nudi: "Bestel je op een werkdag vóór 12.00 uur? Dan doen we ons best om je bestelling nog dezelfde dag te verzenden."
- bol: "voor 23.59 uur besteld, morgen in huis"

### Aanbevolen formuleringen voor Bline [INFERENTIE]
Kies er één nadat eFreight schriftelijk de cut-off, de ophaaltijden en de bezorgdagen heeft bevestigd.

1. **Als eFreight een ochtendophaling plus avondbezorging biedt voor webshoporders** (zoals bol VVB Compleet of DHL For You Vandaag):
   "Op werkdagen voor 23:59 besteld? Morgen in huis."
   Plus op de verzendpagina: "Bestel je op vrijdag na [tijd], zaterdag of zondag? Dan komt je pakket op [dag]."
2. **Als eFreight een normale middagophaling heeft (bijvoorbeeld 15:00 of 17:00):**
   "Op werkdagen voor 15:00 besteld, vandaag verstuurd. Meestal ligt hij de volgende dag bij je op bed."
   (Let op "meestal": het is een verwachting, geen garantie.)
3. **Veiligste variant voor in de aankondigingsbalk:**
   "Binnen 1-2 werkdagen in huis" of "Snel in huis, met track & trace".

Op de productpagina: een dynamische regel die werkdagen kent, bijvoorbeeld "Bestel vandaag voor 15:00, dan is hij er donderdag 8 oktober." Alleen met echte data van eFreight en zonder nep-aftelklok.

### Vragen voor eFreight
1. Wat is de cut-off voor webshoporders (Shopify) om dezelfde dag te verzenden?
2. Welke vervoerder, en hoe laat is de laatste ophaling op werkdagen?
3. Hebben jullie een avondbezorging-na-ochtendophaling (zoals DHL For You Vandaag) voor Shopify-orders?
4. Werken jullie op zaterdag? Is er zaterdag- of zondagbezorging?
5. Welk percentage orders is de afgelopen 3 maanden op tijd verzonden (bij voorkeur gesplitst per bol en eigen orders)?
6. Wat gebeurt er in piekweken (Black Friday, december) met de cut-off?

---

## 9. Bronnen (opgehaald 4 oktober 2026)

Shops: https://bartogi.de/ , https://www.bartogi.nl/ , https://lazamani.nl/ , https://www.tofvel.com/ , https://sockwell.nl/ , https://heydude.nl/ , https://hunterboots.nl/ , https://nl.janjansen.com/ , https://keenfootwear.nl/ , https://www.piedinudi.com/ , https://tonipons.nl/ , https://www.geox.com/nl-NL/ , https://hooijerfootwear.com/

Productpagina's: https://sockwell.nl/products/work-heren-compressiekousen-klasse-1-mushroom , https://lazamani.nl/products/dames-sandalen-75-611-black , https://bartogi.de/products/aaf-damen-pantoletten-grey , https://heydude.nl/products/bradley-ii-nylon-wp-heren-boots-downtown-brown-multi , https://hunterboots.nl/products/unisex-downpour-tall-wellington-boots-chocolate-brown , https://nl.janjansen.com/products/bamboo-ankle-bootie-black , https://keenfootwear.nl/products/mens-uneek-360 , https://www.piedinudi.com/products/zuma-05-11-dames-enkellaarsjes-leer-dark-brown , https://tonipons.nl/products/aina-dames-sneakers-leer-cuiro , https://www.tofvel.com/products/rabara-wolvilt-sloffen-black

Thema's: https://platmart.io/blog/shopify-theme-ids/ , https://themes.shopify.com/themes/prestige/presets/allure , https://themes.shopify.com/themes/impact/presets/impact , https://themes.shopify.com/themes/sleek/presets/sleek , https://themes.shopify.com/themes/local/presets/local , https://themes.shopify.com/themes/be-yours/presets/be-yours , https://themes.shopify.com/themes/horizon/presets/horizon , https://support.maestrooo.com/article/806-sticky-add-to-cart , https://support.maestrooo.com/article/687-theme-licensing-and-transfers , https://docs.foxecom.com/sleek-theme/getting-started/theme-license-and-transfer , https://docs.foxecom.com/sleek-theme/collections-and-products/product-page/product-information

Logistiek en recht: https://www.efreightforwarding.com/e-commerce , https://www.nt.nl/logistiek/2026/09/23/e-freight-forwarding-huurt-20-000-m%C2%B2-logistieke-ruimte-in-amersfoort/ , https://www.dhlecommerce.nl/nl/zakelijk/dhl-for-you-vandaag , https://www.dhlecommerce.nl/nl/consument/faq/verzenden/bezorgduur-dhl , https://partnerplatform.bol.com/nl/cdp/verzenden-via-bol-com-compleet , https://partnerplatform.bol.com/nl/idp/leverbeloftes-vvb , https://api.bol.com/retailer/public/Retailer-API/v11/functional/offer-api/offer-api.html , https://www.acm.nl/nl/verkoop-aan-consumenten/leveren-en-bezorgen , https://www.ictrecht.nl/blog/levertijd-van-een-webwinkel-de-dos-en-donts , https://www.thuiswinkel.org/kennisbank/kennisartikelen/vage-levertermijn-bij-product-plaatsen-mag-niet/ , https://wetten-overheid.nl/wet/BWBR0005289/artikel/230m , https://www.coolblue.nl/ , https://www.dekbed-discounter.nl/ , https://www.yumeko.nl/
