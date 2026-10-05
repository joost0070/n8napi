import sys, os, time, threading, http.server, functools, socketserver, hashlib, requests, json
from playwright.sync_api import sync_playwright
SITE, OUT = sys.argv[1], sys.argv[2]; os.makedirs(OUT, exist_ok=True)
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
class S(socketserver.ThreadingMixIn, http.server.HTTPServer): daemon_threads = True
srv = S(('127.0.0.1', 0), functools.partial(Q, directory=SITE)); port = srv.server_address[1]
threading.Thread(target=srv.serve_forever, daemon=True).start()
BASE = f'http://127.0.0.1:{port}/'
EXE = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'
VIEWS = {'mobiel': dict(viewport={'width': 390, 'height': 844}, device_scale_factor=2, is_mobile=True, has_touch=True),
         'desktop': dict(viewport={'width': 1366, 'height': 800}, device_scale_factor=1)}
CACHE = 'cdn_cache'; os.makedirs(CACHE, exist_ok=True)
def cdn(route):
    u = route.request.url; f = os.path.join(CACHE, hashlib.md5(u.encode()).hexdigest())
    if not os.path.exists(f):
        r = requests.get(u, timeout=60)
        if r.status_code != 200: return route.fulfill(status=r.status_code, body=b'')
        open(f, 'wb').write(r.content); open(f + '.ct', 'w').write(r.headers.get('content-type', 'image/jpeg'))
    route.fulfill(status=200, body=open(f, 'rb').read(), headers={'content-type': open(f + '.ct').read(), 'access-control-allow-origin': '*'})
PAGES = {'home': 'home.html', 'collectie_leeskussens': 'collection.html', 'collectie_hoezen': 'collection_hoezen.html', 'leeskussen_beige': 'product.html', 'leeskussen_wit': 'product_wit.html'}
MEET = '''() => {
 const r = {};
 const ban = document.querySelector('.banner__media img'); if (ban) r.banner = {src: ban.currentSrc.split('/').pop().split('?')[0], w: ban.getBoundingClientRect().width, h: ban.getBoundingClientRect().height};
 r.kaarten = [...document.querySelectorAll('.card__media img')].slice(0, 12).map(i => i.currentSrc.split('/').pop().split('?')[0].split('&')[0]);
 r.galerij = [...document.querySelectorAll('.product__media-list .product__media img, .product__media-list img')].map(i => i.getAttribute('src').split('/').pop().split('?')[0]).filter((v,i,a)=>a.indexOf(v)===i);
 const t = document.querySelector('.slider-counter'); if (t) r.teller = t.innerText.replace(/\\s+/g,' ');
 return r; }'''
met = {}
with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path=EXE, args=['--no-sandbox'])
    for vn, vopt in VIEWS.items():
        ctx = b.new_context(**vopt, locale='nl-NL'); ctx.route('https://cdn.shopify.com/**', cdn); p = ctx.new_page()
        for name, f in PAGES.items():
            if name == 'leeskussen_wit' and vn == 'desktop': pass
            p.goto(BASE + f); p.wait_for_load_state('networkidle', timeout=60000); p.evaluate('document.fonts.ready')
            p.evaluate('window.scrollTo(0, document.body.scrollHeight)'); time.sleep(1.0); p.evaluate('window.scrollTo(0,0)'); time.sleep(0.8)
            p.screenshot(path=f'{OUT}/{name}_{vn}_eerste_scherm.jpg', quality=82, type='jpeg')
            p.screenshot(path=f'{OUT}/{name}_{vn}_volledig.jpg', full_page=True, quality=72, type='jpeg')
            met[f'{name}_{vn}'] = p.evaluate(MEET)
        ctx.close()
    b.close()
json.dump(met, open(f'{OUT}/metingen.json', 'w'), indent=1, ensure_ascii=False)
print(json.dumps(met, indent=1, ensure_ascii=False)[:4000])
