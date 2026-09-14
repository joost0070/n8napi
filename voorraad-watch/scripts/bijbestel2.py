import json,os,re,datetime as dt
from collections import defaultdict
B=os.path.dirname(os.path.abspath(__file__))
TODAY=dt.date(2026,9,14)
tempo={x['mpn']:x for x in json.load(open(f'{B}/tempo.json'))}
ce=json.load(open(f'{B}/rows.json')); info={r['mpn']:r for r in ce}
vd={x['mpn']:x for x in json.load(open(f'{B}/vooruit_data.json'))['sku']}
LEVERTIJD=6      # weken, aanname tot de merk-config er is
K=8              # krimpgewicht: pas bij 8 verkochte stuks weegt de eigen meting vol

# ---- 1. tempo op MODELniveau (parent): daar is wel genoeg waarneming ----
model_stuks=defaultdict(int); model_dagen=defaultdict(int); model_sku=defaultdict(list)
for mpn,t in tempo.items():
    r=info.get(mpn)
    if not r: continue
    p=r['parent'] or r['name']
    model_stuks[p]+=t['stuks_jaar']
    model_dagen[p]=max(model_dagen[p], t['dagen_actief'])
    model_sku[p].append(mpn)
model_tempo={p: model_stuks[p]/max(model_dagen[p],7)*7 for p in model_stuks}

# ---- 2. maatverdeling binnen het model (val terug op het merk) ----
merk_maat=defaultdict(lambda: defaultdict(float))
for mpn,t in tempo.items():
    r=info.get(mpn)
    if r and r['size']: merk_maat[r['brand']][str(r['size'])]+=t['stuks_jaar']

def maataandeel(p, mpn):
    r=info[mpn]; maat=str(r['size'])
    eigen={m: tempo[m]['stuks_jaar'] for m in model_sku[p] if m in tempo}
    tot=sum(eigen.values())
    if tot>=25 and eigen.get(mpn) is not None:
        return eigen[mpn]/tot
    mm=merk_maat.get(r['brand'],{}); t2=sum(mm.values())
    return (mm.get(maat,0)/t2) if t2 else 1/max(len(model_sku[p]),1)

# ---- 3. gekrompen schatting per maat ----
rij=[]
for mpn,t in tempo.items():
    r=info.get(mpn)
    if not r: continue
    p=r['parent'] or r['name']
    prior = model_tempo[p]*maataandeel(p,mpn)          # verwacht tempo op basis van het model
    n = t['stuks_jaar']
    w = n/(n+K)                                        # hoeveel vertrouw ik de eigen meting
    schat = w*t['tempo_wk'] + (1-w)*prior
    if schat<=0.03: continue
    v=vd.get(mpn); weken_seizoen = v['weken_rest'] if v else 26
    vrd=t['vrd']
    weken_leeg = vrd/schat
    weken_zonder = max(0, weken_seizoen-weken_leeg)
    redbaar = max(0, weken_zonder-LEVERTIJD)*schat
    rij.append({'mpn':mpn,'merk':r['brand'],'naam':r['name'],'maat':r['size'],'vrd':vrd,
      'stuks_jaar':n,'ruw':t['tempo_wk'],'prior':round(prior,2),'schat':round(schat,2),
      'weken_leeg':round(weken_leeg,1),'weken_seizoen':weken_seizoen,
      'redbaar':round(redbaar,1),'redbaar_eur':round(redbaar*(r['price'] or 0)),
      'bestel':int(round(min(redbaar+max(0,min(weken_zonder,LEVERTIJD))*schat, schat*weken_seizoen))),
      'prijs':r['price'],'type':v['type'] if v else '?'})

# ---- 4. harde begrenzing: de maten samen mogen nooit sneller lopen dan het model zelf ----
per_model=defaultdict(list)
for x in rij: per_model[info[x['mpn']]['parent'] or info[x['mpn']]['name']].append(x)
for p,xs in per_model.items():
    som=sum(x['schat'] for x in xs); plafond=model_tempo.get(p,0)
    if som>plafond>0:
        f=plafond/som
        for x in xs:
            x['schat']=round(x['schat']*f,2)
            wl = x['vrd']/x['schat'] if x['schat']>0 else 999
            wz = max(0, x['weken_seizoen']-wl)
            x['weken_leeg']=round(wl,1)
            x['redbaar']=round(max(0,wz-LEVERTIJD)*x['schat'],1)
            x['redbaar_eur']=round(x['redbaar']*(x['prijs'] or 0))
            x['bestel']=int(round(min(x['redbaar']+max(0,min(wz,LEVERTIJD))*x['schat'], x['schat']*x['weken_seizoen'])))
rij=[x for x in rij if x['schat']>0.03]

rij.sort(key=lambda x:-x['redbaar_eur'])
top=[x for x in rij if x['redbaar']>=1]
print(f"SKU's die leegraken vóór het seizoenseinde: {len(top):,}  (was 8.053 zonder krimp)")
print(f"redbare omzet bij {LEVERTIJD} wk levertijd: EUR {sum(x['redbaar_eur'] for x in top):,}  (was EUR 11,8 mln)")
print(f"top-100 daarvan: EUR {sum(x['redbaar_eur'] for x in top[:100]):,}")
print(f"top-300 daarvan: EUR {sum(x['redbaar_eur'] for x in top[:300]):,}")
print("\n"+"="*112)
print("BIJBESTELLEN — gekrompen naar modelniveau")
print("="*112)
print(f"{'merk':10s} {'artikel':36s} {'mt':>6s} {'vrd':>4s} {'12m':>4s} {'ruw':>6s} {'model':>6s} {'schat':>6s} {'leeg over':>9s} {'bestel':>6s} {'redbaar':>9s}")
for x in top[:20]:
    leeg='NU LEEG' if x['vrd']==0 else f"{x['weken_leeg']:.0f} wk"
    print(f"{x['merk'][:10]:10s} {str(x['naam'])[:36]:36s} {str(x['maat']):>6s} {x['vrd']:4d} {x['stuks_jaar']:4d} "
          f"{x['ruw']:6.2f} {x['prior']:6.2f} {x['schat']:6.2f} {leeg:>9s} {x['bestel']:6d} {x['redbaar_eur']:9,}")
json.dump(top,open(f'{B}/bijbestel2.json','w'))

print("\n"+"="*112)
print("WAT DE KRIMP DOET — de Jan Jansen-regels die de vorige lijst opbliezen")
print("="*112)
jj=[x for x in rij if x['merk']=='Jan Jansen'][:6]
for x in jj:
    print(f"  {str(x['naam'])[:34]:34s} mt {str(x['maat']):>4s}  12mnd {x['stuks_jaar']:3d} st  "
          f"ruw {x['ruw']:5.2f}/wk -> gekrompen {x['schat']:5.2f}/wk  redbaar EUR {x['redbaar_eur']:,}")
