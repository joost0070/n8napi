import json,os,datetime as dt
from collections import defaultdict
B=os.path.dirname(os.path.abspath(__file__))
TODAY=dt.date(2026,9,14); NU=TODAY.isocalendar()[1]
tempo={x['mpn']:x for x in json.load(open(f'{B}/tempo.json'))}
ce=json.load(open(f'{B}/rows.json')); info={r['mpn']:r for r in ce}
vd={x['mpn']:x for x in json.load(open(f'{B}/vooruit_data.json'))['sku']}
LEVERTIJD_AANNAME=6   # weken; wordt de merk-config zodra die er is

rij=[]
for mpn,t in tempo.items():
    r=info.get(mpn)
    if not r: continue
    v=vd.get(mpn)
    weken_seizoen = v['weken_rest'] if v else 26
    vrd=t['vrd']; tw=t['tempo_wk']
    if tw<=0.05: continue
    weken_leeg = vrd/tw if tw>0 else 999
    # hoeveel weken sta je leeg voordat het seizoen afloopt?
    weken_zonder = max(0, min(weken_seizoen, weken_seizoen-weken_leeg))
    # bijbestellen kan pas na de levertijd; wat je vóór die tijd misloopt is verloren
    mis_totaal = weken_zonder*tw
    mis_onvermijdelijk = max(0, min(weken_zonder, LEVERTIJD_AANNAME))*tw
    redbaar = mis_totaal-mis_onvermijdelijk
    rij.append({**t,'weken_seizoen':weken_seizoen,'weken_leeg':round(weken_leeg,1),
      'mis':round(mis_totaal,1),'redbaar':round(redbaar,1),
      'redbaar_eur':round(redbaar*(r['price'] or 0)),
      'bestel':int(round(min(mis_totaal, tw*weken_seizoen))),
      'type':v['type'] if v else '?'})

rij.sort(key=lambda x:-x['redbaar_eur'])
top=[x for x in rij if x['redbaar']>0.5]
print(f"SKU's die leegraken vóór het seizoenseinde: {len(top):,}")
print(f"  waarvan nu al leeg: {sum(1 for x in top if x['vrd']==0):,}")
print(f"  omzet die nog te redden is bij {LEVERTIJD_AANNAME} wk levertijd: EUR {sum(x['redbaar_eur'] for x in top):,}")
print("\n"+"="*104)
print("BIJBESTELLEN op verkooptempo  (incl. artikelen die NU al leeg staan)")
print("="*104)
print(f"{'merk':10s} {'artikel':38s} {'mt':>6s} {'vrd':>4s} {'st/wk':>6s} {'leeg over':>9s} {'seiz.wk':>7s} {'bestel':>6s} {'redbaar EUR':>11s}")
for x in top[:22]:
    r=info[x['mpn']]
    leeg = 'NU LEEG' if x['vrd']==0 else f"{x['weken_leeg']:.0f} wk"
    print(f"{x['merk'][:10]:10s} {str(x['naam'])[:38]:38s} {str(x['maat']):>6s} {x['vrd']:4d} "
          f"{x['tempo_wk']:6.2f} {leeg:>9s} {x['weken_seizoen']:7d} {x['bestel']:6d} {x['redbaar_eur']:11,}")

# vergelijking met de oude lijst
oud=set(m for m,v in vd.items() if v['projectie']<-0.5 and not v['in_sale'] and v['type']!='NOOS')
nieuw=set(x['mpn'] for x in top[:400])
print(f"\nvergelijking met de vorige bijbestel-lijst:")
print(f"  stond in oude lijst: {len(oud):,} | staat in nieuwe top-400: {len(nieuw & oud):,} overlap")
print(f"  nieuw erbij (was uitgesloten omdat voorraad 0 was): {sum(1 for x in top[:400] if x['vrd']==0):,}")
json.dump(top,open(f'{B}/bijbestel.json','w'))
