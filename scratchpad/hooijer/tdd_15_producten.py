"""Tofvel-deepdive: producten op winst vs omzet, etalage-producten, retourkosten.

Productpagina-bezoeken zitten niet in ShopifyQL; als benadering dienen sessies die
op de productpagina binnenkomen (landing_page_path, alleen afzetlanden).
Retourkosten per paar: omruil = extra heen- en terugzending (2 x verzendkosten);
terugbetaling = gemiste bijdrage (netto - kostprijs) + verloren heenzending.
Schrijft tdd_producten.pkl en tdd_etalage.pkl.
"""
import pandas as pd
from tdd_07_kern import VERZEND_PER_ORDER
from tdd_08_trechter import echt

if __name__ == "__main__":
    r = pd.read_pickle("tdd_regels_verrijkt.pkl")
    o = pd.read_pickle("tdd_orders_verrijkt.pkl")[["shop", "order", "terugbetaald"]]
    r = r[r.web & (r.periode == "P")].merge(o, on=["shop", "order"])
    r["verzend"] = r.shop.map(VERZEND_PER_ORDER)
    r["geld_terug"] = r.terugbetaald > 0
    r["stuk_netto"] = r.netto_ex / r.aantal
    r["retourkosten"] = r.retour_aantal * (
        (r.stuk_netto - r.kostprijs + r.verzend).where(r.geld_terug, 2 * r.verzend))
    r["winst"] = r.netto_ex - r.kost - r.retour_aantal * (r.stuk_netto - r.kostprijs).where(
        r.geld_terug, 0) - r.verzend * r.aantal / r.groupby(["shop", "order"]).aantal.transform("sum")
    p = r.groupby("product").agg(stuks=("aantal", "sum"), omzet_ex=("netto_ex", "sum"),
                                 winst=("winst", "sum"), retour=("retour_aantal", "sum"),
                                 retourkosten=("retourkosten", "sum")).reset_index()
    p["retour_%"] = 100 * p.retour / p.stuks
    p["rang_omzet"] = p.omzet_ex.rank(ascending=False).astype(int)
    p["rang_winst"] = p.winst.rank(ascending=False).astype(int)
    p.to_pickle("tdd_producten.pkl")

    d = pd.read_pickle("tdd_sessies_land.pkl")
    l = echt(d[(d.dim == "landing") & (d.periode == "P")]).copy()
    l = l[l.landing_page_path.str.startswith("/products/", na=False)]
    l["handle"] = l.landing_page_path.str.split("/").str[2]
    l = l.groupby("handle")[["sessions", "sessions_with_cart_additions",
                             "sessions_that_completed_checkout"]].sum()
    vp = pd.read_pickle("tdd_voorraad_product.pkl").set_index("handle")
    e = l.join(vp[["titel", "prijs", "maten", "maten_op_voorraad", "voorraad", "stuks_P"]], how="left")
    e["stuks_P"] = e.stuks_P.fillna(0)
    e.to_pickle("tdd_etalage.pkl")
    pd.set_option("display.width", 250)
    print(p.sort_values("winst", ascending=False).head(22).round(1).to_string())
    print(e.sort_values("sessions", ascending=False).head(30).to_string())
    print("\nZonder verkoop in P:", e[e.stuks_P == 0].sessions.sum(), "landingssessies op",
          (e.stuks_P == 0).sum(), "producten; volledig uitverkocht:",
          e[(e.stuks_P == 0) & (e.voorraad <= 0)].sessions.sum())
