// Assembles the P5 program from p2/content/l1.js … l10.js into the same shapes the P1 builders use.
const path = require('path');
const C = [];
for (let n = 1; n <= 10; n++) C.push(require(path.join(__dirname, 'content', 'l' + n + '.js')));
const GAPS = require(path.join(__dirname, 'content', 'gaps.js'));
C.forEach(c => { const g = GAPS[c.lesson.n];
  c.deck.check = g.check; c.script.check = g.scriptCheck; c.script.reflect = g.scriptReflect; c.investigation = g.inv; });
module.exports = {
  program: 'Math Inquirers Holiday Program',
  level: 'Primary 5',
  slogan: 'Notice it. Test it. Explain why.',
  content: C,
  lessons: C.map(c => c.lesson),                                      // like hp/lessons.js .lessons
  scripts: Object.fromEntries(C.map(c => [c.lesson.n, c.script])),     // like hp/scripts.js
  deck: Object.fromEntries(C.map(c => [String(c.lesson.n), c.deck])),  // like deck/data.js
  qbank: Object.fromEntries(C.map(c => [String(c.lesson.n), c.qbank])) // like hp/qbank.json
};
