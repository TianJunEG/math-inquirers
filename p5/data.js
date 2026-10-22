// Assembles the P5 program from p5/content/l1.js … l10.js into the same shapes the P1 builders use.
const path = require('path');
const C = [];
for (let n = 1; n <= 10; n++) C.push(require(path.join(__dirname, 'content', 'l' + n + '.js')));
const GAPS = require(path.join(__dirname, 'content', 'gaps.js'));
// ---- where the page break really falls: the number of the last question printed on workbook page 1 (2 or 3) ----
const HC = require(path.join(__dirname, '..', 'hp', 'common_html.js'));
const HH = Object.assign({}, HC, { fig: x => '<div class="p img">' + x + '</div>' });
const PAGE_ONE = C.map(c => { let k = 0, broke = false;
  for (const el of c.workbook(HH)) { if (typeof el !== 'string') continue;
    if (el.startsWith('<div class="brk">')) broke = true;
    if (!broke && /class="p q( kn)?"/.test(el)) k++; }
  return k; });
// The line "After question N you may choose" names the last question to DO IN CLASS on page 1: a question printed on page 1 but marked
// take-home (or moved to the page 2 time) in the workbook source ("take-home" / "later" flags) does not count.
const QNUM = /class="p q( kn)?"[^>]*><span class="qn">([^<]*)<\/span>/;
const TAKE_Q = /class="tkq"/;      // a whole question marked take-home (star) or "do it in the page 2 time" in the workbook source
const IN_CLASS_P1 = C.map(c => { let last = 0, broke = false;
  for (const el of c.workbook(HH)) { if (typeof el !== 'string') continue;
    if (el.startsWith('<div class="brk">')) broke = true;
    if (broke) break;
    const m = QNUM.exec(el);
    if (m && !TAKE_Q.test(el)) last = +m[2]; }
  return last; });
const choiceQ = n => IN_CLASS_P1[n - 1];

// ---- the routine table: the part lengths of the ten lessons (p5/budget.json, written by rebuild/p5_budget.py); every lesson adds up to 90 ----
const BUD = require(path.join(__dirname, 'budget.json')).lessons;
const rg = title => { const ds = Object.values(BUD).map(b => { const q = b.parts.find(x => x.title.startsWith(title)); return q ? q.end - q.start : 0; });
  const lo = Math.min(...ds), hi = Math.max(...ds); return lo === hi ? String(lo) : lo + ' to ' + hi; };
const TIMELINE = [
  [rg('Opening'), 'Opening', 'Greet the children, one-paragraph hook, one sentence that the lesson is recorded, read "Today we will...". The opening is inside the 90 minutes.'],
  [rg('Sneak'), 'Sneak-peek puzzles', 'Two puzzles on ideas we have not learnt yet. One hold-up for both puzzles (private), then the answers with one short reason. No volunteer round. Nobody is marked.'],
  [rg('Warm-up'), 'Warm-up', 'One round of a quick game, then four quick questions.'],
  [rg('Explore'), 'Explore', 'Hands-on in pairs. Objects first. 30 seconds of silent thinking, then pair work for 6 minutes at most, then two questions together. A second what-if question is on the slide for any pair that finishes.'],
  [rg('Mini-lesson'), 'Mini-lesson', 'Worked examples with click-to-reveal steps, and short your-turn questions (two items each).'],
  [rg('Brain break'), 'Brain break', 'Stand, stretch, drink water.'],
  [rg('Worksheet page 1'), 'Workbook page 1 (pairs)', 'Start here, the questions without a star. Starred parts are take-home. At the end of the in-class questions you may choose: carry on, or try Think harder.'],
  [rg('Check page 1'), 'Check page 1 together', 'All answers appear; one pair explains the heaviest question, the tutor clicks through the rest.'],
  [rg('Short teaching'), 'Short teaching before page 2', 'Worked examples only for the page 2 questions that stay in class (none in Lesson 5).'],
  [rg('Worksheet page 2'), 'Workbook page 2 (alone)', 'A menu, not a wall: start with the questions named at the top, then choose. Starred parts are take-home. Nobody has to finish.'],
  [rg('Check page 2'), 'Check page 2 together', 'Only the questions that were set in class.'],
  [rg('Talk time'), 'Talk time', '30 seconds of silent thinking, pairs talk 2 minutes, volunteers share 1.5 minutes. Pass is always allowed. The first step of the Investigation is take-home.'],
  [rg('Exit'), 'Exit ticket, reflection, stamp', 'Exit ticket on a slip of paper, a short reflection (pass is always allowed), then the stamp is typed in the chat and goodbye. Lesson 10: certificates.'],
  [rg('Buffer'), 'Buffer (floating time)', 'Not scheduled. It absorbs late arrivals, a mute, a slow breakout. Spend it first if the lesson runs late; do not fill it on purpose.']
];

const praise = n => GAPS[n].praise;
const sneakMins = n => { const q = BUD[String(n)].parts.find(x => x.title.startsWith('Sneak')); return q.end - q.start; };
const scriptCheck = n => [
  'SNEAK-PEEK PUZZLES (about ' + sneakMins(n) + ' minutes). Show the two puzzles one at a time. Say one line only: "Guessing is welcome. Nobody is marked." Puzzle 1 is one that any child can try with objects, drawing or counting, so everybody can start well. Puzzle 2 is a thinking puzzle.',
  'Answers are shown PRIVATELY, never on boards in front of the group. Face to face: children write on their own paper and show it only to you as you walk round. Online: everyone holds their paper up to the camera at the same moment, or shows it to you only, on camera. Do not read answers out with names, do not keep a tally, do not rank. Use ONE hold-up for both puzzles (after puzzle 2, everyone shows their paper at the same moment), then click through the answers and say each one with one short reason. There is NO volunteer round in the sneak-peek; volunteers come in the talk time. Never choose a child because you saw a wrong answer. Never record scores.',
  'Choosing a start: every child has the same neutral line on workbook page 1: "After question ' + choiceQ(n) + ' you may choose: carry on, or try Think harder." (The number is the last question on page 1 of this lesson.) Invite the WHOLE group, never one child: "when you have finished Start here you can choose Think harder, Go further or the Investigation." Never single out a child by name and never announce who is on which page. Pairs are not split unless BOTH children agree. Any child may swap at any time.'
];
const scriptReflect = n => [
  'REFLECTION, about a minute and a half, never skipped (if the clock is behind, make it a one-tick version: pass or one box). Show the exit slip and reflection slide. Children fill in the small box at the bottom of the Investigation and reflection page: "Something I did well", "The hardest part was...", and "What helped me" with tick boxes that include "I asked for help" and "I am still stuck (my tutor will check in with me)". Say: "Pass is always OK. You can write one word, tick a box, or write pass."',
  'It is never collected or shown in public. You may read it privately afterwards to plan the next lesson and to check in with any child who ticked "I am still stuck", in the open session (a quick visit to the shared breakout room or a hand signal, with a parent nearby, never a private message). Never read a child\'s reflection aloud; only a child who volunteers may share. Praise strategy, not speed: "' + praise(n) + '"' + (n === 10 ? ' This is the last lesson, so a volunteer may say what they would tell a friend starting the program.' : '')
];
const scriptTalk = [
  'Protected think time: before anyone speaks, everyone thinks silently for 30 seconds (show the clock). Then pairs talk. This applies to the explore, to the talk question and to any make-up-your-own prompt. The Investigation first step is take-home (or the opener of the next lesson): tell the group so at the end of the talk time.',
  'Talk-time rules: say "You may say pass." Ask for VOLUNTEERS first, then invite others only if they want to. No cold-calling by name, no public tallies or rankings, and no "who got it right?" hands.'
];
C.forEach(c => { const n = c.lesson.n, g = GAPS[n];
  c.deck.check = g.sneak; c.deck.whatIf = g.whatIf; c.deck.checkPic = g.pic || null;
  c.script.check = scriptCheck(n);
  c.script.predict = (c.script.predict || []).concat(['Think for 30 seconds before anyone speaks, and before you touch the objects. Silent thinking. I will show the clock. Then talk with your partner.']); c.script.reflect = scriptReflect(n); c.script.talkRules = scriptTalk;
  c.lesson.solo = g.solo; c.lesson.p1 = g.p1; c.lesson.take = g.take; c.lesson.pose = g.pose; c.investigation = g.inv; });
module.exports = {
  program: 'Math Inquirers Holiday Program',
  level: 'Primary 5',
  slogan: 'Notice it. Test it. Explain why.',
  timeline: TIMELINE,
  pageOne: PAGE_ONE, choiceQ,
  content: C,
  lessons: C.map(c => c.lesson),                                      // like hp/lessons.js .lessons
  scripts: Object.fromEntries(C.map(c => [c.lesson.n, c.script])),     // like hp/scripts.js
  deck: Object.fromEntries(C.map(c => [String(c.lesson.n), c.deck])),  // like deck/data.js
  qbank: Object.fromEntries(C.map(c => [String(c.lesson.n), c.qbank])) // like hp/qbank.json
};
