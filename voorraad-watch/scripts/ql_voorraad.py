"""Haalt voorraadhistorie uit Shopify via ShopifyQL (dataset 'inventory').

Levert per artikel wat nergens anders te krijgen is:
  ending_inventory_units   eindstand per maand  -> hoe lang ligt het er al
  days_out_of_stock        dagen niet leverbaar -> de juiste noemer voor verkooptempo
  inventory_units_sold     verkocht in de periode
  first_day_in_inventory   eerste dag in voorraad (binnen het venster)

Vereist de scope read_analytics. De dataset is uit ShopifyQL Notebooks gehaald
maar werkt via de Admin GraphQL API nog wel.
"""
import os,sys,time,json,subprocess
from shops import SHOPS, API

Q='query($q:String!){ shopifyqlQuery(query:$q){ tableData{ columns{name} rows } parseErrors } }'

def ql(dom, tok, query, pogingen=8):
    body=json.dumps({"query":Q,"variables":{"q":query}})
    for i in range(pogingen):
        r=subprocess.run(["curl","-sS","-m","90","-X","POST",
            "-H",f"X-Shopify-Access-Token: {tok}","-H","Content-Type: application/json",
            "-d",body,f"https://{dom}.myshopify.com/admin/api/{API}/graphql.json"],
            capture_output=True,text=True)
        try: r=json.loads(r.stdout)
        except Exception: time.sleep(5); continue
        if 'THROTTLED' in str(r.get('errors','')): time.sleep(10+5*i); continue
        d=(r.get('data') or {}).get('shopifyqlQuery') or {}
        if d.get('parseErrors'): return None, d['parseErrors']
        return (d.get('tableData') or {}).get('rows') or [], None
    return None, 'throttled'

def per_sku(dom, tok, dagen=365):
    """Eén regel per artikel: eindstand, verkocht, dagen uit voorraad."""
    return ql(dom, tok,
      "FROM inventory SHOW ending_inventory_units, inventory_units_sold, days_out_of_stock, "
      f"first_day_in_inventory GROUP BY product_variant_sku SINCE -{dagen}d UNTIL today LIMIT 1000")

def per_maand(dom, tok, sku, dagen=400):
    """Maandelijkse eindstand van één artikel - de month-end snapshot."""
    return ql(dom, tok,
      "FROM inventory SHOW ending_inventory_units, inventory_units_sold "
      f"GROUP BY month, product_variant_sku WHERE product_variant_sku = '{sku}' "
      f"SINCE -{dagen}d UNTIL today")

if __name__=='__main__':
    tok={d:os.environ.get(e) for n,d,e in SHOPS}
    if len(sys.argv)>2 and sys.argv[1]=='maand':
        sku=sys.argv[2]; dom=sys.argv[3] if len(sys.argv)>3 else 'sockwell-b2c-nl'
        rows,err=per_maand(dom,tok[dom],sku)
        if err: print('fout',err); sys.exit(1)
        for r in sorted(rows,key=lambda r:r['month']):
            print(f"  {r['month'][:7]}  eindstand {int(r['ending_inventory_units']):6,}  "
                  f"verkocht {r['inventory_units_sold']:>3s}")
    else:
        uit={}
        for naam,dom,ev in SHOPS:
            if not tok.get(dom): continue
            rows,err=per_sku(dom,tok[dom])
            if err: print(f"{naam}: {err}"); continue
            uit[dom]=[r for r in rows if r.get('product_variant_sku')]
            print(f"{naam:18s} {len(uit[dom]):5,} artikelen")
            time.sleep(2)
        json.dump(uit,open('ql_voorraad.json','w'))
