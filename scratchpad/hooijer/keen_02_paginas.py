"""KEEN NL: waar landt het verkeer en wat doet het daar?"""
import pandas as pd
import sql

SCHOON = "SINCE 2026-03-01 UNTIL 2026-08-31"
METEN = ("sessions, sessions_with_cart_additions, sessions_that_completed_checkout")
pd.set_option("display.width", 220, "display.max_colwidth", 52)


def af(df):
    df = df.copy()
    df["wagen%"] = df.sessions_with_cart_additions / df.sessions * 100
    df["conv%"] = df.sessions_that_completed_checkout / df.sessions * 100
    return df.replace([float("inf"), float("-inf")], 0).fillna(0)


def soort(pad):
    if pad == "/":
        return "homepage"
    for stuk, naam in (("/products/", "productpagina"), ("/collections/", "collectie"),
                       ("/pages/", "inhoudspagina"), ("/blogs/", "blog"),
                       ("/search", "zoeken"), ("/account", "account"),
                       ("/policies/", "voorwaarden"), ("/apps/", "app")):
        if pad.startswith(stuk):
            return naam
    return "overig"


for shop_sleutel, naam in (("keen_nl", "KEEN NL"), ("heydude_nl", "HEYDUDE NL")):
    df = af(sql.vraag(shop_sleutel, f"FROM sessions SHOW {METEN} GROUP BY landing_page_path "
                                    f"{SCHOON} ORDER BY sessions DESC LIMIT 400"))
    df["soort"] = df.landing_page_path.map(soort)
    tot = df.sessions.sum()
    g = df.groupby("soort").agg(
        sessies=("sessions", "sum"),
        wagen=("sessions_with_cart_additions", "sum"),
        orders=("sessions_that_completed_checkout", "sum")).reset_index()
    g["aandeel%"] = g.sessies / tot * 100
    g["wagen%"] = g.wagen / g.sessies * 100
    g["conv%"] = g.orders / g.sessies * 100
    print(f"\n=== {naam}: landingspagina naar soort (top 400 paden, {tot:,} sessies) ==="
          .replace(",", "."))
    print(g.sort_values("sessies", ascending=False).to_string(
        index=False, float_format=lambda v: f"{v:,.2f}"))
    if shop_sleutel == "keen_nl":
        keen = df

print("\n\n=== KEEN NL: 20 grootste landingspagina's ===")
print(keen.head(20)[["landing_page_path", "sessions", "wagen%", "conv%"]].to_string(
    index=False, float_format=lambda v: f"{v:,.2f}"))

print("\n=== KEEN NL: pagina's met veel verkeer en bijna geen wagen (>=500 sessies) ===")
slecht = keen[(keen.sessions >= 500) & (keen["wagen%"] < 2.0)].sort_values(
    "sessions", ascending=False)
print(slecht[["landing_page_path", "sessions", "wagen%", "conv%"]].to_string(
    index=False, float_format=lambda v: f"{v:,.2f}") if len(slecht) else "  (geen)")
print(f"  samen {slecht.sessions.sum():,} sessies".replace(",", "."))
