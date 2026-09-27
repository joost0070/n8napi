"""Tofvel-deepdive: heeft de prijsverlaging van oktober 2025 winst opgeleverd?

Vergelijkt per maand seizoen 2024/25 (oude prijzen) met 2025/26 (nieuwe prijzen):
orders, paren, omzet excl. btw, bijdrage (na kostprijs, payment, verzending, retour),
advertentiekosten uit het KPI-rapport. Kostprijs = huidige unitCost voor beide jaren
(aanname: inkoopprijs niet wezenlijk veranderd). Schrijft tdd_prijs.pkl.
"""
import pandas as pd
from tdd_07_kern import PAYMENT, VERZEND_PER_ORDER

FAM = r"^(Mula Lungta|Mula|Rabara Maha|Rabara|Slipa Maha|Slipa|Luna Kids|Celsi|Sundara)"


def laad(s):
    delen = []
    for achter in ["_2425", ""]:
        o = pd.read_pickle(f"tdd_orders_{s}{achter}.pkl")
        r = pd.read_pickle(f"tdd_regels_{s}{achter}.pkl")
        o = o[o.bron_kanaal.eq("web")].copy()
        o["exbtw"] = ((o.totaal - o.btw) / o.totaal).where(o.totaal > 0, 1.0)
        r = r.merge(o[["order", "exbtw", "terugbetaald", "terug_verzend", "verzend"]], on="order")
        delen.append(r)
    r = pd.concat(delen).drop_duplicates(["order", "sku", "aantal", "netto"])
    r["d"] = r.datum.str[:10]
    r["maand"] = r.d.str[:7]
    return r


if __name__ == "__main__":
    kosten = pd.read_pickle("tdd_advertentie_week.pkl")
    uit = []
    for s in ["tofvel_nl", "tofvel_de"]:
        r = laad(s)
        # kostprijs voor 2024/25-regels: huidige unitCost per sku, anders per familie
        kp = r.dropna(subset=["kostprijs"]).groupby("sku").kostprijs.median()
        r["kostprijs"] = r.kostprijs.fillna(r.sku.map(kp))
        r["fam"] = r["product"].str.extract(FAM)[0].fillna("Overig")
        r["kostprijs"] = r.kostprijs.fillna(r.groupby("fam").kostprijs.transform("median"))
        r["netto_ex"] = r.netto * r.exbtw
        r["retour_ex"] = r.retour_bedrag * r.exbtw
        per_order = r.groupby("order").agg(maand=("maand", "first"), exbtw=("exbtw", "first"),
                                           terug=("terugbetaald", "first"),
                                           tv=("terug_verzend", "first"),
                                           verzend=("verzend", "first"),
                                           netto_ex=("netto_ex", "sum"),
                                           bruto_ex=("netto_ex", "sum")).reset_index()
        per_order["geld_terug_ex"] = (per_order.terug - per_order.tv) * per_order.exbtw
        # kostprijs: alleen teruggekomen stuks (refund én omruil) gaan weer op voorraad
        r["kost_netto"] = r.kostprijs * (r.aantal - r.retour_aantal)
        m = r.groupby("maand").agg(paren=("aantal", "sum"), kost=("kost_netto", "sum"),
                                   stukprijs=("stukprijs", "mean")).join(
            per_order.groupby("maand").agg(orders=("order", "count"),
                                           omzet_ex=("netto_ex", "sum"),
                                           terug_ex=("geld_terug_ex", "sum"),
                                           verzend_ex=("verzend", "sum")))
        m["bijdrage"] = (m.omzet_ex - m.terug_ex + m.verzend_ex / 1.21 - m.kost
                         - PAYMENT[s] * m.omzet_ex - VERZEND_PER_ORDER[s] * m.orders)
        a = kosten[kosten.shop == s].copy()
        # ISO-week naar maand (maandag van de week)
        a["maand"] = pd.to_datetime(a.jaar.astype(str) + a.week.astype(str).str.zfill(2) + "1",
                                    format="%G%V%u", errors="coerce").dt.strftime("%Y-%m")
        m = m.join(a.groupby("maand").kosten.sum().rename("advertentie")).fillna({"advertentie": 0})
        m["winst_na_adv"] = m.bijdrage - m.advertentie
        m["shop"] = s
        uit.append(m.reset_index())
        # familie x seizoen
        r["seizoen"] = r.d.map(lambda d: "piek 24/25" if "2024-10-01" <= d <= "2025-01-31"
                               else ("piek 25/26" if "2025-10-01" <= d <= "2026-01-31" else None))
        f = r.dropna(subset=["seizoen"]).groupby(["fam", "seizoen"]).agg(
            paren=("aantal", "sum"), prijs=("stukprijs", "median"),
            kost=("kostprijs", "median")).unstack()
        pd.set_option("display.width", 250)
        print(s); print(f.round(1).to_string())
    res = pd.concat(uit)
    res.to_pickle("tdd_prijs.pkl")
    print(res.round(0).to_string())
