// Math Inquirers P6 Post-PSLE Program — Lesson 1: Code the Pattern (sequences and the nth term; loops and a variable)
const N = '#1B2A49', Y = '#FFC93C', SKY = '#DDEBF7', TEAL = '#1F7A6F', RED = '#D64545', WH = '#FFFFFF';
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

// Our own code-block drawing (not Scratch artwork). prog: [kind, text, children?, elseChildren?]
// kinds: hat (yellow), var (red), look (sky), ctl (teal). "(x)" in the text draws a white value slot.
const BK = { hat: [Y, N], var: [RED, WH], look: [SKY, N], ctl: [TEAL, WH] };
const blocks = (prog, label, fs = 16) => {
  const H = Math.round(fs * 1.9), arm = Math.round(fs * 1.1), bot = Math.round(fs * 0.8), cw = fs * 0.57, pp = fs * 0.42, pad = fs * 0.55, bh = Math.round(fs * 0.55);
  const out = []; let mx = 0;
  const parts = t => t.split(/(\([^)]*\))/).filter(s => s);
  const tw = t => parts(t).reduce((a, s) => a + (s[0] === '(' ? (s.length - 2) * cw + 2 * pp : s.length * cw), 0);
  const text = (t, x, y, fg) => {
    let cx = x + pad, s = '';
    parts(t).forEach(seg => {
      if (seg[0] === '(') {
        const inner = seg.slice(1, -1), w = Math.max(inner.length * cw + 2 * pp, fs * 1.4);
        s += `<rect x="${cx.toFixed(0)}" y="${(y + H * 0.17).toFixed(0)}" width="${w.toFixed(0)}" height="${(H * 0.66).toFixed(0)}" rx="${(H * 0.33).toFixed(0)}" fill="${WH}" stroke="${N}" stroke-width="1.5"/>` +
          `<text x="${(cx + w / 2).toFixed(0)}" y="${(y + H / 2 + fs * 0.35).toFixed(0)}" font-size="${fs}" font-weight="700" text-anchor="middle" fill="${N}" font-family="Arial, sans-serif">${esc(inner)}</text>`;
        cx += w;
      } else {
        s += `<text x="${cx.toFixed(0)}" y="${(y + H / 2 + fs * 0.35).toFixed(0)}" font-size="${fs}" font-weight="700" fill="${fg}" font-family="Arial, sans-serif" xml:space="preserve">${esc(seg)}</text>`;
        cx += seg.length * cw;
      }
    });
    return s;
  };
  const measure = (items, y) => {
    items.forEach(it => {
      if (it[0] === 'hat') y += bh * 1.5 + H;
      else if (it.length > 2) { [it[2]].concat(it.length > 3 ? [it[3]] : []).forEach(ch => { y += H; const c0 = y; y = measure(ch, y); if (y === c0) y += H * 0.6; }); y += bot; }
      else y += H;
    });
    return y;
  };
  const walk = (items, x, y) => {
    items.forEach(it => {
      const k = it[0], t = it[1], [bg, fg] = BK[k]; const w = Math.max(tw(t) + 2 * pad, fs * 4);
      if (k === 'hat') {
        y += bh * 1.5;
        out.push(`<path d="M${x} ${y} C${x + fs * 0.8} ${y - bh * 1.9} ${x + fs * 3.2} ${y - bh * 1.9} ${x + fs * 4} ${y} L${x + w} ${y} Q${x + w + 6} ${y} ${x + w + 6} ${y + 6} L${x + w + 6} ${y + H - 6} Q${x + w + 6} ${y + H} ${x + w} ${y + H} L${x + 6} ${y + H} Q${x} ${y + H} ${x} ${y + H - 6} Z" fill="${bg}" stroke="${N}" stroke-width="2" stroke-linejoin="round"/>`);
        out.push(text(t, x, y, fg)); mx = Math.max(mx, x + w + 6); y += H; return;
      }
      if (it.length > 2) {
        const arms = [it[2]].concat(it.length > 3 ? [it[3]] : []), labels = [t, 'else'];
        const segs = []; let yy = y;
        arms.forEach(ch => { const top = yy; yy += H; const c0 = yy; yy = measure(ch, yy); if (yy === c0) yy += H * 0.6; segs.push([top, c0, yy]); });
        const endy = yy + bot, bw = fs * 3.4;
        let d = `M${x + 6} ${y} L${x + w - 6} ${y} Q${x + w} ${y} ${x + w} ${y + 6} L${x + w} ${y + H - 6} Q${x + w} ${y + H} ${x + w - 6} ${y + H} L${x + arm} ${y + H} `;
        segs.forEach(([top, c0, c1], i) => {
          if (i > 0) { const wl = Math.max(tw(labels[i]) + 2 * pad, fs * 4); d += `L${x + arm} ${top} L${x + wl} ${top} L${x + wl} ${top + H} L${x + arm} ${top + H} `; }
          d += `L${x + arm} ${c1} `;
        });
        d += `L${x + bw} ${segs[segs.length - 1][2]} L${x + bw} ${endy - 5} Q${x + bw} ${endy} ${x + bw - 5} ${endy} L${x + 6} ${endy} Q${x} ${endy} ${x} ${endy - 6} L${x} ${y + 6} Q${x} ${y} ${x + 6} ${y} Z`;
        out.push(`<path d="${d}" fill="${bg}" stroke="${N}" stroke-width="2" stroke-linejoin="round"/>`);
        out.push(text(t, x, y, fg)); mx = Math.max(mx, x + w);
        segs.forEach(([top, c0], i) => { if (i > 0) out.push(text(labels[i], x, top, fg)); walk(arms[i], x + arm, c0); });
        y = endy;
      } else {
        out.push(`<rect x="${x}" y="${y}" width="${w.toFixed(0)}" height="${H}" rx="7" fill="${bg}" stroke="${N}" stroke-width="2"/>`);
        out.push(text(t, x, y, fg)); mx = Math.max(mx, x + w); y += H;
      }
    });
    return y;
  };
  const yend = walk(prog, 2, 2), W = Math.ceil(mx + 4), Ht = Math.ceil(yend + 4);
  return `<svg aria-label="${esc(label)}" viewBox="0 0 ${W} ${Ht}" width="${W}" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;vertical-align:top">${out.join('')}</svg>`;
};

// matchstick squares in a row: patterns 1, 2, 3
const sticksSvg = () => {
  const s = 46, gap = 70, ws = [1, 2, 3].map(k => k * s); const tot = ws.reduce((a, b) => a + b, 0) + 2 * gap;
  let x = (600 - tot) / 2, g = '';
  const stick = (x1, y1, x2, y2) => {
    const dx = x2 - x1, dy = y2 - y1, L = Math.hypot(dx, dy), ux = dx / L, uy = dy / L;
    const a = [x1 + ux * 5, y1 + uy * 5], b = [x2 - ux * 5, y2 - uy * 5];
    return `<line x1="${a[0]}" y1="${a[1]}" x2="${b[0]}" y2="${b[1]}" stroke="${N}" stroke-width="5" stroke-linecap="round"/><circle cx="${b[0]}" cy="${b[1]}" r="4.5" fill="${RED}"/>`;
  };
  [1, 2, 3].forEach((k, i) => {
    const top = 20, bot = 20 + s;
    for (let j = 0; j < k; j++) { const x0 = x + j * s; g += stick(x0, top, x0 + s, top) + stick(x0, bot, x0 + s, bot); }
    for (let j = 0; j <= k; j++) { const x0 = x + j * s; g += stick(x0, bot, x0, top); }
    g += `<text x="${x + ws[i] / 2}" y="${bot + 34}" font-size="17" font-weight="700" text-anchor="middle" fill="${TEAL}" font-family="Fredoka, Arial, sans-serif">Pattern ${k}</text>`;
    x += ws[i] + gap;
  });
  return `<svg aria-label="Matchstick squares: patterns 1, 2 and 3" viewBox="0 0 600 112" width="440" xmlns="http://www.w3.org/2000/svg" style="max-width:100%">${g}</svg>`;
};

const pyBox = (H, title, code, note) => H.p([`<div style="border:2px solid ${N};border-radius:12px;background:#FFF4D1;padding:6px 14px;margin-left:40px;display:flex;gap:16px;align-items:center"><pre style="flex:none;margin:2px 0;font-family:'Courier New',monospace;font-size:14px;line-height:1.3;white-space:pre">${esc(code)}</pre><div><div style="font-weight:700;color:${TEAL};font-size:15px">${esc(title)}</div><div style="font-size:14px;color:#3B4A6B">${esc(note)}</div></div></div>`], { after: 0 });

module.exports = {
  lesson: {
    n: 1, week: 1, session: 'A', title: 'Code the Pattern', topic: 'Sequences and the nth Term',
    objective: 'Continue a sequence, find the rule for the nth term of a sequence with a constant difference, use it to find far terms such as the 100th, work backwards to decide whether a number is in a sequence, and test predictions with a loop and a variable in Scratch.',
    skills: 'Pattern spotting, generalising with a letter, predicting, testing in code, debugging (counting the jumps)',
    materials: 'Laptop or desktop with Scratch 3 open (scratch.mit.edu, no account needed), about 25 matchsticks or toothpicks per child (or squared paper), mini whiteboard, workbook. Optional: a Python editor for children who already know Python.',
    online: 'The tutor shares the slides and a Scratch window. Share your Scratch window and build the four blocks together on screen; the blocks are also on the slide. Block colours on our slides are simplified; in Scratch, find blocks by the category name on the left, not by colour. Scratch is free at scratch.mit.edu and needs no account in class. Children hold paper up to the camera or share their screen when asked. Matchsticks can be drawn as lines.',
    warmup: 'Next! Pattern quick-fire: six sequence cards (add, take away, square numbers, doubling, Fibonacci, decimals). Teams race to give the next two terms; a bonus point for the rule.',
    explore: 'Pairs build matchstick triangles in a row (3, 5, 7 sticks), make a table, predict the sticks for pattern 10 and pattern 100 without building them, then check pattern 10 with a loop and a variable in Scratch.',
    mini: 'Term-to-term rule (add 3) versus the rule for the nth term (3n + 2): the difference tells you the times table, then compare to find what to add or take away. Find the 100th term. Test it in code: set term to the 1st term, repeat 99, change term by 3, say term. The 100th term is only 99 jumps from the 1st. Before page 1: work backwards to decide whether a number is in a sequence. Before page 2: trace a loop in a table, plan a program (say first, then change) and find a jump-count bug.',
    share: 'Ali says the 100th term of 7, 10, 13, … is 7 + 3 × 100 = 307. Is he right? Explain with a rule, a picture or code.',
    exit: { q: 'The sequence 8, 11, 14, 17, … (a) Write the rule for the nth term. (b) Find the 100th term. (c) A loop starts at the 1st term. How many times must it repeat "change by 3" to reach the 100th term?', a: '(a) 3n + 5  (b) 305  (c) 99 times' },
    mistakes: [
      'Using only the difference as the rule (writing 3n for 5, 8, 11, …) and not comparing with the 1st term.',
      'Off by one: doing 100 jumps from the 1st term (5 + 3 × 100) instead of 99, in the maths and in the repeat block.',
      'Putting "change" before "say" in a loop, so the sprite never says the 1st term.'
    ],
    extension: 'Make the program say the position and the term together (for example "term 7 is 23") using a second variable pos and the join block. Then make it stop at the first term bigger than 1000.',
    key: [
      ['Q1', '(a) 4, 7, 10, 13, 16, 19. Each new square adds 3 sticks, not 4, because it shares one side with the square before it.  (b) sticks = 3 × n + 1  (c) 301  (d) Pattern 20 (3 × 20 + 1 = 61)'],
      ['Q2', '(a) difference 4; 4n + 2; 402  (b) 5; 5n − 4; 496  (c) 2; 2n + 7; 207  (d) 0.5; 0.5n (or n ÷ 2); 50'],
      ['Q3', '(a) 4n + 1  (b) Yes. 101 − 1 = 100 = 4 × 25, so 101 is the 25th term.  (c) No. Every term is 1 more than a multiple of 4, so every term is odd; 150 is even. (150 − 1 = 149 is not a multiple of 4.)'],
      ['Q4', 'Trace: x is 7, 12, 17, 22.  (a) 22  (b) 502. x starts at 2 and 100 jumps of 5 add 500.'],
      ['Q5', 'Program: when green flag clicked; set n to 4; repeat 20 [say n for 1 seconds; change n by 6]. Say must come before change (or start n at −2 and change first).  (a) 118 (the 20th term: 6 × 20 − 2), the last number it says. It says one term per second.'],
      ['Q6', '(a) 203 (3 + 50 × 4)  (b) 199 (4 × 50 − 1)  (c) Change repeat 50 to repeat 49. The 1st term is already there before the loop starts, so the 50th term is only 49 jumps away.']
    ]
  },

  script: {
    hook: ['Welcome to Math Inquirers P6! The PSLE is done, so there is no exam today: just puzzles, patterns and code.', 'Every lesson we notice a pattern, test it in code, and explain why. Today’s question: how can you find the 100th number in a pattern without writing out all 100?'],
    warmIntro: ['Teams of two. I will show a sequence card. The first team to say the next two terms gets a point, and a bonus point if you can say the rule.', 'Careful: not every card adds the same amount each time.'],
    predict: ['Pattern 1 is a triangle made of 3 matchsticks. Each new pattern adds one more triangle in the row. Before you build anything: how many sticks will pattern 100 need? Write your guess in the corner of your whiteboard.'],
    exploreHints: ['Stuck building: lay the triangles point up, point down, point up, so each new triangle shares a stick.', 'Stuck on pattern 100: “How many sticks does each new triangle add? How many new triangles come after the first one?”', 'Finished early: in Scratch, set sticks to 3, repeat 9, change sticks by 2, say sticks. Does it match your pattern 10? Now change it to reach pattern 100.'],
    think: [
      '“5, 8, 11, 14. The term-to-term rule is add 3. That is great for the next term, but slow for the 100th: I would have to add 3 ninety-nine times.”',
      '“Adding 3 each time is like the 3 times table: 3, 6, 9, 12. Each term is 2 more than the times-table number. So the nth term is 3 × n + 2, which we write 3n + 2. Check the 4th term: 3 × 4 + 2 = 14. Yes.”',
      '“So the 100th term is 3 × 100 + 2 = 302. Now I test it in code. I set term to 5, the 1st term. From the 1st term to the 100th term there are 99 jumps, so repeat 99, change term by 3, then say term. It says 302. The maths and the code agree.”'
    ],
    circulate: ['Ask: “What is the difference? Which times table is it like?”', 'Ask: “Check your rule with the 1st term AND the 4th term. Does it work for both?”', 'Ask: “How many jumps are there from the 1st term to the 20th term?”'],
    hints: ['Hint 1: “Write the times table of the difference under the sequence.”', 'Hint 2: “How far is each term from the times-table number under it?”', 'Hint 3: “Count the jumps for a small case first: from the 1st term to the 4th term is 3 jumps.”'],
    talk: ['“Ali says the 100th term of 7, 10, 13, … is 7 + 3 × 100 = 307. Is he right?”', '“When is the nth-term rule better than adding on? When is code better than both?”'],
    talkAns: 'No. The 1st term is already 7 before any jump, so the 100th term is only 99 jumps away: 7 + 3 × 99 = 304. The rule 3n + 4 gives 304 too. The rule is fastest for one far term; code is best for listing many terms or checking an answer.',
    close: ['“Today you found the 100th term without writing 100 numbers, and you tested it in code. That is what mathematicians and programmers both do.”', '“Do the exit ticket on your own, then show me.”']
  },

  deck: {
    today: 'Find the rule for the nth term of a pattern, predict the 100th term, and test it with a loop in code.',
    warmGame: 'Next! Pattern quick-fire. Six sequence cards. Teams race to say the next two terms; a bonus point for the rule.',
    warmQs: [['4, 9, 14, 19, __', '24'], ['The 10th term of 2, 4, 6, 8, …', '20'], ['The 10th term of 3, 5, 7, 9, …', '21'], ['Ali has $12 and saves $5 a week. How much does he have after 6 weeks?', '$42'], ['100, 93, 86, __', '79']],
    expSetup: ['Build matchstick triangles in a row: pattern 1 has 1 triangle, pattern 2 has 2, pattern 3 has 3.', 'Count the sticks in each pattern. Make a table.', 'Predict the sticks in pattern 10 and in pattern 100. Do not build them!', 'Check pattern 10 in Scratch with a loop and a variable.'],
    expPic: 'three rows of matchstick triangles (3, 5 and 7 sticks) and a small table with question marks for pattern 10 and pattern 100.',
    expAsk: [['How many sticks are in pattern 10?', '21'], ['How many in pattern 100? How did you get it without building it?', '201. Each new triangle adds 2 sticks: 3 + 2 × 99 = 201, or 2 × 100 + 1.'], ['Which pattern uses exactly 75 sticks?', 'Pattern 37: 2 × 37 + 1 = 75.']],
    mini1: { head: 'The 100th term of 5, 8, 11, 14, …', table: [['n', '1', '2', '3', '4'], ['3 × n', '3', '6', '9', '12'], ['term', '5', '8', '11', '14']], body: ['The difference is 3, so compare with the 3 times table.', 'Each term is 2 more: nth term = 3n + 2.', 'Check the 4th term: 3 × 4 + 2 = 14.'], ans: '3 × 100 + 2 = 302.' },
    mini2: { head: 'Test it in code', body: ['set term to 5 (the 1st term).', 'repeat 99: change term by 3 (99 jumps from the 1st term to the 100th).', 'say term.'], ans: 'It says 302, the same as the rule.' },
    keyHead: 'Key idea: the rule for the nth term',
    keyBig: 'The difference tells you the times table. Compare with it to find what to add or take away.',
    keySmall: 'From the 1st term to the nth term there are n − 1 jumps. Test your rule in code.',
    brk: 'Pattern moves: clap, clap, stomp, clap, clap, stomp … Do 12 moves together. Then predict: what is the 20th move? The 30th?',
    ws1: 'Page 1, in pairs: Q1 matchstick squares, Q2 rules and 100th terms, Q3 is it in the sequence?',
    ws2: 'Page 2, on your own: Q4 trace the code, Q5 plan your code, Q6 spot the bug.'
  },

  qbank: {
    core: [
      { q: 'Write the next two terms: 8, 13, 18, 23, …', a: '28, 33 (add 5)' },
      { q: 'Write the rule for the nth term of 3, 5, 7, 9, …', a: '2n + 1' },
      { q: 'Find the 10th term of 7, 10, 13, 16, …', a: '34 (rule 3n + 4: 3 × 10 + 4)' },
      { q: 'Write the next two terms: 40, 36, 32, 28, …', a: '24, 20 (take away 4)' },
      { q: 'What does this code say?  set n to 10, then repeat 3 [change n by 4], then say n.', a: '22 (10 + 4 + 4 + 4)' },
      { q: 'The rule for the nth term is 4n + 3. Write the first three terms.', a: '7, 11, 15' }
    ],
    stretch: [
      { q: 'Find the 100th term of 12, 19, 26, 33, …', a: '705. The rule is 7n + 5, and 7 × 100 + 5 = 705.' },
      { q: 'Is 200 a term of 2, 9, 16, 23, …? Explain.', a: 'No. The rule is 7n − 5. The 29th term is 198 and the 30th term is 205, so 200 is skipped.' },
      { q: 'Matchstick houses in a row: 1 house uses 6 sticks, 2 houses use 11, 3 houses use 16. How many houses can you make with 100 sticks?', a: '19 houses. The rule is 5n + 1: 19 houses use 96 sticks (4 left over) and 20 houses would need 101.' },
      { q: 'What does this code say?  set n to 100, then repeat 8 [change n by −7], then say n.', a: '44 (100 − 8 × 7 = 100 − 56)' },
      { q: 'The 5th term of a sequence is 23 and the 6th term is 27. The difference is always the same. What is the 1st term? What is the rule?', a: '7. Go back 4 jumps of 4: 23 − 16 = 7. The rule is 4n + 3.' },
      { q: 'The 1st term of a sequence is 4 and the 10th term is 40. The difference is always the same. What is the difference?', a: '4. From the 1st term to the 10th term is 9 jumps, and 36 ÷ 9 = 4. (The rule is 4n.)' },
      { q: 'Write a sequence whose 1st term is 10 and whose 100th term is 1000.', a: '10, 20, 30, 40, … (rule 10n). There are 99 jumps, and 990 ÷ 99 = 10.' },
      { q: 'How many terms of 3, 7, 11, 15, … are less than 500?', a: '125. The rule is 4n − 1. The 125th term is 499 and the 126th is 503.' }
    ],
    challenge: [
      { q: 'Pattern 1 is 1 tile, pattern 2 is a 2 by 2 square of tiles, pattern 3 is a 3 by 3 square. How many tiles are in pattern 10? How many more tiles does pattern 11 need than pattern 10?', a: '100 tiles. Pattern 11 has 121 tiles, so 21 more. The differences are 3, 5, 7, 9, …, so this is NOT a constant-difference sequence.' },
      { q: 'A straight fence is 60 m long. There is a post every 4 m, including one at each end. How many posts are there?', a: '16 posts. 60 ÷ 4 = 15 gaps, and there is one more post than gaps.' },
      { q: 'The rule for a sequence is 6n − 4. Ben says every term is even. Is he right? Explain.', a: 'Yes. 6 × n is always even, and an even number take away 4 is even (2, 8, 14, 20, …).' },
      { q: 'Find the first term of 5, 8, 11, 14, … that is bigger than 1000. Which term is it?', a: '1001, the 333rd term. (3n + 2: the 332nd term is 998 and the 333rd is 1001.)' },
      { q: 'A sequence goes 2, 6, 18, 54, … Is the difference the same each time? What is the rule? What is the 7th term?', a: 'No: the differences are 4, 12, 36. Each term is 3 times the one before. The 7th term is 1458 (54, 162, 486, 1458).' },
      { q: 'What does this code say?  set a to 1, set b to 1, then repeat 5 [change a by b, change b by a], then say b.', a: '144. a and b leapfrog: 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 (the Fibonacci numbers).' },
      { q: 'Ben counts 6, 11, 16, 21, … and Mei counts 83, 81, 79, 77, … They say their terms at the same time. When do they say the same number, and what is it?', a: 'At the 12th term they both say 61. The gap starts at 77 and closes by 7 each time (Ben +5, Mei −2): 77 ÷ 7 = 11 jumps after the 1st term. Check: 5 × 12 + 1 = 61 and 85 − 2 × 12 = 61.' },
      { q: 'Which numbers below 60 are in BOTH sequences 2, 5, 8, 11, … and 4, 9, 14, 19, …? Find them all.', a: '14, 29, 44 and 59. One more than each of them is a multiple of both 3 and 5, so a multiple of 15 (15, 30, 45, 60).' },
      { q: 'What does this code say?  set t to 0, set k to 0, then repeat 5 [change k by 1, change t by k], then say t. What would it say with repeat 100?', a: '15 (1 + 2 + 3 + 4 + 5). With repeat 100 it says 5050: pair 1 + 100, 2 + 99, … to make 50 pairs of 101.' }
    ]
  },

  workbook: H => {
    const W = [];
    const hat = ['hat', 'when green flag clicked'];
    const side = (left, wl, right) => H.tbl([wl, 9900 - wl], [H.row([H.cell(['<div style="padding:4px 8px">' + left + '</div>'], wl, { h: 60 }), H.cell(right, 9900 - wl, { h: 60, align: 'left' })])]);
    // Q1 matchstick squares
    W.push(H.q(1, 'Matchstick squares. Each new pattern adds one more square. Fill in the table.', { before: 0, keepNext: true }));
    W.push(H.fig(sticksSvg()));
    { const ws = [2700, 1200, 1200, 1200, 1200, 1200, 1200];
      W.push(H.tbl(ws, [H.row([H.cell('Pattern n', ws[0], { bold: true, fill: 'EDEDED', h: 40 }), ...[1, 2, 3, 4, 5, 6].map(k => H.cell(String(k), 1200, { bold: true, fill: 'EDEDED', h: 40 }))]),
        H.row([H.cell('Sticks', ws[0], { bold: true, h: 70 }), H.cell('4', 1200, { h: 70 }), ...[0, 0, 0, 0, 0].map(() => H.cell('', 1200, { h: 70 }))])])); }
    W.push(H.sub('a', 'Each new square adds ____ sticks. Why not 4? __________________'));
    W.push(H.sub('b', 'Complete the rule:   sticks  =  ______ × n  +  ______'));
    W.push(H.sub('c', 'Pattern 100 has ______ sticks.    (d)  Which pattern has 61 sticks? ____'));
    // Q2 rules
    W.push(H.q(2, 'For each sequence, write the difference, the rule for the nth term and the 100th term.', { keepNext: true }));
    { const ws = [3300, 1900, 2500, 2200];
      W.push(H.tbl(ws, [H.row(['Sequence', 'Difference', 'nth term', '100th term'].map((s, i) => H.cell(s, ws[i], { bold: true, fill: 'D9D9D9', h: 40 }))),
        ...[['a', '6,  10,  14,  18,  …'], ['b', '1,  6,  11,  16,  …'], ['c', '9,  11,  13,  15,  …'], ['d', '0.5,  1,  1.5,  2,  …']].map(([l, s]) =>
          H.row([H.cell(`(${l})   ${s}`, ws[0], { h: 50, align: 'left' }), H.cell('', ws[1]), H.cell('', ws[2]), H.cell('', ws[3])]))])); }
    // Q3 in the sequence?
    W.push(H.q(3, 'Look at the sequence   5,  9,  13,  17,  …', { keepNext: true }));
    W.push(H.sub('a', 'nth term:  __________     (b)  Is 101 a term? Which one?  __________'));
    W.push(H.sub('c', 'Is 150 in the sequence? Explain.  ____________________________'));
    W.push(pyBox(H, 'Python corner (optional): a term tester', 'term = 5\nfor pos in range(1, 101):\n    print(pos, term)\n    term = term + 3',
      'It prints the first 100 terms of 5, 8, 11, … Change the 5 and the 3 to check your answers to Q1 and Q2.'));

    // ---- page 2: code ----
    W.push(H.q(4, 'Predict, then trace. What does this code make the sprite say? Fill in the trace table.', { pb: true, before: 0, keepNext: true }));
    { const tr = H.tbl([2000, 3400], [H.row([H.cell('Loop', 2000, { bold: true, fill: 'EDEDED', h: 40 }), H.cell('x after "change"', 3400, { bold: true, fill: 'EDEDED', h: 40 })]),
        ...[1, 2, 3, 4].map(k => H.row([H.cell(String(k), 2000, { h: 25 }), H.cell('', 3400, { h: 25 })]))]);
      W.push(side(blocks([hat, ['var', 'set x to (2)'], ['ctl', 'repeat (4)', [['var', 'change x by (5)'], ['look', 'say (x) for (1) seconds']]]], 'Code: set x to 2, repeat 4: change x by 5, say x', 14), 4300, [tr, '<div style="text-align:left;padding:8px 4px 0">(a)  The last number it says:  ________</div>'])); }
    W.push(H.sub('b', 'With repeat 100, what is the last number? Explain without running it.'));
    W.push(...H.lines(1));
    // Q5 plan
    W.push(H.q(5, 'Plan your code. Use only these blocks to say the first 20 terms of  4, 10, 16, 22, …  (say … for 1 seconds shows each term in turn; a plain say would only leave the last one on screen.)', { keepNext: true }));
    { const pal = ps => '<div style="display:flex;flex-direction:column;gap:6px;align-items:flex-start">' + ps.map(([p, i]) => blocks(p, 'Block ' + i, 14).replace('max-width:100%', 'flex:none')).join('') + '</div>';
      W.push(side('<div style="display:flex;gap:10px">' + pal([[[hat], 1], [[['var', 'set n to ( )']], 2], [[['var', 'change n by ( )']], 3]]) + pal([[[['ctl', 'repeat ( )', []]], 4], [[['look', 'say (n) for (1) seconds']], 5]]) + '</div>', 4300,
        ['<div style="text-align:left;color:#8A94AD;font-size:14px;padding:0 6px;height:150px">My program:</div>', '<div style="text-align:left;padding:0 6px">(a)  The last number it says:  ________</div>'])); }
    // Q6 bug
    W.push(H.q(6, 'Spot the bug. Mei wants her sprite to say the 50th term of   3,  7,  11,  15,  …   Here is her code.', { keepNext: true }));
    W.push(side(blocks([hat, ['var', 'set n to (3)'], ['ctl', 'repeat (50)', [['var', 'change n by (4)']]], ['look', 'say (n)']], 'Mei’s code: set n to 3, repeat 50: change n by 4, then say n', 14), 4300,
      ['(a)  Her code says:   ________', ' ', '(b)  Use the rule for the nth term.', 'The 50th term is really:   ________']));
    W.push(H.sub('c', 'Fix her code. Explain the bug in one sentence.'));
    W.push(...H.lines(1));
    return W;
  }
};
