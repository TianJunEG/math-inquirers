// Loads every Level 6 Scratch file in the REAL Scratch 3 editor (https://scratch.mit.edu/projects/editor/) in headless
// Chromium (Playwright), the same way a child does: File > Load from your computer. Then it
//   1. static: lists every block opcode and checks it exists in the editor's runtime, checks variable and list
//      references, sprite position, costumes, that every block is drawn in the block workspace, and that no two
//      scripts overlap on screen;
//   2. runs: clicks the green flag (or presses the key) and types the answers, as in cases.js, and checks what the
//      sprite says (the same checks as vm_check.js, but in the editor, which also fences the sprite at the stage edge);
//   3. saves a screenshot of every project.
// Usage:  PW=/path/to/node_modules/playwright node verify/editor_check.js [static|run|both] [outdir]
// Needs outbound HTTPS to scratch.mit.edu (through the proxy in HTTPS_PROXY when there is one).
const path = require('path');
const fs = require('fs');
const { chromium } = require(process.env.PW || 'playwright');
const R = (process.env.ROOT || path.join(__dirname, '..')) + '/';
const MODE = process.argv[2] || 'both';
const OUT = process.argv[3] || '/tmp/editor_check';
fs.mkdirSync(OUT, { recursive: true });
const cases = require(process.env.CASES || './cases.js');
const proxy = process.env.HTTPS_PROXY ? { server: process.env.HTTPS_PROXY.replace(/^(https?:\/\/)[^@]*@/, '$1') } : undefined;
const sleep = ms => new Promise(r => setTimeout(r, ms));

const FIND_VM = () => {
  for (const el of document.querySelectorAll('div')) {
    const k = Object.keys(el).find(k => k.startsWith('__reactFiber$'));
    if (!k) continue;
    let f = el[k];
    while (f) { if (f.memoizedProps && f.memoizedProps.vm) { window.__vm = f.memoizedProps.vm; return true; } f = f.return; }
  }
  return false;
};

async function openEditor(browser, file) {
  const ctx = await browser.newContext({ viewport: { width: 1400, height: 900 } });
  const pg = await ctx.newPage();
  pg.on('dialog', d => d.accept());
  await pg.goto('https://scratch.mit.edu/projects/editor/', { waitUntil: 'domcontentloaded', timeout: 90000 });
  await pg.waitForSelector('[class*="menu-bar_menu-bar-item"]', { timeout: 90000 });
  await pg.waitForFunction(FIND_VM, null, { timeout: 90000, polling: 500 });
  await pg.waitForTimeout(2500);
  await pg.click('text=File');
  const [fc] = await Promise.all([pg.waitForEvent('filechooser'), pg.click('text=Load from your computer')]);
  await fc.setFiles(file);
  await pg.waitForFunction(() => window.__vm && window.__vm.runtime.targets.some(t => t.getName() !== 'Sprite1' && !t.isStage), null, { timeout: 60000, polling: 300 });
  await pg.waitForTimeout(2500);
  await pg.mouse.click(1100, 760); // close the File menu (blank part of the sprite pane)
  await pg.waitForTimeout(300);
  return { ctx, pg };
}

async function staticCheck(pg) {
  return pg.evaluate(() => {
    const vm = window.__vm, rt = vm.runtime;
    const pj = JSON.parse(vm.toJSON());
    const known = new Set([...Object.keys(rt._primitives), ...Object.keys(rt._hats)]);
    const problems = [], opcodes = {}, scripts = {};
    const stage = pj.targets.find(t => t.isStage);
    const stageVars = new Set(Object.keys(stage.variables)), stageLists = new Set(Object.keys(stage.lists)), bc = new Set(Object.keys(stage.broadcasts || {}));
    for (const t of pj.targets) {
      const vars = new Set([...stageVars, ...Object.keys(t.variables)]), lists = new Set([...stageLists, ...Object.keys(t.lists)]);
      let nblocks = 0;
      for (const [id, b] of Object.entries(t.blocks)) {
        if (Array.isArray(b)) continue; // a loose variable reporter
        nblocks++;
        opcodes[b.opcode] = (opcodes[b.opcode] || 0) + 1;
        if (!known.has(b.opcode) && !b.shadow && !/_menu$/.test(b.opcode) && !/^argument_/.test(b.opcode)) problems.push(t.name + ': unknown opcode ' + b.opcode + ' (' + id + ')');
        for (const [fk, fv] of Object.entries(b.fields || {})) {
          if (fk === 'VARIABLE' && !vars.has(fv[1])) problems.push(t.name + ': variable ' + fv[0] + ' not declared (' + id + ')');
          if (fk === 'LIST' && !lists.has(fv[1])) problems.push(t.name + ': list ' + fv[0] + ' not declared (' + id + ')');
          if (fk === 'BROADCAST_OPTION' && !bc.has(fv[1])) problems.push(t.name + ': broadcast ' + fv[0] + ' not declared (' + id + ')');
        }
        for (const iv of Object.values(b.inputs || {})) {
          const a = iv[1];
          if (Array.isArray(a) && a[0] === 12 && !vars.has(a[2])) problems.push(t.name + ': reporter variable ' + a[1] + ' not declared');
          if (Array.isArray(a) && a[0] === 13 && !lists.has(a[2])) problems.push(t.name + ': reporter list ' + a[1] + ' not declared');
        }
      }
      scripts[t.name] = { blocks: nblocks, top: Object.values(t.blocks).filter(b => !Array.isArray(b) && b.topLevel).length };
    }
    const sp = rt.targets.filter(t => !t.isStage).map(t => ({ name: t.getName(), x: t.x, y: t.y, dir: t.direction, size: t.size, visible: t.visible, costumes: t.getCostumes().length, inStage: Math.abs(t.x) <= 240 && Math.abs(t.y) <= 180 }));
    // are all non-shadow blocks drawn, and do top-level scripts overlap?
    const ed = rt.getEditingTarget();
    const ids = new Set([...document.querySelectorAll('[data-id]')].map(e => e.getAttribute('data-id')));
    const missing = Object.entries(ed.blocks._blocks).filter(([id, b]) => !b.shadow && !ids.has(id)).map(([id]) => id);
    const tops = [...document.querySelectorAll('.blocklyBlockCanvas > g.blocklyDraggable')].filter(g => !g.closest('.blocklyFlyout, .blocklyToolboxDiv')).map(g => g.getBoundingClientRect());
    let overlaps = 0;
    for (let i = 0; i < tops.length; i++) for (let j = i + 1; j < tops.length; j++) {
      const a = tops[i], b = tops[j];
      if (a.left < b.right - 2 && b.left < a.right - 2 && a.top < b.bottom - 2 && b.top < a.bottom - 2) overlaps++;
    }
    return { opcodes, scripts, problems, sprites: sp, undrawn: missing.length, topScripts: tops.length, overlaps, lists: Object.fromEntries(Object.values(rt.getTargetForStage().variables).filter(v => v.type === 'list').map(l => [l.name, l.value.length])), extensions: pj.extensions };
  });
}

async function run(pg, trig, answers) {
  await pg.evaluate(() => {
    const vm = window.__vm; window.__said = [];
    if (!window.__sayHook) { window.__sayHook = true; vm.runtime.on('SAY', (t, type, text) => window.__said.push(String(text))); }
  });
  const ans = [...answers];
  if (trig === 'flag') await pg.click('img[class*="green-flag"]');
  else {
    await pg.click('canvas[class*="stage"], [class*="stage_stage"] canvas', { position: { x: 200, y: 150 } });
    const key = trig === ' ' ? 'Space' : trig;
    await pg.keyboard.down(key); await sleep(150); await pg.keyboard.up(key);
  }
  const t0 = Date.now(); let idle = 0;
  while (Date.now() - t0 < 90000) {
    await sleep(150);
    const box = await pg.$('[class*="question_question-input"] input, [class*="question_question-container"] input');
    if (box && ans.length) { await box.fill(String(ans.shift())); await box.press('Enter'); await sleep(200); continue; }
    const n = await pg.evaluate(() => window.__vm.runtime.threads.length);
    if (n === 0) { if (++idle > 3) break; } else idle = 0;
  }
  const r = await pg.evaluate(() => {
    const rt = window.__vm.runtime, sp = rt.targets.find(t => !t.isStage);
    return { said: window.__said, x: sp.x, y: sp.y, dir: sp.direction, vars: Object.fromEntries(Object.values(rt.getTargetForStage().variables).map(v => [v.name, v.value])), threads: rt.threads.length };
  });
  return r;
}

async function main() {
  const browser = await chromium.launch({ proxy });
  const only = process.env.ONLY ? new RegExp(process.env.ONLY) : null;
  const files = [...new Set(cases.map(c => c[0]))].filter(f => !only || only.test(f));
  const out = { static: {}, run: [] };
  const queue = [...files];
  const results = {};
  // one editor per file: static check, screenshot, then every behaviour case for that file
  async function worker() {
    while (queue.length) {
      const f = queue.shift(); const name = path.basename(f);
      try {
        const { ctx, pg } = await openEditor(browser, R + f);
        if (MODE !== 'run') {
          out.static[name] = await staticCheck(pg);
          await pg.screenshot({ path: path.join(OUT, name.replace('.sb3', '.png')) });
        }
        await ctx.close();
        if (MODE !== 'static') {
          for (const c of cases.filter(c => c[0] === f)) {
            const e2 = await openEditor(browser, R + f); // a fresh editor for each run, like a child reloading
            try {
              const r = await run(e2.pg, c[1], c[2]);
              const ok = !!c[3](r);
              out.run.push({ file: name, trigger: c[1], answers: c[2], ok, said: r.said.slice(-8), x: r.x, y: r.y, vars: r.vars });
              console.log(ok ? 'ok  ' : 'FAIL', name, '[' + c[1] + ']', JSON.stringify(r.said.slice(-3)));
              if (!ok) await e2.pg.screenshot({ path: path.join(OUT, 'FAIL_' + name + '_' + c[1] + '.png') });
              else if (/L7|L8|L3/.test(name)) await e2.pg.screenshot({ path: path.join(OUT, 'run_' + name.replace('.sb3', '') + '_' + (c[1] === ' ' ? 'space' : c[1]) + '.png') });
            } catch (e) { out.run.push({ file: name, trigger: c[1], ok: false, error: e.message }); console.log('ERR ', name, c[1], e.message); }
            await e2.ctx.close();
          }
        }
      } catch (e) { console.log('ERR load', name, e.message); out.static[name] = { error: e.message }; }
    }
  }
  const N = +(process.env.WORKERS || 4);
  await Promise.all(Array.from({ length: N }, worker));
  fs.writeFileSync(path.join(OUT, 'editor_check.json'), JSON.stringify(out, null, 1));
  const bad = out.run.filter(r => !r.ok).length + Object.values(out.static).filter(s => s.error || (s.problems && s.problems.length) || s.undrawn).length;
  console.log(bad ? bad + ' PROBLEMS' : 'ALL PASSED', '(' + files.length + ' files, ' + out.run.length + ' runs)');
  await browser.close();
  process.exit(bad ? 1 : 0);
}
main().catch(e => { console.log('FATAL', e); process.exit(2); });
