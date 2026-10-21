// Math Inquirers P5 — Lesson 4: Triangle Areas (area of a triangle; base and height, heights outside the triangle,
// same base and same height, triangles in composite figures, shaded-area puzzles).
// Every figure is drawn to scale from cm coordinates, and every area was checked with exact arithmetic (shoelace formula in Python).

const NAVY = '#1B2A49', YEL = '#FFC93C', SKY = '#DDEBF7', TEAL = '#1F7A6F', WHITE = '#FFFFFF';
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const T = (x, y, s, o = {}) => `<text x="${x}" y="${y}" font-size="${o.size || 15}" font-weight="${o.weight || 700}" text-anchor="${o.anchor || 'middle'}" fill="${o.fill || NAVY}" font-family="Arial">${esc(s)}</text>`;
const svg = (w, h, label, inner) => `<svg aria-label="${esc(label)}" viewBox="0 0 ${w} ${h}" xmlns="http://www.w3.org/2000/svg" style="width:${w}px;max-width:100%">${inner}</svg>`;
// cm -> px with origin (ox, oy) and s px per cm (y up)
const M = (ox, oy, s) => (x, y) => [ox + x * s, oy - y * s];
const poly = (pts, fill = WHITE) => `<polygon points="${pts.map(p => p.join(',')).join(' ')}" fill="${fill}" stroke="${NAVY}" stroke-width="2" stroke-linejoin="round"/>`;
const ln = (a, b, dash) => `<line x1="${a[0]}" y1="${a[1]}" x2="${b[0]}" y2="${b[1]}" stroke="${NAVY}" stroke-width="${dash ? 1.6 : 2}"${dash ? ' stroke-dasharray="6 4"' : ''}/>`;
// right-angle mark at foot f, going dx (±1) along the base and dy (±1, −1 = up) along the height
const ra = (f, dx, dy, k = 9) => `<path d="M${f[0] + dx * k} ${f[1]} V${f[1] + dy * k} H${f[0]}" fill="none" stroke="${NAVY}" stroke-width="1.5"/>`;

// Q1: three triangles, all at 11 px per cm
const q1Fig = () => {
  const s = 11, oy = 196; let g = '';
  // (a) right-angled: legs 8 (base) and 6, slanting side 10
  let P = M(60, oy, s);
  g += poly([P(0, 0), P(8, 0), P(0, 6)], YEL) + ra(P(0, 0), 1, -1);
  g += T(60, 40, '(a)', { anchor: 'start', fill: TEAL }) + T(104, 216, '8 cm') + T(53, 167, '6 cm', { anchor: 'end' }) + T(111, 152, '10 cm', { anchor: 'start' });
  // (b) base 14, top corner above the point 5 cm along, height 12; sides 13 and 15
  P = M(205, oy, s);
  g += poly([P(0, 0), P(14, 0), P(5, 12)], SKY) + ln(P(5, 12), P(5, 0), true) + ra(P(5, 0), 1, -1);
  g += T(205, 40, '(b)', { anchor: 'start', fill: TEAL }) + T(282, 216, '14 cm') + T(225, 130, '13 cm', { anchor: 'end' }) + T(316, 130, '15 cm', { anchor: 'start' }) + T(265, 160, '12 cm', { anchor: 'start' });
  // (c) obtuse: base 9, top corner 6 cm past the end of the base, height 8; long side 17
  P = M(405, oy, s);
  g += ln(P(9, 0), P(15, 0), true) + ln(P(15, 8), P(15, 0), true) + ra(P(15, 0), -1, -1);
  g += poly([P(0, 0), P(9, 0), P(15, 8)], YEL);
  g += T(405, 40, '(c)', { anchor: 'start', fill: TEAL }) + T(454.5, 216, '9 cm') + T(476, 142, '17 cm', { anchor: 'end' }) + T(578, 155, '8 cm', { anchor: 'start' });
  return svg(620, 226, 'Three triangles. (a) right-angled with sides 8 cm, 6 cm and 10 cm. (b) base 14 cm, height 12 cm, sides 13 cm and 15 cm. (c) base 9 cm, height 8 cm outside the triangle, long side 17 cm.', g);
};

// Q2: rectangle ABCD 10 cm by 6 cm drawn twice; triangle PDC and triangle QDC
const q2Fig = () => {
  const s = 22; let g = '';
  [[50, 2, 'P', YEL], [330, 7, 'Q', SKY]].forEach(([ox, px, lab, fill]) => {
    const P = M(ox, 166, s);
    g += poly([P(0, 0), P(10, 0), P(10, 6), P(0, 6)], WHITE) + poly([P(px, 6), P(0, 0), P(10, 0)], fill);
    g += T(ox - 6, 30, 'A', { anchor: 'end' }) + T(ox + 226, 30, 'B', { anchor: 'start' }) + T(ox + 226, 182, 'C', { anchor: 'start' }) + T(ox - 6, 182, 'D', { anchor: 'end' });
    g += T(P(px, 6)[0], 26, lab) + T(ox + 110, 188, '10 cm') + T(ox - 8, 105, '6 cm', { anchor: 'end' });
  });
  return svg(600, 196, 'Rectangle ABCD, 10 cm by 6 cm, drawn twice. Left: P on AB and triangle PDC shaded. Right: Q on AB and triangle QDC shaded.', g);
};

// Q3: quadrilateral ABCD split by the diagonal AC (14 cm); heights 5 cm and 3 cm
const splitFig = () => {
  const P = M(90, 170, 30); let g = '';
  g += poly([P(0, 0), P(4, 5), P(14, 0), P(9, -3)], SKY) + ln(P(0, 0), P(14, 0));
  g += ln(P(4, 5), P(4, 0), true) + ra(P(4, 0), 1, -1) + ln(P(9, -3), P(9, 0), true) + ra(P(9, 0), 1, 1);
  g += T(80, 176, 'A', { anchor: 'end' }) + T(210, 14, 'B') + T(520, 176, 'C', { anchor: 'start' }) + T(360, 284, 'D');
  g += T(216, 100, '5 cm', { anchor: 'start' }) + T(366, 222, '3 cm', { anchor: 'start' }) + T(590, 40, 'AC = 14 cm', { anchor: 'end', fill: TEAL });
  return svg(600, 292, 'Four-sided figure ABCD with diagonal AC of 14 cm. The height from B to AC is 5 cm and the height from D to AC is 3 cm.', g);
};

// Q4: rectangle ABCD 12 cm by 8 cm; E on AB with AE = 4 cm; F on BC with BF = 4 cm; triangle DEF shaded
const takeFig = () => {
  const P = M(150, 250, 26); let g = '';
  g += poly([P(0, 0), P(12, 0), P(12, 8), P(0, 8)], WHITE) + poly([P(0, 0), P(4, 8), P(12, 4)], YEL);
  g += T(142, 38, 'A', { anchor: 'end' }) + T(470, 38, 'B', { anchor: 'start' }) + T(470, 266, 'C', { anchor: 'start' }) + T(142, 266, 'D', { anchor: 'end' }) + T(254, 30, 'E') + T(470, 151, 'F', { anchor: 'start' });
  g += T(202, 32, '4 cm') + T(358, 32, '8 cm') + T(472, 98, '4 cm', { anchor: 'start' }) + T(472, 204, '4 cm', { anchor: 'start' }) + T(140, 150, '8 cm', { anchor: 'end' }) + T(306, 274, '12 cm');
  return svg(600, 282, 'Rectangle ABCD, 12 cm by 8 cm. E is on AB with AE 4 cm and EB 8 cm. F is on BC with BF 4 cm and FC 4 cm. Triangle DEF is shaded.', g);
};

module.exports = {
  lesson: {
    n: 4, week: 2, session: 'B', title: 'Triangle Areas', topic: 'Area of Triangle',
    objective: 'Find the area of a triangle as 1/2 × base × height, choosing a base and the height that meets it at a right angle (also when the height is outside the triangle); use “same base, same height” to explain equal areas; find areas of composite figures and shaded parts by splitting into triangles or by taking away.',
    skills: 'Spotting the height, ignoring lengths that are not needed, reasoning with same base and same height, splitting a figure, taking away from a rectangle, explaining why an area does not change',
    materials: 'Square grid paper (cut-out page at the back of the workbook), scissors, ruler, set square or the corner of a card, mini whiteboard and marker, workbook, pencil.',
    online: 'The tutor shares the slides and clicks to draw heights and reveal each step. For the explore, children draw and cut their rectangle with the camera pointing down at the desk, and hold up the pieces to show they fit. Whiteboards are held up together for the quick questions.',
    warmup: 'Half or not? Three rectangles each have one shaded triangle. Children vote: is the shaded triangle exactly half of the rectangle? (Diagonal: yes. Top corner on the opposite side: yes. Corner to the middle of a side: no, it is 1/4.)',
    explore: 'Cut a rectangle. Pairs draw a rectangle 8 cm by 6 cm on grid paper, mark any point on the top side and join it to the two bottom corners. They cut out the triangle and the two leftover pieces. Do the two pieces cover the triangle exactly? Try a different point. What is the area of the triangle?',
    mini: 'Area of a triangle = 1/2 × base × height. The height meets the base (or the base extended) at a right angle; slanting sides are not heights. Triangles with the same base and the same height have the same area. For harder figures, split into triangles or take the white triangles away from a rectangle.',
    share: 'Ben says, “A triangle with longer sides always has a bigger area.” Is he right?',
    exit: { q: 'A triangle has an area of 42 cm². Its base is 12 cm. What is its height?', a: '7 cm (1/2 × 12 × height = 42, so 6 × height = 42)' },
    mistakes: ['Using a slanting side as the height (1/2 × 14 × 13 for a 13-14-15 triangle).', 'Forgetting the 1/2 and giving the area of the whole rectangle.', 'For a height outside the triangle, measuring the base all the way to the foot of the height (adding the dashed extension to the base).'],
    extension: 'On a grid, draw as many different triangles as you can with area 6 cm² using a base of 4 cm. Where can the top corner go? (Anywhere on the line 3 cm above the base.)',
    key: [
      ['Q1', '(a) 24 cm² (1/2 × 8 × 6)  (b) 84 cm² (1/2 × 14 × 12)  (c) 36 cm² (1/2 × 9 × 8)  (d) 13 cm and 15 cm: they are slanting sides, not at a right angle to the base.'],
      ['Q2', '(a) 30 cm²  (b) 30 cm²  (c) Both have base DC = 10 cm and height 6 cm (P and Q are on AB, 6 cm above DC).  (d) 30 cm² (60 − 30: the triangle is half the rectangle, so the white parts are the other half)'],
      ['Q3', '56 cm² (triangle ABC 1/2 × 14 × 5 = 35, triangle ACD 1/2 × 14 × 3 = 21)'],
      ['Q4', '(a) 96 cm²  (b) ADE 16 cm², EBF 16 cm², FCD 24 cm²  (c) 40 cm² (96 − 56)'],
      ['Q5', '(a) 24 cm²  (b) 4 cm  (c) any base and height that multiply to 48, e.g. base 16 cm and height 3 cm, or base 6 cm and height 8 cm (or base 8 cm and height 6 cm leaning over)']
    ]
  },

  script: {
    hook: ['Welcome back, inquirers! A triangle is half of something. Today we find out half of WHAT, and why a squashed, leaning triangle can have exactly the same area as a neat one.', 'Notice it, test it, explain why. Today “test it” means cutting paper.'],
    warmIntro: ['Here are three rectangles, each with a shaded triangle. Thumbs up if you think the triangle is exactly half of the rectangle, thumbs down if not. Decide for each one before I click.', 'For the one that is not half: how much of the rectangle is it? How do you know?'],
    predict: ['You will draw a rectangle 8 cm by 6 cm and a triangle inside it with its top corner on the top side. Predict: what fraction of the rectangle is the triangle? Does it matter where the top corner is?'],
    exploreHints: ['Stuck: fold each leftover piece along a grid line and lay it on the triangle.', 'Pieces do not fit: check that your top corner is exactly on the top side and the bottom corners are the rectangle’s corners.', 'Finished early: move the top corner right to the end of the top side. What kind of triangle is it now? Is it still half?'],
    think: ['“This triangle has sides 5, 12 and 13. Which two do I multiply? The height must meet the base at a right angle. I look for the square corner: 12 and 5 meet there. 13 is slanting, so I do not use it. 1/2 × 12 × 5 = 30.”', '“Here the top corner is past the end of the base. I extend the base with a dashed line and drop the height to it: 12 cm. The base is still only 11 cm: the dashed part is not part of the triangle. 1/2 × 11 × 12 = 66.”', '“All three triangles sit on the bottom of the same rectangle with their top corner on the top side. Same base, 14 cm. Same height, 9 cm. So they all have the same area, 63 cm², even though they look different.”'],
    circulate: ['Ask: “Point to the height. How do you know it meets the base at a right angle?”', 'Ask: “Which length did you not need? Why not?”', 'Ask: “Did you split the figure or take away? Could you do it the other way to check?”'],
    hints: ['Hint 1: “Find the square corner (the right angle). The two lines that make it are a base and a height.”', 'Hint 2: “If there is no square corner, look for a dashed line drawn at a right angle to a side.”', 'Hint 3: “Box the shape in a rectangle. Find the rectangle’s area, then take away the white triangles.”'],
    talk: ['“Ben says a triangle with longer sides always has a bigger area. Is he right?”', '“How can two triangles that look very different have the same area?”'],
    talkAns: 'No. Two triangles with the same base and the same height have the same area, even if one leans over and has much longer sides. The area depends on the base and the height, not on the slanting sides. A very long, thin triangle can even have a smaller area than a short, wide one.',
    close: ['“Today you found the height (sometimes outside the triangle), and you saw why triangles on the same base with the same height have the same area. That is explaining why.”', '“Show me your exit ticket and collect your stamp.”']
  },

  deck: {
    today: 'Find the base and the height of any triangle, explain why triangles with the same base and height have the same area, and solve shaded-area puzzles.',
    warmGame: 'Half or not? Three rectangles each have one shaded triangle: one cut along a diagonal, one with its top corner on the top side, one from a corner to the middle of a side. Vote: is the shaded part exactly half?',
    warmQs: [['Area of a rectangle 7 cm by 6 cm?', '42 cm²'], ['Half of 42 cm²?', '21 cm²'], ['1/2 × 9 × 4 = ?', '18'], ['A square has an area of 49 cm². How long is each side?', '7 cm'], ['1/2 × 15 × 8 = ?', '60']],
    expSetup: ['Draw a rectangle 8 cm by 6 cm on grid paper.', 'Mark any point on the top side. Join it to the two bottom corners.', 'Cut out the triangle and the two leftover pieces.', 'Do the two pieces cover the triangle exactly? Try again with a different point.'],
    expPic: 'a rectangle 8 cm by 6 cm on a 1 cm grid with a point on the top side joined to the two bottom corners; the middle triangle is yellow and the two leftover corner pieces are blue.',
    expAsk: [['Do the two leftover pieces cover the triangle exactly?', 'Yes, so the triangle is half of the rectangle.'], ['What is the area of the triangle?', '24 cm² (half of 8 × 6 = 48)'], ['Does it matter where the point on the top side is?', 'No: the base is always 8 cm and the height is always 6 cm.']],
    mini1: { head: 'Height outside the triangle', body: ['A triangle has a base of 11 cm. Its top corner is past the end of the base. The height to the base extended is 12 cm, and its sides are 13 cm and 20 cm.', 'What is its area?'], ans: '66 cm² (1/2 × 11 × 12; the 13 cm and 20 cm sides are not needed).' },
    mini2: { head: 'Same base, same height', body: ['A rectangle is 14 cm by 9 cm. Three triangles each use the bottom side as the base, with the top corner at different points on the top side.', 'What is the area of each triangle?'], ans: '63 cm² each (1/2 × 14 × 9), half of the rectangle.' },
    keyHead: 'Key idea: 1/2 × base × height',
    keyBig: 'Area of a triangle = 1/2 × base × height. The height meets the base at a right angle, even when it is outside the triangle.',
    keySmall: 'Same base and same height: same area, whatever the shape.',
    brk: 'Triangle stretch. Make a triangle with your arms above your head. Now make a right angle with one arm. Lean your triangle to the left and to the right: did its height change?',
    ws1: 'Page 1, in pairs: Q1 base and height in three triangles, Q2 triangles in a rectangle.',
    ws2: 'Page 2, on your own: Q3 split into triangles, Q4 take away the white triangles, Q5 same area, different triangles.'
  },

  qbank: {
    core: [
      { q: 'A triangle has a base of 12 cm and a height of 5 cm. What is its area?', a: '30 cm²' },
      { q: 'A right-angled triangle has sides of 8 cm, 15 cm and 17 cm. What is its area?', a: '60 cm² (1/2 × 8 × 15; 17 cm is the slanting side)' },
      { q: 'A triangle has an area of 36 cm² and a height of 8 cm. How long is its base?', a: '9 cm (1/2 × 9 × 8 = 36)' },
      { q: 'A rectangle 9 cm by 6 cm is cut along a diagonal into two triangles. What is the area of each triangle?', a: '27 cm²' },
      { q: 'A square has sides of 8 cm. A triangle inside it has one side of the square as its base and its top corner on the opposite side. What is the area of the triangle?', a: '32 cm²' },
      { q: 'A triangle has a base of 14 cm and a height of 9 cm. A second triangle has the same base and the same height. What is the total area of the two triangles?', a: '126 cm² (63 + 63)' }
    ],
    stretch: [
      { q: 'A triangle has an area of 45 cm². Its base is 10 cm. What is its height?', a: '9 cm' },
      { q: 'A right-angled triangle has sides of 12 cm, 16 cm and 20 cm. What is its area?', a: '96 cm² (1/2 × 12 × 16)' },
      { q: 'A square has sides of 10 cm. A triangle is drawn with one side of the square as its base and its top corner on the opposite side. What is the area of the triangle?', a: '50 cm²' },
      { q: 'A triangle and a rectangle have the same base, 12 cm, and the same height, 7 cm. What is the difference between their areas?', a: '42 cm² (84 − 42)' },
      { q: 'Triangle P has a base of 8 cm and a height of 5 cm. Triangle Q has a base of 4 cm and the same area as P. What is the height of Q?', a: '10 cm (area 20 cm²)' },
      { q: 'A rectangle is 12 cm by 8 cm. M is the middle of the top side. M is joined to the two bottom corners. What is the area of the triangle? What is the area of the rest of the rectangle?', a: '48 cm² and 48 cm²' },
      { q: 'A figure is a square of side 6 cm with a triangle on top. The base of the triangle is the top side of the square and its height is 4 cm. What is the area of the figure?', a: '48 cm² (36 + 12)' },
      { q: 'What is the area of a triangle with a base of 7.5 cm and a height of 4 cm?', a: '15 cm²' }
    ],
    challenge: [
      { q: 'Triangle ABC has an area of 60 cm². D is the middle point of BC. What is the area of triangle ABD?', a: '30 cm² (half the base, same height)' },
      { q: 'A rectangle is 12 cm by 8 cm. P is the middle of the top side and Q is the middle of the right side. What is the area of the triangle joining P, Q and the bottom-left corner?', a: '36 cm² (96 − 24 − 12 − 24)' },
      { q: 'A triangle and a square have the same area. The square has sides of 6 cm. The triangle has a base of 9 cm. What is the height of the triangle?', a: '8 cm (1/2 × 9 × 8 = 36)' },
      { q: 'Square ABCD has sides of 8 cm (A top-left, B bottom-left, C bottom-right, D top-right). BC is extended to E so that CE = 4 cm. AE cuts CD at F. What is the difference between the area of triangle ADF and the area of triangle FCE?', a: '16 cm² (add the shape ABCF to both: square 64 cm² and triangle ABE 48 cm², so the difference is 64 − 48)' },
      { q: 'List every pair of whole numbers (base and height, in cm) for a triangle with an area of 6 cm².', a: '6 pairs: 1 and 12, 2 and 6, 3 and 4, 4 and 3, 6 and 2, 12 and 1 (base × height must be 12)' },
      { q: 'Ali draws a triangle with a base of 10 cm and a height of 6 cm. Mei draws a triangle with a base of 5 cm and twice the area of Ali’s triangle. What is the height of Mei’s triangle?', a: '24 cm (Mei’s area is 60 cm²)' },
      { q: 'A right-angled triangle has sides of 15 cm, 20 cm and 25 cm. What is its height when the 25 cm side is the base?', a: '12 cm (area 1/2 × 15 × 20 = 150 cm², and 1/2 × 25 × 12 = 150)' },
      { q: 'Two squares stand side by side on a line, touching: a big square of side 10 cm and a small square of side 6 cm. Join the bottom-left corner of the big square, the top-right corner of the big square and the top-right corner of the small square to make a triangle. What is its area? Try again with a small square of side 4 cm. What do you notice?', a: '50 cm² both times: it is always half of the big square (box it in a rectangle and take away three right-angled triangles: 160 − 50 − 12 − 48 = 50, and 140 − 50 − 12 − 28 = 50)' },
      { q: 'Triangle ABC has an area of 54 cm². D is a point on BC with BD = 4 cm and DC = 8 cm. What is the area of triangle ABD?', a: '18 cm² (the height is 9 cm because 1/2 × 12 × 9 = 54; ABD has base 4 cm and the same height)' }
    ]
  },

  workbook: H => [
    H.p('Area of a triangle = 1/2 × base × height. The height meets the base at a right angle.', { after: 40 }),
    H.q(1, 'Find the area of each triangle. The drawings are to scale.', { before: 40, keepNext: true }),
    H.fig(q1Fig()),
    H.sub('a', 'Area of (a) = __________ cm²       (b)  Area of (b) = __________ cm²       (c)  Area of (c) = __________ cm²'),
    H.sub('d', 'Which lengths in (b) did you NOT need? Why not?'), ...H.lines(1),
    H.q(2, 'ABCD is a rectangle 10 cm by 6 cm. P and Q are points on AB.', { keepNext: true }),
    H.fig(q2Fig()),
    H.sub('a', 'Area of triangle PDC = ____________ cm²          (b)  Area of triangle QDC = ____________ cm²'),
    H.sub('c', 'Explain why the two triangles have the same area.'), ...H.lines(1),
    H.sub('d', 'In the left rectangle, what is the total area of the two white parts?'), H.ans(),

    H.q(3, 'Find the area of the figure ABCD. Split it into two triangles along AC.', { pb: true, before: 0, keepNext: true }),
    H.fig(splitFig()),
    H.ans('Area:'),
    H.q(4, 'ABCD is a rectangle. Find the area of the shaded triangle DEF.', { keepNext: true }),
    H.fig(takeFig()),
    H.sub('a', 'Area of the rectangle ABCD = ______________ cm²'),
    H.sub('b', 'White triangles:   ADE = ________ cm²     EBF = ________ cm²     FCD = ________ cm²'),
    H.sub('c', 'Area of the shaded triangle DEF = ______________ cm²'),
    H.q(5, 'Mei draws a triangle with a base of 8 cm and a height of 6 cm.', { keepNext: true }),
    H.sub('a', 'What is the area of Mei’s triangle?'), H.ans(),
    H.sub('b', 'Siti’s triangle has the same area but a base of 12 cm. What is its height?'), H.ans(),
    H.sub('c', 'Give the base and height of one more triangle with the same area.'), H.ans('Base: ________ cm     Height:')
  ]
};
