"""Welke orders en welke merken zijn na alle kosten nog winstgevend?"""
import pandas as pd
pd.set_option("display.width", 220)

ADV_NL, ORDERS_NL, BRUTO_NL = 39286.05, 3280, 187792.86
VERZEND, RETOURZ, PAYMENT = 6.00, 6.00, 0.0078

o = pd.read_pickle("bar_orders_nl.pkl")
adv_per_order = ADV_NL / ORDERS_NL
print(f"Advertentiekosten € {ADV_NL:,.0f} over {ORDERS_NL:,} orders = "
      f"€ {adv_per_order:.2f} per order\n".replace(",", "."))

o["productmarge"] = o.netto_nu - o.inkoop_nu
o["verzendlast"] = VERZEND + o.retourpakket * RETOURZ - o.verzendopbrengst
o["payment"] = o.bruto * PAYMENT
o["bijdrage voor adv"] = o.productmarge - o.verzendlast - o.payment
o["bijdrage na adv"] = o["bijdrage voor adv"] - adv_per_order

g = o.groupby("schijf", observed=True).agg(
    orders=("order", "count"), omzet=("bruto", "sum"),
    voor_adv=("bijdrage voor adv", "sum"), na_adv=("bijdrage na adv", "sum")).reset_index()
g["per order voor adv"] = g.voor_adv / g.orders
g["per order na adv"] = g.na_adv / g.orders
g["aandeel orders%"] = g.orders / len(o) * 100
print("=== bijdrage per orderschijf, advertentiekosten gelijk per order toegerekend ===")
print(g[["schijf","orders","aandeel orders%","omzet","per order voor adv","na_adv",
         "per order na adv"]].to_string(index=False, float_format=lambda v: f"{v:,.1f}"))

verlies = g[g["per order na adv"] < 0]
print(f"\n  verliesgevende schijven: {verlies.orders.sum():,} orders "
      f"({verlies.orders.sum()/len(o)*100:.0f}%), samen € {verlies.na_adv.sum():,.0f} negatief"
      .replace(",", "."))

print("\n=== nieuwe tegenover terugkerende klanten ===")
o["soort"] = o.klantorders.apply(lambda n: "nieuw" if n <= 1 else "terugkerend")
k = o.groupby("soort").agg(orders=("order","count"), omzet=("bruto","sum"),
                           bijdrage=("bijdrage voor adv","sum")).reset_index()
k["aandeel%"] = k.orders / len(o) * 100
k["bijdrage per order"] = k.bijdrage / k.orders
print(k.to_string(index=False, float_format=lambda v: f"{v:,.1f}"))

print("\n=== merkmix: wat als Bartogi NL de mix van DE had? ===")
nl = pd.read_pickle("bar_regels_bartogi_nl.pkl")
de = pd.read_pickle("bar_regels_bartogi_de.pkl")
def marges(d):
    d = d[d.kostprijs > 0].copy()
    d["n"] = d.netto * d.aantal_nu / d.aantal.replace(0, 1)
    d["k"] = d.kostprijs * d.aantal_nu
    g = d.groupby("merk").agg(netto=("n","sum"), inkoop=("k","sum")).reset_index()
    g["marge%"] = (1 - g.inkoop/g.netto) * 100
    g["aandeel"] = g.netto / g.netto.sum()
    return g
mn, md = marges(nl), marges(de)
mn["merk_s"] = mn.merk.str.upper(); md["merk_s"] = md.merk.str.upper()
mn = mn.groupby("merk_s").apply(lambda d: pd.Series({
    "netto": d.netto.sum(), "inkoop": d.inkoop.sum()}), include_groups=False).reset_index()
md = md.groupby("merk_s").apply(lambda d: pd.Series({
    "netto": d.netto.sum(), "inkoop": d.inkoop.sum()}), include_groups=False).reset_index()
for d in (mn, md):
    d["marge%"] = (1 - d.inkoop/d.netto) * 100
    d["aandeel"] = d.netto / d.netto.sum()
s = mn.merge(md, on="merk_s", suffixes=("_nl", "_de"), how="outer").fillna(0)
werkelijk = (1 - mn.inkoop.sum()/mn.netto.sum()) * 100
s2 = s[(s.aandeel_de > 0) & (s["marge%_nl"] > 0)]
gesimuleerd = (s2.aandeel_de/s2.aandeel_de.sum() * s2["marge%_nl"]).sum()
print(s[["merk_s","aandeel_nl","marge%_nl","aandeel_de","marge%_de"]].sort_values(
    "aandeel_nl", ascending=False).to_string(index=False, float_format=lambda v: f"{v:,.3f}"))
print(f"\n  productmarge NL werkelijk            : {werkelijk:.1f}%")
print(f"  productmarge NL met de merkmix van DE: {gesimuleerd:.1f}%")
print(f"  effect van de merkmix                : {gesimuleerd-werkelijk:+.1f} procentpunt")
