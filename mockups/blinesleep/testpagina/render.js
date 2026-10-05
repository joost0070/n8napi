// Lokale renderer: rendert de echte Dawn-bestanden van Bline met liquidjs en de echte productdata.
// Gebruik: node render.js <themadir> <uitdir>
const fs = require('fs');
const path = require('path');
const { Liquid } = require('liquidjs');

const THEME = path.resolve(process.argv[2] || 'theme');
const OUT = path.resolve(process.argv[3] || 'site');
fs.mkdirSync(OUT, { recursive: true });
const EXTRA = path.resolve(__dirname, 'extra');

const stripHeader = (s) => s.slice(s.indexOf('{'));
const readJSON = (p) => JSON.parse(stripHeader(fs.readFileSync(p, 'utf8')));
const DATA = JSON.parse(fs.readFileSync(path.join(__dirname, process.env.DATA || 'data.json'), 'utf8'));
const LOCALE = readJSON(path.join(THEME, 'locales/nl.json'));
const LOCALE_EN = readJSON(path.join(THEME, 'locales/en.default.json'));
const SETTINGS_DATA = readJSON(path.join(THEME, 'config/settings_data.json'));

// ---------- kleuren ----------
class Color {
  constructor(hex) {
    hex = (hex || '#000000').replace('#', '');
    if (hex.length === 3) hex = hex.split('').map((c) => c + c).join('');
    this.red = parseInt(hex.slice(0, 2), 16); this.green = parseInt(hex.slice(2, 4), 16); this.blue = parseInt(hex.slice(4, 6), 16);
    this.alpha = 1.0; this.hex = '#' + hex.toLowerCase();
    this.rgb = `${this.red} ${this.green} ${this.blue}`;
  }
  toString() { return this.hex; }
  toJSON() { return this.hex; }
}
const isHex = (v) => typeof v === 'string' && /^#[0-9a-fA-F]{3,6}$/.test(v);
function hsl(c) {
  let r = c.red / 255, g = c.green / 255, b = c.blue / 255;
  const max = Math.max(r, g, b), min = Math.min(r, g, b); let h, s, l = (max + min) / 2;
  if (max === min) { h = s = 0; } else {
    const d = max - min; s = l > 0.5 ? d / (2 - max - min) : d / (max + min);
    h = max === r ? (g - b) / d + (g < b ? 6 : 0) : max === g ? (b - r) / d + 2 : (r - g) / d + 4; h /= 6;
  }
  return [h, s, l];
}
function fromHsl(h, s, l) {
  let r, g, b;
  if (s === 0) { r = g = b = l; } else {
    const hue2rgb = (p, q, t) => { if (t < 0) t += 1; if (t > 1) t -= 1; if (t < 1 / 6) return p + (q - p) * 6 * t; if (t < 1 / 2) return q; if (t < 2 / 3) return p + (q - p) * (2 / 3 - t) * 6; return p; };
    const q = l < 0.5 ? l * (1 + s) : l + s - l * s; const p = 2 * l - q;
    r = hue2rgb(p, q, h + 1 / 3); g = hue2rgb(p, q, h); b = hue2rgb(p, q, h - 1 / 3);
  }
  const hx = (x) => Math.round(x * 255).toString(16).padStart(2, '0');
  return new Color('#' + hx(r) + hx(g) + hx(b));
}
const toColor = (v) => (v instanceof Color ? v : new Color(String(v)));

// ---------- fonts ----------
class Font {
  constructor(handle) {
    this.handle = handle; const m = /_([ni])(\d)$/.exec(handle) || [];
    this.family = '"Nunito Sans"'; this.fallback_families = 'sans-serif';
    this.style = m[1] === 'i' ? 'italic' : 'normal'; this.weight = m[2] ? Number(m[2]) * 100 : 400;
    this.system = false;
  }
  toString() { return this.handle; }
}

// ---------- settings ----------
function wrapSettings(obj) {
  const out = {};
  for (const [k, v] of Object.entries(obj)) {
    if (k.startsWith('type_') && k.endsWith('_font')) out[k] = new Font(v);
    else if (isHex(v)) out[k] = new Color(v);
    else out[k] = v;
  }
  return out;
}
const cur = SETTINGS_DATA.current;
const settings = wrapSettings(cur);
settings.color_schemes = Object.entries(cur.color_schemes).map(([id, s]) => ({ id, settings: wrapSettings(s.settings), toString() { return id; } }));
settings.color_schemes_by_id = Object.fromEntries(settings.color_schemes.map((s) => [s.id, s]));
// Shopify-afbeeldingen uit settings (logo, favicon)
const SHOP_IMAGES = {
  'bline-logo.png': { src: 'https://cdn.shopify.com/s/files/1/1112/3965/9859/files/bline-logo.png?v=1791194891', width: 2000, height: 839 },
  'bline-icoon.png': { src: 'https://cdn.shopify.com/s/files/1/1112/3965/9859/files/bline-icoon.png?v=1791194891', width: 512, height: 512 },
};
function shopImage(v) {
  if (typeof v !== 'string' || !v.startsWith('shopify://shop_images/')) return v;
  const name = v.split('/').pop();
  const i = SHOP_IMAGES[name] || { src: 'https://cdn.shopify.com/s/files/1/1112/3965/9859/files/' + name, width: 2048, height: 2048 };
  return mkImage(i.src, i.width, i.height, name);
}
for (const k of Object.keys(settings)) settings[k] = shopImage(settings[k]);

// ---------- afbeeldingen ----------
function mkImage(src, width, height, alt) {
  return { src, width, height, alt: alt || '', aspect_ratio: width && height ? width / height : 1, id: Math.abs(hash(src)), media_type: 'image', presentation: { focal_point: '50.0% 50.0%' }, toString() { return src; } };
}
function hash(s) { let h = 0; for (const c of String(s)) h = (h * 31 + c.charCodeAt(0)) | 0; return h; }
const numId = (gid) => Number(String(gid).split('/').pop());

// ---------- producten ----------
const products = {};
const OUDE = ['leeskussen', 'hoes-leeskussen'];
for (const p of DATA.products.nodes) {
  if (OUDE.includes(p.handle)) continue;
  const media = p.media.nodes.filter((m) => m.image).map((m, i) => {
    const img = mkImage(m.image.url, m.image.width, m.image.height, m.alt);
    return { id: numId(m.id), alt: m.alt, media_type: 'image', position: i + 1, preview_image: img, aspect_ratio: img.aspect_ratio, src: img.src, width: img.width, height: img.height, toString() { return img.src; } };
  });
  const prod = { id: numId(p.id), handle: p.handle, title: p.title, vendor: p.vendor, type: p.productType, url: '/products/' + p.handle,
    description: p.descriptionHtml, content: p.descriptionHtml, media, images: media.map((m) => m.preview_image), featured_media: media[0], featured_image: media[0] && media[0].preview_image,
    available: p.variants.nodes.some((v) => v.availableForSale), tags: [], template_suffix: p.templateSuffix, has_only_default_variant: p.variants.nodes.length === 1 && p.variants.nodes[0].title === 'Default Title', requires_selling_plan: false, selling_plan_groups: [], gift_card: false, 'gift_card?': false,
    quantity_price_breaks_configured: false, 'quantity_price_breaks_configured?': false, collections: [],
    metafields: { bline: Object.fromEntries(p.metafields.nodes.map((m) => [m.key, { value: m.value, type: m.type, toString() { return m.value; } }])) } };
  prod.variants = p.variants.nodes.map((v) => {
    const fm = media.find((m) => v.image && m.preview_image.src.split('?')[0] === v.image.url.split('?')[0]) || media[0];
    return { id: numId(v.id), title: v.title, price: Math.round(Number(v.price) * 100), compare_at_price: v.compareAtPrice ? Math.round(Number(v.compareAtPrice) * 100) : null,
      available: v.availableForSale, sku: v.sku, barcode: v.barcode, inventory_quantity: v.inventoryQuantity, inventory_management: 'shopify', inventory_policy: 'deny',
      options: v.selectedOptions.map((o) => o.value), option1: v.selectedOptions[0] && v.selectedOptions[0].value, name: p.title + ' - ' + v.title,
      featured_media: fm, featured_image: fm && fm.preview_image, image: fm && fm.preview_image, url: prod.url + '?variant=' + numId(v.id), product: null,
      requires_shipping: true, taxable: true, quantity_rule: { min: 1, max: null, increment: 1 }, quantity_price_breaks: [], selling_plan_allocations: [], store_availabilities: [],
      unit_price_measurement: null, weight: 3900, toString() { return String(numId(v.id)); } };
  });
  prod.variants.forEach((v) => (v.product = prod));
  prod.price = Math.min(...prod.variants.map((v) => v.price)); prod.price_min = prod.price; prod.price_max = Math.max(...prod.variants.map((v) => v.price));
  prod.price_varies = prod.price_min !== prod.price_max; prod.compare_at_price = null; prod.compare_at_price_max = 0; prod.compare_at_price_min = 0; prod.compare_at_price_varies = false;
  prod.first_available_variant = prod.variants[0]; prod.selected_variant = null; prod.selected_or_first_available_variant = prod.variants[0];
  prod.options = p.options.map((o) => o.name);
  prod.options_by_name = {};
  prod.options_with_values = p.options.map((o) => {
    const opt = { name: o.name, position: o.position, selected_value: prod.variants[0].options[o.position - 1] };
    opt.values = o.optionValues.map((ov) => {
      const vr = prod.variants.find((v) => v.options[o.position - 1] === ov.name);
      return { name: ov.name, id: hash(o.name + ov.name) & 0xffffff, available: !!(vr && vr.available), selected: opt.selected_value === ov.name, swatch: null,
        variant: vr, product_url: null, toString() { return ov.name; } };
    });
    prod.options_by_name[o.name] = opt;
    return opt;
  });
  prod.__gid = p.id; prod.__collecties = (p.collections ? p.collections.nodes : []).map((c) => c.handle);
  products[p.handle] = prod;
}
// lijst met productreferenties (bline.kleuren) omzetten naar producten
for (const prod of Object.values(products)) {
  const mf = prod.metafields.bline.kleuren;
  if (mf && mf.type === 'list.product_reference') { const ids = JSON.parse(mf.value); mf.value = ids.map((g) => Object.values(products).find((x) => x.__gid === g)).filter(Boolean); }
}
const all_products = products;

// ---------- menus ----------
function mkLink(i) { return { title: i.title, url: i.url, links: (i.items || []).map(mkLink), active: false, child_active: false, current: false, child_current: false, levels: 0, type: 'http_link' }; }
const linklists = {};
for (const m of DATA.menus.nodes) linklists[m.handle] = { handle: m.handle, title: m.title, links: m.items.map(mkLink), levels: 1 };

// ---------- vertalingen ----------
function lookup(obj, key) { return key.split('.').reduce((o, k) => (o == null ? undefined : o[k]), obj); }
function translate(key, args) {
  let v = lookup(LOCALE, key); if (v === undefined) v = lookup(LOCALE_EN, key);
  if (v === undefined) return 'Translation missing: nl.' + key;
  if (typeof v === 'object') { const c = Number(args.count); v = c === 1 ? v.one : v.other; }
  return String(v).replace(/\{\{\s*(\w+)\s*\}\}/g, (_, n) => (args[n] !== undefined ? args[n] : ''));
}

// ---------- engine ----------
const fixSrc = (src) => src.replace(/(\|\s*image_tag:[^}]*?)\|\s*escape(\s*-?\}\})/g, '$1$2').replace(/render block( -?%\})/g, "render '__app_block', block: block$1");
const nfs = require('fs');
const customFs = { exists: async (f) => nfs.existsSync(f), existsSync: (f) => nfs.existsSync(f), readFile: async (f) => fixSrc(nfs.readFileSync(f, 'utf8')), readFileSync: (f) => fixSrc(nfs.readFileSync(f, 'utf8')), resolve: (root, file, ext) => path.resolve(root, file + (path.extname(file) ? '' : ext)), contains: () => true, dirname: path.dirname, sep: path.sep, fallback: () => undefined };
const engine = new Liquid({ fs: customFs, root: [THEME], partials: [path.join(THEME, 'snippets'), EXTRA], extname: '.liquid', strictFilters: false, strictVariables: false, dynamicPartials: true, jekyllInclude: false, ownPropertyOnly: false, outputEscape: undefined, keepOutputType: false, relativeReference: false });
const kw = (args) => { const o = {}; const pos = []; for (const a of args) { if (Array.isArray(a) && a.length === 2 && typeof a[0] === 'string') o[a[0]] = a[1]; else pos.push(a); } return [o, pos]; };
const money = (c) => { const n = Number(c || 0) / 100; return '€' + n.toFixed(2).replace('.', ','); };
const cdn = (src, o) => { if (!src) return ''; src = String(src); const q = []; if (o.width) q.push('width=' + o.width); if (o.height) q.push('height=' + o.height); if (o.crop) q.push('crop=' + o.crop); return q.length ? src + (src.includes('?') ? '&' : '?') + q.join('&') : src; };
const srcOf = (v) => (v == null ? '' : typeof v === 'string' ? v : v.src || (v.preview_image && v.preview_image.src) || String(v));

engine.registerFilter('t', (k, ...a) => translate(String(k), kw(a)[0]));
engine.registerFilter('asset_url', (n) => 'assets/' + n);
engine.registerFilter('asset_img_url', (n) => 'assets/' + n);
engine.registerFilter('shopify_asset_url', (n) => 'assets/' + n);
engine.registerFilter('file_url', (n) => 'assets/' + n);
engine.registerFilter('stylesheet_tag', (u) => `<link href="${u}" rel="stylesheet" type="text/css" media="all" />`);
engine.registerFilter('script_tag', (u) => `<script src="${u}" type="text/javascript"></script>`);
engine.registerFilter('preload_tag', (u) => `<link href="${u}" rel="preload">`);
engine.registerFilter('inline_asset_content', (n) => { try { return fs.readFileSync(path.join(THEME, 'assets', n), 'utf8'); } catch { return ''; } });
engine.registerFilter('money', money);
engine.registerFilter('money_with_currency', (c) => money(c) + ' EUR');
engine.registerFilter('money_without_trailing_zeros', (c) => money(c).replace(',00', ''));
engine.registerFilter('money_without_currency', (c) => money(c).replace('€', ''));
engine.registerFilter('image_url', (v, ...a) => { const s = new String(cdn(srcOf(v), kw(a)[0])); s.__img = (v && typeof v === 'object' && !(v instanceof String)) ? (v.preview_image || v) : (v && v.__img); return s; });
engine.registerFilter('img_url', (v, size) => srcOf(v));
engine.registerFilter('image_tag', (url, ...a) => {
  const [o] = kw(a); const attrs = []; const im = url && url.__img;
  if (im) { if (o.alt === undefined) o.alt = (im.alt || '').replace(/"/g, '&quot;'); if (o.width === undefined && im.width) o.width = im.width; if (o.height === undefined && im.width) o.height = Math.round((o.width / im.width) * im.height); }
  url = String(url);
  const base = String(url).split('?')[0];
  const widths = o.widths ? String(o.widths).split(',').map((s) => s.trim()) : null;
  if (widths) attrs.push(`srcset="${widths.map((w) => `${base}?width=${w} ${w}w`).join(', ')}"`);
  attrs.unshift(`src="${url}"`);
  for (const [k, v] of Object.entries(o)) { if (k === 'widths' || k === 'preload') continue; if (v === false || v == null) continue; attrs.push(`${k}="${v}"`); }
  return `<img ${attrs.join(' ')}>`;
});
engine.registerFilter('placeholder_svg_tag', (n, cls) => `<svg class="${cls || ''}" viewBox="0 0 100 100"></svg>`);
engine.registerFilter('font_face', (f) => {
  const w = f && f.weight ? f.weight : 400; const file = w >= 700 ? 'nunito_n7.woff2' : 'nunito_n4.woff2';
  return `@font-face{font-family:"Nunito Sans";font-weight:${w};font-style:${f && f.style || 'normal'};font-display:swap;src:url("fonts/${file}") format("woff2");}`;
});
engine.registerFilter('font_url', (f) => 'fonts/' + ((f && f.weight >= 700) ? 'nunito_n7.woff2' : 'nunito_n4.woff2'));
engine.registerFilter('font_modify', (f, prop, val) => { const n = Object.assign(Object.create(Font.prototype), f); if (prop === 'weight') n.weight = val === 'bold' ? 700 : val === 'bolder' ? Math.min(900, f.weight + 300) : Number(val) || f.weight; if (prop === 'style') n.style = val; return n; });
engine.registerFilter('color_brightness', (c) => { c = toColor(c); return (c.red * 299 + c.green * 587 + c.blue * 114) / 1000; });
engine.registerFilter('color_lighten', (c, p) => { const [h, s, l] = hsl(toColor(c)); return fromHsl(h, s, Math.min(1, l + p / 100)); });
engine.registerFilter('color_darken', (c, p) => { const [h, s, l] = hsl(toColor(c)); return fromHsl(h, s, Math.max(0, l - p / 100)); });
engine.registerFilter('color_modify', (c) => toColor(c));
engine.registerFilter('color_to_rgb', (c) => { c = toColor(c); return `rgb(${c.red}, ${c.green}, ${c.blue})`; });
engine.registerFilter('json', (v) => { try { return JSON.stringify(v, (k, x) => (k === 'product' ? undefined : x)); } catch { return 'null'; } });
engine.registerFilter('handleize', (s) => String(s || '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, ''));
engine.registerFilter('handle', (s) => String(s || '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, ''));
engine.registerFilter('link_to', (t, u) => `<a href="${u}">${t}</a>`);
engine.registerFilter('within', (u) => u);
engine.registerFilter('structured_data', () => '');
engine.registerFilter('payment_type_svg_tag', (t) => { const n = { ideal: 'iDEAL', bancontact: 'BC', apple_pay: 'Pay', visa: 'VISA', master: 'MC', google_pay: 'GPay', shopify_pay: 'shop', maestro: 'MAE' }[t] || t; return `<svg class="icon icon--full-color" viewBox="0 0 38 24" width="38" height="24" role="img" aria-label="${t}"><rect x=".5" y=".5" width="37" height="23" rx="3" fill="#fff" stroke="#ccc"/><text x="19" y="16" font-size="9" font-family="Arial" font-weight="700" text-anchor="middle" fill="#1F2A37">${n}</text></svg>`; });
engine.registerFilter('default_errors', () => '');
engine.registerFilter('metafield_tag', (m) => String(m && m.value || ''));
engine.registerFilter('metafield_text', (m) => String(m && m.value || ''));
engine.registerFilter('item_count_for_variant', () => 0);
engine.registerFilter('class_list', () => '');
engine.registerFilter('highlight', (s) => s);
engine.registerFilter('format_address', () => '');
engine.registerFilter('time_tag', (d) => { const m = ['januari','februari','maart','april','mei','juni','juli','augustus','september','oktober','november','december']; const x = new Date(d); return `<time datetime="${d}">${x.getUTCDate()} ${m[x.getUTCMonth()]} ${x.getUTCFullYear()}</time>`; });
engine.registerFilter('url_for_vendor', (v) => '/collections/vendors?q=' + v);
engine.registerFilter('url_for_type', (v) => '/collections/types?q=' + v);
engine.registerFilter('customer_login_link', (t) => `<a href="/account/login">${t}</a>`);
engine.registerFilter('payment_terms', () => '');
engine.registerFilter('external_video_url', () => '');
engine.registerFilter('media_tag', () => '');
engine.registerFilter('video_tag', () => '');
engine.registerFilter('model_viewer_tag', () => '');
engine.registerFilter('img_tag', (u) => `<img src="${u}">`);

// Raw-blokken zonder uitvoer
for (const name of ['schema', 'javascript', 'stylesheet', 'doc']) {
  engine.registerTag(name, {
    parse(token, remain) { this.toks = []; let t; while ((t = remain.shift())) { if (t.name === 'end' + name) return; } },
    *render() { return ''; },
  });
}
function blockTag(name, wrap) {
  engine.registerTag(name, {
    parse(token, remain) {
      this.args = token.args; this.tpls = [];
      const stream = this.liquid.parser.parseStream(remain);
      stream.on('tag:end' + name, () => stream.stop()).on('template', (t) => this.tpls.push(t)).on('end', () => { throw new Error('tag ' + name + ' niet gesloten'); });
      stream.start();
    },
    *render(ctx, emitter) {
      const html = yield this.liquid.renderer.renderTemplates(this.tpls, ctx);
      const pre = yield* wrap.call(this, ctx);
      emitter.write(pre[0] + html + pre[1]);
    },
  });
}
blockTag('style', function* () { return ['<style data-shopify>', '</style>']; });
blockTag('paginate', function* () { return ['', '']; });
blockTag('form', function* (ctx) {
  const a = this.args; const type = (/['"]([^'"]+)['"]/.exec(a) || [])[1];
  const pick = (k) => { const m = new RegExp(k + ":\\s*('[^']*'|\"[^\"]*\"|[\\w.\\[\\]-]+)").exec(a); return m ? m[1] : null; };
  const evalArg = function* (expr) { if (!expr) return ''; if (/^['"]/.test(expr)) return expr.slice(1, -1); return yield this.liquid.evalValue(expr, ctx); }.bind(this);
  const id = yield* evalArg(pick('id')); const cls = yield* evalArg(pick('class'));
  const action = { product: '/cart/add', cart: '/cart', contact: '/contact', localization: '/localization', customer: '/contact#contact_form' }[type] || '/' + type;
  const extra = type === 'product' ? '<input type="hidden" name="form_type" value="product" /><input type="hidden" name="utf8" value="✓" />' : '';
  return [`<form method="post" action="${action}" id="${id || ''}" accept-charset="UTF-8" class="${cls || ''}" enctype="multipart/form-data" novalidate="novalidate" data-type="add-to-cart-form">${extra}`, '</form>'];
});

// {% section 'naam' %} en {% sections 'groep' %}
let sectionCounter = 0;
function mkSection(id, data) {
  const blocks = (data.block_order || Object.keys(data.blocks || {})).map((bid) => {
    const b = data.blocks[bid];
    const blk = { id: bid, type: b.type, settings: wrapSettings(b.settings || {}), shopify_attributes: `data-block-id="${bid}"`, disabled: !!b.disabled };
    if (b.type.startsWith('shopify://apps/')) blk.toString = () => '__app_block';
    for (const k of Object.keys(blk.settings)) blk.settings[k] = shopImage(blk.settings[k]);
    if (blk.settings.product && typeof blk.settings.product === 'string') blk.settings.product = products[blk.settings.product];
    if (typeof blk.settings.menu === 'string' && linklists[blk.settings.menu]) blk.settings.menu = linklists[blk.settings.menu];
    return blk;
  }).filter((b) => !b.disabled);
  const s = wrapSettings(data.settings || {});
  for (const k of Object.keys(s)) if (typeof s[k] === 'string' && s[k].startsWith('shopify://pages/')) s[k] = '/pages/' + s[k].slice(16);
  for (const k of Object.keys(s)) { s[k] = shopImage(s[k]); if (k === 'product' && typeof s[k] === 'string') s[k] = products[s[k]]; if (k === 'collection' && typeof s[k] === 'string') s[k] = collections[s[k]]; if ((k === 'menu' || k.endsWith('_menu') || k === 'menu') && typeof s[k] === 'string' && linklists[s[k]]) s[k] = linklists[s[k]]; }
  return { id, settings: s, blocks, block_order: data.block_order, index: ++sectionCounter, location: 'template' };
}
async function renderSection(type, id, data, ctxScope) {
  const file = path.join(THEME, 'sections', type + '.liquid');
  if (!fs.existsSync(file)) return `<!-- sectie ${type} ontbreekt -->`;
  const section = mkSection(id, data);
  const tpl = engine.parse(fixSrc(fs.readFileSync(file, 'utf8')).replace(/render block( %}|s*-?%})/g, "render '__app_block', block: block$1"), file);
  const g = Object.assign({}, ctxScope, { section });
  for (const b of section.blocks) for (const k of Object.keys(b.settings)) if (/liquid/.test(k) && typeof b.settings[k] === 'string') { const src = b.settings[k]; b.settings[k] = { toString() { try { return engine.parseAndRenderSync(src, {}, { globals: Object.assign({}, g, { block: b }) }); } catch (e) { return '<!-- custom_liquid fout: ' + e.message + ' -->'; } } }; }
  for (const k of Object.keys(section.settings)) if (/liquid/.test(k) && typeof section.settings[k] === 'string') { const src = section.settings[k]; section.settings[k] = { toString() { try { return engine.parseAndRenderSync(src, {}, { globals: g }); } catch (e) { return '<!-- custom_liquid fout: ' + e.message + ' -->'; } } }; }
  const html = await engine.render(tpl, {}, { globals: g });
  return `<div id="shopify-section-${id}" class="shopify-section ${data.__cls || ''}">${html}</div>`;
}
let GLOBAL = {};
engine.registerTag('section', {
  parse(token) { this.name = /['"]([^'"]+)['"]/.exec(token.args)[1]; },
  *render(ctx, emitter) {
    const html = yield renderSection(this.name, this.name, { settings: {} }, ctx.getAll());
    emitter.write(html);
  },
});
engine.registerTag('sections', {
  parse(token) { this.name = /['"]([^'"]+)['"]/.exec(token.args)[1]; },
  *render(ctx, emitter) {
    const grp = readJSON(path.join(THEME, 'sections', this.name + '.json'));
    let out = '';
    for (const sid of grp.order) {
      const d = grp.sections[sid]; if (d.disabled) continue;
      const cls = this.name.replace('-group', '') + '-section';
      out += yield renderSection(d.type, `sections--1__${sid}`, Object.assign({ __cls: `section-group-${cls}` }, d), ctx.getAll());
    }
    emitter.write(out);
  },
});

// ---------- collecties ----------
const collections = {};
for (const c of DATA.collections.nodes) { const ps = c.products.nodes.map((n) => products[n.handle]).filter(Boolean); collections[c.handle] = { id: hash(c.handle) & 0xffffff, handle: c.handle, title: c.title, url: '/collections/' + c.handle, description: c.descriptionHtml, products: ps, products_count: ps.length, all_products_count: ps.length, image: null, featured_image: ps[0] && ps[0].media[0] && ps[0].media[0].preview_image, filters: [], sort_options: [], toString() { return c.handle; } }; }
for (const p of Object.values(products)) p.collections = p.__collecties.map((h) => collections[h]).filter(Boolean);
collections.all = { handle: 'all', title: 'Producten', url: '/collections/all', products: Object.values(products), products_count: Object.keys(products).length, filters: [] };

// ---------- winkelwagen ----------
function mkCart(lines) {
  const items = lines.map(([handle, kleur, qty, korting], i) => {
    const p = products[handle]; const v = p.variants.find((x) => x.title === kleur) || p.variants[0];
    const line = v.price * qty; const disc = korting || 0;
    return { id: v.id, key: v.id + ':' + i, index: i + 1, product: p, variant: v, variant_id: v.id, product_id: p.id, title: p.has_only_default_variant ? p.title : p.title + ' - ' + kleur, quantity: qty,
      price: v.price, original_price: v.price, final_price: v.price - disc / qty, original_line_price: line, final_line_price: line - disc, line_price: line - disc,
      url: v.url, image: v.featured_image, options_with_values: p.has_only_default_variant ? [] : [{ name: 'Kleur', value: kleur }], product_has_only_default_variant: p.has_only_default_variant,
      line_level_discount_allocations: disc ? [{ amount: disc, discount_application: { title: 'Extra hoes: €9,99 korting', type: 'automatic' } }] : [], discounts: [], properties: {},
      selling_plan_allocation: null, unit_price_measurement: null, requires_shipping: true, sku: v.sku, vendor: 'Bline', gift_card: false, quantity_rule: { min: 1, max: null, increment: 1 }, has_components: false };
  });
  const total = items.reduce((s, it) => s + it.final_line_price, 0);
  return { items, item_count: items.reduce((s, i) => s + i.quantity, 0), total_price: total, items_subtotal_price: total, original_total_price: items.reduce((s, it) => s + it.original_line_price, 0),
    total_discount: items.reduce((s, it) => s + (it.original_line_price - it.final_line_price), 0), cart_level_discount_applications: [], discount_applications: [], note: '', attributes: {}, requires_shipping: true,
    taxes_included: true, duties_included: false, currency: { iso_code: 'EUR' }, empty: items.length === 0, 'empty?': items.length === 0 };
}

// ---------- pagina's ----------
const routes = { root_url: '/', cart_url: '/cart', cart_add_url: '/cart/add', cart_change_url: '/cart/change', cart_update_url: '/cart/update', search_url: '/search', predictive_search_url: '/search/suggest', account_url: '/account', account_login_url: '/account/login', account_logout_url: '/account/logout', account_register_url: '/account/register', account_addresses_url: '/account/addresses', all_products_collection_url: '/collections/all', collections_url: '/collections', product_recommendations_url: '/recommendations/products' };
const shop = { name: 'BlineSleep.nl', url: 'https://www.blinesleep.nl', domain: 'www.blinesleep.nl', currency: 'EUR', money_format: '€{{amount_with_comma_separator}}', customer_accounts_enabled: true, customer_accounts_optional: true,
  enabled_payment_types: ['ideal', 'bancontact', 'apple_pay', 'google_pay', 'visa', 'master', 'shopify_pay', 'maestro'], shipping_policy: { body: '<p>x</p>', url: '/policies/shipping-policy', title: 'Verzendbeleid' }, refund_policy: { body: 'x', url: '/policies/refund-policy' }, brand: { logo: null }, metafields: {}, accepts_gift_cards: false, published_locales: [{ iso_code: 'nl', primary: true }] };

async function renderPage({ template, out, pageType, extraScope, title, cartLines }) {
  sectionCounter = 0;
  const tjson = readJSON(path.join(THEME, 'templates', template + '.json'));
  const cart = mkCart(cartLines || []);
  const scope = Object.assign({ settings, shop, routes, linklists, collections, all_products, products, cart, request: { page_type: pageType, design_mode: false, visual_preview_mode: false, locale: { iso_code: 'nl', primary: true }, host: 'www.blinesleep.nl', origin: 'https://www.blinesleep.nl', path: extraScope.__path || '/' },
    localization: { available_countries: [], available_languages: [], country: { iso_code: 'NL' }, language: { iso_code: 'nl' } }, template: { name: template.split('.')[0], suffix: template.split('.')[1] || null, directory: null, toString() { return template; } },
    canonical_url: 'https://www.blinesleep.nl' + (extraScope.__path || '/'), page_title: title, page_description: '', content_for_header: '', current_page: 1, powered_by_link: '', customer: null, blogs: {}, pages: {}, scripts: {}, additional_checkout_buttons: false, content_for_additional_checkout_buttons: '' }, extraScope);
  let content = '';
  for (const sid of tjson.order) {
    const d = tjson.sections[sid]; if (d.disabled) continue;
    content += await renderSection(d.type, `template--1__${sid}`, d, scope);
  }
  scope.content_for_layout = `<!-- template ${template} -->` + content;
  const layout = engine.parse(fixSrc(fs.readFileSync(path.join(THEME, 'layout/theme.liquid'), 'utf8')));
  let html = await engine.render(layout, {}, { globals: scope });
  html = html.replace('<head>', '<head><base href="./">');
  html = html.replace(/<script type="module">\s*import \* as StandardEvents[\s\S]*?<\/script>/, '<script>window.StandardEvents={createViewEventElement:(B=HTMLElement)=>class extends B{dispatchViewEvent(){}}};class VE extends HTMLElement{dispatchViewEvent(){}};customElements.define("collection-component",class extends VE{});customElements.define("product-component",class extends VE{});</script>');
  fs.writeFileSync(path.join(OUT, out), html);
  return html;
}

module.exports = { renderPage, products, engine };

if (require.main === module) {
  (async () => {
    // assets en afbeeldingen lokaal klaarzetten
    fs.mkdirSync(path.join(OUT, 'assets'), { recursive: true });
    for (const f of fs.readdirSync(path.join(THEME, 'assets'))) fs.copyFileSync(path.join(THEME, 'assets', f), path.join(OUT, 'assets', f));
    fs.cpSync(path.join(__dirname, 'site/fonts'), path.join(OUT, 'fonts'), { recursive: true });
    const P = products['leeskussen-beige'];
    const pages = (process.argv[4] || 'product,home,hoes,collection,page,article,blog').split(',');
    const LK = '/products/leeskussen-beige';
    if (pages.includes('product')) await renderPage({ template: 'product', out: 'product.html', pageType: 'product', title: P.title, extraScope: { product: P, __path: LK }, cartLines: [['leeskussen-beige', 'Default Title', 1]] });
    if (pages.includes('product')) await renderPage({ template: 'product', out: 'product_lade_leeg.html', pageType: 'product', title: P.title, extraScope: { product: P, __path: LK }, cartLines: [] });
    if (pages.includes('product')) await renderPage({ template: 'product', out: 'product_lade_bundel.html', pageType: 'product', title: P.title, extraScope: { product: P, __path: LK }, cartLines: [['leeskussen-beige', 'Default Title', 1], ['hoes-wit', 'Default Title', 1, 999]] });
    for (const k of ['wit', 'blauw', 'grijs', 'zwart']) if (pages.includes('product')) await renderPage({ template: 'product', out: 'product_' + k + '.html', pageType: 'product', title: products['leeskussen-' + k].title, extraScope: { product: products['leeskussen-' + k], __path: '/products/leeskussen-' + k }, cartLines: [['leeskussen-' + k, 'Default Title', 1]] });
    if (pages.includes('hoes')) await renderPage({ template: 'product.hoes', out: 'hoes.html', pageType: 'product', title: products['hoes-blauw'].title, extraScope: { product: products['hoes-blauw'], __path: '/products/hoes-blauw' } });
    if (pages.includes('home')) await renderPage({ template: 'index', out: 'home.html', pageType: 'index', title: 'BlineSleep.nl', extraScope: { __path: '/' }, cartLines: [['leeskussen-beige', 'Default Title', 1]] });
    if (pages.includes('collection')) await renderPage({ template: 'collection', out: 'collection.html', pageType: 'collection', title: 'Leeskussens', extraScope: { collection: collections.leeskussens, __path: '/collections/leeskussens' } });
    if (pages.includes('collection')) await renderPage({ template: 'collection', out: 'collection_hoezen.html', pageType: 'collection', title: 'Hoezen', extraScope: { collection: collections.hoezen, __path: '/collections/hoezen' } });
    if (pages.includes('page')) {
      const pg = DATA.pages.nodes.find((x) => x.handle === 'over-bline');
      const tpl = pg.templateSuffix && fs.existsSync(path.join(THEME, 'templates', 'page.' + pg.templateSuffix + '.json')) ? 'page.' + pg.templateSuffix : 'page';
      await renderPage({ template: tpl, out: 'page.html', pageType: 'page', title: pg.title, extraScope: { page: { title: pg.title, handle: pg.handle, url: '/pages/' + pg.handle, content: pg.body }, __path: '/pages/over-bline' } });
    }
    const C = JSON.parse(fs.readFileSync(path.join(__dirname, 'content.json'), 'utf8'));
    const B = C.blogs.nodes[0];
    const mkArt = (a) => ({ id: numId(a.id), handle: a.handle, title: a.title, content: a.body, excerpt: a.summary, excerpt_or_content: a.summary || a.body, url: '/blogs/' + B.handle + '/' + a.handle, published_at: a.publishedAt, created_at: a.publishedAt, author: (a.author && a.author.name) || 'Bline', image: a.image ? mkImage(a.image.url, a.image.width, a.image.height, a.image.altText) : null, comments_count: 0, comments: [], tags: [], comments_enabled: false, 'comments_enabled?': false });
    const arts = B.articles.nodes.map(mkArt);
    const blog = { id: numId(B.id), handle: B.handle, title: B.title, url: '/blogs/' + B.handle, articles: arts, articles_count: arts.length, all_tags: [], tags: [], comments_enabled: false, 'comments_enabled?': false };
    if (pages.includes('blog')) await renderPage({ template: 'blog', out: 'blog.html', pageType: 'blog', title: 'Blog', extraScope: { blog, __path: blog.url } });
    if (pages.includes('article')) { const a = arts.find((x) => x.handle === 'leeskussen-of-extra-kussens'); await renderPage({ template: 'article', out: 'article.html', pageType: 'article', title: a.title, extraScope: { blog, article: a, __path: a.url } }); }
    for (const [h, tpl, out] of [['leeskussen-of-losse-kussens', 'page', 'vergelijking.html'], ['veelgestelde-vragen', 'page.veelgestelde-vragen', 'vragen.html']]) {
      if (!pages.includes('page')) continue; const pg = C.pages.nodes.find((x) => x.handle === h);
      await renderPage({ template: tpl, out, pageType: 'page', title: pg.title, extraScope: { page: { title: pg.title, handle: h, url: '/pages/' + h, content: pg.body }, __path: '/pages/' + h } });
    }
    console.log('klaar');
  })().catch((e) => { console.error(e); process.exit(1); });
}
