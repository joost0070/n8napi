"""KEEN NL: nieuw tegenover terugkerend, en wat de eerste order waard is."""
import pandas as pd
import shop

VRAAG = """
query($cursor: String) {
  orders(first: 100, after: $cursor, reverse: false,
         query: "created_at:>=2026-03-01 created_at:<=2026-08-31") {
    pageInfo { hasNextPage endCursor }
    nodes {
      name createdAt
      customer { id numberOfOrders }
      customerJourneySummary { firstVisit { source } momentsCount { count } }
      currentSubtotalPriceSet { shopMoney { amount } }
      subtotalPriceSet { shopMoney { amount } }
      lineItems(first: 1) { nodes { quantity } }
    }
  }
}
"""

rijen, cursor = [], None
while True:
    d = shop.gql("keen_nl", VRAAG, {"cursor": cursor})
    blok = d["orders"]
    for o in blok["nodes"]:
        klant = o["customer"] or {}
        reis = o.get("customerJourneySummary") or {}
        eerste = (reis.get("firstVisit") or {})
        rijen.append({
            "order": o["name"], "datum": o["createdAt"][:10],
            "klant": klant.get("id"),
            "orders_van_klant": int(klant.get("numberOfOrders") or 0),
            "eerste_bron": eerste.get("source") or "onbekend",
            "momenten": (reis.get("momentsCount") or {}).get("count") or 0,
            "bedrag": float((o["subtotalPriceSet"] or {}).get("shopMoney", {}).get("amount") or 0),
            "bedrag_nu": float((o["currentSubtotalPriceSet"] or {}).get("shopMoney", {}).get("amount") or 0),
        })
    if not blok["pageInfo"]["hasNextPage"]:
        break
    cursor = blok["pageInfo"]["endCursor"]

df = pd.DataFrame(rijen)
df.to_pickle("keen_orders.pkl")
df["soort"] = df.orders_van_klant.apply(lambda n: "nieuw" if n <= 1 else "terugkerend")
pd.set_option("display.width", 200)

print(f"=== KEEN NL: {len(df):,} orders, maart t/m augustus 2026 ===\n".replace(",", "."))
g = df.groupby("soort").agg(orders=("order", "count"), omzet=("bedrag", "sum"),
                            gemiddeld=("bedrag", "mean"),
                            na_retour=("bedrag_nu", "sum")).reset_index()
g["aandeel orders%"] = g.orders / g.orders.sum() * 100
g["aandeel omzet%"] = g.omzet / g.omzet.sum() * 100
g["behouden%"] = g.na_retour / g.omzet * 100
print(g.to_string(index=False, float_format=lambda v: f"{v:,.2f}"))

print("\n=== eerste bezoekbron van de order ===")
b = df.groupby("eerste_bron").agg(orders=("order", "count"), omzet=("bedrag", "sum"),
                                  gemiddeld=("bedrag", "mean"),
                                  na_retour=("bedrag_nu", "sum")).reset_index()
b["aandeel%"] = b.orders / b.orders.sum() * 100
b["behouden%"] = b.na_retour / b.omzet * 100
print(b.sort_values("orders", ascending=False).head(10).to_string(
    index=False, float_format=lambda v: f"{v:,.2f}"))

print("\n=== hoeveel bezoeken gaan er aan een order vooraf ===")
df["momentgroep"] = pd.cut(df.momenten, [-1, 1, 2, 5, 10, 10000],
                           labels=["1", "2", "3-5", "6-10", "11+"])
m = df.groupby("momentgroep", observed=True).agg(
    orders=("order", "count"), gemiddeld=("bedrag", "mean")).reset_index()
m["aandeel%"] = m.orders / m.orders.sum() * 100
print(m.to_string(index=False, float_format=lambda v: f"{v:,.2f}"))
print(f"  mediaan aantal bezoeken voor een order: {df.momenten.median():.0f}")
