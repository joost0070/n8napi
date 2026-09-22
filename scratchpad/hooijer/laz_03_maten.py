"""Bestellen Lazamani-klanten meerdere maten van hetzelfde model tegelijk?

Dat is de klassieke verklaring voor een hoog retourpercentage bij schoenen: de
klant bestelt twee maten om te passen en stuurt er één terug. Als dat zo is, is
het retourpercentage geen kwaliteitsprobleem maar een maatinformatieprobleem.
"""
import pandas as pd
import shop

VRAAG = """
query($cursor: String) {
  orders(first: 50, after: $cursor,
         query: "created_at:>=2026-07-01 created_at:<=2026-08-31") {
    pageInfo { hasNextPage endCursor }
    nodes {
      name
      subtotalPriceSet { shopMoney { amount } }
      currentSubtotalPriceSet { shopMoney { amount } }
      lineItems(first: 40) { nodes {
        quantity
        variant { title }
        product { id title } } }
    } } }
"""


def haal(sleutel):
    rijen, cursor = [], None
    while True:
        d = shop.gql(sleutel, VRAAG, {"cursor": cursor})
        for o in d["orders"]["nodes"]:
            regels = o["lineItems"]["nodes"]
            per_product = {}
            stuks = 0
            for r in regels:
                pid = (r["product"] or {}).get("id") or "?"
                per_product.setdefault(pid, set()).add((r["variant"] or {}).get("title"))
                stuks += r["quantity"]
            dubbel = sum(1 for maten in per_product.values() if len(maten) > 1)
            rijen.append({
                "order": o["name"], "producten": len(per_product), "stuks": stuks,
                "modellen_met_meer_maten": dubbel,
                "subtotaal": float(o["subtotalPriceSet"]["shopMoney"]["amount"]),
                "na_retour": float(o["currentSubtotalPriceSet"]["shopMoney"]["amount"]),
            })
        if not d["orders"]["pageInfo"]["hasNextPage"]:
            break
        cursor = d["orders"]["pageInfo"]["endCursor"]
    return pd.DataFrame(rijen)


if __name__ == "__main__":
    pd.set_option("display.width", 200)
    for sleutel in ("lazamani_nl", "lazamani_de"):
        df = haal(sleutel)
        df.to_pickle(f"laz_maten_{sleutel}.pkl")
        df["meer maten"] = df.modellen_met_meer_maten > 0
        df["behouden%"] = df.na_retour / df.subtotaal * 100
        g = df.groupby("meer maten").agg(
            orders=("order", "count"), subtotaal=("subtotaal", "sum"),
            gemiddeld=("subtotaal", "mean"), na=("na_retour", "sum"),
            stuks=("stuks", "mean")).reset_index()
        g["aandeel orders%"] = g.orders / g.orders.sum() * 100
        g["behouden%"] = g.na / g.subtotaal * 100
        print(f"\n=== {shop.LABELS[sleutel]}, juli en augustus 2026, {len(df):,} orders ==="
              .replace(",", "."))
        print(g.to_string(index=False, float_format=lambda v: f"{v:,.2f}"))
