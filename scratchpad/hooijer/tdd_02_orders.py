"""Tofvel-deepdive: orders ophalen.

licht  : alle orders sinds 2021 (klant, datum, bedrag) voor herhaalaankoop en klantwaarde
zwaar  : orders vanaf 2025-06-29 met regels, kostprijs, korting, retour en herkomst

Gebruik: python3 tdd_02_orders.py <shopsleutel> [<van> <tot> <achtervoegsel>]
  met van/tot alleen het zware deel over dat venster (bv. seizoen 2024/25).
Schrijft tdd_licht_<shop>.pkl, tdd_orders_<shop>.pkl, tdd_regels_<shop>.pkl.
Klantgegevens blijven beperkt tot een intern klant-id; geen namen of adressen.
"""
import sys
import pandas as pd
import shop

LICHT = """
query($cursor: String, $q: String!) {
  orders(first: 250, after: $cursor, query: $q, sortKey: CREATED_AT) {
    pageInfo { hasNextPage endCursor }
    nodes { name createdAt cancelledAt test sourceName
      customer { id }
      subtotalPriceSet { shopMoney { amount } }
      totalRefundedSet { shopMoney { amount } } } } }
"""

ZWAAR = """
query($cursor: String, $q: String!) {
  orders(first: 25, after: $cursor, query: $q, sortKey: CREATED_AT) {
    pageInfo { hasNextPage endCursor }
    nodes { name createdAt cancelledAt test sourceName
      customer { id }
      discountCodes
      shippingAddress { countryCodeV2 }
      subtotalPriceSet { shopMoney { amount } }
      totalDiscountsSet { shopMoney { amount } }
      totalShippingPriceSet { shopMoney { amount } }
      totalTaxSet { shopMoney { amount } }
      totalPriceSet { shopMoney { amount } }
      totalRefundedSet { shopMoney { amount } }
      totalRefundedShippingSet { shopMoney { amount } }
      customerJourneySummary {
        daysToConversion
        momentsCount { count }
        firstVisit { source sourceType referrerUrl landingPage
          utmParameters { source medium campaign } }
        lastVisit { source sourceType referrerUrl landingPage
          utmParameters { source medium campaign } } }
      lineItems(first: 20) { nodes {
        sku quantity currentQuantity
        variant { id title compareAtPrice price
          inventoryItem { unitCost { amount } } }
        product { id title productType }
        originalUnitPriceSet { shopMoney { amount } }
        originalTotalSet { shopMoney { amount } }
        discountedTotalSet { shopMoney { amount } }
        totalDiscountSet { shopMoney { amount } } } }
      refunds(first: 10) { createdAt
        totalRefundedSet { shopMoney { amount } }
        refundLineItems(first: 20) { nodes { quantity
          lineItem { sku } subtotalSet { shopMoney { amount } } } } } } } }
"""


def bedrag(x):
    return float(x["shopMoney"]["amount"]) if x else 0.0


def blader(sleutel, vraag, q, verwerk):
    cursor = None
    while True:
        d = shop.gql(sleutel, vraag, {"cursor": cursor, "q": q}, timeout=180)
        for o in d["orders"]["nodes"]:
            verwerk(o)
        if not d["orders"]["pageInfo"]["hasNextPage"]:
            return
        cursor = d["orders"]["pageInfo"]["endCursor"]


def bezoek(v, pre):
    v = v or {}
    utm = v.get("utmParameters") or {}
    return {f"{pre}_bron": v.get("source"), f"{pre}_type": v.get("sourceType"),
            f"{pre}_ref": v.get("referrerUrl"), f"{pre}_landing": v.get("landingPage"),
            f"{pre}_utm_source": utm.get("source"), f"{pre}_utm_medium": utm.get("medium"),
            f"{pre}_utm_campaign": utm.get("campaign")}


def main(sleutel, van="2025-06-29", tot=None, achter=""):
    if achter:  # alleen zwaar deel over een eigen venster
        return zwaar(sleutel, f"created_at:>={van} created_at:<={tot}", achter)
    licht = []
    blader(sleutel, LICHT, "created_at:>=2021-01-01", lambda o: licht.append({
        "order": o["name"], "datum": o["createdAt"], "geannuleerd": bool(o["cancelledAt"]),
        "test": o["test"], "bron_kanaal": o["sourceName"],
        "klant": (o["customer"] or {}).get("id"),
        "subtotaal": bedrag(o["subtotalPriceSet"]),
        "terugbetaald": bedrag(o["totalRefundedSet"])}))
    pd.DataFrame(licht).to_pickle(f"tdd_licht_{sleutel}.pkl")
    print(f"{sleutel}: licht {len(licht)} orders", flush=True)
    zwaar(sleutel, f"created_at:>={van}", "")


def zwaar(sleutel, q, achter):
    orders, regels = [], []

    def verwerk(o):
        cj = o["customerJourneySummary"] or {}
        rij = {"order": o["name"], "datum": o["createdAt"],
               "geannuleerd": bool(o["cancelledAt"]), "test": o["test"],
               "bron_kanaal": o["sourceName"], "klant": (o["customer"] or {}).get("id"),
               "codes": ",".join(o["discountCodes"] or []),
               "land": (o["shippingAddress"] or {}).get("countryCodeV2"),
               "subtotaal": bedrag(o["subtotalPriceSet"]),
               "korting": bedrag(o["totalDiscountsSet"]),
               "verzend": bedrag(o["totalShippingPriceSet"]),
               "btw": bedrag(o["totalTaxSet"]), "totaal": bedrag(o["totalPriceSet"]),
               "terugbetaald": bedrag(o["totalRefundedSet"]),
               "terug_verzend": bedrag(o["totalRefundedShippingSet"]),
               "dagen_tot_conversie": cj.get("daysToConversion"),
               "momenten": (cj.get("momentsCount") or {}).get("count")}
        rij.update(bezoek(cj.get("firstVisit"), "eerste"))
        rij.update(bezoek(cj.get("lastVisit"), "laatste"))
        retour = {}
        for rf in o["refunds"]:
            for rl in rf["refundLineItems"]["nodes"]:
                k = (rl["lineItem"] or {}).get("sku")
                a = retour.setdefault(k, [0, 0.0, rf["createdAt"]])
                a[0] += rl["quantity"]
                a[1] += bedrag(rl["subtotalSet"])
        orders.append(rij)
        for r in o["lineItems"]["nodes"]:
            v = r["variant"] or {}
            kost = ((v.get("inventoryItem") or {}).get("unitCost") or {}).get("amount")
            rt = retour.get(r["sku"], [0, 0.0, None])
            regels.append({
                "order": o["name"], "datum": o["createdAt"], "sku": r["sku"],
                "product_id": (r["product"] or {}).get("id"),
                "product": (r["product"] or {}).get("title") or "",
                "soort": (r["product"] or {}).get("productType") or "",
                "maat": v.get("title") or "", "aantal": r["quantity"],
                "aantal_nu": r["currentQuantity"],
                "adviesprijs": float(v["compareAtPrice"]) if v.get("compareAtPrice") else None,
                "prijs_nu": float(v["price"]) if v.get("price") else None,
                "stukprijs": bedrag(r["originalUnitPriceSet"]),
                "bruto": bedrag(r["originalTotalSet"]),
                "netto": bedrag(r["discountedTotalSet"]),
                "regelkorting": bedrag(r["totalDiscountSet"]),
                "kostprijs": float(kost) if kost else None,
                "retour_aantal": rt[0], "retour_bedrag": rt[1], "retour_datum": rt[2]})

    blader(sleutel, ZWAAR, q, verwerk)
    pd.DataFrame(orders).to_pickle(f"tdd_orders_{sleutel}{achter}.pkl")
    pd.DataFrame(regels).to_pickle(f"tdd_regels_{sleutel}{achter}.pkl")
    print(f"{sleutel}: zwaar {len(orders)} orders, {len(regels)} regels", flush=True)


if __name__ == "__main__":
    main(*sys.argv[1:])
