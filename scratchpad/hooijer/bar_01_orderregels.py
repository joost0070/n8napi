"""Bartogi: alle orderregels YTD met kostprijs, korting, retour en verzendkosten.

Shopify's eigen gross_profit is voor deze shop tot en met juni onbruikbaar (de
kostprijzen zijn pas later ingevoerd). We rekenen de marge daarom zelf uit de
orderregels: verkoopprijs na korting tegen de kostprijs van de variant.

Let op: unitCost is de kostprijs van NU, niet die van het moment van verkoop.
Voor schoenen die een seizoen meegaan is dat een redelijke benadering.
"""
import sys
import pandas as pd
import shop

VRAAG = """
query($cursor: String) {
  orders(first: 40, after: $cursor, reverse: false,
         query: "created_at:>=2026-01-01 created_at:<=2026-09-21") {
    pageInfo { hasNextPage endCursor }
    nodes {
      name createdAt
      totalShippingPriceSet { shopMoney { amount } }
      totalDiscountsSet { shopMoney { amount } }
      subtotalPriceSet { shopMoney { amount } }
      currentSubtotalPriceSet { shopMoney { amount } }
      customer { numberOfOrders }
      customerJourneySummary { firstVisit { source } }
      lineItems(first: 50) { nodes {
        quantity currentQuantity
        sku title
        originalTotalSet { shopMoney { amount } }
        discountedTotalSet { shopMoney { amount } }
        variant { title inventoryItem { unitCost { amount } } }
        product { title vendor productType }
      } }
    } } }
"""


def haal(sleutel: str) -> pd.DataFrame:
    rijen, cursor, n = [], None, 0
    while True:
        d = shop.gql(sleutel, VRAAG, {"cursor": cursor}, timeout=180)
        blok = d["orders"]
        for o in blok["nodes"]:
            n += 1
            reis = (o.get("customerJourneySummary") or {}).get("firstVisit") or {}
            gemeen = {
                "order": o["name"], "datum": o["createdAt"][:10],
                "maand": o["createdAt"][:7],
                "verzendopbrengst": float(o["totalShippingPriceSet"]["shopMoney"]["amount"]),
                "orderkorting": float(o["totalDiscountsSet"]["shopMoney"]["amount"]),
                "subtotaal": float(o["subtotalPriceSet"]["shopMoney"]["amount"]),
                "subtotaal_nu": float(o["currentSubtotalPriceSet"]["shopMoney"]["amount"]),
                "orders_van_klant": int((o["customer"] or {}).get("numberOfOrders") or 0),
                "eerste_bron": reis.get("source") or "onbekend",
            }
            regels = o["lineItems"]["nodes"]
            for r in regels:
                kost = ((r["variant"] or {}).get("inventoryItem") or {}).get("unitCost") or {}
                p = r["product"] or {}
                rijen.append({**gemeen,
                    "regels_in_order": len(regels),
                    "sku": r["sku"], "artikel": r["title"],
                    "merk": p.get("vendor") or "", "type": p.get("productType") or "",
                    "maat": (r["variant"] or {}).get("title") or "",
                    "aantal": r["quantity"], "aantal_nu": r["currentQuantity"],
                    "bruto": float(r["originalTotalSet"]["shopMoney"]["amount"]),
                    "netto": float(r["discountedTotalSet"]["shopMoney"]["amount"]),
                    "kostprijs": float(kost.get("amount") or 0),
                })
        if not blok["pageInfo"]["hasNextPage"]:
            break
        cursor = blok["pageInfo"]["endCursor"]
    print(f"  {shop.LABELS[sleutel]}: {n:,} orders, {len(rijen):,} regels".replace(",", "."),
          flush=True)
    return pd.DataFrame(rijen)


if __name__ == "__main__":
    for sleutel in (sys.argv[1:] or ["bartogi_nl", "bartogi_de"]):
        df = haal(sleutel)
        df.to_pickle(f"bar_regels_{sleutel}.pkl")
