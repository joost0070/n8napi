"""Sessies per maand per shop: zitten er gaten of knikken in de meting?"""
from concurrent.futures import ThreadPoolExecutor

import pandas as pd

import shop
import sql


def haal(sleutel):
    df = sql.vraag(sleutel, "FROM sessions SHOW sessions GROUP BY month "
                            "SINCE 2025-08-01 UNTIL 2026-09-21 ORDER BY month")
    df["shop"] = shop.LABELS.get(sleutel, sleutel)
    return df


with ThreadPoolExecutor(max_workers=5) as pool:
    alles = pd.concat(pool.map(haal, shop.SHOPS), ignore_index=True)

tabel = alles.pivot_table(index="shop", columns="month", values="sessions",
                          aggfunc="sum").fillna(0).astype(int)
tabel.columns = [c[:7] for c in tabel.columns]
tabel = tabel.sort_values(tabel.columns[-2], ascending=False)
tabel.loc["ALLE SHOPS"] = tabel.sum()
pd.set_option("display.width", 250, "display.max_columns", 30)
print(tabel.to_string())
tabel.to_csv("maandreeks_sessies.csv")
