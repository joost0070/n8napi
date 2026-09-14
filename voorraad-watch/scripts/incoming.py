"""Scant of Shopify 'incoming' (verwachte levering) gevuld is - dan zijn inkooporders zichtbaar."""
import json,os,glob
from gql import gql
Q='''query($cur:String){ productVariants(first:100, after:$cur){
  pageInfo{ hasNextPage endCursor }
  edges{ node{ sku inventoryQuantity inventoryItem{ inventoryLevels(first:3){ edges{ node{
    quantities(names:["available","incoming","on_hand","committed"]){ name quantity } } } } } } } } }'''
for dom,maxp in (('sockwell-b2c-nl',12),('tofvel-nl',8),('heydude-nl',10)):
    cur=None; n=0; inc=0; incsum=0; comm=0; voorb=[]
    for _ in range(maxp):
        r=gql(dom,Q,{"cur":cur})
        d=((r.get('data') or {}).get('productVariants') or {})
        for e in d.get('edges',[]):
            nd=e['node']; n+=1
            for le in (nd['inventoryItem']['inventoryLevels']['edges'] or []):
                q={x['name']:x['quantity'] for x in le['node']['quantities']}
                if (q.get('incoming') or 0)>0: inc+=1; incsum+=q['incoming']; voorb.append((nd['sku'],q))
                if (q.get('committed') or 0)>0: comm+=1
        if not d.get('pageInfo',{}).get('hasNextPage'): break
        cur=d['pageInfo']['endCursor']
    print(f"{dom:18s} varianten bekeken {n:4d} | incoming>0: {inc:3d} (totaal {incsum} st) | committed>0: {comm:3d}")
    for s,q in voorb[:3]: print(f"    {s} -> {q}")
