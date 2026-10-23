const C = require('../hp/common.js');
const { fs, D, CW, t, p, cell, tbl, row, gap, footer, page, AlignmentType, BorderStyle, WidthType } = C;
const L = require('./data.js');
const PROG = L.program, SLOGAN = L.slogan;
const BUD = require('./budget.json').lessons;          // the clock of every lesson (rebuild/p4_budget.py writes it)
const fm = x => String(Math.round(x * 10) / 10);
const bp = (n, title) => BUD[n].parts.find(p => p.title === title);
const rg = (a, b) => fm(a) + '–' + fm(b) + ' min';
const to = (a, b) => fm(a) + ' to ' + fm(b);
const dr = (title) => { const d = L.lessons.map(l => { const p = bp(l.n, title); return p.end - p.start; }); const lo = Math.min(...d), hi = Math.max(...d); return lo === hi ? fm(lo) : fm(lo) + ' to ' + fm(hi); };
const G = [];
const S = 21; // body size (10.5pt)
const tx = (s, o = {}) => p(t(s, { size: S, ...o }), { after: o.after === undefined ? 80 : o.after, line: 280 });
const h1 = (s, pb) => p(t(s, { bold: true, size: 32, color: '1F3864' }), { before: 0, after: 100, pb, keepNext: true });
const h2 = (s) => p(t(s, { bold: true, size: 24, color: '1F3864' }), { before: 160, after: 60, keepNext: true });
const bl = (label, text) => p([t(label + '  ', { bold: true, size: S }), t(text, { size: S })], { after: 60, indent: { left: 240 }, line: 280 });
const bu = (s) => p([t('•  ', { size: S }), t(s, { size: S })], { after: 40, indent: { left: 420, hanging: 220 }, line: 280 });
const hd = (s, w) => cell(s, w, { bold: true, fill: 'D9E2F3', size: 20, h: 70 });
const c2 = (s, w, o = {}) => cell(s, w, { size: 20, align: AlignmentType.LEFT, h: 70, ...o });

/* ---------- Title ---------- */
G.push(p(t('PRIMARY 4 HOLIDAY PROGRAM', { bold: true, size: 22, color: '666666' }), { after: 20 }));
G.push(p(t(PROG, { bold: true, size: 52 }), { after: 40 }));
G.push(p(t(SLOGAN, { italics: true, size: 30, color: '1F3864' }), { after: 120 }));
G.push(tx('Program guide for tutors: schedule, lesson routine, ten minute-by-minute lesson scripts with answer keys, a progress tracker and a parent summary. Math Inquirers is online first: every lesson runs live on video; the face-to-face notes are kept for partner centres.'));
G.push(h2('The program at a glance'));
G.push(tbl([2300, 7600], [
  ['Level', 'Ages 9 to 11 (builds on Primary 4 maths). Every child gets the same pages and chooses how far to go'],
  ['Length', '10 lessons of 90 minutes, two a week over the 5 weeks of the holidays'],
  ['Syllabus', 'This level builds on Primary 4 maths and goes beyond it on purpose. Do not describe it as P4-aligned or as covering the MOE syllabus. Lesson 3 (order of operations and brackets) and the unknown-angle items in Lesson 6 are labelled “stretch beyond P4”: they are Primary 5 topics. The compass turns in Lesson 6 are enrichment that the primary syllabus does not list.'],
  ['Group size', 'Up to 8 children per tutor, live online. Pilot with 6. Add a second tutor or helper above 8.'],
  ['Focus', 'Thinking skills: making a list in order, guess and check, drawing a model, working backwards, finding patterns, reasoning and explaining. Not speed drills.'],
  ['The arc of every lesson', 'Start concrete with objects, record in a table, spot the pattern, state the rule, use it (often backwards), then explain why.'],
  ['What children take home', 'A student workbook with an inquiry journal, 10 worksheets and a certificate'],
  ['Before tutors start', 'Every tutor signs the tutor confidentiality agreement before receiving any materials.']
].map(r => row([cell(r[0], 2300, { bold: true, fill: 'F2F2F2', size: 20, align: AlignmentType.LEFT, h: 70 }), c2(r[1], 7600)]))));

G.push(h2('Schedule'));
G.push(tbl([900, 900, 3000, 2400, 2700], [
  row([hd('Week', 900), hd('Lesson', 900), hd('Title', 3000), hd('Topic', 2400), hd('Big idea', 2700)]),
  ...L.lessons.map(l => row([c2('Week ' + l.week + (l.session === 'A' ? 'a' : 'b'), 900, { align: AlignmentType.CENTER }), c2(String(l.n), 900, { align: AlignmentType.CENTER }), c2(l.title, 3000, { bold: true }), c2(l.topic, 2400), c2(l.skills.split(',')[0], 2700)]))
]));
G.push(tx('Suggested pairing: two lessons a week, for example Tuesday and Thursday, or Saturday and Sunday. Keep the same time slot all five weeks.', { before: 60 }));

/* ---------- Routine ---------- */
G.push(h1('The 90-minute lesson routine', true));
G.push(tx('Every lesson uses the same routine so children know what to expect and tutors can prepare quickly.'));
const R = [
  [dr('Opening'), 'Opening', 'Hello and the title slide. Read “Today we will…” aloud and say that the lesson is recorded.', 'Greet each child by name.', 'Greet each child by name. Say what is recorded (the tutor and the screen).'],
  [dr('Sneak-peek puzzles'), 'Sneak-peek puzzles', 'Two puzzles on an idea we have not learnt yet: the first uses objects, a drawing or counting (about 60 seconds), the second is a thinking question (about 90 seconds), then ONE check for both puzzles (children say the answers together on three), then the answers. Guesses and “I do not know” are welcome. Nobody is marked and the answers do not decide who does what.', 'Own paper; say it together on three when the tutor says. Tutor looks only to plan help.', 'Children write on their own paper and say it together on three when the tutor says (nothing is held up to the camera). No private chat.'],
  [dr('Warm-up'), 'Warm-up game and quick questions', 'One short round of the game (about 90 seconds), then three quick questions. Everyone joins in.', 'Sit in a circle or horseshoe.', 'Cameras on. Answers by thumbs, hands or chat.'],
  [dr('Explore (in pairs)'), 'Explore', 'Hands-on in pairs. Objects first, no writing yet. Two debrief questions.', 'Materials box on each table.', 'Each child has their own materials at home. The only breakout of the first half: about 60 seconds each way, closed by a 60-second timer.'],
  [dr('Mini-lesson'), 'Mini-lesson', 'Tutor builds the example on the board, names the rule and asks what stays the same and what changes. At most one optional “your turn” slide and at most three questions.', 'Whiteboard.', 'Shared slide and annotation tool.'],
  [dr('Brain break'), 'Brain break', 'Water and toilet first, then a short movement game. Clock check at the end: more than 1.5 minutes behind means skip the next optional item.', 'A short movement game.', 'Stand up on camera. Count the stretches together.'],
  [dr('Worksheet'), 'Worksheet', 'Page 1 in pairs, check page 1, short teaching, page 2 alone, check page 2. The last 2 to 3 minutes of the page-2 block are the standing buffer: it is spent first if earlier parts overran, then the choice questions, and never the checks, the exit ticket or Looking back. Tutor asks “how do you know?” rather than giving answers. The exact windows are in each lesson script.', 'Printed workbook, tutor circulates.', 'Printed workbook. Child ticks their own page against the answer slide. Nothing is held up to the camera. Tutor checks one or two answers each.'],
  [dr('Talk time'), 'Talk time', 'One minute of pair talk (no breakout: tell the grown-up beside you, or write one sentence), then volunteers share one answer and explain it.', 'Each child shares in turn.', 'Each child unmutes in turn.'],
  [dr('Exit ticket'), 'Exit ticket and stamp', 'One question on a slip of paper. Stamp the inquiry journal.', 'Paper slip, tutor stamps.', 'Child writes the answer on the slip. Nothing is held up to the camera. Tutor stamps the next time or posts it.'],
  [dr('Looking back'), 'Looking back (2 minutes of writing)', 'Children fill in the small “Looking back” box on page 3, a page every child reaches, with a tick-box for one thing they could try next. Write, tick or pass. Nobody is made to share. Never graded or collected. (Lesson 10 ends with 2.5 minutes of certificates and goodbye as a whole group.)', 'Pencil and workbook.', 'Children write on the printed page. Passing is always allowed. A child who ticks “still stuck” gets a check-in in the open session.']
];
G.push(tbl([1100, 1450, 2800, 2150, 2400], [row([hd('Minutes', 1100), hd('Part', 1450), hd('What happens', 2800), hd('Face to face', 2150), hd('Online', 2400)]), ...R.map(r => row([c2(r[0], 1100, { align: AlignmentType.CENTER, bold: true }), c2(r[1], 1450, { bold: true }), c2(r[2], 2800), c2(r[3], 2150), c2(r[4], 2400)]))]));
G.push(h2('The clock in every lesson'));
G.push(tx('Every lesson adds up to 90 minutes. The table gives the minute each part starts. Worksheet windows, slide times and the buffer are in each lesson script, and in the time pill on every slide.'));
{ const ws = [800, 1000, 1000, 1000, 1000, 1000, 1100, 1000, 1000, 1000]; const nm = ['Sneak-peek puzzles', 'Warm-up', 'Explore (in pairs)', 'Mini-lesson', 'Brain break', 'Worksheet', 'Talk time', 'Exit ticket', 'Looking back'];
  G.push(tbl(ws, [row([hd('Lesson', ws[0]), ...['Sneak-peek', 'Warm-up', 'Explore', 'Mini-lesson', 'Break', 'Worksheet', 'Talk time', 'Exit ticket', 'Looking back'].map((h, i) => hd(h, ws[i + 1]))]),
    ...L.lessons.map(l => row([c2(String(l.n), ws[0], { align: AlignmentType.CENTER, bold: true }), ...nm.map((t, i) => c2(fm(bp(l.n, t).start), ws[i + 1], { align: AlignmentType.CENTER }))]))])); }
G.push(tx('Lesson 10 also has Certificates and goodbye, from minute 87.5 to 90.', { before: 60 }));
G.push(h2('Teaching habits that matter'));
['Ask “How do you know?” after every answer, right or wrong.', 'Wait 10 seconds before helping. Let children struggle a little.', 'Praise the thinking (“You checked it two ways”), not just the answer.', 'Let children disagree with each other and settle it with objects or a drawing.', 'If a child finishes early, use the Challenge or Extension question, not extra drill.'].forEach(s => G.push(bu(s)));

G.push(h2('Preparing the materials'));
['Send the workbook PDF to parents one week before. Ask them to print it single-sided and the cut-out pages on card if they can.', 'Cut-outs used: digit, point, sign and bracket cards (Lessons 2, 3, 5, 10), square grid (Lessons 7, 8), dot grid and cube net (Lesson 8), graph grids (Lesson 9), fraction wall (Lesson 4), right-angle testers (Lesson 6), and a paper clock, pizza circles and what-to-bring page (Lessons 4, 6). Children bring a clear plastic 180 degree protractor and a 30 cm ruler for Lesson 6 (a school one is fine; they are cheap to buy). Lesson 6 Q1 asks children to measure with it, and the arms there are drawn short with the instruction to extend them with a ruler. Tutors keep two or three spare protractors.', 'Keep the answer key with the tutor only. Check answers together on screen.', 'Use the shared screen or a digital whiteboard for the mini-lesson table.'].forEach(s => G.push(bu(s)));
G.push(h2('Setting up online'));
['Send parents the workbook and materials list one week before. Needed: the printed workbook and cut-outs, scissors, a ruler, paper and a pencil.', 'Use one approved platform with breakout rooms and screen share. Admit only registered children and never share the link publicly.', 'Ask the parent to sit nearby but not give answers. The camera should show the child’s page and hands.', 'Nothing is held up to the camera. At the end of each lesson children tick their own work against the answer slide. If a child is still stuck, they mark their own look-back page and the parent photographs it for the tutor after class (business WhatsApp), never during the recorded class.', 'Lessons are recorded on the approved platform so that children who miss one can catch up; follow “Recording the lesson” in this guide. Do not make your own recordings or photos. Add a second tutor or helper above 8 children.'].forEach(s => G.push(bu(s)));

G.push(h1('Materials master list', true));
G.push(tbl([900, 2600, 3200, 3200], [row([hd('Lesson', 900), hd('Title', 2600), hd('Face to face', 3200), hd('Online set-up', 3200)]), ...L.lessons.map(l => row([c2(String(l.n), 900, { align: AlignmentType.CENTER, bold: true }), c2(l.title, 2600), c2(l.materials, 3200), c2(l.online, 3200)]))]));

/* ---------- Lesson scripts ---------- */
const DD = L.deck;
const SC = L.scripts;
const QB = L.qbank;
const tag = (s, fill) => cell(s, 1000, { bold: true, fill, size: 18, h: 50, align: AlignmentType.CENTER });
const seg = (time, title) => p([t(time + '   ', { bold: true, size: 22, color: 'FFFFFF' }), t(title, { bold: true, size: 22, color: 'FFFFFF' })], { before: 160, after: 60, keepNext: true, shading: { type: 'clear', fill: '1F3864', color: 'auto' } });
const say = (lines) => lines.forEach((s, i) => G.push(p([t(i === 0 ? 'SAY   ' : '          ', { bold: true, size: 19, color: '1F6F5C' }), t('“' + s.replace(/^[“"]|[”"]$/g, '') + '”', { size: S, italics: true })], { after: 50, indent: { left: 900, hanging: 900 }, line: 280 })));
const doo = (lines) => lines.forEach((s, i) => G.push(p([t(i === 0 ? 'DO     ' : '          ', { bold: true, size: 19, color: '7F6000' }), t(s, { size: S })], { after: 40, indent: { left: 900, hanging: 900 }, line: 280 })));
const REC = require('../levels/reccues.js'); let CURL = null; const SEGS = [];
const rec = (text) => G.push(p([t('REC   ', { bold: true, size: 19, color: '6B3FA0' }), t(text, { size: S, italics: true })], { after: 40, indent: { left: 900, hanging: 900 }, line: 280 }));
// the REC cue reads whole minutes from '0–N': pass cueMin when the minutes a child needs differ from the part length
const pushSeg = (a, b, title, cueMin) => { const time = rg(a, b); G.push(seg(time, title)); const c = REC.cue(title, '0–' + (cueMin || (b - a)), CURL); SEGS.push({ time, title, action: c.action }); rec(c.say); };
const ask = (rows, h1c, h2c) => { G.push(tbl([4600, 5300], [row([hd(h1c || 'Ask', 4600), hd(h2c || 'Expect', 5300)]), ...rows.map(r => row([c2(r[0], 4600), c2(r[1], 5300)]))])); G.push(gap(40)); };
const stuck = (lines) => lines.map(x => String(x).replace(/^Stuck( on [^:]{0,40})?:\s*/i, '')).forEach((s, i) => G.push(p([t(i === 0 ? 'IF STUCK   ' : '                ', { bold: true, size: 19, color: 'A61C00' }), t(s, { size: S })], { after: 40, indent: { left: 1300, hanging: 1300 }, line: 280 })));

G.push(h1('How to use the scripts', true));
G.push(tx('Every lesson below is a minute-by-minute script. The slides match it: one slide or two for each part. You do not have to say the words exactly, but keep the questions, because the questions are what makes children think.'));
G.push(tbl([1500, 8400], [
  ['SAY', 'Words to say aloud, in plain language for 8- and 9-year-olds. Said in your own voice, not read from the page.'],
  ['DO', 'What you do: set up, hand out, show a slide, or move around the room.'],
  ['ASK / EXPECT', 'Questions to put to the group, with the answer you are listening for. Let children answer before you explain.'],
  ['IF STUCK', 'A ladder of help. Give hint 1, wait ten seconds, then give hint 2. Do not give the answer.']
].map(r => row([cell(r[0], 1500, { bold: true, fill: 'F2F2F2', size: 20, align: AlignmentType.LEFT, h: 70 }), c2(r[1], 8400)]))));
G.push(h2('Five habits that run through every script'));
['Predict first. Before children test anything, ask for a guess and write it down. A wrong guess is useful because we can test it.', 'Wait ten seconds after every question. Count silently. Most children answer in the last four.', 'Ask “How do you know?” after right answers too, so that children do not read your face for the answer.', 'Praise the thinking, not the answer: “You checked it two ways” beats “Well done”.', 'When an answer is wrong, say “Let us test that,” and use objects, not “No”.'].forEach(s => G.push(bu(s)));
G.push(h2('Answering a wrong answer'));
ask([
  ['A child gives a wrong answer', '“Thank you. Let us test it with the counters.” Then build it together.'],
  ['A child gives a right answer but cannot explain', '“Show me with your counters.” Then: “Tell your partner how you know.”'],
  ['A child says “I do not know”', '“What do you notice? What could you try first?” Offer hint 1.'],
  ['Two children disagree', '“Both of you, convince the group using objects.” Let the objects decide.']
], 'If…', 'Then…');

G.push(h1('Recording the lesson', true));
G.push(tx(REC.RULES.why));
G.push(h2('How to teach so the recording works'));
REC.RULES.voice.forEach(x => G.push(bu(x)));
G.push(h2('Privacy and consent'));
REC.RULES.privacy.forEach(x => G.push(bu(x)));
G.push(tx('These are suggested working rules. Make sure the parent consent wording, the tutor agreement and the platform settings match them before the first recorded lesson.'));
G.push(h2('After the lesson'));
REC.RULES.upload.forEach(x => G.push(bu(x)));

const SYLL = {
  3: 'Stretch beyond P4. Order of operations and brackets are in the MOE Primary 5 syllabus, not Primary 4, so this lesson is a Primary 5 preview. Never describe it as P4-aligned. The four-operation practice and the “times as many” bar-model problems are on the P4 level; say so if a parent asks.',
  6: 'Measuring and estimating angles with a protractor is a P4 topic. Finding unknown angles (angles in squares and rectangles, angles side by side) is stretch beyond P4: it is Primary 5 in the MOE syllabus. Clock-hand angles and the 8-point compass turns are enrichment: the primary syllabus does not list them. Never describe this lesson as P4-aligned.'
};
L.lessons.forEach(l => {
  CURL = l; SEGS.length = 0;
  const Bn = BUD[l.n], P = (t) => bp(l.n, t), SW = Bn.slide_windows, WB = Bn.worksheet_blocks, BUF = Bn.buffer;
  const ps = (t, title, cueMin) => pushSeg(P(t).start, P(t).end, title, cueMin);
  l = Object.assign({}, l, { gaps: L.content[l.n - 1].gaps });
  const d = DD[String(l.n)], s = SC[l.n], q = QB[String(l.n)];
  G.push(h1('Lesson ' + l.n + ': ' + l.title, true));
  G.push(p(t('Week ' + l.week + (l.session === 'A' ? ' (first lesson)' : ' (second lesson)') + '   •   ' + l.topic + '   •   Workbook: Lesson ' + l.n, { size: 20, color: '666666' }), { after: 80 }));
  G.push(tbl([1900, 8000], [
    ['Objective', l.objective], ...(SYLL[l.n] ? [['Syllabus note', SYLL[l.n]]] : []), ['Thinking skills', l.skills], ['Materials', l.materials], ['Online set-up', l.online],
    ['Prepare', 'Solve the worksheet yourself first. Set out one materials box per pair. Open the slides for this lesson and check the answers in the speaker notes.'],
    ['Watching the recording', 'A child who missed the live lesson watches the recording. They need: ' + l.materials + ' The REC lines tell them when to pause; the chapter list at the end of this lesson shows each part.']
  ].map(r => row([cell(r[0], 1900, { bold: true, fill: 'F2F2F2', size: 20, align: AlignmentType.LEFT, h: 60 }), c2(r[1], 8000, { h: 60 })]))));
  G.push(gap(40));

  ps('Opening', 'Opening');
  say(s.hook);
  doo(['Greet each child by name. Show the lesson title slide. Read “Today we will…” aloud. Keep it to one minute.']);

  ps('Sneak-peek puzzles', 'Sneak-peek puzzles', 3);
  say(['Two sneak-peek puzzles about ' + l.gaps.idea + '. These are ideas we have not learnt yet, so guessing and “I do not know” are welcome. Nobody is marked. Write your answer on your own paper and say it together with everyone on three.']);
  doo(['Show the Sneak-peek puzzles slide. Give about 60 seconds for puzzle 1 and about 90 seconds for puzzle 2. Question 1 uses objects, a drawing or counting, so every child can start. Question 2 is a thinking question. Do not teach and do not say who is right yet.',
    'Answers are shown only to you: each child writes on their own paper and says it together on three (nothing is held up to the camera). Make ONE check for both puzzles, after puzzle 2: children say the answers together on three. Never use private chat or direct messages, and never ask for boards or paper held up in front of the group or to the camera. Walk the group through the answers at the end, using the slide, naming no child, so everyone hears the reasoning.',
    'Use what you see only to plan your help. It does not decide who works on which page. Everyone starts on Start here (page 1) and the invitation is for the WHOLE group: “' + l.gaps.p1 + ' When you have finished Start here you can choose Think harder, Go further or the Investigation.” Never single out or name a child, never announce who is on which page, and do not split a pair unless both children agree. If one child of a pair moves on and the other does not, join the other child to another pair or work with them yourself straight away. Children who choose Think harder or Go further stay in the same room and still join the checks at minutes ' + fm(SW.ws1ans[0]) + ' and ' + fm(SW.ws2ans[0]) + ', talk time, the exit ticket and the reflection.']);
  ask(l.gaps.check.map((x, i) => ['Sneak-peek ' + (i + 1) + (x.kind === 'access' ? ' (objects, drawing or counting)' : ' (thinking)') + ': ' + x.q, x.a]), 'Sneak-peek puzzle', 'Answer');
  doo(['A good reason sounds like: ' + l.gaps.why]);

  ps('Warm-up', 'Warm-up game and quick questions');
  doo([d.warmGame + ' (Today play one short round, about 90 seconds, because the Sneak-peek puzzles came first.)']);
  say(s.warmIntro);
  doo(['After the game, ask the three quick questions on the warm-up slides, about 30 seconds each, with no follow-up questions. Use thumbs or a whisper to partners before taking answers.']);
  ask(d.warmQs.map(x => [x[0], x[1]]));
  if (d.warmWeekly) doo(['Moved to the Weekly Dose of Thinking Math (not asked in class): ' + d.warmWeekly.map(x => x[0] + ' ' + x[1]).join('   ')]);

  ps('Explore (in pairs)', 'Explore (in pairs, with objects)');
  say(s.predict);
  doo(d.expSetup.map((x, i) => (i + 1) + '. ' + x));
  say(['Talk to your partner while you work. I will come round and ask you questions.']);
  stuck(s.exploreHints);
  doo(['Online: this is the only breakout of the first half. Open the rooms for about 60 seconds, and close them with a 60-second auto-close timer. At about minute ' + fm(SW.explore2[0]) + ', say “Pencils down” and bring the group back together. Take the two questions below, one at a time.']);
  ask(d.expAsk.map(x => [x[0], x[1]]));

  ps('Mini-lesson', 'Mini-lesson (you teach, they join in)');
  doo(['Show the mini-lesson slides. Think aloud as you work. Say what you notice, what you test and how you check. Children copy how you think.']);
  say(s.think);
  G.push(tbl([4600, 5300], [row([hd('Worked example on the slides', 4600), hd('Answer', 5300)]), row([c2(d.mini1.head + '. ' + (d.mini1.body || []).join(' '), 4600), c2(d.mini1.ans, 5300)]), row([c2(d.mini2.head + '. ' + (d.mini2.body || []).join(' '), 4600), c2(d.mini2.ans, 5300)])]));
  G.push(gap(40));
  say([d.keyHead.replace(/^Key idea: /, 'The key idea today is: ') + '. ' + d.keyBig + ' Say it with me.']);
  const tryW = Object.keys(SW).filter(k => /^try/.test(k));
  doo(['Show the key idea slide at minutes ' + to(SW.key[0], SW.key[1]) + '. ' + (tryW.length ? 'The one “your turn” slide (minutes ' + to(SW[tryW[0]][0], SW[tryW[0]][1]) + ') is optional: skip it if you are behind. Ask at most three of the questions in the slide notes.' : 'There is no “your turn” slide in this lesson. Ask at most three of the questions in the slide notes.') + ' The “common mistakes” on that slide are for you, not the children. Watch for them during the worksheet:']);
  l.mistakes.forEach(m => G.push(bu(m)));

  ps('Brain break', 'Brain break');
  doo([d.brk, 'Water and a toilet stop come FIRST (about one minute), then the game (about two minutes). Keep the whole break to ' + fm(P('Brain break').end - P('Brain break').start) + ' minutes. CLOCK CHECK at minute ' + fm(P('Brain break').end) + ': if you are more than 1.5 minutes behind, skip the next optional item (the “your turn” slide, or a second speaker-note question), never a check, the exit ticket or Looking back.']);

  ps('Worksheet', 'Worksheet (pairs, then alone)');
  doo(['Minute ' + fm(P('Worksheet').start) + ': give out the workbook. Read the title of Lesson ' + l.n + ' aloud. Say “Pairs first. Talk before you write.”', 'Minutes ' + to(WB[0].start, WB[0].end) + ': pairs work together on the first page (online, allow about 2 minutes to move into and out of breakout rooms, or run page 1 as a whole-group screen-share). Minutes ' + to(WB[1].start, WB[1].end) + ': check page 1 together. Minutes ' + to(WB[2].start, WB[2].end) + ': the short teaching before page 2. Minutes ' + to(WB[3].start, WB[3].end) + ': each child works alone on the second page. Minutes ' + to(WB[4].start, WB[4].end) + ': check page 2 together.', 'STANDING BUFFER: the last ' + fm(BUF.end - BUF.start) + ' minutes of the page-2 block (minutes ' + to(BUF.start, BUF.end) + ') are not given to any question. If earlier parts ran long, page 2 starts late and the buffer is spent first, then the choice questions at the end of the page. Never shorten the checks, the exit ticket or Looking back. Do not mention the buffer to the children.'].concat(l.gaps.plan));
  say(['Pairs first. Read each question aloud and talk about it before you write. I am not looking for speed. I am looking for good thinking.']);
  doo(['Circulate and ask:']);
  s.circulate.forEach(c => G.push(bu(c)));
  stuck(s.hints);
  doo(['Choosing (printed on page 1: “' + l.gaps.p1 + '”): every child may carry on or try Think harder. Make the offer to the whole group, never to one child by name, and never by private message. The Think harder page, the Go further page and the Investigation have no fixed time slot: any child may choose them when they have finished Start here, and they are good for take-home. Page 2 is on your own and has a printed note about which questions to do first, so nobody has to rush. Every lesson has an Investigation on page 3, with an easy first step and a model answer in the answer key below: it has several valid answers, so ask “How did you decide?” and “Is there another way?” rather than marking it right or wrong.']);
  G.push(h2('Think harder and Go further questions'));
  ask([...(q.stretch || []).slice(0, 4).map((x, i) => ['Workbook Think harder ' + (i + 1) + ': ' + x.q, x.a]), ...(q.challenge || []).slice(-3).map((x, i) => ['Workbook Go further ' + (i + 1) + ': ' + x.q, x.a])], 'Question', 'Answer');
  G.push(tx('These are the questions on the Think harder page and the Go further page in the workbook. More are in the separate Question Bank.', { size: 19, color: '666666' }));

  ps('Talk time', 'Talk time');
  doo(['Bring the group back to a circle (or camera on, mics on). Pair talk is one minute and needs no breakout room: children tell the grown-up beside them, or write one sentence. Then ask for volunteers first. No cold-calling, nobody has to speak, and passing is always fine. Never keep a tally or scoreboard in front of the group. Praise the reasons, not the speed.']);
  say(s.talk);
  ask([[l.share, s.talkAns]], 'Discussion question', 'Listen for');
  if (s.talkWeekly) doo(['Moved to the Weekly Dose of Thinking Math (not asked in class): ' + s.talkWeekly.join(' ') + ' ' + (s.talkWeeklyAns || '')]);

  ps('Exit ticket', 'Exit ticket and closing');
  doo(['Give each child a slip of paper (or ask them to write on their journal page). No talking, no helping. Show the exit ticket slide.']);
  ask([[l.exit.q, l.exit.a]], 'Exit ticket', 'Answer');
  say(s.close);
  doo(['Stamp the inquiry journal when a child hands in their ticket. Mark S, D or H in the progress tracker at the back of this guide. If a child marked D or H, plan two minutes of catch-up at the start of the next lesson.']);
  ps('Looking back', 'Looking back (2 minutes of writing)', 2);
  say(['Turn to page 3, the Looking back box. Write, tick or pass. Two minutes, no talking.', 'Model one yourself first: “' + l.gaps.reflect + '” Ticking “I am still stuck” is a good thing to do: it tells me where to help.']);
  doo(['Run it in two minutes. It is never collected, never graded, never corrected and never shown to the group. Do not ask a child to hold a box or page to the camera; children tick their own box against the answer slide. Do not ask anyone to read theirs aloud; if a child wants to share, take one volunteer and thank them for the strategy. If “I am still stuck” is ticked, check in during the open session: a quick visit to the shared breakout room or a hand signal, with a parent nearby. Never send a direct message. Praise the strategy (“you drew it”, “you asked for help”), not the speed or the score.']);
  if (l.n === 10) {
    ps('Certificates and goodbye', 'Certificates and goodbye');
    say(s.farewell);
    doo(['Whole group, no per-child comments. Before the lesson, write one personal sentence for each child: certificates and stamped journals are posted or sent with it after the lesson, and the sentence is never read out. Show the last slide. Three volunteers each name one puzzle and one way in (about 20 seconds each). Say one sentence about the group, then goodbye. Give parents the one-page summary from this guide.']);
  }
  G.push(h2('Extension: for any child who wants more'));
  G.push(tx(l.extension));
  G.push(h2('Answer key (workbook)'));
  l.key.forEach(k => G.push(p([t(k[0] + '  ', { bold: true, size: 20 }), t(k[1], { size: 20 })], { after: 50, indent: { left: 240 }, line: 270 })));
  G.push(p([t('Investigation  ', { bold: true, size: 20 }), t(l.gaps.invest.head + ' (' + l.gaps.invest.kind.trim() + ') Easy first step: ' + (l.gaps.invest.easy || '') + '  Model answer: ' + l.gaps.invest.key, { size: 20 })], { after: 50, indent: { left: 240 }, line: 270 }));
  G.push(p([t('Go further  ', { bold: true, size: 20 }), t(l.gaps.go2.q + ' ' + l.gaps.go2.a, { size: 20 })], { after: 50, indent: { left: 240 }, line: 270 }));
  G.push(p([t('Sneak-peek puzzles  ', { bold: true, size: 20 }), t(l.gaps.check.map((x, i) => '(' + (i + 1) + ') ' + x.a).join('  '), { size: 20 })], { after: 50, indent: { left: 240 }, line: 270 }));
  G.push(h2('Recording chapters and what a child watching later does'));
  G.push(tbl([1300, 3200, 5400], [row([hd('Time', 1300), hd('Chapter marker', 3200), hd('A child watching later', 5400)]), ...SEGS.map(x => row([c2(x.time, 1300), c2(x.title, 3200), c2(x.action, 5400)]))]));
  G.push(gap(40));
});

/* ---------- Tracker ---------- */
G.push(h1('Progress tracker', true));
G.push(tx('After each exit ticket, write S (secure: correct and can explain), D (developing: correct but cannot explain yet) or H (needs help). Use the notes for what to revisit next lesson.'));
{ const ws = [2000, ...Array(10).fill(580), 2100]; const head = [hd('Student', ws[0]), ...Array.from({ length: 10 }, (_, i) => hd('L' + (i + 1), 580)), hd('Notes', ws[11])];
  G.push(tbl(ws, [row(head), ...Array.from({ length: 10 }, () => row(ws.map((w, i) => cell('', w, { h: 150 }))))])); }
G.push(h2('Ending the program'));
['In Lesson 10, send or post each child a certificate and their completed inquiry journal with a personal sentence you wrote before the lesson (the live close is whole-group, 2.5 minutes).', 'Send parents a short message through the approved channel: one thing their child did well, and one thing to keep practising.', 'Delete or hand over all Student Data within 7 days after the last lesson (this is in the tutor agreement).'].forEach(s => G.push(bu(s)));

/* ---------- Tutor checklist ---------- */
G.push(h1('Tutor checklist', true));
G.push(h2('Before each lesson'));
['Read the lesson plan and solve the worksheet yourself without looking at the key.', 'Check materials are ready, or the online set-up has been sent.', 'Test the platform, screen share and annotation tools 10 minutes early (online).', 'Print or open the slide deck for the lesson.'].forEach(s => G.push(bu(s)));
G.push(h2('During the lesson'));
['Circulate and ask questions rather than giving answers.', 'Use only the approved channels to contact parents. No private messages to children: invitations go to the whole group and check-ins happen in the open session.', 'Do not take your own photos or recordings. The only recording is the lesson recording made on the approved platform under “Recording the lesson”.', 'If you have a concern about a child’s safety or welfare, tell the Company straight away.'].forEach(s => G.push(bu(s)));
G.push(h2('After the lesson'));
['Stamp inquiry journals and fill in the tracker.', 'Collect worksheets and answer keys (face to face) and keep them secure.', 'Note any child who needs help, and plan a short catch-up at the start of the next lesson.'].forEach(s => G.push(bu(s)));

/* ---------- Parent summary ---------- */
G.push(p(t(PROG, { bold: true, size: 44 }), { pb: true, after: 40 }));
G.push(p(t(SLOGAN, { italics: true, size: 28, color: '1F3864' }), { after: 100 }));
G.push(p(t('A 10-lesson holiday maths program for ages 9 to 11 (builds on Primary 4 maths)', { bold: true, size: 26 }), { after: 100 }));
G.push(tx('Your child will spend the holidays as a young mathematician: noticing patterns, testing ideas with real objects and explaining their thinking. Lessons are live online in small groups, hands-on, and built around thinking, not speed.'));
G.push(h2('What your child will do'));
L.lessons.forEach(l => G.push(bu('Lesson ' + l.n + ', ' + l.title + ': ' + l.topic.toLowerCase())));
G.push(h2('How you can help'));
['Ask “How do you know?” when your child tells you an answer.', 'Let your child try first. Please sit nearby, but let them find the answer.', 'Print the workbook and cut-outs, and keep scissors, a ruler and a pencil ready.'].forEach(s => G.push(bu(s)));
G.push(h2('Practical details'));
G.push(tbl([2500, 7400], [['Dates', '[start date] to [end date], two lessons a week'], ['Time', '[day] and [day], [start time] to [end time]'], ['Where', 'Live online video class (link sent after registration)'], ['Group size', '[number] children'], ['Fee', 'S$250 beta fee for all 10 lessons (S$25 a lesson), printed workbook and cut-out kit included'], ['Contact', '[name, phone or email]']].map(r => row([cell(r[0], 2500, { bold: true, fill: 'F2F2F2', size: 20, align: AlignmentType.LEFT, h: 80 }), c2(r[1], 7400, { h: 80 })]))));
G.push(p(t('Math Inquirers Holiday Program is an independent enrichment program. It builds problem-solving and thinking skills and is not affiliated with, run by or endorsed by the Ministry of Education or any school.', { size: 18, italics: true, color: '666666' }), { before: 200, after: 0 }));

const doc = new D.Document({ styles: { default: { document: { run: { font: 'Arial', size: S } } } }, sections: [{ properties: { page }, footers: { default: footer(PROG + ' P4 • Program guide') }, children: G }] });
D.Packer.toBuffer(doc).then(b => { fs.writeFileSync('P4_Holiday_Program_Guide.docx', b); console.log('guide built'); });
