// Math Inquirers P4 Holiday Program — Lesson 2: Big Number Puzzles (Numbers to 100 000)
const tip = require('../tip.js');
const FG = require('../../levels/figs_l4_6.js');
const N = '#1B2A49', Y = '#FFC93C', SKY = '#DDEBF7', TEAL = '#1F7A6F', RED = '#D64545', WH = '#FFFFFF';
const F = 'Fredoka, Arial, sans-serif';
const txt = (x, y, s, size = 18, fill = N, anchor = 'middle', weight = 700) =>
  `<text x="${x}" y="${y}" font-size="${size}" font-weight="${weight}" text-anchor="${anchor}" fill="${fill}" font-family="${F}">${s}</text>`;

// a row of digit cards (workbook drawing)
const cardsSvg = (digits, label) => {
  const w = 60, g = 18, tot = digits.length * w + (digits.length - 1) * g, x0 = (600 - tot) / 2;
  let s = `<svg aria-label="${label}" viewBox="0 0 600 90" width="600" xmlns="http://www.w3.org/2000/svg" style="max-width:100%">`;
  digits.forEach((d, i) => {
    const x = x0 + i * (w + g);
    s += `<rect x="${x}" y="6" width="${w}" height="78" rx="10" fill="${Y}" stroke="${N}" stroke-width="3"/>` + txt(x + w / 2, 60, d, 42);
  });
  return s + '</svg>';
};

// Q2: number line from 62 000 to 64 000
const lineSvg = () => {
  const x0 = 50, x1 = 550;
  let s = `<svg aria-label="Number line from 62 000 to 64 000 with 62 500, 63 000 and 63 500 marked" viewBox="0 0 600 80" width="600" xmlns="http://www.w3.org/2000/svg" style="max-width:100%">`;
  s += `<line x1="${x0 - 20}" y1="30" x2="${x1 + 20}" y2="30" stroke="${N}" stroke-width="3"/>`;
  for (let i = 0; i <= 20; i++) {
    const x = x0 + i * 25, big = i % 5 === 0;
    s += `<line x1="${x}" y1="${big ? 18 : 24}" x2="${x}" y2="${big ? 42 : 36}" stroke="${N}" stroke-width="${big ? 3 : 1.5}"/>`;
  }
  [['62 000', 0], ['62 500', 5], ['63 000', 10], ['63 500', 15], ['64 000', 20]].forEach(([t, i]) => { s += txt(x0 + i * 25, 66, t, 16, i === 10 ? TEAL : N); });
  return s + '</svg>';
};

module.exports = {
  lesson: {
    n: 2, week: 1, session: 'B', title: 'Big Number Puzzles', topic: 'Numbers to 100 000',
    objective: 'Round numbers to the nearest 10, 100 and 1000 using a number line, work backwards from a rounded number to find the smallest and largest possible numbers, use rounding to estimate and check, and solve 5-digit number riddles, digit-card puzzles and number patterns.',
    skills: 'Using a number line, working backwards, making a list in order, using the clues one at a time, looking for a pattern',
    materials: 'Digit cards 0 to 9 (one set per child: cut them from the Digit, point, sign and bracket cards page), mini whiteboards, a place-value chart (ten thousands to ones), a blank number line strip.',
    online: 'Children cut out the digit cards from the kit page before the lesson and move them on camera; the tutor marks the number lines on the slides.',
    warmup: 'Place It Right (5 digits): the tutor draws digit cards one at a time. After each card, children must write it in the ten thousands, thousands, hundreds, tens or ones box straight away. Round 1: biggest number wins. Round 2: closest to 50 000 wins.',
    explore: 'Pairs use the digit cards 2, 4, 5, 7 and 9 once each to make 5-digit numbers. Which of their numbers round to 50 000 when rounded to the nearest thousand? They try to find them all and decide which one is closest to 50 000.',
    mini: 'Round with a number line: 36 482 lies between 36 000 and 37 000; the halfway mark is 36 500, so it rounds to 36 000 (to the nearest hundred, 36 500). Work backwards: a number that rounds to 25 000 (nearest thousand) is from 24 500 to 25 499. Estimate 7 × 3 089 as 7 × 3 000 = 21 000; the exact answer (21 623) is more, because 3 089 was rounded down. Before page 2: a riddle that starts with a rounding clue (20 003); number patterns (find the rule, then continue); digit-card puzzles: the ones digit decides odd or even, and 0 cannot go first.',
    share: 'Siti says 49 999 rounds to 50 000 to the nearest 10, the nearest 100 and the nearest 1000. Is she right?',
    exit: { q: 'Round 74 652 to the nearest thousand. Then write the smallest whole number that rounds to 74 000 to the nearest thousand.', a: '75 000. The smallest is 73 500.' },
    mistakes: [
      'Rounding by looking at the wrong digit, or forgetting to carry when the digit to change is a 9 (63 950 to the nearest hundred written as 63 900 or 63 000 instead of 64 000).',
      'Working backwards with the wrong limits: saying the largest number that rounds to 63 000 is 63 500 (it rounds up to 64 000) instead of 63 499.',
      'Digit-card puzzles: putting 0 in the ten thousands place, or making the biggest number first and then hoping it is even, instead of choosing the ones digit first.'
    ],
    extension: 'How many whole numbers round to 45 000 to the nearest thousand AND to 50 000 to the nearest ten thousand? (500: from 45 000 to 45 499.)',
    key: [
      ['Q1', '47 285: 47 290, 47 300, 47 000.  63 950: 63 950, 64 000, 64 000.  Try next: 9049: 9050, 9000, 9000.  80 503: 80 500, 80 500, 81 000.'],
      ['Q2', '(a) Smallest 62 500, largest 63 499  (b) 5345, 5346, 5347, 5348, 5349, 5350, 5351, 5352, 5353, 5354 (10 numbers)'],
      ['Q3', '(a) 6 × 5 000 = 30 000  (b) Less: 4 982 was rounded up to 5 000, so each day was counted as a little more than it really is.  (c) 29 892'],
      ['Q4', '(a) 47 621  (b) 10 001, 10 010, 10 100, 11 000, 20 000 (5 numbers)'],
      ['Q5', '(a) 26 450, 27 450  (b) 76 800, 75 300  (c) 99 990, 100 000  (d) 32 500'],
      ['Q6', '(a) 86 530  (b) 30 685  (c) 60 358']
    ]
  },

  script: {
    hook: ['Welcome back, inquirers! Today our numbers get BIG: all the way up to 100 000. That is more than the number of people who fit in the National Stadium.', 'Big numbers are often rounded. Today we find out what a rounded number can hide, and we solve riddles about 5-digit numbers. Notice it. Test it. Explain why.'],
    warmIntro: ['Draw five boxes on your whiteboard: ten thousands, thousands, hundreds, tens, ones. I turn over one digit card at a time. Write it in a box straight away. No moving it later!', 'Round 1: make the biggest number. Round 2: make the number closest to 50 000. Where will you put a 4? A 5?'],
    predict: ['You have the cards 2, 4, 5, 7 and 9. How many of the numbers you can make will round to 50 000 to the nearest thousand? Write your guess.'],
    exploreHints: ['Stuck: which ten thousands digit could give a number near 50 000? There is no 5 0 … because there is no 0 card.', 'Not sure about one number: draw a number line from 49 000 to 50 000. Where is the halfway mark?', 'Finished early: which number you can make is closest to 70 000?'],
    think: [
      '“36 482 to the nearest thousand. It is between 36 000 and 37 000. Halfway is 36 500. 36 482 is just below halfway, so it is nearer 36 000.”',
      '“A number rounds to 25 000. The smallest it could be is 24 500, because 24 500 is exactly halfway and halfway rounds up. The largest is 25 499. 25 500 would round up to 26 000.”',
      '“7 × 3 089. I round 3 089 to 3 000, so the estimate is 21 000. I rounded DOWN, so the real answer must be a bit more: 21 623.”'
    ],
    circulate: ['Ask: “Which two round numbers is it between? Where is the halfway mark?”', 'Ask: “Could the number be bigger than that and still round to the same number?”', 'Ask: “Which clue gives you the fewest numbers to try? Start there.”'],
    hints: ['Hint 1: “Draw a number line. Mark the two round numbers and halfway.”', 'Hint 2: “Look only at the digit to the right of the place you round to.”', 'Hint 3: “For odd or even, choose the ones digit FIRST.”'],
    talk: ["“Siti says 49 999 rounds to 50 000 to the nearest 10, 100 AND 1000. Is she right?”"],
    talkWeekly: ["“Ravi says 45 000 rounds to 40 000 to the nearest ten thousand. Is he right?”"],
    talkAns: "Siti is right: 49 999 is only 1 away from 50 000, so it rounds to 50 000 every time.",
    talkWeeklyAns: "Ravi is wrong: 45 000 is exactly halfway between 40 000 and 50 000, and halfway rounds up, so it rounds to 50 000.",
    close: ['“Today you used number lines to round, and you worked backwards to find what a rounded number could really be.”', '“Hand me your exit ticket and I will stamp your inquiry journal.”']
  },

  deck: {
    today: 'Round big numbers on a number line, work backwards from a rounded number, and solve 5-digit riddles and patterns.',
    warmGame: 'Place It Right (5 digits). The tutor turns over digit cards one at a time. Write each in a box straight away. Round 1: biggest wins. Round 2: closest to 50 000 wins.',
    warmQs: [["What is the 7 worth in 47 352?", "7000"], ["Sixty thousand and forty-five in numerals?", "60 045"], ["1000 more than 59 600?", "60 600"]],
    warmWeekly: [["40 000 + 3000 + 50 + 8 = ?", "43 058"], ["36 815 to the nearest 1000?", "37 000"]],
    expSetup: ['Take the digit cards 2, 4, 5, 7 and 9.', 'Make a 5-digit number using each card once. Write it down.', 'Round it to the nearest thousand. Does it round to 50 000?', 'Find ALL the numbers that round to 50 000. Which is closest to 50 000?'],
    expPic: 'five yellow digit cards 2, 4, 5, 7 and 9 above a number line from 49 000 to 51 000 with 49 500 and 50 500 marked.',
    expAsk: [["Which numbers round to 50 000?", "49 527, 49 572, 49 725, 49 752."], ["How do you know you have them all?", "They must be from 49 500 to 50 499. With no 0 card, they start 49 and then 5 or 7: 2 numbers each."]],
    mini1: { head: 'Round 36 482 to the nearest thousand', body: ['Which two thousands is it between? 36 000 and 37 000.', 'Halfway is 36 500.', 'Is 36 482 before or after halfway?'], ans: '36 000 (it is before halfway). To the nearest hundred it is 36 500.' },
    mini2: { head: 'Work backwards: what rounds to 25 000?', body: ['Rounded to the nearest thousand, a number is 25 000.', 'The halfway marks are 24 500 and 25 500.', 'What are the smallest and largest whole numbers it can be?'], ans: 'Smallest 24 500, largest 25 499 (25 500 rounds up to 26 000).' },
    keyHead: 'Key idea: find the halfway mark', keyBig: 'To round, find the two round numbers and the halfway mark. Halfway or more rounds up.', keySmall: 'Working backwards: the smallest number IS the halfway mark below; the largest is 1 less than the halfway mark above.',
    brk: 'Human number line. Five children hold 10 000, 20 000, 30 000, 40 000, 50 000. The tutor calls a number: everyone points to the nearest ten thousand.',
    ws1: 'Page 1, in pairs: Q1 rounding table, Q2 working backwards. Q3 estimating is the first question on your own.',
    ws2: 'Page 2, on your own: Q4 number riddles, Q5 patterns, Q6 digit cards.'
  },

  qbank: {
    core: [
      { q: 'In 64 205, what is the digit 4 worth?', a: '4000 (4 thousands)' },
      { q: 'Write fifty-three thousand and eighty in numerals.', a: '53 080' },
      { q: 'Mei’s number is 27 649. Is it closer to 27 000 or to 28 000? Draw a number line from 27 000 to 28 000 and mark the halfway point (27 500) to help you.', a: '28 000 (27 649 is past the halfway point 27 500).' },
      { q: 'What number is 1000 less than 70 230?', a: '69 230' },
      { q: 'Put these numbers in order, smallest first: 45 099, 45 909, 45 990, 45 900.', a: '45 099, 45 900, 45 909, 45 990' },
      { q: 'A bakery baked 6352 buns. Is that closer to 6300 or to 6400? Draw a number line from 6300 to 6400 and mark the halfway point (6350).', a: '6400 (6352 is just past the halfway point 6350).' }
    ],
    stretch: [
      { q: 'I am a 5-digit number. All my digits are the same. Rounded to the nearest ten thousand, I am 60 000. Who am I?', a: '55 555 (66 666 rounds to 70 000; 44 444 rounds to 40 000).' },
      { q: 'Use the digit cards 1, 4, 6, 7 and 9 once each. Make the 5-digit number that is closest to 70 000.', a: '69 741 (259 away; the closest number above 70 000 is 71 469, which is 1469 away).' },
      { q: 'Find the rule and write the next two numbers: 17 250, 19 500, 21 750, ____, ____', a: 'Add 2250 each time: 24 000, 26 250.' },
      { q: 'How many whole numbers round to 3500 when rounded to the nearest hundred?', a: '100 (from 3450 to 3549).' },
      { q: 'A whole number rounds to 5350 to the nearest 10, AND to 5400 to the nearest 100. Find ALL the numbers it could be.', a: '5350, 5351, 5352, 5353, 5354 (5 numbers). To the nearest 10 it is 5345 to 5354; to the nearest 100 it is 5350 to 5449; both: 5350 to 5354.' },
      { q: 'Estimate 8 × 6102 by rounding 6102 to the nearest thousand first. Is the exact answer more or less than your estimate?', a: '8 × 6000 = 48 000. More, because 6102 was rounded down (exact: 48 816).' },
      { q: 'The crowd at a concert was 38 000 when rounded to the nearest thousand. What is the smallest and the largest the crowd could have been?', a: 'Smallest 37 500 and largest 38 499 (37 499 rounds down to 37 000 and 38 500 rounds up to 39 000).' },
      { q: 'What is the largest 5-digit odd number with all its digits different that rounds to 90 000 when rounded to the nearest ten thousand?', a: '94 875. Numbers that round to 90 000 go up to 94 999. The first two digits are 9 and 4, then the biggest digits left are 8 and 7, and the ones digit must be odd, so 5 (not 6).' }
    ],
    challenge: [
      { q: 'Ali counts on in 1000s, starting at 3456. He stops at the last number below 100 000. What is the last number he says? How many numbers does he say?', a: '99 456. He says 97 numbers (3456, 4456, … 99 456).' },
      { q: 'How many whole numbers round to 45 000 to the nearest thousand AND to 50 000 to the nearest ten thousand?', a: '500. To the nearest thousand: 44 500 to 45 499. To the nearest ten thousand: 45 000 to 54 999. Both: 45 000 to 45 499.' },
      { q: 'A palindrome reads the same forwards and backwards, like 12 321. How many 5-digit palindromes are there between 40 000 and 50 000?', a: '100. They look like 4 a b a 4: 10 choices for a and 10 for b.' },
      { q: 'A 5-digit number has all its digits different, and its digits add up to 10. What is the largest it can be? What is the smallest?', a: 'Largest 43 210, smallest 10 234 (the only five different digits that add up to 10 are 0, 1, 2, 3, 4).' },
      { q: 'Find all the 5-digit palindromes that round to 50 000 when rounded to the nearest thousand.', a: '10: 49 594, 49 694, 49 794, 49 894, 49 994, 50 005, 50 105, 50 205, 50 305, 50 405.' },
      { q: 'Ben writes all the numbers from 99 990 to 100 000. How many digits does he write altogether?', a: '56. 99 990 to 99 999 is 10 numbers × 5 digits = 50, and 100 000 has 6 digits.' },
      { q: 'How many 5-digit numbers have digits that add up to 3?', a: '15. Ten thousands digit 1: the other 2 goes as 2 in one place (4 ways) or 1 and 1 in two places (6 ways): 10. Ten thousands digit 2: 4 ways. Ten thousands digit 3: 1 way (30 000). 10 + 4 + 1 = 15.' },
      { q: 'Make up your own number riddle about a 5-digit number. Use a rounding clue, a clue about the digits and an odd-or-even clue, so that exactly ONE number fits. Check your riddle: list every number that fits the rounding clue, then cross out the ones that break the other clues. Swap riddles with a partner.', a: 'Riddles will vary. Check that the rounding clue gives the right range and that only one number is left. Model riddle: "Rounded to the nearest thousand I am 30 000. All my digits are different. My digits add up to 12. I am odd." The only number is 30 261.' },
      { q: 'The distance counter on Mr Tan’s car shows 39 993 km. This number is a palindrome: it reads the same forwards and backwards. What is the next palindrome the counter will show? How many more kilometres is that?', a: '40 004, which is 11 km more.' }
    ]
  },

  workbook: H => {
    const W = [];
    W.push(H.q(1, 'Round each number. Draw a number line if it helps.', { before: 40, keepNext: true }));
    W.push(H.tbl([2475, 2475, 2475, 2475], [
      H.row(['Number', 'to the nearest 10', 'to the nearest 100', 'to the nearest 1000'].map(s => H.cell(s, 2475, { bold: true, fill: 'EDEDED', h: 30 }))),
      ...['47 285', '63 950'].map(n => H.row([H.cell(n, 2475, { bold: true, h: 50 }), H.cell('', 2475, { h: 50 }), H.cell('', 2475, { h: 50 }), H.cell('', 2475, { h: 50 })]))
    ]));
    W.push(H.fig(FG.numberLine({ min: 47000, max: 48000, major: 500, minor: 100, fmt: v => String(v).replace(/(\d)(\d{3})$/, '$1 $2'), size: 18, label: 'A number line from 47 000 to 48 000 with ticks every 100 and 47 500 labelled, for marking 47 285.' })));
    W.push(H.sub('', 'Mark 47 285 on the line with an X. Which thousand is it closer to?  ________'));
    W.push(H.gap(40));
    W.push(H.sub('', 'Try next, if you have time:   9049  →  ________  ________  ________        80 503  →  ________  ________  ________'));
    W.push(H.q(2, 'Work backwards.', { keepNext: true }));
    W.push(H.sub('a', 'The number of people at a concert is 63 000 when rounded to the nearest thousand. What is the smallest and the largest number of people there could be?', { keepNext: true }));
    W.push(H.fig(lineSvg()));
    W.push(tip('63 500 is halfway between 63 000 and 64 000. Does it round up or down?  ____________'));
    W.push(H.sub('', 'Smallest:  ____________          Largest:  ____________'));
    W.push(H.sub('b', 'A whole number rounds to 5350 to the nearest 10. Find ALL the numbers it could be. Start at 5340 and check each one.', { keepNext: true }));
    W.push(tip('5345 is halfway between 5340 and 5350. Does 5345 round up or down? What about 5344?  ____________'));
    W.push(H.ans('Numbers:'));
    W.push(H.q(3, 'A bakery bakes 4982 buns every day for 6 days.', { keepNext: true }));
    W.push(H.sub('a', 'Round 4982 to the nearest thousand and estimate the total.   Estimate:  ____________'));
    W.push(H.sub('b', 'Is the exact total more or less than your estimate? How do you know without working it out?'));
    W.push(...H.lines(1));
    W.push(H.sub('c', 'Work out the exact total.   Exact total:  ____________'));

    W.push(H.q(4, 'Number riddles. Who am I?', { pb: true, before: 0, keepNext: true }));
    W.push(H.sub('a', 'I am a 5-digit number. Rounded to the nearest thousand, I am 48 000. My hundreds digit is 6. My ones digit is 1 and my tens digit is double my ones digit.', { keepNext: true }));
    W.push(H.sub('', 'Hint: the numbers that round to 48 000 are from 47 500 to 48 499. Which of them have 6 in the hundreds place?', { keepNext: true }));
    W.push(H.ans('I am:'));
    W.push(H.sub('b', 'I am a 5-digit number. My digits add up to 2. Find ALL the numbers I could be. List them in order.', { keepNext: true }));
    W.push(tip('the digits are two 1s (and zeros) or one 2 (and zeros). The first digit cannot be 0. Write 20 000 and 10 001, then move the digits around.'));
    W.push(...H.lines(2));
    W.push(H.ans('How many numbers?'));
    W.push(H.q(5, 'Find the rule. Write the next numbers.', { keepNext: true }));
    W.push(H.sub('a', '23 450,   24 450,   25 450,   ________,   ________'));
    W.push(H.sub('b', '81 300,   79 800,   78 300,   ________,   ________'));
    W.push(H.sub('c', '99 950,   99 960,   99 970,   99 980,   ________,   ________'));
    W.push(H.sub('d', '12 500,   15 000,   17 500,   20 000 …   What is the first number in this pattern that is more than 30 000?   ________'));
    W.push(H.q(6, 'Use the digit cards 0, 3, 5, 6 and 8 once each to make a 5-digit number.', { keepNext: true }));
    W.push(H.fig(cardsSvg([0, 3, 5, 6, 8], 'Digit cards 0, 3, 5, 6 and 8')));
    W.push(H.sub('a', 'The largest even number:  ____________'));
    W.push(H.sub('b', 'The smallest odd number:  ____________'));
    W.push(H.sub('c', 'The number closest to 60 000:  ____________'));
    return W;
  }
};

// ---- close_gaps + fix pass: sneak-peek puzzles, Investigation (with an easy first step), Looking back, Go further (docs/audit/close_gaps_p4.md, fixpass_p4.md)
module.exports.gaps = {
 "idea": "rounding",
 "check": [
  {
   "q": "Draw a number line from 7 000 to 8 000. Put a dot at 7 500, halfway. Then put a dot at 7 200. Is the 7 200 dot nearer to 7 000 or to 8 000?",
   "a": "Nearer to 7 000. 7 200 is only 200 from 7 000 but 800 from 8 000, and it is left of the halfway dot 7 500.",
   "s": "Nearer to 7 000: it is only 200 away, not 800.",
   "kind": "access"
  },
  {
   "q": "A shop says \"about 8 000 people came\" (rounded to the nearest thousand). Which of these could be the real number: 7 499, 7 500, 8 499, 8 500? Hint: draw a number line from 7 000 to 9 000.",
   "a": "7 500 and 8 499. The real number is from 7 500 to 8 499 (7 499 rounds down to 7 000; 8 500 rounds up to 9 000).",
   "s": "7 500 and 8 499.",
   "kind": "think"
  }
 ],
 "why": "Find the two round numbers and the halfway mark. Halfway or more rounds up.",
 "invest": {
  "kind": "Is it always true? Test and explain.",
  "head": "Double rounding",
  "intro": "Mei says: \"If I round a number to the nearest hundred, and then round that answer to the nearest thousand, I always get the same answer as rounding to the nearest thousand straight away.\"",
  "parts": [
   "Test Mei's idea on at least 5 numbers. Show each test on the lines (number, nearest hundred, then nearest thousand, and straight to the nearest thousand). Include 3 280, 1 449 and 1 450.",
   "Is Mei always right? If not, write one number that breaks her idea.",
   "Look at the numbers that break it. What do their last three digits have in common?"
  ],
  "lines": 5,
  "key": "Mei is not always right. 3 280 gives 3 300 then 3 000, and straight to 3 000: the same. 1 449 gives 1 400 then 1 000, and straight to 1 000: the same. 1 450 gives 1 500 then 2 000, but straight to the nearest thousand it is 1 000: different. Every number whose last three digits are 450 to 499 breaks the idea (checked by brute force for every whole number below 100 000). Why: rounding to the nearest hundred first turns a number just BELOW the halfway mark into exactly the halfway mark, which then rounds up. Look for children who test numbers near the halfway mark instead of only easy numbers, and who say \"I tested ...\" before they say \"I think ...\".",
  "easy": "Round 3 280 to the nearest hundred. Then round your answer to the nearest thousand. Now round 3 280 straight to the nearest thousand. Did you get the same answer both ways?"
 },
 "reflect": "Something I did well: I drew the number line. The hardest part was working out which way a number like 450 rounds. What helped me: marking the halfway point on the number line. One thing I could try next: a number line for every rounding question.",
 "go2": {
  "q": "Which number you can make is closest to 70 000? Why can you not make 70 000?",
  "a": "72 459 (2 459 away). 70 000 needs a 0 card and there is none; with the cards 2, 4, 5, 7 and 9 the closest below is 59 742 (10 258 away)."
 },
 "cap": "Page 2 is on your own. Do question 3 first, then Q4a, Q5 and Q6a. The rest is a choice for the end.",
 "p1": "Pairs: Q1 and Q2. Then Q3 alone. After question 3 you may choose: carry on, or try Think harder.",
 "plan": ["Pairs do Q1 and Q2 (about 10 minutes of work; Q2a and Q2b stay). Q3, the bakery question, is the first question each child does on their own at the start of page 2 time. Its answer is checked together with page 2, which takes about 30 seconds longer."]
};
