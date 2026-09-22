"""Hoeveel van de 12-maands sessies komt uit de piek die niets opleverde?

Voor Sockwell NL en Tofvel NL zit oktober 2025 t/m januari 2026 een uitbraak van
verkeer met een conversie die ver onder hun eigen huidige niveau ligt. We zetten
die periode af tegen het recente niveau van dezelfde shop.
"""
import pandas as pd
import sql

pd.set_option("display.width", 200)

GEVALLEN = {
    "sockwell_nl": "Sockwell NL",
    "tofvel_nl": "Tofvel NL",
    "tofvel_de": "Tofvel DE",
    "sockwell_de": "Sockwell DE",
    "lazamani_de": "Lazamani DE",
    "bartogi_de": "Bartogi DE",
}
PIEK = "SINCE 2025-10-01 UNTIL 2026-01-31"
NU = "SINCE 2026-06-01 UNTIL 2026-08-31"
METEN = ("sessions, sessions_with_cart_additions, sessions_that_completed_checkout")

rijen = []
for sleutel, naam in GEVALLEN.items():
    piek = sql.vraag(sleutel, f"FROM sessions SHOW {METEN} {PIEK}").iloc[0]
    nu = sql.vraag(sleutel, f"FROM sessions SHOW {METEN} {NU}").iloc[0]
    conv_piek = piek.sessions_that_completed_checkout / piek.sessions * 100
    conv_nu = nu.sessions_that_completed_checkout / nu.sessions * 100
    # Hoeveel sessies zouden er in de piek zijn geweest bij de huidige conversie?
    echt = (piek.sessions_that_completed_checkout / (conv_nu / 100)) if conv_nu else 0
    rijen.append({
        "shop": naam,
        "sessies piek okt-jan": int(piek.sessions),
        "conv% piek": conv_piek,
        "conv% nu": conv_nu,
        "orders piek": int(piek.sessions_that_completed_checkout),
        "sessies bij huidige conv": int(echt),
        "onverklaard": int(piek.sessions - echt),
    })

df = pd.DataFrame(rijen).sort_values("onverklaard", ascending=False)
print(df.to_string(index=False, float_format=lambda v: f"{v:,.2f}"))
print(f"\nonverklaarde sessies samen: {df.onverklaard.sum():,}".replace(",", "."))
print("ter vergelijking, 12-maands totaal alle shops: 2.873.327")
print(f"aandeel: {df.onverklaard.sum() / 2873327 * 100:.1f}%")
