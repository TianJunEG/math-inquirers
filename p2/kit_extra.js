// Number-grid pages for the P2 program: 1 to 100 chart, missing-numbers chart, "starts at" chart (for 1000-chart pieces).
const P = require('../hp/kit.js').parts;
const { svg, note } = P;
const NAVY = '#1B2A49', YEL = '#FFC93C', SKY = '#DDEBF7';
const F = 'Fredoka, Arial, sans-serif';
const CW = 62, CH = 52, OX = 40, OY = 14;

// cells: function (r,c) -> {text, fill} ; text '' draws an empty (write-in) cell
function grid(cell, foot) {
  let b = '';
  for (let r = 0; r < 10; r++) for (let c = 0; c < 10; c++) {
    const { text, fill } = cell(r, c), x = OX + c * CW, y = OY + r * CH;
    b += `<rect x="${x}" y="${y}" width="${CW}" height="${CH}" fill="${fill}" stroke="${NAVY}" stroke-width="2"/>`;
    if (text !== '') b += `<text x="${x + CW / 2}" y="${y + CH / 2 + 10}" font-size="28" font-weight="700" text-anchor="middle" fill="${NAVY}" font-family="${F}">${text}</text>`;
  }
  b += `<rect x="${OX}" y="${OY}" width="${CW * 10}" height="${CH * 10}" fill="none" stroke="${NAVY}" stroke-width="4"/>`;
  const h = OY * 2 + CH * 10 + 26;
  b += note(OX, h - 6, foot);
  return svg(h, b);
}
// 1 to 100, last column (multiples of 10) shaded
function hundredChart() {
  return grid((r, c) => ({ text: String(r * 10 + c + 1), fill: c === 9 ? '#FFF1C9' : '#fff' }),
    'Along a row: +1 each step. Down a column: +10 each step. Shaded: multiples of 10.');
}
// 1 to 100 with 32 cells left empty (fixed pattern; answers are r*10+c+1)
const MISSING = new Set([3, 7, 12, 18, 20, 24, 29, 33, 35, 41, 46, 50, 52, 57, 61, 65, 68, 73, 77, 80, 84, 88, 91, 94, 96, 99, 15, 38, 59, 70, 82, 100].map(n => n));
function missingChart() {
  return grid((r, c) => { const n = r * 10 + c + 1; return MISSING.has(n) ? { text: '', fill: '#FFF8DC' } : { text: String(n), fill: '#fff' }; },
    'Fill the yellow squares. Each is 1 more than its left and 10 more than the one above.');
}
// blank chart with a starting number to write in the first square
function startChart() {
  return grid((r, c) => ({ text: '', fill: r === 0 && c === 0 ? YEL : '#fff' }),
    'Write a starting number in the yellow square (e.g. 381). Rows go +1, columns go +10.');
}
module.exports = { hundredChart, missingChart, startChart, MISSING };
