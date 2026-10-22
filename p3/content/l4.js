// Math Inquirers P3, Lesson 4: Model Makers (word problems with bar models)
// Heuristics taught: draw a model; before and after (look for what stays the same).

// ---------- bar-model SVG helpers for the workbook (viewBox 600 wide) ----------
const NAVY = '#1B2A49', YEL = '#FFC93C', SKY = '#DDEBF7', TEAL = '#1F7A6F', WHITE = '#FFFFFF';
const txt = (x, y, s, o = {}) => `<text x="${x}" y="${y}" font-size="${o.size || 17}" font-weight="${o.w || 700}" text-anchor="${o.a || 'middle'}" fill="${o.fill || NAVY}" font-family="Arial">${s}</text>`;
const rect = (x, y, w, h, fill, label, o = {}) => `<rect x="${x}" y="${y}" width="${w}" height="${h}" fill="${fill}" stroke="${NAVY}" stroke-width="2.5"${o.dash ? ' stroke-dasharray="7 5"' : ''}/>` + (label ? txt(x + w / 2, y + h / 2 + 6, label, o) : '');
// horizontal curly brace from x0 to x1; ends sit on y; up=true points up
const braceH = (x0, x1, y, up, label) => {
  const h = 14, q = Math.min(10, (x1 - x0) / 4), m = (x0 + x1) / 2, s = up ? -1 : 1, ym = y + s * h / 2, yt = y + s * h;
  return `<path d="M${x0} ${y} Q${x0} ${ym} ${x0 + q} ${ym} L${m - q} ${ym} Q${m} ${ym} ${m} ${yt} Q${m} ${ym} ${m + q} ${ym} L${x1 - q} ${ym} Q${x1} ${ym} ${x1} ${y}" fill="none" stroke="${NAVY}" stroke-width="2.5"/>` + (label ? txt(m, up ? yt - 7 : yt + 19, label, { fill: TEAL }) : '');
};
// vertical curly brace on the right, from y0 to y1, ends on x
const braceV = (y0, y1, x, label) => {
  const h = 14, q = Math.min(10, (y1 - y0) / 4), m = (y0 + y1) / 2, xm = x + h / 2, xt = x + h;
  return `<path d="M${x} ${y0} Q${xm} ${y0} ${xm} ${y0 + q} L${xm} ${m - q} Q${xm} ${m} ${xt} ${m} Q${xm} ${m} ${xm} ${m + q} L${xm} ${y1 - q} Q${xm} ${y1} ${x} ${y1}" fill="none" stroke="${NAVY}" stroke-width="2.5"/>` + (label ? txt(xt + 8, m + 6, label, { a: 'start', fill: TEAL }) : '');
};
const svg = (label, h, inner, w = 470) => `<svg aria-label="${label}" viewBox="0 0 600 ${h}" xmlns="http://www.w3.org/2000/svg" style="width:${w}px;max-width:100%">${inner}</svg>`;
const name = (y, s) => txt(10, y, s, { a: 'start' });

const q1Fig = () => {
  const x = 100, y = 46, h = 40, W = 460, k = W / 1250, a = Math.round(486 * k), b = Math.round(378 * k);
  return svg('Part-whole bar: 1250 buns cut into 486, 378 and a missing part', 100,
    name(y + 27, 'Buns') + rect(x, y, a, h, SKY, '486') + rect(x + a, y, b, h, YEL, '378') + rect(x + a + b, y, W - a - b, h, WHITE, '?') +
    braceH(x, x + W, y - 4, true, '1250 buns'));
};
const q2Fig = () => {
  const x = 90, h = 34, k = 400 / 473, mei = Math.round(345 * k), ali = Math.round(473 * k), ben = Math.round(394 * k);
  const ys = [12, 62, 112];
  let s = name(ys[0] + 24, 'Mei') + rect(x, ys[0], mei, h, SKY, '345');
  s += name(ys[1] + 24, 'Ali') + rect(x, ys[1], mei, h, SKY, '') + rect(x + mei, ys[1], ali - mei, h, YEL, '128') + txt(x + ali + 18, ys[1] + 24, '?', { size: 20, fill: TEAL });
  s += name(ys[2] + 24, 'Ben') + rect(x, ys[2], ben, h, '#D3F1E4', '?') + rect(x + ben, ys[2], ali - ben, h, WHITE, '79', { dash: true });
  s += `<line x1="${x + mei}" y1="${ys[0]}" x2="${x + mei}" y2="${ys[1] + h}" stroke="${NAVY}" stroke-width="1.5" stroke-dasharray="4 4"/><line x1="${x + ali}" y1="${ys[1]}" x2="${x + ali}" y2="${ys[2] + h}" stroke="${NAVY}" stroke-width="1.5" stroke-dasharray="4 4"/>`;
  return svg('Comparison bars for Mei, Ali and Ben', 156, s, 420);
};
const q3Fig = () => {
  const x = 90, u = 90, h = 36, y1 = 20, y2 = 76;
  let s = name(y1 + 25, 'Ravi') + rect(x, y1, u, h, YEL, '');
  s += name(y2 + 25, 'Siti');
  for (let i = 0; i < 3; i++) s += rect(x + i * u, y2, u, h, YEL, '');
  s += braceV(y1, y2 + h, x + 3 * u + 14, '248 beads');
  return svg('Units model: Ravi 1 unit, Siti 3 units, 248 altogether', 130, s, 430);
};
const drawBox = (h = 150) => svg('Space to draw your model', h, `<rect x="4" y="4" width="592" height="${h - 8}" rx="10" fill="#FFFFFF" stroke="${NAVY}" stroke-width="2" stroke-dasharray="8 6"/>` + txt(18, 28, 'Draw your model here.', { a: 'start', size: 15, w: 600, fill: '#5B6785' }), 560);

module.exports = {
  lesson: {
    n: 4, week: 2, session: 'B', title: 'Model Makers', topic: 'Word Problems: Bar Models',
    objective: 'Draw bar models for part-whole, comparison, times-as-many and before-and-after word problems, and use them to solve two-step problems and check the answers.',
    skills: 'Draw a model, before and after, look for what stays the same, check the answer',
    materials: 'Multilink cubes (about 30 per pair), strips of squared paper, scissors, mini whiteboards and markers.',
    online: 'Tutor builds the bars on a shared slide. Each child uses Lego bricks, coins or paper strips at home, and a whiteboard or paper to draw bars. Print the workbook before the lesson. Pairs work in one breakout room for 10 minutes, then return for the check slide.',
    warmup: 'Arm bars. The tutor reads a sentence such as "Ali has 5 more than Ben". Children show the two bars with their hands, then draw them on whiteboards in 10 seconds.',
    explore: 'Cube towers. Pairs build two towers with 20 cubes altogether where one tower has 4 more cubes than the other. Then two towers with 20 cubes where one is 3 times as tall as the other. Then they draw each pair of towers as bars.',
    mini: 'Part-whole: one bar for the whole, cut into parts. Comparison: a bar for each person, longer for more, with the difference marked. Times as many: equal units. Before and after: ask what stays the same (the total, or the difference).',
    share: 'When two children are each given the same amount of money, why does the difference between them stay the same?',
    exit: { q: 'Ali has 3 times as many stickers as Ben. They have 80 stickers altogether. How many stickers does Ali have? Draw the model.', a: '60. 4 units = 80, so 1 unit = 20, and Ali has 3 units.' },
    mistakes: [
      'Comparing with the wrong person (Ben has 79 fewer than ALI, not Mei), or drawing "more than" as a shorter bar.',
      'Times as many: dividing the total by 3 instead of by 3 + 1 = 4 units.',
      'Make them equal: giving the whole difference instead of half of it.'
    ],
    extension: 'Write your own before-and-after story, draw its model and check it. Swap with a partner.',
    key: [
      ['Q1', '(a) 1250 − 486 − 378 = 386 buns  (b) 486 − 378 = 108 more'],
      ['Q2', '(a) Ali 345 + 128 = 473; Ben 473 − 79 = 394  (b) 345 + 473 + 394 = 1212 stickers'],
      ['Q3', '(a) 4 units; 1 unit = 248 ÷ 4 = 62 beads  (b) Siti has 3 × 62 = 186; 2 units = 124 more than Ravi'],
      ['Q4', 'Take away the extra: 150 − 24 = 126; 126 ÷ 2 = 63. Ben 63, Ali 63 + 24 = 87. Check 63 + 87 = 150.'],
      ['Q5', '(a) 19 stickers (difference 38, give half; both have 66)  (b) 38 is the whole difference. Giving 38 would leave Mei with 47 and Siti with 85: they just swap. Mei must give half of the difference.'],
      ['Q6', '(a) $27 (Ali $55, Ben $28)  (b) $27  (c) The difference stays the same, because both boys got the same amount.']
    ]
  },

  script: {
    hook: ['Today we are Model Makers. Word problems can look scary, but if we draw the story as bars, the answer often jumps out at us. A good model is like a map of the problem.'],
    warmIntro: ['I will read a sentence. Show me the two bars with your hands. Which hand is higher? Then draw it on your whiteboard.', 'How did you show "3 times as many"? How did you show "altogether"?'],
    predict: ['Twenty cubes make two towers. One tower has 4 more cubes than the other. Guess: how many cubes are in each tower? Write your guess, then build it to test.'],
    exploreHints: [
      'Stuck: build two towers the same height first. Then move cubes until one is 4 taller.',
      'Confused: "Take the extra 4 cubes away first. Share what is left fairly. Then put the 4 back."',
      'Ready for more: the Go further what-if on the slide (3 towers, 30 cubes). Or: 30 cubes where one tower is 4 times as tall as the other.'
    ],
    think: [
      '"A hall has 1500 seats: 645 red, 480 blue and the rest green. It is one whole cut into parts, so I draw ONE bar for 1500 and cut it into 645, 480 and a question mark. Whole take away the parts: 1500 − 645 = 855, 855 − 480 = 375. Check: 645 + 480 + 375 = 1500."',
      '"Siti has 167 MORE than Ravi, so her bar is longer: Ravi’s bar and an extra piece of 167. Ben has 95 FEWER than Siti, so I compare Ben with Siti, not with Ravi."',
      '"Before and after: when both girls get the same amount, both bars grow by the same piece, so the difference stays the same. I look for what stays the same."'
    ],
    circulate: [
      'Ask: "Is this a whole cut into parts, or two amounts being compared?"',
      'Ask: "Who has more? Whose bar is longer? Longer by how much?"',
      'Ask: "What stays the same in this story: the total or the difference?"'
    ],
    hints: [
      'Hint 1: "Draw a bar for each person. Label what you know."',
      'Hint 2: "Put a question mark on the part you need to find."',
      'Hint 3: "Look for equal units. How many units are there altogether?"'
    ],
    talk: ['"Mei and Siti are each given $5. Why does the difference between them stay the same?"', '"How can a model help you check your answer?"'],
    talkAns: 'Both bars grow by the same piece, so the gap between their ends does not change. To check, put your answers back into the model: the parts must make the whole and the difference must match the story.',
    close: ['"You turned words into pictures today. Next time a word problem looks hard, draw it first."']
  },

  deck: {
    today: 'Draw bar models for word problems: parts of a whole, comparing, times as many, and before and after.',
    warmGame: 'Arm bars. The tutor reads a sentence. Children show the two bars with their hands, then draw them on whiteboards in 10 seconds.',
    warmQs: [['348 + 52', '400'], ['1000 − 365', '635'], ['3 units = 27. What is 1 unit?', '9'], ['Ben has 40. Ali has 15 more than Ben. How many does Ali have?', '55'], ['Mei has 60. Siti has 12 fewer than Mei. How many does Siti have?', '48']],
    expSetup: ['Take 20 cubes. Build two towers. One tower must have 4 more cubes than the other.', 'Stand the towers side by side. How many cubes are in each?', 'Now use 20 cubes again: one tower must be 3 times as tall as the other.', 'Draw each pair of towers as two bars on your whiteboard.'],
    expPic: 'two cube towers side by side, the taller one with its extra cubes in yellow, and a brace showing 20 cubes altogether.',
    expAsk: [
      ['How did you find the two towers?', 'Take away the extra 4 (16 left), share 16 into two equal towers of 8, then put the 4 back: 8 and 12.'],
      ['How many cubes are in each tower when one is 3 times as tall?', '5 and 15. Together the towers make 4 equal parts of 5.'],
      ['Could you make "3 times as tall" with 22 cubes? Why?', 'No. We need 4 equal parts, and 22 cannot be shared into 4 equal parts (5 each leaves 2).']
    ],
    mini1: { head: 'Part-whole model', body: ['A hall has 1500 seats: 645 are red, 480 are blue and the rest are green.', 'Draw one bar for 1500 and cut it into 645, 480 and ?.', 'Whole take away the parts: 1500 − 645 − 480.'], ans: '375 green seats.' },
    mini2: { head: 'Comparison model', body: ['Ravi has 236 cards. Siti has 167 more cards than Ravi. Ben has 95 fewer cards than Siti.', 'Draw a bar for each child. Siti: 236 + 167.', 'Ben: Siti’s number − 95.'], ans: 'Siti 403, Ben 308.' },
    keyHead: 'Key idea: draw a model',
    keyBig: 'Draw a bar for each amount. Label what you know and put ? on what you want to find.',
    keySmall: 'Then ask: what stays the same? The total, or the difference?',
    brk: 'Stretch and shrink. Tutor calls "longer bar": stretch your arms wide. "Shorter bar": bring them close. "3 times as long": take three big steps.',
    ws1: 'Page 1, in pairs: Q1 part-whole, Q2 comparison with three children, Q3 times as many.',
    ws2: 'Page 2, on your own: Q4 total and difference, Q5 give to make equal, Q6 same amount given to both (the difference stays the same).'
  },

  qbank: {
    core: [
      { q: 'There are 2345 people at a concert. 1180 of them are adults. How many are children? Draw one long bar for all the people and mark off the part for the adults.', a: '1165' },
      { q: 'A red ribbon is 145 cm long. A blue ribbon is 68 cm longer. Draw the red ribbon as a bar, then draw a longer bar for the blue ribbon. How long is the blue ribbon?', a: '213 cm' },
      { q: 'Ravi has 512 stamps. Siti has 139 fewer stamps than Ravi. Draw a bar for each child. How many stamps does Siti have? How many do they have altogether?', a: 'Siti 373; altogether 885' },
      { q: 'Ali has 23 cards. Ben has 4 times as many cards as Ali. Draw 1 box for Ali and 4 boxes for Ben. How many cards does Ben have? How many do they have altogether?', a: 'Ben 92; altogether 115' },
      { q: 'A box has 1000 beads. Mei uses 365 beads for a necklace and 248 beads for a bracelet. How many beads are left?', a: '387' },
      { q: 'A pen costs $3. A bag costs 5 times as much as the pen. Draw 1 box for the pen and 5 boxes for the bag. How much more does the bag cost than the pen?', a: '$12 (the bag costs $15; 4 more boxes of $3)' }
    ],
    stretch: [
      { q: 'Ali and Ben have 96 cards altogether. Ali has 3 times as many cards as Ben. How many more cards does Ali have than Ben?', a: '48. 4 units = 96, 1 unit = 24, and the difference is 2 units.' },
      { q: 'Siti has 54 more beads than Mei. Siti gives Mei some beads, and now they have the same number. How many beads did Siti give Mei?', a: '27 (half of the difference).' },
      { q: 'Three boxes hold 600 pens altogether. Box A has 50 more pens than Box B. Box C has 50 more pens than Box A. How many pens are in Box C?', a: '250. Take away the extras (50 + 100 = 150): 450 ÷ 3 = 150 in Box B, so A has 200 and C has 250.' },
      { q: 'A bag of rice and a bag of flour weigh 9 kg altogether. The rice is 3 kg heavier than the flour. How heavy is each bag?', a: 'Flour 3 kg, rice 6 kg (9 − 3 = 6, 6 ÷ 2 = 3).' },
      { q: 'Mei is 8 years old. Her mother is 36. How old will Mei be when her mother is 3 times as old as Mei?', a: '14. The difference, 28 years, never changes. Mother 3 units, Mei 1 unit, so 2 units = 28 and Mei is 14 (mother 42).' },
      { q: 'Ali has $45. Ben has $18. Grandma gives each boy the same amount of money. Now Ali has twice as much money as Ben. How much money did Grandma give each boy?', a: '$9. The difference, $27, stays the same. Now Ali has 2 units and Ben 1 unit, so 1 unit = $27. Ben now has $27, so Grandma gave each boy $27 − $18 = $9. Check: $54 = 2 × $27.' },
      { q: 'Ben had 3 times as many marbles as Ravi. Ben gave Ravi 20 marbles, and then they had the same number. How many marbles did Ben have at first?', a: '60. The difference is 2 units and Ben gave half of it, so 1 unit = 20. Ravi had 20, Ben had 60.' },
      { q: 'A bag of sugar and 2 bags of flour have a total mass of 1700 g. Each bag of flour is 400 g heavier than the bag of sugar. What is the mass of the bag of sugar?', a: '300 g (1700 − 800 = 900 for 3 equal units, 900 ÷ 3 = 300).' },
      { q: 'Ali has saved $48. Ben has saved $15. From now on each boy saves $6 a week. After how many weeks will Ali have twice as much as Ben?', a: '3 weeks. The difference, $33, stays the same, so Ben must reach $33: $15 + $18. Then Ali has $66.' }
    ],
    challenge: [
      { q: 'Ali and Ben have 120 stickers altogether. Ali has 3 times as many as Ben. Ali gives some stickers to Ben, and then Ali has only twice as many as Ben. How many stickers does Ali give to Ben?', a: '10. At first 4 units = 120, so Ben 30 and Ali 90. The total is still 120, but now Ali has 2 parts and Ben 1 part, so 3 equal parts = 120 and each part is 40. Ben now has 40 and Ali 80. Ben went from 30 to 40, so Ali gave 10.' },
      { q: 'A pencil box and 3 pens cost $25 altogether. A pencil box and 5 pens cost $35 altogether. How much does one pen cost? How much does the pencil box cost?', a: 'Pen $5, box $10. The second bill is $10 more because it has 2 more pens, so 2 pens cost $10 and 1 pen $5. Then 3 pens cost $15, so the box costs $25 − $15 = $10.' },
      { q: 'Ali, Ben and Ravi have 185 marbles altogether. Ali has twice as many as Ben. Ben has 15 more than Ravi. How many marbles does each boy have?', a: 'Ravi 35, Ben 50, Ali 100.' },
      { q: 'Ravi, Mei and Siti have 160 beads altogether. Mei has 3 times as many beads as Siti. Ravi has 20 more beads than Mei. How many beads does each child have?', a: 'Siti 20, Mei 60, Ravi 80. Siti is 1 unit, Mei 3 units, Ravi 3 units and 20 more. Take away the extra 20: 140 for 7 equal units, so 1 unit = 20.' },
      { q: 'A club has 3 times as many boys as girls. Then 12 boys leave and 12 girls join, and now there are the same number of boys and girls. How many children are in the club?', a: '48 (12 girls and 36 boys at first; 24 and 24 after).' },
      { q: '2 jugs and 3 cups hold 1800 ml of water altogether. A jug holds 3 times as much as a cup. How much does a cup hold?', a: '200 ml. 2 jugs = 6 cups, so 9 cups = 1800 ml.' },
      { q: 'Make up your own before-and-after story about stickers or money, where one child gives some to another child. Draw its model, solve it and check it. Then change ONE number in your story. What changes in the answer, and what stays the same? Swap with a partner.', a: 'Answers vary. Check that the model matches the story, the total is the same before and after, and the child can explain what changed. Example: Ali has 50 stickers and Ben has 20. Ali gives Ben some so that they have the same number. (Ali gives 15; the difference is 30 and half of it is 15.) If Ali had 60, he would give 20: the difference grows by 10 and the gift by 5.' },
      { q: 'Ravi is 7 years old and his sister is 3. In how many years will their ages add up to 30? Explain how you know.', a: '10 years. Now they add up to 10, and each year the total grows by 2 (one year for each child). 30 − 10 = 20, and 20 ÷ 2 = 10. Check: 17 + 13 = 30.' },
      { q: 'A ribbon 4 m 75 cm long is cut into 3 pieces. The second piece is twice as long as the first. The third piece is 25 cm longer than the second. How long is the third piece?', a: '2 m 5 cm. 475 − 25 = 450 cm for 5 equal units, so 1 unit = 90 cm; third piece = 180 + 25 = 205 cm.' }
    ]
  },

  workbook: H => {
    const out = [];
    out.push(H.p('Draw a model. Label what you know. Put a ? on what you want to find.', { after: 40 }));
    // Q1
    out.push(H.q(1, 'A bakery made 1250 buns. It sold 486 buns in the morning and 378 buns in the afternoon.', { before: 60, keepNext: true }));
    out.push(H.fig(q1Fig()));
    out.push(H.p('Hint: add the two amounts sold first (486 + 378). Then take that away from 1250.', { after: 20 }));
    out.push(H.sub('a', 'How many buns were left?   ________'));
    out.push(H.sub('b', 'How many more buns were sold in the morning than in the afternoon?   ________'));
    // Q2
    out.push(H.q(2, 'Mei has 345 stickers. Ali has 128 more stickers than Mei. Ben has 79 fewer stickers than Ali.', { keepNext: true }));
    out.push(H.fig(q2Fig()));
    out.push(H.p('Hint: find Ali first (compare with Mei). Then find Ben (compare with Ali, not Mei).', { after: 20 }));
    out.push(H.sub('a', 'Ali has ______ stickers.      Ben has ______ stickers.'));
    out.push(H.sub('b', 'How many stickers do the three children have altogether?   ______'));
    // Q3
    out.push(H.q(3, 'Siti has 3 times as many beads as Ravi. They have 248 beads altogether. Each box in the picture is 1 unit (one equal part).', { keepNext: true }));
    out.push(H.fig(q3Fig()));
    out.push(H.sub('a', 'How many units are there altogether?   ______      1 unit = ______ beads'));
    out.push(H.sub('b', 'Siti has ______ beads. She has ______ more beads than Ravi.'));
    // ---------- page 2 ----------
    out.push(H.q(4, 'Ali and Ben have 150 marbles altogether. Ali has 24 more marbles than Ben. How many marbles does each boy have?', { pb: true, before: 0, keepNext: true }));
    out.push(H.p('Hint: you can guess and check. Try Ben = 50, so Ali = 74. Is the total 150? Too big or too small? Try again.', { after: 20 }));
    out.push(H.fig(drawBox(100)));
    out.push(H.sub('', 'Ben: ________      Ali: ________'));
    out.push(H.q(5, 'Mei has 85 stickers. Siti has 47 stickers. Mei gives some stickers to Siti so that they both have the same number.', { keepNext: true }));
    out.push(H.p('Hint: try giving 10 stickers. Do they have the same number now? Keep trying.', { after: 20 }));
    out.push(H.fig(drawBox(100)));
    out.push(H.sub('a', 'How many stickers does Mei give Siti?   ________'));
    out.push(H.sub('b', 'Ravi says, "Mei must give Siti 38 stickers, because 85 − 47 = 38." What mistake did Ravi make?'));
    out.push(...H.lines(2));
    out.push(H.q(6, 'Ali has $45. Ben has $18. Grandma gives each boy $10.', { keepNext: true }));
    out.push(H.fig(drawBox(120)));
    out.push(H.sub('a', 'How much more money does Ali have than Ben now?   ________'));
    out.push(H.sub('b', 'How much more did Ali have than Ben before Grandma gave the money?   ________'));
    out.push(H.sub('c', 'What do you notice? Why?'));
    out.push(...H.lines(1));
    return out;
  }
};
