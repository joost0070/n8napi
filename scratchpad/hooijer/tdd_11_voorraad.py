"""Tofvel-deepdive: voorraad per product en maat tegen de vraag in de vorige piek.

Voorraad is gedeeld over NL/DE/EU (zelfde aantallen per SKU), dus één voorraad.
Piekvraag = verkochte stuks okt 2025 - jan 2026 over alle drie de shops.
Schrijft tdd_voorraad.pkl (per SKU) en tdd_voorraad_product.pkl.
"""
import pandas as pd

if __name__ == "__main__":
    a = pd.read_pickle("assortiment_tofvel_nl.pkl")
    r = pd.read_pickle("tdd_regels_verrijkt.pkl")
    r = r[r.web]
    piek = r[(r.d >= "2025-10-01") & (r.d <= "2026-01-31")]
    vraag = piek.groupby("sku").aantal.sum().rename("piek_stuks")
    p_nu = r[r.periode == "P"].groupby("sku").aantal.sum().rename("stuks_P")
    v = a.merge(vraag, left_on="sku", right_index=True, how="left") \
         .merge(p_nu, left_on="sku", right_index=True, how="left").fillna(
             {"piek_stuks": 0, "stuks_P": 0})
    # weken dekking bij piektempo (17,4 weken in okt-jan)
    v["piek_per_week"] = v.piek_stuks / 17.4
    v["weken_dekking"] = v.voorraad / v.piek_per_week.where(v.piek_per_week > 0)
    v.to_pickle("tdd_voorraad.pkl")
    prod = v.groupby(["handle", "titel"]).agg(
        prijs=("prijs", "median"), maten=("maat", "count"),
        maten_op_voorraad=("voorraad", lambda x: (x > 0).sum()),
        voorraad=("voorraad", "sum"), piek_stuks=("piek_stuks", "sum"),
        stuks_P=("stuks_P", "sum")).reset_index()
    # aandeel van de piekvraag dat valt op maten die nu op 0 staan
    nul = v[v.voorraad <= 0].groupby("handle").piek_stuks.sum()
    prod["piekvraag_op_uitverkochte_maten"] = prod.handle.map(nul).fillna(0)
    prod["dekking_%"] = 100 * prod.maten_op_voorraad / prod.maten
    prod.to_pickle("tdd_voorraad_product.pkl")
    pd.set_option("display.width", 250)
    pd.set_option("display.max_colwidth", 45)
    print(prod.sort_values("piek_stuks", ascending=False).round(1).to_string())
    print("\nTotaal piekvraag:", v.piek_stuks.sum(), " waarvan op maten met voorraad 0:",
          v[v.voorraad <= 0].piek_stuks.sum())
