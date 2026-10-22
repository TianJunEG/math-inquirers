// Math Inquirers P2 — Lesson 5: Mystery Number Machines (working backwards, two steps, + − × ÷; bar models)
// Every answer below was worked out and checked forwards.

const NAVY = '#1B2A49', YEL = '#FFC93C', SKY = '#DDEBF7', TEAL = '#1F7A6F', WHITE = '#FFFFFF';

// Q4 picture: a bar cut into 3 equal bags, one bag split into "taken out" and "left" (no numbers given)
const barQ4 = () => {
  let s = `<svg aria-label="A bar for all of Ravi’s sweets, cut into 3 equal bags. One bag is split into two parts." viewBox="0 0 600 170" xmlns="http://www.w3.org/2000/svg" style="width:430px;max-width:100%">`;
  s += `<path d="M40 52 v-12 H520 v12" fill="none" stroke="${NAVY}" stroke-width="3"/>`;
  s += `<text x="280" y="28" font-size="18" font-weight="700" text-anchor="middle" fill="${NAVY}" font-family="Arial">all of Ravi’s sweets: ?</text>`;
  for (let i = 0; i < 3; i++) s += `<rect x="${40 + i * 160}" y="62" width="160" height="56" fill="${i === 2 ? WHITE : SKY}" stroke="${NAVY}" stroke-width="3"/><text x="${i === 2 ? 472 : 120 + i * 160}" y="97" font-size="18" font-weight="700" text-anchor="middle" fill="${NAVY}" font-family="Arial">bag ${i + 1}</text>`;
  s += `<line x1="424" y1="62" x2="424" y2="118" stroke="${NAVY}" stroke-width="3" stroke-dasharray="6 5"/>`;
  s += `<rect x="361" y="64" width="62" height="52" fill="${YEL}" opacity="0.55"/>`;
  s += `<text x="392" y="146" font-size="16" font-weight="700" text-anchor="middle" fill="${TEAL}" font-family="Arial">taken out</text><text x="472" y="146" font-size="16" font-weight="700" text-anchor="middle" fill="${TEAL}" font-family="Arial">left</text>`;
  return s + '</svg>';
};

// Q3 picture: before-and-after bars, drawn to scale (6 units per number), with the two unknown bars shown as "?"
const barQ3 = () => {
  const bar = (y, w, label, fill, txt, dash) => `<rect x="150" y="${y}" width="${w}" height="40" fill="${fill}" stroke="${NAVY}" stroke-width="3"${dash ? ' stroke-dasharray="8 6"' : ''}/><text x="140" y="${y + 26}" font-size="16" font-weight="700" text-anchor="end" fill="${NAVY}" font-family="Arial">${label}</text><text x="${150 + w / 2}" y="${y + 28}" font-size="20" font-weight="700" text-anchor="middle" fill="${NAVY}" font-family="Arial">${txt}</text>`;
  let s = `<svg aria-label="Three bars drawn to scale: Siti at first (unknown), after giving 24 stickers (unknown), and now (50 stickers)." viewBox="0 0 600 190" xmlns="http://www.w3.org/2000/svg" style="width:430px;max-width:100%">`;
  s += bar(10, 354, 'At first', WHITE, '?', true) + bar(70, 210, 'Gave 24', WHITE, '?', true) + bar(130, 300, 'Now', YEL, '50', false);
  s += `<text x="520" y="64" font-size="15" font-weight="700" fill="${TEAL}" font-family="Arial">− 24</text><text x="470" y="124" font-size="15" font-weight="700" fill="${TEAL}" font-family="Arial">+ 15</text>`;
  return s + '</svg>';
};

module.exports = {
  lesson: {
    n: 5, week: 3, session: 'A', title: 'Mystery Number Machines', topic: 'Working Backwards',
    objective: 'Find a mystery number in two-step puzzles with +, −, × and ÷ by working backwards (undo the last step first with the opposite operation), check by going forwards, and use before-and-after bar models for stories where an amount changes.',
    skills: 'Inverse operations, working backwards, guess and check, before-and-after bar models, checking forwards',
    materials: 'Mini whiteboards, counters, paper cups, number machine cards (× 2, × 3, × 4, × 5, × 10 and + or − cards from 1 to 20), paper strips for bars.',
    online: 'Machine cards shown on the slide; children write on whiteboards and hold them up. For bars, children draw on paper or fold paper strips into equal parts.',
    warmup: 'Guess my machine: the tutor is a one-step machine (for example × 3 or + 15). Children call out IN numbers, the tutor says the OUT, and children guess the rule. Then the tutor says only an OUT and children say what went IN.',
    explore: 'Pairs build a two-step machine from two cards (one × card and one + or − card). One partner secretly picks a start number, runs it through and says only the OUT. The other works backwards to find the start. Then they swap the order of the cards: does the same start give the same OUT?',
    mini: 'Opposites undo: + and −, × and ÷. Draw the machine, go backwards, undo the LAST step first, then check forwards. For stories that change an amount, draw a before-and-after bar and undo each change from the end.',
    share: 'To undo “× 2, then + 6” with OUT 20, Mei takes away 6 first. Ali divides by 2 first. Who is right?',
    exit: { q: 'I think of a number. I multiply it by 4, then take away 6. I get 14. What is my number?', a: '5 (14 + 6 = 20, 20 ÷ 4 = 5; check 5 × 4 = 20, 20 − 6 = 14)' },
    mistakes: ['Doing the same step again instead of the opposite (27 × 2 instead of 27 ÷ 2).', 'Undoing the steps in the wrong order: the first step first instead of the last step first.', 'Bar stories: stopping at one part (one bag or one half) instead of finding the whole, or forgetting to undo one of the changes.'],
    extension: 'Make a three-step machine with a × card, a ÷ card and a + card. Give a partner only the OUT. Can they find the IN? Which OUT numbers make your machine impossible to undo?',
    key: [
      ['Q1', '(a) 10  (b) 16  (c) 24  (d) 9  (undo the last step first: e.g. (a) 27 − 7 = 20, 20 ÷ 2 = 10)'],
      ['Q2', '(a) IN 4 → OUT 14; IN 10 → OUT 32; OUT 17 ← IN 5; OUT 29 ← IN 9.  (b) IN 3, 5, 10, 20 give OUT 7, 11, 21, 41.'],
      ['Q3', '59 stickers (50 − 15 = 35, 35 + 24 = 59; check 59 − 24 = 35, 35 + 15 = 50)'],
      ['Q4', '30 sweets (one bag: 6 + 4 = 10; 3 bags: 10 × 3 = 30)'],
      ['Q5', '(a) Mei 18  (b) Ali 14  (c) No: the order of the steps matters  (d) 7 (18 − 4 = 14, 14 ÷ 2 = 7)']
    ]
  },

  script: {
    hook: ['Good morning, inquirers! Today you are code-breakers. A number went into a secret machine and something came out. Your job is to run the machine backwards and find the number that went in.', 'Remember our rule: notice it, test it, explain why.'],
    warmIntro: ['I am a machine. Give me a number and I will tell you what comes out. Ready? You say 4, I say 12. You say 10, I say 30. What am I doing?', 'Now I only tell you what comes out: 18. What went in? How did you work it out?'],
    predict: ['Here are two machine cards: × 2 and + 6. If I put 4 in, what comes out? Now I swap the cards: + 6 first, then × 2. Will the same number come out? Thumbs up or down before we test it.'],
    exploreHints: ['Stuck: write the machine as boxes and arrows, then put your partner’s OUT number in the last box.', 'Mixed up: “What was the LAST thing the machine did? Undo that first.”', 'Finished early: find an OUT number your partner can NOT undo with whole numbers. Why does it not work?'],
    think: ['“Mystery number × 3, then + 4, gives 25. I go backwards. The last step was + 4, so I undo it first with − 4: 25 − 4 = 21. The step before was × 3, so I undo it with ÷ 3: 21 ÷ 3 = 7. Check forwards: 7 × 3 = 21, 21 + 4 = 25. ✓”', '“Ben gave away 18 stamps, then bought 25, and now has 60. I draw the bars and start at the end. Before he bought 25 he had 60 − 25 = 35. Before he gave away 18 he had 35 + 18 = 53. Check: 53 − 18 = 35, 35 + 25 = 60. ✓”', '“Mei gave away half her beads, then used 5. She has 9 left. The half she kept is 5 + 9 = 14. The other half is also 14. So she had 14 + 14 = 28.”'],
    circulate: ['Ask: “What was the last step? What is its opposite?”', 'Ask: “Show me your check going forwards. Do you get the OUT number?”', 'Ask: “Point to your bar. Which part do you know? Which part is the mystery?”'],
    hints: ['Hint 1: “Draw the machine boxes. Write the OUT in the last box.”', 'Hint 2: “Cover the first step with your finger. Undo only the last step.”', 'Hint 3: “For bars: start from what is left now and put back each change, from the end to the start.”'],
    talk: ['“To undo × 2, then + 6, with OUT 20, Mei takes away 6 first. Ali divides by 2 first. Who is right? Test both.”', '“Why do we undo the LAST step first?”'],
    talkAns: 'Mei is right: 20 − 6 = 14, 14 ÷ 2 = 7, and 7 × 2 + 6 = 20. Ali gets 20 ÷ 2 = 10, 10 − 6 = 4, but 4 × 2 + 6 = 14, not 20. The last step happened last, so it must be undone first, like taking off shoes before socks.',
    close: ['“Today you ran machines backwards and drew before-and-after bars. Code-breakers always check forwards, and you did. Well done, inquirers!”']
  },

  deck: {
    today: 'Find mystery numbers in two-step machines with + − × ÷ by working backwards, and draw before-and-after bars for stories.',
    warmGame: 'Guess my machine. The tutor is a secret one-step machine. Call out an IN number, hear the OUT, and guess the rule. Then the tutor gives only an OUT: what went IN?',
    warmQs: [['I think of a number. I multiply it by 2. I get 18. What is it?', '9'], ['I think of a number. I divide it by 5. I get 4. What is it?', '20'], ['I think of a number. I take away 25. I get 40. What is it?', '65'], ['What is the opposite of × 4?', '÷ 4'], ['I think of a number. I multiply it by 3, then add 4. I get 19. What is it?', '5']],
    expSetup: ['Pick one × card and one + or − card. Put them in a row: that is your machine.', 'Secretly choose a start number. Run it through both cards. Say only the OUT.', 'Your partner works backwards to find your start number. Check it together.', 'Swap the order of the two cards. Put the same start number in. Is the OUT the same?'],
    expPic: 'two machine cards in a row (× 2 then + 6) between a yellow box with a question mark and a blue OUT box showing 20, with a dashed arrow going back from OUT to IN.',
    expAsk: [['How did you find your partner’s start number?', 'Undo the last card first with its opposite, then undo the first card.'], ['What is the opposite of × 3? Of − 8?', '÷ 3. + 8.'], ['Does it matter which card goes first?', 'Yes. Start 4: × 2 then + 6 gives 14, but + 6 then × 2 gives 20.']],
    mini1: { head: 'Two steps: undo the last step first', body: ['? → × 3 → + 4 → 25', 'Undo + 4: 25 − 4 = 21.', 'Undo × 3: 21 ÷ 3 = ?', 'Check forwards.'], ans: '7 (7 × 3 = 21, 21 + 4 = 25).' },
    mini2: { head: 'Before and after: draw the bars', body: ['Ben had some stamps. He gave 18 to Mei. Then he bought 25 more. Now he has 60.', 'Before he bought 25: 60 − 25 = 35.', 'Before he gave 18: 35 + 18 = ?'], ans: '53 stamps (check 53 − 18 = 35, 35 + 25 = 60).' },
    keyHead: 'Key idea: undo it backwards',
    keyBig: 'Start at the end. Undo the LAST step first with its opposite, then the step before. Check by going forwards.',
    keySmall: 'Opposites: + and − undo each other. × and ÷ undo each other.',
    brk: 'Machine moves. The tutor calls a machine (“× 2 jumps!”, “+ 3 claps!”) on a number on the board, and everyone does the OUT number of moves.',
    ws1: 'Page 1, in pairs: Q1 two-step mystery machines, Q2 machine tables and finding a two-step rule.',
    ws2: 'Page 2, on your own: Q3 before-and-after stickers, Q4 sweets in equal bags, Q5 does the order matter. (The three-children marbles problem is now Think Harder 4.)'
  },

  qbank: {
    core: [
      { q: 'I think of a number. I multiply it by 5. I get 45. What is my number?', a: '9' },
      { q: 'I think of a number. I divide it by 2. I get 8. What is my number?', a: '16' },
      { q: 'I think of a number. I add 35. I get 90. What is my number?', a: '55' },
      { q: 'I think of a number. I multiply it by 3, then add 2. I get 20. What is my number?', a: '6 (20 − 2 = 18, 18 ÷ 3 = 6)' },
      { q: 'I think of a number. I take away 10, then divide by 4. I get 5. What is my number?', a: '30 (5 × 4 = 20, 20 + 10 = 30)' },
      { q: 'Mei had some stickers. She gave away 14 and has 27 left. How many did she have at first?', a: '41 (27 + 14)' }
    ],
    stretch: [
      { q: 'A machine multiplies by a number, then adds a number. IN 2 gives OUT 11 and IN 5 gives OUT 20. Find what the machine does (try × 2, × 3, × 4 … with IN 2, then test IN 5). Then: what OUT does IN 10 give? Which IN gives OUT 26?', a: '× 3, then + 5. IN 10 gives OUT 35. OUT 26 comes from IN 7 (26 − 5 = 21, 21 ÷ 3 = 7).' },
      { q: 'Ben had some money. He spent $15 on a book. Then his dad gave him $10. Now he has $42. How much money did Ben have at first?', a: '$47 (42 − 10 = 32, 32 + 15 = 47)' },
      { q: 'Siti had some beads. She gave half of them to Mei. Then she bought 12 more. Now she has 30 beads. How many beads did Siti have at first?', a: '36 (30 − 12 = 18 is half, 18 + 18 = 36)' },
      { q: 'Ali, Ben and Siti have 40 marbles altogether. Ben has 5 more marbles than Ali. Siti has 8 more marbles than Ali. How many marbles does each child have? Draw a bar for each child.', a: 'Ali 9, Ben 14, Siti 17 (40 − 5 − 8 = 27, 27 ÷ 3 = 9; check 9 + 14 + 17 = 40)' },
      { q: 'A machine does × 2, then − 3. What goes IN to give OUT 17? What goes IN to give OUT 1?', a: '10, and 2 (17 + 3 = 20, 20 ÷ 2 = 10; 1 + 3 = 4, 4 ÷ 2 = 2)' },
      { q: 'I think of a number. I divide it by 3, then multiply by 10. I get 50. What is my number?', a: '15 (50 ÷ 10 = 5, 5 × 3 = 15)' },
      { q: 'A bus had some people on it. At the first stop, 12 got off and 5 got on. At the second stop, 8 got off. Now there are 20 people on the bus. How many were on the bus at first?', a: '35 (20 + 8 = 28, 28 − 5 = 23, 23 + 12 = 35)' },
      { q: 'A machine does × 4, then + 13. The OUT is 45. What went IN?', a: '8 (45 − 13 = 32, 32 ÷ 4 = 8)' },
      { q: 'A machine multiplies by a number, then adds a number. IN 1 gives OUT 9. IN 3 gives OUT 19. What does the machine do?', a: '× 5, then + 4 (1 × 5 + 4 = 9 and 3 × 5 + 4 = 19; × 2, × 3, × 4 and × 10 do not fit both)' }
    ],
    challenge: [
      { q: 'Ali, Ben and Siti share 42 stickers. Ben gets 2 more than Ali. Siti gets twice as many as Ali. How many stickers does each child get?', a: 'Ali 10, Ben 12, Siti 20 (40 ÷ 4 = 10)' },
      { q: 'A machine does × 2, then − 4. Ravi puts a number in, then puts the OUT straight back in again. The final OUT is 12. What number did he put in first?', a: '6 (back twice: 12 → 8 → 6)' },
      { q: 'Ben gives Ali 5 marbles. Now they both have 20 marbles. How many marbles did each boy have before? How many MORE marbles did Ben have than Ali at first? Why is it not 5? What if Ben had given 8 marbles and they ended with the same number?', a: 'Ben 25, Ali 15. Ben had 10 more, because Ben lost 5 AND Ali gained 5. If Ben gave 8, he had 16 more at first: the gap at the start is always double the number given.' },
      { q: 'A machine does × 2, then + 1. Can the OUT ever be 20? Which OUT numbers between 10 and 20 can it make? Explain how you know.', a: 'No. × 2 always gives an even number, and + 1 makes it odd, so every OUT is odd. The OUT numbers between 10 and 20 are 11, 13, 15, 17 and 19 (IN 5, 6, 7, 8, 9).' },
      { q: 'Make up your own before-and-after story: someone gives some away, then gets some more, and ends with 40. Draw the bars and work out how many they had at first. Check by going forwards. Then change ONE number in your story. What happens to the number at the start? Swap with a partner.', a: 'Open. Example: Ben had some stamps, gave 18 away, then bought 13 more and has 40. Undo the last step: 40 − 13 = 27; undo the first: 27 + 18 = 45. Check: 45 − 18 = 27, 27 + 13 = 40. If the 13 changes to 15, the start changes to 43: a bigger amount bought means a smaller start.' },
      { q: 'I think of a number. If I add 10 to it, I get the same answer as when I multiply it by 3. What is my number?', a: '5 (5 + 10 = 15 and 5 × 3 = 15)' },
      { q: 'Siti had some sweets. She gave Ben 1 more than half of them. Now she has 7 sweets left. How many sweets did she have at first?', a: '16 (7 + 1 = 8 is half, 8 + 8 = 16; she gave Ben 9)' },
      { q: 'A machine does × 2, then − 1. Mei puts a number through the machine 3 times in a row (each OUT goes back in). The final OUT is 17. What number did she start with?', a: '3 (17 + 1 = 18, 18 ÷ 2 = 9; 9 + 1 = 10, 10 ÷ 2 = 5; 5 + 1 = 6, 6 ÷ 2 = 3; check 3 → 5 → 9 → 17)' },
      { q: 'Three boxes have 30 pens altogether. 5 pens are moved from box A to box B. Then 3 pens are moved from box B to box C. Now all three boxes have the same number of pens. How many pens were in each box at first?', a: 'A 15, B 8, C 7 (each ends with 10; undo the moves from the end)' }
    ]
  },

  workbook: H => {
    const mach = cells => H.tbl(cells.map(c => c.w), [H.row(cells.map(c => H.cell(c.text, c.w, { fill: c.fill, bold: c.bold, h: 70, size: 24 })))]);
    const m2 = (a, b, out) => mach([{ text: '?', w: 1500, fill: 'FFF2CC', bold: true }, { text: '→', w: 700 }, { text: a, w: 1500, fill: 'EDEDED' }, { text: '→', w: 700 }, { text: b, w: 1500, fill: 'EDEDED' }, { text: '→', w: 700 }, { text: out, w: 1500, fill: 'DDEBF7', bold: true }]);
    const ws = [1900, 2000, 2000, 2000, 2000];
    const io = (ins, outs) => H.tbl(ws, [H.row([H.cell('IN', ws[0], { bold: true, fill: 'EDEDED' }), ...ins.map((s, i) => H.cell(s, ws[i + 1], { h: 90, size: 24 }))]), H.row([H.cell('OUT', ws[0], { bold: true, fill: 'EDEDED' }), ...outs.map((s, i) => H.cell(s, ws[i + 1], { h: 90, size: 24 }))])]);
    return [
      H.p('IN = what goes in.   OUT = what comes out.   Undo = do the opposite.', { after: 50 }),
      H.q(1, 'Mystery machines. Find the number that went IN and write it in the yellow box. Undo the LAST step first, then check forwards.', { before: 40, keepNext: true }),
      H.sub('a', 'I multiply by 2, then add 7. I get 27.', { after: 30, keepNext: true }), m2('× 2', '+ 7', '27'), H.gap(16),
      H.sub('b', 'I take away 8, then multiply by 5. I get 40.', { after: 30, keepNext: true }), m2('− 8', '× 5', '40'), H.gap(16),
      H.sub('c', 'I divide by 3, then add 12. I get 20.', { after: 30, keepNext: true }), m2('÷ 3', '+ 12', '20'), H.gap(16),
      H.sub('d', 'I multiply by 4, then take away 15. I get 21.', { after: 30, keepNext: true }), m2('× 4', '− 15', '21'),
      H.q(2, 'Two-step number machines.', { keepNext: true }),
      H.sub('a', 'This machine does × 3, then + 2. Fill in the table.', { keepNext: true }),
      io(['4', '10', '', ''], ['', '', '17', '29']), H.gap(30),
      H.sub('b', 'This machine does × 2, then + 1. Fill in the table for IN 3, 5, 10 and 20.', { keepNext: true }),
      io(['3', '5', '10', '20'], ['', '', '', '']),

      H.q(3, 'Siti had some stickers. She gave 24 stickers to her brother. Then her mother gave her 15 more. Now she has 50 stickers. How many stickers did Siti have at first? Fill in the two ? bars first (start from what Siti has now).', { pb: true, before: 0, keepNext: true }),
      H.fig(barQ3()), H.ans(),
      H.q(4, 'Ravi put all his sweets into 3 bags, with the same number in each bag. He took 4 sweets out of bag 3. Now bag 3 has 6 sweets. How many sweets did Ravi have altogether?', { keepNext: true }),
      H.fig(barQ4()),
      H.ans(),
      H.q(5, 'Mei and Ali both put 5 into a machine.', { keepNext: true }),
      H.sub('a', 'Mei’s machine does + 4, then × 2. What comes out?   ________'),
      H.sub('b', 'Ali’s machine does × 2, then + 4. What comes out?   ________'),
      H.sub('c', 'Do the two machines always give the same answer?   ________'),
      H.sub('d', 'What must Ali put IN to get the same OUT as Mei?   ________')
    ];
  }
};
