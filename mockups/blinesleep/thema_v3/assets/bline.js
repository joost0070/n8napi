/* Bline: beelden per kleur en meelopende knop */
(function () {
  var KLEUREN = ['wit', 'beige', 'blauw', 'grijs', 'zwart'];

  function gekozenKleur() {
    var el = document.querySelector('variant-selects input[data-option-name="Kleur"]:checked, variant-selects select[data-option-name="Kleur"]');
    if (!el) {
      var sel = document.querySelector('variant-selects select');
      el = sel || null;
    }
    return el ? String(el.value).toLowerCase() : null;
  }

  function kleurVanAlt(alt) {
    var m = String(alt || '').toLowerCase().match(/kleur (wit|beige|blauw|grijs|zwart)/);
    return m ? m[1] : null;
  }

  function filterBeelden() {
    var kleur = gekozenKleur();
    if (!kleur || KLEUREN.indexOf(kleur) === -1) return;
    var items = document.querySelectorAll('.product__media-item, .thumbnail-list__item');
    var veranderd = false;
    items.forEach(function (item) {
      var img = item.querySelector('img');
      if (!img) return;
      var k = kleurVanAlt(img.getAttribute('alt'));
      var verbergen = k !== null && k !== kleur;
      if (item.classList.contains('bline-media-verborgen') !== verbergen) {
        item.classList.toggle('bline-media-verborgen', verbergen);
        veranderd = true;
      }
    });
    if (!veranderd) return;
    // Teller van de veegslider (mobiel) opnieuw tellen, alleen zichtbare beelden
    document.querySelectorAll('media-gallery slider-component').forEach(function (s) {
      if (typeof s.resetPages !== 'function') return;
      if (s.slider) s.slider.scrollLeft = 0;
      s.resetPages();
    });
  }

  function init() {
    filterBeelden();
    document.addEventListener('change', function (e) {
      if (e.target.closest && e.target.closest('variant-selects')) setTimeout(filterBeelden, 0);
    });
    var hoofd = document.querySelector('[id^="MainProduct-"]') || document.querySelector('main');
    if (hoofd && 'MutationObserver' in window) {
      new MutationObserver(function () { filterBeelden(); }).observe(hoofd, { childList: true, subtree: true });
    }
    stickyKnop();
  }

  function stickyKnop() {
    var balk = document.querySelector('[data-bline-sticky]');
    if (!balk) return;
    var knop = balk.querySelector('button');
    var prijs = balk.querySelector('[data-bline-sticky-prijs]');
    function hoofdknop() { return document.querySelector('product-form [name="add"]'); }
    function prijsBijwerken() {
      var p = document.querySelector('[id^="price-"] .price-item--last, [id^="price-"] .price-item--regular');
      if (p && prijs) prijs.textContent = p.textContent.trim();
      var h = hoofdknop();
      if (h && knop) {
        knop.disabled = h.disabled;
        var span = h.querySelector('span');
        if (span) knop.textContent = span.textContent.trim();
      }
    }
    knop.addEventListener('click', function () {
      var h = hoofdknop();
      if (h && !h.disabled) h.click();
    });
    var h = hoofdknop();
    if (!h || !('IntersectionObserver' in window)) return;
    new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        var onder = en.boundingClientRect.top < 0;
        // Op mobiel ook tonen als de hoofdknop nog onder de vouw staat
        var mobiel = window.matchMedia('(max-width: 749px)').matches;
        var zichtbaar = !en.isIntersecting && (onder || mobiel);
        balk.classList.toggle('is-zichtbaar', zichtbaar);
        balk.setAttribute('aria-hidden', zichtbaar ? 'false' : 'true');
        balk.inert = !zichtbaar;
        if (zichtbaar) prijsBijwerken();
      });
    }).observe(h);
    document.addEventListener('change', function () { setTimeout(prijsBijwerken, 400); });
    prijsBijwerken();
  }

  // "Kleur: Wit": de gekozen kleur in het label meteen bijwerken (Shopify ververst het daarna ook zelf)
  function kleurLabel(e) {
    var input = e.target;
    if (!input || input.type !== 'radio' || !input.closest('variant-selects')) return;
    var set = input.closest('fieldset');
    var label = set && set.querySelector('[data-selected-value]');
    if (label) label.textContent = input.value;
  }

  // Upsell in de lade: losse hoes toevoegen, daarna de lade opnieuw tonen
  function upsell(e) {
    var knop = e.target.closest && e.target.closest('[data-bline-upsell]');
    if (!knop) return;
    e.preventDefault();
    knop.setAttribute('aria-busy', 'true');
    var lade = document.querySelector('cart-drawer');
    var secties = lade && typeof lade.getSectionsToRender === 'function'
      ? lade.getSectionsToRender().map(function (s) { return s.id; }) : ['cart-drawer', 'cart-icon-bubble'];
    fetch((window.routes && window.routes.cart_add_url ? window.routes.cart_add_url : '/cart/add') + '.js', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
      body: JSON.stringify({ items: [{ id: Number(knop.getAttribute('data-bline-upsell')), quantity: 1 }], sections: secties, sections_url: window.location.pathname })
    })
      .then(function (r) { return r.json(); })
      .then(function (state) {
        if (state && state.sections && lade && typeof lade.renderContents === 'function') lade.renderContents(state);
        else window.location.href = '/cart';
      })
      .catch(function () { window.location.href = '/cart'; });
  }

  document.addEventListener('change', kleurLabel);
  // Kleurbolletjes in de upsell: andere hoes kiezen voordat je toevoegt
  function upsellKleur(e) {
    var bol = e.target.closest && e.target.closest('[data-up-kleur]');
    if (!bol) return;
    var kaart = bol.closest('[data-up-kaart]');
    if (!kaart) return;
    [].forEach.call(kaart.querySelectorAll('[data-up-kleur]'), function (b) {
      var aan = b === bol;
      b.classList.toggle('is-gekozen', aan);
      b.setAttribute('aria-checked', aan ? 'true' : 'false');
    });
    var foto = kaart.querySelector('.bline-upsell__foto img');
    if (foto) { foto.src = bol.getAttribute('data-up-beeld'); foto.removeAttribute('srcset'); }
    var naam = kaart.querySelector('[data-up-naam]');
    if (naam) naam.textContent = bol.getAttribute('data-up-naamtekst');
    [].forEach.call(kaart.querySelectorAll('[data-up-link]'), function (a) { a.href = bol.getAttribute('data-up-url'); });
    var was = kaart.querySelector('[data-up-was]'); if (was) was.textContent = bol.getAttribute('data-up-was');
    var prijs = kaart.querySelector('[data-up-prijs]'); if (prijs) prijs.textContent = bol.getAttribute('data-up-prijstekst');
    var knop = kaart.querySelector('[data-bline-upsell]');
    if (knop) {
      knop.setAttribute('data-bline-upsell', bol.getAttribute('data-up-kleur'));
      knop.setAttribute('aria-label', bol.getAttribute('data-up-naamtekst') + ' toevoegen voor ' + bol.getAttribute('data-up-prijstekst'));
    }
  }

  document.addEventListener('click', upsellKleur);
  document.addEventListener('click', upsell);

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
