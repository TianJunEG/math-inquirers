// Bridge to the Level 6 workbook's own figure code for lessons 9 and 10 (p6/content/l9.js, l10.js): blocks(), codeFig() (code + list panel), hexChains() and FG.dotPlot().
// Reads a JSON list of requests on stdin, writes a JSON list of results.  Nothing is copied except the two dot-plot specifications (a function cannot cross JSON); they are the
// same numbers as l9.js workbook() Q1 and Q4 (w5lib.py asserts the dot-plot aria labels occur in l9.js).
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
const L = { l9: load('l9.js', ['blocks', 'codeFig', 'codeSvg']), l10: load('l10.js', ['blocks', 'codeSvg', 'hexChains']) };
const FG = require(path.join(root, 'levels', 'figs_l4_6.js'));
const reqs = JSON.parse(fs.readFileSync(0, 'utf8'));
const out = reqs.map(r => {
  switch (r.kind) {
    case 'blocks': { const b = L[r.lesson].__blocks(r.prog, r.fs || 16); return { svg: b.svg, w: b.w, h: b.h }; }
    case 'codefig': return L.l9.__codeFig(r.prog, r.aria, r.list || null);
    case 'hex': return L.l10.__hexChains();
    case 'dot1': return FG.dotPlot({ min: 0, max: 10, data: [4, 7, 2, 8, 9], w: 420, axis: 'books read', label: 'A dot plot of books read: one dot each at 2, 4, 7, 8 and 9 on a scale from 0 to 10.' });
    case 'dot4': return FG.dotPlot({ min: 8, max: 22, data: [10, 12, 12, 15, 16, 20], w: 460, axis: 'dollars a week', fmt: v => '$' + v, tick: 2, extra: (x0, x1, y) => FG.T(x1 + 24, y - 20, '$69 →', { size: 18, anchor: 'end', fill: FG.RED }), label: 'A dot plot of pocket money from $8 to $22: dots at 10, 12 (two), 15, 16 and 20. The seventh pupil, $69, is off the scale to the right.' });
    default: throw new Error('unknown kind ' + r.kind);
  }
});
process.stdout.write(JSON.stringify(out));
