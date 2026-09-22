"""Retouren, eerlijker gerekend.

Een retour kost niet automatisch de hele marge: komt de schoen ongeschonden terug
en wordt hij opnieuw verkocht, dan is het vooral afhandeling en werkkapitaal. Pas
wat niet meer verkoopbaar is (gedragen, uit het seizoen, afgeprijsd) kost marge.
Omdat het onverkoopbare deel hier niet te meten is, rekenen we drie scenario's.

Wat wel hard is: elk retourpakket kost afhandeling, ongeacht wat ermee gebeurt.
"""
import pandas as pd

RETOURKOSTEN = 9.00
MARGE = 0.54
SCENARIOS = {"alles herverkocht": 0.00, "een vijfde onverkoopbaar": 0.20,
             "twee vijfde onverkoopbaar": 0.40}

df = pd.read_pickle("nulmeting_v2.pkl")
df = df[(df.sleutel != "_totaal") & (df.sessions >= 10000)].copy()
df["retour euro"] = -df["returns"]
df["pakketten"] = df["retour euro"] / df.AOV

mediaan = df["retour%"].median()
df["te veel pp"] = (df["retour%"] - mediaan).clip(lower=0)
df["bespaarbaar euro"] = df["te veel pp"] / 100 * df.gross_sales
df["bespaarbare pakketten"] = df["bespaarbaar euro"] / df.AOV

print(f"Mediaan retourpercentage: {mediaan:.1f}%. Doel: elke shop daarheen.\n")
print("=== wat het nu kost, alle shops samen, per half jaar ===")
for naam, deel in SCENARIOS.items():
    kost = (df["pakketten"] * RETOURKOSTEN).sum() + (df["retour euro"] * deel * MARGE).sum()
    print(f"  {naam:<28} € {kost:>9,.0f}   (€ {kost*2:>9,.0f} per jaar)".replace(",", "."))

print(f"\n  waarvan zeker: afhandeling van {df['pakketten'].sum():,.0f} pakketten = "
      f"€ {(df['pakketten']*RETOURKOSTEN).sum():,.0f} per half jaar".replace(",", "."))

print("\n=== wat naar de mediaan brengen oplevert, per shop, per jaar ===")
for naam, deel in SCENARIOS.items():
    df[naam] = ((df["bespaarbare pakketten"] * RETOURKOSTEN
                 + df["bespaarbaar euro"] * deel * MARGE) * 2)
pd.set_option("display.width", 210)
toon = df[df["te veel pp"] > 0][
    ["shop", "retour%", "te veel pp", "bespaarbaar euro"] + list(SCENARIOS)
].sort_values(list(SCENARIOS)[1], ascending=False)
print(toon.to_string(index=False, float_format=lambda v: f"{v:,.0f}"))
print("  " + "-" * 100)
for naam in SCENARIOS:
    print(f"  totaal {naam:<28} € {df[naam].sum():>9,.0f} per jaar".replace(",", "."))
df.to_pickle("controle_retouren.pkl")
