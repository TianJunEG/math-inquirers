// Runs every Lesson 7 drawing from make_l7_sizes.py in the real Scratch editor and checks that the turtle stays on the
// stage (the editor fences a sprite at the stage edge, which would break a closed shape), comes home when the turns
// add up to a whole number of full turns, and that the real extents equal the maths (a turtle simulation).
// Usage: PW=.../playwright node verify/l7_sizes_check.js <outdir>
const path = require('path'), fs = require('fs'), cp = require('child_process');
const { chromium } = require(process.env.PW || 'playwright');
const OUT = process.argv[2] || '/tmp/l7_sizes'; fs.mkdirSync(OUT, { recursive: true });
const sb3 = path.join(OUT, 'L7_sizes_test.sb3');
const rows = JSON.parse(cp.execFileSync('python3', [path.join(__dirname, 'make_l7_sizes.py'), sb3]).toString());
const proxy = process.env.HTTPS_PROXY ? { server: process.env.HTTPS_PROXY.replace(/^(https?:\/\/)[^@]*@/, '$1') } : undefined;
const sleep = ms => new Promise(r => setTimeout(r, ms));
const rad = d => d * Math.PI / 180;
function sim(r) {
  let [x, y] = r.start, dir = 90, minx = x, maxx = x, miny = y, maxy = y;
  const reps = r.rosette ? 48 : r.n; // rosette: 12 x 4 moves
  for (let i = 0; i < r.n; i++) {
    const inner = r.rosette ? 4 : 1;
    for (let k = 0; k < inner; k++) {
      x += r.move * Math.sin(rad(dir)); y += r.move * Math.cos(rad(dir));
      dir += r.rosette ? 90 : r.turn;
      minx = Math.min(minx, x); maxx = Math.max(maxx, x); miny = Math.min(miny, y); maxy = Math.max(maxy, y);
    }
    if (r.rosette) dir += r.turn;
  }
  return { x, y, dir: ((dir % 360) + 360) % 360, minx, maxx, miny, maxy };
}
(async () => {
  const b = await chromium.launch({ proxy });
  const pg = await (await b.newContext({ viewport: { width: 1400, height: 900 } })).newPage();
  pg.on('dialog', d => d.accept());
  await pg.goto('https://scratch.mit.edu/projects/editor/', { waitUntil: 'domcontentloaded', timeout: 90000 });
  await pg.waitForSelector('[class*="menu-bar_menu-bar-item"]', { timeout: 90000 });
  await pg.waitForFunction(() => {
    for (const el of document.querySelectorAll('div')) { const k = Object.keys(el).find(k => k.startsWith('__reactFiber$')); if (!k) continue; let f = el[k]; while (f) { if (f.memoizedProps && f.memoizedProps.vm) { window.__vm = f.memoizedProps.vm; return true; } f = f.return; } } return false; }, null, { timeout: 90000, polling: 500 });
  await pg.waitForTimeout(2500);
  await pg.click('text=File');
  const [fc] = await Promise.all([pg.waitForEvent('filechooser'), pg.click('text=Load from your computer')]);
  await fc.setFiles(sb3);
  await pg.waitForFunction(() => window.__vm.runtime.targets.some(t => t.getName() === 'Turtle'), null, { timeout: 60000 });
  await pg.waitForTimeout(2500);
  await pg.mouse.click(1100, 760);
  await pg.evaluate(() => {
    const rt = window.__vm.runtime, sp = rt.targets.find(t => t.getName() === 'Turtle');
    window.__t = { min: [1e9, 1e9], max: [-1e9, -1e9] };
    setInterval(() => { const T = window.__t; T.min[0] = Math.min(T.min[0], sp.x); T.max[0] = Math.max(T.max[0], sp.x); T.min[1] = Math.min(T.min[1], sp.y); T.max[1] = Math.max(T.max[1], sp.y); }, 2);
  });
  const res = []; let bad = 0;
  for (const r of rows) {
    await pg.evaluate(() => { window.__t.min = [1e9, 1e9]; window.__t.max = [-1e9, -1e9]; });
    await pg.click('[class*="stage_stage"] canvas', { position: { x: 200, y: 150 } });
    await pg.keyboard.down(r.key); await sleep(120); await pg.keyboard.up(r.key);
    const t0 = Date.now(); let idle = 0;
    while (Date.now() - t0 < 60000) { await sleep(120); const n = await pg.evaluate(() => window.__vm.runtime.threads.length); if (!n) { if (++idle > 3) break; } else idle = 0; }
    const g = await pg.evaluate(() => { const rt = window.__vm.runtime, sp = rt.targets.find(t => t.getName() === 'Turtle'); const v = Object.fromEntries(Object.values(rt.getTargetForStage().variables).map(v => [v.name, v.value])); return { x: sp.x, y: sp.y, dir: sp.direction, v, t: window.__t }; });
    const s = sim(r);
    const closes = Math.abs(s.x - r.start[0]) < 0.5 && Math.abs(s.y - r.start[1]) < 0.5;
    const inStage = s.minx >= -240 && s.maxx <= 240 && s.miny >= -180 && s.maxy <= 180;
    const guiHome = Math.abs(g.x - s.x) < 0.5 && Math.abs(g.y - s.y) < 0.5; // editor ended where the maths says (so no fence moved it)
    const guiExt = Math.abs(g.t.min[0] - s.minx) < 1.5 && Math.abs(g.t.max[0] - s.maxx) < 1.5 && Math.abs(g.t.min[1] - s.miny) < 1.5 && Math.abs(g.t.max[1] - s.maxy) < 1.5;
    const ok = guiHome && guiExt && inStage;
    if (!ok) bad++;
    const row = { key: r.key, label: r.label, closes, simExtent: [Math.round(s.minx), Math.round(s.maxx), Math.round(s.miny), Math.round(s.maxy)], editorEnd: [Math.round(g.x * 10) / 10, Math.round(g.y * 10) / 10], editorExtent: [Math.round(g.t.min[0]), Math.round(g.t.max[0]), Math.round(g.t.min[1]), Math.round(g.t.max[1])], inStage, ok };
    res.push(row); console.log(ok ? 'ok  ' : 'FAIL', JSON.stringify(row));
    if (['d', 'm', 'o', 'p', 'q', 'u'].includes(r.key) || !ok) {
      const st = await pg.$('[class*="stage_stage"] canvas'); await st.screenshot({ path: path.join(OUT, 'stage_' + r.key + '_' + r.label.replace(/[^a-z0-9]+/gi, '_') + '.png') });
    }
  }
  fs.writeFileSync(path.join(OUT, 'l7_sizes.json'), JSON.stringify(res, null, 1));
  console.log(bad ? bad + ' FAILED' : 'ALL L7 DRAWINGS FIT AND RAN IN THE EDITOR');
  await b.close(); process.exit(bad ? 1 : 0);
})().catch(e => { console.log('FATAL', e); process.exit(2); });
