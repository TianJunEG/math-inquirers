const C = require('./common.js');
const { fs, D, CW, t, p, cell, tbl, row, q, sub, ans, lines, img, gap, banner, footer, page, AlignmentType, BorderStyle, WidthType } = C;
const L = require('./lessons.js');
const PROG = L.program, SLOGAN = L.slogan;
const G = [];
const S = 21;
const tx = (s, o = {}) => p(t(s, { size: S, ...o }), { after: o.after === undefined ? 80 : o.after, line: 280 });
const h1 = (s, pb) => p(t(s, { bold: true, size: 32, color: '1F3864' }), { before: 0, after: 100, pb, keepNext: true });
const h2 = (s) => p(t(s, { bold: true, size: 24, color: '1F3864' }), { before: 160, after: 60, keepNext: true });
const bu = (s) => p([t('•  ', { size: S }), t(s, { size: S })], { after: 40, indent: { left: 420, hanging: 220 }, line: 280 });
const hd = (s, w) => cell(s, w, { bold: true, fill: 'D9E2F3', size: 20, h: 70 });
const c2 = (s, w, o = {}) => cell(s, w, { size: 20, align: AlignmentType.LEFT, h: 70, ...o });
const seg = (time, title) => p([t(time + '   ', { bold: true, size: 22, color: 'FFFFFF' }), t(title, { bold: true, size: 22, color: 'FFFFFF' })], { before: 160, after: 60, keepNext: true, shading: { type: 'clear', fill: '1F3864', color: 'auto' } });
const say = (lines_) => lines_.forEach((s, i) => G.push(p([t(i === 0 ? 'SAY   ' : '          ', { bold: true, size: 19, color: '1F6F5C' }), t('“' + s + '”', { size: S, italics: true })], { after: 50, indent: { left: 900, hanging: 900 }, line: 280 })));
const doo = (lines_) => lines_.forEach((s, i) => G.push(p([t(i === 0 ? 'DO     ' : '          ', { bold: true, size: 19, color: '7F6000' }), t(s, { size: S })], { after: 40, indent: { left: 900, hanging: 900 }, line: 280 })));
const ask = (rows, a, b) => { G.push(tbl([4600, 5300], [row([hd(a || 'Ask', 4600), hd(b || 'Expect', 5300)]), ...rows.map(r => row([c2(r[0], 4600), c2(r[1], 5300)]))])); G.push(gap(40)); };
const kv = (rows) => tbl([2200, 7700], rows.map(r => row([cell(r[0], 2200, { bold: true, fill: 'F2F2F2', size: 20, align: AlignmentType.LEFT, h: 70 }), c2(r[1], 7700)])));

/* ---------- Title ---------- */
G.push(p(t('TRIAL LESSON  •  60 MINUTES  •  PRIMARY 1', { bold: true, size: 22, color: '666666' }), { after: 20 }));
G.push(p(t(PROG, { bold: true, size: 44 }), { after: 40 }));
G.push(p(t('Lesson 6: Coin Combos', { bold: true, size: 36 }), { after: 40 }));
G.push(p(t(SLOGAN, { italics: true, size: 28, color: '1F3864' }), { after: 120 }));
G.push(tx('A shortened version of Lesson 6 for one classroom period, designed for a class of 29. It has a timed plan with a script, a two-page worksheet, exit tickets, a coin cut-out page and a one-page observation sheet so that you can record what happened.'));
G.push(h2('At a glance'));
G.push(kv([
  ['Big idea', 'Find every way to make an amount with coins, and be sure you have found them all, by starting with the biggest coin and working down.'],
  ['Objective', 'Pupils make 20¢ and 30¢ in different ways with 20¢, 10¢ and 5¢ coins, record the ways in a table, find the fewest coins for an amount, and explain how they know they have every way.'],
  ['Class set-up', '14 pairs and 1 group of three. One coin sheet and one mini whiteboard (or scrap paper) per pair. Each pupil has a worksheet and a pencil.'],
  ['Materials', '15 sheets of the coin cut-outs (one per pair, already cut and in an envelope), 29 worksheets (2 pages, double-sided), 29 exit tickets, 15 mini whiteboards or scrap paper, a board or visualiser for the demonstration.'],
  ['Prepare', 'Solve the worksheet yourself. Cut the coins ahead of time (you can use real 5¢, 10¢ and 20¢ coins instead). Put one envelope on every pair’s desk before pupils arrive.'],
  ['Before you use it', 'Check with your school leaders before using outside material with a class. Do not put pupil names on the observation sheet or take photos of pupils. Record only counts and what you observed.']
]));
G.push(h2('The 60 minutes'));
G.push(tbl([1300, 1900, 6700], [row([hd('Minutes', 1300), hd('Part', 1900), hd('What happens', 6700)]),
  ...[['0–5', 'Warm-up', 'Coin shop: quick questions with the coins on their desks'], ['5–15', 'Explore', 'In pairs, make 20¢ in as many ways as they can'], ['15–23', 'Mini-lesson', 'Worked examples and the key idea'], ['23–25', 'Brain break', 'Coin toss count, standing up'], ['25–45', 'Worksheet', 'Pairs first, then on their own, then stretch'], ['45–53', 'Talk time', 'Share and explain why'], ['53–60', 'Exit ticket', 'One question on a slip, collect, one-sentence reflection']].map(r => row([c2(r[0], 1300, { bold: true }), c2(r[1], 1900, { bold: true }), c2(r[2], 6700)]))]));
G.push(gap(40));
G.push(h2('Running it with 29 pupils'));
['Seat pupils in pairs before the lesson and put the envelope on the desk. Decide who is the trio.', 'Use signals: “Pencils down” for attention, and “Show me” for pairs to hold up their whiteboard so that you can scan the room in ten seconds.', 'Split the room into three zones and visit each zone in turn while pairs work, so that every pair is asked at least one question.', 'When a pair is stuck, give hint 1 and move on. Come back in two minutes. Do not rescue a pair too quickly.', 'For pupils who find the work hard, start the table with the ways that use no 20¢ coin. For fast finishers, give the stretch question, then the challenge.', 'Count out loud from the back of the room: “Ten seconds to finish” and “Five seconds”, so that pupils can plan their finish.'].forEach(s => G.push(bu(s)));

/* ---------- Script ---------- */
G.push(h1('Script'));
G.push(seg('0–5 min', 'Warm-up: Coin shop'));
doo(['Pupils already have the coin sheet on the desk. Hold up a price tag (or write it on the board) for each question. Pairs show the coins, then hold them up.']);
say(['Welcome to the coin shop! I will show you a price tag. You and your partner pay for it with your coins. Show me.']);
ask([['Pay 15¢ using two coins.', '5¢ + 10¢'], ['Pay 25¢ using two coins.', '5¢ + 20¢'], ['Pay 30¢ using two coins.', '10¢ + 20¢'], ['Pay 35¢ using three coins.', '20¢ + 10¢ + 5¢'], ['Who used the fewest coins for 30¢? How many?', '2 coins. You cannot do it with only one.']]);

G.push(seg('5–15 min', 'Explore: how many ways make 20¢?'));
say(['Today we are going to find every way to make 20¢ using only 20¢, 10¢ and 5¢ coins. First, a prediction. How many different ways do you think there are? Write your guess on your whiteboard.', 'Make 20¢ with your coins. Then change some coins to make 20¢ a different way. Draw or write each way. Keep going. Talk to your partner. I will come and ask questions.']);
doo(['Ask pairs to write each way on the whiteboard, like “10 + 5 + 5”.', 'At about minute 13, say “Pencils down” and ask the three questions below.']);
ask([['How many ways did you find for 20¢?', '4 ways: 20; 10 + 10; 10 + 5 + 5; 5 + 5 + 5 + 5.'], ['How do you know you have all of them?', 'Start with the biggest coin and work down.'], ['Are 10 + 5 + 5 and 5 + 10 + 5 different ways?', 'No. The same coins in a different order is the same way.']]);
G.push(p([t('IF STUCK   ', { bold: true, size: 19, color: 'A61C00' }), t('Hint 1: “Start with the biggest coin that fits.”  Hint 2: “Keep one coin the same and change the others.”  Hint 3: “Make 10¢ first, then 10¢ again.”', { size: S })], { after: 60, indent: { left: 1300, hanging: 1300 }, line: 280 }));

G.push(seg('15–23 min', 'Mini-lesson'));
doo(['Draw the table on the board as you think aloud. Columns: 20¢, 10¢, 5¢.']);
say(['Ways to make 15¢ with 10¢ and 5¢ coins. I start with the biggest coin: one 10¢. Then 5¢ is left, so one 5¢ coin. That is one way: 10 + 5.', 'Now no 10¢ coin. Only 5¢ coins: 5 + 5 + 5. That makes two ways altogether.', 'Now 25¢ with 20¢, 10¢ and 5¢. With one 20¢: 20 + 5. With 10¢ but no 20¢: 10 + 10 + 5, and 10 + 5 + 5 + 5. With only 5¢ coins: 5 + 5 + 5 + 5 + 5. That makes 4 ways, and the table helped me to not miss any or repeat any.', 'The key idea today: start with the biggest coin and work down. Same coins in a different order count as one way. Say it with me.']);
ask([['How many ways make 15¢ using 10¢ and 5¢?', '2 ways: 10 + 5; 5 + 5 + 5.'], ['How many ways make 25¢ using 20¢, 10¢ and 5¢?', '4 ways.']]);
G.push(p([t('Watch for: ', { bold: true, size: S }), t('writing the same way twice in a different order; missing the “no 20¢, no 10¢” row; forgetting that the coins must add up exactly.', { size: S })], { after: 60 }));

G.push(seg('23–25 min', 'Brain break: coin toss count'));
doo(['Pupils stand. Toss a pretend coin: heads, 5 star jumps. Tails, 10 knee lifts. Do three tosses and count the total together. Then sit down and take out the worksheet.']);

G.push(seg('25–45 min', 'Worksheet (20 minutes)'));
doo(['Minutes 25 to 33: pairs do Question 1 together (the 30¢ table).', 'Minutes 33 to 41: each pupil does Questions 2 and 3 alone.', 'Minutes 41 to 45: stretch question for pupils who have finished. Others finish Question 3.']);
say(['Pairs first on Question 1. Talk about each way before you write it. I am not looking for speed. I am looking for good thinking. Check each way adds up to 30¢.']);
doo(['Circulate and ask:']);
['“Which coin did you start with in this way?”', '“Is this way the same as that one? Show me with coins.”', '“How do you know there are no more ways?”'].forEach(s => G.push(bu(s)));
G.push(p([t('IF STUCK   ', { bold: true, size: 19, color: 'A61C00' }), t('Hint 1: “Begin with the biggest coin.”  Hint 2: “Keep one coin fixed and change the others.”  Hint 3: “Add up your coins. Is it exactly 30¢?”', { size: S })], { after: 60, indent: { left: 1300, hanging: 1300 }, line: 280 }));
G.push(h2('Worksheet answers'));
ask([
  ['Q1. Ways to make 30¢ with 20¢, 10¢ and 5¢', '6 ways: 20 + 10; 20 + 5 + 5; 10 + 10 + 10; 10 + 10 + 5 + 5; 10 + 5 + 5 + 5 + 5; 5 × 6. (a) fewest: 20 + 10 (2 coins). (b) most: 5 × 6 (6 coins). (c) Start with the biggest coin and work down.'],
  ['Q2. Mei pays 45¢. Fewest coins from 5¢, 10¢, 20¢, 50¢?', '3 coins: 20¢ + 20¢ + 5¢.'],
  ['Q3. Ben has 3 coins worth 35¢. Which coins? Can he use only 2?', '20¢ + 10¢ + 5¢. No: two coins can make 10, 15, 20, 25, 30, 40, 55, 60, 70 or 100, and 35 is not one of them.'],
  ['Stretch. Ali pays 55¢ with exactly 5 coins, using at least one 5¢, one 10¢ and one 20¢.', '20¢ + 10¢ + 10¢ + 10¢ + 5¢ (the only way).']
], 'Question', 'Answer');

G.push(seg('45–53 min', 'Talk time'));
doo(['Bring pupils to attention. Pick two or three pairs, not only the fastest. Ask for the reason, not only the answer.']);
say(['Who found a way to make 30¢ that nobody else found? Tell us.', 'How did you make sure you found every way?', 'Is 10 + 5 + 5 different from 5 + 10 + 5?', 'Why can 35¢ never be made with only two coins?']);
ask([['How did you make sure you found every way?', 'Start with the biggest coin and work down, using a table.'], ['Is 10 + 5 + 5 different from 5 + 10 + 5?', 'No. They use the same coins, so they are one way.'], ['Why can 35¢ never be made with two coins?', 'Listen for: try every pair of coins and none of them add to 35.']], 'Ask', 'Listen for');

G.push(seg('53–60 min', 'Exit ticket and closing'));
doo(['Hand out the exit ticket slips. No talking, no helping. Give about 4 minutes. Collect the slips, then collect the worksheets and coin envelopes.']);
ask([['Make 25¢ using exactly three coins from 5¢, 10¢, 20¢, 50¢.', '10¢ + 10¢ + 5¢.']], 'Exit ticket', 'Answer');
say(['You found every way and you could explain how you knew. That is what an inquirer does: notice, test, check and explain why.', 'Thumbs up, sideways or down: how hard was today? Tell your partner one thing you liked.']);

/* ---------- Observation sheet ---------- */
G.push(h1('After the lesson: what to record', true));
G.push(tx('Fill this in within an hour of the lesson, while you still remember. Please do not write pupil names. This sheet is what will tell us how to improve the program.'));
G.push(h2('Timing'));
G.push(tbl([2400, 1600, 1600, 4300], [row([hd('Part', 2400), hd('Planned', 1600), hd('Actual', 1600), hd('Notes: too long, too short, rushed?', 4300)]), ...[['Warm-up', '5'], ['Explore', '10'], ['Mini-lesson', '8'], ['Brain break', '2'], ['Worksheet', '20'], ['Talk time', '8'], ['Exit ticket', '7']].map(r => row([c2(r[0], 2400, { bold: true }), c2(r[1], 1600, { align: AlignmentType.CENTER }), c2('', 1600), c2('', 4300)]))]));
G.push(h2('How the pupils did'));
G.push(tbl([6200, 3700], [row([hd('Measure', 6200), hd('Count', 3700)]), ...[
  'Pairs that found all 4 ways for 20¢ in Explore (out of 15)',
  'Pairs that used “biggest coin first” without being told',
  'Pairs that found all 6 ways for 30¢ (out of 15)',
  'Pupils who got Question 2 right (45¢ in 3 coins) (out of 29)',
  'Pupils who got the exit ticket right (out of 29)',
  'Pupils who could say why in their own words (your estimate)'
].map(r => row([c2(r, 6200), c2('', 3700)]))]));
G.push(h2('What to change'));
['Which question or step confused most pupils?', 'Which part of the script did you change, and why?', 'Which materials did not work (coins, worksheet layout, whiteboards)?'].forEach(s => { G.push(p(t(s, { size: S, bold: true }), { before: 60, after: 10 })); G.push(...lines(1)); });
G.push(h2('Pupil voice (ask a few pupils in the last minute)'));
['What was the best part?', 'What was the hardest part?', 'Would you like to do more lessons like this? Why or why not?'].forEach(s => G.push(bu(s)));

/* ---------- Student worksheet ---------- */
const hdr = (title, pb = true) => [
  p([t('Lesson 6', { bold: true, size: 24 })], { align: AlignmentType.RIGHT, after: 60, pb }),
  tbl([CW], [row([cell(t(PROG.toUpperCase() + '  •  PRIMARY 1', { bold: true, size: 24 }), CW, { fill: 'D9D9D9', h: 100 })]), row([cell(t('MONEY', { bold: true, size: 26 }), CW, { h: 100 })])]),
  p([t('Name: ', { bold: true, size: 24 }), t('______________________   ', { size: 24 }), t('Class: ', { bold: true, size: 24 }), t('_________   ', { size: 24 }), t('Date: ', { bold: true, size: 24 }), t('____________', { size: 24 })], { before: 160, after: 80 }),
  p(t(title, { bold: true, size: 44 }), { align: AlignmentType.CENTER, after: 100, before: 20 })
];
G.push(...hdr('COIN COMBOS'));
G.push(p('We have 5¢, 10¢, 20¢ and 50¢ coins. You can use the same kind of coin more than once.', { after: 100 }));
G.push(q(1, 'Show different ways to make exactly 30¢ using only 20¢, 10¢ and 5¢ coins. Write how many of each coin in the table. Use your coins to test each way.', { before: 100, keepNext: true }));
{ const ws = [2500, 2470, 2470, 2460];
  G.push(tbl(ws, [row(['Way', 'Number of 20¢', 'Number of 10¢', 'Number of 5¢'].map((s, i) => cell(s, ws[i], { bold: true, fill: 'D9D9D9', size: 22 }))), ...['A', 'B', 'C', 'D', 'E', 'F'].map(l => row([cell(l, ws[0], { bold: true, h: 140 }), cell('', ws[1]), cell('', ws[2]), cell('', ws[3])]))])); }
G.push(gap(60));
G.push(sub('a', 'Which way uses the FEWEST coins?')); G.push(ans());
G.push(sub('b', 'Which way uses the MOST coins?')); G.push(ans());
G.push(sub('c', 'How do you know you have found ALL the ways?'));
G.push(...lines(2));

G.push(p('', { pb: true, after: 0 }));
G.push(p(t('Lesson 6  •  Coin Combos  •  Name: ____________________', { bold: true, size: 22, color: '666666' }), { after: 80 }));
G.push(q(2, 'Mei wants to pay exactly 45¢. She can use 5¢, 10¢, 20¢ and 50¢ coins. What is the smallest number of coins she can use? Which coins are they?', { before: 60 }));
G.push(...lines(2)); G.push(ans());
G.push(q(3, 'Ben has 3 coins. They are worth 35¢ altogether. Which coins does he have?', { before: 200 }));
G.push(ans());
G.push(sub('a', 'Can Ben make 35¢ using only 2 coins? Explain your answer.'));
G.push(...lines(2));
G.push(banner('Stretch  (for strong thinkers)'));
G.push(q(4, 'Ali pays 55¢ with exactly 5 coins. He uses at least one 5¢, one 10¢ and one 20¢ coin. Which coins does he use?', { before: 140 }));
G.push(...lines(3)); G.push(ans());
G.push(p([t('One thing I noticed today: ______________________________________', { size: 24 })], { before: 200, after: 60 }));

/* ---------- Exit tickets ---------- */
G.push(p(t('Exit tickets', { bold: true, size: 40 }), { pb: true, after: 80, align: AlignmentType.CENTER }));
G.push(p(t('Print one page for 8 pupils (4 rows of two slips) and cut along the lines. You need 29 slips, so print four pages.', { size: 22 }), { after: 120, align: AlignmentType.CENTER }));
{
  const w = CW / 2; const sl = () => cell([p(t('Exit ticket  •  Lesson 6', { bold: true, size: 20 }), { after: 40 }), p(t('Make 25¢ using exactly three coins from 5¢, 10¢, 20¢, 50¢.', { size: 22 }), { after: 120 }), p(t('My answer: ______________________', { size: 22 }), { after: 100 }), p(t('How do I know? ____________________', { size: 22 }), { after: 40 })], w, { align: AlignmentType.LEFT, h: 140, borders: { top: { style: BorderStyle.DASHED, size: 6, color: '777777' }, bottom: { style: BorderStyle.DASHED, size: 6, color: '777777' }, left: { style: BorderStyle.DASHED, size: 6, color: '777777' }, right: { style: BorderStyle.DASHED, size: 6, color: '777777' } } });
  G.push(tbl([w, w], [row([sl(), sl()]), row([sl(), sl()]), row([sl(), sl()]), row([sl(), sl()])]));
}

/* ---------- Coin cut-outs ---------- */
G.push(p(t('Coin cut-outs', { bold: true, size: 40 }), { pb: true, after: 80, align: AlignmentType.CENTER }));
G.push(p(t('Print 15 copies of this page, one for each pair. Cut along the circles and put the coins in an envelope. Each sheet has 7 × 5¢, 7 × 10¢, 6 × 20¢ and 5 × 50¢. You can also use real or play coins instead.', { size: 24 }), { after: 120, align: AlignmentType.CENTER }));
G.push(img('coins.png', 600, 369));

const doc = new D.Document({ styles: { default: { document: { run: { font: 'Arial', size: S } } } }, sections: [{ properties: { page }, footers: { default: footer(PROG + ' • Lesson 6 trial (60 minutes)') }, children: G }] });
D.Packer.toBuffer(doc).then(b => { fs.writeFileSync('Math_Inquirers_Lesson6_Trial_60min.docx', b); console.log('trial built'); });
