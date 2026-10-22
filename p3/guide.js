const C = require('../hp/common.js');
const { fs, D, CW, t, p, cell, tbl, row, gap, footer, page, AlignmentType, BorderStyle, WidthType } = C;
const L = require('./data.js');
const PROG = L.program, SLOGAN = L.slogan;
const GF = JSON.parse(fs.readFileSync(__dirname + '/gifted.json', 'utf8'));
const plain = x => String(x).replace(/\[\[(\d+)\/(\d+)\]\]/g, '$1/$2');
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
G.push(p(t('PRIMARY 3 HOLIDAY PROGRAM', { bold: true, size: 22, color: '666666' }), { after: 20 }));
G.push(p(t(PROG, { bold: true, size: 52 }), { after: 40 }));
G.push(p(t(SLOGAN, { italics: true, size: 30, color: '1F3864' }), { after: 120 }));
G.push(tx('Program guide for tutors: schedule, lesson routine, ten minute-by-minute lesson scripts with answer keys, a progress tracker and a parent summary. Math Inquirers is online first: every lesson runs live on video; the face-to-face notes are kept for partner centres.'));
G.push(h2('The program at a glance'));
G.push(tbl([2300, 7600], [
  ['Level', 'Children finishing Primary 3 (ages 9 to 10), going into P4, who are ready for more thinking than standard practice'],
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
  ['0–10', 'Opening and warm-up', '0 to 2 opening. 2 to 5 sneak-peek puzzles (private answers, nobody marked). 5 to 8 a quick game. 8 to 10 five quick questions.', 'Sit in a circle or horseshoe.', 'Cameras on. Sneak-peek answers on paper held to the tutor, or by private chat. Game answers by thumbs or hands.'],
  ['10–25', 'Explore', 'Hands-on in pairs. Objects first, no writing yet.', 'Materials box on each table.', 'Each child has their own materials at home. Pairs go to breakout rooms.'],
  ['25–35', 'Mini-lesson', 'Tutor builds the table on the board, names the rule and asks what stays the same and what changes.', 'Whiteboard.', 'Shared slide and annotation tool.'],
  ['35–40', 'Brain break', 'Stand, stretch, drink water.', 'A short movement game.', 'Stand up on camera. Count the stretches together.'],
  ['40–70', 'Worksheet', 'Page 1 (Start here) in pairs, short teaching, page 2 alone. After question 3 any child may choose Think harder or the Investigation. Tutor asks “how do you know?” rather than giving answers.', 'Printed workbook, tutor circulates.', 'Printed workbook. Child holds the page up to the camera privately (not to the group). Tutor checks one or two answers each.'],
  ['70–80', 'Talk time', 'Share one answer and explain it. Compare methods.', 'Volunteers share. Passing is always fine.', 'Volunteers unmute. The tutor asks for volunteers first, never calls a child by name cold, and keeps no public tallies or rankings.'],
  ['80–90', 'Exit ticket, look back and stamp', '80 to 86 exit ticket on a slip of paper. 86 to 88 look back (2 minutes, short and safe, pass allowed). 88 to 90 stamp the inquiry journal and close.', 'Paper slip, tutor stamps.', 'Child writes the answer and shows it to the tutor only. Tutor stamps the next time or posts it.']
];
G.push(tbl([900, 1450, 2700, 2300, 2550], [row([hd('Minutes', 900), hd('Part', 1450), hd('What happens', 2700), hd('Face to face', 2300), hd('Online', 2550)]), ...R.map(r => row([c2(r[0], 900, { align: AlignmentType.CENTER, bold: true }), c2(r[1], 1450, { bold: true }), c2(r[2], 2700), c2(r[3], 2300), c2(r[4], 2550)]))]));
G.push(h2('Teaching habits that matter'));
['Ask “How do you know?” after every answer, right or wrong. Never mark or compare children in front of the group.', 'Wait 10 seconds before helping. Let children struggle a little.', 'Praise the thinking (“You checked it two ways”), not just the answer.', 'Let children disagree with each other and settle it with objects or a drawing.', 'If a child wants more, point to Think harder, Go further or the Investigation, not extra drill. Never label children.'].forEach(s => G.push(bu(s)));

G.push(h2('Sneak-peek puzzles, choice and look-back (every lesson)'));
['Sneak-peek puzzles (minutes 2 to 5): two small puzzles on ideas we have not learnt yet. Puzzle 1 is an access puzzle that any child can try with objects, a drawing or counting, so everyone has a first win. Puzzle 2 is a thinking puzzle. Say: “These are ideas we have not learnt yet. Guessing and I do not know are welcome. Nobody is marked.” Children show answers privately (their own paper held up to you, or a private chat message), never boards held up together, never read out.', 'Choice, not sorting: there are no public labels. Every child gets the same Start here pages. After question 3 of page 1 any child may carry on, or try Think harder (and Go further). The Investigation is open to everyone; its easy first step is printed on page 2 of Start here and on the Investigation page. You may quietly invite a child by private chat message (never by name in front of the group). You never announce who is on which page, and pairs are not split unless both children agree.', 'Go further on the explore slide: a second what-if question is on the explore slide from minute 10 so that nobody waits. Any pair may take it up when their first task is done.', 'Talk time: ask for volunteers first. A pass is always fine, and so is sharing with a partner. Do not cold-call by name. Do not keep public tallies or rankings.', 'Look back (minutes 86 to 88, two minutes): Something I did well, The hardest part was, What helped me. A pass is always allowed. The page is never collected or read out; children keep it. A child who ticks “I am still stuck” may show the page to you privately or send a private chat message; you may read a page privately and check in quietly.'].forEach(s => G.push(bu(s)));
G.push(h2('Preparing the materials'));
['Send the workbook PDF to parents one week before. Ask them to print it single-sided and the cut-out pages on card if they can.', 'Cut-outs used: digit cards (Lessons 1, 2), fraction wall (Lesson 6), square grid (Lesson 7), right-angle tester (Lesson 8), play coins and notes (Lesson 9).', 'Keep the answer key with the tutor only. Check answers together on screen.', 'Use the shared screen or a digital whiteboard for the mini-lesson table.'].forEach(s => G.push(bu(s)));
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
  const d = DD[String(l.n)], s = SC[l.n], q = QB[String(l.n)];
  G.push(h1('Lesson ' + l.n + ': ' + l.title, true));
  G.push(p(t('Week ' + l.week + (l.session === 'A' ? ' (first lesson)' : ' (second lesson)') + '   •   ' + l.topic + '   •   Workbook: Lesson ' + l.n, { size: 20, color: '666666' }), { after: 80 }));
  G.push(tbl([1900, 8000], [
    ['Objective', l.objective], ['Thinking skills', l.skills], ['Materials', l.materials], ['Online set-up', l.online],
    ['Prepare', 'Solve the worksheet yourself first. Set out one materials box per pair. Open the slides for this lesson and check the answers in the speaker notes.']
  ].map(r => row([cell(r[0], 1900, { bold: true, fill: 'F2F2F2', size: 20, align: AlignmentType.LEFT, h: 60 }), c2(r[1], 8000, { h: 60 })]))));
  G.push(gap(40));

  G.push(seg('0–2 min', 'Opening'));
  say(s.hook);
  doo(['Greet each child by name. Show the lesson title slide. Read “Today we will…” aloud.']);

  G.push(seg('2–10 min', 'Sneak-peek puzzles (2–5), warm-up game (5–8) and quick questions (8–10)'));
  const gf = GF[String(l.n)], PL = gf.plan;
  say(['Here are two sneak-peek puzzles. These are ideas we have not learnt yet, so guessing is welcome and so is “I do not know”. Nobody is marked. Show me your answer privately: hold your paper up to me, or send me a private message.']);
  doo(['Show the “Sneak-peek puzzles” slide (minutes 2 to 5). Read puzzle 1 aloud and give about 1 minute: it is an access puzzle, so any child can try it with objects, a drawing or counting. Then puzzle 2, about 1 minute, the thinking puzzle. Look at the papers or private messages quietly. Do not show the answers on the slide and do not read answers out. Say “thank you” to everyone in the same way.',
    'Nobody is labelled. Never say who got it, who is on which page, or “fast group” or “top group”. You may use what you see to decide whom to invite quietly, by private chat message, to try Think harder today. It is an invitation, never a ranking: every child can choose Think harder or the Investigation after question 3 of page 1. We come back to puzzle 2 in talk time, for volunteers.']);
  ask(gf.check.map((c, i) => ['Puzzle ' + (i + 1) + (i === 0 ? ' (access): ' : ' (thinking): ') + plain(c.q), plain(c.a) + '. Listen for: ' + plain(c.why)]), 'Sneak-peek puzzle', 'Answer (tutor only) and what to listen for');
  G.push(h2('Choice during the lesson (groups of 8, online)'));
  ['Minutes 10 to 40 (explore, mini-lesson, brain break): everyone does the same. The explore slide has a Go further what-if from minute 10, so a pair that has finished its first task has real work at once. Do not say who is ready for it.',
   'Minute 40: everyone opens Start here page 1 and works in pairs. A line at the top says: “After question 3 you may choose: carry on, or try Think harder.” You never announce who is on which page. If you want a particular child to try Think harder, send a quiet private chat message (never by name in front of the group). Do not split a pair unless both children agree.',
   'The first-step help for the Investigation is printed on page 2 of Start here, so every child sees it. At about minute 52, check in with two or three children for two minutes each, including children on Start here: ask “how do you know?”, not “is it done?”.',
   'Minute ' + PL.stretch[0] + ': everyone chooses what to do next: finish page 2, Think harder, Go further or the Investigation. Everyone is back together for talk time at minute 70.',
   'Next lesson everything starts again from the same pages: nobody is on a track.'].forEach(x => G.push(bu(x)));
  doo(['Warm-up game (minutes 5 to 8). Now the game, then the quick questions (minutes 8 to 10): ' + d.warmGame]);
  say(s.warmIntro);
  doo(['After the game, ask the quick questions on the warm-up slides. Use thumbs or a whisper to partners before taking answers.']);
  ask(d.warmQs.map(x => [x[0], x[1]]));

  G.push(seg('10–25 min', 'Explore (in pairs, with objects)'));
  say(s.predict);
  doo(d.expSetup.map((x, i) => (i + 1) + '. ' + x));
  say(['Talk to your partner while you work. I will come round and ask you questions.']);
  stuck(s.exploreHints);
  doo(['Pairs work from minute 10. If a pair finishes the first task, they may take the Go further what-if on the slide (do not say who). At about minute 15 bring the group back together and take the three questions below, one at a time (minutes 15 to 25).']);
  ask(d.expAsk.map(x => [x[0], x[1]]));

  G.push(seg('25–35 min', 'Mini-lesson (you teach, they join in)'));
  doo(['Show the mini-lesson slides. Think aloud as you work. Say what you notice, what you test and how you check. Children copy how you think.']);
  say(s.think);
  G.push(tbl([4600, 5300], [row([hd('Worked example on the slides', 4600), hd('Answer', 5300)]), row([c2(d.mini1.head + '. ' + (d.mini1.body || []).join(' '), 4600), c2(d.mini1.ans, 5300)]), row([c2(d.mini2.head + '. ' + (d.mini2.body || []).join(' '), 4600), c2(d.mini2.ans, 5300)])]));
  G.push(gap(40));
  say([d.keyHead.replace(/^Key idea: /, 'The key idea today is: ') + '. ' + d.keyBig + ' Say it with me.']);
  doo(['Show the key idea slide at minutes ' + PL.key[0] + ' to ' + PL.key[1] + '. The “common mistakes” on that slide are for you, not the children. Watch for them during the worksheet:']);
  l.mistakes.forEach(m => G.push(bu(m)));

  G.push(seg('35–40 min', 'Brain break'));
  doo([d.brk, 'Water. Toilet break for anyone who needs it. Keep it to five minutes.']);

  G.push(seg('40–70 min', 'Worksheet (Start here pages, then your choice)'));
  doo(['Minute 40: give out the workbook. Read the title of Lesson ' + l.n + ' aloud. Say “Pairs first. Talk before you write.”', 'Minutes 40 to 52: page 1 (Start here) in pairs; where the deck has a short teaching slide, it comes first. Minutes 52 to 54: check page 1 together. Minutes 54 to ' + PL.ws2[0] + ': short teaching before page 2. Minutes ' + PL.ws2[0] + ' to ' + PL.ws2[1] + ': each child works alone on page 2. Minutes ' + PL.ws2ans[0] + ' to ' + PL.ws2ans[1] + ': check page 2 together. Minutes ' + PL.stretch[0] + ' to 70: everyone chooses Think harder, Go further or the Investigation. A child who finishes early starts on one of them at once, and any child may choose them after question 3 of page 1.']);
  say(['Pairs first. Read each question aloud and talk about it before you write. I am not looking for speed. I am looking for good thinking.']);
  doo(['Circulate and ask:']);
  s.circulate.forEach(c => G.push(bu(c)));
  stuck(s.hints);
  doo(['Anyone who wants more may choose Think harder first, then Go further, or the Investigation (its easy first step is on page 2 of Start here). You may quietly invite a child by private chat message. Never announce who is on which page, and do not split a pair unless both children agree.']);
  G.push(h2('Think harder and Go further questions'));
  ask([...(q.stretch || []).slice(0, 4).map((x, i) => ['Workbook Think harder ' + (i + 1) + ': ' + x.q, x.a]), ...(q.challenge || []).slice(-3).map((x, i) => ['Workbook Go further ' + (i + 5) + ': ' + x.q, x.a])], 'Question', 'Answer');
  G.push(tx('These are the questions on the Think harder and Go further pages in the workbook. More are in the separate Question Bank.', { size: 19, color: '666666' }));

  G.push(seg('70–80 min', 'Talk time'));
  doo(['Bring the group back together (camera on). Ask for volunteers first. A pass is always fine, and so is sharing with a partner. Do not call a child by name cold, and keep no public tallies or rankings. If you want a particular child to share, invite them quietly beforehand by private chat message. Come back to sneak-peek puzzle 2: “Now we know the idea, how could it help?”']);
  say(s.talk);
  ask([[l.share, s.talkAns]], 'Discussion question', 'Listen for');

  G.push(seg('80–90 min', 'Exit ticket (80–86), look back (86–88) and closing (88–90)'));
  doo(['Minutes 80 to 86. Give each child a slip of paper (or ask them to write on their journal page). No talking, no helping. Show the exit ticket slide. Children show the answer to you only (paper held to the camera, or private chat); never mark or read answers out in front of the group.']);
  ask([[l.exit.q, l.exit.a]], 'Exit ticket', 'Answer');
  G.push(h2('Look back (minutes 86 to 88, two minutes)'));
  say(['Turn to the last page of today’s lesson and find Look back. Tick or write one thing for each line: something you did well, the hardest part, and what helped you. There are no right answers, and you may pass on any line.', 'Would anyone like to share something they did well, or what helped? Thank you. When you got stuck and tried something else, that is exactly what mathematicians do.']);
  doo(['Give a full 2 minutes. Never collect the page, mark it or read it out in front of the group: children keep it. You may read a page privately, and a child who ticked “I am still stuck (my tutor will check in privately)” may show it to you privately or send a private chat message; check in quietly after the lesson or at the start of the next one. Invite volunteers only. Praise the strategy (“you drew it and that got you unstuck”), not the speed or the answer.']);
  say(s.close);
  doo(['Minutes 88 to 90. Stamp the inquiry journal when a child has shown you their exit ticket. Mark S, D or H in the progress tracker at the back of this guide (it is for you only). If a child is marked D or H, plan two minutes of quiet catch-up at the start of the next lesson.']);
  G.push(h2('Extension for children who want more'));
  G.push(tx(l.extension));
  G.push(h2('Answer key (workbook)'));
  l.key.forEach(k => G.push(p([t(k[0] + '  ', { bold: true, size: 20 }), t(k[1], { size: 20 })], { after: 50, indent: { left: 240 }, line: 270 })));
  G.push(p([t('Sneak-peek puzzles  ', { bold: true, size: 20 }), t(GF[String(l.n)].check.map((c, i) => 'Puzzle ' + (i + 1) + ': ' + plain(c.a)).join('   '), { size: 20 })], { after: 50, indent: { left: 240 }, line: 270 }));
  G.push(p([t('Investigation (' + GF[String(l.n)].inv.title + ')  ', { bold: true, size: 20 }), t('Model answer and what to look for: ' + plain(GF[String(l.n)].inv.model), { size: 20 })], { after: 50, indent: { left: 240 }, line: 270 }));
  G.push(p([t('Go further (explore slide)  ', { bold: true, size: 20 }), t(plain(GF[String(l.n)].go) + ' Answer: ' + plain(GF[String(l.n)].goans), { size: 20 })], { after: 50, indent: { left: 240 }, line: 270 }));
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
['Circulate and ask questions rather than giving answers.', 'Use only the approved channels to contact parents. Never contact a child outside the lesson platform. The in-lesson private chat is only for lesson matters (a quiet invitation, a quiet check-in) and stays on the platform.', 'Do not take photos or recordings unless the Company has approved it and parents have consented.', 'If you have a concern about a child’s safety or welfare, tell the Company straight away.'].forEach(s => G.push(bu(s)));
G.push(h2('After the lesson'));
['Stamp inquiry journals and fill in the tracker.', 'Keep answer keys secure. Collect worksheets face to face only if a child offers them; the look-back page is never collected.', 'Note any child who needs help, and plan a short catch-up at the start of the next lesson.'].forEach(s => G.push(bu(s)));

/* ---------- Parent summary ---------- */
G.push(p(t(PROG, { bold: true, size: 44 }), { pb: true, after: 40 }));
G.push(p(t(SLOGAN, { italics: true, size: 28, color: '1F3864' }), { after: 100 }));
G.push(p(t('A 10-lesson holiday maths program for children finishing Primary 3', { bold: true, size: 26 }), { after: 100 }));
G.push(tx('Your child will spend the holidays as a young mathematician: noticing patterns, testing ideas with real objects and explaining their thinking. Lessons are live online in small groups, hands-on, and built around thinking, not speed.'));
G.push(h2('What your child will do'));
L.lessons.forEach(l => G.push(bu('Lesson ' + l.n + ', ' + l.title + ': ' + l.topic.toLowerCase())));
G.push(h2('How you can help'));
['Ask “How do you know?” when your child tells you an answer.', 'Let your child try first. Please sit nearby, but let them find the answer.', 'Print the workbook and cut-outs, and keep scissors, a ruler and a pencil ready.'].forEach(s => G.push(bu(s)));
G.push(h2('Practical details'));
G.push(tbl([2500, 7400], [['Dates', '[start date] to [end date], two lessons a week'], ['Time', '[day] and [day], [start time] to [end time]'], ['Where', 'Live online video class (link sent after registration)'], ['Group size', '[number] children'], ['Fee', 'S$500 introductory (regular S$650), workbook included, payable in 3 instalments'], ['Contact', '[name, phone or email]']].map(r => row([cell(r[0], 2500, { bold: true, fill: 'F2F2F2', size: 20, align: AlignmentType.LEFT, h: 80 }), c2(r[1], 7400, { h: 80 })]))));
G.push(p(t('Math Inquirers Holiday Program is an independent enrichment program. It is inspired by enrichment-style thinking skills but is not affiliated with, run by or endorsed by the Ministry of Education or any school.', { size: 18, italics: true, color: '666666' }), { before: 200, after: 0 }));

const doc = new D.Document({ styles: { default: { document: { run: { font: 'Arial', size: S } } } }, sections: [{ properties: { page }, footers: { default: footer(PROG + ' P3 • Program guide') }, children: G }] });
D.Packer.toBuffer(doc).then(b => { fs.writeFileSync('P3_Holiday_Program_Guide.docx', b); console.log('guide built'); });
