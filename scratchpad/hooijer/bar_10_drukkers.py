"""Welke producten drukken de marge, en hoeveel?"""
import pandas as pd
pd.set_option("display.width", 235, "display.max_colwidth", 40)

d = pd.read_pickle("bar_artikelen.pkl")
nl = d[d.shop == "bartogi_nl"].copy()

# per model samenvatten (alle maten van hetzelfde artikel samen)
m = nl.groupby(["merk", "artikel"], dropna=False).agg(
    stuks=("stuks", "sum"), retour_stuks=("stuks_retour", "sum"),
    lijst=("lijst", "sum"), bruto=("bruto", "sum"), afprijzing=("afprijzing", "sum"),
    omzet=("omzet", "sum"), inkoop=("inkoop", "sum"), retour=("retour", "sum"),
    advertentie=("advertentie", "sum"), verzendkosten=("verzendkosten", "sum"),
    brutowinst=("brutowinst", "sum"), tekort=("tekort tot 20%", "sum"),
    prijs=("prijs nu", "median"), kostprijs=("kostprijs", "median")).reset_index()
m["marge%"] = m.brutowinst / m.bruto * 100
m["afprijzing%"] = m.afprijzing / m.lijst * 100
m["retour%"] = m.retour_stuks / m.stuks * 100

print("=== de 20 artikelen die de marge het hardst drukken ===")
print("    (tekort = wat er ontbrak om op 20% brutowinstmarge uit te komen)\n")
top = m.sort_values("tekort", ascending=False).head(20)
print(top[["merk", "artikel", "stuks", "bruto", "afprijzing%", "retour%", "marge%",
           "tekort"]].to_string(index=False, float_format=lambda v: f"{v:,.1f}"))
print(f"\n  deze 20 samen: € {top.tekort.sum():,.0f} tekort op een totaal tekort van "
      f"€ {m.tekort.sum():,.0f}  ({top.tekort.sum()/m.tekort.sum()*100:.0f}%)"
      .replace(",", "."))

print("\n\n=== waar komt het tekort vandaan? drie oorzaken uit elkaar getrokken ===")
tot_lijst, tot_bruto = m.lijst.sum(), m.bruto.sum()
posten = {
    "afprijzing (prijs onder vanprijs)": m.afprijzing.sum(),
    "retouren (omzet die terugkwam)": m.retour.sum(),
    "advertentiekosten": m.advertentie.sum(),
    "verzendkosten minus opbrengsten": m.verzendkosten.sum() - nl.verzendopbrengst.sum(),
}
for naam, v in sorted(posten.items(), key=lambda t: -t[1]):
    print(f"  {naam:<38} € {v:>9,.0f}   {v/tot_bruto*100:>5.1f}% van de bruto omzet"
          .replace(",", "."))

print("\n\n=== retouren: welke artikelen kosten het meest? ===")
r = m[m.stuks >= 10].copy()
r["retourkosten"] = r.retour - r.retour / r.omzet.replace(0, 1) * 0  # omzet die wegviel
r = r.sort_values("retour", ascending=False).head(15)
print(r[["merk", "artikel", "stuks", "retour_stuks", "retour%", "retour", "marge%"]]
      .to_string(index=False, float_format=lambda v: f"{v:,.1f}"))
print(f"\n  alle retouren samen: € {m.retour.sum():,.0f} aan omzet die terugkwam "
      f"({m.retour.sum()/tot_bruto*100:.1f}% van de bruto omzet)".replace(",", "."))

print("\n\n=== hoeveel van de omzet haalt het doel van 20%? ===")
schijf = pd.cut(m["marge%"], [-1e9, -20, 0, 10, 20, 30, 1e9],
                labels=["onder -20%", "-20% tot 0%", "0-10%", "10-20%", "20-30%", "boven 30%"])
s = m.groupby(schijf, observed=True).agg(
    artikelen=("artikel", "count"), stuks=("stuks", "sum"), bruto=("bruto", "sum"),
    brutowinst=("brutowinst", "sum")).reset_index()
s["aandeel omzet%"] = s.bruto / tot_bruto * 100
print(s.to_string(index=False, float_format=lambda v: f"{v:,.1f}"))
onder = m[m["marge%"] < 20]
print(f"\n  {len(onder):,} van de {len(m):,} artikelen zitten onder de 20% "
      f"({onder.bruto.sum()/tot_bruto*100:.0f}% van de omzet), samen € {onder.tekort.sum():,.0f} tekort"
      .replace(",", "."))
m.to_pickle("bar_modellen_nl.pkl")
