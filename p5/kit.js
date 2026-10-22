// Cut-out kit for the P5 program.
const P = require('../hp/kit.js').parts;
const P2 = require('../p2/kit.js').parts;
const K = require('../hp/levelkit.js');
const { H, lab2 } = P;
module.exports = () => [
  H('Cut-outs', 'For the Level 5 program. Cut along the dashed lines and keep the pieces in one envelope.'),
  lab2('Fraction wall (Lessons 2 and 3)'), K.fractionWall(),
  '<div class="brk"></div>', H('Square grid', 'For Lesson 4 (triangle areas).'), K.grid(),
  '<div class="brk"></div>', H('Dot grid', 'For Lesson 8.'), K.dots(),
  '<div class="brk"></div>', H('Cube net', 'For Lesson 5 (volume).'), K.cubeNet()
];
