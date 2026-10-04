# M6 Webshop en operatie: setup-blauwdruk met kosten voor Bline Sleep (status oktober 2026)

Leeswijzer: per vraag staan feiten met bron (Cited Findings), daarna eigen afleidingen (Inferences) en open punten (Gaps). Bedragen zijn excl. btw tenzij anders vermeld. USD-bedragen zijn waar nodig indicatief omgerekend tegen circa 1 USD = EUR 0,85 tot 0,90; die koers is niet in dit onderzoek geverifieerd. Bronnen zijn deels blogs/aggregators (gemarkeerd als "claim"); primaire bronnen zijn waar mogelijk gebruikt (Shopify, GS1, Douane, PostNL, leveranciers).

## 1. Platform: Shopify-abonnement, alternatieven en thema

### Takeaway
Shopify Basic (EUR 28/mnd maandelijks, EUR 21 bij jaarbetaling) volstaat voor de start; Grow (EUR 78 / EUR 59) pas bij meerdere medewerkers of lagere kaarttarieven. Lightspeed (vanaf EUR 68/mnd) en WooCommerce (hosting EUR 10-50/mnd plus eigen uren) zijn geen betere keuze voor een klein team dat snel wil lanceren met apps voor levertijd, reviews en Klaviyo. Premium thema Prestige (USD 400 eenmalig) of Impact (circa USD 380) past bij een premium home-merk.

### Cited Findings
- Shopify NL 2026: Basic EUR 28/mnd (maandelijks) of EUR 21/mnd (jaarlijks); Grow EUR 78/mnd of EUR 59/mnd jaarlijks; prijzen excl. btw, stand september 2026 (claim, agency-blog): [bedrijfssoftwaregids.nl](https://bedrijfssoftwaregids.nl/blog/shopify-prijzen-nederland-2026/); [Flatline Agency](https://www.flatlineagency.com/blog/shopify-costs)
- Basic bevat 2 staff accounts, Grow 5 (claim): [bedrijfssoftwaregids.nl](https://bedrijfssoftwaregids.nl/blog/shopify-prijzen-nederland-2026/)
- Bij een externe PSP (Mollie, MultiSafepay, Pay.nl) rekent Shopify extra transactiekosten: Basic 2%, Grow 1%, Advanced 0,6%, Plus 0,2%, over het volledige orderbedrag incl. btw en verzending, bovenop de PSP-kosten: [Flatline Agency, Shopify Payments vs PSP's](https://www.flatlineagency.com/blog/shopify-payments-vs-third-party-psps)
- Lightspeed eCom 2026: Essential EUR 68/mnd (250 varianten), Advanced EUR 120/mnd (5.000 varianten), Professional EUR 259/mnd; variantlimieten zijn harde grenzen (claim): [codemaker-s.com](https://codemaker-s.com/platform/lightspeed)
- WooCommerce: geen platformabonnement of platform-transactiekosten; hosting circa EUR 10-50/mnd plus betaalde thema's/extensies en eigen uren (claim): [bedrijfssoftwaregids.nl WooCommerce review](https://bedrijfssoftwaregids.nl/blog/woocommerce-review-2026/); [codemaker-s.com](https://codemaker-s.com/platform/lightspeed)
- Judge.me heeft per 31 januari 2026 WooCommerce, BigCommerce en andere platformen verlaten (alleen nog Shopify) (claim): [WiserReview](https://wiserreview.com/blog/okendo-vs-judge-me/)
- Prestige (Maestrooo) kost USD 400 eenmalig, gepositioneerd voor luxe- en lifestylemerken: [Avada](https://avada.io/blog/prestige-theme-shopify/); [BSS Commerce](https://bsscommerce.com/shopify/prestige-shopify-theme/)
- Impact (Maestrooo) circa USD 380 eenmalig; premium thema's kosten USD 140-400 eenmalig en worden pas betaald bij publiceren (claim): [Charle Agency](https://www.charleagency.com/articles/best-shopify-themes/)

### Inferences
- Shopify Payments gebruiken is vrijwel verplicht om de 2% extra fee op Basic te vermijden; daarmee vervalt Riverty (alleen via externe PSP) in de startfase (zie vraag 2).
- Thema-advies: Prestige voor een rustige, editorial premium uitstraling (grote beelden, verhaal); Impact als je meer conversie-elementen (USP-balken, bundels, vergelijkingen) wilt. Beide van dezelfde maker, dus vergelijkbare kwaliteit. Gratis Dawn/Horizon is een valide budgetstart.
- WooCommerce valt af door onderhoudslast voor een team van 2 plus agent; Lightspeed biedt geen voordeel boven Shopify voor D2C zonder fysieke winkel.

### Gaps
- Exacte actuele prijs op shopify.com/nl/pricing niet rechtstreeks opgehaald (alleen via secundaire bronnen met datum september 2026).
- Geen onafhankelijke data over conversieverschil tussen Prestige, Impact en gratis thema's.

## 2. Betalingen: Shopify Payments, iDEAL, Bancontact, Klarna, Riverty, fraude

### Takeaway
Shopify Payments is beschikbaar in NL en BE en dekt iDEAL (EUR 0,29), Bancontact (EUR 0,39), Klarna (2,99% + EUR 0,35) en kaarten (1,9% + EUR 0,25 op Basic). Klarna via Shopify Payments wordt uitbetaald in de eerstvolgende Shopify-payout en Klarna draagt het wanbetalingsrisico; Bline krijgt dus vooraf betaald. Let op: Shopify-verwerkingskosten worden bij refunds niet terugbetaald, relevant bij de 100-nachten-proefperiode.

### Cited Findings
- Shopify Payments NL-tarieven (september 2026): kaarten 1,9% + EUR 0,25 (Basic), 1,8% (Grow), 1,6% (Advanced); Amex/internationaal 2,9%/2,8%/2,6% + EUR 0,25; iDEAL EUR 0,29 per transactie; Bancontact EUR 0,39 (Advanced/Plus EUR 0,29); Klarna 2,99% + EUR 0,35 (Plus 2,19% + EUR 0,35): [Flatline Agency](https://www.flatlineagency.com/blog/shopify-payments-vs-third-party-psps)
- Er wordt in NL geen btw geheven over Shopify Payments-verwerkingskosten (claim): [samenvatting zoekresultaten, o.a. Flatline/Letstalkshop](https://www.letstalkshop.com/blog/shopify-payment-gateways-comparison-by-country)
- Shopify Payments werkt in NL en BE; iDEAL, kaarten, Klarna (Pay Later, Slice It, Pay Now) en Bancontact zijn beschikbaar; uitbetalingen starten pas na goedkeuring/verificatie (1-3 werkdagen); Riverty niet genoemd: [web-builders.nl](https://web-builders.nl/en/blog/shopify-payments-netherlands/)
- Shopify (primair, NL-blog): bij Klarna via Shopify Payments wordt "een goedgekeurde betaling opgenomen in je volgende Shopify Payments-uitbetaling"; Klarna neemt het betaalrisico van de consument binnen hun voorwaarden; bij terugbetaling worden de Shopify Payments-kosten niet terugbetaald; Klarna-refunds kunnen tot 180 dagen na de eerste afschrijving: [Shopify NL, Wat is Klarna](https://www.shopify.com/nl/blog/wat-is-klarna)
- Riverty via Mollie: 2,99% + EUR 0,35 in NL/BE/DE/AT; merchant krijgt vooraf en volledig betaald door Mollie; settlement-vertraging 5 werkdagen; Riverty draagt wanbetalingsrisico: [Mollie, Riverty](https://www.mollie.com/payments/riverty)
- Consument: Klarna geeft 30 dagen betaaltermijn en betalen in 3 delen; Riverty 14 dagen (claim): [Dutch Cowboys](https://www.dutchcowboys.nl/online/dit-is-het-verschil-tussen-riverty-en-klarna)
- PreProduct "charge later" en "deposit" werken door de kaart te vaulten via Shopify, PayPal of Stripe; iDEAL-ondersteuning niet vermeld: [PreProduct](https://preproduct.io/); [PreProduct deposits](https://preproduct.io/shopify-deposit-payments/)

### Inferences
- Rekenvoorbeeld dekbed EUR 249: iDEAL EUR 0,29 (0,1%); kaart EUR 4,98 (2,0%); Klarna EUR 7,80 (3,1%). Bij een retour via Klarna blijft circa EUR 7,80 kosten achter. Bij een retourpercentage van 10% op de proefperiode is dat beheersbaar, maar neem het mee in de unit economics.
- Riverty niet nodig bij start: Klarna dekt "achteraf betalen" binnen Shopify Payments. Riverty toevoegen via Mollie kost op Basic 2% extra Shopify-fee bovenop 2,99%, dus circa 5% per order.
- iDEAL is een directe betaling en is niet te vaulten voor "later afschrijven"; voor een Nederlands publiek is "volledige betaling bij bestelling" met een duidelijke leverdatum daarom het enige praktische model. Deposit/charge-later pre-orders (PreProduct) werken in NL alleen goed voor kaartbetalers. Bline hoeft dit ook niet: 8-12 werkdagen levertijd is gewone verkoop met langere levertijd, geen pre-order van nog niet geproduceerde voorraad.
- Fraude: Shopify Payments heeft standaard fraudeanalyse (niet geverifieerd in deze ronde); iDEAL en Bancontact zijn bankgeautoriseerd en kennen geen chargebacks zoals kaarten; Klarna draagt het kredietrisico. Het grootste resterende risico is kaartchargebacks en misbruik van de proefperiode (bijv. herhaald retourneren). Advies: maximum van 1 proefperiode-retour per klant/adres per jaar in de voorwaarden.
- Multi-currency later: Shopify Markets/Payments kan valuta's tonen; voor NL/BE is alles EUR, dus pas relevant bij DE/UK/CH-uitbreiding.

### Gaps
- Uitbetalingsfrequentie van Shopify Payments in NL (dagelijks/wekelijks) niet bevestigd in primaire bron.
- Shopify Payments-fraudetools (Shopify Protect is niet in EU beschikbaar volgens eerdere kennis) niet geverifieerd voor NL 2026.
- Of Klarna-tarief via Shopify Payments in BE gelijk is aan NL niet bevestigd.

## 3. Apps: reviews, e-mail/SMS, levertijd/pre-order, bundels, abonnementen

### Takeaway
Een lean app-stack kost bij de start circa EUR 30-110/mnd: Judge.me (gratis of USD 15), Klaviyo (gratis tot 250 profielen, daarna USD 20-30), een levertijd-/backorder-app als STOQ (USD 10) of een eigen theme-snippet met metafield, en eventueel Gorgias Starter. Okendo (USD 119) en PreProduct (USD 59,99) zijn voor de start overkill.

### Cited Findings
- Judge.me: Forever Free (USD 0, onbeperkte reviewverzoeken, met branding) en Awesome USD 15/mnd vlak, zonder ordertoeslag; 500.000+ winkels: [WiserReview Judge.me](https://wiserreview.com/blog/judge-me-review/); [WiserReview Okendo vs Judge.me](https://wiserreview.com/blog/okendo-vs-judge-me/)
- Okendo: Essential USD 19, maar realistisch Growth USD 119/mnd omdat Essential AI-samenvattingen, Google Shopping-sterren en Klaviyo-integratie uitsluit (claim): [WiserReview](https://wiserreview.com/blog/okendo-vs-judge-me/)
- Klaviyo 2026: gratis tot 250 actieve profielen (500 e-mails/mnd, 150 SMS-credits); Email USD 20/mnd bij 500 profielen, USD 30 bij 1.000, USD 150 bij 10.000; Email+SMS vanaf USD 60/mnd (1.250 SMS-credits); facturatie op actieve profielen: [Emailtooltester](https://www.emailtooltester.com/en/reviews/klaviyo/pricing/); [Omnisend blog](https://www.omnisend.com/blog/klaviyo-pricing/)
- Klaviyo SMS naar NL: 12 credits per bericht, circa USD 0,108 per SMS (claim): [FirstPier](https://www.firstpier.com/resources/sms-klaviyo-pricing)
- STOQ: vlak USD 10/29/69 per maand, Shopify Markets en rapportage op elk betaald plan; toont verwachte leverdatum en schakelt product automatisch naar backorder (bron is de leverancier zelf): [STOQ pricing](https://www.stoqapp.com/pricing); [STOQ vs Timesact](https://www.stoqapp.com/compare/stoq-vs-timesact)
- Timesact: vaste plannen gekoppeld aan Shopify-plan, USD 23 op Basic tot USD 147 op Plus; flexibele plannen USD 0,20-0,30 per order boven 10 (bron: concurrent STOQ, dus met voorzichtigheid): [STOQ vs Timesact](https://www.stoqapp.com/compare/stoq-vs-timesact); [Timesact](https://timesact.com/)
- PreProduct: Starter USD 0 + 5% van pre-order-omzet; Scale USD 59,99/mnd (0% tot USD 5k/mnd, daarna 0,5%); Scale Plus USD 259,99; ondersteunt charge upfront, charge later, deposit, payment plans via Shopify Payments, Shopify Flow en Klaviyo-events, API: [PreProduct](https://preproduct.io/)
- Okendo "never left Shopify"; Yotpo-prijzen niet gevonden in deze ronde.

### Inferences
- Reviews: Judge.me gratis tot lancering, Awesome (USD 15) zodra branding weg moet en Google Shopping-sterren gewenst zijn. Okendo pas zinvol bij quiz/attributen (bijv. "warmteslaper/koude slaper") op schaal.
- Klaviyo: start gratis; post-purchase flow over batchstatus ("je dekbed is onderweg vanuit onze atelierpartner", "aangekomen in NL") is hier belangrijker dan marketingmail, omdat de levertijd 8-12 werkdagen is. SMS voorlopig niet (NL-klanten verwachten WhatsApp of e-mail; SMS kost ~USD 0,11/stuk).
- Levertijd-app: STOQ Starter USD 10 is de goedkoopste kant-en-klare optie. Alternatief zonder app: een theme-snippet (Liquid) die een shop-metafield "volgende_verzenddatum" en "levervenster" toont, wekelijks bijgewerkt door n8n (zie vraag 4 en 8). Dat geeft exact de gewenste "bestel voor woensdag 23:59, verwacht di 20 okt tot vr 23 okt".
- Bundels (dekbed + kussen + hoes): Shopify heeft een eigen gratis Bundles-app (niet geverifieerd in deze ronde); alternatief is een vaste bundel-SKU in de fabriek, wat inpakken per order eenvoudiger maakt.
- Abonnementen: niet zinvol voor dekbedden (aankoopcyclus jaren). Eventueel later voor kussenslopen/hoeslakens of een "verfris-abonnement", maar geen prioriteit.

### Gaps
- Yotpo 2026-prijzen niet gevonden.
- Of STOQ/Timesact een terugkerende "wekelijkse batchdatum" automatisch kunnen berekenen (in plaats van een vaste datum per product) is niet bevestigd; documentatie noemt alleen vaste verzendtekst/datum per product.

## 4. Leverdatum per wekelijkse drop en voorraadmodel in Shopify

### Takeaway
Behandel fabrieksvoorraad als een eigen Shopify-locatie ("Fabriek CN") met echte aantallen die de agent wekelijks doorgeeft, en later een tweede locatie ("eFreight NL") voor gebufferde bestsellers. Toon een berekende leverdatum op basis van de batchcyclus (cut-off woensdag, verzending donderdag) via metafields of een simpele app. Vooraf volledig betalen is het juiste model; "pre-order"-functionaliteit is niet nodig.

### Cited Findings
- Luchtvracht Shanghai-Amsterdam: circa USD 4,3/kg met transittijd 5-7 dagen (september 2026); voor zendingen vanaf 500 kg vanaf 29,4 CNY/kg met 2-7 dagen transit (claim, forwarder-site): [Sino Shipping](https://www.sino-shipping.com/freight-china-netherland/)
- Flexport-indicaties Shanghai-Amsterdam: Deferred USD 6,29/kg (8 dagen), Standard USD 6,51/kg (6 dagen), Express USD 8,69/kg: [Flexport rates](https://www.flexport.com/rates/shanghai-china/amsterdam-netherlands)
- STOQ toont een verwachte leverdatum en verzendtekst op de productpagina: [STOQ](https://www.stoqapp.com/compare/stoq-vs-timesact)
- n8n heeft een Shopify-node (orders get/getAll/create/update/delete, productbewerkingen) en een Shopify Trigger (webhooks zoals orders/create): eigen controle in n8n-repository `packages/nodes-base/nodes/Shopify/` (ShopifyTrigger.node.ts, OrderDescription.ts).

### Inferences
- Tijdlijn (afleiding uit 5-7 dagen transit plus inklaring plus PostNL 1 dag): bestelling ma-wo, verzending do, aankomst AMS ~di/wo volgende week, inklaring 1-2 werkdagen, crossdock en PostNL-overdracht do/vr, bezorging vr/ma. Dat is 6-9 werkdagen na een woensdagorder. Een bestelling op donderdag wacht een week extra: tot circa 11-13 werkdagen. "8-12 werkdagen" klopt gemiddeld; beter is een dynamisch venster per besteldag.
- Datumlogica voor de site (voorstel): volgende_verzenddatum = eerstvolgende donderdag na de cut-off (wo 23:59); verwacht_vanaf = verzenddatum + 7 werkdagen; verwacht_tot = verzenddatum + 9 werkdagen; feestdagen (Koningsdag, Chinese feestdagen zoals Golden Week begin oktober en Chinees Nieuwjaar) in een tabel uitsluiten.
- Voorraadmodel: locatie "Fabriek CN" met "track quantity" aan en "doorgaan met verkopen als uitverkocht" uit, zodat je niet verkoopt wat de fabriek niet heeft. Bij lage aantallen eventueel overselling toestaan per variant met tag "levering-batch". Metafields: product.metafields.bline.bron = fabriek/nl, shop.metafields.bline.volgende_batch, order-tag "batch-2026-W42".
- Bij NL-buffervoorraad: Shopify routeert naar de NL-locatie; de productpagina toont dan "1-2 werkdagen" voor die variant (product/variant-metafield of locatie-afhankelijke tekst).
- Juridisch: bij verkoop op afstand is levertijd vooraf duidelijk tonen verplicht; zonder afspraak geldt maximaal 30 dagen (algemene kennis, niet in deze ronde geverifieerd).

### Gaps
- Werkelijke transit- en inklaringstijd bij eFreight voor kleine wekelijkse batches (50-200 kg) niet gevonden; offerte nodig.
- Directe vluchten/routes vanuit Hangzhou (HGH) naar AMS en hun prijs niet gevonden; Hangzhou-vracht loopt vaak via Shanghai (PVG), niet bevestigd.

## 5. Orderflow, EAN, verpakken, douane, crossdock en kosten per stap

### Takeaway
Advies: fabriek pakt per klantorder in een Bline-doos met orderbarcode (geen vervoerderslabel), alles in een geconsolideerde B2B-luchtzending op naam van Bline als importeur; eFreight klaart in als één aangifte en plakt bij aankomst per pakket het PostNL/DHL-label (crossdock). Indicatief kost de logistieke keten per dekbed circa EUR 30-40 bij 25 orders per week, waarvan luchtvracht (afhankelijk van volumegewicht) de grootste post is. De nieuwe EUR 3-douaneheffing (sinds 1 juli 2026) geldt niet voor deze B2B-import.

### Cited Findings
- GS1 Nederland 2026 (primair): 1 losse artikelcode EUR 37 eenmalig; codepakket 10 codes EUR 61/jaar; 100 codes EUR 92/jaar; 1.000 codes EUR 189/jaar; plus jaarlijkse GS1-bijdrage EUR 28 bij omzet EUR 0-1 mln; alles excl. btw: [GS1 Nederland tarieven](https://www.gs1.nl/producten-services/digital-identity/tarieven/). Let op: secundaire bron noemt een starterpakket 10 codes EUR 55/jaar en pakket 100 EUR 85, vermoedelijk verouderd: [Boloo](https://boloo.co/blog/gs1-ean-codes)
- Douane (primair): sinds 1 juli 2026 vervalt de vrijstelling van invoerrechten onder EUR 150 en geldt EUR 3 per artikelsoort, maar alleen voor "goederen met een waarde van maximaal EUR 150 die een verkoper van buiten de EU rechtstreeks levert aan een consument in de EU"; niet voor een NL-bedrijf dat bulkvoorraad importeert: [Douane, invoerrechten e-commerce](https://www.douane.nl/onderwerpen/invoer-en-uitvoer/invoer/aangifte-doen/aangifte-doen-bij-e-commerce/invoerrechten-betalen-voor-e-commerce/)
- Inklaringskosten (algemeen, niet eFreight-specifiek): gemiddeld EUR 50-150 per aangifte; zendingen < EUR 1.000 EUR 50-80; EUR 1.000-10.000 EUR 80-150; bij luchtvracht daarnaast afhandelingskosten EUR 50-200 per zending en beveiligingstoeslagen EUR 15-50 (claim, contentsite): [Illustrify](https://illustrify.nl/inzichten/inklaringskosten/); [KVK over expediteurs](https://www.kvk.nl/internationaal/de-expediteur-helpt-importeurs-met-transport-en-inklaren/)
- Luchtvrachttarieven Shanghai-AMS: USD 4,3/kg (5-7 dagen) tot USD 6,29-8,69/kg afhankelijk van service: [Sino Shipping](https://www.sino-shipping.com/freight-china-netherland/); [Flexport](https://www.flexport.com/rates/shanghai-china/amsterdam-netherlands). Luchtvrachttarieven daalden 2% maand-op-maand in september 2026 (claim): [Sino Shipping](https://www.sino-shipping.com/freight-china-netherland/)
- E-Freight Forwarding (primair): diensten air freight, ocean freight, road transport, consolidation, fulfilment, e-commerce, volledige douane-inklaring; adres Lindeboomseweg 57, Amersfoort; offerte-reactie binnen 24 uur; geen prijzen, crossdock, retouren of België genoemd: [E-Freight Forwarding](https://www.efreightforwarding.com/en)
- E-Freight huurt circa 20.000 m2 logistieke ruimte aan de Vanadiumweg in Amersfoort om lucht- en zeevracht uit China, douane, opslag, fulfilment en Europese distributie uit te breiden (september 2026): [Nieuwsblad Transport](https://www.nt.nl/logistiek/2026/09/23/e-freight-forwarding-huurt-20-000-m%C2%B2-logistieke-ruimte-in-amersfoort/)
- Monta: fulfilmentkosten per order vanaf EUR 2,95 (pick/pack, materiaal, arbeid), maar offertes op maat; geen gepubliceerd crossdocktarief: [Monta tarieven](https://monta.nl/fulfilment/tarieven/); [Monta BE prijzen](https://gomonta.com/nl-be/fulfilment/prijzen-fulfilment/)
- PostNL zakelijke pakketten NL 2026 (excl. btw): 100-250 pakketten/jaar EUR 7,40; 250-500 EUR 7,35; 500-1.000 EUR 7,30; 1.000-2.500 EUR 7,00; 2.500-5.000 EUR 6,85: [PostNL zakelijke pakkettarieven 2026 (pdf)](https://www.postnl.nl/api/assets/blt43aa441bfc1e29f2/blt1ea4757b14457356/zakelijke-pakkettarieven-2026.pdf)
- PostNL België (verzending binnen België door BE-klanten): 0-500 pakketten/jaar EUR 6,02 (afhaalpunt) of EUR 6,72 (thuis); 1.000-5.000 EUR 5,50/6,20: [PostNL BE tarieven](https://www.postnl.be/zakelijke-oplossingen/tarieven/)

### Inferences
- Waarom labels in NL en niet in China: adreswijzigingen, annuleringen en douanecontroles blijven mogelijk tot aankomst; vervoerderslabels hebben een beperkte geldigheid en vervoerderscontracten zitten bij eFreight/Bline. De fabriek plakt alleen een orderlabel (ordernummer + QR/Code128) en een paklijst; eFreight scant en print het vervoerderslabel (crossdock). Alternatief (fabriek print PDF-labels) is mogelijk maar riskanter.
- Douane: één importaangifte per week op naam van Bline (importeur met EORI), met commerciële factuur en paklijst per batch. Invoer-btw kan in NL via een artikel 23-vergunning worden verlegd (algemene kennis, niet in deze ronde geverifieerd; check bij eFreight). Invoerrechten op dekbedden/beddengoed hangen af van de GN-code; zie module over douane/product.
- Luchtvracht en volumegewicht: dekbedden zijn licht maar volumineus; luchtvracht rekent doorgaans op volumegewicht (gangbare deler 6.000 cm3/kg, niet geverifieerd in deze ronde). Een niet-gecomprimeerd dekbed van 60x45x20 cm weegt volumetrisch circa 9 kg; vacuumverpakt naar 40x30x15 cm circa 3 kg. Vacuumverpakking (of rolverpakking) is daarmee de grootste kostenhefboom.
- Kosten per stap (indicatief, voorbeeld 25 dekbedden per week, 3-4 kg belastbaar gewicht per stuk, 75-100 kg per batch):
  - EAN: GS1 100 codes EUR 92 + bijdrage EUR 28 = circa EUR 120/jaar (EUR 10/mnd).
  - Luchtvracht: 3,5 kg x circa USD 5-7/kg all-in voor kleine batches = circa EUR 15-21 per dekbed (kleine batches liggen boven de USD 4,3 marktprijs voor grotere zendingen).
  - Afhandeling luchthaven + inklaring: EUR 100-250 per week / 25 = EUR 4-10 per order.
  - Crossdock/scannen/label plakken per pakket: geen publieke prijs; schatting EUR 1-2,50 (onder Monta's EUR 2,95 voor volledige pick/pack).
  - PostNL pakket NL: EUR 7,40 (lage volumes); eFreight heeft vermoedelijk scherpere tarieven via eigen contracten.
  - Totaal: circa EUR 28-41 per order bij 25 orders/week; bij 100 orders/week daalt inklaring naar EUR 1-2,50 per order en luchtvracht per kg ook.
- Bij bestsellers in NL-buffer (zeevracht naar eFreight-opslag) verschuift de kost naar opslag en pick/pack (circa EUR 3+ per order) en dalen vrachtkosten per stuk sterk; dat is de logische stap zodra een SKU voorspelbaar loopt.

### Gaps
- Concrete eFreight-tarieven (luchtvracht kleine batches, inklaring per aangifte, crossdock per pakket, opslag, retourverwerking, vervoerderstarieven NL/BE) zijn niet publiek; offerte aanvragen met dit exacte scenario.
- PostNL-tarief NL naar BE vanuit een NL-zakelijk contract niet gevonden in deze ronde (PostNL-tarievenboekje juli 2026 niet uitgelezen); DHL eCommerce NL/BE-tarieven niet gevonden.
- Minimale chargeable weight / minimumtarieven per luchtvrachtzending (vaak per 45/100 kg-breaks) niet gevonden.
- Of de fabriek kan inpakken per order met eigen QR-labels en paklijsten: afhankelijk van fabriek/agent, niet onderzocht.

## 6. Klantenservice, WhatsApp, retouren en B-keuze

### Takeaway
Start met een gedeelde inbox (Shopify Inbox of Gmail) plus duidelijke FAQ over levertijd; stap over op Gorgias Starter/Basic (USD 10-60/mnd) zodra er meer dan circa 50 tickets per maand zijn. Retouren via een retourportaal (Sendcloud vanaf circa EUR 40-87/mnd, of eFreight-oplossing) naar eFreight; B-keuze via een eigen outletpagina en/of opkopers als 2dekansje.com.

### Cited Findings
- Gorgias 2026: Starter USD 10/mnd (50 tickets), Basic USD 60 (300 tickets), Pro USD 360 (2.000), Advanced USD 900 (5.000); overage USD 0,36-0,40 per ticket; AI-agent USD 1,00 per volledig opgeloste interactie (maandcontract), telt ook als ticket; facturatie per ticket, niet per seat: [Chatarmin](https://chatarmin.com/en/blog/gorgias-pricing); [eesel.ai](https://www.eesel.ai/blog/gorgias-ai-pricing-complete-2026-cost-breakdown-and-guide)
- Sendcloud: retourportaal beschikbaar op Growth, Premium en Pro; branded portaal, labelloze retouren, QR-codes, regels per product/land/reden, meertalig. Prijzen in bronnen conflicteren: "Lite EUR 87/mnd + EUR 0,09 per label" en "Growth EUR 175/mnd + EUR 0,08 per label" versus "Small Shop vanaf EUR 40/mnd": [Sendcloud pricing](https://www.sendcloud.com/pricing/); [Capterra](https://www.capterra.com/p/189663/SendCloud/); [Sendcloud help retourportaal](https://support.sendcloud.com/hc/en-us/articles/360025142691-How-do-I-set-up-my-return-portal)
- bol-retouren: met ongeveer een derde van de retouren is iets mis; verpakkingsschade wordt verkocht als "Retourdeals", gebruikssporen via partner BuyBay als "Retourkansjes" op bol, Blokker, eBay en Amazon: [Kassa/BNNVARA](https://www.bnnvara.nl/kassa/artikelen/tweedekansje-of-als-nieuw-verkocht-dit-gebeurt-er-met-jouw-retourpakketje)
- 2dekansje.com neemt als B2B-partner retouren van webwinkels over en verzorgt grading, opslag en verkoop via eigen kanalen: [2dekansje.com](https://www.2dekansje.com/service/b2b-partner-worden/)
- bol-partners kunnen bol-retourlabels tegen gereduceerd tarief gebruiken of retouren zelf regelen: [bol partnerplatform](https://partnerplatform.bol.com/nl/idp/retouropties)

### Inferences
- SLA-voorstel: reactie binnen 1 werkdag (ma-vr), Nederlandstalig, met standaardantwoorden voor "waar is mijn bestelling" gekoppeld aan batchstatus. Proactieve batch-mails (vraag 3) verlagen WISMO-tickets het meest bij 8-12 werkdagen levertijd.
- WhatsApp: populair in NL; kan via WhatsApp Business (gratis app) of via helpdesk-integratie; kosten van WhatsApp Business API via Gorgias niet gevonden.
- Hygiëne: dekbedden die geslapen zijn (100-nachten-proef) kunnen niet als nieuw terug in de verkoop. Opties: reinigen en als B-keuze op eigen outletpagina, verkoop via 2dekansje-achtige opkopers, of doneren. Dit moet in de marge-calculatie (proefretour = vrijwel volledig verlies op vracht en deels op product).
- Retourportaal: omdat retouren naar eFreight gaan, eerst vragen of eFreight een retourportaal/retourlabelservice levert; anders Sendcloud of het gratis Shopify-klantaccount "retour aanvragen" plus PostNL-retourlabel via n8n.
- B-keuze op bol: bol heeft geen bevestigde "2ndChance"-verkopersprogramma voor partners gevonden; een B-keuze-aanbod als aparte conditie op bol (tweedehands/"zo goed als nieuw") is niet geverifieerd.

### Gaps
- Kosten WhatsApp-kanaal in Gorgias/Zendesk niet gevonden; Zendesk-prijzen en Shopify Inbox (gratis, niet geverifieerd) niet onderzocht.
- ReturnGo-prijzen niet onderzocht.
- PostNL-retourlabeltarief niet gevonden.
- Hoe bol omgaat met B-keuze-aanbiedingen van externe partners (conditie "tweedehands") niet bevestigd.

## 7. Boekhouding, Moneybird en multi-currency

### Takeaway
Shopify koppelen aan Moneybird kan met een app (circa EUR 15 tot USD 54/mnd) of met de bestaande n8n-setup van Shop4You via de Moneybird-API (geen native n8n-node; HTTP Request). Voor een tweede administratie (Bline als aparte bv/handelsnaam) is een standaardapp de snelste start; n8n is goedkoper zodra de flows staan.

### Cited Findings
- Combidesk Moneybird Bookkeeping USD 18-54/mnd afhankelijk van synchronisatiesnelheid en Shopify Payments-boeking; Moneybird Accounting vanaf USD 12,99/mnd; boekhoudkoppelingen.nl EUR 15 per administratie per maand (EUR 180/jaar); Make vanaf USD 9/mnd, Zapier vanaf USD 19,99/mnd; maatwerk indicatief EUR 1.500-15.000 (claim, vergelijkingssite): [Riverflows](https://riverflowsbv.com/koppelingen/shopify-moneybird); [Shopify App Store Moneybird Accounting](https://apps.shopify.com/moneybird-4); [boekhoudkoppelingen.nl](https://boekhoudkoppelingen.nl/koppeling/shopify-moneybird)
- Na koppeling wordt per betaalde bestelling automatisch een verkoopfactuur in Moneybird aangemaakt: [Riverflows](https://riverflowsbv.com/koppelingen/shopify-moneybird)
- n8n-repository bevat geen native Moneybird-, Klaviyo-, Gorgias-, Sendcloud- of PostNL-node; wel Shopify en Shopify Trigger: eigen controle `packages/nodes-base/nodes/` in deze repository.

### Inferences
- Belangrijk voor de boekhouding: Shopify Payments-payouts zijn netto (omzet minus kosten minus refunds); de koppeling moet payouts en kosten apart boeken, anders klopt de bankreconciliatie niet. Daarom de variant die "uitbetalingen" meeneemt (Combidesk hoger tier of Moneybird Accounting "orders en uitbetalingen").
- Importkosten (vracht, inklaring, invoer-btw/verlegging) komen als inkoopfacturen van eFreight; de agentfacturen in USD/CNY moeten met koers geboekt worden (Moneybird ondersteunt vreemde valuta, niet geverifieerd).
- Multi-currency: niet nodig voor NL/BE (EUR). Bij latere uitbreiding naar DE geen valuta-issue; UK/CH vereisen Shopify Markets-valuta en aparte btw/douane.

### Gaps
- Of Shop4You en Bline één Moneybird-administratie delen of apart moeten (rechtsvorm) valt buiten deze module.

## 8. Productfotografie, video en 3D/AI-beelden

### Takeaway
Een packshotset kost circa EUR 8-15 per beeld; een sfeershoot met locatie, styling en nabewerking circa EUR 1.500-2.500; een studiodag EUR 1.150-1.800. Voor een premium slaapmerk is minimaal één echte sfeershoot nodig (textuur, licht, bed-styling); AI/3D is geschikt voor varianten (kleuren, maten, achtergronden) en advertentievariaties, mits het product niet misleidend wordt weergegeven.

### Cited Findings
- Packshot op wit EUR 5-25 per product indicatief; standaard packshot EUR 8-15 per beeld; bij een aanbieder eerste foto EUR 29, extra foto van hetzelfde product EUR 9; tien producten fotograferen EUR 200-600 (claim, aanbieders/contentsites): [de-product-fotograaf.nl](https://de-product-fotograaf.nl/productfotografie-kosten/); [Oase Creative](https://oasecreative.nl/kennisbank/productfotografie-kosten-2026); [Fotofy](https://fotofy.nl/tarieven)
- Sfeer-/lifestyleshoot met locatie, styling en editing EUR 1.500 tot soms EUR 2.500; studiodag EUR 1.150-1.799; gemiddeld uurtarief EUR 94 (claim): [Oase Creative](https://oasecreative.nl/kennisbank/productfotografie-kosten-2026); [Viralistic](https://viralistic.nl/blog/en/product-photography-costs); [offertje.nl](https://offertje.nl/blog/wat-kost-een-fotograaf/)

### Inferences
- Budget launch (afleiding): packshots 3 SKU's x 6 beelden x EUR 12 = circa EUR 220; 1 sfeershoot EUR 2.000; korte productvideo's (vulling, gewicht, "fluffiness") vaak in dezelfde dag mee te nemen, prijs niet gevonden. Totaal circa EUR 2.500-4.000 eenmalig.
- AI/3D: geschikt voor achtergrond- en kleurvarianten en voor advertentietests; voor textuur en vulling (dons/microvezel) blijft echte fotografie geloofwaardiger. Productweergave moet overeenkomen met het werkelijke product (anders risico op misleiding en retouren).
- Fabriek/agent kan referentiefoto's en korte video's leveren (vullen, naaien, QC), wat ook bruikbaar is als "made with care"-content; kwaliteit wisselend.

### Gaps
- Prijzen voor korte productvideo's en Reels/UGC-creators in NL niet gevonden in deze ronde.
- Geen bron gevonden over consumentenacceptatie van AI-productbeelden in de beddengoedcategorie.

## 9. Integratie met n8n: wat eerst automatiseren

### Takeaway
Automatiseer eerst de wekelijkse batch-export (woensdag 23:59): alle betaalde, onverzonden orders taggen met "batch-JJJJ-WW", paklijst plus orderlabels (PDF/CSV) naar agent/fabriek, en pre-alert met commerciële factuur naar eFreight. Daarna de leverdatum-metafield en klantstatusmails. Moneybird draait al bij Shop4You en kan hergebruikt worden.

### Cited Findings
- n8n Shopify-node ondersteunt orders (get, getAll, create, update, delete) en producten; Shopify Trigger ontvangt webhooks (onder meer order create/paid): eigen controle in `packages/nodes-base/nodes/Shopify/` (OrderDescription.ts, ShopifyTrigger.node.ts) in deze repository.
- Geen native n8n-nodes voor Moneybird, Klaviyo, Gorgias, Sendcloud of PostNL in deze repository; integratie via HTTP Request-node: eigen controle `packages/nodes-base/nodes/`.
- PreProduct biedt Shopify Flow-acties/triggers, Klaviyo-events en een REST API: [PreProduct](https://preproduct.io/)

### Inferences
- Prioriteit 1, wekelijkse batch (Cron wo 23:59 of do 06:00): Shopify orders ophalen (status paid, unfulfilled, niet getagd) → tag "batch-2026-W42" → Google Sheet per batch (SKU-totalen + regel per order) → PDF-paklijsten en orderlabels met QR → e-mail naar agent; commerciële factuur/paklijst naar eFreight als pre-alert.
- Prioriteit 2, leverdatum: wekelijks een shop-metafield bijwerken (volgende verzenddatum, venster) via Shopify GraphQL Admin API in een HTTP Request-node (de standaard Shopify-node dekt metafields niet volledig; niet in detail geverifieerd).
- Prioriteit 3, klantstatus: events "verzonden vanuit fabriek" (do), "aangekomen en ingeklaard" (na eFreight-melding), "track & trace" (na crossdock) naar Klaviyo (HTTP Request) of Shopify-notificaties. Dit voorkomt de meeste klantvragen.
- Prioriteit 4, boekhouding: hergebruik bestaande Moneybird-flows; voeg payouts en eFreight-inkoopfacturen toe.
- Prioriteit 5, retouren: retourverzoek (formulier of portaal) → label → bij ontvangst bij eFreight refund in Shopify + B-keuze-voorraad in Sheet/Shopify.
- Later: voorraadsync met fabriek (wekelijkse telling van agent in Sheet → Shopify-locatie "Fabriek CN"), bol-koppeling voor B-keuze of buffervoorraad.

### Gaps
- Of eFreight een API of webhook heeft voor statusupdates (aankomst, inklaring, track & trace) is onbekend; anders e-mailparsing in n8n.

## 10. Maandelijks kostenoverzicht (indicatief, afleiding)

### Takeaway
Vaste software- en abonnementskosten bij start: circa EUR 75-200/mnd (lean) tot EUR 300-450/mnd (comfortabel). Variabele kosten per dekbedorder: betaling EUR 0,29-8, logistiek circa EUR 28-41 bij 25 orders per week. Eenmalig: thema circa EUR 350, fotografie EUR 2.500-4.000, EAN-instap circa EUR 120/jaar.

### Cited Findings
- Alle onderliggende bedragen staan met bron in vragen 1 tot en met 8 (Shopify, Klaviyo, Judge.me, STOQ, Gorgias, Sendcloud, Moneybird-koppeling, GS1, PostNL, luchtvracht, inklaring, fotografie).

### Inferences
Vaste kosten per maand (USD omgerekend circa 0,87; excl. btw):

| Post | Lean start (0-100 orders/mnd) | Groei (300-500 orders/mnd) | Bron/opmerking |
|---|---|---|---|
| Shopify | EUR 28 (Basic) of EUR 21 jaarlijks | EUR 78 (Grow) of EUR 59 jaarlijks | vraag 1 |
| Thema Prestige/Impact (USD 380-400 eenmalig, over 24 mnd) | circa EUR 14 | circa EUR 14 | vraag 1 |
| Reviews Judge.me | EUR 0 | circa EUR 13 (USD 15) | vraag 3 |
| Klaviyo | EUR 0 (tot 250 profielen) | circa EUR 26-130 (1.000-10.000 profielen) | vraag 3 |
| Leverdatum-app STOQ (of eigen n8n-metafield EUR 0) | EUR 0-9 | EUR 9-25 | vraag 3 |
| Helpdesk Gorgias | EUR 0 (Inbox/Gmail) tot EUR 9 | circa EUR 52 (Basic) | vraag 6 |
| Retourportaal Sendcloud (of eFreight) | EUR 0 | EUR 40-87 | vraag 6, prijzen conflicteren |
| Moneybird-koppeling (of n8n EUR 0) | EUR 0-15 | EUR 15-47 | vraag 7 |
| GS1 (EUR 92 + EUR 28 per jaar) | EUR 10 | EUR 10 | vraag 5 |
| n8n | bestaande Shop4You-instance, marginaal | idem | aanname |
| Totaal vast | circa EUR 52-125 | circa EUR 230-450 | |

Variabele kosten per dekbedorder (voorbeeld EUR 249, 3-4 kg belastbaar na vacuumverpakking):

| Stap | 25 orders/week | 100 orders/week | Opmerking |
|---|---|---|---|
| Betaling (iDEAL / kaart / Klarna) | EUR 0,29 / 4,98 / 7,80 | idem | vraag 2 |
| Luchtvracht | circa EUR 15-21 | circa EUR 12-17 | vraag 5, afhankelijk volumegewicht |
| Luchthavenafhandeling + inklaring (EUR 100-250/week) | EUR 4-10 | EUR 1-2,50 | vraag 5 |
| Crossdock/label per pakket | EUR 1-2,50 (schatting) | idem | geen publieke prijs |
| PostNL NL | EUR 7,40 | EUR 7,00 | vraag 5; eFreight-contract mogelijk lager |
| Totaal logistiek per order | circa EUR 28-41 | circa EUR 21-29 | excl. invoerrechten en retouren |

- Invoerrechten (afhankelijk van GN-code) en retourkosten (100-nachten-proef) komen hier nog bovenop; zie product/douane-module.
- Gevoeligheid: zonder vacuumverpakking (circa 9 kg volumetrisch) stijgt luchtvracht per dekbed naar circa EUR 40-55, wat het model onrendabel kan maken bij een verkoopprijs onder EUR 200.

### Gaps
- Alle eFreight-posten zijn schattingen; een offerte op basis van dit scenario (wekelijks 50-200 kg, geconsolideerd, X pakketten, crossdock, NL+BE last mile, retouren) is de belangrijkste openstaande actie.
- Werkelijke afmetingen/gewicht van het Bline-dekbed in vacuumverpakking onbekend; bepaalt de luchtvrachtkosten.
