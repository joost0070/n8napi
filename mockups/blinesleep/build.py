"""Builds the static Bline Sleep mockup pages (index, product, bewijs, cart).

Run: python3 build.py   (writes the .html files next to this script)
"""
from pathlib import Path

import art
from art import icon

OUT = Path(__file__).parent


def page(title, body, desc=""):
    return f"""<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="styles.css">
</head>
<body>
{body}
</body>
</html>
"""


def header(active="", cart=0):
    links = [("Dekbedden", "product.html"), ("Beddengoed", "#"), ("Kussens &amp; sloop", "#"),
             ("Ons bewijs", "bewijs.html"), ("Van de fabriek", "#")]
    act = ' class="active"'
    nav = "".join(f'<a href="{h}"{act if t == active else ""}>{t}</a>' for t, h in links)
    count = f'<span class="cart-count">{cart}</span>' if cart else ""
    return f"""
<div class="announce">Volgende verzending uit onze fabriek vertrekt <b>donderdag</b><span class="sep">·</span>Gratis retour in Nederland</div>
<header class="site-header">
  <div class="container">
    <a class="menu-btn" href="#" aria-label="Menu">{icon('menu')}</a>
    <a class="logo" href="index.html" aria-label="bline sleep, naar de homepage"><span class="word">bline</span><span class="mark"></span><span class="sub">sleep</span></a>
    <nav class="nav" aria-label="Hoofdmenu">{nav}</nav>
    <div class="header-icons">
      <a href="#" aria-label="Zoeken">{icon('search')}</a>
      <a href="#" class="hide-m" aria-label="Account">{icon('user')}</a>
      <a href="cart.html" aria-label="Winkelwagen">{icon('bag')}{count}</a>
    </div>
  </div>
</header>"""


def footer():
    return f"""
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-about">
        <a class="logo" href="index.html"><span class="word">bline</span><span class="mark"></span><span class="sub">sleep</span></a>
        <p>Premium dekbedden, beddengoed en zijde, rechtstreeks van de fabriek. Met de cijfers erbij.</p>
        <div class="footer-contact">
          <span>{icon('chat')} Klantenservice in het Nederlands</span>
          <span>{icon('clock')} Ma t/m vr, 9:00 tot 17:00</span>
          <span>{icon('mail')} hallo@blinesleep.nl</span>
        </div>
      </div>
      <div><h4>Shop</h4><ul><li>Dekbedden</li><li>Beddengoed</li><li>Kussens &amp; sloop</li><li>De Slaapset</li></ul></div>
      <div><h4>Ons bewijs</h4><ul><li>Specificaties</li><li>Certificaat checken</li><li>Labrapporten</li><li>Van de fabriek</li></ul></div>
      <div><h4>Service</h4><ul><li>Bezorging &amp; drops</li><li>100 nachten proefslapen</li><li>Retourneren</li><li>Wassen &amp; onderhoud</li></ul></div>
      <div><h4>Over Bline</h4><ul><li>Ons verhaal</li><li>Contact</li><li>Voorwaarden</li><li>Privacy</li></ul></div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 Bline Sleep · KvK 00000000 · Verzonden vanuit Nederland</span>
      {pay_badges()}
    </div>
  </div>
</footer>"""


def pay_badges():
    return ('<div class="pay-badges"><span class="pay ideal">iDEAL</span><span class="pay bancontact">Bancontact</span>'
            '<span class="pay klarna">Klarna</span><span class="pay">Creditcard</span></div>')


CHECK_ZELF = f'<a class="check-link" href="#">Check zelf {icon("external")}</a>'


# ======================================================================= HOME
def home():
    trust = [
        ("shield", "Certificaat zelf checken", "Elk nummer staat bij het product, met directe link."),
        ("truck", "Levering vanuit Nederland", "Verzonden uit ons magazijn, bezorgd door PostNL."),
        ("moon", "100 nachten proefslapen", "Op al onze dekbedden. Niet goed, dan gratis retour."),
        ("flask", "Labgetest per partij", "Onafhankelijk lab, uitslag per partij openbaar."),
    ]
    trust_html = "".join(f'<div class="trust-item"><span class="ic">{icon(i)}</span><div><b>{t}</b><span>{d}</span></div></div>' for i, t, d in trust)

    cards = [
        ("duvet", ("#F2ECE2", "#E0D4C1"), "Wekelijkse drop", "gold", "Het Donsdekbed", "vanaf", "€399",
         "95% ganzendons · 750+ cuin · Tencel tijk", ["4 seizoenen", "Zomer", "4 maten"]),
        ("sheets", ("#EEF0EA", "#D7DDD0"), "Op voorraad", "", "Tencel beddengoed", "vanaf", "€159",
         "100% Tencel lyocell · 300TC · koel en zacht", ["Overtrek + 2 slopen", "4 kleuren"]),
        ("silk", ("#F4EEE6", "#E2D5C2"), "Op voorraad", "", "Zijden kussensloop", "", "€59",
         "100% moerbeizijde · 22 momme · grade 6A", ["60 x 70 cm", "3 kleuren"]),
    ]
    cards_html = ""
    for kind, bg, tag, tagc, name, pre, price, spec, chips in cards:
        chip_html = "".join(f'<span class="chip">{c}</span>' for c in chips)
        pre_html = f"<small>{pre}</small>" if pre else ""
        cards_html += f"""
      <article class="product-card">
        <a href="product.html" class="media"><span class="tag pill {tagc}"><span class="dot"></span>{tag}</span>{art.product_scene(kind, bg, label=name)}</a>
        <div class="meta"><h3>{name}</h3><span class="price">{pre_html}{price}</span></div>
        <p class="spec">{spec}</p>
        <div class="spec-chips">{chip_html}</div>
      </article>"""

    steps = [
        ("factory", "01", "Fabriek", "We werken met fabrieken die ook voor de grote merken maken. Zelfde materialen, zelfde naaiateliers, zonder merkopslag."),
        ("inspect", "02", "Inspectie &amp; labtest", "Elke partij wordt gewogen, gecontroleerd en door een onafhankelijk lab getest. Haalt hij de norm niet, dan verkopen we hem niet."),
        ("deliver", "03", "Naar jou vanuit Nederland", "Elke week komt er een drop binnen in ons magazijn in Nederland. Van daaruit bezorgen we bij jou thuis."),
    ]
    steps_html = ""
    for i, (k, n, t, d) in enumerate(steps):
        arrow = f'<span class="step-arrow">{icon("chevron")}</span>' if i < 2 else ""
        steps_html += f'<div class="step"><span class="num">{n}</span><div class="step-ill">{art.step_art(k)}</div><h3 class="h3">{t}</h3><p>{d}</p>{arrow}</div>'

    ok = icon("check")
    compare_rows = [
        ("Vulling", "95% ganzendons, 5% veertjes", "Dons en veren, percentage vaak niet vermeld"),
        ("Vulkracht", "750+ cuin, gemeten per partij", "Zelden vermeld"),
        ("Tijk", "100% Tencel lyocell batist, 300TC", "Katoen of polyester mix"),
        ("Certificaat", f'RDS nr. CU-XXXXXXX<br>{CHECK_ZELF}', "Logo, zonder nummer"),
    ]
    compare_html = "".join(f'<tr><td>{k}</td><td class="ours"><span class="ok">{ok}<span>{v}</span></span></td><td class="theirs">{t}</td></tr>' for k, v, t in compare_rows)

    videos = [("sort", "4:12", "Hoe dons gesorteerd wordt", "Van ruwe vulling naar 95% dons, in drie stappen."),
              ("inspect", "2:48", "Inspectie voor vertrek", "Wat we controleren voordat een partij de container in gaat."),
              ("joost", "3:05", "Waarom geen tussenhandel", "Waar het prijsverschil echt vandaan komt.")]
    video_html = "".join(f'<article class="video-card"><div class="media">{art.video_scene(k)}<span class="play">{icon("play")}</span><span class="duration">{d}</span></div>'
                         f'<h3>{t}</h3><p class="muted">{p}</p></article>' for k, d, t, p in videos)

    body = f"""{header()}
<main>
  <section class="hero">
    <div class="container">
      <div class="hero-top">
        <div>
          <span class="eyebrow">Rechtstreeks van de fabriek</span>
          <h1 class="display h1">Topkwaliteit rechtstreeks van de fabriek. <em>Zonder tussenhandel, met bewijs.</em></h1>
        </div>
        <div>
          <p class="lead">Dons, Tencel en zijde van de fabrieken die ook voor de grote merken maken. Wij laten zien wat erin zit.</p>
          <div class="cta-row">
            <a class="btn btn-primary" href="product.html">Bekijk de collectie {icon('arrow')}</a>
            <a class="btn btn-ghost" href="#zo-werken-wij">Zo werken wij</a>
          </div>
        </div>
      </div>
      <div class="media hero-media">
        <span class="tag pill"><span class="dot"></span>Labgetest · partij BL-D-2610</span>
        {art.bedroom()}
        <div class="float-card">
          <div class="fc-title"><b>Wat zit erin</b><span class="pill sage">Het Donsdekbed</span></div>
          <div class="row"><span>Vulling</span><span>95% ganzendons</span></div>
          <div class="row"><span>Vulkracht</span><span>750+ cuin</span></div>
          <div class="row"><span>Tijk</span><span>Tencel batist, 300TC</span></div>
          <div class="row"><span>RDS-certificaat</span>{CHECK_ZELF}</div>
        </div>
      </div>
      <div class="trust-row">{trust_html}</div>
    </div>
  </section>

  <section class="section" style="padding-top:72px">
    <div class="container">
      <div class="section-head">
        <div><span class="eyebrow">De collectie</span><h2 class="h2">Drie producten. Elk met de cijfers erbij.</h2></div>
        <p>We beginnen klein: alleen producten waarvan we de fabriek, de vulling en de testuitslag kennen.</p>
      </div>
      <div class="product-grid">{cards_html}
      </div>
    </div>
  </section>

  <section class="section bg-sand" id="zo-werken-wij">
    <div class="container">
      <div class="section-head">
        <div><span class="eyebrow">Zo werken wij</span><h2 class="h2">Van de fabriek naar jouw slaapkamer. Met één tussenstop: onze controle.</h2></div>
        <p>Geen groothandel, geen importeur, geen showroom. Wel een vaste fabriek, een onafhankelijk lab en een magazijn in Nederland.</p>
      </div>
      <div class="steps">{steps_html}</div>
      <div class="delivery-line">
        <span class="dl-ic">{icon('truck')}</span>
        <p><b>Op voorraad: 1-2 werkdagen.</b> Uit de wekelijkse drop: 7-10 werkdagen, je ziet de datum vooraf.</p>
        <div class="dl-tags"><span class="pill">Gratis verzending</span><span class="pill">Retour in Nederland</span></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container proof">
      <div>
        <span class="eyebrow">Ons bewijs</span>
        <h2 class="h2">Wat erin zit, staat erop. Tot op het certificaatnummer.</h2>
        <p class="lead">Veel dekbedden noemen "dons" zonder percentage en een keurmerk zonder nummer. Wij zetten de cijfers erbij, en de link om ze zelf te controleren.</p>
        <ul class="ticks">
          <li>{ok}Specificaties per product, niet per categorie</li>
          <li>{ok}Certificaatnummers die je zelf opzoekt</li>
          <li>{ok}Labrapport per partij, als PDF</li>
        </ul>
        <div class="cta-row">
          <a class="btn btn-primary" href="bewijs.html">Check zelf {icon('external')}</a>
          <a class="link-arrow" href="bewijs.html">Zo lees je specs {icon('arrow')}</a>
        </div>
      </div>
      <div class="spec-card">
        <div class="spec-card-head"><b>Het Donsdekbed</b><span class="pill"><span class="dot"></span>Partij BL-D-2610</span></div>
        <table class="compare">
          <thead><tr><th>Spec</th><th>Bline</th><th>Vaak in de winkel</th></tr></thead>
          <tbody>{compare_html}</tbody>
        </table>
        <div class="spec-card-foot">Vergeleken op basis van productlabels, zonder merknamen. Laatst bijgewerkt oktober 2026.</div>
      </div>
    </div>
  </section>

  <section class="section bg-ink">
    <div class="container">
      <div class="factory-head">
        <div>
          <span class="eyebrow">Van de fabriek</span>
          <h2 class="h2" style="margin-top:14px">Joost in de fabriek</h2>
          <p class="muted" style="margin:14px 0 0;max-width:560px">Geen stockbeelden. Korte video's uit de fabriek in Zhejiang, opgenomen tijdens ons bezoek. Zo zie je zelf waar je dekbed vandaan komt.</p>
        </div>
        <div class="joost">
          <span class="avatar">{art.avatar()}</span>
          <div><b style="color:#F7F4EF;font-weight:500">Joost</b><div class="muted small">Oprichter, filmt zelf</div></div>
          <a class="btn btn-light btn-sm" href="#" style="margin-left:16px">Alle video's</a>
        </div>
      </div>
      <div class="video-grid">{video_html}</div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="bundle">
        <div class="media">{art.bundle_scene()}</div>
        <div class="bundle-body">
          <span class="eyebrow">De Slaapset</span>
          <h2 class="h2">Dekbed, Tencel set en 2 kussens. In één keer goed.</h2>
          <p class="muted">Alles op elkaar afgestemd: dezelfde maat, dezelfde tijkkwaliteit. Als set iets voordeliger, je ziet het voordeel direct in je winkelwagen.</p>
          <ul class="bundle-list">
            <li><span>Het Donsdekbed · 4 seizoenen</span><span>vanaf €399</span></li>
            <li><span>Tencel beddengoed set</span><span>vanaf €159</span></li>
            <li><span>2 x Donskussen, 60 x 70</span><span>€89 per stuk</span></li>
          </ul>
          <div class="cta-row"><a class="btn btn-primary" href="product.html">Stel je set samen {icon('arrow')}</a><span class="muted small">Mee met de drop van donderdag</span></div>
        </div>
      </div>
    </div>
  </section>

  <section class="section bg-sand">
    <div class="container waitlist">
      <span class="eyebrow">De volgende drop</span>
      <h2 class="h2">Als eerste weten wanneer de nieuwe partij binnen is.</h2>
      <p class="muted">Eén mail per drop, met het labrapport erbij. Geen kortingsspam.</p>
      <div class="choice-row" style="margin-top:26px">
        <span class="choice on"><span class="box">{icon('check')}</span>Dekbedden</span>
        <span class="choice on"><span class="box">{icon('check')}</span>Beddengoed</span>
        <span class="choice"><span class="box"></span>Zijde</span>
      </div>
      <form class="form-inline" onsubmit="return false">
        <input class="input" type="email" placeholder="Je e-mailadres" aria-label="E-mailadres">
        <button class="btn btn-primary" type="submit">Zet me op de lijst</button>
      </form>
      <p class="small muted">Uitschrijven kan altijd. We delen je adres met niemand.</p>
    </div>
  </section>
</main>
{footer()}"""
    return page("Bline Sleep", body, "Premium dekbedden, beddengoed en zijde rechtstreeks van de fabriek.")


# ======================================================================= PRODUCT
def product():
    ok = icon("check")
    sizes = ["140 x 220", "200 x 220", "240 x 220", "260 x 220"]
    size_html = "".join(f'<span class="opt{" on" if s == "240 x 220" else ""}">{s}</span>' for s in sizes)
    weights = [("140 x 220", "300 + 450 g"), ("200 x 220", "430 + 640 g"), ("240 x 220", "520 + 770 g"), ("260 x 220", "560 + 840 g")]
    weights_html = "".join(f'<div class="{"on" if s == "240 x 220" else ""}"><b>{s}</b><span>{g}</span></div>' for s, g in weights)

    thumbs = [
        art.product_scene("duvet", ("#F2ECE2", "#DED2BE")),
        art.bedroom(),
        art.seam_detail(),
        art.hand_down(),
    ]
    thumbs_html = "".join(f'<div class="media{" active" if i == 0 else ""}">{t}</div>' for i, t in enumerate(thumbs))

    vs_rows = [
        ("Vulling", "95% ganzendons, 5% veertjes", "Vaak 60-90% dons, of alleen \"dons en veren\""),
        ("Vulkracht", "750+ cuin, gemeten per partij", "Meestal niet vermeld"),
        ("Tijk", "100% Tencel lyocell batist, 300TC", "Katoen percal of polyester mix"),
        ("Constructie", "Cassettes met tussenwanden", "Doorgestikte vakken, koudere naden"),
        ("Certificaat", "RDS en OEKO-TEX, met nummer", "Logo zonder controleerbaar nummer"),
        ("Labrapport", "Openbaar, per partij", "Niet openbaar"),
    ]
    dash = icon("dash")
    ours = "".join(f'<li><span class="k">{k}</span><span class="v">{ok}{a}</span></li>' for k, a, _ in vs_rows)
    theirs = "".join(f'<li><span class="k">{k}</span><span class="v">{dash}{b}</span></li>' for k, _, b in vs_rows)

    addons = [
        ("sheets", ("#EEF0EA", "#D7DDD0"), "Tencel beddengoed set", "240 x 220 · Ecru · overtrek + 2 slopen", "€189", True),
        ("pillow", ("#F2ECE2", "#E0D4C1"), "2 x Donskussen", "60 x 70 · medium · 90% dons", "€178", True),
        ("silk", ("#F4EEE6", "#E2D5C2"), "Zijden kussensloop", "60 x 70 · Champagne · 22 momme", "€59", False),
    ]
    addons_html = "".join(
        f'<div class="addon{" on" if on else ""}"><div class="media">{art.product_scene(k, bg, w=400, h=300)}</div>'
        f'<div class="addon-body"><div class="top"><b>{t}</b><span class="tick">{ok if on else ""}</span></div>'
        f'<span class="muted">{d}</span><span class="addon-price">{p}</span></div></div>' for k, bg, t, d, p, on in addons)

    faqs = [
        ("Hoe werkt 100 nachten proefslapen?",
         "Slaap minstens 30 nachten onder je dekbed, zodat je echt went aan een nieuw dekbed. Bevalt het niet? Meld hem binnen 100 nachten aan en stuur hem gratis terug naar ons adres in Nederland. Je krijgt het volledige bedrag terug.", True),
        ("Kan ik het dekbed wassen?", "Ja, op 40°C in een grote machine, of laat hem stomen bij een wasserette. Droog hem op laag vuur met een paar droogballen, zodat het dons weer luchtig wordt.", False),
        ("Wanneer wordt mijn bestelling bezorgd?", "Op voorraad: 1-2 werkdagen. Uit de wekelijkse drop: 7-10 werkdagen. Je ziet de verwachte datum altijd voordat je afrekent.", False),
        ("Hoe werkt retourneren?", "Je meldt je retour aan via je account. Je krijgt een gratis label en stuurt het pakket naar ons magazijn in Nederland. Binnen 5 werkdagen staat het geld terug.", False),
    ]
    faq_html = "".join(f'<details{" open" if o else ""}><summary>{q}<span class="pm">{icon("minus" if o else "plus")}</span></summary><p>{a}</p></details>' for q, a, o in faqs)

    body = f"""{header("Dekbedden", cart=0)}
<main>
  <div class="container">
    <nav class="breadcrumb" aria-label="Kruimelpad"><a href="index.html">Home</a><span class="sep">/</span><a href="#">Dekbedden</a><span class="sep">/</span><span class="here">Het Donsdekbed · 4 seizoenen</span></nav>
    <section class="pdp">
      <div class="gallery">
        <div class="media gallery-main"><span class="tag pill"><span class="dot"></span>Partij BL-D-2610 · labgetest</span>{art.product_scene("duvet-big", ("#F3EDE3", "#DBCEB9"), label="Het Donsdekbed, gevouwen", w=400, h=410)}</div>
        <div class="gallery-dots"><i class="on"></i><i></i><i></i><i></i></div>
        <div class="gallery-thumbs">{thumbs_html}</div>
      </div>
      <div class="buybox">
        <span class="eyebrow">Dekbedden</span>
        <h1>Het Donsdekbed · 4 seizoenen</h1>
        <p class="promise">Twee lagen die je met drukknopen samen of los gebruikt. Gevuld met 95% ganzendons, in een tijk van Tencel die ademt. Warm in januari, nooit klam.</p>
        <div class="rating-line"><span class="pill sage">Nieuw</span><span>Eerste partij, nog geen reviews. Wel een labrapport: <a class="check-link" href="#">bekijk PDF</a></span></div>
        <div class="price-row">
          <span class="price">€429</span><span class="price-sub">240 x 220 cm</span>
          <span class="price-note">Incl. btw, gratis verzending<br>100 nachten proefslapen</span>
        </div>
        <div class="opt-label"><span>Maat: <b>240 x 220 cm</b></span><a href="#">Welke maat past?</a></div>
        <div class="size-grid">{size_html}</div>
        <div class="opt-label"><span>Warmte: <b>4 seizoenen</b></span><a href="#">Verschil uitgelegd</a></div>
        <div class="warmth-grid">
          <div class="warmth"><span class="w-ic">{icon('sun')}</span><div><b>Zomer</b><span>Eén lichte laag, voor warme slapers</span></div></div>
          <div class="warmth on"><span class="w-ic">{icon('layers')}</span><div><b>4 seizoenen</b><span>Zomer + lente laag, met drukknopen</span></div></div>
        </div>
        <div class="delivery-box">
          <span class="d-ic">{icon('truck')}</span>
          <div>
            <p>Bestel vandaag, vertrekt <b>donderdag</b> met de drop, bij jou tussen <b>15 en 17 oktober</b>.</p>
            <div class="timeline">
              <div class="done"><b>Vandaag</b>Besteld</div>
              <div><b>Do 8 okt</b>Vertrek drop</div>
              <div><b>15-17 okt</b>Bij jou thuis</div>
            </div>
          </div>
        </div>
        <div class="atc-row">
          <div class="qty"><button aria-label="Minder">−</button><span>1</span><button aria-label="Meer">+</button></div>
          <a class="btn btn-primary" href="cart.html">In winkelwagen · €429</a>
        </div>
        <ul class="mini-trust">
          <li>{icon('moon')}100 nachten proefslapen</li>
          <li>{icon('return')}Gratis retour in Nederland</li>
          <li>{icon('shield')}Certificaten zelf te checken</li>
          <li>{icon('chat')}Service in het Nederlands</li>
        </ul>
      </div>
    </section>
  </div>

  <section class="section bg-sand">
    <div class="container inside">
      <aside class="inside-aside">
        <span class="eyebrow">Wat zit erin</span>
        <h2 class="h2">Elke spec, met bron.</h2>
        <p class="muted">Dit zit er in partij BL-D-2610. Bij een nieuwe partij werken we deze tabel bij, met een nieuw labrapport.</p>
        <div class="media">{art.hand_down()}</div>
      </aside>
      <div class="spec-card">
        <div class="spec-card-head"><b>Het Donsdekbed · partij BL-D-2610</b><span class="muted small">Bijgewerkt 1 okt 2026</span></div>
        <table class="spec-table">
          <tr><th>Vulling</th><td><span class="val">95% ganzendons, 5% veertjes</span><span class="note">Witte ganzendons, gewassen en gesorteerd in de fabriek. Geen eendendons bijgemengd.</span></td></tr>
          <tr><th>Vulkracht</th><td><span class="val">750+ cuin</span><span class="note">Gemeten volgens de IDFB-testmethode. Uitslag deze partij: 768 cuin.</span></td></tr>
          <tr><th>Vulgewicht per maat</th><td><div class="weights">{weights_html}</div><span class="note">Zomerlaag + lentelaag. Samen geknoopt is dit je winterdekbed.</span></td></tr>
          <tr><th>Tijk</th><td><span class="val">100% Tencel lyocell batist, 300TC</span><span class="note">Enkeldraads garen, downproof geweven. Zacht, stil en vochtregulerend.</span></td></tr>
          <tr><th>Constructie</th><td><span class="val">Cassettes met tussenwanden</span><span class="note">Tussenwanden van 4 cm houden het dons op zijn plek, zonder koude naden. Paspel rondom.</span></td></tr>
          <tr><th>Certificaten</th><td><div class="cert-row">
            <div class="cert"><span class="seal">RDS</span><div><b>Responsible Down Standard</b><code>Licentie CU-XXXXXXX</code></div>{CHECK_ZELF}</div>
            <div class="cert"><span class="seal">OEKO</span><div><b>OEKO-TEX Standard 100</b><code>Nr. 00.HXX.00000</code></div>{CHECK_ZELF}</div>
          </div></td></tr>
          <tr><th>Labtest</th><td><div class="lab-grid">
            <div><b>95,4%</b><span>Donspercentage</span></div>
            <div><b>768 cuin</b><span>Vulkracht</span></div>
            <div><b>Voldoet</b><span>Reinheid, EN 12935</span></div>
          </div><div class="links"><a class="check-link" href="#">{icon('doc')} Labrapport BL-D-2610 (PDF, 1,2 MB)</a><a class="check-link" href="bewijs.html">Alle partijen bekijken</a></div></td></tr>
          <tr><th>Herkomst</th><td><span class="val">Fabriek in Zhejiang, China</span><span class="note">Dezelfde fabriek maakt ook voor Europese merken. Wij bezochten haar in november 2026.</span><div class="links"><a class="check-link" href="#">{icon('play')} Bekijk de fabrieksvideo</a></div></td></tr>
        </table>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head">
        <div><span class="eyebrow">Waarom dit dekbed</span><h2 class="h2">Naast elkaar gelegd, alleen op specs.</h2></div>
        <p>Geen merknamen, geen mooie woorden. Alleen de regels die op een label horen te staan.</p>
      </div>
      <div class="vs">
        <div class="vs-col ours"><h3>Het Donsdekbed</h3><p class="sub">Bline · partij BL-D-2610</p><ul>{ours}</ul></div>
        <div class="vs-col theirs"><h3>Gemiddeld winkel-donsdekbed</h3><p class="sub">Wat we op productlabels in winkels tegenkomen</p><ul>{theirs}</ul></div>
      </div>
      <p class="disclaimer">Gebaseerd op specificaties die op productlabels van donsdekbedden in Nederlandse winkels staan vermeld. Je kunt elke regel aan onze kant zelf controleren.</p>
    </div>
  </section>

  <section class="section bg-sand">
    <div class="container">
      <div class="section-head">
        <div><span class="eyebrow">Maak het compleet</span><h2 class="h2">De Slaapset</h2></div>
        <p>Dekbed, Tencel set en kussens in dezelfde maat. Samen besteld net iets voordeliger.</p>
      </div>
      <div class="complete">
        {addons_html}
        <div class="set-summary">
          <span class="eyebrow">Jouw Slaapset</span>
          <h3>4 artikelen, 1 levering</h3>
          <div class="line"><span>Het Donsdekbed · 240 x 220</span><span>€429</span></div>
          <div class="line"><span>Tencel beddengoed set</span><span>€189</span></div>
          <div class="line"><span>2 x Donskussen</span><span>€178</span></div>
          <div class="line saving"><span>Slaapset voordeel</span><span>−€40</span></div>
          <div class="line total"><span>Totaal</span><span>€756</span></div>
          <p class="note">Het setvoordeel geldt als je dekbed, set en kussens samen bestelt.</p>
          <a class="btn btn-primary btn-block" href="cart.html">Set in winkelwagen</a>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container faq-wrap">
      <aside>
        <span class="eyebrow">Vragen</span>
        <h2 class="h2" style="margin-top:14px">Goed om te weten</h2>
        <div class="help-card"><span class="avatar">{art.avatar()}</span><div><b>Vraag het ons</b><span>Antwoord binnen een werkdag, in het Nederlands.</span></div></div>
      </aside>
      <div class="faq">{faq_html}</div>
    </div>
  </section>
</main>
{footer()}"""
    return page("Het Donsdekbed", body, "Het Donsdekbed 4 seizoenen: 95% ganzendons, 750+ cuin, Tencel tijk.")


# ======================================================================= BEWIJS
def bewijs():
    ok = icon("check")
    standards = [
        ("duvet", ("#F2ECE2", "#E0D4C1"), "Donsdekbed", [("Dons", "min. 95% ganzendons"), ("Vulkracht", "min. 750 cuin"), ("Tijk", "Tencel batist, 300TC"), ("Constructie", "Cassettes, tussenwanden"), ("Certificaten", "RDS · OEKO-TEX")],
         "Onder de norm? Dan gaat de partij terug naar de fabriek."),
        ("sheets", ("#EEF0EA", "#D7DDD0"), "Tencel beddengoed", [("Vezel", "100% Tencel lyocell"), ("Binding", "Satijn, 300TC"), ("Garen", "Enkeldraads"), ("Kleurvastheid", "min. 4 (ISO 105)"), ("Certificaat", "OEKO-TEX")],
         "Maximaal 3% krimp na drie wasbeurten, getest per partij."),
        ("silk", ("#F4EEE6", "#E2D5C2"), "Zijden kussensloop", [("Zijde", "100% moerbeizijde"), ("Gewicht", "22 momme"), ("Kwaliteit", "Grade 6A"), ("Sluiting", "Verborgen rits"), ("Certificaat", "OEKO-TEX")],
         "Gewicht per partij gewogen, tolerantie 0,5 momme."),
    ]
    std_html = ""
    for k, bg, t, rows, mn in standards:
        li = "".join(f'<li><span>{a}</span><span>{b}</span></li>' for a, b in rows)
        std_html += (f'<article class="standard"><div class="media">{art.product_scene(k, bg, w=400, h=225)}</div><div class="standard-body">'
                     f'<h3>{t}</h3><ul class="std-list">{li}</ul><p class="std-min">{ok}{mn}</p></div></article>')

    dots = "".join('<i class="f"></i>' if i in (19, 38, 57, 76, 95) else "<i></i>" for i in range(100))

    lab_rows = [
        ("BL-D-2611", "2 okt 2026", "4 seizoenen, 240 x 220", "Volgt", "Volgt", "Volgt", "pending", "In het lab", False),
        ("BL-D-2610", "29 sep 2026", "4 seizoenen, alle maten", "95,4%", "768 cuin", "Voldoet", "pass", "Goedgekeurd", True),
        ("BL-D-2609", "15 sep 2026", "Zomer, alle maten", "95,1%", "762 cuin", "Voldoet", "pass", "Goedgekeurd", True),
        ("BL-D-2608B", "1 sep 2026", "4 seizoenen, 200 x 220", '<span style="color:var(--danger)">92,8%</span>', '<span style="color:var(--danger)">731 cuin</span>', "Voldoet", "fail", "Afgekeurd, terug naar fabriek", True),
        ("BL-D-2608", "18 aug 2026", "4 seizoenen, alle maten", "95,6%", "771 cuin", "Voldoet", "pass", "Goedgekeurd", True),
    ]
    lab_html = ""
    for b, d, p, dp, vk, r, st, stt, pdf in lab_rows:
        cls = ' class="rejected"' if st == "fail" else ""
        link = f'<a class="check-link" href="#">{icon("download")} PDF</a>' if pdf else '<span class="muted small">Volgt</span>'
        lab_html += (f'<tr{cls}><td class="batch">{b}</td><td class="num">{d}</td><td>{p}</td><td class="num res">{dp}</td>'
                     f'<td class="num res">{vk}</td><td>{r}</td><td><span class="status {st}"><i></i>{stt}</span></td><td>{link}</td></tr>')

    strip = [
        (art.factory_floor(), "Naaien", "Het naaiatelier in Zhejiang"),
        (art.scale_scene(), "Wegen", "Vulgewicht per cassette"),
        (art.seam_detail(), "Stikken", "Tussenwanden van 4 cm"),
        (art.lab_scene(), "Testen", "Steekproef per partij"),
        (art.boxes_scene(), "Nederland", "Klaar voor verzending"),
    ]
    strip_html = "".join(f'<figure><div class="media">{s}</div><figcaption><b>{a}</b>{c}</figcaption></figure>' for s, a, c in strip)

    minis = [("Thread count (TC)", "Het aantal draden per vierkante inch. 300TC in enkeldraads garen is fijner dan 600TC met dubbele draden, ook al klinkt het lager."),
             ("Momme", "De zwaarte van zijde. 19 momme is licht, 22 momme is dichter, gladder en gaat langer mee."),
             ("Downproof", "Zo strak geweven dat dons er niet doorheen prikt. Zonder coating, dus de tijk blijft ademen.")]
    minis_html = "".join(f'<div class="explain" style="padding:28px 30px"><span class="eyebrow plain">Begrip</span><h3 style="font-size:26px">{t}</h3><p style="margin:0">{d}</p></div>' for t, d in minis)

    body = f"""{header("Ons bewijs")}
<main>
  <section class="page-hero">
    <div class="container page-hero-grid">
      <div>
        <span class="eyebrow">Ons bewijs</span>
        <h1 class="display">Wat erin zit, staat erop. <em class="accent">En je kunt het checken.</em></h1>
        <p class="lead">Premium is geen gevoel. Het is een vulpercentage, een vulkracht, een garen en een certificaatnummer. Hier lees je welke norm wij hanteren, hoe je specs leest en hoe je onze claims zelf controleert.</p>
        <nav class="anchor-nav"><a href="#standaard">Onze standaard</a><a href="#lezen">Specs lezen</a><a href="#checken">Certificaat checken</a><a href="#labtests">Labtests per partij</a><a href="#fabriek">De fabriek</a></nav>
      </div>
      <div class="media">{art.lab_report_scene()}</div>
    </div>
  </section>

  <section class="section" id="standaard" style="padding-top:40px">
    <div class="container">
      <div class="section-head">
        <div><span class="eyebrow">Onze standaard</span><h2 class="h2">De lat per product. Op papier, en in het lab.</h2></div>
        <p>Dit zijn de minimale specs die een partij moet halen voordat we hem verkopen. Haalt hij ze niet, dan gaat hij terug.</p>
      </div>
      <div class="standard-grid">{std_html}</div>
    </div>
  </section>

  <section class="section bg-sand" id="lezen">
    <div class="container">
      <div class="section-head">
        <div><span class="eyebrow">Zo lees je de specs</span><h2 class="h2">Twee getallen die het verschil maken.</h2></div>
        <p>Vulkracht en donspercentage zeggen meer over een dekbed dan elk mooi woord. Zo lees je ze, bij ons en bij anderen.</p>
      </div>
      <div class="explain-grid">
        <div class="explain">
          <span class="eyebrow plain">Vulkracht · cuin</span>
          <h3>Hoe luchtig is het dons?</h3>
          <p>Vulkracht meet hoeveel ruimte 1 ounce dons inneemt, in kubieke inch. Hoe hoger, hoe groter de donsbolletjes: meer warmte bij minder gewicht, en een dekbed dat jaren luchtig blijft.</p>
          <div class="scale">
            <div class="scale-marker" style="left:67%"><span>Deze partij: 768</span></div>
            <div class="scale-bar"></div>
            <div style="position:relative;height:44px;margin-top:10px;font-size:12px;color:var(--muted)">
              <div style="position:absolute;left:12.5%;transform:translateX(-50%);text-align:center"><b style="display:block;color:var(--ink);font-size:13px">550</b>Basis</div>
              <div style="position:absolute;left:37.5%;transform:translateX(-50%);text-align:center"><b style="display:block;color:var(--ink);font-size:13px">650</b>Goed</div>
              <div style="position:absolute;left:62.5%;transform:translateX(-50%);text-align:center"><b style="display:block;color:var(--sage-dark);font-size:13px">750</b>Onze norm</div>
              <div style="position:absolute;left:87.5%;transform:translateX(-50%);text-align:center"><b style="display:block;color:var(--ink);font-size:13px">850</b>Expeditie</div>
            </div>
          </div>
          <div class="callout">Een vulkracht zegt pas iets als de meetmethode erbij staat. Europese en Amerikaanse methodes geven andere uitkomsten. Wij meten volgens de Europese IDFB-methode.</div>
        </div>
        <div class="explain">
          <span class="eyebrow plain">Donspercentage</span>
          <h3>Hoeveel is echt dons?</h3>
          <p>"Dons" op een label kan van alles betekenen. Het percentage vertelt hoeveel echte donsbolletjes erin zitten. De rest zijn veertjes met een schacht: zwaarder, minder warm en ze kunnen prikken.</p>
          <div class="dot-grid">{dots}</div>
          <div class="legend"><span><i></i>95 delen dons</span><span><i class="f"></i>5 delen kleine veertjes</span></div>
          <div class="callout">Staat er alleen "dons" of "dons en veren" zonder percentage? Vraag ernaar. Wij leggen de lat op minimaal 95%.</div>
        </div>
      </div>
      <div class="standard-grid" style="margin-top:24px">{minis_html}</div>
    </div>
  </section>

  <section class="section" id="checken">
    <div class="container cert-steps">
      <div>
        <span class="eyebrow">Certificaat checken</span>
        <h2 class="h2" style="margin:14px 0 18px">Controleer ons in drie minuten.</h2>
        <p class="muted">Een keurmerklogo kan iedereen plaatsen. Een nummer dat klopt in de database van de uitgever niet. Zo check je het zelf.</p>
        <ol class="num-steps" style="padding:0;margin:28px 0 0;list-style:none">
          <li><span class="n">1</span><div><b>Kopieer het nummer</b><p>Elk certificaatnummer staat op de productpagina en op het label in je dekbed.</p></div></li>
          <li><span class="n">2</span><div><b>Open de database van de uitgever</b><p>Voor RDS is dat de certificaatdatabase van Textile Exchange, voor OEKO-TEX de Label Check op hun eigen site.</p></div></li>
          <li><span class="n">3</span><div><b>Vergelijk houder, product en geldigheid</b><p>Staat onze fabriek erbij, klopt de productgroep en is het certificaat nog geldig? Dan klopt onze claim.</p></div></li>
        </ol>
      </div>
      <div class="browser">
        <div class="browser-bar"><i></i><i></i><i></i><span class="url">{icon('lock').replace('<svg', '<svg style="width:12px;height:12px;margin-right:6px"')} certificaatdatabase van de uitgever</span></div>
        <div class="browser-body">
          <div class="field-label">Certificaat- of licentienummer</div>
          <div class="fake-input">{icon('search').replace('<svg', '<svg style="width:16px;height:16px;color:#9AA0A8"')}CU-XXXXXXX<span class="caret"></span></div>
          <div class="result">
            <div class="r-head">{icon('shield')} Geldig certificaat gevonden</div>
            <dl>
              <dt>Standaard</dt><dd>Responsible Down Standard</dd>
              <dt>Houder</dt><dd>[Fabrieksnaam] Home Textile Co., Ltd.</dd>
              <dt>Locatie</dt><dd>Zhejiang, China</dd>
              <dt>Producten</dt><dd>Dekbedden, kussens</dd>
              <dt>Geldig tot</dt><dd>30-09-2027</dd>
            </dl>
          </div>
          <p class="small muted" style="margin:16px 0 0">Klopt er iets niet? Mail ons op hallo@blinesleep.nl. We reageren binnen een werkdag.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section bg-sand" id="labtests">
    <div class="container">
      <div class="section-head">
        <div><span class="eyebrow">Labtests per partij</span><h2 class="h2">Elke partij getest. Ook de partijen die we niet verkopen.</h2></div>
        <p>Een onafhankelijk textiellab test een steekproef uit elke partij voordat die de fabriek verlaat. De uitslag staat hier, met het volledige rapport.</p>
      </div>
      <div class="table-card">
        <div class="table-tools">
          <div class="tabs"><span class="on">Dekbedden</span><span>Beddengoed</span><span>Zijde</span></div>
          <a class="link-arrow" href="#">{icon('download')} Alle rapporten</a>
        </div>
        <table class="lab-table">
          <thead><tr><th>Partij</th><th>Getest op</th><th>Product</th><th>Dons<br><span style="text-transform:none;letter-spacing:0">norm ≥ 95%</span></th><th>Vulkracht<br><span style="text-transform:none;letter-spacing:0">norm ≥ 750 cuin</span></th><th>Reinheid<br><span style="text-transform:none;letter-spacing:0">EN 12935</span></th><th>Status</th><th>Rapport</th></tr></thead>
          <tbody>{lab_html}</tbody>
        </table>
        <div class="table-foot"><span>Lab: onafhankelijk en ISO 17025-geaccrediteerd. Steekproef: 3 stuks per partij.</span><span>Testmethodes: EN 12934, EN 12935, IDFB</span></div>
      </div>
    </div>
  </section>

  <section class="section" id="fabriek">
    <div class="container">
      <div class="story">
        <div>
          <span class="eyebrow">De fabriek</span>
          <h2 class="h2" style="margin:14px 0 18px">Wij gingen kijken. En we gaan elk jaar terug.</h2>
          <p class="lead">In november 2026 bezocht Joost de fabriek in Zhejiang waar ons dekbed wordt gemaakt. Een familiebedrijf dat al jaren produceert voor Europese merken.</p>
          <p class="muted">We zagen hoe dons wordt gewassen en gesorteerd, hoe de tijk wordt geweven en hoe elke cassette wordt gevuld en gewogen. Alles wat we zagen, filmden we. Je vindt het bij Van de fabriek.</p>
        </div>
        <div>
          <blockquote>"We willen niet dat je ons op ons woord gelooft. Daarom laten we de fabriek, de cijfers en de rapporten zien."</blockquote>
          <cite><span class="avatar">{art.avatar()}</span><span><b style="color:var(--ink);font-weight:600">Joost</b><br>Oprichter Bline Sleep</span></cite>
        </div>
      </div>
      <div class="photo-strip">{strip_html}</div>
    </div>
  </section>
</main>
{footer()}"""
    return page("Ons bewijs", body, "Hoe Bline Sleep specs, certificaten en labtests openbaar maakt.")


# ======================================================================= CART
def cart():
    items = [
        ("duvet", ("#F2ECE2", "#E0D4C1"), "Het Donsdekbed · 4 seizoenen", "240 x 220 cm · 95% ganzendons · 750+ cuin", "drop", "Met de drop van donderdag · 15-17 oktober", "€429", ""),
        ("sheets", ("#EEF0EA", "#D7DDD0"), "Tencel beddengoed set", "240 x 220 cm · Ecru · overtrek + 2 slopen 60 x 70", "drop", "Met de drop van donderdag · 15-17 oktober", "€189", ""),
        ("silk", ("#F4EEE6", "#E2D5C2"), "Zijden kussensloop", "60 x 70 cm · Champagne · 22 momme", "stock", "Op voorraad · 1-2 werkdagen", "€59", ""),
    ]
    items_html = ""
    for k, bg, t, v, sk, st, p, _ in items:
        ic = icon("box") if sk == "stock" else icon("calendar")
        items_html += f"""
        <div class="cart-item">
          <div class="media">{art.product_scene(k, bg, w=264, h=300)}</div>
          <div>
            <div class="ci-title">{t}</div>
            <div class="ci-variant">{v}</div>
            <span class="ci-ship {sk}">{ic}{st}</span>
            <div class="ci-actions"><div class="qty"><button aria-label="Minder">−</button><span>1</span><button aria-label="Meer">+</button></div><a href="#">Verwijderen</a><a href="#">Bewaren</a></div>
          </div>
          <div class="ci-price">{p}</div>
        </div>"""

    body = f"""{header(cart=3)}
<main>
  <div class="container">
    <div class="cart-head">
      <div><span class="eyebrow">Winkelwagen</span><h1 style="margin-top:12px">Je winkelwagen</h1></div>
      <div class="checkout-steps"><span class="on"><span class="n">1</span>Winkelwagen</span><span class="bar"></span><span><span class="n">2</span>Gegevens</span><span class="bar"></span><span><span class="n">3</span>Betalen</span></div>
    </div>
    <section class="cart">
      <div>
        <div class="cart-items">{items_html}</div>
        <div class="split">
          <div class="split-head"><b>Zo wordt je bestelling bezorgd</b><span class="pill sage">2 zendingen, geen extra kosten</span></div>
          <div class="split-rows">
            <div class="split-row stock"><span class="s-ic">{icon('box')}</span><div><b>Zijden sloop</b><span>Op voorraad, 1-2 werkdagen</span><div class="when">Bij jou op di 6 of wo 7 oktober</div></div></div>
            <div class="split-row drop"><span class="s-ic">{icon('truck')}</span><div><b>Dekbed en set</b><span>Met de drop van donderdag</span><div class="when">Bij jou tussen 15 en 17 oktober</div></div></div>
          </div>
          <div class="split-note"><span>Liever alles in één keer? Dan gaat de sloop mee met de drop.</span><span class="toggle" role="switch" aria-checked="false"></span></div>
        </div>
      </div>
      <aside class="summary">
        <h2>Overzicht</h2>
        <div class="sum-line"><span>Subtotaal (3 artikelen)</span><span>€677</span></div>
        <div class="sum-line saving"><span>Slaapset voordeel<small>Dekbed en Tencel set samen</small></span><span>−€30</span></div>
        <div class="sum-line"><span>Verzending</span><span>Gratis</span></div>
        <div class="callout" style="margin:10px 0 4px;font-size:13px">Zijden sloop: op voorraad, 1-2 werkdagen · Dekbed en set: met de drop van donderdag, 15-17 oktober</div>
        <div class="sum-total"><span>Totaal</span><div><b>€647</b><small>Incl. €112,29 btw</small></div></div>
        <div class="code-row"><input class="input" placeholder="Kortingscode" aria-label="Kortingscode"><button class="btn btn-ghost btn-sm">Toepassen</button></div>
        <a class="btn btn-primary btn-block" href="#">{icon('lock')} Veilig afrekenen</a>
        {pay_badges()}
        <ul class="summary-trust">
          <li>{icon('moon')}100 nachten proefslapen op je dekbed</li>
          <li>{icon('return')}Gratis retour naar een adres in Nederland</li>
          <li>{icon('chat')}Vragen? Klantenservice in het Nederlands</li>
        </ul>
      </aside>
    </section>
  </div>
</main>
{footer()}"""
    return page("Winkelwagen", body, "Winkelwagen Bline Sleep")


if __name__ == "__main__":
    for name, fn in [("index.html", home), ("product.html", product), ("bewijs.html", bewijs), ("cart.html", cart)]:
        (OUT / name).write_text(fn(), encoding="utf-8")
        print("wrote", name)
