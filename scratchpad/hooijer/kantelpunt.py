"""Wanneer kantelt het precies, en hoe scherp? Dagelijks, rond de overgang."""
from concurrent.futures import ThreadPoolExecutor
import pandas as pd
import sql

SHOPS = ["lazamani_nl", "sockwell_nl", "keen_nl", "heydude_nl", "bartogi_nl", "lazamani_de"]

def haal(sleutel):
    return sql.vraag(sleutel, "FROM sessions SHOW sessions, sessions_that_completed_checkout "
                              "GROUP BY day, referrer_source SINCE 2026-01-15 UNTIL 2026-03-05 "
                              "ORDER BY day")

with ThreadPoolExecutor(max_workers=6) as pool:
    alles = pd.concat(pool.map(haal, SHOPS), ignore_index=True)
alles["dag"] = alles.day.str[:10]

per_dag = alles.pivot_table(index="dag", columns="referrer_source", values="sessions",
                            aggfunc="sum").fillna(0).astype(int)
orders = alles.groupby("dag").sessions_that_completed_checkout.sum()
per_dag["TOTAAL"] = per_dag.sum(axis=1)
per_dag["orders"] = orders
per_dag["sess/order"] = (per_dag.TOTAAL / per_dag.orders).round(1)
pd.set_option("display.width", 200, "display.max_rows", 60)
print("=== zes grootste shops samen, sessies per dag naar bron ===")
print(per_dag.to_string())
