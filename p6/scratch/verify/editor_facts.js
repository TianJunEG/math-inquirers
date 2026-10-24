// Facts the 7-point editor check in docs/audit/fixes_p6.md asks for, read from the real Scratch editor:
// block names and colours in the palette (points 1 to 5) and the mod / list behaviour (points 3 and 6).
// Usage: PW=.../playwright node verify/editor_facts.js <outdir>
const path = require('path'), fs = require('fs');
const { chromium } = require(process.env.PW || 'playwright');
const R = path.join(__dirname, '..') + '/';
const OUT = process.argv[2] || '/tmp/editor_facts'; fs.mkdirSync(OUT, { recursive: true });
const proxy = process.env.HTTPS_PROXY ? { server: process.env.HTTPS_PROXY.replace(/^(https?:\/\/)[^@]*@/, '$1') } : undefined;
(async () => {
  const b = await chromium.launch({ proxy });
  const pg = await (await b.newContext({ viewport: { width: 1400, height: 900 } })).newPage();
  pg.on('dialog', d => d.accept());
  await pg.goto('https://scratch.mit.edu/projects/editor/', { waitUntil: 'domcontentloaded', timeout: 90000 });
  await pg.waitForSelector('[class*="menu-bar_menu-bar-item"]', { timeout: 90000 });
  await pg.waitForFunction(() => { for (const el of document.querySelectorAll('div')) { const k = Object.keys(el).find(k => k.startsWith('__reactFiber$')); if (!k) continue; let f = el[k]; while (f) { if (f.memoizedProps && f.memoizedProps.vm) { window.__vm = f.memoizedProps.vm; return true; } f = f.return; } } return false; }, null, { timeout: 90000, polling: 500 });
  await pg.waitForTimeout(2500);
  await pg.click('text=File');
  const [fc] = await Promise.all([pg.waitForEvent('filechooser'), pg.click('text=Load from your computer')]);
  await fc.setFiles(R + 'answers/L8_Code_Machine_ANSWER.sb3');
  await pg.waitForFunction(() => window.__vm.runtime.targets.some(t => t.getName() === 'Friend'), null, { timeout: 60000 });
  await pg.waitForTimeout(2500);
  await pg.mouse.click(1100, 760);
  const facts = {};
  for (const cat of ['Motion', 'Events', 'Control', 'Sensing', 'Operators', 'Variables']) {
    await pg.click(`.blocklyToolboxCategory:has(.blocklyToolboxCategoryLabel:text-is("${cat}"))`); await pg.waitForTimeout(1200);
    await pg.screenshot({ path: path.join(OUT, 'palette_' + cat + '.png'), clip: { x: 0, y: 48, width: 320, height: 852 } });
  }
  // every block in the palette (the flyout is one long list): its words and its colour
  facts.palette = await pg.evaluate(() => {
    const fl = document.querySelector('.blocklyFlyout');
    return [...fl.querySelectorAll('g.blocklyDraggable[data-id]')].filter(g => g.parentElement.classList.contains('blocklyBlockCanvas')).map(g => {
      const path = g.querySelector(':scope > path.blocklyPath');
      const words = [...g.querySelectorAll('text')].filter(t => !t.closest('g.blocklyDraggable[data-shadow-id]')).map(t => t.textContent.trim()).filter(Boolean);
      return { text: words.join(' '), fill: path && path.getAttribute('fill') };
    });
  });
  facts.vm = await pg.evaluate(() => {
    const vm = window.__vm, rt = vm.runtime, P = rt._primitives;
    const out = {};
    out.mod = { 'minus4 mod 26': P.operator_mod({ NUM1: -4, NUM2: 26 }), '41 mod 12': P.operator_mod({ NUM1: 41, NUM2: 12 }), 'minus1 mod 26': P.operator_mod({ NUM1: -1, NUM2: 26 }), '100 mod 26': P.operator_mod({ NUM1: 100, NUM2: 26 }) };
    const stage = rt.getTargetForStage(); const alpha = Object.values(stage.variables).find(v => v.name === 'alphabet');
    const util = { target: rt.targets.find(t => t.getName() === 'Friend') };
    util.target.lookupVariableByNameAndType = (n, t) => Object.values(stage.variables).find(v => v.name === n && v.type === t);
    out.itemNumUpper = P.data_itemnumoflist({ ITEM: 'C', LIST: { name: 'alphabet', id: alpha.id } }, util);
    out.itemNumLower = P.data_itemnumoflist({ ITEM: 'c', LIST: { name: 'alphabet', id: alpha.id } }, util);
    out.itemNumSpace = P.data_itemnumoflist({ ITEM: ' ', LIST: { name: 'alphabet', id: alpha.id } }, util);
    out.itemOf27 = P.data_itemoflist({ INDEX: 27, LIST: { name: 'alphabet', id: alpha.id } }, util);
    out.hasTurnLeft = !!P.motion_turnleft; out.hasPenClear = !!P.pen_clear;
    out.version = (navigator.userAgent);
    return out;
  });
  fs.writeFileSync(path.join(OUT, 'editor_facts.json'), JSON.stringify(facts, null, 1));
  console.log(JSON.stringify(facts.vm)); console.log(facts.palette.length, 'palette blocks');
  await b.close();
})().catch(e => { console.log('FATAL', e); process.exit(2); });
