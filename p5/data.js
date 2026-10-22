// Assembles the P5 program from p5/content/l1.js … l10.js into the same shapes the P1 builders use.
const path = require('path');
const C = [];
for (let n = 1; n <= 10; n++) C.push(require(path.join(__dirname, 'content', 'l' + n + '.js')));
const GAPS = require(path.join(__dirname, 'content', 'gaps.js'));

// ---- the one timeline used by decks, scripts, guide and workbook (minutes) ----
const TIMELINE = [
  ['0–3', 'Sneak-peek puzzles', 'Two puzzles on ideas we have not learnt yet. Answers shown privately. Nobody is marked.'],
  ['3–9', 'Warm-up', 'A quick game, then the quick questions.'],
  ['9–21', 'Explore', 'Hands-on in pairs. Objects first. A second what-if question is on the slide for anyone who wants more.'],
  ['21–33', 'Mini-lesson', 'Worked examples with click-to-reveal steps, and your-turn questions.'],
  ['33–37', 'Brain break', 'Stand, stretch, drink water.'],
  ['37–49', 'Workbook page 1 (pairs)', 'Start here. After question 3 you may choose: carry on, or try Think harder.'],
  ['49–53', 'Check page 1 together', 'Four minutes, so every part can be explained.'],
  ['53–58', 'Short teaching before page 2', 'One or two worked examples for the page 2 question types.'],
  ['58–72', 'Workbook page 2 (alone)', 'A menu, not a wall: start with the questions named at the top, then choose. Nobody has to finish.'],
  ['72–76', 'Check page 2 together', 'Four minutes.'],
  ['76–82', 'Talk time', 'Pairs talk, volunteers share, then everyone tries the first step of the Investigation. Pass is always allowed.'],
  ['82–86', 'Exit ticket', 'One question on a slip of paper.'],
  ['86–88', 'Reflection (2 minutes)', 'The small box on the Investigation and reflection page. Pass is always allowed.'],
  ['88–90', 'Stamp and goodbye', 'Stamp the inquiry journal. Lesson 10: certificates.']
];

const praise = n => GAPS[n].praise;
const scriptCheck = n => [
  'Minutes 0 to 3. SNEAK-PEEK PUZZLES. Show the two puzzles one at a time. Say: "These are ideas we have not learnt yet. Guessing is welcome and so is \'I do not know\'. Nobody is marked." Puzzle 1 is one that any child can try with objects, drawing or counting, so everybody can start well. Puzzle 2 is a thinking puzzle.',
  'Answers are shown PRIVATELY, never on boards in front of the group. Face to face: children write on their own paper and show it only to you as you walk round. Online: children type the answer in a private chat message to you, or hold the paper up to the camera only if the platform lets only you see it. Do not read answers out with names, do not keep a tally, do not rank. Then ask for VOLUNTEERS to say how they thought (put a hand up or use a reaction); never choose a child because you saw a wrong answer. Never record scores.',
  'Choosing a start: every child has the same neutral line on workbook page 1: "After question 3 you may choose: carry on, or try Think harder." You may quietly invite a child by PRIVATE chat message (never by name in front of the group, and never by announcing who is on which page). Pairs are not split unless BOTH children agree. Any child may swap at any time.'
];
const scriptReflect = n => [
  'Minutes 86 to 88. REFLECTION, 2 minutes, never skipped. Show the exit slip and reflection slide. Children fill in the small box at the bottom of the Investigation and reflection page: "Something I did well", "The hardest part was...", and "What helped me" with tick boxes that include "I asked for help" and "I am still stuck (my tutor will check in privately)". Say: "Pass is always OK. You can write one word, tick a box, type an emoji in the private chat, or write pass."',
  'It is never collected or shown in public. You may read it privately afterwards (or read the private chat) to plan the next lesson and to check in privately with any child who ticked "I am still stuck". Never read a child\'s reflection aloud; only a child who volunteers may share. Praise strategy, not speed: "' + praise(n) + '"' + (n === 10 ? ' This is the last lesson, so a volunteer may say what they would tell a friend starting the program.' : '')
];
const scriptTalk = [
  'Talk-time rules: say "You may say pass." Ask for VOLUNTEERS first, then invite others only if they want to. No cold-calling by name, no public tallies or rankings, and no "who got it right?" hands.'
];
C.forEach(c => { const n = c.lesson.n, g = GAPS[n];
  c.deck.check = g.sneak; c.deck.whatIf = g.whatIf; c.deck.checkPic = g.pic || null;
  c.script.check = scriptCheck(n); c.script.reflect = scriptReflect(n); c.script.talkRules = scriptTalk;
  c.lesson.solo = g.solo; c.investigation = g.inv; });
module.exports = {
  program: 'Math Inquirers Holiday Program',
  level: 'Primary 5',
  slogan: 'Notice it. Test it. Explain why.',
  timeline: TIMELINE,
  content: C,
  lessons: C.map(c => c.lesson),                                      // like hp/lessons.js .lessons
  scripts: Object.fromEntries(C.map(c => [c.lesson.n, c.script])),     // like hp/scripts.js
  deck: Object.fromEntries(C.map(c => [String(c.lesson.n), c.deck])),  // like deck/data.js
  qbank: Object.fromEntries(C.map(c => [String(c.lesson.n), c.qbank])) // like hp/qbank.json
};
