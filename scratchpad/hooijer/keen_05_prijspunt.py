"""Hoort een laag winkelwagenpercentage bij een hoog prijspunt?

Toets over alle 17 shops: hangt het wagenpercentage samen met de orderwaarde?
En wat gebeurt er als je niet op wagenpercentage stuurt maar op euro per sessie?
"""
import pandas as pd

df = pd.read_pickle("nulmeting_v2.pkl")
df = df[(df.sleutel != "_totaal") & (df.sessions >= 10000)].copy()
df["euro per sessie"] = df.net_sales / df.sessions
df["euro per wagen"] = df.net_sales / df.sessions_with_cart_additions

r = df["wagen%"].corr(df.AOV)
r_rang = df["wagen%"].rank().corr(df.AOV.rank())
print(f"samenhang wagen% met AOV: Pearson {r:.2f}, Spearman {r_rang:.2f}  "
      f"(n={len(df)} shops)\n")

# Hoeveel wagen% verwacht je bij de AOV van deze shop? Eenvoudige lijn door de rest.
import numpy as np
for uit in ("KEEN NL",):
    rest = df[df.shop != uit]
    helling, snij = np.polyfit(rest.AOV, rest["wagen%"], 1)
    keen = df[df.shop == uit].iloc[0]
    verwacht = helling * keen.AOV + snij
    print(f"Lijn door de 12 andere shops: wagen% = {snij:.2f} {helling:+.4f} x AOV")
    print(f"  Bij KEEN's AOV van € {keen.AOV:.2f} hoort dus ongeveer {verwacht:.2f}%")
    print(f"  KEEN doet werkelijk {keen['wagen%']:.2f}%  "
          f"({keen['wagen%'] - verwacht:+.2f} procentpunt)\n")

pd.set_option("display.width", 200)
toon = df[["shop", "sessions", "AOV", "wagen%", "conversie%", "euro per sessie",
           "euro per wagen", "retour%"]].sort_values("euro per sessie", ascending=False)
print("=== gerangschikt op euro per sessie, niet op wagenpercentage ===")
print(toon.to_string(index=False, float_format=lambda v: f"{v:,.2f}"))
