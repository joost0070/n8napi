from pathlib import Path
from playwright.sync_api import sync_playwright
D = Path(__file__).parent.resolve()
JOBS = [("bline-logo.svg", 2000, 839), ("bline-logo-wit.svg", 2000, 839), ("bline-logo-sleep.svg", 2000, 1196), ("bline-icoon.svg", 512, 512)]
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/chrome")
    for f, w, h in JOBS:
        pg = b.new_page(viewport={"width": w, "height": h})
        svg = (D/f).read_text().replace("<svg ", '<svg width="%d" height="%d" ' % (w, h))
        pg.set_content('<html><body style="margin:0;background:transparent">' + svg + '</body></html>')
        pg.screenshot(path=str(D/f.replace(".svg", ".png")), omit_background=True)
        pg.close()
    b.close()
print("ok")
