const C = require('../hp/common.js');
const { fs, D, CW, t, p, cell, tbl, row, gap, footer, page, AlignmentType, BorderStyle, WidthType } = C;
const L = require('./data.js');
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
  ['Level', 'Children whose school year covers Primary 5 topics (ages 10 to 12), going into P6, the PSLE year, who are ready for more thinking than standard practice'],
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

/* ---------- Routine ---------- */
G.push(h1('The 90-minute lesson routine', true));
G.push(tx('Every lesson uses the same routine so children know what to expect and tutors can prepare quickly.'));
const R = L.timeline;
G.push(tbl([1000, 2600, 6300], [row([hd('Minutes', 1000), hd('Part', 2600), hd('What happens', 6300)]), ...R.map(r => row([c2(r[0], 1000, { align: AlignmentType.CENTER, bold: true }), c2(r[1], 2600, { bold: true }), c2(r[2], 6300)]))]));
G.push(tx('This is the one timeline used by the slides, the scripts and the workbook. Online, children keep cameras on and share work by holding paper to the camera or by showing it to the tutor only, on camera. Face to face, children sit in pairs and the tutor circulates.', { before: 60 }));
G.push(h2('Teaching habits that matter'));
['Ask “How do you know?” after every answer, right or wrong.', 'Wait 10 seconds before helping. Let children struggle a little.', 'Talk time is by invitation: ask for volunteers first, never cold-call a child by name, always allow “pass”, and never keep public tallies or rankings.', 'Praise the thinking (“You checked it two ways”), not just the answer.', 'Let children disagree with each other and settle it with objects or a drawing.', 'If a child finishes early, offer the Go further what-if or the Investigation, not extra drill.'].forEach(s => G.push(bu(s)));

G.push(h2('Preparing the materials'));
['Send the workbook PDF to parents one week before. Ask them to print it single-sided and the cut-out pages on card if they can.', 'Cut-outs used: square grid and dot grid (Lessons 4, 8), fraction wall (Lessons 2, 3), cube net (Lesson 5). Children need a protractor and a ruler.', 'Keep the answer key with the tutor only. Check answers together on screen.', 'Use the shared screen or a digital whiteboard for the mini-lesson table.'].forEach(s => G.push(bu(s)));
G.push(h2('Setting up online'));
['Send parents the workbook and materials list one week before. Needed: the printed workbook and cut-outs, scissors, a ruler, paper and a pencil.', 'Use one approved platform with breakout rooms and screen share. Admit only registered children and never share the link publicly.', 'Ask the parent to sit nearby but not give answers. The camera should show the child’s page and hands.', 'Hold up the answer page to the camera at the end of each lesson, or ask the parent to take a photo and send it to the tutor through the approved parent channel (the child does not send it directly).', 'Do not record lessons (this is in the tutor agreement). Add a second tutor or helper above 8 children.'].forEach(s => G.push(bu(s)));

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
['Every lesson starts with 3 minutes of sneak-peek puzzles: two puzzles on ideas we have not learnt yet. The first is an access puzzle any child can try with objects, drawing or counting, so everybody starts with a win. The second is a thinking puzzle. Say clearly: guessing and “I do not know” are welcome and nobody is marked.', 'Answers are shown privately: on the child’s own paper held to you as you walk round. Online, everyone holds their paper up to the camera at the same moment, or shows it to you only, on camera. Never use boards in front of the group, never read answers out with names, never keep a tally or a ranking. Ask for volunteers to say how they thought.', 'Choosing a start: every child has the same neutral line on workbook page 1, “After question 3 you may choose: carry on, or try Think harder.” (In Lesson 1 the line says “After question 2”.) Invite the WHOLE group, never one child: "when you have finished Start here you can choose Think harder, Go further or the Investigation." Never announce who is on which page, never name a child in front of the group for this, and do not split a pair unless both children agree. Any child may swap at any time. The Go further what-if on the explore slide and the Investigation (printed on the page every child gets) give anyone more to do without waiting.', 'Every lesson ends with a 2-minute reflection in a small box on the Investigation and reflection page: “Something I did well”, “The hardest part was...”, “What helped me” ticks that include “I asked for help” and “I am still stuck”, and “Next time I will try ...”. Pass is always allowed. It is never collected or read out in public; you may read it to plan the next lesson. Follow-up for “I am still stuck” is defined: in the NEXT lesson, in the open session, at minutes 37 to 49 (page 1 pair work), visit those children first in their shared breakout room with the camera on and a parent nearby (face to face: at their table), and go through the idea with one worked example. You may also re-teach the most-ticked idea to the whole group in the warm-up. After Lesson 10 there is no next lesson, so the follow-up goes to the parent through the approved parent channel. Praise strategy, not speed.',
 'Open think time: minutes 62 to 72 of every lesson are protected, 10 quiet minutes for any child who wants a longer problem (Think harder, Go further or the Investigation). No hints unless a child asks and no calling on anyone. Children still on Start here carry on with it. It is open to every child, never announced as a group for particular children.'].forEach(s => G.push(bu(s)));
G.push(h2('Answering a wrong answer'));
ask([
  ['A child gives a wrong answer', '“Thank you. Let us test it with the counters.” Then build it together.'],
  ['A child gives a right answer but cannot explain', '“Show me with your counters.” Then: “Tell your partner how you know.”'],
  ['A child says “I do not know”', '“What do you notice? What could you try first?” Offer hint 1.'],
  ['Two children disagree', '“Both of you, convince the group using objects.” Let the objects decide.']
], 'If…', 'Then…');

L.lessons.forEach(l => {
  const d = DD[String(l.n)], s = SC[l.n], q = QB[String(l.n)];
  G.push(h1('Lesson ' + l.n + ': ' + l.title, true));
  G.push(p(t('Week ' + l.week + (l.session === 'A' ? ' (first lesson)' : ' (second lesson)') + '   •   ' + l.topic + '   •   Workbook: Lesson ' + l.n, { size: 20, color: '666666' }), { after: 80 }));
  G.push(tbl([1900, 8000], [
    ['Objective', l.objective], ['Thinking skills', l.skills], ['Materials', l.materials], ['Online set-up', l.online],
    ['Prepare', 'Solve the worksheet yourself first. Set out one materials box per pair. Open the slides for this lesson and check the answers in the speaker notes.']
  ].map(r => row([cell(r[0], 1900, { bold: true, fill: 'F2F2F2', size: 20, align: AlignmentType.LEFT, h: 60 }), c2(r[1], 8000, { h: 60 })]))));
  G.push(gap(40));

  G.push(seg('0 min', 'Opening (before the clock starts)'));
  say(s.hook);
  doo(['Greet each child by name. Show the lesson title slide. Read “Today we will…” aloud.']);

  G.push(seg('0–3 min', 'Sneak-peek puzzles (private answers)'));
  ask(d.check.map((x, i) => [(i === 0 ? 'Puzzle 1 (access): ' : 'Puzzle 2 (thinking): ') + x[0], x[1]]), 'Puzzle', 'Listen for');
  doo(s.check);
  G.push(seg('3–9 min', 'Warm-up'));
  doo(['Minutes 3 to 9: the warm-up game below (one or two rounds only) and then the quick questions. If you are short of time, ask only the first three quick questions.']);
  doo([d.warmGame]);
  say(s.warmIntro);
  doo(['After the game, ask the quick questions on the warm-up slides. Use thumbs or a whisper to partners before taking answers.']);
  ask(d.warmQs.map(x => [x[0], x[1]]));

  G.push(seg('9–21 min', 'Explore (in pairs, with objects)'));
  say(s.predict);
  doo(d.expSetup.map((x, i) => (i + 1) + '. ' + x));
  say(['Talk to your partner while you work. I will come round and ask you questions.']);
  stuck(s.exploreHints);
  doo(['Go further what-if (on the second explore slide, for anyone who wants more, so nobody waits): ' + d.whatIf[0] + ' (Answer: ' + d.whatIf[1] + ')', 'At about minute 19, say “Pencils down” and bring the group back together. Take the three questions below, one at a time.']);
  ask(d.expAsk.map(x => [x[0], x[1]]));

  G.push(seg('21–33 min', 'Mini-lesson (you teach, they join in)'));
  doo(['Show the mini-lesson slides. Think aloud as you work. Say what you notice, what you test and how you check. Children copy how you think.']);
  say(s.think);
  G.push(tbl([4600, 5300], [row([hd('Worked example on the slides', 4600), hd('Answer', 5300)]), row([c2(d.mini1.head + '. ' + (d.mini1.body || []).join(' '), 4600), c2(d.mini1.ans, 5300)]), row([c2(d.mini2.head + '. ' + (d.mini2.body || []).join(' '), 4600), c2(d.mini2.ans, 5300)])]));
  G.push(gap(40));
  say([d.keyHead.replace(/^Key idea: /, 'The key idea today is: ') + '. ' + d.keyBig + ' Say it with me.']);
  doo(['Show the key idea slide at minutes 32 to 33. The “common mistakes” on that slide are for you, not the children. Watch for them during the worksheet:']);
  l.mistakes.forEach(m => G.push(bu(m)));

  G.push(seg('33–37 min', 'Brain break'));
  doo([d.brk, 'Water. Toilet break for anyone who needs it. Keep it to four minutes.']);

  G.push(seg('37–72 min', 'Workbook (page 1 in pairs, check, teaching, page 2 alone)'));
  doo(['Minute 37: give out the workbook. Say “Pairs first. Talk before you write.”', 'Minutes 37 to 49: pairs work on page 1. Minutes 49 to 53: check page 1 together (four minutes, so every part can be explained). Minutes 53 to 58: the short teaching slides for the page 2 question types. Minutes 58 to 72: each child works alone on page 2; it is a menu, not a wall, so nobody has to finish, and minutes 62 to 72 are protected open think time for Think harder, Go further or the Investigation. Minutes 72 to 76: check page 2 together.']);
  say(['Pairs first. Read each question aloud and talk about it before you write. I am not looking for speed. I am looking for good thinking.', 'After question ' + L.choiceAfter(l.n) + ' you may choose: carry on, or try Think harder. You can swap at any time.']);
  doo(['Circulate and ask:']);
  s.circulate.forEach(c => G.push(bu(c)));
  stuck(s.hints);
  doo(['Quick finishers: offer the Go further page or the Investigation. Everyone has the same neutral line on page 1. Invite the whole group ("when you have finished Start here you can choose Think harder, Go further or the Investigation"); never single out a child, never announce who is on which page, and do not split a pair unless both children agree.']);
  ask([['Investigation (printed on the Investigation and reflection page every child gets): ' + l.title + ' (' + INV[l.n].title + ')', 'First step for everyone: ' + INV[l.n].first + ' ' + INV[l.n].parts.map((x, i) => '(' + 'abc'[i] + ') ' + x).join(' ')], ['What to look for / model answer', INV[l.n].a]], 'Investigation', 'Detail');
  G.push(h2('Think harder and Go further questions'));
  ask([...(q.stretch || []).slice(0, 4).map((x, i) => ['Workbook Think harder ' + (i + 1) + ': ' + x.q, x.a]), ...(q.challenge || []).slice(-3).map((x, i) => ['Workbook Go further ' + (i + 5) + ': ' + x.q, x.a])], 'Question', 'Answer');
  G.push(tx('These are the questions on the Think harder and Go further pages in the workbook. More are in the separate Question Bank.', { size: 19, color: '666666' }));

  G.push(seg('76–82 min', 'Talk time'));
  doo(L.scripts[l.n].talkRules.concat(['Bring the group back to a circle (or camera on, mics on). Pairs talk for 2 minutes first.']));
  say(s.talk);
  ask([[l.share, s.talkAns]], 'Discussion question', 'Listen for');

  G.push(seg('82–90 min', 'Exit ticket, reflection and closing'));
  doo(['Give each child a slip of paper (or ask them to write on their journal page). No talking, no helping. Show the exit ticket slide.']);
  ask([[l.exit.q, l.exit.a]], 'Exit ticket', 'Answer');
  say(s.close);
  doo(s.reflect);
  doo(['Stamp the inquiry journal when a child hands in their ticket. Mark S, D or H in the progress tracker at the back of this guide (private to you, never shown to children). If a child is marked D or H, plan two minutes of catch-up at the start of the next lesson.']);
  G.push(h2('Extension for anyone who wants more'));
  G.push(tx(l.extension));
  G.push(h2('Answer key (workbook)'));
  l.key.forEach(k => G.push(p([t(k[0] + '  ', { bold: true, size: 20 }), t(k[1], { size: 20 })], { after: 50, indent: { left: 240 }, line: 270 })));
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
['Circulate and ask questions rather than giving answers.', 'Contact parents only through the approved channels. All contact with children stays in the open session: invitations are made to the whole group, and check-ins happen in the shared room with a parent nearby.', 'Do not take photos or recordings unless the Company has approved it and parents have consented.', 'If you have a concern about a child’s safety or welfare, tell the Company straight away.'].forEach(s => G.push(bu(s)));
G.push(h2('After the lesson'));
['Stamp inquiry journals and fill in the tracker.', 'Collect worksheets and answer keys (face to face) and keep them secure.', 'Note any child who needs help, and plan a short catch-up at the start of the next lesson.'].forEach(s => G.push(bu(s)));

/* ---------- Parent summary ---------- */
G.push(p(t(PROG, { bold: true, size: 44 }), { pb: true, after: 40 }));
G.push(p(t(SLOGAN, { italics: true, size: 28, color: '1F3864' }), { after: 100 }));
G.push(p(t('A 10-lesson holiday maths program for children whose school year covers Primary 5 topics', { bold: true, size: 26 }), { after: 100 }));
G.push(tx('Your child will spend the holidays as a young mathematician: noticing patterns, testing ideas with real objects and explaining their thinking. Lessons are live online in small groups, hands-on, and built around thinking, not speed.'));
G.push(h2('What your child will do'));
L.lessons.forEach(l => G.push(bu('Lesson ' + l.n + ', ' + l.title + ': ' + l.topic.toLowerCase())));
G.push(h2('How you can help'));
['Ask “How do you know?” when your child tells you an answer.', 'Let your child try first. Please sit nearby, but let them find the answer.', 'Print the workbook and cut-outs before the lesson, and keep scissors, a ruler and a pencil ready.', 'Lesson 5: 24 to 36 small cubes (dice, Lego, sugar cubes) or squared paper. Lesson 9: 20 matchsticks or toothpicks (or squared paper).'].forEach(s => G.push(bu(s)));
G.push(h2('Practical details'));
G.push(tbl([2500, 7400], [['Dates', '[start date] to [end date], two lessons a week'], ['Time', '[day] and [day], [start time] to [end time]'], ['Where', 'Live online video class (link sent after registration)'], ['Group size', '[number] children'], ['Fee', 'S$500 introductory (regular S$650), workbook included, payable in 3 instalments'], ['Contact', '[name, phone or email]']].map(r => row([cell(r[0], 2500, { bold: true, fill: 'F2F2F2', size: 20, align: AlignmentType.LEFT, h: 80 }), c2(r[1], 7400, { h: 80 })]))));
G.push(p(t('Math Inquirers Holiday Program is an independent enrichment program. It builds the thinking skills of problem solving but is not affiliated with, run by or endorsed by the Ministry of Education or any school.', { size: 18, italics: true, color: '666666' }), { before: 200, after: 0 }));

const doc = new D.Document({ styles: { default: { document: { run: { font: 'Arial', size: S } } } }, sections: [{ properties: { page }, footers: { default: footer(PROG + ' P5 • Program guide') }, children: G }] });
D.Packer.toBuffer(doc).then(b => { fs.writeFileSync('P5_Holiday_Program_Guide.docx', b); console.log('guide built'); });
