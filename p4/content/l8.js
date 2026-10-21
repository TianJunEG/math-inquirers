// Math Inquirers P4 Holiday Program — Lesson 8: Symmetry and Nets
const N = '#1B2A49', Y = '#FFC93C', SKY = '#DDEBF7', TEAL = '#1F7A6F', RED = '#D64545', WH = '#FFFFFF';
const F = 'Fredoka, Arial, sans-serif';

// ---------- drawing helpers ----------
const svg = (w, h, label, inner) => `<svg aria-label="${label}" viewBox="0 0 ${w} ${h}" width="${w}" xmlns="http://www.w3.org/2000/svg" style="max-width:100%">${inner}</svg>`;
const tx = (x, y, s, size = 18, fill = N, anchor = 'middle', weight = 700) => `<text x="${x}" y="${y}" font-size="${size}" font-weight="${weight}" text-anchor="${anchor}" fill="${fill}" font-family="${F}">${s}</text>`;
const grid = (x0, y0, cols, rows, c, op = 0.25) => {
  let d = '';
  for (let i = 0; i <= cols; i++) d += `M${x0 + i * c} ${y0} V${y0 + rows * c} `;
  for (let j = 0; j <= rows; j++) d += `M${x0} ${y0 + j * c} H${x0 + cols * c} `;
  return `<path d="${d}" stroke="${N}" stroke-width="1" opacity="${op}" fill="none"/>`;
};
// cells: [[x,y], ...]; labels: {'x,y': text}
const net = (cells, c, x0, y0, labels = {}, fill = SKY, size = 20) => cells.map(([x, y]) => {
  const t = labels[x + ',' + y];
  return `<rect x="${x0 + x * c}" y="${y0 + y * c}" width="${c}" height="${c}" fill="${fill}" stroke="${N}" stroke-width="2.5"/>` +
    (t !== undefined ? tx(x0 + x * c + c / 2, y0 + y * c + c / 2 + size * 0.36, t, size) : '');
}).join('');
const dims = cells => [Math.max(...cells.map(a => a[0])) + 1, Math.max(...cells.map(a => a[1])) + 1];
const row4 = y => [[0, y], [1, y], [2, y], [3, y]];

// Q1: six shapes made of 6 squares (A, C, E fold into a cube)
const Q1NETS = [
  ['A', [...row4(1), [1, 0], [1, 2]]],
  ['B', [...row4(1), [0, 0], [2, 0]]],
  ['C', [[0, 0], [1, 0], [2, 0], [2, 1], [3, 1], [4, 1]]],
  ['D', [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [1, 0]]],
  ['E', [[0, 0], [1, 0], [1, 1], [2, 1], [2, 2], [3, 2]]],
  ['F', [[0, 0], [1, 0], [0, 1], [1, 1], [2, 1], [3, 1]]]
];
const q1Svg = () => {
  const c = 20, pw = 200, ph = 84;
  let s = '';
  Q1NETS.forEach(([L, cells], i) => {
    const px = (i % 3) * pw, py = Math.floor(i / 3) * ph, [w, h] = dims(cells);
    s += `<rect x="${px + 4}" y="${py + 4}" width="${pw - 8}" height="${ph - 8}" rx="10" fill="${WH}" stroke="${N}" stroke-width="1.5" opacity="0.9"/>`;
    s += tx(px + 22, py + 26, L, 20, TEAL) + `<rect x="${px + 12}" y="${py + 36}" width="22" height="22" rx="4" fill="${WH}" stroke="${N}" stroke-width="2"/>`;
    s += net(cells, c, px + 44 + (150 - w * c) / 2, py + (ph - h * c) / 2, {}, SKY);
  });
  return svg(600, 2 * ph, 'Six shapes made of 6 squares, labelled A to F, each with a tick box', s);
};
// Q2: net with letters (A–E, B–D, C–F opposite)
const side = (fig, w, inner) => `<div class="p sub" style="display:flex;gap:12px;align-items:flex-start;margin-bottom:4px;padding-left:0"><div style="flex:1;min-width:0">${inner}</div><div style="flex:none;width:${w}px">${fig}</div></div>`;
const q2Svg = () => {
  const c = 36, cells = [[0, 0], [0, 1], [1, 1], [2, 1], [2, 2], [3, 2]];
  const lab = { '0,0': 'A', '0,1': 'B', '1,1': 'C', '2,1': 'D', '2,2': 'E', '3,2': 'F' };
  return svg(4 * c + 8, 3 * c + 8, 'A net of a cube with faces lettered A to F', net(cells, c, 4, 4, lab, SKY, 22));
};
// Q3: two dice nets with some numbers missing
const q3Svg = () => {
  const c = 30;
  const a = [...row4(1), [0, 0], [3, 2]], la = { '0,0': '1', '2,1': '4', '3,1': '2', '0,1': '', '1,1': '', '3,2': '' };
  const b = [[0, 0], [1, 0], [1, 1], [2, 1], [2, 2], [3, 2]], lb = { '0,0': '5', '1,1': '1', '2,2': '3' };
  let s = tx(70, 22, '(a)', 18, TEAL) + net(a, c, 70, 32, la, WH, 24) + tx(350, 22, '(b)', 18, TEAL) + net(b, c, 350, 32, lb, WH, 24);
  return svg(600, 3 * c + 40, 'Two dice nets. Net (a) shows 1, 4 and 2. Net (b) shows 5, 1 and 3. The other squares are empty.', s);
};
// Q4: complete the symmetric figures (only half is drawn)
const half = (pts, c, x0, y0) => `<polyline points="${pts.map(([a, b]) => `${x0 + a * c},${y0 + b * c}`).join(' ')}" fill="none" stroke="${N}" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>`;
const q4Svg = () => {
  const c = 20, ax = 30, ay = 30, bx = 330, by = 30;
  let s = tx(ax, 18, '(a)', 18, TEAL, 'start') + grid(ax, ay, 10, 7, c) + `<line x1="${ax + 5 * c}" y1="${ay - 10}" x2="${ax + 5 * c}" y2="${ay + 7 * c + 10}" stroke="${RED}" stroke-width="3" stroke-dasharray="8 6"/>`;
  s += half([[5, 0], [3, 2], [3, 5], [1, 7], [4, 7], [5, 6]], c, ax, ay);
  s += tx(bx, 18, '(b)', 18, TEAL, 'start') + grid(bx, by, 10, 8, c) + `<line x1="${bx - 10}" y1="${by + 4 * c}" x2="${bx + 10 * c + 10}" y2="${by + 4 * c}" stroke="${RED}" stroke-width="3" stroke-dasharray="8 6"/>`;
  s += half([[1, 4], [0, 2], [3, 3], [6, 1], [9, 2], [10, 4]], c, bx, by);
  return svg(600, by + 8 * c + 14, 'Two half figures on grids. (a) half a rocket on the left of an up-down dashed line. (b) the top half of a fish above an across dashed line.', s);
};
// Q5: lines of symmetry
const Q5SH = [['a', [[0, 0], [1, 0], [2, 0], [1, 1], [1, 2]]], ['b', [[0, 0], [2, 0], [0, 1], [1, 1], [2, 1], [0, 2], [2, 2]]], ['c', [[1, 0], [0, 1], [1, 1], [2, 1], [1, 2]]], ['d', [[1, 0], [2, 0], [0, 1], [1, 1]]]];
const q5Svg = () => {
  const c = 26, pw = 150;
  let s = '';
  Q5SH.forEach(([L, cells], i) => {
    const [w, h] = dims(cells), px = i * pw;
    s += tx(px + 14, 20, `(${L})`, 18, TEAL, 'start') + net(cells, c, px + (pw - w * c) / 2, 30 + (3 * c - h * c) / 2, {}, Y);
  });
  return svg(600, 3 * c + 40, 'Four shapes made of squares: (a) a T shape, (b) an H shape, (c) a plus shape, (d) a zigzag of 4 squares', s);
};
// Q6: 4 by 4 grids, columns A–D and rows 1–4, B2 B3 C2 C3 D2 shaded, two dashed lines
const q6Grid = (x0, y0, c) => {
  const sh = [[1, 1], [1, 2], [2, 1], [2, 2], [3, 1]];
  let s = '';
  for (let x = 0; x < 4; x++) for (let y = 0; y < 4; y++) {
    const on = sh.some(([a, b]) => a === x && b === y);
    s += `<rect x="${x0 + x * c}" y="${y0 + y * c}" width="${c}" height="${c}" fill="${on ? TEAL : WH}" stroke="${N}" stroke-width="2"/>`;
  }
  'ABCD'.split('').forEach((L, i) => { s += tx(x0 + i * c + c / 2, y0 - 8, L, 16, N); });
  [1, 2, 3, 4].forEach((n, i) => { s += tx(x0 - 10, y0 + i * c + c / 2 + 6, n, 16, N); });
  s += `<line x1="${x0 + 2 * c}" y1="${y0 - 22}" x2="${x0 + 2 * c}" y2="${y0 + 4 * c + 12}" stroke="${RED}" stroke-width="3" stroke-dasharray="7 5"/>`;
  s += `<line x1="${x0 - 22}" y1="${y0 + 2 * c}" x2="${x0 + 4 * c + 12}" y2="${y0 + 2 * c}" stroke="${RED}" stroke-width="3" stroke-dasharray="7 5"/>`;
  return s;
};
const q6Svg = () => svg(600, 4 * 26 + 50, 'Three copies of a 4 by 4 grid with columns A to D and rows 1 to 4. Squares B2, B3, C2, C3 and D2 are shaded. An up-down dashed line and an across dashed line go through the middle.',
  [50, 250, 450].map(x => q6Grid(x, 34, 26)).join(''));

module.exports = {
  lesson: {
    n: 8, week: 4, session: 'B', title: 'Symmetry and Nets', topic: 'Symmetry and Nets',
    objective: 'Decide whether a shape made of 6 squares folds into a cube by folding it in your head, find which faces of a net are opposite (and use it for dice), complete a figure so that a given line is a line of symmetry, find all the lines of symmetry of a shape, and shade squares to make a pattern symmetric.',
    skills: 'Visualising (folding in your head), making a list in order, testing every case, explaining why',
    materials: 'Squared paper (2 cm squares), scissors, sticky tape, 6 paper squares per child, a dice, a small mirror (optional), mini whiteboards, coloured pencils.',
    online: 'Children cut out 6 paper squares and a few 2 cm grid strips before the lesson and fold on camera; the tutor clicks to reveal each fold on the slides and shades the grids.',
    warmup: 'Fold It in Your Head: the tutor shows a capital letter drawn on squares (H, T, E, L, U, Z). Children show with fingers how many lines of symmetry it has, then explain where the fold line goes.',
    explore: 'Pairs join 6 paper squares edge to edge, cut the shape out and try to fold it into a cube with no gaps and no overlaps. They record every shape that works on squared paper and look for what the failures have in common.',
    mini: 'Fold a net in your head: choose a base, fold up the squares that touch it as walls, then see where the others swing to. A net works when there is exactly one base, one lid and four walls. Opposite faces: in a straight line of 3 squares, the two ends are opposite; at the two ends of a step (a zigzag of 4), the ends are opposite; the last pair is what is left. On a dice, opposite faces add up to 7. Before page 2: complete a symmetric figure by counting squares from the line to each corner; a rectangle has 2 lines of symmetry, not 4 (the diagonal fold does not match); shade squares so every shaded square has a partner the same distance from the line.',
    share: 'Mei says: "Every shape made of 6 squares folds into a cube." Ben says: "If a shape has 4 squares in a row, it always folds into a cube." Who is right?',
    exit: { q: 'This dice net shows 1, 3 and 2. Which number goes in the square marked "?"', a: '4. The "?" square is opposite the 3 (the ends of a step), and 3 + 4 = 7.' },
    mistakes: [
      'Thinking any 6 squares make a cube, and ticking shapes with a 2 by 2 block, 5 squares in a row, or two squares that close the same end.',
      'Saying the two squares next to each other in a net are opposite, instead of the squares with one square between them.',
      'Saying a rectangle has 4 lines of symmetry (including the diagonals), or completing a symmetric figure by copying (sliding) the half instead of flipping it.'
    ],
    extension: 'How many different nets of a cube are there? (11, if turned or flipped copies count as the same.) Draw as many as you can on squared paper.',
    key: [
      ['Q1', '(a) 3 shapes: A, C and E; one shape that does not fold, with a reason, for example: B has two squares on the same side of the row of 4, so both close the same end. D has 5 squares in a row: the 5th lands on the 1st. F has a 2 by 2 block: 4 squares meet at one corner, but only 3 faces of a cube meet at a corner.'],
      ['Q2', 'Opposite A: E.  Opposite B: D.  Opposite C: F.'],
      ['Q3', '(a) The long row reads 3, 5, 4, 2 (left to right) and the square below the right end is 6.  (b) Top row 5, 4; middle row 1, 2; bottom row 3, 6.  (c) 1 and 6 are the ends of a step, so they are opposite and add up to 7.'],
      ['Q4', '(a) Rocket: flip each corner across the dashed line, the same number of squares on the other side: shoulders 2 squares to the right of the line, fin tips 4 squares to the right at the bottom, bottom edge ends 1 square right of the line, notch on the line, then join.  (b) Fish: flip each corner below the line, the same number of squares: tail tip 2 below, then 1 below, back 3 below, 2 below, nose on the line.'],
      ['Q5', '(a) 1 (up-down)  (b) 2 (up-down and across)  (c) 4 (up-down, across and both corner-to-corner)  (d) 0'],
      ['Q6', '2 ways: shade A2 (the up-down line becomes a line of symmetry) or shade D3 (the across line becomes a line of symmetry). No other square works.']
    ]
  },

  script: {
    hook: ['Welcome, Shape Detectives! Today we fold things: paper into cubes, and pictures in half in our heads.', 'Some shapes made of 6 squares fold into a perfect cube and some do not. By the end you will be able to tell which, without cutting. Notice it. Test it. Explain why.'],
    warmIntro: ['I will show a letter made of squares. Imagine folding it so the two halves match exactly. How many different ways can you fold it? Show me with your fingers.', 'Then tell me where the fold line goes: up and down, or across?'],
    predict: ['You have 6 squares. Do you think EVERY shape you make with them will fold into a cube? Write yes or no in the corner of your whiteboard.'],
    exploreHints: ['Stuck: start with 4 squares in a row, which wrap round to make the walls. Where can the other two go?', 'Not sure if it is new: "Is it the same as one we have, just turned or flipped over?"', 'Finished early: find a shape that does NOT fold. Why does it fail?'],
    think: [
      '“I choose a base: a square with lots of neighbours. The squares touching it fold up and become walls: left, right and back. This square is joined to the right wall, so when the right wall stands up it swings round to the front. The last square folds over the top: the lid. One base, four walls, one lid. It works.”',
      '“This one: base in the middle. Two walls go up, front and back. This square hangs from the back wall and swings round to the left. But this other one hangs from the front wall and ALSO swings to the left. Two squares in the same place, and nothing on the right. Not a net.”',
      '“Opposite faces: in a straight line of 3, the two ends are opposite, because the middle one folds between them. At the two ends of a step, the ends are opposite too. Then the last two letters must be the last pair.”'
    ],
    circulate: ['Ask: “Which square is your base? Which ones become walls?”', 'Ask: “Which face lands on top of this one? Is anything already there?”', 'Ask: “How many squares is this corner from the line? Where is its partner?”'],
    hints: ['Hint 1: “Shade the base. Fold the walls up one at a time with your finger.”', 'Hint 2: “Look for a straight line of 3 squares. The ends are opposite.”', 'Hint 3: “Count the squares from the dashed line to each corner. Put a dot the same number of squares on the other side.”'],
    talk: ['“Mei says every shape made of 6 squares folds into a cube. Ben says a shape with 4 squares in a row always does. Who is right?”', '“How can you tell two faces are opposite without folding?”'],
    talkAns: 'Neither is right. A 2 by 3 rectangle has 6 squares but does not fold into a cube (Mei is wrong). A row of 4 with both extra squares on the same side does not fold either, because both close the same end (Ben is wrong). In a straight line of 3 squares, the two ends are opposite.',
    close: ['“You folded cubes in your head today, and you found the hidden partners in symmetric shapes.”', '“Hand me your exit ticket and I will stamp your inquiry journal.”']
  },

  deck: {
    today: 'Find out which shapes fold into a cube, find opposite faces on a dice net, and complete symmetric figures.',
    warmGame: 'Fold It in Your Head. A letter made of squares appears. Show with your fingers how many lines of symmetry it has, then show where the fold goes.',
    warmQs: [['How many faces does a cube have?', '6'], ['How many edges?', '12'], ['How many corners?', '8'], ['On a dice, 1 is opposite 6 and 2 is opposite 5. What is opposite 3?', '4'], ['How many ways can you fold a rectangle (not a square) so the halves match?', '2']],
    expSetup: ['Take 6 paper squares.', 'Join them edge to edge (whole sides touching) and tape them.', 'Try to fold your shape into a cube: no gaps, no overlaps.', 'Draw every shape that works. Did any fail? Why?'],
    expPic: 'six loose paper squares, a cross-shaped net and a folded cube.',
    expAsk: [['How many different nets did your group find?', 'There are 11 altogether (turned or flipped copies are the same).'], ['What made a shape fail?', 'Two squares landed on the same face: for example a 2 by 2 block, 5 in a row, or two squares closing the same end.'], ['Do all nets have 4 squares in a row?', 'No. Some have rows of 3 (2 rows of 3), and the staircase has no more than 2 in a row.']],
    mini1: { head: 'Fold it in your head', body: ['Shade a base. The squares touching it fold up as walls.', 'A square joined to a wall swings round with it.', 'Is there one base, one lid and four walls?'], ans: 'Yes: it is a net of a cube. If two squares land in the same place, it is not.' },
    mini2: { head: 'Opposite faces', body: ['In a straight line of 3 squares, the ends are opposite.', 'The two ends of a step are opposite.', 'The last two faces are the last pair.'], ans: 'On a dice, opposite faces add up to 7.' },
    keyHead: 'Key idea: fold it in your head', keyBig: 'A net works when it has one base, one lid and four walls with nothing overlapping. In a line of 3, the ends are opposite.', keySmall: 'A line of symmetry: fold along it and the two halves match exactly.',
    brk: 'Mirror partner! The tutor moves slowly; you are the mirror. Raise your right hand when the tutor raises the left.',
    ws1: 'Page 1, in pairs: Q1 which shapes fold into a cube, Q2 opposite letters, Q3 dice nets.',
    ws2: 'Page 2, on your own: Q4 complete the symmetric figures, Q5 lines of symmetry, Q6 shade one more square.'
  },

  qbank: {
    core: [
      { q: 'Hold a box or a dice. How many faces, edges and corners does a cube have? Count them one by one.', a: '6 faces, 12 edges, 8 corners.' },
      { q: 'Fold a square piece of paper so that the two halves match exactly. How many different ways can you fold it like this? (Folds from corner to corner count too.)', a: '4 ways (across the middle both ways, and along both diagonals).' },
      { q: 'Now fold a rectangle that is not a square so that the two halves match exactly. How many different ways can you fold it?', a: '2 ways (across the middle both ways). Folding along a diagonal does not make the halves match.' },
      { q: 'Look at a dice. Opposite faces add up to 7. Which number is on the face opposite 2?', a: '5' },
      { q: 'Write the capital letters A, B, F, H, L and T on paper in big block letters. Which of them can be folded so that the two halves match exactly?', a: 'A, B, H and T. F and L cannot.' },
      { q: 'Tape 6 squares in a row. Can you fold the row into a cube with no gaps and no overlaps? What goes wrong?', a: 'No. Four squares wrap round to make the walls, but the 5th and 6th land on top of the 1st and 2nd, and two ends are left open.' }
    ],
    stretch: [
      { q: 'A cuboid is 3 cm long, 2 cm wide and 1 cm high. Its net is drawn on 1 cm squared paper. How many squares does the net cover?', a: '22 squares: 2 faces of 3 by 2 (6 each), 2 faces of 3 by 1 (3 each) and 2 faces of 2 by 1 (2 each). 12 + 6 + 4 = 22.' },
      { q: 'Ben puts a dice on the table. The top face shows 3 and the front face shows 5. What numbers are on the bottom face and on the back face?', a: 'Bottom 4 (3 + 4 = 7). Back 2 (5 + 2 = 7).' },
      { q: 'A dice is on a table. Mei walks round it and can see the top and the four side faces. The numbers she can see add up to 19. What number is on the bottom face?', a: '2. All six faces add up to 1 + 2 + 3 + 4 + 5 + 6 = 21, and 21 − 19 = 2.' },
      { q: 'There are 5 different shapes made of 4 squares joined edge to edge (a line, a square, an L, a T and a zigzag). Which one has exactly 1 line of symmetry?', a: 'Only the T. The line has 2, the square has 4, the L and the zigzag have 0.' },
      { q: 'Can a 2 by 3 rectangle of squares fold into a cube? Explain.', a: 'No. It has a 2 by 2 block of squares: 4 squares meet at one corner, but on a cube only 3 faces meet at a corner, so two of them would overlap.' },
      { q: 'Which shape made of 5 squares joined edge to edge has exactly 2 lines of symmetry?', a: 'Only the row of 5 squares (one line up-down through the middle square and one line along the row).' },
      { q: 'Ben folds a net into a cube. Each face is a different colour. How many faces can touch the red face along an edge? Could 5 faces touch it?', a: '4 faces touch it. 5 cannot: the face opposite red never touches it.' },
      { q: 'On a 3 by 3 grid of squares, shade 3 squares so that the pattern has exactly 1 line of symmetry. Then shade 2 squares so that the pattern has exactly 2 lines of symmetry. Draw both patterns.', a: 'Answers vary. One line: for example the whole top row (3 squares), or the top-left, top-right and centre squares. Two lines: the top-middle and bottom-middle squares, or the left-middle and right-middle squares, or two opposite corners.' }
    ],
    challenge: [
      { q: 'Two dice are glued together face to face, and the two glued faces show the same number. The numbers on all the faces you can still see add up to 36. What number is on the glued faces?', a: '3. Two dice have 21 + 21 = 42 altogether. The hidden faces add up to 42 − 36 = 6, and they show the same number, so each is 3.' },
      { q: 'Show why a net of a cube can never have 5 squares in a row. What is the most squares in a row a net can have?', a: 'With 5 in a row, four squares wrap round to make a ring of walls and the 5th lands on top of the 1st, so two squares share a face and no face is left for the other end. The most is 4 in a row (for example the cross-shaped net).' },
      { q: 'An open box (a cube with no lid) is made from 5 squares. Of the 12 different shapes made of 5 squares joined edge to edge, how many fold into an open box? (Turned or flipped copies count as the same.)', a: '8. Only 4 shapes do not fold: the row of 5, the V (an L with arms of 3 and 3), the U (a C shape) and the P (a 2 by 2 block with one extra square).' },
      { q: 'Three dice are stacked in a tower on a table. The top face of the tower shows 5. What is the total of the numbers on all the faces you cannot see (the faces touching each other and the table)?', a: '16. The top dice: its bottom is 2 (5 + 2 = 7). The middle dice: top and bottom are opposite, 7. The bottom dice: top and bottom, 7. 2 + 7 + 7 = 16.' },
      { q: 'Ali says: "On a dice, the numbers on the 4 side faces always add up to 14." Is he right? Explain.', a: 'Yes. The 4 side faces are two opposite pairs, and each pair adds up to 7: 7 + 7 = 14.' },
      { q: 'A cube has faces numbered 1 to 6 (not a normal dice). Face 1 touches faces 2, 3, 4 and 5. Face 2 touches faces 1, 3, 5 and 6. Which face is opposite 1? Opposite 2? Opposite 3?', a: 'Opposite 1 is 6 (the only face it does not touch). Opposite 2 is 4. That leaves 3 and 5, so opposite 3 is 5.' },
      { q: 'Design your own dice. Draw a net of a cube that is not one of the nets in this lesson, and write the numbers 1 to 6 on it so that opposite faces add up to 7. Name each pair of opposite faces to prove it works. Then rub out two numbers and challenge a partner to put them back.', a: 'Designs will vary: check each pair of opposite faces on the net adds up to 7. Model: a row of four squares 2, 1, 5, 6 with a 3 above the 1 and a 4 below the 1. Opposite pairs: 2 and 5, 1 and 6 (first and third, second and fourth in the row), and 3 and 4 (above and below).' },
      { q: 'In how many ways can you shade exactly 2 squares of a 3 by 3 grid so that the up-down line through the middle is a line of symmetry?', a: '6. Both squares in the middle column: 3 ways. One square in each side column, in the same row: 3 ways.' },
      { q: 'Shade exactly 5 squares of a 3 by 3 grid so that the pattern has 4 lines of symmetry. There are 2 ways. Find both.', a: 'The middle square and the 4 corners (an X), or the middle square and the 4 edge-middle squares (a plus).' }
    ]
  },

  workbook: H => {
    const W = [];
    W.push(H.q(1, 'Each shape is made of 6 squares. Which ones fold into a cube? Tick them.', { before: 40, keepNext: true }));
    W.push(H.fig(q1Svg()));
    W.push(H.sub('a', 'Shapes ticked: ____     Shape that does NOT fold: ____ . Explain why:'));
    W.push(...H.lines(1));
    W.push(H.q(2, 'This net folds into a cube. Which letter is opposite …', { keepNext: true }));
    W.push(side(q2Svg(), 160, [H.sub('a', 'A?  ________', { after: 40 }), H.sub('b', 'B?  ________', { after: 40 }), H.sub('c', 'C?  ________')].join('')));
    W.push(H.q(3, 'On a dice, the numbers on opposite faces add up to 7. Write the missing numbers on each dice net.', { keepNext: true }));
    W.push(H.fig(q3Svg()));
    W.push(H.sub('', 'In net (b), how did you find the number opposite 1?  ____________________________'));

    W.push(H.q(4, 'Complete each figure so that the dashed line is a line of symmetry.', { pb: true, before: 0, keepNext: true }));
    W.push(H.fig(q4Svg()));
    W.push(H.sub('', 'Count the squares from the line to each corner. Put a dot the same number of squares on the other side, then join the dots.'));
    W.push(H.q(5, 'Draw ALL the lines of symmetry on each shape. Then write how many.', { keepNext: true }));
    W.push(H.fig(q5Svg()));
    W.push(H.sub('', '(a) ________      (b) ________      (c) ________      (d) ________'));
    W.push(H.q(6, 'Shade ONE more square so that a dashed line becomes a line of symmetry of the shaded squares. Find ALL the ways. Use a new grid for each.', { keepNext: true }));
    W.push(H.fig(q6Svg()));
    W.push(H.sub('a', 'The squares I shaded (like A1):  ______________        How many ways?  ________'));
    W.push(H.sub('b', 'Choose a square that does NOT work. Where would its partner have to be?'));
    W.push(...H.lines(1));
    return W;
  }
};
