"""Screenshots van de lokaal gerenderde testpagina's. Gebruik: python3 shoot.py <sitedir> <uitdir> [prefix]"""
import sys, json, os, subprocess, time, threading, http.server, functools, socketserver
from playwright.sync_api import sync_playwright
SITE, OUT = sys.argv[1], sys.argv[2]; PRE = sys.argv[3] if len(sys.argv) > 3 else ''
os.makedirs(OUT, exist_ok=True)
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
H = functools.partial(Q, directory=SITE)
class S(socketserver.ThreadingMixIn, http.server.HTTPServer): daemon_threads = True
srv = S(('127.0.0.1', 0), H); port = srv.server_address[1]
threading.Thread(target=srv.serve_forever, daemon=True).start()
BASE = f'http://127.0.0.1:{port}/'
EXE = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'
VIEWS = {'mobiel': dict(viewport={'width': 390, 'height': 844}, device_scale_factor=2, is_mobile=True, has_touch=True),
         'desktop': dict(viewport={'width': 1366, 'height': 800}, device_scale_factor=1)}
metingen = {}
import requests, hashlib
CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cdn_cache'); os.makedirs(CACHE, exist_ok=True)
def cdn(route):
    u = route.request.url; f = os.path.join(CACHE, hashlib.md5(u.encode()).hexdigest())
    if not os.path.exists(f):
        r = requests.get(u, timeout=60)
        if r.status_code != 200: return route.fulfill(status=r.status_code, body=b'')
        open(f, 'wb').write(r.content); open(f + '.ct', 'w').write(r.headers.get('content-type', 'image/jpeg'))
    route.fulfill(status=200, body=open(f, 'rb').read(), headers={'content-type': open(f + '.ct').read(), 'access-control-allow-origin': '*'})
def wait(p):
    p.wait_for_load_state('networkidle', timeout=30000); p.evaluate('document.fonts.ready'); time.sleep(0.6)
with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path=EXE, args=['--no-sandbox'])
    for vn, vopt in VIEWS.items():
        ctx = b.new_context(**vopt, locale='nl-NL'); ctx.route('https://cdn.shopify.com/**', cdn); p = ctx.new_page()
        # productpagina
        p.goto(BASE + 'product.html'); wait(p)
        p.screenshot(path=f'{OUT}/{PRE}product_{vn}_eerste_scherm.png')
        p.screenshot(path=f'{OUT}/{PRE}product_{vn}_volledig.png', full_page=True)
        p.evaluate("window.scrollTo(0, document.querySelector('.bline-kleurkeuze').getBoundingClientRect().top + scrollY - 140)"); time.sleep(0.8)
        p.screenshot(path=f'{OUT}/{PRE}product_{vn}_kleurkeuze.png'); p.evaluate('window.scrollTo(0,0)'); time.sleep(0.4)
        metingen[f'product_{vn}'] = p.evaluate(open(os.path.join(os.path.dirname(__file__), 'meet.js')).read())
        # homepage
        p.goto(BASE + 'home.html'); wait(p)
        p.screenshot(path=f'{OUT}/{PRE}home_{vn}_eerste_scherm.png')
        p.screenshot(path=f'{OUT}/{PRE}home_{vn}_volledig.png', full_page=True)
        metingen[f'home_{vn}'] = p.evaluate(open(os.path.join(os.path.dirname(__file__), 'meet.js')).read())
        # lade
        for naam in ['product', 'product_lade_bundel']:
            p.goto(BASE + naam + '.html'); wait(p)
            p.evaluate("document.querySelector('cart-drawer') && document.querySelector('cart-drawer').open()"); time.sleep(1)
            p.screenshot(path=f'{OUT}/{PRE}lade_{vn}{"_bundel" if "bundel" in naam else ""}.png')
            metingen[f'lade_{vn}{"_bundel" if "bundel" in naam else ""}'] = p.evaluate(open(os.path.join(os.path.dirname(__file__), 'meet_lade.js')).read())
        for extra in ['hoes', 'collection', 'collection_hoezen', 'page', 'article', 'blog', 'vergelijking', 'vragen']:
            if os.path.exists(os.path.join(SITE, extra + '.html')):
                p.goto(BASE + extra + '.html'); wait(p)
                p.screenshot(path=f'{OUT}/{PRE}{extra}_{vn}_eerste_scherm.png')
                if extra in ('hoes', 'collection'):
                    p.screenshot(path=f'{OUT}/{PRE}{extra}_{vn}_volledig.png', full_page=True)
                    metingen[f'{extra}_{vn}'] = p.evaluate(open(os.path.join(os.path.dirname(__file__), 'meet.js')).read())
        ctx.close()
    b.close()
json.dump(metingen, open(f'{OUT}/{PRE}metingen.json', 'w'), indent=1, ensure_ascii=False)
print('ok')
