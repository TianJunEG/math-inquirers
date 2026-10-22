// Math Inquirers P6 — Lesson 3: Below Zero (negative numbers; a sprite on a number line; variables below 0)
// Every answer below was worked out and checked (number line jumps, and the code traced by hand and run in Python).

const NAVY = '#1B2A49', YEL = '#FFC93C', SKY = '#DDEBF7', TEAL = '#1F7A6F', RED = '#D64545', WHITE = '#FFFFFF';
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const N = v => (v < 0 ? '−' + (-v) : String(v));

// ---- our own code-block drawings: rounded shapes with the block text; [x] = an input pill ----
const BK = { event: [YEL, NAVY], control: [TEAL, WHITE], var: [RED, WHITE], motion: [SKY, NAVY], looks: [WHITE, NAVY] };
const tw = (s, fs) => { let w = 0; for (const ch of s) { if ("il.,:;|!'()[] ".includes(ch)) w += 0.32; else if ('mwMW'.includes(ch)) w += 0.86; else if (ch !== ch.toLowerCase() || '−+×=<>*?'.includes(ch)) w += 0.66; else w += 0.57; } return w * fs; };
const rowParts = (x, y, text, kind, fs, rh) => {
  const [fill, fg] = BK[kind]; const segs = text.split(/(\[[^\]]*\])/).filter(Boolean); const pad = fs * 0.6;
  let out = '', cx = x + pad;
  for (const sg of segs) {
    if (sg[0] === '[') {
      const v = sg.slice(1, -1), pw = Math.max(tw(v, fs) + fs * 1.1, fs * 1.6), ph = fs * 1.3;
      out += `<rect x="${cx.toFixed(0)}" y="${(y + (rh - ph) / 2).toFixed(0)}" width="${pw.toFixed(0)}" height="${ph.toFixed(0)}" rx="${(ph / 2).toFixed(0)}" fill="${fill === WHITE ? SKY : WHITE}" stroke="${NAVY}" stroke-width="1.5"/><text x="${(cx + pw / 2).toFixed(0)}" y="${(y + rh / 2 + fs * 0.36).toFixed(0)}" font-size="${fs}" font-weight="700" text-anchor="middle" fill="${NAVY}" font-family="Arial">${esc(v)}</text>`;
      cx += pw + fs * 0.35;
    } else if (sg.trim()) {
      out += `<text x="${cx.toFixed(0)}" y="${(y + rh / 2 + fs * 0.36).toFixed(0)}" font-size="${fs}" font-weight="700" fill="${fg}" font-family="Arial">${esc(sg.trim())}</text>`;
      cx += tw(sg.trim(), fs) + fs * 0.25;
    }
  }
  return [out, cx - fs * 0.25 + pad - x];
};
// prog: [[indent, kind, text], ...]; returns {g, w, h} drawn from (ox, oy)
const blocksG = (prog, fs, ox = 0, oy = 0) => {
  const rh = fs * 1.75, arm = fs, foot = fs * 0.75; let shapes = '', texts = '', y = oy + (prog[0][1] === 'event' ? fs * 0.6 : 2), maxx = 0; const stack = [];
  const close = lv => { while (stack.length && stack[stack.length - 1][0] >= lv) { const [, x, yt, w] = stack.pop(); shapes += `<path d="M${x} ${yt} H${x + w} V${yt + rh} H${x + arm} V${y} H${x + w} V${y + foot} H${x} Z" fill="${TEAL}" stroke="${NAVY}" stroke-width="2" stroke-linejoin="round"/>`; y += foot; } };
  for (const [lv, kind, text] of prog) {
    close(lv); const x = ox + 2 + lv * arm; let [parts, w] = rowParts(x, y, text, kind, fs, rh); w = Math.max(w, fs * 4);
    if (kind === 'control') stack.push([lv, x, y, w]);
    else if (kind === 'event') shapes += `<path d="M${x} ${y + rh} V${y + fs * 0.15} Q${x + fs * 2} ${y - fs * 0.75} ${x + fs * 4} ${y + fs * 0.15} H${x + w - 8} Q${x + w} ${y + fs * 0.15} ${x + w} ${y + fs * 0.15 + 8} V${y + rh} Z" fill="${YEL}" stroke="${NAVY}" stroke-width="2" stroke-linejoin="round"/>`;
    else shapes += `<rect x="${x}" y="${y.toFixed(0)}" width="${w.toFixed(0)}" height="${rh.toFixed(0)}" rx="7" fill="${BK[kind][0]}" stroke="${NAVY}" stroke-width="2"/>`;
    texts += parts; maxx = Math.max(maxx, x + w); y += rh;
  }
  close(0);
  return { g: shapes + texts, w: maxx - ox + 4, h: y - oy + 4 };
};
const blocksSvg = (prog, label, fs = 16, maxw = 600) => { const b = blocksG(prog, fs); const W = Math.ceil(b.w), Hh = Math.ceil(b.h); return `<svg aria-label="${esc(label)}" viewBox="0 0 ${W} ${Hh}" xmlns="http://www.w3.org/2000/svg" style="width:${Math.min(W * 1.1, maxw).toFixed(0)}px;max-width:100%">${b.g}</svg>`; };
// number line from lo to hi; marks [[v, label, colour]]
const numline = (lo, hi, opts = {}) => {
  const w = opts.w || 600, h = opts.h || 80, ly = opts.ly || 34, x0 = 24, x1 = w - 24, X = v => x0 + (v - lo) * (x1 - x0) / (hi - lo);
  let s = `<line x1="${x0 - 14}" y1="${ly}" x2="${x1 + 14}" y2="${ly}" stroke="${NAVY}" stroke-width="2"/><polygon points="${x0 - 20},${ly} ${x0 - 10},${ly - 5} ${x0 - 10},${ly + 5}" fill="${NAVY}"/><polygon points="${x1 + 20},${ly} ${x1 + 10},${ly - 5} ${x1 + 10},${ly + 5}" fill="${NAVY}"/>`;
  for (let v = lo; v <= hi; v++) {
    const big = v % (opts.labEvery || 1) === 0;
    s += `<line x1="${X(v).toFixed(1)}" y1="${ly - (big ? 8 : 5)}" x2="${X(v).toFixed(1)}" y2="${ly + (big ? 8 : 5)}" stroke="${NAVY}" stroke-width="${v === 0 ? 2.5 : 1.5}"/>`;
    if (big) s += `<text x="${X(v).toFixed(1)}" y="${ly + 26}" font-size="14" font-weight="${v === 0 ? 700 : 400}" text-anchor="middle" fill="${v === 0 ? TEAL : NAVY}" font-family="Arial">${N(v)}</text>`;
  }
  for (const [v, t, c] of (opts.marks || [])) s += `<circle cx="${X(v).toFixed(1)}" cy="${ly}" r="7" fill="${c}" stroke="${NAVY}" stroke-width="2"/><text x="${X(v).toFixed(1)}" y="${ly - 14}" font-size="16" font-weight="700" text-anchor="middle" fill="${NAVY}" font-family="Arial">${esc(t)}</text>`;
  return `<svg aria-label="${esc(opts.label || 'Number line')}" viewBox="0 0 ${w} ${h}" xmlns="http://www.w3.org/2000/svg" style="width:600px;max-width:100%">${s}</svg>`;
};
// an empty trace table drawn in SVG, placed at (x, y)
const traceTable = (x, y, heads, rows, cw, rh = 30) => {
  let s = '';
  heads.forEach((t, i) => { s += `<rect x="${x + i * cw}" y="${y}" width="${cw}" height="${rh}" fill="${YEL}" stroke="${NAVY}" stroke-width="1.5"/><text x="${x + i * cw + cw / 2}" y="${y + rh / 2 + 5}" font-size="14" font-weight="700" text-anchor="middle" fill="${NAVY}" font-family="Arial">${esc(t)}</text>`; });
  rows.forEach((r, j) => r.forEach((t, i) => { s += `<rect x="${x + i * cw}" y="${y + (j + 1) * rh}" width="${cw}" height="${rh}" fill="${WHITE}" stroke="${NAVY}" stroke-width="1.5"/><text x="${x + i * cw + cw / 2}" y="${y + (j + 1) * rh + rh / 2 + 5}" font-size="14" font-weight="700" text-anchor="middle" fill="${NAVY}" font-family="Arial">${esc(t)}</text>`; }));
  return s;
};
const PY = 'temp = 5\nfor hour in range(6):\n    temp = temp + (-3)\n    print(temp)';
const planFig = () => {
  const b = blocksG([[0, 'event', 'when green flag clicked'], [0, 'var', 'set depth to [      ]'], [0, 'control', 'repeat [      ]'], [1, 'var', 'change depth by [      ]'], [1, 'looks', 'say [depth] for [1] seconds']], 14, 4, 6);
  let s = `<svg aria-label="Plan with blanks: set depth to blank, repeat blank, change depth by blank, say depth. Question (b) beside it, and an optional Python box." viewBox="0 0 600 186" xmlns="http://www.w3.org/2000/svg" style="width:600px;max-width:100%">${b.g}`;
  s += `<text x="300" y="18" font-size="15" fill="${NAVY}" font-family="Arial">(a) Fill in the three blanks.</text>`;
  s += `<text x="300" y="40" font-size="15" fill="${NAVY}" font-family="Arial">(b) After the loop she is at −28 m.</text><text x="320" y="58" font-size="15" fill="${NAVY}" font-family="Arial">One more block: change depth by ______.</text><text x="320" y="76" font-size="15" fill="${NAVY}" font-family="Arial">What number brings her back to 0 m?</text>`;
  s += `<rect x="300" y="94" width="296" height="90" rx="10" fill="${SKY}" stroke="${NAVY}" stroke-width="1.5"/><text x="310" y="111" font-size="14" font-weight="700" fill="${TEAL}" font-family="Arial">Know Python? Today’s thermometer:</text>`;
  PY.split('\n').forEach((l, i) => { s += `<text x="314" y="${130 + i * 16}" font-size="14" fill="${NAVY}" font-family="Courier New, monospace" xml:space="preserve">${esc(l)}</text>`; });
  return s + '</svg>';
};

// sea-level picture on the left, the three questions with answer lines on the right
const seaFig = () => {
  const lvl = 92, sc = 5, Y = v => lvl - v * sc;
  let s = `<svg aria-label="Sea level picture: a seagull at 9 m, a diver at minus 6 m and a crab at minus 15 m, with three questions beside it" viewBox="0 0 600 186" xmlns="http://www.w3.org/2000/svg" style="width:600px;max-width:100%">`;
  s += `<rect x="100" y="${lvl}" width="230" height="${186 - lvl}" fill="${SKY}"/><path d="M100 ${lvl} q11.5 -6 23 0 t23 0 t23 0 t23 0 t23 0 t23 0 t23 0 t23 0 t23 0 t23 0" fill="none" stroke="${NAVY}" stroke-width="2"/>`;
  s += `<line x1="62" y1="${Y(12)}" x2="62" y2="${Y(-17)}" stroke="${NAVY}" stroke-width="2"/>`;
  for (let v = -15; v <= 10; v += 5) s += `<line x1="56" y1="${Y(v)}" x2="68" y2="${Y(v)}" stroke="${NAVY}" stroke-width="2"/><text x="50" y="${Y(v) + 5}" font-size="14" text-anchor="end" fill="${v === 0 ? TEAL : NAVY}" font-weight="${v === 0 ? 700 : 400}" font-family="Arial">${N(v)} m</text>`;
  s += `<line x1="68" y1="${Y(9)}" x2="140" y2="${Y(9)}" stroke="${NAVY}" stroke-dasharray="4 4"/><line x1="68" y1="${Y(-6)}" x2="140" y2="${Y(-6)}" stroke="${NAVY}" stroke-dasharray="4 4"/><line x1="68" y1="${Y(-15)}" x2="205" y2="${Y(-15)}" stroke="${NAVY}" stroke-dasharray="4 4"/>`;
  s += `<path d="M146 ${Y(9)} q11 -12 22 0 q11 -12 22 0" fill="none" stroke="${NAVY}" stroke-width="3"/><text x="196" y="${Y(9) + 5}" font-size="15" font-weight="700" fill="${NAVY}" font-family="Arial">seagull: 9 m</text>`;
  s += `<ellipse cx="166" cy="${Y(-6)}" rx="22" ry="7" fill="${YEL}" stroke="${NAVY}" stroke-width="2"/><circle cx="194" cy="${Y(-6)}" r="7" fill="${YEL}" stroke="${NAVY}" stroke-width="2"/><text x="208" y="${Y(-6) + 5}" font-size="15" font-weight="700" fill="${NAVY}" font-family="Arial">diver: −6 m</text>`;
  s += `<ellipse cx="222" cy="${Y(-15) - 3}" rx="14" ry="8" fill="${RED}" stroke="${NAVY}" stroke-width="2"/><text x="242" y="${Y(-15) + 2}" font-size="15" font-weight="700" fill="${NAVY}" font-family="Arial">crab: −15 m</text>`;
  s += `<text x="236" y="${lvl - 8}" font-size="14" font-weight="700" fill="${TEAL}" font-family="Arial">sea level</text>`;
  const qs = [['(a) How far above the diver', 'is the seagull?'], ['(b) How far below the diver', 'is the crab?'], ['(c) The diver swims up 4 m, then', 'down 11 m. Her height now?']];
  qs.forEach((q, i) => { const y = 22 + i * 58; s += `<text x="350" y="${y}" font-size="15" fill="${NAVY}" font-family="Arial">${esc(q[0])}</text><text x="370" y="${y + 22}" font-size="15" fill="${NAVY}" font-family="Arial">${esc(q[1])}</text><line x1="${370 + tw(q[1], 15) * 0.86 + 8}" y1="${y + 24}" x2="596" y2="${y + 24}" stroke="#8A94AD" stroke-width="1.5" stroke-dasharray="3 3"/>`; });
  return s + '</svg>';
};

const traceFig = () => {
  const b = blocksG([[0, 'event', 'when green flag clicked'], [0, 'motion', 'set x to [40]'], [0, 'control', 'repeat [4]'], [1, 'motion', 'change x by [−30]'], [0, 'looks', 'say [x position]']], 14, 4, 6);
  let s = `<svg aria-label="Code: set x to 40, repeat 4: change x by minus 30, then say x position. Beside it an empty trace table and two questions." viewBox="0 0 600 ${Math.max(Math.ceil(b.h) + 8, 150)}" xmlns="http://www.w3.org/2000/svg" style="width:600px;max-width:100%">${b.g}`;
  s += traceTable(250, 8, ['repeat', 'start', '1', '2', '3', '4'], [['x', '40', '', '', '', '']], 57, 28);
  const qs = [['(a) What does the sprite say at the end?', ''], ['(b) How many MORE repeats would take', 'it to x = −200?']];
  s += `<text x="250" y="96" font-size="15" fill="${NAVY}" font-family="Arial">(a) What does it say at the end?</text><line x1="478" y1="98" x2="596" y2="98" stroke="#8A94AD" stroke-width="1.5" stroke-dasharray="3 3"/>`;
  s += `<text x="250" y="124" font-size="15" fill="${NAVY}" font-family="Arial">(b) How many MORE repeats would</text><text x="270" y="146" font-size="15" fill="${NAVY}" font-family="Arial">take it to x = −200?</text><line x1="410" y1="148" x2="596" y2="148" stroke="#8A94AD" stroke-width="1.5" stroke-dasharray="3 3"/>`;
  return s + '</svg>';
};

// code blocks on the left, questions with answer lines on the right (lines: text rows; blanks: row indexes that get an answer line)
const codeQ = (prog, lines, blanks, label) => {
  const b = blocksG(prog, 14, 4, 6); const H2 = Math.max(Math.ceil(b.h) + 6, lines.length * 25 + 12);
  let s = `<svg aria-label="${esc(label)}" viewBox="0 0 600 ${H2}" xmlns="http://www.w3.org/2000/svg" style="width:560px;max-width:100%">${b.g}`;
  lines.forEach((t, i) => { const y = 20 + i * 25; s += `<text x="310" y="${y}" font-size="15" fill="${NAVY}" font-family="Arial">${esc(t)}</text>`; if (blanks.includes(i)) s += `<line x1="${310 + tw(t, 15) * 0.86 + 8}" y1="${y + 2}" x2="596" y2="${y + 2}" stroke="#8A94AD" stroke-width="1.5" stroke-dasharray="3 3"/>`; });
  return s + '</svg>';
};

module.exports = {
  lesson: {
    n: 3, week: 2, session: 'A', title: 'Below Zero', topic: 'Negative Numbers',
    objective: 'Order and compare negative numbers on a number line; add and subtract with negative numbers by moving along the line, in temperature, lift and sea-level contexts; use "change by" a negative number in code and trace a variable that goes below 0.',
    skills: 'Number line reasoning, splitting a jump at 0, difference as a distance, tracing code, debugging, planning a loop',
    materials: 'Laptop or desktop with Scratch 3 (scratch.mit.edu, free, no log-in needed), mini whiteboard and marker, workbook, pencil.',
    online: 'Children keep Scratch open in one browser tab and the video call in another. The tutor screen-shares Scratch to show the x number under the stage. Children share their screens only when asked; page 1 of the worksheet is done on paper with laptops turned away. Type the minus sign with the keyboard minus key (the hyphen); do not copy and paste a number from the slide or chat, because the slide uses a different minus character that Scratch will not accept. Block colours on our slides are simplified; in Scratch, find blocks by the category name on the left, not by colour.',
    warmup: 'Cold city line-up: five cities on a December morning (Singapore 25 °C, Tokyo 3 °C, Seoul −7 °C, Beijing −9 °C, Harbin −22 °C). Children put them in order from coldest to warmest, then find the gap between two of them.',
    explore: 'At the computer: the Scratch stage is a number line (x from −240 to 240). Pairs predict and test where a sprite ends up after "change x by 100" and "change x by −250", then build a thermometer program (set temp to 5, repeat 6: change temp by −3, say temp) and predict the last number before clicking the flag.',
    mini: 'Right is bigger. To add, move right; to add a negative, move left (that is what "change by −3" does). Split every jump at 0. a − b is the jump from b to a: 7 − (−3) = 10 because from −3 to 7 is 10 steps right. Check by adding back.',
    share: 'Ben says −8 is bigger than −3 because 8 is bigger than 3. Is he right? Use a thermometer or a lift to explain.',
    exit: { q: 'It is −3 °C. The temperature falls 6 degrees, then rises 4 degrees. What is the temperature now?', a: '−5 °C (−3 − 6 = −9, then −9 + 4 = −5)' },
    mistakes: ['Ordering negatives by their digits only (saying −9 is bigger than −4).', 'Crossing zero wrongly, e.g. 3 − 8 answered as 5 or −11, instead of splitting the jump at 0 (3 down to 0, then 5 more: −5).', 'In code, using "change by 1" when the variable should go down, or counting the start value as one of the repeats when tracing.'],
    extension: 'Make Dot walk along the stage as the temperature changes: inside the loop add "set x to temp × 10" and "if temp < 0 then say Below zero!". Predict where Dot stops before running it.',
    key: [
      ['Q1', '(a) A = −8, B = −3, C = 4  (b) −12, −5, −1, 0, 3, 7  (c) −4 > −9;  −1 < 0;  −15 < 2'],
      ['Q2', '(a) 3 p.m. (−11 °C)  (b) 11 degrees (−24 up to −13)  (c) 9 degrees (−11 down to −20)  (d) −25 °C  (e) 44 degrees (13 up to 0, then 31 more)'],
      ['Q3', '(a) 15 m (6 up to sea level, then 9 more)  (b) 9 m (−6 down to −15)  (c) −13 m (−6 + 4 = −2, then −2 − 11 = −13)'],
      ['Q4', '(a) 3  (b) −7  (c) −8  (d) −8  (e) 8 (from −3 to 5)  (f) 6 (from −7 to −1)'],
      ['Q5', '(a) Table: start 40; 1: 10; 2: −20; 3: −50; 4: −80. The sprite says −80.  (b) 4 more repeats (−80 to −200 is 120, and 120 ÷ 30 = 4)'],
      ['Q6', '(a) 13 (the lift goes up: 5 + 8)  (b) change floor by −1  (c) −3, the third basement (B3)'],
      ['Q7', '(a) set depth to 0; repeat 7; change depth by −4; say depth (7 × 4 = 28)  (b) 28 (change depth by 28 brings the diver back to 0 m)']
    ]
  },

  script: {
    hook: ['Welcome back, inquirers! In Secondary 1 you will meet numbers that go below zero. You already know some: the freezer, a winter holiday in Japan, the basement car park. Today we find out how they behave, and we make the computer go below zero too.', 'Notice it, test it, explain why. Today "test it" means test it in Scratch.'],
    warmIntro: ['Here are five cities at 7 a.m. on a December morning. Put them in order from coldest to warmest. Beijing is −9 and Seoul is −7. Nine is bigger than seven, so which is colder? Argue with your partner.', 'How many degrees warmer is Tokyo than Seoul? How did you count it?'],
    predict: ['Your sprite is at x = 0. It changes x by 100, then changes x by −250. Where will it be? Write your prediction before you test it.', 'The thermometer starts at 5 and goes down 3, six times. What is the last number it will say? Write it down first.'],
    exploreHints: ['Stuck: drag the sprite left and right and watch the x number under the stage. Left of the middle is negative.', 'Wrong prediction: draw a number line on your whiteboard and do the six jumps of 3. Where do you cross 0?', 'Finished early: make the sprite walk with the temperature (set x to temp × 10), or add "if temp < 0 then say Below zero!".'],
    think: ['“It is −4 °C and it rises 9 degrees. Rising means moving right. From −4 it takes 4 to get to 0. I still have 5 of my 9 left, so I land on 5 °C.”', '“Change temp by −4 means I add negative 4. Adding a negative moves me left, so it is the same as taking away 4: 1 + (−4) = 1 − 4 = −3.”', '“7 − (−3) asks how far it is from −3 to 7. From −3 up to 0 is 3, from 0 up to 7 is 7. That is 10 steps right, so the answer is 10. Check: −3 + 10 = 7.”'],
    circulate: ['Ask: “Which way did you move? Where did you cross zero?”', 'Ask: “How can you check your answer by adding back?”', 'Ask: “In your trace table, which row is the start and which rows are the repeats?”'],
    hints: ['Hint 1: “Draw a number line and mark 0 first.”', 'Hint 2: “Split the jump at 0: how far to 0, and how far after it?”', 'Hint 3: “For a − b, start at b and count to a. Right means a positive answer, left means a negative answer.”'],
    talk: ['“Ben says −8 is bigger than −3 because 8 is bigger than 3. Is he right?”', '“Why does change by −3 make a number go down?”'],
    talkAns: 'Ben is not right. −8 is further left on the number line, so it is smaller: −8 °C is colder than −3 °C and floor −8 is lower than floor −3. The digit tells us how far from 0, the sign tells us which side. Change by −3 adds a negative, which moves left, so it is the same as taking away 3.',
    close: ['“Today you went below zero on paper and in code. In Secondary 1 these are called negative numbers or integers, and you already know how to move with them. Well done, inquirers!”']
  },

  deck: {
    today: 'Use a number line to compare, add and subtract negative numbers, and make a variable in code go below zero.',
    warmGame: 'Cold city line-up. Five cities at 7 a.m. on a December morning: Singapore 25 °C, Tokyo 3 °C, Seoul −7 °C, Beijing −9 °C, Harbin −22 °C. Put them in order from coldest to warmest, then find how many degrees warmer Tokyo is than Seoul.',
    warmQs: [['It is 3 °C. It falls 5 degrees. What is it now?', '−2 °C'], ['Which is colder: −7 °C or −2 °C?', '−7 °C'], ['A lift is at B1. It goes down 2 floors. Where is it?', 'B3']],
    expSetup: ['In Scratch, set x to 0: the sprite is in the middle of the stage.', 'Predict, then test: change x by 100, then change x by −250. Where is the sprite?', 'Build the thermometer: set temp to 5, repeat 6: change temp by −3, say temp.', 'Predict the last number it says. Then click the flag and check.'],
    expPic: 'the Scratch stage drawn as a number line from −240 to 240 with a yellow dot at −150, and the thermometer program drawn as coloured blocks (when green flag clicked, set temp to 5, repeat 6, change temp by −3, say temp).',
    expAsk: [['Where did the sprite end up after +100 and then −250?', 'x = −150'], ['What was the last number the thermometer said?', '−13 (2, −1, −4, −7, −10, −13)'], ['How do we make a variable go down in Scratch?', 'Change it by a negative number: adding a negative moves left.']],
    mini1: { head: 'Up and down the line', body: ['It is −4 °C at 6 a.m. It rises 9 degrees by noon, then falls 7 degrees by night.', 'Split each jump at 0: −4 up to 0 is 4, then 5 more; 5 down to 0, then 2 more.', 'What is the temperature at noon, and at night?'], ans: 'Noon 5 °C, night −2 °C.' },
    mini2: { head: 'Subtracting: the jump from b to a', body: ['How much warmer is 7 °C than −3 °C? That is 7 − (−3).', 'Start at −3 and count to 7: 3 up to 0, then 7 more.', 'What is 7 − (−3)?'], ans: '10 (check: −3 + 10 = 7).' },
    keyHead: 'Key idea: move along the number line',
    keyBig: 'Right is bigger. Adding a positive moves right; adding a negative moves left. a − b is the jump from b to a.',
    keySmall: 'In code, “change by −3” makes a variable go down by 3.',
    brk: 'Human lift. Standing tall is floor 0; reach up for each floor up, bend lower for each floor down. Moves: up 3, down 5, down 2, up 6. Call out the floor after each move (3, −2, −4, 2).',
    ws1: 'Page 1, in pairs (paper only): Q1 number line and order, Q2 Harbin temperatures, Q3 sea level.',
    ws2: 'Page 2, on your own: Q4 calculations with negatives, Q5 trace the sprite code, Q6 the lift bug, Q7 plan the diver code.'
  },

  qbank: {
    core: [
      { q: 'On a thermometer, 0 °C is where water freezes. Colder than that, numbers have a minus sign: −3 °C means 3 degrees below zero. Draw a thermometer or number line and write these in order, coldest first: −4, 2, −10, 0, −1.', a: '−10, −4, −1, 0, 2' },
      { q: 'It is −3 °C (3 degrees below zero). The temperature rises by 8 degrees. What is it now? Count up on a thermometer drawing.', a: '5 °C' },
      { q: 'It is 2 °C. The temperature falls by 7 degrees. What is it now? Count down on a thermometer drawing: 2, 1, 0, then below zero.', a: '−5 °C' },
      { q: 'Which is colder, −6 °C or −11 °C? By how many degrees? Mark both on a thermometer drawing.', a: '−11 °C, by 5 degrees' },
      { q: 'In a building the floors are numbered …, −2, −1, 0, 1, 2, … where 0 is the ground floor and −1 is the first floor below it. A lift is at floor −2. It goes up 6 floors. Which floor is it on now? Count the floors one by one.', a: 'Floor 4 (−2 + 6 = 4)' },
      { q: 'In Scratch the stage is a number line. A sprite is at x = 30. It runs “change x by −50” (move 50 steps to the left). Where is it now?', a: 'x = −20' }
    ],
    stretch: [
      { q: 'Work out −7 + 12 and 5 − 13.', a: '5 and −8' },
      { q: 'A diver is at −14 m. A seagull is flying at 9 m. How far apart are they?', a: '23 m (14 up to sea level, then 9 more)' },
      { q: 'Work out 4 − (−6). Hint: how far is it from −6 to 4?', a: '10' },
      { q: 'Find the missing number: −3 + ____ = −10.', a: '−7 (adding −7 moves 7 to the left)' },
      { q: 'At 6 a.m. it was −4 °C. By 2 p.m. it was 7 °C. By 10 p.m. it had fallen 9 degrees. How much did it rise from 6 a.m. to 2 p.m.? What was the temperature at 10 p.m.?', a: 'It rose 11 degrees; at 10 p.m. it was −2 °C (7 − 9).' },
      { q: 'set n to 10, then repeat 5 times: change n by −4. Then say n. What does it say?', a: '−10 (10 − 20)' },
      { q: 'What number is exactly halfway between −9 and 3?', a: '−3 (the gap is 12; −9 + 6 = −3 and 3 − 6 = −3)' },
      { q: 'A submarine is at −120 m. It rises 45 m, then dives 70 m. Where is it now?', a: '−145 m (−120 + 45 = −75, −75 − 70 = −145)' }
    ],
    challenge: [
      { q: 'Put −4, −3, −2, −1, 0, 1, 2, 3, 4 in a 3 by 3 grid so that every row, every column and both diagonals add up to 0.', a: 'One answer: top row −3, 2, 1; middle row 4, 0, −4; bottom row −1, −2, 3. 0 must be in the middle and 4 and −4 cannot be in corners; the other 7 answers are turns and flips of this one.' },
      { q: 'At midnight it was −6 °C. It rose 2 degrees every hour until 7 a.m., then 3 degrees every hour. What was the temperature at 10 a.m.?', a: '17 °C (−6 + 7 × 2 = 8 at 7 a.m., then 8 + 3 × 3 = 17)' },
      { q: 'A sprite starts at x = 200. It runs: repeat until x < −100 [change x by 50, change x by −80]. (It keeps repeating until x is less than −100.) How many repeats does it make, and what is x at the end? Then: if the sprite must end at exactly x = −100 after 8 repeats, what must x start as?', a: '11 repeats, ending at x = −130 (each repeat moves −30: 200 − 30 × 10 = −100 is not yet less than −100, and 200 − 30 × 11 = −130). For 8 repeats the sprite moves 8 × −30 = −240, so x must start at −100 + 240 = 140.' },
      { q: 'Ali says: “When I subtract a negative number, the answer is always bigger than the number I started with.” Test his claim on at least three examples (include −3 − (−4)). Is he always right? Explain with a number line. What happens when you subtract a positive number?', a: 'Yes. Examples: −3 − (−4) = 1 (bigger than −3), 0 − (−4) = 4, 5 − (−4) = 9, −8 − (−4) = −4. Subtracting −4 is the same as adding 4: on the number line it moves 4 to the right, so the answer is 4 more. Subtracting a positive number makes the answer smaller (−3 − 4 = −7).' },
      { q: 'A sprite starts at x = −10. It moves +5, then −3, then +5, then −3, and so on. After how many moves is it first at a number greater than 0? Where is it?', a: 'After 7 moves, at x = 1 (−5, −8, −3, −6, −1, −4, 1).' },
      { q: 'Lift A starts at the surface of a mine (0 m) and goes down 35 m every minute. Lift B starts at −300 m and goes up 25 m every minute. When are they at the same height, and at what height?', a: 'After 5 minutes, at −175 m (the gap of 300 m closes by 60 m each minute).' },
      { q: 'Make up your own temperature story with at least three changes (rises and falls) that starts below zero and ends at exactly −7 °C. Write the story, the working and a number-line sketch. Swap with a partner and check each other’s.', a: 'Open. Example: starts at −2 °C, falls 6 degrees (−8), rises 3 degrees (−5), falls 2 degrees (−7). Check that the story really ends at −7 and that each change is shown on a number line.' },
      { q: 'Two numbers add up to −2. Their difference is 10. What are the two numbers?', a: '4 and −6 (4 + (−6) = −2 and 4 − (−6) = 10)' },
      { q: 'In some Singapore buildings there is no level 0. (Q6 on page 2 uses 0 for the ground floor; here, level 1 is the ground floor and B1 is the level below it.) A lift goes from level 4 down to B3. How many floors does it go down? (Count the levels one by one; do not use a number line with 0.)', a: '6 floors (4, 3, 2, 1, B1, B2, B3: six moves down). A number line with 0 would give 7, because it counts a level 0 that these buildings do not have.' }
    ]
  },

  workbook: H0 => { const H = Object.assign({}, H0, { sub: (l, t, o) => H0.sub(l, typeof t === 'string' ? t.replace(/ {2,}/g, m => '\u00A0'.repeat(m.length)) : t, o) }); return [
    H.q(1, 'The number line. Numbers get bigger to the right.', { before: 40, keepNext: true }),
    H.fig(numline(-10, 10, { h: 70, ly: 36, marks: [[-8, 'A', SKY], [-3, 'B', SKY], [4, 'C', YEL]], label: 'Number line from minus 10 to 10 with points A, B and C' })),
    H.sub('a', 'Write the number at each letter.      A = ______      B = ______      C = ______'),
    H.sub('b', 'Smallest first:   3,  −5,  0,  −1,  −12,  7   →  ______________________'),
    H.sub('c', 'Write < or > in each gap.       −4  ____  −9          −1  ____  0          −15  ____  2'),
    H.q(2, 'On a December trip to Harbin, China, Mei wrote down the temperature.', { keepNext: true }),
    H.tbl([2400, 1500, 1500, 1500, 1500, 1500], [
      H.row(['Time', '6 a.m.', '9 a.m.', '12 noon', '3 p.m.', '9 p.m.'].map((s, i) => H.cell(s, i ? 1500 : 2400, { bold: true, fill: 'D9D9D9', h: 40 }))),
      H.row(['Temperature', '−24 °C', '−19 °C', '−13 °C', '−11 °C', '−20 °C'].map((s, i) => H.cell(s, i ? 1500 : 2400, { bold: !i, h: 40 })))
    ]),
    H.gap(40),
    H.sub('a', 'At which time was it warmest?   ______________'),
    H.sub('b', 'How many degrees did it rise from 6 a.m. to 12 noon?   ______________'),
    H.sub('c', 'How many degrees did it fall from 3 p.m. to 9 p.m.?   ______________'),
    H.sub('d', 'Midnight was 5 degrees colder than 9 p.m. What was the temperature? ______'),
    H.sub('e', 'At noon Singapore was 31 °C. How much warmer was it than Harbin?   ________'),
    H.q(3, 'Heights above sea level are positive. Heights below sea level are negative.', { keepNext: true }),
    H.fig(seaFig()),

    H.q(4, 'Work these out. Draw the jumps on the number line to help you.', { pb: true, before: 0, keepNext: true }),
    H.fig(numline(-12, 12, { h: 42, ly: 12, labEvery: 2, label: 'Blank number line from minus 12 to 12 to draw jumps on' })),
    H.sub('a', '−6 + 9 = ________       (b)  4 − 11 = ________       (c)  −3 − 5 = ________'),
    H.sub('d', '−2 + (−6) = ______     (e)  5 − (−3) = ______      (f)  −1 − (−7) = ______'),
    H.q(5, 'Trace the code. Fill in the table to show x after each repeat.', { keepNext: true }),
    H.fig(traceFig()),
    H.q(6, 'Find the bug. Siti wants the lift to go DOWN 8 floors from floor 5. (0 = ground floor)', { keepNext: true }),
    H.fig(codeQ([[0, 'event', 'when green flag clicked'], [0, 'var', 'set floor to [5]'], [0, 'control', 'repeat [8]'], [1, 'var', 'change floor by [1]'], [1, 'looks', 'say [floor] for [1] seconds']], ['(a) Her code says this floor last:', '(b) Change ONE block so the lift', 'goes down. New block:', '(c) Now the last floor it says is', 'which basement?'], [0, 2, 4], 'Siti\'s code: set floor to 5, repeat 8: change floor by 1, say floor. Questions with answer lines beside it.')),
    H.q(7, 'Plan your code. A diver starts at sea level (0 m) and goes down 4 m at a time to −28 m.', { keepNext: true }),
    H.fig(planFig())
  ]; }
};
