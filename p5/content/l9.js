// Math Inquirers P5 — Lesson 9: Pattern Generalisers (patterns and number sense)
const { TKQ, TKP } = require('./take.js');
// Heuristics: look for a pattern, make a table, say the rule in words (no letters), work backwards from a total,
// guess and check with a table, supposition ("suppose they are all the same").
// Every pattern term, count and answer below was worked out and checked with a short Python script.
// Figures are drawn from the stated rules: tables in a row 2 × n + 2 chairs; matchstick houses 5 × n + 1 sticks;
// (the border-tiles pattern on the slides: a row of n tiles with a grey border has 2 × n + 6 grey tiles).
const N = '#1B2A49', Y = '#FFC93C', SKY = '#DDEBF7', TEAL = '#1F7A6F', RED = '#D64545', WH = '#FFFFFF';
const FF = 'Fredoka, Arial, sans-serif';
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const txt = (x, y, s, size = 16, fill = N, anchor = 'middle', weight = 700) =>
  `<text x="${x}" y="${y}" font-size="${size}" font-weight="${weight}" text-anchor="${anchor}" fill="${fill}" font-family="${FF}">${esc(s)}</text>`;
const svg = (h, label, g) => `<svg aria-label="${esc(label)}" viewBox="0 0 600 ${h}" width="330" xmlns="http://www.w3.org/2000/svg" style="max-width:100%">${g}</svg>`;

// Q1: square tables pushed together in a row, one chair on every free side (1, 2, 3 tables: 4, 6, 8 chairs)
const tablesSvg = () => {
  const T = 48, off = 26, r = 10; let g = '', ox = 18;
  [1, 2, 3].forEach(n => {
    const x0 = ox + off, y0 = 40;
    for (let i = 0; i < n; i++) {
      const x = x0 + i * T;
      g += `<circle cx="${x + T / 2}" cy="${y0 - 16}" r="${r}" fill="${Y}" stroke="${N}" stroke-width="2.5"/>`;
      g += `<circle cx="${x + T / 2}" cy="${y0 + T + 16}" r="${r}" fill="${Y}" stroke="${N}" stroke-width="2.5"/>`;
    }
    g += `<circle cx="${x0 - 16}" cy="${y0 + T / 2}" r="${r}" fill="${Y}" stroke="${N}" stroke-width="2.5"/>`;
    g += `<circle cx="${x0 + n * T + 16}" cy="${y0 + T / 2}" r="${r}" fill="${Y}" stroke="${N}" stroke-width="2.5"/>`;
    for (let i = 0; i < n; i++) g += `<rect x="${x0 + i * T}" y="${y0}" width="${T}" height="${T}" fill="${SKY}" stroke="${N}" stroke-width="3"/>`;
    g += txt(x0 + n * T / 2, 148, `${n} table${n > 1 ? 's' : ''}`, 16);
    ox += n * T + 2 * off + 52;
  });
  return svg(160, 'Square tables in a row with a chair on each free side: 1 table has 4 chairs, 2 tables have 6 chairs, 3 tables have 8 chairs', g);
};

// Q2: matchstick houses in a row (square + equilateral roof); n houses use 5 × n + 1 sticks (6, 11, 16)
const housesSvg = () => {
  const u = 52, rh = u * Math.sqrt(3) / 2, base = 132, gap = 4; let g = '', ox = 30;
  const stick = (x1, y1, x2, y2) => {
    const L = Math.hypot(x2 - x1, y2 - y1), dx = (x2 - x1) / L * gap, dy = (y2 - y1) / L * gap;
    return `<line x1="${(x1 + dx).toFixed(1)}" y1="${(y1 + dy).toFixed(1)}" x2="${(x2 - dx).toFixed(1)}" y2="${(y2 - dy).toFixed(1)}" stroke="${N}" stroke-width="6" stroke-linecap="round"/>`;
  };
  [1, 2, 3].forEach(n => {
    for (let i = 0; i < n; i++) {
      const x = ox + i * u;
      g += stick(x, base, x + u, base) + stick(x, base - u, x + u, base - u);
      g += stick(x, base - u, x + u / 2, base - u - rh) + stick(x + u / 2, base - u - rh, x + u, base - u);
    }
    for (let i = 0; i <= n; i++) g += stick(ox + i * u, base, ox + i * u, base - u);
    g += txt(ox + n * u / 2, base + 30, `${n} house${n > 1 ? 's' : ''}`, 16);
    ox += n * u + 64;
  });
  return svg(172, 'Matchstick houses in a row: 1 house uses 6 sticks, 2 houses use 11 sticks, 3 houses use 16 sticks', g);
};

module.exports = {
  lesson: {
    n: 9, week: 5, session: 'A', title: 'Pattern Generalisers', topic: 'Patterns and Number Sense',
    objective: 'Continue growing patterns drawn as figures, say the rule for any figure in words (for example, number of sticks = 3 × figure number + 1) and explain it from the picture, work backwards from a total to find the figure, and solve “two kinds of things” problems with a guess-and-check table and with supposition.',
    skills: 'Looking for a pattern, making a table, describing the rule in words, working backwards, guess and check, supposition, explaining from a picture',
    materials: 'Matchsticks or toothpicks (about 20 per child, 40 if possible), square paper tiles or the square grid from the cut-out pages, mini whiteboard, workbook.',
    online: 'Children have toothpicks and paper squares ready on the desk and build each figure on camera. The tutor shares the slides; pairs work in breakout rooms for the explore and page 1, and check their tables against the slide.',
    warmup: 'Guess My Rule: children call out numbers, the tutor puts each through a secret two-step machine (× 3, then + 1) and says what comes out. Nobody races: everyone tests their idea on the next number, then says the rule in words when they are ready. Then five quick pattern questions on whiteboards.',
    explore: 'High fives: if everyone in our group of 8 high-fives everyone else exactly once, how many high fives is that? Pairs guess first, then start small (2, 3, 4 children), draw dots and lines, make a table and look for a pattern. If a pair wants more: a class of 30.',
    mini: 'Growing patterns: count each figure, put the counts in a table, see what each new figure adds and WHY from the picture (a new square shares a side, so it adds 3 sticks, not 4). Say the rule in words: sticks = 3 × figure number + 1. Use it for a far figure (figure 25) and backwards (61 sticks: take away 1, divide by 3). See the same pattern two ways (a border of tiles, on the slides). Before page 2: guess and check with a table (each change moves the total by the same amount); supposition (suppose they are all the cheaper kind, find the gap, divide by the change per swap); marks taken away for a wrong answer (each wrong answer costs the marks you lost AND the marks taken away).',
    share: 'Mei says: “10 squares in a row need 31 sticks, so 20 squares need 62 sticks.” Is she right? Explain with a picture.',
    exit: { q: 'Figure 1 of a pattern has 6 dots. Each figure has 4 more dots than the figure before.  (a) How many dots are in figure 20?  (b) Which figure has 102 dots?', a: '(a) 82 (6 + 19 × 4, or 4 × 20 + 2)  (b) Figure 25 (102 − 2 = 100, 100 ÷ 4 = 25)' },
    mistakes: [
      'Doubling: thinking figure 20 has twice as many as figure 10 (62 sticks instead of 61), because the starting stick or the end chairs get counted twice.',
      'Counting the jumps wrongly: adding 25 lots of 3 to figure 1 for figure 25, instead of 24 lots, or writing the rule as “add 3” without saying what to do with the figure number.',
      'Supposition: dividing the gap by the value of one thing (22 ÷ 4) instead of by the change for each swap (22 ÷ 2), and not checking the answer against BOTH facts (how many things and the total).'
    ],
    extension: 'A square grid of matchsticks: a 1 by 1 grid uses 4 sticks, a 2 by 2 grid uses 12 sticks. How many sticks for a 3 by 3 grid? A 10 by 10 grid? (24 and 220: a 10 by 10 grid has 11 rows of 10 sticks across and 11 columns of 10 sticks down.)',
    key: [
      ['Q1', '(a) 10, 12; 10 tables: 22 chairs  (b) Number of chairs = 2 × number of tables + 2  (c) 24 tables (2 × 24 + 2 = 50)  (d) No. 20 tables seat 2 × 20 + 2 = 42, not 44. Doubling counts the 2 end chairs twice.'],
      ['Q2', '(a) 5 sticks: the new house shares a wall with the house before  (b) Number of sticks = 5 × number of houses + 1; 20 houses need 101 sticks  (c) 39 houses (5 × 39 + 1 = 196 sticks), with 4 sticks left over'],
      ['Q3', '8 adult tickets and 7 child tickets (8 × $12 + 7 × $7 = $96 + $49 = $145). Each adult ticket in place of a child ticket adds $5.'],
      ['Q4', '(a) $6.00; up by 30¢  (b) 14 fifty-cent coins (and 16 twenty-cent coins). $10.20 − $6.00 = $4.20; $4.20 ÷ 30¢ = 14. Check: $7.00 + $3.20 = $10.20.'],
      ['Q5', '(a) 15 correct (all correct would be 100 marks; each wrong answer costs 5 + 2 = 7 marks; 100 − 65 = 35, 35 ÷ 7 = 5 wrong). Check: 75 − 10 = 65.  (b) Every score is 100 take away a number of 7s (100, 93, 86, 79, …). 100 − 80 = 20 is not a multiple of 7, so 80 is impossible.']
    ]
  },

  script: {
    hook: ['Today you become pattern generalisers. That is a big word for a simple, powerful idea: if you can see HOW a pattern grows, you can jump straight to the 100th figure without drawing 100 pictures.', 'Mathematicians and coders do this all the time. By the end of today you will say the rule for any figure in words, and use it backwards too.'],
    warmIntro: ['I have a secret machine. It does two things to every number. You call out a number, I tell you what comes out.', 'When you think you know the rule, do not shout it. Test it on the next number first. Then say it in words.'],
    predict: ['If all 8 of us high-five everyone else once, how many high fives is that? Write your guess in the corner of your whiteboard. Is it more or less than 50?'],
    exploreHints: ['Stuck: start with 2 children. Then 3. Draw each child as a dot and each high five as a line.', 'Stuck on the table: when a new child joins, how many NEW high fives does that child make?', 'If a pair wants more: how many high fives for a class of 30? Is there a quick way without adding 29 numbers?'],
    think: [
      '“Squares in a row. Figure 1 has 4 sticks, figure 2 has 7, figure 3 has 10. Each new square adds 3, not 4, because it shares a side with the square before. So I start with 1 stick and add 3 for every square: sticks = 3 × figure number + 1.”',
      '“For figure 25 I do not draw 25 squares. 3 × 25 + 1 = 76. And backwards: 61 sticks. Undo the last step first: 61 − 1 = 60, then 60 ÷ 3 = 20. Figure 20. I check: 3 × 20 + 1 = 61.”',
      '“Supposition. 24 vehicles with 70 wheels. Suppose they are ALL motorcycles: 48 wheels. I am 22 wheels short. Each time a motorcycle becomes a car I get 2 more wheels, so 22 ÷ 2 = 11 cars. Check both facts: 11 + 13 = 24 vehicles and 44 + 26 = 70 wheels.”'
    ],
    circulate: ['Ask: “What does each new figure add? Show me where it is in the picture.”', 'Ask: “Say your rule in words. Does it work for figure 1, 2 AND 3?”', 'Ask: “What did you suppose? How much does the total change for each swap?”'],
    hints: ['Hint 1: “Make a table: figure number in one row, count in the other.”', 'Hint 2: “Colour the part that stays the same in one colour and the part that grows in another.”', 'Hint 3: “To go backwards, undo the steps in reverse order: take away first, then divide.”'],
    talk: ['“Mei says 10 squares in a row need 31 sticks, so 20 squares need 62. Is she right?”', '“In Q4 and Q5, which did you like better: a guess-and-check table or supposition? Why?”'],
    talkAns: 'Mei is not right: 20 squares need 3 × 20 + 1 = 61 sticks. The rule is “3 for each square, plus 1 starting stick”. Doubling 31 doubles the starting stick too, so it counts one stick too many. The same thing happens with the end chairs in Q1.',
    close: ['“Today you found how patterns grow, said the rule in words, used it forwards and backwards, and solved two-kinds problems by supposing. That is generalising: one rule for every case.”', '“Do the exit ticket on your own, then show me.”']
  },

  deck: {
    today: 'See how a pattern grows, say the rule for any figure in words, work backwards from a total, and solve problems by supposing.',
    warmGame: 'Guess My Rule. Call out a number; the tutor puts it through a secret two-step machine and says what comes out. Test your idea on the next number before you say the rule in words. Play 1 round.',
    warmQs: [['7, 11, 15, 19, __, __', '23, 27'], ['1, 4, 9, 16, 25, __', '36'], ['2, 6, 18, 54, __', '162'], ['The 20th even number', '40']],
    expSetup: ['Guess first: if all 8 of us high-five everyone else once, how many high fives is that?', 'Start small: 2 children, then 3, then 4. Draw each child as a dot and each high five as a line.', 'Make a table: number of children and number of high fives. Stop at 6 children.', 'Look for a pattern in the table. What does each new child add?'],
    expPic: 'dots for 2, 3 and 4 children joined by lines, one line for each high five (1, 3 and 6 lines).',
    expAsk: [['How many high fives for 5 children?', '10. The table goes 1, 3, 6, 10: each new child high-fives everyone already there (add 2, then 3, then 4).'], ['How many for 6 children?', '15 (10 + 5).']],
    mini1: { head: 'Matchstick squares in a row: 4, 7, 10 sticks. Figure 25? Which figure uses 61 sticks?', body: ['Each new square shares a side, so it adds 3 sticks.', 'Rule in words: sticks = 3 × figure number + 1. Figure 25: 3 × 25 + 1 = 76.', 'Backwards: 61 − 1 = 60, 60 ÷ 3 = 20.'], ans: 'Figure 25 has 76 sticks; 61 sticks is figure 20. Check: 3 × 20 + 1 = 61.' },
    mini2: { head: 'A row of yellow tiles with a grey border: figure 1 has 8 grey tiles, figure 2 has 10, figure 3 has 12. How many grey tiles in figure 12?', body: ['Way 1: a top row and a bottom row of (figure + 2) tiles, and 1 tile at each end: 2 × figure number + 6.', 'Way 2: the whole rectangle is 3 rows of (figure + 2) tiles; take away the yellow tiles: 3 × 14 − 12.', 'Both ways: 30.'], ans: 'Figure 12 has 30 grey tiles. Two ways of seeing, one answer.' },
    keyHead: 'Key idea: find the rule, say it in words',
    keyBig: 'See what stays the same and what grows. Say the rule in words: sticks = 3 × figure number + 1.',
    keySmall: 'Check the rule on every figure. To go backwards, undo the steps in reverse: take away, then divide.',
    brk: 'Pattern moves: clap, clap, stamp, clap, clap, stamp … Do 12 moves together. Then: what is the 20th move? The 30th?',
    ws1: 'Page 1, in pairs: Q1 (a) (b) tables and chairs, Q2 (a) (b) matchstick houses (Q1 (c) (d) and Q2 (c) are take-home).',
    ws2: 'Page 2, on your own: Q3 guess and check with a table, Q4 (a) coins by supposition (Q4 (b) and Q5, the quiz with marks taken away, are take-home).'
  },

  qbank: {
    core: [
      { q: '5, 9, 13, 17, …  What is the 10th number in this pattern?', a: '41 (5 + 9 × 4: there are 9 jumps of 4 from the 1st number to the 10th).' },
      { q: 'Matchstick squares in a row use 4, 7, 10, … sticks. How many sticks are needed for 8 squares?', a: '25 (3 × 8 + 1).' },
      { q: '2, 6, 10, 14, …  Is 50 in this pattern? Explain.', a: 'Yes. 50 − 2 = 48 and 48 ÷ 4 = 12 jumps, so 50 is the 13th number.' },
      { q: 'There are 15 bicycles and tricycles in a shed. They have 37 wheels altogether. How many tricycles are there?', a: '7 tricycles (suppose all 15 are bicycles: 30 wheels; 7 wheels short; each tricycle adds 1 more wheel). 8 bicycles. Check: 16 + 21 = 37.' },
      { q: 'The rule for a dot pattern is: number of dots = 3 × figure number + 2. How many dots are in figure 15?', a: '47' },
      { q: 'Pens cost $2 each and files cost $3 each. Ben buys 10 items and pays $24. How many files does he buy?', a: '4 files and 6 pens (all pens would be $20; each file instead of a pen adds $1). Check: $12 + $12 = $24.' }
    ],
    stretch: [
      { q: 'Beads repeat in the order red, red, blue, yellow, yellow, yellow. What colour is the 50th bead? How many yellow beads are in the first 100?', a: 'Red (50 = 8 × 6 + 2, so it is the 2nd bead of a group). 49 yellow beads: 16 full groups of 6 give 96 beads and 48 yellow, and beads 97 to 100 are red, red, blue, yellow.' },
      { q: '40 square tables in one long row seat 2 × 40 + 2 = 82 people. How many can sit if the tables are put in 8 rows of 5 tables instead?', a: '96 (each row of 5 seats 12, and 8 × 12 = 96). One long row seats only 82. Splitting the tables gives more end seats.' },
      { q: 'A farm has chickens and goats. There are 35 heads and 94 legs. How many goats are there?', a: '12 goats and 23 chickens (all chickens would have 70 legs; 24 legs short; each goat adds 2 legs). Check: 48 + 46 = 94.' },
      { q: 'Work out 1 + 3, 1 + 3 + 5 and 1 + 3 + 5 + 7. What do you notice? Use it to add the first 20 odd numbers, 1 + 3 + … + 39.', a: '4, 9, 16: square numbers. The first 20 odd numbers add up to 20 × 20 = 400. (Each new odd number adds an L-shaped layer to a square of dots.)' },
      { q: 'Ali saves $3 in week 1. Each week he saves $2 more than the week before. How much does he save in week 15?', a: '$31 ($3 + 14 × $2).' },
      { q: '3, 8, 13, 18, …  What is the first number in this pattern that is greater than 200?', a: '203 (the 41st number: 3 + 40 × 5).' },
      { q: 'Two whole numbers next to each other multiply to give 702. What are they?', a: '26 and 27. 25 × 26 = 650 is too small and 27 × 28 = 756 is too big. Check: 26 × 27 = 702.' },
      { q: 'A test has 10 questions. A correct answer scores 3 marks and 1 mark is taken away for each wrong answer. Siti answered every question and scored 18. How many did she get correct?', a: '7 (all correct would be 30; each wrong answer costs 3 + 1 = 4 marks; 12 ÷ 4 = 3 wrong). Check: 21 − 3 = 18.' }
    ],
    challenge: [
      { q: 'A staircase is built from squares: step 1 is 1 square, step 2 adds a column of 2 (3 squares altogether), step 3 adds a column of 3 (6 squares). How many squares are there in the staircase with 10 steps?', a: '55 (1 + 2 + 3 + … + 10). Two copies of the staircase make a 10 by 11 rectangle: 110 ÷ 2 = 55.' },
      { q: 'Make up your own growing pattern with matchsticks, dots or tiles. Draw the first three figures, work out the rule in words, and write two questions for a partner: the number of sticks in figure 50, and which figure uses exactly 100 sticks (or explain why no figure does). Swap and check. What if the pattern started with a different first figure?', a: 'Open-ended. Sample: matchstick triangles in a row use 3, 5, 7, … sticks, so sticks = 2 × figure number + 1. Figure 50 uses 101 sticks. No figure uses exactly 100 sticks, because 2 × figure number + 1 is always odd (figure 49 uses 99 and figure 50 uses 101). Check that the rule works for figures 1, 2 and 3.' },
      { q: 'How many squares of all sizes are there on a 4 by 4 grid?', a: '30 (16 small, 9 of size 2 by 2, 4 of size 3 by 3 and 1 of size 4 by 4).' },
      { q: 'Spiders have 8 legs and beetles have 6 legs. A box holds 20 of them. (a) If there are 8 spiders, how many legs are there altogether? (b) List ALL the possible totals of legs. (c) Mei says the box has 135 legs. Why must she be wrong? How many spiders would give 148 legs?', a: '(a) 8 × 8 + 12 × 6 = 136 legs. (b) The smallest total is 120 (no spiders) and each spider instead of a beetle adds 2 legs, so the totals are every EVEN number from 120 to 160: 21 different totals. (c) 135 is odd and every total is even. 148 = 120 + 28, so 14 spiders (and 6 beetles).' },
      { q: 'How many digits are needed to number the pages of a book from page 1 to page 150?', a: '342 (9 one-digit pages, 90 two-digit pages = 180 digits, 51 three-digit pages = 153 digits).' },
      { q: 'A square grid of matchsticks: a 1 by 1 grid uses 4 sticks and a 2 by 2 grid uses 12 sticks. How many sticks does a 10 by 10 grid use?', a: '220. There are 11 rows of 10 sticks going across and 11 columns of 10 sticks going down: 110 + 110.' },
      { q: 'A dot pattern makes diamonds. Figure 1 has 1 dot. Figure 2 has rows of 1, 3 and 1 dots (5 dots). Figure 3 has rows of 1, 3, 5, 3 and 1 dots (13 dots). How many dots are in figure 6?', a: '61. The counts go 1, 5, 13, 25, 41, 61 (add 4, 8, 12, 16, 20). Or: each diamond is two square numbers of dots, 6 × 6 + 5 × 5 = 36 + 25 = 61.' },
      { q: 'A quiz has 25 questions. A correct answer scores 4 marks, 1 mark is taken away for each wrong answer, and a blank scores 0. Mei left 3 questions blank and scored 68. How many did she get correct?', a: '18. She answered 22 questions. All 22 correct would be 88 marks; each wrong answer costs 4 + 1 = 5 marks; 88 − 68 = 20, 20 ÷ 5 = 4 wrong. Check: 72 − 4 = 68.' },
      { q: 'Ali writes the counting numbers one after another without spaces: 123456789101112131415… What is the 100th digit he writes?', a: '5. The numbers 1 to 9 use 9 digits. That leaves 91 digits: 45 two-digit numbers (10 to 54) use 90 of them, so the 100th digit is the first digit of 55.' }
    ]
  },

  workbook: H => {
    const W = [];
    W.push(H.p('A growing pattern: find what stays the same and what grows each time. Then say the rule in words, like this:  number of sticks = 3 × figure number + 1.', { after: 40 }));
    // Q1 tables and chairs
    W.push(H.q(1, 'At a hawker centre, square tables are pushed together in a row. One chair goes on each free side.', { before: 10, keepNext: true }));
    W.push(H.fig(tablesSvg()));
    W.push(H.sub('a', '4 tables:  ______ chairs.   5 tables:  ______ chairs.   10 tables:  ______ chairs.'));
    W.push(H.sub('b', 'Rule in words:   chairs  =  ______ × tables  +  ______'));
    W.push(H.sub('c', [TKP, 'How many tables are needed to seat exactly 50 people?   ______________']));
    W.push(H.sub('d', [TKP, 'Ben says, “10 tables seat 22 people, so 20 tables seat 44.” Is he right? Explain.'], { after: 20 }));
    W.push(...H.lines(1));
    // Q2 matchstick houses
    W.push(H.q(2, 'Matchstick houses are joined in a row.', { keepNext: true }));
    W.push(H.fig(housesSvg()));
    W.push(H.sub('a', 'Each new house adds ______ sticks. Why not 6?  ______________________________', { after: 40 }));
    W.push(H.sub('b', 'Rule:   sticks  =  ______ × houses  +  ______.   For 20 houses:  ______ sticks.'));
    W.push(H.sub('c', [TKP, 'Mei has 200 sticks. Greatest number of houses she can make? Sticks left over?  ______________']));
    // ---- page 2 ----
    W.push(H.q(3, 'Guess and check with a table. Adult tickets to the Science Centre cost $12 each and child tickets cost $7 each. A group buys 15 tickets for $145 altogether. How many adult tickets do they buy?', { pb: true, before: 0, keepNext: true }));
    { const ws = [2000, 2000, 3400, 2500];
      W.push(H.tbl(ws, [H.row(['Adult tickets', 'Child tickets', 'Total cost', 'Too much or too little?'].map((s, i) => H.cell(s, ws[i], { bold: true, fill: 'D9D9D9', h: 40 }))),
        H.row([H.cell('5', ws[0], { h: 40 }), H.cell('10', ws[1], { h: 40 }), H.cell('$60 + $70 = $130', ws[2], { h: 40 }), H.cell('too little', ws[3], { h: 40 })]),
        ...[1, 2, 3].map(() => H.row(ws.map(w => H.cell('', w, { h: 50 }))))])); }
    W.push(H.p('Answer:  ______ adult tickets and ______ child tickets.', { before: 40, after: 20 }));
    // Q5 supposition, coins
    W.push(H.q(4, 'Siti has 30 coins. They are all 20¢ and 50¢ coins, worth $10.20 altogether.', { keepNext: true }));
    W.push(H.sub('a', 'If all 30 coins were 20¢: worth ____________.  Each change of a 20¢ for a 50¢ adds ____________.'));
    W.push(H.sub('b', [TKP, 'How many 50¢ coins does Siti have? Show your working and check.'], { after: 20 }));
    W.push(...H.lines(2));
    // Q6 marks taken away
    W.push(H.q(5, [TKQ, 'A quiz has 20 questions. Each correct answer scores 5 marks. For each wrong answer, 2 marks are taken away. Ali answered every question and scored 65 marks.'], { keepNext: true }));
    W.push(H.sub('a', 'How many questions did Ali get correct? Hint: suppose he got them all correct first.', { after: 20 }));
    W.push(...H.lines(2));
    W.push(H.sub('b', 'Mei also answered every question and says she scored 80 marks. Why must she be wrong? Start here: all correct scores 100. Each wrong answer takes off 7. Write the scores for 0, 1, 2, 3 wrong: 100, ____, ____, ____. Is 80 in your list?', { after: 20 }));
    W.push(...H.lines(2));
    return W;
  }
};

// ---- figure for the printed Go further B1 (the diamond dot pattern): figures 1, 2 and 3 ----
{
  const D = '#1B2A49', T = '#1F7A6F';
  let g = '', x0 = 10;
  [[1], [1, 3, 1], [1, 3, 5, 3, 1]].forEach((rows, f) => {
    const w = 5 * 18, cx = x0 + w / 2, h = rows.length;
    rows.forEach((n, r) => { for (let i = 0; i < n; i++) g += `<circle cx="${cx + (i - (n - 1) / 2) * 18}" cy="${20 + r * 18}" r="6" fill="#FFC93C" stroke="${D}" stroke-width="2"/>`; });
    g += `<text x="${cx}" y="${20 + 4 * 18 + 24}" font-size="16" font-weight="700" text-anchor="middle" fill="${T}" font-family="Arial">Figure ${f + 1}</text>`;
    x0 += w + 26;
  });
  const fig = `<svg aria-label="Three diamond dot patterns: figure 1 has 1 dot, figure 2 has rows of 1, 3 and 1 dots, figure 3 has rows of 1, 3, 5, 3 and 1 dots" viewBox="0 0 ${x0} 124" xmlns="http://www.w3.org/2000/svg" style="width:${Math.round(x0 * 0.8)}px;max-width:100%">${g}</svg>`;
  module.exports.qbank.challenge[module.exports.qbank.challenge.length - 3].fig = fig;
}
