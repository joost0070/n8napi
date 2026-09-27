"""Tofvel-deepdive: kerncijfers en winst per shop en periode, op orderniveau.

Bedragen excl. btw (per order omgerekend met btw/totaal). Kostprijs = huidige
unitCost van de variant (in Shopify pas sinds 2026 bij de verkoop vastgelegd, dus
ShopifyQL-COGS is voor oudere periodes leeg). Retouren = werkelijk terugbetaald geld
(excl. terugbetaalde verzendkosten) op orders uit de periode (cohort). Let op:
refundLineItems tellen ook omruilingen (Returnista) mee zonder dat er geld
teruggaat; die zitten daarom in stuks_retour maar niet in het retourbedrag.
Omruilorders (niet-web) kosten wel een verzending. Kostenregels volgens het MT-rapport:
payment % van bruto, verzendkosten per verzonden order; advertentie uit KPI-rapport.
Schrijft tdd_kern.pkl, tdd_regels_verrijkt.pkl, tdd_orders_verrijkt.pkl.
"""
import pandas as pd
from tdd_01_sessies import PERIODES, SHOPS

PAYMENT = {"tofvel_nl": 0.0070, "tofvel_de": 0.0504, "tofvel_en": 0.0328}  # MT YTD
VERZEND_PER_ORDER = {"tofvel_nl": 6.00, "tofvel_de": 6.50, "tofvel_en": 6.50}  # MT wk 38
ADV_WEKEN = {"P": (2026, 27, 39), "V": (2026, 14, 26), "J": (2025, 27, 39)}


def periode(d):
    for p, (van, tot) in PERIODES.items():
        if van <= d <= tot:
            return p
    return None


def laad(s):
    o = pd.read_pickle(f"tdd_orders_{s}.pkl")
    r = pd.read_pickle(f"tdd_regels_{s}.pkl")
    o["d"] = o.datum.str[:10]
    o["periode"] = o.d.map(periode)
    o["web"] = o.bron_kanaal.eq("web")
    o["exbtw"] = ((o.totaal - o.btw) / o.totaal).where(o.totaal > 0, 1.0)
    r = r.merge(o[["order", "d", "periode", "web", "exbtw", "klant"]], on="order")
    for k in ["bruto", "netto", "regelkorting", "retour_bedrag"]:
        r[k + "_ex"] = r[k] * r.exbtw
    r["kost"] = r.kostprijs.fillna(0) * r.aantal
    r["kost_retour"] = r.kostprijs.fillna(0) * r.retour_aantal
    r["adviesprijs_ex"] = r.adviesprijs * r.exbtw
    return o, r


def advertentie(s, p):
    a = pd.read_pickle("tdd_advertentie_week.pkl")
    jaar, w0, w1 = ADV_WEKEN[p]
    a = a[(a.shop == s) & (a.jaar == jaar) & a.week.between(w0, w1)]
    totaal = a.kosten.sum()
    if p == "P" and not (a.week == 39).any():  # week 39 nog niet in rapport: wk 38 x 6/7
        totaal += a[a.week == 38].kosten.sum() * 6 / 7
    return totaal


def kern(s, p, o, r):
    oo, rr = o[(o.periode == p) & o.web], r[(r.periode == p) & r.web]
    bruto = rr.bruto_ex.sum()
    korting = (rr.bruto_ex - rr.netto_ex).sum() + \
        (oo.korting * oo.exbtw).sum() - rr.regelkorting_ex.sum()
    netto_voor_retour = rr.netto_ex.sum() - ((oo.korting * oo.exbtw).sum() - rr.regelkorting_ex.sum())
    retour = ((oo.terugbetaald - oo.terug_verzend) * oo.exbtw).sum()
    omruil = o[(o.periode == p) & ~o.web]
    verzendopbrengst = ((oo.verzend - oo.terug_verzend) * oo.exbtw).sum()
    netto = netto_voor_retour - retour + verzendopbrengst
    inkoop = rr.kost.sum() - rr.kost_retour.sum()
    payment = PAYMENT[s] * bruto
    verzendkosten = VERZEND_PER_ORDER[s] * (len(oo) + len(omruil))
    adv = advertentie(s, p)
    winst = netto - inkoop - payment - verzendkosten - adv
    return {"shop": s, "periode": p, "orders": len(oo), "klanten": oo.klant.nunique(),
            "stuks": rr.aantal.sum(), "stuks_retour": rr.retour_aantal.sum(),
            "orders_retour": oo.terugbetaald.gt(0).sum(),
            "omruilorders": len(omruil), "retour_regelwaarde": rr.retour_bedrag_ex.sum(),
            "bruto": bruto, "korting": korting, "retour": retour,
            "verzendopbrengst": verzendopbrengst, "netto": netto, "inkoop": inkoop,
            "payment": payment, "verzendkosten": verzendkosten, "advertentie": adv,
            "winst": winst, "aov_netto": netto_voor_retour / max(len(oo), 1),
            "orders_met_korting": (oo.korting > 0).sum()}


if __name__ == "__main__":
    rijen, alle_r, alle_o = [], [], []
    for s in SHOPS:
        o, r = laad(s)
        o["shop"], r["shop"] = s, s
        alle_o.append(o)
        alle_r.append(r)
        for p in PERIODES:
            rijen.append(kern(s, p, o, r))
    k = pd.DataFrame(rijen)
    k["marge_%"] = 100 * k.winst / k.netto
    k["marge_%_bruto"] = 100 * k.winst / k.bruto  # zoals MT-rapport (brutowinst / bruto)
    k["retour_stuks_%"] = 100 * k.stuks_retour / k.stuks
    k["retour_orders_%"] = 100 * k.orders_retour / k.orders
    k["korting_orders_%"] = 100 * k.orders_met_korting / k.orders
    k["korting_%_bruto"] = 100 * k.korting / k.bruto
    k.to_pickle("tdd_kern.pkl")
    pd.concat(alle_r).to_pickle("tdd_regels_verrijkt.pkl")
    pd.concat(alle_o).to_pickle("tdd_orders_verrijkt.pkl")
    pd.set_option("display.width", 250)
    print(k.round(1).T.to_string())
