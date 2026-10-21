// Math Inquirers P6 — Lesson 6: Fair or Unfair? (probability as a fraction; random numbers; running a game 1000 times)
// Every probability below was computed exactly with fractions by listing all equally likely outcomes, and sanity-checked by simulation.

const NAVY = '#1B2A49', YEL = '#FFC93C', SKY = '#DDEBF7', TEAL = '#1F7A6F', RED = '#D64545', WHITE = '#FFFFFF';
const escx = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

// Code blocks in our own simple style: [kind, text, children?, elseChildren?]
// kinds: hat (start block), ctrl (repeat / if), var (set / change), look (say). [text] = a white value pill, [?] = an empty gap.
const BK = { hat: [RED, WHITE], ctrl: [YEL, NAVY], var: [TEAL, WHITE], look: [SKY, NAVY] };
function blocks(nodes, label, fs = 15) {
  const h = Math.round(fs * 1.9), step = Math.round(fs * 1.2), cw = fs * 0.58, F = 'Arial, sans-serif';
  const segs = t => t.split(/(\[[^\]]*\])/).filter(s => s.trim() !== '');
  const pillW = c => c === '?' ? fs * 5 : c.length * cw + fs;
  const textW = t => segs(t).reduce((w, s) => w + (s[0] === '[' ? pillW(s.slice(1, -1)) : s.trim().length * cw) + fs * 0.35, 0);
  const out = []; let maxX = 0;
  const txt = (x, y, t, fg) => {
    let cx = x, s = '';
    for (const g of segs(t)) {
      if (g[0] === '[') {
        const c = g.slice(1, -1), w = pillW(c), ph = h - 9;
        s += `<rect x="${cx.toFixed(1)}" y="${(y - ph / 2).toFixed(1)}" width="${w.toFixed(1)}" height="${ph}" rx="${ph / 2}" fill="${WHITE}" stroke="${NAVY}" stroke-width="1.5"${c === '?' ? ' stroke-dasharray="4 3"' : ''}/>`;
        if (c !== '?') s += `<text x="${(cx + w / 2).toFixed(1)}" y="${(y + fs * 0.36).toFixed(1)}" font-size="${fs}" font-weight="700" text-anchor="middle" fill="${NAVY}" font-family="${F}">${escx(c)}</text>`;
        cx += w + fs * 0.35;
      } else {
        const t2 = g.trim();
        s += `<text x="${cx.toFixed(1)}" y="${(y + fs * 0.36).toFixed(1)}" font-size="${fs}" font-weight="700" fill="${fg}" font-family="${F}">${escx(t2)}</text>`;
        cx += t2.length * cw + fs * 0.35;
      }
    }
    maxX = Math.max(maxX, cx); return s;
  };
  const lay = (list, x, y) => {
    for (const [kind, text, kids, els] of list) {
      const [bg, fg] = BK[kind]; const w = Math.max(textW(text) + fs * 1.2, fs * 5);
      if (!kids) {
        out.push(`<rect x="${x}" y="${y}" width="${w.toFixed(1)}" height="${h}" rx="${kind === 'hat' ? fs * 0.9 : 5}" fill="${bg}" stroke="${NAVY}" stroke-width="2"/>` + txt(x + fs * 0.6, y + h / 2, text, fg));
        maxX = Math.max(maxX, x + w); y += h;
      } else {
        const y0 = y, idx = out.length; out.push('');
        let labels = txt(x + fs * 0.6, y0 + h / 2, text, fg); y += h; y = lay(kids, x + step, y);
        let yE = null; if (els) { yE = y; labels += txt(x + fs * 0.6, y + h / 2, 'else', fg); y += h; y = lay(els, x + step, y); }
        const hb = Math.round(h * 0.55), wb = fs * 5;
        const pts = [[x, y0], [x + w, y0], [x + w, y0 + h], [x + step, y0 + h]];
        if (els) pts.push([x + step, yE], [x + wb, yE], [x + wb, yE + h], [x + step, yE + h]);
        pts.push([x + step, y], [x + wb, y], [x + wb, y + hb], [x, y + hb]);
        out[idx] = `<polygon points="${pts.map(p => p.map(v => (+v).toFixed(1)).join(',')).join(' ')}" fill="${bg}" stroke="${NAVY}" stroke-width="2" stroke-linejoin="round"/>` + labels;
        y += hb; maxX = Math.max(maxX, x + w);
      }
    }
    return y;
  };
  const Hh = Math.ceil(lay(nodes, 2, 2) + 2), W = Math.ceil(maxX + 4);
  return `<svg aria-label="${escx(label)}" viewBox="0 0 ${W} ${Hh}" xmlns="http://www.w3.org/2000/svg" style="width:${W}px;max-width:100%">${out.join('')}</svg>`;
}
// optional Python version in a small dashed box
function pyBox(lines, title, W = 380) {
  const lh = 16, Hh = 58 + lines.length * lh;
  let s = `<svg aria-label="${escx(title.replace('|', ' '))}" viewBox="0 0 ${W} ${Hh}" xmlns="http://www.w3.org/2000/svg" style="width:${W}px;max-width:100%"><rect x="2" y="2" width="${W - 4}" height="${Hh - 4}" rx="10" fill="${WHITE}" stroke="${NAVY}" stroke-width="2" stroke-dasharray="7 5"/>`;
  title.split('|').forEach((tl, i) => { s += `<text x="16" y="${25 + i * 19}" font-size="15" font-weight="700" fill="${TEAL}" font-family="Arial, sans-serif">${escx(tl)}</text>`; });
  lines.forEach((l, i) => { s += `<text x="16" y="${64 + i * lh}" font-size="14" fill="${NAVY}" font-family="Courier New, monospace" xml:space="preserve" style="white-space:pre">${escx(l)}</text>`; });
  return s + '</svg>';
}

// spinner with 8 equal parts: 3 red (R), 2 blue (B), 2 yellow (Y), 1 green (G)
const spinner = () => {
  const cols = [['R', RED, WHITE], ['B', SKY, NAVY], ['Y', YEL, NAVY], ['R', RED, WHITE], ['G', TEAL, WHITE], ['B', SKY, NAVY], ['R', RED, WHITE], ['Y', YEL, NAVY]];
  const cx = 110, cy = 110, r = 96; let s = `<svg aria-label="A spinner with 8 equal parts: 3 red, 2 blue, 2 yellow and 1 green" viewBox="0 0 220 220" xmlns="http://www.w3.org/2000/svg" style="width:220px;max-width:100%">`;
  cols.forEach(([l, f, fg], i) => {
    const a0 = (i * 45 - 90) * Math.PI / 180, a1 = ((i + 1) * 45 - 90) * Math.PI / 180, am = (a0 + a1) / 2;
    s += `<path d="M${cx},${cy} L${(cx + r * Math.cos(a0)).toFixed(1)},${(cy + r * Math.sin(a0)).toFixed(1)} A${r},${r} 0 0 1 ${(cx + r * Math.cos(a1)).toFixed(1)},${(cy + r * Math.sin(a1)).toFixed(1)} Z" fill="${f}" stroke="${NAVY}" stroke-width="2.5"/>`;
    s += `<text x="${(cx + 66 * Math.cos(am)).toFixed(1)}" y="${(cy + 66 * Math.sin(am) + 8).toFixed(1)}" font-size="22" font-weight="700" text-anchor="middle" fill="${fg}" font-family="Arial">${l}</text>`;
  });
  s += `<line x1="${cx}" y1="${cy}" x2="${cx + 30}" y2="${cy - 44}" stroke="${NAVY}" stroke-width="6" stroke-linecap="round"/><circle cx="${cx}" cy="${cy}" r="9" fill="${NAVY}"/>`;
  return s + '</svg>';
};
const coinCode = [['hat', 'when green flag clicked'], ['var', 'set heads to [0]'], ['ctrl', 'repeat [1000]', [['ctrl', 'if [pick random 1 to 2] = [1] then', [['var', 'change heads by [1]']]]]], ['look', 'say heads']];
const planCode = [['hat', 'when green flag clicked'], ['var', 'set doubles to [0]'], ['ctrl', 'repeat [1000]', [['var', 'set a to pick random 1 to [?]'], ['var', 'set b to pick random 1 to [?]'], ['ctrl', 'if [?] then', [['var', 'change doubles by [1]']]]]], ['look', 'say doubles']];

module.exports = {
  lesson: {
    n: 6, week: 3, session: 'B', title: 'Fair or Unfair?', topic: 'Probability',
    objective: 'Write a probability as a fraction (ways it can happen out of equally likely outcomes), list all 36 outcomes for two dice, decide whether a game is fair, change a game to make it fair, and run a game 1000 times in code, explaining why the result is close to what we expect but not exact.',
    skills: 'Listing equally likely outcomes, fractions in simplest form, expected number = fraction × number of tries, judging fairness, simulating with random numbers',
    materials: 'Laptop or desktop with Scratch 3 (scratch.mit.edu), two dice per pair (or the tutor’s dice program), a coin, coloured counters and a paper bag, mini whiteboards, tally sheet.',
    online: 'Children roll real dice at home; anyone without dice builds the dice program live in the shared Scratch window (pick random 1 to 6, twice) and uses that. This lesson is enrichment: probability is new to most children, so keep it playful. Block colours on our slides are simplified; in Scratch, find blocks by the category name on the left, not by colour. Pairs play the Explore game in breakout rooms and type their tallies into the chat so the group total can be added up.',
    warmup: 'Where on the line? Six events (roll a 7, flip heads, roll less than 5, pick a vowel from SINGAPORE, roll 1 to 6, pick the 1 red card from 10). Teams place each on a 0 to 1 probability line and give the fraction.',
    explore: 'The Dice Race: roll two dice and add. Player A wins on 2, 3, 4, 10, 11 or 12; player B wins on 5, 6, 7, 8 or 9. Pairs predict, play 20 rounds, tally the wins, then add up the whole group’s results.',
    mini: 'Probability = number of ways it can happen ÷ number of equally likely outcomes, written as a fraction. Two dice give 6 × 6 = 36 equally likely outcomes (a nested loop!). A game is fair when every player has the same probability of winning. Expected number = probability × number of tries; a simulation lands close to this, but not exactly, because each run is random.',
    share: 'Mei flipped a coin 10 times and got 7 heads. She says the coin is unfair. Do you agree? How could you test it?',
    exit: { q: 'Roll two dice and add. What is the probability that the total is 8? If you roll them 360 times, about how many 8s do you expect?', a: '5/36 (2+6, 3+5, 4+4, 5+3, 6+2); about 50 (5/36 × 360 = 50).' },
    mistakes: ['Treating outcomes as equally likely when they are not (two coins: “two heads, two tails, one of each” as thirds; dice totals 2 to 12 as elevenths).', 'Thinking a random result should come out exactly as expected, or that a coin “is due” a head after several tails.', 'Not simplifying, or writing the number of ways instead of the fraction (6 instead of 6/36 = 1/6).'],
    extension: 'Change the Dice Race so that it is fair, using totals only (a total of 7 may mean “roll again”). Test your rules in code with 1000 games. How close to 500 : 500 do you get?',
    key: [
      ['Q1', '(a) 3/8  (b) 6/8 = 3/4  (c) about 375 (3/8 × 1000)  (d) No. Each spin is random, so the count wobbles around 375; 362 is close. About 19 runs in 20 land between 345 and 405.'],
      ['Q2', '(a) about 500 (1/2 × 1000)  (b) No. The flips are random, so each run gives a slightly different count near 500. Exactly 500 happens only about 1 run in 40.  (c) about 200 (1/5 × 1000)'],
      ['Q3', '(a) 4/10 = 2/5  (b) 2 red (6 red, 6 blue: 6/12 = 1/2)  (c) 10 blue (4 red out of 20: 4/20 = 1/5)'],
      ['Q4', '(a) Differences: 0 appears 6 times, 1: 10, 2: 8, 3: 6, 4: 4, 5: 2 (36 in all).  (b) Ali 24/36 = 2/3, Ben 12/36 = 1/3  (c) Not fair: Ali is twice as likely to win, even though each has 3 differences.  (d) Any split with 18 outcomes each, e.g. Ali on 1, 3, 5 (odd) and Ben on 0, 2, 4 (even); or Ali on 1, 2 and Ben on 0, 3, 4, 5; or Ali on 0, 1, 5 and Ben on 2, 3, 4.'],
      ['Q5', 'Gaps: 6, 6, a = b.  (a) About 167: P(double) = 6/36 = 1/6, and 1/6 × 1000 = 166 2/3.  (b) A count must be a whole number, and each run is random, so it lands near 167 (about 19 runs in 20 between 145 and 190), not exactly on it.']
    ]
  },

  script: {
    hook: ['Welcome, inquirers! Today we play games and then ask the big question: is this game fair? Our feelings are not enough. We will count outcomes with fractions, and then make the computer play a game a thousand times to test our maths.'],
    warmIntro: ['Here is a line from 0 to 1. 0 means impossible, 1 means certain, 1/2 means an even chance.', 'For each card, decide where it goes on the line and give its fraction. Teams, you have 20 seconds per card.'],
    predict: ['In the Dice Race, player A wins on six totals: 2, 3, 4, 10, 11, 12. Player B wins on only five: 5, 6, 7, 8, 9. Who do you think will win more often? Write A, B or “same”, and a reason.'],
    exploreHints: ['Keep a tally: one column for A, one for B. Write the total each time.', 'Surprised by your results? Write down which totals came up most.', 'Finished early: in how many ways can two dice make a total of 7? Of 2? Use a red die and a blue die so 1 + 6 and 6 + 1 are different.'],
    think: ['“Roll one dice. More than 4 means 5 or 6: that is 2 ways out of 6 equally likely outcomes. So the probability is 2/6, which is 1/3.”', '“Two dice. The red die has 6 outcomes and for each one the blue die has 6, so 6 × 6 = 36, just like last lesson’s nested loop. A total of 7 happens 6 times: 1 + 6, 2 + 5, 3 + 4, 4 + 3, 5 + 2, 6 + 1. So P(7) = 6/36 = 1/6. A total of 2 happens once: 1/36.”', '“In 1000 games I expect B to win about 2/3 × 1000, which is 666 2/3. A count cannot be 666 2/3, and every run is random, so the program will say something close, like 670 or 649, but almost never exactly 667.”'],
    circulate: ['Ask: “What are the equally likely outcomes here? How many are there?”', 'Ask: “What fraction do you expect? So about how many out of 1000?”', 'Ask: “Your program said 158, not 167. Is it broken? How could you check?” (run it again; run 10 000 games and look at the fraction)'],
    hints: ['Hint 1: “List every outcome. Are they all equally likely?”', 'Hint 2: “For two dice, draw the 6 by 6 table.”', 'Hint 3: “Expected number = probability × number of tries.”'],
    talk: ['“Mei flipped a coin 10 times and got 7 heads. She says the coin is unfair. Do you agree?”', '“How many flips would you need before you believed her? How could a program help?”'],
    talkAns: 'Not yet: 10 flips is far too few. With a fair coin, 7 or more heads in 10 flips happens 176 times in 1024, about 1 time in 6. To test it, flip many more times (or simulate 1000 flips of a fair coin to see how much the counts wobble). If 1000 real flips gave 700 heads, that would be strong evidence: a fair coin almost never does that.',
    close: ['“Today you measured chance with fractions, found the hidden unfairness in a game, and let the computer play a thousand games to test your maths. Close, not exact: that is how random things behave.”']
  },

  deck: {
    today: 'Measure chance with fractions, decide if a game is fair, and test it by running the game 1000 times in code.',
    warmGame: 'Where on the line? Teams place six events on a 0 to 1 probability line and give each one’s fraction: roll a 7, flip heads, roll less than 5, pick a vowel from SINGAPORE, roll 1 to 6, pick the 1 red card from 10.',
    warmQs: [['Simplify 6/36', '1/6'], ['1/6 of 600', '100'], ['2/5 of 1000', '400'], ['Which is bigger: 5/12 or 4/9?', '4/9 (16/36 is more than 15/36)'], ['1 − 3/10', '7/10']],
    expSetup: ['Roll two dice and add. A wins on 2, 3, 4, 10, 11 or 12. B wins on 5, 6, 7, 8 or 9.', 'Predict: who will win more often? A has 6 totals, B has only 5.', 'Play 20 rounds with your partner. Tally the wins.', 'Add up the whole group’s results. What do you notice?'],
    expPic: 'two dice showing 3 and 5, an A box with the totals 2, 3, 4, 10, 11, 12 and a B box with the totals 5, 6, 7, 8, 9, next to a tally chart.',
    expAsk: [['Who won more often in your pair? In the whole group?', 'Usually B. The group total is closer to B winning about 2 rounds in every 3.'], ['A has more totals. Why does B win more often?', 'The totals are not equally likely: 7 can be made in 6 ways, 2 in only 1 way. B’s totals can be made in 24 of the 36 ways.'], ['How could we be sure without playing forever?', 'List all 36 equally likely outcomes, or let a computer play 1000 games.']],
    mini1: { head: 'A spinner with 6 equal parts: 3 blue, 2 yellow, 1 red', body: ['6 equal parts, so 6 equally likely outcomes.', 'Yellow: 2 parts out of 6.', 'Spin 600 times: expect 1/3 of 600.'], ans: 'P(yellow) = 2/6 = 1/3; about 200 yellows in 600 spins (not exactly).' },
    mini2: { head: 'Two dice: the 36 outcomes', body: ['6 outcomes for the red die × 6 for the blue = 36.', 'Total 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.', 'Explore game: A’s totals happen 12 ways, B’s 24 ways.'], ans: 'P(7) = 6/36 = 1/6. P(A wins) = 12/36 = 1/3, P(B wins) = 24/36 = 2/3: not fair.' },
    keyHead: 'Key idea: count the equally likely outcomes',
    keyBig: 'Probability = ways it can happen ÷ equally likely outcomes. A game is fair when every player has the same probability of winning.',
    keySmall: 'Expected number = probability × tries. 1000 random games land close to it, but not exactly.',
    brk: 'Human dice. The tutor rolls a dice: 1 or 2, five star jumps; 3 or 4, touch your toes five times; 5 or 6, spin round once. Which will we do most? (Each has the same chance: 2/6 = 1/3.)',
    ws1: 'Page 1, in pairs: Q1 the spinner, Q2 predict the coin program, Q3 change the bag.',
    ws2: 'Page 2, on your own: Q4 the Difference Game (and the Python corner), Q5 plan the doubles program.'
  },

  qbank: {
    core: [
      { q: 'Roll a dice. Write down every possible result. How many of them are even? So the chance of an even number is __ out of __. Write it as a fraction.', a: '3 out of 6 = 1/2 (2, 4 or 6)' },
      { q: 'A bag has 3 red and 7 yellow counters. You pick one without looking. How many counters are there altogether? What is the chance (as a fraction) that you pick yellow?', a: '10 counters; 7/10' },
      { q: 'You flip a coin 200 times. About how many heads do you expect? Will it be exactly that number?', a: 'About 100 (half of 200), but probably not exactly 100' },
      { q: 'A spinner has 4 equal parts: red, red, blue, green. Write the chance of spinning red as a fraction.', a: '2/4 = 1/2' },
      { q: 'Roll a normal dice. Can you roll a 9? Choose one: impossible, unlikely, likely or certain.', a: 'Impossible: the probability is 0 (a dice only shows 1 to 6)' },
      { q: 'A game: you win if the dice shows 1 or 2; your friend wins if it shows 3, 4, 5 or 6. Write the six dice results and who wins each one. Is the game fair? Why or why not?', a: 'You win on 2 of the 6 results and your friend on 4 of the 6, so it is not fair (2/6 = 1/3 against 4/6 = 2/3).' }
    ],
    stretch: [
      { q: 'A spinner has 10 equal parts numbered 1 to 10. What is the probability of spinning a prime number?', a: '4/10 = 2/5 (2, 3, 5, 7)' },
      { q: 'Roll two dice and add. What is the probability that the total is 9?', a: '4/36 = 1/9 (3+6, 4+5, 5+4, 6+3)' },
      { q: 'A bag has 5 red counters and some blue counters. The probability of picking red is 1/4. How many blue counters are there?', a: '15 (5 out of 20 is 1/4)' },
      { q: 'Ali flips a coin 3 times. What is the probability that he gets heads all 3 times?', a: '1/8 (8 equally likely outcomes: HHH, HHT, HTH, HTT, THH, THT, TTH, TTT)' },
      { q: 'One letter is picked at random from the word MATHEMATICS. What is the probability that it is M?', a: '2/11' },
      { q: 'A program rolls a dice 1200 times and counts the numbers bigger than 4. About how many should it count? The program says 391. Is something wrong? Explain.', a: 'About 400 (2 of the 6 results are bigger than 4, and 1/3 × 1200 = 400). 391 is close, so nothing is wrong: a random simulation is never exactly the expected number.' },
      { q: 'Roll two dice. What is the probability that at least one of them shows a 6?', a: '11/36 (6 with the red die, 6 with the blue die, minus the 6 + 6 counted twice: 6 + 6 − 1 = 11)' },
      { q: 'Roll a dice. Ali wins on 1 or 2; Ben wins on 3, 4, 5 or 6. Ben scores 1 point for each win. How many points should Ali score for each win to make the game fair?', a: '2 points (Ali wins 1/3 of the time and Ben 2/3, so Ali needs twice as many points per win)' }
    ],
    challenge: [
      { q: 'Three coins are flipped. What is the probability of getting exactly 2 heads?', a: '3/8 (HHT, HTH, THH out of 8 outcomes)' },
      { q: 'A number from 1 to 30 is picked at random. What is the probability that it is a multiple of 3 or a multiple of 5?', a: '14/30 = 7/15 (10 multiples of 3, 6 of 5, and 15 and 30 are counted twice: 10 + 6 − 2 = 14)' },
      { q: 'Roll two dice and multiply the numbers. What is the probability that the answer is odd?', a: '9/36 = 1/4 (both dice must be odd: 3 × 3 = 9 ways)' },
      { q: 'A spinner is spun 1000 times in a program and lands on red 248 times. Is red most likely 1/2, 1/4 or 1/8 of the spinner? Explain.', a: '1/4: we would expect about 250 reds, and 248 is close. 1/2 would give about 500 and 1/8 about 125.' },
      { q: 'A bag has 4 red and 6 blue counters. Ali picks a red counter and keeps it. What is the probability that the next counter picked is red?', a: '3/9 = 1/3 (3 red left out of 9)' },
      { q: 'Ben says: “When you flip two coins you get two heads, two tails, or one of each, so the chance of one of each is 1/3.” Is he right?', a: 'No: HH, HT, TH, TT are the 4 equally likely outcomes, and one of each happens 2 ways: 2/4 = 1/2.' },
      { q: 'Design a FAIR game for two players using one dice, two coins or a spinner. Write the rules and show with a list or table that each player has the same chance of winning. Then change ONE rule to make the game unfair, and say who is favoured.', a: 'Open. Example: roll one dice; Player A wins on 1, 2 or 3 and Player B wins on 4, 5 or 6 (3/6 each). Change: A also wins on 4. Now A has 4/6 and B has 2/6, so A is favoured. Check that every outcome is listed and the winning outcomes add up to the whole.' },
      { q: 'Mei and Ali each roll one dice. Mei wins if her number is bigger. Ali wins if his number is bigger or the same. Is the game fair? What is the probability that Mei wins?', a: 'Not fair. Mei wins 15/36 = 5/12; Ali wins 21/36 = 7/12 (15 bigger + 6 the same). Fair version: the same number means roll again.' },
      { q: 'Spinner A has 3 equal parts: 1, 2, 3. Spinner B has 4 equal parts: 1, 2, 3, 4. Spin both and multiply. Even wins if the answer is even, Odd wins if it is odd. Is the game fair?', a: 'Not fair. There are 3 × 4 = 12 outcomes; the answer is odd only when both are odd: 2 × 2 = 4 ways. P(Odd) = 4/12 = 1/3, P(Even) = 8/12 = 2/3.' }
    ]
  },

  workbook: H => {
    const tx = h => '<div style="text-align:left;font-size:16px;line-height:1.5">' + h + '</div>';
    const L = t => '<b style="color:#1F7A6F">' + t + '</b> ';
    const blank = w => '<span style="display:inline-block;width:' + w + 'px;border-bottom:2px dotted #8A94AD"></span>';
    const dw = [1500, 1400, 1400, 1400, 1400, 1400, 1400];
    const diff = H.tbl(dw, [H.row(['Difference', '1', '2', '3', '4', '5', '6'].map((s, i) => H.cell(s, dw[i], { bold: true, fill: 'D9D9D9', h: 34 }))),
      ...[1, 2, 3, 4, 5, 6].map(r => H.row([H.cell(String(r), dw[0], { bold: true, fill: 'D9D9D9', h: 34 }), ...[1, 2, 3, 4, 5, 6].map(c => H.cell(r === 1 || r === c ? String(Math.abs(r - c)) : '', dw[c], { h: 34 }))]))]);
    const py = pyBox(['import random', 'a_wins = 0', 'b_wins = 0', 'for game in range(1000):', '    d1 = random.randint(1, 6)', '    d2 = random.randint(1, 6)', '    if 5 <= d1 + d2 <= 9:', '        b_wins = b_wins + 1', '    else:', '        a_wins = a_wins + 1', 'print(a_wins, b_wins)'], 'Python corner (optional): the Explore|game. Change it to test Q4.', 320);
    return [
      H.q(1, 'Ben’s spinner has 8 equal parts: 3 red (R), 2 blue (B), 2 yellow (Y) and 1 green (G). Write each probability as a fraction in its simplest form.', { before: 20, keepNext: true }),
      H.tbl([3000, 6900], [H.row([H.cell('<div>' + spinner() + '</div>', 3000, { h: 20 }), H.cell(tx(L('(a)') + 'P(red) = ' + blank(70) + '      ' + L('(b)') + 'P(not yellow) = ' + blank(70) + '<br>' + L('(c)') + 'Ben makes the spinner in code and spins it 1000 times. About how many reds do you expect? ' + blank(70) + '<br>' + L('(d)') + 'His program says 362 reds. Ben says, “My program is wrong!” Do you agree? Explain.<br>' + blank(430) + '<br>' + blank(430)), 6900, { h: 30 })])]),
      H.q(2, 'Predict what this code does. “pick random 1 to 2” gives 1 or 2, each with probability 1/2.', { keepNext: true }),
      H.tbl([4900, 5000], [H.row([H.cell('<div style="text-align:left">' + blocks(coinCode, 'Code: set heads to 0, repeat 1000 times: if pick random 1 to 2 equals 1 then change heads by 1; then say heads', 14) + '</div>', 4900, { h: 40 }), H.cell(tx(L('(a)') + 'About what number will it say? ' + blank(70) + '<br>' + L('(b)') + 'Mei runs it 3 times and gets 513, 489 and 502. Is her code broken? Explain.<br>' + blank(330) + '<br>' + L('(c)') + 'If “pick random 1 to 2” is changed to “pick random 1 to 5”, about what will it say? ' + blank(70)), 5000, { h: 30 })])]),
      H.q(3, 'A bag has 4 red and 6 blue counters. You pick one without looking.', { keepNext: true }),
      H.sub('a', 'What is the probability of picking red?   ________'),
      H.sub('b', 'How many red counters must be added so that P(red) = 1/2?   ________'),
      H.sub('c', 'Start again with 4 red and 6 blue. How many blue counters must be added so that P(red) = 1/5?   ________'),

      H.q(4, 'The Difference Game. Roll two dice. The difference is the bigger number minus the smaller (0 if they are the same). Ali wins on 0, 1 or 2. Ben wins on 3, 4 or 5.', { pb: true, before: 0, keepNext: true }),
      H.tbl([5200, 4700], [H.row([H.cell('<div>' + diff + '</div>', 5200, { h: 20 }), H.cell('<div>' + py + '</div>', 4700, { h: 20 })])]),
      H.sub('a', 'Complete the table.     (b)  P(Ali wins) = ________      P(Ben wins) = ________'),
      H.sub('c', 'Is the game fair? Explain.   ' + '_'.repeat(40)),
      H.sub('d', 'Change who wins on which differences so that the game is fair.', { keepNext: true }), ...H.lines(1),
      H.q(5, 'Plan your code. Fill the 3 gaps to count doubles in 1000 rolls of two dice.', { keepNext: true }),
      H.tbl([5000, 4900], [H.row([H.cell('<div style="text-align:left">' + blocks(planCode, 'Plan with gaps: set doubles to 0, repeat 1000 times: set a to pick random 1 to a gap, set b to pick random 1 to a gap, if a gap then change doubles by 1; then say doubles', 14) + '</div>', 5000, { h: 30 }),
        H.cell(tx(L('(a)') + 'About what number will it say? Show your fraction.<br>' + blank(250) + '<br><br>' + L('(b)') + 'Why will it not say exactly 1000 × 1/6?<br>' + blank(300) + '<br>' + blank(300)), 4900, { h: 30 })])])
    ];
  }
};
