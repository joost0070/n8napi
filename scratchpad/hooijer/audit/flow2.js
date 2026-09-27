const { chromium, devices } = require('/opt/node22/lib/node_modules/playwright');
(async () => {
  const b = await chromium.launch(); const ctx = await b.newContext({ ...devices['iPhone 13'], locale: 'nl-NL', timezoneId: 'Europe/Amsterdam' });
  const p = await ctx.newPage(); const log = {};
  const weg = async () => {
    for (const t of ['Accepteer alles']) { const k = p.getByRole('button', { name: t, exact: true }).first(); if (await k.isVisible().catch(()=>false)) await k.click(); }
    for (const s of ['[aria-label*="Close" i]', '[aria-label*="sluit" i]', 'button.klaviyo-close-form']) { const k = p.locator(s).first(); if (await k.isVisible().catch(()=>false)) await k.click().catch(()=>{}); }
  };
  await p.goto('https://www.tofvel.com/?country=NL', { waitUntil: 'load', timeout: 90000 }); await p.waitForTimeout(3000); await weg();
  await p.goto('https://www.tofvel.com/products/mula-wolvilt-sloffen-vineyard', { waitUntil: 'load' }); await p.waitForTimeout(7000); await weg(); await p.waitForTimeout(800);
  const titel = p.getByText('TITLE', { exact: true }).first();
  if (await titel.isVisible().catch(()=>false)) { await titel.scrollIntoViewIfNeeded(); await p.evaluate(() => window.scrollBy(0, -150)); }
  await p.waitForTimeout(800); await p.screenshot({ path: 'tofvel_09_vineyard_maten.png' });
  log.vineyard_maten = await p.evaluate(() => [...document.querySelectorAll('input[type=radio]')].filter(i => /^\d+$/.test(i.value)).map(i => i.value + (i.disabled || i.classList.contains('disabled') ? ' (uit)' : '')).join(', '));
  // klik een uitverkochte maat indien aanwezig
  await p.goto('https://www.tofvel.com/collections/alle-pantoffels', { waitUntil: 'load' }); await p.waitForTimeout(3000); await weg();
  await p.screenshot({ path: 'tofvel_03_collectie.png' });
  await p.evaluate(() => window.scrollTo(0, 900)); await p.waitForTimeout(1000); await p.screenshot({ path: 'tofvel_03c_collectie_producten.png' });
  await p.goto('https://www.tofvel.com/products/mula-wolvilt-sloffen-black', { waitUntil: 'load' }); await p.waitForTimeout(3000); await weg();
  const m = p.locator('label').filter({ hasText: /^39$/ }).first(); await m.click().catch(e => log.maatfout = String(e).slice(0,120));
  await p.locator('button[name="add"]').first().click().catch(e => log.addfout = String(e).slice(0,120));
  await p.waitForTimeout(3000); await weg(); await p.screenshot({ path: 'tofvel_10_mand_lade.png' });
  await p.goto('https://www.tofvel.com/checkout', { waitUntil: 'load', timeout: 90000 }); await p.waitForTimeout(6000);
  await p.screenshot({ path: 'tofvel_08_checkout.png' }); await p.screenshot({ path: 'tofvel_08b_checkout_vol.png', fullPage: true });
  log.checkout = (await p.evaluate(() => document.body.innerText)).slice(0, 2500);
  require('fs').writeFileSync('flow2.json', JSON.stringify(log, null, 1)); console.log(JSON.stringify(log, null, 1).slice(0, 3500));
  await b.close();
})();
