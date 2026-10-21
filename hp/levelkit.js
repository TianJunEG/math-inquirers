// Extra cut-out parts for P3 to P6: square grid, dot grid, right-angle tester, wide fraction wall, cube net, code cards.
const P = require('./kit.js').parts;
const { svg, note } = P;
const NAVY = '#1B2A49', YEL = '#FFC93C', TEAL = '#1F7A6F', SKY = '#DDEBF7', RED = '#D64545';
const dash = 'stroke-dasharray="6 4"';
function grid(rows = 14, cols = 20, s = 32) {
  let b = '';
  for (let r = 0; r <= rows; r++) b += `<line x1="30" y1="${20 + r * s}" x2="${30 + cols * s}" y2="${20 + r * s}" stroke="#9AA6C0" stroke-width="1.2"/>`;
  for (let c = 0; c <= cols; c++) b += `<line x1="${30 + c * s}" y1="20" x2="${30 + c * s}" y2="${20 + rows * s}" stroke="#9AA6C0" stroke-width="1.2"/>`;
  return svg(40 + rows * s, b);
}
function dots(rows = 14, cols = 20, s = 32) {
  let b = '';
  for (let r = 0; r <= rows; r++) for (let c = 0; c <= cols; c++) b += `<circle cx="${30 + c * s}" cy="${20 + r * s}" r="2.6" fill="${NAVY}"/>`;
  return svg(40 + rows * s, b);
}
function rightAngle() {
  let b = '';
  [[40, 30], [260, 30], [480, 30]].forEach(([x, y]) => {
    b += `<path d="M${x} ${y} h160 v40 h-120 v120 h-40 Z" fill="${YEL}" stroke="${NAVY}" stroke-width="2" ${dash}/><rect x="${x}" y="${y}" width="22" height="22" fill="none" stroke="${NAVY}" stroke-width="2"/>`;
  });
  b += note(40, 220, 'Cut out a right-angle tester. Put its corner on an angle: bigger, smaller or exactly a right angle?');
  return svg(240, b);
}
function fractionWall() {
  const rows = [1, 2, 3, 4, 5, 6, 8, 10, 12];
  const fills = [YEL, SKY, '#E3F3EF', '#FFF1C9', '#F6D4D4', '#E8E1F7', SKY, '#E3F3EF', '#FFF1C9'];
  let b = '';
  rows.forEach((n, r) => {
    const y = 20 + r * 58, w = 640 / n;
    for (let i = 0; i < n; i++) b += `<rect x="${30 + i * w}" y="${y}" width="${w}" height="46" fill="${fills[r]}" stroke="${NAVY}" stroke-width="2"/><text x="${30 + i * w + w / 2}" y="${y + 31}" font-size="${n > 8 ? 16 : 20}" font-weight="800" text-anchor="middle" fill="${NAVY}">${n === 1 ? '1' : '1/' + n}</text>`;
  });
  b += note(30, 560, 'Line the strips up under the whole. Which fractions are the same size?');
  return svg(580, b);
}
function cubeNet(s = 110) {
  const cells = [[1, 0], [0, 1], [1, 1], [2, 1], [3, 1], [1, 2]];
  let b = '';
  cells.forEach(([c, r]) => b += `<rect x="${40 + c * s}" y="${20 + r * s}" width="${s}" height="${s}" fill="${SKY}" stroke="${NAVY}" stroke-width="2.5"/>`);
  b += note(40, 20 + 3 * s + 26, 'Cut round the outside, fold on the lines and tape: a cube. Try drawing other nets on the square grid.');
  return svg(3 * s + 50, b);
}
function codeCards() {
  const cards = [['when green flag clicked', YEL], ['repeat 10', '#F2A93B'], ['move 10 steps', '#4C8BF5'], ['turn right 90 degrees', '#4C8BF5'], ['say (answer)', '#9A6CF0'], ['set n to 1', '#E8762C'], ['change n by 1', '#E8762C'], ['if … then', '#F2A93B'], ['ask … and wait', '#5CB1D6'], ['pen down', TEAL]];
  let b = '';
  cards.forEach(([t, f], i) => {
    const x = 30 + (i % 2) * 330, y = 20 + Math.floor(i / 2) * 78;
    b += `<path d="M${x} ${y} h30 l8 8 h20 l8 -8 h234 v56 h-234 l-8 8 h-20 l-8 -8 h-30 Z" fill="${f}" stroke="${NAVY}" stroke-width="2" ${dash}/><text x="${x + 18}" y="${y + 36}" font-size="20" font-weight="800" fill="#fff">${t}</text>`;
  });
  b += note(30, 420, 'Unplugged coding: cut out the blocks and snap them into a program on the table before you build it on screen.');
  return svg(440, b);
}
module.exports = { grid, dots, rightAngle, fractionWall, cubeNet, codeCards, money: [P.coins, P.notes] };
