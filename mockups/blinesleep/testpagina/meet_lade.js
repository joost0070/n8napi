(() => {
  const r = (sel) => { const e = document.querySelector(sel); if (!e) return null; const b = e.getBoundingClientRect(); const cs = getComputedStyle(e); return { top: Math.round(b.top), h: Math.round(b.height), w: Math.round(b.width), font: cs.fontSize, tekst: (e.innerText || '').trim().slice(0, 120) }; };
  return { lade: r('cart-drawer .drawer__inner'), afrekenen: r('cart-drawer #CartDrawer-Checkout'), totaal: r('cart-drawer .totals__total-value'), optie: r('cart-drawer .product-option'), upsell: r('cart-drawer .bline-upsell'), upsell_knop: r('cart-drawer .bline-upsell button'), korting: r('cart-drawer .discounts') };
})()
