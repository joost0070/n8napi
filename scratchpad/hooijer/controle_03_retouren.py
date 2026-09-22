"""De tweede knop: retouren. Hoeveel brutowinst staat er per shop op het spel?

Bij KEEN bleek de retourstroom meer winst te kosten dan de hele trechterkans.
Deze toets kijkt of dat bij meer shops zo is.
"""
import pandas as pd

RETOURKOSTEN = 9.00   # aanname: retourzending, inspectie, herverpakken per pakket
MARGE = 0.54          # voorlopige eenheidsmarge; wordt in de volgende stap per shop

df = pd.read_pickle("nulmeting_v2.pkl")
df = df[(df.sleutel != "_totaal") & (df.sessions >= 10000)].copy()

df["retour euro"] = -df["returns"]
df["retourpakketten"] = df["retour euro"] / df.AOV
df["winstverlies retour"] = df["retour euro"] * MARGE + df["retourpakketten"] * RETOURKOSTEN

# Wat als elke shop naar de mediaan van de groep zou gaan?
mediaan = df["retour%"].median()
df["te veel pp"] = (df["retour%"] - mediaan).clip(lower=0)
df["bespaarbaar euro"] = df["te veel pp"] / 100 * df.gross_sales
df["winst uit retour"] = (df["bespaarbaar euro"] * MARGE
                          + df["bespaarbaar euro"] / df.AOV * RETOURKOSTEN)

pd.set_option("display.width", 210)
print(f"Mediaan retourpercentage van de groep: {mediaan:.1f}%")
print(f"Gerekend met {MARGE*100:.0f}% marge en € {RETOURKOSTEN:.2f} afhandeling per pakket.\n")
toon = df[["shop", "gross_sales", "retour%", "retour euro", "retourpakketten",
           "winstverlies retour", "te veel pp", "winst uit retour"]].sort_values(
    "winst uit retour", ascending=False)
print(toon.to_string(index=False, float_format=lambda v: f"{v:,.0f}"))
print(f"\nSamen staat er € {df['winstverlies retour'].sum():,.0f} brutowinst per half jaar "
      f"in de retourstroom.".replace(",", "."))
print(f"Naar de mediaan brengen levert € {df['winst uit retour'].sum():,.0f} per half jaar "
      f"(€ {df['winst uit retour'].sum()*2:,.0f} per jaar).".replace(",", "."))
df.to_pickle("controle_retouren.pkl")
