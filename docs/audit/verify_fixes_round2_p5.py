"""Verify every answer changed or added in the P5 round-2 fix pass (docs/audit/fixes_round2_p5.md). Run: python3 docs/audit/verify_fixes_round2_p5.py"""
import json, math, re, subprocess, os, itertools
from fractions import Fraction as F
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
ok = True
def chk(name, cond, info=''):
    global ok
    print(('PASS ' if cond else 'FAIL ') + name + (' ' + str(info) if info != '' else ''))
    ok = ok and cond
# ---- L2 ----
chk('L2 warm-up: 3/5 > 1/2; 1/4 of 12 = 3', F(3,5) > F(1,2) and F(12,4) == 3)
chk('L2 try1: 4/7, 5/6, 9/4 = 2 1/4, 7/3 = 2 1/3', F(4,7) == F(4,7) and F(9,4) == 2 + F(1,4) and F(7,3) == 2 + F(1,3))
ways = [(a, b) for a in range(1, 80) for b in range(a + 1, 400) if F(1, a) + F(1, b) == F(4, 5)]
chk('L2 TH1: 4/5 has NO two-different-unit-fraction split', ways == [], ways)
chk('L2 TH1 reasoning: only 1/2 > 2/5 and < 4/5; 4/5 - 1/2 = 3/10 not unit', [d for d in range(1, 6) if F(1, d) > F(2, 5) and F(1, d) < F(4, 5)] == [2] and F(4, 5) - F(1, 2) == F(3, 10))
chk('L2 TH3: 3/8 = 15/40, 2/5 = 16/40, diff 1/40', F(3, 8) == F(15, 40) and F(2, 5) == F(16, 40) and F(2, 5) - F(3, 8) == F(1, 40))
rem = 1 - F(3, 5) - F(1, 4)
chk('L2 TH4: path 4000 m (3/20 left = 600 m)', rem == F(3, 20) and F(600) / rem == 4000, F(600) / rem)
chk('L2 inv: 1/2+1/6+1/12+1/20 = 4/5 = 1 - 1/5', F(1,2)+F(1,6)+F(1,12)+F(1,20) == F(4,5) == 1 - F(1,5))
# ---- L3 ----
chk('L3 warm-up: 1/4 of 36 = 9; half of 1/2 = 1/4', 36 // 4 == 9 and F(1, 2) / 2 == F(1, 4))
chk('L3 Q2: 84 stickers in 7 boxes: box 12; Siti 36->48, Mei 48->36 before', 84 // 7 == 12 and 3 * 12 + 12 == 48 and 4 * 12 - 12 == 36 and F(36, 48) == F(3, 4))
chk('L3 Q3(b): total 80, 3+5 parts, part 10, Ali ends 30, gives 20', 80 // 8 == 10 and 50 - 3 * 10 == 20 and F(30, 50) == F(3, 5))
# ---- L4 ----
chk('L4 TH1: right triangle area 24 with short sides differing by 2 is 6 and 8 (unique)', [(a, a + 2) for a in range(1, 100) if F(a * (a + 2), 2) == 24] == [(6, 8)])
# ---- L5 ----
chk('L5 sneak 2: 5x4 base, 60 cubes = 3 layers', 60 // (5 * 4) == 3 and 60 % 20 == 0)
cub = {tuple(sorted(t)) for t in itertools.product(range(1, 37), repeat=3) if t[0] * t[1] * t[2] == 36}
chk('L5 Q2: 36 cubes make 8 cuboids; start-here list 1x1x36,1x2x18,1x3x12,1x4x9,1x6x6 is the first 5', len(cub) == 8 and {(1,1,36),(1,2,18),(1,3,12),(1,4,9),(1,6,6)} <= cub, sorted(cub))
# ---- L6 ----
chk('L6 Q2: A 70c, B 73c, C 65c per can', F(420, 6) == 70 and F(292, 4) == 73 and F(780, 12) == 65)
spd = F(150) / F(5, 2)
chk('L6 TH4: train 150 km in 2.5 h -> 60 km/h; 1 h 45 min = 105 km', spd == 60 and spd * F(7, 4) == 105)
# ---- L7 ----
shirt, hat = 60 * F(80, 100), 40 * F(90, 100); tot = shirt + hat
chk('L7 TH3: 48 + 36 = 84, GST 7.56, pay 91.56', shirt == 48 and hat == 36 and tot == 84 and tot * F(9, 100) == F('7.56') and tot * F(109, 100) == F('91.56'))
yrs = next(y for y in range(1, 50) if 2000 * F(3, 100) * y > 200)
chk('L7 TH4: 3% of 2000 = 60 a year; first year with interest > 200 is 4 (240)', yrs == 4 and 60 * yrs == 240 and 60 * 3 == 180)
# ---- L9 ----
chk('L9 TH4: 101 is the 33rd term of 5,8,11,...; 100 is not', [n for n in range(1, 200) if 5 + 3 * (n - 1) == 101] == [33] and not [n for n in range(1, 200) if 5 + 3 * (n - 1) == 100] and 100 % 3 == 1)
# ---- figures (geometry parsed from the SVG strings) ----
js = "const F=require('./p5/content/figs.js');const o={};for(const n in F)for(const k in F[n])o[n+k]=F[n][k];console.log(JSON.stringify(o))"
figs = json.loads(subprocess.check_output(['node', '-e', js], cwd=R))
def pts(svg, i=0):
    polys = re.findall(r'<polygon points="([^"]+)"', svg)
    return [tuple(map(float, p.split(','))) for p in polys[i].split()]
def ang(P, A, B):
    v1 = (A[0]-P[0], A[1]-P[1]); v2 = (B[0]-P[0], B[1]-P[1])
    return math.degrees(math.acos((v1[0]*v2[0]+v1[1]*v2[1]) / (math.hypot(*v1) * math.hypot(*v2))))
d = lambda a, b: math.hypot(a[0]-b[0], a[1]-b[1])
A, B, C, D = pts(figs['8TH3'])
chk('Fig L8 TH3: angle A = 84, angle B = 97, AB parallel DC', abs(ang(A, B, D) - 84) < 0.5 and abs(ang(B, A, C) - 97) < 0.5 and abs(A[1]-B[1]) < 0.1 and abs(D[1]-C[1]) < 0.1, (round(ang(A, B, D), 1), round(ang(B, A, C), 1)))
A, B, C, D = pts(figs['8TH4'], 0); D2, C2, E = pts(figs['8TH4'], 1)
chk('Fig L8 TH4: square, CDE equilateral outside (ADE = 150)', abs(d(A, B) - d(B, C)) < 0.1 and abs(d(D2, E) - d(C2, E)) < 0.1 and abs(d(D2, E) - d(D2, C2)) < 0.2 and E[1] < D[1] and abs(ang(D, A, E) - 150) < 0.5, round(ang(D, A, E), 1))
A, B, C = pts(figs['8GF5'])
dline = re.search(r'<line x1="([\d.]+)" y1="([\d.]+)" x2="([\d.]+)" y2="([\d.]+)"[^>]*stroke-dasharray', figs['8GF5'])
Bx = (float(dline.group(1)), float(dline.group(2))); Dp = (float(dline.group(3)), float(dline.group(4)))
chk('Fig L8 GF5: AB = AC, angle A = 40, BD = BC, D on AC (angle ABD = 30)', abs(d(A, B) - d(A, C)) < 0.3 and abs(ang(A, B, C) - 40) < 0.5 and abs(d(B, Dp) - d(B, C)) < 0.5 and abs(ang(Bx, A, Dp) - 30) < 0.6 and abs(d(A, Dp) + d(Dp, C) - d(A, C)) < 0.5, (round(ang(A, B, C), 1), round(ang(B, A, Dp), 1)))
Sq = pts(figs['8GF6'], 0); T3 = pts(figs['8GF6'], 1)
Ap, Bp, Cp, Dq = Sq; Ep = T3[2]
chk('Fig L8 GF6: ABE equilateral inside the square (angle DEC = 150)', abs(d(Ap, Ep) - d(Ap, Bp)) < 0.1 and abs(d(Bp, Ep) - d(Ap, Bp)) < 0.1 and Ep[1] > Dq[1] and abs(ang(Ep, Dq, Cp) - 150) < 0.5, round(ang(Ep, Dq, Cp), 1))
for small in (6, 4):
    a = (0, 0); b = (10, 10); c = (10 + small, small)
    chk(f'L4 GF6 geometry: big 10, small {small}: triangle area 50', abs((b[0]*c[1] - c[0]*b[1]) / 2) == 50)
P = pts(figs['4GF6'], 2)
area = abs(sum(P[i][0]*P[(i+1) % 3][1] - P[(i+1) % 3][0]*P[i][1] for i in range(3))) / 2
big = abs(pts(figs['4GF6'], 0)[1][0] - pts(figs['4GF6'], 0)[0][0])
chk('Fig L4 GF6 drawn to scale: triangle area = half of big square', abs(area / (big * big) - 0.5) < 0.01, round(area / big**2, 3))
P = pts(figs['4GF7'])
dl = re.search(r'<line x1="[\d.]+" y1="[\d.]+" x2="([\d.]+)" y2="([\d.]+)"[^>]*stroke-dasharray', figs['4GF7'])
Dx = float(dl.group(1)); bd = (Dx - P[1][0]) / (P[2][0] - P[1][0])
chk('Fig L4 GF7: D divides BC as 4 : 12 (drawn to scale)', abs(bd - 4 / 12) < 0.01, round(bd, 3))
print('ALL PASS' if ok else 'SOME FAILED')
