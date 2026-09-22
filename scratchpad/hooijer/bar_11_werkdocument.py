"""Werkdocument: marge en bodemprijs per artikel, per merk.

Bodemprijs = verkoopprijs waarbij dit artikel 20% brutowinstmarge haalt, gegeven
zijn eigen inkoopprijs en retourpercentage:
    P = ( C(1-r) + verzendkosten/stuk - verzendopbrengst/stuk )
        / ( (1-r) - payment% - advertentie% - 0,20 )
"""
import pandas as pd

BTW = {"bartogi_nl": 1.21, "bartogi_de": 1.19}
LABEL = {"bartogi_nl": "NL", "bartogi_de": "DE"}
PAR = {"bartogi_nl": dict(adv=0.2092, pay=0.0078, verz=4.85, opbr=1.34),
       "bartogi_de": dict(adv=0.0878, pay=0.0310, verz=4.88, opbr=1.34)}
DOEL = 0.20
MAANDEN = 8.7   # 1 jan t/m 21 sep


def per_model(sleutel):
    d = pd.read_pickle("bar_artikelen.pkl")
    d = d[d.shop == sleutel].copy()
    btw, p = BTW[sleutel], PAR[sleutel]

    a = pd.read_pickle(f"assortiment_{sleutel}.pkl")
    voorraad = a.groupby("titel").voorraad.sum()

    m = d.groupby(["merk", "artikel"], dropna=False).agg(
        maten=("maat", "nunique"), stuks=("stuks", "sum"),
        retour_stuks=("stuks_retour", "sum"), lijst=("lijst", "sum"),
        bruto=("bruto", "sum"), afprijzing=("afprijzing", "sum"),
        omzet=("omzet", "sum"), inkoop=("inkoop", "sum"), retour=("retour", "sum"),
        brutowinst=("brutowinst", "sum"), tekort=("tekort tot 20%", "sum"),
        kostprijs=("kostprijs", "median"), vanprijs=("vanprijs", "median"),
    ).reset_index()
    m["prijs nu incl"] = m.bruto / m.stuks * btw
    m["vanprijs incl"] = m.vanprijs.fillna(0)
    m["marge%"] = m.brutowinst / m.bruto * 100
    m["afprijzing%"] = m.afprijzing / m.lijst * 100
    m["retour%"] = m.retour_stuks / m.stuks * 100
    m["voorraad"] = m.artikel.map(voorraad).fillna(0)
    m["voorraaddekking mnd"] = m.voorraad / (m.stuks / MAANDEN).replace(0, pd.NA)

    r = (m["retour%"] / 100).clip(upper=0.6)
    noemer = (1 - r) - p["pay"] - p["adv"] - DOEL
    m["bodemprijs incl"] = ((m.kostprijs * (1 - r) + p["verz"] - p["opbr"])
                            / noemer.where(noemer > 0.02)) * btw
    m["verhoging nodig"] = m["bodemprijs incl"] - m["prijs nu incl"]
    m["bodem boven vanprijs"] = m["bodemprijs incl"] > m["vanprijs incl"]

    def advies(row):
        if row["marge%"] >= DOEL * 100:
            return "op doel"
        if pd.isna(row["bodemprijs incl"]):
            return "onhaalbaar bij huidige kosten: uitfaseren"
        if row["bodem boven vanprijs"] and row["vanprijs incl"] > 0:
            return "bodemprijs ligt boven de adviesprijs: niet oplosbaar met prijs"
        dek = row["voorraaddekking mnd"]
        if pd.notna(dek) and dek > 18:
            return "voorraad te groot: prijs handhaven, snel weg"
        if pd.notna(dek) and dek < 6:
            return "prijs omhoog naar bodemprijs"
        return "prijs omhoog, gefaseerd"

    m["advies"] = m.apply(advies, axis=1)
    m["shop"] = LABEL[sleutel]
    return m


alles = pd.concat([per_model(s) for s in ("bartogi_nl", "bartogi_de")], ignore_index=True)
alles.to_pickle("bar_werkdocument.pkl")

pd.set_option("display.width", 240, "display.max_colwidth", 40)
print("=== verdeling van het advies (Bartogi NL) ===")
nl = alles[alles.shop == "NL"]
g = nl.groupby("advies").agg(artikelen=("artikel", "count"), stuks=("stuks", "sum"),
                             omzet=("bruto", "sum"), tekort=("tekort", "sum")).reset_index()
g["aandeel omzet%"] = g.omzet / nl.bruto.sum() * 100
print(g.sort_values("tekort", ascending=False).to_string(
    index=False, float_format=lambda v: f"{v:,.1f}"))

print("\n=== voorbeeld: de tien grootste tekorten met hun bodemprijs (NL) ===")
t = nl.sort_values("tekort", ascending=False).head(10)
print(t[["merk", "artikel", "stuks", "voorraad", "voorraaddekking mnd", "prijs nu incl",
         "vanprijs incl", "kostprijs", "retour%", "marge%", "bodemprijs incl",
         "verhoging nodig", "advies"]].to_string(index=False, float_format=lambda v: f"{v:,.1f}"))
