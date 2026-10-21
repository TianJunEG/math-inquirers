// Math Inquirers P2, Lesson 8: Shape Builders (2D and 3D shapes)
// Counts checked by program: squares in grids, triangles in figures, cubes in stacks, and every net folded by rolling a cube over it.

const N = '#1B2A49', Y = '#FFC93C', SK = '#DDEBF7', TL = '#1F7A6F', W = '#FFFFFF';
const FONT = 'Fredoka, Arial, sans-serif';
const FR = (a, b) => `<span style="display:inline-flex;flex-direction:column;align-items:center;vertical-align:middle;line-height:1;margin:0 3px;font-size:.95em"><span style="padding:0 3px 2px;border-bottom:2px solid currentColor">${a}</span><span style="padding:2px 3px 0">${b}</span></span>`;
const rich = (H, s, o = {}) => {
  if (!H.TextRun || !H.t) return s.replace(/\{(\d+)\/(\d+)\}/g, '$1/$2');
  const out = []; const re = /\{(\d+)\/(\d+)\}/g; let m, last = 0;
  while ((m = re.exec(s))) { if (m.index > last) out.push(H.t(s.slice(last, m.index), o)); out.push(new H.TextRun(FR(m[1], m[2]))); last = re.lastIndex; }
  if (last < s.length) out.push(H.t(s.slice(last), o));
  return out;
};

// ---------- SVG helpers (viewBox width 600) ----------
const svg = (w, h, body, label, disp) => `<svg viewBox="0 0 ${w} ${h}" width="${disp || w}" height="${Math.round((disp || w) * h / w)}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="${label}" style="max-width:100%;height:auto">${body}</svg>`;
const f1 = v => (Math.round(v * 10) / 10).toString();
const rect = (x, y, w, h, fill = W, sw = 2.5, extra = '') => `<rect x="${f1(x)}" y="${f1(y)}" width="${f1(w)}" height="${f1(h)}" fill="${fill}" stroke="${N}" stroke-width="${sw}"${extra}/>`;
const line = (x1, y1, x2, y2, sw = 2.5, col = N, dash = '') => `<line x1="${f1(x1)}" y1="${f1(y1)}" x2="${f1(x2)}" y2="${f1(y2)}" stroke="${col}" stroke-width="${sw}" stroke-linecap="round"${dash ? ` stroke-dasharray="${dash}"` : ''}/>`;
const poly = (pts, fill = W, sw = 2.5) => `<polygon points="${pts.map(p => f1(p[0]) + ',' + f1(p[1])).join(' ')}" fill="${fill}" stroke="${N}" stroke-width="${sw}" stroke-linejoin="round"/>`;
const path = (d, fill = SK) => `<path d="${d}" fill="${fill}" stroke="${N}" stroke-width="2.5" stroke-linejoin="round"/>`;
const text = (x, y, s, size = 18, fill = N, anchor = 'middle', weight = 700) => `<text x="${f1(x)}" y="${f1(y)}" font-size="${size}" font-weight="${weight}" text-anchor="${anchor}" fill="${fill}" font-family="${FONT}">${s}</text>`;
const grid = (x, y, cols, rows, c) => { let d = ''; for (let i = 1; i < cols; i++) d += `M${x + i * c} ${y} V${y + rows * c} `; for (let j = 1; j < rows; j++) d += `M${x} ${y + j * c} H${x + cols * c} `; return rect(x, y, cols * c, rows * c) + `<path d="${d}" stroke="${N}" stroke-width="2.5" fill="none"/>`; };
// cube stacks: cells [x right, y back, z up], drawn from the front, right and above (depth = 0.4 of a cube)
const stack = (cells, s, ox, oy) => {
  const d = s * 0.4; let o = '';
  [...cells].sort((a, b) => (b[1] - a[1]) || (a[2] - b[2]) || (a[0] - b[0])).forEach(([x, y, z]) => {
    const X = ox + x * s + y * d, Yb = oy - z * s - y * d;
    o += rect(X, Yb - s, s, s, Y, 2);
    o += poly([[X, Yb - s], [X + s, Yb - s], [X + s + d, Yb - s - d], [X + d, Yb - s - d]], W, 2);
    o += poly([[X + s, Yb], [X + s, Yb - s], [X + s + d, Yb - s - d], [X + s + d, Yb - d]], SK, 2);
  });
  return o;
};
const hmap = rows => { const c = []; rows.forEach((r, y) => r.forEach((h, x) => { for (let z = 0; z < h; z++) c.push([x, y, z]); })); return c; }; // first row = FRONT
const netCells = rows => { const c = []; rows.forEach((r, y) => [...r].forEach((ch, x) => { if (ch === '#') c.push([x, y]); })); return c; };
const net = (rows, x0, y0, c, fill = SK) => netCells(rows).map(([x, y]) => rect(x0 + x * c, y0 + y * c, c, c, fill)).join('');

// Q1: robot made of 2 squares, 3 triangles, 4 semicircles and 2 quarter circles; count table on the right
const q2svg = () => {
  const x = -150; let s = '';
  s += poly([[300 + x, 8], [262 + x, 58], [338 + x, 58]], SK);                                  // hat: triangle
  s += rect(262 + x, 58, 76, 76, SK);                                                            // head: square
  s += path(`M${262 + x} 72 A24 24 0 0 0 ${262 + x} 120 Z`) + path(`M${338 + x} 72 A24 24 0 0 1 ${338 + x} 120 Z`); // ears: semicircles
  s += rect(244 + x, 134, 112, 112, SK);                                                         // body: square
  s += path(`M${244 + x} 134 L${196 + x} 134 A48 48 0 0 0 ${244 + x} 182 Z`) + path(`M${356 + x} 134 L${404 + x} 134 A48 48 0 0 1 ${356 + x} 182 Z`); // shoulders: quarter circles
  s += poly([[200 + x, 190], [234 + x, 190], [217 + x, 226]], SK) + poly([[366 + x, 190], [400 + x, 190], [383 + x, 226]], SK); // hands: triangles
  s += path(`M${244 + x} 282 A28 28 0 0 1 ${300 + x} 282 Z`) + path(`M${300 + x} 282 A28 28 0 0 1 ${356 + x} 282 Z`); // feet: semicircles
  // count table
  const rows = [['Square', i => rect(i, -14, 28, 28, SK)], ['Triangle', i => poly([[i + 14, -16], [i, 12], [i + 28, 12]], SK)], ['Semicircle', i => path(`M${i} 10 A15 15 0 0 1 ${i + 30} 10 Z`)], ['Quarter circle', i => path(`M${i} 12 L${i} -16 A28 28 0 0 1 ${i + 28} 12 Z`)]];
  rows.forEach(([name, icon], k) => {
    const y = 48 + k * 62;
    s += `<g transform="translate(0 ${y})">${icon(318)}</g>` + text(360, y + 7, name, 17, N, 'start') + rect(500, y - 22, 70, 46, 'none', 2, ' rx="6" stroke-dasharray="4 3"');
  });
  return svg(600, 290, s, 'A robot made of shapes, and a table: square, triangle, semicircle, quarter circle, each with a box to write how many', 470);
};
// Q2: a) 4 by 4 grid  b) triangle with 2 lines from the top corner and 1 line across the middle
const q3svg = () => {
  let s = text(14, 22, 'a', 20, N, 'start') + grid(40, 14, 4, 4, 38);
  const A = [440, 12], B = [320, 170], C = [560, 170];
  s += text(300, 22, 'b', 20, N, 'start') + poly([A, B, C]) + line(A[0], A[1], 400, 170) + line(A[0], A[1], 480, 170) + line(380, 91, 500, 91);
  return svg(600, 182, s, 'a: a grid 4 squares long and 4 squares high. b: a triangle with 2 lines from the top corner to the bottom and 1 line across the middle', 470);
};
// Q3: three stacks
const q4svg = () => {
  const s0 = 34; let s = '';
  s += stack(hmap([[2, 2, 1]]), s0, 40, 160) + text(98, 196, 'A', 20);
  s += stack(hmap([[2, 2], [2, 2]]), s0, 240, 160) + text(298, 196, 'B', 20);
  s += stack(hmap([[1, 1, 1], [2, 2, 1], [3, 2, 1]]), s0, 420, 160) + text(492, 196, 'C', 20);
  return svg(600, 204, s, 'Three stacks of cubes. A: 3 cubes in a row with 2 cubes on top of the left two. B: a big cube 2 long, 2 deep and 2 high. C: a bottom layer 3 by 3, then a layer 2 by 2 at the back left, then 1 cube on top at the back left', 470);
};
// Q4: six nets; Q4b: a shape of 5 squares on a dotted grid
const NETS = [['A', ['.#..', '####', '.#..']], ['B', ['###', '###']], ['C', ['#...', '####', '...#']], ['D', ['.##.', '####']], ['E', ['##..', '.##.', '..##']], ['F', ['#....', '#####']]];
const q5svg = () => {
  const c = 26; let s = '';
  NETS.forEach(([l, rows], i) => {
    const x = 30 + (i % 3) * 196, y = 12 + Math.floor(i / 3) * 104;
    s += text(x, y + 22, l, 20, N, 'start') + net(rows, x + 24, y + 6, c);
  });
  return svg(600, 206, s, 'Six shapes made of 6 squares, labelled A to F', 470);
};
const q5bsvg = () => {
  const c = 30, x0 = 195, y0 = 6; let s = '';
  for (let i = 0; i <= 7; i++) s += line(x0 + i * c - 30, y0, x0 + i * c - 30, y0 + 4 * c, 1.5, '#B9C7DD', '3 4');
  for (let j = 0; j <= 4; j++) s += line(x0 - 30, y0 + j * c, x0 + 6 * c, y0 + j * c, 1.5, '#B9C7DD', '3 4');
  s += net(['.....', '..#..', '.####', '.....'], x0 - 30, y0, c);
  return svg(600, 132, s, 'A row of 4 squares with 1 square above the second square, on a dotted grid', 420);
};
// Q5: dice net (top flap 1, row 2, 3, ?, ?, bottom flap ?)
const q6svg = () => {
  const c = 50, x0 = 200, y0 = 6; let s = net(['#...', '####', '#...'], x0, y0, c, W);
  [[0, 0, '1'], [0, 1, '2'], [1, 1, '3']].forEach(([x, y, t]) => { s += text(x0 + x * c + c / 2, y0 + y * c + c / 2 + 9, t, 26); });
  return svg(600, 162, s, 'A dice net: a row of 4 squares with one square above and one below the first square. The top square shows 1, the row starts 2, 3, and three squares are blank', 380);
};

module.exports = {
  lesson: {
    n: 8, week: 4, session: 'B', title: 'Shape Builders', topic: '2D and 3D Shapes',
    objective: 'Name semicircles and quarter circles and use them to make and break up shapes; count every square and triangle in a figure by working in order; count the cubes in a stack, including hidden ones, layer by layer; decide which nets fold into a cube.',
    skills: 'Spatial reasoning, systematic counting, folding in your head, explaining',
    materials: 'Paper circles (2 per child), scissors, about 12 linking cubes per child (or sugar cubes), printed cube nets, mini whiteboards.',
    online: 'Children cut circles and build stacks on camera; nets are printed from the back of the workbook, or cut from an empty box.',
    warmup: 'Name the solid: a dice, a tissue box, a tin can, a party hat, a drum and a traffic cone. Children make the solid with their hands, then name it (cube, cuboid, cylinder, cone).',
    explore: 'Cut one paper circle into 2 semicircles and another into 4 quarter circles. Make new shapes with the pieces and find different ways to make a whole circle.',
    mini: 'A semicircle has 1 straight side and 1 curved side; a quarter circle has 2 straight sides meeting at a square corner and 1 curved side. Count the pieces in a picture one kind at a time; count every square by size (slide a window); count triangles by the line they sit on. Before page 2: count cubes layer by layer (cubes do not float, so hidden cubes hold up the top ones); fold nets in your head (each square must land on a new face; squares in a line with one square between them are opposite).',
    share: 'How can you be sure you counted every cube in a stack, even the ones you cannot see?',
    exit: { q: 'How many cubes are in a stack with a bottom layer 3 cubes long and 2 cubes deep, and 1 cube on top?', a: '7 (6 + 1)' },
    mistakes: [
      'Counting only the 1 by 1 squares in Q2a (16 instead of 30).',
      'Counting only the cubes you can see in Q3 and forgetting the hidden cubes underneath and behind.',
      'Thinking any 6 joined squares fold into a cube (Q4): B, D and F do not.'
    ],
    extension: 'How many squares are in a grid 5 squares long and 5 squares high? (25 + 16 + 9 + 4 + 1 = 55)',
    key: [
      ['Q1', 'Square 2, triangle 3, semicircle 4, quarter circle 2. (a) semicircles (b) 11 pieces (c) 3 circles: 3 semicircles are 6 quarter circles, 6 + 6 = 12 quarter circles, and 4 quarter circles make a circle.'],
      ['Q2', '(a) 1 by 1: 16, 2 by 2: 9, 3 by 3: 4, 4 by 4: 1; 30 squares  (b) 6 on the bottom line + 6 on the line across = 12 triangles'],
      ['Q3', '(a) A 5, B 8, C 14 (9 + 4 + 1)  (b) 13 more cubes (27 − 14)'],
      ['Q4', '(a) A, C and E  (b) the new square goes under any one of the 4 squares in the row (4 possible places)'],
      ['Q5', 'Row: 2, 3, 5, 4. Bottom square: 6. (1 and 6, 2 and 5, 3 and 4 are opposite.)']
    ]
  },

  script: {
    hook: ['Good morning, inquirers! Today we are shape builders. We will cut circles into pieces, hunt for hidden squares and triangles, count cubes we cannot even see, and fold flat paper into a cube.', 'The secret for every puzzle today: count in order, so nothing is missed and nothing is counted twice.'],
    warmIntro: ['I will show you something from home. Make its shape with your hands: a cube, a cuboid, a cylinder or a cone. Then we say its name together.'],
    predict: ['Before we cut: if I cut a circle in half, and then cut one half in half again, how many pieces will I have? What will they look like?'],
    exploreHints: ['Stuck folding: fold the circle so the edges match exactly, then press the fold flat.', 'Not sure of a name: “Count the straight sides. One straight side: semicircle. Two straight sides: quarter circle.”', 'Finished early: find 3 different ways to make a whole circle from your pieces.'],
    think: [
      '“To name a piece I count its straight sides. One straight side and one curved side: a semicircle. Two straight sides that meet at a square corner, and one curved side: a quarter circle. Turning it round does not change its name.”',
      '“Squares hide inside bigger squares. I count by size: 1 by 1 first, then I slide a 2 by 2 window and count the places it fits, then 3 by 3. Then I add them up.”',
      '“For cubes I count layer by layer. Cubes cannot float, so if I see a cube on top, there must be a cube under it, even if I cannot see it.”'
    ],
    circulate: ['Ask: “How many straight sides does it have? So what is it called?”', 'Ask: “Where else can your window fit? Have you tried every place?”', 'Ask: “What is holding up that top cube?”'],
    hints: ['Hint 1: “Count one kind or one size at a time, and tick each one.”', 'Hint 2: “Build it with cubes, or cut out the net and fold it.”', 'Hint 3: “For a net, pick a bottom square and fold the others up one at a time.”'],
    talk: ['“How can you be sure you counted every cube in a stack, even the ones you cannot see?”', '“Why can 6 squares in a 2 by 3 rectangle not fold into a cube?”'],
    talkAns: 'Count layer by layer; every cube on top sits on a cube below, so the hidden ones must be there. In a 2 by 3 rectangle, 4 squares meet at a corner, but only 3 faces of a cube meet at a corner, so two squares end up on the same face.',
    close: ['“You named pieces by their sides, counted in order and folded nets in your head. That is real shape building.”']
  },

  deck: {
    today: 'Build shapes from semicircles and quarter circles, count every hidden square, triangle and cube, and find which nets fold into a cube.',
    warmGame: 'Name the solid: a dice, a tissue box, a tin can, a party hat, a drum and a traffic cone. Make the shape with your hands, then name it.',
    warmQs: [['How many faces does a cube have?', '6'], ['How many flat faces does a cylinder have?', '2'], ['Cut a circle into 2 equal parts. What is each part called?', 'A semicircle'], ['How many quarter circles make 1 whole circle?', '4'], ['Which solid has a tip and can roll?', 'A cone']],
    expSetup: ['Take 2 paper circles that are the same size.', 'Fold one in half and cut along the fold.', 'Fold the other in half, then in half again. Open it and cut along both folds.', 'Use your pieces to make new shapes. Name them.'],
    expPic: 'one paper circle cut into 2 semicircles, and another cut into 4 quarter circles, with arrows from each circle to its pieces.',
    expAsk: [['How many quarter circles cover a semicircle exactly?', '2'], ['Find 3 different ways to make a whole circle from your pieces.', '2 semicircles; 4 quarter circles; 1 semicircle and 2 quarter circles.'], ['How many straight sides has a quarter circle? Are they the same length?', '2, and yes: they meet at a square corner.']],
    mini1: { head: 'Find the pieces', body: ['A mushroom is made of a semicircle cap, a square stem and 2 quarter circles of grass.', 'Count one kind at a time: 1 straight and 1 curved side, then 2 straight sides and 1 curved side, then 4 straight sides.', 'How many pieces of each kind?'], ans: 'Semicircle 1, quarter circles 2, square 1: 4 pieces.' },
    mini2: { head: 'Count every square', body: ['A grid 3 squares long and 3 squares high.', 'Count by size: 1 by 1, then slide a 2 by 2 window, then the whole grid.', 'How many squares altogether?'], ans: '9 + 4 + 1 = 14 squares.' },
    keyHead: 'Key idea: count in order',
    keyBig: 'Sort what you count, by size, by the line it sits on or by layer, so you never miss one or count one twice.',
    keySmall: 'Name a piece by its sides: a semicircle has 1 straight side, a quarter circle has 2.',
    brk: 'Be a shape! Make a semicircle, a cone, a cube and a cylinder with your body when the tutor calls it.',
    ws1: 'Page 1, in pairs: Q1 the robot and circle pieces, Q2 count every square and triangle.',
    ws2: 'Page 2, on your own: Q3 count the cubes, Q4 which nets fold into a cube, Q5 the dice net.'
  },

  qbank: {
    core: [
      { q: 'How many quarter circles make a whole circle?', a: '4' },
      { q: 'How many semicircles make a whole circle?', a: '2' },
      { q: 'How many faces does a cube have?', a: '6' },
      { q: 'How many squares are in a grid 2 squares long and 2 squares high?', a: '5 (4 small + 1 big)' },
      { q: 'A tower has 3 cubes. Ali builds 2 more towers just like it. How many cubes are there altogether?', a: '9' },
      { q: 'Which solid has 2 flat faces that are circles and 1 curved face?', a: 'A cylinder' }
    ],
    stretch: [
      { q: 'How many quarter circles make 3 semicircles?', a: '6' },
      { q: 'How many squares are in a grid 3 squares long and 2 squares high?', a: '8 (6 small + 2 made of 4 small ones)' },
      { q: 'A stack has 2 layers. Each layer is 3 cubes long and 2 cubes wide. How many cubes?', a: '12' },
      { q: 'Six squares are joined in a straight line. Can they fold into a cube? Explain.', a: 'No. When you fold the line round, the 5th square lands on the same face as the 1st and the 6th on the 2nd, and the two ends are left open.' },
      { q: 'A shape is made of a square with a semicircle on each of its 4 sides, curved sides outward. How many straight sides does its outside edge have? How many curved sides?', a: 'No straight sides and 4 curved sides.' },
      { q: 'How many triangles are in a square with one line from corner to corner?', a: '2' },
      { q: 'Mei builds a big cube 2 cubes long, 2 wide and 2 high. She takes away 1 cube from a corner. How many cubes are left?', a: '7' },
      { q: 'A stack is 4 cubes long, 2 cubes wide and 2 cubes high. How many cubes?', a: '16 (8 in each layer)' }
    ],
    challenge: [
      { q: 'How many squares can you find in a grid 4 squares long and 3 squares high?', a: '20 (12 + 6 + 2)' },
      { q: 'A square has both lines from corner to corner drawn. How many triangles can you find?', a: '8 (4 small + 4 made of 2 small ones)' },
      { q: 'Ben has 3 semicircles and 1 quarter circle, all cut from same-size circles. How many more quarter circles does he need to make exactly 2 whole circles?', a: '1 more (3 semicircles = 6 quarter circles, + 1 = 7; 2 circles need 8)' },
      { q: 'A big cube is built from small cubes: 3 long, 3 wide and 3 high. Its outside is painted. How many small cubes have no paint at all?', a: '1 (only the cube in the very middle is not on the outside)' },
      { q: 'Steps are made of cubes. They are 3 cubes high, then 2, then 1, and every step is 3 cubes wide from front to back. How many cubes?', a: '18 (9 + 6 + 3)' },
      { q: 'How many triangles are in a triangle with 3 lines from the top corner to the bottom and 1 line across the middle?', a: '20 (10 sit on the bottom line + 10 sit on the line across)' },
      { q: 'A pyramid of cubes has a top layer of 1 cube, then a layer 2 by 2, then a layer 3 by 3, then a bottom layer 4 by 4. How many cubes are there?', a: '30 (1 + 4 + 9 + 16)' },
      { q: 'How many squares can you find in a grid 5 squares long and 5 squares high?', a: '55 (25 + 16 + 9 + 4 + 1)' },
      { q: 'On a dice, opposite faces add up to 7. You can see 3 faces showing 1, 2 and 3. What numbers are on the 3 faces you cannot see? What do they add up to?', a: '6, 5 and 4; they add up to 15.' }
    ]
  },

  workbook: H => {
    const R = (s, o) => rich(H, s, o);
    const sp = n => ' '.repeat(n);
    const out = [];
    out.push(H.q(1, 'The robot is made of pieces. Count each kind of piece and write how many in the boxes. Tick each piece as you count it.', { before: 40, keepNext: true }));
    out.push(H.fig(q2svg()));
    out.push(H.sub('a', 'Which kind is there the most of?  __________' + sp(4) + 'b' + sp(2) + 'Pieces altogether?  _____'));
    out.push(H.sub('c', 'Mei has 3 semicircles and 6 quarter circles, all cut from same-size circles. How many whole circles can she make? Show how.', { after: 20 }));
    out.push(...H.lines(1));
    out.push(H.q(2, 'Count every shape. Work in order.', { keepNext: true }));
    out.push(H.fig(q3svg()));
    const ws = [1700, 1700, 1700, 1700, 3100];
    out.push(H.tbl(ws, [H.row(['a   1 by 1', '2 by 2', '3 by 3', '4 by 4', 'Squares altogether'].map((t, i) => H.cell(t, ws[i], { bold: true, fill: 'EDEDED' }))), H.row(ws.map(w => H.cell('', w, { h: 120 })))]));
    out.push(H.sub('b', 'Triangles on the bottom line: ____' + sp(4) + 'on the line across: ____' + sp(4) + 'altogether: ____'));

    out.push(H.q(3, 'Count the cubes. Every cube sits on the table or on another cube, and there are no gaps at the back.', { pb: true, before: 0, keepNext: true }));
    out.push(H.fig(q4svg()));
    out.push(H.sub('a', 'A:  ______ cubes' + sp(12) + 'B:  ______ cubes' + sp(12) + 'C:  ______ cubes'));
    out.push(H.sub('b', 'Ravi wants to turn stack C into a big cube 3 cubes long, 3 cubes wide and 3 cubes high. How many more cubes does he need?   ______'));
    out.push(H.q(4, 'Which of these will fold up into a cube? Circle the letters.', { keepNext: true }));
    out.push(H.fig(q5svg()));
    out.push(H.sub('b', 'Add ONE more square to this shape so that it folds into a cube. Draw it on the grid.', { keepNext: true }));
    out.push(H.fig(q5bsvg()));
    out.push(H.q(5, 'On a dice, the numbers on opposite faces add up to 7. This net folds into a dice. Write the missing numbers.', { keepNext: true }));
    out.push(H.fig(q6svg()));
    return out;
  }
};
