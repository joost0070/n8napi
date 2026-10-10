"""Sessie 9: uitsneden van de nieuwe blokken en metingen. python3 shoot_s9.py <sitedir> <uitdir>"""
import sys, json, os, time, threading, http.server, functools, socketserver
from playwright.sync_api import sync_playwright
sys.argv += []
SITE, OUT = sys.argv[1], sys.argv[2]; os.makedirs(OUT, exist_ok=True)
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
srv = socketserver.ThreadingTCPServer(('127.0.0.1', 0), functools.partial(Q, directory=SITE)); srv.daemon_threads = True
threading.Thread(target=srv.serve_forever, daemon=True).start(); BASE = f'http://127.0.0.1:{srv.server_address[1]}/'
import shoot_cdn
VIEWS = {'mobiel': dict(viewport={'width': 390, 'height': 844}, device_scale_factor=2, is_mobile=True, has_touch=True), 'desktop': dict(viewport={'width': 1366, 'height': 800}, device_scale_factor=1)}
MEET = """(sel) => { const e = document.querySelector(sel); if (!e) return null; const b = e.getBoundingClientRect(); const cs = getComputedStyle(e);
  return { top: Math.round(b.top + scrollY), h: Math.round(b.height), w: Math.round(b.width), font: cs.fontSize, weight: cs.fontWeight, color: cs.color, tekst: (e.innerText || '').trim().slice(0, 90) }; }"""
def wait(p): p.wait_for_load_state('networkidle', timeout=30000); p.evaluate('document.fonts.ready'); time.sleep(0.6)
def naar(p, sel, boven=120):
    p.evaluate(f"window.scrollTo(0, document.querySelector('{sel}').getBoundingClientRect().top + scrollY - {boven})"); time.sleep(0.8)
m = {}
with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args=['--no-sandbox'])
    for vn, vo in VIEWS.items():
        ctx = b.new_context(**vo, locale='nl-NL'); ctx.route('https://cdn.shopify.com/**', shoot_cdn.cdn); p = ctx.new_page()
        p.goto(BASE + 'product.html'); wait(p)
        r = {k: p.evaluate(MEET, s) for k, s in {'knop': '.product-form__submit', 'betaal': '.bline-betaal', 'bol': '.product__info-container .bline-bol', 'gemaakt': '.bline-gemaakt', 'gemaakt_kop': '.bline-gemaakt__kop', 'gemaakt_link': '.bline-gemaakt a', 'goed_om_te_weten': '.bline-waarom', 'voet_tel': 'footer a[href^="tel:"]'}.items()}
        r['bol_direct_onder_betaal'] = p.evaluate("(() => { const a = document.querySelector('.bline-betaal'), b = document.querySelector('.product__info-container .bline-bol'); return a && b && a.nextElementSibling === b; })()")
        r['bol_link'] = p.evaluate("!!document.querySelector('.bline-bol a')"); r['bol_img'] = p.evaluate("!!document.querySelector('.bline-bol img, .bline-bol svg')")
        m['product_' + vn] = r
        naar(p, '.bline-betaal', 360 if vn == 'mobiel' else 420); p.screenshot(path=f'{OUT}/product_{vn}_bol_onder_betaaliconen.png')
        naar(p, '.bline-gemaakt', 300); p.screenshot(path=f'{OUT}/product_{vn}_gemaakt_door.png')
        naar(p, 'footer a[href^="tel:"]', 400); p.screenshot(path=f'{OUT}/product_{vn}_voettekst_telefoon.png')
        p.goto(BASE + 'home.html'); wait(p)
        m['home_' + vn] = {k: p.evaluate(MEET, s) for k, s in {'raster_leeskussens': '#shopify-section-template--1__leeskussens', 'bol': '.bline-bol-sectie', 'bol_tekst': '.bline-bol', 'raster_hoezen': '#shopify-section-template--1__hoezen'}.items()}
        naar(p, '#shopify-section-template--1__leeskussens', 0 if vn == 'mobiel' else -150); p.screenshot(path=f'{OUT}/home_{vn}_bol_onder_raster.png')
        p.goto(BASE + 'page.html'); wait(p)
        m['over_bline_' + vn] = {'foto_sectie': p.evaluate("document.querySelectorAll('.bline-foto').length"), 'img_in_main': p.evaluate("document.querySelectorAll('main img').length"), 'titel': p.evaluate(MEET, 'main h1'), 'tel': p.evaluate(MEET, 'main a[href^=\"tel:\"]')}
        p.screenshot(path=f'{OUT}/over_bline_{vn}_volledig.png', full_page=True)
        ctx.close()
    b.close()
json.dump(m, open(f'{OUT}/metingen_s9.json', 'w'), indent=1, ensure_ascii=False); print(json.dumps(m, indent=1, ensure_ascii=False))
