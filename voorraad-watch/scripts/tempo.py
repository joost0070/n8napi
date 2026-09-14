import json,glob,os,datetime as dt
from collections import defaultdict
B=os.path.dirname(os.path.abspath(__file__))
TODAY=dt.date(2026,9,14)
ce=json.load(open(f'{B}/rows.json')); info={r['mpn']:r for r in ce}
ean2={r['ean']:r['mpn'] for r in ce if r.get('ean')}

verkoop=defaultdict(list)          # mpn -> [(datum, aantal)]
for f in glob.glob(f'{B}/shop/*_orders.json'):
    for r in json.load(open(f)):
        s=r.get('sku'); m=s if s in info else ean2.get(s)
        if m and (r.get('q') or 0)>0: verkoop[m].append((dt.date.fromisoformat(r['d']), r['q']))
for f in glob.glob(f'{B}/ord/o*.json'):
    try: d=json.load(open(f))
    except: continue
    for o in d.get('Content') or []:
        try: od=dt.datetime.fromisoformat(o['OrderDate']).date()
        except: continue
        for l in o.get('Lines') or []:
            if l.get('Status')=='CANCELED': continue
            m=l.get('MerchantProductNo')
            if m in info and (l.get('Quantity') or 0)>0: verkoop[m].append((od,l['Quantity']))

rij=[]
for mpn,r in info.items():
    v=verkoop.get(mpn,[])
    if not v: continue
    v.sort()
    eerste,laatste=v[0][0],v[-1][0]
    stuks=sum(q for _,q in v)
    # alleen het laatste jaar, anders meet je oude collecties mee
    vj=[(d,q) for d,q in v if (TODAY-d).days<=365]
    if not vj: continue
    e2,l2=vj[0][0],vj[-1][0]
    dagen_actief=max((l2-e2).days+1, 7)
    tempo=sum(q for _,q in vj)/dagen_actief*7       # stuks per week TERWIJL het verkocht
    stil=(TODAY-l2).days
    vrd=r['stock'] or 0
    uitverkocht = vrd==0 and stil<=45
    rij.append({'mpn':mpn,'merk':r['brand'],'naam':r['name'],'maat':r['size'],
      'vrd':vrd,'stuks_jaar':sum(q for _,q in vj),'dagen_actief':dagen_actief,
      'tempo_wk':round(tempo,2),'dagen_stil':stil,'uitverkocht':uitverkocht,
      'prijs':r['price'],'weken_tot_leeg': round(vrd/tempo,1) if tempo>0 else None})

print(f"SKU's met verkoop in 12 mnd: {len(rij):,}")
uv=[x for x in rij if x['uitverkocht']]
print(f"waarvan NU uitverkocht met recente vraag: {len(uv):,}")
print(f"  hun gemeten vraag: {sum(x['stuks_jaar'] for x in uv):,} stuks — maar dat is een ONDERGRENS")

# hoe scheef meet ik? vergelijk tempo van uitverkochte vs voorradige SKU's
inv=[x for x in rij if x['vrd']>0]
def med(a): a=sorted(a); return a[len(a)//2] if a else 0
print(f"\nmediaan verkooptempo terwijl op voorraad:")
print(f"  SKU's die nu uitverkocht zijn : {med([x['tempo_wk'] for x in uv]):.2f} stuks/wk")
print(f"  SKU's die nog voorraad hebben : {med([x['tempo_wk'] for x in inv]):.2f} stuks/wk")

print("\n"+"="*96)
print("SOKKEN — zelfde inkoop, ander tempo (Sockwell, 12 mnd)")
print("="*96)
sw=[x for x in rij if x['merk']=='Sockwell']
sw.sort(key=lambda x:-x['tempo_wk'])
print(f"{'artikel':46s} {'mt':>6s} {'vrd':>5s} {'12mnd':>6s} {'akt.dgn':>7s} {'st/wk':>6s} {'wk leeg':>8s}")
for x in sw[:8]+sw[-5:]:
    if x['vrd']==0: rest='LEEG'
    elif x['weken_tot_leeg'] is not None: rest=f"{x['weken_tot_leeg']:.0f}"
    else: rest='-'
    print(f"{str(x['naam'])[:46]:46s} {str(x['maat']):>6s} {x['vrd']:5d} {x['stuks_jaar']:6d} "
          f"{x['dagen_actief']:7d} {x['tempo_wk']:6.2f} {rest:>8s}")
json.dump(rij,open(f'{B}/tempo.json','w'))
