// Math Inquirers P4 — Lesson 6: Angle Turns (estimating and measuring angles, finding all the angles in a fan,
// angles on a clock face, turns on the 8-point compass, angles in squares and rectangles)
// Every angle in the drawings is drawn to size: coordinates are computed with cos and sin, so a protractor reads true.
// Every answer below was worked out and checked (compass turns, clock angles and the "find all" items with a short Python script).

const NAVY = '#1B2A49', YEL = '#FFC93C', SKY = '#DDEBF7', TEAL = '#1F7A6F', WHITE = '#FFFFFF', RED = '#D64545';
const T = (x, y, s, size = 16, fill = NAVY, anchor = 'middle', weight = 700) => `<text x="${x.toFixed(1)}" y="${y.toFixed(1)}" font-size="${size}" font-weight="${weight}" text-anchor="${anchor}" fill="${fill}" font-family="Arial">${s}</text>`;
const rad = d => d * Math.PI / 180;
const pt = (cx, cy, r, deg) => [cx + r * Math.cos(rad(deg)), cy - r * Math.sin(rad(deg))]; // maths angle: 0° points right, anticlockwise is positive
const L = (a, b, w = 3, c = NAVY) => `<line x1="${a[0].toFixed(1)}" y1="${a[1].toFixed(1)}" x2="${b[0].toFixed(1)}" y2="${b[1].toFixed(1)}" stroke="${c}" stroke-width="${w}" stroke-linecap="round"/>`;
const arc = (cx, cy, r, d0, d1, c = TEAL, w = 2.5) => { const a = pt(cx, cy, r, d0), b = pt(cx, cy, r, d1); return `<path d="M${a[0].toFixed(1)} ${a[1].toFixed(1)} A${r} ${r} 0 ${d1 - d0 > 180 ? 1 : 0} 0 ${b[0].toFixed(1)} ${b[1].toFixed(1)}" fill="none" stroke="${c}" stroke-width="${w}"/>`; };
const sq = (cx, cy, r, d0) => { const a = pt(cx, cy, r, d0), b = pt(cx, cy, r * 1.414, d0 + 45), c = pt(cx, cy, r, d0 + 90); return `<path d="M${a[0].toFixed(1)} ${a[1].toFixed(1)} L${b[0].toFixed(1)} ${b[1].toFixed(1)} L${c[0].toFixed(1)} ${c[1].toFixed(1)}" fill="none" stroke="${TEAL}" stroke-width="2.5"/>`; };

// one angle placed in the middle of a panel: arms from d0 to d1 (maths degrees), arm length r
const angleIn = (px, py, pw, ph, d0, d1, r, name) => {
  const ps = [[0, 0], pt(0, 0, r, d0), pt(0, 0, r, d1)];
  const xs = ps.map(p => p[0]), ys = ps.map(p => p[1]);
  const cx = px + pw / 2 - (Math.min(...xs) + Math.max(...xs)) / 2, cy = py + ph / 2 - (Math.min(...ys) + Math.max(...ys)) / 2;
  const lab = pt(cx, cy, 48, (d0 + d1) / 2);
  return L([cx, cy], pt(cx, cy, r, d0)) + L([cx, cy], pt(cx, cy, r, d1)) + arc(cx, cy, 28, d0, d1) + T(lab[0], lab[1] + 6, name, 18, TEAL) + `<circle cx="${cx.toFixed(1)}" cy="${cy.toFixed(1)}" r="3.5" fill="${NAVY}"/>`;
};
const fourAngles = () => `<svg aria-label="Four angles drawn to size: a, b, c and d" viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg" style="width:420px;max-width:100%">` +
  `<rect x="2" y="2" width="596" height="356" rx="12" fill="${WHITE}" stroke="#C9D4EC" stroke-width="2"/><line x1="300" y1="12" x2="300" y2="348" stroke="#C9D4EC" stroke-width="2"/><line x1="12" y1="180" x2="588" y2="180" stroke="#C9D4EC" stroke-width="2"/>` +
  angleIn(0, 0, 300, 180, 0, 40, 170, 'a') + angleIn(300, 0, 300, 180, 20, 135, 145, 'b') +
  angleIn(0, 180, 300, 180, 200, 275, 145, 'c') + angleIn(300, 180, 300, 180, 12, 162, 140, 'd') + '</svg>';

// Q2: a fan of 4 rays from O: OA at 0°, OB at 30°, OC at 90°, OD at 135°
const fan = () => {
  const O = [250, 222], R = 200;
  let s = `<svg aria-label="Four rays OA, OB, OC and OD from one point O. The angle between OA and OB is 30 degrees, between OB and OC is 60 degrees, between OC and OD is 45 degrees." viewBox="0 0 600 250" xmlns="http://www.w3.org/2000/svg" style="width:300px;max-width:100%">`;
  [[0, 'A'], [30, 'B'], [90, 'C'], [135, 'D']].forEach(([d, n]) => { s += L(O, pt(O[0], O[1], R, d)); const q = pt(O[0], O[1], R + 18, d); s += T(q[0], q[1] + 6, n, 18); });
  s += arc(O[0], O[1], 120, 0, 30) + arc(O[0], O[1], 60, 30, 90) + arc(O[0], O[1], 90, 90, 135);
  let q = pt(O[0], O[1], 145, 15); s += T(q[0], q[1] + 6, '30°', 16, TEAL);
  q = pt(O[0], O[1], 82, 60); s += T(q[0], q[1] + 6, '60°', 16, TEAL);
  q = pt(O[0], O[1], 115, 112.5); s += T(q[0], q[1] + 6, '45°', 16, TEAL);
  return s + `<circle cx="${O[0]}" cy="${O[1]}" r="4" fill="${NAVY}"/>` + T(O[0] - 4, O[1] + 24, 'O', 18) + '</svg>';
};

// Q4: 8-point compass
const compass = () => {
  const c = [80, 80];
  let s = `<svg aria-label="An 8-point compass: N, NE, E, SE, S, SW, W, NW" viewBox="0 0 160 160" xmlns="http://www.w3.org/2000/svg" style="width:84px;max-width:100%">`;
  ['E', 'NE', 'N', 'NW', 'W', 'SW', 'S', 'SE'].forEach((n, i) => {
    const d = i * 45, main = i % 2 === 0;
    s += L(c, pt(c[0], c[1], main ? 52 : 40, d), main ? 3 : 2);
    const q = pt(c[0], c[1], main ? 66 : 62, d); s += T(q[0], q[1] + 5, n, main ? 15 : 13, main ? NAVY : TEAL);
  });
  return s + `<circle cx="80" cy="80" r="5" fill="${YEL}" stroke="${NAVY}" stroke-width="2"/></svg>`;
};

// Q5: (a) rectangle with a line from a corner, (b) square corner cut into 3 angles, (c) two squares sharing a corner
const corners = () => {
  let s = `<svg aria-label="Three drawings. (a) A rectangle with a line from its top left corner; the angle between the left side and the line is 58 degrees and angle a is between the line and the top side. (b) A square with two lines from its bottom left corner making three angles: 15 degrees, angle b and 48 degrees. (c) Two squares share a corner and overlap by 30 degrees; angle c is the big angle between their outer sides." viewBox="0 0 600 205" xmlns="http://www.w3.org/2000/svg" style="width:400px;max-width:100%">`;
  // (a) rectangle 150 x 100, top-left corner A
  const A = [20, 50];
  s += `<rect x="20" y="50" width="150" height="100" fill="${SKY}" stroke="${NAVY}" stroke-width="3"/>`;
  const e = [170, 50 + 150 * Math.tan(rad(32))];
  s += L(A, e) + arc(A[0], A[1], 30, -32, 0) + arc(A[0], A[1], 22, -90, -32);
  let q = pt(A[0], A[1], 48, -16); s += T(q[0], q[1] + 6, 'a', 16, TEAL);
  q = pt(A[0], A[1], 40, -61); s += T(q[0], q[1] + 6, '58°', 14, TEAL);
  s += T(95, 190, '(a) rectangle', 15, TEAL);
  // (b) square 140, bottom-left corner B
  const B = [205, 170];
  s += `<rect x="205" y="30" width="140" height="140" fill="${SKY}" stroke="${NAVY}" stroke-width="3"/>`;
  s += L(B, [345, 170 - 140 * Math.tan(rad(15))]) + L(B, [345, 170 - 140 * Math.tan(rad(42))]);
  s += arc(B[0], B[1], 70, 0, 15) + arc(B[0], B[1], 44, 15, 42) + arc(B[0], B[1], 30, 42, 90);
  q = pt(B[0], B[1], 92, 7.5); s += T(q[0], q[1] + 6, '15°', 14, TEAL);
  q = pt(B[0], B[1], 62, 28.5); s += T(q[0], q[1] + 6, 'b', 16, TEAL);
  q = pt(B[0], B[1], 52, 66); s += T(q[0], q[1] + 6, '48°', 14, TEAL);
  s += T(275, 196, '(b) square', 15, TEAL);
  // (c) two squares of side 100 sharing corner O: one with sides at 0° and 90°, one with sides at 60° and 150°
  const O = [470, 165], S = 100;
  const sqp = d0 => [O, pt(O[0], O[1], S, d0), pt(O[0], O[1], S * Math.SQRT2, d0 + 45), pt(O[0], O[1], S, d0 + 90)].map(p => p.map(v => v.toFixed(1)).join(',')).join(' ');
  s += `<polygon points="${sqp(0)}" fill="${SKY}" stroke="${NAVY}" stroke-width="3" opacity="0.9"/><polygon points="${sqp(60)}" fill="${YEL}" fill-opacity="0.45" stroke="${NAVY}" stroke-width="3"/>`;
  s += arc(O[0], O[1], 40, 60, 90, RED) + arc(O[0], O[1], 22, 0, 150);
  q = pt(O[0], O[1], 56, 75); s += T(q[0], q[1] + 5, '30°', 14, RED);
  q = pt(O[0], O[1], 30, 120); s += T(q[0] - 2, q[1] + 6, 'c', 16, TEAL);
  s += T(470, 196, '(c) two squares', 15, TEAL);
  return s + '</svg>';
};

module.exports = {
  lesson: {
    n: 6, week: 3, session: 'B', title: 'Angle Turns', topic: 'Angles',
    objective: 'Estimate and measure angles with a protractor, find every angle in a fan of rays, work out angles between clock hands (30° for each number) and turns of the minute hand (6° a minute), turn on the 8-point compass (45° steps) and work backwards from a turn, and find unknown angles in squares and rectangles.',
    skills: 'Estimating with 90° and 180°, measuring, systematic counting, adding and subtracting angles, working backwards, explaining with turns',
    materials: 'A protractor and a ruler for each child, a paper clock with a split pin (or a real clock), a square of paper for checking right angles, mini whiteboards, a compass card on the floor or wall.',
    online: 'Children use their own protractor and a paper clock at home. The 8-point compass is shown on the slides; children stand and turn on camera, with the screen as North.',
    warmup: 'Robot turns: everyone stands facing the front (North). The tutor calls turns (quarter turn clockwise, half turn, 45° anticlockwise) and children turn, then name the direction they face.',
    explore: 'Pairs set a paper clock to every o’clock time and look at the angle between the hands. Which times make a right angle (check with a paper corner)? Which make a straight line? What is the angle at 1 o’clock?',
    mini: 'Measure: centre on the vertex, baseline on one arm, count up from the 0 on that arm; estimate first so you choose the right scale. A full turn is 360°: 12 clock spaces of 30°, 8 compass steps of 45°. Angles side by side add up; a 90° corner minus the parts you know gives the missing part.',
    share: 'Is turning 270° clockwise the same as turning 90° anticlockwise? How do you know?',
    exit: { q: 'Face N. Turn 135° clockwise. Which way do you face? What is the angle between the clock hands at 5 o’clock?', a: 'SE. 150° (5 spaces of 30°).' },
    mistakes: ['Reading the wrong protractor scale (writing 140° for a 40° angle) instead of starting from the 0 on the arm and checking with an estimate.', 'Counting the numbers on the clock instead of the spaces between them, or measuring the bigger way round (210° instead of 150° at 7 o’clock).', 'Compass turns: mixing up clockwise and anticlockwise, or counting the starting direction as the first 45° step.'],
    extension: 'Find all the o’clock times when the angle between the hands is more than 90° (the smaller angle). (4, 5, 6, 7 and 8 o’clock.) Then: at 6:30 the hands are not on top of each other. Why not?',
    key: [
      ['Q1', 'a 40°,  b 115°,  c 75°,  d 150° (allow 2° either way; estimates within about 20° are good).  b and d are bigger than a right angle.'],
      ['Q2', '(a) 6 angles  (b) ∠AOB 30°, ∠BOC 60°, ∠COD 45°, ∠AOC 90°, ∠BOD 105°, ∠AOD 135°  (c) ∠AOC'],
      ['Q3', '(a) 120°  (b) 150°  (c) 1 o’clock and 11 o’clock  (d) 150° (25 minutes × 6°)'],
      ['Q4', '(a) N  (b) E  (c) 135° clockwise  (d) NE'],
      ['Q5', '(a) ∠a = 32° (90° − 58°)  (b) ∠b = 27° (90° − 15° − 48°)  (c) ∠c = 150° (90° + 90° − 30°)'],
      ['Q6', '(a) SW (N → E → NE → SW)  (b) Two ways: 45° clockwise and 135° anticlockwise; or 90° clockwise and 180°.']
    ]
  },

  script: {
    hook: ['Good morning, inquirers! Today everything turns: you, the hands of a clock, and a robot. An angle tells us how much something has turned.', 'Remember: notice it, test it with a protractor or a paper clock, explain why.'],
    warmIntro: ['Everybody stand up and face the front. The front is North. Ready? Quarter turn clockwise! Which way are you facing now?', 'Back to North. Half turn! Now 45 degrees anticlockwise: just half of a quarter turn. Where are you facing?'],
    predict: ['On a clock, which o’clock times do you think make a right angle between the hands? Write down your guess before you try.'],
    exploreHints: ['Stuck: put the minute hand on 12. Move only the hour hand, one number at a time.', 'Not sure if it is a right angle: hold the corner of a square of paper between the hands.', 'Finished early: what is the angle at 1 o’clock? How can you work it out without a protractor?'],
    think: ['“I estimate first. This angle is a bit smaller than a right angle, so about 60 or 70 degrees. I put the centre of the protractor on the vertex and the baseline along one arm. That arm points to 0 on the inside scale, so I count up the inside scale: 10, 20 … 65. Not 115: my estimate says it is smaller than 90.”', '“A clock face is a full turn, 360 degrees, cut into 12 equal spaces. 360 divided by 12 is 30. At 2 o’clock the hands are 2 spaces apart: 60 degrees. At 10 o’clock I go the shorter way: also 2 spaces, 60 degrees.”', '“I face North-West. I turn 135 degrees clockwise. Each step on the compass is 45 degrees, so 135 is 3 steps: North, North-East, East. I face East.”'],
    circulate: ['Ask: “Is this angle bigger or smaller than a right angle? So which number on the protractor makes sense?”', 'Ask: “How many spaces apart are the hands? How many degrees is one space?”', 'Ask: “How many 45° steps is that turn? Which way: clockwise or anticlockwise?”'],
    hints: ['Hint 1: “Estimate first: compare with the corner of a page (90°).”', 'Hint 2: “Draw the clock or the compass and count the spaces or steps with your pencil.”', 'Hint 3: “For a corner of a square or rectangle: the parts add up to 90°. Take away the parts you know.”'],
    talk: ['“Is turning 270° clockwise the same as turning 90° anticlockwise? Test it: stand up and do both.”', '“Ben says the angle at 3 o’clock is smaller than at 9 o’clock because 3 is smaller than 9. Who agrees?”'],
    talkAns: 'Yes: 270° clockwise and 90° anticlockwise make a full turn (360°) together, so you end up facing the same way. Ben is wrong: at 3 o’clock and at 9 o’clock the hands are 3 spaces apart the shorter way, so both angles are 90°.',
    close: ['“Today you estimated before you measured, counted spaces on a clock and steps on a compass, and found every angle in a fan. Inquirers check with an estimate. Well done!”']
  },

  deck: {
    today: 'Estimate and measure angles, find every angle in a fan, work out clock angles, turn on the 8-point compass and find missing angles in squares and rectangles.',
    warmGame: 'Robot turns. Stand and face the front (North). The tutor calls a turn; everyone turns and names the direction they now face.',
    warmQs: [['How many degrees in a right angle?', '90°'], ['How many degrees in a half turn?', '180°'], ['How many right angles make a full turn?', '4'], ['Face N. Quarter turn anticlockwise. Which way now?', 'W'], ['Which is bigger: a 3/4 turn or 250°?', 'A 3/4 turn (270°)']],
    expSetup: ['Take a paper clock with two hands.', 'Set it to each o’clock time: 1 o’clock, 2 o’clock … 12 o’clock.', 'Which times make a right angle between the hands? Check with a paper corner.', 'Which time makes a straight line? What is the angle at 1 o’clock?'],
    expPic: 'a clock face showing 3 o’clock with a small square marking the right angle between the hands, and the question “Which other times make a right angle?”',
    expAsk: [['Which o’clock times make a right angle?', '3 o’clock and 9 o’clock.'], ['Which time makes a straight line?', '6 o’clock (180°, a half turn).'], ['What is the angle at 1 o’clock? How do you know?', '30°: a full turn is 360° and the clock has 12 equal spaces, 360 ÷ 12 = 30.']],
    mini1: { head: 'Measure with a protractor', body: ['Estimate: the angle is smaller than a right angle.', 'Centre on the vertex, baseline along one arm.', 'Count up from the 0 on that arm: which number?'], ans: '65° (not 115°: the estimate says less than 90°).' },
    mini2: { head: 'Compass turns: 45° steps', body: ['Face NW. Turn 135° clockwise.', '135° = 3 steps of 45°.', 'Count 3 steps clockwise: N, NE, …'], ans: 'E.' },
    keyHead: 'Key idea: count the turn',
    keyBig: 'A full turn is 360°: 4 right angles, 8 compass steps of 45°, 12 clock spaces of 30°. Estimate first, then measure.',
    keySmall: 'Angles side by side add up. The corner of a square or rectangle is 90°.',
    brk: 'Compass dance. Stand facing North. Jump a quarter turn clockwise on each clap: N, E, S, W, N. Then half turns, then 45° steps saying each direction.',
    ws1: 'Page 1, in pairs: Q1 estimate then measure four angles, Q2 every angle in the fan.',
    ws2: 'Page 2, on your own: Q3 clock angles, Q4 compass turns, Q5 corners of squares and rectangles, Q6 the robot.'
  },

  qbank: {
    core: [
      { q: 'How many degrees are there in a half turn?', a: '180°' },
      { q: 'How many degrees are there in 3/4 of a turn?', a: '270°' },
      { q: 'Ali faces E. He turns 90° clockwise. Which direction does he face now?', a: 'S' },
      { q: 'Mei faces N. She turns 135° anticlockwise. Which direction does she face now?', a: 'SW' },
      { q: 'What is the angle between the hands of a clock at 6 o’clock?', a: '180°' },
      { q: 'A line from a corner of a rectangle cuts the 90° corner into two angles. One angle is 64°. What is the other?', a: '26°' }
    ],
    stretch: [
      { q: 'Siti faces SE. She turns 225° clockwise. Which direction does she face now?', a: 'N (225° is 5 steps of 45°: S, SW, W, NW, N)' },
      { q: 'What is the angle between the clock hands at 10 o’clock? At 2 o’clock? What do you notice?', a: '60° and 60°. Both are 2 spaces apart the shorter way.' },
      { q: 'How many degrees does the minute hand turn from 7:15 to 7:50?', a: '210° (35 minutes × 6°)' },
      { q: 'The corner of a square is cut into two angles. One angle is 4 times as big as the other. Find both angles.', a: '18° and 72° (5 equal parts make 90°, so one part is 18°)' },
      { q: 'Mei faces W. She turns clockwise until she faces SE. How many degrees does she turn?', a: '225° (W → NW → N → NE → E → SE: 5 steps of 45°)' },
      { q: 'Four rays come out of one point, making 3 angles side by side: 25°, 40° and 25°. How many angles are there altogether? What is the biggest?', a: '6 angles (25°, 40°, 25°, 65°, 65°, 90°); the biggest is 90°.' },
      { q: 'Ravi faces N and turns anticlockwise to face S. Then he turns anticlockwise again to face E. How many degrees has he turned altogether?', a: '270° (180° + 90°)' },
      { q: 'In a rectangle, a line from one corner makes a 27° angle with the long side. What angle does it make with the short side?', a: '63° (90° − 27°)' }
    ],
    challenge: [
      { q: 'What is the angle between the hands of a clock at 3:30?', a: '75° (the minute hand points to 6; the hour hand is halfway from 3 to 4, so it is 2 and a half spaces from the 6: 30° + 30° + 15°)' },
      { q: 'Five rays come out of one point and make 4 equal angles side by side. The angle between the two outside rays is 120°. How many angles can you find altogether? How many of them are right angles?', a: '10 angles (4 + 3 + 2 + 1). Each small angle is 30°, so the right angles are the 3-part angles: 2 of them.' },
      { q: 'A robot faces N. It turns 45° clockwise, again and again. After how many turns does it first face N again? Which way does it face after 30 turns?', a: '8 turns. After 30 turns it faces W (30 = 3 × 8 + 6, and 6 steps from N is W).' },
      { q: 'The minute hand turns 90°. How many minutes have passed? The hour hand turns 90°. How many hours have passed?', a: '15 minutes; 3 hours' },
      { q: 'How many degrees does the hour hand turn in 20 minutes?', a: '10° (it turns 30° in 60 minutes)' },
      { q: 'Mei faces S and turns clockwise to face NE. Ali faces S and turns anticlockwise to face NE. How many more degrees did Mei turn than Ali?', a: '90° (Mei 225°, Ali 135°)' },
      { q: 'What is the angle between the hands of a clock at 9:30?', a: '105° (the hour hand is halfway between 9 and 10; from it to the 6 is 3 and a half spaces: 3 × 30° + 15°)' },
      { q: 'The corner of a square is cut into 3 angles. The middle angle is twice the smallest. The biggest is 3 times the smallest. Find all three angles.', a: '15°, 30° and 45° (6 equal parts make 90°, so one part is 15°)' },
      { q: 'Two squares share one corner and overlap. The angle between their outside sides is 160°. What is the angle where they overlap?', a: '20° (90° + 90° = 180°, and 180° − 160° = 20°)' }
    ]
  },

  workbook: H => [
    H.q(1, 'Estimate each angle first. Then measure it with your protractor.', { before: 40, keepNext: true }),
    H.fig(fourAngles()),
    H.tbl([2400, 1875, 1875, 1875, 1875], [
      H.row(['Angle', 'a', 'b', 'c', 'd'].map((s, i) => H.cell(s, i ? 1875 : 2400, { bold: true, fill: 'EDEDED' }))),
      H.row([H.cell('My estimate', 2400, { bold: true, h: 90 }), ...[0, 1, 2, 3].map(() => H.cell('', 1875))]),
      H.row([H.cell('I measured', 2400, { bold: true, h: 90 }), ...[0, 1, 2, 3].map(() => H.cell('', 1875))])
    ]),
    H.gap(20),
    H.q(2, 'Four rays OA, OB, OC and OD come out of point O. ∠AOB means the angle at O between OA and OB.', { keepNext: true }),
    H.fig(fan()),
    H.sub('a', 'How many angles can you find altogether?   ________'),
    H.sub('b', 'Name every angle and find its size. Work in order so you do not miss one.'),
    ...H.lines(1),
    H.sub('c', 'Which angle is a right angle?   ________'),

    H.q(3, 'Clock angles. A full turn is 360° and a clock face has 12 equal spaces. Find the smaller angle between the hands.', { pb: true, before: 0, keepNext: true }),
    H.sub('a', 'At 4 o’clock:  ________          (b)  At 7 o’clock:  ________'),
    H.sub('c', 'Find both o’clock times when the angle is 30°.   ______________'),
    H.sub('d', 'How many degrees does the minute hand turn from 3:10 to 3:35?   ________'),
    H.q(4, 'Compass turns. One step from a direction to the next one is 45°.', { keepNext: true }),
    H.fig(compass()),
    H.sub('a', 'Ali faces W and turns 90° clockwise. Now he faces:   ______'),
    H.sub('b', 'Mei faces SW and turns 135° anticlockwise. Now she faces:   ______'),
    H.sub('c', 'Siti faces NE and wants to face S. Her smallest turn is:  ____________'),
    H.sub('d', 'Ravi turns 90° anticlockwise and ends up facing NW. At first he faced:   ______'),
    H.q(5, 'The corners of squares and rectangles are 90°. Find the angles marked a, b and c.', { keepNext: true }),
    H.fig(corners()),
    H.sub('', '∠a = ________          ∠b = ________          ∠c = ________'),
    H.q(6, 'A robot starts facing N.', { keepNext: true }),
    H.sub('a', 'It turns 90° clockwise, then 45° anticlockwise, then 180°. Now it faces:  ______'),
    H.sub('b', 'Ben wants it to turn from N to W using two DIFFERENT cards from:  45° clockwise,  90° clockwise,  135° anticlockwise,  180°.  Find ALL the pairs that work.'),
    ...H.lines(1)
  ]
};
