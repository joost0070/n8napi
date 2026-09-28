"""Weekhistorie van voorraad voor de best verkopende modellen.

Per week de eindstand en het aantal dagen uit voorraad, 400 dagen terug. Daaruit:
  - hoe lang een uitverkochte bestseller leeg stond voordat hij terugkwam
    (de werkelijke hersteltijd per merk)
  - of een model vorig jaar in dezelfde weken leeg stond
De voorraad is gespiegeld over de shops, dus per artikel volstaat één shop.
"""
import os, json, time, glob
from collections import defaultdict
from ql_voorraad import ql
from shops import SHOPS

B = os.path.dirname(os.path.abspath(__file__))
tok = {d: os.environ.get(e) for n, d, e in SHOPS}
os.makedirs(f'{B}/wk', exist_ok=True)

ce = json.load(open(f'{B}/rows.json'))
info = {r['mpn']: r for r in ce}
ean2 = {r['ean']: r['mpn'] for r in ce if r.get('ean')}
def naar(s): return s if s in info else ean2.get(s)

# ---- welke modellen: top 150 op 12 maanden + alles wat de laatste 28 dagen verkocht ----
tempo = {x['mpn']: x for x in json.load(open(f'{B}/tempo_ql.json'))}
model_12 = defaultdict(int)
for m, t in tempo.items():
    r = info.get(m)
    if r: model_12[r['parent'] or r['name']] += t['stuks_jaar']
model_28 = defaultdict(int)
for f in glob.glob(f'{B}/ql28/*.json'):
    for r in json.load(open(f)):
        m = naar(r['product_variant_sku'])
        if m:
            model_28[info[m]['parent'] or info[m]['name']] += int(r['inventory_units_sold'] or 0)
top = {p for p, _ in sorted(model_12.items(), key=lambda x: -x[1])[:150]}
top |= {p for p, _ in sorted(model_28.items(), key=lambda x: -x[1])[:60]}

skus = [r['mpn'] for r in ce if (r['parent'] or r['name']) in top]
print(f"modellen: {len(top)} | maten: {len(skus)}")

# ---- per artikel één shop kiezen waar hij in staat ----
aanwezig = defaultdict(set)
for f in glob.glob(f'{B}/ql/*.json'):
    dom = os.path.basename(f)[:-5]
    for r in json.load(open(f)):
        m = naar(r['product_variant_sku'])
        if m: aanwezig[m].add(dom)
voorkeur = ['rge9fj-je', 'sockwell-b2c-nl', 'tofvel-nl', 'lazamani-nl', 'heydude-nl', 'keen-nl',
            'toni-pons-nl', 'jan-jansen-nl', 'ns3a4j-i1', 'bartogi-nl', 'bartogi-de']
per_shop = defaultdict(list)
for m in skus:
    doms = aanwezig.get(m)
    if not doms: continue
    dom = next((d for d in voorkeur if d in doms), sorted(doms)[0])
    # Shopify-SKU is de EAN; ChannelEngine gebruikt hetzelfde nummer
    per_shop[dom].append(info[m].get('ean') or m)

for dom, lijst in per_shop.items():
    for i in range(0, len(lijst), 80):
        pad = f'{B}/wk/{dom}_{i//80}.json'
        if os.path.exists(pad): continue
        deel = lijst[i:i+80]
        inlijst = ",".join(f"'{s}'" for s in deel)
        q = ("FROM inventory SHOW ending_inventory_units, days_out_of_stock, inventory_units_sold "
             f"GROUP BY week, product_variant_sku WHERE product_variant_sku IN ({inlijst}) "
             "SINCE -400d UNTIL today LIMIT 100000")
        rows, err = ql(dom, tok[dom], q)
        if err:
            print(f"{dom} blok {i//80}: FOUT {str(err)[:120]}", flush=True)
            continue
        json.dump(rows, open(pad, 'w'))
        print(f"{dom:18s} blok {i//80}: {len(rows):6,} weekregels", flush=True)
        time.sleep(2)
print("klaar")
