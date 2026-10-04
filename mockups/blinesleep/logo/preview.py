from pathlib import Path
from playwright.sync_api import sync_playwright
D = Path(__file__).parent.resolve()
logo = (D/"bline-logo.svg").read_text(); wit = (D/"bline-logo-wit.svg").read_text()
sleep = (D/"bline-logo-sleep.svg").read_text(); icon = (D/"bline-icoon.svg").read_text()
html = f"""<html><head><style>
body{{margin:0;font-family:Inter,Arial;background:#fff}}
.row{{display:flex}} .c{{flex:1;height:300px;display:flex;align-items:center;justify-content:center}}
.c svg{{height:84px}} .s svg{{height:120px}}
.hdr{{display:flex;align-items:center;justify-content:space-between;padding:0 48px;height:84px;background:#F7F4EF;border-bottom:1px solid #E3DACB;font-size:14px;color:#1F2A37}}
.hdr svg{{height:34px}} .ic svg{{height:120px;margin:0 12px}} .ic .sm svg{{height:32px}} .ic .xs svg{{height:16px}}
</style></head><body>
<div class=hdr><span>Leeskussens&nbsp;&nbsp;&nbsp;Over Bline&nbsp;&nbsp;&nbsp;Vragen</span>{logo}<span>Zoeken&nbsp;&nbsp;&nbsp;Winkelwagen (0)</span></div>
<div class=row><div class=c style="background:#F7F4EF">{logo}</div><div class=c style="background:#1F2A37">{wit}</div><div class=c style="background:#8E8C88">{wit}</div></div>
<div class=row><div class="c s" style="background:#fff">{sleep}</div><div class="c ic" style="background:#fff">{icon}<span class=sm>{icon}</span><span class=xs>{icon}</span></div></div>
</body></html>"""
(D/"preview.html").write_text(html)
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/chrome"); pg = b.new_page(viewport={"width":1350,"height":684}); pg.goto((D/"preview.html").as_uri())
    pg.screenshot(path=str(D/"logo_voorbeeld.png")); b.close()
