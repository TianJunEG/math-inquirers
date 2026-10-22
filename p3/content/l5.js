// Math Inquirers P3 — Lesson 5: Remainder Riddles (Division)
// Heuristics taught: work backwards (groups × size + leftover) and make a list (then test each clue).
const NV = '#1B2A49', YL = '#FFC93C';
const shareSvg = () => {
  let s = `<svg aria-label="Six empty plates and 47 counters to share" viewBox="0 0 600 190" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:480px">`;
  for (let i = 0; i < 6; i++) s += `<circle cx="${60 + i * 96}" cy="42" r="34" fill="#fff" stroke="${NV}" stroke-width="3" stroke-dasharray="7 5"/>`;
  s += `<text x="300" y="104" font-size="16" font-weight="700" text-anchor="middle" fill="#1F7A6F" font-family="Arial">47 counters to share among the 6 plates</text>`;
  for (let k = 0; k < 47; k++) s += `<circle cx="${40 + (k % 12) * 46}" cy="${126 + Math.floor(k / 12) * 20}" r="8" fill="${YL}" stroke="${NV}" stroke-width="2"/>`;
  return s + '</svg>';
};

module.exports = {
  lesson: {
    n: 5, week: 3, session: 'A',
    title: 'Remainder Riddles',
    topic: 'Division',
    objective: 'Divide with remainders, check that the remainder is smaller than the number we divide by, decide what the leftover means in a story, work backwards from groups and leftovers, and solve "what number am I?" riddles by making a list.',
    skills: 'Division with remainders, interpreting the remainder (one more group or leave it out), working backwards (groups × size + leftover), making a systematic list and testing each clue, making a table',
    materials: '25 counters per child (or beans or buttons), 6 small cups for groups, mini whiteboards and markers. For the sneak-peek puzzles: paper, a pencil and a few counters or small objects for each child.',
    online: 'Children use 25 small things at home (dried beans, buttons, LEGO bricks) and a few cups or bowls. Share the screen for the slides; children hold whiteboards up to the camera. Print the workbook before the lesson. Pairs work in one breakout room for 10 minutes, then return for the check slide.',
    warmup: 'Leftover Lucky Dip: the tutor calls a number of sweets and a group size (23 in 4s). Children show the number of groups on one hand and the leftover on the other, then explain with a times-table fact.',
    explore: 'Pairs put 25 counters into groups of 2, 3, 4, 5 and 6 and record the groups and the leftover in a table. They notice that 25 leaves 1 over for 2, 3, 4 and 6, and nothing for 5, and explain why (24 is in the 2, 3, 4 and 6 tables).',
    mini: 'The remainder is always smaller than the number we divide by. Check with groups × size + leftover. Then read the story: does the leftover need one more group (vans), or do only full groups count (boxes, things you can buy)?',
    share: 'Why can the remainder never be as big as the number we divide by?',
    exit: { q: '29 children go on a ride. Each car holds 4 children. How many cars are needed? Write the division and explain what the leftover means.', a: '29 ÷ 4 = 7 r 1. 8 cars are needed: the 1 child left over still needs a car.' },
    mistakes: [
      'Leaving a remainder that is as big as, or bigger than, the number we divide by (60 ÷ 7 = 7 r 11).',
      'Giving the division answer when the story needs one more group (minibuses, boxes for ALL the eggs), or adding one when only full groups count (books she can buy).',
      'Stopping at the first number that fits one clue in a riddle, without testing the other clue or finding ALL the numbers.'
    ],
    extension: 'Find the smallest number bigger than 1 that leaves a remainder of 1 when it is divided by 2, 3, 4, 5 and 6. (61: it is one more than 60, which is in all five tables.)',
    key: [
      ['Q1', '(a) 7 each, 5 left over (6 × 7 = 42, 47 − 42 = 5).  (b) 1 more (48 = 6 × 8).  (c) The remainder 11 is bigger than 7, so another group of 7 fits: 60 ÷ 7 = 8 r 4 (7 × 8 = 56, 60 − 56 = 4).'],
      ['Q2', '(a) 75 ÷ 9 = 8 r 3, so 9 minibuses (the 3 pupils left over need a bus too).  (b) 60 ÷ 7 = 8 r 4, so 8 books ($4 is not enough for another).  (c) 87 ÷ 6 = 14 r 3: 14 full boxes.  (d) 15 boxes to hold all the eggs.'],
      ['Q3', '(a) 12 × 8 + 5 = 96 + 5 = 101 marbles.  (b) 101 ÷ 9 = 11 r 2: 11 full bags, 2 marbles left over (9 × 11 = 99).'],
      ['Q4', '(a) Remainder 3 when ÷ 5: 43, 48, 53, 58. Remainders when ÷ 4: 3, 0, 1, 2. I am 53.  (b) 11, 23, 35 and 47 (remainder 5 when ÷ 6: 11, 17, 23, 29, 35, 41, 47; only 11, 23, 35, 47 leave 3 when ÷ 4). They go up in 12s.'],
      ['Q5', '(a) 0, 1, 2, 3, 4, 5, 6, 7 (the remainder must be smaller than 8).  (b) 63 (biggest remainder 7; 56 + 7 = 63; 64 + 7 = 71 is too big).'],
      ['Q6', '(a) 5 tables and 35 children (5 × 6 + 5 = 35 and 5 × 7 = 35). In the table the gap shrinks by 1 each row: 1 table 11 and 7, 2 tables 17 and 14, 3 tables 23 and 21, 4 tables 29 and 28, 5 tables 35 and 35.  (b) 5 × 8 = 40 seats, 40 − 35 = 5 empty seats.']
    ]
  },

  script: {
    hook: ['Welcome, Remainder Riddlers! When we share things out, there are often some left over. Today the leftovers are clues: they tell us how many buses to book, which number is hiding, and how many tables are in the room.'],
    warmIntro: ['I will call out some sweets and a group size. Show me the number of groups on one hand and the leftover on the other.', '23 sweets in groups of 4. How many groups? How many left over? Which times-table fact helped you?'],
    predict: ['We will put 25 counters into groups of 2, 3, 4, 5 and 6. Which group size do you think leaves nothing over? Write a guess.'],
    exploreHints: [
      'Stuck: make the groups with counters and push the leftovers to one side.',
      'Use a times-table fact: 6 × 4 = 24, so 25 in groups of 4 is 6 groups and 1 left over.',
      'Ready for more: the Go further what-if on the slide: try 49 counters. Which group sizes leave 1 over? Why?'
    ],
    think: [
      '“38 sweets for 5 children. I count in 5s: 5 × 7 = 35, 5 × 8 = 40, too many. So each child gets 7.”',
      '“I used 35, so 38 − 35 = 3 are left over. Is 3 smaller than 5? Yes. So 38 ÷ 5 = 7 r 3. Check: 7 × 5 + 3 = 38.”',
      '“50 people, vans of 8: 50 ÷ 8 = 6 r 2. Those 2 people still need a ride, so 7 vans. But 50 cakes in boxes of 8 fill only 6 boxes. Same division, different answer, so I read the question again.”'
    ],
    circulate: [
      'Ask: “Is your remainder smaller than the number you divided by?”',
      'Ask: “What happens to the leftover in this story?”',
      'Ask: “How do you know there are no more numbers in your list?”'
    ],
    hints: [
      'Hint 1: “Which times table do you need? Count up in it.”',
      'Hint 2: “Groups × size + leftover gives the starting number.”',
      'Hint 3: “List the numbers that fit one clue. Then test each one with the other clue.”'
    ],
    talk: ['“Why can the remainder never be as big as the number we divide by?”', '“75 ÷ 9 = 8 r 3. Why was the minibus answer 9, not 8?”'],
    talkAns: 'If the leftover were as big as the group size, we could make one more group, so the remainder is always smaller. The 3 pupils left over still need a seat, so we need one more minibus: 9.',
    close: ['“Today you read the leftovers like clues. Inquirers ask what an answer means, not just what it is.”']
  },

  deck: {
    today: 'Divide with leftovers, decide what the leftover means in a story, work backwards, and crack “what number am I?” riddles with a list.',
    warmGame: 'Leftover Lucky Dip. The tutor calls a number of sweets and a group size (23 in 4s, 17 in 3s, 26 in 8s, 41 in 6s). Children show the groups on one hand and the leftover on the other.',
    warmQs: [['17 ÷ 5', '3 r 2'], ['30 ÷ 7', '4 r 2'], ['45 ÷ 6', '7 r 3'], ['50 ÷ 8', '6 r 2'], ['63 ÷ 9', '7 r 0 (nothing left over)']],
    expSetup: ['Take 25 counters.', 'Put them in groups of 2, then 3, 4, 5 and 6.', 'Record the groups and the leftover in a table.', 'Ask: what do you notice about the leftovers?'],
    expPic: '25 counters in six groups of 4 with 1 left over, next to a table with columns Group size, Groups and Left over.',
    expAsk: [
      ['Which group size left nothing over?', 'Groups of 5: 25 is in the 5 times table (5 × 5).'],
      ['Why did 2s, 3s, 4s and 6s all leave 1 over?', '24 is in the 2, 3, 4 and 6 tables, and 25 is one more than 24.'],
      ['In groups of 4, can 4 or more be left over?', 'No. If 4 were left, they would make another group. The leftover is always smaller than the group size.']
    ],
    mini1: { head: 'Share 38 sweets equally among 5 children', body: ['Count in 5s: 5 × 7 = 35, 5 × 8 = 40 is too many.', '38 − 35 = 3 left over, and 3 is smaller than 5.', 'Check: 7 × 5 + 3 = 38.'], ans: '7 each, 3 left over: 38 ÷ 5 = 7 r 3.' },
    mini2: { head: '50 people, vans of 8. How many vans?', body: ['50 ÷ 8 = 6 r 2.', 'The 2 people left over still need a ride.', 'Compare: 50 cakes in boxes of 8 fill only 6 boxes.'], ans: '7 vans (but only 6 full boxes of cakes).' },
    keyHead: 'Key idea: read the leftover',
    keyBig: 'The remainder is always smaller than the number we divide by. Start number = groups × size + leftover.',
    keySmall: 'Then ask: does the leftover need one more group, or is it left out?',
    brk: 'Clap-and-stomp groups. The tutor calls “Clap 17 in 5s!” Everyone claps in groups of 5, then stomps once for each leftover clap. Then 23 in 4s and 20 in 6s.',
    ws1: 'Page 1, in pairs: Q1 sharing stickers and fixing a wrong remainder, Q2 what the leftover means, Q3 working backwards and repacking.',
    ws2: 'Page 2, on your own: Q4 what number am I (list and test, find all), Q5 the biggest remainder, then Q6 the party tables (make a table) if you have time.'
  },

  qbank: {
    core: [
      { q: 'Share 35 counters equally among 4 children. How many counters does each child get? How many counters are left over? (Use counters or draw dots in 4 groups.)', a: '8 each, 3 left over (4 × 8 = 32, 35 − 32 = 3)' },
      { q: 'Put 58 sweets into bags with 7 sweets in each bag. How many full bags can you fill? How many sweets are left over? (Use counters or draw dots.)', a: '8 full bags, 2 sweets left over (7 × 8 = 56)' },
      { q: '6 friends share 45 stickers equally. How many does each friend get? How many are left over?', a: '7 each, 3 left over (6 × 7 = 42)' },
      { q: '30 children go on an outing. Each car holds 4 children. How many cars are needed?', a: '8 cars (30 ÷ 4 = 7 r 2; the 2 children left over need a car too)' },
      { q: 'A ribbon is 50 cm long. Siti cuts it into pieces 6 cm long. How many whole pieces does she get? How much ribbon is left?', a: '8 pieces, 2 cm left (6 × 8 = 48)' },
      { q: 'Ben packs muffins into boxes of 5. He fills 7 boxes and has 3 muffins left over. How many muffins does he have?', a: '38 (7 × 5 + 3)' }
    ],
    stretch: [
      { q: 'Mei has 53 beads. She makes bracelets with 8 beads each. How many bracelets can she make? How many more beads does she need to make one more bracelet?', a: '6 bracelets (53 ÷ 8 = 6 r 5). She needs 3 more beads (56 − 53).' },
      { q: 'I am a number between 20 and 30. When I am divided by 4, the remainder is 3. When I am divided by 6, the remainder is 5. What number am I?', a: '23 (remainder 3 when ÷ 4: 23 and 27; 23 ÷ 6 = 3 r 5, 27 ÷ 6 = 4 r 3)' },
      { q: 'What is the biggest 2-digit number that leaves a remainder of 8 when it is divided by 9?', a: '98 (9 × 10 + 8 = 98; 99 ÷ 9 has no remainder)' },
      { q: 'A boat can carry 9 people at a time. 100 people want to cross the river. How many boatloads are needed?', a: '12 boatloads (100 ÷ 9 = 11 r 1; the last person needs a boatload too)' },
      { q: 'Siti fills 9 bags with 7 oranges each and has 5 oranges left over. She packs all the oranges again into bags of 8. How many full bags does she get? How many are left over?', a: '68 oranges (9 × 7 + 5). 68 ÷ 8 = 8 r 4: 8 full bags, 4 left over.' },
      { q: 'A pattern goes circle, triangle, square, circle, triangle, square, … What is the 50th shape?', a: 'Triangle (50 ÷ 3 = 16 r 2; the 2nd shape in the repeat)' },
      { q: 'Find all the 2-digit numbers less than 40 that leave a remainder of 2 when divided by 3 AND when divided by 4.', a: '14, 26 and 38 (each is 2 more than a number in both the 3 and 4 tables: 12, 24, 36)' },
      { q: 'Mei has 29 beads. She puts them into bags of 4. Then she tips them out and puts them into bags of 5. Then into bags of 6. Each time she writes how many beads are left over. Which bag size leaves the most beads over? Which leaves the fewest?', a: 'Bags of 4: 7 bags and 1 left. Bags of 5: 5 bags and 4 left. Bags of 6: 4 bags and 5 left. Bags of 6 leave the most (5), bags of 4 leave the fewest (1).' }
    ],
    challenge: [
      { q: 'I am a 2-digit number. When I am divided by 3, by 4 or by 5, the remainder is always 2. What number am I?', a: '62 (60 is in the 3, 4 and 5 tables; 60 + 2 = 62; the next one, 122, has 3 digits)' },
      { q: 'A box has more than 30 but fewer than 50 chocolates. They can be shared equally among 2, 3, 4 or 6 children with none left over. Find all the numbers of chocolates there could be.', a: '36 and 48 (numbers in the 12 times table)' },
      { q: 'A number is divided by 6. The answer and the remainder are the same number, and it is not 0. Find all the numbers it could be.', a: '7, 14, 21, 28 and 35 (1 r 1, 2 r 2, 3 r 3, 4 r 4, 5 r 5; the remainder cannot be 6 or more)' },
      { q: 'Ben counts his marbles in 5s and has 3 left over. He counts them in 7s and has 3 left over. He has more than 50 and fewer than 100 marbles. How many does he have?', a: '73 (35 is in both tables; 35 + 3 = 38 is too small; 70 + 3 = 73)' },
      { q: 'When 100 is divided by a 1-digit number, the remainder is 1. Find all the numbers it could be.', a: '3 and 9 (100 ÷ 3 = 33 r 1, 100 ÷ 9 = 11 r 1; 99 is only in the 1, 3 and 9 tables, and dividing by 1 leaves no remainder)' },
      { q: 'A farmer counts her eggs. In 2s, 3s, 4s, 5s or 6s there is always 1 egg left over. In 7s there are none left over. What is the smallest number of eggs she can have?', a: '301 (one more than a number in the 60 times table: 61, 121, 181, 241, 301; only 301 is in the 7 table: 7 × 43)' },
      { q: 'Make up your own remainder riddle: "I am a number between ___ and ___. When I am divided by ___ the remainder is ___. When I am divided by ___ the remainder is ___." Check that only ONE number fits, by listing the numbers for the first clue and testing them. Swap with a partner.', a: 'Answers vary. Check that the number fits both clues and only ONE number does. Example: "Between 20 and 50; ÷ 5 leaves 2; ÷ 6 leaves 4." Only 22 fits (22 = 4 × 5 + 2 = 3 × 6 + 4). With the range 20 to 60, 52 would fit too.' },
      { q: 'Today is Monday. What day of the week will it be 100 days from today? What day of the week was it 100 days ago? Explain how you know.', a: '100 days from today: Wednesday. 100 ÷ 7 = 14 remainder 2, so after 14 weeks it is Monday again, then 2 more days. 100 days ago: Saturday. Go back 14 weeks to a Monday, then 2 more days back: Sunday, then Saturday.' },
      { q: 'Mr Lim gives pens to his pupils. If each pupil gets 4 pens, 10 pens are left over. If each pupil gets 6 pens, he is 4 pens short. How many pupils are there? How many pens does he have?', a: '7 pupils and 38 pens (giving 2 more pens each needs 10 + 4 = 14 pens, and 14 ÷ 2 = 7; 7 × 4 + 10 = 38, 7 × 6 = 42 = 38 + 4)' }
    ]
  },

  workbook: H => {
    const W = [];
    const ws = [2700, 1800, 1800, 1800, 1800];
    W.push(H.p('When we share or make groups, some may be left over. The leftover is called the remainder. It is always smaller than the number we divide by.', { after: 100 }));
    W.push(H.q(1, 'Siti shares 47 stickers equally among 6 friends.', { before: 100, keepNext: true }));
    W.push(H.fig(shareSvg()));
    W.push(H.sub('a', 'How many stickers does each friend get?   ____      How many are left over?   ____'));
    W.push(H.sub('b', 'What is the smallest number of extra stickers Siti needs so that none are left over?   ____'));
    W.push(H.sub('c', 'Ben works out 60 ÷ 7. He writes:  60 ÷ 7 = 7 remainder 11.  What is wrong? Write the correct answer.', { keepNext: true }));
    W.push(...H.lines(2));
    W.push(H.q(2, 'Divide. Then decide what to do with the leftover.', { keepNext: true }));
    W.push(H.sub('a', '75 pupils. 1 minibus holds 9 pupils. How many minibuses?   ____'));
    W.push(H.sub('b', '$60. 1 book costs $7. How many books can Mei buy?   ____'));
    W.push(H.sub('c', '87 eggs. 1 box holds 6 eggs. How many boxes are FULL?   ____', { keepNext: true }));
    W.push(H.sub('d', 'How many boxes hold ALL the eggs?   ____', { keepNext: true }));
    W.push(...H.lines(1));
    W.push(H.q(3, 'Ravi packs marbles into bags of 8. He fills 12 bags and has 5 marbles left over.', { keepNext: true }));
    W.push(H.p('Hint: draw 12 bags of 8, then 5 more.', { after: 20 }));
    W.push(H.sub('a', 'How many marbles does Ravi have?   ____'));
    W.push(...H.lines(1));
    W.push(H.sub('b', '(if time) He tips them all out and packs them again into bags of 9. How many full bags does he get? How many marbles are left over?', { keepNext: true }));
    W.push(H.ans('Full bags: ______     Left over:'));

    W.push(H.q(4, 'What number am I? Make a list, then test each number.', { pb: true, before: 0, keepNext: true }));
    W.push(H.sub('a', 'I am between 40 and 60. When I am divided by 5, the remainder is 3. When I am divided by 4, the remainder is 1.', { keepNext: true }));
    W.push(H.tbl(ws, [
      H.row([H.cell('Remainder 3 when ÷ 5', ws[0], { bold: true, fill: 'EDEDED', size: 22 }), ...[1, 2, 3, 4].map(i => H.cell('', ws[i], { h: 140 }))]),
      H.row([H.cell('Remainder when ÷ 4', ws[0], { bold: true, fill: 'EDEDED', size: 22 }), ...[1, 2, 3, 4].map(i => H.cell('', ws[i], { h: 140 }))])
    ]));
    W.push(H.ans('I am:'));
    W.push(H.sub('b', '(if time) I am a 2-digit number less than 50. When I am divided by 6, the remainder is 5. When I am divided by 4, the remainder is 3. Find ALL the numbers I could be.', { keepNext: true }));
    W.push(...H.lines(2));
    W.push(H.q(5, 'Dividing by 8.', { keepNext: true }));
    W.push(H.sub('a', 'Write ALL the remainders you could get when you divide a number by 8. Hint: share 9, 10, 11, … counters into groups of 8. What is left over each time?', { keepNext: true }));
    W.push(H.ans());
    W.push(H.sub('b', 'A number between 60 and 70 is divided by 8. The remainder is as big as it can be. What is the number?   ____'));
    W.push(H.q(6, '(if time) At a class party, children sit at tables. If 6 children sit at each table, 5 children have no seat. If 7 children sit at each table, every seat is filled and nobody is left over.', { keepNext: true }));
    const tw = [3300, 1100, 1100, 1100, 1100, 1100, 1100];
    W.push(H.tbl(tw, [
      H.row([H.cell('Number of tables', tw[0], { bold: true, fill: 'D9D9D9', size: 22 }), ...[1, 2, 3, 4, 5, 6].map(i => H.cell(String(i), tw[i], { bold: true, fill: 'D9D9D9' }))]),
      H.row([H.cell('Children: 6 at each table, 5 with no seat', tw[0], { bold: true, size: 20 }), H.cell('11', tw[1]), ...[2, 3, 4, 5, 6].map(i => H.cell('', tw[i], { h: 130 }))]),
      H.row([H.cell('Children: 7 at each table', tw[0], { bold: true, size: 20 }), H.cell('7', tw[1]), ...[2, 3, 4, 5, 6].map(i => H.cell('', tw[i], { h: 130 }))])
    ]));
    W.push(H.sub('a', 'How many tables are there?   ____      How many children?   ____'));
    W.push(H.sub('b', 'If 8 children sit at each table instead, how many seats are empty?   ____'));
    return W;
  }
};
