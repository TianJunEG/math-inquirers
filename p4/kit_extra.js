// Extra cut-out pages for the P4 program (fix pass): card page, graph grid, paper clock + pizza circles + "bring from home" box.
// Own file for P4: uses only the shared svg/H/note helpers from hp/kit.js, never edits them.
const P = require('../hp/kit.js').parts;
const { svg, H, note } = P;
const NAVY = '#1B2A49', YEL = '#FFC93C', TEAL = '#1F7A6F', SKY = '#DDEBF7', RED = '#D64545';
const dash = 'stroke-dasharray="6 4"';
const F = 'Fredoka, Arial, sans-serif';

// 36 cards: digits 0-9 twice, 4 decimal points, signs + - x / twice, 2 pairs of brackets
function cards() {
  const faces = [];
  for (let k = 0; k < 2; k++) for (let d = 0; d <= 9; d++) faces.push([String(d), SKY, 'd']);
  for (let i = 0; i < 4; i++) faces.push(['.', YEL, 'p']);
  for (let k = 0; k < 2; k++) ['+', '−', '×', '÷'].forEach(s => faces.push([s, '#E3F3EF', 's']));
  for (let k = 0; k < 2; k++) { faces.push(['(', '#FFF0C2', 'b']); faces.push([')', '#FFF0C2', 'b']); }
  const w = 110, h = 128, gx = 8, gy = 10, cols = 6;
  let b = '';
  faces.forEach(([t, fill, kind], i) => {
    const c = i % cols, r = Math.floor(i / cols), x = 14 + c * (w + gx), y = 14 + r * (h + gy);
    b += `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="8" fill="${fill}" stroke="${NAVY}" stroke-width="2.5" ${dash}/>`;
    if (kind === 'p') b += `<circle cx="${x + w / 2}" cy="${y + h / 2 + 22}" r="11" fill="${NAVY}"/><text x="${x + w / 2}" y="${y + 26}" font-size="14" font-weight="800" text-anchor="middle" fill="${NAVY}" font-family="Nunito Sans, Arial">point</text>`;
    else b += `<text x="${x + w / 2}" y="${y + h / 2 + 26}" font-size="${kind === 'd' ? 76 : 80}" font-weight="700" text-anchor="middle" fill="${NAVY}" font-family="${F}">${t}</text>`;
  });
  const rows = Math.ceil(faces.length / cols);
  const hh = 28 + rows * (h + gy);
  b += note(14, hh + 8, 'Cut along the dashed lines. Keep the cards in one envelope. Digits: Lessons 2, 3, 5 and 10. Decimal points: Lesson 5. Signs and brackets: Lesson 3.');
  return svg(hh + 24, b);
}

// two blank line-graph grids, scale boxes to fill in
function graphGrids() {
  const s = 26, cols = 22, rows = 12;
  let b = '';
  [0, 1].forEach(k => {
    const oy = 40 + k * (rows * s + 120), ox = 70;
    b += `<text x="14" y="${oy - 14}" font-size="16" font-weight="800" fill="${NAVY}" font-family="Nunito Sans, Arial">Graph ${k + 1}.   Each line up the side is worth: ______      Title: ______________________________</text>`;
    for (let r = 0; r <= rows; r++) b += `<line x1="${ox}" y1="${oy + r * s}" x2="${ox + cols * s}" y2="${oy + r * s}" stroke="${r === rows ? NAVY : '#9AA6C0'}" stroke-width="${r === rows ? 3 : 1.2}"/>`;
    for (let c = 0; c <= cols; c++) b += `<line x1="${ox + c * s}" y1="${oy}" x2="${ox + c * s}" y2="${oy + rows * s}" stroke="${c === 0 ? NAVY : '#9AA6C0'}" stroke-width="${c === 0 ? 3 : 1.2}"/>`;
    for (let r = 0; r <= rows; r += 2) b += `<rect x="14" y="${oy + (rows - r) * s - 11}" width="48" height="22" rx="4" fill="#fff" stroke="#8A94AD" stroke-width="1.2"/>`;
    b += `<text x="${ox + cols * s / 2}" y="${oy + rows * s + 36}" font-size="15" font-weight="800" text-anchor="middle" fill="${NAVY}" font-family="Nunito Sans, Arial">what is along the bottom: ____________________</text>`;
  });
  const hh = 60 + 2 * (rows * s + 120);
  b += note(14, hh - 8, 'Write the scale in the small boxes at the side first (for example 0, 10, 20 ...). Print extra copies if you need them.');
  return svg(hh, b);
}

// paper clock face + hands, pizza circles, bring-from-home box
function clockPage() {
  let b = '';
  const cx = 230, cy = 230, R = 205;
  b += `<circle cx="${cx}" cy="${cy}" r="${R}" fill="#fff" stroke="${NAVY}" stroke-width="3" ${dash}/>`;
  for (let i = 0; i < 60; i++) {
    const a = i * 6 * Math.PI / 180, big = i % 5 === 0, r1 = R - (big ? 24 : 12), r2 = R - 4;
    b += `<line x1="${cx + r1 * Math.sin(a)}" y1="${cy - r1 * Math.cos(a)}" x2="${cx + r2 * Math.sin(a)}" y2="${cy - r2 * Math.cos(a)}" stroke="${NAVY}" stroke-width="${big ? 3 : 1.4}"/>`;
  }
  for (let h = 1; h <= 12; h++) {
    const a = h * 30 * Math.PI / 180, r = R - 52;
    b += `<text x="${cx + r * Math.sin(a)}" y="${cy - r * Math.cos(a) + 12}" font-size="36" font-weight="700" text-anchor="middle" fill="${NAVY}" font-family="${F}">${h}</text>`;
  }
  b += `<circle cx="${cx}" cy="${cy}" r="7" fill="${RED}"/><text x="${cx}" y="${cy + 46}" font-size="13" text-anchor="middle" fill="#666" font-family="Nunito Sans, Arial">push a split pin here</text>`;
  // hands
  b += `<g ${dash}><path d="M500 60 h24 l6 -22 l6 22 h24 v200 h-60 Z" fill="${YEL}" stroke="${NAVY}" stroke-width="2.5"/></g><text x="530" y="290" font-size="15" font-weight="800" text-anchor="middle" fill="${NAVY}" font-family="Nunito Sans, Arial">hour hand</text>`;
  b += `<g ${dash}><path d="M620 40 h20 l6 -22 l6 22 h20 v270 h-52 Z" fill="${SKY}" stroke="${NAVY}" stroke-width="2.5"/></g><text x="646" y="334" font-size="15" font-weight="800" text-anchor="middle" fill="${NAVY}" font-family="Nunito Sans, Arial">minute hand</text>`;
  b += `<circle cx="530" cy="236" r="5" fill="${RED}"/><circle cx="646" cy="286" r="5" fill="${RED}"/>`;
  b += note(480, 360, 'Make a hole at each red dot, then join the hands to the centre of the face with a split pin.');
  // pizza circles
  b += `<text x="14" y="510" font-size="18" font-weight="800" fill="${NAVY}" font-family="Nunito Sans, Arial">Pizza circles (Lesson 4): cut out each circle, then cut it into 4 equal slices (quarters)</text>`;
  [120, 350, 580].forEach(x => {
    b += `<circle cx="${x}" cy="640" r="105" fill="#FFF0C2" stroke="${NAVY}" stroke-width="3" ${dash}/>`;
    b += `<line x1="${x - 105}" y1="640" x2="${x + 105}" y2="640" stroke="#C9A24A" stroke-width="1.4" ${dash}/><line x1="${x}" y1="535" x2="${x}" y2="745" stroke="#C9A24A" stroke-width="1.4" ${dash}/>`;
  });
  b += note(14, 770, 'Faint lines show where to cut. Fold each circle in half twice to check the 4 slices are equal.');
  // bring from home
  b += `<rect x="14" y="796" width="672" height="150" rx="12" fill="#F3FBF9" stroke="${TEAL}" stroke-width="3"/>`;
  b += `<text x="34" y="830" font-size="20" font-weight="800" fill="${TEAL}" font-family="Nunito Sans, Arial">Bring from home (not printed here)</text>`;
  ['A clear 180 degree protractor and a 30 cm ruler. Lesson 6 starts with them, so have them ready.',
    'No protractor? Ask at school for a real clear plastic one first. Fallback: print the protractor kit page on a transparency sheet. Or tell your tutor: there are spares.',
    'A ruler and two coloured pencils (Lessons 7 and 9). Scissors and tape (Lessons 4, 6, 7 and 8).',
    'Squared paper, if you want extra: the Square grid page can be cut into 1 cm squares for Lessons 7 and 8.'].forEach((t, i) => {
    b += `<text x="34" y="${858 + i * 24}" font-size="15" fill="${NAVY}" font-family="Nunito Sans, Arial">• ${t}</text>`;
  });
  return svg(960, b);
}


// Cut-out 180 degree protractor, drawn in millimetres so it prints at actual size (print at 100%).
// Radius 75 mm; outer scale 0 at the right, inner scale 0 at the left; ticks every 1, 5 and 10 degrees; check bar 5 cm.
function protractor(copy) {
  const R = 75, cx = 80, cy = 84, W = 160, Ht = 98;
  const pt = (r, deg) => [cx + r * Math.cos(deg * Math.PI / 180), cy - r * Math.sin(deg * Math.PI / 180)];
  const f = v => v.toFixed(2);
  let b = `<path d="M${cx - R} ${cy} A${R} ${R} 0 0 1 ${cx + R} ${cy} L${cx + R} ${cy + 8} L${cx - R} ${cy + 8} Z" fill="#F4F9FD" stroke="${NAVY}" stroke-width="0.5" stroke-dasharray="2 1.4"/>`;
  b += `<path d="M${cx - 50} ${cy} A50 50 0 0 1 ${cx + 50} ${cy}" fill="none" stroke="#9AA6C0" stroke-width="0.25"/>`;
  for (let a = 0; a <= 180; a += 10) { const [x1, y1] = pt(14, a), [x2, y2] = pt(R - 9, a); b += `<line x1="${f(x1)}" y1="${f(y1)}" x2="${f(x2)}" y2="${f(y2)}" stroke="#B5BFD4" stroke-width="0.22"/>`; }
  for (let a = 0; a <= 180; a++) {
    const len = a % 10 === 0 ? 5 : a % 5 === 0 ? 3.4 : 2;
    const [x1, y1] = pt(R, a), [x2, y2] = pt(R - len, a);
    b += `<line x1="${f(x1)}" y1="${f(y1)}" x2="${f(x2)}" y2="${f(y2)}" stroke="${NAVY}" stroke-width="${a % 10 === 0 ? 0.4 : 0.22}"/>`;
  }
  for (let a = 0; a <= 180; a++) {
    const len = a % 10 === 0 ? 4 : a % 5 === 0 ? 2.8 : 1.6;
    const [x1, y1] = pt(R - 22, a), [x2, y2] = pt(R - 22 + len, a);
    b += `<line x1="${f(x1)}" y1="${f(y1)}" x2="${f(x2)}" y2="${f(y2)}" stroke="${TEAL}" stroke-width="${a % 10 === 0 ? 0.4 : 0.22}"/>`;
  }
  for (let a = 0; a <= 180; a += 10) {
    const [ox, oy] = pt(R - 9.2, a);
    // outer scale: 0 at right (angle a measured from the right); inner scale: 0 at left
    b += `<text x="${f(ox)}" y="${f(oy + 1.1)}" font-size="3.4" font-weight="700" text-anchor="middle" fill="${NAVY}" font-family="Arial, sans-serif" transform="rotate(${90 - a} ${f(ox)} ${f(oy)})">${a}</text>`;
  }
  for (let a = 0; a <= 180; a += 10) {
    const [x, y] = pt(R - 28, a);
    b += `<text x="${f(x)}" y="${f(y + 1.1)}" font-size="3.4" font-weight="700" text-anchor="middle" fill="${TEAL}" font-family="Arial, sans-serif" transform="rotate(${90 - a} ${f(x)} ${f(y)})">${180 - a}</text>`;
  }
  // baseline and centre mark
  b += `<line x1="${cx - R - 3}" y1="${cy}" x2="${cx + R + 3}" y2="${cy}" stroke="${NAVY}" stroke-width="0.5"/>`;
  b += `<line x1="${cx}" y1="${cy - 9}" x2="${cx}" y2="${cy + 3.4}" stroke="${RED}" stroke-width="0.4"/><circle cx="${cx}" cy="${cy}" r="1.6" fill="none" stroke="${RED}" stroke-width="0.4"/><circle cx="${cx}" cy="${cy}" r="0.4" fill="${RED}"/>`;
  b += `<text x="${cx}" y="${cy + 6.4}" font-size="3" text-anchor="middle" fill="${RED}" font-family="Arial, sans-serif" font-weight="700">centre: put on the corner</text>`;
  b += `<text x="${cx - R + 1}" y="${cy + 6.5}" font-size="3" fill="${NAVY}" font-family="Arial, sans-serif" font-weight="700">baseline: line up with one arm</text>`;
  b += `<text x="${cx}" y="${cy - 35}" font-size="3.6" font-weight="700" text-anchor="middle" fill="${NAVY}" stroke="#F4F9FD" stroke-width="1.2" paint-order="stroke" font-family="Arial, sans-serif">Math Inquirers 180° protractor ${copy}</text>`;
  b += `<text x="${cx}" y="${cy - 30}" font-size="2.8" text-anchor="middle" fill="${TEAL}" stroke="#F4F9FD" stroke-width="1.2" paint-order="stroke" font-family="Arial, sans-serif">start at the 0 on the arm you line up</text>`;
  return `<div class="p" style="text-align:center;margin:0 0 2mm"><svg viewBox="0 0 ${W} ${Ht}" width="${W}mm" height="${Ht}mm" xmlns="http://www.w3.org/2000/svg">${b}</svg></div>`;
}
// 5 cm check bar (millimetres, so it prints at actual size) with the print instruction
function protractorCheckBar() {
  let b = `<rect x="3.5" y="6" width="50" height="6" fill="${YEL}" stroke="${NAVY}" stroke-width="0.4"/>`;
  for (let m = 0; m <= 50; m++) { const L = m % 10 === 0 ? 3 : m % 5 === 0 ? 2.2 : 1.3; b += `<line x1="${3.5 + m}" y1="12" x2="${3.5 + m}" y2="${12 - L}" stroke="${NAVY}" stroke-width="0.25"/>`; }
  for (let c = 0; c <= 5; c++) b += `<text x="${3.5 + c * 10}" y="16.5" font-size="3.4" font-weight="700" text-anchor="middle" fill="${NAVY}" font-family="Arial, sans-serif">${c}</text>`;
  b += `<text x="56" y="9.8" font-size="3.6" font-weight="700" fill="${NAVY}" font-family="Arial, sans-serif">this bar is 5 cm long (50 mm)</text>`;
  b += `<text x="3.5" y="3.2" font-size="4" font-weight="700" fill="${RED}" font-family="Arial, sans-serif">Print at 100% / actual size - check the bar is 5 cm</text>`;
  return `<div class="p" style="margin:0 0 3mm"><svg viewBox="0 0 160 19" width="160mm" height="19mm" xmlns="http://www.w3.org/2000/svg">${b}</svg></div>`;
}
function protractorPage() {
  return protractorCheckBar() + protractor('A') + protractor('B');
}

module.exports = { cards, graphGrids, clockPage, protractorPage, protractor, protractorCheckBar, H };
