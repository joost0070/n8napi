"""Verkooptempo op gemeten leverbaarheid.

Oud: dagen leverbaar benaderd met eerste tot laatste verkoopdatum.
Nieuw: 365 - days_out_of_stock uit ShopifyQL. Een maat die na drie weken
uitverkocht raakte krijgt nu zijn werkelijke noemer.
"""
import json,glob,os,statistics
from collections import defaultdict
B=os.path.dirname(os.path.abspath(__file__))
VENSTER=365
ce=json.load(open(f'{B}/rows.json')); info={r['mpn']:r for r in ce}
ean2={r['ean']:r['mpn'] for r in ce if r.get('ean')}
oud={x['mpn']:x for x in json.load(open(f'{B}/tempo.json'))}

# ---- ShopifyQL per SKU samenvoegen over de shops ----
uit=defaultdict(list); shopverkoop=defaultdict(int); eind=defaultdict(list)
for f in glob.glob(f'{B}/ql/*.json'):
    for r in json.load(open(f)):
        s=r['product_variant_sku']
        m = s if s in info else ean2.get(s)
        if not m: continue
        try: d=int(r['days_out_of_stock'] or 0)
        except Exception: continue
        uit[m].append(min(d,VENSTER))
        try: shopverkoop[m]+=int(r['inventory_units_sold'] or 0)
        except Exception: pass
        try: eind[m].append(int(r['ending_inventory_units'] or 0))
        except Exception: pass

# De voorraad is gespiegeld, dus de shops horen dezelfde dagen te melden.
# Waar ze verschillen nemen we de mediaan.
dagen_uit={m: int(statistics.median(v)) for m,v in uit.items()}
spreiding=[max(v)-min(v) for v in uit.values() if len(v)>1]
print(f"artikelen met ShopifyQL-historie : {len(dagen_uit):,}")
if spreiding:
    eens=sum(1 for x in spreiding if x==0)
    print(f"  shops eens over dagen-uit-voorraad: {eens:,}/{len(spreiding):,} ({100*eens/len(spreiding):.1f}%)")

nieuw=[]; verschoven=0; groot=[]
for m,o in oud.items():
    d=dagen_uit.get(m)
    n=o['stuks_jaar']
    if d is None:
        # geen historie: oude benadering aanhouden, maar markeren
        nieuw.append({**o,'dagen_uit':None,'dagen_lever':o['dagen_actief'],'bron':'benadering'})
        continue
    # Bijna het hele jaar uit voorraad maar toch verkopen: die twee spreken
    # elkaar tegen (nalevering, of een dag met kortstondige voorraad). Dan een
    # ruimere ondergrens, anders schiet het tempo omhoog op een enkele verkoop.
    lever = max(VENSTER-d, 28 if d>=330 else 14)
    t=n/lever*7
    if o['tempo_wk']>0 and abs(t-o['tempo_wk'])/o['tempo_wk']>0.25: verschoven+=1
    if n>=10 and o['tempo_wk']>0 and t>o['tempo_wk']*1.4: groot.append((t/o['tempo_wk'],o,t,d))
    nieuw.append({**o,'tempo_wk':round(t,3),'dagen_uit':d,'dagen_lever':lever,'bron':'gemeten'})

gem=[x for x in nieuw if x['bron']=='gemeten']
print(f"  tempo gemeten                   : {len(gem):,}")
print(f"  tempo nog benaderd              : {len(nieuw)-len(gem):,}")
print(f"  meer dan 25% verschoven         : {verschoven:,}")
print(f"\nGROOTSTE OPWAARTSE CORRECTIES (waren te laag ingeschat)")
print(f"{'merk':11s} {'artikel':44s} {'mt':>6s} {'12m':>4s} {'uit vrd':>8s} {'oud/wk':>7s} {'nieuw/wk':>9s}")
for f,o,t,d in sorted(groot,key=lambda x:-x[0])[:14]:
    r=info[o['mpn']]
    print(f"{str(o['merk'])[:11]:11s} {str(o['naam'])[:44]:44s} {str(o['maat']):>6s} {o['stuks_jaar']:4d} "
          f"{d:6d} d {o['tempo_wk']:7.2f} {t:9.2f}")
json.dump(nieuw,open(f'{B}/tempo_ql.json','w'))
print("\n-> tempo_ql.json geschreven")
