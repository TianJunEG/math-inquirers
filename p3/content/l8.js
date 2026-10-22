// Math Inquirers P3 – Lesson 8: Angle and Line Detectives (Angles, perpendicular and parallel lines)
// Heuristics taught: (1) count in an organised way (visit every corner or meeting point; small angles first); (2) look for a pattern.
const N = '#1B2A49', Y = '#FFC93C', S = '#DDEBF7', G = '#1F7A6F', W = '#FFFFFF', LG = '#B9C6DE';

// ---------- small SVG helpers for the workbook ----------
const svg = (w, h, body, label, dw) => `<svg viewBox="0 0 ${w} ${h}" width="${dw || w}" role="img" aria-label="${label}" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto">${body}</svg>`;
const txt = (x, y, s, o = {}) => `<text x="${x}" y="${y}" font-size="${o.size || 20}" font-weight="${o.w || 700}" text-anchor="${o.anchor || 'middle'}" fill="${o.fill || N}" font-family="Fredoka, Arial, sans-serif">${s}</text>`;
const ln = (x1, y1, x2, y2, o = {}) => `<line x1="${x1.toFixed(1)}" y1="${y1.toFixed(1)}" x2="${x2.toFixed(1)}" y2="${y2.toFixed(1)}" stroke="${o.c || N}" stroke-width="${o.sw || 4}" stroke-linecap="round"/>`;
const dot = (x, y, r = 5) => `<circle cx="${x}" cy="${y}" r="${r}" fill="${N}"/>`;
const poly = (pts, fill = S) => `<polygon points="${pts.map(([a, b]) => a.toFixed(1) + ',' + b.toFixed(1)).join(' ')}" fill="${fill}" stroke="${N}" stroke-width="3.5" stroke-linejoin="miter"/>`;
const bgGrid = (x, y, cols, rows, c) => {
  let d = '';
  for (let i = 0; i <= cols; i++) d += `M${x + i * c} ${y}V${y + rows * c}`;
  for (let j = 0; j <= rows; j++) d += `M${x} ${y + j * c}H${x + cols * c}`;
  return `<path d="${d}" stroke="${LG}" stroke-width="1.2" fill="none"/>`;
};
const rad = d => d * Math.PI / 180;

// Q1: six angles. [letter, first arm direction (degrees, anticlockwise from east), size, arm 1 length, arm 2 length]
// a 90 (turned), b 45, c 120, d 90 (one short arm), e 150, f 70 (long arms)
const ANG = [['a', 25, 90, 62, 62], ['b', 60, 45, 66, 66], ['c', 10, 120, 58, 58], ['d', 0, 90, 70, 34], ['e', 200, 150, 52, 52], ['f', 100, 60, 72, 72]];
const q1Fig = () => {
  let b = '';
  ANG.forEach(([l, d1, sz, L1, L2], i) => {
    const d2 = d1 + sz;
    const p1 = [L1 * Math.cos(rad(d1)), -L1 * Math.sin(rad(d1))], p2 = [L2 * Math.cos(rad(d2)), -L2 * Math.sin(rad(d2))];
    const xs = [0, p1[0], p2[0]], ys = [0, p1[1], p2[1]];
    const cx = 50 + i * 100, cy = 62;
    const vx = cx - (Math.min(...xs) + Math.max(...xs)) / 2, vy = cy - (Math.min(...ys) + Math.max(...ys)) / 2;
    const r = 16, a1 = [vx + r * Math.cos(rad(d1)), vy - r * Math.sin(rad(d1))], a2 = [vx + r * Math.cos(rad(d2)), vy - r * Math.sin(rad(d2))];
    b += `<path d="M${a1[0].toFixed(1)} ${a1[1].toFixed(1)} A${r} ${r} 0 0 0 ${a2[0].toFixed(1)} ${a2[1].toFixed(1)}" fill="none" stroke="${G}" stroke-width="3"/>`;
    b += ln(vx, vy, vx + p1[0], vy + p1[1]) + ln(vx, vy, vx + p2[0], vy + p2[1]) + dot(vx, vy, 4);
    b += txt(cx, 148, l, { size: 22 });
  });
  return svg(600, 158, b, 'Six angles labelled a to f, each marked with a small arc. Some are turned, and the arms have different lengths.', 500);
};
// Q2: four shapes (unit u, y up inside each shape)
const shapeAt = (pts, x0, y0, u, H) => pts.map(([a, b]) => [x0 + a * u, y0 + (H - b) * u]);
const q2Fig = () => {
  const u = 28;
  const plus = [[1, 0], [2, 0], [2, 1], [3, 1], [3, 2], [2, 2], [2, 3], [1, 3], [1, 2], [0, 2], [0, 1], [1, 1]];
  const stair = [[0, 0], [3, 0], [3, 1], [2, 1], [2, 2], [1, 2], [1, 3], [0, 3]];
  const house = [[0, 0], [4, 0], [4, 3], [2, 5], [0, 3]];          // the roof top is a right angle
  const trap = [[0, 0], [5, 0], [3, 3], [0, 3]];
  let b = poly(shapeAt(plus, 40, 54, u, 3)) + poly(shapeAt(stair, 175, 54, u, 3)) + poly(shapeAt(house, 300, 0, u, 5)) + poly(shapeAt(trap, 440, 54, u, 3));
  [['A', 82], ['B', 217], ['C', 356], ['D', 510]].forEach(([l, x]) => { b += txt(x, 172, l, { size: 22 }); });
  return svg(600, 180, b, 'Four shapes: A a plus sign, B a staircase with 3 steps, C a house shape with a pointed roof, D a shape with a long bottom, a slanted right side and two square corners on the left', 400);
};
// Q3: 6 lines from one point, spread out like a fan (5 gaps of 30 degrees)
const q3Fig = () => {
  const ox = 190, oy = 196, L = 170; let b = '';
  [15, 45, 75, 105, 135, 165].forEach(d => { b += ln(ox, oy, ox + L * Math.cos(rad(d)), oy - L * Math.sin(rad(d)), { sw: 4 }); });
  b += dot(ox, oy, 6) + txt(ox, oy + 26, 'O', { size: 22 });
  return svg(380, 228, b, 'Six straight lines going out from one point O, spread out like a fan', 215);
};
// Q4: letters made of straight lines
const q4Fig = () => {
  let b = ''; const w = 50, h = 80, top = 16, o = { sw: 7 };
  const L = {
    E: x => ln(x, top, x, top + h, o) + ln(x, top, x + w, top, o) + ln(x, top + h / 2, x + w * 0.8, top + h / 2, o) + ln(x, top + h, x + w, top + h, o),
    H: x => ln(x, top, x, top + h, o) + ln(x + w, top, x + w, top + h, o) + ln(x, top + h / 2, x + w, top + h / 2, o),
    T: x => ln(x, top, x + w, top, o) + ln(x + w / 2, top, x + w / 2, top + h, o),
    L: x => ln(x, top, x, top + h, o) + ln(x, top + h, x + w, top + h, o),
    Z: x => ln(x, top, x + w, top, o) + ln(x + w, top, x, top + h, o) + ln(x, top + h, x + w, top + h, o),
    N: x => ln(x, top + h, x, top, o) + ln(x, top, x + w, top + h, o) + ln(x + w, top + h, x + w, top, o)
  };
  'EHTLZN'.split('').forEach((c, i) => { b += L[c](45 + i * 95); });
  return svg(600, 112, b, 'The capital letters E, H, T, L, Z and N drawn with straight lines', 420);
};
// Q5: square grid with lines AB and EF
const q5Fig = () => {
  const c = 36, x0 = 28, y0 = 14, P = (a, b) => [x0 + a * c, y0 + b * c];
  let b = bgGrid(x0, y0, 14, 7, c);
  const seg = (p, q) => ln(...P(...p), ...P(...q), { sw: 4 });
  b += seg([1, 6], [5, 2]) + seg([9, 6], [13, 4]);
  const lab = (a, bb, s, dx, dy) => dot(...P(a, bb), 5.5) + txt(P(a, bb)[0] + dx, P(a, bb)[1] + dy, s, { size: 20 });
  b += lab(1, 6, 'A', -14, 20) + lab(5, 2, 'B', 14, -6) + lab(3, 4, 'D', -16, -6) + lab(7, 5, 'C', 14, 20) + lab(9, 6, 'E', -14, 20) + lab(13, 4, 'F', 16, -6) + lab(11, 5, 'G', -4, 24);
  return svg(560, 280, b, 'A square grid. Line AB goes 1 square right and 1 square up at each step, and D is on AB. Point C is not on AB. Line EF goes 2 squares right and 1 square up at each step, and G is on EF.', 400);
};
// Q6: a window: rectangle with one line across and one line down through the middle
const q6Fig = () => svg(240, 160, `<rect x="20" y="15" width="200" height="130" fill="${S}" stroke="${N}" stroke-width="4"/>` + ln(120, 15, 120, 145) + ln(20, 80, 220, 80), 'A rectangle with one line from the middle of the top to the middle of the bottom and one line from the middle of the left side to the middle of the right side', 220);
module.exports = {
  lesson: {
    n: 8, week: 4, session: 'B', title: 'Angle and Line Detectives', topic: 'Angles, Perpendicular and Parallel Lines',
    objective: 'Compare angles with a right angle using a folded-paper checker, count the angles at a point and the right angles in shapes and figures in an organised way, find a pattern in the counts, and find and draw perpendicular and parallel lines.',
    skills: 'Organised counting, pattern spotting, checking with a tool, explaining',
    materials: 'Scrap paper to fold a right-angle checker, a ruler, mini whiteboards, square grid paper.',
    online: 'Each child folds a right-angle checker on camera and goes on a 2-minute right-angle hunt at home; the tutor shares the grid slides to draw on. Print the workbook before the lesson. Pairs work in one breakout room for 10 minutes, then return for the check slide.',
    warmup: 'Clock angles: is the angle between the hands at 3, 1, 5, 9, 10 and 4 o’clock a right angle, smaller or bigger? Show it with your arms. Then quick questions.',
    explore: 'Fold any scrap of paper twice to make a right-angle checker. Hunt for 3 right angles, 1 angle smaller and 1 angle bigger than a right angle. Why is the folded corner always a right angle?',
    mini: 'The size of an angle is how far it opens, not how long its arms are. Count the angles at a point: small ones first (4 lines: 3 + 2 + 1 = 6) and look for the pattern 1, 3, 6, 10. Count right angles inside a shape corner by corner (an L has 6 corners but 5 right angles inside); count right angles where lines meet point by point. Perpendicular and parallel lines: list every pair. Before page 2: parallel and perpendicular lines on a square grid (same steps; swap the steps and turn).',
    share: 'Mei says: “An angle with longer arms is a bigger angle.” Do you agree? How can you test it?',
    exit: { q: 'Which of these letters have BOTH a pair of parallel lines and a pair of perpendicular lines: F, V, H, Z?', a: 'F and H' },
    mistakes: ['Thinking an angle with longer arms is bigger, or that a turned right angle is not a right angle.', 'Counting every corner of a shape as a right angle, even a dent corner (inside it is bigger than a right angle).', 'Counting angles or line pairs at random, so some are missed or counted twice.'],
    extension: 'How many right angles are in a square drawn as a noughts-and-crosses grid (2 lines down and 2 lines across inside it)? (36)',
    key: [
      ['Q1', 'Smaller than a right angle: b, f.  Right angle: a, d.  Bigger than a right angle: c, e.'],
      ['Q2', 'A 8 (the 4 dent corners are bigger),  B 6 (2 dent corners),  C 3 (the 2 bottom corners and the top of the roof),  D 2.'],
      ['Q3', '(a) 5 + 4 + 3 + 2 + 1 = 15 angles.  (b) 8 lines: 7 + 6 + 5 + 4 + 3 + 2 + 1 = 28 angles.'],
      ['Q4', '(a) E and H: both.  T and L: perpendicular only.  Z and N: parallel only.  (b) E: 3 pairs of parallel lines and 3 pairs of perpendicular lines.'],
      ['Q5', '(a) A line through C going 1 square right and 1 square up at each step (the same steps as AB).  (b) A line through D going 1 square right and 1 square down at each step.  (c) A line through G going 1 square right and 2 squares down (or 1 left and 2 up) at each step. Check each with the right-angle checker.'],
      ['Q6', '16 right angles: 4 outer corners × 1, 4 points where the lines meet the sides × 2, and 4 in the middle.']
    ]
  },

  script: {
    hook: ['Today you are angle and line detectives. Detectives do not guess: they check every clue with a tool. Our tool is a right-angle checker that you make yourself from any scrap of paper.', 'By the end you will be able to find every angle in a picture without missing one, and spot lines that never meet.'],
    warmIntro: ['Look at each clock. Make the two hands with your arms. Is the angle a right angle, like the corner of a book? Smaller? Or bigger?', 'Clock 1: 3 o’clock. Show me!'],
    predict: ['I will fold a torn piece of paper with wiggly edges, twice. Will the corner I make be a right angle, even though the paper is wiggly? Thumbs up for yes, down for no.'],
    exploreHints: ['Stuck folding: fold once to make a straight edge, then fold that edge onto itself so the two halves line up exactly.', 'Not sure if it is a right angle: put the corner of your checker into the angle. If both arms line up with the edges, it is a right angle.', 'Ready for more: find an angle that is exactly 2 right angles. (A straight line!)'],
    think: ['“Here are 4 lines from one point. I count the small angles first: 3. Then the angles made of 2 small ones: 2. Then 3 small ones: 1. 3 + 2 + 1 = 6. I go in order so I never miss one.”', '“2 lines make 1 angle, 3 lines make 3, 4 lines make 6. The jumps are 2, 3, 4… so the next jump is 5. I can predict without drawing.”', '“To count right angles in a picture I visit every point where lines meet, one by one, and write how many right angles are at each point. Then I add.”'],
    circulate: ['Ask: “Did you check that corner with your checker, or did you guess?”', 'Ask: “Which points have you visited? Which are left?”', 'Ask: “Do these two lines ever meet if we make them longer?”'],
    hints: ['Hint 1: “Use your right-angle checker on every corner.”', 'Hint 2: “Count the small angles first, then the bigger ones made of small ones.”', 'Hint 3: “Make a list of every pair of lines and test each pair.”'],
    talk: ['“Mei says an angle with longer arms is bigger. Do you agree? How can you test it?”', '“How did you make sure you did not miss any angles?”'],
    talkAns: 'No. The size of an angle is how far the arms open (how much one arm turns to reach the other). Draw two angles that open the same amount, one with long arms and one with short arms: the checker fits both the same way. To miss none, count in order: small angles first, or visit every meeting point.',
    close: ['“You checked with a tool, counted in order and found a pattern. That is how real detectives work. Well done!”']
  },

  deck: {
    today: 'Compare angles with a right angle, count angles and right angles without missing any, and find perpendicular and parallel lines.',
    warmGame: 'Clock angles. Make the clock hands with your arms: is the angle at 3, 1, 5, 9, 10 and 4 o’clock a right angle, smaller or bigger?',
    warmQs: [['How many right angles does a rectangle have?', '4'], ['How many sides does a hexagon have?', '6'], ['Name a capital letter made of 2 lines that meet at a right angle.', 'L (or T)'], ['Do the two long edges of a ruler ever meet?', 'No: they are parallel']],
    expSetup: ['Take any scrap of paper.', 'Fold it in half to make a straight fold.', 'Fold again so the fold lies exactly on itself.', 'Use the corner to hunt for right angles, smaller angles and bigger angles.'],
    expPic: 'a scrap of paper folded twice; the corner of the folds is a right angle, used as a checker.',
    expAsk: [['Why is the folded corner always a right angle?', 'The first fold makes a straight line. Folding it onto itself cuts the straight line into 2 equal angles: each is a right angle.'], ['Is an angle bigger if its arms are longer?', 'No. The size is how far the arms open, not how long they are.'], ['Where did you find angles bigger than a right angle?', 'For example an open laptop, a door opened wide, a clock at 5 o’clock.']],
    mini1: { head: 'Count the angles at a point', table: [['Lines from one point', '2', '3', '4', '5'], ['Angles', '1', '3', '6', '?']], body: ['4 lines from one point make 3 small angles.', 'Count in order: made of 1 small angle: 3. Made of 2: 2. Made of 3: 1.', 'Look for the pattern: 1, 3, 6. What comes next?'], ans: '4 lines: 3 + 2 + 1 = 6 angles. The jumps are 2, 3, 4, so 5 lines make 10.' },
    mini2: { head: 'Right angles where lines meet', body: ['A rectangle has one line from the middle of the top to the middle of the bottom.', 'Visit every point where lines meet: 4 corners have 1 right angle each; the 2 middle points have 2 each.', 'How many right angles altogether?'], ans: '4 + 4 = 8 right angles' },
    keyHead: 'Key idea: count in order, look for a pattern',
    keyBig: 'Visit every corner or meeting point, and count small angles first. When the counts grow, look for a pattern.',
    keySmall: 'An angle’s size is how far it opens, not how long its arms are.',
    brk: 'Body angles. Make a right angle with your arms, then a smaller angle, then a bigger one. Now hold your arms parallel, then perpendicular.',
    ws1: 'Page 1, in pairs: Q1 sort six angles, Q2 right angles inside shapes, Q3 angles at a point.',
    ws2: 'Page 2, on your own: Q4 lines in letters, Q5 draw lines on a grid (Q5c is Think Harder, if you have time), Q6 right angles in a window.'
  },

  qbank: {
    core: [
      { q: 'A right angle is a square corner, like the corner of a page. How many right angles does a rectangle have? Check with the corner of a piece of paper.', a: '4' },
      { q: 'At 3 o’clock the minute hand points at 12 and the hour hand points at 3. Is the angle between the hands smaller than, bigger than, or the same as the corner of a page?', a: 'The same: a right angle' },
      { q: 'At 2 o’clock, is the angle between the clock hands smaller or bigger than the corner of a page?', a: 'Smaller' },
      { q: 'Parallel lines are straight lines that stay the same distance apart and never meet, like the two rails of a train track. Name 2 capital letters that have a pair of parallel lines.', a: 'For example H and E (also F, N, Z, U, M).' },
      { q: 'Two straight lines cross like a plus sign (+). Each square corner where they cross is a right angle. How many right angles do they make?', a: '4' },
      { q: '3 lines go out from one point, spread out like a fan. An angle is the space between two lines. How many different angles can you find? (Draw it and count.)', a: '3 (2 small ones and 1 made of both)' }
    ],
    stretch: [
      { q: 'I have 4 sides and 4 right angles. My sides are not all the same length. What shape am I? How many pairs of parallel lines do I have?', a: 'A rectangle. 2 pairs of parallel lines.' },
      { q: 'A U shape is made of 5 squares: 3 squares in a row with 1 more square on top of each end square. How many right angles are inside it?', a: '6 (it has 8 corners; the 2 corners at the bottom of the gap are bigger than a right angle inside the shape).' },
      { q: 'Look at a clock face. For each o’clock time from 1 o’clock to 11 o’clock, is the angle between the hands (the short way round) smaller than, the same as, or bigger than a right angle? Put each time in the right group.', a: 'Smaller than a right angle: 1, 2, 10 and 11 o’clock. A right angle: 3 and 9 o’clock. Bigger: 4, 5, 6, 7 and 8 o’clock (at 6 o’clock the hands make a straight line).' },
      { q: 'The # sign is made of 4 lines: 2 upright lines and 2 lines across. How many pairs of parallel lines does it have? How many pairs of perpendicular lines?', a: '2 pairs of parallel lines and 4 pairs of perpendicular lines.' },
      { q: 'Draw me on square grid paper: (a) I have 4 sides, exactly 2 right angles and exactly 1 pair of parallel lines. (b) I have 4 sides and 2 pairs of parallel lines, but no right angles.', a: '(a) For example a shape with a long bottom, a shorter top parallel to it, one upright side and one slanted side. (b) For example a slanted parallelogram or a rhombus with no square corners.' },
      { q: 'How many right angles can you find in the letter E (4 straight lines)?', a: '4: 1 at the top corner, 2 where the middle line meets the upright line, 1 at the bottom corner.' },
      { q: 'Is the smaller angle between the clock hands at 4 o’clock the same size as at 8 o’clock?', a: 'Yes, in both the hands are 4 hour-marks apart the short way round.' },
      { q: 'The letter H is made of 3 straight lines: 2 upright lines and 1 line across. List every pair of lines. Which pairs are parallel and which pairs are perpendicular?', a: '3 pairs: the two upright lines (parallel), the line across with the left upright (perpendicular) and the line across with the right upright (perpendicular). So 1 pair of parallel lines and 2 pairs of perpendicular lines.' }
    ],
    challenge: [
      { q: '4 lines from one point make 6 angles. How many lines from one point are needed to make exactly 10 angles?', a: '5 lines (4 + 3 + 2 + 1 = 10).' },
      { q: 'A staircase is made of columns of 1, 2 and 3 squares standing side by side (3 steps). It has 6 right angles inside it. How many right angles are inside a staircase with 4 steps? With 5 steps? With 10 steps? Find a rule and explain why it works.', a: '4 steps: 7. 5 steps: 8. 10 steps: 13. The rule is: number of steps + 3. Each column has one square corner at its top right (that is the number of steps), the tallest column has one more at its top left, and there are 2 square corners at the bottom. The inside corners where one step meets the next are dents (bigger than a right angle), so they do not count.' },
      { q: 'A square has 2 lines down and 2 lines across inside it, like a noughts-and-crosses grid. How many right angles can you find?', a: '36: 4 corners × 1, 8 points on the sides × 2, and 4 crossing points × 4.' },
      { q: 'A 4-sided shape has 3 right angles. Draw it. Test the 4th angle with your checker. Can a 5-sided shape have exactly 3 right angles? Draw one.', a: 'The 4th angle is a right angle too (it is a rectangle). Yes: cut one corner off a rectangle with one slanted cut.' },
      { q: 'Mei says: "Perpendicular lines must be one going straight up and one going straight across." Is she right? On a square grid, draw two perpendicular lines that are both slanted. Check with your checker. How do you know they are perpendicular?', a: 'No. Perpendicular lines meet at a right angle however the page is turned. On a square grid, one line going 1 right and 1 up at each step and another going 1 left and 1 up at each step are perpendicular (and so are 2 right 1 up with 1 left 2 up). Turning the page so that one line is flat shows the other one standing straight up.' },
      { q: 'Ben says: “A shape with 4 sides and 2 pairs of parallel lines must have right angles.” Is he right?', a: 'No. A slanted parallelogram (or a rhombus) has 2 pairs of parallel lines but no right angles.' },
      { q: 'Make up your own "Which shape am I?" riddle about a shape on square grid paper. Use words like sides, right angles, parallel and perpendicular, and give 3 clues. Draw the answer. Then check: can a partner draw a DIFFERENT shape that fits your clues? If yes, add a clue.', a: 'Answers vary. Check that the drawn shape fits every clue and that the clues are about sides, right angles and parallel lines. Example: "I have 6 straight sides. I have 5 right angles inside me. I have one dent." (An L shape.) Other shapes could fit the first two clues, so the third clue matters.' },
      { q: 'A long rectangle is cut into 6 squares in a row by 5 lines. How many right angles can you find?', a: '24. 4 at the corners, and each of the 5 lines makes 2 right angles at the top and 2 at the bottom: 4 + 5 × 4 = 24.' },
      { q: 'Can a 6-sided shape have 6 right angles inside it? What is the most right angles a 6-sided shape can have inside?', a: 'No. The most is 5, for example an L shape. Children try to draw 6 square corners and always find a dent. A proof is not expected.' }
    ]
  },

  workbook: H => {
    const side = (fig, right) => `<div class="p img" style="display:flex;align-items:center;gap:22px;text-align:left"><div style="flex:none">${fig}</div><div style="flex:1">${right}</div></div>`;
    const W6 = [2100, 1300, 1300, 1300, 1300, 1300, 1300];
    return [
      H.q(1, 'Fold a right-angle checker. Use it to sort the angles a to f.', { before: 20, keepNext: true }),
      H.fig(q1Fig()),
      H.sub('', 'Smaller: ________    Right angle: ________    Bigger: ________'),
      H.q(2, 'How many right angles are INSIDE each shape? Check every corner with your checker.', { keepNext: true }),
      H.fig(q2Fig()),
      H.tbl([2475, 1856, 1856, 1857, 1856], [
        H.row(['Shape', 'A', 'B', 'C', 'D'].map((s, i) => H.cell(s, [2475, 1856, 1856, 1857, 1856][i], { bold: true, fill: 'EDEDED' }))),
        H.row([H.cell('Right angles inside', 2475, { bold: true }), ...[1856, 1856, 1857, 1856].map(w => H.cell(' ', w, { h: 40 }))])
      ]),
      H.q(3, 'These 6 lines all start at point O.', { keepNext: true }),
      side(q3Fig(), H.sub('a', 'How many angles? Count the small ones first, then those made of 2 small ones, and so on.') + H.sub('', 'Made of 1: ___  2: ___  3: ___  4: ___  5: ___') + H.sub('', 'Total: ________')),
      H.sub('b', 'Look for a pattern. 8 lines start at one point, spread out like these. How many angles are there?   ________'),

      H.q(4, 'Look at the lines in these letters. Parallel lines never meet and stay the same distance apart, like train tracks. Perpendicular lines meet at a right angle (a square corner). Write Yes or No in the table.', { pb: true, before: 0, keepNext: true }),
      H.fig(q4Fig()),
      H.tbl(W6, [
        H.row(['Letter', 'E', 'H', 'T', 'L', 'Z', 'N'].map((s, i) => H.cell(s, W6[i], { bold: true, fill: 'EDEDED' }))),
        H.row([H.cell('Parallel lines?', W6[0], { bold: true, size: 20 }), ...W6.slice(1).map(w => H.cell(' ', w, { h: 30 }))]),
        H.row([H.cell('Perpendicular lines?', W6[0], { bold: true, size: 20 }), ...W6.slice(1).map(w => H.cell(' ', w, { h: 30 }))])
      ]),
      H.sub('b', 'In the letter E: pairs of parallel lines ____    pairs of perpendicular lines ____'),
      H.q(5, 'Use a ruler. Draw on the grid.', { keepNext: true }),
      H.fig(q5Fig()),
      H.sub('a', 'Through C, draw a line parallel to AB.     (b)  Through D, draw a line perpendicular to AB.'),
      H.sub('c', 'Think harder (if you have time): through G, draw a line perpendicular to EF. Check it with your checker. Hint: try 1 right and 2 down.'),
      H.q(6, 'How many right angles can you find in this window?', { keepNext: true }),
      side(q6Fig(), H.sub('', 'Visit every point where lines meet. Write how many right angles are at each point, then add.') + H.sub('', 'Right angles altogether:  ________'))
    ];
  }
};
