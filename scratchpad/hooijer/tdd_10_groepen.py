"""Tofvel-deepdive: winst per order, uitgesplitst naar nieuw/terugkerend en kanaal.

Winst per order = netto regels excl. btw - terugbetaald + verzendopbrengst - kostprijs
(teruggekomen stuks weer op voorraad) - payment - verzendkosten. Advertentie niet per
order toe te rekenen (Google Ads-klikken zijn niet te scheiden van organisch).
Schrijft tdd_orderwinst.pkl.
"""
import pandas as pd
from tdd_07_kern import PAYMENT, VERZEND_PER_ORDER
from tdd_09_klanten import orderkanaal

if __name__ == "__main__":
    o = pd.read_pickle("tdd_orders_verrijkt.pkl")
    r = pd.read_pickle("tdd_regels_verrijkt.pkl")
    kl = pd.read_pickle("tdd_orders_klant.pkl")[["shop", "order", "volgnr"]]
    o = o[o.web & o.periode.notna()].merge(kl, on=["shop", "order"], how="left")
    o["groep"] = o.volgnr.map(lambda v: "Nieuw" if v == 1 else
                              ("Terugkerend" if v > 1 else "Gast / onbekend"))
    reg = r[r.web].groupby(["shop", "order"]).agg(
        netto_ex=("netto_ex", "sum"), bruto_ex=("bruto_ex", "sum"), kost=("kost", "sum"),
        kost_retour=("kost_retour", "sum"), stuks=("aantal", "sum"),
        stuks_retour=("retour_aantal", "sum")).reset_index()
    o = o.merge(reg, on=["shop", "order"], how="left")
    o["korting_ex"] = (o.korting * o.exbtw).clip(lower=0)
    o["terug_ex"] = ((o.terugbetaald - o.terug_verzend) * o.exbtw)
    o["verzend_ex"] = ((o.verzend - o.terug_verzend) * o.exbtw)
    o["winst"] = (o.netto_ex - o.terug_ex + o.verzend_ex - (o.kost - o.kost_retour)
                  - o.shop.map(PAYMENT) * o.bruto_ex - o.shop.map(VERZEND_PER_ORDER))
    o["kanaal"] = o.apply(orderkanaal, axis=1)
    o.to_pickle("tdd_orderwinst.pkl")

    def samen(g):
        return pd.Series({
            "orders": len(g), "aandeel_orders_%": 0, "omzet_ex": g.netto_ex.sum(),
            "aov_ex": g.netto_ex.mean(), "stuks_per_order": g.stuks.mean(),
            "met_korting_%": 100 * (g.korting > 0).mean(),
            "retour_stuks_%": 100 * g.stuks_retour.sum() / g.stuks.sum(),
            "geld_terug_%": 100 * g.terug_ex.sum() / g.netto_ex.sum(),
            "winst": g.winst.sum(), "winst_per_order": g.winst.mean(),
            "marge_%": 100 * g.winst.sum() / (g.netto_ex.sum() + g.verzend_ex.sum())})

    pd.set_option("display.width", 250)
    for dim in ["groep", "kanaal"]:
        t = o.groupby(["shop", "periode", dim]).apply(samen).reset_index()
        t["aandeel_orders_%"] = 100 * t.orders / t.groupby(["shop", "periode"]).orders.transform("sum")
        print(t[t.shop != "tofvel_en"].round(1).to_string())
    # kanaal x groep in P
    p = o[(o.periode == "P") & (o.shop == "tofvel_nl")]
    print(pd.crosstab(p.kanaal, p.groep, margins=True))
