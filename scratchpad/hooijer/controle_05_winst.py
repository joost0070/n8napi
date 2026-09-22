"""De gecorrigeerde rangschikking, op brutowinst, met beide knoppen.

Knop 1: de trechter, maar tegen een doel dat bij het prijspunt van de shop hoort.
Knop 2: retouren terug naar de mediaan van de groep.

Marge: catalogusmarge per shop (verkoopprijs tegen kostprijs over het assortiment),
voor alle shops op dezelfde manier gemeten. Geijkt tegen de shops waar Shopify's
eigen gerealiseerde marge betrouwbaar is.
"""
import pandas as pd
import shop

RETOURKOSTEN, ONVERKOOPBAAR = 9.00, 0.20

def catalogusmarge(sleutel):
    try:
        df = pd.read_pickle(f"assortiment_{sleutel}.pkl")
    except FileNotFoundError:
        return None, 0
    g = df[(df.prijs > 0) & (df.kostprijs > 0)]
    if len(g) < 20:
        return None, 0
    return (1 - g.kostprijs / g.prijs).median() * 100, len(g) / len(df) * 100

scheef = pd.read_pickle("controle_scheefheid.pkl")
retour = pd.read_pickle("controle_retouren.pkl").set_index("shop")

rijen = []
for _, r in scheef.iterrows():
    marge, dekking = catalogusmarge(r.sleutel)
    rijen.append({"shop": r.shop, "sleutel": r.sleutel, "AOV": r.AOV,
                  "sessies": r.sessions, "wagen%": r["wagen%"],
                  "catalogusmarge%": marge, "kostprijsdekking%": dekking,
                  "omzet trechter": r["omzet nieuw"],
                  "bespaarbaar retour": retour.loc[r.shop, "bespaarbaar euro"]})
df = pd.DataFrame(rijen)

groepsmarge = df["catalogusmarge%"].median()
df["marge%"] = df["catalogusmarge%"].fillna(groepsmarge)
print(f"Catalogusmarge, mediaan over de shops: {groepsmarge:.1f}%")
print("Shops zonder bruikbare kostprijzen krijgen die mediaan.\n")

df["winst trechter"] = df["omzet trechter"] * df["marge%"] / 100 * 2       # jaarbasis
df["winst retour"] = ((df["bespaarbaar retour"] / df.AOV * RETOURKOSTEN
                       + df["bespaarbaar retour"] * ONVERKOOPBAAR * df["marge%"] / 100) * 2)
df["winst totaal"] = df["winst trechter"] + df["winst retour"]

pd.set_option("display.width", 220)
print("=== gecorrigeerde rangschikking op brutowinst per jaar ===")
print(f"    (retouren: een vijfde onverkoopbaar, € {RETOURKOSTEN:.2f} afhandeling per pakket)\n")
toon = df[["shop", "sessies", "AOV", "wagen%", "catalogusmarge%", "kostprijsdekking%",
           "winst trechter", "winst retour", "winst totaal"]].sort_values(
    "winst totaal", ascending=False)
print(toon.to_string(index=False, float_format=lambda v: f"{v:,.0f}"))
print(f"\n  samen € {df['winst totaal'].sum():,.0f} brutowinst per jaar".replace(",", "."))
df.to_pickle("controle_winst.pkl")
df.to_csv("controle_winstrangschikking.csv", index=False)
