const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--no-sandbox'] });
  const p = await b.newPage({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true });
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto('file:///mnt/project-files/infosys-prep/website/index.html');
  await p.click('nav.tabs button[data-tab="greedy"]');
  await p.waitForTimeout(300);
  console.log('greedy count:', await p.textContent('#gr-count'));
  await p.locator('#gr-list details').first().locator('summary').click();
  console.log('overflow:', await p.evaluate(() => [document.documentElement.scrollWidth, document.documentElement.clientWidth]));
  console.log('errors:', errs.length ? errs : 'none');
  await b.close();
})().catch(e => { console.error('FAILED', e.message); process.exit(1); });
