// Math Inquirers P3, Lesson 10: Challenge Day (mixed, incl. bar graphs and logic)
const NAVY = '#1B2A49', YEL = '#FFC93C', SKY = '#DDEBF7', TEAL = '#1F7A6F', RED = '#D64545', WHITE = '#FFFFFF';
const txt = (x, y, s, o = {}) => `<text x="${x}" y="${y}" font-size="${o.size || 16}" font-weight="${o.weight || 700}" text-anchor="${o.anchor || 'middle'}" fill="${o.fill || NAVY}" font-family="Arial, sans-serif"${o.extra || ''}>${s}</text>`;

// Bar graph drawn to scale: 4 px per cup, gridlines every 10 cups, Lime juice bar left for the child to draw.
const drinksGraph = () => {
  const data = [['Milo', 45], ['Teh', 30], ['Kopi', 55], ['Bandung', 20], ['Lime juice', null]];
  const x0 = 80, y0 = 290, k = 4, slot = 100, bw = 58;
  let s = '';
  for (let v = 0; v <= 60; v += 10) {
    const y = y0 - v * k;
    s += `<line x1="${x0}" y1="${y}" x2="${x0 + 5 * slot + 10}" y2="${y}" stroke="${v ? '#C9D4EC' : NAVY}" stroke-width="${v ? 1.5 : 3}"/>`;
    s += txt(x0 - 10, y + 5, String(v), { anchor: 'end', size: 15 });
  }
  s += `<line x1="${x0}" y1="${y0}" x2="${x0}" y2="${y0 - 62 * k}" stroke="${NAVY}" stroke-width="3"/>`;
  data.forEach(([n, v], i) => {
    const x = x0 + 21 + i * slot;
    if (v !== null) s += `<rect x="${x}" y="${y0 - v * k}" width="${bw}" height="${v * k}" fill="${[YEL, SKY, TEAL, RED][i]}" stroke="${NAVY}" stroke-width="2.5"/>`;
    s += txt(x + bw / 2, y0 + 22, n, { size: 15 });
  });
  s += txt(22, y0 - 120, 'Number of cups', { size: 15, extra: ` transform="rotate(-90 22 ${y0 - 120})"` });
  s += txt(x0 + 255, y0 + 46, 'Drink', { size: 15 });
  return `<svg aria-label="Bar graph of cups of drinks sold: Milo 45, Teh 30, Kopi 55, Bandung 20, Lime juice bar missing" viewBox="0 0 600 345" xmlns="http://www.w3.org/2000/svg" style="width:400px;max-width:100%">${s}</svg>`;
};
// Matchstick squares: 1, 2 and 3 squares in a row
const sticks = () => {
  const u = 52; let s = '';
  const stick = (x1, y1, x2, y2) => `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${NAVY}" stroke-width="7" stroke-linecap="round"/><circle cx="${x2}" cy="${y2}" r="0"/>`;
  let ox = 20;
  [1, 2, 3].forEach((n, j) => {
    for (let i = 0; i < n; i++) { const x = ox + i * u; s += stick(x, 20, x + u, 20) + stick(x, 20 + u, x + u, 20 + u); }
    for (let i = 0; i <= n; i++) { const x = ox + i * u; s += stick(x, 20, x, 20 + u); }
    s += txt(ox + n * u / 2, 20 + u + 32, `${n} square${n > 1 ? 's' : ''}: ${[4, 7, 10][j]} sticks`, { size: 15 });
    ox += n * u + 70;
  });
  return `<svg aria-label="Matchstick squares: 1 square uses 4 sticks, 2 squares use 7 sticks, 3 squares use 10 sticks" viewBox="0 0 600 115" xmlns="http://www.w3.org/2000/svg" style="width:340px;max-width:100%">${s}</svg>`;
};
const digitCards = () => {
  let s = '';
  ['2', '5', '8'].forEach((d, i) => { s += `<rect x="${10 + i * 70}" y="6" width="56" height="64" rx="8" fill="${YEL}" stroke="${NAVY}" stroke-width="3"/>` + txt(38 + i * 70, 50, d, { size: 30 }); });
  return `<svg aria-label="Digit cards 2, 5 and 8" viewBox="0 0 600 76" xmlns="http://www.w3.org/2000/svg" style="width:380px;max-width:100%">${s}</svg>`;
};

module.exports = {
  lesson: {
    n: 10, week: 5, session: 'B', title: 'Challenge Day', topic: 'Mixed puzzles: bar graphs and logic',
    objective: 'Choose a way to start a puzzle (draw it, list it, make a table), solve a logic grid with ticks and crosses, read and complete a bar graph with a scale, and explain the thinking.',
    skills: 'Choosing a strategy, logical reasoning, reading scales, listing systematically, perseverance, explaining',
    materials: 'Puzzle cards for 2 stations (list, measure), digit cards 0 to 9 (or paper cards), squared paper, mini whiteboards, certificates, stamps.',
    online: 'Two stations, 7 minutes each. Pairs stay in one breakout room, and the tutor shares the next station card when the timer ends. No physical materials beyond paper. Logic grids and graphs are shared on screen and annotated together.',
    warmup: 'Relay chain: one quick question from our P3 lessons, the answer is passed on to the next child as the start of the next question (6 × 9, add 46, × 7, take away 250, ÷ 5, then change 90 minutes to hours and minutes). Then 5 quick questions.',
    explore: 'Two stations, about 7 minutes each, in pairs: List (make every 3-digit number from 3 digit cards) and Measure (a 120 cm ribbon is cut into 3 pieces, each 10 cm longer than the one before: draw it and find each piece). The tutor shares each station card on screen. Write the answer and how you started.',
    mini: 'How to start a puzzle: draw it (a queue: 4th from the front and 6th from the back means 4 + 6 − 1 = 9 people), make a table (a logic grid: a tick in a box means crosses in the rest of its row and column), read the scale of a bar graph (what does one space stand for? halfway between two lines). Then list it in order before page 2.',
    share: 'Pick one puzzle and teach it to the group: how did you START it, and how do you know your answer is right?',
    exit: { q: 'Ali is 4th from the front and 4th from the back of a queue. How many people are in the queue? Which start did you use?', a: '7 people (3 in front, Ali, 3 behind: 4 + 4 − 1 = 7). Draw it.' },
    mistakes: [
      'Queues: adding the two positions and counting the person twice (3rd from front and 5th from back is 7, not 8).',
      'Bar graphs: reading every space as 1 instead of checking the scale, or not reading the halfway values (45, 55).',
      'Logic grids: putting a tick but forgetting to cross out the rest of that row and column; or guessing instead of using a clue.'
    ],
    extension: 'Write your own logic grid puzzle with 3 people and 3 things. Test it on a friend: does it have exactly one answer? Which clue could you take away?',
    key: [
      ['Q1', '(a) Kopi  (b) 25 cups (55 − 30)  (c) 50 cups (200 − 45 − 30 − 55 − 20); the bar reaches the 50 line  (d) Milo and Kopi (45 + 55 = 100)'],
      ['Q2', 'Ali: football. Mei: chess. Ravi: swimming. Siti: choir. (Clue 2: Mei and Ravi are not in the choir; with clue 1, Siti is. Clue 3: the swimmer is Ravi or Siti, so Ravi. Ali is not chess, so football; Mei chess.)'],
      ['Q3', '(a) 7 people (3 + 5 − 1)  (b) 6 people (Ali 2nd, 3 between, Siti 6th and last)'],
      ['Q4', '(a) 258, 285, 528, 582, 825, 852  (b) 2 odd numbers: 285 and 825  (c) 582 (18 away from 600)'],
      ['Q5', 'Table: 13, 16, 19 sticks (add 3 each time)  (a) 25 sticks  (b) 10 squares'],
      ['Q6', '411, 321, 213 (3 numbers: the ones digit is 1, 3 or 5; list each case)']
    ]
  },
  script: {
    hook: ['Welcome to Challenge Day! Today there is no new topic: there are puzzles from every lesson. Clever inquirers do not always know the answer straight away. They know how to START: draw it, list it, or make a table.'],
    warmIntro: ['Relay chain: I ask the first question. The answer is the start of the next question, so listen carefully and pass it on. If someone is stuck, the group can help with a hint, not the answer.'],
    predict: ['Look at the two stations. Which one do you think will be harder? Write your guess, and we will see at the end.'],
    exploreHints: ['Stuck: “How could you start? Draw it, list it, or make a table?”', 'List station: “Start with the smallest digit in the hundreds place. How many numbers does each digit give?”', 'Measure station: “Draw the three pieces. What if all three were the same? What is extra?”', 'Ready for more: make a puzzle card for the next pair.'],
    think: [
      '“Siti is 4th from the front and 6th from the back. I draw the queue: 3 people in front of Siti, Siti, then 5 people behind her. 3 + 1 + 5 = 9. If I add 4 + 6 I count Siti twice, so I take 1 away: 10 − 1 = 9.”',
      '“A logic grid: Ben does not like curry puff or popiah, so I put two crosses in Ben’s row. Only kaya toast is left, so a tick. A tick means crosses in the rest of that column, so nobody else has kaya toast.”',
      '“A bar graph: first I read the scale. The lines go 0, 2, 4, 6, so each space is 2. A bar halfway between 6 and 8 shows 7.”'
    ],
    circulate: ['Ask: “How did you start? Why did you choose that?”', 'Ask: “Which clue did you use first? Why that one?”', 'Ask: “How do you know you have found ALL of them?”'],
    hints: ['Hint 1: “Draw it: put people or bars on paper.”', 'Hint 2: “Make a table and cross out what cannot be.”', 'Hint 3: “List it in order, smallest first, so you do not miss one.”'],
    talk: ['“Which start helped you most today: draw it, list it or make a table? Why?”', '“Why do we take away 1 in a queue puzzle?”'],
    talkAns: 'Open answers for the first. Queue: the person is counted from the front AND from the back, so they are counted twice; take away 1.',
    close: ['“You are real inquirers now: you notice, test, and explain why. Here is your certificate.”', 'Give each child a certificate and tell them one specific thing they did well in the program.']
  },
  deck: {
    today: 'Choose how to start a puzzle: draw it, list it or make a table. Solve a logic grid and read a bar graph with a scale.',
    warmGame: 'Relay chain. Each answer is passed on and becomes the start of the next question.',
    warmQs: [['What is the value of the digit 7 in 4732?', '700'], ['3/8 + 2/8 = ?', '5/8'], ['47 ÷ 5 = ?', '9 remainder 2'], ['A rectangle is 6 cm by 4 cm. What is its perimeter?', '20 cm'], ['2 kg 50 g = __ g', '2050 g']],
    expSetup: ['Two stations, 7 minutes each: List, then Measure.', 'Work in pairs. Read the puzzle card aloud.', 'Before you solve it, decide: draw it, list it or make a table?', 'Write the answer and how you started.'],
    expPic: 'two station cards: three digit cards, and a 120 cm ribbon to be cut into 3 pieces.',
    expAsk: [['How did you start each puzzle?', 'Open: draw it, list it, make a table.'], ['How many numbers did the List station make? How do you know you have them all?', '6 numbers: 2 for each hundreds digit, listed in order.'], ['Measure station: how long is each piece of ribbon?', '30 cm, 40 cm and 50 cm (take away the extra 10 + 20 = 30 cm, 90 cm ÷ 3 = 30 cm).']],
    mini1: { head: 'Draw it: a queue', body: ['Siti is 4th from the front and 6th from the back of a queue.', 'How many people are in the queue?'], ans: '9 people: 3 in front, Siti, 5 behind (4 + 6 − 1 = 9).' },
    mini2: { head: 'Make a table: a logic grid', body: ['Ben, Siti and Ravi each like a different snack: curry puff, kaya toast, popiah.', 'Ben does not like curry puff or popiah. Ravi does not like curry puff. Who likes what?'], ans: 'Ben: kaya toast. Ravi: popiah. Siti: curry puff.' },
    keyHead: 'Key idea: how to start a puzzle',
    keyBig: 'Stuck? Draw it, list it in order, or make a table. Then check every clue.',
    keySmall: 'Logic grid: a tick means crosses in the rest of its row and column. Bar graph: read the scale first.',
    brk: 'Freeze dance with maths. When the music stops, the tutor shows a 24-hour time; make the clock hands with your arms.',
    ws1: 'Page 1, in pairs: Q1 the drinks bar graph, Q2 the CCA logic grid.',
    ws2: 'Page 2, on your own: Q3 queues, Q4 digit cards, Q5 matchstick squares, then Q6 a number riddle if you have time.'
  },
  qbank: {
    core: [
      { q: 'Mei is 5th from the front and 4th from the back of a queue. Draw circles for the children in the queue. How many children are in the queue?', a: '8 (5 + 4 − 1: Mei is counted in both)' },
      { q: 'Two numbers add up to 50. One number is 12 more than the other. Guess a pair, check it, and improve your guess. What are the two numbers?', a: '19 and 31 (19 + 31 = 50 and 31 − 19 = 12; or 50 − 12 = 38 and 38 ÷ 2 = 19)' },
      { q: 'Make all the 3-digit numbers you can with the digit cards 1, 4 and 7 (use each card once). Which of them are even?', a: '147, 174, 417, 471, 714, 741. Even: 174 and 714.' },
      { q: 'A bar graph has lines at 0, 10, 20, 30, 40 and 50. A bar stops halfway between 30 and 40. What number does it show?', a: '35' },
      { q: '5, 9, 13, 17, … What is the 10th number in this pattern?', a: '41 (add 4 each time: 5, 9, 13, 17, 21, 25, 29, 33, 37, 41)' },
      { q: 'Ali has $5. He buys 2 drinks at $1.35 each. How much money does he have left?', a: '$2.30 ($1.35 + $1.35 = $2.70; $5 − $2.70 = $2.30)' }
    ],
    stretch: [
      { q: 'Ali has three coins: 10¢, 20¢ and 50¢. He picks one coin, or two coins, or all three. List every different amount of money he can make, in order. How many amounts are there?', a: '7 amounts: 10¢, 20¢, 30¢ (10 + 20), 50¢, 60¢ (10 + 50), 70¢ (20 + 50), 80¢ (all three). Listing by the number of coins (one, two, three) makes sure none is missed.' },
      { q: 'Ali, Ben and Siti each have a different pet: a cat, a dog and a fish. Ali’s pet has no fur. Ben does not have the dog. Who has which pet?', a: 'Ali: fish. Ben: cat. Siti: dog.' },
      { q: 'Triangles are made in a row with sticks: 1 triangle uses 3 sticks, 2 triangles use 5 sticks, 3 triangles use 7 sticks. How many sticks are needed for 12 triangles?', a: '25 sticks (add 2 each time: 3 + 11 × 2 = 25)' },
      { q: 'Use the digits 3, 0, 6 and 9 once each. Make the largest even 4-digit number and the smallest odd 4-digit number.', a: 'Largest even: 9630. Smallest odd: 3069.' },
      { q: 'A bar graph shows stamps: Ali 35 and Ben 20. Mei has 15 more than Ben. Siti has as many as Ali and Ben together. How many stamps do the four children have altogether?', a: '145 (Mei 35, Siti 55; 35 + 20 + 35 + 55 = 145)' },
      { q: 'Ali, Ben and Siti stand in a line. Ali is not first. Ben is just behind Siti. Who is first?', a: 'Siti (the order is Siti, Ben, Ali)' },
      { q: 'A snail climbs a wall 12 m high. Each day it climbs up 5 m, and each night it slides down 2 m. On which day does it reach the top?', a: 'Day 4 (highest point each day: 5, 8, 11, 14 m; it passes 12 m on day 4)' },
      { q: 'Two numbers add up to 100. Their difference is 24. What are the numbers?', a: '62 and 38' }
    ],
    challenge: [
      { q: 'Ben is 3rd from the front and 5th from the back of a queue, so there are 7 children. Add the two numbers: what do you get? Does this always work? Mei is 6th from the front in a queue of 15. Where is she from the back? Write a rule that links "from the front", "from the back" and "how many in the queue".', a: '3 + 5 = 8, which is 1 more than 7. It always works: the child in question is counted in both numbers, so (from the front) + (from the back) = (children in the queue) + 1. Mei is 15 + 1 − 6 = 10th from the back.' },
      { q: 'How many squares of any size are there in a 3 by 3 grid of squares?', a: '14 (9 small, 4 of size 2 by 2, 1 of size 3 by 3)' },
      { q: '6 children meet. Each child shakes hands once with every other child. How many handshakes are there?', a: '15 (5 + 4 + 3 + 2 + 1)' },
      { q: 'One of Ali, Ben and Mei ate the last kueh. Ali says, “Ben ate it.” Ben says, “I did not eat it.” Mei says, “I did not eat it.” Only ONE of them is telling the truth. Who ate the kueh?', a: 'Mei. Test each child: if Ali ate it, Ben and Mei are both telling the truth (2 truthful, not 1). If Ben ate it, Ali and Mei are both truthful (2). If Mei ate it, only Ben is truthful (1). So it was Mei.' },
      { q: 'Ali, Ben, Mei and Siti read 8, 11, 13 and 15 books (each child a different number). Mei read the most. Siti read more than Ben. Ali read 2 fewer books than Siti. How many books did each child read? Then draw the bar graph.', a: 'Mei 15, Siti 13, Ali 11, Ben 8 (the only way). Mei has the most, 15. Ali is 2 fewer than Siti, and the only two numbers that are 2 apart among the rest (8, 11, 13) are 11 and 13, so Siti 13 and Ali 11. Ben is left with 8, and Siti (13) read more than Ben (8).' },
      { q: 'Squares are built from sticks. Figure 1 is 1 square (4 sticks). Figure 2 is a 2 by 2 block of 4 squares (12 sticks). Figure 3 is a 3 by 3 block of 9 squares (24 sticks). How many sticks does Figure 4 need? Make a table and look at the jumps. How many sticks does Figure 10 need?', a: 'Figure 4: 40 sticks. The table goes 4, 12, 24, 40, 60, 84, 112, 144, 180, 220. The jumps are 8, 12, 16, 20, 24, 28, 32, 36, 40: they go up by 4 each time. Figure 10 needs 220 sticks. (Rule: 2 × n × (n + 1).)' },
      { q: 'Make up your own logic puzzle with 3 people and 3 things (colours, pets or sports). Write 3 or 4 clues. Test it on a partner: does it have exactly ONE answer? Is there a clue you could take away and still have only one answer?', a: 'Answers vary. Check that the clues fit one arrangement only (try every arrangement of the 3 things). Example: Sam, Lee and Mei wear red, blue and green. Clues: Sam is not wearing red. Lee is not wearing blue. Mei is not wearing green. Sam is not wearing blue. The only answer is Sam green, Lee red, Mei blue. The clue "Mei is not wearing green" could be taken away and there is still only one answer.' },
      { q: 'In a queue, Siti is 6th from the front and Ravi is 4th from the back. There are 3 children between them, and Siti is in front of Ravi. How many children are in the queue?', a: '13 (Siti 6th, Ravi 6 + 3 + 1 = 10th from the front, then 3 more behind Ravi)' },
      { q: 'A bar graph shows the paper collected by 4 classes. 3P1 collected 10 kg more than 3P2. 3P3 collected the same as 3P1. 3P4 collected 5 kg less than 3P2. Altogether they collected 135 kg. How much did each class collect?', a: '3P1 40 kg, 3P2 30 kg, 3P3 40 kg, 3P4 25 kg (take away the extras 10 + 10 − 5 = 15: 120 kg ÷ 4 = 30 kg for 3P2)' }
    ]
  },
  workbook: H => {
    const { q, sub, ans, lines, p, tbl, row, cell, fig, t } = H;
    const W = [];
    // ---------- page 1 ----------
    W.push(q(1, 'A drinks stall sold 200 cups of drinks on Monday. The bar graph shows the cups sold, but the bar for Lime juice is missing.', { before: 60, keepNext: true }));
    W.push(fig(drinksGraph()));
    W.push(sub('a', 'Which drink shown sold the most? ________     (b)  How many more cups of Kopi than Teh? ____'));
    W.push(sub('c', 'How many cups of Lime juice were sold?   ____   Now draw its bar on the graph.'));
    W.push(sub('d', 'Which two drinks together sold exactly 100 cups?   ________ and ________'));
    W.push(q(2, 'Ali, Mei, Ravi and Siti are each in a different CCA. Use the clues: put a ✓ or a cross in each box, then write each child’s CCA in the last column.', { keepNext: true }));
    W.push(sub('Clue 1', 'Ali is not in the choir and does not play chess.', { after: 40 }));
    W.push(sub('Clue 2', 'Mei and Ravi are not in the choir.', { after: 40 }));
    W.push(sub('Clue 3', 'The swimmer’s name has 4 letters.'));
    { const ws = [1500, 1600, 1600, 1600, 1600, 2000];
      W.push(tbl(ws, [row(['', 'Chess', 'Choir', 'Football', 'Swimming', 'CCA'].map((s, i) => cell(s, ws[i], { bold: true, fill: i === 5 ? 'D9D9D9' : 'EDEDED', h: 40 }))),
        ...['Ali', 'Mei', 'Ravi', 'Siti'].map(n => row([cell(n, ws[0], { bold: true, h: 45 }), ...[1, 2, 3, 4, 5].map(i => cell('', ws[i]))]))])); }
    // ---------- page 2 ----------
    W.push(q(3, 'Draw it! Queues.', { pb: true, before: 0, keepNext: true }));
    W.push(sub('a', 'Ben is 3rd from the front and 5th from the back. How many in the queue?  ____'));
    W.push(sub('b', 'Ali is 2nd from the front, Siti is last, 3 people are between them. How many in all?  ____'));
    W.push(q(4, 'List it! Make 3-digit numbers with these cards. Use each card once in every number.', { keepNext: true }));
    W.push(fig(digitCards()));
    W.push(sub('a', 'List ALL the numbers, in order from smallest to largest.'));
    W.push(...lines(1));
    W.push(sub('b', 'How many of them are odd numbers?   ____'));
    W.push(sub('c', 'Which number is closest to 600?   ____'));
    W.push(q(5, 'Make a table! Squares are made in a row with sticks. Fill in the table.', { keepNext: true }));
    W.push(fig(sticks()));
    { const ws = [2100, 1300, 1300, 1300, 1300, 1300, 1300];
      W.push(tbl(ws, [row(['Squares', '1', '2', '3', '4', '5', '6'].map((s, i) => cell(s, ws[i], { bold: true, fill: 'EDEDED', h: 50 }))),
        row(['Sticks', '4', '7', '10', '', '', ''].map((s, i) => cell(s, ws[i], { bold: i === 0, h: 60, size: 24 })))])); }
    W.push(sub('a', 'How many sticks are needed for 8 squares?   ____'));
    W.push(sub('b', 'Ben uses 31 sticks. How many squares does he make?   ____'));
    W.push(q(6, '(if time) I am a 3-digit odd number. My digits add up to 6. My hundreds digit is bigger than my tens digit. None of my digits is 0. What could I be? Find ALL the answers.', { keepNext: true }));
    W.push(...lines(2));
    return W;
  }
};
