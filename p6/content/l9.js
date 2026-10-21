// Math Inquirers P6 (post-PSLE maths + coding bridge) — Lesson 9: Data Detectives (averages and data; lists, adding up, mean)
// Every answer below was worked out by hand and checked (means computed exactly; Python programs run).

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
const codeSvg = (prog, aria) => { const b = blocks(prog); return `<svg aria-label="${esc(aria)}" viewBox="0 0 ${b.w} ${b.h}" xmlns="http://www.w3.org/2000/svg" style="width:${b.w}px;max-width:100%">${b.svg}</svg>`; };
const codeFig = (prog, aria, list) => {
  const b = blocks(prog);
  let extra = '', W = b.w, Hh = b.h;
  if (list) { const m = listMon(list[0], list[1], b.w + 40, 2); extra = m.s; W = b.w + 40 + m.w + 4; Hh = Math.max(Hh, m.h + 6); }
  return `<svg aria-label="${esc(aria)}" viewBox="0 0 ${W} ${Hh}" xmlns="http://www.w3.org/2000/svg" style="width:${W}px;max-width:100%">${b.svg}${extra}</svg>`;
};
const pyBox = (title, code) => `<div style="margin:0"><div style="border:2px solid ${TEAL};border-radius:10px;padding:6px 12px;background:#F3FAF8"><div style="font-weight:700;color:${TEAL};font-size:14px">${esc(title)}</div><pre style="margin:2px 0 0;font-family:'Courier New',monospace;font-size:11.5px;line-height:1.3;color:${NAVY}">${esc(code).replace(/\n/g, '&#10;')}</pre></div></div>`;

const PY_MEAN = `data = [3, 0, 4, 1, 2]        # goals in 5 matches
total = 0
for value in data:
    total = total + value
mean = total / len(data)
print("Total:", total)
print("Mean:", mean)
above = 0
for value in data:
    if value > mean:
        above = above + 1
print("Above the mean:", above)`;

const PY_WB = `data = [3, 0, 4, 1, 2]
total = 0
for value in data:
    total = total + value
mean = total / len(data)
print("Mean:", mean)`;

module.exports = {
  lesson: {
    n: 9, week: 5, session: 'A', title: 'Data Detectives', topic: 'Averages and Data',
    objective: 'Find the mean as total ÷ number of values and as levelling out, use total = mean × number of values to find a missing value, predict how changing the data changes the mean, compare the mean with the median and mode when one value is extreme, and build a list program that adds up the data and finds the mean.',
    skills: 'Mean, working back from a mean to a total, reasoning about change, median and mode, lists and loops in code, tracing code',
    materials: 'Laptop or desktop with Scratch 3 (scratch.mit.edu; free, in the browser), workbook, pencil, mini whiteboard, about 25 linking cubes or counters for levelling towers. A calculator only for checking.',
    online: 'Data is collected in the chat. Children share their screen to show their code. The tutor shares a starter project as an .sb3 file (one sprite with an empty list called data; children use File, Load from your computer) or children build it from the slide in 5 minutes. Block colours on our slides are simplified; in Scratch, find blocks by the category name on the left, not by colour. The mean is familiar from primary school; the new parts are lists and loops, median and mode, and misleading averages.',
    warmup: 'Quick-eye mean: the tutor flashes five numbers for 5 seconds; children write an estimate of the mean on a whiteboard; closest gets a point. Then five quick questions on the slide.',
    explore: 'Class data hunt: everyone posts the number of letters in their full name (no spaces). Estimate the mean, work it out by hand, then type the data into a Scratch list and run the mean program to check. Predict, then test: what happens to the mean when the tutor adds a value of 30?',
    mini: 'Mean = total ÷ how many. It is the level when the towers are evened out, so the amounts above and below it balance. Total = mean × how many, so a missing value = total − the known values. A new value above the mean pulls it up; a new value equal to the mean leaves it the same. One extreme value can make the mean misleading: the median (the middle value in order) or the mode (the most common value) may describe a typical value better. In code, a loop adds each item of the list to total, then we divide by the length of the list.',
    share: 'Can the mean be a number that nobody in the group has? Can the mean be bigger than every value in the list?',
    exit: { q: 'The mean of 3 numbers is 9. Two of them are 5 and 12. What is the third number? A fourth number, 13, is added. What is the new mean?', a: '10 (total 3 × 9 = 27; 27 − 5 − 12 = 10). New mean 10 (27 + 13 = 40, 40 ÷ 4 = 10).' },
    mistakes: ['Dividing by the wrong count: leaving out a value of 0, or forgetting the new value when one is added.', 'Finding a missing value from the MEAN instead of from the TOTAL (mean × how many) minus the known values.', 'Thinking the mean must be one of the values, or that it is always a typical value even when one value is extreme.'],
    extension: 'Make a list of 5 whole numbers with mean 10, median 8 and mode 7 (one answer: 7, 7, 8, 13, 15). Then change your program so it also finds the largest value in the list.',
    key: [
      ['Q1', '(a) 30  (b) 6  (c) −2, +1, −4, +2, +3; they add up to 0 (the values above and below the mean balance)'],
      ['Q2', '(a) 68 points (17 × 4)  (b) 19 (68 − 15 − 20 − 14)  (c) 22 (5 × 18 = 90, 90 − 68 = 22)'],
      ['Q3', '(a) stays the same: 10 (60 ÷ 6)  (b) goes up: 13  (c) goes down: 9 (36 ÷ 4)  (d) goes up: 16 (80 ÷ 5)'],
      ['Q4', '(a) $22 (154 ÷ 7)  (b) $15  (c) $12  (d) 6 pupils  (e) Not fair: the one $69 pulls the mean up, and 6 of the 7 pupils get less than $22. The median $15 describes a typical pupil better.'],
      ['Q5', 'Trace: i = 1, 2, 3, 4; item i = 5, 9, 6, 12; total = 5, 14, 20, 32.  (a) 8 (32 ÷ 4)  (b) repeat (length of scores) and say total ÷ (length of scores); it should now say 9 (45 ÷ 5)'],
      ['Q6', '(a) 31 °C (217 ÷ 7)  (b) 3 days (33, 32 and 34)  (c) Blank 1: mean.  Blank 2: count.  It says 3.']
    ]
  },

  script: {
    hook: ['Welcome back, data detectives! Newspapers, games and even your PSLE results come with averages. Today we find out what the mean really is, how one number can trick it, and how a computer adds up a whole list in a blink.', 'Our rule today: work it out by hand first, then let the code test it. Notice it. Test it. Explain why.'],
    warmIntro: ['Quick-eye mean! I will show five numbers for five seconds only. No working out: just write your best guess of the mean. Closest guess wins a point.', 'How did you guess so fast? Who looked for a number in the middle and checked that the big ones and small ones balance?'],
    predict: ['Before we add anything up: the mean number of letters in our names. Will it be bigger or smaller than the number of letters in YOUR name? Write a prediction.', 'If our tutor joins with a 30-letter name, will the mean go up a little or a lot? Thumbs up for a lot, sideways for a little.'],
    exploreHints: ['Stuck on the hand calculation: add the values two at a time and write each running total, just like the variable total in the code.', 'Code says something strange: check that every value is in the list once, and that you divide by the length of the list, not by a number you typed.', 'Finished early: find a new value you could add that keeps the mean exactly the same. Test it in the program.'],
    think: ['“Goals in 5 matches: 3, 0, 4, 1, 2. The 0 is a real value: that match counts. Total 3 + 0 + 4 + 1 + 2 = 10. Five matches, so the mean is 10 ÷ 5 = 2. Check by balancing: 3 is 1 above, 4 is 2 above: 3 above in all. 0 is 2 below, 1 is 1 below: 3 below in all. They balance, so 2 is right.”', '“The mean of 4 test scores is 15, so the total must be 4 × 15 = 60. The three I know make 12 + 18 + 14 = 44. The missing score is 60 − 44 = 16. I never subtract from the mean: I subtract from the total.”', '“Goals by 7 players: 1, 2, 2, 3, 4, 5, 25. The mean is 42 ÷ 7 = 6, but 6 of the 7 players scored fewer than 6! The one big value pulled the mean up. The median, the middle value in order, is 3. That describes a typical player better.”'],
    circulate: ['Ask: “What is the total? How many values are there? Did you count the 0?”', 'Ask: “Before you calculate: will the mean go up, go down or stay the same? Why?”', 'Ask: “Point to the block that adds up. What is total after the second time round the loop?”'],
    hints: ['Hint 1: “Find the total first. Mean × how many gives the total.”', 'Hint 2: “Draw the values as towers. Move cubes from tall towers to short ones until they are level.”', 'Hint 3: “For a trace table, do one loop at a time: which item? what is total now? then change i by 1.”'],
    talk: ['“Can the mean be a number that nobody in the group has?”', '“Can the mean be bigger than every value in the list? Why or why not?”'],
    talkAns: 'Yes: the mean of 2 and 3 is 2.5, a number nobody in the group has. No: the mean is always between the smallest and the largest value. Levelling out moves cubes from taller towers to shorter ones, so the level can never be higher than the tallest tower or lower than the shortest.',
    close: ['“Today you found means by levelling and by dividing, worked backwards from a mean to a total, and caught a misleading average. And your code added up a whole list for you. Next lesson is our Showcase Challenge: start thinking about a puzzle you would like to turn into a program.”', 'Homework thought for next lesson: decide which starter you will change (A, B, C or Clock Jumper) and what your twist will be, so you can start building straight away.']
  },

  deck: {
    today: 'Find the mean by levelling and by dividing, work back from a mean to a total, catch a misleading average, and make a program that finds the mean of a list.',
    warmGame: 'Quick-eye mean. The tutor flashes five numbers for 5 seconds. Write your best estimate of the mean, no working out. Closest guess wins a point. Three rounds.',
    warmQs: [['Find the mean of 4, 6 and 8.', '6'], ['Find the mean of 10, 20, 30 and 40.', '25'], ['5 children have a mean of 12 sweets. How many sweets altogether?', '60'], ['Find the mean of 3, 3, 3, 3 and 100.', '22.4'], ['Find the mean of 2.5 and 3.5.', '3']],
    expSetup: ['Everyone posts in the chat the number of letters in their full name (no spaces). Write the list.', 'Estimate the mean. Then work it out by hand: total ÷ how many.', 'Type the data into the Scratch list called data and run the mean program. Same answer?', 'Predict, then test: add a value of 30 to the list. What happens to the mean?'],
    expPic: 'a list panel called data holding the name-letter counts, an arrow to the mean program blocks (set total to 0, repeat length of data, change total by item i of data), and a yellow box saying mean = ?',
    expAsk: [['Was your estimate close? How did you estimate?', 'Pick a value in the middle, then check that the values above it and below it roughly balance.'], ['What happened to the mean when 30 was added?', 'It went up, a lot, because 30 is far above every other value. One big value pulls the mean towards it.'], ['Did the program and your hand calculation agree?', 'They should. If not, look for a value typed twice or missed, or dividing by the wrong number.']],
    mini1: { head: 'Find the mean, then balance-check', body: ['Goals in 5 matches: 3, 0, 4, 1, 2.', 'Total: 3 + 0 + 4 + 1 + 2 = 10. There are 5 values (the 0 counts).', 'Mean = 10 ÷ 5. Check: above the mean and below the mean should balance.'], ans: '2. Above: +1 and +2. Below: −2 and −1. They balance.' },
    mini2: { head: 'Missing value: use the total', body: ['The mean of 4 test scores is 15. Three of them are 12, 18 and 14.', 'Total of all 4: 4 × 15 = 60.', 'Known: 12 + 18 + 14 = 44. Missing score = 60 − 44.'], ans: '16. A 5th score of 15 would keep the mean at 15.' },
    keyHead: 'Key idea: mean = total ÷ how many',
    keyBig: 'Mean = total ÷ how many values. Turn it round: total = mean × how many. The values above and below the mean always balance.',
    keySmall: 'One extreme value can pull the mean a long way. Then the median (middle value) or mode (most common) may describe a typical value better.',
    brk: 'Dice jumps. Roll two dice on screen: everyone does that many star jumps. Three rounds. What was the mean number of jumps per round?',
    ws1: 'Page 1, in pairs: Q1 mean and balance check, Q2 missing score from the total, Q3 predict how the mean changes, Q4 a misleading mean (median and mode).',
    ws2: 'Page 2, on your own: Q5 trace the mean program, Q6 Singapore temperatures and plan the code that counts the days above the mean.'
  },

  qbank: {
    core: [
      { q: 'Find the mean of 3, 5, 7 and 9.', a: '6 (24 ÷ 4)' },
      { q: 'Find the mean of 10, 0, 8 and 6.', a: '6 (24 ÷ 4: the 0 counts as a value)' },
      { q: 'The mean of 5 numbers is 11. What is their total?', a: '55' },
      { q: 'Four bags have a mean mass of 2.5 kg. What is their total mass?', a: '10 kg' },
      { q: 'Find the median and the mode of 4, 9, 2, 9, 6.', a: 'In order: 2, 4, 6, 9, 9. Median 6, mode 9.' },
      { q: 'A Scratch list called marks holds 6, 8 and 7. A loop starts total at 0 and adds every item to total. What is total after the loop? What is the mean?', a: 'Total 21, mean 7' }
    ],
    stretch: [
      { q: 'The mean height of 4 children is 150 cm. A fifth child joins the group and the mean height becomes 152 cm. How tall is the fifth child?', a: '160 cm (5 × 152 = 760, 4 × 150 = 600, 760 − 600 = 160)' },
      { q: 'Mei’s mean score for 3 tests is 84. What must she score in the 4th test to raise her mean to 86?', a: '92 (4 × 86 = 344, 3 × 84 = 252, 344 − 252 = 92)' },
      { q: 'Write 5 whole numbers with a mean of 6 and a mode of 4.', a: 'Open, e.g. 4, 4, 5, 8, 9 (total 30, and 4 appears most often). Check the total is 30.' },
      { q: 'A Scratch list holds 8 numbers with a mean of 12. Then the number 21 is added to the list. What will the mean program say now?', a: '13 (8 × 12 = 96, 96 + 21 = 117, 117 ÷ 9 = 13)' },
      { q: 'The mean of 7, 11, x and 14 is 10. What is x?', a: '8 (4 × 10 = 40, 40 − 7 − 11 − 14 = 8)' },
      { q: 'The mean of five numbers is 20. Each number is doubled and then 3 is taken away. What is the new mean?', a: '37 (20 × 2 − 3)' },
      { q: 'Ali’s mean for 5 spelling tests is 16. His mean for the first 3 tests is 15. What is the mean of his last 2 tests?', a: '17.5 (5 × 16 = 80, 3 × 15 = 45, 80 − 45 = 35, 35 ÷ 2 = 17.5)' },
      { q: 'Five whole numbers have a mean of 9, a median of 8 and a mode of 8. The smallest is 5 and the largest is 14. Find all five numbers.', a: '5, 8, 8, 10, 14 (total 45; the middle one is 8; 8 must appear twice, and it can only be the 2nd number, so the 4th is 45 − 5 − 8 − 8 − 14 = 10)' }
    ],
    challenge: [
      { q: 'Five numbers have a mean of 8. One number is removed, and the mean of the other four is 7. Which number was removed?', a: '12 (5 × 8 = 40, 4 × 7 = 28, 40 − 28 = 12)' },
      { q: 'A basketball player’s mean score for 9 games is 30 points. How many points must she score in the 10th game to raise her mean to 32?', a: '50 (10 × 32 = 320, 9 × 30 = 270, 320 − 270 = 50)' },
      { q: 'Five whole numbers have a mean of 6, a median of 5 and only one mode, 2. What is the largest the biggest number can be?', a: '15 (2, 2, 5, 6, 15: the total is 30, so the last two make 21; the 4th must be at least 6, or 5 would tie with 2 as a mode)' },
      { q: 'Can the mean of 5 whole numbers be bigger than 4 of them? Give an example.', a: 'Yes, e.g. 1, 1, 1, 1, 16 has mean 4, which is bigger than four of the numbers.' },
      { q: 'The mean of 4 numbers is 15. One of the numbers is changed and the mean becomes 18. By how much was that number changed?', a: 'It went up by 12 (the total went from 60 to 72)' },
      { q: 'Jun’s program adds 5 to every item in a list of 10 numbers, then doubles every item. The mean was 7 before. What is the mean now?', a: '24 ((7 + 5) × 2)' },
      { q: 'Find ALL the sets of three different counting numbers whose mean is 4 and whose median is 4.', a: '3 sets: 1, 4, 7;  2, 4, 6;  3, 4, 5 (the total is 12, the middle is 4, so the other two add to 8 and one is less than 4)' },
      { q: 'The mean of 1, 2, 3, … , 99 is 50. Explain why without adding them all up. Then plan a short program that checks it.', a: 'Pair them: 1 + 99, 2 + 98, … , 49 + 51 each make 100, with 50 left in the middle. Every pair balances around 50, so the mean is 50 (total 4950 ÷ 99 = 50). Program: set total to 0, set n to 1, repeat 99 (change total by n, change n by 1), say total ÷ 99.' },
      { q: 'A group of 8 children has a mean mass of 41 kg. When their tutor joins, the mean mass of all 9 becomes 44 kg. What is the tutor’s mass?', a: '68 kg (9 × 44 = 396, 8 × 41 = 328, 396 − 328 = 68)' }
    ]
  },

  workbook: H => {
    const meanProg = ['when green flag clicked', 'set total to 0', 'set i to 1', { c: 'repeat 4', body: ['change total by (item i of scores)', 'change i by 1'] }, 'say (total / 4)'];
    const planProg = ['set count to 0', 'set i to 1', { c: 'repeat (length of temps)', body: [{ c: 'if (item i of temps) > ( _____ ) then', body: ['change ( _____ ) by 1'] }, 'change i by 1'] }, 'say count'];
    const w1 = [3300, 1100, 1100, 1100, 1100, 1100, 1100];
    const w3 = [4000, 3400, 2500];
    const w4 = [1500, 1000, 1700, 1700];
    const side = (l, r) => `<div class="p img" style="display:flex;gap:14px;align-items:flex-start;justify-content:space-between;margin:4px 0 8px"><div style="flex:none">${l}</div><div style="flex:1;min-width:0">${r}</div></div>`;
    return [
      H.q(1, 'Five friends counted the books they read in the holidays:   4,   7,   2,   8,   9', { before: 0, keepNext: true }),
      H.sub('a', 'What is the total?   ________          (b)  What is the mean?   ________'),
      H.sub('c', 'Balance check: how far is each value above (+) or below (−) the mean?', { after: 40, keepNext: true }),
      H.sub('', '4 → ____     7 → ____     2 → ____     8 → ____     9 → ____      Add them up: ____'),
      H.q(2, 'Siti played 4 games. Her mean score was 17. Her first three scores were 15, 20 and 14.', { keepNext: true }),
      H.sub('a', 'Her total for the 4 games?  ______          (b)  Her 4th score?  ______'),
      H.sub('c', 'She plays a 5th game. What must she score to make her mean exactly 18?   ______'),
      H.q(3, 'The data 6, 8, 10, 12, 14 has a mean of 10. Predict first: up, down or the same? Then work out the new mean.', { keepNext: true }),
      H.tbl(w3, [
        H.row(['Change', 'Up, down or the same?', 'New mean'].map((s, i) => H.cell(s, w3[i], { bold: true, fill: 'EDEDED', h: 40 }))),
        ...['(a) Add a new value, 10.', '(b) Add 3 to every value.', '(c) Remove the 14.', '(d) Change the 14 to 44.'].map(s => H.row([H.cell(s, w3[0], { align: 'left', h: 45 }), H.cell('', w3[1], { h: 45 }), H.cell('', w3[2], { h: 45 })]))
      ]),
      H.q(4, 'Seven P6 pupils get this pocket money each week:   $10,  $12,  $12,  $15,  $16,  $20,  $69', { keepNext: true }),
      H.sub('a', 'Mean  ____      (b)  Median (middle value)  ____      (c)  Mode (most often)  ____'),
      H.sub('d', 'How many of the pupils get less than the mean?   ________'),
      H.sub('e', 'Jun says, “A typical pupil gets $22 a week.” Is that fair? Which average describes a typical pupil better? Explain.'),
      ...H.lines(2),

      H.q(5, 'Trace the code. The list called scores holds 5, 9, 6 and 12 (item 1 is 5, item 2 is 9, and so on). Fill in the trace table, one row for each time round the loop.', { pb: true, before: 0, keepNext: true }),
      side(codeSvg(meanProg, 'Code blocks: when green flag clicked, set total to 0, set i to 1, repeat 4 (change total by item i of scores, change i by 1), say total divided by 4.'),
        H.tbl(w4, [
          H.row(['Loop', 'i', 'item i', 'total'].map((s, i) => H.cell(s, w4[i], { bold: true, fill: 'EDEDED', h: 60 }))),
          ...['1st', '2nd', '3rd', '4th'].map(s => H.row([H.cell(s, w4[0], { bold: true, h: 75 }), H.cell('', w4[1], { h: 75 }), H.cell('', w4[2], { h: 75 }), H.cell('', w4[3], { h: 75 })]))
        ])),
      H.sub('a', 'What does the sprite say?   ________'),
      H.sub('b', 'Jo adds a 5th score, 13, to the list. Which two blocks must change so the program works for a list of ANY length? What should it say now?'),
      ...H.lines(2),
      H.q(6, 'The highest temperature each day for a week in Singapore, in °C:   29,  31,  33,  30,  32,  34,  28', { keepNext: true }),
      H.sub('a', 'Mean temperature?  ____ °C          (b)  Days hotter than the mean?  ____'),
      H.sub('c', 'Plan your code. The variable mean already holds your answer to (a). Fill in the two blanks so the program counts the days hotter than the mean. What will it say?', { keepNext: true }),
      side(codeSvg(planProg, 'Code blocks with two blanks: set count to 0, set i to 1, repeat length of temps (if item i of temps is greater than blank then change blank by 1; change i by 1), say count.'),
        pyBox('Python (optional): put the temperatures in data. Does it agree with (a)?', PY_WB)),
      H.sub('', 'Blank 1:  ____________        Blank 2:  ____________        It says:  ________')
    ];
  }
};
