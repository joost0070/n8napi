"""KEEN NL: wat leveren de mogelijke ingrepen op in winst, niet in omzet?

Marge: Shopify geeft voor KEEN in juli 55,6% en in augustus 54,2% brutomarge op
netto-omzet. Dat zijn de enige twee maanden waarin de kostprijzen gevuld en
stabiel zijn. We rekenen behoudend met 54%.
"""
import pandas as pd
import sql

MARGE = 0.54
RETOURKOSTEN = 9.00     # retourzending, inspectie en herverpakken per pakket
MAANDEN = 6

basis = pd.read_pickle("nulmeting_v2.pkl")
k = basis[basis.sleutel == "keen_nl"].iloc[0]

SESSIES, AOV = k.sessions, k.AOV
AFREKEN, ORDER = k["afreken%"] / 100, k["order%"] / 100
print(f"Uitgangspunt KEEN NL, maart t/m augustus 2026")
print(f"  {SESSIES:,.0f} sessies, {k['wagen%']:.2f}% in de wagen, AOV € {AOV:.2f}"
      .replace(",", "."))
print(f"  van wagen naar afrekenen {AFREKEN*100:.1f}%, van afrekenen naar order "
      f"{ORDER*100:.1f}%")
print(f"  brutomarge {MARGE*100:.0f}%, retourpercentage {k['retour%']:.1f}%\n")


def trechterwinst(punten, naam):
    wagens = SESSIES * punten / 100
    orders = wagens * AFREKEN * ORDER
    omzet = orders * AOV
    winst = omzet * MARGE
    print(f"{naam}")
    print(f"  +{punten:.2f} procentpunt = {wagens:,.0f} extra winkelwagens, "
          f"{orders:,.0f} extra orders".replace(",", "."))
    print(f"  netto-omzet  € {omzet:>9,.0f} per half jaar   "
          f"(€ {omzet*2:>9,.0f} op jaarbasis)".replace(",", "."))
    print(f"  brutowinst   € {winst:>9,.0f} per half jaar   "
          f"(€ {winst*2:>9,.0f} op jaarbasis)\n".replace(",", "."))
    return winst


w1 = trechterwinst(1.00, "A. Eerste trechterstap +1 procentpunt (3,30% -> 4,30%)")
w2 = trechterwinst(1.05, "B. Naar het niveau dat bij KEEN's prijspunt hoort (4,35%)")
w3 = trechterwinst(5.71, "C. Naar het niveau van HEYDUDE (9,01%) - bovengrens, onrealistisch")

# ---- retouren
kop = sql.vraag("keen_nl", "FROM sales SHOW gross_sales, returns, orders "
                           "SINCE 2026-03-01 UNTIL 2026-08-31").iloc[0]
print("D. Retouren terugbrengen")
for punten in (2, 3, 5):
    minder_euro = kop.gross_sales * punten / 100
    pakketten = minder_euro / AOV
    winst = minder_euro * MARGE + pakketten * RETOURKOSTEN
    print(f"  -{punten} procentpunt ({k['retour%']:.1f}% -> {k['retour%']-punten:.1f}%): "
          f"€ {minder_euro:,.0f} minder retour, {pakketten:,.0f} pakketten minder"
          .replace(",", "."))
    print(f"     brutowinst € {winst:,.0f} per half jaar  (€ {winst*2:,.0f} op jaarbasis)"
          .replace(",", "."))

# ---- de drie damesmodellen met de hoogste retouren
print("\nE. Alleen de drie damesmodellen met de hoogste retouren naar shopgemiddelde")
p = sql.vraag("keen_nl", "FROM sales SHOW gross_sales, returns GROUP BY product_title "
                         "SINCE 2026-03-01 UNTIL 2026-08-31 ORDER BY returns ASC LIMIT 40")
p["retour%"] = -p.returns / p.gross_sales * 100
doel = k["retour%"]
slecht = p[(p["retour%"] > doel + 8) & (p.gross_sales > 3000)]
besparing = ((slecht["retour%"] - doel) / 100 * slecht.gross_sales).sum()
pakketten = besparing / AOV
winst = besparing * MARGE + pakketten * RETOURKOSTEN
print(slecht[["product_title", "gross_sales", "retour%"]].to_string(
    index=False, float_format=lambda v: f"{v:,.0f}"))
print(f"  samen € {besparing:,.0f} minder retour, brutowinst € {winst:,.0f} per half jaar "
      f"(€ {winst*2:,.0f} op jaarbasis)".replace(",", "."))
