// Cut-out kit for the P4 program.
const P = require('../hp/kit.js').parts;
const P2 = require('../p2/kit.js').parts;
const K = require('../hp/levelkit.js');
const { H, lab2 } = P;
module.exports = () => [
  H('Cut-outs', 'For the P4 program. Cut along the dashed lines and keep the pieces in one envelope.'),
  lab2('Fraction wall (Lesson 4)'), K.fractionWall(),
  '<div class="brk"></div>', H('Square grid', 'For Lessons 7 and 8.'), K.grid(),
  '<div class="brk"></div>', H('Dot grid', 'For Lesson 8 (symmetry).'), K.dots(),
  '<div class="brk"></div>', H('Cube net', 'For Lesson 8.'), K.cubeNet(),
  lab2('Right-angle testers (Lesson 6)'), K.rightAngle()
];
