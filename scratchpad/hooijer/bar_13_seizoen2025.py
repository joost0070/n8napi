"""Orderregels 2025 ophalen, om het seizoenspatroon per productsoort te bepalen."""
import sys
import pandas as pd
import shop

VRAAG = """
query($cursor: String) {
  orders(first: 50, after: $cursor, reverse: false,
         query: "created_at:>=2025-01-01 created_at:<=2025-12-31") {
    pageInfo { hasNextPage endCursor }
    nodes { name createdAt
      lineItems(first: 50) { nodes {
        quantity currentQuantity sku title
        discountedTotalSet { shopMoney { amount } }
        product { title vendor } } } } } }
"""

def haal(sleutel):
    rijen, cursor = [], None
    while True:
        d = shop.gql(sleutel, VRAAG, {"cursor": cursor}, timeout=180)
        for o in d["orders"]["nodes"]:
            for r in o["lineItems"]["nodes"]:
                p = r["product"] or {}
                rijen.append({
                    "maand": o["createdAt"][:7], "sku": r["sku"],
                    "artikel": r["title"], "merk": p.get("vendor") or "",
                    "aantal": r["quantity"], "aantal_nu": r["currentQuantity"],
                    "netto": float(r["discountedTotalSet"]["shopMoney"]["amount"]),
                })
        if not d["orders"]["pageInfo"]["hasNextPage"]:
            break
        cursor = d["orders"]["pageInfo"]["endCursor"]
    df = pd.DataFrame(rijen)
    df.to_pickle(f"bar_2025_{sleutel}.pkl")
    print(f"  {shop.LABELS[sleutel]}: {len(df):,} regels, {df.aantal.sum():,} stuks"
          .replace(",", "."), flush=True)
    return df

if __name__ == "__main__":
    for s in (sys.argv[1:] or ["bartogi_nl", "bartogi_de"]):
        haal(s)
