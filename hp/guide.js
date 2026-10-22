const C = require('./common.js');
const { fs, D, CW, t, p, cell, tbl, row, gap, footer, page, AlignmentType, BorderStyle, WidthType } = C;
const L = require('./lessons.js');
const GAPS = require('./gaps.json');
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
G.push(p(t('PRIMARY 1 HOLIDAY PROGRAM', { bold: true, size: 22, color: '666666' }), { after: 20 }));
G.push(p(t(PROG, { bold: true, size: 52 }), { after: 40 }));
G.push(p(t(SLOGAN, { italics: true, size: 30, color: '1F3864' }), { after: 120 }));
G.push(tx('Program guide for tutors: schedule, lesson routine, ten minute-by-minute lesson scripts with answer keys, a progress tracker and a parent summary. Math Inquirers is online first: every lesson runs live on video; the face-to-face notes are kept for partner centres.'));
G.push(h2('The program at a glance'));
G.push(tbl([2300, 7600], [
  ['Level', 'Primary 1 (ages 6 to 7), for children ready for more thinking than standard practice'],
  ['Length', '10 lessons of 90 minutes, two a week over the 5 weeks of the holidays'],
  ['Group size', 'Up to 8 children per tutor, live online. Pilot with 6. Add a second tutor or helper above 8.'],
  ['Focus', 'Thinking skills: spotting patterns, stating rules, working backwards, reasoning and explaining. Not speed drills.'],
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
  ['0–10', 'Warm-up', 'A quick game (0 to 5) and quick questions (5 to 7). The last 3 minutes (7 to 10) are the sneak-peek puzzles: two short puzzles on ideas we have not learnt yet. The first is one that any child can try with objects, a drawing or counting. The second makes you think. Answers are never put on boards in front of the group.', 'Sit in a circle or horseshoe.', 'Cameras on. Answers by thumbs, hands or whisper. Sneak-peek answers are shown to the tutor only, on camera.'],
  ['10–25', 'Explore', 'Hands-on in pairs. Objects first, no writing yet. Any pair may also choose the “Go further” what-if question on the slide from minute 15, so nobody waits.', 'Materials box on each table.', 'Each child has their own materials at home. Pairs go to breakout rooms.'],
  ['25–35', 'Mini-lesson', 'Tutor builds the table on the board, names the rule and asks what stays the same and what changes.', 'Whiteboard.', 'Shared slide and annotation tool.'],
  ['35–40', 'Brain break', 'Stand, stretch, drink water.', 'A short movement game.', 'Stand up on camera. Count the stretches together.'],
  ['40–72', 'Worksheet', 'Tutor reads questions 1 and 2 aloud, then pairs read the rest. Start in pairs, finish alone, then check together (the last 4 minutes, starting with a 1-minute stand-up stretch). Tutor asks “how do you know?” rather than giving answers. Every child’s workbook says: “After question 3 you may choose: carry on, or try Think harder.” Think harder (T), Go further (C) and the Investigation are printed for every child. The tutor never announces who is on which page.', 'Printed workbook, tutor circulates.', 'Printed workbook. Child holds the page up to the camera. Tutor checks one or two answers each.'],
  ['72–80', 'Talk time', 'Volunteers share one answer and explain it; passing is always fine. The tutor asks for volunteers first and never calls a child by name to answer. No tallies, no rankings.', 'Volunteers first. A child who prefers can show a drawing or pass.', 'Volunteers unmute. Others may pass or type in chat.'],
  ['80–90', 'Exit ticket, look-back and stamp', 'One question on a slip of paper (80 to 88). Stamp the inquiry journal. Then a two-minute look-back (88 to 90) in the workbook. A pass is always allowed.', 'Paper slip, tutor stamps.', 'Child writes the answer and shows the camera. Tutor stamps the next time or posts it.']
];
G.push(tbl([900, 1450, 2700, 2300, 2550], [row([hd('Minutes', 900), hd('Part', 1450), hd('What happens', 2700), hd('Face to face', 2300), hd('Online', 2550)]), ...R.map(r => row([c2(r[0], 900, { align: AlignmentType.CENTER, bold: true }), c2(r[1], 1450, { bold: true }), c2(r[2], 2700), c2(r[3], 2300), c2(r[4], 2550)]))]));
G.push(h2('Teaching habits that matter'));
['Ask “How do you know?” after every answer, right or wrong.', 'Wait 10 seconds before helping. Let children struggle a little.', 'Praise the thinking (“You checked it two ways”), not just the answer.', 'Let children disagree with each other and settle it with objects or a drawing.', 'If a child finishes early, use the Challenge or Extension question, not extra drill.'].forEach(s => G.push(bu(s)));

G.push(h2('Sneak-peek puzzles, choice time and look-back (every lesson)'));
['Sneak-peek puzzles (minutes 7 to 10). Two questions on the lesson’s key idea. The first is an access question: every child can try it with objects, drawing or counting, so everyone starts with a win. The second makes you think. Say: “These are ideas we have not learnt yet. A guess is a great start, and ‘I do not know’ is welcome. Nobody is marked.” Children write or draw on their own paper. Answers are not shown on boards in front of the group: face to face, each child holds their own paper low so that only the tutor sees it; online, each child writes on their own paper and shows it to the tutor on camera, or everyone holds their paper to the camera at the same moment. There are no private chat messages. Never use boards held up in front of the group. Never write scores down or announce them.', 'Choice time. Every workbook has the same neutral line on page 1: “After question 3 you may choose: carry on, or try Think harder.” Any child may choose. There is no list of who is ahead, and no criterion is printed. The tutor never announces who is on which page, and never names a child in front of the group. The tutor invites the WHOLE group at once, so nobody is singled out, for example: “When you have finished Start here, you can choose Think harder, Go further or the Investigation.” Say the same to any child who asks. Pairs are not split unless both children agree. A child who finds Think harder too hard goes back to Start here, with no fuss.', 'Online with a group of 8, the tutor can see each child’s page because each child already holds it up to the camera. Above 8 children, the helper keeps an eye on the children who have moved on while the tutor works with the others.', 'Talk time. Ask for volunteers first. Never call a child by name to answer. A child may pass, show a drawing or let a partner read for them. No public tallies and no rankings: do not say who is first or who got most right.', 'Look-back (minutes 88 to 90, two minutes). The box is on the Choose and look-back page of the workbook, which every child reaches: “Something I did well”, “The hardest part was ...”, “What helped me”, with tick options that include “I asked for help” and “I am still stuck (my tutor will come and help)”. Passing is always allowed. The box is never collected, shown or read out in front of the group. The tutor may look at it afterwards. If a child ticks “I am still stuck”, check in during the open session: a quick visit to the shared breakout room or a hand signal, with a parent nearby. Never send a direct message. Praise the strategy (“Drawing it got you unstuck”), not the speed.', 'The Investigation is printed on the Choose and look-back page for every child, with an easy first step, and is optional. It has several valid answers. The key gives a model answer and what to look for. Accept any correct noticing, and ask “How do you know?”.'].forEach(s => G.push(bu(s)));
G.push(h2('Setting up face to face'));
['Seat children in pairs. Keep a materials box per pair so no time is lost.', 'Print the workbook double-sided and staple it. Print the cut-out page on card for Lessons 6 and 9.', 'Keep the answer key with the tutor only. Collect worksheets at the end unless the group is told to keep them.', 'Use a whiteboard or large paper for the mini-lesson table.'].forEach(s => G.push(bu(s)));
G.push(h2('Setting up online'));
['Send parents the workbook and materials list one week before. Needed: counters or coins, two colours of paper pieces, a cup, straws or lolly sticks (never real matches or toothpicks), paper, a pencil and a cm ruler (Lesson 9).', 'Use one approved platform with breakout rooms and screen share. Admit only registered children and never share the link publicly.', 'Ask the parent to sit nearby but not give answers. The camera should show the child’s page and hands.', 'Hold up the answer page to the camera at the end of each lesson, or take a photo and send it through the approved channel.', 'Do not record lessons (this is in the tutor agreement). Add a second tutor or helper above 8 children.'].forEach(s => G.push(bu(s)));

G.push(h1('Materials master list', true));
G.push(tbl([900, 2600, 3200, 3200], [row([hd('Lesson', 900), hd('Title', 2600), hd('Face to face', 3200), hd('Online set-up', 3200)]), ...L.lessons.map(l => row([c2(String(l.n), 900, { align: AlignmentType.CENTER, bold: true }), c2(l.title, 2600), c2(l.materials, 3200), c2(l.online, 3200)]))]));

/* ---------- Lesson scripts ---------- */
const DD = require('../deck/data.js');
const WG = { 3: 'Quick vote. Each child chooses ONE fruit. Face to face: a sticky dot. Online: when the tutor points to a fruit, give a thumbs up (no typing needed).', 6: 'Coin shop. Three price tags in cents only: eraser 65¢, pencil 80¢, sticker 30¢. Pay exactly with play coins. Any way that pays exactly is a good way. Then look for a way with fewer coins.', 8: 'Guess my number. The tutor thinks of a number from 1 to 20. Ask yes or no questions. How few can we use together?', 10: 'Whiteboard round. The tutor asks a quick question from each lesson. Everybody writes the answer on a whiteboard or paper at the same time. No passing round and nobody on the spot.' };
const SC = require('./scripts.js');
const QB = require('./qbank.json');
const tag = (s, fill) => cell(s, 1000, { bold: true, fill, size: 18, h: 50, align: AlignmentType.CENTER });
const seg = (time, title) => p([t(time + '   ', { bold: true, size: 22, color: 'FFFFFF' }), t(title, { bold: true, size: 22, color: 'FFFFFF' })], { before: 160, after: 60, keepNext: true, shading: { type: 'clear', fill: '1F3864', color: 'auto' } });
const say = (lines) => lines.forEach((s, i) => G.push(p([t(i === 0 ? 'SAY   ' : '          ', { bold: true, size: 19, color: '1F6F5C' }), t('“' + s.replace(/^[“"]|[”"]$/g, '') + '”', { size: S, italics: true })], { after: 50, indent: { left: 900, hanging: 900 }, line: 280 })));
const doo = (lines) => lines.forEach((s, i) => G.push(p([t(i === 0 ? 'DO     ' : '          ', { bold: true, size: 19, color: '7F6000' }), t(s, { size: S })], { after: 40, indent: { left: 900, hanging: 900 }, line: 280 })));
const ask = (rows, h1c, h2c) => { G.push(tbl([4600, 5300], [row([hd(h1c || 'Ask', 4600), hd(h2c || 'Expect', 5300)]), ...rows.map(r => row([c2(r[0], 4600), c2(r[1], 5300)]))])); G.push(gap(40)); };
const stuck = (lines) => lines.forEach((s, i) => G.push(p([t(i === 0 ? 'IF STUCK   ' : '                ', { bold: true, size: 19, color: 'A61C00' }), t(s, { size: S })], { after: 40, indent: { left: 1300, hanging: 1300 }, line: 280 })));

G.push(h1('How to use the scripts', true));
G.push(tx('Every lesson below is a minute-by-minute script. The slides match it: one slide or two for each part. You do not have to say the words exactly, but keep the questions, because the questions are what makes children think.'));
G.push(tbl([1500, 8400], [
  ['SAY', 'Words to say aloud, in plain language for 6- and 7-year-olds. Said in your own voice, not read from the page.'],
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

  G.push(seg('2–7 min', 'Warm-up game and quick questions'));
  doo([WG[l.n] || d.warmGame]);
  say(s.warmIntro);
  doo(['After the game, ask the quick questions on the warm-up slides (minutes 5 to 7; if time is short, take questions 1 to 3). Use thumbs or a whisper to partners before taking answers.']);
  ask(d.warmQs.map(x => [x[0], x[1]]));
  G.push(seg('7–10 min', 'Sneak-peek puzzles (3 minutes)'));
  say(['These two are sneak-peek puzzles. They are ideas we have not learnt yet, so a guess is a great start. “I do not know” is welcome too. Nobody is marked.', 'The first one you can try with counters or a drawing. Write or draw on your own paper. When I say, show it to me only (online: hold your paper up to the camera for me).']);
  doo(['Show the sneak-peek slide. Give about a minute for each question, then see the answers without a public board: face to face, walk round and look at papers held low; online, ask children to hold their papers to the camera at the same moment. Do not show or read out anyone’s answer. Click to show each answer to the whole group only after all children have had a try, and say “Lots of us had a different idea, and that is fine.”', 'Quietly note who found the second question easy. Do not write scores on the board or say who is “ahead”. At minute 40 invite the whole group: “When you have finished Start here, you can choose Think harder, Go further or the Investigation.” Do not name a child in front of the group. Everyone joins Explore and the Mini-lesson.', 'At minute 40: read questions 1 and 2 aloud, then pairs read the rest. Say: “After question 3 you may choose: carry on, or try Think harder.” Do not split a pair unless both children agree.']);
  ask(GAPS[String(l.n)].check.map((c, i) => [(i === 0 ? 'Sneak-peek 1 (any child can try): ' : 'Sneak-peek 2 (thinking): ') + c.q, c.a]), 'Question', 'Answer and why');

  G.push(seg('10–25 min', 'Explore (in pairs, with objects)'));
  say(s.predict);
  doo(d.expSetup.map((x, i) => (i + 1) + '. ' + x));
  say(['Talk to your partner while you work. I will come round and ask you questions.']);
  stuck(s.exploreHints);
  if (l.cards) { doo(['Print the Puzzle cards page from the back of the workbook (or show the Lesson 10 cards slide). Pairs get ONE card for 10 minutes, then swap with another pair for 4 minutes. Answers:']); ask(l.cards.map(c => [c.title + ': ' + c.text, c.answer]), 'Puzzle card', 'Answer'); }
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

  G.push(seg('40–72 min', 'Worksheet (pairs, then alone, then check together)'));
  doo(['Minute 40: give out the workbook. Read the title of Lesson ' + l.n + ' aloud and read questions 1 and 2 aloud. Say “Pairs first. Talk before you write. After question 3 you may choose: carry on, or try Think harder.”', 'About minutes 40 to 54: pairs work together on the first page, with a short teaching slide before it and a check-together slide after it. After that, a short teaching slide, then about 10 minutes (58 to 68) when each child works alone on the second page; the exact times are on each slide. Minutes 68 to 72: everyone stands up and stretches for a minute, then check the second page together. Think harder (T), Go further (C) and the Investigation are not a timed part of the lesson: every child has them in the workbook and may choose them at any time, or at home.']);
  say(['Pairs first. Read each question aloud and talk about it before you write. I am not looking for speed. I am looking for good thinking.']);
  doo(['Circulate and ask:']);
  s.circulate.forEach(c => G.push(bu(c)));
  stuck(s.hints);
  doo(['Children who choose more: Think harder T1 first (it is in the workbook), then the Think harder slide, then Go further, then the Investigation on the Choose and look-back page. Never announce who is on which page, and do not split a pair unless both children agree.']);
  G.push(h2('Think harder, Go further and Investigation'));
  ask([...(q.stretch || []).slice(0, 4).map((x, i) => ['Workbook Think harder T' + (i + 1) + ': ' + x.q, x.a]), ...(GAPS[String(l.n)].tx || []).map(x => ['Workbook Think harder ' + x.label + ': ' + x.q + ' ' + (x.subs || []).map(z => '(' + z[0] + ') ' + z[1]).join(' '), x.a]), ...(q.challenge || []).slice(-3).map((x, i) => ['Workbook Go further C' + (i + 1) + ': ' + x.q, x.a])], 'Question', 'Answer');
  G.push(tx('These are the questions on the Think harder and Go further pages in the workbook. The Think harder slide has three more questions; their answers are in the answer key below. More are in the separate Question Bank.', { size: 19, color: '666666' }));

  G.push(seg('72–80 min', 'Talk time'));
  doo(['Bring the group back to a circle (or camera on, mics on). Ask for volunteers first: “Who would like to share?” Never call a child by name to answer. Say that passing is always fine. A child may show a drawing or let a partner speak. No tallies, no rankings.']);
  say(s.talk);
  ask([[l.share, s.talkAns]], 'Discussion question', 'Listen for');

  G.push(seg('80–88 min', 'Exit ticket and closing'));
  doo(['Give each child a slip of paper (or ask them to write on their journal page). No talking, no helping. Show the exit ticket slide.']);
  ask([[l.exit.q, l.exit.a]], 'Exit ticket', 'Answer');
  say(s.close);
  G.push(seg('88–90 min', 'Look-back (2 minutes)'));
  say(['Turn to the Choose and look-back page and look at the box called “Look-back”. Tick what was hard for you and what helped you. Write or draw one thing you did well. You can pass. If you are still stuck, tick the box and I will come and help you. I will not say your name to the group. This is not shown to the group.', 'Thank you. Drawing it, using counters, asking a friend or asking for help: those are all good ways to get unstuck.']);
  doo(['Show the look-back slide. Keep it to two minutes. Do not ask children to read out their boxes. Never mark or grade the box, and never collect it in front of the group. You may look at it later. Praise the strategy a child used, not how quickly they finished.']);
  doo(['Stamp the inquiry journal when a child hands in their ticket. Mark S, D or H in the progress tracker at the back of this guide (it is for you only). If a child marked D or H, plan two minutes of catch-up at the start of the next lesson in the open session (a shared breakout room or a hand signal, with a parent nearby), never by direct message.']);
  G.push(h2('Extension for children who want more'));
  G.push(tx(l.extension));
  G.push(h2('Answer key (workbook)'));
  l.key.filter(k => !/^Think harder slide/.test(k[0])).forEach(k => G.push(p([t(k[0] + '  ', { bold: true, size: 20 }), t(k[1], { size: 20 })], { after: 50, indent: { left: 240 }, line: 270 })));
  G.push(p([t('Think harder slide  ', { bold: true, size: 20 }), t(q.stretch.slice(4, 7).map((x, i) => (i + 1) + ') ' + x.a).join('  '), { size: 20 })], { after: 50, indent: { left: 240 }, line: 270 }));
  GAPS[String(l.n)].check.forEach((c, i) => G.push(p([t('Sneak-peek ' + (i + 1) + '  ', { bold: true, size: 20 }), t(c.a, { size: 20 })], { after: 50, indent: { left: 240 }, line: 270 })));
  G.push(p([t('Investigation (' + GAPS[String(l.n)].invest.title + ')  ', { bold: true, size: 20 }), t(GAPS[String(l.n)].invest.model, { size: 20 })], { after: 50, indent: { left: 240 }, line: 270 }));
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
G.push(p(t('A 10-lesson holiday maths program for Primary 1', { bold: true, size: 26 }), { after: 100 }));
G.push(tx('Your child will spend the holidays as a young mathematician: noticing patterns, testing ideas with real objects and explaining their thinking. Lessons are in small groups, hands-on, and built around thinking, not speed.'));
G.push(h2('What your child will do'));
L.lessons.forEach(l => G.push(bu('Lesson ' + l.n + ', ' + l.title + ': ' + l.topic.toLowerCase())));
G.push(h2('How you can help'));
['Ask “How do you know?” when your child tells you an answer.', 'Let your child try first. Please sit nearby, but let them find the answer.', 'Help gather simple materials: counters or coins, paper and a pencil (online groups).'].forEach(s => G.push(bu(s)));
G.push(h2('Practical details'));
G.push(tbl([2500, 7400], [['Dates', '[start date] to [end date], two lessons a week'], ['Time', '[day] and [day], [start time] to [end time]'], ['Where', '[venue address] or [online link sent after registration]'], ['Group size', '[number] children'], ['Fee', '[amount]'], ['Contact', '[name, phone or email]']].map(r => row([cell(r[0], 2500, { bold: true, fill: 'F2F2F2', size: 20, align: AlignmentType.LEFT, h: 80 }), c2(r[1], 7400, { h: 80 })]))));
G.push(p(t('Math Inquirers Holiday Program is an independent enrichment program. It is inspired by enrichment-style thinking skills but is not affiliated with, run by or endorsed by the Ministry of Education or any school.', { size: 18, italics: true, color: '666666' }), { before: 200, after: 0 }));

const doc = new D.Document({ styles: { default: { document: { run: { font: 'Arial', size: S } } } }, sections: [{ properties: { page }, footers: { default: footer(PROG + ' • Program guide') }, children: G }] });
D.Packer.toBuffer(doc).then(b => { fs.writeFileSync('P1_Holiday_Program_Guide.docx', b); console.log('guide built'); });
