import os, requests, json
# META_SMAP_TOKEN: tijdelijke gebruikerstoken via de live app SMAP AUTO POST (advertenties aanmaken);
# anders de systeemgebruiker (lezen en beheren).
T=os.environ.get('META_SMAP_TOKEN') or os.environ['META_ACCESS_TOKEN']; A=os.environ['META_AD_ACCOUNT_ID']; A=A if A.startswith('act_') else 'act_'+A
PAGE=os.environ['META_PAGE_ID']; PIXEL=os.environ['META_PIXEL_ID']
V='https://graph.facebook.com/v23.0/'
def g(p, **q):
    q['access_token']=T; return requests.get(V+p, params=q, timeout=90).json()
def post(p, data=None, files=None):
    d=dict(data or {}); d['access_token']=T
    d={k:(json.dumps(v) if isinstance(v,(dict,list)) else v) for k,v in d.items()}
    return requests.post(V+p, data=d, files=files, timeout=180).json()
