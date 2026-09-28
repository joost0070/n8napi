// ============================================================================
// Uitverkoopradar - n8n Code node ("Run once for all items")
//
// Per model: recent tempo (28 dagen, gecorrigeerd voor leegstand), ontseizoend
// naar een jaarniveau, en daarna week voor week vooruit van de voorraad
// afgeboekt tot die op is. Signaal als dat eerder is dan de hersteltijd + marge.
// Referentie-implementatie en uitleg: voorraad-watch/scripts/uitverkoop.py en
// voorraad-watch/UITVERKOOPRADAR.md.
//
// Verwacht deze nodes:
//   Webshops                      1 item per shop {naam, domein, token}
//   ShopifyQL: voorraad           1 antwoord per shop, in dezelfde volgorde
//   Shopify: orders               pagina's {orders:[...]}, 800 dagen terug
//   Shopify: producten            pagina's {products:[...]}: prijs, van-prijs, gepubliceerd
//   CE: orders 53 weken           pagina's {Content:[...]}
//   CE: producten (alle maten)    pagina's {Content:[...]}
//   Merk-config                   regels met o.a. merk, levertijd_dagen, hersteltijd_weken
// ============================================================================

const MERKSHOP = new Set(['keen-nl','jan-jansen-nl','heydude-nl','rge9fj-je','lazamani-nl','lazamani-de',
  'lazamani-en','toni-pons-nl','tofvel-nl','tofvel-de','tofvel-en','sockwell-b2c-nl','sockwell-b2c-de',
  'sockwell-b2c-en','ns3a4j-i1']);
const LEVERTIJD_STD = 6, VEILIG = 2, DEKKING = 8;

const vandaag = new Date();
const isoWeek = (d) => { const t = new Date(Date.UTC(d.getFullYear(), d.getMonth(), d.getDate()));
  t.setUTCDate(t.getUTCDate() + 4 - (t.getUTCDay() || 7));
  const y = new Date(Date.UTC(t.getUTCFullYear(), 0, 1));
  return [t.getUTCFullYear(), Math.ceil(((t - y) / 86400000 + 1) / 7)]; };
const [JAAR, NU] = isoWeek(vandaag);
const RECENT = [...new Set([...Array(28).keys()].map(k =>
  isoWeek(new Date(vandaag.getTime() - (k + 1) * 86400000))[1]))];
const volgende = (w) => w % 53 + 1;

// ---- ChannelEngine: artikelstam ----
const ex = (p, k) => (p.ExtraData || []).find(e => e.Key === k)?.Value ?? null;
const seizoenVan = (s) => { s = (s || '').toLowerCase();
  if (/herfst|winter|autumn/.test(s)) return 'FW';
  if (/lente|zomer|spring|summer/.test(s)) return 'SS';
  return 'ONBEKEND'; };
const art = {}, eanNaar = {};
for (const pg of $('CE: producten (alle maten)').all()) {
  for (const p of pg.json.Content || []) {
    if (!p.ParentMerchantProductNo) continue;
    const jaar = String(ex(p, 'Seizoensjaar') || '').toUpperCase();
    art[p.MerchantProductNo] = {
      mpn: p.MerchantProductNo, merk: p.Brand, naam: p.Name, maat: p.Size,
      model: p.ParentMerchantProductNo, voorraadCE: p.Stock || 0, prijs: p.Price || 0,
      sz: seizoenVan(ex(p, 'seizoen_NL') || ex(p, 'seizoen_EN')), jaar,
    };
    if (p.Ean) eanNaar[p.Ean] = p.MerchantProductNo;
  }
}
const naar = (s) => (art[s] ? s : eanNaar[s]);
const stype = (a) => (a.jaar === 'NOOS' ? 'NOOS' : a.sz);
const familie = (a) => `${a.merk}|${String(a.naam || '').split(/\s+/).slice(0, 2).join(' ').toLowerCase()}`;
const DAG = 86400000;

// ---- verkoop per dag per merk en per model (groei en 'vorig jaar zelfde weken') ----
const merkDag = {}, modelDag = {};
const telDag = (mpn, d, q) => { const a = art[mpn]; if (!a || q <= 0) return;
  const k = d.toISOString().slice(0, 10);
  (merkDag[a.merk] = merkDag[a.merk] || {})[k] = (merkDag[a.merk][k] || 0) + q;
  (modelDag[a.model] = modelDag[a.model] || {})[k] = (modelDag[a.model][k] || 0) + q; };
const somTussen = (dag, van, tot) => { if (!dag) return 0; const a = van.toISOString().slice(0, 10), b = tot.toISOString().slice(0, 10);
  let s = 0; for (const [k, q] of Object.entries(dag)) if (k >= a && k < b) s += q; return s; };

// ---- seizoenscurves: de twee laatste VOLLEDIGE cycli sep-aug, elk apart genormaliseerd ----
// (in januari is sep-aug van dit seizoen nog niet af en hoort het er niet in)
const eindJr = vandaag.getMonth() >= 8 ? vandaag.getFullYear() : vandaag.getFullYear() - 1;
const c2e = new Date(eindJr, 8, 1), c2s = new Date(eindJr - 1, 8, 1), c1s = new Date(eindJr - 2, 8, 1);
const staartVan = new Date(c2e.getTime() - 56 * DAG);
const cyc = { parent: {}, familie: {}, merktype: {} }, staart = [];
const telCurve = (mpn, d, q) => {
  const a = art[mpn]; if (!a || q <= 0) return;
  telDag(mpn, d, q);
  const c = d >= c1s && d < c2s ? 0 : d >= c2s && d < c2e ? 1 : -1; if (c < 0) return;
  const w = isoWeek(d)[1];
  for (const [niv, k] of [['parent', a.model], ['familie', familie(a)], ['merktype', `${a.merk}|${stype(a)}`]]) {
    const x = cyc[niv][k] = cyc[niv][k] || [{}, {}];
    x[c][w] = (x[c][w] || 0) + q;
    if (c === 1 && d >= staartVan) staart.push([niv, k, w, a.merk, q]);
  }
};
for (const pg of $('Shopify: orders').all()) {
  for (const o of pg.json.orders || []) {
    if (o.cancelled_at) continue;
    const d = new Date(o.created_at);
    for (const li of o.line_items || []) { const m = naar(li.sku); if (m) telCurve(m, d, li.quantity || 0); }
  }
}
const ceRegels = [];
for (const pg of $('CE: orders 53 weken').all()) {
  for (const o of pg.json.Content || []) {
    const d = new Date(o.OrderDate);
    for (const l of o.Lines || []) {
      if (l.Status === 'CANCELED') continue;
      telCurve(l.MerchantProductNo, d, l.Quantity || 0);
      ceRegels.push({ d, m: l.MerchantProductNo, q: l.Quantity || 0, kanaal: o.ChannelName,
        tot: +l.LineTotalInclVat || 0, fee: (+l.FeeFixed || 0) + (+l.LineTotalInclVat || 0) * (+l.FeeRate || 0) / 100 });
    }
  }
}
// Merkgroei: laatste 6 weken tegen dezelfde 6 weken vorig jaar. Een sprong aan het eind van de
// cyclus (Hunter, eind aug 2026: ~2,5x) wordt teruggerekend naar het niveau van de rest van de
// cyclus, anders leest de curve die sprong als seizoenspiek.
const groei = {};
for (const [merk, dag] of Object.entries(merkDag)) {
  const nu = somTussen(dag, new Date(vandaag - 42 * DAG), vandaag);
  const vj = somTussen(dag, new Date(vandaag - (42 + 364) * DAG), new Date(vandaag - 364 * DAG));
  if (vj >= 30) groei[merk] = nu / vj;
}
for (const [niv, k, w, merk, q] of staart) {
  const g = groei[merk];
  if (g && (g > 1.3 || g < 0.77)) cyc[niv][k][1][w] -= q * (1 - 1 / g);
}
const NAAD = isoWeek(c2s)[1];   // begin van de cyclus: niet over deze naad gladstrijken
const maakIdx = (x) => {
  const delen = []; let tot = 0;
  for (const c of x) {
    const t = Object.values(c).reduce((a, b) => a + b, 0); tot += t;
    if (t >= 60) { const d = {}; for (let w = 1; w <= 53; w++) d[w] = (c[w] || 0) / t; delen.push(d); }
  }
  if (!delen.length || tot < 150) return null;
  const i = {}; for (let w = 1; w <= 53; w++) i[w] = delen.reduce((s, d) => s + d[w], 0) / delen.length;
  const g = {}; let s = 0;
  for (let w = 1; w <= 53; w++) {
    const buren = [i[w]]; if (w !== NAAD) buren.push(i[((w - 2 + 53) % 53) + 1]); if (volgende(w) !== NAAD) buren.push(i[volgende(w)]);
    g[w] = buren.reduce((a, b) => a + b, 0) / buren.length; s += g[w]; }
  for (let w = 1; w <= 53; w++) g[w] /= s;
  const vec = [...Array(52).keys()].map(k => g[k + 1]);
  let top13 = 0; for (let k = 0; k < 52; k++) { let t = 0; for (let j = 0; j < 13; j++) t += vec[(k + j) % 52]; top13 = Math.max(top13, t); }
  let dal = 1, min = Infinity;
  for (let w = 1; w <= 53; w++) { const v = g[((w - 2 + 53) % 53) + 1] + g[w] + g[volgende(w)]; if (v < min) { min = v; dal = w; } }
  let piek = 1; for (let w = 1; w <= 53; w++) if (g[w] > g[piek]) piek = w;
  let cum = 0, afprijs = null, w = dal;
  for (let k = 0; k < 53; k++) { cum += g[w]; if (cum >= 0.70) { afprijs = w; break; } w = volgende(w); }
  return { idx: g, top13, dal, piek, afprijs };
};
const IDX = {};
for (const niv of Object.keys(cyc)) { IDX[niv] = {}; for (const [k, x] of Object.entries(cyc[niv])) { const v = maakIdx(x); if (v) IDX[niv][k] = v; } }
const curveVoor = (a) => IDX.parent[a.model] || IDX.familie[familie(a)] || IDX.merktype[`${a.merk}|${stype(a)}`] || null;

// ---- collectie ----
const HSZ = (NU >= 30 || NU <= 5) ? 'FW' : 'SS';
const HJR = (HSZ === 'FW' && NU <= 5) ? JAAR - 1 : JAAR;
const VSZ = HSZ === 'FW' ? 'SS' : 'FW', VJR = HSZ === 'FW' ? HJR : HJR - 1;
const collectie = (a, cv) => {
  if ((cv && cv.top13 < 0.33) || a.jaar === 'NOOS') return (!cv || cv.top13 < 0.45) ? 'doorlopend' : 'lopend?';
  if (!/^\d{4}$/.test(a.jaar)) return 'geen label';
  const j = +a.jaar;
  if (a.sz === HSZ && j === HJR) return 'lopend';
  if (a.sz === VSZ && j === VJR) return 'net voorbij';
  if (a.sz === HSZ && j === HJR - 1) return 'vorig jaar';
  return 'ouder';
};
const BESTELBAAR = new Set(['lopend', 'doorlopend', 'lopend?', 'geen label', 'doorloper']);
// Seizoensjaar = introductiejaar. Een ouder artikel dat nu op volle prijs goed verkoopt is een
// doorloper (bv. Hunter Downpour Tall, label FW 2025, in sep 2026 de best verkochte laars).
const OUD = new Set(['vorig jaar', 'ouder', 'net voorbij']);

// ---- Shopify-producten: online en afgeprijsd? prijsregime per collectie ----
const live = {}, sale = {}, colSale = {};
for (const pg of $('Shopify: producten').all()) {
  for (const p of pg.json.products || []) {
    const online = p.status === 'active' && !!p.published_at;
    for (const v of p.variants || []) {
      const m = naar(v.sku); if (!m) continue;
      if (online) live[m] = true;
      const af = +v.compare_at_price > +v.price * 1.02;
      if (af) sale[m] = true;
      const a = art[m], k = `${a.merk}|${a.sz}|${a.jaar}`;
      const c = colSale[k] = colSale[k] || [0, 0]; c[1]++; if (af) c[0]++;
    }
  }
}
const colInSale = (a) => { const c = colSale[`${a.merk}|${a.sz}|${a.jaar}`]; return !!c && c[1] >= 40 && c[0] / c[1] >= 0.45; };

// ---- ShopifyQL per shop: 28 dagen en 365 dagen ----
const shops = $('Webshops').all().map(i => i.json);
const qlAntw = $('ShopifyQL: voorraad').all().map(i => i.json);
const q28 = {}, q365 = {};
qlAntw.forEach((antw, i) => {
  const dom = shops[i]?.domein;
  const data = antw.data || {};
  for (const [sleutel, doel] of [['d28', q28], ['d365', q365]]) {
    for (const r of data[sleutel]?.tableData?.rows || []) {
      const m = naar(r.product_variant_sku); if (!m) continue;
      (doel[m] = doel[m] || []).push({ dom, eind: Math.max(+r.ending_inventory_units || 0, 0),
        verk: Math.max(+r.inventory_units_sold || 0, 0), leeg: Math.max(+r.days_out_of_stock || 0, 0) });
    }
  }
});
const mediaan = (a) => { if (!a.length) return 0; const s = [...a].sort((x, y) => x - y); return s[Math.floor(s.length / 2)]; };

const grens = new Date(vandaag.getTime() - 28 * 86400000);
const mp28 = {}; let feeSom = 0, omzetSom = 0;
for (const r of ceRegels) {
  if (r.d < grens) continue;
  if (art[r.m]) mp28[r.m] = (mp28[r.m] || 0) + r.q;
  feeSom += r.fee; omzetSom += r.tot;
}

// ---- hersteltijd per merk: opgegeven levertijd (leverancier), anders de gemeten hersteltijd
//      (hoe lang een bestseller in de praktijk leeg stond), anders standaard ----
const cfg = {};
for (const pg of $('Merk-config').all()) { const r = pg.json; if (r.merk) cfg[String(r.merk).trim().toLowerCase()] = r; }
const levertijd = (merk) => { const c = cfg[String(merk || '').toLowerCase()] || {};
  const opgegeven = +c.levertijd_dagen ? Math.ceil(+c.levertijd_dagen / 7) : +c.levertijd_weken;
  return opgegeven || +c.hersteltijd_weken || LEVERTIJD_STD; };

// ---- per model ----
const modellen = {};
for (const m of new Set([...Object.keys(q28), ...Object.keys(q365), ...Object.keys(mp28)])) {
  if (art[m]) (modellen[art[m].model] = modellen[art[m].model] || []).push(m);
}
const merkMaat = {};
for (const [m, rows] of Object.entries(q365)) {
  const a = art[m]; const n = rows.reduce((s, r) => s + r.verk, 0);
  (merkMaat[a.merk] = merkMaat[a.merk] || {})[a.maat] = (merkMaat[a.merk][a.maat] || 0) + n;
}
const afboeken = (vrd, jv, idx) => { if (vrd <= 0) return 0; let rest = vrd, dagen = 0, w = NU;
  for (let k = 0; k < 52; k++) { const v = jv * idx[w]; if (v >= rest) return dagen + 7 * rest / v; rest -= v; dagen += 7; w = volgende(w); }
  return null; };
const vraagOver = (jv, idx, weken) => { let s = 0, w = NU; for (let k = 0; k < weken; k++) { s += jv * idx[w]; w = volgende(w); } return s; };
const maatNr = (m) => { const n = parseFloat(String(m || '').replace(',', '.')); return Number.isFinite(n) ? n : 999; };
const RANG = { 'LEEG': 0, 'TE LAAT': 1, 'BESTEL NU': 2, 'VOLGENDE WEEK': 3, 'OK': 4, 'GEEN VRAAG': 5 };

const uit = [];
for (const [model, mpns] of Object.entries(modellen)) {
  const rij = mpns.map(m => {
    const a = art[m], r28 = q28[m] || [], r365 = q365[m] || [];
    const n12 = r365.reduce((s, r) => s + r.verk, 0) + 0;
    const leeg12 = mediaan(r365.map(r => r.leeg));
    return { m, a, maat: a.maat,
      vrd: r28.length ? Math.max(...r28.map(r => r.eind)) : a.voorraadCE,
      verk28: r28.reduce((s, r) => s + r.verk, 0) + (mp28[m] || 0),
      leeg28: r28.length ? Math.min(mediaan(r28.map(r => r.leeg)), 28) : 28,
      n12, t12: n12 / Math.max(365 - leeg12, 14) * 7,
      kanaal: { merkshop: r28.filter(r => MERKSHOP.has(r.dom)).reduce((s, r) => s + r.verk, 0),
                breed: r28.filter(r => !MERKSHOP.has(r.dom)).reduce((s, r) => s + r.verk, 0),
                marktplaats: mp28[m] || 0 } };
  });
  const a0 = rij.reduce((b, x) => (x.n12 > b.n12 ? x : b), rij[0]).a;
  const cv = curveVoor(a0); if (!cv) continue;
  let col = collectie(a0, cv);

  const mm = merkMaat[a0.merk] || {}, mtot = rij.reduce((s, x) => s + (mm[x.maat] || 0), 0);
  const gtot = rij.reduce((s, x) => s + x.n12 + 3 * x.verk28, 0), K = 10;
  for (const x of rij) x.aandeel = (x.n12 + 3 * x.verk28 + K * (mtot ? (mm[x.maat] || 0) / mtot : 1 / rij.length)) / (gtot + K);
  const as = rij.reduce((s, x) => s + x.aandeel, 0) || 1; for (const x of rij) x.aandeel /= as;

  const verk28 = rij.reduce((s, x) => s + x.verk28, 0);
  const besch = rij.reduce((s, x) => s + x.aandeel * (28 - x.leeg28), 0);
  const idxRecent = RECENT.reduce((s, w) => s + cv.idx[w], 0) / RECENT.length;
  const j12 = rij.reduce((s, x) => s + x.t12, 0) * 52, n12 = rij.reduce((s, x) => s + x.n12, 0);
  let jaarvraag, bron;
  if (verk28 >= 8 && besch >= 5 && idxRecent >= 0.5 / 52) {
    jaarvraag = verk28 / besch * 7 / idxRecent; bron = 'recent';
    if (n12 >= 30 && j12 > 0) jaarvraag = Math.min(Math.max(jaarvraag, 0.4 * j12), 2.5 * j12 * Math.max(1, groei[a0.merk] || 1));
  } else if (j12 > 0) { jaarvraag = j12; bron = '12 mnd'; } else continue;

  const lt = levertijd(a0.merk);
  for (const x of rij) {
    const jv = jaarvraag * x.aandeel;
    x.dagen = afboeken(x.vrd, jv, cv.idx);
    x.bestel = Math.max(0, Math.round(vraagOver(jv, cv.idx, lt + DEKKING) - x.vrd));
    const horizon = vraagOver(jv, cv.idx, lt + VEILIG + DEKKING);
    x.status = (horizon < 2 && x.vrd === 0) ? 'GEEN VRAAG' : x.vrd === 0 ? 'LEEG'
      : x.dagen === null ? 'OK' : x.dagen < lt * 7 ? 'TE LAAT' : x.dagen < (lt + VEILIG) * 7 ? 'BESTEL NU'
      : x.dagen < (lt + VEILIG + 2) * 7 ? 'VOLGENDE WEEK' : 'OK';
  }
  const kern = new Set(); let cum = 0;
  for (const x of [...rij].sort((p, q) => q.aandeel - p.aandeel)) { if (cum >= 0.8) break; kern.add(x.m); cum += x.aandeel; }
  const kernRij = rij.filter(x => kern.has(x.m) && x.status !== 'GEEN VRAAG');
  const status = kernRij.reduce((s, x) => (RANG[x.status] < RANG[s] ? x.status : s), 'OK');
  const eerste = kernRij.filter(x => x.dagen !== null).reduce((s, x) => Math.min(s, x.dagen), Infinity);
  const totVrd = rij.reduce((s, x) => s + x.vrd, 0);

  const nLive = rij.filter(x => live[x.m]).length, nSale = rij.filter(x => live[x.m] && sale[x.m]).length;
  const inSale = colInSale(a0), label = col;
  if (OUD.has(col) && verk28 >= 8 && nLive > 0 && nSale / nLive < 0.5) col = 'doorloper';

  // controle: vorig jaar dezelfde weken (28 dagen terug en de komende hersteltijd + dekking)
  const vjd = new Date(vandaag - 364 * DAG), md = modelDag[model];
  const vj28 = somTussen(md, new Date(vjd - 28 * DAG), vjd);
  const vjHor = somTussen(md, vjd, new Date(vjd.getTime() + (lt + DEKKING) * 7 * DAG));
  const verwacht = rij.reduce((s, x) => s + vraagOver(jaarvraag * x.aandeel, cv.idx, lt + DEKKING), 0);
  const misEur = rij.filter(x => kern.has(x.m) && ['LEEG', 'TE LAAT'].includes(x.status))
    .reduce((s, x) => s + vraagOver(jaarvraag * x.aandeel, cv.idx, lt) * (x.a.prijs || 0), 0);

  uit.push({ model, merk: a0.merk, naam: a0.naam, collectie: col, label, seizoen: `${a0.sz} ${a0.jaar}`.trim(),
    piek: cv.piek, afprijs_wk: cv.afprijs, verk28, voorraad: totVrd, jaarvraag: Math.round(jaarvraag), bron,
    levertijd: lt, status, eerste_leeg: Number.isFinite(eerste) ? Math.round(eerste) : null,
    kanaal: ['merkshop', 'breed', 'marktplaats'].reduce((o, k) => ({ ...o, [k]: rij.reduce((s, x) => s + x.kanaal[k], 0) }), {}),
    // de prijs van het model zelf beslist; de collectievlag gaat als info mee
    bestelbaar: BESTELBAAR.has(col) && nLive > 0 && nSale / nLive < 0.5, collectie_in_sale: inSale,
    vj_28: vj28, vj_horizon: vjHor, verwacht_horizon: Math.round(verwacht), mis_eur: Math.round(misEur),
    weinig_historie: n12 < 30 || vjHor < 20,
    sprong: vj28 >= 3 && verk28 >= 4 * vj28 ? Math.round(10 * verk28 / vj28) / 10 : null,
    bestel_totaal: rij.filter(x => kern.has(x.m)).reduce((s, x) => s + x.bestel, 0),
    maten: rij.filter(x => x.status !== 'GEEN VRAAG' || x.vrd > 0).sort((p, q) => maatNr(p.maat) - maatNr(q.maat)).map(x => ({
      maat: x.maat, vrd: x.vrd, verk28: x.verk28, dagen: x.dagen === null ? null : Math.round(x.dagen),
      status: x.status, bestel: x.bestel, kern: kern.has(x.m) })),
  });
}

const top10 = uit.filter(u => u.verk28 > 0).sort((a, b) => b.verk28 - a.verk28).slice(0, 10);
const signalen = uit.filter(u => u.bestelbaar && ['LEEG', 'TE LAAT', 'BESTEL NU'].includes(u.status) && u.verk28 >= 3)
  // leeg en te laat samen, op gemiste omzet binnen de hersteltijd; daarna bestel-nu op volume
  .sort((a, b) => ((['LEEG', 'TE LAAT'].includes(a.status) ? 0 : 1) - (['LEEG', 'TE LAAT'].includes(b.status) ? 0 : 1))
    || (b.mis_eur - a.mis_eur) || (b.verk28 - a.verk28));

return [{ json: {
  peildatum: vandaag.toISOString().slice(0, 10), week: NU, huidige_collectie: `${HSZ} ${HJR}`,
  marktplaats_fee_pct: omzetSom ? Math.round(1000 * feeSom / omzetSom) / 10 : null,
  top10, signalen: signalen.slice(0, 40), n_signalen: signalen.length,
  urgent: signalen.filter(u => ['LEEG', 'TE LAAT'].includes(u.status)).length,
  groei: Object.fromEntries(Object.entries(groei).map(([m, g]) => [m, Math.round(100 * g) / 100])),
} }];
