// Bridge to the Level 6 workbook's own figure code for lessons 5 and 6 (p6/content/l5.js, l6.js): blocks(), cards(), grid(), spinner() and the two FG.grid() empty tables.
// Reads a JSON list of requests on stdin, writes a JSON list of svg strings.  Nothing is copied: the workbook files are loaded and their functions are called as printed.
const fs = require('fs'), path = require('path'), Module = require('module');
const root = path.join(__dirname, '..', '..', '..');
function load(name, names) {
  const file = path.join(root, 'p6', 'content', name);
  const req = Module.createRequire(file);
  const src = fs.readFileSync(file, 'utf8');
  const m = { exports: {} };
  new Function('module', 'require', '__dirname', src + '\n;' + names.map(n => `module.__${n}=typeof ${n}==="undefined"?null:${n};`).join(''))(m, req, path.dirname(file));
  return m;
}
const L = { l5: load('l5.js', ['blocks', 'cards', 'grid', 'listCode', 'planCode']), l6: load('l6.js', ['blocks', 'spinner', 'coinCode', 'planCode']) };
const FG = require(path.join(root, 'levels', 'figs_l4_6.js'));
const reqs = JSON.parse(fs.readFileSync(0, 'utf8'));
const out = reqs.map(r => {
  const m = L[r.lesson];
  switch (r.kind) {
    case 'blocks': return m.__blocks(r.prog || m['__' + r.named], r.label, r.fs || 15);
    case 'cards': return m.__cards(r.digits);
    case 'grid': return m.__grid();
    case 'spinner': return m.__spinner();
    case 'fggrid': return FG.grid(r.spec);
    case 'prog': return JSON.stringify(m['__' + r.named]);
    default: throw new Error('unknown kind ' + r.kind);
  }
});
process.stdout.write(JSON.stringify(out));
