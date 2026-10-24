// Level 3 holiday online practice, WEEK 5 (lessons 9 and 10): prints, as JSON, the PRINTED workbook figures (and the five small item pictures of Lesson 9 Q3) taken from the SAME
// generator functions that draw the printed workbook pages (p3/figs_l3.js: the ribbon bar, the 24-hour strip, the time lines, the bus line, the bar models of Lesson 9 Think harder 3,
// Go further 5 and 6, the two queues of Lesson 10 Q3; p3/content/l10.js: the drinks bar graph, the matchstick squares and the digit cards).  The lesson files check that the data
// of the figures they redraw (larger, for a phone) equals the data in these printed figures.  The content file does not export its helpers, so it is compiled with one extra
// export line appended (the file is not changed).
//   node practice/holiday/p3/figs_p3_w5.js   ->  {figs: {name: svg}, pics: {item name: svg}}
const Module = require('module'), fs = require('fs'), path = require('path');
const ROOT = path.join(__dirname, '..', '..', '..');
function load(file, names) {
  const full = path.join(ROOT, 'p3', 'content', file);
  const m = new Module(full, null); m.filename = full; m.paths = Module._nodeModulePaths(path.dirname(full));
  m._compile(fs.readFileSync(full, 'utf8') + `\nmodule.exports.__f={${names}};`, full);
  return m.exports.__f;
}
const T = load('l10.js', 'sticks,digitCards,drinksGraph');
const L3 = require(path.join(ROOT, 'p3', 'figs_l3.js'));
const FX = L3.FX;
const only = s => { const m = /<svg[\s\S]*<\/svg>/.exec(s); return m ? m[0] : s; };
const figs = {};
for (const [k, v] of Object.entries({ l9_ribbon: '9.1f', l9_strip: '9.4', l9_q5a: '9.5a', l9_q5b: '9.5b', l9_q5c: '9.5c', l9_q6: '9.6', l9_t2: '9.t2', l9_t3: '9.t3', l9_c5: '9.c5', l9_c6: '9.c6', l10_q3a: '10.3a', l10_q3b: '10.3b' })) figs[k] = only(FX[v]());
figs.l10_sticks = T.sticks(); figs.l10_cards = T.digitCards(); figs.l10_graph = T.drinksGraph();
const pics = {};
for (const n of ['Book', 'Pen set', 'Puzzle', 'Stickers', 'Water bottle']) pics[n] = L3.itemPic3(n);
console.log(JSON.stringify({ figs, pics }));
