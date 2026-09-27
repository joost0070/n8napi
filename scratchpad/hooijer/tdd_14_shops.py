"""Tofvel-deepdive: Tofvel naast de andere shops over dezelfde 90 dagen.

Sessiefilter voor alle shops gelijk: alleen landen met minimaal één afgeronde
checkout in de periode (weert botverkeer uit landen zonder kopers). Marge =
ShopifyQL gross_margin (alleen betrouwbaar waar kostprijs bij verkoop is vastgelegd).
Schrijft tdd_shops.pkl.
"""
import pandas as pd
import shop
import sql

VAN, TOT = "2026-06-29", "2026-09-26"
M = ("sessions, sessions_with_cart_additions, sessions_that_reached_checkout, "
     "sessions_that_completed_checkout")

if __name__ == "__main__":
    rijen = []
    for s in shop.SHOPS:
        ses = sql.vraag(s, f"FROM sessions SHOW {M} GROUP BY session_country "
                           f"SINCE {VAN} UNTIL {TOT} ORDER BY sessions DESC LIMIT 1000")
        echt = ses[ses.sessions_that_completed_checkout > 0]
        v = sql.vraag(s, f"FROM sales SHOW gross_sales, discounts, returns, net_sales, orders, "
                         f"cost_of_goods_sold, gross_profit SINCE {VAN} UNTIL {TOT}")
        v = v.iloc[0] if len(v) else pd.Series(dtype=float)
        rijen.append({"shop": shop.LABELS[s], "sleutel": s,
                      "sessies_alle": ses.sessions.sum(), "sessies_echt": echt.sessions.sum(),
                      "wagen": echt.sessions_with_cart_additions.sum(),
                      "checkout": echt.sessions_that_reached_checkout.sum(),
                      "afgerond": echt.sessions_that_completed_checkout.sum(),
                      **{k: v.get(k) for k in ["gross_sales", "discounts", "returns",
                                               "net_sales", "orders", "cost_of_goods_sold",
                                               "gross_profit"]}})
        print(s, flush=True)
    d = pd.DataFrame(rijen)
    d["wagen_%"] = 100 * d.wagen / d.sessies_echt
    d["order_%_van_checkout"] = 100 * d.afgerond / d.checkout
    d["conversie_%"] = 100 * d.afgerond / d.sessies_echt
    d["aov"] = d.net_sales / d.orders
    d["retour_%"] = -100 * d.returns / d.gross_sales
    d["korting_%"] = -100 * d.discounts / d.gross_sales
    d["marge_%"] = 100 * d.gross_profit / d.net_sales
    d["kost_dekking_%"] = 100 * d.cost_of_goods_sold / (d.net_sales * 0.5)  # ruwe indicatie
    d.to_pickle("tdd_shops.pkl")
    pd.set_option("display.width", 250)
    print(d[["shop", "sessies_alle", "sessies_echt", "wagen_%", "order_%_van_checkout",
             "conversie_%", "orders", "net_sales", "aov", "retour_%", "korting_%",
             "marge_%"]].round(1).to_string())
