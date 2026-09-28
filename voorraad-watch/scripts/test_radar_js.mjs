// Test: draai de n8n Code node lokaal. Uitvoeren in de datamap (rows.json, shop/, ord/, ql/, ql28/):
//   node <repo>/voorraad-watch/scripts/test_radar_js.mjs <repo>/voorraad-watch/workflows/uitverkoopradar.js
// Draait de n8n Code node lokaal op de opgehaalde data; $('Node') wordt nagebootst.
import fs from 'fs'; import path from 'path';
const B = '.', rd = f => JSON.parse(fs.readFileSync(f));
const lijst = d => fs.readdirSync(d).map(f => path.join(d, f));
const shops = fs.readFileSync('shops.py', 'utf8').matchAll(/\("([^"]+)","([^"]+)","([^"]+)"\)/g);
const web = [...shops].map(m => ({ naam: m[1], domein: m[2], token: m[3] }));
const ce = rd('rows.json');
const ceProd = [{ Content: ce.map(r => ({ MerchantProductNo: r.mpn, ParentMerchantProductNo: r.parent || r.name, Brand: r.brand,
  Name: r.name, Size: r.size, Stock: r.stock, Price: r.price, Ean: r.ean,
  ExtraData: [{ Key: 'Seizoensjaar', Value: r.season_year }, { Key: 'seizoen_NL', Value: r.season }] })) }];
const shopOrd = [], shopProd = [];
for (const w of web) {
  const o = `shop/${w.domein}_orders.json`, p = `shop/${w.domein}_products.json`;
  if (fs.existsSync(o)) shopOrd.push({ orders: rd(o).map(r => ({ created_at: r.d + 'T12:00:00Z', line_items: [{ sku: r.sku, quantity: r.q }] })) });
  if (fs.existsSync(p)) shopProd.push({ products: rd(p).map(v => ({ status: 'active', published_at: v.gepubliceerd,
    variants: [{ sku: v.sku, price: v.prijs, compare_at_price: v.vanaf }] })) });
}
const ceOrd = [...lijst('ord'), ...lijst('ord28')].filter(f => f.endsWith('.json')).map(f => { try { return rd(f); } catch { return {}; } });
const seen = new Set(); for (const pg of ceOrd) pg.Content = (pg.Content || []).filter(o => !seen.has(o.Id) && seen.add(o.Id));
const ql = web.map(w => ({ data: {
  d28: { tableData: { rows: fs.existsSync(`ql28/${w.domein}.json`) ? rd(`ql28/${w.domein}.json`) : [] } },
  d365: { tableData: { rows: fs.existsSync(`ql/${w.domein}.json`) ? rd(`ql/${w.domein}.json`) : [] } } } }));
const merk = (() => { const r = fs.readFileSync(new URL('../config/merk-config.template.csv', import.meta.url), 'utf8').split('\n').filter(l => l && !l.startsWith('#')); const h = r[0].split(';'); return r.slice(1).map(l => Object.fromEntries(l.split(';').map((v, i) => [h[i], v]))); })();
const bron = { 'Webshops': web, 'ShopifyQL: voorraad': ql, 'Shopify: orders': shopOrd, 'Shopify: producten': shopProd,
  'CE: orders 53 weken': ceOrd, 'CE: producten (alle maten)': ceProd, 'Merk-config': merk };
globalThis.$ = n => ({ all: () => bron[n].map(json => ({ json })), first: () => ({ json: bron[n][0] }) });
const code = fs.readFileSync(process.argv[2], 'utf8');
const uit = new Function(code)()[0].json;
fs.writeFileSync('radar_js.json', JSON.stringify(uit, null, 1));
console.log('signalen', uit.n_signalen, 'urgent', uit.urgent, 'groei', JSON.stringify(uit.groei));
for (const [i, t] of uit.top10.entries()) console.log(i + 1, t.merk.padEnd(9), t.naam.slice(0, 40).padEnd(40), t.collectie.padEnd(11), String(t.verk28).padStart(4), String(t.voorraad).padStart(5), String(t.eerste_leeg ?? '-').padStart(5), t.status);
console.log('--- eerste 10 signalen');
for (const s of uit.signalen.slice(0, 10)) console.log(s.status.padEnd(9), s.naam.slice(0, 40).padEnd(40), s.verk28, 'mis', s.mis_eur, 'vj', s.vj_horizon, 'verw', s.verwacht_horizon, s.sprong ? 'sprong ' + s.sprong + 'x' : '');
