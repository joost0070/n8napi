"""Waar kwam het verkeer vandaan dat geen orders opleverde?

We vergelijken de piekperiode met een schone periode, op elke dimensie die
ShopifyQL biedt, voor de vier grootste shops samen.
"""
from concurrent.futures import ThreadPoolExecutor
import pandas as pd
import sql

PIEK = "SINCE 2025-10-01 UNTIL 2026-01-31"
SCHOON = "SINCE 2026-06-01 UNTIL 2026-08-31"
SHOPS = ["lazamani_nl", "sockwell_nl", "keen_nl", "tofvel_nl", "lazamani_de", "bartogi_de"]
METEN = "sessions, sessions_that_completed_checkout"

def haal(arg):
    sleutel, dim, periode = arg
    df = sql.vraag(sleutel, f"FROM sessions SHOW {METEN} GROUP BY {dim} {periode} "
                            f"ORDER BY sessions DESC LIMIT 15")
    df["dim"] = dim
    return df

def tabel(dim):
    taken = [(s, dim, PIEK) for s in SHOPS]
    with ThreadPoolExecutor(max_workers=5) as pool:
        piek = pd.concat(pool.map(haal, taken), ignore_index=True)
    taken = [(s, dim, SCHOON) for s in SHOPS]
    with ThreadPoolExecutor(max_workers=5) as pool:
        schoon = pd.concat(pool.map(haal, taken), ignore_index=True)

    def vouw(df, naam):
        g = df.groupby(dim)[["sessions", "sessions_that_completed_checkout"]].sum()
        g.columns = [f"sess {naam}", f"ord {naam}"]
        return g

    samen = vouw(piek, "piek").join(vouw(schoon, "nu"), how="outer").fillna(0)
    samen["conv% piek"] = samen["ord piek"] / samen["sess piek"] * 100
    samen["conv% nu"] = samen["ord nu"] / samen["sess nu"] * 100
    samen = samen.sort_values("sess piek", ascending=False).head(12)
    print(f"\n=== GROUP BY {dim} (zes shops samen) ===")
    print(samen.to_string(float_format=lambda v: f"{v:,.2f}"))

pd.set_option("display.width", 220)
for dim in ["referrer_source", "referrer_name", "utm_source", "utm_medium", "landing_page_path"]:
    tabel(dim)
