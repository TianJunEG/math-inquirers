// Math Inquirers P5 — Lesson 3: Before and After (fraction word problems with units: before-and-after models,
// fraction of a remainder, constant total, constant difference, one amount unchanged).
// Every answer below was worked out with units and checked by brute force with exact fractions (Python).

const NAVY = '#1B2A49', YEL = '#FFC93C', SKY = '#DDEBF7', TEAL = '#1F7A6F', WHITE = '#FFFFFF';
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const T = (x, y, s, o = {}) => `<text x="${x}" y="${y}" font-size="${o.size || 15}" font-weight="${o.weight || 700}" text-anchor="${o.anchor || 'middle'}" fill="${o.fill || NAVY}" font-family="Arial">${esc(s)}</text>`;
const box = (x, y, w, h, fill = WHITE) => `<rect x="${x}" y="${y}" width="${w}" height="${h}" fill="${fill}" stroke="${NAVY}" stroke-width="2"/>`;
const svg = (w, h, label, inner, px) => `<svg aria-label="${esc(label)}" viewBox="0 0 ${w} ${h}" xmlns="http://www.w3.org/2000/svg" style="width:${px || w}px;max-width:100%">${inner}</svg>`;

// Q1: an empty bar for Ravi's money, for children to divide
const raviBar = () => svg(600, 70, 'An empty bar labelled Ravi’s money at first, to be divided into units',
  T(112, 41, 'Ravi’s money', { anchor: 'end' }) + box(122, 16, 460, 40) + T(352, 68, 'Divide the bar: the book, the pen and what is left.', { size: 14, weight: 400 }));

// Q2: the After model drawn as units (Siti 3 units, Mei 4 units)
const afterModel = () => {
  let s = T(10, 20, 'After Siti gave Mei 12 stickers:', { anchor: 'start', fill: TEAL });
  s += T(78, 55, 'Siti', { anchor: 'end' });
  for (let i = 0; i < 3; i++) s += box(90 + i * 64, 34, 64, 32, YEL);
  s += T(78, 99, 'Mei', { anchor: 'end' });
  for (let i = 0; i < 4; i++) s += box(90 + i * 64, 78, 64, 32, SKY);
  s += T(470, 78, 'Draw the Before model', { size: 14, weight: 400 }) + T(470, 96, 'on the right of this.', { size: 14, weight: 400 });
  return svg(600, 120, 'After model: Siti has 3 equal units and Mei has 4 equal units', s);
};

module.exports = {
  lesson: {
    n: 3, week: 2, session: 'A', title: 'Before and After', topic: 'Fraction Word Problems',
    objective: 'Solve fraction word problems with units and before-and-after models: fraction of a remainder, giving between two people (the total stays the same), both getting or spending the same amount (the difference stays the same), and one amount that does not change.',
    skills: 'Drawing bar models, choosing what stays the same, splitting parts into equal units, working backwards, checking an answer against every condition',
    materials: 'Mini whiteboard and marker, 24 counters or paper squares (two colours), paper strips for bar models, workbook, pencil.',
    online: 'The tutor shares the slides and builds each bar model click by click. Children draw their models on whiteboards and hold them up to the camera together. For the explore, each child moves paper squares on the desk with the camera pointing down.',
    warmup: 'What’s left? A jar has 120 marbles. Three cards are turned over one at a time: give away 1/4, give away 1/3 of what is left, give away 5/6 of what is left. Children track what is left on whiteboards (90, 60, 10).',
    explore: 'Counter swap. Ali has 18 counters and Mei has 6. Pairs move counters from Ali to Mei one at a time and record Ali, Mei, the total and the difference in a table. Then they start again and give BOTH children 2 more counters each time. What never changes in each table? When does Mei have 1/2 as many as Ali?',
    mini: 'Fractions become equal units in a bar. Fraction of a remainder: cut the parts that are left into equal units so every part is the same size. Before you draw a before-and-after model, ask what stays the same: the total (one gives to the other), the difference (both get or spend the same) or one amount (only the other changes). Draw that part the same in both models.',
    share: 'Ali has 50 marbles and Mei has 30. Ali gives Mei some marbles. Can the difference still be 20 afterwards?',
    exit: { q: 'Ali had 35 stickers and Siti had 25. How many stickers must Ali give Siti so that Ali has 1/2 as many stickers as Siti?', a: '15 (the total stays 60; 3 units = 60, so Ali has 1 unit = 20 at the end: 35 − 20 = 15)' },
    mistakes: ['Taking the second fraction of the whole amount instead of the remainder (1/4 of the remainder read as 1/4 of all the money).', 'Thinking the difference goes down by 10 when one person gives the other 10 (it goes down by 20: one loses 10, the other gains 10).', 'Keeping the units from the Before model when the thing that stays the same is a different amount, so the units in the two models are not the same size.'],
    extension: 'Make up your own before-and-after story where the total stays the same and the answer is 24. Swap with a partner and solve each other’s story with a model.',
    key: [
      ['Q1', '(a) 1/6 (1/4 of the 2/3 that was left)  (b) $72 (3 units = $36 left out of 6 units, 1 unit = $12)  (c) $12 (book $24, pen $12)'],
      ['Q2', '(a) 84 (giving does not change the total)  (b) Siti 48, Mei 36 (after: 7 units = 84, 1 unit = 12; Siti 36 + 12 = 48)'],
      ['Q3', '(a) No. If Ali gives 20, Ali has 30 and Ben has 50. Giving 10 makes them the same (40 each): Ali loses 10 and Ben gains 10, so the gap of 20 closes by 20.  (b) 20 (total 80 = 8 units, 1 unit = 10; Ali 30, Ben 50)'],
      ['Q4', '(a) The difference: $24  (b) $22 (the difference $24 is 1 unit; Ali 2 units = $48, so $48 − $26 = $22)'],
      ['Q5', '(a) $50 each (difference $30 = 3 units, 1 unit = $10; Siti $10, Mei $40)  (b) Mei $40, Siti $10'],
      ['Q6', '(a) Blue (only red beads were added)  (b) 70 (blue 4 units, red 3 units → 6 units; 3 units = 30, 1 unit = 10)  (c) 100']
    ]
  },

  script: {
    hook: ['Welcome back, inquirers! Today’s problems all have a story with a BEFORE and an AFTER: someone spends money, gives away stickers, or gets a bit older.', 'The trick that makes them easy is to notice what stays the same. Notice it, test it, explain why.'],
    warmIntro: ['A jar has 120 marbles. I will turn over three cards. After each card, write how many marbles are LEFT. Careful: read whether the card says “of the whole jar” or “of what is left”.', 'How did you find 1/3 of what was left? Show me your bar.'],
    predict: ['Ali has 18 counters and Mei has 6. Ali gives Mei counters one at a time. Before you move any, predict: what will happen to the total? To the difference?', 'Now both children get 2 more counters each time. Predict again: total or difference, which one stays the same?'],
    exploreHints: ['Stuck: make a table with four columns, Ali, Mei, total, difference, and fill one row after every move.', 'Not sure about the difference: line the two rows of counters up side by side and count the extra ones.', 'Finished early: how many counters must Ali give so that Mei has 1/3 as many as Ali? (He gives 0: she already does, 6 is 1/3 of 18.) What about 3/5 as many? (Ali gives 3: 15 and 9.)'],
    think: ['“Mei spent 2/5 on a bag, so I draw 5 parts and shade 2. Then 1/2 of the REMAINDER on shoes. The remainder is 3 parts and I can’t halve 3 parts nicely, so I cut every part into 2. Now there are 10 equal units: bag 4, shoes 3, left 3.”', '“3 units are $27, so 1 unit is $9 and 10 units are $90. Check: bag $36, shoes $27, left $27. That adds to $90.”', '“Ali gives Ben 14 cards. Did the total change? No, the cards only moved. So the total after is still 96. After, Ali has 1/3 as many as Ben: Ali 1 unit, Ben 3 units. 4 units = 96, 1 unit = 24. Ali had 14 more before: 38.”'],
    circulate: ['Ask: “What stays the same in this story: the total, the difference, or one amount? How do you know?”', 'Ask: “Are your units all the same size? Point to one unit and tell me what it is worth.”', 'Ask: “Check your answer in the story. Does every sentence still work?”'],
    hints: ['Hint 1: “Draw the AFTER model first. That is the part with the fraction.”', 'Hint 2: “Which amount did not change? Label it with its number in BOTH models.”', 'Hint 3: “Find what 1 unit is worth, then work backwards to the start.”'],
    talk: ['“Ali has 50 marbles and Mei has 30. Ali gives Mei some marbles. Can the difference still be 20 afterwards?”', '“When does the total stay the same, and when does the difference stay the same?”'],
    talkAns: 'Yes. If Ali gives Mei 20 marbles, Ali has 30 and Mei has 50: the difference is 20 again, but now Mei has more. The total is 80 the whole time. Giving between two people keeps the total the same; both getting (or spending) the same amount keeps the difference the same.',
    close: ['“Today you drew models with a before and an after, and you found the part that stays the same. Next time a story changes, ask yourself: what did NOT change?”', '“Show me your exit ticket and collect your stamp.”']
  },

  deck: {
    today: 'Draw before-and-after models, find what stays the same, and solve fraction stories with units.',
    warmGame: 'What’s left? A jar has 120 marbles. Turn over one card at a time: give away 1/4; give away 1/3 of what is left; give away 5/6 of what is left. Children write how many are left after each card.',
    warmQs: [['What is 2/5 of 45?', '18'], ['3/4 of a number is 27. What is the number?', '36'], ['What is 1/3 of 3/4?', '1/4'], ['Ali has 12 more stickers than Ben. Each gets 5 more. What is the difference now?', 'Still 12'], ['Ali has 30 cards and Ben has 20. Ali gives Ben 5. What is the total now?', 'Still 50']],
    expSetup: ['Ali takes 18 counters. Mei takes 6 counters.', 'Ali gives Mei 1 counter at a time. After each move write Ali, Mei, the total and the difference in a table.', 'Start again from 18 and 6. This time give BOTH children 2 more counters each time. Fill in a new table.', 'What never changes in each table? When does Mei have 1/2 as many counters as Ali?'],
    expPic: 'two rows of counters: Ali’s row of 18 yellow counters and Mei’s row of 6 blue counters, with an arrow from Ali’s row to Mei’s row.',
    expAsk: [['What stayed the same when Ali gave counters to Mei?', 'The total: 24 every time.'], ['What stayed the same when both children got 2 more?', 'The difference: 12 every time.'], ['When did Mei have 1/2 as many as Ali?', 'After Ali gave 2 (16 and 8), and after both got 6 more (24 and 12).']],
    mini1: { head: 'Fraction of a remainder', body: ['Mei spent 2/5 of her money on a bag and 1/2 of the remainder on shoes. She had $27 left.', 'How much money did she have at first? Cut the remaining parts into equal units.'], ans: '$90 (10 units; 3 units = $27, 1 unit = $9).' },
    mini2: { head: 'The total stays the same', body: ['Ali and Ben had 96 cards altogether. Ali gave Ben 14 cards. Then Ali had 1/3 as many cards as Ben.', 'How many cards did Ali have at first?'], ans: '38 (after: 4 units = 96, Ali 1 unit = 24; 24 + 14 = 38).' },
    keyHead: 'Key idea: find what stays the same',
    keyBig: 'Ask what stays the same: the total, the difference, or one amount. Draw it the same in the Before and the After model.',
    keySmall: 'Fraction of a remainder: cut the parts that are left into equal units.',
    brk: 'Fraction stretch. Arms wide is the whole. Show 1/2, then 1/4, then 3/4 of the whole with your arms. Touch your toes for 0!',
    ws1: 'Page 1, in pairs: Q1 fraction of a remainder, Q2 the sticker swap (total stays the same), Q3 Ali and Ben’s marbles.',
    ws2: 'Page 2, on your own: Q4 the same gift for both, Q5 the same spending for both, Q6 the bead box.'
  },

  qbank: {
    core: [
      { q: 'A baker made some buns. She sold 2/5 of them in the morning and 1/3 of the remaining buns in the afternoon. She had 120 buns left. How many buns did she make?', a: '300 (left = 2/3 of 3/5 = 2/5 of all the buns; 2/5 = 120, so 1/5 = 60). She sold 60 in the afternoon.' },
      { q: 'Ben is 10 years old and his father is 38. In how many years will Ben’s age be 1/2 of his father’s age?', a: '18 years (the difference, 28, is 1 unit; Ben will be 28 and his father 56)' },
      { q: 'Siti had $60. She spent 1/4 of it on a book and 1/3 of the remainder on a T-shirt. How much money did she have left?', a: '$30 (book $15, remainder $45, T-shirt $15)' },
      { q: 'Ali had 26 stamps and Ravi had 34. How many stamps must Ravi give Ali so that they have the same number?', a: '4 (the total is 60, so 30 each)' },
      { q: 'There are 40 pupils in a hall. 3/8 of them are boys. How many more girls than boys are there?', a: '10 (15 boys and 25 girls)' },
      { q: 'Mei and Siti had the same amount of money. Mei spent $18 and Siti spent $42. Then Siti had 1/3 as much money as Mei. How much did each of them have at first?', a: '$54 (after: the difference $24 is 2 units, so 1 unit = $12; Siti $12 + $42 = $54; Mei $36 + $18 = $54)' }
    ],
    stretch: [
      { q: 'Ravi spent 1/4 of his money on Monday and 2/5 of the remainder on Tuesday. He spent $66 altogether. How much money did he have at first?', a: '$120 (20 units: Monday 5 units, Tuesday 6 units; 11 units = $66, so 1 unit = $6)' },
      { q: 'A box had red pens and blue pens. 2/3 of the pens were blue. After 12 blue pens were taken out, 1/2 of the pens were blue. How many pens were in the box at first?', a: '36 (the red pens did not change: red 1 unit, blue 2 units at first, 1 unit after; 1 unit = 12)' },
      { q: 'Mrs Tan is 41 years old and her son is 9. How many years ago was her son’s age 1/5 of her age?', a: '1 year ago (the difference, 32, is 4 units; 1 unit = 8: son 8, Mrs Tan 40)' },
      { q: 'Ben and Siti had $140 altogether. Ben spent 1/2 of his money and Siti spent $20. Then they had the same amount left. How much did Ben have at first?', a: '$80 (Ben 2 units, Siti 1 unit + $20; 3 units = $120, 1 unit = $40)' },
      { q: 'Ali had 40 more stickers than Mei. Each of them was given 10 more stickers. Then Mei had 3/5 as many stickers as Ali. How many stickers did Mei have at first?', a: '50 (the difference, 40, is 2 units; Mei 3 units = 60 after, so 50 at first)' },
      { q: 'A tank was 3/4 full of water. After 18 litres were used, it was 1/2 full. How many litres does the tank hold when it is full?', a: '72 litres (1/4 of the tank = 18 litres)' },
      { q: 'Siti gave 1/3 of her stickers to Mei. Then they had the same number of stickers. Mei had 15 stickers at first. How many did Siti have at first?', a: '45 (Siti 3 units; after giving 1 unit she has 2 units, and Mei has 15 + 1 unit = 2 units, so 1 unit = 15)' },
      { q: 'Ravi had $45 and Ben had $15. Their aunt gave each of them the same amount of money. Then Ben had 1/2 as much as Ravi. How much did the aunt give each boy?', a: '$15 (the difference, $30, is 1 unit; Ben $30, Ravi $60)' }
    ],
    challenge: [
      { q: 'Ali, Ben and Mei shared $180. Ali took 1/3 of the money, Ben took 1/4 of what was left and Mei took the rest. How much more did Mei get than Ali?', a: '$30 (Ali $60, Ben $30, Mei $90)' },
      { q: 'Mei had some money. She spent $12, then spent 1/2 of what was left, then spent $8. She had $10 left. How much did she have at first?', a: '$48 (work backwards: 10 + 8 = 18; 18 × 2 = 36; 36 + 12 = 48)' },
      { q: 'A father and his son are 50 years old altogether. In 5 years, the son’s age will be 1/3 of the father’s age. How old is the son now?', a: '10 (in 5 years the total is 60 = 4 units, the son is 15)' },
      { q: 'Ali had 3/5 as many cards as Ben. After Ben gave Ali 20 cards, they had the same number. How many cards did they have altogether?', a: '160 (Ali 3 units, Ben 5 units; same means 4 units each, so Ben gave 1 unit = 20; 8 units = 160)' },
      { q: 'In a basket, 1/3 of the fruits were apples. 10 apples were eaten and 10 pears were put in. Now 1/6 of the fruits are apples. How many fruits are in the basket?', a: '60 (the total did not change; 1/3 − 1/6 = 1/6 of the fruits is 10)' },
      { q: 'Siti spent 2/5 of her money on a dress and 1/3 of the remainder on shoes. The dress cost $30 more than the shoes. How much money did Siti have at first?', a: '$150 (15 units: dress 6 units, remainder 9 units, shoes 3 units; 3 units = $30, 1 unit = $10)' },
      { q: 'Mei had $200 and Siti had $80. Mei spent 3 times as much money as Siti. Then they had the same amount left. How much money did Siti spend?', a: '$60 (Siti spent 1 unit, Mei spent 3 units; the $120 difference is 2 units, so 1 unit = $60; both have $20 left)' },
      { q: 'Ravi had some stickers. He gave 1/2 of them and 4 more to Ali. Then he gave 1/2 of the stickers he had left and 4 more to Ben. He had 4 stickers left. How many stickers did he have at first?', a: '40 (work backwards: (4 + 4) × 2 = 16, (16 + 4) × 2 = 40)' },
      { q: 'Ali and Ben had 140 stamps altogether. Ali gave away 1/3 of his stamps and Ben gave away 1/2 of his. Then they had the same number of stamps left. How many stamps did Ben give away?', a: '40 (Ali 3 units, keeps 2 units; Ben keeps 2 units, so Ben had 4 units; 7 units = 140, 1 unit = 20)' }
    ]
  },

  workbook: H => [
    H.p('Draw a model for every question. First ask: what stays the same?', { after: 40 }),
    H.q(1, 'Ravi had some money. He spent 1/3 of it on a book and 1/4 of the remainder on a pen. He had $36 left.', { before: 40, keepNext: true }),
    H.fig(raviBar()),
    H.sub('a', 'What fraction of his money did he spend on the pen?   ____________'),
    H.sub('b', 'How much money did Ravi have at first?'), H.ans(),
    H.sub('c', 'How much more did the book cost than the pen?'), H.ans(),
    H.q(2, 'Siti and Mei had 84 stickers altogether. Siti gave Mei 12 stickers. Then Siti had 3/4 as many stickers as Mei.', { keepNext: true }),
    H.fig(afterModel()),
    H.sub('a', 'How many stickers did they have altogether after the swap?   ____________'),
    H.sub('b', 'How many stickers did Siti have at first? How many did Mei have at first?'), H.ans('Siti: __________     Mei:'),
    H.q(3, 'Ali has 50 marbles and Ben has 30 marbles. Ali wants to give Ben some of his marbles.', { keepNext: true }),
    H.sub('a', 'Ben says, “Ali must give me 20 marbles so that we have the same number, because he has 20 more than me.” Is Ben right? Explain.'), ...H.lines(1),
    H.sub('b', 'How many marbles must Ali give Ben so that Ali has 3/5 as many marbles as Ben?'), H.ans(),

    H.q(4, 'Ravi had $50 and Ali had $26. Their mother gave each of them the same amount of money. Then Ali had 2/3 as much money as Ravi.', { pb: true, before: 0, keepNext: true }),
    H.sub('a', 'What stays the same: the total or the difference? How much is it?'), H.ans(),
    H.sub('b', 'How much money did their mother give each boy?'), ...H.lines(2), H.ans(),
    H.q(5, 'Mei had $90 and Siti had $60. Each of them spent the same amount of money. Then Siti had 1/4 as much money as Mei.', { keepNext: true }),
    H.sub('a', 'How much money did each girl spend?'), ...H.lines(2), H.ans(),
    H.sub('b', 'How much money did each girl have left?'), H.ans('Mei:  $________     Siti:'),
    H.q(6, 'A box had red beads and blue beads. 3/7 of the beads were red. Then 30 red beads were added. Now 3/5 of the beads are red.', { keepNext: true }),
    H.sub('a', 'Which colour of beads did not change?'), H.ans(),
    H.sub('b', 'How many beads were in the box at first?'), ...H.lines(2), H.ans(),
    H.sub('c', 'How many beads are in the box now?'), H.ans()
  ]
};
