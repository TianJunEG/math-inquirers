// Math Inquirers P2, Lesson 3: Legs, Wheels and Arrays (Multiplication and division, tables 2, 3, 4, 5, 10)
// Every answer below was worked out and checked; "find all" answers list every case.

const N = '#1B2A49', Y = '#FFC93C', SKY = '#DDEBF7', TEAL = '#1F7A6F', RED = '#D64545', W = '#FFFFFF';
const txt = (x, y, s, o = {}) => `<text x="${x}" y="${y}" font-size="${o.size || 18}" font-weight="${o.w || 700}" text-anchor="${o.anchor || 'middle'}" fill="${o.fill || N}" font-family="Fredoka, Arial, sans-serif">${s}</text>`;
const svg = (w, h, label, inner, width) => `<svg viewBox="0 0 ${w} ${h}" xmlns="http://www.w3.org/2000/svg" aria-label="${label}" style="width:${width || w}px;max-width:100%;height:auto">${inner}</svg>`;

// Q1: 4 rows of 5 counters
function arrayFig() {
  let g = '';
  for (let r = 0; r < 4; r++) for (let c = 0; c < 5; c++) g += `<circle cx="${190 + c * 56}" cy="${34 + r * 50}" r="19" fill="${Y}" stroke="${N}" stroke-width="3"/>`;
  return svg(600, 220, 'An array of counters: 4 rows with 5 counters in each row', g, 260);
}
// Q2: tray of 3 rows of 10 cups, a cloth hides rows 2 and 3 except the first cup of each
function trayFig() {
  let g = `<rect x="22" y="14" width="556" height="186" rx="18" fill="${SKY}" stroke="${N}" stroke-width="3"/>`;
  for (let r = 0; r < 3; r++) for (let c = 0; c < 10; c++) {
    const x = 70 + c * 51, y = 52 + r * 56;
    g += `<path d="M${x - 17} ${y - 16} L${x + 17} ${y - 16} L${x + 12} ${y + 18} L${x - 12} ${y + 18} Z" fill="${W}" stroke="${N}" stroke-width="3" stroke-linejoin="round"/>`;
  }
  g += `<rect x="96" y="80" width="474" height="114" rx="12" fill="${RED}" stroke="${N}" stroke-width="3"/>`;
  for (let i = 1; i < 9; i++) g += `<line x1="${96 + i * 52.7}" y1="80" x2="${96 + i * 52.7}" y2="194" stroke="#F2A7A7" stroke-width="3"/>`;
  g += `<line x1="96" y1="137" x2="570" y2="137" stroke="#F2A7A7" stroke-width="3"/>` + txt(333, 145, 'cloth', { size: 26, fill: W });
  return svg(600, 214, 'A tray of cups in 3 rows of 10. A cloth covers all of rows 2 and 3 except the first cup in each row', g, 360);
}
// Q7: a bicycle and a tricycle
function cyclesFig() {
  const wheel = (x, y, r) => `<circle cx="${x}" cy="${y}" r="${r}" fill="${W}" stroke="${N}" stroke-width="4"/><circle cx="${x}" cy="${y}" r="4" fill="${N}"/>`;
  let g = wheel(70, 100, 34) + wheel(200, 100, 34) + `<path d="M70 100 L120 52 L175 52 L200 100 M120 52 L135 100 L70 100 M175 52 L170 34 M160 34 L184 34" fill="none" stroke="${TEAL}" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/><rect x="108" y="40" width="26" height="9" rx="4" fill="${N}"/>` + txt(135, 160, 'bicycle: 2 wheels', { size: 20 });
  g += wheel(500, 96, 38) + [372, 414].map(x => `<ellipse cx="${x}" cy="108" rx="11" ry="28" fill="${W}" stroke="${N}" stroke-width="4"/><circle cx="${x}" cy="108" r="3" fill="${N}"/>`).join('') + `<path d="M372 108 L414 108 M393 108 L460 70 L500 96 M460 70 L452 44 M440 44 L466 44" fill="none" stroke="${RED}" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/><rect x="408" y="62" width="30" height="9" rx="4" fill="${N}"/>` + txt(440, 160, 'tricycle: 3 wheels', { size: 20 });
  return svg(600, 172, 'A bicycle with 2 wheels and a tricycle with 3 wheels: one big front wheel and two rear wheels side by side', g, 360);
}

const lesson = {
  n: 3, week: 2, session: 'A', title: 'Legs, Wheels and Arrays', topic: 'Multiplication and Division',
  objective: 'Read an array as rows of equal groups and write two multiplication and two division sentences for it; solve "how many of each" legs and wheels puzzles with a table; share with leftovers and decide what the leftover means; find all the arrays for a number.',
  skills: 'Draw it (arrays), make a table, guess and check, working in order to find all the ways',
  materials: 'About 30 counters per pair, mini whiteboards, squared paper. Optional: picture cards of hens and goats, bicycles and tricycles.',
  online: 'Each child has 30 small objects (buttons, dried beans or Lego bricks) and a whiteboard or paper. The tutor shares the slides; children hold their arrays and tables up to the camera.',
  warmup: 'Legs and wheels count: three picture cards (4 cars, 6 hens, 5 bicycles). Count the wheels or legs in 2s and 4s, then click to check. About 2.5 minutes.',
  explore: 'Farm legs: a pen has only hens (2 legs) and goats (4 legs). The farmer counts 16 legs. Pairs use counters or drawings to find every possible mix of hens and goats, and record each one.',
  mini: 'Arrays: rows × number in each row; two multiplication and two division facts from one array; count the hidden part of an array. Then "how many of each": start with all of one kind in a table and swap one at a time. Sharing with leftovers (Q4, Q5) is division with a remainder, a P3 topic: say "3 left over" in words and do not write remainders as "r 3".',
  share: 'Ravi shares stickers equally among 4 friends. Can the number left over ever be 4 or more? Why?',
  exit: { q: 'A pen has hens and goats. There are 5 animals and 14 legs. How many hens and how many goats?', a: '3 hens and 2 goats (6 + 8 = 14 legs).' },
  mistakes: [
    'Counting the hidden part of an array one by one (or guessing) instead of using rows × number in each row and taking away the ones you can see.',
    'Giving the number of whole groups as the answer when the leftover still needs a place (28 children, vans of 5: writing 5 vans instead of 6).',
    'In "how many of each" puzzles, matching only one clue (the legs) and forgetting to check the other (the number of animals).'
  ],
  takehome: 'None: all six Core questions fit in class, so no Core item moves to take-home in this lesson.',
  extension: 'Find all the arrays (at least 2 rows, at least 2 in each row) for 16 counters. (3 ways: 2 rows of 8, 4 rows of 4, 8 rows of 2.)',
  key: [
    ['Q1', '(a) 4 × 5 = 20 and 5 × 4 = 20.  (b) 20 ÷ 4 = 5 and 20 ÷ 5 = 4.'],
    ['Q2', '(a) 30 cups (3 rows of 10).  (b) 18 cups. We can see 12 (10 in the top row and 1 more in each of the other 2 rows), and 30 − 12 = 18.  (c) e.g. "3 rows of 10 is 30, then take away the 12 I can see."'],
    ['Q3', '4 hens and 3 goats. Table: 7 hens 0 goats 14 legs; 6, 1, 16; 5, 2, 18; 4, 3, 20. Each swap adds 2 legs. Check: 8 + 12 = 20 legs and 4 + 3 = 7 animals.'],
    ['Q4', '(a) 5 stickers each (4 × 5 = 20).  (b) 3 left over.  (c) 1 more sticker: 24 stickers give 6 each with none left over.'],
    ['Q5', '(a) 6 vans. 5 vans hold 25 children and the other 3 children need a van too.  (b) 2 empty seats (6 vans hold 30, and 30 − 28 = 2).'],
    ['Q6', '4 ways: 2 rows of 10, 4 rows of 5, 5 rows of 4, 10 rows of 2. 3 rows does not work (3 rows of 6 is 18, 3 rows of 7 is 21). More than 10 rows would leave fewer than 2 chairs in a row.']
  ]
};

const script = {
  hook: ['Welcome back, inquirers! Today we are on a farm and in a bicycle shop. We will count legs and wheels, line things up in neat rows called arrays, and share things out fairly.', 'Our big question today: when there are two kinds of things mixed up, how can we find out how many of each there are, without guessing wildly?'],
  warmIntro: ['Here are some cards. Each card shows some cars, bicycles or animals. Count the wheels or the legs. Count in 2s, 3s, 4s or 5s, not in 1s!', 'Show me the number with your fingers or on your whiteboard. Then we will click to check.'],
  predict: ['The farmer has only hens and goats in a pen. He counts 16 legs. How many animals do you think there are? Is there only one answer? Write a guess.'],
  exploreHints: [
    'Stuck: try all hens first. How many hens make 16 legs?',
    'Then swap one hen for a goat. What happens to the number of legs? Fix it.',
    'Finished early: which mix has the most animals? Which has the fewest? How do you know there are no more mixes?'
  ],
  think: [
    '"3 rows of 4 dots. I count the rows: 3. I count how many in each row: 4. 4, 8, 12. So 3 × 4 = 12. If I turn my head, it is 4 rows of 3, so 4 × 3 = 12 too. Sharing 12 into 3 rows gives 4 in each row: 12 ÷ 3 = 4. Putting 12 in groups of 4 gives 3 groups: 12 ÷ 4 = 3."',
    '"Part of this tray is under a cloth. I do not need to see every cookie. The top row shows 5 in each row. The side shows 4 rows. 4 rows of 5 is 20. I can see 8, so 20 − 8 = 12 are hidden."',
    '"6 vehicles, bicycles and cars, 16 wheels. I start with all bicycles: 6 bicycles is 12 wheels. Too few. I swap one bicycle for a car: that adds 2 wheels, 14. Swap again: 16. So 4 bicycles and 2 cars. Check: 8 + 8 = 16 wheels, 4 + 2 = 6 vehicles."'
  ],
  circulate: [
    'Ask: "How many rows? How many in each row? Which multiplication is that?"',
    'Ask: "What changes each time you swap one animal for the other kind?"',
    'Ask: "Did you check BOTH clues: the number of animals and the number of legs?"'
  ],
  hints: [
    'Hint 1: "Draw it. Dots in rows, or circles for heads and sticks for legs."',
    'Hint 2: "Start with all of one kind. Then swap one at a time."',
    'Hint 3: "Make a table so you can see the pattern and do not miss a row."'
  ],
  talk: ['"Ravi shares stickers equally among 4 friends. Can the number left over ever be 4 or more?"'],
  talkAns: 'No. If 4 or more were left, Ravi could give each friend one more, so the leftover is always 0, 1, 2 or 3.',
  close: ['"Today you drew arrays, made tables and checked both clues. Next time a puzzle has two kinds of things mixed up, start with all of one kind and swap one at a time."']
};

const deck = {
  today: 'Use arrays for multiplication and division, find how many of each with a table, and share with leftovers.',
  warmGame: 'Legs and wheels count, three picture cards: 4 cars, 6 hens, 5 bicycles. Count the wheels or legs in 2s and 4s. (Spare cards: 3 tricycles, 5 dogs, 2 cars and 1 bicycle.)',
  warmQs: [['3 × 5 = ?', '15'], ['4 groups of 4. How many?', '16'], ['20 ÷ 2 = ?', '10'], ['30 shared equally by 10 children. How many each?', '3'], ['How many 5s make 35?', '7']],
  expSetup: ['A pen has only hens (2 legs) and goats (4 legs).', 'The farmer counts 16 legs altogether.', 'Use counters or drawings to find a mix of hens and goats.', 'Find every mix. Record each one.'],
  expPic: 'a farm pen with a hen (2 legs) and a goat (4 legs) beside it and a sign that reads "16 legs".',
  expAsk: [['How many different mixes did you find?', '5 mixes: 8 hens; 6 hens and 1 goat; 4 hens and 2 goats; 2 hens and 3 goats; 4 goats.'], ['How do you know you have them all?', 'The goats went 0, 1, 2, 3, 4. Five goats would need 20 legs, too many.'], ['What happens each time you swap 2 hens for 1 goat?', 'The legs stay at 16: 2 hens have 4 legs, the same as 1 goat.']],
  mini1: { head: 'Arrays: rows of equal groups', body: ['3 rows of 4 dots.', '3 × 4 = 12 and 4 × 3 = 12.', '12 ÷ 3 = 4 and 12 ÷ 4 = 3.', 'A tray of 4 rows of 5 cookies has some under a cloth. We can see 8. How many are hidden?'], ans: '12 hidden (4 rows of 5 is 20, and 20 − 8 = 12).' },
  mini2: { head: 'How many of each? Make a table', body: ['6 vehicles: bicycles (2 wheels) and cars (4 wheels). 16 wheels altogether.', 'Start with all bicycles: 6 bicycles, 12 wheels.', 'Swap one bicycle for a car each time: 14, then 16 wheels.', 'How many of each?'], ans: '4 bicycles and 2 cars (8 + 8 = 16 wheels).' },
  keyHead: 'Key idea: draw it, then make a table',
  keyBig: 'An array is rows of equal groups: rows × number in each row. For "how many of each", start with all of one kind and swap one at a time in a table.',
  keySmall: 'Every swap changes the total by the same amount. Check both clues at the end.',
  brk: 'Array moves. The tutor calls "3 rows of 4!": do 3 rows of 4 claps, counting 4, 8, 12. Then "5 rows of 2" jumps and "2 rows of 10" stomps.',
  ws1: 'Page 1, in pairs: Q1 an array, Q2 the cups under the cloth, Q3 hens and goats with a table.',
  ws2: 'Page 2, on your own: Q4 sharing stickers, Q5 vans for a trip, Q6 all the arrays of 20 chairs. (Bicycles and tricycles is Go further 7, not part of page 2.)'
};

const qbank = {
  core: [
    { q: 'How many wheels are there on 5 bicycles?', a: '10 wheels (2, 4, 6, 8, 10).' },
    { q: 'There are 4 rows of chairs with 5 chairs in each row. How many chairs are there?', a: '20 chairs (4 × 5 = 20).' },
    { q: '18 sweets are shared equally among 3 children. How many sweets does each child get?', a: '6 sweets (18 ÷ 3 = 6).' },
    { q: 'How many legs do 7 hens have?', a: '14 legs (7 × 2 = 14).' },
    { q: 'An array has 2 rows of 10 dots. Write two multiplication sentences and two division sentences for it.', a: '2 × 10 = 20, 10 × 2 = 20, 20 ÷ 2 = 10, 20 ÷ 10 = 2.' },
    { q: '25 pencils are tied in bundles of 5. How many bundles are there?', a: '5 bundles (25 ÷ 5 = 5).' }
  ],
  stretch: [
    { q: 'A shop has some bicycles (2 wheels) and some tricycles (3 wheels), at least one of each. There are 17 wheels altogether. Find ALL the ways. Start with 1 tricycle, then 2 tricycles, and so on. Make a table or use counters. How do you know you have found them all?', a: '3 ways: 7 bicycles and 1 tricycle (14 + 3); 4 bicycles and 3 tricycles (8 + 9); 1 bicycle and 5 tricycles (2 + 15). 0, 2 or 4 tricycles leave an odd number of wheels, which bicycles cannot make, and 6 or more tricycles need 18 wheels or more.', fig: cyclesFig() },
    { q: 'A farm has 9 animals, each a hen (2 legs) or a goat (4 legs). Mei counts 25 legs. Siti counts 26 legs. Only one of them can be right. Who? How many hens and goats?', a: 'Siti is right: 5 hens and 4 goats (10 + 16 = 26). Mei cannot be right: every hen has 2 legs and every goat has 4 legs, so the total is always an even number, and 25 is odd. (Start with 9 hens, 18 legs; each swap to a goat adds 2: 18, 20, 22, 24, 26.)' },
    { q: 'Ali shares 34 marbles equally among 4 friends, giving as many as he can. How many does each friend get? How many are left over?', a: '8 each (4 × 8 = 32) and 2 left over.' },
    { q: 'An array of stickers has 4 rows. Ben counts 12 stickers in the first 3 rows. How many stickers are in the whole array?', a: '16 stickers. 3 rows have 12, so each row has 4 (12 ÷ 3 = 4); 4 rows of 4 is 16.' },
    { q: '27 children go on a boat ride. Each boat holds 4 children. How many boats are needed? How many empty seats are there?', a: '7 boats (6 boats hold 24, and the other 3 children need a boat too). 7 boats have 28 seats, so 1 empty seat.' },
    { q: 'In a car park there are cars (4 wheels) and motorcycles (2 wheels). There are 8 vehicles and 22 wheels. How many cars are there?', a: '3 cars (and 5 motorcycles). Start with 8 motorcycles (16 wheels); each swap to a car adds 2 wheels; 3 swaps make 22. Check: 12 + 10 = 22.' },
    { q: 'Find all the numbers from 21 to 49 that can be shared equally into 5 groups AND equally into 2 groups with nothing left over.', a: '30 and 40 (they are in both the 5 and the 2 times tables).' },
    { q: 'Siti has 24 cupcakes. She puts them in boxes with the same number in every box. The boxes hold 2, 3, 4, 5 or 10 cupcakes. Which box sizes leave no cupcakes over, and how many boxes does each need?', a: 'Boxes of 2 (12 boxes), boxes of 3 (8 boxes), boxes of 4 (6 boxes). Boxes of 5 and 10 leave 4 over.' },
    { q: 'A table has 4 legs and a stool has 3 legs. Ravi counts 17 legs on the tables and stools in a room. How many tables and how many stools are there?', a: '2 tables and 3 stools (8 + 9 = 17). No other mix works: 0, 1, 3 or 4 tables leave 17, 13, 5 or 1 legs, which are not in the 3 times table.' }
  ],
  challenge: [
    { q: 'Ali says: “Every number from 4 to 30 can be made into an array with at least 2 rows and at least 2 counters in each row.” Is he right? Find ALL the numbers that cannot. Explain why they cannot.', a: 'No. 5, 7, 11, 13, 17, 19, 23 and 29 cannot (8 numbers): only 1 row works.' },
    { q: 'A shop sells bicycles (2 wheels), tricycles (3 wheels) and toy cars (4 wheels). There are 9 vehicles and 28 wheels altogether, with at least one of each kind. Find ALL the ways.', a: '3 ways (bikes, trikes, cars): 3, 2, 4; 2, 4, 3; 1, 6, 2.' },
    { q: 'A pen has 10 animals, all hens (2 legs) and goats (4 legs). What are ALL the numbers of legs that Mei could count? Why can she never count 21 legs, or 42 legs?', a: '20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40 (11 numbers). All hens is 20 legs and each swap to a goat adds 2, up to all goats at 40. 21 is odd and the total is always even; 42 is more than 10 goats can have (40).' },
    { q: 'Mei says: "I counted the legs of some hens and goats. There were 9 legs." Can she be right? Explain.', a: 'No. Hens have 2 legs and goats have 4, so the total is always an even number (in the 2 times table). 9 is odd.' },
    { q: 'Make up your own “how many of each” puzzle with two kinds of things that have different numbers of legs or wheels. Write the clues (how many things, how many legs or wheels) so that there is exactly ONE answer. Solve it with a table, then swap with a partner. Then change the number of legs in your puzzle so that it has NO answer.', a: 'Open. Example: spiders (8 legs) and birds (2 legs): 5 animals and 28 legs gives 3 spiders and 2 birds (24 + 4 = 28), and it is the only answer because each swap changes the legs by 6. With 5 animals and 25 legs there is no answer: the total is always even.' },
    { q: 'I am a number between 10 and 30. I can be put into groups of 3 with none left over, and into groups of 4 with none left over. When I am put into groups of 5, 4 are left over. What number am I?', a: '24. Numbers in both the 3 and 4 times tables between 10 and 30 are 12 and 24; 12 in groups of 5 leaves 2, 24 leaves 4.' },
    { q: 'A shop has 12 vehicles. Each one is a bicycle (2 wheels) or a tricycle (3 wheels). Mei says: “Ravi could count 24 wheels, or 25, or 26, or any number of wheels up to 36.” Is she right? Could he count 37? Then think about 12 hens (2 legs) and goats (4 legs): why can Ravi count 25 wheels but never 25 legs?', a: 'Mei is right. All 12 bicycles make 24 wheels and all 12 tricycles make 36. Each swap of a bicycle for a tricycle adds exactly 1 wheel, so the totals go up 1 at a time and none is skipped: every number from 24 to 36, and 37 is too many. For hens and goats each swap adds 2 legs, so the total can only be 24, 26, 28 … 48: always even, so never 25.' },
    { q: 'Mr Lim has between 20 and 30 sweets. When he puts them in groups of 4, 3 are left over. When he puts them in groups of 5, 2 are left over. How many sweets does he have?', a: '27. Groups of 4 with 3 left: 23 or 27. Groups of 5 with 2 left: 22 or 27. Only 27 is in both lists.' },
    { q: 'A pen has hens and goats. There are 2 more hens than goats. There are 22 legs altogether. How many hens and how many goats?', a: '5 hens and 3 goats. Guess and check: 1 goat and 3 hens make 10 legs; 2 and 4 make 16; 3 and 5 make 22. Check: 12 + 10 = 22.' }
  ]
};

const workbook = H => {
  const out = [];
  const hw = [2400, 1500, 1500, 1500, 1500, 1500];
  const hr = (lab, first) => H.row([H.cell(lab, hw[0], { bold: true, fill: 'D9D9D9', h: 80 }), H.cell(first || '\u00a0', hw[1], { h: 80 }), ...hw.slice(2).map(w => H.cell('\u00a0', w, { h: 80 }))]);
  // ---- page 1 (in pairs)
  out.push(H.q(1, 'Mei puts counters in an array.', { before: 20, keepNext: true }));
  out.push(H.fig(arrayFig()));
  out.push(H.sub('a', 'Two multiplication sentences:     ____ × ____ = ____        ____ × ____ = ____'));
  out.push(H.sub('b', 'Two division sentences:     ____ ÷ ____ = ____        ____ ÷ ____ = ____'));
  out.push(H.q(2, 'A tray has the same number of cups in every row. A cloth covers some of the cups.', { keepNext: true }));
  out.push(H.fig(trayFig()));
  out.push(H.sub('a', 'How many cups altogether?   ______        (b)  How many under the cloth?   ______'));
  out.push(H.sub('c', 'How did you work it out without lifting the cloth?'));
  out.push(...H.lines(1));
  out.push(H.q(3, 'A pen has hens and goats. A hen has 2 legs and a goat has 4 legs. There are 7 animals and 20 legs altogether. Start with all hens. Then swap one hen for a goat each time.', { keepNext: true }));
  { const ws = [1900, 1600, 1600, 1600, 1600, 1600];
    const r = (lab, first) => H.row([H.cell(lab, ws[0], { bold: true, fill: 'D9D9D9', h: 80 }), H.cell(first, ws[1], { h: 80 }), ...ws.slice(2).map(w => H.cell('\u00a0', w, { h: 80 }))]);
    out.push(H.tbl(ws, [r('Hens', '7'), r('Goats', '0'), r('Legs', '14')])); }
  out.push(H.gap(30));
  out.push(H.sub('a', 'How many hens and how many goats?    ______ hens    ______ goats'));
  // ---- page 2 (on your own)
  out.push(H.q(4, 'Ravi has 23 stickers. He shares them equally among 4 friends, giving each friend as many as he can. Tip: draw 4 friends and deal out the stickers one at a time.', { pb: true, before: 0, keepNext: true }));
  out.push(H.sub('a', 'How many does each friend get?   ______        (b)  How many are left over?   ______'));
  out.push(H.sub('c', 'What is the smallest number of extra stickers Ravi needs so that none are left over?   ______'));
  out.push(H.q(5, '28 children go on a trip. Each van holds 5 children.', { keepNext: true }));
  out.push(H.sub('a', 'How many vans are needed?   ______        (b)  How many empty seats?   ______'));
  out.push(H.q(6, 'Mr Tan puts 20 chairs in equal rows. There must be at least 2 rows and at least 2 chairs in each row. Find ALL the ways. Try 2 rows, 3 rows, 4 rows and so on. Stop at 10 rows.', { keepNext: true }));
  { const w6 = [2100, 867, 867, 867, 867, 867, 867, 867, 867, 864];
    const r6 = (lab, vals) => H.row([H.cell(lab, w6[0], { bold: true, fill: 'D9D9D9', h: 80 }), ...w6.slice(1).map((w, i) => H.cell(vals ? String(vals[i]) : '\u00a0', w, { h: 80 }))]);
    out.push(H.tbl(w6, [r6('Rows', [2, 3, 4, 5, 6, 7, 8, 9, 10]), r6('Chairs in each row'), r6('Does it work?')])); }
  return out;
};

module.exports = { lesson, script, deck, qbank, workbook };
