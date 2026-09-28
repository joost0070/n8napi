"""Haalt in één keer alle data op die de uitverkoopradar nodig heeft.

Draaien in een lege datamap (de routine doet dat elke ochtend):
    mkdir -p /tmp/radar && cd /tmp/radar && python3 <repo>/voorraad-watch/scripts/ophalen.py

Wat er in de datamap komt:
  rows.json            ChannelEngine artikelstam, één regel per maat
  ord/  ord28/         ChannelEngine-orders: 400 dagen en de laatste 28 dagen
  shop/                Shopify per shop: orders 800 dagen en producten (prijs, van-prijs, online)
  ql/  ql28/           ShopifyQL per shop: verkocht, eindstand en dagen uit voorraad (365 en 28 dagen)
  sku_barcode.json     SKU -> barcode voor shops met eigen SKU's (Keen)
  tempo_ql.json        12-maandstempo per maat op de dagen dat hij leverbaar was

Sleutels: ChannelEngine via de proxy, Shopify via de omgevingsvariabelen SHOPIFY_TOKEN_*.
"""
import os, sys, json, glob, time, subprocess, datetime as dt, threading, statistics
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
CE = "https://hooijerfootwear.channelengine.net/api/v2"
VANDAAG = dt.date.today()


def stap(naam):
    print(f"\n== {naam} ({dt.datetime.now():%H:%M:%S})", flush=True)


def ce_get(url, pogingen=5):
    for i in range(pogingen):
        r = subprocess.run(["curl", "-sS", "-m", "90", url], capture_output=True, text=True)
        try:
            d = json.loads(r.stdout)
            if isinstance(d, dict) and d.get('Content') is not None:
                return d
        except Exception:
            pass
        time.sleep(2 + 3 * i)
    return None


def seizoen(s):
    s = (s or '').lower()
    if 'herfst' in s or 'winter' in s or 'autumn' in s: return 'FW'
    if 'lente' in s or 'zomer' in s or 'spring' in s or 'summer' in s: return 'SS'
    if 'alle' in s or 'all' in s: return 'ALL'
    return 'ONBEKEND'


# ---- 1. ChannelEngine artikelstam ----
def artikelstam():
    stap("ChannelEngine: artikelstam")
    eerste = ce_get(f"{CE}/products?page=1")
    if not eerste:
        sys.exit("ChannelEngine niet bereikbaar")
    paginas = -(-eerste['TotalCount'] // eerste['ItemsPerPage'])
    with ThreadPoolExecutor(6) as ex:
        rest = list(ex.map(lambda p: ce_get(f"{CE}/products?page={p}"), range(2, paginas + 1)))
    rows = []
    for d in [eerste] + rest:
        for p in (d or {}).get('Content') or []:
            if not p.get('ParentMerchantProductNo'):
                continue                      # alleen maten, geen hoofdartikelen
            ed = {e['Key']: e['Value'] for e in p.get('ExtraData') or []}
            s = ed.get('seizoen_NL') or ed.get('seizoen_EN')
            rows.append({'mpn': p['MerchantProductNo'], 'parent': p.get('ParentMerchantProductNo'),
                         'name': p.get('Name'), 'brand': (p.get('Brand') or ed.get('merk') or 'ONBEKEND').strip(),
                         'size': p.get('Size'), 'color': p.get('Color'), 'ean': p.get('Ean'),
                         'stock': p.get('Stock') or 0, 'price': p.get('Price') or 0.0,
                         'purchase': p.get('PurchasePrice'), 'active': p.get('IsActive'),
                         'season': s, 'season_year': ed.get('Seizoensjaar'), 'season_code': seizoen(s)})
    ontbreekt = sum(1 for d in rest if not d)
    json.dump(rows, open('rows.json', 'w'))
    print(f"{len(rows):,} maten uit {paginas} pagina's" + (f" (LET OP: {ontbreekt} pagina's mislukt)" if ontbreekt else ""))


# ---- 2. ChannelEngine orders ----
def ce_orders():
    stap("ChannelEngine: orders 400 dagen")
    os.makedirs('ord', exist_ok=True); os.makedirs('ord28', exist_ok=True)
    van = (VANDAAG - dt.timedelta(days=400)).isoformat() + "T00:00:00Z"
    grens28 = (VANDAAG - dt.timedelta(days=28)).isoformat()
    pagina, n, n28 = 1, 0, 0
    while True:
        d = ce_get(f"{CE}/orders?fromDate={van}&page={pagina}")
        c = (d or {}).get('Content') or []
        if not c:
            break
        json.dump(d, open(f'ord/o{pagina}.json', 'w'))
        recent = [o for o in c if (o.get('OrderDate') or '')[:10] >= grens28]
        if recent:
            json.dump({'Content': recent}, open(f'ord28/o{pagina}.json', 'w'))
        n += len(c); n28 += len(recent); pagina += 1
    print(f"{n:,} orders, waarvan {n28:,} in de laatste 28 dagen")


# ---- 3. Shopify orders en producten ----
def shopify():
    stap("Shopify: orders 800 dagen en producten")
    import pull_shopify  # noqa: F401  (draait bij import, schrijft naar shop/)


# ---- 4. ShopifyQL ----
def shopifyql():
    from ql_voorraad import ql
    from shops import SHOPS
    for dagen, map_ in ((365, 'ql'), (28, 'ql28')):
        stap(f"ShopifyQL: {dagen} dagen")
        os.makedirs(map_, exist_ok=True)
        q = ("FROM inventory SHOW ending_inventory_units, inventory_units_sold, days_out_of_stock "
             f"GROUP BY product_variant_sku SINCE -{dagen}d UNTIL today LIMIT 100000")
        for naam, dom, env in SHOPS:
            tok = os.environ.get(env)
            if not tok:
                print(f"{naam:18s} geen token"); continue
            rows, err = ql(dom, tok, q)
            if err:
                print(f"{naam:18s} FOUT {str(err)[:80]}"); continue
            rows = [r for r in rows if r.get('product_variant_sku')]
            json.dump(rows, open(f'{map_}/{dom}.json', 'w'))
            print(f"{naam:18s} {len(rows):6,} artikelen", flush=True)
            time.sleep(2)


# ---- 5. SKU -> barcode ----
def barcodes():
    # Alleen shops waarvan de SKU's meestal geen EAN zijn (Keen: '1004347-7'); de rest koppelt
    # al op EAN. Scheelt ~10 minuten ten opzichte van alle shops langslopen.
    stap("Shopify: SKU -> barcode")
    doms = []
    for f in glob.glob('shop/*_products.json'):
        skus = [str(v.get('sku') or '') for v in json.load(open(f))]
        skus = [x for x in skus if x]
        if skus and sum(1 for x in skus if not x.isdigit()) / len(skus) > 0.3:
            doms.append(os.path.basename(f)[:-len('_products.json')])
    print('shops met eigen SKU\'s:', ', '.join(doms) or 'geen')
    if doms:
        subprocess.run([sys.executable, os.path.join(HIER, 'pull_barcode.py')] + doms, check=False)


# ---- 6. 12-maandstempo op leverbare dagen ----
def tempo():
    stap("12-maandstempo")
    ce = json.load(open('rows.json')); info = {r['mpn']: r for r in ce}
    ean0 = {str(r['ean']).lstrip('0'): r['mpn'] for r in ce if r.get('ean')}
    sku_bc = json.load(open('sku_barcode.json')) if os.path.exists('sku_barcode.json') else {}
    def naar(s):
        if s in info: return s
        s = str(s or ''); m = ean0.get(s.lstrip('0'))
        return m or (ean0.get(str(sku_bc[s]).lstrip('0')) if s in sku_bc else None)
    verkocht, uit = defaultdict(int), defaultdict(list)
    for f in glob.glob('ql/*.json'):
        for r in json.load(open(f)):
            m = naar(r['product_variant_sku'])
            if not m: continue
            try:
                verkocht[m] += max(int(float(r['inventory_units_sold'] or 0)), 0)
                uit[m].append(min(max(int(float(r['days_out_of_stock'] or 0)), 0), 365))
            except Exception:
                pass
    grens = (VANDAAG - dt.timedelta(days=365)).isoformat()
    for f in glob.glob('ord/o*.json'):
        for o in json.load(open(f)).get('Content') or []:
            if (o.get('OrderDate') or '')[:10] < grens: continue
            for l in o.get('Lines') or []:
                if l.get('Status') != 'CANCELED' and l.get('MerchantProductNo') in info:
                    verkocht[l['MerchantProductNo']] += l.get('Quantity') or 0
    uitv = []
    for m, n in verkocht.items():
        d = int(statistics.median(uit[m])) if uit.get(m) else 0
        lever = max(365 - d, 28 if d >= 330 else 14)
        uitv.append({'mpn': m, 'stuks_jaar': n, 'tempo_wk': round(n / lever * 7, 3), 'dagen_uit': d})
    json.dump(uitv, open('tempo_ql.json', 'w'))
    print(f"{len(uitv):,} maten met een 12-maandstempo")


if __name__ == '__main__':
    t0 = time.time()
    artikelstam(); ce_orders(); shopifyql(); shopify(); barcodes(); tempo()
    print(f"\nklaar in {(time.time() - t0) / 60:.1f} min")
