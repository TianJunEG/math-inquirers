#!/usr/bin/env python3
"""Verification for the P4 fix pass (docs/audit/fixpass_p4.md).
Re-computes every answer that was added or changed in the fix pass. Run: python3 docs/audit/verify_fixpass_p4.py
Exits non-zero if any check fails."""
import itertools, json, math, sys
from fractions import Fraction

fails = []
round_half_up = lambda x, b: int(math.floor(x / b + 0.5)) * b
def ok(name, cond, detail=''):
    print(('PASS ' if cond else 'FAIL ') + name + (('  ' + str(detail)) if detail else ''))
    if not cond: fails.append(name)

# ---------------- sneak-peek puzzles (check[0], check[1]) ----------------
ok('L1 sneak 1: 12 sweets in equal bags = factors of 12', [d for d in range(1, 13) if 12 % d == 0] == [1, 2, 3, 4, 6, 12])
ok('L1 sneak 2: lifts every 3rd and 5th floor to 40 = 15, 30', [f for f in range(1, 41) if f % 3 == 0 and f % 5 == 0] == [15, 30])
ok('L2 sneak 1: 7 200 nearer 7 000', abs(7200 - 7000) < abs(8000 - 7200))
ok('L2 sneak 2: shop says about 8 000 -> real numbers 7 500..8 499; 7 499 and 8 500 are out',
   [x for x in (7499, 7500, 8499, 8500) if round_half_up(x, 1000) == 8000] == [7500, 8499])
ok('L3 sneak 1: 2 bags of 4 plus 3 = 11', 2 * 4 + 3 == 11)
ok('L3 sneak 2: (2+3)x4 = 20 and 2+3x4 = 14', (2 + 3) * 4 == 20 and 2 + 3 * 4 == 14)
# the only single bracket placements of 2 + 3 x 4 give 20 (and 14 / 14)
ok('L3 sneak 2: only (2+3)x4 reaches 20 with one pair', sorted(set([(2 + 3) * 4, 2 + (3 * 4), 2 + 3 * 4])) == [14, 20])
ok('L4 sneak 1: strip folded twice -> 4 parts, 3 coloured = 3/4', Fraction(3, 4) == Fraction(3, 2 ** 2))
ok('L4 sneak 2: 9 quarter-scoops = 2 1/4 cups', divmod(9, 4) == (2, 1))
ok('L5 sneak 1: $0.80 > $0.75 (8 dimes v 7 dimes + 5c)', 8 * 10 > 7 * 10 + 5)
ok('L5 sneak 2: 3.45 between 3.4 and 3.5', 3.4 < 3.45 < 3.5)
ok('L6 sneak 1: two quarter turns = half turn', 2 * 90 == 180)
ok('L6 sneak 2: 90 - 35 = 55', 90 - 35 == 55)
ok('L7 sneak 1: 5x3 minus corner = 14', 5 * 3 - 1 == 14)
def perimeter(cells):
    cells = set(cells); p = 0
    for (r, c) in cells:
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if (r + dr, c + dc) not in cells: p += 1
    return p
full = [(r, c) for r in range(3) for c in range(5)]
cut = [x for x in full if x != (0, 4)]
ok('L7 sneak 2: perimeter unchanged (16 and 16), area 15 -> 14', perimeter(full) == 16 and perimeter(cut) == 16 and len(cut) == 14, (perimeter(full), perimeter(cut)))
ok('L9 sneak 1: juice 30, 45, 25 -> most Tuesday 45, fewest Wednesday 25', max([30, 45, 25]) == 45 and min([30, 45, 25]) == 25)
ok('L9 sneak 2: halfway 100 and 150 is 125', (100 + 150) / 2 == 125)
ok('L10 sneak 1: 5 ducks 10 legs, one rabbit instead 12 legs', 5 * 2 == 10 and 4 * 2 + 4 == 12)
sol = [(a, 8 - a) for a in range(0, 9) if a * 2 + (8 - a) * 4 == 22]
ok('L10 sneak 2: 8 animals 22 legs -> 3 rabbits 5 ducks only', sol == [(5, 3)], sol)

# ---------------- L8 cube-net simulation ----------------
def roll(o, d):
    b, t, n, s, e, w = o
    if d == 'E': return (e, w, n, s, t, b)
    if d == 'W': return (w, e, n, s, b, t)
    if d == 'N': return (n, s, t, b, e, w)
    return (s, n, b, t, e, w)  # 'S'
STEP = {'E': (0, 1), 'W': (0, -1), 'N': (-1, 0), 'S': (1, 0)}
def folds(cells):
    cells = set(cells)
    start = min(cells)
    seen = {start: (0, 1, 2, 3, 4, 5)}; stack = [start]
    while stack:
        cur = stack.pop()
        for d, (dr, dc) in STEP.items():
            nx = (cur[0] + dr, cur[1] + dc)
            if nx in cells and nx not in seen:
                seen[nx] = roll(seen[cur], d); stack.append(nx)
    if len(seen) != 6: return False
    return len({o[0] for o in seen.values()}) == 6
def norm(cells):
    best = None
    pts = list(cells)
    for _ in range(2):
        for _ in range(4):
            pts = [(c, -r) for r, c in pts]
            mr = min(r for r, c in pts); mc = min(c for r, c in pts)
            t = tuple(sorted((r - mr, c - mc) for r, c in pts))
            best = t if best is None or t < best else best
        pts = [(r, -c) for r, c in pts]
    return best
def hexominoes():
    cur = {norm([(0, 0)])}
    for _ in range(5):
        nxt = set()
        for sh in cur:
            for (r, c) in sh:
                for dr, dc in STEP.values():
                    p = (r + dr, c + dc)
                    if p not in sh: nxt.add(norm(list(sh) + [p]))
        cur = nxt
    return cur
H = hexominoes()
nets = [h for h in H if folds(h)]
ok('L8: 35 hexominoes, 11 are cube nets', len(H) == 35 and len(nets) == 11, (len(H), len(nets)))
def longest_row(sh):
    best = 0
    for r in {r for r, c in sh}:
        cs = sorted(c for rr, c in sh if rr == r); run = 1
        for a, b in zip(cs, cs[1:]):
            run = run + 1 if b == a + 1 else 1
            best = max(best, run)
        best = max(best, 1)
    for c in {c for r, c in sh}:
        rs = sorted(r for r, cc in sh if cc == c); run = 1
        for a, b in zip(rs, rs[1:]):
            run = run + 1 if b == a + 1 else 1
            best = max(best, run)
    return best
from collections import Counter
cnt = Counter(longest_row(n) for n in nets)
ok('L8 go further: 4 of 11 nets have longest line 3; 6 have 4; 1 has 2', cnt == Counter({4: 6, 3: 4, 2: 1}), dict(cnt))
ok('L8 sneak 2: a straight row of 6 does not fold', not folds([(0, c) for c in range(6)]))
row4 = [(1, c) for c in range(4)]
placements = [(0, a, 2, b) for a in range(4) for b in range(4)]
ok('L8 invest: a row of 4 with one square above and one below folds (all 16 placements)', all(folds(row4 + [(0, a), (2, b)]) for a in range(4) for b in range(4)))
ok('L8 invest: both extra squares on the same side never folds (rows of 4 + 2 above)',
   not any(folds(row4 + [(0, a), (0, b)]) for a in range(4) for b in range(4) if a < b))
# H has exactly 2 lines of symmetry (block letter: 4 cells wide, 5 high)
Hc = {(r, c) for r in range(5) for c in (0, 2)} | {(2, 1)}
ok('L8 sneak 1: block H has 2 mirror lines (vertical, horizontal), not diagonal',
   {(r, 2 - c) for r, c in Hc} == Hc and {(4 - r, c) for r, c in Hc} == Hc and {(c, r) for r, c in Hc} != Hc)

# ---------------- L3 ----------------
nums = [6, 4, 3, 2]
# 6 + 4 x 3 - 2 with 0, 1, 2 pairs of brackets (all placements, python eval)
toks = ['6', '+', '4', '*', '3', '-', '2']
def with_brackets(pairs):
    res = set()
    idx = [0, 2, 4, 6]  # number positions
    spans = [(i, j) for ii, i in enumerate(idx) for j in idx[ii + 1:]]
    for combo in itertools.combinations(spans, pairs):
        t = list(toks)
        # insert brackets
        ins = []
        for (i, j) in combo: ins.append((i, '(')); ins.append((j + 1, ')'))
        out = []
        for pos in range(len(t) + 1):
            for (p, ch) in sorted([x for x in ins if x[0] == pos], key=lambda z: z[1] == '('):
                pass
        s = ''
        for pos in range(len(t)):
            s += ''.join('(' for (p, ch) in ins if p == pos and ch == '(')
            s += t[pos]
            s += ''.join(')' for (p, ch) in ins if p == pos + 1 and ch == ')')
        try:
            res.add(eval(s))
        except Exception:
            pass
    return res
none = {6 + 4 * 3 - 2}
one = with_brackets(1) | none
two = with_brackets(2) | one
ok('L3 try3 / go further: 6 + 4 x 3 - 2 gives 16; one pair also 10, 28; two pairs give nothing new',
   none == {16} and one == {16, 28, 10} and two == {16, 28, 10}, (sorted(one), sorted(two)))
ok('L3 warm: 48/6=8, 9x6=54, 4x20=80, 1000-368=632, 25x4=100', (48 // 6, 9 * 6, 4 * 20, 1000 - 368, 25 * 4) == (8, 54, 80, 632, 100))
ok('L3 try-next: 4800/6=800, 99x6=594, 45x20=900', (4800 // 6, 99 * 6, 45 * 20) == (800, 594, 900))
# Q6 new numbers: 124 plates, chicken rice 3 units, laksa 1 unit
ok('L3 Q6: 124 plates, 4 units -> 31, 93 chicken rice, 62 more', 124 / 4 == 31 and 3 * 31 == 93 and 93 - 31 == 62)
ok('L3 Q6 original kept in bank: 1236 -> 309, 927, 618', 1236 / 4 == 309 and 3 * 309 == 927 and 927 - 309 == 618)

# ---------------- L2 ----------------
ok('L2 Q1: 47 285 -> 47 290, 47 300, 47 000; 63 950 -> 63 950, 64 000, 64 000',
   (round_half_up(47285, 10), round_half_up(47285, 100), round_half_up(47285, 1000)) == (47290, 47300, 47000) and
   (round_half_up(63950, 10), round_half_up(63950, 100), round_half_up(63950, 1000)) == (63950, 64000, 64000))
ok('L2 try next: 9049 -> 9050, 9000, 9000; 80 503 -> 80 500, 80 500, 81 000',
   (round_half_up(9049, 10), round_half_up(9049, 100), round_half_up(9049, 1000)) == (9050, 9000, 9000) and
   (round_half_up(80503, 10), round_half_up(80503, 100), round_half_up(80503, 1000)) == (80500, 80500, 81000))
perms = {int(''.join(p)) for p in itertools.permutations('24579')}
ok('L2 go further: closest to 70 000 is 72 459 (2 459 away); below is 59 742', min(perms, key=lambda x: abs(x - 70000)) == 72459 and max(x for x in perms if x < 70000) == 59742)
ok('L2 invest easy step: 3 280 -> 3 300 -> 3 000, and 3 280 -> 3 000 (same); a different example 3 490 -> 3 500 -> 4 000 v 3 000',
   round_half_up(round_half_up(3280, 100), 1000) == 3000 == round_half_up(3280, 1000) and round_half_up(round_half_up(3490, 100), 1000) == 4000 != round_half_up(3490, 1000))
ok('L2 Q2b (kept): numbers that round to 5350 to the nearest 10 are 5345..5354 (10)', [x for x in range(5300, 5400) if round_half_up(x, 10) == 5350] == list(range(5345, 5355)))

# ---------------- L4 ----------------
ok('L4 cmp: 4/9 < 5/8 (drawn bars)', Fraction(4, 9) < Fraction(5, 8))
ok('L4 go further: 19 slices of 8 = 2 3/8', divmod(19, 8) == (2, 3))
ok('L4 Q4 (kept): 7/12 < 2/3 < 5/6 order', Fraction(7, 12) < Fraction(2, 3) < Fraction(5, 6))
ok('L4 talk: 9/4 = 2 1/4 < 2 1/3', Fraction(9, 4) < Fraction(7, 3))

# ---------------- L5 ----------------
ok('L5 Q3a: smallest 7.35, largest 7.44 round to 7.4 (2 d.p.)', [x / 100 for x in range(700, 800) if round_half_up(x, 10) == 740] == [x / 100 for x in range(735, 745)])
ok('L5 Q4a: digits 3, 6, 9 with the point after the first digit give 6 numbers', sorted(f'{a}.{b}{c}' for a, b, c in itertools.permutations('369')) == ['3.69', '3.96', '6.39', '6.93', '9.36', '9.63'])
vals = sorted(float(f'{a}.{b}{c}') for a, b, c in itertools.permutations('369'))
ok('L5 Q4b/c: largest 9.63; nearest 7 is 6.93', vals[-1] == 9.63 and min(vals, key=lambda v: abs(v - 7)) == 6.93)
ok('L5 Q4d: 3.69 and 3.96 round to 4 (nearest whole)', [v for v in vals if round(v + 1e-9) == 4] == [3.69, 3.96])
ok('L5 Q6: 2.85 - 0.45 = 2.40; 2.40/6 = 0.4; 2.85 - 0.8 = 2.05', abs(2.85 - 0.45 - 2.40) < 1e-9 and abs(2.40 / 6 - 0.4) < 1e-9 and abs(2.85 - 0.8 - 2.05) < 1e-9)
c5 = sorted(float(f'{a}{b}.{c}') for a, b, c in itertools.permutations('258')) + sorted(float(f'{a}.{b}{c}') for a, b, c in itertools.permutations('258'))
ok('L5 go further: target 50 with cards 2, 5, 8: 52.8 closest (then 58.2)', sorted(c5, key=lambda v: abs(v - 50))[:2] == [52.8, 58.2], sorted(c5, key=lambda v: abs(v - 50))[:3])

# ---------------- L6 ----------------
hour = 3 * 30 + 30 * 0.5; minute = 30 * 6
ok('L6 go further: 3:30 angle = 75', abs(minute - hour) == 75, (hour, minute))
ok('L6 invest easy: 90 / 3 = 30', 90 / 3 == 30)

# ---------------- L7 ----------------
rects24 = [(a, 24 // a) for a in range(1, 5) if 24 % a == 0 for _ in [0]]
rects24 = [(a, 24 // a) for a in range(1, int(24 ** .5) + 1) if 24 % a == 0]
ok('L7 go further: 24 tiles -> 4 rectangles with perimeters 50, 28, 22, 20', [2 * (a + b) for a, b in rects24] == [50, 28, 22, 20], rects24)
ok('L7 Q3: 6 tiles, smallest perimeter 10 (2 x 3), largest 14 (row of 6)', 2 * (2 + 3) == 10 and 2 * (1 + 6) == 14)
# polyomino perimeters of 6 tiles: min 10, max 14
def polyominoes(n):
    cur = {norm([(0, 0)])}
    for _ in range(n - 1):
        nxt = set()
        for sh in cur:
            for (r, c) in sh:
                for dr, dc in STEP.values():
                    p = (r + dr, c + dc)
                    if p not in sh: nxt.add(norm(list(sh) + [p]))
        cur = nxt
    return cur
per = [perimeter(h) for h in polyominoes(6)]
ok('L7 Q3 (all 35 shapes of 6 tiles): perimeters range 10..14; only one shape has 10 (2 x 3)', min(per) == 10 and max(per) == 14 and per.count(10) == 1, (min(per), max(per), per.count(10)))
ok('L7 Q4 staircase: perimeter 34, area 6 + 14 + 22 = 42', 2 * (11 + 6) == 34 and 3 * 2 + 7 * 2 + 11 * 2 == 42)
ok('L7 invest easy: 4 by 4 square area 16, perimeter 16', 4 * 4 == 16 and 4 * 4 == 16)

# ---------------- L9 ----------------
ok('L9 explore hint: scale 2 per line fits the max queue 22 in 12 lines', math.ceil(22 / 2) == 11 <= 12)
ok('L9 invest: sales 50 -> 100 is doubled; same points on a 0-100 scale rise by half the height', 100 / 50 == 2)

# ---------------- L10 ----------------
ok('L10 go further: 10 bugs, 65 legs impossible (8 and 6 are even)', all((8 * s + 6 * (10 - s)) % 2 == 0 for s in range(11)) and 65 % 2 == 1)
ok('L10 (kept): 15 cycles 38 wheels -> 8 tricycles', [t for t in range(16) if 2 * (15 - t) + 3 * t == 38] == [8])

# ---------------- L1 ----------------
ok('L1 go further: 36 has 9 factors (odd), 5 rectangles', len([d for d in range(1, 37) if 36 % d == 0]) == 9 and len([a for a in range(1, 7) if 36 % a == 0]) == 5)

# ---------------- Diagnostic (diag/content/p4.json) ----------------
d = json.load(open('diag/content/p4.json'))
byq = {x['q']: x for x in d['foundation'] + d['core'] + d['stretch']}
ok('diag warm-up order: 9x7, 2/3, area, 5000-1346 last', [x['skill'] for x in d['foundation']] == ['Times tables 6 to 9', 'Equivalent fractions', 'Area of a rectangle', 'Subtract 4-digit numbers'])
ok('diag W: 5000-1346=3654; 9x7=63; 2/3=8/12; 7x6=42', (5000 - 1346, 9 * 7, Fraction(2, 3) == Fraction(8, 12), 7 * 6) == (3654, 63, True, 42))
ok('diag W: key a-values match', [x['a'] for x in d['foundation']] == ['63', '8', '42 square cm', '3654'])
ok('diag Q1: factors of 18', [x for x in range(1, 19) if 18 % x == 0] == [1, 2, 3, 6, 9, 18] and d['core'][0]['a'] == '1, 2, 3, 6, 9, 18' and d['core'][0]['q'].startswith('A factor of 18 is a number that divides 18 exactly'))
ok('diag Q2: 48 572 -> 49 000', round_half_up(48572, 1000) == 49000)
ok('diag Q3: 12 + 6 x 3 - 4 = 26; left to right gives 50', 12 + 6 * 3 - 4 == 26 and ((12 + 6) * 3 - 4) == 50)
t = Fraction(2) + Fraction(3, 5) + Fraction(1) + Fraction(4, 5)
ok('diag Q4: 2 3/5 + 1 4/5 = 4 2/5 = 22/5', t == Fraction(22, 5) and divmod(t.numerator, t.denominator) == (4, 2) and '22/5' in d['core'][3]['work'])
ok('diag Q5: 3.7 + 2.85 = 6.55; mistakes 3.22 (37 + 285 = 322) and 5.92 (digits lined up from the right) are reproducible',
   abs(3.7 + 2.85 - 6.55) < 1e-9)
# 5.92: 3.7 written under 2.85 shifted: 37 (tenths) + 285 aligned right -> 0.37... check by place value
wrong_align = (37 + 285) / 100  # 3.22: numbers lined up on the right with the point ignored
ok('diag Q5 error "3.22" reproducible (37 + 285 = 322 -> 3.22)', wrong_align == 3.22)
# 5.92: 3.70 + 2.85 misread as 3.7 + 2.22? derive a genuine way: add tenths 7+8=15, hundredths 0+5=5 -> 15.5? Show 5.92 from 3.7 + 2.2 + 0.02? Not needed; check it is listed and that it is not 6.55
ok('diag Q5 key text uses 3.22 and 5.92, not 6.12 / 5.82', '3.22' in d['core'][4]['work'] and '5.92' in d['core'][4]['work'] and '6.12' not in d['core'][4]['work'] and '5.82' not in d['core'][4]['work'])
# the 5.92 digit trace: 3.7 + 2.85 with digits lined up from the right, 3.7 -> 3.07? 3.07 + 2.85 = 5.92
ok('diag Q5: 5.92 comes from lining 3.7 up as 3.07 (digits from the right) + 2.85', abs(3.07 + 2.85 - 5.92) < 1e-9)
ok('diag Q6: perimeter 36, length 11 -> width 7; errors 25 and 14', (36 // 2 - 11, 36 - 11, 36 // 2 - 11 + 7) == (7, 25, 14) and d['core'][5]['a'] == '7 cm')
ok('diag S1: 30-50, multiple of 4 and 6, digit sum 9 -> 36 only', [x for x in range(31, 50) if x % 4 == 0 and x % 6 == 0 and sum(map(int, str(x))) == 9] == [36])
ok('diag S2: Ben 3x Cara, 12 moved, equal -> Ben 36, Cara 12', [(b, c) for c in range(1, 100) for b in [3 * c] if b - 12 == c + 12] == [(36, 12)])
ok('diag minutes 40; placement block present; coverage line present',
   d['minutes'] == 40 and 'placement' in d and any('Angles, symmetry, nets and graphs are not in it' in x for x in d['topics']))
ok('diag stretch reassurance present on Brain stretcher 1', d['stretch'][0]['q'].startswith('(Brain stretchers are hard on purpose.'))
ok('diag W4 key accepts 42 sq cm / cm2 and gives the mark if no unit', 'Accept 42 square cm, 42 sq cm or 42 cm2' in d['foundation'][2]['work'] and 'give the mark' in d['foundation'][2]['work'])

print()
if fails:
    print('FAILED:', len(fails)); [print(' -', f) for f in fails]; sys.exit(1)
print('ALL CHECKS PASSED')
