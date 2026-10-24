// Level 1 (P1) holiday workbook: figures built from hp/figs_l1_3.js. Each function returns an HTML block (centred SVG).
const F = require('./figs_l1_3.js');
const { svg, T, R, L, C, P, icon, coinF, noteF, numberLineF, barModelF, pictureRowF, pictographF, NAVY, Y, BL, GR, RD, TEAL } = F;
const W = (s, mt = 0) => `<div class="p img" style="text-align:center;margin:${mt}px 0 2px">${s}</div>`;

// L1 No.3: frog hops on two big number lines (0-20). First hop of the 4s is drawn as the model; line 2 is empty for the 5s.
const frogLines = () => {
  const line = (frogHop) => numberLineF({ min: 0, max: 20, W: 600, labelEvery: 1, size: 17, hops: frogHop ? [{ from: 0, to: 4, label: '4', h: 26 }] : [], frog: 0 }, 50);
  return W(svg(600, 80, line(true), 'Number line 0 to 20 with a frog on 0 and its first hop of 4'), 0) + W(svg(600, 80, line(false), 'Empty number line 0 to 20 with a frog on 0'), 0);
};

// L1 No.5: boxes of stickers (stars). Box 1 has 2, Box 2 has 5, boxes 3 and 4 are empty to draw in.
const stickerBoxes = () => {
  const bw = 112, bh = 84, gap = 40, x0 = 14, y0 = 30; let s = '';
  const pos = [[0, 0], [1, 0], [2, 0], [0, 1], [1, 1]];
  [2, 5, null, null].forEach((n, i) => {
    const x = x0 + i * (bw + gap);
    s += T(x + bw / 2, y0 - 8, 'Box ' + (i + 1), 17) + R(x, y0, bw, bh, n === null ? '#fff' : '#FFF9E8', { dash: n === null, sw: 2.6, rx: 8 });
    if (n === null) s += T(x + bw / 2, y0 + bh / 2 + 5, 'draw here', 15, { w: 600, c: '#44506F', i: true });
    else for (let k = 0; k < n; k++) s += icon('star', x + 22 + pos[k][0] * 34 + (n === 2 ? 17 : 0), y0 + 26 + pos[k][1] * 38 - (n === 2 ? -10 : 0), 32);
    if (i < 3) { const xa = x + bw + 6, xb = x + bw + gap - 6; s += L(xa, y0 + bh / 2, xb, y0 + bh / 2, { sw: 2.6 }) + F.arrowHead(xb + 3, y0 + bh / 2, 'r', 8) + T((xa + xb) / 2, y0 + bh / 2 - 8, '+3', 17, { c: TEAL }); }
  });
  return W(svg(4 * bw + 3 * gap + 28, y0 + bh + 10, s, 'Boxes of stickers: box 1 has 2 stars, box 2 has 5 stars, boxes 3 and 4 are empty'), 4);
};

// pattern rows
const row = (items, o = {}) => W(svg((o.x0 === undefined ? 12 : o.x0) * 2 + (o.pitch || (o.size || 40) + 12) * items.length + (o.answer ? 20 + 74 + (o.answerW || 70) : 0), (o.size || 40) + 34, pictureRowF({ items, ...o }, 2), o.label || 'pattern row'), 2);
const pat = (core, len) => Array.from({ length: len }, (_, i) => core[i % core.length]);
const blanks = n => Array(n).fill('?');
// No.4: circle, star, square repeating, places 1-8 shown and 9-12 empty
const p4 = () => row([...pat(['circle', 'star', 'square'], 8), ...blanks(4)], { size: 32, pitch: 46, label: 'A repeating pattern of shapes, places 1 to 8 shown, 9 to 12 empty' });
const p1 = () => row([...pat(['circle', 'triangle', 'square'], 7), '?', '?'], { size: 34, pitch: 48, label: 'Shape pattern circle triangle square, places 8 and 9 empty' });
// No.2: circle, square, triangle, circle, square, triangle, circle, then empty to place 10
const p2 = () => row([...pat(['circle', 'square', 'triangle'], 7), ...blanks(3)], { size: 32, pitch: 42, answer: true, answerW: 80, label: 'Shape pattern, 7 shown and places 8 to 10 empty' });
const p3 = () => row([...pat(['red', 'red', 'blue'], 7), ...blanks(1)], { size: 32, pitch: 42, answer: true, answerW: 80, label: 'Counter pattern red red blue, 7 shown and place 8 empty' });
const p5 = () => row([...pat(['cat', 'dog', 'dog'], 7), ...blanks(5)], { size: 38, pitch: 48, label: 'Animal pattern cat dog dog, 7 shown and places 8 to 12 empty' });
const p6 = () => row([...['=A', '=B', '=C', '=D', '=A', '=B', '=C'].map(x => '#' + x[1]), ...blanks(4)], { size: 38, pitch: 48, label: 'Letter tiles A B C D A B C then empty places 8 to 11' });
// Think harder T1: circle, triangle, triangle, square (2 cores shown + places to 14 empty); T3: red blue blue x2 shown
const t1 = () => row([...pat(['circle', 'triangle', 'triangle', 'square'], 8), ...blanks(6)], { size: 32, pitch: 41, x0: 8, label: 'Shape pattern, 8 shown and 6 empty places' });
const t3 = () => row(pat(['red', 'blue', 'blue'], 6), { size: 34, pitch: 44, label: 'Beads red blue blue red blue blue' });
// squares made of sticks: 1, 2, 3 squares
const stickSquares = () => {
  const u = 34; let s = '', x = 14; const stick = (x1, y1, x2, y2) => L(x1, y1, x2, y2, { sw: 6, c: '#B8860B' }) + L(x1, y1, x2, y2, { sw: 2.2, c: NAVY });
  [1, 2, 3].forEach(k => {
    const x0 = x, y0 = 12;
    for (let i = 0; i <= k; i++) s += stick(x0 + i * u, y0, x0 + i * u, y0 + u);
    for (let i = 0; i < k; i++) s += stick(x0 + i * u, y0, x0 + (i + 1) * u, y0) + stick(x0 + i * u, y0 + u, x0 + (i + 1) * u, y0 + u);
    s += T(x0 + k * u / 2, y0 + u + 26, k + (k > 1 ? ' squares' : ' square'), 16);
    x += k * u + 46;
  });
  return W(svg(x, 90, s, 'Squares in a row made with sticks: 1, 2 and 3 squares'), 2);
};
// dots 1, 3, 6, 10, 15 (triangles of dots)
const dotTriangles = () => {
  let s = '', x = 14; const d = 17;
  [1, 2, 3, 4, 5].forEach(k => {
    const w = k * d;
    for (let r = 0; r < k; r++) for (let c = 0; c <= r; c++) s += C(x + (k - 1 - r) * d / 2 + c * d + d / 2, 12 + r * d + d / 2, 6, NAVY, { sw: 1 });
    s += T(x + w / 2, 12 + k * d + 24, [1, 3, 6, 10, 15][k - 1], 16);
    x += w + 26;
  });
  return W(svg(x, 12 + 5 * d + 34, s, 'Dots in triangles: 1, 3, 6, 10 and 15'), 2);
};

// ---- coins ----
const coinCell = (v, label) => `<div style="text-align:center">${svg(50, 46, coinF(v, 25, 23), v + ' cent coin', 50)}<div style="font-size:12px;font-weight:700">${label}</div></div>`;
const coinsRow = (vals, o = {}) => W(F.coinRow(vals, o), 2);
// No.3: purse strip for 85¢
const purse = () => W(svg(560, 90, coinTrayInner([5, 10, 20, 50], 6, 8) + R(10, 62, 540, 24, '#fff', { dash: true, sw: 2.4, rx: 8 }) + T(280, 79, 'My 85¢ purse: place coins here', 15, { w: 600, c: '#44506F', i: true }), 'Tray with a 5, 10, 20 and 50 cent coin and an empty purse for 85 cents'), 2);
function coinTrayInner(vals, x, y) { let s = '', cx = x; vals.forEach(v => { const r = F.COIN[v].r; s += coinF(v, cx + r + 4, y + 26 + 0); cx += 2 * r + 14; }); return s; }
const trayRow = (vals, extra = '') => W(svg(560, 52, coinTrayInner(vals, 6, -1) + extra, 'Coins: ' + vals.join(', ') + ' cents'), 2);
const benTwo = () => {
  let s = coinTrayInner([5, 10, 20, 50], 6, 4);
  s += T(380, 36, 'Two coins:', 16, { a: 'end' }) + coinF(20, 410, 31, { empty: true, q: true }) + T(443, 38, '+', 24) + coinF(20, 476, 31, { empty: true, q: true }) + T(510, 38, '= 35¢ ?', 17, { a: 'start' });
  return W(svg(580, 64, s, 'Coin tray and two empty coins for the 35 cent question'), 2);
};

// ---- picture graphs ----
const FRUIT = [['Apple', 6, 'apple'], ['Banana', 5, 'banana'], ['Orange', 8, 'orange'], ['Grape', 3, 'grape'], ['Watermelon', 5, 'melon']];
const fruitGraph = () => { const o = { rows: FRUIT.map(r => ({ name: r[0], n: r[1], icon: r[2] })), key: '1 child', maxN: 8, size: 30, labelW: 124, rowPad: 5, keyH: 40, keyGap: 8 }; const r = pictographF(o, 3); return W(svg(124 + 37 * 8 + 18, r.h + 2, r.s, 'Picture graph of fruit votes, one picture for each child'), 2); };
const PETS = [['Dog', 4, 'dog'], ['Cat', 7, 'cat'], ['Fish', 3, 'fish'], ['Bird', 5, 'bird']];
const petGraph = () => { const o = { rows: PETS.map(r => ({ name: r[0], n: r[1], icon: r[2] })), key: '1 pet', maxN: 7, size: 30, gap: 12, labelW: 80, rowPad: 3, keyRight: true }; const r = pictographF(o, 3); return W(svg(80 + 42 * 7 + 18 + 150, r.h + 2, r.s, 'Picture graph of pets in a street, one picture for each pet'), 2); };
// Think harder: 1 picture = 2 children. Red 3, Blue 5, Green 4.
const starGraph = () => {
  const o = { rows: [{ name: 'Red', n: 3, icon: 'star' }, { name: 'Blue', n: 5, icon: 'star' }, { name: 'Green', n: 4, icon: 'star' }], key: '2 children', halfKey: '1 child', maxN: 6, size: 30, labelW: 80, rowPad: 3, keyH: 36, keyGap: 6 };
  const r = pictographF(o, 3); return W(svg(400, r.h + 2, r.s, 'Picture graph: one star is 2 children, half a star is 1 child'), 2);
};
const blankRow = (name) => { const o = { rows: [{ name, n: 0, icon: 'star' }], noKey: true, key: '2 children', maxN: 6, size: 30, rowPad: 4, labelW: 80 }; const r = pictographF(o, 3); return W(svg(80 + 38 * 6 + 18, r.h + 2, r.s, 'Empty row for ' + name + ' with the key one star is 2 children'), 2); };
const appleRow = () => { const o = { rows: [{ name: 'Apple', n: 3.5, icon: 'star' }], noKey: true, key: '2 children', maxN: 5, size: 30, rowPad: 4, labelW: 80 }; const r = pictographF(o, 3); return W(svg(80 + 38 * 5 + 18, r.h + 2, r.s, 'Apple row: 3 stars and half a star; one star is 2 children'), 2); };

// ---- L9 ----
// No.4: 1 clip = 2 erasers
const clipEraser = () => {
  const o = { unit: 36, labelW: 76, rowH: 34, gap: 14, rows: [
    { label: '1 clip', segs: [{ u: 2, t: 'clip', k: 'a' }] },
    { label: '2 erasers', segs: [{ u: 1, t: 'e', k: 'b', size: 14 }, { u: 1, t: 'e', k: 'b', size: 14 }] },
    { label: 'desk', segs: [1, 2, 3, 4, 5].map(() => ({ u: 2, t: 'clip', k: 'a' })), tail: '? erasers' },
    { label: 'pencil', segs: Array.from({ length: 12 }, () => ({ u: 1, t: 'e', k: 'b', size: 14 })), tail: '? clips' }] };
  const r = barModelF(o, 4); return W(svg(600, r.y + 8, r.s, 'One clip is as long as two erasers. A desk of 5 clips. A pencil of 12 erasers.'), 4);
};
// No.5: pencils in cubes, same baseline
const pencilCubes = () => {
  const u = 36, x0 = 70; let s = '', y = 4; const cube = (x, yy, k) => R(x, yy, u, 30, k === 'd' ? '#fff' : Y, { dash: k === 'd', sw: 2.4 });
  [['Mei', 8, 0], ['Ali', 8, 3], ['Ben', 6, 2]].forEach(([nm, n, extra]) => {
    s += T(x0 - 8, y + 21, nm, 17, { a: 'end' });
    for (let i = 0; i < n; i++) s += cube(x0 + i * u, y, 'a');
    for (let i = 0; i < extra; i++) s += cube(x0 + (n + i) * u, y, 'd');
    if (nm === 'Ali') s += T(x0 + (n + extra / 2) * u, y + 52, '3 longer', 15, { c: TEAL });
    if (nm === 'Ben') s += T(x0 + (n + extra / 2) * u, y + 52, '2 shorter than Mei', 15, { c: TEAL, a: 'start' }).replace(/x="[\d.]+"/, `x="${x0 + n * u + 6}"`);
    y += nm === 'Mei' ? 40 : 60;
  });
  return W(svg(520, y + 14, s, 'Mei: 8 cubes. Ali: 8 cubes and 3 more. Ben: 6 cubes and 2 fewer than Mei.'), 4);
};
const ruler6 = () => { // L9 No.6: ruler 0-12 with pencil from 0 to 12 and crayon from 3 to 8
  const items = [{ from: 3, to: 8, label: 'crayon', fill: GR }, { from: 0, to: 12, label: 'pencil', fill: Y }];
  const r = F.rulerF({ min: 0, max: 12, W: 600 }, 84) + F.barsOnRulerF(items, { min: 0, max: 12, W: 600 }, 84);
  return W(svg(600, 138, r, 'A ruler from 0 to 12 centimetres with a pencil from 0 and a crayon from 3'), 2);
};

// L5 No.4a: a queue of 20 (front on the left), Mei's place marked
const queue20 = () => {
  const s0 = 28, pitch = 33; let o = '';
  for (let r = 0; r < 2; r++) for (let i = 0; i < 10; i++) {
    const n = r * 10 + i + 1, cx = 40 + i * pitch * 1.5 + 0, cy = 38 + r * 52;
    o += C(cx, cy, s0 / 2, n === 7 ? Y : '#fff', { sw: 2.4 }) + T(cx, cy + 27, n, 14, { c: '#44506F' });
    if (n === 7) o += T(cx, cy + 6, 'Mei', 14, { w: 800 });
  }
  o += T(10, 14, 'front', 15, { a: 'start', c: TEAL, i: true });
  return W(svg(560, 126, o, 'A queue of 20 children in two rows of 10, numbered 1 to 20 from the front; Mei is the 7th'), 2);
};
// L2 No.6: two bars, one is 2 more, total 10
const bars10 = () => { const r = barModelF({ unit: 40, labelW: 90, rowH: 34, gap: 14, rows: [{ label: 'smaller', segs: [{ u: 3, t: '?', k: 'a' }] }, { label: 'bigger', segs: [{ u: 3, t: '?', k: 'a' }, { u: 1, t: '2', k: 'h' }] }], vbrace: { from: 0, to: 1, t: '10 altogether' } }, 4); return W(svg(520, r.y + 6, r.s, 'Two bars: the bigger number is 2 more than the smaller; together 10'), 2); };
// number machine strip: cells [{t, k:'q'|'op'|'out'}]
const machine = (cells) => {
  let s = '', x = 6; const w = 86, h = 46, gap = 34;
  cells.forEach((c, i) => {
    s += R(x, 10, w, h, c.k === 'q' ? Y : c.k === 'out' ? BL : '#EDEDED', { sw: 2.6, rx: 6 }) + T(x + w / 2, 10 + h / 2 + 9, c.t, 26, { w: 800 });
    if (i < cells.length - 1) s += L(x + w + 4, 33, x + w + gap - 8, 33, { sw: 2.6 }) + F.arrowHead(x + w + gap - 4, 33, 'r', 8);
    x += w + gap;
  });
  return W(svg(x - gap + 12, 66, s, 'A number machine strip: ' + cells.map(c => c.t).join(', ')), 2);
};
const mT1 = () => machine([{ t: '?', k: 'q' }, { t: '− 5', k: 'op' }, { t: '+ 3', k: 'op' }, { t: '12', k: 'out' }]);
const mT2 = () => machine([{ t: '?', k: 'q' }, { t: '− 6', k: 'op' }, { t: '+ 4', k: 'op' }, { t: '− 3', k: 'op' }, { t: '10', k: 'out' }]);
// C2 snail: a wall scale 0..9 cm, drawn tall
const snailWall = () => {
  let s = '', y0 = 236, k = 21; s += R(60, y0 - 9 * k, 56, 9 * k, '#F4F1E8', { sw: 2.6 });
  for (let v = 0; v <= 9; v++) { s += L(52, y0 - v * k, 116, y0 - v * k, { sw: v % 3 ? 1.4 : 2.4 }) + T(40, y0 - v * k + 6, v, 16, { a: 'end' }); }
  s += T(88, y0 - 9 * k - 10, 'top', 15, { c: TEAL }) + T(88, y0 + 20, 'bottom', 15, { c: TEAL });
  s += `<ellipse cx="150" cy="${y0 - 12}" rx="26" ry="14" fill="${GR}" stroke="${NAVY}" stroke-width="2.4"/>` + C(150, y0 - 14, 8, '#fff', { sw: 2.4 }) + T(150, y0 - 10, '·', 20) + L(172, y0 - 22, 184, y0 - 38, { sw: 2.4 }) + C(184, y0 - 40, 3, NAVY, { sw: 1 });
  s += T(210, y0 - 100, 'The snail starts at the bottom.', 16, { a: 'start', w: 600 }) + T(210, y0 - 76, 'Day: up 3 cm.   Night: back 1 cm.', 16, { a: 'start', w: 600 });
  return W(svg(520, y0 + 30, s, 'A wall 9 cm high with a scale from 0 to 9 and a snail at the bottom'), 2);
};
// L6 T5: dollar notes and price tags
const dollars = () => {
  let s = '', x = 6; [[2], [5], [10], [50]].forEach(([v], i) => { s += noteF(v, x, 4, 84, 40); x += 94; }); s += coinF(100, x + 22, 26); s += T(x + 54, 32, '= $1 coin', 15, { a: 'start', w: 600 });
  const tag = (x0, nm, pr) => P([[x0 + 14, 58], [x0 + 130, 58], [x0 + 130, 94], [x0 + 14, 94], [x0, 76]], Y, { sw: 2.4 }) + C(x0 + 14, 76, 4, '#fff', { sw: 1.6 }) + T(x0 + 74, 74, nm, 14, {}) + T(x0 + 74, 90, pr, 17, {});
  return W(svg(590, 52, s, 'Dollar notes of 2, 5, 10 and 50, a 1 dollar coin, and price tags: toy 17 dollars, bicycle 65 dollars, helmet 8 dollars'), 2);
};
// extra (Think harder / Go further) figures by '<lesson>.<T|C><n>'
const FX = {
  '3.T1': Object.assign(() => starGraph(), { lines: 1 }),
  '3.T2': Object.assign(() => '', { lines: 1 }),
  '3.T3': Object.assign(() => blankRow('Pizza'), { lines: 1 }),
  '3.T4': Object.assign(() => appleRow(), { lines: 1 }),
  '4.T1': Object.assign(() => t1(), { lines: 1 }),
  '4.T2': Object.assign(() => '', { lines: 2 }),
  '4.T3': Object.assign(() => t3(), { lines: 1 }),
  '4.T4': Object.assign(() => stickSquares(), { lines: 1 }),
  '4.C2': Object.assign(() => dotTriangles(), { lines: 3 }),
  '6.T2': Object.assign(() => '', { lines: 1 }),
  '6.T3': Object.assign(() => '', { lines: 1 }),
  '5.T1': Object.assign(() => mT1(), { lines: 1 }),
  '5.T2': Object.assign(() => mT2(), { lines: 1 }),
  '5.C2': Object.assign(() => snailWall(), { lines: 2 }),
};
module.exports = { bars10, dollars, p1, queue20, FX, frogLines, stickerBoxes, p2, p3, p4, p5, p6, t1, t3, stickSquares, dotTriangles, coinCell, coinsRow, purse, trayRow, benTwo, fruitGraph, petGraph, starGraph, blankRow, appleRow, clipEraser, pencilCubes, ruler6, W };
