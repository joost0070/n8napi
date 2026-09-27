// Mobiele PDP-audit: screenshots + kenmerken. Gebruik: node pdp.js <naam> <url> [maat]
const { chromium, devices } = require('/opt/node22/lib/node_modules/playwright');
const [naam, url, maat] = process.argv.slice(2);
(async () => {
  const browser = await chromium.launch();
  const ctx = await browser.newContext({ ...devices['iPhone 13'], locale: 'nl-NL', timezoneId: 'Europe/Amsterdam' });
  for (const d of ['.tofvel.com', 'tofvel.com', '.sockwell.nl', '.heydude.nl', '.glerups.eu', '.baabuk.com'])
    await ctx.addCookies([{ name: 'localization', value: 'NL', domain: d, path: '/' },
                          { name: 'cart_currency', value: 'EUR', domain: d, path: '/' }]).catch(()=>{});
  const page = await ctx.newPage();
  const r = { naam, url };
  const t0 = Date.now();
  await page.goto(url, { waitUntil: 'load', timeout: 90000 });
  r.load_s = (Date.now() - t0) / 1000;
  await page.waitForTimeout(4000);
  await page.screenshot({ path: `${naam}_1_eerste_scherm_met_popups.png` });
  for (const t of ['Accepteer alles', 'Alles accepteren', 'Accepteren', 'Accept all', 'Accept All', 'Accept', 'Allow all', 'Akkoord', 'Alle akzeptieren', 'OK']) {
    const b = page.getByRole('button', { name: t, exact: true }).first();
    if (await b.isVisible().catch(() => false)) { r.cookieknop = t; await b.click().catch(()=>{}); break; }
  }
  for (const t of ['Netherlands - EUR', 'Nederland']) {
    const b = page.getByText(t, { exact: true }).first();
    if (await b.isVisible().catch(() => false)) { await b.click().catch(()=>{}); await page.waitForTimeout(2500); break; }
  }
  for (const sel of ['[aria-label*="close" i]', '[aria-label*="sluit" i]', 'button.needsclick[aria-label]']) {
    const b = page.locator(sel).first();
    if (await b.isVisible().catch(() => false)) await b.click().catch(()=>{});
  }
  await page.keyboard.press('Escape').catch(()=>{});
  await page.waitForTimeout(1500);
  await page.screenshot({ path: `${naam}_2_eerste_scherm.png` });
  await page.screenshot({ path: `${naam}_4_volledig.png`, fullPage: true });
  const perf = await page.evaluate(() => {
    const res = performance.getEntriesByType('resource');
    const hosts = new Set(res.map(x => { try { return new URL(x.name).host } catch { return '' } }));
    return { requests: res.length, kb: Math.round(res.reduce((a, x) => a + (x.transferSize || 0), 0) / 1024),
             hosts: hosts.size };
  });
  Object.assign(r, perf);
  r.lcp_s = await page.evaluate(() => new Promise(res => {
    let v = 0; new PerformanceObserver(l => { for (const e of l.getEntries()) v = e.startTime; })
      .observe({ type: 'largest-contentful-paint', buffered: true });
    setTimeout(() => res(Math.round(v) / 1000), 500);
  }));
  const tekst = await page.evaluate(() => document.body.innerText);
  r.tekst = tekst;
  const zoek = (re) => (tekst.match(re) || [null])[0];
  r.maatgids = zoek(/(maat(tabel|gids|advies|informatie)|size (guide|chart)|sizing|größentabelle|pasvorm)/i);
  r.levertijd = zoek(/(vandaag besteld[^\n]*|morgen in huis[^\n]*|voor \d+[:.]\d+ besteld[^\n]*|delivery[^\n]{0,40}days|ship[^\n]{0,30}(days|within)[^\n]*|werkdag[^\n]*)/i);
  r.retour = zoek(/(\d+ dagen[^\n]{0,30}(retour|bedenktijd)|gratis retour[^\n]*|free returns[^\n]*|retourneren[^\n]{0,40})/i);
  r.verzending = zoek(/(gratis verzending[^\n]*|free shipping[^\n]*|verzendkosten[^\n]*)/i);
  r.reviews = zoek(/(\d[,.]\d+\s*\(\d+\)|\d+ reviews|\d+ beoordelingen)/i);
  const knop = page.locator('button[name="add"], form[action*="/cart/add"] button[type="submit"], button:has-text("winkelmand"), button:has-text("Add to cart")').first();
  const bb = await knop.boundingBox().catch(() => null);
  r.knop_y_px = bb ? Math.round(bb.y) : null; r.scherm_h = page.viewportSize().height;
  r.knop_schermen = bb ? +(bb.y / r.scherm_h).toFixed(1) : null;
  // sticky knop? scroll ver naar beneden en kijk of er een zichtbare koopknop in beeld is
  await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight * 0.6));
  await page.waitForTimeout(1200);
  r.sticky_knop = await page.evaluate(() => [...document.querySelectorAll('button, a')].some(b => {
    const s = getComputedStyle(b); const q = b.getBoundingClientRect();
    return /winkel|cart|bestel|add|kaufen|toevoegen/i.test(b.innerText) && q.top >= 0 && q.bottom <= innerHeight && q.height > 20;
  }));
  await page.screenshot({ path: `${naam}_3_gescrold.png` });
  require('fs').writeFileSync(`${naam}.json`, JSON.stringify(r, null, 1));
  const { tekst: _, ...kort } = r; console.log(JSON.stringify(kort));
  await browser.close();
})().catch(e => { console.log(naam, 'FOUT', String(e).slice(0, 300)); process.exit(0); });
