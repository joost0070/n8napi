"""Funnels per ingang: trechter per landingspaginatype, bron en pagina.

Tofvel NL (NL+BE, 1 jun - 3 okt 2026) in detail; alle shops per landingspaginatype
(landen met minstens één order, laatste 90 dagen). Schrijft fun_ingangen.pkl.
"""
import pandas as pd
import shop
import sql

M = ("sessions, sessions_with_cart_additions, sessions_that_reached_checkout, "
     "sessions_that_completed_checkout, bounce_rate, average_session_duration, pageviews")
NL = "WHERE session_country IN ('Netherlands', 'The Netherlands', 'Belgium')"
VENSTER = "SINCE 2026-06-01 UNTIL 2026-10-03"

if __name__ == "__main__":
    uit = []
    for naam, dim in [("type", "landing_page_type"),
                      ("type_bron", "landing_page_type, referrer_source"),
                      ("type_apparaat", "landing_page_type, session_device_type"),
                      ("bron", "referrer_source, referrer_name, utm_source, utm_medium"),
                      ("pagina", "landing_page_path")]:
        df = sql.vraag("tofvel_nl", f"FROM sessions SHOW {M} {NL} GROUP BY {dim} {VENSTER} "
                                    f"ORDER BY sessions DESC LIMIT 400")
        df["dim"], df["shop"] = naam, "tofvel_nl"
        uit.append(df)
    for s in shop.SHOPS:
        land = sql.vraag(s, "FROM sessions SHOW sessions, sessions_that_completed_checkout "
                            "GROUP BY session_country SINCE -90d UNTIL today "
                            "ORDER BY sessions DESC LIMIT 300")
        echte = land[land.sessions_that_completed_checkout > 0].session_country.tolist()
        if not echte:
            continue
        lijst = ", ".join("'" + l.replace("'", "\\'") + "'" for l in echte)
        df = sql.vraag(s, f"FROM sessions SHOW {M} WHERE session_country IN ({lijst}) "
                          f"GROUP BY landing_page_type SINCE -90d UNTIL today "
                          f"ORDER BY sessions DESC LIMIT 50")
        df["dim"], df["shop"] = "alle_shops_type", s
        uit.append(df)
        print(s, flush=True)
    pd.concat(uit, ignore_index=True).to_pickle("fun_ingangen.pkl")
