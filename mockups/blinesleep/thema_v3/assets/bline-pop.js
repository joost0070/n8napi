/* Bline aanmeldpop-up: meldt aan bij Klaviyo (dubbele bevestiging) en start zo de welkomstflow met 10%. */
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
  if (staat.dicht && Date.now() - staat.dicht < DAGEN_NA_SLUITEN * 864e5) return;
  // wie uit een Bline-mail komt, staat al op de lijst
  if (/[?&]utm_source=klaviyo/i.test(location.search) || /[?&]_kx=/.test(location.search)) return;

  var vorigeFocus = null, open = false;
  function toon(bron) {
    if (open || document.querySelector('cart-drawer.active, .drawer.active')) return;
    open = true; vorigeFocus = document.activeElement;
    pop.hidden = false;
    requestAnimationFrame(function () { pop.classList.add('is-open'); });
    document.documentElement.classList.add('b3-pop-open');
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
    document.documentElement.classList.remove('b3-pop-open');
    setTimeout(function () { pop.hidden = true; }, 250);
    var s = lees(); if (!s.aangemeld) { s.dicht = Date.now(); bewaar(s); }
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

  // tonen na 25 seconden, na de helft van de pagina, of (desktop) als de muis naar boven het venster uit gaat
  var timer = setTimeout(function () { toon('tijd'); }, 25000);
  function opScroll() {
    var h = document.documentElement.scrollHeight - window.innerHeight;
    if (h > 400 && window.scrollY / h > 0.5) toon('scroll');
  }
  function opVerlaten(e) { if (!e.relatedTarget && e.clientY <= 0) toon('verlaten'); }
  window.addEventListener('scroll', opScroll, { passive: true });
  document.addEventListener('mouseout', opVerlaten);
  function stopWachten() {
    clearTimeout(timer);
    window.removeEventListener('scroll', opScroll);
    document.removeEventListener('mouseout', opVerlaten);
  }

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
