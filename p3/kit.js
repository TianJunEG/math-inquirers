// Cut-out kit for the P3 program.
const P = require('../hp/kit.js').parts;
const P2 = require('../p2/kit.js').parts;
const K = require('../hp/levelkit.js');
const { H, lab2 } = P;
module.exports = () => [
  H('Cut-outs', 'For the Level 3 program. Cut along the dashed lines and keep the pieces in one envelope.'),
  lab2('Digit cards (Lessons 1 and 2)'), P2.digits(),
  '<div class="brk"></div>', H('Fraction wall', 'For Lesson 6. Cut the strips apart.'), K.fractionWall(),
  '<div class="brk"></div>', H('Square grid', 'For Lesson 7. Each square is one unit.'), K.grid(),
  lab2('Right-angle testers (Lesson 8)'), K.rightAngle(),
  '<div class="brk"></div>', H('Play coins', 'For Lesson 9.'), P.coins(),
  '<div class="brk"></div>', H('Play notes and $1 coins', 'For Lesson 9.'), P.notes()
];
