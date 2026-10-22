// Math Inquirers P5 — Lesson 10: Challenge Day (mixed strategies: working backwards, logic, models, listing, supposition)
const { TKQ, TKP, LATER } = require('./take.js');
// Choose a start and explain it: draw a model, list it in order, make a table, work backwards, guess and check / suppose, use a logic grid.
// Every answer below was worked out and checked with a short Python script (exhaustive search for every "find all" and every logic puzzle).
const N = '#1B2A49', Y = '#FFC93C', SKY = '#DDEBF7', TEAL = '#1F7A6F', RED = '#D64545', WH = '#FFFFFF';
const FF = 'Fredoka, Arial, sans-serif';
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const txt = (x, y, s, size = 16, fill = N, anchor = 'middle', weight = 700) =>
  `<text x="${x}" y="${y}" font-size="${size}" font-weight="${weight}" text-anchor="${anchor}" fill="${fill}" font-family="${FF}">${esc(s)}</text>`;

// Q4: a 3 by 4 grid of unit squares (3 rows, 4 columns), drawn to scale: 12 small squares
const gridSvg = () => {
  const s = 56, x0 = 150, y0 = 14; let g = '';
  for (let r = 0; r < 3; r++) for (let c = 0; c < 4; c++)
    g += `<rect x="${x0 + c * s}" y="${y0 + r * s}" width="${s}" height="${s}" fill="${SKY}" stroke="${N}" stroke-width="3"/>`;
  g += txt(x0 + 2 * s, y0 + 3 * s + 30, '3 rows of 4 small squares', 16);
  return `<svg aria-label="A rectangle made of 3 rows of 4 small squares" viewBox="0 0 600 220" width="380" xmlns="http://www.w3.org/2000/svg" style="max-width:100%">${g}</svg>`;
};

module.exports = {
  lesson: {
    n: 10, week: 5, session: 'B', title: 'Challenge Day', topic: 'Mixed Strategies',
    objective: 'Choose a way to start a puzzle (draw a model, list in order, make a table, work backwards, guess and check or suppose, use a logic grid), solve competition-style problems, check every clue, and explain why the chosen start works.',
    skills: 'Choosing a strategy, working backwards with fractions, logic grids, models with units, systematic listing, supposition, checking against every clue, explaining',
    materials: 'Four puzzle cards shown on the slide, or sent as images to each breakout room (backwards, logic, counting, guess and check), mini whiteboards, scrap paper, a 3 by 4 grid drawn on paper, certificates, stamps.',
    online: 'Each breakout pair gets one puzzle card on screen and reports back how they started; logic grids and models are shared on screen and annotated together. Children hold their working up to the camera.',
    warmup: 'Mix-up relay: six cards from the earlier lessons (place value, fractions, area of a triangle, volume, rate, percentage; angles and patterns are in the quick questions). Read a card and ask for a volunteer (a child may say pass once, or choose a green quick card or an orange think-about-it card); that child answers and invites the next volunteer. Then four quick questions on whiteboards.',
    explore: 'Puzzle menu: pairs choose 2 of 4 puzzle cards (backwards number puzzle, pets logic, squares on a grid, two numbers). They write the answer AND how they started: draw, list, table, work backwards or guess and check.',
    mini: 'How to START: draw a model (units and parts), list in order, make a table, work backwards (undo the last step first), guess and check or suppose, logic grid (a tick means crosses in the rest of its row and column). Check every answer against every clue. Before page 2: count shapes of every size systematically, find who is lying by trying each possibility, and keep the difference in ages the same.',
    share: 'Pick one puzzle and teach it in two sentences: how did you START and how do you know your answer is right? Could another start also work?',
    exit: { q: 'Ravi spends 1/2 of his money on a ticket, then $5 on a snack, and has $7 left. How much money did he start with? Say which start you used.', a: '$24. Work backwards: 7 + 5 = 12, and 12 is half of his money, so 12 × 2 = 24. Check: 24 ÷ 2 = 12, 12 − 5 = 7.' },
    mistakes: [
      'Working backwards in the wrong order or using the wrong operation, such as taking away instead of adding back (7 + 5 = 12, then doubling for the half that was spent, 24), or halving instead of doubling.',
      'Stopping when one clue works instead of checking every clue, and in logic puzzles guessing instead of using a clue that tells you something for sure.',
      'Counting only the smallest squares or rectangles (12 in a 3 by 4 grid) and missing the bigger ones made of several small squares; not counting in order by size.'
    ],
    extension: 'Write your own logic puzzle with four people and four things. Test it on a friend: does it have exactly ONE answer? Which clue could you take away without ruining it?',
    key: [
      ['Q1', 'Ali: chicken rice. Ben: laksa. Mei: satay. Siti: roti prata. (Clue 2 says a girl ordered the roti prata, so it is Mei or Siti, and clue 4 rules out Mei: roti prata is Siti\'s. Ali is then chicken rice by clue 1. Ben is not satay, so laksa, and Mei has satay.)'],
      ['Q2', '$63. Work backwards: 15 × 2 = 30 before the gift; 30 + 12 = 42 before lunch; 42 is 2/3 of the money, so 1/3 is 21 and the start is 63. Check: 63 − 21 = 42, 42 − 12 = 30, 30 ÷ 2 = 15 left.'],
      ['Q3', 'Mei $60, Ravi $55. Model: Mei is 4 units; Ravi is 3 units and $10. 7 units + $10 = $115, so 7 units = $105 and 1 unit = $15. Mei 4 × 15 = $60, Ravi 3 × 15 + 10 = $55. Check: 60 + 55 = 115 and 3/4 of 60 = 45, 45 + 10 = 55.'],
      ['Q4', '(a) 12 squares of size 1 by 1  (b) 6 squares of size 2 by 2 and 2 squares of size 3 by 3  (c) 12 + 6 + 2 = 20 squares. (There are none bigger: the grid is only 3 rows tall.)'],
      ['Q5', 'Ben broke the vase. Try each child: if Ali did it, Ali and Ben both lie (2 liars); if Mei did it, Ali and Mei both lie (2 liars); if Ben did it, only Ben lies (1 liar). Only Ben fits.'],
      ['Q6', '(a) In 7 years: Mum will be 48 and Mei 16, and 3 × 16 = 48. (Table: after 1 year 42 and 10; 2 years 43 and 11; … 7 years 48 and 16.) Quick way: Mum is always 32 years older. When she is 3 times as old, the 32 years are 2 times Mei\'s age, so Mei is 16, which is 7 years from now.  (b) Open: for example "I made a table of their ages", "I used the age gap, which never changes" or "I guessed and checked".']
    ]
  },

  script: {
    hook: ['Welcome to Challenge Day! There is no new topic today. There are puzzles from every lesson, and the only question that matters is: how do you START?', 'Clever inquirers do not always know the answer straight away. They have a toolbox of starts, and they check and explain.'],
    warmIntro: ['Mix-up relay: I read a card, a volunteer answers and invites the next volunteer. You may pass once.'],
    predict: ['Look at the four puzzle cards. Which one do you think will be the hardest? Write your guess in the corner of your whiteboard and we will see at the end.'],
    exploreHints: ['Stuck: "How could you start? Draw it, list it, make a table, work backwards, or guess and check?"', 'Backwards puzzle: "Write the steps going forwards first. Then undo the LAST step first."', 'Logic puzzle: "Find a clue that tells you something for sure. Put a cross where it cannot be."', 'If a pair wants more: make a puzzle card for the next pair.'],
    think: [
      '“A number is doubled, then 7 is added, then divided by 3, and the answer is 5. I work backwards and undo the last step first: 5 × 3 = 15, then 15 − 7 = 8, then 8 ÷ 2 = 4. I check forwards: 4 × 2 = 8, 8 + 7 = 15, 15 ÷ 3 = 5.”',
      '“A logic grid. Ravi does not play swimming. Siti plays neither football nor badminton, so Siti swims for sure. A tick means crosses in the rest of that row AND that column. Ben does not play football, so Ben badminton and Ravi football. I check every clue.”',
      '“How many squares are in a 2 by 3 grid? If I count only the small ones I get 6, but there are bigger squares. I count by size: 1 by 1: 6. 2 by 2: 2. Total 8. Counting by size means I do not miss any.”'
    ],
    circulate: ['Ask: "How did you start? Is there another start that would work?"', 'Ask: "Did you check your answer against EVERY clue?"', 'Ask: "What would you try first if the numbers were much bigger?"'],
    hints: ['Hint 1: “Draw a bar or a table. Put what you know in it.”', 'Hint 2: “Which clue tells you something for sure? Start there.”', 'Hint 3: “Undo the last step first. Fractions: if half was spent, half is left.”'],
    talk: ['“Pick one puzzle and tell your partner in two sentences. You can say: I started by ____. I know it is right because ____. You may pass.”', '“Which start do you think was the most useful today? When would you NOT use it?”'],
    talkAns: 'Open. Praise reasons, not just answers. Good answers say what the start does: a model shows how the parts relate, working backwards undoes steps in reverse, a logic grid keeps clues tidy, listing by size makes sure nothing is missed. Different starts can both work.',
    close: ['“Today you used a toolbox of starts and checked every clue. That is how problem solvers work, and it is the end of our Math Inquirers program.”', '“Do the exit ticket on your own, then show me. Then it is certificate time!”']
  },

  deck: {
    today: 'Choose a start for a puzzle: draw a model, work backwards, use a logic grid, list in order or guess and check. Then check every clue.',
    warmGame: 'Mix-up relay. Six cards from earlier lessons (a quick question each). Read a card; a volunteer answers and invites the next volunteer. You may say pass once.',
    warmQs: [['What is 3/4 of 48?', '36'], ['A tap fills 6 litres in 2 minutes. How long to fill 45 litres?', '15 minutes'], ['Two angles on a straight line are 65° and ___', '115°'], ['Next in the pattern: 5, 8, 11, 14, __', '17']],
    expSetup: ['Your pair gets ONE of the 4 puzzle cards. Work in pairs.', 'Write your answer, and write HOW you started (draw, list, table, work backwards, guess and check).', 'Check your answer against every clue.', 'Be ready to teach your card to the group in two sentences.'],
    expPic: 'four puzzle cards laid out on a desk: a number machine, a 3 by 3 logic grid, a grid of squares and two number boxes.',
    expAsk: [['Card A: a number is doubled, 7 is added, the answer is divided by 3, giving 5. What was the number?', '4 (work backwards: 5 × 3 = 15, 15 − 7 = 8, 8 ÷ 2 = 4).'], ['Card B: Ali, Ben and Mei have a cat, a dog and a fish. Ali has no dog. Ben has no cat and no dog. Who has what?', 'Ben has the fish, Ali the cat, Mei the dog.'], ['Card D: two numbers add to 20 and differ by 6. What are they?', '13 and 7 (guess and check, or take away the 6 and share: 14 ÷ 2 = 7, then 7 + 6 = 13).']],
    mini1: { head: 'Working backwards: spent 1/4, then $10, then half of the rest. $13 left.', body: ['Draw it: start, then each step. Work back from the end.', '$13 left is half of the rest, so the rest was $26. Before lunch: 26 + 10 = 36.', '$36 is 3/4 of the money, so 1/4 is $12 and all of it is $48.'], ans: '$48. Check: 48 − 12 = 36, 36 − 10 = 26, 26 ÷ 2 = 13 ✓' },
    mini2: { head: 'Logic grid: Ravi, Siti and Ben play badminton, swimming and football. Ravi does not swim. Siti does not play football or badminton. Ben does not play football.', body: ['Siti: not football, not badminton, so swimming for sure.', 'A tick means crosses in the rest of its row and column.', 'Ben is not football, so badminton; Ravi is football.'], ans: 'Ravi football, Siti swimming, Ben badminton. Check all three clues.' },
    keyHead: 'Key idea: choose a start, check every clue',
    keyBig: 'Draw it, list it, make a table, work backwards, guess and check or suppose, use a logic grid. Then explain why your start works.',
    keySmall: 'Check your answer against EVERY clue, not just one.',
    brk: 'Puzzle stretch: stand up and show a 3 by 3 grid with your fingers. How many squares can you find on it? Count by size and tell your neighbour.',
    ws1: 'Page 1, in pairs: Q1 a food logic grid, Q2 a money puzzle (work backwards). Q3, two amounts with a model, is printed on page 1 but done in the page 2 time.',
    ws2: 'Page 2, on your own: Q3 two amounts with a model (from page 1), Q4 (a) how many squares (Q4 (b) (c), Q5 who broke the vase and Q6 ages are take-home). Say which start you used.'
  },

  qbank: {
    core: [
      { q: 'A number is multiplied by 4, then 6 is taken away, and the answer is 50. What was the number?', a: '14 (work backwards: 50 + 6 = 56, 56 ÷ 4 = 14).' },
      { q: 'Ali has 1/2 of his money left after buying a book for $9. How much did he have at first?', a: '$18 ($9 is the other half).' },
      { q: 'Two numbers add up to 40 and the bigger is 8 more than the smaller. What are the two numbers?', a: '24 and 16 (take away the 8: 32, share: 16 and 16, then add 8 back to one: 24 and 16).' },
      { q: 'Ravi, Siti and Ben each have a different pet: a rabbit, a hamster and a bird. Ravi has no bird and no hamster. Siti has no hamster. Who has the bird?', a: 'Siti. Ravi has the rabbit (no bird, no hamster). Siti is not the hamster, so she has the bird, and Ben has the hamster.' },
      { q: 'How many squares of all sizes are in a 2 by 2 grid of small squares?', a: '5 (4 small and 1 big).' },
      { q: 'Pens cost $2 and pads cost $3. Ben buys 10 items and pays $24. How many pads?', a: '4 pads and 6 pens (all pens would be $20; each pad instead of a pen adds $1).' }
    ],
    stretch: [
      { q: 'Siti spent 2/5 of her money, then 1/3 of what was left. She had $24 left at the end. How much did she start with?', a: '$60. Work backwards: $24 is 2/3 of what was left, so that was $36; $36 is 3/5 of her money, so 1/5 is $12 and she started with $60. Check: 60 − 24 = 36, 36 − 12 = 24.' },
      { q: 'How many 3-digit numbers have digits that add up to 5? List them all in order.', a: '15 numbers: 104, 113, 122, 131, 140, 203, 212, 221, 230, 302, 311, 320, 401, 410, 500.' },
      { q: 'The sum of two consecutive numbers (numbers that are next to each other, like 40 and 41) is 145. What are the two numbers?', a: '72 and 73 (145 is 1 more than twice 72).' },
      { q: 'A snail climbs 3 m up a 10 m wall each day, and slips down 2 m each night. On which day does it reach the top?', a: 'Day 8. After 7 days and nights it is at 7 m. On day 8 it climbs 3 m to reach 10 m before it can slip.' },
      { q: 'Ben has 14 coins, all 50¢ and 20¢ coins, worth $4.90. How many of each?', a: '7 fifty-cent coins and 7 twenty-cent coins (all 20¢ would be $2.80; $2.10 short; each swap adds 30¢; 210 ÷ 30 = 7).' },
      { q: 'What is the smallest whole number bigger than 1 that leaves a remainder of 1 when divided by 2, by 3, by 4, by 5 and by 6?', a: '61 (it is 1 more than a multiple of 2, 3, 4, 5 and 6; the smallest such multiple is 60).' },
      { q: 'I think of a number, multiply it by 4, take away 10, halve it and add 3. The answer is 22. What is my number?', a: '12. Work backwards: 22 − 3 = 19, 19 × 2 = 38, 38 + 10 = 48, 48 ÷ 4 = 12.' },
      { q: '1/2 of a number is 5 more than 1/3 of the same number. What is the number?', a: '30. The difference between a half and a third is 1/6, and 1/6 of the number is 5. Check: 15 and 10.' }
    ],
    challenge: [
      { q: 'At the first bus stop, 1/3 of the passengers got off. At the second stop, half of those left got off and 3 got on. There are now 12 passengers. How many were on the bus at first?', a: '27. Work backwards: 12 − 3 = 9; 9 is half of what was left, so 18 were left after stop 1; 18 is 2/3 of the passengers, so 1/3 is 9 and there were 27 at first.' },
      { q: 'How many rectangles of all sizes are there in a 1 by 5 strip of 5 small squares?', a: '15 (5 of length 1, 4 of length 2, 3 of length 3, 2 of length 4 and 1 of length 5: 5 + 4 + 3 + 2 + 1).' },
      { q: 'In the 3 by 4 grid of Question 4 there are 20 squares. How many rectangles of ALL sizes are there (a square counts as a rectangle)? Count by size. Then explain how you know you have not missed any or counted any twice.', a: '60 rectangles. Count by size, width by height (the grid is 4 wide and 3 tall): 1 by 1: 12, 2 by 1: 9, 3 by 1: 6, 4 by 1: 3 (30 with height 1); 1 by 2: 8, 2 by 2: 6, 3 by 2: 4, 4 by 2: 2 (20 with height 2); 1 by 3: 4, 2 by 3: 3, 3 by 3: 2, 4 by 3: 1 (10 with height 3). 30 + 20 + 10 = 60. Check: a rectangle is chosen by 2 of the 5 vertical lines (10 ways) and 2 of the 4 horizontal lines (6 ways): 10 × 6 = 60.' },
      { q: 'How many times does the digit 4 appear when you write all the whole numbers from 1 to 50?', a: '15 (in the ones place: 4, 14, 24, 34 and 44 is 5 times; in the tens place: 40 to 49 is 10 times; 5 + 10 = 15).' },
      { q: 'Make up your own logic puzzle with four people and four things (pets, dishes, sports …). Write at least four clues. Test it on a partner: does it have exactly ONE answer? Which clue could you take away without spoiling it, and which clue could you NOT take away?', a: 'Open-ended. Check by trying to find a second solution: if one exists, add a clue. A good test is to remove each clue in turn and count the solutions. Sample: the hawker-centre puzzle in Question 2 has exactly one solution (checked by trying all 24 arrangements); without clue 4 (Mei did not order roti prata) it has more than one.' },
      { q: 'A monkey eats half of the rambutans in a pile and 1 more, every day for 3 days. After the third day there are none left. How many were in the pile at the start?', a: '14. Work backwards: after day 3 there are 0; before day 3 there were 2 (half of 2 is 1, and 1 more is 2); before day 2: (2 + 1) × 2 = 6; before day 1: (6 + 1) × 2 = 14. Check: 14 → 6 → 2 → 0.' },
      { q: 'A water tank is 1/3 full. After 20 litres are added it is 1/2 full. Then 1/4 of the water in the tank is let out. How many litres of water are in the tank now? What fraction of the tank is full?', a: '45 litres, which is 3/8 of the tank. The 20 litres are 1/2 − 1/3 = 1/6 of the tank, so the full tank holds 120 litres. Half full is 60 litres; letting out 1/4 of it (15 litres) leaves 45 litres, and 45 ÷ 120 = 3/8.' },
      { q: '25 coins of 50¢, 10¢ and 20¢ are worth $5.30 altogether. There are twice as many 10¢ coins as 50¢ coins. How many coins of each kind are there?', a: '3 fifty-cent coins, 6 ten-cent coins and 16 twenty-cent coins. Suppose all 25 coins were 20¢: that is $5.00. Every 50¢ coin comes with two 10¢ coins; this group of 3 coins is worth 70¢, and replacing three 20¢ coins (60¢) with it adds 10¢. The extra is 30¢, so there are 3 groups. Check: 150¢ + 60¢ + 320¢ = 530¢ and 3 + 6 + 16 = 25.' },
      { q: 'Ali, Ben, Mei and Siti sit in a row of 4 chairs. Mei is not on either end. Ben does not sit next to Mei. Siti sits somewhere to the left of Ali. Ben is not on the left end. In what order do they sit, from left to right?', a: 'Siti, Mei, Ali, Ben. Mei is in chair 2 or 3. If Mei is in chair 3, the only chair not next to her is chair 1, but Ben is not on the left end, so that fails. So Mei is in chair 2, the only chair not next to her is chair 4, so Ben is in chair 4. Siti and Ali are in chairs 1 and 3 and Siti is on the left: Siti 1, Ali 3.' }
    ]
  },

  workbook: H => {
    const W = [];
    W.push(H.p('Choose a start: draw a model, list in order, make a table, work backwards or guess and check. Check your answer against EVERY clue.', { after: 40 }));
    // Q1 logic (was Q2)
    W.push(H.q(1, 'Logic grid. Ali, Ben, Mei and Siti each ordered a different dish at a hawker centre. Use the clues to find who ordered what. Put a tick for yes and a cross for no.', { keepNext: true }));
    ['Clue 1:  Ali did not order laksa or satay.', 'Clue 2:  The roti prata was ordered by a girl (Mei and Siti are girls; Ali and Ben are boys).', 'Clue 3:  Ben did not order satay.     Clue 4:  Mei did not order roti prata.'].forEach(c => W.push(H.p(c, { indent: { left: 400 }, after: 10 })));
    { const ws = [1900, 2000, 2000, 2000, 2000];
      W.push(H.tbl(ws, [H.row(['', 'Chicken rice', 'Laksa', 'Satay', 'Roti prata'].map((s, i) => H.cell(s, ws[i], { bold: true, fill: 'EDEDED', h: 40 }))),
        ...['Ali', 'Ben', 'Mei', 'Siti'].map(n => H.row([H.cell(n, ws[0], { bold: true, h: 34 }), ...ws.slice(1).map(w => H.cell('', w, { h: 34 }))]))])); }
    W.push(H.p('Ali: __________   Ben: __________   Mei: __________   Siti: __________', { before: 20, after: 10 }));
    // Q2 backwards (was Q1)
    W.push(H.q(2, 'Working backwards. Ali spent 1/3 of his money on a book. He then spent $12 on lunch. He spent half of what was left on a gift. Ali had $15 left at the end. How much money did he start with?', { before: 20, keepNext: true }));
    W.push(H.p(['<b style="color:#1F7A6F">Start here:</b> write the steps in order. Then undo the LAST step first.'], { after: 20 }));
    W.push(...H.lines(1));
    W.push(H.ans('Answer:  $'));
    // Q3 model
    W.push(H.q(3, [LATER, 'Draw a model. Mei and Ravi have $115 altogether. Ravi has $10 more than 3/4 of Mei’s money. How much money does each have? Check your answer against BOTH clues.'], { keepNext: true }));
    W.push(H.p(['<b style="color:#1F7A6F">Start here:</b> Mei is 4 equal units. How many units is 3/4 of Mei’s? Where does the $10 go?'], { after: 20 }));
    W.push(...H.lines(2));
    W.push(H.ans('Mei:  $____________    Ravi:  $____________', 0));

    // ---- page 2 ----
    W.push(H.q(4, 'How many squares of ALL sizes can you find in this 3 by 4 grid? Count by size so you do not miss any.', { pb: true, before: 0, keepNext: true }));
    W.push(H.fig(gridSvg()));
    W.push(H.sub('a', 'Squares of size 1 by 1:   ____________'));
    W.push(H.sub('b', [TKP, 'Squares of size 2 by 2:   ____________    Squares of size 3 by 3:   ____________']));
    W.push(H.sub('c', [TKP, 'How many squares altogether? How do you know there are none bigger?'], { after: 20 }));
    W.push(...H.lines(1));
    // Q5 truth
    W.push(H.q(5, [TKQ, 'Ali, Ben and Mei were playing. One of them broke a vase. Ali says, “Ben broke it.” Ben says, “Mei broke it.” Mei says, “I did not break it.” Exactly ONE of the three children is lying. Who broke the vase? Try each child and count the liars.'], { keepNext: true }));
    { const ws = [2600, 2400, 2400, 2500];
      W.push(H.tbl(ws, [H.row(['If the vase was broken by …', 'Is Ali lying?', 'Is Ben lying?', 'Is Mei lying?'].map((s, i) => H.cell(s, ws[i], { bold: true, fill: 'D9D9D9', h: 40 }))),
        ...['Ali', 'Ben', 'Mei'].map(n => H.row([H.cell(n, ws[0], { bold: true, h: 40 }), ...ws.slice(1).map(w => H.cell('', w, { h: 40 }))]))])); }
    W.push(H.p('Answer:  ______________________ broke the vase.', { before: 30, after: 10 }));
    // Q6 ages
    W.push(H.q(6, [TKQ, 'Mum is 41 years old and Mei is 9 years old.'], { keepNext: true }));
    W.push(H.sub('a', 'In how many years will Mum be exactly 3 times as old as Mei? Show your table or working.', { after: 20 }));
    W.push(...H.lines(2));
    W.push(H.sub('b', 'Which start did you use? Why did you choose it?', { after: 20 }));
    W.push(...H.lines(1));
    return W;
  }
};
