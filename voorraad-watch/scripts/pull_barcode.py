"""SKU -> barcode per shop, voor shops waar de SKU geen EAN is (Keen: '1004347-7')."""
import json, os, sys, urllib.request, time
from shops import SHOPS, API
uit = {}
for naam, dom, env in SHOPS:
    if len(sys.argv) > 1 and dom not in sys.argv[1:]: continue
    tok = os.environ.get(env); cur = None; n = 0
    while True:
        q = '{ productVariants(first: 250%s) { pageInfo { hasNextPage endCursor } nodes { sku barcode } } }' % (f', after: "{cur}"' if cur else '')
        req = urllib.request.Request(f'https://{dom}.myshopify.com/admin/api/{API}/graphql.json', data=json.dumps({'query': q}).encode(),
                                     headers={'X-Shopify-Access-Token': tok, 'Content-Type': 'application/json'})
        d = json.load(urllib.request.urlopen(req, timeout=60))['data']['productVariants']
        for v in d['nodes']:
            if v['sku'] and v['barcode'] and v['sku'] != v['barcode']: uit[v['sku']] = v['barcode']; n += 1
        if not d['pageInfo']['hasNextPage']: break
        cur = d['pageInfo']['endCursor']; time.sleep(0.5)
    print(f'{naam:18s} {n:6,} sku≠barcode')
json.dump(uit, open('sku_barcode.json', 'w'))
