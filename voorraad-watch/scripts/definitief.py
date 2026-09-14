import json,glob,os,datetime as dt
from collections import defaultdict
B=os.path.dirname(os.path.abspath(__file__))
TODAY=dt.date(2026,9,14); NU=TODAY.isocalendar()[1]
LEVERTIJD=6; K=8
ce=json.load(open(f'{B}/rows.json')); info={r['mpn']:r for r in ce}
ean2={r['ean']:r['mpn'] for r in ce if r.get('ean')}
sz=json.load(open(f'{B}/seizoen2.json'))
tempo={x['mpn']:x for x in json.load(open(f'{B}/tempo.json'))}
def stype(r): return 'NOOS' if str(r.get('season_year') or '').upper()=='NOOS' else r['season_code']
def schoon(s): return str(s or '').encode('latin-1','ignore').decode('utf-8','ignore') or str(s or '')

# ---- levenscyclus: staat het artikel nog in een webshop? ----
live={}
for f in glob.glob(f'{B}/shop/*_products.json'):
    dom=os.path.basename(f).replace('_products.json','')
    for v in json.load(open(f)):
        s=v.get('sku'); m=s if s in info else ean2.get(s)
        if not m: continue
        cur=live.get(m,{'gepubliceerd':False,'prijs':None,'vanaf':None,'vrd':0,'shop':None,'aangemaakt':None})
        if v.get('gepubliceerd'): cur['gepubliceerd']=True
        if (v.get('vrd') or 0)>=cur['vrd']:
            cur.update({'prijs':v['prijs'],'vanaf':v.get('vanaf'),'vrd':v.get('vrd') or 0,'shop':dom})
        a=v.get('aangemaakt')
        if a and (cur['aangemaakt'] is None or a>cur['aangemaakt']): cur['aangemaakt']=a
        live[m]=cur

# ---- laatste verkoopdatum ----
laatste={}
for f in glob.glob(f'{B}/shop/*_orders.json'):
    for r in json.load(open(f)):
        s=r.get('sku'); m=s if s in info else ean2.get(s)
        if m:
            d=dt.date.fromisoformat(r['d'])
            if m not in laatste or d>laatste[m]: laatste[m]=d

# ---- tempo met krimp + plafond (zoals eerder) ----
model_stuks=defaultdict(int); model_dagen=defaultdict(int); model_sku=defaultdict(list)
for m,t in tempo.items():
    r=info.get(m)
    if not r: continue
    p=r['parent'] or r['name']
    model_stuks[p]+=t['stuks_jaar']; model_dagen[p]=max(model_dagen[p],t['dagen_actief']); model_sku[p].append(m)
model_tempo={p: model_stuks[p]/max(model_dagen[p],7)*7 for p in model_stuks}
merk_maat=defaultdict(lambda: defaultdict(float))
for m,t in tempo.items():
    r=info.get(m)
    if r and r['size']: merk_maat[r['brand']][str(r['size'])]+=t['stuks_jaar']
def aandeel(p,m):
    r=info[m]; eigen={x:tempo[x]['stuks_jaar'] for x in model_sku[p] if x in tempo}
    tot=sum(eigen.values())
    if tot>=25: return eigen.get(m,0)/tot
    mm=merk_maat.get(r['brand'],{}); t2=sum(mm.values())
    return (mm.get(str(r['size']),0)/t2) if t2 else 1/max(len(model_sku[p]),1)

rij=[]
for m,t in tempo.items():
    r=info.get(m)
    if not r: continue
    p=r['parent'] or r['name']; s=f"{r['brand']}|{stype(r)}"
    S=sz.get(s)
    if not S: continue
    # Een vlakke jaarcurve is geen seizoen. Piek/gemiddelde onder 2,2 = doorlopend,
    # en dan geldt een vaste horizon van 26 weken in plaats van een seizoenseinde.
    i=[v for v in S['idx'].values()]
    vlak = (max(i)/(sum(i)/len(i))) < 2.2
    if stype(r)=='NOOS' or vlak: rest, weken, doorlopend = 0.5, 26, True
    else: rest, weken, doorlopend = S['rest'], S['weken'], False
    prior=model_tempo[p]*aandeel(p,m); n=t['stuks_jaar']; w=n/(n+K)
    schat=w*t['tempo_wk']+(1-w)*prior
    lv=live.get(m,{})
    rij.append({'mpn':m,'merk':r['brand'],'naam':schoon(r['name']),'maat':schoon(r['size']),
      'type':stype(r),'vrd':r['stock'] or 0,'n12':n,'schat':schat,'rest':rest,'weken':weken,
      'prijs':r['price'],'inkoop':r['purchase'] or (r['price'] or 0)*0.45,
      'doorlopend':doorlopend,
      'live':lv.get('gepubliceerd',False),'shopprijs':lv.get('prijs'),'vanaf':lv.get('vanaf'),
      'laatste':str(laatste.get(m)) if m in laatste else None,'parent':p})

# plafond per model
per=defaultdict(list)
for x in rij: per[x['parent']].append(x)
for p,xs in per.items():
    som=sum(x['schat'] for x in xs); plaf=model_tempo.get(p,0)
    if som>plaf>0:
        f=plaf/som
        for x in xs: x['schat']*=f

for x in rij:
    x['schat']=round(x['schat'],2)
    x['restvraag']=round(x['schat']*x['weken'],1)
    x['projectie']=round(x['vrd']-x['restvraag'],1)
    x['weken_leeg']=round(x['vrd']/x['schat'],1) if x['schat']>0 else None
    x['jaren']=round(x['vrd']/(x['schat']*52),1) if x['schat']>0 else None

afgeprijsd=lambda x: bool(x['vanaf'] and x['shopprijs'] and x['vanaf']>x['shopprijs']*1.02)
genoeg=lambda x: x['n12']>=10 or model_stuks[x['parent']]>=30
verse=lambda x: x['laatste'] and (TODAY-dt.date.fromisoformat(x['laatste'])).days<=120

bij=[x for x in rij if x['projectie']<-0.5 and genoeg(x) and x['live'] and not afgeprijsd(x) and verse(x) and x['schat']>0.1]
for x in bij:
    weken_zonder=max(0,x['weken']-(x['weken_leeg'] or 0))
    x['redbaar']=round(max(0,weken_zonder-LEVERTIJD)*x['schat'],1)
    x['eur']=round(x['redbaar']*(x['prijs'] or 0))
    x['bestel']=int(round(min(weken_zonder*x['schat'], x['schat']*x['weken'])))
bij=[x for x in bij if x['bestel']>=3]
bij.sort(key=lambda x:-x['eur'])

afp=[x for x in rij if not x['doorlopend'] and x['projectie']>0.5 and x['restvraag']>0.2
     and not afgeprijsd(x) and x['vrd']>0 and genoeg(x)]
for x in afp: x['eur']=round(x['projectie']*x['inkoop'])
afp.sort(key=lambda x:-x['eur'])

print(f"BIJBESTELLEN : {len(bij):,} maten | {sum(x['bestel'] for x in bij):,} paar | EUR {sum(x['eur'] for x in bij):,}")
print(f"  uitgesloten: niet meer in een webshop {sum(1 for x in rij if not x['live']):,} | "
      f"zelf afgeprijsd {sum(1 for x in rij if afgeprijsd(x)):,} | "
      f"geen verkoop in 120 dgn {sum(1 for x in rij if not verse(x)):,}")
doorl=[x for x in rij if x['doorlopend'] and x['projectie']>0.5 and x['vrd']>0 and genoeg(x)]
for x in doorl: x['eur']=round(x['projectie']*x['inkoop'])
doorl.sort(key=lambda x:-x['eur'])
print(f"NU AFPRIJZEN (seizoen) : {len(afp):,} maten | EUR {sum(x['eur'] for x in afp):,}")
print(f"DOORLOPEND TE RUIM     : {len(doorl):,} maten | EUR {sum(x['eur'] for x in doorl):,}")
print("\nmerken als doorlopend behandeld: " + ', '.join(sorted({x['merk'] for x in rij if x['doorlopend']})))
print("\nTOP BIJBESTELLEN")
print(f"{'merk':10s} {'artikel + kleur':52s} {'mt':>6s} {'vrd':>4s} {'12m':>4s} {'/wk':>5s} {'leeg':>6s} {'seiz':>5s} {'bestel':>6s} {'laatste':>11s}")
for x in bij[:16]:
    leeg = 'LEEG' if x['vrd']==0 else f"{x['weken_leeg']:.0f}w"
    print(f"{x['merk'][:10]:10s} {x['naam'][:52]:52s} {x['maat'][:6]:>6s} {x['vrd']:4d} {x['n12']:4d} "
          f"{x['schat']:5.2f} {leeg:>6s} {x['weken']:5d} {x['bestel']:6d} {str(x['laatste']):>11s}")
print("\nTOP NU AFPRIJZEN")
for x in afp[:12]:
    print(f"{x['merk'][:10]:10s} {x['naam'][:52]:52s} {x['maat'][:6]:>6s} vrd {x['vrd']:4d} 12m {x['n12']:4d} "
          f"rest {x['restvraag']:6.1f} in {x['weken']:2d}wk -> over {x['projectie']:6.1f}  EUR {x['eur']:,}")
json.dump({'bij':bij[:200],'afp':afp[:200],'doorl':doorl[:200],
  'kpi':{'bij_n':len(bij),'bij_st':sum(x['bestel'] for x in bij),'bij_eur':sum(x['eur'] for x in bij),
         'afp_n':len(afp),'afp_eur':sum(x['eur'] for x in afp),
         'doorl_n':len(doorl),'doorl_eur':sum(x['eur'] for x in doorl),
         'uit_niet_live':sum(1 for x in rij if not x['live']),
         'uit_sale':sum(1 for x in rij if afgeprijsd(x)),
         'uit_stil':sum(1 for x in rij if not verse(x))},
  'seizoen':sz}, open(f'{B}/def_data.json','w'), ensure_ascii=False)
