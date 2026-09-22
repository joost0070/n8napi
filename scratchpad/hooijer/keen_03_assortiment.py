"""Assortiment en voorraad: hoeveel is er online, en hoeveel daarvan is te koop?"""
import sys
import pandas as pd
import shop

VRAAG = """
query($cursor: String) {
  products(first: 50, after: $cursor, query: "status:active") {
    pageInfo { hasNextPage endCursor }
    nodes {
      handle title productType totalInventory
      publishedAt
      variants(first: 100) {
        nodes {
          title sku price compareAtPrice
          inventoryQuantity
          inventoryItem { unitCost { amount } }
        }
      }
    }
  }
}
"""


def haal(sleutel: str) -> pd.DataFrame:
    rijen, cursor = [], None
    while True:
        data = shop.gql(sleutel, VRAAG, {"cursor": cursor})
        blok = data["products"]
        for p in blok["nodes"]:
            for v in p["variants"]["nodes"]:
                kost = (v["inventoryItem"] or {}).get("unitCost") or {}
                rijen.append({
                    "handle": p["handle"], "titel": p["title"],
                    "type": p["productType"] or "",
                    "maat": v["title"], "sku": v["sku"],
                    "prijs": float(v["price"] or 0),
                    "vanprijs": float(v["compareAtPrice"] or 0),
                    "kostprijs": float(kost.get("amount") or 0),
                    "voorraad": v["inventoryQuantity"] or 0,
                })
        if not blok["pageInfo"]["hasNextPage"]:
            break
        cursor = blok["pageInfo"]["endCursor"]
    return pd.DataFrame(rijen)


if __name__ == "__main__":
    for sleutel in (sys.argv[1:] or ["keen_nl", "heydude_nl"]):
        df = haal(sleutel)
        df.to_pickle(f"assortiment_{sleutel}.pkl")
        product = df.groupby(["handle", "titel"]).agg(
            maten=("maat", "count"),
            maten_op_voorraad=("voorraad", lambda v: (v > 0).sum()),
            voorraad=("voorraad", "sum"),
            prijs=("prijs", "median"),
            afgeprijsd=("vanprijs", lambda v: (v > 0).sum()),
        ).reset_index()
        product["dekking%"] = product.maten_op_voorraad / product.maten * 100

        print(f"\n=== {shop.LABELS[sleutel]} ===")
        print(f"  actieve producten            : {len(product):,}".replace(",", "."))
        print(f"  varianten (maten)            : {len(df):,}".replace(",", "."))
        uit = product[product.maten_op_voorraad == 0]
        print(f"  producten volledig uitverkocht maar nog actief: {len(uit):,} "
              f"({len(uit)/len(product)*100:.0f}%)".replace(",", "."))
        dun = product[(product.maten_op_voorraad > 0) & (product["dekking%"] < 50)]
        print(f"  producten met minder dan de helft van de maten: {len(dun):,} "
              f"({len(dun)/len(product)*100:.0f}%)".replace(",", "."))
        print(f"  mediane maatdekking          : {product['dekking%'].median():.0f}%")
        print(f"  mediane prijs                : € {product.prijs.median():,.2f}")
        te_koop = df[df.voorraad > 0]
        print(f"  mediane prijs van wat op voorraad is: € {te_koop.prijs.median():,.2f}")
        print(f"  varianten met een van-prijs (afgeprijsd): "
              f"{(df.vanprijs > 0).sum()/len(df)*100:.0f}%")
