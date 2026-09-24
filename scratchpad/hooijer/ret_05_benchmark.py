"""Eigen retourpercentages per shop en productsoort, naast de Returnista-benchmark (EU).

Bron: ShopifyQL, bruto omzet en retourwaarde per product, 1 januari t/m 31 augustus
2026. Retourpercentage op waarde. Retouren worden geboekt in de maand waarin ze
binnenkomen; over acht maanden valt dat verschil grotendeels weg.
"""
from concurrent.futures import ThreadPoolExecutor
import pandas as pd
import shop, sql
from bar_14_soort import soort

BENCH = {"Sandalen": 23.2, "Laarzen/boots": 25.1, "Wandelschoenen": 28.5, "Sneakers": 23.75,
         "Sokken": 1.25, "Footwear totaal": 28.0}
SHOPS = ["lazamani_nl", "lazamani_de", "keen_nl", "heydude_nl", "bartogi_nl", "bartogi_de",
         "hunter_nl", "tofvel_nl", "toni_pons_nl" if "toni_pons_nl" in shop.SHOPS else "tonipons_nl",
         "sockwell_nl", "sockwell_de", "janjansen", "tofvel_de", "lazamani_en", "sockwell_en"]


def haal(s):
    d = sql.vraag(s, "FROM sales SHOW gross_sales, returns GROUP BY product_title "
                     "SINCE 2026-01-01 UNTIL 2026-08-31 ORDER BY gross_sales DESC LIMIT 2000")
    d = d[d.product_title.notna()].copy()
    d["shop"] = shop.LABELS[s]
    d["soort"] = d.product_title.map(soort)
    tot = sql.vraag(s, "FROM sales SHOW gross_sales, returns SINCE 2026-01-01 UNTIL 2026-08-31").iloc[0]
    return d, (shop.LABELS[s], tot.gross_sales, -tot.returns)


with ThreadPoolExecutor(max_workers=5) as p:
    uit = list(p.map(haal, [s for s in SHOPS if s in shop.SHOPS]))
d = pd.concat([u[0] for u in uit], ignore_index=True)
tot = pd.DataFrame([u[1] for u in uit], columns=["shop", "bruto", "retour"])
tot["retour%"] = tot.retour / tot.bruto * 100
d["retour"] = -d.returns
d.to_pickle("ret_benchmark.pkl")

pd.set_option("display.width", 220)
print("=== per shop (retour op waarde, jan-aug 2026) tegen footwear-benchmark 28% ===")
print(tot.sort_values("retour%", ascending=False).to_string(
    index=False, float_format=lambda v: f"{v:,.1f}"))

k = d.groupby(["soort"]).agg(bruto=("gross_sales", "sum"), retour=("retour", "sum"))
k["retour%"] = k.retour / k.bruto * 100
k["benchmark"] = k.index.map(BENCH)
k = k[k.bruto > 20000].sort_values("bruto", ascending=False)
print("\n=== per productsoort, alle shops samen ===")
print(k.to_string(float_format=lambda v: f"{v:,.1f}"))

x = d[d.soort.isin(["Sandalen", "Laarzen/boots", "Wandelschoenen", "Sneakers", "Pantoffels",
                    "Instappers/klompen", "Teenslippers/slippers", "Sokken"])]
m = x.groupby(["shop", "soort"]).agg(bruto=("gross_sales", "sum"), retour=("retour", "sum"))
m = m[m.bruto > 5000]
m["retour%"] = m.retour / m.bruto * 100
tab = m["retour%"].unstack().round(1)
print("\n=== retour% per shop en soort (alleen waar meer dan € 5.000 omzet) ===")
print(tab.to_string())
