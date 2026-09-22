"""Trechter per verkeersbron, per shop, op de schone periode."""
from concurrent.futures import ThreadPoolExecutor
import pandas as pd
import shop, sql

PERIODE = "SINCE 2026-03-01 UNTIL 2026-08-31"
METEN = ("sessions, sessions_with_cart_additions, sessions_that_reached_checkout, "
         "sessions_that_completed_checkout")

def haal(sleutel):
    df = sql.vraag(sleutel, f"FROM sessions SHOW {METEN} GROUP BY referrer_source "
                            f"{PERIODE} ORDER BY sessions DESC")
    df["shop"] = shop.LABELS.get(sleutel, sleutel)
    return df

with ThreadPoolExecutor(max_workers=5) as pool:
    alles = pd.concat(pool.map(haal, shop.SHOPS), ignore_index=True)

def afgeleid(df):
    df = df.copy()
    df["wagen%"] = df.sessions_with_cart_additions / df.sessions * 100
    df["conversie%"] = df.sessions_that_completed_checkout / df.sessions * 100
    return df.replace([float("inf"), float("-inf")], 0).fillna(0)

alles = afgeleid(alles)
alles.to_pickle("bronnen_v2.pkl")

groep = afgeleid(alles.groupby("referrer_source")[
    ["sessions", "sessions_with_cart_additions", "sessions_that_reached_checkout",
     "sessions_that_completed_checkout"]].sum().reset_index())
groep["aandeel sessies%"] = groep.sessions / groep.sessions.sum() * 100
pd.set_option("display.width", 200)
print("=== ALLE SHOPS SAMEN, maart t/m augustus 2026, per verkeersbron ===")
print(groep.sort_values("sessions", ascending=False).to_string(
    index=False, float_format=lambda v: f"{v:,.2f}"))

print("\n=== conversie% per bron per shop (grootste shops) ===")
kruis = alles.pivot_table(index="shop", columns="referrer_source", values="conversie%")
sessies = alles.groupby("shop").sessions.sum().sort_values(ascending=False)
print(kruis.reindex(sessies.index).head(10)[
    ["search", "direct", "social", "email"]].to_string(float_format=lambda v: f"{v:,.2f}"))
