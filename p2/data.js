// Assembles the P2 program from p2/content/l1.js … l10.js into the same shapes the P1 builders use.
const path = require('path');
const C = [];
for (let n = 1; n <= 10; n++) C.push(require(path.join(__dirname, 'content', 'l' + n + '.js')));
// Close-the-gaps content (warm-up check, open investigation, reflection): p2/gaps.json, shared with the slide generators.
const GAPS = require('./gaps.json');
C.forEach(c => { const g = GAPS[String(c.lesson.n)]; c.gaps = g; });
// Mathematician stories (one per lesson; docs/stories/final_p2.json, shortened for the child pages): p2/stories.json
const STORIES = require('./stories.json');
module.exports = {
  gaps: GAPS,
  stories: STORIES,
  program: 'Math Inquirers Holiday Program',
  level: 'Level 2',
  slogan: 'Notice it. Test it. Explain why.',
  content: C,
  lessons: C.map(c => c.lesson),                                      // like hp/lessons.js .lessons
  scripts: Object.fromEntries(C.map(c => [c.lesson.n, c.script])),     // like hp/scripts.js
  deck: Object.fromEntries(C.map(c => [String(c.lesson.n), c.deck])),  // like deck/data.js
  qbank: Object.fromEntries(C.map(c => [String(c.lesson.n), c.qbank])) // like hp/qbank.json
};
