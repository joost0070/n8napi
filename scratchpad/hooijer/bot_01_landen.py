"""Botverkeer: welke landen leveren sessies zonder kopers, per shop, en sinds wanneer.

Vergelijkt 1-30 sep 2026 met jun-aug 2026 per land: sessies, winkelwagens, orders
(via sessies met afgeronde checkout) en orders op verzendland (Admin API, 2024-2026).
Schrijft bot_landen.pkl.
"""
import pandas as pd
import shop
import sql

M = ("sessions, sessions_with_cart_additions, sessions_that_completed_checkout, "
     "bounce_rate, average_session_duration, pageviews")

if __name__ == "__main__":
    rijen = []
    for s in shop.SHOPS:
        for naam, venster in [("jun-aug", "SINCE 2026-06-01 UNTIL 2026-08-31"),
                              ("sep", "SINCE 2026-09-01 UNTIL 2026-09-30")]:
            df = sql.vraag(s, f"FROM sessions SHOW {M} GROUP BY session_country "
                              f"{venster} ORDER BY sessions DESC LIMIT 300")
            df["shop"], df["venster"] = s, naam
            rijen.append(df)
        print(s, flush=True)
    d = pd.concat(rijen, ignore_index=True)
    d.to_pickle("bot_landen.pkl")
