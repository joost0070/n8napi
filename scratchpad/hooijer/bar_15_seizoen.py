"""Seizoenscorrectie: wat verkoopt er nog in oktober t/m december?

Het jaargemiddelde is voor schoenen een slechte voorspeller. Sandalen die in
juli goed liepen verkopen in november niets, laarzen juist wel. We leiden per
productsoort uit 2025 af hoeveel er in oktober t/m december werd verkocht per
stuk dat in januari t/m september was verkocht, en projecteren daarmee de
resterende vraag van 2026.

    seizoensindex = stuks okt-dec 2025 / stuks jan-sep 2025   (per productsoort)
    verwachte vraag okt-dec 2026 = stuks jan-sep 2026 x index
"""
import pandas as pd
from bar_14_soort import soort

pd.set_option("display.width", 210)
LABEL = {"bartogi_nl": "NL", "bartogi_de": "DE"}
Q4 = ["2025-10", "2025-11", "2025-12"]


def index_per_soort(sleutel):
    d = pd.read_pickle(f"bar_2025_{sleutel}.pkl").copy()
    d["soort"] = d.artikel.map(soort)
    d["periode"] = d.maand.map(lambda m: "q4" if m in Q4 else ("jansep" if m < "2025-10" else "x"))
    g = d[d.periode != "x"].pivot_table(index="soort", columns="periode",
                                        values="aantal", aggfunc="sum").fillna(0)
    for k in ("q4", "jansep"):
        if k not in g:
            g[k] = 0
    g["index"] = g.q4 / g.jansep.replace(0, pd.NA)
    shop_index = g.q4.sum() / g.jansep.sum()
    # te dunne soorten terug naar het shopgemiddelde
    g.loc[g.jansep < 25, "index"] = shop_index
    g["index"] = g["index"].fillna(shop_index)
    return g, shop_index


def toepassen(sleutel):
    idx, shop_index = index_per_soort(sleutel)
    w = pd.read_pickle("bar_werkdocument.pkl")
    w = w[w.shop == LABEL[sleutel]].copy()
    w["soort"] = w.artikel.map(soort)
    w["seizoensindex"] = w.soort.map(idx["index"]).fillna(shop_index)
    w["verwacht okt-dec"] = w.stuks * w.seizoensindex
    w["voorraad na Q4"] = w.voorraad - w["verwacht okt-dec"]
    w["dekking Q4"] = w.voorraad / w["verwacht okt-dec"].replace(0, pd.NA)
    return w, idx, shop_index


def advies(r):
    if r["marge%"] >= 20:
        return "op doel"
    if pd.isna(r["bodemprijs incl"]):
        return "onhaalbaar bij huidige kosten: uitfaseren"
    if r["bodem boven vanprijs"] and r["vanprijs incl"] > 0:
        return "bodemprijs boven adviesprijs: niet met prijs op te lossen"
    if r["verwacht okt-dec"] < 1:
        return "buiten seizoen: uit de aanbieding halen, bewaren tot volgend jaar"
    d = r["dekking Q4"]
    if pd.isna(d) or d > 4:
        return "veel meer voorraad dan Q4-vraag: prijs handhaven, ruimen"
    if d < 1.5:
        return "verkoopt dit kwartaal uit: prijs omhoog naar bodemprijs"
    return "prijs omhoog, gefaseerd"


if __name__ == "__main__":
    stukken = []
    for sleutel in ("bartogi_nl", "bartogi_de"):
        w, idx, si = toepassen(sleutel)
        w["advies_seizoen"] = w.apply(advies, axis=1)
        stukken.append(w)
        if sleutel == "bartogi_nl":
            print("=== seizoensindex per productsoort (Bartogi NL, uit 2025) ===")
            print("    hoeveel stuks in okt-dec per stuk verkocht in jan-sep\n")
            t = idx.sort_values("index", ascending=False)
            t = t[t.jansep >= 10]
            print(t[["jansep", "q4", "index"]].to_string(float_format=lambda v: f"{v:,.2f}"))
            print(f"\n  shopgemiddelde: {si:.2f}")
    alles = pd.concat(stukken, ignore_index=True)
    alles.to_pickle("bar_werkdocument_seizoen.pkl")

    nl = alles[alles.shop == "NL"]
    print("\n\n=== advies mét seizoen tegenover zonder (Bartogi NL) ===")
    k = pd.crosstab(nl.advies, nl.advies_seizoen).T
    print(k.to_string())
    print("\n=== nieuwe verdeling ===")
    g = nl.groupby("advies_seizoen").agg(
        artikelen=("artikel", "count"), stuks=("stuks", "sum"), omzet=("bruto", "sum"),
        tekort=("tekort", "sum"), verwacht=("verwacht okt-dec", "sum"),
        voorraad=("voorraad", "sum")).reset_index()
    g["aandeel omzet%"] = g.omzet / nl.bruto.sum() * 100
    print(g.sort_values("tekort", ascending=False).to_string(
        index=False, float_format=lambda v: f"{v:,.1f}"))
