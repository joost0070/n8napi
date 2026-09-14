import json,os,datetime as dt
from collections import defaultdict
BASE=os.path.dirname(os.path.abspath(__file__))
TODAY=dt.date(2026,9,14); NU=TODAY.isocalendar()[1]
HORIZON_NOOS=26
ce=json.load(open(f'{BASE}/rows.json'))
info={r['mpn']:r for r in ce}
sz=json.load(open(f'{BASE}/seizoen_data.json'))
kort=json.load(open(f'{BASE}/korting_data.json'))
vraagraw=json.load(open(f'{BASE}/vraag.json'))
vraag=defaultdict(int)
for k,q in vraagraw.items():
    mpn,y,w=k.rsplit('|',2); vraag[(mpn,int(y),int(w))]+=q

def stype(r):
    return 'NOOS' if str(r.get('season_year') or '').upper()=='NOOS' else r['season_code']

# ---------- seizoensindex per merk x type ----------
idx={}; dal={}
for sleutel,curve in sz['curves'].items():
    c={int(w):q for w,q in curve.items()}
    tot=sum(c.values())
    if tot<150: continue
    glad={w: sum(c.get(((w-1+d-1)%53)+1,0) for d in range(-1,2))/3 for w in range(1,54)}
    dal[sleutel]=min(glad,key=lambda w:glad[w])
    idx[sleutel]={w:c.get(w,0)/tot for w in range(1,54)}

def restaandeel(sleutel,w):
    """aandeel van de jaarvraag dat nog tussen nu en het seizoensdal valt"""
    if sleutel not in idx: return None,None
    d=dal[sleutel]; s=0.0; n=0
    k=w
    while k!=d and n<53:
        s+=idx[sleutel][k]; k=k%53+1; n+=1
    return s,n

def geleefd(sleutel,weken=26):
    """aandeel van de jaarvraag in de afgelopen N weken (voor run-rate schatting)"""
    if sleutel not in idx: return None
    s=0.0; k=NU
    for _ in range(weken):
        k=(k-2)%53+1; s+=idx[sleutel][k]
    return s

# ---------- per SKU vooruitkijken ----------
uit=[]
for r in ce:
    vrd=r['stock'] or 0
    if vrd<=0: continue
    t=stype(r); merk=r['brand']; sleutel=f"{merk}|{t}"
    # verkoop laatste 26 weken (alle kanalen)
    recent=0
    k=NU; y=TODAY.isocalendar()[0]
    for _ in range(26):
        recent+=vraag.get((r['mpn'],y,k),0)
        k-=1
        if k<1: k=52; y-=1
    aandeel_verstreken=geleefd(sleutel)
    if aandeel_verstreken is None or not aandeel_verstreken: continue
    jaarvraag = recent/aandeel_verstreken
    if t=='NOOS':
        # doorlopend artikel: geen seizoenseinde. Beoordeel tegen een vaste horizon
        # van 26 weken - dat is de voorraad die je redelijkerwijs wilt aanhouden.
        weken_rest=HORIZON_NOOS
        rest=HORIZON_NOOS/52
        restvraag=jaarvraag*rest
    else:
        rest,weken_rest=restaandeel(sleutel,NU)
        if rest is None: continue
        restvraag = jaarvraag*rest
    proj = vrd - restvraag
    inkoop = r['purchase'] or (r['price'] or 0)*0.45
    kg = kort.get(merk,{})
    nu_sale = kg.get('nu'); basis=kg.get('basis'); live=kg.get('live_pct')
    in_sale = (nu_sale is not None and basis is not None and nu_sale >= max(30, basis+20)) or (live is not None and live>=45)
    uit.append({'mpn':r['mpn'],'merk':merk,'artikel':r['name'],'maat':r['size'],'type':t,
      'voorraad':vrd,'recent26':recent,'jaarvraag':round(jaarvraag,1),
      'restvraag':round(restvraag,1),'weken_rest':weken_rest,
      'projectie':round(proj,1),'inkoop':round(inkoop,2),'prijs':r['price'],
      'waarde':round(vrd*inkoop),'in_sale':in_sale,
      'risico_eur':round(max(proj,0)*inkoop),'gemist_eur':round(max(-proj,0)*(r['price'] or 0))})

print(f"SKU's met voorraad beoordeeld: {len(uit):,}")
tek=[x for x in uit if x['projectie']<-0.5]
ovr=[x for x in uit if x['projectie']>0.5 and x['restvraag']>0.2]
print(f"  tekort voor seizoenseinde : {len(tek):,} SKU's | gemiste omzet EUR {sum(x['gemist_eur'] for x in tek):,}")
print(f"  overschot bij seizoenseinde: {len(ovr):,} SKU's | vastgelegd EUR {sum(x['risico_eur'] for x in ovr):,}")

print("\n"+"="*100)
print("BIJBESTELLEN — tekort verwacht, merk staat NIET in de sale")
print("="*100)
print(f"{'merk':12s} {'artikel':34s} {'mt':>5s} {'vrd':>4s} {'restvraag':>9s} {'tekort':>7s} {'wk':>3s} {'gemist EUR':>10s}")
kandidaat=sorted([x for x in tek if not x['in_sale']], key=lambda x:-x['gemist_eur'])
for x in kandidaat[:16]:
    print(f"{x['merk'][:12]:12s} {str(x['artikel'])[:34]:34s} {str(x['maat'] or '-'):>5s} {x['voorraad']:4d} "
          f"{x['restvraag']:9.1f} {-x['projectie']:7.1f} {x['weken_rest']:3d} {x['gemist_eur']:10,}")

print("\n"+"="*100)
print("NU AFPRIJZEN — overschot verwacht en het merk verkoopt NOG op volle prijs")
print("="*100)
print(f"{'merk':12s} {'artikel':34s} {'mt':>5s} {'vrd':>4s} {'restvraag':>9s} {'over':>6s} {'wk':>3s} {'risico EUR':>10s}")
vroeg=sorted([x for x in ovr if not x['in_sale']], key=lambda x:-x['risico_eur'])
for x in vroeg[:16]:
    print(f"{x['merk'][:12]:12s} {str(x['artikel'])[:34]:34s} {str(x['maat'] or '-'):>5s} {x['voorraad']:4d} "
          f"{x['restvraag']:9.1f} {x['projectie']:6.1f} {x['weken_rest']:3d} {x['risico_eur']:10,}")

print("\n"+"="*100)
print("DOORLOPENDE ARTIKELEN (NOOS) — beoordeeld tegen 26 weken, niet tegen een seizoenseinde")
print("="*100)
noos=[x for x in uit if x['type']=='NOOS']
nover=sorted([x for x in noos if x['projectie']>0.5],key=lambda x:-x['risico_eur'])
ntek=sorted([x for x in noos if x['projectie']<-0.5],key=lambda x:-x['gemist_eur'])
print(f"  {len(noos):,} SKU's | te ruim: {len(nover):,} (EUR {sum(x['risico_eur'] for x in nover):,}) | te krap: {len(ntek):,}")
print(f"{'merk':10s} {'artikel':32s} {'mt':>6s} {'vrd':>5s} {'jaarvraag':>9s} {'jaren vrd':>9s} {'risico EUR':>10s}")
for x in nover[:10]:
    jr = x['voorraad']/x['jaarvraag'] if x['jaarvraag']>0 else 999
    print(f"{x['merk'][:10]:10s} {str(x['artikel'])[:32]:32s} {str(x['maat']):>6s} {x['voorraad']:5d} "
          f"{x['jaarvraag']:9.1f} {('>99' if jr>99 else f'{jr:.1f}'):>9s} {x['risico_eur']:10,}")

print("\n"+"="*100)
print("NIET BIJBESTELLEN — tekort, maar het merk zit al in de sale")
print("="*100)
insale=sorted([x for x in tek if x['in_sale']], key=lambda x:-x['gemist_eur'])
print(f"  {len(insale):,} SKU's, samen EUR {sum(x['gemist_eur'] for x in insale):,} theoretisch gemiste omzet")
for x in insale[:6]:
    print(f"  {x['merk'][:12]:12s} {str(x['artikel'])[:38]:38s} mt {str(x['maat']):>5s} tekort {-x['projectie']:.1f}")

samenv=defaultdict(lambda: defaultdict(float))
for x in uit:
    s=samenv[x['merk']]
    s['skus']+=1; s['waarde']+=x['waarde']
    if x['projectie']<-0.5: s['tekort']+=1; s['gemist']+=x['gemist_eur']
    elif x['projectie']>0.5 and x['restvraag']>0.2: s['over']+=1; s['risico']+=x['risico_eur']
json.dump({'sku':uit,'merk':{k:dict(v) for k,v in samenv.items()},
           'idx':{k:{str(w):round(v,5) for w,v in c.items()} for k,c in idx.items()},
           'dal':dal},
          open(f'{BASE}/vooruit_data.json','w'))
print("\n-> vooruit_data.json geschreven")
