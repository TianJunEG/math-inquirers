// Math Inquirers P3, Lesson 3: Times Table Treasure (tables of 6, 7, 8 and 9)
// Heuristics taught: look for a pattern; make a systematic list (and use facts you know to split an array).

// ---------- small SVG helpers for the workbook (viewBox about 600 wide) ----------
const NAVY = '#1B2A49', YEL = '#FFC93C', SKY = '#DDEBF7', TEAL = '#1F7A6F';
const txt = (x, y, s, o = {}) => `<text x="${x}" y="${y}" font-size="${o.size || 16}" font-weight="${o.w || 700}" text-anchor="${o.a || 'middle'}" fill="${o.fill || NAVY}" font-family="Arial">${s}</text>`;

// 7 rows of 8 dots, split after row 5
const arraySvg = () => {
  const rows = 7, cols = 8, gx = 34, gy = 30, x0 = 120, y0 = 30;
  let s = `<svg aria-label="An array of 7 rows of 8 dots split into 5 rows and 2 rows" viewBox="0 0 600 260" xmlns="http://www.w3.org/2000/svg" style="width:440px;max-width:100%">`;
  for (let r = 0; r < rows; r++) for (let c = 0; c < cols; c++) {
    const y = y0 + r * gy + (r >= 5 ? 18 : 0);
    s += `<circle cx="${x0 + c * gx}" cy="${y}" r="11" fill="${r < 5 ? YEL : SKY}" stroke="${NAVY}" stroke-width="2"/>`;
  }
  const yl = y0 + 4 * gy + 24;
  s += `<line x1="${x0 - 30}" y1="${yl}" x2="${x0 + 7 * gx + 30}" y2="${yl}" stroke="#D64545" stroke-width="3" stroke-dasharray="8 6"/>`;
  // brackets on the right
  const bx = x0 + 7 * gx + 40;
  const br = (ya, yb, label) => `<path d="M${bx} ${ya} h12 V${yb} h-12" fill="none" stroke="${NAVY}" stroke-width="2.5"/>` + txt(bx + 24, (ya + yb) / 2 + 6, label, { a: 'start', size: 17 });
  s += br(y0 - 12, y0 + 4 * gy + 12, '5 rows of 8');
  s += br(y0 + 5 * gy + 6, y0 + 6 * gy + 30, '2 rows of 8');
  s += txt(40, y0 + 2 * gy + 6, '7 rows', { size: 16, fill: TEAL });
  return s + '</svg>';
};

module.exports = {
  lesson: {
    n: 3, week: 2, session: 'A', title: 'Times Table Treasure', topic: 'Tables of 6, 7, 8 and 9',
    objective: 'Find and explain patterns in the 6, 7, 8 and 9 times tables, use last-digit patterns, split an array into facts we know, and solve grid and list puzzles in a careful order.',
    skills: 'Look for a pattern, make a systematic list, use known facts, explain why',
    materials: 'Multiplication square (1 to 10), dot paper, coloured pencils, a ruler, mini whiteboards.',
    online: 'Tutor draws on a shared digit-circle slide. Each child draws 10 dots round a circle (like a clock) labelled 0 to 9, and has dot paper and coloured pencils.',
    warmup: 'Buzz! Count round the group from 1 to 70. Say "Buzz" instead of any number in the 7 times table. Play again with 6s (to 60), then 8s (to 80).',
    explore: 'Last-digit circles. Pairs draw 10 dots round a circle labelled 0 to 9. For the 6 times table they join the last digits in order (6, 2, 8, 4, 0, back to 6). Then they try the 4s and the 8s. Which tables make the same shape? Why does the 6s shape never touch an odd digit?',
    mini: 'Look for a pattern: in the 8 times table the last digits go 8, 6, 4, 2, 0 and repeat, so only the ones digit decides the last digit (8 × 23 ends like 8 × 3). Then split an array into two facts we know: 6 × 8 = 5 × 8 + 1 × 8, and 9 × 7 = 10 × 7 − 7.',
    share: 'Why is every answer in the 6 times table even, but the 7 times table has odd and even answers?',
    exit: { q: 'What is the last digit of 6 × 47? Explain how you know without working out 6 × 47.', a: '2. Only 6 × 7 = 42 decides the last digit, because 6 × 40 ends in 0. (6 × 47 = 282.)' },
    mistakes: [
      'Checking the 9s table only by "the digits add up to 9" (81 passes that test, but 9 × 8 is 72).',
      'Splitting an array and then giving one part as the answer (writing 40 for 7 × 8 instead of 40 + 16).',
      'Missing or repeating ways in a list because the rows are not tried in order 2, 3, 4, 5 …'
    ],
    extension: 'Draw last-digit circles for all the tables from 1 to 9 and group the tables that make the same shape. Explain why 1 and 9, 2 and 8, 3 and 7, 4 and 6 pair up.',
    key: [
      ['Q1', '(a) 9, 18, 27, 36, 45, 54, 63, 72, 81, 90  (b) The tens digit goes up by 1 and the ones digit goes down by 1; the two digits add up to 9; the tens digit is 1 less than the number of nines.  (c) In 9 × 8 the tens digit is 1 less than 8, so it is 7, and 7 + 2 = 9, so 9 × 8 = 72. 81 is 9 × 9.'],
      ['Q2', '(a) Answers 7, 14, 21, 28, 35, 42, 49, 56, 63, 70; last digits 7, 4, 1, 8, 5, 2, 9, 6, 3, 0  (b) All ten digits 0 to 9, each once  (c) 3 and 9 (the 3s: 3, 6, 9, 2, 5, 8, 1, 4, 7, 0; the 9s: 9, 8, 7 … 0). Tables 2, 4, 6, 8 give only even last digits; the 5s give only 5 and 0.  (d) 2, because 7 × 6 = 42 (7 × 46 = 322).'],
      ['Q3', '(a) 5 × 8 = 40, 2 × 8 = 16, so 7 × 8 = 56  (b) For example 5 × 6 + 4 × 6 = 30 + 24 = 54, or 10 × 6 − 6 = 54.'],
      ['Q4', 'Rows 7, 9, 6. Columns 8, 6, 9. Row 7: 56, 42, 63. Row 9: 72, 54, 81. Row 6: 48, 36, 54. (Start with 81 = 9 × 9.)'],
      ['Q5', '(a) 2 rows of 18, 3 of 12, 4 of 9, 6 of 6, 9 of 4, 12 of 3, 18 of 2  (b) 7 ways  (c) 6 rows of 6: turned round it is the same, so it has no partner. That is why the number of ways is odd.'],
      ['Q6', '(a) 24, 48, 72, 96  (b) 48 (digit sums: 24 → 6, 48 → 12, 72 → 9, 96 → 15)']
    ]
  },

  script: {
    hook: ['Today we are treasure hunters inside the times tables. The 6, 7, 8 and 9 tables are full of hidden patterns. If you can spot a pattern, you can use it to check answers and to find answers you have never learnt.'],
    warmIntro: ['We are going to count round the group. When it is a number in the 7 times table, do not say it. Say "Buzz!" instead.', 'Which numbers did we Buzz? What do you notice about them?'],
    predict: ['Here is a circle with the digits 0 to 9, like a clock. I write the 6 times table and look only at the last digit: 6, 12, 18 … the last digits are 6, 2, 8. If I join those dots in order, what shape do you think we will get? Will it ever touch an odd digit?'],
    exploreHints: [
      'Stuck: write the table down the side of your page first, then circle the last digit of each answer.',
      'Confused: "Look only at the ones digit. 6 × 3 = 18, so we join to the 8."',
      'Finished early: try the 7s. How many dots does it touch? Try the 3s and compare.'
    ],
    think: [
      '"Look at the 8 times table: 8, 16, 24, 32, 40, 48 … The last digits go 8, 6, 4, 2, 0, then 8, 6, 4, 2, 0 again. So the pattern repeats every 5."',
      '"What is the last digit of 8 × 23? 8 × 20 ends in 0, so only 8 × 3 matters. 8 × 3 = 24, so 8 × 23 ends in 4. Check: 8 × 23 = 184. Yes."',
      '"I do not know 6 × 8 by heart? I split the array: 5 rows of 8 is 40, one more row of 8 is 8, so 6 × 8 = 48. For 9 × 7 I can do 10 sevens, which is 70, and take one 7 away: 63."'
    ],
    circulate: [
      'Ask: "What pattern do you notice? Does it work every time? Test one more."',
      'Ask: "Which facts do you already know that could help you?"',
      'Ask: "How do you know you have found every way? What order did you go in?"'
    ],
    hints: [
      'Hint 1: "Write the table in order and look at the ones digits only."',
      'Hint 2: "Split the big fact into two smaller facts you know, then add."',
      'Hint 3: "For a grid puzzle, start with a number that can only be made in one way, like 81 or 49."'
    ],
    talk: ['"Why is every answer in the 6 times table even?"', '"Why does the 7 times table have odd and even answers?"'],
    talkAns: '6 groups can always be put into 3 pairs of groups, so nothing is left over: the answer is even. With 7 groups one group has no partner, so when each group is odd the answer is odd.',
    close: ['"You found patterns, tested them and explained why they work. That is exactly what mathematicians do."']
  },

  deck: {
    today: 'Find hidden patterns in the 6, 7, 8 and 9 times tables, use them to check answers, and solve times-table puzzles in order.',
    warmGame: 'Buzz! Count round the group from 1. Say "Buzz" instead of any number in the 7 times table. Then play with 6s and 8s.',
    warmQs: [['6 × 7 = ?', '42'], ['9 × 9 = ?', '81'], ['8 × ? = 64', '8'], ['Which is bigger: 6 × 8 or 7 × 7?', '7 × 7 = 49 is 1 more than 6 × 8 = 48']],
    expSetup: ['Draw 10 dots round a circle. Label them 0 to 9, like a clock.', 'Write the 6 times table. Circle the last digit of each answer.', 'Join the last digits in order: 6 → 2 → 8 → 4 → 0 → back to 6.', 'Now do the same for the 4s and the 8s. Compare the shapes.'],
    expPic: 'a circle of 10 dots labelled 0 to 9 with a star joining 6, 2, 8, 4, 0.',
    expAsk: [
      ['Which tables made the same shape?', 'The 4s and the 6s make the same star (going round opposite ways). The 2s and the 8s make the same shape.'],
      ['Why does the 6s shape never touch an odd digit?', 'Every answer in the 6 times table is even: 6 groups can be put into 3 pairs of groups.'],
      ['Which table do you think makes the same shape as the 3s?', 'The 7s, because 3 + 7 = 10, just like 4 + 6 and 2 + 8.']
    ],
    mini1: { head: 'Last digits repeat', body: ['The 8 times table ends in 8, 6, 4, 2, 0 and then repeats.', 'What is the last digit of 8 × 23?', '8 × 20 ends in 0, so only 8 × 3 = 24 matters.'], ans: '4 (8 × 23 = 184).' },
    mini2: { head: 'Split the array', body: ['9 × 7: split 9 rows of 7 into 5 rows and 4 rows.', '5 × 7 = 35 and 4 × 7 = 28.', 'Or: 10 × 7 = 70, take away one 7.'], ans: '63.' },
    keyHead: 'Key idea: look for a pattern',
    keyBig: 'Look for a pattern and test it. Use facts you know to find facts you do not know.',
    keySmall: 'When there are many answers, make a list in order so none are missed.',
    brk: 'Times-table jumps. Tutor calls a fact like 6 × 3: children do that many star jumps in groups of 6, counting 6, 12, 18 aloud.',
    ws1: 'Page 1, in pairs: Q1 patterns in the 9s, Q2 last digits of the 7s, Q3 split an array.',
    ws2: 'Page 2, on your own: Q4 grid puzzle, Q5 every way to arrange 36 chairs, Q6 number riddle.'
  },

  qbank: {
    core: [
      { q: 'Find 8 × 6 and 6 × 8. What do you notice?', a: 'Both are 48. Swapping the numbers does not change the answer.' },
      { q: 'You know 5 × 9 = 45. Use it to find 6 × 9.', a: '54 (one more 9: 45 + 9).' },
      { q: 'Fill in the box: 7 × □ = 63', a: '9' },
      { q: 'A spider has 8 legs. How many legs do 7 spiders have?', a: '56' },
      { q: 'Write the last digits of the 6 times table from 6 × 1 to 6 × 10. Which digits appear?', a: '6, 2, 8, 4, 0, 6, 2, 8, 4, 0. Only 6, 2, 8, 4 and 0.' },
      { q: 'Find 9 × 7 by working out 10 × 7 and taking away one 7.', a: '70 − 7 = 63' }
    ],
    stretch: [
      { q: 'The digits of every answer in the 9 times table (9 × 1 to 9 × 10) add up to 9. Which of these are in the 9 times table: 54, 65, 72, 83?', a: '54 and 72 (5 + 4 = 9 and 7 + 2 = 9; 6 + 5 and 8 + 3 make 11). 54 = 9 × 6, 72 = 9 × 8.' },
      { q: 'What is the last digit of 8 × 8 × 8? Use last digits only.', a: '2. 8 × 8 = 64 ends in 4, and 4 × 8 = 32 ends in 2. (8 × 8 × 8 = 512.)' },
      { q: 'Ravi says: "Every answer in the 6 times table is even." Is he right? Explain why.', a: 'Yes. 6 groups can always be put into 3 pairs of groups, so nothing is left over. (6 × 7 = 3 × 14 = 42.)' },
      { q: 'Find ALL the 2-digit numbers that can be divided exactly by 7 and whose digits add up to 10.', a: '28 and 91. (List 14, 21, 28 … 98 and add the digits of each: only 28 and 91 make 10.)' },
      { q: 'Which is more, 7 × 8 or 6 × 9? By how much?', a: '7 × 8 = 56 is 2 more than 6 × 9 = 54.' },
      { q: 'The last digit of 9 × 9 is 1. What is the last digit of 9 × 9 × 9 × 9?', a: '1. Last digits go 9, 1, 9, 1. (9 × 9 × 9 × 9 = 6561.)' },
      { q: 'Ben multiplies a number by 6. His answer ends in 4. What could the last digit of his number be? Find all the possible digits.', a: '4 or 9 (6 × 4 = 24 and 6 × 9 = 54; no other digit gives a last digit of 4).' },
      { q: 'Mei’s age × 6 = 48. Ali’s age × 7 = 63. Who is older, and by how many years?', a: 'Mei is 8, Ali is 9, so Ali is older by 1 year.' }
    ],
    challenge: [
      { q: 'Four numbers in a multiplication square are 42 and 48 in the top row, and 49 and 56 in the row below. What are the two row numbers and the two column numbers?', a: 'Rows 6 and 7, columns 7 and 8. Start with 49: it can only be 7 × 7.' },
      { q: 'Ben writes the answers of the 6 times table from 6 × 1 to 6 × 20. How many of the answers end in 8?', a: '4 (18, 48, 78, 108). The last digits 6, 2, 8, 4, 0 repeat every 5, so 8 comes once in every 5.' },
      { q: 'How many numbers from 1 to 200 can be divided exactly by both 6 and 9?', a: '11. They are the numbers in the 18 times table: 18, 36, 54 … 198.' },
      { q: 'Siti writes the 7 times table from 7 × 1 to 7 × 20. How many answers end in 3?', a: '2 (63 and 133). Each digit appears once in every 10 answers.' },
      { q: 'Siti says the answer to 6 × 7 × 8 × 9 ends in 4. Is she right? Use last digits only.', a: 'Yes. 6 × 7 = 42 → 2; 2 × 8 = 16 → 6; 6 × 9 = 54 → 4. (The answer is 3024.)' },
      { q: 'Mei multiplies two DIFFERENT numbers from 6, 7, 8 and 9. Find all the answers she can get.', a: '6 answers: 42, 48, 54, 56, 63, 72 (6×7, 6×8, 6×9, 7×8, 7×9, 8×9).' },
      { q: 'Mei has between 40 and 60 sweets. She can share them equally among 6 friends with none left over. She can also share them equally among 9 friends with none left over. How many sweets does she have?', a: '54. Numbers that work for 6 and 9 are 18, 36, 54, 72 …; only 54 is between 40 and 60.' },
      { q: 'Ben keeps multiplying by 7: 7, 49, 343 … He writes only the last digit each time: 7, 9, 3 … What is the last digit when he has multiplied 8 sevens together? Explain the pattern.', a: '1. The last digits go 7, 9, 3, 1 and then repeat, so the 4th and the 8th are both 1.' },
      { q: 'I am a 3-digit number less than 200. I can be divided exactly by 7 and by 9. My digits add up to 9. What number am I?', a: '126. Numbers that work for 7 and 9 are 63, 126, 189 …; the 3-digit ones below 200 are 126 and 189, and only 1 + 2 + 6 = 9.' }
    ]
  },

  workbook: H => {
    const out = [];
    const C = (s, w, o) => H.cell(s, w, o);
    out.push(H.p('Look for a pattern and test it. Use facts you know to find facts you do not know.', { after: 80 }));
    // Q1
    out.push(H.q(1, 'Patterns in the 9 times table.', { before: 100, keepNext: true }));
    out.push(H.sub('a', 'Fill in the answers.', { keepNext: true }));
    { const ws = [1400, 850, 850, 850, 850, 850, 850, 850, 850, 850, 850];
      out.push(H.tbl(ws, [
        H.row([C('9 ×', ws[0], { bold: true, fill: 'D9D9D9' }), ...Array.from({ length: 10 }, (_, i) => C(String(i + 1), 850, { bold: true, fill: 'EDEDED' }))]),
        H.row([C('Answer', ws[0], { bold: true, fill: 'EDEDED' }), C('9', 850), C('18', 850), ...Array.from({ length: 8 }, () => C('', 850, { h: 150 }))])
      ])); }
    out.push(H.sub('b', 'Look at the tens digits and the ones digits. Write TWO patterns you notice.'));
    out.push(...H.lines(2));
    out.push(H.sub('c', 'Ali says 9 × 8 = 81, because 8 + 1 = 9. Use a pattern to explain why he is wrong.'));
    out.push(...H.lines(2));
    // Q2
    out.push(H.q(2, 'Last digits in the 7 times table.', { keepNext: true }));
    out.push(H.sub('a', 'Fill in the answers and their last digits.', { keepNext: true }));
    { const ws = [1400, 850, 850, 850, 850, 850, 850, 850, 850, 850, 850];
      out.push(H.tbl(ws, [
        H.row([C('7 ×', ws[0], { bold: true, fill: 'D9D9D9' }), ...Array.from({ length: 10 }, (_, i) => C(String(i + 1), 850, { bold: true, fill: 'EDEDED' }))]),
        H.row([C('Answer', ws[0], { bold: true, fill: 'EDEDED' }), C('7', 850), C('14', 850), ...Array.from({ length: 8 }, () => C('', 850, { h: 130 }))]),
        H.row([C('Last digit', ws[0], { bold: true, fill: 'EDEDED' }), C('7', 850), C('4', 850), ...Array.from({ length: 8 }, () => C('', 850, { h: 130 }))])
      ])); }
    out.push(H.sub('b', 'Which of the digits 0 to 9 appear as a last digit?   ______________________'));
    out.push(H.sub('c', 'Find ALL the other times tables from 2 to 9 whose last digits use all ten digits 0 to 9.   ____________'));
    out.push(H.sub('d', 'Without working out 7 × 46, what is its last digit? Explain.'));
    out.push(...H.lines(1));
    // Q3
    out.push(H.q(3, 'Mei does not know 7 × 8. She splits the array of 7 rows of 8 dots into two parts.', { keepNext: true }));
    out.push(H.fig(arraySvg()));
    out.push(H.sub('a', '5 × 8 = ______      2 × 8 = ______      so  7 × 8 = ______'));
    out.push(H.sub('b', 'Split 9 × 6 into two facts you know. Show your working.'));
    out.push(...H.lines(2));
    // ---------- page 2 ----------
    out.push(H.q(4, 'Grid puzzle. Each number in the grid is the row number × the column number. The row and column numbers are all from 1 to 10. Find the six missing row and column numbers, then fill in the grid.', { pb: true, before: 0, keepNext: true }));
    { const ws = [2475, 2475, 2475, 2475];
      const hd = s => C(s, 2475, { bold: true, fill: 'D9D9D9', h: 150, size: 26 });
      const v = s => C(s, 2475, { bold: true, h: 150, size: 26 });
      out.push(H.tbl(ws, [
        H.row([hd('×'), hd(''), hd(''), hd('')]),
        H.row([hd(''), v('56'), v(''), v('')]),
        H.row([hd(''), v(''), v(''), v('81')]),
        H.row([hd(''), v('48'), v('36'), v('')])
      ])); }
    out.push(H.p('Hint: which number can be made in only one way?', { after: 60 }));
    out.push(H.q(5, 'Ben puts 36 chairs in equal rows. There must be at least 2 rows and at least 2 chairs in each row. 3 rows of 12 is different from 12 rows of 3.', { keepNext: true }));
    out.push(H.sub('a', 'Find ALL the ways. Try 2 rows, then 3 rows, then 4 rows … in order.', { keepNext: true }));
    { const ws = [2300, 950, 950, 950, 950, 950, 950, 950, 950];
      out.push(H.tbl(ws, [
        H.row([C('Number of rows', ws[0], { bold: true, fill: 'EDEDED' }), C('2', 950), ...Array.from({ length: 7 }, () => C('', 950, { h: 140 }))]),
        H.row([C('Chairs in each row', ws[0], { bold: true, fill: 'EDEDED' }), C('18', 950), ...Array.from({ length: 7 }, () => C('', 950, { h: 140 }))])
      ])); }
    out.push(H.sub('b', 'How many ways are there?   ______'));
    out.push(H.sub('c', 'Most ways come in pairs, like 2 rows of 18 and 18 rows of 2. Which way has no partner? Why?'));
    out.push(...H.lines(2));
    out.push(H.q(6, 'Number riddle.', { keepNext: true }));
    out.push(H.sub('a', 'Find ALL the 2-digit numbers that can be divided exactly by 6 AND by 8. Hint: list the 2-digit numbers you can divide exactly by 8 (16, 24, 32 …), then test each one.'));
    out.push(...H.lines(2));
    out.push(H.sub('b', 'I am one of your numbers. My digits add up to 12. What number am I?'));
    out.push(H.ans());
    return out;
  }
};
