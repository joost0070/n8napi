"""Wanneer begint en stopt de piek precies? Per week, per shop."""
from concurrent.futures import ThreadPoolExecutor
import pandas as pd
import shop, sql

GETROFFEN = ["sockwell_nl", "tofvel_nl", "lazamani_de", "bartogi_de", "sockwell_de", "tofvel_de"]
CONTROLE = ["heydude_nl", "keen_nl", "lazamani_nl", "bartogi_nl"]

def haal(sleutel):
    df = sql.vraag(sleutel, "FROM sessions SHOW sessions, sessions_that_completed_checkout "
                            "GROUP BY week SINCE 2025-08-01 UNTIL 2026-03-31 ORDER BY week")
    df["shop"] = shop.LABELS.get(sleutel, sleutel)
    return df

with ThreadPoolExecutor(max_workers=5) as pool:
    alles = pd.concat(pool.map(haal, GETROFFEN + CONTROLE), ignore_index=True)
alles["week"] = alles.week.str[:10]

pd.set_option("display.width", 260, "display.max_columns", 40)
for titel, groep in (("GETROFFEN SHOPS", GETROFFEN), ("CONTROLE SHOPS", CONTROLE)):
    namen = [shop.LABELS[s] for s in groep]
    tab = (alles[alles.shop.isin(namen)]
           .pivot_table(index="shop", columns="week", values="sessions", aggfunc="sum")
           .fillna(0).astype(int).reindex(namen))
    print(f"\n=== {titel}: sessies per week ===")
    print(tab.to_string())
