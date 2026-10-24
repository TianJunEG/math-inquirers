const C = require('../hp/common.js');
const { fs, D, CW, t, p, cell, tbl, row, gap, footer, page, AlignmentType, BorderStyle, WidthType } = C;
const L = require('./data.js');
const HG = require('../levels/habit_guide.js');   // focus habit line (levels/habits.json)
const SG = require('../levels/spine_guide.js');   // strategy card + common look-back lines (levels/spine.json)
const BUD = require('./budget.json').lessons;   // written by rebuild/p6_budget.py: the minute plan of every lesson
const fm = x => String(x);
const TAKEHOME = { 1: 'Q5', 2: 'Q5', 4: 'Q7', 5: 'Q5', 7: 'Q5', 8: 'Q5', 9: 'Q6', 10: 'Q2' };   // the worksheet question moved to take-home (starred in the workbook)
const partOf = (n, title) => BUD[String(n)].parts.find(q => q.title.startsWith(title));
const rg = q => fm(q.start) + '–' + fm(q.end);
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
  ['Level', 'Primary 6 students after the PSLE (ages 11 to 13), going into Secondary 1, who enjoy thinking and coding puzzles'],
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
  ['2', 'Opening', 'Welcome, the hook and today’s question.', 'Sit in a circle or horseshoe.', 'Cameras on.'],
  ['3.5 to 4.5', 'Sneak-peek puzzles', 'Two puzzles on ideas we have not learnt yet. The first is an access puzzle any child can try with objects or a drawing. Everyone shows their paper ONCE, after both puzzles, then the answers are clicked through. Nobody is marked.', 'Own paper held to the tutor.', 'Everyone says the answers together on three; nothing is held up to the camera.'],
  ['5.5 to 6.5', 'Warm-up', 'A quick game of 3 or 4 items, then 3 quick questions. Everyone joins in.', 'Sit in a circle or horseshoe.', 'Cameras on. Answers by thumbs, hands or chat.'],
  ['12.5 to 15', 'Explore', 'Hands-on in pairs. Objects first, no writing yet. Two discussion questions at the end.', 'Materials box on each table.', 'Each child has their own materials at home. Pairs go to breakout rooms.'],
  ['8 to 12.5', 'Mini-lesson', 'Tutor builds the table on the board, names the rule and asks what stays the same and what changes.', 'Whiteboard.', 'Shared slide and annotation tool.'],
  ['4.5 to 5.5', 'Brain break', 'Stand, stretch, drink water.', 'A short movement game.', 'Stand up on camera. Count the stretches together.'],
  ['30 to 35.5', 'Worksheet', 'Start in pairs, finish alone. Tutor asks “how do you know?” rather than giving answers. One question is marked take-home with a star. Check together: all answers appear at once, children mark in a different colour, one volunteer explains the key question (about 35 seconds a question).', 'Printed workbook, tutor circulates.', 'Printed workbook. Child ticks their own page against the answer slide. Nothing is held up to the camera. Tutor checks one or two answers each.'],
  ['1.5 to 4', 'Flex', 'Unscripted buffer right after the worksheet check. Use it for Think harder or to catch up. It is lost first when the lesson runs late.', 'Open.', 'Open.'],
  ['5 to 6', 'Talk time', 'Volunteers share an answer and explain it. Pass is always fine. No cold-calling by name, no tallies or rankings.', 'Volunteers first.', 'Volunteers unmute. Invitations to try Think harder go to the whole group.'],
  ['6.5 to 8.5', 'Exit slip, looking back, stamp', 'Exit slip (2.5 to 4.5 minutes, everyone ticks it against the answer slide), then looking back (2 minutes, private), then close and stamp (2 minutes). The last four minutes are never cut.', 'Paper slip, tutor stamps.', 'Child writes the answer on the Finish page and ticks it. Tutor stamps the next time or posts it.']
];
G.push(tx('The column “Minutes” gives how long each part lasts. The exact minute marks for each lesson are printed in its own script below and on its slides; each lesson adds up to 90 minutes. Never cut the sneak-peek puzzles, the exit slip, the looking back or the stamp. If you run late, use the ladder after the table.'));
G.push(tbl([900, 1450, 2700, 2300, 2550], [row([hd('Minutes', 900), hd('Part', 1450), hd('What happens', 2700), hd('Face to face', 2300), hd('Online', 2550)]), ...R.map(r => row([c2(r[0], 900, { align: AlignmentType.CENTER, bold: true }), c2(r[1], 1450, { bold: true }), c2(r[2], 2700), c2(r[3], 2300), c2(r[4], 2550)]))]));
G.push(h2('If you run late: the cut-first ladder'));
G.push(tx('Every lesson has a flex buffer (1.5 to 4 minutes) right after the worksheet check. It is the first thing to lose. If the lesson is still late, cut in this order and never touch the fixed items:'));
['Skip the Go further what-if (it is not a slide any more: it is in the notes of the explore slide and can be pasted in the chat).', 'Ask one quick question fewer in the warm-up, then one explore discussion question fewer.', 'Check together: explain only the starred question on each page (the one that carries the idea).', 'Move the second talk question to the opener of the next lesson.', 'Never cut: the sneak-peek puzzles, the exit slip, the looking back (2 minutes), the stamp, and in Lesson 10 the certificates and the last stamp.'].forEach((x, i) => G.push(bl((i + 1) + '.', x)));
G.push(h2('Teaching habits that matter'));
['Ask “How do you know?” after every answer, right or wrong.', 'Wait 10 seconds before helping. Let children struggle a little.', 'Praise the thinking (“You checked it two ways”), not just the answer.', 'Let children disagree with each other and settle it with objects or a drawing.', 'If a child finishes early, point to Think harder, Go further or the Investigation on the Finish page, not extra drill. Never say who is on which page, and never split a pair unless both children agree.'].forEach(s => G.push(bu(s)));

G.push(h2('Toolbox and look-back (every lesson)'));
G.push(tx('Every lesson has one TOOL OF THE DAY, shown on the workbook card on page 1, on the title slide (with a small badge on the talk slide) and named in your script. It is one of eight tools a child can choose for any problem. Say its name, point at the card, and at talk time ask where the tool helped. Lesson 10: children choose their own tool. Passing is always allowed.'));
G.push(tbl([2500, 7400], [row([hd('Tool', 2500), hd('What we say (ages 10 to 13)', 7400)]), ...SG.DATA.tools.map(t => row([c2(t.name, 2500, { bold: true }), c2(t.def.C, 7400)]))]));
G.push(gap(40));
G.push(tx('The look-back is the same every lesson: pick ONE problem from today and ask three things. ' + SG.DATA.lookback.prompts.C.map((q, i) => (i + 1) + ') ' + q).join(' ') + ' Children tick yes or not yet for questions 1 and 2, write one short line for question 3 (I checked by ...), and tick the tools they used. The timer is ' + SG.info(6, 1).timer + ' seconds, then stamp the journals. Nothing is collected, read aloud or marked.'));
G.push(h2('Focus habit (every lesson)'));
G.push(tx('Every lesson names ONE focus habit on its front page, on the opening slide and on the look-back slide, and has one “explain your thinking” item in the online practice. The habit is something the children practise; you are not testing it. The same six habits are used at every level. Do not give the answer first: ask the prompt, wait, and give a hint only if the child is stuck.'));
G.push(tbl([1500, 2700, 5700], [row([hd('Habit', 1500), hd('Child says', 2700), hd('Your move and prompt', 5700)]), ...Object.keys(HG.DATA.habits).map(k => row([c2(k, 1500, { bold: true }), c2('“' + HG.DATA.habits[k].phrase + '”', 2700), c2(HG.DATA.habits[k].move + ' Say: “' + HG.DATA.habits[k].prompt + '”', 5700)]))]));
G.push(gap(40));
G.push(h2('Preparing the materials'));
['Send the workbook PDF to parents one week before. Ask them to print it single-sided and the cut-out pages on card if they can.', 'Each child needs a computer or tablet with Scratch 3 (free online). Python is optional (any online Python editor). Scratch starter files: lessons 1 to 9 each have one .sb3 file and Lesson 10 has four (L10A to L10D), kept in the folder p6/scratch/starters. Send the lesson’s file to parents with the workbook; the child opens it with File, Load from your computer. No Scratch account, log-in or sharing is needed, and the tutor answer versions in p6/scratch/answers are never sent to families. Cut-outs used: unplugged code cards (Lessons 1, 4, 7), square grid (Lessons 7, 9).', 'Keep the answer key with the tutor only. Check answers together on screen.', 'Use the shared screen or a digital whiteboard for the mini-lesson table.'].forEach(s => G.push(bu(s)));
G.push(h2('Setting up online'));
['Send parents the workbook and materials list one week before. Needed: the printed workbook and cut-outs, scissors, a ruler, paper and a pencil, and a computer with Scratch (plus the lesson’s Scratch starter file, saved where the child can find it, for example the Downloads folder).', 'Use one approved platform with breakout rooms and screen share. Admit only registered children and never share the link publicly.', 'Ask the parent to sit nearby but not give answers. The camera should show the child’s page and hands.', 'Nothing is held up to the camera. At the end of each lesson children tick their own work against the answer slide. If a child is still stuck, they mark their own look-back page and the parent photographs it for the tutor after class (business WhatsApp), never during the recorded class.', 'Lessons are recorded on the approved platform so that children who miss one can catch up; follow “Recording the lesson” in this guide. Do not make your own recordings or photos. Add a second tutor or helper above 8 children.'].forEach(s => G.push(bu(s)));

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
// a segment is a budget part {start, end} from p6/budget.json; the REC cue gets a whole-minute length (rounded) because reccues.js reads whole minutes
const pushSeg = (part, title, over) => { const time = fm(part.start) + '–' + fm(part.end) + ' min'; G.push(seg(time, title)); const c = over || REC.cue(title, '0–' + (part.end - part.start), CURL); SEGS.push({ time, title, action: c.action }); rec(c.say); };
const ask = (rows, h1c, h2c) => { G.push(tbl([4600, 5300], [row([hd(h1c || 'Ask', 4600), hd(h2c || 'Expect', 5300)]), ...rows.map(r => row([c2(r[0], 4600), c2(r[1], 5300)]))])); G.push(gap(40)); };
const stuck = (lines) => lines.forEach((s, i) => G.push(p([t(i === 0 ? 'IF STUCK   ' : '                ', { bold: true, size: 19, color: 'A61C00' }), t(s, { size: S })], { after: 40, indent: { left: 1300, hanging: 1300 }, line: 280 })));

G.push(h1('How to use the scripts', true));
G.push(tx('Rules for every lesson: no public labels (never say advanced, top group, strong or early finisher), no announcing who is on which page, no cold-calling by name, no public tallies or rankings, and “pass” is always fine. Every lesson below is a minute-by-minute script. The slides match it: one slide or two for each part. You do not have to say the words exactly, but keep the questions, because the questions are what makes children think.'));
G.push(tbl([1500, 8400], [
  ['SAY', 'Words to say aloud, in plain language for 11- to 13-year-olds. Said in your own voice, not read from the page.'],
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

L.lessons.forEach(l => {
  CURL = l; SEGS.length = 0;
  const BP = t => partOf(l.n, t), ten = l.n === 10;
  const d = DD[String(l.n)], s = SC[l.n], q = QB[String(l.n)], gp = L.gaps[String(l.n)];
  G.push(h1('Lesson ' + l.n + ': ' + l.title, true));
  G.push(p(t('Week ' + l.week + (l.session === 'A' ? ' (first lesson)' : ' (second lesson)') + '   •   ' + l.topic + '   •   Workbook: Lesson ' + l.n, { size: 20, color: '666666' }), { after: 80 }));
  G.push(tx(HG.line(6, l.n), { bold: true, size: 20, after: 100 }));
  G.push(tbl([1900, 8000], [
    ['Objective', l.objective], ['Thinking skills', l.skills], ['Materials', l.materials], ['Online set-up', l.online],
    ['Prepare', 'Solve the worksheet yourself first. Set out one materials box per pair. Open the slides for this lesson and check the answers in the speaker notes.'],
    ['Watching the recording', 'A child who missed the live lesson watches the recording. They need: ' + l.materials + ' The REC lines tell them when to pause; the chapter list at the end of this lesson shows each part.']
  ].map(r => row([cell(r[0], 1900, { bold: true, fill: 'F2F2F2', size: 20, align: AlignmentType.LEFT, h: 60 }), c2(r[1], 8000, { h: 60 })]))));
  G.push(gap(40));
  if (ten) doo(['Lesson 10 timing: this lesson changes the usual routine, so use this plan instead of the usual minute marks. ' + BUD['10'].parts.map(q => q.title + ' ' + rg(q)).join('; ') + '. A working copy of one starter with one change is full marks. The showcase gives each child 2 minutes 15 seconds plus a 20-second switch (8 children fit in 22 minutes). The slide deck has the same times.']);

  pushSeg(BP('Opening'), 'Opening');
  say(s.hook);
  doo(['Greet each child by name. Show the lesson title slide. Read “Today we will…” aloud.']);
  { const sp = SG.info(6, l.n); say([sp.openSay]); doo([sp.openDo + (sp.kitLine ? ' Say: “' + sp.kitLine + '.”' : '')]); }

  pushSeg(BP('Sneak'), 'Sneak-peek puzzles');
  say(['Two sneak-peek puzzles. They are ideas we have not learnt yet, so guessing is welcome and “I do not know” is welcome. Nobody is marked. Write your answers on your own paper. When I say “say it”, after BOTH puzzles, everyone says the answers together on three, once.']);
  ask(gp.sneak.map(x => [x[0], x[1]]), 'Sneak-peek puzzle', 'Answer and what to listen for');
  doo(['Puzzle 1 is an access puzzle: any child can try it with objects, a drawing or counting, so everyone gets a first win. Puzzle 2 is a thinking puzzle on the idea of today’s lesson.', 'ONE check moment: after both puzzles, everyone says the answers together on three, once (nothing is held up to the camera). Never use private chat and never read wrong answers aloud. At minute ' + fm(BP('Sneak').end - 1) + ' click through the answers, one after the other with no reaction round (each answer in 15 words or fewer), and say: “Both of these are what we learn today.”', 'Do not record the sneak-peek as a mark. Never announce who got which right, never say who will start on which page, and never use the word “advanced” or “top group”.', 'Invite the WHOLE group, never one child: “When you have finished Start here, you can choose Think harder, Go further or the Investigation.” Nobody is singled out. The point printed on page 1 (“After question N you may choose…”) is the same for all. Any child can choose it, and any child can go back. Do not split a pair unless both children agree.']);
  if (!ten) {
    const wp = BP('Warm-up');
  pushSeg(wp, 'Warm-up');
  doo([d.warmGame + ' (Minutes ' + rg({ start: wp.start, end: wp.end - 2.5 }) + '. Keep it friendly: no racing or timers, and no points for being first. Play only the items on the slide.)']);
  say(s.warmIntro);
  doo(['At about minute ' + fm(wp.end - 2.5) + ', ask the ' + d.warmQs.length + ' quick questions on the warm-up slide. Use thumbs or a whisper to partners before taking answers. Stop at minute ' + fm(wp.end) + '.']);
  ask(d.warmQs.map(x => [x[0], x[1]]));

  const ep = BP('Explore');
  pushSeg(ep, 'Explore (in pairs, with objects)');
  say(s.predict);
  doo(d.expSetup.map((x, i) => (i + 1) + '. ' + x));
  say(['Talk to your partner while you work. I will come round and ask you questions.']);
  stuck(s.exploreHints);
  doo(['Go further what-if (not a slide any more: paste it in the chat for any pair that finishes early, and skip it first if you run late): ' + gp.go[0] + ' Answer: ' + gp.go[1] + ' Nobody has to wait: a pair that has finished can pick this up.']);
  doo(['At about minute ' + fm(ep.end - 3) + ', say “Pencils down” and bring the group back together. Take the ' + ['', 'one', 'two', 'three'][d.expAsk.length] + ' questions below, one at a time.']);
  ask(d.expAsk.map(x => [x[0], x[1]]));

  const mp = BP('Mini-lesson');
  pushSeg(mp, 'Mini-lesson (you teach, they join in)');
  doo(['Show the mini-lesson slides. Think aloud as you work. Say what you notice, what you test and how you check. Children copy how you think.']);
  say(s.think);
  G.push(tbl([4600, 5300], [row([hd('Worked example on the slides', 4600), hd('Answer', 5300)]), row([c2(d.mini1.head + '. ' + (d.mini1.body || []).join(' '), 4600), c2(d.mini1.ans, 5300)]), row([c2(d.mini2.head + '. ' + (d.mini2.body || []).join(' '), 4600), c2(d.mini2.ans, 5300)])]));
  G.push(gap(40));
  say([d.keyHead.replace(/^Key idea: /, 'The key idea today is: ') + '. ' + d.keyBig + ' Say it with me.']);
  doo(['Show the key idea slide in the last minute or two of the mini-lesson (it ends at minute ' + fm(mp.end) + '). The “common mistakes” on that slide are for you, not the children. Watch for them during the worksheet:']);
  l.mistakes.forEach(m => G.push(bu(m)));

  const bk = BP('Brain break');
  pushSeg(bk, 'Brain break');
  doo([d.brk, 'Water. Toilet break for anyone who needs it. Keep it to ' + fm(bk.end - bk.start) + ' minutes.']);

  const wsp = BP('Worksheet'), fp = BP('Flex');
  pushSeg(wsp, 'Worksheet (pairs, then alone, then your choice)');
  doo(['Minute ' + fm(wsp.start) + ': give out the workbook. Read the title of Lesson ' + l.n + ' aloud. Say “Pairs first. Talk before you write.”', 'Follow the minute labels on the slides: short teaching slides come before page 1 and before page 2, pairs work together on page 1, each child works alone on page 2, and a check-together slide follows each page. Show the page preview slides, do not read them aloud. On the check slides ALL the answers are shown at once: children mark in a different colour, and one volunteer explains only the question that carries the idea (about 35 seconds a question). ' + (TAKEHOME[l.n] ? 'Question ' + TAKEHOME[l.n] + ' is marked with a star and the words “take-home” in the workbook: children do it at home, its answer is on the check slide and in the key, and you take it up at the start of the next lesson. ' : 'No question is moved to take-home in this lesson. ') + 'Any child who has finished can choose Think harder, Go further or the Investigation (all printed in the workbook; the extra slides are optional and carry no clock time). The Finish page is for everyone. The worksheet part ends at minute ' + fm(wsp.end) + '.']);
  say(['Pairs first. Read each question aloud and talk about it before you write. I am not looking for speed. I am looking for good thinking.']);
  doo(['Circulate and ask:']);
  s.circulate.forEach(c => G.push(bu(c)));
  stuck(s.hints);
  doo(['Think harder, Go further and the Investigation are open to every child, with no label. The Investigation is printed on the Finish page that every child gets. After question 3 (see the line printed on page 1) any child may choose to carry on or try Think harder. Never announce who is on which page. Do not split a pair unless both children agree.']);
  G.push(h2('Stretch and challenge questions'));
  const TH = l.th;
  ask([...TH.map((x, i) => ['Workbook Think harder ' + (i + 1) + ': ' + x.q, x.a]), ...(q.challenge || []).slice(-3).map((x, i) => ['Workbook Go further ' + (i + TH.length + 1) + ': ' + x.q, x.a]), ['Workbook Investigation, Finish page (' + gp.inv.kind + '): ' + gp.inv.q + ' ' + gp.inv.first, gp.inv.a]], 'Question', 'Answer');
  G.push(tx('These are the questions on the Think harder, Go further and Finish pages in the workbook. More are in the separate Question Bank.', { size: 19, color: '666666' }));

  G.push(seg(rg(fp) + ' min', 'Flex (unscripted buffer, lost first)'));
  doo(['Flex: ' + fm(fp.end - fp.start) + ' minutes with no script, right after the worksheet check. Use them for Think harder, a pair that needs a catch-up, or the second talk question. This is the part you lose first when the lesson is running late; the sneak-peek puzzles, the exit slip, the looking back and the stamp are never cut.']);

  pushSeg(BP('Talk time'), 'Talk time');
  doo(['Bring the group back to a circle (or camera on, mics on). Ask for volunteers first and choose two or three of them, not only the fastest. Never cold-call a child by name. “Pass” is always fine, and the next person helps. No public tallies, points or rankings.']);
  say(s.talk);
  if (s.talkNext) doo(['Second talk question (cut-first ladder: only if flex is left, otherwise it is the opener of the next lesson): ' + s.talkNext]);
  { const sp = SG.info(6, l.n); ask([[l.share, s.talkAns], [sp.talkAsk, sp.talkListen]], 'Discussion question', 'Listen for'); }

  const xp = BP('Exit slip');
  pushSeg({ start: xp.start, end: 90 }, 'Exit slip, looking back and closing');
  doo(['Minutes ' + fm(xp.start) + ' to 86: exit slip. Children write on the exit slip box of the Finish page (or a slip of paper). No talking, no helping. Show the exit ticket slide. When most children are done, everyone ticks the slip against the answer slide; nothing is held up to the camera.']);
  ask([[l.exit.q, l.exit.a]], 'Exit slip', 'Answer');
  say(s.close);
  G.push(h2('Look back (2 minutes, minutes 86 to 88: timer ' + SG.info(6, l.n).timer + ' seconds, then stamps)'));
  { const sp = SG.info(6, l.n);
    say([sp.lookSay, 'Thank you. Drawing it, listing, trying a smaller case or checking another way: those are all good ways to get unstuck.']);
    doo(['Show the look-back slide and start its timer (' + sp.timer + ' seconds); the Look back box is on the Finish page, not on the Think harder pages. ' + sp.lookDo.replace(/^Start the timer\. /, '').replace(/ Then stamp journals\.$/, '') + ' Never mark or grade the box, never collect it in front of the group and never read an answer out. Never ask a child to show the box to the camera. Praise the strategy, not the speed: \u201c' + gp.reflectEx + ', and that is what got you unstuck\u201d, never \u201cyou were quick\u201d. If a child ticks \u201cI am still stuck\u201d, check in during the open session the same day: visit the shared breakout room or use a hand signal, with a parent nearby, never by private message.']);
  }
  doo(['Minutes 88 to 90: stamp the inquiry journal when a child shows you the exit slip. Mark S, D or H in the progress tracker at the back of this guide. If a child marked D or H, plan two minutes of catch-up at the start of the next lesson.']);
  } else {
    const cp = BP('Challenge'), sp = BP('Starter'), bk = BP('Brain break'), pb = BP('Plan and build'), fp = BP('Flex'), sh = BP('Showcase'), xp = BP('Exit slip'), lb = BP('Looking back'), cl = BP('Certificates');
    pushSeg(cp, 'Explore: challenge round in teams of 2, then check');
    say(s.predict);
    doo(d.expSetup.map((x, i) => (i + 1) + '. ' + x));
    say(['Talk to your partner while you work. I will come round and ask you questions.']);
    stuck(s.exploreHints);
    doo(['Teams do Q1 and Q3. Q2 (prime hunters) is marked with a star and the words “take-home”: its answer is on the check slide and in the key. There is no separate “how we started” slide: ask it as the first line of the check together. Do not read the page preview aloud. On the check slide all answers appear at once and children mark in a different colour (about 35 seconds a question). The challenge round ends at minute ' + fm(cp.end) + '.']);
    ask(d.expAsk.slice(0, 1).map(x => [x[0], x[1]]));

    pushSeg(sp, 'Starter projects: mini-lesson (you teach, they join in)');
    doo(['Run only Starter A live (the Mystery Machine). Starters B, C and D get one line each on their slides and children run them when they load the file. Think aloud as you work: say what you notice, what you test and how you check.']);
    say(s.think);
    G.push(tbl([4600, 5300], [row([hd('Worked example on the slides', 4600), hd('Answer', 5300)]), row([c2(d.mini1.head + '. ' + (d.mini1.body || []).join(' '), 4600), c2(d.mini1.ans, 5300)]), row([c2(d.mini2.head + '. ' + (d.mini2.body || []).join(' '), 4600), c2(d.mini2.ans, 5300)])]));
    G.push(gap(40));
    say([d.keyHead.replace(/^Key idea: /, 'The key idea today is: ') + '. ' + d.keyBig + ' Say it with me.']);
    doo(['Show the key idea slide at the end of the starter projects. The “common mistakes” on that slide are for you, not the children. Watch for them while children build:']);
    l.mistakes.forEach(m => G.push(bu(m)));

    pushSeg(bk, 'Brain break');
    doo([d.brk, 'Water at the desk, no toilet round (say so at the start of the break). Keep it to ' + fm(bk.end - bk.start) + ' minutes.']);

    pushSeg(pb, 'Plan and build (workbook page 2, then Scratch)', { say: 'Pause. Fill in your plan on workbook page 2 (your idea, the answer you worked out by hand, and your twist), then build your program in Scratch and test it with a value you worked out first. This takes about ' + fm(pb.end - pb.start) + ' minutes. Press play to see how the showcase works.', action: 'Pause. Fill in the plan on workbook page 2, build and test the program in Scratch (about ' + fm(pb.end - pb.start) + ' minutes). Press play for the showcase.' });
    doo(['Minute ' + fm(pb.start) + ': children plan on workbook page 2 and then build. Q4: only the part for the starter the child picked (about 2 minutes); Q5: three cells (idea, answer, twist); Q6: three test rows written BEFORE running. Do not read the preview slide aloud. A working copy of one starter with one change is full marks. Think harder, Go further and the Investigation are open to every child, with no label. The build part ends at minute ' + fm(pb.end) + '.']);
    say(['Plan first, on paper. Then build. I am not looking for speed. I am looking for good thinking.']);
    doo(['Time checks for you (say them aloud): minute 40 “plan finished, start building”; minute 52 “save your file, test with your worked-out value”; minute 58 “stop building, show-and-tell next”. If most children are still building at minute 58, the flex (to ' + fm(fp.end) + ') is for finishing. If you are still behind at ' + fm(fp.end) + ', do not shorten the exit slip, the looking back or the certificates: start the showcase on time and give each child 2 minutes (show 20 s, run 25 s, test 30 s, maths 45 s). A child whose program is not working shows the plan page and the one test worked out by hand, and you run the unchanged starter for the audience. That is a complete showcase.']);
    doo(['Circulate and ask:']);
    s.circulate.forEach(c => G.push(bu(c)));
    stuck(s.hints);
    G.push(h2('Stretch and challenge questions'));
    const TH = l.th;
    ask([...TH.map((x, i) => ['Workbook Think harder ' + (i + 1) + ': ' + x.q, x.a]), ...(q.challenge || []).slice(-3).map((x, i) => ['Workbook Go further ' + (i + TH.length + 1) + ': ' + x.q, x.a]), ['Workbook Investigation, Finish page (' + gp.inv.kind + '): ' + gp.inv.q + ' ' + gp.inv.first, gp.inv.a]], 'Question', 'Answer');

    G.push(seg(rg(fp) + ' min', 'Flex (unscripted buffer, lost first)'));
    doo(['Flex: ' + fm(fp.end - fp.start) + ' minutes with no script, right after the build. Use them to finish and save, to fix one bug, or to get the showcase screens ready. Lose it first.']);

    pushSeg(sh, 'Showcase (8 children, 2 minutes 15 seconds each)');
    doo(['Each child gets 2 minutes 15 seconds (show the puzzle 25 seconds, run it 30 seconds, show one test you knew the answer to 35 seconds, explain the maths 45 seconds) plus a 20-second switch, so 8 children take about 21 minutes. The audience types stars in the chat (two stars and a question); stars are not spoken. A child may paste a screenshot into the chat and you run their file. Pass is always fine.']);
    say([l.share]);

    pushSeg(xp, 'Exit slip with the talk question');
    doo(['Children write the exit slip on the Finish page, with no talking and no helping. The last line is the talk question, answered on the slip: ' + s.talk[0] + ' Everyone ticks the slip against the answer slide. There is no separate talk time in this lesson.']);
    ask([[l.exit.q, l.exit.a]], 'Exit slip', 'Answer');

    pushSeg(lb, 'Looking back');
    { const sp = SG.info(6, l.n);
      say([sp.lookSay, 'Thank you. Drawing it, listing, trying a smaller case or checking another way: those are all good ways to get unstuck.']);
      doo(['Show the look-back slide and start its timer (' + sp.timer + ' seconds); the Look back box is on the Finish page. ' + sp.lookDo.replace(/^Start the timer\. /, '').replace(/ Then stamp journals\.$/, '') + ' Never mark or grade the box, never collect it in front of the group and never read an answer out. Never ask a child to show the box to the camera. Praise the strategy, not the speed: \u201c' + gp.reflectEx + ', and that is what got you unstuck\u201d, never \u201cyou were quick\u201d. If a child ticks \u201cI am still stuck\u201d, check in during the open session the same day: visit the shared breakout room or use a hand signal, with a parent nearby, never by private message.']);
      doo(['Tool question: ' + sp.talkAsk + ' ' + sp.talkListen]);
    }

    pushSeg(cl, 'Certificates and closing');
    say(s.close);
    doo(['Certificates are sent to parents as a PDF with one specific line of praise already written for each child (use the showcase rubric). On the last slide say one sentence of praise to the whole group. Stamp the last journal page when a child shows you the exit slip. Mark S, D or H in the progress tracker at the back of this guide.']);
  }
  G.push(h2('Extra idea for anyone who wants it'));
  G.push(tx(l.extension));
  G.push(h2('Answer key (workbook)'));
  l.key.forEach(k => G.push(p([t(k[0] + '  ', { bold: true, size: 20 }), t(k[1], { size: 20 })], { after: 50, indent: { left: 240 }, line: 270 })));
  G.push(p([t('Investigation  ', { bold: true, size: 20 }), t(gp.inv.a, { size: 20 })], { after: 50, indent: { left: 240 }, line: 270 }));
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
['In Lesson 10, send each child a certificate as a PDF with one specific line of praise already written, and hand over (or post) their completed inquiry journal.', 'Send parents a short message through the approved channel: one thing their child did well, and one thing to keep practising.', 'Delete or hand over all Student Data within 7 days after the last lesson (this is in the tutor agreement).'].forEach(s => G.push(bu(s)));

/* ---------- Tutor checklist ---------- */
G.push(h1('Tutor checklist', true));
G.push(h2('Before each lesson'));
['Read the lesson plan and solve the worksheet yourself without looking at the key.', 'Check materials are ready, or the online set-up has been sent.', 'Test the platform, screen share and annotation tools 10 minutes early (online).', 'Print or open the slide deck for the lesson.'].forEach(s => G.push(bu(s)));
G.push(h2('During the lesson'));
['Circulate and ask questions rather than giving answers.', 'Use only the approved channels to contact parents. No private messages to children.', 'Do not take your own photos or recordings. The only recording is the lesson recording made on the approved platform under “Recording the lesson”.', 'If you have a concern about a child’s safety or welfare, tell the Company straight away.'].forEach(s => G.push(bu(s)));
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
G.push(tbl([2500, 7400], [['Dates', '[start date] to [end date], two lessons a week'], ['Time', '[day] and [day], [start time] to [end time]'], ['Where', 'Live online video class (link sent after registration)'], ['Group size', '[number] children'], ['Fee', 'S$250 beta fee for all 10 lessons (S$25 a lesson), printed workbook and cut-out kit included'], ['Contact', '[name, phone or email]']].map(r => row([cell(r[0], 2500, { bold: true, fill: 'F2F2F2', size: 20, align: AlignmentType.LEFT, h: 80 }), c2(r[1], 7400, { h: 80 })]))));
G.push(p(t('Math Inquirers Holiday Program is an independent enrichment program. It is inspired by thinking-skills enrichment ideas but is not affiliated with, run by or endorsed by the Ministry of Education or any school.', { size: 18, italics: true, color: '666666' }), { before: 200, after: 0 }));

const doc = new D.Document({ styles: { default: { document: { run: { font: 'Arial', size: S } } } }, sections: [{ properties: { page }, footers: { default: footer(PROG + ' P6 • Program guide') }, children: G }] });
D.Packer.toBuffer(doc).then(b => { fs.writeFileSync('P6_Holiday_Program_Guide.docx', b); console.log('guide built'); });
