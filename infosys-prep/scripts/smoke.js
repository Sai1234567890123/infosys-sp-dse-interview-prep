const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--no-sandbox'] });
  const p = await b.newPage();
  const errs = [];
  p.on('pageerror', e => errs.push(e.message));
  await p.goto('file:///mnt/project-files/infosys-prep/website/index.html');
  await p.waitForTimeout(800);
  console.log('stat cards:', await p.$$eval('#stats .card b', els => els.map(e => e.textContent).join(' ')));
  console.log('inf count:', await p.textContent('#inf-count'));
  console.log('pattern rows:', await p.$$eval('#patterns tbody tr', r => r.length));
  await p.click('nav.tabs button[data-tab="cf"]');
  console.log('cf count:', await p.textContent('#cf-count'));
  await p.click('nav.tabs button[data-tab="top"]');
  console.log('top items:', await p.$$eval('#top-list details', r => r.length));
  console.log('errors:', errs.length ? errs : 'none');
  await b.close();
})().catch(e => { console.error('FAILED', e.message); process.exit(1); });
