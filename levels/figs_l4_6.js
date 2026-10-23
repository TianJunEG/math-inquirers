'use strict';
// Shared figure helpers for the Level 4, 5 and 6 holiday workbooks (CommonJS, returns SVG strings for H.fig).
// Rules (docs/audit_final/diagrams_holiday.md): text >= 9 pt when printed on A4, shapes large, shading that survives black and white
// (hatching plus a label, never colour alone), figures never print the answer.
//
//   fit(svg, level)   enlarge an existing figure so its smallest text prints at >= 9 pt (used by every H.fig in p4, p5, p6)
//   barModel(spec)    bars in units with braces, "?" boxes, overhangs, before/after rows
//   numberLine(spec)  ticks with labels, marks, arcs; the line does not have to start at 0
//   clockFace(spec)   analogue clock with hour and minute hands, optional sector arc
//   queueRow(spec)    row of numbered circles (queues)
//   grid(spec)        sample-space grids (rows x cols with headers)
//   dotPlot(spec)     dot plot on a number line
//   lineGraph(spec)   line graph with a legible scale
//   angleArms(spec)   angle with long arms and a vertex dot (for the protractor)
//   ringClock(spec)   modular circle with n points
const N = '#1B2A49', Y = '#FFC93C', SKY = '#DDEBF7', TEAL = '#1F7A6F', RED = '#D64545', WH = '#FFFFFF', GR = '#5B6785';
const F = 'Fredoka, Arial, sans-serif';

const T = (x, y, s, o = {}) =>
  `<text x="${r2(x)}" y="${r2(y)}" font-size="${o.size || 17}" font-weight="${o.weight || 700}" text-anchor="${o.anchor || 'middle'}" fill="${o.fill || N}" font-family="${F}">${s}</text>`;
function r2(v) { return Math.round(v * 100) / 100; }
const L = (x1, y1, x2, y2, o = {}) =>
  `<line x1="${r2(x1)}" y1="${r2(y1)}" x2="${r2(x2)}" y2="${r2(y2)}" stroke="${o.c || N}" stroke-width="${o.w || 3}"${o.dash ? ` stroke-dasharray="${o.dash}"` : ''}${o.cap ? ' stroke-linecap="round"' : ''}/>`;
const R = (x, y, w, h, o = {}) =>
  `<rect x="${r2(x)}" y="${r2(y)}" width="${r2(w)}" height="${r2(h)}" fill="${o.fill || WH}" stroke="${o.c || N}" stroke-width="${o.w || 3}"${o.rx ? ` rx="${o.rx}"` : ''}${o.dash ? ` stroke-dasharray="${o.dash}"` : ''}/>`;
const C = (x, y, r, o = {}) =>
  `<circle cx="${r2(x)}" cy="${r2(y)}" r="${r}" fill="${o.fill || WH}" stroke="${o.c || N}" stroke-width="${o.w || 3}"/>`;
const DEFS = `<defs><pattern id="mi-hatch" width="9" height="9" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="9" height="9" fill="${Y}"/><line x1="0" y1="0" x2="0" y2="9" stroke="${N}" stroke-width="2"/></pattern>` +
  `<pattern id="mi-dots" width="8" height="8" patternUnits="userSpaceOnUse"><rect width="8" height="8" fill="${SKY}"/><circle cx="4" cy="4" r="1.6" fill="${N}"/></pattern></defs>`;
const svg = (vw, vh, inner, label, width) =>
  `<svg aria-label="${label.replace(/"/g, '&quot;')}" viewBox="0 0 ${vw} ${vh}" width="${width || Math.round(vw * 0.75)}" xmlns="http://www.w3.org/2000/svg" style="max-width:100%">${DEFS}${inner}</svg>`;

// ---------------------------------------------------------------------------------------------------------------------------------
// fit: make sure the smallest text in a figure prints at >= minPt (default 9) on the A4 print.
// Scale from CSS px to printed pt: 0.75 (px to pt) x 0.943 (print gutter shrink); Level 5's page is laid out 850 px wide and shrunk by 0.81.
const fit = (s, level, opt = {}) => {
  const minPt = opt.minPt || 9.2, k = 0.75 * 0.943 * (level === 5 ? 0.81 : 1);
  const maxW = opt.maxW || (level === 5 ? 790 : 650);
  const m = s.match(/<svg[^>]*>/);
  if (!m) return s;
  const tag = m[0];
  const vb = tag.match(/viewBox="[\d.-]+ [\d.-]+ ([\d.]+) ([\d.]+)"/);
  if (!vb) return s;
  const vw = +vb[1];
  const wm = tag.match(/ width="([\d.]+)"/);
  const sm = tag.match(/style="[^"]*?(?:^|;|")width:\s*([\d.]+)px/) || tag.match(/style="width:\s*([\d.]+)px/);
  const w0 = wm ? +wm[1] : sm ? +sm[1] : vw;
  let fs = [...s.matchAll(/font-size[=:]\s*"?([\d.]+)/g)].map(x => +x[1]);
  if (!fs.length) return s;
  // ignore a single tiny decorative glyph? no: every text counts
  const mn = Math.min(...fs);
  const need = minPt / (mn * k) * vw;
  const w = Math.min(maxW, Math.max(w0, Math.ceil(need)));
  if (w === w0) return s;
  let tag2 = wm ? tag.replace(/ width="[\d.]+"/, ` width="${w}"`) : tag.replace('<svg', `<svg width="${w}"`);
  if (sm) tag2 = tag2.replace(/width:\s*[\d.]+px/, `width:${w}px`);
  return s.replace(tag, tag2);
};

// ---------------------------------------------------------------------------------------------------------------------------------
// barModel
// spec: { w=600, unit (px per unit; default fits), left=120 (label column), rows:[{name, off=0, segs:[{u, t, f}], note}], notes:[...], label }
//   seg.f: 'plain' | 'shade' (hatched) | 'blank' (dashed outline: "draw it") | 'unk' (white with ? )
//   annotations (spec.ann): {k:'brace', row, from, to, side:'top'|'bottom', t}   brace over/under units from..to of a row
//                           {k:'dim', row, from, to, t}                          double-headed arrow below the row (an overhang)
//                           {k:'vline', from, to rows, at}                        dashed vertical line at unit position
//                           {k:'txt', row, at, t, dx, dy}
const barModel = (spec) => {
  const w = spec.w || 600, left = spec.left === undefined ? 112 : spec.left, rowH = spec.rowH || 46;
  const maxU = Math.max(...spec.rows.map(r => (r.off || 0) + r.segs.reduce((a, s) => a + s.u, 0)));
  const U = spec.unit || (w - left - (spec.right || 20)) / maxU;
  const ann = spec.ann || [];
  const topPad = (row) => ann.some(a => a.k === 'brace' && a.row === row && (a.side || 'top') === 'top') ? 58 : 8;
  const botPad = (row) => ann.some(a => (a.k === 'brace' && a.row === row && a.side === 'bottom') || (a.k === 'dim' && a.row === row)) ? 62 : 8;
  let y = 6; const ys = [];
  spec.rows.forEach((r, i) => { y += topPad(i); ys[i] = y; y += rowH + botPad(i); });
  const h = Math.ceil(y);
  let s = '';
  spec.rows.forEach((r, i) => {
    const y0 = ys[i];
    if (r.name) s += T(left - 12, y0 + rowH / 2 + 6, r.name, { size: 18, anchor: 'end' });
    let x = left + (r.off || 0) * U;
    r.segs.forEach(sg => {
      const f = sg.f || 'plain', wd = sg.u * U;
      const fill = f === 'shade' ? 'url(#mi-hatch)' : f === 'dots' ? 'url(#mi-dots)' : WH;
      s += R(x, y0, wd, rowH, { fill, dash: f === 'blank' ? '8 6' : '', w: 3 });
      if (sg.t !== undefined && sg.t !== '') {
        const bg = f === 'shade' || f === 'dots';
        if (bg) s += `<rect x="${r2(x + wd / 2 - (String(sg.t).length * 5.5 + 7))}" y="${r2(y0 + rowH / 2 - 14)}" width="${r2(String(sg.t).length * 11 + 14)}" height="28" rx="6" fill="#fff"/>`;
        s += T(x + wd / 2, y0 + rowH / 2 + 7, sg.t, { size: sg.size || 19 });
      }
      x += wd;
    });
    if (r.note) s += T(x + 12, y0 + rowH / 2 + 7, r.note, { size: 18, anchor: 'start', fill: TEAL });
  });
  ann.forEach(a => {
    const y0 = ys[a.row === undefined ? 0 : a.row];
    const rr = spec.rows[a.row === undefined ? 0 : a.row];
    const xa = left + ((rr.off || 0) + (a.from || 0)) * U, xb = left + ((rr.off || 0) + (a.to || 0)) * U, xm = (xa + xb) / 2;
    if (a.k === 'brace') {
      const top = (a.side || 'top') === 'top';
      const yb = top ? y0 - 8 : y0 + rowH + 8, d = top ? -1 : 1;
      s += `<path d="M${r2(xa)} ${r2(yb)} q0 ${12 * d} 12 ${12 * d} L${r2(xm - 12)} ${r2(yb + 12 * d)} q12 0 12 ${12 * d} q0 ${-12 * d} 12 ${-12 * d} L${r2(xb - 12)} ${r2(yb + 12 * d)} q12 0 12 ${-12 * d}" fill="none" stroke="${N}" stroke-width="3"/>`;
      s += T(xm, top ? yb - 36 : yb + 44, a.t, { size: a.size || 19, fill: a.fill || TEAL });
    } else if (a.k === 'dim') {
      const yb = y0 + rowH + 22;
      s += L(xa, yb, xb, yb, { w: 3, c: RED }) + `<polygon points="${r2(xa)},${yb} ${r2(xa + 11)},${yb - 7} ${r2(xa + 11)},${yb + 7}" fill="${RED}"/><polygon points="${r2(xb)},${yb} ${r2(xb - 11)},${yb - 7} ${r2(xb - 11)},${yb + 7}" fill="${RED}"/>`;
      s += L(xa, y0 + rowH, xa, yb + 8, { w: 2, c: RED, dash: '4 3' }) + L(xb, y0 + rowH, xb, yb + 8, { w: 2, c: RED, dash: '4 3' });
      s += T(xm, yb + 28, a.t, { size: 18, fill: RED });
    } else if (a.k === 'rbrace') {   // vertical brace on the right spanning rows r1..r2 (at = unit position of the right end of the bars)
      const x = left + a.at * U + 14, ya = ys[a.r1] , yb = ys[a.r2] + rowH, ym = (ya + yb) / 2;
      s += `<path d="M${r2(x)} ${r2(ya)} q12 0 12 12 L${r2(x + 12)} ${r2(ym - 12)} q0 12 12 12 q-12 0 -12 12 L${r2(x + 12)} ${r2(yb - 12)} q0 12 -12 12" fill="none" stroke="${N}" stroke-width="3"/>`;
      s += T(x + 32, ym + 7, a.t, { size: a.size || 19, fill: a.fill || TEAL, anchor: 'start' });
    } else if (a.k === 'vline') {
      const ya = ys[a.r1 || 0] - 6, yb2 = ys[a.r2 === undefined ? spec.rows.length - 1 : a.r2] + rowH + 6, x = left + a.at * U;
      s += L(x, ya, x, yb2, { w: 2.5, dash: '7 5', c: GR });
    } else if (a.k === 'txt') {
      s += T(left + ((rr.off || 0) + (a.at || 0)) * U + (a.dx || 0), y0 + (a.dy === undefined ? -10 : a.dy), a.t, { size: a.size || 18, fill: a.fill || TEAL, anchor: a.anchor || 'middle' });
    }
  });
  return svg(w, h, s, spec.label || 'A bar model', spec.width);
};

// ---------------------------------------------------------------------------------------------------------------------------------
// numberLine: {w=600, h, min, max, major, minor (tick step; default major), x0=36, x1=w-36, fmt(v)->string, labelEvery (major steps, default 1),
//   hideLabels:[v], marks:[{v, t (label above), k:'dot'|'arrow'|'x'|'box'}], arcs:[{a,b,t,dir:'up'|'down'}], label, y}
const numberLine = (sp) => { const r = lineParts(sp); return svg(r.w, r.h, r.inner, sp.label || 'A number line', sp.width); };
// stackSvg: several figure parts ({inner,h}) one under the other in one svg
const stackSvg = (parts, label, w = 600, width) => {
  let y = 0, s = '';
  parts.forEach(p => { s += `<g transform="translate(0 ${y})">${p.inner}</g>`; y += p.h + (p.gap === undefined ? 0 : p.gap); });
  return svg(w, y, s, label, width);
};
const lineParts = (sp) => {
  const w = sp.w || 600, x0 = sp.x0 === undefined ? 40 : sp.x0, x1 = sp.x1 === undefined ? w - 40 : sp.x1;
  const top = sp.top === undefined ? ((sp.marks || []).some(m => m.t) || (sp.arcs || []).some(a => (a.dir || 'up') === 'up') ? 50 : 18) : sp.top;
  const y = top + 14, h = sp.h || (y + 46);
  const sx = v => x0 + (v - sp.min) / (sp.max - sp.min) * (x1 - x0);
  const fmt = sp.fmt || (v => String(v));
  let s = L(x0 - 14, y, x1 + 14, y, { w: 3.5 });
  s += `<polygon points="${x1 + 20},${y} ${x1 + 8},${y - 7} ${x1 + 8},${y + 7}" fill="${N}"/>`;
  const major = sp.major, minor = sp.minor || sp.major, eps = 1e-9;
  const nMinor = Math.round((sp.max - sp.min) / minor);
  for (let i = 0; i <= nMinor; i++) {
    const v = sp.min + i * minor, x = sx(v);
    const isMaj = Math.abs(((v - sp.min) / major) - Math.round((v - sp.min) / major)) < 1e-6;
    s += L(x, y - (isMaj ? 15 : 9), x, y + (isMaj ? 15 : 9), { w: isMaj ? 3.5 : 2.5 });
    const idx = Math.round((v - sp.min) / major);
    const show = isMaj && idx % (sp.labelEvery || 1) === 0 && !(sp.hideLabels || []).some(q => Math.abs(q - v) < 1e-9);
    if (show || (sp.showLabels || []).some(q => Math.abs(q - v) < 1e-9)) s += T(x, y + 36, fmt(v), { size: sp.size || 18 });
  }
  (sp.arcs || []).forEach(a => {
    const xa = sx(a.a), xb = sx(a.b), up = (a.dir || 'up') === 'up', hh = 30, d = up ? -1 : 1, yy = y + d * 18;
    s += `<path d="M${r2(xa)} ${yy} Q${r2((xa + xb) / 2)} ${yy + d * hh * 1.6} ${r2(xb)} ${yy}" fill="none" stroke="${TEAL}" stroke-width="3"/>`;
    s += `<polygon points="${r2(xb)},${yy} ${r2(xb - 9)},${yy + d * 4 - 3 * d} ${r2(xb - 3)},${yy + d * 11}" fill="${TEAL}"/>`;
    if (a.t) s += T((xa + xb) / 2, yy + d * (hh * 0.8 + 12) + (up ? 0 : 14), a.t, { size: 18, fill: TEAL });
  });
  (sp.marks || []).forEach(m => {
    const x = sx(m.v), k = m.k || 'arrow';
    if (k === 'x') s += L(x - 9, y - 9, x + 9, y + 9, { w: 4, c: RED }) + L(x - 9, y + 9, x + 9, y - 9, { w: 4, c: RED });
    else if (k === 'dot') s += C(x, y, 8, { fill: Y });
    else if (k === 'box') s += R(x - 22, y - 56, 44, 34, { w: 3, dash: '5 3' }) + L(x, y - 22, x, y - 10, { w: 2.5 });
    else {
      s += `<circle cx="${r2(x)}" cy="${y - 38}" r="15" fill="${Y}" stroke="${N}" stroke-width="3"/>` + T(x, y - 32, m.t || '', { size: 19 });
      s += L(x, y - 23, x, y - 16, { w: 3, c: TEAL }) + `<polygon points="${r2(x)},${y - 8} ${r2(x - 7)},${y - 18} ${r2(x + 7)},${y - 18}" fill="${TEAL}"/>`;
    }
    if (m.t && k !== 'arrow') s += T(x, y - 28, m.t, { size: 18, fill: TEAL });
  });
  if (sp.tag) s += T(8, y + 7, sp.tag, { size: 19, fill: TEAL, anchor: 'start' });
  return { inner: s, w, h };
};

// ---------------------------------------------------------------------------------------------------------------------------------
// clockFace: {cx, cy, r, h, m (minutes 0-59; hour hand moves with the minutes), numerals=true, noHands, sector:{from,to (clock degrees from 12, clockwise)}, label letter}
const clockInner = (sp) => {
  const cx = sp.cx, cy = sp.cy, r = sp.r;
  let s = C(cx, cy, r, { fill: WH, w: 4 });
  if (sp.sector) {
    const a = sp.sector.from, b = sp.sector.to, rr = sp.sector.r || r * 0.55;
    const P = (d, rad) => [cx + rad * Math.sin(d * Math.PI / 180), cy - rad * Math.cos(d * Math.PI / 180)];
    const [xa, ya] = P(a, rr), [xb, yb] = P(b, rr);
    s += `<path d="M${r2(cx)} ${r2(cy)} L${r2(xa)} ${r2(ya)} A${rr} ${rr} 0 ${((b - a + 360) % 360) > 180 ? 1 : 0} 1 ${r2(xb)} ${r2(yb)} Z" fill="url(#mi-hatch)" stroke="${N}" stroke-width="2"/>`;
  }
  for (let i = 0; i < 60; i++) {
    const a = i * 6 * Math.PI / 180, big = i % 5 === 0;
    if (!big && r < 55) continue;
    const r1 = r - (big ? 11 : 5);
    s += L(cx + r1 * Math.sin(a), cy - r1 * Math.cos(a), cx + (r - 2) * Math.sin(a), cy - (r - 2) * Math.cos(a), { w: big ? 3 : 1.5 });
  }
  if (sp.numerals !== false) for (let i = 1; i <= 12; i++) {
    const a = i * 30 * Math.PI / 180, rr = r - 27 * Math.max(0.7, Math.min(1.1, r / 80));
    s += T(cx + rr * Math.sin(a), cy - rr * Math.cos(a) + 6, i, { size: Math.max(16, r * 0.2) });
  }
  if (!sp.noHands) {
    const mm = sp.m || 0, hh = sp.h || 0;
    const ha = ((hh % 12) + mm / 60) * 30 * Math.PI / 180, ma = mm * 6 * Math.PI / 180;
    s += L(cx, cy, cx + r * 0.5 * Math.sin(ha), cy - r * 0.5 * Math.cos(ha), { w: 8, cap: true });
    s += L(cx, cy, cx + r * 0.78 * Math.sin(ma), cy - r * 0.78 * Math.cos(ma), { w: 4, cap: true, c: RED });
  }
  s += C(cx, cy, 5, { fill: N, w: 1 });
  return s;
};
const clockFace = (sp) => {
  const r = sp.r || 70, w = sp.w || r * 2 + 20, h = sp.h2 || r * 2 + 20;
  return svg(w, h, clockInner({ cx: w / 2, cy: h / 2, r, h: sp.h, m: sp.m, numerals: sp.numerals, noHands: sp.noHands, sector: sp.sector }), sp.label || 'A clock face', sp.width);
};
// several clocks side by side: items [{h,m,cap,noHands,sector}]
const clocks = (items, o = {}) => {
  const r = o.r || 78, gap = o.gap || 30, cw = r * 2 + gap, w = Math.max(items.length * cw, 120), capH = 34;
  let s = '';
  items.forEach((c, i) => {
    const cx = i * cw + cw / 2, cy = r + 12;
    s += clockInner({ cx, cy, r, h: c.h, m: c.m, noHands: c.noHands, sector: c.sector });
    if (c.cap) s += T(cx, cy + r + 30, c.cap, { size: 19 });
  });
  return svg(w, r * 2 + 24 + capH, s, o.label || 'Clock faces', o.width || w);
};

// ---------------------------------------------------------------------------------------------------------------------------------
// queueRow: n circles numbered 1..n, optional marked {i:'Mei'} and braces
const queueRow = (sp) => {
  const n = sp.n, w = sp.w || 600, rr = Math.min(19, (w - 40) / n / 2 - 2), step = (w - 40) / n;
  const y = sp.y || 70;
  let s = '';
  for (let i = 0; i < n; i++) {
    const x = 20 + step * (i + 0.5), mk = sp.marks && sp.marks[i + 1];
    s += C(x, y, rr, { fill: mk ? Y : WH, w: mk ? 4 : 3 });
    s += T(x, y + 6, i + 1, { size: 15 });
    if (mk) s += T(x, y - rr - 10, mk, { size: 18, fill: TEAL });
  }
  s += T(20, y + rr + 28, sp.front || 'FRONT', { size: 16, anchor: 'start', fill: GR }) + T(w - 20, y + rr + 28, sp.back || 'BACK', { size: 16, anchor: 'end', fill: GR });
  return svg(w, y + rr + 40, s, sp.label || 'A queue', sp.width);
};

// ---------------------------------------------------------------------------------------------------------------------------------
// grid: sample-space grid. {rows:[labels], cols:[labels], rowTitle, colTitle, cell (px), fill(i,j)->text}
const grid = (sp) => {
  const nr = sp.rows.length, nc = sp.cols.length, cell = sp.cell || 56, lx = 96, ty = 66;
  const w = lx + nc * cell + 20, h = ty + nr * cell + 14;
  let s = '';
  if (sp.colTitle) s += T(lx + nc * cell / 2, 22, sp.colTitle, { size: 18, fill: TEAL });
  if (sp.rowTitle) s += `<text transform="translate(18 ${ty + nr * cell / 2}) rotate(-90)" font-size="18" font-weight="700" text-anchor="middle" fill="${TEAL}" font-family="${F}">${sp.rowTitle}</text>`;
  sp.cols.forEach((c, j) => { s += R(lx + j * cell, ty - 36, cell, 34, { fill: SKY, w: 2.5 }) + T(lx + j * cell + cell / 2, ty - 12, c, { size: 19 }); });
  sp.rows.forEach((rr, i) => {
    s += R(lx - 46, ty + i * cell, 46, cell, { fill: SKY, w: 2.5 }) + T(lx - 23, ty + i * cell + cell / 2 + 7, rr, { size: 19 });
    sp.cols.forEach((c, j) => {
      const tx = sp.fill ? sp.fill(i, j) : '';
      const hi = sp.hi && sp.hi(i, j);
      s += R(lx + j * cell, ty + i * cell, cell, cell, { fill: hi ? 'url(#mi-hatch)' : WH, w: 2.5 });
      if (tx !== '' && tx !== undefined) s += (hi ? `<rect x="${lx + j * cell + cell / 2 - 17}" y="${ty + i * cell + cell / 2 - 14}" width="34" height="26" rx="5" fill="#fff"/>` : '') + T(lx + j * cell + cell / 2, ty + i * cell + cell / 2 + 7, tx, { size: 19 });
    });
  });
  return svg(w, h, s, sp.label || 'A grid', sp.width);
};

// ---------------------------------------------------------------------------------------------------------------------------------
// dotPlot: {min, max, data:[...], fmt, meanLine (value), label}. Each value stacks dots.
const dotPlot = (sp) => {
  const w = sp.w || 600, x0 = 40, x1 = w - 40, step = (x1 - x0) / (sp.max - sp.min);
  const counts = {}; (sp.data || []).forEach(v => counts[v] = (counts[v] || 0) + 1);
  const maxc = Math.max(1, ...Object.values(counts)), rr = Math.min(15, step / 2 - 2), top = 28 + maxc * (rr * 2 + 4), y = top + 6;
  let s = L(x0 - 10, y, x1 + 10, y, { w: 3.5 });
  for (let v = sp.min; v <= sp.max; v += (sp.tick || 1)) {
    const x = x0 + (v - sp.min) * step;
    s += L(x, y - 8, x, y + 10, { w: 3 }) + T(x, y + 34, sp.fmt ? sp.fmt(v) : v, { size: 18 });
  }
  Object.keys(counts).forEach(k => { for (let i = 0; i < counts[k]; i++) s += C(x0 + (k - sp.min) * step, y - 14 - rr - i * (rr * 2 + 4), rr, { fill: Y, w: 2.5 }); });
  if (sp.meanLine !== undefined) { const xm = x0 + (sp.meanLine - sp.min) * step; s += L(xm, 14, xm, y + 4, { w: 3, dash: '8 5', c: RED }) + T(xm, 12, sp.meanText || 'mean', { size: 17, fill: RED }); }
  if (sp.axis) s += T(w / 2, y + 66, sp.axis, { size: 17, fill: GR });
  return svg(w, y + (sp.axis ? 76 : 50), s, sp.label || 'A dot plot', sp.width);
};

// ---------------------------------------------------------------------------------------------------------------------------------
// angleArms: draws angle ABC style: vertex at (x,y), first arm along base direction a0 (deg, anti-clockwise from east), second at a0+ang.
// items [{ang, a0, len, tag}] in one figure; positions in a row.
const angleFig = (items, o = {}) => {
  const len = o.len || 120, cw = o.cw || (len * 1.3 + 40), w = items.length * cw + 20, h = o.h || len * 1.05 + 60;
  let s = '';
  items.forEach((it, i) => {
    const x = 20 + i * cw + 16, y = h - 34, a0 = (it.a0 || 0) * Math.PI / 180, a1 = ((it.a0 || 0) + it.ang) * Math.PI / 180, ln = it.len || len;
    const e0 = [x + ln * Math.cos(a0), y - ln * Math.sin(a0)], e1 = [x + ln * Math.cos(a1), y - ln * Math.sin(a1)];
    s += L(x, y, e0[0], e0[1], { w: 4, cap: true }) + L(x, y, e1[0], e1[1], { w: 4, cap: true });
    const ar = 28, A0 = [x + ar * Math.cos(a0), y - ar * Math.sin(a0)], A1 = [x + ar * Math.cos(a1), y - ar * Math.sin(a1)];
    s += `<path d="M${r2(A0[0])} ${r2(A0[1])} A${ar} ${ar} 0 ${it.ang > 180 ? 1 : 0} 0 ${r2(A1[0])} ${r2(A1[1])}" fill="none" stroke="${RED}" stroke-width="3"/>`;
    s += C(x, y, 5, { fill: N, w: 1 });
    if (it.tag) s += T(x + ln * 0.45, y + 26, it.tag, { size: 20 });
  });
  return svg(w, h, s, o.label || 'Angles', o.width || w);
};

module.exports = { fit, barModel, numberLine, lineParts, stackSvg, clockFace, clocks, queueRow, grid, dotPlot, angleFig, svg, T, L, R, C, DEFS, N, Y, SKY, TEAL, RED, WH, GR, F };
