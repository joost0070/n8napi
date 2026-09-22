"""Marge per merk bij Bartogi NL en DE, uit de orderregels.

Onafhankelijk van Shopify's gross_profit (die pas vanaf juni gevuld is) en van
de MT-rapportage (waar de inkoopkosten pas vanaf week 32 echt zijn).
"""
import pandas as pd
pd.set_option("display.width", 230, "display.max_colwidth", 26)

for sleutel, naam in (("bartogi_nl", "Bartogi NL"), ("bartogi_de", "Bartogi DE")):
    d = pd.read_pickle(f"bar_regels_{sleutel}.pkl")
    d["kosten"] = d.kostprijs * d.aantal
    d["korting_regel"] = d.bruto - d.netto
    d["geretourneerd"] = d.aantal - d.aantal_nu
    d["netto_na_retour"] = d.netto * d.aantal_nu / d.aantal.replace(0, 1)
    d["kosten_na_retour"] = d.kostprijs * d.aantal_nu
    dekking = (d.kostprijs > 0).mean() * 100
    omzetdekking = d[d.kostprijs > 0].netto.sum() / d.netto.sum() * 100

    print(f"\n{'='*105}\n=== {naam}: {len(d):,} regels, kostprijs bekend voor "
          f"{dekking:.0f}% van de regels en {omzetdekking:.0f}% van de omzet"
          .replace(",", "."))

    g = d[d.kostprijs > 0]
    tot_bruto, tot_netto, tot_kost = g.bruto.sum(), g.netto.sum(), g.kosten.sum()
    print(f"    bruto € {tot_bruto:,.0f} | na korting € {tot_netto:,.0f} | "
          f"inkoop € {tot_kost:,.0f} | productmarge {(1-tot_kost/tot_netto)*100:.1f}%"
          .replace(",", "."))
    nr = g.netto_na_retour.sum(); kr = g.kosten_na_retour.sum()
    print(f"    na retour: omzet € {nr:,.0f} | inkoop € {kr:,.0f} | "
          f"marge {(1-kr/nr)*100:.1f}% | retour {(1-nr/tot_netto)*100:.1f}% van de omzet"
          .replace(",", "."))

    m = g.groupby("merk").agg(
        stuks=("aantal", "sum"), bruto=("bruto", "sum"), netto=("netto", "sum"),
        inkoop=("kosten", "sum"), retour_stuks=("geretourneerd", "sum"),
        netto_na=("netto_na_retour", "sum"), inkoop_na=("kosten_na_retour", "sum"),
    ).reset_index()
    m["korting%"] = (1 - m.netto / m.bruto) * 100
    m["productmarge%"] = (1 - m.inkoop / m.netto) * 100
    m["retour%"] = m.retour_stuks / m.stuks * 100
    m["marge na retour%"] = (1 - m.inkoop_na / m.netto_na) * 100
    m["aandeel omzet%"] = m.netto / m.netto.sum() * 100
    m["marge euro na retour"] = m.netto_na - m.inkoop_na
    m = m[m.netto > 500].sort_values("netto", ascending=False)
    print(m[["merk", "stuks", "netto", "aandeel omzet%", "korting%", "productmarge%",
             "retour%", "marge na retour%", "marge euro na retour"]].to_string(
        index=False, float_format=lambda v: f"{v:,.1f}"))
