/* Bline v3: kleur wisselen, aantal, extra hoes, galerij en in de winkelwagen. */
(function () {
  'use strict';
  function geld(c) {
    var e = Math.floor(c / 100), ct = String(c % 100).padStart(2, '0');
    return '€' + String(e).replace(/\B(?=(\d{3})+(?!\d))/g, '.') + ',' + ct;
  }

  function Galerij(el) {
    var track = el.querySelector('[data-b3-track]');
    var duims = el.querySelectorAll('.b3-gal__stip i');
    var nu = el.querySelector('[data-b3-nu]');
    function index() { return Math.round(track.scrollLeft / Math.max(track.clientWidth, 1)); }
    function zet() {
      var i = index();
      if (nu) nu.textContent = i + 1;
      duims.forEach(function (d, j) { d.classList.toggle('is-actief', i === j); });
    }
    var t;
    track.addEventListener('scroll', function () { clearTimeout(t); t = setTimeout(zet, 60); }, { passive: true });
    return { reset: function () { track.scrollLeft = 0; zet(); } };
  }

  function Product(root) {
    var D = JSON.parse(root.querySelector('[data-b3-data]').textContent);
    var staat = { kleur: D.gekozen, aantal: 1, hoes: false };
    var gal = {};
    root.querySelectorAll('.b3-gal').forEach(function (g) { gal[g.getAttribute('data-kleur')] = Galerij(g); });
    var $ = function (s) { return root.querySelector(s); };
    var $$ = function (s) { return root.querySelectorAll(s); };

    function hoesPrijs(k) { return staat.aantal === 2 ? k.hoesPrijs : k.hoesPrijs - D.korting; }
    function totaal() {
      var k = D.kleuren[staat.kleur];
      var som = k.prijs * staat.aantal + (staat.hoes ? k.hoesPrijs : 0);
      return (staat.aantal === 2 || staat.hoes) ? som - D.korting : som;
    }
    function teken() {
      var k = D.kleuren[staat.kleur];
      $('[data-b3-kleurnaam]').textContent = k.naam;
      $('[data-b3-prijs]').textContent = geld(k.prijs);
      $('[data-b3-prijs1]').textContent = geld(k.prijs);
      $('[data-b3-prijs2]').textContent = geld(k.prijs * 2 - D.korting);
      $('[data-b3-prijs2oud]').textContent = geld(k.prijs * 2);
      $('[data-b3-hoesnaam]').textContent = k.naam.toLowerCase();
      $('[data-b3-hoesprijs]').textContent = geld(hoesPrijs(k));
      var oud = $('[data-b3-hoesoud]'); oud.textContent = geld(k.hoesPrijs); oud.hidden = staat.aantal === 2;
      var hb = $('[data-b3-hoesbeeld] img'); if (hb && k.hoesBeeld) hb.src = k.hoesBeeld;
      $('[data-b3-hoes]').closest('.b3-hoes').hidden = !k.hoesBeschikbaar;
      $('[data-b3-knopprijs]').textContent = geld(totaal());
      $('[data-b3-plaknaam]').textContent = k.naam;
      $('[data-b3-plakprijs]').textContent = geld(totaal());
      $('[data-b3-hint2]').hidden = staat.aantal !== 2;
      $$('[data-b3-koop]').forEach(function (b) { b.disabled = !k.beschikbaar; });
      $('[data-b3-knoptekst]').textContent = k.beschikbaar ? 'In winkelwagen' : 'Tijdelijk uitverkocht';
    }
    function kies(kleur, scroll) {
      if (!D.kleuren[kleur]) return;
      staat.kleur = kleur;
      $$('.b3-gal').forEach(function (g) { g.hidden = g.getAttribute('data-kleur') !== kleur; });
      $$('[data-b3-kleur]').forEach(function (b) {
        var aan = b.getAttribute('data-b3-kleur') === kleur;
        b.classList.toggle('is-gekozen', aan); b.setAttribute('aria-checked', aan ? 'true' : 'false');
      });
      var g = root.querySelector('.b3-gal[data-kleur="' + kleur + '"]');
      g.querySelectorAll('img[loading="lazy"]').forEach(function (i, n) { if (n < 3) i.loading = 'eager'; });
      gal[kleur].reset();
      teken();
      try {
        if (root.getAttribute('data-pagina') === 'product') history.replaceState(null, '', D.kleuren[kleur].url + location.search.replace(/([?&])kleur=[^&]*/, '$1').replace(/[?&]$/, ''));
        else { var u = new URL(location.href); u.searchParams.set('kleur', kleur); history.replaceState(null, '', u); }
      } catch (e) {}
      if (scroll) root.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
    $$('[data-b3-kleur]').forEach(function (b) { b.addEventListener('click', function () { kies(b.getAttribute('data-b3-kleur')); }); });
    document.querySelectorAll('[data-b3-zet-kleur]').forEach(function (b) {
      b.addEventListener('click', function (e) { e.preventDefault(); kies(b.getAttribute('data-b3-zet-kleur'), true); });
    });
    $$('[data-b3-aantal]').forEach(function (b) {
      b.addEventListener('click', function () {
        staat.aantal = Number(b.getAttribute('data-b3-aantal'));
        $$('[data-b3-aantal]').forEach(function (x) { var aan = x === b; x.classList.toggle('is-gekozen', aan); x.setAttribute('aria-checked', aan ? 'true' : 'false'); });
        teken();
      });
    });
    $('[data-b3-hoes]').addEventListener('change', function (e) { staat.hoes = e.target.checked; teken(); });

    function koop(knop) {
      var k = D.kleuren[staat.kleur];
      var items = [{ id: k.variant, quantity: staat.aantal }];
      if (staat.hoes && k.hoesBeschikbaar) items.push({ id: k.hoes, quantity: 1 });
      var lade = document.querySelector('cart-drawer');
      var secties = lade && typeof lade.getSectionsToRender === 'function' ? lade.getSectionsToRender().map(function (s) { return s.id; }) : [];
      var fout = $('[data-b3-fout]'); fout.hidden = true;
      knop.disabled = true; knop.setAttribute('aria-busy', 'true');
      fetch((window.routes && window.routes.cart_add_url ? window.routes.cart_add_url : '/cart/add') + '.js', {
        method: 'POST', headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
        body: JSON.stringify({ items: items, sections: secties, sections_url: window.location.pathname })
      }).then(function (r) { return r.json().then(function (j) { if (!r.ok) throw j; return j; }); })
        .then(function (state) {
          if (lade && typeof lade.renderContents === 'function' && state.sections) {
            lade.classList.remove('is-empty');
            lade.renderContents(state);
          } else { window.location.href = (window.routes && window.routes.cart_url) || '/cart'; }
        })
        .catch(function () { fout.hidden = false; })
        .finally(function () { knop.disabled = false; knop.removeAttribute('aria-busy'); });
    }
    $$('[data-b3-koop]').forEach(function (b) { b.addEventListener('click', function () { koop(b); }); });

    var plak = $('[data-b3-plak]'), hoofdknop = $('.b3-knop--groot');
    if (plak && hoofdknop) {
      // alleen tonen als de grote knop boven uit beeld is gescrold
      var wacht = false;
      var meet = function () { wacht = false; plak.hidden = hoofdknop.getBoundingClientRect().bottom > 0; };
      window.addEventListener('scroll', function () { if (!wacht) { wacht = true; requestAnimationFrame(meet); } }, { passive: true });
      meet();
    }
    var q = new URLSearchParams(location.search).get('kleur');
    if (q && D.kleuren[q] && q !== staat.kleur) kies(q); else teken();
  }

  function videos() {
    if (!('IntersectionObserver' in window)) return;
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        var v = e.target;
        if (e.isIntersecting) { if (v.preload === 'none') v.preload = 'auto'; var p = v.play(); if (p && p.catch) p.catch(function () {}); }
        else v.pause();
      });
    }, { threshold: .35 });
    document.querySelectorAll('.b3 video').forEach(function (v) { io.observe(v); });
  }

  function start() {
    document.querySelectorAll('[data-b3-product]').forEach(Product);
    videos();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start); else start();
})();
