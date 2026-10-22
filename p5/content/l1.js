// Math Inquirers Level 5 — Lesson 1: Million Puzzles (numbers to 10 million, four operations)
// Heuristics: test the best number just below AND just above a target; use the clues in order and check every clue;
// estimate by rounding to catch wrong answers; brackets first, then × and ÷, then + and −; write the range before "find all".
// Every answer below was worked out and checked with a short Python script (exact search over all cases).
const N = '#1B2A49', Y = '#FFC93C', SKY = '#DDEBF7', TEAL = '#1F7A6F', RED = '#D64545', WH = '#FFFFFF';
const FF = 'Fredoka, Arial, sans-serif';
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const txt = (x, y, s, size = 18, fill = N, anchor = 'middle', weight = 700) =>
  `<text x="${x}" y="${y}" font-size="${size}" font-weight="${weight}" text-anchor="${anchor}" fill="${fill}" font-family="${FF}">${esc(s)}</text>`;

// seven digit cards in a row
const cardsSvg = (digits, label) => {
  const w = 50, h = 62, gap = 16, tot = digits.length * w + (digits.length - 1) * gap, x0 = (600 - tot) / 2;
  let g = '';
  digits.forEach((d, i) => {
    const x = x0 + i * (w + gap);
    g += `<rect x="${x}" y="6" width="${w}" height="${h}" rx="10" fill="${Y}" stroke="${N}" stroke-width="3"/>` + txt(x + w / 2, 6 + h / 2 + 12, d, 32);
  });
  return `<svg aria-label="${esc(label)}" viewBox="0 0 600 76" width="600" xmlns="http://www.w3.org/2000/svg" style="max-width:76%">${g}</svg>`;
};

// number line for Q6: the numbers that round to 2 500 000 (nearest thousand)
const roundLine = () => {
  const x0 = 40, x1 = 560, y = 60;
  const ticks = [['2 499 000', x0], ['2 499 500', x0 + 130], ['2 500 000', 300], ['2 500 500', x1 - 130], ['2 501 000', x1]];
  let g = `<line x1="${x0 - 20}" y1="${y}" x2="${x1 + 20}" y2="${y}" stroke="${N}" stroke-width="3"/>`;
  g += `<rect x="${x0 + 130}" y="${y - 14}" width="260" height="28" fill="${SKY}" stroke="${N}" stroke-width="2" stroke-dasharray="6 4"/>`;
  ticks.forEach(([s, x], i) => {
    g += `<line x1="${x}" y1="${y - 18}" x2="${x}" y2="${y + 18}" stroke="${N}" stroke-width="3"/>` + txt(x, y + 44, s, 15, i === 2 ? TEAL : N);
  });
  g += txt(300, 26, 'Which numbers round to 2 500 000?', 16, TEAL);
  return `<svg aria-label="Number line from 2 499 000 to 2 501 000 with the middle part, around 2 500 000, shaded" viewBox="0 0 600 116" width="600" xmlns="http://www.w3.org/2000/svg" style="max-width:100%">${g}</svg>`;
};

module.exports = {
  lesson: {
    n: 1, week: 1, session: 'A', title: 'Million Puzzles', topic: 'Numbers to 10 Million',
    objective: 'Read, write and compare numbers up to 10 million; solve digit-card and digit-riddle puzzles with place value (testing the best number just below and just above a target); estimate to check large calculations; and use the order of operations and brackets to hit target numbers.',
    skills: 'Place value to 10 million, testing both sides of a target, reasoning from clues in order, estimating by rounding, order of operations with brackets, making a list in order',
    materials: 'Digit cards 0 to 9 (one set per child), a 7-column place-value mat (M, HTh, TTh, Th, H, T, O), mini whiteboard, a calculator for the explore (every child needs one; a phone calculator is fine), workbook.',
    online: 'Children cut out paper digit cards and draw a 7-box place-value mat before the lesson and hold them up to the camera. The tutor shares the slides and writes on the place-value chart. Pairs work in breakout rooms for the explore and page 1. Before the lesson, ask every parent to put a calculator (a phone calculator is fine) next to the child for the explore.',
    warmup: 'Million Maker: the tutor turns over digit cards one at a time; children write each digit in one of seven place-value boxes straight away and cannot move it. Closest to 5 000 000 wins. Then five quick questions on whiteboards.',
    explore: 'How long is a million seconds? Pairs guess first (an hour, a day, a week, a month or a year), then work out the seconds in an hour and in a day and use them to find how many days a million seconds lasts.',
    mini: 'Read 7-digit numbers in groups of three from the right; tell the value of a digit apart from how many thousands a number has. Closest to a target with digit cards: build the best number just below and the best just above, then compare the gaps. Digit riddles: use the rounding clue to fix the first digits, follow the clues in order and check every clue at the end. Before page 2: estimate by rounding to catch wrong calculator answers; brackets first, then × and ÷, then + and −; for "find all" with rounding, write the range first.',
    share: 'Siti says a 7-digit number is always bigger than a 6-digit number. Ravi says not if the 6-digit number has bigger digits, like 999 999. Who is right? Explain.',
    exit: { q: '(a) What is the value of the digit 4 in 8 406 125?  (b) Add one pair of brackets to make it true:  5 + 3 × 8 − 2 = 62', a: '(a) 400 000  (b) (5 + 3) × 8 − 2 = 62' },
    mistakes: [
      'Leaving out zeros that hold a place, for example writing three million, forty thousand and six as 340 006 instead of 3 040 006, or mixing up the value of a digit (3000) with how many thousands a number has (4053).',
      'Looking only on one side of the target: for "closest to 6 000 000" trying only numbers that start with 6 and missing 5 986 320, which is closer.',
      'Working from left to right and ignoring the order of operations (6 + 4 × 5 read as 50 instead of 26).'
    ],
    extension: 'Use the digit cards 0 to 9, each at most once, to make the 7-digit number closest to 5 000 000. (5 012 346 is 12 346 away and 4 987 653 is 12 347 away, so 5 012 346 wins by 1.)',
    key: [
      ['Q1', '(a) 5 308 040  (b) 400 000; 8  (c) 3250'],
      ['Q2', '(a) 9 865 320  (b) 2 035 698  (c) Just below: 5 986 320 (13 680 away). Just above: 6 023 589 (23 589 away). Closest: 5 986 320.'],
      ['Q3', '7 253 609. Rounding gives 7 2 with ten thousands digit 5 or more, or 7 3 with ten thousands digit 4 or less. "3 more" only works for 7 25: 2 + 3 = 5. Then thousands 5 − 2 = 3, hundreds 6, tens 0, and 7 + 2 + 5 + 3 + 6 + 0 = 23, so the ones digit is 32 − 23 = 9.'],
      ['Q4', '(a) about 100 000: could be right  (b) about 60 000: must be wrong  (c) about 6 300 000: must be wrong  (d) about 320 000: could be right'],
      ['Q5', '(a) (6 + 4) × 5 − 2 = 48  (b) 6 + 4 × (5 − 2) = 18  (c) 1 000 000 ÷ (200 + 300) × 2 = 4000  (d) 5 × (3 × 9 − 7) = 100'],
      ['Q6', '(a) 2 499 500 and 2 500 499  (b) 2 500 002, 2 500 011, 2 500 020, 2 500 101, 2 500 110, 2 500 200: 6 numbers. None below 2 500 000: 2 499 5__ already has digits adding to at least 29.']
    ]
  },

  script: {
    hook: ['Welcome to Math Inquirers Level 5! This holiday we play with puzzles that stretch you before P6. Every lesson we notice a pattern, test it and explain why.', 'Today our numbers grow up to 10 million. How big is a million, really? By the end you will know, and you will solve puzzles that most adults get wrong.'],
    warmIntro: ['Draw seven boxes for millions down to ones. I turn over one digit card at a time. Write it in a box straight away. No moving it later!', 'The winner is the number closest to 5 000 000. Think: where does a 4 go? A 9? A 0?'],
    predict: ['Before any working: how long is a million seconds? An hour, a day, a week, a month or a year? Write your guess in the corner of your whiteboard and do not change it.'],
    exploreHints: ['Stuck: how many seconds in one minute? In one hour? Multiply, do not add.', 'Stuck on days: you know the seconds in one day. How many days make close to 1 000 000? Try 10 days first.', 'Finished early: how long is 10 million seconds? More or less than a school term?'],
    think: [
      '“Cards 0, 1, 2, 4, 5, 7, 8. I want the number closest to 5 000 000. I could start with 5 and make the smallest number after it: 5 012 478. That is 12 478 too big.”',
      '“But I must also look just below the target. Start with 4 and make the biggest number after it: 4 875 210. That is 124 790 too small. I compare the two gaps: 12 478 is smaller, so 5 012 478 wins. I always test both sides.”',
      '“For a digit riddle I use the clue that fixes the most digits first. Rounded to the nearest hundred thousand it is 3 600 000, so it starts 3 5 with a big digit next, or 3 6 with a small digit next. Then I follow the other clues one by one and check every clue at the end.”'
    ],
    circulate: ['Ask: “Did you look just below AND just above the target?”', 'Ask: “Which clue fixes the most digits? Start there.”', 'Ask: “Estimate first. Is the calculator answer about the right size?”'],
    hints: ['Hint 1: “Read the number in groups of three from the right: millions, thousands, ones.”', 'Hint 2: “Write the two best numbers, one just below and one just above, and find each gap.”', 'Hint 3: “Put each clue’s digit straight into the place-value chart as you go.”'],
    talk: ['“Siti says a 7-digit number is always bigger than a 6-digit number. Ravi says not if the 6-digit number has bigger digits, like 999 999. Who is right?”', '“How did you check that you had found ALL the numbers in Q6?”'],
    talkAns: 'Siti is right. The smallest 7-digit number is 1 000 000 and the biggest 6-digit number is 999 999, which is 1 less. A 7-digit number has a millions digit that is at least 1, and that alone beats every 6-digit number, whatever its digits are.',
    close: ['“Today you read numbers up to 10 million, tested both sides of a target, followed clues to a single answer and used estimation and brackets. That is how inquirers work with big numbers.”', '“Do the exit ticket on your own, then show me.”']
  },

  deck: {
    today: 'Read and build numbers up to 10 million, solve digit puzzles, estimate to catch mistakes and use brackets to hit a target.',
    warmGame: 'Million Maker. Draw seven boxes (M to O). The tutor turns over digit cards one at a time; write each one in a box straight away and do not move it. Closest to 5 000 000 wins. Play 3 rounds.',
    warmQs: [['Write in numerals: 3 million, 40 thousand and 6', '3 040 006'], ['The value of the 7 in 2 716 450', '700 000'], ['4 560 000 ÷ 1000', '4560'], ['Round 6 849 500 to the nearest thousand', '6 850 000'], ['8 + 4 × 5 − 6 ÷ 2', '25']],
    expSetup: ['Guess first: is a million seconds about an hour, a day, a week, a month or a year? Write your guess.', 'Work out how many seconds there are in 1 hour.', 'Work out how many seconds there are in 1 day.', 'How many days is 1 000 000 seconds? Get as close as you can, then compare with your guess.'],
    expPic: 'a stopwatch next to a big counter showing 1 000 000 seconds, with a calendar page and a question mark.',
    expAsk: [['How many seconds are in 1 day?', '86 400 (60 × 60 = 3600 in an hour, × 24).'], ['About how many days is a million seconds?', 'Between 11 and 12 days: 11 days = 950 400 s and 12 days = 1 036 800 s. About 11 and a half days.'], ['About how long is 10 million seconds?', 'About 116 days, nearly 4 months (10 × 11.6 days).']],
    mini1: { head: 'Closest to 5 000 000 with the cards 0, 1, 2, 4, 5, 7, 8', body: ['Just above: start with 5, then the smallest: 5 012 478 (12 478 away).', 'Just below: start with 4, then the biggest: 4 875 210 (124 790 away).', 'Compare the gaps.'], ans: '5 012 478 is closest. Always test both sides of the target.' },
    mini2: { head: 'Digit riddle: rounds to 3 600 000 (nearest hundred thousand); ten thousands digit is 4 more than the hundred thousands digit; thousands digit is their difference; hundreds digit is half the thousands digit; tens digit 0; digits add to 31; all different', body: ['Rounding: 3 5 with a big digit next, or 3 6 with a small digit next.', '4 more: 5 + 4 = 9 works; 6 + 4 = 10 does not.', 'Thousands 9 − 5 = 4, hundreds 2, tens 0, ones 31 − 23 = 8.'], ans: '3 594 208. Check every clue at the end.' },
    keyHead: 'Key idea: test both sides, check every clue',
    keyBig: 'Place value tells you what each digit is worth. To get closest to a target, test the best number just below AND just above.',
    keySmall: 'Riddles: start with the clue that fixes the most digits, then check every clue at the end.',
    brk: 'Human number line: stand up and stretch as tall as 10 million, crouch as small as 1, then show where 5 million, 2 500 000 and 9 900 000 would be with your arms.',
    ws1: 'Page 1, in pairs: Q1 place value, Q2 digit cards and the closest number, Q3 the digit riddle.',
    ws2: 'Page 2, on your own: Q4 estimate to catch mistakes, Q5 brackets and a target of 100, Q6 find all the numbers.'
  },

  qbank: {
    core: [
      { q: 'Write 4 030 205 in words.', a: 'Four million, thirty thousand, two hundred and five.' },
      { q: 'What is the value of the digit 6 in 3 621 480?', a: '600 000' },
      { q: 'Round 5 482 716 to the nearest thousand.', a: '5 483 000' },
      { q: 'Use seven digit cards, 0 1 2 3 4 5 6, each once. Make the greatest 7-digit number you can, and then the smallest. (A 7-digit number cannot start with 0.)', a: 'Greatest 6 543 210; smallest 1 023 456.' },
      { q: 'A shop has 48 pens. It sells 6 packs. Each pack has 3 red pens and 4 blue pens. How many pens are left? (Draw the packs or use counters if it helps.)', a: '6 (each pack has 7 pens, 6 packs are 42 pens, 48 − 42 = 6). As one number sentence: 48 − 6 × (3 + 4) = 6.' },
      { q: 'Estimate 6912 × 48 by rounding 6912 to the nearest thousand and 48 to the nearest ten.', a: 'About 350 000 (7000 × 50). The exact answer is 331 776.' }
    ],
    stretch: [
      { q: 'How many 7-digit numbers have digits that add up to 2? List them all.', a: '7 numbers: 1 000 001, 1 000 010, 1 000 100, 1 001 000, 1 010 000, 1 100 000 and 2 000 000.' },
      { q: 'Put ONE pair of brackets into 2 + 3 × 4 + 5 to make 25. Then put one pair in a different place to make 29.', a: '(2 + 3) × 4 + 5 = 25 and 2 + 3 × (4 + 5) = 29. (29 is the biggest you can make with one pair.)' },
      { q: 'A whole number rounded to the nearest thousand is 640 000. What is the greatest it could be? The smallest?', a: 'Greatest 640 499, smallest 639 500.' },
      { q: 'Use each of the digits 1, 2, 3, 4, 5, 6 and 7 once. What is the difference between the greatest and the smallest 7-digit number you can make?', a: '6 419 754 (7 654 321 − 1 234 567).' },
      { q: 'Which is the best estimate of 4108 × 29: 12 000, 120 000 or 1 200 000? Explain.', a: '120 000, because 4000 × 30 = 120 000. (Exactly 119 132.)' },
      { q: 'Use 2, 3, 5 and 7 once each, with +, −, ×, ÷ and brackets, to make 29, then 31, then 100.', a: '29 = 5 × 7 − 2 × 3;  31 = 2 × 5 + 3 × 7;  100 = 2 × 5 × (3 + 7). Other ways are possible.' },
      { q: 'Use four 4s with +, −, ×, ÷ and brackets to make 3, then 5, then 7.', a: '(4 + 4 + 4) ÷ 4 = 3;  (4 × 4 + 4) ÷ 4 = 5;  4 + 4 − 4 ÷ 4 = 7. Other ways are possible.' },
      { q: 'Use the seven digit cards 1, 2, 5, 6, 7, 8, 9 once each to make the 7-digit number closest to 7 000 000. Test both sides of the target.', a: '6 987 521 (12 479 below 7 000 000). The best number above is 7 125 689, which is 125 689 away.' }
    ],
    challenge: [
      { q: 'Make up your own digit riddle for a 7-digit number. Use at least 5 clues (for example: all digits different, a rounding clue, a clue that compares two digits, a digit sum). Only ONE number may fit. Swap with a partner: do you get the same answer? How can you be sure your riddle has only one answer?', a: 'Open-ended. Check the riddle by listing every number that fits the rounding clue first. Sample riddle with exactly one answer (checked on a computer over all 7-digit numbers): all digits different; rounds to 5 400 000 to the nearest hundred thousand; the ten thousands digit is 1 less than the hundred thousands digit; the thousands digit is the sum of those two digits; the tens digit is 0 and the hundreds digit is even; the digits add up to 30. Answer: 5 437 209.' },
      { q: 'Write 1 000 000 as the product of two whole numbers that have no zero digits at all.', a: '64 × 15 625. (1 000 000 = 10 × 10 × 10 × 10 × 10 × 10; put all the 2s together to make 64 and all the 5s together to make 15 625.)' },
      { q: 'Ben multiplies a 4-digit number by a 3-digit number. How many digits can his answer have?', a: '6 or 7. The smallest answer is 1000 × 100 = 100 000 (6 digits); the greatest is 9999 × 999 = 9 989 001 (7 digits).' },
      { q: 'A palindrome reads the same forwards and backwards, like 3 456 543. How many 7-digit palindromes are there between 3 000 000 and 4 000 000?', a: '1000. The first and last digits are 3; the 2nd, 3rd and 4th digits can be anything (10 × 10 × 10), and they fix the rest.' },
      { q: 'Use 1, 2, 3, 4, 5 in this order, with +, −, ×, ÷ and brackets, to make 100.', a: '(1 × 2 + 3) × 4 × 5 = 100  (or 1 × (2 + 3) × 4 × 5 = 100).' },
      { q: 'A heart beats about 70 times a minute. About how many days does it take to beat 1 000 000 times?', a: 'About 10 days. 70 × 60 × 24 = 100 800 beats a day, and 1 000 000 ÷ 100 800 is just under 10.' },
      { q: 'Put brackets into 1 + 2 × 3 + 4 × 5 + 6 to make the answer as big as possible. You may use more than one pair. What is the biggest answer?', a: '231: (1 + 2) × (3 + 4) × (5 + 6) = 3 × 7 × 11. With no brackets it is only 33.' },
      { q: 'I am a 7-digit odd number. My digits are all different and add up to 42. Rounded to the nearest hundred thousand, I am 7 000 000. I am the smallest number that fits. Who am I?', a: '6 953 487. Seven different digits adding to 42 must be 3, 4, 5, 6, 7, 8, 9 (the biggest seven digits add to exactly 42), so there is no 0. The number is between 6 950 000 and 7 049 999, so it starts 6 9 with 5, 7 or 8 next; the smallest is 6 95 then 3, 4, 8, 7 (it must end in an odd digit).' },
      { q: 'Ali writes all the whole numbers from 1 to 1000. How many digits does he write? (Go further: how many if he writes all the numbers from 1 to 1 000 000?)', a: '2893.  9 × 1 + 90 × 2 + 900 × 3 + 4 = 9 + 180 + 2700 + 4.  Go further: 5 888 896  (9 × 1 + 90 × 2 + 900 × 3 + 9000 × 4 + 90 000 × 5 + 900 000 × 6 + 7 = 9 + 180 + 2700 + 36 000 + 450 000 + 5 400 000 + 7).' }
    ]
  },

  workbook: H => {
    const W = [];
    const raw = s => [s];
    // Q1 place value
    W.push(H.q(1, 'Place value. Read big numbers in groups of three from the right:  4 | 053 | 200.', { before: 20, keepNext: true }));
    W.push(H.sub('a', 'Numerals for five million, three hundred and eight thousand and forty:  ________'));
    W.push(H.sub('b', 'In 6 482 315, the digit 4 stands for ________.  The ten thousands digit is ____.'));
    W.push(H.sub('c', 'How many thousands make 3 250 000?   __________'));
    // Q2 digit cards
    W.push(H.q(2, 'Use ALL seven digit cards, each once, to make a 7-digit number (it cannot start with 0).', { keepNext: true }));
    W.push(H.fig(cardsSvg([0, 2, 3, 5, 6, 8, 9], 'Digit cards 0, 2, 3, 5, 6, 8 and 9')));
    W.push(H.sub('a', 'Greatest:  ____________      (b)  Smallest EVEN:  ____________'));
    W.push(H.sub('c', 'Closest to 6 000 000:  ______________   Test both sides of the target!', { keepNext: true }));
    W.push(H.sub(' ', 'Best just below:  ______________   It is  __________  away.'));
    W.push(H.sub(' ', 'Best just above:  ______________   It is  __________  away.'));
    // Q3 riddle
    W.push(H.q(3, 'Digit riddle  (try this one if you like). Use the clues one at a time, then check them all.', { keepNext: true }));
    { const clues = ['I am a 7-digit number. My digits are all different.',
      'Rounded to the nearest hundred thousand, I am 7 300 000.',
      'My ten thousands digit is 3 more than my hundred thousands digit.',
      'My thousands digit = my ten thousands digit − my hundred thousands digit.',
      'My hundreds digit is twice my thousands digit. My tens digit is 0.',
      'My digits add up to 32.',
      'START HERE: I start 7 2 … or 7 3 …  Which start fits Clue 3?'];
      W.push(H.tbl([9900], [H.row([H.cell(['<div style="text-align:left;padding:2px 10px;line-height:1.5">' + clues.map((c, i) => i < 6 ? `<b style="color:${TEAL}">Clue ${i + 1}.</b>&nbsp; ${esc(c)}` : `<b style="color:${TEAL}">${esc(c)}</b>`).join('<br>') + '</div>'], 9900, { h: 60 })])])); }
    { const ws = Array(7).fill(1414); ws[6] = 1416;
      W.push(H.tbl(ws, [H.row(['M', 'HTh', 'TTh', 'Th', 'H', 'T', 'O'].map((s, i) => H.cell(s, ws[i], { bold: true, fill: 'EDEDED', h: 30 }))),
        H.row(ws.map(w => H.cell('', w, { h: 80 })))])); }
    W.push(H.sub(' ', 'I am  ______________________'));

    // ---- page 2 ----
    W.push(H.q(4, 'Ravi used a calculator. Estimate each answer by rounding. Which answers must be wrong?', { pb: true, before: 0, keepNext: true }));
    { const ws = [3500, 1700, 2500, 2200];
      W.push(H.tbl(ws, [H.row(['Calculation', 'Ravi’s answer', 'My estimate', 'Could be right / Must be wrong'].map((s, i) => H.cell(s, ws[i], { bold: true, fill: 'D9D9D9', h: 40 }))),
        ...[['(a)  4987 × 21', '104 727'], ['(b)  3 004 512 ÷ 48', '6259'], ['(c)  2 345 678 + 3 987 654', '5 333 332'], ['(d)  806 × 395', '318 370']].map(([c, a]) =>
          H.row([H.cell(c, ws[0], { h: 90, align: 'left' }), H.cell(a, ws[1], { h: 90 }), H.cell('', ws[2]), H.cell('', ws[3])]))])); }
    // Q5 brackets
    W.push(H.q(5, 'Brackets first, then × and ÷, then + and −. Put in ONE pair of brackets to make each statement true.', { keepNext: true }));
    W.push(H.sub('a', '6  +  4  ×  5  −  2  =  48'));
    W.push(H.sub('b', '6  +  4  ×  5  −  2  =  18'));
    W.push(H.sub('c', '1 000 000  ÷  200  +  300  ×  2  =  4000'));
    W.push(H.sub('d', 'Target 100! Use 3, 5, 7 and 9 once each with +, −, ×, ÷ and brackets to make 100.  Hint: 100 = 5 × 20.', { after: 40 }));
    W.push(...H.lines(1));
    // Q6 find all
    W.push(H.q(6, 'A 7-digit number rounded to the nearest thousand is 2 500 000. Its digits add up to 9.', { keepNext: true }));
    W.push(H.fig(roundLine()));
    W.push(H.p(['<b style="color:' + TEAL + '">Start here:</b> numbers from 2 500 000 up begin 2 5 0 …  Those three digits add to 7, so the last four digits must add to ____. Try 2 500 002 first.'], { after: 20 }));
    W.push(H.sub('a', 'Write the range first. The smallest number that rounds to 2 500 000 is ____________ and the greatest is ____________.'));
    W.push(H.sub('b', 'Find ALL the numbers. Make a list in order. How do you know you have them all?', { after: 40 }));
    W.push(...H.lines(3));
    return W;
  }
};
