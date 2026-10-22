import collections
# cell: (code, text)  code in S,E,L,N,X
S='SAME';E='EARLIER';L='LATER';N='NOT';X='n/a'
def c(code,txt): return (code,txt)
rows=[]
def r(lid,title,hk,cn,jp,kr): rows.append((lid,title,hk,cn,jp,kr))
mix=c('X','mixed review, not mapped')
# ---------- Level 1 (g=1) ----------
r('1.1','Count with the Frog: skip counting, rules',
 c('S','SAME P1 (skip-count 2/5/10; rule-finding not a unit)'),c('S','SAME G1-2 (patterns)'),c('S','SAME G1-2 (number sequence G1; groups G2; rules not named)'),c('S','SAME G1-2 (patterns)'))
r('1.2','Number Bond Inquiry',
 c('S','SAME P1 (add/sub to 20)'),c('S','SAME G1-2 (add/sub within 20)'),c('S','SAME G1 (numbers as sum/difference; ten as a unit)'),c('S','SAME G1-2 (compose/decompose)'))
r('1.3','Fruit Party: picture graphs',
 c('L','LATER P2 (pictograms)'),c('S','SAME G1-2 (classification only; pictogram not named)'),c('S','SAME G1 (pictures for quantities; tables/graphs G2)'),c('S','SAME G1-2 (graphs with symbols)'))
r('1.4','Pattern Inquiry: repeating, growing',
 c('N','NOT (no pattern unit; algebra P5)'),c('S','SAME G1-2 (pattern rules)'),c('N','NOT as a topic (functions G4)'),c('S','SAME G1-2 (repeat/increase rules)'))
r('1.5','Mystery Number: working backwards',
 c('L','LATER P5 (equations)'),c('S','SAME G1-2 (inverse operations only)'),c('L','LATER G3 (box-expressions; inverse relation G2)'),c('S','SAME G1-2 (box in +/- sentences)'))
r('1.6','Coin Combos: money',
 c('S','SAME P1 (Money I)'),c('S','SAME G1-2 (RMB, thematic activity)'),c('N','NOT listed'),c('N','NOT listed'))
r('1.7','Shape Safari: 2D shapes',
 c('S','SAME P1'),c('S','SAME G1-2'),c('S','SAME G1 (formal triangles/quadrilaterals G2)'),c('S','SAME G1-2'))
r('1.8','Logic Lab: sorting, Venn, logic',
 c('S','SAME P1 (enrichment topics only)'),c('S','SAME G1-2 (classification; logic grids not named)'),c('L','LATER G2 (classify into tables); Venn/grids not named'),c('S','SAME G1-2 (classification)'))
r('1.9','Measure It!: length',
 c('S','SAME P1'),c('S','SAME G1-2'),c('L','LATER G2 (standard units cm/m; comparison G1)'),c('S','SAME G1-2'))
r('1.10','Challenge Day (mixed)',mix,mix,mix,mix)
# ---------- Level 2 (g=2) ----------
r('2.1','Digit Detectives: numbers to 1000',
 c('S','SAME P2'),c('S','SAME G1-2 (to 10 000)'),c('S','SAME G2 (3-digit simple G1; 4-digit G2)'),c('S','SAME G1-2 (to 4 digits)'))
r('2.2','Missing Digits: 3-digit add/sub',
 c('S','SAME P2 (with borrowing)'),c('S','SAME G1-2'),c('S','SAME G2-3 (simple 3-digit G2)'),c('L','LATER G3-4 (3-digit add/sub)'))
r('2.3','Legs, Wheels, Arrays: multiplication, division',
 c('S','SAME P2'),c('S','SAME G1-2 (table facts)'),c('S','SAME G2 (x); division G3'),c('S','SAME G1-2 (x tables); division G3-4'))
r('2.4','Pattern Machines: patterns with multiplication',
 c('S','SAME P2 (tables); growth rules not a unit'),c('S','SAME G1-4 (pattern rules)'),c('S','SAME G2 (table patterns); growth tables G4'),c('S','SAME G1-4 (patterns)'))
r('2.5','Mystery Number Machines: two-step backwards, bar models',
 c('L','LATER P5 (equations)'),c('L','LATER G5-6 (equality property)'),c('L','LATER G3 (box-expressions)'),c('S','SAME G1-2 (box, +/- only)'))
r('2.6','Market Day: money',
 c('S','SAME P2 (Money II)'),c('S','SAME G1-2 (RMB)'),c('N','NOT listed'),c('N','NOT listed'))
r('2.7','Fair Shares: fractions',
 c('L','LATER P3 (Fractions I)'),c('L','LATER G3-4'),c('S','SAME G2 (1/2, 1/4); unit fractions, add/sub G3'),c('L','LATER G3-4'))
r('2.8','Shape Builders: 2D/3D, cubes, nets',
 c('S','SAME P2 (3-D II); nets P5'),c('S','SAME G1-2 (solids, building); nets G5-6'),c('S','SAME G2 (boxes); nets G4'),c('S','SAME G1-2 (cube stacks); nets G5-6'))
r('2.9','Measure Masters: m, cm, g, kg, litre, time',
 c('L','LATER P3 (g/kg, L); time, length P1-2'),c('S','SAME G1-2 (length, time); g/kg G3-4; L/mL G5-6'),c('S','SAME G2 (length, L/dL/mL, time); g/kg G3'),c('S','SAME G1-2 (length, time); L, g, kg G3-4'))
r('2.10','Challenge Day (mixed)',mix,mix,mix,mix)
# ---------- Level 3 (g=3) ----------
r('3.1','Number Sleuths: numbers to 10 000',
 c('E','EARLIER P2'),c('E','EARLIER G1-2'),c('E','EARLIER G2'),c('E','EARLIER G1-2'))
r('3.2','Cryptarithms: 4-digit add/sub',
 c('S','SAME P3'),c('S','SAME G3-4'),c('S','SAME G3'),c('S','SAME G3-4'))
r('3.3','Times Table Treasure: 6-9 tables',
 c('E','EARLIER P2 (tables 0-10)'),c('E','EARLIER G1-2'),c('E','EARLIER G2 (to 9x9)'),c('E','EARLIER G1-2'))
r('3.4','Model Makers: bar-model word problems',
 c('S','SAME P3-4 (4-operation problems; bar model not named)'),c('S','SAME G3-4 (addition/multiplication models; bar model not named)'),c('S','SAME G3-4 (diagrams generic; tape diagram not named)'),c('S','SAME G3-4 (bar model not named)'))
r('3.5','Remainder Riddles: division with remainders',
 c('S','SAME P3 (concept P2)'),c('S','SAME G3-4 (remainder not named in text read)'),c('S','SAME G3'),c('S','SAME G3-4'))
r('3.6','Fraction Walls: equivalent, compare, add/sub',
 c('S','SAME P3 (equivalent P3; reduce/expand P4)'),c('S','SAME G3-4 (like denominators); equivalent G5-6'),c('S','SAME G3-4 (unit fractions G3; equal fractions G4)'),c('S','SAME G3-4 (like denominators); equivalent G5-6'))
r('3.7','Area Architects: area and perimeter',
 c('L','LATER P4'),c('S','SAME G3-4'),c('L','LATER G4 (area); perimeter not itemised'),c('L','LATER G5-6'))
r('3.8','Angle and Line Detectives: angles, perpendicular, parallel',
 c('S','SAME P2-3 (angles, perpendicular P2; parallel P3)'),c('S','SAME G3-4'),c('S','SAME G3-4 (angles G3; parallel/perpendicular G4)'),c('S','SAME G3-4'))
r('3.9','Measure and Money: compound units, budgets, 24-hour time',
 c('S','SAME P3 (24-hour time P3)'),c('S','SAME G3-4 (24-hour time, mass units; RMB earlier)'),c('S','SAME G3 (km, g/kg, seconds); money/24-hour not listed'),c('S','SAME G3-4 (units, durations); money not listed'))
r('3.10','Challenge Day: bar graphs, logic',
 c('S','SAME P3 (bar charts; scales P4)'),c('S','SAME G3-4 (bar charts); logic grids not named'),c('S','SAME G3 (bar graphs); logic grids not named'),c('S','SAME G3-4 (bar graphs); logic grids not named'))
# ---------- Level 4 (g=4) ----------
r('4.1','Factor Hunters: factors, multiples',
 c('S','SAME P4'),c('L','LATER G5-6'),c('L','LATER G5'),c('L','LATER G5-6'))
r('4.2','Big Number Puzzles: 5-digit, rounding, estimation',
 c('E','EARLIER P3 (5-digit); rounding P5'),c('S','SAME G3-4 (large numbers, estimation); rounding not named'),c('S','SAME G4 (rounding; oku and cho units)'),c('L','LATER G5-6 (rounding); numbers >10 000 G3-4'))
r('4.3','Operation Detectives: order of operations',
 c('E','EARLIER P3 (brackets, mixed operations)'),c('S','SAME G3-4 (mixed, up to 3 steps)'),c('S','SAME G4'),c('L','LATER G5-6'))
r('4.4','Fraction Frontier: improper/mixed, fraction of a set',
 c('S','SAME P4'),c('L','LATER G5-6 (common denominators)'),c('S','SAME G4 (terms); unlike denominators G5'),c('S','SAME G3-4 (improper/mixed); unlike denominators G5-6'))
r('4.5','Decimal Detectives: decimals to 3 places',
 c('S','SAME P4 (to 4 d.p.)'),c('S','SAME G3-4 (initial decimals)'),c('S','SAME G4 (tenths G3)'),c('S','SAME G3-4 (to 3 places)'))
r('4.6','Angle Turns: protractor, clock, compass',
 c('L','LATER P6 (degree unit)'),c('S','SAME G3-4 (protractor)'),c('S','SAME G4'),c('S','SAME G3-4'))
r('4.7','Area Architects II: composite area, perimeter',
 c('S','SAME P4 (composites P5)'),c('S','SAME G3-4 (rectangle/square)'),c('S','SAME G4 (composites in activities)'),c('L','LATER G5-6'))
r('4.8','Symmetry and Nets',
 c('L','LATER P5-6 (nets P5, symmetry P6)'),c('L','LATER G5-6 (nets, axes); intuitive G3-4'),c('L','LATER G6 (symmetry); nets G4'),c('L','LATER G5-6 (nets, symmetry); reflection G3-4'))
r('4.9','Data Detectives: tables, line graphs',
 c('L','LATER P6 (broken-line graphs)'),c('L','LATER G5-6 (line charts)'),c('S','SAME G4'),c('S','SAME G3-4'))
r('4.10','Challenge Day (mixed heuristics)',mix,mix,mix,mix)
# ---------- Level 5 (g=5) ----------
r('5.1','Million Puzzles: numbers to 10 million',
 c('S','SAME P5'),c('E','EARLIER G3-4 (wan, yi units)'),c('E','EARLIER G4 (oku, cho)'),c('E','EARLIER G3-4'))
r('5.2','Fraction Feats: fractions and division, 4 operations',
 c('S','SAME P5'),c('S','SAME G5-6'),c('S','SAME G5 (division as fraction); x and / by fractions G6'),c('S','SAME G5-6'))
r('5.3','Before and After: fraction word problems',
 c('S','SAME P5'),c('S','SAME G5-6'),c('S','SAME G5-6 (add/sub G5; x, / G6)'),c('S','SAME G5-6'))
r('5.4','Triangle Areas',
 c('S','SAME P5'),c('S','SAME G5-6'),c('S','SAME G5'),c('S','SAME G5-6'))
r('5.5','Volume Vault: cuboid volume',
 c('S','SAME P5'),c('S','SAME G5-6'),c('S','SAME G5'),c('S','SAME G5-6'))
r('5.6','Rate Racers: unit rate, speed',
 c('L','LATER P6 (speed)'),c('E','EARLIER G3-4 (price/speed relations); ratio G5-6'),c('S','SAME G5 (per-unit quantity, speed)'),c('S','SAME G5-6 (ratio/rate; speed not listed)'))
r('5.7','Percentage Puzzles: discount, GST',
 c('L','LATER P6'),c('S','SAME G5-6'),c('S','SAME G5'),c('S','SAME G5-6'))
r('5.8','Angle Chasers: triangle/quadrilateral angles',
 c('N','NOT (angle-sum facts not in primary list)'),c('S','SAME G5-6 (triangle 180 degrees)'),c('S','SAME G5'),c('E','EARLIER G3-4'))
r('5.9','Pattern Generalisers: rules in words, 3n+1',
 c('S','SAME P5 (letters for numbers)'),c('S','SAME G5-6 (letters)'),c('E','EARLIER G4 (varying quantities); letters G6'),c('S','SAME G5-6 (correspondence tables)'))
r('5.10','Challenge Day (mixed strategies)',mix,mix,mix,mix)
# ---------- Level 6 (g=6) ----------
r('6.1','Code the Pattern: sequences, nth term',
 c('N','NOT (nth term); letters P5'),c('N','NOT (nth term); letters G5-6'),c('N','NOT (nth term); letters G6'),c('N','NOT (nth term); correspondence G5-6'))
r('6.2','Prime Hunters: primes, factor trees',
 c('E','EARLIER P4 (primes); factor trees secondary'),c('S','SAME G5-6 (primes; factor trees not named)'),c('L','LATER JHS1 (primes since 2017); factors G5'),c('L','LATER middle school (factors G5-6)'))
r('6.3','Below Zero: negative numbers',
 c('N','NOT (secondary)'),c('S','SAME G5-6 (introduced only, thematic)'),c('L','LATER JHS1'),c('L','LATER middle school'))
r('6.4','Algebra Machines: expressions, equations',
 c('E','EARLIER P5 (algebra, equations)'),c('S','SAME G5-6 (letters, equality property); equations secondary'),c('S','SAME G6 (letters); equations JHS1'),c('L','LATER middle school (box/triangle only in primary)'))
r('6.5','Every Possible Way: counting',
 c('N','NOT'),c('S','SAME G5-6 (listing outcomes only)'),c('S','SAME G6 (possible cases)'),c('L','LATER middle school'))
r('6.6','Fair or Unfair?: probability',
 c('N','NOT'),c('S','SAME G5-6 (qualitative)'),c('L','LATER (lower secondary; not in primary)'),c('S','SAME G5-6 (numeric possibility, simple events)'))
r('6.7','Turtle Geometry: polygon angles, coding',
 c('N','NOT (polygon angle sums secondary)'),c('S','SAME G5-6 (triangle sum only)'),c('E','EARLIER G5 (regular polygons, programming example)'),c('E','EARLIER G3-4 (angle sums, regular polygons)'))
r('6.8','Secret Codes: clock arithmetic, ciphers',
 c('N','NOT'),c('N','NOT'),c('N','NOT'),c('N','NOT'))
r('6.9','Data Detectives: mean, median, mode',
 c('S','SAME P6 (average only)'),c('E','EARLIER G3-4 (mean); median/mode not primary'),c('S','SAME G6 (mean, median, mode; mean of measures G5)'),c('S','SAME G5-6 (mean); median/mode middle school'))
r('6.10','Showcase Challenge (mixed + code)',mix,mix,mix,mix)
assert len(rows)==60
def esc(s): return s.replace('|','/')
out=[]
out.append('| # | Lesson (topic) | Hong Kong | Mainland China | Japan | South Korea |')
out.append('|---|---|---|---|---|---|')
tal={k:collections.Counter() for k in ['HK','CN','JP','KR']}
for lid,title,hk,cn,jp,kr in rows:
    out.append('| %s | %s | %s | %s | %s | %s |'%(lid,esc(title),esc(hk[1]),esc(cn[1]),esc(jp[1]),esc(kr[1])))
    for k,cell in zip(['HK','CN','JP','KR'],[hk,cn,jp,kr]): tal[k][cell[0]]+=1
open('/tmp/claude-0/-home-user-math-inquirers/6d6b173e-8eda-5fdf-9c4d-af677bceddc6/scratchpad/mk/matrix.md','w').write('\n'.join(out)+'\n')
t=['| Jurisdiction | SAME | EARLIER | LATER | NOT | mixed (n/a) |','|---|---|---|---|---|---|']
for k,nm in [('HK','Hong Kong'),('CN','Mainland China'),('JP','Japan'),('KR','South Korea')]:
    t.append('| %s | %d | %d | %d | %d | %d |'%(nm,tal[k]['S'],tal[k]['E'],tal[k]['L'],tal[k]['N'],tal[k]['X']))
open('/tmp/claude-0/-home-user-math-inquirers/6d6b173e-8eda-5fdf-9c4d-af677bceddc6/scratchpad/mk/tally.md','w').write('\n'.join(t)+'\n')
print('\n'.join(t))
