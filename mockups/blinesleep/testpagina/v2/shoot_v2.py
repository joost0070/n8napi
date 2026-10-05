import sys, os, time, threading, http.server, functools, socketserver, json
from playwright.sync_api import sync_playwright
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shoot_cdn import cdn
SITE, OUT = sys.argv[1], sys.argv[2]; os.makedirs(OUT, exist_ok=True)
ONLY = sys.argv[3].split(',') if len(sys.argv) > 3 else None
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
class S(socketserver.ThreadingMixIn, http.server.HTTPServer): daemon_threads = True
srv = S(('127.0.0.1', 0), functools.partial(Q, directory=SITE)); port = srv.server_address[1]
threading.Thread(target=srv.serve_forever, daemon=True).start()
BASE = f'http://127.0.0.1:{port}/'
EXE = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'
VIEWS = {'mobiel': dict(viewport={'width': 390, 'height': 844}, device_scale_factor=2, is_mobile=True, has_touch=True),
         'desktop': dict(viewport={'width': 1366, 'height': 800}, device_scale_factor=1)}
PAGES = {'home': 'home.html', 'collectie': 'collectie.html', 'product': 'product.html', 'materialen': 'materialen.html', 'lezen_in_bed': 'lezen-in-bed.html',
         'product_wit': 'product_wit.html', 'set': 'set.html', 'collectie_beige': 'collectie_beige.html', 'collectie_hoezen': 'collectie_hoezen.html', 'kleurengids': 'kleurengids.html', 'maatgids': 'maatgids.html', 'bline_sleep': 'bline-sleep.html'}
if ONLY: PAGES = {k: v for k, v in PAGES.items() if k in ONLY}
MEET = '''() => {
 const r = {};
 r.kapotte_beelden = [...document.images].filter(i => i.complete && i.naturalWidth === 0 && i.getAttribute('src')).map(i => i.getAttribute('src').slice(0,120));
 r.translation_missing = document.body.innerText.includes('Translation missing');
 r.breder_dan_scherm = document.documentElement.scrollWidth > window.innerWidth + 1;
 r.hoogte = document.documentElement.scrollHeight;
 r.secties = [...document.querySelectorAll('main .shopify-section')].map(s => { const h = s.querySelector('h1,h2,.title'); return (h ? h.innerText.trim().slice(0,40) : s.id.split('__').pop()); });
 const klein = []; document.querySelectorAll('main p, main li, main a, main span, main td, main th').forEach(e => { const cs = getComputedStyle(e); if (e.offsetParent && e.innerText && e.innerText.trim() && e.children.length === 0 && parseFloat(cs.fontSize) < 14) klein.push(e.innerText.trim().slice(0,30) + ' ' + cs.fontSize); });
 r.tekst_onder_14px = klein.slice(0, 15);
 return r; }'''
met = {}
with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path=EXE, args=['--no-sandbox'])
    for vn, vopt in VIEWS.items():
        ctx = b.new_context(**vopt, locale='nl-NL'); ctx.route('https://cdn.shopify.com/**', cdn); p = ctx.new_page()
        for name, f in PAGES.items():
            p.goto(BASE + f); p.wait_for_load_state('networkidle', timeout=90000); p.evaluate('document.fonts.ready')
            h = p.evaluate('document.documentElement.scrollHeight')
            for y in range(0, h, 600): p.evaluate(f'window.scrollTo(0,{y})'); time.sleep(0.05)
            time.sleep(1.0); p.evaluate('window.scrollTo(0,0)'); time.sleep(0.6)
            p.screenshot(path=f'{OUT}/{name}_{vn}_eerste_scherm.jpg', quality=80, type='jpeg')
            p.screenshot(path=f'{OUT}/{name}_{vn}_volledig.jpg', full_page=True, quality=60, type='jpeg', scale='css')
            met[f'{name}_{vn}'] = p.evaluate(MEET)
        ctx.close()
    b.close()
json.dump(met, open(f'{OUT}/metingen.json', 'w'), indent=1, ensure_ascii=False)
for k, v in met.items(): print(k, 'kapot', len(v['kapotte_beelden']), 'TM', v['translation_missing'], 'breed', v['breder_dan_scherm'], 'h', v['hoogte'], 'klein', v['tekst_onder_14px'][:4])
