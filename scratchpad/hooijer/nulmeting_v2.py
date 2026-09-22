"""Nulmeting op schone data: maart t/m augustus 2026.

Waarom dit venster: van 18 september 2025 tot en met 12 februari 2026 was de
sessiemeting van alle shops kapot (herkomst ging verloren, sessies werden
opgeblazen, orders werden vrijwel allemaal op 'direct' geboekt). Februari 2026
is half besmet. Maart 2026 is de eerste hele schone maand.

Bronnen
  trechter : ShopifyQL dataset `sessions`
  geld     : ShopifyQL dataset `sales`
Meetwijze
  wagen%     = sessies met winkelwagentoevoeging / sessies
  afreken%   = sessies tot afrekenen / sessies met winkelwagentoevoeging
  order%     = sessies met afgeronde bestelling / sessies tot afrekenen
  conversie% = sessies met afgeronde bestelling / sessies
  AOV        = netto-omzet / orders (sales-dataset, dus inclusief orders
               die niet aan een webshopsessie hangen)
"""
from concurrent.futures import ThreadPoolExecutor

import pandas as pd

import shop
import sql

SCHOON = "SINCE 2026-03-01 UNTIL 2026-08-31"          # 184 dagen
VORIG_JAAR = "SINCE 2025-06-01 UNTIL 2025-08-31"      # schoon, vóór de storing
DIT_JAAR = "SINCE 2026-06-01 UNTIL 2026-08-31"        # schoon, zelfde seizoen
MAANDEN = 6

TRECHTER = ("sessions, sessions_with_cart_additions, "
            "sessions_that_reached_checkout, sessions_that_completed_checkout")
GELD = "gross_sales, discounts, returns, net_sales, orders"


def meet(sleutel: str, periode: str) -> dict:
    trechter = sql.vraag(sleutel, f"FROM sessions SHOW {TRECHTER} {periode}")
    geld = sql.vraag(sleutel, f"FROM sales SHOW {GELD} {periode}")
    regel = {"shop": shop.LABELS.get(sleutel, sleutel), "sleutel": sleutel}
    for bron in (trechter, geld):
        for kolom in bron.columns:
            regel[kolom] = bron[kolom].iloc[0] if len(bron) else 0
    return regel


def afgeleid(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["wagen%"] = df.sessions_with_cart_additions / df.sessions * 100
    df["afreken%"] = (df.sessions_that_reached_checkout
                      / df.sessions_with_cart_additions * 100)
    df["order%"] = (df.sessions_that_completed_checkout
                    / df.sessions_that_reached_checkout * 100)
    df["conversie%"] = df.sessions_that_completed_checkout / df.sessions * 100
    df["AOV"] = df.net_sales / df.orders
    df["korting%"] = -df.discounts / df.gross_sales * 100
    df["retour%"] = -df.returns / df.gross_sales * 100
    return df.replace([float("inf"), float("-inf")], 0).fillna(0)


def totaalregel(df: pd.DataFrame) -> pd.DataFrame:
    som = {k: df[k].sum() for k in df.columns
           if k not in {"shop", "sleutel"} and not k.endswith("%") and k != "AOV"}
    som.update({"shop": "ALLE SHOPS", "sleutel": "_totaal"})
    return afgeleid(pd.concat([df, pd.DataFrame([som])], ignore_index=True))


def ophalen(periode: str) -> pd.DataFrame:
    with ThreadPoolExecutor(max_workers=5) as pool:
        rijen = list(pool.map(lambda s: meet(s, periode), shop.SHOPS))
    return pd.DataFrame(rijen).fillna(0)


if __name__ == "__main__":
    basis = ophalen(SCHOON)
    basis = basis.sort_values("sessions", ascending=False).reset_index(drop=True)
    tabel = totaalregel(basis)
    tabel.to_pickle("nulmeting_v2.pkl")

    pd.set_option("display.width", 240, "display.max_columns", 40)
    toon = ["shop", "sessions", "sessions_with_cart_additions", "wagen%",
            "sessions_that_reached_checkout", "afreken%",
            "sessions_that_completed_checkout", "order%", "conversie%",
            "net_sales", "orders", "AOV", "korting%", "retour%"]
    print(f"=== NULMETING maart t/m augustus 2026 ({MAANDEN} maanden) ===\n")
    print(tabel[toon].to_string(index=False, float_format=lambda v: f"{v:,.2f}"))
