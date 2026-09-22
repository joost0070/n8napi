"""De winst-en-verliesrekening met afprijzing als eigen post, plus scenario's."""
import pandas as pd
pd.set_option("display.width", 200)

r = pd.read_pickle("bar_regels_nl_afprijzing.pkl")
LIJST, AFPR, ONTV, INKOOP = (r.lijstprijs_na.sum(), r.afprijzing_na.sum(),
                             r.verkocht_na.sum(), r.inkoop_na.sum())
VERZ_OPBR, PAYMENT, VERZEND, ADV = 5403.24, 1464.50, 19608.00, 39286.05
BRUTO_MT = 187792.86

print("=== Bartogi NL: winst-en-verliesrekening met afprijzing zichtbaar ===")
print("    (1 jan t/m 21 sep 2026, na retour, exclusief btw)\n")
regels = [("waarde tegen normale retailprijs", LIJST, +1),
          ("afprijzing", -AFPR, -1),
          ("= werkelijk ontvangen voor de artikelen", ONTV, 0),
          ("inkoopkosten", -INKOOP, -1),
          ("= productmarge", ONTV - INKOOP, 0),
          ("verzendopbrengsten", VERZ_OPBR, +1),
          ("verzendkosten", -VERZEND, -1),
          ("payment costs", -PAYMENT, -1),
          ("advertentiekosten", -ADV, -1)]
winst = ONTV - INKOOP + VERZ_OPBR - VERZEND - PAYMENT - ADV
for naam, bedrag, soort in regels:
    streep = "  " if soort == 0 else "    "
    print(f"{streep}{naam:<42} € {bedrag:>10,.0f}   {bedrag/LIJST*100:>6.1f}%"
          .replace(",", "."))
print(f"  {'= brutowinst':<42} € {winst:>10,.0f}   {winst/LIJST*100:>6.1f}%".replace(",", "."))
print(f"\n  afprijzing is € {AFPR:,.0f} — dat is {AFPR/ADV:.1f}x de advertentiekosten "
      f"en {AFPR/INKOOP:.2f}x de inkoopkosten".replace(",", "."))

print("\n\n=== wat gebeurt er als er minder wordt afgeprijsd? ===")
print("    (zelfde verkochte aantallen, alleen een hogere prijs)\n")
huidig = AFPR / LIJST * 100
for doel in (huidig, 37.1, 35, 30, 25):
    nieuwe_afpr = doel / 100 * LIJST
    extra = AFPR - nieuwe_afpr
    nieuwe_winst = winst + extra
    nieuwe_bruto = BRUTO_MT + extra
    label = "nu" if abs(doel - huidig) < 0.1 else ("DE-niveau" if doel == 37.1 else "")
    print(f"  afprijzing {doel:>4.1f}% {label:<10} € {extra:>8,.0f} erbij  ->  "
          f"brutowinst € {nieuwe_winst:>8,.0f}  marge {nieuwe_winst/nieuwe_bruto*100:>5.1f}%"
          .replace(",", "."))

print("\n\n=== waarom wordt er afgeprijsd? voorraad tegenover verkoop ===")
x = pd.ExcelFile("/root/.claude/uploads/1e31e512-cd0c-5072-be78-df4a915d8c94/"
                 "da359934-inkoopprijzen_per_merk.xlsx")
o = x.parse("Overzicht", header=3).dropna(subset=["Merk"])
o = o[o.Merk != "Merk"]
for k in ("Voorraad stuks", "Inkoopwaarde", "Verkocht YTD"):
    o[k] = pd.to_numeric(o[k], errors="coerce")
o["jaren voorraad"] = o["Voorraad stuks"] / o["Verkocht YTD"].replace(0, pd.NA) * 0.72
print(o[["Merk", "Voorraad stuks", "Inkoopwaarde", "Verkocht YTD", "jaren voorraad"]]
      .sort_values("Inkoopwaarde", ascending=False).head(12).to_string(
    index=False, float_format=lambda v: f"{v:,.1f}"))
print(f"\n  totaal voorraad: {o['Voorraad stuks'].sum():,.0f} stuks, "
      f"inkoopwaarde € {o['Inkoopwaarde'].sum():,.0f}".replace(",", "."))
print(f"  verkocht YTD (marktplaatsen): {o['Verkocht YTD'].sum():,.0f} stuks"
      .replace(",", "."))
