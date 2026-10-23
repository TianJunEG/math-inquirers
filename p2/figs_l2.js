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
    s += T(x0 - 12, y + rh / 2 + 6, r.label, 20, { a: 'end' });
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
  return W(svg(600, 96, T(10, 18, 'a  from 65¢ up to $1 (100¢): count up in hops', 15, { a: 'start', w: 600, c: '#44506F' }) + l1, 'Number line from 65 cents to 1 dollar'), 2) + W(svg(600, 96, T(10, 18, 'b  from $26 up to $50: count up in hops', 15, { a: 'start', w: 600, c: '#44506F' }) + l2, 'Number line from 26 dollars to 50 dollars'), 2);
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
  { head: 'a  Which is bigger?', label: '1/3', n: 3, s: 1 }, { label: '1/8', n: 8, s: 1 },
  { label: '5/9', n: 9, s: 5 }, { label: '7/9', n: 9, s: 7 },
  { head: 'b  Smallest first', label: '1/5', n: 5, s: 1 }, { label: '1/2', n: 2, s: 1 }, { label: '1/10', n: 10, s: 1 }, { label: '1/4', n: 4, s: 1 }], { gap: 8, label: 'Bars of the same length cut into equal parts, for comparing fractions' });
const fracT2 = () => fracBars([{ label: '3/8', n: 8, s: 3 }, { label: '3/5', n: 5, s: 3 }], { label: 'Two bars of the same length: 3 of 8 equal parts and 3 of 5 equal parts shaded' });
const fracT3 = () => fracBars([{ label: '3/8 + 2/8', n: 8, s: 3, s2: 2, tail: '= ?' }], { label: 'A bar cut into 8 equal parts with 3 parts and then 2 parts shaded' });
const FX = {
  '7.3': fracQ3, '7.t2': fracT2, '7.t3': fracT3,
  '2.6': bars700,
  '3.4': sharing23,
  '5.t2': benBars, '5.t3': sitiBars, '5.t4': marbleBars,
  '6.1': legend1, '6.2': pay8, '6.3': changeLines, '6.5': spendBar, '6.6': stickerEraser,
};
module.exports = { fracQ3, itemPic, FX, W, bm, fracBars, sharing23, bars700, benBars, sitiBars, marbleBars, legend1, pay8, changeLines, spendBar };
