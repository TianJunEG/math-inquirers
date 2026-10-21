// Math Inquirers P3, Lesson 2: Cryptarithm Crackers (Addition and subtraction)
// Heuristics taught: work backwards (undo with the opposite operation); guess and check (then improve).
const N = '#1B2A49', Y = '#FFC93C', SKY = '#DDEBF7', T = '#1F7A6F', R = '#D64545', W = '#FFFFFF';
const F = 'font-family="Fredoka, Arial"';

// shapes used in the shape puzzles: S star, C circle, T triangle
const shape = (k, cx, cy, r) => {
  if (k === 'C') return `<circle cx="${cx}" cy="${cy}" r="${r * 0.8}" fill="${T}" stroke="${N}" stroke-width="3"/>`;
  if (k === 'T') return `<polygon points="${cx},${cy - r} ${cx + r * 0.95},${cy + r * 0.75} ${cx - r * 0.95},${cy + r * 0.75}" fill="${R}" stroke="${N}" stroke-width="3" stroke-linejoin="round"/>`;
  let pts = []; for (let i = 0; i < 10; i++) { const a = Math.PI / 5 * i - Math.PI / 2, rr = i % 2 ? r * 0.42 : r; pts.push((cx + rr * Math.cos(a)).toFixed(1) + ',' + (cy + rr * Math.sin(a)).toFixed(1)); }
  return `<polygon points="${pts.join(' ')}" fill="${Y}" stroke="${N}" stroke-width="3" stroke-linejoin="round"/>`;
};
// a column sum: rows are strings, right-aligned; '?' = empty box, S/C/T = shapes, digits as text
const colsum = (rows, op, x0, y0, cw = 40, rh = 46, label = '') => {
  const cols = Math.max(...rows.map(r => r.length)); let s = '';
  if (label) s += `<text x="${x0 - 40}" y="${y0 + 26}" font-size="22" font-weight="700" fill="${T}" ${F}>${label}</text>`;
  rows.forEach((r, i) => {
    const last = i === rows.length - 1, y = y0 + i * rh + (last ? 18 : 0);
    [...r.padStart(cols)].forEach((ch, j) => {
      const x = x0 + j * cw;
      if (ch === '?') s += `<rect x="${x + 3}" y="${y}" width="${cw - 6}" height="${rh - 8}" rx="6" fill="${W}" stroke="${N}" stroke-width="2.5"/>`;
      else if ('SCT'.includes(ch)) s += shape(ch, x + cw / 2, y + (rh - 8) / 2, (rh - 8) / 2 - 1);
      else if (ch !== ' ') s += `<text x="${x + cw / 2}" y="${y + rh - 16}" font-size="30" font-weight="600" text-anchor="middle" fill="${N}" ${F}>${ch}</text>`;
    });
    if (i === rows.length - 2) s += `<text x="${x0 - 18}" y="${y + rh - 16}" font-size="32" font-weight="700" text-anchor="middle" fill="${N}" ${F}>${op}</text><line x1="${x0 - 34}" y1="${y + rh + 1}" x2="${x0 + cols * cw}" y2="${y + rh + 1}" stroke="${N}" stroke-width="3"/>`;
  });
  return s;
};
// a shape sum written along one line, e.g. 'SC+SC=TSC'
const shapeLine = str => {
  const cw = 40, x0 = 300 - str.length * cw / 2; let s = '';
  [...str].forEach((ch, i) => { const x = x0 + i * cw + cw / 2; s += 'SCT'.includes(ch) ? shape(ch, x, 32, 17) : `<text x="${x}" y="44" font-size="34" font-weight="700" text-anchor="middle" fill="${N}" ${F}>${ch}</text>`; });
  return s;
};
const svg = (label, h, inner, maxw = 600, vbw = 600) => `<svg aria-label="${label}" viewBox="0 0 ${vbw} ${h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:${maxw}px">${inner}</svg>`;
const cardsSvg = ds => {
  const w = 62, g = 12, tot = ds.length * w + (ds.length - 1) * g, x0 = (600 - tot) / 2; let s = '';
  ds.forEach((d, i) => { const x = x0 + i * (w + g); s += `<rect x="${x}" y="4" width="${w}" height="76" rx="10" fill="${Y}" stroke="${N}" stroke-width="3"/><text x="${x + w / 2}" y="58" font-size="42" font-weight="700" text-anchor="middle" fill="${N}" ${F}>${d}</text>`; });
  return svg('Digit cards ' + ds.join(', '), 84, s, 380);
};
const magicSvg = vals => {
  const c = 48, x0 = 4; let s = '';
  vals.forEach((v, i) => { const x = x0 + (i % 3) * c, y = 4 + Math.floor(i / 3) * c; s += `<rect x="${x}" y="${y}" width="${c}" height="${c}" fill="${v ? SKY : W}" stroke="${N}" stroke-width="3"/>` + (v ? `<text x="${x + c / 2}" y="${y + c / 2 + 6}" font-size="17" font-weight="600" text-anchor="middle" fill="${N}" ${F}>${v}</text>` : ''); });
  return svg('Magic square with some numbers missing', 3 * c + 8, s, 3 * c + 8, 3 * c + 8);
};
const pyramid = (x0, vals, label) => { // vals: [top, midL, midR, botL, botM, botR]
  const bw = 84, bh = 40; const pos = [[x0 + bw, 30], [x0 + bw / 2, 30 + bh], [x0 + 1.5 * bw, 30 + bh], [x0, 30 + 2 * bh], [x0 + bw, 30 + 2 * bh], [x0 + 2 * bw, 30 + 2 * bh]];
  let s = `<text x="${x0}" y="20" font-size="20" font-weight="700" fill="${T}" ${F}>${label}</text>`;
  pos.forEach(([x, y], i) => { const v = vals[i]; s += `<rect x="${x}" y="${y}" width="${bw}" height="${bh}" fill="${v ? SKY : W}" stroke="${N}" stroke-width="2.5"/>` + (v ? `<text x="${x + bw / 2}" y="${y + 28}" font-size="22" font-weight="600" text-anchor="middle" fill="${N}" ${F}>${v}</text>` : ''); });
  return s;
};

module.exports = {
  lesson: {
    n: 2, week: 1, session: 'B',
    title: 'Cryptarithm Crackers',
    topic: 'Addition and Subtraction',
    objective: 'Find missing digits in 4-digit addition and subtraction by working column by column from the ones, check subtraction by adding, work backwards in magic squares and number pyramids, and use guess, check and improve for digit-card and shape puzzles.',
    skills: 'Column addition and subtraction with regrouping, using the opposite operation (work backwards), guess and check then improve, reasoning about carrying, explaining "this is the only answer"',
    materials: 'Digit cards 0–9 (one set per child), mini whiteboards, a printed 3 × 3 grid, counters or small paper squares to move around.',
    online: 'Children use the cut-out digit cards at the back of the workbook (or paper squares numbered 0–9) and draw the grids on paper. Share the screen for the column sums and write on them.',
    warmup: 'Make 1000: the tutor shows a number (350, 720, 105, 999, 460, 75); children write the number that makes 1000 with it.',
    explore: 'Pairs use the digit cards 1 to 9, each once, to make a sum: 3-digit number + 3-digit number = 3-digit number. They find as many as they can and look for what is always true.',
    mini: 'Missing digits: start at the ones column, write the carry, then move left. Subtraction: turn it into an addition to check. Digit-card puzzles: guess, check, then improve the guess.',
    share: 'Why do we always start a missing-digit puzzle at the ones column?',
    exit: { q: 'Find the missing digits:  3□82 + 14□9 = 5141', a: '3682 + 1459 = 5141. The missing digits are 6 and 5.' },
    mistakes: [
      'Forgetting the carried 1 when working out the missing digit in the next column.',
      'In subtraction, looking for a digit with 3 − □ = 8 (there is none) instead of regrouping: 13 − 5 = 8.',
      'Magic squares: guessing numbers instead of finding a full line first to get the total.'
    ],
    extension: 'Find three different sums □□□ + □□□ = □□□ that use the digits 1 to 9 once each. Add the digits of each answer. What do you notice? (They always add up to 18, e.g. 173 + 286 = 459 and 218 + 349 = 567.)',
    key: [
      ['Q1', '(a) 3447 + 2578 = 6025  (b) 7003 − 4465 = 2538'],
      ['Q2', '(a) 1173, e.g. 642 + 531  (b) 381, e.g. 135 + 246  (c) 47: 412 − 365 (the only way)'],
      ['Q3', '(a) Magic total 4500. Middle row 1900, 1500, 1100. Bottom row 1400, 1300, 1800.  (b) Numbers opposite each other across the centre add up to 3000 (e.g. 1200 + 1800, 1700 + 1300).'],
      ['Q4', '(a) Middle row 2375, 3600. Bottom row 1250, 1125, 2475.  (b) Both corner bricks are 1500 (middle row 3500, 3500).'],
      ['Q5', '(a) 5872 and 7406  (b) The two digits in each place add up to 9, so there is never a carry.  (c) 5873 (one more than 9999 − 4127 = 5872)'],
      ['Q6', '★ = 5, ● = 0, ▲ = 1:  50 + 50 + 50 = 150']
    ]
  },

  script: {
    hook: ['Welcome, Cryptarithm Crackers! Some digits in today’s sums have gone missing, and some have been turned into shapes. Like code-breakers, we will crack them one column at a time and prove our answer is the only one.'],
    warmIntro: ['I show you a number. You write the number that makes 1000 with it. Ready? 350.', 'How did you work it out? Did anyone go to 400 first, then to 1000?'],
    predict: ['Can you use the digits 1 to 9, each once, to make a sum like □□□ + □□□ = □□□? Do you think there are many ways, a few, or none?'],
    exploreHints: [
      'Stuck: “Put small digits in the hundreds of the two numbers you add. Try 1 and 2.”',
      'Close but a digit repeats: “Swap two cards in the ones column and add again.”',
      'Finished early: “Add up the digits of your answer. Does a friend’s answer give the same total?”'
    ],
    think: [
      '“4□68 + 17□5 = □043. I start at the ones: 8 + 5 = 13. I write 3 and carry 1.”',
      '“Tens: 6 + □ + the carried 1 must end in 4. 6 + 7 + 1 = 14. So the box is 7, and I carry 1 again.”',
      '“Hundreds: □ + 7 + 1 must end in 0, so it makes 10. □ is 2. Thousands: 4 + 1 + 1 = 6. So 4268 + 1775 = 6043. I check by adding it all again.”',
      '“For subtraction I turn it round: 6□02 − □35□ = 1947 means 1947 + □35□ = 6□02. Now I can add, column by column.”'
    ],
    circulate: ['Ask: “Which column did you start with? Why?”', 'Ask: “Is there a carry coming into this column?”', 'Ask: “How do you know this is the ONLY answer?”'],
    hints: ['Hint 1: “Start at the ones column.”', 'Hint 2: “Write the carried 1 above the next column.”', 'Hint 3: “For subtraction, check by adding.”'],
    talk: ['“Why do we start at the ones column?”', '“How can a puzzle have only one answer?”'],
    talkAns: 'A carry moves from right to left, so the ones column is the only column with nothing coming into it. Once we know the ones, we know the carry, and then the next column has only one possible digit, and so on.',
    close: ['“Code-breakers check every column. Today you worked backwards, guessed and improved, and proved your answers.”']
  },

  deck: {
    today: 'Crack missing digits one column at a time, check subtraction by adding, and solve magic squares and shape puzzles.',
    warmGame: 'Make 1000. The tutor shows a number; children write the number that makes 1000 with it: 350, 720, 105, 999, 460, 75.',
    warmQs: [['3456 + 1000 = ?', '4456'], ['5000 − 1 = ?', '4999'], ['2700 + 300 = ?', '3000'], ['8000 − 2500 = ?', '5500'], ['4999 + 2 = ?', '5001']],
    expSetup: ['Take the digit cards 1 to 9.', 'Make □□□ + □□□ = □□□ using every card once.', 'Check the sum by adding.', 'Find more. What is always true?'],
    expPic: 'nine digit cards 1 to 9 above an empty column sum: three boxes plus three boxes equals three boxes.',
    expAsk: [
      ['How many sums did you find?', 'There are many: 168 if 173 + 286 and 286 + 173 count once. For example 173 + 286 = 459 and 218 + 349 = 567.'],
      ['How many times did you carry?', 'Exactly once in every sum.'],
      ['Add the digits of your answer. What do you notice?', 'They always add up to 18 (4 + 5 + 9, 5 + 6 + 7).']
    ],
    mini1: { head: 'Missing digits: 4□68 + 17□5 = □043', body: ['Ones: 8 + 5 = 13, write 3, carry 1.', 'Tens: 6 + □ + 1 = 14, so □ = 7, carry 1.', 'Hundreds: □ + 7 + 1 = 10, so □ = 2, carry 1.', 'Thousands: 4 + 1 + 1 = 6.'], ans: '4268 + 1775 = 6043.' },
    mini2: { head: 'Check by adding: 6□02 − □35□ = 1947', body: ['Turn it round: 1947 + □35□ = 6□02.', 'Ones: 7 + □ ends in 2, so □ = 5 (12), carry 1.', 'Tens: 4 + 5 + 1 = 10, carry 1. Hundreds: 9 + 3 + 1 = 13, so the top box is 3, carry 1.', 'Thousands: 1 + □ + 1 = 6, so □ = 4.'], ans: '6302 − 4355 = 1947.' },
    keyHead: 'Key idea: one column at a time',
    keyBig: 'Start at the ones and carry to the left. Check subtraction by adding. Stuck? Guess, check, then improve.',
    keySmall: 'A puzzle is cracked when you can say why it is the ONLY answer.',
    brk: 'Code-breaker moves. Tutor says a digit: odd means hop on one foot that many times, even means clap that many times. Then 0: freeze!',
    ws1: 'Page 1, in pairs: Q1 missing digits; Q2 digit cards 1 to 6.',
    ws2: 'Page 2, on your own: Q3 magic square; Q4 number pyramids; Q5 the 9999 pattern; Q6 shape puzzle.'
  },

  qbank: {
    core: [
      { q: 'Work out 3999 + 2456. Use a shortcut.', a: '6455 (add 4000 to get 6456, then take away 1)' },
      { q: '7000 − 2468 = ?', a: '4532' },
      { q: 'Find the missing digit:  4□27 + 1365 = 5992', a: '6 (4627 + 1365 = 5992)' },
      { q: 'Find the missing digit:  8□50 − 3420 = 5230', a: '6 (8650 − 3420 = 5230)' },
      { q: 'In a magic square, every row adds up to 2400. One row has 900 and 600 in it. What is the missing number in that row?', a: '900' },
      { q: 'A shop had 5000 stickers. It sold 1275 on Monday and 1480 on Tuesday. How many stickers are left?', a: '2245' }
    ],
    stretch: [
      { q: 'Find the missing digits:  2□7□ + □6□9 = 6000', a: '2371 + 3629 = 6000 (the only way)' },
      { q: 'In a number pyramid, each brick is the sum of the two bricks under it. The bottom row is 1200, □, □. The middle row is 2650, □. The top brick is 6000. Find the missing bricks.', a: 'Bottom row 1200, 1450, 1900. Middle row 2650, 3350.' },
      { q: 'Ali meant to add 1099 to a number, but he added 1999 by mistake and got 6543. What is the correct answer?', a: '5643 (he added 900 too much: 6543 − 900)' },
      { q: 'What is the smallest 4-digit number whose digits add up to 30? What is the greatest?', a: 'Smallest 3999, greatest 9993.' },
      { q: '◆● + ● = ●◆. Different shapes are different digits. Find ◆ and ●.', a: '◆ = 8, ● = 9:  89 + 9 = 98' },
      { q: 'Use the 9999 trick:  10 000 − 3746 = ?', a: '6254 (9999 − 3746 = 6253, then add 1)' },
      { q: '▲▲ + ■■ = ●■●. Different shapes are different digits. Find them.', a: '▲ = 9, ■ = 2, ● = 1:  99 + 22 = 121' },
      { q: 'Use the cards 2, 3, 5, 6 once each to make two 2-digit numbers. Make the difference as small as possible.', a: '9 (35 − 26, or 62 − 53)' }
    ],
    challenge: [
      { q: 'Find the missing digits:  8□0□ − □4□7 = 2468', a: '8905 − 6437 = 2468 (the only way; check 2468 + 6437 = 8905)' },
      { q: 'A 4-digit number has all different digits that add up to 30. Find the difference between the greatest and the smallest such number.', a: '3087. The only four different digits that add up to 30 are 9, 8, 7, 6, so 9876 − 6789 = 3087.' },
      { q: 'Mei thinks of a number. She adds 2500, then takes away 1750, and gets 6000. What was her number?', a: '5250 (work backwards: 6000 + 1750 = 7750, 7750 − 2500 = 5250)' },
      { q: '■▲● − ●▲ = ●■▲. Different shapes are different digits. Find the digits.', a: '■ = 7, ▲ = 3, ● = 6:  736 − 63 = 673' },
      { q: 'Make a magic square with the numbers 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700 and 1800. What is the magic total?', a: '4200, with 1400 in the centre. One answer: 1100, 1600, 1500 / 1800, 1400, 1000 / 1300, 1200, 1700.' },
      { q: 'Use the digits 1 to 9 once each:  □□□ + □□□ = □□□. What is the greatest possible answer?', a: '981, e.g. 235 + 746 = 981' },
      { q: '◆◆ + ●● + ▲▲ = ◆●▲. Different shapes are different digits. Find them.', a: '◆ = 1, ● = 9, ▲ = 8:  11 + 99 + 88 = 198' },
      { q: 'Use the digit cards 1 to 8 once each to make two 4-digit numbers. Make their difference as small as possible.', a: '247:  5123 − 4876 (the only way). The thousands digits must be next to each other; 5 and 4 in the middle work best.' },
      { q: '★■● + ★●■ = ●■★. Different shapes are different digits. Find them.', a: '★ = 4, ■ = 5, ● = 9:  459 + 495 = 954' }
    ]
  },

  workbook: H => [
    H.p('Work one column at a time, starting with the ones. Remember the carried 1!', { after: 80 }),
    H.q(1, 'Find the missing digits. Write them in the boxes.', { before: 40, keepNext: true }),
    H.fig(svg('Two column sums with missing digits', 200,
      colsum(['3?47', '25?8', '?025'], '+', 110, 20, 40, 50, '(a)') + colsum(['7?03', '?46?', '2538'], '−', 410, 20, 40, 50, '(b)'), 520)),
    H.sub('c', 'Hint for (b): turn it round and add, 2538 + □46□ = 7□03. Check (b) by adding: 2538  +  ________  =  ________'),
    H.q(2, 'Use the digit cards 1 to 6, each once, to make two 3-digit numbers.', { keepNext: true }),
    H.fig(cardsSvg(['1', '2', '3', '4', '5', '6'])),
    H.sub('a', 'Make the sum as GREAT as possible.          ________  +  ________  =  ________'),
    H.sub('b', 'Make the sum as SMALL as possible.          ________  +  ________  =  ________'),
    H.sub('c', 'Make the DIFFERENCE as small as possible. Guess, check, then improve. Write your tries.'),
    ...H.lines(2),
    H.ans('Best:'),

    H.q(3, 'Magic square: every row, column and diagonal adds up to the same total.', { pb: true, before: 0, keepNext: true }),
    H.fig(magicSvg([1200, 1700, 1600, '', 1500, '', '', '', ''])),
    H.sub('a', 'What is the magic total?   ________   Fill in the missing numbers.'),
    H.sub('b', 'Look at two numbers opposite each other across the centre. What do you notice?'),
    ...H.lines(1),
    H.q(4, 'Number pyramids: each brick is the sum of the two bricks under it. Work backwards.', { before: 80, keepNext: true }),
    H.fig(svg('Two number pyramids with missing bricks', 160, pyramid(30, [5975, '', 3600, 1250, '', ''], '(a)') + pyramid(318, [7000, '', '', '', 2000, ''], '(b)  corner bricks are equal'), 450)),
    H.q(5, 'Look for a pattern.', { before: 80, keepNext: true }),
    H.sub('a', '4127 + ________ = 9999    and    2593 + ________ = 9999'),
    H.sub('b', 'What do you notice about the digits? Why is there no carrying?'),
    ...H.lines(1),
    H.sub('c', 'Use your pattern:   10 000 − 4127  =  ________'),
    H.q(6, 'Shape puzzle. Each shape stands for a digit. Different shapes are different digits.', { before: 80, keepNext: true }),
    H.fig(svg('Shape sum: star circle plus star circle plus star circle equals triangle star circle', 64, shapeLine('SC+SC+SC=TSC'), 400)),
    H.sub('a', '★ = ______   ● = ______   ▲ = ______'),
    H.sub('b', 'The ones column: ● + ● + ● ends in ●. Which digits can ● be? Try 0 and 5, then check the tens column. How do you know?'),
    ...H.lines(1)
  ]
};
