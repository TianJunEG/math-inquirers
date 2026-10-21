// Math Inquirers P4 Holiday Program — Lesson 3: Operation Detectives (Four operations)
const N = '#1B2A49', Y = '#FFC93C', SKY = '#DDEBF7', TEAL = '#1F7A6F', WH = '#FFFFFF', G = '#EDEDED';
const F = 'Fredoka, Arial, sans-serif';
const tx = (x, y, s, size = 22, fill = N, anchor = 'middle', weight = 700) =>
  `<text x="${x}" y="${y}" font-size="${size}" font-weight="${weight}" text-anchor="${anchor}" fill="${fill}" font-family="${F}">${s}</text>`;

// missing-sign puzzles: numbers with empty circles between them
const signsSvg = () => {
  const rows = [['a', [7, 6, 4], 38], ['b', [48, 6, 2], 16], ['c', [9, 3, 5], 8], ['d', [12, 3, 2, 5], 14]];
  let s = `<svg aria-label="Four number sentences with empty circles for the missing signs" viewBox="0 0 600 224" width="440" xmlns="http://www.w3.org/2000/svg" style="max-width:100%">`;
  rows.forEach(([l, nums, t], i) => {
    const y = 30 + i * 54; let x = 80;
    s += tx(30, y + 8, '(' + l + ')', 20, TEAL);
    nums.forEach((n, k) => {
      s += tx(x, y + 9, n, 28); x += 52;
      if (k < nums.length - 1) { s += `<circle cx="${x}" cy="${y}" r="20" fill="${WH}" stroke="${N}" stroke-width="3"/>`; x += 52; }
    });
    s += tx(x, y + 9, '=', 28) + tx(x + 52, y + 9, t, 28);
  });
  return s + '</svg>';
};

// machine chain: ? -> x6 -> -18 -> /4 -> 30
const machineSvg = () => {
  const cells = [['?', Y], ['× 6', G], ['− 18', G], ['÷ 4', G], ['30', SKY]];
  let s = `<svg aria-label="Number machine chain: a number goes in, times 6, take away 18, divide by 4, and 30 comes out" viewBox="0 0 600 100" width="420" xmlns="http://www.w3.org/2000/svg" style="max-width:100%">`;
  cells.forEach(([t, f], i) => {
    const x = 6 + i * 120;
    s += `<rect x="${x}" y="18" width="88" height="62" rx="12" fill="${f}" stroke="${N}" stroke-width="3"/>` + tx(x + 44, 58, t, 26);
    if (i < 4) s += `<line x1="${x + 92}" y1="49" x2="${x + 112}" y2="49" stroke="${N}" stroke-width="3"/><polygon points="${x + 118},49 ${x + 108},43 ${x + 108},55" fill="${N}"/>`;
  });
  return s + '</svg>';
};

// two number chains with blanks
const chainSvg = () => {
  const rows = [['a', ['', '', '13', '21', '']], ['b', ['4', '', '', '18', '']]];
  let s = `<svg aria-label="Two number chains with missing numbers" viewBox="0 0 600 150" width="360" xmlns="http://www.w3.org/2000/svg" style="max-width:100%">`;
  rows.forEach(([l, cells], i) => {
    const y = 14 + i * 70;
    s += tx(30, y + 38, '(' + l + ')', 20, TEAL);
    cells.forEach((c, k) => {
      const x = 80 + k * 100;
      s += `<rect x="${x}" y="${y}" width="78" height="54" rx="10" fill="${c ? SKY : WH}" stroke="${N}" stroke-width="3"/>` + (c ? tx(x + 39, y + 37, c, 26) : '');
      if (k < 4) s += tx(x + 89, y + 40, ',', 26);
    });
  });
  return s + '</svg>';
};

module.exports = {
  lesson: {
    n: 3, week: 2, session: 'A', title: 'Operation Detectives', topic: 'Four operations',
    objective: 'Use the order of operations (brackets first, then multiplication and division from left to right, then addition and subtraction from left to right), find missing signs and brackets to hit a target, work backwards through a chain of operations, and solve "times as many" problems with a bar model.',
    skills: 'Order of operations, estimating then testing, guess and check, working backwards, drawing a bar model, explaining why a number trick works',
    materials: 'Mini whiteboards and markers; paper number cards 0 to 9; sign cards +, −, ×, ÷ and two pairs of bracket cards (one set per child); scrap paper for bar models.',
    online: 'Children write on mini whiteboards and hold them up to the camera. Before the lesson they cut out sign and bracket cards so they can move them on camera for the explore task.',
    warmup: 'Target Numbers: four cards 2, 4, 5 and 9. Use any of the cards once each with +, −, × and ÷ to hit each target (13, 22, 36, 81). First good way wins a point; then hunt for a second way.',
    explore: 'Pairs take the number sentence 6 + 4 × 3 − 2 and put ONE pair of brackets in different places. They work out each answer, record every different answer they find, and decide which placement gives the biggest and the smallest answer.',
    mini: 'Order of operations: 40 − 8 × 3 + 6 ÷ 2 = 40 − 24 + 3 = 19 (× and ÷ first, then left to right). Missing signs: estimate first (a big target needs ×), test, adjust: 8 × 5 − 3 = 37. Brackets to hit a target: 2 + 3 × (4 + 5) = 29. Before page 2: work backwards through a machine chain by undoing each step; a number trick (double, add 10, halve, take away your number: always 5); bar model for "4 times as many" with a total; number chains where each number is the sum of the two before.',
    share: 'Ben says 20 − 8 + 2 = 10 because you add first. Mei says the answer is 14. Who is right, and why?',
    exit: { q: 'Work out 50 − 6 × (3 + 4).', a: '8 (brackets first: 7; then 6 × 7 = 42; then 50 − 42 = 8).' },
    mistakes: [
      'Working strictly from left to right and ignoring the order: 40 − 8 × 3 done as 32 × 3.',
      'Thinking addition always comes before subtraction (or multiplication before division) instead of working left to right: 20 − 8 + 2 answered 10, 72 ÷ 8 × 3 answered 3.',
      'Working backwards but using the same operation instead of the opposite one (for − 18, taking away 18 again instead of adding 18).'
    ],
    extension: 'Use four 4s and any of +, −, ×, ÷ and brackets to make every number from 0 to 9. (For example 0 = 4 + 4 − 4 − 4, 1 = (4 + 4) ÷ (4 + 4), 2 = 4 ÷ 4 + 4 ÷ 4, 3 = (4 + 4 + 4) ÷ 4, 4 = (4 − 4) × 4 + 4, 5 = (4 × 4 + 4) ÷ 4, 6 = (4 + 4) ÷ 4 + 4, 7 = 4 + 4 − 4 ÷ 4, 8 = 4 + 4 + 4 − 4, 9 = 4 + 4 + 4 ÷ 4.)',
    key: [
      ['Q1', '(a) 106  (b) 250  (c) 27  (d) 98  (e) 12'],
      ['Q2', '(a) 7 × 6 − 4 = 38  (b) 48 ÷ 6 × 2 = 16  (c) 9 ÷ 3 + 5 = 8  (d) 12 ÷ 3 + 2 × 5 = 14. Each puzzle has only one answer.'],
      ['Q3', '(a) 41  (b) (4 + 8) × 5 − 3 = 57  (c) 4 + 8 × (5 − 3) = 20  (d) (4 + 8) × (5 − 3) = 12 × 2 = 24'],
      ['Q4', '(a) 23. Work backwards: 30 × 4 = 120, 120 + 18 = 138, 138 ÷ 6 = 23.  (b) Check: 23 × 6 = 138, 138 − 18 = 120, 120 ÷ 4 = 30.'],
      ['Q5', 'The answer is always 7 (for example 3: 15, 50, 10, 7). (a) It is always 7.  (b) Multiplying by 5 and then dividing by 5 gets you back to your number. The 35 is shared into 5 groups too, so you get your number and 7 more. Taking away your number leaves 7.'],
      ['Q6', '(a) Chicken rice: 3 units. Laksa: 1 unit. 4 units = 1 236.  (b) 1 unit = 1 236 ÷ 4 = 309. Chicken rice = 3 × 309 = 927 plates.  (c) 2 units = 618 more plates.'],
      ['Q7', '(a) 5, 8, 13, 21, 34 (21 − 13 = 8, 13 − 8 = 5, 13 + 21 = 34).  (b) 4, 7, 11, 18, 29.']
    ]
  },

  script: {
    hook: ['Welcome back, detectives! Today the clues are the signs: +, −, × and ÷, and the brackets that boss them around.', 'The same numbers can give very different answers. Our job is to find out why, and to make numbers do what we want. Notice it. Test it. Explain why.'],
    warmIntro: ['Here are four cards: 2, 4, 5 and 9. You can use each card once, with plus, minus, times or divide.', 'When a target appears, race to hit it on your whiteboard. Then look for a second way!'],
    predict: ['Look at 6 + 4 × 3 − 2. If you can put ONE pair of brackets anywhere, how many different answers do you think you can make? Write your guess in the corner of your whiteboard.'],
    exploreHints: ['Stuck: put the brackets round 6 + 4 first. What do you work out first now?', 'Not sure if you have them all: "Make a list of every place the brackets can go: round two numbers, round three numbers."', 'Finished early: can TWO pairs of brackets make a new answer?'],
    think: [
      '"40 − 8 × 3 + 6 ÷ 2. No brackets, so I look for × and ÷ first: 8 × 3 is 24 and 6 ÷ 2 is 3. Now I have 40 − 24 + 3. Only + and − are left, so I go from left to right: 16, then 19."',
      '"8, 5 and 3 must make 37. Even adding all three only makes 16, so there must be a times. 8 × 5 is 40, and 40 − 3 is 37. Let me check by doing it in the right order: 8 × 5 − 3 = 37."',
      '"21 came out of the machine. The last step was divide by 2, so I undo it: times 2 gives 42. Then undo take away 6: add 6, 48. Then undo times 4: divide by 4, 12. I check by going forwards."'
    ],
    circulate: ['Ask: "Which part do you work out first? Point to it and underline it."', 'Ask: "Is your target big or small compared with the numbers? What does that tell you?"', 'Ask: "What is the opposite of this step? How do you undo it?"'],
    hints: ['Hint 1: "Underline the part in brackets, then the × and ÷ parts. Do those first."', 'Hint 2: "Estimate first. A big target usually needs a ×. Try one sign, then test it."', 'Hint 3: "Working backwards, start at the END and undo each step: × becomes ÷, − becomes +."'],
    talk: ['"Ben says 20 − 8 + 2 = 10 because you add first. Mei says 14. Who is right?"', '"How did you know which sign to try first in the missing-sign puzzles?"'],
    talkAns: 'Mei is right. When there are only + and − (or only × and ÷), we work from left to right: 20 − 8 = 12, then 12 + 2 = 14. Ben worked out 8 + 2 first, which would need brackets: 20 − (8 + 2) = 10.',
    close: ['"Today you made the signs and brackets work for you, and you worked backwards like real detectives."', '"Hand me your exit ticket and I will stamp your inquiry journal."']
  },

  deck: {
    today: 'Use the order of operations, find missing signs and brackets to hit a target, and work backwards through number chains.',
    warmGame: 'Target Numbers. Use the cards 2, 4, 5 and 9 (each once at most) with +, −, × and ÷ to hit 13, 22, 36 and 81.',
    warmQs: [['25 × 4 = ?', '100'], ['4 800 ÷ 6 = ?', '800'], ['99 × 6 = ?', '594'], ['1 000 − 368 = ?', '632'], ['45 × 20 = ?', '900']],
    expSetup: ['Write 6 + 4 × 3 − 2 on your whiteboard and work it out.', 'Put ONE pair of brackets somewhere. Work it out again.', 'Move the brackets to other places. Write every answer.', 'How many different answers? Which is the biggest? The smallest?'],
    expPic: 'number and sign cards 6 + 4 × 3 − 2 in a row, with a pair of bracket cards waiting above them.',
    expAsk: [['How many different answers did you find?', '3 answers: 16, 28 and 10.'], ['Where do the brackets go for the biggest answer?', '(6 + 4) × 3 − 2 = 28.'], ['Why do some brackets not change the answer?', 'Brackets round 4 × 3 change nothing: × is done first anyway.']],
    mini1: { head: 'Order of operations', body: ['40 − 8 × 3 + 6 ÷ 2', '× and ÷ first: 24 and 3.', '40 − 24 + 3, left to right.'], ans: '19' },
    mini2: { head: 'Missing signs', body: ['8 ○ 5 ○ 3 = 37', '37 is big, so try ×: 8 × 5 = 40.', '40 and 3 make 37 how?'], ans: '8 × 5 − 3 = 37' },
    keyHead: 'Key idea: order matters', keyBig: 'Brackets first. Then × and ÷, then + and −, each from left to right.', keySmall: 'To hit a target: estimate, test, adjust. Working backwards: undo each step with the opposite operation.',
    brk: 'Odd or even stand-up. I read a number sentence: stand up if the answer is even, crouch if it is odd. 3 + 4 × 2, then (3 + 4) × 2, then 20 ÷ 4 + 1, then 20 ÷ (4 + 1).',
    ws1: 'Page 1, in pairs: Q1 order of operations, Q2 missing signs, Q3 brackets.',
    ws2: 'Page 2, on your own: Q4 machine chain, Q5 number trick, Q6 bar model, Q7 number chains.'
  },

  qbank: {
    core: [
      { q: 'Work out 18 + 6 × 3.', a: '36' },
      { q: 'Work out (18 + 6) × 3.', a: '72' },
      { q: 'Work out 56 ÷ 7 × 2.', a: '16' },
      { q: 'Work out 90 − 30 ÷ 5.', a: '84' },
      { q: 'Work out 2 345 × 3.', a: '7 035' },
      { q: 'Work out 4 236 ÷ 6.', a: '706' }
    ],
    stretch: [
      { q: 'Work out 120 − 4 × (18 + 7).', a: '20 (18 + 7 = 25, 4 × 25 = 100, 120 − 100 = 20).' },
      { q: 'Put ONE pair of brackets in 3 + 5 × 6 − 2 to make the answer 46.', a: '(3 + 5) × 6 − 2 = 8 × 6 − 2 = 46.' },
      { q: 'Write +, −, × or ÷ in each gap to make this true:  12 __ 4 __ 5 = 15', a: '12 ÷ 4 × 5 = 15 (the only way).' },
      { q: 'I think of a number. I multiply it by 8 and then take away 15. The answer is 425. What is my number?', a: '55 (425 + 15 = 440, 440 ÷ 8 = 55).' },
      { q: 'There are 2 340 red and blue beads. There are 4 times as many blue beads as red beads. How many red beads are there?', a: '468 (5 units = 2 340, 1 unit = 468).' },
      { q: 'In this chain, each number after the first two is the sum of the two before it. Fill in the gaps: 3, __, __, 17, __', a: '3, 7, 10, 17, 27.' },
      { q: 'A plate of noodles costs $4 and a drink costs $2. Ravi buys 3 plates of noodles and 2 drinks. Write ONE number sentence for the total cost and work it out.', a: '3 × 4 + 2 × 2 = 16, so $16.' },
      { q: 'Is 50 − 20 − 10 the same as 50 − (20 − 10)? Explain.', a: 'No. 50 − 20 − 10 = 20 (left to right), but 50 − (20 − 10) = 50 − 10 = 40.' }
    ],
    challenge: [
      { q: 'Use four 4s and any of +, −, ×, ÷ and brackets to make 5.', a: 'For example (4 × 4 + 4) ÷ 4 = 20 ÷ 4 = 5.' },
      { q: 'Start at 7. If a number is even, halve it. If it is odd, multiply it by 3 and add 1. How many steps does it take to reach 1?', a: '16 steps: 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1.' },
      { q: 'Two numbers add up to 1 000. One number is 4 times the other. What are the two numbers?', a: '200 and 800 (5 units = 1 000, 1 unit = 200).' },
      { q: 'Ali has $56 more than Ben. Together they have $300. How much money does Ben have?', a: '$122 (300 − 56 = 244, 244 ÷ 2 = 122; Ali has $178).' },
      { q: 'Use 3, 4, 5 and 6 once each, with any signs and brackets, to make 24. Find two different ways.', a: 'For example 6 × (5 − 4 + 3) = 24 and (3 + 5 − 4) × 6 = 24. Other ways are possible.' },
      { q: 'The same number goes in every box:  □ × □ − □ = 30. What is the number?', a: '6 (6 × 6 − 6 = 36 − 6 = 30). Try 5: 20, too small; try 7: 42, too big.' },
      { q: 'Put + or − in each gap so that the answer is 7:  1 __ 2 __ 3 __ 4 __ 5 __ 6 = 7. Find ALL the ways.', a: '2 ways: 1 − 2 + 3 + 4 − 5 + 6 = 7 and 1 + 2 − 3 − 4 + 5 + 6 = 7. (All + makes 21, which is 14 too many. Changing a + to a − takes that number away twice, so the numbers we change must add up to 7: 2 and 5, or 3 and 4.)' },
      { q: 'Mei spent half of her money on a book. Then she spent $6 on lunch. Then she spent half of what was left on a gift. She had $9 left. How much money did she have at first?', a: '$48. Work backwards: $9 was half of what was left, so before the gift she had $18. Before lunch: $18 + $6 = $24. That was half, so at first she had $48.' },
      { q: 'In a number chain, each number after the first two is the sum of the two before it. The 5th number is 30 and the 6th number is 49. What is the 1st number?', a: '3. Work backwards: 4th = 49 − 30 = 19, 3rd = 30 − 19 = 11, 2nd = 19 − 11 = 8, 1st = 11 − 8 = 3. The chain is 3, 8, 11, 19, 30, 49.' }
    ]
  },

  workbook: H => {
    const W = [];
    W.push(H.p('Brackets first. Then × and ÷, working from left to right. Then + and −, working from left to right.', { after: 80 }));
    W.push(H.q(1, 'Work out. Underline the part you do first.', { before: 40, keepNext: true }));
    W.push(H.sub('a', '36 + 14 × 5  =  ____________'));
    W.push(H.sub('b', '(36 + 14) × 5  =  ____________'));
    W.push(H.sub('c', '72 ÷ 8 × 3  =  ____________'));
    W.push(H.sub('d', '100 − 45 ÷ 5 + 7  =  ____________'));
    W.push(H.sub('e', '6 × (25 − 17) ÷ 4  =  ____________'));
    W.push(H.q(2, 'Missing signs. Write +, −, × or ÷ in each circle to make the number sentence true. You may use a sign more than once.', { keepNext: true }));
    W.push(H.fig(signsSvg()));
    W.push(H.q(3, 'Brackets change the answer. Look at  4 + 8 × 5 − 3', { keepNext: true }));
    W.push(H.sub('a', 'With no brackets:   4 + 8 × 5 − 3  =  ________'));
    W.push(H.sub('b', 'Put in ONE pair of brackets to make 57:     4  +  8  ×  5  −  3  =  57'));
    W.push(H.sub('c', 'Put in ONE pair of brackets to make 20:     4  +  8  ×  5  −  3  =  20'));
    W.push(H.sub('d', 'Mei used TWO pairs of brackets and made 24. Show where she put them:     4  +  8  ×  5  −  3  =  24'));

    W.push(H.q(4, 'A number goes into this machine chain. 30 comes out.', { pb: true, before: 0, keepNext: true }));
    W.push(H.fig(machineSvg()));
    W.push(H.sub('a', ['Work backwards. What number went in?  ________      <b style="color:#1F7A6F">b</b>  Check it going forwards.']));
    W.push(H.q(5, 'Number trick. Think of a number. Multiply it by 5. Add 35. Divide by 5. Take away the number you started with. Try it with two different numbers.', { keepNext: true }));
    { const ws = [1980, 1980, 1980, 1980, 1980];
      W.push(H.tbl(ws, [H.row(['My number', '× 5', '+ 35', '÷ 5', '− my number'].map((s, i) => H.cell(s, ws[i], { bold: true, fill: 'EDEDED' }))),
        ...[0, 1].map(() => H.row(ws.map(w => H.cell('', w, { h: 55 }))))])); }
    W.push(H.sub('a', 'What do you notice?  ______________________________'));
    W.push(H.sub('b', 'Explain why it works. A bar model can help.'));
    W.push(...H.lines(1));
    W.push(H.q(6, 'A hawker stall sold 3 times as many plates of chicken rice as plates of laksa. It sold 1 236 plates altogether.', { keepNext: true }));
    W.push(H.sub('a', 'Draw a bar model.'));
    W.push(H.gap(240));
    W.push(H.sub('b', 'How many plates of chicken rice did it sell?'));
    W.push(H.ans());
    W.push(H.sub('c', 'How many more plates of chicken rice than laksa did it sell?'));
    W.push(H.ans());
    W.push(H.q(7, 'Number chains. After the first two numbers, each number is the sum of the two numbers before it. Example: 2, 5, 7, 12, 19. Fill in the missing numbers.', { keepNext: true }));
    W.push(H.fig(chainSvg()));
    W.push(H.sub('a', ['Chain (a): work backwards from 13 and 21.     <b style="color:#1F7A6F">b</b>  Chain (b): guess the 2nd number, then check.']));
    return W;
  }
};
