import json,threading,functools,http.server,socketserver,re
from playwright.sync_api import sync_playwright
SITE='site_r3'
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*a): pass
srv=socketserver.TCPServer(('127.0.0.1',0),functools.partial(Q,directory=SITE)); threading.Thread(target=srv.serve_forever,daemon=True).start()
bundel=open(SITE+'/product_lade_bundel.html').read()
gevraagd={}
def add(route):
    gevraagd['body']=json.loads(route.request.post_data)
    route.fulfill(status=200,content_type='application/json',body=json.dumps({'id':1,'sections':{'cart-drawer':bundel,'cart-icon-bubble':'<div class="shopify-section"><span>2</span></div>'}}))
with sync_playwright() as pw:
    b=pw.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
    c=b.new_context(viewport={'width':390,'height':844},device_scale_factor=2,is_mobile=True,has_touch=True); c.route('https://cdn.shopify.com/**',lambda r:r.fulfill(status=200,body=b''))
    p=c.new_page(); p.route('**/cart/add.js',add)
    p.goto(f'http://127.0.0.1:{srv.server_address[1]}/product.html'); p.wait_for_load_state('networkidle')
    p.evaluate("document.querySelector('cart-drawer').open()"); p.wait_for_timeout(800)
    p.click('[data-bline-upsell]'); p.wait_for_timeout(1500)
    print('verzoek:',gevraagd.get('body'))
    print('regels na klik:',p.evaluate("[...document.querySelectorAll('cart-drawer .cart-item__name')].map(e=>e.textContent.trim())"))
    print('upsell nog zichtbaar:',p.evaluate("!!document.querySelector('cart-drawer .bline-upsell')"))
    print('totaal:',p.evaluate("document.querySelector('cart-drawer .totals__total-value').textContent.trim()"))
