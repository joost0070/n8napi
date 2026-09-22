"""Lazamani NL en DE: waar zitten de retouren?"""
from concurrent.futures import ThreadPoolExecutor
import pandas as pd
import shop, sql

SCHOON = "SINCE 2026-03-01 UNTIL 2026-08-31"
pd.set_option("display.width", 210, "display.max_colwidth", 46)


def per_maand(s):
    d = sql.vraag(s, f"FROM sales SHOW gross_sales, returns GROUP BY month {SCHOON} "
                     f"ORDER BY month")
    d["shop"] = shop.LABELS[s]; d["maand"] = d.month.str[:7]
    d["retour%"] = -d.returns / d.gross_sales * 100
    return d


with ThreadPoolExecutor(max_workers=3) as p:
    m = pd.concat(p.map(per_maand, ["lazamani_nl", "lazamani_de", "lazamani_en"]),
                  ignore_index=True)
print("=== retourpercentage per maand ===")
print(m.pivot_table(index="shop", columns="maand", values="retour%").to_string(
    float_format=lambda v: f"{v:,.1f}"))

for s in ("lazamani_nl", "lazamani_de"):
    p_ = sql.vraag(s, f"FROM sales SHOW gross_sales, returns, net_sales, net_items_sold "
                      f"GROUP BY product_title {SCHOON} ORDER BY returns ASC LIMIT 18")
    p_["retour%"] = -p_.returns / p_.gross_sales * 100
    print(f"\n=== {shop.LABELS[s]}: grootste retourposten ===")
    print(p_[["product_title", "gross_sales", "returns", "retour%",
              "net_items_sold"]].to_string(index=False, float_format=lambda v: f"{v:,.0f}"))

# prijsvergelijking over de drie shops, op sku
print("\n\n=== zelfde artikel, andere prijs? ===")
stukken = []
for s in ("lazamani_nl", "lazamani_de", "lazamani_en"):
    d = pd.read_pickle(f"assortiment_{s}.pkl")[["sku", "titel", "prijs", "kostprijs"]]
    d = d[d.sku.notna() & (d.sku != "") & (d.prijs > 0)]
    d = d.groupby("sku").agg(titel=("titel", "first"), prijs=("prijs", "median"),
                             kostprijs=("kostprijs", "median")).reset_index()
    d["shop"] = shop.LABELS[s]
    stukken.append(d)
alle = pd.concat(stukken)
kruis = alle.pivot_table(index="sku", columns="shop", values="prijs")
kruis = kruis.dropna()
print(f"  {len(kruis):,} artikelen komen in alle drie de shops voor".replace(",", "."))
for a, b in (("Lazamani NL", "Lazamani DE"), ("Lazamani NL", "Lazamani EN")):
    verschil = (kruis[b] / kruis[a] - 1) * 100
    print(f"  {b} tegenover {a}: mediaan {verschil.median():+.1f}%, "
          f"{(verschil.abs() > 1).mean()*100:.0f}% wijkt af")
print("\n  voorbeelden:")
titels = alle.drop_duplicates("sku").set_index("sku").titel
print(kruis.join(titels).head(12).to_string(float_format=lambda v: f"{v:,.2f}"))
