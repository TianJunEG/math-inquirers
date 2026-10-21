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
G.push(p(t('PRIMARY 6 HOLIDAY PROGRAM', { bold: true, size: 22, color: '666666' }), { after: 20 }));
G.push(p(t(PROG, { bold: true, size: 52 }), { after: 40 }));
G.push(p(t(SLOGAN, { italics: true, size: 30, color: '1F3864' }), { after: 120 }));
G.push(tx('Program guide for tutors: schedule, lesson routine, ten minute-by-minute lesson scripts with answer keys, a progress tracker and a parent summary. Math Inquirers is online first: every lesson runs live on video; the face-to-face notes are kept for partner centres.'));
G.push(h2('The program at a glance'));
G.push(tbl([2300, 7600], [
  ['Level', 'Primary 6 students after the PSLE (ages 12), after the PSLE, going into Secondary 1, who are ready for more thinking than standard practice'],
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
const R = [
  ['0–10', 'Warm-up', 'A quick game from the lesson plan. Everyone joins in.', 'Sit in a circle or horseshoe.', 'Cameras on. Answers by thumbs, hands or chat.'],
  ['10–25', 'Explore', 'Hands-on in pairs. Objects first, no writing yet.', 'Materials box on each table.', 'Each child has their own materials at home. Pairs go to breakout rooms.'],
  ['25–35', 'Mini-lesson', 'Tutor builds the table on the board, names the rule and asks what stays the same and what changes.', 'Whiteboard.', 'Shared slide and annotation tool.'],
  ['35–40', 'Brain break', 'Stand, stretch, drink water.', 'A short movement game.', 'Stand up on camera. Count the stretches together.'],
  ['40–75', 'Worksheet', 'Start in pairs, finish alone. Tutor asks “how do you know?” rather than giving answers.', 'Printed workbook, tutor circulates.', 'Printed workbook. Child holds the page up to the camera. Tutor checks one or two answers each.'],
  ['75–82', 'Talk time', 'Share one answer and explain it. Compare methods.', 'Each child shares in turn.', 'Each child unmutes in turn.'],
  ['82–90', 'Exit ticket and stamp', 'One question on a slip of paper. Stamp the inquiry journal.', 'Paper slip, tutor stamps.', 'Child writes the answer and shows the camera. Tutor stamps the next time or posts it.']
];
G.push(tbl([900, 1450, 2700, 2300, 2550], [row([hd('Minutes', 900), hd('Part', 1450), hd('What happens', 2700), hd('Face to face', 2300), hd('Online', 2550)]), ...R.map(r => row([c2(r[0], 900, { align: AlignmentType.CENTER, bold: true }), c2(r[1], 1450, { bold: true }), c2(r[2], 2700), c2(r[3], 2300), c2(r[4], 2550)]))]));
G.push(h2('Teaching habits that matter'));
['Ask “How do you know?” after every answer, right or wrong.', 'Wait 10 seconds before helping. Let children struggle a little.', 'Praise the thinking (“You checked it two ways”), not just the answer.', 'Let children disagree with each other and settle it with objects or a drawing.', 'If a child finishes early, use the Challenge or Extension question, not extra drill.'].forEach(s => G.push(bu(s)));

G.push(h2('Preparing the materials'));
['Send the workbook PDF to parents one week before. Ask them to print it single-sided and the cut-out pages on card if they can.', 'Each child needs a computer or tablet with Scratch 3 (free online). Python is optional (any online Python editor). Cut-outs used: unplugged code cards (Lessons 1, 4, 7), square grid (Lessons 7, 9).', 'Keep the answer key with the tutor only. Check answers together on screen.', 'Use the shared screen or a digital whiteboard for the mini-lesson table.'].forEach(s => G.push(bu(s)));
G.push(h2('Setting up online'));
['Send parents the workbook and materials list one week before. Needed: the printed workbook and cut-outs, scissors, a ruler, paper and a pencil, and a computer with Scratch.', 'Use one approved platform with breakout rooms and screen share. Admit only registered children and never share the link publicly.', 'Ask the parent to sit nearby but not give answers. The camera should show the child’s page and hands.', 'Hold up the answer page to the camera at the end of each lesson, or take a photo and send it through the approved channel.', 'Do not record lessons (this is in the tutor agreement). Add a second tutor or helper above 8 children.'].forEach(s => G.push(bu(s)));

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
const ask = (rows, h1c, h2c) => { G.push(tbl([4600, 5300], [row([hd(h1c || 'Ask', 4600), hd(h2c || 'Expect', 5300)]), ...rows.map(r => row([c2(r[0], 4600), c2(r[1], 5300)]))])); G.push(gap(40)); };
const stuck = (lines) => lines.forEach((s, i) => G.push(p([t(i === 0 ? 'IF STUCK   ' : '                ', { bold: true, size: 19, color: 'A61C00' }), t(s, { size: S })], { after: 40, indent: { left: 1300, hanging: 1300 }, line: 280 })));

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

L.lessons.forEach(l => {
  const d = DD[String(l.n)], s = SC[l.n], q = QB[String(l.n)], gp = L.gaps[String(l.n)];
  G.push(h1('Lesson ' + l.n + ': ' + l.title, true));
  G.push(p(t('Week ' + l.week + (l.session === 'A' ? ' (first lesson)' : ' (second lesson)') + '   •   ' + l.topic + '   •   Workbook: Lesson ' + l.n, { size: 20, color: '666666' }), { after: 80 }));
  G.push(tbl([1900, 8000], [
    ['Objective', l.objective], ['Thinking skills', l.skills], ['Materials', l.materials], ['Online set-up', l.online],
    ['Prepare', 'Solve the worksheet yourself first. Set out one materials box per pair. Open the slides for this lesson and check the answers in the speaker notes.']
  ].map(r => row([cell(r[0], 1900, { bold: true, fill: 'F2F2F2', size: 20, align: AlignmentType.LEFT, h: 60 }), c2(r[1], 8000, { h: 60 })]))));
  G.push(gap(40));
  if (l.n === 10) doo(['Lesson 10 timing: this lesson changes the usual routine, so use this plan instead of the minute marks below. Warm-up 0 to 5; challenge round 5 to 22; starter projects 22 to 29; brain break 29 to 32; plan and build 32 to 62 (a working copy of one starter with one change is full marks); showcase 62 to 87 (3 minutes each plus a 20-second switch); exit ticket and certificates 87 to 90. The slide deck has the same times.']);

  G.push(seg('0–2 min', 'Opening'));
  say(s.hook);
  doo(['Greet each child by name. Show the lesson title slide. Read “Today we will…” aloud.']);

  G.push(seg('2–10 min', 'Warm-up'));
  doo(['Warm-up check first (slide 2, 3 minutes). It comes out of the 10-minute warm-up: play the game for about 3 minutes and ask only the first three quick questions after it.']);
  say(['Two quick puzzles. They are new, not from last time. Write your answer AND one reason on your whiteboard. Hold it up when I say.']);
  ask(gp.check.map(x => [x[0], x[1]]), 'Warm-up check', 'Answer and the reason to listen for');
  doo(['Fast track (nobody is labelled). If a child has BOTH answers right and a sensible reason, send a private chat message: “Today start on the Think Harder page at minute 40.” Fast-track children still join Explore, the mini-lesson and Talk time; only the worksheet time changes. Tell everyone: “Some of you start on a different page today. It changes every lesson, and you can move any time.” Never say “advanced”, never record the check as a mark, and let any child choose the main pages. A fast-track child who gets stuck goes back to the main page. This works because groups are small (up to 8) and each child has a printed workbook, so you can give children different pages quietly.']);
  doo([d.warmGame]);
  say(s.warmIntro);
  doo(['After the game, ask the quick questions on the warm-up slides. Use thumbs or a whisper to partners before taking answers.']);
  ask(d.warmQs.map(x => [x[0], x[1]]));

  G.push(seg('10–25 min', 'Explore (in pairs, with objects)'));
  say(s.predict);
  doo(d.expSetup.map((x, i) => (i + 1) + '. ' + x));
  say(['Talk to your partner while you work. I will come round and ask you questions.']);
  stuck(s.exploreHints);
  doo(['At about minute 22, say “Pencils down” and bring the group back together. Take the three questions below, one at a time.']);
  ask(d.expAsk.map(x => [x[0], x[1]]));

  G.push(seg('25–35 min', 'Mini-lesson (you teach, they join in)'));
  doo(['Show the mini-lesson slides. Think aloud as you work. Say what you notice, what you test and how you check. Children copy how you think.']);
  say(s.think);
  G.push(tbl([4600, 5300], [row([hd('Worked example on the slides', 4600), hd('Answer', 5300)]), row([c2(d.mini1.head + '. ' + (d.mini1.body || []).join(' '), 4600), c2(d.mini1.ans, 5300)]), row([c2(d.mini2.head + '. ' + (d.mini2.body || []).join(' '), 4600), c2(d.mini2.ans, 5300)])]));
  G.push(gap(40));
  say([d.keyHead.replace(/^Key idea: /, 'The key idea today is: ') + '. ' + d.keyBig + ' Say it with me.']);
  doo(['Show the key idea slide at minutes 33 to 35. The “common mistakes” on that slide are for you, not the children. Watch for them during the worksheet:']);
  l.mistakes.forEach(m => G.push(bu(m)));

  G.push(seg('35–40 min', 'Brain break'));
  doo([d.brk, 'Water. Toilet break for anyone who needs it. Keep it to five minutes.']);

  G.push(seg('40–75 min', 'Worksheet (pairs, then alone, then stretch)'));
  doo(['Minute 40: give out the workbook. Read the title of Lesson ' + l.n + ' aloud. Say “Pairs first. Talk before you write.”', 'Minutes 40 to 55: pairs work together on the first page (with the short teaching slides). Minutes 55 to 72: each child works alone on the second page. Minutes 72 to 75: check together, then stretch and challenge for early finishers.']);
  say(['Pairs first. Read each question aloud and talk about it before you write. I am not looking for speed. I am looking for good thinking.']);
  doo(['Circulate and ask:']);
  s.circulate.forEach(c => G.push(bu(c)));
  stuck(s.hints);
  doo(['Early finishers: give the stretch question first, then the challenge, then the Open investigation (it is the last box on the second Think Harder page). Fast-track children start there at minute 40.']);
  G.push(h2('Stretch and challenge questions'));
  ask([...(q.stretch || []).slice(0, 4).map((x, i) => ['Workbook Think Harder ' + (i + 1) + ': ' + x.q, x.a]), ...(q.challenge || []).slice(-3).map((x, i) => ['Workbook Challenge ' + (i + 5) + ': ' + x.q, x.a]), ['Workbook Open investigation (' + gp.inv.kind + '): ' + gp.inv.q, gp.inv.a]], 'Question', 'Answer');
  G.push(tx('These are the questions on the two Think Harder pages in the workbook. More are in the separate Question Bank.', { size: 19, color: '666666' }));

  G.push(seg('75–82 min', 'Talk time'));
  doo(['Bring the group back to a circle (or camera on, mics on). Ask two or three children to share, not only the fastest.']);
  say(s.talk);
  ask([[l.share, s.talkAns]], 'Discussion question', 'Listen for');

  G.push(seg('82–90 min', 'Exit ticket and closing'));
  doo(['Give each child a slip of paper (or ask them to write on their journal page). No talking, no helping. Show the exit ticket slide.']);
  ask([[l.exit.q, l.exit.a]], 'Exit ticket', 'Answer');
  say(s.close);
  G.push(h2('Reflection: What was hard? (1 minute)'));
  say(['Last minute, just for you. On the last page of today’s lesson, finish the three sentences in the box called “What was hard?”: the hardest part was, I got unstuck by, next time I will try. Nobody marks it, and nobody has to show it. Then I would like to hear ONE sentence from two or three of you. “Pass” is fine.']);
  doo(['Run it at about minute 88, while you collect exit tickets (slide at the end). Never grade or correct it, and never read it out without the child’s say-so. Praise the strategy, not the speed: say “you ' + gp.reflectEx + ' — that is what got you unstuck”, never “you were quick”. If a child writes “nothing was hard”, ask “what would make it harder?”.']);
  doo(['Stamp the inquiry journal when a child hands in their ticket. Mark S, D or H in the progress tracker at the back of this guide. If a child marked D or H, plan two minutes of catch-up at the start of the next lesson.']);
  G.push(h2('Extension for children who are ready'));
  G.push(tx(l.extension));
  G.push(h2('Answer key (workbook)'));
  l.key.forEach(k => G.push(p([t(k[0] + '  ', { bold: true, size: 20 }), t(k[1], { size: 20 })], { after: 50, indent: { left: 240 }, line: 270 })));
  G.push(p([t('Investigation  ', { bold: true, size: 20 }), t(gp.inv.a, { size: 20 })], { after: 50, indent: { left: 240 }, line: 270 }));
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
['Circulate and ask questions rather than giving answers.', 'Use only the approved channels to contact parents. No private messages to children.', 'Do not take photos or recordings unless the Company has approved it and parents have consented.', 'If you have a concern about a child’s safety or welfare, tell the Company straight away.'].forEach(s => G.push(bu(s)));
G.push(h2('After the lesson'));
['Stamp inquiry journals and fill in the tracker.', 'Collect worksheets and answer keys (face to face) and keep them secure.', 'Note any child who needs help, and plan a short catch-up at the start of the next lesson.'].forEach(s => G.push(bu(s)));

/* ---------- Parent summary ---------- */
G.push(p(t(PROG, { bold: true, size: 44 }), { pb: true, after: 40 }));
G.push(p(t(SLOGAN, { italics: true, size: 28, color: '1F3864' }), { after: 100 }));
G.push(p(t('A 10-lesson holiday maths program for Primary 6 students after the PSLE', { bold: true, size: 26 }), { after: 100 }));
G.push(tx('Your child will spend the holidays as a young mathematician: noticing patterns, testing ideas with real objects and explaining their thinking. Lessons are live online in small groups, hands-on, and built around thinking, not speed.'));
G.push(h2('What your child will do'));
L.lessons.forEach(l => G.push(bu('Lesson ' + l.n + ', ' + l.title + ': ' + l.topic.toLowerCase())));
G.push(h2('How you can help'));
['Ask “How do you know?” when your child tells you an answer.', 'Let your child try first. Please sit nearby, but let them find the answer.', 'Print the workbook and cut-outs, and keep scissors, a ruler and a pencil ready.'].forEach(s => G.push(bu(s)));
G.push(h2('Practical details'));
G.push(tbl([2500, 7400], [['Dates', '[start date] to [end date], two lessons a week'], ['Time', '[day] and [day], [start time] to [end time]'], ['Where', 'Live online video class (link sent after registration)'], ['Group size', '[number] children'], ['Fee', 'S$500 introductory (regular S$650), workbook included, payable in 3 instalments'], ['Contact', '[name, phone or email]']].map(r => row([cell(r[0], 2500, { bold: true, fill: 'F2F2F2', size: 20, align: AlignmentType.LEFT, h: 80 }), c2(r[1], 7400, { h: 80 })]))));
G.push(p(t('Math Inquirers Holiday Program is an independent enrichment program. It is inspired by gifted-education-style thinking skills but is not affiliated with, run by or endorsed by the Ministry of Education or any school.', { size: 18, italics: true, color: '666666' }), { before: 200, after: 0 }));

const doc = new D.Document({ styles: { default: { document: { run: { font: 'Arial', size: S } } } }, sections: [{ properties: { page }, footers: { default: footer(PROG + ' P6 • Program guide') }, children: G }] });
D.Packer.toBuffer(doc).then(b => { fs.writeFileSync('P6_Holiday_Program_Guide.docx', b); console.log('guide built'); });
