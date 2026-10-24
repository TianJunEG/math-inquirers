const FG = require('../../levels/figs_l4_6.js');
// Math Inquirers P6 — Lesson 4: Algebra Machines (expressions and simple equations; input, rule, output)
// Every answer below was worked out, checked forwards, and every program was traced by hand and run in Python.

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
// code blocks on the left, questions with answer lines on the right (lines: text rows; blanks: row indexes that get an answer line)
const codeQ = (prog, lines, blanks, label) => {
  const b = blocksG(prog, 14, 4, 6); const H2 = Math.max(Math.ceil(b.h) + 6, lines.length * 25 + 12);
  let s = `<svg aria-label="${esc(label)}" viewBox="0 0 600 ${H2}" xmlns="http://www.w3.org/2000/svg" style="width:560px;max-width:100%">${b.g}`;
  lines.forEach((t, i) => { const y = 20 + i * 25; s += `<text x="310" y="${y}" font-size="15" fill="${NAVY}" font-family="Arial">${esc(t)}</text>`; if (blanks.includes(i)) s += `<line x1="${310 + tw(t, 15) * 0.86 + 8}" y1="${y + 2}" x2="596" y2="${y + 2}" stroke="#8A94AD" stroke-width="1.5" stroke-dasharray="3 3"/>`; });
  return s + '</svg>';
};

const PY = 'n = int(input("IN? "))\nout = n * 3 + 2\nprint("OUT:", out)';
const qline = (x, y, t, x2 = 596) => `<text x="${x}" y="${y}" font-size="15" fill="${NAVY}" font-family="Arial">${esc(t)}</text><line x1="${(x + tw(t, 15) * 0.86 + 8).toFixed(0)}" y1="${y + 2}" x2="${x2}" y2="${y + 2}" stroke="#8A94AD" stroke-width="1.5" stroke-dasharray="3 3"/>`;
const qtext = (x, y, t, bold) => `<text x="${x}" y="${y}" font-size="15" ${bold ? 'font-weight="700" ' : ''}fill="${NAVY}" font-family="Arial">${esc(t)}</text>`;

// Q1: three IN/OUT tables with a rule line beside each
const rulesFig = () => {
  const T = [['b', ['1', '2', '3', '4', '10'], ['6', '9', '12', '15', '']], ['c', ['1', '2', '3', '4', ''], ['3', '8', '13', '18', '48']], ['d', ['1', '2', '3', '4', '20'], ['1', '5', '9', '13', '']]];
  let s = `<svg aria-label="Four tables of IN and OUT numbers with gaps, and a line to write each rule" viewBox="0 0 600 218" xmlns="http://www.w3.org/2000/svg" style="width:600px;max-width:100%">`;
  s += `<text x="2" y="22" font-size="15" font-weight="700" fill="${TEAL}" font-family="Arial">(a)</text>` + qtext(28, 22, 'IN 1, 2, 3, 4 give OUT 4, 5, 6, 7.   Rule: OUT = n + ____    OUT for IN 10 = ____', false);
  T.forEach(([l, ins, outs], k) => {
    const y = 30 + k * 62;
    s += `<text x="2" y="${y + 36}" font-size="15" font-weight="700" fill="${TEAL}" font-family="Arial">(${l})</text>`;
    s += traceTable(28, y, ['IN', ...ins], [['OUT', ...outs]], 52, 28);
    s += qline(354, y + 36, 'Rule: OUT =');
  });
  return s + '</svg>';
};
// Q2: two machines with the same steps in a different order
const twoMachines = () => {
  const box = (x, y, t, f) => `<rect x="${x}" y="${y}" width="74" height="34" rx="8" fill="${f}" stroke="${NAVY}" stroke-width="2"/><text x="${x + 37}" y="${y + 23}" font-size="16" font-weight="700" text-anchor="middle" fill="${NAVY}" font-family="Arial">${esc(t)}</text>`;
  const arrow = (x, y) => `<line x1="${x}" y1="${y}" x2="${x + 22}" y2="${y}" stroke="${NAVY}" stroke-width="2.5"/><polygon points="${x + 30},${y} ${x + 20},${y - 6} ${x + 20},${y + 6}" fill="${NAVY}"/>`;
  let s = `<svg aria-label="Machine P: n, add 3, times 4, OUT. Machine Q: n, times 4, add 3, OUT." viewBox="0 0 600 80" xmlns="http://www.w3.org/2000/svg" style="width:560px;max-width:100%">`;
  [['P', '+ 3', '× 4'], ['Q', '× 4', '+ 3']].forEach(([m, a, b], k) => {
    const y = 3 + k * 40;
    s += `<text x="10" y="${y + 24}" font-size="17" font-weight="700" fill="${TEAL}" font-family="Arial">Machine ${m}</text>`;
    s += box(120, y, 'n', YEL) + arrow(198, y + 17) + box(234, y, a, WHITE) + arrow(312, y + 17) + box(348, y, b, WHITE) + arrow(426, y + 17) + box(462, y, 'OUT', SKY);
  });
  return s + '</svg>';
};
// Q4: machine code on the left; questions and the optional Python box on the right
const askFig = () => {
  const b = blocksG([[0, 'event', 'when green flag clicked'], [0, 'looks', 'ask [IN?] and wait'], [0, 'var', 'set out to [(answer * 2) − 7]'], [0, 'looks', 'say [out]']], 14, 4, 6);
  let s = `<svg aria-label="Code: ask IN? and wait, set out to answer times 2 minus 7, say out. Questions and an optional Python box beside it." viewBox="0 0 600 160" xmlns="http://www.w3.org/2000/svg" style="width:600px;max-width:100%">${b.g}`;
  s += qline(300, 16, '(a) You type 10. It says') + qline(300, 38, '(b) You type 3. It says') + qline(300, 60, '(c) To make it say 25, type');
  s += `<rect x="290" y="72" width="306" height="86" rx="10" fill="${SKY}" stroke="${NAVY}" stroke-width="1.5"/><text x="300" y="90" font-size="14" font-weight="700" fill="${TEAL}" font-family="Arial">Know Python? The explore machine:</text>`;
  PY.split('\n').forEach((l, i) => { s += `<text x="300" y="${110 + i * 16}" font-size="14" fill="${NAVY}" font-family="Courier New, monospace" xml:space="preserve">${esc(l)}</text>`; });
  return s + '</svg>';
};
// Q5: loop code on the left; trace table and questions on the right
const loopFig = () => {
  const b = blocksG([[0, 'event', 'when green flag clicked'], [0, 'var', 'set n to [1]'], [0, 'control', 'repeat [4]'], [1, 'looks', 'say [(n * 4) + 1] for [1] seconds'], [1, 'var', 'change n by [1]']], 14, 4, 6);
  let s = `<svg aria-label="Code: set n to 1, repeat 4: say n times 4 plus 1, change n by 1. An empty trace table and questions beside it." viewBox="0 0 600 ${Math.max(Math.ceil(b.h) + 6, 152)}" xmlns="http://www.w3.org/2000/svg" style="width:600px;max-width:100%">${b.g}`;
  s += traceTable(330, 4, ['repeat', 'n', 'it says'], [['1', '1', ''], ['2', '', ''], ['3', '', ''], ['4', '', '']], 80, 20);
  s += qline(300, 124, '(b) The rule: it says') + qline(300, 146, '(c) With repeat 10, the last number is');
  return s + '</svg>';
};

module.exports = {
  lesson: {
    n: 4, week: 2, session: 'B', title: 'Algebra Machines', topic: 'Expressions and Equations',
    objective: 'Find the rule of a function machine from a table and write it with a letter (OUT = 3n + 2); see that the order of the steps matters and use brackets; solve simple equations by running the machine backwards and checking forwards; build an input-rule-output program and use a search loop to test an answer.',
    skills: 'Rule finding from a table, writing expressions with a letter, order of operations and brackets, inverse operations, solving simple equations, tracing loops, explaining a number trick with algebra',
    materials: 'Laptop or desktop with Scratch 3 (scratch.mit.edu, free), mini whiteboard and marker, workbook, pencil. Starter file: L4_Function_Machine.sb3.',
    online: 'Pairs work in breakout rooms for the explore: one partner shares their screen with the machine running and types in the numbers the other partner calls out. Page 1 of the worksheet is done on paper with laptops turned away. Starter file L4_Function_Machine.sb3 (File, Load from your computer; no account needed) has ask IN? and wait, a variable out and say out, with the rule block set to just answer; children change it to the secret rule (the tutor builds the (answer * 3) + 2 version live). Block colours on our slides are simplified; in Scratch, find blocks by the category name on the left, not by colour.',
    warmup: 'Guess my rule: the tutor is a machine. Children call out IN numbers (any number is fine), the tutor says the OUT, and children guess the rule (5n, 2n − 1, 3n + 2: three rounds), then check it on every pair.',
    explore: 'At the computer: the tutor builds a machine in Scratch live for 2 minutes (ask IN? and wait, set out to (answer * 3) + 2, say out). In each pair one child changes it to a secret two-step rule and shares their screen; the partner calls IN numbers and tries to write the rule with n using as few IN numbers as possible. Swapping jobs is the Go further what-if.',
    mini: 'From a table: how much OUT goes up for each 1 that IN goes up gives the × part; then fix the + or − part and check on every pair. Order matters: (n + 2) × 5 is not 5n + 2. To find IN from OUT, run the machine backwards: undo the last step first, then check forwards.',
    share: 'To solve 4n + 7 = 43, Ravi tries n = 1, 2, 3 … like the computer. Mei runs the machine backwards. Which way is better, and when?',
    exit: { q: 'A machine does × 4, then + 5. (a) IN 6: what is OUT? (b) OUT 45: what was IN?', a: '(a) 29  (b) 10 (45 − 5 = 40, 40 ÷ 4 = 10)' },
    mistakes: ['Finding a rule from the first pair only (1 → 6 “add 5”) without checking it on the other pairs.', 'Undoing the steps in the wrong order, or doing the same step again instead of its opposite.', 'Ignoring brackets or the order of operations: reading 4n + 1 as “add 1, then times 4”.'],
    extension: 'Build the search program in Scratch for 8n − 5 = 91. Then change it to look for n × n + n = 90, which has no easy backwards step. What does it say? (9)',
    key: [
      ['Q1', '(a) OUT = n + 3; OUT for 10 is 13  (b) OUT for 10 is 33; rule OUT = 3n + 3  (c) IN is 10; rule OUT = 5n − 2  (d) OUT for 20 is 77; rule OUT = 4n − 3'],
      ['Q2', '(a) P gives 32, Q gives 23  (b) P: OUT = (n + 3) × 4;  Q: OUT = 4n + 3  (c) No: (n + 3) × 4 = 4n + 12, so P is always 9 more than Q.'],
      ['Q3', '(a) n = 8 (43 + 5 = 48, 48 ÷ 6 = 8)  (b) n = 10 (74 − 4 = 70, 70 ÷ 7)  (c) n = 12 (45 ÷ 5 = 9, 9 + 3)  (d) n = 24 (15 − 9 = 6, 6 × 4)'],
      ['Q4', '(a) 13  (b) −1  (c) 16 (25 + 7 = 32, 32 ÷ 2 = 16)'],
      ['Q5', '(a) Table: n = 1, 2, 3, 4; it says 5, 9, 13, 17  (b) 4n + 1  (c) 41'],
      ['Q6', '(a) set n to 0; repeat until (n * 8) − 5 = 91; change n by 1  (b) 12  (c) 91 + 5 = 96, 96 ÷ 8 = 12 ✓'],
      ['Q7', '(a) 7 gives 3; 10 gives 3  (b) n + 5, 2n + 10, 2n + 6, n + 3, 3  (c) Halving 2n + 6 gives n + 3; taking away n leaves 3, whatever n is.']
    ]
  },

  script: {
    hook: ['Today you are machine builders and machine breakers. Every machine has a secret rule. In Secondary 1 the rule is written with a letter, like 3n + 2, and that is all algebra is: a machine written down.', 'Notice it, test it, explain why. Today we test our rules in code.'],
    warmIntro: ['I am a machine. Call out a number and I will tell you what comes out. You say 3, I say 8. You say 7, I say 12. What is my rule?', 'Which numbers did you choose to call out? Which ones helped you most?'],
    predict: ['My machine does times 3, then add 2. If you type 4, what will it say? Write your prediction before we run the code.', 'If I swap the steps, add 2 first and then times 3, will 4 give the same answer? Thumbs up or down.'],
    exploreHints: ['Stuck building: put the * block inside the + block, then put “answer” in the first gap of the *.', 'Stuck cracking a rule: ask for IN 0, 1, 2, 3. How much does OUT go up each time?', 'Finished early: swap jobs (the Go further what-if), make a three-step machine, or put ask and say in a forever loop.'],
    think: ['“IN goes up by 1 and OUT goes up by 4 each time. That is what times 4 does. 4 × 1 is 4 but OUT is 7, so I add 3. Rule: 4n + 3. Check: 4 × 4 + 3 = 19.”', '“Machine A adds 2 then times 5; machine B times 5 then adds 2. For 4: (4 + 2) × 5 = 30 and 4 × 5 + 2 = 22. Same steps, different order, different answer. The brackets show what happens first.”', '“5n − 4 = 31. The machine did times 5, then take away 4. I undo the last step first: 31 + 4 = 35. Then undo times 5: 35 ÷ 5 = 7. Check: 7 × 5 − 4 = 31.”'],
    circulate: ['Ask: “Did you check your rule on every pair, not just the first?”', 'Ask: “What was the last step? What is its opposite?”', 'Ask: “How could the computer check your answer?”'],
    hints: ['Hint 1: “How much does OUT go up when IN goes up by 1? That is the × part.”', 'Hint 2: “Draw the machine boxes. Write the OUT at the end and go backwards.”', 'Hint 3: “Put your answer back into the machine. Do you get the OUT?”'],
    talk: ['“To solve 4n + 7 = 43, Ravi tries n = 1, 2, 3 … like the computer. Mei runs the machine backwards. Which way is better, and when?”'],
    talkNext: '“Why do we undo the LAST step first?” (Only if flex is left; otherwise it is the opener of the next lesson.)',
    talkAns: 'Both give n = 9. Running backwards is quicker by hand and works for big numbers. Trying every n is easy to code and also works when there is no easy backwards step (like n × n + n = 90), but it is slow by hand and must stop if there is no whole-number answer. We undo the last step first because it was the last thing done, like taking off shoes before socks.',
    close: ['“Today you wrote rules with a letter, ran machines backwards and let the computer search. That is the start of Secondary 1 algebra, and you explained it in your own words. Well done, inquirers!”']
  },

  deck: {
    today: 'Find a machine’s rule and write it with a letter, run machines backwards to solve equations, and build a machine in code.',
    warmGame: 'Guess my rule. The tutor is a machine with a secret rule. Call out IN numbers, hear the OUT, and guess the rule. Three rounds: 5n, 2n − 1, 3n + 2. Check each rule on every pair.',
    warmQs: [['n = 6. What is 4n?', '24'], ['n = 6. What is 3n − 5?', '13'], ['2n = 18. What is n?', '9']],
    expSetup: ['Watch the tutor build the machine in Scratch: ask IN? and wait, set out to (answer * 3) + 2, say out.', 'Change the rule to your own secret two-step rule. One partner shares their screen.', 'The other partner calls IN numbers and writes the rule with n, using as few IN numbers as possible.'],
    expPic: 'a machine drawn as boxes (IN → × 3 → + 2 → OUT) above the Scratch program drawn as coloured blocks (when green flag clicked, ask IN? and wait, set out to (answer * 3) + 2, say out).',
    expAsk: [['How did you write the rule with n?', 'The × part first, then the + or − part, e.g. 3n + 2.'], ['The machine × 3, + 2 says 20. How can you find IN without guessing?', 'Run it backwards: 20 − 2 = 18, 18 ÷ 3 = 6.']],
    mini1: { head: 'From a table to a rule', body: ['IN 1, 2, 3, 4 gives OUT 7, 11, 15, 19.', 'OUT goes up 4 each time, so × 4. 4 × 1 = 4, but OUT is 7, so + 3.', 'What is the rule? Check it on IN 4.'], ans: 'OUT = 4n + 3 (4 × 4 + 3 = 19).' },
    mini2: { head: 'Run the machine backwards', body: ['A machine does × 5, then − 4. OUT is 31. That is 5n − 4 = 31.', 'Undo the last step first: 31 + 4 = 35. Then undo × 5: 35 ÷ 5.', 'What is n? Check forwards.'], ans: 'n = 7 (7 × 5 − 4 = 31).' },
    keyHead: 'Key idea: a rule is a machine',
    keyBig: 'OUT = 3n + 2 means × 3, then + 2. To find IN from OUT, run the machine backwards: undo the last step first.',
    keySmall: 'Check every answer by running the machine forwards.',
    brk: 'Jumping machine. Rule: double it, then take away 1. The tutor calls IN 2, 3, 4, 5; everyone does that many OUT star jumps (3, 5, 7, 9). Last round: “I did 11 jumps. What was my IN?” (6).',
    ws1: 'Page 1, in pairs (paper only): Q1 guess my rule tables (the first is a one-step warm-up), Q2 two machines in a different order, Q3 run machines backwards.',
    ws2: 'Page 2, on your own: Q4 predict the machine code, Q5 trace a loop, Q6 plan a search, Q7 explain a number trick with n.'
  },

  qbank: {
    core: [
      { q: 'A number machine multiplies IN by 4 and then adds 1. (We write this OUT = 4n + 1.) What comes OUT when 6 goes IN? Try 2 and 3 first.', a: '25 (6 × 4 = 24, then + 1)' },
      { q: 'A machine changes IN 1, 2, 3, 4 into OUT 3, 5, 7, 9. Look at how OUT goes up each time. What does the machine do? What will come OUT when 10 goes IN?', a: 'It doubles IN and then adds 1 (OUT = 2n + 1). IN 10 gives 21.' },
      { q: 'I think of a number and multiply it by 3. I get 54. What was my number? (Guess and check, or share 54 into 3 equal groups.)', a: '18' },
      { q: 'A machine multiplies by 6, then takes away 4. OUT is 38. What was IN? Try some numbers, or undo the steps.', a: '7 (38 + 4 = 42, 42 ÷ 6 = 7)' },
      { q: 'Ali has some stickers. Mei has 5 more than Ali. Fill in the table: if Ali has 3 stickers, Mei has __ and they have __ altogether. If Ali has 7, they have __ altogether. If Ali has 10, they have __. What do you notice about how the total changes?', a: 'Ali 3: Mei 8, total 11. Ali 7: Mei 12, total 19. Ali 10: Mei 15, total 25. Each extra sticker Ali has adds 2 to the total (one for Ali and one for Mei).' },
      { q: 'A Scratch machine runs three blocks. “ask for IN” waits for you to type a number, and Scratch calls what you typed “answer”. “set out to (answer * 3) + 4” makes out equal to answer times 3, plus 4 (* means ×). “say out” shows out. You type 7. What does it say?', a: '25' }
    ],
    stretch: [
      { q: 'IN 1, 2, 3, 4 gives OUT 1, 7, 13, 19. Find the rule. What is OUT when IN is 20?', a: 'OUT = 6n − 5; IN 20 gives 115.' },
      { q: 'Solve 9n − 7 = 65.', a: 'n = 8 (65 + 7 = 72, 72 ÷ 9 = 8)' },
      { q: 'Machine A does × 2, then + 10. Machine B does + 5, then × 2. Put 7 into both. What do you notice? Explain with n.', fig: (() => { const { T, R, L, SKY, Y, N } = FG; let g = ''; const strip = (y, ops, tag) => { let x = 20; g += T(x, y + 30, tag, { size: 18, anchor: 'start', fill: FG.TEAL }); x = 110; g += R(x, y + 8, 56, 40, { fill: Y, w: 3, rx: 6 }) + T(x + 28, y + 35, 'IN', { size: 19 }); x += 56; ops.forEach(o => { g += L(x, y + 28, x + 26, y + 28, { w: 3 }) + `<polygon points="${x + 34},${y + 28} ${x + 24},${y + 22} ${x + 24},${y + 34}" fill="${N}"/>`; x += 34; g += R(x, y + 8, 76, 40, { fill: SKY, w: 3, rx: 6 }) + T(x + 38, y + 35, o, { size: 20 }); x += 76; }); g += L(x, y + 28, x + 26, y + 28, { w: 3 }) + `<polygon points="${x + 34},${y + 28} ${x + 24},${y + 22} ${x + 24},${y + 34}" fill="${N}"/>`; x += 34; g += R(x, y + 8, 64, 40, { fill: '#fff', w: 3, rx: 6 }) + T(x + 32, y + 35, 'OUT', { size: 19 }); }; strip(0, ['× 2', '+ 10'], 'Machine A'); strip(64, ['+ 5', '× 2'], 'Machine B'); return FG.svg(600, 124, g, 'Two number machines. Machine A: IN, times 2, then plus 10, OUT. Machine B: IN, plus 5, then times 2, OUT.'); })(), a: 'Both give 24. (n + 5) × 2 = 2n + 10, so they always give the same OUT.' },
      { q: 'I think of a number, divide it by 4, then add 6. I get 15. What is my number?', a: '36 (15 − 6 = 9, 9 × 4 = 36)' },
      { q: 'IN 3 gives OUT 11. IN 7 gives OUT 23. The rule is “× a number, then + a number”. Find it.', a: 'OUT = 3n + 2 (IN up 4, OUT up 12, so × 3; 9 + 2 = 11)' },
      { q: 'set n to 2, then repeat 3 times: set n to (n × 2) + 1. Then say n. What does it say?', a: '23 (2 → 5 → 11 → 23)' },
      { q: 'Solve (n + 6) × 4 = 60.', a: 'n = 9 (60 ÷ 4 = 15, 15 − 6 = 9)' },
      { q: 'A taxi charges $4 to start, plus $2 for every km. Write the cost in dollars for n km. How far can you go for $30?', a: '2n + 4 dollars; 13 km (30 − 4 = 26, 26 ÷ 2 = 13)' }
    ],
    challenge: [
      { q: 'A machine does × 3, then − 4. Which IN number comes out as the SAME number?', a: '2 (2 × 3 − 4 = 2; 3n − 4 = n)' },
      { q: 'Two machines are joined: the OUT of the first goes into the second. Each one does × 2, then + 1. IN 5 gives OUT 23. Which IN gives OUT 63?', a: '15 (63 → 31 → 15; check 15 → 31 → 63)' },
      { q: 'Three numbers in a row add up to 87. Call the smallest n. Write the sum with n and find the numbers.', a: 'n + (n + 1) + (n + 2) = 3n + 3 = 87, so n = 28: the numbers are 28, 29, 30.' },
      { q: 'set n to 0, then repeat until (n × 7) + 3 > 100: change n by 1. Then say n. What does it say?', a: '14 (13 gives 94, 14 gives 101)' },
      { q: 'Machine M does × 5, then − 3. Machine N does × 2, then + 15. Which IN gives the same OUT on both machines? What is that OUT?', a: 'IN 6, OUT 27 (5n − 3 = 2n + 15, so 3n = 18)' },
      { q: 'Which is bigger, 3n + 5 or 3(n + 2)? Does it depend on n?', a: '3(n + 2) = 3n + 6 is always 1 bigger; it does not depend on n.' },
      { q: 'Find two different machines of the form “× a number, then + or − a number” that both turn IN 5 into OUT 18. Then find the machine of this form that ALSO turns IN 2 into OUT 6. Is there only one?', a: 'Many machines turn 5 into 18: × 3 then + 3, × 2 then + 8, × 1 then + 13, × 4 then − 2, … Only × 4 then − 2 also turns 2 into 6 (4 × 2 − 2 = 6). Two pairs of IN and OUT fix the rule: 5a + b = 18 and 2a + b = 6 give 3a = 12, so a = 4 and b = −2.' },
      { q: 'Mei is n years old. Her mother is 3 times as old. In 12 years, her mother will be twice as old as Mei. How old is Mei now? (The bars are not drawn to scale.)', fig: FG.barModel({ left: 200, right: 20, rowH: 34, rows: [{ name: 'Mei now', segs: [{ u: 1 }] }, { name: 'Mother now', segs: [{ u: 1 }, { u: 1 }, { u: 1 }] }, { name: 'Mei in 12 years', segs: [{ u: 1 }, { u: 1.5, f: 'shade', t: '+ 12' }] }, { name: 'Mother in 12 years', segs: [{ u: 1 }, { u: 1 }, { u: 1 }, { u: 1.5, f: 'shade', t: '+ 12' }] }], label: 'Not to scale. Bars for the ages now (Mei 1 part, her mother 3 parts) and in 12 years (each bar has a shaded extra part for 12 years).' }), a: '12 (3n + 12 = 2(n + 12), so n = 12; mother 36; in 12 years 24 and 48)' },
      { q: 'Ali’s secret machine does × a number, then + or − a number. IN 4 gives OUT 9. IN 9 gives OUT 24. What does IN 20 give? Which IN gives OUT 99?', a: 'The rule is 3n − 3. IN 20 gives 57. OUT 99 comes from IN 34.' }
    ]
  },

  workbook: H0 => { const H = Object.assign({}, H0, { sub: (l, t, o) => H0.sub(l, typeof t === 'string' ? t.replace(/ {2,}/g, m => '\u00A0'.repeat(m.length)) : t, o) }); return [
    H.q(1, 'Guess my rule. Fill in the gaps. Write each rule with n.', { before: 10, keepNext: true }),
    H.fig(rulesFig()),
    H.q(2, 'Two machines use the same steps in a different order.', { keepNext: true }),
    H.fig(twoMachines()),
    H.sub('a', 'Put in 5.     Machine P gives __________     Machine Q gives __________'),
    H.sub('b', 'Write each rule with n.    P:  OUT = __________    Q:  OUT = __________'),
    H.sub('c', 'Can P and Q ever give the same OUT for the same IN? Explain.  ______________________________'),
    H.q(3, 'Run each machine backwards to find n. Then check by going forwards.', { keepNext: true }),
    H.sub('a', 'n → × 6 → − 5 → 43             n = ________     Check: ________________'),
    H.sub('b', '7n + 4 = 74                              n = ________     Check: ________________'),
    H.sub('c', '(n − 3) × 5 = 45                        n = ________     Check: ________________'),
    H.sub('d', 'n ÷ 4 + 9 = 15                           n = ________     Check: ________________'),

    H.q(4, 'Predict what the code says. (In Scratch, * means ×.)', { pb: true, before: 0, keepNext: true }),
    H.fig(askFig()),
    H.q(5, 'Trace the code. Fill in the table.', { keepNext: true }),
    H.fig(loopFig()),
    H.q(6, 'Plan a search. Find n when 8n − 5 = 91 by trying n = 0, 1, 2, 3 …', { keepNext: true }),
    H.fig(codeQ([[0, 'var', 'set n to [    ]'], [0, 'control', 'repeat until [(n * 8) − 5 = ___]'], [1, 'var', 'change n by [    ]'], [0, 'looks', 'say [n]']], ['(a) Fill in the three blanks.', '(b) What will it say?', '(c) Check by running the machine', 'backwards:'], [1, 3], 'Search plan with blanks: set n to blank, repeat until n times 8 minus 5 equals blank, change n by blank, say n. Questions beside it.')),
    H.q(7, '★ Take-home. The number trick. Think of a number. Add 5. Double it. Take away 4. Halve it. Take away the number you first thought of.', { keepNext: true }),
    H.sub('a', 'Try it with 7: you get ______.     Try it with 10: you get ______.'),
    H.sub('b', 'Use n:  n → n + 5 → 2n + 10 → _______ → _______ → _______   (the first steps are done for you)'),
    H.sub('c', 'Explain why you always get the same answer.'),
    ...H.lines(1)
  ]; }
};
