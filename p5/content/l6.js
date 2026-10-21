// Math Inquirers P5 — Lesson 6: Rate Racers (rate per unit, better buys, taps and printers, charges, comparing plans)
// Every answer below was worked out with exact fractions; the "fewest cost" answers were checked against every possible mix of packs.

const NAVY = '#1B2A49', YEL = '#FFC93C', SKY = '#DDEBF7', TEAL = '#1F7A6F', RED = '#D64545', WHITE = '#FFFFFF', CREAM = '#FFF9EC';
const F = 'Arial, sans-serif';
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const tx = (x, y, s, o = {}) => `<text x="${x}" y="${y}" font-size="${o.size || 16}" font-weight="${o.w || 700}" text-anchor="${o.a || 'middle'}" fill="${o.fill || NAVY}" font-family="${F}">${esc(s)}</text>`;
const svg = (w, h, label, inner, dw) => `<svg aria-label="${esc(label)}" viewBox="0 0 ${w} ${h}" xmlns="http://www.w3.org/2000/svg" style="width:${dw || w}px;max-width:100%">${inner}</svg>`;

// three shop price boards
const figShops = () => {
  const board = (x, name, l1, l2, l3, fill) =>
    `<rect x="${x}" y="8" width="180" height="128" rx="12" fill="${fill}" stroke="${NAVY}" stroke-width="2.5"/>` +
    `<rect x="${x}" y="8" width="180" height="32" rx="12" fill="${NAVY}"/><rect x="${x}" y="28" width="180" height="12" fill="${NAVY}"/>` +
    tx(x + 90, 31, name, { fill: WHITE, size: 17 }) + tx(x + 90, 70, l1, { size: 17 }) + tx(x + 90, 100, l2, { size: 22 }) + (l3 ? tx(x + 90, 126, l3, { size: 15, fill: RED }) : '');
  return svg(600, 144, 'Shop A: 6 cans for $4.20. Shop B: 4 cans for $2.92. Shop C: pack of 10 cans for $7.80, get 2 more cans free.',
    board(10, 'SHOP A', 'Pack of 6 cans', '$4.20', '', WHITE) + board(210, 'SHOP B', 'Pack of 4 cans', '$2.92', '', WHITE) + board(410, 'SHOP C', 'Pack of 10 cans', '$7.80', '+ 2 cans FREE!', '#FFF0C2'), 300);
};
// a tank with two taps and a leak
const figTaps = () => {
  let s = `<rect x="150" y="110" width="300" height="110" fill="${WHITE}" stroke="${NAVY}" stroke-width="3"/><rect x="152" y="150" width="296" height="68" fill="${SKY}"/>`;
  s += tx(300, 195, 'holds 240 ℓ', { size: 22 });
  s += `<path d="M30 66 H250 V104" fill="none" stroke="${NAVY}" stroke-width="10" stroke-linecap="round"/><path d="M650 66 H350 V104" fill="none" stroke="${NAVY}" stroke-width="10" stroke-linecap="round"/>`;
  s += `<line x1="250" y1="112" x2="250" y2="146" stroke="#7FB2DE" stroke-width="6" stroke-dasharray="8 5"/><line x1="350" y1="112" x2="350" y2="146" stroke="#7FB2DE" stroke-width="6" stroke-dasharray="8 5"/>`;
  s += tx(30, 40, 'Tap A: 12 ℓ a min', { a: 'start', size: 22 }) + tx(650, 40, 'Tap B: 18 ℓ a min', { a: 'end', size: 22 });
  s += `<circle cx="430" cy="232" r="4" fill="#7FB2DE"/><circle cx="440" cy="246" r="4" fill="#7FB2DE"/>` + tx(456, 244, 'crack: 6 ℓ a min out', { a: 'start', size: 22, fill: RED });
  return svg(680, 260, 'A 240-litre tank filled by tap A at 12 litres a minute and tap B at 18 litres a minute, with a crack that lets out 6 litres a minute', s, 250);
};
const figPark = () => svg(440, 132, 'Car park sign: first hour $1.20; after that 60 cents for every half hour or part of a half hour',
  `<rect x="6" y="6" width="428" height="120" rx="14" fill="${WHITE}" stroke="${NAVY}" stroke-width="3"/><circle cx="56" cy="66" r="34" fill="${TEAL}"/>` + tx(56, 80, 'P', { size: 40, fill: WHITE }) +
  tx(104, 38, 'CITY CAR PARK', { a: 'start', size: 18, fill: TEAL }) + tx(104, 70, 'First hour:  $1.20', { a: 'start', size: 18 }) +
  tx(104, 98, 'After that:  60¢ for every half hour', { a: 'start', size: 16 }) + tx(104, 118, 'or part of a half hour', { a: 'start', size: 16 }));

module.exports = {
  lesson: {
    n: 6, week: 3, session: 'B', title: 'Rate Racers', topic: 'Rate',
    objective: 'Find a rate for 1 unit and use it to scale up or work backwards in a rate table; compare buys by the price of one item; add rates when taps or printers work together and take away a leak; work out charges “for every half hour or part of it”; and compare two price plans with a table.',
    skills: 'Find the value of 1 unit, make a table, compare, guess and check with a table, draw a timeline, check with a second method',
    materials: 'Mini whiteboards, a calculator for checking only, a stopwatch (or phone), a few real price tags or supermarket flyers if you have them.',
    online: 'Children hold whiteboards up to the camera; the tutor fills the rate tables on the slides. Pairs work in breakout rooms for the Explore. The brain break uses a phone stopwatch.',
    warmup: 'Better Buy Showdown: three pairs of packs (pens, juice, eggs). Children point left or right for the better buy, then prove it with the price of one. Then five quick rate questions.',
    explore: 'Printer race: Printer A prints 72 pages in 4 minutes and Printer B prints 50 pages in 2 minutes. Pairs build a rate table for each printer, decide which is faster, then predict and work out how long both printers together take to print 430 pages.',
    mini: 'A rate tells how much for 1 unit: per minute, per kg, per can. Find the value of 1 first, then multiply to scale up or divide to find how long. Better buy: compare the price of 1 (or of the same number of items). Working together: add the rates; a leak or drain takes its rate away. Worked examples: pens at two shops; two taps and a leak filling a 180 ℓ tank.',
    share: 'Is the biggest pack always the best buy? Give an example with numbers.',
    exit: { q: 'Tap A fills 15 ℓ a minute and tap B fills 10 ℓ a minute. How long do both taps together take to fill a 200 ℓ tank? How long if a leak also lets out 5 ℓ a minute?', a: '8 minutes (200 ÷ 25); with the leak 10 minutes (200 ÷ 20)' },
    mistakes: ['Adding or averaging the times when taps or printers work together (20 min and 30 min gives 50 min or 25 min) instead of adding the rates.', 'Choosing the better buy by the pack price, or dividing a free-gift deal by the cans paid for instead of all the cans received.', 'Charges “for every half hour or part of it”: dividing exactly instead of rounding up to the next half hour, or charging the first hour twice.'],
    extension: 'Make a better-buy poster: three pack sizes of the same snack where the biggest pack is NOT the best buy. Swap with a partner: can they find the best buy and prove it?',
    key: [
      ['Q1', '(a) Bottles: 16, 48, 80; minutes for 160 bottles: 10; 12 minutes: 192 bottles  (b) 9.25 a.m. (400 ÷ 16 = 25 minutes)'],
      ['Q2', '(a) A 70¢, B 73¢, C 65¢ (Shop C gives 12 cans for $7.80)  (b) Shop C  (c) Three ways make exactly 20 cans: 1 deal from C (12 cans) + 2 packs from B = $7.80 + $5.84 = $13.64 (the cheapest); 2 packs from A + 2 packs from B = $8.40 + $5.84 = $14.24; 5 packs from B = $14.60. Any correct way with its correct cost is fine'],
      ['Q3', '(a) 20 minutes (240 ÷ 12)  (b) 8 minutes (240 ÷ 30)  (c) 10 minutes (240 ÷ 24)  (d) 20 minutes (120 ÷ 6)'],
      ['Q4', '(a) 18 minutes (900 ÷ 50)  (b) 20 minutes (P prints 150 pages alone in 5 min; 750 ÷ 50 = 15 min more)  (c) 540 pages (both work 18 min: P 30 × 18 = 540, Q 20 × 18 = 360)'],
      ['Q5', '(a) $4.80 (3 h 35 min: first hour $1.20, then 2 h 35 min is 5 half hours and 5 min, so 6 lots of 60¢ = $3.60)  (b) 3 hours ($3.60 − $1.20 = $2.40 = 4 half hours after the first hour)'],
      ['Q6', '(a) Gym A $50, $70, $90; Gym B $35, $70, $105  (b) 10 visits  (c) Gym A, by $12 ($86 and $98)']
    ]
  },

  script: {
    hook: ['Welcome, Rate Racers! Today is about “how much for one”: one minute, one kilogram, one can. Once you know the rate for one, you can predict anything: how many pages in an hour, which pack is cheaper, when the tank will be full.', 'Shops, taps, printers and car parks all run on rates. By the end you will spot the trap in “Buy 10, get 2 free!”'],
    warmIntro: ['Better Buy Showdown! Two packs of the same thing. Point left or right: which is the better buy? Then prove it.', 'Pens: 3 for $2.40, or 5 for $3.80. Point now. Who can prove it?'],
    predict: ['Printer A prints 72 pages in 4 minutes. Printer B prints 50 pages in 2 minutes. Which is faster? Now both print a 430-page job together. Guess the time before you work it out.'],
    exploreHints: ['Stuck: how many pages does each printer print in 1 minute? Start the table with 1 minute.', 'Not sure how to compare: “Compare the same number of minutes for both printers.”', 'Finished early: how many pages should go to each printer so both finish at the same time?'],
    think: ['“5 kg of rice cost $9.50. I want the price of 1 kg first: $9.50 ÷ 5 = $1.90. Now anything is easy: 3 kg is 3 × $1.90 = $5.70. And backwards: $13.30 is 1330 cents and 1 kg costs 190 cents, so 1330 ÷ 190 = 133 ÷ 19 = 7 kg.”', '“Pens: 3 for $1.95 is 65¢ each. 5 for $3.10 is 62¢ each. So the 5-pack is the better buy, if I need that many. I check another way: 15 pens cost 5 × $1.95 = $9.75 or 3 × $3.10 = $9.30.”', '“Two taps fill 9 ℓ and 6 ℓ each minute. Together, every minute, 15 ℓ go in. 180 ÷ 15 = 12 minutes. A leak takes out 3 ℓ a minute, so only 12 ℓ stay in each minute: 180 ÷ 12 = 15 minutes.”'],
    circulate: ['Ask: “What is the rate for 1? One minute, one can, one kilogram?”', 'Ask: “How many cans do you really get in that deal?”', 'Ask: “Each minute, how much goes in and how much comes out?”'],
    hints: ['Hint 1: “Find the amount for 1 unit first.”', 'Hint 2: “Make a table: 1 minute, 2 minutes, 5 minutes … or draw a timeline.”', 'Hint 3: “Working together? Add the rates, not the times.”'],
    talk: ['“Is the biggest pack always the best buy? Give an example with numbers.”', '“Where did you see a bigger pack that was NOT the better buy today?”'],
    talkAns: 'No. Compare the price of 1: for example 3 pens for $1.95 is 65¢ a pen but 5 pens for $3.10 is 62¢ a pen (here the bigger pack is better); but if the 10-pack costs $7.50 and the 4-pack costs $2.80, the 4-pack is 70¢ a pen and the 10-pack is 75¢ a pen, so the small pack is the better buy. The better buy also depends on how many you really need.',
    close: ['“Today you found the rate for 1 and raced with it: scaling up, working backwards, adding taps together and catching the free-gift trap. Notice it, test it, explain why.”']
  },

  deck: {
    today: 'Find the rate for 1, compare better buys, add rates when taps and printers work together, and work out charges and price plans.',
    warmGame: 'Better Buy Showdown. Three pairs of packs: pens (3 for $2.40 or 5 for $3.80), juice (1.5 ℓ for $3.00 or 2 ℓ for $3.80), eggs (10 for $3.20 or 12 for $3.96). Point to the better buy, then prove it with the price of 1.',
    warmQs: [['4 kg of rice cost $10. How much is 1 kg?', '$2.50'], ['A printer prints 30 pages a minute. How many pages in 6 minutes?', '180 pages'], ['A tap lets out 450 ml in 3 minutes. How many ml a minute?', '150 ml'], ['Cheese costs $1.20 for 100 g. How much is 1 kg?', '$12'], ['Ali types 40 words a minute. How long for 200 words?', '5 minutes']],
    expSetup: ['Printer A prints 72 pages in 4 minutes. Printer B prints 50 pages in 2 minutes.', 'Make a rate table for each printer: 1, 2, 4 and 10 minutes.', 'Which printer is faster? Show how you know.', 'Predict, then work out: how long do both printers together take to print 430 pages?'],
    expPic: 'two printers side by side, A with “72 pages in 4 min” and B with “50 pages in 2 min”, above two empty rate tables with rows for minutes and pages.',
    expAsk: [['Which printer is faster? How do you know?', 'B: 25 pages a minute; A: 18 pages a minute. (Or compare 4 minutes: A 72, B 100.)'], ['How long do both together take for 430 pages?', '10 minutes: together 18 + 25 = 43 pages a minute, and 430 ÷ 43 = 10.'], ['Why is the rate for 1 minute so useful?', 'We can compare the printers fairly, multiply to scale up and divide to find a time.']],
    mini1: { head: 'Better buy: pens at 3 for $1.95 or 5 for $3.10', table: [['Pack', '3 pens', '5 pens'], ['Price', '$1.95', '$3.10'], ['1 pen', '65¢', '62¢']], body: ['Find the price of 1 pen at each shop.', 'Check another way: 15 pens cost $9.75 or $9.30.'], ans: 'The 5-pack is the better buy (62¢ a pen). But if Mei needs only 3 pens, the 3-pack costs less.' },
    mini2: { head: 'Taps together: a 180 ℓ tank, taps of 9 ℓ and 6 ℓ a minute', body: ['Together: 9 + 6 = 15 ℓ a minute, so 180 ÷ 15 = 12 minutes.', 'A leak lets out 3 ℓ a minute: 15 − 3 = 12 ℓ stay in each minute.', '180 ÷ 12 = 15 minutes.'], ans: '12 minutes; with the leak, 15 minutes. Add the rates, never the times.' },
    keyHead: 'Key idea: find the rate for 1',
    keyBig: 'Find how much for 1 unit (1 minute, 1 kg, 1 can). Multiply to scale up; divide to find how many or how long.',
    keySmall: 'Working together, the rates add. A leak or drain takes its rate away. Compare buys by the price of 1, counting every item you get.',
    brk: 'Rate race! How many star jumps can you do in 10 seconds? Predict your 1-minute total (× 6). Then test for 30 seconds: does your rate stay the same?',
    ws1: 'Page 1, in pairs: Q1 the bottling machine, Q2 the best buy, Q3 the taps and the crack.',
    ws2: 'Page 2, on your own: Q4 the printers, Q5 the car park, Q6 the two gyms.'
  },

  qbank: {
    core: [
      { q: '4 apples cost $2. How much do 8 apples cost? How much do 12 apples cost? How much does 1 apple cost? (Make a table if it helps.)', a: '$4; $6; 50¢ each.' },
      { q: 'A printer prints 24 pages a minute. How long does it take to print 360 pages?', a: '15 minutes' },
      { q: 'Pack A has 3 pens for $2. Pack B has 6 pens for $5. Which is the better buy? (Hint: how much would 6 pens cost if you bought Pack A twice?)', a: 'Pack A. Two Pack A cost $4 for 6 pens, but Pack B costs $5 for 6 pens. (Pack A is about 67¢ a pen and Pack B is about 83¢ a pen.)' },
      { q: 'A tap fills a 120 ℓ tank at 8 ℓ a minute. How long does it take?', a: '15 minutes' },
      { q: 'Tap A fills 2 litres every minute and tap B fills 3 litres every minute. Both are turned on together. How many litres are in the tank after 1 minute? After 2 minutes? After 5 minutes? How long do they take to put in 20 litres?', a: '5 litres after 1 minute, 10 after 2 minutes, 25 after 5 minutes. 20 litres takes 4 minutes (5 + 5 + 5 + 5).' },
      { q: 'Nuts cost $1.50 for every 100 g. How much do 650 g cost?', a: '$9.75' }
    ],
    stretch: [
      { q: 'A tap fills a tank in 12 minutes at 15 ℓ a minute. When a second tap is also turned on, the tank fills in 9 minutes. How many litres a minute does the second tap fill?', a: '5 ℓ a minute (the tank holds 180 ℓ; 180 ÷ 9 = 20 ℓ a minute together; 20 − 15 = 5)' },
      { q: 'Eggs are sold in boxes of 10 for $3.30 and boxes of 6 for $2.10. Siti needs at least 28 eggs. What is the least she can pay?', a: '$9.60 (one box of 10 and three boxes of 6 make 28 eggs; three boxes of 10 cost $9.90)' },
      { q: 'A car park charges $1.50 for the first hour and $1 for every half hour or part of a half hour after that. How much does it cost to park from 10.15 a.m. to 2.50 p.m.?', a: '$9.50 (4 h 35 min: first hour, then 3 h 35 min is 8 half hours or parts)' },
      { q: 'Phone plan A costs $15 a month plus 10¢ a minute. Plan B costs 25¢ a minute with no monthly fee. For how many minutes in a month do the two plans cost the same?', a: '100 minutes (Plan B costs 15¢ more each minute; $15 ÷ 15¢ = 100; both cost $25)' },
      { q: '3 machines make 360 masks in 4 minutes. At the same rate, how many masks do 5 machines make in 6 minutes?', a: '900 (1 machine makes 30 masks a minute: 30 × 5 × 6)' },
      { q: 'Shop X sells pens at 80¢ each. Shop Y sells 4 pens for $3.00 and gives 1 extra pen free with every 4 pens bought. Mei needs 20 pens. Which shop is cheaper, and by how much?', a: 'Shop Y by $4. At X, 20 pens cost $16.00. At Y, each deal gives 5 pens for $3.00, so 20 pens are 4 deals, $12.00.' },
      { q: 'A full tank holds 300 ℓ. A drain lets out 15 ℓ a minute, but a tap is left on that adds 5 ℓ a minute. How long does the tank take to empty?', a: '30 minutes (300 ÷ 10)' },
      { q: 'A dripping tap drips 5 ml of water every 2 seconds. How many litres of water does it waste in one whole day?', a: '216 ℓ (in 1 day there are 86 400 seconds, 43 200 drips of 5 ml is 216 000 ml).' }
    ],
    challenge: [
      { q: 'Printer P prints a job in 6 minutes. Printer Q prints the same job in 3 minutes. How long do they take working together?', a: '2 minutes (pretend the job is 6 pages: P prints 1 page a minute, Q 2 pages, together 3 a minute)' },
      { q: 'Siti buys pens at 3 for $2 and sells them at 2 for $2. How many pens must she buy and sell to make a profit of $10?', a: '30 pens (6 pens cost $4 and sell for $6: $2 profit for every 6 pens)' },
      { q: 'A machine starts at 9.52 a.m. and makes 50 cups a minute. At 10.00 a.m. a second machine starts, making 30 cups a minute. At what time have they made 1600 cups altogether?', a: '10.15 a.m. (400 cups by 10.00; 1200 ÷ 80 = 15 minutes more)' },
      { q: 'Ben needs at least 20 cans. Shop A sells 6 cans for $4.20, shop B sells 4 cans for $2.92 and shop C sells a deal of 10 cans for $7.80 with 2 cans free. He can buy from more than one shop, but only whole packs. What is the least he can pay?', a: '$13.64 (1 deal from C and 2 packs from B make 20 cans). Check the bigger totals: 22 cans cost at least $14.92 (C + A + B) and 24 cans cost at least $15.60 (2 deals from C), so they cannot be cheaper.' },
      { q: 'A tap fills 9 ℓ a minute. How long does it take to fill an empty tank 60 cm long, 50 cm wide and 45 cm high?', a: '15 minutes (135 000 cm³ = 135 ℓ; 135 ÷ 9)' },
      { q: 'Make up your own better-buy puzzle: three pack sizes of the same snack where the BIGGEST pack is NOT the best buy. Give the sizes and prices, swap with a partner, and ask them to find the best buy and prove it. What price would make the biggest pack the best buy?', a: 'Open-ended. Sample: 6 for $3.00 (50¢ each), 10 for $5.50 (55¢ each) and 12 for $7.20 (60¢ each): the 6-pack is the best buy. If the 12-pack cost $5.40 or less (45¢ each or less) it would be the best buy.' },
      { q: '3 cats eat 3 fish in 3 minutes. At this rate, how many cats are needed to eat 100 fish in 100 minutes?', a: '3 cats (each cat eats 1 fish every 3 minutes, so the 3 cats eat 1 fish a minute: 100 fish in 100 minutes)' },
      { q: 'Candle A is 20 cm tall and burns down 2 cm every hour. Candle B is 14 cm tall and burns down 1 cm every hour. They are lit at the same time. After how many hours are they the same height? How tall are they then?', a: 'After 6 hours, both 8 cm tall (the gap of 6 cm closes by 1 cm each hour)' },
      { q: 'A tap fills an empty bath in 12 minutes. With the plug out, a full bath empties in 20 minutes. Ben turns on the tap but forgets the plug. How long does the bath take to fill?', a: '30 minutes (pretend the bath holds 60 ℓ: 5 ℓ a minute in, 3 ℓ a minute out, 2 ℓ a minute stay: 60 ÷ 2)' }
    ]
  },

  workbook: H => {
    const t = h => '<div style="text-align:left;font-size:16px;line-height:1.55">' + h + '</div>';
    const L = s => '<b style="color:#1F7A6F">' + s + '</b> ';
    const rw = [2400, 1500, 1500, 1500, 1500, 1500];
    const rateTbl = H.tbl(rw, [
      H.row([H.cell('Minutes', rw[0], { bold: true, fill: 'D9D9D9', h: 38 }), ...['1', '3', '5', '', '12'].map((s, i) => H.cell(s, rw[i + 1], { bold: true, h: 38, fill: s ? 'EDEDED' : undefined }))]),
      H.row([H.cell('Bottles', rw[0], { bold: true, fill: 'D9D9D9', h: 38 }), ...['', '48', '', '160', ''].map((s, i) => H.cell(s, rw[i + 1], { bold: true, h: 38, fill: s ? 'EDEDED' : undefined }))])
    ]);
    const gw = [2400, 2500, 2500, 2500];
    const gymTbl = H.tbl(gw, [
      H.row(['Number of visits', '5', '10', '15'].map((s, i) => H.cell(s, gw[i], { bold: true, fill: 'D9D9D9', h: 50 }))),
      H.row([H.cell('Gym A costs', gw[0], { bold: true, h: 60 }), H.cell('', gw[1]), H.cell('', gw[2]), H.cell('', gw[3])]),
      H.row([H.cell('Gym B costs', gw[0], { bold: true, h: 60 }), H.cell('', gw[1]), H.cell('', gw[2]), H.cell('', gw[3])])
    ]);
    return [
      H.q(1, 'A machine fills 48 bottles every 3 minutes. (a) Complete the rate table.', { before: 20, keepNext: true }),
      rateTbl,
      H.sub('b', 'The machine starts at 9.00 a.m. At what time has it filled 400 bottles?   ________________'),
      H.q(2, 'Three shops sell the same can of drink.', { keepNext: true }),
      H.fig(figShops()),
      H.sub('a', 'Price of 1 can:   A ________   B ________   C ________'),
      H.sub('b', 'Which shop is the best buy?   ________'),
      H.sub('c', 'Ben needs exactly 20 cans. He may buy from more than one shop, but only whole packs. Find one way and work out the cost.', { keepNext: true }),
      ...H.lines(1),
      H.q(3, 'An empty tank holds 240 ℓ.', { keepNext: true }),
      H.tbl([3600, 6300], [H.row([H.cell('<div>' + figTaps() + '</div>', 3600, { h: 20 }),
        H.cell(t(L('(a)') + 'Only tap A is turned on. How long does it take to fill the tank?   ________<br>' + L('(b)') + 'Both taps are turned on. How long does it take now?   ________<br>' + L('(c)') + 'Both taps are on, and the crack lets out 6 ℓ a minute. How long to fill the tank?   ________<br>' + L('(d)') + 'The tank is full. Both taps are turned off but the crack still leaks. How long until it is half full?   ________'), 6300, { h: 40 })])]),

      H.q(4, 'Printer P prints 30 pages a minute. Printer Q prints 20 pages a minute. A job has 900 pages.', { pb: true, before: 0, keepNext: true }),
      H.sub('a', 'Both printers start together. How long do they take to print the job?   ________'),
      H.sub('b', 'Instead, P starts alone. After 5 minutes, Q joins in. How long does the whole job take from the start?', { keepNext: true }),
      ...H.lines(1),
      H.sub('c', 'Mei splits the 900 pages between P and Q so that both printers start together and finish at the same time. How many pages does she give to P?   ________'),
      H.q(5, 'Look at the car park sign.', { keepNext: true }),
      H.fig(figPark()),
      H.p(['<b style="color:#1F7A6F">Start here:</b> how long is 9.40 a.m. to 1.15 p.m.? Count the first hour, then count the half hours (or parts of a half hour) that are left.'], { after: 20 }),
      H.sub('a', 'Ali parks from 9.40 a.m. to 1.15 p.m. How much does he pay?', { keepNext: true }),
      ...H.lines(1),
      H.sub('b', 'Mei pays $3.60. What is the longest time she could have parked?   ________________'),
      H.q(6, 'Gym A charges $30 to join and then $4 for each visit. Gym B has no joining fee and charges $7 for each visit.', { keepNext: true }),
      H.sub('a', 'Complete the table.', { keepNext: true, after: 60 }),
      gymTbl,
      H.sub('b', 'For how many visits do the two gyms cost the same?   ________'),
      H.sub('c', 'Siti plans to go 14 times. Which gym is cheaper for her, and by how much?   ________________________')
    ];
  }
};
