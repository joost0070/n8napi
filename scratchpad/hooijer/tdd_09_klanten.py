"""Tofvel-deepdive: nieuwe vs terugkerende klanten, herhaalaankoop en klantwaarde.

Nieuw = eerste order van dit klant-id in de shop sinds 2021 (orders van vóór 2021
ontbreken, dus 'nieuw' is een lichte overschatting). Klantwaarde op subtotaal excl.
btw minus terugbetaald. Schrijft tdd_klanten.pkl en tdd_orders_klant.pkl.
"""
import pandas as pd
from tdd_01_sessies import SHOPS

BTW = {"tofvel_nl": 1.21, "tofvel_de": 1.19, "tofvel_en": 1.21}


def orderkanaal(r):
    bron, utm = str(r.laatste_bron), str(r.laatste_utm_source).lower()
    ref = str(r.laatste_ref)
    if utm == "klaviyo" or bron == "email" or "android.gm" in bron:
        return "E-mail"
    if bron in ("Google", "Bing", "DuckDuckGo", "Yahoo") or "ecosia" in bron or \
            "syndicatedsearch" in bron:
        return "Zoekmachine"
    if bron in ("Instagram", "Facebook") or utm in ("ig", "facebook", "fb"):
        return "Social"
    if bron == "direct" or "tofvel" in ref:
        return "Direct"
    if bron == "nan":
        return "Onbekend (geen cookietoestemming)"
    return "Overig / onbekende bron"


if __name__ == "__main__":
    uit, alle = [], []
    for s in SHOPS:
        l = pd.read_pickle(f"tdd_licht_{s}.pkl")
        l = l[l.bron_kanaal.eq("web") & l.klant.notna() & ~l.test].copy()
        l["d"] = pd.to_datetime(l.datum.str[:10])
        l["waarde"] = (l.subtotaal - l.terugbetaald).clip(lower=0) / BTW[s]
        l = l.sort_values("d")
        l["volgnr"] = l.groupby("klant").cumcount() + 1
        eerste = l.groupby("klant").d.min().rename("eerste")
        l = l.join(eerste, on="klant")
        l["shop"] = s
        alle.append(l)
        # herhaalaankoop per cohort (eerste order in jaar)
        for jaar in [2022, 2023, 2024, 2025]:
            c = l[l.eerste.dt.year == jaar]
            klanten = c.klant.nunique()
            rij = {"shop": s, "cohort": jaar, "klanten": klanten}
            for dgn in [90, 180, 365]:
                binnen = c[c.d <= c.eerste + pd.Timedelta(days=dgn)]
                rij[f"waarde_{dgn}d"] = binnen.waarde.sum() / klanten
                rij[f"herhaal_{dgn}d_%"] = 100 * (binnen.groupby("klant").size() > 1).mean()
            twee = c[c.volgnr == 2]
            rij["dagen_tot_2e_mediaan"] = (twee.d - twee.eerste).dt.days.median()
            rij["ooit_herhaal_%"] = 100 * (c.groupby("klant").size() > 1).mean()
            uit.append(rij)
    k = pd.DataFrame(uit)
    k.to_pickle("tdd_klanten.pkl")
    pd.concat(alle).to_pickle("tdd_orders_klant.pkl")
    pd.set_option("display.width", 250)
    print(k.round(1).to_string())
