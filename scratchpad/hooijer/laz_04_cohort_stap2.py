"""1. Retouren per ordermaand (niet per retourmaand) — dat rijpt nog.
   2. Waar in de winkel gaat stap 1 -> stap 2 mis bij Lazamani NL?"""
import pandas as pd
import shop, sql

VRAAG = """
query($cursor: String) {
  orders(first: 100, after: $cursor,
         query: "created_at:>=2026-03-01 created_at:<=2026-08-31") {
    pageInfo { hasNextPage endCursor }
    nodes { name createdAt
      subtotalPriceSet { shopMoney { amount } }
      currentSubtotalPriceSet { shopMoney { amount } } } } }
"""
rijen, cursor = [], None
while True:
    d = shop.gql("lazamani_nl", VRAAG, {"cursor": cursor})
    for o in d["orders"]["nodes"]:
        rijen.append({"maand": o["createdAt"][:7],
                      "besteld": float(o["subtotalPriceSet"]["shopMoney"]["amount"]),
                      "behouden": float(o["currentSubtotalPriceSet"]["shopMoney"]["amount"])})
    if not d["orders"]["pageInfo"]["hasNextPage"]:
        break
    cursor = d["orders"]["pageInfo"]["endCursor"]

df = pd.DataFrame(rijen)
g = df.groupby("maand").agg(orders=("besteld", "count"), besteld=("besteld", "sum"),
                            behouden=("behouden", "sum")).reset_index()
g["retour% van de order"] = (1 - g.behouden / g.besteld) * 100
pd.set_option("display.width", 200)
print("=== Lazamani NL: retour gemeten op de maand waarin BESTELD is ===")
print(g.to_string(index=False, float_format=lambda v: f"{v:,.1f}"))
print("  let op: recente maanden zijn nog niet uitgerijpt, het retourvenster loopt nog.\n")

SCHOON = "SINCE 2026-03-01 UNTIL 2026-08-31"
M = ("sessions, sessions_with_cart_additions, sessions_that_reached_checkout, "
     "sessions_that_completed_checkout")

def soort(p):
    if p == "/": return "homepage"
    for s, n in (("/products/", "productpagina"), ("/collections/", "collectiepagina"),
                 ("/pages/", "inhoud"), ("/blogs/", "blog"), ("/search", "zoeken")):
        if p.startswith(s): return n
    return "overig"

print("=== waar landt men, en wat gebeurt er daarna ===")
for s in ("lazamani_nl", "sockwell_nl"):
    d = sql.vraag(s, f"FROM sessions SHOW {M} GROUP BY landing_page_path {SCHOON} "
                     f"ORDER BY sessions DESC LIMIT 400")
    d["soort"] = d.landing_page_path.map(soort)
    a = d.groupby("soort").agg(
        sessies=("sessions", "sum"), wagen=("sessions_with_cart_additions", "sum"),
        afrekenen=("sessions_that_reached_checkout", "sum"),
        orders=("sessions_that_completed_checkout", "sum")).reset_index()
    a["aandeel%"] = a.sessies / a.sessies.sum() * 100
    a["wagen%"] = a.wagen / a.sessies * 100
    a["afreken%"] = a.afrekenen / a.wagen * 100
    a["order%"] = a.orders / a.afrekenen * 100
    print(f"\n-- {shop.LABELS[s]}")
    print(a.sort_values("sessies", ascending=False).to_string(
        index=False, float_format=lambda v: f"{v:,.2f}"))
