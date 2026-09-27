"""Tofvel-deepdive stap 0: toegang, scopes en gevulde gegevens per Tofvel-shop."""
import shop, sql

NODIG = ["read_orders", "read_all_orders", "read_products", "read_customers",
         "read_reports", "read_analytics", "read_returns", "read_discounts",
         "read_price_rules", "read_inventory"]
SHOPS = ["tofvel_nl", "tofvel_de", "tofvel_en"]

for s in SHOPS:
    d = shop.gql(s, """{ shop { name primaryDomain { host } currencyCode ianaTimezone }
      currentAppInstallation { accessScopes { handle } } }""")
    scopes = {x["handle"] for x in d["currentAppInstallation"]["accessScopes"]}
    mist = [n for n in NODIG if n not in scopes]
    print(f"\n{s}: {d['shop']['name']} {d['shop']['primaryDomain']['host']} "
          f"{d['shop']['currencyCode']} {d['shop']['ianaTimezone']}")
    print(f"  {len(scopes)} scopes; ontbrekend: {mist or 'geen'}")
    print("  ", sorted(scopes))
