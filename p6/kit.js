// Cut-out kit for the P6 program.
const P = require('../hp/kit.js').parts;
const P2 = require('../p2/kit.js').parts;
const K = require('../hp/levelkit.js');
const { H, lab2 } = P;
module.exports = () => [
  H('Cut-outs', 'For the Level 6 program. Cut along the dashed lines and keep the pieces in one envelope.'),
  lab2('Unplugged code cards (Lessons 1, 4 and 7)'), K.codeCards(),
  '<div class="brk"></div>', H('Square grid', 'For Lessons 7 and 9.'), K.grid()
];
