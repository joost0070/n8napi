import sys, os, time, threading, http.server, functools, socketserver
from playwright.sync_api import sync_playwright
sys.path.insert(0,'.')
from shoot_cdn import cdn
SITE, OUT = sys.argv[1], sys.argv[2]; os.makedirs(OUT, exist_ok=True)
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*a): pass
class S(socketserver.ThreadingMixIn, http.server.HTTPServer): daemon_threads=True
srv=S(('127.0.0.1',0),functools.partial(Q,directory=SITE)); port=srv.server_address[1]
threading.Thread(target=srv.serve_forever,daemon=True).start()
EXE='/opt/pw-browsers/chromium-1194/chrome-linux/chrome'
with sync_playwright() as pw:
    b=pw.chromium.launch(executable_path=EXE,args=['--no-sandbox'])
    ctx=b.new_context(viewport={'width':1366,'height':800}); ctx.route('https://cdn.shopify.com/**',cdn); p=ctx.new_page()
    p.goto(f'http://127.0.0.1:{port}/home.html'); p.wait_for_load_state('networkidle')
    p.evaluate("document.querySelector('details.mega-menu').setAttribute('open',''); document.querySelector('.mega-menu__content').style.zIndex=50"); time.sleep(1.0)
    print(p.evaluate("(()=>{const c=document.querySelector('.mega-menu__content');const cs=getComputedStyle(c);const r=c.getBoundingClientRect();return [cs.opacity,cs.visibility,cs.display,r.top,r.height,cs.zIndex]})()"))
    p.screenshot(path=f'{OUT}/megamenu_desktop.jpg',quality=80,type='jpeg')
    ctx.close()
    ctx=b.new_context(viewport={'width':390,'height':844},device_scale_factor=2,is_mobile=True,has_touch=True); ctx.route('https://cdn.shopify.com/**',cdn); p=ctx.new_page()
    p.goto(f'http://127.0.0.1:{port}/home.html'); p.wait_for_load_state('networkidle')
    p.evaluate("(()=>{const d=document.querySelector('#Details-menu-drawer-container');d.setAttribute('open','');d.classList.add('menu-opening');document.body.classList.add('overflow-hidden-tablet')})()"); time.sleep(1.2)
    p.screenshot(path=f'{OUT}/menu_mobiel.jpg',quality=80,type='jpeg')
    ctx.close(); b.close()
