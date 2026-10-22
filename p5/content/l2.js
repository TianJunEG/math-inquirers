// Math Inquirers P5 — Lesson 2: Fraction Feats (four operations of fractions, fraction and division)
// Heuristics: draw a model (bar or pizza); test in order (unit fractions: try 1/2, 1/3, 1/4 … and stop when the first part is too small);
// find the remainder first, then take the fraction of the remainder; look for a pattern in the sums; test both ways.
// Every answer below was worked out and checked with Python (fractions module, exact search over all cases).
const N = '#1B2A49', Y = '#FFC93C', SKY = '#DDEBF7', TEAL = '#1F7A6F', RED = '#D64545', WH = '#FFFFFF';
const FF = 'Fredoka, Arial, sans-serif';
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const txt = (x, y, s, size = 18, fill = N, anchor = 'middle', weight = 700) =>
  `<text x="${x}" y="${y}" font-size="${size}" font-weight="${weight}" text-anchor="${anchor}" fill="${fill}" font-family="${FF}">${esc(s)}</text>`;

// stacked fraction for workbook text (raw HTML, so pass it inside an array)
const fr = (n, d) => `<span style="display:inline-flex;flex-direction:column;align-items:center;vertical-align:middle;line-height:1.1;margin:0 3px;font-weight:600"><span style="padding:0 3px">${n}</span><span style="border-top:2px solid ${N};padding:0 3px">${d}</span></span>`;
const BOX = `<span style="display:inline-block;width:30px;height:26px;border:2px solid ${N};border-radius:5px;background:#fff;vertical-align:middle"></span>`;
const ufr = () => fr(1, BOX);
const card = d => `<span style="display:inline-flex;width:30px;height:38px;border:2px solid ${N};border-radius:6px;background:${Y};align-items:center;justify-content:center;font-weight:700;font-size:20px;vertical-align:middle;margin:0 3px">${d}</span>`;
const boxfr = () => `<span style="display:inline-flex;flex-direction:column;align-items:center;vertical-align:middle;margin:0 4px">${BOX}<span style="border-top:2px solid ${N};width:36px;margin:3px 0"></span>${BOX}</span>`;

// bar model for Q3: 240 stickers, a bar cut into 4 equal parts
const stickerBar = () => {
  const x0 = 60, w = 480, y = 46, h = 50;
  let g = `<path d="M${x0} ${y - 8} V${y - 20} H${x0 + w} V${y - 8}" fill="none" stroke="${N}" stroke-width="2.5"/>` + txt(x0 + w / 2, y - 28, '240 stickers', 17);
  for (let i = 0; i < 4; i++) g += `<rect x="${x0 + i * w / 4}" y="${y}" width="${w / 4}" height="${h}" fill="${i === 0 ? SKY : WH}" stroke="${N}" stroke-width="2.5"/>`;
  g += txt(x0 + w / 8, y + h + 24, 'Ben', 16, TEAL) + txt(x0 + w * 5 / 8, y + h + 24, 'the remainder: draw the rest!', 16, TEAL);
  return `<svg aria-label="A bar for 240 stickers cut into 4 equal parts; the first part is for Ben" viewBox="0 0 600 126" width="600" xmlns="http://www.w3.org/2000/svg" style="max-width:62%">${g}</svg>`;
};

// Q1(c): Group A's share (2/3) and Group B's share (3/5) drawn as bars of the same length (drawn shapes, no glyphs)
const shareBars = () => {
  const x0 = 90, w = 360; let g = '';
  [['Group A', 3, 2], ['Group B', 5, 3]].forEach(([lab, parts, shaded], r) => {
    const y = 12 + r * 52;
    g += txt(x0 - 10, y + 27, lab, 16, N, 'end');
    for (let i = 0; i < parts; i++) g += `<rect x="${x0 + i * w / parts}" y="${y}" width="${w / parts}" height="38" fill="${i < shaded ? Y : WH}" stroke="${N}" stroke-width="2.5"/>`;
  });
  g += txt(x0 + w + 12, 40, 'shaded = a share', 15, TEAL, 'start', 600);
  return `<svg aria-label="Two bars of the same length. Group A is cut in 3 equal parts with 2 shaded. Group B is cut in 5 equal parts with 3 shaded." viewBox="0 0 650 120" width="650" xmlns="http://www.w3.org/2000/svg" style="max-width:58%">${g}</svg>`;
};

module.exports = {
  lesson: {
    n: 2, week: 1, session: 'B', title: 'Fraction Feats', topic: 'Fractions: Four Operations',
    objective: 'Link fractions and division (3 ÷ 4 = 3/4); write fractions as the sum of two different unit fractions by testing in order; solve fraction-of-a-remainder problems forwards and backwards with a bar model; and spot and explain patterns in fraction sums.',
    skills: 'Fraction and division (whole number ÷ whole number), drawing a model (bar, pizza), testing in order and knowing when to stop, fraction of a remainder, working backwards, looking for a pattern, testing both ways',
    materials: 'Paper circles (6 per child) to cut as pizzas, scissors, a strip of paper for bar models, digit cards 1 to 4, mini whiteboard, workbook.',
    online: 'Children cut out six paper circles before the lesson and fold or cut them on camera. The tutor shares the slides and draws the bar models live. Pairs work in breakout rooms for the explore and page 1.',
    warmup: 'Fraction Face-off: two fractions appear; children hold up 1 finger if the first is bigger and 2 if the second is. Nobody has to explain their finger: pairs whisper a reason to a partner (same top? close to 1? more than a whole?) and only volunteers share it. Then five quick questions on whiteboards.',
    explore: 'Pizza sharing: pairs share 3 pizzas equally among 4 friends, then 5 pizzas among 6 friends, with paper circles. How much does each friend get? Can you cut so that each friend gets only 2 pieces?',
    mini: 'a ÷ b = a/b: 3 pizzas among 4 friends gives 3/4 each, and 7 pizzas among 3 friends gives 7/3 = 2 1/3 each. Unit fractions: try 1/2, 1/3, 1/4 … in order, take it away and check whether what is left is a unit fraction; stop once the first part is less than half of the fraction. Fraction of a remainder: find the remainder first, then take the fraction of the remainder, with a bar model cut into equal small units. Before page 2: a pattern in fraction sums (1 take away the last piece), working backwards with a model, and testing both ways with digit cards.',
    share: 'Ben says 1/2 + 1/3 = 2/5 because you add the tops and add the bottoms. Use a pizza picture to show why he is wrong.',
    exit: { q: '(a) 4 pizzas are shared equally among 5 children. How much does each child get?  (b) Ali had 60 marbles. He gave 1/3 of them to Mei and 1/2 of the remainder to Ben. How many marbles did Ali have left?', a: '(a) 4/5 of a pizza  (b) 20 marbles (60 − 20 = 40 left, then half of 40 is given away)' },
    mistakes: [
      'Taking the second fraction of the whole amount instead of the remainder (2/3 of 240 instead of 2/3 of 180).',
      'Adding tops and bottoms: 1/2 + 1/3 = 2/5, or using the same unit fraction twice when the question asks for different ones.',
      'Writing 3 ÷ 4 as 4/3, or writing 7 ÷ 3 as 3/7.'
    ],
    extension: 'Write 1 as the sum of three different unit fractions. Is there more than one way? (Only one: 1/2 + 1/3 + 1/6.)',
    key: [
      ['Q1', '(a) 5/8  (b) 9/4 = 2 1/4 m  (c) Group A. 2/3 = 10/15 and 3/5 = 9/15. (Or: each child in A is 1/3 short of a whole pizza, in B 2/5 short, and 2/5 is more than 1/3.)'],
      ['Q2', '(a) 1/2 + 1/5  (b) 1/4 + 1/5  (c) 1/3 + 1/24 and 1/4 + 1/8. (1/5 leaves 7/40, not a unit fraction; after that the first part is less than half of 3/8, so stop.)'],
      ['Q3', '(a) 120  (b) 60  (c) 1/4. Ben 60, remainder 180, Ali 2/3 of 180 = 120, left 60 = 1/4 of 240.'],
      ['Q4', '(a) 1/30, 1/42. The bottom numbers are 1 × 2, 2 × 3, 3 × 4, 4 × 5, …  (b) 2/3, 3/4, 4/5  (c) 9/10. 1/90 is the 9th term (9 × 10), and each sum is 1 take away the next unit fraction.'],
      ['Q5', '(a) $120  (b) $36. Model: 10 equal units; game 4, book 3, left 3 units = $36, so 1 unit = $12.'],
      ['Q6', '(a) 4/1 + 3/2 = 5 1/2  (b) 1/3 + 2/4 = 5/6 (1/4 + 2/3 = 11/12 is bigger, so test both ways)  (c) 1/4 + 2/3 = 11/12, only 1/12 away from 1']
    ]
  },

  script: {
    hook: ['Welcome back, inquirers! Today is pizza day: we share pizzas fairly, cut them in clever ways and find out what the Ancient Egyptians knew about fractions.', 'Notice it, test it, explain why: by the end you will solve fraction puzzles that trip up grown-ups.'],
    warmIntro: ['Fraction Face-off! Two fractions appear. One finger if the first is bigger, two fingers if the second is bigger.', 'Tell your partner a reason in a whisper: same top? Close to 1? More than a whole? Try it without common denominators first, but any method is welcome. I will only ask volunteers to share, and you may pass.'],
    predict: ['3 pizzas are shared equally among 4 friends. Will each friend get more than half a pizza or less? Write your prediction before you cut anything.'],
    exploreHints: ['Stuck: cut every pizza into 4 equal pieces. How many pieces are there? How many does each friend get?', 'Too many pieces: can you cut some pizzas in halves and only one into quarters?', 'Finished early: share 5 pizzas among 6 friends so that each friend gets just 2 pieces.'],
    think: [
      '“3 pizzas among 4 friends. If I cut each pizza into quarters, there are 12 quarters and each friend gets 3 of them: 3/4. So 3 ÷ 4 = 3/4. The top number is what is shared, the bottom number is how many share it.”',
      '“Now 7/12 as two different unit fractions. I try in order. 1/2: 7/12 − 6/12 = 1/12, a unit fraction, yes. 1/3: 7/12 − 4/12 = 3/12 = 1/4, yes. 1/4: what is left is 1/3, the same pair again. Once my first part is smaller than half of 7/12, the other part would be bigger, so I stop. Two ways.”',
      '“Mei had 180 beads. She used 1/3 for a bracelet and 3/4 of the REMAINDER for a necklace. I draw a bar in 3 parts. The remainder is 2 parts, which I cut into 4 small units, so the whole bar is 6 small units. Bracelet 2, necklace 3, left 1. 6 units = 180, so 1 unit = 30. She has 30 beads left.”'
    ],
    circulate: ['Ask: “Is that a fraction of the whole or of the remainder?”', 'Ask: “How do you know you have found all the ways? When can you stop?”', 'Ask: “Show me your model. Are all the small units the same size?”'],
    hints: ['Hint 1: “Draw a bar. Cut it into the parts the first fraction tells you.”', 'Hint 2: “Cut the remainder again so every unit in the bar is the same size.”', 'Hint 3: “Take away the unit fraction and simplify. Is the top number 1?”'],
    talk: ['“Ben says 1/2 + 1/3 = 2/5 because you add the tops and add the bottoms. Is he right? Use a pizza to show why.”', '“In Q4, why is each sum 1 take away a unit fraction?”'],
    talkAns: 'He is wrong. 1/2 of a pizza is already more than 2/5, so adding 1/3 more cannot give 2/5. Cut into sixths: 1/2 = 3/6 and 1/3 = 2/6, so the total is 5/6. We can only add the tops when the pieces are the same size.',
    close: ['“Today you shared pizzas, found unit fractions by testing in order, took fractions of a remainder with a model and found a pattern in fraction sums. Great inquiring!”', '“Do the exit ticket on your own, then show me.”']
  },

  deck: {
    today: 'Share pizzas fairly, write fractions as unit fractions, take a fraction of a remainder with a model and find patterns in fraction sums.',
    warmGame: 'Fraction Face-off. Two fractions appear. Hold up 1 finger if the first is bigger, 2 if the second is. Whisper a reason to your partner (same top? close to 1? more than a whole?); volunteers share. 3/5 or 3/7, 5/6 or 6/7, 4/9 or 1/2, 7/8 or 8/7.',
    warmQs: [['3 ÷ 4 as a fraction', '3/4'], ['2/3 + 1/6', '5/6'], ['3/4 of 20', '15'], ['Which is bigger, 1/2 or 3/5?', '3/5'], ['1/4 of 12', '3']],
    expSetup: ['Take 3 paper pizzas. Share them equally among 4 friends.', 'How much does each friend get? Write it as a fraction.', 'Can you cut so that each friend gets only 2 pieces?', 'Now share 5 pizzas among 6 friends, with only 2 pieces each.'],
    expPic: 'three pizzas (circles) and four smiley faces waiting for their share, with a question mark.',
    expAsk: [['How much pizza does each of the 4 friends get?', '3/4 of a pizza (3 ÷ 4 = 3/4).'], ['How can each friend get only 2 pieces?', 'Cut 2 pizzas into halves and 1 pizza into quarters: each friend gets 1/2 + 1/4 = 3/4.'], ['5 pizzas among 6 friends, 2 pieces each?', 'Cut 3 pizzas into halves and 2 pizzas into thirds: each gets 1/2 + 1/3 = 5/6.']],
    mini1: { head: 'Write 7/12 as the sum of two different unit fractions', body: ['Try 1/2: 7/12 − 6/12 = 1/12. Yes.', 'Try 1/3: 7/12 − 4/12 = 3/12 = 1/4. Yes.', 'Try 1/4: we get 1/3, the same pair. Stop: the first part is now less than half of 7/12.'], ans: 'Two ways: 1/2 + 1/12 and 1/3 + 1/4.' },
    mini2: { head: 'Mei had 180 beads. She used 1/3 of them for a bracelet and 3/4 of the remainder for a necklace. How many beads were left?', body: ['Bar in 3 parts: bracelet 1 part, remainder 2 parts.', 'Cut the remainder into 4 small units: the whole bar is 6 units.', 'Bracelet 2 units, necklace 3 units, left 1 unit. 6 units = 180.'], ans: '1 unit = 30. 30 beads were left.' },
    keyHead: 'Key idea: the fraction of WHAT?',
    keyBig: 'Find the remainder first, then take the fraction of the remainder. Draw a model with equal small units.',
    keySmall: 'a ÷ b = a/b. Unit fractions: test 1/2, 1/3, 1/4 … in order and stop when the first part is too small.',
    brk: 'Fraction freeze: walk on the spot. When the tutor calls a fraction, freeze in a pose: arms up for more than 1/2, arms out for exactly 1/2, crouch for less than 1/2.',
    ws1: 'Page 1, in pairs: Q1 sharing and fraction and division, Q2 unit fraction puzzles, Q3 fraction of a remainder.',
    ws2: 'Page 2, on your own: Q4 a fraction pattern, Q5 work backwards with a model, Q6 digit-card fractions.'
  },

  qbank: {
    core: [
      { q: '4 friends share 3 chocolate bars equally. Draw the bars and cut them. How much chocolate does each friend get?', a: '3/4 of a bar (cut every bar into 4 pieces: 12 pieces, 3 each; 3 ÷ 4 = 3/4).' },
      { q: 'Siti ate 1/2 of a pizza and Ben ate 1/4 of the same pizza. Draw the pizza. What fraction did they eat altogether? What fraction is left?', a: '3/4 eaten, 1/4 left.' },
      { q: 'A pizza is cut into 12 equal slices (draw it). Ravi eats 1/3 of the pizza and Mei eats 1/4 of the pizza. How many slices did they eat? What fraction of the pizza is left?', a: '4 + 3 = 7 slices eaten; 5 slices are left, which is 5/12 of the pizza.' },
      { q: 'Find 3/5 of 15 sweets. (Draw 15 dots and put them into 5 equal groups.)', a: '9 (each group has 3 dots, and 3 groups make 9).' },
      { q: 'Half of a cake is left. Ali eats half of what is left. Draw the cake. What fraction of the WHOLE cake did Ali eat?', a: '1/4 of the whole cake.' },
      { q: 'Mei has 3/4 of a pizza and Ali has 2/3 of a pizza (the pizzas are the same size). Who has more? Draw two bars to show how you know.', a: 'Mei. Cut both bars into 12 equal parts: 3/4 = 9 parts and 2/3 = 8 parts. (Or: Mei is 1/4 short of a whole pizza and Ali is 1/3 short, and 1/4 is less than 1/3.)' }
    ],
    stretch: [
      { q: 'Can 4/5 be written as the sum of two DIFFERENT unit fractions? Test in order and explain how you know when to stop.', a: 'No. The bigger unit fraction must be more than half of 4/5 (more than 2/5) and less than 4/5, so only 1/2 can be tried: 4/5 − 1/2 = 3/10, which is not a unit fraction. 1/3 is already less than 2/5, so we stop.' },
      { q: 'Ben ate 1/3 of a pizza. Ali ate 1/4 of what was left. What fraction of the pizza is left?', a: '1/2. 2/3 was left after Ben; Ali ate 1/4 of it, so 3/4 of 2/3 = 1/2 is left.' },
      { q: 'Siti shares 3 cakes equally among 8 children. Ben shares 2 cakes equally among 5 children. Whose child gets more cake, and how much more?', a: 'Ben\'s children get more, by 1/40 of a cake. Siti: 3/8 = 15/40 of a cake each. Ben: 2/5 = 16/40 of a cake each. 16/40 − 15/40 = 1/40.' },
      { q: 'Mei walked 3/5 of a path in the morning and 1/4 of the WHOLE path in the afternoon. She still had 600 m to walk. How long is the path?', a: '4000 m. 3/5 + 1/4 = 17/20 of the path is done, so 3/20 is left. 3/20 is 600 m, so 1/20 is 200 m and the whole path is 20 × 200 = 4000 m.' },
      { q: 'Which is bigger, 5/6 or 6/7? Explain without finding common denominators.', a: '6/7. 5/6 is 1/6 short of 1 and 6/7 is only 1/7 short of 1, and 1/7 is smaller than 1/6.' },
      { q: '(Preview of P6) A rope 3/4 m long is cut into 3 equal pieces. How long is each piece? Draw a bar to help.', a: '1/4 m (3/4 ÷ 3: 3 quarters shared by 3 pieces is 1 quarter each).' },
      { q: 'Find a fraction between 2/5 and 1/2 with 20 as the bottom number.', a: '9/20 (2/5 = 8/20 and 1/2 = 10/20).' },
      { q: 'Which is bigger, 7/8 of 24 or 5/6 of 30?', a: '5/6 of 30. 7/8 of 24 = 21 and 5/6 of 30 = 25.' }
    ],
    challenge: [
      { q: 'Write 1 as the sum of three different unit fractions. Find all the ways.', a: 'Only one way: 1/2 + 1/3 + 1/6. (The biggest part must be 1/2, and then 1/2 = 1/3 + 1/6 is the only split into two different unit fractions.)' },
      { q: 'Work out 1/2 × 2/3 × 3/4 × 4/5 × … × 99/100.', a: '1/100. Each top number cancels the bottom number before it, leaving 1 on top and 100 at the bottom.' },
      { q: 'Mrs Tan baked some cookies. She gave 1/2 of them to her neighbours, 1/3 of the remainder to Ben and 1/4 of what was then left to Mei. She had 30 cookies left. How many did she bake?', a: '120. What is left is 1/2 × 2/3 × 3/4 = 1/4 of the cookies, and 1/4 is 30.' },
      { q: 'Make up your own story about a fraction of a REMAINDER (it must use "of what was left" at least once) with a whole-number answer. Solve it with a bar model, swap with a partner, and check each other. Then change one fraction in your story: what changes in the answer, and what stays the same?', a: 'Open-ended. Sample: a shop had 60 oranges, sold 1/3 of them, then 1/4 of the oranges that were left. How many are left? (60 - 20 = 40; 1/4 of 40 = 10; 30 left.) Check that the model uses equal small units and that the second fraction is taken of the remainder.' },
      { q: 'Use the digit cards 1, 3, 5 and 7 once each to make two fractions. Take the smaller from the bigger. What is the smallest difference you can make (more than 0)?', a: '8/35, from 3/7 − 1/5 (15/35 − 7/35).' },
      { q: 'Write 3/4 as the sum of three DIFFERENT unit fractions. Find all the ways and explain how you know you have found them all.', a: 'Exactly three ways: 1/2 + 1/5 + 1/20, 1/2 + 1/6 + 1/12 and 1/3 + 1/4 + 1/6. (The biggest part must be 1/2 or 1/3: three unit fractions of 1/5 or less add to less than 3/4. Then test in order, as in the lesson.)' },
      { q: 'Work out 1/6 + 1/12 + 1/20 + 1/30 + 1/42 without finding a common denominator for all five. (Hint: 1/6 = 1/2 − 1/3.)', a: '5/14. Each fraction is a difference: (1/2 − 1/3) + (1/3 − 1/4) + (1/4 − 1/5) + (1/5 − 1/6) + (1/6 − 1/7). The middle parts cancel, leaving 1/2 − 1/7 = 5/14.' },
      { q: '5 pizzas are shared equally among 12 children. Each child must get exactly 2 pieces, and each piece must be a unit fraction of a pizza (like 1/3 or 1/4). How can the pizzas be cut?', a: 'Each child gets 5/12. Two ways: 1/3 + 1/12 (cut 4 pizzas into thirds and 1 pizza into twelfths), or 1/4 + 1/6 (cut 3 pizzas into quarters and 2 pizzas into sixths).' },
      { q: 'A tank is full of water. Every hour, 1/3 of the water that is in the tank is let out. After 3 hours there are 16 litres left. (a) How much water was in the full tank? (b) After how many hours is less than half of the original water left? (c) How much water has been let out by then?', a: '(a) 54 litres: each hour 2/3 is left, 54 → 36 → 24 → 16.  (b) 2 hours: 24 litres is less than half of 54 (27), but after 1 hour 36 litres is more than half.  (c) 54 − 24 = 30 litres.' }
    ]
  },

  workbook: H => {
    const W = [];
    // Q1 sharing
    W.push(H.q(1, 'Sharing. Remember: a ÷ b = a/b.', { before: 20, keepNext: true }));
    W.push(H.sub('a', '5 pizzas are shared equally among 8 children. Each gets  ______  of a pizza.'));
    W.push(H.sub('b', 'A 9 m ribbon is cut into 4 equal pieces. Each piece is  ______  m long.  (a fraction or mixed number)'));
    W.push(H.sub('c', 'Group A shares 2 pizzas among 3 children. Group B shares 3 pizzas among 5 children. In which group does each child get more? Explain.', { after: 20 }));
    W.push(H.p(['<b style="color:' + TEAL + '">Hint:</b> how much of a whole pizza is each child short of?'], { after: 10 }));
    W.push(H.fig(shareBars()));
    // Q2 unit fractions
    W.push(H.q(2, 'Write each fraction as the sum of two DIFFERENT unit fractions (1 on top). Take away 1/2, then 1/3 … Is what is left a unit fraction?', { keepNext: true }));
    W.push(H.p(['<b style="color:' + TEAL + '">Start here:</b>&nbsp; ' + fr(7, 10) + ' − ' + fr(1, 2) + '. Write ' + fr(1, 2) + ' as tenths: ' + fr(1, 2) + ' = ' + fr('____', 10) + '. So ' + fr(7, 10) + ' − ' + fr(1, 2) + ' = ' + fr('____', 10) + ' = ' + fr(1, '____') + '.'], { after: 20 }));
    W.push(H.sub('a', [fr(7, 10) + '&nbsp; = &nbsp;' + ufr() + '&nbsp; + &nbsp;' + ufr() + '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>(b)</b>&nbsp;&nbsp; ' + fr(9, 20) + '&nbsp; = &nbsp;' + ufr() + '&nbsp; + &nbsp;' + ufr() + '&nbsp;&nbsp; <span style="font-size:15px">(hint: ' + fr(1, 4) + ' = ' + fr('__', 20) + ')</span>']));
    W.push(H.sub('c', ['Find TWO ways for ' + fr(3, 8) + ':&nbsp;&nbsp; ' + fr(3, 8) + ' = ' + ufr() + ' + ' + ufr() + '&nbsp;&nbsp;&nbsp; and &nbsp;&nbsp;&nbsp;' + fr(3, 8) + ' = ' + ufr() + ' + ' + ufr()]));
    W.push(H.sub(' ', 'Test 1/3, 1/4, 1/5 … in order. How do you know when to stop?', { after: 40 }));
    W.push(...H.lines(1));
    // Q3 remainder
    W.push(H.q(3, ['Siti had 240 stickers. She gave ' + fr(1, 4) + ' of them to Ben and ' + fr(2, 3) + ' of the REMAINDER to Ali.'], { keepNext: true }));
    W.push(H.fig(stickerBar()));
    W.push(H.sub('a', 'How many stickers did Ali get?   __________'));
    W.push(H.sub('b', 'How many stickers did Siti have left?   __________'));
    W.push(H.sub('c', 'What fraction of her 240 stickers did Siti have left?   __________'));

    // ---- page 2 ----
    W.push(H.q(4, ['Look for a pattern:&nbsp;&nbsp; ' + [[1, 2], [1, 6], [1, 12], [1, 20]].map(([a, b]) => fr(a, b)).join(' ,&nbsp; ') + ' ,&nbsp; …'], { pb: true, before: 0, keepNext: true }));
    W.push(H.sub('a', 'Write the next two fractions:   ________ ,  ________    What do you notice about the bottom numbers?', { after: 40 }));
    W.push(...H.lines(1));
    W.push(H.sub('b', 'Work out each sum. Give each answer in its simplest form.', { keepNext: true }));
    { const ws = [6600, 3300];
      const sums = [[[1, 2], [1, 6]], [[1, 2], [1, 6], [1, 12]], [[1, 2], [1, 6], [1, 12], [1, 20]]];
      W.push(H.tbl(ws, sums.map(sm => H.row([H.cell(['<div style="text-align:left;padding-left:12px">' + sm.map(([a, b]) => fr(a, b)).join(' + ') + ' &nbsp;=</div>'], ws[0], { h: 36 }), H.cell('', ws[1], { h: 36 })])))); }
    W.push(H.sub('c', ['Predict:&nbsp; ' + fr(1, 2) + ' + ' + fr(1, 6) + ' + ' + fr(1, 12) + ' + … + ' + fr(1, 90) + ' = ________&nbsp;&nbsp; Explain how you know.'], { after: 40 }));
    W.push(...H.lines(1));
    // Q5 backwards
    W.push(H.q(5, ['Ravi spent ' + fr(2, 5) + ' of his money on a game and ' + fr(1, 2) + ' of the remainder on a book. He had $36 left. Draw a model.'], { keepNext: true }));
    W.push(H.p(['<b style="color:' + TEAL + '">Start here:</b> draw 5 equal parts; the game takes 2. Cut the rest to find half of it.'], { after: 20 }));
    W.push(H.tbl([9900], [H.row([H.cell('', 9900, { h: 520 })])]));
    W.push(H.sub('a', 'How much money did Ravi have at first?   __________'));
    W.push(H.sub('b', 'How much did the book cost?   __________'));
    // Q6 digit cards
    W.push(H.q(6, ['Use the digit cards ' + [1, 2, 3, 4].map(card).join('') + ' once each in the boxes (fractions need not be proper).'], { keepNext: true }));
    W.push(H.fig('<div style="text-align:center;font-size:24px;font-weight:700">' + boxfr() + ' &nbsp;+&nbsp; ' + boxfr() + '</div>'));
    W.push(H.sub('a', 'The largest sum:   ______________________'));
    W.push(H.sub('b', 'The smallest sum:   ______________________   Did you test both ways?'));
    W.push(H.sub('c', 'The sum closest to 1:   ______________________'));
    return W;
  }
};
