"""Hoe verhoudt Bartogi NL zich tot alle andere webshops? Bron: MT-rapportage YTD."""
import pandas as pd
pd.set_option("display.width", 220)

d = pd.read_excel("bartogi/2026 _ MT-rapportage _ Omzet en kosten Week en YTD (3).xlsx",
                  sheet_name="Week + YTD", header=None).iloc[32:55]
k = {1:"kanaal",4:"bruto",6:"korting",8:"retour",10:"verzendopbr",11:"netto",
     13:"inkoop",15:"payment",17:"verzend",19:"advertentie",24:"winst",25:"marge"}
df = pd.DataFrame({n: d[j] for j, n in k.items()})
df = df[df.kanaal.notna() & (df.kanaal != "Webshop/ kanaal")]
for c in df.columns[1:]:
    df[c] = pd.to_numeric(df[c], errors="coerce")
df = df[df.bruto > 20000]

WEBSHOPS = ["Bartogi NL","Bartogi DE","Lazamani NL","Lazamani DE","Lazamani COM","Tofvel NL",
            "Tofvel DE","Sockwell NL","Sockwell DE","Sockwell EU/FR/IT/ES","HEYDUDE NL",
            "Toni Pons NL","Keenfootwear.nl","Hunterboots.nl","JanJansen NL"]
w = df[df.kanaal.isin(WEBSHOPS)].copy()
for naam, kol in (("advertentie%","advertentie"),("inkoop%","inkoop"),
                  ("korting%","korting"),("retour%","retour"),("verzend%","verzend")):
    w[naam] = w[kol] / w.bruto * 100
w["marge%"] = w.marge * 100
w["verzendverlies%"] = (w.verzend - w.verzendopbr) / w.bruto * 100

print("=== alle webshops, kosten als % van de eigen bruto omzet (MT-rapportage YTD) ===")
print(w[["kanaal","bruto","korting%","retour%","inkoop%","verzendverlies%","advertentie%",
         "marge%"]].sort_values("advertentie%", ascending=False).to_string(
    index=False, float_format=lambda v: f"{v:,.1f}"))

med = w.advertentie.sum() / w.bruto.sum() * 100
print(f"\n  advertentie over alle webshops samen: {med:.2f}% van de bruto omzet")
print(f"  Bartogi NL: {w[w.kanaal=='Bartogi NL'].advertentie.iloc[0]/w[w.kanaal=='Bartogi NL'].bruto.iloc[0]*100:.2f}%"
      f"  -> hoogste van alle webshops")

nl = w[w.kanaal == "Bartogi NL"].iloc[0]
for doel, label in ((med, "portfoliogemiddelde"), (12.0, "12%"), (8.78, "DE-niveau")):
    besp = nl.advertentie - doel/100 * nl.bruto
    print(f"  naar {label:<20} ({doel:5.2f}%): € {besp:>8,.0f} erbij -> marge "
          f"{(nl.marge*nl.bruto + besp)/nl.bruto*100:5.2f}%".replace(",", "."))

print("\n=== ranglijst inkoopkosten (hoe hoger, hoe lager de productmarge) ===")
print(w[["kanaal","inkoop%","marge%"]].sort_values("inkoop%", ascending=False).head(8)
      .to_string(index=False, float_format=lambda v: f"{v:,.1f}"))
