"""Tofvel-deepdive: sessies per land x (apparaat | bron | dag | landingspagina).

Nodig om botverkeer (landen buiten de afzetmarkt, 0 winkelwagens) eruit te filteren
voordat trechter, apparaat en kanaal worden beoordeeld. Schrijft tdd_sessies_land.pkl.
"""
import pandas as pd
import sql
from tdd_01_sessies import M, PERIODES, SHOPS

DIMS = {"apparaat": "session_device_type",
        "bron": "referrer_source, referrer_name, utm_source, utm_medium",
        "dag": "day",
        "landing": "landing_page_path"}

if __name__ == "__main__":
    uit = []
    for s in SHOPS:
        for p, (van, tot) in PERIODES.items():
            for naam, dim in DIMS.items():
                q = (f"FROM sessions SHOW {M} GROUP BY session_country, {dim} "
                     f"SINCE {van} UNTIL {tot} ORDER BY sessions DESC LIMIT 5000")
                df = sql.vraag(s, q)
                df["dim"], df["shop"], df["periode"] = naam, s, p
                uit.append(df)
            print(s, p, flush=True)
    pd.concat(uit, ignore_index=True).to_pickle("tdd_sessies_land.pkl")
