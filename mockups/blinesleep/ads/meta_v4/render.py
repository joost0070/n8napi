# Rendert elk .ad-blok uit ads.html naar een losse jpg op ware grootte (1x).
import os,sys
from playwright.sync_api import sync_playwright
os.makedirs('uit',exist_ok=True)
with sync_playwright() as pw:
    b=pw.chromium.launch(executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/chrome")
    pg=b.new_page(viewport={'width':1400,'height':2200},device_scale_factor=1)
    pg.goto('file://'+os.path.abspath(sys.argv[1] if len(sys.argv)>1 else 'ads.html')); pg.wait_for_timeout(1500)
    pg.evaluate("document.fonts.ready")
    for el in pg.query_selector_all('.ad'):
        i=el.get_attribute('id'); el.screenshot(path=f'uit/bline-meta-{i}.jpg',type='jpeg',quality=92); print(i)
    b.close()
