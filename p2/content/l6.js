// Math Inquirers Level 2 — Lesson 6: Market Day (money: pay exactly, fewest notes and coins, change, "is there enough?")
// Singapore money: coins 5¢, 10¢, 20¢, 50¢, $1; notes $2, $5, $10, $50, $100 (no $20 note).
// Every answer below was worked out and checked; "find all" answers were enumerated by a short program.

const NAVY = '#1B2A49', YEL = '#FFC93C', WHITE = '#FFFFFF';

// Q4 picture: four price tags
const tagsQ4 = () => {
  const items = [['Book', '$9'], ['Pen', '$3'], ['Bag', '$14'], ['Cap', '$8']];
  let s = `<svg aria-label="Price tags: book $9, pen $3, bag $14, cap $8" viewBox="0 0 600 110" xmlns="http://www.w3.org/2000/svg" style="width:520px;max-width:100%">`;
  items.forEach(([name, price], i) => {
    const x = 6 + i * 150;
    s += `<polygon points="${x},55 ${x + 26},10 ${x + 140},10 ${x + 140},100 ${x + 26},100" fill="${YEL}" stroke="${NAVY}" stroke-width="3" stroke-linejoin="round"/><circle cx="${x + 24}" cy="55" r="6" fill="${WHITE}" stroke="${NAVY}" stroke-width="3"/>`;
    s += `<text x="${x + 84}" y="46" font-size="20" font-weight="700" text-anchor="middle" fill="${NAVY}" font-family="Arial">${name}</text><text x="${x + 84}" y="84" font-size="28" font-weight="700" text-anchor="middle" fill="${NAVY}" font-family="Arial">${price}</text>`;
  });
  return s + '</svg>';
};

module.exports = {
  lesson: {
    n: 6, week: 3, session: 'B', title: 'Market Day', topic: 'Money',
    objective: 'Read and write money in dollars and cents, pay exactly with the fewest notes and coins, make a list in order to find every way to pay, give change by counting on, decide whether there is enough money, and work backwards to find how much someone had at first.',
    skills: 'Systematic listing (make a list in order), working backwards, counting on, comparing, justifying "there are no more ways"',
    materials: 'Play money: coins 5¢, 10¢, 20¢, 50¢, $1 and notes $2, $5, $10, $50 (about 6 of each per pair), price tags, mini whiteboards.',
    online: 'Print the cut-out coins and notes, or use real money at home. No play money? Draw each coin and note on paper. The shop and the toy stall are on the slides; children show their money to the camera.',
    warmup: 'Market Day shop: six items priced from 85¢ to $57.20. Pay exactly with notes and coins. Who can pay with the fewest pieces of money?',
    explore: 'The toy stall: kite $6, ball $4, yo-yo $3, bubbles $2, sticker $1. Each pair has $10. They choose toys (at most one of each), find the cost and the change, then try to find every basket that costs exactly $10, listing them in order.',
    mini: 'Money in dollars and cents ($3.45 = 345¢). Make a list in order: biggest note first, then one fewer each time, in a table. Work backwards from the money that is left: put back each amount spent, from the last to the first.',
    share: 'Mei says: “To pay $40 with the fewest notes, I use two $20 notes.” What would you tell her?',
    exit: { q: 'A pen costs $3.65. Pay exactly with the fewest notes and coins.', a: '$2 + $1 + 50¢ + 10¢ + 5¢ (5 pieces)' },
    mistakes: ['Mixing up dollars and cents: writing 345¢ as $34.5, or reading $3.05 as $3.50.', 'Using a $20 note (there is no $20 note), or not starting with the biggest note that fits when finding the fewest.', 'Listing ways with no order, so some ways are missed or the same way is written twice.'],
    extension: 'Find every way to pay exactly $10 using $5 notes, $2 notes and $1 coins. (There are 10.)',
    key: [
      ['Q1', 'Curry puff $1.65: $1 + 50¢ + 10¢ + 5¢ (4).  Notebook $4.30: $2 + $2 + 20¢ + 10¢ (4).  Umbrella $18.75: $10 + $5 + $2 + $1 + 50¢ + 20¢ + 5¢ (7).  Bicycle $76: $50 + $10 + $10 + $5 + $1 (5).'],
      ['Q2', '7 ways ($5, $2, $1): 1,1,1 / 1,0,3 / 0,4,0 / 0,3,2 / 0,2,4 / 0,1,6 / 0,0,8. Row H is spare: tell children "you may not need every row".  (a) 7 ways  (b) $5 + $1 + $1 + $1, and $2 + $2 + $2 + $2'],
      ['Q3', '(a) 35¢  (b) $24 change: $10 + $10 + $2 + $2 (there is no $20 note)'],
      ['Q4', '(a) No. The bag and the cap cost $14 + $8 = $22. She has $20, so she is $2 short.  (b) She spends $17: book and cap ($9 + $8), or bag and pen ($14 + $3). Those are the only two pairs.'],
      ['Q5', '(a) 25¢ + 30¢ + 45¢ = 100¢ = $1.00  (Think harder 1 is the half-money puzzle with the kite and the ball: $20.)'],
      ['Q6', '3 ways: 4 erasers; 2 erasers and 5 stickers; 10 stickers. (1 or 3 erasers leave 150¢ or 50¢, which 20¢ stickers cannot make exactly.)']
    ]
  },

  script: {
    hook: ['Welcome to Market Day, inquirers! Today you are shoppers AND shopkeepers. You will pay exactly, give change, and find every way to pay without missing one.', 'Notice it, test it with play money, and explain why.'],
    warmIntro: ['Here is our market. The sticker book costs $3.45. That means 3 dollars and 45 cents. Pay exactly with your play money.', 'Now count your pieces. Who used the fewest? How did you choose?'],
    predict: ['The toy stall has a kite, a ball, a yo-yo, bubbles and a sticker. You have $10. How many different baskets do you think cost EXACTLY $10? Write a guess.'],
    exploreHints: ['Stuck: start with the most expensive toy. Put it in the basket. How much is left to spend?', 'Repeating baskets: “Kite and ball is the same basket as ball and kite.”', 'Finished early: which basket gives you the most toys for $10? Which gives exactly $1 change?'],
    think: ['“Ways to pay $6 with $5 notes, $2 notes and $1 coins. I start with the biggest note: one $5. $1 is left, so one $1 coin. Now no $5: three $2, then two $2 and two $1, one $2 and four $1, no $2 and six $1. The $2 column went 3, 2, 1, 0, so I know I am finished: 5 ways.”', '“Mei spent 80¢ on a drink, then 65¢ on a bun, and has 55¢ left. I work backwards from the end. Before the bun she had 55 + 65 = 120¢. Before the drink she had 120 + 80 = 200¢. That is $2.”', '“Change from $1 for 45¢: I count on like a shopkeeper. 45¢ and 5¢ is 50¢. 50¢ and 50¢ is $1. So the change is 5¢ + 50¢ = 55¢.”'],
    circulate: ['Ask: “Is this in cents or in dollars? How do you know?”', 'Ask: “What is the biggest note that is not too much?”', 'Ask: “How do you know you have found every way?”'],
    hints: ['Hint 1: “Lay out real play money and count it.”', 'Hint 2: “Make a table with a column for each note or coin. Start with as many of the biggest as you can.”', 'Hint 3: “Start from the money that is left and put back what was spent.”'],
    talk: ['“Mei says: To pay $40 with the fewest notes, I use two $20 notes. What would you tell her?”', '“How did you make sure you found every way to pay?”'],
    talkAns: 'There is no $20 note in Singapore. $50 is too much, so we use $10 notes: $10 + $10 + $10 + $10, which is 4 notes. To find every way, start with the most of the biggest note and use one fewer each time, in a table.',
    close: ['“Great shopping, inquirers! You paid exactly, gave change and made lists in order. A good shopkeeper always checks, and so did you.”']
  },

  deck: {
    today: 'Pay exactly with the fewest notes and coins, list every way in order, give change and work backwards with money.',
    warmGame: 'Market Day shop. Six items with price tags from 85¢ to $57.20. Pay exactly with play notes and coins. Who can pay with the fewest pieces?',
    warmQs: [['Write 345¢ in dollars and cents.', '$3.45'], ['How many cents is $2.05?', '205¢'], ['Which is more: $1.50 or 105¢?', '$1.50 (150¢)'], ['Pay 75¢ with the fewest coins.', '50¢ + 20¢ + 5¢'], ['You have 60¢. A sticker costs 85¢. How much more do you need?', '25¢']],
    expSetup: ['You have $10. Look at the toy stall: kite $6, ball $4, yo-yo $3, bubbles $2, sticker $1.', 'Choose some toys (at most one of each). How much do they cost? How much change do you get?', 'Find every basket that costs EXACTLY $10.', 'Make a list in order so you do not miss one or count one twice.'],
    expPic: 'a toy stall with a kite, a ball, a yo-yo, a tub of bubbles and a sticker, each with a yellow price tag ($6, $4, $3, $2, $1), and a $10 note.',
    expAsk: [['How many baskets cost exactly $10?', '3: kite + ball; kite + yo-yo + sticker; ball + yo-yo + bubbles + sticker.'], ['How do you know you have them all?', 'Start with the kite in the basket, then without the kite, and list in order.'], ['You buy the kite and the bubbles. How much change?', '$10 − $8 = $2.']],
    mini1: { head: 'Make a list in order: pay $6 with $5, $2 and $1', table: [['$5', '$2', '$1'], ['1', '0', '1'], ['0', '3', '0'], ['0', '2', '2'], ['0', '1', '4'], ['0', '0', '6']], body: ['Start with the biggest note: one $5, then $1.', 'No $5: three $2, two $2, one $2, no $2. Fill up with $1 coins.'], ans: '5 ways.' },
    mini2: { head: 'Work backwards with money', body: ['Mei bought a drink for 80¢. Then she bought a bun for 65¢. She has 55¢ left.', 'Before the bun: 55¢ + 65¢ = 120¢.', 'Before the drink: 120¢ + 80¢ = ?'], ans: '200¢ = $2.' },
    keyHead: 'Key idea: in order, and backwards',
    keyBig: 'To find every way, make a list in order: the most of the biggest note first, then one fewer each time. To find what someone had at first, work backwards and put back what was spent.',
    keySmall: '100¢ = $1. There is no $20 note.',
    brk: 'Shopkeeper stretch. The tutor calls an amount: reach up high for dollars, touch your toes for cents. “$3.50!” “75¢!” “205¢!” (that is $2.05: reach up!).',
    ws1: 'Page 1, in pairs: Q1 pay exactly with the fewest notes and coins, Q2 every way to pay $8.',
    ws2: 'Page 2, on your own: Q3 change, Q4 is there enough, Q5 work backwards, Q6 stickers and erasers for exactly $2.'
  },

  qbank: {
    core: [
      { q: 'Write 275¢ in dollars and cents.', a: '$2.75' },
      { q: 'Pay exactly 65¢ with the fewest coins.', a: '50¢ + 10¢ + 5¢ (3 coins)' },
      { q: 'Pay exactly $17 with the fewest notes.', a: '$10 + $5 + $2 (3 notes)' },
      { q: 'A pencil costs 45¢. Mei pays with a $1 coin. How much change does she get?', a: '55¢' },
      { q: 'Ali has $20. He buys a book for $12. Does he have enough money left to buy a kite for $9?', a: 'No. He has $8 left, which is $1 short.' },
      { q: 'Ben had some money. He spent $6 and has $9 left. How much money did he have at first?', a: '$15' }
    ],
    stretch: [
      { q: 'Ben spent half of his money on a kite. Then he spent $4 on a ball. He had $6 left. How much money did Ben have at first? Tip: draw his money as a bar cut in half.', a: '$20 ($6 + $4 = $10 is the half he kept after the kite, so the other half is also $10: $10 + $10 = $20).' },
      { q: 'How many ways can you pay exactly $10 using $5 notes, $2 notes and $1 coins?', a: '10 ways (1 + 3 + 6)' },
      { q: 'Ali has 4 coins. They are worth $1.25 altogether. Find all the sets of 4 coins he could have.', a: '2 sets: $1 + 10¢ + 10¢ + 5¢, and 50¢ + 50¢ + 20¢ + 5¢' },
      { q: 'How many different ways can you pay exactly 40¢ using 5¢, 10¢ and 20¢ coins? Make a list in order, starting with the most 20¢ coins.', a: '9 ways: two 20¢ (1 way); one 20¢ and 20¢ more (3 ways); no 20¢ (5 ways).' },
      { q: 'Pens cost $3 each and books cost $7 each. Ben buys 6 things and spends exactly $30. How many pens and how many books does he buy? Make a table.', a: '3 pens and 3 books ($9 + $21 = $30). Table: 6 pens $18, 5 pens and 1 book $22, 4 and 2 $26, 3 and 3 $30 ✓. Each swap of a pen for a book adds $4.' },
      { q: 'Ravi had some money. He spent $8, then he spent half of what was left. He had $6 left. How much money did Ravi have at first?', a: '$20 ($6 + $6 = $12 was left after the $8; $12 + $8 = $20)' },
      { q: 'Siti has 5 coins. They are all 20¢ or 50¢ coins, worth $1.60 altogether. How many of each coin does she have?', a: 'Three 20¢ and two 50¢ (60¢ + 100¢ = 160¢)' },
      { q: 'Ali pays exactly 90¢ with 5 coins. Find all the sets of 5 coins he could use.', a: '3 sets: 50¢ + 20¢ + 10¢ + 5¢ + 5¢; 50¢ + 10¢ + 10¢ + 10¢ + 10¢; 20¢ + 20¢ + 20¢ + 20¢ + 10¢' },
      { q: 'A pen costs $3 more than a pencil. Together they cost $11. How much does each cost?', a: 'Pencil $4, pen $7 ($11 − $3 = $8, $8 ÷ 2 = $4)' }
    ],
    challenge: [
      { q: 'Ali has 10 coins. Every coin is a 10¢ coin or a 20¢ coin. They could be worth $1.50: how many of each coin is that? Write ALL the totals his 10 coins could be worth. Could they be worth $1.55? Explain.', a: 'Five and five. Totals $1.00 to $2.00, 10¢ apart (11). Not $1.55.' },
      { q: 'Mei has $1. At the snack stall: chips 45¢, sweet 15¢, jelly 25¢, biscuit 30¢, lollipop 20¢. She wants as many DIFFERENT snacks as she can. Which should she buy?', a: 'Sweet, lollipop, jelly and biscuit (90¢). Five snacks cost $1.35.' },
      { q: 'Ben has 6 coins. Every coin is 10¢ or 50¢. List all the amounts he could have.', a: '7 amounts: 60¢, $1, $1.40, $1.80, $2.20, $2.60, $3' },
      { q: 'Which amounts 10¢, 20¢, 30¢, … up to $1 can be paid exactly using only 20¢ and 50¢ coins? Which cannot? Explain why.', a: 'Can: 20¢, 40¢, 50¢, 60¢, 70¢, 80¢, 90¢ and $1. Cannot: 10¢ and 30¢. 20¢, 40¢, 60¢, 80¢ and $1 are made of 20¢ coins only. 50¢, 70¢ and 90¢ need one 50¢ coin and then 0, 20¢ or 40¢ more in 20¢ coins. 10¢ is smaller than every coin, and 30¢ is too small for a 50¢ coin and is not made of 20¢ coins.' },
      { q: 'Make up your own price list for 5 snacks (prices in cents) so that Mei, with exactly $1, can buy exactly TWO different baskets that cost exactly $1. Check by listing every basket in order. Swap with a partner. Is your answer the same?', a: 'Open. Example: 50¢, 30¢, 20¢, 60¢, 40¢. The two baskets that cost $1 are 50¢ + 30¢ + 20¢ and 60¢ + 40¢. No other basket makes exactly $1, so the list has exactly two.' },
      { q: 'Three friends share the cost of a $15 present. Ali pays $2 more than Ben. Siti pays $2 more than Ali. How much does each pay?', a: 'Ben $3, Ali $5, Siti $7' },
      { q: 'Siti had some money. She spent half of it on a book. Then she spent half of what was left on a pen. She had $5 left. How much money did she have at first?', a: '$20 ($5 + $5 = $10 before the pen; $10 + $10 = $20)' },
      { q: 'Sweets cost 5¢ each and lollipops cost 20¢ each. Ben buys 8 things altogether and spends exactly $1. How many sweets and how many lollipops does he buy?', a: '4 sweets and 4 lollipops (20¢ + 80¢ = $1)' },
      { q: 'Mei has one $10 note, one $5 note, one $2 note and one $1 coin. How many different amounts can she pay exactly, using one or more of them?', a: '15 amounts: $1, $2, $3, $5, $6, $7, $8, $10, $11, $12, $13, $15, $16, $17, $18' }
    ]
  },

  workbook: H => {
    const w1 = [2200, 1300, 5200, 1200];
    const hd = (s, w) => H.cell(s, w, { bold: true, fill: 'D9D9D9', size: 22 });
    const items = [['Curry puff', '$1.65'], ['Notebook', '$4.30'], ['Umbrella', '$18.75'], ['Bicycle', '$76']];
    const w2 = [1300, 2150, 2150, 2150, 2150];
    return [
      H.p('Coins: 5¢, 10¢, 20¢, 50¢, $1.   Notes: $2, $5, $10, $50, $100.   (There is no $20 note.)   100¢ = $1.   Careful: 50¢ is a coin, $50 is a note.', { after: 40 }),
      H.q(1, 'Pay exactly. Use the FEWEST notes and coins you can.', { before: 60, keepNext: true }),
      H.tbl(w1, [H.row(['Item', 'Price', 'Notes and coins I use', 'Pieces'].map((s, i) => hd(s, w1[i]))),
        ...items.map(([a, b]) => H.row([H.cell(a, w1[0], { bold: true, h: 130 }), H.cell(b, w1[1], { bold: true, size: 26 }), H.cell('', w1[2]), H.cell('', w1[3])]))]),
      H.q(2, 'Find EVERY way to pay exactly $8 using $5 notes, $2 notes and $1 coins. Make a list in order: start with the most $5 notes. You may not need every row.', { keepNext: true }),
      H.tbl(w2, [H.row(['Way', 'Number of $5', 'Number of $2', 'Number of $1', 'Pieces altogether'].map((s, i) => hd(s, w2[i]))),
        ...'ABCDEFGH'.split('').map(l => H.row([H.cell(l, w2[0], { bold: true, h: 60 }), H.cell('', w2[1]), H.cell('', w2[2]), H.cell('', w2[3]), H.cell('', w2[4])]))]),
      H.sub('a', 'How many ways are there?   ________'),
      H.sub('b', 'Two ways use exactly 4 pieces of money. What are they?'),
      H.ans(),

      H.q(3, 'Change.', { pb: true, before: 0, keepNext: true }),
      H.sub('a', 'Mei buys an eraser for 65¢. She pays with a $1 coin. How much change does she get?   ________'),
      H.sub('b', 'Ali buys a game for $26. He pays with a $50 note. How much change does he get? Which notes give this change with the fewest notes?'),
      H.ans(),
      H.q(4, 'Siti has $20 to spend.', { keepNext: true }),
      H.fig(tagsQ4()),
      H.sub('a', 'Can Siti buy the bag and the cap? Explain.'),
      ...H.lines(1),
      H.sub('b', 'Siti buys two different things and gets exactly $3 change. Find ALL the pairs she could buy.'),
      ...H.lines(2),
      H.q(5, 'Work backwards.', { keepNext: true }),
      H.sub('a', 'Mei spent 45¢ on a sweet and 30¢ on a pencil. She has 25¢ left. How much money did she have at first? Write it in dollars and cents.   ________'),
      H.q(6, 'Stickers cost 20¢ each. Erasers cost 50¢ each. Siti spends exactly $2. How many stickers and erasers could she buy? Find ALL the ways. (She might buy only one kind.)', { keepNext: true }),
      ...H.lines(3)
    ];
  }
};
