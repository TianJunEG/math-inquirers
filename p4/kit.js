// Cut-out kit for the P4 program.
const P = require('../hp/kit.js').parts;
const P2 = require('../p2/kit.js').parts;
const K = require('../hp/levelkit.js');
const X = require('./kit_extra.js');
const { H, lab2 } = P;
module.exports = () => [
  H('Cut-outs', 'For the P4 program. Cut along the dashed lines and keep the pieces in one envelope.'),
  lab2('Fraction wall (Lesson 4)'), K.fractionWall(),
  '<div class="brk"></div>', H('Square grid', 'For Lessons 7 and 8. Cut it into 1 cm squares if you need paper squares.'), K.grid(),
  '<div class="brk"></div>', H('Dot grid', 'For Lesson 8 (symmetry).'), K.dots(),
  '<div class="brk"></div>', H('Cube net', 'For Lesson 8.'), K.cubeNet(),
  lab2('Right-angle testers (Lesson 6)'), K.rightAngle(),
  '<div class="brk"></div>', H('Print on a transparency sheet (OHP film)', 'Fallback for Lesson 6 only. A real clear plastic protractor from school is the first choice. Use inkjet or laser film to match your printer, print at 100% actual size and check the 5 cm bar. On paper you cannot see through it: use it only to estimate and compare angles, never to measure.'), X.protractorPage(),
  '<div class="brk"></div>', H('Digit, point, sign and bracket cards', 'For Lessons 2, 3, 5 and 10. Two sets of the digits 0 to 9, four decimal points, the four signs twice and two pairs of brackets.'), X.cards(),
  '<div class="brk"></div>', H('Graph grids', 'For Lesson 9. Fill in the scale before you plot.'), X.graphGrids(),
  '<div class="brk"></div>', H('Paper clock, pizza circles and what to bring', 'For Lessons 4 and 6.'), X.clockPage()
];
