"""Welk twaalfmaandsvenster hoort bij de nulmeting in hoofdstuk 4?

We proberen drie lezingen van 'de laatste twaalf maanden' en vergelijken de
optelsom met het getal uit het startpakket (2.723.799 sessies).
"""
from concurrent.futures import ThreadPoolExecutor

import shop
import sql

VENSTERS = {
    "A 12 hele maanden (2025-09-01 t/m 2026-08-31)": "SINCE 2025-09-01 UNTIL 2026-08-31",
    "B relatief (-12m t/m vandaag)": "SINCE -12m UNTIL today",
    "C rollend jaar (2025-09-22 t/m 2026-09-21)": "SINCE 2025-09-22 UNTIL 2026-09-21",
}
# Shops uit de tabel van hoofdstuk 4 (Lazamani EN en Sockwell EN staan er niet in).
IN_TABEL = [s for s in shop.SHOPS if s not in {"lazamani_en", "sockwell_en"}]


def haal(argument):
    sleutel, periode = argument
    df = sql.vraag(sleutel, f"FROM sessions SHOW sessions {periode}")
    return sleutel, (int(df["sessions"].iloc[0]) if len(df) else 0)


if __name__ == "__main__":
    for naam, periode in VENSTERS.items():
        with ThreadPoolExecutor(max_workers=6) as pool:
            uitkomst = dict(pool.map(haal, [(s, periode) for s in IN_TABEL]))
        totaal = sum(uitkomst.values())
        print(f"{naam:<48} totaal sessies = {totaal:>10,}".replace(",", "."))
    print("\nstartpakket hoofdstuk 4                          totaal sessies =  2.723.799")
