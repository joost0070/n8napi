# Bline thema v3 (concept, nog niet in de winkel)

Nieuwe secties voor de Dawn-winkel: het leeskussen als één product in vijf kleuren, met een speelse, afwisselende opbouw. Alleen goedgekeurde originele beelden (Higgsfield/bol en de shoot), geen eigen montages.

- `sections/b3-product.liquid`: galerij per kleur (media van elk kleurproduct), kleur wisselen zonder de pagina te verlaten, 1 of 2 kussens, extra hoes in dezelfde kleur, knop met totaalprijs, plakbalk op mobiel.
- `sections/b3-band`, `b3-momenten`, `b3-binnenkant`, `b3-kleuren`, `b3-verhaal` (video), `b3-score`, `b3-vergelijk`, `b3-hoezen`, `b3-vragen`.
- `snippets/b3-head.liquid` (in `layout/theme.liquid` vlak voor `</head>`), `b3-icoon`, `b3-ster`.
- `assets/bline-v3.css`, `bline-v3.js`, lettertypen Poppins en Instrument Serif (lokaal, woff2, OFL).
- `templates/index.json` en `product.json`: volgorde van de secties.
- `galerijvolgorde.json`: voorgestelde volgorde van de media per kleur (in Shopify zetten met `productReorderMedia`; Wit krijgt `wit-gebruik-05` en `-06` erbij, de eigen bewerkte details en de maatgids-tekening gaan eraf).

Kortingen: rekent op de bestaande automatische kortingen (2 kussens of kussen + hoes: €9,99, niet stapelen). Getest: 1 = €79,99, 2 = €149,99, 1 + hoes = €104,99, 2 + hoes = €184,98, Wit + hoes = €89,99.
