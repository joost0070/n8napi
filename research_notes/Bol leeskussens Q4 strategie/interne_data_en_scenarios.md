# Bline leeskussen on bol.com: internal sales, ads and rank data (Jun–Sep 2026) and Q4 unit-economics scenarios

Data pulled read-only on 2026-09-27 (GET only; advertiser bulk-report POSTs only). Sources are the bol Retailer API v10, the bol Advertiser API v11 bulk reports, and the Google Sheet `1dy1WZNtPqJkAfEpKZ-MLa-R26VYCGuCyovhbFdPavpw` (referred to below as "Sheet"). Weeks are ISO weeks 2026 (wk 26 = 22–28 Jun … wk 39 = 21–27 Sep; wk 39 data ends 26-09 for ads and 25-09 for shipments). "Pillow" = any of the five pillow EANs (white 8720892179074 + bundles beige/blue/grey/black); "cover" = the five loose-cover EANs. Money is EUR; tables are rounded to whole euros unless the value is a price point. Shipment records contain customer PII; nothing personal is reproduced here.

Source shorthand used below:
- [Shipments API](https://api.bol.com/retailer/shipments) = list `GET /retailer/shipments?page=N&fulfilment-method=FBR` (122 shipments, orders placed 2026-06-27 … 2026-09-25; FBB list empty) plus `GET /retailer/shipments/{id}` for every shipment (unitPrice, commission, EAN, country).
- [Campaign reports](https://api.bol.com/advertiser/reporting/bulk-reports) = CAMPAIGN_PERFORMANCE bulk reports for windows 2026-07-29..07-31, 08-01..08-25, 08-26..09-19, 09-20..09-26; SEARCH_TERM_PERFORMANCE for 08-01..08-25, 08-26..09-18, 09-19..09-26; SOV for 08-23..09-05, 09-06..09-19, 09-20..09-26; BIDDING 09-20..09-26; BS_CAMPAIGN_PERFORMANCE 09-01..09-26.
- [Sheet: Bol Ads Performance](https://docs.google.com/spreadsheets/d/1dy1WZNtPqJkAfEpKZ-MLa-R26VYCGuCyovhbFdPavpw) tab `📥 Bol Ads Performance` (daily campaign rows 2026-07-02 … 09-26), tab `📈 Bol Ranks` (daily rank snapshots 2026-07-03 … 09-25), tab `💰 Winstmotor Dagelijks` (daily P&L 2026-07-02 … 09-26), tab `🧪 Winsttest` (price-test plan), tab `📡 Radar Concurrenten` (weekly competitor prices 2026-07-20 … 09-21).
- [Offer insights API](https://api.bol.com/retailer/insights/offer) = `GET /retailer/insights/offer?offer-id=…&period=WEEK&number-of-periods=14&name=PRODUCT_VISITS` per offer (and BUY_BOX_PERCENTAGE for the white pillow).
- [Ratings API](https://api.bol.com/retailer/products/8720892179074/ratings), [Returns API](https://api.bol.com/retailer/returns), [Offer API](https://api.bol.com/retailer/offers/0ab6c304-f4a5-46c8-ac75-afe1384266ac), [Price-star API](https://api.bol.com/retailer/products/8720892179074/price-star-boundaries?condition=NEW), [Performance API](https://api.bol.com/retailer/insights/performance/indicator).

---

## Key question 1: Units sold per week (Jun–Sep 2026) by product and country, and average selling price per week

### Takeaway
65 pillows and 63 covers were shipped for orders placed 27-06 … 25-09 (July was the best month with 32 pillows = 1.03/day; August 20 = 0.65/day; 1–25 Sep 11 = 0.44/day). Belgium took 55% of pillow units. The average pillow price rose from 69.99–77 (Jun/early Jul) to 86–90 (Aug–mid Sep) and is 79.99 since the 19-09 price cut; the commission bol actually charged per shipment is 8.95 on 79.99 and 9.92 on 89.98 (11.0–11.2% of the consumer price), far below the 16.4% used in the internal model.

### Cited Findings
Weekly pillow units, country split and average selling price (order-placed date; wk 26 starts 22-06 but the API only holds shipments from 27-06):

| ISO wk | dates | pillows | NL/BE | white | beige | blue | grey | black | avg price incl VAT | avg white | avg bundle | covers (NL/BE) | cover revenue incl VAT |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 26 | 22-06–28-06 | 1 | 1/0 | 0 | 0 | 1 | 0 | 0 | 69.99 | – | 69.99 | 1 (1/0) | 100 |
| 27 | 29-06–05-07 | 3 | 2/1 | 1 | 0 | 2 | 0 | 0 | 69.99 | 69.98 | 69.99 | 0 | 0 |
| 28 | 06-07–12-07 | 7 | 6/1 | 1 | 3 | 1 | 2 | 0 | 77.12 | 69.98 | 78.31 | 2 (0/2) | 70 |
| 29 | 13-07–19-07 | 13 | 3/10 | 4 | 2 | 2 | 3 | 2 | 76.90 | 69.98 | 79.98 | 7 (6/1) | 335 |
| 30 | 20-07–26-07 | 10 | 5/5 | 2 | 1 | 2 | 1 | 4 | 80.18 | 69.98 | 82.73 | 9 (8/1) | 450 |
| 31 | 27-07–02-08 | 1 | 0/1 | 0 | 0 | 1 | 0 | 0 | 79.98 | – | 79.98 | 11 (10/1) | 517 |
| 32 | 03-08–09-08 | 6 | 2/4 | 0 | 4 | 1 | 1 | 0 | 86.65 | – | 86.65 | 8 (7/1) | 358 |
| 33 | 10-08–16-08 | 5 | 2/3 | 2 | 0 | 0 | 1 | 2 | 85.98 | 79.99 | 89.98 | 13 (7/6) | 611 |
| 34 | 17-08–23-08 | 2 | 0/2 | 0 | 1 | 1 | 0 | 0 | 89.98 | – | 89.98 | 5 (4/1) | 200 |
| 35 | 24-08–30-08 | 5 | 4/1 | 2 | 1 | 0 | 1 | 1 | 85.98 | 79.99 | 89.98 | 4 (3/1) | 280 |
| 36 | 31-08–06-09 | 1 | 1/0 | 0 | 1 | 0 | 0 | 0 | 89.98 | – | 89.98 | 1 (1/0) | 70 |
| 37 | 07-09–13-09 | 4 | 1/3 | 1 | 2 | 0 | 1 | 0 | 87.48 | 79.99 | 89.98 | 0 | 0 |
| 38 | 14-09–20-09 | 3 | 0/3 | 0 | 1 | 0 | 2 | 0 | 83.32 | – | 83.32 | 2 (2/0) | 140 |
| 39 | 21-09–25-09 | 4 | 2/2 | 0 | 3 | 0 | 1 | 0 | 79.99 | – | 79.99 | 0 | 0 |

— [Shipments API](https://api.bol.com/retailer/shipments) (all 122 shipment details, aggregated by `order.orderPlacedDateTime`).

- Monthly pillow totals: June (27–30 only) 2 (1 NL/1 BE, avg 69.99); July 32 (16 NL/16 BE, avg 77.54, revenue 2,481 incl VAT); August 20 (9 NL/11 BE, avg 86.48, revenue 1,730); 1–25 September 11 (3 NL/8 BE, avg 83.62, revenue 920). Covers: July 25 (revenue 1,180), August 34 (1,640), September 3 (210). — [Shipments API](https://api.bol.com/retailer/shipments)
- Country split over the whole window: pillows 29 NL / 36 BE (55% BE); covers 49 NL / 14 BE. — [Shipments API](https://api.bol.com/retailer/shipments)
- Colour mix Jun–Sep: white 13 (20%), beige 19, blue 11, grey 12, black 10. — [Shipments API](https://api.bol.com/retailer/shipments)
- Price history measured from shipments: white 69.98 on every sale up to 24-07, then 79.99 from 11-08 to 13-09, none sold since the cut to 69.99 on 19-09 (0 white units 19–25 Sep). Bundles 69.99 (late June), 79.98 (Jul; black briefly 82.98 on 21/24-07), 89.98 from 26-07 to 17-09, 79.99 from 20-09. — [Shipments API](https://api.bol.com/retailer/shipments); consistent with the price-history block in [Sheet: Winsttest](https://docs.google.com/spreadsheets/d/1dy1WZNtPqJkAfEpKZ-MLa-R26VYCGuCyovhbFdPavpw) ("wit los 69,98 tot 24-07, daarna 79,99 vanaf 13-08; bundels 69,99 in juni, 79,98/79,99 in juli, 89,98 vanaf eind juli").
- Commission per shipment item as reported by bol (field `commission`, available on all shipments from 26-07 onward; 50 earlier items have no commission field): 8.95 on 79.98/79.99 (11.2%), 9.24 on 82.98 (11.1%), 9.92 on 89.98 (11.0%). It fits commission = 1.18 + 9.71% × consumer price exactly for all three price points. — [Shipments API](https://api.bol.com/retailer/shipments)
- The internal model uses 16.4% of the price incl VAT ("gemeten uit echte zendingen: 14,65 bij 89,98 / 13,15 bij 79,99"), and the `💰 Winstmotor Dagelijks` tab booked 14.65 commission on the 01-09 sale at 89.98 but 9.92 on the 18-09 sale at 89.98 and 8.95 on the 24-09 sale at 79.99, i.e. the sheet switched from the 16.4% formula to the API value in mid-September. — [Sheet: Winsttest](https://docs.google.com/spreadsheets/d/1dy1WZNtPqJkAfEpKZ-MLa-R26VYCGuCyovhbFdPavpw); [Sheet: Winstmotor Dagelijks](https://docs.google.com/spreadsheets/d/1dy1WZNtPqJkAfEpKZ-MLa-R26VYCGuCyovhbFdPavpw)
- Current offers (27-09): white 69.99, stock 248, FBR with delivery code VVB; bundles all 79.99, stock beige 43 / blue 87 / grey 80 / black 80 (these equal the loose-cover stocks per colour, i.e. bundle availability is capped by covers, not pillows); loose covers 29.95–34.98, white cover stock 27; FBB inventory 0 for all cover EANs; buy-box share 100% NL and BE in weeks 34–39. — [Offer API](https://api.bol.com/retailer/offers/0ab6c304-f4a5-46c8-ac75-afe1384266ac); [Offer insights API](https://api.bol.com/retailer/insights/offer); [Inventory API](https://api.bol.com/retailer/inventory)
- Only one multi-unit pillow order in the window (2× black, 21-07). Nine shipments were cover-only orders. — [Shipments API](https://api.bol.com/retailer/shipments)

### Inferences
- The 55% BE share means blended shipping is 0.45×5.07 + 0.55×7.14 = 6.21 ex VAT per pillow, not the 74/26 NL/BE mix the Winsttest tab assumes (which gives 5.61).
- If the API `commission` field is the real charge (bol invoices commission ex VAT and the VAT is reclaimable), every pillow earns 3–5 euro more than the internal model says (see scenario table in Q6). This is the single largest correction to the internal unit economics and should be verified against a bol invoice/specification before relying on it.
- Cover sales collapsed from 34 (Aug) to 3 (Sep) in the same weeks that the "Bline-Hoezen-AUTO" campaign spend went from 22–31/week (wk 32–34) to under 1/week (wk 35+), see Q2. Covers are a second profit line (revenue 3,130 incl VAT Jun–Sep) that the pillow-only test plan ignores.

### Gaps
- Shipments before 27-06 are not returned by the API (rolling 3-month window), so June is incomplete; the Sheet claims 39 pillows in 22-06 … 05-08 at "normal" prices, which the API cannot verify for 22–26 June.
- No shipment `commission` values exist before 26-07, so the 69.98/69.99 commission is extrapolated (1.18 + 9.71% → 7.98 at 69.99).
- Whether the API `commission` is ex VAT and whether a separate fixed fee is invoiced was not verifiable via the API (no invoice/specification endpoint was queried).

---

## Key question 2: Ad spend, clicks, impressions, attributed conversions, ACoS, conversion rate per week; ad-attributed vs organic share

### Takeaway
Total ad spend 2 Jul–26 Sep was about 627 euro (519 on pillow campaigns) for 1,148 clicks and 43 attributed conversions; pillow campaigns attributed 32 conversions against 65 pillows shipped (≈49% ad-attributed, ≈51% organic). Since 1 Aug the pillow AUTO campaign runs at 3–6 euro/day, 0.26–0.68 CPC, 2–5% click-to-order conversion, and its ACoS swings 11–46% week to week on 1–3 conversions.

### Cited Findings
Weekly ads (all campaigns incl. covers/puzzle; "pillow camp." = Leeskussen AUTO/MANUAL/EXACT/BESTSELLERS/GENERIC campaigns). Weeks 27–30 from the Sheet (bulk reports older than ~60 days are refused), weeks 31–39 from bulk reports (the two agree to the cent where they overlap, e.g. wk 33 cost 32.14 both; wk 38 conversions differ: Sheet 0, report 3, because the Sheet snapshot pre-dates the 14-day attribution window). Pillow visits = sum of PRODUCT_VISITS of the five pillow offers.

| ISO wk | dates | pillows shipped | pillow visits | units/visits | ad cost all | ad cost pillow camp. | clicks all | impressions all | ad conv14d all | pillow-camp conv14d | ad-attributed share of pillows | ACoS all | pillow ads / pillow rev ex VAT |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 27 | 29-06–05-07 | 3 | 244 | 1.2% | 54 | 54 | 85 | 2,125 | 1 | 1 | 33% | 94% | 31% |
| 28 | 06-07–12-07 | 7 | 219 | 3.2% | 54 | 54 | 101 | 3,064 | 4 | 4 | 57% | 22% | 12% |
| 29 | 13-07–19-07 | 13 | 259 | 5.0% | 67 | 67 | 122 | 3,693 | 11 | 11 | 85% | 9% | 8% |
| 30 | 20-07–26-07 | 10 | 258 | 3.9% | 130 | 119 | 184 | 5,588 | 4 | 3 | 30% | 43% | 18% |
| 31 | 27-07–02-08 | 1 | 173 | 0.6% | 68 | 58 | 111 | 3,254 | 1 | 0 | 0% | 235% | 88% |
| 32 | 03-08–09-08 | 6 | 154 | 3.9% | 37 | 13 | 93 | 1,878 | 5 | 2 | 33% | 13% | 3% |
| 33 | 10-08–16-08 | 5 | 71 | 7.0% | 32 | 0 | 71 | 1,293 | 4 | 0 | 0% | 15% | 0% |
| 34 | 17-08–23-08 | 2 | 131 | 1.5% | 41 | 10 | 98 | 1,798 | 3 | 1 | 50% | 31% | 7% |
| 35 | 24-08–30-08 | 5 | 135 | 3.7% | 34 | 34 | 57 | 2,400 | 1 | 1 | 20% | 46% | 9% |
| 36 | 31-08–06-09 | 1 | 117 | 0.9% | 23 | 23 | 50 | 1,330 | 1 | 1 | 100% | 31% | 31% |
| 37 | 07-09–13-09 | 4 | 146 | 2.7% | 24 | 24 | 60 | 1,548 | 3 | 3 | 75% | 11% | 8% |
| 38 | 14-09–20-09 | 3 | 239 | 1.3% | 30 | 30 | 56 | 1,697 | 3 | 3 | 100% | 14% | 14% |
| 39 | 21-09–26-09 | 4 | 166 | 2.4% | 32 | 32 | 60 | 1,740 | 2 | 2 | 50% | 24% | 12% |

— [Sheet: Bol Ads Performance](https://docs.google.com/spreadsheets/d/1dy1WZNtPqJkAfEpKZ-MLa-R26VYCGuCyovhbFdPavpw) (wk 27–30), [Campaign reports](https://api.bol.com/advertiser/reporting/bulk-reports) (wk 31–39), [Shipments API](https://api.bol.com/retailer/shipments), [Offer insights API](https://api.bol.com/retailer/insights/offer).

- Totals 2 Jul–26 Sep: ad cost 627 (pillow campaigns 519), clicks 1,148, attributed conversions 43 (pillow campaigns 32), pillows shipped 65, pillow revenue ex VAT 4,356. Pillow-campaign spend / pillow revenue ex VAT = 11.9% overall. — [Sheet: Bol Ads Performance](https://docs.google.com/spreadsheets/d/1dy1WZNtPqJkAfEpKZ-MLa-R26VYCGuCyovhbFdPavpw); [Campaign reports](https://api.bol.com/advertiser/reporting/bulk-reports)
- 1 Aug–26 Sep (bulk-report window): cost 321 (pillow campaigns 225), 656 clicks (437 on pillow campaigns), 23 attributed conversions (13 on pillow campaigns) with attributed sales 1,356 (925 pillow), ACoS all 23.7%, pillow ACoS 24.3%; 30 pillows shipped 1 Aug–25 Sep, so 13/30 = 43% ad-attributed. — [Campaign reports](https://api.bol.com/advertiser/reporting/bulk-reports); [Shipments API](https://api.bol.com/retailer/shipments)
- Pillow AUTO campaign (1000000001919694) daily cost since 1 Aug: 0.7–5.8/day through 18-09, then 7.23 (19-09), 9.32 (20-09), 14.23 (21-09), 1.52 (22-09, campaign paused during the day per the Sheet), 6.04, 5.46, 0.26, 4.74 (23–26 Sep). CPC 0.26–0.68. Conversions since 1 Aug on this campaign: 06-08, 07-08, 21-08, 24-08, 31-08, 11-09 (1 each), 13-09 (2), 17-09 (2), 20-09 (1), 23-09 (2). — [Campaign reports](https://api.bol.com/advertiser/reporting/bulk-reports)
- July was carried by the same AUTO campaign at 8–19/day in the first three weeks (2–20 Jul: 1 conversion on 05-07, 2 on 06-07, 1 on 09-07, 1 on 11-07, 1 on 13-07, 6 on 16-07 with 388 sales, 3 on 17-07, 1 on 19-07, 1 on 21-07), then throttled to 0–3/day from 22-07. — [Sheet: Bol Ads Performance](https://docs.google.com/spreadsheets/d/1dy1WZNtPqJkAfEpKZ-MLa-R26VYCGuCyovhbFdPavpw)
- Other pillow campaigns in the window: EXACT campaign (1000000002023131) spent 24 on 19 Aug–2 Sep with 0 conversions (CPC 0.66–1.35); MANUAL campaign 1.5 with 0 conversions; BESTSELLERS/GENERIC campaigns spent ~33 on 29–31 Jul with 0 conversions and nothing after 1 Aug. Cover campaign (Hoezen AUTO): 22.41 (wk 32), 31.07 (wk 33), 31.15 (wk 34) with 1–2 conversions/week, then ≤0.24/week from wk 35. — [Campaign reports](https://api.bol.com/advertiser/reporting/bulk-reports); [Sheet: Bol Ads Performance](https://docs.google.com/spreadsheets/d/1dy1WZNtPqJkAfEpKZ-MLa-R26VYCGuCyovhbFdPavpw)
- Branded Shelves "Test brand shelve" 1–26 Sep: 1,212 served / 568 viewable impressions, 8 clicks, cost 3.39, 0 post-click conversions, 1 post-view conversion (13-09). — [Campaign reports](https://api.bol.com/advertiser/reporting/bulk-reports) (BS_CAMPAIGN_PERFORMANCE)
- Bidding report 20–26 Sep (AUTO campaign): win rate 93–99% on days it ran fully (59–65% on 22-09), impression share SEARCH 3.4–14.6%, CATEGORY 1.0–6.2%, PRODUCT 1.0–4.9%; average winning bid SEARCH 0.72–0.94, CATEGORY 0.56–1.01, PRODUCT 0.43–0.48; auctions participated per day SEARCH 113–256, CATEGORY 204–837, PRODUCT 761–4,118. — [Campaign reports](https://api.bol.com/advertiser/reporting/bulk-reports) (BIDDING)
- Search terms 1 Aug–26 Sep (AUTO+EXACT): "leeskussen" 1,645 impressions, 51 clicks, cost 46.03, 2 conversions; "rugkussen bed" 472 imp, 13 clicks, 8.42, 1 conversion; "rugsteun bed" 314 imp, 15 clicks, 8.70, 0; "leeskussen bed" 126 imp, 6 clicks, 6.82, 0; "bookseat" 221 imp, 2 clicks, 1.05, 0; "bline leeskussen" 0.80, 1 conversion. Only 4 search terms converted in 8 weeks. — [Campaign reports](https://api.bol.com/advertiser/reporting/bulk-reports) (SEARCH_TERM_PERFORMANCE)
- Campaign settings: the AUTO campaign configuration snapshot in the local config shows dailyBudget 15 and acosTargetPercentage 15, target NL+BE, all channels, start 2026-06-09; the Winsttest tab says budget 15 from 19-09, 8 from 22-09, ACoS target 20 (19–23 Sep) then 15 (from 24-09); the brief for this research says budget 10. — [Sheet: Winsttest](https://docs.google.com/spreadsheets/d/1dy1WZNtPqJkAfEpKZ-MLa-R26VYCGuCyovhbFdPavpw); local `auto_campaign.json`
- The BE campaign 1000000002095476 started 27-09 and has no rows in any report (reports end 26-09). — [Campaign reports](https://api.bol.com/advertiser/reporting/bulk-reports)

### Inferences
- Click-to-order conversion of the AUTO campaign (2–5% in most weeks, 0% in wk 31/33) is in line with the product-page conversion (units/visits 1–5%); ads are not converting worse than organic traffic, they simply buy few clicks (50–60/week since wk 35).
- Weeks with ≥4 pillows shipped (28, 29, 30, 32, 33, 35, 37, 39) all had either ≥250 pillow visits or ≥5 attributed conversions; the two zero/one-unit weeks with normal traffic (31, 36) coincide with the price step-ups (79.98→89.98 on 26-07; the 4–8 day delivery promise from 1 Sep).
- Attributed share of ~45–50% means roughly half of pillow sales would need to be replaced by organic demand if ads were switched off; the organic half is concentrated in weeks where organic rank on "leeskussen" was ≤10 (see Q3).

### Gaps
- July ad spend for campaigns other than the AUTO campaign (BESTSELLERS, GENERIC, MANUAL) is only in the Sheet for 20–31 Jul; bulk reports for dates before 29-07 are refused (older than ~60 days), so weeks 27–29 spend is a lower bound.
- June ads (campaign start 09-06) are not in the Sheet (starts 02-07) and not retrievable via reports.
- Attribution is bol's 14-day post-click model; no order-level match between ad conversions and shipments is possible, so "ad-attributed share" compares counts, not the same orders.

---

## Key question 3: Organic rank on key terms, product visits per week, the September stock-out and the 19-09 price cut

### Takeaway
Organic rank data exist only as sparse snapshots: on "leeskussen" (NL) the beige bundle sat at 5–12 in July, slipped to 15–22 in mid/late August and 22–27 in September; the white pillow showed 6–8 on 19-08 and 26-08 and has not appeared in any rank snapshot since. Pillow product visits fell from ~250/week (Jul) to 71–146/week (mid-Aug to mid-Sep), then spiked to 239 in the price-cut week (14–20 Sep, 22 white-pillow visits on 19-09 alone) without a matching rise in orders (3 that week, 4 the next). The stock-out (delivery promise 4–8 days from 1 Sep) shows up as 10 consecutive days without a pillow order (1–10 Sep) at otherwise normal traffic.

### Cited Findings
- Rank snapshots come from the `📈 Bol Ranks` tab (bol product-ranks API, `type` SEARCH, organic flag `gesponsord=NEE`); the API only returns a term on days the product had ≥6 impressions on it, so most (term, day) cells are empty. Direct calls to `GET /retailer/insights/product-ranks?ean=8720892179074&type=SEARCH` for 29-08, 05-09, 12-09, 20-09 and 26-09 returned empty `ranks` arrays for the white pillow. — [Sheet: Bol Ranks](https://docs.google.com/spreadsheets/d/1dy1WZNtPqJkAfEpKZ-MLa-R26VYCGuCyovhbFdPavpw); [Product ranks API](https://api.bol.com/retailer/insights/product-ranks)
- Organic rank on "leeskussen" (NL unless stated), beige bundle: 05-07 8; 07-07 10; 08-07 8; 09-07 5; 12-07 12; 13-07 8; 16-07 5; 19-07 8; 20-07 8; 04-08 10; 06-08 10; 07-08 16 (BE 20); 09-08 8; 10-08 8; 12-08 8; 13-08 18; 15-08 15; 17-08 16/17; 18-08 18; 21-08 22; 22-08 20; 23-08 20; 24-08 21; 06-09 25; 08-09 25/26; 09-09 24; 10-09 27; 14-09 22; 15-09 16 (BE 11); 22-09 27; 24-09 18. White pillow: 07-08 25 (NL and BE); 19-08 8; 22-08 19; 26-08 6. Blue: 24-07 23, 26-07 25, 12-08 25, 15-08 30. Grey: 13-07 46, 19-09 21. — [Sheet: Bol Ranks](https://docs.google.com/spreadsheets/d/1dy1WZNtPqJkAfEpKZ-MLa-R26VYCGuCyovhbFdPavpw)
- Organic rank on "bookseat" (beige, NL): 07-07 8; 09-08 10; 15-08 8; 17-08 8 (blue 16); 30-08 16; blue 03-09 22. "rugkussen bed" (beige): 14-07 7; 20-08 16. "leeskussen bed": 16 rows, all sponsored positions except none organic in the tab; "rugsteun bed": 28 rows, all sponsored. — [Sheet: Bol Ranks](https://docs.google.com/spreadsheets/d/1dy1WZNtPqJkAfEpKZ-MLa-R26VYCGuCyovhbFdPavpw)
- Sponsored positions on "leeskussen" (beige/blue) were 2 on most July days (03-07 … 31-07), then 8–14 in late Aug/Sep and 100–105 on 23-09 and 25-09. — [Sheet: Bol Ranks](https://docs.google.com/spreadsheets/d/1dy1WZNtPqJkAfEpKZ-MLa-R26VYCGuCyovhbFdPavpw)
- Pillow product visits per week (sum of 5 pillow offers; white in brackets): wk 26 156 (10); 27 244 (19); 28 219 (22); 29 259 (33); 30 258 (53); 31 173 (37); 32 154 (18); 33 71 (18); 34 131 (28); 35 135 (20); 36 117 (15); 37 146 (17); 38 239 (51); 39 166 (22). Beige is the most visited offer every week (33–135). Cover visits: 26/week (wk 30) → 52/73/85 (wk 32–34) → 2–13/week after. — [Offer insights API](https://api.bol.com/retailer/insights/offer)
- White-pillow visits per day around the price cut: 14-09 3, 15-09 5, 16-09 5, 17-09 6, 18-09 2, 19-09 22 (NL 12/BE 10), 20-09 8, 21-09 5, 22-09 4, 23-09 6, 24-09 3, 25-09 2, 26-09 2. — [Offer insights API](https://api.bol.com/retailer/insights/offer) (period=DAY)
- Stock-out period: the Winsttest tab records "gerealiseerd 01-09 t/m 17-09: 5 kussens; voorraad was op, levertijd stond op 4-8 dagen" and, for blocks A/B, "voorraad raakte op en levertijd stond op 4-8 dagen (22-07 t/m 18-09)". — [Sheet: Winsttest](https://docs.google.com/spreadsheets/d/1dy1WZNtPqJkAfEpKZ-MLa-R26VYCGuCyovhbFdPavpw)
- Pillow orders by day in September: none 1–10 Sep; 11-09 2; 13-09 2; 17-09 1; 20-09 2; 23-09 2; 25-09 2 (0 on 19, 21, 22, 24). So 0 pillows 1–8 Sep, 5 pillows 9–18 Sep, 6 pillows 19–25 Sep (0.86/day) vs 0.65/day in August. — [Shipments API](https://api.bol.com/retailer/shipments)
- During the zero-order stretch 1–10 Sep the AUTO campaign still had 80–308 impressions and 3–13 clicks per day (cost 1.4–5.0/day) and pillow visits were 117 (wk 36), i.e. traffic continued. — [Campaign reports](https://api.bol.com/advertiser/reporting/bulk-reports); [Offer insights API](https://api.bol.com/retailer/insights/offer)
- The Winsttest tab's interim reading of phase 1 (23-09): "tempo 0,50/dag, TACOS 25%", 2 sales / 128 revenue ex VAT / 32.30 ads through 22-09. — [Sheet: Winsttest](https://docs.google.com/spreadsheets/d/1dy1WZNtPqJkAfEpKZ-MLa-R26VYCGuCyovhbFdPavpw)
- Search demand seen by the ads (searchVolume in SEARCH_TERM_PERFORMANCE, summed over the days our ads showed): "leeskussen" 557 (wk 32), 439, 661, 616, 437, 505, 456, 386 (wk 39, 6 days); "rugkussen bed" 68, –, 136, 279, 141, 171, 153, 79; "bookseat" 38–64/week; "leeskussen bed" 14–37/week; "rugsteun bed" 27–121/week. All terms summed: 1,123 (wk 32), 1,168, 1,286, 1,369, 871, 834, 1,281, 981. — [Campaign reports](https://api.bol.com/advertiser/reporting/bulk-reports) (SEARCH_TERM_PERFORMANCE)

### Inferences
- The organic slide on "leeskussen" (beige from ~8 to ~20+) starts in the week of 13–18 Aug, two to three weeks after the bundle price went from 79.98 to 89.98 (26-07) and while weekly units fell from 10–13 to 2–6; it precedes the September stock-out, so the stock-out did not cause the rank loss but the price step-up plus lower sales velocity plausibly did.
- The stock-out cost is visible as conversion, not traffic: about 10 days of zero orders at ~17 visits/day and ~7 ad clicks/day. At the August run rate (0.65/day) that is ~6–7 lost pillows (~150 euro contribution at the 89.98 price using the model commission), plus ~25 euro of ad spend that bought nothing.
- The 19-09 price cut produced a one-day visit spike (22 white visits on 19-09, likely bol's "price drop" surfacing) but no white-pillow sales at 69.99 in the first seven days; bundle sales (6 in 19–25 Sep) recovered to slightly above the August pace. It is too early (7 days, 6 units) to read elasticity.
- Search demand for "leeskussen" as seen by the ads was flat-to-down from mid-August to late September (661 → 386), so the Sheet's expectation of a Q4 uplift ("november 1,7 keer het zoekvolume van augustus") is not yet visible in the data through 26-09.

### Gaps
- No continuous daily organic-rank series exists for any term; the product-ranks API returns nothing for the white pillow on the five dates tested, so white-pillow rank since 26-08 is unknown.
- No rank data at all for "leeskussen bed" and "rugsteun bed" organic positions (all captured rows for those terms are sponsored).
- The exact dates on which stock hit zero and on which the delivery promise changed to 4–8 days are not in any API field; only the Sheet's narrative (1 Sep–17/18 Sep) and the zero-order stretch (1–10 Sep) are available.
- searchVolume in the search-term report only counts days on which the campaign served on that term; it is a lower bound of market search volume, not a market total.

---

## Key question 4: Share of voice (SOV) on SEARCH / CATEGORY / PRODUCT pages, NL and BE, last weeks

### Takeaway
In the week 20–26 Sep Bline's sponsored impression share on the "Leeskussen" chunk averaged 14.7% (NL) and 17.7% (BE) on search pages, 8–9% on product pages and 9% (NL) / 18% (BE) on category pages; NL search share had dropped to 6.6–8.2% in weeks 36–37 (stock-out, budget throttled) and recovered after 19-09.

### Cited Findings
Weekly average impression share (click share in brackets), Leeskussen chunk, all channels pooled per day-row (SOV report rows are per country × page × channel × day; wk 34 has only 23–24 Aug):

| ISO wk | NL SEARCH | NL CATEGORY | NL PRODUCT | BE SEARCH | BE CATEGORY | BE PRODUCT |
|---|---|---|---|---|---|---|
| 35 (24–30 Aug) | 23.6% (12.4%) | 8.8% (0%) | 9.2% (6.1%) | 17.7% (8.5%) | 11.6% (2.1%) | 8.9% (1.6%) |
| 36 (31 Aug–6 Sep) | 8.2% (9.7%) | 0.4% (0%) | 8.4% (8.8%) | 13.3% (7.8%) | 0.2% (0%) | 8.4% (8.4%) |
| 37 (7–13 Sep) | 6.6% (7.7%) | 0.7% (0%) | 10.9% (7.8%) | 12.0% (6.1%) | 1.7% (1.2%) | 11.0% (9.0%) |
| 38 (14–20 Sep) | 13.7% (12.7%) | 4.3% (0.7%) | 8.5% (5.2%) | 14.3% (17.0%) | 9.5% (10.1%) | 10.0% (6.2%) |
| 39 (21–26 Sep) | 14.7% (11.4%) | 8.7% (6.8%) | 8.3% (4.9%) | 17.7% (13.0%) | 18.1% (5.3%) | 10.7% (13.2%) |

— [Campaign reports](https://api.bol.com/advertiser/reporting/bulk-reports) (SOV, three windows 23-08 … 26-09; 598 Leeskussen rows, plus 227 Kussensloop and 29 Puzzelmat rows not used).

- 20–26 Sep by channel, NL SEARCH: APP 17.8% (click share 13.7%), MOBILE 15.0% (10.7%), DESKTOP 11.6% (10.5%), TABLET 42.6% (4 days). BE SEARCH: DESKTOP 23.5%, APP 19.7% (click share 32.1%), MOBILE 12.2% (33.3%). — [Campaign reports](https://api.bol.com/advertiser/reporting/bulk-reports) (SOV 20-09..26-09)
- Daily NL SEARCH impression share 20–26 Sep (APP/DESKTOP/MOBILE): 20-09 26/23/23%; 21-09 25/14/4%; 22-09 2/3/2% (campaign paused part of the day); 23-09 30/27/30%; 24-09 14/8/18%; 25-09 13/3/17%; 26-09 14/3/11%. — [Campaign reports](https://api.bol.com/advertiser/reporting/bulk-reports) (SOV 20-09..26-09)
- The SOV report reports only Bline's own share (brand = Bline in all 854 rows); competitor shares are not exposed. — [Campaign reports](https://api.bol.com/advertiser/reporting/bulk-reports)
- Competitor prices tracked weekly (Radar tab, category leeskussen): Ten Cate Leeskussen (Bookseat) 59.95 (20-07 … 24-08) → 69.95 (31-08, 07-09) → 54.99 (14-09) → 57.99 (21-09), 3 reviews (5.0) unchanged; Ten Cate variant 89.95 throughout, reviews 16 → 18 (4.61); Ducky Dons 79.00 throughout, 5 reviews (4.8). — [Sheet: Radar Concurrenten](https://docs.google.com/spreadsheets/d/1dy1WZNtPqJkAfEpKZ-MLa-R26VYCGuCyovhbFdPavpw)

### Inferences
- Search-page SOV tracks the daily budget almost one-to-one (share collapses on 22-09 when the campaign paused and in weeks 36–37 when spend was ~3/day); with a 15% impression share and ~93–99% auction win rate, the campaign is budget-limited, not bid-limited (see bidding data in Q2).
- Category-page share is negligible (<1%) whenever budget is tight, which is where the 2 on "leeskussen" sponsored slots in July came from; those slots have not been bought since late August.

### Gaps
- No SOV data before 23-08 (older report windows are refused), so July share of voice cannot be compared.
- Competitor SOV is not available from the API; only own share.

---

## Key question 5: Reviews (count and rating per EAN now) and service KPIs

### Takeaway
All five pillow EANs share one review pool: 13 ratings (9×5, 3×4, 0×3, 1×2, 0×1; average 4.54); none of the five cover EANs has a rating. Bol's service indicators show one cancellation in week 37 (1 of 5 orders, above the 2% norm) and one return in week 36 (1 of 2, above the 11.1% norm); track-and-trace compliance 100%.

### Cited Findings
- Ratings on 27-09 for EANs 8720892179074 / 8720892687241 / 8720892687258 / 8720892687265 / 8720892687272 (identical response for each): rating 5 → 9, rating 4 → 3, rating 3 → 0, rating 2 → 1, rating 1 → 0 (13 total, mean 4.54). Cover EANs 8720892179098 / 8720892687203 / 8720892687210 / 8720892687227 / 8720892687234: 0 ratings. — [Ratings API](https://api.bol.com/retailer/products/8720892179074/ratings)
- The Sheet counted "13 op de familie" on 14-09, so no new rating arrived between 14-09 and 27-09. — [Sheet: Winsttest](https://docs.google.com/spreadsheets/d/1dy1WZNtPqJkAfEpKZ-MLa-R26VYCGuCyovhbFdPavpw)
- Returns registered 22-06 … 26-09 on pillow EANs: 22-06 beige ("kwaliteit valt tegen"), 10-07 blue ("kwaliteit valt tegen"), 15-07 blue ("kwaliteit valt tegen"), 05/06-08 beige + black (two failed-to-collect cancellations, then accepted on 26-08 "geen reden"), 21-09 beige (open, "verkeerd besteld / onduidelijke productinformatie"), 26-09 white (open, "ik heb me bedacht"). That is 7 distinct pillow returns against 65 pillows shipped (≈11%). Cover returns in the window: 17-07 black ("dubbel besteld"), 31-07 grey ("toch niet nodig"), 20-08 black, 28-08 grey (expired), 11-09 grey ("onduidelijke productinformatie"). — [Returns API](https://api.bol.com/retailer/returns)
- Performance indicators: week 36 RETURNS 1/2 = 50% (norm ≤11.1%, non-conforming), CANCELLATIONS 0/2; week 37 CANCELLATIONS 1/5 = 20% (norm ≤2%, non-conforming), RETURNS 0/5; weeks 38 and 39 CANCELLATIONS 0/5, RETURNS 0/5; TRACK_AND_TRACE 100% in weeks 36–39; REVIEWS indicator returns no score (norm ≥8). — [Performance API](https://api.bol.com/retailer/insights/performance/indicator)
- Price-star boundaries (condition NEW) on 27-09: for the white pillow level 5 up to 96.97, level 4 up to 97.00, level 3 up to 102, level 2 up to 107; the four bundles level 5 up to 96.97, levels 3–4 up to 100. Current prices (69.99 / 79.99) are far below the 5-star boundary. — [Price-star API](https://api.bol.com/retailer/products/8720892179074/price-star-boundaries?condition=NEW)

### Inferences
- The observed pillow return rate (~11% of units, 3 of 7 for "quality disappoints") is below the 17% return provision in the model; keeping 17% is conservative by roughly 1 euro per pillow.
- Every price point in the scenario table keeps 5 price stars, so price stars are not a lever between 59.99 and 96.97.

### Gaps
- The ratings endpoint gives counts only; review texts, dates and the per-colour split are not available via the API.
- The week-37 cancellation (1 of 5) cannot be tied to an order via the API.

---

## Key question 6: Scenario table for Q4 — contribution per pillow before ads, break-even ad cost per sale, TACOS at break-even, profit per day at 1/2/3/5 sales per day and 16/30/50 euro ad spend per day

### Takeaway
With the brief's cost base (landed 14.00 pillow / 19.27 bundle, commission 16.4%, blended shipping at the actual 45/55 NL/BE mix, pick & pack 2.15, 17% return provision, storage 4.90/day fixed), a white pillow contributes 15 euro at 59.99, 18 at 64.99, 21 at 69.99, 25 at 74.98 and 28 at 79.99 before ads; a bundle contributes 9 / 12 / 15 / 19 / 22 at the same prices. Break-even ad spend per sale equals that contribution (TACOS 30–42% for white, 17–33% for bundles). Using the commission bol actually charged in shipments (1.18 + 9.71%) adds 3–4 euro per unit. At the historical best pace (1/day) the line only covers storage and 16 euro/day of ads at ≥69.99 white; 2/day is needed for 30 euro/day of ads to pay off; 3/day carries 50 euro/day at every price ≥69.99 (white) or ≥74.98 (bundle).

### Cited Findings
Cost inputs (from the brief, verified where possible): landed cost batch 2 = 14.00 per pillow (Sheet: 5,096.12 goods + 959.79 freight/duties for 252 units = 14.00, bank-verified 22-09), bundle 19.27; shipping NL 5.07 / BE 7.14 ex VAT; pick & pack 2.15; return provision 17% × (landed × 0.86 + 4.00) = 2.73 (pillow) / 3.50 (bundle); storage 4.90/day for the whole line; VAT 21% inside the consumer price; NL/BE mix 45/55 from shipments (blended shipping 6.21). — [Sheet: Winsttest](https://docs.google.com/spreadsheets/d/1dy1WZNtPqJkAfEpKZ-MLa-R26VYCGuCyovhbFdPavpw) (KOSTPRIJS BATCH 2 block); [Shipments API](https://api.bol.com/retailer/shipments)

Contribution per unit before ads (= break-even ad cost per sale), model commission 16.4% of consumer price:

| price incl VAT | net ex VAT | commission 16.4% | white: NL | white: BE | white: blended | white: TACOS at break-even | bundle: NL | bundle: BE | bundle: blended | bundle: TACOS at break-even |
|---|---|---|---|---|---|---|---|---|---|---|
| 59.99 | 50 | 10 | 16 | 14 | 15 (14.65) | 30% | 10 | 8 | 9 (8.61) | 17% |
| 64.99 | 54 | 11 | 19 | 17 | 18 (17.97) | 33% | 13 | 11 | 12 (11.93) | 22% |
| 69.99 | 58 | 11 | 22 | 20 | 21 (21.28) | 37% | 16 | 14 | 15 (15.24) | 26% |
| 74.98 | 62 | 12 | 26 | 24 | 25 (24.58) | 40% | 20 | 18 | 19 (18.54) | 30% |
| 79.99 | 66 | 13 | 29 | 27 | 28 (27.90) | 42% | 23 | 21 | 22 (21.86) | 33% |

Same, with the commission as charged on real shipments (1.18 + 9.71% of consumer price; extrapolated below 79.98):

| price incl VAT | measured commission | white blended contribution | TACOS at break-even | bundle blended contribution | TACOS at break-even |
|---|---|---|---|---|---|
| 59.99 | 7 (7.01) | 17 (17.49) | 35% | 11 (11.45) | 23% |
| 64.99 | 7 (7.49) | 21 (21.13) | 39% | 15 (15.09) | 28% |
| 69.99 | 8 (7.98) | 25 (24.78) | 43% | 19 (18.74) | 32% |
| 74.98 | 8 (8.46) | 28 (28.42) | 46% | 22 (22.38) | 36% |
| 79.99 | 9 (8.95) | 32 (32.08) | 49% | 26 (26.03) | 39% |

— computed from the inputs above and [Shipments API](https://api.bol.com/retailer/shipments) commission values. TACOS = break-even ad cost / revenue ex VAT (the definition the Sheet uses: ads ÷ omzet_ex).

Profit per day = units × blended contribution − ad spend − 4.90 storage (model commission 16.4%). Cells show ad spend 16 / 30 / 50 euro per day:

| price, product | contribution | 1 sale/day | 2 sales/day | 3 sales/day | 5 sales/day |
|---|---|---|---|---|---|
| 59.99 white | 15 | −6 / −20 / −40 | 8 / −6 / −26 | 23 / 9 / −11 | 52 / 38 / 18 |
| 64.99 white | 18 | −3 / −17 / −37 | 15 / 1 / −19 | 33 / 19 / −1 | 69 / 55 / 35 |
| 69.99 white | 21 | 0 / −14 / −34 | 22 / 8 / −12 | 43 / 29 / 9 | 85 / 71 / 51 |
| 74.98 white | 25 | 4 / −10 / −30 | 28 / 14 / −6 | 53 / 39 / 19 | 102 / 88 / 68 |
| 79.99 white | 28 | 7 / −7 / −27 | 35 / 21 / 1 | 63 / 49 / 29 | 119 / 105 / 85 |
| 59.99 bundle | 9 | −12 / −26 / −46 | −4 / −18 / −38 | 5 / −9 / −29 | 22 / 8 / −12 |
| 64.99 bundle | 12 | −9 / −23 / −43 | 3 / −11 / −31 | 15 / 1 / −19 | 39 / 25 / 5 |
| 69.99 bundle | 15 | −6 / −20 / −40 | 10 / −4 / −24 | 25 / 11 / −9 | 55 / 41 / 21 |
| 74.98 bundle | 19 | −2 / −16 / −36 | 16 / 2 / −18 | 35 / 21 / 1 | 72 / 58 / 38 |
| 79.99 bundle | 22 | 1 / −13 / −33 | 23 / 9 / −11 | 45 / 31 / 11 | 88 / 74 / 54 |

Same matrix with the measured commission:

| price, product | contribution | 1 sale/day | 2 sales/day | 3 sales/day | 5 sales/day |
|---|---|---|---|---|---|
| 59.99 white | 17 | −3 / −17 / −37 | 14 / 0 / −20 | 32 / 18 / −2 | 67 / 53 / 33 |
| 64.99 white | 21 | 0 / −14 / −34 | 21 / 7 / −13 | 43 / 29 / 9 | 85 / 71 / 51 |
| 69.99 white | 25 | 4 / −10 / −30 | 29 / 15 / −5 | 53 / 39 / 19 | 103 / 89 / 69 |
| 74.98 white | 28 | 8 / −6 / −26 | 36 / 22 / 2 | 64 / 50 / 30 | 121 / 107 / 87 |
| 79.99 white | 32 | 11 / −3 / −23 | 43 / 29 / 9 | 75 / 61 / 41 | 139 / 125 / 105 |
| 59.99 bundle | 11 | −9 / −23 / −43 | 2 / −12 / −32 | 13 / −1 / −21 | 36 / 22 / 2 |
| 64.99 bundle | 15 | −6 / −20 / −40 | 9 / −5 / −25 | 24 / 10 / −10 | 55 / 41 / 21 |
| 69.99 bundle | 19 | −2 / −16 / −36 | 17 / 3 / −17 | 35 / 21 / 1 | 73 / 59 / 39 |
| 74.98 bundle | 22 | 1 / −13 / −33 | 24 / 10 / −10 | 46 / 32 / 12 | 91 / 77 / 57 |
| 79.99 bundle | 26 | 5 / −9 / −29 | 31 / 17 / −3 | 57 / 43 / 23 | 109 / 95 / 75 |

- Realised mix for weighting: 20% white / 80% bundles over Jun–Sep (13 of 65 pillows). At the current pairing (white 69.99 / bundle 79.99) the mix-weighted contribution is 0.2×21.28 + 0.8×21.86 = 21.7 (model commission) or 0.2×24.78 + 0.8×26.03 = 25.8 (measured). — [Shipments API](https://api.bol.com/retailer/shipments)
- Historical ad cost per attributed pillow conversion: 519 / 32 = 16.2 euro (2 Jul–26 Sep), 225 / 13 = 17.3 euro (1 Aug–26 Sep); per pillow shipped (all pillows, organic included) 519 / 65 = 8.0 euro. — [Sheet: Bol Ads Performance](https://docs.google.com/spreadsheets/d/1dy1WZNtPqJkAfEpKZ-MLa-R26VYCGuCyovhbFdPavpw); [Campaign reports](https://api.bol.com/advertiser/reporting/bulk-reports)
- Realised daily net profit in the Sheet's own P&L (per shipping day; includes storage 2.40–4.90/day and, since mid-Sep, the API commission): 1–26 September sums to +181 euro on 12 units shipped, with 104 sponsored-ads and 3 branded-shelf spend; non-sale days run −4 to −14 and sale days +17 to +145 (14-09 +145 with 4 units; 25-09 +72 with 3 units; 21-09 +31 with 2 units and 14.23 ads). 12–31 August sums to +302 on 11 units. — [Sheet: Winstmotor Dagelijks](https://docs.google.com/spreadsheets/d/1dy1WZNtPqJkAfEpKZ-MLa-R26VYCGuCyovhbFdPavpw)
- The Sheet's own phase plan values contribution at 22.80 (89.98/79.99), 16.18 (79.99/69.99), 12.87 (74.98/64.99) and 9.56 (69.98/59.99) per pillow using landed 19.77 and 16.4% commission; the corrected batch-2 landed (14.00) raises those by ~0.50 per its own note. — [Sheet: Winsttest](https://docs.google.com/spreadsheets/d/1dy1WZNtPqJkAfEpKZ-MLa-R26VYCGuCyovhbFdPavpw)

### Inferences
- Each 5-euro price step changes contribution by 3.3 euro (0.826 VAT factor minus 0.164 commission) under the model, or 3.7 euro with the measured commission; the volume needed to hold profit constant when dropping from 69.99 to 64.99 (white) is ×1.18 (model) and from 79.99 to 74.98 (bundle) ×1.18 — not the ×1.26 the Sheet quotes, because the Sheet's base contribution is lower.
- The historical cost per ad-attributed pillow (16–17 euro) is below the break-even ad cost at every price ≥64.99 for white and ≥74.98 for bundles under the model commission, and at every listed price under the measured commission; under the 8% TACOS cap in the Sheet only ~5 euro of ads per pillow are allowed, which is a third of what the economics permit.
- At the best historical pace (1.03/day in July) the line is at or below zero after storage even with 16 euro/day ads unless white is ≥69.99 and bundles ≥79.99; the plan only becomes clearly profitable at ≥2 pillows/day, which has never been sustained for a full week (best week 13 units = 1.9/day, wk 29).

### Gaps
- Whether bol's commission is really 1.18 + 9.71% (ex VAT) must be confirmed on an invoice; the model's 16.4% may be a VAT-inclusive published rate, in which case the true ex-VAT cost is the measured figure and the table with measured commission applies.
- No Q4 2025 data exist in the API window, so seasonality (Sinterklaas/Christmas uplift) cannot be quantified internally; the Sheet's "november 1,7 keer het zoekvolume van augustus" is an unsourced internal assumption.

---

## Key question 7: Cash/stock constraint — 248 pillows now plus 248 late November; how many per day can be sold through Q4 without running out, and what a stock-out in early December costs versus not pushing

### Takeaway
248 pillows on 27-09 last until 20-11 at 4.6/day (or until 30-11 at 3.9/day); with the second 248 the whole of Q4 supports 5.2/day — four to five times the best month ever (1.03/day). Stock only becomes binding if Q4 velocity exceeds ~4/day; at 3/day the first batch alone lasts to 18-12. Bundles are capped separately by covers (beige 43 is the bottleneck). A December stock-out would cost roughly the daily velocity × contribution (21–26 euro) per day plus the conversion hangover seen in September (10 days at zero orders with traffic intact).

### Cited Findings
- Stock on 27-09: white pillow 248 (offer stock, managedByRetailer, FBR/VVB); bundle offers show beige 43, blue 87, grey 80, black 80, identical to the loose-cover stocks, so bundles draw from the same 248 pillows and are limited per colour by covers. — [Offer API](https://api.bol.com/retailer/offers/0ab6c304-f4a5-46c8-ac75-afe1384266ac); per-offer reads of the bundle and cover offers via the same endpoint
- Second batch: 248 more pillows expected late November (brief); the Sheet notes batch 2 was 500 units at USD 11.60 of which 252 landed in this shipment and "de 248 die nog komen krijgen eigen vracht". — [Sheet: Winsttest](https://docs.google.com/spreadsheets/d/1dy1WZNtPqJkAfEpKZ-MLa-R26VYCGuCyovhbFdPavpw)
- Run-out arithmetic from 27-09: 248 units ÷ 54 days (to 20-11) = 4.6/day; ÷ 64 days (to 30-11) = 3.9/day; 496 units ÷ 95 days (to 31-12) = 5.2/day. At 1/day the first 248 last to June 2027; 2/day → 29-01-2027; 3/day → 18-12-2026; 4/day → 28-11-2026; 5/day → 15-11-2026. — arithmetic on [Offer API](https://api.bol.com/retailer/offers/0ab6c304-f4a5-46c8-ac75-afe1384266ac) stock
- Best observed velocities: July 32 units in 31 days (1.03/day); best week 13 (wk 29, 1.9/day); best 7-day stretch after the price cut 6 units (19–25 Sep, 0.86/day); August 0.65/day. — [Shipments API](https://api.bol.com/retailer/shipments)
- September stock-out signature: 0 pillow orders 1–10 Sep with pillow visits 117 (wk 36) and 3–13 ad clicks/day, then 5 orders 11–17 Sep; no visible traffic loss afterwards (visits 146 wk 37, 239 wk 38). — [Shipments API](https://api.bol.com/retailer/shipments); [Offer insights API](https://api.bol.com/retailer/insights/offer); [Campaign reports](https://api.bol.com/advertiser/reporting/bulk-reports)
- Organic rank for the beige bundle on "leeskussen" was 25–27 during 6–10 Sep and 16–22 on 14–15 Sep, versus 20–22 in the last week of August, i.e. no additional rank drop attributable to the stock-out itself. — [Sheet: Bol Ranks](https://docs.google.com/spreadsheets/d/1dy1WZNtPqJkAfEpKZ-MLa-R26VYCGuCyovhbFdPavpw)
- Stock-related target in the Sheet: the year goal needs 135–332 pillows Sep–Dec (1.1–2.7/day) depending on price; the "VOORRAADPOORT" excludes beige from any low-price phase if fewer than 20 beige covers remain. — [Sheet: Winsttest](https://docs.google.com/spreadsheets/d/1dy1WZNtPqJkAfEpKZ-MLa-R26VYCGuCyovhbFdPavpw)

### Inferences
- Demand, not stock, is the Q4 constraint: even the Sheet's most ambitious target (2.7/day) uses only 59% of the 496-unit Q4 capacity, and a "push" to 3/day still leaves ~250 units on 31-12 if batch 2 lands. Stock only becomes the binding constraint at ≥4/day sustained from October, which no historical period approaches.
- If a push did reach 4/day and batch 2 slipped from 30-11 to, say, 10-12, the gap would be ~12 days × 4 units × 21–26 euro = roughly 1,000–1,250 euro of lost contribution, plus the September pattern of ~10 days of zero conversion while ads keep spending (~25–60 euro wasted at current budgets) and a probable rank loss in the highest-demand weeks. Against that, "not pushing" (staying at ~2/day) forgoes ~2 × 21–26 = 42–52 euro of contribution per day for the 54–64 days before batch 2 (≈2,300–3,300 euro), so the arithmetic favours pushing as long as batch 2 is reliably in stock before the first 248 run out; the practical rule is to cap velocity at ~3.9/day (248 ÷ 64 days) until batch 2 is confirmed shipped.
- The colour cap matters more than the pillow cap: beige is the best-selling and most-visited colour (19 of 65 units, 33–135 visits/week) with only 43 covers; at the Jun–Sep colour mix (29% beige) a total of ~150 pillows would exhaust beige, i.e. beige runs out at ~1.6/day total velocity before 30-11 unless covers are restocked.

### Gaps
- The arrival date and quantity certainty of batch 2 (late November) come only from the brief and the Sheet; no purchase-order or shipment tracking data were available.
- No internal data quantify the December demand uplift or the rank penalty of an out-of-stock week in peak season; the September episode happened in a low-demand month and lasted ~10 days, so it is a weak proxy.
- Cash constraint (whether funding for batch 2 or more covers is in place) was not visible in any source consulted.
