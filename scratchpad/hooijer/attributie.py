"""Verschoof de order-toewijzing van 'direct' naar 'search' op hetzelfde moment?"""
from concurrent.futures import ThreadPoolExecutor
import pandas as pd
import sql

SHOPS = ["lazamani_nl", "sockwell_nl", "keen_nl", "heydude_nl", "bartogi_nl", "lazamani_de"]

def haal(sleutel):
    return sql.vraag(sleutel, "FROM sessions SHOW sessions, sessions_that_completed_checkout "
                              "GROUP BY month, referrer_source SINCE 2025-06-01 UNTIL 2026-08-31 "
                              "ORDER BY month")

with ThreadPoolExecutor(max_workers=6) as pool:
    alles = pd.concat(pool.map(haal, SHOPS), ignore_index=True)
alles["maand"] = alles.month.str[:7]

pd.set_option("display.width", 220)
for meting, titel in (("sessions", "SESSIES"),
                      ("sessions_that_completed_checkout", "ORDERS")):
    tab = alles.pivot_table(index="maand", columns="referrer_source", values=meting,
                            aggfunc="sum").fillna(0).astype(int)
    tab["TOTAAL"] = tab.sum(axis=1)
    if meting == "sessions":
        sessies = tab.copy()
    print(f"\n=== {titel} per maand naar bron (zes grootste shops) ===")
    print(tab.to_string())
    if meting != "sessions":
        aandeel = (tab[["direct", "search"]].div(tab.TOTAAL, axis=0) * 100).round(1)
        aandeel.columns = ["% orders direct", "% orders search"]
        print("\n--- aandeel in de orders ---")
        print(aandeel.to_string())
