"""Verse data voor de uitverkoopradar.

1. ShopifyQL per shop, laatste 28 dagen: eindstand, verkocht, dagen uit voorraad.
2. ChannelEngine-orders laatste 28 dagen (marktplaatsen).
"""
import os, json, time, subprocess, datetime as dt
from ql_voorraad import ql
from shops import SHOPS

B = os.path.dirname(os.path.abspath(__file__))
tok = {d: os.environ.get(e) for n, d, e in SHOPS}
os.makedirs(f'{B}/ql28', exist_ok=True)
os.makedirs(f'{B}/ord28', exist_ok=True)

Q = ("FROM inventory SHOW ending_inventory_units, inventory_units_sold, days_out_of_stock "
     "GROUP BY product_variant_sku SINCE -28d UNTIL today LIMIT 100000")

for naam, dom, ev in SHOPS:
    pad = f'{B}/ql28/{dom}.json'
    if os.path.exists(pad):
        print(f"{naam:18s} al binnen", flush=True)
        continue
    t = time.time()
    rows, err = ql(dom, tok[dom], Q)
    if err:
        print(f"{naam:18s} FOUT {str(err)[:100]}", flush=True)
        continue
    rows = [r for r in rows if r.get('product_variant_sku')]
    json.dump(rows, open(pad, 'w'))
    print(f"{naam:18s} {len(rows):6,} artikelen in {time.time()-t:.0f}s", flush=True)
    time.sleep(2)

# ---- ChannelEngine: orders laatste 28 dagen ----
van = (dt.date.today() - dt.timedelta(days=28)).isoformat() + "T00:00:00Z"
pagina = 1
totaal = 0
while True:
    url = f"https://hooijerfootwear.channelengine.net/api/v2/orders?fromDate={van}&page={pagina}"
    r = subprocess.run(["curl", "-sS", "--retry", "3", "-m", "60", url], capture_output=True, text=True)
    try:
        d = json.loads(r.stdout)
    except Exception:
        print("CE-fout op pagina", pagina)
        break
    c = d.get('Content') or []
    if not c:
        break
    json.dump(d, open(f'{B}/ord28/o{pagina}.json', 'w'))
    totaal += len(c)
    pagina += 1
print(f"ChannelEngine: {totaal} orders sinds {van[:10]}")
print("klaar")
