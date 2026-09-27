"""Tofvel maatadvies per model: retour per maat (Shopify) en redenen apart (Returnista).

Retour% per model en maat: Shopify-orders okt 2024 - aug 2026 (NL+DE, web), geretourneerde
paren incl. omruil. Redenen: Returnista jan-sep 2026, 'Fit not as expected' en 'Quality'
opgesplitst op basis van de toelichting van de klant. Schrijft tdd_maatadvies.pkl.
"""
import re
import pandas as pd
from tdd_18_omruil import model, maat

CATS = [
    ("Links/rechts verschilt", r"linker|rechter|ene slof|1 slof|links en rechts|één slof"),
    ("Instap te krap / hoge wreef", r"wreef|instap|opening|öffnung|kom .*niet in|kom er niet|niet in de|"
                                     r"niet aan|aan te trekken|aantrekken|aan te doen|schoenlepel|"
                                     r"hiel niet in|aankrijg|niet in komen|lastig in|moeilijk in|"
                                     r"moeilijk om aan|zeer moeilijk|te hoge\) slof|hoger model nodig"),
    ("Te smal (breedte)", r"te smal|smalle leest|leest is .*smal|brede voet|breed voor deze|"
                          r"te breed voor deze|bekneld|te strak|zit te strak|wide feet|te small"),
    ("Te wijd / hiel slipt eruit", r"slip|zwem|te los|veel te breed|ruimer|nicht richtig|rutschen"),
    ("Zool / comfort / geluid", r"zool|sohle|stijf|stug|hard|steun|hobbel|bobbel|geluid|hak|warm|"
                                r"randje|niet vlak|loopt niet"),
]


def reden(r):
    tekst = str(r.return_reason_comment or "").lower()
    if tekst and tekst != "nan":
        for naam, patroon in CATS:
            if re.search(patroon, tekst):
                return naam
    basis = r["Return reasons description"]
    return {"Too small": "Te klein (lengte)", "Too large": "Te groot (lengte)",
            "Fit not as expected": "Pasvorm, niet toegelicht",
            "Quality not as expected": "Kwaliteit / overig"}.get(basis, "Kwaliteit / overig")


if __name__ == "__main__":
    ret = pd.read_pickle("tofvel_retouren.pkl")
    ret["reden_los"] = ret.apply(reden, axis=1)
    ret.to_pickle("tdd_retouren_los.pkl")
    red = pd.crosstab(ret.model, ret.reden_los)
    om = pd.read_pickle("tdd_omruil.pkl")
    omr = om[om.stap.abs() <= 3].groupby("model").stap.agg(
        omruil_n="count", maat_omhoog=lambda s: (s > 0).sum(), maat_omlaag=lambda s: (s < 0).sum())

    regels = []
    for s in ["tofvel_nl", "tofvel_de"]:
        for achter in ["", "_2425"]:
            r = pd.read_pickle(f"tdd_regels_{s}{achter}.pkl")
            o = pd.read_pickle(f"tdd_orders_{s}{achter}.pkl")
            r = r.merge(o[["order", "bron_kanaal"]], on="order")
            regels.append(r[r.bron_kanaal == "web"])
    r = pd.concat(regels).drop_duplicates(["order", "sku", "maat"])
    r = r[(r.datum.str[:10] >= "2024-10-01") & (r.datum.str[:10] <= "2026-08-31")]
    r["model"] = r["product"].map(model)
    r["maat_n"] = r.maat.map(maat)
    per_model = r.groupby("model").agg(verkocht=("aantal", "sum"), retour=("retour_aantal", "sum"))
    per_model["retour_%"] = 100 * per_model.retour / per_model.verkocht
    per_maat = r.groupby(["model", "maat_n"]).agg(verkocht=("aantal", "sum"),
                                                  retour=("retour_aantal", "sum")).reset_index()
    per_maat["retour_%"] = 100 * per_maat.retour / per_maat.verkocht
    aandeel = red.div(red.sum(axis=1), axis=0) * 100
    tab = per_model.join(red.sum(axis=1).rename("returnista_n")).join(aandeel.round(0)).join(omr)
    pd.to_pickle({"model": tab, "maat": per_maat, "redenen_n": red}, "tdd_maatadvies.pkl")
    pd.set_option("display.width", 300)
    print(tab.round(1).T.to_string())
    for m in ["Mula", "Rabara", "Rabara Maha", "Slipa Maha", "Slipa", "Luna Kids"]:
        x = per_maat[(per_maat.model == m) & (per_maat.verkocht >= 20)]
        print(m, x[["maat_n", "verkocht", "retour_%"]].round(1).values.tolist())
