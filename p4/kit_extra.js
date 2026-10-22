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
    'No protractor? Tell your tutor before Lesson 6: the tutor has spares, or you can share with a partner.',
    'A ruler and two coloured pencils (Lessons 7 and 9). Scissors and tape (Lessons 4, 6, 7 and 8).',
    'Squared paper, if you want extra: the Square grid page can be cut into 1 cm squares for Lessons 7 and 8.'].forEach((t, i) => {
    b += `<text x="34" y="${858 + i * 24}" font-size="15" fill="${NAVY}" font-family="Nunito Sans, Arial">• ${t}</text>`;
  });
  return svg(960, b);
}

module.exports = { cards, graphGrids, clockPage, H };
