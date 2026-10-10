# Testpagina's shop v2 (sessie 11)

- `edit.py`: maakt de 38 bewerkte beelden uit de goedgekeurde originelen (Pillow). Bronnen in `orig/`, uitvoer in `bewerkt/`.
- `tpl*.py`: schrijven de JSON-sjablonen (homepage, collectie, pagina's).
- `render2.js <thema> <uit> [pagina's]`: lokale Liquid-renderer (uitbreiding van `../render.js`): video, sets (`bline.set_onderdelen`), collectie-metafields (`bline.extra_kaarten`), `images[...]` uit Files (`images.json`), sjabloon per product en collectie, en de nieuwe pagina's.
- `shoot_v2.py <site> <uit>`: 390 x 844 (2x) en 1366 x 800, eerste scherm en volledig, met `metingen.json` (kapotte beelden, "Translation missing", breder dan scherm, kleine tekst).
- `shoot_menu.py`: megamenu desktop en mobiel menu open.
- `vergelijk.py`: Bline naast Yumeko en de ENV-stores.
- `stijl.py`: stijlcontrole over alle nieuwe teksten.

De ophaal- en uploadscripts staan niet in de repo, omdat ze de winkelnaam bevatten. Benadering zoals eerder: Judge.me nagebootst, betaaliconen als plaatsvervangers, video toont alleen de poster (Chromium zonder h264), winkelwagen niet echt gevuld.
