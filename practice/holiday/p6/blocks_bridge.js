// Bridge to the Level 6 workbook's own figure generators (p6/content/l1.js, l2.js): reads {kind, ...} requests as a JSON list on stdin, writes a JSON list of svg strings.
// It does not copy the drawing code: it loads the workbook content file and uses its blocks(), sticksSvg() and treesSvg() as printed.
const fs = require('fs'), path = require('path');
const root = path.join(__dirname, '..', '..', '..');
function load(file, names) {
  const src = fs.readFileSync(path.join(root, 'p6', 'content', file), 'utf8');
  const m = { exports: {} };
  new Function('module', 'require', '__dirname', src + '\n;' + names.map(n => `module.__${n}=typeof ${n}==="undefined"?null:${n};`).join(''))(m, require, path.join(root, 'p6', 'content'));
  return m;
}
const l1 = load('l1.js', ['blocks', 'sticksSvg']);
const l2 = load('l2.js', ['treesSvg']);
const reqs = JSON.parse(fs.readFileSync(0, 'utf8'));
const out = reqs.map(r => {
  if (r.kind === 'blocks') return l1.__blocks(r.prog, r.label || 'Code', r.fs || 14);
  if (r.kind === 'sticks') return l1.__sticksSvg();
  if (r.kind === 'trees') return l2.__treesSvg();
  throw new Error('unknown figure kind ' + r.kind);
});
process.stdout.write(JSON.stringify(out));
