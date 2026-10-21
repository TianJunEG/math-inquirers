// Math Inquirers P3 — Lesson 6: Fraction Walls (Fractions)
// Heuristics taught: draw a model (fraction wall / bar) and make the parts the same size (equivalent fractions).
// Every drawing below cuts a whole into EXACTLY equal parts (widths, angles or grid squares computed from the whole).
const NAVY = '#1B2A49', YEL = '#FFC93C', SKY = '#DDEBF7', TEAL = '#1F7A6F', WHITE = '#FFFFFF';
const FF = 'Fredoka, Arial, sans-serif';
const r1 = x => Math.round(x * 100) / 100;

// stacked fraction for the workbook text (raw HTML, used inside arrays so it is not escaped)
const fr = (n, d) => `<span style="display:inline-flex;flex-direction:column;align-items:center;vertical-align:middle;line-height:1.1;margin:0 3px;font-weight:600"><span style="padding:0 3px">${n}</span><span style="border-top:2px solid ${NAVY};padding:0 3px">${d}</span></span>`;
const BOX = `<span style="display:inline-block;width:24px;height:22px;border:2px solid ${NAVY};border-radius:4px;background:#fff;vertical-align:middle"></span>`;
const OV = `<span style="display:inline-block;width:30px;height:30px;border:2px solid ${NAVY};border-radius:50%;background:#fff;vertical-align:middle;margin:0 8px"></span>`;
const div = (s, st = '') => `<div style="text-align:left;font-size:18px;${st}">${s}</div>`;

// stacked fraction inside an SVG
const sfr = (x, y, n, d, size = 16, col = NAVY) =>
  `<text x="${r1(x)}" y="${r1(y - 3)}" font-size="${size}" font-weight="700" text-anchor="middle" fill="${col}" font-family="${FF}">${n}</text>` +
  `<line x1="${r1(x - size * 0.45)}" y1="${r1(y + 1)}" x2="${r1(x + size * 0.45)}" y2="${r1(y + 1)}" stroke="${col}" stroke-width="1.6"/>` +
  `<text x="${r1(x)}" y="${r1(y + size + 1)}" font-size="${size}" font-weight="700" text-anchor="middle" fill="${col}" font-family="${FF}">${d}</text>`;

// fraction wall: rows 1, 1/2, 1/3, 1/4, 1/6, 1/8, 1/12, each row split into equal parts
const wall = () => {
  const dens = [1, 2, 3, 4, 6, 8, 12], x0 = 10, W = 580, h = 46;
  let s = `<svg aria-label="Fraction wall: one whole, halves, thirds, quarters, sixths, eighths and twelfths" viewBox="0 0 600 ${dens.length * h + 4}" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:500px">`;
  dens.forEach((d, r) => {
    const y = 2 + r * h, w = W / d, fill = d === 1 ? YEL : (r % 2 ? SKY : WHITE);
    for (let i = 0; i < d; i++) {
      s += `<rect x="${r1(x0 + i * w)}" y="${y}" width="${r1(w)}" height="${h}" fill="${fill}" stroke="${NAVY}" stroke-width="2"/>`;
      if (d === 1) s += `<text x="${x0 + W / 2}" y="${y + 30}" font-size="20" font-weight="700" text-anchor="middle" fill="${NAVY}" font-family="${FF}">1 whole</text>`;
      else s += sfr(x0 + i * w + w / 2, y + 22, 1, d, 15);
    }
  });
  return s + '</svg>';
};

// Q2 shapes, all cut into equal parts
const shapes = () => {
  let s = `<svg aria-label="Five shapes A to E, each cut into equal parts with some parts shaded" viewBox="0 0 600 170" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:500px">`;
  const lab = (x, t) => `<text x="${x}" y="160" font-size="18" font-weight="700" text-anchor="middle" fill="${NAVY}" font-family="${FF}">${t}</text>`;
  // A: square with both diagonals: 4 equal triangles, top one shaded
  { const x = 10, y = 20, a = 100;
    s += `<polygon points="${x},${y} ${x + a},${y} ${x + a / 2},${y + a / 2}" fill="${YEL}"/>`;
    s += `<rect x="${x}" y="${y}" width="${a}" height="${a}" fill="none" stroke="${NAVY}" stroke-width="2.5"/><line x1="${x}" y1="${y}" x2="${x + a}" y2="${y + a}" stroke="${NAVY}" stroke-width="2"/><line x1="${x + a}" y1="${y}" x2="${x}" y2="${y + a}" stroke="${NAVY}" stroke-width="2"/>`;
    s += lab(x + a / 2, 'A'); }
  // B: rectangle cut into 8 equal strips, strips 2 and 6 shaded
  { const x = 128, y = 35, w = 112, h = 70, sw = w / 8;
    for (let i = 0; i < 8; i++) s += `<rect x="${r1(x + i * sw)}" y="${y}" width="${r1(sw)}" height="${h}" fill="${i === 1 || i === 5 ? YEL : WHITE}" stroke="${NAVY}" stroke-width="2"/>`;
    s += lab(x + w / 2, 'B'); }
  // C: circle cut into 6 equal sectors (60° each), 2 shaded
  { const cx = 310, cy = 70, R = 52;
    for (let i = 0; i < 6; i++) {
      const a0 = (i * 60 - 90) * Math.PI / 180, a1 = ((i + 1) * 60 - 90) * Math.PI / 180;
      s += `<path d="M${cx},${cy} L${r1(cx + R * Math.cos(a0))},${r1(cy + R * Math.sin(a0))} A${R},${R} 0 0 1 ${r1(cx + R * Math.cos(a1))},${r1(cy + R * Math.sin(a1))} Z" fill="${i === 0 || i === 1 ? YEL : WHITE}" stroke="${NAVY}" stroke-width="2"/>`;
    }
    s += lab(cx, 'C'); }
  // D: 4 by 3 grid of equal squares, 3 shaded (not next to each other)
  { const x = 375, y = 32, c = 25, on = ['0,0', '2,1', '1,2'];
    for (let r = 0; r < 3; r++) for (let k = 0; k < 4; k++) s += `<rect x="${x + k * c}" y="${y + r * c}" width="${c}" height="${c}" fill="${on.includes(k + ',' + r) ? YEL : WHITE}" stroke="${NAVY}" stroke-width="2"/>`;
    s += lab(x + 2 * c, 'D'); }
  // E: 4 by 2 grid of equal squares, 3 shaded
  { const x = 492, y = 45, c = 25, on = ['0,0', '1,0', '3,1'];
    for (let r = 0; r < 2; r++) for (let k = 0; k < 4; k++) s += `<rect x="${x + k * c}" y="${y + r * c}" width="${c}" height="${c}" fill="${on.includes(k + ',' + r) ? YEL : WHITE}" stroke="${NAVY}" stroke-width="2"/>`;
    s += lab(x + 2 * c, 'E'); }
  return s + '</svg>';
};

// Q6 partner cards
const cards = () => {
  const top = [[1, 4], [2, 3], [3, 8], [5, 12], [1, 6]], bot = [[7, 12], [6, 8], [5, 6], [5, 8], [4, 12]];
  let s = `<svg aria-label="Ten fraction cards in two rows" viewBox="0 0 600 220" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:440px">`;
  const card = (x, y, n, d, fill) => `<rect x="${x}" y="${y}" width="90" height="70" rx="10" fill="${fill}" stroke="${NAVY}" stroke-width="2.5"/>` + sfr(x + 45, y + 34, n, d, 22);
  top.forEach(([n, d], i) => { s += card(15 + i * 117, 8, n, d, YEL); });
  bot.forEach(([n, d], i) => { s += card(15 + i * 117, 142, n, d, SKY); });
  return s + '</svg>';
};

module.exports = {
  lesson: {
    n: 6, week: 3, session: 'B',
    title: 'Fraction Walls',
    topic: 'Fractions',
    objective: 'Use a fraction wall to find equivalent fractions, compare and order fractions by making the parts the same size, and add and subtract like and related fractions within one whole.',
    skills: 'Drawing a model (fraction wall, bar), equivalent fractions (multiply top and bottom by the same number), comparing with the same bottom number or the same top number, adding related fractions, finding all fractions between two fractions',
    materials: '7 paper strips per child, all the same length (24 cm works well), ruler, coloured pencils, scissors, mini whiteboards.',
    online: 'Children cut seven 24 cm strips from A4 paper before the lesson (or print the fraction strip page). Marks every 12, 8, 6, 4, 3 and 2 cm give halves, thirds, quarters, sixths, eighths and twelfths. Share the screen for the slides.',
    warmup: 'Fraction Flash: four shapes cut into equal parts appear on screen. Children write the fraction shaded on whiteboards, then click to check. Ask: “How do you know the parts are equal?”',
    explore: 'Pairs fold and mark paper strips into halves, quarters, eighths, thirds, sixths and twelfths, label every part and stack them into a fraction wall. They look for pieces that line up exactly (1/2 = 2/4 = 4/8 …) and test whether eighths can cover 1/3 exactly (they cannot).',
    mini: 'Every row of the wall is one whole cut into equal parts; more parts means smaller parts. Equal fractions line up on the wall: multiply the top and bottom by the same number. To compare or add, make the parts the same size first, then compare or add the top numbers only.',
    share: 'Why is 1/8 smaller than 1/6, even though 8 is bigger than 6?',
    exit: { q: 'Ali says 1/4 + 1/8 = 2/12. Is he right? Write the correct answer and show how you know.', a: 'No. 1/4 = 2/8, so 1/4 + 1/8 = 2/8 + 1/8 = 3/8. We add the parts, not the bottom numbers.' },
    mistakes: [
      'Adding the bottom numbers as well as the top numbers (1/3 + 1/3 = 2/6, or 1/4 + 1/8 = 2/12).',
      'Thinking 1/8 is bigger than 1/6 because 8 is bigger than 6.',
      'Comparing or adding fractions with different-sized parts without changing one first (1/4 + 3/8 = 4/8).'
    ],
    extension: 'How many different ways can you fill one whole bar using 1/2, 1/4 and 1/8 pieces, as many of each as you like? (9 ways. Work in order: two halves; one half with the other half made of quarters and eighths in 3 ways; no halves, with 4, 3, 2, 1 or 0 quarters filled up with eighths: 5 ways.)',
    key: [
      ['Q1', '(a) 2, 3, 4, 6: 1/2 = 2/4 = 3/6 = 4/8 = 6/12.  (b) 4, 8: 2/3 = 4/6 = 8/12.  (c) 6, 9: 3/4 = 6/8 = 9/12.  (d) The bottom number is always double the top number (the top and bottom are multiplied by the same number).'],
      ['Q2', '(a) >  (b) <  (c) =  (d) > (3/4 = 6/8)  (e) < (same top number; sevenths are bigger than ninths)  (f) < (2/3 = 8/12, 3/4 = 9/12)  (g) 1/3, 5/12, 1/2, 3/4 (4/12, 5/12, 6/12, 9/12).'],
      ['Q3', '(a) A, B and D (A: 1 of 4 equal parts; B: 2/8 = 1/4; D: 3/12 = 1/4).  (b) C: 2/6 (= 1/3) shaded.  E: 3/8 shaded.'],
      ['Q4', '(a) 5/7  (b) 2/8 + 3/8 = 5/8  (c) 4/12 + 5/12 = 9/12 (= 3/4)  (d) 5/6 − 2/6 = 3/6 (= 1/2)  (e) 10/10 − 3/10 = 7/10  (f) 5/10 + 3/10 = 8/10 (= 4/5).'],
      ['Q5', '(a) 1/6 + 4/6 = 5/6 of the fence.  (b) 1/6 is not painted.  (c) 4/6 − 1/6 = 3/6 = 1/2 of the fence more in the afternoon.'],
      ['Q6', '(a) 1/4 and 6/8;  2/3 and 4/12;  3/8 and 5/8;  5/12 and 7/12;  1/6 and 5/6.  (b) Any correct pair with different bottom numbers, e.g. 1/2 + 4/8, 1/3 + 8/12, 3/4 + 2/8, 2/5 + 6/10.'],
      ['Q7', '(a) 7/12 and 8/12 (1/2 = 6/12 and 3/4 = 9/12; the end fractions are not between).  (b) 8/12 = 2/3.']
    ]
  },

  script: {
    hook: ['Welcome, wall builders! Today we build a fraction wall and use it to spot fractions that look different but are the same amount, to decide which fraction is bigger, and to add fractions without falling into the bottom-number trap.'],
    warmIntro: ['Look at the shape. How many equal parts? How many are shaded? Write the fraction on your whiteboard.', 'How do you know the parts are equal? What would go wrong if they were not?'],
    predict: ['Which is bigger: one sixth of a strip or one eighth of the same strip? Write a guess before we fold.'],
    exploreHints: [
      'Stuck: fold the strip in half, then in half again, then again. How many parts now?',
      'For thirds: roll the strip into an S shape until the three parts are the same, or mark every 8 cm.',
      'Finished early: find three different pieces that together cover exactly one half.'
    ],
    think: [
      '“1/3 on the wall lines up with 2 sixths and with 4 twelfths. Same amount, different pieces: 1/3 = 2/6 = 4/12.”',
      '“From 1/3 to 2/6, the top and the bottom were both doubled. From 1/3 to 4/12, both times 4. So 2/5 = 4/10 without a wall.”',
      '“5/6 or 3/4? The parts are different sizes, so I change both to twelfths: 10/12 and 9/12. Now the parts match: 5/6 is bigger.”'
    ],
    circulate: [
      'Ask: “Are the parts the same size? How do you know?”',
      'Ask: “Which fraction did you change, and what did you multiply by?”',
      'Ask: “You added the bottom numbers. Show me on the bar: did the pieces change size?”'
    ],
    hints: [
      'Hint 1: “Find both fractions on the wall. Which one reaches further?”',
      'Hint 2: “Change one fraction so both have the same bottom number.”',
      'Hint 3: “Draw a bar and cut it into the smaller pieces.”'
    ],
    talk: ['“Why is 1/8 smaller than 1/6, even though 8 is bigger than 6?”', '“Why is 1/3 + 1/3 not 2/6?”'],
    talkAns: 'The same whole is cut into more pieces, so each eighth is smaller than each sixth. 1/3 + 1/3 is two thirds: the pieces are still thirds, so we add only the top numbers (2/6 is just 1/3).',
    close: ['“Today you made the parts the same size before you compared or added. Inquirers check that a comparison is fair.”']
  },

  deck: {
    today: 'Build a fraction wall, find equal fractions, compare fractions by making the parts the same size, and add related fractions.',
    warmGame: 'Fraction Flash. Four shapes cut into equal parts appear on screen (eighths of a circle, sixths of a rectangle, sixths of a hexagon, tenths of a bar). Children write the fraction shaded, then click to check.',
    warmQs: [['How many quarters make one whole?', '4'], ['Which is bigger: 1/3 or 1/5?', '1/3'], ['1/2 = ?/10', '5'], ['2/9 + 4/9', '6/9'], ['1 − 2/5', '3/5']],
    expSetup: ['Take 7 paper strips, all the same length.', 'Keep one whole. Fold or mark the others into 2, 4, 8, 3, 6 and 12 equal parts.', 'Label every part and stack the strips into a wall.', 'Ask: which pieces line up exactly?'],
    expPic: 'A small fraction wall: one whole, halves, quarters and eighths, all with equal parts and a dashed line at one half.',
    expAsk: [
      ['How many 1/8 pieces fit exactly on 1/2?', '4 (1/2 = 4/8).'],
      ['Which is bigger, 1/6 or 1/8? Why?', '1/6: the whole is cut into fewer parts, so each part is bigger.'],
      ['Can eighths cover 1/3 exactly?', 'No. 2 eighths are too small and 3 eighths are too big. Sixths and twelfths can (2/6, 4/12).']
    ],
    mini1: { head: 'Equal fractions on the wall: 1/3', body: ['1/3 lines up with 2 sixths and with 4 twelfths.', 'Top and bottom are multiplied by the same number (× 2, × 4).', 'So 2/5 = 4/10 without a wall.'], ans: '1/3 = 2/6 = 4/12.' },
    mini2: { head: 'Which is bigger: 5/6 or 3/4?', body: ['Different-sized parts, so make them the same.', '5/6 = 10/12 and 3/4 = 9/12.', 'Now compare the top numbers.'], ans: '5/6 is bigger (10/12 > 9/12).' },
    keyHead: 'Key idea: make the parts the same size',
    keyBig: 'To compare or add fractions, the parts must be the same size. Use the wall, or change one fraction to an equal fraction with the same bottom number.',
    keySmall: 'When we add, we add the top numbers. The bottom number (the size of the parts) stays the same.',
    brk: 'Fraction turns. The tutor calls a turn: “a quarter turn!”, “a half turn!”, “three quarters of a turn!”, “two quarters!” Children turn on the spot and freeze. Which calls make the same turn?',
    ws1: 'Page 1, in pairs: Q1 the fraction wall and equal fractions, Q2 compare and order.',
    ws2: 'Page 2, on your own: Q3 which shapes show one quarter, Q4 add and subtract, Q5 Ravi paints a fence, Q6 partners that make one whole, Q7 all the twelfths between one half and three quarters.'
  },

  qbank: {
    core: [
      { q: 'Fill in the box: 1/2 = ?/10', a: '5 (1/2 = 5/10)' },
      { q: 'Which is bigger: 1/6 or 1/9?', a: '1/6 (sixths are bigger pieces than ninths)' },
      { q: 'Work out 2/9 + 5/9.', a: '7/9' },
      { q: 'Work out 1 − 3/8.', a: '5/8 (8/8 − 3/8)' },
      { q: 'Put these in order, smallest first: 5/12, 1/12, 11/12.', a: '1/12, 5/12, 11/12' },
      { q: 'Fill in the box: 2/5 = ?/10', a: '4 (2/5 = 4/10)' }
    ],
    stretch: [
      { q: 'Which is bigger, 3/5 or 7/10? Show how you know.', a: '7/10 (3/5 = 6/10, and 7/10 is bigger than 6/10)' },
      { q: 'Siti reads 1/4 of a book on Monday and 1/2 of the book on Tuesday. What fraction of the book has she read? What fraction is left?', a: 'She has read 3/4 (1/4 + 2/4). 1/4 is left.' },
      { q: 'Put these in order, smallest first: 2/3, 5/6, 7/12.', a: '7/12, 2/3, 5/6 (7/12, 8/12, 10/12)' },
      { q: 'Write two fractions equal to 4/6: one with a smaller bottom number and one with a bigger bottom number.', a: '2/3 and 8/12' },
      { q: 'A jug is 5/6 full of water. Ravi pours out 1/2 of the whole jug. What fraction of the jug is still full?', a: '1/3 (5/6 − 3/6 = 2/6 = 1/3)' },
      { q: 'Which fraction with bottom number 8 is exactly halfway between 1/4 and 1/2?', a: '3/8 (1/4 = 2/8 and 1/2 = 4/8)' },
      { q: 'Work out 1/2 + 1/4 + 1/8.', a: '7/8 (4/8 + 2/8 + 1/8)' },
      { q: 'Mei says 2/3 is bigger than 3/4, because 2/3 is missing only one piece. Is she right? Explain.', a: 'No. Both are missing one piece, but 2/3 is missing 1/3 and 3/4 is missing only 1/4, a smaller piece. So 3/4 is bigger (8/12 < 9/12).' }
    ],
    challenge: [
      { q: 'Which is bigger, 3/7 or 5/9? Use 1/2 to help you.', a: '5/9. 3/7 is less than 1/2 (half of 7 is 3 and a half) and 5/9 is more than 1/2 (half of 9 is 4 and a half).' },
      { q: 'Which is bigger, 2/5 or 4/9? Hint: make the top numbers the same.', a: '4/9. 2/5 = 4/10, and ninths are bigger pieces than tenths, so 4/9 > 4/10.' },
      { q: 'Use the digits 1, 2, 3 and 6, once each, to make two equal fractions: ?/? = ?/?. Find both ways.', a: '1/2 = 3/6 and 1/3 = 2/6' },
      { q: 'A ribbon is cut into equal pieces. Ali takes 1/3 of the ribbon and Ben takes 1/6 of it. Mei takes the rest. Who has the most ribbon?', a: 'Mei. Ali 2/6, Ben 1/6, Mei 6/6 − 3/6 = 3/6 = 1/2.' },
      { q: 'Find all the fractions with bottom number 12 that are bigger than 2/3 but smaller than 1.', a: '9/12, 10/12 and 11/12 (2/3 = 8/12)' },
      { q: 'I am a fraction equal to 3/4. My top number and my bottom number add up to 14. What fraction am I?', a: '6/8 (3 + 4 = 7, and 14 is double 7, so double the top and the bottom)' },
      { q: 'A fraction is equal to 2/3. Its bottom number is 4 more than its top number. What is the fraction?', a: '8/12 (in 2/3 the bottom is 1 more than the top; 4 times as much: 8/12)' },
      { q: 'Fill one whole bar using exactly 5 pieces. You may use 1/2, 1/4 and 1/8 pieces, as many of each as you like. Find all the ways.', a: '2 ways: 1/2 + 1/8 + 1/8 + 1/8 + 1/8, and 1/4 + 1/4 + 1/4 + 1/8 + 1/8.' },
      { q: 'Siti and Ravi each have the same size bottle of juice. Siti drinks 2/3 of her bottle. Ravi drinks 7/12 of his. Who drinks more? How much more?', a: 'Siti, by 1/12 of a bottle (2/3 = 8/12, and 8/12 − 7/12 = 1/12).' }
    ]
  },

  workbook: H => {
    const W = [];
    W.push(H.p('Each row of a fraction wall is one whole, cut into EQUAL parts. To compare or add fractions, make the parts the same size.', { after: 80 }));
    W.push(H.q(1, 'Use the fraction wall.', { before: 80, keepNext: true, after: 40 }));
    W.push(H.fig(wall()));
    W.push(H.sub('a', [fr(1, 2), ' = ', fr(BOX, 4), ' = ', fr(BOX, 6), ' = ', fr(BOX, 8), ' = ', fr(BOX, 12)], { after: 60 }));
    W.push(H.sub('b', [fr(2, 3), ' = ', fr(BOX, 6), ' = ', fr(BOX, 12), '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(c)&nbsp;&nbsp;', fr(3, 4), ' = ', fr(BOX, 8), ' = ', fr(BOX, 12)], { after: 60 }));
    W.push(H.sub('d', 'Look at your answers to (a). What do you notice about the top and bottom numbers?', { keepNext: true, after: 0 }));
    W.push(...H.lines(1));
    W.push(H.q(2, ['Write ', '&gt;', ', ', '&lt;', ' or = in each circle.'], { keepNext: true }));
    const cw = [3300, 3300, 3300];
    const cmp = (l, a, b) => H.cell([div(`(${l})&nbsp;&nbsp;${fr(...a)}${OV}${fr(...b)}`, 'font-size:20px')], 3300, { h: 110 });
    W.push(H.tbl(cw, [
      H.row([cmp('a', [1, 5], [1, 7]), cmp('b', [3, 8], [5, 8]), cmp('c', [2, 3], [4, 6])]),
      H.row([cmp('d', [3, 4], [5, 8]), cmp('e', [4, 9], [4, 7]), cmp('f', [2, 3], [3, 4])])
    ]));
    W.push(H.sub('g', ['Put in order, smallest first:&nbsp;&nbsp;', fr(5, 12), ',&nbsp;&nbsp;', fr(1, 2), ',&nbsp;&nbsp;', fr(1, 3), ',&nbsp;&nbsp;', fr(3, 4)], { keepNext: true }));
    W.push(H.ans('Smallest first:'));

    W.push(H.q(3, 'Each shape is cut into equal parts.', { pb: true, before: 0, keepNext: true, after: 20 }));
    W.push(H.fig(shapes()));
    W.push(H.sub('a', ['Which shapes have exactly ', fr(1, 4), ' shaded?   ________']));
    W.push(H.sub('b', 'For each of the other shapes, write the fraction that is shaded.   ________________'));
    W.push(H.q(4, 'Add or subtract. Make the parts the same size first.', { keepNext: true }));
    const sum = (l, a, op, b) => H.cell([div(`(${l})&nbsp;&nbsp;${typeof a === 'number' ? a : fr(...a)}&nbsp;${op}&nbsp;${fr(...b)}&nbsp;=&nbsp;________`, 'font-size:20px'), '<div style="height:26px"></div>'], 3300, { h: 70 });
    W.push(H.tbl(cw, [
      H.row([sum('a', [2, 7], '+', [3, 7]), sum('b', [1, 4], '+', [3, 8]), sum('c', [1, 3], '+', [5, 12])]),
      H.row([sum('d', [5, 6], '−', [1, 3]), sum('e', 1, '−', [3, 10]), sum('f', [1, 2], '+', [3, 10])])
    ]));
    W.push(H.q(5, ['Ravi paints ', fr(1, 6), ' of a fence in the morning and ', fr(2, 3), ' of the same fence in the afternoon. Draw a bar to help you.'], { keepNext: true }));
    W.push(H.sub('a', 'What fraction of the fence has he painted?   ________'));
    W.push(H.sub('b', 'What fraction of the fence is not painted yet?   ________'));
    W.push(H.sub('c', 'How much more of the fence did he paint in the afternoon than in the morning?   ________', { keepNext: true }));
    W.push(...H.lines(1));
    W.push(H.q(6, 'Partners that make ONE WHOLE.', { keepNext: true }));
    W.push(H.sub('a', 'Join each yellow card to the blue card that makes one whole with it.', { keepNext: true, after: 20 }));
    W.push(H.fig(cards()));
    W.push(H.sub('b', 'Write one more pair of fractions with different bottom numbers that make one whole.   ________________'));
    W.push(H.q(7, 'Fractions in between.', { keepNext: true }));
    W.push(H.sub('a', ['Find ALL the fractions with bottom number 12 that are bigger than ', fr(1, 2), ' but smaller than ', fr(3, 4), '.'], { keepNext: true }));
    W.push(H.ans());
    W.push(H.sub('b', ['Which one of your fractions is equal to ', fr(2, 3), '?   ________']));
    return W;
  }
};
