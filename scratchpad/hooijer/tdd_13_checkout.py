"""Tofvel-deepdive: verlaten checkouts (Admin API) per periode en herstel.

Shopify registreert alleen checkouts waarin een e-mailadres of telefoonnummer is
ingevuld. 'Hersteld' = completedAt gevuld (later alsnog afgerond).
Schrijft tdd_checkouts.pkl.
"""
import pandas as pd
import shop
from tdd_01_sessies import PERIODES, SHOPS

Q = """query($c: String, $q: String) {
  abandonedCheckouts(first: 100, after: $c, query: $q) {
    pageInfo { hasNextPage endCursor }
    nodes { createdAt completedAt totalPriceSet { shopMoney { amount } }
      lineItems(first: 10) { nodes { quantity title } } } } }"""

if __name__ == "__main__":
    rijen = []
    for s in SHOPS:
        for p, (van, tot) in PERIODES.items():
            c = None
            while True:
                d = shop.gql(s, Q, {"c": c, "q": f"created_at:>={van} created_at:<={tot}"})
                for n in d["abandonedCheckouts"]["nodes"]:
                    rijen.append({"shop": s, "periode": p, "datum": n["createdAt"][:10],
                                  "hersteld": n["completedAt"] is not None,
                                  "waarde": float(n["totalPriceSet"]["shopMoney"]["amount"]),
                                  "stuks": sum(x["quantity"] for x in n["lineItems"]["nodes"])})
                pi = d["abandonedCheckouts"]["pageInfo"]
                if not pi["hasNextPage"]:
                    break
                c = pi["endCursor"]
    df = pd.DataFrame(rijen)
    df.to_pickle("tdd_checkouts.pkl")
    t = df.groupby(["shop", "periode"]).agg(verlaten=("waarde", "size"), waarde=("waarde", "sum"),
                                             hersteld=("hersteld", "sum"),
                                             hersteld_waarde=("waarde", lambda w: w[df.loc[w.index, "hersteld"]].sum()))
    t["herstel_%"] = 100 * t.hersteld / t.verlaten
    print(t.round(1).to_string())
