import os,requests,json,sys,time
REV=os.environ.get('KREV','2026-07-15')
def k(acc,method,path,body=None,params=None,rev=None):
    key=os.environ[acc]
    url=path if path.startswith('http') else 'https://a.klaviyo.com/api/'+path.lstrip('/')
    for poging in range(5):
        r=requests.request(method,url,headers={'Authorization':'Klaviyo-API-Key '+key,'revision':rev or REV,'accept':'application/vnd.api+json','content-type':'application/vnd.api+json'},json=body,params=params,timeout=60)
        if r.status_code==429: time.sleep(int(r.headers.get('Retry-After','3'))+1); continue
        break
    try: j=r.json()
    except Exception: j={'raw':r.text[:500]}
    return r.status_code,j
def alles(acc,path,params=None,rev=None):
    out=[]; sc,j=k(acc,'GET',path,params=params,rev=rev)
    while True:
        if sc!=200: return sc,j
        out+=j.get('data',[])
        nxt=(j.get('links') or {}).get('next')
        if not nxt: return 200,out
        sc,j=k(acc,'GET',nxt,rev=rev)
