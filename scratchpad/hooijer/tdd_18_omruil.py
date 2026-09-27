"""Tofvel maatadvies: welke kant gaan omruilingen op (maat groter/kleiner/andere kleur)?

Koppelt Returnista-omruilingen (orderregel + SKU) aan de omruilorder in Shopify
(bron = Returnista-app, zelfde klant, na de retourdatum, zelfde model).
Schrijft tdd_omruil.pkl.
"""
import re
import pandas as pd

FAM = r"^(Mula Lungta|Mula|Rabara Maha|Rabara|Slipa Maha|Slipa|Luna Kids|Celsi|Sundara)"
DUITS = {"Wollfilz-Hausschuhe": "Wolvilt Sloffen", "Wollfilz-Pantoffel": "Wolvilt Pantoffels"}


def model(titel):
    m = re.match(FAM, str(titel))
    return m.group(1) if m else None


def maat(x):
    try:
        return float(str(x).split()[0].replace(",", "."))
    except ValueError:
        return None


if __name__ == "__main__":
    ret = pd.read_pickle("tofvel_retouren.pkl")
    ret["sku"] = ret.SKU.astype(str).str.split(".").str[0].str.zfill(13)
    ret["d"] = ret["Created at"].astype(str).str[:10]
    regels, orders = [], []
    for s in ["tofvel_nl", "tofvel_de"]:
        for achter in ["", "_2425"]:
            r = pd.read_pickle(f"tdd_regels_{s}{achter}.pkl")
            o = pd.read_pickle(f"tdd_orders_{s}{achter}.pkl")
            regels.append(r.merge(o[["order", "klant", "bron_kanaal"]], on="order"))
    r = pd.concat(regels).drop_duplicates(["order", "sku", "maat"])
    r["sku"] = r.sku.astype(str).str.zfill(13)
    r["model"] = r["product"].map(model)
    r["maat_n"] = r.maat.map(maat)
    r["d"] = r.datum.str[:10]
    omruilorders = r[r.bron_kanaal != "web"]
    orig = ret.merge(r[["order", "sku", "klant", "maat_n", "product"]],
                     left_on=["Order number", "sku"], right_on=["order", "sku"], how="left")
    uit = []
    for _, x in orig[orig["Resolution type"] == "Exchange"].iterrows():
        kand = omruilorders[(omruilorders.klant == x.klant) & (omruilorders.d >= x.d)]
        kand = kand[kand.model == x.model]
        nieuw = kand.sort_values("d").head(1)
        rij = {"order": x["Order number"], "model": x.model, "reden": x["Return reasons description"],
               "maat_oud": x.maat_n, "product_oud": x["product"]}
        if len(nieuw):
            n = nieuw.iloc[0]
            rij.update({"maat_nieuw": n.maat_n, "product_nieuw": n["product"]})
        uit.append(rij)
    o = pd.DataFrame(uit)
    o["stap"] = o.maat_nieuw - o.maat_oud
    o.to_pickle("tdd_omruil.pkl")
    print(len(o), "omruilingen; gekoppeld:", o.maat_nieuw.notna().sum())
    print(pd.crosstab([o.model, o.reden], o.stap, margins=True))
