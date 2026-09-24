"""Hunter NL: is het afrekenlek echt, of breekt de meting?

Zet per periode het afrekenpercentage per sessie naast de echte orders (kassa)
per sessie met winkelwagen, en het deel van de orders dat Shopify aan een
sessie kan koppelen. Een plotselinge daling van die koppeling wijst op een
meetprobleem (cookiebanner of toestemming), niet op klanten die afhaken.
"""
import sql

M = ("sessions, sessions_with_cart_additions, sessions_that_reached_checkout, "
     "sessions_that_completed_checkout")
PERIODEN = [("1-17 sep 2025", "SINCE 2025-09-01 UNTIL 2025-09-17"),
            ("1-18 aug 2026", "SINCE 2026-08-01 UNTIL 2026-08-18"),
            ("19-31 aug 2026", "SINCE 2026-08-19 UNTIL 2026-08-31"),
            ("1-17 sep 2026", "SINCE 2026-09-01 UNTIL 2026-09-17")]

if __name__ == "__main__":
    for label, per in PERIODEN:
        s = sql.vraag("hunter_nl", f"FROM sessions SHOW {M} {per}").iloc[0]
        o = sql.vraag("hunter_nl", f"FROM sales SHOW orders {per}").iloc[0].orders
        print(f"{label:<16} afrekenen {s.sessions_that_reached_checkout / s.sessions_with_cart_additions * 100:5.1f}%"
              f"  orders per wagen {o / s.sessions_with_cart_additions * 100:5.1f}%"
              f"  gekoppeld {s.sessions_that_completed_checkout / o * 100:4.0f}%")
