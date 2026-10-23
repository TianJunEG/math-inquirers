// Math Inquirers P2, Lesson 10: Puzzle Day (mixed puzzles: how to start a puzzle)
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
    const y = 4 + i * 37;
    b += `<rect x="0" y="${y}" width="600" height="37" fill="${i % 2 ? W : SKY}"/>` + txt(12, y + 24, d, 16, { a: 'start' });
    if (k) for (let j = 0; j < k; j++) b += cone(130 + j * 36, y + 1);
    else b += txt(130, y + 24, 'Draw the pictures for Thursday here.', 15, { a: 'start', c: TEAL, w: 600 });
  });
  b += `<rect x="0" y="4" width="600" height="148" fill="none" stroke="${N}" stroke-width="2"/><line x1="118" y1="4" x2="118" y2="152" stroke="${N}" stroke-width="2"/>`;
  b += cone(200, 156) + txt(236, 182, '= 5 ice-creams', 17, { a: 'start' });
  return svg(600, 192, b, 'Picture graph of ice-creams sold. Monday 4 pictures, Tuesday 6, Wednesday 3, Thursday blank. Each picture stands for 5 ice-creams.');
})();
const cakeFig = svg(600, 64, `<rect x="50" y="8" width="500" height="48" rx="6" fill="${Y}" stroke="${N}" stroke-width="3"/>` + Array.from({ length: 9 }, (_, i) => `<line x1="${100 + i * 50}" y1="8" x2="${100 + i * 50}" y2="56" stroke="${N}" stroke-width="2.5"/>`).join(''), 'A cake cut into 10 equal pieces in a row');
const towersFig = (() => {
  // Tower 1 = 4 cubes, Tower 2 = 8 cubes, Tower 3 = 12 cubes (one cube = 9 px high)
  let b = '', x = 150; const c = 9;
  [1, 2, 3].forEach(n => {
    for (let i = 0; i < 4 * n; i++) b += `<rect x="${x}" y="${118 - (i + 1) * c}" width="${c * 3}" height="${c}" fill="${Y}" stroke="${N}" stroke-width="1.5"/>`;
    b += txt(x + c * 1.5, 138, 'Tower ' + n, 15);
    x += 110;
  });
  return `<svg viewBox="0 0 600 146" width="420" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Three towers of cubes. Tower 1 has 4 cubes, Tower 2 has 8 cubes, Tower 3 has 12 cubes" style="max-width:100%">${b}</svg>`;
})();
const W5 = [2300, 1900, 1900, 1900, 1900];

/* ---------- module ---------- */
module.exports = {
  lesson: {
    n: 10, week: 5, session: 'B', title: 'Puzzle Day', topic: 'Mixed Puzzles',
    objective: 'Choose a way to start a puzzle (draw it, list it in order, make a table) and use it on mixed puzzles: picture graphs with a key of 5 or 10, a logic grid with exactly one answer, numbers to 1000, money, fractions, and × and ÷ with the 2, 3, 4, 5 and 10 tables. Check the answer and explain it.',
    skills: 'Choosing a strategy, drawing models, listing in order, making tables, logical elimination, checking, explaining',
    materials: 'Four station cards (all on one slide in the deck, and printed in the tutor guide), play coins, digit cards 0 to 9, paper strips for fractions, mini whiteboards, certificates, stamps.',
    online: 'Each breakout pair takes two station cards (the tutor pastes their text into the breakout room chat), about 2 minutes a card, and everyone reports back to the group. Each child needs digit cards (cut from paper), a pencil and a mini whiteboard.',
    warmup: 'Relay review: three quick cards (digits, change, fractions; spare: missing digits, legs, patterns). A volunteer answers, then chooses a friend who has not had a turn; any child may pass.',
    explore: 'Four station cards on one slide; each breakout pair takes two, about 2 minutes each (a tutor cannot visit four physical stations online): Card 1 a picture graph with a key of 5, Card 2 a logic grid about pets, Card 3 a coin puzzle (70¢ with exactly 4 coins), Card 4 a fraction strip cut into 8 parts. Pairs write how they started each one: draw, list or table.',
    mini: 'How to start a puzzle. Draw it: bars for before-and-after stories (Mei gave half her stickers away, then 6 more, and has 4 left: the half she kept is 4 + 6 = 10, so she had 20). List it in order: digit cards 2, 0, 5 make 205, 250, 502, 520 (0 cannot go first). Make a table: 7 heads and 20 legs, chickens and goats; try 0, 1, 2, 3 goats until the legs are 20 (3 goats, 4 chickens). Then check and explain.',
    share: 'Pick one puzzle and teach it to the group in two sentences: how you started it, and how you know your answer is right.',
    exit: { q: '5 bicycles and tricycles have 13 wheels altogether. How many tricycles are there? How did you start?', a: '3 tricycles and 2 bicycles (9 + 4 = 13). A table of 0, 1, 2, 3 tricycles works well.' },
    mistakes: ['Picture graph: counting the pictures instead of using the key (writing 6 instead of 30 for Tuesday).', 'Listing: putting 0 first (038 is not a 3-digit number) or missing a number because the list is not in order.', 'Logic grid: putting a tick without crossing out the rest of that row and column, so the next clue cannot be used.'],
    takehome: 'Page 1: the whole of Q3 (the coins table, 6 coins worth $1.80). The how-to-start teaching slide is not shown separately: the key idea slide says the same.',
    extension: 'Write a challenge puzzle for next year’s group, with the answer and a hint that says how to start it. Check it has exactly one answer.',
    key: [
      ['Q1', '(a) 30  (b) Thursday sold 25 ice-creams: draw 5 pictures (90 − 20 − 30 − 15 = 25)  (c) $30 (15 ice-creams at $2 each)'],
      ['Q2', '(a) 308, 380, 803, 830  (b) Greatest 830, smallest 308  (c) 308, 380, 803'],
      ['Q3', 'Two 50¢ coins and four 20¢ coins (100¢ + 80¢ = 180¢ = $1.80). Table: 0 → $1.20, 1 → $1.50, 2 → $1.80 ✓'],
      ['Q4', 'Ali: car. Ben: MRT. Mei: bus. Siti: walk.'],
      ['Q5', '(a) 5/10  (b) 2/10  (c) Mei, Ali, Ben'],
      ['Q6', '(a) 16, 20, 24 cubes in Towers 4, 5, 6; Tower 8 has 32 cubes (each tower adds 4: 4, 8, 12, 16, 20, 24, 28, 32)  (b) Tower 9 (36 cubes: 4 × 9, or keep adding 4: 32, 36)']
    ]
  },

  script: {
    hook: ['Welcome to Puzzle Day, inquirers! Today’s puzzles mix everything from our ten lessons.', 'Clever inquirers do not know every answer straight away. They know how to START: draw it, list it, or make a table.'],
    warmIntro: ['Relay time! I show a card and ask for a volunteer. That person answers, then chooses a friend who has not had a turn. You can always say pass. A different answer gets “let us test that”, never a groan.'],
    predict: ['Look at the four station cards. Which one will be hardest? Which way will you start it: draw, list or table? Write your guess.'],
    exploreHints: ['Stuck: “Can you draw it? Can you list the ways in order?”', 'Graph card: “Look at the key first. What is one picture worth?”', 'Finished early: “Is there another answer? How do you know there is not?”'],
    think: ['“Mei had some stickers. She gave half to Ben. Then she gave 6 to Siti and had 4 left. I cannot hold that in my head, so I draw a bar cut into two halves. One half went to Ben. The other half is the 6 for Siti and the 4 left: 6 + 4 = 10. Both halves are the same, so Mei had 10 + 10 = 20 stickers. Check: half of 20 is 10, 10 − 6 = 4 ✓.”', '“Digit cards 2, 0 and 5. How many 3-digit numbers? I list them in order, smallest hundreds digit first. 0 cannot go first. 2: 205, 250. 5: 502, 520. Four numbers, and I know I have them all because I went in order.”', '“Chickens and goats: 7 heads and 20 legs. I make a table. 0 goats: 14 legs. 1 goat: 16. 2 goats: 18. 3 goats: 20 ✓. So 3 goats and 4 chickens. Each goat I swap in adds 2 legs.”'],
    circulate: ['Ask: “How did you start this one? Draw, list or table?”', 'Ask: “How do you know there is only one answer?”', 'Ask: “Show me your check.”'],
    hints: ['Hint 1: “Which lesson does this remind you of?”', 'Hint 2: “Draw it, list it in order, or make a table.”', 'Hint 3: “Try a small number first, then change it one step at a time.”'],
    talk: ['“Which puzzle was hardest today? How did you start it?”'],
    talkAns: 'Open answers. Listen for a clear start (I drew bars, I listed in order, I made a table) and a check (I put my answer back into the puzzle).',
    close: ['“You are real inquirers now: you notice it, test it and explain why. And when you are stuck, you know how to start.”', 'Give each child a certificate and say one specific thing they did well in the program.']
  },

  deck: {
    today: 'Learn three ways to start a puzzle, then use them on mixed challenges.',
    warmGame: 'Relay review. Three cards: digit cards, change and fractions (spare: missing digits, legs, patterns). A volunteer answers, then chooses a friend who has not had a turn (pass is always fine).',
    warmQs: [['Share 40 stickers equally among 5 children. How many each?', '8'], ['It is 10:55 am. What time is it 10 minutes later?', '11:05 am'], ['Which is bigger: 1/3 or 1/5 of the same cake?', '1/3'], ['Half of a circle is called a …', 'Half circle'], ['I think of a number and add 30. I get 100. What is my number?', '70']],
    expSetup: ['Your pair takes two station cards (for example 1 and 3, or 2 and 4).', 'Read the card aloud. Before you solve it, write how you will start: draw, list or table.', 'Solve it and check it (about 2 minutes a card). Then take the other card.', 'Be ready to explain how you started and how you know.'],
    expPic: 'four puzzle cards on a table: a picture graph with a key, a 3 by 3 logic grid, play coins and a paper strip folded into equal parts.',
    stationCards: [["Card 1: picture graph", "Each picture stands for 5 books. Monday has 3 pictures, Tuesday 5 pictures, Wednesday 2 pictures. How many books were read on these 3 days?", "50 books (10 pictures × 5)"], ["Card 2: logic grid", "Ali, Ben and Cai each have one pet: a cat, a dog or a fish. Ben has the fish. Ali does not have the dog. Who has the cat?", "Ali has the cat (Ben has the fish, so Ali and Cai share the cat and the dog; Ali does not have the dog, so Ali has the cat and Cai has the dog)"], ["Card 3: coin puzzle", "Make 70¢ with exactly 4 coins. You can use 5¢, 10¢, 20¢ and 50¢ coins. Find all the ways.", "2 ways: 50¢ + 10¢ + 5¢ + 5¢, and 20¢ + 20¢ + 20¢ + 10¢"], ["Card 4: fraction strip", "A strip is cut into 8 equal parts. 3 parts are red and 2 parts are blue. What fraction is NOT coloured?", "3/8"]],
    expAsk: [['How did you start each card?', 'Open answers. Draw it, list it, or make a table.'], ['Which card was hardest? Why?', 'Open answers.'], ['What helped when you were stuck?', 'Drawing it, going in order, trying small numbers first, checking with the clues.']],
    mini1: { head: 'Draw it: a before-and-after story', body: ['Mei had some stickers. She gave half of them to Ben.', 'Then she gave 6 to Siti. Now she has 4 left.', 'How many stickers did she have at first?'], ans: '20. The half she kept is 6 + 4 = 10, so she had 10 + 10 = 20. Check: 20 → 10 → 4.' },
    mini2: { head: 'Make a table: heads and legs', body: ['A farm has chickens and goats.', 'There are 7 heads and 20 legs.', 'How many goats are there?'], ans: '3 goats and 4 chickens. Table: 0 goats 14 legs, 1 goat 16, 2 goats 18, 3 goats 20 ✓. Check: 12 + 8 = 20.' },
    keyHead: 'Key idea: how to start a puzzle', keyBig: 'Stuck? Draw it, list it in order, or make a table.', keySmall: 'Then check your answer against every clue and explain why.',
    brk: 'Freeze with maths. Dance until the music stops, then make the shape the tutor calls with your arms: a half circle, a quarter circle, a cone, a cuboid.',
    ws1: 'Page 1, in pairs: Q1 picture graph, Q2 digit cards, Q3 coins in a table.',
    ws2: 'Page 2, on your own: Q4 logic grid, Q5 cake fractions, Q6 towers of cubes.'
  },

  qbank: {
    core: [
      { q: 'Use the digit cards 5, 1 and 9 once each. Make the greatest 3-digit number and the smallest 3-digit number.', a: '951 and 159' },
      { q: 'In a picture graph, each picture stands for 2 children. Apples has 4 pictures. How many children chose apples?', a: '8 children' },
      { q: 'Ali has 3 bags with 5 marbles in each bag. Mei has 4 bags with 4 marbles in each bag. Who has more marbles? How many more?', a: 'Mei, by 1 (Ali 15, Mei 16)' },
      { q: 'Make 80¢ with exactly 3 coins. You can use 5¢, 10¢, 20¢ and 50¢ coins.', a: '50¢ + 20¢ + 10¢ (the only way)' },
      { q: 'A cake is cut into 8 equal pieces. Siti eats 2 pieces and Ben eats 3 pieces. What fraction of the cake is left?', a: '3/8' },
      { q: 'Ben is taller than Ali. Ali is taller than Mei. Siti is taller than Ben. Who is the tallest? Who is the shortest?', a: 'Siti is the tallest. Mei is the shortest.' }
    ],
    stretch: [
      { q: '30 children chose a fruit. In the picture graph each picture stands for 5 children. Apple has 2 pictures and banana has 3 pictures. The mango row is missing. How many pictures should the mango row have?', a: '1 picture (30 − 10 − 15 = 5 children)' },
      { q: 'Mei saves $3 on day 1, $6 on day 2, $9 on day 3, and so on ($3 more each day). Ali saves $10 every day. Make a table of how much each child has saved altogether after each day. On which day does Mei FIRST have more than Ali?', a: 'Day 6. Mei’s totals: $3, $9, $18, $30, $45, $63. Ali’s totals: $10, $20, $30, $40, $50, $60. On day 6 Mei has $63 and Ali has $60. (On day 5 Mei still has less: $45 and $50.)' },
      { q: 'A bus had some people on it. At the first stop half of the people got off. At the second stop 6 people got on. Now there are 14 people on the bus. How many people were on the bus at the start? Draw a bar to start.', a: '16 (14 − 6 = 8 is half, 8 + 8 = 16).' },
      { q: '5, 9, 13, 17, … Will 49 be in this pattern? Will 50? How do you know?', a: '49 will be in the pattern and 50 will not. The pattern adds 4 each time, so every number in it is 1 more than a number in the 4 times table: 5 = 4 + 1, 9 = 8 + 1, 13 = 12 + 1. 49 = 48 + 1, but 50 is 2 more than 48.' },
      { q: 'A farm has chickens and cows. There are 8 heads and 22 legs. How many cows are there?', a: '3 cows and 5 chickens (12 + 10 = 22)' },
      { q: 'Mei spent half of her money on a book. Then she spent $4 on a pen. She has $6 left. How much money did she have at first?', a: '$20 (the half she kept is $4 + $6 = $10)' },
      { q: 'Ali, Ben and Siti each chose a different colour: red, blue or green. Ali did not choose red. Siti chose blue. Who chose green?', a: 'Ali (Siti has blue, Ali is not red, so Ali is green and Ben is red)' },
      { q: 'A rope 30 m long is cut into pieces 5 m long. How many pieces are there? How many cuts?', a: '6 pieces and 5 cuts' }
    ],
    challenge: [
      { q: 'Use three DIFFERENT digit cards to make 3-digit numbers. With the cards 0, 3 and 8 you can make exactly 4 numbers. With the cards 3, 5 and 8 you can make 6. Which sets of three different cards make exactly 4 numbers? Test some sets and write a rule. Does your rule always work?', a: 'Exactly the sets with a 0 card: 0, a, b make a0b, ab0, b0a, ba0. Sets without 0 make 6.' },
      { q: 'Ali, Mei, Siti and Ben each go to school a different way: bus, MRT, car or walking. Clues: Siti walks. Ben does not go by bus or by car. Mei does not go by car. Who goes by what? Then take away ONE clue at a time. Which clue could you take away and still have exactly one answer? How many answers does each clue-less puzzle have?', a: 'Ali car, Mei bus, Siti walks, Ben MRT. No clue can go (8, 4 or 2 answers).' },
      { q: 'A cake is cut into 12 equal slices and shared by Mei, Ali and Ben. Ben gets 2 more slices than Mei, and Ali gets 2 more slices than Ben. What fraction of the cake does each child get? Each slice weighs 100 g. How heavy is Ali’s share?', a: 'Mei 2/12, Ben 4/12, Ali 6/12 (2 + 4 + 6 = 12). Ali’s share is 6 slices × 100 g = 600 g. How to start: draw the three bars, take away the extras (2 + 4 = 6), share the other 6 equally (2 each), then put the extras back.' },
      { q: 'Ali saves 20¢ on day 1, 40¢ on day 2, 60¢ on day 3, and so on, saving 20¢ more each day. On which day will the TOTAL he has saved first be MORE than $2? Make a table of the day, the amount saved that day, and the total so far.', a: 'Day 5. Totals so far: day 1 20¢, day 2 60¢, day 3 $1.20, day 4 $2.00 (exactly $2, not more), day 5 $3.00.' },
      { q: 'Make up your own challenge puzzle for next year’s group. It can be about digits, money, patterns, fractions, shapes or logic. Write the puzzle, its answer, and a hint that says how to start (draw it, list it or make a table). Check that it has exactly ONE answer. Swap with a partner: can they solve it using your hint?', a: 'Open. Check that the puzzle has exactly one answer (try to find a second one), that the hint names a way to start, and that the answer is checked against every clue. Example: “Ali has 5 coins, all 10¢ or 20¢, worth 90¢. How many of each?” The answer is one 10¢ and four 20¢ (10 + 80 = 90), and it is the only one, because each swap of a 10¢ for a 20¢ adds exactly 10¢.' },
      { q: 'A ribbon is cut into 10 equal pieces. Siti uses 3/10 of it and Ben uses 4/10 of it. What fraction is left? Each piece is 5 cm long. How long is the part that is left?', a: '3/10 is left; 15 cm' },
      { q: 'A picture graph has lost its key. Football has 6 pictures and swimming has 4 pictures. 10 more children chose football than swimming. How many children chose swimming? Football?', a: 'Swimming 20, football 30 (2 pictures stand for 10 children, so 1 picture stands for 5)' },
      { q: 'Ali, Ben, Mei and Siti each have one coin: 10¢, 20¢, 50¢ or $1. Mei has more money than Ali but less than Ben. Ben does not have the $1 coin. Who has which coin?', a: 'Ali 10¢, Mei 20¢, Ben 50¢, Siti $1. Ben is not $1 and two people have less than him, so Ben has 50¢; then Ali 10¢ and Mei 20¢, and Siti has the $1.' },
      { q: 'At a hawker centre, chicken rice costs $4 a plate and noodles cost $3 a bowl. Ravi’s family buys 7 dishes for $25. How many plates of chicken rice do they buy? What is the smallest total 7 dishes can cost? The biggest? Can 7 dishes cost $30? Can they cost EVERY whole-dollar amount in between?', a: '4 plates of chicken rice and 3 bowls of noodles ($16 + $9 = $25). Table: 0 plates → $21, 1 → $22, 2 → $23, 3 → $24, 4 → $25 ✓. Smallest $21 (all noodles), biggest $28 (all chicken rice), so $30 is impossible. Each swap of a bowl for a plate adds exactly $1, so every whole dollar from $21 to $28 is possible.' }
    ]
  },

  workbook: H => [
    H.q(1, 'The picture graph shows the ice-creams a stall sold.', { before: 40, keepNext: true }),
    H.fig(graphFig),
    H.sub('a', 'How many ice-creams were sold on Tuesday?   ______'),
    H.sub('b', '90 ice-creams were sold in the 4 days. Draw Thursday’s pictures on the graph.'),
    H.sub('c', 'Each ice-cream costs $2. How much did the stall get on Wednesday?  ______'),
    H.q(2, 'Use the digit cards  3,  0  and  8  once each to make a 3-digit number.', { keepNext: true }),
    H.sub('a', 'List ALL the numbers in order.  ______________________________'),
    H.sub('b', 'Greatest: ________     Smallest: ________'),
    H.sub('c', 'Which of them are between 300 and 810?  ______________________'),
    H.q(3, [H.t('★ take-home  ', { bold: true, color: 'B45F06' }), H.t('Ben has 6 coins. They are all 50¢ and 20¢ coins. Together they are worth $1.80. How many of each coin does he have? Make a table.')], { keepNext: true }),
    H.tbl([3300, 3300, 3300], [
      H.row(['Number of 50¢', 'Number of 20¢', 'Total'].map(s => H.cell(s, 3300, { bold: true, fill: 'EDEDED', h: 30 }))),
      H.row([H.cell('0', 3300, { h: 30 }), H.cell('6', 3300, { h: 30 }), H.cell('$1.20', 3300, { h: 30 })]),
      ...[1, 2, 3].map(() => H.row([H.cell('\u00a0', 3300, { h: 20 }), H.cell('\u00a0', 3300, { h: 20 }), H.cell('\u00a0', 3300, { h: 20 })]))
    ]),
    H.sub('', 'Ben has ______ 50¢ coins and ______ 20¢ coins.'),
    H.q(4, 'Ali, Mei, Siti and Ben each go to school a different way: bus, MRT, car or walking. Put a tick where it fits and a cross where it cannot.', { pb: true, before: 0, keepNext: true }),
    H.fig('<div style="text-align:left;padding-left:40px;line-height:1.6">Clue 1: Siti lives next to the school, so she walks.<br>Clue 2: Ben does not go by bus or by car.<br>Clue 3: Mei does not go by car.</div>'),
    H.tbl(W5, [
      H.row(['', 'Bus', 'MRT', 'Car', 'Walk'].map((s, i) => H.cell(s, W5[i], { bold: true, fill: 'EDEDED', h: 30 }))),
      ...['Ali', 'Mei', 'Siti', 'Ben'].map(n => H.row([H.cell(n, W5[0], { bold: true, h: 40 }), ...[1, 2, 3, 4].map(i => H.cell('', W5[i], { h: 40 }))]))
    ]),
    H.sub('', 'Ali: ________   Mei: ________   Siti: ________   Ben: ________'),
    H.q(5, 'A cake is cut into 10 equal pieces. Ali eats 3/10 of the cake. Mei eats 2 more pieces than Ali. Ben eats the rest.', { keepNext: true }),
    H.fig(cakeFig),
    H.sub('a', 'What fraction of the cake does Mei eat?   ________'),
    H.sub('b', 'What fraction of the cake does Ben eat?   ________'),
    H.sub('c', 'Order the children, the one who eats the most first.  __________________'),
    H.q(6, 'Ben builds towers with cubes. Tower 1 has 4 cubes, Tower 2 has 8 cubes and Tower 3 has 12 cubes. Keep the pattern going.', { keepNext: true }),
    H.fig(towersFig),
    H.tbl([2400, 1250, 1250, 1250, 1250, 1250, 1250], [
      H.row(['Tower', '1', '2', '3', '4', '5', '6'].map((s, i) => H.cell(s, i ? 1250 : 2400, { bold: true, fill: 'EDEDED', h: 30 }))),
      H.row(['Cubes', '4', '8', '12', '', '', ''].map((s, i) => H.cell(s, i ? 1250 : 2400, { bold: i === 0, h: 60 })))
    ]),
    H.sub('a', 'How many cubes are in Tower 8?   ________', { after: 60 }),
    H.sub('b', 'Which tower has 36 cubes?   Tower ________')
  ]
};
