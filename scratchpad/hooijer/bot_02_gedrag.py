"""Botverkeer Tofvel NL: gedrag per land en dag; kopers per land; AI-verwijzers in alle shops.

Schrijft bot_gedrag.pkl, bot_kopers.pkl, bot_ai.pkl.
"""
import pandas as pd
import shop
import sql

BOTLANDEN = ["Brazil", "Pakistan", "South Africa", "Argentina", "Colombia", "Bangladesh",
             "Chile", "United Arab Emirates", "Ukraine", "Venezuela", "Ecuador", "Mexico",
             "Russia", "Kenya", "Israel", "Ireland", "Singapore"]
AI = r"chatgpt|openai|perplexity|gemini|copilot|claude|bard|you\.com|deepseek|mistral|grok"
M = "sessions, sessions_with_cart_additions, sessions_that_completed_checkout, bounce_rate, average_session_duration, pageviews"

if __name__ == "__main__":
    lijst = ", ".join(f"'{l}'" for l in BOTLANDEN)
    uit = []
    for dim in ["day", "session_device_type", "landing_page_type", "referrer_source",
                "landing_page_path"]:
        df = sql.vraag("tofvel_nl", f"FROM sessions SHOW {M} WHERE session_country IN ({lijst}) "
                                    f"GROUP BY {dim} SINCE 2026-09-15 UNTIL 2026-09-30 "
                                    f"ORDER BY sessions DESC LIMIT 60")
        df = df.rename(columns={dim: "waarde"}); df["dim"] = dim; uit.append(df)
    pd.concat(uit).to_pickle("bot_gedrag.pkl")

    kopers = []
    for s in shop.SHOPS:
        df = sql.vraag(s, "FROM sales SHOW orders, net_sales GROUP BY shipping_country "
                          "SINCE 2024-01-01 UNTIL 2026-09-30 ORDER BY orders DESC LIMIT 100")
        df["shop"] = s; kopers.append(df)
    pd.concat(kopers).to_pickle("bot_kopers.pkl")

    ai = []
    for s in shop.SHOPS:
        df = sql.vraag(s, "FROM sessions SHOW sessions, sessions_with_cart_additions, "
                          "sessions_that_completed_checkout GROUP BY referrer_name, utm_source "
                          "SINCE 2026-04-01 UNTIL 2026-09-30 ORDER BY sessions DESC LIMIT 1000")
        df["shop"] = s
        tekst = df.referrer_name.astype(str) + " " + df.utm_source.astype(str)
        ai.append(df[tekst.str.contains(AI, case=False, regex=True)])
    pd.concat(ai).to_pickle("bot_ai.pkl")
    print("klaar")
