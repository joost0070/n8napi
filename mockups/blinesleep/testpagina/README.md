# Testpagina's van het Bline-thema (sessie 7)

Rendert de echte Liquid-bestanden van het Dawn-thema lokaal met liquidjs, met de echte productdata, en maakt screenshots met Playwright.

1. Thema ophalen in `theme/` (Admin API, `themeFiles`) en productdata in `data.json` en `content.json` (Admin API). Die ophaalscripts staan niet in de repo, omdat ze de winkelnaam bevatten.
2. `node render.js <themamap> <uitmap>`: schrijft product, lade, home, hoes, collectie, blog, artikel en pagina's als HTML.
3. `python3 shoot.py <uitmap> <screenshotmap>`: 390 x 844 en 1366 x 800, met metingen in `metingen.json`.
4. `python3 upselltest.py`: klikt op de upsell in de lade en controleert welke hoes wordt aangevraagd.

Benadering: Shopify-filters zijn nagebouwd (zie `render.js`), het reviewblok van Judge.me is nagebootst met dezelfde klassen (`extra/__app_block.liquid`), betaaliconen zijn grijze plaatsvervangers en de winkelwagen wordt niet echt gevuld.
