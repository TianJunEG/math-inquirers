// Math Inquirers P6 (post-PSLE maths + coding bridge) — Lesson 10: Showcase Challenge (mixed challenge round, then each child builds and shows a small puzzle program)
// Every answer below was worked out by hand and checked; every Python program was run.

const NAVY = '#1B2A49', YEL = '#FFC93C', SKY = '#DDEBF7', TEAL = '#1F7A6F', RED = '#D64545', WHITE = '#FFFFFF';
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

// ---- our own code-block drawings (simple coloured rounded shapes, not Scratch artwork) ----
const BK = { event: [YEL, NAVY], ctrl: [TEAL, WHITE], var: [SKY, NAVY], list: [WHITE, NAVY], look: [RED, WHITE] };
const kindOf = s => { const w = s.split(' ')[0]; return w === 'when' ? 'event' : ['repeat', 'if', 'else'].includes(w) ? 'ctrl' : ['set', 'change'].includes(w) ? 'var' : ['add', 'delete'].includes(w) ? 'list' : 'look'; };
function blocks(prog, fs = 16) {
  const H = Math.round(fs * 1.9), ind = Math.round(fs * 1.5), cw = fs * 0.6, pad = 10;
  const tw = s => Math.round(s.length * cw + 2 * pad);
  const txt = (s, x, y, c) => `<text x="${x + pad}" y="${y + Math.round(H * 0.66)}" font-size="${fs}" font-weight="700" fill="${c}" font-family="Arial">${esc(s)}</text>`;
  const lay = (items, x, y0) => {
    let s = '', y = y0, w = 0;
    for (const it of items) {
      if (typeof it === 'string') {
        const k = kindOf(it), [f, c] = BK[k], bw = tw(it);
        s += `<rect x="${x}" y="${y}" width="${bw}" height="${H}" rx="${k === 'event' ? 14 : 8}" fill="${f}" stroke="${NAVY}" stroke-width="2"/>` + txt(it, x, y, c);
        y += H; w = Math.max(w, x + bw);
      } else {
        const segs = [[it.c, it.body]]; if (it.else) segs.push(['else', it.else]);
        let pts = [[x, y]], inner = '', heads = '';
        segs.forEach(([lab, body]) => {
          const hw = Math.max(tw(lab), ind + 70);
          pts.push([x + hw, y], [x + hw, y + H], [x + ind, y + H]);
          heads += txt(lab, x, y, WHITE); w = Math.max(w, x + hw);
          const r = lay(body, x + ind, y + H); inner += r.s; w = Math.max(w, r.w);
          y = Math.max(r.y, y + H + Math.round(H * 0.5));
          pts.push([x + ind, y]);
        });
        const bh = Math.round(H * 0.45);
        pts.push([x + ind + 60, y], [x + ind + 60, y + bh], [x, y + bh]);
        s += `<polygon points="${pts.map(p => p.join(',')).join(' ')}" fill="${TEAL}" stroke="${NAVY}" stroke-width="2" stroke-linejoin="round"/>` + heads + inner;
        y += bh;
      }
    }
    return { s, y, w };
  };
  const r = lay(prog, 2, 2);
  return { svg: r.s, w: Math.ceil(r.w + 4), h: Math.ceil(r.y + 4) };
}
// a list monitor: a panel with a title and numbered rows
const listMon = (name, vals, x, y, fs = 16) => {
  const rh = Math.round(fs * 1.7), w = 150;
  let s = `<rect x="${x}" y="${y}" width="${w}" height="${rh * (vals.length + 1) + 10}" rx="10" fill="${WHITE}" stroke="${NAVY}" stroke-width="2"/>`;
  s += `<text x="${x + w / 2}" y="${y + rh - 6}" font-size="${fs}" font-weight="700" text-anchor="middle" fill="${TEAL}" font-family="Arial">${esc(name)}</text>`;
  vals.forEach((v, i) => {
    const yy = y + rh * (i + 1) + 4;
    s += `<text x="${x + 14}" y="${yy + rh - 8}" font-size="${fs}" font-weight="700" fill="${NAVY}" font-family="Arial">${i + 1}</text>`;
    s += `<rect x="${x + 42}" y="${yy + 3}" width="${w - 56}" height="${rh - 6}" rx="6" fill="${YEL}" stroke="${NAVY}" stroke-width="1.5"/><text x="${x + 42 + (w - 56) / 2}" y="${yy + rh - 8}" font-size="${fs}" font-weight="700" text-anchor="middle" fill="${NAVY}" font-family="Arial">${esc(v)}</text>`;
  });
  return { s, w, h: rh * (vals.length + 1) + 10 };
};
const codeSvg = (prog, aria, fs) => { const b = blocks(prog, fs); return `<svg aria-label="${esc(aria)}" viewBox="0 0 ${b.w} ${b.h}" xmlns="http://www.w3.org/2000/svg" style="width:${b.w}px;max-width:100%">${b.svg}</svg>`; };
const codeFig = (prog, aria, list) => {
  const b = blocks(prog);
  let extra = '', W = b.w, Hh = b.h;
  if (list) { const m = listMon(list[0], list[1], b.w + 40, 2); extra = m.s; W = b.w + 40 + m.w + 4; Hh = Math.max(Hh, m.h + 6); }
  return `<svg aria-label="${esc(aria)}" viewBox="0 0 ${W} ${Hh}" xmlns="http://www.w3.org/2000/svg" style="width:${W}px;max-width:100%">${b.svg}${extra}</svg>`;
};
const pyBox = (title, code) => `<div style="margin:0"><div style="border:2px solid ${TEAL};border-radius:10px;padding:6px 12px;background:#F3FAF8"><div style="font-weight:700;color:${TEAL};font-size:14px">${esc(title)}</div><pre style="margin:2px 0 0;font-family:'Courier New',monospace;font-size:11.5px;line-height:1.3;color:${NAVY}">${esc(code).replace(/\n/g, '&#10;')}</pre></div></div>`;

// hexagon chains made of sticks: 1, 2 and 3 hexagons (pointy-top, sharing upright sides)
const hexChains = () => {
  const r = 20, w = Math.sqrt(3) * r, cy = 32;
  let s = '';
  const stick = (x1, y1, x2, y2) => `<line x1="${x1.toFixed(1)}" y1="${y1.toFixed(1)}" x2="${x2.toFixed(1)}" y2="${y2.toFixed(1)}" stroke="${NAVY}" stroke-width="7" stroke-linecap="round"/><line x1="${x1.toFixed(1)}" y1="${y1.toFixed(1)}" x2="${x2.toFixed(1)}" y2="${y2.toFixed(1)}" stroke="${YEL}" stroke-width="3.5" stroke-linecap="round"/>`;
  let x0 = 20;
  [[1, '6 sticks'], [2, '11 sticks'], [3, '16 sticks']].forEach(([n, lab]) => {
    for (let k = 0; k < n; k++) {
      const cx = x0 + w / 2 + k * w;
      const v = [-90, -30, 30, 90, 150, 210].map(a => [cx + r * Math.cos(a * Math.PI / 180), cy + r * Math.sin(a * Math.PI / 180)]);
      for (let e = 0; e < 6; e++) { if (k > 0 && e === 4) continue; const a = v[e], b = v[(e + 1) % 6]; s += stick(a[0], a[1], b[0], b[1]); }
    }
    const mx = x0 + Math.max(n * w, 70) / 2;
    s += `<text x="${mx.toFixed(1)}" y="${cy + r + 22}" font-size="15" font-weight="700" text-anchor="middle" fill="${TEAL}" font-family="Arial">${n} hexagon${n > 1 ? 's' : ''}</text><text x="${mx.toFixed(1)}" y="${cy + r + 40}" font-size="15" font-weight="700" text-anchor="middle" fill="${NAVY}" font-family="Arial">${lab}</text>`;
    x0 += Math.max(n * w, 70) + 30;
  });
  return `<svg aria-label="Hexagon chains made of sticks: 1 hexagon uses 6 sticks, 2 hexagons use 11 sticks, 3 hexagons use 16 sticks" viewBox="0 0 ${Math.ceil(x0)} 100" xmlns="http://www.w3.org/2000/svg" style="width:${Math.ceil(x0)}px;max-width:100%">${s}</svg>`;
};

const PY_MACHINE = `import random
n = random.randint(1, 20)
out = n * 3 + 4
print("My machine does x 3, then + 4.")
print("Out came", out)
guess = int(input("What went in? "))
if guess == n:
    print("You cracked it!")
else:
    print("No, it was", n)`;

module.exports = {
  lesson: {
    n: 10, week: 5, session: 'B', title: 'Showcase Challenge', topic: 'Mixed: Maths and Code',
    objective: 'Use ideas from all nine lessons (sequences, primes, negative numbers, algebra, counting, probability, angles, clock arithmetic, averages) in a mixed challenge round, then plan, build, test and present a small puzzle program, working out the maths by hand first and explaining why it works.',
    skills: 'Choosing a strategy, connecting topics, planning code, testing with a known answer, presenting and explaining',
    materials: 'Laptop or desktop with Scratch 3 (scratch.mit.edu), workbook (challenge round on page 1, planning sheet on page 2), pencil, mini whiteboard, the starter projects as .sb3 files (A Mystery Machine, B Prime or Not?, C Lucky Seven, D Clock Jumper; children use File, Load from your computer), or build them from the slides, certificates, stamps.',
    online: 'Challenge round in teams of 2 in breakout rooms. Building: everyone in the main room with cameras on, asking for help in the chat. Showcase: in two rounds of 4, each child shares their screen for 2 minutes 30 seconds; the audience writes one question for each presenter and the tutor posts stars first (two stars and a question). A child may show a screenshot and the tutor runs the file. Children may paste a screenshot into the chat instead and the tutor runs their file, which removes screen-share switching. Block colours on our slides are simplified; in Scratch, find blocks by the category name on the left, not by colour.',
    warmup: 'Lightning relay: one quick question from each of Lessons 1 to 9, passed round the group by volunteers. Then five quick questions on the slide.',
    explore: 'Challenge round in teams of 2: workbook page 1, three puzzles from across the program (hexagon pattern and code, primes, and a quick-fire round with negatives, machines, angles and clock arithmetic). 1 point for each answer, 1 for a check (by hand or in code), 1 for a clear reason; each team keeps its own score on page 1 and shows it only if the team wants to. Then talk: how did you start each puzzle?',
    mini: 'From puzzle to program: pick a maths idea, work out the answer by hand first, turn the rule into blocks (input, rule, check, output), test with a value you already know, then add a twist. Starter A, Mystery Machine: the computer picks n from 1 to 20, shows 3n + 4, and checks your guess (backwards: subtract 4, divide by 3). Starter B, Prime or Not?: a loop counts the factors of n with mod; exactly 2 factors means prime. Starter C, Lucky Seven: roll two dice 1000 times and count the 7s; 6 of the 36 results make 7, so expect about 167, never exactly.',
    share: 'Showcase: 2 minutes 30 seconds each, in two rounds of 4. Show the puzzle, run the program, show one test where you knew the answer first, and explain the maths that makes it work.',
    exit: { q: 'Write one thing your program does, one test you did (the input and the answer you expected), and the maths that explains it.', a: 'Open. Look for a test worked out by hand before running the program, and a correct maths reason.' },
    mistakes: ['Coding before working out the maths, so there is no way to tell whether the output is right.', 'Testing only once, or only with the value the program happened to show, instead of a value worked out by hand (and an edge case such as 1 or 0).', 'Showcase: reading the code block by block instead of explaining the maths puzzle and why the program works.'],
    extension: 'Level up your program: ask 5 questions and keep a score, let the player choose the rule, or count every dice total in a list. Write a Python version and check it gives the same results.',
    key: [
      ['Q1', '(a) 51  (b) 5n + 1  (c) 20 hexagons (5n + 1 = 101)  (d) 76: it checks a chain of 15 hexagons (6 + 14 × 5)'],
      ['Q2', '(a) 49 (factors 1, 7, 49; the only other 2-digit number with exactly 3 factors is 25)  (b) 2 × 2 × 3 × 7  (c) 3 + 37, 11 + 29, 17 + 23 (3 ways)'],
      ['Q3', '(a) −7 °C (−4 + 9 = 5, 5 − 12 = −7)  (b) 5 (5 × 3 − 10 = 5)  (c) 15 sides (360 ÷ 24)  (d) 1 o’clock (9 + 100 = 109 = 9 × 12 + 1)  (parts e and f are now in Think harder 4)'],
      ['Q4', '(a) 31; 18 ((58 − 4) ÷ 3)  (b) 4 factors (1, 7, 13, 91): not prime  (c) about 139: 5 of the 36 equally likely results make 8 (2 + 6, 3 + 5, 4 + 4, 5 + 3, 6 + 2), and 1000 × 5 ÷ 36 ≈ 139; the program gives a number near this, not exactly'],
      ['Q5', 'Open: an idea, the puzzle, its answer worked out by hand, and a twist.'],
      ['Q6', 'Open: blocks (under 15) and at least two tests worked out before running, one of them an edge case.']
    ]
  },

  script: {
    hook: ['Welcome to our last lesson, inquirers! Two parts today. First a challenge round with puzzles from all nine lessons. Then you become the puzzle maker: you build a small program that sets a maths puzzle, and you show it to the group.', 'Our rule all program long: notice it, test it, explain why. Today you do all three in front of an audience.'],
    warmIntro: ['Lightning relay! I ask a quick question from one of our lessons and ask for a volunteer to answer. The child who answers reads the next card and invites someone who has not had a turn. “Pass” is always fine, and the next person helps. Ready? First one: what is the 10th term of 3, 7, 11, 15?', 'Which lesson did that question come from? Can you remember the trick we learned?'],
    predict: ['Look at the puzzles on page 1. Which one do you think will be hardest? Which lesson does each one come from? Write your guesses at the top of the page.'],
    exploreHints: ['Stuck on a puzzle: which lesson does it remind you of? Make a table, list it in order, or draw it.', 'Got an answer: earn the check point. Check it a different way, or test it in code.', 'Finished early: write a rule for Q1 that would make 2027 sticks. Is it possible with hexagons?'],
    think: ['“Hexagon chains: 6, 11, 16 sticks. Each new hexagon shares one side with the last one, so it adds 5 sticks. The first hexagon is 6 = 5 + 1. So n hexagons use 5n + 1 sticks. For 10 hexagons: 51. I can test that in code: start at 6 and change by 5 nine times.”', '“Mystery Machine: the program picks n, works out 3n + 4 and shows it. If it shows 19, I go backwards: 19 − 4 = 15, 15 ÷ 3 = 5. Before I trust the program, I test it with a number I already know: if n is 5 it must show 19.”', '“Lucky Seven: there are 6 × 6 = 36 equally likely results for two dice. 1 + 6, 2 + 5, 3 + 4, 4 + 3, 5 + 2, 6 + 1 make 7: that is 6 of 36, one sixth. So in 1000 rolls I expect about 167. When I run it I got 152, then 182, then 162: close to 167 but never the same, because the rolls are random.”'],
    circulate: ['Ask: “What answer should your program give for this input? How do you know?”', 'Ask: “What happens with an edge case: 1, 0, or the biggest number?”', 'Ask: “In one sentence, what maths is your program about?”'],
    hints: ['Hint 1: “Start from a starter project and change one thing: the rule, the numbers, or the question.”', 'Hint 2: “Write the maths on your planning sheet first. Then find one block for each line of your plan.”', 'Hint 3: “If the program disagrees with you, trace it in a table: which value goes in, what does each block do?”'],
    talk: ['“What was the hardest bug you fixed today? How did you find it?”', '“Which maths idea from the program would you like to explore further, and what would you try next?”'],
    talkAns: 'Open answers. Listen for: testing with a value worked out by hand, tracing the code in a table, and maths links (nth term, primes, negative numbers, equations, probability, angles, averages). This is enrichment toward secondary maths and coding, not a preview of exam topics.',
    close: ['“Ten lessons ago you predicted the 100th term of a pattern and checked it in code. Today you built your own puzzle program and explained the maths to an audience. That is what inquirers do. Here is your certificate. Keep noticing, keep testing, and keep asking why!”', 'Give each child a certificate and tell them one specific thing they did well in their showcase.']
  },

  deck: {
    today: 'Take on a challenge round with puzzles from all nine lessons, then plan, build, test and show your own puzzle program.',
    warmGame: 'Lightning relay. The tutor asks a quick question from one of Lessons 1 to 9 and asks for a volunteer; the child who answers asks the next question (from the cards on screen) and invites someone who has not had a turn. Pass is always fine.',
    warmQs: [['What is the nth term of 4, 7, 10, 13, …?', '3n + 1'], ['Is 91 a prime number?', 'No: 7 × 13'], ['−5 + 8 − 6 = ?', '−3'], ['A regular hexagon: what angle does the turtle turn at each corner?', '60°'], ['Mean of 7, 9, 11 and 13?', '10']],
    expSetup: ['Teams of 2. Open the workbook at page 1: the challenge round.', 'Three puzzles from across the program. Maths first.', 'Score: 1 point for each answer, 1 for a check, 1 for a clear reason. Keep your own score on page 1.', 'After 10 minutes we check together.'],
    expPic: 'a scoreboard with three columns: answer, check, reason, and a point for each.',
    expAsk: [['How did you start the hexagon puzzle?', 'Make a table of hexagons and sticks; notice + 5 each time; the rule is 5n + 1.'], ['How did you know you had found every way to write 40 as two primes?', 'Go through the primes in order up to 20 and test whether 40 minus each one is prime.'], ['Which check did you do in code?', 'For example, run the hexagon loop, or list the digit-card numbers with nested loops and count the multiples of 3.']],
    mini1: { head: 'Starter A: Mystery Machine', body: ['The program picks n from 1 to 20 and shows 3n + 4.', 'The player works backwards: subtract 4, then divide by 3.', 'Test with a value you know: n = 5 must show 19.'], ans: 'Out 25 → 7. Out 64 → 20. Out 3 is impossible: the smallest OUT for n from 1 to 20 is 7.' },
    mini2: { head: 'Starter C: Lucky Seven', body: ['Roll two dice 1000 times. Count the 7s.', '36 equally likely results; 6 of them make 7.', 'So expect about 1000 ÷ 6.'], ans: 'About 167. Each run gives a slightly different number (for example 152, 182, 162): random results vary.' },
    keyHead: 'Key idea: maths first, then code to test it',
    keyBig: 'Work out the answer by hand first. Then the program is a test: if it agrees with you, you are probably both right; if not, find out which one is wrong.',
    keySmall: 'A good showcase: show the puzzle, run it, show a test you knew the answer to, and explain why it works.',
    brk: 'Turtle moves. The tutor calls a polygon; everyone turns on the spot by its outside angle at every corner (triangle: 120°, square: 90°, hexagon: 60°) and counts until they face the front again.',
    ws1: 'Page 1, in teams of 2 (the challenge round): Q1 hexagon chains and code, Q2 primes, Q3 quick-fire round (negatives, machines, turtle angles, clock).',
    ws2: 'Page 2, on your own (plan and build): Q4 test the starters by hand, Q5 my puzzle program, Q6 blocks and test table, then build it in Scratch.'
  },

  moved: [
    { q: 'Cards 1, 2, 3, 4 make 2-digit numbers (no card twice). (a) How many numbers? How many are even? (b) One of the numbers is picked at random. What is the probability it is a multiple of 3?', a: '(a) 12 numbers (4 × 3); 6 are even (3 + 3). (b) 4/12 = 1/3 (12, 21, 24, 42).' }
  ],

  qbank: {
    core: [
      { q: 'Find the 20th term of 5, 8, 11, 14, … (Write the terms out, or look for a shortcut.)', a: '62 (the nth term is 3n + 2, so 3 × 20 + 2)' },
      { q: 'Break 60 into smaller and smaller multiplications until every number is prime (2, 3, 5, 7, 11, …). Write 60 as a product of primes.', a: '2 × 2 × 3 × 5' },
      { q: 'The temperature is −3 °C (3 degrees below zero). It falls by 5 degrees. What is it now? Count down on a thermometer drawing.', a: '−8 °C' },
      { q: 'A machine does × 4, then − 6. What comes out when 5 goes in?', a: '14' },
      { q: 'How many different 2-digit numbers can you make with the digit cards 3, 5 and 7 (each card used at most once)?', a: '6 (35, 37, 53, 57, 73, 75)' },
      { q: 'Find the mean of 12, 15, 9, 20 and 14.', a: '14 (70 ÷ 5)' }
    ],
    stretch: [
      { q: 'A row of squares uses 4, 7, 10, 13, … matchsticks. Which pattern number uses exactly 100 matchsticks?', a: 'Pattern 33 (3n + 1 = 100)' },
      { q: 'Find all the prime numbers between 80 and 100.', a: '83, 89 and 97' },
      { q: 'A regular polygon has an angle of 150° inside each corner. How many sides does it have?', a: '12 (the turn at each corner is 180° − 150° = 30°, and 360 ÷ 30 = 12)' },
      { q: 'Two dice are rolled and the numbers are added. What is the probability that the total is 10 or more?', a: '6/36 = 1/6 (10: 3 ways, 11: 2 ways, 12: 1 way)' },
      { q: 'Use a Caesar cipher with a shift of 5 to encode the word MATHS.', a: 'RFYMX' },
      { q: 'It is 10 o’clock. What time will a 12-hour clock show 50 hours later?', a: '12 o’clock (10 + 50 = 60, and 60 is a multiple of 12)' },
      { q: 'The mean of 6 numbers is 9. One more number is added and the mean becomes 10. What number was added?', a: '16 (7 × 10 − 6 × 9)' },
      { q: 'In how many different orders can 4 children stand in a line?', a: '24 (4 × 3 × 2 × 1)' }
    ],
    challenge: [
      { q: 'How many of the numbers from 1 to 100 are NOT multiples of 2 or of 3?', a: '33 (multiples of 2: 50, of 3: 33, of both (6): 16; 100 − (50 + 33 − 16) = 33)' },
      { q: 'A machine does × 3, then − 8. Mei puts a number in and gets the SAME number out. What is it? What if the machine does × 3, then + 8?', a: '4 (4 × 3 − 8 = 4). With + 8 it is −4 (−4 × 3 + 8 = −4).' },
      { q: 'How many squares of any size are there on a 4 by 4 grid?', a: '30 (16 + 9 + 4 + 1)' },
      { q: 'The nth term of a sequence is 4n + 1. Find all the prime numbers among its first 15 terms. Is any term of the sequence even? Explain.', a: 'The first 15 terms are 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61. The primes are 5, 13, 17, 29, 37, 41, 53 and 61 (8 of them). No term is even: 4n is even, and even + 1 is odd.' },
      { q: 'A turtle repeats [move 100, turn ↻ 150]. After how many repeats does it first face the way it started? What does it draw, and how many times does it go round?', a: '12 repeats (12 × 150° = 1800° = 5 × 360°, and no smaller number of repeats gives a multiple of 360°). It draws a 12-point star going round 5 times.' },
      { q: 'Three numbers have a mean of 8 and a median of 7. The biggest is 9 more than the smallest. Find the three numbers.', a: '4, 7 and 13 (the total is 24, so the smallest and biggest add to 17 and differ by 9)' },
      { q: 'Make up a challenge question that mixes TWO topics from the programme (for example primes and the clock, or sequences and negative numbers). Write the question, the answer and the working. Swap with a partner and solve each other’s.', a: 'Open. Example: “The nth term of a sequence is 7n − 3. Which is the first term that is a multiple of 5?” The terms are 4, 11, 18, 25, so it is the 4th term, 25. Check that the answer is correct and that both topics are really needed.' },
      { q: 'A spinner has the numbers 1 to 8, all equally likely. Ravi spins it twice and adds the numbers. What is the probability that the total is 9? Plan a program that tests it 1000 times.', a: '8/64 = 1/8 (1 + 8, 2 + 7, … , 8 + 1), so about 125 in 1000. Program: set nines to 0; repeat 1000 (if pick random 1 to 8 + pick random 1 to 8 = 9 then change nines by 1); say nines.' },
      { q: 'The nth term of a sequence is 6n − 1. Is 2027 (the year you start Secondary 1) in the sequence? Which is the first term bigger than 2027?', a: 'Yes: it is the 338th term (6 × 338 − 1 = 2027). The first term bigger than 2027 is the 339th, 2033.' }
    ]
  },

  workbook: H => {
    const hexProg = ['set sticks to 6', { c: 'repeat 14', body: ['change sticks by 5'] }, 'say sticks'];
    const side = (l, r) => `<div class="p img" style="display:flex;gap:14px;align-items:center;justify-content:space-between;margin:4px 0 8px"><div style="flex:none">${l}</div><div style="flex:1;min-width:0">${r}</div></div>`;
    const wt = [2600, 3300, 2700, 1300];
    const wp = [3600, 6300];
    return [
      H.q(1, 'Chains of hexagons are made from sticks.', { before: 0, keepNext: true }),
      side(hexChains(), codeSvg(hexProg, 'Code blocks: set sticks to 6, repeat 14 (change sticks by 5), say sticks', 14)),
      H.sub('a', 'Sticks for 10 hexagons?  ____      (b)  Rule for n hexagons:  sticks = __________'),
      H.sub('c', 'How many hexagons can be made with exactly 101 sticks?  ____'),
      H.sub('d', 'Predict what the code says.  ____       Which chain does it check?  ____ hexagons'),
      H.q(2, 'Prime hunters.', { before: 20, keepNext: true }),
      H.sub('a', 'I have 2 digits and exactly 3 factors. My digits add up to 13. What am I?  ____'),
      H.sub('b', 'Write 84 as a product of prime numbers.  ________________'),
      H.sub('c', 'Find ALL the ways to write 40 as two primes added.  __________________'),
      H.q(3, 'Quick-fire round.', { before: 20, keepNext: true }),
      H.sub('a', 'It is −4 °C. It warms up 9 °C, then cools 12 °C. What is it now?  ____'),
      H.sub('b', 'A machine does × 3, then − 10. Which IN number comes OUT unchanged?  ____'),
      H.sub('c', 'A turtle draws a regular polygon, turning 24° at each corner. Sides?  ____'),
      H.sub('d', 'It is 9 o’clock. What time will a 12-hour clock show 100 hours from now?  ____'),

      H.q(4, 'Maths first! Work out what each starter project should do BEFORE you run it.', { pb: true, before: 0, keepNext: true }),
      H.sub('a', 'Mystery Machine (× 3, then + 4).  n = 9 gives?  ____     OUT 58 came from?  ____'),
      H.sub('b', 'Prime or Not? How many factors does it count for 91?  ____     Prime?  ____'),
      H.sub('c', 'Lucky Seven, changed to count 8s: about how many 8s in 1000 rolls? Why?'),
      ...H.lines(1),
      H.q(5, 'My puzzle program: the plan.', { keepNext: true }),
      H.tbl(wp, [
        ['My idea (Starter A, B, C or my own)', 'The maths puzzle it asks', 'Its answer, worked out by hand', 'My twist (what I change or add)'].map(s => H.row([H.cell(s, wp[0], { bold: true, fill: 'EDEDED', align: 'left', h: 50 }), H.cell(' ', wp[1], { h: 50 })]))
      ].flat()),
      H.q(6, 'Plan your blocks (under 15) in the box. Fill in each test BEFORE you run it.', { keepNext: true }),
      side(`<div style="width:330px;height:190px;border:2px solid #1B2A49;border-radius:8px;background:#FFFFFF"></div>`, pyBox('Python fans (optional): Starter A. To test it with Q4(a), change line 2 to  n = 9', PY_MACHINE)),
      H.tbl(wt, [
        H.row(['Input (what I type or set)', 'It should say (by hand)', 'It said', 'Same? ✓'].map((s, i) => H.cell(s, wt[i], { bold: true, fill: 'EDEDED', h: 60 }))),
        ...['Test 1', 'Test 2', 'Edge case'].map(t => H.row([H.cell(t, wt[0], { bold: true, align: 'left', h: 60 }), ...wt.slice(1).map(w => H.cell(' ', w, { h: 60 }))]))
      ]),
      H.sub('', 'Ready to show?   [  ] I can explain the maths   [  ] I tested a value I knew   [  ] I tested an edge case', { after: 0 })
    ];
  }
};
