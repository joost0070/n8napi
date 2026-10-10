# Bline leeskussen op Meta (Facebook en Instagram): strategie, advertenties en testplan (07-10-2026)

Onderzoek voor Bline (merk van Shop4You). Bouwt voort op:
- `research_notes/Bline Sleep risicos en voorbeelden/markt_advertenties_2026-10-05.md` (Ad Library werkte toen niet, bol-zoekdata);
- `research_notes/Bline Sleep risicos en voorbeelden/onderzoek_beeldopbouw_2026-10-05.md` (welke beelden er per kleur zijn);
- `research_notes/Bline Sleep risicos en voorbeelden/webshop_best_practices_2026-10-06.md` (ACM-regels, meting, conversie);
- `reports/Bline funnel en advertentieplan.md` (break-even €34 per aankoop, landingspagina's, UTM);
- `research_notes/Bol leeskussens Q4 strategie/` (prijsbanden, concurrenten, interne verkoopdata, Q4-kalender).

**Opdrachtwijziging tijdens het onderzoek:** de bestaande 10 Meta-creatives en teksten in `mockups/blinesleep/ads/meta/` zijn door de eigenaar afgekeurd. Ze worden hier niet als basis gebruikt. Hoofdstuk 4.6 zegt kort wat eraan mis was, zodat het niet terugkomt. De nieuwe advertentieset (hoofdstuk 9) is volledig opnieuw ontworpen.

Labels: **[Bron]** is een gevonden bron met link en jaartal, **[Inschatting]** is een eigen afleiding of rekensom, **[Intern]** komt uit eigen data van Bline.

---

## Samenvatting: de 12 belangrijkste beslissingen

1. **Eén campagne, één advertentieset, één budget van €10 per dag.** Advantage+ verkoopcampagne (de opvolger van Advantage+ shopping), NL plus Vlaanderen samen, Advantage+ doelgroep en plaatsingen. Bij €10 per dag haalt Bline nooit de leerfase (25 tot 50 aankopen per week); splitsen maakt dat alleen erger. Geen aparte retargetingcampagne in de eerste 6 weken.
2. **Optimaliseren op Aankoop**, niet op Toevoegen aan winkelwagen. Pas na €150 zonder aankoop maar met 8 of meer toevoegingen eenmalig overstappen op winkelwagen. Weinig toevoegingen betekent een probleem in advertentie of pagina, niet in het doel.
3. **Eerst meting, dan pas geld.** Pixel plus Conversions API via de Shopify-app op "Maximaal", testbestelling zichtbaar als Purchase met waarde, domein geverifieerd, cookiebanner aan. Reken erop dat Meta in NL door weigeren van cookies maar een deel van de aankopen ziet; beoordeel op Shopify-orders met UTM.
4. **Begin met 6 advertenties die echt van elkaar verschillen**, niet met 15. Meta groepeert gelijkende advertenties tot één "entity"; verschil moet zitten in minstens twee van: format, persoon, omgeving, voordeel. Na 10 tot 14 dagen 4 nieuwe erbij, vanaf 16 november 4 seizoensadvertenties.
5. **Video en demonstratie krijgen voorrang.** Demo, unboxing, testimonial en "aanbod eerst" scoren de hoogste trefkans in de dataset van Motion (2026). De eerste advertentie is een nieuwe montage van de bestaande productvideo in 9:16 en 4:5; de eerste nieuwe opname is een telefoonvideo "kussens stapelen tegen Bline".
6. **Het probleem laten zien, niet erover praten.** Sterkste invalshoek voor koude doelgroepen: de kussenstapel die wegschuift tegenover één kussen dat blijft staan, gevolgd door het zijvak en de wasbare hoes. Geen medische woorden, geen "heb jij last van..." (verboden door Meta én door eigen regels).
7. **Nieuwe beeldregels:** product minstens 40% van het beeld, één kop van maximaal 8 woorden, tekst maximaal ongeveer 20% van het vlak, contrast in de feed met donkerblauw (#1F2A37), terracotta (#C4623E) of salie (#7C8B74) in plaats van alles beige. Nooit meer ingekleurde beelden; de roodharige vrouw alleen in het echte witte origineel.
8. **Elke advertentie landt op de kleurpagina die in beeld is**, met de prijs van die kleur in de tekst (€79,99; wit €69,99). Geen "vanaf €69,99" bij een beige of blauw beeld. Vaste UTM met `{{ad.name}}` en `{{placement}}`.
9. **Schrijfstijl:** eerste zin is de hook en staat los (maximaal ongeveer 125 tekens), daarna kort probleem, oplossing, 2 tot 3 feiten, bezwaar weg, aanbod. Per advertentie 3 tot 5 eigen tekstvarianten; Meta's eigen AI-tekst en het herschrijven van tekst in beelden uitzetten (staat sinds 27-07-2026 standaard aan).
10. **België is geen bijzaak:** 55% van de bol-kussens ging naar België. Eén campagne voor NL en Vlaanderen in neutraal Nederlands met "je", geen Hollandse spreektaal, "gratis verzending in Nederland en België" expliciet. Wallonië en Brussel uitsluiten zolang er geen Franse pagina is.
11. **Q4 zonder nepkorting:** starten vóór half oktober (advies van Meta), Black Friday-week niet opschalen (CPM 2 tot 3 keer hoger), cadeau-invalshoek vanaf 16 november met echte besteldeadlines (Sinterklaas NL 5 december, Sint-Niklaas BE 6 december, Kerst). Alleen echte voordelen: 2 kussens of extra hoes €9,99 voordeel, die ook op bol gelden.
12. **Stopregels:** advertentie na €8 met link-CTR onder 0,6% vervangen; na 7 dagen advertenties zonder enige winkelwagen pauzeren; €150 zonder aankoop: stoppen en trechter nalopen; kosten per aankoop over 14 dagen onder €25 met 4+ aankopen: budget +20%; boven €34: niet opschalen.

---

## 1. Strategie 2026 voor een nieuw D2C-merk met één product van ongeveer €80

### 1.1 Wat er in 2025-2026 veranderde

- **Andromeda** is Meta's nieuwe selectiesysteem dat uit tientallen miljoenen advertenties een paar duizend kandidaten per persoon kiest. Meta meldt +6% recall en +8% advertentiekwaliteit; adverteerders met Advantage+ creative zagen gemiddeld 22% hogere ROAS ([Meta Engineering, 2024](https://engineering.fb.com/2024/12/02/production-engineering/meta-andromeda-advantage-automation-next-gen-personalized-ads-retrieval-engine/)). Gevolg: de inhoud van de advertentie bepaalt steeds meer wie hem ziet; doelgroepinstellingen worden minder belangrijk ([Chatterbuzz, 2026](https://www.chatterbuzzmedia.com/blog/meta-andromeda-creative-targeting/)).
- **Advantage+ shopping bestaat niet meer als apart type.** Meta voegde het samen tot één "Advantage+ verkoopcampagne" met drie hendels: budget op campagneniveau, Advantage+ doelgroep, Advantage+ plaatsingen. Vanaf API-versie 24.0 (8 oktober 2025) konden geen oude ASC-campagnes meer gemaakt worden, in Q1 2026 is het oude type helemaal uitgefaseerd ([PPC Land, 2025](https://ppc.land/meta-deprecates-legacy-campaign-apis-for-advantage-structure/)).
- **Leerfase:** Meta's vuistregel is ongeveer 50 optimalisatie-events per advertentieset in 7 dagen; grote wijzigingen (budget meer dan ongeveer 20%, nieuw doel, nieuwe doelgroep, nieuwe advertenties) zetten de teller terug ([Meta Business Help](https://www.facebook.com/business/help/112167992830700), samengevat door [LSEO, 2025](https://lseo.com/paid-media/paid-social-media-marketing/understanding-the-facebook-ads-learning-phase-a-full-guide)). Volgens [1ClickReport (2026)](https://www.1clickreport.com/blog/advantage-plus-shopping-25-conversions-2026-guide) verlaagde Meta dit in april 2026 naar 25 per week voor Advantage+ verkoopcampagnes; een officiële Meta-bron daarvoor vond ik niet.
- **Attributie:** sinds januari 2026 zijn 7- en 28-dagen view-vensters uit de rapportage verdwenen; standaard is nu 7 dagen klik, 1 dag "engage-through" en 1 dag view ([Dataslayer, 2026](https://dataslayer.ai/blog/meta-ads-attribution-window-removed-january-2026)).
- **Event-prioritering (AEM) hoeft niet meer handmatig;** domeinverificatie is niet meer verplicht maar wel aan te raden ([Jon Loomer, 2025](https://www.jonloomer.com/meta-announces-big-changes-to-website-conversion-campaigns/)).

### 1.2 Wat €10 per dag realistisch oplevert

[Inschatting] Rekensom met voorzichtige NL-waarden:

| Stap | Aanname | Per week (€70) |
|---|---|---|
| CPM (kosten per 1.000 vertoningen) | €6 tot €10 | 7.000 tot 11.700 vertoningen |
| Link-CTR | 0,8% tot 1,5% | 55 tot 175 klikken |
| Naar winkelwagen | 5% tot 8% van bezoekers | 3 tot 14 |
| Aankoop | 1% tot 2% van bezoekers | 1 tot 3 |
| Kosten per aankoop | | €23 tot €70 |

Break-even is €34 per aankoop (funnelplan, hoofdstuk 8). Bline zit dus rond break-even of erboven, en haalt nooit 25 of 50 aankopen per week. De advertentieset blijft "Leren beperkt". Dat is bij dit budget normaal en geen reden om in te grijpen. Het vooraf betaalde bedrag van €150 is na 15 dagen op.

### 1.3 Campagnestructuur

| Keuze | Advies | Waarom |
|---|---|---|
| Aantal campagnes | 1 | Volume op één plek leert het snelst; vijf kleine campagnes concurreren met elkaar ([Blck Alpaca, 2026](https://blckalpaca.at/en/knowledge-base/social-media/paid-social-performance-marketing/meta-andromeda-gem-advantage-plus)). Jetfuel adviseert onder $100 per dag "één brede campagne met 6+ sterke creatives" ([Jetfuel, 2026](https://jetfuel.agency/meta-ads-strategy-for-dtc-ecommerce-brands-in-2026-the-andromeda-playbook/)). |
| Type | Advantage+ verkoopcampagne | Het enige verkooptype dat Meta nog doorontwikkelt; 1 advertentieset is genoeg. |
| CBO of ABO | Campagnebudget (Advantage+ budget). Met één advertentieset maakt het niet uit. | ABO alleen nodig als je later een losse test-set wilt die niet leeggegeten wordt. |
| Advertentiesets | 1 | Elke extra set halveert het signaal. |
| Advertenties | 6 bij start, 10 na week 2, 14 in Q4 (oude pauzeren) | Andromeda wil verscheidenheid, maar bij €10 per dag krijgen 15 advertenties elk vrijwel niets. Minimaal 6 echt verschillende is de ondergrens die Jetfuel noemt. |
| Budget wijzigen | Hoogstens 1 keer per week, maximaal 20% | Elke grote wijziging start het leren opnieuw. |

### 1.4 Creatives testen

- **Verscheidenheid telt, niet aantal.** Meta groepeert advertenties die er voor zijn beeld- en taalmodellen hetzelfde uitzien tot één "entity". Tien versies van dezelfde video met een andere openingszin zijn één entity, geen tien ([Jetfuel, 2026](https://jetfuel.agency/meta-ads-strategy-for-dtc-ecommerce-brands-in-2026-the-andromeda-playbook/)). Een nieuwe entity verschilt in minstens twee van: format, persoon, omgeving, voordeel.
- **Verwacht weinig winnaars.** In 550.000 advertenties werd 5 tot 8% een echte winnaar en kreeg ongeveer de helft nooit serieus budget ([Motion, 2026](https://motionapp.com/events/2026-creative-strategy-bootcamp/homebase/2026-creative-benchmarks)). Dat Meta één advertentie het meeste geld geeft, is normaal.
- **Testtool:** Meta heeft sinds oktober 2025 een ingebouwde creatieve test (tot 5 advertenties, eigen deel van het budget, tot 30 dagen) ([Search Engine Journal, 2025](https://www.searchenginejournal.com/how-to-evaluate-creative-performance-in-meta-ads/558741/)). [Inschatting] Bij €10 per dag levert een test van €2 per dag geen bruikbare uitslag op. Nieuwe advertenties gewoon in de bestaande set zetten, in groepjes van 3 tot 4.
- **Wanneer stoppen:** zie het testplan (hoofdstuk 10). Kern: niet oordelen op aankopen per advertentie (te weinig), maar op klik, winkelwagen en kosten per bezoek, en pas na genoeg uitgave.

### 1.5 Retargeting apart of niet

Met een Advantage+ doelgroep gaat volgens Jon Loomer al 25 tot 35% (soms 45%) van het budget naar bestaande klanten en mensen die al betrokken waren; een aparte retargetset is meestal overbodig. Uitzondering die hij noemt: een duur product met maximaal ongeveer $50 per dag, waar je direct op verkoop wilt sturen ([Jon Loomer, 2025-2026](https://www.jonloomer.com/qvt/is-remarketing-still-relevant/), [Jon Loomer](https://www.jonloomer.com/prioritize-remarketing-over-metas-algorithmic-ad-targeting/)).

Advies voor Bline:
- **Week 1 tot 6: geen aparte retargeting.** [Inschatting] Bij 150 tot 600 bezoekers per maand is de groep zo klein dat €2 per dag dezelfde mensen tien keer per week laat zien. Meta toont de advertenties al aan bezoekers binnen de ene campagne. De verlaten-winkelwagen- en welkomstmails in Klaviyo doen het werk dat retargeting anders doet.
- **Opnieuw bekijken** zodra er 1.000+ websitebezoekers per 30 dagen zijn of het totale budget €20+ per dag is. Dan: €3 per dag, bezoekers productpagina en winkelwagen van 14 dagen, uitsluiten kopers 30 dagen, advertentie A10 (30 dagen proberen) en A13 (twee kussens).
- **Let op:** omdat Meta ook geld uitgeeft aan mensen die toch al zouden kopen (zie de les van Piedi Nudi: geld ging naar de eigen merknaam), overschat de Meta-rapportage het effect. Daarom de wekelijkse controle op Shopify-orders (hoofdstuk 6).

### 1.6 Doelgroep: breed of interesses

- **Breed, met Advantage+ doelgroep, zonder of met een lichte suggestie.** Meta heeft in januari 2026 handmatige interesses uit catalogusadvertenties gehaald ([zoekresultaat over Meta catalog ads, 2026](https://cropink.com/meta-catalog-ads)); de richting is duidelijk. De creatives doen de targeting: een advertentie met een student op een gamekussen bereikt andere mensen dan een met een vrouw van 60 op de bank.
- **Harde instellingen (controls):** locatie, minimumleeftijd, taal. Advies: minimumleeftijd 25 [Inschatting: koopkracht en leesgedrag; eerst breed laten, leeftijdsverdeling na 14 dagen bekijken], taal Nederlands.
- **Suggestie (optioneel):** leeftijd 30 tot 65. Meta mag daarbuiten gaan.

### 1.7 NL en België

- [Intern] Van juni tot september 2026 ging 55% van de bol-kussens naar België (36 van 65); Bline's vertoningsaandeel op bol is in België hoger (18 tot 20%) dan in NL (8%) (`interne_data_en_scenarios.md`, `markt_en_concurrenten.md`).
- **Eén campagne voor beide.** Splitsen per land kost signaal. Locatie: Nederland plus de provincies Antwerpen, Limburg, Oost-Vlaanderen, Vlaams-Brabant en West-Vlaanderen. Brussel en Wallonië niet zolang er geen Franse pagina is.
- **Per land kijken, niet per land sturen:** elke maandag uitsplitsen op land. Pas splitsen als het budget €25+ per dag is en de kosten per aankoop meer dan 30% verschillen [Inschatting].
- **Toon:** Belgen reageren beter op bescheiden, minder schreeuwerige communicatie ([KVK, e-commerce in België](https://www.kvk.nl/internationaal/e-commerce-in-belgie/)); prijs weegt zwaarder en reviews iets lichter dan in NL ([Trustpilot via Emerce, 2019](https://www.emerce.nl/wire/prijs-bepaalt-keuze-webwinkel-belgi-reviews-bepalend-nederland)); 77% van de Belgen wordt over de streep getrokken door gratis verzending en track-and-trace is belangrijk ([Emerce, 2021](https://www.emerce.nl/achtergrond/wat-verwachten-belgen-van-nederlandse-webshops-drie-adviezen-over-bezorging)). Vertaling: "je" is prima, geen "lekker", "hartstikke", "even checken"; "gratis verzending in Nederland en België" uitschrijven.

### 1.8 Optimalisatie-event: Aankoop of Toevoegen aan winkelwagen

Bronnen spreken elkaar tegen. Aimerce adviseert onder het drempelvolume op winkelwagen te optimaliseren ([Aimerce, 2026](https://www.aimerce.ai/blogs/meta-atc-purchases-vs-awareness-traffic-what-to-run-and-when-to-use-them)); in de Shopify-community wordt ook gepleit voor Aankoop vanaf dag één, omdat winkelwagen-optimalisatie "kijkers" vindt die niet kopen ([Shopify Community, 2026](https://community.shopify.com/t/new-meta-pixel-with-no-purchase-data-best-optimization-strategy-for-a-new-store/650420)).

**Advies:** starten op **Aankoop** met de echte orderwaarde. [Inschatting] Bij 3 tot 14 toevoegingen per week haalt ook winkelwagen de drempel niet; je ruilt dan een duidelijk doel in voor een vaag doel zonder het leren te halen. Overstapregel: na €150 met 0 aankopen maar 8 of meer toevoegingen, één keer overstappen op Toevoegen aan winkelwagen en 14 dagen laten staan. Minder dan 8 toevoegingen: het event is niet het probleem; dan advertenties en productpagina nalopen.

### 1.9 Instellingen die je bij Bline moet uitzetten

- **Advantage+ creative "tekstverbeteringen", "tekst genereren" en "tekst in afbeelding herschrijven" uit.** Sinds 27 juli 2026 herschrijft Meta standaard koppen die in een afbeelding staan, tot 8 varianten, zonder menselijke controle ([Common Thread Collective, 2026](https://commonthreadco.com/blogs/coachs-corner/meta-advantage-plus-creative-image-text-rewriting-ecommerce-2026)). Voor Bline is dat een risico op medische woorden of verkeerde prijzen. Vul ook de lijst "beperkte woorden" in (rugpijn, ergonomisch, houding, orthopedisch, beste, nummer 1, korting).
- **Achtergrond genereren, beeld uitbreiden, animatie toevoegen uit.** Geen nieuwe AI-beelden zonder akkoord, en Meta zet dan een "AI-info"-label naast "Gesponsord" als er fotorealistische AI-mensen in staan ([Meta Help, 2025-2026](https://www.meta.com/en-gb/help/artificial-intelligence/355108217670024/)).
- **Plaatsingen:** Advantage+ plaatsingen, maar Audience Network uitsluiten [Inschatting: veel klikken van lage kwaliteit bij kleine budgetten].
- **Geen dagdelen.** De Piedi Nudi-piek (13 tot 22 uur, vrijdag en zaterdag) kan in Advantage+ niet met een dagbudget worden ingesteld en Meta verdeelt zelf. Gebruik die piek alleen om nieuwe advertenties op donderdag of vrijdag live te zetten [Inschatting].

---

## 2. Formats: wat werkt voor dit product

### 2.1 Wat het bewijs zegt

- **Trefkans per visueel format** (Motion, 578.750 advertenties, $1,29 miljard, 2026): unboxing 9,8%, "aanbod eerst"-banner 8,6%, demo 8,1%, testimonial 6,5%. Formats die meer budget krijgen dan hun aandeel: brief (persoonlijke boodschap), tekst op een onverwachte plek, post-it ([Motion formatbibliotheek, 2026](https://motionapp.com/library/formats/)).
- **Statisch en video naast elkaar.** Mediaan 61% statisch, 39% video over 67.000 advertenties; producten met zichtbaar effect gebruiken meer video ([Segwise, 2026](https://segwise.ai/blog/static-video-ratio-meta-ads)). Video heeft hogere CTR maar ook hogere CPM.
- **Vijf vaste DTC-formats:** "wij tegen zij", probleem-oplossing, demo, testimonial, redenen-waarom ([Segwise, maart 2026](https://segwise.ai/blog/100m-meta-ads-5-formats-dtc)). Statische formats die in 2026 goed werken: één kernidee in maximaal 10 woorden, het "dambord" (2 x 2 met tekst en beeld afwisselend), platform-native (ziet eruit als een gewone post) ([Admetrics, april 2026](https://www.admetrics.io/post/five-static-ad-formats-outperforming-video-in-2026)).
- **Partnership-advertenties met makers:** volgens een door Meta aangehaalde vergelijking 19% hogere CTR, 10% hogere conversie en 5% lagere CPA dan dezelfde content vanaf het merkaccount ([Martechvibe, 2025](https://martechvibe.com/article/creator-ads-deliver-19-higher-ctr-on-meta-partnership-ads)).
- **Vertical eerst:** Meta adviseert in de feestdagengids aparte formats te maken (verticale video voor Reels, statisch voor de feed, carrousel) in plaats van één beeld te verschalen ([Relevant Audience over Meta's playbook, augustus 2026](https://www.relevantaudience.com/meta/meta-holiday-playbook-four-phases-q4/)).

### 2.2 Specificaties en veilige zones

| Plaatsing | Formaat | Veilige zone voor tekst en logo | Bron |
|---|---|---|---|
| Feed (FB en IG) | 4:5, 1080 x 1350 (of 1440 x 1800) | Hele beeld zichtbaar; houd 60 px marge rondom | [Billo, 2026](https://billo.app/?p=50654) |
| Stories en Reels | 9:16, 1080 x 1920 | Boven 14% (269 px), onder 35% (672 px), zijkanten 6% (65 px) vrij. Bruikbaar vlak: x 65 tot 1015, y 269 tot 1248 | [Inro safe zone tool, 2026](https://www.inro.social/tools/instagram-reels-safe-zone-checker), [Billo, 2026](https://billo.app/?p=50654) |
| Carrousel | 1:1, 1080 x 1080, 2 tot 10 kaarten | 60 px marge | |
| Video | MP4 H.264, 30 fps; voor verkoop 15 tot 30 s; ondertitels ingebrand | Zelfde zones als hierboven | [Metricool, 2026](https://metricool.com/meta-ad-formats/) |

Ondertitels zijn nodig: het grootste deel van de mobiele video wordt zonder geluid gestart ([Digiday, ouder onderzoek](https://digiday.com/sponsored/75-percent-of-people-watch-mobile-videos-on-mute/)), en Meta raadt ondertitels ook voor Reels aan ([Metricool, 2026](https://metricool.com/meta-ad-formats/)).

### 2.3 Per format: waarom en prioriteit voor Bline

| Format | Waarom voor een leeskussen | Prioriteit | Materiaal |
|---|---|---|---|
| **Demo-video 9:16 en 4:5** | Het voordeel (blijft staan, vak, hoes eraf) is iets wat je moet zien. Hoge trefkans. | 1 | Bestaande productvideo opnieuw monteren; daarna telefoonopname |
| **Probleem-oplossing / wij tegen kussenstapel** | Het herkenbare probleem is de kussenstapel. Vergelijken met "losse kussens" is veilig (geen concurrent genoemd). | 1 | Statisch nu, video zodra opgenomen |
| **Productuitleg met lijntjes (annotated)** | Legt in één beeld de €80 uit: 3,8 kg, vak, hoes, maat. | 1 | Bestaand productbeeld |
| **Moment / persoon (native)** | Andere persoon, andere kamer, andere functie = nieuwe entity. | 1 | Bestaande sfeerbeelden |
| **Carrousel kleur en moment** | Vijf kleuren is een echte keuze; elke kaart een andere persoon. | 2 | Bestaande sfeerbeelden |
| **Aanbod eerst (30 dagen proberen, gratis verzending)** | Hoogste trefkans-format; Bline heeft geen korting maar wel een echt risico-arm aanbod. | 2 | Bestaand productbeeld |
| **Maat op het bed** | Antwoord op de bekende klacht "neemt de halve bedbreedte in" bij XXL-kussens. | 2 | Bestaande maattekening |
| **Unboxing** | Hoogste trefkans bij Motion; laat zien wat er in de doos zit en hoe het kussen opbolt. | 2 | Nieuw (telefoon) |
| **UGC / maker** | Echte persoon, eigen kamer, telefoonbeeld. Werkt bij Cloudpillo (15 tot 20 korte video's per week) ([MT/Sprout, 2024](https://mtsprout.nl/groei/cloudpillo-hoofdkussen)). | 2 (zodra er maker is) | Nieuw, via Collabs |
| **Testimonial met klantcitaat** | Sterk, maar bol-reviewteksten mogen niet (afspraak) en eigen reviews zijn er nog niet. | 3 (na 5+ Judge.me-reviews) | Eigen reviews |
| **Voor/na** | Werkt niet goed voor een kussen zonder lichamelijke claim; "voor" = kussenstapel valt al onder probleem-oplossing. Risico op impliciete gezondheidsclaim. | Niet | |
| **Collectie / Instant Experience** | Bedoeld voor veel producten. | Niet | |
| **Advantage+ catalogusadvertenties** | Eén product in vijf kleuren; catalogus voegt weinig toe en de Shopify-feed bevat ook hoezen. Catalogus wel synchroniseren voor later. | 3 (na 4 weken, alleen als test) | Feed |

---

## 3. Manier van schrijven

### 3.1 Regels

- **Primaire tekst:** de eerste ongeveer 125 tekens zijn zichtbaar zonder "meer" ([AdsUploader, 2026](https://adsuploader.com/blog/meta-ad-copy-specs)). De hook moet daarin staan en mag niet afhangen van de rest. Uit een analyse van overlevende advertenties: korter dan 50 tekens scoort het best, met een tweede piek bij 250 tot 500 tekens ([Webtonic, 2026](https://www.webtonic.io/blog/ad-text-optimization-statistics)). Advies: per advertentie één korte variant (onder 60 tekens) en één middellange (250 tot 400 tekens).
- **Kop:** 27 tot 40 tekens; **beschrijving:** 25 tot 30 tekens (wordt vaak niet getoond, dus niets belangrijks alleen daar).
- **Meerdere teksten:** tot 5 primaire teksten en 5 koppen per advertentie; Meta noemt het "geoptimaliseerd" vanaf 3 ([Jon Loomer](https://www.jonloomer.com/meta-ads-creative-optimization/)). Wel zelf schrijven, AI-varianten uit.
- **Structuur middellange tekst:** 1) hook, 2) herkenbaar moment in één zin, 3) wat Bline anders doet (2 tot 3 feiten met getallen), 4) bezwaar weg (prijs, maat, wassen, risico), 5) aanbod en verzending.
- **Toon:** feitelijk, rustig, licht humoristisch, "je". Geen uitroeptekens in reeks, geen "ultiem", "upgrade", "ontdek", "officiële website" (de MCC-les: standaardformules leverden "gemiddelde" of "slechte" advertentiekwaliteit op).
- **Emoji's:** maximaal één, alleen functioneel (bijvoorbeeld een boek). Geen rijen vinkjes; die lezen als sjabloon.
- **CTA-knop:** "Nu kopen" voor alle advertenties. [Inschatting] "Meer info" geeft vaak meer klikken maar minder kopers; pas testen als er genoeg data is.
- **Prijs:** de prijs van de kleur die in beeld is. Bij wit "€69,99", bij andere kleuren "€79,99". Prijs in de tekst helpt kijkers die het te duur vinden vóór de klik af te haken; dat bespaart klikgeld [Inschatting].
- **Aanbod:** alleen wat echt en permanent is: gratis verzending NL en BE, 1 tot 2 werkdagen, 30 dagen proberen, 2 kussens €9,99 voordeel, extra hoes €9,99 voordeel. Geen doorgestreepte prijs, geen "op=op", geen aftelklok.
- **Sociale bewijskracht:** "4,5 van 5 op bol.com (13 reviews)", altijd met het aantal. Klein en feitelijk, niet als hoofdboodschap (13 reviews is een dunne basis; de 4,5 met "13" erbij is eerlijker en geloofwaardiger).
- **Verboden woorden en vormen:** rugpijn, ergonomisch, houding, orthopedisch, therapeutisch, ontlast, nek, "beste", "nummer 1", "heb jij last van", "ben jij iemand die...". Meta verbiedt teksten die een persoonlijk kenmerk of gezondheidstoestand van de kijker suggereren ([Jon Loomer over het personal attributes-beleid](https://www.jonloomer.com/can-we-use-the-words-you-and-your-in-facebook-ads-copy/)). Geen persoonsnamen, ook niet als "klant Lisa".

### 3.2 Hooks voor Bline (eerste regel, alle binnen de regels)

| Nr | Hook | Invalshoek |
|---|---|---|
| 1 | Drie kussens achter je rug en na tien minuten lig je weer half plat. | Probleem |
| 2 | Eén kussen dat blijft staan als je ertegenaan leunt. | Oplossing |
| 3 | Je bed heeft geen rugleuning. Dit is er één. | Kernidee |
| 4 | Waar laat jij je telefoon als je in bed leest? | Detail (zijvak) |
| 5 | 3,8 kilo traagschuim. Daarom schuift hij niet weg. | Feit |
| 6 | Lezen, laptop of serie: rechtop in bed zonder kussenberg. | Momenten |
| 7 | De hoes gaat eraf en in de was op 30 °C. Het kussen niet. | Bezwaar (hygiëne) |
| 8 | 65 cm breed. Op een bed van 160 blijft er 95 cm over. | Bezwaar (maat) |
| 9 | Probeer hem 30 dagen in je eigen bed. | Risico weg |
| 10 | Nog één hoofdstuk. En nog één. | Herkenning lezers |
| 11 | Niet alleen voor in bed: ook op de bank. | Nieuwe plek |
| 12 | Cadeau voor wie elke avond "nog even" leest. | Q4 |
| 13 | Elke avond je kussens opbouwen? Eén keer neerzetten is genoeg. | Gemak |
| 14 | Kopers op bol.com geven hem een 4,5 (13 reviews). Nu ook rechtstreeks bij ons. | Bewijs |

Hook 13 begint met een vraag over gedrag, niet over een kenmerk of klacht; dat valt binnen het beleid.

---

## 4. Beeld

### 4.1 Tekst in het beeld

- Meta handhaaft de 20%-regel niet meer, maar beelden met minder tekst presteren volgens Meta nog steeds beter ([Social News Desk, 2020](https://www.socialnewsdesk.com/blog/facebooks-20-rule-is-no-more/)). Advies: één kop van maximaal 8 woorden, eventueel één ondersteunende regel of één badge.
- **Grootte op 1080 px breed:** kop 72 tot 96 px, Poppins SemiBold of Bold, regelafstand 1,05; ondersteunende regel 36 tot 40 px Poppins Regular; badges 30 tot 34 px. Kleiner dan 30 px is op een telefoon niet leesbaar.
- **Waar:** in 4:5 bovenaan (eerste 25%) of in een vlak naast het product; in 9:16 tussen y 269 en y 1248.
- **Geen italic schreeftletter als accent** in advertenties: klein en dun valt weg op mobiel en het geeft een sjabloongevoel. Schreef blijft voor de website.

### 4.2 Kleur en contrast

- De feed van een slaapkamer- of interieurliefhebber is beige en wit. Een beige advertentie valt daarin weg. Gebruik de merkkleuren met contrast:
  - Nacht `#1F2A37` (donkere vlakken, tekst op licht);
  - Terracotta `#C4623E` (één accent per advertentie: badge, onderstreping);
  - Salie `#7C8B74` en Mist `#E5EAF2` (rustige vlakken);
  - Zand `#F2EADF` (alleen als achtergrond achter donkere producten);
  - Ster `#E8A317` (alleen voor de ster bij de score).
- Logo: woordmerk `mockups/blinesleep/logo/bline-logo.svg` (of `bline-logo-wit.svg` op donker), 44 px hoog, in een hoek, nooit in een kopbalk.

### 4.3 Productshot of lifestyle, mensen

- Mix beide: het product moet in elke advertentie in de eerste seconde herkenbaar zijn (wigvorm, kleur, vak). Lifestyle verkoopt het moment; productshot verkoopt de keuze.
- Gezichten trekken aandacht, maar de Higgsfield-mensen zijn AI-gemaakt. [Inschatting] Mensen voelen dat steeds vaker aan ("te glad"); dat verklaart deels het "goedkope" gevoel. Gebruik ze voor momenten, niet als "klant". Gebruik de echte shoot (wit, vrouw met laptop) als enige echte persoon tot er UGC is.
- Fotorealistische AI-mensen kunnen een "AI-info"-label naast "Gesponsord" krijgen als Meta ze herkent ([Meta Help](https://www.meta.com/en-gb/help/artificial-intelligence/355108217670024/)). Nog een reden om snel echt beeld te maken.
- **Kleurtrouw:** de Higgsfield-kussens wijken soms af van het echte product (grijs_04 is lichter, beige_04 heeft een linnenstructuur). Klachten over "kleur komt niet overeen" zijn bij concurrenten een bekend minpunt (`markt_en_concurrenten.md`). Voor kleurkeuze dus de productfoto's (serie 05/07), voor sfeer de Higgsfield-beelden.

### 4.4 Prijsbadges en "native"

- Prijsbadge alleen bij aanbod- en cadeau-advertenties, met de prijs van de kleur in beeld.
- Mix gepolijst en "native": native betekent een gewone foto met één tekstregel zoals in een Instagram-story (witte tekst in een afgeronde balk), geen kaders, geen kopbalk.

### 4.5 Bronbeelden die gebruikt mogen worden

Alle paden onder `mockups/blinesleep/`. Higgsfield-originelen zijn 2048 x 2048 png (ook via `beelden_higgsfield/koppeling.json`), bol-beelden 1200 x 1200.

| Code | Bestand | Wat | Gebruik |
|---|---|---|---|
| H-blauw04 | `beelden_higgsfield/blauw_04_b6493bcc.png` | Man ±50, avond, leeslamp, blauwe muur | Probleem-oplossing, kerst |
| H-zwart03 | `beelden_higgsfield/zwart_03_8a600508.png` | Tiener met koptelefoon en laptop | Gamen/studie, Sinterklaas |
| H-zwart02 | `beelden_higgsfield/zwart_02_7f568477.png` | Vrouw ±65 op grijze bank, zwart kussen | Bank |
| H-wit06 | `beelden_higgsfield/wit_06_dd51760c.png` | Zelfde scène met wit kussen | Carrousel wit |
| H-beige04 | `beelden_higgsfield/beige_04_9d9bf3d0.png` | Vrouw ±35, grijze trui, leest | Carrousel beige, post-it |
| H-grijs04 | `beelden_higgsfield/grijs_04_e88bcb0c.png` | Vrouw ±45, zolderkamer, laptop | Carrousel grijs |
| H-grijs03 | `beelden_higgsfield/grijs_03_3470a6af.png` | Man ±35, T-shirt, laptop | Split twee kussens |
| H-blauw02 | `beelden_higgsfield/blauw_02_3695e0c2.png` | Vrouw krullen, gele trui, laptop, planten | Reserve |
| H-beige07 | `beelden_higgsfield/beige_07_08c2e4d1.png` | Packshot beige op bed met boek | Uitleg met lijntjes, cadeau |
| B-wit07 | `beelden_bol/wit_07_1200.jpg` | **Echte shoot**: vrouw met laptop, wit kussen | Native werken |
| B-wit05 | `beelden_bol/wit_05_1200.jpg` | **Echte shoot**: wit kussen met boek | Kleurenslideshow |
| B-wit10 | `beelden_bol/wit_10_1200.jpg` | **Echte shoot**: open rits, traagschuim | Uitleg, video |
| B-wit11 | `beelden_bol/wit_11_1200.jpg` | Maattekening 65 x 50 x 45 | Maat op bed |
| Packshots | `beelden_higgsfield/blauw_05_2a75b663.png`, `grijs_05_e0126ef9.png`, `zwart_05_fe50e2b8.png`, `beige_07_08c2e4d1.png`, `beelden_bol/wit_05_1200.jpg` | Zelfde opstelling per kleur | Kleurenslideshow, aanbod |
| Maatgids | `beelden_bewerkt/bline-maatgids-bedden-01.jpg` | Bovenaanzicht 140/160/180 | Maat op bed |
| Productvideo | Shopify Files "video leeskussen.mp4" (1080 x 1080, 25 s) | Leunen, vak, hoes eraf | Demo |

Niet gebruiken: de ingekleurde versies van de roodharige vrouw (`blauw_08`, `grijs_08`, `beige_02` en de `bline-tegel-*-sfeer`-montages), de bol-hoofdbeelden met tekst (`*_00`), de beelden met "Berg je boek eenvoudig op!" en de gedrapeerde hoes als kegel.

### 4.6 Wat er mis was met de afgekeurde set (niet herhalen)

1. **Eén sjabloon voor alles:** lichte kopbalk met kop, foto eronder, logo rechts, vrijwel alles beige en gebroken wit. In de feed oogt dat als één advertentie, en Meta ziet het als bijna dezelfde entity. Geen contrast, geen duimstopper.
2. **Ingekleurde beelden:** de roodharige vrouw in drie van de negen advertenties, telkens in een andere kussenkleur die achteraf is ingekleurd. Randen en licht kloppen niet; dat voelt goedkoop en onecht.
3. **Het probleem werd nergens getoond.** "Geen kussenfort meer" is een woordgrap die de kijker zelf moet vertalen; de wegzakkende kussenstapel zag je niet.
4. **Product te klein of onduidelijk:** de collage van vier momenten (vier kleine gezichten, het kussen nauwelijks leesbaar op mobiel), de vulling zonder context, de hoes als kegel.
5. **Reels-versies met tekst in de dode zone:** in de 9:16-versies stonden "Vak voor je telefoon · hoes wasbaar" (y ≈ 1600 tot 1670) en de voetregel (y ≈ 1815) in de onderste 35%, achter de knop en het bijschrift van Instagram.
6. **Inhoud klopte niet met beeld:** "Gamen" zonder iemand die gamet; "Vanaf €69,99" bij een beige of grijs kussen dat €79,99 kost.
7. **Zwak bewijs als hoofdboodschap:** een grote "4,5" op basis van 13 reviews op een ander platform, met "nu ook in onze eigen winkel" (over de verkoper, niet over de koper).
8. **Bundel met €104,99 als hoofdgetal** voor koude doelgroepen: hoogste prijs als eerste indruk.
9. **Geen video, geen demonstratie, geen echte mensen, geen maat-op-bed:** precies de formats met de hoogste trefkans ontbraken.
10. **Teksten:** rijen vinkjes, dezelfde "4,5 uit 5 op bol.com" in bijna elke advertentie, eerste zin niet sterk genoeg om los te staan.

---

## 5. Concurrenten en voorbeelden

**Bereikbaarheid:** de Meta Ad Library gaf op 07-10-2026 opnieuw HTTP 403 zonder ingelogde sessie (ook op 05-10). Concurrent-advertenties op Meta zijn dus niet één op één bekeken. Wat hieronder staat komt van websites, bol-data en artikelen. Advies blijft: Joost zoekt één keer ingelogd op "leeskussen", "Ella Sleeps", "Q-Living", "CozySense" en "husband pillow" (land NL en BE, alle advertenties) en stuurt screenshots.

| Aanbieder | Prijs | Aanbod en hooks | Les voor Bline |
|---|---|---|---|
| **Ella Sleeps** (nr. 1 op bol) | €49,95, doorgestreept €55,95 (eigen site, 07-10-2026); bol €45,99 | "Stevige rugsteun die niet wegzakt", losse nekrol, 3 vakken, fluweel, 30 nachten proefslapen, gratis verzending NL/BE/DE/FR, Klarna 3 x €16,65, 93 reviews (95% vijf sterren) ([Ella Sleeps, 2026](https://ellasleeps.com/products/leeskussen)) | Zelfde kernbelofte ("blijft staan"). Bline moet het verschil laten zien: katoen in plaats van fluweel, wasbare hoes, 3,8 kg, vijf rustige kleuren. Niet op prijs concurreren. |
| **Q-Living** | €49,95 tot €54,95 (bol) | Nekrol, armleuningen, meerdere vakken, 7 kleuren; klacht "zit vrij rechtop", hoes niet in de machine (`markt_en_concurrenten.md`) | Wasbare hoes is een echt verschil; benoemen. |
| **CozySense, generieke bol-kussens** | €32 tot €45 | Lange titels met "ergonomisch", "orthopedisch", "CertiPUR", doorgestreepte "deal"-prijs | Bline mag die woorden niet gebruiken; dat is juist een kans om er rustiger en betrouwbaarder uit te zien. |
| **Ten Cate** | €80,88 (meestal €89,95) | Merk, "inclusief hoes", nette naden | Zelfde prijsband: kwaliteit en merk, niet korting. |
| **Husband Pillow** (VS) | $79,95 (van $119,95) | "Your comfort just got an upgrade", 101 nachten proberen, 3 jaar garantie, gratis verzending, 32 kleuren, verkoop gebouwd op scènes (lezen, voeden, ontspannen) ([husbandpillow.com, 2026](https://husbandpillow.com/)) | Lange proefperiode en veel kleuren als hoofdargument; doorgestreepte prijzen passen niet bij de ACM-regels. |
| **Linenspa** (VS) | ongeveer $50 | Shredded traagschuim, verschillende maten, in tests "comfortabelst" ([Your Best Digs](https://www.yourbestdigs.com/reviews/the-best-sit-up-pillow/)) | Shredded foam is gangbaar; het gewicht (3,8 kg) onderscheidt meer dan het woord "traagschuim". |
| **Milliard** (VS) | vanaf $24,99, 4,4 uit 3.279 reviews (Walmart) ([Walmart](https://www.walmart.com/c/kp/milliard-memory-foam)) | Prijs en reviewaantal | Laat zien hoe ver Bline van de bulkprijs zit: argument moet kwaliteit en gemak zijn. |
| **Cloudpillo** (NL, geen leeskussen) | Kussens €89 tot €125 | Permanent "1+1 gratis", 100 nachten, "4,5 uit 34.000 reviews" ([cloudpillo.com, 2026](https://cloudpillo.com/)); 15 tot 20 korte video's per week, vooral Instagram ([MT/Sprout](https://mtsprout.nl/groei/cloudpillo-hoofdkussen)); omzet €12,5 miljoen ([MT/Sprout](https://mtsprout.nl/nieuws/nieuws-startups-scaleups/omzet-cloudpillo-steeg-400-procent-jumbo-bekijkt-opties-voor-la-place)) | Groei komt uit veel korte, echte video's, niet uit gepolijste stilstaande beelden. Het permanente 1+1-model past niet bij Bline (marge en ACM). |

Conclusies:
1. Iedereen belooft "blijft staan" of "zakt niet weg". Bline wint niet met dezelfde zin, maar met het **laten zien** (video) en met **feiten die anderen niet hebben** (3,8 kg, katoenen hoes 400 TC, 30 °C, 5 rustige kleuren, 65 cm breed).
2. Proefperiode (30 tot 101 nachten) en gratis verzending zijn standaard. Ze horen in elke advertentie, maar zijn geen onderscheid.
3. Concurrenten werken met doorgestreepte prijzen; Bline kan dat niet en hoeft dat niet. Een echt voordeel (tweede hoes, tweede kussen) en een cadeau-invalshoek zijn de eerlijke vervanging.

---

## 6. Landingspagina en meting

### 6.1 Welke pagina per advertentie

- **Productpagina met de kleur die in beeld is** (`/products/leeskussen-<kleur>`), nooit de homepage of een collectie. Advertenties met meerdere kleuren: `/products/leeskussen-beige` (beige is de best verkochte kleur op bol, 19 van 65). Twee kussens: `?aantal=2`; extra hoes: `?hoes=1` (niet vooraf aangevinkt, dat mag niet volgens de ACM) (funnelplan hoofdstuk 1).
- **Prijs in advertentie = prijs op de pagina = prijs op bol.**
- Controleer vóór livegang of de kleurparameter ook werkt als Meta zijn eigen parameters (`fbclid`) toevoegt.

### 6.2 UTM

URL-parameters op advertentieniveau (Meta vult de waarden zelf in):

```
utm_source={{site_source_name}}&utm_medium=paid_social&utm_campaign={{campaign.name}}&utm_content={{ad.name}}&utm_term={{placement}}
```

Namen in kleine letters zonder spaties (zie hoofdstuk 8), zodat ze leesbaar in Shopify-rapporten staan.

### 6.3 Pixel en Conversions API: checklist vóór de eerste euro

| Nr | Wat | Klaar als |
|---|---|---|
| 1 | Shopify Facebook & Instagram-app gekoppeld aan het juiste Business-account, pixel en catalogus | Pixel-id in Events Manager is die van Bline, niet van uwleeskussen.nl |
| 2 | Gegevensdeling op **Maximaal** (pixel plus Conversions API) ([Shopify Help](https://help.shopify.com/en/manual/promoting-marketing/analyze-marketing/meta-data-sharing)) | Events Manager toont "Browser en server" bij Purchase |
| 3 | Testbestelling (echte betaling, daarna terugboeken) | 1 Purchase, juiste waarde incl. btw, valuta EUR, niet dubbel (deduplicatie via event-id) |
| 4 | ViewContent, AddToCart, InitiateCheckout komen binnen | Alle drie zichtbaar met kleurvariant als content_id |
| 5 | Kwaliteit van gekoppelde gegevens (Event Match Quality) bij Purchase | 6 of hoger |
| 6 | Domein `blinesleep.nl` geverifieerd in Business-instellingen | Groen vinkje (aanbevolen, niet verplicht) |
| 7 | Attributie in de advertentieset | 7 dagen klik, 1 dag engage, 1 dag view (standaard) |
| 8 | Cookiebanner aan voor EER, gelijkwaardige knoppen "accepteren" en "weigeren" | Banner zichtbaar in NL en BE (incognito getest) |

### 6.4 Toestemming (cookiebanner) en wat dat met meting doet

- Shopify toont de banner standaard aan bezoekers in de EER; niet-noodzakelijke gegevens worden pas na toestemming verzameld en "pixels werken op basis van de toestemming in deze regio's" ([Shopify Help](https://help.shopify.com/en/manual/privacy-and-security/privacy/customer-privacy-settings/privacy-settings)).
- In NL geeft gemiddeld ongeveer 42% toestemming voor marketingcookies (Cookiebot-benchmark 2026, via [Searchlab](https://searchlab.nl/statistieken/privacy-avg-statistieken-nederland-2026); secundaire bron).
- **Gevolg** [Inschatting]: Meta ziet mogelijk maar 40 tot 70% van de echte aankopen. Meta's eigen kosten per aankoop lijkt dan hoger dan in werkelijkheid, en Meta leert trager.
- **Daarom wekelijks zelf rekenen:** Meta-uitgave gedeeld door (Shopify-orders met `utm_medium=paid_social` plus de stijging in "direct" en merkzoekverkeer ten opzichte van de week vóór de start). Gebruik dat "totaalgetal" voor de stopregels, niet alleen Meta's getal.
- Les van Piedi Nudi: daar werkte de conversiemeting niet en liep het geld naar de eigen merknaam. Bij Meta is het gelijkwaardige risico: zonder werkende Purchase optimaliseert Meta op niets. Punt 3 van de checklist is daarom een harde voorwaarde.

---

## 7. Seizoen en timing (Q4 2026)

### 7.1 Kalender

| Periode | Wat er gebeurt | Wat Bline doet |
|---|---|---|
| Nu tot 15 oktober | Meta adviseert "start ads by mid-October to let Meta learn before the peak" ([Social Media Today over Meta's tips, augustus 2026](https://www.socialmediatoday.com/news/meta-shares-holiday-2026-tips-for-small-businesses/826785/)) | Meting rond, golf 1 (6 advertenties) live, zo dicht mogelijk bij 15 oktober |
| 15 oktober tot 15 november | "Ontdekfase" in Meta's playbook ([Relevant Audience, 2026](https://www.relevantaudience.com/meta/meta-holiday-playbook-four-phases-q4/)) | Golf 2 rond 25 oktober; €10 per dag houden of naar €12 bij kosten per aankoop onder €25 |
| 16 tot 26 november | Sinterklaas-zoekgedrag piekt in de laatste weken van november ([Keurigonline, 2025](https://www.keurigonline.nl/blog/google-zoek-trends-2025-in-nederland)) | Golf 3 (cadeau) live |
| 27 november (Black Friday) tot 30 november (Cyber Monday) | CPM in de Black Friday-week 2 tot 3 keer het jaargemiddelde; Q4-CPM 25 tot 50% hoger dan Q2-Q3 ([Common Thread over Meta's Holiday Insights, 2026](https://commonthreadco.com/blogs/coachs-corner/meta-holiday-insights-center-2026-q4-ecommerce)). Aankopen spreiden zich over heel november ("Black November") ([NIQ, 2025](https://nielseniq.com/global/nl/news-center/2025/black-friday-is-uit-black-november-is-in/)) | Budget niet verhogen tenzij de kosten per aankoop in de week ervoor onder €25 lagen. Geen nepactie. |
| 1 tot 3 december | Laatste besteldagen Sinterklaas | Cadeau-advertentie met echte deadline |
| 5 december (za, NL) en 6 december (zo, Sint-Niklaas in Vlaanderen) | | Na 3 december Sinterklaas-advertentie pauzeren |
| 7 tot 21 december | Kerst-piek, half december ongeveer zo groot als het Black Friday-weekend op bol ([Boloo](https://www.boloo.co/bibliotheek/de-bol-com-piekmaanden-een-guide-voor-bol-com-verkopers)) | Kerstadvertentie met besteldeadline |
| 22 december tot januari | "Fresh start" | Terug naar de beste 3 vaste advertenties; januari is rustig |

**Besteldeadlines** [Inschatting, eerst met ChannelDock en de vervoerder bevestigen]: bij 1 tot 2 werkdagen levering: voor 5 december in NL uiterlijk **woensdag 2 december** bestellen (veilig) of donderdag 3 december vóór de afhaaltijd; voor 6 december in België dezelfde dagen (zondag wordt niet bezorgd). Voor Kerst (vrijdag 25 december): uiterlijk **maandag 21 december**. Alleen een deadline noemen als die klopt; dat is informatie, geen nep-urgentie.

### 7.2 Q4 benutten zonder nepkorting

- **Wat mag:** een echte, nieuwe actie met een "van"-prijs die de laagste prijs van de afgelopen 30 dagen is ([ACM](https://www.acm.nl/nl/publicaties/acm-wil-einde-aan-nepkortingen-na-komst-strengere-regels)); volume-aanbiedingen (2 kussens) en extra's vallen buiten de 30-dagenregel maar moeten waar zijn ([Europese Commissie](https://commission.europa.eu/law/law-topic/consumer-protection-law/unfair-commercial-practices-law/price-indication-directive_en)). De ACM vond in 2025 bij 75% van de onderzochte winkels misleidende kortingen ([NOS, 2025](https://nos.nl/l/2591200)).
- **Voor Bline:**
  1. Cadeau-invalshoek in plaats van korting (A11, A12).
  2. Bestaande voordelen als "cadeauset": twee kussens €149,99 (€9,99 voordeel), kussen plus extra hoes (€9,99 voordeel op de hoes). Die gelden permanent en moeten ook op bol gelden (afspraak: prijzen gelijk aan bol).
  3. Een echte Black Friday-actie alleen als die ook op bol loopt en de "van"-prijs klopt. Op bol telt de "meestal"-prijs over 90 dagen (`markt_en_concurrenten.md`). Advies: geen Black Friday-korting; het levert bij €34 marge weinig op en het merk staat nog niet.
  4. Welkomstcode van 10% (Klaviyo): niet in advertenties noemen in de eerste 6 weken. Het verlaagt de marge naar ongeveer €26 per kussen en trekt kortingzoekers. Pas testen als er 10+ aankopen via Meta zijn [Inschatting].
- **Voorraad:** bij een versnelling in december bewaken dat beige hoezen (43 stuks op 27-09) niet op raken (`interne_data_en_scenarios.md`). Een kleur die bijna op is uit de advertenties halen.

---

## 8. Advies: campagne-opzet

| Niveau | Naam | Instelling |
|---|---|---|
| Campagne | `bl_sales_nlbe` | Advantage+ verkoopcampagne; doel Verkoop; campagnebudget €10 per dag; geen biedlimiet (hoogste volume); start uiterlijk 15 oktober |
| Advertentieset | `bl_nl-vl_adv-aud` | Conversielocatie website; prestatiedoel: aantal conversies maximaliseren; event **Purchase**; locatie NL + 5 Vlaamse provincies; minimumleeftijd 25; taal Nederlands; Advantage+ doelgroep (optioneel suggestie 30-65); Advantage+ plaatsingen zonder Audience Network; attributie standaard |
| Advertenties | `bl_a01_demo-video` tot `bl_a14_postit` | Zie hoofdstuk 9. Advantage+ creative: alleen "relevante opmerkingen" en "aanpassen aan plaatsing" (zonder bijsnijden van tekst) aan; alle generatieve opties uit; lijst beperkte woorden ingevuld |
| Later (niet nu) | `bl_retarget_nlbe` | Alleen bij 1.000+ bezoekers per 30 dagen of €20+ per dag totaal; €3 per dag; A10 en A13 |

**Budgetverloop** [Inschatting]:

| Periode | Per dag | Totaal | Voorwaarde |
|---|---|---|---|
| Dag 1 tot 15 (vooraf betaald) | €10 | €150 | Meting werkt |
| Dag 16 tot 30 | €10 (of €12) | €150 tot €180 | €12 alleen bij kosten per aankoop onder €25 met 4+ aankopen |
| 16 tot 26 november | €10 tot €15 | | Golf 3 live; maximaal +20% per week |
| Black Friday-week | gelijk houden | | CPM hoog |
| 1 tot 21 december | €10 tot €15 | | Kerst; daarna terug naar €10 |

---

## 9. De nieuwe advertentieset (14 advertenties)

### 9.1 Huisstijl voor alle advertenties

- **Canvas:** feed 1080 x 1350 (4:5), Reels/Stories 1080 x 1920 (9:16), carrousel 1080 x 1080. Elke statische advertentie in 4:5 en 9:16 aanleveren; in Meta per plaatsing het juiste formaat koppelen.
- **Letters:** Poppins Bold (koppen), Poppins Regular (ondersteunend), Poppins Medium (badges). Kop 72 tot 96 px, regelafstand 1,05, letterafstand -1%. Ondersteunend 36 tot 40 px. Niets kleiner dan 30 px.
- **Kleuren:** Nacht `#1F2A37`, Terracotta `#C4623E`, Salie `#7C8B74`, Mist `#E5EAF2`, Zand `#F2EADF`, Wit `#FFFFFF`, Ster `#E8A317`. Per advertentie één achtergrondkleur en hoogstens één accent.
- **Logo:** 44 px hoog, linksonder in 4:5 (x 60, y 1250), in 9:16 linksboven binnen de veilige zone (x 65, y 290) of weglaten.
- **Badge-stijl:** afgeronde balk (radius 999), padding 18 x 28 px, Poppins Medium 32 px.
- **Bijsnijden:** alleen uitsnijden en schalen; geen inkleuren, geen montage van twee scènes in één foto, geen AI-uitbreiding. Bij 9:16 van een vierkant origineel: beeld schalen tot 1920 hoog en midden kiezen, of het vierkant op een effen kleurvlak zetten.
- **Bestandsnamen:** `bline-meta-a01-demo-916.mp4`, `bline-meta-a02-stapel-45.jpg` enzovoort.

### 9.2 Overzicht

| Nr | Naam | Format | Golf | Persoon / omgeving / voordeel | Landing |
|---|---|---|---|---|---|
| A01 | `bl_a01_demo-video` | Video 9:16 + 4:5, 15 s | 1 | Productvideo / slaapkamer / blijft staan, vak, hoes | `/products/leeskussen-wit` |
| A02 | `bl_a02_stapel-vs-bline` | Statisch 4:5 + 9:16 | 1 | Man 50 / avond / probleem-oplossing | `/products/leeskussen-blauw` |
| A03 | `bl_a03_uitleg-lijntjes` | Statisch 4:5 + 9:16 | 1 | Geen persoon / packshot / waarom €80 | `/products/leeskussen-beige` |
| A04 | `bl_a04_werken-native` | Statisch 4:5 + 9:16, native | 1 | Echte vrouw / laptop / werken | `/products/leeskussen-wit` |
| A05 | `bl_a05_bank` | Statisch 4:5 + 9:16 | 1 | Vrouw 65 / bank / nieuwe plek | `/products/leeskussen-zwart` |
| A06 | `bl_a06_carrousel-kleur-moment` | Carrousel 6 kaarten | 1 | 5 personen / 5 kamers / kleurkeuze | per kaart de kleur |
| A07 | `bl_a07_ugc-stapel` | Video 9:16, 18 s, telefoon | 2 | Echte handen / echte slaapkamer / probleem tegen oplossing | `/products/leeskussen-beige` |
| A08 | `bl_a08_kleuren-slideshow` | Video 9:16 + 4:5, 8 s | 2 | Packshots / 5 kleuren | `/products/leeskussen-beige` |
| A09 | `bl_a09_maat-op-bed` | Statisch 4:5 + 9:16 | 2 | Maattekening / bed / maatbezwaar | `/products/leeskussen-wit` |
| A10 | `bl_a10_30-dagen` | Statisch 4:5 + 9:16, aanbod eerst | 2 | Packshot / risico weg | `/products/leeskussen-grijs` |
| A11 | `bl_a11_sinterklaas` | Statisch 4:5 + 9:16 | 3 (16 nov tot 3 dec) | Tiener / gamen / cadeau | `/products/leeskussen-zwart` |
| A12 | `bl_a12_kerst` | Statisch 4:5 + 9:16 | 3 (4 tot 21 dec) | Man / avondlamp / cadeau | `/products/leeskussen-blauw` |
| A13 | `bl_a13_twee-kussens` | Statisch 4:5 + 9:16, split screen | 3 | Twee personen / samen / bundel | `/products/leeskussen-beige?aantal=2` |
| A14 | `bl_a14_postit` | Statisch 4:5, lo-fi | 2 | Vrouw 35 / lezen / gewoonte | `/products/leeskussen-beige` |

Golf 1 = livegang (6 advertenties). Golf 2 = dag 10 tot 14 (A07 zodra opgenomen, A08, A09, A10, A14; samen 5, kies de 4 die als eerste klaar zijn). Golf 3 = vanaf 16 november.

### 9.3 Per advertentie

Elke advertentie krijgt de UTM uit 6.2 en de knop **Nu kopen**.

---

#### A01 `bl_a01_demo-video`: "Leun er gerust tegenaan"

- **Format:** video, 9:16 (1080 x 1920) en 4:5 (1080 x 1350), 15 seconden, ingebrande ondertitels, zonder muziek met tekst of met rustige muziek zonder zang.
- **Basis:** de bestaande productvideo (Shopify Files, "video leeskussen.mp4", 1080 x 1080, 25 s). Ik kon die video hier niet bekijken (staat niet in de repository); de montage hieronder gaat uit van de scènes die in de eerdere teksten staan (leunen, telefoon in het vak, hoes eraf). De monteur kiest de exacte tijdcodes.
- **Montage (9:16):** effen Nacht-achtergrond `#1F2A37`. Video geschaald naar 960 x 960, x 60, y 300 tot 1260. Kop boven de video op y 300 tot 360 is te krap; zet de koptekst daarom **in** de video, bovenin (y 330 tot 430), wit, Poppins Bold 64 px, met een zachte schaduw.
  - 0,0 tot 1,5 s: het moment van achteroverleunen (de beweging moet direct in beeld zijn, geen logo, geen fade-in). Tekst: **"Leun er gerust tegenaan."**
  - 1,5 tot 5 s: kussen staat, persoon zit rechtop. Tekst: **"Hij blijft staan."**
  - 5 tot 8 s: telefoon gaat in het zijvak. Tekst: **"Telefoon in het vak."**
  - 8 tot 12 s: rits open, hoes eraf. Tekst: **"Hoes eraf, in de was op 30 °C."**
  - 12 tot 15 s: eindbeeld: kussen in rust, logo wit 56 px midden, eronder **"Gratis verzending in NL en BE · 30 dagen proberen"** (Poppins Regular 34 px, wit). Alles boven y 1248.
- **4:5-versie:** video 1080 x 1080 op y 135 tot 1215, Nacht-band boven (0 tot 135) en onder (1215 tot 1350) leeg, dezelfde teksten in de video.
- **Primaire tekst (kort):** Eén kussen dat blijft staan als je ertegenaan leunt.
- **Primaire tekst (middel):**
  > Eén kussen dat blijft staan als je ertegenaan leunt.
  > 3,8 kg traagschuim in stukjes, een vak voor je telefoon en een katoenen hoes die eraf kan en in de was op 30 °C.
  > Wit leeskussen, €69,99. Gratis verzending in Nederland en België, 30 dagen proberen.
- **Extra varianten:** hook 2, hook 5, hook 13 uit 3.2.
- **Kop:** Zie hoe hij blijft staan · **Beschrijving:** Wit, €69,99
- **Landing:** `https://www.blinesleep.nl/products/leeskussen-wit`

---

#### A02 `bl_a02_stapel-vs-bline`: kussenstapel tegen Bline

- **Format:** statisch 4:5 en 9:16, "wij tegen zij" (vergelijkingskaart).
- **Basis:** H-blauw04 (`beelden_higgsfield/blauw_04_b6493bcc.png`).
- **Layout 4:5:**
  - Bovenste 52% (y 0 tot 700): foto, uitsnede 2048 x 1327 vanaf y 260 van het origineel (man en kussen, lamp rechts boven in beeld), geschaald naar 1080 x 700. Het kussen moet volledig in beeld zijn.
  - Onderste 48% (y 700 tot 1350): Wit vlak met een tabel van twee kolommen, 60 px marge.
    - Kolomkoppen op y 740: links **"Kussens stapelen"** (Poppins Medium 34 px, grijs `#6E7581`), rechts **"Bline leeskussen"** (Poppins Bold 34 px, Nacht). Rechterkolom heeft een lichte Mist-achtergrond `#E5EAF2`, afgeronde hoeken 24 px, zodat het oog daar landt.
    - Vier rijen, 34 px, regelafstand 1,25, scheidingslijn `#E3DACB`:
      1. "Schuiven weg als je leunt" | "Blijft staan: 3,8 kg traagschuim"
      2. "Telefoon ergens in het dekbed" | "Vak aan de zijkant"
      3. "Elke avond opnieuw opbouwen" | "Neerzetten en klaar"
      4. "Kussenslopen vol vlekken" | "Hoes eraf, wassen op 30 °C"
    - Links per rij een klein grijs streepje, rechts een terracotta stip (`#C4623E`, 14 px). Geen vinkjes.
  - Kop over de foto, linksboven (x 60, y 60): **"Drie kussens of één die blijft staan?"** wit, Poppins Bold 72 px, twee regels, op een zachte donkere gradient (Nacht 0% naar 45% van boven naar beneden, alleen bovenste 260 px).
  - Logo wit, rechtsboven op de foto (x 960, y 60, rechts uitgelijnd).
- **Layout 9:16:** foto y 0 tot 1000 (uitsnede 2048 x 1896 schalen naar 1080 x 1000), kop op y 290 tot 450; tabel y 1000 tot 1248 met alleen rij 1 en 2 (de rest valt in de dode zone). Onder y 1248 alleen Wit vlak.
- **Primaire tekst (kort):** Drie kussens achter je rug en na tien minuten lig je weer half plat.
- **Primaire tekst (middel):**
  > Drie kussens achter je rug en na tien minuten lig je weer half plat.
  > Bline is één wigvormig kussen van 3,8 kg traagschuim. Het blijft staan als je leunt, heeft een vak voor je telefoon en een hoes die in de was kan.
  > €79,99 in blauw, beige, grijs of zwart. Gratis verzending in Nederland en België, 30 dagen proberen.
- **Extra varianten:** hook 13, hook 3.
- **Kop:** Eén kussen in plaats van drie · **Beschrijving:** Gratis verzending NL en BE
- **Landing:** `https://www.blinesleep.nl/products/leeskussen-blauw`

---

#### A03 `bl_a03_uitleg-lijntjes`: productuitleg met lijntjes

- **Format:** statisch 4:5 en 9:16, "annotated product".
- **Basis:** H-beige07 (`beelden_higgsfield/beige_07_08c2e4d1.png`), het beige kussen op bed met boek.
- **Layout 4:5:** achtergrond Salie `#7C8B74` volledig. Foto als afgerond vlak (radius 32 px) van 960 x 960 op x 60, y 290; uitsnede: het hele kussen plus boek, kussen gecentreerd.
  - Kop op Salie, x 60, y 70: **"Een rugleuning voor je bed."** wit, Poppins Bold 80 px, één of twee regels.
  - Vier labels in witte afgeronde badges (Poppins Medium 30 px, Nacht tekst), elk met een witte lijn van 3 px naar het product:
    1. Linksboven bij de schuine voorkant: **"3,8 kg traagschuim in stukjes"**
    2. Rechts halverwege bij de zijkant: **"Vak voor je telefoon"** (lijn naar het zijpaneel)
    3. Linksonder bij de naad: **"Katoenen hoes, rits, 30 °C"**
    4. Onder het kussen een maatlijn met pijltjes over de volle breedte van het kussen, met badge **"65 cm breed"**
  - Logo wit linksonder (x 60, y 1270).
- **Layout 9:16:** zelfde, Salie-achtergrond; kop y 290 tot 470; foto 960 x 960 op y 500 tot 1460 (onderste deel van de foto valt in de dode zone, dus maatlijn en badge 4 op y ≤ 1240 zetten, net onder het kussen); badges binnen x 65 tot 1015.
- **Primaire tekst (kort):** Je bed heeft geen rugleuning. Dit is er één.
- **Primaire tekst (middel):**
  > Je bed heeft geen rugleuning. Dit is er één.
  > Wat je krijgt voor €79,99: 3,8 kg traagschuim in stukjes, zodat hij blijft staan. Een vak voor je telefoon. Een hoes van katoen (400 TC) met rits, wasbaar op 30 °C. 65 x 50 x 45 cm.
  > Vijf kleuren. Gratis verzending in Nederland en België, 1 tot 2 werkdagen.
- **Extra varianten:** hook 5, hook 14.
- **Kop:** Wat zit erin, wat krijg je · **Beschrijving:** Beige, €79,99
- **Landing:** `https://www.blinesleep.nl/products/leeskussen-beige`

---

#### A04 `bl_a04_werken-native`: "Laptop op schoot, rug tegen iets stevigs"

- **Format:** statisch 4:5 en 9:16, platform-native (ziet eruit als een gewone Instagram-story).
- **Basis:** B-wit07 (`beelden_bol/wit_07_1200.jpg`), de echte shoot. Waar mogelijk de originele DSC-foto uit Shopify Files in volle resolutie gebruiken.
- **Layout 4:5:** foto volledig, uitsnede 960 x 1200 uit het 1200 x 1200 origineel (x 120 tot 1080, hele hoogte), geschaald naar 1080 x 1350. Geen kaders, geen kleurvlakken.
  - Eén tekstregel in Instagram-stijl: witte afgeronde balk (radius 16 px) met Nacht tekst, Poppins Medium 40 px, gecentreerd op y 160: **"thuiswerken vanuit bed, maar dan rechtop"** (kleine letters, zoals een echte story).
  - Rechtsonder klein (x 1020, y 1290, rechts uitgelijnd), wit met schaduw, Poppins Regular 28 px: "bline leeskussen · wit". Geen logo.
- **Layout 9:16:** foto geschaald tot 1920 hoog, horizontaal gecentreerd op de vrouw; tekstbalk op y 380.
- **Primaire tekst (kort):** Laptop op schoot, rug tegen iets stevigs.
- **Primaire tekst (middel):**
  > Laptop op schoot, rug tegen iets stevigs.
  > Voor de avonden dat je nog even iets afmaakt in bed. Bline blijft staan, je telefoon zit in het vak aan de zijkant en de hoes gaat in de was.
  > Wit leeskussen €69,99. Gratis verzending in Nederland en België.
- **Extra varianten:** hook 6, hook 4.
- **Kop:** Rechtop in bed, zonder kussenberg · **Beschrijving:** Wit, €69,99
- **Landing:** `https://www.blinesleep.nl/products/leeskussen-wit`

---

#### A05 `bl_a05_bank`: "Niet alleen voor in bed"

- **Format:** statisch 4:5 en 9:16.
- **Basis:** H-zwart02 (`beelden_higgsfield/zwart_02_7f568477.png`), vrouw op grijze bank met zwart kussen.
- **Layout 4:5:** achtergrond Zand `#F2EADF`. Foto 1080 x 1080 onderaan (y 270 tot 1350), uitsnede: vrouw en het hele kussen, bank tot de linkerrand.
  - Bovenste band (y 0 tot 270), Zand: kop x 60, y 70: **"Niet alleen voor in bed."** Nacht, Poppins Bold 80 px. Daaronder (y 190) Poppins Regular 36 px, `#3D4856`: "Ook op de bank: rechtop met je boek."
  - Logo Nacht rechtsboven (x 1020, y 80, rechts uitgelijnd).
- **Layout 9:16:** Zand-achtergrond; kop en regel op y 290 tot 500; foto 1080 x 1080 op y 520 tot 1600. Belangrijkste deel (gezicht, kussen) boven y 1248.
- **Primaire tekst (kort):** Niet alleen voor in bed: ook op de bank.
- **Primaire tekst (middel):**
  > Niet alleen voor in bed: ook op de bank.
  > Zet Bline tegen de leuning en je zit rechtop met je boek, zonder dat er kussens wegglijden. 3,8 kg traagschuim, een vak voor je telefoon en een katoenen hoes die in de was kan.
  > Zwart leeskussen €79,99. Gratis verzending in Nederland en België, 30 dagen proberen.
- **Extra varianten:** hook 10, hook 2.
- **Kop:** In bed en op de bank · **Beschrijving:** Zwart, €79,99
- **Landing:** `https://www.blinesleep.nl/products/leeskussen-zwart`

---

#### A06 `bl_a06_carrousel-kleur-moment`: "Kies je kleur, kies je moment"

- **Format:** carrousel, 6 kaarten 1080 x 1080. Elke kaart een andere persoon en kamer.
- **Kaartopbouw (1 tot 5):** foto vierkant volledig. Linksonder (x 50, y 960) een witte afgeronde badge, Poppins Medium 32 px, Nacht: kleur en moment. Geen andere tekst.

| Kaart | Bron | Uitsnede | Badge | Kop (Meta) | Beschrijving | Link |
|---|---|---|---|---|---|---|
| 1 | H-beige04 `beelden_higgsfield/beige_04_9d9bf3d0.png` | volledig | Beige · zondagochtend | Beige | €79,99 | `/products/leeskussen-beige` |
| 2 | H-blauw04 `beelden_higgsfield/blauw_04_b6493bcc.png` | volledig | Blauw · laatste hoofdstuk | Blauw | €79,99 | `/products/leeskussen-blauw` |
| 3 | H-grijs04 `beelden_higgsfield/grijs_04_e88bcb0c.png` | volledig | Grijs · nog even mailen | Grijs | €79,99 | `/products/leeskussen-grijs` |
| 4 | H-zwart03 `beelden_higgsfield/zwart_03_8a600508.png` | volledig | Zwart · gamen | Zwart | €79,99 | `/products/leeskussen-zwart` |
| 5 | H-wit06 `beelden_higgsfield/wit_06_dd51760c.png` | volledig | Wit · op de bank | Wit | €69,99 | `/products/leeskussen-wit` |
| 6 | Vijf packshots (zie A08) | 2 rijen: 3 boven, 2 onder, elk 320 x 320 met 20 px tussenruimte, op Mist `#E5EAF2` | Kop bovenaan Poppins Bold 64 px: **"Zelfde kussen, vijf kleuren."** | Vergelijk de kleuren | Gratis verzending | `/products/leeskussen-beige` |

- **Controle vooraf:** grijs_04 toont een lichter grijs dan het echte grijze kussen. Leg naast de echte hoes; wijkt het zichtbaar af, gebruik dan H-grijs03 (`grijs_03_3470a6af.png`) voor kaart 3 met badge "Grijs · laptop op schoot".
- **Primaire tekst (kort):** Zelfde kussen, vijf kleuren. Welke past bij jouw bed?
- **Primaire tekst (middel):**
  > Zelfde kussen, vijf kleuren. Welke past bij jouw bed?
  > Elk Bline-kussen heeft 3,8 kg traagschuim, een vak voor je telefoon en een katoenen hoes met rits die in de was kan. Wit €69,99, de andere kleuren €79,99.
  > Gratis verzending in Nederland en België.
- **Instelling:** "Beste kaarten automatisch eerst tonen" aan; laatste kaart met link naar de site uit (kaart 6 doet dat al).

---

#### A07 `bl_a07_ugc-stapel`: telefoonvideo "Elke avond hetzelfde"

- **Format:** video 9:16, 18 seconden, gefilmd met een telefoon in een echte slaapkamer, daglicht, geen studio. Geen gezicht nodig (handen, romp, bed). **Nieuw materiaal** (zie hoofdstuk 11).
- **Script (tekst op beeld, Poppins Bold 60 px wit met zwarte rand of Instagram-tekstbalk, y 330 tot 450):**
  - 0,0 tot 2,5 s: drie gewone kussens tegen het hoofdeinde. Iemand gaat zitten en leunt; de kussens schuiven weg. Tekst: **"Elke avond hetzelfde."**
  - 2,5 tot 4,5 s: de kussens worden van het bed geveegd. Tekst: **"Weg ermee."**
  - 4,5 tot 7 s: Bline (beige) wordt neergezet. Tekst: **"Eén kussen."**
  - 7 tot 10 s: leunen, kussen houdt zijn vorm; hand drukt in de schuine kant en het veert terug. Tekst: **"Blijft staan."**
  - 10 tot 12,5 s: telefoon in het zijvak. Tekst: **"Telefoon erin."**
  - 12,5 tot 15 s: rits half open, traagschuim zichtbaar. Tekst: **"3,8 kg traagschuim."**
  - 15 tot 18 s: rustig eindbeeld van het kussen op bed met boek. Tekst: **"Gratis verzending NL en BE · 30 dagen proberen"**, klein logo boven y 1248.
- **Geluid:** omgevingsgeluid (het ploffen van kussens werkt) plus ondertitels; geen voice-over nodig.
- **Primaire tekst (kort):** Elke avond je kussens opbouwen? Eén keer neerzetten is genoeg.
- **Primaire tekst (middel):**
  > Elke avond je kussens opbouwen? Eén keer neerzetten is genoeg.
  > Bline is een wigvormig leeskussen met 3,8 kg traagschuim. Leun ertegenaan en hij blijft staan. Telefoon in het vak, hoes in de was.
  > Beige €79,99. Gratis verzending in Nederland en België, 30 dagen proberen.
- **Kop:** Kussens stapelen is voorbij · **Beschrijving:** Beige, €79,99
- **Landing:** `https://www.blinesleep.nl/products/leeskussen-beige`

---

#### A08 `bl_a08_kleuren-slideshow`: "Vijf kleuren in acht seconden"

- **Format:** video 9:16 en 4:5, 8 seconden, gemaakt van bestaande packshots (snelle wissels, geen effecten behalve een korte zoom van 100% naar 104% per beeld).
- **Beelden (in deze volgorde, elk 1,3 s):** `beelden_bol/wit_05_1200.jpg`, `beelden_higgsfield/beige_07_08c2e4d1.png`, `beelden_higgsfield/blauw_05_2a75b663.png`, `beelden_higgsfield/grijs_05_e0126ef9.png`, `beelden_higgsfield/zwart_05_fe50e2b8.png`; daarna 1,5 s eindbeeld.
- **Layout 9:16:** packshot 1080 x 1080 op y 420 tot 1500 (kussen gecentreerd, boek mag mee); boven (y 290) de kleurnaam groot, Poppins Bold 96 px, Nacht op Mist `#E5EAF2`-achtergrond die per kleur wisselt: Wit → Mist, Beige → Zand, Blauw → Mist, Grijs → `#ECEAE6`, Zwart → Zand. Onder de naam (y 410) de prijs, Poppins Regular 40 px: "€69,99" bij wit, "€79,99" bij de rest.
- **Eindbeeld:** Nacht-achtergrond, vijf kleine packshots op een rij (elk 180 x 180), kop wit Poppins Bold 64 px: **"Welke past bij jouw bed?"**, regel 34 px: "Gratis verzending NL en BE".
- **4:5:** zelfde, packshot 1080 x 1080 op y 270 tot 1350, naam en prijs in de band erboven.
- **Primaire tekst (kort):** Zelfde kussen, vijf kleuren.
- **Primaire tekst (middel):**
  > Zelfde kussen, vijf kleuren: wit, beige, blauw, grijs en zwart.
  > 3,8 kg traagschuim, vak voor je telefoon, katoenen hoes die in de was kan. Gratis verzending in Nederland en België.
- **Kop:** Kies je kleur · **Beschrijving:** Wit €69,99, rest €79,99
- **Landing:** `https://www.blinesleep.nl/products/leeskussen-beige`

---

#### A09 `bl_a09_maat-op-bed`: "65 cm. Er blijft genoeg bed over."

- **Format:** statisch 4:5 en 9:16, uitlegbeeld.
- **Basis:** B-wit11 (`beelden_bol/wit_11_1200.jpg`, maattekening) en `beelden_bewerkt/bline-maatgids-bedden-01.jpg` (bovenaanzicht 140/160/180).
- **Layout 4:5:** achtergrond Wit.
  - Kop x 60, y 60: **"65 cm breed."** Nacht, Poppins Bold 88 px; tweede regel Terracotta `#C4623E`, Poppins Bold 64 px: **"Er blijft genoeg bed over."**
  - Midden (y 300 tot 860): maattekening wit_11, 760 x 560, gecentreerd. De bestaande tekst "Traagschuim Vulling" in die tekening wegsnijden (bovenste 18% van het beeld) zodat alleen kussen en maatlijnen overblijven.
  - Onder (y 900 tot 1240): de drie bedden uit de maatgids als drie simpele rechthoeken (lijn 3 px Nacht), elk met het kussen als Zand-vlak van 65 cm op schaal en eronder Poppins Medium 30 px: "140 cm: 75 cm over", "160 cm: 95 cm over", "180 cm: 115 cm over". Liever opnieuw tekenen dan de bestaande afbeelding verkleinen (te kleine letters).
  - Logo Nacht linksonder (x 60, y 1280).
- **Layout 9:16:** kop y 290 tot 470, tekening y 500 tot 900, bedden y 920 tot 1240.
- **Primaire tekst (kort):** 65 cm breed. Op een bed van 160 blijft er 95 cm over.
- **Primaire tekst (middel):**
  > 65 cm breed. Op een bed van 160 blijft er 95 cm over.
  > Bline is 65 cm breed, 50 cm hoog en 45 cm diep. Groot genoeg om tegenaan te leunen, klein genoeg om naast iemand te liggen die al slaapt.
  > Wit €69,99. Gratis verzending in Nederland en België, 30 dagen proberen.
- **Kop:** Past op je bed, ook met z'n tweeën · **Beschrijving:** 65 x 50 x 45 cm
- **Landing:** `https://www.blinesleep.nl/products/leeskussen-wit`

---

#### A10 `bl_a10_30-dagen`: "30 dagen proberen. In je eigen bed."

- **Format:** statisch 4:5 en 9:16, "aanbod eerst" (offer-first banner, zonder korting).
- **Basis:** grijze packshot H-grijs05 (`beelden_higgsfield/grijs_05_e0126ef9.png`).
- **Layout 4:5:** achtergrond Terracotta `#C4623E` op de bovenste 45% (y 0 tot 610), Zand `#F2EADF` daaronder.
  - Op Terracotta, x 60, y 70: **"30 dagen proberen."** wit, Poppins Bold 96 px; regel 2 (y 190) wit Poppins Bold 72 px: **"In je eigen bed."**
  - Daaronder (y 320) twee witte badges naast elkaar met Terracotta tekst, Poppins Medium 32 px: "Gratis verzending NL en BE" en "In 1 tot 2 werkdagen".
  - Packshot als afgerond vlak (radius 32 px) 860 x 860, gecentreerd, y 440 tot 1300, half over de kleurgrens (dat geeft diepte).
  - Logo Nacht linksonder (x 60, y 1290) mag weg als het botst met de foto.
- **Layout 9:16:** Terracotta y 0 tot 900 met kop op y 290 tot 520 en badges op y 560; packshot 860 x 860 op y 620 tot 1480 (kussen zelf boven y 1248).
- **Let op:** retour is op eigen kosten (funnelplan); dus niet "gratis retour" schrijven. Als Joost besluit gratis retour in te voeren, kan dat in de badge.
- **Primaire tekst (kort):** Probeer hem 30 dagen in je eigen bed.
- **Primaire tekst (middel):**
  > Probeer hem 30 dagen in je eigen bed.
  > Past hij niet bij je, dan stuur je hem binnen 30 dagen terug. Bline leeskussen: 3,8 kg traagschuim, vak voor je telefoon, katoenen hoes die in de was kan.
  > Grijs €79,99. Gratis verzending in Nederland en België, in 1 tot 2 werkdagen in huis.
- **Kop:** 30 dagen proberen · **Beschrijving:** Grijs, €79,99
- **Landing:** `https://www.blinesleep.nl/products/leeskussen-grijs`

---

#### A11 `bl_a11_sinterklaas`: cadeau voor de gamer of student

- **Format:** statisch 4:5 en 9:16. Live 16 november tot en met de echte laatste besteldag (naar verwachting 2 of 3 december).
- **Basis:** H-zwart03 (`beelden_higgsfield/zwart_03_8a600508.png`).
- **Layout 4:5:** foto volledig 1080 x 1350, uitsnede 1638 x 2048 midden uit het origineel (tiener, kussen en schermlicht in beeld).
  - Bovenaan een Nacht-gradient (0 tot 360 px). Kop x 60, y 70, wit, Poppins Bold 76 px: **"Cadeau voor wie altijd 'nog even' in bed zit."**
  - Onderaan een witte afgeronde balk (x 60, y 1180, breedte 960, hoogte 100), Nacht tekst Poppins Medium 34 px: **"Voor 5 december in huis: bestel uiterlijk 2 december"** (datum pas invullen na bevestiging door ChannelDock).
  - Geen Sinterklaas-figuur, geen pakjes (geen nieuw beeld nodig).
- **Layout 9:16:** foto geschaald tot 1920 hoog; kop y 290 tot 500; balk met datum op y 1120 tot 1220.
- **Primaire tekst (kort):** Cadeau voor wie elke avond "nog even" in bed gamet of leest.
- **Primaire tekst (middel):**
  > Cadeau voor wie elke avond "nog even" in bed gamet of leest.
  > Bline is een stevig leeskussen dat blijft staan, met een vak voor de telefoon en een hoes die in de was kan. Zwart €79,99.
  > Voor pakjesavond in huis: bestel uiterlijk woensdag 2 december. Gratis verzending in Nederland en België.
- **Kop:** Sinterklaascadeau dat elke avond gebruikt wordt · **Beschrijving:** Zwart, €79,99
- **Landing:** `https://www.blinesleep.nl/products/leeskussen-zwart`

---

#### A12 `bl_a12_kerst`: "Een avond lezen, cadeau gedaan"

- **Format:** statisch 4:5 en 9:16. Live 4 tot en met 21 december.
- **Basis:** H-blauw04 (`beelden_higgsfield/blauw_04_b6493bcc.png`), warm lamplicht.
- **Layout 4:5:** achtergrond Nacht `#1F2A37`. Foto als afgerond vlak 960 x 960 op x 60, y 330 (man, kussen en lamp).
  - Kop wit, x 60, y 70, Poppins Bold 80 px: **"Cadeau voor de lezer in huis."**
  - Onder de foto (y 1310 te krap): zet de deadline als witte badge **in** de foto linksonder (x 90, y 1190): "Voor Kerst in huis: bestel uiterlijk 21 december", Poppins Medium 30 px, Nacht tekst.
  - Kleine ster `#E8A317` alleen als die bij de score staat; hier niet gebruiken.
- **Layout 9:16:** Nacht-achtergrond; kop y 290 tot 480; foto 960 x 960 op y 500 tot 1460; badge op y 1150.
- **Primaire tekst (kort):** Cadeau voor wie elke avond "nog één hoofdstuk" zegt.
- **Primaire tekst (middel):**
  > Cadeau voor wie elke avond "nog één hoofdstuk" zegt.
  > Een leeskussen dat blijft staan, met een vak voor de telefoon of leesbril en een katoenen hoes die in de was kan. Blauw €79,99; vier andere kleuren.
  > Voor Kerst in huis: bestel uiterlijk maandag 21 december. Gratis verzending in Nederland en België.
- **Kop:** Kerstcadeau voor lezers · **Beschrijving:** Blauw, €79,99
- **Landing:** `https://www.blinesleep.nl/products/leeskussen-blauw`

---

#### A13 `bl_a13_twee-kussens`: "Eén voor jou, één voor naast je"

- **Format:** statisch 4:5 en 9:16, split screen. Golf 3 (vanaf 16 november), daarna blijven als het werkt.
- **Basis:** links H-grijs03 (`beelden_higgsfield/grijs_03_3470a6af.png`, man met laptop), rechts H-beige04 (`beelden_higgsfield/beige_04_9d9bf3d0.png`, vrouw met boek). Twee aparte foto's naast elkaar met een witte lijn van 8 px ertussen: dat is een split screen, geen montage in één scène.
- **Layout 4:5:** beide foto's 536 x 900 op y 450 tot 1350 (uitsnede: persoon en kussen midden).
  - Bovenste vlak Zand (y 0 tot 450). Kop x 60, y 60, Nacht, Poppins Bold 80 px: **"Eén voor jou, één voor naast je."**
  - Regel (y 260) Poppins Regular 38 px `#3D4856`: "2 kussens €149,99 · je bespaart €9,99"
  - Logo Nacht rechtsboven.
- **Layout 9:16:** Zand y 0 tot 620 (kop y 290 tot 480, regel y 520), foto's 536 x 1300 op y 620 tot 1920 (gezichten boven y 1248).
- **Controle vooraf:** kunnen twee verschillende kleuren in de bundel? Zo niet, beide foto's in dezelfde kleur kiezen (bijvoorbeeld twee beige: H-beige04 en H-beige03) en dat in de tekst zeggen.
- **Primaire tekst (kort):** Eén voor jou, één voor naast je. Twee kussens, €9,99 voordeel.
- **Primaire tekst (middel):**
  > Eén voor jou, één voor naast je.
  > Wie samen in bed leest, ziet of werkt, wil niet om één kussen vechten. Twee Bline-kussens kosten €149,99 in plaats van €159,98.
  > Gratis verzending in Nederland en België, 30 dagen proberen.
- **Kop:** 2 kussens, €9,99 voordeel · **Beschrijving:** Samen €149,99
- **Landing:** `https://www.blinesleep.nl/products/leeskussen-beige?aantal=2`

---

#### A14 `bl_a14_postit`: lo-fi post-it

- **Format:** statisch 4:5, "post-it" (format dat bij Motion meer budget krijgt dan zijn aandeel).
- **Basis:** H-beige04 (`beelden_higgsfield/beige_04_9d9bf3d0.png`). Gebruik deze advertentie niet tegelijk met A06-kaart 1 als die dezelfde foto toont; anders H-blauw03 (`blauw_03_42dcdd8e.png`) nemen.
- **Layout 4:5:** foto volledig (uitsnede 1638 x 2048 met vrouw en kussen). Rechtsboven een getekende post-it van 420 x 420 px, lichtgeel `#F6E7A1`, 4 graden gedraaid, zachte schaduw. Tekst in een handschriftletter (bijvoorbeeld Caveat Bold 46 px, Nacht), drie regels:
  **"nieuwe regel:**
  **geen kussenberg**
  **meer op bed"**
- Verder geen tekst, geen logo.
- **Primaire tekst (kort):** Nieuwe regel: geen kussenberg meer op bed.
- **Primaire tekst (middel):**
  > Nieuwe regel: geen kussenberg meer op bed.
  > Eén leeskussen van 3,8 kg dat blijft staan, met een vak voor je telefoon en een hoes die in de was kan. Overdag staat het netjes op bed in een van vijf rustige kleuren.
  > Beige €79,99. Gratis verzending in Nederland en België.
- **Kop:** Eén kussen, geen berg · **Beschrijving:** Beige, €79,99
- **Landing:** `https://www.blinesleep.nl/products/leeskussen-beige`

---

## 10. Testplan met stopregels

### 10.1 Volgorde

| Wanneer | Actie | Niet doen |
|---|---|---|
| Dag -3 tot 0 | Checklist 6.3 helemaal groen; golf 1 klaarzetten | Live zonder Purchase-test |
| Dag 1 | Campagne live met A01 tot A06 | |
| Dag 1 tot 7 | Alleen kijken; geen wijzigingen behalve een kapotte link | Budget of doelgroep aanpassen |
| Dag 4 | Eerste check per advertentie (regel 1) | |
| Dag 8 | Weekcheck (maandag): regels 2 tot 4 | |
| Dag 10 tot 14 | Golf 2: 4 nieuwe advertenties tegelijk toevoegen, slechtste 2 van golf 1 pauzeren | Eén advertentie per dag toevoegen (elke keer opnieuw leren) |
| Dag 15 | €150 op: beslissing doorgaan (regel 5) | Opwaarderen zonder beslissing |
| Dag 28 | Evaluatie maand: winnende invalshoek uitbreiden met 2 nieuwe varianten in een ander format | |
| 16 november | Golf 3 live; niet-seizoens verliezers pauzeren | Meer dan 8 actieve advertenties bij €10 per dag |

### 10.2 Stopregels en drempels

[Inschatting] De drempels hieronder zijn afgeleid van het break-even van €34 en gangbare waarden; ze zijn voor Bline nog niet gemeten. Na 4 weken bijstellen op de eigen cijfers.

| Nr | Regel | Wanneer | Actie |
|---|---|---|---|
| 1 | Geen aandacht | Advertentie heeft €8 of meer uitgegeven en link-CTR onder 0,6%, of (video) minder dan 20% van de vertoningen kijkt 3 seconden | Pauzeren, vervangen door een nieuwe invalshoek (niet een variant van dezelfde) |
| 2 | Wel klik, geen interesse | Advertentie €20 of meer uitgegeven, 0 keer in winkelwagen, terwijl andere advertenties wel winkelwagens hebben | Pauzeren |
| 3 | Geen budget gekregen | Advertentie na 7 dagen minder dan €3 uitgegeven | Laten staan als de rest goed loopt; anders na 14 dagen vervangen |
| 4 | Pagina-probleem | Totaal 100+ klikken, maar minder dan 3% van de bezoekers zet iets in de winkelwagen | Advertenties laten staan; productpagina, prijs en laadtijd nalopen (Clarity-opnames) |
| 5 | Leeg kanaal | €150 uitgegeven en 0 aankopen (Shopify, niet alleen Meta) | Campagne pauzeren; meting, pagina en checkout nalopen (regel uit het funnelplan); als 8+ winkelwagens: herstart op Toevoegen aan winkelwagen (zie 1.8) |
| 6 | Te duur | Kosten per aankoop over 14 dagen boven €34 (totaalgetal uit 6.4) | Niet opschalen; slechtste advertenties vervangen; aanbod-advertenties (A10, A13) meer ruimte geven |
| 7 | Goed | Kosten per aankoop over 14 dagen onder €25 met minstens 4 aankopen | Budget +20% (dus €12), na een week opnieuw |
| 8 | Moeheid | Frequentie boven 3 per 7 dagen en CTR van de beste advertentie 30% lager dan in week 1 | Nieuwe golf eerder inzetten |
| 9 | Verkeerde reacties | Reacties over gezondheid of medische vragen onder een advertentie | Feitelijk antwoorden zonder claim ("Het is een leeskussen om rechtop te zitten; vragen over klachten kun je beter aan een arts stellen") |

### 10.3 Wat elke maandag in het overzicht staat

Per advertentie: uitgave, vertoningen, frequentie, link-CTR, kosten per klik, 3-secondenratio (video), winkelwagens, aankopen (Meta). Totaal: Shopify-orders met `utm_medium=paid_social`, omzet, kosten per aankoop (totaalgetal), verdeling NL en BE, verdeling leeftijd en geslacht, verdeling plaatsing. Daarnaast één regel: wat er die week buiten Meta veranderde (bol-actie, prijs, voorraad, mails).

---

## 11. Benodigd beeldmateriaal (prioriteit)

Alleen eigen opnames; geen nieuwe AI-beelden zonder akkoord.

| Prio | Wat | Waarvoor | Hoe | Tijd |
|---|---|---|---|---|
| 1 | **De bestaande productvideo** als bestand (1080 x 1080, 25 s) uit Shopify Files, plus het ruwe materiaal als dat er is | A01 | Downloaden en aan de monteur geven | 1 uur |
| 1 | **Telefoonvideo "kussens stapelen tegen Bline"** (script A07), 9:16, 4K of 1080p, daglicht, echte slaapkamer, beige kussen | A07 en losse fragmenten voor latere video's | Joost of iemand van het team, telefoon op statief en los; 3 tot 5 takes per shot | Halve dag |
| 1 | **Hand die in het kussen drukt en loslaat** (close-up, 5 s) | Bewijs "blijft staan", ook bruikbaar als eerste seconde van A01 en A07 | Telefoon, zijlicht | Mee met de vorige |
| 2 | **Unboxing**: doos open, kussen eruit, hoe het opbolt (als het vacuüm verpakt is) of hoe het uit de doos komt | Nieuwe advertentie (unboxing heeft de hoogste trefkans bij Motion) | Telefoon, bovenaanzicht en zijkant | 1 uur |
| 2 | **Hoes eraf en in de wasmachine** (10 tot 12 s) | Nieuwe video tegen het bezwaar "kan dat schoon?" | Telefoon | 1 uur |
| 2 | **Echte foto's per kleur in daglicht** (zelfde opstelling, telefoon of camera) | Kleurtrouw; vervangt Higgsfield-beelden in A06 als kleuren afwijken | Eén ochtend, vijf hoezen wisselen | 2 uur |
| 2 | **Kussen op een bed van 160 cm**, bovenaanzicht, met iemand die ernaast ligt | A09 met echte foto in plaats van tekening | Telefoon vanaf trap of hoge stoel | 1 uur |
| 3 | **Makers (Collabs)**: 2 tot 3 boekenliefhebbers of studenten uit NL en Vlaanderen die het kussen echt gebruiken en een korte video maken; als partnership-advertentie inzetten | UGC, testimonial, nieuwe personen | Product gratis in ruil voor een video en gebruiksrecht voor advertenties | 2 tot 4 weken |
| 3 | **Eigen reviews met foto** (Judge.me), na 5+ | Testimonial-advertentie | Reviewmail dag 14 (bestaat al) | Vanzelf |
| Optioneel | Nieuwe Higgsfield-sfeerbeelden (bijvoorbeeld twee mensen in één bed, iemand op een zolderkamer met kerstlicht) | Meer variatie in personen en omgevingen | **Alleen na akkoord van Joost** | |

---

## 12. Bronnen

Meta en platform:
- [Meta Engineering: Andromeda (2024)](https://engineering.fb.com/2024/12/02/production-engineering/meta-andromeda-advantage-automation-next-gen-personalized-ads-retrieval-engine/)
- [PPC Land: einde van de oude ASC-campagnes (2025)](https://ppc.land/meta-deprecates-legacy-campaign-apis-for-advantage-structure/)
- [Bir.ch: gids Advantage+ verkoopcampagnes (2025)](https://bir.ch/blog/advantage-plus-sales-campaigns-guide)
- [Meta Business Help: leerfase](https://www.facebook.com/business/help/112167992830700) en samenvatting [LSEO (2025)](https://lseo.com/paid-media/paid-social-media-marketing/understanding-the-facebook-ads-learning-phase-a-full-guide)
- [1ClickReport: drempel 25 conversies (2026, niet officieel bevestigd)](https://www.1clickreport.com/blog/advantage-plus-shopping-25-conversions-2026-guide)
- [Blck Alpaca: Andromeda, GEM en Advantage+ (2026)](https://blckalpaca.at/en/knowledge-base/social-media/paid-social-performance-marketing/meta-andromeda-gem-advantage-plus)
- [Jetfuel: Andromeda-playbook (juli 2026)](https://jetfuel.agency/meta-ads-strategy-for-dtc-ecommerce-brands-in-2026-the-andromeda-playbook/)
- [Chatterbuzz: creative als targeting (2026)](https://www.chatterbuzzmedia.com/blog/meta-andromeda-creative-targeting/)
- [Jon Loomer: is remarketing nog relevant](https://www.jonloomer.com/qvt/is-remarketing-still-relevant/), [remarketing voorrang geven](https://www.jonloomer.com/prioritize-remarketing-over-metas-algorithmic-ad-targeting/), [meerdere teksten](https://www.jonloomer.com/meta-ads-creative-optimization/), ["you" en persoonlijke kenmerken](https://www.jonloomer.com/can-we-use-the-words-you-and-your-in-facebook-ads-copy/), [AEM-wijziging (2025)](https://www.jonloomer.com/meta-announces-big-changes-to-website-conversion-campaigns/)
- [Search Engine Journal: creatieve test in Ads Manager (2025)](https://www.searchenginejournal.com/how-to-evaluate-creative-performance-in-meta-ads/558741/)
- [Aimerce: winkelwagen of aankoop (2026)](https://www.aimerce.ai/blogs/meta-atc-purchases-vs-awareness-traffic-what-to-run-and-when-to-use-them), [Shopify Community: nieuwe pixel (2026)](https://community.shopify.com/t/new-meta-pixel-with-no-purchase-data-best-optimization-strategy-for-a-new-store/650420)
- [Dataslayer: attributievensters (2026)](https://dataslayer.ai/blog/meta-ads-attribution-window-removed-january-2026)
- [Common Thread: tekst in beelden herschrijven (2026)](https://commonthreadco.com/blogs/coachs-corner/meta-advantage-plus-creative-image-text-rewriting-ecommerce-2026), [Holiday Insights Center (2026)](https://commonthreadco.com/blogs/coachs-corner/meta-holiday-insights-center-2026-q4-ecommerce)
- [Meta Help: AI-labels in advertenties](https://www.meta.com/en-gb/help/artificial-intelligence/355108217670024/)
- [Social Media Today: Meta's feestdagentips 2026](https://www.socialmediatoday.com/news/meta-shares-holiday-2026-tips-for-small-businesses/826785/), [Relevant Audience: vier fases Q4 (2026)](https://www.relevantaudience.com/meta/meta-holiday-playbook-four-phases-q4/)

Creatives en formats:
- [Motion: 2026 Creative Benchmarks](https://motionapp.com/events/2026-creative-strategy-bootcamp/homebase/2026-creative-benchmarks), [Motion formatbibliotheek (2026)](https://motionapp.com/library/formats/)
- [Segwise: statisch tegen video (2026)](https://segwise.ai/blog/static-video-ratio-meta-ads), [Segwise: vijf DTC-formats (2026)](https://segwise.ai/blog/100m-meta-ads-5-formats-dtc)
- [Admetrics: vijf statische formats (2026)](https://www.admetrics.io/post/five-static-ad-formats-outperforming-video-in-2026)
- [Billo: veilige zones 2026](https://billo.app/?p=50654), [Inro: Reels safe zone checker](https://www.inro.social/tools/instagram-reels-safe-zone-checker), [Metricool: Meta-formats 2026](https://metricool.com/meta-ad-formats/)
- [AdsUploader: tekstlimieten (2026)](https://adsuploader.com/blog/meta-ad-copy-specs), [Webtonic: lengte advertentietekst (2026)](https://www.webtonic.io/blog/ad-text-optimization-statistics)
- [Social News Desk: einde 20%-regel (2020)](https://www.socialnewsdesk.com/blog/facebooks-20-rule-is-no-more/), [Digiday: video zonder geluid (ouder)](https://digiday.com/sponsored/75-percent-of-people-watch-mobile-videos-on-mute/)
- [Martechvibe: partnership-advertenties (2025)](https://martechvibe.com/article/creator-ads-deliver-19-higher-ctr-on-meta-partnership-ads)

Markt en concurrenten:
- [Ella Sleeps leeskussen (bezocht 07-10-2026)](https://ellasleeps.com/products/leeskussen), [Husband Pillow (2026)](https://husbandpillow.com/), [Cloudpillo (2026)](https://cloudpillo.com/), [MT/Sprout over Cloudpillo](https://mtsprout.nl/groei/cloudpillo-hoofdkussen), [MT/Sprout omzet Cloudpillo](https://mtsprout.nl/nieuws/nieuws-startups-scaleups/omzet-cloudpillo-steeg-400-procent-jumbo-bekijkt-opties-voor-la-place), [Your Best Digs: sit-up pillows](https://www.yourbestdigs.com/reviews/the-best-sit-up-pillow/), [Walmart: Milliard](https://www.walmart.com/c/kp/milliard-memory-foam)
- bol top-10 en interne data: `research_notes/Bol leeskussens Q4 strategie/markt_en_concurrenten.md`, `interne_data_en_scenarios.md`, `bol_q4_prijs_promoties.md`

België, meting, regels:
- [KVK: e-commerce in België](https://www.kvk.nl/internationaal/e-commerce-in-belgie/), [Emerce: Trustpilot-onderzoek NL/BE (2019)](https://www.emerce.nl/wire/prijs-bepaalt-keuze-webwinkel-belgi-reviews-bepalend-nederland), [Emerce: Belgen en bezorging (2021)](https://www.emerce.nl/achtergrond/wat-verwachten-belgen-van-nederlandse-webshops-drie-adviezen-over-bezorging)
- [Shopify Help: privacy-instellingen en cookiebanner](https://help.shopify.com/en/manual/privacy-and-security/privacy/customer-privacy-settings/privacy-settings), [Shopify Help: gegevensdeling met Meta](https://help.shopify.com/en/manual/promoting-marketing/analyze-marketing/meta-data-sharing)
- [Searchlab: privacy-statistieken NL 2026 (secundair)](https://searchlab.nl/statistieken/privacy-avg-statistieken-nederland-2026)
- [ACM: nepkortingen](https://www.acm.nl/nl/publicaties/acm-wil-einde-aan-nepkortingen-na-komst-strengere-regels), [Europese Commissie: prijsaanduiding](https://commission.europa.eu/law/law-topic/consumer-protection-law/unfair-commercial-practices-law/price-indication-directive_en), [NOS: misleidende Black Friday-reclames (2025)](https://nos.nl/l/2591200)
- [NIQ: Black November (2025)](https://nielseniq.com/global/nl/news-center/2025/black-friday-is-uit-black-november-is-in/), [Keurigonline: zoektrends NL (2025)](https://www.keurigonline.nl/blog/google-zoek-trends-2025-in-nederland), [Boloo: piekmaanden](https://www.boloo.co/bibliotheek/de-bol-com-piekmaanden-een-guide-voor-bol-com-verkopers)

Niet bereikbaar op 07-10-2026: Meta Ad Library (403 zonder inlog), Meta Business Help-pagina's (worden niet geladen zonder browser), Kruidvat-productpagina (403), jonloomer.com-artikelen deels (403; inhoud via zoekresultaten).
