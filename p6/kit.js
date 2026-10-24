// Cut-out kit for the P6 program.
const P = require('../hp/kit.js').parts;
const P2 = require('../p2/kit.js').parts;
const K = require('../hp/levelkit.js');
const { H, lab2, svg, note } = P;
// Code cards with black text on a white block (white text on colour turns into pattern in black and white print); the colour stays as a stripe.
const codeCards = () => {
  const cards = [['when green flag clicked', '#FFC93C'], ['repeat 10', '#F2A93B'], ['move 10 steps', '#4C8BF5'], ['turn right 90 degrees', '#4C8BF5'], ['say (answer)', '#9A6CF0'], ['set n to 1', '#E8762C'], ['change n by 1', '#E8762C'], ['if … then', '#F2A93B'], ['ask … and wait', '#5CB1D6'], ['pen down', '#1F7A6F']];
  let b = '';
  cards.forEach(([t, f], i) => {
    const x = 30 + (i % 2) * 330, y = 20 + Math.floor(i / 2) * 78;
    b += `<path d="M${x} ${y} h30 l8 8 h20 l8 -8 h234 v56 h-234 l-8 8 h-20 l-8 -8 h-30 Z" fill="#FFFFFF" stroke="#1B2A49" stroke-width="3" stroke-dasharray="6 4"/><rect x="${x + 6}" y="${y + 12}" width="10" height="32" fill="${f}" stroke="#1B2A49" stroke-width="2"/><text x="${x + 28}" y="${y + 36}" font-size="20" font-weight="800" fill="#1B2A49">${t}</text>`;
  });
  b += note(30, 416, 'Unplugged coding: cut out the blocks and snap them into a program');
  b += note(30, 436, 'on the table before you build it on screen.');
  return svg(450, b);
};
module.exports = () => [
  H('Cut-outs', 'For the P6 program. Cut along the dashed lines and keep the pieces in one envelope.'),
  lab2('Unplugged code cards (Lessons 1, 4 and 7)'), codeCards(),
  '<div class="brk"></div>', H('Square grid', 'For Lessons 7 and 9.'), K.grid()
];
