import json,os,glob,re,datetime as dt
from collections import defaultdict
B=os.path.dirname(os.path.abspath(__file__))
E=json.load(open(f'{B}/engine_data.json'))
ce=json.load(open(f'{B}/rows.json')); info={r['mpn']:r for r in ce}
tempo={x['mpn']:x for x in json.load(open(f'{B}/tempo.json'))}

def rij(x):
    return {'merk':x['merk'],'artikel':x['naam'],'maat':x['maat'],'vrd':x['vrd'],'n12':x['n12'],
            'tempo':x['schat'],'piek':x['piek'],'najaar':x['najaar'],'weken':x['weken'],
            'bestel':x.get('bestel'),'proj':x.get('projectie'),'restvraag':x.get('restvraag'),
            'eur':x.get('eur'),'prijs':x.get('shopprijs') or x.get('prijs'),
            'vanaf':x.get('vanaf'),'laatste':x.get('laatste'),'basis':x['niveau'],
            'ean':x['mpn'],'doorlopend':x.get('doorlopend'),
            'dagen_uit':x.get('dagen_uit'),'bron':x.get('tempo_bron'),
            'mom':x.get('mom'),'horizon':x.get('horizon'),
            'verwacht':x.get('verwacht_horizon')}
out={'kpi':E['kpi'],
     'bij':[rij(x) for x in E['bij'][:18]],
     'afp':[rij(x) for x in E['afp'][:18]],
     'doorl':[rij(x) for x in E['doorl'][:10]]}

# ---- najaarsvooruitzicht per merk: welke modellen dragen wk38-52 ----
alles={x['mpn']:x for x in E['bij']+E['afp']+E['doorl']}
mod=defaultdict(lambda: {'merk':None,'naam':None,'najaar':0,'piek':0,'jaar':0.0,'vrd':0,'skus':0})
for x in E['bij']+E['afp']+E['doorl']:
    r=info[x['mpn']]; p=r['parent'] or r['name']
    m=mod[p]
    m['merk']=x['merk']; m['najaar']=x['najaar']; m['piek']=x['piek']
    m['naam']=re.sub(r'\s+(Zwart|Black|Navy|Cognac).*$','',x['naam'])[:44]
    m['jaar']+=x['schat']*52; m['vrd']+=x['vrd']; m['skus']+=1
per=defaultdict(list)
for p,m in mod.items():
    if m['jaar']<10: continue
    m['najaarsvraag']=round(m['jaar']*m['najaar']/100)
    per[m['merk']].append(m)
uit={}
for merk,ms in per.items():
    ms.sort(key=lambda m:-m['najaarsvraag'])
    tot_n=sum(m['najaarsvraag'] for m in ms); tot_v=sum(m['vrd'] for m in ms)
    uit[merk]={'najaarsvraag':tot_n,'voorraad':tot_v,
      'modellen':[{'naam':m['naam'],'piek':m['piek'],'najaar':m['najaar'],
                   'vraag':m['najaarsvraag'],'vrd':m['vrd'],'skus':m['skus']} for m in ms[:6]]}
mom=json.load(open(f'{B}/momentum.json'))
for merk,v in uit.items():
    m=mom.get(merk) or {}
    v['mom']=m.get('factor') or mom['_groep']['factor']
    v['mom_ruw']=m.get('ruw'); v['mom_ly']=m.get('ly'); v['mom_nu']=m.get('nu')
out['momentum']=mom
out['vooruitzicht']=dict(sorted(uit.items(), key=lambda x:-x[1]['najaarsvraag'])[:8])
json.dump(out,open(f'{B}/dash3.json','w'),ensure_ascii=False)
d=json.load(open(f'{B}/dashboard_data.json'))
v=json.load(open(f'{B}/vooruit_dash.json'))
open(f'{B}/data_inline.js','w').write(
 "const DATA = "+json.dumps(d,ensure_ascii=False,separators=(',',':'))+";\n"
 "const VD = "+json.dumps(v,ensure_ascii=False,separators=(',',':'))+";\n"
 "const E = "+json.dumps(out,ensure_ascii=False,separators=(',',':'))+";")
print('kpi:',out['kpi'])
print('vooruitzicht merken:',list(out['vooruitzicht']))
for m,x in list(out['vooruitzicht'].items())[:3]:
    print(f"  {m}: najaarsvraag {x['najaarsvraag']} st, voorraad {x['voorraad']}")
    for mm in x['modellen'][:3]:
        print(f"     {mm['naam'][:40]:40s} piek wk{mm['piek']} najaar {mm['najaar']}% vraag {mm['vraag']} vrd {mm['vrd']}")
