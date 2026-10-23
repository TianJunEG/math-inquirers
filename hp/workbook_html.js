const C = require('./common_html.js');
const { fs, D, CW, t, p, cell, tbl, row, q, sub, ans, lines, img, gap, banner, footer, page, dots, AlignmentType, BorderStyle, WidthType, ShadingType, VerticalAlign, Paragraph, TextRun, TableCell } = C;
const L = require('./lessons.js');
const PROG = L.program, SLOGAN = L.slogan;
const W = [];
const SP = require('../levels/spine_wb.js');   // strategy card + common look-back (docs/pedagogy/spine_routine_spec.md); wording in levels/spine.json
const LEVEL = 1;
const COMPACT = new Set([3, 6, 7]);   // lessons whose first page is too full for the full card: compact chip in the header row (see docs/pedagogy/spine_routine_build_notes.md)
const hdr = (n, topic, title, pb = true, tag = 'Start here') => {
  const first = tag === 'Start here';   // the card sits on the first page of each lesson only
  const choose = first && SP.DATA.lessons[`${LEVEL}.${n}`].main === 'choose';
  const compact = first && COMPACT.has(n);
  const card = first && !compact ? SP.card(LEVEL, n) : '';
  const chip = compact ? SP.card(LEVEL, n, true) : '';
  return [
  `<div class="p lh${pb ? ' pb' : ''}"><span class="lbadge">Lesson ${n}</span><span class="ltopic">${topic}</span>${chip}${tag ? `<span style="margin-left:${compact ? '3mm' : 'auto'};background:#FFC93C;color:#1B2A49;border-radius:999px;padding:4px 16px;font-weight:700;font-size:15px">${tag}</span>` : ''}</div>`,
  choose || !card ? `<div class="p ltitle">${title}</div>` : `<div class="p ltrow" style="display:flex;align-items:center;justify-content:space-between;gap:4mm;margin:4px 0 6px"><div class="ltitle" style="flex:1;min-width:0;margin:0 0 8px;${title.length > 15 ? 'font-size:29px;line-height:1.12' : ''}">${title}</div>${card}</div>`,
  `<div class="p namer"><b>Name</b><span></span><b>Group</b><span style="max-width:90px"></span><b>Date</b><span style="max-width:110px"></span></div>`,
  ...(choose ? [card] : [])
  ];
};

const QB = require('./qbank.json');
const FG = require('./figs_l1_3_l1.js');   // Level 1 figures (shared helper hp/figs_l1_3.js)
const NL = () => new TextRun('<br>');
const GAPS = require('./gaps.json');
const b64 = f => 'data:image/png;base64,' + fs.readFileSync(f).toString('base64');
const BOX = b64('gap_box.png'), FACE = [1, 2, 3].map(k => b64(`gap_face_${k}.png`));
const ib = (src, px) => `<img src="${src}" style="width:${px}px;height:${px}px;vertical-align:middle;margin:0 3px 0 6px">`;
const opt = (txt) => `<span style="white-space:nowrap">${ib(BOX, 19)}${esc2(txt)}</span>`;
const esc2 = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;');
const choice = () => `<div class="p" style="border:2px dashed #1F7A6F;border-radius:12px;background:#E8F5F2;padding:5px 12px;font-size:15.5px;line-height:1.3;margin:2px 0 8px">After question 3 you may choose: carry on, or try <b>Think harder</b>.</div>`;
const fast = choice;
const refl = (n) => [SP.lookback(LEVEL)];   // common look-back (three prompts, tool ticks, still stuck / pass); replaces the old five-row box
const invest = (n) => { const v = GAPS[String(n)].invest; return [banner('Investigation: ' + v.title), p(new TextRun('<i>Choose this any time you like. You do not have to finish it.</i>'), { before: 40, after: 40 }), p(new TextRun('<b>Easy first step:</b> ' + esc2(v.first)), { after: 40 }), p(new TextRun('<b>Then:</b> ' + esc2(v.q)), { after: 40 }), ...lines((v.lines || 4) + 2)]; };
const coreEnd = (n) => [p('', { pb: true, after: 0 }), p(t('Lesson ' + n + '  •  ' + L.lessons[n - 1].topic.toUpperCase() + '  •  Choose, then look back', { bold: true, size: 22, color: '666666' }), { after: 60 }), ...invest(n), gap(60), ...refl(n)];
const txp = (n) => (GAPS[String(n)].tx || []).flatMap(x => [q(x.label, x.q, { before: 60, after: 40, keepNext: true }), ...(n === 6 && x.label === 'T5' ? [FG.dollars()] : []), ...(x.subs || []).map(s => sub(s[0], s[1])), ...lines(1)]);
const extra = (n) => {
  const ls = L.lessons[n - 1], b = QB[String(n)];
  const out = [...hdr(n, ls.topic, 'Think harder', true, '')];
  const tight = (GAPS[String(n)].tx || []).length > 0 || Object.keys(FG.FX).some(k => k.startsWith(n + '.'));
  if (!tight) out.push(p(t('Use objects, draw a picture or make a table. Then write how you know. Choose any question you like, in any order.', { italics: true, size: 24 }), { after: 80, align: AlignmentType.CENTER }));
  out.push(banner('Think harder'));
  b.stretch.slice(0, 4).forEach((x, i) => { out.push(q('T' + (i + 1), x.q, { before: tight ? 60 : 140, after: 40, keepNext: true })); const fx = FG.FX[n + '.T' + (i + 1)]; if (fx) { const h = fx(); if (h) out.push(h); } out.push(...lines(fx ? (fx.lines === undefined ? 2 : fx.lines) : (GAPS[String(n)].tx || []).length ? 2 : 3)); });
  out.push(...txp(n));
  out.push(p('', { pb: true, after: 0 }));
  out.push(p(t('Lesson ' + n + '  •  ' + ls.topic.toUpperCase(), { bold: true, size: 22, color: '666666' }), { after: 60 }));
  out.push(banner('Go further'));
  b.challenge.slice(-3).forEach((x, i) => { out.push(q('C' + (i + 1), x.q, { before: 200, after: 40, keepNext: true })); if (x.img) out.push(img(x.img[0], x.img[1], x.img[2])); const fx = FG.FX[n + '.C' + (i + 1)]; if (fx) { const h = fx(); if (h) out.push(h); } out.push(...lines(x.img || fx ? 3 : 4)); });
  return out;
};
const stamps=L.lessons.map(ls=>`<div class="stamp"><div class="sn">Lesson ${ls.n}</div><div class="st">${ls.title}</div><div class="sc"></div></div>`).join('');
W.push(`<div class="cover"><svg viewBox="0 0 680 320" width="100%"><g transform="translate(70,70) rotate(-10)"><rect x="-40" y="-40" width="80" height="80" fill="#FFC93C" stroke="#1B2A49" stroke-width="3"/></g><g transform="translate(250,95) rotate(8)"><polygon points="0,-50 50,40 -50,40" fill="#7CC8F5" stroke="#1B2A49" stroke-width="3"/></g><g transform="translate(450,65) rotate(-6)"><rect x="-70" y="-30" width="140" height="60" fill="#3DBE7A" stroke="#1B2A49" stroke-width="3"/></g><g transform="translate(600,180) rotate(12)"><rect x="-40" y="-40" width="80" height="80" fill="#FF7A59" stroke="#1B2A49" stroke-width="3"/></g><g transform="translate(110,250) rotate(6)"><polygon points="0,-46 44,34 -44,34" fill="#FF7A59" stroke="#1B2A49" stroke-width="3"/></g><g transform="translate(360,250) rotate(-8)"><rect x="-60" y="-35" width="120" height="70" fill="#B9A6F2" stroke="#1B2A49" stroke-width="3"/></g></svg><div class="ccard"><span class="badge">PRIMARY 1 · HOLIDAY PROGRAM</span><div class="ctitle">Math<br><span>Inquirers</span></div><div class="cslogan">${SLOGAN}</div></div><div class="cname"><b>Name</b><i></i><b>Group</b><i style="max-width:120px"></i></div><div class="rules"><div class="rt">My Inquirer Rules</div><div class="rg"><div><b>1</b> Notice the pattern.</div><div><b>2</b> Test it with objects first.</div><div><b>3</b> Check your answer.</div><div><b>4</b> Explain why.</div></div></div></div>`);
W.push(`<div class="p pb jr"><div class="jt">My Inquiry Journal</div><div class="jsub">Your tutor stamps each lesson.</div><div class="sg">${stamps}</div><div class="p" style="margin-top:18px">Tutor: ______________________&nbsp;&nbsp;&nbsp; Program dates: ______________________</div></div>`);

/* ---------- LESSON 1 ---------- */
W.push(...hdr(1, 'Whole Numbers: Number Patterns', 'COUNT WITH THE FROG!')); W.push(fast());
W.push(p('Fill in the missing numbers. Your number strip is in the kit at the back.', { italics: true, after: 80 }));
W.push(q(1, 'Skip counting. Fill in the blanks.'));
W.push(sub('a', 'Counting in 2s:   2,  4,  6,  ____,  ____,  12,  ____,  16'));
W.push(sub('b', 'Counting in 5s:   5,  10,  ____,  20,  ____,  30,  ____'));
W.push(sub('c', 'Counting in 3s:   3,  6,  ____,  12,  ____,  18'));
W.push(q(2, 'What is the rule? Fill in the rule and the next two numbers.'));
W.push(sub('a', '4,  7,  10,  13,  ____,  ____        Rule: ______________'));
W.push(sub('b', '30,  27,  24,  21,  ____,  ____       Rule: ______________'));
W.push(sub('c', '2,  6,  10,  14,  ____,  ____        Rule: ______________'));
W.push(q(3, 'A frog starts at 0 and hops 4 steps each time. Circle or colour the numbers where the frog lands. The first hop is drawn for you.', { keepNext: true }));
W.push(FG.frogLines());
W.push(sub('a', 'A second frog also starts at 0 but hops 5 steps each time. Mark its landing numbers with a cross (X) on the second number line.'));
W.push(sub('b', 'Besides 0, which number do BOTH frogs land on?'));
W.push(ans());
W.push(q(4, 'Ali counts in 2s from 2 up to 30. Mei counts in 5s from 5 up to 30. Write both lists first.', { pb: true, before: 0 }));
W.push(sub('a', 'Which numbers will BOTH of them say?'));
W.push(ans());
W.push(sub('b', 'What do you notice about these numbers?'));
W.push(...lines(2));
W.push(q(5, 'Mei puts stickers in boxes. Box 1 has 2 stickers. Each box after it has 3 more stickers than the box before.', { keepNext: true }));
W.push(FG.stickerBoxes());
{ const ws = [CW - 8000, ...Array(10).fill(800)]; const vals = ['2', '5'];
  W.push(tbl(ws, [row([cell('Box', ws[0], { bold: true, fill: 'EDEDED' }), ...Array.from({ length: 10 }, (_, i) => cell(String(i + 1), 800, { bold: true, fill: 'EDEDED' }))]),
    row([cell('Stickers', ws[0], { bold: true }), ...Array.from({ length: 10 }, (_, i) => cell(vals[i] || '', 800, { h: 160 }))])])); }
W.push(gap(100));
W.push(sub('a', 'Fill in the table. How many stickers are in Box 10?'));
W.push(ans());
W.push(sub('b', 'Look at the numbers of stickers. Are they odd or even? What pattern do you see?'));
W.push(...lines(2));

/* ---------- LESSON 2 ---------- */
W.push(...coreEnd(1));
W.push(...extra(1));
W.push(...hdr(2, 'Whole Numbers: Number Bonds', 'NUMBER BOND INQUIRY')); W.push(fast());
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
W.push(q(4, 'The = sign means “is the same as”. Use counters or draw dots to make both sides the same. Fill in the blanks.', { pb: true, before: 0, keepNext: true }));
W.push(sub('a', '5 + 3 = 4 + ____            (b)  7 + ____ = 9 + 2'));
W.push(sub('c', '3 + 8 = ____ + 5            (d)  6 + 6 = 10 + ____'));
W.push(sub('e', 'Mei says “4 + 4 = 8 + 1 is true.” Is she right? Explain.'));
W.push(...lines(2));
W.push(q(5, 'Magic triangle. Put 1, 2, 3, 4, 5 and 6 in the circles so that each side adds up to 9. Start with 1, 2 and 3 in the corners.', { keepNext: true }));
W.push(p([t('Hint: use counters. Find the number between each pair of corners.', { italics: true })], { indent: { left: 560 }, after: 60 }));
W.push(img('magic.png', 230, 205));
W.push(sub('a', 'Which numbers go between the corners?   ______________'));
W.push(sub('b', 'If you have time: now make each side add up to 10. Which numbers are in the corners this time?   ______________'));
W.push(q(6, 'Two numbers add up to 10. One is 2 more than the other. What are the numbers?', { keepNext: true }));
W.push(FG.bars10());
W.push(ans('Answer:', 560));
W.push(p([t('If you have time: two numbers add up to 12. One is 4 more than the other. What are they?   ', { size: 24 }), t('___________', { size: 24 })], { indent: { left: 560 }, after: 100 }));

/* ---------- LESSON 3 ---------- */
W.push(...coreEnd(2));
W.push(...extra(2));
W.push(...hdr(3, 'Picture Graphs', 'LET’S PLAN THE FRUIT PARTY!')); W.push(fast());
W.push(p('Our teacher wants to buy fruit for a class party. Every child voted for ONE fruit. The picture graph shows the votes.', { after: 40 }));
W.push(FG.fruitGraph());
W.push(gap(20));
W.push(banner('Part A: Read the graph'));
W.push(q(1, 'Which fruit got the most votes?', { before: 140 })); W.push(ans());
W.push(q(2, 'Which fruit got the fewest votes?')); W.push(ans());
W.push(q(3, 'How many more children chose orange than grape?')); W.push(ans());
W.push(q(4, 'Two fruits got the same number of votes. Which two fruits are they?')); W.push(ans());
W.push(q(5, 'How many children voted altogether? (Hint: each child had only 1 vote.)')); W.push(ans());
W.push(q(6, [t('Mei says, “Orange is the best fruit for the whole school!”')], { before: 100 }));
W.push(sub('a', [t('Is Mei right?    '), t('Yes  /  No', { bold: true })]));
W.push(sub('b', 'Why do you think so?'));
W.push(...lines(1));
W.push(q(7, 'What else should the teacher think about before buying fruit for the party?'));
W.push(...lines(1));
W.push(gap(20));
W.push(banner('Part B: Now it’s your turn!'));
W.push(p('Ask your own group to vote. Each child votes for ONE fruit. Make a tally mark for each vote.', { before: 140, after: 100 }));
W.push(tbl([2400, 5700, 1800], [row([cell('Fruit', 2400, { bold: true, fill: 'D9D9D9' }), cell('Tally', 5700, { bold: true, fill: 'D9D9D9' }), cell('Total', 1800, { bold: true, fill: 'D9D9D9' })]), ...['Apple', 'Banana', 'Orange', 'Grape', 'Watermelon'].map(f => row([cell(f, 2400, { bold: true }), cell('', 5700, { h: 30 }), cell('', 1800, { h: 30 })]))]));
W.push(q(8, 'Which fruit did YOUR group like best?  ____________________    Is it the same as the graph above?  Yes / No', { before: 40 }));
W.push(q(9, 'Why might two groups choose different fruits?'));
W.push(...lines(1));

/* ---------- LESSON 4 ---------- */
W.push(...coreEnd(3));
W.push(...extra(3));
W.push(...hdr(4, 'Patterns', 'PATTERN INQUIRY')); W.push(fast());
W.push(q(1, 'Look at the shape pattern. Draw the missing shapes in places 8 and 9.', { before: 60 }));
W.push(FG.p1());
W.push(q(2, 'The pattern is circle, square, triangle, circle, square, triangle, circle … What is the 10th one? (Keep writing the pattern until you get there.)', { before: 100, keepNext: true }));
W.push(FG.p2());
W.push(q(3, 'The pattern is red, red, blue, red, red, blue, red … What is the 8th one?', { before: 100, keepNext: true }));
W.push(FG.p3());
W.push(q(4, 'Look at this pattern. It keeps going in the same way. You may draw in the empty boxes.', { keepNext: true }));
W.push(FG.p4());
W.push(sub('a', 'What shape will be in place 10?   ____________________'));
W.push(sub('b', 'What shape will be in place 12?   ____________________'));
W.push(sub('c', 'What shape will be in place 30? (Keep drawing, or look for a shortcut.)   ____________'));
W.push(sub('d', 'How do you know?'));
W.push(...lines(1));
W.push(q(5, 'The pattern is cat, dog, dog, cat, dog, dog, cat … What is the 12th one?', { before: 100, keepNext: true }));
W.push(FG.p5());
W.push(ans('Answer:', 560));
W.push(q(6, 'The pattern is A, B, C, D, A, B, C … What is the 11th one? (Write the letters in a row and number them.)', { before: 100, keepNext: true }));
W.push(FG.p6());
W.push(ans('Answer:', 560));
W.push(q(7, 'Ben makes a row of triangles with sticks.', { keepNext: true }));
W.push(img('sticks.png', 470, 96));
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
W.push(q(8, 'If you have time: Ben has 15 sticks. How many triangles in a row can he make?'));
W.push(ans('Answer:', 560));
W.push(p([t('Show how you worked it out:', { italics: true })], { indent: { left: 560 } }));
W.push(...lines(2));

/* ---------- LESSON 5 ---------- */
const mach = (cells) => { const ws = cells.map(c => c.w); return tbl(ws, [row(cells.map(c => cell(c.text, c.w, { fill: c.fill, bold: c.bold, h: 110, size: 26 })))]); };
W.push(...coreEnd(4));
W.push(...extra(4));
W.push(...hdr(5, 'Working Backwards', 'MYSTERY NUMBER')); W.push(fast());
W.push(p('Find each mystery number. Try a number and check it.', { italics: true, after: 80 }));
W.push(q(1, 'I think of a number. Find it and write it in the yellow box.', { keepNext: true }));
W.push(sub('a', 'I add 5. I get 12.', { after: 40, keepNext: true }));
W.push(mach([{ text: '?', w: 1700, fill: 'FFF2CC', bold: true }, { text: '→', w: 800 }, { text: '+ 5', w: 1700, fill: 'EDEDED' }, { text: '→', w: 800 }, { text: '12', w: 1700, fill: 'DDEBF7', bold: true }]));
W.push(gap(40));
W.push(sub('b', 'I take away 3. I get 9.', { after: 40, keepNext: true }));
W.push(mach([{ text: '?', w: 1700, fill: 'FFF2CC', bold: true }, { text: '→', w: 800 }, { text: '− 3', w: 1700, fill: 'EDEDED' }, { text: '→', w: 800 }, { text: '9', w: 1700, fill: 'DDEBF7', bold: true }]));
W.push(gap(40));
W.push(sub('c', 'I add 4. Then I take away 2. I get 10.', { after: 40, keepNext: true }));
W.push(mach([{ text: '?', w: 1300, fill: 'FFF2CC', bold: true }, { text: '→', w: 600 }, { text: '+ 4', w: 1300, fill: 'EDEDED' }, { text: '→', w: 600 }, { text: '− 2', w: 1300, fill: 'EDEDED' }, { text: '→', w: 600 }, { text: '10', w: 1300, fill: 'DDEBF7', bold: true }]));
W.push(q(2, 'A number machine adds the same number every time.', { keepNext: true }));
W.push(sub('a', 'It adds 6. Fill in the table.', { keepNext: true }));
W.push(tbl([1800, 1500, 1500, 1500, 1500], [row([cell('IN', 1800, { bold: true, fill: 'EDEDED' }), cell('2', 1500), cell('5', 1500), cell('9', 1500), cell('', 1500, { h: 140 })]), row([cell('OUT', 1800, { bold: true, fill: 'EDEDED' }), cell('8', 1500), cell('11', 1500), cell('', 1500, { h: 140 }), cell('14', 1500)])]));
W.push(gap(100));
W.push(sub('b', 'A different machine. What does it do?', { keepNext: true }));
W.push(tbl([1800, 1500, 1500, 1500, 1500], [row([cell('IN', 1800, { bold: true, fill: 'EDEDED' }), cell('3', 1500), cell('6', 1500), cell('10', 1500), cell('15', 1500)]), row([cell('OUT', 1800, { bold: true, fill: 'EDEDED' }), cell('7', 1500), cell('10', 1500), cell('14', 1500), cell('', 1500, { h: 140 })])]));
W.push(p([t('Rule: ______________     If you have time: OUT 30 means IN ______', { size: 26 })], { indent: { left: 1000 }, before: 100, after: 100 }));
W.push(q(3, 'Ali has 8 marbles. Mei has 5 more marbles than Ali.', { pb: true, before: 0 }));
W.push(sub('a', 'How many marbles does Mei have?   ____'));
W.push(p('Ben has 6 fewer marbles than Mei.', { indent: { left: 560 }, after: 80 }));
W.push(sub('b', 'How many marbles does Ben have?   ____'));
W.push(sub('c', 'How many more marbles does Mei have than Ben?   ____'));
W.push(sub('d', 'If you have time: how many marbles do they have altogether?   ____'));
W.push(p([t('Colour one box for each marble to help you. Ali’s bar is done for you.', { italics: true })], { indent: { left: 560 }, after: 60 }));
{ const ws = [1300, ...Array(14).fill(610)]; W.push(tbl(ws, ['Ali', 'Mei', 'Ben'].map(nm => row([cell(nm, ws[0], { bold: true, h: 110 }), ...Array.from({ length: 14 }, (_, i) => cell('', 610, { h: 110, fill: nm === 'Ali' && i < 8 ? 'D9D9D9' : undefined }))])))); }
W.push(gap(60));
W.push(q(4, 'Queue puzzles.', { keepNext: true }));
W.push(sub('a', 'There are 20 children in a queue. Mei is 7th from the front. How many children are behind her?', { keepNext: true }));
W.push(FG.queue20());
W.push(ans());
W.push(sub('b', 'Ali is 3rd from the front AND 3rd from the back. How many children are in the queue? Draw the children as circles first.'));
W.push(ans());
W.push(...lines(1));
W.push(q(5, [new C.TextRun('<svg aria-label="star" viewBox="0 0 24 24" width="20" height="20" style="vertical-align:-3px;margin-right:4px"><polygon points="12,1.5 15,8.6 22.5,9.2 16.8,14.1 18.6,21.5 12,17.6 5.4,21.5 7.2,14.1 1.5,9.2 9,8.6" fill="#FFC93C" stroke="#1B2A49" stroke-width="1.6" stroke-linejoin="round"/></svg><b>Take-home</b> '), t('(if you have time, or at home): make your own mystery number story. Give it to a friend to solve!')]));
W.push(...lines(3));

/* ---------- LESSON 6 ---------- */
W.push(...coreEnd(5));
W.push(...extra(5));
W.push(...hdr(6, 'Money', 'COIN COMBOS')); W.push(fast());
W.push(p('We have 5¢, 10¢, 20¢ and 50¢ coins. You can use the same kind of coin more than once.', { after: 100 }));
W.push(q(1, 'Show different ways to make exactly 20¢ using only 20¢, 10¢ and 5¢ coins. Write how many of each coin in the table.', { before: 100, keepNext: true }));
{ const ws = [2500, 2470, 2470, 2460];
  W.push(tbl(ws, [row(['Way', 'Number of 20¢', 'Number of 10¢', 'Number of 5¢'].map((s, i) => cell(i ? [FG.coinCell([0, 20, 10, 5][i], s)] : s, ws[i], { bold: true, fill: 'D9D9D9', size: 22, h: 10 }))), ...['A', 'B', 'C', 'D', 'E'].map(l => row([cell(l, ws[0], { bold: true, h: 30 }), cell('', ws[1], { h: 30 }), cell('', ws[2], { h: 30 }), cell('', ws[3], { h: 30 })]))])); }
W.push(p([t('You may not need every row.', { italics: true })], { indent: { left: 560 }, after: 20 }));
W.push(sub('a', 'Which way uses the FEWEST coins?   ____________'));
W.push(sub('b', 'Which way uses the MOST coins?   ____________'));
W.push(sub('c', 'How do you know you have found ALL the ways?'));
W.push(...lines(1));
W.push(q(2, 'Find ALL the ways to make 25¢ using 20¢, 10¢ and 5¢ coins. Start with the biggest coin. Write each way like this:  20¢ + 5¢   (Hint: there are 4 ways.)', { before: 120, keepNext: true }));
W.push(...lines(4));
W.push(q(3, 'Mei wants to pay exactly 85¢ using 5¢, 10¢, 20¢ and 50¢ coins.', { pb: true, before: 0, keepNext: true }));
W.push(FG.purse());
W.push(p([t('Tip: use play coins. Pay 85¢ any way you can, then try to use fewer coins.', { italics: true })], { indent: { left: 560 }, after: 60 }));
W.push(sub('a', 'What is the smallest number of coins she can use? Which coins are they?')); W.push(ans());
W.push(sub('b', 'If you have time: find a different way that uses exactly 6 coins.')); W.push(ans());
W.push(q(4, 'Can Ben make 35¢ using only 2 coins? Explain your answer.', { keepNext: true }));
W.push(FG.benTwo());
W.push(...lines(2));
W.push(q(5, 'Ali has a 20¢ coin, a 10¢ coin and a 5¢ coin. How much money does he have?', { keepNext: true }));
W.push(FG.coinsRow([20, 10, 5]));
W.push(ans('Answer:', 560));
W.push(q(6, 'Mei has two 20¢ coins and one 5¢ coin. How much money does she have?', { keepNext: true }));
W.push(FG.coinsRow([20, 20, 5]));
W.push(ans('Answer:', 560));

/* ---------- LESSON 7 ---------- */
W.push(...coreEnd(6));
W.push(...extra(6));
W.push(...hdr(7, 'Shapes', 'SHAPE SAFARI')); W.push(fast());
W.push(q(1, 'Count the shapes in the house picture.', { before: 40, keepNext: true }));
W.push(img('house.png', 270, 172));
W.push(tbl([2475, 2475, 2475, 2475], [row(['Circle', 'Triangle', 'Square', 'Rectangle'].map(s => cell(s, 2475, { bold: true, fill: 'EDEDED' }))), row(['', '', '', ''].map(s => cell(s, 2475, { h: 60 })))]));
W.push(sub('a', 'Which shape is there the most of?   ____________      (b)  How many shapes altogether?   ____'));
W.push(q(2, 'Sides and corners. Look at the shapes, then fill in the table.', { keepNext: true }));
W.push(img('shapes6.png', 380, 73));
{ const ws = [3300, 3300, 3300]; const rs = [['Circle', '0', '0'], ['Triangle', '3', '3'], ['Square', '', ''], ['Pentagon', '', ''], ['Hexagon', '', ''], ['Octagon', '', '']];
  W.push(tbl(ws, [row(['Shape', 'Straight sides', 'Corners'].map((s, i) => cell(s, ws[i], { bold: true, fill: 'EDEDED' }))), ...rs.map(r => row(r.map((s, i) => cell(s, ws[i], { h: 24, bold: i === 0, size: 22 }))))])); }
W.push(gap(60));
W.push(sub('a', 'What do you notice about the number of sides and corners?  ______________________'));
W.push(sub('b', 'A shape has 7 sides. How many corners does it have?   ____'));
W.push(q(3, 'Who am I?', { before: 40 }));
W.push(sub('a', 'I have 4 sides, all the same length, and 4 square corners.   ____________'));
W.push(sub('b', 'I have no corners and no straight sides.   ____________'));
W.push(sub('c', 'I have 6 sides.   ____________'));
W.push(q(4, 'How many triangles can you find in each picture? Count the small ones first, then the bigger ones.', { keepNext: true }));
W.push(img('trifigs_ab.png', 470, 165));
W.push(p([t('A: ____          B: ____', { bold: true })], { indent: { left: 1000 }, after: 100 }));
W.push(q(5, 'Two triangles of the same size are put together along one side. Draw one shape you can make. What is it called?'));
W.push(...lines(4));
W.push(p([t('Shape name: ____________________', { bold: true })], { indent: { left: 560 }, before: 120 }));
W.push(q(6, 'How many squares can you find in this picture? Count the small ones first, then the bigger one.', { keepNext: true }));
W.push(img('grid2x2.png', 220, 132));
W.push(ans('Number of squares:', 1000));

/* ---------- LESSON 8 ---------- */
W.push(...coreEnd(7));
W.push(...extra(7));
W.push(...hdr(8, 'Logic and Sorting', 'LOGIC LAB')); W.push(fast());
W.push(q(1, 'Put them in order using the clues.', { before: 40 }));
W.push(sub('a', 'Ali is taller than Ben. Ben is taller than Mei.   Tallest: ________   Shortest: ________'));
W.push(sub('b', 'The cat is heavier than the dog. The hen is lighter than the dog.   Heaviest: ________   Lightest: ________'));
W.push(sub('c', [t('The red ribbon is longer than the blue one.'), NL(), t('The green one is shorter than the blue one.'), NL(), t('The yellow one is longer than the red one.'), NL(), t('Write them from longest to shortest:')]));
W.push(p([t('______________,  ______________,  ______________,  ______________')], { indent: { left: 1000 }, after: 100 }));
W.push(q(2, 'Write 1 to 10 in the loops “Numbers less than 6” and “Odd numbers”.', { keepNext: true }));
W.push(`<div class="p kn" style="border:2px solid #1F7A6F;border-radius:10px;background:#E8F5F2;padding:6px 14px;margin:2px 0 8px;font-size:15.5px"><b>Odd</b> numbers end in 1, 3, 5, 7 or 9. <b>Even</b> numbers end in 0, 2, 4, 6 or 8.</div>`);
W.push(img('venn.png', 330, 183));
W.push(sub('a', 'Numbers in BOTH circles: ____________________'));
W.push(sub('b', 'Why are they in the middle?'));
W.push(...lines(2));
W.push(q(3, 'Who has which pet? Ali, Mei and Ben each have a different pet: cat, dog or fish.', { pb: true, before: 0 }));
W.push(p('Clue 1: Ali has no cat and no dog.', { indent: { left: 560 }, after: 40 }));
W.push(p('Clue 2: Mei does not have a dog.', { indent: { left: 560 }, after: 100 }));
W.push(p([t('Tick where it fits, cross where it cannot. Clue 1 is crossed for you.', { italics: true })], { indent: { left: 560 }, after: 80 }));
W.push(tbl([2400, 2300, 2300, 2300], [row(['', 'Cat', 'Dog', 'Fish'].map((s, i) => cell(s, i ? 2300 : 2400, { bold: true, fill: 'EDEDED' }))), ...['Ali', 'Mei', 'Ben'].map(n => row([cell(n, 2400, { bold: true, h: 150 }), cell(n === 'Ali' ? 'X' : '', 2300, { bold: true }), cell(n === 'Ali' ? 'X' : '', 2300, { bold: true }), cell('', 2300)]))]));
W.push(p([t('Ali has the ______.   Mei has the ______.   Ben has the ______.', { bold: true })], { indent: { left: 560 }, before: 120, after: 100 }));
W.push(q(4, 'Four children stand in a line: Ali, Ben, Mei and Sam.', { keepNext: true }));
W.push(p('Mei is first. Ali is in front of Ben. Ben is in front of Sam. Who stands where?', { indent: { left: 560 }, after: 80 }));
W.push(tbl([2475, 2475, 2475, 2475], [row(['1st', '2nd', '3rd', '4th'].map(s => cell(s, 2475, { bold: true, fill: 'EDEDED' }))), row(['', '', '', ''].map(s => cell(s, 2475, { h: 150 })))]));
W.push(q(5, 'If you have time: number riddle.', { before: 200, keepNext: true }));
W.push(sub('a', 'I am between 10 and 20. I am odd. You say me counting in 5s.   ____'));
W.push(q(6, 'If you have time: which one does NOT belong?   3,   6,   9,   11', { keepNext: true }));
W.push(p('Explain why. Find a second reason.', { indent: { left: 560 }, after: 40 }));
W.push(...lines(2));

/* ---------- LESSON 9 ---------- */
W.push(...coreEnd(8));
W.push(...extra(8));
W.push(...hdr(9, 'Length', 'MEASURE IT!')); W.push(fast());
W.push(q(1, 'Three ribbons are made of equal squares.', { before: 40, keepNext: true }));
W.push(img('ribbons.png', 400, 160));
W.push(sub('a', 'Which ribbon is the longest?   ____       (b)  Which is the shortest?   ____'));
W.push(sub('c', 'How many squares longer is ribbon A than ribbon B?   ____'));
W.push(sub('d', 'Ribbon A and ribbon B are put end to end. How many squares long is that?   ____'));
W.push(sub('e', 'Ribbon C is cut shorter by 2 squares. Which ribbon is it now the same length as?   ____'));
W.push(q(2, 'Write what you guessed, what you measured, and how far off your guess was. In the last row, guess first, then measure it with the cube strip from the back of the workbook.', { keepNext: true }));
W.push(tbl([2900, 1900, 1900, 3200], [row(['Object', 'My guess', 'Measured', 'How far off my guess was'].map((s, i) => cell(s, [2900, 1900, 1900, 3200][i], { bold: true, fill: 'EDEDED' }))), ...['A pencil', 'A book', 'A shoe', 'My choice: ____________'].map(n => row([cell(n, 2900, { h: 110, align: AlignmentType.LEFT }), cell('', 1900), cell('', 1900), cell('', 3200)]))]));
W.push(sub('a', 'Why must every cube be the same size?'));
W.push(...lines(1));
W.push(q(3, 'Ali’s desk is 6 spans long. Mei measures the same desk: 8 spans.', { pb: true, before: 0 }));
W.push(img('desk_spans.png', 440, 110));
W.push(sub('a', 'Whose span is longer?   ____________'));
W.push(sub('b', 'How do you know?'));
W.push(...lines(2));
W.push(q(4, 'If you have time: 1 clip = 2 erasers.', { keepNext: true }));
W.push(FG.clipEraser());
W.push(sub('a', 'A desk is 5 clips. How many erasers? (Draw it or count in 2s.)   ____'));
W.push(sub('b', 'A pencil is 12 erasers long. How many clips?   ____'));
W.push(q(5, 'Mei’s pencil is 8 cubes. Ali’s is 3 cubes longer. Ben’s is 2 cubes shorter.', { keepNext: true }));
W.push(FG.pencilCubes());
W.push(sub('a', 'How long is Ali’s pencil?   ____ cubes'));
W.push(sub('b', 'How long is Ben’s pencil?   ____ cubes'));
W.push(sub('c', 'All three end to end: ____ cubes?'));
W.push(q(6, 'Read the ruler.', { keepNext: true }));
W.push(FG.ruler6());
W.push(sub('a', 'The pencil goes from 0 to 12 cm. How long?   ____ cm'));
W.push(sub('b', 'The crayon goes from 3 to 8 cm. How long? (Hop from 3 to 8.)   ____ cm'));
W.push(sub('c', 'My pencil: ____ cm. Longer or shorter than 10 cm?   ________'));

/* ---------- LESSON 10 ---------- */
W.push(...coreEnd(9));
W.push(...extra(9));
W.push(...hdr(10, 'Mixed Puzzles', 'PUZZLE DAY!')); W.push(fast());
W.push(p([t('Show how you know. Remember the inquirer rules!', { italics: true })], { after: 60 }));
W.push(q(1, 'Pattern:   3,   8,   13,   18,   ____,   ____       Rule: ______________', { before: 40 }));
W.push(q(2, 'Two numbers add up to 12. One is 2 more than the other. What are they?  ___ and ___'));
W.push(q(3, 'The graph shows pets in a street.', { keepNext: true }));
W.push(FG.petGraph());
W.push(sub('a', 'How many more cats than birds?   ____      (b)  How many pets altogether?   ____'));
W.push(sub('c', 'Which two kinds of pet together make exactly 10?   ______________'));
W.push(q(4, 'You have one 20¢ coin, two 10¢ coins and two 5¢ coins.', { keepNext: true, before: 60 }));
W.push(FG.coinsRow([20, 10, 10, 5, 5]));
W.push(sub('a', 'How much money do you have?   ____      (b)  Which coins make exactly 35¢?   __________'));
W.push(q(5, 'Shapes', { keepNext: true, pb: true, before: 0 }));
W.push(sub('a', 'I have 4 sides, all the same length, and 4 square corners. What am I?   ____________'));
W.push(sub('b', 'How many triangles are in this picture?   ____', { keepNext: true }));
W.push(img('tri_one.png', 200, 137));
W.push(q(6, 'Ali is older than Ben. Mei is younger than Ben. Who is the youngest?   ____________'));
W.push(q(7, 'If you have time: I think of a number. I add 9, then take away 4. I get 10. What is it? (Try a number and check.)   ____'));
W.push(q(8, 'A pencil is 6 cubes long. A pen is 4 cubes longer than the pencil.', { keepNext: true }));
W.push(sub('a', 'How long is the pen?   ____ cubes'));
W.push(sub('b', 'Put the pen and the pencil end to end. How long are they together?   ____ cubes'));
W.push(q(9, 'Make a puzzle for a friend. Write the puzzle and the answer here. (We swap puzzles in talk time.)', { keepNext: true }));
W.push(...lines(4));
W.push(p([t('The puzzle I liked best today was ______________________ because ______________________', { size: 24 })], { before: 240, after: 100 }));

W.push(...coreEnd(10));
W.push(...extra(10));
/* ---------- APPENDIX: CUT-OUTS ---------- */
W.push('<div class="brk"></div>');
W.push(...require('./kit.js')());

/* ---------- LESSON 10 PUZZLE CARDS ---------- */
{
  const K = require('./kit.js').parts;
  const cards = L.lessons[9].cards;
  const card = (c, i) => `<div style="border:3px dashed #1B2A49;border-radius:14px;padding:26px 24px;min-height:260px;background:#FFFDF5"><div style="font-weight:800;font-size:22px;color:#1F7A6F;letter-spacing:1px;margin-bottom:14px">${i + 1}.&nbsp; ${c.title.toUpperCase()}</div><div style="font-size:22px;line-height:1.45;color:#1B2A49">${c.text.replace(/&/g, '&amp;').replace(/</g, '&lt;')}</div></div>`;
  W.push('<div class="brk"></div>');
  W.push(K.H('Puzzle cards', 'For Lesson 10 (Puzzle Day). Cut along the dashed lines. Choose a card to start with. You may swap with another pair later. Show how you know on a whiteboard or on paper.'));
  W.push(`<div class="p" style="display:grid;grid-template-columns:1fr 1fr;gap:22px;margin-top:10px">${cards.map(card).join('')}</div>`);
}

W.push(`<div class="cert pb"><div class="ci"><div class="ct">CERTIFICATE OF COMPLETION</div><div class="cp">${PROG}</div><div class="cs">Primary 1 Holiday Program</div><div class="cl">This certifies that</div><div class="cn"></div><div class="cl">completed all 10 lessons, solved puzzles, spotted patterns and explained their thinking.</div><div class="cq">${SLOGAN}</div><div class="cl">Tutor: ____________________ &nbsp;&nbsp;&nbsp; Date: ________________</div></div></div>`);
fs.writeFileSync('workbook_body.html', W.join('\n'));
console.log('html body built');
