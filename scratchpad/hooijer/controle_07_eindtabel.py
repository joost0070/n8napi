"""De eindtabel: elke shop, elke knop, in brutowinst per jaar.

Trechter : alle drie de stappen naar hun eerlijke maatstaf.
           stap 1 -> het niveau dat bij het prijspunt van de shop hoort
           stap 2 en 3 -> het groepsniveau
Retouren : naar de mediaan van de groep, een vijfde onverkoopbaar.
Marge    : catalogusmarge, geijkt op de shops waar Shopify's gerealiseerde marge
           betrouwbaar is (juli en augustus 2026 allebei plausibel).
"""
from concurrent.futures import ThreadPoolExecutor
import numpy as np
import pandas as pd
import shop, sql

RETOURKOSTEN, ONVERKOOPBAAR = 9.00, 0.20

# ---------- marge ijken
def gerealiseerd(sleutel):
    d = sql.vraag(sleutel, "FROM sales SHOW net_sales, cost_of_goods_sold GROUP BY month "
                           "SINCE 2026-07-01 UNTIL 2026-08-31")
    m = (1 - d.cost_of_goods_sold / d.net_sales) * 100
    m = m[(m > 20) & (m < 90)]
    return sleutel, (m.mean() if len(m) == 2 else None)

with ThreadPoolExecutor(max_workers=5) as pool:
    echt = dict(pool.map(gerealiseerd, shop.SHOPS))

def catalogus(sleutel):
    try:
        d = pd.read_pickle(f"assortiment_{sleutel}.pkl")
    except FileNotFoundError:
        return None
    g = d[(d.prijs > 0) & (d.kostprijs > 0)]
    return (1 - g.kostprijs / g.prijs).median() * 100 if len(g) >= 20 else None

kat = {s: catalogus(s) for s in shop.SHOPS}
paren = [(kat[s], echt[s]) for s in shop.SHOPS if kat[s] and echt[s]]
factor = float(np.median([e / k for k, e in paren]))
print(f"Marge-ijking op {len(paren)} shops waar beide bronnen bruikbaar zijn:")
for s in shop.SHOPS:
    if kat[s] and echt[s]:
        print(f"  {shop.LABELS[s]:<15} catalogus {kat[s]:5.1f}%   gerealiseerd {echt[s]:5.1f}%")
print(f"  ijkfactor (mediaan): {factor:.2f}\n")

# ---------- trechter, alle drie de stappen
df = pd.read_pickle("nulmeting_v2.pkl")
groep = df[df.sleutel == "_totaal"].iloc[0]
df = df[(df.sleutel != "_totaal") & (df.sessions >= 10000)].copy()

doelen = []
for naam in df.shop:
    rest = df[df.shop != naam]
    h, s = np.polyfit(rest.AOV, rest["wagen%"], 1)
    doelen.append(h * df.loc[df.shop == naam, "AOV"].iloc[0] + s)
df["doel stap1"] = doelen

def orders(r, gebruik_doel):
    s1 = max(r["wagen%"], r["doel stap1"]) if gebruik_doel else r["wagen%"]
    s2 = max(r["afreken%"], groep["afreken%"]) if gebruik_doel else r["afreken%"]
    s3 = max(r["order%"], groep["order%"]) if gebruik_doel else r["order%"]
    return r.sessions * s1 / 100 * s2 / 100 * s3 / 100

df["extra orders"] = df.apply(lambda r: orders(r, True) - orders(r, False), axis=1)
df["omzet trechter"] = df["extra orders"] * df.AOV

# ---------- retouren
mediaan = df["retour%"].median()
df["bespaarbaar retour"] = (df["retour%"] - mediaan).clip(lower=0) / 100 * df.gross_sales

# ---------- winst
df["marge%"] = [(kat[s] or np.median([v for v in kat.values() if v])) * factor
                for s in df.sleutel]
df["winst trechter"] = df["omzet trechter"] * df["marge%"] / 100 * 2
df["winst retour"] = ((df["bespaarbaar retour"] / df.AOV * RETOURKOSTEN
                       + df["bespaarbaar retour"] * ONVERKOOPBAAR * df["marge%"] / 100) * 2)
df["winst totaal"] = df["winst trechter"] + df["winst retour"]

pd.set_option("display.width", 220)
print("=== GECORRIGEERDE RANGSCHIKKING — brutowinst per jaar ===\n")
toon = df[["shop", "sessions", "AOV", "wagen%", "doel stap1", "marge%",
           "extra orders", "winst trechter", "winst retour", "winst totaal"]].sort_values(
    "winst totaal", ascending=False)
print(toon.to_string(index=False, float_format=lambda v: f"{v:,.0f}"))
print(f"\n  samen € {df['winst totaal'].sum():,.0f} brutowinst per jaar".replace(",", "."))
df.to_pickle("controle_eindtabel.pkl")
df.to_csv("controle_eindtabel.csv", index=False)
