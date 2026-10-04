"""Renders the mockups to PNG with Playwright (Chromium)."""
import os
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).parent.resolve()
OUT = ROOT / "screenshots"
OUT.mkdir(exist_ok=True)

SHOTS = [
    ("index.html", "01_home_desktop.png", (1440, 900), True),
    ("product.html", "02_product_desktop.png", (1440, 900), True),
    ("bewijs.html", "03_bewijs_desktop.png", (1440, 900), True),
    ("cart.html", "04_cart_desktop.png", (1440, 900), True),
    ("index.html", "05_home_mobile.png", (390, 844), True),
    ("product.html", "06_product_mobile.png", (390, 844), True),
]

only = set(sys.argv[1:])


def find_chromium():
    base = Path(os.environ.get("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers"))
    for cand in [base / "chromium-1194/chrome-linux/chrome", base / "chromium/chrome-linux/chrome"]:
        if cand.exists():
            return str(cand)
    return None


with sync_playwright() as p:
    try:
        browser = p.chromium.launch()
    except Exception:
        browser = p.chromium.launch(executable_path=find_chromium())
    for src, out, (w, h), full in SHOTS:
        if only and out not in only:
            continue
        mobile = w < 500
        ctx = browser.new_context(viewport={"width": w, "height": h}, device_scale_factor=2 if mobile else 1,
                                  is_mobile=mobile, has_touch=mobile)
        page = ctx.new_page()
        page.goto((ROOT / src).as_uri())
        page.evaluate("document.fonts.ready")
        page.wait_for_timeout(300)
        page.screenshot(path=str(OUT / out), full_page=full)
        print("shot", out, page.evaluate("document.documentElement.scrollHeight"),
              "overflowX" if page.evaluate("document.documentElement.scrollWidth > innerWidth") else "")
        ctx.close()
    browser.close()
