// Math Inquirers P4 Holiday Program — Lesson 4: Fraction Frontier (Fractions)
const N = '#1B2A49', Y = '#FFC93C', SKY = '#DDEBF7', TEAL = '#1F7A6F', WH = '#FFFFFF';
const F = 'Fredoka, Arial, sans-serif';
const tx = (x, y, s, size = 22, fill = N, anchor = 'middle', weight = 700) =>
  `<text x="${x}" y="${y}" font-size="${size}" font-weight="${weight}" text-anchor="${anchor}" fill="${fill}" font-family="${F}">${s}</text>`;
// stacked fractions for the workbook text (HTML)
const fr = (n, d) => `<span style="display:inline-flex;flex-direction:column;align-items:center;vertical-align:middle;line-height:1.05;margin:0 3px;font-weight:700"><span style="padding:0 3px">${n}</span><span style="border-top:2px solid ${N};padding:0 3px">${d}</span></span>`;
const mx = (w, n, d) => `<b>${w}</b>${fr(n, d)}`;
const box = `<span style="display:inline-block;width:38px;height:32px;border:2px solid ${N};border-radius:4px;vertical-align:middle;background:#fff;margin:0 10px"></span>`;
// stacked fraction inside an SVG
const sfr = (x, y, n, d, size = 18, fill = N) =>
  tx(x, y, n, size, fill) + `<line x1="${x - size * 0.55}" y1="${y + 5}" x2="${x + size * 0.55}" y2="${y + 5}" stroke="${fill}" stroke-width="2"/>` + tx(x, y + size + 4, d, size, fill);

// Q1: three bars cut into fifths, 13 fifths shaded
const barsSvg = () => {
  let s = `<svg aria-label="Three bars, each cut into 5 equal parts. Two whole bars and 3 parts of the third bar are shaded." viewBox="0 0 600 90" width="360" xmlns="http://www.w3.org/2000/svg" style="max-width:100%">`;
  let k = 0;
  for (let b = 0; b < 3; b++) {
    const x0 = 20 + b * 195;
    for (let i = 0; i < 5; i++) { s += `<rect x="${x0 + i * 34}" y="14" width="34" height="56" fill="${k < 13 ? Y : WH}" stroke="${N}" stroke-width="3"/>`; k++; }
    s += `<rect x="${x0}" y="14" width="170" height="56" fill="none" stroke="${N}" stroke-width="4"/>`;
  }
  return s + '</svg>';
};

// Q2: number line 0 to 3 in quarters, arrows A, B, C at 3/4, 7/4, 10/4
const lineSvg = () => {
  const x0 = 40, u = 172, y = 92;
  let s = `<svg aria-label="A number line from 0 to 3 marked in quarters, with arrows A, B and C" viewBox="0 0 600 140" width="380" xmlns="http://www.w3.org/2000/svg" style="max-width:100%">`;
  s += `<line x1="${x0 - 10}" y1="${y}" x2="${x0 + 3 * u + 14}" y2="${y}" stroke="${N}" stroke-width="3"/>`;
  for (let q = 0; q <= 12; q++) {
    const x = x0 + q * u / 4, big = q % 4 === 0;
    s += `<line x1="${x}" y1="${y - (big ? 16 : 9)}" x2="${x}" y2="${y + (big ? 16 : 9)}" stroke="${N}" stroke-width="${big ? 4 : 2.5}"/>`;
    if (big) s += tx(x, y + 42, q / 4, 22);
  }
  [['A', 3], ['B', 7], ['C', 10]].forEach(([l, q]) => {
    const x = x0 + q * u / 4;
    s += `<circle cx="${x}" cy="22" r="15" fill="${Y}" stroke="${N}" stroke-width="2.5"/>` + tx(x, 29, l, 19) +
      `<line x1="${x}" y1="38" x2="${x}" y2="${y - 22}" stroke="${TEAL}" stroke-width="3"/><polygon points="${x},${y - 14} ${x - 6},${y - 26} ${x + 6},${y - 26}" fill="${TEAL}"/>`;
  });
  return s + '</svg>';
};

// Q3: bar model template, 8 units, total 24 children
const setSvg = () => {
  let s = `<svg aria-label="A bar cut into 8 equal units, with 24 children written above the whole bar" viewBox="0 0 600 112" width="380" xmlns="http://www.w3.org/2000/svg" style="max-width:100%">`;
  s += `<path d="M60 52 Q60 38 74 38 L290 38 Q300 38 300 28 Q300 38 310 38 L526 38 Q540 38 540 52" fill="none" stroke="${N}" stroke-width="2.5"/>` + tx(300, 20, '24 children', 18, TEAL);
  for (let i = 0; i < 8; i++) s += `<rect x="${60 + i * 60}" y="58" width="60" height="44" fill="${WH}" stroke="${N}" stroke-width="3"/>`;
  return s + '</svg>';
};

module.exports = {
  lesson: {
    n: 4, week: 2, session: 'B', title: 'Fraction Frontier', topic: 'Fractions',
    objective: 'Change between improper fractions and mixed numbers using fraction bars and number lines, find a fraction of a set (and the whole set from a part) with a bar model, and compare fractions with different denominators by making the denominators the same, comparing with one half, or comparing pieces of the same numerator.',
    skills: 'Drawing a fraction model, using a number line, drawing a bar model, making a list in order, comparing with a benchmark, explaining a comparison',
    materials: 'Paper strips (one per child, to fold into halves, quarters and eighths), paper circles to cut into quarters, 30 counters, mini whiteboards and markers.',
    online: 'Before the lesson children cut out 3 paper circles and cut each into 4 equal slices; they fold paper strips on camera and hold up mini whiteboards.',
    warmup: 'More or less than a half? The tutor shows a fraction card (3/8, 5/9, 6/12, 7/10, 2/5, 4/7). Thumbs up if it is more than a half, thumbs down if less, flat hand if it is exactly a half. Then explain how you know.',
    explore: 'Pizza party: every pizza is cut into 4 equal slices and Ravi\'s group eats 11 slices. Pairs use paper quarter-slices to build whole pizzas, then write how many pizzas were eaten in two ways (11/4 and 2 3/4) and decide how many slices make exactly 3 pizzas.',
    mini: 'Improper fraction to mixed number with bars: 7/3 = 3 thirds + 3 thirds + 1 third = 2 1/3. Mixed number to improper fraction: 4 2/3 = 12 thirds + 2 thirds = 14/3. Fractions on a number line in thirds. Fraction of a set with a bar model: 3/5 of 30 (5 units = 30, 1 unit = 6, 3 units = 18). Before page 2: compare unlike fractions by making the denominators the same (2/3 = 6/9 > 5/9), by comparing with one half, or by the size of the pieces (2/5 > 2/9); find the whole from a part (2/3 of a bag is 24 marbles, so 36); find ALL fractions between two fractions by changing to the same denominator.',
    share: 'Which is more: 2 1/3 pizzas or 9/4 pizzas? Mei says 9/4 because 9 is a big number. Is she right?',
    exit: { q: 'Write 23/5 as a mixed number. Then find 3/5 of 25.', a: '4 3/5; 15.' },
    mistakes: [
      'Changing a mixed number to an improper fraction by multiplying the whole number by the numerator, or forgetting to add the numerator (3 2/5 written as 6/5 or 15/5).',
      'Thinking the bigger denominator means the bigger fraction (3/7 > 3/5 "because 7 is bigger than 5").',
      'Finding a fraction of a set by dividing by the numerator, or stopping at one unit (3/8 of 24 answered 8 or 3).'
    ],
    extension: 'Find a fraction between 2/3 and 3/4. (For example 17/24: 2/3 = 16/24 and 3/4 = 18/24. Another one is 7/10: 2/3 = 40/60, 7/10 = 42/60 and 3/4 = 45/60.)',
    key: [
      ['Q1', '(a) 13 fifths: 13/5 = 2 3/5  (b) 4 3/4  (c) 17/5  (d) 40'],
      ['Q2', '(a) A = 3/4,  B = 1 3/4 (7/4),  C = 2 2/4 = 2 1/2 (10/4)  (b) 9/4 = 2 1/4: one small mark after 2.'],
      ['Q3', '(a) 8 units = 24, 1 unit = 3, 3 units = 9 children.  (b) 5 units = 15 children (24 − 9 = 15).'],
      ['Q4', '(a) >  (3/4 = 6/8)  (b) >  (2/3 = 8/12)  (c) <  (4/9 is less than a half, 5/8 is more)  (d) >  (fifths are bigger pieces than sevenths)  (e) 7/12, 2/3, 5/6'],
      ['Q5', '(a) 3 units = 27, 1 unit = 9, 5 units = 45 sweets.  (b) 2 units = 18 sweets are not red.'],
      ['Q6', '1/3 = 4/12 and 3/4 = 9/12. The fractions in between: 5/12, 6/12, 7/12, 8/12. That is 4 fractions (4/12 and 9/12 are equal to 1/3 and 3/4, so they do not count).'],
      ['Q7', '17/6 = 2 5/6. Between 2 and 3: 13/6, 14/6, 15/6, 16/6, 17/6. Odd numerators: 13/6, 15/6, 17/6. 15/6 = 2 1/2 is exactly in the middle and 13/6 is closer to 2, so only 17/6 is closer to 3.']
    ]
  },

  script: {
    hook: ['Welcome to the Fraction Frontier! Out here, fractions can be bigger than 1, and two fractions that look different can be the same size.', 'Today we build fractions with bars, line them up on number lines and find out which fraction is really bigger. Notice it. Test it. Explain why.'],
    warmIntro: ['I will show you a fraction. Thumbs up if it is more than a half, thumbs down if it is less, flat hand if it is exactly a half.', 'Be ready to tell us HOW you know. A hint: what is half of the bottom number?'],
    predict: ['Each pizza has 4 slices. Ravi\'s group eats 11 slices. Is that more than 2 pizzas or less? More than 3? Write your guess before you build it.'],
    exploreHints: ['Stuck: put 4 slices together. That is one whole pizza. How many whole pizzas can you make?', 'Not sure how to write it: "How many quarters did they eat? How many WHOLE pizzas and how many quarters left over?"', 'Finished early: what if every pizza had 6 slices and they ate 11 slices?'],
    think: [
      '"7 thirds. 3 thirds make one whole, so I fill one bar: that uses 3. Another 3 fills a second bar. 1 third is left over. So 7/3 is 2 wholes and 1 third: 2 1/3. I can also say 7 ÷ 3 = 2 remainder 1."',
      '"4 2/3 as thirds: each whole is 3 thirds, so 4 wholes are 12 thirds. Add the 2 thirds: 14 thirds, 14/3."',
      '"3/5 of 30 stickers. The bottom number tells me how many equal units: 5. 5 units are 30, so 1 unit is 6. I need 3 units: 18."'
    ],
    circulate: ['Ask: "How many of these pieces make one whole?"', 'Ask: "Draw the bar. How many units? What is one unit worth?"', 'Ask: "Can you make the bottom numbers the same? Is it more or less than a half?"'],
    hints: ['Hint 1: "The denominator tells you how many pieces make one whole."', 'Hint 2: "For a fraction of a set, divide by the bottom number first, then multiply by the top number."', 'Hint 3: "To compare, change one fraction so both have the same denominator, or compare each with a half."'],
    talk: ['"Which is more: 2 1/3 pizzas or 9/4 pizzas? Mei says 9/4 because 9 is a big number."', '"Ravi says 3/7 is bigger than 3/5 because 7 is bigger than 5. What would you tell him?"'],
    talkAns: '2 1/3 is more. 9/4 = 2 1/4, and both have 2 wholes. A third is bigger than a quarter (sharing one pizza among 3 gives bigger slices than sharing among 4), so 2 1/3 is bigger. Mei looked at the 9 alone, but quarters are small pieces. For Ravi: 3/5 is bigger, because fifths are bigger pieces than sevenths.',
    close: ['"You were real fraction explorers today: you built fractions, lined them up and compared them with good reasons."', '"Hand me your exit ticket and I will stamp your inquiry journal."']
  },

  deck: {
    today: 'Change between improper fractions and mixed numbers, find a fraction of a set with a bar model, and compare fractions with different denominators.',
    warmGame: 'More or less than a half? Thumbs up for more, thumbs down for less, flat hand for exactly a half: 3/8, 5/9, 6/12, 7/10, 2/5, 4/7.',
    warmQs: [['1/2 of 18 = ?', '9'], ['1/4 of 20 = ?', '5'], ['2/3 = ?/12', '8'], ['3/4 + 1/8 = ?', '7/8'], ['1 − 3/10 = ?', '7/10']],
    expSetup: ['Cut paper circles into 4 equal slices (quarters).', 'Ravi\'s group eats 11 slices. Take 11 quarter-slices.', 'Put the slices together to build whole pizzas.', 'Write how many pizzas they ate in two different ways.'],
    expPic: 'three pizzas cut into quarters: two whole pizzas and one pizza with 3 of its 4 slices, next to the question "11 slices = ? pizzas".',
    expAsk: [['How many pizzas did they eat?', '2 whole pizzas and 3 quarters: 11/4 = 2 3/4.'], ['How many slices make exactly 3 pizzas?', '12 slices: 12/4 = 3.'], ['What if each pizza had 6 slices and they ate 11?', '11/6 = 1 5/6: one whole pizza and 5 sixths.']],
    mini1: { head: 'Improper fraction to mixed number', body: ['7/3: fill whole bars of 3 thirds.', '3 + 3 + 1 = 7 thirds.', '2 wholes and 1 third.'], ans: '7/3 = 2 1/3' },
    mini2: { head: 'Fraction of a set', body: ['3/5 of 30 stickers.', '5 units = 30, so 1 unit = 6.', '3 units = ?'], ans: '18 stickers' },
    keyHead: 'Key idea: fractions can be more than 1', keyBig: 'The denominator tells how many pieces make 1 whole: 7/3 = 2 1/3.', keySmall: 'Fraction of a set: the denominator gives the units. Find 1 unit, then the units you need.',
    brk: 'Fraction stand-up. I call a fraction: stand up if it is more than 1, sit down if it is less than 1, hands on your head if it is exactly 1. 5/4, 3/8, 6/6, 9/5, 7/12, 12/12.',
    ws1: 'Page 1, in pairs: Q1 fraction bars, Q2 number line, Q3 fraction of a set.',
    ws2: 'Page 2, on your own: Q4 compare, Q5 find the whole, Q6 find all the fractions, Q7 who am I?'
  },

  qbank: {
    core: [
      { q: 'Write 11/3 as a mixed number.', a: '3 2/3' },
      { q: 'Write 2 3/4 as an improper fraction.', a: '11/4' },
      { q: 'Find 1/4 of 32.', a: '8' },
      { q: 'Find 2/3 of 18.', a: '12' },
      { q: 'Which is bigger, 5/6 or 2/3?', a: '5/6 (2/3 = 4/6)' },
      { q: 'Work out 3/10 + 2/5.', a: '7/10 (2/5 = 4/10)' }
    ],
    stretch: [
      { q: 'How many quarters are there in 4 3/4?', a: '19 (4 wholes = 16 quarters, plus 3).' },
      { q: 'Siti has 40 beads. 3/8 of them are blue. How many beads are NOT blue?', a: '25 (1 unit = 5, blue = 15, not blue = 5 units = 25).' },
      { q: 'Put these fractions in order, smallest first: 2/3, 1/2, 5/6, 7/12', a: '1/2, 7/12, 2/3, 5/6 (6/12, 7/12, 8/12, 10/12).' },
      { q: '2/5 of a number is 16. What is the number?', a: '40 (2 units = 16, 1 unit = 8, 5 units = 40).' },
      { q: 'Find ALL the fractions with denominator 10 that are bigger than 1/5 but smaller than 1/2.', a: '3/10 and 4/10 (1/5 = 2/10 and 1/2 = 5/10 do not count).' },
      { q: 'A ribbon is 3 m long. Mei cuts it into pieces that are each 1/4 m long. How many pieces does she get?', a: '12 pieces (4 in each metre).' },
      { q: 'Ben ate 7/4 pizzas and Ravi ate 1 5/8 pizzas. Who ate more?', a: 'Ben. 7/4 = 14/8 = 1 6/8, which is more than 1 5/8.' },
      { q: 'Ravi says 3/7 is bigger than 3/5 because 7 is bigger than 5. Is he right? Explain.', a: 'No. Both have 3 pieces, but sevenths are smaller pieces than fifths, so 3/5 is bigger.' }
    ],
    challenge: [
      { q: 'How many fractions with denominator 12 are bigger than 1/4 but smaller than 2/3?', a: '4: 4/12, 5/12, 6/12, 7/12 (1/4 = 3/12 and 2/3 = 8/12 do not count).' },
      { q: 'Mei spent 1/3 of her money on a book and 1/4 of her money on a pen. She had $25 left. How much money did she have at first?', a: '$60. Book 4/12, pen 3/12, so 5/12 is left. 5 units = $25, 1 unit = $5, 12 units = $60.' },
      { q: 'A tank is 3/8 full of water. After 15 litres more are poured in, it is 3/4 full. How many litres does the full tank hold?', a: '40 litres. 3/4 = 6/8, so 15 litres is 3/8. 1/8 = 5 litres, 8/8 = 40 litres.' },
      { q: 'Use two of the digit cards 2, 3, 5 and 7 to make a fraction smaller than 1 that is as close to 1 as possible.', a: '5/7. It is 2/7 short of 1. The next best, 2/3, is 1/3 = 2/6 short, and 2/7 is less than 2/6.' },
      { q: 'In a bag of marbles, 1/4 are red and 1/3 are blue. The other 10 marbles are green. How many marbles are in the bag?', a: '24. Red 3/12 and blue 4/12, so green is 5/12. 5 units = 10, 1 unit = 2, 12 units = 24.' },
      { q: 'A cake is cut into 12 equal pieces. Mei eats 1/4 of the cake and Ben eats 1/3 of the cake. How many pieces are left?', a: '5 pieces (Mei 3 pieces, Ben 4 pieces, 12 − 7 = 5).' },
      { q: 'I am a fraction equal to 3/4. My numerator and denominator add up to 28. Who am I?', a: '12/16. 3/4 has 3 + 4 = 7 parts; 28 ÷ 7 = 4, so 3 × 4 = 12 and 4 × 4 = 16.' },
      { q: 'Half of a number is 3 more than a third of the number. What is the number?', a: '18. Half = 3 sixths and a third = 2 sixths, so 1 sixth = 3 and the number is 6 sixths = 18. Check: 9 is 3 more than 6.' },
      { q: 'Siti read 2/5 of her book on Monday. On Tuesday she read half of the pages that were left. She still has 45 pages to read. How many pages are in the book?', a: '150 pages. Cut each fifth in half to make tenths: Monday 4 tenths, the rest is 6 tenths, Tuesday 3 tenths, 3 tenths left = 45. 1 tenth = 15, 10 tenths = 150.' }
    ]
  },

  workbook: H => {
    const W = [];
    W.push(H.p(['<b>Improper fraction:</b> 1 or more, like ', fr(7, 4), '.   <b>Mixed number:</b> a whole number and a fraction, like ', mx(1, 3, 4), '.'], { after: 40 }));
    W.push(H.q(1, 'Each bar is one whole.', { before: 40, keepNext: true }));
    W.push(H.fig(barsSvg()));
    W.push(H.sub('a', 'Fifths shaded: _____    Improper fraction: _____    Mixed number: _____'));
    W.push(H.sub('b', ['Write ', fr(19, 4), ' as a mixed number. ______     <b style="color:#1F7A6F">c</b>  Write ', mx(3, 2, 5), ' as an improper fraction. ______']));
    W.push(H.sub('d', 'How many eighths are there in 5 wholes?     ______'));
    W.push(H.q(2, 'This number line is marked in quarters.', { keepNext: true }));
    W.push(H.fig(lineSvg()));
    W.push(H.sub('a', 'Write the number at each arrow.     A = ______     B = ______     C = ______'));
    W.push(H.sub('b', ['Mark ', fr(9, 4), ' on the number line with an X.']));
    W.push(H.q(3, ['Fraction of a set. There are 24 children in a class. ', fr(3, 8), ' of them wear glasses. Use the bar model.'], { keepNext: true }));
    W.push(H.fig(setSvg()));
    W.push(H.sub('a', ['How many wear glasses? ______      <b style="color:#1F7A6F">b</b>  How many do NOT wear glasses? ______']));

    W.push(H.q(4, 'Compare. Write > or < in each box. Then write how you know.', { pb: true, before: 0, keepNext: true }));
    W.push(H.sub('a', [fr(3, 4), box, fr(5, 8), '     ____________________________']));
    W.push(H.sub('b', [fr(2, 3), box, fr(7, 12), '     ____________________________']));
    W.push(H.sub('c', [fr(4, 9), box, fr(5, 8), '     ____________________________']));
    W.push(H.sub('d', [fr(3, 5), box, fr(3, 7), '     ____________________________']));
    W.push(H.sub('e', ['Put in order, smallest first:   ', fr(2, 3), ',  ', fr(5, 6), ',  ', fr(7, 12), '        ________,  ________,  ________']));
    W.push(H.q(5, ['', fr(3, 5), ' of the sweets in a jar are red. There are 27 red sweets.'], { keepNext: true }));
    W.push(H.sub('a', 'Draw a bar model. How many sweets are in the jar?'));
    W.push(H.gap(700));
    W.push(H.ans());
    W.push(H.sub('b', 'How many sweets are NOT red?'));
    W.push(H.ans());
    W.push(H.q(6, ['Find ALL the fractions with denominator 12 that are bigger than ', fr(1, 3), ' but smaller than ', fr(3, 4), '.'], { keepNext: true }));
    W.push(...H.lines(2));
    W.push(H.ans('How many?'));
    W.push(H.q(7, 'Who am I? I am an improper fraction. My denominator is 6. I am between 2 and 3. My numerator is an odd number. I am closer to 3 than to 2.', { keepNext: true }));
    W.push(H.sub('a', 'Make a list, then cross out the ones that do not fit.'));
    W.push(...H.lines(2));
    W.push(H.ans('I am:'));
    return W;
  }
};
