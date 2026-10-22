const C = require('../hp/common.js');
const { fs, D, CW, t, p, cell, tbl, row, gap, footer, page, AlignmentType, BorderStyle, WidthType } = C;
const L = require('./data.js');
const bx = t => String(t).replace(/\{box\}/g, '[ ]');
/* Minutes come from p2/budget.json (written by rebuild/p2budget.py, the single source for slide pills, notes and this guide). */
const BUD = require('./budget.json').lessons;
const num = x => String(+(+x).toFixed(2));
const pt = (n, title) => { const x = BUD[n].parts.find(y => y.title === title); if (!x) throw new Error('no part ' + title + ' in lesson ' + n); return x; };
const has = (n, title) => BUD[n].parts.some(y => y.title === title);
const rng = (a, b) => num(a) + '–' + num(b);
// time = 'a–b min' shown in the guide; rec = whole-minute range for the REC cue (levels/reccues.js reads only whole numbers)
const part = (n, ...titles) => { const a = pt(n, titles[0]).start, b = pt(n, titles[titles.length - 1]).end; return { a, b, d: b - a, time: rng(a, b) + ' min', rec: '0–' + Math.max(1, Math.round(b - a)) + ' min' }; };
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
G.push(p(t('PRIMARY 2 HOLIDAY PROGRAM', { bold: true, size: 22, color: '666666' }), { after: 20 }));
G.push(p(t(PROG, { bold: true, size: 52 }), { after: 40 }));
G.push(p(t(SLOGAN, { italics: true, size: 30, color: '1F3864' }), { after: 120 }));
G.push(tx('Program guide for tutors: schedule, lesson routine, ten minute-by-minute lesson scripts with answer keys, a progress tracker and a parent summary. Math Inquirers is online first: every lesson runs live on video; the face-to-face notes are kept for partner centres.'));
G.push(h2('The program at a glance'));
G.push(tbl([2300, 7600], [
  ['Level', 'Children finishing Primary 2 (ages 8 to 9), going into P3, who are ready for more thinking than standard practice'],
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
G.push(tx('Every lesson uses the same routine so children know what to expect and tutors can prepare quickly. The times below are the standard timeline; the lesson scripts give the exact minutes for each lesson. Every lesson adds up to exactly 90 minutes, including the named Flex block.'));
const R = [
  ['0–10.5', 'Opening, sneak-peek and warm-up', 'Welcome (0–1.5): kit is on the desk from minute 0. Sneak-peek puzzles (1.5–6): two puzzles on ideas not learnt yet, answers shown only to the tutor, nobody marked. A short game (6–8.5). Two quick questions (8.5–10.5). Everyone joins in.', 'Sit in a circle or horseshoe.', 'Cameras on. Answers on own paper held to the camera at the same moment, or shown to the tutor only; or thumbs. Never by private chat or message. No whiteboards raised together.'],
  ['10.5–23.5', 'Explore', 'Hands-on in pairs. Objects first, no writing yet. One round of breakout rooms (60 seconds each way, about 5.5 minutes of pair work), then the group talks it through (about 4 minutes).', 'Materials box on each table.', 'Each child has their own materials at home, out on the desk from minute 0. Pairs go to breakout rooms once, with an auto-timer.'],
  ['23.5–35.5', 'Mini-lesson', 'Tutor builds the table on the board, names the rule and asks what stays the same and what changes. Lessons 9 and 10 are shorter (10.5 and 10 minutes).', 'Whiteboard.', 'Shared slide and annotation tool.'],
  ['35.5–38.5', 'Brain break', 'Stand, stretch, drink water: two minutes of movement, one for water.', 'A short movement game.', 'Stand up on camera. Count the stretches together.'],
  ['38.5–73.5', 'Worksheet', 'Page 1 in pairs (38.5–52.5), check together (52.5–55), short teaching (55–59.5), page 2 alone (59.5–71), check together (71–73.5). Tutor asks “how do you know?” rather than giving answers. Questions marked ★ take-home are done at home. Lessons 5, 6 and 10 open with a short teach slide, and Lessons 4, 9 and 10 have slightly different times: each lesson script gives its own.', 'Printed workbook, tutor circulates.', 'Printed workbook. Child holds the page up to the camera. Tutor checks one or two answers each. Pairs stay in the main room.'],
  ['73.5–76.5', 'Flex (spare time)', 'Three spare minutes kept on purpose (4.5 in Lesson 9, 4 in Lesson 10 and 5 in Lesson 4). Absorb a late start or a slow page 2 here. If you are on time, use it for the Investigation share or a second volunteer. Never add new content.', 'Same room.', 'Stay on camera. Keep the break short.'],
  ['76.5–81.5', 'Talk time', 'Pairs talk for 90 seconds, then two volunteers share one answer and explain it. One question. Any child may pass. No cold-calling by name, no public tallies or rankings.', 'The tutor invites volunteers first.', 'The tutor invites volunteers; a child unmutes when invited. Quiet children can be invited, with a parent nearby, by a quick word in the open session; never by private chat or message.'],
  ['81.5–90', 'Exit ticket, Looking back and stamp', 'Exit ticket (81.5–86.5, one question on a slip of paper, held up one child at a time). Looking back (86.5–88.5, in the box on the “Before you go” page after page 2, a pass is always allowed). Closing and stamps (88.5–90; Lesson 10: certificates and closing 87–90).', 'Paper slip, tutor stamps.', 'Child writes the answer and shows the tutor only. Tutor stamps the next time or posts it.']
];
G.push(tbl([900, 1450, 2700, 2300, 2550], [row([hd('Minutes', 900), hd('Part', 1450), hd('What happens', 2700), hd('Face to face', 2300), hd('Online', 2550)]), ...R.map(r => row([c2(r[0], 900, { align: AlignmentType.CENTER, bold: true }), c2(r[1], 1450, { bold: true }), c2(r[2], 2700), c2(r[3], 2300), c2(r[4], 2550)]))]));
G.push(h2('Teaching habits that matter'));
['Ask “How do you know?” after answers, right or wrong, but invite rather than single out: “Would anyone like to say how they started?” “I am not sure yet” is always a fine answer.', 'Wait 10 seconds before helping. Let children struggle a little.', 'Praise the thinking (“You checked it two ways”), not just the answer.', 'Let children disagree with each other and settle it with objects or a drawing.', 'If a child would like more, offer Think harder, Go further or the Investigation as a choice. Never name who is on which page, and never use extra drill.'].forEach(s => G.push(bu(s)));

G.push(h2('Preparing the materials'));
['Send the workbook PDF to parents one week before. Ask them to print it single-sided and the cut-out pages on card if they can.', 'Cut-outs used: place-value cards (Lessons 1, 2, 10), digit cards (Lessons 1 and 10), number chart 1 to 100, missing numbers chart and My own chart (Lesson 1: patterns on a chart), play coins and notes (Lesson 6), fraction strips (Lesson 7), cube nets and paper cube strips (Lesson 8), paper clock (Lesson 9).', 'Keep the answer key with the tutor only. Check answers together on screen.', 'Use the shared screen or a digital whiteboard for the mini-lesson table.'].forEach(s => G.push(bu(s)));
G.push(h2('Setting up online'));
['Send parents the workbook and materials list one week before. Needed: the printed workbook and cut-outs, 20 counters or small objects, scissors, a split pin or short pencil for the clock, paper and a pencil.', 'Use one approved platform with breakout rooms and screen share. Admit only registered children and never share the link publicly.', 'Ask the parent to sit nearby but not give answers. The camera should show the child’s page and hands.', 'Hold up the answer page to the camera at the end of each lesson, or take a photo and send it through the approved channel.', 'Lessons are recorded on the approved platform so that children who miss one can catch up; follow “Recording the lesson” in this guide. Do not make your own recordings or photos. Add a second tutor or helper above 8 children.'].forEach(s => G.push(bu(s)));

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
const pushSeg = (time, title, recTime) => { G.push(seg(time, title)); const c = REC.cue(title, recTime || time, CURL); SEGS.push({ time, title, action: c.action }); rec(c.say); };
const ask = (rows, h1c, h2c) => { G.push(tbl([4600, 5300], [row([hd(h1c || 'Ask', 4600), hd(h2c || 'Expect', 5300)]), ...rows.map(r => row([c2(r[0], 4600), c2(r[1], 5300)]))])); G.push(gap(40)); };
const stuck = (lines) => lines.forEach((s, i) => G.push(p([t(i === 0 ? 'IF STUCK   ' : '                ', { bold: true, size: 19, color: 'A61C00' }), t(s, { size: S })], { after: 40, indent: { left: 1300, hanging: 1300 }, line: 280 })));

G.push(h1('How to use the scripts', true));
G.push(tx('Every lesson below is a minute-by-minute script. The slides match it: each part has its own few slides, and each slide shows the same minutes as the script. You do not have to say the words exactly, but keep the questions, because the questions are what makes children think.'));
G.push(tbl([1500, 8400], [
  ['SAY', 'Words to say aloud, in plain language for 8- and 9-year-olds. Said in your own voice, not read from the page.'],
  ['DO', 'What you do: set up, hand out, show a slide, or move around the room.'],
  ['ASK / EXPECT', 'Questions to put to the group, with the answer you are listening for. Let children answer before you explain.'],
  ['IF STUCK', 'A ladder of help. Give hint 1, wait ten seconds, then give hint 2. Do not give the answer.']
].map(r => row([cell(r[0], 1500, { bold: true, fill: 'F2F2F2', size: 20, align: AlignmentType.LEFT, h: 70 }), c2(r[1], 8400)]))));
G.push(h2('Five habits that run through every script'));
['Predict first. Before children test anything, ask for a guess and write it down. A wrong guess is useful because we can test it.', 'Wait ten seconds after every question. Count silently. Most children answer in the last four.', 'Ask “How do you know?” after right answers too (to volunteers), so that children do not read your face for the answer.', 'Praise the thinking, not the answer: “You checked it two ways” beats “Well done”.', 'When an answer is wrong, say “Let us test that,” and use objects, not “No”.'].forEach(s => G.push(bu(s)));
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
  G.push(h1('Lesson ' + l.n + ': ' + l.title, true));
  G.push(p(t('Week ' + l.week + (l.session === 'A' ? ' (first lesson)' : ' (second lesson)') + '   •   ' + l.topic + '   •   Workbook: Lesson ' + l.n, { size: 20, color: '666666' }), { after: 80 }));
  G.push(tbl([1900, 8000], [
    ['Objective', l.objective], ['Thinking skills', l.skills], ['Materials', l.materials], ['Online set-up', l.online],
    ['Prepare', 'Solve the worksheet yourself first. Set out one materials box per pair. Open the slides for this lesson and check the answers in the speaker notes.'],
    ['Watching the recording', 'A child who missed the live lesson watches the recording. They need: ' + l.materials + ' The REC lines tell them when to pause; the chapter list at the end of this lesson shows each part.']
  ].map(r => row([cell(r[0], 1900, { bold: true, fill: 'F2F2F2', size: 20, align: AlignmentType.LEFT, h: 60 }), c2(r[1], 8000, { h: 60 })]))));
  G.push(gap(40));

  const X = l.n === 10, n = l.n;
  const sOp = part(n, 'Opening'), sSn = part(n, 'Sneak-peek puzzles'), sWu = part(n, 'Warm-up'), sEx = part(n, 'Explore'), sMi = part(n, 'Mini-lesson'), sBr = part(n, 'Brain break');
  const wsFirst = has(n, 'Worksheet teach slide') ? 'Worksheet teach slide' : 'Worksheet page 1 (pairs)';
  const sWs = part(n, wsFirst, 'Check together, page 2'), sFl = part(n, 'Flex (spare time)'), sTa = part(n, 'Talk time'), sEt = part(n, 'Exit ticket'), sLb = part(n, 'Looking back'), sCl = part(n, X ? 'Certificates and closing' : 'Closing and stamps');
  const p1 = pt(n, 'Worksheet page 1 (pairs)'), ck1 = pt(n, 'Check together, page 1'), tch = pt(n, 'Short teaching'), p2 = pt(n, 'Worksheet page 2 (alone)'), ck2 = pt(n, 'Check together, page 2');
  const lat = (x, y) => num(x) + ' to ' + num(y);
  pushSeg(sOp.time, 'Opening', sOp.rec);
  say(s.hook);
  doo(['Greet each child by name. Show the lesson title slide. Read “Today we will…” aloud. The kit is on the desk from minute 0: ask everyone to show you the materials for today (a 30-second check; the materials list is above and on the title slide).']);

  const gp = L.gaps[String(l.n)], GC = L.gaps.common;
  pushSeg(sSn.time, 'Sneak-peek puzzles (' + num(sSn.d) + ' minutes)', sSn.rec);
  say([GC.preSay]);
  doo(GC.preDo);
  ask(gp.pre.map((x, i) => [(i === 0 ? 'Question 1 (access: objects, drawing or counting): ' : 'Question 2 (thinking): ') + bx(x.q), bx(x.a) + '  Listen for: ' + x.w]), 'Sneak-peek puzzle', 'Answer and what to listen for');
  doo(['The neutral line “' + GC.neutral + '” is printed on page 1 of the workbook, next to the lesson title. Nobody is labelled and nothing is announced.']);

  pushSeg(sWu.time, 'Warm-up', sWu.rec);
  doo([d.warmGame]);
  say(s.warmIntro);
  doo(['Keep the game to about two and a half minutes (' + lat(sWu.a, sWu.a + 2.5) + '): stop it on the clock. Then the quick questions (' + lat(sWu.a + 2.5, sWu.b) + '): ask questions 1 and 3 only (these are the two on the slide); questions 2, 4 and 5 are spare. Children answer by thumbs, a whisper to a partner. Do not name a child.']);
  ask(d.warmQs.map(x => [x[0], x[1]]));

  const pairs = X ? 4.5 : 5.5, tDown = sEx.a + 2.5 + pairs;
  pushSeg(sEx.time, 'Explore (in pairs, with objects)', sEx.rec);
  doo(['Timing (' + num(sEx.d) + ' minutes): set up and predict, ' + lat(sEx.a, sEx.a + 1.5) + '. One round of breakout rooms with an auto-timer: 60 seconds to get in, ' + num(pairs) + ' minutes of pair work (' + lat(sEx.a + 2.5, tDown) + '), 60 seconds to come back. Then the group debrief, ' + lat(tDown + 1, sEx.b) + '.']);
  say(s.predict);
  doo(d.expSetup.map((x, i) => (i + 1) + '. ' + x));
  say(['Talk to your partner while you work. I will come round and ask you questions.']);
  stuck(s.exploreHints);
  if (d.stationCards) { doo(['Station cards (all four are on ONE slide in the deck). Each pair takes two cards, about 2 minutes each (' + num(pairs) + ' minutes of pair work in all):']); ask(d.stationCards.map(x => [x[0] + '. ' + x[1], x[2]]), 'Station card', 'Answer'); }
  doo(['Go further (a second what-if, so nobody waits): it is the box at the foot of the Explore slide; post it in the chat as well when pairs go to their rooms. Any child may try it any time, as a choice. Never name who does. Question: ' + L.gaps[String(l.n)].whatif.q.replace(/^Go further: /, '') + '  Answer: ' + L.gaps[String(l.n)].whatif.a]);
  doo(['At about minute ' + num(tDown) + ', say “Pencils down” and bring the group back together (60 seconds). Take the three questions below, one at a time (about ' + num(sEx.b - tDown - 1) + ' minutes in all). Ask “How do you know?” on question 2 only; take about 15 seconds of talk on the others.']);
  ask(d.expAsk.map(x => [x[0], x[1]]));

  pushSeg(sMi.time, 'Mini-lesson (you teach, they join in)', sMi.rec);
  doo(['Show the mini-lesson slides. Think aloud as you work. Say what you notice, what you test and how you check. Children copy how you think.']);
  say(s.think);
  G.push(tbl([4600, 5300], [row([hd('Worked example on the slides', 4600), hd('Answer', 5300)]), row([c2(d.mini1.head + '. ' + (d.mini1.body || []).join(' '), 4600), c2(d.mini1.ans, 5300)]), row([c2(d.mini2.head + '. ' + (d.mini2.body || []).join(' '), 4600), c2(d.mini2.ans, 5300)])]));
  G.push(gap(40));
  say([d.keyHead.replace(/^Key idea: /, 'The key idea today is: ') + '. ' + d.keyBig + ' Say it with me.']);
  doo(['Show the key idea slide at about minutes ' + lat(sMi.b - 1, sMi.b) + '. The “common mistakes” on that slide are for you, not the children. Watch for them during the worksheet:']);
  l.mistakes.forEach(m => G.push(bu(m)));

  pushSeg(sBr.time, 'Brain break', sBr.rec);
  doo([d.brk, 'Water. Toilet break for anyone who needs it. Keep it to three minutes: two of movement, one for water.']);

  pushSeg(sWs.time, 'Worksheet (pairs, then alone, then stretch)', sWs.rec);
  const wsT = has(n, 'Worksheet teach slide') ? pt(n, 'Worksheet teach slide') : null;
  doo(['Minute ' + num(sWs.a) + ': give out the workbook. Read the title of Lesson ' + l.n + ' aloud. Say “Pairs first. Talk before you write.”', (wsT ? 'Minutes ' + lat(wsT.start, wsT.end) + ': a short teach slide first (this lesson). ' : '') + 'Minutes ' + lat(p1.start, p1.end) + ': pairs work together on the first page (the 2 minutes at the start are for finding the page and setting up; pairs stay in the main room). Minutes ' + lat(ck1.start, ck1.end) + ': check page 1 together (read only the answer line, children mark their own, one “How do you know?” for the page). Minutes ' + lat(tch.start, tch.end) + ': short teaching for page 2. Minutes ' + lat(p2.start, p2.end) + ': each child works alone on the second page. Minutes ' + lat(ck2.start, ck2.end) + ': check page 2 together (answer lines only, children mark their own). Think harder, Go further and the Investigation are open to any child at any time after question 3.']);
  doo(['Take-home stars: ' + l.takehome + ' Each is marked on the page with a ★ and the words take-home, stays Core (not Think harder), and keeps its answer on the check-together slide so a child can mark it at home. Do not spend class time on them. Late rule, printed here on purpose: at minute ' + num(p2.start) + ' (the start of page 2), if the clock is more than 2 minutes late, drop the last Core question of page 2 to take-home (children put a ★ beside it). Never shorten talk time, the exit ticket, looking back or the closing.']);
  say(['Pairs first. Read each question aloud and talk about it before you write. I am not looking for speed. I am looking for good thinking.']);
  doo(['Circulate and ask:']);
  s.circulate.forEach(c => G.push(bu(c)));
  stuck(s.hints);
  doo(['A choice, not a track: after question 3 any child may carry on or try Think harder (the neutral line is printed on page 1). Invite the WHOLE group at once, never one child: "When you have finished Start here, you can choose Think harder, Go further or the Investigation." Never announce who is on which page, never name a child in front of the group, and do not split a pair unless both children agree. Children may move either way at any time. The Investigation is printed on the last core page, so every child sees it.']);
  G.push(h2('Think harder and Go further questions'));
  ask([...(q.stretch || []).slice(0, 4).map((x, i) => ['Workbook Think harder ' + (i + 1) + ': ' + x.q, x.a]), ...(q.challenge || []).slice(-3).map((x, i) => ['Workbook Go further ' + (i + 5) + ': ' + x.q, x.a])], 'Question', 'Answer');
  G.push(tx('These are the questions on the two Think harder pages in the workbook (Think harder, then Go further). More are in the separate Question Bank.', { size: 19, color: '666666' }));
  ask([['Workbook Investigation (on the “Before you go” page): ' + gp.invest.title + '. ' + gp.invest.text + ' ' + gp.invest.first + (gp.invest.need ? ' ' + gp.invest.need : ''), gp.invest.model]], 'Investigation (several answers are right)', 'Model answer and what to look for');

  pushSeg(sFl.time, 'Flex (spare time)', sFl.rec);
  doo(['Spare time, kept on purpose (' + num(sFl.d) + ' minutes). Use it to absorb a late start, a camera problem or a slow page 2. If you are on time, spend it on the Investigation share or a second talk-time volunteer, or an early start on talk time. Do not add new content. Never take time from the exit ticket, looking back or the stamp.']);

  pushSeg(sTa.time, 'Talk time', sTa.rec);
  doo(['Bring the group back to a circle (or camera on, mics on). Pairs talk for 90 seconds, then two volunteers share (about ' + num(sTa.d) + ' minutes in all). One question only. ' + GC.talkDo]);
  say(s.talk);
  ask([[l.share, s.talkAns]], 'Discussion question', 'Listen for');

  pushSeg(sEt.time, 'Exit ticket', sEt.rec);
  doo(['Give each child a slip of paper (or ask them to write on their journal page). No talking, no helping. Show the exit ticket slide. About 2 minutes of child work; then children hold their slips up one at a time (never all together) and the answer is on the next click.']);
  ask([[bx(l.exit.q), bx(l.exit.a)]], 'Exit ticket', 'Answer');
  pushSeg(sLb.time, 'Looking back (2 minutes)', sLb.rec);
  say([GC.refSay]);
  doo([GC.refDo]);
  pushSeg(sCl.time, X ? 'Certificates and closing' : 'Closing and stamps (' + num(sCl.d) + ' minutes)', sCl.rec);
  say(s.close);
  doo(['Stamp the inquiry journal when a child hands in their ticket. Mark S, D or H in the progress tracker at the back of this guide (this is for you only, never shared with the children). If a child marked D or H, plan two minutes of catch-up at the start of the next lesson.']);
  G.push(h2('Think harder and Go further'));
  G.push(tx(l.extension));
  G.push(h2('Answer key (workbook)'));
  l.key.forEach(k => G.push(p([t(k[0] + '  ', { bold: true, size: 20 }), t(k[1], { size: 20 })], { after: 50, indent: { left: 240 }, line: 270 })));
  G.push(p([t('Investigation  ', { bold: true, size: 20 }), t('(' + gp.invest.title + '). ' + gp.invest.model, { size: 20 })], { after: 50, indent: { left: 240 }, line: 270 }));
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
['Circulate and ask questions rather than giving answers.', 'Use only the approved channels to contact parents. No private messages to children. Invite the whole group, never one child. If a child ticks “I am still stuck”, check in during the open session (a quick visit to the shared breakout room or a hand signal, with a parent nearby). Never use personal accounts.', 'Do not take your own photos or recordings. The only recording is the lesson recording made on the approved platform under “Recording the lesson”.', 'If you have a concern about a child’s safety or welfare, tell the Company straight away.'].forEach(s => G.push(bu(s)));
G.push(h2('After the lesson'));
['Stamp inquiry journals and fill in the tracker.', 'Collect worksheets and answer keys (face to face) and keep them secure.', 'Note any child who needs help, and plan a short catch-up at the start of the next lesson.'].forEach(s => G.push(bu(s)));

/* ---------- Parent summary ---------- */
G.push(p(t(PROG, { bold: true, size: 44 }), { pb: true, after: 40 }));
G.push(p(t(SLOGAN, { italics: true, size: 28, color: '1F3864' }), { after: 100 }));
G.push(p(t('A 10-lesson holiday maths program for children finishing Primary 2', { bold: true, size: 26 }), { after: 100 }));
G.push(tx('Your child will spend the holidays as a young mathematician: noticing patterns, testing ideas with real objects and explaining their thinking. Lessons are live online in small groups, hands-on, and built around thinking, not speed.'));
G.push(h2('What your child will do'));
L.lessons.forEach(l => G.push(bu('Lesson ' + l.n + ', ' + l.title + ': ' + l.topic.toLowerCase())));
G.push(h2('How you can help'));
['Ask “How do you know?” when your child tells you an answer.', 'Let your child try first. Please sit nearby, but let them find the answer.', 'Print the workbook and cut-outs, and keep counters, scissors and a pencil ready.'].forEach(s => G.push(bu(s)));
G.push(h2('Practical details'));
G.push(tbl([2500, 7400], [['Dates', '[start date] to [end date], two lessons a week'], ['Time', '[day] and [day], [start time] to [end time]'], ['Where', 'Live online video class (link sent after registration)'], ['Group size', '[number] children'], ['Fee', 'S$500 introductory (regular S$650), workbook included, payable in 3 instalments'], ['Contact', '[name, phone or email]']].map(r => row([cell(r[0], 2500, { bold: true, fill: 'F2F2F2', size: 20, align: AlignmentType.LEFT, h: 80 }), c2(r[1], 7400, { h: 80 })]))));
G.push(p(t('Math Inquirers Holiday Program is an independent enrichment program. It is inspired by enrichment-style thinking skills but is not affiliated with, run by or endorsed by the Ministry of Education or any school.', { size: 18, italics: true, color: '666666' }), { before: 200, after: 0 }));

const doc = new D.Document({ styles: { default: { document: { run: { font: 'Arial', size: S } } } }, sections: [{ properties: { page }, footers: { default: footer(PROG + ' P2 • Program guide') }, children: G }] });
D.Packer.toBuffer(doc).then(b => { fs.writeFileSync('P2_Holiday_Program_Guide.docx', b); console.log('guide built'); });
