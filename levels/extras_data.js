// Dumps what levels/mkextras.py needs for level N as JSON:  node levels/extras_data.js 2
// Reads pN/data.js (lessons, scripts, qbank, lesson-1 workbook sheet) and pN/parent_side.json. Nothing is computed or invented here.
const path = require('path');
const R = path.join(__dirname, '..');
const N = process.argv[2];
const L = require(path.join(R, 'p' + N, 'data.js'));
const C = require(path.join(R, 'hp', 'common_html.js'));
const H = Object.assign({}, C, { fig: s => '<div class="p img" style="text-align:center">' + s + '</div>' });
const c1 = L.content[0];
console.log(JSON.stringify({
  program: L.program, level: L.level, slogan: L.slogan,
  lessons: L.lessons, qbank: L.qbank, scripts: L.scripts,
  wb1: c1.workbook(H),
  side: require(path.join(R, 'p' + N, 'parent_side.json'))
}));
