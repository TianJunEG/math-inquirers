const C = require('../hp/common.js');
const { fs, D, CW, t, p, cell, tbl, row, gap, footer, page, AlignmentType, BorderStyle, WidthType } = C;
const L = require('./data.js');
const ST = require('./stories.json');
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
G.push(p(t('PRIMARY 4 HOLIDAY PROGRAM', { bold: true, size: 22, color: '666666' }), { after: 20 }));
G.push(p(t(PROG, { bold: true, size: 52 }), { after: 40 }));
G.push(p(t(SLOGAN, { italics: true, size: 30, color: '1F3864' }), { after: 120 }));
G.push(tx('Program guide for tutors: schedule, lesson routine, ten minute-by-minute lesson scripts with answer keys, a progress tracker and a parent summary. Math Inquirers is online first: every lesson runs live on video; the face-to-face notes are kept for partner centres.'));
G.push(h2('The program at a glance'));
G.push(tbl([2300, 7600], [
  ['Level', 'Children whose school year covers Primary 4 topics (ages 10 to 11), going into P5, who enjoy thinking about maths. Every child gets the same pages and chooses how far to go'],
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
  ['0–4', 'Sneak-peek puzzles', 'Hello (0 to 1), then two sneak-peek puzzles on an idea we have not learnt yet (1 to 4): the first uses objects, a drawing or counting, the second is a thinking question. Guesses and “I do not know” are welcome. Nobody is marked and the answers do not decide who does what.', 'Own paper, held to the camera when the tutor says. Tutor looks only to plan help.', 'Children write on their own paper and hold it to the camera at the same moment, or show only the tutor on camera.'],
  ['4–8', 'Warm-up game and quick questions', 'One short round of the game (4 to 6) and the quick questions (6 to 8). Everyone joins in.', 'Sit in a circle or horseshoe.', 'Cameras on. Answers by thumbs, hands or chat.'],
  ['8–18', 'Explore', 'Hands-on in pairs. Objects first, no writing yet.', 'Materials box on each table.', 'Each child has their own materials at home. Pairs go to breakout rooms.'],
  ['18–30', 'Mini-lesson', 'Tutor builds the table on the board, names the rule and asks what stays the same and what changes.', 'Whiteboard.', 'Shared slide and annotation tool.'],
  ['30–34', 'Brain break', 'Stand, stretch, drink water.', 'A short movement game.', 'Stand up on camera. Count the stretches together.'],
  ['34–80', 'Worksheet', 'Page 1 in pairs (34 to 50), check (50 to 53), short teaching (53 to 58), page 2 alone (58 to 76), check (76 to 80). Tutor asks “how do you know?” rather than giving answers.', 'Printed workbook, tutor circulates.', 'Printed workbook. Child holds the page up to the camera. Tutor checks one or two answers each.'],
  ['80–85', 'Talk time', 'Share one answer and explain it. Compare methods.', 'Each child shares in turn.', 'Each child unmutes in turn.'],
  ['85–88', 'Exit ticket and stamp', 'One question on a slip of paper. Stamp the inquiry journal. (Lesson 10: 85 to 87.)', 'Paper slip, tutor stamps.', 'Child writes the answer and shows the camera. Tutor stamps the next time or posts it.'],
  ['88–90', 'Looking back (2 minutes)', 'Children fill in the small “Looking back” box on page 3, a page every child reaches. Write, tick or pass. Nobody is made to share. Never graded or collected. (Lesson 10: 87 to 89, certificates 89 to 90.)', 'Pencil and workbook.', 'Children write on the printed page. Passing is always allowed. A child who ticks “still stuck” gets a check-in in the open session.']
];
G.push(tbl([900, 1450, 2700, 2300, 2550], [row([hd('Minutes', 900), hd('Part', 1450), hd('What happens', 2700), hd('Face to face', 2300), hd('Online', 2550)]), ...R.map(r => row([c2(r[0], 900, { align: AlignmentType.CENTER, bold: true }), c2(r[1], 1450, { bold: true }), c2(r[2], 2700), c2(r[3], 2300), c2(r[4], 2550)]))]));
G.push(h2('Teaching habits that matter'));
['Ask “How do you know?” after every answer, right or wrong.', 'Wait 10 seconds before helping. Let children struggle a little.', 'Praise the thinking (“You checked it two ways”), not just the answer.', 'Let children disagree with each other and settle it with objects or a drawing.', 'If a child finishes early, use the Challenge or Extension question, not extra drill.'].forEach(s => G.push(bu(s)));

G.push(h2('Preparing the materials'));
['Send the workbook PDF to parents one week before. Ask them to print it single-sided and the cut-out pages on card if they can.', 'Cut-outs used: digit, point, sign and bracket cards (Lessons 2, 3, 5, 10), square grid (Lessons 7, 8), dot grid and cube net (Lesson 8), graph grids (Lesson 9), fraction wall (Lesson 4), right-angle testers (Lesson 6), and a paper clock, pizza circles and what-to-bring page (Lessons 4, 6). Children bring their own clear 180 degree protractor and a 30 cm ruler for Lesson 6.', 'Keep the answer key with the tutor only. Check answers together on screen.', 'Use the shared screen or a digital whiteboard for the mini-lesson table.'].forEach(s => G.push(bu(s)));
G.push(h2('Setting up online'));
['Send parents the workbook and materials list one week before. Needed: the printed workbook and cut-outs, scissors, a ruler, paper and a pencil.', 'Use one approved platform with breakout rooms and screen share. Admit only registered children and never share the link publicly.', 'Ask the parent to sit nearby but not give answers. The camera should show the child’s page and hands.', 'Hold up the answer page to the camera at the end of each lesson, or take a photo and send it through the approved channel.', 'Do not record lessons (this is in the tutor agreement). Add a second tutor or helper above 8 children.'].forEach(s => G.push(bu(s)));

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
const stuck = (lines) => lines.map(x => String(x).replace(/^Stuck( on [^:]{0,40})?:\s*/i, '')).forEach((s, i) => G.push(p([t(i === 0 ? 'IF STUCK   ' : '                ', { bold: true, size: 19, color: 'A61C00' }), t(s, { size: S })], { after: 40, indent: { left: 1300, hanging: 1300 }, line: 280 })));

G.push(h1('Level 4 stories: the mathematicians', true));
G.push(tx('Each lesson has an optional 2-minute Story break at the brain break (after the mini-lesson, before the worksheet): one slide with a short true story and a Try it question, a Story corner box on the workbook page that every child reaches (the Investigation and Looking back page), and a line in the script. Skip it whenever time is short. Stories marked \u201caccounts say\u201d or with uncertain dates are labelled as such on purpose. Dates for people from long ago are estimates.'));
G.push(tbl([700, 2100, 2600, 1700, 2800], [row([hd('Lesson', 700), hd('Person', 2100), hd('Country', 2600), hd('Years', 1700), hd('Link to the lesson', 2800)]), ...ST.map(s => row([c2(String(s.n), 700, { align: AlignmentType.CENTER, bold: true }), c2(s.name, 2100, { bold: true }), c2(s.country, 2600), c2(s.years, 1700), c2(s.link, 2800)]))]));
G.push(tx('Safeguarding and tone: offer the story and the Try it question to the whole group, never to one child by name. Children may pass. No scores or tallies. Keep the Start here / Think harder / Go further names.', { before: 60, size: 19 }));
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
  l = Object.assign({}, l, { gaps: L.content[l.n - 1].gaps });
  const d = DD[String(l.n)], s = SC[l.n], q = QB[String(l.n)];
  G.push(h1('Lesson ' + l.n + ': ' + l.title, true));
  G.push(p(t('Week ' + l.week + (l.session === 'A' ? ' (first lesson)' : ' (second lesson)') + '   •   ' + l.topic + '   •   Workbook: Lesson ' + l.n, { size: 20, color: '666666' }), { after: 80 }));
  G.push(tbl([1900, 8000], [
    ['Objective', l.objective], ['Thinking skills', l.skills], ['Materials', l.materials], ['Online set-up', l.online],
    ['Prepare', 'Solve the worksheet yourself first. Set out one materials box per pair. Open the slides for this lesson and check the answers in the speaker notes.']
  ].map(r => row([cell(r[0], 1900, { bold: true, fill: 'F2F2F2', size: 20, align: AlignmentType.LEFT, h: 60 }), c2(r[1], 8000, { h: 60 })]))));
  G.push(gap(40));

  G.push(seg('0–1 min', 'Opening'));
  say(s.hook);
  doo(['Greet each child by name. Show the lesson title slide. Read “Today we will…” aloud. Keep it to one minute.']);

  G.push(seg('1–4 min', 'Sneak-peek puzzles (3 minutes)'));
  say(['Two sneak-peek puzzles about ' + l.gaps.idea + '. These are ideas we have not learnt yet, so guessing and “I do not know” are welcome. Nobody is marked. Write your answer on your own paper and hold it up to the camera when I say.']);
  doo(['Show the Sneak-peek puzzles slide. Give about 90 seconds per question. Question 1 uses objects, a drawing or counting, so every child can start. Question 2 is a thinking question. Do not teach and do not say who is right yet.',
    'Answers are shown only to you: each child writes on their own paper and holds it to the camera at the same moment (or shows only you, on camera). Keep every part of this in the shared session, and never ask for boards up in front of the group. Walk the group through the answers at the end, using the slide, naming no child, so everyone hears the reasoning.',
    'Use what you see only to plan your help. It does not decide who works on which page. Everyone starts on Start here (page 1) and the invitation is for the WHOLE group: “After question ' + (l.gaps.chooseAfter || 3) + ' you may choose: carry on, or try Think harder. When you have finished Start here you can choose Think harder, Go further or the Investigation.” Never single out or name a child, never announce who is on which page, and do not split a pair unless both children agree. If one child of a pair moves on and the other does not, join the other child to another pair or work with them yourself straight away. Children who choose Think harder or Go further stay in the same room and still join the checks at minutes 50 and 76, talk time, the exit ticket and the reflection.']);
  ask(l.gaps.check.map((x, i) => ['Sneak-peek ' + (i + 1) + (x.kind === 'access' ? ' (objects, drawing or counting)' : ' (thinking)') + ': ' + x.q, x.a]), 'Sneak-peek puzzle', 'Answer');
  doo(['A good reason sounds like: ' + l.gaps.why]);

  G.push(seg('4–8 min', 'Warm-up game and quick questions'));
  doo([d.warmGame + ' (Today play one short round, about 2 minutes, because the Sneak-peek puzzles came first.)']);
  say(s.warmIntro);
  doo(['After the game, ask the quick questions on the warm-up slides. Use thumbs or a whisper to partners before taking answers.']);
  ask(d.warmQs.map(x => [x[0], x[1]]));

  G.push(seg('8–18 min', 'Explore (in pairs, with objects)'));
  say(s.predict);
  doo(d.expSetup.map((x, i) => (i + 1) + '. ' + x));
  say(['Talk to your partner while you work. I will come round and ask you questions.']);
  stuck(s.exploreHints);
  doo(['At about minute 16, say “Pencils down” and bring the group back together. Take the three questions below, one at a time.']);
  ask(d.expAsk.map(x => [x[0], x[1]]));

  G.push(seg('18–30 min', 'Mini-lesson (you teach, they join in)'));
  doo(['Show the mini-lesson slides. Think aloud as you work. Say what you notice, what you test and how you check. Children copy how you think.']);
  say(s.think);
  G.push(tbl([4600, 5300], [row([hd('Worked example on the slides', 4600), hd('Answer', 5300)]), row([c2(d.mini1.head + '. ' + (d.mini1.body || []).join(' '), 4600), c2(d.mini1.ans, 5300)]), row([c2(d.mini2.head + '. ' + (d.mini2.body || []).join(' '), 4600), c2(d.mini2.ans, 5300)])]));
  G.push(gap(40));
  say([d.keyHead.replace(/^Key idea: /, 'The key idea today is: ') + '. ' + d.keyBig + ' Say it with me.']);
  doo(['Show the key idea slide at minutes 29 to 30. The “your turn” slides are optional: skip them if you are short of time. The “common mistakes” on that slide are for you, not the children. Watch for them during the worksheet:']);
  l.mistakes.forEach(m => G.push(bu(m)));

  G.push(seg('30–34 min', 'Brain break'));
  doo([d.brk, 'Water. Toilet break for anyone who needs it. Keep it to four minutes (or two minutes of movement and then the optional story below).']);
  { const st = ST[l.n - 1]; doo(['Story break (optional, 2 minutes): today\u2019s mathematician is ' + st.name + ' (' + st.country + ', ' + st.years + '). ' + st.link + ' Show the Story break slide (it follows the Brain break slide), read the story aloud or ask a volunteer, then offer the Try it question to the whole group. Nobody is marked or ranked.' + (st.label ? ' The story says \u201caccounts say\u201d on purpose: do not turn it into a certain fact.' : ''), 'To skip: say \u201cWe will keep this story for another day\u201d and go straight to the worksheet. Nothing later depends on the story. Try it answer: ' + st.a]); }

  G.push(seg('34–80 min', 'Worksheet (pairs, then alone)'));
  doo(['Minute 34: give out the workbook. Read the title of Lesson ' + l.n + ' aloud. Say “Pairs first. Talk before you write.”', 'Minutes 34 to 50: pairs work together on the first page (online, allow about 2 minutes to move into and out of breakout rooms, or run page 1 as a whole-group screen-share). Minutes 50 to 53: check page 1 together. Minutes 53 to 58: the short teaching before page 2. Minutes 58 to 76: each child works alone on the second page. Minutes 76 to 80: check page 2 together.']);
  say(['Pairs first. Read each question aloud and talk about it before you write. I am not looking for speed. I am looking for good thinking.']);
  doo(['Circulate and ask:']);
  s.circulate.forEach(c => G.push(bu(c)));
  stuck(s.hints);
  doo(['Choosing: after question ' + (l.gaps.chooseAfter || 3) + ' on page 1 every child may carry on or try Think harder. Make the offer to the whole group, never to one child by name. The Think harder page, the Go further page and the Investigation have no fixed time slot: any child may choose them when they have finished Start here, and they are good for take-home. Page 2 is on your own and has a printed note about which questions to do first, so nobody has to rush. Every lesson has an Investigation on page 3, with an easy first step and a model answer in the answer key below: it has several valid answers, so ask “How did you decide?” and “Is there another way?” rather than marking it right or wrong.' + ([3, 4, 5, 7].includes(l.n) ? ' The deck has a slide marked ON DEMAND (and in Lesson 5 two): it is not part of the five-minute teaching before page 2. Show it only while children work on page 2, when a child chooses that choice question, and make the offer to the whole group.' : '')]);
  G.push(h2('Think harder and Go further questions'));
  ask([...(q.stretch || []).slice(0, 4).map((x, i) => ['Workbook Think harder ' + (i + 1) + ': ' + x.q, x.a]), ...(q.challenge || []).slice(-3).map((x, i) => ['Workbook Go further ' + (i + 1) + ': ' + x.q, x.a])], 'Question', 'Answer');
  G.push(tx('These are the questions on the Think harder page and the Go further page in the workbook. More are in the separate Question Bank.', { size: 19, color: '666666' }));

  G.push(seg('80–85 min', 'Talk time'));
  doo(['Bring the group back to a circle (or camera on, mics on). Ask for volunteers first. No cold-calling, nobody has to speak, and passing is always fine. Never keep a tally or scoreboard in front of the group. Praise the reasons, not the speed.']);
  say(s.talk);
  ask([[l.share, s.talkAns]], 'Discussion question', 'Listen for');

  G.push(seg(l.n === 10 ? '85–87 min' : '85–88 min', 'Exit ticket and closing'));
  doo(['Give each child a slip of paper (or ask them to write on their journal page). No talking, no helping. Show the exit ticket slide.']);
  ask([[l.exit.q, l.exit.a]], 'Exit ticket', 'Answer');
  say(s.close);
  doo(['Stamp the inquiry journal when a child hands in their ticket. Mark S, D or H in the progress tracker at the back of this guide. If a child marked D or H, plan two minutes of catch-up at the start of the next lesson.']);
  G.push(seg(l.n === 10 ? '87–89 min' : '88–90 min', 'Looking back (2 minutes)'));
  say(['Turn to page 3, to the small box called Looking back. You can write, tick or pass: you choose. Finish what you like: Something I did well, The hardest part was, What helped me. Two minutes, no talking.', 'Model one yourself first: “' + l.gaps.reflect + '” Ticking “I am still stuck” is a good thing to do: it tells me where to help.']);
  doo(['Run it in two minutes. It is never collected, never graded, never corrected and never shown to the group. You may look at a child’s box only if the child holds it to your camera. Do not ask anyone to read theirs aloud; if a child wants to share, take one volunteer and thank them for the strategy. If “I am still stuck” is ticked, check in during the open session: a quick visit to the shared breakout room or a hand signal, with a parent nearby. Praise the strategy (“you drew it”, “you asked for help”), not the speed or the score.']);
  G.push(h2('Extension: for any child who wants more'));
  G.push(tx(l.extension));
  G.push(h2('Answer key (workbook)'));
  l.key.forEach(k => G.push(p([t(k[0] + '  ', { bold: true, size: 20 }), t(k[1], { size: 20 })], { after: 50, indent: { left: 240 }, line: 270 })));
  G.push(p([t('Investigation  ', { bold: true, size: 20 }), t(l.gaps.invest.head + ' (' + l.gaps.invest.kind.trim() + ') Easy first step: ' + (l.gaps.invest.easy || '') + '  Model answer: ' + l.gaps.invest.key, { size: 20 })], { after: 50, indent: { left: 240 }, line: 270 }));
  G.push(p([t('Go further  ', { bold: true, size: 20 }), t(l.gaps.go2.q + ' ' + l.gaps.go2.a, { size: 20 })], { after: 50, indent: { left: 240 }, line: 270 }));
  G.push(p([t('Story corner try-it  ', { bold: true, size: 20 }), t(ST[l.n - 1].name + ': ' + ST[l.n - 1].q + ' Answer: ' + ST[l.n - 1].a, { size: 20 })], { after: 50, indent: { left: 240 }, line: 270 }));
  G.push(p([t('Sneak-peek puzzles  ', { bold: true, size: 20 }), t(l.gaps.check.map((x, i) => '(' + (i + 1) + ') ' + x.a).join('  '), { size: 20 })], { after: 50, indent: { left: 240 }, line: 270 }));
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
['Circulate and ask questions rather than giving answers.', 'Use only the approved channels to contact parents. Invitations to children go to the whole group and check-ins happen in the open session.', 'Do not take photos or recordings unless the Company has approved it and parents have consented.', 'If you have a concern about a child’s safety or welfare, tell the Company straight away.'].forEach(s => G.push(bu(s)));
G.push(h2('After the lesson'));
['Stamp inquiry journals and fill in the tracker.', 'Collect worksheets and answer keys (face to face) and keep them secure.', 'Note any child who needs help, and plan a short catch-up at the start of the next lesson.'].forEach(s => G.push(bu(s)));

/* ---------- Parent summary ---------- */
G.push(p(t(PROG, { bold: true, size: 44 }), { pb: true, after: 40 }));
G.push(p(t(SLOGAN, { italics: true, size: 28, color: '1F3864' }), { after: 100 }));
G.push(p(t('A 10-lesson holiday maths program for children whose school year covers Primary 4 topics', { bold: true, size: 26 }), { after: 100 }));
G.push(tx('Your child will spend the holidays as a young mathematician: noticing patterns, testing ideas with real objects and explaining their thinking. Lessons are live online in small groups, hands-on, and built around thinking, not speed.'));
G.push(h2('What your child will do'));
L.lessons.forEach(l => G.push(bu('Lesson ' + l.n + ', ' + l.title + ': ' + l.topic.toLowerCase())));
G.push(h2('How you can help'));
['Ask “How do you know?” when your child tells you an answer.', 'Let your child try first. Please sit nearby, but let them find the answer.', 'Print the workbook and cut-outs, and keep scissors, a ruler and a pencil ready.'].forEach(s => G.push(bu(s)));
G.push(h2('Practical details'));
G.push(tbl([2500, 7400], [['Dates', '[start date] to [end date], two lessons a week'], ['Time', '[day] and [day], [start time] to [end time]'], ['Where', 'Live online video class (link sent after registration)'], ['Group size', '[number] children'], ['Fee', 'S$500 introductory (regular S$650), workbook included, payable in 3 instalments'], ['Contact', '[name, phone or email]']].map(r => row([cell(r[0], 2500, { bold: true, fill: 'F2F2F2', size: 20, align: AlignmentType.LEFT, h: 80 }), c2(r[1], 7400, { h: 80 })]))));
G.push(p(t('Math Inquirers Holiday Program is an independent enrichment program. It builds problem-solving and thinking skills and is not affiliated with, run by or endorsed by the Ministry of Education or any school.', { size: 18, italics: true, color: '666666' }), { before: 200, after: 0 }));

const doc = new D.Document({ styles: { default: { document: { run: { font: 'Arial', size: S } } } }, sections: [{ properties: { page }, footers: { default: footer(PROG + ' P4 • Program guide') }, children: G }] });
D.Packer.toBuffer(doc).then(b => { fs.writeFileSync('P4_Holiday_Program_Guide.docx', b); console.log('guide built'); });
