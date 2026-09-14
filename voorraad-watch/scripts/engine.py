"""Voorraad Watch - curve op modelniveau, niet op merkniveau."""
import json,glob,os,re,datetime as dt
from collections import defaultdict
B=os.path.dirname(os.path.abspath(__file__))
TODAY=dt.date(2026,9,14); NU=TODAY.isocalendar()[1]
LEVERTIJD=6; K=8; MIN_CURVE=150
C1=(dt.date(2024,9,2),dt.date(2025,8,31)); C2=(dt.date(2025,9,1),dt.date(2026,8,30))
ce=json.load(open(f'{B}/rows.json')); info={r['mpn']:r for r in ce}
ean2={r['ean']:r['mpn'] for r in ce if r.get('ean')}
# Verkooptempo op gemeten leverbaarheid waar die er is (tempo_ql.json),
# anders de oude benadering op eerste-tot-laatste-verkoopdatum.
import os.path as _p
_tf = f'{B}/tempo_ql.json' if _p.exists(f'{B}/tempo_ql.json') else f'{B}/tempo.json'
tempo={x['mpn']:x for x in json.load(open(_tf))}
# Momentum per merk: laatste 13 weken tegen dezelfde weken vorig jaar, begrensd
# op 0,70-1,50. Het tempo meet de afgelopen 12 maanden en bevat de groei die al
# gebeurd is; deze factor projecteert de beweging vooruit.
MOM=json.load(open(f'{B}/momentum.json'))
def momentum(merk):
    v=MOM.get(merk) or MOM['_groep']
    return v.get('factor') or MOM['_groep']['factor']
def stype(r): return 'NOOS' if str(r.get('season_year') or '').upper()=='NOOS' else r['season_code']
def fix(s):
    s=str(s or '')
    try: return s.encode('latin-1').decode('utf-8')
    except Exception: return s
def familie(r):
    w=re.sub(r'\s+',' ',str(r['name'] or '')).split()
    return f"{r['brand']}|{' '.join(w[:2]).lower()}" if w else f"{r['brand']}|?"

# ---- vraag per niveau, per cyclus ----
niveaus=('parent','familie','merktype')
c=defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(int))))  # niveau->sleutel->cyclus->week
def tel(mpn,d,q):
    r=info.get(mpn)
    if not r or q<=0: return
    cyc = 'c1' if C1[0]<=d<=C1[1] else 'c2' if C2[0]<=d<=C2[1] else None
    if not cyc: return
    w=d.isocalendar()[1]
    c['parent'][r['parent'] or r['name']][cyc][w]+=q
    c['familie'][familie(r)][cyc][w]+=q
    c['merktype'][f"{r['brand']}|{stype(r)}"][cyc][w]+=q
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

def maakidx(cycli):
    delen=[]; tot_all=0
    for naam in ('c1','c2'):
        cc=cycli.get(naam,{}); t=sum(cc.values()); tot_all+=t
        if t>=60: delen.append({w: cc.get(w,0)/t for w in range(1,54)})
    if not delen or tot_all<MIN_CURVE: return None
    i={w: sum(d[w] for d in delen)/len(delen) for w in range(1,54)}
    glad={w: sum(i[((w-1+k+53)%53)+1] for k in (-1,0,1))/3 for w in range(1,54)}
    dal=min(glad,key=lambda w:glad[w])
    vec=[i[w] for w in range(1,53)]
    top13=max(sum(vec[(s+k)%52] for k in range(13)) for s in range(52))
    rest=0.0; w=NU; n=0
    while w!=dal and n<53: rest+=i[w]; w=w%53+1; n+=1
    return {'idx':i,'dal':dal,'top13':top13,'rest':rest,'weken':n,'stuks':tot_all,
            'piek':max(i,key=lambda x:i[x]),'najaar':sum(i[w] for w in range(38,53))}
IDX={niv:{k:maakidx(v) for k,v in c[niv].items()} for niv in niveaus}
for niv in niveaus: IDX[niv]={k:v for k,v in IDX[niv].items() if v}
print(f"curves: parent {len(IDX['parent']):,} | familie {len(IDX['familie']):,} | merk×type {len(IDX['merktype']):,}")

def aandeel_komende(cv, n):
    """Aandeel van de jaarvraag in de eerstvolgende n weken - seizoensgewogen."""
    i=cv['idx']; s=0.0; w=NU
    for _ in range(int(n)): s+=i[w]; w=w%53+1
    return s

def curve_voor(r):
    for niv,sleutel in (('parent',r['parent'] or r['name']),('familie',familie(r)),
                        ('merktype',f"{r['brand']}|{stype(r)}")):
        v=IDX[niv].get(sleutel)
        if v: return niv,v
    return None,None

# ---- tempo met krimp + plafond ----
mstuks=defaultdict(int); mdagen=defaultdict(int); msku=defaultdict(list)
for m,t in tempo.items():
    r=info.get(m)
    if not r: continue
    p=r['parent'] or r['name']
    # Zelfde noemer als de maten zelf: gemeten leverbaarheid waar die er is.
    dg = t.get('dagen_lever') or t['dagen_actief']
    mstuks[p]+=t['stuks_jaar']; mdagen[p]=max(mdagen[p],dg); msku[p].append(m)
mtempo={p: mstuks[p]/max(mdagen[p],7)*7 for p in mstuks}
merkmaat=defaultdict(lambda: defaultdict(float))
for m,t in tempo.items():
    r=info.get(m)
    if r and r['size']: merkmaat[r['brand']][str(r['size'])]+=t['stuks_jaar']
def aandeel(p,m):
    eigen={x:tempo[x]['stuks_jaar'] for x in msku[p] if x in tempo}; tot=sum(eigen.values())
    if tot>=25: return eigen.get(m,0)/tot
    mm=merkmaat.get(info[m]['brand'],{}); t2=sum(mm.values())
    return (mm.get(str(info[m]['size']),0)/t2) if t2 else 1/max(len(msku[p]),1)

# ---- live webshop ----
# De fysieke voorraad is het hoogste van ChannelEngine en de webshops: 210 SKU's
# lopen uiteen, en een besteladvies op een te lage stand kost dubbel geld.
shopvrd={}
live={}
for f in glob.glob(f'{B}/shop/*_products.json'):
    for v in json.load(open(f)):
        s=v.get('sku'); m=s if s in info else ean2.get(s)
        if not m: continue
        cur=live.setdefault(m,{'pub':False,'prijs':None,'vanaf':None,'vrd':-1})
        if v.get('gepubliceerd'): cur['pub']=True
        if (v.get('vrd') or 0)>=cur['vrd']:
            cur.update({'prijs':v['prijs'],'vanaf':v.get('vanaf'),'vrd':v.get('vrd') or 0})
        shopvrd[m]=max(shopvrd.get(m,-10**9), v.get('vrd') or 0)
laatste={}
for f in glob.glob(f'{B}/shop/*_orders.json'):
    for r in json.load(open(f)):
        s=r.get('sku'); m=s if s in info else ean2.get(s)
        if m:
            d=dt.date.fromisoformat(r['d'])
            if m not in laatste or d>laatste[m]: laatste[m]=d

# ---- prijsregime per COLLECTIE, niet per merk ----
# Een merk heeft zelden een prijsregime: de zomercollectie wordt opgeruimd terwijl
# de nieuwe wintercollectie op volle prijs staat. De eenheid is merk x seizoen x
# seizoensjaar. Elke FW2026-collectie staat op 0% afprijzing; Lazamani FW2024 op 97%.
col=defaultdict(lambda:[0,0]); merkcol=defaultdict(lambda:[0,0])
for m,lv in live.items():
    r=info.get(m)
    if not r or lv.get('prijs') is None: continue
    sale = bool(lv.get('vanaf') and lv['vanaf']>lv['prijs']*1.02)
    k=(r['brand'], r['season_code'], str(r['season_year'] or '?'))
    col[k][1]+=1; merkcol[r['brand']][1]+=1
    if sale: col[k][0]+=1; merkcol[r['brand']][0]+=1
DREMPEL=0.45; MINV=40
def collectie(r):
    return (r['brand'], r['season_code'], str(r['season_year'] or '?'))
def col_pct(r):
    a,b=col.get(collectie(r),[0,0])
    if b>=MINV: return a/b, 'collectie'
    a,b=merkcol.get(r['brand'],[0,0])
    if b>=MINV: return a/b, 'merk'
    return None, None
def col_in_sale(r):
    p,_=col_pct(r)
    return p is not None and p>=DREMPEL


rij=[]
for m,t in tempo.items():
    r=info.get(m)
    if not r: continue
    niv,cv=curve_voor(r)
    if not cv: continue
    # Doorlopend of seizoensgebonden bepaalt de gemeten curve, niet het label in
    # ChannelEngine. Wally Braided staat daar als NOOS, maar doet 74% van zijn jaar
    # in 13 weken en 2% in wk38-52 - dat is geen doorlopend artikel.
    doorlopend = cv['top13']<0.33
    rest,weken = (0.5,26) if doorlopend else (cv['rest'],cv['weken'])
    p=r['parent'] or r['name']
    n=t['stuks_jaar']; w=n/(n+K)
    schat=w*t['tempo_wk']+(1-w)*mtempo[p]*aandeel(p,m)
    lv=live.get(m,{})
    rij.append({'mpn':m,'merk':r['brand'],'naam':fix(r['name']),'maat':fix(r['size']),
      'vrd':max(r['stock'] or 0, shopvrd.get(m,-10**9)),'ce_vrd':r['stock'] or 0,
      'shop_vrd':shopvrd.get(m),'n12':n,'schat':schat,'rest':rest,'weken':weken,'niveau':niv,
      'piek':cv['piek'],'top13':round(100*cv['top13']),'najaar':round(100*cv['najaar']),
      '_cv':cv,'col':'|'.join(collectie(r)),
      'col_pct':(lambda p: round(100*p) if p is not None else None)(col_pct(r)[0]),
      'col_bron':col_pct(r)[1],'col_sale':col_in_sale(r),
      'doorlopend':doorlopend,'mom':momentum(r['Brand'] if 'Brand' in r else r['brand']),
      'prijs':r['price'],'inkoop':r['purchase'] or (r['price'] or 0)*0.45,
      'dagen_uit':t.get('dagen_uit'),'tempo_bron':t.get('bron','benadering'),
      'live':lv.get('pub',False),'shopprijs':lv.get('prijs'),'vanaf':lv.get('vanaf'),
      'laatste':str(laatste[m]) if m in laatste else None,'parent':p})
per=defaultdict(list)
for x in rij: per[x['parent']].append(x)
for p,xs in per.items():
    som=sum(x['schat'] for x in xs); plaf=mtempo.get(p,0)
    if som>plaf>0:
        f=plaf/som
        for x in xs: x['schat']*=f
for x in rij:
    x['schat']=round(x['schat'],2)
    # Seizoensgewogen: het tempo is een jaargemiddelde, dus vermenigvuldigen met
    # het aantal resterende weken telt piek- en dalweken even zwaar. Het aandeel
    # van de jaarvraag dat nog komt is de juiste maat. Daarna het momentum erop.
    x['restvraag']=round(x['schat']*52*x['rest']*x['mom'],1)
    x['vlak_restvraag']=round(x['schat']*x['weken'],1)
    x['projectie']=round(x['vrd']-x['restvraag'],1)
    x['weken_leeg']=round(x['vrd']/x['schat'],1) if x['schat']>0 else None

afgeprijsd=lambda x: bool(x['vanaf'] and x['shopprijs'] and x['vanaf']>x['shopprijs']*1.02)
genoeg=lambda x: x['n12']>=10 or mstuks[x['parent']]>=30
vers=lambda x: x['laatste'] and (TODAY-dt.date.fromisoformat(x['laatste'])).days<=120
MIN_NAJAAR=12   # minstens 12% van de jaarvraag moet nog in wk38-52 vallen

DEKKING=8   # weken voorraad die je wilt hebben bovenop de levertijd
# Niet bijbestellen in een collectie die wordt opgeruimd, ook al is dit ene
# artikel nog niet afgeprijsd: je koopt dan in om straks met korting te verkopen.
bij=[x for x in rij if x['projectie']<-0.5 and genoeg(x) and x['live'] and not afgeprijsd(x)
     and not x['col_sale'] and vers(x) and x['schat']>0.1 and x['najaar']>=MIN_NAJAAR]
for x in bij:
    # Bestel wat je nodig hebt tot de volgende levering kan landen: levertijd plus
    # een dekkingsperiode, seizoensgewogen en met het momentum erop. Niet het hele
    # seizoen in een keer - daar kun je tussendoor op bijsturen.
    cv=x['_cv']
    horizon=min(LEVERTIJD+DEKKING, x['weken'])
    verwacht = x['schat']*52*aandeel_komende(cv, horizon)*x['mom']
    x['horizon']=horizon
    x['verwacht_horizon']=round(verwacht,1)
    x['bestel']=int(round(max(0, verwacht - x['vrd'])))
    wz=max(0,x['weken']-(x['weken_leeg'] or 0))
    x['redbaar']=round(max(0,min(wz,x['weken'])-LEVERTIJD)*x['schat']*x['mom'],1)
    x['eur']=round(x['redbaar']*(x['prijs'] or 0))
bij=[x for x in bij if x['bestel']>=3]; bij.sort(key=lambda x:-x['eur'])

afp=[x for x in rij if not x['doorlopend'] and x['projectie']>0.5 and x['restvraag']>0.2
     and not afgeprijsd(x) and not x['col_sale'] and x['vrd']>0 and genoeg(x)]
verdiep=[x for x in rij if x['projectie']>0.5 and x['col_sale'] and not afgeprijsd(x)
         and x['vrd']>0 and genoeg(x)]
for x in verdiep: x['eur']=round(x['projectie']*x['inkoop'])
verdiep.sort(key=lambda x:-x['eur'])
for x in afp: x['eur']=round(x['projectie']*x['inkoop'])
afp.sort(key=lambda x:-x['eur'])
doorl=[x for x in rij if x['doorlopend'] and x['projectie']>0.5 and x['vrd']>0 and genoeg(x)]
for x in doorl: x['eur']=round(x['projectie']*x['inkoop'])
doorl.sort(key=lambda x:-x['eur'])

geweerd=[x for x in rij if x['projectie']<-0.5 and genoeg(x) and x['live'] and not afgeprijsd(x)
         and vers(x) and x['najaar']<MIN_NAJAAR]
print(f"\nBIJBESTELLEN : {len(bij):,} maten | {sum(x['bestel'] for x in bij):,} paar | EUR {sum(x['eur'] for x in bij):,}")
print(f"  geweerd omdat het seizoen voorbij is (<{MIN_NAJAAR}% vraag in wk38-52): {len(geweerd):,} maten")
print(f"NU AFPRIJZEN : {len(afp):,} | EUR {sum(x['eur'] for x in afp):,}   (collectie nog op volle prijs)")
print(f"KORTING VERDIEPEN : {len(verdiep):,} | EUR {sum(x['eur'] for x in verdiep):,}   (collectie loopt al in de sale)")
geblokt=[x for x in rij if x['projectie']<-0.5 and genoeg(x) and x['live'] and not afgeprijsd(x)
         and vers(x) and x['najaar']>=MIN_NAJAAR and x['col_sale']]
print(f"  niet besteld omdat de COLLECTIE in de sale loopt: {len(geblokt):,} maten")
print(f"DOORLOPEND TE RUIM: {len(doorl):,} | EUR {sum(x['eur'] for x in doorl):,}")
print("\nTOP BIJBESTELLEN — met de curve waarop het gebaseerd is")
print(f"{'merk':9s} {'artikel + kleur':50s} {'mt':>6s} {'vrd':>4s} {'12m':>4s} {'/wk':>5s} {'piek':>5s} {'najaar':>7s} {'bestel':>6s} {'basis':>9s}")
for x in bij[:18]:
    print(f"{x['merk'][:9]:9s} {x['naam'][:50]:50s} {x['maat'][:6]:>6s} {x['vrd']:4d} {x['n12']:4d} {x['schat']:5.2f} "
          f"{('wk'+str(x['piek'])):>5s} {str(x['najaar'])+'%':>7s} {x['bestel']:6d} {x['niveau']:>9s}")
print("\nHEYDUDE in de bijbestellijst:")
hd=[x for x in bij if x['merk']=='HEYDUDE']
print(f"  {len(hd)} maten: " + ', '.join(sorted({x['naam'].split(' Heren')[0].split(' Dames')[0] for x in hd})[:8]))
print("\nHEYDUDE geweerd (zomermodellen):")
hg=[x for x in geweerd if x['merk']=='HEYDUDE']
print(f"  {len(hg)} maten: " + ', '.join(sorted({x['naam'].split(' Heren')[0].split(' Dames')[0] for x in hg})[:8]))
for x in rij: x.pop('_cv',None)
json.dump({'bij':bij[:200],'afp':afp[:200],'doorl':doorl[:120],'verdiep':verdiep[:60],
  'collecties':[{'merk':k[0],'seizoen':k[1],'jaar':k[2],'sale':a,'totaal':b,'pct':round(100*a/b)}
                for k,(a,b) in sorted(col.items(), key=lambda x:(x[0][0],x[0][2])) if b>=MINV],
  'kpi':{'bij_n':len(bij),'bij_st':sum(x['bestel'] for x in bij),'bij_eur':sum(x['eur'] for x in bij),
         'afp_n':len(afp),'afp_eur':sum(x['eur'] for x in afp),
         'doorl_n':len(doorl),'doorl_eur':sum(x['eur'] for x in doorl),
         'geweerd':len(geweerd),'uit_niet_live':sum(1 for x in rij if not x['live']),
         'verdiep_n':len(verdiep),'verdiep_eur':sum(x['eur'] for x in verdiep),
         'col_geblokt':len(geblokt),
         'uit_sale':sum(1 for x in rij if afgeprijsd(x)),'uit_stil':sum(1 for x in rij if not vers(x))}},
  open(f'{B}/engine_data.json','w'), ensure_ascii=False)
