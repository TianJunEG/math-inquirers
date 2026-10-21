// Math Inquirers P6 — Lesson 7: Turtle Geometry (angles in polygons; pen drawing with turns)
// Every answer below was worked out and checked: turn = 360 ÷ sides, inside = 180 − turn,
// star turn = 360 × times round ÷ points, angle sum = (sides − 2) × 180. The Python program was run.

const NAVY = '#1B2A49', YEL = '#FFC93C', SKY = '#DDEBF7', TEAL = '#1F7A6F', RED = '#D64545', WHITE = '#FFFFFF';
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

// ---------- code blocks: our own simple coloured shapes (never Scratch artwork) ----------
// prog: [kind, text] or [kind, text, [children]] for a C-shaped block; {…} marks a white slot.
const BC = { event: [YEL, NAVY], ctrl: [WHITE, NAVY], motion: [SKY, NAVY], pen: [TEAL, WHITE], var: [RED, WHITE], looks: [YEL, NAVY] };
const cwid = (s, fs) => [...s].reduce((a, c) => a + fs * (/[iltfjr .,:()'|]/.test(c) ? 0.32 : /[A-Zmw%×]/.test(c) ? 0.76 : 0.58), 0);
const segs = t => t.split(/(\{[^}]*\})/).filter(s => s.trim()).map(s => s[0] === '{' ? { t: s.slice(1, -1), slot: true } : { t: s.trim(), slot: false });
function blocks(prog, o = {}) {
  const fs = o.fs || 15, h = o.h || 30, pad = 9, arm = 16, gap = 6, sp = 8;
  const lineW = t => segs(t).reduce((a, g) => a + cwid(g.t, fs) + (g.slot ? 2 * sp : 0) + gap, 0) - gap + 2 * pad;
  const ty = y => (y + h / 2 + fs * 0.36).toFixed(1);
  const txt = (x, y, t, fg) => {
    let s = '', cx = x + pad;
    for (const g of segs(t)) {
      const w = cwid(g.t, fs);
      if (g.slot) {
        s += `<rect x="${cx.toFixed(1)}" y="${y + 5}" width="${(w + 2 * sp).toFixed(1)}" height="${h - 10}" rx="${(h - 10) / 2}" fill="${WHITE}" stroke="${NAVY}" stroke-width="1.5"/>`;
        s += `<text x="${(cx + sp + w / 2).toFixed(1)}" y="${ty(y)}" font-size="${fs}" font-weight="700" text-anchor="middle" fill="${NAVY}" font-family="Arial">${esc(g.t)}</text>`;
        cx += w + 2 * sp + gap;
      } else {
        s += `<text x="${cx.toFixed(1)}" y="${ty(y)}" font-size="${fs}" font-weight="700" fill="${fg}" font-family="Arial">${esc(g.t)}</text>`;
        cx += w + gap;
      }
    }
    return s;
  };
  let maxX = 0;
  const draw = (items, x, y) => {
    let s = '';
    for (const [kind, t, kids] of items) {
      const [bg, fg] = BC[kind];
      if (kids) {
        const w = Math.max(lineW(t), 110), r = draw(kids, x + arm, y + h + 2);
        const yb = Math.max(r.y, y + h + 16), wb = Math.max(w * 0.45, 70);
        s += `<path d="M${x} ${y} H${(x + w).toFixed(1)} V${y + h} H${x + arm} V${yb} H${(x + wb).toFixed(1)} V${yb + 14} H${x} Z" fill="${bg}" stroke="${NAVY}" stroke-width="2" stroke-linejoin="round"/>` + txt(x, y, t, fg) + r.s;
        maxX = Math.max(maxX, x + w, r.maxX || 0); y = yb + 16;
      } else {
        const w = lineW(t);
        s += `<rect x="${x}" y="${y}" width="${w.toFixed(1)}" height="${h}" rx="${kind === 'event' ? 14 : 7}" fill="${bg}" stroke="${NAVY}" stroke-width="2"/>` + txt(x, y, t, fg);
        maxX = Math.max(maxX, x + w); y += h + 2;
      }
    }
    return { s, y, maxX };
  };
  const r = draw(prog, 2, 2);
  return { svg: r.s, w: Math.ceil(maxX + 4), h: Math.ceil(r.y + 2) };
}

// a corner of a shape: the turtle walks along AB, turns at B, walks along BC (turn 70°, inside 110°)
const cornerFig = () => {
  const t = 70, B = [330, 70], L = 170, r = Math.PI / 180;
  const A = [B[0] - L, B[1]], C = [B[0] + 150 * Math.cos(t * r), B[1] + 150 * Math.sin(t * r)];
  const arc = (rad, a1, a2, col) => `<path d="M${(B[0] + rad * Math.cos(a1 * r)).toFixed(1)} ${(B[1] + rad * Math.sin(a1 * r)).toFixed(1)} A${rad} ${rad} 0 0 1 ${(B[0] + rad * Math.cos(a2 * r)).toFixed(1)} ${(B[1] + rad * Math.sin(a2 * r)).toFixed(1)}" fill="none" stroke="${col}" stroke-width="4"/>`;
  const lab = (rad, a, s, col) => `<text x="${(B[0] + rad * Math.cos(a * r)).toFixed(1)}" y="${(B[1] + rad * Math.sin(a * r) + 6).toFixed(1)}" font-size="16" font-weight="700" text-anchor="middle" fill="${col}" font-family="Arial">${s}</text>`;
  let s = `<svg aria-label="A corner of a shape. The turtle walks along one side, then turns 70 degrees from straight on. The inside angle is 110 degrees. 70 + 110 = 180." viewBox="0 0 600 230" xmlns="http://www.w3.org/2000/svg" style="width:520px;max-width:100%">`;
  s += `<line x1="${B[0]}" y1="${B[1]}" x2="${B[0] + 150}" y2="${B[1]}" stroke="${NAVY}" stroke-width="3" stroke-dasharray="8 6"/>`;
  s += `<polyline points="${A.join(',')} ${B.join(',')} ${C.map(v => v.toFixed(1)).join(',')}" fill="none" stroke="${NAVY}" stroke-width="5" stroke-linejoin="round"/>`;
  s += `<polygon points="${A[0] + 70},${B[1] - 9} ${A[0] + 92},${B[1]} ${A[0] + 70},${B[1] + 9}" fill="${TEAL}"/>`;
  s += arc(52, 0, t, RED) + arc(34, t, 180, TEAL);
  s += lab(90, t / 2, 'turn 70°', RED) + lab(62, (t + 180) / 2 + 12, 'inside 110°', TEAL);
  s += `<text x="${B[0] + 160}" y="${B[1] + 6}" font-size="15" fill="${NAVY}" font-family="Arial">straight on</text>`;
  s += `<text x="20" y="200" font-size="16" font-weight="700" fill="${NAVY}" font-family="Arial">turn + inside angle = 180°</text>`;
  s += `<text x="20" y="222" font-size="15" fill="${NAVY}" font-family="Arial">(they sit on one straight line)</text>`;
  return s + '</svg>';
};

// blocks on the left, an empty drawing frame on the right
const codeAndFrame = (prog, label, frameText) => {
  const b = blocks(prog), W = 600, fx = b.w + 30, H = Math.max(b.h, 190);
  let s = `<svg aria-label="${esc(label)}" viewBox="0 0 ${W} ${H + 4}" xmlns="http://www.w3.org/2000/svg" style="width:580px;max-width:100%">` + b.svg;
  if (frameText) s += `<rect x="${fx}" y="2" width="${W - fx - 4}" height="${H}" rx="12" fill="${WHITE}" stroke="${NAVY}" stroke-width="2" stroke-dasharray="7 5"/><text x="${fx + 12}" y="24" font-size="14" fill="${NAVY}" font-family="Arial">${esc(frameText)}</text>`;
  return s + '</svg>';
};

const PY = `import turtle
t = turtle.Turtle()
n = 5          # number of points (or sides)
k = 2          # times round: 1 for a polygon
turn = 360 * k / n
total = 0
for i in range(n):
    t.forward(150)
    t.right(turn)
    total = total + turn
print("turn", turn, "total", total, "angle", 180 - turn)
turtle.done()`;
// output when run: turn 144.0 total 720.0 angle 36.0

const pyBox = H => H.tbl([9900], [H.row([H.cell(
  `<div style="text-align:left"><div style="font-weight:700;margin-bottom:4px">Python version (optional): the same turtle in Python. Change n and k to test your answers to Q1 and Q5.</div><div style="font-family:'Liberation Mono',Consolas,monospace;font-size:13.5px;line-height:1.35;white-space:pre">${esc(PY)}</div></div>`,
  9900, { fill: 'DDEBF7', h: 60 })])]);

module.exports = {
  lesson: {
    n: 7, week: 4, session: 'A', title: 'Turtle Geometry', topic: 'Angles in Polygons',
    objective: 'Use the idea that a turtle going once round a closed shape turns 360° altogether to find the turn angle (360° ÷ sides) and inside angle (180° − turn) of regular polygons, work backwards from an angle to the number of sides, extend to star polygons (turn = 360° × times round ÷ points), and test every prediction with a pen program in Scratch (or Python turtle).',
    skills: 'Turn (exterior) and inside (interior) angles, angles on a straight line, angle sum of a polygon, star polygons, predicting and tracing code, repeat loops and variables',
    materials: 'A laptop or desktop with Scratch 3 open (scratch.mit.edu) and the Pen extension added, mini whiteboards, a protractor, plain or squared paper.',
    online: 'Pairs work in breakout rooms: one child drives Scratch and shares the screen, the other predicts, then they swap. Children hold drawings up to the camera. A tablet works for Scratch but is slower.',
    warmup: 'Turtle says: everyone stands and faces the screen (call it north). The tutor calls turns (right 90, right 180, left 270, right 45, right 360) and children turn their bodies, then say which way they face. Finish with: one full turn made of 3 equal turns. How big is each turn?',
    explore: 'At the computer in pairs: build the square program (pen down, repeat 4: move 100, turn right 90). Change it to draw an equilateral triangle, then a regular pentagon and a regular hexagon, predicting each turn before running it. Record the sides, the turn and whether the shape closes. What do sides × turn always make?',
    mini: 'The turtle turns the outside angle: turn + inside angle = 180°. Going round once, the turns add up to 360°, so a regular polygon with n sides turns 360° ÷ n (octagon: turn 45°, inside 135°). Work backwards from an inside angle (174° → turn 6° → 60 sides; 115° is impossible because 360 ÷ 65 is not whole). A star goes round more than once: the 5-point star turns 720° ÷ 5 = 144°. Before page 2: trace a running total in a table, plan an 8-point star that goes round 3 times, and add up the inside angles of an octagon (1080°).',
    share: 'Ali says the turtle turns by the inside angle of the shape. Mei says it turns by the outside angle. Who is right? Use a triangle to explain.',
    exit: { q: 'A turtle draws a regular polygon and turns 5° at every corner. How many sides does the polygon have? What is each inside angle?', a: '72 sides (360 ÷ 5 = 72); each inside angle is 175° (180 − 5)' },
    mistakes: ['Using the inside angle as the turn: turn 60° for a triangle draws half a hexagon, and turn 108° for a pentagon does not close.', 'Dividing 180 by the number of sides instead of 360, or forgetting that turn + inside angle = 180°.', 'Stars: thinking the turns always add up to 360°. A star goes round more than once, so its turns add up to 720°, 1080° and so on.'],
    extension: 'Draw a rosette: repeat 12 [draw a square, then turn right 30]. How far does the turtle turn altogether? (12 × (360 + 30) = 4680° = 13 full turns.) Design your own rosette and predict its total turning before you run it.',
    key: [
      ['Q1', '9 sides: turn 40°, inside 140°.  10 sides: 36°, 144°.  12 sides: 30°, 150°.  18 sides: 20°, 160°.  36 sides: 10°, 170°.  Sides × turn = 360° every time.  (a) The turtle makes one full turn to come home facing the same way.  (b) 180°: the turn and the inside angle sit on one straight line.  (c) The turn gets smaller, the inside angle gets closer to 180° and the shape looks more and more like a circle.'],
      ['Q2', '(a) An equilateral triangle, drawn 3 times over (after 3 moves the turtle is back where it started).  (b) 9 × 120° = 1080° = 3 full turns.  (c) Change the turn to 40° (360 ÷ 9).'],
      ['Q3', '(a) Turn 15° (180 − 165), 24 sides (360 ÷ 15): repeat 24 [move, turn right 15].  (b) 15 sides (360 ÷ 24); inside angle 156°.  (c) No: the turn would be 50°, and 360 ÷ 50 = 7.2 is not a whole number of sides.'],
      ['Q4', 'Totals: 80, 160, 240, 320, 400, 480, 560, 640, 720.  (a) 720  (b) 2 times round (720 ÷ 360)  (c) a 9-point star  (d) 100° (180 − 80)'],
      ['Q5', '9 points, 4 times round: 1440°, turn 160°, point 20°.  18 points, 5 times round: 1800°, turn 100°, point 80°.  20 points, 3 times round: 1080°, turn 54°, point 126°.  (b) The 9-point star that goes round 4 times (20° points).'],
      ['Q6', 'Triangle 60°, 180°.  Square 90°, 360°.  Pentagon 108°, 540°.  Hexagon 120°, 720°.  (a) 180° more each time  (b) 1440° (check: 10 × 144° = 1440°)  (c) (n − 2) × 180°, or n × 180° − 360°']
    ]
  },

  script: {
    hook: ['Today you are turtle pilots. A turtle with a pen can draw any shape, but only if you tell it exactly how far to turn at every corner.', 'Our rule today: work the turn out with maths first, then test it in code. Notice it. Test it. Explain why.'],
    warmIntro: ['Stand up and face your screen. Call that north. I am the programmer and you are the turtle. Turn right 90. Which way are you facing now?', 'Now: how can you make one full turn using 3 equal turns? How big is each turn?'],
    predict: ['Here is the square program: repeat 4, move 100, turn right 90. I want an equilateral triangle. What turn should I type? Write your prediction on your whiteboard before anyone runs it.'],
    exploreHints: ['Stuck: walk the shape yourself. Walk one side, then turn at the corner. How far did your body turn?', 'Typed turn 60 for the triangle? Run it and look. Does the turtle come home? How far has it turned altogether?', 'Finished early: predict the turn for a regular shape with 10 sides, then test it.'],
    think: ['“An octagon has 8 equal turns. To come home facing the same way the turtle turns 360° altogether, so each turn is 360 ÷ 8 = 45°. The turn and the inside angle sit on one straight line, so the inside angle is 180 − 45 = 135°.”', '“Working backwards: the inside angle is 174°, so the turn is 180 − 174 = 6°. The turns make 360°, so there are 360 ÷ 6 = 60 sides.”', '“For the star the turtle goes round twice: 720° altogether. 5 equal turns: 720 ÷ 5 = 144°. The angle at each point is 180 − 144 = 36°.”'],
    circulate: ['Ask: “What did you predict before you ran it? Were you right?”', 'Ask: “How far has your turtle turned altogether? How do you know?”', 'Ask: “Which angle does the turtle turn: the inside angle or the outside one? Show me on the picture.”'],
    hints: ['Hint 1: “To come home facing the same way, the turtle makes one full turn: 360°.”', 'Hint 2: “The corners are equal, so share 360° equally between them.”', 'Hint 3: “The turn and the inside angle sit on one straight line: they add up to 180°.”'],
    talk: ['“Ali says the turtle turns by the inside angle of the shape. Mei says it turns by the outside angle. Who is right? Use a triangle to explain.”', '“Why do the turns add up to 360° for every shape the turtle draws going round once?”'],
    talkAns: 'Mei is right. For an equilateral triangle the inside angle is 60° but the turtle turns 120°; turning 60° three times only draws half a hexagon. The turtle starts facing one way and comes home facing the same way after going round once, so it has made exactly one full turn: 360°. A star goes round more than once, so its turns add up to 720°, 1080° and so on.',
    close: ['“Today you predicted every turn with maths and then tested it in code. That is how mathematicians and programmers work together. Well done, inquirers!”']
  },

  deck: {
    today: 'Program a turtle to draw regular polygons and stars, and use the 360° turn to predict every angle before we test it in code.',
    warmGame: 'Turtle says. Stand and face the screen (north). The tutor calls turns; you turn your body and say which way you face. Last one: one full turn in 3 equal turns. How big is each?',
    warmQs: [['Angles on a straight line add up to …?', '180°'], ['How many degrees in a full turn?', '360°'], ['Two angles of a triangle are 50° and 75°. What is the third?', '55°'], ['What is 360 ÷ 8?', '45'], ['Face north. Turn right 90°, then right 180°. Which way do you face?', 'West']],
    expSetup: ['Open Scratch and add the Pen extension. Build: pen down, repeat 4 [move 100, turn right 90].', 'Change it to draw an equilateral triangle. Predict the turn first, then run it.', 'Now a regular pentagon (5 sides) and a regular hexagon (6 sides). Predict, then test.', 'Record sides, turn and “did it close?”. What do sides × turn always make?'],
    expPic: 'the square program as coloured blocks (pen down; repeat 4: move 100 steps, turn right 90 degrees) next to the square it draws, with a small turtle arrow at the start.',
    expAsk: [['What turn did the triangle need? What happened if you typed 60?', '120°. Turn 60 draws only half a hexagon: 3 × 60 = 180°, so the turtle does not come home.'], ['What turns did the pentagon and hexagon need?', 'Pentagon 72°, hexagon 60°.'], ['What do sides × turn always make? Why?', '360°: the turtle comes home facing the same way, so it has made one full turn.']],
    mini1: { head: 'Regular octagon: find the turn', body: ['Going round once, the turtle turns 360° altogether.', '8 equal turns: 360 ÷ 8 = ?', 'Inside angle = 180° − turn.', 'Test it: repeat 8 [move 80, turn right ?]'], ans: 'Turn 45°, inside angle 135°.' },
    mini2: { head: 'A 5-point star', body: ['repeat 5 [move 150, turn right 144]', '5 × 144° = 720°: the turtle goes round twice.', 'Turn = 360° × times round ÷ points = 720 ÷ 5.', 'Angle at each point = 180° − turn = ?'], ans: 'Turn 144°, 36° at each point.' },
    keyHead: 'Key idea: the 360° turn',
    keyBig: 'Going once round a closed shape, the turtle turns 360° altogether. A regular polygon with n sides turns 360° ÷ n at each corner, and its inside angle is 180° − turn.',
    keySmall: 'A star goes round more than once: turn = 360° × times round ÷ points.',
    brk: 'Turtle dance. Walk a square on the spot: step, quarter turn, four times. Then a triangle: step, turn a third of a turn, three times. Then a hexagon.',
    ws1: 'Page 1, in pairs at the computer: Q1 the polygon table, Q2 Ben’s buggy nonagon, Q3 work backwards from an angle.',
    ws2: 'Page 2, on your own: Q4 trace the star program, Q5 plan three stars, Q6 add up the inside angles and find a rule.'
  },

  qbank: {
    core: [
      { q: 'A turtle draws a regular hexagon. How many degrees does it turn at each corner?', a: '60° (360 ÷ 6)' },
      { q: 'What is each inside angle of a regular hexagon?', a: '120° (180 − 60)' },
      { q: 'Fill in the turn so the turtle draws a square: repeat 4 [move 100, turn right ___ ]', a: '90' },
      { q: 'A regular polygon has a turn angle of 72°. How many sides does it have?', a: '5 (360 ÷ 72): a regular pentagon' },
      { q: 'At a corner the turtle turns 50°. What is the inside angle at that corner?', a: '130° (180 − 50)' },
      { q: 'A turtle draws any triangle and comes back to the start facing the same way. How many degrees has it turned altogether?', a: '360°' }
    ],
    stretch: [
      { q: 'Each inside angle of a regular polygon is 4 times its turn angle. How many sides does the polygon have?', a: '10 (turn + 4 × turn = 180°, so the turn is 36° and 360 ÷ 36 = 10; check: inside 144° = 4 × 36°)' },
      { q: 'Each inside angle of a regular polygon is 140°. What do all its inside angles add up to?', a: '1260° (turn 40°, so 9 sides; 9 × 140° = 1260°; check (9 − 2) × 180° = 1260°)' },
      { q: 'Mei’s turtle draws a shape with 4 sides. Its first three turns are 70°, 100° and 90°. It comes home facing the same way after going round once. What is its last turn? What is the inside angle at that corner?', a: 'Last turn 100° (360 − 70 − 100 − 90); inside angle 80° (180 − 100)' },
      { q: 'A regular polygon has n sides. Write its turn angle and its inside angle using n.', a: 'Turn = 360 ÷ n; inside angle = 180 − 360 ÷ n' },
      { q: 'In a regular polygon the turn angle is the same as the inside angle. Which polygon is it?', a: 'A square (turn = inside = 90°, because they add up to 180°)' },
      { q: 'Which regular polygons with 10 to 20 sides have a whole-number turn angle?', a: '10, 12, 15, 18 and 20 sides (turns 36°, 30°, 24°, 20°, 18°); 360 cannot be shared exactly into 11, 13, 14, 16, 17 or 19 equal turns' },
      { q: 'Regular hexagons fit together around a point with no gaps, like a honeycomb. Explain why using angles. Can regular pentagons do the same?', a: 'Three hexagon angles make 3 × 120° = 360°. Pentagons cannot: 3 × 108° = 324° leaves a gap and 4 × 108° = 432° overlaps.' },
      { q: 'A turtle draws a regular hexagon, then a square, then an equilateral triangle, each once round, ending each shape facing the way it started. How many degrees does it turn altogether?', a: '1080° (360° for each shape: 3 × 360°)' }
    ],
    challenge: [
      { q: 'Ali wants a regular pentagon. He types the inside angle by mistake: repeat 5 [move 100, turn right 108]. Does his shape close? How many repeats would make it close, and what would it draw?', a: 'No: 5 × 108° = 540° is not a whole number of turns. 108 × 10 = 1080 = 3 × 360, so 10 repeats close it: a 10-point star that goes round 3 times (each point 72°).' },
      { q: 'How many different stars with 9 points can a turtle draw using equal moves and equal turns? Give the turns.', a: '2: turn 80° (round 2 times) and turn 160° (round 4 times). Turn 120° (3 times round) only draws a triangle 3 times; turns of 200°, 280° … give the same stars turned the other way.' },
      { q: 'Each inside angle of a regular polygon is 5 times its turn angle. How many sides does it have?', a: '12 (6 × turn = 180°, turn 30°, 360 ÷ 30 = 12)' },
      { q: 'How many different 12-point stars can a turtle draw with equal moves and equal turns? Give the turn and how many times it goes round.', a: 'Only 1: turn 150°, going round 5 times (5 × 360 ÷ 12). Turns 60°, 90° and 120° (round 2, 3, 4 times) just redraw a hexagon, square or triangle, and 180° goes back and forth on a line.' },
      { q: 'A turtle runs: repeat 12 [repeat 4 (move 100, turn right 90), turn right 30]. How many full turns does it make altogether?', a: '13 (12 × (360° + 30°) = 4680° = 13 × 360°)' },
      { q: 'Each inside angle of a regular polygon is 20° bigger than each inside angle of a regular hexagon. How many sides does it have?', a: '9 (inside 140°, turn 40°, 360 ÷ 40 = 9)' },
      { q: 'All the inside angles of a regular polygon add up to 1800°. How many sides does it have, and what is its turn angle?', a: '12 sides ((12 − 2) × 180° = 1800°); turn 30°' },
      { q: 'Three hexagons fit exactly around a point: 120° + 120° + 120° = 360°. Find two other sets of three regular polygons that fit exactly around a point.', a: 'Any two of: square + octagon + octagon (90 + 135 + 135); triangle + 12-gon + 12-gon (60 + 150 + 150); square + hexagon + 12-gon (90 + 120 + 150); pentagon + pentagon + 10-gon (108 + 108 + 144); triangle + 10-gon + 15-gon (60 + 144 + 156); also triangle with 18 and 9 sides (60 + 160 + 140), 24 and 8 sides (60 + 165 + 135), 42 and 7 sides; square + pentagon + 20-gon (90 + 108 + 162).' },
      { q: 'Why can a turtle not draw a 6-point star in one go, with equal moves and equal turns? Try turns of 120° and 180°.', a: 'For 6 corners the turn must be 360° × times round ÷ 6 = 60°, 120°, 180°, 240° or 300°. 60° (and 300°) draw a hexagon, 120° (and 240°) go round a triangle twice, and 180° goes back and forth on a line. None visits 6 points as a star (a Star of David is two triangles, so it needs the pen lifted).' }
    ]
  },

  workbook: H => {
    const head = ['Regular polygon', 'Sides', 'Turn angle', 'Inside angle', 'Sides × turn'], w1 = [2700, 1800, 1800, 1800, 1800];
    const rows1 = [['Equilateral triangle', '3', '120°', '60°', '360°'], ['Nonagon', '9', '', '', ''], ['Decagon', '10', '', '', ''], ['Dodecagon', '12', '', '', ''], ['18-gon', '18', '', '', ''], ['36-gon', '36', '', '', '']];
    const t1 = H.tbl(w1, [H.row(head.map((s, i) => H.cell(s, w1[i], { bold: true, fill: 'D9D9D9', size: 22 }))),
      ...rows1.map((r, j) => H.row(r.map((s, i) => H.cell(s, w1[i], { h: 60, size: 22, fill: j === 0 ? 'F2F2F2' : undefined, bold: i < 2 }))))]);
    const q2prog = [['event', 'when green flag clicked'], ['pen', 'erase all'], ['pen', 'pen down'], ['ctrl', 'repeat {9}', [['motion', 'move {80} steps'], ['motion', 'turn right {120} degrees']]]];
    const q4prog = [['event', 'when green flag clicked'], ['var', 'set {total} to {0}'], ['pen', 'pen down'], ['ctrl', 'repeat {9}', [['motion', 'move {150} steps'], ['motion', 'turn right {80} degrees'], ['var', 'change {total} by {80}']]], ['looks', 'say {total}']];
    const w4 = [1800, ...Array(9).fill(900)];
    const t4 = H.tbl(w4, [H.row([H.cell('After repeat', w4[0], { bold: true, fill: 'EDEDED', size: 20 }), ...[1, 2, 3, 4, 5, 6, 7, 8, 9].map(i => H.cell(String(i), 900, { bold: true, fill: 'EDEDED', size: 22 }))]),
      H.row([H.cell('total', w4[0], { bold: true, size: 22, h: 90 }), ...Array(9).fill(0).map(() => H.cell('', 900, { h: 90 }))])]);
    const w5 = [1700, 2000, 2200, 2000, 2000];
    const t5 = H.tbl(w5, [H.row(['Points', 'Times round', 'Total turning', 'Turn angle', 'Angle at each point'].map((s, i) => H.cell(s, w5[i], { bold: true, fill: 'D9D9D9', size: 21 }))),
      ...[['5', '2', '720°', '144°', '36°'], ['9', '4', '', '', ''], ['18', '5', '', '', ''], ['20', '3', '', '', '']].map((r, j) => H.row(r.map((s, i) => H.cell(s, w5[i], { h: 60, size: 22, fill: j === 0 ? 'F2F2F2' : undefined, bold: i < 2 }))))]);
    const w6 = [2700, 1600, 2600, 3000];
    const t6 = H.tbl(w6, [H.row(['Regular polygon', 'Sides', 'Each inside angle', 'All inside angles added'].map((s, i) => H.cell(s, w6[i], { bold: true, fill: 'D9D9D9', size: 21 }))),
      ...[['Equilateral triangle', '3'], ['Square', '4'], ['Pentagon', '5'], ['Hexagon', '6']].map(r => H.row([H.cell(r[0], w6[0], { h: 55, size: 22, bold: true }), H.cell(r[1], w6[1], { h: 55, size: 22, bold: true }), H.cell('', w6[2]), H.cell('', w6[3])]))]);
    return [
      H.p('The turtle (our sprite with its pen down) turns at every corner. The turn is measured from “straight on”, so it is the OUTSIDE angle. Maths first, then test it in Scratch.', { after: 20 }),
      H.fig(cornerFig()),
      H.q(1, 'Regular polygons: all sides equal, all angles equal. Work out each turn and inside angle. Then test two rows in Scratch.', { before: 40, keepNext: true }),
      t1,
      H.sub('a', 'What do you notice about the last column? Why does this happen?', { after: 20 }), ...H.lines(1),
      H.sub('b', 'Add the turn angle and the inside angle in any row. What do you get? Why?', { after: 20 }), ...H.lines(1),
      H.sub('c', 'What happens to the angles as the number of sides grows? What does the 36-gon look like on screen?', { after: 20 }), ...H.lines(1),
      H.q(2, 'Ben wants to draw a regular nonagon (9 sides). Predict what his program draws before you run it.', { keepNext: true }),
      H.fig(codeAndFrame(q2prog, 'Ben’s program: when green flag clicked, erase all, pen down, repeat 9: move 80 steps, turn right 120 degrees. A box to draw a prediction.', 'Draw your prediction here')),
      H.sub('a', 'What does the turtle draw? Explain.', { after: 20 }), ...H.lines(1),
      H.sub('b', 'How many degrees does the turtle turn altogether?', { after: 10 }), H.ans('Answer:  ________ °'),
      H.sub('c', 'Fix Ben’s program. Which number must change, and to what?', { after: 10 }), H.ans('Answer:'),
      H.q(3, 'Plan your code: work backwards from an angle.', { keepNext: true }),
      H.sub('a', 'Each inside angle of a regular polygon is 165°. Find the turn angle and the number of sides. Then write the repeat block.', { after: 10 }),
      H.ans('Turn ______ °     Sides ______     repeat ____ [ move 50, turn right ____ ]'),
      H.sub('b', 'A regular polygon has a turn angle of 24°. How many sides does it have? What is each inside angle?', { after: 10 }),
      H.ans('Sides ______      Inside angle ______ °'),
      H.sub('c', 'Mei says a regular polygon can have inside angles of 130°. Is she right? Explain.', { after: 20 }), ...H.lines(2),

      H.q(4, 'Trace the code. This program keeps a running total of how far the turtle has turned.', { pb: true, before: 0, keepNext: true }),
      H.fig(codeAndFrame(q4prog, 'Program: when green flag clicked, set total to 0, pen down, repeat 9: move 150 steps, turn right 80 degrees, change total by 80; then say total. A box to sketch the drawing.', 'Sketch what it draws')),
      H.p('Fill in the value of total after each repeat.', { after: 20 }),
      t4,
      H.sub('a', 'What does the sprite say at the end?   ________', { after: 60 }),
      H.sub('b', 'How many times does the turtle go round? How do you know?   ____________________________', { after: 60 }),
      H.sub('c', 'What shape does it draw?   ________________', { after: 60 }),
      H.sub('d', 'What is the angle at each point of the shape?   ________ °'),
      H.q(5, 'Plan three stars. A star goes round more than once:  turn = 360° × times round ÷ points.  The angle at each point = 180° − turn.', { keepNext: true }),
      t5,
      H.sub('b', 'Which of your stars has the sharpest points? Test it in Scratch.   ______________________'),
      H.q(6, 'Add up the inside angles of regular polygons.', { keepNext: true }),
      t6,
      H.sub('a', 'What do you add each time the polygon gets one more side?   ________ °', { after: 60 }),
      H.sub('b', 'Predict the total for a regular decagon (10 sides). Check it with your answer to Q1.   ________ °', { after: 60 }),
      H.sub('c', 'Write a rule for the total of the inside angles of a polygon with n sides.   ______________________'),
      pyBox(H)
    ];
  }
};
