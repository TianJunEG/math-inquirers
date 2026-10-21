const C = require('./common.js');
const { fs, D, CW, t, p, cell, tbl, row, q, sub, ans, lines, img, gap, banner, footer, page, dots, AlignmentType, BorderStyle, WidthType, ShadingType, VerticalAlign, Paragraph, TextRun, TableCell } = C;
const L = require('./lessons.js');
const PROG = L.program, SLOGAN = L.slogan;
const W = [];
const hdr = (n, topic, title, pb = true) => [
  p([t('Lesson ' + n, { bold: true, size: 24 })], { align: AlignmentType.RIGHT, after: 60, pb }),
  tbl([CW], [row([cell(t(PROG.toUpperCase() + '  •  PRIMARY 1', { bold: true, size: 24 }), CW, { fill: 'D9D9D9', h: 100 })]), row([cell(t(topic.toUpperCase(), { bold: true, size: 26 }), CW, { h: 100 })])]),
  p([t('Name: ', { bold: true, size: 24 }), t('______________________   ', { size: 24 }), t('Class / Group: ', { bold: true, size: 24 }), t('_________   ', { size: 24 }), t('Date: ', { bold: true, size: 24 }), t('____________', { size: 24 })], { before: 160, after: 120 }),
  p(t(title, { bold: true, size: 44 }), { align: AlignmentType.CENTER, after: 120, before: 20 })
];


const QB = require('./qbank.json');
const extra = (n) => {
  const ls = L.lessons[n - 1], b = QB[String(n)];
  const out = [...hdr(n, ls.topic, 'THINK HARDER')];
  out.push(p(t('Use objects, draw a picture or make a table. Then write how you know.', { italics: true, size: 24 }), { after: 80, align: AlignmentType.CENTER }));
  out.push(banner('Stretch'));
  b.stretch.slice(0, 4).forEach((x, i) => { out.push(q(i + 1, x.q, { before: 140, after: 40, keepNext: true })); out.push(...lines(3)); });
  out.push(p('', { pb: true, after: 0 }));
  out.push(p(t('Lesson ' + n + '  •  ' + ls.topic.toUpperCase(), { bold: true, size: 22, color: '666666' }), { after: 60 }));
  out.push(banner('Challenge  (for strong thinkers)'));
  b.challenge.slice(-3).forEach((x, i) => { out.push(q(i + 5, x.q, { before: 200, after: 40, keepNext: true })); out.push(...lines(4)); });
  return out;
};
/* ---------- COVER + PASSPORT ---------- */
W.push(p(t(PROG.toUpperCase(), { bold: true, size: 48 }), { align: AlignmentType.CENTER, before: 40, after: 60 }));
W.push(p(t(SLOGAN, { italics: true, size: 32 }), { align: AlignmentType.CENTER, after: 80 }));
W.push(p(t('Primary 1 Holiday Program  •  10 lessons  •  Student workbook', { size: 24 }), { align: AlignmentType.CENTER, after: 140 }));
W.push(p([t('Name: ', { bold: true }), t('______________________________   '), t('Group: ', { bold: true }), t('__________')], { after: 140 }));
W.push(banner('My Inquirer Rules'));
['1.  Notice the pattern.', '2.  Test it with objects first.', '3.  Check your answer.', '4.  Explain why.'].forEach(s => W.push(p(t(s, { size: 26 }), { before: 40, after: 20, indent: { left: 400 } })));
W.push(gap(60));
W.push(banner('My Inquiry Journal  (your tutor stamps each lesson)'));
W.push(gap(40));
{
  const w = CW / 2; const rows = [];
  for (let i = 0; i < 10; i += 2) rows.push(row([0, 1].map(k => { const ls = L.lessons[i + k]; return cell(['Lesson ' + ls.n, ls.title, ' '], w, { h: 90 }); })));
  W.push(tbl([w, w], rows));
}
W.push(p(t('Tutor: ______________________    Program dates: ______________________', { size: 22 }), { before: 160, after: 0 }));

/* ---------- LESSON 1 ---------- */
W.push(...hdr(1, 'Whole Numbers: Number Patterns', 'COUNT WITH THE FROG!'));
W.push(p('Look for the pattern. Fill in the missing numbers.', { italics: true, after: 80 }));
W.push(q(1, 'Skip counting. Fill in the blanks.'));
W.push(sub('a', 'Counting in 2s:   2,  4,  6,  ____,  ____,  12,  ____,  16'));
W.push(sub('b', 'Counting in 5s:   5,  10,  ____,  20,  ____,  30,  ____'));
W.push(sub('c', 'Counting in 3s:   3,  6,  ____,  12,  ____,  18'));
W.push(q(2, 'What is the rule? Fill in the rule and the next two numbers.'));
W.push(sub('a', '4,  7,  10,  13,  ____,  ____        Rule: ______________'));
W.push(sub('b', '30,  27,  24,  21,  ____,  ____       Rule: ______________'));
W.push(sub('c', '2,  6,  10,  14,  ____,  ____        Rule: ______________'));
W.push(q(3, 'A frog starts at 0 and hops 4 steps each time. Colour the numbers where the frog lands.', { keepNext: true }));
{ const w = Math.floor(CW / 21); const ws = Array(21).fill(w); ws[20] = CW - w * 20; W.push(tbl(ws, [row(ws.map((x, i) => cell(String(i), x, { size: 20, h: 150 })))])); }
W.push(gap(80));
W.push(sub('a', 'A second frog also starts at 0 but hops 5 steps each time. Mark its landing numbers with a cross (X) above the number line.'));
W.push(sub('b', 'Besides 0, which number do BOTH frogs land on?'));
W.push(ans());
W.push(q(4, 'Ali counts in 2s from 2 up to 50. Mei counts in 5s from 5 up to 50.', { pb: true, before: 0 }));
W.push(sub('a', 'Which numbers will BOTH of them say?'));
W.push(ans());
W.push(sub('b', 'What do you notice about these numbers?'));
W.push(...lines(2));
W.push(q(5, 'Mei puts stickers in boxes. Box 1 has 2 stickers. Each box after it has 3 more stickers than the box before.', { keepNext: true }));
{ const ws = [CW - 8000, ...Array(10).fill(800)]; const vals = ['2', '5'];
  W.push(tbl(ws, [row([cell('Box', ws[0], { bold: true, fill: 'EDEDED' }), ...Array.from({ length: 10 }, (_, i) => cell(String(i + 1), 800, { bold: true, fill: 'EDEDED' }))]),
    row([cell('Stickers', ws[0], { bold: true }), ...Array.from({ length: 10 }, (_, i) => cell(vals[i] || '', 800, { h: 160 }))])])); }
W.push(gap(100));
W.push(sub('a', 'Fill in the table. How many stickers are in Box 10?'));
W.push(ans());
W.push(sub('b', 'Look at the numbers of stickers. Are they odd or even? What pattern do you see?'));
W.push(...lines(2));

/* ---------- LESSON 2 ---------- */
W.push(...extra(1));
W.push(...hdr(2, 'Whole Numbers: Number Bonds', 'NUMBER BOND INQUIRY'));
W.push(q(1, 'Number bonds of 10. Fill in the blanks.', { before: 40, keepNext: true }));
{ const items = ['10 = 3 + ____', '10 = ____ + 6', '10 = 8 + ____', '10 = ____ + 5', '10 = 0 + ____']; const w = CW / 5; W.push(tbl(Array(5).fill(w), [row(items.map(s => cell(s, w, { size: 24, h: 170 })))])); }
W.push(q(2, 'List the pairs that make 10, from the smallest first number.', { keepNext: true }));
W.push(sub('a', '0 + 10,   1 + 9,   2 + ____,   3 + ____,   4 + ____,   5 + ____'));
W.push(sub('b', 'When the first number goes up by 1, what happens to the second number?'));
W.push(...lines(1));
W.push(sub('c', 'How many different pairs make 10 if 3 + 7 and 7 + 3 count as the SAME pair?'));
W.push(ans());
W.push(q(3, 'Use bonds of 10 to help you with bonds of 20.', { keepNext: true }));
W.push(sub('a', '6 + 4 = 10, so  16 + 4 = ____   and   6 + 14 = ____'));
W.push(sub('b', '7 + 3 = 10, so  17 + 3 = ____   and   7 + 13 = ____'));
W.push(sub('c', '20 = 12 + ____        20 = ____ + 9        20 = 15 + ____'));
W.push(q(4, 'The = sign means “is the same as”. Fill in the blanks.', { pb: true, before: 0, keepNext: true }));
W.push(sub('a', '5 + 3 = 4 + ____            (b)  7 + ____ = 9 + 2'));
W.push(sub('c', '3 + 8 = ____ + 5            (d)  6 + 6 = 10 + ____'));
W.push(sub('e', 'Mei says “4 + 4 = 8 + 1 is true.” Is she right? Explain.'));
W.push(...lines(2));
W.push(q(5, 'Magic triangle. Put the numbers 1, 2, 3, 4, 5 and 6 in the circles so that each side of the triangle adds up to 9.', { keepNext: true }));
W.push(img('magic.png', 300, 267));
W.push(sub('a', 'Which numbers did you put in the corners?   ______________'));
W.push(sub('b', 'Challenge: now make each side add up to 10. Which numbers are in the corners this time?   ______________'));
W.push(q(6, 'Two numbers add up to 10. One is 2 more than the other. What are the numbers?', { keepNext: true }));
W.push(ans('Answer:', 560));
W.push(p([t('Challenge: two numbers add up to 12. One is 4 more than the other. What are they?   ', { size: 24 }), t('___________', { size: 24 })], { indent: { left: 560 }, after: 100 }));

/* ---------- LESSON 3 ---------- */
W.push(...extra(2));
W.push(...hdr(3, 'Picture Graphs', 'LET’S PLAN THE FRUIT PARTY!'));
W.push(p('Our teacher wants to buy fruit for a class party. Every child voted for ONE fruit. The picture graph shows the votes.', { after: 120 }));
W.push(p([t('Key:  ', { bold: true }), t('●', { color: '333333' }), t(' = 1 child')], { after: 100 }));
{ const rows = [['Apple', 6, 'C0392B'], ['Banana', 5, 'B8860B'], ['Orange', 8, 'E67E22'], ['Grape', 3, '7D3C98'], ['Watermelon', 5, '1E8449']];
  W.push(tbl([2400, 7500], [row([cell('Fruit', 2400, { bold: true, fill: 'D9D9D9' }), cell('Votes', 7500, { bold: true, fill: 'D9D9D9' })]), ...rows.map(r => row([cell(r[0], 2400, { bold: true, h: 40 }), cell(dots(r[1], r[2]), 7500, { align: AlignmentType.LEFT, h: 40 })]))])); }
W.push(gap(20));
W.push(banner('Part A: Read the graph'));
W.push(q(1, 'Which fruit got the most votes?', { before: 140 })); W.push(ans());
W.push(q(2, 'Which fruit got the fewest votes?')); W.push(ans());
W.push(q(3, 'How many more children chose orange than grape?')); W.push(ans());
W.push(q(4, 'Two fruits got the same number of votes. Which two fruits are they?')); W.push(ans());
W.push(q(5, 'How many children voted altogether? (Hint: each child had only 1 vote.)')); W.push(ans());
W.push(q(6, [t('Mei says, “Orange is the best fruit for the whole school!”')], { pb: true, before: 0 }));
W.push(sub('a', [t('Is Mei right?    '), t('Yes  /  No', { bold: true })]));
W.push(sub('b', 'Why do you think so?'));
W.push(...lines(2));
W.push(q(7, 'What else should the teacher think about before buying fruit for the party?'));
W.push(...lines(3));
W.push(gap(140));
W.push(banner('Part B: Now it’s your turn!'));
W.push(p('Ask your own group to vote. Each child votes for ONE fruit. Make a tally mark for each vote.', { before: 140, after: 100 }));
W.push(tbl([2400, 5700, 1800], [row([cell('Fruit', 2400, { bold: true, fill: 'D9D9D9' }), cell('Tally', 5700, { bold: true, fill: 'D9D9D9' }), cell('Total', 1800, { bold: true, fill: 'D9D9D9' })]), ...['Apple', 'Banana', 'Orange', 'Grape', 'Watermelon'].map(f => row([cell(f, 2400, { bold: true }), cell('', 5700, { h: 90 }), cell('', 1800, { h: 90 })]))]));
W.push(q(8, 'Which fruit did YOUR group like best?  ____________________    Is it the same as the graph above?  Yes / No', { before: 200 }));
W.push(q(9, 'Why might two groups choose different fruits?'));
W.push(...lines(2));

/* ---------- LESSON 4 ---------- */
W.push(...extra(3));
W.push(...hdr(4, 'Patterns', 'PATTERN INQUIRY'));
W.push(q(1, 'Look at the shape pattern. Draw the missing shapes in places 8 and 9.', { before: 60 }));
W.push(img('shapes.png', 640, 92));
W.push(q(2, 'The pattern keeps going in the same way.'));
W.push(sub('a', 'What shape will be in place 10?   ____________________'));
W.push(sub('b', 'What shape will be in place 12?   ____________________'));
W.push(sub('c', 'Without drawing, what shape will be in place 30?   ____________________'));
W.push(sub('d', 'How do you know?'));
W.push(...lines(2));
W.push(q(3, 'Ben makes a row of triangles with matchsticks.', { keepNext: true, pb: true, before: 0 }));
W.push(img('sticks.png', 620, 127));
W.push(sub('a', 'Count the sticks. Fill in the table. Keep going until you reach 10 triangles.'));
{ const ws = [CW - 7600, ...Array(10).fill(760)]; const vals = { 1: '3', 2: '5', 3: '7' };
  W.push(tbl(ws, [row([cell('Triangles', ws[0], { bold: true, fill: 'EDEDED', size: 22 }), ...Array.from({ length: 10 }, (_, i) => cell(String(i + 1), 760, { bold: true, fill: 'EDEDED' }))]),
    row([cell('Sticks', ws[0], { bold: true, size: 22 }), ...Array.from({ length: 10 }, (_, i) => cell(vals[i + 1] || '', 760, { h: 170 }))])])); }
W.push(gap(100));
W.push(sub('b', 'Each time Ben adds 1 more triangle, how many more sticks does he need?'));
W.push(ans());
W.push(sub('c', 'Why does he need only that many more sticks? (Look at the picture.)'));
W.push(...lines(2));
W.push(sub('d', 'How many sticks are needed for 10 triangles?'));
W.push(ans());
W.push(q(4, 'Challenge! Ben has 15 sticks. How many triangles in a row can he make?'));
W.push(ans('Answer:', 560));
W.push(p([t('Show how you worked it out:', { italics: true })], { indent: { left: 560 } }));
W.push(...lines(2));

/* ---------- LESSON 5 ---------- */
const mach = (cells) => { const ws = cells.map(c => c.w); return tbl(ws, [row(cells.map(c => cell(c.text, c.w, { fill: c.fill, bold: c.bold, h: 110, size: 26 })))]); };
W.push(...extra(4));
W.push(...hdr(5, 'Working Backwards', 'MYSTERY NUMBER'));
W.push(p('To find a mystery number, work backwards. Do the opposite steps in the opposite order.', { italics: true, after: 80 }));
W.push(q(1, 'I think of a number. Find my number and write it in the yellow box.', { keepNext: true }));
W.push(sub('a', 'I add 5. I get 12.', { after: 40, keepNext: true }));
W.push(mach([{ text: '?', w: 1700, fill: 'FFF2CC', bold: true }, { text: '→', w: 800 }, { text: '+ 5', w: 1700, fill: 'EDEDED' }, { text: '→', w: 800 }, { text: '12', w: 1700, fill: 'DDEBF7', bold: true }]));
W.push(gap(40));
W.push(sub('b', 'I take away 3. I get 9.', { after: 40, keepNext: true }));
W.push(mach([{ text: '?', w: 1700, fill: 'FFF2CC', bold: true }, { text: '→', w: 800 }, { text: '− 3', w: 1700, fill: 'EDEDED' }, { text: '→', w: 800 }, { text: '9', w: 1700, fill: 'DDEBF7', bold: true }]));
W.push(gap(40));
W.push(sub('c', 'I add 4. Then I take away 2. I get 10.', { after: 40, keepNext: true }));
W.push(mach([{ text: '?', w: 1300, fill: 'FFF2CC', bold: true }, { text: '→', w: 600 }, { text: '+ 4', w: 1300, fill: 'EDEDED' }, { text: '→', w: 600 }, { text: '− 2', w: 1300, fill: 'EDEDED' }, { text: '→', w: 600 }, { text: '10', w: 1300, fill: 'DDEBF7', bold: true }]));
W.push(q(2, 'A number machine adds the same number every time.', { keepNext: true }));
W.push(sub('a', 'The machine adds 6. Fill in the table.', { keepNext: true }));
W.push(tbl([1800, 1500, 1500, 1500, 1500], [row([cell('IN', 1800, { bold: true, fill: 'EDEDED' }), cell('2', 1500), cell('5', 1500), cell('9', 1500), cell('', 1500, { h: 140 })]), row([cell('OUT', 1800, { bold: true, fill: 'EDEDED' }), cell('8', 1500), cell('11', 1500), cell('', 1500, { h: 140 }), cell('14', 1500)])]));
W.push(gap(100));
W.push(sub('b', 'A different machine. What does it do to every number?', { keepNext: true }));
W.push(tbl([1800, 1500, 1500, 1500, 1500], [row([cell('IN', 1800, { bold: true, fill: 'EDEDED' }), cell('3', 1500), cell('6', 1500), cell('10', 1500), cell('15', 1500)]), row([cell('OUT', 1800, { bold: true, fill: 'EDEDED' }), cell('7', 1500), cell('10', 1500), cell('14', 1500), cell('', 1500, { h: 140 })])]));
W.push(p([t('Rule: ______________     If OUT is 30, then IN is ______', { size: 26 })], { indent: { left: 1000 }, before: 100, after: 100 }));
W.push(q(3, 'Ali has 8 marbles. Mei has 5 more marbles than Ali. Ben has 6 fewer marbles than Mei.', { pb: true, before: 0 }));
W.push(sub('a', 'How many marbles does Mei have?   ____'));
W.push(sub('b', 'How many marbles does Ben have?   ____'));
W.push(sub('c', 'How many more marbles does Mei have than Ben?   ____'));
W.push(sub('d', 'How many marbles do they have altogether?   ____'));
W.push(p([t('Draw a bar for each child to help you.', { italics: true })], { indent: { left: 1000 } }));
W.push(...lines(3));
W.push(q(4, 'Queue puzzles.', { keepNext: true }));
W.push(sub('a', 'There are 20 children in a queue. Mei is 7th from the front. How many children are behind her?'));
W.push(ans());
W.push(sub('b', 'Ali is 8th from the front AND 8th from the back. How many children are in the queue? (Careful: Draw it!)'));
W.push(ans());
W.push(...lines(1));
W.push(q(5, 'Make your own mystery number story. Give it to a friend to solve!'));
W.push(...lines(3));

/* ---------- LESSON 6 ---------- */
W.push(...extra(5));
W.push(...hdr(6, 'Money', 'COIN COMBOS'));
W.push(p('We have 5¢, 10¢, 20¢ and 50¢ coins. You can use the same kind of coin more than once.', { after: 100 }));
W.push(q(1, 'Show different ways to make exactly 20¢ using only 20¢, 10¢ and 5¢ coins. Write how many of each coin in the table.', { before: 100, keepNext: true }));
{ const ws = [2500, 2470, 2470, 2460];
  W.push(tbl(ws, [row(['Way', 'Number of 20¢', 'Number of 10¢', 'Number of 5¢'].map((s, i) => cell(s, ws[i], { bold: true, fill: 'D9D9D9', size: 22 }))), ...['A', 'B', 'C', 'D', 'E'].map(l => row([cell(l, ws[0], { bold: true, h: 140 }), cell('', ws[1]), cell('', ws[2]), cell('', ws[3])]))])); }
W.push(gap(60));
W.push(sub('a', 'Which way uses the FEWEST coins?')); W.push(ans());
W.push(sub('b', 'Which way uses the MOST coins?')); W.push(ans());
W.push(sub('c', 'How do you know you have found ALL the ways?'));
W.push(...lines(2));
W.push(q(2, 'Challenge! Find ALL the ways to make 30¢ using 20¢, 10¢ and 5¢ coins. Write each way like this:  20¢ + 5¢ + 5¢', { pb: true, before: 0 }));
W.push(...lines(6));
W.push(q(3, 'Mei wants to pay exactly 85¢ using 5¢, 10¢, 20¢ and 50¢ coins.', { before: 240, keepNext: true }));
W.push(sub('a', 'What is the smallest number of coins she can use? Which coins are they?')); W.push(ans());
W.push(sub('b', 'Find a different way that uses exactly 6 coins.')); W.push(ans());
W.push(q(4, 'Ben has 4 coins. They are worth 70¢ altogether. Find ALL the sets of 4 coins he could have.'));
W.push(...lines(3));
W.push(q(5, 'Can Ben make 35¢ using only 2 coins? Explain your answer.'));
W.push(...lines(2));
W.push(q(6, 'Sam has only 10¢ and 20¢ coins. He pays exactly 90¢ using 6 coins.', { keepNext: true }));
W.push(sub('a', 'How many of each coin does he use?')); W.push(ans());
W.push(sub('b', 'Can Sam pay 90¢ using exactly 4 coins? Explain.'));
W.push(...lines(2));
W.push(q(7, 'Dollars! We also have $1 coins and $2, $5, $10 and $50 notes.', { keepNext: true }));
W.push(sub('a', 'A toy costs $17. Pay exactly with the fewest notes and coins.')); W.push(ans());
W.push(sub('b', 'Show 3 different ways to pay exactly $20.'));
W.push(...lines(3));
W.push(sub('c', 'Mei has one $50 note and two $10 notes. A bicycle costs $65 and a helmet costs $8. Does she have enough money for both? Explain.'));
W.push(...lines(2));

/* ---------- LESSON 7 ---------- */
W.push(...extra(6));
W.push(...hdr(7, 'Shapes', 'SHAPE SAFARI'));
W.push(q(1, 'Count the shapes in the house picture.', { before: 40, keepNext: true }));
W.push(img('house.png', 250, 159));
W.push(tbl([2475, 2475, 2475, 2475], [row(['Circle', 'Triangle', 'Square', 'Rectangle'].map(s => cell(s, 2475, { bold: true, fill: 'EDEDED' }))), row(['', '', '', ''].map(s => cell(s, 2475, { h: 160 })))]));
W.push(gap(40));
W.push(sub('a', 'Which shape is there the most of?   ____________      (b)  How many shapes altogether?   ____'));
W.push(q(2, 'Sides and corners. Fill in the table.', { keepNext: true }));
{ const ws = [3300, 3300, 3300]; const rs = [['Circle', '0', '0'], ['Triangle', '3', '3'], ['Square', '', ''], ['Pentagon', '', ''], ['Hexagon', '', ''], ['Octagon', '', '']];
  W.push(tbl(ws, [row(['Shape', 'Sides', 'Corners'].map((s, i) => cell(s, ws[i], { bold: true, fill: 'EDEDED' }))), ...rs.map(r => row(r.map((s, i) => cell(s, ws[i], { h: 50, bold: i === 0, size: 22 }))))])); }
W.push(gap(60));
W.push(sub('a', 'What do you notice about the number of sides and corners?  ______________________'));
W.push(sub('b', 'A shape has 7 sides. How many corners does it have?   ____'));
W.push(q(3, 'Who am I?', { pb: true, before: 0 }));
W.push(sub('a', 'I have 4 sides. All my sides are the same length. I have 4 corners.   ____________'));
W.push(sub('b', 'I have no corners and no straight sides.   ____________'));
W.push(sub('c', 'I have 6 sides.   ____________'));
W.push(q(4, 'How many triangles can you find in each picture? Count the small ones first, then the bigger ones.', { keepNext: true }));
W.push(img('trifigs.png', 560, 131));
W.push(p([t('A: ____          B: ____          C: ____', { bold: true })], { indent: { left: 1000 }, after: 100 }));
W.push(q(5, 'Two triangles of the same size are put together along one side. Draw one shape you can make. What is it called?'));
W.push(...lines(6));
W.push(p([t('Shape name: ____________________', { bold: true })], { indent: { left: 560 }, before: 120 }));

/* ---------- LESSON 8 ---------- */
W.push(...extra(7));
W.push(...hdr(8, 'Logic and Sorting', 'LOGIC LAB'));
W.push(q(1, 'Put them in order using the clues.', { before: 40 }));
W.push(sub('a', 'Ali is taller than Ben. Ben is taller than Mei.   Tallest: ________   Shortest: ________'));
W.push(sub('b', 'The cat is heavier than the dog. The hen is lighter than the dog.   Heaviest: ________   Lightest: ________'));
W.push(sub('c', 'The red ribbon is longer than the blue one. The green one is shorter than the blue one. The yellow one is longer than the red one. Write them from longest to shortest:'));
W.push(p([t('______________,  ______________,  ______________,  ______________')], { indent: { left: 1000 }, after: 100 }));
W.push(q(2, 'Write each number from 1 to 10 in the right place in the Venn diagram.', { keepNext: true }));
W.push(img('venn.png', 480, 269));
W.push(sub('a', 'Numbers that are in BOTH circles: ____________________'));
W.push(sub('b', 'Why do those numbers belong in the middle?'));
W.push(...lines(2));
W.push(q(3, 'Who has which pet? Ali, Mei and Ben each have ONE pet: a cat, a dog or a fish.', { pb: true, before: 0 }));
W.push(p('Clue 1: Ali does not have a cat or a dog.', { indent: { left: 560 }, after: 40 }));
W.push(p('Clue 2: Mei does not have a dog.', { indent: { left: 560 }, after: 100 }));
W.push(p([t('Put a tick where it fits and a cross where it cannot.', { italics: true })], { indent: { left: 560 }, after: 80 }));
W.push(tbl([2400, 2300, 2300, 2300], [row(['', 'Cat', 'Dog', 'Fish'].map((s, i) => cell(s, i ? 2300 : 2400, { bold: true, fill: 'EDEDED' }))), ...['Ali', 'Mei', 'Ben'].map(n => row([cell(n, 2400, { bold: true, h: 150 }), cell('', 2300), cell('', 2300), cell('', 2300)]))]));
W.push(p([t('Ali has the ______.   Mei has the ______.   Ben has the ______.', { bold: true })], { indent: { left: 560 }, before: 120, after: 100 }));
W.push(q(4, 'Four children stand in a line: Ali, Ben, Mei and Sam.', { keepNext: true }));
W.push(p('Mei is first. Ben is behind Ali. Sam is behind Ben. Where does each child stand?', { indent: { left: 560 }, after: 80 }));
W.push(tbl([2475, 2475, 2475, 2475], [row(['1st', '2nd', '3rd', '4th'].map(s => cell(s, 2475, { bold: true, fill: 'EDEDED' }))), row(['', '', '', ''].map(s => cell(s, 2475, { h: 150 })))]));
W.push(q(5, 'Number riddles. Who am I?', { before: 200, keepNext: true }));
W.push(sub('a', 'I am between 10 and 20. I am odd. When you count in 5s, you say me.   ____'));
W.push(sub('b', 'I am between 20 and 40. When you count in 2s you say me. When you count in 5s you say me too.   ____'));
W.push(sub('c', 'I have 2 digits. My digits add up to 5. I am less than 20.   ____'));
W.push(q(6, 'Which one does NOT belong?   3,   6,   9,   11', { keepNext: true }));
W.push(p('Explain why. Then try to find a second reason!', { indent: { left: 560 }, after: 40 }));
W.push(...lines(2));

/* ---------- LESSON 9 ---------- */
W.push(...extra(8));
W.push(...hdr(9, 'Length', 'MEASURE IT!'));
W.push(q(1, 'Three ribbons are made of equal squares.', { before: 40, keepNext: true }));
W.push(img('ribbons.png', 400, 160));
W.push(sub('a', 'Which ribbon is the longest?   ____       (b)  Which is the shortest?   ____'));
W.push(sub('c', 'How many squares longer is ribbon A than ribbon B?   ____'));
W.push(sub('d', 'Ribbon A and ribbon B are put end to end. How many squares long is that?   ____'));
W.push(sub('e', 'Ribbon C is cut shorter by 2 squares. Which ribbon is it now the same length as?   ____'));
W.push(q(2, 'Measure with cubes. Use the paper cube strip from the back of the workbook (or real cubes). Guess first, then measure.', { keepNext: true }));
W.push(tbl([3300, 2200, 2200, 2200], [row(['Object', 'My guess', 'Measured', 'Difference'].map((s, i) => cell(s, [3300, 2200, 2200, 2200][i], { bold: true, fill: 'EDEDED' }))), ...['A pencil', 'A book', 'A shoe', 'My choice: ____________'].map(n => row([cell(n, 3300, { h: 110, align: AlignmentType.LEFT }), cell('', 2200), cell('', 2200), cell('', 2200)]))]));
W.push(sub('a', 'Why must every cube be the same size?'));
W.push(...lines(1));
W.push(q(3, 'Ali measures a desk with his hand span. It is 6 spans long. Mei measures the same desk with her hand span. It is 8 spans long.', { pb: true, before: 0 }));
W.push(sub('a', 'Whose hand span is longer?   ____________'));
W.push(sub('b', 'How do you know?'));
W.push(...lines(2));
W.push(q(4, 'One paper clip is as long as 2 erasers.'));
W.push(sub('a', 'A desk is 5 paper clips long. How many erasers long is it?   ____'));
W.push(sub('b', 'A pencil is 12 erasers long. How many paper clips long is it?   ____'));
W.push(q(5, 'Mei’s pencil is 8 cubes long. Ali’s pencil is 3 cubes longer than Mei’s. Ben’s pencil is 2 cubes shorter than Mei’s.', { keepNext: true }));
W.push(sub('a', 'How long is Ali’s pencil?   ____ cubes'));
W.push(sub('b', 'How long is Ben’s pencil?   ____ cubes'));
W.push(sub('c', 'If all three pencils are put end to end, how many cubes long are they?   ____ cubes'));
W.push(q(6, 'Challenge! Find something at home that is exactly 10 cubes long. What is it?'));
W.push(...lines(1));

/* ---------- LESSON 10 ---------- */
W.push(...extra(9));
W.push(...hdr(10, 'Mixed Puzzles', 'CHALLENGE DAY!'));
W.push(p([t('Show how you know. Remember the inquirer rules!', { italics: true })], { after: 60 }));
W.push(q(1, 'Pattern:   3,   8,   13,   18,   ____,   ____       Rule: ______________', { before: 40 }));
W.push(q(2, 'Two numbers add up to 12. One is 2 more than the other. What are they?   ____ and ____'));
W.push(q(3, 'The graph shows pets in a street.', { keepNext: true }));
{ const rows = [['Dog', 4, 'B8860B'], ['Cat', 7, 'C0392B'], ['Fish', 3, '2E86C1'], ['Bird', 5, '1E8449']];
  W.push(tbl([2000, 7900], rows.map(r => row([cell(r[0], 2000, { bold: true, h: 40 }), cell(dots(r[1], r[2], 36), 7900, { align: AlignmentType.LEFT, h: 40 })])))); }
W.push(p([t('● = 1 pet', { size: 22 })], { before: 40, after: 60 }));
W.push(sub('a', 'How many more cats than birds?   ____'));
W.push(sub('b', 'How many pets are there altogether?   ____'));
W.push(sub('c', 'Which two kinds of pet together make exactly 10?   ______________'));
W.push(q(4, 'You have one 20¢ coin, two 10¢ coins and two 5¢ coins.'));
W.push(sub('a', 'How much money do you have?   ____'));
W.push(sub('b', 'Which of your coins make exactly 35¢?   ______________'));
W.push(q(5, 'Shapes', { keepNext: true, pb: true, before: 0 }));
W.push(sub('a', 'I have 4 corners and 4 sides all the same length. What am I?   ____________'));
W.push(sub('b', 'How many triangles are in this picture?   ____', { keepNext: true }));
W.push(img('apex2.png', 270, 162));
W.push(q(6, 'Ali is older than Ben. Mei is younger than Ben. Who is the youngest?   ____________'));
W.push(q(7, 'I think of a number. I add 9. Then I take away 4. I get 10. What is my number?   ____'));
W.push(q(8, 'A pencil is 6 cubes long. A pen is 4 cubes longer than the pencil.', { keepNext: true }));
W.push(sub('a', 'How long is the pen?   ____ cubes'));
W.push(sub('b', 'Put the pen and the pencil end to end. How long are they together?   ____ cubes'));
W.push(q(9, 'Make a challenge puzzle for a friend. Write the puzzle and the answer.', { keepNext: true }));
W.push(...lines(4));
W.push(p([t('The puzzle I liked best today was ______________________ because ______________________', { size: 24 })], { before: 240, after: 100 }));

W.push(...extra(10));
/* ---------- APPENDIX: CUT-OUTS ---------- */
W.push(p(t('Cut-outs', { bold: true, size: 40 }), { pb: true, after: 80, align: AlignmentType.CENTER }));
W.push(p(t('For Lesson 6 (Coin Combos) and Lesson 9 (Measure It!). Print, cut along the dashed lines, and keep in an envelope.', { size: 24 }), { after: 120, align: AlignmentType.CENTER }));
W.push(p(t('Play coins', { bold: true, size: 28 }), { after: 60 }));
W.push(img('coins.png', 600, 369));
W.push(p(t('Paper cube strips (every square is the same size)', { bold: true, size: 28 }), { before: 120, after: 60 }));
W.push(img('cubestrip.png', 640, 120));
W.push(p(t('Play notes and $1 coins', { bold: true, size: 40 }), { pb: true, after: 80, align: AlignmentType.CENTER }));
W.push(p(t('For Lesson 6 (Coin Combos). Cut along the dashed lines.', { size: 24 }), { after: 120, align: AlignmentType.CENTER }));
W.push(img('kit_notes.png', 600, 421));
W.push(p(t('Inquirer Kit', { bold: true, size: 40 }), { pb: true, after: 80, align: AlignmentType.CENTER }));
W.push(p(t('Nothing needs to be bought. Print, cut out and keep everything in one envelope.', { size: 24 }), { after: 100, align: AlignmentType.CENTER }));
W.push(img('kit_frames.png', 600, 506));
W.push(p(t('Number strips and sorting tiles', { bold: true, size: 40 }), { pb: true, after: 80, align: AlignmentType.CENTER }));
W.push(img('kit_strips.png', 600, 300));
W.push(img('kit_tiles.png', 600, 391));

/* ---------- CERTIFICATE ---------- */
{
  const thick = { style: BorderStyle.DOUBLE, size: 24, color: '1F3864' };
  const bd = { top: thick, bottom: thick, left: thick, right: thick };
  W.push(p('', { pb: true, after: 400 }));
  W.push(new D.Table({ width: { size: CW, type: WidthType.DXA }, columnWidths: [CW], rows: [new D.TableRow({ children: [new TableCell({
    width: { size: CW, type: WidthType.DXA }, borders: bd, margins: { top: 500, bottom: 500, left: 400, right: 400 }, verticalAlign: VerticalAlign.CENTER,
    children: [
      p(t('CERTIFICATE OF COMPLETION', { bold: true, size: 48, color: '1F3864' }), { align: AlignmentType.CENTER, before: 200, after: 300 }),
      p(t(PROG, { bold: true, size: 36 }), { align: AlignmentType.CENTER, after: 80 }),
      p(t('Primary 1 Holiday Program', { size: 28 }), { align: AlignmentType.CENTER, after: 400 }),
      p(t('This certifies that', { size: 26 }), { align: AlignmentType.CENTER, after: 200 }),
      p(t('________________________________', { size: 34 }), { align: AlignmentType.CENTER, after: 200 }),
      p(t('completed all 10 lessons, solved puzzles, spotted patterns and explained their thinking.', { size: 26 }), { align: AlignmentType.CENTER, after: 400 }),
      p(t(SLOGAN, { italics: true, size: 32, color: '1F3864' }), { align: AlignmentType.CENTER, after: 500 }),
      p(t('Tutor: ____________________          Date: ________________', { size: 24 }), { align: AlignmentType.CENTER, after: 200 })
    ] })] })] }));
}

const doc = new D.Document({ styles: { default: { document: { run: { font: 'Arial', size: 26 } } } }, sections: [{ properties: { page }, footers: { default: footer(PROG + '  •  ' + SLOGAN) }, children: W }] });
D.Packer.toBuffer(doc).then(b => { fs.writeFileSync('P1_Holiday_Program_Student_Workbook.docx', b); console.log('workbook built'); });
