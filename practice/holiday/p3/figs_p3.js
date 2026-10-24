// Level 3 holiday online practice: prints the workbook's own figures (taken from the SAME generator functions that draw the printed
// workbook pages in p3/content/l1.js and l2.js) as JSON, including the completed versions used as correct-answer pictures.
//   node practice/holiday/p3/figs_p3.js   ->  {name: svg string}
// The content files do not export their figure helpers, so they are compiled with one extra export line appended (the files are not changed).
const Module = require('module'), fs = require('fs'), path = require('path');
const ROOT = path.join(__dirname, '..', '..', '..');
function load(file, names) {
  const full = path.join(ROOT, 'p3', 'content', file);
  const m = new Module(full, null); m.filename = full; m.paths = Module._nodeModulePaths(path.dirname(full));
  m._compile(fs.readFileSync(full, 'utf8') + `\nmodule.exports.__f={${names}};`, full);
  return m.exports.__f;
}
const A = load('l1.js', 'cardsSvg');
const B = load('l2.js', 'cardsSvg,colsum,magicSvg,pyramid,svg');
const big = (s, w) => s.replace(/max-width:\d+px/, `max-width:${w}px`);
const out = {};
out.l1_cards_3075 = A.cardsSvg(['3', '0', '7', '5'], 300);
out.l2_cards = B.cardsSvg(['1', '2', '3', '4', '5', '6']);
const q1 = (a, b) => B.svg('Two column sums' + (a === '3?47' ? ' with missing digits' : ' completed'), 200,
  B.colsum([a[0], a[1], a[2]], '+', 110, 20, 40, 50, '(a)') + B.colsum([b[0], b[1], b[2]], '−', 410, 20, 40, 50, '(b)'), 520);
out.l2_q1 = q1(['3?47', '25?8', '?025'], ['5?2', '216', '316']);
out.l2_q1_sol = q1(['3447', '2578', '6025'], ['532', '216', '316']);
out.l2_magic = big(B.magicSvg([1200, 1700, 1600, '', 1500, '', '', '', '']), 300);
out.l2_magic_sol = big(B.magicSvg([1200, 1700, 1600, 1900, 1500, 1100, 1400, 1300, 1800]), 300);
const pyr = (a, b) => B.svg('Two number pyramids' + (a.includes('') ? ' with missing bricks' : ' completed'), 340,
  B.pyramid(30, a, '(a)') + '<g transform="translate(0,170)">' + B.pyramid(30, b, '(b)  corner bricks are equal') + '</g>', 310, 310);
out.l2_pyr = pyr([5975, '', 3600, 1250, '', ''], [7000, '', '', '', 2000, '']);
out.l2_pyr_sol = pyr([5975, 2375, 3600, 1250, 1125, 2475], [7000, 3500, 3500, 1500, 2000, 1500]);
const one = v => B.svg('A number pyramid', 160, B.pyramid(30, v, ''), 310, 310);
out.l2_t3 = one([6000, 2650, '', 1200, '', '']);
out.l2_t3_sol = one([6000, 2650, 3350, 1200, 1450, 1900]);
console.log(JSON.stringify(out));
