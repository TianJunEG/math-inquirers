// Math Inquirers P4 — Lesson 5: Decimal Detectives (decimals to 3 places: number lines, comparing and ordering,
// rounding and rounding backwards, digit-card decimals, money and mass puzzles with bar models)
// Every answer below was worked out and checked (the "find all" and riddle items with a short Python script).

const tip = require('../tip.js');
const FG = require('../../levels/figs_l4_6.js');
const NAVY = '#1B2A49', YEL = '#FFC93C', SKY = '#DDEBF7', TEAL = '#1F7A6F', WHITE = '#FFFFFF', RED = '#D64545';
const T = (x, y, s, size = 16, fill = NAVY, anchor = 'middle', weight = 700) => `<text x="${x}" y="${y}" font-size="${size}" font-weight="${weight}" text-anchor="${anchor}" fill="${fill}" font-family="Arial">${s}</text>`;

// One number line: from x0 to x1, n equal steps, end labels, arrows {at (step number, may be a half), label}
const nline = (y, left, right, arrows, n = 10) => {
  const x0 = 60, x1 = 540, k = (x1 - x0) / n;
  let s = `<line x1="${x0 - 14}" y1="${y}" x2="${x1 + 14}" y2="${y}" stroke="${NAVY}" stroke-width="3"/>`;
  for (let i = 0; i <= n; i++) {
    const big = i === 0 || i === n || i === n / 2;
    s += `<line x1="${x0 + i * k}" y1="${y - (big ? 12 : 8)}" x2="${x0 + i * k}" y2="${y + (big ? 12 : 8)}" stroke="${NAVY}" stroke-width="${big ? 3 : 2}"/>`;
  }
  s += T(x0, y + 34, left, 16) + T(x1, y + 34, right, 16);
  arrows.forEach(([at, lab]) => {
    const x = x0 + at * k;
    s += `<line x1="${x}" y1="${y - 46}" x2="${x}" y2="${y - 16}" stroke="${RED}" stroke-width="3"/><polygon points="${x},${y - 12} ${x - 6},${y - 22} ${x + 6},${y - 22}" fill="${RED}"/>` + T(x, y - 52, lab, 17, RED);
  });
  return s;
};
const lines3 = () => {
  const mk = (tag, min, max, mid, marks, dp) => FG.lineParts({ w: 600, x0: 80, x1: 560, min, max, major: (max - min) / 2, minor: (max - min) / 10, tag, marks: marks.map(([v, t]) => ({ v: min + v * (max - min) / 10, t })), fmt: v => v.toFixed(dp).replace(/\.?0+$/, '') || '0', size: 19 });
  return FG.stackSvg([mk('(a)', 6, 7, 6.5, [[3, 'A'], [8.5, 'B']], 2), mk('(b)', 4.5, 4.6, 4.55, [[3, 'C'], [8, 'D']], 3), mk('(c)', 0.24, 0.25, 0.245, [[7, 'E']], 3)],
    'Three number lines, each with 10 equal steps and the two ends and the middle labelled. Line a from 6 to 7 with arrows A and B. Line b from 4.5 to 4.6 with arrows C and D. Line c from 0.24 to 0.25 with arrow E.');
};
// Q6 picture: two scales, the full box and the empty box
const scales = () => {
  const scale = (cx, label, cans) => {
    let g = `<rect x="${cx - 95}" y="150" width="190" height="56" rx="10" fill="${SKY}" stroke="${NAVY}" stroke-width="3"/><rect x="${cx - 52}" y="162" width="104" height="32" rx="5" fill="${WHITE}" stroke="${NAVY}" stroke-width="2"/>` + T(cx, 184, label, 17);
    g += `<rect x="${cx - 110}" y="136" width="220" height="12" rx="4" fill="${NAVY}"/>`;
    g += `<path d="M${cx - 92} 136 V70 H${cx + 92} V136" fill="${YEL}" stroke="${NAVY}" stroke-width="3" opacity="0.35"/><path d="M${cx - 92} 136 V70 M${cx + 92} 70 V136 M${cx - 92} 136 H${cx + 92}" fill="none" stroke="${NAVY}" stroke-width="3"/>`;
    for (let i = 0; i < cans; i++) {
      const x = cx - 84 + (i % 3) * 58, y = i < 3 ? 104 : 74;
      g += `<rect x="${x}" y="${y}" width="50" height="30" rx="6" fill="${RED}" stroke="${NAVY}" stroke-width="2"/><line x1="${x}" y1="${y + 15}" x2="${x + 50}" y2="${y + 15}" stroke="${WHITE}" stroke-width="2"/>`;
    }
    return g;
  };
  return `<svg aria-label="A box with 6 cans on a scale reads 2.85 kg. The empty box on a scale reads 0.45 kg." viewBox="0 24 600 190" xmlns="http://www.w3.org/2000/svg" style="width:340px;max-width:100%">` +
    scale(160, '2.85 kg', 6) + scale(440, '0.45 kg', 0) + T(160, 40, 'box with 6 cans', 16, TEAL) + T(440, 40, 'empty box', 16, TEAL) + '</svg>';
};

// Q3 scaffold: number line from 7.30 to 7.50 in hundredths (labels only at 7.3, 7.4, 7.5)
const roundLine = () => {
  const x0 = 40, W = 520, y = 34;
  let sv = `<svg aria-label="A number line from 7.30 to 7.50 marked in hundredths, with 7.3, 7.4 and 7.5 labelled and a dot at 7.4" viewBox="0 0 600 84" width="400" xmlns="http://www.w3.org/2000/svg" style="max-width:100%">`;
  sv += `<line x1="${x0 - 10}" y1="${y}" x2="${x0 + W + 10}" y2="${y}" stroke="${NAVY}" stroke-width="3"/>`;
  for (let i = 0; i <= 20; i++) {
    const x = x0 + i * W / 20, big = i % 10 === 0;
    sv += `<line x1="${x}" y1="${y - (big ? 14 : 8)}" x2="${x}" y2="${y + (big ? 14 : 8)}" stroke="${NAVY}" stroke-width="${big ? 4 : 2}"/>`;
    if (big) sv += T(x, y + 38, '7.' + (3 + i / 10), 20);
  }
  sv += `<circle cx="${x0 + W / 2}" cy="${y}" r="9" fill="${YEL}" stroke="${NAVY}" stroke-width="3"/>`;
  return sv + '</svg>';
};
// Q6 scaffold: a bar of 6 equal parts for the cans
const canBar = () => {
  let sv = `<svg aria-label="A bar cut into 6 equal parts, one part for each can. The whole bar is the mass of all 6 cans." viewBox="0 6 600 90" width="400" xmlns="http://www.w3.org/2000/svg" style="max-width:100%">`;
  sv += `<path d="M60 44 Q60 30 74 30 L290 30 Q300 30 300 20 Q300 30 310 30 L526 30 Q540 30 540 44" fill="none" stroke="${NAVY}" stroke-width="2.5"/>` + T(300, 16, 'all 6 cans together', 16, TEAL);
  for (let i = 0; i < 6; i++) sv += `<rect x="${60 + i * 80}" y="50" width="80" height="40" fill="${WHITE}" stroke="${NAVY}" stroke-width="3"/>` + T(100 + i * 80, 76, 'can', 15, '#8A94AD');
  return sv + '</svg>';
};

const jugFig = () => {
  const { T, R, L, N, TEAL } = FG; let g = '';
  [[150, 'full', 'jug full of water', '1.45 kg', 0], [450, 'half', 'jug half full', '0.85 kg', 1]].forEach(([cx, _k, cap, kg, half]) => {
    const top = 20, h = 130, w = 90;
    g += R(cx - w / 2, top, w, h, { w: 4 });
    const lvl = half ? h / 2 : h - 6;
    g += `<rect x="${cx - w / 2 + 2}" y="${top + h - lvl}" width="${w - 4}" height="${lvl - 2}" fill="url(#mi-dots)"/>`;
    g += L(cx - w / 2 - 6, top + h / 2, cx - w / 2 + 12, top + h / 2, { w: 3 });
    g += T(cx, top + h + 26, cap, { size: 18 }) + T(cx, top + h + 52, 'scale reads ' + kg, { size: 19, fill: TEAL });
  });
  return FG.svg(600, 230, g, 'Two jugs. The first is full of water and the scale reads 1.45 kilograms. The second is half full and the scale reads 0.85 kilograms.');
};
module.exports = {
  lesson: {
    n: 5, week: 3, session: 'A', title: 'Decimal Detectives', topic: 'Decimals',
    objective: 'Read decimals to 3 places on number lines, compare and order them by place value, round to the nearest whole number, 1 or 2 decimal places and work backwards from a rounded number (smallest and largest), and solve money and mass puzzles with bar models.',
    skills: 'Place value to thousandths, zooming in on a number line, ordering, rounding and rounding backwards, systematic listing, bar models, checking every clue',
    materials: 'Digit cards 0 to 9 and a decimal point card for each child (cut from the Digit, point, sign and bracket cards page), a place-value chart (ones, tenths, hundredths, thousandths), mini whiteboards, a metre ruler, play money.',
    online: 'Children cut out the digit cards and a decimal point from the kit page before the lesson and move them on camera. The tutor marks the zoom-in number lines on the slides.',
    warmup: 'Target 5: draw three empty boxes on a whiteboard with a decimal point after the first box. The tutor turns over digit cards one at a time; children write each digit in a box straight away (no moving it later). The number closest to 5 wins.',
    explore: 'Pairs use the digit cards 2, 5, 8 and a decimal point card to make as many different decimals as they can (the point goes between two digits), list them in order and find the one closest to 5.',
    mini: 'Zoom in on a number line: each step is 0.1, then 0.01, then 0.001. Line up the decimal points and fill empty places with 0 to compare. Round by finding the two neighbours and the halfway mark; to round backwards, find the smallest and largest numbers that round to the answer.',
    share: 'Ben says 3.405 is bigger than 3.45 because 405 is bigger than 45. Is he right?',
    exit: { q: 'Write 2.8, 2.08 and 2.088 in order, smallest first. Then round 2.088 to 1 decimal place.', a: '2.08, 2.088, 2.8.  2.088 rounds to 2.1.' },
    mistakes: ['Comparing decimals by the number of digits (thinking 3.405 > 3.45 because 405 > 45) instead of lining up the decimal points and comparing place by place.', 'Reading a number line by counting marks without first working out what one step is worth (0.1, 0.01 or 0.001).', 'Rounding backwards: giving 7.45 as the largest number that rounds to 7.4 (it rounds to 7.5), or forgetting 7.35 to 7.39 below 7.4.'],
    extension: 'Use the digit cards 1, 3, 5, 7 and a decimal point. Make the number with 2 decimal places that is closest to 40. (37.51) Then make your own closest-to puzzle for a partner.',
    key: [
      ['Q1', 'A 6.3,  B 6.85,  C 4.53,  D 4.58,  E 0.247.  (f) B (6.85 rounds to 7; 6.3 rounds to 6; the others are near 4.5 or 0.2).'],
      ['Q2', '(a) 3.045, 3.054, 3.405, 3.45, 3.5  (b) No. Line up the points: 3.405 and 3.450 have the same tenths, but 0 hundredths is less than 5 hundredths, so 3.405 is smaller. '],
      ['Q3', '(a) Smallest 7.35, largest 7.44 (7.45 rounds up to 7.5). (Moved to the question bank: how many numbers (10) and the digit-sum clue (7.38).)'],
      ['Q4', '(a) 3.69, 3.96, 6.39, 6.93, 9.36, 9.63  (b) 9.63  (c) 6.93 (only 0.07 away)  (d) 3.69 and 3.96'],
      ['Q5', 'Siti $4.10, Mei $5.30 ($9.40 − $1.20 = $8.20, $8.20 ÷ 2 = $4.10, $4.10 + $1.20 = $5.30; check $4.10 + $5.30 = $9.40).'],
      ['Q6', '(a) 0.4 kg (2.85 − 0.45 = 2.40 kg for 6 cans, 2.40 ÷ 6 = 0.4)  (b) 2.05 kg (2.85 − 0.8)']
    ]
  },

  script: {
    hook: ['Good morning, inquirers! Today you are decimal detectives. Decimals hide in prices, in masses, in race times. A tiny digit after the point can win or lose a race.', 'Our rule today: notice the place, test with a number line, explain why.'],
    warmIntro: ['Draw a box, a decimal point, then two boxes (three empty boxes, with the point after the first). I will turn over a digit card. Write it in a box straight away. You cannot move it later!', 'Our target is 5. The number closest to 5 wins. Where would you put a 4? A 9? A 0?'],
    predict: ['You have the cards 2, 5, 8 and a decimal point. How many different numbers do you think you can make? Write your guess before you start.'],
    exploreHints: ['Stuck: put the point after the first card. Now swap the digit cards around. Then move the point.', 'Not sure if you have them all: “How many numbers start with 2? With 5? With 8? Where can the point go?”', 'Finished early: which number is closest to 50? Which two numbers are closest to each other?'],
    think: ['“Where is the arrow? Between 2.3 and 2.4. I zoom in. That gap is cut into 10 equal steps, so each step is one hundredth, 0.01. The arrow is 6 steps past 2.3, so it is 2.36.”', '“Which is bigger, 4.37 or 4.307? I line up the points. Same ones, same tenths. Hundredths: 7 and 0. 7 hundredths is more, so 4.37 is bigger, even though 4.307 has more digits.”', '“A number with 2 decimal places rounds to 3.8. I look at the number line. The halfway marks are 3.75 and 3.85. 3.75 rounds up to 3.8, so it is the smallest. 3.85 would round up to 3.9, so the largest is 3.84.”'],
    circulate: ['Ask: “What is one small step worth on this number line? How do you know?”', 'Ask: “Line up the decimal points. Which place do you compare first?”', 'Ask: “Would this number round up or down? Where is the halfway mark?”'],
    hints: ['Hint 1: “Write each number in the place-value chart. Fill empty places with 0.”', 'Hint 2: “Count the steps between the two labelled marks. Divide the gap by the number of steps.”', 'Hint 3: “For bars: take away the extra part first, then share the rest equally.”'],
    talk: ["“Ben says 3.405 is bigger than 3.45 because 405 is bigger than 45. Who agrees? How can we check?”"],
    talkWeekly: ["“Why does adding a zero to the end of 3.45 not change it, but putting a zero after the point (3.045) does?”"],
    talkAns: "Ben is wrong. Line up the points: 3.405 and 3.450. The ones and tenths are the same; 0 hundredths is less than 5 hundredths, so 3.405 < 3.45.",
    talkWeeklyAns: "3.45 = 3.450 because 0 thousandths adds nothing, but 3.045 moves the 4 into the hundredths place, so it is a different, smaller number.",
    close: ['“Today you zoomed in on number lines, lined up the points, and worked rounding backwards. Detectives check every clue, and you did. Well done, inquirers!”']
  },

  deck: {
    today: 'Zoom in on number lines, order decimals to 3 places, round and work backwards from a rounded number, and solve money and mass puzzles.',
    warmGame: 'Target 5. Draw three empty boxes with a decimal point after the first. The tutor turns over digit cards one at a time; write each digit in a box straight away. The number closest to 5 wins.',
    warmQs: [["What is the 7 worth in 3.475?", "7 hundredths (0.07)"], ["Write 6 tenths and 4 thousandths as a decimal.", "0.604"], ["Which is bigger: 0.8 or 0.75?", "0.8 (0.80 > 0.75)"]],
    warmWeekly: [["Round 4.68 to 1 decimal place.", "4.7"], ["How much more than $3.05 is $5?", "$1.95"]],
    expSetup: ['Take the digit cards 2, 5, 8 and the decimal point card.', 'Make a decimal with all four cards. The point goes between two digits.', 'Make as many different numbers as you can. Write each one down.', 'Put them in order. Which one is closest to 5?'],
    expPic: 'digit cards 2, 5 and 8 and a decimal point card, with an example 25.8 and the question “Which is closest to 5?”',
    expAsk: [["How many different numbers did you make?", "12: six with 2 decimal places (2.58 … 8.52) and six with 1 decimal place (25.8 … 85.2)."], ["Which is the smallest? The largest?", "2.58 and 85.2."]],
    mini1: { head: 'Order: 4.307, 4.37, 4.073, 4.3', body: ['Line up the decimal points in a place-value chart.', 'Fill empty places with 0: 4.300, 4.307, 4.370, 4.073.', 'Compare the tenths first, then the hundredths, then the thousandths.'], ans: '4.073, 4.3, 4.307, 4.37' },
    mini2: { head: 'Rounding backwards', body: ['A number with 2 decimal places rounds to 3.8 (to 1 decimal place).', 'The halfway marks are 3.75 and 3.85.', 'What is the smallest it can be? The largest?'], ans: 'Smallest 3.75, largest 3.84 (3.85 rounds to 3.9).' },
    keyHead: 'Key idea: line up the points',
    keyBig: 'Line up the decimal points and compare place by place: ones, tenths, hundredths, thousandths. More digits does not mean bigger.',
    keySmall: 'To round, find the two neighbours and the halfway mark. To round backwards, find the smallest and largest numbers that round to it.',
    brk: 'Decimal stand-up. The tutor calls a decimal. More than 0.5: stand tall. Less than 0.5: crouch. Exactly 0.5: freeze like a statue.',
    ws1: 'Page 1, in pairs: Q1 zoom-in number lines, Q2 ordering and the missing digit, Q3 the rounding detective.',
    ws2: 'Page 2, on your own: Q4 digit-card decimals, Q5 money bar model, Q6 the box of cans.'
  },

  qbank: {
    core: [
      { q: 'Ali has 3 one-dollar coins, 4 ten-cent coins and 7 one-cent coins. How much money is that? Write the amount in dollars, using a decimal point.', a: '$3.47' },
      { q: 'Ali has $0.90 and Mei has $0.89. Who has more money? How much more? (Think in cents.)', a: 'Ali has more: 90¢ is 1¢ more than 89¢.' },
      { q: 'Is 7.46 closer to 7.4 or to 7.5? Draw a number line from 7.4 to 7.5 and mark the halfway point 7.45 to help you.', a: '7.5 (7.46 is just past the halfway point 7.45).' },
      { q: 'Ali buys 3 pens at $1.25 each. How much does he pay? (Add $1.25 three times, or think of $1.25 as 125 cents.)', a: '$3.75' },
      { q: 'A stick is 1 metre long. It is cut into 10 equal parts and Mei takes 4 parts. She then cuts one more part into 10 tiny equal pieces and takes 7 of them. How long is Mei’s stick, written as a decimal of a metre?', a: '0.47 m (4 tenths and 7 hundredths).' },
      { q: 'A number line from 3 to 4 has 10 equal steps. An arrow points to the 6th step after 3. What number is it? Now zoom in on the gap between that number and the next step, and cut it into 10 smaller steps. A new arrow points to the 5th small step. What number is that?', a: '3.6, then 3.65.' }
    ],
    stretch: [
      { q: 'Find ALL the digits that can go in the box: 3.□5 < 3.42 (one digit in the box)', a: '0, 1, 2 and 3 (3.45 is more than 3.42)' },
      { q: 'A number with 2 decimal places rounds to 10 when rounded to the nearest whole number. What is the smallest it can be? The largest?', a: 'Smallest 9.50, largest 10.49' },
      { q: 'What number is halfway between 2.6 and 2.7? What number is halfway between 2.6 and 2.61?', a: '2.65 and 2.605' },
      { q: 'Mystery decimal. I have 3 decimal places and I am between 4 and 5. Rounded to 1 decimal place, I am 4.7. My hundredths digit is 2 more than my tenths digit. My digits add up to 25. Who am I?', a: '4.687 (rounds to 4.7, so tenths 6 or 7; tenths 7 would make hundredths 9, 4.79…, too big; so 4.68_ and 4 + 6 + 8 + 7 = 25).' },
      { q: 'Siti buys 4 notebooks that cost the same. She pays with a $10 note and gets $2.60 change. How much does one notebook cost?', a: '$1.85 ($10 − $2.60 = $7.40, $7.40 ÷ 4 = $1.85)' },
      { q: 'Write these in order, smallest first: 0.6, 0.066, 0.606, 0.66, 0.06', a: '0.06, 0.066, 0.6, 0.606, 0.66 (as 0.060, 0.066, 0.600, 0.606, 0.660)' },
      { q: 'Mei is 1.38 m tall. Ben is 0.15 m taller than Mei. Ali is 0.09 m shorter than Ben. How tall is Ali?', a: '1.44 m (Ben 1.53 m)' },
      { q: 'Use the digit cards 2, 4, 7 and a decimal point once each (the point goes between two digits). Which number is closest to 50?', a: '47.2 (2.8 away; the next closest is 42.7)' },
      { q: 'A ribbon 4.8 m long is cut into 6 equal pieces. How long is each piece? Ravi uses 4 of the pieces. How much ribbon does he use?', a: '0.8 m each; 3.2 m' },
      { q: 'A number has 2 decimal places. Rounded to 1 decimal place it is 7.4. How many different numbers could it be? Its digits add up to 18. What is the number?', a: '10 numbers (7.35, 7.36 … 7.44). The number is 7.38 (7.47 also has digits adding to 18, but it rounds to 7.5).' },
      { q: 'Use the digit cards 3, 6, 9 and a decimal point card once each. The point can go between any two digits (like 3.69 or 36.9). How many different numbers can you make? Which is closest to 7? Which rounds to 40 to the nearest whole number?', a: '12 numbers: 3.69, 3.96, 6.39, 6.93, 9.36, 9.63, 36.9, 39.6, 63.9, 69.3, 93.6, 96.3. Closest to 7: 6.93. Rounds to 40: 39.6.' }
    ],
    challenge: [
      { q: 'A number with 3 decimal places rounds to 2.46 when rounded to 2 decimal places. Its digits add up to 20. What is the number?', a: '2.459 (it is from 2.455 to 2.464; 2.45_ needs 9 to make 20; 2.46_ would need 8, but 2.468 rounds to 2.47)' },
      { q: '3 apples and 1 pear weigh 0.95 kg. 1 apple and 1 pear weigh 0.45 kg. All the apples weigh the same. What is the mass of the pear?', a: '0.2 kg (2 apples = 0.95 − 0.45 = 0.5 kg, 1 apple = 0.25 kg, pear = 0.45 − 0.25)' },
      { q: 'Ravi has 10 coins. They are all 20¢ and 50¢ coins. Altogether they make $3.80. How many of each coin does he have?', a: 'Six 50¢ and four 20¢ (ten 20¢ make $2; each swap to a 50¢ adds 30¢; $1.80 more needs 6 swaps)' },
      { q: 'Ben rounds a number with 2 decimal places to the nearest whole number and gets 6. Mei rounds the same number to 1 decimal place and gets 5.5. Find ALL the numbers it could be.', a: '5.50, 5.51, 5.52, 5.53, 5.54' },
      { q: 'A pen costs $0.85 more than a pencil. 2 pens and 1 pencil cost $4.70 altogether. How much does a pencil cost?', a: '$1.00 (3 pencils + $1.70 = $4.70, so 3 pencils cost $3.00; a pen costs $1.85)' },
      { q: 'How many numbers with exactly 2 decimal places are between 3.9 and 4.1? (Do not count 3.9 and 4.1.)', a: '19 (3.91 to 3.99 is 9, 4.00 to 4.09 is 10)' },
      { q: 'Make up your own "closest to" puzzle. Choose four digit cards and a decimal point (the point goes between two digits). Pick a target number and find the number with 2 decimal places that is closest to it. Then ask: what if the target changes? Swap puzzles with a partner and check each other’s answers.', a: 'Puzzles will vary: check by listing every number that can be made. Model: cards 3, 5, 6, 9 and target 40: the closest is 39.65 (0.35 away); the next is 39.56 (0.44 away). What if the target is 50? Then the closest is 53.69 (3.69 away); the closest below 50 is 39.65, which is 10.35 away.' },
      { q: 'Ali, Ben and Siti share $9.20. Ben gets $0.50 more than Ali. Siti gets $1.30 more than Ben. How much does each child get?', fig: FG.barModel({ left: 70, right: 150, rows: [{ name: 'Ali', segs: [{ u: 3 }] }, { name: 'Ben', segs: [{ u: 3 }, { u: 0.8, f: 'shade', t: '$0.50', size: 15 }] }, { name: 'Siti', segs: [{ u: 3 }, { u: 0.8, f: 'shade', t: '$0.50', size: 15 }, { u: 1.8, f: 'dots', t: '$1.30 more', size: 15 }] }], ann: [{ k: 'rbrace', r1: 0, r2: 2, at: 5.6, t: '$9.20' }], label: 'Three bars. Ali has a bar of 3 equal parts. Ben has the same bar and a shaded extra part of 50 cents. Siti has Ben’s bar and a dotted extra part of $1.30. A brace marks $9.20 altogether.' }), a: 'Ali $2.30, Ben $2.80, Siti $4.10 (take away $0.50 + $1.80 = $2.30, then $6.90 ÷ 3 = $2.30)' },
      { q: 'A jug full of water weighs 1.45 kg. When it is half full, it weighs 0.85 kg. What is the mass of the empty jug?', fig: jugFig(), a: '0.25 kg (half the water is 1.45 − 0.85 = 0.6 kg, all the water is 1.2 kg, jug = 1.45 − 1.2)' }
    ]
  },

  workbook: H => [
    H.q(1, 'Zoom in! Write the number that each arrow points to. First work out what one small step is worth.', { before: 40, keepNext: true }),
    H.fig(lines3()),
    H.sub('', 'A = _______    B = _______    C = _______    D = _______    E = _______'),
    H.sub('f', 'Which arrow, A to E, shows a number that rounds to 7?  _____'),
    H.q(2, 'Order and compare.', { keepNext: true }),
    tip('write each number with 3 decimal places (3.5 is 3.500). Compare tenths first.'),
    H.sub('a', 'Write in order, smallest first:   3.405,   3.45,   3.054,   3.5,   3.045', { after: 40 }),
    H.sub('', '_________,  _________,  _________,  _________,  _________', { after: 40 }),
    H.sub('b', 'Ben says 3.405 is bigger than 3.45 because 405 is bigger than 45. Is he right? Explain.'),
    ...H.lines(1),
    H.q(3, 'The rounding detective. A number has 2 decimal places. Rounded to 1 decimal place, it is 7.4. Use the number line: it is marked in hundredths.', { keepNext: true }),
    H.fig(roundLine()),
    tip('7.45 is halfway between 7.4 and 7.5. Which marks on the line round to 7.4?'),
    H.sub('a', 'What is the smallest it can be?  ________     The largest?  ________'),

    H.q(4, 'Use the digit cards 3, 6, 9 and a decimal point card once each. The point goes after the FIRST digit, like 3.69.', { pb: true, before: 0, keepNext: true }),
    H.sub('a', 'Make all 6 numbers and list them in order, smallest first.'),
    ...H.lines(1),
    H.sub('b', 'Which is the largest number?   ________'),
    H.sub('c', 'Which of your numbers is closest to 7?   ________'),
    H.sub('d', 'Two of your numbers round to 4 (to the nearest whole number). Which two?   ________   ________'),
    H.q(5, 'Mei and Siti have $9.40 altogether. Mei has $1.20 more than Siti. How much money does each girl have? The bar model shows the two girls.', { keepNext: true }),
    H.fig(FG.barModel({ left: 90, right: 160, rows: [{ name: 'Siti', segs: [{ u: 3 }] }, { name: 'Mei', segs: [{ u: 3 }, { u: 1, f: 'shade' }] }],
      ann: [{ k: 'dim', row: 1, from: 3, to: 4, t: '$1.20 more' }, { k: 'rbrace', r1: 0, r2: 1, at: 4, t: '$9.40' }],
      label: 'Two bars. Siti has a bar of 3 equal parts. Mei has the same bar plus a shaded extra part marked $1.20 more. A brace on the right marks $9.40 altogether.' })),
    H.sub('', 'Mei  $________          Siti  $________'),
    H.q(6, 'A box holds 6 cans that all have the same mass.', { keepNext: true }),
    H.fig(scales()),
    H.sub('', 'Step 1: the 6 cans alone.   2.85 − 0.45 = ________ kg.      Step 2: share it between the 6 cans.', { keepNext: true }),
    H.fig(canBar()),
    H.sub('a', 'What is the mass of one can?   ________ kg'),
    H.sub('b', 'Ali takes 2 cans out of the box. What is the mass of the box and cans now?   ________ kg')
  ]
};

// ---- close_gaps + fix pass: sneak-peek puzzles, Investigation (with an easy first step), Looking back, Go further (docs/audit/close_gaps_p4.md, fixpass_p4.md)
module.exports.gaps = {
 "idea": "decimals",
 "check": [
  {
   "q": "Ali has 8 ten-cent coins ($0.80). Mei has 7 ten-cent coins and one 5-cent coin ($0.75). Draw the coins. Who has more money?",
   "a": "Ali has more. $0.80 (8 tenths) is more than $0.75 (7 tenths and 5 hundredths). 0.8 is the same as 0.80, and 0.80 is bigger than 0.75.",
   "s": "Ali: $0.80 is more than $0.75.",
   "kind": "access"
  },
  {
   "q": "Write a decimal that is between 3.4 and 3.5. How do you know it fits? Hint: draw a number line from 3.4 to 3.5 with 10 steps.",
   "a": "Any decimal from 3.401 to 3.499, for example 3.45. Write 3.4 as 3.40 and 3.5 as 3.50: 3.45 sits between them.",
   "s": "For example 3.45 (3.40 < 3.45 < 3.50).",
   "kind": "think"
  }
 ],
 "why": "Line up the decimal points and compare place by place. Write extra zeros so every number has the same number of places.",
 "invest": {
  "kind": "Is it always true? Test and explain.",
  "head": "Between two decimals",
  "intro": "Siti says: \"There is no decimal between 0.35 and 0.36, because they are next to each other.\"",
  "parts": [
   "Find a decimal between 0.35 and 0.36. Write it.",
   "Find as many decimals with 3 decimal places as you can between 0.35 and 0.36. Write them in order. How many are there?",
   "Is Siti right? Can you find a decimal between 0.35 and your smallest one? What do you think happens if you keep going?"
  ],
  "lines": 4,
  "key": "(a) Any of 0.351 to 0.359, for example 0.355. (b) Exactly 9 numbers with 3 decimal places: 0.351, 0.352, … 0.359 (checked by brute force). (c) Siti is wrong. Between 0.35 and 0.351 there is 0.3505 (4 decimal places), and between 0.35 and 0.3505 there is 0.35025, and so on: there is no \"next\" decimal after 0.35, you can always find another. Look for place value reasoning (0.35 = 0.350, so 0.351 is a bit more) and for children who write the zeros to compare.",
  "easy": "Write 0.35 as 0.350 and 0.36 as 0.360. Now write ONE decimal that sits between them."
 },
 "reflect": "Something I did well: I wrote the extra zeros. The hardest part was comparing decimals with different numbers of digits. What helped me: adding zeros so they had the same length. One thing I could try next: writing the zeros in a place-value chart.",
 "go2": {
  "q": "What if the target is 50 instead of 5? Which number with these cards is closest to 50?",
  "a": "52.8 (2.8 away). The next closest, 58.2, is 8.2 away."
 },
 "cap": "Page 2 is on your own. Aim for Q4 and Q5 first. Q6 is a choice for the last few minutes.",
 "p1": "After question 3 you may choose: carry on, or try Think harder.",
 "plan": ["Aim for Q4 and Q5 on page 2. Q6 is the choice question for the end of the block."]
};
