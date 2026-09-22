"""Verklaart de maatdekking het lage winkelwagenpercentage?

We koppelen het verkeer per productpagina aan de beschikbare maten van datzelfde
product, en kijken of pagina's met weinig maten op voorraad slechter scoren.
"""
import pandas as pd
import sql

SCHOON = "SINCE 2026-03-01 UNTIL 2026-08-31"
METEN = "sessions, sessions_with_cart_additions, sessions_that_completed_checkout"
pd.set_option("display.width", 200, "display.max_colwidth", 46)


def dekking(sleutel):
    df = pd.read_pickle(f"assortiment_{sleutel}.pkl")
    g = df.groupby("handle").agg(
        titel=("titel", "first"), maten=("maat", "count"),
        op_voorraad=("voorraad", lambda v: (v > 0).sum()),
        stuks=("voorraad", "sum"), prijs=("prijs", "median")).reset_index()
    g["dekking%"] = g.op_voorraad / g.maten * 100
    return g


def verkeer(sleutel):
    df = sql.vraag(sleutel, f"FROM sessions SHOW {METEN} GROUP BY landing_page_path "
                            f"{SCHOON} ORDER BY sessions DESC LIMIT 500")
    df = df[df.landing_page_path.str.startswith("/products/")].copy()
    df["handle"] = df.landing_page_path.str.replace("/products/", "", regex=False)
    return df


for sleutel, naam in (("keen_nl", "KEEN NL"), ("heydude_nl", "HEYDUDE NL")):
    samen = verkeer(sleutel).merge(dekking(sleutel), on="handle", how="inner")
    samen["wagen%"] = samen.sessions_with_cart_additions / samen.sessions * 100

    groepen = pd.cut(samen["dekking%"], [-1, 0, 25, 50, 75, 101],
                     labels=["0% (uitverkocht)", "1-25%", "26-50%", "51-75%", "76-100%"])
    g = samen.groupby(groepen, observed=True).agg(
        paginas=("handle", "count"), sessies=("sessions", "sum"),
        wagen=("sessions_with_cart_additions", "sum"),
        orders=("sessions_that_completed_checkout", "sum")).reset_index()
    g["wagen%"] = g.wagen / g.sessies * 100
    g["conv%"] = g.orders / g.sessies * 100
    g["aandeel sessies%"] = g.sessies / g.sessies.sum() * 100
    print(f"\n=== {naam}: productpagina's naar maatdekking ===")
    print(g.to_string(index=False, float_format=lambda v: f"{v:,.2f}"))
    if sleutel == "keen_nl":
        keen = samen

print("\n\n=== KEEN NL: drukste productpagina's met hun maatdekking ===")
print(keen.sort_values("sessions", ascending=False).head(22)[
    ["handle", "sessions", "wagen%", "maten", "op_voorraad", "dekking%", "stuks", "prijs"]
].to_string(index=False, float_format=lambda v: f"{v:,.1f}"))

print("\n=== KEEN NL: Jasper en Zionic apart ===")
jas = keen[keen.handle.str.contains("jasper|zionic", case=False)]
print(jas[["handle", "sessions", "wagen%", "maten", "op_voorraad", "dekking%",
           "stuks", "prijs"]].to_string(index=False, float_format=lambda v: f"{v:,.1f}"))
print(f"  samen {jas.sessions.sum():,} sessies, "
      f"wagen {jas.sessions_with_cart_additions.sum()/jas.sessions.sum()*100:.2f}%"
      .replace(",", "."))
