import json, sys
# level -> (lo, hi) grade band (grade ~ age - 5): L1 ages 6-8 -> grades 1-3 ... L6 ages 11-13 -> grades 6-8
BAND = {1: (1, 3), 2: (2, 4), 3: (3, 5), 4: (4, 6), 5: (5, 7), 6: (6, 8)}
J = ['ON', 'US', 'AU', 'IN']
# (lesson id, short topic, {jur: (grade|None, tag, note)})   tag '?' = [UNVERIFIED] grade
M = 'MIXED'
D = [
 ('1.1', 'Skip counting 2/3/5, add-or-take-away rules', dict(ON=(1,'?',''), US=(2,'','2.NBT.2'), AU=(1,'','Y1 A01'), IN=(1,'?',''))),
 ('1.2', 'Number bonds to 10 and 20, equal sign', dict(ON=(1,'','G1 equality'), US=(1,'','K bonds to 10'), AU=(1,'','F bonds to 10'), IN=(1,'','Cl1 "Making 10"'))),
 ('1.3', 'Picture graphs, reading a class vote', dict(ON=(1,'',''), US=(2,'','2.MD.10'), AU=(1,'','Y1 ST02'), IN=(2,'','Cl2 Data Handling'))),
 ('1.4', 'Repeating and growing patterns', dict(ON=(2,'','growing G4'), US=(3,'','shape pat. G4'), AU=(1,'','growing Y2'), IN=(1,'?','Cl4 patterns ch.'))),
 ('1.5', 'Working backwards, number machines', dict(ON=(4,'','unknowns G4'), US=(2,'','2.OA.1'), AU=(3,'','Y3 A01'), IN=(3,'?',''))),
 ('1.6', 'Coin combinations (money)', dict(ON=(2,'','coin combos G2'), US=(2,'','MA also G1'), AU=(3,'','Y3 M06'), IN=(1,'','Cl1 rupee coins'))),
 ('1.7', '2D shapes, counting triangles, composing', dict(ON=(1,'',''), US=(1,'','1.G.1-2'), AU=(1,'',''), IN=(2,'','Cl2 shapes'))),
 ('1.8', 'Logic, Venn sorting, logic grid', dict(ON=(None,'','sorting G1'), US=(None,'','sorting K'), AU=(None,'','sorting F'), IN=(None,'','puzzles = NCF theme'))),
 ('1.9', 'Length: ruler, units, convert', dict(ON=(2,'','metric rel. G4'), US=(2,'','convert G4'), AU=(3,'','informal Y1'), IN=(3,'','NCF Prep: std units'))),
 ('1.10', 'Challenge Day (mixed puzzles)', M),
 ('2.1', 'Numbers to 1000, digit cards', dict(ON=(3,'','G3 to 1000'), US=(2,'','2.NBT'), AU=(2,'','Y2 N01'), IN=(3,'?','Cl3 Hundreds ch.'))),
 ('2.2', 'Add/subtract within 1000, missing digits', dict(ON=(3,'?',''), US=(2,'','2.NBT.7'), AU=(3,'','Y3 N03'), IN=(3,'','Cl3 Give and Take'))),
 ('2.3', 'Multiplication, division, arrays', dict(ON=(3,'','G3 rows/cols'), US=(3,'','arrays G2'), AU=(2,'','Y2 N05'), IN=(2,'','Cl2 Grouping'))),
 ('2.4', 'Pattern machines, far places, multiples', dict(ON=(4,'?',''), US=(4,'','3.OA.9 G3'), AU=(3,'','rules Y6'), IN=(4,'','Cl4 Patterns'))),
 ('2.5', 'Mystery number machines, 2-step backwards', dict(ON=(4,'','G4 unknowns'), US=(3,'','3.OA.8'), AU=(3,'','x/div Y5'), IN=(4,'?',''))),
 ('2.6', 'Money, change, working backwards', dict(ON=(3,'','change G3'), US=(2,'','2.MD.8'), AU=(3,'','Y3 M06'), IN=(2,'?',''))),
 ('2.7', 'Fractions: unit, compare, add like', dict(ON=(3,'','add/sub G5'), US=(3,'','add/sub G4'), AU=(3,'','add/sub Y5'), IN=(3,'?','Cl3 Fair Share'))),
 ('2.8', 'Shape builders: composing, cubes, nets', dict(ON=(3,'?',''), US=(1,'','vol. G5, nets G6'), AU=(4,'','nets Y5'), IN=(4,'?',''))),
 ('2.9', 'Mass, volume, length, time to 5 min', dict(ON=(3,'',''), US=(3,'','5-min G2'), AU=(3,'','a.m./p.m. Y4'), IN=(3,'','Cl3 Filling, Time'))),
 ('2.10', 'Challenge Day (mixed puzzles)', M),
 ('3.1', 'Numbers to 10 000', dict(ON=(4,'','G4 to 10 000'), US=(4,'','4.NBT'), AU=(3,'','Y3 N01'), IN=(4,'','Cl4 Thousands'))),
 ('3.2', 'Add/subtract 4-digit, cryptarithms', dict(ON=(4,'?',''), US=(4,'','4.NBT.4'), AU=(4,'','Y4 N06'), IN=(4,'?',''))),
 ('3.3', 'Times tables 6-9, patterns', dict(ON=(4,'','to 10x10 G4'), US=(3,'','3.OA.7'), AU=(4,'','Y4 A02'), IN=(3,'','NCF Prep: to 10x10'))),
 ('3.4', 'Bar-model word problems', dict(ON=(3,'?',''), US=(3,'','3.OA.8; 4.OA.2'), AU=(3,'','Y2-Y4 elab.'), IN=(3,'?',''))),
 ('3.5', 'Division with remainders', dict(ON=(4,'','G4 2-3 digit'), US=(4,'','4.NBT.6'), AU=(5,'','Y5 N07'), IN=(4,'?',''))),
 ('3.6', 'Fraction walls, equivalent fractions', dict(ON=(5,'?',''), US=(3,'','add/sub G4-5'), AU=(4,'','add/sub Y5'), IN=(5,'?','Cl5 Fractions'))),
 ('3.7', 'Area and perimeter of figures', dict(ON=(3,'','area G3'), US=(3,'','3.MD.5-8'), AU=(4,'','Y4 M02'), IN=(5,'?','Cl6 ch.6 confirmed'))),
 ('3.8', 'Angles, perpendicular, parallel', dict(ON=(4,'?',''), US=(4,'','4.MD.5-7, 4.G.1'), AU=(3,'','Y3 M05'), IN=(5,'','Cl5 Angles as Turns'))),
 ('3.9', 'Compound units, budget, 12/24-hour', dict(ON=(4,'?','budget G5'), US=(4,'','4.MD.1-2; 24h none'), AU=(5,'','conv. Y6'), IN=(5,'?',''))),
 ('3.10', 'Challenge Day (bar graph, logic)', M),
 ('4.1', 'Factors, multiples, factor pairs', dict(ON=(7,'?','overview G7'), US=(4,'','4.OA.4'), AU=(5,'','Y5 N02'), IN=(6,'','Cl6 Prime Time'))),
 ('4.2', 'Numbers to 100 000, rounding, estimating', dict(ON=(5,'','G5 to 100 000'), US=(4,'','4.NBT.3'), AU=(4,'','Y4 N07'), IN=(5,'?',''))),
 ('4.3', 'Order of operations, missing signs', dict(ON=(6,'?',''), US=(5,'','5.OA.1; 6.EE'), AU=(6,'','Y6 A02'), IN=(7,'?','Cl7 Arith. Expr.'))),
 ('4.4', 'Improper/mixed, fraction of a set, compare', dict(ON=(5,'?',''), US=(4,'','4.NF'), AU=(4,'','Y4 N04'), IN=(5,'?',''))),
 ('4.5', 'Decimals to 3 places, rounding', dict(ON=(4,'','G4 intro'), US=(4,'','4.NF.5-7'), AU=(4,'','Y4 N01'), IN=(7,'','Cl7 ch.3 (new series)'))),
 ('4.6', 'Angles: protractor, clock, compass turns', dict(ON=(6,'','protractor G6'), US=(4,'','4.MD.6'), AU=(5,'','Y5 M04'), IN=(6,'','Cl6 Lines/Angles'))),
 ('4.7', 'Composite area/perimeter', dict(ON=(5,'?',''), US=(3,'','3.MD.7d'), AU=(5,'','Y5 M02'), IN=(6,'','Cl6 ch.6'))),
 ('4.8', 'Symmetry and nets', dict(ON=(4,'?',''), US=(4,'','nets G6'), AU=(4,'','nets Y5'), IN=(4,'','Cl4 Symmetry'))),
 ('4.9', 'Line graphs, tables, misleading scales', dict(ON=(5,'','broken-line G6'), US=(None,'','5.MD.2 line plot only'), AU=(5,'','Y5 ST02'), IN=(6,'?','NCF Middle'))),
 ('4.10', 'Challenge Day (heuristics)', M),
 ('5.1', 'Numbers to 10 million, digit riddles', dict(ON=(7,'','to 1 billion'), US=(4,'?','to 1 000 000'), AU=(3,'?','"beyond 10 000"'), IN=(7,'','Cl7 lakh/crore/million'))),
 ('5.2', 'Fractions and division, divide fraction by whole', dict(ON=(7,'?',''), US=(5,'','5.NF.3, 5.NF.7'), AU=(7,'?','Y7 N06'), IN=(7,'?','Cl7 ch.8'))),
 ('5.3', 'Fraction word problems, before and after', dict(ON=(6,'?',''), US=(5,'','5.NF.6'), AU=(6,'?',''), IN=(7,'?',''))),
 ('5.4', 'Area of a triangle', dict(ON=(5,'?',''), US=(6,'','6.G.1'), AU=(7,'','Y7 M01'), IN=(7,'?','NCF Middle'))),
 ('5.5', 'Volume of cuboids, water tanks', dict(ON=(6,'?',''), US=(5,'','5.MD.3-5'), AU=(7,'','Y7 M02'), IN=(8,'?',''))),
 ('5.6', 'Rate, price per item, work rate', dict(ON=(7,'?',''), US=(6,'','6.RP.2-3'), AU=(7,'','Y7 N08 ratio'), IN=(8,'','Cl8 Proportional'))),
 ('5.7', 'Percentage, discount, GST', dict(ON=(5,'','intro G5'), US=(6,'','disc./tax G7'), AU=(5,'','disc. Y6'), IN=(7,'?','NCF Middle'))),
 ('5.8', 'Angle chasing (triangle, parallelogram)', dict(ON=(5,'?','parallel G8'), US=(7,'','7.G.5; 8.G.5'), AU=(6,'','tri. sum Y7'), IN=(7,'','Cl7 ch.5, ch.7'))),
 ('5.9', 'Pattern generalisers, nth term in words', dict(ON=(6,'?',''), US=(6,'','6.EE'), AU=(6,'','Y6 A01'), IN=(6,'','Cl6 Patterns ch.1'))),
 ('5.10', 'Challenge Day (strategies)', M),
 ('6.1', 'Sequences, nth term (+ Scratch loop)', dict(ON=(6,'?','coding each grade'), US=(6,'?',''), AU=(6,'','Y6 A01, A03'), IN=(6,'','Cl6 ch.1'))),
 ('6.2', 'Primes, prime factorisation (+ mod code)', dict(ON=(7,'?',''), US=(4,'','pr. fact. G6'), AU=(6,'','pr. fact. Y7'), IN=(6,'?','Cl6 Prime Time'))),
 ('6.3', 'Negative numbers', dict(ON=(6,'','integers G6'), US=(6,'','6.NS.5-7'), AU=(6,'','Y6 N01'), IN=(6,'','Cl6 ch.10'))),
 ('6.4', 'Algebra machines, letter rules, equations', dict(ON=(5,'','multi-term G7'), US=(6,'','6.EE.2,7'), AU=(7,'','Y7 A01-03'), IN=(7,'','Cl7 ch.4'))),
 ('6.5', 'Counting every possible way', dict(ON=(None,'','prob. only'), US=(7,'','7.SP.8; perm. HS'), AU=(None,'','Y7 single-stage'), IN=(5,'','NCF Prep C-4.2'))),
 ('6.6', 'Probability, 2 dice, fair games, simulation', dict(ON=(6,'?','complex G8'), US=(7,'','7.SP.5-8'), AU=(6,'','Y6 P01-02'), IN=(9,'','NCF: Secondary'))),
 ('6.7', 'Turtle geometry, polygon angles', dict(ON=(7,'?','code G4, G7'), US=(8,'?',''), AU=(7,'','Y7 M05'), IN=(8,'?',''))),
 ('6.8', 'Clock arithmetic, mod, Caesar cipher', dict(ON=(None,'',''), US=(None,'',''), AU=(None,'',''), IN=(None,'','Cl8 remainders partial'))),
 ('6.9', 'Mean, median, mode, levelling out', dict(ON=(6,'?','overview: "averages" from G3'), US=(6,'','6.SP.5; MA +mode'), AU=(7,'','Y7 ST01'), IN=(7,'?','NCF Middle C-5.1'))),
 ('6.10', 'Showcase Challenge (maths + code)', M),
]

def label(level, g, tag):
    lo, hi = BAND[level]
    if g is None:
        return 'NOT'
    if g < lo:
        s = 'EARLIER'
    elif g > hi:
        s = 'LATER'
    else:
        s = 'SAME'
    return s

def cell(level, v, j):
    if v == M:
        return 'MIXED'
    g, tag, note = v[j]
    lab = label(level, g, tag)
    pre = {'ON': 'G', 'US': 'G', 'AU': 'Y', 'IN': 'Cl'}[j]
    if g is None:
        out = 'NOT'
    else:
        gg = ('K' if g == 0 else str(g))
        out = '%s %s%s%s' % (lab, pre, gg, tag)
    if note:
        out += ' (%s)' % note
    return out

rows = []
tally = {l: {j: {'SAME': 0, 'EARLIER': 0, 'LATER': 0, 'NOT': 0, 'MIXED': 0} for j in J} for l in range(1, 7)}
for lid, topic, v in D:
    level = int(lid.split('.')[0])
    cs = []
    for j in J:
        c = cell(level, v, j)
        k = c.split(' ')[0]
        tally[level][j][k] += 1
        cs.append(c)
    rows.append('| L%s | %s | %s |' % (lid, topic, ' | '.join(cs)))
matrix = '\n'.join(['| Lesson | Topic | Ontario (Grade) | USA CCSS/MA (Grade) | Australia / Victoria (Year / Level) | India NCERT (Class) |', '|---|---|---|---|---|---|'] + rows)
tl = ['| Program level (ages) | Jurisdiction | SAME | EARLIER | LATER | NOT | MIXED |', '|---|---|---|---|---|---|---|']
tot = {j: {'SAME': 0, 'EARLIER': 0, 'LATER': 0, 'NOT': 0, 'MIXED': 0} for j in J}
names = {'ON': 'Ontario', 'US': 'USA', 'AU': 'Australia', 'IN': 'India'}
ages = {1: '6-8', 2: '7-9', 3: '8-10', 4: '9-11', 5: '10-12', 6: '11-13'}
for l in range(1, 7):
    for j in J:
        t = tally[l][j]
        tl.append('| Level %d (%s) | %s | %d | %d | %d | %d | %d |' % (l, ages[l], names[j], t['SAME'], t['EARLIER'], t['LATER'], t['NOT'], t['MIXED']))
        for k in t:
            tot[j][k] += t[k]
for j in J:
    t = tot[j]
    tl.append('| **All 60** | **%s** | **%d** | **%d** | **%d** | **%d** | **%d** |' % (names[j], t['SAME'], t['EARLIER'], t['LATER'], t['NOT'], t['MIXED']))
open(sys.argv[1], 'w').write(matrix)
open(sys.argv[2], 'w').write('\n'.join(tl))
print(len(D), tot)
unv = sum(1 for _, _, v in D if v != M for j in J if v[j][1] == '?')
print('unverified cells', unv, 'of', sum(1 for _, _, v in D if v != M) * 4)
