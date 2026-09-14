import os,subprocess,json,re,datetime as dt,threading
from shops import SHOPS, API
FROM=(dt.date(2026,9,14)-dt.timedelta(days=800)).isoformat()+"T00:00:00Z"
os.makedirs('shop',exist_ok=True)
FIELDS="id,created_at,cancelled_at,financial_status,line_items,current_total_discounts"

import tempfile,time
_lock=threading.Lock()
def curl(url,tok,poging=0):
    hf=tempfile.NamedTemporaryFile(delete=False,suffix='.hdr')
    hf.close()
    r=subprocess.run(["curl","-sS","-m","90","-D",hf.name,"-H",f"X-Shopify-Access-Token: {tok}",url],
                     capture_output=True,text=True)
    try: hdr=open(hf.name,errors='replace').read()
    except Exception: hdr=''
    finally:
        try: os.unlink(hf.name)
        except Exception: pass
    code=0
    m=re.findall(r'HTTP/[\d.]+ (\d+)',hdr)
    if m: code=int(m[-1])
    if code in (429,500,502,503) and poging<6:
        time.sleep(2+poging*2); return curl(url,tok,poging+1)
    nxt=None
    mm=re.search(r'<([^>]+)>;\s*rel="next"',hdr)
    if mm: nxt=mm.group(1)
    try: body=json.loads(r.stdout)
    except Exception:
        if poging<4: time.sleep(2); return curl(url,tok,poging+1)
        body={}
    if not isinstance(body,dict): body={}
    return {"next":nxt,"code":code},body

def haal(naam,dom,ev):
    tok=os.environ.get(ev)
    if not tok: return
    base=f"https://{dom}.myshopify.com/admin/api/{API}"
    # ---- orders ----
    url=f"{base}/orders.json?status=any&limit=250&created_at_min={FROM}&fields={FIELDS}"
    regels=[];n=0
    while url:
        h,b=curl(url,tok)
        for o in b.get('orders') or []:
            if o.get('cancelled_at'): continue
            d=o['created_at'][:10]; n+=1
            for li in o.get('line_items') or []:
                q=li.get('quantity') or 0
                if q<=0: continue
                regels.append({"d":d,"sku":li.get('sku'),"v":li.get('variant_id'),
                    "p":li.get('product_id'),"q":q,
                    "pr":float(li.get('price') or 0),
                    "dis":float(li.get('total_discount') or 0),
                    "vt":li.get('variant_title'),"t":li.get('title')})
        url=h.get('next')
    with open(f'shop/{dom}_orders.json','w') as f: json.dump(regels,f)
    # ---- producten + varianten ----
    url=f"{base}/products.json?limit=250"
    prods=[]
    while url:
        h,b=curl(url,tok)
        for p in b.get('products') or []:
            for v in p.get('variants') or []:
                prods.append({"pid":p['id'],"vid":v['id'],"sku":v.get('sku'),
                  "titel":p.get('title'),"maat":v.get('title'),
                  "type":p.get('product_type'),"tags":p.get('tags'),
                  "vendor":p.get('vendor'),
                  "prijs":float(v.get('price') or 0),
                  "vanaf":float(v.get('compare_at_price') or 0) if v.get('compare_at_price') else None,
                  "vrd":v.get('inventory_quantity'),
                  "aangemaakt":(p.get('created_at') or '')[:10],
                  "gepubliceerd":(p.get('published_at') or '')[:10]})
        url=h.get('next')
    with open(f'shop/{dom}_products.json','w') as f: json.dump(prods,f)
    print(f"{naam:18s} {n:6,} orders  {len(regels):7,} regels  {len(prods):6,} varianten",flush=True)

ths=[threading.Thread(target=haal,args=s) for s in SHOPS]
for t in ths: t.start()
for t in ths: t.join()
print("klaar")
