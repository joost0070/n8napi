"""Catalogusmarge per shop: verkoopprijs tegen kostprijs, over het hele assortiment.

Niet hetzelfde als de gerealiseerde marge (kortingen en mix ontbreken), maar wel
voor alle shops op dezelfde manier gemeten — en dat is wat een vergelijking nodig
heeft. We ijken hem tegen de shops waar Shopify's eigen marge wel klopt.
"""
from concurrent.futures import ThreadPoolExecutor
import pandas as pd
import shop
from keen_03_assortiment import haal

def doe(sleutel):
    try:
        df = haal(sleutel)
        df.to_pickle(f"assortiment_{sleutel}.pkl")
        return sleutel, len(df)
    except Exception as e:
        return sleutel, f"FOUT {e}"

if __name__ == "__main__":
    nog = [s for s in shop.SHOPS if s not in ("keen_nl", "heydude_nl")]
    with ThreadPoolExecutor(max_workers=4) as pool:
        for sleutel, uitkomst in pool.map(doe, nog):
            print(f"  {shop.LABELS[sleutel]:<16} {uitkomst}", flush=True)
