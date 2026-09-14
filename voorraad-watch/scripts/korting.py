import json,glob,os,datetime as dt
from collections import defaultdict
BASE=os.path.dirname(os.path.abspath(__file__))
TODAY=dt.date(2026,9,14); NUWEEK=TODAY.isocalendar()[1]
ce=json.load(open(f'{BASE}/rows.json'))
info={r['mpn']:r for r in ce}
ean2mpn={r['ean']:r['mpn'] for r in ce if r.get('ean')}

# ---- 1. referentieprijs per SKU = hoogste werkelijk betaalde prijs ----
maxprijs=defaultdict(float); regels=[]
for f in glob.glob(f'{BASE}/shop/*_orders.json'):
    for r in json.load(open(f)):
        s=r.get('sku'); q=r.get('q') or 0
        mpn = s if s in info else ean2mpn.get(s)
        if not mpn or q<=0: continue
        netto=(r.get('pr') or 0) - (r.get('dis') or 0)/max(q,1)
        if netto<=0: continue
        maxprijs[mpn]=max(maxprijs[mpn], r.get('pr') or 0)
        regels.append((mpn, r['d'], q, netto))
print(f"regels met prijs: {len(regels):,}")

# ---- 2. per merk per week: aandeel stuks onder 92% van referentieprijs ----
perweek=defaultdict(lambda:[0,0])   # (merk,week)->[afgeprijsd, totaal]
diepte=defaultdict(list)
for mpn,d,q,netto in regels:
    ref=maxprijs[mpn]
    if ref<=0: continue
    dd=dt.date.fromisoformat(d); w=dd.isocalendar()[1]
    m=info[mpn]['brand']
    a=perweek[(m,w)]; a[1]+=q
    if netto < ref*0.92:
        a[0]+=q; diepte[(m,w)].append(1-netto/ref)

# ---- 3. huidige stand uit de live shop (compare_at_price) ----
live=defaultdict(lambda:[0,0])
for f in glob.glob(f'{BASE}/shop/*_products.json'):
    for v in json.load(open(f)):
        s=v.get('sku'); mpn = s if s in info else ean2mpn.get(s)
        if not mpn: continue
        m=info[mpn]['brand']
        live[m][1]+=1
        if v.get('vanaf') and v['vanaf']>v['prijs']*1.02: live[m][0]+=1

print("\n"+"="*92)
print("KORTINGSSEIZOEN PER MERK  (aandeel verkochte stuks onder 92% van de eigen referentieprijs)")
print("="*92)
print(f"{'merk':14s} {'basis':>6s} {'sale-periodes (weeknr)':38s} {'nu wk38':>8s} {'live in sale':>13s} {'diepte':>7s}")
uit={}
for m in sorted({k[0] for k in perweek}):
    ws={w:(perweek[(m,w)][0]/perweek[(m,w)][1]) for w in range(1,54) if perweek[(m,w)][1]>=20}
    if len(ws)<25: continue
    basis=sorted(ws.values())[len(ws)//2]          # mediaan = normaal niveau
    drempel=max(0.30, basis+0.20)
    hoog=sorted(w for w,v in ws.items() if v>=drempel)
    blokken=[]
    if hoog:
        cur=[hoog[0]]
        for w in hoog[1:]:
            if w-cur[-1]<=2: cur.append(w)
            else: blokken.append(cur); cur=[w]
        blokken.append(cur)
        blokken=[b for b in blokken if len(b)>=2]
    alle=[d for (mm,w),ds in diepte.items() if mm==m for d in ds]
    gem_d=sum(alle)/len(alle) if alle else 0
    lv=live[m]; lvp=round(100*lv[0]/lv[1]) if lv[1] else None
    nu=ws.get(NUWEEK)
    uit[m]={'basis':round(100*basis),'drempel':round(100*drempel),
            'blokken':[[b[0],b[-1]] for b in blokken],
            'nu':round(100*nu) if nu is not None else None,
            'live_pct':lvp,'diepte':round(100*gem_d),
            'week':{w:round(100*v) for w,v in ws.items()}}
    bl=' + '.join(f"{b[0]}-{b[-1]}" for b in blokken) or '—'
    print(f"{m[:14]:14s} {round(100*basis):5d}% {bl:38s} "
          f"{(str(round(100*nu))+'%') if nu is not None else '—':>8s} "
          f"{(str(lvp)+'%') if lvp is not None else '—':>13s} {str(round(100*gem_d))+'%':>7s}")
json.dump(uit,open(f'{BASE}/korting_data.json','w'))
print("\n-> korting_data.json geschreven")
