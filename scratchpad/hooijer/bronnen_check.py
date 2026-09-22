"""Waar komt de uitbraak bij Hunter en de instorting bij Tofvel/Sockwell vandaan?"""
import pandas as pd
import sql

pd.set_option("display.width", 200)

def bron(sleutel, periode, titel, top=6):
    df = sql.vraag(sleutel,
        "FROM sessions SHOW sessions, sessions_with_cart_additions, "
        f"sessions_that_completed_checkout GROUP BY referrer_source {periode} "
        "ORDER BY sessions DESC LIMIT 8")
    if df.empty:
        print(f"\n--- {titel}: geen data"); return
    df["wagen_pct"] = df.sessions_with_cart_additions / df.sessions * 100
    df["conv_pct"] = df.sessions_that_completed_checkout / df.sessions * 100
    print(f"\n--- {titel}")
    print(df.head(top).to_string(index=False, float_format=lambda v: f"{v:,.2f}"))

bron("hunter_nl", "SINCE 2026-09-01 UNTIL 2026-09-21", "Hunter NL  september 2026 (uitbraak)")
bron("hunter_nl", "SINCE 2026-06-01 UNTIL 2026-06-30", "Hunter NL  juni 2026 (ervoor)")
bron("tofvel_nl", "SINCE 2025-11-01 UNTIL 2025-11-30", "Tofvel NL  november 2025 (piek)")
bron("tofvel_nl", "SINCE 2026-07-01 UNTIL 2026-07-31", "Tofvel NL  juli 2026 (dal)")
bron("sockwell_nl", "SINCE 2025-11-01 UNTIL 2025-11-30", "Sockwell NL  november 2025 (piek)")
bron("sockwell_nl", "SINCE 2026-07-01 UNTIL 2026-07-31", "Sockwell NL  juli 2026 (dal)")
