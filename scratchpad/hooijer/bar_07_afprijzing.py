"""Afprijzing als eigen post: hoeveel marge is er weggegeven vóór de kassa?

De afprijzing zit in de verkoopprijs zelf (price tegen compareAtPrice), niet in
de kortingregel. Daardoor verschijnt hij in de rapportage als een hoog
inkooppercentage in plaats van als korting.

Twee correcties ten opzichte van mijn eerdere berekening:
  - Shopify-orderregels staan inclusief btw, de MT-rapportage exclusief.
    Alle regelbedragen worden door 1,21 (NL) respectievelijk 1,19 (DE) gedeeld.
  - de vanprijs (compareAtPrice) komt uit het assortiment en wordt op sku gekoppeld.
"""
import pandas as pd
pd.set_option("display.width", 230, "display.max_colwidth", 26)

BTW = {"bartogi_nl": 1.21, "bartogi_de": 1.19}

for sleutel, naam in (("bartogi_nl", "Bartogi NL"), ("bartogi_de", "Bartogi DE")):
    btw = BTW[sleutel]
    r = pd.read_pickle(f"bar_regels_{sleutel}.pkl").copy()
    a = pd.read_pickle(f"assortiment_{sleutel}.pkl")
    van = a[a.vanprijs > 0].groupby("sku").vanprijs.median()
    r["vanprijs"] = r.sku.map(van)

    # alles exclusief btw
    r["verkocht"] = r.netto / btw                     # werkelijk ontvangen, na kortingcode
    r["lijstprijs"] = (r.vanprijs.fillna(0) * r.aantal) / btw
    r.loc[r.lijstprijs < r.verkocht, "lijstprijs"] = r.verkocht   # geen vanprijs = geen afprijzing
    r["afprijzing"] = r.lijstprijs - r.verkocht
    r["inkoop"] = r.kostprijs * r.aantal

    # na retour
    deel = r.aantal_nu / r.aantal.replace(0, 1)
    for k in ("verkocht", "lijstprijs", "afprijzing"):
        r[f"{k}_na"] = r[k] * deel
    r["inkoop_na"] = r.kostprijs * r.aantal_nu

    v, l, af, ik = (r.verkocht_na.sum(), r.lijstprijs_na.sum(),
                    r.afprijzing_na.sum(), r.inkoop_na.sum())
    print(f"\n{'='*104}\n=== {naam}, 1 jan t/m 21 sep 2026, na retour, exclusief btw ===")
    print(f"  omzet tegen normale retailprijs   € {l:>10,.0f}   100,0%".replace(",", "."))
    print(f"  afprijzing (prijs onder vanprijs) € {-af:>10,.0f}   {-af/l*100:>5.1f}%"
          .replace(",", "."))
    print(f"  werkelijk ontvangen               € {v:>10,.0f}   {v/l*100:>5.1f}%"
          .replace(",", "."))
    print(f"  inkoopkosten                      € {-ik:>10,.0f}   {-ik/l*100:>5.1f}%"
          .replace(",", "."))
    print(f"  productmarge                      € {v-ik:>10,.0f}   {(v-ik)/l*100:>5.1f}%"
          .replace(",", "."))
    print(f"\n  marge als er niets was afgeprijsd : {(1-ik/l)*100:>5.1f}%")
    print(f"  marge zoals die nu is             : {(1-ik/v)*100:>5.1f}%")
    print(f"  verlies door afprijzing           : {(1-ik/l)*100-(1-ik/v)*100:>5.1f} procentpunt")
    print(f"  inkoop als % van de omzet: {ik/l*100:.1f}% zonder afprijzing, "
          f"{ik/v*100:.1f}% met afprijzing")

    afgeprijsd = r[r.afprijzing_na > 0.01]
    print(f"\n  aandeel omzet dat afgeprijsd is verkocht: "
          f"{afgeprijsd.verkocht_na.sum()/v*100:.1f}%")

    m = r.groupby("merk").agg(
        lijst=("lijstprijs_na", "sum"), afpr=("afprijzing_na", "sum"),
        verkocht=("verkocht_na", "sum"), inkoop=("inkoop_na", "sum")).reset_index()
    m = m[m.verkocht > 1000]
    m["afprijzing%"] = m.afpr / m.lijst * 100
    m["marge zonder afprijzing%"] = (1 - m.inkoop / m.lijst) * 100
    m["marge werkelijk%"] = (1 - m.inkoop / m.verkocht) * 100
    m["verlies pp"] = m["marge zonder afprijzing%"] - m["marge werkelijk%"]
    m["aandeel omzet%"] = m.verkocht / m.verkocht.sum() * 100
    m["afprijzing euro"] = m.afpr
    print(m[["merk", "aandeel omzet%", "afprijzing%", "marge zonder afprijzing%",
             "marge werkelijk%", "verlies pp", "afprijzing euro"]].sort_values(
        "afprijzing euro", ascending=False).to_string(
        index=False, float_format=lambda v: f"{v:,.1f}"))
    if sleutel == "bartogi_nl":
        r.to_pickle("bar_regels_nl_afprijzing.pkl")
