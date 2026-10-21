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
  b += `<rect x="470" y="120" width="26" height="150" rx="10" fill="${RED}" stroke="${NAVY}" stroke-width="2" ${dash}/><rect x="530" y="70" width="18" height="200" rx="8" fill="${TEAL}" stroke="${NAVY}" stroke-width="2" ${dash}/>`;
  b += lab(462, 300, 'hour hand') + lab(512, 330, 'minute hand');
  b += note(450, 380, 'Cut out the clock and the hands.') + note(450, 402, 'Pin them at the centre with a') + note(450, 424, 'split pin or a short pencil.');
  return svg(470, b);
}
const kit = () => [
  H('Cut-outs', 'For the P2 program. Cut along the dashed lines and keep the pieces in one envelope.'),
  lab2('Place-value cards (Lessons 1, 2 and 10)'), placeValue(),
  '<div class="brk"></div>', H('Digit cards', 'Two sets of 0 to 9 (Lessons 1 and 2).'), digits(),
  lab2('Fraction strips (Lesson 7)'), fractions(),
  '<div class="brk"></div>', H('Paper clock', 'For Lesson 9 (time).'), clock(),
  lab2('Paper cube strips (Lesson 9)'), P.cubes(),
  '<div class="brk"></div>', H('Play coins', 'For Lesson 6 (Market Day).'), P.coins(),
  '<div class="brk"></div>', H('Play notes and $1 coins', 'For Lesson 6 (Market Day).'), P.notes()
];
module.exports = kit;
module.exports.parts = { placeValue, digits, fractions, clock };
