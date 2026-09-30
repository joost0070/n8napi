# Bol.com listing-SEO and conversion without advertising: rules, practice, checklists (NL/BE, status 30 Sep 2026)

Scope: organic findability and conversion on bol.com NL/BE with no Sponsored Products. The notes build on these two files and do not repeat them: `../Bol leeskussens Q4 strategie/bol_ranking_factoren.md` (ranking = relevance + popularity, the ACM buy-box documents, kwaliteitsscore, Groeibeloning, Select-deals) and `../Bol leeskussens Q4 strategie/conversie_reviews_service.md` (image basics, video basics, the July 2024 review rule, Mijn Leverbelofte, service norms, returns). Where a topic is already covered there, only the new or corrected facts are given here.

Labels used:
- **[bol-doc]** = published by bol on partnerplatform.bol.com, api.bol.com, developers.bol.com or productdatamodel.s-bol.com.
- **[bol-data]** = read directly from a bol machine-readable file (the OpenAPI spec, the data model JSON or a downloadable xlsx).
- **[agency]** = opinion or claim from an agency or tool vendor.
- **[press]** = trade press.
- **[inference]** = my own conclusion.
- **[older]** = source dated before 2025.

All bol pages were fetched on 2026-09-30. The partnerplatform pages show no publication date. The v10 NL data model JSON has metadata `created: 2026-09-30T05:00:00Z`.

---

## 0. The most important new facts (not in the earlier notes)

1. **Bol publishes a per-product-group title template.** The spreadsheet "Gewenste titelopbouw 2025" covers 383 product groups. Every template starts with **[Merk]**. For example, `Kussen`: `[Merk] [Model] [productgroep] - [Afmeting] - [Kleur]`. **[bol-data]** — [Gewenste-titelopbouw-2025.xlsx](https://eu-assets.contentstack.com/v3/assets/blt27f326c486dc0d7d/blt786a75688e01e99a/6914bc2465d9f332a94d0776/Gewenste-titelopbouw-2025.xlsx), linked from [Schrijf een goede titel](https://partnerplatform.bol.com/nl/idp/schrijf-een-goede-titel). Several agencies (Zoloo/Boloo) instead tell sellers to put the keyword first. See §1.
2. **There is no backend keyword or search-term field on bol.** The v10 data model has 7,703 attributes and none of them is a keyword, search-term or tag field. The only text fields that customers see are Name (the title) and Description, plus the specification values. **[bol-data]** — [datamodel_v10_nl.json](https://productdatamodel.s-bol.com/v10/datamodel_v10_nl.json)
3. **Hard limits in the data model:**
   - Name (title): validation `maximumLength: 250`. The filling instruction says "gemiddeld 70 tekens".
   - Description: validation `maximumLength: 10000`. The filling instruction says "maximaal 3000 tekens".
   - Allowed HTML in descriptions: `<b> <br> <h3> <li> <ol> <ul> <p> <strong>`. Everything else is rejected.
   **[bol-data]/[bol-doc]** — [data model](https://productdatamodel.s-bol.com/v10/datamodel_v10_nl.json); [Product Content API docs](https://api.bol.com/retailer/public/Retailer-API/suppliers/product-content.html)
4. **Price stars now have a bol-documented effect table.** 1 star means "Product wordt offline gehaald". The table also gives an average conversion rate per star level: 1★ 0%, 2★ 3.8%, 3★ 4.4%, 4★ and 5★ 4.5–5.6%. 3★ or more qualifies for bol-paid SEA budget, and 4★ or more is needed for "Meedoen aan Promoties". **[bol-data]** — [Prijsster-voordelen-tabel.xlsx](https://eu-assets.contentstack.com/v3/assets/blt27f326c486dc0d7d/blt53b26e59acc21caf/69246292e16a28454ca7690b/Prijsster-voordelen-tabel-10724.xlsx), linked from [Prijssterren](https://partnerplatform.bol.com/nl/idp/prijssterren). This resolves the gap in the earlier notes, where "1 star = offline" came only from agencies.
5. **Bol's review page (2026) is now stricter:** "Het is niet toegestaan om klanten zelf om een review te vragen. Wij sturen namens bol automatisch een uitnodiging na een aankoop." This contradicts the older Sellerly and Bolmate reading that a review request in the invoice e-mail is allowed. **[bol-doc]** — [Productbeoordelingen](https://partnerplatform.bol.com/nl/idp/productbeoordelingen)
6. **Product families pool reviews and views.** Bol says families give "gemiddelde verkoopstijging van wel 10%", that you can "meeliften op de pagina-ranking binnen de productfamilie", and that "Reviews en views worden gebundeld". The API docs add: "Products in the product families also inherit reviews". **[bol-doc]** — [Content: 5 bouwstenen](https://partnerplatform.bol.com/nl/idp/content); [API product families](https://api.bol.com/retailer/public/Retailer-API/v10/functional/retailer-api/product-families.html)
7. **Image labels are a closed list.** The data model has 60 labels in total, covering image, PDF and video. The `Leeskussen` group (chunk 30016181) accepts USP, SIDE, BOTTOM, TOP, BACK, DETAIL, FRONT, IN SITU and OTHER. Unlabelled images are placed "based on their quality scores". Images from a registered brand owner are shown first per label. **[bol-data]/[bol-doc]**
8. **Bol's own content page ("5 bouwstenen") gives numbers:**
   - title 30–150 characters, "alleen Nederlandse woorden";
   - "Met de juiste titel behaal je tot 20% meer conversie";
   - description at least 500 characters; "De eerste 120 tekens worden gebruikt voor Google Shopping";
   - main image preferably 1500×1500.
   The 30–150 range conflicts with the 70-character maximum on the title page. See §1. **[bol-doc]** — [idp/content](https://partnerplatform.bol.com/nl/idp/content)
9. **Content changes are processed within 8 hours.** Search needs at least 1 more day (at least 2 days for new articles). A family change can take up to 24 hours. An objection ("bezwaar") against a rejected change is reviewed by a bol employee within 24 hours. Feedback and upload reports stay available for 28 days. **[bol-doc]** — see §8.

---

## 1. Product titles

### Documented bol rules

- **Page "Schrijf een goede titel"** **[bol-doc]** ([link](https://partnerplatform.bol.com/nl/idp/schrijf-een-goede-titel))
  - Do's: brand (if applicable), model or type number, product group, a hyphen "-" between parts, one or two distinguishing features, and a capital letter at the start.
  - Don'ts: whole words in capitals, English words, "verschillende schrijfwijzen of synoniemen", "veel bijvoeglijke naamwoorden", "meer dan 70 karakters (inclusief spaties)", symbols, and stunt or promotional statements "ook gerelateerd aan feestdagen of jouw offer, zoals 'voordeel', 'vaderdag', 'goedkoop' of 'gratis'".
  - "Door jouw content te verbeteren, kun je een hogere content rating krijgen, wat ervoor zorgt dat jouw aanpassingen sneller door kunnen komen."
  - A short title makes it less likely that "het systeem de melding geeft dat het voor andere content heeft gekozen".
  - "Zorg dat de producttitel binnen 2 weken na het toevoegen van een nieuw artikel goed staat, hier wordt namelijk de pagina URL op gebaseerd."
- **Per-product-group templates** **[bol-data]** (xlsx "Gewenste titelopbouw 2025", 383 rows). Most common patterns:
  - Fashion and sports (104×): `[Merk] - [Lijn/Serie/Model] - Geslacht - [Productgroep] - [Kleur]`
  - Clothing (49×): `[Merk] [Productlijn] - [Geslacht/Doelgroep] [Productgroep]`
  - Home and textile (16×): `[Merk] [Model] [productgroep] - [Afmeting] - [Kleur]`. This covers Kussen, Dekbedovertrek, Bed and Bank.
  - Other examples: Matras `... - [Afmeting] - [Soort vering]`; Opberger `... - [Inhoud/Maat] - [Kleur]`; Hoesje voor mobiele telefoon `[Merk] [Model] - [Geschikt voor telefoonmodel] - [Kleur]`.
  - `Leeskussen` has no row of its own. The closest is `Kussen`.
- **Data model filling instruction for `Name`** **[bol-data]**: "Een goede titel bevat het merk van het artikel, een serienaam, een typenummer en enkele onderscheidende karaktereigenschappen … gemiddeld 70 tekens … niet geheel in hoofdletters … koppeltekens … Vermijd in de titel woorden als 'actie' en 'aanbieding' en verwijzingen naar externe bronnen. Voorbeeld: [Merk] [Productcode of Productnaam] – [Producttype] – [Kenmerk 1] – [Kenmerk 2]."
  - Hard validation: max 250 characters.
  - The `Brand` instruction says: "De titelopbouw begint met het merk."
- **Fashion A/B test** **[bol-doc]**: "Uit een A/B-test blijkt dat de conversie met 10% stijgt als de maat niet in de titel staat." Recommended fashion title: `[Merk] [Serie/Lijn] [Geslacht] [Productgroep] – [Kleur]`. — [Productinformatie toevoegen mode](https://partnerplatform.bol.com/nl/idp/productinformatie-toevoegen-mode)
- **Forbidden in both title and description** **[bol-doc]**: references to prices, websites, promotions, services and sales slogans, for example "Black Friday Deal", "morgen in huis", "op=op", "voordelig", "goedkoop", "gratis". Delivery claims and holiday promotions are also forbidden. Vague sustainability claims are banned: "Milieuvriendelijk, Eco, Duurzaam, Klimaatneutraal, Biologisch afbreekbaar, CO2-neutraal, Bewust, Verantwoord …", following ACM guidance. Violations cost **beleidspunten** (policy points). — [Deze regels gelden voor je productinformatie](https://partnerplatform.bol.com/nl/idp/deze-regels-gelden-voor-je-productinformatie); [Product- en contentmisleiding](https://partnerplatform.bol.com/nl/idp/product-en-contentmisleiding)
- **Search relevance and titles** **[bol-doc]** ([Productinformatie FAQ](https://partnerplatform.bol.com/nl/idp/productinformatie), [Zoekalgoritme](https://partnerplatform.bol.com/nl/idp/zoekalgoritme-van-bol))
  - "Een woord in je titel opnemen betekent niet automatisch dat je artikel zichtbaar is op dat keyword. Per productgroep herkennen we woorden die bij elkaar horen, zoals synoniemen. Daardoor kan je artikel vindbaar zijn op een zoekterm die niet in je titel staat."
  - "Wordt mijn artikel beter vindbaar als ik meer woorden in de titel zet? Ja en nee … relatief meer minder relevante bezoekers … We raden daarom af om veel extra woorden in je titel te zetten."
  - Singular and plural forms, conjugations, diminutives, spelling mistakes and synonyms are handled automatically, "mits ze ook daadwerkelijk worden gezocht door genoeg klanten". Therefore: "Vermijd daarom dubbele spellingsvarianten en synoniemen."
  - A missing synonym can be reported to Partnerservice.
  - "Pas je titel ook niet te vaak aan … Bovendien verslechtert het je zichtbaarheid." — [bol zoektrends](https://partnerplatform.bol.com/nl/idp/bol-zoektrends)
- **Auto-generated titles**:
  - I found **no bol documentation** saying that bol builds Dutch titles from attributes for partner content.
  - Documented automatic behaviour:
    - (a) Dutch titles and descriptions are machine-translated to French **once**; later Dutch edits are not re-translated. **[bol-doc]** — [Franstalige productinformatie](https://partnerplatform.bol.com/nl/idp/franstalige-productinformatie-toevoegen)
    - (b) Since 2024 bol has piloted AI (via Squadra) that fills **attributes** from photos, PDFs and web data. According to Emerce's update, it does not write descriptions. **[press, older 2024-10-07]** — [Emerce](https://www.emerce.nl/nieuws/bol-zet-ai-betere-productomschrijvingen)
    - (c) On shared EANs, bol's content algorithm can pick or combine titles from several suppliers, the brand owner or LvB. See §8.

### Conflicting bol statements (flag to user)

| Source | Title length | Language |
|---|---|---|
| idp/schrijf-een-goede-titel | "meer dan 70 karakters" = don't | no English words |
| idp/content ("5 bouwstenen") | "Tussen 30 en 150 karakters" | "alleen Nederlandse woorden" |
| data model `Name` | "gemiddeld 70"; hard max 250 | – |
| older PDF content guidelines 2020–2022 **[older]** | < 70 | – |

**[inference]** Treat 70 as the target and 150 as a hard ceiling for readability. Anything above 70 is truncated on mobile list pages anyway; agencies report roughly 25–35 visible characters.

### Agency practice (opinion)

- **Zoloo** (Boloo's blog, which now redirects boloo.co to zoloo.co), bol-com-seo, 2026-05-25: `[Hoofdzoekwoord] - [Merk] - [Spec 1] - [Spec 2] - [Voordeel]`; "bol.com weights early-positioned terms higher"; titles over 150 characters are truncated. **[agency]** — [zoloo.co/blog/bol-com-seo](https://zoloo.co/blog/bol-com-seo). This conflicts with bol's brand-first template.
- **Zoloo** listing guide, 2026-07-16: "merk + productsoort + model of toepassing + relevant kenmerk + maat of aantal"; "herhaling maakt de titel moeilijker leesbaar". **[agency]** — [zoloo.co/blog/listing-bol-com](https://zoloo.co/blog/listing-bol-com)
- **Bolmate**, 2025-12-19: `[Merk] [Product] [Belangrijkste kenmerk] [Kleur/Maat]`; keyword stuffing "kan door het algoritme zelfs bestraft worden". This claim is not bol-documented. **[agency]** — [bolmate.nl/bol-com-seo](https://bolmate.nl/bol-com-seo/)
- **MarktMentor** (undated, part of a 2023 series, **[older]**):
  - Search relevance compares the query with "productspecificaties en de titel".
  - Use "-" and not "|", because a pipe "wordt gezien als een echt scheidingsteken" that stops combined terms from matching.
  - Build titles from "basiswoorden" plus "specificatiewoorden".
  **[agency]** — [MarktMentor zoekwoordstrategie](https://www.marktmentor.nl/blog/verbeteren-vindbaarheid-bol-zoekwoordstrategie)
- **Rylee**, 2026-01-04: titles "rijk aan ideale keywords" and optimised for Google featured snippets. No numbers given. **[agency]** — [Rylee](https://rylee.nl/nl/blog/Bol-ranking-optimaliseren)

### Checklist: titles

- [ ] Look up the bol template for your product group in "Gewenste titelopbouw 2025". Home textiles and pillows: `[Merk] [Model] [productgroep] - [Afmeting] - [Kleur]`.
- [ ] Brand first when the brand is registered. The product-group noun must appear in the first ~35 characters. If you test keyword-first, run it on one EAN and measure it (§9, product-ranks).
- [ ] Keep it to 70 characters or less. Separate with " - ". Use one or two distinguishing features. Colour belongs in the title only if it is also the family's distinctive feature.
- [ ] Remove: synonym stacks (for example "Leeskussen - Boekkussen - Rugkussen - Lendekussen"), English words, all-caps words, symbols (| ★ ✓ ®), and promotional, delivery, price, holiday or vague eco words.
- [ ] Get the title right within 14 days of creating the article, because the page URL is derived from it. After that, change it rarely.
- [ ] Put the same main term in the first sentence of the description (§2).
- [ ] BE-FR: write your own French title. Later Dutch edits are **not** re-translated (§3).

---

## 2. Descriptions, specifications (kenmerken/attributen), content score, product group

### Documented bol rules

- **Length and format** **[bol-doc]/[bol-data]**
  - Data model `Description`: "maximaal 3000 tekens"; hard validation 10,000; "Nederlandstalig … bij voorkeur in de 'jij-vorm'"; "Vermijd … 'actie' en 'aanbieding' en verwijzingen naar externe bronnen".
  - idp/content: "Minimaal 500 karakters. De eerste 120 tekens worden gebruikt voor Google Shopping … Woorden uit je titel komen terug in de tekst … kopjes, bullets en dikgedrukte woorden".
  - Older PDF guidelines **[older 2020–2022]**: ideal 300–600 characters, first ~120 characters shown in Google, at most 200 characters for mobile. — [contentrichtlijnen daily care PDF](https://leveranciers.bol.com/content/uploads/2023/11/contentrichtlijnen-daily-care.pdf)
- **HTML** **[bol-doc]**: only `<b>`, `<br>`, `<h3>`, `<li>`, `<ol>`, `<ul>`, `<p>`, `<strong>`. "All other HTML tags … will be rejected by the system." In the seller-account editor this appears as "Kopjes ('Header 3'), dikgedrukt, normale tekst, opsomming". Headings, bold and lists "hebben een bewezen positief effect op de conversie". — [API product content](https://api.bol.com/retailer/public/Retailer-API/suppliers/product-content.html); [Schrijf een duidelijke productbeschrijving](https://partnerplatform.bol.com/nl/idp/schrijf-een-duidelijke-productbeschrijving)
- **Is the description indexed for search?**
  - Bol **does not state it explicitly**. Its search page says only that the algorithm "controleert … de productinformatie van artikelen" and that it also looks at other relevance signals, including category matching and anonymous interaction data. **[bol-doc]**
  - Indirect evidence **[bol-doc]**:
    - (a) "Laat woorden uit je titel ook terugkomen in je beschrijving".
    - (b) The chunk-recommendations model classifies products from Name + Description. Category drives keyword mapping: "Op basis van de productgroep krijgen artikelen namelijk een plek in de winkel en worden de juiste zoekwoorden gekoppeld." — [Productcategorie kiezen](https://partnerplatform.bol.com/nl/idp/productcategorie-kiezen)
  - Agencies disagree:
    - MarktMentor **[older]**: title plus specifications are what rank; the description is not a direct factor.
    - Zoloo 2026: descriptions "are indexed", so work keywords in naturally.
    - Bolmate 2025: title and attributes weigh most "in the initial search phase".
    **[agency]**
- **Specifications drive filters and relevance** **[bol-doc]**
  - "Productspecificaties vormen daarbij de basis voor filters op de website … Hoe meer productspecificaties bekend zijn … hoe gerichter klanten hier dus op kunnen zoeken."
  - A wrong product group means the relevant attributes are never requested, which "maakt het artikel minder goed vindbaar". — [Productcategorie kiezen](https://partnerplatform.bol.com/nl/idp/productcategorie-kiezen)
  - idp/content: specifications "Wordt gevonden in de filters op de lijstpagina" and "Voorkom klantvragen achteraf".
- **Three content levels** **[bol-doc]**
  - Basisinformatie: EAN, title, at least 1 image.
  - Verplicht: needed to reach "productinformatie online".
  - Optioneel: needed to reach "productinformatie compleet".
  - The seller account shows filled/total fields per level and the "kwaliteit van je productinformatie".
  - In the API the matching values are `enrichment.status` 0, 1 or 2 and data-model `enrichmentLevel` 0, 1 or 2. — [Productinformatie toevoegen per artikel](https://partnerplatform.bol.com/nl/idp/productinformatie-toevoegen-per-artikel); [API catalog product content](https://api.bol.com/retailer/public/Retailer-API/v10/functional/retailer-api/catalog-product-content-api.html)
- **Content score ("contentscore", "content rating", "productinformatie score")** **[bol-doc]**
  - An algorithm scores each partner **per product group**, not per article. On shared EANs the partner with the highest score has its content shown. — [Productinformatie schrijven](https://partnerplatform.bol.com/nl/idp/productinformatie-schrijven)
  - A rejected change is "Vaak … [omdat] een andere partij een hogere contentscore heeft". A higher content rating means your changes are accepted faster. — [Oneens met afwijzing](https://partnerplatform.bol.com/nl/idp/oneens-met-afwijzing-gewijzigde-productinformatie)
  - The formula and weights are **not published**.
  - For a single-seller private-label EAN, the score mainly affects how fast your changes are accepted **[inference]**.
- **Product group choice** **[bol-doc]**
  - An article can be in only one product group. You can change it yourself via "Bewerk productinformatie", but the mandatory specifications can change with it.
  - Unique articles with no product group after 10 days are **deleted automatically**.
  - Tip from bol: look at which group comparable products are in.
  - The data model has 5,089 chunks in total. The overview xlsx lists 5,282 classifications across 66 "Product Groups" (as of 25 Aug 2026) and is updated each quarter. — [Het datamodel](https://partnerplatform.bol.com/nl/idp/datamodel)
  - Example: `Leeskussen` = chunk **30016181** (group Textiles). Its mandatory level-1 attributes are Anti-allergie, Biologisch, Kleur, Beschrijving, Materiaal vulling, Aantal stuks in verpakking, Product lengte, Product breedte and Wasbaar. Optional level 2 includes Merk, Productvariant ID (Family Key), Vulgewicht, Stevigheid kussen, Materiaal tijk, Product gewicht, Wasvoorschrift and Verpakkingsinhoud. **[bol-data]**
  - Surprise: `Brand` is enrichment level 2 (optional) in this chunk.
- **Allowed and forbidden in specifications** **[bol-doc]**: deliberately wrong specifications, or changing "aantal stuks in verpakking" or "kleur" to disadvantage others, count as "product- en contentmisleiding" and cost policy points. Adding **correct** extra information is allowed "ook als je het koopblok niet hebt". — [Product- en contentmisleiding](https://partnerplatform.bol.com/nl/idp/product-en-contentmisleiding)
- **Registered brand name rules** **[bol-doc]**
  - A branded product is allowed only if the brand is registered at BOIP for that type of article.
  - For direct-distribution brands (private label), the brand or logo must be printed on the product or original packaging **and** visible on an image uploaded when the article is created. Stickers, watermarks and photoshopped logos are not allowed, and neither is adding the branded image later.
  - Otherwise use "merkloos". — [Merknaam of logo tonen](https://partnerplatform.bol.com/nl/idp/merknaam-of-logo-tonen); data model `Brand` definition

### Agency practice

- Zoloo 2026: description should open with a short product summary, the application and the key limitation; make it scannable. **[agency]**
- Bolmate 2025: missing or incorrect attributes make the product "onzichtbaar" as soon as a customer applies a filter. **[agency]**
- Channable (feed tool): an empty 'colour' means you are not found via the colour filter. **[agency]** — [Channable/feed articles via search](https://helpcenter.channable.com/css/css-nl/titeloptimalisatie/hoe-naar-de-titeloptimalisatie-instellen)
- MarktMentor **[older]**: in the bol app the description is "bijna verborgen", so images carry conversion. **[agency]** — [MarktMentor listing](https://www.marktmentor.nl/blog/optimaliseren-listing-bol)

### Checklist: descriptions and specifications

- [ ] Run `POST /retailer/content/chunk-recommendations` with your title and description. If the top prediction is not your current `gpc.chunkId`, review the product group (§9).
- [ ] Fill **every** level-1 and level-2 attribute of the chunk. Target `enrichment.status = 2` ("productinformatie compleet"). Use values from the fixed lists (LOVs) exactly, with exact capitalisation.
- [ ] Filter-critical attributes for pillows: Kleur, Materiaal vulling, Anti-allergie, Wasbaar, Stevigheid, Product lengte/breedte in cm.
- [ ] Description of 500–3000 characters. The first 120 characters restate the title terms and core benefit, because they are used in Google Shopping. Use `<h3>` sections, a `<ul>` with specifications and USPs, a "Wat zit er in de doos" section, and wash/care instructions. Only the allowed tags.
- [ ] Answer the top customer-question themes in the description. The customer-question insights in the seller account show the topics and the articles with relatively many questions (§8).
- [ ] No prices, delivery claims, URLs, e-mail addresses, "gratis/voordelig", holiday hooks or vague eco claims.
- [ ] Brand visible on the product or packaging in an image from day 1, or use "merkloos".

---

## 3. Keywords

### Documented bol rules and data sources

- **No backend search-terms field.** Confirmed by the absence of any keyword or tag attribute among the 7,703 attributes in the v10 data model. **[bol-data]** Keywords can only live in the title, the description and the specification values. Bol also maps keywords to articles through the product group.
- **bol zoektrends (seller account → Analyse → bol zoektrends)** **[bol-doc]** ([bol zoektrends](https://partnerplatform.bol.com/nl/idp/bol-zoektrends))
  - Shows search-bar volume on web and app, up to 4 years back, and several terms can be compared.
  - "Gerelateerde zoekwoorden" are the most-used queries that literally contain your term.
  - Not case-sensitive and ignores accents.
  - Bol's example: choose "vaatwasser" over "vaatwasautomaat" or "afwasmachine" because customers use it most.
  - "Uit testen blijkt dat partners harder groeien door actief met deze data aan de slag te gaan."
  - Bol also recommends Google Trends, because part of the traffic comes via Google.
- **Retailer API** `GET /retailer/insights/search-terms?search-term=&period=DAY|WEEK|MONTH&number-of-periods=&related-search-terms=true` **[bol-data]**
  - Returns `total`, a per-country split (`countries[].countryCode/value` for NL and BE), `periods[]` and `relatedSearchTerms[{searchTerm,total}]`.
  - History: 365 days, 104 weeks or 48 months. Updated daily at 05:00 with data up to 12:00 the previous day.
  - **No language parameter**, so it is unknown whether French queries from Wallonia are included. See Gaps.
  - Docs: [search-terms](https://api.bol.com/retailer/public/Retailer-API/v10/functional/retailer-api/search-terms.html)
- **Product ranks per search term** `GET /retailer/insights/product-ranks?ean=&date=&type=SEARCH|BROWSE&page=` with `Accept-Language: nl-NL|nl|nl-BE|fr|fr-BE`
  - Returns every `searchTerm` your EAN ranked on, with `rank`, `impressions` (seen for at least 1 second and at least 50% in view) and `wasSponsored`.
  - Up to 3 months back, until yesterday.
  - **[inference]** This is the best bol-native "reverse keyword" source. It shows which queries bol already associates with your EAN, including French queries when fr-BE is used. **[bol-data]**
- **Seller account "Verkoopinzicht"**: position in relevant categories and for relevant search terms over the last 14 days. **[bol-doc]** — [Verkoopinzicht](https://partnerplatform.bol.com/nl/idp/verkoopinzicht)
- **Sponsored Products search-term reports** (only if the advertiser account exists; listed for completeness):
  - Advertising API v11 has a "Search terms performance" report per ad group, plus Share-of-Voice click and impression share at search-term level.
  - Advertising Insights gives the average winning bid per **exact** search term over 14 days.
  **[bol-doc]** — [performance reports](https://api.bol.com/retailer/public/Retailer-API/v11/functional/advertising-api/reporting/performance-reports.html); [insights](https://api.bol.com/retailer/public/Retailer-API/v11/functional/advertising-api/insights/insights.html)
  - Not needed for a no-ads strategy, but any past campaign data is a free keyword source.
- **Coming (ACM commitments, due by 31-12-2026)**: search-term analysis with searches, clicks, CTR, product views, ad views, average scroll depth and average click position. This is already covered in the ranking notes. **[ACM]**
- **Bol autocomplete**: used by agencies (Zoloo 2026: "autocomplete suggestions … based on actual customer searches"). No bol documentation. bol.com blocks scraping (403 in this session). **[agency]**

### Keyword placement

- **Bol's guidance** **[bol-doc]**: use relevant keywords "maar overdrijf niet"; a title is "meer dan een reeks keywords"; no double spellings or synonyms, because bol handles them; words from the title should come back in the description.
- **Agency practice** **[agency]**:
  - Zoloo: 2–4 keywords in the title, main one first.
  - MarktMentor: base word plus specification words, joined with "-" and never "|".
  - Rylee: use the rank tracker to find "ontbrekende zoekwoorden".

### French and Belgian keywords

- **Mechanics** **[bol-doc]**
  - Nearly all partner assortment sold in Dutch-speaking Belgium is published automatically in the French app and website, machine-translated.
  - Free-text fields (title, description) are translated **once**. LOV attributes (dropdowns) are translated automatically every time.
  - French content can be edited only via the **BE** seller account, through "Bewerk productinformatie" and the French flag or the bulk editor. Via the API use `language: fr` (France and Wallonia) or `fr-BE` (Wallonia only).
  - "Originele (Franstalige) producttitels en beschrijvingen zijn vaak echter van betere kwaliteit."
  - Language attributes (product, manual, packaging language) decide whether an item is shown to French-speaking customers.
  - Belgian law requires a manual in both Dutch and French with the shipment.
  — [Franstalige productinformatie](https://partnerplatform.bol.com/nl/idp/franstalige-productinformatie-toevoegen); [Verkopen in België](https://partnerplatform.bol.com/nl/idp/verkopen-in-belgie); [API languages](https://api.bol.com/retailer/public/Retailer-API/suppliers/product-content.html)
- **Reviews**: bol rejects reviews "niet in het Nederlands geschreven". **[bol-doc]** How French-language reviews from Wallonia are handled is not documented. See Gaps.
- **Agency practice** **[agency]**: Flemish vocabulary differs, for example "gsm" instead of "smartphone". — [BolKit BE guide](https://bolkit.nl/blog/internationaal-verkopen-bol-com-belgie). The claim that city names help in Wallonia comes from a non-bol SEO source and is not relevant to bol search.
- **[inference] French keyword candidates for a reading pillow**, to validate with product-ranks (fr-BE) and your own search tests. They are **unverified**:
  - « coussin de lecture »
  - « coussin de lecture pour lit »
  - « coussin dossier lit »
  - « coussin avec accoudoirs »
  - « oreiller de lecture »
  - The machine translation of "leeskussen" is unknown. Check the fr-BE title via `GET /retailer/content/catalog-products/{ean}` with `Accept-Language: fr-BE`.

### Checklist: keywords

- [ ] Build a keyword list from bol zoektrends (seller account) or `insights/search-terms` with `related-search-terms=true`, looking at 104 weeks for seasonality.
- [ ] Pull `insights/product-ranks` for your EANs, 90 days back with `type=SEARCH`, for both `nl` and `fr-BE`. List the terms where you have impressions but rank beyond 20. Those are the content gaps.
- [ ] Title: one main term, the one with the highest bol volume, instead of synonyms. Description: the secondary terms once each, in natural sentences. Specifications: every filterable property.
- [ ] Separately check the fr-BE title and description and rewrite them by hand. Re-check after every Dutch edit, because free text is not re-translated.
- [ ] Put Google Trends (NL/BE) next to the bol volumes for seasonality.

---

## 4. Images and video

### Documented bol rules (new detail beyond the earlier notes)

- **Image specifications** are already in `conversie_reviews_service.md`: 30 KB–10 MB, 500–6000 px, zoom from 1200×1200, white first image, and so on. New points **[bol-doc]** ([Deze regels gelden voor je afbeeldingen](https://partnerplatform.bol.com/nl/idp/regels-voor-afbeeldingen)):
  - Whitespace is cropped automatically and does not count toward the pixel limits.
  - Images are recompressed, which can affect colour accuracy and sharpness.
  - Exact duplicates are not loaded.
  - No spaces in file names or URLs.
  - No Kieskeurig or Consumentenbond stickers, no "uitgebreide garantie" or "gratis verzending", no generic illustrations (except in Hardware and Vehicles), no reviews, no comparisons.
  - Only what the customer receives.
  - An in-package shot is allowed only if an out-of-package shot is also present.
  - The main image must be the **front**: no combined front/side/back views, not a lifestyle image, and no models, text, logos or icons.
  - "Vanaf 1 juli 2025 handhaven wij niet meer op de richtlijnen van afbeeldingen … Wel handhaven we nog steeds op zelfpromotie in afbeeldingen."
  - idp/content recommends **1500×1500** for the main image; "Extra ondersteunende beelden: andere hoeken en standen, details en maten op een schets. Sfeerbeelden en video's voeg je toe waar ze iets toevoegen." — [idp/content](https://partnerplatform.bol.com/nl/idp/content)
- **Order and labels** **[bol-doc]/[bol-data]**
  - In the seller account you pick an "aanzicht" (view) per image. "Zodoende zet het systeem de afbeeldingen automatisch in de juiste volgorde. Deze volgorde wordt op basis van kwaliteit en klantdata bepaald."
  - The same view can be used several times, and all unique images go online.
  - Other partners can take your images offline; they then appear under "Jouw offline afbeeldingen", where you can put them back. — [Afbeelding per stuk](https://partnerplatform.bol.com/nl/idp/afbeelding-per-stuk-toevoegen)
  - API (Product Content v10):
    - `assets[]` holds at most 30 per request, each with a `url` and 1–2 `labels`. "Assets with only valid labels are processed."
    - Labelled images are ordered by the category configuration. Unlabelled images go "in free positions … based on their quality scores". With only PRIMARY/ADDITIONAL metadata, the primary image goes in position 1.
    - Image URLs must be on real hosting: "Een gratis hosting locatie wordt niet geaccepteerd".
    — [API product content](https://api.bol.com/retailer/public/Retailer-API/suppliers/product-content.html); [Bulk afbeeldingen](https://partnerplatform.bol.com/nl/idp/meerdere-afbeeldingen-tegelijk-toevoegen)
  - **Full label list** (data model v10) **[bol-data]**:
    - Image views: FRONT, BACK, SIDE, SIDE LEFT, SIDE RIGHT, SIDE BACK, FRONT SIDE, FRONT SIDE LEFT, FRONT SIDE RIGHT, FRONT BACK, TOP, BOTTOM, DETAIL, INSIDE, PART.
    - Context and usage: IN SITU (sfeerbeeld), INSPIRATION, USER PHOTO, ON MODEL, ON MODEL FRONT, ON MODEL BACK, ON MODEL SIDE.
    - Packaging and contents: PACKSHOT, IN PACKAGE, IN THE BOX, WITH PACKAGE, MULTIPACK, ACCESSORIES.
    - Information graphics: SIZE, SIZE GUIDE, SWATCH, PATTERN / DETAIL FABRIC, TECHDRAWING, USP.
    - Brand and marks: LOGO, ICON, CERTIFICATION, EU IMPORTER MANUFACTURER.
    - Other image labels: AVATAR, BOOKCOVER, BACK COVER, NAVIGATION, OTHER.
    - Video: VIDEO (a direct file URL; YouTube URLs are not valid).
    - PDF documents: MANUAL, ASSEMBLY MANUAL, TECHNICAL MANUAL, GAME RULES, BROCHURE, PREVIEW, PACKAGE INSERT, SAFETY SHEET, PRODUCT INFORMATION SHEET, DATA USAGE INFORMATION, ENERGY LABEL, ENERGY LABEL 2021, CE MARKING, ECE MARKING, DECLARATION OF CONFORMITY, COMMERCIAL DURABILITY GUARANTEE.
    - Allowed per chunk: `Leeskussen` = USP, SIDE, BOTTOM, TOP, BACK, DETAIL, FRONT, IN SITU, OTHER (+ COMMERCIAL DURABILITY GUARANTEE PDF). `Kussen` and `Sierkussen` also allow SIZE, SWATCH and IN PACKAGE.
    - **[inference]** A labelled **USP** slot exists for pillows. That is the sanctioned place for an infographic, still without prices, promotional or delivery claims.
  - **Read-back** `GET /retailer/products/{ean}/assets?usage=PRIMARY|ADDITIONAL|IMAGE` returns `usage`, `order` (the carousel position) and `variants` (small 250×200 and medium up to 550×840, mime type, url). It returns images only, not labels. **[bol-data]**
  - Upload-report sub-statuses show why an image lost **[bol-data]**:
    - `SCORED_OTHER_IMAGE_WON`: "Other image for this slot has a higher quality".
    - `IMAGE_FLAGGED_AS_DUPLICATE`
    - `IMAGE_RATE_LIMITED`: "recently already provided … provide a new URL".
    - `REJECTED_BY_BRAND_AUTHORITY`
    - `REJECTED_BY_LOGISTIC`
    - `UNSUPPORTED_MIMETYPE`
    - `DOWNLOAD_FAILED_404`
  - **Brand-owner priority**: "Afbeeldingen toegevoegd door merkeigenaren worden als eerste getoond, mits deze afbeeldingen de juiste labels … hebben. Per label komen afbeeldingen van niet-merkeigenaren na de afbeeldingen van de merkeigenaar." — [Merkregistratie](https://partnerplatform.bol.com/nl/idp/merkregistratie)
  - Pilot **[bol-doc]**: Offer API v11 bulk image import, `POST /retailer/offers/{offerId}/image-imports`, 1–30 URLs, label `PRIMARY` only. Allow-list only. — [bulk image import](https://api.bol.com/retailer/public/Retailer-API/v11/functional/offer-api/pilots/bulk-image-import.html)
- **Video** (specifications already in the earlier notes) **[bol-doc]**:
  - Upload under "Optioneel".
  - Converted to 16:9, with renditions from 240p up to the source resolution.
  - "We kunnen 1 video per artikel (online) vertonen. De laatst geüploade video wordt getoond". Another seller's later upload overwrites yours.
  - No spaces or special characters in file names.
  - API: label `VIDEO` with a direct file URL. YouTube is not valid.
  - No maximum duration is published. — [Video's toevoegen](https://partnerplatform.bol.com/nl/idp/videos-toevoegen)
- **Visual search**: "Spot & Shop" (bol app, launched January 2026) matches uploaded photos to the assortment. Bol is also integrated with Apple Visual Intelligence. **[press]** — [Emerce 2026-01-27](https://www.emerce.nl/nieuws/bol-maakt-visueel-zoeken-makkelijker-laifunctie-spot-shop). **[inference]** A clean, front-facing, product-only main image probably also helps visual matching. This is unverified.

### Agency practice and reported conversion effect

- Bol's own number: none for images. For video bol says only that the upload sits in a block called "Increase conversion" (see the earlier notes).
- Agencies: see the earlier notes. Boloo's "94% / 250%" and Sellerly's "35% / 7×" are **generic, not bol-specific**.
- Zoloo 2026 recommended order **[agency]**: (1) clear main image, (2) important sides and parts, (3) dimensions with units, (4) realistic use, (5) package contents, (6) compatibility. — [zoloo listing](https://zoloo.co/blog/listing-bol-com)
- Sellerly: use infographics and instruction diagrams to answer doubts. **[agency]** — [Sellerly](https://sellerly.nl/blog/hoe-verhoog-je-je-conversie-op-bol-com)
- **Emerce, Twinkle, e-tailize**: no bol-specific image or video uplift data found.

### Checklist: images and video

- [ ] FRONT: white, 1500×1500 or more, product only, out of the packaging, front view, and the brand visible if you use a brand name.
- [ ] Add at least one each of SIDE, BACK, DETAIL (fabric, zip, pocket), IN SITU (in bed or on the sofa), a dimensions image (on pillows use USP or OTHER, because SIZE is not allowed for Leeskussen), and USP (an infographic with no price or promotional text). Use 6–9 images in total.
- [ ] Label every image. Unlabelled images are ordered by bol's quality score.
- [ ] Check the order via `GET /products/{ean}/assets`, and check the upload report (`SCORED_OTHER_IMAGE_WON`, duplicates).
- [ ] Upload one 16:9 video (direct file, no spaces in the file name). Re-check monthly that it has not been overwritten.
- [ ] No text overlays with "gratis verzending", "garantie", review stars, comparisons or eco claims.

---

## 5. Product families (variants) and bundles

### Documented bol rules

- **Definition** **[bol-doc]**
  - Variants "die slechts op 1 of 2 kenmerken verschillen en verder identiek zijn". Each variant has its own EAN, and several variants on one EAN are impossible.
  - Families are shown on the product page. **Roll-ups** can be set only by bol and show on the search page.
  - Families can be set up by the seller.
  - Families have "geen impact op de prijzen".
  - Examples of what is **not** allowed in one family: a shirt and trousers from the same line, a book series, laptop serial numbers. — [Productfamilies](https://partnerplatform.bol.com/nl/idp/productfamilies)
- **Requirements** **[bol-doc]**:
  - (1) same product group (chunk);
  - (2) same brand, author or artist;
  - (3) each item has a value for the chunk's distinctive feature(s).
  - Distinctive features are fixed per chunk, **at most 2 per category** (`distinctiveFeatureIds`). `Leeskussen` = **Colour only**; `Kussen` = Dropdown Size LxWxH + Firmness Pillow; `Sierkussen` = Colour + Dropdown Size. **[bol-data]**
  - If a chunk has no distinctive feature, the family cannot be created ("Helaas. De artikelen in deze productgroep kunnen we nog niet koppelen"). Ask Partnerservice.
  - 720 of 5,089 chunks have none. **[bol-data]**
- **Family size**:
  - Partnerplatform: "maximaal 250 artikelen".
  - API docs: "maximum of seventy products".
  - **Conflicting bol statements.** **[bol-doc]**
- **Pitfalls** **[bol-doc]** ([Productfamilie aanmaken per stuk](https://partnerplatform.bol.com/nl/idp/productfamilie-aanmaken-per-stuk); [API families](https://api.bol.com/retailer/public/Retailer-API/v10/functional/retailer-api/product-families.html))
  - Values are case- and space-sensitive: "Groen en groen worden als aparte kleuren beschouwd … Lichtgroen is niet hetzelfde als Groen".
  - Two items with the **same** colour and size means only one is shown.
  - An item with an empty distinctive feature is not shown.
  - With 2 features, only items that overlap on one feature are shown as options.
  - Deliberately changing colour or pack size to game families costs policy points.
- **How to create** **[bol-doc]**:
  - One at a time: select the EANs, then "Bewerk productinformatie", then "Koppel varianten".
  - In bulk: an Excel column "Productvariant ID" with the same value per family. No success feedback is given in the bulk flow.
  - API: attribute `Family Key`, max 250 characters, no whitespace. It is **not stored**, so no feedback is returned. For additions after 28 days, send all members again.
  - Unlink: "Bewerk varianten", then "Uit familie halen".
  - Visibility: up to 24 hours (partnerplatform) or 8 hours (API docs). List and search pages update later than the product page.
- **Benefits claimed by bol** **[bol-doc]**: "gemiddelde verkoopstijging van wel 10%", "meeliften op de pagina-ranking", "Reviews en views worden gebundeld". — [idp/content](https://partnerplatform.bol.com/nl/idp/content). The API docs add: "Products in the product families also inherit reviews, which thereby increases the conversion rate."
  - Not documented: whether pooled reviews or views also feed the **search ranking** of each member EAN. The ranking notes found no bol source on how families are de-duplicated in search.
- **Bundles** (a combination of different items under one EAN) **[bol-doc]** — [Bundels](https://partnerplatform.bol.com/nl/idp/bundels)
  - Every EAN must be GS1-registered, including the bundle EAN, which is registered to the partner.
  - At most 4 different EANs.
  - Each item **must also be offered individually**.
  - Bundle price ≤ the sum of the item prices.
  - Content attributes are filled "op basis van het primaire artikel".
  - "In de productomschrijving moeten de EANs én productbeschrijving van alle artikelen in de bundel zichtbaar zijn".
  - Brand-owner permission is needed, and for own-brand combinations the item EANs must be registered to the brand owner.
  - Unbranded combinations are offered as "merkloos".
  - Breaking these rules means the item can be taken offline and/or policy points deducted.
  - Price stars: a bundle on the same EAN as the standard item is priced as the standard item. — [Prijssterren](https://partnerplatform.bol.com/nl/idp/prijssterren)
- **[inference]** For a leeskussen range:
  - The 5 colours of the **same** item (same contents) form one family on Colour.
  - A "kussen + hoes" bundle is a different item. Putting it in the base-pillow family breaks "verder identiek" and creates colour duplicates.
  - Build a separate family of colour bundles, and list both EANs (pillow and cover) in each bundle description.

### Agency practice

- Illustrify and Bolmate (in the ranking notes): separate EANs compete separately and can cannibalise each other. **[agency]**
- No 2025–2026 agency source was found with measured family effects on bol beyond bol's own +10%.

### Checklist: families and bundles

- [ ] Check `distinctiveFeatureIds` for your chunk in the data model before you design variants.
- [ ] Use the same brand string and chunk for all members. Use identical colour spelling (a capital first letter, per the data-model instruction) and unique values per member.
- [ ] Put only identical-except-colour items in a family. Keep bundles and the cover-only item out, or in their own families.
- [ ] After linking, check the product page within 24 hours, then check list and search.
- [ ] Bundles: own GS1 EAN, component EANs and descriptions in the text, components also sold separately, price ≤ the sum.

---

## 6. Reviews and ratings

(Background, including the DSA ban since 1 July 2024 and moderation timings, is in `conversie_reviews_service.md`. These are the 2026 corrections.)

### Documented bol rules **[bol-doc]** — [Productbeoordelingen](https://partnerplatform.bol.com/nl/idp/productbeoordelingen)

- "**Mag ik klanten zelf benaderen voor een review? Het is niet toegestaan om klanten zelf om een review te vragen.** Wij sturen namens bol automatisch een uitnodiging na een aankoop."
- "Sinds 1 juli 2024 zijn gesponsorde reviews verboden via bol. Dit volgt uit de Europese Digital Services Act (DSA)." This covers free products, discounts and gift cards.
- Only buyers can review: "bol accepteert alleen beoordelingen van klanten die het artikel echt kochten". A review cannot be written if the product was not bought via bol, or if the customer has already reviewed it.
- The label "heeft dit artikel gekocht" is added after an order-history check. Checks are done in-house or with **Bazaarvoice**. Reviews usually go live within 24 hours, at most 3 days.
- Bol's system picks which products get invitations. It "kijkt nooit naar eerdere scores" and targets "vooral klanten die vaker reviews schrijven". Invitations go only to customers who opted in to mailings.
- Rejected if the review:
  - is off-product;
  - contains profanity;
  - mentions prices or discounts;
  - contains links, photos, personal data or advertising;
  - is "niet in het Nederlands geschreven";
  - looks dishonest or fraudulent.
  Automated pattern detection can reject or remove reviews afterwards. Random post-checks are also done.
- A negative review is not removed unless it breaks the guidelines. Customers cannot edit a review, only delete it and repost. Bol reviews may **not** be used on your own website.
- Sellers and bol employees may not review items they sell.
- Reviews are switched off for some regulated product groups (a supplements list in xlsx).

### Consequences and agency conflicts

- **Zoloo 2026-05-22** acknowledges that e-mailing customers for reviews "tot sancties kan leiden". It recommends:
  - a **package insert with a QR code** to the product page;
  - relying on bol's invitation, which it says is sent 7–14 days after delivery;
  - a "digitale bonus" (a guide or e-book) included for everyone. **[agency]** — [zoloo.co/blog/bol-review](https://zoloo.co/blog/bol-review)
- **Rylee** (2026) still suggests "e-mailcampagnes om automatisch reviews te vragen". This **conflicts** with the bol rule. **[agency]**
- Sellerly and Bolmate (2024–2025) allow a review line in the invoice e-mail. This is now contradicted by bol's page text. **[agency, older reading]**
- **[inference]** An insert that asks for a review is still "zelf om een review vragen". Bol's text does not carve out inserts. The low-risk options are:
  - (a) excellent product and packaging;
  - (b) an insert with care or usage instructions and a support contact, with **no** review request, or at most a neutral general mention;
  - (c) families to pool existing reviews;
  - (d) conversion levers that raise volume, since bol invites buyers automatically.
  Any "bonus" must be given to all buyers and never be conditional on a review, otherwise it counts as a sponsored review.
- **Seller rating ≠ product review.** The Retailer ratings API (v11 beta) returns `retailerRating`, `productInformationRating`, `deliveryTimeRating`, `shippingRating`, `serviceRating` and `isTopRetailer`. Top Retailer needs an average of 9.0 or more, at least 8.5 on every sub-rating, and at least 20 reviews in the last month. The rating uses the last 3 months if there are at least 5 reviews in that period, otherwise all reviews. **[bol-doc]** — [retailer ratings](https://api.bol.com/retailer/public/Retailer-API/v11/functional/retailer-api/retailer-ratings.html). "Productinformatie" is a sub-rating, so inaccurate content hurts the seller rating directly.
- **AI assistant "Shophulp"** (beta, press of 2026-09-15): ranks items on "customer reviews, relevance and popularity and availability" and deliberately ignores a customer wish to see only the best-rated items. **[press]** — [Emerce](https://www.emerce.nl/nieuws/bol-brengt-echt-slimme-aishoppingassistent-uit)

### Checklist: reviews

- [ ] Remove any review request from e-mails (invoice e-mails included) and from inserts. Keep inserts to care, usage and support information.
- [ ] Never offer discounts, gifts, free products or "bonuses" conditional on a review. Never gate reviews ("only if happy").
- [ ] Put all colour variants in a family so reviews pool.
- [ ] Monitor `GET /retailer/products/{ean}/ratings` (star distribution) weekly. Use the content of 1–3★ reviews to fix the description, images or manual.
- [ ] Monitor the seller rating via `GET /retailer/retailers/current/ratings`, especially `productInformationRating`.

---

## 7. Offer-level factors: what affects product ranking and what affects only the koopblok (buy box)

(Details are in the ranking notes and in `conversie_reviews_service.md`. Only new bol-documented facts are listed here.)

| Factor | Bol-documented effect on the **koopblok** | Bol-documented effect on **search/list ranking** | Notes |
|---|---|---|---|
| **Prijssterren** | Price is a buy-box factor | Bol: better price → "meer bezoek … hoger in de zoekresultaten … meer geklikt" (indirect, via popularity). **1★ = product offline**. Conversion by level: 0% / 3.8% / 4.4% / 4.5–5.6% | Boundaries are recalculated ~4×/day from a Relevant Market Price (outside competitor price, RRP, historical buy-box price over 90 days). API: `GET /products/{ean}/price-star-boundaries`. — [price star docs](https://api.bol.com/retailer/public/Retailer-API/v10/functional/retailer-api/price-star-boundaries.html), [xlsx](https://eu-assets.contentstack.com/v3/assets/blt27f326c486dc0d7d/blt53b26e59acc21caf/69246292e16a28454ca7690b/Prijsster-voordelen-tabel-10724.xlsx) |
| **Maximum price** | A buy-box minimum condition: "Je verkoopprijs ligt onder de maximale verkoopprijs die is gebaseerd op marktinformatie" | Above it the offer is not shown | [Verkoopinzicht](https://partnerplatform.bol.com/nl/idp/verkoopinzicht) |
| **Bestelbaarheid / stock** | Buy-box factor 1 of 5; the minimum condition is "Je hebt voorraad" | Without stock there is no buy box, so no visits (the offer-insights docs say so) and no popularity | Offers v11 `stock.correctedStock` = 0 → unavailable. — [Koopblok](https://partnerplatform.bol.com/nl/idp/koopblok), [offer insights](https://api.bol.com/retailer/public/Retailer-API/v10/functional/retailer-api/offers-insights-and-sales-forecast.html) |
| **Leveringscondities** (delivery time, "vóór 23:00 besteld, morgen in huis", extra delivery-day choice) | Buy-box factor; "Bij artikelen voor dagelijks gebruik speelt snelle levering bijvoorbeeld een grote rol, terwijl bij meubels de prijs vaak belangrijker is" | Not documented as a direct ranking factor. The Leverbeloftescore measures how **attractive** the promise shown is (0–100, 56 days, weighted by visits, compared with a target number from similar partner articles; the cut-off time matters; 60 is needed for Groeibeloning) | [De Leverbeloftescore](https://partnerplatform.bol.com/nl/idp/de-leverbeloftescore) |
| **Kwaliteitsscore** | Buy-box factor; recalculated weekly **on Wednesday**; buy-box position updates in ~20 min (max 1 h) | Not documented as a direct ranking factor. Bolmate claims "minder zichtbaarheid" **[agency]** | Retailers API v11: `GET /retailer/retailers/performance-status` (strikes, policy points, quality score per shipping method) |
| **Conditie** (new or refurbished) | Buy-box factor | – | – |
| **Reviews** | Product reviews are not a buy-box factor (the seller-rating parameter was removed on 30-10-2024, per the ranking notes) | Bol FAQ: more reviews ≠ top position; ranking = relevance + popularity | Indirect via CTR and conversion **[inference]** |
| **Returns** | Part of kwaliteitsscore (returns norm) | Not documented | Agencies call it a "silent product killer" **[agency]** |
| **Customer questions** | Part of kwaliteitsscore (customer-questions norm) | Bolmate lists response speed as a ranking factor **[agency, unverified]** | – |

Other documented buy-box details **[bol-doc]**:
- Price differences of €0.01 have no impact.
- The LvB €2.99 shipping fee under €25 is ignored.
- Bol runs buy-box experiments, so the website can differ from what the seller account shows.
- Sponsored ads never serve without the buy box.

— [Koopblok](https://partnerplatform.bol.com/nl/idp/koopblok)

**[inference] Ranking vs koopblok summary.** Only relevance (content and category) and popularity (clicks and sales) are documented ranking inputs. Price, delivery, quality score and stock act on ranking only through (a) whether you hold the buy box, which is required for any visit or sale to count, and (b) the CTR and conversion they cause. For a single-seller private-label EAN, the buy-box factors matter as **visibility gates**: stock above 0, price below the maximum, 2★ or more to stay online, and a kwaliteitsscore of 65 or more to keep selling. They also matter as conversion levers.

### Checklist: offer

- [ ] Price stars ≥ 3 (SEA budget) and ideally ≥ 4 (promotions). Pull the boundaries daily via the API and keep the price ≤ level 4.
- [ ] Never let `correctedStock` reach 0 on hero EANs. Use `insights/sales-forecast` (weeks-ahead ≤ 12) for replenishment.
- [ ] Make the delivery promise as short as you can reliably keep. Check the Leverbeloftescore (≥ 60) and the "Op tijd geleverd" KPI (`GET /retailer/retailers/kpi-scores?kpi=ON_TIME|FULFILMENT`).
- [ ] Offer visits and buy-box %: `GET /retailer/insights/offer?name=PRODUCT_VISITS` and `BUY_BOX_PERCENTAGE`. Conversion = orders ÷ visits.

---

## 8. Customer questions, content change process and reporting wrong content

### Customer questions **[bol-doc]**

- I found **no bol documentation of a public Q&A section** ("vragen en antwoorden") on bol product pages. Bol product pages could not be fetched (403), so this is unverified on the live page.
- Documented: a customer can use **"Vraag over artikel"** on the product page to contact the seller. This is mentioned on [Merknaam of logo tonen](https://partnerplatform.bol.com/nl/idp/merknaam-of-logo-tonen). Customer questions reach the seller privately, in the seller account or by CRM e-mail.
- Expected response times:
  - 24–48 hours for questions forwarded by bol customer service; after that the question returns to bol.
  - 1 working day for replies in conversations the seller started.
  - A question is flagged as long-open after 18 hours, excluding weekends and holidays.
  — [Klantvragen in je verkoopaccount](https://partnerplatform.bol.com/nl/idp/klantvragen-in-je-verkoopaccount)
- The "Inzichten" page in the seller account shows question **topics** and "welke van je verkochte artikelen relatief veel klantvragen hebben ontvangen", over 28 days to 6 months. Bol's advice: "beantwoord veelgestelde vragen in de productomschrijving". — [Klantvragen (norm)](https://partnerplatform.bol.com/nl/idp/klantvragen)
- The customer-questions norm is part of the kwaliteitsscore. It is dynamic per product group, capped at 15%, with a minimum of 3 questions. See the earlier notes.
- API: `GET /retailer/retailers/kpi-scores?kpi=CASE_ITEM_RATIO|RESPONSE_TIME` (v11 beta) and `GET /retailer/insights/performance/indicator?name=CASE_ITEM_RATIO&year=&week=`. **[bol-data]**

### Content change process and turnaround **[bol-doc]**

| Step | Timing / rule | Source |
|---|---|---|
| Add or change content (seller account, bulk editor, Excel, API) | Processed "binnen 8 uur" | [Productinformatie wijzigen](https://partnerplatform.bol.com/nl/idp/productinformatie-wijzigen) |
| Search index picks up the change | Existing article: at least **1 day**; new article: at least **2 days** | [Zoekalgoritme](https://partnerplatform.bol.com/nl/idp/zoekalgoritme-van-bol) |
| Product family visible | Up to 24 h (product page first, list and search later) | [Productfamilie per stuk](https://partnerplatform.bol.com/nl/idp/productfamilie-aanmaken-per-stuk) |
| API upload report | Wait at least 1 hour before polling; statuses PUBLISHED or DECLINED with a sub-status; kept for **28 days** | [API product content](https://api.bol.com/retailer/public/Retailer-API/suppliers/product-content.html) |
| Feedback in seller account ("Artikelen → Gewijzigde productinformatie → Mijn wijzigingen") | Shows your proposal, its status and the reason; kept for **28 days**. A separate view shows changes **by other sellers**, with who made them | [Productinformatie wijzigen](https://partnerplatform.bol.com/nl/idp/productinformatie-wijzigen) |
| Rejected change ("Afgewezen", usually because another party has a higher contentscore) | Click "oneens" and give a reason. A trained bol employee decides within **24 h** ("geaccepteerd"/"afgewezen"); no reason is shown. You can object again | [Oneens met afwijzing](https://partnerplatform.bol.com/nl/idp/oneens-met-afwijzing-gewijzigde-productinformatie) |
| Accepted content later overwritten | Possible if a partner with a higher content score edits it. "Merkeigenaren kunnen de productinformatie altijd overschrijven" | same |
| Demonstrable error that will not go through | Contact **Partnerservice** | [Productinformatie wijzigen](https://partnerplatform.bol.com/nl/idp/productinformatie-wijzigen) |
| Wrong brand name locked by another brand's protection | Partnerservice | [Merkregistratie](https://partnerplatform.bol.com/nl/idp/merkregistratie) |
| Package dimensions on articles that have ever been in LvB | Set by the bol warehouse and not editable (upload status `REJECTED_BY_LOGISTIC`); go through Partnerservice | same |
| Wrong or unwanted image | Change its view label, or delete it with the bin icon. Images removed by others appear under "Jouw offline afbeeldingen" and can be restored | [Afbeelding per stuk](https://partnerplatform.bol.com/nl/idp/afbeelding-per-stuk-toevoegen) |
| Intellectual-property infringement (your images or brand used by others) | First contact the seller via their shop page or "Vraag over artikel", then the **Notice and Take Down** form | [Merknaam of logo tonen](https://partnerplatform.bol.com/nl/idp/merknaam-of-logo-tonen) |
| Brand protection ("merkregistratie"/"contentbescherming") | For BOIP-registered brands and official distributors. Protects title, description, specifications and images; processing takes about **5 working days**; one authority per brand. **All** content you ever supplied is published retroactively, so clean it up first | [Merkregistratie](https://partnerplatform.bol.com/nl/idp/merkregistratie) |
| French content | BE seller account only; free text is translated once; LOV attributes are re-translated automatically | [Franstalige productinformatie](https://partnerplatform.bol.com/nl/idp/franstalige-productinformatie-toevoegen) |

### Agency practice

- Zoloo 2026: changes processed in 24–48 h, measurable ranking effect after 2–4 weeks. **[agency]**
- Boloo (in the ranking notes): wait 3–5 days before judging. **[agency]**

### Checklist: change process

- [ ] Register the brand (BOIP) and apply for merkregistratie. For a private label this stops other sellers overwriting the title, images and specifications, and gives your labelled images priority.
- [ ] Change one variable per EAN at a time. Log the date and wait at least 1–2 days for indexing and 7–14 days for ranking before judging.
- [ ] Check "Gewijzigde productinformatie → door anderen" weekly, and the upload reports within 28 days.
- [ ] For a rejection, object within the flow and name the error concretely. Escalate demonstrable errors to Partnerservice.

---

## 9. Retailer API endpoints for a read-only automated audit (verified against the specs, 30-09-2026)

Specs checked:
- [Retailer API v10 OpenAPI](https://api.bol.com/retailer/public/apispec/Retailer%20API%20-%20v10) (version 10.x)
- [Product Content v10 YAML](https://api.bol.com/registry/api-definitions/product-content/product-content-v10.yaml) (version 10.2.1)
- [Retailers v11 YAML](https://api.bol.com/registry/api-definitions/retailers/retailers-v11.yaml) (BETA)
- [Offers v11 YAML](https://api.bol.com/registry/api-definitions/offers/offers-v11.yaml)

Common details:
- Media type `application/vnd.retailer.v10+json`; the v11 endpoints use `…v11+json`.
- Auth is OAuth2 client credentials.
- Rate limits are from [/retailer/public/ratelimits](https://api.bol.com/retailer/public/ratelimits). Read the rate-limit headers and back off on 429.
- **Note**: in the v10 spec, the `/retailer/offers*` endpoints (including `POST /offers/export`) and `/subscriptions` are badged **DEPRECATED**. Use Offers API v11 (`GET /retailer/offers`, `GET /retailer/offers/{offer-id}/not-for-sale-reasons`).

| # | Endpoint (all GET unless noted) | Key params | Returns | Audit use | Rate limit |
|---|---|---|---|---|---|
| 1 | `/retailer/content/catalog-products/{ean}` (Product Content v10) | `Accept-Language: nl, nl-BE, fr, fr-BE` | `published` (bool), `gpc.chunkId`, `enrichment.status` (0 offline / 1 online with optional fields missing / 2 complete), `attributes[{id, values[{value, unitId, valueId}]}]` (includes Name and Description), `parties[{name,type,role}]` (brand), `series` | Content completeness vs the data model; title length and patterns; description length and HTML; forbidden words; fr-BE content check. Shows the **winning** content (can be a mix of suppliers) | 10/s |
| 2 | `POST /retailer/content/chunk-recommendations` (Product Content v10) | body `{"productContents":[{"attributes":[{"id":"Name","values":[{"value":…}]},{"id":"Description",…}]}]}` (exact casing) | top 3 `predictions[{chunkId, probability}]` | Product-group sanity check vs `gpc.chunkId` | 10/s |
| 3 | `/retailer/content/upload-report/{upload-id}` (Product Content v10) | – | per attribute or asset: `status` IN_PROGRESS/DECLINED/PUBLISHED, `subStatus` (e.g. REJECTED = "selected product information of others", REJECTED_BY_BRAND_AUTHORITY, SCORED_OTHER_IMAGE_WON, IMAGE_FLAGGED_AS_DUPLICATE, VALIDATION_FAILED_INVALID_LOV_VALUE), `subStatusDescription` | Only for your own uploads; kept 28 days | 10/s |
| 4 | Data model JSON (not an API): `https://productdatamodel.s-bol.com/v10/datamodel_v10_{nl,fr,en}.json` (~39 MB, updated daily) | – | `attributes` (with `validation.maximumLength`, fill instructions), `chunks[{id,name,attributes[{id,enrichmentLevel,lovId,condition}],labels,distinctiveFeatureIds}]`, `lovs`, `labels` | Reference for required attributes, allowed values, allowed image labels and family features | – |
| 5 | `/retailer/products/{ean}/assets` | `usage=PRIMARY\|ADDITIONAL\|IMAGE` | `assets[{usage, order, variants[{size small\|medium, width, height, mimeType, url}]}]` | Image count, carousel order, main-image check (download it and check whiteness, resolution, text via OCR) | 50/min |
| 6 | `/retailer/products/{ean}/placement` | `country-code=NL\|BE`, `Accept-Language: nl\|nl-BE\|fr-BE` | `url` (product page), `categories[{categoryId, categoryName, subcategories}]` | Checks the shop category tree placement and the URL/title slug | 50/min |
| 7 | `/retailer/insights/product-ranks` | `ean`, `date` (yesterday up to 3 months back), `type=SEARCH\|BROWSE` (or omit for both), `page` (50/page, max 200), `Accept-Language: nl-NL,nl,nl-BE,fr,fr-BE` | `ranks[{categoryId, searchTerm, rank, impressions, wasSponsored}]`, `hasNextPage` | Organic rank per search term and category per day; impressions (≥1 s, ≥50% viewable). Filter `wasSponsored=false` | 10/s |
| 8 | `/retailer/insights/search-terms` | `search-term`, `period=DAY\|WEEK\|MONTH`, `number-of-periods`, `related-search-terms=true` | `searchTerms{searchTerm, type, total, countries[{countryCode,value}], periods[{period{day,week,month,year}, total, countries}], relatedSearchTerms[{searchTerm,total}]}` | Keyword volume and seasonality, NL vs BE split; max 365 d / 104 w / 48 m; refreshed daily 05:00 | 10/s |
| 9 | `/retailer/insights/offer` | `offer-id`, `period=DAY\|WEEK\|MONTH`, `number-of-periods` (max 730 d / 104 w / 24 m), `name=PRODUCT_VISITS\|BUY_BOX_PERCENTAGE` | `offerInsights[{name, type, total, countries[], periods[]}]` | Visits (only while you hold the buy box) and buy-box %. Conversion = orders ÷ visits (orders from `GET /retailer/orders`) | 25/s |
| 10 | `/retailer/insights/sales-forecast` | `offer-id`, `weeks-ahead` 1–12 | min/max forecast total and per country/week (ranges when fewer than 2 sales in 28 days) | Stock-out risk | 25/s |
| 11 | `/retailer/products/{ean}/price-star-boundaries` | – | `lastModifiedDateTime`, `priceStarBoundaryLevels[{level, boundaryPrice}]` | Compute the current star level (5★ ≤ level-5 price … 1★ > level-2 price); alert below 3★ or at 1★ (offline risk) | 50/s |
| 12 | `/retailer/products/{ean}/ratings` | – | `ratings[{rating 1–5, count}]` | Review count and average; share of 1–2★ | 50/min |
| 13 | `/retailer/products/{ean}/offers` | `country-code`, `best-offer-only`, `condition`, `page` | Competing offers: `retailerId`, `price`, `fulfilmentMethod`, `bestOffer`, `ultimateOrderTime`, `min/maxDeliveryDate` | Hijacker detection on private-label EANs; buy-box owner | 900/min |
| 14 | `/retailer/products/{ean}/product-ids` | – | `bolProductId`, all related `eans` | Maps EAN to the bol product ID (for URLs and duplicate EANs) | 50/min |
| 15 | `/retailer/products/list-filters` and `POST /retailer/products/list` | `search-term` or `category-id`, `country-code`, filters, `sort=RELEVANCE\|POPULARITY\|PRICE_ASC\|…\|RATING\|WISHLIST`, `page` | Available filters for a query or category; product list (`title`, `eans`), 50 per page | Competitor titles and page-1 composition without scraping; shows which filters exist (maps to attributes) | 50/min each |
| 16 | `/retailer/products/categories` | `Accept-Language` | Full category tree | Category IDs for #15 | **1/min** |
| 17 | `/retailer/insights/performance/indicator` | `name=CANCELLATIONS\|FULFILMENT\|PHONE_AVAILABILITY\|RESPONSE_TIME\|CASE_ITEM_RATIO\|TRACK_AND_TRACE\|RETURNS\|REVIEWS`, `year`, `week` | `score{conforms, numerator, denominator, value, distanceToNorm}`, `norm{condition, value}` | Weekly service norms (last 30 weeks) | 20/min |
| 18 | `/retailer/retailers/kpi-scores` (Retailers v11, BETA) | `kpi=CANCELLATIONS\|CASE_ITEM_RATIO\|FULFILMENT\|HANDOVER\|ON_TIME\|RESPONSE_TIME\|RETURNS\|REVIEWS\|TRACK_AND_TRACE`, week | score, norm, period, `excluded` (from strike calculation) | Newer superset of #17 | 20/min |
| 19 | `/retailer/retailers/performance-status` (v11, BETA) | – | `monitoringSystem` (strikes: count 0–7, weeks with reasons), `policy` (policy points), `qualityScore{yearWeek, score 0–100, shippingMethodScores[…kpiName, score, norm, aggregationLevel]}` | Kwaliteitsscore, strikes and policy points in one call | 10/min |
| 20 | `/retailer/retailers/{retailer-id}/ratings` (v11, BETA; `current` for yourself) | – | `retailerRating`, `productInformationRating`, `deliveryTimeRating`, `shippingRating`, `serviceRating`, `ratingMethod`, `isTopRetailer`, review sentiment counts | Seller rating incl. the "productinformatie" sub-rating | 120/min |
| 21 | `/retailer/offers` and `/retailer/offers/{offer-id}/not-for-sale-reasons` (Offers v11) | `eans`, `for-sale`, `page-size` ≤100, `cursor` | Offer, stock (`amount`, `correctedStock`), pricing, fulfilment (`method` FBR/FBB, `schedule` BOL_DELIVERY_PROMISE/MY_DELIVERY_PROMISE/SHIPPING_VIA_BOL, `deliveryPromise`); reasons by category CONTENT (with `missingAttributes`), PRICE ("Price too high"), STOCK, SHOP_STATUS, SELLING_RIGHTS, ASSORTMENT_POLICY… | Why an offer is offline; stock continuity; delivery-promise setup | 25/s GET list; 50/s per offer |
| 22 | `/retailer/delivery-promise/profiles` (Delivery Promise v1) | – | Mijn Leverbelofte profiles | Checks cut-off and delivery days vs the 3PL | see ratelimits |

Not available via the API (seller account only) **[inference, from the docs]**:
- the content score / content rating;
- the Leverbeloftescore;
- the customer-question topic insights;
- bol zoektrends "gerelateerde zoekwoorden" for multi-term comparison (partly via #8);
- the "Conversie analyse" report;
- video presence (#5 returns images only; #1 attributes do not include video).

**[inference] Minimal audit pipeline per EAN (read-only)**:
1. #14 and #1 (nl + fr-BE) → content snapshot.
2. #4 → required and optional attributes for `gpc.chunkId`; completeness % and missing filter attributes.
3. #2 → does the product-group prediction match?
4. Title rules: ≤70 characters, starts with the brand, contains the product-group noun, no all-caps words, no symbols or forbidden words, no synonym stacks.
5. Description rules: 500–3000 characters, only the allowed tags, the title noun within the first 120 characters.
6. #5 → at least 6 images, main image ≥1200 px (download the original URL; medium is resized).
7. #12 and #20 → review stats.
8. #11 → price stars.
9. #7 (nl, fr-BE; SEARCH + BROWSE; last 30 days) → rank and impressions per term.
10. #8 → volume per term → opportunity = volume × (rank > 10).
11. #9 → visits and buy-box %; plus orders → conversion.
12. #21 → not-for-sale reasons and stock.
13. #18 and #19 → account health.

Store the results daily, because ranks go back only 3 months and the seller account shows 14–30 days.

---

## Gaps and open questions

- **Title length**: bol contradicts itself (70 max on the title page vs 30–150 on the content page). The per-product-group xlsx has no length. The only hard limit is 250 characters.
- **Brand-first vs keyword-first**: bol's templates are brand-first. Zoloo advises keyword-first. No bol or agency A/B data compares the two outside fashion (bol's size-not-in-title +10% test).
- **Description indexing**: not confirmed or denied by bol. Evidence is indirect (category classification, "words from title in description").
- **Content score** formula, weights and visibility: unpublished. It is not in the API.
- **Family size limit**: 250 (partnerplatform) vs 70 (API docs).
- **Family effect on ranking**: bol says views and reviews are pooled and you can "meeliften op de pagina-ranking", but not how search results collapse or represent family members.
- **French search data**: the search-terms endpoint has no language parameter. Whether Walloon French queries are included, and at what volume, is unknown. French keyword candidates are untested.
- **Reviews in French**: bol's rules say non-Dutch reviews are rejected. How that applies to fr-BE customers is not documented.
- **Package inserts**: bol's 2026 text ("niet toegestaan … zelf om een review te vragen") does not mention inserts. Agencies still recommend QR inserts. There is no bol ruling either way.
- **Public Q&A on product pages**: no bol documentation found, and live pages were blocked (403). It needs a manual check in a browser.
- **Video**: no maximum length. There is no API read-back to confirm which video is live or whether it was overwritten.
- **Image conversion uplift on bol**: bol publishes a number for titles ("tot 20% meer conversie"), families (+10% sales) and size-not-in-title (+10%), but nothing for image count or video. Agency figures are generic.
- **Auto-generated titles**: no evidence that bol generates Dutch partner titles from attributes. Only the one-time French machine translation and the AI attribute enrichment (2024 pilot) are documented.
- **e-tailize**: no relevant 2025–2026 bol listing guidance found. Channable's help article on bol image views returned 404.
