"""Alle 17 shops: welke bronnen leverden veel sessies en bijna geen orders?"""
from concurrent.futures import ThreadPoolExecutor
import pandas as pd
import shop, sql

PERIODEN = {"piek okt25-jan26": "SINCE 2025-10-01 UNTIL 2026-01-31",
            "nu jun-aug26": "SINCE 2026-06-01 UNTIL 2026-08-31"}

def haal(arg):
    sleutel, dim, periode = arg
    try:
        df = sql.vraag(sleutel, f"FROM sessions SHOW sessions, sessions_that_completed_checkout "
                                f"GROUP BY {dim} {periode} ORDER BY sessions DESC LIMIT 25")
    except Exception:
        return pd.DataFrame()
    df["shop"] = shop.LABELS.get(sleutel, sleutel)
    df = df.rename(columns={dim: "waarde"})
    df["dim"] = dim
    return df

for naam, periode in PERIODEN.items():
    taken = [(s, d, periode) for s in shop.SHOPS for d in ("referrer_name", "utm_source")]
    with ThreadPoolExecutor(max_workers=6) as pool:
        alles = pd.concat([d for d in pool.map(haal, taken) if len(d)], ignore_index=True)
    g = (alles.groupby(["dim", "waarde"])[["sessions", "sessions_that_completed_checkout"]]
         .sum().reset_index())
    g["conv%"] = g.sessions_that_completed_checkout / g.sessions * 100
    g = g[g.sessions >= 300].sort_values("sessions", ascending=False)
    verdacht = g[g["conv%"] < 0.30]
    print(f"\n=== {naam}: bronnen met >=300 sessies en conversie onder 0,30% ===")
    print(verdacht.to_string(index=False, float_format=lambda v: f"{v:,.2f}")
          if len(verdacht) else "  (geen)")
    print(f"  sessies in deze categorie: {verdacht.sessions.sum():,.0f}".replace(",", "."))
