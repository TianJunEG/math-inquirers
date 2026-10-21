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
  return `<svg aria-label="A bar for 240 stickers cut into 4 equal parts; the first part is for Ben" viewBox="0 0 600 126" width="600" xmlns="http://www.w3.org/2000/svg" style="max-width:80%">${g}</svg>`;
};

module.exports = {
  lesson: {
    n: 2, week: 1, session: 'B', title: 'Fraction Feats', topic: 'Fractions: Four Operations',
    objective: 'Link fractions and division (3 ÷ 4 = 3/4) and divide a proper fraction by a whole number; write fractions as the sum of two different unit fractions by testing in order; solve fraction-of-a-remainder problems forwards and backwards with a bar model; and spot and explain patterns in fraction sums.',
    skills: 'Fraction and division, drawing a model (bar, pizza), testing in order and knowing when to stop, fraction of a remainder, working backwards, looking for a pattern, testing both ways',
    materials: 'Paper circles (6 per child) to cut as pizzas, scissors, a strip of paper for bar models, digit cards 1 to 4, mini whiteboard, workbook.',
    online: 'Children cut out six paper circles before the lesson and fold or cut them on camera. The tutor shares the slides and draws the bar models live. Pairs work in breakout rooms for the explore and page 1.',
    warmup: 'Fraction Face-off: two fractions appear; children hold up 1 finger if the first is bigger and 2 if the second is, then give a reason without finding common denominators. Then five quick questions on whiteboards.',
    explore: 'Pizza sharing: pairs share 3 pizzas equally among 4 friends, then 5 pizzas among 6 friends, with paper circles. How much does each friend get? Can you cut so that each friend gets only 2 pieces?',
    mini: 'a ÷ b = a/b: 3 pizzas among 4 friends gives 3/4 each; a proper fraction ÷ a whole number cuts each part again (3/5 ÷ 2 = 3/10). Unit fractions: try 1/2, 1/3, 1/4 … in order, take it away and check whether what is left is a unit fraction; stop once the first part is less than half of the fraction. Fraction of a remainder: find the remainder first, then take the fraction of the remainder, with a bar model cut into equal small units. Before page 2: a pattern in fraction sums (1 take away the last piece), working backwards with a model, and testing both ways with digit cards.',
    share: 'Ben says 1/2 + 1/3 = 2/5 because you add the tops and add the bottoms. Use a pizza picture to show why he is wrong.',
    exit: { q: '(a) 4 pizzas are shared equally among 5 children. How much does each child get?  (b) Ali had 60 marbles. He gave 1/3 of them to Mei and 1/2 of the remainder to Ben. How many marbles did Ali have left?', a: '(a) 4/5 of a pizza  (b) 20 marbles (60 − 20 = 40 left, then half of 40 is given away)' },
    mistakes: [
      'Taking the second fraction of the whole amount instead of the remainder (2/3 of 240 instead of 2/3 of 180).',
      'Adding tops and bottoms: 1/2 + 1/3 = 2/5, or using the same unit fraction twice when the question asks for different ones.',
      'Writing 3 ÷ 4 as 4/3, or multiplying instead of dividing when a fraction is shared (3/4 ÷ 6 written as 18/4 instead of 1/8).'
    ],
    extension: 'Write 1 as the sum of three different unit fractions. Is there more than one way? (Only one: 1/2 + 1/3 + 1/6.)',
    key: [
      ['Q1', '(a) 5/8  (b) 9/4 = 2 1/4 m  (c) 1/8  (d) Group A. 3/4 = 21/28 and 5/7 = 20/28. (Or: each child in A is 1/4 short of a whole pizza, in B 2/7 short, and 2/7 is more than 1/4.)'],
      ['Q2', '(a) 1/2 + 1/5  (b) 1/4 + 1/5  (c) 1/3 + 1/24 and 1/4 + 1/8. (1/5 leaves 7/40, not a unit fraction; after that the first part is less than half of 3/8, so stop.)'],
      ['Q3', '(a) 120  (b) 60  (c) 1/4. Ben 60, remainder 180, Ali 2/3 of 180 = 120, left 60 = 1/4 of 240.'],
      ['Q4', '(a) 1/30, 1/42. The bottom numbers are 1 × 2, 2 × 3, 3 × 4, 4 × 5, …  (b) 2/3, 3/4, 4/5  (c) 9/10. 1/90 is the 9th term (9 × 10), and each sum is 1 take away the next unit fraction.'],
      ['Q5', '(a) $120  (b) $36. Model: 10 equal units; game 4, book 3, left 3 units = $36, so 1 unit = $12.'],
      ['Q6', '(a) 4/1 + 3/2 = 5 1/2  (b) 1/3 + 2/4 = 5/6 (1/4 + 2/3 = 11/12 is bigger, so test both ways)  (c) 1/4 + 2/3 = 11/12, only 1/12 away from 1']
    ]
  },

  script: {
    hook: ['Welcome back, inquirers! Today is pizza day: we share pizzas fairly, cut them in clever ways and find out what the Ancient Egyptians knew about fractions.', 'Notice it, test it, explain why: by the end you will solve fraction puzzles that trip up grown-ups.'],
    warmIntro: ['Fraction Face-off! Two fractions appear. One finger if the first is bigger, two fingers if the second is bigger.', 'No common denominators allowed. Give me a reason: same top? Close to 1? More than a whole?'],
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
    warmGame: 'Fraction Face-off. Two fractions appear. Hold up 1 finger if the first is bigger, 2 if the second is. Give a reason without common denominators: 3/5 or 3/7, 5/6 or 6/7, 4/9 or 1/2, 7/8 or 8/7.',
    warmQs: [['3 ÷ 4 as a fraction', '3/4'], ['2/3 + 1/6', '5/6'], ['3/4 of 20', '15'], ['2/5 × 3/4', '3/10'], ['4/5 ÷ 2', '2/5']],
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
      { q: 'Write 7 ÷ 9 as a fraction.', a: '7/9' },
      { q: 'Work out 2/3 + 3/4.', a: '17/12 = 1 5/12' },
      { q: 'Work out 5/6 − 1/4.', a: '7/12' },
      { q: 'Find 3/5 of 15.', a: '9' },
      { q: 'Work out 2/3 × 9/10.', a: '3/5' },
      { q: 'Work out 6/7 ÷ 3.', a: '2/7' }
    ],
    stretch: [
      { q: 'Write 2/3 as the sum of two different unit fractions.', a: '1/2 + 1/6 (the only way).' },
      { q: 'Ben ate 1/3 of a pizza. Ali ate 1/4 of what was left. What fraction of the pizza is left?', a: '1/2. 2/3 was left after Ben; Ali ate 1/4 of it, so 3/4 of 2/3 = 1/2 is left.' },
      { q: '1/2 − 1/3 = 1/6 and 1/3 − 1/4 = 1/12. Use the pattern to work out 1/4 − 1/5 and 1/9 − 1/10.', a: '1/20 and 1/90 (the bottom numbers multiply: 4 × 5 and 9 × 10).' },
      { q: '4 litres of juice are poured equally into 6 bottles. How much juice is in each bottle?', a: '4/6 = 2/3 of a litre.' },
      { q: 'Which is bigger, 5/6 or 6/7? Explain without finding common denominators.', a: '6/7. 5/6 is 1/6 short of 1 and 6/7 is only 1/7 short of 1, and 1/7 is smaller than 1/6.' },
      { q: 'A rope 3/4 m long is cut into 3 equal pieces. How long is each piece?', a: '1/4 m (3/4 ÷ 3).' },
      { q: 'Find a fraction between 1/3 and 1/2 with 12 as the bottom number.', a: '5/12 (1/3 = 4/12 and 1/2 = 6/12).' },
      { q: 'Half of a number is 15. What is 2/5 of the number?', a: '12. The number is 30, and 2/5 of 30 = 12.' }
    ],
    challenge: [
      { q: 'Write 1 as the sum of three different unit fractions. Find all the ways.', a: 'Only one way: 1/2 + 1/3 + 1/6. (The biggest part must be 1/2, and then 1/2 = 1/3 + 1/6 is the only split into two different unit fractions.)' },
      { q: 'Work out 1/2 × 2/3 × 3/4 × 4/5 × … × 99/100.', a: '1/100. Each top number cancels the bottom number before it, leaving 1 on top and 100 at the bottom.' },
      { q: 'Mrs Tan baked some cookies. She gave 1/2 of them to her neighbours, 1/3 of the remainder to Ben and 1/4 of what was then left to Mei. She had 30 cookies left. How many did she bake?', a: '120. What is left is 1/2 × 2/3 × 3/4 = 1/4 of the cookies, and 1/4 is 30.' },
      { q: 'Which is more: 2/3 of 3/4 of a cake, or 3/4 of 2/3 of a cake?', a: 'They are the same: both are 1/2 of the cake (2/3 × 3/4 = 3/4 × 2/3 = 6/12).' },
      { q: 'Use the digit cards 1, 3, 5 and 7 once each to make two fractions. Take the smaller from the bigger. What is the smallest difference you can make (more than 0)?', a: '8/35, from 3/7 − 1/5 (15/35 − 7/35).' },
      { q: 'Mei spent 1/4 of her money on Monday and 1/3 of the remainder on Tuesday. She had $50 left. How much did she spend each day?', a: '$25 each day. 1/3 of the remaining 3/4 is 1/4, so she spent 1/4 each day and 1/2 is left. 1/2 = $50, so she had $100.' },
      { q: 'Work out 1/6 + 1/12 + 1/20 + 1/30 + 1/42 without finding a common denominator for all five. (Hint: 1/6 = 1/2 − 1/3.)', a: '5/14. Each fraction is a difference: (1/2 − 1/3) + (1/3 − 1/4) + (1/4 − 1/5) + (1/5 − 1/6) + (1/6 − 1/7). The middle parts cancel, leaving 1/2 − 1/7 = 5/14.' },
      { q: '5 pizzas are shared equally among 12 children. Each child must get exactly 2 pieces, and each piece must be a unit fraction of a pizza (like 1/3 or 1/4). How can the pizzas be cut?', a: 'Each child gets 5/12. Two ways: 1/3 + 1/12 (cut 4 pizzas into thirds and 1 pizza into twelfths), or 1/4 + 1/6 (cut 3 pizzas into quarters and 2 pizzas into sixths).' },
      { q: 'A tank is full of water. 1/3 of the water is let out. Then 1/3 of the water left is let out, and then 1/3 of the water left again. Now 16 litres are left. How much water was in the full tank?', a: '54 litres. Each time 2/3 is left: 54 → 36 → 24 → 16.' }
    ]
  },

  workbook: H => {
    const W = [];
    // Q1 sharing
    W.push(H.q(1, 'Sharing. Remember: a ÷ b = a/b.', { before: 20, keepNext: true }));
    W.push(H.sub('a', '5 pizzas are shared equally among 8 children. Each gets  ______  of a pizza.'));
    W.push(H.sub('b', 'A 9 m ribbon is cut into 4 equal pieces. Each piece is  ______  m long.'));
    W.push(H.sub('c', ['3/4 of a cake is shared equally among 6 children. Each gets  ______  of the whole cake.'.replace('3/4', fr(3, 4))]));
    W.push(H.sub('d', 'Group A shares 3 pizzas among 4 children. Group B shares 5 pizzas among 7 children. In which group does each child get more? Explain.', { after: 40 }));
    W.push(...H.lines(1));
    // Q2 unit fractions
    W.push(H.q(2, 'Write each fraction as the sum of two DIFFERENT unit fractions (1 on top).', { keepNext: true }));
    W.push(H.sub('a', [fr(7, 10) + '&nbsp; = &nbsp;' + ufr() + '&nbsp; + &nbsp;' + ufr() + '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>(b)</b>&nbsp;&nbsp; ' + fr(9, 20) + '&nbsp; = &nbsp;' + ufr() + '&nbsp; + &nbsp;' + ufr()]));
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
      W.push(H.tbl(ws, sums.map(sm => H.row([H.cell(['<div style="text-align:left;padding-left:12px">' + sm.map(([a, b]) => fr(a, b)).join(' + ') + ' &nbsp;=</div>'], ws[0], { h: 50 }), H.cell('', ws[1], { h: 50 })])))); }
    W.push(H.sub('c', ['Predict:&nbsp; ' + fr(1, 2) + ' + ' + fr(1, 6) + ' + ' + fr(1, 12) + ' + … + ' + fr(1, 90) + ' = ________&nbsp;&nbsp; Explain how you know.'], { after: 40 }));
    W.push(...H.lines(1));
    // Q5 backwards
    W.push(H.q(5, ['Ravi spent ' + fr(2, 5) + ' of his money on a game and ' + fr(1, 2) + ' of the remainder on a book. He had $36 left. Draw a model.'], { keepNext: true }));
    W.push(H.tbl([9900], [H.row([H.cell('', 9900, { h: 760 })])]));
    W.push(H.sub('a', 'How much money did Ravi have at first?   __________'));
    W.push(H.sub('b', 'How much did the book cost?   __________'));
    // Q6 digit cards
    W.push(H.q(6, ['Use the digit cards ' + [1, 2, 3, 4].map(card).join('') + ' once each to fill the boxes. The fractions do not have to be proper.'], { keepNext: true }));
    W.push(H.fig('<div style="text-align:center;font-size:24px;font-weight:700">' + boxfr() + ' &nbsp;+&nbsp; ' + boxfr() + '</div>'));
    W.push(H.sub('a', 'The largest sum:   ______________________'));
    W.push(H.sub('b', 'The smallest sum:   ______________________   Did you test both ways?'));
    W.push(H.sub('c', 'The sum closest to 1:   ______________________'));
    return W;
  }
};
