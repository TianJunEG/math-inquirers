// Assembles the P5 program from p5/content/l1.js … l10.js into the same shapes the P1 builders use.
const path = require('path');
const C = [];
for (let n = 1; n <= 10; n++) C.push(require(path.join(__dirname, 'content', 'l' + n + '.js')));
const GAPS = require(path.join(__dirname, 'content', 'gaps.js'));
const STORIES = require(path.join(__dirname, 'content', 'stories.js'));

// ---- the one timeline used by decks, scripts, guide and workbook (minutes) ----
const TIMELINE = [
  ['0–3', 'Sneak-peek puzzles', 'Two puzzles on ideas we have not learnt yet. Answers shown privately. Nobody is marked.'],
  ['3–9', 'Warm-up', 'A quick game, then the quick questions.'],
  ['9–21', 'Explore', 'Hands-on in pairs. Objects first. A second what-if question is on the slide for anyone who wants more.'],
  ['21–33', 'Mini-lesson', 'Worked examples with click-to-reveal steps, and your-turn questions.'],
  ['33–37', 'Brain break', 'Stand, stretch, drink water. Optional Story break (2 minutes, skippable): a short true story about a mathematician linked to the lesson, with one optional try-it question.'],
  ['37–49', 'Workbook page 1 (pairs)', 'Start here. After the choice question (question 3; question 2 in Lesson 1) you may choose: carry on, or try Think harder.'],
  ['49–53', 'Check page 1 together', 'Four minutes, so every part can be explained.'],
  ['53–58', 'Short teaching before page 2', 'One or two worked examples for the page 2 question types.'],
  ['58–72', 'Workbook page 2 (alone)', 'A menu, not a wall: start with the questions named at the top, then choose. Nobody has to finish. Minutes 62 to 72 are protected open think time (10 quiet minutes) for Think harder, Go further or the Investigation.'],
  ['72–76', 'Check page 2 together', 'Four minutes.'],
  ['76–82', 'Talk time', 'Pairs talk, volunteers share, then everyone tries the first step of the Investigation. Pass is always allowed.'],
  ['82–86', 'Exit ticket', 'One question on a slip of paper.'],
  ['86–88', 'Reflection (2 minutes)', 'The small box on the Investigation and reflection page, including "Next time I will try". Pass is always allowed.'],
  ['88–90', 'Stamp and goodbye', 'Stamp the inquiry journal. Lesson 10: certificates.']
];

const praise = n => GAPS[n].praise;
const scriptCheck = n => [
  'Minutes 0 to 3. SNEAK-PEEK PUZZLES. Show the two puzzles one at a time. Say: "These are ideas we have not learnt yet. Guessing is welcome and so is \'I do not know\'. Nobody is marked." Puzzle 1 is one that any child can try with objects, drawing or counting, so everybody can start well. Puzzle 2 is a thinking puzzle.',
  'Answers are shown PRIVATELY, never on boards in front of the group. Face to face: children write on their own paper and show it only to you as you walk round. Online: everyone holds their paper up to the camera at the same moment, or shows it to you only, on camera. Do not read answers out with names, do not keep a tally, do not rank. Then ask for VOLUNTEERS to say how they thought (put a hand up or use a reaction); never choose a child because you saw a wrong answer. Never record scores.',
  'Choosing a start: every child has the same neutral line on workbook page 1: "After question ' + choiceAfter(n) + ' you may choose: carry on, or try Think harder." Invite the WHOLE group, never one child: "when you have finished Start here you can choose Think harder, Go further or the Investigation." Never single out a child by name and never announce who is on which page. Pairs are not split unless BOTH children agree. Any child may swap at any time.'
];
const CHOICE_AFTER = { 1: 2 };            // the choice line says "After question 2" in Lesson 1, "After question 3" elsewhere
const choiceAfter = n => CHOICE_AFTER[n] || 3;
// What the "I am still stuck" tick means. It is NOT a private contact. n < 10: the follow-up happens in the next lesson, in the open
// session, at a fixed time (minutes 37 to 49, page 1 pair work), in the child's shared breakout room with camera on and a parent nearby.
// Lesson 10 has no next lesson, so the follow-up goes to the parent through the approved parent channel (never to the child).
const stuckTick = n => n < 10 ? 'I am still stuck (we will look at it together next lesson, in class)' : 'I am still stuck (my parent can ask my tutor about it)';
const stuckPlan = n => n < 10
  ? 'FOLLOW-UP FOR "I AM STILL STUCK": it happens in the NEXT lesson, in the open session, at a fixed time: minutes 37 to 49 (page 1 pair work). Visit those children FIRST, in their shared breakout room with the camera on and a parent nearby (face to face: at their table, in the open room), and go through the idea they ticked with one worked example. Before that, in the warm-up (minutes 3 to 9) you may re-teach the most-ticked idea to the whole group. All contact with children stays in the open session.'
  : 'FOLLOW-UP FOR "I AM STILL STUCK": Lesson 10 has no next lesson. At the goodbye (88 to 90) tell the whole group: "if something is still tricky, ask your parent to tell me through the usual parent channel and I will send a worked example to your parent." All contact with children stays in the open session.';
const scriptReflect = n => [
  'Minutes 86 to 88. REFLECTION, 2 minutes, never skipped. Show the exit slip and reflection slide. Children fill in the small box at the bottom of the Investigation and reflection page: "Something I did well", "The hardest part was...", "What helped me" with tick boxes that include "I asked for help" and "' + stuckTick(n) + '", and "Next time I will try ...". Say: "Pass is always OK. You can write one word, tick a box, or write pass."',
  'It is never collected or shown in public. You may read it afterwards to plan the next lesson. Never read a child\'s reflection aloud; only a child who volunteers may share. ' + stuckPlan(n) + ' Praise strategy, not speed: "' + praise(n) + '"' + (n === 10 ? ' This is the last lesson, so a volunteer may say what they would tell a friend starting the program.' : '')
];
const scriptTalk = [
  'Talk-time rules: say "You may say pass." Ask for VOLUNTEERS first, then invite others only if they want to. No cold-calling by name, no public tallies or rankings, and no "who got it right?" hands.'
];
// "Story break" line for the tutor script (brain break, 33 to 37). Optional and skippable; no marking, no cold-calling.
const storyLine = st => 'Story break (optional, 2 minutes): after the stretch and a drink, say "Meet a mathematician: ' + st.short + (st.also ? ' (' + st.also + ')' : '') + ', ' + st.yshort + ', ' + st.cshort + '." Read the story on the slide aloud, slowly (about one minute), or let a volunteer read it. Link to today: ' + st.link + ' Then offer the Try it as an OPTIONAL question: "Have a go in your head or on paper, or just listen. Pass is always fine." Volunteers only, nobody is marked. ANSWER (for you; show it only after children have had a go): ' + st.a + (st.legend ? ' Keep the label: ' + st.legend : '') + ' SKIP IT if you are short of time or the group needs the full break: say "we will skip the story today" and go straight to the workbook at minute 37; nothing else depends on it.';
C.forEach(c => { const n = c.lesson.n, g = GAPS[n];
  c.story = STORIES[n]; c.script.story = storyLine(STORIES[n]);
  c.deck.check = g.sneak; c.deck.whatIf = g.whatIf; c.deck.checkPic = g.pic || null;
  c.script.check = scriptCheck(n); c.script.reflect = scriptReflect(n); c.script.talkRules = scriptTalk;
  c.lesson.solo = g.solo; c.investigation = g.inv; });
module.exports = {
  choiceAfter, stuckTick, stuckPlan, stories: STORIES,
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
