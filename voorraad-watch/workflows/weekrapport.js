// ============================================================================
// Weekrapport / dagelijks signaal - n8n Code node ("Run once for all items")
//
// Maandag: volledig rapport (uitverkoopradar + merkoverzicht).
// Andere dagen: alleen als er een kernmaat van een lopend artikel leeg is of
// te laat dreigt te raken. Het IF-node erna beslist of er gemaild wordt.
// ============================================================================
const R = $('Uitverkoopradar').first().json;
const maandag = new Date().getDay() === 1;

const esc = (s) => String(s ?? '').replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const KLEUR = { 'LEEG': '#9B1C1C', 'TE LAAT': '#B42318', 'BESTEL NU': '#B54708', 'VOLGENDE WEEK': '#8A6D00', 'OK': '#2E6B45' };
const pil = (s) => `<span style="display:inline-block;padding:1px 7px;border-radius:3px;font-size:11px;font-weight:600;` +
  `color:#fff;background:${KLEUR[s] || '#6B7280'}">${esc(s)}</span>`;
const dagen = (d) => d === null || d === undefined ? '> 1 jaar' : d === 0 ? 'leeg' : `${d} d`;
const maatstrook = (maten) => maten.filter(x => x.kern).map(x =>
  `<span style="display:inline-block;margin:1px 2px;padding:1px 5px;border:1px solid ${KLEUR[x.status] || '#ccc'};` +
  `border-radius:2px;font:11px monospace;color:${KLEUR[x.status] || '#333'}">${esc(x.maat)} · ${x.vrd === 0 ? 'leeg' : dagen(x.dagen)}</span>`).join('');
const kanaal = (k) => { const t = k.merkshop + k.breed + k.marktplaats || 1;
  return `${Math.round(100 * k.merkshop / t)}% merkshop · ${Math.round(100 * k.breed / t)}% breed · ${Math.round(100 * k.marktplaats / t)}% marktplaats`; };
const th = 'style="text-align:left;padding:6px 8px;border-bottom:2px solid #222;font:600 11px sans-serif;text-transform:uppercase;color:#555"';
const td = 'style="padding:6px 8px;border-bottom:1px solid #ddd;font:13px sans-serif;vertical-align:top"';

let html = `<div style="font-family:sans-serif;max-width:900px">
<h2 style="margin:0 0 4px">Uitverkoopradar – week ${R.week}</h2>
<div style="color:#666;font-size:12px;margin-bottom:16px">Peildatum ${esc(R.peildatum)} · lopende collectie ${esc(R.huidige_collectie)} ·
${R.n_signalen} modellen met een signaal, waarvan ${R.urgent} leeg of te laat</div>`;

// merkgroei: laatste 6 weken tegen dezelfde weken vorig jaar
const groei = Object.entries(R.groei || {}).filter(([, g]) => g >= 1.3 || g <= 0.77).sort((a, b) => b[1] - a[1]);
if (groei.length) html += `<div style="font-size:12px;margin-bottom:12px"><b>Afwijkend tempo t.o.v. vorig jaar (6 wk):</b> ` +
  groei.map(([m, g]) => `${esc(m)} <span style="color:${g >= 1 ? '#2E6B45' : '#B42318'}">${g.toFixed(1)}×</span>`).join(' · ') + `</div>`;
const controle = (u) => {
  let t = `vorig jaar ${u.vj_horizon} · nu verwacht ${u.verwacht_horizon}`;
  if (u.sprong) t += `<div style="color:#B54708;font-weight:600">${u.sprong}× vorig jaar – actie, lancering of echte groei? Eerst bevestigen.</div>`;
  else if (u.weinig_historie) t += `<div style="color:#8A6D00">weinig historie – voorzichtig bestellen</div>`;
  return t; };

html += `<h3 style="margin:18px 0 6px">Top 10 best verkocht – resterende voorraad</h3>
<table style="border-collapse:collapse;width:100%"><tr>
<th ${th}>#</th><th ${th}>Artikel</th><th ${th}>Collectie</th><th ${th}>Verkocht 28 d</th><th ${th}>Voorraad</th>
<th ${th}>1e kernmaat leeg</th><th ${th}>Status</th></tr>`;
R.top10.forEach((u, i) => {
  html += `<tr><td ${td}>${i + 1}</td>
  <td ${td}><b>${esc(u.merk)}</b> ${esc(u.naam)}<br>${maatstrook(u.maten)}
    <div style="color:#777;font-size:11px;margin-top:2px">piek wk ${u.piek} · ${kanaal(u.kanaal)}</div></td>
  <td ${td}>${esc(u.collectie)}<br><span style="color:#777;font-size:11px">${esc(u.seizoen)}${u.collectie === 'doorloper' ? ' · ouder label, verkoopt op volle prijs' : ''}</span></td>
  <td ${td}>${u.verk28}</td><td ${td}>${u.voorraad}</td>
  <td ${td}>${dagen(u.eerste_leeg)}<br><span style="color:#777;font-size:11px">hersteltijd ${u.levertijd} wk</span></td>
  <td ${td}>${pil(u.status)}</td></tr>`;
});
html += `</table>`;

if (R.signalen.length) {
  html += `<h3 style="margin:22px 0 6px">Bijschakelen – lopende collectie en doorlopende artikelen</h3>
  <table style="border-collapse:collapse;width:100%"><tr>
  <th ${th}>Status</th><th ${th}>Artikel</th><th ${th}>Maten</th><th ${th}>Verkocht 28 d</th><th ${th}>Bestelvoorstel</th>
  <th ${th}>Controle: hersteltijd + 8 wk</th></tr>`;
  for (const u of R.signalen.slice(0, 25)) {
    const krap = u.maten.filter(x => x.kern && ['LEEG', 'TE LAAT', 'BESTEL NU'].includes(x.status));
    html += `<tr><td ${td}>${pil(u.status)}</td>
    <td ${td}><b>${esc(u.merk)}</b> ${esc(u.naam)}<br><span style="color:#777;font-size:11px">${esc(u.seizoen)} · piek wk ${u.piek}</span></td>
    <td ${td}>${krap.map(x => `${esc(x.maat)}: ${x.vrd === 0 ? 'leeg' : dagen(x.dagen)}`).join('<br>')}</td>
    <td ${td}>${u.verk28}</td>
    <td ${td}>${krap.map(x => `${esc(x.maat)}: ${x.bestel}`).join('<br>')}
      ${u.kanaal.marktplaats > 0 && u.status !== 'BESTEL NU' ? `<div style="color:#B54708;font-size:11px;margin-top:3px">${Math.round(100 * u.kanaal.marktplaats / Math.max(u.verk28, 1))}% via marktplaats: laatste paren naar eigen shops</div>` : ''}
    </td><td ${td}><span style="font-size:12px">${controle(u)}</span>
      ${u.mis_eur ? `<div style="color:#777;font-size:11px">gemist binnen hersteltijd ± € ${Math.round(u.mis_eur).toLocaleString('nl-NL')}</div>` : ''}</td></tr>`;
  }
  html += `</table>`;
}

html += `<p style="color:#888;font-size:11px;margin-top:18px">Uitverkoopdatum = recente verkoop (28 d, gecorrigeerd voor leegstand),
ontseizoend en week voor week vooruit afgeboekt langs de eigen seizoenscurve van het model. Status volgt de slechtste
kernmaat (samen 80% van de vraag). Vraag is bruto: het signaal komt eerder, niet later. Volgorde: leeg en te laat
eerst, op omzet die binnen de hersteltijd misloopt. Marktplaatsen kosten gemiddeld ${R.marktplaats_fee_pct ?? '?'}% fee: bij de
laatste paren gaat de eigen shop voor. Alleen modellen die zelf op volle prijs staan krijgen een bestelvoorstel.
'Controle' zet het voorstel naast wat er vorig jaar in dezelfde weken verkocht werd.</p></div>`;

// op maandag het merkoverzicht uit de bestaande analyse erbij
if (maandag) {
  const rows = $('Analyse: signaal per maat').all().map(i => i.json);
  const perMerk = {};
  for (const r of rows) {
    const m = perMerk[r.merk] = perMerk[r.merk] || { merk: r.merk, waarde: 0, bij: 0, af: 0 };
    m.waarde += r.voorraadwaarde || 0;
    if (r.signaal === 'BIJBESTELLEN') m.bij++;
    if (r.signaal === 'NU-AFPRIJZEN' || r.signaal === 'KORTING-VERDIEPEN') m.af++;
  }
  const eur = n => '€ ' + Math.round(n).toLocaleString('nl-NL');
  html += `<h3 style="margin:22px 0 6px">Merkoverzicht</h3><table style="border-collapse:collapse"><tr>
  <th ${th}>Merk</th><th ${th}>Voorraadwaarde</th><th ${th}>Maten bijbestellen</th><th ${th}>Maten afprijzen</th></tr>`;
  for (const m of Object.values(perMerk).sort((a, b) => b.waarde - a.waarde).slice(0, 14))
    html += `<tr><td ${td}>${esc(m.merk)}</td><td ${td}>${eur(m.waarde)}</td><td ${td}>${m.bij}</td><td ${td}>${m.af}</td></tr>`;
  html += `</table>`;
}

return [{ json: { html, week: R.week, maandag, urgent: R.urgent,
  onderwerp: maandag ? `Voorraad Watch – week ${R.week}` : `Uitverkoopsignaal – ${R.urgent} artikel(en) leeg of te laat` } }];
