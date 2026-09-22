"""Rangschikking op impact, en een jaar-op-jaarvergelijking die wél mag.

Twee doelniveaus, omdat één doel een schijnzekerheid geeft:
  bovengrens  : naar het niveau van de beste shop (HEYDUDE)
  realistisch : naar het groepsgemiddelde, voor de shops die eronder zitten

Alleen de eerste trechterstap (sessie -> winkelwagen) beweegt; de stappen
daarna blijven staan. Extra orders worden gewaardeerd tegen de eigen AOV van
de shop. Dat veronderstelt dat een extra order evenveel waard is als een
gemiddelde order — zonder kanaaluitsplitsing is er geen betere aanname.
"""
from concurrent.futures import ThreadPoolExecutor

import pandas as pd

import nulmeting_v2 as basis
import shop

DREMPEL = 10000  # shops met minder sessies in het halfjaar blijven buiten de lijst


def impact(df: pd.DataFrame, doel: float, naam: str) -> pd.DataFrame:
    d = df[(df.sleutel != "_totaal") & (df.sessions >= DREMPEL)].copy()
    d = d[d["wagen%"] < doel]
    d["extra wagen"] = (doel - d["wagen%"]) / 100 * d.sessions
    d["extra orders"] = d["extra wagen"] * d["afreken%"] / 100 * d["order%"] / 100
    d["extra omzet 6mnd"] = d["extra orders"] * d.AOV
    d = d.sort_values("extra omzet 6mnd", ascending=False)
    print(f"\n=== {naam} (doel {doel:.2f}% in de wagen) ===")
    print(d[["shop", "sessions", "wagen%", "AOV", "extra orders",
             "extra omzet 6mnd"]].to_string(
        index=False, float_format=lambda v: f"{v:,.2f}"))
    print(f"  samen: € {d['extra omzet 6mnd'].sum():,.0f} over zes maanden"
          .replace(",", "."))
    return d


if __name__ == "__main__":
    tabel = pd.read_pickle("nulmeting_v2.pkl")
    beste = tabel[tabel.sleutel != "_totaal"]["wagen%"].max()
    gemiddeld = tabel[tabel.sleutel == "_totaal"]["wagen%"].iloc[0]

    boven = impact(tabel, beste, "BOVENGRENS: iedereen naar het niveau van HEYDUDE")
    echt = impact(tabel, gemiddeld, "REALISTISCH: achterblijvers naar het groepsgemiddelde")

    samen = (boven[["shop", "extra omzet 6mnd"]]
             .rename(columns={"extra omzet 6mnd": "bovengrens"})
             .merge(echt[["shop", "extra omzet 6mnd"]]
                    .rename(columns={"extra omzet 6mnd": "realistisch"}),
                    on="shop", how="left").fillna(0))
    samen.to_csv("rangschikking_v2.csv", index=False)

    # Jaar-op-jaar, alleen juni t/m augustus: beide kanten van de storing schoon.
    with ThreadPoolExecutor(max_workers=5) as pool:
        vorig = basis.afgeleid(pd.DataFrame(list(
            pool.map(lambda s: basis.meet(s, basis.VORIG_JAAR), shop.SHOPS))).fillna(0))
    with ThreadPoolExecutor(max_workers=5) as pool:
        nu = basis.afgeleid(pd.DataFrame(list(
            pool.map(lambda s: basis.meet(s, basis.DIT_JAAR), shop.SHOPS))).fillna(0))

    kolommen = ["shop", "sessions", "sessions_with_cart_additions", "orders", "net_sales"]
    jaar = vorig[kolommen].merge(nu[kolommen], on="shop", suffixes=(" 2025", " 2026"))

    def vul(df):
        """Totaalregel: absolute getallen optellen, percentages herberekenen."""
        som = df.sum(numeric_only=True)
        som["shop"] = "ALLE SHOPS"
        df = pd.concat([df, pd.DataFrame([som])], ignore_index=True)
        for jr in ("2025", "2026"):
            df[f"wagen% {jr}"] = (df[f"sessions_with_cart_additions {jr}"]
                                  / df[f"sessions {jr}"] * 100)
        for kolom in ("sessions", "orders", "net_sales"):
            df[f"{kolom} %"] = (df[f"{kolom} 2026"] / df[f"{kolom} 2025"] - 1) * 100
        df["wagen pp"] = df["wagen% 2026"] - df["wagen% 2025"]
        return df.replace([float("inf"), float("-inf")], 0).fillna(0)

    jaar = jaar.sort_values("net_sales 2026", ascending=False)
    jaar = vul(jaar)
    jaar.to_csv("jaar_op_jaar.csv", index=False)

    print("\n\n=== JAAR OP JAAR, juni t/m augustus (beide schoon, zelfde seizoen) ===")
    print(jaar[["shop", "sessions 2025", "sessions 2026", "sessions %",
                "wagen% 2025", "wagen% 2026", "wagen pp",
                "net_sales 2025", "net_sales 2026", "net_sales %"]].to_string(
        index=False, float_format=lambda v: f"{v:,.1f}"))
