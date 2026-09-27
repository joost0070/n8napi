"""Tofvel-deepdive: trechter op echte sessies (afzetlanden), per apparaat, bron en week.

Botfilter: alleen sessies uit de landen waar de shop verkoopt. Sessies uit andere
landen hebben in deze periode vrijwel geen winkelwagens (zie tdd_sessies_land.pkl).
Schrijft tdd_trechter.pkl.
"""
import pandas as pd

MARKT = {
    "tofvel_nl": {"The Netherlands", "Netherlands", "Belgium"},
    "tofvel_de": {"Germany", "Austria", "Switzerland", "Luxembourg"},
    # .eu verkoopt vooral naar NL/FR/BE/DE/ES; Ierland, VS, China en Singapore
    # zijn datacenterverkeer zonder winkelwagens en vallen erbuiten.
    "tofvel_en": {"France", "The Netherlands", "Netherlands", "Belgium", "Germany",
                  "Spain", "Italy", "Portugal", "Denmark", "Luxembourg", "Austria",
                  "Poland", "Sweden", "Finland", "Norway", "Switzerland",
                  "United Kingdom"},
}
STAP = ["sessions", "sessions_with_cart_additions", "sessions_that_reached_checkout",
        "sessions_that_completed_checkout"]


def kanaal(r):
    bron, naam = str(r.referrer_source), str(r.referrer_name).lower()
    utm_s, utm_m = str(r.utm_source).lower(), str(r.utm_medium).lower()
    if utm_s == "klaviyo" or bron == "email":
        return "E-mail"
    if utm_m in ("paid", "cpc", "ppc") or bron == "paid":
        return "Betaald social" if utm_s in ("facebook", "fb", "ig", "instagram") \
            else "Betaald zoeken (herkenbaar)"
    if bron == "search":
        return "Zoekmachine (organisch + Google Ads)"
    if bron == "social":
        return "Social organisch"
    if bron == "direct":
        return "Direct"
    return "Referral / overig"


def echt(d):
    return d[d.apply(lambda r: r.session_country in MARKT[r.shop], axis=1)]


def ratio(df):
    df = df.copy()
    df["wagen_%"] = 100 * df.sessions_with_cart_additions / df.sessions
    df["checkout_%_van_wagen"] = 100 * df.sessions_that_reached_checkout / df.sessions_with_cart_additions
    df["order_%_van_checkout"] = 100 * df.sessions_that_completed_checkout / df.sessions_that_reached_checkout
    df["conversie_%"] = 100 * df.sessions_that_completed_checkout / df.sessions
    return df


if __name__ == "__main__":
    d = pd.read_pickle("tdd_sessies_land.pkl")
    uit = []
    # totaal en botaandeel (uit de apparaat-splitsing, die telt elke sessie één keer)
    app = d[d.dim == "apparaat"]
    tot_alle = app.groupby(["shop", "periode"])[STAP].sum()
    e = echt(app)
    tot = e.groupby(["shop", "periode"])[STAP].sum()
    tot["bot_%"] = 100 * (1 - tot.sessions / tot_alle.sessions)
    tot = ratio(tot).reset_index().assign(dim="totaal", waarde="totaal")
    uit.append(tot)
    a = ratio(e.groupby(["shop", "periode", "session_device_type"])[STAP].sum()).reset_index()
    uit.append(a.rename(columns={"session_device_type": "waarde"}).assign(dim="apparaat"))
    b = echt(d[d.dim == "bron"]).copy()
    b["waarde"] = b.apply(kanaal, axis=1)
    uit.append(ratio(b.groupby(["shop", "periode", "waarde"])[STAP].sum()).reset_index()
               .assign(dim="kanaal"))
    w = echt(d[d.dim == "dag"]).copy()
    w["waarde"] = pd.to_datetime(w.day).dt.to_period("W-SUN").dt.start_time.dt.strftime("%Y-%m-%d")
    uit.append(ratio(w.groupby(["shop", "periode", "waarde"])[STAP].sum()).reset_index()
               .assign(dim="week"))
    res = pd.concat(uit, ignore_index=True)
    res.to_pickle("tdd_trechter.pkl")
    pd.set_option("display.width", 250)
    kol = ["shop", "periode", "waarde", "sessions", "wagen_%", "checkout_%_van_wagen",
           "order_%_van_checkout", "conversie_%"]
    print(res[res.dim == "totaal"][kol + ["bot_%"]].round(1).to_string())
    for dim in ["apparaat", "kanaal"]:
        x = res[(res.dim == dim) & (res.sessions >= 50)]
        print(x[kol].round(1).to_string())
    print(res[(res.dim == "week") & (res.shop == "tofvel_nl")][kol].round(1).to_string())
