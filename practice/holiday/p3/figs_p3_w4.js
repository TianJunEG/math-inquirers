// Level 3 holiday online practice, WEEK 4 (lessons 7 and 8): prints, as JSON, the PRINTED workbook figures and the data they are drawn from, taken from the SAME generator
// functions that draw the printed workbook pages (p3/content/l7.js: grid figures, L-shape, staircase; p3/content/l8.js: angles, shapes, fan, letters, grid lines, window;
// p3/figs_l3.js: the eleven clocks of Lesson 8 Think harder 3).  The content files do not export their helpers, so they are compiled with one extra export line appended
// (the files are not changed).  p3lib_w4.py re-draws the figures larger (one angle, one shape, one letter per card) and checks that its data equals the printed figures.
//   node practice/holiday/p3/figs_p3_w4.js   ->  {printed: {name: svg}, data: {...}}
const Module = require('module'), fs = require('fs'), path = require('path');
const ROOT = path.join(__dirname, '..', '..', '..');
function load(file, names) {
  const full = path.join(ROOT, 'p3', 'content', file);
  const m = new Module(full, null); m.filename = full; m.paths = Module._nodeModulePaths(path.dirname(full));
  m._compile(fs.readFileSync(full, 'utf8') + `\nmodule.exports.__f={${names}};`, full);
  return m.exports.__f;
}
const A = load('l7.js', 'q1Fig,q3Fig,q4Fig,q5Fig,FA,FB,FC,FD');
const B = load('l8.js', 'q1Fig,q2Fig,q3Fig,q4Fig,q5Fig,q6Fig,ANG,exFig');
const FX = require(path.join(ROOT, 'p3', 'figs_l3.js')).FX;
const only = s => { const m = /<svg[\s\S]*<\/svg>/.exec(s); return m ? m[0] : s; };
const printed = {
  l7_q1: A.q1Fig(), l7_q4: A.q3Fig(), l7_q5: A.q4Fig(), l7_q6: A.q5Fig(),
  l8_q1: B.q1Fig(), l8_q2: B.q2Fig(), l8_q3: B.q3Fig(), l8_q4: B.q4Fig(), l8_q5: B.q5Fig(), l8_q6: B.q6Fig(), l8_t3: only(FX['8.t3']())
};
console.log(JSON.stringify({ printed, data: { FA: A.FA, FB: A.FB, FC: A.FC, FD: A.FD, ANG: B.ANG } }));
