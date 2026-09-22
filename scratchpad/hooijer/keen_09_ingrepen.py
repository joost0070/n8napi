"""KEEN NL: de drie ingrepen doorgerekend, met hun nulmeting."""
import pandas as pd
import sql

MARGE, RETOURKOSTEN = 0.54, 9.00
SCHOON = "SINCE 2026-03-01 UNTIL 2026-08-31"
M = "sessions, sessions_with_cart_additions, sessions_that_completed_checkout"

basis = pd.read_pickle("nulmeting_v2.pkl")
k = basis[basis.sleutel == "keen_nl"].iloc[0]
AOV, AFREKEN, ORDER = k.AOV, k["afreken%"] / 100, k["order%"] / 100

print("=== Wat retouren KEEN nu kosten ===")
kop = sql.vraag("keen_nl", f"FROM sales SHOW gross_sales, returns {SCHOON}").iloc[0]
pakketten = -kop.returns / AOV
verlies = -kop.returns * MARGE + pakketten * RETOURKOSTEN
print(f"  € {-kop.returns:,.0f} retour over zes maanden, ongeveer {pakketten:,.0f} pakketten"
      .replace(",", "."))
print(f"  misgelopen brutowinst € {-kop.returns*MARGE:,.0f} plus afhandeling "
      f"€ {pakketten*RETOURKOSTEN:,.0f}".replace(",", "."))
print(f"  samen € {verlies:,.0f} per half jaar, € {verlies*2:,.0f} op jaarbasis\n"
      .replace(",", "."))

# ---------- 1. collectiepagina's
pag = sql.vraag("keen_nl", f"FROM sessions SHOW {M} GROUP BY landing_page_path {SCHOON} "
                           f"ORDER BY sessions DESC LIMIT 400")
col = pag[pag.landing_page_path.str.startswith("/collections/")]
s, w = col.sessions.sum(), col.sessions_with_cart_additions.sum()
nu = w / s * 100
for doel in (4.5, 5.0):
    orders = s * (doel - nu) / 100 * AFREKEN * ORDER
    print(f"1. Collectiepagina's van {nu:.2f}% naar {doel:.1f}%: "
          f"{orders:,.0f} orders, brutowinst € {orders*AOV*MARGE:,.0f} per half jaar "
          f"(€ {orders*AOV*MARGE*2:,.0f} per jaar)".replace(",", "."))
print(f"   nulmeting: {s:,.0f} sessies op collectiepagina's, {nu:.2f}% legt iets in de wagen\n"
      .replace(",", "."))

# ---------- 2. retouren op de modellen boven 30%
p = sql.vraag("keen_nl", f"FROM sales SHOW gross_sales, returns GROUP BY product_title "
                         f"{SCHOON} ORDER BY returns ASC LIMIT 60")
p["retour%"] = -p.returns / p.gross_sales * 100
erg = p[(p["retour%"] >= 30) & (p.gross_sales > 3000)]
bespaard = ((erg["retour%"] - k["retour%"]) / 100 * erg.gross_sales).sum()
winst = bespaard * MARGE + bespaard / AOV * RETOURKOSTEN
print(f"2. De {len(erg)} modellen boven 30% retour naar shopgemiddelde {k['retour%']:.1f}%:")
print(f"   € {bespaard:,.0f} minder retour, brutowinst € {winst:,.0f} per half jaar "
      f"(€ {winst*2:,.0f} per jaar)".replace(",", "."))
print(f"   nulmeting per model:")
for _, r in erg.iterrows():
    print(f"     {r.product_title[:44]:<46} € {r.gross_sales:>7,.0f}  {r['retour%']:.0f}%"
          .replace(",", "."))

# ---------- 3. terugkerende klanten
o = pd.read_pickle("keen_orders.pkl")
o["soort"] = o.orders_van_klant.apply(lambda n: "nieuw" if n <= 1 else "terugkerend")
g = o.groupby("soort").agg(omzet=("bedrag", "sum"), na=("bedrag_nu", "sum"),
                           orders=("order", "count"))
g["behouden%"] = g.na / g.omzet * 100
terug, nieuw = g.loc["terugkerend"], g.loc["nieuw"]
extra = terug.omzet * (nieuw["behouden%"] - terug["behouden%"]) / 100
winst3 = extra * MARGE + extra / AOV * RETOURKOSTEN
print(f"\n3. Terugkerende klanten op het retourniveau van nieuwe klanten:")
print(f"   nieuw houdt {nieuw['behouden%']:.1f}% van de orderwaarde, "
      f"terugkerend {terug['behouden%']:.1f}%")
print(f"   € {extra:,.0f} minder retour, brutowinst € {winst3:,.0f} per half jaar "
      f"(€ {winst3*2:,.0f} per jaar)".replace(",", "."))
print(f"   nulmeting: {terug.orders:,.0f} orders van terugkerende klanten, "
      f"€ {terug.omzet:,.0f} bruto, € {terug.na:,.0f} na retour".replace(",", "."))
