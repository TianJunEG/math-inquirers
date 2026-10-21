// Math Inquirers P2, Lesson 7: Fair Shares (fractions)
// Every shaded drawing is built from EQUAL parts (equal bar widths, equal pie angles) unless the question is about unequal parts.

const N = '#1B2A49', Y = '#FFC93C', SK = '#DDEBF7', TL = '#1F7A6F', W = '#FFFFFF';
const FONT = 'Fredoka, Arial, sans-serif';

// ---------- text with stacked fractions: '{3/8}' ----------
const FR = (a, b) => `<span style="display:inline-flex;flex-direction:column;align-items:center;vertical-align:middle;line-height:1;margin:0 3px;font-size:.95em"><span style="padding:0 3px 2px;border-bottom:2px solid currentColor">${a}</span><span style="padding:2px 3px 0">${b}</span></span>`;
const rich = (H, s, o = {}) => {
  if (!H.TextRun || !H.t) return s.replace(/\{(\d+)\/(\d+)\}/g, '$1/$2');
  const out = []; const re = /\{(\d+)\/(\d+)\}/g; let m, last = 0;
  while ((m = re.exec(s))) { if (m.index > last) out.push(H.t(s.slice(last, m.index), o)); out.push(new H.TextRun(FR(m[1], m[2]))); last = re.lastIndex; }
  if (last < s.length) out.push(H.t(s.slice(last), o));
  return out;
};

// ---------- SVG helpers (viewBox width 600) ----------
const svg = (w, h, body, label) => `<svg viewBox="0 0 ${w} ${h}" width="${w}" height="${h}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="${label}" style="max-width:100%;height:auto">${body}</svg>`;
const f1 = v => (Math.round(v * 10) / 10).toString();
const rect = (x, y, w, h, fill = W, sw = 2.5) => `<rect x="${f1(x)}" y="${f1(y)}" width="${f1(w)}" height="${f1(h)}" fill="${fill}" stroke="${N}" stroke-width="${sw}"/>`;
const line = (x1, y1, x2, y2, sw = 2.5) => `<line x1="${f1(x1)}" y1="${f1(y1)}" x2="${f1(x2)}" y2="${f1(y2)}" stroke="${N}" stroke-width="${sw}" stroke-linecap="round"/>`;
const poly = (pts, fill = W) => `<polygon points="${pts.map(p => f1(p[0]) + ',' + f1(p[1])).join(' ')}" fill="${fill}" stroke="${N}" stroke-width="2.5" stroke-linejoin="round"/>`;
const text = (x, y, s, size = 18, fill = N, anchor = 'middle', weight = 700) => `<text x="${f1(x)}" y="${f1(y)}" font-size="${size}" font-weight="${weight}" text-anchor="${anchor}" fill="${fill}" font-family="${FONT}">${s}</text>`;
const sfr = (x, yc, a, b, size = 18) => { const w = size * 0.62 * Math.max(String(a).length, String(b).length) + 6; return text(x, yc - size * 0.2, a, size) + line(x - w / 2, yc, x + w / 2, yc, 2) + text(x, yc + size * 0.88, b, size); };
// a bar of n EQUAL parts; shade = indices
const bar = (x, y, w, h, n, shade = [], fill = Y) => { let s = ''; for (let i = 0; i < n; i++) s += rect(x + i * w / n, y, w / n, h, shade.includes(i) ? fill : W); return s; };
// a circle cut into n EQUAL sectors (360/n degrees each), starting at the top
const pt = (cx, cy, r, a) => [cx + r * Math.cos((a - 90) * Math.PI / 180), cy + r * Math.sin((a - 90) * Math.PI / 180)];
const sector = (cx, cy, r, a0, a1, fill) => { const [x0, y0] = pt(cx, cy, r, a0), [x1, y1] = pt(cx, cy, r, a1); return `<path d="M${cx} ${cy} L${f1(x0)} ${f1(y0)} A${r} ${r} 0 ${a1 - a0 > 180 ? 1 : 0} 1 ${f1(x1)} ${f1(y1)} Z" fill="${fill}" stroke="${N}" stroke-width="2.5" stroke-linejoin="round"/>`; };
const pie = (cx, cy, r, n, shade = []) => { let s = ''; for (let i = 0; i < n; i++) s += sector(cx, cy, r, 360 * i / n, 360 * (i + 1) / n, shade.includes(i) ? Y : W); return s; };

// Q1: six shapes, each cut into 4 parts with 1 part shaded. A, C, E, F are quarters; B and D are not.
const q1svg = () => {
  let s = '';
  // A: square, 4 equal strips (20 wide each)
  s += rect(10, 20, 80, 80) + rect(30, 20, 20, 80, Y) + line(70, 20, 70, 100) + line(30, 20, 30, 100) + line(50, 20, 50, 100);
  // B: circle r 42 at (150,60); cuts at x = 135 and y = 75 (not through the centre)
  const r = 42, cx = 150, cy = 60, a = 15, h = Math.sqrt(r * r - a * a);
  s += `<circle cx="${cx}" cy="${cy}" r="${r}" fill="${W}" stroke="${N}" stroke-width="2.5"/>`;
  s += `<path d="M${cx - a} ${cy + a} L${cx - a} ${f1(cy - h)} A${r} ${r} 0 0 1 ${f1(cx + h)} ${cy + a} Z" fill="${Y}" stroke="${N}" stroke-width="2.5"/>`;
  s += line(cx - a, cy - h, cx - a, cy + h) + line(cx - h, cy + a, cx + h, cy + a);
  // C: rectangle 90 by 60, cut through the middle both ways
  s += rect(205, 30, 90, 60) + rect(205, 30, 45, 30, Y) + line(250, 30, 250, 90) + line(205, 60, 295, 60);
  // D: rectangle 90 by 60 cut into strips 12, 20, 26, 32 wide
  s += rect(305, 30, 90, 60) + rect(363, 30, 32, 60, Y) + line(317, 30, 317, 90) + line(337, 30, 337, 90);
  // E: square with both lines corner to corner (4 same triangles)
  s += rect(410, 20, 80, 80) + poly([[410, 20], [410, 100], [450, 60]], Y) + line(410, 20, 490, 100) + line(490, 20, 410, 100);
  // F: triangle with the middles of its sides joined (4 same triangles); the middle one is shaded
  const ap = [550, 100 - 40 * Math.sqrt(3)], bl = [510, 100], br = [590, 100], ml = [530, (ap[1] + 100) / 2], mr = [570, (ap[1] + 100) / 2], mb = [550, 100];
  s += poly([ap, bl, br]) + poly([ml, mr, mb], Y);
  ['A', 'B', 'C', 'D', 'E', 'F'].forEach((l, i) => { s += text(50 + i * 100, 136, l, 20); });
  return `<div style="width:520px;margin:0 auto">` + svg(600, 142, s, 'Six shapes A to F, each cut into 4 parts with 1 part shaded') + '</div>';
};
// Q2: a) 3 of 8, b) 5 of 6, c) 7 of 10, with answer boxes under each picture
const q2svg = () => {
  let s = text(12, 24, 'a', 20, N, 'start') + bar(30, 42, 170, 40, 8, [0, 3, 5]);
  s += text(232, 24, 'b', 20, N, 'start') + pie(300, 62, 50, 6, [0, 1, 3, 4, 5]);
  s += text(402, 24, 'c', 20, N, 'start');
  const on = ['0,0', '0,1', '0,3', '0,4', '1,1', '1,2', '1,4'];
  for (let r = 0; r < 2; r++) for (let c = 0; c < 5; c++) s += rect(420 + c * 32, 30 + r * 32, 32, 32, on.includes(r + ',' + c) ? Y : W);
  [115, 300, 505].forEach(cx => {
    s += text(cx - 42, 136, 'shaded', 14, N, 'middle', 600) + text(cx + 42, 136, 'not shaded', 14, N, 'middle', 600);
    s += `<rect x="${cx - 70}" y="142" width="56" height="44" rx="6" fill="none" stroke="${N}" stroke-width="2" stroke-dasharray="4 3"/><rect x="${cx + 14}" y="142" width="56" height="44" rx="6" fill="none" stroke="${N}" stroke-width="2" stroke-dasharray="4 3"/>`;
  });
  return svg(600, 190, s, 'a: a bar of 8 equal parts with 3 shaded; b: a circle of 6 equal parts with 5 shaded; c: a grid of 10 equal squares with 7 shaded; under each, a box for the shaded fraction and a box for the not-shaded fraction');
};
// Q4: bars to colour + the sums
const q4svg = () => {
  const rows = [['a', 5, [[2, 5], '+', [1, 5], '=']], ['b', 8, [[3, 8], '+', [4, 8], '=']], ['c', 12, [[4, 12], '+', [5, 12], '=']], ['d', 6, [[1, 6], '+', 'box', '=', '1 whole']], ['e', 10, [[7, 10], '−', [3, 10], '=']]];
  let s = '';
  rows.forEach(([l, n, parts], k) => {
    const y = 8 + k * 58;
    s += text(12, y + 27, l, 20, N, 'start') + bar(34, y + 4, 300, 34, n);
    let x = 372;
    parts.forEach(pp => {
      if (Array.isArray(pp)) { s += sfr(x, y + 21, pp[0], pp[1], 18); x += 36; }
      else if (pp === 'box') { s += `<rect x="${x - 16}" y="${y - 2}" width="34" height="46" rx="5" fill="none" stroke="${N}" stroke-width="2" stroke-dasharray="4 3"/>`; x += 36; }
      else if (pp === '1 whole') { s += text(x + 18, y + 27, '1 whole', 18, N, 'middle'); x += 60; }
      else { s += text(x - 2, y + 28, pp, 20); x += 32; }
    });
    if (l !== 'd') s += `<rect x="${x - 16}" y="${y - 2}" width="40" height="46" rx="5" fill="none" stroke="${N}" stroke-width="2" stroke-dasharray="4 3"/>`;
  });
  return svg(600, 296, s, 'Five bars to colour: 5, 8, 12, 6 and 10 equal parts, each next to a sum with a box for the answer');
};
const q5svg = () => svg(600, 62, text(10, 38, 'Cake', 18, N, 'start') + bar(70, 12, 480, 40, 8), 'A bar of 8 equal parts for the cake');
const q6svg = () => svg(600, 120, text(70, 42, 'Ravi', 18, N, 'end') + bar(85, 15, 480, 40, 4) + text(70, 102, 'Siti', 18, N, 'end') + bar(85, 75, 480, 40, 8), 'Two bars the same length: Ravi\'s pizza in 4 equal parts and Siti\'s pizza in 8 equal parts');

module.exports = {
  lesson: {
    n: 7, week: 4, session: 'A', title: 'Fair Shares', topic: 'Fractions',
    objective: 'Recognise equal parts and name fractions with bottom numbers up to 12; compare unit fractions and like fractions; add and take away like fractions within one whole; solve fair-sharing stories with a bar.',
    skills: 'Checking for equal parts, comparing with the same whole, drawing bars, explaining',
    materials: 'Paper strips of the same length (4 per child), paper squares, scissors, crayons, mini whiteboards.',
    online: 'Each child folds paper strips on camera; the tutor shows fraction bars on the slides and children colour their own bars.',
    warmup: 'Fair or not fair? Six snacks are cut into parts. Thumbs up if all the parts are the same size, thumbs down if not, and say why.',
    explore: 'Fold paper strips into halves, quarters and eighths, write the fraction on each part, line the strips up and compare. Then try to fold a strip into 3 equal parts.',
    mini: 'Equal parts come before fraction names; name the shaded and the not-shaded fraction (bottom number: how many equal parts, top number: how many we take); compare unit fractions with bars of the same length (more parts, smaller parts) and like fractions (count the parts). Before page 2: add like fractions on a bar, fair-sharing stories with a bar, line up halves and eighths of the same whole.',
    share: 'Is 1/2 always bigger than 1/4? When could it not be?',
    exit: { q: 'Which is bigger, 1/7 or 1/9? Then work out 2/9 + 5/9.', a: '1/7 (the same whole cut into fewer parts gives bigger parts). 2/9 + 5/9 = 7/9.' },
    mistakes: [
      'Naming a fraction when the parts are not equal: circling B or D in Q1.',
      'Thinking 1/6 is bigger than 1/4 because 6 is bigger than 4 (Q3).',
      'Adding the bottom numbers too: 2/5 + 1/5 written as 3/10 instead of 3/5 (Q4).'
    ],
    extension: 'Find all the ways to add two fractions with bottom number 8 to make 1 whole (1/8 + 7/8, 2/8 + 6/8, 3/8 + 5/8, 4/8 + 4/8: 4 ways).',
    key: [
      ['Q1', 'A, C, E and F are cut into quarters. (a) B or D: their 4 parts are not the same size, so a part is not a quarter.'],
      ['Q2', '(a) shaded 3/8, not shaded 5/8  (b) 5/6 and 1/6  (c) 7/10 and 3/10'],
      ['Q3', '(a) 1/3; 7/9  (b) 1/10, 1/5, 1/4, 1/2  (c) No. Cutting the same whole into 6 equal parts makes smaller parts than cutting it into 4, so 1/6 is smaller than 1/4.'],
      ['Q4', '(a) 3/5  (b) 7/8  (c) 9/12  (d) 5/6  (e) 4/10'],
      ['Q5', '(a) 5/8  (b) 3/8  (c) Mei, by 1/8'],
      ['Q6', 'Siti. The pizzas are the same size and 1 quarter is the same as 2 eighths; 3 eighths is more than 2 eighths.']
    ]
  },

  script: {
    hook: ['Good morning, inquirers! Today we are cake cutters and pizza sharers. There is one rule: every share must be FAIR.', 'By the end you will name fair shares with fractions, tell which share is bigger, and explain how you know.'],
    warmIntro: ['Look at each snack. Ali and Mei want to share it. Is it fair? Thumbs up for fair, thumbs down for not fair.', 'Be ready to tell me why.'],
    predict: ['Before we fold: which will be bigger, one quarter of a strip or one eighth of the same strip? Show me 4 fingers for a quarter or 8 fingers for an eighth.'],
    exploreHints: ['Stuck folding: match the two ends exactly, then press the fold flat.', 'Not sure what to write: “How many equal parts are there? That number goes at the bottom.”', 'Finished early: can you fold a strip into 3 equal parts? How do you check they are equal?'],
    think: [
      '“Before I name a fraction I check the parts are equal. This bar has 5 parts, all the same size, so the parts are fifths: 5 goes at the bottom. 3 parts are shaded: 3 goes on top. Three fifths.”',
      '“One half or one sixth: which is bigger? Same whole. One half is 1 of 2 parts, one sixth is 1 of 6 parts. More parts means smaller parts, so one half is bigger.”',
      '“Two ninths and four ninths: ninths are the name of the parts, like apples. 2 ninths and 4 ninths are 6 ninths. The parts do not change size, so the bottom number stays 9.”'
    ],
    circulate: ['Ask: “Are all the parts the same size? How do you know?”', 'Ask: “What does the bottom number tell us? What does the top number tell us?”', 'Ask: “Did you draw both wholes the same length?”'],
    hints: ['Hint 1: “Count all the equal parts first. That number goes at the bottom.”', 'Hint 2: “Fold or draw a strip to check which part is bigger.”', 'Hint 3: “Colour the parts on a bar, then count them.”'],
    talk: ['“Is 1/2 always bigger than 1/4? Can you think of a time when it is not?”', '“Why does the bottom number stay the same when we add 2/9 and 4/9?”'],
    talkAns: 'Only when the wholes are the same size: half a small cupcake is less than a quarter of a big cake. When we add ninths, the parts are still ninths, so only the number of parts changes.',
    close: ['“You checked for equal parts, compared fractions with bars and explained why. That is fair and careful maths.”']
  },

  deck: {
    today: 'Cut wholes into equal parts, name and compare fractions, and add fractions to share things fairly.',
    warmGame: 'Fair or not fair? Six snacks are cut into parts: thumbs up if all the parts are the same size, thumbs down if not.',
    warmQs: [['A pizza is cut into 4 equal slices. What is 1 slice called?', 'One quarter, 1/4'], ['How many halves make 1 whole?', '2'], ['How many thirds make 1 whole?', '3'], ['A cake is cut into 5 equal pieces. What is 1 piece called?', 'One fifth, 1/5'], ['2 of 7 equal parts are shaded. What fraction is shaded?', '2/7']],
    expSetup: ['Take 4 paper strips that are the same length.', 'Keep one whole. Fold one in half, one into quarters and one into eighths.', 'Open them out. Write the fraction on every part.', 'Line them up. Then try to fold a strip into 3 equal parts.'],
    expPic: 'four paper strips the same length: one whole, one folded into halves, one into quarters and one into eighths, with 1/2, 1/4 or 1/8 written on every part.',
    expAsk: [['Which part is bigger, 1/4 or 1/8? How do you know?', '1/4: the same strip cut into fewer parts, so each part is longer.'], ['How many eighths fit on one quarter? How many quarters make 1 whole?', '2 eighths; 4 quarters.'], ['How did you fold 3 equal parts? How do you know they are equal?', 'Fold and adjust until the parts match; check by laying one part on another.']],
    mini1: { head: 'Name the fraction', body: ['A bar has 5 equal parts and 3 are shaded.', 'Check the parts are equal, count all the parts (bottom number), then count the shaded parts (top number).', 'What fraction is shaded? What fraction is not?'], ans: '3/5 shaded, 2/5 not shaded; together 5/5, 1 whole.' },
    mini2: { head: 'Compare with bars', body: ['Bars of the same length cut into halves, thirds and sixths, one part shaded in each.', 'Which is bigger: 1/2, 1/3 or 1/6?', 'Then: which is bigger, 2/7 or 5/7?'], ans: '1/6 < 1/3 < 1/2 (more equal parts, smaller parts). 5/7 > 2/7 (same-size parts, more of them).' },
    keyHead: 'Key idea: equal parts',
    keyBig: 'A fraction names equal parts of a whole: the bottom number is how many equal parts, the top number is how many we take.',
    keySmall: 'Same whole: more equal parts means smaller parts.',
    brk: 'Fraction turns. Stand up and turn a whole turn, a half turn, a quarter turn, three quarter turns, then freeze.',
    ws1: 'Page 1, in pairs: Q1 which shapes are cut into quarters, Q2 name the fraction shaded and not shaded, Q3 compare and order.',
    ws2: 'Page 2, on your own: Q4 add and take away, Q5 the cake story, Q6 who eats more pizza.'
  },

  qbank: {
    core: [
      { q: 'A cake is cut into 5 equal pieces. Ben eats 2 pieces. What fraction of the cake does he eat?', a: '2/5' },
      { q: 'How many quarters make 1 whole?', a: '4' },
      { q: 'Which is bigger, 1/3 or 1/6?', a: '1/3 (the same whole cut into 3 parts gives bigger parts than cut into 6)' },
      { q: '3/10 + 4/10 = ?', a: '7/10' },
      { q: 'Which is smaller, 5/8 or 3/8?', a: '3/8' },
      { q: 'A pizza is cut into 6 equal slices. 4 slices are eaten. What fraction of the pizza is left?', a: '2/6' }
    ],
    stretch: [
      { q: 'Write these in order, smallest first: 1/3, 1/12, 1/2, 1/5.', a: '1/12, 1/5, 1/3, 1/2' },
      { q: 'A ribbon is cut into 9 equal pieces. Mei uses 4 pieces and Siti uses 3 pieces. What fraction of the ribbon is left?', a: '2/9 (4 + 3 = 7 pieces used, 9 − 7 = 2 left)' },
      { q: '2/7 + ? = 1 whole', a: '5/7' },
      { q: 'Ali says: “Half of my pizza is bigger than half of your pizza.” Can he be right? Explain.', a: 'Yes, if his pizza is bigger. Halves of different-size wholes are different sizes.' },
      { q: 'Draw 3 squares. Cut each one into 4 EQUAL parts in a different way.', a: 'Any 3 of: 4 strips across, 4 strips down, a 2 by 2 grid, both lines from corner to corner (4 same triangles). Every part must be the same size.' },
      { q: 'Ravi eats 3/8 of a pizza. Ben eats 2/8 of the same pizza. How much more does Ravi eat? How much of the pizza is left?', a: '1/8 more; 3/8 is left (5 eighths eaten).' },
      { q: 'A strip is cut into 4 equal parts. Then each part is cut in half. How many parts are there now? What is each part called?', a: '8 parts; each part is one eighth (1/8). 2 eighths make 1 quarter.' },
      { q: 'Siti shades 4/12 of a shape. Then she shades 5/12 more. How much of the shape is NOT shaded?', a: '3/12 (9 twelfths shaded, 12 − 9 = 3)' }
    ],
    challenge: [
      { q: 'A chocolate bar has 10 equal pieces. Ali eats 1/10 of it. Mei eats 3 more pieces than Ali. What fraction of the bar is left?', a: '5/10 (Ali 1 piece, Mei 4 pieces: 5 eaten, 5 left)' },
      { q: 'I am a fraction with 1 on top. I am smaller than 1/4 but bigger than 1/7. What could I be? Find all the answers.', a: '1/5 and 1/6' },
      { q: 'Two fractions with bottom number 9 add up to 1 whole. One of them is 3/9 more than the other. What are they?', a: '6/9 and 3/9 (take away the extra 3 ninths: 6 left; share: 3 and 3; give the 3 back: 6 and 3)' },
      { q: 'How many different ways can you add two fractions with bottom number 6 to make 1 whole? Each fraction must be at least 1/6, and 1/6 + 5/6 and 5/6 + 1/6 count as the same way.', a: '3 ways: 1/6 + 5/6, 2/6 + 4/6, 3/6 + 3/6' },
      { q: 'Ali shades 1/3 of a strip of 6 equal squares. How many squares does he shade?', a: '2 squares (split the 6 squares into 3 equal groups of 2; one group is 1/3)' },
      { q: 'A pizza is cut into 8 equal slices. Ben eats 1/4 of the pizza. How many slices does he eat?', a: '2 slices (2 eighths make 1 quarter)' },
      { q: 'A cake is cut into 12 equal pieces. Mei gets 4/12. Ali and Ben share the rest, but Ali gets 2/12 more than Ben. What fraction does Ben get?', a: '3/12 (and Ali gets 5/12): 8 pieces are shared; take away Ali\'s extra 2, share 6 as 3 and 3.' },
      { q: 'A paper strip is folded in half, then in half again, then in half again. When you open it, how many equal parts are there? What fraction is each part?', a: '8 equal parts; each is 1/8 (1 fold: 2 parts, 2 folds: 4, 3 folds: 8).' },
      { q: 'Siti eats 1/2 of a pizza. Then Ravi eats 1/2 of what is left. What fraction of the whole pizza is left now?', a: '1/4. After Siti, half is left; Ravi eats half of that half, which is a quarter of the pizza, so a quarter is left.' }
    ]
  },

  workbook: H => {
    const R = (s, o) => rich(H, s, o);
    const out = [];
    out.push(H.q(1, R('Fair shares? Each shape has 4 parts and 1 part is shaded. Circle the shapes that are cut into quarters (4 EQUAL parts).'), { before: 40, keepNext: true }));
    out.push(H.fig(q1svg()));
    out.push(H.sub('a', 'Choose one shape that is NOT cut into quarters. Explain how you know.', { after: 20 }));
    out.push(...H.lines(1));
    out.push(H.q(2, 'What fraction is shaded? What fraction is NOT shaded? Write them in the boxes.', { keepNext: true }));
    out.push(H.fig(q2svg()));
    const sp = n => '\u00a0'.repeat(n);
    out.push(H.q(3, 'Compare the fractions. Draw bars the same length if it helps.', { keepNext: true }));
    out.push(H.sub('a', R('Circle the bigger fraction in each pair:' + sp(6) + '{1/3}' + sp(2) + 'or' + sp(2) + '{1/8}' + sp(12) + '{5/9}' + sp(2) + 'or' + sp(2) + '{7/9}')));
    out.push(H.sub('b', R('Smallest first:' + sp(3) + '{1/5}' + sp(2) + '{1/2}' + sp(2) + '{1/10}' + sp(2) + '{1/4}' + sp(6) + '_____' + sp(3) + '_____' + sp(3) + '_____' + sp(3) + '_____')));
    out.push(H.sub('c', R('Mei says: “{1/6} is bigger than {1/4}, because 6 is bigger than 4.” Is she right? Explain.'), { after: 20 }));
    out.push(...H.lines(1));

    out.push(H.q(4, 'Add or take away. Colour the bars to help you. Write each answer in the box.', { pb: true, before: 0, keepNext: true }));
    out.push(H.fig(q4svg()));
    out.push(H.q(5, 'Mum cuts a cake into 8 equal slices. Ali eats 2 slices. Mei eats 3 slices.', { keepNext: true }));
    out.push(H.fig(q5svg()));
    out.push(H.sub('a', R('What fraction of the cake do they eat altogether?   ________')));
    out.push(H.sub('b', R('What fraction of the cake is left?   ________')));
    out.push(H.sub('c', R('Who eats more? How much more?   ____________________')));
    out.push(H.q(6, 'Ravi and Siti each have a pizza. The pizzas are the same size. Ravi cuts his into 4 equal slices and eats 1 slice. Siti cuts hers into 8 equal slices and eats 3 slices. Who eats more pizza? Colour the bars to show how you know.', { keepNext: true }));
    out.push(H.fig(q6svg()));
    out.push(H.ans('Who eats more?'));
    out.push(...H.lines(1));
    return out;
  }
};
