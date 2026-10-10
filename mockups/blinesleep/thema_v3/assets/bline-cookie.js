/* Bline: Shopify-cookiebanner in eigen woorden. De keuze zelf blijft volledig bij Shopify (Customer Privacy API). */
(function () {
  'use strict';
  var TITEL = 'Cookies';
  var TEKST = 'We gebruiken cookies zodat de winkel goed werkt. Met jouw toestemming meten we ook wat werkt en tonen we je relevante advertenties, met hulp van onder andere Shopify, Google, Meta, Microsoft (Clarity) en Klaviyo. Meer lees je in onze ';
  var LINK = 'privacyverklaring';

  function pasAan(banner) {
    if (!banner || banner.getAttribute('data-bline') === '1') return;
    var kop = banner.querySelector('#shopify-pc__banner__body-title');
    var p = banner.querySelector('.shopify-pc__banner__body p');
    if (kop) kop.textContent = TITEL;
    if (p) {
      var a = document.createElement('a');
      a.href = '/pages/privacy';
      a.id = 'shopify-pc__banner__body-policy-link';
      a.textContent = LINK;
      p.textContent = TEKST;
      p.appendChild(a);
      p.appendChild(document.createTextNode('.'));
    }
    var nee = banner.querySelector('#shopify-pc__banner__btn-decline');
    if (nee) nee.textContent = 'Weigeren';
    var vk = banner.querySelector('#shopify-pc__banner__btn-manage-prefs span');
    if (vk) vk.textContent = 'Voorkeuren';
    banner.setAttribute('data-bline', '1');
  }

  function zoek() { pasAan(document.getElementById('shopify-pc__banner')); }
  zoek();
  if (!('MutationObserver' in window)) return;
  var mo = new MutationObserver(zoek);
  mo.observe(document.documentElement, { childList: true, subtree: true });
  // na een minuut is de banner er of niet; dan hoeft er niet meer gekeken te worden
  setTimeout(function () { mo.disconnect(); }, 60000);
})();
