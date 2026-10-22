# Copy the P2 builders to another level with level text swapped.  python3 levels/mklevel.py 3
import sys, re
N = int(sys.argv[1]); R = '/home/claude/math-inquirers/'
AGE = {3: 'ages 9 to 10', 4: 'ages 10 to 11', 5: 'ages 11 to 12', 6: 'ages 12'}
NEXT = {3: 'going into P4', 4: 'going into P5', 5: 'going into P6, the PSLE year', 6: 'after the PSLE, going into Secondary 1'}
FINISH = {6: 'Primary 6 students after the PSLE'}
KITTEXT = {
 3: "'Cut-outs used: digit cards (Lessons 1, 2), fraction wall (Lesson 6), square grid (Lesson 7), right-angle tester (Lesson 8), play coins and notes (Lesson 9).'",
 4: "'Cut-outs used: square grid and dot grid (Lessons 7, 8), cube net (Lesson 8), fraction wall (Lesson 4), right-angle tester (Lesson 6). Children need their own protractor for Lesson 6.'",
 5: "'Cut-outs used: square grid and dot grid (Lessons 4, 8), fraction wall (Lessons 2, 3), cube net (Lesson 5). Children need a protractor and a ruler.'",
 6: "'Each child needs a computer or tablet with Scratch 3 (free online). Python is optional (any online Python editor). Cut-outs used: unplugged code cards (Lessons 1, 4, 7), square grid (Lessons 7, 9).'",
}
KIT = {
 3: "lab2('Digit cards (Lessons 1 and 2)'), P2.digits(),\n  '<div class=\"brk\"></div>', H('Fraction wall', 'For Lesson 6. Cut the strips apart.'), K.fractionWall(),\n  '<div class=\"brk\"></div>', H('Square grid', 'For Lesson 7. Each square is one unit.'), K.grid(),\n  lab2('Right-angle testers (Lesson 8)'), K.rightAngle(),\n  '<div class=\"brk\"></div>', H('Play coins', 'For Lesson 9.'), P.coins(),\n  '<div class=\"brk\"></div>', H('Play notes and $1 coins', 'For Lesson 9.'), P.notes()",
 4: "lab2('Fraction wall (Lesson 4)'), K.fractionWall(),\n  '<div class=\"brk\"></div>', H('Square grid', 'For Lessons 7 and 8.'), K.grid(),\n  '<div class=\"brk\"></div>', H('Dot grid', 'For Lesson 8 (symmetry).'), K.dots(),\n  '<div class=\"brk\"></div>', H('Cube net', 'For Lesson 8.'), K.cubeNet(),\n  lab2('Right-angle testers (Lesson 6)'), K.rightAngle()",
 5: "lab2('Fraction wall (Lessons 2 and 3)'), K.fractionWall(),\n  '<div class=\"brk\"></div>', H('Square grid', 'For Lesson 4 (triangle areas).'), K.grid(),\n  '<div class=\"brk\"></div>', H('Dot grid', 'For Lesson 8.'), K.dots(),\n  '<div class=\"brk\"></div>', H('Cube net', 'For Lesson 5 (volume).'), K.cubeNet()",
 6: "lab2('Unplugged code cards (Lessons 1, 4 and 7)'), K.codeCards(),\n  '<div class=\"brk\"></div>', H('Square grid', 'For Lessons 7 and 9.'), K.grid()",
}
def sub(s):
    s = s.replace('ages 8 to 9', AGE[N]).replace('going into P3', NEXT[N])
    s = s.replace('Primary 2', 'Primary %d' % N).replace('PRIMARY 2', 'PRIMARY %d' % N).replace('Level 2', 'Level %d' % N).replace('LEVEL 2', 'LEVEL %d' % N).replace('Level2_', 'Level%d_' % N).replace('P2', 'P%d' % N).replace("'./kit.js'", "'./kit.js'")
    return s
for f in ['data.js', 'workbook_html.js', 'wb_pdf.py', 'guide.js']:
    s = sub(open(R + 'p2/' + f).read())
    if f == 'guide.js':
        s = re.sub(r"'Cut-outs used:[^']*'", KITTEXT[N], s)
        s = s.replace("Needed: the printed workbook and cut-outs, 20 counters or small objects, scissors, a split pin or short pencil for the clock, paper and a pencil.",
                      "Needed: the printed workbook and cut-outs, scissors, a ruler, paper and a pencil" + (", and a computer with Scratch." if N == 6 else "."))
        s = s.replace("'Print the workbook and cut-outs, and keep counters, scissors and a pencil ready.'", "'Print the workbook and cut-outs, and keep scissors, a ruler and a pencil ready.'")
        if N == 6:
            s = s.replace('children finishing Primary 6', 'Primary 6 students after the PSLE').replace('Children finishing Primary 6', 'Primary 6 students after the PSLE')
    open(R + 'p%d/' % N + f, 'w').write(s)
open(R + 'p%d/kit.js' % N, 'w').write(f"""// Cut-out kit for the P{N} program.
const P = require('../hp/kit.js').parts;
const P2 = require('../p2/kit.js').parts;
const K = require('../hp/levelkit.js');
const {{ H, lab2 }} = P;
module.exports = () => [
  H('Cut-outs', 'For the Level {N} program. Cut along the dashed lines and keep the pieces in one envelope.'),
  {KIT[N]}
];
""")
print('level', N, 'builders written')
