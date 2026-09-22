"""KEEN NL: trechter over tijd en per verkeersbron, op de schone periode."""
import pandas as pd
import sql

SCHOON = "SINCE 2026-03-01 UNTIL 2026-08-31"
METEN = ("sessions, sessions_with_cart_additions, sessions_that_reached_checkout, "
         "sessions_that_completed_checkout")
pd.set_option("display.width", 220)


def af(df):
    df = df.copy()
    df["wagen%"] = df.sessions_with_cart_additions / df.sessions * 100
    df["afreken%"] = df.sessions_that_reached_checkout / df.sessions_with_cart_additions * 100
    df["order%"] = df.sessions_that_completed_checkout / df.sessions_that_reached_checkout * 100
    df["conv%"] = df.sessions_that_completed_checkout / df.sessions * 100
    return df.replace([float("inf"), float("-inf")], 0).fillna(0)


print("=== KEEN NL per maand ===")
m = af(sql.vraag("keen_nl", f"FROM sessions SHOW {METEN} GROUP BY month {SCHOON} ORDER BY month"))
m["maand"] = m.month.str[:7]
print(m[["maand", "sessions", "sessions_with_cart_additions", "wagen%",
         "sessions_that_reached_checkout", "afreken%",
         "sessions_that_completed_checkout", "order%", "conv%"]].to_string(
    index=False, float_format=lambda v: f"{v:,.2f}"))

print("\n=== KEEN NL per verkeersbron ===")
b = af(sql.vraag("keen_nl", f"FROM sessions SHOW {METEN} GROUP BY referrer_source "
                            f"{SCHOON} ORDER BY sessions DESC"))
b["aandeel%"] = b.sessions / b.sessions.sum() * 100
print(b[["referrer_source", "sessions", "aandeel%", "wagen%", "afreken%", "order%",
         "conv%"]].to_string(index=False, float_format=lambda v: f"{v:,.2f}"))

print("\n=== HEYDUDE NL per verkeersbron, ter vergelijking ===")
h = af(sql.vraag("heydude_nl", f"FROM sessions SHOW {METEN} GROUP BY referrer_source "
                               f"{SCHOON} ORDER BY sessions DESC"))
h["aandeel%"] = h.sessions / h.sessions.sum() * 100
print(h[["referrer_source", "sessions", "aandeel%", "wagen%", "afreken%", "order%",
         "conv%"]].to_string(index=False, float_format=lambda v: f"{v:,.2f}"))

print("\n=== KEEN NL: welke zoekmachines en welke campagnes ===")
for dim in ("referrer_name", "utm_source", "utm_medium", "utm_campaign"):
    d = af(sql.vraag("keen_nl", f"FROM sessions SHOW {METEN} GROUP BY {dim} {SCHOON} "
                                f"ORDER BY sessions DESC LIMIT 10"))
    print(f"\n--- {dim}")
    print(d[[dim, "sessions", "wagen%", "conv%"]].to_string(
        index=False, float_format=lambda v: f"{v:,.2f}"))
