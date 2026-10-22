// Math Inquirers P4 Holiday Program — Lesson 10: Challenge Day (mixed heuristics)
// Every answer below was worked out and checked with a script; each logic puzzle was checked by trying every
// arrangement, and has exactly one answer. "Find all" questions list every case.
const tip = require('../tip.js');
module.exports = {
  lesson: {
    n: 10, week: 5, session: 'B', title: 'Challenge Day', topic: 'Mixed heuristics',
    objective: 'Choose a way into a non-routine problem (guess and check with a table, suppose they are all the same, work backwards, a logic grid, draw it) and use it on competition-style puzzles, checking every answer against every fact.',
    skills: 'Choosing a strategy, guess and check, supposition, working backwards, logical deduction, checking and explaining',
    materials: 'Four puzzle cards (A to D) for the explore stations (pairs choose three), mini whiteboards, counters or cubes, certificates, stamps.',
    online: 'Pairs go to breakout rooms with the puzzle cards (each pair chooses three of the four) and volunteers report back; the tutor ticks and crosses the logic grid on the slide as children call out.',
    warmup: 'Who am I? A 1 to 100 grid and four clues revealed one at a time (2-digit, in the 7 times table, digits add up to 10, odd). Children cross out numbers after each clue until one is left (91).',
    explore: 'Four puzzle stations, one for each way in: A guess and check (two next-door numbers multiply to 210), B heads and legs (10 spiders and beetles, 68 legs), C work backwards (double a number, add 7, get 43), D logic (who has the fish?). Pairs solve as many as they can and write how they started.',
    mini: 'Four ways in. Guess and check with a table: next-door numbers multiplying to 342 (try 20 × 21, too big; 17 × 18, too small; 18 × 19 ✓). Suppose they are all the same: 15 bicycles and tricycles with 38 wheels (all bicycles gives 30 wheels, 8 short, each swap adds 1, so 8 tricycles). Work backwards: half, then − $4, leaves $11 (11 + 4 = 15, 15 × 2 = 30). Before page 2: a logic grid with ticks and crosses; draw a queue (5th from the front and 8th from the back is 4 + 1 + 7 = 12); ages (everyone gets older by the same amount, so the total grows by 2 × the years).',
    share: 'Which way in did you use most today? If you would like to, pick one puzzle and tell the group your way in, in two sentences. You can pass.',
    exit: { q: 'A farm has ducks and goats: 12 heads and 34 legs. How many goats? Show your way in.', a: '5 goats (and 7 ducks). Suppose all ducks: 24 legs, 10 short, each swap adds 2 legs, so 5 swaps. Check: 7 × 2 + 5 × 4 = 34.' },
    mistakes: [
      'Guessing at random instead of using a table, so each try does not tell them whether to go up or down.',
      'Working backwards but doing the same operation again (taking away 4 instead of adding 4) or undoing the steps in the wrong order.',
      'Queues: adding the two positions (5th and 8th makes 13) and counting the person twice; logic puzzles: stopping before every clue has been used.'
    ],
    extension: 'Write your own heads-and-legs puzzle (for example, bicycles and cars) with exactly one answer. Swap with a partner and solve it by supposing.',
    key: [
      ['Q1', '(a) 23 and 24 (23 × 24 = 552)  (b) 2 ways: 9 pens and 2 notebooks ($36 + $14), or 2 pens and 6 notebooks ($8 + $42). Money left for pens: $43, $36, $29, $22, $15, $8, $1; only $36 and $8 are in the 4 times table.'],
      ['Q2', '(a) 36 legs; 14 legs short  (b) 2 legs; 7 goats and 11 chickens (check: 22 + 28 = 50)  (c) 11 cars (and 13 motorcycles: 44 + 26 = 70)'],
      ['Q3', '(a) 52 (30 + 5 = 35, 35 − 9 = 26, 26 × 2 = 52)  (b) 20 (21 × 2 = 42, 42 + 18 = 60, 60 ÷ 3 = 20)'],
      ['Q4', 'Ali: nasi lemak.  Ben: laksa.  Mei: prata.  Siti: chicken rice.'],
      ['Q5', '(a) 18 people (6 + 1 + 11)  (b) 15th from the back (14 people behind him, 20 − 6 = 14)'],
      ['Q6', 'Ben is 10 and his father is 40. (In 5 years the total is 60; 4 equal bars make 60, so Ben will be 15.)']
    ]
  },

  script: {
    hook: ['Welcome to Challenge Day! Today there is no new topic. Instead, you get the puzzles that mathematicians love, the ones where you do not know how to start.', 'Good problem solvers are not people who know every answer. They know how to START. Notice it. Test it. Explain why.'],
    warmIntro: ['I am thinking of a number from 1 to 100. I will give you one clue at a time. After each clue, cross out every number it cannot be.', 'Clue 1: I am a 2-digit number. Which numbers can you cross out straight away?'],
    predict: ['Look at the four puzzle cards. Which one do you think will be hardest? Write the letter in the corner of your whiteboard. We will check at the end.'],
    exploreHints: ['Stuck on card A: try 10 × 11, then a bigger pair. Is the answer too big or too small?', 'Stuck on card B: what if all 10 bugs were beetles? How many legs would that be?', 'Stuck on card C: start at 43 and undo the last thing first.', 'Finished early: make up a new card for one of the stations.'],
    think: [
      '“Two next-door numbers multiply to 342. I estimate: 20 × 20 is 400, too big. Try 17 × 18 = 306, too small. 18 × 19 = 342. My table tells me which way to go after each try.”',
      '“15 bicycles and tricycles with 38 wheels. Suppose they are ALL bicycles: 30 wheels. I am 8 wheels short. Each time I swap a bicycle for a tricycle I get 1 more wheel. So I swap 8: 8 tricycles and 7 bicycles. Check: 14 + 24 = 38.”',
      '“Siti spent half, then $4, and had $11. I start at the end and undo each step, last one first: add the 4 back, $15; double it, $30. Check forwards: half of 30 is 15, take 4 is 11.”'
    ],
    circulate: ['Ask: “What is your way in? Why did you choose it?”', 'Ask: “Does your answer fit EVERY fact in the question? Show me.”', 'Ask: “Could there be another answer? How do you know?”'],
    hints: ['Hint 1: “Make a table and try a number. Was it too big or too small?”', 'Hint 2: “What if they were all the same? How far off are you?”', 'Hint 3: “Start at the end and undo, last step first.”'],
    talk: ['“Which way in did you use most today?”', '“If you would like to, pick one puzzle and tell us your way in, in two sentences. Volunteers first. You can pass.”'],
    talkAns: 'Open answers. Listen for the name of the strategy (guess and check, suppose, work backwards, logic grid, draw it) and a check against every fact.',
    close: ['“You are real inquirers now: you can start a problem you have never seen before.”', 'Give each child a certificate and their stamped inquiry journal. Tell each one a specific thing they did well this holiday.']
  },

  deck: {
    today: 'Choose a way into tricky puzzles: guess and check, suppose, work backwards, and logic. Then check every fact.',
    warmGame: 'Who am I? Four clues, one at a time, on a 1 to 100 grid. Cross out every number that does not fit each clue until one is left.',
    warmQs: [['Buses every 6 min and every 8 min leave together at 9:00. Next together?', '9:24'], ['Round 45 678 to the nearest thousand.', '46 000'], ['3/4 of 24 = ?', '18'], ['0.6 × 4 = ?', '2.4'], ['Turn clockwise from N to SW. How many degrees?', '225°']],
    expSetup: ['Four puzzle cards, A to D. Start with any card.', 'Read the card aloud with your partner.', 'Try something: a guess, a drawing or a table.', 'Write the answer AND how you got it.'],
    expPic: 'four puzzle cards: A "next-door numbers multiply to 210", B "10 bugs, 68 legs", C "double it, add 7, get 43", D "who has the fish?".',
    expAsk: [['How did you start card B?', 'Suppose all 10 are beetles: 60 legs, 8 short; each spider adds 2 legs, so 4 spiders and 6 beetles.'], ['Which card was hardest? What helped?', 'Open answers: a table, a drawing, or starting at the end.'], ['Could any card have two answers? How do you know?', 'No: each one was checked. A: 14 × 15 = 210. C: 18. D: Ali fish, Mei cat, Ravi dog.']],
    mini1: { head: 'Guess and check with a table', table: [['Try', 'Product', ''], ['20 × 21', '420', 'too big'], ['17 × 18', '306', 'too small'], ['18 × 19', '342', 'just right']], body: ['Two next-door numbers multiply to make 342.', 'Each try tells you to go up or down.'], ans: '18 and 19' },
    mini2: { head: 'Suppose they are all the same', body: ['15 bicycles and tricycles have 38 wheels.', 'Suppose all are bicycles: 30 wheels. 8 short.', 'Each swap to a tricycle adds 1 wheel.'], ans: '8 tricycles and 7 bicycles. Check: 14 + 24 = 38.' },
    keyHead: 'Key idea: pick a way in',
    keyBig: 'Guess and check with a table, suppose they are all the same, or work backwards from the end.',
    keySmall: 'Then check your answer against every fact in the question.',
    brk: 'Heads and legs! The tutor calls "3 chickens and 2 goats": stamp that many legs (14). Then "5 animals, 16 legs": who can say the animals?',
    ws1: 'Page 1, in pairs: Q1 guess and check, Q2 heads and legs, Q3 work backwards.',
    ws2: 'Page 2, on your own: Q4 the logic grid, Q5 queues, Q6 ages.'
  },

  qbank: {
    core: [
      { q: 'Two next-door numbers (like 7 and 8) multiply to make 90. What are they? Try some pairs and write each try in a list.', a: '9 and 10' },
      { q: 'A farm has chickens and rabbits. There are 8 heads and 22 legs. How many rabbits are there? Draw 8 animals with 2 legs each first, then see how many legs you still need to add.', a: '3 rabbits (and 5 chickens). Suppose all chickens: 16 legs, 6 short, each swap adds 2.' },
      { q: 'I think of a number. I add 15, then double it. I get 70. What is my number? Start at 70 and undo each step.', a: '20 (70 ÷ 2 = 35, 35 − 15 = 20)' },
      { q: 'Ali is 6th from the front and 6th from the back of a queue. How many people are in the queue? Draw the queue.', a: '11 (5 + 1 + 5)' },
      { q: 'Two numbers add up to 30. One is 6 more than the other. What are they?', a: '12 and 18' },
      { q: 'Ben has 6 coins. Some are 10¢ and some are 50¢. They make $1.40 altogether. How many 50¢ coins does he have? Try 1 fifty-cent coin, then 2, then 3 …', a: '2 (and four 10¢ coins: 100¢ + 40¢ = 140¢)' }
    ],
    stretch: [
      { q: 'There are 20 bicycles and tricycles with 47 wheels altogether. How many tricycles are there?', a: '7 tricycles (and 13 bicycles). All bicycles: 40 wheels, 7 short, each swap adds 1.' },
      { q: 'Two next-door even numbers (like 6 and 8) multiply to make 624. What are they?', a: '24 and 26' },
      { q: 'Ravi spent $15 on a book. Then he spent half of the money left on a bag. He had $18 left. How much money did he have at first?', a: '$51 (18 × 2 = 36, 36 + 15 = 51)' },
      { q: 'Ali, Ben, Mei and Siti are 8, 9, 10 and 11 years old, in some order. Ali is 2 years older than Siti. Ben is older than Mei. Siti is older than Mei. How old is each child?', a: 'Ali 11, Ben 10, Siti 9, Mei 8. Ali is 2 more than Siti, so (Siti, Ali) is (8, 10) or (9, 11). Mei is younger than both Siti and Ben. If Siti were 8, Mei would have to be younger than 8. So Siti is 9 and Ali is 11, and Mei is 8. Ben is the one left, 10.' },
      { q: 'In a queue, Ali is 8th from the front and Ben is 6th from the back. There are 7 children between Ali and Ben. How many children are in the queue? Draw the queue first.', a: '21. Ali is 8th, the 7 children in between are 9th to 15th, and Ben is 16th. Ben is 6th from the back, so 5 children are behind him: 16 + 5 = 21.' },
      { q: 'There are 12 spiders (8 legs) and ants (6 legs) with 82 legs altogether. How many spiders are there?', a: '5 spiders (and 7 ants). All ants: 72 legs, 10 short, each swap adds 2.' },
      { q: 'Two next-door odd numbers (like 7 and 9) multiply to make 783. What are they?', a: '27 and 29. 28 × 28 = 784 is just above 783, so try the odd numbers on either side of 28: 27 × 29 = 783.' },
      { q: 'Siti and her dad are 48 years old altogether. In 6 years, her dad will be 4 times as old as Siti. How old is Siti now?', a: '6 (in 6 years the total is 60: 5 equal bars, so Siti will be 12)' }
    ],
    challenge: [
      { q: 'How many whole numbers from 1 to 100 have the digit 7 in them at least once?', a: '19 (7, 17, 27, 37, 47, 57, 67, 87, 97 and 70 to 79; 77 is counted once)' },
      { q: 'A farm has 20 chickens and goats. The chickens have 4 more legs altogether than the goats. How many chickens are there?', a: '14 chickens (28 legs) and 6 goats (24 legs).' },
      { q: 'I am a 2-digit number. My digits add up to 11. If you swap my digits, the new number is 27 more than me. Who am I?', a: '47 (74 − 47 = 27)' },
      { q: 'Ali, Ben, Mei and Siti sit in a row of 4 seats, numbered 1 to 4 from the left. Mei sits at one end. Ben sits next to Mei. Ali does not sit next to Ben. Ali sits in seat 1 or seat 2. Who sits in each seat?', a: 'Seat 1 Ali, seat 2 Siti, seat 3 Ben, seat 4 Mei.' },
      { q: 'A cake costs $3 more than a drink. 4 cakes and 3 drinks cost $40. How much does a drink cost?', a: '$4 (a cake is $7). Suppose all 7 are drinks: take away 4 × $3 = $12, then $28 ÷ 7 = $4.' },
      { q: 'Ben’s uncle is 4 times as old as Ben. In 10 years, his uncle will be only twice as old as Ben. How old is Ben now?', a: '5 (uncle 20; in 10 years 15 and 30)' },
      { q: 'A hawker centre has 15 tables. Some seat 4 people and some seat 6 people. There are 76 seats altogether. (a) How many tables seat 6? (b) What is the fewest and the most seats 15 tables could have? (c) Could the centre have 77 seats? Explain.', a: '(a) 8 tables seat 6 (and 7 seat 4). All seat 4: 60 seats, 16 short, each swap adds 2. (b) Fewest 60 (all seat 4), most 90 (all seat 6). (c) No. Every table seats an even number of people, so the total must be even, and 77 is odd.' },
      { q: 'Mei gave Ali half of her stickers and 2 more. Then she gave Ben half of the stickers left and 2 more. She had 5 stickers left. How many did she have at first?', a: '32. Work backwards: (5 + 2) × 2 = 14, (14 + 2) × 2 = 32.' },
      { q: 'Make up your own heads-and-legs puzzle (chickens and goats, or bicycles and cars) that has exactly ONE answer. Check it by trying every number of one animal. Then explain why a farmer who counts 12 heads and 35 legs on a farm with only chickens and goats must have counted wrong.', a: 'Puzzles will vary: check by trying every possible number. Model: 10 vehicles, 32 wheels, cars (4 wheels) and motorcycles (2 wheels): 6 cars and 4 motorcycles is the only way. Why 35 is impossible: every chicken has 2 legs and every goat has 4, so the total number of legs is always even, and 35 is odd.' }
    ]
  },

  workbook: H => {
    const W = [];
    W.push(H.q(1, 'Guess and check. Make a table of your tries.', { before: 40, keepNext: true }));
    W.push(H.sub('a', 'Two consecutive numbers (next-door numbers, like 7 and 8) multiply to make 552. What are they?'));
    W.push(...H.lines(1));
    W.push(H.ans('Answer:'));
    W.push(H.sub('b', 'Mei buys some $4 pens and some $7 notebooks for exactly $50. Find ALL the ways.', { keepNext: true }));
    const w = [2200, 1100, 1100, 1100, 1100, 1100, 1100, 1100];
    const cl = (c, i, head) => H.cell(c, w[i], i === 0 || head ? { bold: true, fill: 'EDEDED', h: 40 } : { h: 60 });
    W.push(H.tbl(w, [H.row(['Notebooks', '1', '2', '3', '4', '5', '6', '7'].map((c, i) => cl(c, i, true))),
      H.row(['Money left for pens', '$43', '', '', '', '', '', ''].map((c, i) => cl(c, i))),
      H.row(['Pens?', '', '', '', '', '', '', ''].map((c, i) => cl(c, i)))]));
    W.push(H.gap(40));
    W.push(H.ans('Ways:'));
    W.push(H.q(2, 'A farm has chickens and goats. There are 18 heads and 50 legs altogether.', { keepNext: true }));
    W.push(H.sub('a', 'Suppose all 18 are chickens. Legs:  ______    Legs short:  ______'));
    W.push(H.sub('b', 'Each swap to a goat adds ____ legs. So ____ goats and ____ chickens.'));
    W.push(H.sub('c', 'A car park has cars and motorcycles: 24 vehicles, 70 wheels. How many cars?'));
    W.push(H.ans());
    W.push(H.q(3, 'Work backwards. Start at the end and undo each step, last step first.', { keepNext: true }));
    W.push(H.sub('a', 'Ravi gave away half of his marbles. Then he won 9 marbles and lost 5. Now he has 30. How many did he have at first?'));
    W.push(H.ans());
    W.push(H.sub('b', 'I think of a number. I multiply it by 3, take away 18, then halve the answer. I get 21. What is my number?'));
    W.push(H.ans());

    W.push(H.q(4, 'Ali, Ben, Mei and Siti each ordered a different dish: chicken rice, laksa, prata or nasi lemak. (Chicken rice and nasi lemak are the rice dishes.) Use the grid: ✓ for yes, X for no.', { pb: true, before: 0, keepNext: true }));
    W.push(H.sub('1', 'Ali and Siti both ordered rice dishes.'));
    W.push(H.sub('2', 'Ali did not order chicken rice.'));
    W.push(H.sub('3', 'Ben did not order prata.'));
    const g = [2300, 1900, 1900, 1900, 1900];
    W.push(H.tbl(g, [H.row(['', 'Chicken rice', 'Laksa', 'Prata', 'Nasi lemak'].map((c, i) => H.cell(c, g[i], { bold: true, fill: 'EDEDED', h: 50 }))),
      ...['Ali', 'Ben', 'Mei', 'Siti'].map(n => H.row([H.cell(n, g[0], { bold: true, fill: 'EDEDED', h: 70 }), ...[1, 2, 3, 4].map(i => H.cell('', g[i], { h: 70 }))]))]));
    W.push(H.gap(40));
    W.push(H.sub('a', 'Ali: ___________   Ben: ___________   Mei: ___________   Siti: ___________'));
    W.push(H.q(5, 'Draw the queue.', { keepNext: true }));
    W.push(H.sub('a', 'Mei is 7th from the front and 12th from the back of a queue at the MRT gantry. How many people are in the queue?'));
    W.push(H.ans());
    W.push(H.sub('b', '20 people are in a queue. Ben is 6th from the front. What is his place from the back?   ________'));
    W.push(H.q(6, 'Ben and his father are 50 years old altogether. In 5 years, his father will be 3 times as old as Ben. How old is Ben now? Draw bars.', { keepNext: true }));
    W.push(tip('try an age and check it. Try 1: Ben is 6, so his father is 44. In 5 years: Ben 11, father 49. Is 49 three times 11? No (33). Try again with a different age.'));
    W.push(...H.lines(3));
    W.push(H.ans());
    return W;
  }
};

// ---- close_gaps + fix pass: sneak-peek puzzles, Investigation (with an easy first step), Looking back, Go further (docs/audit/close_gaps_p4.md, fixpass_p4.md)
module.exports.gaps = {
 "idea": "ways in to a puzzle",
 "check": [
  {
   "q": "Draw 5 ducks. A duck has 2 legs. How many legs are there altogether? Now change ONE duck into a rabbit (a rabbit has 4 legs). How many legs now?",
   "a": "10 legs, then 12 legs. Changing a duck into a rabbit adds 2 legs.",
   "s": "10 legs, then 12 legs: each rabbit adds 2.",
   "kind": "access"
  },
  {
   "q": "A garden has only ducks (2 legs) and rabbits (4 legs). There are 8 animals and 22 legs. How many rabbits are there?",
   "a": "3 rabbits (and 5 ducks): 5 × 2 + 3 × 4 = 22. Suppose all 8 are ducks: 16 legs, 6 too few; each rabbit instead of a duck adds 2 legs, so 3 rabbits.",
   "s": "3 rabbits and 5 ducks.",
   "kind": "think"
  }
 ],
 "why": "Pick a way in: guess and check with a table, suppose they are all the same, or work backwards from the end. Then check every fact.",
 "invest": {
  "kind": "Find all the ways.",
  "head": "Ring toss scores",
  "intro": "In a ring-toss game, a small ring scores 3 points and a big ring scores 5 points. You can throw as many rings of each kind as you like. Which total scores are possible?",
  "parts": [
   "List the scores from 1 to 20 that you CAN get, and show how (for example 8 = 3 + 5). Circle the scores you can NOT get.",
   "What do you notice about the scores you cannot get? After which score can you get every number?",
   "What if the rings score 4 and 6? Which scores from 1 to 20 are impossible? Explain why."
  ],
  "lines": 6,
  "key": "(a) You cannot get 1, 2, 4 or 7. You can get 3, 5, 6 (3 + 3), 8 (3 + 5), 9 (3 + 3 + 3), 10 (5 + 5) and every score from 8 up to 20 (checked by brute force up to 30). (b) After 7 you can get every score: 8, 9 and 10 can be made, and adding a 3 gives the next ones. (c) With 4 and 6 every score is even, so all the odd scores are impossible, and 2 as well (every even score from 4 up is possible). Why: both rings score even numbers, and even + even is even. Look for a systematic list or table, and for children who can say WHY about the even scores.",
  "easy": "List the scores you can get with ONE ring: 3 or 5. Then with TWO rings: 3 + 3, 3 + 5 and 5 + 5. Write each total."
 },
 "reflect": "Something I did well: I tried a table when I was stuck. The hardest part was choosing which way in to use. What helped me: trying a table first, then checking every fact.",
 "go2": {
  "q": "What if 10 bugs have 65 legs? Could that happen? Why or why not?",
  "a": "No. Spiders have 8 legs and beetles 6: both are even numbers, so the total number of legs is always even, and 65 is odd."
 },
 "cap": "Page 2 is on your own. Aim for Q4 and Q5 first. Q6 is a choice for the last few minutes."
};
