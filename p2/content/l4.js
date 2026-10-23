// Math Inquirers P2, Lesson 4: Pattern Machines (patterns with multiplication, tables 2, 3, 4, 5, 10)
// Every answer below was worked out and checked; "find all" answers list every case.

const N = '#1B2A49', Y = '#FFC93C', SKY = '#DDEBF7', TEAL = '#1F7A6F', RED = '#D64545', W = '#FFFFFF';
const txt = (x, y, s, o = {}) => `<text x="${x}" y="${y}" font-size="${o.size || 18}" font-weight="${o.w || 700}" text-anchor="${o.anchor || 'middle'}" fill="${o.fill || N}" font-family="Fredoka, Arial, sans-serif">${s}</text>`;
const svg = (w, h, label, inner, width) => `<svg viewBox="0 0 ${w} ${h}" xmlns="http://www.w3.org/2000/svg" aria-label="${label}" style="width:${width || w}px;max-width:100%;height:auto">${inner}</svg>`;
const shape = (k, x, y, r = 20) => {
  if (k === 'tri') return `<polygon points="${x},${y - r} ${x + r},${y + r * 0.8} ${x - r},${y + r * 0.8}" fill="${Y}" stroke="${N}" stroke-width="3" stroke-linejoin="round"/>`;
  if (k === 'cir') return `<circle cx="${x}" cy="${y}" r="${r * 0.9}" fill="${SKY}" stroke="${N}" stroke-width="3"/>`;
  return `<rect x="${x - r * 0.85}" y="${y - r * 0.85}" width="${r * 1.7}" height="${r * 1.7}" fill="${TEAL}" stroke="${N}" stroke-width="3"/>`;
};
// Q1: triangle, circle, circle, square, square (places 1 to 10)
function shapeFig() {
  const P = ['tri', 'cir', 'cir', 'sq', 'sq'];
  let g = '';
  for (let i = 0; i < 10; i++) { const x = 34 + i * 59; g += shape(P[i % 5], x, 34) + txt(x, 88, String(i + 1), { size: 18, fill: TEAL }); }
  g += txt(300, 116, 'place', { size: 16, fill: TEAL, w: 600 });
  return svg(600, 122, 'Shape pattern, places 1 to 10: triangle, circle, circle, square, square, triangle, circle, circle, square, square', g, 540);
}
// Q2: letter tiles M A T H M A T H
function letterFig() {
  let g = '';
  'MATHMATH'.split('').forEach((c, i) => { const x = 24 + i * 70; g += `<rect x="${x}" y="8" width="58" height="58" rx="10" fill="${i < 4 ? Y : '#FFF0C2'}" stroke="${N}" stroke-width="3"/>` + txt(x + 29, 49, c, { size: 30 }) + txt(x + 29, 92, String(i + 1), { size: 18, fill: TEAL }); });
  return svg(600, 100, 'Letter tiles M A T H M A T H in places 1 to 8', g, 470);
}
// Q3: one flower with 5 petals
function flowerFig() {
  let g = '';
  for (let k = 0; k < 5; k++) { const a = (k * 72 - 90) * Math.PI / 180; g += `<ellipse cx="${(50 + 26 * Math.cos(a)).toFixed(1)}" cy="${(50 + 26 * Math.sin(a)).toFixed(1)}" rx="17" ry="12" transform="rotate(${k * 72 - 90} ${(50 + 26 * Math.cos(a)).toFixed(1)} ${(50 + 26 * Math.sin(a)).toFixed(1)})" fill="${RED}" stroke="${N}" stroke-width="3"/>`; }
  g += `<circle cx="50" cy="50" r="14" fill="${Y}" stroke="${N}" stroke-width="3"/>`;
  return svg(100, 100, 'A flower with 5 petals', g, 60);
}
// Q4: 1, 2 and 3 square tables pushed together, one child at each open side
function tablesFig() {
  let g = ''; const s = 44, kid = (x, y) => `<circle cx="${x}" cy="${y}" r="10" fill="${Y}" stroke="${N}" stroke-width="3"/>`;
  [[1, 30], [2, 170], [3, 360]].forEach(([n, x0]) => {
    const y0 = 34;
    for (let i = 0; i < n; i++) g += `<rect x="${x0 + 22 + i * s}" y="${y0}" width="${s}" height="${s}" fill="${SKY}" stroke="${N}" stroke-width="3"/>`;
    for (let i = 0; i < n; i++) g += kid(x0 + 22 + i * s + s / 2, y0 - 16) + kid(x0 + 22 + i * s + s / 2, y0 + s + 16);
    g += kid(x0 + 6, y0 + s / 2) + kid(x0 + 38 + n * s, y0 + s / 2);
    g += txt(x0 + 22 + n * s / 2, y0 + s + 52, n + (n === 1 ? ' table' : ' tables'), { size: 18 });
  });
  return svg(600, 136, 'Square tables in a row with a child at each open side: 1 table seats 4, 2 tables seat 6, 3 tables seat 8', g, 520);
}
// Q6: beads 2 red, 3 yellow, repeating (first 10)
function beadFig() {
  let g = `<line x1="10" y1="40" x2="590" y2="40" stroke="${N}" stroke-width="3"/>`;
  for (let i = 0; i < 10; i++) { const red = i % 5 < 2; g += `<circle cx="${40 + i * 54}" cy="40" r="20" fill="${red ? RED : Y}" stroke="${N}" stroke-width="3"/>` + txt(40 + i * 54, 47, red ? 'R' : 'Y', { size: 18, fill: red ? W : N }); }
  g += txt(578, 47, '…', { size: 22 });
  return svg(600, 78, 'A bead string: 2 red, 3 yellow, 2 red, 3 yellow, and so on', g, 470);
}

const lesson = {
  n: 4, week: 2, session: 'B', title: 'Pattern Machines', topic: 'Patterns with Multiplication',
  objective: 'Find far places in a repeating pattern by counting in groups (the ends of the groups are in a times table); count how many of one shape there are; describe a growing pattern with a table and a rule and use it to go forwards and backwards; find the numbers that two counting patterns share.',
  skills: 'Look for a pattern, make a table, make a list, explain a rule',
  materials: 'Linking cubes in 3 colours (about 20 per pair), mini whiteboards, matchsticks or lolly sticks (about 25 per pair), counters.',
  online: 'Children use coloured pencils and squared paper (or Lego bricks) for the cube train, and draw sticks for the growing pattern. The tutor shares the slides and the children check their tables against the slide.',
  warmup: 'Pattern rhythm: clap, clap, stomp, clap, clap, stomp … The group keeps the rhythm going; the tutor stops and asks what comes on beat 9, beat 10 and beat 20.',
  explore: 'Cube train: build red, red, blue, red, red, blue … with 9 cubes. Without building more, predict the colour of cube 20, then build to check. Which cubes are blue?',
  mini: 'Repeating patterns: find the group size; groups end at the times-table numbers (3, 6, 9 …); then count on from the end of a group. Count how many of one shape by counting the groups.',
  share: 'A pattern repeats every 5 shapes. Is the 10th shape always the same as the 20th? What if the pattern repeats every 3 shapes?',
  exit: { q: 'The pattern goes triangle, circle, square, triangle, circle, square … What is the 17th shape? How do you know?', a: 'A circle. 15 ends a group (5 groups of 3), so 16 is a triangle and 17 is a circle.' },
  mistakes: [
    'Saying that a place in the times table (like 20 for a group of 5) is the FIRST shape of a group, when it is the LAST shape.',
    'Counting the whole pattern one by one to the far place instead of jumping to the end of a group.',
    'Growing patterns: multiplying by the step (10 squares × 3 = 30) and forgetting the start (the extra stick), instead of using the table or the rule.'
  ],
  takehome: 'Page 1: Q2(c) (30 letters, how many Ts) and Q3(b) (beads altogether). Page 2: Q4(d) (23 petals) and Q5(d) (why does it go up by 2). The two machine and growing-pattern teaching slides moved into the mini-lesson.',
  extension: 'Make your own repeating pattern of 4 shapes. Write 3 "far place" questions about it for a partner, with the answers.',
  key: [
    ['Q1', '(a) Square (20 ends a group of 5).  (b) Circle (21 triangle, 22 circle, 23 circle).  (c) Triangle: 40 ends a group (5 × 8 = 40), so 41 starts again.'],
    ['Q2', '(a) A (16 ends a group of 4; 17 is M, 18 is A).  (b) Place 40 (every H ends a group: 4, 8, 12 … the 10th is 4 × 10).  (c) 7 Ts. They are in places 3, 7, 11, 15, 19, 23, 27; 28 ends the 7th group, and places 29 and 30 are M and A.'],
    ['Q3', '(a) 18 yellow beads (12 red is 6 groups of 2 red; each group has 3 yellow).  (b) 30 beads (6 groups of 5).'],
    ['Q4', '(a) 5, 10, 15, 20, 25, 30.  (b) 50 petals.  (c) 7 flowers.  (d) 4 flowers, with 3 petals left over.'],
    ['Q5', '(a) 4, 6, 8, 10, 12, 14.  (b) 22 children.  (c) 9 tables.  (d) Each new table adds 1 seat on the top and 1 on the bottom; the 2 seats at the ends stay the same.'],
    ['Q6', 'Ali (12 numbers, ending at 36): 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36. Mei (9 numbers, ending at 36): 4, 8, 12, 16, 20, 24, 28, 32, 36. Both: 12, 24, 36. They go up by 12 each time.']
  ]
};

const script = {
  hook: ['Hello, pattern machines! Today we find out what is far, far along a pattern, like the 41st shape, without drawing all 41.', 'The secret is groups. If we know the group, the times tables tell us where every group ends.'],
  warmIntro: ['Clap, clap, stomp. Clap, clap, stomp. Keep it going with me!', 'Freeze! What will we do on beat 9? On beat 10? How do you know?'],
  predict: ['Our cube train goes red, red, blue, red, red, blue. What colour do you think cube 20 will be? Write your guess before you build.'],
  exploreHints: [
    'Stuck: put a finger on each blue cube. Say their numbers. What do you notice?',
    'The blue cubes are at 3, 6, 9 … Which table is that? Keep counting in 3s.',
    'Finished early: what colour is cube 30? Cube 31? Explain without building.'
  ],
  think: [
    '"Sun, moon, star, sun, moon, star. The group is 3 shapes long. Every group ends with a star, at 3, 6, 9, 12: the 3 times table. Place 14? 12 is the end of a group, so 13 starts again with a sun, and 14 is a moon."',
    '"Where is the 5th star? There is one star at the end of each group, so the 5th star ends the 5th group: 5 × 3 = 15."',
    '"Squares made of sticks: 4, 7, 10. Each new square needs only 3 more sticks because it shares a side. I make a table and keep adding 3."'
  ],
  circulate: [
    'Ask: "How long is one group? Where does each group end?"',
    'Ask: "Is that place the first shape of a group or the last?"',
    'Ask: "What is the rule? Does it work for every pair in your table?"'
  ],
  hints: [
    'Hint 1: "Draw a line after each group. Count the groups."',
    'Hint 2: "Find the nearest times-table number before your place. That shape ends a group."',
    'Hint 3: "Make a table and look at how much it goes up each time."'
  ],
  talk: ['"A pattern repeats every 5 shapes. Is the 10th shape always the same as the 20th?"'],
  talkAns: 'Yes: 10 and 20 are both in the 5 times table, so both are the last shape of a group. (If it repeated every 3 shapes the answer would be no: 9 ends a group, so 10 is the 1st shape; 18 ends a group, so 20 is the 2nd shape.)',
  close: ['"You did not draw 41 shapes today. You found the group, used a times table and counted on. That is how pattern machines think."']
};

const deck = {
  today: 'Find far places in a pattern by counting in groups, and find the rule of a growing pattern with a table.',
  warmGame: 'Pattern rhythm: clap, clap, stomp, clap, clap, stomp … Keep it going. What do we do on beat 9? Beat 10? Beat 20?',
  warmQs: [['4, 8, 12, __', '16'], ['50, 45, 40, __', '35'], ['3, 6, 9, 12, __', '15'], ['Count in 4s from 4. What is the 10th number?', '40'], ['2, 5, 8, 11, __', '14']],
  expSetup: ['Build a cube train: red, red, blue, red, red, blue …', 'Stop after 9 cubes.', 'Predict: what colour is cube 20? Write it down.', 'Build to check. Which cubes are blue?'],
  expPic: 'a cube train of 9 cubes, red, red, blue three times, with a question mark at cube 20.',
  expAsk: [['What colour is cube 20?', 'Red.'], ['How did you know without building?', 'The blue cubes are at 3, 6, 9 … 18, so 19 and 20 are red.'], ['Which cubes are blue?', 'The 3 times table: 3, 6, 9, 12, 15, 18 …']],
  mini1: { head: 'Far places: count in groups', body: ['Sun, moon, star, sun, moon, star …', 'The group is 3 shapes. Groups end at 3, 6, 9, 12.', 'What is in place 14?'], ans: 'A moon (12 ends a group; 13 sun, 14 moon).' },
  mini2: { head: 'Where is the 5th star?', body: ['One star in each group, at the end.', 'Stars are at 3, 6, 9, 12, 15.', 'Where is the 5th star? How many moons are in the first 21 shapes?'], ans: 'Place 15. 7 moons (21 shapes is 7 groups).' },
  keyHead: 'Key idea: count in groups',
  keyBig: 'Find the group size. The groups end at the times-table numbers. Jump to the end of a group, then count on.',
  keySmall: 'Growing pattern? Make a table, find the rule, then keep going.',
  brk: 'Pattern moves: jump, jump, squat, jump, jump, squat … 15 moves. What is move 15?',
  ws1: 'Page 1, in pairs: Q1 the shape pattern, Q2 the MATH letters, Q3 the bead string.',
  ws2: 'Page 2, on your own: Q4 flower petals, Q5 tables and chairs, Q6 numbers in both counts.'
};

const qbank = {
  core: [
    { q: 'Count in 4s. Fill in the next three numbers: 4, 8, 12, __, __, __', a: '16, 20, 24' },
    { q: 'A pattern goes red, blue, red, blue … What colour is the 10th bead?', a: 'Blue (every even place is blue).' },
    { q: 'Each hand has 5 fingers. How many fingers are on 6 hands?', a: '30 fingers (5, 10, 15, 20, 25, 30).' },
    { q: 'A pattern goes star, circle, circle, star, circle, circle … What is the 9th shape?', a: 'A circle. 9 ends a group of 3, and each group ends with a circle.' },
    { q: 'What is the rule? 3, 7, 11, 15 … Write the next two numbers.', a: 'Add 4. The next numbers are 19 and 23.' },
    { q: 'A number pattern goes 10, 20, 30 … What is the 8th number?', a: '80' }
  ],
  stretch: [
    { q: 'Look at the shape pattern in the Start here page again (places 1 to 10). How many circles are there in the first 30 shapes? How do you know?', a: '12 circles (30 shapes is 6 groups of 5, with 2 circles in each group).', fig: shapeFig() },
    { q: 'Beads go red, red, blue, green, red, red, blue, green … Mei says the 30th bead is blue. Is she right? Which places up to 30 have a green bead?', a: 'Mei is not right. The pattern repeats every 4 beads and 28 ends a group (4 × 7 = 28), so the 29th bead is red and the 30th bead is red. Green beads are the 4th bead of each group: places 4, 8, 12, 16, 20, 24 and 28.' },
    { q: 'Beads go red, yellow, yellow, red, yellow, yellow … How many yellow beads are in the first 18 beads?', a: '12 yellow beads (18 beads is 6 groups of 3, with 2 yellow in each).' },
    { q: 'Houses are made of sticks in a row. 1 house uses 5 sticks, 2 houses use 9 sticks, 3 houses use 13 sticks. How many sticks are needed for 6 houses?', a: '25 sticks. The rule is add 4: 5, 9, 13, 17, 21, 25.' },
    { q: 'Ali counts in 4s from 4. Mei counts in 10s from 10. Which numbers up to 50 do they both say?', a: '20 and 40.' },
    { q: 'A pattern goes 1, 2, 3, 1, 2, 3 … What is the total of the first 15 numbers?', a: '30. 15 numbers is 5 groups, and each group adds up to 6: 6 + 6 + 6 + 6 + 6 = 30.' },
    { q: 'Ben’s pattern is 2, 5, 8, 11 … Will 30 be in his pattern? Explain.', a: 'No. The pattern goes 2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32 … It jumps from 29 to 32. (Every number is 1 less than a number in the 3 times table, and 30 is in the 3 times table.)' },
    { q: 'A pattern repeats every 4 shapes. The 20th shape is a heart. What is the 40th shape? How do you know?', a: 'A heart. 20 and 40 are both in the 4 times table, so both are the last shape of a group.' },
    { q: 'A pattern goes square, circle, circle, square, circle, circle … Mei draws 20 shapes. How many squares does she draw?', a: '7 squares (in places 1, 4, 7, 10, 13, 16, 19). 18 shapes is 6 groups with 6 squares, and place 19 is one more square.' }
  ],
  challenge: [
    { q: 'A pattern starts at 2. It goes up 5, then up 1, then up 5, then up 1, and so on: 2, 7, 8, 13, 14 … Will the pattern ever say 50? Will it ever say 51? Explain how you know.', a: 'It says 50 but never 51. Keep going: 2, 7, 8, 13, 14, 19, 20, 25, 26, 31, 32, 37, 38, 43, 44, 49, 50, 55. Every two steps the number goes up by 6, so 50 is in the list, but the list jumps from 50 to 55 and 51 is not there.' },
    { q: 'Houses are made of sticks in a row: 1 house uses 5 sticks, 2 houses use 9, 3 houses use 13. Ben has 40 sticks. What is the most houses he can make? How many sticks are left over?', a: '9 houses use 37 sticks, with 3 left over (10 houses would need 41).' },
    { q: 'A frog starts at 1 and jumps 4 each time: 1, 5, 9, 13 … Will it land on 37? Will it land on 30? Explain.', a: 'It lands on 37 but not on 30. The frog lands on numbers 1 more than the 4 times table: 36 + 1 = 37, but 30 is not 1 more than a 4 times table number (it lands on 29 and 33).' },
    { q: 'A pattern repeats every 5 shapes. In each group, only the 3rd shape is a star. Which of these places have a star: 13, 23, 30, 48?', a: '13, 23 and 48. Stars are 2 more than the 5 times table: 13 = 10 + 3, 23 = 20 + 3, 48 = 45 + 3. 30 ends a group, so it is the 5th shape.' },
    { q: 'Make up your own repeating pattern of 4 shapes. Write 3 “far place” questions about it for a partner (one place in the 40s), with the answers. Then change your pattern so it repeats every 5 shapes. Which of your answers change? Which stay the same?', a: 'Open. Example: square, circle, circle, triangle. Place 41 is a square (40 ends a group), place 46 is a circle, place 48 is a triangle. With a group of 5 the answers change, except for places that are in both the 4 and the 5 times tables (20 and 40 are still the end of a group, but the last shape of the new pattern may be different).' },
    { q: 'A pattern goes triangle, square, circle, circle, circle, triangle, square, circle, circle, circle … How many circles are in the first 42 shapes?', a: '24 circles. 40 shapes is 8 groups with 3 circles each (24); places 41 and 42 are a triangle and a square.' },
    { q: 'Ali counts in 3s from 3. Mei counts in 4s from 4. They both say 12. Predict the next number they will BOTH say. Then list every number up to 100 that they both say. What do you notice? Why?', a: '24 is next. They both say 12, 24, 36, 48, 60, 72, 84 and 96 (8 numbers): the numbers go up by 12 each time, because 12 is the first number in both the 3 and 4 times tables, and each next one is 12 more.' },
    { q: 'Siti builds towers of cubes. Tower 1 has 2 cubes, tower 2 has 5 cubes, tower 3 has 8 cubes. The towers keep growing in the same way. Which tower has 29 cubes? Is there a tower with exactly 50 cubes? With exactly 100 cubes? Explain how you know.', a: 'Tower 10 has 29 cubes (the rule is add 3: 2, 5, 8, 11, … 29). Tower 17 has 50 cubes. No tower has 100: every tower has 1 less than a number in the 3 times table (tower 10: 30 − 1 = 29), and 101 is not in the 3 times table (99 and 102 are).' },
    { q: 'Frog A starts at 0 and jumps 4 each time: 4, 8, 12 … Frog B starts at 2 and jumps 3 each time: 5, 8, 11 … Which numbers up to 30 do both frogs land on?', a: '8 and 20. Frog A: 4, 8, 12, 16, 20, 24, 28. Frog B: 5, 8, 11, 14, 17, 20, 23, 26, 29.' }
  ]
};

const workbook = H => {
  const out = [];
  const TH = () => H.t('★ take-home  ', { bold: true, color: '1B2A49' });
  const hr = (ws, lab, vals, h = 80) => H.row([H.cell(lab, ws[0], { bold: true, fill: 'D9D9D9', h }), ...vals.map((v, i) => H.cell(v || ' ', ws[i + 1], { h }))]);
  // ---- page 1 (in pairs)
  out.push(H.q(1, 'This pattern keeps going in the same way. Here are places 1 to 10. Tip: draw a line after the LAST shape of each group.', { before: 20, keepNext: true }));
  out.push(H.fig(shapeFig()));
  out.push(H.sub('a', 'What shape is in place 20?   __________        (b)  In place 23?   __________'));
  out.push(H.sub('c', 'What shape is in place 41?   __________     How do you know?'));
  out.push(...H.lines(1));
  out.push(H.q(2, 'Ali writes the letters M, A, T, H again and again.', { keepNext: true }));
  out.push(H.fig(letterFig()));
  out.push(H.sub('a', 'What is the 18th letter?   ______        (b)  Where is the 10th letter H?   place ______'));
  out.push(H.sub('c', [TH(), H.t('Ali writes 30 letters. How many Ts does he write?   ______   Show how you know.')]));
  out.push(...H.lines(1));
  out.push(H.q(3, 'Siti’s bead string goes 2 red, 3 yellow, 2 red, 3 yellow … It has 12 red beads and ends with yellow beads. Tip: draw one group, then count the groups.', { keepNext: true }));
  out.push(H.fig(beadFig()));
  out.push(H.sub('a', 'How many yellow beads?   ______'));
  out.push(H.sub('b', [TH(), H.t('How many beads altogether?   ______')]));
  // ---- page 2 (on your own)
  out.push(H.q(4, 'Each flower has 5 petals.', { pb: true, before: 0, keepNext: true }));
  out.push(H.fig(flowerFig()));
  out.push(H.sub('a', 'Fill in the table.'));
  { const ws = [2100, 1300, 1300, 1300, 1300, 1300, 1300];
    out.push(H.tbl(ws, [hr(ws, 'Flowers', ['1', '2', '3', '4', '5', '6']), hr(ws, 'Petals', ['5', '', '', '', '', ''])])); }
  out.push(H.gap(20));
  out.push(H.sub('b', 'Petals on 10 flowers?   ______        (c)  35 petals make how many flowers?   ______'));
  out.push(H.sub('d', [TH(), H.t('Mei has 23 petals. How many flowers?   ______     Petals left over?   ______')]));
  out.push(H.q(5, 'Square tables are pushed together in a row. One child sits at each open side.', { keepNext: true }));
  out.push(H.fig(tablesFig()));
  out.push(H.sub('a', 'Fill in the table.'));
  { const ws = [2100, 1300, 1300, 1300, 1300, 1300, 1300];
    out.push(H.tbl(ws, [hr(ws, 'Tables', ['1', '2', '3', '4', '5', '6']), hr(ws, 'Children', ['4', '6', '', '', '', ''])])); }
  out.push(H.gap(20));
  out.push(H.sub('b', 'Children at 10 tables?   ______        (c)  Tables for 20 children?   ______'));
  out.push(H.sub('d', [TH(), H.t('Why does the number of children go up by 2 each time?')]));
  out.push(...H.lines(1));
  out.push(H.q(6, 'Ali counts in 3s: 3, 6, 9 … Mei counts in 4s: 4, 8, 12 … Which numbers from 1 to 36 do they BOTH say? Make two lists.', { keepNext: true }));
  out.push(H.sub('a', 'Ali:  3,  6,  9,  ____________________________________'));
  out.push(H.sub('b', 'Mei:  4,  8,  12,  ___________________________________'));
  out.push(H.sub('c', 'Both say:   ______________      What do you notice?   ______________'));
  return out;
};

module.exports = { lesson, script, deck, qbank, workbook };
