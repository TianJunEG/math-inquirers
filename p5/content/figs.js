// Small figures for the printed Think harder (TH1-TH4) and Go further (GF5-GF7) pages of the P5 workbook (re-audit fix #12).
// Used by workbook_html.js only. Keys: FIGS[lesson]['TH3'] or ['GF6']. Each value is an <svg> string (drawn shapes, no figure answers).
// The geometry is exact (angles and lengths as in the question), so the pictures do not mislead.
const N = '#1B2A49', Y = '#FFC93C', SKY = '#DDEBF7', TEAL = '#1F7A6F', WH = '#FFFFFF';
const FF = 'Fredoka, Arial, sans-serif';
const T = (x, y, s, size = 16, fill = N, anchor = 'middle', weight = 700) =>
  `<text x="${x.toFixed(1)}" y="${y.toFixed(1)}" font-size="${size}" font-weight="${weight}" text-anchor="${anchor}" fill="${fill}" font-family="${FF}">${s}</text>`;
const line = (a, b, w = 3, col = N, dash = '') => `<line x1="${a[0].toFixed(1)}" y1="${a[1].toFixed(1)}" x2="${b[0].toFixed(1)}" y2="${b[1].toFixed(1)}" stroke="${col}" stroke-width="${w}" stroke-linecap="round"${dash ? ` stroke-dasharray="${dash}"` : ''}/>`;
const poly = (pts, fill = 'none', w = 3, col = N) => `<polygon points="${pts.map(p => p[0].toFixed(1) + ',' + p[1].toFixed(1)).join(' ')}" fill="${fill}" stroke="${col}" stroke-width="${w}" stroke-linejoin="round"/>`;
const svg = (label, W, H, inner, maxw) => `<svg aria-label="${label}" viewBox="0 0 ${W} ${H}" width="${W}" xmlns="http://www.w3.org/2000/svg" style="max-width:${maxw || 60}%">${inner}</svg>`;
// a tick mark across a segment (equal-length marker)
const tick = (a, b, n = 1) => {
  const mx = (a[0] + b[0]) / 2, my = (a[1] + b[1]) / 2, dx = b[0] - a[0], dy = b[1] - a[1], L = Math.hypot(dx, dy);
  const ux = dx / L, uy = dy / L, nx = -uy, ny = ux; let g = '';
  for (let i = 0; i < n; i++) { const o = (i - (n - 1) / 2) * 7; g += line([mx + ux * o - nx * 7, my + uy * o - ny * 7], [mx + ux * o + nx * 7, my + uy * o + ny * 7], 2.5); }
  return g;
};
// arc for an angle at vertex P between directions a1 and a2 (radians, SVG coordinates), radius r
const arc = (P, a1, a2, r) => {
  const x1 = P[0] + r * Math.cos(a1), y1 = P[1] + r * Math.sin(a1), x2 = P[0] + r * Math.cos(a2), y2 = P[1] + r * Math.sin(a2);
  let d = a2 - a1; while (d > Math.PI) d -= 2 * Math.PI; while (d < -Math.PI) d += 2 * Math.PI;
  return `<path d="M${x1.toFixed(1)} ${y1.toFixed(1)} A${r} ${r} 0 0 ${d > 0 ? 1 : 0} ${x2.toFixed(1)} ${y2.toFixed(1)}" fill="none" stroke="${TEAL}" stroke-width="2.5"/>`;
};
const rad = d => d * Math.PI / 180;

const FIGS = {};

// ---------- L4 Go further Q6: two squares side by side (big 10 cm, small 6 cm) ----------
{
  const s = 14, x0 = 30, yb = 175; // 1 cm = 14 px
  const bl = [x0, yb], bigTR = [x0 + 10 * s, yb - 10 * s], smallTR = [x0 + 16 * s, yb - 6 * s];
  let g = poly([bl, [x0 + 10 * s, yb], bigTR, [x0, yb - 10 * s]], WH) + poly([[x0 + 10 * s, yb], [x0 + 16 * s, yb], smallTR, [x0 + 10 * s, yb - 6 * s]], WH);
  g += poly([bl, bigTR, smallTR], 'rgba(255,201,60,0.55)', 3.5);
  g += T(x0 + 5 * s, yb + 22, 'big square: 10 cm') + T(x0 + 13 * s, yb + 22, '6 cm');
  g += T(x0 + 5.6 * s, yb - 6.2 * s, 'the triangle', 15, TEAL);
  FIGS[4] = { GF6: svg('Two squares side by side on a line, a big one of side 10 cm and a small one of side 6 cm. A triangle joins the bottom-left corner and top-right corner of the big square and the top-right corner of the small square.', 280, 205, g, 52) };
}
// ---------- L4 Go further Q7: triangle ABC, D on BC with BD = 4 and DC = 8 ----------
{
  const s = 20, B = [30, 150], C = [30 + 12 * s, 150], A = [30 + 3 * s, 20], D = [30 + 4 * s, 150];
  let g = poly([A, B, C], WH) + line(A, D, 3, N, '7 5');
  g += T(A[0], A[1] - 8, 'A') + T(B[0] - 12, B[1] + 6, 'B') + T(C[0] + 12, C[1] + 6, 'C') + T(D[0] + 2, D[1] + 22, 'D');
  g += T(30 + 2 * s, 176, '4 cm', 15, TEAL) + T(30 + 8 * s, 176, '8 cm', 15, TEAL);
  g += `<text x="${A[0] + 74}" y="64" font-size="15" font-weight="700" fill="${TEAL}" font-family="${FF}">area of ABC = 54 cm&#178;</text>`;
  FIGS[4].GF7 = svg('Triangle ABC with a point D on side BC. BD is 4 cm and DC is 8 cm. A dashed line joins A to D.', 300, 190, g, 55);
}
// ---------- L5 Go further Q7: tank (30 cm wide, 20 cm front to back), water 10 cm deep, block 10 x 10 x 15 stood upright ----------
{
  const s = 6, x0 = 40, yb = 150, tw = 30 * s, th = 22 * s; // front view; tank drawn 22 cm high
  let g = `<rect x="${x0}" y="${yb - 10 * s}" width="${tw}" height="${10 * s}" fill="${SKY}"/>`;
  g += `<path d="M${x0} ${yb - th} V${yb} H${x0 + tw} V${yb - th}" fill="none" stroke="${N}" stroke-width="4" stroke-linejoin="round"/>`;
  g += `<rect x="${x0 + 10 * s}" y="${yb - 15 * s}" width="${10 * s}" height="${15 * s}" fill="${Y}" stroke="${N}" stroke-width="3"/>`;
  g += T(x0 + 15 * s, yb - 7 * s, 'block', 14) + T(x0 + 15 * s, yb - 7 * s + 16, '10 by 10', 12, N, 'middle', 600);
  g += line([x0 + tw + 14, yb - 15 * s], [x0 + tw + 14, yb], 2, TEAL) + T(x0 + tw + 20, yb - 7.5 * s, '15 cm', 14, TEAL, 'start');
  g += line([x0 - 14, yb - 10 * s], [x0 - 14, yb], 2, TEAL) + T(x0 - 18, yb - 5 * s + 5, '10 cm', 14, TEAL, 'end');
  g += T(x0 + tw / 2, yb + 24, 'base 30 cm by 20 cm  (front view)', 15, TEAL);
  g += T(x0 + 5 * s, yb - 10 * s - 8, 'water', 14, TEAL);
  FIGS[5] = { GF7: svg('Front view of a tank with water 10 centimetres deep. A block 10 by 10 by 15 centimetres stands upright on the bottom, sticking out above the water.', 330, 185, g, 62) };
}
// ---------- L8 Think harder Q3: trapezium ABCD, AB parallel to DC, angle DAB 84, angle ABC 97 ----------
{
  const sc = 1.0, A = [60, 25], B = [260, 25];
  const D = [A[0] + 120.7 * Math.cos(rad(84)) * sc, 145], C = [B[0] + 120.9 * Math.cos(rad(83)) * sc, 145];
  let g = poly([A, B, C, D], WH);
  const arr = (p, q, dx) => { const m = [(p[0] + q[0]) / 2 + dx, (p[1] + q[1]) / 2]; return line([m[0] - 8, m[1] - 6], [m[0] + 2, m[1]], 2.5) + line([m[0] + 2, m[1]], [m[0] - 8, m[1] + 6], 2.5); };
  g += arr(A, B, 0) + arr(D, C, 0);
  g += T(A[0] - 14, A[1] + 4, 'A') + T(B[0] + 14, B[1] + 4, 'B') + T(C[0] + 14, C[1] + 16, 'C') + T(D[0] - 14, D[1] + 16, 'D');
  g += arc(A, 0, rad(84), 26) + T(A[0] + 44, A[1] + 28, '84&#176;', 15, TEAL);
  g += arc(B, rad(180), rad(180 - 97), 26) + T(B[0] - 44, B[1] + 30, '97&#176;', 15, TEAL);
  g += T(150, 14, 'AB is parallel to DC', 14, TEAL);
  FIGS[8] = { TH3: svg('Trapezium ABCD with AB parallel to DC. Angle DAB is 84 degrees and angle ABC is 97 degrees. The arrows on AB and DC show they are parallel.', 330, 180, g, 58) };
}
// ---------- L8 Think harder Q4: square ABCD with an equilateral triangle CDE outside it ----------
{
  const s = 100, A = [90, 200], B = [190, 200], C = [190, 100], D = [90, 100], E = [140, 100 - 86.6];
  let g = poly([A, B, C, D], WH) + poly([D, C, E], 'rgba(255,201,60,0.45)');
  g += tick(D, E) + tick(C, E) + tick(D, C);
  g += T(A[0] - 14, A[1] + 6, 'A') + T(B[0] + 14, B[1] + 6, 'B') + T(C[0] + 14, C[1] + 6, 'C') + T(D[0] - 14, D[1] + 6, 'D') + T(E[0], E[1] - 8, 'E');
  g += T(140, 158, 'square', 14, TEAL, 'middle', 600) + T(240, 60, 'CDE is', 14, TEAL, 'start', 600) + T(240, 77, 'equilateral', 14, TEAL, 'start', 600);
  FIGS[8].TH4 = svg('A square ABCD with an equilateral triangle CDE drawn on side CD, outside the square. Point E is outside the square.', 330, 215, g, 52);
}
// ---------- L8 Go further Q5: isosceles ABC (AB = AC, angle A = 40), D on AC with BD = BC ----------
{
  const L = 190, half = rad(20), B = [60, 190], BC = 2 * L * Math.sin(half), C = [B[0] + BC, 190];
  const A = [B[0] + BC / 2, 190 - L * Math.cos(half)];
  const ux = (A[0] - C[0]) / L, uy = (A[1] - C[1]) / L, CD = 2 * BC * Math.cos(rad(70));
  const D = [C[0] + CD * ux, C[1] + CD * uy];
  let g = poly([A, B, C], WH) + line(B, D, 3, N, '7 5');
  g += tick(A, B, 1) + tick(A, C, 1) + tick(B, C, 2) + tick(B, D, 2);
  g += T(A[0], A[1] - 8, 'A') + T(B[0] - 14, B[1] + 6, 'B') + T(C[0] + 14, C[1] + 6, 'C') + T(D[0] + 14, D[1] - 2, 'D');
  g += T(A[0], A[1] + 46, '40&#176;', 15, TEAL);
  FIGS[8].GF5 = svg('Isosceles triangle ABC with AB equal to AC and angle BAC 40 degrees. D is a point on AC and BD is equal to BC (matching tick marks).', 280, 215, g, 52);
}
// ---------- L8 Go further Q6: square ABCD with equilateral triangle ABE inside ----------
{
  const A = [60, 190], B = [180, 190], C = [180, 70], D = [60, 70], E = [120, 190 - 120 * Math.sqrt(3) / 2];
  let g = poly([A, B, C, D], WH) + poly([A, B, E], 'rgba(255,201,60,0.45)') + line(E, D, 3, N, '7 5') + line(E, C, 3, N, '7 5');
  g += tick(A, E) + tick(B, E) + tick(A, B);
  g += T(A[0] - 14, A[1] + 6, 'A') + T(B[0] + 14, B[1] + 6, 'B') + T(C[0] + 14, C[1] + 6, 'C') + T(D[0] - 14, D[1] + 6, 'D') + T(E[0], E[1] - 10, 'E');
  FIGS[8].GF6 = svg('A square ABCD with an equilateral triangle ABE drawn on side AB inside the square. Dashed lines join E to D and to C.', 260, 220, g, 46);
}
module.exports = FIGS;
