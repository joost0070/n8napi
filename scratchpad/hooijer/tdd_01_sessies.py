"""Tofvel-deepdive: sessies en trechter per shop en periode, uitgesplitst.

Periodes: P = afgelopen 90 dagen t/m gisteren, V = 90 dagen daarvoor,
J = zelfde 90 dagen vorig jaar. Schrijft tdd_sessies.pkl.
"""
import pandas as pd
import sql

SHOPS = ["tofvel_nl", "tofvel_de", "tofvel_en"]
PERIODES = {"P": ("2026-06-29", "2026-09-26"),
            "V": ("2026-03-31", "2026-06-28"),
            "J": ("2025-06-29", "2025-09-26")}
M = ("sessions, sessions_with_cart_additions, sessions_that_reached_checkout, "
     "sessions_that_completed_checkout")
DIMS = [None, "session_device_type", "referrer_source", "session_country",
        "day", "landing_page_type"]

if __name__ == "__main__":
    uit = []
    for s in SHOPS:
        for p, (van, tot) in PERIODES.items():
            for dim in DIMS:
                q = f"FROM sessions SHOW {M}"
                if dim:
                    q += f" GROUP BY {dim}"
                q += f" SINCE {van} UNTIL {tot}"
                if dim:
                    q += " ORDER BY sessions DESC LIMIT 1000"
                df = sql.vraag(s, q)
                df = df.rename(columns={dim: "waarde"}) if dim else df.assign(waarde="totaal")
                df["dim"] = dim or "totaal"
                df["shop"], df["periode"] = s, p
                uit.append(df)
            print(s, p, "klaar", flush=True)
    res = pd.concat(uit, ignore_index=True)
    res.to_pickle("tdd_sessies.pkl")
    print(res[res.dim == "totaal"].to_string())
