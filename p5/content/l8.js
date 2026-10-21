// Math Inquirers P5 — Lesson 8: Angle Chasers (angles on a line and at a point, vertically opposite, triangles, parallelogram, rhombus, trapezium)
// Every figure is built from coordinates and every stated angle is checked by chk() (it throws if the drawing disagrees).
// Every answer was worked out and checked.

const N = '#1B2A49', Y = '#FFC93C', SKY = '#DDEBF7', TEAL = '#1F7A6F', RED = '#D64545', WH = '#FFFFFF', SOFT = '#FFF0C2';
const F = 'Fredoka, Arial, sans-serif';
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const f1 = v => (+v).toFixed(1);
const rad = d => d * Math.PI / 180;
// polar point: centre (x, y), distance r, maths angle in degrees (anticlockwise, y up) -> SVG point
const P = (x, y, r, deg) => [x + r * Math.cos(rad(deg)), y - r * Math.sin(rad(deg))];
const ang = (v, a, b) => {
  let d = Math.abs(Math.atan2(a[1] - v[1], a[0] - v[0]) - Math.atan2(b[1] - v[1], b[0] - v[0])) * 180 / Math.PI;
  return d > 180 ? 360 - d : d;
};
const chk = (v, a, b, exp, name) => { if (Math.abs(ang(v, a, b) - exp) > 0.05) throw new Error('Angle ' + name + ' is ' + ang(v, a, b).toFixed(2) + ' not ' + exp); };
const dist = (a, b) => Math.hypot(a[0] - b[0], a[1] - b[1]);
const chkEq = (a, b, c, d, name) => { if (Math.abs(dist(a, b) - dist(c, d)) > 0.05) throw new Error('Sides ' + name + ' are not equal'); };
const chkPar = (a, b, c, d, name) => { const x = (b[0] - a[0]) * (d[1] - c[1]) - (b[1] - a[1]) * (d[0] - c[0]); if (Math.abs(x) > 0.5) throw new Error('Not parallel ' + name); };

const svg = (w, h, label, inner, k = 1) => `<svg aria-label="${esc(label)}" viewBox="0 0 ${w} ${h}" xmlns="http://www.w3.org/2000/svg" style="width:${Math.round(w * k)}px;max-width:100%">${inner}</svg>`;
const tx = (x, y, s, size = 16, fill = N, anchor = 'middle', weight = 700) => `<text x="${f1(x)}" y="${f1(y)}" font-size="${size}" font-weight="${weight}" text-anchor="${anchor}" fill="${fill}" font-family="${F}">${esc(s)}</text>`;
const line = (a, b, col = N, sw = 3, dash = '') => `<line x1="${f1(a[0])}" y1="${f1(a[1])}" x2="${f1(b[0])}" y2="${f1(b[1])}" stroke="${col}" stroke-width="${sw}" stroke-linecap="round"${dash ? ` stroke-dasharray="${dash}"` : ''}/>`;
const poly = (pts, fill = SKY, sw = 3) => `<polygon points="${pts.map(p => f1(p[0]) + ',' + f1(p[1])).join(' ')}" fill="${fill}" stroke="${N}" stroke-width="${sw}" stroke-linejoin="round"/>`;
// angle arc at v between rays to a and b (the smaller angle). label: text at the middle of the wedge, or '' for none
const arc = (v, a, b, r, label = '', col = RED, lr = 0, fs = 18) => {
  const a1 = Math.atan2(a[1] - v[1], a[0] - v[0]), a2 = Math.atan2(b[1] - v[1], b[0] - v[0]);
  let d = a2 - a1; while (d > Math.PI) d -= 2 * Math.PI; while (d < -Math.PI) d += 2 * Math.PI;
  const p1 = [v[0] + r * Math.cos(a1), v[1] + r * Math.sin(a1)], p2 = [v[0] + r * Math.cos(a2), v[1] + r * Math.sin(a2)];
  let s = `<path d="M${f1(p1[0])} ${f1(p1[1])} A${r} ${r} 0 0 ${d > 0 ? 1 : 0} ${f1(p2[0])} ${f1(p2[1])}" fill="none" stroke="${col}" stroke-width="3"/>`;
  if (label) { const am = a1 + d / 2, rr = lr || r + 22; s += tx(v[0] + rr * Math.cos(am), v[1] + rr * Math.sin(am) + fs * 0.35, label, fs, col); }
  return s;
};
const square = (v, a, b, s = 14) => { // right-angle mark at v between rays to a and b
  const u = [a[0] - v[0], a[1] - v[1]], w = [b[0] - v[0], b[1] - v[1]], lu = Math.hypot(...u), lw = Math.hypot(...w);
  const p1 = [v[0] + u[0] / lu * s, v[1] + u[1] / lu * s], p2 = [p1[0] + w[0] / lw * s, p1[1] + w[1] / lw * s], p3 = [v[0] + w[0] / lw * s, v[1] + w[1] / lw * s];
  return `<path d="M${f1(p1[0])} ${f1(p1[1])} L${f1(p2[0])} ${f1(p2[1])} L${f1(p3[0])} ${f1(p3[1])}" fill="none" stroke="${RED}" stroke-width="2.5"/>`;
};
// equal-side tick mark(s) across the middle of a side
const tick = (a, b, n = 1) => {
  const m = [(a[0] + b[0]) / 2, (a[1] + b[1]) / 2], l = dist(a, b), u = [(b[0] - a[0]) / l, (b[1] - a[1]) / l], nn = [-u[1], u[0]];
  let s = '';
  for (let i = 0; i < n; i++) { const o = (i - (n - 1) / 2) * 7, c = [m[0] + u[0] * o, m[1] + u[1] * o]; s += `<line x1="${f1(c[0] - nn[0] * 8)}" y1="${f1(c[1] - nn[1] * 8)}" x2="${f1(c[0] + nn[0] * 8)}" y2="${f1(c[1] + nn[1] * 8)}" stroke="${RED}" stroke-width="3"/>`; }
  return s;
};
// parallel-line arrow on a side
const parr = (a, b) => {
  const m = [(a[0] + b[0]) / 2, (a[1] + b[1]) / 2], l = dist(a, b), u = [(b[0] - a[0]) / l, (b[1] - a[1]) / l], nn = [-u[1], u[0]];
  const t = [m[0] + u[0] * 8, m[1] + u[1] * 8], p = [m[0] - u[0] * 6 + nn[0] * 7, m[1] - u[1] * 6 + nn[1] * 7], q = [m[0] - u[0] * 6 - nn[0] * 7, m[1] - u[1] * 6 - nn[1] * 7];
  return `<polyline points="${f1(p[0])},${f1(p[1])} ${f1(t[0])},${f1(t[1])} ${f1(q[0])},${f1(q[1])}" fill="none" stroke="${TEAL}" stroke-width="3"/>`;
};
const pl = (p, name, dx, dy, size = 20) => tx(p[0] + dx, p[1] + dy, name, size, N);

// ---------- Q1: two lines crossing (left) and four angles round a point (right) ----------
const q1Fig = () => {
  const O = [140, 96], A = P(...O, 95, 200), B = P(...O, 95, 20), C = P(...O, 95, 132), D = P(...O, 95, 312);
  chk(O, A, C, 68, 'AOC'); chk(O, B, C, 112, 'BOC'); chk(O, B, D, 68, 'BOD'); chk(O, A, D, 112, 'AOD');
  let s = line(A, B) + line(C, D) + arc(O, A, C, 30, '68°', RED, 58);
  s += pl(A, 'A', -14, 6) + pl(B, 'B', 14, 6) + pl(C, 'C', -4, -10) + pl(D, 'D', 6, 20) + pl(O, 'O', 14, 20);
  const Q = [430, 96], d1 = P(...Q, 80, 0), d2 = P(...Q, 80, 95), d3 = P(...Q, 80, 225), d4 = P(...Q, 80, 295);
  chk(Q, d1, d2, 95, 'q1'); chk(Q, d2, d3, 130, 'q2'); chk(Q, d3, d4, 70, 'q3'); chk(Q, d4, d1, 65, 'q4');
  s += [d1, d2, d3, d4].map(d => line(Q, d)).join('');
  s += arc(Q, d1, d2, 26, '95°', RED, 50) + arc(Q, d2, d3, 26, '130°', RED, 52) + arc(Q, d3, d4, 26, '70°', RED, 50) + arc(Q, d4, d1, 26, '?', RED, 48);
  return svg(600, 190, 'Left: two straight lines AB and CD cross at O and angle AOC is 68 degrees. Right: four angles meet at a point and measure 95, 130, 70 and a question mark degrees.', s, 0.85);
};

// ---------- Q2: parallelogram ABCD (A = 72), rhombus PQRS (P = 64) with diagonal PR, trapezium (A = 110, B = 80) ----------
const q3Fig = () => {
  // parallelogram: A bottom-left, sides 120 and 80
  const A = [16, 150], B = [A[0] + 120, A[1]], Dd = P(...A, 80, 72), C = [Dd[0] + 120, Dd[1]];
  chk(A, B, Dd, 72, 'DAB'); chk(B, A, C, 108, 'ABC'); chkPar(A, B, Dd, C, 'AB DC'); chkEq(A, Dd, B, C, 'AD BC');
  let s = poly([A, B, C, Dd], SKY) + arc(A, B, Dd, 26, '72°', RED, 44) + tick(A, B) + tick(Dd, C) + tick(A, Dd, 2) + tick(B, C, 2);
  s += pl(A, 'A', -10, 14) + pl(B, 'B', 8, 16) + pl(C, 'C', 12, 2) + pl(Dd, 'D', -12, 2);
  // rhombus
  const p = [236, 150], q = [p[0] + 96, p[1]], sp = P(...p, 96, 64), r = [sp[0] + 96, sp[1]];
  chk(p, q, sp, 64, 'QPS'); chk(q, p, r, 116, 'PQR'); chk(p, q, r, 32, 'QPR'); chkEq(p, q, q, r, 'PQ QR'); chkEq(p, q, p, sp, 'PQ PS');
  s += poly([p, q, r, sp], SKY) + line(p, r, TEAL, 3, '7 5') + arc(p, q, sp, 26) + (() => { const t = P(...p, 62, 50); return tx(t[0], t[1] + 6, '64°', 18, RED); })() + arc(p, q, r, 62, '?', RED, 84);
  s += tick(p, q) + tick(q, r) + tick(r, sp) + tick(sp, p);
  s += pl(p, 'P', -10, 14) + pl(q, 'Q', 8, 16) + pl(r, 'R', 12, 2) + pl(sp, 'S', -12, 2);
  // trapezium: AB // DC, A = 110, B = 80
  const tA = [462, 40], tB = [tA[0] + 100, tA[1]], tD = P(...tA, 100, 250);
  // leg BC leaves B at maths angle 260 (angle ABC = 80) and reaches the level of D
  const L = (tD[1] - tB[1]) / Math.sin(rad(80));
  const BC = P(...tB, L, 260);
  const C2 = [BC[0], tD[1]];
  chk(tA, tB, tD, 110, 'trap A'); chk(tB, tA, C2, 80, 'trap B'); chkPar(tA, tB, tD, C2, 'trap AB DC'); chk(tD, tA, C2, 70, 'trap D'); chk(C2, tD, tB, 100, 'trap C');
  s += poly([tA, tB, C2, tD], SKY) + parr(tA, tB) + parr(tD, C2) + arc(tA, tB, tD, 24, '110°', RED, 50) + arc(tB, tA, C2, 24, '80°', RED, 46) + arc(tD, tA, C2, 24, '?', RED, 46) + arc(C2, tB, tD, 24, '?', RED, 46);
  s += pl(tA, 'A', -14, 2) + pl(tB, 'B', 14, 2) + pl(C2, 'C', 14, 18) + pl(tD, 'D', -14, 18);
  s += tx(76, 176, 'Parallelogram', 15, TEAL, 'middle', 600) + tx(284, 176, 'Rhombus', 15, TEAL, 'middle', 600) + tx(500, 176, 'Trapezium', 15, TEAL, 'middle', 600);
  return svg(600, 184, 'Three shapes. A parallelogram ABCD with angle A 72 degrees and equal opposite sides. A rhombus PQRS with angle P 64 degrees, all sides equal, and the diagonal PR drawn dashed. A trapezium ABCD with AB parallel to DC, angle A 110 degrees and angle B 80 degrees.', s, 1);
};

// ---------- Q4 (chain): triangle ABC, D on BC, AB = AD, angle B = 62, angle DAC = 38 ----------
const q4Fig = () => {
  const L = 130, B = [50, 168], A = P(...B, L, 62), D = [B[0] + 2 * L * Math.cos(rad(62)), B[1]];
  const DC = L * Math.sin(rad(38)) / Math.sin(rad(24)), C = [D[0] + DC, B[1]];
  chkEq(B, A, A, D, 'AB AD'); chk(B, A, C, 62, 'B'); chk(A, D, C, 38, 'DAC'); chk(D, A, B, 62, 'ADB'); chk(D, A, C, 118, 'ADC'); chk(C, A, B, 24, 'C'); chk(A, B, D, 56, 'BAD');
  let s = poly([A, B, C], SKY) + line(A, D) + tick(B, A) + tick(A, D);
  s += arc(B, C, A, 34, '62°', RED, 60) + arc(A, D, C, 38, '38°', RED, 66);
  s += pl(A, 'A', 0, -8) + pl(B, 'B', -12, 16) + pl(D, 'D', 0, 22) + pl(C, 'C', 14, 16);
  return svg(600, 190, 'Triangle ABC. D is a point on BC with AB equal to AD. Angle ABC is 62 degrees and angle DAC is 38 degrees. The line AD is drawn.', s, 0.85);
};

// ---------- Q5: parallelogram ABCD, E on DC with DA = DE, angle ABC = 56 ----------
const q5Fig = () => {
  const D = [70, 160], a = 100, c = 200, A = P(...D, a, 56), B = [A[0] + c, A[1]], C = [D[0] + c, D[1]], E = [D[0] + a, D[1]];
  chkPar(A, B, D, C, 'AB DC'); chkEq(A, D, B, C, 'AD BC'); chkEq(D, A, D, E, 'DA DE');
  chk(B, A, C, 56, 'ABC'); chk(D, A, C, 56, 'ADC'); chk(E, D, A, 62, 'DEA'); chk(E, A, C, 118, 'AEC'); chk(A, E, B, 62, 'EAB'); chk(A, D, B, 124, 'DAB');
  let s = poly([A, B, C, D], SKY) + line(A, E) + tick(D, A) + tick(D, E);
  s += arc(B, A, C, 30, '56°', RED, 56);
  s += pl(A, 'A', -2, -10) + pl(B, 'B', 4, -10) + pl(C, 'C', 14, 18) + pl(D, 'D', -12, 18) + pl(E, 'E', 0, 22);
  return svg(600, 190, 'Parallelogram ABCD with E a point on the side DC and DA equal to DE. Angle ABC is 56 degrees. The line AE is drawn.', s, 0.85);
};

module.exports = {
  lesson: {
    n: 8, week: 4, session: 'B', title: 'Angle Chasers', topic: 'Angles, Triangles and Quadrilaterals',
    objective: 'Use the angle facts (straight line 180°, point 360°, vertically opposite, triangle 180°, isosceles and equilateral triangles, parallelogram, rhombus, trapezium) to chase unknown angles through a figure, step by step, giving a reason for every step; and list every case when only one angle of an isosceles triangle is given.',
    skills: 'Angle-chase chains with reasons, using a diagram carefully, finding all cases, checking by adding, explaining',
    materials: 'Paper, ruler, pencil, scissors, protractor, red and blue pencils, the dot-grid cut-out, mini whiteboards, workbook.',
    online: 'Children tear or cut the corners of a paper triangle and quadrilateral on camera. The tutor screen-shares the slides and draws on the figures with the annotation tool. Children keep a red pencil for the angle they are chasing.',
    warmup: 'Guess the angle: four angles drawn on the slide (30°, 90°, 120°, 150°). Children estimate each one using 90° and 45° as markers, then the tutor reveals the true sizes.',
    explore: 'Tear it up: draw any triangle and tear off its three corners; fit them together on a straight line. Then do the same with a four-sided shape and fit the four corners round a point. Predict first, then say what you notice.',
    mini: 'An angle chase is a chain: find one angle, say WHY, and use it to find the next. The reasons: angles on a straight line add up to 180°; angles at a point add up to 360°; vertically opposite angles are equal; angles in a triangle add up to 180°; an isosceles triangle has equal base angles; a parallelogram has equal opposite angles and adjacent angles that add up to 180°; a rhombus is a parallelogram with 4 equal sides; between the parallel sides of a trapezium the angles add up to 180°.',
    share: 'Ravi says an isosceles triangle can have an angle bigger than 90°. Mei says it cannot. Who is right? Can it have a right angle? Find the other two angles each time.',
    exit: { q: 'In triangle PQR, PQ = PR and angle QPR = 44°. Find angle PQR. Write the reason for each step.', a: '68° (angles in a triangle add up to 180°: 180° − 44° = 136°; PQ = PR so the base angles are equal: 136° ÷ 2 = 68°)' },
    mistakes: ['Measuring or guessing from the picture instead of using an angle fact (drawings are not always to scale).', 'Calling the wrong angles equal in an isosceles triangle: the equal angles are opposite the equal sides, which are the base angles, not the angle between the equal sides.', 'Giving only one case when one angle of an isosceles triangle is known (the given angle could be the top angle or a base angle).'],
    extension: 'Draw a triangle and put the three angle labels 40°, 60° and 80° on the corners. Cut the corners off and fit them together. Now do the same with any four-sided shape. Explain in one sentence why a four-sided shape always gives 360°. (Hint: draw a line from one corner to the opposite corner.)',
    key: [
      ['Q1', '(a) 112° (angles on a straight line: 180° − 68°)  (b) 68° (vertically opposite AOC)  (c) 112° (vertically opposite BOC)  (d) 65° (angles at a point: 360° − 95° − 130° − 70°)'],
      ['Q2', '(a) Parallelogram: B = 108° (adjacent angles add up to 180°), C = 72° (opposite A), D = 108° (opposite B)  (b) Rhombus: PQR = 116° (180° − 64°). Triangle PQR is isosceles (PQ = QR), so QPR = (180° − 116°) ÷ 2 = 32°  (c) Trapezium: D = 70° (180° − 110°), C = 100° (180° − 80°)'],
      ['Q3', '(a) ADB = 62° (AB = AD, so the base angles are equal)  (b) BAD = 56° (180° − 62° − 62°)  (c) ADC = 118° (angles on a straight line: 180° − 62°)  (d) ACD = 24° (180° − 118° − 38°)'],
      ['Q4', '(a) ADC = 56° (opposite angles of a parallelogram are equal)  (b) DEA = 62° (DA = DE, so (180° − 56°) ÷ 2)  (c) AEC = 118° (straight line: 180° − 62°)  (d) EAB = 62° (angle DAB = 180° − 56° = 124°, then 124° − 62°)'],
      ['Q5', '(a) Two triangles: 50°, 50°, 80° (the 50° angle is a base angle) or 50°, 65°, 65° (50° is the top angle)  (b) Only one: 100°, 40°, 40°. The 100° angle must be the top angle, because two angles of 100° would already be 200°.']
    ]
  },

  script: {
    hook: ['Welcome back, inquirers! Today we are detectives again, and the clue is an angle. Surveyors, builders and pilots all use angles to find things they cannot measure. We will find angles without using a protractor at all.', 'Notice it, test it, explain why. Today "explain why" has a special meaning: every angle you find needs a REASON.'],
    warmIntro: ['Here are four angles. You are not allowed a protractor. Use the corner of your paper: that is 90°. Fold it in half: that is 45°. Write your guesses on your whiteboard.', 'Which was the hardest to guess? How did you decide?'],
    predict: ['Draw any triangle and tear off the three corners. What do you think will happen when you put the corners together side by side? Write it down before you try.', 'Now a four-sided shape. Will the four corners fit on a straight line, or round a point?'],
    exploreHints: ['Stuck: put the three pointed corners together so that the points touch. Are they flat along the bottom?', 'Corners do not fit: draw a long straight line first and put the corners along it.', 'Finished early: draw a triangle with a right angle. Do the corners still fit the same way?'],
    think: ['“I want the angle next to 75° on a straight line. A straight line is 180°, so 180 take away 75 is 105. My reason: angles on a straight line add up to 180°.”', '“Triangle with 50° and 30°: the three angles add up to 180°, so the third is 180 − 50 − 30 = 100°. My reason: angles in a triangle add up to 180°.”', '“This triangle is isosceles and the top angle is 50°. The other two angles are equal. 180 − 50 = 130, and 130 ÷ 2 = 65 each. My reason: base angles of an isosceles triangle are equal.”'],
    circulate: ['Ask: “What is your reason for that angle?”', 'Ask: “Which angle did you find first? Which angle does it help you find next?”', 'Ask: “Do your angles add up to 180° in each triangle? Check.”'],
    hints: ['Hint 1: “Write down every angle you know first.”', 'Hint 2: “Look for a straight line, a triangle or a pair of equal sides. Each one gives you an angle fact.”', 'Hint 3: “Find ONE new angle and give its reason. Then look again: what can you find with it?”'],
    talk: ['“Ravi says an isosceles triangle can have an angle bigger than 90°. Mei says it cannot. Who is right?”', '“Can an isosceles triangle have a right angle? What are the other two angles?”'],
    talkAns: 'Ravi is right. An isosceles triangle can have one big angle: for example 120°, 30°, 30°. It cannot have two angles of 90° or more, because they would already add up to 180° or more. It can have exactly one right angle: 90°, 45°, 45°. Mei is thinking of the base angles, and she is right about those: the two equal base angles are always less than 90°.',
    close: ['“Today you chased angles with reasons. A detective who can say why is much harder to argue with. Well done, inquirers!”', '“Show me your exit ticket and I will stamp your inquiry journal.”']
  },

  deck: {
    today: 'Chase unknown angles through triangles, parallelograms, rhombuses and trapezia, giving a reason for every step.',
    warmGame: 'Guess the angle. Four angles are drawn on the slide (30°, 90°, 120°, 150°). Use the corner of your paper (90°) and a fold (45°) to estimate each one. Write A, B, C and D guesses, then check.',
    warmQs: [['Angles on a straight line: 180° − 125° = ?', '55°'], ['Angles at a point: 150°, 90°, 80° and one more. Find it.', '40°'], ['A triangle has angles 90° and 35°. Third angle?', '55°'], ['Isosceles triangle, top angle 40°. One base angle?', '70°'], ['A parallelogram has a 70° angle. What is the angle next to it?', '110°']],
    expSetup: ['Draw any triangle. Colour its three corners red, blue and green.', 'Tear off the three corners. Fit them together side by side with the points touching.', 'Draw any four-sided shape and tear off its four corners. Fit them round a point.', 'Say what you notice. Do you think it works for every triangle?'],
    expPic: 'a triangle with its three corners coloured, and the three torn corners fitted side by side on a straight line; beside it a four-sided shape with four coloured corners fitted round a point.',
    expAsk: [['Where did the three corners of a triangle fit?', 'On a straight line: they add up to 180°.'], ['Where did the four corners of a four-sided shape fit?', 'Round a point: they add up to 360°.'], ['Does it work for every triangle?', 'Yes, but the best test is to try a very different triangle (fat, thin, right-angled) and see.']],
    mini1: { head: 'An angle chase with reasons', body: ['Triangle PQR. S is a point on QR. Angle Q is 50°, angle PSQ is 75°, angle R is 30°.', 'Find angle QPS, angle PSR and angle SPR. Give a reason for each.'], ans: 'QPS = 55° (angles in a triangle), PSR = 105° (straight line), SPR = 45° (angles in a triangle). Check: 55° + 45° = 100° = angle QPR.' },
    mini2: { head: 'Rhombus and its diagonal', body: ['Rhombus ABCD. Angle DAB is 50°. The diagonal BD is drawn.', 'Find angle ABC, then angle ABD. Give a reason for each.'], ans: 'ABC = 130° (adjacent angles of a rhombus add up to 180°), ABD = 65° (AB = AD, so the base angles are equal: 130° ÷ 2).' },
    keyHead: 'Key idea: one angle, one reason',
    keyBig: 'Find one angle. Say WHY. Use it to find the next one. That is an angle chase.',
    keySmall: 'Do not measure the drawing: use straight line 180°, point 360°, triangle 180°, equal base angles, and the shape facts.',
    brk: 'Angle statues. The tutor calls an angle: 90° is arms in an L, 180° is arms straight out, 45° is arms half-way. Children make it with their arms on camera. Then call 360° (turn all the way round!).',
    ws1: 'Page 1, in pairs: Q1 straight lines, a point and vertically opposite angles, Q2 parallelogram, rhombus and trapezium.',
    ws2: 'Page 2, on your own: Q3 angle chase in a triangle, Q4 parallelogram and isosceles triangle, Q5 find every isosceles triangle.'
  },

  qbank: {
    core: [
      { q: 'Two angles on a straight line. One is 127°. What is the other?', a: '53° (180° − 127°)' },
      { q: 'Four angles meet at a point. Three are 150°, 90° and 80°. What is the fourth?', a: '40° (360° − 320°)' },
      { q: 'Two angles of a triangle are 48° and 67°. What is the third angle?', a: '65° (180° − 115°)' },
      { q: 'An isosceles triangle has a top angle of 30°. What is each base angle?', a: '75° ((180° − 30°) ÷ 2)' },
      { q: 'A parallelogram has one angle of 70°. What are the other three angles?', a: '110°, 70°, 110° (opposite angles are equal; adjacent angles add up to 180°)' },
      { q: 'In rhombus ABCD, angle ABC is 124°. What is angle BCD?', a: '56° (adjacent angles add up to 180°)' }
    ],
    stretch: [
      { q: 'Two straight lines cross. One of the four angles is 38°. What are the other three? How many different sizes are there?', a: '142°, 38°, 142°. There are two different sizes: 38° and 142°.' },
      { q: 'An isosceles triangle has an angle of 110°. Find the other two angles. Why is there only one answer?', a: '35° and 35°. 110° cannot be a base angle (two of them would be 220°), so it is the top angle and 180° − 110° = 70° is shared by two equal base angles.' },
      { q: 'In trapezium ABCD, AB is parallel to DC. Angle DAB is 84° and angle ABC is 97°. Find angle ADC and angle BCD.', a: 'ADC = 96° and BCD = 83° (angles between the parallel sides add up to 180°). Check: 84° + 97° + 96° + 83° = 360°.' },
      { q: 'ABCD is a square. CDE is an equilateral triangle, and E is outside the square. Find angle ADE and angle DAE.', a: 'ADE = 150° (90° + 60°). Triangle ADE is isosceles (AD = DE), so DAE = (180° − 150°) ÷ 2 = 15°.' },
      { q: 'Rhombus ABCD has angle ABC = 100°. The diagonal AC is drawn. Find angle BAC.', a: '40° (AB = BC, so triangle ABC is isosceles: (180° − 100°) ÷ 2)' },
      { q: 'What is the smaller angle between the hands of a clock at 5 o\'clock? At 8 o\'clock?', a: '150° at 5 o\'clock (5 × 30°). At 8 o\'clock the big angle is 240°, so the smaller angle is 120°.' },
      { q: 'How many degrees does the minute hand of a clock turn through in 10 minutes? In 45 minutes?', a: '60° (a full turn of 360° takes 60 minutes, so 6° a minute) and 270°.' },
      { q: 'In a parallelogram ABCD, angle A is 40° bigger than angle B. Find angle A and angle B.', a: 'A = 110°, B = 70°. Adjacent angles add up to 180°; 180° − 40° = 140°, and 140° ÷ 2 = 70°, so A is 70° + 40° = 110°.' }
    ],
    challenge: [
      { q: 'Two identical right-angled triangles with angles 30°, 60° and 90° are joined with their shorter sides (the sides opposite the 30° angles) touching, with the right angles together, to make one big triangle. What are the angles of the big triangle?', a: '30°, 30°, 120°. The two right angles make a straight line, and the two 60° angles together make 120°.' },
      { q: 'Three angles of a four-sided shape are 95°, 110° and 85°. What is the fourth angle? Could the shape be a parallelogram?', a: '70° (360° − 290°). It cannot be a parallelogram: the angles 95°, 110°, 85° and 70° have no equal opposite pairs.' },
      { q: 'In triangle ABC, angle B = 70° and angle C = 50°. The line AD cuts angle A into two equal angles, with D on BC. Find angle ADB and angle ADC.', a: 'Angle A = 60°, so each part is 30°. ADB = 180° − 70° − 30° = 80°, and ADC = 180° − 80° = 100° (check: 30° + 50° + 100° = 180°).' },
      { q: 'An isosceles triangle has angles that are all whole numbers of degrees, and one of them is 20°. List every possible triangle.', a: '20°, 20°, 140° and 20°, 80°, 80°.' },
      { q: 'Triangle ABC has angle A = 20°, angle B = 60° and angle C = 100°. D is a point on AB so that angle ACD = 40°. Find the three angles of triangle ACD and the three angles of triangle BCD.', a: 'Triangle ACD: 20°, 40°, 120°. Triangle BCD: angle BCD = 60°, B = 60° and D = 60°, so it is equilateral.' },
      { q: 'In parallelogram ABCD, angle ABC = 72°. E is a point on AD with AB = AE. Find angle ABE and angle EBC.', a: 'Angle BAD = 108° (adjacent angles add up to 180°). Triangle ABE is isosceles with top angle 108°, so ABE = 36°. Then EBC = 72° − 36° = 36°.' },
      { q: 'ABC is an isosceles triangle with AB = AC and angle BAC = 40°. D is a point on AC with BD = BC. Find angle ABD.', a: '30°. Angles B and C are (180° − 40°) ÷ 2 = 70°. In triangle BCD, BD = BC, so angle BDC = angle C = 70°, which makes angle CBD = 40°. Then ABD = 70° − 40° = 30°.' },
      { q: 'ABCD is a square. E is a point inside it so that ABE is an equilateral triangle. Find angle DEC.', a: '150°. AE = AB = AD, so triangle ADE is isosceles with angle DAE = 90° − 60° = 30°, which makes angle AED = 75°. In the same way angle BEC = 75°. Angle AEB = 60°. Round E: 360° − 75° − 75° − 60° = 150°.' },
      { q: 'In an isosceles triangle, one angle is 30° bigger than another angle. Find all the possible sets of three angles.', a: 'Two sets: 50°, 50°, 80° and 40°, 70°, 70°. (If the top angle is 30° bigger than a base angle: 3 equal parts and 30° make 180°, so base 50°. If a base angle is 30° bigger than the top: top 40°, base 70°.)' }
    ]
  },

  workbook: H => [
    H.q(1, 'Left: straight lines AB and CD cross at O. Right: four angles meet at a point. Drawings are not to scale, so do not use a protractor.', { before: 20, keepNext: true }),
    H.fig(q1Fig()),
    H.sub('a', 'Angle BOC = ______    (b) Angle BOD = ______    (c) Angle AOD = ______', { after: 40 }),
    H.sub('d', 'The missing angle at the point on the right = ________.   Which angle fact did you use? ______________________', { after: 40 }),
    H.q(2, 'Find the missing angles. Write each angle fact you use.', { keepNext: true, before: 100 }),
    H.fig(q3Fig()),
    H.sub('a', 'Parallelogram:   angle B = ______   angle C = ______   angle D = ______', { after: 40 }),
    H.sub('b', 'Rhombus:   angle PQR = ______   angle QPR = ______  (hint: PQ = QR)', { after: 40 }),
    H.sub('c', 'Trapezium:   angle D = ______   angle C = ______', { after: 40 }),
    H.q(3, 'In triangle ABC, D is on BC and AB = AD. Angle B = 62° and angle DAC = 38°. Find each angle and write the reason.', { pb: true, before: 0, keepNext: true }),
    H.fig(q4Fig()),
    H.sub('a', 'Angle ADB = _____  because ______________________', { after: 40 }),
    H.sub('b', 'Angle BAD = ______  because ______________________', { after: 40 }),
    H.sub('c', 'Angle ADC = ______  because ______________________', { after: 40 }),
    H.sub('d', 'Angle ACD = ______  because ______________________', { after: 40 }),
    H.q(4, 'ABCD is a parallelogram. E is a point on DC with DA = DE. Angle ABC = 56°.', { keepNext: true, before: 60 }),
    H.fig(q5Fig()),
    H.sub('a', 'ADC = _____    (b) DEA = _____    (c) AEC = _____    (d) EAB = _____', { after: 40 }),
    H.ans('Show how you found angle EAB:', 20),
    H.q(5, 'An isosceles triangle has one angle of 50°. What could the other two angles be? Find every case.', { keepNext: true, before: 60 }),
    H.sub('a', 'List both:  _________________  and  _________________', { after: 40 }),
    H.sub('b', 'An isosceles triangle has one angle of 100°. How many different triangles can you make? Explain.', { after: 40 }),
    ...H.lines(1)
  ]
};
