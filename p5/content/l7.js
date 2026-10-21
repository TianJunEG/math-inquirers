// Math Inquirers P5 — Lesson 7: Percentage Puzzles (percentage of a quantity, discount, GST, increase and decrease, percentage of a remainder)
// Every answer below was worked out and checked with exact fractions in Python. GST in Singapore is 9%.

const N = '#1B2A49', Y = '#FFC93C', SKY = '#DDEBF7', TEAL = '#1F7A6F', RED = '#D64545', WH = '#FFFFFF';
const F = 'Fredoka, Arial, sans-serif';
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const svg = (w, h, label, inner) => `<svg aria-label="${esc(label)}" viewBox="0 0 ${w} ${h}" xmlns="http://www.w3.org/2000/svg" style="width:${w}px;max-width:100%">${inner}</svg>`;
const tx = (x, y, s, size = 16, fill = N, anchor = 'middle', weight = 700) => `<text x="${x}" y="${y}" font-size="${size}" font-weight="${weight}" text-anchor="${anchor}" fill="${fill}" font-family="${F}">${esc(s)}</text>`;

// Q2: two shop signs for the rice cooker
const shopsFig = () => {
  const tag = (x, fill, lines, title) => {
    let s = `<polygon points="${x},60 ${x + 34},8 ${x + 280},8 ${x + 280},112 ${x + 34},112" fill="${fill}" stroke="${N}" stroke-width="3" stroke-linejoin="round"/><circle cx="${x + 30}" cy="60" r="7" fill="${WH}" stroke="${N}" stroke-width="2.5"/>`;
    s += tx(x + 160, 34, title, 18, N);
    lines.forEach((l, i) => { s += tx(x + 160, 60 + i * 22, l, 15, i === 0 ? TEAL : N, 'middle', i === 0 ? 700 : 600); });
    return s;
  };
  return svg(600, 120, 'Two price tags. Shop A: rice cooker 160 dollars before GST, 20 percent off, 9 percent GST added at the till. Shop B: the same rice cooker for 140 dollars, GST included.',
    tag(4, Y, ['$160 before GST', '20% OFF today!', '9% GST added at the till'], 'Shop A') +
    tag(312, SKY, ['$140', 'GST already included', 'No sale today'], 'Shop B'), 0.8);
};

// Q4: a bar of $120 cut into 10 equal parts, with an empty bar for the remainder
const barFig = () => {
  let s = '';
  const x0 = 40, w = 52;
  for (let i = 0; i < 10; i++) s += `<rect x="${x0 + i * w}" y="30" width="${w}" height="38" fill="${WH}" stroke="${N}" stroke-width="2.5"/>`;
  s += `<path d="M${x0} 24 V16 H${x0 + 10 * w} V24" fill="none" stroke="${N}" stroke-width="2"/>` + tx(x0 + 5 * w, 12, '$120', 16);
  s += tx(x0 + 5 * w, 92, 'Each part is 10% of $120. Shade the bag. Then split what is left into 4 equal parts.', 14, N, 'middle', 600);
  return svg(600, 100, 'A bar for 120 dollars cut into 10 equal parts', s);
};

module.exports = {
  lesson: {
    n: 7, week: 4, session: 'A', title: 'Percentage Puzzles', topic: 'Percentage',
    objective: 'Find any percentage of an amount by building it from 10%, 5% and 1%; work out a discount and then 9% GST on the sale price; find a percentage of a remainder; and spot the classic percentage traps. (A preview of P6, on the Think Harder page: find a percentage increase or decrease by comparing the change with the original amount.)',
    skills: 'Asking "percentage of what?", building from 10% and 1%, bar models, making a table, comparing deals, explaining a trap',
    materials: 'Mini whiteboard and marker, workbook, pencil, a hundred-square page (or squared paper), a calculator for checking only at the end of each page.',
    online: 'Children keep the workbook and a whiteboard in front of the camera. The tutor screen-shares the slides and draws bar models with the annotation tool. Calculators stay closed until the check-together slides.',
    warmup: 'Hundred-square snap: three 10 by 10 squares with part shaded. Children write the percentage shaded AND the percentage not shaded on their whiteboards before the reveal.',
    explore: 'Up 10%, down 10%. A $200 bicycle goes up by 10%, then down by 10% of the new price. Pairs predict first, then work it out both ways round (up first, down first) and compare.',
    mini: '10% is one tenth: divide by 10. Half of 10% is 5%; 1% is one hundredth. Build any percentage from these. For a discount then GST: take off the discount first, then work out 9% of the SALE price. Always ask: percentage of WHAT?',
    share: 'Which is better for the shopper: add 9% GST first and then take 20% off, or take 20% off first and then add 9% GST?',
    exit: { q: 'A $30 toy is sold at 20% off. Then 9% GST is added to the sale price. How much do you pay?', a: '$26.16 (20% of $30 = $6, sale price $24; 9% of $24 = $2.16; $24 + $2.16 = $26.16)' },
    mistakes: ['Adding percentages of different wholes: 20% of the money and then 25% of the REMAINDER is not 45% of the money.', 'Thinking that going up by a percentage and then down by the same percentage brings you back to the start.', 'Working out a percentage increase or decrease using the new amount instead of the original amount, or adding GST to the price before the discount and then taking the discount off the wrong amount.'],
    extension: 'A shop raises every price by 25%, then has a "20% off everything" sale. Is the sale price more than, less than or the same as the old price? Try it with $40, $100 and $64. Can you explain why?',
    key: [
      ['Q1', '10%: $24   5%: $12   1%: $2.40   15%: $36   35%: $84   99%: $237.60.  (a) 35% = 3 × 10% + 5% = $72 + $12 = $84.  (b) 99% = 100% − 1% = $240 − $2.40 = $237.60.'],
      ['Q2', '(a) $128 (20% of $160 = $32)  (b) $11.52 (10% of $128 = $12.80, 1% = $1.28; $12.80 − $1.28)  (c) $139.52  (d) Shop A, by 48¢ ($140 − $139.52)'],
      ['Q3', '(a) $100 (25% of $80 = $20)  (b) $80 (20% of $100 = $20)  (c) No. The 20% is taken from $100, not from $80. 20% of $100 is $20, the same $20 that was added, so the price is back to $80, not $84.'],
      ['Q4', '(a) $24 (20% of $120)  (b) $24 (25% of the $96 left)  (c) $72  (d) 60%. The 25% is of the $96 left, not of $120, so she spent $48 of $120 = 40% and 60% is left ($72 out of $120).'],
      ['Q5', 'Girls 24, boys 16. Glasses: girls 6 (25% of 24), boys 8 (50% of 16), whole class 14.  (a) 35% (14 out of 40)'],
      ['Think Harder Q1 (a P6 preview: percentage change)', '(a) 25% ($1 out of $4)  (b) 20% ($1 out of $5)  (c) A percentage change compares the change with the starting amount. $1 out of $4 is a bigger part than $1 out of $5.'],
      ['Think Harder Q2', '(a) Shop X $45 (pays for 3 boxes); Shop Y $42 (30% of $60 = $18 off). Shop Y is the better buy, by $3.  (b) 25% (1 box free out of 4, $15 off $60)']
    ]
  },

  script: {
    hook: ['Welcome back, inquirers! Look around any shop in Singapore and you will see percentages everywhere: 20% off, 9% GST, prices up 10%. Shops are very good at percentages. Today we make sure we are better.', 'Notice it, test it, explain why. Today the big question is always: percentage of WHAT?'],
    warmIntro: ['Here are three hundred-squares. Each one has 100 small squares. Write how much is shaded as a percentage, and how much is NOT shaded. Whiteboards up when I say go.', 'Did anyone find the "not shaded" part without counting? How?'],
    predict: ['A bicycle costs $200. The price goes up by 10%. Later the new price goes down by 10%. What is the price now? Write your prediction before you work anything out.', 'Thumbs up if you think it is back to $200. Thumbs down if you think it is less. Sideways if you think it is more.'],
    exploreHints: ['Stuck: what is 10% of $200? Add it on. Now what is 10% of the NEW price?', 'Got $200: check which amount you took 10% of the second time. Was it $200 or $220?', 'Finished early: try up 50% then down 50%. Is the gap bigger or smaller than with 10%?'],
    think: ['“I want 45% of $60. 10% is one tenth, so I divide by 10: $6. Half of that is 5%: $3. 45% is four 10%s and one 5%: $24 + $3 = $27.”', '“98% is nearly all of it. So I find what is missing: 2%. 1% of $60 is 60 cents, so 2% is $1.20, and 98% is $60 − $1.20 = $58.80.”', '“For the fan I take off the discount first: 15% of $120 is $18, so the sale price is $102. The GST is 9% of $102, not of $120. 10% of $102 is $10.20, 1% is $1.02, so 9% is $9.18. I pay $111.18.”'],
    circulate: ['Ask: “Percentage of what? Point to the whole.”', 'Ask: “Can you build that percentage from 10%, 5% and 1%?”', 'Ask: “After the first change, what is the new whole?”'],
    hints: ['Hint 1: “Find 10% first by dividing by 10.”', 'Hint 2: “Draw a bar for the whole and cut it into 10 equal parts.”', 'Hint 3: “Write what the whole is BEFORE you work out each percentage.”'],
    talk: ['“Which is better for the shopper: add 9% GST first and then take 20% off, or take 20% off first and then add 9% GST?”', '“Mei says 20% off and then 9% GST is the same as 11% off. Is she right?”'],
    talkAns: 'They give exactly the same price. On $100: GST first gives $109, then 20% off gives $87.20; 20% off first gives $80, then GST gives $87.20. Each change multiplies the price, and the order of multiplying does not matter. Mei is not right: 11% off $100 is $89, not $87.20, because the 9% GST is worked out on the smaller sale price.',
    close: ['“Today you found that percentages can trick you when the whole changes. Before every percentage, ask: of what? Well done, inquirers!”', '“Show me your exit ticket and I will stamp your inquiry journal.”']
  },

  deck: {
    today: 'Build any percentage from 10%, 5% and 1%, work out discounts and GST, and catch the percentage traps.',
    warmGame: 'Hundred-square snap. Three 10 by 10 squares have part shaded (30, 45 and 64 small squares). Write the percentage shaded and the percentage not shaded before the reveal.',
    warmQs: [['50% of $90', '$45'], ['10% of 350', '35'], ['25% of 48', '12'], ['1% of $700', '$7'], ['3 out of 20 as a percentage', '15%']],
    expSetup: ['A bicycle costs $200. Predict: if the price goes up 10% and then down 10%, what is it?', 'Work it out: up 10% first. Then take 10% of the NEW price off.', 'Now try it the other way: down 10% first, then up 10%.', 'Compare both answers with your prediction. What do you notice?'],
    expPic: 'a $200 price tag, an arrow marked "+10%" to a tag with a question mark, then an arrow marked "−10%" to another tag with a question mark.',
    expAsk: [['Is the price back to $200?', 'No: $200 → $220 → $198.'], ['Does the order matter?', 'No: $200 → $180 → $198 too.'], ['Why is it $2 less?', 'The 10% taken off is 10% of $220 = $22, which is more than the $20 that was added.']],
    mini1: { head: 'Build it from 10%, 5% and 1%', body: ['Find 45% and 98% of $60.', '10% = $6, 5% = $3, so 45% = $24 + $3.', '1% = $0.60, so 98% = $60 − $1.20.'], ans: '45% of $60 = $27; 98% of $60 = $58.80.' },
    mini2: { head: 'Discount first, then GST', body: ['A fan costs $120 before GST. It is sold at 15% off. Then 9% GST is added.', '15% of $120 = $18, so the sale price is $102.', '9% of $102 = $10.20 − $1.02.'], ans: 'GST $9.18; you pay $111.18.' },
    keyHead: 'Key idea: percentage of WHAT?',
    keyBig: 'Build any percentage from 10%, 5% and 1%. Before each step, ask: percentage of what?',
    keySmall: 'Take the discount off first, then work out GST on the sale price. After a change, the new amount is the new whole.',
    brk: 'Percent stretch. The tutor calls out a percentage: 100% is standing tall with arms up, 50% is hands on your head, 25% is hands on your knees, 0% is sitting down. Then 75%? (hands on shoulders).',
    ws1: 'Page 1, in pairs: Q1 build percentages of $240, Q2 two shops and GST, Q3 up 25% then down 20%.',
    ws2: 'Page 2, on your own: Q4 percentage of a remainder, Q5 glasses in a class. Think Harder: Q1 percentage increase and decrease (a P6 preview), Q2 the better deal.'
  },

  qbank: {
    core: [
      { q: 'Find 10% of $360 and 15% of $360.', a: '$36 and $54 ($36 + $18)' },
      { q: 'A book costs $45. It is sold at a 20% discount. What is the sale price?', a: '$36 (20% of $45 = $9)' },
      { q: 'A meal costs $30 before GST. GST is 9%. How much is the meal with GST?', a: '$32.70 (9% of $30 = $2.70)' },
      { q: '24 of the 40 pupils in a class walk to school. What percentage walk to school?', a: '60% (24 out of 40 = 60 out of 100)' },
      { q: 'Ali had $60. He spent 25% of it. How much did he have left?', a: '$45' },
      { q: '21 of the 60 seats in a hall are empty. What percentage of the seats are empty?', a: '35% (21 out of 60 = 35 out of 100)' }
    ],
    stretch: [
      { q: 'At a hawker centre, a plate of chicken rice went up from $4 to $5. A month later, it went back down from $5 to $4. (a) Find the percentage increase from $4 to $5. (b) Find the percentage decrease from $5 to $4. (c) Both changes are $1. Why are the two percentages different? Hint: percentage change = the change out of the amount you START with.', a: '(a) 25% ($1 out of $4)  (b) 20% ($1 out of $5)  (c) Each change is compared with its own starting amount: $1 out of $4 is a bigger part than $1 out of $5. (Percentage change is a P6 skill: a preview.)' },
      { q: 'A box of cereal costs $15 in two shops. Shop X: "Buy 3, get 1 free!"  Shop Y: "30% off every box!"  Mei buys 4 boxes. (a) How much does she pay at each shop? Which is the better buy, and by how much? (b) Shop X\'s deal is really how many percent off?', a: '(a) Shop X $45 (she pays for 3 boxes); Shop Y $42 (30% of $60 = $18 off). Shop Y is the better buy, by $3.  (b) 25% off (1 box free out of 4, $15 off $60)' },
      { q: 'Siti says, "15% of $80 is $8 + $4 = $12." Explain her method. Use it to find 15% of $46.', a: 'She found 10% ($8) and 5% (half of 10%, $4) and added them. 15% of $46 = $4.60 + $2.30 = $6.90.' },
      { q: 'A $250 bicycle is sold at a 12% discount. How much money is saved? What is the sale price?', a: 'Saved $30 (10% = $25, 2% = $5); sale price $220.' },
      { q: 'A watch costs $80 before GST. GST is 9%. Mei pays with a $100 note. How much change does she get?', a: '$12.80 (GST $7.20, so the watch costs $87.20)' },
      { q: 'Siti had $200. She spent 40% of it on shoes and 50% of the rest on a bag. How much money did she have left?', a: '$60 (shoes $80, $120 left, bag $60, $60 left)' },
      { q: 'Which is bigger: 30% of 70 or 70% of 30? Try another pair like this. What do you notice?', a: 'They are the same: both are 21. In general, a% of b is the same as b% of a (for example 4% of 25 = 25% of 4 = 1).' },
      { q: 'Ravi scored 18 out of 25 in Test A and 27 out of 40 in Test B. In which test did he do better?', a: 'Test A: 72% (18 out of 25) is more than 67.5% (27 out of 40).' }
    ],
    challenge: [
      { q: 'A $100 jacket goes up by 20%, then the new price goes down by 20%. What is the final price? Is it a percentage increase or decrease from $100, and how much?', a: '$96 ($120, then 20% of $120 = $24 off). A 4% decrease.' },
      { q: 'After a 20% discount, a shirt costs $40. Ben says the price before the discount was $48. Is he right? Find the price before the discount.', a: 'No. $40 is 80% of the old price, so 10% is $5 and 100% is $50. (Ben added 20% of $40, but the 20% was of the old price.)' },
      { q: 'A tank is 40% full. After 60 ℓ of water is poured in, it is 70% full. How much water can the tank hold?', a: '200 ℓ (the 60 ℓ is 30% of the tank, so 10% is 20 ℓ)' },
      { q: 'Mei\'s score went up by 20% from Test 1 to Test 2. Then it went down by 20% from Test 2 to Test 3. Her Test 3 score was 48. What was her Test 1 score?', a: '50. Work backwards: 48 is 80% of Test 2, so Test 2 = 60; 60 is 120% of Test 1, so Test 1 = 50.' },
      { q: 'A school has 800 pupils. 45% are boys. 20% of the boys and 30% of the girls take the school bus. What percentage of all the pupils take the bus?', a: '25.5% (boys 360, 72 take the bus; girls 440, 132 take the bus; 204 out of 800)' },
      { q: 'A box has 20 marbles. 75% of them are red and the rest are blue. How many red marbles must be taken out so that only 50% of the marbles left are red?', a: '10. The 5 blue marbles stay. If they are 50% of the box, there are 10 marbles left, so 20 − 10 = 10 red marbles are taken out.' },
      { q: 'A price tag says $109, GST included. GST is 9%. Ali says the GST is 9% of $109, which is $9.81. Is he right? How much GST is in the price?', a: 'No. $109 is 109% of the price before GST, so 1% is $1 and the GST is $9. (9% of $109 is wrong because GST is 9% of the price BEFORE GST.)' },
      { q: 'An $80 lamp is on sale in two shops. Shop P takes 25% off. Shop Q takes 10% off, and then a further 15% off the new price. In which shop is the lamp cheaper, and by how much?', a: 'Shop P, by $1.20. P: $80 − $20 = $60. Q: $80 − $8 = $72, then 15% of $72 = $10.80 off, $61.20.' },
      { q: 'Mrs Tan spent 40% of her money on groceries and 25% of the remaining money on a gift. She had $54 left. How much money did she have at first?', a: '$120. Work backwards: $54 is 75% of the remainder, so the remainder is $72. $72 is 60% of her money, so 10% is $12 and 100% is $120.' }
    ]
  },

  workbook: H => [
    H.q(1, 'Percent means "out of 100". Build percentages of $240 from 10%, 5% and 1%. Fill in the table.', { before: 20, keepNext: true }),
    H.tbl([2100, 1300, 1300, 1300, 1300, 1300, 1300], [
      H.row(['Percentage', '10%', '5%', '1%', '15%', '35%', '99%'].map((s, i) => H.cell(s, i ? 1300 : 2100, { bold: true, fill: 'D9D9D9', h: 40 }))),
      H.row(['of $240', ' ', ' ', ' ', ' ', ' ', ' '].map((s, i) => H.cell(s, i ? 1300 : 2100, { bold: !i, h: 50 })))
    ]),
    H.sub('a', 'How did you find 35% from the boxes you already had?  ____________________________', { after: 40 }),
    H.sub('b', 'A quick way to find 99% of $240:  ____________________________', { after: 40 }),
    H.q(2, 'Mei wants a rice cooker. Two shops sell the same one. GST is 9%.', { keepNext: true }),
    H.fig(shopsFig()),
    H.sub('a', 'Shop A: the price after 20% off, before GST.      ____________'),
    H.sub('b', 'Shop A: the GST on the sale price.      ____________'),
    H.sub('c', 'Shop A: the price Mei pays.      ____________'),
    H.sub('d', 'Which shop is cheaper? By how much?      ________________________'),
    H.q(3, 'A T-shirt cost $80. The shop raised its price by 25%. A month later, it cut the new price by 20%.', { keepNext: true }),
    H.sub('a', 'The price after the 25% rise:   ____________          (b)  The price after the 20% cut:   ____________'),
    H.sub('c', 'Siti says, "Up 25% and then down 20% is the same as up 5%, so the final price is $84." Is she right? Explain.', { after: 40 }),
    ...H.lines(1),

    H.q(4, 'Siti had $120. She spent 20% of her money on a bag. Then she spent 25% of the remaining money on a book.', { pb: true, before: 0, keepNext: true }),
    H.fig(barFig()),
    H.sub('a', 'The bag cost  ________        (b)  The book cost  ________        (c)  Money left  ________'),
    H.sub('d', 'Ben says, "She spent 20% + 25% = 45%, so 55% of her money is left." What percentage of her money is really left? Explain.', { after: 40 }),
    ...H.lines(1),
    H.q(5, 'There are 40 pupils in a class. 60% of them are girls. 25% of the girls and 50% of the boys wear glasses. Fill in the table.', { keepNext: true }),
    H.tbl([3300, 2200, 2200, 2200], [
      H.row([' ', 'Girls', 'Boys', 'Whole class'].map((s, i) => H.cell(s, i ? 2200 : 3300, { bold: true, fill: 'D9D9D9', h: 40 }))),
      H.row(['Number of pupils', ' ', ' ', '40'].map((s, i) => H.cell(s, i ? 2200 : 3300, { bold: !i, h: 60 }))),
      H.row(['Wear glasses', ' ', ' ', ' '].map((s, i) => H.cell(s, i ? 2200 : 3300, { bold: !i, h: 60 })))
    ]),
    H.sub('a', 'What percentage of the whole class wear glasses?      ____________')
  ]
};
