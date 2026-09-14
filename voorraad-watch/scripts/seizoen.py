import json,glob,os,datetime as dt
from collections import defaultdict
BASE=os.path.dirname(os.path.abspath(__file__))
TODAY=dt.date(2026,9,14); NUWEEK=TODAY.isocalendar()[1]

# ---------- CE-artikelen als stamdata ----------
ce=json.load(open(f'{BASE}/rows.json'))
info={}
for r in ce:
    info[r['mpn']]={'merk':r['brand'],'maat':r['size'],'seizoen':r['season_code'],
                    'jaar':str(r['season_year'] or ''),'vrd':r['stock'],'prijs':r['price'],
                    'inkoop':r['purchase'],'naam':r['name'],'parent':r['parent'],'waarde':r['value']}
ean2mpn={r['ean']:r['mpn'] for r in ce if r.get('ean')}

# ---------- vraag samenvoegen: webshop + marktplaats ----------
vraag=defaultdict(int)          # (mpn, iso-jaar, week) -> stuks
korting=defaultdict(lambda:[0,0])   # (merk, iso-jaar, week) -> [stuks met korting, totaal]
merkweek=defaultdict(int)       # (merk, seizoen, week) -> stuks (over 2 jaar opgeteld)
bron=defaultdict(int)

for f in glob.glob(f'{BASE}/shop/*_orders.json'):
    for r in json.load(open(f)):
        s=r.get('sku'); q=r.get('q') or 0
        mpn = s if s in info else ean2mpn.get(s)
        if not mpn or q<=0: continue
        d=dt.date.fromisoformat(r['d']); y,w,_=d.isocalendar()
        vraag[(mpn,y,w)]+=q; bron['shopify']+=q
        m=info[mpn]['merk']
        k=korting[(m,y,w)]; k[1]+=q
        if (r.get('dis') or 0)>0: k[0]+=q

for f in glob.glob(f'{BASE}/ord/o*.json'):
    try: d=json.load(open(f))
    except: continue
    for o in d.get('Content') or []:
        try: od=dt.datetime.fromisoformat(o['OrderDate']).date()
        except: continue
        for l in o.get('Lines') or []:
            if l.get('Status')=='CANCELED': continue
            mpn=l.get('MerchantProductNo'); q=l.get('Quantity') or 0
            if mpn not in info or q<=0: continue
            y,w,_=od.isocalendar()
            vraag[(mpn,y,w)]+=q; bron['marktplaats']+=q

print(f"vraag samengevoegd: webshop {bron['shopify']:,} + marktplaats {bron['marktplaats']:,} stuks")

# ---------- seizoenscurve per merk x seizoen ----------
for (mpn,y,w),q in vraag.items():
    i=info[mpn]
    sz='NOOS' if i['jaar'].upper()=='NOOS' else i['seizoen']
    merkweek[(i['merk'],sz,w)]+=q

def venster(curve):
    """curve: dict week->stuks. Geeft start/piek/eind op basis van cumulatief aandeel."""
    tot=sum(curve.values())
    if tot<150: return None
    # roteer zodat het dal het beginpunt is
    wk=list(range(1,54))
    glad={w: sum(curve.get(((w-1+d-1)%53)+1,0) for d in range(-1,2))/3 for w in wk}
    dal=min(glad,key=lambda w:glad[w])
    volg=[((dal-1+i)%53)+1 for i in range(53)]
    cum=0; start=eind=piek=None; best=0
    for w in volg:
        v=curve.get(w,0)
        if v>best: best=v; piek=w
        cum+=v
        if start is None and cum>=0.05*tot: start=w
        if eind is None and cum>=0.95*tot: eind=w
    return {'start':start,'piek':piek,'eind':eind,'stuks':tot,
            'dal':dal,'curve':{w:curve.get(w,0) for w in wk}}

print("\n"+"="*86)
print("SEIZOENSVENSTER UIT DE DATA  (26 maanden vraag, alle kanalen)")
print("="*86)
print(f"{'merk':16s} {'seizoen':8s} {'stuks':>8s} {'start':>7s} {'piek':>6s} {'eind':>6s}  {'venster':>9s}")
vensters={}
for (merk,sz,w) in list(merkweek):
    pass
groepen=defaultdict(dict)
for (merk,sz,w),q in merkweek.items(): groepen[(merk,sz)][w]=q
for (merk,sz),c in sorted(groepen.items(), key=lambda x:-sum(x[1].values())):
    v=venster(c)
    if not v: continue
    lengte=((v['eind']-v['start'])%53)+1
    vensters[f"{merk}|{sz}"]={k:v[k] for k in ('start','piek','eind','stuks')}
    print(f"{merk[:16]:16s} {sz:8s} {v['stuks']:8,} {('wk '+str(v['start'])):>7s} "
          f"{('wk '+str(v['piek'])):>6s} {('wk '+str(v['eind'])):>6s}  {str(lengte)+' wk':>9s}")

# ---------- kortingsseizoen per merk ----------
print("\n"+"="*86)
print("KORTINGSSEIZOEN  (aandeel webshopstuks met korting, per week, 2 jaar gemiddeld)")
print("="*86)
perweek=defaultdict(lambda:[0,0])
for (m,y,w),(kq,tq) in korting.items(): 
    a=perweek[(m,w)]; a[0]+=kq; a[1]+=tq
merken=sorted({m for m,_ in perweek})
regimes={}
for m in merken:
    ws={w:(perweek[(m,w)][0]/perweek[(m,w)][1] if perweek[(m,w)][1]>=15 else None) for w in range(1,54)}
    geldig={w:v for w,v in ws.items() if v is not None}
    if len(geldig)<25: continue
    gem=sum(geldig.values())/len(geldig)
    drempel=max(0.35, gem*1.6)
    hoog=sorted(w for w,v in geldig.items() if v>=drempel)
    if not hoog: continue
    # aaneengesloten blokken vinden
    blokken=[];huidig=[hoog[0]]
    for w in hoog[1:]:
        if w-huidig[-1]<=2: huidig.append(w)
        else: blokken.append(huidig); huidig=[w]
    blokken.append(huidig)
    blokken=[b for b in blokken if len(b)>=3]
    regimes[m]={'gemiddeld':round(100*gem),'drempel':round(100*drempel),
                'blokken':[[b[0],b[-1]] for b in blokken],
                'nu':round(100*geldig.get(NUWEEK,0)) if NUWEEK in geldig else None,
                'week':{w:round(100*v) for w,v in geldig.items()}}
    bl=' + '.join(f"wk {b[0]}-{b[-1]}" for b in blokken) or '—'
    print(f"{m[:16]:16s} gemiddeld {round(100*gem):3d}%  sale-periodes: {bl:34s} nu: {regimes[m]['nu']}%")

json.dump({'vensters':vensters,'regimes':regimes,
           'curves':{f"{m}|{s}":c for (m,s),c in groepen.items()}},
          open(f'{BASE}/seizoen_data.json','w'))
json.dump({f"{k[0]}|{k[1]}|{k[2]}":v for k,v in vraag.items()}, open(f'{BASE}/vraag.json','w'))
print("\n-> seizoen_data.json + vraag.json geschreven")
