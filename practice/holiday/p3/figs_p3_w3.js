// Level 3 holiday online practice, WEEK 3 (lessons 5 and 6): prints the workbook's own figures as JSON, taken from the SAME generator functions that
// draw the printed workbook pages (p3/content/l5.js: the 47 counters and 6 plates; p3/content/l6.js: the fraction wall, the five shapes and the partner cards;
// p3/figs_l3.js: the empty bars of Lesson 6 Q5, Think harder 2 to 4 and Go further 6).  The content files do not export their figure helpers, so they are compiled
// with one extra export line appended (the files are not changed).
//   node practice/holiday/p3/figs_p3_w3.js   ->  {name: svg string}
const Module = require('module'), fs = require('fs'), path = require('path');
const ROOT = path.join(__dirname, '..', '..', '..');
function load(file, names) {
  const full = path.join(ROOT, 'p3', 'content', file);
  const m = new Module(full, null); m.filename = full; m.paths = Module._nodeModulePaths(path.dirname(full));
  m._compile(fs.readFileSync(full, 'utf8') + `\nmodule.exports.__f={${names}};`, full);
  return m.exports.__f;
}
const A = load('l5.js', 'shareSvg');
const B = load('l6.js', 'wall,shapes,cards');
const FX = require(path.join(ROOT, 'p3', 'figs_l3.js')).FX;
const only = s => { const m = /<svg[\s\S]*<\/svg>/.exec(s); return m ? m[0] : s; };
const out = {};
out.l5_share = A.shareSvg();
out.l6_wall = B.wall(); out.l6_shapes = B.shapes(); out.l6_cards = B.cards();
for (const [k, v] of Object.entries({ l6_q5: '6.5', l6_t2: '6.t2', l6_t3: '6.t3', l6_t4: '6.t4', l6_c6: '6.c6' })) out[k] = only(FX[v]());
for (const k of Object.keys(out)) {
  out[k] = out[k].replace(/^<svg([^>]*?)style="[^"]*?(?:width:(\d+)px)?[^"]*"/, (m, a, w) => `<svg${a}style="width:100%;max-width:${w || 480}px;height:auto;display:block;margin:0 auto"`);
}
console.log(JSON.stringify(out));
