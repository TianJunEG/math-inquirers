// Math Inquirers P4 Holiday Program — Lesson 1: Factor Hunters (Factors and multiples)
const N = '#1B2A49', Y = '#FFC93C', SKY = '#DDEBF7', TEAL = '#1F7A6F', RED = '#D64545', WH = '#FFFFFF';
const F = 'Fredoka, Arial, sans-serif';
const txt = (x, y, s, size = 18, fill = N, anchor = 'middle', weight = 700) =>
  `<text x="${x}" y="${y}" font-size="${size}" font-weight="${weight}" text-anchor="${anchor}" fill="${fill}" font-family="${F}">${s}</text>`;

// Q2: one way to plant 40 trees (4 rows of 10)
const treesSvg = () => {
  let s = `<svg aria-label="One way: 40 trees planted in 4 rows of 10" viewBox="0 0 600 120" width="600" xmlns="http://www.w3.org/2000/svg" style="max-width:100%">`;
  for (let r = 0; r < 4; r++) for (let c = 0; c < 10; c++) {
    const x = 150 + c * 34, y = 16 + r * 24;
    s += `<circle cx="${x}" cy="${y}" r="9" fill="${TEAL}" stroke="${N}" stroke-width="2"/>`;
  }
  s += txt(90, 58, '4 rows', 16, TEAL) + txt(303, 114, '10 trees in each row', 15, TEAL);
  return s + '</svg>';
};

// Q4: bus timetable strip (minutes after 6:00)
const busSvg = () => {
  const x0 = 40, k = 4.2;
  let s = `<svg aria-label="A time line from 6:00 am to 7:00 am marked every 5 minutes" viewBox="0 0 600 120" width="600" xmlns="http://www.w3.org/2000/svg" style="max-width:100%">`;
  s += `<line x1="${x0}" y1="60" x2="${x0 + 60 * k}" y2="60" stroke="${N}" stroke-width="3"/>`;
  for (let m = 0; m <= 60; m += 5) {
    const x = x0 + m * k, big = m % 15 === 0;
    s += `<line x1="${x}" y1="${big ? 48 : 53}" x2="${x}" y2="${big ? 72 : 67}" stroke="${N}" stroke-width="${big ? 3 : 2}"/>`;
    if (m % 10 === 0 || m % 15 === 0) s += txt(x, 96, m === 0 ? '6:00' : m === 60 ? '7:00' : ':' + String(m).padStart(2, '0'), 15);
  }
  s += txt(x0 + 60 * k + 40, 66, 'am', 16, TEAL, 'start');
  return s + '</svg>';
};

module.exports = {
  lesson: {
    n: 1, week: 1, session: 'A', title: 'Factor Hunters', topic: 'Factors and multiples',
    objective: 'Find all the factor pairs of a number by working in order, find common factors and common multiples to solve sharing and timetable puzzles, discover which numbers have an odd number of factors, and solve multiple-based logic riddles.',
    skills: 'Making a list in order, looking for a pattern, using clues one at a time, explaining why',
    materials: '36 square tiles or squared paper per pair, mini whiteboards, coloured pencils, a 1 to 50 number strip.',
    online: 'Children cut 24 paper squares (or use squared paper) before the lesson and build rectangles on camera; the tutor marks the bus time line and the factor rainbow on the slides.',
    warmup: 'Fizz-Buzz: count round the group from 1. Say "Fizz" for a multiple of 3, "Buzz" for a multiple of 4 and "Fizz-Buzz" for a multiple of both. Which numbers were Fizz-Buzz?',
    explore: 'Pairs use 24 square tiles to build every different rectangle that uses all the tiles (a 3 by 8 and an 8 by 3 count as the same). They record each one as a multiplication and decide how they know they have found them all.',
    mini: 'Factor pairs in order: 36 = 1 × 36, 2 × 18, 3 × 12, 4 × 9, 6 × 6 (5 does not divide 36); stop when the pairs meet and draw a factor rainbow. Common factors: 12 apples and 18 oranges share the factors 1, 2, 3, 6, so 6 bags with 2 apples and 3 oranges each. Common multiples: buses every 6 and 8 minutes meet again after 24 minutes. Before page 2: square numbers have an odd number of factors (100 has 9; 18 has 6); for riddles, list the multiples of the bigger number first, then check each clue.',
    share: 'Ali says: "Bigger numbers always have more factors." Is he right? Give an example to show it.',
    exit: { q: 'Write all the factors of 18. Then find the smallest number that is a multiple of both 4 and 9.', a: '1, 2, 3, 6, 9, 18. The smallest common multiple of 4 and 9 is 36.' },
    mistakes: [
      'Listing factors at random and missing one, or stopping too early (for 48, forgetting 6 × 8), instead of trying 1, 2, 3 … in order until the pairs meet.',
      'Mixing up factors and multiples: saying 12 is a factor of 4, or listing 4, 8, 12 as the factors of 4.',
      'For common multiples, multiplying the two numbers every time (10 × 15 = 150 minutes) instead of listing the multiples to find the first one they share (30).'
    ],
    extension: 'Which numbers from 1 to 50 have exactly 4 factors? Is there a pattern? (There are 15: 6, 8, 10, 14, 15, 21, 22, 26, 27, 33, 34, 35, 38, 39, 46.)',
    key: [
      ['Q1', '(a) 1 × 48, 2 × 24, 3 × 16, 4 × 12, 6 × 8  (b) 1, 2, 3, 4, 6, 8, 12, 16, 24, 48: 10 factors  (c) 7 is not a factor, and the next number, 8, is already in a pair (6 × 8). The pairs have met, so there are no more.'],
      ['Q2', '6 ways: 2 rows of 20, 4 rows of 10, 5 rows of 8, 8 rows of 5, 10 rows of 4, 20 rows of 2.'],
      ['Q3', '(a) 18: 1, 2, 3, 6, 9, 18.  24: 1, 2, 3, 4, 6, 8, 12, 24  (b) 1, 2, 3, 6  (c) 6 packs, each with 3 red and 4 blue beads.'],
      ['Q4', '(a) Bus 33: 6:00, 6:10, 6:20, 6:30 …  Bus 51: 6:00, 6:15, 6:30 …  Together again at 6:30 am.  (b) Every 30 minutes: 6:00, 6:30, 7:00, 7:30, 8:00, so 5 times.'],
      ['Q5', '(a) 6: 4 factors, 9: 3, 10: 4, 15: 4, 16: 5, 25: 3  (b) 9 and 25. Each is a number times itself (3 × 3 and 5 × 5).  (c) 4, 9, 25, 49'],
      ['Q6', '(a) 36 (multiples of 12 between 30 and 70 are 36, 48, 60; 48 is a multiple of 8; in 60 the ones digit is smaller).  (b) Ravi. 6 = 2 × 3, so every multiple of 6 is in the 3 times table. Mei is wrong: 9 is a multiple of 3 but not of 6.']
    ]
  },

  script: {
    hook: ['Welcome, Factor Hunters! Every number hides its factors inside it, and today we hunt them all down, without missing a single one.', 'We will also find out when two buses meet again, and why some numbers have an odd number of factors. Notice it. Test it. Explain why.'],
    warmIntro: ['We count round the group, one number each. If your number is in the 3 times table, say "Fizz". In the 4 times table, say "Buzz". In both, say "Fizz-Buzz"!', 'Before we start: which will be the first Fizz-Buzz number? Write your guess on your whiteboard.'],
    predict: ['You have 24 square tiles. You must use all of them to make one rectangle. How many different rectangles do you think you can make? Write your guess.'],
    exploreHints: ['Stuck: start with one long row. How many tiles in the row? Now try 2 rows.', 'Not sure if 4 by 6 and 6 by 4 are different: turn your rectangle round. Is it the same shape?', 'Finished early: do it again with 36 tiles. Something special happens. What is it?'],
    think: [
      '“Factor pairs of 36. I try 1, 2, 3 in order. 1 × 36. 2 × 18. 3 × 12. 4 × 9. Does 5 work? No, 36 is not in the 5 times table. 6 × 6. The next number, 9, is already in a pair, so the pairs have met. I stop. 36 has 9 factors.”',
      '“12 apples and 18 oranges in identical bags, nothing left over. The number of bags must be a factor of 12 AND a factor of 18. The common factors are 1, 2, 3, 6. The most bags is 6, with 2 apples and 3 oranges in each.”',
      '“Buses every 6 minutes and every 8 minutes. I list the multiples: 6, 12, 18, 24 … and 8, 16, 24. The first number in both lists is 24, so they meet again after 24 minutes, not 48.”'
    ],
    circulate: ['Ask: “How do you know you have found every factor pair? Where did you stop?”', 'Ask: “Is that a factor or a multiple? Which is bigger?”', 'Ask: “Which list did you write: the factors, or the multiples? Which do you need for this question?”'],
    hints: ['Hint 1: “Try 1, 2, 3, 4 … in order. Does it go in exactly?”', 'Hint 2: “Draw the rectangles, or make them with tiles.”', 'Hint 3: “Write the first few multiples of each number in two rows. Circle the numbers in both rows.”'],
    talk: ['“Ali says: bigger numbers always have more factors. Who agrees? Can you find an example that proves him wrong?”', '“Why did the 36-tile rectangles give an odd number of factors?”'],
    talkAns: 'Ali is wrong. 24 has 8 factors but 29, which is bigger, has only 2 (1 and 29). 36 has an odd number of factors because one of its pairs is 6 × 6, and 6 is only counted once.',
    close: ['“Today you hunted factors in order, so none could hide. You found common factors for sharing and common multiples for timetables.”', '“Hand me your exit ticket and I will stamp your inquiry journal.”']
  },

  deck: {
    today: 'Hunt down every factor of a number, use common factors and common multiples to solve puzzles, and crack multiple riddles.',
    warmGame: 'Fizz-Buzz. Count round the group from 1. Say "Fizz" for a multiple of 3, "Buzz" for a multiple of 4 and "Fizz-Buzz" for a multiple of both.',
    warmQs: [['Is 7 a factor of 56?', 'Yes: 7 × 8 = 56'], ['The first five multiples of 6?', '6, 12, 18, 24, 30'], ['Name a common multiple of 4 and 6.', '12 (or 24, 36 …)'], ['Is 45 a multiple of 4?', 'No: 44 and 48 are'], ['18 as a product, 3 ways?', '1 × 18, 2 × 9, 3 × 6']],
    expSetup: ['Take 24 square tiles.', 'Use ALL the tiles to make a rectangle. Write it as a multiplication, like 2 × 12.', 'Make as many different rectangles as you can. A 2 by 12 and a 12 by 2 count as the same.', 'How do you know you have found them all?'],
    expPic: 'a rectangle of 24 tiles in 3 rows of 8, next to an empty grid for the next rectangle.',
    expAsk: [['How many rectangles did you make?', '4: 1 × 24, 2 × 12, 3 × 8, 4 × 6.'], ['How do you know you have them all?', 'Try 1, 2, 3, 4, 5, 6 rows in order. 5 rows does not work; 6 rows is the 4 × 6 turned round.'], ['What do the side lengths tell us about 24?', 'They are the factors of 24: 1, 2, 3, 4, 6, 8, 12, 24.']],
    mini1: { head: 'All the factor pairs of 36', body: ['Try 1, 2, 3 … in order: 1 × 36, 2 × 18, 3 × 12, 4 × 9.', '5 is not a factor. 6 × 6. The pairs have met.', 'How many factors? Draw a factor rainbow.'], ans: '9 factors: 1, 2, 3, 4, 6, 9, 12, 18, 36.' },
    mini2: { head: 'When do the buses meet again?', body: ['Bus A leaves every 6 minutes, bus B every 8 minutes.', 'Both leave at 7:00 am. List the multiples of 6 and of 8.', 'Which number is in both lists first?'], ans: '24 minutes, so 7:24 am. 24 is the smallest common multiple of 6 and 8.' },
    keyHead: 'Key idea: hunt in order', keyBig: 'Factors: try 1, 2, 3 … in order until the pairs meet. Multiples: list them and look for the first number in both lists.', keySmall: 'A factor goes into a number exactly. A multiple is in its times table.',
    brk: 'Factor freeze. The tutor calls a number. Stand up if your age, 10, is a factor of it. Sit down if it is not. Then try 3, 4 and 5.',
    ws1: 'Page 1, in pairs: Q1 factor pairs of 48, Q2 trees in rows, Q3 beads in packs.',
    ws2: 'Page 2, on your own: Q4 the buses, Q5 counting factors, Q6 multiple riddles.'
  },

  qbank: {
    core: [
      { q: 'Write all the factors of 12.', a: '1, 2, 3, 4, 6, 12' },
      { q: 'Write the first five multiples of 7.', a: '7, 14, 21, 28, 35' },
      { q: 'Is 4 a factor of 52? How do you know?', a: 'Yes: 4 × 13 = 52.' },
      { q: 'Find a common multiple of 3 and 5 that is less than 20.', a: '15' },
      { q: 'Write all the factor pairs of 20.', a: '1 × 20, 2 × 10, 4 × 5' },
      { q: 'What is the smallest number that is a multiple of both 4 and 6?', a: '12' }
    ],
    stretch: [
      { q: 'How many factors does 36 have? List them in order.', a: '9 factors: 1, 2, 3, 4, 6, 9, 12, 18, 36.' },
      { q: 'One lighthouse flashes every 6 seconds. Another flashes every 9 seconds. They flash together now. After how many seconds will they next flash together?', a: '18 seconds (6, 12, 18 and 9, 18).' },
      { q: 'Find all the common factors of 24 and 36.', a: '1, 2, 3, 4, 6, 12' },
      { q: 'I am a multiple of 7 between 50 and 80. My digits add up to 11. Who am I?', a: '56 (the multiples of 7 are 56, 63, 70, 77; only 5 + 6 = 11).' },
      { q: 'Ben shares 28 stickers equally among some friends with none left over. He has more than 1 friend and gives each friend more than 1 sticker. How many friends could he have? Find all the answers.', a: '2, 4, 7 or 14 friends.' },
      { q: 'Which number less than 30 has the most factors?', a: '24, with 8 factors: 1, 2, 3, 4, 6, 8, 12, 24.' },
      { q: 'Which of these numbers are multiples of both 4 and 9: 54, 72, 96, 108?', a: '72 and 108' },
      { q: 'Mrs Tan has 36 pencils and 48 erasers. She puts them into identical packs with nothing left over. What is the greatest number of packs she can make? What is in each pack?', a: '12 packs, each with 3 pencils and 4 erasers.' }
    ],
    challenge: [
      { q: 'How many numbers from 1 to 100 are multiples of 4 or multiples of 6 (or both)?', a: '33. Multiples of 4: 25. Multiples of 6: 16. Both (multiples of 12): 8, counted twice. 25 + 16 − 8 = 33.' },
      { q: 'Mei has between 30 and 50 eggs. When she packs them in 4s, 1 egg is left. When she packs them in 5s, 1 egg is left. How many eggs does she have?', a: '41. One less than the number of eggs is a common multiple of 4 and 5 (20, 40, 60), so 21, 41 or 61; only 41 is between 30 and 50.' },
      { q: 'What is the smallest number that has exactly 6 factors?', a: '12 (1, 2, 3, 4, 6, 12). Every number below 12 has fewer than 6 factors.' },
      { q: 'Ali counts in 6s from 6. Mei counts in 8s from 8. Both stop at 100. How many numbers do they both say?', a: '4: 24, 48, 72, 96.' },
      { q: 'Ravi runs one lap of a track every 4 minutes. Siti runs one lap every 6 minutes. They start together at the start line. How many laps has each run when they are next at the start line together?', a: 'After 12 minutes: Ravi has run 3 laps and Siti 2 laps.' },
      { q: 'Find a number between 20 and 40 that has exactly 4 factors, and both of its factor pairs use odd numbers only.', a: '21 (1 × 21, 3 × 7), 27 (1 × 27, 3 × 9), 33 (1 × 33, 3 × 11), 35 (1 × 35, 5 × 7) or 39 (1 × 39, 3 × 13). Any one of these.' },
      { q: 'Three school bells ring every 4 minutes, every 6 minutes and every 10 minutes. They all ring together at 9:00 am. When do they next all ring together?', a: '10:00 am. The smallest common multiple of 4, 6 and 10 is 60 minutes.' },
      { q: 'I am a number less than 100. When I am divided by 2, 3, 4, 5 or 6, there is always 1 left over. I am bigger than 1. Who am I?', a: '61. One less than the number is a common multiple of 2, 3, 4, 5 and 6: 60. 60 + 1 = 61 (the next one, 121, is too big).' },
      { q: 'There are 20 closed lockers, numbered 1 to 20. Child 1 opens every locker. Child 2 changes every 2nd locker (opens it if it is closed, closes it if it is open). Child 3 changes every 3rd locker, and so on, up to child 20. Which lockers are open at the end?', a: '1, 4, 9 and 16. Each locker is changed once for every factor of its number. Only numbers with an odd number of factors (1, 4, 9, 16: a number times itself) end up open.' }
    ]
  },

  workbook: H => {
    const W = [];
    W.push(H.p('A factor goes into a number exactly. A multiple is in the number\'s times table. 6 is a factor of 24, and 24 is a multiple of 6.', { after: 80 }));
    W.push(H.q(1, 'Hunt down every factor of 48.', { before: 60, keepNext: true }));
    W.push(H.sub('a', 'Write the factor pairs of 48 in order. You may not need every row.', { keepNext: true }));
    W.push(H.tbl([1650, 1650, 1650, 1650, 1650, 1650], [
      H.row(['1 × 48', '____ × ____', '____ × ____', '____ × ____', '____ × ____', '____ × ____'].map(s => H.cell(s, 1650, { h: 110 })))
    ]));
    W.push(H.gap(60));
    W.push(H.sub('b', 'List all the factors of 48 in order.'));
    W.push(H.ans('Factors:'));
    W.push(H.sub('c', 'How many factors does 48 have? ______   How did you know when to stop looking?'));
    W.push(...H.lines(1));
    W.push(H.q(2, 'A gardener plants 40 trees in equal rows. There are at least 2 rows, and at least 2 trees in each row.', { keepNext: true }));
    W.push(H.fig(treesSvg()));
    W.push(H.sub('a', 'Find every way. Fill in the table. You may not need every row.', { keepNext: true }));
    W.push(H.tbl([1100, 1100, 1100, 1100, 1100, 1100, 1100, 1100, 1100], [
      H.row([H.cell('Rows', 1100, { bold: true, fill: 'EDEDED' }), ...['4', '', '', '', '', '', '', ''].map(s => H.cell(s, 1100))]),
      H.row([H.cell('Trees in a row', 1100, { bold: true, fill: 'EDEDED' }), ...['10', '', '', '', '', '', '', ''].map(s => H.cell(s, 1100))])
    ]));
    W.push(H.gap(60));
    W.push(H.ans('How many ways?'));
    W.push(H.q(3, 'Mei has 18 red beads and 24 blue beads. She puts them into identical packs. Every pack has the same number of red beads and the same number of blue beads. No beads are left over.', { keepNext: true }));
    W.push(H.sub('a', 'Factors of 18:  ________________________     Factors of 24:  ________________________________'));
    W.push(H.sub('b', 'Common factors of 18 and 24:  ________________________'));
    W.push(H.sub('c', 'What is the greatest number of packs she can make?  ______   Each pack has ______ red and ______ blue.'));

    W.push(H.q(4, 'At an interchange, Bus 33 leaves every 10 minutes and Bus 51 leaves every 15 minutes. Both buses leave at 6:00 am.', { pb: true, before: 0, keepNext: true }));
    W.push(H.fig(busSvg()));
    W.push(H.sub('a', 'Bus 33 leaves at 6:00, 6:10, ______, ______ …    Bus 51 leaves at 6:00, ______, ______ …'));
    W.push(H.ans('They next leave together at:'));
    W.push(H.sub('b', 'How many times do they leave together from 6:00 am to 8:00 am? Count 6:00 and 8:00 too.'));
    W.push(H.ans('Number of times:'));
    W.push(H.q(5, 'Count the factors.', { keepNext: true }));
    W.push(H.sub('a', 'Fill in the table.', { keepNext: true }));
    W.push(H.tbl([2400, 1250, 1250, 1250, 1250, 1250, 1250], [
      H.row([H.cell('Number', 2400, { bold: true, fill: 'EDEDED' }), ...['6', '9', '10', '15', '16', '25'].map(s => H.cell(s, 1250, { bold: true, fill: 'EDEDED' }))]),
      H.row([H.cell('How many factors?', 2400, { bold: true }), ...Array(6).fill('').map(s => H.cell(s, 1250, { h: 130 }))])
    ]));
    W.push(H.gap(60));
    W.push(H.sub('b', 'Which of these numbers have exactly 3 factors? What do you notice about them?'));
    W.push(...H.lines(2));
    W.push(H.sub('c', 'Find ALL the numbers from 1 to 60 that have exactly 3 factors.'));
    W.push(H.ans('Numbers:'));
    W.push(H.q(6, 'Multiple riddles.', { keepNext: true }));
    W.push(H.sub('a', 'I am a number between 30 and 70. I am a multiple of 3 and a multiple of 4, but I am NOT a multiple of 8. My ones digit is bigger than my tens digit. Who am I?'));
    W.push(H.ans('I am:'));
    W.push(H.sub('b', 'Ravi says: "Every multiple of 6 is also a multiple of 3." Mei says: "Every multiple of 3 is also a multiple of 6." Who is right? Explain with an example.'));
    W.push(...H.lines(3));
    return W;
  }
};
