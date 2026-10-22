// Math Inquirers P6 Post-PSLE Program — Lesson 2: Prime Hunters (primes, factors, prime factorisation; if, mod and a counter)
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

const pyBox = (H, title, code, note) => H.p([`<div style="border:2px solid ${N};border-radius:12px;background:#FFF4D1;padding:6px 14px;margin-left:40px;display:flex;gap:16px;align-items:center"><pre style="flex:none;margin:2px 0;font-family:'Courier New',monospace;font-size:14px;line-height:1.3;white-space:pre">${esc(code)}</pre><div><div style="font-weight:700;color:${TEAL};font-size:15px">${esc(title)}</div><div style="font-size:14px;color:#3B4A6B">${esc(note)}</div></div></div>`], { after: 0 });
// two factor-tree tops for the workbook: the number, two branches, two empty boxes
const treesSvg = () => {
  let g = '';
  [[150, '72'], [450, '150']].forEach(([cx, v]) => {
    g += `<line x1="${cx}" y1="44" x2="${cx - 70}" y2="98" stroke="${N}" stroke-width="3"/><line x1="${cx}" y1="44" x2="${cx + 70}" y2="98" stroke="${N}" stroke-width="3"/>` +
      `<circle cx="${cx}" cy="28" r="24" fill="${Y}" stroke="${N}" stroke-width="3"/><text x="${cx}" y="35" font-size="19" font-weight="700" text-anchor="middle" fill="${N}" font-family="Fredoka, Arial, sans-serif">${v}</text>` +
      `<rect x="${cx - 100}" y="98" width="60" height="34" rx="8" fill="${WH}" stroke="${N}" stroke-width="2.5"/><rect x="${cx + 40}" y="98" width="60" height="34" rx="8" fill="${WH}" stroke="${N}" stroke-width="2.5"/>`;
  });
  return `<svg aria-label="Factor tree tops for 72 and 150, each splitting into two empty boxes" viewBox="0 0 600 200" width="560" xmlns="http://www.w3.org/2000/svg" style="max-width:100%">${g}</svg>`;
};

module.exports = {
  lesson: {
    n: 2, week: 1, session: 'B', title: 'Prime Hunters', topic: 'Primes, Factors and Prime Factorisation',
    objective: 'Find all the factors of a number using factor pairs, decide whether a number is prime by testing small divisors, write a number as a product of primes with a factor tree, use mod (the remainder), if and a counter in code to count factors, and explore Goldbach pairs and numbers with exactly 3 factors.',
    skills: 'Systematic listing (factor pairs), testing and ruling out, reasoning about when to stop, tracing code, generalising (squares of primes)',
    materials: 'Laptop or desktop with Scratch 3 open, a printed 1 to 100 grid (or squared paper), two coloured pencils, mini whiteboard, workbook. Optional: a Python editor for children who already know Python.',
    online: 'Share the 1 to 100 grid on screen and annotate it while children work on their own printed or hand-drawn grid. Build the prime checker together in your shared Scratch window; the blocks are also on the slide. Block colours on our slides are simplified; in Scratch, find blocks by the category name on the left, not by colour. Children hold their grid up to the camera at minute 22.',
    warmup: 'Factor pair hunt: six number cards (12, 16, 20, 24, 29, 30). With a partner, find every factor pair for each card and explain one pair you found. One card has only one pair: which one, and why? No racing and no points.',
    explore: 'The sieve of Eratosthenes by hand on a 1 to 100 grid: cross out 1, circle 2 and cross out its other multiples, then do the same for 3, 5 and 7. Count the primes and decide why we can stop after 7.',
    mini: 'Factors come in pairs; stop when the pairs meet (36 has 9 factors because 6 × 6 counts once). A prime has exactly 2 factors; 1 is not prime. Test 91: 2, 3 and 5 fail, 7 works (7 × 13), so it is not prime; stop testing once d × d is bigger than the number. Factor trees: 60 = 2 × 2 × 3 × 5 whichever way you split it. Code: n mod d is the remainder; if it is 0, d is a factor; a counter counts the factors; count = 2 means prime. Before page 2: trace a loop with mod, Goldbach pairs (20 = 3 + 17 = 7 + 13), and counting the factors of square numbers.',
    share: 'Why does a square number like 36 have an odd number of factors, when most numbers have an even number?',
    exit: { q: '(a) Is 111 prime? Show your test. (b) Write 66 as a product of primes. (c) Optional: is 133 prime?', a: '(a) No. 1 + 1 + 1 = 3, so 3 divides it: 111 = 3 × 37.  (b) 66 = 2 × 3 × 11  (c) No. 133 = 7 × 19.' },
    mistakes: [
      'Saying 1 is prime, or that 2 is not prime because it is even.',
      'Missing factors by not working in pairs, or counting the middle factor of a square number twice (6 in 36).',
      'Stopping a factor tree at a number that is not prime (72 = 2 × 2 × 18), or reading mod as division (thinking 10 mod 4 is 2.5 instead of the remainder 2).'
    ],
    extension: 'First add if count = 2 then say prime, else say not prime after the loop. Then put the prime checker inside a second loop so n goes 1, 2, 3, … 100 and the sprite says only the primes. Does it find 25 primes, like the sieve?',
    key: [
      ['Q1', '28: 1, 2, 4, 7, 14, 28 (6 factors, not prime).  31: 1, 31 (2, prime).  49: 1, 7, 49 (3, not prime).  51: 1, 3, 17, 51 (4, not prime: 51 = 3 × 17).  1: 1 (1 factor, not prime).  (a) 67, 83 and 97 are prime (57 = 3 × 19, 77 = 7 × 11, 99 = 9 × 11).  (b) No. 8 + 7 = 15, a multiple of 3, so 87 = 3 × 29.'],
      ['Q2', '(a) 72 = 2 × 2 × 2 × 3 × 3  (b) 150 = 2 × 3 × 5 × 5  (c) 126 (2 × 3 × 3 × 7)'],
      ['Q3', 'd = 1 to 6.  6 mod d: 0, 0, 0, 2, 1, 0.  count after each loop: 1, 2, 3, 3, 3, 4.  (a) 4 (the factors 1, 2, 3, 6)  (b) It says 2, so 13 is prime: its only factors are 1 and 13.'],
      ['Q4', '(a) 24 = 5 + 19 = 7 + 17 = 11 + 13 (3 ways)  (b) An odd total needs one even and one odd number. The only even prime is 2, and 27 − 2 = 25 is not prime.'],
      ['Q5', '(a) 4, 9, 25 (three numbers up to 30)  (b) They are squares of primes (2 × 2, 3 × 3, 5 × 5). Their factors are 1, the prime and the square.  (The 36 and the 50 versions are Think harder 4.)'],
      ['Q6', 'E, C, B. Inside B: F (with A inside F), then D. It says 1, 2, 4, 5, 8, 10, 20, 40 (8 numbers, one per second).']
    ]
  },

  script: {
    hook: ['Welcome back, inquirers! Today we hunt primes, the building blocks of every whole number.', 'People have hunted primes for over 2000 years, and today computers hunt them to keep the internet safe. We hunt by hand first, then teach a computer to do it.'],
    warmIntro: ['Factor pair hunt. I show a number. With your partner, find every factor pair: every pair of whole numbers that multiply to make it. Take your time. Be ready to explain one pair you found. There is no race and there are no points.', 'One card is special. See if you can spot which one.'],
    predict: ['How many prime numbers do you think there are from 1 to 100? Write a guess. Then we find out with a 2000-year-old method called the sieve.'],
    exploreHints: ['Stuck: circle 2, then cross out 4, 6, 8, … every 2nd number. Then circle 3 and cross out every 3rd number.', 'Crossing out the same number twice: “That is fine. 6 is a multiple of 2 AND of 3.”', 'Finished early: circle 11 and look for a multiple of 11 below 100 that is not crossed out yet. Is there one? Why not?'],
    think: [
      '“Factors of 36. I work in pairs: 1 × 36, 2 × 18, 3 × 12, 4 × 9, 6 × 6. The next would be 9 × 4, which I already have, so I stop. 9 factors, because 6 only counts once.”',
      '“Is 91 prime? It is not even. 9 + 1 = 10, not a multiple of 3. It does not end in 0 or 5. Try 7: 7 × 13 = 91. So 91 is NOT prime. It looks prime, but it is not.”',
      '“How far do I need to test? 10 × 10 = 100 is bigger than 91, so if 91 had a factor pair, one of the pair would be less than 10. I only test 2, 3, 5 and 7.”',
      '“In code, n mod d is the remainder when n is divided by d. If it is 0, d is a factor, so I change count by 1. At the end, count = 2 means prime.”'
    ],
    circulate: ['Ask: “How do you know you have found every factor?”', 'Ask: “Why can you stop testing at 7 for numbers below 100?”', 'Ask: “Point to the block that adds 1 to count. When does it run?”'],
    hints: ['Hint 1: “Start with 1 × the number, then try 2, 3, 4 … and stop when the pairs meet.”', 'Hint 2: “Use the quick tests: even? digits add to a multiple of 3? ends in 0 or 5? Then try 7.”', 'Hint 3: “Split the number into any two factors you know, then keep splitting until every branch ends in a prime.”'],
    talk: ['“Why does a square number like 36 have an odd number of factors?”', '“Is there a biggest prime? What do you think?”'],
    talkAns: 'Factors come in pairs that multiply to the number. For a square number one pair is a number times itself (6 × 6), and that factor is counted only once, so the total is odd. There is no biggest prime: Euclid showed this about 2300 years ago (a teaser for secondary school).',
    close: ['“You sieved, you tested, you split numbers into primes, and you taught a computer to count factors. Real prime hunters!”', '“Do the exit ticket on your own, then show me.”']
  },

  deck: {
    today: 'Find factors in pairs, test whether a number is prime, split numbers into primes, and teach a computer to count factors with mod.',
    warmGame: 'Factor pair hunt. Six number cards. With a partner, find every factor pair and explain one. One card has only one pair: which one?',
    warmQs: [['17 ÷ 5 = 3 remainder __', '2'], ['30 ÷ 6 = 5 remainder __', '0'], ['23 ÷ 4 = 5 remainder __', '3'], ['100 ÷ 7: what is the remainder?', '2 (7 × 14 = 98)'], ['A remainder of 0 means …?', 'It divides exactly: it is a factor.']],
    expSetup: ['On the 1 to 100 grid, cross out 1. It is not prime.', 'Circle 2. Cross out every other multiple of 2.', 'Circle the next number not crossed out (3) and cross out its multiples. Do the same for 5 and 7.', 'Circle every number left. Count the primes.'],
    expPic: 'the first three rows of a 1 to 100 grid with 2 and 3 circled and the multiples of 2 crossed out.',
    expAsk: [['How many primes are there from 1 to 100?', '25.'], ['Why could we stop after crossing out the multiples of 7?', 'The next prime is 11, and 11 × 11 = 121 is bigger than 100. Every smaller multiple of 11 (22, 33, … 99) has a smaller factor, so it is already crossed out.'], ['Is 1 prime? Is 2 prime?', '1 is not: it has only one factor. 2 is prime (factors 1 and 2), the only even prime.']],
    mini1: { head: 'Is 91 prime?', body: ['Not even; 9 + 1 = 10 is not a multiple of 3; does not end in 0 or 5.', 'Try 7: 91 ÷ 7 = 13.', 'Stop testing once d × d is bigger than the number (10 × 10 = 100).'], ans: 'Not prime: 91 = 7 × 13.' },
    mini2: { head: 'Prime checker in code (n = 15)', body: ['repeat n: if n mod d = 0 then change count by 1; change d by 1.', 'n mod d is the remainder. 0 means d is a factor.', 'At the end, count = 2 means prime.'], ans: 'Factors 1, 3, 5 and 15: count = 4, not 2, so 15 is not prime.' },
    keyHead: 'Key idea: exactly two factors',
    keyBig: 'A prime has exactly 2 factors: 1 and itself. Test 2, 3, 5, 7, … until d × d is bigger than the number.',
    keySmall: 'n mod d gives the remainder. n mod d = 0 means d is a factor of n.',
    brk: 'Prime or not? Jump for prime, squat for not prime: 7, 9, 13, 21, 2, 1, 31, 27, 51, 53.',
    ws1: 'Page 1, in pairs: Q1 factors, primes and prime tests, Q2 factor trees.',
    ws2: 'Page 2, on your own: Q3 trace the factor counter, Q4 Goldbach pairs, Q5 exactly 3 factors, Q6 plan your code.'
  },

  moved: [
    { q: 'Write 36 as the sum of two primes in every way. Then find ALL the numbers from 1 to 50 with exactly 3 factors. What is the next one after 50?', a: '36 = 5 + 31 = 7 + 29 = 13 + 23 = 17 + 19 (4 ways). Exactly 3 factors: 4, 9, 25, 49 (squares of primes). Next after 50: 121 (11 × 11).' }
  ],

  qbank: {
    core: [
      { q: 'List all the factors of 18. Hint: find pairs of numbers that multiply to 18.', a: '1, 2, 3, 6, 9, 18' },
      { q: 'A number is called prime if it has exactly two factors: 1 and itself. For example, 7 is prime (factors 1 and 7) but 8 is not (factors 1, 2, 4, 8). Is 21 prime? Is 23 prime? List the factors of each.', a: '21 is not prime (factors 1, 3, 7, 21). 23 is prime (its only factors are 1 and 23).' },
      { q: '29 sweets are shared equally among 4 children. How many sweets are left over? (In code, the left-over number is written 29 mod 4.)', a: '1 (4 × 7 = 28, so 1 is left over: 29 mod 4 = 1)' },
      { q: 'Write 30 as a multiplication of as many numbers (bigger than 1) as you can. For example, 30 = 5 × 6 uses two numbers. Can you use three? Can you use four?', a: '30 = 2 × 3 × 5 uses three numbers, and you cannot use four: none of 2, 3 and 5 can be split again. (These are the prime factors of 30.)' },
      { q: 'A prime number has exactly two factors. Which of these are prime: 21, 23, 25, 27, 29? Hint: try dividing each by 2, 3 and 5.', a: '23 and 29' },
      { q: 'The primes begin 2, 3, 5, 7, 11, 13, 17, 19. Write 20 as the sum of two of them.', a: '3 + 17 or 7 + 13' }
    ],
    stretch: [
      { q: 'How many factors does 64 have? List them.', a: '7: 1, 2, 4, 8, 16, 32, 64 (8 × 8 counts once).' },
      { q: 'Find the smallest number that has exactly 6 factors.', a: '12 (1, 2, 3, 4, 6, 12). Every number below 12 has fewer than 6 factors.' },
      { q: 'Write 100 as the sum of two primes in every possible way.', a: '6 ways: 3 + 97, 11 + 89, 17 + 83, 29 + 71, 41 + 59, 47 + 53.' },
      { q: 'What does this code say?  set count to 0, set d to 1, then repeat 45 [if 45 mod d = 0 then change count by 1; change d by 1], then say count.', a: '6. It counts the factors of 45: 1, 3, 5, 9, 15, 45.' },
      { q: 'Twin primes differ by 2, like 11 and 13. Find all the twin prime pairs below 50.', a: '6 pairs: 3 and 5, 5 and 7, 11 and 13, 17 and 19, 29 and 31, 41 and 43.' },
      { q: 'A number is 2 × 2 × 5 × 7. What is the number? How many factors does it have?', a: '140. It has 12 factors: 1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140.' },
      { q: 'Which number below 30 has the most factors?', a: '24, with 8 factors (1, 2, 3, 4, 6, 8, 12, 24).' },
      { q: 'A number between 20 and 40 leaves remainder 1 when divided by 2, by 3 and by 4. Find both possible numbers.', a: '25 and 37. Each is 1 more than a multiple of 12.' }
    ],
    challenge: [
      { q: 'Find the smallest number with exactly 8 factors, and then the smallest ODD number with exactly 8 factors. Why is the odd one so much bigger?', a: '24 (1, 2, 3, 4, 6, 8, 12, 24) and 105 (1, 3, 5, 7, 15, 21, 35, 105). 8 factors need either three different primes multiplied (like 3 × 5 × 7) or a prime cubed times another prime (like 2 × 2 × 2 × 3). With only odd primes the smallest choices are 3 × 5 × 7 = 105 (3 × 3 × 3 × 5 = 135 is bigger), but one factor of 2 makes the number much smaller.' },
      { q: 'Ali multiplies two different primes and gets 91. Mei multiplies three different primes and gets 105. Which primes did each of them use?', a: 'Ali: 7 × 13. Mei: 3 × 5 × 7.' },
      { q: 'Find the smallest number that can be divided exactly by 2, 3, 4, 5 and 6.', a: '60. It needs 2 × 2 (for 4), a 3 and a 5: 2 × 2 × 3 × 5 = 60.' },
      { q: '1001 = 7 × 11 × 13. Use this to write 3003 and 5005 as products of primes.', a: '3003 = 3 × 7 × 11 × 13 and 5005 = 5 × 7 × 11 × 13.' },
      { q: 'Find all the numbers between 100 and 200 that have exactly 3 factors.', a: '121 and 169 (11 × 11 and 13 × 13). 144 = 12 × 12 does not work because 12 is not prime.' },
      { q: 'Which even number below 50 can be written as the sum of two primes in the most ways? How many ways?', a: '48, in 5 ways: 5 + 43, 7 + 41, 11 + 37, 17 + 31, 19 + 29.' },
      { q: 'Make up a “Who am I?” number puzzle using factors and primes, for example: “I am between 30 and 60 and I have exactly three factors.” Write 2 or 3 clues so that only ONE number fits. Swap with a partner, then check that no other number fits.', a: 'Open. Example: “I am between 30 and 60 and I have exactly 3 factors” fits only 49 (7 × 7). The numbers with exactly 3 factors are the squares of primes: 4, 9, 25, 49, 121, … Check a puzzle by listing every number that fits the clues.' },
      { q: 'A farmer counts her eggs in 2s, 3s, 4s, 5s and 6s, and each time there is 1 egg left over. When she counts them in 7s, none are left over. What is the smallest number of eggs she could have?', a: '301. It must be 1 more than a multiple of 60: 61, 121, 181, 241, 301, … The first of these in the 7 times table is 301 = 7 × 43.' },
      { q: '20 lockers are closed. Student 1 opens every locker. Student 2 changes every 2nd locker (open to closed, closed to open). Student 3 changes every 3rd locker, and so on up to student 20. Which lockers are open at the end?', a: '1, 4, 9 and 16. Locker n is changed once for each factor of n. Only square numbers have an odd number of factors, so only they end up open.' }
    ]
  },

  workbook: H => {
    const W = [];
    const hat = ['hat', 'when green flag clicked'];
    const side = (left, wl, right) => H.tbl([wl, 9900 - wl], [H.row([H.cell(['<div style="padding:4px 8px">' + left + '</div>'], wl, { h: 60 }), H.cell(right, 9900 - wl, { h: 60, align: 'left' })])]);
    const txt = (t, pad) => `<div style="text-align:left;padding:${pad || '6px 4px 0'}">${esc(t)}</div>`;
    const dl = '<div style="border-bottom:2px dotted #8A94AD;height:26px;margin:0 4px"></div>';
    // Q1 factors table and prime tests
    W.push(H.q(1, 'A prime number has exactly 2 factors: 1 and itself. Use factor pairs to fill in the table.', { before: 0, keepNext: true }));
    { const ws = [1400, 5300, 1600, 1600];
      W.push(H.tbl(ws, [H.row(['Number', 'All its factors', 'How many?', 'Prime?'].map((s, i) => H.cell(s, ws[i], { bold: true, fill: 'D9D9D9', h: 40 }))),
        ...['28', '31', '49', '51', '1'].map(v => H.row([H.cell(v, ws[0], { bold: true, h: 55 }), H.cell('', ws[1]), H.cell('', ws[2]), H.cell('', ws[3])]))])); }
    W.push(H.sub('a', 'Test with 2, 3, 5 and 7. Circle the primes:     57     67     77     83     97     99'));
    W.push(H.sub('b', 'Ali says 87 is prime because it is odd and does not end in 5. Is he right?'));
    W.push(...H.lines(1));
    // Q2 factor trees
    W.push(H.q(2, 'Factor trees. Keep splitting until every branch ends in a prime.', { keepNext: true }));
    W.push(H.fig(treesSvg()));
    W.push(H.sub('a', '72  =  _______________      (b)  150  =  _______________'));
    W.push(H.sub('c', 'A number is 2 × 3 × 3 × 7. What is the number?   ________'));
    W.push(H.p([`<div style="border:2px solid ${N};border-radius:12px;background:#FFF4D1;padding:6px 14px;margin-left:40px"><div style="font-size:14px;color:#3B4A6B"><b style="color:${TEAL};font-size:15px">Python corner (optional): a factor finder.</b>  n % d is n mod d. It lists the factors of n and counts them. Change n to check Q1.</div><pre style="margin:4px 0 2px;font-family:'Courier New',monospace;font-size:14px;line-height:1.3;white-space:pre">${esc('n = 28\nf = [d for d in range(1, n + 1) if n % d == 0]\nprint(f, len(f))')}</pre></div>`], { after: 0 }));

    // ---- page 2 ----
    W.push(H.q(3, 'Predict, then trace. This code counts the factors of 6. Fill in the trace table.', { pb: true, before: 0, keepNext: true }));
    { const tr = H.tbl([1300, 2200, 2200], [H.row(['d', '6 mod d', 'count after'].map((s, i) => H.cell(s, [1300, 2200, 2200][i], { bold: true, fill: 'EDEDED', h: 20 }))),
        ...[1, 2, 3, 4, 5, 6].map(k => H.row([H.cell(String(k), 1300, { h: 5 }), H.cell(k === 1 ? '0' : '', 2200, { h: 12 }), H.cell(k === 1 ? '1' : '', 2200, { h: 12 })]))]);
      W.push(side(blocks([hat, ['var', 'set count to (0)'], ['var', 'set d to (1)'], ['ctl', 'repeat (6)', [['ctl', 'if (6 mod d = 0) then', [['var', 'change count by (1)']]], ['var', 'change d by (1)']]], ['look', 'say (count)']], 'Code: set count to 0, d to 1; repeat 6: if 6 mod d = 0 then change count by 1; change d by 1; then say count', 14), 4100,
        [tr, txt('(a)  What does it say at the end?  ______', '8px 4px 0'), txt('(b)  Change both 6s to 13. What does it say? Why?'), dl])); }
    // Q4 Goldbach
    W.push(H.q(4, 'Goldbach’s guess: every even number above 2 is a sum of two primes.', { keepNext: true }));
    W.push(H.sub('a', '24 in every way:  ________________________________'));
    W.push(H.sub('b', 'Explain why 27 cannot be the sum of two primes.'));
    // Q5 exactly 3 factors
    W.push(H.q(5, 'Exactly 3 factors.', { keepNext: true }));
    W.push(H.sub('a', 'All the numbers from 1 to 30 with exactly 3 factors (there are 3):  ______________'));
    W.push(H.sub('b', 'What do you notice?  ______________________________'));
    // Q6 plan
    W.push(H.q(6, 'Plan your code. Put the blocks in order so the sprite says every factor of 40.', { keepNext: true }));
    { const lb = (t, p) => `<div style="display:flex;align-items:center;gap:6px"><b style="width:18px">${t}</b>${blocks(p, 'Block ' + t, 14).replace('max-width:100%', 'flex:none')}</div>`;
      const col = xs => '<div style="display:flex;flex-direction:column;gap:6px;align-items:flex-start">' + xs.join('') + '</div>';
      W.push(side('<div style="display:flex;gap:14px">' + col([lb('A', [['look', 'say (d) for (1) seconds']]), lb('B', [['ctl', 'repeat (40)', []]]), lb('C', [['var', 'set d to (1)']])]) + col([lb('D', [['var', 'change d by (1)']]), lb('E', [hat]), lb('F', [['ctl', 'if (40 mod d = 0) then', []]])]) + '</div>', 5600,
        [txt('My order (show what goes inside):', '2px 4px 0'), dl, txt('How many numbers does it say?  ______', '10px 4px 0')]));
    }
    return W;
  }
};
