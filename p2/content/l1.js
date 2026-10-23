// Math Inquirers P2 Holiday Program — Lesson 1: Digit Detectives (Numbers to 1000)
const N = '#1B2A49', Y = '#FFC93C', SKY = '#DDEBF7', TEAL = '#1F7A6F', RED = '#D64545', WH = '#FFFFFF';
const F = 'Fredoka, Arial, sans-serif';

// a row of digit cards (workbook drawing)
const cardsSvg = (digits, label) => {
  const w = 70, g = 22, tot = digits.length * w + (digits.length - 1) * g, x0 = (600 - tot) / 2;
  let s = `<svg aria-label="${label}" viewBox="0 0 600 110" width="600" xmlns="http://www.w3.org/2000/svg" style="max-width:100%">`;
  digits.forEach((d, i) => {
    const x = x0 + i * (w + g);
    s += `<rect x="${x}" y="8" width="${w}" height="92" rx="12" fill="${Y}" stroke="${N}" stroke-width="3"/>` +
      `<text x="${x + w / 2}" y="72" font-size="50" font-weight="700" text-anchor="middle" fill="${N}" font-family="${F}">${d}</text>`;
  });
  return s + '</svg>';
};

// pieces of a 1000 chart (rows of 10): cells = [col,row,text]
const pieceSvg = () => {
  const c = 74, h = 50;
  const cellAt = (ox, oy, col, row, txt) => {
    const x = ox + col * c, y = oy + row * h;
    return `<rect x="${x}" y="${y}" width="${c}" height="${h}" fill="${txt ? SKY : WH}" stroke="${N}" stroke-width="3"/>` +
      (txt ? `<text x="${x + c / 2}" y="${y + 33}" font-size="22" font-weight="700" text-anchor="middle" fill="${N}" font-family="${F}">${txt}</text>` : '');
  };
  let s = `<svg aria-label="Two pieces of a 1000 chart" viewBox="0 0 600 200" width="600" xmlns="http://www.w3.org/2000/svg" style="max-width:100%">`;
  s += `<text x="40" y="26" font-size="20" font-weight="700" fill="${TEAL}" font-family="${F}">Piece A</text>`;
  const A = [['347', '', ''], ['', '358', ''], ['', '', '369']];
  A.forEach((r, ri) => r.forEach((t, ci) => { s += cellAt(40, 40, ci, ri, t); }));
  s += `<text x="350" y="26" font-size="20" font-weight="700" fill="${TEAL}" font-family="${F}">Piece B</text>`;
  [[1, 0, '586'], [0, 1, ''], [1, 1, ''], [2, 1, ''], [1, 2, '']].forEach(([ci, ri, t]) => { s += cellAt(350, 40, ci, ri, t); });
  return s + '</svg>';
};

module.exports = {
  lesson: {
    n: 1, week: 1, session: 'A', title: 'Digit Detectives', topic: 'Numbers to 1000',
    objective: 'Read and build 3-digit numbers by place value (also with more than 9 tens), make every number from a set of digit cards by listing in order, find the biggest and smallest, and use patterns on a 1000 chart to count on and back in 1s, 10s and 100s.',
    skills: 'Place value, making a list in order, looking for a pattern, reasoning about zero',
    materials: 'Digit cards 0 to 9 (one set per child), place-value mat (hundreds, tens, ones), base-ten blocks or paper strips and squares, mini whiteboards, the 1000-chart pieces on the workbook page (rows of 10).',
    online: 'Children cut out paper digit cards before the lesson and move them on camera; the tutor writes on the slide 1000-chart pieces.',
    warmup: 'Place It Right: the tutor draws digit cards one at a time. After each card, children must write it in the hundreds, tens or ones box straight away and cannot move it. Biggest number wins. Then play again for the smallest.',
    explore: 'Pairs take the digit cards 3, 5 and 8 and make every 3-digit number they can, using each card once. They record each number, then find the biggest and the smallest and decide how they know they have found them all.',
    mini: 'Place value: 5 hundreds, 12 tens and 4 ones is 500 + 120 + 4 = 624. Make a list in order: fix the hundreds digit, then swap the other two (1, 6, 9 gives 169, 196, 619, 691, 916, 961). Biggest: biggest digit in the hundreds place. Zero can never be the hundreds digit. Before page 2: on a 1000 chart one square right is 1 more, one square down is 10 more; count on and back across a hundred (608, 598, 588); solve a digit riddle by listing the tens and ones that fit.',
    share: 'Which is bigger, 401 or 399? Ali says 399 because it has two 9s. Who is right, and why?',
    exit: { q: 'Use the digit cards 6, 0 and 2 once each. Write the biggest and the smallest 3-digit number.', a: 'Biggest 620, smallest 206.' },
    mistakes: [
      'Writing 6 hundreds, 15 tens and 2 ones as 6152 instead of regrouping 15 tens as 1 hundred and 5 tens (752).',
      'Listing digit-card numbers at random, so one is missed or written twice, or counting 059 as a 3-digit number.',
      'Counting back in 10s across a hundred: 512, 502, 592 instead of 512, 502, 492.'
    ],
    takehome: 'Page 2: Q4(b) (two squares below 385) and the whole of Q5 (count on and back, four items). The teaching slide for counting past a hundred is not shown in class.',
    extension: 'Use any three of the cards 1, 3, 5 and 7. How many different 3-digit numbers can you make? (24: 6 for each set of three cards, and there are 4 sets.)',
    key: [
      ['Q1', '(a) 407  (b) 752  (c) 3 tens; 13 tens  (d) 70'],
      ['Q2', '(a) Start with 2: 247, 274. Start with 4: 427, 472. Start with 7: 724, 742.  (b) Biggest 742, smallest 247  (c) 472 (only 28 away from 500)  (d) 2 odd numbers: 247 and 427'],
      ['Q3', '(a) 509, 590, 905, 950  (b) 0 cannot be the hundreds digit (059 is not a 3-digit number), so only 5 or 9 can start: 2 + 2 = 4 numbers, not 6.'],
      ['Q4', 'Piece A: 348, 349 / 357, 359 / 367, 368.  Piece B: 595, 596, 597 in the middle row and 606 at the bottom.  (a) Down: 10 more. Right: 1 more.  (b) 405 (395, then 405)'],
      ['Q5', '(a) 347, 447  (b) 502, 492  (c) 1000  (d) 700, 699'],
      ['Q6', '(a) 435  (b) 6 numbers: 102, 111, 120, 201, 210, 300']
    ]
  },

  script: {
    hook: ['Welcome, Digit Detectives! Every 3-digit number is made of just three digits, but WHERE a digit sits changes everything.', 'Today we find every number hiding in a set of digit cards, and we make sure we do not miss any. Notice it. Test it. Explain why.'],
    warmIntro: ['Draw three boxes on your whiteboard: hundreds, tens, ones. I will turn over one digit card at a time. As soon as you see it, write it in a box. No moving it later!', 'Try to make the BIGGEST number. Where will you put a 9? Where will you put a 1? Why?'],
    predict: ['You have the cards 3, 5 and 8. How many different 3-digit numbers do you think you can make with them? Write your guess in the corner of your whiteboard.'],
    exploreHints: ['Stuck: put the 3 in the hundreds place first. What can the other two cards do?', 'Not sure if you have them all: “How many numbers start with 3? With 5? With 8?”', 'Finished early: add a 0 card and make numbers with 0, 3 and 5. Why are there fewer?'],
    think: [
      '“5 hundreds, 12 tens and 4 ones. 12 tens is 120, so the number is 500 + 120 + 4 = 624. I can also see it as 6 hundreds, 2 tens, 4 ones, because 10 of the tens make another hundred.”',
      '“Cards 1, 6 and 9. I keep the hundreds digit the same and swap the other two. 1 first: 169, 196. 6 first: 619, 691. 9 first: 916, 961. Each card starts 2 numbers, and 3 cards make 6 numbers. That is how I know I have them all.”',
      '“The biggest number has the biggest digit in the hundreds place: 961. The smallest has the smallest digit in the hundreds place: 169. But zero can never go first: 036 would be just 36 (thirty-six), which has only 2 digits, so it is not a 3-digit number.”'
    ],
    circulate: ['Ask: “How many of your numbers start with this card? Is that all of them?”', 'Ask: “What is this digit worth? How many tens is that?”', 'Ask: “Point to the number one square below this one on the chart. How much bigger is it?”'],
    hints: ['Hint 1: “Fix the hundreds digit first.”', 'Hint 2: “Build it with blocks: hundreds, tens and ones. Can 10 tens become a hundred?”', 'Hint 3: “Say the numbers out loud as you count on in 10s. What happens after 590?”'],
    talk: ['“Which is bigger, 401 or 399? Ali says 399 because it has two 9s. Who agrees?”'],
    talkAns: '401 is bigger. Compare the hundreds first: 4 hundreds is more than 3 hundreds, so the tens and ones do not matter. Count on from 399: 400, 401.',
    close: ['“You were real detectives today: you made a list in order, so no number could hide from you.”', '“Hand me your exit ticket and I will stamp your inquiry journal.”']
  },

  deck: {
    today: 'Build 3-digit numbers, find every number from digit cards by listing in order, and spot patterns on a 1000 chart.',
    warmGame: 'Place It Right. The tutor turns over digit cards one at a time. Write each one in the hundreds, tens or ones box straight away. No moving! Biggest number wins.',
    warmQs: [['4 hundreds, 6 tens, 2 ones = ?', '462'], ['What is the 8 worth in 384?', '80'], ['10 more than 296?', '306'], ['100 less than 405?', '305'], ['The biggest 3-digit number?', '999']],
    expSetup: ['Take the digit cards 3, 5 and 8.', 'Make a 3-digit number using each card once. Write it down.', 'Make as many different numbers as you can.', 'Circle the biggest and the smallest. Have you got them all?'],
    expPic: 'three yellow digit cards 3, 5 and 8 above three boxes labelled H, T and O.',
    expAsk: [['How many numbers did you make?', '6: 358, 385, 538, 583, 835, 853.'], ['How do you know you have them all?', 'List in order: each card starts 2 numbers, and 3 × 2 = 6.'], ['Which is the biggest? The smallest?', '853 and 358: put the biggest digit first for the biggest.']],
    mini1: { head: 'Place value: more than 9 tens', body: ['5 hundreds, 12 tens and 4 ones.', '12 tens = 120.', '500 + 120 + 4 = ?'], ans: '624. Ten of the tens make another hundred.' },
    mini2: { head: 'Every number from 1, 6, 9', body: ['Fix the hundreds digit, then swap the other two.', '1 first: 169, 196. 6 first: 619, 691. 9 first: 916, 961.', 'How many? Which is biggest?'], ans: '6 numbers. Biggest 961, smallest 169.' },
    keyHead: 'Key idea: list in order', keyBig: 'Fix the hundreds digit, then swap the others. Each card starts the same number of numbers.', keySmall: 'Zero can never be the hundreds digit. Biggest digit first makes the biggest number.',
    brk: 'Swap the digits. Each child puts three digit cards in a row (hundreds, tens, ones). The tutor calls “swap the hundreds and the tens” or “swap the tens and the ones”. Say your new number together on three. Is it bigger or smaller?',
    ws1: 'Page 1, in pairs: Q1 place value, Q2 the cards 2, 7, 4, Q3 the cards with a zero.',
    ws2: 'Page 2, on your own: Q4 chart pieces, Q5 count on and back, Q6 digit riddles.'
  },

  qbank: {
    core: [
      { q: 'What number is 5 hundreds, 3 tens and 8 ones?', a: '538' },
      { q: 'In 914, what is the digit 1 worth?', a: '10 (1 ten)' },
      { q: 'What number is 100 more than 457?', a: '557' },
      { q: 'What number is 10 less than 603?', a: '593' },
      { q: 'Use the digit cards 3, 6 and 1 once each. Make the biggest 3-digit number.', a: '631' },
      { q: 'Put these numbers in order, smallest first: 409, 490, 94, 940.', a: '94, 409, 490, 940' }
    ],
    stretch: [
      { q: 'Use the digit cards 2, 6 and 9 once each. Make a list in order of every 3-digit number you can make that is bigger than 500. How do you know you have found them all?', a: '4 numbers: 629, 692, 926, 962. The hundreds digit must be 6 or 9 (a number that starts with 2 is smaller than 500). With 6 in the hundreds, the other two cards make 629 and 692; with 9 in the hundreds, they make 926 and 962.' },
      { q: 'Use the digit cards 4, 4 and 7. How many different 3-digit numbers can you make? Why is it not 6?', a: '3 numbers: 447, 474, 744. The two 4s look the same, so swapping them does not make a new number.' },
      { q: 'Ali has 46 ten-blocks. Siti has 3 hundred-blocks and 15 ten-blocks. Who has the bigger number? How much bigger?', a: 'Ali: 46 tens is 460. Siti: 3 hundreds and 15 tens is 300 + 150 = 450. Ali has the bigger number, by 10.' },
      { q: 'Mei says: “If I swap the tens digit and the ones digit of a 3-digit number, the new number is always smaller.” Is she right? Show what happens with some examples. When does the number stay the same?', a: 'No. 452 becomes 425, which is smaller, but 425 becomes 452, which is bigger. It gets smaller when the tens digit is bigger than the ones digit, bigger when it is smaller, and stays the same when the two digits are the same (733).' },
      { q: 'I am a 3-digit number. My digits add up to 4. Find all the numbers I could be.', a: '10 numbers: 103, 112, 121, 130, 202, 211, 220, 301, 310, 400.' },
      { q: 'Use the digit cards 2, 5 and 9 once each. Which number you can make is closest to 600?', a: '592 (only 8 away).' },
      { q: 'How many 3-digit numbers have 7 in the hundreds place and 0 in the ones place?', a: '10: 700, 710, 720, … 790.' },
      { q: 'On a 1000 chart with rows of 10, which number is directly below 495 (one square down)? Which number is directly above 501 (one square up)?', a: '505 is directly below 495. 491 is directly above 501.' }
    ],
    challenge: [
      { q: 'Use any three of the digit cards 1, 3, 5 and 7. How many different 3-digit numbers can you make?', a: '24. Leave out one card (4 choices); each set of 3 cards makes 6 numbers: 6 + 6 + 6 + 6 = 24.' },
      { q: 'How many 3-digit numbers have digits that add up to 5?', a: '15. Hundreds digit 1: 5 numbers; 2: 4; 3: 3; 4: 2; 5: 1. 5 + 4 + 3 + 2 + 1 = 15.' },
      { q: 'I am an odd 3-digit number. My three digits are all different and add up to 6. Find all the numbers I could be.', a: '6 numbers: 105, 123, 213, 231, 321, 501.' },
      { q: 'Make up your own 3-digit number riddle with three clues, so that exactly ONE number fits (use clues about the hundreds digit, the digits adding up, odd or even, double or half). Write the answer on the back. After each clue, say how many numbers still fit. Swap with a partner and solve theirs.', a: 'Open. Example: “I am between 300 and 400. My digits add up to 9. My ones digit is double my tens digit.” Clue 1 leaves 100 numbers, clue 2 leaves 7 (306, 315, 324, 333, 342, 351, 360), clue 3 leaves only 324. Check that a partner cannot find a second number that fits all the clues.' },
      { q: 'A book has pages numbered 1 to 120. How many digits are printed altogether?', a: '252. Pages 1 to 9: 9 digits. Pages 10 to 99: 90 pages × 2 = 180 digits. Pages 100 to 120: 21 pages × 3 = 63 digits. 9 + 180 + 63 = 252.' },
      { q: 'Use three DIFFERENT cards from 0, 2, 5 and 8 to make a 3-digit number. How many different numbers can you make? Why is it not 4 × 3 × 2 = 24?', a: '18. Only 2, 5 or 8 can go in the hundreds place (3 choices), then 3 cards are left for the tens (3 choices) and 2 for the ones (2 choices): 3 × 3 × 2 = 18. 24 counts numbers that start with 0 (like 025), and those are not 3-digit numbers.' },
      { q: 'Mei uses each of the digit cards 1, 2, 3, 4, 5 and 6 once to make two 3-digit numbers. She adds them. What is the smallest total she can make?', a: '381, for example 135 + 246. The smallest digits 1 and 2 go in the hundreds places, 3 and 4 in the tens, 5 and 6 in the ones: 300 + 70 + 11 = 381.' },
      { q: 'Ali counts in 5s, starting at 3: 3, 8, 13, 18 … Will he say 500? Will he say 998? Explain.', a: 'He says only numbers ending in 3 or 8. So he will not say 500, but he will say 998.' },
      { q: 'Ben writes all the numbers from 300 to 399. How many times does he write the digit 3?', a: '120. Hundreds place: 100 times. Tens place (330 to 339): 10 times. Ones place (303, 313, … 393): 10 times. 100 + 10 + 10 = 120.' }
    ]
  },

  workbook: H => {
    const W = [];
    const TH = () => H.t('★ take-home  ', { bold: true, color: '1B2A49' });
    W.push(H.p('A 3-digit number has hundreds, tens and ones. Where a digit sits tells you what it is worth.', { after: 80 }));
    W.push(H.q(1, 'Place value. Fill in the blanks.', { before: 60, keepNext: true }));
    W.push(H.sub('a', '4 hundreds, 0 tens and 7 ones  =  ________'));
    W.push(H.sub('b', '6 hundreds, 15 tens and 2 ones  =  ________'));
    W.push(H.sub('c', '830  =  8 hundreds and ____ tens        830  =  7 hundreds and ____ tens'));
    W.push(H.sub('d', 'In 572, the digit 7 is worth  ________'));
    W.push(H.q(2, 'Use the digit cards 2, 7 and 4. Use each card once to make a 3-digit number.', { keepNext: true }));
    W.push(H.fig(cardsSvg([2, 7, 4], 'Digit cards 2, 7 and 4')));
    W.push(H.sub('a', 'Make a list in order. Write every number you can make.', { keepNext: true }));
    W.push(H.tbl([3300, 3300, 3300], [
      H.row(['Start with 2', 'Start with 4', 'Start with 7'].map(s => H.cell(s, 3300, { bold: true, fill: 'EDEDED' }))),
      H.row([0, 1, 2].map(() => H.cell('______     ______', 3300, { h: 170 })))
    ]));
    W.push(H.gap(60));
    W.push(H.sub('b', 'Biggest number:  ________        Smallest number:  ________'));
    W.push(H.sub('c', 'Which of your numbers is closest to 500?  ________'));
    W.push(H.sub('d', 'How many of your numbers are odd?  ________'));
    W.push(H.q(3, 'Now use the digit cards 0, 5 and 9.', { keepNext: true }));
    W.push(H.fig(cardsSvg([0, 5, 9], 'Digit cards 0, 5 and 9')));
    W.push(H.sub('a', 'List every 3-digit number you can make, in order.'));
    W.push(H.ans('Numbers:'));
    W.push(H.sub('b', 'The cards 2, 7, 4 made 6 numbers. Why do 0, 5, 9 make fewer?'));
    W.push(...H.lines(2));

    W.push(H.q(4, 'These are pieces cut from a 1000 chart. Each row has 10 numbers. Fill in the empty squares.', { keepNext: true }));
    W.push(H.fig(pieceSvg()));
    W.push(H.sub('a', 'On the chart, one square DOWN is ______ more.  One square RIGHT is ______ more.'));
    W.push(H.sub('b', [TH(), H.t('Which number is 2 squares below 385 on the chart?  ________')]));
    W.push(H.q(5, [TH(), H.t('Look for the pattern. Fill in the next numbers.')], { keepNext: true }));
    W.push(H.sub('a', '47,   147,   247,   ______,   ______'));
    W.push(H.sub('b', '532,   522,   512,   ______,   ______'));
    W.push(H.sub('c', '980,   985,   990,   995,   ______'));
    W.push(H.sub('d', '703,   702,   701,   ______,   ______'));
    W.push(H.q(6, 'Digit riddles. Who am I?', { keepNext: true }));
    W.push(H.sub('a', 'I am a 3-digit number. My hundreds digit is 4. My ones digit is 2 more than my tens digit. My digits add up to 12.'));
    W.push(H.ans('I am:'));
    W.push(H.sub('b', 'I am a 3-digit number. My digits add up to 3. Find ALL the numbers I could be. Tip: use 3 counters. Put 1 counter in the hundreds box, then share the other 2 between the tens and the ones. Then try 2 counters in the hundreds box.'));
    W.push(...H.lines(3));
    W.push(H.ans('How many numbers?'));
    return W;
  }
};
