// Math Inquirers P2 Holiday Program — Lesson 2: Missing Digit Mysteries (Addition and subtraction within 1000)
const N = '#1B2A49', Y = '#FFC93C', SKY = '#DDEBF7', TEAL = '#1F7A6F', WH = '#FFFFFF';
const F = 'Fredoka, Arial, sans-serif';
const T = (x, y, s, size = 30, fill = N, anchor = 'middle', weight = 700) =>
  `<text x="${x}" y="${y}" font-size="${size}" font-weight="${weight}" text-anchor="${anchor}" fill="${fill}" font-family="${F}">${s}</text>`;

// one column sum; '?' is a box to fill. x0 = left edge of the sign column
const colSum = (x0, label, top, bot, res, op) => {
  const c = 40, rows = [top, bot, res], ys = [60, 108, 176];
  let s = T(x0 + 4, 30, label, 22, TEAL, 'start');
  rows.forEach((r, ri) => {
    const digs = r.split('');
    digs.forEach((d, i) => {
      const x = x0 + 30 + (3 - digs.length + i) * c + (4 - 3) * c; // right-aligned in 4 columns
      if (d === '?') s += `<rect x="${x - 16}" y="${ys[ri] - 32}" width="32" height="40" rx="6" fill="${Y}" fill-opacity="0.35" stroke="${N}" stroke-width="2.5"/>`;
      else s += T(x, ys[ri], d, 32);
    });
  });
  s += T(x0 + 22, 108, op, 32);
  s += `<line x1="${x0 + 10}" y1="126" x2="${x0 + 30 + 4 * c}" y2="126" stroke="${N}" stroke-width="3"/>`;
  return s;
};
const sumsSvg = (items, label) => {
  const w = 200, vw = items.length * 200, px = items.length * 180;
  let s = `<svg aria-label="${label}" viewBox="0 0 ${vw} 196" width="${px}" xmlns="http://www.w3.org/2000/svg" style="width:${px}px;max-width:100%">`;
  items.forEach((it, i) => { s += colSum(i * w + (w - 200) / 2, it[0], it[1], it[2], it[3], it[4]); });
  return s + '</svg>';
};

// a 3 by 3 magic square with some numbers given
const squareSvg = g => {
  const c = 66, x0 = 300 - 1.5 * c;
  let s = `<svg aria-label="Magic square with 80, 60, 50, 40 and 20 given" viewBox="0 0 600 206" width="600" xmlns="http://www.w3.org/2000/svg" style="max-width:100%">`;
  g.forEach((r, ri) => r.forEach((v, ci) => {
    s += `<rect x="${x0 + ci * c}" y="${4 + ri * c}" width="${c}" height="${c}" fill="${v === '' ? WH : SKY}" stroke="${N}" stroke-width="3"/>`;
    if (v !== '') s += T(x0 + ci * c + c / 2, 4 + ri * c + c / 2 + 10, v, 28);
  }));
  return s + '</svg>';
};

// two empty magic triangles with the number tiles
const triSvg = () => {
  const one = (ox, title, pre = {}) => {
    const pos = [[150, 40], [40, 230], [260, 230], [95, 135], [150, 230], [205, 135]];
    let s = T(ox + 150, -14, title, 20, TEAL);
    s += `<polygon points="${ox + 150},40 ${ox + 40},230 ${ox + 260},230" fill="none" stroke="${N}" stroke-width="3" stroke-linejoin="round"/>`;
    pos.forEach(([x, y], i) => { s += `<circle cx="${ox + x}" cy="${y}" r="26" fill="${i < 3 ? Y : WH}" stroke="${N}" stroke-width="3"/>`; if (pre[i]) s += T(ox + x, y + 7, pre[i], 20); });
    return s;
  };
  let s = `<svg aria-label="Two magic triangles (the first has 110 and 120 in two corners) and the numbers 110 to 160" viewBox="0 0 600 392" width="480" xmlns="http://www.w3.org/2000/svg" style="width:480px;max-width:100%">`;
  s += `<g transform="translate(0,34)">${one(0, '(a) Each side = 390', { 0: 110, 1: 120 })}${one(300, '(b) Each side = 420')}</g>`;
  s += `<rect x="40" y="296" width="520" height="86" rx="12" fill="none" stroke="${N}" stroke-width="2" stroke-dasharray="6 4"/>` + T(300, 320, 'Number tiles: use all six in EACH triangle', 18, TEAL);
  [110, 120, 130, 140, 150, 160].forEach((n, i) => {
    const x = 60 + i * 82;
    s += `<rect x="${x}" y="332" width="70" height="40" rx="8" fill="${SKY}" stroke="${N}" stroke-width="2.5"/>` + T(x + 35, 361, n, 22);
  });
  return s + '</svg>';
};

module.exports = {
  lesson: {
    n: 2, week: 1, session: 'B', title: 'Missing Digit Mysteries', topic: 'Addition and Subtraction within 1000',
    objective: 'Find missing digits in 3-digit addition and subtraction by starting at the ones and checking for a carry, use "=" as "is the same as" to balance number sentences, and complete magic squares and triangles with bigger numbers.',
    skills: 'Working backwards, guess and check, reasoning about regrouping, balancing, drawing a model',
    materials: 'Digit cards 0 to 9, base-ten blocks or place-value counters, mini whiteboards, a paper magic triangle with 6 circles and number tiles 110 to 160.',
    online: 'Children write column sums on whiteboards and say the answer together on three; number tiles are cut from paper before the lesson. The tutor writes on the slide sums.',
    warmup: 'Partners to 100 and 1000: the tutor says a number and children call out its partner (65 → 35, then 370 → 630, then 125 → 875).',
    explore: 'Pairs pick any 3-digit number and find its partner that makes 999, then check by adding. They do it for several numbers and look at the digits in each column.',
    mini: 'Missing digits: start at the ones column and ask "was there a carry?" (4[ ]7 + 28[ ] = 723 gives 437 + 286). For subtraction, turn it into an addition and work backwards (6[ ]2 − 24[ ] = 385 becomes 385 + 24[ ] = 6[ ]2). Balance: 245 + 130 = 200 + [ ]; 245 is 45 more than 200, so the box is 45 more than 130 (175). Before page 2: magic squares (find a full line for the total, then total minus the two you know), magic triangles (small side totals need small corners), and two numbers from their total and difference (take away the extra, halve, give it back).',
    share: 'Why do we start at the ones column when we look for missing digits?',
    exit: { q: '3[ ]4 + 257 = 601. Which digit goes in the box?', a: 'The box is 4 (344 + 257 = 601: ones 4 + 7 = 11; tens 4 + 5 + 1 = 10). Bonus for anyone who would like it: 4[ ]6 + 37[ ] = 801 gives 2 in the first box and 5 in the second box (426 + 375 = 801).' },
    mistakes: [
      'Forgetting the carried 1: in Q1c writing 6 in the tens box (8 + 6 = 14) instead of 5 (8 + 5 + 1 = 14).',
      'Reading "=" as "the answer comes next": 350 + 140 = 300 + [ ] answered 490.',
      'Magic triangle: putting the biggest numbers in the corners when the side total is small (390 needs the smallest corners).'
    ],
    takehome: 'Page 1: the line under Q1 (check one answer by adding the full numbers), and Q3 c and d (480 + ___ = 500 + 260, and Ravi\'s 398 + 205). Page 2: the whole of Q5 (the magic triangle); its teaching slide is not shown in class.',
    extension: 'Make your own missing-digit sum with two boxes that has exactly ONE answer. Swap with a partner. (Check: does any other digit also work?)',
    key: [
      ['Q1', '(a) 224 + 355 = 579  (b) 462 + 375 = 837  (c) 386 + 259 = 645'],
      ['Q2', '(a) 778 − 325 = 453  (b) 543 − 267 = 276'],
      ['Q3', '(a) 190  (b) 525  (c) 280  (d) Yes. 398 is 2 less than 400 and 205 is 2 more than 203, so both sides are the same (603).'],
      ['Q4', '(a) 150 (diagonal 80 + 50 + 20)  (b) Top: 10. Middle: 30 and 70. Bottom: 90.  (c) Yes, still magic. New total 450: every line has 3 numbers and each is 100 more, so 150 + 300.'],
      ['Q5', '(a) Corners 110, 120, 130. Between 110 and 120: 160. Between 120 and 130: 140. Between 130 and 110: 150. (Think harder 1 is the same triangle with sides of 420: corners 140, 150, 160; between 140 and 150: 130; between 150 and 160: 110; between 160 and 140: 120.)'],
      ['Q6', '250 and 450 (700 − 200 = 500, half of 500 is 250, 250 + 200 = 450).']
    ]
  },

  script: {
    hook: ['Welcome back, detectives! Someone has spilled ink on our sums and some digits have disappeared.', 'Today we find the missing digits, make both sides of "=" balance, and crack some magic squares. Notice it. Test it. Explain why.'],
    warmIntro: ['I say a number. You say its partner to make 100. Ready? 65!', 'Now partners to 1000. 370! How did you find 630 so fast?'],
    predict: ['Pick any 3-digit number. I predict that its partner to make 999 will be easy to find, with no carrying at all. Do you think I am right? Let us test it.'],
    exploreHints: ['Stuck: start with the hundreds. What goes with 3 to make 9?', 'Not sure: add your two numbers in a column sum to check the total is 999.', 'Finished early: try partners to 1000. What changes in the ones column?'],
    think: [
      '“4[ ]7 + 28[ ] = 723. I start at the ones: 7 plus the ones box ends in 3. 7 + 6 = 13. So the ones box is 6, and I carry 1 ten.”',
      '“Tens: the tens box + 8 + the carried 1 ends in 2. 3 + 8 + 1 = 12. So the tens box is 3, and I carry 1 hundred. Hundreds: 4 + 2 + 1 = 7. It matches! I check by adding: 437 + 286 = 723.”',
      '“6[ ]2 − 24[ ] = 385. Subtraction is harder, so I work backwards and turn it into an addition: 385 + 24[ ] = 6[ ]2. Ones: 5 + the ones box ends in 2, 5 + 7 = 12, so it is 7. Tens: 8 + 4 + 1 = 13, so the tens box is 3. Hundreds: 3 + 2 + 1 = 6 ✓.”',
      '“245 + 130 = 200 + [ ]. I do not need to add. 245 is 45 more than 200, so the box must be 45 more than 130. That is 175. Both sides are 375.”'
    ],
    circulate: ['Ask: “Which column did you start with? Why?”', 'Ask: “Was there a carry into this column? How do you know?”', 'Ask: “What is each side of the = sign worth? Are they the same?”'],
    hints: ['Hint 1: “Start at the ones column.”', 'Hint 2: “Try a digit in the box and add. Too big or too small?”', 'Hint 3: “Turn the subtraction into an addition: answer + bottom number = top number.”'],
    talk: ['“Why do we start at the ones column when we look for missing digits?”'],
    talkAns: 'The ones column can make a carry that changes the tens column, and the tens can change the hundreds, so we must know the ones first.',
    close: ['“You were digit detectives again: you started at the ones, checked every carry and proved each answer by adding.”', '“Exit ticket, then your stamp.”']
  },

  deck: {
    today: 'Find missing digits in 3-digit sums, make both sides of "=" balance, and solve magic squares and triangles with bigger numbers.',
    warmGame: 'Partners to 100 and 1000. The tutor says a number; say its partner. 65 → 35, then 370 → 630, then 125 → 875.',
    warmQs: [['65 + __ = 100', '35'], ['300 + 450 = ?', '750'], ['700 − 250 = ?', '450'], ['238 + 10 = ?', '248'], ['500 − __ = 120', '380']],
    expSetup: ['Pick any 3-digit number, like 358.', 'Find its partner that makes 999. Check by adding.', 'Do it for three more numbers.', 'Look at each column. What do you notice?'],
    expPic: 'a column sum 358 + 641 = 999 with each column shaded and the label "9" above each column.',
    expAsk: [['What did you notice about each column?', 'The two digits in each column add up to 9.'], ['Why is there never a carry?', 'No column adds up to more than 9.'], ['Find the partner of 274 without adding.', '725: 2 + 7, 7 + 2 and 4 + 5 all make 9.']],
    mini1: { head: 'Missing digits: start at the ones', body: ['4[ ]7 + 28[ ] = 723', 'Ones: 7 + the ones box ends in 3, so it is 6 (13, carry 1).', 'Tens: the tens box + 8 + 1 ends in 2, so it is 3 (12, carry 1).', 'Hundreds: 4 + 2 + 1 = 7 ✓'], ans: '437 + 286 = 723.' },
    mini2: { head: 'Balance: "=" means "is the same as"', body: ['245 + 130 = 200 + [ ]', '245 is 45 more than 200, so the box is 45 more than 130.'], ans: '175. Both sides are 375.' },
    keyHead: 'Key idea: start at the ones', keyBig: 'Start at the ones column and ask: was there a carry? Check by adding.', keySmall: 'Turn a subtraction into an addition to work backwards. "=" means both sides are the same.',
    brk: 'Balance bodies. Stand like a see-saw with arms out. The tutor says a number sentence: stay level if it is true, tip to one side if it is false.',
    ws1: 'Page 1, in pairs: Q1 missing digits in additions, Q2 in subtractions, Q3 balance it.',
    ws2: 'Page 2, on your own: Q4 magic square, Q5 magic triangles, Q6 two mystery numbers.'
  },

  qbank: {
    core: [
      { q: '3[ ]5 + 214 = 579. Which digit goes in the box?', a: '6 (365 + 214 = 579)' },
      { q: '6[ ]8 − 205 = 433. Which digit goes in the box?', a: '3 (638 − 205 = 433)' },
      { q: 'What number goes in the box to make this true?  400 + 250 = 300 + [ ]', a: '350' },
      { q: 'What must be added to 365 to make 500?', a: '135' },
      { q: 'What number goes in the box?  [ ] − 150 = 600', a: '750' },
      { q: 'True or false? 299 + 101 = 300 + 100. Explain.', a: 'True. 299 is 1 less than 300 and 101 is 1 more than 100, so both sides are 400.' }
    ],
    stretch: [
      { q: 'A magic triangle has 3 corner circles and 3 circles in the middle of the sides. Put the numbers 110, 120, 130, 140, 150 and 160 in the circles, once each, so that every side adds up to 420. Draw the triangle. Which numbers are in the corners?', a: 'Corners 140, 150, 160. Between 140 and 150: 130. Between 150 and 160: 110. Between 160 and 140: 120 (each side: 140 + 130 + 150 = 420, 150 + 110 + 160 = 420, 160 + 120 + 140 = 420).' },
      { q: 'Find the missing digits:  5[ ] + [ ]7 + 38 = 132. There are three numbers, so the carry from the ones may be more than 1.', a: '57 + 37 + 38 = 132. Ones: 7 + 7 + 8 = 22, so write 2 and carry 2 tens. Tens: 5 + 3 + 3 + 2 = 13. The first box is 7 and the second box is 3.' },
      { q: 'Mei did 523 − 267 and wrote 266. She checked by adding 266 + 267 = 533. Was her answer right? What mistake did she make? What is the right answer?', a: 'No. Her check gives 533, not 523, so 266 is wrong. The right answer is 256 (ones: 13 − 7 = 6; tens: the 2 tens lent 1 ten to the ones, so 1 ten is left and we borrow again: 11 − 6 = 5; hundreds: 4 − 2 = 2). Check: 256 + 267 = 523. Mei’s tens digit is 1 too big: she forgot that the tens had already lent 1 ten to the ones.' },
      { q: 'True or false? Say how you know without working out both sides. (a) 346 + 199 = 345 + 200  (b) 270 + 130 = 260 + 150  (c) 618 + 99 = 600 + 117', a: '(a) True: 346 is 1 more than 345 and 199 is 1 less than 200. (b) False: 270 is 10 more than 260, but 130 is 20 less than 150, so the sides are 400 and 410. (c) True: 618 is 18 more than 600 and 99 is 18 less than 117 (both sides are 717).' },
      { q: 'A shop had 905 eggs. It sold some in the morning and 260 in the afternoon. 345 eggs were left. How many eggs were sold in the morning?', a: '300. Work backwards: 345 + 260 = 605 eggs after the morning sales; 905 − 605 = 300.' },
      { q: 'What number goes in the box to make this true?  900 − [ ] = 450 + 175', a: '275 (450 + 175 = 625 and 900 − 625 = 275).' },
      { q: 'Which is bigger, 347 + 258 or 350 + 255? Explain how you know without adding.', a: 'They are the same (both 605). 347 is 3 less than 350 and 258 is 3 more than 255, so moving 3 from one number to the other does not change the total.' },
      { q: 'The numbers 20, 40, 60, 80, 100, 120, 140, 160 and 180 make a magic square. What is the magic total? Which number goes in the middle?', a: '300 (all nine add up to 900, shared equally by the 3 rows). The middle is 100.' },
      { q: 'Put 11, 12, 13, 14, 15 and 16 in a magic triangle so each side adds up to 39. Which numbers go in the corners?', a: '11, 12 and 13. Between 11 and 12: 16. Between 12 and 13: 14. Between 13 and 11: 15.' }
    ],
    challenge: [
      { q: 'Use the digit cards 1, 2, 3, 4, 5 and 6 once each to make two 3-digit numbers. Make the difference as BIG as possible.', a: '531: 654 − 123.' },
      { q: 'The same number goes in both boxes:  [ ] + 150 = 550 − [ ]. What is the number?', a: '200 (200 + 150 = 350 and 550 − 200 = 350).' },
      { q: 'I add 199 to my number, then take away 99. I get 650. What is my number?', a: '550. Work backwards: 650 + 99 = 749, then 749 − 199 = 550.' },
      { q: 'Put 110, 120, 130, 140, 150 and 160 in a magic triangle. What is the smallest side total you can make? The biggest? Find a triangle with side total 400. Could the side total be 380? Explain.', a: 'Smallest 390 (corners 110, 120, 130) and biggest 420 (corners 140, 150, 160). For 400 use corners 110, 130 and 150, with 160 between 110 and 130, 120 between 130 and 150, and 140 between 150 and 110. 380 is impossible: the three corners are counted twice, so the 3 sides add up to 810 plus the corners, and the corners add up to at least 360, so each side is at least 390.' },
      { q: 'Make up your own missing-digit addition with TWO missing digits (use two boxes) that has exactly ONE answer. Then make one with two missing digits that has MORE than one answer. What is different about the second one? Swap with a partner and check each other’s.', a: 'Open. Example with one answer: 4[ ]6 + 37[ ] = 801 (426 + 375; ones 6 + 5 = 11 forces the second box, then the tens force the first). Example with more than one answer: [ ][ ]7 + 4[ ][ ] = 1000, where the tens digits only need to add up to 9, so there are 10 answers. When two missing digits in the same column only need to add up to a fixed number, many pairs of digits work.' },
      { q: 'What is the smallest 3-digit number you can add to 386 so that the answer has three digits that are all the same?', a: '169 (386 + 169 = 555). 444 is only 58 more than 386, and 58 is not a 3-digit number.' },
      { q: 'Find ALL the ways to fill in the four boxes:  [ ][ ]7 + 4[ ][ ] = 1000', a: '10 ways: 507 + 493, 517 + 483, 527 + 473, 537 + 463, 547 + 453, 557 + 443, 567 + 433, 577 + 423, 587 + 413, 597 + 403. Ones: 7 + 3 = 10. Hundreds: 5 + 4 + 1 = 10. The two tens digits add up to 9 (with the carried 1 they make 10).' },
      { q: 'Box A and Box B hold 250 marbles together. Box B and Box C hold 350. Box A and Box C hold 400. How many marbles are in each box?', a: 'Box A 150, Box B 100, Box C 250. Box B + Box C is 100 more than Box A + Box B, so Box C has 100 more than Box A. Box A and Box C together are 400: take away the extra 100 to get 300, and half of 300 is 150. So Box A has 150 and Box C has 250. Then Box B has 250 − 150 = 100.' },
      { q: 'Use the digit cards 1, 2, 3, 4, 5 and 6 once each to make two 3-digit numbers. Make the difference as SMALL as possible.', a: '47: 412 − 365. The hundreds digits are next to each other (4 and 3); then make the number starting with 4 as small as possible (412) and the one starting with 3 as big as possible (365).' }
    ]
  },

  workbook: H => {
    const W = [];
    const TH = () => H.t('★ take-home  ', { bold: true, color: '1B2A49' });
    W.push(H.p('Each yellow box hides one digit (on the slides a hidden digit is a box too). Start at the ones column. Ask: was there a carry?', { after: 60 }));
    W.push(H.q(1, 'Find the missing digits. Write them in the boxes.', { before: 60, keepNext: true }));
    W.push(H.fig(sumsSvg([['(a)', '2?4', '35?', '579', '+'], ['(b)', '46?', '?75', '837', '+'], ['(c)', '?86', '2?9', '645', '+']], 'Three additions with missing digits')));
    W.push(H.p([TH(), H.t('Check one of your answers by adding the full numbers:  ______ + ______ = ______')], { after: 100 }));
    W.push(H.q(2, 'Find the missing digits. Try a digit and check it. Check: answer + the number you took away = the number you started with. Tip for (b): 3 − 7 cannot be done, so think 13 − 7.', { keepNext: true }));
    W.push(H.fig(sumsSvg([['(a)', '7?8', '32?', '453', '−'], ['(b)', '5?3', '?67', '276', '−']], 'Two subtractions with missing digits')));
    W.push(H.q(3, 'The = sign means “is the same as”. Fill in the boxes.', { keepNext: true }));
    W.push(H.sub('a', '350 + 140  =  300 + ______'));
    W.push(H.sub('b', '625 − 200  =  ______ − 100'));
    W.push(H.sub('c', [TH(), H.t('480 + ______  =  500 + 260')]));
    W.push(H.sub('d', [TH(), H.t('Ravi says 398 + 205 = 400 + 203 is true. Is he right? Explain how you know without adding.')]));
    W.push(...H.lines(2));

    W.push(H.q(4, 'Magic square. Every row, column and diagonal adds up to the same total.', { keepNext: true }));
    W.push(H.fig(squareSvg([[80, '', 60], ['', 50, ''], [40, '', 20]])));
    W.push(H.gap(60));
    W.push(H.sub('a', 'What is the magic total? (Find a line with all three numbers.)   ________'));
    W.push(H.sub('b', 'Fill in the empty squares.'));
    W.push(H.sub('c', 'Add 100 to every number. Is it still a magic square? What is the new total? Explain.'));
    W.push(...H.lines(2));
    W.push(H.q(5, [TH(), H.t('Magic triangle. Put the numbers 110, 120, 130, 140, 150 and 160 in the circles, once each, so every side has the same total.')], { keepNext: true }));
    W.push(H.fig(triSvg()));
    W.push(H.sub('a', 'Each side adds up to 390. The numbers 110 and 120 are already in two corners. First: what goes between them? Then fill in all the circles. Which numbers are in the corners?  __________'));
    W.push(H.sub('b', 'Each side adds up to 420. Fill in the second triangle. Which numbers are in the corners?  __________'));
    W.push(H.q(6, 'Mei thinks of two numbers. They add up to 700. One number is 200 more than the other. What are the two numbers? Draw a model: two bars, and the long bar is 200 longer.', { keepNext: true }));
    W.push(...H.lines(4));
    W.push(H.p([H.t('Answer:   ____________   and   ____________', { bold: true })], { indent: { left: 560 }, before: 60 }));
    return W;
  }
};
