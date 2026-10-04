# How Jack Bloomfield set up Bloom Build (factory relationships, QC, trust), Quince lessons, and the playbook for premium bedding in NL/EU

Research date: 4 Oct 2026. This adds to `jack_bloomfield_model.md` and does not repeat it (that file covers ACN, cost-stack snippet, refund policy, Made.com and the EU €3 duty).

**Labels used**
- **[FACT]**: verifiable, e.g. something a page or listing shows, a publication date or a view count.
- **[CLAIM]**: Jack or Bloom Build says it.
- **[INFERENCE]**: my own reasoning.
- **[FOUNDER PREMISE]**: Joost's assumption, passed on by the coordinator.

**Method note, and what is new compared with the earlier notes.** YouTube transcripts stayed blocked: the transcript API returned "IpBlocked", the get_transcript endpoint returned "FAILED_PRECONDITION", and the third-party transcript sites returned 403 or empty pages. However, YouTube's public page data returned the **full titles, publication dates, view counts, descriptions and chapter lists** for all 22 episodes of his weekly series *"Building Bloom Build"* (May–Oct 2026), and for his Shorts. Jack writes these descriptions as detailed episode summaries, so they are the richest primary source available. The Bloom Build Shopify store data was also read (products.json, pages.json, rendered About, Shipping, Trade and Warranty pages). LinkedIn (HTTP 999), Reddit (blocked) and the Judge.me review data (store not found under the shop domain) remained inaccessible. Every YouTube citation below is to the video page. The content cited is the creator's own description or chapter text, not a transcript.

---

## 1. What his YouTube series, media and podcasts reveal: timeline and numbers

### Takeaway
Bloom Build is very young. Jack moved to Hong Kong around early 2026. The site went live on about 20 June 2026, and the first online order shipped in late June 2026. Everything is documented in a weekly, professionally produced "build in public" series. The numbers he has stated publicly are all [CLAIMS], and loose ones:
- "hundreds of thousands of dollars in orders" within a few weeks (August 2026)
- a 10% conversion from sample to full order
- each sample box takes in about $12 and costs about $20
- 12 suppliers across China
- one freight deal that saves $150k a year
- 28 orders and 1,000 samples in the queue before Golden Week (early October 2026)

### Cited Findings

**Timeline, built from the episode descriptions (all [FACT] for dates and views; [CLAIM] for content)**
- **30 Aug 2024**, "bts: starting a business in china at 22": a trip to Foshan, described there as "China's furniture city", to source suppliers, tour furniture factories and "negotiate bulk order deals". This was the exploratory phase, about 18 months before Bloom Build — [YouTube](https://www.youtube.com/watch?v=ADzo5eEdHd8)
- **Jan–Apr 2026**, Shorts about sourcing. Titles include:
  - "How to pay Chinese Suppliers!" (271k views)
  - "How Fake 'Factories' in China Scam New Brands"
  - "China Looks Cheap Until You See the Real Costs (This Is Why Businesses Fail)"
  - "This 'Hot' Product Looks Profitable… Until You See the MOQ"
  - "Your China Supplier Isn't Screwing You Over — You're Telling Them To" (15 Apr 2026)
  - "The 3 China Sourcing Fairs You Need to Know"
  - "Inside the Canton Fair…"
  - "Bunnings Is Not Aussie, The Factories Prove It"

  Only the titles were retrievable — [Shorts tab](https://www.youtube.com/@jackbloomfieldbts/shorts); [example](https://www.youtube.com/watch?v=4u4Z8pnyhj0)
- **8 Apr 2026**: the Shopify "About" page was created. The Shipping page followed on 4 May, Trade on 16 May, FAQ on 26 May and the 10-year Warranty on 31 Aug 2026 [FACT, from the store's pages.json created_at fields] — [buybloombuild.com/pages.json](https://buybloombuild.com/pages.json)
- **2 May 2026**, EP1 "moving to China at 23 to build my second startup" (35k views): "This video isn't about moving to Hong Kong. It's about starting again from zero" — [YouTube](https://www.youtube.com/watch?v=TMbknFlEj6g)
- **9 May 2026**, "Inside My Chinese Startup" (Foshan supplier meetings, covered in section 2) — [YouTube](https://www.youtube.com/watch?v=ZCKbMiJ6OR4)
- **16 May 2026**, "Negotiating With China's Biggest Factories". With 270k views, this is his most-watched long-form video — [YouTube](https://www.youtube.com/watch?v=zt3F7kRB5ik)
- **20 Jun 2026**, "Going Live for the First Time": "After three months on the ground in China building a direct-to-factory supplier network, Bloom Build finally goes live". The episode covers "dynamic factory-direct pricing", the marketing strategy from day one, the first orders, and "calling our first customers one by one" — [YouTube](https://www.youtube.com/watch?v=APzVQOjjm7o)
- **28 Jun 2026**, "Biggest Shipment Yet": "Bloom Build ships its first online order". Note that this description says "Six months after moving to China", while the 20 June one says "three months", which is inconsistent — [YouTube](https://www.youtube.com/watch?v=Oo1l2kBVAcM)
- **10 Jul 2026**: news.com.au published the video "24 year-old Aussie's billion-dollar move stuns China" ("At just 16, Jack Bloomfield made himself a fortune… Now, he is taking on China"). This is independent media coverage, and its framing is profile journalism, not verification — [YouTube/news.com.au](https://www.youtube.com/watch?v=pxhtF275XOU)
- **1 Aug 2026**, "Growing Too Fast": "Our orders exploded this month". A backlog of sample orders built up, and a customer emailed that "our competitors beat us to the sale". Jack calls this the "first conversion from a sample box to a real tile order". He made three fixes:
  - "cutting our range down to a core set of styles"
  - "buying sample stock upfront"
  - "handing fulfilment to a 3PL so every box ships within hours"

  — [YouTube](https://www.youtube.com/watch?v=Q8z_gs8R76k)
- **8 Aug 2026**, "Every Order We Ship Loses Money": "We have taken **hundreds of thousands of dollars in orders**, and right now every single one loses money… shipping quotes of **$1,000 on orders our customers paid $500 for**". The episode includes an "underground freight forwarder in Shenzhen with no signage" and three options: "refund everything, ship direct, or consolidate and make customers wait". He ran a test of 75 kg of tiles to Australia — [YouTube](https://www.youtube.com/watch?v=zvVg61patS0)
- **15 Aug 2026**, "We're Losing $105,000 Every Week": "most of our orders start with a sample… **Only 10% do** [convert]". He hires a first salesperson in response — [YouTube](https://www.youtube.com/watch?v=60vXK94474w)
- **22 Aug 2026**, "Why I Don't Take Money From VCs": a VC fund "with nearly a billion dollars under management" has courted him since 2021. In his previous company he "raised tens of millions". Bloom Build is presented as not VC-funded. The episode also shows "the daily team sync with our people on the ground in China" — [YouTube](https://www.youtube.com/watch?v=0qghQn0coVk)
- **29 Aug 2026**, "Unlocking China Shipping": a new freight partner, covered in section 2. The deal "saves us **$150,000 a year**" — [YouTube](https://www.youtube.com/watch?v=i4UmTLUjk38)
- **5 Sep 2026**, "Preparing My Business for 10,000 Orders a Month": the episode covers:
  - a "sample operation hidden 100 meters from our supplier that can cut thousands of samples a day"
  - "why tile factories cannot make samples"
  - "consolidating **12 suppliers** across China into one system"
  - "from 15 steps in the back of Matthew's car down to 3"
  - "a third party logistics warehouse so every sample ships the same day"

  — [YouTube](https://www.youtube.com/watch?v=B9WaFbfGyBQ)
- **12 Sep 2026**, "Proving You're Paying Double" (142k views): "how we do all seven jobs ourselves (quality control, palletizing, freight, and delivery) to land 50% cheaper", and "the transparent cost model we publish" — [YouTube](https://www.youtube.com/watch?v=g6TTeH1X2kU)
- **20 Sep 2026**, "Why Everything You Own Was Bought for 10x Less": he finds a tile sold by "Australia's biggest tile retailer" at $45–65/m² "at the factory in 15 seconds… Under $10", and sells it "for $26 with every cost shown". The episode also covers "how we check quality at the source (trust but verify)" and "the automated system that fulfils an order with no humans in the loop except a QC inspector" — [YouTube](https://www.youtube.com/watch?v=X6ZsjEAEh8k)
- **26 Sep 2026**, "Why We Lose Money on Purpose": "we take **$12 and spend $20 on every box**". He says "you cannot buy trust with an ad, so stop asking people for a huge jump and give them a small leap first" — [YouTube](https://www.youtube.com/watch?v=ExJe92ksibU)
- **3 Oct 2026**, "Before China Shuts Down": "I have **28 orders and 1,000 samples** to get out before" Golden Week. He says the first job is "telling every customer the real delivery date before they feel the delay" — [YouTube](https://www.youtube.com/watch?v=XlU6mOOw8MY)
- Production: since September the series has been credited "Produced By Byron Morgan | Exportfilms" [FACT] — [YouTube](https://www.youtube.com/watch?v=B9WaFbfGyBQ)
- The series playlist is titled "Bloom Build: Building a Billion Dollar Startup in China" [FACT] — [Playlist](https://www.youtube.com/playlist?list=PL5XRGZOI0cdtRAJK8XRfnNIBGM8mANV-g)
- The site claims "As covered by news.com.au" and "Channel 9 · 4 min · Why tiles cost so much in Australia… A tile leaves the factory at $12/m² and lands on an Australian floor at $89/m²" [CLAIM] — [buybloombuild.com](https://buybloombuild.com/)
- Search snippets also attribute coverage on Channel 10's The Project, Sunrise and Forbes to him [CLAIM, via LinkedIn snippet; not verified] — [LinkedIn](https://hk.linkedin.com/in/jack-bloomfield)

### Inferences
- Order of events: three months of supplier-building on the ground (about March–June 2026), then a soft launch, then a sample-led funnel. Logistics nearly broke the unit economics within 6–8 weeks of launch, and were fixed by renegotiating freight and moving to a 3PL. The real work after the factory deals was **logistics and sample operations**, not the factory conversation itself [INFERENCE].
- Scale check: 28 orders versus 1,000 samples in the Golden Week queue, together with "10% conversion", points to a business that in October 2026 still runs on a few hundred to a few thousand full orders in total. "Hundreds of thousands of dollars" in orders is plausible at an average order of A$1–3k [INFERENCE; no AOV is published].
- The "$105,000 a week on the table" figure is most likely the unconverted sample pipeline multiplied by an assumed order value. It is a marketing framing, not lost revenue [INFERENCE].
- Long-form views (12k–270k per episode) and news.com.au coverage are a low-cost acquisition engine. The content itself is the "trust" asset [INFERENCE].

### Gaps
- No transcripts, so the actual words in the chapters remain unknown. This covers chapters such as "The payment-terms secret", "MOQ trick that cuts your upfront cash by 90%", "Breaking the MOQ", "FCL vs LCL", "The $600 shipping wall" and "QC + how China innovates". A human watching episodes 7DfS1DCWc-8, sq87s3r_RMo, zt3F7kRB5ik and X6ZsjEAEh8k (about 2 hours in total) would close most remaining gaps.
- No revenue, gross margin or AOV stated anywhere. No podcast appearances about Bloom Build were found. The podcasts that were found date from his Disputify/dropshipping era and are listed in the earlier notes.

---

## 2. Factory relationships: how he found and approached factories, got them to sell from stock, and what terms he got

### Takeaway
His method is to show up in person in Foshan or Guangzhou with a Chinese-speaking local employee, and pitch factories (not trading companies) to sell **their existing stock** to Australian end customers through Bloom Build, cutting out the importer, distributor and showroom. Some factories refused, and one tried a 20% surcharge. The large factory that agreed asked for **a 12-month volume commitment in exchange for competitive pricing from day one**. He says he got factories to drop MOQs "to nothing", and that competitors have since pressured factories to "ban" him from their best stock. This supports Joost's premise that "it's about the conversations with factories", with two caveats: it took a local relationship manager, and the moat is fragile.

### Cited Findings
- The pitch [CLAIM]: "stop selling to Australian retailers. Sell directly to Australian consumers, through us. Cut out the four middlemen sitting between the factory and the homeowner." It means asking factories "to break a model they've been running for 30 years" — [YouTube EP2](https://www.youtube.com/watch?v=ZCKbMiJ6OR4)
- Day-1 outcomes in Foshan [CLAIM]: "Some of them get it. Some don't. One supplier admits their entire stock-tracking system lives in a single person's brain. Another tries to charge us 20% more for the privilege of selling their own inventory. By the end of the day, we've got two suppliers locked in" — [YouTube EP2](https://www.youtube.com/watch?v=ZCKbMiJ6OR4)
- The large-factory deal [CLAIM]: "The first supplier produces 200 million square metres of tile a year. 18,000 employees across four production bases. The most SKUs of any tile company in China. They listened. They pushed back. Then they came back with a counter…: **competitive pricing from day one, in exchange for a real volume commitment over 12 months**." He describes the chain he is cutting as "Factory, agent, brand, retailer, customer. Four layers". Relationship-building included a Foshan banquet next to "the biggest LED panel manufacturer in China"; "Neither of us speaks a word of Mandarin" — [YouTube](https://www.youtube.com/watch?v=zt3F7kRB5ik)
- The playbook episode, "A Chinese Factory Told Me I'd Destroy the Market" (18 Jul 2026, 57k views) [CLAIM]. It promises "how we negotiate directly with Chinese factories, **why we hold zero inventory, how we got suppliers to drop their MOQs to nothing, why showing up in person beats showrooms every time**". Chapters include:
  - "Show up in person"
  - "'We'll do that together' – Lewis" (apparently a factory counterpart)
  - "Why the West trusts China now"
  - "Finding your wedge"
  - "Real factories, not showrooms"
  - "This isn't for everyone"
  - "Lewis's biggest problem"
  - "Zero inventory risk"
  - "QC + how China innovates"
  - "The warehouse"
  - "FCL vs LCL shipping"
  - "Breaking the MOQ"
  - "The $600 shipping wall"

  The episode follows "one real customer order from raw sandstone to a finished tile" in a "300-acre tile factory" — [YouTube](https://www.youtube.com/watch?v=7DfS1DCWc-8)
- Pushback from incumbents, and negotiating rules [CLAIM]: "Competitors have already convinced factories to **ban us from buying their best stock**". The episode promises "the **payment-terms secret** that keeps the whole system alive, the **first-year rule** of negotiating in China, and the **MOQ trick that cuts your upfront cash by 90%**". Other chapters: "The Aldi Playbook", "Never Negotiate First", "One More Door" — [YouTube](https://www.youtube.com/watch?v=sq87s3r_RMo)
- Day of four suppliers in Guangzhou [CLAIM]: "Hours of negotiating, walking, pitching the same model again and again" — [YouTube](https://www.youtube.com/watch?v=tSQ14tVjrWQ)
- The supplier base had grown to "**12 suppliers across China**" by September 2026, consolidated "into one system" [CLAIM] — [YouTube](https://www.youtube.com/watch?v=B9WaFbfGyBQ)
- Freight negotiation, an example of his negotiating style [CLAIM]. Two asks "mattered more than a cheaper rate": "a new pricing tier for small shipments and getting the handling charges waived". He uses "the placard system we use to prepare for every big meeting in China" and puts "the question back on the other side instead of feeding them demands". He calls the result "the moment they went from no to yes" — [YouTube](https://www.youtube.com/watch?v=i4UmTLUjk38)
- The people side [CLAIM]. Connie was hired in Guangzhou. Hiring criteria: "drive over competence, commercial awareness, culture fit". She "transformed our suppliers, quality control, and logistics", and then quit — [YouTube](https://www.youtube.com/watch?v=AmKQXzbfLGE). Connie was "the person who found every supplier and built every relationship in this series", and she handed over to Matthew — [YouTube](https://www.youtube.com/watch?v=sq87s3r_RMo). A LinkedIn post sought "a Chinese-speaking A player based in (or around) Foshan to lead sourcing and quality and help build our China team" [CLAIM, via search snippet] — [LinkedIn](https://www.linkedin.com/in/jack-bloomfield/)
- Why factory stock is possible in tiles: tile factories keep large standard collections. The episode on samples says "tile factories cannot make samples", so he built a separate sample-cutting operation 100 m from a supplier [CLAIM] — [YouTube](https://www.youtube.com/watch?v=B9WaFbfGyBQ)
- Product and catalogue facts (4 Oct 2026) [FACT]:
  - 55 full-size tile SKUs plus 55 matching A$5 sample SKUs, all with vendor "BloomBuild".
  - Prices run from A$26.46 to A$101.52 per m², median about A$42.
  - The earliest products were created on 12 May 2026.
  - Some carry the tag "archived-sep26", consistent with the "cut our range to a core set" decision.
  - Product copy: "Sourced direct from our manufacturing partners - the same factories supplying many of Australia's premium tile retailers."

  — [products.json](https://buybloombuild.com/products.json)

### Inferences
- "Selling from their stock" in practice means Bloom Build is a white-label reseller of standard factory collections. The SKUs are renamed after Australian places, and the factory brand never appears. In return the factory gets a new direct-retail channel with cash up front and no design work. The factory's risk is channel conflict with its existing Australian importers, which explains both the "20% surcharge" and the "ban" stories [INFERENCE].
- The 12-month volume commitment is the real currency of the deal. "MOQs to nothing" probably applies per order (picking from stock), while an aggregate annual volume is promised [INFERENCE, based on the EP3 description].
- Without a Mandarin-speaking, commercially sharp local employee, the model stalls. Jack lost his first one within about a month [INFERENCE].

### Gaps
- Actual payment terms (deposit, payment on pickup, credit), contract form (written vs WeChat), exclusivity, and the size of the 12-month volume commitment: the topics are named in chapter titles but their content is unknown.
- The identity of the factories: not named anywhere. "Lewis" is unidentified.

---

## 3. Quality control in China, team set-up, and why Hong Kong

### Takeaway
QC is done **at source, per order, by Bloom Build's own small China team**: first Connie, then Matthew, plus at least one QC inspector. The principle is "trust but verify", and the inspector is the only human step in an otherwise automated order flow. Jack runs the business from Hong Kong with a daily 15-minute sync with the China team. No third-party inspection firm is mentioned anywhere. He gives no explicit reason for Hong Kong; the reasons below are inferences.

### Cited Findings
- First order QC [CLAIM]: "We are in China to inspect the tiles before they ship, the quality control process **with our team on the ground**, the problems that pile up in real time, and the race to get a container on a boat… This customer didn't even order a sample, so what we send is the first thing they see. If we can't get one order right, how do we ever get to fifty?" — [YouTube](https://www.youtube.com/watch?v=Oo1l2kBVAcM)
- "How we check quality at the source (**trust but verify**), the automated system that fulfils an order with **no humans in the loop except a QC inspector**". The chapter "Factory Warehouse Quality Test" is shown [CLAIM] — [YouTube](https://www.youtube.com/watch?v=X6ZsjEAEh8k)
- "We do all seven jobs ourselves (**quality control, palletizing, freight, and delivery**)" [CLAIM] — [YouTube](https://www.youtube.com/watch?v=g6TTeH1X2kU)
- Site claims [CLAIM]:
  - "First-grade, every time… same production lines… We don't sell seconds, factory rejects or B-grade stock. **We quality control every order before it ships**" — [About](https://buybloombuild.com/pages/about)
  - The shipping timeline says "Week 1 – Factory dispatch: Your tiles are packed, quality-checked, and loaded for shipping" — [Shipping & Delivery](https://buybloombuild.com/pages/shipping-delivery)
- Operating rhythm [CLAIM]: "a full day running the business from Hong Kong, the **daily team sync with our people on the ground in China**" (chapter "The 15 Min Team Sync") — [YouTube](https://www.youtube.com/watch?v=0qghQn0coVk)
- Hong Kong framing [CLAIM]: "Building Bloom Build follows Jack Bloomfield as he **moves to Hong Kong** to build a direct-from-factory building supply business out of China" — [YouTube](https://www.youtube.com/watch?v=APzVQOjjm7o)
- Hong Kong was also the base for supplier hunting at "Hong Kong's Biggest Fair" (an "AI suppliers" episode) [FACT, title] — [Channel videos](https://www.youtube.com/@jackbloomfieldbts/videos)

### Inferences
- **Why Hong Kong** [INFERENCE; not stated in any accessible source]: an English-speaking common-law base, easy banking and payments in USD, CNY and HKD, no mainland work-visa complexity, and roughly 1–2 hours by train to Foshan and Guangzhou. It also gives him the personal-brand story of "the Aussie in China".
- The QC set-up is lean and visual: inspecting factory stock in the warehouse before palletising. That works for tiles, where defects are visible, sizes are standard and shade/batch is checked by eye. For textiles it would not be enough without lab testing; see the playbook in section 7.
- His warranty shifts much of the shade and visible-defect risk to the customer's own inspection before installation (section 4). That is a legal backstop that complements the thin QC [INFERENCE].

### Gaps
- The number of QC staff, inspection standard (AQL or otherwise), defect or breakage rates, and whether any lab tests (e.g. slip or PEI) are commissioned independently rather than taken from factory data.

---

## 4. Building customer trust: transparency, samples, content, and how breakage and claims are handled

### Takeaway
Trust rests on four pillars:
1. **Radical cost transparency**: a published cost stack and "cost-plus" pricing.
2. **A loss-leading A$5 sample box**, explicitly framed as buying trust.
3. **Weekly founder content plus mainstream media.**
4. **Proactive delivery communication, a free damage replacement and a 10-year warranty.**

The warranty is generous in headline but strict in its conditions.

### Cited Findings
- Transparency [CLAIM]: "Transparent Pricing: We show you exactly how we price tiles… Just straightforward **cost-plus margins**". The About page breaks down retail markups as importer 25–40%, distributor 20–30% and showroom 100–200%. It compares "Major Retailers $89–$95/m²" with "$19–$27/m²" ("Same quality. 72% less cost.") — [About](https://buybloombuild.com/pages/about)
- Sample philosophy [CLAIM]: "the fear everyone has buying online (wrong colour, wrong size, arrives late or never)… bigger when it is a bathroom you saved years for from a company 8,000 kilometres away… **we take $12 and spend $20 on every box**… you cannot buy trust with an ad… give them a small leap first" — [YouTube](https://www.youtube.com/watch?v=ExJe92ksibU). Packaging was treated as the first trust touchpoint: "Get it right and they trust us. Get it wrong and we lose the sale" — [YouTube](https://www.youtube.com/watch?v=OimEV4MzcAA)
- Customer contact [CLAIM]: "calling our first customers one by one to find out who they really are" — [YouTube](https://www.youtube.com/watch?v=APzVQOjjm7o)
- Delay communication [CLAIM]: "telling every customer the real delivery date before they feel the delay" — [YouTube](https://www.youtube.com/watch?v=XlU6mOOw8MY)
- The shipping page sets expectations up front [FACT, site text]: "We don't hold stock in Australia… shipped by sea freight to your door. It takes 3–6 weeks, and it's why our prices are up to 60% lower". There is a 4-step timeline from "Day 0" to "Weeks 4–6", and "Damaged on arrival? We replace them free." — [Shipping & Delivery](https://buybloombuild.com/pages/shipping-delivery)
- 10-year warranty (page created 31 Aug 2026) [FACT, site text]:
  - It covers manufacturing defects: cracking not caused by installation, glaze delamination or crazing, and body failure.
  - It is provided by "BloomBuild AU Pty Ltd (ABN 41 698 205 408)".
  - Conditions:
    - "Inspect before you install… Installation of a tile is acceptance of its visible condition"
    - "Dry-lay first… drawing from several boxes"
    - professional installation to AS 3958.1
    - correct application
    - pH-neutral cleaning
    - residential use only, with 2 years for commercial
    - for trade/credit accounts, valid "only while all amounts owing… are paid in full and on time"
  - Technical ratings are "as tested by the manufacturer", with no warranty that they will be maintained.

  — [Warranty](https://buybloombuild.com/pages/warranty)
- Social proof [CLAIM]: "4.75 average · 1,249 verified reviews" and "Renovators, tilers and developers who skipped the middleman" — [Home](https://buybloombuild.com/). The Trade page says "Used by 120+ builders" and "AU/NZ compliant" — [Trade](https://buybloombuild.com/pages/trade)
- Founder-content trust: the stated aim of the series is "Not the polished version. The real one", and "Steal everything that's useful" [CLAIM] — [YouTube](https://www.youtube.com/watch?v=ZCKbMiJ6OR4); [YouTube](https://www.youtube.com/watch?v=7DfS1DCWc-8)

### Inferences
- The review count (1,249 by early October 2026, about 3.5 months after launch, against "28 orders" in the Golden Week queue) probably includes **sample-box reviews**, which are easy to collect. It should not be read as 1,249 full orders [INFERENCE]. The page code shows a Judge.me widget, but the store's public Judge.me page returned "Store Not Found", so the count could not be checked independently.
- The cost transparency numbers are **internally inconsistent**, a reputational risk:
  - "Under $10" ex-factory (YouTube)
  - "$12/m²" (Channel 9 blurb)
  - "materials $9.69" (LinkedIn snippet, earlier notes)
  - "leaves the factory at around $25/m²" (the factory-direct landing page, per my scrape)
  - Retail anchors vary between $45–65, $70, $89–95 and $146/m².

  A copycat should publish one auditable cost stack per SKU [INFERENCE; the $25 figure comes from my scrape of [the landing page](https://buybloombuild.com/pages/bloom-build-factory-direct-tiles-australia)].

### Gaps
- The real breakage and claim rate, claim handling time, and any ACCC or Fair Trading complaints were not found.

---

## 5. What criticism or customer experiences exist (Reddit, ProductReview, Google)?

### Takeaway
**I found no independent customer reviews or criticism of Bloom Build.** Web search for "Bloom Build" or "BloomBuild" together with reddit, ProductReview or Trustpilot returned only unrelated tile games and brands. Reddit search was blocked, and the Judge.me public page was not found. Bloom Build's own videos are the best available record of failure points:
- every order losing money on freight
- a sample backlog
- losing a sale to competitors on speed
- losing its key employee
- being "banned" from some factories' best stock
- Golden Week delays

### Cited Findings
- The search for reviews returned no Bloom Build results — [search performed 4 Oct 2026; no URL]
- Self-reported problems [CLAIM]:
  - "a customer email telling us our competitors beat us to the sale" — [YouTube](https://www.youtube.com/watch?v=Q8z_gs8R76k)
  - "every single one loses money… shipping quotes of $1,000 on orders our customers paid $500 for" — [YouTube](https://www.youtube.com/watch?v=zvVg61patS0)
  - The new freight partner initially: "They were terrible" — [YouTube](https://www.youtube.com/watch?v=i4UmTLUjk38)
  - "Competitors have already convinced factories to ban us" — [YouTube](https://www.youtube.com/watch?v=sq87s3r_RMo)
- Previous scepticism about Jack's opacity (2021) is in the earlier notes — [Boss Hunting](https://www.bosshunting.com.au/hustle/jack-bloomfield-interview)
- The news.com.au headline frames him as having "made himself a fortune" at 16. That is profile framing, not a verified figure — [news.com.au YouTube](https://www.youtube.com/watch?v=pxhtF275XOU)

### Inferences
- The business is only about 3.5 months past launch and order volume is small, so a review footprint on Reddit or ProductReview has probably not formed yet. Absence of criticism is not evidence of quality [INFERENCE].
- The "build in public" format lets Jack control the failure narrative. Every problem appears with its fix in the same episode. That is good marketing but not independent verification [INFERENCE].
- The "same factories that supply major retailers" claim is the type of comparative claim Williams-Sonoma attacked Quince over (section 6). In the EU this falls under the Unfair Commercial Practices Directive rules on misleading comparisons [INFERENCE].

### Gaps
- ProductReview.com.au, Google Business reviews (address in Wilston QLD), and r/AusRenovation or r/AusPropertyChat threads could not be accessed. They need a manual check.

---

## 6. Other factory-direct, transparent, premium home-goods models: Quince and lessons

### Takeaway
Quince is the scaled bedding analogue. It is "manufacturer-to-consumer", partner factories hold inventory and ship to the customer, it runs small test runs and reorders winners, and growth came largely from organic, creator-led comparison content. It also shows the **risks of "same quality as luxury brand X" marketing**: a November 2025 Williams-Sonoma lawsuit alleged invalid GOTS certificate numbers on a sheet set, mislabelled organic towels, unsubstantiated price comparisons and review manipulation. The suit was dismissed with leave to amend.

### Cited Findings
- Quince was founded in 2019 as "Last Brand" and rebranded in June 2020. Model: "goods are produced by partner factories and shipped directly to customers". It had about 800 employees and about US$1.1bn revenue (November 2025). Lawsuits: Williams-Sonoma (November 2025), Tapestry/Coach (April 2025), and Yeti and Deckers (design disputes) — [Wikipedia](https://en.wikipedia.org/wiki/Quince_(company))
- Sacra [secondary analysis; partly Quince's own claims]:
  - Quince "contracts directly with over 100 specialist factories across India, Italy, Turkey, Mongolia, Cambodia".
  - It "holds inventory at the factory until sold" and ships "directly from those factories to customers' doors".
  - It "bears full responsibility for quality control… returns, warranties", with a 365-day returns window and free shipping.
  - Revenue: about $221M (2023), $340M (2024, estimated), about $700M annualised (August 2025) and $2.0B annualised (February 2026).
  - Growth relied on "organic and earned media rather than paid social… influencer-driven haul content and TikTok comparison videos".

  — [Sacra](https://sacra.com/c/quince/)
- Another (low-authority) source says Quince works with "30-plus factories" and adjusts orders weekly. This conflicts with Sacra's 100+ — [michaelbeausoleil.com via search snippet](https://www.michaelbeausoleil.com/quince/); [Sacra](https://sacra.com/c/quince/)
- Small-batch testing: Quince uses "sophisticated data modeling" to test products in small batches, "quickly replenish winners, and drop the duds" — [Patchwork Brief](https://insights.getpatch.work/p/the-supply-chain-powering-quince)
- Origin story: Sid Gupta questioned why hotel-quality sheets felt better than home sheets despite not being "prohibitively expensive", and bedding became a key category — [search snippet: Business of Fashion / founder profiles](https://www.businessoffashion.com/people/sid-gupta/)
- Williams-Sonoma v. Quince (filed 21 November 2025, N.D. Cal.). Allegations:
  - Quince marketed towels as "GOTS-certified organic cotton", which Quince later called an "error".
  - "a GOTS certification number displayed on a Quince sheet set turned out to be invalid".
  - Experts doubted its long-staple organic cotton claims.
  - "Beyond Compare" charts allegedly lacked substantiation.
  - Quince allegedly hid low-star reviews and gave "reward points" for reviews.

  — [The Fashion Law](https://www.thefashionlaw.com/williams-sonoma-files-lawsuit-against-quince-accusing-brand-of-deceptive-dupe-tactics/). Judge Davila granted Quince's motion to dismiss for failure to plausibly plead, with leave to amend — [The Fashion Law](https://www.thefashionlaw.com/quince-beats-williams-sonoma-false-advertising-claims-over-product-comparisons/); [Law360](https://www.law360.com/consumerprotection/articles/2532414)

### Inferences
- Quince versus Bloom Build:
  - Quince **co-designs and commissions** production, with small test runs and factory-held finished goods. Bloom Build **resells existing factory catalogue stock**.
  - For premium bedding, the Quince approach (own specs, certified fibre, factory-held inventory) fits a "high quality" positioning better than picking from generic stock.
  - Bloom Build's "sell their stock" approach fits only commodity SKUs [INFERENCE].
- Lesson from the lawsuit: in bedding, certification claims (OEKO-TEX, GOTS, fibre origin, thread count) are where a factory-direct brand gets attacked. Verify every certificate number per batch in the public GOTS/OEKO-TEX databases before using it in marketing [INFERENCE].

### Gaps
- How Quince actually pays factories, its exact mix of US warehouses versus direct-from-factory shipping, and its bedding factory origins were not confirmed by a primary source.

---

## 7. Transferable playbook: premium bed linen in NL/EU (what to copy from Jack, what to change)

### Takeaway
Copy from Jack:
- in-person factory conversations with a local Mandarin-speaking operator
- cost-plus transparency
- a loss-leading sample (swatch) box
- QC at source per order
- weekly founder content
- proactive delivery honesty

Change three things for bedding:
1. **Speed.** Bedding is a light, comfort/impulse purchase. Dutch shoppers expect about 2–3 days and accept about 5 at most. So start with air/courier or a small EU buffer stock, and switch fast-moving SKUs to sea freight only once demand is proven.
2. **Specification instead of stock-picking.** Premium quality needs your own spec, lab tests and certificates, not generic factory stock.
3. **EU-compliant returns and claims.**

A pre-order or limited-drop format can still justify a 2–4 week wait for specific collections, provided the delivery date is explicit and the reward (price, exclusivity) is visible.

### Cited Findings
- [FOUNDER PREMISE] (coordinator, 4 Oct 2026): Jack ships tiles by sea because they are heavy and bulky, and tile buyers plan renovations weeks ahead. Bedding (duvet covers, duvets, pillows) is light, a comfort or impulse purchase, and planned less in advance. The bedding version therefore needs faster delivery from the start (air or a small EU buffer), with sea once proven.
- Bloom Build itself admits that speed costs sales even in tiles: "a customer email telling us our competitors beat us to the sale" [CLAIM] — [YouTube](https://www.youtube.com/watch?v=Q8z_gs8R76k)
- Delivery expectations (Sendcloud, 2021 survey of 7,873 consumers in 8 countries including NL): consumers expect standard delivery in 2–3 days on average; "Het maximum aantal dagen dat ze willen wachten is ongeveer vijf" ("the maximum number of days they are willing to wait is about five"); "Als de levertijd onbekend is of te langzaam, is de helft van de Europese consumenten geneigd de bestelling niet af te ronden" ("if the delivery time is unknown or too slow, half of European consumers tend not to complete the order") — [FashionUnited](https://fashionunited.nl/nieuws/business/rapport-sendcloud-dit-zijn-de-verwachtingen-omtrent-bezorging-van-europese-consumenten/2022072754256)
- Sendcloud E-commerce Delivery Compass 2025 (1,000 Dutch consumers):
  - 81% prefer a specific time slot over "as fast as possible"
  - willingness to pay about €4.47 shipping on a €50 order
  - 45.8% prefer flexible delivery options over free shipping
  - 24.2% won't reorder if tracking is inadequate

  — [Thuiswinkel.org](https://www.thuiswinkel.org/kennisbank/kennisartikelen/nederlandse-shopper-wil-grip-op-bezorging-dit-zijn-de-cijfers/)
- Same survey (June 2025):
  - 60.1% of Dutch shoppers had a delivery problem in the previous 3 months, and 25% received a package late
  - 35.6% abandon a store after delays, and 45.3% don't reorder after a failed delivery
  - over 73% expect immediate notification of delays

  — [Twinkle](https://twinklemagazine.nl/2025/06/helft-van-nederlandse-consumenten-keert-webshop-de-rug-toe-na-leveringsprob/index.xml)
- Jack's own logistics lesson: small consignments broke the economics (a $1,000 freight quote on a $500 order) until he negotiated a small-shipment price tier and waived handling fees [CLAIM] — [YouTube](https://www.youtube.com/watch?v=zvVg61patS0); [YouTube](https://www.youtube.com/watch?v=i4UmTLUjk38)
- The sample economics he accepts: $12 revenue against $20 cost per box, with 10% conversion to a full order [CLAIM] — [YouTube](https://www.youtube.com/watch?v=ExJe92ksibU); [YouTube](https://www.youtube.com/watch?v=60vXK94474w)

### Inferences: the playbook [all INFERENCE unless marked]

**A. Copy from Jack**
1. **The factory conversation as the core asset.** Visit Chinese textile clusters in person: Nantong/Haimen (home textiles), Keqiao/Shaoxing (fabrics), and Zhejiang/Anhui (down and feather) for duvets and pillows. Pitch a *direct-retail partnership*, not a one-off purchase order.

   Jack's deal structure is the one to copy: **an aggregate 12-month volume commitment in exchange for day-one pricing and per-order MOQ relief**.

   For premium linen, ask for:
   - fabric or greige held at the factory, with make-to-order cut-and-sew in small runs
   - per-colourway MOQs of tens rather than hundreds of sets
   - priority slots

   This supports Joost's thesis that it is "about the conversations".
2. **Hire a local Mandarin-speaking sourcing and QC lead early.** Jack's whole supplier network was built by one hire (Connie), and he nearly lost it when she left. Budget for two people, or a retainer plus one person, so relationships don't depend on one individual. Document every supplier contact and term in a shared system (his "12 suppliers into one system").
3. **QC at source per order, "trust but verify".** For bedding this is not enough on its own. Add:
   - pre-shipment inspection (AQL 2.5) on seams, size tolerance and shade per dye lot
   - **lab tests per fabric batch**: fibre composition, thread count verification, pilling, colourfastness, shrinkage
   - valid OEKO-TEX/GOTS certificates checked in the public databases (the Quince lesson)
   - for down and feather: fill power, down/feather ratio, and RDS
4. **Cost-plus transparency, with one consistent, auditable cost stack per product.** Jack's figures contradict each other ($9.69, <$10, $12, $25). Example structure: fabric, cut-and-sew, packaging, QC/lab, freight, duty (HS 6302 plus the €3 per-line fee for parcels ≤€150 until 2028), VAT, returns reserve, margin.
5. **The loss-leading sample box becomes a swatch kit.** Fabric swatches are cheap and light (letterbox format), so the economics are better than tile samples. The swatch kit also captures email and phone details for a follow-up sales call (his "first salesperson" step, triggered by 10% conversion).
6. **Weekly build-in-public content** filmed in the factories, with professional production once it works (Jack uses Exportfilms). Use a "Dutch founder in Nantong" angle. Pitch Dutch media around the price-gap story (e.g. RTL Z, AD, Consumentenbond-style "what do sheets really cost").
7. **Delivery honesty**: send the real date up front, notify proactively around Chinese New Year and Golden Week, and track every stage. This matches the Dutch finding that 73% expect immediate notification of delays.

**B. Change for bedding (incorporating the founder premise)**
1. **Speed tiers.** Dutch expectation is 2–3 days, with about 5 days as the ceiling.
   - **Launch:** hold a **small EU buffer stock** (e.g. an NL 3PL) of the 3–5 core SKUs in core sizes (140×200/220, 200×200/220, 240×220, pillowcases 60×70). These ship next-day and cover most impulse demand.
   - **Long tail** (colours, sizes, duvets): **air or courier B2C direct from China** (about 7–12 days), sold with an explicit "made for you / shipped from our atelier partner" date.
   - **Once demand is proven:** move fast movers to sea plus EU 3PL, which lowers the cost per unit.

   This is the reverse of Jack, who can be slow because tile buyers plan ahead.
2. **Pre-order and limited drops** fit premium bedding when:
   - it is a named seasonal collection (e.g. a "winter linen drop", limited colourway or numbered batch)
   - the price advantage over in-stock retail is shown explicitly (e.g. pre-order price vs regular price)
   - a fixed delivery date is shown at checkout, consistent with the Sendcloud data that *unknown* delivery time drives abandonment
   - there is a "notify me / reserve" deposit-free option.

   Keep 2–4 weeks as the ceiling. Never present pre-order as standard for core basics.
3. **Specification over stock.** Do not copy "sell the factory's existing stock". Generic Chinese bedding stock is a commodity, and in EU sizes it rarely exists as stock anyway. Copy Quince instead: your own spec (fibre, weave, GSM or thread count, finishing, EU sizes), small test runs, reorders of winners, and finished goods held at the factory or 3PL.
4. **Returns and claims.** The 14-day EU withdrawal right applies, so a Bloom Build-style "no change of mind" policy is impossible. Use an NL returns address. Copy the *idea* of Jack's conditional warranty: wash before use, follow the care label, and report visible defects before use or washing. Pair it with a quality guarantee, e.g. a 1–3 year seam and fabric warranty, because a long guarantee is a premium signal.
5. **Claims hygiene.** Avoid "same factory as [brand]" claims unless you can prove them. Comparison charts need named, current, like-for-like comparators (the Williams-Sonoma v. Quince allegations).

**C. Where Joost's premise needs nuance**
- "Mostly about the right conversations with factories": the factory deal was the *entry ticket*. Jack's first 3 months after launch were dominated by **small-order freight economics, sample operations, a 3PL and people**, and freight alone made every order loss-making for a period. For bedding, the speed tier (buffer stock vs air) and the certificate and testing discipline will matter as much as the factory conversation.
- "Not dropship but high quality": supported in Jack's positioning (first grade, QC every order). In tiles, however, "quality" means "same product as the showroom", whereas in premium bedding it must be *demonstrated* (lab data, certificates, hand feel through swatches).

### Gaps
- No NL-specific data found on acceptable delivery times for *bedding or home textiles* specifically, or on pre-order acceptance. The figures above are general e-commerce data (Sendcloud 2021, 2025).
- No public example found of an EU premium-bedding brand running a China factory-direct pre-order or drop model, so success rates cannot be cited.
- Air or courier cost per kg from China to NL for a duvet-cover set, and Chinese textile-cluster MOQ norms for EU sizes, were not researched in this pass.
