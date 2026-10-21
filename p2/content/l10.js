// Math Inquirers P2, Lesson 10: Challenge Day (mixed puzzles: how to start a puzzle)
// Every answer below was worked out and checked; the logic grids were checked by a short program for exactly one solution.
const N = '#1B2A49', Y = '#FFC93C', SKY = '#DDEBF7', TEAL = '#1F7A6F', RED = '#D64545', W = '#FFFFFF';
const F = 'font-family="Arial, sans-serif"';
const svg = (w, h, body, label) => `<svg viewBox="0 0 ${w} ${h}" width="${w}" style="max-width:100%" role="img" aria-label="${label}" xmlns="http://www.w3.org/2000/svg">${body}</svg>`;
const txt = (x, y, s, size = 16, o = {}) => `<text x="${x}" y="${y}" font-size="${size}" font-weight="${o.w || 700}" text-anchor="${o.a || 'middle'}" fill="${o.c || N}" ${F}>${s}</text>`;

/* ---------- drawings ---------- */
const cone = (x, y) => `<polygon points="${x + 4},${y + 12} ${x + 24},${y + 12} ${x + 14},${y + 34}" fill="${Y}" stroke="${N}" stroke-width="2"/><circle cx="${x + 14}" cy="${y + 9}" r="10" fill="${RED}" stroke="${N}" stroke-width="2"/>`;
const graphFig = (() => {
  const rows = [['Monday', 4], ['Tuesday', 6], ['Wednesday', 3], ['Thursday', null]];
  let b = '';
  rows.forEach(([d, k], i) => {
    const y = 6 + i * 42;
    b += `<rect x="0" y="${y}" width="600" height="40" fill="${i % 2 ? W : SKY}"/>` + txt(12, y + 26, d, 16, { a: 'start' });
    if (k) for (let j = 0; j < k; j++) b += cone(130 + j * 36, y + 2);
    else b += txt(130, y + 26, 'Draw the pictures for Thursday here.', 15, { a: 'start', c: TEAL, w: 600 });
  });
  b += `<rect x="0" y="6" width="600" height="168" fill="none" stroke="${N}" stroke-width="2"/><line x1="118" y1="6" x2="118" y2="174" stroke="${N}" stroke-width="2"/>`;
  b += cone(200, 182) + txt(236, 208, '= 5 ice-creams', 17, { a: 'start' });
  return svg(600, 222, b, 'Picture graph of ice-creams sold. Monday 4 pictures, Tuesday 6, Wednesday 3, Thursday blank. Each picture stands for 5 ice-creams.');
})();
const cardsFig = svg(600, 70, [3, 0, 8].map((d, i) => `<rect x="${210 + i * 64}" y="6" width="52" height="60" rx="8" fill="${W}" stroke="${N}" stroke-width="3"/>` + txt(236 + i * 64, 48, d, 32)).join(''), 'Three digit cards: 3, 0 and 8');
const cakeFig = svg(600, 64, `<rect x="50" y="8" width="500" height="48" rx="6" fill="${Y}" stroke="${N}" stroke-width="3"/>` + Array.from({ length: 9 }, (_, i) => `<line x1="${100 + i * 50}" y1="8" x2="${100 + i * 50}" y2="56" stroke="${N}" stroke-width="2.5"/>`).join(''), 'A cake cut into 10 equal pieces in a row');
const tablesFig = (() => {
  let b = '', x = 30;
  [1, 2, 3].forEach(n => {
    const w = n * 40;
    b += `<rect x="${x}" y="22" width="${w}" height="40" fill="${SKY}" stroke="${N}" stroke-width="2.5"/>`;
    for (let i = 1; i < n; i++) b += `<line x1="${x + i * 40}" y1="22" x2="${x + i * 40}" y2="62" stroke="${N}" stroke-width="1.5"/>`;
    for (let i = 0; i < n; i++) b += `<circle cx="${x + 20 + i * 40}" cy="11" r="8" fill="${RED}" stroke="${N}" stroke-width="2"/><circle cx="${x + 20 + i * 40}" cy="73" r="8" fill="${RED}" stroke="${N}" stroke-width="2"/>`;
    b += `<circle cx="${x - 11}" cy="42" r="8" fill="${RED}" stroke="${N}" stroke-width="2"/><circle cx="${x + w + 11}" cy="42" r="8" fill="${RED}" stroke="${N}" stroke-width="2"/>`;
    b += txt(x + w / 2, 104, n + (n === 1 ? ' table' : ' tables'), 15);
    x += w + 90;
  });
  return svg(600, 112, b, '1 table seats 4 people, 2 tables pushed together seat 6, 3 tables seat 8');
})();
const W5 = [2300, 1900, 1900, 1900, 1900];

/* ---------- module ---------- */
module.exports = {
  lesson: {
    n: 10, week: 5, session: 'B', title: 'Challenge Day', topic: 'Mixed Puzzles',
    objective: 'Choose a way to start a puzzle (draw it, list it in order, make a table) and use it on mixed puzzles: picture graphs with a key of 5 or 10, a logic grid with exactly one answer, numbers to 1000, money, fractions, and × and ÷ with the 2, 3, 4, 5 and 10 tables. Check the answer and explain it.',
    skills: 'Choosing a strategy, drawing models, listing in order, making tables, logical elimination, checking, explaining',
    materials: 'Puzzle cards for 4 stations, play coins, digit cards 0 to 9, paper strips for fractions, mini whiteboards, certificates, stamps.',
    online: 'Breakout pairs work on one station card each and report back to the group. Each child needs digit cards (cut from paper), a pencil and a mini whiteboard.',
    warmup: 'Relay review: six quick cards, one from each earlier topic (digits, missing digits, legs, patterns, change, fractions). The answer is passed round the group.',
    explore: 'Station rotation (4 stations, about 3 minutes each, or one card per breakout pair): a picture graph with a key, a logic grid, a coin puzzle and a fraction strip puzzle. Pairs write how they started each one.',
    mini: 'How to start a puzzle. Draw it: bars for before-and-after stories (Mei gave half her stickers away, then 6 more, and has 4 left: the half she kept is 4 + 6 = 10, so she had 20). List it in order: digit cards 2, 0, 5 make 205, 250, 502, 520 (0 cannot go first). Make a table: 7 heads and 20 legs, chickens and goats; try 0, 1, 2, 3 goats until the legs are 20 (3 goats, 4 chickens). Then check and explain.',
    share: 'Pick one puzzle and teach it to the group in two sentences: how you started it, and how you know your answer is right.',
    exit: { q: '5 bicycles and tricycles have 13 wheels altogether. How many tricycles are there? How did you start?', a: '3 tricycles and 2 bicycles (9 + 4 = 13). A table of 0, 1, 2, 3 tricycles works well.' },
    mistakes: ['Picture graph: counting the pictures instead of using the key (writing 6 instead of 30 for Tuesday).', 'Listing: putting 0 first (038 is not a 3-digit number) or missing a number because the list is not in order.', 'Logic grid: putting a tick without crossing out the rest of that row and column, so the next clue cannot be used.'],
    extension: 'Write a challenge puzzle for next year’s group, with the answer and a hint that says how to start it. Check it has exactly one answer.',
    key: [
      ['Q1', '(a) 30  (b) 15 more  (c) Thursday 25 ice-creams: draw 5 pictures (90 − 20 − 30 − 15 = 25)  (d) $30 (15 ice-creams at $2 each)'],
      ['Q2', '(a) 308, 380, 803, 830  (b) Greatest 830, smallest 308  (c) 308, 380, 803'],
      ['Q3', 'Two 50¢ coins and four 20¢ coins (100¢ + 80¢ = 180¢ = $1.80). Table: 0 → $1.20, 1 → $1.50, 2 → $1.80 ✓'],
      ['Q4', 'Ali: car. Ben: MRT. Mei: bus. Siti: walk.'],
      ['Q5', '(a) 5/10  (b) 2/10  (c) Mei, Ali, Ben'],
      ['Q6', '(a) 10, 12, 14: 6 tables seat 14 people  (b) 9 tables (each table adds 2 seats: 4, 6, 8, … 20)'],
      ['Q7', '463 (4 + 6 + 3 = 13, and 6 is double 3)']
    ]
  },

  script: {
    hook: ['Welcome to Challenge Day, inquirers! Today’s puzzles mix everything from our ten lessons.', 'Clever inquirers do not know every answer straight away. They know how to START: draw it, list it, or make a table.'],
    warmIntro: ['Relay time! I show a card and say a name. That person answers, then picks the next person. A wrong answer gets a friendly “try again”, never a groan.'],
    predict: ['Look at the four station cards. Which one will be hardest? Which way will you start it: draw, list or table? Write your guess.'],
    exploreHints: ['Stuck: “Can you draw it? Can you list the ways in order?”', 'Graph card: “Look at the key first. What is one picture worth?”', 'Finished early: “Is there another answer? How do you know there is not?”'],
    think: ['“Mei had some stickers. She gave half to Ben. Then she gave 6 to Siti and had 4 left. I cannot hold that in my head, so I draw a bar cut into two halves. One half went to Ben. The other half is the 6 for Siti and the 4 left: 6 + 4 = 10. Both halves are the same, so Mei had 10 + 10 = 20 stickers. Check: half of 20 is 10, 10 − 6 = 4 ✓.”', '“Digit cards 2, 0 and 5. How many 3-digit numbers? I list them in order, smallest hundreds digit first. 0 cannot go first. 2: 205, 250. 5: 502, 520. Four numbers, and I know I have them all because I went in order.”', '“Chickens and goats: 7 heads and 20 legs. I make a table. 0 goats: 14 legs. 1 goat: 16. 2 goats: 18. 3 goats: 20 ✓. So 3 goats and 4 chickens. Each goat I swap in adds 2 legs.”'],
    circulate: ['Ask: “How did you start this one? Draw, list or table?”', 'Ask: “How do you know there is only one answer?”', 'Ask: “Show me your check.”'],
    hints: ['Hint 1: “Which lesson does this remind you of?”', 'Hint 2: “Draw it, list it in order, or make a table.”', 'Hint 3: “Try a small number first, then change it one step at a time.”'],
    talk: ['“Which puzzle was hardest today? How did you start it?”', '“When is a table better than a drawing?”'],
    talkAns: 'Open answers. Listen for a clear start (I drew bars, I listed in order, I made a table) and a check (I put my answer back into the puzzle). A table is good when we try 0, 1, 2, 3 … and something grows each time; a drawing is good for before-and-after stories and more-than or fewer-than.',
    close: ['“You are real inquirers now: you notice it, test it and explain why. And when you are stuck, you know how to start.”', 'Give each child a certificate and say one specific thing they did well in the program.']
  },

  deck: {
    today: 'Learn three ways to start a puzzle, then use them on mixed challenges.',
    warmGame: 'Relay review. Six cards, one from each earlier topic: digit cards, missing digits, legs, patterns, change and fractions. Answer, then pass to the next person.',
    warmQs: [['Share 40 stickers equally among 5 children. How many each?', '8'], ['It is 10:55 a.m. What time is it 10 minutes later?', '11:05 a.m.'], ['Which is bigger: 1/3 or 1/5 of the same cake?', '1/3'], ['Half of a circle is called a …', 'Semicircle'], ['I think of a number and add 30. I get 100. What is my number?', '70']],
    expSetup: ['Four station cards: a picture graph, a logic grid, a coin puzzle and a fraction strip.', 'Work in pairs. Read the card aloud.', 'Before you solve it, write how you will start: draw, list or table.', 'Solve it, check it, and be ready to explain.'],
    expPic: 'four puzzle cards on a table: a picture graph with a key, a 3 by 3 logic grid, play coins and a paper strip folded into equal parts.',
    expAsk: [['How did you start each card?', 'Open answers. Draw it, list it, or make a table.'], ['Which card was hardest? Why?', 'Open answers.'], ['What helped when you were stuck?', 'Drawing it, going in order, trying small numbers first, checking with the clues.']],
    mini1: { head: 'Draw it: a before-and-after story', body: ['Mei had some stickers. She gave half of them to Ben.', 'Then she gave 6 to Siti. Now she has 4 left.', 'How many stickers did she have at first?'], ans: '20. The half she kept is 6 + 4 = 10, so she had 10 + 10 = 20. Check: 20 → 10 → 4.' },
    mini2: { head: 'Make a table: heads and legs', body: ['A farm has chickens and goats.', 'There are 7 heads and 20 legs.', 'How many goats are there?'], ans: '3 goats and 4 chickens. Table: 0 goats 14 legs, 1 goat 16, 2 goats 18, 3 goats 20 ✓. Check: 12 + 8 = 20.' },
    keyHead: 'Key idea: how to start a puzzle', keyBig: 'Stuck? Draw it, list it in order, or make a table.', keySmall: 'Then check your answer against every clue and explain why.',
    brk: 'Freeze with maths. Dance until the music stops, then make the shape the tutor calls with your arms: a semicircle, a quarter circle, a cone, a cuboid.',
    ws1: 'Page 1, in pairs: Q1 picture graph, Q2 digit cards, Q3 coins in a table.',
    ws2: 'Page 2, on your own: Q4 logic grid, Q5 cake fractions, Q6 tables in a row, Q7 mystery number.'
  },

  qbank: {
    core: [
      { q: 'Use the digit cards 5, 1 and 9 once each. Make the greatest 3-digit number and the smallest 3-digit number.', a: '951 and 159' },
      { q: 'In a picture graph, each ★ stands for 2 children. Apples has 4 stars. How many children chose apples?', a: '8 children' },
      { q: 'Ali has 3 bags with 5 marbles in each bag. Mei has 4 bags with 4 marbles in each bag. Who has more marbles? How many more?', a: 'Mei, by 1 (Ali 15, Mei 16)' },
      { q: 'Make 80¢ with exactly 3 coins. You can use 5¢, 10¢, 20¢ and 50¢ coins.', a: '50¢ + 20¢ + 10¢ (the only way)' },
      { q: 'A cake is cut into 8 equal pieces. Siti eats 2 pieces and Ben eats 3 pieces. What fraction of the cake is left?', a: '3/8' },
      { q: 'Ben is taller than Ali. Ali is taller than Mei. Siti is taller than Ben. Who is the tallest? Who is the shortest?', a: 'Siti is the tallest. Mei is the shortest.' }
    ],
    stretch: [
      { q: '30 children chose a fruit. In the picture graph each ● stands for 5 children. Apple has ●● and banana has ●●●. The mango row is missing. How many ● should the mango row have?', a: '1 ● (apple 10, banana 15, so mango is 30 − 25 = 5 children)' },
      { q: 'How many 3-digit numbers have digits that add up to 3? List them all.', a: '6: 102, 111, 120, 201, 210, 300' },
      { q: 'Ravi has 4 boxes of 5 pencils and 3 boxes of 10 pencils. He shares all the pencils equally among 5 friends. How many does each friend get?', a: '10 (20 + 30 = 50 pencils; 50 ÷ 5 = 10)' },
      { q: '5, 9, 13, 17, … What is the 10th number in this pattern?', a: '41 (add 4: 21, 25, 29, 33, 37, 41)' },
      { q: 'A farm has chickens and cows. There are 8 heads and 22 legs. How many cows are there?', a: '3 cows and 5 chickens (12 + 10 = 22)' },
      { q: 'Mei spent half of her money on a book. Then she spent $4 on a pen. She has $6 left. How much money did she have at first?', a: '$20 (the half she kept is $4 + $6 = $10)' },
      { q: 'Ali, Ben and Siti each chose a different colour: red, blue or green. Ali did not choose red. Siti chose blue. Who chose green?', a: 'Ali (Siti has blue, Ali is not red, so Ali is green and Ben is red)' },
      { q: 'A rope 30 m long is cut into pieces 5 m long. How many pieces are there? How many cuts?', a: '6 pieces and 5 cuts' }
    ],
    challenge: [
      { q: 'Two numbers add up to 100. One number is 30 more than the other. What are the two numbers?', a: '35 and 65 (take away the extra 30: 70, share: 35 and 35, give 30 back)' },
      { q: 'I am a 3-digit number. My ones digit is 0. My hundreds digit is 2 more than my tens digit. My digits add up to 12. What number am I?', a: '750' },
      { q: 'There are 8 bicycles and tricycles in a park. They have 20 wheels altogether. How many tricycles are there?', a: '4 tricycles and 4 bicycles (12 + 8 = 20)' },
      { q: 'Ali has 9 coins. They are all 10¢ and 20¢ coins. Together they are worth $1.30. How many 20¢ coins does he have?', a: '4 (four 20¢ = 80¢ and five 10¢ = 50¢)' },
      { q: 'Ali, Ben and Mei are 7, 8 and 9 years old. Ali is not the oldest. Mei is older than Ali. Ben is younger than Ali. How old is each child?', a: 'Ben 7, Ali 8, Mei 9' },
      { q: 'A ribbon is cut into 10 equal pieces. Siti uses 3/10 of it and Ben uses 4/10 of it. What fraction is left? Each piece is 5 cm long. How long is the part that is left?', a: '3/10 is left; 15 cm' },
      { q: 'A picture graph has lost its key. Football has 6 pictures and swimming has 4 pictures. 10 more children chose football than swimming. How many children chose swimming? Football?', a: 'Swimming 20, football 30 (2 pictures stand for 10 children, so 1 picture stands for 5)' },
      { q: 'Ali, Ben, Mei and Siti each have one coin: 10¢, 20¢, 50¢ or $1. Mei has more money than Ali but less than Ben. Ben does not have the $1 coin. Who has which coin?', a: 'Ali 10¢, Mei 20¢, Ben 50¢, Siti $1. Ben is not $1 and two people have less than him, so Ben has 50¢; then Ali 10¢ and Mei 20¢, and Siti has the $1.' },
      { q: 'At a hawker centre, chicken rice costs $4 a plate and noodles cost $3 a bowl. Ravi’s family buys 7 dishes for $25. How many plates of chicken rice do they buy?', a: '4 plates of chicken rice and 3 bowls of noodles ($16 + $9 = $25). Table: 0 → $21, 1 → $22, 2 → $23, 3 → $24, 4 → $25 ✓' }
    ]
  },

  workbook: H => [
    H.p('Before you start each puzzle, think: draw it, list it, or make a table? Then check your answer.', { after: 40 }),
    H.q(1, 'The picture graph shows the ice-creams a stall sold.', { before: 40, keepNext: true }),
    H.fig(graphFig),
    H.sub('a', 'How many ice-creams were sold on Tuesday?   ________'),
    H.sub('b', 'How many more were sold on Tuesday than on Wednesday?   ________'),
    H.sub('c', '90 ice-creams were sold in the 4 days. Draw the pictures for Thursday on the graph.'),
    H.sub('d', 'Each ice-cream costs $2. How much money did the stall get on Wednesday?   ________'),
    H.q(2, 'Use each digit card once to make a 3-digit number.', { keepNext: true }),
    H.fig(cardsFig),
    H.sub('a', 'List ALL the 3-digit numbers you can make, in order.   ________________________________'),
    H.sub('b', 'Greatest: ________     Smallest: ________'),
    H.sub('c', 'Which of your numbers are between 300 and 810?   ________________________'),
    H.q(3, 'Ben has 6 coins. They are all 50¢ and 20¢ coins. Together they are worth $1.80. How many of each coin does he have? Make a table.', { keepNext: true }),
    H.tbl([3300, 3300, 3300], [
      H.row(['Number of 50¢', 'Number of 20¢', 'Total'].map(s => H.cell(s, 3300, { bold: true, fill: 'EDEDED', h: 30 }))),
      H.row([H.cell('0', 3300, { h: 30 }), H.cell('6', 3300, { h: 30 }), H.cell('$1.20', 3300, { h: 30 })]),
      ...[1, 2, 3].map(() => H.row([H.cell('', 3300, { h: 30 }), H.cell('', 3300, { h: 30 }), H.cell('', 3300, { h: 30 })]))
    ]),
    H.sub('', 'Ben has ______ 50¢ coins and ______ 20¢ coins.'),
    H.q(4, 'Ali, Mei, Siti and Ben each go to school a different way: bus, MRT, car or walking. Put a tick where it fits and a cross where it cannot.', { pb: true, before: 0, keepNext: true }),
    H.p('Clue 1: Siti lives next to the school, so she walks.   Clue 2: Ben does not go by bus or by car.   Clue 3: Mei does not go by car.', { after: 60, indent: { left: 560 } }),
    H.tbl(W5, [
      H.row(['', 'Bus', 'MRT', 'Car', 'Walk'].map((s, i) => H.cell(s, W5[i], { bold: true, fill: 'EDEDED', h: 30 }))),
      ...['Ali', 'Mei', 'Siti', 'Ben'].map(n => H.row([H.cell(n, W5[0], { bold: true, h: 50 }), ...[1, 2, 3, 4].map(i => H.cell('', W5[i], { h: 50 }))]))
    ]),
    H.sub('', 'Ali: ________   Mei: ________   Siti: ________   Ben: ________'),
    H.q(5, 'A cake is cut into 10 equal pieces. Ali eats 3/10 of the cake. Mei eats 2 more pieces than Ali. Ben eats the rest.', { keepNext: true }),
    H.fig(cakeFig),
    H.sub('a', 'What fraction of the cake does Mei eat?   ________'),
    H.sub('b', 'What fraction of the cake does Ben eat?   ________'),
    H.sub('c', 'Put the children in order, from the one who eats the most.   ______________________'),
    H.q(6, 'Square tables are pushed together in a row.', { keepNext: true }),
    H.fig(tablesFig),
    H.tbl([2400, 1250, 1250, 1250, 1250, 1250, 1250], [
      H.row(['Tables', '1', '2', '3', '4', '5', '6'].map((s, i) => H.cell(s, i ? 1250 : 2400, { bold: true, fill: 'EDEDED', h: 30 }))),
      H.row(['People', '4', '6', '8', '', '', ''].map((s, i) => H.cell(s, i ? 1250 : 2400, { bold: i === 0, h: 30 })))
    ]),
    H.sub('a', 'How many people can sit at 6 tables?   ________'),
    H.sub('b', 'How many tables are needed for 20 people?   ________'),
    H.q(7, 'Who am I? I am a 3-digit number. My hundreds digit is 4. My tens digit is double my ones digit. My digits add up to 13.   ________')
  ]
};
