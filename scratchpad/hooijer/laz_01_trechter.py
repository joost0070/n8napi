"""Lazamani NL, DE en EN naast elkaar: trechter, tijd en verkeersbron."""
from concurrent.futures import ThreadPoolExecutor
import pandas as pd
import shop, sql

SCHOON = "SINCE 2026-03-01 UNTIL 2026-08-31"
M = ("sessions, sessions_with_cart_additions, sessions_that_reached_checkout, "
     "sessions_that_completed_checkout")
SHOPS = ["lazamani_nl", "lazamani_de", "lazamani_en"]
pd.set_option("display.width", 220)


def af(d):
    d = d.copy()
    d["wagen%"] = d.sessions_with_cart_additions / d.sessions * 100
    d["afreken%"] = d.sessions_that_reached_checkout / d.sessions_with_cart_additions * 100
    d["order%"] = d.sessions_that_completed_checkout / d.sessions_that_reached_checkout * 100
    d["conv%"] = d.sessions_that_completed_checkout / d.sessions * 100
    return d.replace([float("inf"), float("-inf")], 0).fillna(0)


basis = pd.read_pickle("nulmeting_v2.pkl")
groep = basis[basis.sleutel == "_totaal"].iloc[0]
laz = basis[basis.sleutel.isin(SHOPS)]
print("=== de drie shops naast de groep ===")
t = pd.concat([laz, basis[basis.sleutel == "_totaal"]])
print(t[["shop", "sessions", "wagen%", "afreken%", "order%", "conversie%",
         "net_sales", "orders", "AOV", "korting%", "retour%"]].to_string(
    index=False, float_format=lambda v: f"{v:,.2f}"))

print("\n=== per maand ===")
def maand(s):
    d = af(sql.vraag(s, f"FROM sessions SHOW {M} GROUP BY month {SCHOON} ORDER BY month"))
    d["shop"] = shop.LABELS[s]; d["maand"] = d.month.str[:7]
    return d
with ThreadPoolExecutor(max_workers=3) as p:
    m = pd.concat(p.map(maand, SHOPS), ignore_index=True)
for kol in ("wagen%", "afreken%", "order%"):
    print(f"\n-- {kol}")
    print(m.pivot_table(index="shop", columns="maand", values=kol).to_string(
        float_format=lambda v: f"{v:,.2f}"))

print("\n\n=== per verkeersbron ===")
def bron(s):
    d = af(sql.vraag(s, f"FROM sessions SHOW {M} GROUP BY referrer_source {SCHOON} "
                        f"ORDER BY sessions DESC"))
    d["shop"] = shop.LABELS[s]
    d["aandeel%"] = d.sessions / d.sessions.sum() * 100
    return d
with ThreadPoolExecutor(max_workers=3) as p:
    b = pd.concat(p.map(bron, SHOPS), ignore_index=True)
print(b[b.sessions > 300][["shop", "referrer_source", "sessions", "aandeel%", "wagen%",
                           "afreken%", "order%", "conv%"]].to_string(
    index=False, float_format=lambda v: f"{v:,.2f}"))
