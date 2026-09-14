import json, os, re, datetime as dt
from collections import defaultdict
BASE=os.path.dirname(os.path.abspath(__file__))
rows=json.load(open(f'{BASE}/rows.json'))
weekly=json.load(open(f'{BASE}/weekly.json'))
def sortkey(x):
    try: return (0,float(x))
    except: return (1,99.0)
def norm(s):
    if not s: return None
    s=str(s).strip().replace(',','.')
    m=re.match(r'^(\d{2}(?:\.5)?)',s)
    return m.group(1) if m else s[:8]
for r in rows: r['nsize']=norm(r['size'])
ws=[r for r in rows if r['stock']>0]
out={}
out['kpi']={
 'skus_totaal':len(rows),'skus_voorraad':len(ws),
 'stuks':sum(r['stock'] for r in ws),
 'waarde':round(sum(r['value'] for r in ws)),
 'dead_waarde':round(sum(r['value'] for r in ws if r['s52']==0)),
 'dead_skus':sum(1 for r in ws if r['s52']==0),
 'oos_met_vraag':sum(1 for r in rows if r['stock']==0 and r['s13']>0),
 'ce_stuks_52w':sum(r['s52'] for r in rows),
 'retour_52w':sum(r['ret'] for r in rows),
}
# merken
bm=defaultdict(lambda: defaultdict(float))
for r in ws:
    b=bm[r['brand']]
    b['skus']+=1;b['stock']+=r['stock'];b['value']+=r['value']
    b['s52']+=r['s52'];b['s13']+=r['s13'];b['ret']+=r['ret']
    b[r['season_code']]+=r['value']
    if r['s52']==0: b['dead']+=r['value']
out['merken']=[]
for b,v in sorted(bm.items(),key=lambda x:-x[1]['value']):
    if v['value']<500: continue
    wk=v['s13']/13
    out['merken'].append({'merk':b,'skus':int(v['skus']),'stuks':int(v['stock']),
     'waarde':round(v['value']),'s52':int(v['s52']),'s13':int(v['s13']),
     'woc':round(v['stock']/wk) if wk else None,'dead':round(v['dead']),
     'FW':round(v['FW']),'SS':round(v['SS']),'ONB':round(v['ONBEKEND']),
     'retour_pct':round(100*v['ret']/v['s52']) if v['s52'] else None})
# maatcurve
out['curves']={}
for brand in ['Keen','Crocs','Hunter','Tofvel','Lazamani','Toni Pons','HEYDUDE','Sockwell']:
    br=[r for r in rows if r['brand']==brand and r['nsize']]
    sold=defaultdict(int);stock=defaultdict(int)
    for r in br: sold[r['nsize']]+=r['s52'];stock[r['nsize']]+=r['stock']
    ts,tk=sum(sold.values()),sum(stock.values())
    if ts<50 or tk<100: continue
    items=[(s,100*sold[s]/ts,100*stock[s]/tk) for s in sorted(set(sold)|set(stock),key=sortkey)
           if (sold[s] or stock[s]) and (100*sold[s]/ts>0.8 or 100*stock[s]/tk>0.8)]
    out['curves'][brand]={'verkoop':ts,'voorraad':tk,
      'data':[{'maat':s,'verk':round(v,1),'vrd':round(k,1),'delta':round(k-v,1)} for s,v,k in items]}
# gebroken reeksen
bymodel=defaultdict(list)
for r in rows: bymodel[(r['brand'],r['parent'] or r['name'])].append(r)
broken=[]
for (brand,parent),vs in bymodel.items():
    s13=sum(v['s13'] for v in vs)
    if s13<4: continue
    sizes=[v for v in vs if v['nsize']]
    if len(sizes)<4: continue
    oos=[v for v in sizes if v['stock']==0 and v['s52']>0]
    if not oos: continue
    broken.append({'merk':brand,'model':str(vs[0]['name'])[:46],'s13':s13,
      'oos':len(oos),'tot':len(sizes),'vrd':sum(v['stock'] for v in sizes),
      'mis4wk':round(sum(v['s52'] for v in oos)/52*4,1),
      'maten':sorted({v['nsize'] for v in oos},key=sortkey)[:10],
      'prijs':vs[0]['price']})
broken.sort(key=lambda x:-x['mis4wk'])
out['broken']=broken[:18]
# overstock
over=[]
for r in ws:
    if r['value']<800: continue
    wk=r['s52']/52
    woc=r['stock']/wk if wk>0 else 999
    if woc>=52: over.append({'merk':r['brand'],'artikel':str(r['name'])[:44],'maat':r['nsize'],
      'seizoen':r['season_code'],'jaar':r['season_year'],'vrd':r['stock'],'s52':r['s52'],
      'waarde':round(r['value']),'woc':None if woc>=999 else round(woc)})
over.sort(key=lambda x:-x['waarde'])
out['overstock']=over[:18]
# seizoenscurve marketplace-vraag per week
out['weekly']=weekly
json.dump(out,open(f'{BASE}/dashboard_data.json','w'),ensure_ascii=False)
print('export ok:', {k:(len(v) if isinstance(v,(list,dict)) else v) for k,v in out.items() if k!='kpi'})
print(json.dumps(out['kpi'],indent=1))
