import re, json, sys, glob
from tpl import HDR
SCHRAP=['ontdek','ervaar','til ','hoger niveau','stap in de wereld','ultiem','perfect','optimaal','naadloos','moeiteloos','tijdloos','essentieel','onmisbaar','toonbeeld','must-have',' dé ','niet alleen','of je nu','kortom','welkom bij','je kent het','handbagage','van een mens','klinkt gezellig','kussenfort','eerlijk','beste','allerbeste','uniek','revolutionair','pijn','klacht','ergonomisch',' rug','nek ','houding','gezond','medisch','joost','kuiphuis']
DASH=['—','–',' - ']
def texts():
    out=[]
    for f in glob.glob('theme/templates/*.json')+glob.glob('theme/sections/*group.json'):
        raw=open(f).read(); d=json.loads(raw[raw.index('{'):])
        def walk(o,path):
            if isinstance(o,dict):
                for k,v in o.items(): walk(v,path+'.'+k)
            elif isinstance(o,list):
                for i,v in enumerate(o): walk(v,path)
            elif isinstance(o,str) and not o.startswith(('shopify://','scheme-','#')) and ' ' in o and not re.match(r'^[a-z_\-]+$',o):
                out.append((f.split('/')[-1]+path,o))
        walk(d,'')
    for f in glob.glob('theme/sections/bline-*.liquid')+glob.glob('theme/snippets/bline-*.liquid'):
        s=re.sub(r'\{%-?\s*comment\s*-?%\}.*?\{%-?\s*endcomment\s*-?%\}','',open(f).read(),flags=re.S)
        s=re.sub(r'\{%\s*schema\s*%\}.*','',s,flags=re.S)
        for t in re.findall(r'>([^<>{}]*[A-Za-z][^<>{}]*)<',s): out.append((f.split('/')[-1],t))
        for t in re.findall(r"'([^']{12,})'",s): out.append((f.split('/')[-1],t))
    for f in ['sets.json']:
        for x in json.load(open(f)):
            for k in ['title','body','seo','desc']: out.append(('set '+x['handle']+' '+k,x[k]))
    for f in ['make_pages.py','make_cols.py']:
        for t in re.findall(r"'([^']{20,})'",open(f).read()): out.append((f,t))
    return out
hits=0
for w,t in texts():
    if any(c in t for c in ['{%','{{','$','=','(',';','|']): continue
    low=' '+re.sub('<[^>]+>',' ',t).lower()+' '
    for s in SCHRAP:
        if s in low: print('SCHRAP',repr(s),'|',w,'|',t[:100]); hits+=1
    for d in DASH:
        if d in t: print('STREEP',repr(d),'|',w,'|',t[:100]); hits+=1
    if re.search(r'\b(u|uw)\b',low): print('U/UW |',w,'|',t[:100]); hits+=1
    if '!' in re.sub('<[^>]+>','',t): print('UITROEP |',w,'|',t[:100]); hits+=1
print('treffers',hits)
