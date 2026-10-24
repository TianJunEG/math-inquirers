const C = require('../hp/common.js');
const { fs, D, CW, t, p, cell, tbl, row, gap, footer, page, AlignmentType, BorderStyle, WidthType } = C;
const L = require('./data.js');
const HG = require('../levels/habit_guide.js');   // focus habit line (levels/habits.json)
const SG = require('../levels/spine_guide.js');   // strategy card + common look-back lines (levels/spine.json)
const BUD = require('./budget.json').lessons;   // written by rebuild/p5_budget.py: the minute plan of every lesson (every lesson adds up to 90)
const fm = x => String(x);
const partOf = (n, title) => BUD[String(n)].parts.find(q => q.title.startsWith(title));
const rg = q => q ? fm(q.start) + '–' + fm(q.end) : '';
const PAIRWORK = { 1: 6, 2: 6, 3: 6, 4: 6.5, 5: 6, 6: 6, 7: 6, 8: 6.5, 9: 5.5, 10: 6 };   // minutes of pair work in the explore (rebuild/p5_gaps.py has the same table)
const PROG = L.program, SLOGAN = L.slogan;
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
G.push(p(t('PRIMARY 5 HOLIDAY PROGRAM', { bold: true, size: 22, color: '666666' }), { after: 20 }));
G.push(p(t(PROG, { bold: true, size: 52 }), { after: 40 }));
G.push(p(t(SLOGAN, { italics: true, size: 30, color: '1F3864' }), { after: 120 }));
G.push(tx('Program guide for tutors: schedule, lesson routine, ten minute-by-minute lesson scripts with answer keys, a progress tracker and a parent summary. Math Inquirers is online first: every lesson runs live on video; the face-to-face notes are kept for partner centres.'));
G.push(h2('The program at a glance'));
G.push(tbl([2300, 7600], [
  ['Level', 'Children finishing Primary 5 (ages 11 to 12), going into P6, the PSLE year, who are ready for more thinking than standard practice'],
  ['Length', '10 lessons of 90 minutes, two a week over the 5 weeks of the holidays'],
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
G.push(tx('Week 5 of the December 2026 beta: lessons 9 and 10 are four days apart. Friday 25 December is skipped, so lesson 9 moves to Wednesday 23 December (4:45 to 6:15 pm) and lesson 10 stays on Sunday 27 December (4:15 to 5:45 pm). In the other weeks the two lessons are two days apart, so tell families early. At the end of lesson 9 remind children that the two days of a normal week become four, and that the Lesson 9 take-home parts can be done in that time.', { before: 60 }));

/* ---------- Routine ---------- */
G.push(h1('The 90-minute lesson routine', true));
G.push(tx('Every lesson uses the same routine so children know what to expect and tutors can prepare quickly. The column “Minutes” gives how long each part lasts across the ten lessons (for example 4 to 4.5); the exact minute marks of each lesson are printed in its own script below and on its slides, and each lesson adds up to exactly 90 minutes. The opening is inside the 90 minutes. The last part, the buffer, is floating time that is not scheduled.'));
const R = L.timeline;
G.push(tbl([1000, 2600, 6300], [row([hd('Minutes', 1000), hd('Part', 2600), hd('What happens', 6300)]), ...R.map(r => row([c2(r[0], 1000, { align: AlignmentType.CENTER, bold: true }), c2(r[1], 2600, { bold: true }), c2(r[2], 6300)]))]));
G.push(tx('This is the one routine used by the slides, the scripts and the workbook. Online, children keep cameras on and share work by saying answers together on three or by fingers; nothing is held up to the camera. Face to face, children sit in pairs and the tutor circulates.', { before: 60 }));
G.push(h2('If you run late: the cut-first ladder and the buffer'));
G.push(tx('Every lesson ends with a buffer of 1 to 5 minutes (about 3 on average) of floating time, so a late arrival, a muted microphone or a slow breakout room does not land on the worksheet. Spend the buffer first. If you are still more than 2 minutes behind at the end of the brain break, cut in this order, and never touch the fixed items:'));
['The first step of the Investigation. It is already take-home (or the opener of the next lesson); do not even mention it in class, and drop the second talk question.', 'Quick question 4 in the warm-up.', 'The Go further what-if on the explore slide.', 'The last in-class item of page 2. Page 2 is a menu: stop at the minute printed in the lesson.', 'The reflection becomes a one-tick version: pass, or one box.'].forEach((x, i) => G.push(bl((i + 1) + '.', x)));
G.push(tx('Never cut: the sneak-peek puzzles, the exit ticket, the stamp (typed in the chat), and in Lesson 10 the certificates. Parts marked with a star in the workbook are take-home: say so once and do not wait for them. The clock checkpoints of each lesson are in its table.'));
G.push(h2('Teaching habits that matter'));
['Ask “How do you know?” after every answer, right or wrong.', 'Wait 10 seconds before helping. Let children struggle a little.', 'Talk time is by invitation: ask for volunteers first, never cold-call a child by name, always allow “pass”, and never keep public tallies or rankings.', 'Praise the thinking (“You checked it two ways”), not just the answer.', 'Let children disagree with each other and settle it with objects or a drawing.', 'If a child finishes early, offer the Go further what-if or the Investigation, not extra drill.'].forEach(s => G.push(bu(s)));

G.push(h2('Preparing the materials'));
['Send the workbook PDF to parents one week before. Ask them to print it single-sided and the cut-out pages on card if they can.', 'Cut-outs used: square grid and dot grid (Lessons 4, 8), fraction wall (Lessons 2, 3), cube net (Lesson 5). Children need a protractor and a ruler.', 'Keep the answer key with the tutor only. Check answers together on screen.', 'Use the shared screen or a digital whiteboard for the mini-lesson table.'].forEach(s => G.push(bu(s)));
G.push(h2('Setting up online'));
['Send parents the workbook and materials list one week before. Needed: the printed workbook and cut-outs, scissors, a ruler, paper and a pencil.', 'Use one approved platform with breakout rooms and screen share. Admit only registered children and never share the link publicly.', 'Ask the parent to sit nearby but not give answers. The camera should show the child’s page and hands.', 'Nothing is held up to the camera. At the end of each lesson children tick their own work against the answer slide. If a child is still stuck, they mark their own look-back page and the parent photographs it for the tutor after class (business WhatsApp), never during the recorded class.', 'Lessons are recorded on the approved platform so that children who miss one can catch up; follow “Recording the lesson” in this guide. Do not make your own recordings or photos. Add a second tutor or helper above 8 children.'].forEach(s => G.push(bu(s)));

G.push(h1('Materials master list', true));
G.push(tbl([900, 2600, 3200, 3200], [row([hd('Lesson', 900), hd('Title', 2600), hd('Face to face', 3200), hd('Online set-up', 3200)]), ...L.lessons.map(l => row([c2(String(l.n), 900, { align: AlignmentType.CENTER, bold: true }), c2(l.title, 2600), c2(l.materials, 3200), c2(l.online, 3200)]))]));

/* ---------- Lesson scripts ---------- */
const DD = L.deck;
const SC = L.scripts;
const QB = L.qbank;
const INV = Object.fromEntries(L.content.map(c => [c.lesson.n, c.investigation]));
const tag = (s, fill) => cell(s, 1000, { bold: true, fill, size: 18, h: 50, align: AlignmentType.CENTER });
const seg = (time, title) => p([t(time + '   ', { bold: true, size: 22, color: 'FFFFFF' }), t(title, { bold: true, size: 22, color: 'FFFFFF' })], { before: 160, after: 60, keepNext: true, shading: { type: 'clear', fill: '1F3864', color: 'auto' } });
const say = (lines) => lines.forEach((s, i) => G.push(p([t(i === 0 ? 'SAY   ' : '          ', { bold: true, size: 19, color: '1F6F5C' }), t('“' + s.replace(/^[“"]|[”"]$/g, '') + '”', { size: S, italics: true })], { after: 50, indent: { left: 900, hanging: 900 }, line: 280 })));
const doo = (lines) => lines.forEach((s, i) => G.push(p([t(i === 0 ? 'DO     ' : '          ', { bold: true, size: 19, color: '7F6000' }), t(s, { size: S })], { after: 40, indent: { left: 900, hanging: 900 }, line: 280 })));
const REC = require('../levels/reccues.js'); let CURL = null; const SEGS = [];
const rec = (text) => G.push(p([t('REC   ', { bold: true, size: 19, color: '6B3FA0' }), t(text, { size: S, italics: true })], { after: 40, indent: { left: 900, hanging: 900 }, line: 280 }));
// a segment is a budget part {start, end} from p5/budget.json; the REC cue gets a whole-minute length (rounded) because reccues.js reads whole minutes
const pushSeg = (part, title) => { const time = rg(part) + ' min'; G.push(seg(time, title)); const c = REC.cue(title, '0–' + (part.end - part.start), CURL); SEGS.push({ time, title, action: c.action }); rec(c.say); };
const ask = (rows, h1c, h2c) => { G.push(tbl([4600, 5300], [row([hd(h1c || 'Ask', 4600), hd(h2c || 'Expect', 5300)]), ...rows.map(r => row([c2(r[0], 4600), c2(r[1], 5300)]))])); G.push(gap(40)); };
const stuck = (lines) => lines.forEach((s, i) => G.push(p([t(i === 0 ? 'IF STUCK   ' : '                ', { bold: true, size: 19, color: 'A61C00' }), t(s, { size: S })], { after: 40, indent: { left: 1300, hanging: 1300 }, line: 280 })));

G.push(h1('How to use the scripts', true));
G.push(tx('Every lesson below is a minute-by-minute script. The slides match it: one slide or two for each part. You do not have to say the words exactly, but keep the questions, because the questions are what makes children think.'));
G.push(tbl([1500, 8400], [
  ['SAY', 'Words to say aloud, in plain language for 10- to 12-year-olds. Said in your own voice, not read from the page.'],
  ['DO', 'What you do: set up, hand out, show a slide, or move around the room.'],
  ['ASK / EXPECT', 'Questions to put to the group, with the answer you are listening for. Let children answer before you explain.'],
  ['IF STUCK', 'A ladder of help. Give hint 1, wait ten seconds, then give hint 2. Do not give the answer.']
].map(r => row([cell(r[0], 1500, { bold: true, fill: 'F2F2F2', size: 20, align: AlignmentType.LEFT, h: 70 }), c2(r[1], 8400)]))));
G.push(h2('Five habits that run through every script'));
['Predict first. Before children test anything, ask for a guess and write it down. A wrong guess is useful because we can test it.', 'Wait ten seconds after every question. Count silently. Most children answer in the last four.', 'Ask “How do you know?” after right answers too, so that children do not read your face for the answer.', 'Praise the thinking, not the answer: “You checked it two ways” beats “Well done”.', 'When an answer is wrong, say “Let us test that,” and use objects, not “No”.'].forEach(s => G.push(bu(s)));
G.push(h2('Sneak-peek puzzles, choosing a start and the reflection'));
['Every lesson starts, after the 2-minute opening, with about 4 minutes of sneak-peek puzzles: two puzzles on ideas we have not learnt yet. The first is an access puzzle any child can try with objects, drawing or counting, so everybody starts with a win. The second is a thinking puzzle. Say clearly: guessing and “I do not know” are welcome and nobody is marked.', 'Answers are shown privately: on the child’s own paper held to you as you walk round. Online, children say the answers together on three; nothing is held up to the camera. Use ONE check for both puzzles (say the answers together on three), then click through the answers and say each with one short reason. There is no volunteer round in the sneak-peek. Never use boards in front of the group, never read answers out with names, never keep a tally or a ranking.', 'Choosing a start: every child has the same neutral line on workbook page 1, “After question 2 or 3 (the line on each lesson’s page 1 gives the number) you may choose: carry on, or try Think harder.” Invite the WHOLE group, never one child: "when you have finished Start here you can choose Think harder, Go further or the Investigation." Never announce who is on which page, never name a child in front of the group for this, and do not split a pair unless both children agree. Any child may swap at any time. The Go further what-if on the explore slide and the Investigation (printed on the page every child gets) give anyone more to do without waiting.', 'Every lesson ends with the common Look back (about a minute and a half) in the Look back box at the bottom of the Investigation page: three questions (did I answer the question, is my answer reasonable, how can I check it another way), the tools the child used, and “I am still stuck (my tutor will come)”. Pass is always allowed. It is never collected or read out in public; you may read it privately to plan the next lesson, and you check in with anyone who ticked “still stuck” in the open session (a quick visit to the shared breakout room or a hand signal, with a parent nearby, never a private message). Praise strategy, not speed.'].forEach(s => G.push(bu(s)));
G.push(h2('Toolbox and look-back (every lesson)'));
G.push(tx('Every lesson has one TOOL OF THE DAY, shown on the workbook card on page 1, on the title slide (with a small badge on the talk slide) and named in your script. It is one of eight tools a child can choose for any problem. Say its name, point at the card, and at talk time ask where the tool helped. Lesson 10: children choose their own tool. Passing is always allowed.'));
G.push(tbl([2500, 7400], [row([hd('Tool', 2500), hd('What we say (ages 10 to 13)', 7400)]), ...SG.DATA.tools.map(t => row([c2(t.name, 2500, { bold: true }), c2(t.def.C, 7400)]))]));
G.push(gap(40));
G.push(tx('The look-back is the same every lesson: pick ONE problem from today and ask three things. ' + SG.DATA.lookback.prompts.C.map((q, i) => (i + 1) + ') ' + q).join(' ') + ' Children tick yes or not yet for questions 1 and 2, write one short line for question 3 (I checked by ...), and tick the tools they used. The timer is ' + SG.info(5, 1).timer + ' seconds, then stamp the journals. Nothing is collected, read aloud or marked.'));
G.push(h2('Focus habit (every lesson)'));
G.push(tx('Every lesson names ONE focus habit on its front page, on the opening slide and on the look-back slide, and has one “explain your thinking” item in the online practice. The habit is something the children practise; you are not testing it. The same six habits are used at every level. Do not give the answer first: ask the prompt, wait, and give a hint only if the child is stuck.'));
G.push(tbl([1500, 2700, 5700], [row([hd('Habit', 1500), hd('Child says', 2700), hd('Your move and prompt', 5700)]), ...Object.keys(HG.DATA.habits).map(k => row([c2(k, 1500, { bold: true }), c2('“' + HG.DATA.habits[k].phrase + '”', 2700), c2(HG.DATA.habits[k].move + ' Say: “' + HG.DATA.habits[k].prompt + '”', 5700)]))]));
G.push(gap(40));
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

L.lessons.forEach(l => {
  CURL = l; SEGS.length = 0;
  const d = DD[String(l.n)], s = SC[l.n], q = QB[String(l.n)];
  const BP = t => partOf(l.n, t), P1 = BP('Worksheet page 1'), K1 = BP('Check page 1'), TS = BP('Short teaching'), P2 = BP('Worksheet page 2'), K2 = BP('Check page 2'), EX = BP('Explore'), BUF = BP('Buffer');
  const dur = q => fm(q.end - q.start);
  G.push(h1('Lesson ' + l.n + ': ' + l.title, true));
  G.push(p(t('Week ' + l.week + (l.session === 'A' ? ' (first lesson)' : ' (second lesson)') + '   •   ' + l.topic + '   •   Workbook: Lesson ' + l.n, { size: 20, color: '666666' }), { after: 80 }));
  G.push(tx(HG.line(5, l.n), { bold: true, size: 20, after: 100 }));
  G.push(tbl([1900, 8000], [
    ['Objective', l.objective], ['Thinking skills', l.skills], ['Materials', l.materials], ['Online set-up', l.online],
    ['Prepare', 'Solve the worksheet yourself first. Set out one materials box per pair. Open the slides for this lesson and check the answers in the speaker notes.'],
    ['Clock checkpoints', 'Explore done at ' + fm(EX.end) + ', mini-lesson done at ' + fm(BP('Mini-lesson').end) + ', brain break done at ' + fm(BP('Brain break').end) + ', page 1 done at ' + fm(P1.end) + ', check page 1 done at ' + fm(K1.end) + (TS ? ', short teaching done at ' + fm(TS.end) : '') + ', page 2 done at ' + fm(P2.end) + ', check page 2 done at ' + fm(K2.end) + ', talk time done at ' + fm(BP('Talk time').end) + ', buffer ' + dur(BUF) + ' minutes (' + rg(BUF) + '). If you are more than 2 minutes behind at the end of the brain break, use the cut-first ladder in the routine section.'],
    ['Take-home (starred in the workbook)', l.take + '. Say once that the starred parts are for home, and do not wait for them. Their answers are on the check slides and in the key below.'],
    ['Watching the recording', 'A child who missed the live lesson watches the recording. They need: ' + l.materials + ' The REC lines tell them when to pause; the chapter list at the end of this lesson shows each part.']
  ].map(r => row([cell(r[0], 1900, { bold: true, fill: 'F2F2F2', size: 20, align: AlignmentType.LEFT, h: 60 }), c2(r[1], 8000, { h: 60 })]))));
  G.push(gap(40));

  pushSeg(BP('Opening'), 'Opening (inside the 90 minutes)');
  say(s.hook);
  doo(['Greet the children with a wave and in the chat (do not go round naming every child), say in one sentence that the lesson is recorded, show the lesson title slide and read “Today we will…” aloud. Keep the hook short: ' + fm(BP('Opening').end - BP('Opening').start) + ' minutes in all.']);
  { const sp = SG.info(5, l.n); say([sp.openSay]); doo([sp.openDo + (sp.kitLine ? ' Say: “' + sp.kitLine + '.”' : '')]); }

  pushSeg(BP('Sneak'), 'Sneak-peek puzzles (private answers)');
  ask(d.check.map((x, i) => [(i === 0 ? 'Puzzle 1 (access): ' : 'Puzzle 2 (thinking): ') + x[0], x[1]]), 'Puzzle', 'Listen for');
  doo(s.check);
  pushSeg(BP('Warm-up'), 'Warm-up');
  doo(['Minutes ' + rg(BP('Warm-up')) + ': the warm-up game below (ONE round only) and then four quick questions. If you are short of time, skip quick question 4.']);
  doo([d.warmGame]);
  say(s.warmIntro);
  doo(['After the game, ask the four quick questions on the warm-up slides. Use thumbs or a whisper to partners before taking answers.']);
  ask(d.warmQs.map(x => [x[0], x[1]]));

  pushSeg(EX, 'Explore (in pairs, with objects)');
  say(s.predict);
  doo(d.expSetup.map((x, i) => (i + 1) + '. ' + x));
  say(['Talk to your partner while you work. I will come round and ask you questions.']);
  stuck(s.exploreHints);
  doo(['Go further what-if (on the second explore slide, for anyone who wants more, so nobody waits): ' + d.whatIf[0] + ' (Answer: ' + d.whatIf[1] + ')', 'Pair work is at most ' + fm(PAIRWORK[l.n]) + ' minutes after the 30 seconds of silent thinking: at minute ' + fm(EX.end - 4) + ', say “Pencils down” and bring the group back together. Take the two questions below, one at a time (about a minute each).']);
  ask(d.expAsk.map(x => [x[0], x[1]]));

  pushSeg(BP('Mini-lesson'), 'Mini-lesson (you teach, they join in)');
  doo(['Show the mini-lesson slides. Think aloud as you work. Say what you notice, what you test and how you check. Children copy how you think.']);
  say(s.think);
  G.push(tbl([4600, 5300], [row([hd('Worked example on the slides', 4600), hd('Answer', 5300)]), row([c2(d.mini1.head + '. ' + (d.mini1.body || []).join(' '), 4600), c2(d.mini1.ans, 5300)]), row([c2(d.mini2.head + '. ' + (d.mini2.body || []).join(' '), 4600), c2(d.mini2.ans, 5300)])]));
  G.push(gap(40));
  say([d.keyHead.replace(/^Key idea: /, 'The key idea today is: ') + '. ' + d.keyBig + ' Say it with me.']);
  doo(['Show the key idea slide in the last minute or two of the mini-lesson (its slide shows the minutes). The “common mistakes” on that slide are for you, not the children. Watch for them during the worksheet:']);
  l.mistakes.forEach(m => G.push(bu(m)));

  pushSeg(BP('Brain break'), 'Brain break');
  doo([d.brk, 'Water. Toilet break for anyone who needs it. Keep it to ' + dur(BP('Brain break')) + ' minutes.']);

  pushSeg({ start: P1.start, end: K2.end }, 'Workbook (page 1 in pairs, check, teaching, page 2 alone, check)');
  doo(['Minute ' + fm(P1.start) + ': give out the workbook. Say “Pairs first. Talk before you write. The starred parts are for home.”', 'Minutes ' + rg(P1) + ': pairs work on page 1: ' + l.p1 + '. Minutes ' + rg(K1) + ': check page 1 together (one pair explains the heaviest question, you click through the rest). ' + (TS ? 'Minutes ' + rg(TS) + ': the short teaching slides for the page 2 questions that stay in class. ' : 'There is no short teaching in this lesson: go straight to page 2. ') + 'Minutes ' + rg(P2) + ': each child works alone on page 2: ' + l.solo + '; it is a menu, not a wall, so nobody has to finish. Stop at minute ' + fm(P2.end) + '. Minutes ' + rg(K2) + ': check page 2 together (only the questions that were set).']);
  say(['Pairs first. Read each question aloud and talk about it before you write. I am not looking for speed. I am looking for good thinking.', 'After question ' + L.choiceQ(l.n) + ' you may choose: carry on, or try Think harder. You can swap at any time.']);
  doo(['Circulate and ask:']);
  s.circulate.forEach(c => G.push(bu(c)));
  stuck(s.hints);
  doo(['Pairs who want more: offer the Go further page or the Investigation. Everyone has the same neutral line on page 1. Invite the whole group ("when you have finished Start here you can choose Think harder, Go further or the Investigation"); never single out a child, never announce who is on which page, and do not split a pair unless both children agree.']);
  ask([['Investigation (printed on the Investigation and reflection page every child gets): ' + l.title + ' (' + INV[l.n].title + ')', 'First step for everyone: ' + INV[l.n].first + ' ' + INV[l.n].parts.map((x, i) => '(' + 'abc'[i] + ') ' + x).join(' ')], ['What to look for / model answer', INV[l.n].a]], 'Investigation', 'Detail');
  G.push(h2('Think harder and Go further questions'));
  ask([...(q.stretch || []).slice(0, 4).map((x, i) => ['Workbook Think harder A' + (i + 1) + ': ' + x.q, x.a]), ...(q.challenge || []).slice(-3).map((x, i) => ['Workbook Go further B' + (i + 1) + ': ' + x.q, x.a]), ...(l.pose ? [['Make up your own (printed under Go further, after 30 seconds of silent thinking): ' + l.pose, 'Open-ended. Check that a partner can solve it and that exactly one answer fits; ask “what if you changed one number?”']] : [])], 'Question', 'Answer');
  G.push(tx('These are the questions on the Think harder and Go further pages in the workbook. More are in the separate Question Bank.', { size: 19, color: '666666' }));

  pushSeg(BP('Talk time'), 'Talk time');
  doo(L.scripts[l.n].talkRules.concat(['Bring the group back to a circle (or camera on, mics on). 30 seconds of silent thinking, pairs talk for 2 minutes, volunteers share for 1 and a half minutes. Finish by saying that the first step of the Investigation is take-home (or the opener of the next lesson); do not do it in class.']));
  say(s.talk);
  { const sp = SG.info(5, l.n); ask([[l.share, s.talkAns], [sp.talkAsk, sp.talkListen]], 'Discussion question', 'Listen for'); }

  pushSeg(BP('Exit'), 'Exit ticket, reflection and closing');
  doo(['Give each child a slip of paper (or ask them to write on their journal page). No talking, no helping. Show the exit ticket slide.']);
  ask([[l.exit.q, l.exit.a]], 'Exit ticket', 'Answer');
  say(s.close);
  { const sp = SG.info(5, l.n);
    say([sp.lookSay + ' ' + sp.checkTogether, 'Thank you. Drawing it, listing, trying a smaller case or checking another way: those are all good ways to get unstuck.']);
    doo(['Show the look-back slide and start its timer (' + sp.timer + ' seconds); the Look back box is at the bottom of the Investigation page. ' + sp.lookDo.replace(/^Start the timer\. /, '') + ' If the clock is behind, the look-back becomes a one-tick version: pass or one box. Never mark or grade the box, never collect it in front of the group and never read a child\u2019s answer aloud; you may look at it privately afterwards. If a child ticks \u201cI am still stuck\u201d, check in during the open session (a quick visit to the shared breakout room or a hand signal, with a parent nearby), never by private message. Pass is always allowed.']); }
  doo([(l.n === 10 ? 'Hand out the certificates (about 12 seconds each, shown by the tutor on screen) and type the last stamp in the chat. ' : 'Type each child’s stamp in the chat in one message (you can also stamp the inquiry journal at the next lesson). ') + 'Mark S, D or H in the progress tracker at the back of this guide (private to you, never shown to children). If a child is marked D or H, plan two minutes of catch-up at the start of the next lesson.']);
  pushSeg(BUF, 'Floating time (the buffer) and close');
  doo(['The buffer is ' + dur(BUF) + ' minutes of floating time at the end. It has no script. It is what absorbs a late start or a slow breakout room, so it is spent first when the lesson runs late. If it is still there, use it for the Go further what-if, a pair that needs a catch-up, or an early goodbye.']);
  G.push(h2('Extension for anyone who wants more'));
  G.push(tx(l.extension));
  G.push(h2('Answer key (workbook)'));
  l.key.forEach(k => G.push(p([t(k[0] + '  ', { bold: true, size: 20 }), t(k[1], { size: 20 })], { after: 50, indent: { left: 240 }, line: 270 })));
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
['In Lesson 10, give each child a certificate and their completed inquiry journal.', 'Send parents a short message through the approved channel: one thing their child did well, and one thing to keep practising.', 'Delete or hand over all Student Data within 7 days after the last lesson (this is in the tutor agreement).'].forEach(s => G.push(bu(s)));

/* ---------- Tutor checklist ---------- */
G.push(h1('Tutor checklist', true));
G.push(h2('Before each lesson'));
['Read the lesson plan and solve the worksheet yourself without looking at the key.', 'Check materials are ready, or the online set-up has been sent.', 'Test the platform, screen share and annotation tools 10 minutes early (online).', 'Print or open the slide deck for the lesson.'].forEach(s => G.push(bu(s)));
G.push(h2('During the lesson'));
['Circulate and ask questions rather than giving answers.', 'Contact parents only through the approved channels. No private messages to children: invitations and check-ins are made to the whole group or in the open session.', 'Do not take your own photos or recordings. The only recording is the lesson recording made on the approved platform under “Recording the lesson”.', 'If you have a concern about a child’s safety or welfare, tell the Company straight away.'].forEach(s => G.push(bu(s)));
G.push(h2('After the lesson'));
['Stamp inquiry journals and fill in the tracker.', 'Collect worksheets and answer keys (face to face) and keep them secure.', 'Note any child who needs help, and plan a short catch-up at the start of the next lesson.'].forEach(s => G.push(bu(s)));

/* ---------- Parent summary ---------- */
G.push(p(t(PROG, { bold: true, size: 44 }), { pb: true, after: 40 }));
G.push(p(t(SLOGAN, { italics: true, size: 28, color: '1F3864' }), { after: 100 }));
G.push(p(t('A 10-lesson holiday maths program for children finishing Primary 5', { bold: true, size: 26 }), { after: 100 }));
G.push(tx('Your child will spend the holidays as a young mathematician: noticing patterns, testing ideas with real objects and explaining their thinking. Lessons are live online in small groups, hands-on, and built around thinking, not speed.'));
G.push(h2('What your child will do'));
L.lessons.forEach(l => G.push(bu('Lesson ' + l.n + ', ' + l.title + ': ' + l.topic.toLowerCase())));
G.push(h2('How you can help'));
['Ask “How do you know?” when your child tells you an answer.', 'Let your child try first. Please sit nearby, but let them find the answer.', 'Print the workbook and cut-outs before the lesson, and keep scissors, a ruler and a pencil ready.', 'Lesson 5: 24 to 36 small cubes (dice, Lego, sugar cubes) or squared paper. Lesson 9: 20 matchsticks or toothpicks (or squared paper).'].forEach(s => G.push(bu(s)));
G.push(h2('Practical details'));
G.push(tbl([2500, 7400], [['Dates', '[start date] to [end date], two lessons a week'], ['Time', '[day] and [day], [start time] to [end time]'], ['Where', 'Live online video class (link sent after registration)'], ['Group size', '[number] children'], ['Fee', 'S$250 beta fee for all 10 lessons (S$25 a lesson), printed workbook and cut-out kit included'], ['Contact', '[name, phone or email]']].map(r => row([cell(r[0], 2500, { bold: true, fill: 'F2F2F2', size: 20, align: AlignmentType.LEFT, h: 80 }), c2(r[1], 7400, { h: 80 })]))));
G.push(p(t('Math Inquirers Holiday Program is an independent enrichment program. It builds the thinking skills of problem solving but is not affiliated with, run by or endorsed by the Ministry of Education or any school.', { size: 18, italics: true, color: '666666' }), { before: 200, after: 0 }));

const doc = new D.Document({ styles: { default: { document: { run: { font: 'Arial', size: S } } } }, sections: [{ properties: { page }, footers: { default: footer(PROG + ' P5 • Program guide') }, children: G }] });
D.Packer.toBuffer(doc).then(b => { fs.writeFileSync('P5_Holiday_Program_Guide.docx', b); console.log('guide built'); });
