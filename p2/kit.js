// Cut-out kit for the P2 program: place-value cards, digit cards, fraction strips, a paper clock, coins and notes, cube strips.
const P = require('../hp/kit.js').parts;
const { svg, H, lab, note, lab2 } = P;
const NAVY = '#1B2A49', YEL = '#FFC93C', TEAL = '#1F7A6F', SKY = '#DDEBF7', RED = '#D64545';
const dash = 'stroke-dasharray="6 4"';

function placeValue() {
  // arrow-card style: hundreds (wide), tens (middle), ones (narrow)
  let b = '';
  const rowY = [20, 100, 180, 260, 340, 420, 500, 580, 660];
  for (let i = 1; i <= 9; i++) {
    const y = rowY[i - 1];
    b += `<rect x="20" y="${y}" width="270" height="62" fill="${SKY}" stroke="${NAVY}" stroke-width="2" ${dash}/><text x="155" y="${y + 43}" font-size="34" font-weight="800" text-anchor="middle" fill="${NAVY}">${i}00</text>`;
    b += `<rect x="320" y="${y}" width="190" height="62" fill="#FFF1C9" stroke="${NAVY}" stroke-width="2" ${dash}/><text x="415" y="${y + 43}" font-size="34" font-weight="800" text-anchor="middle" fill="${NAVY}">${i}0</text>`;
    b += `<rect x="540" y="${y}" width="120" height="62" fill="#E3F3EF" stroke="${NAVY}" stroke-width="2" ${dash}/><text x="600" y="${y + 43}" font-size="34" font-weight="800" text-anchor="middle" fill="${NAVY}">${i}</text>`;
  }
  b += note(20, 748, 'Lay the cards on top of each other, right edges together: 300 + 40 + 7 shows 347.');
  return svg(760, b);
}
function digits() {
  let b = '';
  for (let s = 0; s < 2; s++) for (let d = 0; d <= 9; d++) {
    const x = 20 + (d % 5) * 134, y = 20 + (Math.floor(d / 5) + s * 2) * 130;
    b += `<rect x="${x}" y="${y}" width="118" height="114" rx="10" fill="#fff" stroke="${NAVY}" stroke-width="2" ${dash}/><text x="${x + 59}" y="${y + 78}" font-size="64" font-weight="800" text-anchor="middle" fill="${s ? TEAL : NAVY}">${d}</text>`;
  }
  return svg(560, b);
}
function fractions() {
  const rows = [[1, '1 whole'], [2, '1/2'], [3, '1/3'], [4, '1/4'], [6, '1/6'], [8, '1/8']];
  const fills = [YEL, SKY, '#E3F3EF', '#FFF1C9', '#F6D4D4', '#E8E1F7'];
  let b = '';
  rows.forEach(([n, l], r) => {
    const y = 20 + r * 76, w = 640 / n;
    for (let i = 0; i < n; i++) {
      b += `<rect x="${30 + i * w}" y="${y}" width="${w}" height="56" fill="${fills[r]}" stroke="${NAVY}" stroke-width="2"/><text x="${30 + i * w + w / 2}" y="${y + 37}" font-size="${n > 6 ? 20 : 24}" font-weight="800" text-anchor="middle" fill="${NAVY}">${l}</text>`;
    }
  });
  b += note(30, 490, 'Cut along each strip, then cut the parts apart. Compare: which is bigger, 1/3 or 1/4?');
  return svg(510, b);
}
function clock() {
  const cx = 230, cy = 230, r = 190;
  let b = `<circle cx="${cx}" cy="${cy}" r="${r}" fill="#fff" stroke="${NAVY}" stroke-width="4"/><circle cx="${cx}" cy="${cy}" r="${r + 14}" fill="none" stroke="${NAVY}" stroke-width="1.5" ${dash}/>`;
  for (let m = 0; m < 60; m++) {
    const a = m * Math.PI / 30, long = m % 5 === 0;
    const x1 = cx + Math.sin(a) * (r - (long ? 18 : 9)), y1 = cy - Math.cos(a) * (r - (long ? 18 : 9));
    const x2 = cx + Math.sin(a) * r, y2 = cy - Math.cos(a) * r;
    b += `<line x1="${x1.toFixed(1)}" y1="${y1.toFixed(1)}" x2="${x2.toFixed(1)}" y2="${y2.toFixed(1)}" stroke="${NAVY}" stroke-width="${long ? 3 : 1.5}"/>`;
  }
  for (let h = 1; h <= 12; h++) {
    const a = h * Math.PI / 6;
    b += `<text x="${(cx + Math.sin(a) * (r - 44)).toFixed(1)}" y="${(cy - Math.cos(a) * (r - 44) + 11).toFixed(1)}" font-size="30" font-weight="800" text-anchor="middle" fill="${NAVY}">${h}</text>`;
  }
  b += `<circle cx="${cx}" cy="${cy}" r="7" fill="${NAVY}"/>`;
  // hands to cut out
  // same colours as the clock in Lesson 9: hour hand = short, thick, navy; minute hand = long, thin, red
  b += `<rect x="470" y="120" width="28" height="150" rx="10" fill="${NAVY}" stroke="${NAVY}" stroke-width="2" ${dash}/><rect x="534" y="70" width="12" height="200" rx="6" fill="${RED}" stroke="${NAVY}" stroke-width="2" ${dash}/>`;
  b += lab(440, 300, 'hour hand') + lab(440, 322, '(short, thick)') + lab(520, 346, 'minute hand') + lab(520, 368, '(long, thin)');
  b += note(450, 400, 'Cut out the clock and the hands.') + note(450, 422, 'Pin them at the centre with a') + note(450, 444, 'split pin or a short pencil.');
  return svg(470, b);
}
// Lesson 8: the six nets A to F from the workbook figure, to cut out and fold. Dashed = cut, solid = fold.
function nets() {
  const NETS = [['A', ['.#..', '####', '.#..']], ['B', ['###', '###']], ['C', ['#...', '####', '...#']], ['D', ['.##.', '####']], ['E', ['##..', '.##.', '..##']], ['F', ['#....', '#####']]];
  const c = 52; let b = '';
  NETS.forEach(([l, rows], i) => {
    const ox = 30 + (i % 2) * 350, oy = 44 + Math.floor(i / 2) * 200;
    const has = (x, y) => !!rows[y] && rows[y][x] === '#';
    let cells = '', cut = '';
    rows.forEach((r, y) => [...r].forEach((ch, x) => {
      if (ch !== '#') return;
      const X = ox + x * c, Y = oy + y * c;
      cells += `<rect x="${X}" y="${Y}" width="${c}" height="${c}" fill="${SKY}" stroke="${NAVY}" stroke-width="1.5"/>`;
      if (!has(x, y - 1)) cut += `M${X} ${Y}h${c}`;
      if (!has(x, y + 1)) cut += `M${X} ${Y + c}h${c}`;
      if (!has(x - 1, y)) cut += `M${X} ${Y}v${c}`;
      if (!has(x + 1, y)) cut += `M${X + c} ${Y}v${c}`;
    }));
    b += `<text x="${ox}" y="${oy - 14}" font-size="24" font-weight="800" fill="${TEAL}">Net ${l}</text>` + cells + `<path d="${cut}" fill="none" stroke="${NAVY}" stroke-width="3" ${dash}/>`;
  });
  b += note(30, 640, 'Cut along the dashed lines. Fold along the solid lines. Which nets fold up into a cube?');
  return svg(660, b);
}
// two extra $1 coins so that the all-$1 way in Lesson 6 Q2 (eight $1 coins) is possible
function spareDollars() {
  let b = '';
  for (let i = 0; i < 2; i++) { const x = 55 + i * 105; b += `<circle cx="${x}" cy="50" r="38" fill="#EBD98A" stroke="${NAVY}" stroke-width="2.5" ${dash}/><circle cx="${x}" cy="50" r="30" fill="none" stroke="#888" stroke-width="1"/><text x="${x}" y="57" font-size="20" font-weight="800" text-anchor="middle" fill="${NAVY}">$1</text>`; }
  return lab2('Two spare $1 coins') + svg(100, b);
}
const kit = () => [
  H('Cut-outs', 'For the P2 program. Cut along the dashed lines and keep the pieces in one envelope.'),
  lab2('Place-value cards (Lessons 1, 2 and 10)'), placeValue(),
  '<div class="brk"></div>', H('Digit cards', 'Two sets of 0 to 9 (Lessons 1 and 10).'), digits(),
  '<div class="brk"></div>', lab2('Fraction strips (Lesson 7)'), fractions(),
  '<div class="brk"></div>', H('Paper clock', 'For Lesson 9 (time).'), clock(),
  lab2('Paper strips of numbered squares (Lesson 9: ribbons and lengths)'), P.cubes(),
  '<div class="brk"></div>', H('Cube nets', 'For Lesson 8 (Shape Builders). Cut out each net and try folding it. Which ones make a cube?'), nets(),
  '<div class="brk"></div>', H('Play coins', 'For Lesson 6 (Market Day). Seven 5¢, seven 10¢, six 20¢ and five 50¢. Keep spare coins in the envelope.'), P.coins(),
  '<div class="brk"></div>', H('Play notes and $1 coins', 'For Lesson 6 (Market Day). Eight $1 coins (six here and two spare below), four $2, four $5, four $10 and two $50 notes. Keep spare coins in the envelope.'), P.notes(), spareDollars()
];
module.exports = kit;
module.exports.parts = { placeValue, digits, fractions, clock, nets };
