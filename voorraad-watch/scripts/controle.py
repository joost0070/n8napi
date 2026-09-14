import json,glob,os
from collections import defaultdict
BASE=os.path.dirname(os.path.abspath(__file__))
ce=json.load(open(f'{BASE}/rows.json'))
info={r['mpn']:r for r in ce}
ean2mpn={r['ean']:r['mpn'] for r in ce if r.get('ean')}
sh={}
for f in glob.glob(f'{BASE}/shop/*_products.json'):
    dom=os.path.basename(f).replace('_products.json','')
    for v in json.load(open(f)):
        s=v.get('sku'); mpn = s if s in info else ean2mpn.get(s)
        if not mpn: continue
        sh.setdefault(mpn,[]).append({**v,'shop':dom})

vd=json.load(open(f'{BASE}/vooruit_data.json'))['sku']
def toon(titel, lijst):
    print("\n"+"="*104); print(titel); print("="*104)
    print(f"{'merk':10s} {'artikel':30s} {'mt':>5s} {'CE':>5s} {'shop':>5s} {'afw':>5s} {'prijs':>8s} {'vanaf':>8s} {'korting':>8s} {'shop':12s}")
    for x in lijst:
        vs=sh.get(x['mpn'])
        if not vs: 
            print(f"{x['merk'][:10]:10s} {str(x['artikel'])[:30]:30s} {str(x['maat']):>5s} {x['voorraad']:5d} {'—':>5s}   niet in webshop")
            continue
        v=max(vs,key=lambda a:(a.get('vrd') or 0))
        shopvrd=v.get('vrd') or 0
        vanaf=v.get('vanaf')
        kor=f"-{round(100*(1-v['prijs']/vanaf))}%" if vanaf and vanaf>v['prijs'] else "—"
        print(f"{x['merk'][:10]:10s} {str(x['artikel'])[:30]:30s} {str(x['maat']):>5s} {x['voorraad']:5d} {shopvrd:5d} "
              f"{shopvrd-x['voorraad']:5d} {v['prijs']:8.2f} {(f'{vanaf:.2f}' if vanaf else '—'):>8s} {kor:>8s} {v['shop'][:12]:12s}")

tek=sorted([x for x in vd if x['projectie']<-0.5 and not x['in_sale']],key=lambda x:-x['gemist_eur'])[:8]
ovr=sorted([x for x in vd if x['projectie']>0.5 and not x['in_sale']],key=lambda x:-x['risico_eur'])[:8]
toon("CONTROLE — signaal BIJBESTELLEN, naast de live webshopstand", tek)
toon("CONTROLE — signaal NU AFPRIJZEN, naast de live webshopstand", ovr)

# match-statistiek
gelijk=afw=ontbr=0
for x in vd:
    vs=sh.get(x['mpn'])
    if not vs: ontbr+=1; continue
    tot=max((a.get('vrd') or 0) for a in vs)
    if abs(tot-x['voorraad'])<=1: gelijk+=1
    else: afw+=1
print(f"\nvoorraadcontrole over {len(vd):,} SKU's: gelijk {gelijk:,} | wijkt af {afw:,} | niet in webshop {ontbr:,}")
