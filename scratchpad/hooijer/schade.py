"""Hoeveel sessies zijn er spook, en wat is de trechter zonder de storingsperiode?

Storing: 18 september 2025 t/m 12 februari 2026 (148 dagen).
Anker: orders. Die worden bij de kassa geteld en zijn niet geraakt.
"""
import pandas as pd

alles = pd.read_pickle("piek_maanden.pkl")
g = alles.groupby("maand")[["sessions", "sessions_with_cart_additions",
                            "sessions_that_completed_checkout", "orders"]].sum()
g["wagen%"] = g.sessions_with_cart_additions / g.sessions * 100
g["sess/order"] = g.sessions / g.orders

STORING = ["2025-09", "2025-10", "2025-11", "2025-12", "2026-01", "2026-02"]
SCHOON_VOOR = ["2025-06", "2025-07", "2025-08"]
SCHOON_NA = ["2026-03", "2026-04", "2026-05", "2026-06", "2026-07", "2026-08"]
KERN = ["2025-10", "2025-11", "2025-12", "2026-01"]  # volledig binnen de storing

schoon = g.loc[SCHOON_VOOR + SCHOON_NA]
norm_spo = schoon.sessions.sum() / schoon.orders.sum()
norm_wagen = (schoon.sessions_with_cart_additions.sum() / schoon.sessions.sum()) * 100

print(f"Normaal, buiten de storing: {norm_spo:.1f} sessies per order, "
      f"{norm_wagen:.2f}% legt iets in de wagen\n")

kern = g.loc[KERN]
verwacht = kern.orders.sum() * norm_spo
spook = kern.sessions.sum() - verwacht
print(f"Volle storingsmaanden okt-jan: {kern.sessions.sum():,.0f} sessies, "
      f"{kern.orders.sum():,.0f} orders".replace(",", "."))
print(f"  bij normaal gedrag verwacht: {verwacht:,.0f} sessies".replace(",", "."))
print(f"  spooksessies:                {spook:,.0f}  ({spook/kern.sessions.sum()*100:.0f}% "
      f"van die maanden)".replace(",", "."))

# Effect op de nulmeting van 12 maanden (sep 2025 t/m aug 2026)
JAAR = ["2025-09", "2025-10", "2025-11", "2025-12", "2026-01", "2026-02",
        "2026-03", "2026-04", "2026-05", "2026-06", "2026-07", "2026-08"]
jaar = g.loc[JAAR]
print(f"\nNulmeting zoals gemeten (sep25-aug26):")
print(f"  {jaar.sessions.sum():,.0f} sessies, "
      f"{jaar.sessions_with_cart_additions.sum() / jaar.sessions.sum()*100:.2f}% in de wagen"
      .replace(",", "."))
print(f"Zelfde jaar, storingsmaanden eruit (mrt-aug 2026):")
na = g.loc[SCHOON_NA]
print(f"  {na.sessions.sum():,.0f} sessies in 6 maanden, "
      f"{na.sessions_with_cart_additions.sum() / na.sessions.sum()*100:.2f}% in de wagen"
      .replace(",", "."))
print(f"Ter vergelijking, de drie maanden vóór de storing (jun-aug 2025):")
voor = g.loc[SCHOON_VOOR]
print(f"  {voor.sessions.sum():,.0f} sessies, "
      f"{voor.sessions_with_cart_additions.sum() / voor.sessions.sum()*100:.2f}% in de wagen"
      .replace(",", "."))

pd.set_option("display.width", 200)
print("\n=== per maand, alle 17 shops ===")
print(g[["sessions", "orders", "sess/order", "wagen%"]].to_string(
    float_format=lambda v: f"{v:,.2f}"))
