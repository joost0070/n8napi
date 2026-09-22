"""De rangschikking kijkt alleen naar stap 1. Lekken shops daar wel het meest?

Per shop: wat levert het op om stap 1, stap 2 of stap 3 naar het groepsniveau te
brengen, met de andere twee stappen ongemoeid? Dan zie je welke stap bij welke
shop de knop is.
"""
import pandas as pd

df = pd.read_pickle("nulmeting_v2.pkl")
groep = df[df.sleutel == "_totaal"].iloc[0]
df = df[(df.sleutel != "_totaal") & (df.sessions >= 10000)].copy()

D1, D2, D3 = groep["wagen%"], groep["afreken%"], groep["order%"]
print(f"Groepsniveau: stap 1 {D1:.2f}% in de wagen, stap 2 {D2:.1f}% naar afrekenen, "
      f"stap 3 {D3:.1f}% naar order\n")


def orders(sessies, s1, s2, s3):
    return sessies * s1 / 100 * s2 / 100 * s3 / 100


for stap, (kolom, doel) in enumerate(
        [("wagen%", D1), ("afreken%", D2), ("order%", D3)], start=1):
    nu = df.apply(lambda r: orders(r.sessions, r["wagen%"], r["afreken%"], r["order%"]), axis=1)
    verbeterd = df.apply(lambda r: orders(
        r.sessions,
        max(r["wagen%"], doel) if kolom == "wagen%" else r["wagen%"],
        max(r["afreken%"], doel) if kolom == "afreken%" else r["afreken%"],
        max(r["order%"], doel) if kolom == "order%" else r["order%"]), axis=1)
    df[f"stap {stap}"] = (verbeterd - nu) * df.AOV

df["beste stap"] = df[["stap 1", "stap 2", "stap 3"]].idxmax(axis=1)
df["grootste winst"] = df[["stap 1", "stap 2", "stap 3"]].max(axis=1)

pd.set_option("display.width", 210)
toon = df[["shop", "sessions", "wagen%", "afreken%", "order%",
           "stap 1", "stap 2", "stap 3", "beste stap"]].sort_values(
    "stap 1", ascending=False)
print("=== extra omzet per half jaar als die ene stap naar groepsniveau gaat ===")
print(toon.to_string(index=False, float_format=lambda v: f"{v:,.0f}"))

anders = df[df["beste stap"] != "stap 1"]
print(f"\nBij {len(anders)} van de {len(df)} shops zit de grootste kans NIET in stap 1:")
for _, r in anders.sort_values("grootste winst", ascending=False).iterrows():
    print(f"  {r.shop:<15} {r['beste stap']}  € {r['grootste winst']:>8,.0f} per half jaar "
          f"(stap 1 zou € {r['stap 1']:,.0f} zijn)".replace(",", "."))
df.to_pickle("controle_stappen.pkl")
