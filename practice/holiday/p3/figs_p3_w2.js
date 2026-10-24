// Level 3 holiday online practice, WEEK 2 (lessons 3 and 4): prints the workbook's own figures as JSON, taken from the SAME generator functions that
// draw the printed workbook pages (p3/content/l3.js: the array of dots; p3/content/l4.js: the bar models of Q1 to Q3; p3/figs_l3.js: the bar models of Lesson 4
// Q4 to Q6, Think harder 1 to 4 and Go further 7).  The content files do not export their figure helpers, so they are compiled with one extra export line
// appended (the files are not changed).
//   node practice/holiday/p3/figs_p3_w2.js   ->  {name: svg string}
const Module = require('module'), fs = require('fs'), path = require('path');
const ROOT = path.join(__dirname, '..', '..', '..');
function load(file, names) {
  const full = path.join(ROOT, 'p3', 'content', file);
  const m = new Module(full, null); m.filename = full; m.paths = Module._nodeModulePaths(path.dirname(full));
  m._compile(fs.readFileSync(full, 'utf8') + `\nmodule.exports.__f={${names}};`, full);
  return m.exports.__f;
}
const A = load('l3.js', 'arraySvg');
const B = load('l4.js', 'q1Fig,q2Fig,q3Fig');
const FX = require(path.join(ROOT, 'p3', 'figs_l3.js')).FX;
// the figure wrapper div of figs_l3.js is dropped: only the <svg> is kept
const only = s => { const m = /<svg[\s\S]*<\/svg>/.exec(s); return m ? m[0] : s; };
const out = {};
out.l3_array = A.arraySvg();
out.l4_q1 = B.q1Fig(); out.l4_q2 = B.q2Fig(); out.l4_q3 = B.q3Fig();
for (const [k, v] of Object.entries({ l4_q4: '4.4', l4_q5: '4.5', l4_q6: '4.6', l4_t1: '4.t1', l4_t2: '4.t2', l4_t3: '4.t3', l4_t4: '4.t4', l4_c7: '4.c7' })) out[k] = only(FX[v]());
// every figure: the root <svg> style is made fluid (full width of the card, never wider than the printed size, height by ratio)
for (const k of Object.keys(out)) {
  out[k] = out[k].replace(/^<svg([^>]*?)style="[^"]*?(?:width:(\d+)px)?[^"]*"/, (m, a, w) => `<svg${a}style="width:100%;max-width:${w || 480}px;height:auto;display:block;margin:0 auto"`);
}
// The lesson builder raises every font so that text is at least 12 px on a 290 px wide phone figure, which makes the row labels ("Ali before",
// "3rd piece") and the end labels ("150 altogether", "475 cm") wider than the printed figure leaves room for. Each figure's viewBox is therefore
// widened on the left and right until every label fits at the raised size (same rule as practice/holiday/hlib.py lift_text: PHONE_PX = 290, MIN_PX = 12).
function widen(svg) {
  const m = /viewBox="(-?[\d.]+) (-?[\d.]+) ([\d.]+) ([\d.]+)"/.exec(svg);
  if (!m) return svg;
  const h = +m[4], base = +m[3];
  const texts = [...svg.matchAll(/<text\b([^>]*)>([^<]*)<\/text>/g)].map(t => ({
    x: +/ x="(-?[\d.]+)"/.exec(t[1])[1], size: +(/font-size="([\d.]+)"/.exec(t[1]) || [0, 16])[1],
    anchor: (/text-anchor="(\w+)"/.exec(t[1]) || [0, 'start'])[1], n: t[2].length }));
  let lo = 0, hi = base;
  for (let it = 0; it < 12; it++) {
    const W = hi - lo, need = Math.round(12 / Math.min(1, 290 / W) * 10) / 10;
    let nlo = 0, nhi = base;
    for (const t of texts) {
      const w = t.n * 0.62 * Math.max(t.size, need) + 6;
      const l = t.anchor === 'end' ? t.x - w : t.anchor === 'middle' ? t.x - w / 2 : t.x, r = t.anchor === 'end' ? t.x : t.anchor === 'middle' ? t.x + w / 2 : t.x + w;
      nlo = Math.min(nlo, l); nhi = Math.max(nhi, r);
    }
    if (nlo === lo && nhi === hi) break;
    lo = Math.floor(nlo); hi = Math.ceil(nhi);
  }
  return svg.replace(/viewBox="[^"]*"/, `viewBox="${lo} 0 ${hi - lo} ${h}"`);
}
for (const k of Object.keys(out)) out[k] = widen(out[k]);
console.log(JSON.stringify(out));
