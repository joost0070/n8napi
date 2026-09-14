"""Spiegelcontrole: staat dezelfde voorraad in alle shops en in ChannelEngine gelijk?"""
import json,glob,os,datetime as dt
from collections import defaultdict
B=os.path.dirname(os.path.abspath(__file__))
ce=json.load(open(f'{B}/rows.json')); info={r['mpn']:r for r in ce}
ean2={r['ean']:r['mpn'] for r in ce if r.get('ean')}

# centrale voorraad uit ChannelEngine (magazijn 1)
centraal={}
for f in glob.glob(f'{B}/stk/s*.json'):
    try: d=json.load(open(f))
    except: continue
    for o in d.get('Content') or []:
        centraal[o['MerchantProductNo']]={'vrd':o.get('Stock') or 0,'upd':(o.get('UpdatedAt') or '')[:10]}

# per shop
shops=defaultdict(dict)
for f in glob.glob(f'{B}/shop/*_products.json'):
    dom=os.path.basename(f).replace('_products.json','')
    for v in json.load(open(f)):
        s=v.get('sku'); q=v.get('vrd')
        if not s or q is None: continue
        shops[s][dom]=max(shops[s].get(dom,-10**9), q)

bev=[]
for sku,perdom in shops.items():
    mpn = sku if sku in info else ean2.get(sku)
    c = centraal.get(mpn,{}).get('vrd') if mpn else None
    waarden=list(perdom.values())
    lo,hi=min(waarden),max(waarden)
    ce_afw = (c is not None and c!=hi)
    if hi==lo and not ce_afw: continue
    r=info.get(mpn,{})
    bev.append({'sku':sku,'merk':r.get('brand'),'naam':str(r.get('name'))[:46],'maat':r.get('size'),
      'shops':perdom,'spreiding':hi-lo,'laag':hi<=10,'ce':c,'ce_afw':ce_afw,
      'prijs':r.get('price'),'upd':centraal.get(mpn,{}).get('upd')})

onderling=[x for x in bev if x['spreiding']>0]
ce_mis=[x for x in bev if x['ce_afw']]
urgent=[x for x in onderling if x['laag']]
print(f"SKU's in meerdere shops        : {sum(1 for v in shops.values() if len(v)>1):,}")
print(f"shops onderling niet gelijk    : {len(onderling):,}")
print(f"  waarvan voorraad <= 10 stuks : {len(urgent):,}   <- hier ontstaat overselling")
print(f"ChannelEngine wijkt af van shop: {len(ce_mis):,}")
print()
print("URGENT — lage voorraad die per kanaal verschilt")
print(f"{'merk':11s} {'artikel':40s} {'mt':>6s} {'CE':>4s}  standen per shop")
for x in sorted(urgent,key=lambda x:-x['spreiding'])[:15]:
    st=' '.join(f"{d.split('-')[0][:8]}:{q}" for d,q in sorted(x['shops'].items(),key=lambda y:-y[1]))
    print(f"{str(x['merk'])[:11]:11s} {x['naam']:40s} {str(x['maat']):>6s} {str(x['ce']):>4s}  {st}")
if ce_mis:
    print("\nChannelEngine vs webshop (voedt bol.com, Amazon, Kaufland, ANWB)")
    for x in sorted(ce_mis,key=lambda x: abs((x['ce'] or 0)-max(x['shops'].values())))[-10:]:
        st=' '.join(f"{d.split('-')[0][:8]}:{q}" for d,q in sorted(x['shops'].items(),key=lambda y:-y[1]))
        print(f"  {str(x['merk'])[:11]:11s} {x['naam'][:40]:40s} mt {str(x['maat']):>6s} CE={x['ce']} | {st}")
json.dump({'onderling':len(onderling),'urgent':len(urgent),'ce_mis':len(ce_mis),
           'lijst':[{k:v for k,v in x.items()} for x in sorted(onderling,key=lambda x:(not x['laag'],-x['spreiding']))[:60]]},
          open(f'{B}/spiegel.json','w'),ensure_ascii=False)
