"""Realistische Q4-kans: de prijs mag nooit boven de eigen adviesprijs uit."""
import pandas as pd
pd.set_option("display.width", 235, "display.max_colwidth", 44)

d = pd.read_pickle("bar_q4.pkl").copy()
d["doelprijs"] = d[["bodemprijs incl", "vanprijs incl"]].min(axis=1)
d.loc[d["vanprijs incl"] <= 0, "doelprijs"] = d["bodemprijs incl"]
d["doelprijs"] = d[["doelprijs", "prijs nu incl"]].max(axis=1)
d["verhoging"] = d.doelprijs - d["prijs nu incl"]
d["kans realistisch"] = d["verkoopbaar Q4"] * d.verhoging / d.btw
d["onder kostprijs"] = d["prijs nu incl"] / d.btw < d.kostprijs

for shopnaam in ("NL", "DE"):
    s = d[d.shop == shopnaam]
    haalbaar = s[s["kans realistisch"] > 0]
    print(f"\n=== Bartogi {shopnaam}: realistische kans oktober t/m december ===")
    print(f"  theoretische prijsruimte (tot bodemprijs) : € {s['kans Q4'].sum():>8,.0f}"
          .replace(",", "."))
    print(f"  begrensd op de eigen adviesprijs          : € {s['kans realistisch'].sum():>8,.0f}"
          .replace(",", "."))
    print(f"  aantal artikelen met ruimte               : {len(haalbaar):>8,}".replace(",", "."))
    print(f"  Q4-omzet bij de huidige prijs             : € {s['omzet Q4 nu'].sum():>8,.0f}"
          .replace(",", "."))
    if s['omzet Q4 nu'].sum():
        print(f"  dat is een margeverbetering van             {s['kans realistisch'].sum()/s['omzet Q4 nu'].sum()*100:>7.1f} "
              f"procentpunt op de Q4-omzet")

nl = d[d.shop == "NL"]
print("\n\n=== Bartogi NL: waar de realistische kans zit ===")
g = nl[nl["kans realistisch"] > 0].groupby("soort").agg(
    artikelen=("artikel", "count"), verkoopbaar=("verkoopbaar Q4", "sum"),
    gem_verhoging=("verhoging", "mean"), kans=("kans realistisch", "sum")).reset_index()
print(g.sort_values("kans", ascending=False).to_string(
    index=False, float_format=lambda v: f"{v:,.1f}"))

print("\n=== de 15 grootste, met een prijs die binnen de adviesprijs blijft ===")
t = nl[nl["kans realistisch"] > 0].sort_values("kans realistisch", ascending=False).head(15)
print(t[["merk", "artikel", "soort", "voorraad", "verkoopbaar Q4", "prijs nu incl",
         "doelprijs", "vanprijs incl", "marge%", "kans realistisch"]].to_string(
    index=False, float_format=lambda v: f"{v:,.1f}"))

print("\n\n=== artikelen die onder de kostprijs verkocht worden ===")
ok = nl[nl["onder kostprijs"]]
print(f"  {len(ok):,} artikelen, {ok.stuks.sum():,.0f} stuks verkocht dit jaar, "
      f"{ok.voorraad.sum():,.0f} nog op voorraad".replace(",", "."))
print(f"  omzet € {ok.bruto.sum():,.0f}, brutowinst € {ok.brutowinst.sum():,.0f}"
      .replace(",", "."))
print(ok.sort_values("stuks", ascending=False).head(10)[
    ["merk", "artikel", "stuks", "voorraad", "prijs nu incl", "kostprijs", "vanprijs incl",
     "marge%"]].to_string(index=False, float_format=lambda v: f"{v:,.1f}"))
d.to_pickle("bar_q4_realistisch.pkl")
