import json,glob,os,datetime as dt
from collections import defaultdict
B=os.path.dirname(os.path.abspath(__file__))
TODAY=dt.date(2026,9,14); NU=TODAY.isocalendar()[1]
ce=json.load(open(f'{B}/rows.json')); info={r['mpn']:r for r in ce}
ean2={r['ean']:r['mpn'] for r in ce if r.get('ean')}
def stype(r): return 'NOOS' if str(r.get('season_year') or '').upper()=='NOOS' else r['season_code']

# twee VOLLEDIGE cycli van 52 weken, uitgelijnd op het begin van het najaar
C1=(dt.date(2024,9,2), dt.date(2025,8,31))
C2=(dt.date(2025,9,1), dt.date(2026,8,30))
cyc=defaultdict(lambda: defaultdict(int))   # (sleutel, cyclus) -> week -> stuks
def tel(mpn,d,q):
    r=info.get(mpn)
    if not r: return
    s=f"{r['brand']}|{stype(r)}"
    for naam,(a,b) in (('c1',C1),('c2',C2)):
        if a<=d<=b: cyc[(s,naam)][d.isocalendar()[1]]+=q
for f in glob.glob(f'{B}/shop/*_orders.json'):
    for r in json.load(open(f)):
        s=r.get('sku'); m=s if s in info else ean2.get(s)
        if m: tel(m, dt.date.fromisoformat(r['d']), r.get('q') or 0)
for f in glob.glob(f'{B}/ord/o*.json'):
    try: d=json.load(open(f))
    except: continue
    for o in d.get('Content') or []:
        try: od=dt.datetime.fromisoformat(o['OrderDate']).date()
        except: continue
        for l in o.get('Lines') or []:
            if l.get('Status')!='CANCELED': tel(l.get('MerchantProductNo'), od, l.get('Quantity') or 0)

# index = GEMIDDELDE van de weekaandelen per cyclus (niet de som van de stuks)
idx={}; dal={}; volume={}
sleutels={k[0] for k in cyc}
for s in sleutels:
    delen=[]
    for naam in ('c1','c2'):
        c=cyc[(s,naam)]; tot=sum(c.values())
        if tot<120: continue
        delen.append({w: c.get(w,0)/tot for w in range(1,54)})
    if not delen: continue
    i={w: sum(d[w] for d in delen)/len(delen) for w in range(1,54)}
    idx[s]=i; volume[s]=sum(sum(cyc[(s,n)].values()) for n in ('c1','c2'))
    glad={w: sum(i[((w-1+d+53)%53)+1] for d in (-1,0,1))/3 for w in range(1,54)}
    dal[s]=min(glad,key=lambda w:glad[w])

def venster(s):
    i=idx[s]; d=dal[s]; volg=[]; w=d
    for _ in range(53): volg.append(w); w=w%53+1
    cum=0; start=eind=None; piek=max(i,key=lambda x:i[x])
    for w in volg:
        cum+=i[w]
        if start is None and cum>=0.08: start=w
        if eind is None and cum>=0.92: eind=w
    return start,piek,eind

print("SEIZOENSVENSTER — twee volledige cycli, per cyclus genormaliseerd")
print(f"{'merk|type':26s} {'stuks':>7s} {'start':>6s} {'piek':>6s} {'eind':>6s} {'dal':>5s} {'nog te gaan':>12s}")
uit={}
for s in sorted(idx,key=lambda x:-volume[x]):
    if volume[s]<400: continue
    st,pk,ei=venster(s)
    # restaandeel vanaf nu tot het dal
    rest=0.0; w=NU; n=0
    while w!=dal[s] and n<53: rest+=idx[s][w]; w=w%53+1; n+=1
    uit[s]={'start':st,'piek':pk,'eind':ei,'dal':dal[s],'rest':round(rest,3),'weken':n,
            'stuks':volume[s],'idx':{str(k):round(v,5) for k,v in idx[s].items()}}
    print(f"{s[:26]:26s} {volume[s]:7,} {('wk '+str(st)):>6s} {('wk '+str(pk)):>6s} "
          f"{('wk '+str(ei)):>6s} {dal[s]:5d} {f'{100*rest:.0f}% / {n} wk':>12s}")
json.dump(uit,open(f'{B}/seizoen2.json','w'))

print("\nHUNTER FW per cyclus, weken 30-52 (aandeel van het jaar):")
for naam in ('c1','c2'):
    c=cyc[('Hunter|FW',naam)]; tot=sum(c.values())
    if tot: print(f"  {naam} (tot {tot:4d}): " + ' '.join(f"w{w}:{100*c.get(w,0)/tot:.0f}%" for w in range(30,53,2)))
