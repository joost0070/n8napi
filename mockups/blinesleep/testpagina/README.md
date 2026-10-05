# Testpagina's van het Bline-thema (sessie 7)

Rendert de echte Liquid-bestanden van het Dawn-thema lokaal met liquidjs, met de echte productdata, en maakt screenshots met Playwright.

1. Thema ophalen in `theme/` (Admin API, `themeFiles`) en productdata in `data.json` en `content.json` (Admin API). Die ophaalscripts staan niet in de repo, omdat ze de winkelnaam bevatten.
2. `node render.js <themamap> <uitmap>`: schrijft product, lade, home, hoes, collectie, blog, artikel en pagina's als HTML.
3. `python3 shoot.py <uitmap> <screenshotmap>`: 390 x 844 en 1366 x 800, met metingen in `metingen.json`.
4. `python3 upselltest.py`: klikt op de upsell in de lade en controleert welke hoes wordt aangevraagd.

Benadering: Shopify-filters zijn nagebouwd (zie `render.js`), het reviewblok van Judge.me is nagebootst met dezelfde klassen (`extra/__app_block.liquid`), betaaliconen zijn grijze plaatsvervangers en de winkelwagen wordt niet echt gevuld.

Sessie 8 (elke kleur een eigen product): `render.js` slaat de oude producten `leeskussen` en `hoes-leeskussen` over, leest de lijst `bline.kleuren` als productreferenties, vult de collecties uit de echte collectiedata en rendert product per kleur (`product.html` is Beige, `product_<kleur>.html`), hoes Blauw (`hoes.html`) en de collecties Leeskussens en Hoezen. Lettertype: Nunito Sans (woff2, latin) in `site/fonts/`. `shoot.py` maakt ook een schermafdruk van de kleurkeuze en meet de kleurvlakken en productkaarten.
