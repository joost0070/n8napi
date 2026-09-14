import json,glob,os
from collections import defaultdict
B=os.path.dirname(os.path.abspath(__file__))
vd=json.load(open(f'{B}/vooruit_data.json'))
kort=json.load(open(f'{B}/korting_data.json'))
sz=json.load(open(f'{B}/seizoen_data.json'))
ce=json.load(open(f'{B}/rows.json')); info={r['mpn']:r for r in ce}
ean2={r['ean']:r['mpn'] for r in ce if r.get('ean')}
sku=vd['sku']

# live shopprijzen
sh={}
for f in glob.glob(f'{B}/shop/*_products.json'):
    dom=os.path.basename(f).replace('_products.json','')
    for v in json.load(open(f)):
        s=v.get('sku'); m=s if s in info else ean2.get(s)
        if m and (v.get('vrd') or 0)>=(sh.get(m,{}).get('vrd') or -1):
            sh[m]={'prijs':v['prijs'],'vanaf':v.get('vanaf'),'vrd':v.get('vrd') or 0,'shop':dom}

def rij(x,soort):
    s=sh.get(x['mpn'],{})
    return {'merk':x['merk'],'artikel':str(x['artikel'])[:46],'maat':x['maat'],'type':x['type'],
            'vrd':x['voorraad'],'restvraag':round(x['restvraag'],1),'weken':x['weken_rest'],
            'delta':round(x['projectie'],1),'eur':x['gemist_eur'] if soort=='tekort' else x['risico_eur'],
            'prijs':s.get('prijs'),'vanaf':s.get('vanaf'),'shopvrd':s.get('vrd'),'shop':s.get('shop'),
            'jaarvraag':x['jaarvraag']}

bij=sorted([x for x in sku if x['projectie']<-0.5 and not x['in_sale'] and x['type']!='NOOS'],key=lambda x:-x['gemist_eur'])
afp=sorted([x for x in sku if x['projectie']>0.5 and not x['in_sale'] and x['type']!='NOOS' and x['restvraag']>0.2],key=lambda x:-x['risico_eur'])
nib=sorted([x for x in sku if x['projectie']<-0.5 and x['in_sale']],key=lambda x:-x['gemist_eur'])
noos=sorted([x for x in sku if x['type']=='NOOS' and x['projectie']>0.5],key=lambda x:-x['risico_eur'])

out={'kpi':{
  'skus':len(sku),
  'bij_n':len(bij),'bij_eur':sum(x['gemist_eur'] for x in bij),
  'afp_n':len(afp),'afp_eur':sum(x['risico_eur'] for x in afp),
  'nib_n':len(nib),'nib_eur':sum(x['gemist_eur'] for x in nib),
  'noos_n':len(noos),'noos_eur':sum(x['risico_eur'] for x in noos),
 },
 'bijbestellen':[rij(x,'tekort') for x in bij[:14]],
 'afprijzen':[rij(x,'over') for x in afp[:14]],
 'noos':[rij(x,'over') for x in noos[:12]],
 'nietbij':[rij(x,'tekort') for x in nib[:8]],
 'korting':kort,
 'vensters':sz['vensters'],
}
# seizoenscurves voor de merken die ertoe doen
belangrijk=['Tofvel|ONBEKEND','Tofvel|FW','Hunter|FW','Lazamani|SS','Lazamani|FW','HEYDUDE|SS','Keen|SS','Sockwell|ONBEKEND','Toni Pons|SS','Crocs|NOOS']
out['curves']={}
for k in belangrijk:
    c=sz['curves'].get(k)
    if not c: continue
    tot=sum(c.values()) or 1
    out['curves'][k]={'stuks':tot,'w':{str(w):round(100*c.get(str(w),0)/tot,2) for w in range(1,53)}}
json.dump(out,open(f'{B}/vooruit_dash.json','w'),ensure_ascii=False)
print('kpi:',json.dumps(out['kpi'],indent=1))
print('curves:',list(out['curves'].keys()))
print('korting merken:',list(kort.keys()))
