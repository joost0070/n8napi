import json,glob,os,datetime as dt
from collections import defaultdict
BASE=os.path.dirname(os.path.abspath(__file__))
TODAY=dt.date(2026,9,14)
upd={}
for f in glob.glob(f'{BASE}/stk/s*.json'):
    try: d=json.load(open(f))
    except: continue
    for o in d.get('Content') or []:
        try: u=dt.datetime.fromisoformat(o['UpdatedAt']).date()
        except: continue
        upd[o['MerchantProductNo']]={'stock':o.get('Stock') or 0,'upd':u}
print('offers met timestamp:',len(upd))
rows=json.load(open(f'{BASE}/rows.json'))
buckets=defaultdict(lambda:[0,0.0])
brandbuck=defaultdict(lambda:defaultdict(float))
geenCE_recent=[];geenCE_oud=[]
for r in rows:
    if (r['stock'] or 0)<=0: continue
    u=upd.get(r['mpn'])
    if not u: continue
    d=(TODAY-u['upd']).days
    b='0-30 dgn' if d<=30 else '31-90 dgn' if d<=90 else '91-180 dgn' if d<=180 else '181-365 dgn' if d<=365 else '1-2 jaar' if d<=730 else '>2 jaar'
    buckets[b][0]+=1; buckets[b][1]+=r['value']
    brandbuck[r['brand']][b]+=r['value']
    if r['s52']==0:
        (geenCE_recent if d<=90 else geenCE_oud).append((r['value'],r,d))
orde=['0-30 dgn','31-90 dgn','91-180 dgn','181-365 dgn','1-2 jaar','>2 jaar']
print('\n=== LAATSTE VOORRAADMUTATIE (alle kanalen, ook webshop) ===')
tot=sum(v[1] for v in buckets.values())
for b in orde:
    n,v=buckets.get(b,[0,0])
    print(f"  {b:12s} {n:6,} SKU's  EUR {v:11,.0f}  {100*v/tot:5.1f}%")
print(f"  {'TOTAAL':12s} {sum(v[0] for v in buckets.values()):6,} SKU's  EUR {tot:11,.0f}")
rv=sum(x[0] for x in geenCE_recent); ov=sum(x[0] for x in geenCE_oud)
print(f"\n=== DE 'DEAD STOCK' VAN EUR 1,93 MLN ONTLEED ===")
print(f"  beweegt wel, maar niet via marktplaats (<=90 dgn): EUR {rv:,.0f}  ({len(geenCE_recent):,} SKU's)")
print(f"  staat ook echt stil (>90 dgn geen mutatie):        EUR {ov:,.0f}  ({len(geenCE_oud):,} SKU's)")
print('\n=== ECHT STILSTAAND PER MERK (>180 dgn geen mutatie) ===')
per=defaultdict(float)
for r in rows:
    if (r['stock'] or 0)<=0: continue
    u=upd.get(r['mpn'])
    if u and (TODAY-u['upd']).days>180: per[r['brand']]+=r['value']
for b,v in sorted(per.items(),key=lambda x:-x[1])[:12]:
    print(f"  {b[:20]:20s} EUR {v:11,.0f}")
print(f"  {'TOTAAL':20s} EUR {sum(per.values()):11,.0f}")
json.dump({'buckets':{b:buckets.get(b,[0,0]) for b in orde},
           'splits':{'beweegt':rv,'stil':ov},
           'stil_per_merk':dict(sorted(per.items(),key=lambda x:-x[1])[:12])},
          open(f'{BASE}/age_data.json','w'))
