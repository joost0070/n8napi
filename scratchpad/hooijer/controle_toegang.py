"""Levenstest: antwoordt elke shop op de Admin API en op ShopifyQL?"""
from concurrent.futures import ThreadPoolExecutor

import shop
import sql


def test(sleutel: str) -> dict:
    regel = {"sleutel": sleutel, "label": shop.LABELS.get(sleutel, sleutel)}
    try:
        info = shop.controleer(sleutel)
        regel["admin"] = "ok"
        regel["naam"] = info["name"]
        regel["valuta"] = info["currencyCode"]
        regel["tijdzone"] = info["ianaTimezone"]
    except Exception as fout:
        regel["admin"] = f"FOUT: {fout}"
        return regel
    try:
        df = sql.vraag(sleutel, "FROM sessions SHOW sessions SINCE -1m UNTIL today")
        regel["shopifyql"] = "ok"
        regel["sessies_30d"] = int(df["sessions"].iloc[0]) if len(df) else 0
    except Exception as fout:
        regel["shopifyql"] = f"FOUT: {fout}"
    return regel


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=6) as pool:
        rijen = list(pool.map(test, shop.SHOPS))
    breed = max(len(r["label"]) for r in rijen)
    for r in sorted(rijen, key=lambda r: -r.get("sessies_30d", -1)):
        print(f"{r['label']:<{breed}}  admin={r['admin']:<8} "
              f"shopifyql={r.get('shopifyql','-'):<8} "
              f"sessies 30d={r.get('sessies_30d','-'):>8}  "
              f"{r.get('naam','')} [{r.get('valuta','')}] {r.get('tijdzone','')}")
