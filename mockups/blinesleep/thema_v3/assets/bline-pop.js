/* Bline aanmeldpop-up: meldt aan bij Klaviyo (enkele aanmelding) en start zo de welkomstflow met de 10%-code. */
(function () {
  'use strict';
  var pop = document.querySelector('[data-b3-pop]');
  if (!pop) return;
  var SLEUTEL = 'bline_pop';
  var DAGEN_NA_SLUITEN = 14;

  function lees() { try { return JSON.parse(localStorage.getItem(SLEUTEL) || '{}'); } catch (e) { return {}; } }
  function bewaar(v) { try { localStorage.setItem(SLEUTEL, JSON.stringify(v)); } catch (e) {} }
  function meet(naam, data) {
    try { if (window.Shopify && Shopify.analytics && Shopify.analytics.publish) Shopify.analytics.publish(naam, data || {}); } catch (e) {}
  }

  var staat = lees();
  if (staat.aangemeld) return;
  var recent = function (t) { return t && Date.now() - t < DAGEN_NA_SLUITEN * 864e5; };
  // pop-up niet vanzelf na wegklikken; de teaser blijft dan wel, tenzij die zelf is weggeklikt
  var popMag = !recent(staat.dicht);
  var teaserMag = !recent(staat.teaserDicht);
  if (!popMag && !teaserMag) return;
  // wie uit een Bline-mail komt, staat al op de lijst
  if (/[?&]utm_source=klaviyo/i.test(location.search) || /[?&]_kx=/.test(location.search)) return;

  var teaser = document.querySelector('[data-b3-teaser]');
  function teaserToon() {
    if (!teaser || !teaserMag || open) return;
    teaser.hidden = false;
    requestAnimationFrame(function () { teaser.classList.add('is-zichtbaar'); });
  }
  function teaserWeg() {
    if (!teaser) return;
    teaser.classList.remove('is-zichtbaar');
    setTimeout(function () { if (!teaser.classList.contains('is-zichtbaar')) teaser.hidden = true; }, 250);
  }
  if (teaser) {
    teaser.querySelector('[data-b3-teaser-open]').addEventListener('click', function () { toon('teaser'); });
    teaser.querySelector('[data-b3-teaser-x]').addEventListener('click', function () {
      teaserMag = false; teaserWeg();
      var s2 = lees(); s2.teaserDicht = Date.now(); bewaar(s2);
    });
  }

  var vorigeFocus = null, open = false;
  function toon(bron) {
    if (open || document.querySelector('cart-drawer.active, .drawer.active')) return;
    open = true; vorigeFocus = document.activeElement;
    teaserWeg();
    pop.hidden = false;
    requestAnimationFrame(function () { pop.classList.add('is-open'); });
    document.documentElement.classList.add('b3-pop-open');
    if (pop.classList.contains('b3-pop--compact')) document.documentElement.classList.add('b3-pop-compact-open');
    var veld = pop.querySelector('#b3-pop-mail');
    if (veld && window.matchMedia('(min-width: 750px)').matches) setTimeout(function () { veld.focus(); }, 250);
    else { var x = pop.querySelector('.b3-pop__x'); if (x) x.focus(); }
    meet('bline_pop_getoond', { bron: bron });
    stopWachten();
  }
  function sluit() {
    if (!open) return;
    open = false;
    pop.classList.remove('is-open');
    document.documentElement.classList.remove('b3-pop-open', 'b3-pop-compact-open');
    setTimeout(function () { pop.hidden = true; }, 250);
    var s = lees(); if (!s.aangemeld) { s.dicht = Date.now(); bewaar(s); }
    popMag = false;
    if (!s.aangemeld) setTimeout(teaserToon, 400);
    if (vorigeFocus && vorigeFocus.focus) vorigeFocus.focus();
  }
  pop.querySelectorAll('[data-b3-pop-dicht]').forEach(function (b) { b.addEventListener('click', sluit); });
  pop.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') { sluit(); return; }
    if (e.key !== 'Tab') return;
    // focus binnen de pop-up houden
    var f = [].filter.call(pop.querySelectorAll('button, input, a[href]'), function (el) { return el.offsetParent !== null; });
    if (!f.length) return;
    var eerste = f[0], laatste = f[f.length - 1];
    if (e.shiftKey && document.activeElement === eerste) { e.preventDefault(); laatste.focus(); }
    else if (!e.shiftKey && document.activeElement === laatste) { e.preventDefault(); eerste.focus(); }
  });

  /* Wanneer: pas na een cookiekeuze, nooit tegelijk met de cookiebanner.
     Desktop: bij verlaten van de pagina; op andere pagina's dan een productpagina ook na 12 s.
     Mobiel: niet op de eerste pagina van een bezoek; vanaf de tweede pagina na 10 s, als compacte balk onderin.
     Nooit als er al iets in de winkelwagen ligt of iemand net een product toevoegt. */
  var desktop = window.matchMedia('(min-width: 750px)').matches;
  var opProduct = pop.getAttribute('data-template') === 'product';
  var paginas = 1;
  try { paginas = (parseInt(sessionStorage.getItem('bline_pv') || '0', 10) || 0) + 1; sessionStorage.setItem('bline_pv', String(paginas)); } catch (e) {}
  if (!desktop) pop.classList.add('b3-pop--compact');

  var timer = null, gestopt = false;
  function opVerlaten(e) { if (!e.relatedTarget && e.clientY <= 0) toon('verlaten'); }
  function stopWachten() {
    gestopt = true;
    clearTimeout(timer);
    document.removeEventListener('mouseout', opVerlaten);
  }
  function startWachten() {
    setTimeout(teaserToon, 2500);
    if (gestopt || !popMag) return;
    if (parseInt(pop.getAttribute('data-kar') || '0', 10) > 0) return;
    if (desktop) {
      document.addEventListener('mouseout', opVerlaten);
      if (!opProduct) timer = setTimeout(function () { toon('tijd'); }, 12000);
    } else if (paginas >= 2) {
      timer = setTimeout(function () { toon('tijd'); }, 10000);
    }
  }
  // wie een product in de winkelwagen legt, krijgt geen pop-up meer
  document.addEventListener('submit', function (e) {
    if (e.target && e.target.matches && e.target.matches('form[action*="/cart/add"]')) stopWachten();
  }, true);
  document.addEventListener('click', function (e) {
    var t = e.target && e.target.closest && e.target.closest('[name="add"], [data-b3-koop], [data-bline-upsell]');
    if (t && !pop.contains(t)) stopWachten();
  }, true);

  // wacht op de cookiekeuze (Shopify Customer Privacy API), met de banner zelf als reservecontrole
  function bannerOpen() {
    var b = document.getElementById('shopify-pc__banner'); if (!b) return false;
    var cs = getComputedStyle(b);
    return b.getClientRects().length > 0 && cs.display !== 'none' && cs.visibility !== 'hidden' && cs.opacity !== '0';
  }
  function keuzeGemaakt() {
    try {
      var cp = window.Shopify && Shopify.customerPrivacy;
      if (cp && typeof cp.shouldShowBanner === 'function') {
        if (!cp.shouldShowBanner()) return true;
        var c = cp.currentVisitorConsent && cp.currentVisitorConsent();
        return !!(c && (c.marketing !== '' || c.analytics !== ''));
      }
    } catch (e) {}
    return null;
  }
  var gestart = false;
  function start() { if (gestart) return; gestart = true; setTimeout(startWachten, 800); }
  document.addEventListener('visitorConsentCollected', start);
  var pogingen = 0;
  (function wacht() {
    if (gestart) return;
    var k = keuzeGemaakt();
    if (k === true && !bannerOpen()) return start();
    pogingen++;
    // geen privacy-API na 8 s en geen banner in beeld: gewoon starten
    if (k === null && pogingen > 16 && !bannerOpen()) return start();
    setTimeout(wacht, 500);
  })();

  var form = pop.querySelector('[data-b3-pop-form]');
  var fout = pop.querySelector('[data-b3-pop-fout]');
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var veld = form.querySelector('input[type=email]');
    var mail = (veld.value || '').trim();
    fout.hidden = true;
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(mail)) {
      fout.textContent = 'Vul een geldig e-mailadres in.'; fout.hidden = false; veld.focus(); return;
    }
    var knop = form.querySelector('button[type=submit]');
    knop.disabled = true; knop.setAttribute('aria-busy', 'true');
    fetch('https://a.klaviyo.com/client/subscriptions/?company_id=' + encodeURIComponent(pop.getAttribute('data-bedrijf')), {
      method: 'POST',
      headers: { 'Content-Type': 'application/vnd.api+json', revision: '2026-07-15' },
      body: JSON.stringify({ data: { type: 'subscription', attributes: {
        custom_source: 'Bline pop-up 10%',
        profile: { data: { type: 'profile', attributes: { email: mail, subscriptions: { email: { marketing: { consent: 'SUBSCRIBED' } } } } } }
      }, relationships: { list: { data: { type: 'list', id: pop.getAttribute('data-lijst') } } } } })
    }).then(function (r) {
      if (!r.ok) throw new Error('status ' + r.status);
      bewaar({ aangemeld: Date.now() });
      teaserMag = false;
      // bezoeker herkennen, zodat bekeken producten ook bij Klaviyo binnenkomen
      try {
        if (window.klaviyo && typeof window.klaviyo.identify === 'function') window.klaviyo.identify({ email: mail });
        else { window._learnq = window._learnq || []; window._learnq.push(['identify', { $email: mail }]); }
      } catch (x) {}
      meet('bline_pop_aangemeld', {});
      pop.querySelector('[data-b3-pop-stap="vraag"]').hidden = true;
      var klaar = pop.querySelector('[data-b3-pop-stap="klaar"]');
      klaar.hidden = false;
      var kop = klaar.querySelector('.b3-kop'); if (kop) kop.focus();
    }).catch(function () {
      fout.textContent = 'Dat lukte even niet. Probeer het zo nog eens.'; fout.hidden = false;
    }).finally(function () { knop.disabled = false; knop.removeAttribute('aria-busy'); });
  });
})();
