// Math Inquirers P6 — Lesson 7: Turtle Geometry (angles in polygons; pen drawing with turns)
// Every answer below was worked out and checked: turn = 360 ÷ sides, inside = 180 − turn,
// star turn = 360 × times round ÷ points, angle sum = (sides − 2) × 180. The Python program was run.

const NAVY = '#1B2A49', YEL = '#FFC93C', SKY = '#DDEBF7', TEAL = '#1F7A6F', RED = '#D64545', WHITE = '#FFFFFF';
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

// ---------- code blocks: our own simple coloured shapes (never Scratch artwork) ----------
// prog: [kind, text] or [kind, text, [children]] for a C-shaped block; {…} marks a white slot.
const BC = { event: [YEL, NAVY], ctrl: [WHITE, NAVY], motion: [SKY, NAVY], pen: [TEAL, WHITE], var: [RED, WHITE], looks: [YEL, NAVY] };
const cwid = (s, fs) => [...s].reduce((a, c) => a + fs * (/[iltfjr .,:()'|]/.test(c) ? 0.36 : /[A-Zmw%×]/.test(c) ? 0.78 : 0.62), 0);
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
  const t = 70, B = [150, 34], r = Math.PI / 180;
  const A = [20, B[1]], C = [B[0] + 95 * Math.cos(t * r), B[1] + 95 * Math.sin(t * r)];
  const pt = (rad, a) => [(B[0] + rad * Math.cos(a * r)).toFixed(1), (B[1] + rad * Math.sin(a * r)).toFixed(1)];
  const arc = (rad, a1, a2, col) => `<path d="M${pt(rad, a1).join(' ')} A${rad} ${rad} 0 0 1 ${pt(rad, a2).join(' ')}" fill="none" stroke="${col}" stroke-width="3.5"/>`;
  let s = `<svg aria-label="A corner of a shape. The turtle walks along one side, then turns 70 degrees from straight on. The inside angle is 110 degrees, and 70 + 110 = 180." viewBox="0 0 300 130" xmlns="http://www.w3.org/2000/svg" style="width:210px;max-width:100%">`;
  s += `<line x1="${B[0]}" y1="${B[1]}" x2="${B[0] + 110}" y2="${B[1]}" stroke="${NAVY}" stroke-width="2.5" stroke-dasharray="7 5"/>`;
  s += `<polyline points="${A.join(',')} ${B.join(',')} ${C.map(v => v.toFixed(1)).join(',')}" fill="none" stroke="${NAVY}" stroke-width="4" stroke-linejoin="round"/>`;
  s += `<polygon points="60,${B[1] - 8} 80,${B[1]} 60,${B[1] + 8}" fill="${TEAL}"/>`;
  s += arc(40, 0, t, RED) + arc(26, t, 180, TEAL);
  const [tx, ty] = pt(62, 30), [ix, iy] = pt(48, 140);
  s += `<text x="${tx}" y="${(+ty + 5).toFixed(1)}" font-size="15" font-weight="700" fill="${RED}" font-family="Arial">turn 70°</text>`;
  s += `<text x="${ix}" y="${(+iy + 12).toFixed(1)}" font-size="15" font-weight="700" text-anchor="end" fill="${TEAL}" font-family="Arial">inside 110°</text>`;
  s += `<text x="${B[0] + 30}" y="${B[1] - 8}" font-size="14" fill="${NAVY}" font-family="Arial">straight on</text>`;
  return s + '</svg>';
};

// blocks on the left; on the right an empty drawing frame, or a trace table (after repeat 1..rows, value blank)
const codeAndFrame = (prog, label, frameText, trace) => {
  const b = blocks(prog, { fs: 14, h: 25 }), W = 600, fx = b.w + 30;
  const Ht = Math.max(b.h, trace ? (trace.rows + 1) * 22 + 4 : 140);
  let s = `<svg aria-label="${esc(label)}" viewBox="0 0 ${W} ${Ht + 4}" xmlns="http://www.w3.org/2000/svg" style="width:560px;max-width:100%">` + b.svg;
  if (frameText) s += `<rect x="${fx}" y="2" width="${W - fx - 4}" height="${Ht}" rx="12" fill="${WHITE}" stroke="${NAVY}" stroke-width="2" stroke-dasharray="7 5"/><text x="${fx + 12}" y="22" font-size="14" fill="${NAVY}" font-family="Arial">${esc(frameText)}</text>`;
  if (trace) {
    const c1 = 130, c2 = 130, x0 = W - c1 - c2 - 6;
    s += `<rect x="${x0}" y="2" width="${c1 + c2}" height="22" fill="${YEL}" stroke="${NAVY}" stroke-width="2"/><text x="${x0 + c1 / 2}" y="18" font-size="14" font-weight="700" text-anchor="middle" fill="${NAVY}" font-family="Arial">after repeat</text><text x="${x0 + c1 + c2 / 2}" y="18" font-size="14" font-weight="700" text-anchor="middle" fill="${NAVY}" font-family="Arial">${esc(trace.head)}</text>`;
    let d = '';
    for (let i = 1; i <= trace.rows; i++) { const y = 2 + 22 * i; d += `<text x="${x0 + c1 / 2}" y="${y + 16}" font-size="14" font-weight="700" text-anchor="middle" fill="${NAVY}" font-family="Arial">${i}</text>`; }
    s += `<rect x="${x0}" y="24" width="${c1 + c2}" height="${22 * trace.rows}" fill="${WHITE}" stroke="${NAVY}" stroke-width="2"/>` + d;
    s += `<path d="M${x0 + c1} 2 V${24 + 22 * trace.rows}${Array.from({ length: trace.rows - 1 }, (_, i) => ` M${x0} ${46 + 22 * i} H${x0 + c1 + c2}`).join('')}" stroke="${NAVY}" stroke-width="1" fill="none"/>`;
  }
  return s + '</svg>';
};

const PY = `import turtle
t = turtle.Turtle()
n, k = 5, 2   # points, rounds
turn = 360 * k / n
for i in range(n):
    t.forward(150)
    t.right(turn)
print(turn, n * turn)
turtle.done()`;
// checked by running it (with a recording stand-in for the turtle window): prints "144.0 720.0" (the turn, then the total turning)

const pyHTML = s => esc(s).split('\n').map(l => l.replace(/^ +/, m => '&nbsp;'.repeat(m.length)).replace(/ {2,}/g, m => '&nbsp;'.repeat(m.length))).join('<br>');
const pyBox = H => {
  const ls = PY.split('\n'), code = part => `<div style="text-align:left;font-family:'Liberation Mono',Consolas,monospace;font-size:12.5px;line-height:1.3">${pyHTML(part.join('\n'))}</div>`;
  return H.tbl([3100, 3400, 3400], [H.row([
    H.cell('<div style="text-align:left;font-weight:700">Python version (optional)<div style="font-weight:400;margin-top:2px">Prints the turn and the total (144.0 720.0). Needs Python turtle, e.g. Trinket.</div></div>', 3100, { fill: 'DDEBF7', h: 40 }),
    H.cell(code(ls.slice(0, 4)), 3400, { h: 40 }), H.cell(code(ls.slice(4)), 3400, { h: 40 })])]);
};

module.exports = {
  lesson: {
    n: 7, week: 4, session: 'A', title: 'Turtle Geometry', topic: 'Angles in Polygons',
    objective: 'Use the idea that a turtle going once round a closed shape turns 360° altogether to find the turn angle (360° ÷ sides) and inside angle (180° − turn) of regular polygons, work backwards from an angle to the number of sides, extend to star polygons (turn = 360° × times round ÷ points), and test every prediction with a pen program in Scratch (or Python turtle).',
    skills: 'Turn (exterior) and inside (interior) angles, angles on a straight line, angle sum of a polygon, star polygons, predicting and tracing code, repeat loops and variables',
    materials: 'A laptop or desktop with Scratch 3 open (scratch.mit.edu) and the Pen extension added, mini whiteboards, a protractor, plain or squared paper.',
    online: 'Pairs work in breakout rooms: one child drives Scratch and shares the screen, the other predicts, then they swap. Children hold drawings up to the camera. A tablet works for Scratch but is slower. Every drawing starts with the same 4 set-up blocks (erase all, go to x: -50 y: 100, point in direction 90, pen down) so shapes stay on the stage; turn blocks in Scratch show an arrow (turn ↻ is clockwise, our “turn right”). Block colours on our slides are simplified; in Scratch, find blocks by the category name on the left (Motion, Pen, Control), not by colour.',
    warmup: 'Turtle says: everyone stands and faces the screen (call it north). The tutor calls turns (right 90, right 180, left 270, right 45, right 360) and children turn their bodies, then say which way they face. Finish with: one full turn made of 3 equal turns. How big is each turn?',
    explore: 'At the computer in pairs: build the square program (the 4 set-up blocks, then repeat 4: move 100, turn ↻ 90; the clockwise arrow block is “turn right”). The 4 set-up blocks are erase all, go to x: -50 y: 100, point in direction 90, pen down: they start every run in the same place so big shapes stay on the 480 by 360 stage. Change it to draw an equilateral triangle, then a regular pentagon and a regular hexagon, predicting each turn before running it. Record the sides, the turn and whether the shape closes. What do sides × turn always make?',
    mini: 'The turtle turns the outside angle: turn + inside angle = 180°. Going round once, the turns add up to 360°, so a regular polygon with n sides turns 360° ÷ n (octagon: turn 45°, inside 135°). Work backwards from an inside angle (174° → turn 6° → 60 sides; 115° is impossible because 360 ÷ 65 is not whole). A star goes round more than once: the 5-point star turns 720° ÷ 5 = 144°. Before page 2: trace a running total in a table, plan an 8-point star that goes round 3 times, and add up the inside angles of an octagon (1080°).',
    share: 'Ali says the turtle turns by the inside angle of the shape. Mei says it turns by the outside angle. Who is right? Use a triangle to explain.',
    exit: { q: 'A turtle draws a regular polygon and turns 5° at every corner. How many sides does the polygon have? What is each inside angle?', a: '72 sides (360 ÷ 5 = 72); each inside angle is 175° (180 − 5)' },
    mistakes: ['Using the inside angle as the turn: turn 60° for a triangle draws half a hexagon, and turn 108° for a pentagon does not close.', 'Dividing 180 by the number of sides instead of 360, or forgetting that turn + inside angle = 180°.', 'Stars: thinking the turns always add up to 360°. A star goes round more than once, so its turns add up to 720°, 1080° and so on.'],
    extension: 'Draw a rosette: repeat 12 [draw a square, then turn ↻ 30]. Start this one with go to x: 0 y: 0 instead of x: -50 y: 100, so the rosette stays on the stage. How far does the turtle turn altogether? (12 × (360 + 30) = 4680° = 13 full turns.) Design your own rosette and predict its total turning before you run it.',
    key: [
      ['Q1', '3 sides (example): 120°, 60°, 360°.  9 sides: turn 40°, inside 140°.  10 sides: 36°, 144°.  36 sides: 10°, 170°.  Turn 24°: 15 sides, inside 156°.  Inside 165°: turn 15°, 24 sides.  Last column 360° every time.  (a) Sides × turn = 360°: the turtle makes one full turn to come home facing the same way.  (b) No: the turn would be 50°, and 360 ÷ 50 = 7.2 is not a whole number of sides.'],
      ['Q2', '(a) An equilateral triangle, drawn 3 times over (each turn of 120° is a triangle’s turn, so after 3 moves the turtle is back where it started).  (b) 9 × 120° = 1080° = 3 full turns.  (c) Change the turn from 120 to 40 (360 ÷ 9).'],
      ['Q3', 'Totals: 80, 160, 240, 320, 400, 480, 560, 640, 720.  (a) 720  (b) 2 times (720 ÷ 360)  (c) a 9-point star  (d) 100° (180 − 80)'],
      ['Q4', '9 points, 4 times round: total 1440°, turn 160°, point 20°.  20 points, 3 times round: total 1080°, turn 54°, point 126°.  Sharper points: the 9-point star (20°).'],
      ['Q5', 'Each inside angle: 60°, 90°, 108°, 120°, 144°.  Added: 180°, 360°, 540°, 720°, 1440°.  (a) 180°  (b) (n − 2) × 180°, or n × 180° − 360°']
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
    expSetup: ['Add the Pen extension. Build the 4 set-up blocks, then repeat 4 [move 100, turn ↻ 90].', 'Change it to draw an equilateral triangle. Predict the turn first, then run it.', 'Now a regular pentagon (5 sides) and a regular hexagon (6 sides). Predict, then test.', 'Record sides, turn and “did it close?”. What do sides × turn always make?'],
    expPic: 'the square program as coloured blocks (pen down; repeat 4: move 100 steps, turn ↻ 90 degrees) next to the square it draws, with a small turtle arrow at the start.',
    expAsk: [['What turn did the triangle need? What happened if you typed 60?', '120°. Turn 60 draws only half a hexagon: 3 × 60 = 180°, so the turtle does not come home.'], ['What turns did the pentagon and hexagon need?', 'Pentagon 72°, hexagon 60°.'], ['What do sides × turn always make? Why?', '360°: the turtle comes home facing the same way, so it has made one full turn.']],
    mini1: { head: 'Regular octagon: find the turn', body: ['Going round once, the turtle turns 360° altogether.', '8 equal turns: 360 ÷ 8 = ?', 'Inside angle = 180° − turn.', 'Test it: repeat 8 [move 80, turn ↻ ?]'], ans: 'Turn 45°, inside angle 135°.' },
    mini2: { head: 'A 5-point star', body: ['repeat 5 [move 150, turn ↻ 144]', '5 × 144° = 720°: the turtle goes round twice.', 'Turn = 360° × times round ÷ points = 720 ÷ 5.', 'Angle at each point = 180° − turn = ?'], ans: 'Turn 144°, 36° at each point.' },
    keyHead: 'Key idea: the 360° turn',
    keyBig: 'Going once round a closed shape, the turtle turns 360° altogether. A regular polygon with n sides turns 360° ÷ n at each corner, and its inside angle is 180° − turn.',
    keySmall: 'A star goes round more than once: turn = 360° × times round ÷ points.',
    brk: 'Turtle dance. Walk a square on the spot: step, quarter turn, four times. Then a triangle: step, turn a third of a turn, three times. Then a hexagon.',
    ws1: 'Page 1, in pairs at the computer: Q1 the polygon table, forwards and backwards; Q2 Ben’s buggy nonagon.',
    ws2: 'Page 2, on your own: Q3 trace the star program, Q4 plan two stars, Q5 add up the inside angles and find a rule.'
  },

  qbank: {
    core: [
      { q: 'A turtle draws a regular hexagon. How many degrees does it turn at each corner?', a: '60° (360 ÷ 6)' },
      { q: 'What is each inside angle of a regular hexagon?', a: '120° (180 − 60)' },
      { q: 'Fill in the turn so the turtle draws a square: repeat 4 [move 100, turn ↻ ___ ]', a: '90' },
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
      { q: 'Ali wants a regular pentagon. He types the inside angle by mistake: repeat 5 [move 100, turn ↻ 108]. Does his shape close? How many repeats would make it close, and what would it draw?', a: 'No: 5 × 108° = 540° is not a whole number of turns. 108 × 10 = 1080 = 3 × 360, so 10 repeats close it: a 10-point star that goes round 3 times (each point 72°).' },
      { q: 'How many different stars with 9 points can a turtle draw using equal moves and equal turns? Give the turns.', a: '2: turn 80° (round 2 times) and turn 160° (round 4 times). Turn 120° (3 times round) only draws a triangle 3 times; turns of 200°, 280° … give the same stars turned the other way.' },
      { q: 'Each inside angle of a regular polygon is 5 times its turn angle. How many sides does it have?', a: '12 (6 × turn = 180°, turn 30°, 360 ÷ 30 = 12)' },
      { q: 'How many different 12-point stars can a turtle draw with equal moves and equal turns? Give the turn and how many times it goes round.', a: 'Only 1: turn 150°, going round 5 times (5 × 360 ÷ 12). Turns 60°, 90° and 120° (round 2, 3, 4 times) just redraw a hexagon, square or triangle, and 180° goes back and forth on a line.' },
      { q: 'A turtle runs: repeat 12 [repeat 4 (move 100, turn ↻ 90), turn ↻ 30]. How many full turns does it make altogether?', a: '13 (12 × (360° + 30°) = 4680° = 13 × 360°)' },
      { q: 'Each inside angle of a regular polygon is 20° bigger than each inside angle of a regular hexagon. How many sides does it have?', a: '9 (inside 140°, turn 40°, 360 ÷ 40 = 9)' },
      { q: 'All the inside angles of a regular polygon add up to 1800°. How many sides does it have, and what is its turn angle?', a: '12 sides ((12 − 2) × 180° = 1800°); turn 30°' },
      { q: 'A square, a hexagon and a 12-sided shape fit exactly around a point: 90° + 120° + 150° = 360°. Find one other set of three regular polygons whose inside angles add up to 360° (hint: the answer uses a square or a triangle).', a: 'Square + octagon + octagon (90° + 135° + 135°) or triangle + 12-gon + 12-gon (60° + 150° + 150°).' },
      { q: 'Try turn 120 and turn 60 with repeat 6 and move 100. Which one draws a hexagon? Why does the other not make a 6-point star?', a: 'Turn 60 draws the hexagon (6 × 60° = 360°, one full turn). Turn 120 draws a triangle twice round (6 × 120° = 720°, two full turns), and it only visits 3 corners, not 6.' }
    ]
  },

  workbook: H => {
    const w1 = [2475, 2475, 2475, 2475];
    const rows1 = [['3', '120°', '60°', '360°'], ['9', '', '', ''], ['10', '', '', ''], ['36', '', '', ''], ['', '24°', '', ''], ['', '', '165°', '']];
    const t1 = H.tbl(w1, [H.row(['Sides', 'Turn angle', 'Inside angle', 'Sides × turn'].map((s, i) => H.cell(s, w1[i], { bold: true, fill: 'D9D9D9', size: 22, h: 50 }))),
      ...rows1.map((r, j) => H.row(r.map((s, i) => H.cell(s, w1[i], { h: 45, size: 22, fill: j === 0 ? 'F2F2F2' : undefined, bold: true }))))]);
    const q2prog = [['event', 'when green flag clicked'], ['pen', 'pen down'], ['ctrl', 'repeat {9}', [['motion', 'move {80} steps'], ['motion', 'turn ↻ {120} degrees']]]];
    const q3prog = [['event', 'when green flag clicked'], ['var', 'set {total} to {0}'], ['pen', 'pen down'], ['ctrl', 'repeat {9}', [['motion', 'move {150} steps'], ['motion', 'turn ↻ {80} degrees'], ['var', 'change {total} by {80}']]], ['looks', 'say {total}']];
    const w4 = [1700, 2000, 2200, 2000, 2000];
    const t4 = H.tbl(w4, [H.row(['Points', 'Times round', 'Total turning', 'Turn angle', 'Point angle'].map((s, i) => H.cell(s, w4[i], { bold: true, fill: 'D9D9D9', size: 21, h: 45 }))),
      ...[['5', '2', '720°', '144°', '36°'], ['9', '4', '', '', ''], ['20', '3', '', '', '']].map((r, j) => H.row(r.map((s, i) => H.cell(s, w4[i], { h: 45, size: 22, fill: j === 0 ? 'F2F2F2' : undefined, bold: i < 2 }))))]);
    const w5 = [2900, 1400, 1400, 1400, 1400, 1400];
    const t5 = H.tbl(w5, [H.row(['Sides', '3', '4', '5', '6', '10'].map((s, i) => H.cell(s, w5[i], { bold: true, fill: 'D9D9D9', size: 22, h: 45 }))),
      H.row(['Each inside angle', '', '', '', '', ''].map((s, i) => H.cell(s, w5[i], { bold: i === 0, size: 21, h: 60 }))),
      H.row(['All inside angles added', '', '', '', '', ''].map((s, i) => H.cell(s, w5[i], { bold: i === 0, size: 21, h: 60 })))]);
    const intro = H.tbl([6400, 3500], [H.row([
      H.cell('The turtle turns by the OUTSIDE angle, measured from “straight on”. So turn + inside angle = 180°. Maths first, then test it in Scratch. Start every drawing with: erase all, go to x: -50 y: 100, point in direction 90, pen down. Turn with the ↻ block.', 6400, { align: 'left', h: 30 }),
      H.cell('<div style="text-align:center">' + cornerFig() + '</div>', 3500, { h: 10 })])]);
    return [
      intro,
      H.q(1, 'Regular polygons. Fill in the table: some rows go forwards, some backwards. Test two rows in Scratch (move 80; but 30 for 24 sides, 10 for 36).', { before: 40, keepNext: true }),
      t1,
      H.sub('a', 'What do you notice about the last column? Why does this happen?', { after: 20 }), ...H.lines(1),
      H.sub('b', 'Mei says a regular polygon can have inside angles of 130°. Is she right? Explain.', { after: 20 }), ...H.lines(1),
      H.q(2, 'Ben wants a regular nonagon (9 sides). Predict what his program draws, then run it (after the set-up).', { keepNext: true }),
      H.fig(codeAndFrame(q2prog, 'Ben’s program: when green flag clicked, pen down, repeat 9: move 80 steps, turn ↻ 120 degrees. A box to draw a prediction.', 'Draw your prediction here')),
      H.sub('a', 'What does the turtle draw? Explain.', { after: 20 }), ...H.lines(1),
      H.sub('b', 'Total turning  ________ °        (c)  Fix it: change  ________  to  ________'),

      H.q(3, 'Trace the code. The program keeps a running total of how far the turtle has turned. Fill in the table.', { pb: true, before: 0, keepNext: true }),
      H.fig(codeAndFrame(q3prog, 'Program: when green flag clicked, set total to 0, pen down, repeat 9: move 150 steps, turn ↻ 80 degrees, change total by 80; then say total. A trace table for total after repeats 1 to 9.', null, { rows: 9, head: 'total' })),
      H.sub('a', 'The sprite says  ________      (b)  Times the turtle goes round  ________', { after: 60 }),
      H.sub('c', 'It draws a  __________________      (d)  Point angle  ________ °'),
      H.q(4, 'Plan two stars, then test them (move 120 for the 9-point star, move 100 for the 20-point). Which has sharper points?   Turn = 360° × times round ÷ points.   Point angle = 180° − turn.', { keepNext: true }),
      t4,
      H.q(5, 'Add up the inside angles of regular polygons (use Q1 for 10 sides).', { keepNext: true }),
      t5,
      H.sub('a', 'One more side adds  ______ °      (b)  For n sides:  total = ______________'),
      pyBox(H)
    ];
  }
};
