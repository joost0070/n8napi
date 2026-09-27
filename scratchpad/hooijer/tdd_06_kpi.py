"""Tofvel-deepdive: advertentiekosten per week uit het Tofvel KPI-rapport (upload).

Leest 'RD - Kosten NL/DE/EU' (Google Ads, Bing Ads, Meta Ads) vanaf 2024.
Schrijft tdd_advertentie_week.pkl: shop, jaar, week, kanaal, kosten.
"""
import pandas as pd

F = "tofvel_extra/2026 _ Tofvel _ KPI-rapportage op weekniveau.xlsx"
TAB = {"tofvel_nl": "RD - Kosten NL", "tofvel_de": "RD - Kosten DE",
       "tofvel_en": "RD - Kosten EU"}


def blokken(df):
    """Zoekt per platform (rij 0) de kolom met 'Jaar & week' en de kostenkolom."""
    uit = []
    for j in range(df.shape[1]):
        platform = str(df.iat[0, j])
        if platform in ("Google Ads", "Bing Ads", "Meta Ads"):
            kop = [str(df.iat[1, k]) for k in range(j, min(j + 6, df.shape[1]))]
            kosten = next((j + i for i, v in enumerate(kop)
                           if v.startswith(("Kosten", "Cost"))), None)
            if kosten is not None:
                uit.append((platform, j, kosten))
    return uit


rijen = []
for shop_, tab in TAB.items():
    df = pd.read_excel(F, sheet_name=tab, header=None)
    for platform, wk, kost in blokken(df):
        for i in range(2, len(df)):
            w = str(df.iat[i, wk])
            if "|" not in w:
                continue
            jaar, week = w.split("|")
            rijen.append({"shop": shop_, "jaar": int(jaar), "week": int(week),
                          "kanaal": platform,
                          "kosten": pd.to_numeric(df.iat[i, kost], errors="coerce")})
res = pd.DataFrame(rijen).fillna({"kosten": 0})
res.to_pickle("tdd_advertentie_week.pkl")
if __name__ == "__main__":
    t = res[res.week.between(27, 39)].pivot_table(index=["shop", "jaar"], columns="kanaal",
                                                   values="kosten", aggfunc="sum")
    print(t.round(0))
    print(res[(res.jaar == 2026)].groupby(["shop", "kanaal"]).week.agg(["min", "max"]))
