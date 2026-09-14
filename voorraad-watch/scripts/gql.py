import os,subprocess,json,sys
from shops import SHOPS,API
tok={d:os.environ.get(e) for n,d,e in SHOPS}
def gql(dom,q,var=None):
    body=json.dumps({"query":q,"variables":var or {}})
    r=subprocess.run(["curl","-sS","-m","60","-X","POST",
      "-H",f"X-Shopify-Access-Token: {tok[dom]}","-H","Content-Type: application/json",
      "-d",body,f"https://{dom}.myshopify.com/admin/api/{API}/graphql.json"],
      capture_output=True,text=True)
    try: return json.loads(r.stdout)
    except Exception: return {"raw":r.stdout[:300]}
if __name__=="__main__":
    dom='sockwell-b2c-nl'
    print("=== 1. inventoryItem + level, met updatedAt ===")
    q='''{ productVariants(first:1, query:"sku:0845028010323"){ edges{ node{
        id sku title updatedAt inventoryQuantity
        inventoryItem{ id updatedAt createdAt tracked
          inventoryLevels(first:5){ edges{ node{ updatedAt
            quantities(names:["available","incoming","on_hand","committed"]){ name quantity } } } } } } } } }'''
    print(json.dumps(gql(dom,q),indent=1)[:1600])
