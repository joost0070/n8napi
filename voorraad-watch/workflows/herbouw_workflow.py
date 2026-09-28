"""Herbouwt de bedrading van voorraad-watch-wekelijks.json.

Wat er mis was in de eerdere versie:
  - De analyse-node had zeven inkomende verbindingen. In n8n draait een node dan
    per binnenkomende tak, dus zeven keer, deels voordat de andere bronnen klaar
    zijn. Nu wacht een Merge-node (append, meerdere ingangen) tot alles binnen is.
  - De Shopify-nodes geven per pagina {orders:[...]} en {products:[...]}; de
    analyse las ze alsof elk item een order was. Nu worden ze eerst uitgepakt.
  - De snapshot schreef alle ~60.000 maten per run naar Google Sheets. Nu alleen
    de maten met een signaal, en alleen op maandag.

Wat er bij komt:
  - Een dagelijkse trigger (07:30) naast de wekelijkse.
  - ShopifyQL per shop: voorraad, verkoop en dagen uit voorraad (28 en 365 dagen).
  - De uitverkoopradar en een rapport dat op maandag altijd, en op andere dagen
    alleen bij een acuut signaal verstuurd wordt.

Draaien:  python3 herbouw_workflow.py   (in deze map)
"""
import json, os

HIER = os.path.dirname(os.path.abspath(__file__))
PAD = os.path.join(HIER, 'voorraad-watch-wekelijks.json')
w = json.load(open(PAD))
nodes = {n['name']: n for n in w['nodes']}

def js(naam): return open(os.path.join(HIER, naam)).read()

# ---- 1. Shopify-pagina's uitpakken in de analyse ----
a = nodes['Analyse: signaal per maat']
code = a['parameters']['jsCode']
code = code.replace(
    "const shopOrd   = $('Shopify: orders').all().map(i => i.json);",
    "// De Shopify-node geeft per pagina {orders:[...]}; uitpakken tot losse orders.\n"
    "const shopOrd   = $('Shopify: orders').all().flatMap(i => i.json.orders || []);")
code = code.replace(
    "const shopProd  = $('Shopify: producten').all().map(i => i.json);",
    "const shopProd  = $('Shopify: producten').all().flatMap(i => i.json.products || []);")
assert 'flatMap(i => i.json.orders' in code, 'Shopify-orders niet gevonden in de analysecode'
a['parameters']['jsCode'] = code

# ---- 2. nieuwe nodes ----
QL = ("FROM inventory SHOW ending_inventory_units, inventory_units_sold, days_out_of_stock "
      "GROUP BY product_variant_sku SINCE -{d}d UNTIL today LIMIT 100000")
gql = ('{ d28: shopifyqlQuery(query: \\"' + QL.format(d=28) + '\\") { tableData { rows } parseErrors } '
       'd365: shopifyqlQuery(query: \\"' + QL.format(d=365) + '\\") { tableData { rows } parseErrors } }')
nieuw = [
    {"parameters": {"rule": {"interval": [{"field": "days", "triggerAtHour": 7, "triggerAtMinute": 30}]}},
     "id": "trigger-daily", "name": "Elke dag 07:30", "type": "n8n-nodes-base.scheduleTrigger",
     "typeVersion": 1.3, "position": [-460, 520],
     "notes": "Dagelijkse run voor de uitverkoopradar. Mailt alleen als er iets acuut is."},
    {"parameters": {
        "method": "POST",
        "url": "={{ 'https://' + $json.domein + '.myshopify.com/admin/api/2024-10/graphql.json' }}",
        "sendHeaders": True,
        "headerParameters": {"parameters": [{"name": "X-Shopify-Access-Token", "value": "={{ $env[$json.token] }}"}]},
        "sendBody": True, "specifyBody": "json",
        "jsonBody": "={{ JSON.stringify({ query: \"" + gql + "\" }) }}",
        "options": {"timeout": 180000, "batching": {"batch": {"batchSize": 1, "batchInterval": 2000}}}},
     "id": "shop-ql", "name": "ShopifyQL: voorraad", "type": "n8n-nodes-base.httpRequest",
     "typeVersion": 4.4, "position": [-240, 1420],
     "notes": "Per shop: eindstand, verkoop en dagen uit voorraad, 28 en 365 dagen. Eén shop per keer, ShopifyQL heeft een strakke limiet."},
    {"parameters": {"mode": "append", "numberInputs": 8},
     "id": "wacht", "name": "Wacht op alle bronnen", "type": "n8n-nodes-base.merge",
     "typeVersion": 3.2, "position": [0, 700],
     "notes": "Zonder dit wachtpunt draait de analyse een keer per binnenkomende bron."},
    {"parameters": {"mode": "runOnceForAllItems", "language": "javaScript", "jsCode": js('uitverkoopradar.js')},
     "id": "radar", "name": "Uitverkoopradar", "type": "n8n-nodes-base.code",
     "typeVersion": 2, "position": [440, 700]},
    {"parameters": {"mode": "runOnceForAllItems", "language": "javaScript", "jsCode": js('weekrapport.js')},
     "id": "rapport", "name": "Weekrapport bouwen", "type": "n8n-nodes-base.code",
     "typeVersion": 2, "position": [660, 700]},
    {"parameters": {"conditions": {"options": {"caseSensitive": True, "leftValue": "", "typeValidation": "loose"},
        "conditions": [{"id": "stuur", "leftValue": "={{ $json.maandag || $json.urgent > 0 }}",
                        "rightValue": True, "operator": {"type": "boolean", "operation": "true", "singleValue": True}}],
        "combinator": "and"}, "options": {}},
     "id": "versturen", "name": "Versturen?", "type": "n8n-nodes-base.if",
     "typeVersion": 2.2, "position": [880, 700]},
    {"parameters": {"conditions": {"options": {"caseSensitive": True, "leftValue": "", "typeValidation": "loose"},
        "conditions": [{"id": "ma", "leftValue": "={{ new Date().getDay() === 1 && $json.signaal !== 'OK' }}",
                        "rightValue": True, "operator": {"type": "boolean", "operation": "true", "singleValue": True}}],
        "combinator": "and"}, "options": {}},
     "id": "alleen-signalen", "name": "Maandag, alleen signalen", "type": "n8n-nodes-base.filter",
     "typeVersion": 2.2, "position": [440, 480]},
]
# oude rapportnode vervangen; nodes uit een eerdere run eerst weghalen, zodat dit script
# vaker gedraaid kan worden zonder dubbele nodes
namen = {n['name'] for n in nieuw}
w['nodes'] = [n for n in w['nodes'] if n['name'] not in namen] + nieuw
nodes = {n['name']: n for n in w['nodes']}
nodes['Mail het weekrapport']['parameters']['subject'] = "={{ $json.onderwerp }}"
nodes['Analyse: signaal per maat']['position'] = [220, 700]
nodes['Snapshot wegschrijven']['position'] = [660, 480]
nodes['Mail het weekrapport']['position'] = [1100, 680]

# ---- 3. verbindingen opnieuw ----
def naar(*doelen):
    return {"main": [[{"node": d, "type": "main", "index": i} for d, i in doelen]]}
bronnen = ['Merk-config', 'CE: producten (alle maten)', 'CE: orders 53 weken', 'CE: retouren 53 weken',
           'CE: voorraadmutaties', 'Webshops']
c = {}
for trig in ('Elke maandag 07:00', 'Elke dag 07:30'):
    c[trig] = naar(*[(b, 0) for b in bronnen])
c['Webshops'] = naar(('Shopify: orders', 0), ('Shopify: producten', 0), ('ShopifyQL: voorraad', 0))
volgorde = ['Merk-config', 'CE: producten (alle maten)', 'CE: orders 53 weken', 'CE: retouren 53 weken',
            'CE: voorraadmutaties', 'Shopify: orders', 'Shopify: producten', 'ShopifyQL: voorraad']
for i, b in enumerate(volgorde):
    c[b] = naar(('Wacht op alle bronnen', i))
c['Wacht op alle bronnen'] = naar(('Analyse: signaal per maat', 0))
c['Analyse: signaal per maat'] = naar(('Uitverkoopradar', 0), ('Maandag, alleen signalen', 0))
c['Maandag, alleen signalen'] = naar(('Snapshot wegschrijven', 0))
c['Uitverkoopradar'] = naar(('Weekrapport bouwen', 0))
c['Weekrapport bouwen'] = naar(('Versturen?', 0))
c['Versturen?'] = {"main": [[{"node": "Mail het weekrapport", "type": "main", "index": 0}], []]}
w['connections'] = c

# De analyse draait eenmaal per run; de radar leest zijn bronnen zelf via $('...')
json.dump(w, open(PAD, 'w'), indent=2, ensure_ascii=False)
print(f"workflow herbouwd: {len(w['nodes'])} nodes, {sum(len(v['main'][0]) for v in c.values())} verbindingen")
