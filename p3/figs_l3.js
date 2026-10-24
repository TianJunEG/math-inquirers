// Level 3 (P3) holiday workbook: figures built from hp/figs_l1_3.js. Keys: '<lesson>.<q>' (after the question text),
// '<lesson>.<q><letter>' (after a part), '<lesson>.t<n>' (Think harder 1-4), '<lesson>.c<n>' (Go further, numbered 5-7).
const F = require('../hp/figs_l1_3.js');
const { svg, T, R, L, C, P, icon, numberLineF, barModelF, timeLineF, hopF, NAVY, Y, BL, GR, RD, TEAL } = F;
const { fracBars } = require('../p2/figs_l2.js');
const W = (s, mt = 0) => `<div class="p img" style="text-align:center;margin:${mt}px 0 2px">${s}</div>`;
const bm = (o, label) => { const r = barModelF({ unit: 60, labelW: 90, rowH: 34, gap: 14, ...o }, o.y0 || 14); return W(svg(o.W || 600, r.y + (o.pad || 8), r.s + (o.extra ? o.extra(r) : ''), label || 'bar model')); };
const Q = '?';

// ---------------- Lesson 4: bar models (skeletons: the child fills in and solves) ----------------
const l4q4 = () => bm({ y0: 4, rows: [{ label: 'Ben', segs: [{ u: 3, t: Q, k: 'a' }] }, { label: 'Ali', segs: [{ u: 3, t: Q, k: 'a' }, { u: 1, t: '24 more', k: 'h', size: 15 }] }], vbrace: { from: 0, to: 1, t: '150 altogether' }, unit: 76 }, 'Two bars: Ali has 24 more than Ben; 150 altogether');
const l4q5 = () => bm({ y0: 4, rows: [
  { label: 'Mei', segs: [{ u: 8.5, t: '85', k: 'a' }] },
  { label: 'Siti', segs: [{ u: 4.7, t: '47', k: 'b' }, { u: 3.8, t: '?', k: 'd', tpos: .18 }] }], unit: 50, labelW: 70,
  extra: r => L(70 + 6 + 66 * 5, r.tops[0] - 8, 70 + 6 + 66 * 5, r.tops[1] + 42, { dash: true, sw: 2 }) + T(70 + 6 + 66 * 5, r.tops[1] + 60, 'same number here', 15, { c: TEAL }) }, 'Mei has 85, Siti has 47; Mei gives some to Siti until they are equal');
const l4q6 = () => bm({ y0: 4, rows: [
  { label: 'Ali before', segs: [{ u: 45, t: '$45', k: 'a' }] },
  { label: 'Ben before', segs: [{ u: 18, t: '$18', k: 'b' }] },
  { label: 'Ali now', segs: [{ u: 45, t: '$45', k: 'a' }, { u: 10, t: '+$10', k: 'h', size: 15 }] },
  { label: 'Ben now', segs: [{ u: 18, t: '$18', k: 'b' }, { u: 10, t: '+$10', k: 'h', size: 15 }] }], unit: 7, labelW: 100, rowH: 28, gap: 10 }, 'Before and after bars: Ali 45 and Ben 18, then each gets 10 more');
const l4t1 = () => bm({ y0: 4, rows: [{ label: 'Ben', segs: [{ u: 1, t: Q, k: 'b' }] }, { label: 'Ali', segs: [{ u: 1, t: Q, k: 'a' }, { u: 1, t: Q, k: 'a' }, { u: 1, t: Q, k: 'a' }] }], vbrace: { from: 0, to: 1, t: '96 altogether' }, unit: 90, rowH: 22, gap: 6 }, 'Ali has 3 times as many as Ben; 96 altogether');
const l4t2 = () => bm({ y0: 4, rows: [{ label: 'Mei', segs: [{ u: 3, t: Q, k: 'a' }] }, { label: 'Siti', segs: [{ u: 3, t: Q, k: 'a' }, { u: 1.3, t: '54 more', k: 'h', size: 15 }] }], unit: 80, rowH: 22, gap: 6 }, 'Siti has 54 more beads than Mei');
const l4t3 = () => bm({ y0: 4, rows: [{ label: 'Box B', segs: [{ u: 3, t: Q, k: 'a' }] }, { label: 'Box A', segs: [{ u: 3, t: Q, k: 'a' }, { u: .8, t: '50', k: 'h' }] }, { label: 'Box C', segs: [{ u: 3, t: Q, k: 'a' }, { u: .8, t: '50', k: 'h' }, { u: .8, t: '50', k: 'h' }] }], vbrace: { from: 0, to: 2, t: '600' }, unit: 80, rowH: 22, gap: 6 }, 'Boxes A, B, C of pens, 600 altogether');
const l4t4 = () => bm({ y0: 4, rows: [{ label: 'Flour', segs: [{ u: 3, t: Q, k: 'a' }] }, { label: 'Rice', segs: [{ u: 3, t: Q, k: 'a' }, { u: 1, t: '3 kg', k: 'h' }] }], vbrace: { from: 0, to: 1, t: '9 kg' }, unit: 80, rowH: 22, gap: 6 }, 'Rice is 3 kg heavier than flour; 9 kg altogether');
const l4c7 = () => bm({ y0: 4, rows: [{ label: '1st piece', segs: [{ u: 1, t: Q, k: 'a' }] }, { label: '2nd piece', segs: [{ u: 1, t: Q, k: 'a' }, { u: 1, t: Q, k: 'a' }] }, { label: '3rd piece', segs: [{ u: 1, t: Q, k: 'a' }, { u: 1, t: Q, k: 'a' }, { u: .8, t: '25 cm', k: 'h', size: 14 }] }], vbrace: { from: 0, to: 2, t: '475 cm' }, unit: 80, labelW: 100, rowH: 28, gap: 8 }, 'A ribbon cut in 3 pieces: the 2nd is twice the 1st, the 3rd is 25 cm longer than the 2nd');

// ---------------- Lesson 6: empty bars cut into equal parts (the child shades) ----------------
const empty = (rows, label) => fracBars(rows.map(r => ({ ...r, s: 0 })), { label, gap: 10, bw: 360, x0: 128 });
const l6q5 = () => empty([{ label: 'whole fence', n: 6 }], 'A bar for the fence cut into 6 equal parts');
const l6t2 = () => empty([{ label: 'fifths', n: 5 }, { label: 'tenths', n: 10 }], 'Two bars of the same length, one cut into fifths and one into tenths');
const l6t3 = () => empty([{ label: 'the book', n: 4 }], 'A bar for the book cut into 4 equal parts');
const l6t4 = () => empty([{ label: 'thirds', n: 3 }, { label: 'sixths', n: 6 }, { label: 'twelfths', n: 12 }], 'Three bars of the same length cut into thirds, sixths and twelfths');
const l6c6 = () => W(svg(600, 150, (() => {
  let s = T(10, 22, 'One whole bar (8 equal parts of 1/8):', 16, { a: 'start' }); for (let i = 0; i < 8; i++) s += R(10 + i * 40, 32, 40, 30, '#fff', { sw: 2.4 });
  s += T(10, 96, 'Pieces you may use:', 16, { a: 'start' });
  s += R(10, 106, 160, 30, Y, { sw: 2.4 }) + T(90, 128, '1/2', 17); s += R(190, 106, 80, 30, BL, { sw: 2.4 }) + T(230, 128, '1/4', 17); s += R(290, 106, 40, 30, GR, { sw: 2.4 }) + T(310, 128, '1/8', 16);
  return s; })(), 'A whole bar of 8 parts and pieces of 1/2, 1/4 and 1/8'), 2);

// ---------------- Lesson 9: measures and time ----------------
const ribbon3m = () => bm({ rows: [{ label: '3 m', segs: [{ u: 65, t: '65', k: 'a' }, { u: 65, t: '65', k: 'a' }, { u: 65, t: '65', k: 'a' }, { u: 65, t: '65', k: 'a' }, { u: 40, t: '?', k: 'd' }], brace: { from: 0, to: 300, t: '3 m = 300 cm', pos: 'top' } }], unit: 1.5, labelW: 60, rowH: 34, y0: 14 }, 'A ribbon 3 m long cut into four pieces of 65 cm');
const hm = t => { const h = Math.floor(t / 60) % 24, m = t % 60; return h + ':' + String(m).padStart(2, '0'); };
const ap = t => { const h = Math.floor(t / 60) % 24, m = t % 60, pm = h >= 12, h12 = h % 12 || 12; return h12 + ':' + String(m).padStart(2, '0') + (pm ? ' pm' : ' am'); };
// time line with ticks and blank hops; ticks [{t,label?}] ; hops [[from,to]]
const tline = (o) => {
  const dy = o.ticks.some(k => k.dy) ? 20 : 0, H = (o.H || 92) + dy, y0 = o.y0 || 58;
  let s = timeLineF({ t0: o.t0, t1: o.t1, W: 600, pad: 40, ticks: o.ticks.map(k => ({ t: k.t, label: k.label === undefined ? ap(k.t) : k.label, big: k.big, dy: k.dy })), jumps: (o.hops || []).map(h => ({ from: h[0], to: h[1], label: h[2] === undefined ? '? min' : h[2], h: 22, dash: false })), marks: [] }, y0);
  return W(svg(600, H, s, o.label || 'time line'), 0);
};
const l9q5a = () => tline({ t0: 938, t1: 1037, ticks: [{ t: 945, label: '3:45 pm' }, { t: 960, label: '4:00' }, { t: 1020, label: '5:00' }, { t: 1030, label: '5:10 pm' }], hops: [[945, 960, '? min'], [960, 1020, '? h'], [1020, 1030, '? min']], label: 'Time line from 3:45 pm to 5:10 pm with the o’clock times 4:00 and 5:00' });
const l9q5b = () => tline({ t0: 988, t1: 1062, ticks: [{ t: 995, label: '4:35 pm' }, { t: 1020, label: '5:00' }, { t: 1045, label: '?' }], hops: [[995, 1020, '? min'], [1020, 1045, '? min']], label: 'Time line starting at 4:35 pm with 5:00 marked and a question mark at the end of the lesson' });
const l9q5c = () => tline({ t0: 1125, t1: 1285, ticks: [{ t: 1140, label: '7:00' }, { t: 1200, label: '8:00' }, { t: 1260, label: '9:00' }, { t: 1275, label: '9:15 pm', dy: 20 }], hops: [[1260, 1275, '? min']], label: 'Time line ending at 9:15 pm with 7:00, 8:00 and 9:00 marked' });
const l9q6 = () => { // buses every 25 minutes from 06:40; Ravi arrives 08:15
  const t0 = 395, ticks = []; for (let k = 0; k < 6; k++) ticks.push({ t: 400 + k * 25, label: k === 0 ? '06:40' : '' });
  ticks.push({ t: 495, label: '08:15', big: true });
  const o = { t0: 380, t1: 545, W: 600, pad: 40 }; let s = timeLineF({ ...o, ticks }, 56);
  s += T(40 + (495 - 380) * (520 / 165), 22, 'Ravi arrives', 15, { c: TEAL }) + L(40 + (495 - 380) * (520 / 165), 26, 40 + (495 - 380) * (520 / 165), 44, { c: TEAL, sw: 2.4 });
  return W(svg(600, 86, s, 'Time line from 06:40 with a mark every 25 minutes for the buses and Ravi at 08:15'), 0);
};
const l9q4 = () => { // 0-24 hour strip
  let s = '', x0 = 24, w = 552, X = h => x0 + h * w / 24;
  s += R(X(0), 20, X(12) - X(0), 30, '#fff', { sw: 2.4 }) + R(X(12), 20, X(24) - X(12), 30, 'url(#dt)', { sw: 2.4 });
  s += `<rect x="${F.f1(X(12) - 40)}" y="26" width="80" height="18" fill="#fff"/>`;
  s += T(X(6), 40, 'am', 17) + R(X(18) - 18, 26, 36, 22, '#fff', { sw: 0 }) + T(X(18), 42, 'pm', 17);
  for (let h = 0; h <= 24; h += 3) s += L(X(h), 50, X(h), 60, { sw: 2.4 }) + T(X(h), 78, String(h).padStart(2, '0') + ':00', 14.5);
  s += T(X(12), 12, 'noon', 14, { c: TEAL });
  return W(svg(600, 90, s, 'A strip for the 24 hours of a day: 00:00 to 12:00 is am, 12:00 to 24:00 is pm'), 0);
};
const l9t2 = () => tline({ t0: 520, t1: 1290, ticks: [{ t: 570, label: '09:30' }, { t: 720, label: '12:00' }, { t: 900, label: '15:00' }, { t: 1080, label: '18:00' }, { t: 1260, label: '21:00' }], hops: [], H: 76, y0: 40, label: 'Time line from 09:30 to 21:00' });
const l9t3 = () => bm({ y0: 10, rows: [{ label: 'Box + 4 books', segs: [{ u: 1.25, t: 'box', k: 'h', size: 14 }, { u: 1, t: Q, k: 'a' }, { u: 1, t: Q, k: 'a' }, { u: 1, t: Q, k: 'a' }, { u: 1, t: Q, k: 'a' }], brace: { from: 0, to: 5.25, t: '1 kg 50 g', pos: 'bottom' } }], unit: 90, labelW: 130, rowH: 30 }, 'A box of 250 g with four books; 1 kg 50 g altogether');
const l9c5 = () => bm({ y0: 10, rows: [
  { label: 'Full', segs: [{ u: 1, t: 'bottle', k: 'h', size: 14 }, { u: 1.5, t: 'water', k: 'b' }, { u: 1.5, t: 'water', k: 'b' }], brace: { from: 0, to: 4, t: '1 kg 200 g', pos: 'top' } },
  { label: 'Half poured out', segs: [{ u: 1, t: 'bottle', k: 'h', size: 14 }, { u: 1.5, t: 'water', k: 'b' }], brace: { from: 0, to: 2.5, t: '750 g', pos: 'bottom' } }], unit: 70, labelW: 130, rowH: 28, gap: 12 }, 'A bottle full of water and with half poured out');
const l9c6 = () => bm({ y0: 10, rows: [
  { label: '3 pens', segs: [{ u: 1, t: Q, k: 'a' }, { u: 1, t: Q, k: 'a' }, { u: 1, t: Q, k: 'a' }] },
  { label: '2 files', segs: [{ u: 1, t: Q, k: 'a' }, { u: .6, t: '60¢', k: 'h', size: 14 }, { u: 1, t: Q, k: 'a' }, { u: .6, t: '60¢', k: 'h', size: 14 }] }], vbrace: { from: 0, to: 1, t: '$9.20' }, unit: 80, rowH: 30, gap: 10 }, '3 pens and 2 files cost $9.20; a file costs 60 cents more than a pen');

// ---------------- Lesson 10 ----------------
const queue3 = () => { // a: Ben, 3rd from the front and 5th from the back
  let s = T(8, 18, 'front', 15, { a: 'start', c: TEAL, i: true }) + T(592, 18, 'back', 15, { a: 'end', c: TEAL, i: true });
  const r = 17, yA = 52, yB = 118, xB = 150;
  [1, 2].forEach((n, i) => { s += C(xB - (2 - i) * 46, yA, r, '#fff') + T(xB - (2 - i) * 46, yA + 36, n + (n === 1 ? 'st' : 'nd'), 14); });
  s += C(xB, yA, r, Y) + T(xB, yA + 6, 'Ben', 14, {}) + T(xB + 28, yA + 6, '3rd', 14, { a: 'start' });
  s += C(xB, yB, r, Y) + T(xB, yB + 6, 'Ben', 14, {}) + T(xB, yB + 36, '5th', 14);
  [4, 3, 2, 1].forEach((n, i) => { s += C(xB + (i + 1) * 46, yB, r, '#fff') + T(xB + (i + 1) * 46, yB + 36, n === 1 ? 'last' : n + (n === 2 ? 'nd' : n === 3 ? 'rd' : 'th'), 14); });
  s += L(xB, yA + 20, xB, yB - 20, { dash: true, sw: 2 });
  s += T(350, yA + 6, 'counting from the front', 15, { a: 'start', w: 600, c: '#44506F' }) + T(430, yB - 26, 'counting from the back', 15, { a: 'start', w: 600, c: '#44506F' });
  return W(svg(600, 160, s, 'Ben is 3rd from the front and 5th from the back: the two counts share Ben'), 0);
};
const queue3b = () => {
  let s = T(8, 18, 'front', 15, { a: 'start', c: TEAL, i: true }) + T(592, 18, 'back', 15, { a: 'end', c: TEAL, i: true });
  const r = 17, y = 56;
  s += C(50, y, r, '#fff') + C(110, y, r, Y) + T(110, y + 6, 'Ali', 14);
  s += R(150, y - 20, 300, 40, '#fff', { dash: true, sw: 2.4, rx: 10 }) + T(300, y + 6, '3 people between', 16, { c: TEAL });
  s += C(520, y, r, Y) + T(520, y + 6, 'Siti', 14);
  return W(svg(600, 90, s, 'Ali is 2nd from the front, 3 people are between Ali and Siti, and Siti is last'), 0);
};
// small item pictures for the shopping list (about 9 mm), shown above each name
const itemPic3 = (name) => {
  const k = {
    'Book': () => `<rect x="8" y="5" width="32" height="36" rx="3" fill="${BL}" stroke="${NAVY}" stroke-width="2.4"/><line x1="15" y1="5" x2="15" y2="41" stroke="${NAVY}" stroke-width="2"/><line x1="21" y1="16" x2="34" y2="16" stroke="${NAVY}" stroke-width="2"/><line x1="21" y1="24" x2="34" y2="24" stroke="${NAVY}" stroke-width="2"/>`,
    'Pen set': () => [10, 20, 30].map((x, i) => `<rect x="${x}" y="6" width="7" height="32" rx="2" fill="${[Y, RD, GR][i]}" stroke="${NAVY}" stroke-width="2"/><polygon points="${x},38 ${x + 7},38 ${x + 3.5},44" fill="${NAVY}"/>`).join(''),
    'Puzzle': () => `<path d="M8 10 H20 a5 5 0 1 1 8 0 H40 V22 a5 5 0 1 0 0 8 V40 H8 Z" fill="${GR}" stroke="${NAVY}" stroke-width="2.4" stroke-linejoin="round"/>`,
    'Stickers': () => `<polygon points="24,4 29,17 43,17 32,26 36,40 24,32 12,40 16,26 5,17 19,17" fill="${Y}" stroke="${NAVY}" stroke-width="2.4" stroke-linejoin="round"/>`,
    'Water bottle': () => `<rect x="17" y="3" width="14" height="7" rx="2" fill="#fff" stroke="${NAVY}" stroke-width="2.2"/><path d="M15 12 H33 V40 Q33 44 29 44 H19 Q15 44 15 40 Z" fill="${BL}" stroke="${NAVY}" stroke-width="2.4"/>`
  }[name];
  return k ? `<svg viewBox="0 0 48 48" width="34" height="34" xmlns="http://www.w3.org/2000/svg" aria-label="${name}" style="vertical-align:middle">${k()}</svg>` : '';
};
const l9c = () => bm({ rows: [{ label: '3 m 6 cm', segs: [{ u: 100, t: '1 m', k: 'a' }, { u: 100, t: '1 m', k: 'a' }, { u: 100, t: '1 m', k: 'a' }, { u: 22, t: '6', k: 'h', size: 14 }], brace: { from: 0, to: 322, t: '= ? cm', pos: 'top' } }], unit: 1.5, labelW: 96, rowH: 34, y0: 14 }, 'A bar for 3 m 6 cm: three 1 m pieces and 6 cm');
const clocks11 = () => { let s = ''; for (let k = 1; k <= 11; k++) { const col = (k - 1) % 6, row = Math.floor((k - 1) / 6), cx = 50 + col * 100, cy = 38 + row * 88; s += F.clockF(cx, cy, 33, k, 0, { numbers: false, minor: false }) + T(cx, cy + 53, k + ':00', 15); } return W(svg(600, 182, s, 'Eleven clock faces showing 1 o’clock to 11 o’clock'), 2); };
// base-ten blocks key: thousand cube, hundred flat, ten rod, one unit
const blocksKey = () => {
  let s = '', x = 10;
  // thousand: a cube drawn as front face + top + side
  s += R(x, 22, 46, 46, '#fff', { sw: 2.4 }) + P([[x, 22], [x + 14, 10], [x + 60, 10], [x + 46, 22]], '#F0F2F6', { sw: 2.2 }) + P([[x + 46, 22], [x + 60, 10], [x + 60, 56], [x + 46, 68]], '#DDE2EC', { sw: 2.2 });
  for (let i = 1; i < 10; i++) s += L(x + i * 4.6, 22, x + i * 4.6, 68, { sw: .6 }) + L(x, 22 + i * 4.6, x + 46, 22 + i * 4.6, { sw: .6 });
  s += T(x + 30, 90, '1 thousand', 15); x += 120;
  s += R(x, 22, 46, 46, '#fff', { sw: 2.4 }); for (let i = 1; i < 10; i++) s += L(x + i * 4.6, 22, x + i * 4.6, 68, { sw: .8 }) + L(x, 22 + i * 4.6, x + 46, 22 + i * 4.6, { sw: .8 });
  s += T(x + 23, 90, '1 hundred', 15); x += 110;
  s += R(x, 22, 9, 46, '#fff', { sw: 2.4 }); for (let i = 1; i < 10; i++) s += L(x, 22 + i * 4.6, x + 9, 22 + i * 4.6, { sw: .8 });
  s += T(x + 4, 90, '1 ten', 15); x += 90;
  s += R(x, 59, 9, 9, Y, { sw: 2.2 }); s += T(x + 4, 90, '1 one', 15);
  s += T(330, 52, '10 hundreds make 1 thousand', 15, { a: 'start', w: 600, i: true, c: '#44506F' });
  return W(svg(600, 100, s, 'Base-ten blocks: a thousand cube, a hundred flat, a ten rod and a one unit'), 2);
};
const FX = {
  '8.t3': clocks11,
  '4.4': l4q4, '4.5': l4q5, '4.6': l4q6, '4.t1': l4t1, '4.t2': l4t2, '4.t3': l4t3, '4.t4': l4t4, '4.c7': l4c7,
  '6.5': l6q5, '6.t2': l6t2, '6.t3': l6t3, '6.t4': l6t4, '6.c6': l6c6,
  '9.1f': ribbon3m, '9.4': l9q4, '9.5a': l9q5a, '9.5b': l9q5b, '9.5c': l9q5c, '9.6': l9q6, '9.t2': l9t2, '9.t3': l9t3, '9.c5': l9c5, '9.c6': l9c6,
  '10.3a': queue3, '10.3b': queue3b,
};
module.exports = { FX, itemPic3 };
