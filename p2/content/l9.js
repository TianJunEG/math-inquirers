// Math Inquirers P2, Lesson 9: Measure Masters (length, mass, volume, time)
// Every answer below was worked out and checked (jug pours listed step by step, times counted across the hour).
const N = '#1B2A49', Y = '#FFC93C', SKY = '#DDEBF7', TEAL = '#1F7A6F', RED = '#D64545', W = '#FFFFFF';
const F = 'font-family="Arial, sans-serif"';
const svg = (w, h, body, label) => `<svg viewBox="0 0 ${w} ${h}" width="${w}" style="max-width:100%" role="img" aria-label="${label}" xmlns="http://www.w3.org/2000/svg">${body}</svg>`;
const txt = (x, y, s, size = 16, o = {}) => `<text x="${x}" y="${y}" font-size="${size}" font-weight="${o.w || 700}" text-anchor="${o.a || 'middle'}" fill="${o.c || N}" ${F}>${s}</text>`;

/* ---------- drawings ---------- */
// one item sitting on a pan; returns [svg, width]
const item = (k, x, base) => {
  if (k === 'melon') return [`<ellipse cx="${x + 24}" cy="${base - 18}" rx="24" ry="18" fill="${TEAL}" stroke="${N}" stroke-width="2.5"/><path d="M${x + 12} ${base - 30} Q${x + 24} ${base - 18} ${x + 12} ${base - 6} M${x + 24} ${base - 36} Q${x + 36} ${base - 18} ${x + 24} ${base}" stroke="${W}" stroke-width="2.5" fill="none"/>`, 48];
  if (k === 'apple') return [`<circle cx="${x + 12}" cy="${base - 12}" r="12" fill="${RED}" stroke="${N}" stroke-width="2.5"/><line x1="${x + 12}" y1="${base - 24}" x2="${x + 15}" y2="${base - 31}" stroke="${N}" stroke-width="2.5"/>`, 24];
  if (k === 'lemon') return [`<ellipse cx="${x + 9}" cy="${base - 8}" rx="9" ry="8" fill="${Y}" stroke="${N}" stroke-width="2.5"/>`, 18];
  if (k === 'w100') return [`<path d="M${x} ${base} L${x + 3} ${base - 22} L${x + 39} ${base - 22} L${x + 42} ${base} Z" fill="${W}" stroke="${N}" stroke-width="2"/>${txt(x + 21, base - 6, '100 g', 14)}`, 42];
  return ['', 0];
};
const pan = (cx, py, items) => {
  let w = items.reduce((s, k) => s + item(k, 0, 0)[1] + 2, -2), x = cx - w / 2, out = '';
  items.forEach(k => { const [g, iw] = item(k, x, py); out += g; x += iw + 2; });
  const pw = Math.max(64, w + 10);
  return out + `<path d="M${cx - pw / 2} ${py} L${cx + pw / 2} ${py} L${cx + pw / 2 - 8} ${py + 8} L${cx - pw / 2 + 8} ${py + 8} Z" fill="${SKY}" stroke="${N}" stroke-width="2.5"/>`;
};
const scale = (cx, top, left, right, label, arm) => {
  const by = top + 64;
  return txt(cx, top + 16, label, 16, { c: TEAL }) +
    pan(cx - arm, by - 6, left) + pan(cx + arm, by - 6, right) +
    `<line x1="${cx - arm}" y1="${by + 3}" x2="${cx + arm}" y2="${by + 3}" stroke="${N}" stroke-width="5"/>` +
    `<line x1="${cx}" y1="${by + 3}" x2="${cx}" y2="${by + 44}" stroke="${N}" stroke-width="6"/><polygon points="${cx},${by - 5} ${cx - 7},${by + 7} ${cx + 7},${by + 7}" fill="${Y}" stroke="${N}" stroke-width="2"/><rect x="${cx - 34}" y="${by + 44}" width="68" height="10" rx="4" fill="${N}"/>`;
};
const scalesFig = svg(600, 125,
  scale(88, 2, ['melon'], ['apple', 'apple'], 'Scale 1', 52) +
  scale(270, 2, ['apple'], ['w100', 'w100'], 'Scale 2', 56) +
  scale(476, 2, ['melon'], ['apple', 'lemon', 'lemon', 'lemon', 'lemon'], 'Scale 3', 62),
  'Three balanced scales. Scale 1: one melon balances two apples. Scale 2: one apple balances two 100 g weights. Scale 3: one melon balances one apple and four lemons.');

const jug = (x, base, h, w, lab) => `<path d="M${x} ${base - h} L${x + w} ${base - h} L${x + w} ${base} L${x} ${base} Z" fill="${SKY}" stroke="${N}" stroke-width="3"/><path d="M${x + w} ${base - h + 10} q18 4 18 ${h / 3} q0 ${h / 4} -18 ${h / 3}" fill="none" stroke="${N}" stroke-width="3"/><path d="M${x} ${base - h} l-10 -8" stroke="${N}" stroke-width="3"/>${txt(x + w / 2, base - h / 2 + 7, lab, 20)}`;
const jugsFig = svg(600, 86,
  jug(170, 80, 46, 56, '3 ℓ') + jug(300, 80, 72, 74, '5 ℓ') +
  txt(470, 40, 'No marks', 15, { c: TEAL }) + txt(470, 60, 'on the jugs!', 15, { c: TEAL }),
  'A 3 litre jug and a 5 litre jug with no marks on them');

const ribbonFig = (() => {
  const k = 4, x0 = 40, rL = 64 * k, ov = 5 * k, bL = 46 * k; // drawn to scale; the blue length is not labelled
  return svg(600, 112,
    `<rect x="${x0}" y="26" width="${rL}" height="24" rx="5" fill="${RED}" stroke="${N}" stroke-width="2.5"/>${txt(x0 + rL / 2, 44, 'red: 64 cm', 15, { c: W })}` +
    `<rect x="${x0 + rL - ov}" y="42" width="${bL}" height="24" rx="5" fill="${SKY}" stroke="${N}" stroke-width="2.5"/>${txt(x0 + rL - ov + bL / 2 + 6, 60, 'blue', 15)}` +
    `<rect x="${x0 + rL - ov}" y="42" width="${ov}" height="8" fill="${Y}" stroke="${N}" stroke-width="1.5"/>` +
    `<line x1="${x0 + rL - ov / 2}" y1="24" x2="${x0 + rL - ov / 2}" y2="20" stroke="${N}" stroke-width="2"/>${txt(x0 + rL - ov / 2, 16, 'overlap 5 cm', 14, { c: TEAL })}` +
    `<line x1="${x0}" y1="82" x2="${x0 + rL - ov + bL}" y2="82" stroke="${N}" stroke-width="2"/><line x1="${x0}" y1="75" x2="${x0}" y2="89" stroke="${N}" stroke-width="2"/><line x1="${x0 + rL - ov + bL}" y1="75" x2="${x0 + rL - ov + bL}" y2="89" stroke="${N}" stroke-width="2"/>${txt(x0 + (rL - ov + bL) / 2, 106, 'new ribbon: ? cm', 15)}`,
    'A red ribbon 64 centimetres long and a blue ribbon glued end to end, overlapping by 5 centimetres');
})();

const clock = (cx, cy, h, m, cap, R = 52) => {
  // numerals sit OUTSIDE the ring of minute marks so the long hand can reach the marks without covering a numeral
  let s = `<circle cx="${cx}" cy="${cy}" r="${R}" fill="${W}" stroke="${N}" stroke-width="4"/>`;
  for (let i = 0; i < 60; i++) { const a = i * Math.PI / 30, r1 = i % 5 ? R - 6 : R - 11; s += `<line x1="${(cx + r1 * Math.sin(a)).toFixed(1)}" y1="${(cy - r1 * Math.cos(a)).toFixed(1)}" x2="${(cx + (R - 2) * Math.sin(a)).toFixed(1)}" y2="${(cy - (R - 2) * Math.cos(a)).toFixed(1)}" stroke="${N}" stroke-width="${i % 5 ? 1 : 2.5}"/>`; }
  for (let n = 1; n <= 12; n++) { const a = n * Math.PI / 6; s += txt((cx + (R + 15) * Math.sin(a)).toFixed(1), (cy - (R + 15) * Math.cos(a) + 5.5).toFixed(1), n, 15); }
  const ha = ((h % 12) * 30 + m * 0.5) * Math.PI / 180, ma = m * 6 * Math.PI / 180;
  // hour hand: short, thick, navy.  minute hand: long, thin, red, ending at the minute marks
  s += `<line x1="${cx}" y1="${cy}" x2="${(cx + R * 0.45 * Math.sin(ha)).toFixed(1)}" y2="${(cy - R * 0.45 * Math.cos(ha)).toFixed(1)}" stroke="${N}" stroke-width="7" stroke-linecap="round"/>`;
  s += `<line x1="${cx}" y1="${cy}" x2="${(cx + (R - 4) * Math.sin(ma)).toFixed(1)}" y2="${(cy - (R - 4) * Math.cos(ma)).toFixed(1)}" stroke="${RED}" stroke-width="3" stroke-linecap="round"/><circle cx="${cx}" cy="${cy}" r="5" fill="${N}"/>`;
  return s + txt(cx, cy + R + 38, cap, 15, { w: 600 });
};
const clocksFig = svg(600, 188,
  txt(170 - 84, 86, 'A', 22, { c: TEAL }) + clock(170, 80, 7, 25, 'Ali is eating breakfast.') +
  txt(430 - 84, 86, 'B', 22, { c: TEAL }) + clock(430, 80, 4, 50, 'Ali is at swimming after school.') +
  txt(300, 184, 'short thick hand = hour     long red hand = minute', 14, { c: TEAL }),
  'Two clocks. Clock A: Ali is eating breakfast. Clock B: Ali is at swimming after school. The short thick navy hand is the hour hand and the long thin red hand is the minute hand.').replace('width="600"', 'width="450"');

/* ---------- module ---------- */
module.exports = {
  lesson: {
    n: 9, week: 5, session: 'A', title: 'Measure Masters', topic: 'Length, Mass, Volume and Time',
    objective: 'Solve balance-scale puzzles in g and kg by swapping things that balance; solve pouring puzzles with litre jugs by keeping a table of every pour; join and cut lengths in m and cm (overlaps, pieces and cuts); tell the time to 5 minutes with am and pm and find start times, end times and how long, also across the hour.',
    skills: 'Reasoning with equal amounts (swapping), working step by step, keeping a table, counting on in time, checking',
    materials: 'A coat hanger, two paper cups, string, a glue stick, a spoon and about 20 20¢ coins (a home-made balance; backup: a ruler balanced on a pencil); for the jug puzzles two cups or bottles of different size (about 3 and 5 units), a jug of dry rice or sand (or water), and tape marking 3 and 5 units; a cardboard clock with hands; mini whiteboards.',
    online: 'Children build the coat-hanger balance, hang it and test that it is level BEFORE the lesson (kit message, then a 30-second check at minute 0) and describe it aloud (nothing is held up to the camera). No coat-hanger balance at home? The tutor balances a ruler on a pencil on camera and pairs share one view. The tutor shares the slide balances, jugs and clocks and annotates on screen. Each child needs a cardboard or paper-plate clock. For the pouring puzzles use dry rice or sand rather than water when online, and let children act out each pour with the two containers.',
    warmup: 'Which unit? The tutor shows three things (a door, a bag of rice, brushing your teeth). Children show m, cm, kg, g, ℓ or minutes on whiteboards, then explain.',
    explore: 'Balance lab with a coat-hanger balance (hung and tested level before the lesson): how many 20¢ coins balance a glue stick? Guess first, then test. The spoon is a take-home: which is heavier, the glue stick or the spoon, and how do you know without putting them on the balance together?',
    mini: 'A level balance means both sides are equally heavy, so we can swap one thing for whatever balances it (watermelon = 3 pineapples; pineapple = 2 kg; so watermelon = 6 kg; watermelon = pineapple + 4 bags, so the 4 bags are 4 kg). Jug puzzles: fill, pour or empty, and write every pour in a table (4 ℓ and 9 ℓ jugs: fill 9, pour into 4 twice, emptying in between, leaves 1 ℓ).',
    share: 'A melon balances 2 apples. Can you swap the melon on a scale for 2 apples and keep it level? Why?',
    exit: { q: 'A lesson starts at 4:50 pm and lasts 25 minutes. What time does it end?', a: '5:15 pm (4:50 to 5:00 is 10 minutes, 15 more minutes is 5:15)' },
    mistakes: ['Balance puzzles: adding the masses on the two sides instead of using "both sides are the same".', 'Jug puzzles: writing "pour" without saying how much is in each jug after the pour, so the steps cannot be checked.', 'Time: counting on past the hour as if there were 100 minutes in an hour (4:50 + 25 minutes written as 4:75 or 5:75).'],
    takehome: 'Page 1: Q2(b) (get exactly 1 ℓ). Page 2: Q4(b) (the ribbon with a 5 cm overlap) and Q5(c) (how long is the trip). Also at home: try the spoon on the balance. The ribbon teaching slide and the time try-it slide are not shown in class.',
    extension: 'Make your own jug puzzle with two jug sizes and a target amount. Check that it can be done, and list every pour.',
    key: [
      ['Q1', '(a) 200 g  (b) 400 g  (c) 50 g (the melon is 400 g, the apple is 200 g, so 4 lemons are 200 g)  (d) 8 lemons'],
      ['Q2', '(a) Fill the 5 ℓ jug. Pour it into the 3 ℓ jug until the 3 ℓ jug is full. 2 ℓ is left in the 5 ℓ jug.  (b) Fill the 3 ℓ jug and pour it into the 5 ℓ jug. Fill the 3 ℓ jug again and pour until the 5 ℓ jug is full (2 ℓ goes in). 1 ℓ is left in the 3 ℓ jug.'],
      ['Q3', '(3 ℓ jug, 5 ℓ jug) Start 0, 0. 1: fill the 5 ℓ jug: 0, 5. 2: pour into the 3 ℓ jug until it is full: 3, 2. 3: empty the 3 ℓ jug: 0, 2. 4: pour the 2 ℓ into the 3 ℓ jug: 2, 0. 5: fill the 5 ℓ jug: 2, 5. 6: pour into the 3 ℓ jug until it is full (1 ℓ fits): 3, 4. 4 ℓ ✓ (6 steps is the shortest way; checked by search.)'],
      ['Q4', '(a) 46 cm  (b) 105 cm (64 + 46 = 110, take away the 5 cm overlap)'],
      ['Q5', '(a) A 7:25 am  B 4:50 pm  (b) 5:25 pm  (c) 45 minutes (10:45 to 11:00 is 15 minutes, 30 more)']
    ]
  },

  script: {
    hook: ['Good morning, Measure Masters! Today we measure how long, how heavy, how much water and how much time.', 'Some puzzles today have no ruler, no scale with numbers and no marks on the jugs. We will use our heads: notice it, test it, explain why.'],
    warmIntro: ['I will show you something. Write the unit you would use to measure it on your whiteboard: m, cm, kg, g, ℓ or minutes. Show me on three.', 'Be ready to say why. Why not grams for a bag of rice?'],
    predict: ['Look at your balance. A glue stick goes in one cup. How many 20¢ coins will balance it? Write your guess before you test.'],
    exploreHints: ['Stuck: check the hanger is level with both cups empty before you start.', 'Coins keep sliding: put them in the cup one at a time and stop when the hanger is level.', 'Finished early: find something that balances exactly the same number of coins as your glue stick.'],
    think: ['“A watermelon balances 3 pineapples. One pineapple balances a 2 kg weight. The scale is level, so both sides are equally heavy. I can swap each pineapple for 2 kg: 2, 4, 6. The watermelon is 6 kg.”', '“Now the watermelon balances one pineapple and 4 bags of sugar. The watermelon is 6 kg and the pineapple is 2 kg, so the bags must be the rest: 6 − 2 = 4 kg. 4 bags make 4 kg, so each bag is 1 kg. I check: 2 + 1 + 1 + 1 + 1 = 6 ✓.”', '“A jug puzzle: a 4 ℓ jug and a 9 ℓ jug, and I want exactly 1 ℓ. I fill the 9 ℓ jug. I pour into the 4 ℓ jug until it is full: 9 − 4 = 5 left. I empty the 4 ℓ jug and pour again: 5 − 4 = 1. I write every pour in a table so I can check it.”'],
    circulate: ['Ask: “The scale is level. What does that tell you?”', 'Ask: “What can you swap the melon for?”', 'Ask: “How much is in each jug now? Show me in your table.”'],
    hints: ['Hint 1: “Find the thing you know first. Which scale has a number on it?”', 'Hint 2: “Swap: put what balances it on the scale instead.”', 'Hint 3: “For jugs, write the two amounts after every pour.”'],
    talk: ['“How did swapping help you with the balance puzzles?”'],
    talkAns: 'A level balance means the two sides weigh the same, so the melon can be swapped for 2 apples (or 400 g) and the scale stays level. (If a pair finishes early: a table shows how much is in each jug after every pour, so we can check every step and find our way back.)',
    close: ['“You were real Measure Masters today. You swapped things on a balance, you found exact amounts with no marks on the jugs, and you counted time across the hour.”', 'Next lesson is Puzzle Day: bring your best thinking!']
  },

  deck: {
    today: 'Solve balance, jug and ribbon puzzles, and work out times and how long things take.',
    warmGame: 'Which unit? Show three things one at a time (a door, a bag of rice, brushing teeth; spare: a pencil, a strawberry, a bucket of water). Children write m, cm, kg, g, ℓ or minutes on whiteboards and explain.',
    warmQs: [['35 cm + 40 cm = ?', '75 cm'], ['The minute hand points to 6. How many minutes past the hour?', '30 minutes'], ['A 5 ℓ bucket has 2 ℓ of water. How much more fills it?', '3 ℓ'], ['Lunch at 12:30. am or pm?', 'pm'], ['One bag of rice is 5 kg. How heavy are 2 bags?', '10 kg']],
    expSetup: ['Your two cups are already hanging from the coat hanger (done before the lesson). Check it is level when the cups are empty.', 'Put a glue stick in one cup. Guess: how many 20¢ coins will balance it?', 'Add coins one at a time until the hanger is level.', 'Write your number. How do you know it is level?'],
    expPic: 'a coat hanger with a paper cup hanging from each end: a glue stick in one cup and a pile of 20¢ coins in the other, and the hanger level.',
    expAsk: [['How many coins balanced your glue stick?', 'Open answers. The count depends on the coins and the objects.'], ['The glue stick balances 8 coins and the spoon balances 5 coins. Which is heavier?', 'The glue stick: it needs more of the same coin.'], ['Your partner used erasers and got a different number. Why?', 'Erasers and coins are different units. To compare, use the same unit.']],
    mini1: { head: 'Balance puzzle: swap it', body: ['A watermelon balances 3 pineapples.', 'One pineapple balances a 2 kg weight.', 'The watermelon also balances 1 pineapple and 4 bags of sugar.', 'How heavy is the watermelon? One bag of sugar?'], ans: 'Watermelon 6 kg (2 + 2 + 2). The 4 bags are 6 − 2 = 4 kg, so each bag is 1 kg. Check: 2 + 1 + 1 + 1 + 1 = 6.' },
    mini2: { head: 'Jug puzzle: keep a table', body: ['You have a 4 ℓ jug and a 9 ℓ jug with no marks.', 'You can fill a jug, empty it, or pour from one into the other.', 'How can you get exactly 1 ℓ?'], ans: 'Fill the 9 ℓ jug (0, 9). Pour into the 4 ℓ jug (4, 5). Empty the 4 ℓ jug (0, 5). Pour again (4, 1). 1 ℓ is left in the 9 ℓ jug.' },
    keyHead: 'Key idea: same on both sides', keyBig: 'A level balance means both sides are equally heavy, so you can swap. For jugs, write every pour in a table.', keySmall: 'For time, count on to the o’clock first, then count the rest.',
    brk: 'Be a balance! Stand on one leg with your arms out. The tutor calls “heavy left!” or “heavy right!” and you tip, then come back level.',
    ws1: 'Page 1, in pairs: Q1 balance scales, Q2 pouring with a 3 ℓ and a 5 ℓ jug.',
    ws2: 'Page 2, on your own: Q3 the 4 ℓ jug puzzle in a table, Q4 ribbons in cm and m, Q5 clocks, am and pm, and how long.'
  },

  qbank: {
    core: [
      { q: 'One bag of flour balances 2 bags of sugar. A bag of sugar is 300 g. How heavy is the bag of flour?', a: '600 g (300 + 300)' },
      { q: 'A bucket holds 10 ℓ. It has 4 ℓ of water in it. Ali pours in 3 ℓ more. How many more litres are needed to fill it?', a: '3 ℓ (4 + 3 = 7, and 10 − 7 = 3)' },
      { q: 'A ribbon is 90 cm long. Mei cuts off 25 cm. How long is the piece that is left?', a: '65 cm' },
      { q: 'A cartoon starts at 5:40 pm and lasts 30 minutes. What time does it end?', a: '6:10 pm' },
      { q: 'Write am or pm. Ben eats lunch at 12:30 ____. He goes to bed at 8:45 ____.', a: 'pm and pm' },
      { q: 'The minute hand points to 7. How many minutes past the hour is it?', a: '35 minutes (count in 5s: 5, 10, 15, 20, 25, 30, 35)' }
    ],
    stretch: [
      { q: '2 apples and 1 lemon balance 1 pomelo. 1 pomelo balances 5 lemons. How many lemons balance 1 apple? How many lemons balance 1 pomelo and 1 apple together?', a: '1 apple balances 2 lemons. Swap the pomelo for 5 lemons: 2 apples and 1 lemon balance 5 lemons. Take 1 lemon off both sides: 2 apples balance 4 lemons, so 1 apple balances 2 lemons. A pomelo and an apple balance 5 + 2 = 7 lemons.' },
      { q: 'Mei’s family leaves home at 10:45 am. They reach Grandma’s flat at 12:10 pm. How long is the trip?', a: '1 hour 25 minutes (10:45 to 11:00 is 15 minutes, 11:00 to 12:00 is 1 hour, 12:00 to 12:10 is 10 minutes).' },
      { q: '3 apples balance 1 pomelo. The pomelo and 2 apples together balance a 500 g weight. How heavy is one apple? How heavy is the pomelo?', a: 'Apple 100 g, pomelo 300 g (5 apples balance 500 g).' },
      { q: 'You have a 2 ℓ jug and a 7 ℓ jug with no marks. How can you get exactly 3 ℓ? List each pour.', a: 'Fill 7, pour into 2, empty 2, pour again: 3 ℓ is left in the 7 ℓ jug.' },
      { q: 'Mei’s piano lesson ends at 4:15 pm. It lasted 45 minutes. What time did it start?', a: '3:30 pm (count back 15 minutes to 4:00, then 30 more minutes to 3:30)' },
      { q: 'Buses to the MRT station leave every 15 minutes. The first bus leaves at 6:50 am. Ravi reaches the bus stop at 7:40 am. How long does he wait? The ride takes 25 minutes. When does he reach the MRT station?', a: 'Buses: 6:50, 7:05, 7:20, 7:35, 7:50. He waits 10 minutes for the 7:50 bus and reaches the station at 8:15 am (7:50 to 8:00 is 10 minutes, 15 more minutes).' },
      { q: 'Three ribbons, each 30 cm long, are glued end to end in a line. Each join overlaps by 2 cm. How long is the long ribbon?', a: '86 cm (30 + 30 + 30 = 90; there are 2 joins, so take away 2 + 2 = 4)' },
      { q: 'A tank has 20 ℓ of water. A tap adds 5 ℓ every 10 minutes. The tap is turned on at 9:40 am. At what time does the tank have 40 ℓ?', a: '10:20 am (20 ℓ more is 4 lots of 5 ℓ, which takes 4 lots of 10 minutes = 40 minutes)' },
      { q: 'A box with 4 same books in it is 1000 g. The empty box is 200 g. How heavy is one book?', a: '200 g (the books are 1000 − 200 = 800 g; 200 + 200 + 200 + 200 = 800)' },
      { q: 'Ali’s clock is 10 minutes fast. It shows 3:05 pm. What is the real time?', a: '2:55 pm' }
    ],
    challenge: [
      { q: 'A basket with 4 apples is 700 g. The same basket with 2 apples is 500 g. How heavy is the empty basket?', a: '300 g (the 2 extra apples are 200 g)' },
      { q: 'A rope 40 cm long is cut into pieces 10 cm long. Each cut takes 2 minutes. How long does the cutting take?', a: '6 minutes (4 pieces need only 3 cuts)' },
      { q: 'A film is 1 hour 40 minutes long. It ends at 12:20 pm. What time did it start?', a: '10:40 am (1 hour before 12:20 pm is 11:20 am, then 40 minutes earlier is 10:40 am)' },
      { q: 'Ali’s watch loses 5 minutes every hour. He sets it to the right time at 8:00 am. What does his watch show at 12 noon?', a: '11:40 am (4 hours, 5 minutes slow each hour: 20 minutes slow)' },
      { q: 'Make up your own jug puzzle: choose two jug sizes between 2 ℓ and 9 ℓ and a target amount, and check that it can be done by listing every pour. Then try this: with a 4 ℓ jug and a 6 ℓ jug, can you ever measure exactly 5 ℓ? Explain why or why not.', a: 'Open. Example: a 3 ℓ and a 7 ℓ jug make 5 ℓ (see the pours in the question above). With a 4 ℓ and a 6 ℓ jug you can only ever measure 2 ℓ, 4 ℓ or 6 ℓ: both jugs hold an even number of litres, so every pour, fill or empty changes the amounts by even numbers. 5 is odd, so it is impossible.' },
      { q: 'Ravi has a 5 ℓ jug, a 3 ℓ jug and a big bucket. How can he get exactly 7 ℓ of water in the bucket?', a: 'One way: fill the 5 ℓ jug and pour it into the 3 ℓ jug until that is full: 2 ℓ is left. Pour the 2 ℓ into the bucket. Then fill the 5 ℓ jug and pour it all into the bucket: 2 + 5 = 7 ℓ. (Other ways work too, e.g. 1 ℓ + 3 ℓ + 3 ℓ. Whole jugs alone give 3, 5, 6, 8, 9, 10 …, never 7.)' },
      { q: 'You have a 3 ℓ jug and a 7 ℓ jug with no marks. How can you get exactly 5 ℓ? List each pour.', a: '(3 ℓ, 7 ℓ): fill 7 (0, 7); pour (3, 4); empty 3 (0, 4); pour (3, 1); empty 3 (0, 1); pour (1, 0); fill 7 (1, 7); pour until the 3 ℓ jug is full (3, 5). 5 ℓ in the 7 ℓ jug.' },
      { q: 'Scale 1: 2 cubes and 1 ball balance 2 balls. Scale 2: 1 ball and 1 cube balance a 300 g weight. How heavy is one cube? How heavy is one ball?', a: 'Take one ball off both sides of scale 1: 2 cubes balance 1 ball. On scale 2, swap the ball for 2 cubes: 3 cubes balance 300 g, so a cube is 100 g and a ball is 200 g. Check scale 1: 100 + 100 + 200 = 400 = 200 + 200.' },
      { q: 'Mei has 3 lessons in a row. Each lesson is 35 minutes long, with a 10-minute break between lessons. The first lesson starts at 8:15 am. What time does the last lesson end?', a: '10:20 am (8:15 to 8:50, break to 9:00, 9:00 to 9:35, break to 9:45, 9:45 to 10:20)' }
    ]
  },

  workbook: H => [
    H.p('A level balance means both sides are equally heavy. Show how you know for every answer.', { after: 40 }),
    H.q(1, 'Each scale is level.', { before: 40, keepNext: true }),
    H.fig(scalesFig),
    H.sub('a', 'How heavy is 1 apple?   ________ g'),
    H.sub('b', 'How heavy is the melon?   ________ g'),
    H.sub('c', 'How heavy is 1 lemon? Show how you know. Tip: on Scale 3, melon = apple + 4 lemons.'),
    ...H.lines(2),
    H.sub('d', 'How many lemons balance the melon?   ________ lemons'),
    H.q(2, 'You have a 3 ℓ jug and a 5 ℓ jug. You can fill a jug from the tap, empty a jug into the sink, or pour from one jug into the other until one jug is full or the other is empty.', { keepNext: true }),
    H.fig(jugsFig),
    H.sub('a', 'How can you get exactly 2 ℓ? Write the steps.'),
    ...H.lines(1),
    H.sub('b', [H.t('★ take-home  ', { bold: true, color: 'B45F06' }), H.t('How can you get exactly 1 ℓ? Write the steps.')]),
    ...H.lines(2),
    H.q(3, 'Next puzzle. Get exactly 4 ℓ in the 5 ℓ jug. Start with both jugs empty. The first three steps are done for you: you now have 2 ℓ in the 5 ℓ jug. Tip: act it out with two cups of different sizes, or draw the jugs. Where can that 2 ℓ go? Write each step in the table. You may not need every row.', { pb: true, before: 0, keepNext: true }),
    H.tbl([1300, 4600, 2000, 2000], [
      H.row(['Step', 'What I do', '3 ℓ jug', '5 ℓ jug'].map((s, i) => H.cell(s, [1300, 4600, 2000, 2000][i], { bold: true, fill: 'EDEDED', h: 15 }))),
      H.row([H.cell('Start', 1300, { bold: true, h: 15 }), H.cell('both jugs empty', 4600, { h: 15 }), H.cell('0 ℓ', 2000, { h: 15 }), H.cell('0 ℓ', 2000, { h: 15 })]),
      H.row([H.cell('1', 1300, { bold: true, h: 15 }), H.cell('Fill the 5 ℓ jug', 4600, { h: 15 }), H.cell('0 ℓ', 2000, { h: 15 }), H.cell('5 ℓ', 2000, { h: 15 })]),
      H.row([H.cell('2', 1300, { bold: true, h: 15 }), H.cell('Pour the 5 ℓ jug into the 3 ℓ jug until it is full', 4600, { h: 15 }), H.cell('3 ℓ', 2000, { h: 15 }), H.cell('2 ℓ', 2000, { h: 15 })]),
      H.row([H.cell('3', 1300, { bold: true, h: 15 }), H.cell('Empty the 3 ℓ jug', 4600, { h: 15 }), H.cell('0 ℓ', 2000, { h: 15 }), H.cell('2 ℓ', 2000, { h: 15 })]),
      ...[4, 5, 6, 7].map(n => H.row([H.cell(String(n), 1300, { bold: true, h: 15 }), H.cell('', 4600, { h: 15 }), H.cell('', 2000, { h: 15 }), H.cell('', 2000, { h: 15 })]))
    ]),
    H.q(4, 'Siti has a red ribbon 64 cm long. Her blue ribbon is 18 cm shorter than the red ribbon.', { keepNext: true }),
    H.sub('a', 'How long is the blue ribbon?   ________ cm'),
    H.sub('b', [H.t('★ take-home  ', { bold: true, color: 'B45F06' }), H.t('She glues them end to end with a 5 cm overlap. The new ribbon is ________ cm long.')], { keepNext: true }),
    H.fig(ribbonFig),
    H.q(5, 'Read the clocks. Hint: on clock B the hour hand is almost on the 5. Is it 4 o\u2019clock or 5 o\u2019clock?', { keepNext: true }),
    H.fig(clocksFig),
    H.sub('a', 'Write each time with am or pm.   A: ____________   B: ____________', { after: 50 }),
    H.sub('b', 'Swimming starts at the time on clock B and lasts 35 minutes. It ends at ____________', { after: 50 }),
    H.sub('c', [H.t('★ take-home  ', { bold: true, color: 'B45F06' }), H.t('Mei’s family leaves home at 10:45 am. They reach Grandma’s flat at 11:30 am. How long is the trip?   ______________')])
  ]
};
