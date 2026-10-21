// Math Inquirers P6 — Lesson 5: Every Possible Way (counting / combinatorics; nested loops that list every case)
// Every counting answer below was enumerated by a program and checked by hand.

const NAVY = '#1B2A49', YEL = '#FFC93C', SKY = '#DDEBF7', TEAL = '#1F7A6F', RED = '#D64545', WHITE = '#FFFFFF';
const escx = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

// Code blocks in our own simple style: [kind, text, children?, elseChildren?]
// kinds: hat (start block), ctrl (repeat / if), var (set / change), look (say). [text] = a white value pill, [?] = an empty gap.
const BK = { hat: [RED, WHITE], ctrl: [YEL, NAVY], var: [TEAL, WHITE], look: [SKY, NAVY] };
function blocks(nodes, label, fs = 15) {
  const h = Math.round(fs * 1.9), step = Math.round(fs * 1.2), cw = fs * 0.58, F = 'Arial, sans-serif';
  const segs = t => t.split(/(\[[^\]]*\])/).filter(s => s.trim() !== '');
  const pillW = c => c === '?' ? fs * 5 : c.length * cw + fs;
  const textW = t => segs(t).reduce((w, s) => w + (s[0] === '[' ? pillW(s.slice(1, -1)) : s.trim().length * cw) + fs * 0.35, 0);
  const out = []; let maxX = 0;
  const txt = (x, y, t, fg) => {
    let cx = x, s = '';
    for (const g of segs(t)) {
      if (g[0] === '[') {
        const c = g.slice(1, -1), w = pillW(c), ph = h - 9;
        s += `<rect x="${cx.toFixed(1)}" y="${(y - ph / 2).toFixed(1)}" width="${w.toFixed(1)}" height="${ph}" rx="${ph / 2}" fill="${WHITE}" stroke="${NAVY}" stroke-width="1.5"${c === '?' ? ' stroke-dasharray="4 3"' : ''}/>`;
        if (c !== '?') s += `<text x="${(cx + w / 2).toFixed(1)}" y="${(y + fs * 0.36).toFixed(1)}" font-size="${fs}" font-weight="700" text-anchor="middle" fill="${NAVY}" font-family="${F}">${escx(c)}</text>`;
        cx += w + fs * 0.35;
      } else {
        const t2 = g.trim();
        s += `<text x="${cx.toFixed(1)}" y="${(y + fs * 0.36).toFixed(1)}" font-size="${fs}" font-weight="700" fill="${fg}" font-family="${F}">${escx(t2)}</text>`;
        cx += t2.length * cw + fs * 0.35;
      }
    }
    maxX = Math.max(maxX, cx); return s;
  };
  const lay = (list, x, y) => {
    for (const [kind, text, kids, els] of list) {
      const [bg, fg] = BK[kind]; const w = Math.max(textW(text) + fs * 1.2, fs * 5);
      if (!kids) {
        out.push(`<rect x="${x}" y="${y}" width="${w.toFixed(1)}" height="${h}" rx="${kind === 'hat' ? fs * 0.9 : 5}" fill="${bg}" stroke="${NAVY}" stroke-width="2"/>` + txt(x + fs * 0.6, y + h / 2, text, fg));
        maxX = Math.max(maxX, x + w); y += h;
      } else {
        const y0 = y, idx = out.length; out.push('');
        let labels = txt(x + fs * 0.6, y0 + h / 2, text, fg); y += h; y = lay(kids, x + step, y);
        let yE = null; if (els) { yE = y; labels += txt(x + fs * 0.6, y + h / 2, 'else', fg); y += h; y = lay(els, x + step, y); }
        const hb = Math.round(h * 0.55), wb = fs * 5;
        const pts = [[x, y0], [x + w, y0], [x + w, y0 + h], [x + step, y0 + h]];
        if (els) pts.push([x + step, yE], [x + wb, yE], [x + wb, yE + h], [x + step, yE + h]);
        pts.push([x + step, y], [x + wb, y], [x + wb, y + hb], [x, y + hb]);
        out[idx] = `<polygon points="${pts.map(p => p.map(v => (+v).toFixed(1)).join(',')).join(' ')}" fill="${bg}" stroke="${NAVY}" stroke-width="2" stroke-linejoin="round"/>` + labels;
        y += hb; maxX = Math.max(maxX, x + w);
      }
    }
    return y;
  };
  const Hh = Math.ceil(lay(nodes, 2, 2) + 2), W = Math.ceil(maxX + 4);
  return `<svg aria-label="${escx(label)}" viewBox="0 0 ${W} ${Hh}" xmlns="http://www.w3.org/2000/svg" style="width:${W}px;max-width:100%">${out.join('')}</svg>`;
}
// optional Python version in a small dashed box
function pyBox(lines, title) {
  const lh = 17, W = 380, Hh = 58 + lines.length * lh;
  let s = `<svg aria-label="${escx(title.replace('|', ' '))}" viewBox="0 0 ${W} ${Hh}" xmlns="http://www.w3.org/2000/svg" style="width:${W}px;max-width:100%"><rect x="2" y="2" width="${W - 4}" height="${Hh - 4}" rx="10" fill="${WHITE}" stroke="${NAVY}" stroke-width="2" stroke-dasharray="7 5"/>`;
  title.split('|').forEach((tl, i) => { s += `<text x="16" y="${25 + i * 19}" font-size="15" font-weight="700" fill="${TEAL}" font-family="Arial, sans-serif">${escx(tl)}</text>`; });
  lines.forEach((l, i) => { s += `<text x="16" y="${66 + i * lh}" font-size="14" fill="${NAVY}" font-family="Courier New, monospace" xml:space="preserve" style="white-space:pre">${escx(l)}</text>`; });
  return s + '</svg>';
}
const cards = ds => {
  let s = `<svg aria-label="Digit cards ${ds.join(', ')}" viewBox="0 0 240 60" xmlns="http://www.w3.org/2000/svg" style="width:240px;max-width:100%">`;
  ds.forEach((d, i) => { const x = 120 - ds.length * 30 + i * 60 + 4; s += `<rect x="${x}" y="4" width="52" height="52" rx="9" fill="${i % 2 ? SKY : YEL}" stroke="${NAVY}" stroke-width="3"/><text x="${x + 26}" y="42" font-size="30" font-weight="700" text-anchor="middle" fill="${NAVY}" font-family="Fredoka, Arial">${d}</text>`; });
  return s + '</svg>';
};
// 3 by 3 grid of streets, A bottom left, B top right, puddle at P (1 along, 1 up). Small circles at the corners to write in.
const grid = () => {
  const c = 48, x0 = 34, y0 = 26; let s = `<svg aria-label="A 3 by 3 grid of streets from A at the bottom left to B at the top right, with a puddle at point P" viewBox="0 0 230 204" xmlns="http://www.w3.org/2000/svg" style="width:230px;max-width:100%">`;
  for (let i = 0; i <= 3; i++) s += `<line x1="${x0}" y1="${y0 + i * c}" x2="${x0 + 3 * c}" y2="${y0 + i * c}" stroke="${NAVY}" stroke-width="4"/><line x1="${x0 + i * c}" y1="${y0}" x2="${x0 + i * c}" y2="${y0 + 3 * c}" stroke="${NAVY}" stroke-width="4"/>`;
  for (let i = 0; i <= 3; i++) for (let j = 0; j <= 3; j++) { const isP = i === 1 && j === 1; s += `<circle cx="${x0 + i * c}" cy="${y0 + (3 - j) * c}" r="15" fill="${isP ? SKY : WHITE}" stroke="${NAVY}" stroke-width="2.5"/>`; }
  s += `<text x="${x0 - 30}" y="${y0 + 3 * c + 30}" font-size="22" font-weight="700" fill="${TEAL}" font-family="Arial">A</text><text x="${x0 + 3 * c + 12}" y="${y0 - 8}" font-size="22" font-weight="700" fill="${TEAL}" font-family="Arial">B</text>`;
  s += `<text x="${x0 + c + 18}" y="${y0 + 2 * c + 32}" font-size="18" font-weight="700" fill="${NAVY}" font-family="Arial">P</text>`;
  return s + '</svg>';
};

const listCode = [['hat', 'when start clicked'], ['var', 'set a to [1]'], ['ctrl', 'repeat [3]', [['var', 'set b to [1]'], ['ctrl', 'repeat [4]', [['look', 'say [join a b] for 1 seconds'], ['var', 'change b by [1]']]], ['var', 'change a by [1]']]]];
const planCode = [['hat', 'when start clicked'], ['var', 'set count to [0]'], ['var', 'set a to [1]'], ['ctrl', 'repeat [?]', [['var', 'set b to [1]'], ['ctrl', 'repeat [?]', [['ctrl', 'if [?] then', [['var', 'change count by [1]']]], ['var', 'change b by [1]']]], ['var', 'change a by [1]']]], ['look', 'say count']];

module.exports = {
  lesson: {
    n: 5, week: 3, session: 'A', title: 'Every Possible Way', topic: 'Counting',
    objective: 'Count every possible case without missing one or counting one twice: list in order, use the multiplication rule for choices made one after another, take care with order and with 0 in digit puzzles, count handshakes and grid routes, and test each count with nested loops in code.',
    skills: 'Systematic listing, the multiplication rule, avoiding double counting, adding as you go (grid routes), tracing and planning nested loops',
    materials: 'Laptop or desktop with Scratch 3 (scratch.mit.edu) open, the starter project “Every Order” (one loop that says each tea), mini whiteboards, digit cards 0 to 9, squared paper.',
    online: 'Children share their screen when they test code. The tutor shares the starter project link in the chat. Digit cards can be cut from paper. Breakout rooms in pairs for the Explore.',
    warmup: 'Count it, don’t list it: six quick counting puzzles (pages 15 to 40, lamp posts, numbers with a 7 in them …). Teams race to answer each one and must say how they counted.',
    explore: 'The bubble tea shop: 3 teas and 2 toppings. Pairs list every order on paper, then predict how many there are when sizes M and L are added. At the computer, they add a second loop inside the starter project so the sprite says every order.',
    mini: 'Fix the first choice and run through every second choice: a tree shows why 3 shirts and 2 shorts make 3 × 2 = 6 outfits. A nested loop does the same thing: the inner loop runs all the way round for each turn of the outer loop. When order does not matter (handshakes), each pair is counted twice, so halve, or let the code keep only a < b.',
    share: 'Why does the multiplication rule work for outfits, but 5 × 5 gives the wrong answer for handshakes between 5 friends?',
    exit: { q: 'Six friends meet. Every pair of friends shakes hands once. How many handshakes are there? Show how you know.', a: '15 (5 + 4 + 3 + 2 + 1, or 6 × 5 ÷ 2).' },
    mistakes: ['Adding the choices instead of multiplying them (4 T-shirts and 3 shorts gives 7 outfits).', 'Counting each handshake twice (7 × 6 = 42) or letting a person shake their own hand.', 'Digit cards: putting 0 at the front of a number, or using the same card twice.'],
    extension: 'Write a program that counts every 3-digit number whose digits add up to 5 (three loops, one inside another). Then change 5 to other totals: which total gives the most numbers?',
    key: [
      ['Q1', '(a) 12 (4 × 3)  (b) 24 (4 × 3 × 2)  (c) 2 extra pairs: with 5 pairs, 4 × 5 × 2 = 40; with 4 pairs only 4 × 4 × 2 = 32.'],
      ['Q2', '(a) 9 (3 choices for the tens, as 0 cannot go first, then 3 for the ones: 3 × 3): 30, 35, 38, 50, 53, 58, 80, 83, 85  (b) 18 (3 × 3 × 2)'],
      ['Q3', '(a) a 1, b 1: 11;  1, 2: 12;  1, 3: 13;  1, 4: 14;  2, 1: 21;  2, 2: 22  (b) 12 (3 × 4)  (c) 34  (d) 20 (5 × 4)'],
      ['Q4', '(a) 21 (6 + 5 + 4 + 3 + 2 + 1)  (b) Every handshake has been counted twice, once for each person: 42 ÷ 2 = 21.  (c) 10 people (9 + 8 + … + 1 = 45, or 10 × 9 ÷ 2 = 45)'],
      ['Q5', '(a) 20 (corner numbers, bottom row up: 1 1 1 1 / 1 2 3 4 / 1 3 6 10 / 1 4 10 20)  (b) 8 (put 0 at P: 1 1 1 1 / 1 0 1 2 / 1 1 2 4 / 1 2 4 8). 12 routes go through P.'],
      ['Q6', 'Gaps: repeat 7, repeat 7, if a < b (a > b also works: either keeps each pair once).  (a) 21, the same as Q4(a); the “if” is checked 7 × 7 = 49 times.  (b) It says 7: it counts each person with themselves (a = b), which is not a handshake.']
    ]
  },

  script: {
    hook: ['Welcome back, inquirers! Today’s question sounds easy: how many ways? But counting every possible way, with none missing and none counted twice, is a skill that mathematicians and programmers use every day.', 'By the end of today you will make the computer list every case for you, and you will know when its answer is right.'],
    warmIntro: ['Six puzzles. Do not list them all: find a quick way to count, and be ready to say how you counted.', 'First one: a book, pages 15 to 40. How many pages? Careful, it is not 25!'],
    predict: ['The bubble tea shop has 3 teas and 2 toppings. Before you list them, write your guess: how many different orders? Now the shop adds sizes M and L. Will the number of orders go up by 2, or double, or something else? Write a prediction.'],
    exploreHints: ['Stuck listing: write the first tea, then every topping with it. Then the next tea.', 'Code stuck: drag a second repeat block INSIDE the first one. Which loop should say the topping?', 'Finished early: add sugar levels 0%, 50% and 100%. Predict the number of orders first, then add a third loop to test it.'],
    think: ['“3 shirts and 2 pairs of shorts. I fix the red shirt and try every pair of shorts: red with black, red with grey. That is 2. Every shirt gets the same 2, so 3 shirts give 3 groups of 2: 3 × 2 = 6. Add 2 caps: each of the 6 outfits splits into 2, so 12.”', '“In code, the outer loop picks the shirt and the inner loop picks the shorts. The inner loop goes all the way round for EACH shirt, so the say block runs 3 × 2 = 6 times.”', '“5 friends shaking hands. Friend A shakes 4 hands. B has already shaken A’s, so 3 new ones. C: 2 new. D: 1 new. E: none left. 4 + 3 + 2 + 1 = 10. Or: 5 people times 4 hands is 20, but each handshake has two people in it, so I counted every one twice: 20 ÷ 2 = 10.”'],
    circulate: ['Ask: “Which choice did you fix first? How do you know you have them all?”', 'Ask: “Point to the inner loop. How many times does it run for one turn of the outer loop?”', 'Ask: “Have you counted any pair twice? Has anyone shaken their own hand?”'],
    hints: ['Hint 1: “Fix the first choice, then run through every second choice.”', 'Hint 2: “Draw a tree, or a table with a row for each first choice.”', 'Hint 3: “If the order does not matter, has your method counted each pair twice?”'],
    talk: ['“Why does the multiplication rule work for outfits, but 5 × 5 gives the wrong answer for handshakes between 5 friends?”', '“How would you change a program that lists every pair so that it lists each handshake once?”'],
    talkAns: 'For outfits, every shirt goes with every pair of shorts and a shirt-and-shorts outfit is different from any other, so 3 × 2 counts each outfit once. For handshakes, 5 × 5 = 25 includes each person with themselves (5 cases) and counts A with B and B with A as two, so 25 − 5 = 20 and 20 ÷ 2 = 10. In code, keep only the pairs with a < b.',
    close: ['“Today you counted things that would take ages to list: you fixed one choice, multiplied, and halved when you counted twice. Then the computer listed every case to test you. Notice it, test it, explain why.”']
  },

  deck: {
    today: 'Count every possible way without missing one or counting one twice, use the multiplication rule, and make nested loops list every case for us.',
    warmGame: 'Count it, don’t list it. Six quick counting puzzles (pages 15 to 40, two-digit numbers, multiples of 5, lamp posts, numbers with a 7, even numbers). Teams race and must say how they counted.',
    warmQs: [['3 × 4 × 2 = ?', '24'], ['1 + 2 + 3 + … + 10 = ?', '55'], ['How many whole numbers from 100 to 999?', '900'], ['6 × 5 ÷ 2 = ?', '15'], ['repeat 5 { repeat 2 { say hi } }: how many his?', '10']],
    expSetup: ['A bubble tea shop has 3 teas (milk, green, taro) and 2 toppings (pearls, jelly).', 'On paper, list every order of 1 tea and 1 topping. How do you know you have them all?', 'The shop adds sizes M and L. Predict how many orders now, then check.', 'At the computer: open “Every Order” and put a second loop inside the first so the sprite says every order.'],
    expPic: 'the menu board: three tea cups (milk, green, taro), two toppings (pearls, jelly) and sizes M and L, next to the starter code (repeat 3: say tea, change tea by 1).',
    expAsk: [['How many orders with 3 teas and 2 toppings? With sizes M and L too?', '6 orders; with sizes, 12 (each of the 6 orders comes in 2 sizes: 6 × 2).'], ['How did you make sure you had every order, with none twice?', 'Fix the tea, go through every topping, then move to the next tea: a list in order, like a tree.'], ['In your code, which loop goes round faster?', 'The inner loop: it runs all the way round (2 toppings) for every single turn of the outer loop (each tea).']],
    mini1: { head: 'The multiplication rule: 3 shirts and 2 pairs of shorts', body: ['Fix a shirt, then try every pair of shorts: 2 outfits for each shirt.', '3 shirts give 3 groups of 2: 3 × 2.', 'Add 2 caps: each outfit splits into 2.'], ans: '6 outfits; with caps, 6 × 2 = 12.' },
    mini2: { head: 'Handshakes: 5 friends, every pair shakes once', body: ['A shakes 4 new hands, B 3 new, C 2, D 1, E 0.', 'Or: 5 × 4 = 20 counts every handshake twice.', 'In code: check every pair (a, b) and keep only a < b.'], ans: '4 + 3 + 2 + 1 = 10, or 20 ÷ 2 = 10 handshakes.' },
    keyHead: 'Key idea: every case, exactly once',
    keyBig: 'Work in order: fix the first choice and run through every second choice. Choices made one after another multiply.',
    keySmall: 'A nested loop does the same: the inner loop runs all the way round for each turn of the outer loop. If order does not matter, check you have not counted each pair twice.',
    brk: 'Every possible pose: arms up or arms out (2), and standing, squatting or on one leg (3). That is 2 × 3 = 6 poses. The tutor calls a number from 1 to 6 and everyone does that pose.',
    ws1: 'Page 1, in pairs: Q1 outfits, Q2 digit cards, Q3 trace the nested loop.',
    ws2: 'Page 2, on your own: Q4 handshakes, Q5 routes on a grid, Q6 plan the handshake program.'
  },

  qbank: {
    core: [
      { q: 'A shop sells 3 shirts and 5 pairs of trousers. How many different outfits of 1 shirt and 1 pair of trousers can you make?', a: '15 (3 × 5)' },
      { q: 'List every 2-digit number you can make from the cards 4, 6 and 9, using each card at most once.', a: '6 numbers: 46, 49, 64, 69, 94, 96' },
      { q: '4 friends meet. Every pair shakes hands once. How many handshakes?', a: '6 (3 + 2 + 1)' },
      { q: 'How many times does this say “hi”?  repeat 4 { repeat 6 { say hi } }', a: '24 (4 × 6)' },
      { q: 'A grid is 3 squares wide and 1 square tall. How many routes go from the bottom left corner to the top right corner, going only right or up?', a: '4 (go up at one of the 4 lines across)' },
      { q: 'A lock has 2 dials. Each dial shows a digit from 0 to 9. How many different codes are there?', a: '100 (10 × 10: 00 to 99)' }
    ],
    stretch: [
      { q: 'A set lunch is 1 main, 1 drink and 1 dessert. There are 4 mains and 3 drinks. There are 60 different set lunches. How many desserts are there?', a: '5 (4 × 3 = 12 and 60 ÷ 12 = 5)' },
      { q: 'How many 3-digit numbers can you make from the cards 1, 2, 3 and 4, using each card at most once? How many of them are even?', a: '24 (4 × 3 × 2); 12 are even (the last card is 2 or 4: 2 choices, then 3 × 2 for the others)' },
      { q: 'In a league of 6 teams, every team plays every other team twice (once at home, once away). How many matches are played?', a: '30 (6 × 5: each ordered pair is one home match)' },
      { q: 'A 4-digit PIN uses only the digits 1, 2 and 3. Digits may repeat. How many PINs are there?', a: '81 (3 × 3 × 3 × 3)' },
      { q: 'A hexagon has 6 corners. How many diagonals does it have?', a: '9 (6 corners make 6 × 5 ÷ 2 = 15 lines; 6 of them are sides, so 9 are diagonals)' },
      { q: 'How many rectangles of any size can you find in a strip of 4 squares in a row?', a: '10 (4 of length 1, 3 of length 2, 2 of length 3, 1 of length 4)' },
      { q: '5 children line up for a photo. In how many different orders can they stand? In how many of these is Ali at the front?', a: '120 (5 × 4 × 3 × 2 × 1); 24 with Ali at the front (4 × 3 × 2 × 1)' },
      { q: 'How many routes go from one corner of a grid 4 squares wide and 2 squares tall to the opposite corner, going only right or up?', a: '15' }
    ],
    challenge: [
      { q: 'How many different triangles can you make by joining 3 of the 5 corners of a pentagon?', a: '10' },
      { q: 'How many 2-digit numbers have two different digits?', a: '81 (90 two-digit numbers, minus the 9 with both digits the same: 11, 22, …, 99)' },
      { q: 'How many digits are printed to number the pages of a book from page 1 to page 120?', a: '252 (9 one-digit + 90 × 2 + 21 × 3 = 9 + 180 + 63)' },
      { q: 'An ice cream shop has 6 flavours. A cup has 2 different flavours, and the order does not matter. How many different cups are there?', a: '15 (6 × 5 ÷ 2)' },
      { q: '4 friends each send a card to every other friend. How many cards are sent?', a: '12 (4 × 3: here A to B and B to A are different cards)' },
      { q: 'How many squares of any size are there on a 3 by 3 grid of squares?', a: '14 (9 small, 4 of size 2 by 2, 1 of size 3 by 3)' },
      { q: 'How many routes go from one corner of a 4 by 4 grid of squares to the opposite corner, going only right or up?', a: '70 (add as you go: the corner numbers on the diagonal row are 1, 4, 10, 20, 35, then 70)' },
      { q: 'A set of dominoes has one domino for every pair of spot numbers from 0 to 6, including doubles such as 3 | 3. How many dominoes are in the set?', a: '28 (7 doubles, plus 6 + 5 + 4 + 3 + 2 + 1 = 21 with two different numbers)' },
      { q: 'How many 3-digit numbers have digits that add up to 5? (For example, 203.)', a: '15 (first digit 1: 5 numbers, 2: 4, 3: 3, 4: 2, 5: 1; they are 104, 113, 122, 131, 140, 203, 212, 221, 230, 302, 311, 320, 401, 410, 500)' }
    ]
  },

  workbook: H => {
    const tx = h => '<div style="text-align:left;font-size:16px;line-height:1.5">' + h + '</div>';
    const L = t => '<b style="color:#1F7A6F">' + t + '</b> ';
    const blank = w => '<span style="display:inline-block;width:' + w + 'px;border-bottom:2px dotted #8A94AD"></span>';
    const traceW = [1100, 1100, 2100];
    const trace = H.tbl(traceW, [H.row(['a', 'b', 'Sprite says'].map((s, i) => H.cell(s, traceW[i], { bold: true, fill: 'D9D9D9', h: 50 }))), ...[1, 2, 3, 4, 5, 6].map(() => H.row(traceW.map(w => H.cell('', w, { h: 165 }))))]);
    const codeAndTrace = H.tbl([5300, 4600], [H.row([
      H.cell('<div style="text-align:left">' + blocks(listCode, 'Code: set a to 1, repeat 3 times: set b to 1, repeat 4 times: say join a b, change b by 1; then change a by 1', 14) + '</div>', 5300, { h: 40 }),
      H.cell('<div>' + trace + tx(L('(b)') + 'How many things does it say altogether? ' + blank(50) + '<br>' + L('(c)') + 'The last thing it says? ' + blank(50) + '<br>' + L('(d)') + 'If “repeat 3” becomes “repeat 5”, how many things will it say? ' + blank(50)) + '</div>', 4600, { h: 30 })])]);
    const py = pyBox(['teas = ["milk", "green", "taro"]', 'toppings = ["pearls", "jelly"]', 'count = 0', 'for tea in teas:', '    for top in toppings:', '        print(tea, "tea with", top)', '        count = count + 1', 'print(count, "orders")'], 'Python corner (optional): our Explore|program. Change the lists to test Q1.');
    const planAndPy = H.tbl([4200, 5700], [H.row([
      H.cell('<div style="text-align:left">' + blocks(planCode, 'Plan with gaps: set count to 0, set a to 1, repeat a gap: set b to 1, repeat a gap: if a gap then change count by 1; change b by 1; change a by 1; say count', 13) + '</div>', 4200, { h: 30 }),
      H.cell('<div>' + tx(L('(a)') + 'What will the program say? ' + blank(50) + '<br>Does it agree with Q4(a)? ' + blank(50) + '<br>' + L('(b)') + 'If the test is changed to <b>a = b</b>, what will it say? What is it counting now?<br>' + blank(330) + '<br>') + py + '</div>', 5700, { h: 30 })])]);
    const routes = H.tbl([3600, 6300], [H.row([H.cell('<div>' + grid() + '</div>', 3600, { h: 20 }), H.cell(tx('Write in each circle the number of routes from A to it. A gets 1. Each other circle = the number on its left + the number below it.<br>' + L('(a)') + 'How many routes go from A to B? ' + blank(60) + '<br>' + L('(b)') + 'A puddle covers the blue point P. Do it again with 0 at P. How many routes avoid P? ' + blank(60)), 6300, { h: 40 })])]);
    return [
      H.q(1, 'Mei packs 4 T-shirts, 3 pairs of shorts and 2 caps for camp.', { before: 20, keepNext: true }),
      H.sub('a', 'Outfits of 1 T-shirt and 1 pair of shorts: how many?  _____    (b)  With a cap too?  _____'),
      H.sub('c', 'Mei wants at least 40 outfits with a cap. What is the fewest number of extra pairs of shorts she must buy? Show how you know.', { keepNext: true }),
      ...H.lines(1),
      H.q(2, 'Digit cards. Use each card at most once in a number. A number cannot start with 0.', { keepNext: true }),
      H.tbl([3300, 6600], [H.row([H.cell('<div>' + cards([0, 3, 5, 8]) + '</div>', 3300, { h: 20 }), H.cell(tx(L('(a)') + 'How many 2-digit numbers can you make? ' + blank(50) + '<br>List them from smallest to largest:<br>' + blank(420) + '<br>' + L('(b)') + 'How many 3-digit numbers? Write the multiplication. ' + blank(110)), 6600, { h: 30 })])]),
      H.q(3, 'Trace the code. (a) Fill in a, b and what the sprite says, for the first 6 things it says.', { keepNext: true }),
      codeAndTrace,

      H.q(4, 'Seven friends meet. Every pair of friends shakes hands once.', { pb: true, before: 0, keepNext: true }),
      H.sub('a', 'How many handshakes are there? Show your list or your method.', { keepNext: true }),
      ...H.lines(1),
      H.sub('b', 'Ali says, “Each person shakes 6 hands, so 7 × 6 = 42 handshakes.” What is wrong? Fix it.', { keepNext: true }),
      ...H.lines(1),
      H.sub('c', 'Another party has 45 handshakes. How many people are there?   ______'),
      H.q(5, 'Routes on a grid. Walk along the lines from A to B, going only right or up.', { keepNext: true }),
      routes,
      H.q(6, 'Plan your code. Fill in the 3 gaps so the program counts the handshakes for the 7 friends in Q4. The test after “if” must keep each handshake once.', { keepNext: true }),
      planAndPy
    ];
  }
};
