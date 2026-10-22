// Math Inquirers P6 — Lesson 8: Secret Codes (clock / modular arithmetic; lists, letters and mod)
// Every answer below was worked out and checked by computer: letter numbers A = 0 … Z = 25,
// code number = (letter number + shift) mod 26; clock and calendar answers use mod 12 and mod 7. The Python program was run.

const NAVY = '#1B2A49', YEL = '#FFC93C', SKY = '#DDEBF7', TEAL = '#1F7A6F', RED = '#D64545', WHITE = '#FFFFFF';
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

// ---------- code blocks: our own simple coloured shapes (never Scratch artwork) ----------
// prog: [kind, text] or [kind, text, [children]] for a C-shaped block; {…} marks a white slot.
const BC = { event: [YEL, NAVY], ctrl: [WHITE, NAVY], motion: [SKY, NAVY], sense: [SKY, NAVY], pen: [TEAL, WHITE], var: [RED, WHITE], looks: [YEL, NAVY] };
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

const ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
// letter-number strip: A to Z with 0 to 25 underneath
const strip = () => {
  const cw = 596 / 26;
  let s = `<svg aria-label="Letter numbers: A is 0, B is 1, C is 2 and so on up to Z is 25" viewBox="0 0 600 52" xmlns="http://www.w3.org/2000/svg" style="width:580px;max-width:100%">`;
  s += `<rect x="2" y="2" width="596" height="48" rx="6" fill="${WHITE}" stroke="${NAVY}" stroke-width="2"/><rect x="2" y="2" width="596" height="24" rx="6" fill="${YEL}" stroke="${NAVY}" stroke-width="2"/>`;
  let d = '';
  for (let i = 0; i < 26; i++) {
    const x = 2 + cw * i;
    if (i) d += `M${x.toFixed(1)} 2 V50 `;
    s += `<text x="${(x + cw / 2).toFixed(1)}" y="20" font-size="15" font-weight="700" text-anchor="middle" fill="${NAVY}" font-family="Arial">${ABC[i]}</text>`;
    s += `<text x="${(x + cw / 2).toFixed(1)}" y="44" font-size="14" text-anchor="middle" fill="${NAVY}" font-family="Arial">${i}</text>`;
  }
  return s + `<path d="${d}" stroke="${NAVY}" stroke-width="1"/></svg>`;
};
const codeFig = (prog, label) => {
  const b = blocks(prog, { fs: 15, h: 28 }), w = Math.max(b.w, 300);
  return `<svg aria-label="${esc(label)}" viewBox="0 0 ${w} ${b.h}" xmlns="http://www.w3.org/2000/svg" style="width:${Math.round(w * 0.93)}px;max-width:100%">${b.svg}</svg>`;
};

const PY = `alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
message = "MEET AT THE MRT"
shift = 3
code = ""
for letter in message:
    if letter in alphabet:
        n = alphabet.index(letter)   # A is 0
        m = (n + shift) % 26         # % is mod
        code = code + alphabet[m]
    else:
        code = code + letter         # keep spaces
print(code)`;
// checked by running it: prints "PHHW DW WKH PUW"

const pyHTML = s => esc(s).split('\n').map(l => l.replace(/^ +/, m => '&nbsp;'.repeat(m.length)).replace(/ {2,}/g, m => '&nbsp;'.repeat(m.length))).join('<br>');
const pyBox = H => {
  const ls = PY.split('\n'), code = part => `<div style="flex:1;text-align:left;font-family:'Liberation Mono',Consolas,monospace;font-size:12px;line-height:1.3;white-space:nowrap">${pyHTML(part.join('\n'))}</div>`;
  return H.tbl([9900], [H.row([H.cell(
    `<div style="text-align:left;font-weight:700;margin-bottom:3px">Optional, for children who already code: Python version. % is mod. Change the message and shift to test Q2; a negative shift decodes.</div>${code(ls)}`, 9900, { fill: 'EFEFEF', h: 40 })])]);
};

module.exports = {
  lesson: {
    n: 8, week: 4, session: 'B', title: 'Secret Codes', topic: 'Clock (Modular) Arithmetic',
    objective: 'Do clock arithmetic (counting past the end wraps round to the start), use n mod m as the remainder when n is divided by m, solve clock and calendar puzzles with mod 12 and mod 7, code and decode Caesar ciphers with letter numbers (A = 0 … Z = 25, code = (letter + shift) mod 26), crack a code, and test it all with a Scratch program that uses a list of letters and mod.',
    skills: 'Remainders and mod, clock and calendar arithmetic, negative numbers on a clock, Caesar ciphers, cracking codes by reasoning, lists and letters in code, tracing code in a table',
    materials: 'A laptop or desktop with Scratch 3 open (the tutor builds and shares a starter project with a list called alphabet holding A to Z; no .sb3 file exists in this repository, so build it beforehand), mini whiteboards, paper for code strips, scissors.',
    online: 'Children make their code strips on paper and hold them to the camera. Children hold up their coded name on paper to the camera, or the tutor reads out the coded names; partners decode on paper. Pairs use breakout rooms for the coding part; the driver shares the screen. Starter project: the tutor shares an .sb3 file (not a link only) containing the list alphabet with A to Z already filled in, and the loop already built; children add the three cipher blocks. Block colours on our slides are simplified; in Scratch, list blocks are red-orange (Variables palette) and you find blocks by the category name on the left, not by colour.',
    warmup: 'Clock jumps: the tutor shows a clock and asks “It is 9 o’clock. What time is it 4 hours later?” Children answer on whiteboards. Then times past 12, times going backwards, 24 hours later, and a day-of-the-week jump.',
    explore: 'Pairs make a shift-3 code strip (the alphabet, with the alphabet again underneath starting at D). They code their first names, swap and decode, then decode the tutor’s message PDWK LV IXQ. What happens to X, Y and Z? How do you decode?',
    mini: 'Clock arithmetic: 9 o’clock + 5 hours = 2 o’clock, because 14 mod 12 = 2 (mod = the remainder). A week is a 7-day clock: 45 days after Thursday is Sunday (45 mod 7 = 3). Letters are numbers 0 to 25 on a 26-hour clock: Caesar code = (letter + shift) mod 26 (ZOO with shift 5 is ETT); decode by shifting back and adding 26 if you go below 0 (AEB with shift 4 is WAX). Before page 2: trace the code in a table (SKY, shift 10 gives CUI), crack a code from a short word (YMNX NX KZS is THIS IS FUN), and combine shifts (15 then 15 is shift 4).',
    share: 'Why does a shift of 26 change nothing? Why is decoding a shift-3 message the same as coding it again with shift 23?',
    exit: { q: 'Code the word HI with a shift of 25. What do you notice?', a: 'GH (H = 7, 7 + 25 = 32, 32 mod 26 = 6 = G; I = 8, 33 mod 26 = 7 = H). A shift of 25 is the same as shifting back 1, because 25 = 26 − 1.' },
    mistakes: ['Off by one: counting A as 1 in the maths (we use A = 0, Z = 25), or forgetting that Scratch’s list starts at item 1.', 'Not wrapping round: writing a number bigger than 25 (or below 0 when decoding) instead of taking away or adding 26.', 'Calendars: counting today as day 1 (Saturday + 2 days is Monday, not Sunday), or giving the quotient instead of the remainder for mod.'],
    extension: 'The starter already keeps spaces (if the letter is in the alphabet list, code it, else join the letter itself). Add a “crack” button that says the message decoded with every shift from 1 to 25.',
    key: [
      ['Q1', '(a) 3 o’clock (15 − 12)  (b) 5 o’clock (30 mod 12 = 6, 11 + 6 = 17, 17 − 12 = 5)  (c) 7 o’clock (4 − 9 = −5, −5 + 12 = 7)  (d) Monday (100 mod 7 = 2, Saturday + 2)  (e) Thursday (30 mod 7 = 2, Saturday back 2)  (the three “mod” sums are now in Think harder 4)'],
      ['Q2', '(a) WPGGH  (b) CODE IS FUN  (c) 16 (10 + 16 = 26)'],
      ['Q3', 'W: 22, 27, 1, B.  A: 0, 5, 5, F.  Y: 24, 29, 3, D.  The program says BFD.'],
      ['Q4', '(a) BPM, probably THE  (b) 8 (T = 19, 19 + 8 = 27, 27 mod 26 = 1 = B)  (c) THE (the first word). The whole message, THE KEY IS UNDER THE MAT, is now in Think harder 4.'],
      ['Q5', '(a) 15  (b) 5 (31 mod 26)  (c) He gets the original message back: 9 + 17 = 26, a full turn  (d) 13 (13 + 13 = 26)']
    ]
  },

  script: {
    hook: ['Today you are code-breakers. Spies, generals and computers all hide messages with codes. The oldest one we know is over 2000 years old, and it runs on the same maths as a clock.', 'Notice it. Test it. Explain why. Today “test it” means: crack it, then let the computer check.'],
    warmIntro: ['Look at the clock. It is 9 o’clock. What time will it be 4 hours later? How did you work it out?', 'Now 11 o’clock and 13 hours later. Did you go past 12? What happened?'],
    predict: ['With a shift of 3, A becomes D and B becomes E. What do you think Z becomes? Write your guess before you make the strip.'],
    exploreHints: ['Stuck making the strip: write A to Z on one line. Underneath, start at D under A, and keep going.', 'Stuck at the end of the alphabet: “After Z, where does the bottom row carry on?”', 'Finished early: invent a shift, code a short message for your partner, and give them only one clue.'],
    think: ['“It is 9 o’clock. I count on 5 hours: 10, 11, 12, 1, 2. Adding gives 14, but a clock wraps round after 12, so 14 − 12 = 2. In maths we write 14 mod 12 = 2: the remainder when 14 is divided by 12.”', '“To code Z with shift 5: Z is 25. 25 + 5 = 30. There is no letter 30, so I wrap round: 30 − 26 = 4, and 4 is E.”', '“To decode A with shift 4: A is 0. 0 − 4 = −4. Below zero, so I add 26: −4 + 26 = 22, and 22 is W.”'],
    circulate: ['Ask: “What number is that letter? Did you start at A = 0?”', 'Ask: “Your number went past 25. What do you do?”', 'Ask: “How can you check your code? Decode it again and see if you get back the message.”'],
    hints: ['Hint 1: “Change each letter to its number first. Use the strip.”', 'Hint 2: “Add the shift. If you go past 25, take away 26.”', 'Hint 3: “To decode, take away the shift. If you go below 0, add 26.”'],
    talk: ['“Why does a shift of 26 change nothing?”', '“Ali says decoding shift 3 is the same as coding again with shift 23. Is he right? Why?”'],
    talkAns: 'A shift of 26 moves every letter once round the whole 26-letter clock, so each letter lands back on itself (26 mod 26 = 0). Ali is right: shifting back 3 and shifting forward 23 land on the same letter, because 23 + 3 = 26 is a full turn. For example D (3): 3 − 3 = 0 = A, and 3 + 23 = 26, 26 mod 26 = 0 = A.',
    close: ['“Today you used clock arithmetic to make and break codes, and you made the computer do it for you. Mathematicians call this modular arithmetic, and it helps protect messages sent on the internet. Well done, code-breakers!”']
  },

  deck: {
    today: 'Use clock arithmetic (mod) to solve time and calendar puzzles, make and break secret codes, and build a code machine in Scratch.',
    warmGame: 'Clock jumps. The tutor shows a clock and calls a time and a jump (“9 o’clock, 4 hours later?”). Answer on whiteboards. Then jumps past 12, jumps backwards, and a day-of-the-week jump.',
    warmQs: [['17 ÷ 5: what is the remainder?', '2'], ['30 ÷ 7: what is the remainder?', '2'], ['26 ÷ 26: what is the remainder?', '0'], ['40 ÷ 12: what is the remainder?', '4'], ['Which of 7, 9, 10, 12 leave remainder 1 when divided by 3?', '7 and 10']],
    expSetup: ['Make a code strip: write A to Z. Underneath, write the alphabet again starting at D (A → D, B → E …).', 'Code your first name with shift 3. Swap with your partner and decode each other’s.', 'Decode the tutor’s message: PDWK LV IXQ', 'What happens to X, Y and Z? How do you decode: which way do you shift?'],
    expPic: 'two rows of letters: A to Z on top, and underneath the shift-3 row starting D, E, F … ending A, B, C, with X, Y and Z highlighted and arrows showing them wrap round to A, B, C.',
    expAsk: [['What do X, Y and Z become with shift 3?', 'A, B and C: after Z the alphabet wraps round to the start.'], ['How do you decode a shift-3 message?', 'Shift each letter back 3 (or forward 23). PDWK LV IXQ is MATH IS FUN.'], ['What does a shift of 26 do?', 'Nothing: every letter goes once round and lands on itself.']],
    mini1: { head: 'Clock arithmetic: 9 o’clock + 5 hours', body: ['Count on 5: 10, 11, 12, 1, 2.', 'Adding gives 14. A clock wraps round after 12: 14 − 12 = 2.', '14 mod 12 = 2: the remainder when 14 is divided by 12.', 'Thursday + 45 days: 45 mod 7 = ?'], ans: '2 o’clock. 45 mod 7 = 3, so Sunday.' },
    mini2: { head: 'Caesar code: ZOO with shift 5', body: ['Letter numbers: Z = 25, O = 14.', 'Z: 25 + 5 = 30, 30 mod 26 = 4 = E.', 'O: 14 + 5 = 19 = T.', 'Decode AEB (shift 4): A = 0, 0 − 4 = −4, + 26 = 22 = W …'], ans: 'ZOO → ETT.  AEB → WAX.' },
    keyHead: 'Key idea: wrap round like a clock',
    keyBig: 'n mod m is the remainder when n is divided by m. On a clock with m numbers, counting past the end wraps round to the start.',
    keySmall: 'Caesar code: code number = (letter number + shift) mod 26. Decode: shift back (add 26 if you go below 0), or shift forward by 26 − shift.',
    brk: 'Clock arms. Your arm is the hour hand. The tutor calls a time and you point to it. Then “add 5 hours!” and you sweep your arm round to the new time. Try “add 12 hours!”',
    ws1: 'Page 1, in pairs: Q1 clock and calendar puzzles with mod, Q2 code and decode with a Caesar shift (test it in Scratch).',
    ws2: 'Page 2, on your own: Q3 trace the code machine in a table, Q4 crack a secret message, Q5 combine two shifts.'
  },

  moved: [
    { q: '(a) Work out 29 mod 12, 50 mod 7 and 100 mod 26. (b) Decode the whole message from Q4 (BPM SMG QA CVLMZ BPM UIB) with the shift you found.', a: '(a) 29 mod 12 = 5, 50 mod 7 = 1, 100 mod 26 = 22.  (b) THE KEY IS UNDER THE MAT.' }
  ],

  qbank: {
    core: [
      { q: 'It is 10 o’clock. What time will it be 5 hours later?', a: '3 o’clock (15 − 12 = 3)' },
      { q: 'A clock has 12 numbers. Start at 12 and move 20 hours forward. Where do you stop? (This is written 20 mod 12: the remainder when 20 is divided by 12.)', a: '8 o’clock (20 − 12 = 8, so 20 mod 12 = 8)' },
      { q: 'What is the remainder when 45 is divided by 7? Hint: count up in 7s.', a: '3 (45 = 6 × 7 + 3)' },
      { q: 'Today is Monday. What day will it be 10 days from today?', a: 'Thursday (10 mod 7 = 3; Monday + 3 days)' },
      { q: 'A secret code moves every letter one place along the alphabet: A becomes B, B becomes C, and so on. Code the word DOG. (Write the alphabet out to help you.)', a: 'EPH' },
      { q: 'Using the same code (every letter moves one place along), decode KBN. Move each letter one place back.', a: 'JAM' }
    ],
    stretch: [
      { q: 'The pattern CODECODECODE… goes on and on. What is the 100th letter?', a: 'E (100 mod 4 = 0, so the 100th letter is the 4th letter of CODE)' },
      { q: 'It is 10 o’clock now. What time will it be 1000 hours from now (on a 12-hour clock)?', a: '2 o’clock (1000 mod 12 = 4, and 10 + 4 = 14, 14 − 12 = 2)' },
      { q: 'Find the smallest number bigger than 10 that leaves a remainder of 3 when it is divided by 4 and also when it is divided by 5.', a: '23 (3 more than a multiple of 20: 23 = 5 × 4 + 3 = 4 × 5 + 3)' },
      { q: 'Decode BYFFI. It was made with a shift of 20.', a: 'HELLO (B = 1: 1 − 20 = −19, + 26 = 7 = H; Y = 24 − 20 = 4 = E; F = 5 − 20 = −15, + 26 = 11 = L; I = 8 − 20 = −12, + 26 = 14 = O)' },
      { q: 'Today is Monday. What day will it be in 365 days? In 366 days?', a: 'Tuesday and Wednesday (365 = 52 × 7 + 1, 366 = 52 × 7 + 2)' },
      { q: 'Mei codes with a shift of 3. Ben codes with a shift of 29. Do their codes give the same answer? Why?', a: 'Yes: 29 mod 26 = 3, so a shift of 29 is a full turn (26) plus 3.' },
      { q: 'Work out 47 mod 12, 35 mod 12 and (47 + 35) mod 12. What do you notice?', a: '11, 11 and 10. Adding the remainders and taking mod 12 again gives the same answer: (11 + 11) mod 12 = 22 mod 12 = 10.' },
      { q: 'On a 24-hour clock it is 21:00. What time will it be 50 hours later?', a: '23:00 (50 mod 24 = 2, and 21 + 2 = 23)' }
    ],
    challenge: [
      { q: 'Mei makes a new code: multiply each letter number by 2, then take mod 26. Why can her friend not always decode it?', a: 'Two letters can give the same code letter: A (0) and N (13) both give 0 = A (13 × 2 = 26). So every code letter could stand for two different letters.' },
      { q: 'Ben’s code multiplies each letter number by 3, then takes mod 26. Code the word CAB. Do two letters ever get the same code letter?', a: 'GAD (C = 2 gives 6 = G, A = 0 gives 0 = A, B = 1 gives 3 = D). No: all 26 letters get different code letters, because 3 and 26 have no common factor.' },
      { q: 'Crack this Caesar code. Hint: a one-letter word is usually A or I.   X ADKT BPIWH', a: 'I LOVE MATHS (X = 23 is I = 8, so the shift is 15)' },
      { q: 'Find the smallest number that leaves a remainder of 2 when it is divided by 3, by 4 or by 5, and is a multiple of 7.', a: '182 (it is 2 more than a multiple of 60: 62, 122, 182, and 182 = 7 × 26). The smaller numbers 2, 62 and 122 are not multiples of 7.' },
      { q: 'Ali goes to the library every 4th day and Mei every 6th day. They are both there on Day 0, a Monday. On which day of the week do they next meet? And on which day of the week is their 5th meeting after Day 0?', a: 'They next meet on Day 12 (the smallest number in both the 4 and 6 times tables), and 12 mod 7 = 5, so it is a Saturday. Their 5th meeting after Day 0 is on Day 60, and 60 mod 7 = 4, so it is a Friday.' },
      { q: 'Ali codes a message with a shift of k, then codes the result again with the same shift k. It is the same as one shift of 6. What could k be? Find every answer from 0 to 25.', a: '3 or 16 (3 + 3 = 6; 16 + 16 = 32 and 32 mod 26 = 6)' },
      { q: 'Write your own secret message of at least 8 letters and code it with a shift of your choice. Write clear instructions telling a friend how to decode it, and explain how a friend could crack it without being told the shift. Swap and decode.', a: 'Open. Check the code by decoding it, and that the cracking idea is sensible: try every shift from 1 to 25, or use the commonest letter (often E) or a short word (A or I). Example: MEET AT SIX with a shift of 3 is PHHW DW VLA.' },
      { q: 'Ali codes a message with a shift of 7. Mei codes Ali’s result with another shift. The final message is the same as the original coded with a shift of 2. What shift did Mei use?', a: '21 (7 + 21 = 28, and 28 mod 26 = 2)' },
      { q: 'Start at 12 on a clock and keep jumping forward 5 hours. Do you land on every number before you get back to 12? What about jumps of 4 hours?', a: 'Jumps of 5: yes, all 12 numbers (5, 10, 3, 8, 1, 6, 11, 4, 9, 2, 7, 12). Jumps of 4: no, only 4, 8 and 12, because 4 shares a factor with 12.' }
    ]
  },

  workbook: H => {
    const loop = [['var', 'set {n} to {(item # of (letter) in alphabet) − 1}'], ['var', 'set {m} to {(n + shift) mod 26}'], ['var', 'set {code} to {join (code) (item (m + 1) of alphabet)}']];
    const w3 = [1800, 1700, 1800, 2700, 1900];
    const t3 = H.tbl(w3, [H.row(['Letter', 'n', 'n + 5', 'm = (n + 5) mod 26', 'Code letter'].map((s, i) => H.cell(s, w3[i], { bold: true, fill: 'D9D9D9', size: 22, h: 45 }))),
      ...['W', 'A', 'Y'].map(l => H.row([H.cell(l, w3[0], { bold: true, size: 24, h: 60 }), ...[1, 2, 3, 4].map(i => H.cell('', w3[i], { h: 60 }))]))]);
    return [
      H.p('Letter numbers (we start at A = 0). Use them for every code question in this lesson.', { after: 10 }),
      H.fig(strip()),
      H.q(1, 'Clock and calendar puzzles. A clock wraps round after 12; a week wraps round after 7 days.', { before: 40, keepNext: true }),
      H.sub('a', 'It is 8 o’clock. 7 hours later it is  ______ o’clock.      (b)  It is 11 o’clock. 30 hours later (count 12 hours at a time):  ______ o’clock.', { after: 60 }),
      H.sub('c', 'It is 4 o’clock. 9 hours ago it was  ______ o’clock.      (d)  Today is Saturday. In 100 days:  __________ .', { after: 60 }),
      H.sub('e', 'Today is Saturday. 30 days ago it was  __________ .', { after: 60 }),
      H.q(2, 'Caesar codes. Code number = (letter number + shift) mod 26. Test your answers in Scratch (type the message in capital letters; the starter keeps the spaces).', { keepNext: true }),
      H.sub('a', 'Code the word PIZZA with a shift of 7.      ______________________', { after: 60 }),
      H.sub('b', 'Decode this message. It was made with a shift of 10:   MYNO SC PEX      ______________________', { after: 60 }),
      H.sub('c', 'Ben wants to decode shift 10 by shifting FORWARD instead. Which shift should he use?   ______'),
      pyBox(H),

      H.q(3, 'Trace the code. The Scratch code machine has a list called alphabet (item 1 is A). For each letter of the message WAY, with shift = 5, it does these three blocks:', { pb: true, before: 0, keepNext: true }),
      H.fig(codeFig(loop, 'Three blocks: set n to (item number of the letter in alphabet) minus 1; set m to (n + shift) mod 26; set code to join code and item (m + 1) of alphabet.')),
      t3,
      H.sub('a', 'At the end the program says the code. What does it say?   ______________'),
      H.q(4, 'Crack the code. Mei found this message. It was made with a Caesar shift, but she does not know which one.', { keepNext: true }),
      H.p('BPM  SMG  QA  CVLMZ  BPM  UIB', { after: 30, align: 'center', size: 30, bold: true }),
      H.sub('a', 'Which 3-letter word appears twice?  ________   What English word could it be?  ________', { after: 60 }),
      H.sub('b', 'If you are right, what shift turns T into B?  ______', { after: 60 }),
      H.sub('c', 'Decode the first word of the message with that shift:   ____________'),
      H.q(5, 'Two shifts in a row. Shifts add up like jumps on a 26-hour clock. (Example: shift 2 then shift 3 moves A to C to F, the same as shift 5.)', { keepNext: true }),
      H.sub('a', 'Shift 6, then shift 9 is the same as one shift of  ______ .      (b)  Shift 19, then shift 12:  one shift of  ______ .', { after: 60 }),
      H.sub('c', 'Ben codes a message with shift 9, then codes the result with shift 17. What does he get? Why?', { after: 20 }), ...H.lines(1),
      H.sub('d', 'Which shift (not 0), used twice, always gives back the original message?   ______')
    ];
  }
};
