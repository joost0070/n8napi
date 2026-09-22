"""Wanneer begint de storing? Dagelijks rond half september 2025."""
from concurrent.futures import ThreadPoolExecutor
import pandas as pd
import sql

SHOPS = ["lazamani_nl", "sockwell_nl", "keen_nl", "heydude_nl", "bartogi_nl", "lazamani_de"]

def haal(sleutel):
    return sql.vraag(sleutel, "FROM sessions SHOW sessions, sessions_that_completed_checkout "
                              "GROUP BY day, referrer_source SINCE 2025-09-05 UNTIL 2025-10-05 "
                              "ORDER BY day")

with ThreadPoolExecutor(max_workers=6) as pool:
    alles = pd.concat(pool.map(haal, SHOPS), ignore_index=True)
alles["dag"] = alles.day.str[:10]

sess = alles.pivot_table(index="dag", columns="referrer_source", values="sessions",
                         aggfunc="sum").fillna(0).astype(int)
ord_ = alles.pivot_table(index="dag", columns="referrer_source",
                         values="sessions_that_completed_checkout",
                         aggfunc="sum").fillna(0).astype(int)
tab = pd.DataFrame({
    "sess direct": sess.get("direct", 0),
    "sess search": sess.get("search", 0),
    "sess totaal": sess.sum(axis=1),
    "ord direct": ord_.get("direct", 0),
    "ord search": ord_.get("search", 0),
    "ord totaal": ord_.sum(axis=1),
})
tab["% ord direct"] = (tab["ord direct"] / tab["ord totaal"] * 100).round(1)
pd.set_option("display.width", 200, "display.max_rows", 40)
print("=== zes grootste shops samen, per dag ===")
print(tab.to_string())
