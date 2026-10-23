// Shared drawing helpers for the Level 1-3 holiday workbooks (hp/ = L1, p2/ = L2, p3/ = L3).
// Every function returns an SVG string (or an SVG fragment when the name ends in "F").
// House style: 1 SVG unit = about 0.26 mm on the printed page (the SVG is set to width:100%, max-width = viewBox width in px).
// So: icons >= 30 units (8 mm), text >= 15 units (about 11 pt), lines 2-3 units. Navy outlines; shading is ALWAYS
// backed by a label or a hatch so the black-and-white print still works (never colour alone).
const NAVY = '#1B2A49', Y = '#FFE08A', BL = '#CFE5F7', GR = '#CDEBD9', RD = '#F6B8B0', PALE = '#F4F6FA', TEAL = '#1F7A6F';
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const f1 = n => (Math.round(n * 10) / 10).toString();

const svg = (w, h, inner, label, maxw) =>
  `<svg aria-label="${esc(label || 'figure')}" viewBox="0 0 ${w} ${h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:${maxw || w}px;height:auto;display:inline-block" font-family="Nunito, Arial, sans-serif">` +
  `<defs>` +
  `<pattern id="hz" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="8" height="8" fill="#fff"/><line x1="0" y1="0" x2="0" y2="8" stroke="${NAVY}" stroke-width="2.2"/></pattern>` +
  `<pattern id="dt" width="8" height="8" patternUnits="userSpaceOnUse"><rect width="8" height="8" fill="#fff"/><circle cx="4" cy="4" r="1.6" fill="${NAVY}"/></pattern>` +
  `</defs>${inner}</svg>`;

const T = (x, y, s, size = 16, o = {}) =>
  `<text x="${f1(x)}" y="${f1(y)}" font-size="${size}" font-weight="${o.w || 700}" text-anchor="${o.a || 'middle'}" fill="${o.c || NAVY}"${o.i ? ' font-style="italic"' : ''}>${esc(s)}</text>`;
const R = (x, y, w, h, fill = '#fff', o = {}) =>
  `<rect x="${f1(x)}" y="${f1(y)}" width="${f1(w)}" height="${f1(h)}" fill="${fill}" stroke="${o.stroke || NAVY}" stroke-width="${o.sw || 2.5}"${o.dash ? ' stroke-dasharray="7 5"' : ''}${o.rx ? ` rx="${o.rx}"` : ''}/>`;
const L = (x1, y1, x2, y2, o = {}) => `<line x1="${f1(x1)}" y1="${f1(y1)}" x2="${f1(x2)}" y2="${f1(y2)}" stroke="${o.c || NAVY}" stroke-width="${o.sw || 2.5}"${o.dash ? ' stroke-dasharray="6 5"' : ''} stroke-linecap="round"/>`;
const C = (cx, cy, r, fill = '#fff', o = {}) => `<circle cx="${f1(cx)}" cy="${f1(cy)}" r="${f1(r)}" fill="${fill}" stroke="${o.stroke || NAVY}" stroke-width="${o.sw || 2.5}"${o.dash ? ' stroke-dasharray="5 4"' : ''}/>`;
const P = (pts, fill = '#fff', o = {}) => `<polygon points="${pts.map(p => f1(p[0]) + ',' + f1(p[1])).join(' ')}" fill="${fill}" stroke="${o.stroke || NAVY}" stroke-width="${o.sw || 2.5}" stroke-linejoin="round"/>`;
const arrowHead = (x, y, dir, s = 8, c = NAVY) => { // dir: 'r','l','d','u'
  const d = { r: [[x, y], [x - s, y - s * .6], [x - s, y + s * .6]], l: [[x, y], [x + s, y - s * .6], [x + s, y + s * .6]], d: [[x, y], [x - s * .6, y - s], [x + s * .6, y - s]], u: [[x, y], [x - s * .6, y + s], [x + s * .6, y + s]] }[dir];
  return `<polygon points="${d.map(p => f1(p[0]) + ',' + f1(p[1])).join(' ')}" fill="${c}"/>`;
};
// curved hop from (x1,y) to (x2,y) arching up by h, arrow head at the end, label above
const hopF = (x1, x2, y, h = 34, label = '', o = {}) => {
  const mx = (x1 + x2) / 2, c = o.c || NAVY;
  return `<path d="M${f1(x1)} ${f1(y)} Q${f1(mx)} ${f1(y - h * 2)} ${f1(x2)} ${f1(y - 2)}" fill="none" stroke="${c}" stroke-width="${o.sw || 2.6}"${o.dash ? ' stroke-dasharray="6 5"' : ''}/>` +
    arrowHead(x2, y - 2, 'd', 7, c) + (label ? T(mx, y - h - 6, label, o.size || 16, { c: o.lc || c }) : '');
};

// ---------------------------------------------------------------- small icons (centre cx,cy; size s = overall width)
const ICON = {
  star: (cx, cy, s, fill = Y) => { const pts = []; for (let i = 0; i < 10; i++) { const a = -Math.PI / 2 + i * Math.PI / 5, r = (i % 2 ? .22 : .5) * s; pts.push([cx + r * Math.cos(a), cy + r * Math.sin(a) * 1 + s * .03]); } return P(pts, fill, { sw: 2.2 }); },
  heart: (cx, cy, s, fill = RD) => { const k = s / 40; return `<path transform="translate(${f1(cx - 20 * k)},${f1(cy - 18 * k)}) scale(${k})" d="M20 36 C2 22 0 12 6 6 C12 0 19 3 20 10 C21 3 28 0 34 6 C40 12 38 22 20 36 Z" fill="${fill}" stroke="${NAVY}" stroke-width="${2.2 / k}" stroke-linejoin="round"/>`; },
  circle: (cx, cy, s, fill = '#fff') => C(cx, cy, s * .46, fill, { sw: 2.6 }),
  square: (cx, cy, s, fill = '#fff') => R(cx - s * .43, cy - s * .43, s * .86, s * .86, fill, { sw: 2.6 }),
  triangle: (cx, cy, s, fill = '#fff') => P([[cx, cy - s * .46], [cx + s * .5, cy + s * .4], [cx - s * .5, cy + s * .4]], fill, { sw: 2.6 }),
  dot: (cx, cy, s, fill = NAVY) => C(cx, cy, s * .3, fill, { sw: 2 }),
  ring: (cx, cy, s) => C(cx, cy, s * .3, '#fff', { sw: 2.4 }),
  cat: (cx, cy, s) => { const k = s / 40; return P([[cx - 17 * k, cy - 2 * k], [cx - 15 * k, cy - 20 * k], [cx - 3 * k, cy - 11 * k]], '#fff') + P([[cx + 17 * k, cy - 2 * k], [cx + 15 * k, cy - 20 * k], [cx + 3 * k, cy - 11 * k]], '#fff') + C(cx, cy + 3 * k, 17 * k, '#fff') + C(cx - 6 * k, cy, 2.2 * k, NAVY) + C(cx + 6 * k, cy, 2.2 * k, NAVY) + P([[cx, cy + 4 * k], [cx - 2.5 * k, cy + 7 * k], [cx + 2.5 * k, cy + 7 * k]], NAVY, { sw: 1 }) + L(cx - 6 * k, cy + 9 * k, cx - 19 * k, cy + 6 * k, { sw: 1.6 }) + L(cx - 6 * k, cy + 11 * k, cx - 19 * k, cy + 13 * k, { sw: 1.6 }) + L(cx + 6 * k, cy + 9 * k, cx + 19 * k, cy + 6 * k, { sw: 1.6 }) + L(cx + 6 * k, cy + 11 * k, cx + 19 * k, cy + 13 * k, { sw: 1.6 }); },
  dog: (cx, cy, s) => { const k = s / 40; return `<ellipse cx="${f1(cx - 17 * k)}" cy="${f1(cy + 1 * k)}" rx="${f1(6 * k)}" ry="${f1(12 * k)}" fill="${NAVY}"/><ellipse cx="${f1(cx + 17 * k)}" cy="${f1(cy + 1 * k)}" rx="${f1(6 * k)}" ry="${f1(12 * k)}" fill="${NAVY}"/>` + C(cx, cy + 1 * k, 15 * k, '#fff') + C(cx - 5.5 * k, cy - 3 * k, 2.2 * k, NAVY) + C(cx + 5.5 * k, cy - 3 * k, 2.2 * k, NAVY) + `<ellipse cx="${f1(cx)}" cy="${f1(cy + 6 * k)}" rx="${f1(6 * k)}" ry="${f1(4.5 * k)}" fill="#fff" stroke="${NAVY}" stroke-width="1.8"/>` + C(cx, cy + 4.5 * k, 2.2 * k, NAVY, { sw: 1 }); },
  fish: (cx, cy, s, fill = BL) => { const k = s / 40; return P([[cx + 10 * k, cy], [cx + 22 * k, cy - 11 * k], [cx + 22 * k, cy + 11 * k]], fill) + `<ellipse cx="${f1(cx - 3 * k)}" cy="${f1(cy)}" rx="${f1(16 * k)}" ry="${f1(11 * k)}" fill="${fill}" stroke="${NAVY}" stroke-width="2.4"/>` + C(cx - 10 * k, cy - 3 * k, 2.2 * k, NAVY, { sw: 1 }) + `<path d="M${f1(cx - 1 * k)} ${f1(cy - 6 * k)} Q${f1(cx + 3 * k)} ${f1(cy)} ${f1(cx - 1 * k)} ${f1(cy + 6 * k)}" fill="none" stroke="${NAVY}" stroke-width="1.8"/>`; },
  bird: (cx, cy, s, fill = Y) => { const k = s / 40; return P([[cx - 14 * k, cy - 2 * k], [cx - 23 * k, cy - 4 * k], [cx - 23 * k, cy + 8 * k]], fill) + `<ellipse cx="${f1(cx - 2 * k)}" cy="${f1(cy + 4 * k)}" rx="${f1(15 * k)}" ry="${f1(11 * k)}" fill="${fill}" stroke="${NAVY}" stroke-width="2.4"/>` + C(cx + 9 * k, cy - 7 * k, 8 * k, fill) + P([[cx + 16 * k, cy - 9 * k], [cx + 24 * k, cy - 6 * k], [cx + 16 * k, cy - 4 * k]], NAVY, { sw: 1 }) + C(cx + 10 * k, cy - 9 * k, 1.8 * k, NAVY, { sw: 1 }) + `<path d="M${f1(cx - 6 * k)} ${f1(cy + 2 * k)} Q${f1(cx)} ${f1(cy + 12 * k)} ${f1(cx + 6 * k)} ${f1(cy + 2 * k)}" fill="none" stroke="${NAVY}" stroke-width="1.8"/>`; },
  apple: (cx, cy, s) => { const k = s / 40; return `<path d="M${f1(cx)} ${f1(cy - 12 * k)} C${f1(cx - 8 * k)} ${f1(cy - 20 * k)} ${f1(cx - 21 * k)} ${f1(cy - 10 * k)} ${f1(cx - 18 * k)} ${f1(cy + 3 * k)} C${f1(cx - 15 * k)} ${f1(cy + 17 * k)} ${f1(cx - 6 * k)} ${f1(cy + 20 * k)} ${f1(cx)} ${f1(cy + 16 * k)} C${f1(cx + 6 * k)} ${f1(cy + 20 * k)} ${f1(cx + 15 * k)} ${f1(cy + 17 * k)} ${f1(cx + 18 * k)} ${f1(cy + 3 * k)} C${f1(cx + 21 * k)} ${f1(cy - 10 * k)} ${f1(cx + 8 * k)} ${f1(cy - 20 * k)} ${f1(cx)} ${f1(cy - 12 * k)} Z" fill="${RD}" stroke="${NAVY}" stroke-width="2.4"/>` + L(cx, cy - 12 * k, cx + 2 * k, cy - 21 * k, { sw: 2.4 }) + `<path d="M${f1(cx + 2 * k)} ${f1(cy - 17 * k)} Q${f1(cx + 11 * k)} ${f1(cy - 24 * k)} ${f1(cx + 14 * k)} ${f1(cy - 16 * k)} Q${f1(cx + 6 * k)} ${f1(cy - 12 * k)} ${f1(cx + 2 * k)} ${f1(cy - 17 * k)}" fill="${GR}" stroke="${NAVY}" stroke-width="1.8"/>`; },
  banana: (cx, cy, s) => { const k = s / 40; return `<path d="M${f1(cx - 19 * k)} ${f1(cy - 12 * k)} Q${f1(cx - 14 * k)} ${f1(cy + 18 * k)} ${f1(cx + 18 * k)} ${f1(cy + 8 * k)} L${f1(cx + 21 * k)} ${f1(cy + 2 * k)} Q${f1(cx - 3 * k)} ${f1(cy + 8 * k)} ${f1(cx - 11 * k)} ${f1(cy - 14 * k)} Z" fill="${Y}" stroke="${NAVY}" stroke-width="2.4" stroke-linejoin="round"/>` + L(cx - 19 * k, cy - 12 * k, cx - 21 * k, cy - 18 * k, { sw: 3 }); },
  orange: (cx, cy, s) => { const k = s / 40; return C(cx, cy + 1 * k, 17 * k, '#FFC27A') + `<path d="M${f1(cx - 4 * k)} ${f1(cy - 15 * k)} Q${f1(cx + 4 * k)} ${f1(cy - 24 * k)} ${f1(cx + 10 * k)} ${f1(cy - 16 * k)} Q${f1(cx + 2 * k)} ${f1(cy - 12 * k)} ${f1(cx - 4 * k)} ${f1(cy - 15 * k)}" fill="${GR}" stroke="${NAVY}" stroke-width="1.8"/>` + C(cx - 6 * k, cy - 2 * k, 1.2 * k, NAVY, { sw: 1 }) + C(cx + 5 * k, cy + 4 * k, 1.2 * k, NAVY, { sw: 1 }) + C(cx - 2 * k, cy + 9 * k, 1.2 * k, NAVY, { sw: 1 }); },
  grape: (cx, cy, s) => { const k = s / 40, d = [[-9, -8], [0, -8], [9, -8], [-4.5, 0], [4.5, 0], [0, 8]]; return d.map(p => C(cx + p[0] * k, cy + p[1] * k + 1 * k, 5.6 * k, '#D9C2F0', { sw: 1.9 })).join('') + L(cx, cy - 14 * k, cx + 2 * k, cy - 20 * k, { sw: 2.2 }) + `<path d="M${f1(cx + 2 * k)} ${f1(cy - 17 * k)} Q${f1(cx + 11 * k)} ${f1(cy - 22 * k)} ${f1(cx + 13 * k)} ${f1(cy - 15 * k)} Q${f1(cx + 6 * k)} ${f1(cy - 13 * k)} ${f1(cx + 2 * k)} ${f1(cy - 17 * k)}" fill="${GR}" stroke="${NAVY}" stroke-width="1.6"/>`; },
  melon: (cx, cy, s) => { const k = s / 40; return `<path d="M${f1(cx - 21 * k)} ${f1(cy - 6 * k)} A${f1(21 * k)} ${f1(21 * k)} 0 0 0 ${f1(cx + 21 * k)} ${f1(cy - 6 * k)} Z" fill="${RD}" stroke="${NAVY}" stroke-width="2.4" stroke-linejoin="round"/><path d="M${f1(cx - 18 * k)} ${f1(cy - 6 * k)} A${f1(18 * k)} ${f1(18 * k)} 0 0 0 ${f1(cx + 18 * k)} ${f1(cy - 6 * k)}" fill="none" stroke="${NAVY}" stroke-width="3.2" stroke-dasharray="1 0"/>` + `<path d="M${f1(cx - 21 * k)} ${f1(cy - 6 * k)} A${f1(21 * k)} ${f1(21 * k)} 0 0 0 ${f1(cx + 21 * k)} ${f1(cy - 6 * k)}" fill="none" stroke="${NAVY}" stroke-width="2.4"/>` + [[-8, 1], [0, 4], [8, 1], [-3, 9], [4, 9]].map(p => `<ellipse cx="${f1(cx + p[0] * k)}" cy="${f1(cy + p[1] * k)}" rx="${f1(1.6 * k)}" ry="${f1(2.4 * k)}" fill="${NAVY}"/>`).join(''); },
  duck: (cx, cy, s) => ICON.bird(cx, cy, s, Y),
  // coloured counters that still read in black and white: a letter inside
  red: (cx, cy, s) => C(cx, cy, s * .44, RD, { sw: 2.6 }) + T(cx, cy + s * .16, 'R', s * .46, { w: 800 }),
  blue: (cx, cy, s) => C(cx, cy, s * .44, BL, { sw: 2.6 }) + T(cx, cy + s * .16, 'B', s * .46, { w: 800 }),
  green: (cx, cy, s) => C(cx, cy, s * .44, GR, { sw: 2.6 }) + T(cx, cy + s * .16, 'G', s * .46, { w: 800 }),
};
// icon by name; "half" draws the left half only (clipped) with a dashed right edge
const icon = (name, cx, cy, s, o = {}) => {
  const f = ICON[name]; if (!f) throw new Error('no icon ' + name);
  if (!o.half) return f(cx, cy, s);
  const id = 'h' + Math.round(cx * 7 + cy * 13 + s);
  return `<clipPath id="${id}"><rect x="${f1(cx - s)}" y="${f1(cy - s)}" width="${f1(s)}" height="${f1(s * 2)}"/></clipPath><g clip-path="url(#${id})">${f(cx, cy, s)}</g>` + L(cx, cy - s * .55, cx, cy + s * .55, { sw: 1.6, dash: true });
};

// ---------------------------------------------------------------- coins and notes (values printed with cents)
const COIN = { 5: { r: 17, f: '#F1F3F6' }, 10: { r: 19, f: '#F1F3F6' }, 20: { r: 21.5, f: '#F1F3F6' }, 50: { r: 24.5, f: '#F1F3F6' }, 100: { r: 27, f: '#FBF0C4' } };
const coinF = (v, cx, cy, o = {}) => {
  const d = COIN[v]; const r = (o.r || d.r), lab = v >= 100 ? '$' + v / 100 : v + '¢';
  if (o.empty) return C(cx, cy, r, '#fff', { dash: true, sw: 2.2 }) + (o.q ? T(cx, cy + 6, '?', 18, { c: '#8A94AD' }) : '');
  return C(cx, cy, r, d.f, { sw: 2.6 }) + C(cx, cy, r - 3.6, 'none', { sw: 1.1 }) + T(cx, cy + (v >= 100 ? 6 : 5.5), lab, v >= 50 || v === 20 ? 16 : 14.5, { w: 800 });
};
const coinRow = (vals, o = {}) => { // horizontal row of coins; returns svg
  const gap = o.gap || 10, h = o.h || 52; let x = 6, inner = '';
  vals.forEach(v => { const r = (v === '?' ? 22 : COIN[v].r); inner += v === '?' ? coinF(20, x + r, h / 2, { empty: true, q: true, r }) : coinF(v, x + r, h / 2); x += 2 * r + gap; });
  return svg(Math.max(x, 60), h, inner, o.label || 'coins', o.maxw || x);
};
const NOTE = { 1: ['#E9F4EA', '$1'], 2: ['#F6E1E1', '$2'], 5: ['#E1F1EC', '$5'], 10: ['#F6E3E3', '$10'], 50: ['#E3E8F6', '$50'] };
const noteF = (v, x, y, w = 92, h = 46, o = {}) => {
  const d = NOTE[v];
  return R(x, y, w, h, d ? d[0] : '#fff', { sw: 2.4, rx: 3 }) + R(x + 5, y + 5, w - 10, h - 10, 'none', { sw: 1.1 }) + T(x + w / 2, y + h / 2 + 8, '$' + v, 22, { w: 800 });
};

// ---------------------------------------------------------------- number line (labels >= 15 units), hops above, optional frog
const frogF = (cx, cy, s = 40) => { const k = s / 40; return `<ellipse cx="${f1(cx)}" cy="${f1(cy)}" rx="${f1(16 * k)}" ry="${f1(12 * k)}" fill="${GR}" stroke="${NAVY}" stroke-width="2.4"/>` + C(cx - 8 * k, cy - 11 * k, 5.5 * k, '#fff', { sw: 2 }) + C(cx + 8 * k, cy - 11 * k, 5.5 * k, '#fff', { sw: 2 }) + C(cx - 8 * k, cy - 11 * k, 1.8 * k, NAVY, { sw: 1 }) + C(cx + 8 * k, cy - 11 * k, 1.8 * k, NAVY, { sw: 1 }) + `<path d="M${f1(cx - 7 * k)} ${f1(cy + 2 * k)} Q${f1(cx)} ${f1(cy + 8 * k)} ${f1(cx + 7 * k)} ${f1(cy + 2 * k)}" fill="none" stroke="${NAVY}" stroke-width="1.8"/>`; };
// opts: min,max,step,W (svg width), pad, labelEvery, hops:[{from,to,label,dash}], marks:[{v,kind:'dot'|'x'|'ring'}], frog:v, hopH, h
const numberLineF = (o, y0) => {
  const min = o.min, max = o.max, W = o.W || 600, pad = o.pad || 22, n = max - min, dx = (W - 2 * pad) / n;
  const X = v => pad + (v - min) * dx; let s = L(pad - 8, y0, W - pad + 8, y0, { sw: 3 }) + arrowHead(W - pad + 12, y0, 'r', 9);
  for (let v = min; v <= max; v += (o.step || 1)) {
    const big = (v - min) % (o.labelEvery || 1) === 0;
    s += L(X(v), y0 - (big ? 8 : 5), X(v), y0 + (big ? 8 : 5), { sw: big ? 2.6 : 2 });
    if (big) s += T(X(v), y0 + 28, o.fmt ? o.fmt(v) : v, o.size || 16);
  }
  (o.hops || []).forEach(h => { s += hopF(X(h.from), X(h.to), y0 - 10, h.h || Math.min(46, 14 + (h.to - h.from) * dx * .22), h.label || '', { dash: h.dash, size: 15 }); });
  (o.marks || []).forEach(m => { const x = X(m.v); s += m.kind === 'x' ? L(x - 7, y0 - 24, x + 7, y0 - 10, { sw: 3 }) + L(x + 7, y0 - 24, x - 7, y0 - 10, { sw: 3 }) : m.kind === 'ring' ? C(x, y0 - 16, 8, '#fff', { sw: 2.6 }) : C(x, y0 - 16, 7, NAVY); });
  if (o.frog !== undefined) s += frogF(X(o.frog), y0 - 22, 34);
  return s;
};

// ---------------------------------------------------------------- bar model
// rows: [{label, segs:[{u, t, k}], brace:{from,to,t,pos}, tail:'?'}]; k: 'a' yellow, 'b' blue, 'h' hatch, 'd' dashed empty, 'w' white
// opts: unit (px per unit), labelW, rowH, gap, x0 ; segs may carry {u,t,k,sub} ; top braces drawn above, bottom braces below
const SEGFILL = { a: Y, b: BL, g: GR, h: 'url(#hz)', dt: 'url(#dt)', w: '#fff', d: '#fff' };
const barModelF = (o, y0) => {
  const unit = o.unit || 40, lw = o.labelW === undefined ? 70 : o.labelW, rh = o.rowH || 44, gap = o.gap || 26, x0 = o.x0 === undefined ? lw + 6 : o.x0;
  let s = '', y = y0, maxX = 0;
  (o.rows || []).forEach(r => {
    if (r.brace && r.brace.pos === 'top') y += 30;
    const top = y; let x = x0 + (r.indent || 0) * unit;
    if (r.label) s += T(x0 - 8, top + rh / 2 + 6, r.label, 17, { a: 'end' });
    (r.segs || []).forEach(g => {
      const w = g.u * unit;
      s += R(x, top, w, rh, SEGFILL[g.k || 'w'], { dash: g.k === 'd', sw: 2.6 });
      if (g.t !== undefined && g.t !== '') s += (g.k === 'h' || g.k === 'dt' ? `<rect x="${f1(x + w / 2 - (String(g.t).length * 5 + 6))}" y="${f1(top + rh / 2 - 13)}" width="${f1(String(g.t).length * 10 + 12)}" height="26" fill="#fff" rx="4"/>` : '') + T(x + w / 2, top + rh / 2 + 6, g.t, g.size || 17);
      x += w;
    });
    if (r.tail) s += T(x + 10, top + rh / 2 + 7, r.tail, 22, { a: 'start', c: TEAL });
    maxX = Math.max(maxX, x);
    if (r.brace) {
      const b = r.brace, bx0 = x0 + (r.indent || 0) * unit + b.from * unit, bx1 = x0 + (r.indent || 0) * unit + b.to * unit, up = b.pos === 'top', yb = up ? top - 4 : top + rh + 4, d = up ? -13 : 13, m = (bx0 + bx1) / 2;
      s += `<path d="M${f1(bx0)} ${f1(yb)} Q${f1(bx0)} ${f1(yb + d)} ${f1(bx0 + 12)} ${f1(yb + d)} L${f1(m - 12)} ${f1(yb + d)} Q${f1(m)} ${f1(yb + d)} ${f1(m)} ${f1(yb + 2 * d)} Q${f1(m)} ${f1(yb + d)} ${f1(m + 12)} ${f1(yb + d)} L${f1(bx1 - 12)} ${f1(yb + d)} Q${f1(bx1)} ${f1(yb + d)} ${f1(bx1)} ${f1(yb)}" fill="none" stroke="${NAVY}" stroke-width="2.4"/>`;
      if (b.t) s += T(m, up ? yb + 2 * d - 6 : yb + 2 * d + 19, b.t, 18, { c: b.c || TEAL });
      if (!up) y += b.t ? 52 : 34;
    }
    y += rh + gap;
  });
  return { s, y: y - gap, maxX };
};
// full svg for a bar model
const barModel = (o) => {
  const W = o.W || 600, r = barModelF(o, o.y0 || 8), h = r.y + (o.pad || 14);
  return svg(W, h, r.s + (o.extra ? o.extra(r) : ''), o.label || 'bar model');
};

// ---------------------------------------------------------------- picture row: items with place numbers below
// items: [name|null|'?'], dashed empty box when null or '?'
const pictureRowF = (o, y0) => {
  const s = o.size || 42, pitch = o.pitch || s + 12, x0 = o.x0 === undefined ? 12 : o.x0; let out = '';
  (o.items || []).forEach((it, i) => {
    const cx = x0 + pitch * i + pitch / 2, cy = y0 + s / 2 + 4;
    if (it === null || it === '?') out += R(cx - s / 2, cy - s / 2, s, s, '#fff', { dash: true, sw: 2.2, rx: 5 }) + (it === '?' ? T(cx, cy + 7, '?', 22, { c: '#8A94AD' }) : '');
    else if (typeof it === 'string' && it.startsWith('=')) out += T(cx, cy + 9, it.slice(1), 30, { w: 800 });  // letter tiles: '=A'
    else if (typeof it === 'string' && it.startsWith('#')) { const nm = it.slice(1); out += R(cx - s / 2, cy - s / 2, s, s, Y, { sw: 2.4, rx: 6 }) + T(cx, cy + 9, nm, 28, { w: 800 }); }
    else if (it && typeof it === 'object') out += icon(it.k, cx, cy, s, it);
    else out += icon(it, cx, cy, s);
    if (o.numbers !== false) out += T(cx, cy + s / 2 + 22, (o.start || 1) + i, 16, { c: NAVY });
  });
  if (o.answer) { const ax = (o.x0 === undefined ? 12 : o.x0) + pitch * o.items.length + 14; out += T(ax, y0 + s / 2 + 12, 'Answer:', 17, { a: 'start' }) + L(ax + 74, y0 + s / 2 + 14, ax + 74 + (o.answerW || 70), y0 + s / 2 + 14, { sw: 2, dash: true }); }
  return out;
};
const pictureRow = (o) => {
  const s = o.size || 42, pitch = o.pitch || s + 12, W = (o.x0 === undefined ? 12 : o.x0) * 2 + pitch * o.items.length + (o.answer ? 20 + 74 + (o.answerW || 70) : 0), H = s + 6 + (o.numbers === false ? 6 : 26);
  return svg(W, H, pictureRowF(o, 2), o.label || 'picture row', W);
};

// ---------------------------------------------------------------- picture graph (pictograph): rows [{name, n, icon}], key text, optional half
const pictographF = (o, y0) => {
  const s = o.size || 36, pitch = s + 6, lw = o.labelW || 130, rh = s + (o.rowPad === undefined ? 12 : o.rowPad); let out = '';
  o.rows.forEach((r, i) => {
    const y = y0 + i * rh, cy = y + rh / 2;
    out += R(0, y, lw, rh, '#EDEDED', { sw: 2 }) + T(lw / 2, cy + 6, r.name, 17) + R(lw, y, pitch * (o.maxN || 9) + 14, rh, '#fff', { sw: 2 });
    for (let k = 0; k < Math.floor(r.n); k++) out += icon(r.icon || o.icon, lw + 10 + pitch * k + pitch / 2, cy, s);
    if (r.n % 1) out += icon(r.icon || o.icon, lw + 10 + pitch * Math.floor(r.n) + pitch / 2, cy, s, { half: true });
    if (r.blank) out += T(lw + 14, cy + 6, r.blank, 15, { a: 'start', i: true, c: '#8A94AD' });
  });
  if (o.keyRight) { const kx = lw + pitch * (o.maxN || 9) + 30, kh = 74, ky = y0 + o.rows.length * rh / 2 - kh / 2;
    out += R(kx, ky, 128, kh, '#FFF4D1', { sw: 2, rx: 6 }) + T(kx + 64, ky + 22, 'Key', 17) + icon(o.icon || o.rows[0].icon, kx + 30, ky + 50, 30) + T(kx + 52, ky + 56, '= ' + o.key, 16, { a: 'start' });
    return { s: out, h: y0 + o.rows.length * rh + 4 }; }
  if (o.noKey) return { s: out, h: y0 + o.rows.length * rh + 4 };
  const ky = y0 + o.rows.length * rh + (o.keyGap === undefined ? 12 : o.keyGap), kh = o.keyH || 50, kc = ky + kh / 2;
  out += R(0, ky, lw + pitch * (o.maxN || 9) + 14, kh, '#FFF4D1', { sw: 2, rx: 6 }) + T(14, kc + 6, 'Key:', 17, { a: 'start' }) + icon(o.icon || o.rows[0].icon, 92, kc, Math.min(32, kh - 8)) + T(116, kc + 6, '= ' + o.key, 17, { a: 'start' });
  if (o.halfKey) out += icon(o.icon || o.rows[0].icon, 262, kc, Math.min(32, kh - 8), { half: true }) + T(284, kc + 6, '= ' + o.halfKey, 17, { a: 'start' });
  return { s: out, h: ky + kh + 4 };
};
const pictograph = (o) => {
  const W = (o.labelW || 130) + (36 + 6) * 0 + ((o.size || 36) + 6) * (o.maxN || 9) + 18, r = pictographF(o, 4);
  return svg(W, r.h + 2, r.s, o.label || 'picture graph', W);
};

// ---------------------------------------------------------------- clock face (>= 35 mm: r >= 66 units). Hour hand short and thick, minute hand long and thin.
const clockF = (cx, cy, r, h, m, o = {}) => {
  let s = C(cx, cy, r, '#fff', { sw: 3.2 });
  for (let i = 0; i < 60; i++) { const a = i * Math.PI / 30, big = i % 5 === 0, r1 = r - (big ? 10 : 5); s += L(cx + r1 * Math.sin(a), cy - r1 * Math.cos(a), cx + (r - 2) * Math.sin(a), cy - (r - 2) * Math.cos(a), { sw: big ? 2.4 : 1.2 }); }
  if (o.numbers !== false) for (let i = 1; i <= 12; i++) { const a = i * Math.PI / 6, rr = r - 24; s += T(cx + rr * Math.sin(a), cy - rr * Math.cos(a) + 6, i, Math.max(15, r * .2)); }
  if (h !== null) {
    const ha = ((h % 12) + m / 60) * Math.PI / 6, ma = m * Math.PI / 30;
    s += L(cx, cy, cx + r * .5 * Math.sin(ha), cy - r * .5 * Math.cos(ha), { sw: 6 }) + L(cx, cy, cx + r * .78 * Math.sin(ma), cy - r * .78 * Math.cos(ma), { sw: 3 });
  }
  return s + C(cx, cy, 4, NAVY);
};

// ---------------------------------------------------------------- time line (minutes since midnight), ticks with labels, optional jumps
// o: t0,t1 (minutes), W, ticks:[{t,label,big}], jumps:[{from,to,label}], marks:[{t,label}], fmt(t)
const timeLineF = (o, y0) => {
  const W = o.W || 600, pad = o.pad || 26, dx = (W - 2 * pad) / (o.t1 - o.t0), X = t => pad + (t - o.t0) * dx;
  let s = L(pad - 10, y0, W - pad + 10, y0, { sw: 3 }) + arrowHead(W - pad + 14, y0, 'r', 9);
  (o.ticks || []).forEach(k => { s += L(X(k.t), y0 - (k.big === false ? 6 : 10), X(k.t), y0 + (k.big === false ? 6 : 10), { sw: 2.6 }) + (k.label !== undefined ? T(X(k.t), y0 + 30, k.label, o.size || 16) : ''); });
  (o.jumps || []).forEach(j => { s += hopF(X(j.from), X(j.to), y0 - 10, j.h || 36, j.label || '', { size: 15, dash: j.dash }); });
  (o.marks || []).forEach(m => { s += C(X(m.t), y0, 6, NAVY) + (m.label ? T(X(m.t), y0 - 16, m.label, 15, { c: TEAL }) : ''); });
  return s;
};

// ---------------------------------------------------------------- ruler: [min,max] cm, object bars drawn above (start NOT always 0)
const rulerF = (o, y0) => {
  const W = o.W || 600, pad = 26, n = o.max - o.min, dx = (W - 2 * pad) / n, X = v => pad + (v - o.min) * dx, h = 46;
  let s = R(pad - 12, y0, W - 2 * pad + 24, h, '#FFF4D1', { sw: 2.6 });
  for (let v = o.min; v <= o.max; v++) { s += L(X(v), y0, X(v), y0 + 14, { sw: 2.2 }); s += T(X(v), y0 + 36, v, 17); if (v < o.max) s += L(X(v) + dx / 2, y0, X(v) + dx / 2, y0 + 8, { sw: 1.4 }); }
  return s;
};
const barsOnRulerF = (items, o, y0) => { // items: [{from,to,label,fill}] drawn above ruler top at y0
  const W = o.W || 600, pad = 26, dx = (W - 2 * pad) / (o.max - o.min), X = v => pad + (v - o.min) * dx; let s = '';
  items.forEach((it, i) => { const y = y0 - (items.length - i) * 34; s += R(X(it.from), y, (it.to - it.from) * dx, 26, it.fill || Y, { sw: 2.4, rx: 4 }) + T(X(it.from) + (it.to - it.from) * dx / 2, y + 19, it.label || '', 16); });
  return s;
};

module.exports = { NAVY, Y, BL, GR, RD, PALE, TEAL, esc, f1, svg, T, R, L, C, P, arrowHead, hopF, ICON, icon, COIN, coinF, coinRow, noteF, frogF, numberLineF, barModelF, barModel, pictureRowF, pictureRow, pictographF, pictograph, clockF, timeLineF, rulerF, barsOnRulerF };
