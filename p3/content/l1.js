// Math Inquirers P3, Lesson 1: Number Sleuths (Numbers to 10 000)
// Heuristics taught: make a list in order; look for a pattern.
const N = '#1B2A49', Y = '#FFC93C', SKY = '#DDEBF7', T = '#1F7A6F', W = '#FFFFFF';

// a row of digit cards (workbook figure)
const cardsSvg = (ds, maxw = 250) => {
  const w = 76, g = 16, tot = ds.length * w + (ds.length - 1) * g, x0 = (600 - tot) / 2;
  let s = `<svg aria-label="Digit cards ${ds.join(', ')}" viewBox="0 0 600 104" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:${maxw}px">`;
  ds.forEach((d, i) => {
    const x = x0 + i * (w + g);
    s += `<rect x="${x}" y="6" width="${w}" height="92" rx="12" fill="${Y}" stroke="${N}" stroke-width="3"/>` +
      `<text x="${x + w / 2}" y="70" font-size="50" font-weight="700" text-anchor="middle" fill="${N}" font-family="Fredoka, Arial">${d}</text>`;
  });
  return s + '</svg>';
};

module.exports = {
  lesson: {
    n: 1, week: 1, session: 'A',
    title: 'Number Sleuths',
    topic: 'Numbers to 10 000',
    objective: 'Read and build 4-digit numbers by place value; make the greatest, smallest, odd, even and closest numbers from digit cards; list every number in order; solve clue puzzles and continue number patterns.',
    skills: 'Place value to 10 000, renaming (15 hundreds = 1 thousand 5 hundreds), making a list in order, looking for a pattern, using clues one at a time, explaining "I have them all"',
    materials: 'Digit cards 0–9 (two sets per child), a place value mat (Th H T O), mini whiteboards, a 10-sided die or a bag of digit cards 0–9 for the warm-up game.',
    online: 'Children cut out the digit cards at the back of the workbook (or write 0–9 on small paper squares) and draw a Th H T O mat on paper. The tutor draws the digits on camera.',
    warmup: 'Biggest number wins: the tutor draws four digits one at a time; children write each one in Th, H, T or O straight away and cannot move it. The biggest number scores a point. Then play for the smallest.',
    explore: 'Pairs use the cards 2, 4, 6 and 8 to make every 4-digit number between 4000 and 6000, then find the one closest to 5000.',
    mini: 'Greatest and smallest: decide the thousands digit first (0 can never go first). Odd or even: choose the ones digit first. Closest: check the nearest number above and the nearest below. Make a list in order: fix the first digit, then list the rest from smallest.',
    share: 'Mei says the smallest 4-digit number she can make with 3, 0, 7, 5 is 0357. Do you agree?',
    exit: { q: 'Use the cards 6, 0, 3, 8 once each. Write the smallest 4-digit number and the greatest odd 4-digit number.', a: 'Smallest: 3068. Greatest odd: 8603 (3 is the only odd card, so it goes in the ones place).' },
    mistakes: [
      'Putting 0 first for the smallest number (0357 is really 357, a 3-digit number).',
      'For the greatest odd number, making the greatest number first and then trying to fix it, instead of choosing the ones digit first.',
      'Listing numbers in a random order, so some are missed or written twice (especially with the two 5s in Q2).'
    ],
    extension: 'With the cards 1, 2, 3, 4, how many 4-digit numbers can you make? How many of them are odd? (24 numbers; 12 are odd, because 6 end in 1 and 6 end in 3.)',
    key: [
      ['Q1', '(a) 7530  (b) 3057  (c) 7503  (d) 5037  (e) It is only 37 away from 5000. The closest number below 5000 is 3750, which is 1250 away.'],
      ['Q2', 'Starting with 2: 2055, 2505, 2550. Starting with 5: 5025, 5052, 5205, 5250, 5502, 5520.  (a) 9 numbers  (b) 4 (5205, 5250, 5502, 5520)'],
      ['Q3', '(a) 9550, 9450 (take away 100)  (b) 4567, 5678 (add 1111)  (c) 1015, 1021 (add 1, 2, 3, 4, then 5, then 6)  (d) Yes, 5000 is in the pattern (3000 + 8 jumps of 250). The number right after it is 5250'],
      ['Q4', '(a) 5527  (b) 13 hundreds  (c) No. 23 tens is 230, so the number is 6000 + 230 = 6230.'],
      ['Q5', '(a) 6903 (thousands 6, ones 3, hundreds 6 + 0 + 3 = 9, so the tens digit must be 0)  (b) Greatest 3201, smallest 1023. The only four different digits that add up to 6 are 0, 1, 2, 3, and an odd number ends in 1 or 3.'],
      ['Q6', '10 numbers. Starting with 3: 3000. Starting with 2: 2100, 2010, 2001. Starting with 1: 1200, 1110, 1101, 1020, 1011, 1002.  (b) 1, 3 and 6 numbers: the counts go up by 2, then by 3.']
    ]
  },

  script: {
    hook: ['Welcome, Number Sleuths! Every number hides clues in its digits. Today we use the clues to find mystery numbers, build the biggest and the smallest, and prove that we have found every number.'],
    warmIntro: ['Draw a Th H T O mat. I will call out four digits, one at a time. Write each digit in a box straight away. No moving!', 'Who made the biggest number? Where did you put the 9? Why there?'],
    predict: ['With the cards 2, 4, 6 and 8, how many 4-digit numbers between 4000 and 6000 can you make? Write a guess first.'],
    exploreHints: [
      'Stuck: “Which card must go in the thousands place if the number is between 4000 and 6000?”',
      'Missing some: “Keep the 4 in front. Now change the hundreds digit in order: 2, then 6, then 8.”',
      'Ready for more: the Go further what-if on the slide (cards 2, 4, 5, 8: 12 numbers between 4000 and 6000). Or: “How many numbers can you make altogether with the four cards?” (24: six start with each card.)'
    ],
    think: [
      '“Greatest number from 4, 0, 8, 1. The thousands place is worth the most, so the biggest digit goes there: 8. Then 4, then 1, then 0: 8410.”',
      '“Smallest. I want the smallest digit first, but 0 cannot go first or it is not a 4-digit number. So 1 goes first, then 0, then 4, then 8: 1048.”',
      '“Greatest odd number from 2, 9, 6, 0. An odd number ends in an odd digit. The only odd card is 9, so I put 9 in the ones place FIRST. Then the biggest of the rest, in order: 6, 2, 0. So 6209.”',
      '“3-digit numbers from 0, 3, 6. I fix the first digit: 3. Then 306, 360. Next first digit: 6. Then 603, 630. 0 cannot go first. So there are 4 numbers, and my list shows I have them all.”'
    ],
    circulate: ['Ask: “Which place is worth the most?”', 'Ask: “Where does the odd digit of an odd number go?”', 'Ask: “How do you know your list has every number?”'],
    hints: ['Hint 1: “Decide the thousands digit first.”', 'Hint 2: “For odd or even, decide the ones digit first.”', 'Hint 3: “Make a list: fix the first digit, then go in order from smallest.”'],
    talk: ['“Is 0357 a 4-digit number?”', '“How do you know you found ALL the numbers in your list?”'],
    talkAns: 'No. 0357 is really 357, a 3-digit number, so the smallest 4-digit number is 3057. We know a list is complete because we fixed the first digit and listed the rest in order from smallest, so nothing is missed or repeated.',
    close: ['“Sleuths use every clue and check every case. Today you made lists in order and proved you had them all.”']
  },

  deck: {
    today: 'Build 4-digit numbers, make the greatest and smallest, list every number in order and crack clue puzzles.',
    warmGame: 'Biggest number wins. Draw four digits one at a time; children place each in Th, H, T or O straight away and cannot move it. Biggest number scores. Then play for the smallest.',
    warmQs: [['What is the value of the 7 in 4719?', '700'], ['3000 + 40 + 5 = ?', '3045'], ['What is 1 more than 4999?', '5000'], ['What is 100 less than 6050?', '5950'], ['Which is greater: 7089 or 7098?', '7098']],
    expSetup: ['Take the cards 2, 4, 6 and 8.', 'Make 4-digit numbers between 4000 and 6000.', 'Write each one on your whiteboard.', 'Which one is closest to 5000?'],
    expPic: 'digit cards 2, 4, 6, 8 above a number line from 4000 to 6000 with 5000 marked.',
    expAsk: [
      ['How many numbers did you make?', '6: 4268, 4286, 4628, 4682, 4826, 4862.'],
      ['How do you know you have them all?', 'Every one must start with 4. Then list in order: hundreds digit 2, 6, 8, with two numbers each.'],
      ['Which is closest to 5000?', '4862, only 138 away. The nearest number above 5000 is 6248, which is 1248 away.']
    ],
    mini1: { head: 'Greatest and smallest with 4, 0, 8, 1', body: ['Greatest: biggest digit in the thousands place, then the next biggest.', 'Smallest: the smallest digit that is not 0 goes first, then 0.'], ans: '8410 and 1048.' },
    mini2: { head: 'Make a list in order: 3-digit numbers from 0, 3, 6', body: ['Fix the first digit: 3, then 6 (never 0).', 'For each, list the rest from smallest.'], ans: '4 numbers: 306, 360, 603, 630.' },
    keyHead: 'Key idea: start at the biggest place',
    keyBig: 'Decide the thousands digit first. To find every number, fix the first digit and list the rest in order.',
    keySmall: 'Odd or even? Choose the ones digit first.',
    brk: 'Place value moves. The tutor says a 4-digit number: jump for each thousand, clap for each hundred, tap your knees for each ten, touch your toes for each one.',
    ws1: 'Page 1, in pairs: Q1 cards 3, 0, 7, 5; Q2 every number from 2, 0, 5, 5; Q3 patterns.',
    ws2: 'Page 2, on your own: Q4 place value puzzles; Q5(a) what number am I?; then Q5(b) and Q6 (digits that add up to 3) if you have time.'
  },

  qbank: {
    core: [
      { q: 'Write the number. Think of 6 big boxes of 1000 sweets, 4 packets of 10 sweets and 9 loose sweets. (There are no boxes of 100.)', a: '6049' },
      { q: 'Look at the place value chart:  Th 2 | H 8 | T 3 | O 7.  This is the number 2837. How much is the digit 8 worth?', a: '800' },
      { q: 'Use the cards 9, 1, 4, 6 once each. Make the smallest 4-digit number.', a: '1469' },
      { q: 'What number is 10 less than 5003?', a: '4993' },
      { q: 'Continue the pattern: 7250, 7500, 7750, ___, ___', a: '8000, 8250 (add 250)' },
      { q: 'Order from smallest to greatest: 4089, 4809, 4098, 4890', a: '4089, 4098, 4809, 4890' }
    ],
    stretch: [
      { q: 'Use the cards 5, 0, 8, 2 once each. Make the greatest even number and the smallest odd number.', a: 'Greatest even: 8520. Smallest odd: 2085 (5 is the only odd card, so it goes last).' },
      { q: 'How many 4-digit numbers can you make with the cards 1, 1, 0, 0? List them.', a: '3 numbers: 1001, 1010, 1100.' },
      { q: 'A number has 7 thousands, 13 hundreds and 6 ones. What is the number?', a: '8306 (7000 + 1300 + 6)' },
      { q: 'I am between 5000 and 6000. My hundreds, tens and ones digits are all the same. My digits add up to 11. What number am I?', a: '5222 (5 + 2 + 2 + 2 = 11)' },
      { q: 'What is the smallest 4-digit number with all different digits that add up to 10?', a: '1027 (start 1, 0; the last two digits must add to 9 and cannot be 0 or 1, so 2 and 7)' },
      { q: 'How many times do you write the digit 5 when you write all the numbers from 1 to 100?', a: '20 (ten times in the ones place: 5, 15, …, 95; ten times in the tens place: 50 to 59)' },
      { q: 'Continue the pattern: 1, 3, 7, 15, 31, ___, ___', a: '63, 127 (double and add 1; the jumps are 2, 4, 8, 16, 32, 64)' },
      { q: 'How many 4-digit numbers between 3000 and 4000 read the same forwards and backwards, like 3443?', a: '10 (3003, 3113, 3223, …, 3993)' }
    ],
    challenge: [
      { q: 'Ali writes a 4-digit number using only odd digits, all different. It is as close to 5000 as possible. What is it?', a: '5137 (137 more than 5000). The closest below 5000 is 3975, which is 1025 less.' },
      { q: 'A pattern starts at 1000 and goes up by 7 each time: 1000, 1007, 1014, … Is 1100 in the pattern? Explain.', a: 'No. 14 jumps of 7 is 98, so 1098 is in the pattern. The next number is 1105, so 1100 is skipped.' },
      { q: 'How many digits are needed to number the pages of a book from page 1 to page 120?', a: '252 digits: pages 1–9 use 9, pages 10–99 use 90 × 2 = 180, pages 100–120 use 21 × 3 = 63.' },
      { q: '4-digit numbers whose digits add up to 3 can be counted by their first digit: 1, 3, 6. Count the ones whose digits add up to 4 by their first digit too. Use the pattern to predict how many 4-digit numbers have digits that add up to 5, and check by listing the ones that start with 4.', a: 'Digit sum 4: 1, 3, 6, 10 (20 numbers altogether). Digit sum 5: the counts by first digit (5, 4, 3, 2, 1) are 1, 3, 6, 10, 15, so 35 numbers altogether. Check: the numbers that start with 4 are 4100, 4010 and 4001 (3 numbers).' },
      { q: 'I am an even 4-digit number with all different digits. My thousands digit is 4 more than my ones digit. My hundreds digit is double my tens digit. My digits add up to 20. What number am I?', a: '6842 (6 = 2 + 4, 8 = 2 × 4, 6 + 8 + 4 + 2 = 20). It is the only one.' },
      { q: 'Mei makes 3-digit numbers using any three of the cards 2, 4, 6, 8. How many different numbers can she make?', a: '24 (6 numbers start with each card: for 2, the numbers are 246, 248, 264, 268, 284, 286)' },
      { q: 'Make up your own "What number am I?" puzzle. Choose a secret 4-digit number and write 3 or 4 clues about its digits. Check that ONLY ONE number fits all your clues. Then swap with a partner.', a: 'Answers vary. Check that every clue is true for the secret number and that the clues together leave only one number (list the numbers that fit clue 1, then cross out with clue 2, and so on). Example: "I am between 4000 and 5000. My hundreds digit is 1 less than my thousands digit. My ones digit is 3 times my tens digit. My digits add up to 15." The only number is 4326.' },
      { q: 'A 4-digit number has all different digits. Its thousands digit is the sum of its other three digits. What is the greatest such number? What is the smallest?', a: 'Greatest 9810 (9 = 8 + 1 + 0). Smallest 3012 (the smallest sum of three different digits is 0 + 1 + 2 = 3).' },
      { q: 'Mei uses the cards 1, 2, 3, 4 once each to make 4-digit numbers. She lists them all from smallest to greatest. What is the 10th number in her list?', a: '2341. Six numbers start with 1; then 2134 (7th), 2143 (8th), 2314 (9th), 2341 (10th).' }
    ]
  },

  workbook: H => [
    H.p('Digit cards: use each card once in each number. A 4-digit number cannot start with 0.', { after: 80 }),
    H.q(1, 'Use these digit cards once each to make 4-digit numbers.', { before: 40, keepNext: true }),
    H.fig(cardsSvg(['3', '0', '7', '5'])),
    H.sub('a', 'The greatest number:   ______________'),
    H.sub('b', 'The smallest number:   ______________'),
    H.sub('c', 'The greatest ODD number:   ______________'),
    H.sub('d', 'The number closest to 5000:   ______________'),
    H.sub('e', 'Why is (d) the closest?   It is only ________ away from 5000.'),
    H.q(2, 'Make a list in order. Write ALL the 4-digit numbers you can make with the cards  2,  0,  5,  5.  Start with the smallest.', { keepNext: true }),
    H.tbl([2400, 7500], [
      H.row([H.cell('Starting with 2', 2400, { bold: true, fill: 'EDEDED', h: 110 }), H.cell('', 7500)]),
      H.row([H.cell('Starting with 5', 2400, { bold: true, fill: 'EDEDED', h: 110 }), H.cell('', 7500)])
    ]),
    H.gap(20),
    H.sub('a', 'How many numbers did you find?   ______'),
    H.sub('b', 'How many of them are greater than 5200?   ______'),
    H.q(3, 'Look for a pattern. Write the next two numbers.', { keepNext: true }),
    H.sub('a', '9850,   9750,   9650,   ________,   ________'),
    H.sub('b', '1234,   2345,   3456,   ________,   ________'),
    H.sub('c', '1000,   1001,   1003,   1006,   1010,   ________,   ________'),
    H.sub('d', '3000,  3250,  3500,  3750,  …   Keep going. Will 5000 be in the pattern?  ________   Which number comes right after 5000?  ________'),

    H.q(4, 'Place value puzzles.', { pb: true, before: 0, keepNext: true }),
    H.p('Hint: 10 hundreds make 1 thousand. You can draw a box for each thousand, hundred, ten and one.', { after: 40 }),
    H.sub('a', '4 thousands, 15 hundreds, 2 tens and 7 ones make   ____________'),
    H.sub('b', '7305  =  6 thousands  +  ______ hundreds  +  5 ones'),
    H.sub('c', 'Mei says that 6 thousands, 0 hundreds and 23 tens is 6023. Is she right? Explain.'),
    ...H.lines(2),
    H.q(5, 'What number am I? Use one clue at a time.', { keepNext: true }),
    H.sub('a', 'Read the clues.', { keepNext: true }),
    H.tbl([9900], [H.row([H.cell(['Clue 1:  I am between 6000 and 7000.', 'Clue 2:  My ones digit is half of my thousands digit.', 'Clue 3:  My hundreds digit is the sum of my other three digits.'], 9900, { align: 'left', fill: 'EDEDED', h: 90 })])]),
    H.ans('I am:'),
    H.sub('b', '(if time) I am a 4-digit ODD number. All my digits are different. My digits add up to 6. What is the greatest number I can be? What is the smallest?'),
    H.ans('Greatest:'),
    H.ans('Smallest:'),
    H.q(6, '(if time) How many 4-digit numbers have digits that add up to 3? Make a list in order. Start with the biggest thousands digit.', { keepNext: true }),
    H.tbl([2400, 7500], [
      H.row([H.cell('Thousands digit 3', 2400, { bold: true, fill: 'EDEDED', h: 120 }), H.cell('', 7500)]),
      H.row([H.cell('Thousands digit 2', 2400, { bold: true, fill: 'EDEDED', h: 120 }), H.cell('', 7500)]),
      H.row([H.cell('Thousands digit 1', 2400, { bold: true, fill: 'EDEDED', h: 120 }), H.cell('', 7500)])
    ]),
    H.gap(40),
    H.sub('a', 'How many numbers altogether?   ______'),
    H.sub('b', 'How many start with 3? With 2? With 1? What do you notice?'),
    ...H.lines(1)
  ]
};
