(() => {
  const r = (sel) => { const e = document.querySelector(sel); if (!e) return null; const b = e.getBoundingClientRect(); const cs = getComputedStyle(e);
    return { top: Math.round(b.top + scrollY), h: Math.round(b.height), w: Math.round(b.width), font: cs.fontSize, weight: cs.fontWeight, color: cs.color, radius: cs.borderRadius, ls: cs.letterSpacing, lh: cs.lineHeight, tekst: (e.innerText || '').trim().slice(0, 80) }; };
  const out = {
    balk: r('.announcement-bar__message'), header: r('.header-wrapper'), menu_desktop: r('.header__inline-menu'), hamburger: r('header-drawer summary'),
    titel: r('.product__title h1'), ondertitel: r('.bline-ondertitel'), prijs: r('.product__info-container .price-item--regular'), btw: r('.product__tax'),
    kleurlabel: r('.bline-kleurkeuze__label, .product-form__input--pill legend, .product-form__input legend'), knop: r('.product-form__submit'), vinkjes: r('.product__info-container .bline-vinkjes'),
    bundelregel: r('.bline-bundelregel'), betaal: r('.bline-betaal'), foto: r('.product__media-item img, .product__media img'), uitklap_tekst: r('.bline-uitklap .accordion__content'),
    kruimel: r('.bline-kruimel'), reviews: r('.bline-reviews'), hero_kop: r('.banner__heading'), hero_knop: r('.banner__buttons .button'),
    kleurvlak: r('.bline-kleurvlak.is-gekozen'), kleurvlak_niet: r('.bline-kleurvlak:not(.is-gekozen)'), kleurvlak_rand: (() => { const e = document.querySelector('.bline-kleurvlak.is-gekozen'); return e ? getComputedStyle(e).borderTopWidth + ' + ' + getComputedStyle(e).boxShadow : null; })(),
    sticky: r('[data-bline-sticky]'), score: r('.bline-score'), kaarten: [...document.querySelectorAll('.product-grid .grid__item, .collection .grid__item')].slice(0, 6).map((e) => { const b = e.getBoundingClientRect(); return Math.round(b.left) + ',' + Math.round(b.top + scrollY) + ' ' + Math.round(b.width) + 'x' + Math.round(b.height); }),
  };
  const secs = [...document.querySelectorAll('main .shopify-section')].map((s) => { const cs = getComputedStyle(s.firstElementChild || s); const inner = s.querySelector('[class*="section-template"][class*="padding"], .section-padding, [class*="-padding"]'); const ic = inner ? getComputedStyle(inner) : null; return { id: s.id.replace('shopify-section-', ''), h: Math.round(s.getBoundingClientRect().height), pt: ic && ic.paddingTop, pb: ic && ic.paddingBottom, mt: getComputedStyle(s).marginTop }; });
  out.secties = secs;
  const klein = [...document.querySelectorAll('main *')].filter((e) => e.childNodes.length && [...e.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim()) && e.offsetParent && parseFloat(getComputedStyle(e).fontSize) < 16).map((e) => e.tagName + '.' + e.className + ' ' + getComputedStyle(e).fontSize + ' ' + e.textContent.trim().slice(0, 30));
  out.tekst_onder_16px = klein.slice(0, 30);
  out.zwevend = [...document.querySelectorAll('body *')].filter((e) => ['fixed', 'sticky'].includes(getComputedStyle(e).position) && e.offsetParent !== undefined && e.getBoundingClientRect().height > 0).map((e) => e.tagName + '.' + (e.className.baseVal !== undefined ? '' : e.className)).slice(0, 20);
  out.pagina_hoogte = document.documentElement.scrollHeight;
  return out;
})()
