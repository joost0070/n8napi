"""Wat is er in oktober t/m december nog te verdienen?

Vooruitkijkend, niet terugkijkend: per artikel de verwachte vraag van dit
kwartaal, begrensd door de voorraad, tegen het verschil tussen de huidige prijs
en de bodemprijs.
"""
import pandas as pd
pd.set_option("display.width", 235, "display.max_colwidth", 42)

BTW = {"NL": 1.21, "DE": 1.19}
d = pd.read_pickle("bar_werkdocument_seizoen.pkl").copy()
d["btw"] = d.shop.map(BTW)
d["verkoopbaar Q4"] = d[["verwacht okt-dec", "voorraad"]].min(axis=1)
d["prijsruimte"] = (d["bodemprijs incl"] - d["prijs nu incl"]).clip(lower=0) / d.btw
d["kans Q4"] = d["verkoopbaar Q4"] * d.prijsruimte
d["omzet Q4 nu"] = d["verkoopbaar Q4"] * d["prijs nu incl"] / d.btw
d.to_pickle("bar_q4.pkl")

for shopnaam in ("NL", "DE"):
    s = d[d.shop == shopnaam]
    print(f"\n{'='*104}\n=== Bartogi {shopnaam}: vooruitzicht oktober t/m december ===")
    print(f"  verwachte vraag        {s['verwacht okt-dec'].sum():>8,.0f} stuks".replace(",", "."))
    print(f"  daarvan op voorraad    {s['verkoopbaar Q4'].sum():>8,.0f} stuks".replace(",", "."))
    print(f"  omzet bij huidige prijs € {s['omzet Q4 nu'].sum():>9,.0f}".replace(",", "."))
    g = s.groupby("advies_seizoen").agg(
        artikelen=("artikel", "count"), voorraad=("voorraad", "sum"),
        vraag=("verwacht okt-dec", "sum"), verkoopbaar=("verkoopbaar Q4", "sum"),
        omzet_q4=("omzet Q4 nu", "sum"), kans=("kans Q4", "sum")).reset_index()
    print(g.sort_values("kans", ascending=False).to_string(
        index=False, float_format=lambda v: f"{v:,.0f}"))
    print(f"  prijsruimte die dit kwartaal te pakken is: € {s['kans Q4'].sum():,.0f}"
          .replace(",", "."))

nl = d[d.shop == "NL"]
print("\n\n=== Bartogi NL: de 15 artikelen met de grootste kans dit kwartaal ===")
t = nl.sort_values("kans Q4", ascending=False).head(15)
print(t[["merk", "artikel", "soort", "voorraad", "verwacht okt-dec", "verkoopbaar Q4",
         "prijs nu incl", "bodemprijs incl", "marge%", "kans Q4"]].to_string(
    index=False, float_format=lambda v: f"{v:,.1f}"))

print("\n\n=== wat er nu onnodig afgeprijsd staat en toch niet verkoopt ===")
buiten = nl[nl.advies_seizoen.str.startswith("buiten seizoen")]
print(f"  {len(buiten):,} artikelen, {buiten.voorraad.sum():,.0f} stuks voorraad"
      .replace(",", "."))
print(f"  verwachte vraag dit kwartaal: {buiten['verwacht okt-dec'].sum():,.0f} stuks "
      f"({buiten['verwacht okt-dec'].sum()/buiten.voorraad.sum()*100:.1f}% van de voorraad)"
      .replace(",", "."))
print(f"  gemiddelde afprijzing nu: {buiten['afprijzing%'].mean():.0f}%")
print(f"  die voorraad tegen adviesprijs waard: € {(buiten.voorraad * buiten['vanprijs incl'] / 1.21).sum():,.0f}"
      .replace(",", "."))
print(f"  tegen de huidige afgeprijsde prijs:   € {(buiten.voorraad * buiten['prijs nu incl'] / 1.21).sum():,.0f}"
      .replace(",", "."))
g2 = buiten.groupby("soort").agg(artikelen=("artikel","count"), voorraad=("voorraad","sum"),
                                 vraag=("verwacht okt-dec","sum"),
                                 afpr=("afprijzing%","mean")).reset_index()
print(g2.sort_values("voorraad", ascending=False).head(8).to_string(
    index=False, float_format=lambda v: f"{v:,.0f}"))
