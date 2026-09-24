"""Orderregels per shop over een venster, voor retourpercentages per model en maat.

Gebruik: python3 ret_02_orderregels.py <shopsleutel> <van> <tot>
"""
import sys
import pandas as pd
import shop

VRAAG = """
query($cursor: String, $q: String!) {
  orders(first: 50, after: $cursor, query: $q) {
    pageInfo { hasNextPage endCursor }
    nodes { name createdAt
      lineItems(first: 50) { nodes {
        sku quantity currentQuantity
        variant { title }
        product { title }
        discountedTotalSet { shopMoney { amount } } } } } } }
"""


def haal(sleutel, van, tot):
    rijen, cursor = [], None
    q = f"created_at:>={van} created_at:<={tot}"
    while True:
        d = shop.gql(sleutel, VRAAG, {"cursor": cursor, "q": q}, timeout=180)
        for o in d["orders"]["nodes"]:
            for r in o["lineItems"]["nodes"]:
                rijen.append({
                    "order": o["name"], "datum": o["createdAt"][:10],
                    "sku": str(r["sku"] or "").zfill(13),
                    "product": (r["product"] or {}).get("title") or "",
                    "maat": (r["variant"] or {}).get("title") or "",
                    "aantal": r["quantity"], "aantal_nu": r["currentQuantity"],
                    "netto": float(r["discountedTotalSet"]["shopMoney"]["amount"]),
                })
        if not d["orders"]["pageInfo"]["hasNextPage"]:
            break
        cursor = d["orders"]["pageInfo"]["endCursor"]
    df = pd.DataFrame(rijen)
    df.to_pickle(f"ret_regels_{sleutel}.pkl")
    print(f"  {sleutel}: {df.order.nunique():,} orders, {df.aantal.sum():,} paren "
          f"({van} t/m {tot})".replace(",", "."), flush=True)


if __name__ == "__main__":
    haal(sys.argv[1], sys.argv[2], sys.argv[3])
