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
  return L([cx, cy], pt(cx, cy, r, d0)) + L([cx, cy], pt(cx, cy, r, d1)) + arc(cx, cy, 28, d0, d1) + T(lab[0], lab[1] + 7, name, 22, TEAL) + `<circle cx="${cx.toFixed(1)}" cy="${cy.toFixed(1)}" r="3.5" fill="${NAVY}"/>`;
};
const fourAngles = () => `<svg aria-label="Four angles drawn to size: a, b, c and d" viewBox="0 0 600 360" xmlns="http://www.w3.org/2000/svg" style="width:340px;max-width:100%">` +
  `<rect x="2" y="2" width="596" height="356" rx="12" fill="${WHITE}" stroke="#C9D4EC" stroke-width="2"/><line x1="300" y1="12" x2="300" y2="348" stroke="#C9D4EC" stroke-width="2"/><line x1="12" y1="180" x2="588" y2="180" stroke="#C9D4EC" stroke-width="2"/>` +
  angleIn(0, 0, 300, 180, 0, 40, 170, 'a') + angleIn(300, 0, 300, 180, 20, 135, 145, 'b') +
  angleIn(0, 180, 300, 180, 200, 275, 145, 'c') + angleIn(300, 180, 300, 180, 12, 162, 140, 'd') + '</svg>';

// Q2: a fan of 4 rays from O: OA at 0°, OB at 30°, OC at 90°, OD at 135°
const fan = () => {
  const O = [250, 228], R = 188;
  let s = `<svg aria-label="Four rays OA, OB, OC and OD from one point O. The angle between OA and OB is 30 degrees, between OB and OC is 60 degrees, between OC and OD is 45 degrees." viewBox="0 0 600 262" xmlns="http://www.w3.org/2000/svg" style="width:270px;max-width:100%">`;
  [[0, 'A'], [30, 'B'], [90, 'C'], [135, 'D']].forEach(([d, n]) => { s += L(O, pt(O[0], O[1], R, d)); const q = pt(O[0], O[1], R + 18, d); s += T(q[0], q[1] + 8, n, 24); });
  s += arc(O[0], O[1], 120, 0, 30) + arc(O[0], O[1], 60, 30, 90) + arc(O[0], O[1], 90, 90, 135);
  let q = pt(O[0], O[1], 145, 15); s += T(q[0] + 8, q[1] + 7, '30°', 21, TEAL);
  q = pt(O[0], O[1], 84, 60); s += T(q[0] + 6, q[1] + 7, '60°', 21, TEAL);
  q = pt(O[0], O[1], 118, 112.5); s += T(q[0], q[1] + 7, '45°', 21, TEAL);
  return s + `<circle cx="${O[0]}" cy="${O[1]}" r="4" fill="${NAVY}"/>` + T(O[0] - 4, O[1] + 26, 'O', 22) + '</svg>';
};

// Q4: 8-point compass
const compass = () => {
  const c = [100, 100];
  let s = `<svg aria-label="An 8-point compass: N, NE, E, SE, S, SW, W, NW" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg" style="width:104px;max-width:100%">`;
  ['E', 'NE', 'N', 'NW', 'W', 'SW', 'S', 'SE'].forEach((n, i) => {
    const d = i * 45, main = i % 2 === 0;
    s += L(c, pt(c[0], c[1], main ? 62 : 46, d), main ? 4 : 3);
    const q = pt(c[0], c[1], main ? 80 : 74, d); s += T(q[0], q[1] + 8, n, main ? 26 : 22, main ? NAVY : TEAL);
  });
  return s + `<circle cx="100" cy="100" r="7" fill="${YEL}" stroke="${NAVY}" stroke-width="2.5"/></svg>`;
};

// Q5: (a) rectangle with a line from a corner, (b) square corner cut into 3 angles
const corners = () => {
  let s = `<svg aria-label="A rectangle with a line from its top left corner; the angle between the left side and the line is 58 degrees and angle a is between the line and the top side." viewBox="0 20 190 150" xmlns="http://www.w3.org/2000/svg" style="width:190px;max-width:100%">`;
  // (a) rectangle 150 x 100, top-left corner A
  const A = [20, 50];
  s += `<rect x="20" y="50" width="150" height="100" fill="${SKY}" stroke="${NAVY}" stroke-width="3"/>`;
  const e = [170, 50 + 150 * Math.tan(rad(32))];
  s += L(A, e) + arc(A[0], A[1], 30, -32, 0) + arc(A[0], A[1], 22, -90, -32);
  let q = pt(A[0], A[1], 88, -13); s += T(q[0], q[1] + 6, 'a', 19, TEAL);
  q = pt(A[0], A[1], 64, -64); s += T(q[0] + 4, q[1] + 6, '58°', 18, TEAL);
  return s + '</svg>';
};

// Think Harder challenge 9: two squares sharing corner O. Outside sides make 160°, overlap is the unknown.
const overlapFig = () => {
  const O = [250, 150], S = 105;
  const sqp = d0 => [O, pt(O[0], O[1], S, d0), pt(O[0], O[1], S * Math.SQRT2, d0 + 45), pt(O[0], O[1], S, d0 + 90)].map(p => p.map(v => v.toFixed(1)).join(',')).join(' ');
  let s = `<svg aria-label="Two squares share the corner O and overlap. The angle between their outside sides is 160 degrees. The angle where they overlap is marked with a question mark." viewBox="0 0 500 175" xmlns="http://www.w3.org/2000/svg" style="width:380px;max-width:100%">`;
  s += `<polygon points="${sqp(0)}" fill="${SKY}" stroke="${NAVY}" stroke-width="3" opacity="0.9"/><polygon points="${sqp(70)}" fill="${YEL}" fill-opacity="0.45" stroke="${NAVY}" stroke-width="3"/>`;
  s += arc(O[0], O[1], 38, 70, 90, RED, 3) + arc(O[0], O[1], 82, 0, 160, TEAL, 3);
  s += L(pt(O[0], O[1], 38, 80), pt(O[0], O[1], 118, 80), 2, RED);
  let q = pt(O[0], O[1], 134, 80); s += T(q[0], q[1] + 8, '?', 26, RED);
  q = pt(O[0], O[1], 98, 128); s += T(q[0], q[1] + 6, '160°', 17, TEAL);
  return s + `<circle cx="${O[0]}" cy="${O[1]}" r="3.5" fill="${NAVY}"/>` + T(O[0] + 4, O[1] + 20, 'O', 18) + '</svg>';
};

module.exports = {
  lesson: {
    n: 6, week: 3, session: 'B', title: 'Angle Turns', topic: 'Angles',
    objective: 'Estimate and measure angles with a protractor, find every angle in a fan of rays, work out angles between clock hands (30° for each number), turn on the 8-point compass (45° steps), and find an unknown angle in a rectangle corner.',
    skills: 'Estimating with 90° and 180°, measuring, systematic counting, adding and subtracting angles, explaining with turns',
    materials: 'A protractor and a ruler for each child (bring from home: the kit page lists them), the paper clock from the cut-out page with a split pin (or a real clock), a square of paper for checking right angles, mini whiteboards, a compass card on the floor or wall.',
    online: 'Children use their own protractor and ruler and the paper clock cut out from the kit page. Self-view on screen may be mirrored: say turn towards your own right hand, not the screen’s left. The 8-point compass is shown on the slides; children stand and turn on camera, with the screen as North.',
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
      ['Q3', '(a) 120°  (b) 150°'],
      ['Q4', '(a) N  (b) E'],
      ['Q5', '∠a = 32° (90° − 58°)'],
      ['Q6', '(a) SW (N → E → NE → SW)']
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
    ws2: 'Page 2, on your own: Q3 clock angles, Q4 compass turns, Q5 a corner of a rectangle, Q6 the robot.'
  },

  qbank: {
    core: [
      { q: 'Stand up and face the front. Turn all the way round until you face the front again: that is a full turn, 360°. How many degrees is a half turn? How many degrees is a quarter turn?', a: '180° for a half turn and 90° for a quarter turn.' },
      { q: 'The corner of a page is a right angle, 90°. How many right angles make a full turn? How many degrees is a turn of 3 right angles (3/4 of a turn)?', a: '4 right angles make a full turn. Three right angles are 270°.' },
      { q: 'Ali faces East. He turns a quarter turn clockwise (the way the clock hands go). Which direction does he face now? Stand up and try it.', a: 'S' },
      { q: 'A compass has 8 directions: N, NE, E, SE, S, SW, W, NW. Each step to the next one is 45°. Mei faces N and turns 3 steps anticlockwise. Which direction does she face now? How many degrees did she turn?', a: 'SW. She turned 3 × 45° = 135°.' },
      { q: 'A clock has 12 equal gaps between the numbers, all the way round the 360° circle. How many degrees is one gap? What is the angle between the hands at 1 o’clock? At 6 o’clock?', a: '30° for one gap (360 ÷ 12). 30° at 1 o’clock and 180° at 6 o’clock.' },
      { q: 'The corner of a rectangle is 90°. A line from the corner cuts it into two angles. One angle is 64°. What is the other?', a: '26° (90° − 64°)' }
    ],
    stretch: [
      { q: 'Siti faces SE. She turns 225° clockwise. Which direction does she face now?', a: 'N (225° is 5 steps of 45°: S, SW, W, NW, N)' },
      { q: 'What is the angle between the clock hands at 10 o’clock? At 2 o’clock? What do you notice?', a: '60° and 60°. Both are 2 spaces apart the shorter way.' },
      { q: 'How many degrees does the minute hand turn from 7:15 to 7:50?', a: '210° (7 jumps of 5 minutes, and each jump is one clock space of 30°)' },
      { q: 'A robot starts facing N. Ben wants it to turn from N to W using two DIFFERENT cards from:  45° clockwise,  90° clockwise,  135° anticlockwise,  180°.  Find ALL the pairs that work.', a: 'Two ways: 45° clockwise and 135° anticlockwise; or 90° clockwise and 180°.' },
      { q: 'Mei faces W. She turns clockwise until she faces SE. How many degrees does she turn?', a: '225° (W → NW → N → NE → E → SE: 5 steps of 45°)' },
      { q: 'Four rays come out of one point, making 3 angles side by side: 25°, 40° and 25°. How many angles are there altogether? What is the biggest?', a: '6 angles (25°, 40°, 25°, 65°, 65°, 90°); the biggest is 90°.' },
      { q: 'Ravi faces N and turns anticlockwise to face S. Then he turns anticlockwise again to face E. How many degrees has he turned altogether?', a: '270° (180° + 90°)' },
      { q: 'The minute hand of a clock turns 150° starting at 2:10. What time is it then?', a: '2:35 (the minute hand turns 6° every minute, and 150 ÷ 6 = 25 minutes; 2:10 + 25 minutes).' },
      { q: 'The corner of a square is cut into two angles. One angle is 4 times as big as the other. Find both angles.', a: '18° and 72° (5 equal parts make 90°, so one part is 18°)' }
    ],
    challenge: [
      { q: 'What is the angle between the hands of a clock at 3:30?', a: '75° (the minute hand points to 6; the hour hand is halfway from 3 to 4, so it is 2 and a half spaces from the 6: 30° + 30° + 15°)' },
      { q: 'Five rays come out of one point and make 4 equal angles side by side. The angle between the two outside rays is 120°. How many angles can you find altogether? How many of them are right angles?', a: '10 angles (4 + 3 + 2 + 1). Each small angle is 30°, so the right angles are the 3-part angles: 2 of them.' },
      { q: 'A robot faces N. It turns 45° clockwise, again and again. After how many turns does it first face N again? Which way does it face after 30 turns?', a: '8 turns. After 30 turns it faces W (30 = 3 × 8 + 6, and 6 steps from N is W).' },
      { q: 'At 4 o’clock the angle between the clock hands is 120°. What is the angle at 4:10?', a: '65°. In 10 minutes the minute hand turns 60° and the hour hand turns 5° the same way, so the gap shrinks by 55°: 120° − 55° = 65°.' },
      { q: 'Mei says: "At 2 o’clock the angle between the clock hands is 60°, so at 10 o’clock it must be 60° too." Is she right? Explain with a drawing. Which other pairs of o’clock times have the same angle?', a: 'She is right. 10 o’clock is the mirror image of 2 o’clock across the line from 12 to 6, so the hands make the same angle. The other pairs are 1 and 11 (30°), 3 and 9 (90°), 4 and 8 (120°), 5 and 7 (150°).' },
      { q: 'Mei faces S and turns clockwise to face NE. Ali faces S and turns anticlockwise to face NE. How many more degrees did Mei turn than Ali?', a: '90° (Mei 225°, Ali 135°)' },
      { q: 'Make up your own clock-angle puzzle. Choose a time that is NOT an o’clock time (half past is easiest), work out the angle between the hands, and write your puzzle as "What is the angle at …?". Draw the clock to check your answer. Then find a second time with the same angle.', a: 'Puzzles will vary. Model: 9:30 is 105° (the hour hand is halfway between 9 and 10, 3 and a half spaces, 3 × 30° + 15°). Another time with the same angle is 2:30.' },
      { q: 'The corner of a square is cut into 3 angles. The middle angle is twice the smallest. The biggest is 3 times the smallest. Find all three angles.', a: '15°, 30° and 45° (6 equal parts make 90°, so one part is 15°)' },
      { q: 'Two squares share one corner O and overlap, like the picture. The angle covered by both squares together (from the outside side of one square to the outside side of the other) is 160°. What is the angle where the squares overlap?', a: '20° (90° + 90° = 180°, and 180° − 160° = 20°)', fig: overlapFig() }
    ]
  },

  workbook: H => [
    H.q(1, 'Estimate each angle first. Then measure it with your protractor. The arms are short: draw them longer with a ruler first. Tip: put the centre of the protractor on the corner, and count up from the 0 that lines up with one arm.', { before: 40, keepNext: true }),
    H.fig(fourAngles()),
    H.tbl([2400, 1875, 1875, 1875, 1875], [
      H.row(['Angle', 'a', 'b', 'c', 'd'].map((s, i) => H.cell(s, i ? 1875 : 2400, { bold: true, fill: 'EDEDED' }))),
      H.row([H.cell('My estimate', 2400, { bold: true, h: 56 }), ...[0, 1, 2, 3].map(() => H.cell('', 1875))]),
      H.row([H.cell('I measured', 2400, { bold: true, h: 56 }), ...[0, 1, 2, 3].map(() => H.cell('', 1875))])
    ]),
    H.gap(20),
    H.q(2, 'Four rays OA, OB, OC and OD come out of point O. ∠AOB means the angle at O between OA and OB.', { keepNext: true }),
    H.fig(fan()),
    H.sub('a', 'How many angles can you find altogether?   ________'),
    H.sub('b', 'Name every angle and find its size. Work in order so you do not miss one.'),
    ...H.lines(1),
    H.sub('c', 'Which angle is a right angle?   ________'),

    H.q(3, 'Clock angles. A clock face has 12 equal spaces in 360°. Find the smaller angle.', { pb: true, before: 0, keepNext: true }),
    H.sub('a', ['At 4 o’clock:  ________          <b style="color:#1F7A6F">b</b>  At 7 o’clock:  ________']),
    H.q(4, 'Compass turns. One step from a direction to the next one is 45°.', { keepNext: true }),
    H.fig(compass()),
    H.sub('a', 'Ali faces W and turns 90° clockwise. Now he faces:   ______'),
    H.sub('b', 'Mei faces SW and turns 135° anticlockwise. Now she faces:   ______'),
    H.q(5, 'The corner of a rectangle is 90°. Find the angle marked a.', { keepNext: true }),
    H.fig(corners()),
    H.sub('', '∠a = ________'),
    H.q(6, 'A robot starts facing N.', { keepNext: true }),
    H.sub('', 'It turns 90° clockwise, then 45° anticlockwise, then 180°. Now it faces:  ______')
  ]
};

// ---- close_gaps + fix pass: sneak-peek puzzles, Investigation (with an easy first step), Looking back, Go further (docs/audit/close_gaps_p4.md, fixpass_p4.md)
module.exports.gaps = {
 "idea": "angles and turns",
 "check": [
  {
   "q": "Stand up and face the screen. Turn a quarter turn to your right. Then turn another quarter turn the same way. How many quarter turns did you make? Which way are you facing now, compared with the start?",
   "a": "2 quarter turns, which is a half turn. You are facing the opposite way (your back is to the screen).",
   "s": "2 quarter turns: you face the opposite way.",
   "kind": "access"
  },
  {
   "q": "A square corner is cut into two angles. One angle is 35°. What is the other angle? How do you know?",
   "a": "55°. A square corner is 90°, and 90° − 35° = 55°.",
   "s": "55° (90° − 35°).",
   "kind": "think"
  }
 ],
 "why": "A square corner is 90° and a half turn is 180°. Angles side by side add up to the whole turn.",
 "invest": {
  "kind": "Find all the ways.",
  "head": "Splitting a corner",
  "intro": "A square corner is 90°. Mei cuts it into three angles. Every angle is a whole multiple of 10°: 10°, 20°, 30° and so on. One way is 10°, 20° and 60°. (30°, 50°, 10° and 10°, 30°, 50° count as the same set.)",
  "parts": [
   "Find as many different sets of three angles as you can.",
   "How do you know you have found them all? Write how you checked.",
   "What if the corner is a straight line (180°) cut into three angles that are multiples of 30°? Find all the sets. What stays the same?"
  ],
  "lines": 5,
  "key": "(a) Seven sets: 10, 10, 70; 10, 20, 60; 10, 30, 50; 10, 40, 40; 20, 20, 50; 20, 30, 40; 30, 30, 30 (checked by brute force). (b) A good method: fix the smallest angle, then list the other two in order. Counting in units of 10° helps: three whole numbers that add up to 9. (c) Three sets: 30, 30, 120; 30, 60, 90; 60, 60, 60. What stays the same: the three angles always add up to the whole turn (90° or 180°). Low floor: any three angles that add to 90°. Look for children who realise a list needs a system.",
  "easy": "A square corner is 90°. Draw it and split it into three EQUAL angles. How big is each one?"
 },
 "reflect": "Something I did well: I estimated each angle before I measured. The hardest part was reading the protractor scale. What helped me: starting from the 0 that lines up with one arm.",
 "go2": {
  "q": "What if the clock shows half past three (3:30)? Is the angle still 90°? Why not?",
  "a": "No. It is 75°: at 3:30 the hour hand has moved halfway from 3 to 4, which is 15° past the 3. The minute hand points at 6 (180°) and the hour hand at 105°."
 },
 "chooseAfter": 2,
 "cap": "Page 2 is on your own. Aim for Q3 and Q4 first. Q5 and Q6 are choices for the last few minutes."
};
