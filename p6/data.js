// Assembles the P6 program from p6/content/l1.js … l10.js into the same shapes the P1 builders use.
const path = require('path');
const C = [];
for (let n = 1; n <= 10; n++) C.push(require(path.join(__dirname, 'content', 'l' + n + '.js')));
const GAPS = require('./content/gaps.json');
C.forEach((c, i) => { const g = GAPS[String(i + 1)]; c.gaps = g; c.lesson.moved = c.moved || []; const mv = c.moved || []; c.lesson.th = c.qbank.stretch.slice(0, 4 - mv.length).concat(mv); });
module.exports = {
  gaps: GAPS,
  program: 'Math Inquirers Holiday Program',
  level: 'Level 6',
  slogan: 'Notice it. Test it. Explain why.',
  content: C,
  lessons: C.map(c => c.lesson),                                      // like hp/lessons.js .lessons
  scripts: Object.fromEntries(C.map(c => [c.lesson.n, c.script])),     // like hp/scripts.js
  deck: Object.fromEntries(C.map(c => [String(c.lesson.n), c.deck])),  // like deck/data.js
  qbank: Object.fromEntries(C.map(c => [String(c.lesson.n), c.qbank])) // like hp/qbank.json
};
