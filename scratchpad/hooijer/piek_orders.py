"""Beslissende toets: als sessies verdubbelen maar orders niet, is het verkeer niet echt.

Orders zijn de harde grond: die worden geteld bij de kassa, niet door het
sessiescript. We zetten per maand sessies naast orders voor alle shops samen.
"""
from concurrent.futures import ThreadPoolExecutor
import pandas as pd
import shop, sql

def haal(sleutel):
    s = sql.vraag(sleutel, "FROM sessions SHOW sessions, sessions_with_cart_additions, "
                           "sessions_that_completed_checkout GROUP BY month "
                           "SINCE 2025-06-01 UNTIL 2026-08-31 ORDER BY month")
    g = sql.vraag(sleutel, "FROM sales SHOW orders, net_sales GROUP BY month "
                           "SINCE 2025-06-01 UNTIL 2026-08-31 ORDER BY month")
    df = s.merge(g, on="month", how="outer").fillna(0)
    df["shop"] = shop.LABELS.get(sleutel, sleutel)
    return df

with ThreadPoolExecutor(max_workers=5) as pool:
    alles = pd.concat(pool.map(haal, shop.SHOPS), ignore_index=True)
alles["maand"] = alles.month.str[:7]
alles.to_pickle("piek_maanden.pkl")

groep = alles.groupby("maand")[["sessions", "sessions_with_cart_additions",
                                "sessions_that_completed_checkout", "orders", "net_sales"]].sum()
groep["wagen%"] = groep.sessions_with_cart_additions / groep.sessions * 100
groep["conv%"] = groep.sessions_that_completed_checkout / groep.sessions * 100
groep["sessies per order"] = groep.sessions / groep.orders

pd.set_option("display.width", 200)
print("=== ALLE 17 SHOPS SAMEN, per maand ===")
print(groep.to_string(float_format=lambda v: f"{v:,.2f}"))
