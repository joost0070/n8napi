"""Rangschikking op verwachte impact, volgens dezelfde methode als hoofdstuk 4
maar op twee vensters, zodat zichtbaar wordt hoeveel het venster uitmaakt.

Methode (ongewijzigd overgenomen): breng alleen de eerste trechterstap
(sessie -> winkelwagen) naar het niveau van de beste shop; de stappen daarna
blijven gelijk. Waardeer de extra orders tegen de eigen AOV van de shop.
Dat is een bovengrens, geen belofte.
"""
import pandas as pd

TE_KLEIN = 20000  # shops onder dit aantal sessies per jaar laten we buiten de rangschikking


def rangschik(pad: str, factor: float, naam: str) -> pd.DataFrame:
    df = pd.read_pickle(pad)
    df = df[df.sleutel != "_totaal"].copy()
    df["aov"] = df.net_sales / df.orders

    beste = df.wagen_pct.max()
    winnaar = df.loc[df.wagen_pct.idxmax(), "shop"]

    df["extra_wagen"] = (beste - df.wagen_pct) / 100 * df.sessions
    df["extra_orders"] = (df.extra_wagen * df.afreken_pct / 100
                          * df.order_pct / 100)
    df["extra_omzet"] = df.extra_orders * df.aov
    # naar jaarbasis
    df["sessies_jaar"] = df.sessions * factor
    df["extra_orders_jaar"] = df.extra_orders * factor
    df["extra_omzet_jaar"] = df.extra_omzet * factor

    df = df[df.sessies_jaar >= TE_KLEIN]
    df = df.sort_values("extra_omzet_jaar", ascending=False)
    print(f"\n=== {naam} (beste shop = {winnaar}, {beste:.2f}%) ===")
    print(df[["shop", "sessies_jaar", "wagen_pct", "aov", "extra_orders_jaar",
              "extra_omzet_jaar"]].to_string(
        index=False,
        float_format=lambda v: f"{v:,.2f}",
        formatters={"sessies_jaar": lambda v: f"{v:,.0f}"}))
    return df


oud = rangschik("nulmeting.pkl", 1.0, "venster A: laatste 12 maanden (jouw hoofdstuk 4)")
nieuw = rangschik("nulmeting_recent.pkl", 4.0,
                  "venster B: juni t/m augustus 2026, naar jaarbasis (x4)")

samen = (oud[["shop", "extra_omzet_jaar"]].rename(columns={"extra_omzet_jaar": "12mnd"})
         .merge(nieuw[["shop", "extra_omzet_jaar"]].rename(
             columns={"extra_omzet_jaar": "recent"}), on="shop", how="outer")
         .fillna(0))
samen["rang_12mnd"] = samen["12mnd"].rank(ascending=False).astype(int)
samen["rang_recent"] = samen["recent"].rank(ascending=False).astype(int)
samen["verschuiving"] = samen.rang_12mnd - samen.rang_recent
print("\n=== verschuiving in rangorde ===")
print(samen.sort_values("recent", ascending=False).to_string(
    index=False, float_format=lambda v: f"{v:,.0f}"))
