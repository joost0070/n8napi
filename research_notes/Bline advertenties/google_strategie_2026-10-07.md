# Bline leeskussen: Google Ads-strategie 2026 en zoekwoorduniversum

Datum: 7 oktober 2026. Voor: Joost (Shop4You / Bline). Status: advies, niets aangezet. Hoort bij `google_zoekwoorden_universum.csv` (216 zoekwoorden in deze map) en bouwt voort op de importbestanden in `mockups/blinesleep/ads/google/`.

Markering: **[Inschatting]** = eigen schatting met onderbouwing, geen gemeten feit. Alle bedragen incl. btw tenzij anders vermeld.

---

## Samenvatting

1. **Eerst meten, dan pas geld.** Geen euro boven €5 per dag totdat een testbestelling als "Aankoop" met de juiste waarde in Google Ads staat én de eerste echte bestelling via een advertentieklik in Google Ads terugkomt. Dat is precies waar Piedi Nudi misging (€831 uitgegeven, 0 conversies gemeten).
2. **Mix voor €10-15 per dag:** Standaard Shopping (ongeveer 60%), Search generiek op koopwoorden (ongeveer 30%), een kleine merkcampagne (€1 per dag, met plafond) en vanaf 13 november een aparte cadeaucampagne (€2 per dag). Geen Performance Max, Demand Gen of YouTube in de testfase.
3. **NL en BE samen in één campagne per type** (taal Nederlands), in plaats van gesplitst. Bij dit budget komt geen enkele losse campagne aan de 15 aankopen per 30 dagen die doel-ROAS nodig heeft ([Google, 2026](https://support.google.com/google-ads/answer/6268637)). Splitsen kan vanaf 30+ aankopen per maand.
4. **Bieden in drie stappen:** handmatige CPC (Shopping per productgroep, Search per zoekwoord) → Max. conversiewaarde zonder doel zodra er 15+ aankopen in 30 dagen zijn → doel-ROAS van ongeveer 250% na nog eens 2-4 weken. Google noemt nu "tot ongeveer 50 conversies of 3 conversiecycli" voor de leerfase ([TechWyse, 2026](https://www.techwyse.com/news/platform-updates/google-ads-smart-bidding-learning-period-50-conversions)).
5. **Rekenregel voor het bod:** maximale CPC = conversieratio × €34 (de kosten per aankoop waarbij je quitte speelt). Bij 1,5% conversie is dat €0,51. Startbiedingen €0,40-0,55, verwachte CPC €0,30-0,70 [Inschatting].
6. **Zoekwoordtypes:** exact en woordgroep, geen breed. Breed werkt alleen goed met slim bieden en conversiedata ([Google, 2026](https://support.google.com/google-ads/answer/7478529)). Sinds 1 september 2026 zet Google campagnes met breed of automatisch gemaakte items om naar AI Max ([Commonthread, 2026](https://commonthreadco.com/blogs/coachs-corner/google-ai-max-migration-live-september-1-2026-ecommerce)): beide uit laten.
7. **Zoekwoorduniversum: 216 termen in 19 groepen**, waarvan 175 om op te bieden en 34 met prioriteit 1 (de startset). Geschat volume van de startset: ongeveer 8.000 zoekopdrachten per maand in NL en 2.150 in Vlaanderen [Inschatting]. "leeskussen" alleen is ongeveer de helft daarvan.
8. **Echte data bepaalt de volgorde:** op bol was "leeskussen" 6 keer zo groot als de nummer 2 ("rugkussen bed"), en Google-autocomplete toont dezelfde top. Nieuw voor België: "leeskussen zetel" staat in Vlaanderen bovenaan.
9. **Niet bieden:** concurrentmerken (Ella, Ten Cate, Q-Living), winkels (ikea, action, lidl), zwangerschap, kraamtijd, herstel na een operatie en slapen met het hoofd omhoog. Die laatste vier vragen om een medische belofte die Bline niet mag en kan doen. Frans pas als er een Franse productpagina en feed zijn.
10. **Uitsluitingen in 4 gedeelde lijsten** (algemeen, merk, concurrenten, productmismatch) met samen ongeveer 260 termen, in plaats van de huidige 35.
11. **Shopping-feed:** titel begint met "Leeskussen voor bed en bank", categorie 2700 (Beddengoed > Kussens, niet de gezondheidscategorie), 5 product highlights, custom labels voor soort, prijsgroep, prestatie, seizoen en voorraad via een Google Sheet als aanvullende feed. Gratis vermeldingen aan.
12. **Q4-kalender:** start zo snel mogelijk in oktober (leerdata), cadeaucampagne 13 november t/m 21 december, budget +20-30% vanaf 16 november alleen als de kosten per aankoop onder €34 liggen. Black Friday is 27 november, pakjesavond 5 december.

---

## 0. Uitgangspunten en data

**Product en grenzen.** Wigvormig leeskussen 65 x 50 x 45 cm, 3,8 kg traagschuim, zijvak, katoenen hoes 400 TC met rits, wasbaar op 30 °C, 5 kleuren. €79,99 (wit €69,99), losse hoes €29,99-34,99. Gratis verzending NL/BE, 1-2 werkdagen, 30 dagen proberen, 4,5/5 op bol.com (13 reviews). Geen medische claims (rugpijn, ergonomisch, houding), geen "beste", geen doorgestreepte prijzen, geen nep-urgentie.

**Rekenregels** (uit `reports/Bline funnel en advertentieplan.md`):

| | Waarde |
|---|---|
| Bijdrage per kussen vóór advertenties | ongeveer €34 |
| Break-even kosten per aankoop | €34 |
| Break-even ROAS (omzet incl. btw / advertentiekosten) | ongeveer 2,3 (wit 2,2) |
| Als Google de waarde **excl. btw** binnenkrijgt (€66,10) | break-even ROAS ongeveer 1,95 |

**Break-even CPC = conversieratio × €34:**

| Conversieratio webshop | Maximale CPC om quitte te spelen |
|---|---|
| 1,0% | €0,34 |
| 1,5% | €0,51 |
| 2,0% | €0,68 |
| 3,0% | €1,02 |

Een nieuwe webshop zonder merkbekendheid zit naar verwachting op 1-2% [Inschatting]. Op bol haalde Bline 3,7% (43 aankopen op 1.148 klikken, juli-september 2026, `Bol leeskussens Q4 strategie/interne_data_en_scenarios.md`), maar een marktplaats converteert beter dan een onbekende shop.

**Databronnen voor zoekwoorden en volumes**

| Bron | Wat het geeft | Beperking |
|---|---|---|
| bol-zoektermrapport Bline, 1 aug - 26 sep 2026 (147 termen) | echte zoekopdrachten met productintentie, bol-volume, klikken, aankopen | alleen dagen waarop Bline meebood; NL en BE samen |
| Google-autocomplete NL, BE-nl en BE-fr (opgehaald 7 okt 2026, ruim 1.500 suggesties) | welke combinaties mensen echt typen, plus een relevantiescore per suggestie | geen absolute aantallen |
| Google Trends | niet bereikbaar (HTTP 429 vanaf deze omgeving) | geen seizoenscurve |
| Google Zoekwoordplanner | nog niet: vraagt een actief Ads-account | eerste taak zodra het account er is |

**Hoe de volumes geschat zijn** [Inschatting]:
- bol-maandvolume = bol-som / dagen gezien × 30; bij minder dan 20 dagen het meetkundig gemiddelde van die waarde en (som / 57 dagen × 30), omdat de korte reeksen anders overschatten.
- Google-factor: 2× het bol-volume voor korte termen (1-2 woorden), 3× voor langere zinnen ("kussen om rechtop te zitten in bed"); mensen typen in Google vaker hele zinnen dan op bol. 94% van de Nederlandse online shoppers gebruikt bol ([trade.gov, 2024](https://www.trade.gov/country-commercial-guides/netherlands-ecommerce)), dus bol is groot, maar Google vangt ook oriënterend zoeken.
- Verdeling 80% NL en 20% BE (Vlaanderen), afgerond op de stappen die de Zoekwoordplanner ook gebruikt (10, 20, 30 ... 3.600).
- Termen zonder bol-data: geschat vanuit autocomplete-positie en verwante termen.

Uitkomst voor de grootste termen: "leeskussen" ongeveer 3.600 per maand in NL en 880 in BE; "rugkussen bed" 1.300 / 320; "rugsteun bed" 720 / 170. In november en december waarschijnlijk 2 tot 2,5 keer zoveel (bol-brede piek, kerstweek ongeveer 2,6× begin augustus; `Bol leeskussens Q4 strategie/markt_en_concurrenten.md`).

---

## 1. Campagnemix voor een nieuw merk met één product (vraag 1)

**Wat de bronnen zeggen**
- Standaard Shopping is voor nieuwe accounts het meest voorspelbaar: het leunt op feed, prijs en zoekintentie en minder op conversiegeschiedenis, en het budget loopt gelijkmatig. Performance Max zoekt agressief naar kansen over alle kanalen en kan een klein budget snel opmaken ([Dotidot, 2026](https://www.dotidot.io/post/google-shopping-vs-performance-max)).
- Sinds oktober 2024 krijgt PMax geen voorrang meer op Standaard Shopping voor dezelfde producten; de advertentierangschikking beslist ([ppc.land, 2024](https://ppc.land/performance-max-vs-standard-shopping-google-revamps-ad-auction-for-holidays/)). Beide naast elkaar kan dus, maar ze concurreren om dezelfde klik.
- PMax is transparanter geworden: zoektermen zichtbaar en tot 10.000 uitsluitingen per campagne sinds maart 2025 ([ppc.land, 2025](https://ppc.land/google-raises-negative-keywords-limit-to-10-000-for-performance-max-campaigns/); [Search Engine Land, 2025](https://searchengineland.com/google-adds-search-terms-visibility-to-performance-max-campaigns-453489)). Het blijft wel een campagne die leert op conversies; zonder data stuurt hij op klikken die goedkoop zijn, vaak merkverkeer.
- Demand Gen heeft sinds april 2026 een minimum van $5 per dag, en doel-ROAS vraagt 50 conversies in 35 dagen ([Google Ads Developer Blog, 2026](https://ads-developers.googleblog.com/2026/02/minimum-budget-requirement-for-demand.html); [Google, 2026](https://support.google.com/google-ads/answer/6268637)). Voor een product met bijna geen merkbekendheid en €10-15 per dag is dat te dun.
- Eigen MCC-lessen (schoenen en sokken, 4 weken, €22.757): Shopping op merk ROAS 8,2, zoeken niet-merk 3,1, PMax generiek 4,1. Display, Video en Demand Gen stonden uit. Les: rendement komt vooral uit merk, generiek haalt 3-4.
- Piedi Nudi (zustermerk): "Branded Shopping NL" €564 en "Generic PMax NL" €267, 0 conversies gemeten, het meeste geld naar zoekopdrachten op de eigen merknaam. Les: merk en generiek scheiden, en meten vóór uitgeven.
- Sinds 30 april 2026 bestaat AI Max for Shopping als opt-in voor Standaard Shopping (tekstadvertenties en andere landingspagina's erbij) ([ppc.land, 2026](https://ppc.land/google-brings-ai-max-to-shopping-campaigns-targeting-conversational-queries/)). Niet aanzetten in de testfase: dan weet je niet meer waar de klik vandaan komt.

**Oordeel per type**

| Type | In testfase? | Waarom |
|---|---|---|
| Standaard Shopping | **Ja, hoofdcampagne** | Productbeeld, prijs en kleur in de advertentie; mensen die "leeskussen" zoeken willen vergelijken. Volledige controle over biedingen en zoektermen. |
| Search generiek | **Ja** | Pakt zinnen die Shopping slecht vangt ("kussen om rechtop te zitten in bed") en laat de prijs uitleggen (waarom €80 tegen Ella €46). |
| Search merk | **Ja, klein** | Vrijwel geen merkvolume, maar Meta-advertenties en bol-kopers gaan "bline leeskussen" zoeken. Goedkoop, en houdt merkverkeer uit de generieke cijfers. |
| Search cadeau | **Ja, alleen 13 nov - 21 dec** | Grote, brede termen; een eigen budget voorkomt dat ze de rest opeten. |
| Performance Max (alleen feed) | Nee, later | Pas bij 30+ aankopen per maand, twee maanden op rij. Dan als test naast Shopping, met merkuitsluiting. |
| Performance Max met assets | Nee | Vraagt beeld en video per kanaal en nog meer data; Display-verkeer converteert slecht voor een onbekend merk. |
| Demand Gen / YouTube | Nee | Minimumbudget, 50 conversies voor doel-ROAS, en Meta doet het "nog niet zoekende" publiek al (funnelplan). |
| Dynamische zoekadvertenties | Nee | Nieuwe DSA's aanmaken kan niet meer; bestaande gaan in februari 2027 naar AI Max ([Commonthread, 2026](https://commonthreadco.com/blogs/coachs-corner/google-ai-max-migration-live-september-1-2026-ecommerce)). |

**Volgorde en budget**

| Fase | Wanneer | Campagnes | Budget per dag |
|---|---|---|---|
| 0. Meten | vóór livegang | niets | €0 |
| 1. Meetweek | dag 1-7 na live | 01 Shopping €4, 00 Merk €1 | €5 |
| 2. Test | week 2 tot ongeveer 12 nov | 01 Shopping €7-8, 02 Generiek €4-5, 00 Merk €1 | €12-14 |
| 3. Q4 | 13 nov - 21 dec | idem + 03 Cadeau €2; +20-30% op 01/02 vanaf 16 nov als de kosten per aankoop onder €34 liggen | €14-18 |
| 4. Opschalen | vanaf 30+ aankopen per maand | test 05 PMax (feed, merk uitgesloten) naast Shopping; daarna eventueel splitsen NL/BE | volgens resultaat |

Rekenvoorbeeld fase 2 [Inschatting]: €12 per dag is €365 per maand. Bij een gemiddelde CPC van €0,45 zijn dat ongeveer 810 klikken; bij 1,5% conversie ongeveer 12 aankopen, dus €30 per aankoop en een ROAS van ongeveer 2,6. Dat is net winstgevend. Bij 1% conversie zijn het 8 aankopen à €46: verlies. Daarom zijn de eerste 4-6 weken een meting, geen winstmachine.

---

## 2. Biedstrategie per fase en verwachte CPC (vraag 2)

**Wat de bronnen zeggen**
- Doel-ROAS in Search en Shopping vraagt minstens 15 conversies in de afgelopen 30 dagen, met een waarde boven €0 ([Google, 2026](https://support.google.com/google-ads/answer/6268637)).
- De leerfase start bij een nieuwe strategie, een gewijzigde instelling of het toevoegen of verwijderen van zoekwoorden en producten ([Google, 2026](https://support.google.com/google-ads/answer/13020501)); Google noemt sinds september 2026 "tot ongeveer 50 conversies of 3 conversiecycli" ([TechWyse, 2026](https://www.techwyse.com/news/platform-updates/google-ads-smart-bidding-learning-period-50-conversions)).
- Enhanced CPC bestaat sinds maart 2025 niet meer voor Search; handmatige CPC wel ([Search Engine Land, 2024](https://searchengineland.com/google-ads-deprecate-enhanced-cpc-search-display-446350)).
- Max. conversies en Max. conversiewaarde zonder doel hebben geen minimum aan conversies.

**Advies per fase**

| Fase | Shopping | Search generiek | Merk | Overstappen als |
|---|---|---|---|---|
| A. Start (week 1-6) | Handmatige CPC per productgroep: kussens €0,45, wit €0,40, hoezen uitgesloten | Handmatige CPC per zoekwoord: "leeskussen" exact €0,55, prioriteit 1 overig €0,40-0,50 | Handmatige CPC €0,30 | 15+ aankopen in 30 dagen in Shopping, meting gecontroleerd |
| B. Leren (2-4 weken) | Max. conversiewaarde zonder doel | blijft handmatig tot zelf 15+ aankopen in 30 dagen, of samen met Shopping in een portfoliostrategie | handmatig | ROAS over 14 dagen stabiel boven 2,3 en 30+ aankopen in 30 dagen (alle campagnes) |
| C. Sturen | Doel-ROAS 250% (bij omzet incl. btw; 210% als de waarde excl. btw is) | idem, of portfolio met Shopping | handmatig | doel elke 2 weken met hooguit 10-15% bijstellen |

Waarom handmatig in plaats van "Max. klikken met CPC-plafond" (huidige opzet): Max. klikken zoekt de goedkoopste klikken binnen het plafond, en bij woordgroep zijn dat vaak de minst relevante varianten. Met 20-35 zoekwoorden is handmatig bieden per zoekwoord goed te doen en zie je precies wat elk woord kost. Max. klikken met plafond is een acceptabel alternatief als het beheer zo simpel mogelijk moet; zet het plafond dan op €0,55.

**Verwachte CPC [Inschatting]**

| Thema | Verwachte CPC NL | Onderbouwing |
|---|---|---|
| Shopping, alle termen | €0,30-0,55 | MCC-gemiddelde €0,42; Piedi Nudi €0,24-0,40 |
| "leeskussen" (exact, Search) | €0,50-0,90 | meeste concurrentie: Ella (~200 Google-advertenties), Swiss Sense, bol zelf (bol adverteert op Google voor zijn verkopers); bol-winnend bod €1,01 |
| leeskussen bed / bank / voor in bed | €0,40-0,70 | bol-winnend bod "leeskussen bed" €1,17, maar minder adverteerders op Google |
| rugkussen bed, rugsteun bed | €0,30-0,60 | bol €0,75 en €0,87; veel irrelevante varianten houden de prijs laag |
| lange zinnen (rechtop zitten, lezen in bed) | €0,20-0,45 | weinig concurrentie |
| cadeau voor boekenliefhebber | €0,30-0,80, hoger in december | veel boekhandels en cadeausites |
| BE (Vlaanderen) | 10-20% lager dan NL | minder adverteerders |

Ter vergelijking: Searchlab noemt €0,45-1,20 voor e-commerce in Nederland ([Searchlab, 2026](https://searchlab.nl/blog/google-ads-kosten-per-branche-infographic)). In de piekweken rond Black Friday, Sinterklaas en kerst rekenen bureaus met 20-40% hogere klikprijzen (bol-gegevens, `bol_advertising_q4.md`).

**Minimale conversies per maand, samengevat:** 15 in 30 dagen voor doel-ROAS (Search/Shopping); 30+ per maand voordat PMax zinvol is (MCC-les); 50 in 35 dagen voor doel-ROAS in Demand Gen.

---

## 3. Zoekwoordtypes in 2026 (vraag 3)

**Wat de bronnen zeggen**
- Alle drie de types matchen nu op betekenis, niet letterlijk. Exact = "zelfde betekenis of intentie"; woordgroep = zoekopdracht bevat de betekenis, ook specifieker; breed = verwante zoekopdrachten, ook zonder de woorden. Google: "Het is essentieel om slim bieden te gebruiken met breed" ([Google, 2026](https://support.google.com/google-ads/answer/7478529)).
- Uitsluitingen matchen **niet** op varianten: meervoud en synoniemen moet je zelf toevoegen ([Google, 2026](https://support.google.com/google-ads/answer/2453972)).
- AI Max: sinds 1 september 2026 zijn campagnes met breed op campagneniveau of automatisch gemaakte items omgezet naar AI Max (zoektermen erbij, en bij automatische items ook door Google geschreven koppen). Campagnes met alleen exact en woordgroep zijn niet omgezet ([Commonthread, 2026](https://commonthreadco.com/blogs/coachs-corner/google-ai-max-migration-live-september-1-2026-ecommerce)).

**Advies bij €4-5 per dag voor Search**
- **Exact** voor de grote, dubbelzinnige koppen: leeskussen, leeskussens, rugsteun bed, rugkussen bank, zitkussen bed, bookseat. Hier zit de meeste rommel omheen (ikea, kind, verstelbaar).
- **Woordgroep** voor de rest: lange zinnen met duidelijke intentie.
- **Exact + woordgroep** voor de paar topwoorden waar je beide wilt: leeskussen bed, rugkussen bed, merktermen. Zet ze dan in dezelfde groep; Google kiest zelf het best passende woord.
- **Geen breed** tot er 30+ aankopen per maand zijn. Daarna als test in één advertentiegroep met slim bieden.
- **Instellingen controleren bij aanmaken:** AI Max uit, "automatisch gemaakte items" uit, "URL-uitbreiding" uit, zoekpartners uit, Display-netwerk uit.

---

## 4. Het zoekwoorduniversum (vraag 4)

Volledige lijst: `google_zoekwoorden_universum.csv` (216 regels, kolommen thema, advertentiegroep, zoekwoord, matchtype, volume NL, volume BE, bron, intentie, prioriteit, opmerking).

**Prioriteiten:** 1 = startset (vanaf fase 2). 2 = toevoegen na 2-4 weken, of zodra prioriteit 1 het budget niet opmaakt. 3 = later, als test met laag bod, of alleen onder voorwaarden (Franse pagina, conversiedata, echte aanbieding).

**Overzicht per advertentiegroep** (volumes = som van de zoekwoorden waarop geboden wordt, per maand, [Inschatting]; "niet bieden" en "uitsluiten" tellen niet mee)

| Advertentiegroep | Zoekwoorden | Prio 1 / 2 / 3 | Volume NL | Volume BE |
|---|---|---|---|---|
| 00 Merk \| Merk | 8 | 5 / 2 / 1 | 160 | 100 |
| 00 Merk \| Hoes | 3 | 2 / 1 / 0 | 30 | 30 |
| 02 Generiek \| Leeskussen | 10 | 3 / 4 / 3 | 4.540 | 1.100 |
| 02 Generiek \| Leeskussen bed | 9 | 3 / 5 / 1 | 800 | 220 |
| 02 Generiek \| Leeskussen bank en zetel | 7 | 5 / 2 / 0 | 440 | 290 |
| 02 Generiek \| Rugkussen bed | 16 | 5 / 9 / 2 | 1.940 | 500 |
| 02 Generiek \| Rugkussen bank en zetel | 6 | 0 / 4 / 2 | 340 | 200 |
| 02 Generiek \| Rugsteun bed | 14 | 6 / 8 / 0 | 1.340 | 350 |
| 02 Generiek \| Rechtop zitten in bed | 12 | 4 / 3 / 5 | 390 | 140 |
| 02 Generiek \| Lezen en tv in bed | 14 | 0 / 6 / 8 | 350 | 130 |
| 02 Generiek \| Kenmerken | 15 | 1 / 7 / 7 | 390 | 150 |
| 02 Generiek \| Kleuren | 19 | 0 / 5 / 14 | 300 | 190 |
| 02 Generiek \| Bookseat en wigkussen | 9 | 0 / 0 / 9 | 1.080 | 290 |
| 02 Generiek \| Hoes (alleen voor Bline) | 6 | 0 / 0 / 6 | 300 | 80 |
| 03 Cadeau \| Cadeau voor lezers | 15 | 0 / 11 / 4 | 1.670 | 420 |
| 04 BE-FR \| Coussin de lecture | 14 | 0 / 0 / 14 | 0 | 850 (Frans) |
| 04 BE-FR \| Coussin dossier lit | 3 | 0 / 0 / 3 | 0 | 120 (Frans) |
| Niet bieden: concurrenten en winkels | 20 | (prio 3) | | |
| Uitsluiten: zwanger, zorg, medisch | 16 | n.v.t. | | |
| **Totaal** | **216** | **175 om op te bieden: 34 / 67 / 74**, plus 25 niet bieden en 16 uitsluiten | | |

**De startset (prioriteit 1, 34 zoekwoorden)**

| Groep | Zoekwoorden (matchtype) |
|---|---|
| Merk | bline leeskussen (E+W), bline (W), blinesleep (E+W), bline sleep (E+W), bline kussen (W) |
| Merk hoes | bline leeskussen hoes (E+W), bline hoes (W) |
| Leeskussen | leeskussen (E), leeskussens (E), leeskussen kopen (W) |
| Leeskussen bed | leeskussen bed (E+W), leeskussen voor in bed (W), leeskussen in bed (W) |
| Bank en zetel | leeskussen bank (W), leeskussen voor bank (W), leeskussen voor op de bank (W), leeskussen voor in bed en bank (W), leeskussen zetel (W) |
| Rugkussen bed | rugkussen bed (E+W), rugkussen voor in bed (W), rugkussen in bed (W), rugkussen bed lezen (W), rugkussen leeskussen (W) |
| Rugsteun bed | rugsteun bed (E), rugsteun voor in bed (W), rugsteun in bed (W), rugsteun kussen bed (W), rugsteun kussen voor in bed (W), rugsteun bed lezen (W) |
| Rechtop zitten | kussen om rechtop te zitten in bed (W), kussen om in bed te zitten (W), kussen rechtop zitten bed (W), kussen om rechtop in bed te zitten (W) |
| Kenmerken | leeskussen traagschuim (W) |

E = exact, W = woordgroep. De prioriteitstelling per groep in de tabel hierboven telt ook enkele "niet bieden"-regels binnen een groep mee (bijvoorbeeld "lezen in bed", "wigkussen"); de volumes niet. Geschat bereik van de startset: ongeveer 8.000 zoekopdrachten per maand in NL en 2.150 in BE (waarvan generiek 7.850 en 2.060).

**Keuzes per thema, met reden**

- **Leeskussen (enkel, meervoud, kopen).** Kern van alles. Exact op "leeskussen" omdat autocomplete laat zien dat de directe varianten vooral winkels zijn (ikea relevantie 901, action 900, lidl 601, kwantum 558) of kinderkussens. Shopping vangt de rest met beeld.
- **"Voor in bed" en "bank".** "leeskussen voor in bed" staat in NL op 1 onder "leeskussen v", en in BE op 1 onder "leeskussen". Bank en zetel (Vlaams) samen in één groep met de tekst "voor bank, zetel en bed".
- **Rugkussen en rugsteun bed.** Op bol nummer 2 en 3. "rugkussen bed" leverde op bol 1 aankoop bij 13 klikken; "rugsteun bed" 15 klikken en 0 aankopen. Rugsteun trekt ook verstelbare en elektrische frames (€85-400) en zorg-uitleen (Medipoint, thuiszorgwinkel, huren). Daarom exact plus stevige uitsluitingen. "rugkussen bank" is dubbelzinnig (losse rugkussens van een bankstel), dus exact en prioriteit 2.
- **Wigkussen.** Bline is wigvormig, maar wie "wigkussen" zoekt wil meestal het hoofd hoger bij het slapen (reflux, snurken, apneu), benen omhoog, of een zitwig voor de auto of stoel. Alleen "wigkussen voor in bed" en "wigkussen bed" exact, prioriteit 3, pas met conversiedata. De advertentie zegt "Niet om op te slapen" om verkeerde klikken te voorkomen.
- **Bedkussen om rechtop te zitten.** Precies het probleem dat Bline oplost en weinig concurrentie: prioriteit 1. "kussen om in bed te zitten" staat bovenaan onder "kussen om".
- **Lezen, tv, laptop in bed.** Echte gebruiksmomenten, kleine volumes, prioriteit 2. "lezen in bed" alleen is te breed (lampjes, brillen, "is lezen in bed slecht"); dat is een blogonderwerp. "laptop kussen bed" betekent vooral een schootkussen of laptoptafel: niet bieden.
- **Zwangerschap en na een operatie: uitsluiten.** Bieden op het woord is op zich geen claim, maar de zoeker verwacht dat het kussen geschikt is voor zwangerschap, kraamtijd of herstel. Om die klik waar te maken moet de advertentie of pagina iets over gezondheid beloven, en dat mag Bline niet (en Google beperkt advertenties met onbetrouwbare gezondheidsclaims, [Google, 2026](https://support.google.com/adspolicy/answer/15936857)). Bovendien bleek dit bij uwleeskussen.nl tot afgekeurde advertenties te leiden. Wie zwanger is en het kussen gewoon om te lezen gebruikt, vindt het via "leeskussen bed".
- **Cadeau.** "cadeau voor boekenliefhebber" en varianten zijn groot (8 varianten in autocomplete) en passen bij een product van €80. Wel oriënterend: lagere conversie. Alleen in een eigen campagne met budgetplafond, 13 november t/m 21 december. "cadeau moeder" en "cadeau ouderen" los zijn te breed; alleen de combinatie met lezen (prioriteit 3). Geen leeftijds- of zorgbeloftes in de tekst.
- **Vlaams en Frans.** Vlaams zit in de Nederlandstalige campagne (zetel, ruggesteun). Frans ("coussin de lecture", nummer 1 is "coussin de lecture au lit") pas met een Franse productpagina, Franse feed en een aparte campagne met taal Frans. Op bol kwam "coussin de lecture" 38 keer voor in 10 dagen met 1 klik.
- **Concurrentmerken: niet bieden.** Mag wel: Google beperkt merknamen niet als zoekwoord, wel in de advertentietekst ([Google, 2026](https://support.google.com/adspolicy/answer/6118)). Maar Bline is €20-35 duurder dan Ella (€45,99, 164 reviews), de Kwaliteitsscore op andermans merk is laag, en het kost budget dat de koopwoorden harder nodig hebben. In Search uitsluiten; Shopping mag erop verschijnen (productvergelijking met beeld), na 2 weken bekijken. Winkels (ikea, action, lidl, kwantum, hema, leenbakker, jysk, beter bed, bol) overal uitsluiten.
- **Hoes.** Wie "leeskussen hoes" zoekt heeft meestal al een ander kussen (autocomplete: Ten Cate, Happybed). De Bline-hoes past alleen op Bline. Daarom: merk-hoes in de merkcampagne (prioriteit 1, voor bol-kopers die een tweede hoes willen), generieke hoes-termen alleen exact en met "Past op Bline, 65 x 50 x 45" vastgezet op positie 2 (prioriteit 3).
- **Kenmerken en kleuren.** Kleine volumes (bol: 6-9 zoekopdrachten per kleur in 2 maanden). Eén kleurgroep met per zoekwoord de juiste landingspagina, in plaats van vijf groepen met elk 3 woorden. "ergonomisch leeskussen" alleen exact met laag bod; het woord nooit in de tekst.
- **Bookseat.** Op bol een synoniem voor leeskussen, maar "The Bookseat" is ook een boekensteun-merk en "book seat" is op Google vooral treinen en vliegtuigen. Exact, prioriteit 3, merknaam niet in de tekst; Shopping dekt het.

**Wat er verandert ten opzichte van de 44 zoekwoorden in `bline-google-3_zoekwoorden.csv`**
- Erbij als prioriteit 1: leeskussens, leeskussen in bed, leeskussen voor op de bank, leeskussen voor bank, leeskussen zetel, rugkussen in bed, rugkussen bed lezen, rugsteun in bed, rugsteun kussen bed (+ voor in bed), rugsteun bed lezen, kussen om in bed te zitten, kussen rechtop zitten bed, kussen om rechtop in bed te zitten, bline hoes, bline leeskussen hoes.
- Naar prioriteit 3 of exact: boekkussen, bookseat, ergonomisch leeskussen, leeskussen hoes en hoes leeskussen (uit de algemene groep, naar een eigen hoesgroep), rugkussen bank (exact).
- Samenvoegen: de vijf kleurgroepen worden één groep "Kleuren" met URL per zoekwoord.
- Locatie: de generieke campagne ook op België (Vlaams).

---

## 5. Uitsluitingen (vraag 5)

Google staat 20 gedeelde lijsten per account toe met elk tot 5.000 termen, en 1.000 uitsluitingen op accountniveau ([Google, 2026](https://support.google.com/google-ads/answer/6372658)). Uitsluitingen matchen niet op meervoud of synoniemen, dus die staan er apart in.

**Opzet**

| Lijst | Koppelen aan | Type |
|---|---|---|
| A. Bline \| Algemeen | alle campagnes (00 t/m 04), later ook PMax | woordgroep, tenzij [exact] |
| B. Bline \| Merk | 01 Shopping, 02 Generiek, 03 Cadeau | woordgroep |
| C. Bline \| Concurrenten | 02 Generiek, 03 Cadeau (Shopping: na 2 weken beslissen) | woordgroep |
| D. Bline \| Productmismatch Search | 02 Generiek, 03 Cadeau | woordgroep, tenzij [exact] |

Waarom B: zo blijft merkverkeer in de merkcampagne en zie je eerlijk wat generiek oplevert (de Piedi Nudi-les).

**A. Algemeen (ongeveer 175 termen)**
- Gratis en tweedehands: gratis, tweedehands, 2e hands, tweede hands, 2dehands, gebruikt, marktplaats, vinted, kringloop
- Zelf maken: zelf maken, maken, diy, patroon, naaipatroon, haken, gehaakt, breien, naaien, tutorial, tuto, handleiding
- Winkels en platforms: ikea, action, lidl, aldi, kwantum, hema, leenbakker, jysk, blokker, xenos, temu, aliexpress, shein, wish, kruidvat, zeeman, primark, karwei, hornbach, praxis, gamma, decathlon, wibra, beter bed, sleepworld, swiss sense, auping, bol com, bol.com, bolcom, amazon
- Kinderen en dieren: baby, babies, kind, kinderen, kinder, kinderkamer, peuter, jongen, meisje, tiener, hond, honden, kat, katten, poes, huisdier
- Zorg en medisch: medisch, ziekenhuis, rugpijn, nekpijn, hernia, reflux, maagzuur, apneu, snurken, scoliose, decubitus, orthopedisch, fysio, fysiotherapie, operatie, revalidatie, thuiszorg, thuiszorgwinkel, zorgwinkel, medipoint, vegro, huren, lenen, uitleen, stuitje, coccyx, heup, knie, been, benen, voeten, onderrug, lendensteun, zwanger, zwangerschap, zwangerschapskussen, bevalling, kraamweek, kraamzorg, kraampakket, borstvoeding, voedingskussen, keizersnede
- Andere plekken en producten: auto, autostoel, bureaustoel, kantoorstoel, gamestoel, gamingstoel, rolstoel, rollator, scootmobiel, fiets, motor, scooter, boot, camper, caravan, tuin, tuinbank, tuinstoel, buiten, loungeset, pallet, palletkussen, strand, zwembad, bad, ligbad, vliegtuig, reiskussen, nekkussen, hoofdkussen, dekbed, matras, kussensloop, kussenslopen, elektrisch, elektrische, verstelbaar, verstelbare, massage, warmte, infrarood, opblaasbaar, opblaasbare, wigkussen been, beenkussen
- Puzzel (echte bol-rommel): puzzel, puzzelmat, puzzelmap, puzzeltafel, puzzelbord, puzzelplank, puzzelplaat
- Banen en info: vacature, vacatures, baan, banen, stage, salaris, wat is, betekenis, engels, in het engels, vertaling, duits, definitie
- Losse brede woorden [exact]: [bank], [banken], [kussen], [kussens], [rugkussen], [rugsteun], [wigkussen], [lezen in bed]

Let op: "werk" staat er bewust niet in (anders valt "kussen om te werken in bed" weg). "slapen" staat in lijst D (alleen generiek Search), niet in A, zodat de merkcampagne en latere slaapproducten van Bline er geen last van hebben.

**B. Merk:** bline, blinesleep, bline sleep, [blin], [blins]

**C. Concurrenten (ongeveer 45 termen):** ella, ella sleeps, ellasleeps, q living, q-living, qliving, ten cate, tencate, cozysense, ducky dons, happybed, happy bed, homca, best life, eloneo, sleepy lounge, zensation, havargo, vitapur, milliard, costway, isleep, sleeplife, zelesta, livarno, icon, symposium, weids wonen, polydaun, sleeptight, droomtextiel, lyxus, soft silky, defa, novamed, sissel, tempur, dorsaback, lucovitaal, wellpur, nira, froli, inventum, the bookseat

**D. Productmismatch Search (ongeveer 40 termen):** armleuning, armleuningen, armsteun, nekrol, neksteun, hoofdsteun, schoot, op schoot, vloer, grond, rond, 2 personen, 90 cm, 140, 140 cm, 160, 160 cm, 180, 180 cm, 200, goedkoop, goedkope, aanbieding, korting, sale, uitverkoop, black friday (weghalen als er een echte actie is), teddy, pompom, pom pom, fluffy, minecraft, stitch, sierkussen, sierkussens, zitzak, slapen, zijslaper, lendekussen

Waarom D niet op Shopping: Shopping-advertenties tonen het kussen met beeld, dus wie een kussen met armleuning zoekt ziet meteen dat het iets anders is. Eventuele klikken zie je in het zoektermrapport.

---

## 6. Advertentieteksten en assets (vraag 6)

**Regels die in alle teksten zijn toegepast**
- Geen "beste", geen rugpijn, ergonomisch, houding of orthopedisch, geen doorgestreepte prijzen, geen "nu nog" of "laatste kans", geen uitroeptekens.
- Prijzen alleen zoals ze echt zijn ("Vanaf €69,99" klopt door wit; hoes "vanaf €29,99").
- "2 kussens: €9,99 voordeel" uit de huidige CSV staat er niet in. Alleen terugzetten als die bundelprijs echt in de shop staat.
- Elke advertentie: 15 koppen (max. 30 tekens), 4 beschrijvingen (max. 90 tekens), lengte automatisch gecontroleerd. Tekens geteld zoals Google telt (€ en ° tellen als 1).

**Pinnen: in principe niet.** Vastzetten verkleint het aantal combinaties dat Google kan testen en verlaagt de advertentiesterkte ([Pattern, 2025](https://au.pattern.com/blog/best-practices-for-responsive-search-ads-rsa-in-2025/)). Twee uitzonderingen: in de merkadvertentie twee merkkoppen op positie 1, en in de generieke hoesadvertentie "Past op Bline, 65 x 50 x 45" op positie 2, zodat niemand met een ander kussen klikt.

**Gedeelde kernkoppen** (komen in de meeste groepen terug): Gratis verzending NL en BE (26) · 30 dagen proberen (17) · Hoes wasbaar op 30 °C (21) · 3,8 kg stevig traagschuim (25) · Met vak voor je telefoon (24) · In 1-2 werkdagen in huis (24) · 4,5 uit 5 op bol.com (20) · Katoenen hoes met rits (22) · Kies uit 5 rustige kleuren (26) · Leeskussen dat blijft staan (27) · Geen kussenfort meer (20) · Bline leeskussen (16).

**Responsieve zoekadvertenties per advertentiegroep**

#### 00 Merk | Merk

Final URL: `https://www.blinesleep.nl/` · pad: `/leeskussen/bline` · Pinnen: Kop 1 en 2 vastzetten op positie 1 (twee varianten: 'Bline leeskussen' en 'Officiële webshop van Bline'). Rest los.

| # | Kop | Tekens |
|---|---|---|
| 1 | Bline leeskussen | 16 |
| 2 | Officiële webshop van Bline | 27 |
| 3 | Leeskussen dat blijft staan | 27 |
| 4 | Geen kussenfort meer | 20 |
| 5 | Met vak voor je telefoon | 24 |
| 6 | 3,8 kg stevig traagschuim | 25 |
| 7 | Hoes wasbaar op 30 °C | 21 |
| 8 | Kies uit 5 rustige kleuren | 26 |
| 9 | Gratis verzending NL en BE | 26 |
| 10 | 30 dagen proberen | 17 |
| 11 | In 1-2 werkdagen in huis | 24 |
| 12 | 4,5 uit 5 op bol.com | 20 |
| 13 | Een Nederlands merk uit Borne | 29 |
| 14 | Vragen? App ons gerust | 22 |
| 15 | Betaal met iDEAL of Bancontact | 30 |

| # | Beschrijving | Tekens |
|---|---|---|
| 1 | Het leeskussen van Bline: stevig traagschuim, vak voor je telefoon en een wasbare hoes. | 87 |
| 2 | Katoenen hoes met rits, wasbaar op 30 °C. In wit, beige, blauw, grijs en zwart. | 79 |
| 3 | Gratis verzending in Nederland en België. Binnen 1-2 werkdagen in huis. | 71 |
| 4 | Al 4,5 uit 5 op bol.com. 30 dagen proberen en een echte klantenservice. | 71 |

#### 00 Merk | Hoes

Final URL: `[URL hoes-product, controleren]` · pad: `/hoes/bline` · Pinnen: Geen pin.

| # | Kop | Tekens |
|---|---|---|
| 1 | Hoes voor je Bline leeskussen | 29 |
| 2 | Extra hoes voor de wasdag | 25 |
| 3 | Losse hoes vanaf €29,99 | 23 |
| 4 | Katoen 400 TC met rits | 22 |
| 5 | Wasbaar op 30 °C | 16 |
| 6 | Hoes in 5 kleuren | 17 |
| 7 | Past op elk Bline leeskussen | 28 |
| 8 | Wissel van kleur | 16 |
| 9 | Gratis verzending NL en BE | 26 |
| 10 | 30 dagen proberen | 17 |
| 11 | In 1-2 werkdagen in huis | 24 |
| 12 | 4,5 uit 5 op bol.com | 20 |
| 13 | Bline leeskussen hoes | 21 |
| 14 | Vragen? App ons gerust | 22 |
| 15 | Betaal met iDEAL of Bancontact | 30 |

| # | Beschrijving | Tekens |
|---|---|---|
| 1 | Losse hoes voor het Bline leeskussen. Katoen 400 TC met rits, wasbaar op 30 °C. | 79 |
| 2 | In wit, beige, blauw, grijs en zwart. Handig als de andere hoes in de was zit. | 78 |
| 3 | Gratis verzending in Nederland en België. Binnen 1-2 werkdagen in huis. | 71 |
| 4 | Al 4,5 uit 5 op bol.com. 30 dagen proberen en een echte klantenservice. | 71 |

#### 02 Generiek | Leeskussen

Final URL: `https://www.blinesleep.nl/products/leeskussen-beige` · pad: `/leeskussen/5-kleuren` · Pinnen: Geen pin.

| # | Kop | Tekens |
|---|---|---|
| 1 | Leeskussen voor bed en bank | 27 |
| 2 | Leeskussen kopen | 16 |
| 3 | Bline leeskussen | 16 |
| 4 | Leeskussen dat blijft staan | 27 |
| 5 | Geen kussenfort meer | 20 |
| 6 | Met vak voor je telefoon | 24 |
| 7 | 3,8 kg stevig traagschuim | 25 |
| 8 | Hoes wasbaar op 30 °C | 21 |
| 9 | Katoenen hoes met rits | 22 |
| 10 | Kies uit 5 rustige kleuren | 26 |
| 11 | Gratis verzending NL en BE | 26 |
| 12 | 30 dagen proberen | 17 |
| 13 | In 1-2 werkdagen in huis | 24 |
| 14 | 4,5 uit 5 op bol.com | 20 |
| 15 | Vanaf €69,99 | 12 |

| # | Beschrijving | Tekens |
|---|---|---|
| 1 | Leeskussen met vak voor je telefoon. Stevig traagschuim dat blijft staan als je leunt. | 86 |
| 2 | Katoenen hoes met rits, wasbaar op 30 °C. In wit, beige, blauw, grijs en zwart. | 79 |
| 3 | Gratis verzending in Nederland en België. Binnen 1-2 werkdagen in huis. | 71 |
| 4 | Al 4,5 uit 5 op bol.com. 30 dagen proberen en een echte klantenservice. | 71 |

#### 02 Generiek | Leeskussen bed

Final URL: `https://www.blinesleep.nl/products/leeskussen-beige` · pad: `/leeskussen/bed` · Pinnen: Geen pin.

| # | Kop | Tekens |
|---|---|---|
| 1 | Leeskussen voor in bed | 22 |
| 2 | Rechtop lezen in bed | 20 |
| 3 | Geen stapel kussens meer | 24 |
| 4 | Bline leeskussen | 16 |
| 5 | Leeskussen dat blijft staan | 27 |
| 6 | Met vak voor je telefoon | 24 |
| 7 | 3,8 kg stevig traagschuim | 25 |
| 8 | Hoes wasbaar op 30 °C | 21 |
| 9 | Katoenen hoes met rits | 22 |
| 10 | Kies uit 5 rustige kleuren | 26 |
| 11 | Gratis verzending NL en BE | 26 |
| 12 | 30 dagen proberen | 17 |
| 13 | In 1-2 werkdagen in huis | 24 |
| 14 | 4,5 uit 5 op bol.com | 20 |
| 15 | Vanaf €69,99 | 12 |

| # | Beschrijving | Tekens |
|---|---|---|
| 1 | Zit rechtop in bed met een boek of een serie. Stevig traagschuim dat niet wegzakt. | 82 |
| 2 | Katoenen hoes met rits, wasbaar op 30 °C. In wit, beige, blauw, grijs en zwart. | 79 |
| 3 | Gratis verzending in Nederland en België. Binnen 1-2 werkdagen in huis. | 71 |
| 4 | Al 4,5 uit 5 op bol.com. 30 dagen proberen en een echte klantenservice. | 71 |

#### 02 Generiek | Leeskussen bank en zetel

Final URL: `https://www.blinesleep.nl/products/leeskussen-beige` · pad: `/leeskussen/bank` · Pinnen: Geen pin.

| # | Kop | Tekens |
|---|---|---|
| 1 | Leeskussen voor de bank | 23 |
| 2 | Leeskussen voor bed en zetel | 28 |
| 3 | Voor bank, zetel en bed | 23 |
| 4 | Bline leeskussen | 16 |
| 5 | Leeskussen dat blijft staan | 27 |
| 6 | Met vak voor je telefoon | 24 |
| 7 | 3,8 kg stevig traagschuim | 25 |
| 8 | Hoes wasbaar op 30 °C | 21 |
| 9 | Katoenen hoes met rits | 22 |
| 10 | Kies uit 5 rustige kleuren | 26 |
| 11 | Gratis verzending NL en BE | 26 |
| 12 | 30 dagen proberen | 17 |
| 13 | In 1-2 werkdagen in huis | 24 |
| 14 | 4,5 uit 5 op bol.com | 20 |
| 15 | Betaal met iDEAL of Bancontact | 30 |

| # | Beschrijving | Tekens |
|---|---|---|
| 1 | Leeskussen voor bank, zetel en bed. Stevig traagschuim met vak voor je telefoon. | 80 |
| 2 | Katoenen hoes met rits, wasbaar op 30 °C. In wit, beige, blauw, grijs en zwart. | 79 |
| 3 | Gratis verzending in Nederland en België. Binnen 1-2 werkdagen in huis. | 71 |
| 4 | Al 4,5 uit 5 op bol.com. 30 dagen proberen en een echte klantenservice. | 71 |

#### 02 Generiek | Rugkussen bed

Final URL: `https://www.blinesleep.nl/products/leeskussen-beige` · pad: `/rugkussen/bed` · Pinnen: Geen pin.

| # | Kop | Tekens |
|---|---|---|
| 1 | Rugkussen voor in bed | 21 |
| 2 | Stevig rugkussen voor bed | 25 |
| 3 | Rugkussen van traagschuim | 25 |
| 4 | Rechtop lezen in bed | 20 |
| 5 | Bline leeskussen | 16 |
| 6 | Geen kussenfort meer | 20 |
| 7 | Met vak voor je telefoon | 24 |
| 8 | 3,8 kg stevig traagschuim | 25 |
| 9 | Hoes wasbaar op 30 °C | 21 |
| 10 | Katoenen hoes met rits | 22 |
| 11 | Kies uit 5 rustige kleuren | 26 |
| 12 | Gratis verzending NL en BE | 26 |
| 13 | 30 dagen proberen | 17 |
| 14 | In 1-2 werkdagen in huis | 24 |
| 15 | 4,5 uit 5 op bol.com | 20 |

| # | Beschrijving | Tekens |
|---|---|---|
| 1 | Rugkussen voor in bed van 3,8 kg traagschuim. Blijft staan als je ertegen leunt. | 80 |
| 2 | Katoenen hoes met rits, wasbaar op 30 °C. In wit, beige, blauw, grijs en zwart. | 79 |
| 3 | Gratis verzending in Nederland en België. Binnen 1-2 werkdagen in huis. | 71 |
| 4 | Al 4,5 uit 5 op bol.com. 30 dagen proberen en een echte klantenservice. | 71 |

#### 02 Generiek | Rugkussen bank en zetel

Final URL: `https://www.blinesleep.nl/products/leeskussen-beige` · pad: `/rugkussen/bank` · Pinnen: Geen pin.

| # | Kop | Tekens |
|---|---|---|
| 1 | Rugkussen voor de bank | 22 |
| 2 | Rugkussen voor bank en zetel | 28 |
| 3 | Los rugkussen, 65 x 50 x 45 | 27 |
| 4 | Ook fijn in bed | 15 |
| 5 | Bline leeskussen | 16 |
| 6 | Leeskussen dat blijft staan | 27 |
| 7 | Met vak voor je telefoon | 24 |
| 8 | 3,8 kg stevig traagschuim | 25 |
| 9 | Hoes wasbaar op 30 °C | 21 |
| 10 | Katoenen hoes met rits | 22 |
| 11 | Kies uit 5 rustige kleuren | 26 |
| 12 | Gratis verzending NL en BE | 26 |
| 13 | 30 dagen proberen | 17 |
| 14 | In 1-2 werkdagen in huis | 24 |
| 15 | 4,5 uit 5 op bol.com | 20 |

| # | Beschrijving | Tekens |
|---|---|---|
| 1 | Los rugkussen voor bank, zetel of bed. Met vak voor je telefoon en een wasbare hoes. | 84 |
| 2 | Katoenen hoes met rits, wasbaar op 30 °C. In wit, beige, blauw, grijs en zwart. | 79 |
| 3 | Gratis verzending in Nederland en België. Binnen 1-2 werkdagen in huis. | 71 |
| 4 | Al 4,5 uit 5 op bol.com. 30 dagen proberen en een echte klantenservice. | 71 |

#### 02 Generiek | Rugsteun bed

Final URL: `https://www.blinesleep.nl/products/leeskussen-beige` · pad: `/rugsteun/bed` · Pinnen: Geen pin.

| # | Kop | Tekens |
|---|---|---|
| 1 | Rugsteun voor in bed | 20 |
| 2 | Kussen als rugsteun in bed | 26 |
| 3 | Geen frame, geen stekker | 24 |
| 4 | Rechtop lezen in bed | 20 |
| 5 | Bline leeskussen | 16 |
| 6 | Leeskussen dat blijft staan | 27 |
| 7 | Met vak voor je telefoon | 24 |
| 8 | 3,8 kg stevig traagschuim | 25 |
| 9 | Hoes wasbaar op 30 °C | 21 |
| 10 | Katoenen hoes met rits | 22 |
| 11 | Kies uit 5 rustige kleuren | 26 |
| 12 | Gratis verzending NL en BE | 26 |
| 13 | 30 dagen proberen | 17 |
| 14 | In 1-2 werkdagen in huis | 24 |
| 15 | 4,5 uit 5 op bol.com | 20 |

| # | Beschrijving | Tekens |
|---|---|---|
| 1 | Kussen als rugsteun in bed, van stevig traagschuim. Geen frame en geen stekker nodig. | 85 |
| 2 | Katoenen hoes met rits, wasbaar op 30 °C. In wit, beige, blauw, grijs en zwart. | 79 |
| 3 | Gratis verzending in Nederland en België. Binnen 1-2 werkdagen in huis. | 71 |
| 4 | Al 4,5 uit 5 op bol.com. 30 dagen proberen en een echte klantenservice. | 71 |

#### 02 Generiek | Rechtop zitten in bed

Final URL: `https://www.blinesleep.nl/products/leeskussen-beige` · pad: `/rechtop-zitten/bed` · Pinnen: Geen pin.

| # | Kop | Tekens |
|---|---|---|
| 1 | Rechtop zitten in bed | 21 |
| 2 | Kussen om rechtop te zitten | 27 |
| 3 | Zit rechtop met een boek | 24 |
| 4 | Geen kussenfort meer | 20 |
| 5 | Bline leeskussen | 16 |
| 6 | Leeskussen dat blijft staan | 27 |
| 7 | Met vak voor je telefoon | 24 |
| 8 | 3,8 kg stevig traagschuim | 25 |
| 9 | Hoes wasbaar op 30 °C | 21 |
| 10 | Katoenen hoes met rits | 22 |
| 11 | Kies uit 5 rustige kleuren | 26 |
| 12 | Gratis verzending NL en BE | 26 |
| 13 | 30 dagen proberen | 17 |
| 14 | In 1-2 werkdagen in huis | 24 |
| 15 | 4,5 uit 5 op bol.com | 20 |

| # | Beschrijving | Tekens |
|---|---|---|
| 1 | Kussen om rechtop te zitten in bed of op de bank. Houdt zijn vorm als je leunt. | 79 |
| 2 | Katoenen hoes met rits, wasbaar op 30 °C. In wit, beige, blauw, grijs en zwart. | 79 |
| 3 | Gratis verzending in Nederland en België. Binnen 1-2 werkdagen in huis. | 71 |
| 4 | Al 4,5 uit 5 op bol.com. 30 dagen proberen en een echte klantenservice. | 71 |

#### 02 Generiek | Lezen en tv in bed

Final URL: `https://www.blinesleep.nl/products/leeskussen-beige` · pad: `/lezen/bed` · Pinnen: Geen pin.

| # | Kop | Tekens |
|---|---|---|
| 1 | Lezen of tv kijken in bed | 25 |
| 2 | Kussen om te lezen in bed | 25 |
| 3 | Serie kijken in bed | 19 |
| 4 | Voor boek, serie en laptop | 26 |
| 5 | Bline leeskussen | 16 |
| 6 | Leeskussen dat blijft staan | 27 |
| 7 | Geen kussenfort meer | 20 |
| 8 | Met vak voor je telefoon | 24 |
| 9 | 3,8 kg stevig traagschuim | 25 |
| 10 | Hoes wasbaar op 30 °C | 21 |
| 11 | Kies uit 5 rustige kleuren | 26 |
| 12 | Gratis verzending NL en BE | 26 |
| 13 | 30 dagen proberen | 17 |
| 14 | In 1-2 werkdagen in huis | 24 |
| 15 | 4,5 uit 5 op bol.com | 20 |

| # | Beschrijving | Tekens |
|---|---|---|
| 1 | Voor lezen, series of even werken in bed. Met vak voor telefoon, bril of e-reader. | 82 |
| 2 | Katoenen hoes met rits, wasbaar op 30 °C. In wit, beige, blauw, grijs en zwart. | 79 |
| 3 | Gratis verzending in Nederland en België. Binnen 1-2 werkdagen in huis. | 71 |
| 4 | Al 4,5 uit 5 op bol.com. 30 dagen proberen en een echte klantenservice. | 71 |

#### 02 Generiek | Kenmerken

Final URL: `https://www.blinesleep.nl/products/leeskussen-beige` · pad: `/leeskussen/traagschuim` · Pinnen: Geen pin.

| # | Kop | Tekens |
|---|---|---|
| 1 | Leeskussen van traagschuim | 26 |
| 2 | Hoes van katoen 400 TC | 22 |
| 3 | Zijvak voor je telefoon | 23 |
| 4 | Hoes eraf, in de was | 20 |
| 5 | Bline leeskussen | 16 |
| 6 | Leeskussen dat blijft staan | 27 |
| 7 | Geen kussenfort meer | 20 |
| 8 | 3,8 kg stevig traagschuim | 25 |
| 9 | Hoes wasbaar op 30 °C | 21 |
| 10 | Kies uit 5 rustige kleuren | 26 |
| 11 | Gratis verzending NL en BE | 26 |
| 12 | 30 dagen proberen | 17 |
| 13 | In 1-2 werkdagen in huis | 24 |
| 14 | 4,5 uit 5 op bol.com | 20 |
| 15 | Vanaf €69,99 | 12 |

| # | Beschrijving | Tekens |
|---|---|---|
| 1 | 3,8 kg traagschuim in een katoenen hoes van 400 TC. Hoes met rits, wasbaar op 30 °C. | 84 |
| 2 | Leeskussen van 65 x 50 x 45 cm met zijvak voor je telefoon. In vijf rustige kleuren. | 84 |
| 3 | Gratis verzending in Nederland en België. Binnen 1-2 werkdagen in huis. | 71 |
| 4 | Al 4,5 uit 5 op bol.com. 30 dagen proberen en een echte klantenservice. | 71 |

#### 02 Generiek | Kleuren

Final URL: `[final URL per zoekwoord: /products/leeskussen-<kleur>]` · pad: `/leeskussen/kleuren` · Pinnen: Geen pin. Wil je de kleur in de kop: één RSA per kleur met kop 'Leeskussen <kleur>' (zie huidige CSV), of een advertentiecustomizer.

| # | Kop | Tekens |
|---|---|---|
| 1 | Leeskussen in 5 kleuren | 23 |
| 2 | Vijf rustige kleuren | 20 |
| 3 | Kies je kleur | 13 |
| 4 | Ook losse hoezen per kleur | 26 |
| 5 | Bline leeskussen | 16 |
| 6 | Leeskussen dat blijft staan | 27 |
| 7 | Geen kussenfort meer | 20 |
| 8 | Met vak voor je telefoon | 24 |
| 9 | 3,8 kg stevig traagschuim | 25 |
| 10 | Hoes wasbaar op 30 °C | 21 |
| 11 | Katoenen hoes met rits | 22 |
| 12 | Gratis verzending NL en BE | 26 |
| 13 | 30 dagen proberen | 17 |
| 14 | In 1-2 werkdagen in huis | 24 |
| 15 | 4,5 uit 5 op bol.com | 20 |

| # | Beschrijving | Tekens |
|---|---|---|
| 1 | In wit, beige, blauw, grijs en zwart. Een bijpassende losse hoes in elke kleur. | 79 |
| 2 | Leeskussen met vak voor je telefoon. Stevig traagschuim dat blijft staan als je leunt. | 86 |
| 3 | Gratis verzending in Nederland en België. Binnen 1-2 werkdagen in huis. | 71 |
| 4 | Al 4,5 uit 5 op bol.com. 30 dagen proberen en een echte klantenservice. | 71 |

#### 02 Generiek | Bookseat en wigkussen

Final URL: `https://www.blinesleep.nl/products/leeskussen-beige` · pad: `/leeskussen/wigvorm` · Pinnen: Geen pin. De zin 'Niet om op te slapen' filtert reflux- en slaapwigzoekers weg.

| # | Kop | Tekens |
|---|---|---|
| 1 | Wigvormig leeskussen | 20 |
| 2 | Wigkussen om in te zitten | 25 |
| 3 | Leeskussen in wigvorm | 21 |
| 4 | Rechtop lezen in bed | 20 |
| 5 | Bline leeskussen | 16 |
| 6 | Leeskussen dat blijft staan | 27 |
| 7 | Geen kussenfort meer | 20 |
| 8 | Met vak voor je telefoon | 24 |
| 9 | 3,8 kg stevig traagschuim | 25 |
| 10 | Hoes wasbaar op 30 °C | 21 |
| 11 | Kies uit 5 rustige kleuren | 26 |
| 12 | Gratis verzending NL en BE | 26 |
| 13 | 30 dagen proberen | 17 |
| 14 | In 1-2 werkdagen in huis | 24 |
| 15 | 4,5 uit 5 op bol.com | 20 |

| # | Beschrijving | Tekens |
|---|---|---|
| 1 | Wigvormig leeskussen om rechtop te zitten in bed of op de bank. Niet om op te slapen. | 85 |
| 2 | Katoenen hoes met rits, wasbaar op 30 °C. In wit, beige, blauw, grijs en zwart. | 79 |
| 3 | Gratis verzending in Nederland en België. Binnen 1-2 werkdagen in huis. | 71 |
| 4 | Al 4,5 uit 5 op bol.com. 30 dagen proberen en een echte klantenservice. | 71 |

#### 02 Generiek | Hoes (alleen voor Bline)

Final URL: `[URL hoes-product, controleren]` · pad: `/hoes/leeskussen` · Pinnen: Kop 2 ('Past op Bline, 65 x 50 x 45') vastzetten op positie 2, zodat niemand met een ander kussen klikt.

| # | Kop | Tekens |
|---|---|---|
| 1 | Hoes voor Bline leeskussen | 26 |
| 2 | Past op Bline, 65 x 50 x 45 | 27 |
| 3 | Katoen 400 TC met rits | 22 |
| 4 | Wasbaar op 30 °C | 16 |
| 5 | Losse hoes vanaf €29,99 | 23 |
| 6 | Hoes in 5 kleuren | 17 |
| 7 | Extra hoes voor de wasdag | 25 |
| 8 | Wissel van kleur | 16 |
| 9 | Gratis verzending NL en BE | 26 |
| 10 | 30 dagen proberen | 17 |
| 11 | In 1-2 werkdagen in huis | 24 |
| 12 | 4,5 uit 5 op bol.com | 20 |
| 13 | Bline leeskussen | 16 |
| 14 | Vragen? App ons gerust | 22 |
| 15 | Betaal met iDEAL of Bancontact | 30 |

| # | Beschrijving | Tekens |
|---|---|---|
| 1 | Losse hoes voor het Bline leeskussen. Past alleen op Bline (65 x 50 x 45 cm). | 77 |
| 2 | Katoen 400 TC met rits, wasbaar op 30 °C. In wit, beige, blauw, grijs en zwart. | 79 |
| 3 | Gratis verzending in Nederland en België. Binnen 1-2 werkdagen in huis. | 71 |
| 4 | Al 4,5 uit 5 op bol.com. 30 dagen proberen en een echte klantenservice. | 71 |

#### 03 Cadeau | Cadeau voor lezers

Final URL: `https://www.blinesleep.nl/products/leeskussen-beige` · pad: `/cadeau/lezer` · Pinnen: Geen pin. Alleen actief 13 nov t/m 21 dec. Geen 'op tijd voor 5 december' tenzij de levertijd dat echt haalt.

| # | Kop | Tekens |
|---|---|---|
| 1 | Cadeau voor een lezer | 21 |
| 2 | Cadeau voor boekenliefhebbers | 29 |
| 3 | Voor wie graag in bed leest | 27 |
| 4 | Leeskussen als cadeau | 21 |
| 5 | Voor wie altijd een boek leest | 30 |
| 6 | Bline leeskussen | 16 |
| 7 | Leeskussen dat blijft staan | 27 |
| 8 | Geen kussenfort meer | 20 |
| 9 | Met vak voor je telefoon | 24 |
| 10 | 3,8 kg stevig traagschuim | 25 |
| 11 | Hoes wasbaar op 30 °C | 21 |
| 12 | Kies uit 5 rustige kleuren | 26 |
| 13 | Gratis verzending NL en BE | 26 |
| 14 | 30 dagen proberen | 17 |
| 15 | In 1-2 werkdagen in huis | 24 |

| # | Beschrijving | Tekens |
|---|---|---|
| 1 | Cadeau voor wie graag leest: een leeskussen dat blijft staan, met vak voor de telefoon. | 87 |
| 2 | Twijfel over de kleur? Je hebt 30 dagen om te proberen. Gratis verzending NL en BE. | 83 |
| 3 | Katoenen hoes met rits, wasbaar op 30 °C. In wit, beige, blauw, grijs en zwart. | 79 |
| 4 | Al 4,5 uit 5 op bol.com. 30 dagen proberen en een echte klantenservice. | 71 |

#### 04 BE-FR | Coussin de lecture (later)

Final URL: `[Franse productpagina, nog te maken]` · pad: `/coussin/lecture` · Pinnen: Pas gebruiken met een Franse productpagina en Franse feed; laat de vertaling nakijken door een Franstalige.

| # | Kop | Tekens |
|---|---|---|
| 1 | Coussin de lecture Bline | 24 |
| 2 | Coussin de lecture pour lit | 27 |
| 3 | Pour le lit et le canapé | 24 |
| 4 | Lire assis dans son lit | 23 |
| 5 | Il garde sa forme | 17 |
| 6 | Poche pour téléphone | 20 |
| 7 | Mousse à mémoire de forme | 25 |
| 8 | Housse lavable à 30 °C | 22 |
| 9 | Housse en coton avec zip | 24 |
| 10 | 5 couleurs douces | 17 |
| 11 | Livraison gratuite en Belgique | 30 |
| 12 | Essai de 30 jours | 17 |
| 13 | Livré en 1 à 2 jours ouvrés | 27 |
| 14 | Note de 4,5/5 sur bol.com | 25 |
| 15 | Payez avec Bancontact | 21 |

| # | Beschrijving | Tekens |
|---|---|---|
| 1 | Coussin de lecture avec poche pour téléphone. Mousse ferme qui reste en place. | 78 |
| 2 | Housse en coton avec zip, lavable à 30 °C. En blanc, beige, bleu, gris et noir. | 79 |
| 3 | Livraison gratuite en Belgique. Livré chez vous en 1 à 2 jours ouvrés. | 70 |
| 4 | Note de 4,5/5 sur bol.com. Essai de 30 jours et un vrai service client. | 71 |

**Assets (op accountniveau, tenzij anders vermeld)**

*Sitelinks* (linktekst max. 25, regels max. 35 tekens). Nooit naar een collectie als landingspagina voor een product (funnelplan); de hoes-sitelink dus naar een hoesproduct.

| Linktekst | Regel 1 | Regel 2 | URL |
|---|---|---|---|
| Vijf kleuren (12) | Wit, beige, blauw, grijs, zwart (31) | Kies je kleur op de site (24) | /#kleuren |
| Losse hoezen (12) | Tweede hoes voor de wasdag (26) | Katoen 400 TC, met rits (23) | [hoesproduct, controleren] |
| Maten en details (16) | 65 x 50 x 45 cm, 3,8 kg (23) | Getekende maten en video (24) | [productpagina #maten, controleren] |
| Veelgestelde vragen (19) | Maat, wassen, levertijd (23) | Alles op één pagina (19) | /pages/veelgestelde-vragen |
| Verzending en retour (20) | Gratis verzending NL en BE (26) | 30 dagen proberen (17) | [beleidspagina, controleren] |
| Over Bline (10) | Een Nederlands merk uit Borne (29) | Bel of app ons gerust (21) | /pages/over-bline |

*Highlights (callouts, max. 25):* Gratis verzending NL en BE (26) · 30 dagen proberen (17) · In 1-2 werkdagen in huis (24) · Hoes wasbaar op 30 °C (21) · 3,8 kg traagschuim (18) · Vak voor je telefoon (20) · Katoen 400 TC met rits (22) · Betaal met iDEAL (16) · Bancontact voor België (22) · Nederlands merk (15) · Klantenservice per app (22). Maximaal 4 tegelijk zichtbaar; Google kiest.

*Gestructureerde fragmenten:* "Stijlen": Wit, Beige, Blauw, Grijs, Zwart. "Typen": Leeskussen, Losse hoes.

*Prijs-asset* (type Producten, taal Nederlands; minimaal 3, aanbevolen 5+ items, kop en beschrijving max. 25 tekens, [Google, 2026](https://support.google.com/google-ads/answer/7065415)):

| Kop | Beschrijving | Prijs | URL |
|---|---|---|---|
| Leeskussen beige (16) | Met vak voor telefoon (21) | €79,99 | /products/leeskussen-beige |
| Leeskussen wit (14) | Katoenen hoes met rits (22) | €69,99 | /products/leeskussen-wit |
| Leeskussen blauw (16) | Traagschuim, 3,8 kg (19) | €79,99 | /products/leeskussen-blauw |
| Leeskussen grijs (16) | Hoes wasbaar op 30 °C (21) | €79,99 | /products/leeskussen-grijs |
| Leeskussen zwart (16) | Gratis verzending (17) | €79,99 | /products/leeskussen-zwart |
| Losse hoes (10) | Katoen 400 TC, met rits (23) | vanaf €29,99 | [hoesproduct] |

*Promotie-asset:* alleen bij een echte actie die ook in de shop staat (bijvoorbeeld een bundel kussen + hoes met vaste prijs, of een Black Friday-actie die Joost besluit). Niet alle feestdagen zijn in het Nederlands beschikbaar als "gelegenheid" ([Google, 2026](https://support.google.com/google-ads/answer/7367521)); dan zonder gelegenheid, met begin- en einddatum. Geen nep-acties.

*Afbeeldingsassets in Search:* pas mogelijk als het account 60 dagen open is en de afgelopen 30 dagen Search-uitgaven had ([ppc.land, 2026](https://ppc.land/google-ads-bans-blurry-image-assets-and-cuts-eligibility-to-60-day-accounts/); [Google, 2026](https://support.google.com/google-ads/answer/9566341)). Voor een nieuw account dus pas begin december. Klaarzetten: beeld 01 per kleur (kussen op bed met boek) in 1:1 (1200 x 1200) en 1,91:1 (1200 x 628), zonder tekst in beeld, plus 2 gebruiksbeelden. Bedrijfsnaam "Bline" en logo als merkasset (vraagt adverteerdersverificatie).

---

## 7. Shopping en Merchant Center (vraag 7)

**Wat de Shopify Google & YouTube-app doet en niet doet**

| Doet de app | Doet de app niet (zelf regelen) |
|---|---|
| Producten, titels, beschrijvingen, beelden, prijzen, voorraad en GTIN naar Merchant Center ([Charle, 2026](https://www.charleagency.com/articles/shopify-google-shopping-guide/)) | Standaard Shopping-campagne aanmaken: alleen PMax gaat vanuit de app; Shopping maak je in Google Ads |
| Google-productcategorie en custom label 0-4 via metavelden of bulkbewerker ([Shopify Community, 2025](https://community.shopify.com/t/google-youtube-app-category-specific-attributes-feed/416703)) | product_highlight, product_detail, lifestyle_image_link: niet in de app, dus via een aanvullende feed |
| Conversies Aankoop, Toevoegen aan winkelwagen, Checkout gestart, plus optie voor verbeterde conversies ([Google, 2026](https://support.google.com/google-ads/answer/13494537)) | Aankoop als enige primaire conversie zetten (handmatig) |
| Gratis vermeldingen aanzetten | Verzend- en retourbeleid in Merchant Center volledig invullen, reviews voor sterren |

**Titelformule** (max. 150 tekens, de eerste 70 zijn meestal zichtbaar, geen promotietekst, geen hoofdletters als nadruk; [Google, 2026](https://support.google.com/merchants/answer/6324415)):

`[Producttype voor gebruik], [Merk] [Kleur], [synoniem] van [gewicht] [materiaal] met [kenmerk], [hoes], [maat]`

- Kussen (137 tekens): `Leeskussen voor bed en bank, Bline Beige, rugkussen van 3,8 kg traagschuim met vak voor telefoon, katoenen hoes met rits, 65 x 50 x 45 cm`
- Hoes (100 tekens): `Hoes voor Bline leeskussen, Beige, katoen 400 TC met rits, wasbaar op 30 °C, past op 65 x 50 x 45 cm`

Verschil met de titel in `LEESMIJ.md`: "Leeskussen voor bed en bank" vooraan (de zoektermen van bol en autocomplete) en "rugkussen" erbij, zodat "rugkussen bed" ook matcht. Het merk staat vroeg maar niet als eerste woord, omdat bijna niemand op "Bline" zoekt.

**Beschrijving** (voorstel, geen claims, ongeveer 600 tekens):
> Het Bline leeskussen is een wigvormig rugkussen om rechtop te zitten in bed of op de bank. Lezen, een serie kijken of even werken: het kussen van 3,8 kg traagschuim houdt zijn vorm als je ertegen leunt, dus geen stapel losse kussens meer. In het zijvak passen je telefoon, bril of e-reader. De hoes is van katoen (400 TC), heeft een rits en kan op 30 °C in de was. Afmetingen 65 x 50 x 45 cm. Verkrijgbaar in wit, beige, blauw, grijs en zwart, met losse hoezen in dezelfde kleuren.

**product_highlight** (2-100 stuks, aanbevolen 4-6, max. 150 tekens, alleen over het product zelf; [Google, 2026](https://support.google.com/merchants/answer/9216100)):
1. Wigvorm van 65 x 50 x 45 cm om rechtop te zitten in bed of op de bank (69)
2. 3,8 kg stevig traagschuim dat zijn vorm houdt als je ertegen leunt (66)
3. Zijvak voor telefoon, bril of e-reader (38)
4. Katoenen hoes van 400 TC met rits, wasbaar op 30 °C (51)
5. Leverbaar in wit, beige, blauw, grijs en zwart (46)

**product_detail** (sectie : naam : waarde): Afmetingen : Maat : 65 x 50 x 45 cm · Afmetingen : Gewicht : 3,8 kg · Materiaal : Vulling : traagschuim · Materiaal : Hoes : katoen 400 TC · Onderhoud : Wassen : hoes op 30 °C, met rits afneembaar · Uitvoering : Opbergvak : zijvak.

**Overige attributen**

| Attribuut | Kussen | Hoes |
|---|---|---|
| google_product_category | 2700 (Huis en tuin > Linnengoed > Beddengoed > Kussens) | 2927 (... > Beddengoed > Kussenhoezen) |
| Niet gebruiken | 7404 (Gezondheid > Rugzorg > Ondersteuningskussens): trekt de gezondheidscontext erbij | |
| product_type | Slaapkamer > Leeskussens > Leeskussen | Slaapkamer > Leeskussens > Hoes |
| brand | Bline | Bline |
| gtin | EAN per kleur | EAN per kleur |
| color | Wit / Beige / Blauw / Grijs / Zwart | idem |
| material | Traagschuim/Katoen | Katoen |
| size | 65 x 50 x 45 cm | 65 x 50 x 45 cm |
| item_group_id | optioneel `bline-leeskussen` als de kleuren als losse producten in Shopify staan | `bline-hoes` |
| lifestyle_image_link | gebruiksbeeld per kleur | rits-detail |
| Hoofdbeeld | beeld 01 zonder tekst (al geregeld) | |

Taxonomie-ID's uit de Nederlandse Google-lijst ([Google, 2026](https://www.google.com/basepages/producttype/taxonomy-with-ids.nl-NL.txt)).

**Custom labels** (max. 5, elk tot 100 tekens en 1.000 unieke waarden; [Google, 2026](https://support.google.com/merchants/answer/7052112)):

| Label | Inhoud | Waarden | Gebruik |
|---|---|---|---|
| custom_label_0 | soort | kussen, hoes | hoezen apart bieden of uitsluiten |
| custom_label_1 | prijs/marge | 6999 (wit), 7999 | wit lager bieden |
| custom_label_2 | prestatie (maandelijks bijwerken) | bestseller, normaal, nieuw, laag | later PMax splitsen zoals in het MCC |
| custom_label_3 | seizoen | q4-cadeau, standaard | in Q4 cadeau-producten hoger bieden |
| custom_label_4 | voorraad | ok, laag | kleur met lage voorraad omlaag, voorkomt uitverkocht door advertenties |

**Aanvullende feed via Google Sheet:** in Merchant Center een extra gegevensbron "Google Spreadsheets". Eerste kolom `id`, exact gelijk aan de ID's die de app aanmaakt (vorm `shopify_NL_<product-id>_<variant-id>`, en apart voor BE als die markt wordt gesynchroniseerd; overnemen uit Merchant Center, niet zelf bedenken). Verdere kolommen: product_highlight (meerdere kolommen), product_detail, custom_label_0-4, lifestyle_image_link, en eventueel title. De sheet overschrijft alleen die velden ([Cypress North, 2025](https://cypressnorth.com/resources/guides/how-to-use-a-supplemental-feed-in-google-merchant-center-next-a-step-by-step-guide/)). Een sheet is hier genoeg; een feed-app (Simprosys, DataFeedWatch) is pas nodig bij veel producten.

**Shopping-campagne indelen:** productgroepen op custom_label_0: "kussen" (verder op item-ID per kleur, zodat je per kleur ziet wat werkt) en "hoes" uitgesloten. Na 4 weken de hoes testen met €0,15.

**Gratis vermeldingen:** aanzetten in Merchant Center (onder "Gratis vermeldingen" of "Overal op Google"). Producten kunnen dan gratis verschijnen in Google Zoeken, het Shopping-tabblad, Afbeeldingen en YouTube ([Emerce, 2020](https://www.emerce.nl/achtergrond/alles-over-google-free-listings)). Retourbeleid invullen kan labels als "30 dagen retour" opleveren (`webshop_best_practices_2026-10-06.md`).

**Sterren:** productbeoordelingen vragen minimaal 50 reviews over alle producten; per product zijn er 3 nodig om sterren in een Shopping-advertentie te tonen ([Google, 2026](https://support.google.com/merchants/answer/14549080)). Met Judge.me (of Google Klantenreviews) verzamelen vanaf de eerste bestelling; tot die tijd staat de 4,5 op bol in de tekstadvertenties.

---

## 8. Meting en privacy (vraag 8)

**Wat er verplicht en nodig is**
- Sinds maart 2024 moet je voor gebruikers in de EER toestemming vragen en die signalen (ad_user_data, ad_personalization) aan Google doorgeven via Consent Mode v2; anders geen nieuwe EER-gebruikers in remarketinglijsten en minder meting ([Search Engine Journal, 2024](https://www.searchenginejournal.com/consent-mode-v2-google-shares-shares-key-details-for-advertisers/)).
- Bij "geavanceerde" consent mode stuurt de tag ook zonder toestemming cookieloze pings, waarmee Google conversies kan modelleren; bij "basis" wordt niets verstuurd tot toestemming ([Google, 2026](https://support.google.com/google-ads/answer/10000067)).
- De Google & YouTube-app maakt de conversies Aankoop, Toevoegen aan winkelwagen en Checkout gestart, en kan verbeterde conversies aanzetten. Google waarschuwt voor dubbele tags als je ook een eigen pixel of storefront-tag hebt ([Google, 2026](https://support.google.com/google-ads/answer/13494537)).
- Statussen: "Niet geverifieerd" = tag nog nooit gezien; "Geen recente conversies" = tag werkt, maar geen conversie uit een advertentie in 7 dagen; "Conversies worden geregistreerd" = goed ([Elevar, 2025](https://docs.getelevar.com/docs/troubleshooting-google-ads-conversion-tracking-statuses)).

**Controlelijst: geen budget vóórdat alles hier is afgevinkt**

| Nr | Stap | Klaar als |
|---|---|---|
| 1 | Shopify: cookiemelding voor de EU aan (NL en BE), met weigeren even makkelijk als accepteren | banner zichtbaar in een privévenster |
| 2 | Google & YouTube-app: Merchant Center en het nieuwe Google Ads-account koppelen, conversiemeting aan, verbeterde conversies aan | in de app staat "verbonden" bij beide |
| 3 | Google Ads > Doelen > Conversies: alleen **Aankoop** primair, Toevoegen aan winkelwagen en Checkout gestart secundair. Geen GA4-import van dezelfde aankoop als primair, geen oude tags, geen vaste waarde van €1 | in het overzicht staat precies één primaire actie in het doel "Aankopen" |
| 4 | Instellingen Aankoop: telling "Elke", klikvenster 30 dagen, attributie datagestuurd. Nagaan of de waarde incl. of excl. btw en verzending is (bepaalt de break-even ROAS: 2,3 of 1,95) | genoteerd in het logboek |
| 5 | Testbestelling (echte betaling, daarna terugbetalen) met Tag Assistant aan ([Google, 2026](https://support.google.com/google-ads/answer/10989978)) | Tag Assistant toont de aankoop-tag met de juiste waarde en EUR; status van Aankoop gaat binnen 24-48 uur van "Niet geverifieerd" naar "Geen recente conversies" |
| 6 | Toestemming testen: in een privévenster weigeren en kijken of er geen advertentiecookies worden gezet (alleen cookieloze pings) | gecontroleerd in Tag Assistant |
| 7 | Merchant Center: alle 10 producten goedgekeurd voor NL en BE, verzending (gratis, 0-1 dag verwerking, 1-2 dagen vervoer) en retourbeleid ingevuld | geen afkeuringen in Diagnose |
| 8 | Meetweek (fase 1): €5 per dag. Elke Shopify-bestelling met bron Google Ads (of gclid in de landingspagina) moet binnen 72 uur ook in Google Ads staan | status "Conversies worden geregistreerd"; aantal Ads-aankopen = Shopify-aankopen uit Google (marge ±20%) |
| 9 | Pas daarna naar fase 2 (€12-14 per dag) | |

Wekelijks blijven vergelijken: Shopify-aankopen met bron Google tegen Google Ads-aankopen. Een gat van meer dan 30% is een meetprobleem, geen prestatieprobleem: dan eerst de meting, niet de biedingen.

Wat Piedi Nudi leert: een campagne zonder werkende primaire conversie stuurt op klikken, en goedkope klikken zijn vaak de eigen merknaam. Stap 3 en 8 voorkomen dat.

---

## 9. Stopregels en optimalisatieritme (vraag 9)

**Stopregels** (bovenop die in het funnelplan)

| Niveau | Regel | Actie |
|---|---|---|
| Account | meting niet bevestigd (stap 8) | niet boven €5 per dag |
| Campagne | €150 uitgegeven zonder aankoop | pauzeren; meting en productpagina nalopen |
| Campagne | kosten per aankoop over 14 dagen boven €34 | biedingen 15% omlaag, slechtste zoektermen uitsluiten |
| Campagne | kosten per aankoop onder €25 over 14 dagen | budget +20% per week |
| Zoekwoord | €34 kosten zonder aankoop | bod 30% omlaag |
| Zoekwoord | €50 kosten zonder aankoop | pauzeren |
| Zoekwoord | CTR onder 2% na 300 vertoningen | tekst of zoekwoord herzien; Kwaliteitsscore 4 of lager na 2 weken: pauzeren |
| Zoekterm | niet passend (zie lijst A-D) | meteen uitsluiten, ook bij 1 klik |
| Zoekterm | passend, 15+ klikken, 0 aankopen | als exact zoekwoord met lager bod, of uitsluiten |
| Product (Shopping) | €34 kosten zonder aankoop | bod op dat item 30% omlaag |
| Slim bieden | na overstap | 2 weken niets wijzigen behalve uitsluitingen; doel per keer hooguit 10-15% |

**Ritme**

| Wanneer | Wat (tijd) |
|---|---|
| Dagelijks in de meetweek | uitgaven, afkeuringen, conversiestatus (5 min) |
| Elke maandag | zoektermrapport Search en Shopping (en later PMax), uitsluitingen toevoegen, biedingen per zoekwoord en product, budget per campagne, Shopify tegen Ads-aankopen, Merchant Center Diagnose (30 min) |
| Elke 2 weken | asset-rapport van de advertenties: koppen met "Laag" na 2.000+ vertoningen vervangen; prioriteit 2-zoekwoorden toevoegen als het budget niet op is |
| Maandelijks | custom_label_2 (prestatie) bijwerken, fasebesluit (handmatig → slim bieden), volumes in de CSV vervangen door de Zoekwoordplanner, uur- en dagrapport (Piedi Nudi: piek 13-22 uur en vrijdag/zaterdag, 80% mobiel) |
| Q4 | 13 nov cadeaucampagne aan; 16 nov budget +20-30% als de kosten per aankoop onder €34 liggen; 3 dec laatste dag voor Sinterklaas-levering (bij 1-2 werkdagen) in de tekst alleen als ChannelDock dat haalt; 21 dec cadeau uit; januari budget terug |

---

## 10. Concreet advies

### 10.1 Campagne-opzet

| Campagne | Type | Budget per dag | Bieden (start) | Locatie | Taal | Netwerk | Schema |
|---|---|---|---|---|---|---|---|
| 00 Search \| Merk \| NL+BE | Search | €1 | handmatige CPC €0,30 | NL + BE, "aanwezigheid" (niet "interesse") | Nederlands | alleen Google Zoeken | altijd |
| 01 Shopping \| Leeskussen \| NL+BE | Standaard Shopping, prioriteit laag | €4 (meetweek), daarna €7-8 | handmatige CPC: kussens €0,45, wit €0,40, hoezen uitgesloten; BE -10% (hogere verzendkosten: €7,14 tegen €5,07) | NL + BE, aanwezigheid | (feed: Nederlands) | zonder zoekpartners | altijd |
| 02 Search \| Generiek \| NL+BE | Search | €4-5 (vanaf week 2) | handmatige CPC per zoekwoord: leeskussen €0,55, overige prio 1 €0,40-0,50 | NL + BE, aanwezigheid | Nederlands | alleen Google Zoeken | altijd; na 4 weken eventueel +15% op 19-22 uur |
| 03 Search \| Cadeau \| NL+BE | Search | €2 | handmatige CPC €0,35-0,45 | NL + BE | Nederlands | alleen Google Zoeken | 13 nov - 21 dec |
| 04 Search \| Generiek \| BE-FR | Search | later | handmatig | BE | Frans | alleen Google Zoeken | pas met Franse pagina en feed |
| 05 PMax \| Feed \| NL+BE | Performance Max (alleen feed) | later | Max. conversiewaarde | NL + BE | | alle | pas bij 30+ aankopen per maand, merk uitgesloten |

Voor alle Search-campagnes: AI Max uit, automatisch gemaakte items uit, URL-uitbreiding uit, zoekpartners en Display uit, automatische tagging aan (gclid; geen UTM's in Google Ads, zoals afgesproken in het funnelplan).

Advertentiegroepen en landingspagina's:

| Campagne | Advertentiegroep | Landingspagina |
|---|---|---|
| 00 | Merk | homepage |
| 00 | Hoes | hoesproduct |
| 02 | Leeskussen; Leeskussen bed; Leeskussen bank en zetel; Rugkussen bed; Rugkussen bank en zetel; Rugsteun bed; Rechtop zitten in bed; Lezen en tv in bed; Kenmerken; Bookseat en wigkussen | /products/leeskussen-beige (alle kleuren op één pagina) |
| 02 | Kleuren | per zoekwoord /products/leeskussen-&lt;kleur&gt; |
| 02 | Hoes (alleen voor Bline) | hoesproduct |
| 03 | Cadeau voor lezers | /products/leeskussen-beige |
| 04 | Coussin de lecture; Coussin dossier lit | Franse productpagina |

Bij de start (fase 2) alleen de groepen met prioriteit 1-zoekwoorden aanzetten: Leeskussen, Leeskussen bed, Leeskussen bank en zetel, Rugkussen bed, Rugsteun bed, Rechtop zitten in bed, Kenmerken. De rest gepauzeerd klaarzetten.

### 10.2 Zoekwoorden per groep
Zie de tabel "startset" in hoofdstuk 4 en de volledige lijst in `google_zoekwoorden_universum.csv` (kolom prioriteit en matchtype).

### 10.3 Uitsluitingen
Zie hoofdstuk 5: vier gedeelde lijsten, koppelingen volgens de tabel daar.

### 10.4 RSA-teksten en assets
Zie hoofdstuk 6.

### 10.5 Shopping-feed
Zie hoofdstuk 7: titelformule, beschrijving, 5 highlights, product_detail, categorie 2700/2927, custom labels via Google Sheet.

### 10.6 Wat aanpassen in de importbestanden (`mockups/blinesleep/ads/google/`)

| Bestand | Aanpassing |
|---|---|
| 1_campagnes | Generiek: locatie NL;BE en naam "02 Search \| Generiek \| NL+BE"; biedstrategie handmatige CPC (of Max. klikken met plafond €0,55). Shopping als één campagne NL+BE in plaats van NL €8 en BE €3. Cadeau-campagne toevoegen (gepauzeerd). |
| 2_advertentiegroepen | "Leeskussen algemeen" en de 5 kleurgroepen vervangen door de groepen uit 10.1. |
| 3_zoekwoorden | Vervangen door de prioriteit 1-regels uit de CSV (34); prioriteit 2 en 3 gepauzeerd erbij. |
| 4_advertenties | Teksten uit hoofdstuk 6; "2 kussens: €9,99 voordeel" alleen bij een echte bundelprijs. |
| 5_uitsluitingen | Vier lijsten uit hoofdstuk 5 (ongeveer 260 termen) in plaats van één lijst met 35. |
| 6_extensies | Sitelinks aanvullen (Maten en details, Verzending en retour), 11 highlights, snippet "Typen", prijs-asset. Afbeeldingen pas na 60 dagen. |
| LEESMIJ (Shopping) | Titel volgens de nieuwe formule; categorie 2700; aanvullende feed; bieden handmatig in plaats van Max. klikken. |

### 10.7 Openstaande punten voor Joost
1. Wordt de conversiewaarde incl. of excl. btw doorgegeven? Bepaalt het doel-ROAS.
2. Komt er een Franse productpagina? Zo ja, dan campagne 04 en een Franse feed.
3. Is er een echte bundelprijs (2 kussens of kussen + hoes)? Dan pas een promotie-asset.
4. URL's van het hoesproduct en de pagina met verzending en retour.
5. Haalt ChannelDock "voor 5 december in huis" bij bestellingen tot 3 december? Alleen dan mag dat in de cadeau-teksten.

---

## Bronnen

**Eigen data en notities**
- bol-zoektermrapport Bline, 1 aug - 26 sep 2026: `scratchpad/onderzoek/bol_zoektermen_bline_2026-08-01_09-26.csv`
- `research_notes/Bline Sleep risicos en voorbeelden/google_ads_mcc_lessen.md` (2026) en `markt_advertenties_2026-10-05.md`
- `research_notes/Bol leeskussens Q4 strategie/` (markt_en_concurrenten, bol_advertising_q4, bol_q4_prijs_promoties, interne_data_en_scenarios; 2026)
- `reports/Bline funnel en advertentieplan.md` (v2.0, 2026), `mockups/blinesleep/ads/google/` (2026)
- Google-autocomplete NL, BE-nl, BE-fr, opgehaald 7 oktober 2026 via suggestqueries.google.com en google.com/complete (eigen opvraging; ruim 1.500 suggesties met relevantiescore)

**Google (helpcentrum en beleid)**
- [Over doel-ROAS (2026)](https://support.google.com/google-ads/answer/6268637)
- [Leerperiode van biedstrategieën (2026)](https://support.google.com/google-ads/answer/13020501)
- [Zoekwoordmatchtypes (2026)](https://support.google.com/google-ads/answer/7478529)
- [Uitsluitingszoekwoorden (2026)](https://support.google.com/google-ads/answer/2453972)
- [Accountlimieten (2026)](https://support.google.com/google-ads/answer/6372658)
- [Prijs-assets (2026)](https://support.google.com/google-ads/answer/7065415)
- [Promotie-assets (2026)](https://support.google.com/google-ads/answer/7367521)
- [Afbeeldingsassets in Search (2026)](https://support.google.com/google-ads/answer/9566341)
- [Merkenbeleid (2026)](https://support.google.com/adspolicy/answer/6118)
- [Onbetrouwbare claims (2026)](https://support.google.com/adspolicy/answer/15936857)
- [Conversiemeting met de Google & YouTube-app op Shopify (2026)](https://support.google.com/google-ads/answer/13494537)
- [Consent mode (2026)](https://support.google.com/google-ads/answer/10000067)
- [Tag Assistant voor conversieacties (2026)](https://support.google.com/google-ads/answer/10989978)
- [Merchant Center: titel (2026)](https://support.google.com/merchants/answer/6324415)
- [Merchant Center: productgegevensspecificatie (2026)](https://support.google.com/merchants/answer/7052112)
- [Merchant Center: product_highlight (2026)](https://support.google.com/merchants/answer/9216100)
- [Merchant Center: productbeoordelingen (2026)](https://support.google.com/merchants/answer/14549080)
- [Google-productcategorieën met ID's, Nederlands (2026)](https://www.google.com/basepages/producttype/taxonomy-with-ids.nl-NL.txt)
- [Google Ads Developer Blog: minimumbudget Demand Gen (2026)](https://ads-developers.googleblog.com/2026/02/minimum-budget-requirement-for-demand.html)

**Vakpers en gidsen**
- [Commonthread: AI Max-migratie 1 september (2026)](https://commonthreadco.com/blogs/coachs-corner/google-ai-max-migration-live-september-1-2026-ecommerce)
- [ppc.land: AI Max voor Shopping (2026)](https://ppc.land/google-brings-ai-max-to-shopping-campaigns-targeting-conversational-queries/)
- [ppc.land: afbeeldingsassets alleen voor accounts van 60+ dagen (2026)](https://ppc.land/google-ads-bans-blurry-image-assets-and-cuts-eligibility-to-60-day-accounts/)
- [ppc.land: 10.000 uitsluitingen in PMax (2025)](https://ppc.land/google-raises-negative-keywords-limit-to-10-000-for-performance-max-campaigns/)
- [ppc.land: PMax niet langer voorrang op Standaard Shopping (2024)](https://ppc.land/performance-max-vs-standard-shopping-google-revamps-ad-auction-for-holidays/)
- [Search Engine Land: zoektermen in PMax (2025)](https://searchengineland.com/google-adds-search-terms-visibility-to-performance-max-campaigns-453489)
- [Search Engine Land: einde Enhanced CPC (2024)](https://searchengineland.com/google-ads-deprecate-enhanced-cpc-search-display-446350)
- [TechWyse: leerfase 50 conversies (2026)](https://www.techwyse.com/news/platform-updates/google-ads-smart-bidding-learning-period-50-conversions)
- [Dotidot: Shopping tegen PMax (2026)](https://www.dotidot.io/post/google-shopping-vs-performance-max)
- [Search Engine Journal: Consent Mode v2 (2024)](https://www.searchenginejournal.com/consent-mode-v2-google-shares-shares-key-details-for-advertisers/)
- [Elevar: statussen van conversieacties (2025)](https://docs.getelevar.com/docs/troubleshooting-google-ads-conversion-tracking-statuses)
- [Pattern: RSA en pinnen (2025)](https://au.pattern.com/blog/best-practices-for-responsive-search-ads-rsa-in-2025/)
- [Charle: Shopify Google Shopping-gids (2026)](https://www.charleagency.com/articles/shopify-google-shopping-guide/)
- [Shopify Community: categorie en custom labels in de app (2025)](https://community.shopify.com/t/google-youtube-app-category-specific-attributes-feed/416703)
- [Cypress North: aanvullende feed in Merchant Center Next (2025)](https://cypressnorth.com/resources/guides/how-to-use-a-supplemental-feed-in-google-merchant-center-next-a-step-by-step-guide/)
- [Searchlab: Google Ads-kosten per branche NL (2026)](https://searchlab.nl/blog/google-ads-kosten-per-branche-infographic)
- [Emerce: Google free listings (2020)](https://www.emerce.nl/achtergrond/alles-over-google-free-listings)
- [trade.gov: e-commerce Nederland (2024)](https://www.trade.gov/country-commercial-guides/netherlands-ecommerce)

**Niet gelukt:** Google Trends (HTTP 429), dus geen seizoenscurve voor "leeskussen"; Zoekwoordplanner (vraagt een Ads-account). De volumes in de CSV zijn daarom schattingen en moeten in de eerste maand worden vervangen door Zoekwoordplanner-cijfers.
