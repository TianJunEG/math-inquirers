// Math Inquirers P3 – Lesson 7: Area Architects (Area and perimeter)
// Heuristics taught: (1) make a list in order; (2) change the shape (push the steps out; cut it up or fill it in).
const N = '#1B2A49', Y = '#FFC93C', S = '#DDEBF7', G = '#1F7A6F', W = '#FFFFFF', LG = '#B9C6DE';

// ---------- small SVG helpers for the workbook ----------
const svg = (w, h, body, label, dw) => `<svg viewBox="0 0 ${w} ${h}" width="${dw || w}" role="img" aria-label="${label}" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto">${body}</svg>`;
const txt = (x, y, s, o = {}) => `<text x="${x}" y="${y}" font-size="${o.size || 18}" font-weight="${o.w || 700}" text-anchor="${o.anchor || 'middle'}" fill="${o.fill || N}" font-family="Fredoka, Arial, sans-serif">${s}</text>`;
// light background grid: cols x rows squares of size c, top-left (x, y)
const bgGrid = (x, y, cols, rows, c) => {
  let d = '';
  for (let i = 0; i <= cols; i++) d += `M${x + i * c} ${y}V${y + rows * c}`;
  for (let j = 0; j <= rows; j++) d += `M${x} ${y + j * c}H${x + cols * c}`;
  return `<path d="${d}" stroke="${LG}" stroke-width="1.2" fill="none"/>`;
};
// a figure made of grid squares: shaded squares, thin inner lines, thick outline (only edges not shared)
const cellsFig = (cells, x0, y0, c, fill = S) => {
  const has = new Set(cells.map(([a, b]) => a + ',' + b));
  let r = '', d = '';
  cells.forEach(([a, b]) => {
    const x = x0 + a * c, y = y0 + b * c;
    r += `<rect x="${x}" y="${y}" width="${c}" height="${c}" fill="${fill}" stroke="${N}" stroke-width="1"/>`;
    if (!has.has(a + ',' + (b - 1))) d += `M${x} ${y}H${x + c}`;
    if (!has.has(a + ',' + (b + 1))) d += `M${x} ${y + c}H${x + c}`;
    if (!has.has((a - 1) + ',' + b)) d += `M${x} ${y}V${y + c}`;
    if (!has.has((a + 1) + ',' + b)) d += `M${x + c} ${y}V${y + c}`;
  });
  return r + `<path d="${d}" stroke="${N}" stroke-width="3.5" stroke-linecap="square" fill="none"/>`;
};

// Q1 figures (x right, y down), each square 1 cm
const FA = [[0, 0], [1, 0], [2, 0], [3, 0], [0, 1], [1, 1], [2, 1], [3, 1]];          // 4 by 2: area 8, perimeter 12
const FB = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [0, 1], [1, 1], [2, 1]];          // 5 on top, 3 below: area 8, perimeter 14
const FC = [[0, 0], [1, 0], [2, 0], [0, 1], [1, 1], [2, 1], [0, 2], [1, 2], [2, 2]];  // 3 by 3: area 9, perimeter 12
const FD = [[0, 0], [2, 0], [0, 1], [1, 1], [2, 1]];                                  // U shape: area 5, perimeter 12
const sh = (cells, dx, dy) => cells.map(([a, b]) => [a + dx, b + dy]);
const q1Fig = () => {
  const c = 26, x0 = 14, y0 = 6;
  let b = bgGrid(x0, y0, 22, 5, c);
  b += cellsFig(sh(FA, 1, 1), x0, y0, c) + cellsFig(sh(FB, 6, 1), x0, y0, c) + cellsFig(sh(FC, 12, 1), x0, y0, c) + cellsFig(sh(FD, 17, 1), x0, y0, c);
  [['A', 3], ['B', 8.5], ['C', 13.5], ['D', 18.5]].forEach(([l, cx]) => { b += txt(x0 + cx * c, y0 + 5 * c + 26, l, { size: 22 }); });
  return svg(600, 170, b, 'Four figures on a 1 cm square grid: A is a 4 by 2 rectangle; B has 5 squares on top and 3 below; C is a 3 by 3 square; D is a U shape of 5 squares', 500);
};
// Q3: L-shape, 10 cm by 7 cm with a 4 cm by 3 cm corner cut away (scale 22 px per cm)
const q3Fig = () => {
  const k = 22, x0 = 80, y0 = 34;
  const P = [[0, 0], [6, 0], [6, 3], [10, 3], [10, 7], [0, 7]].map(([a, b]) => `${x0 + a * k},${y0 + b * k}`).join(' ');
  let b = `<polygon points="${P}" fill="${S}" stroke="${N}" stroke-width="3.5" stroke-linejoin="miter"/>`;
  const o = { size: 22 };
  b += txt(x0 + 3 * k, y0 - 10, '6 cm', o) + txt(x0 - 12, y0 + 3.5 * k + 7, '7 cm', { size: 22, anchor: 'end' }) + txt(x0 + 5 * k, y0 + 7 * k + 28, '10 cm', o) + txt(x0 + 10 * k + 12, y0 + 5 * k + 7, '4 cm', { size: 22, anchor: 'start' });
  return svg(380, 222, b, 'An L-shaped figure. Bottom 10 cm, left side 7 cm, top 6 cm, right side 4 cm. The step in the top right corner has no lengths marked.', 320);
};
// Q4: staircase 4, 3, 2, 1 squares high
const q4Fig = () => {
  const c = 30, x0 = 10, y0 = 6;
  const cells = []; [4, 3, 2, 1].forEach((h, i) => { for (let k = 0; k < h; k++) cells.push([1 + i, 4 - k]); });
  return svg(200, 190, bgGrid(x0, y0, 6, 6, c) + cellsFig(cells, x0, y0, c), 'A staircase figure on a 1 cm grid: columns of 4, 3, 2 and 1 squares standing side by side', 170);
};
// Q5: L of 4 squares, drawn twice (for a and b)
const q5Fig = () => {
  const c = 30, L = [[2, 1], [2, 2], [2, 3], [3, 3]];
  let b = '';
  [[40, '(a)'], [340, '(b)']].forEach(([x0, l]) => { b += txt(x0 + 90, 24, l, { size: 24 }) + bgGrid(x0, 32, 6, 5, c) + cellsFig(L, x0, 32, c); });
  return svg(600, 190, b, 'Two copies of an L shape made of 4 squares on a 1 cm grid: 3 squares in a column with 1 more square to the right of the bottom one', 520);
};
module.exports = {
  lesson: {
    n: 7, week: 4, session: 'A', title: 'Area Architects', topic: 'Area and Perimeter',
    objective: 'Find the area and perimeter of figures made of squares and rectangles, find every rectangle with a given perimeter by listing in order, and use “change the shape” (push the steps out; cut up or fill in) to find perimeters and areas quickly.',
    skills: 'Systematic listing, changing the shape, spatial reasoning, explaining',
    materials: '12 square tiles (or 12 squares cut from 1 cm grid paper) per child, 1 cm grid paper, mini whiteboards, a ruler. For the sneak-peek puzzles: paper, a pencil and a few counters or small objects for each child.',
    online: 'Children cut 12 squares from squared paper (or draw on squared paper) and check them against the grid slide the tutor shares; nothing is held up to the camera.',
    warmup: 'Area or perimeter? The tutor reads a job (fence a garden, tile a floor). Children trace a finger round the edge for perimeter or wipe a flat palm for area. Then quick questions on squares and rectangles.',
    explore: 'Use exactly 12 squares to make every different rectangle. Record the length, width and perimeter of each. Which has the longest perimeter? The shortest?',
    mini: 'List rectangles with a perimeter of 20 cm in order (length + width = 10). Push the steps of a staircase out to see it has the same perimeter as a rectangle; watch out for dents. Find the area of an L-shape two ways: cut it into rectangles, or fill in the corner and take it away. Before page 1: a square with the same perimeter as a rectangle. Before page 2: what happens to the perimeter when one square is added.',
    share: 'Two gardens have the same perimeter. Must they have the same area? Give an example.',
    exit: { q: 'A rectangle has a perimeter of 12 cm. Its length is 4 cm. What is its area?', a: '8 cm² (width 2 cm because 4 + 2 = 6, half of 12)' },
    mistakes: ['Mixing up area and perimeter, or writing cm for an area (it is cm²).', 'Counting the squares along the edge instead of the edges (for perimeter, count the sides of the squares, not the squares).', 'Pushing out the sides of a shape with a dent: the two walls of a dent must be added on.'],
    extension: 'Find all the rectangles with whole-cm sides and a perimeter of 24 cm. Which has the biggest area? (11 by 1, 10 by 2, 9 by 3, 8 by 4, 7 by 5, 6 by 6; the 6 by 6 square, 36 cm²)',
    key: [
      ['Q1', 'A: 8 cm², 12 cm.  B: 8 cm², 14 cm.  C: 9 cm², 12 cm.  D: 5 cm², 12 cm.  (a) A and B (both 8 cm²).  (b) A, C and D (all 12 cm).'],
      ['Q2', 'Length + width = 9 m: 8 by 1 (8 m²), 7 by 2 (14 m²), 6 by 3 (18 m²), 5 by 4 (20 m²). 4 gardens. Biggest area: 5 m by 4 m, 20 m².'],
      ['Q3', 'Rectangle perimeter 7 + 3 + 7 + 3 = 20 cm. Square side 20 ÷ 4 = 5 cm. Area 5 × 5 = 25 cm².'],
      ['Q4', 'Missing sides 4 cm (10 − 6) and 3 cm (7 − 4). (a) Area 58 cm² (6 × 7 + 4 × 4 = 42 + 16, or 10 × 7 − 4 × 3 = 70 − 12).  (b) Perimeter 34 cm (push the step out: 10 + 7 + 10 + 7).'],
      ['Q5', '(a) 10 cm²  (b) 16 cm  (c) The perimeter stays 16 cm (same as the 4 by 4 square); the area goes up by 6 cm² to 16 cm².'],
      ['Q6', '(a) Any square that touches the L along only one side, e.g. above the top square: perimeter 12 cm.  (b) Only one place: the square to the right of the middle square (it touches 2 sides).  (c) No. To make 8 cm the new square would have to touch 3 sides of the L, and there is no such gap.']
    ]
  },

  script: {
    hook: ['Today you are architects. Architects plan rooms, gardens and fences, so they need two numbers: how much space is inside (the area) and how long the edge is (the perimeter).', 'Here is a puzzle to keep in your head: can two gardens have the same fence but different amounts of grass? Let us find out.'],
    warmIntro: ['When I read a job, show me with your hand. If the job goes round the edge, trace a finger round the edge in the air: perimeter. If the job covers the inside, wipe your flat palm: area.', 'Ready? Job 1: put a fence round a garden.'],
    predict: ['You have 12 squares. You must use all of them to make a rectangle. Will every rectangle you make have the same perimeter? Thumbs up for yes, down for no. Write your guess on your whiteboard.'],
    exploreHints: ['Stuck: put 2 squares in each row. How many rows do you need for 12?', 'Not sure how to find the perimeter: run your finger round the edge and count every side of a square you pass.', 'Ready for more: can you make a rectangle with 12 squares that has a perimeter of 20 cm? (No: the perimeters are 26, 16 and 14 cm.)'],
    think: ['“Ravi has 20 m of fence. Half of it goes along one length and one width, so length + width = 10. I list in order: width 1, length 9; width 2, length 8; and so on. I stop at 5 and 5, because after that the rectangles just turn round.”', '“This staircase has short steps with no numbers. I do not need them! I push the top pieces up and the side pieces out. Now it is a rectangle with the same perimeter: 8 + 6 + 8 + 6 = 28 cm.”', '“For the area of an L-shape I cut it into two rectangles. Then I check another way: I fill in the missing corner and take it away. Both ways give 42 cm², so I trust my answer.”'],
    circulate: ['Ask: “Is that the area or the perimeter? Which unit goes with it?”', 'Ask: “How do you know you have found every rectangle?”', 'Ask: “Can you push the steps out? Is there a dent?”'],
    hints: ['Hint 1: “Draw it on the grid and count.”', 'Hint 2: “Half the perimeter is one length plus one width.”', 'Hint 3: “Cut the shape into rectangles. Find each area, then add.”'],
    talk: ['“Two gardens have the same perimeter. Must they have the same area? Show me an example.”', '“When does pushing out the steps NOT work?”'],
    talkAns: 'No. A 9 m by 1 m garden and a 5 m by 5 m garden both have a 20 m fence, but the areas are 9 m² and 25 m². Pushing out does not work when the shape has a dent: the two walls of the dent are extra.',
    close: ['“You listed in order so nothing was missed, and you changed the shape to make it easy. Real architects do the same. Well done!”']
  },

  deck: {
    today: 'Find every rectangle with the same perimeter, push steps out to find perimeters fast, and cut up or fill in shapes to find their area.',
    warmGame: 'Area or perimeter? Trace a finger round the edge for perimeter, wipe a flat palm for area: fence a garden, tile a floor, ribbon round a card, paint a wall, frame a photo, cover a book.',
    warmQs: [['8 × 7 = ?', '56'], ['A square has sides of 6 cm. What is its perimeter?', '24 cm'], ['A rectangle is 8 cm by 3 cm. What is its area?', '24 cm²']],
    takeHome: [['A square has an area of 49 cm². How long is each side?', '7 cm']],
    expSetup: ['Take 12 squares.', 'Make a rectangle using ALL 12 squares.', 'Record its length, width and perimeter in a table.', 'Make every different rectangle (there are three). Which has the longest perimeter?'],
    expPic: '12 loose squares and an empty table with columns Length, Width, Perimeter.',
    expAsk: [['How many different rectangles did you make?', '3: 12 by 1, 6 by 2 and 4 by 3 (turning one round does not make a new one).'], ['Do they all have the same perimeter?', 'No: 26 cm, 16 cm and 14 cm. Same area, different perimeters.'], ['Which has the longest perimeter? Why?', 'The long thin one (12 by 1): fewer squares touch, so more edges are on the outside.']],
    mini1: { head: 'Same fence, different gardens', table: [['Length', '9', '8', '7', '6', '5'], ['Width', '1', '2', '3', '4', '5'], ['Area (m²)', '9', '16', '21', '24', '25']], body: ['Ravi has 20 m of fence for a rectangular garden with whole-metre sides.', 'Length + width = 20 ÷ 2 = 10. List in order, width 1 first.', 'Which garden has the biggest area?'], ans: '5 gardens. 5 m by 5 m has the biggest area: 25 m².' },
    mini2: { head: 'Push the steps out', body: ['A staircase shape is 8 cm wide and 6 cm tall. The steps have no lengths marked.', 'Slide the pieces facing up to the top: together they make 8 cm. Slide the pieces facing right: together they make 6 cm.', 'What is the perimeter?'], ans: '8 + 6 + 8 + 6 = 28 cm' },
    keyHead: 'Key idea: list in order, change the shape',
    keyBig: 'Perimeter: push the steps out (but add the walls of a dent). Area: cut it into rectangles, or fill it in and take away.',
    keySmall: 'Same perimeter does not mean same area. List the rectangles in order to find them all.',
    brk: 'Perimeter march: march on the spot and trace a big square in the air, counting its 4 sides. Then stretch tall and thin like a 9 by 1 garden, then wide like a 5 by 5 garden.',
    ws1: 'Page 1, in pairs: Q1 area and perimeter on a grid, Q2 every rectangle with an 18 m fence, Q3 a square and a rectangle with the same perimeter.',
    ws2: 'Page 2, on your own: Q4 an L-shape with missing sides, Q5 a staircase, then Q6 add one square if you have time.'
  },

  qbank: {
    core: [
      { q: 'A rectangle is 9 cm long and 4 cm wide. Walk all the way round its edge: how far is that? (This distance is called the perimeter.) Draw it on squared paper if you like.', a: '26 cm (9 + 4 + 9 + 4)' },
      { q: 'Cover a rectangle 7 cm long and 6 cm wide with squares that are 1 cm by 1 cm. There are 6 rows with 7 squares in each row. How many squares cover it? (The number of squares is the area, in cm².)', a: '42 cm² (6 rows of 7)' },
      { q: 'A square has 4 equal sides. The distance all the way round it is 32 cm. How long is each side?', a: '8 cm (32 ÷ 4)' },
      { q: 'A square floor is covered with 36 small squares (1 cm by 1 cm), with the same number of squares in each row and each column. How many squares are there along one side? How far is it all the way round the edge?', a: '6 squares along one side (6 × 6 = 36), so the distance round is 6 + 6 + 6 + 6 = 24 cm.' },
      { q: 'A rectangle is covered by 40 small squares (1 cm by 1 cm), with 8 squares in each row. How many rows are there? How far is it all the way round the edge?', a: '5 rows (8 × 5 = 40). The distance round is 8 + 5 + 8 + 5 = 26 cm.' },
      { q: 'A figure is made of 7 squares, each 1 cm by 1 cm. What is its area? Can you say its perimeter without seeing it?', a: 'Area 7 cm². No: the perimeter depends on how the squares are joined (it can be 12, 14 or 16 cm).' }
    ],
    stretch: [
      { q: 'Find all the rectangles with whole-cm sides and an area of 24 cm². Which one has the shortest perimeter?', a: '24 by 1 (50 cm), 12 by 2 (28 cm), 8 by 3 (22 cm), 6 by 4 (20 cm). The 6 cm by 4 cm rectangle has the shortest perimeter.' },
      { q: 'A rectangle is 12 cm long. Its perimeter is 30 cm. Find its area.', a: 'Length + width = 15, so the width is 3 cm. Area 12 × 3 = 36 cm².' },
      { q: 'A rectangle 8 cm by 2 cm and a square have the same perimeter. Which has the bigger area, and by how much?', a: 'Perimeter 20 cm, so the square has sides of 5 cm. Square 25 cm², rectangle 16 cm². The square, by 9 cm².' },
      { q: 'A square with sides of 6 cm is cut into two rectangles of the same size. What is the perimeter of each rectangle?', a: 'Each rectangle is 6 cm by 3 cm, so its perimeter is 18 cm.' },
      { q: 'How many tiles 2 cm by 2 cm are needed to cover a mat 10 cm by 8 cm?', a: '5 tiles along and 4 tiles down: 20 tiles.' },
      { q: 'A rectangle has an area of 18 cm² and a perimeter of 18 cm. Find its length and width.', a: '6 cm and 3 cm (6 × 3 = 18 and 6 + 3 + 6 + 3 = 18).' },
      { q: 'Mei’s garden is 9 m by 5 m. Ali’s garden is 7 m by 7 m. Whose garden needs the longer fence? Whose has the bigger area?', a: 'Both fences are 28 m. Ali’s garden has the bigger area: 49 m² against 45 m².' },
      { q: 'Use exactly 6 squares (each 1 cm by 1 cm), whole sides touching. Draw a figure with a perimeter of 10 cm and one with a perimeter of 14 cm. What is the biggest perimeter possible?', a: '10 cm: only the 2 by 3 rectangle. 14 cm: any shape with no 2 by 2 block, e.g. a row of 6. 14 cm is the biggest: 6 squares have 24 sides, they need at least 5 touches to join, and each touch hides 2 sides (24 − 10 = 14).' }
    ],
    challenge: [
      { q: 'List every rectangle with whole-cm sides and a perimeter of 24 cm, with its area, in a table. What do you notice as the rectangle gets closer to a square? Use what you notice to predict the biggest area for a perimeter of 40 cm, then check.', a: '11 by 1 (11 cm²), 10 by 2 (20), 9 by 3 (27), 8 by 4 (32), 7 by 5 (35), 6 by 6 (36). The area grows as the sides get closer to each other, and the square has the biggest area. For 40 cm the square is 10 by 10, area 100 cm² (the next best, 11 by 9, is 99 cm²).' },
      { q: 'A rectangle is made of 2 same-size squares side by side. Its perimeter is 36 cm. What is its area?', a: 'The perimeter is 6 sides of a small square, so each side is 6 cm. Area 2 × 36 = 72 cm².' },
      { q: 'A rectangle 6 cm by 4 cm is cut into two rectangles with one straight cut that is parallel to one side. Find the total perimeter of the two pieces. Is there more than one answer?', a: 'Yes, two answers. A cut parallel to the 4 cm sides is 4 cm long: 20 + 4 + 4 = 28 cm. A cut parallel to the 6 cm sides is 6 cm long: 20 + 6 + 6 = 32 cm.' },
      { q: 'A square has a perimeter of 20 cm. Four of these squares are put together to make one big square. Find the perimeter and the area of the big square. The perimeter of the big square is not 4 times as long as 20 cm. Explain why, and why the area is 4 times as big.', a: 'Small side 5 cm, big side 10 cm. Perimeter 40 cm, area 100 cm² (a small square has area 25 cm²). The sides only double, so the perimeter only doubles (20 to 40). But the area counts all 4 small squares: 4 × 25 = 100 cm².' },
      { q: 'A rectangle is 10 m long and 8 m wide. A 4 m by 3 m rectangle is cut out of one corner. Find the area and the perimeter that are left. Then cut the same 4 m by 3 m rectangle out of the MIDDLE of one long side instead. Find the new area and perimeter. What stays the same and what changes?', a: 'Corner cut: area 80 − 12 = 68 m², perimeter 36 m (the same as the 10 by 8 rectangle: push the corner out). Notch in the middle of a long side: area 68 m² and perimeter 36 + 3 + 3 = 42 m (take away 4 m of edge and add 4 + 3 + 3). The area is the same in both, but the perimeter is different.' },
      { q: 'A square with sides of 8 cm is cut into four same-size squares. The four small squares are put in a row, touching whole sides. Find the perimeter of the row. Then compare with the perimeter of the big square and with the area of each shape. What stays the same and what changes?', a: 'Each small square has sides of 4 cm. The row is 16 cm by 4 cm, so its perimeter is 40 cm. The 8 cm square has a perimeter of 32 cm. The area is 64 cm² for both. The area stays the same but the perimeter goes up when the pieces are spread out.' },
      { q: 'Make up your own rectangle puzzle. Choose a rectangle with whole-cm sides, then give a partner only TWO clues about it (for example its area and its perimeter). Check that only ONE rectangle fits both clues. Which two clues did you choose, and why do they work?', a: 'Answers vary. Check that the clues fit the secret rectangle and that listing the rectangles for the first clue leaves exactly one for the second. Example: "Area 24 cm² and perimeter 20 cm". The rectangles with area 24 cm² are 24 by 1 (perimeter 50), 12 by 2 (28), 8 by 3 (22) and 6 by 4 (20), so only 6 by 4 fits.' },
      { q: 'Ali joins 5 same-size squares with sides of 2 cm, whole sides touching. What is the biggest perimeter his shape can have? The smallest?', a: 'Biggest 24 cm (12 sides of 2 cm, e.g. a row of 5). Smallest 20 cm (10 sides: a 2 by 2 square with one more square on a side).' },
      { q: 'A rectangle 7 cm by 5 cm has a 1 cm square cut out of each of its 4 corners. Find the new area and the new perimeter.', a: 'Area 35 − 4 = 31 cm². Perimeter still 24 cm: push the cut corners out and you get the 7 by 5 rectangle back.' }
    ]
  },

  workbook: H => {
    // figure on the left, questions on the right (keeps a question and its picture together on one page)
    const side = (fig, right) => `<div class="p img" style="display:flex;align-items:center;gap:22px;text-align:left"><div style="flex:none">${fig}</div><div style="flex:1">${right}</div></div>`;
    return [
      H.q(1, 'Each small square is 1 cm by 1 cm. Find the area (in cm²) and the perimeter (in cm) of each figure.', { before: 20, keepNext: true }),
      H.fig(q1Fig()),
      H.tbl([2475, 1856, 1856, 1857, 1856], [
        H.row(['Figure', 'A', 'B', 'C', 'D'].map((s, i) => H.cell(s, [2475, 1856, 1856, 1857, 1856][i], { bold: true, fill: 'EDEDED' }))),
        H.row([H.cell('Area (cm²)', 2475, { bold: true }), ...[1856, 1856, 1857, 1856].map(w => H.cell('\u00a0', w, { h: 30 }))]),
        H.row([H.cell('Perimeter (cm)', 2475, { bold: true }), ...[1856, 1856, 1857, 1856].map(w => H.cell('\u00a0', w, { h: 30 }))])
      ]),
      H.gap(20),
      H.sub('a', 'Which two figures have the same area but different perimeters?   ________'),
      H.sub('b', 'Which figures have the same perimeter but different areas?   ________'),
      H.q(2, 'Siti has 18 m of fence. She makes a rectangular garden with the whole fence. Each side is a whole number of metres. List ALL the gardens she can make, in order.', { keepNext: true }),
      H.tbl([2475, 2475, 2475, 2475], [
        H.row(['Length (m)', 'Width (m)', 'Check: perimeter', 'Area (m²)'].map(s => H.cell(s, 2475, { bold: true, fill: 'EDEDED' }))),
        ...[0, 1, 2, 3, 4].map(() => H.row([2475, 2475, 2475, 2475].map(w => H.cell('\u00a0', w, { h: 20 }))))
      ]),
      H.p('You may not need all the rows.', { after: 20 }),
      H.gap(20),
      H.sub('a', 'Which garden has the biggest area?   ______________'),
      H.q(3, 'A square has the same perimeter as a rectangle 7 cm long and 3 cm wide. Hint: first walk round the rectangle. What is the area of the square?   ____________ cm²', { after: 60 }),

      H.q(4, 'Find the two missing sides first. Then find the area and the perimeter of this figure. Hint: you can cut the figure into two rectangles.', { pb: true, before: 0, keepNext: true }),
      H.p('Missing sides: across = 10 − 6, down = 7 − 4.', { after: 20 }),
      side(q3Fig(), H.sub('', 'Missing sides:  ____ and ____') + H.sub('a', 'Area = __________ cm²') + H.sub('b', 'Perimeter = __________ cm')),
      H.q(5, 'Look at this staircase.', { keepNext: true }),
      side(q4Fig(), H.sub('a', 'What is its area?   ________ cm²') + H.sub('b', 'What is its perimeter?   ________ cm')),
      H.sub('c', 'Ben fills in the gaps with squares to make a 4 by 4 square. What happens to the perimeter? What happens to the area?'),
      ...H.lines(1),
      H.q(6, '(if time) This L shape is made of 4 squares. Its perimeter is 10 cm. Add ONE square that shares a whole side with the L. Shade it.', { keepNext: true }),
      H.fig(q5Fig()),
      H.sub('a', 'In grid (a), add a square so that the perimeter becomes 12 cm.'),
      H.sub('b', 'In grid (b), add a square so that the perimeter stays 10 cm.'),
      H.sub('c', 'Can you add one square so that the perimeter becomes 8 cm? Explain.   ________________')
    ];
  }
};
