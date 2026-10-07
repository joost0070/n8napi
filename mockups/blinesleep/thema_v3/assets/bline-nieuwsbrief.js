/* Bline: het nieuwsbriefveld in de footer meldt aan bij Klaviyo (zelfde lijst als de pop-up), zodat ook hier de 10%-code volgt. */
(function () {
  'use strict';
  var form = document.getElementById('ContactFooter');
  if (!form) return;
  var BEDRIJF = 'VGJhRR', LIJST = 'SAeiP6';

  function melding(tekst, goed) {
    var m = form.querySelector('[data-bline-nb]');
    if (!m) {
      m = document.createElement('p');
      m.setAttribute('data-bline-nb', '');
      m.setAttribute('role', goed ? 'status' : 'alert');
      m.className = 'newsletter-form__message form__message';
      form.appendChild(m);
    }
    m.textContent = tekst;
  }

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var veld = form.querySelector('input[type=email]');
    var mail = ((veld && veld.value) || '').trim();
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(mail)) { melding('Vul een geldig e-mailadres in.', false); if (veld) veld.focus(); return; }
    var knop = form.querySelector('button');
    if (knop) knop.disabled = true;
    fetch('https://a.klaviyo.com/client/subscriptions/?company_id=' + BEDRIJF, {
      method: 'POST',
      headers: { 'Content-Type': 'application/vnd.api+json', revision: '2026-07-15' },
      body: JSON.stringify({ data: { type: 'subscription', attributes: {
        custom_source: 'Bline footer 10%',
        profile: { data: { type: 'profile', attributes: { email: mail, subscriptions: { email: { marketing: { consent: 'SUBSCRIBED' } } } } } }
      }, relationships: { list: { data: { type: 'list', id: LIJST } } } } })
    }).then(function (r) {
      if (!r.ok) throw new Error(String(r.status));
      try { localStorage.setItem('bline_pop', JSON.stringify({ aangemeld: Date.now() })); } catch (x) {}
      try { if (window.klaviyo && typeof window.klaviyo.identify === 'function') window.klaviyo.identify({ email: mail }); } catch (x) {}
      if (veld) veld.value = '';
      melding('Gelukt. Je code voor 10% komt zo in je mail.', true);
    }).catch(function () {
      melding('Dat lukte even niet. Probeer het zo nog eens.', false);
    }).finally(function () { if (knop) knop.disabled = false; });
  });
})();
