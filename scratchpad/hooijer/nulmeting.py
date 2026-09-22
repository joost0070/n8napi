"""Nulmeting: de trechter over alle shops, opnieuw opgehaald uit ShopifyQL.

Bron A  dataset `sessions`  -> sessies, wagen, afrekenen, order
Bron B  dataset `sales`     -> bruto-omzet, netto-omzet, orders, AOV

Let op: `sessions_that_completed_checkout` (bron A) en `orders` (bron B) zijn
niet hetzelfde. A telt sessies in de webshop die eindigen in een bestelling,
B telt bestellingen ongeacht herkomst. Ze worden apart getoond, niet gemengd.
"""
import sys
from concurrent.futures import ThreadPoolExecutor

import pandas as pd

import shop
import sql

PERIODE = sys.argv[1] if len(sys.argv) > 1 else "SINCE -12m UNTIL today"

TRECHTER = ("sessions, sessions_with_cart_additions, "
            "sessions_that_reached_checkout, sessions_that_completed_checkout")
GELD = "gross_sales, discounts, returns, net_sales, orders, average_order_value"


def haal(sleutel: str) -> dict:
    trechter = sql.vraag(sleutel, f"FROM sessions SHOW {TRECHTER} {PERIODE}")
    geld = sql.vraag(sleutel, f"FROM sales SHOW {GELD} {PERIODE}")
    regel = {"sleutel": sleutel, "shop": shop.LABELS.get(sleutel, sleutel)}
    for kolom in trechter.columns:
        regel[kolom] = trechter[kolom].iloc[0] if len(trechter) else 0
    for kolom in geld.columns:
        regel[kolom] = geld[kolom].iloc[0] if len(geld) else 0
    return regel


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=5) as pool:
        rijen = list(pool.map(haal, shop.SHOPS))

    df = pd.DataFrame(rijen).fillna(0)
    totaal = {kolom: df[kolom].sum() for kolom in df.columns
              if kolom not in {"sleutel", "shop", "average_order_value"}}
    totaal["sleutel"] = "_totaal"
    totaal["shop"] = "Alle shops"
    totaal["average_order_value"] = (totaal["net_sales"] / totaal["orders"]
                                     if totaal["orders"] else 0)
    df = pd.concat([df, pd.DataFrame([totaal])], ignore_index=True)

    df["wagen_pct"] = df.sessions_with_cart_additions / df.sessions * 100
    df["afreken_pct"] = (df.sessions_that_reached_checkout
                         / df.sessions_with_cart_additions * 100)
    df["order_pct"] = (df.sessions_that_completed_checkout
                       / df.sessions_that_reached_checkout * 100)
    df["conversie_pct"] = df.sessions_that_completed_checkout / df.sessions * 100

    df = df.sort_values(["sleutel"], key=lambda k: k.eq("_totaal")).sort_values(
        "sessions", ascending=False, kind="stable")
    df.to_pickle("nulmeting.pkl")
    df.to_csv("nulmeting.csv", index=False)

    pd.set_option("display.width", 220, "display.max_columns", 30)
    toon = df[["shop", "sessions", "sessions_with_cart_additions", "wagen_pct",
               "sessions_that_reached_checkout", "afreken_pct",
               "sessions_that_completed_checkout", "order_pct", "conversie_pct",
               "net_sales", "orders", "average_order_value"]]
    print(f"periode: {PERIODE}\n")
    print(toon.to_string(index=False, float_format=lambda v: f"{v:,.2f}"))
