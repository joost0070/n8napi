"""KEEN NL: waar zitten de retouren, en wat kosten ze?"""
import pandas as pd
import sql

SCHOON = "SINCE 2026-03-01 UNTIL 2026-08-31"
pd.set_option("display.width", 210, "display.max_colwidth", 44)

kop = sql.vraag("keen_nl", f"FROM sales SHOW gross_sales, discounts, returns, net_sales, "
                           f"orders, net_items_sold {SCHOON}").iloc[0]
print("=== KEEN NL, maart t/m augustus 2026 ===")
print(f"  bruto-omzet   € {kop.gross_sales:>12,.0f}".replace(",", "."))
print(f"  kortingen     € {kop.discounts:>12,.0f}  ({-kop.discounts/kop.gross_sales*100:.1f}%)"
      .replace(",", "."))
print(f"  retouren      € {kop.returns:>12,.0f}  ({-kop.returns/kop.gross_sales*100:.1f}%)"
      .replace(",", "."))
print(f"  netto-omzet   € {kop.net_sales:>12,.0f}".replace(",", "."))

print("\n=== retourpercentage per maand ===")
m = sql.vraag("keen_nl", f"FROM sales SHOW gross_sales, returns, net_sales GROUP BY month "
                         f"{SCHOON} ORDER BY month")
m["maand"] = m.month.str[:7]
m["retour%"] = -m.returns / m.gross_sales * 100
print(m[["maand", "gross_sales", "returns", "retour%"]].to_string(
    index=False, float_format=lambda v: f"{v:,.2f}"))

print("\n=== producten met de meeste retouren in euro's ===")
p = sql.vraag("keen_nl", f"FROM sales SHOW gross_sales, returns, net_sales, net_items_sold "
                         f"GROUP BY product_title {SCHOON} ORDER BY returns ASC LIMIT 20")
p["retour%"] = -p.returns / p.gross_sales * 100
print(p[["product_title", "gross_sales", "returns", "retour%", "net_sales"]].to_string(
    index=False, float_format=lambda v: f"{v:,.0f}"))

print("\n=== ter vergelijking: retour% van de andere shops ===")
tab = pd.read_pickle("nulmeting_v2.pkl")
print(tab[tab.sessions >= 10000][["shop", "retour%", "korting%"]].sort_values(
    "retour%", ascending=False).to_string(index=False, float_format=lambda v: f"{v:,.1f}"))
