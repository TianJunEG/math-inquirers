// Level 2 (P2) holiday workbook: figures built from hp/figs_l1_3.js. Keys are '<lesson>.<question>' (core page),
// '<lesson>.t<n>' (Think harder 1-4) and '<lesson>.c<n>' (Go further, numbered 5-7). Each value is a function returning an HTML block.
const F = require('../hp/figs_l1_3.js');
const { svg, T, R, L, C, P, icon, coinF, noteF, numberLineF, barModelF, pictureRowF, clockF, timeLineF, NAVY, Y, BL, GR, RD, TEAL } = F;
const W = (s, mt = 0) => `<div class="p img" style="text-align:center;margin:${mt}px 0 2px">${s}</div>`;
const bm = (o, label) => { const r = barModelF({ unit: 60, labelW: 96, rowH: 34, gap: 16, ...o }, o.y0 || 8); return W(svg(o.W || 600, r.y + (o.pad || 6), r.s, label || 'bar model')); };

// fraction bars: [{label:'1/3', n:3, s:1}] stacked, equal total length
const fracBars = (rows, o = {}) => {
  const bw = o.bw || 380, x0 = o.x0 || 90, rh = o.rh || 30, gap = o.gap || 12; let s = '', y = 6;
  rows.forEach(r => {
    if (r.head) { s += T(10, y + 14, r.head, 18, { a: 'start', c: TEAL }); y += 24; }
    s += T(x0 - 12, y + rh / 2 + 6, r.label, r.label.length > 5 ? 16 : 20, { a: 'end' });
    for (let i = 0; i < r.n; i++) s += R(x0 + i * bw / r.n, y, bw / r.n, rh, i < r.s ? 'url(#hz)' : (i < r.s + (r.s2 || 0) ? 'url(#dt)' : '#fff'), { sw: 2.4 });
    if (r.tail) s += T(x0 + bw + 14, y + rh / 2 + 6, r.tail, 17, { a: 'start', c: TEAL });
    y += rh + gap;
  });
  return W(svg(o.W || 600, y, s, o.label || 'fraction bars'), 2);
};
const fracLabel = (a, b) => a + '/' + b;

// P2 L3 No.4: Ravi shares 23 stickers among 4 friends
const sharing23 = () => {
  let s = R(8, 6, 584, 92, '#FFF9E8', { sw: 2.4, rx: 8 }) + T(92, 40, 'Ravi’s', 18) + T(92, 62, '23 stickers', 18);
  for (let i = 0; i < 23; i++) s += icon('star', 190 + (i % 12) * 33 + (i >= 12 ? 16 : 0), 32 + Math.floor(i / 12) * 36, 31);
  for (let f = 0; f < 4; f++) { const cx = 62 + f * 114; s += icon('face', cx, 126, 40, { v: f }) + C(cx, 200, 44, '#fff', { dash: true, sw: 2.4 }) + T(cx, 262, 'Friend ' + (f + 1), 16); }
  s += R(478, 150, 114, 100, '#fff', { dash: true, sw: 2.4, rx: 8 }) + T(535, 140, 'left over', 17, { c: TEAL });
  return W(svg(600, 272, s, 'Ravi has 23 stickers, 4 friends with an empty plate each, and a box for the stickers left over'), 2);
};

// P2 L2 No.6: two bars, long bar is 200 longer, total 700
const bars700 = () => bm({ rows: [{ label: 'short bar', segs: [{ u: 3, t: '?', k: 'a' }] }, { label: 'long bar', segs: [{ u: 3, t: '?', k: 'a' }, { u: 1.3, t: '200', k: 'h' }] }], vbrace: { from: 0, to: 1, t: '700 altogether' }, W: 600, unit: 68 }, 'Two bars: the long bar is 200 longer; together 700');
// P2 L5 T2: Ben's money, book $15, dad gives as much as he had left, now $42
const benBars = () => bm({ rows: [
  { label: 'At first', segs: [{ u: 1.3, t: '$15 book', k: 'h' }, { u: 2, t: 'left', k: 'a' }], brace: { from: 0, to: 3.3, t: '? at first', pos: 'top' } },
  { label: 'After the gift', segs: [{ u: 2, t: 'left', k: 'a' }, { u: 2, t: 'gift', k: 'b' }], brace: { from: 0, to: 4, t: '$42 now', pos: 'bottom' } }], unit: 70, labelW: 110 }, 'Bars for the money story');
// P2 L5 T3: Siti's beads
const sitiBars = () => bm({ rows: [
  { label: 'At first', segs: [{ u: 2, t: 'half', k: 'a' }, { u: 2, t: 'half', k: 'dt', size: 15 }], brace: { from: 0, to: 4, t: '? beads', pos: 'top' } },
  { label: 'Now', segs: [{ u: 2, t: 'half', k: 'a' }, { u: 1.4, t: '12', k: 'h' }], brace: { from: 0, to: 3.4, t: '30 beads', pos: 'bottom' } }], unit: 70, labelW: 100 }, 'Bars: half given away, 12 more bought, 30 now');
// P2 L5 T4: three children's marbles, total 40
const marbleBars = () => bm({ rows: [
  { label: 'Ali', segs: [{ u: 3, t: '?', k: 'a' }] },
  { label: 'Ben', segs: [{ u: 3, t: '?', k: 'a' }, { u: .9, t: '5', k: 'h' }] },
  { label: 'Siti', segs: [{ u: 3, t: '?', k: 'a' }, { u: 1.4, t: '8', k: 'h' }] }], vbrace: { from: 0, to: 2, t: '40' }, unit: 80, gap: 12, rowH: 30 }, 'Three bars: Ben has 5 more than Ali and Siti has 8 more than Ali; 40 altogether');

// ---- money (L6) ----
const tray = () => { // the notes and coins we use
  let s = '', x = 6;
  [[5, 'note'], [2, 'note'], [1, 'coin']].forEach(([v, k]) => { if (k === 'note') { s += noteF(v, x, 10, 92, 44); x += 104; } else { s += coinF(100, x + 27, 32); x += 66; } });
  return s;
};
const pay8 = () => W(svg(600, 66, tray() + T(300, 36, '= pay exactly $8', 19, { a: 'start' }) + T(300, 58, '(use each kind as often as you like)', 14, { a: 'start', w: 600, c: '#44506F', i: true }), 'A $5 note, a $2 note and a $1 coin, to pay exactly 8 dollars'), 2);
const legend1 = () => { // L6 No.1: all notes and coins we have
  let s = T(4, 18, 'Coins:', 16, { a: 'start' }), x = 62;
  [5, 10, 20, 50, 100].forEach(v => { const r = F.COIN[v].r; s += coinF(v, x + r, 36); x += 2 * r + 12; });
  s += T(340, 18, 'Notes:', 16, { a: 'start' }); x = 396;
  [2, 5, 10].forEach((v, i) => { s += noteF(v, 340 + i * 80, 30, 72, 38); });
  return W(svg(600, 80, s, 'The coins 5, 10, 20, 50 cents and 1 dollar, and the notes 2, 5, 10 and 50 dollars'), 2);
};
// change by counting up: start and end marked, hops left for the child
const changeLines = () => {
  const l1 = numberLineF({ min: 65, max: 100, W: 600, step: 5, labelEvery: 5, fmt: v => v + '¢', marks: [{ v: 65, kind: 'dot' }, { v: 100, kind: 'dot' }], size: 16 }, 70);
  const l2 = numberLineF({ min: 26, max: 50, W: 600, step: 1, labelEvery: 2, fmt: v => '$' + v, marks: [{ v: 26, kind: 'dot' }, { v: 50, kind: 'dot' }], size: 16 }, 70);
  return W(svg(600, 112, T(10, 18, 'a  from 65¢ up to $1 (100¢): count up in hops', 15, { a: 'start', w: 600, c: '#44506F' }) + l1, 'Number line from 65 cents to 1 dollar'), 2) + W(svg(600, 112, T(10, 18, 'b  from $26 up to $50: count up in hops', 15, { a: 'start', w: 600, c: '#44506F' }) + l2, 'Number line from 26 dollars to 50 dollars'), 2);
};
const spendBar = () => bm({ rows: [{ label: 'Siti', segs: [{ u: 1.6, t: '45¢', k: 'a' }, { u: 1.2, t: '30¢', k: 'b' }, { u: 1.0, t: '25¢ left', k: 'dt' }], brace: { from: 0, to: 3.8, t: '? at first', pos: 'bottom' } }], unit: 110, labelW: 60, rowH: 44 }, 'A bar: 45 cents, 30 cents and 25 cents left');
const stickerEraser = () => W(svg(600, 76, (() => { let s = ''; s += R(10, 10, 130, 56, Y, { sw: 2.4, rx: 6 }) + icon('star', 38, 38, 32) + T(100, 44, '20¢', 22); s += T(150, 44, 'each sticker', 15, { a: 'start', w: 600 }); s += R(330, 10, 130, 56, BL, { sw: 2.4, rx: 6 }) + P([[352, 28], [388, 28], [388, 48], [352, 48]], '#fff', { sw: 2 }) + T(425, 44, '50¢', 22); s += T(470, 44, 'each eraser', 15, { a: 'start', w: 600 }); return s; })(), 'A sticker costs 20 cents and an eraser costs 50 cents'), 2);
// small item pictures for price tables (inline svg, about 9 mm)
const itemPic = (name) => {
  const k = {
    'Curry puff': () => `<path d="M6 30 Q6 8 24 8 Q42 8 42 30 Z" fill="#F0C27A" stroke="${NAVY}" stroke-width="2.4"/><path d="M12 24 Q24 14 36 24" fill="none" stroke="${NAVY}" stroke-width="1.8" stroke-dasharray="3 3"/>`,
    'Notebook': () => `<rect x="9" y="4" width="30" height="36" rx="3" fill="${BL}" stroke="${NAVY}" stroke-width="2.4"/><line x1="16" y1="4" x2="16" y2="40" stroke="${NAVY}" stroke-width="2"/><line x1="21" y1="14" x2="34" y2="14" stroke="${NAVY}" stroke-width="2"/><line x1="21" y1="22" x2="34" y2="22" stroke="${NAVY}" stroke-width="2"/>`,
    'Umbrella': () => `<path d="M4 24 Q4 4 24 4 Q44 4 44 24 Q38 18 34 24 Q29 18 24 24 Q19 18 14 24 Q10 18 4 24 Z" fill="${RD}" stroke="${NAVY}" stroke-width="2.4"/><path d="M24 24 L24 38 Q24 43 19 42" fill="none" stroke="${NAVY}" stroke-width="2.6"/>`,
    'Bicycle': () => `<circle cx="11" cy="30" r="8" fill="#fff" stroke="${NAVY}" stroke-width="2.4"/><circle cx="37" cy="30" r="8" fill="#fff" stroke="${NAVY}" stroke-width="2.4"/><path d="M11 30 L20 14 L32 14 L37 30 M20 14 L25 30 L11 30 M25 30 L32 14 M17 11 L23 11 M30 10 L35 10" fill="none" stroke="${NAVY}" stroke-width="2.4" stroke-linejoin="round"/>`
  }[name];
  return k ? `<svg viewBox="0 0 48 46" width="38" height="36" xmlns="http://www.w3.org/2000/svg" aria-label="${name}" style="vertical-align:middle">${k()}</svg> ` : '';
};
const fracQ3 = () => fracBars([
  { head: 'a  Which is bigger?', label: '1/3', n: 3, s: 0 }, { label: '1/8', n: 8, s: 0 },
  { label: '5/9', n: 9, s: 0 }, { label: '7/9', n: 9, s: 0 },
  { head: 'b  Smallest first', label: '1/5', n: 5, s: 0 }, { label: '1/2', n: 2, s: 0 }, { label: '1/10', n: 10, s: 0 }, { label: '1/4', n: 4, s: 0 }], { gap: 8, label: 'Bars of the same length cut into equal parts, not shaded, for comparing fractions' });
const fracT2 = () => fracBars([{ label: '3/8', n: 8, s: 3 }, { label: '3/5', n: 5, s: 3 }], { label: 'Two bars of the same length: 3 of 8 equal parts and 3 of 5 equal parts shaded' });
const fracT3 = () => fracBars([{ label: '3/8 + 2/8', n: 8, s: 3, s2: 2, tail: '= ?' }], { label: 'A bar cut into 8 equal parts with 3 parts and then 2 parts shaded' });
// ---- balance scales: items 'apple','lemon','pomelo','cube','ball','w:<label>' ----
const itemShape = (name, cx, cy, sz) => {
  if (name === 'apple') return icon('apple', cx, cy, sz);
  if (name === 'lemon') return `<ellipse cx="${cx}" cy="${cy}" rx="${sz * .42}" ry="${sz * .3}" fill="${Y}" stroke="${NAVY}" stroke-width="2.4"/>` + P([[cx - sz * .42, cy], [cx - sz * .52, cy - 3], [cx - sz * .52, cy + 3]], Y, { sw: 1.6 }) + P([[cx + sz * .42, cy], [cx + sz * .52, cy - 3], [cx + sz * .52, cy + 3]], Y, { sw: 1.6 });
  if (name === 'melon') return `<ellipse cx="${cx}" cy="${cy}" rx="${sz * .6}" ry="${sz * .46}" fill="${GR}" stroke="${NAVY}" stroke-width="2.6"/>` + `<path d="M${cx - sz * .2} ${cy - sz * .44} Q${cx - sz * .36} ${cy} ${cx - sz * .2} ${cy + sz * .44} M${cx + sz * .2} ${cy - sz * .44} Q${cx + sz * .36} ${cy} ${cx + sz * .2} ${cy + sz * .44}" fill="none" stroke="${NAVY}" stroke-width="1.8"/>`;
  if (name === 'pomelo') return C(cx, cy, sz * .56, GR, { sw: 2.6 }) + `<path d="M${cx - sz * .3} ${cy - sz * .15} Q${cx} ${cy - sz * .4} ${cx + sz * .3} ${cy - sz * .15}" fill="none" stroke="${NAVY}" stroke-width="1.8"/>`;
  if (name === 'cube') return R(cx - sz * .36, cy - sz * .36, sz * .72, sz * .72, BL, { sw: 2.4 }) + L(cx - sz * .36, cy - sz * .36 + 8, cx + sz * .36, cy - sz * .36 + 8, { sw: 1.4 });
  if (name === 'ball') return C(cx, cy, sz * .42, RD, { sw: 2.4 }) + `<path d="M${cx - sz * .4} ${cy} Q${cx} ${cy + sz * .2} ${cx + sz * .4} ${cy}" fill="none" stroke="${NAVY}" stroke-width="1.8"/>`;
  if (name.startsWith('w:')) return P([[cx - sz * .66, cy + sz * .4], [cx + sz * .66, cy + sz * .4], [cx + sz * .42, cy - sz * .4], [cx - sz * .42, cy - sz * .4]], '#E6E9F0', { sw: 2.4 }) + T(cx, cy + sz * .24, name.slice(2).replace(' g', 'g'), 14, { w: 800 });
  return '';
};
const scaleF = (cx, left, right, o = {}) => {
  // beam at y, pans hang d below it so a second row of items sits under the beam, post base at y + d + 58
  const arm = o.arm || 130, y = o.y || 40, sz = o.sz || 34, d = o.drop || 70, pw = o.pw || 50; let s = '';
  s += L(cx, y, cx, y + d + 58, { sw: 3 }) + P([[cx - (o.post || 24), y + d + 58], [cx + (o.post || 24), y + d + 58], [cx, y + 6]], '#fff', { sw: 2.4 }) + L(cx - arm, y, cx + arm, y, { sw: 4 });
  [[cx - arm, left], [cx + arm, right]].forEach(([px, items]) => {
    s += L(px, y, px - pw + 4, y + d, { sw: 1.8 }) + L(px, y, px + pw - 4, y + d, { sw: 1.8 }) + `<path d="M${px - pw} ${y + d} Q${px} ${y + d + 18} ${px + pw} ${y + d}" fill="#fff" stroke="${NAVY}" stroke-width="2.6"/>`;
    const heavy = items.length && items[0].startsWith('w:'), pitch = sz * (heavy ? 1.5 : .95), per = heavy ? 2 : 3, n = items.length;
    items.forEach((it, i) => { const row = Math.floor(i / per), col = i % per, inRow = Math.min(per, n - row * per); s += itemShape(it, px + (col - (inRow - 1) / 2) * pitch, y + d - 12 - row * (sz * .9), sz); });
  });
  return s;
};
const balances = (defs, label, h) => W(svg(600, h || 200, defs.map((d, i) => scaleF(150 + i * 300, d[0], d[1], { arm: 80, sz: 34, y: 40, drop: 70 })).join('') + defs.map((d, i) => T(150 + i * 300, 16, 'Scale ' + (i + 1), 17)).join(''), label), 2);
// L9 No.1: three level scales, each item named under its pan
const scalesQ1 = () => {
  const defs = [[['melon'], ['apple', 'apple'], 'melon', '2 apples', 94], [['apple'], ['w:100 g', 'w:100 g'], 'apple', '2 × 100 g', 286], [['melon'], ['apple', 'lemon', 'lemon', 'lemon', 'lemon'], 'melon', 'apple, 4 lemons', 476]];
  let s = '';
  defs.forEach((d, i) => { const cx = d[4]; s += scaleF(cx, d[0], d[1], { arm: 52, pw: 40, post: 12, sz: 27, y: 40, drop: 70 }) + T(cx, 16, 'Scale ' + (i + 1), 17) + T(cx - 52, 158, d[2], 15, { w: 700 }) + T(cx + 68, 158, d[3], 15, { w: 700 }); });
  return svg(600, 206, s, 'Three level scales. Scale 1: a melon and 2 apples. Scale 2: an apple and two 100 g weights. Scale 3: a melon and an apple with 4 lemons.');
};
const balT1 = () => balances([[['apple', 'apple', 'lemon'], ['pomelo']], [['pomelo'], ['lemon', 'lemon', 'lemon', 'lemon', 'lemon']]], 'Two level scales: 2 apples and a lemon balance a pomelo; a pomelo balances 5 lemons');
const balT3 = () => balances([[['apple', 'apple', 'apple'], ['pomelo']], [['pomelo', 'apple', 'apple'], ['w:500 g']]], 'Two level scales: 3 apples balance a pomelo; a pomelo and 2 apples balance 500 g');
const balC6 = () => balances([[['cube', 'cube', 'ball'], ['ball', 'ball']], [['ball', 'cube'], ['w:300 g']]], 'Two level scales: 2 cubes and a ball balance 2 balls; a ball and a cube balance 300 g');

// ---- towers (C6 Lesson 4): tower k has 3k - 1 cubes ----
const towers = () => { let s = '', x = 30; const c = 24;
  [2, 5, 8].forEach((n, i) => { for (let k = 0; k < n; k++) s += R(x, 212 - (k + 1) * c, c, c, Y, { sw: 2.2 }); s += T(x + c / 2, 232, 'Tower ' + (i + 1), 15); x += c + 70; });
  s += T(x + 10, 120, '… keeps growing the same way', 15, { a: 'start', w: 600, i: true, c: '#44506F' });
  return W(svg(600, 240, s, 'Towers of cubes with 2, 5 and 8 cubes'), 2); };
const frogs = () => {
  const mk = (start, jump, name) => numberLineF({ min: 0, max: 30, W: 600, labelEvery: 2, size: 15, hops: [{ from: start, to: start + jump, label: '' + jump, h: 26 }], frog: start }, 72);
  return W(svg(600, 106, T(8, 14, 'Frog A: starts at 0, jumps 4', 15, { a: 'start', w: 600 }) + mk(0, 4), 'Number line 0 to 30 with frog A on 0 and its first jump of 4'), 0) + W(svg(600, 106, T(8, 14, 'Frog B: starts at 2, jumps 3', 15, { a: 'start', w: 600 }) + mk(2, 3), 'Number line 0 to 30 with frog B on 2 and its first jump of 3'), 0);
};
// time lines
const tl = (t0, t1, ticks, hops, label) => { const dy = ticks.some(k => k.dy) ? 20 : 0, y0 = 54; return W(svg(600, y0 + 34 + dy + 14, timeLineF({ t0, t1, W: 600, pad: 40, ticks, jumps: hops.map(h => ({ from: h[0], to: h[1], label: h[2], h: 22 })), marks: [] }, y0), label), 0); };
const l9t2 = () => tl(632, 745, [{ t: 645, label: '10:45 am', dy: 20 }, { t: 660, label: '11:00' }, { t: 720, label: '12:00' }, { t: 730, label: '12:10 pm', dy: 20 }], [[645, 660, '? min'], [660, 720, '? h'], [720, 730, '? min']], 'Time line from 10:45 am to 12:10 pm with 11:00 and 12:00 marked');
const l9c7 = () => tl(485, 650, [{ t: 495, label: '8:15 am' }], [], 'Time line starting at 8:15 am for three lessons and two breaks');
// base-ten blocks: rod = 10, flat = 100
const rod = (x, y) => { let s = ''; for (let i = 0; i < 10; i++) s += R(x, y + i * 5.2, 11, 5.2, '#fff', { sw: 1.1 }); return s + R(x, y, 11, 52, 'none', { sw: 2 }); };
const flat = (x, y) => { let s = R(x, y, 52, 52, '#fff', { sw: 2 }); for (let i = 1; i < 10; i++) s += L(x + i * 5.2, y, x + i * 5.2, y + 52, { sw: .8 }) + L(x, y + i * 5.2, x + 52, y + i * 5.2, { sw: .8 }); return s; };
const blocksT3 = () => {
  let s = T(6, 16, 'Ali: 46 ten-blocks', 16, { a: 'start' });
  for (let i = 0; i < 46; i++) s += rod(8 + (i % 23) * 24, 24 + Math.floor(i / 23) * 62);
  s += T(6, 168, 'Siti: 3 hundred-blocks and 15 ten-blocks', 16, { a: 'start' });
  for (let i = 0; i < 3; i++) s += flat(8 + i * 62, 178);
  for (let i = 0; i < 15; i++) s += rod(210 + i * 24, 178);
  return W(svg(600, 240, s, 'Ali has 46 ten-blocks. Siti has 3 hundred-blocks and 15 ten-blocks.'), 2);
};
const strip12 = () => fracBars([{ label: 'one whole', n: 12, s: 0 }], { label: 'A strip cut into 12 equal parts' });
const strip10 = () => fracBars([{ label: 'one whole', n: 10, s: 0 }], { label: 'A strip cut into 10 equal parts' });
const kiteBar = () => bm({ rows: [{ label: 'Ben’s money', segs: [{ u: 2, t: 'kite (half)', k: 'a', size: 15 }, { u: .8, t: '$4', k: 'h' }, { u: 1.2, t: '$6 left', k: 'b', size: 15 }], brace: { from: 0, to: 4, t: '? at first', pos: 'top' } }], unit: 100, labelW: 134, rowH: 36 }, 'Ben’s money as a bar cut in half');
// L3 No.3: a pen of 7 animals, all hens to start (2 legs each), one swapped for a goat at a time
const hens7 = () => { let s = R(6, 4, 326, 56, '#fff', { sw: 2.2, rx: 8, dash: true }) + T(168, 78, 'the pen: 7 animals', 16, { w: 600, c: '#44506F' }); for (let i = 0; i < 7; i++) s += icon('bird', 36 + i * 44, 34, 32); s += T(352, 28, 'hen: 2 legs', 17, { a: 'start' }) + T(352, 52, 'goat: 4 legs', 17, { a: 'start' }); return W(svg(520, 84, s, 'A pen with 7 hens, each hen has 2 legs and each goat has 4 legs'), 2); };
// L3 No.5: one van with 5 seats and 28 children
const vans28 = () => { let s = R(6, 6, 188, 46, '#fff', { sw: 2.6, rx: 8 }); for (let i = 0; i < 5; i++) s += R(16 + i * 34, 14, 28, 30, Y, { sw: 2, rx: 4 }); s += T(100, 72, 'one van: 5 seats', 15); for (let i = 0; i < 28; i++) s += icon('face', 250 + (i % 14) * 24, 22 + Math.floor(i / 14) * 28, 22, { v: i }); s += T(400, 78, '28 children', 15); return W(svg(600, 90, s, 'A van with 5 seats and 28 children waiting'), 2); };
// layers seen from above: [[cols, rows, label], ...]
const layers = (defs, label) => { let s = '', x = 10; const c = 30; defs.forEach(([cols, rows, name]) => { for (let i = 0; i < cols; i++) for (let j = 0; j < rows; j++) s += R(x + i * c, 24 + j * c, c, c, Y, { sw: 2.2 }); s += T(x + cols * c / 2, 14, name, 16); x += cols * c + 40; }); return W(svg(Math.max(x, 300), 24 + 4 * 30 + 12, s, label), 2); };
const layersT1 = () => layers([[4, 3, 'bottom layer'], [3, 2, 'middle layer'], [1, 1, 'top']], 'Three layers of cubes seen from above: 4 by 3, 3 by 2 and 1');
const layersC5 = () => layers([[1, 1, 'top'], [2, 2, 'next'], [3, 3, 'next'], [4, 4, 'bottom']], 'Four layers seen from above: 1 by 1, 2 by 2, 3 by 3 and 4 by 4');
// L4 T4: houses made of sticks in a row (a house is 2 walls, a floor and 2 roof sticks; houses share walls): 5, 9, 13 sticks
const stickHouses = () => {
  let s = '', x = 14; const w = 40, h = 36, r = 22; const st = (x1, y1, x2, y2) => L(x1, y1, x2, y2, { sw: 6, c: '#B8860B' }) + L(x1, y1, x2, y2, { sw: 2, c: NAVY });
  [1, 2, 3].forEach(k => { const y0 = 12 + r; for (let i = 0; i <= k; i++) s += st(x + i * w, y0, x + i * w, y0 + h); for (let i = 0; i < k; i++) s += st(x + i * w, y0 + h, x + (i + 1) * w, y0 + h) + st(x + i * w, y0, x + i * w + w / 2, y0 - r) + st(x + i * w + w / 2, y0 - r, x + (i + 1) * w, y0); s += T(x + k * w / 2, y0 + h + 26, k + (k > 1 ? ' houses' : ' house'), 16); x += k * w + 50; });
  return W(svg(Math.max(x, 300), 112, s, 'Houses made of sticks in a row: 1, 2 and 3 houses'), 2);
};
const FX2 = {
  '4.t4': stickHouses,
  '8.t1': layersT1, '8.c5': layersC5,
  '3.3': hens7, '3.5': vans28,
  '4.c6': towers, '4.c7': frogs, '9.t2': l9t2, '9.c7': l9c7, '9.t1': balT1, '9.t3': balT3, '9.c6': balC6, '1.t3': blocksT3, '7.c5': strip12, '7.c6': strip10, '6.t1': kiteBar,
};
const FX = {
  ...FX2,
  '7.3': fracQ3, '7.t2': fracT2, '7.t3': fracT3,
  '2.6': bars700,
  '3.4': sharing23,
  '5.t2': benBars, '5.t3': sitiBars, '5.t4': marbleBars,
  '6.1': legend1, '6.2': pay8, '6.3': changeLines, '6.5': spendBar, '6.6': stickerEraser,
};
module.exports = { scalesQ1, fracQ3, itemPic, FX, W, bm, fracBars, sharing23, bars700, benBars, sitiBars, marbleBars, legend1, pay8, changeLines, spendBar };
