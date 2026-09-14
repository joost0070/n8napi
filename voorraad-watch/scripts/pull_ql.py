import os,time,json
from ql_voorraad import ql
from shops import SHOPS
tok={d:os.environ.get(e) for n,d,e in SHOPS}
os.makedirs('ql',exist_ok=True)
Q=("FROM inventory SHOW ending_inventory_units, days_out_of_stock, inventory_units_sold, "
   "first_day_in_inventory GROUP BY product_variant_sku SINCE -365d UNTIL today LIMIT 100000")
for naam,dom,ev in SHOPS:
    p=f'ql/{dom}.json'
    if os.path.exists(p): print(f"{naam:18s} overgeslagen"); continue
    t=time.time(); rows,err=ql(dom,tok[dom],Q)
    if err:
        print(f"{naam:18s} FOUT {str(err)[:90]}",flush=True); continue
    met=[r for r in rows if r.get('product_variant_sku')]
    json.dump(met,open(p,'w'))
    print(f"{naam:18s} {len(met):6,} artikelen in {time.time()-t:.0f}s",flush=True)
    time.sleep(3)
print('klaar')
