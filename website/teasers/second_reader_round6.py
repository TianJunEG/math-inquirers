#!/usr/bin/env python3
"""Second reader, fix round 6 (AUDIT_ROUND6 condition G6): 17 puzzles per level (102 in all) solved from the QUESTION TEXT ONLY.

    python3 website/teasers/second_reader_round6.py

Written by someone other than the author of the generator and checker code: it imports none of kinds*.py, brute*.py, build_bank.py, verify_bank.py
or taxonomy.py.  Every solution below was worked out by reading the printed question (the numbers are copied from the text, the arithmetic is
written out in plain Python), and only afterwards compared with the answer in batches/m11 and m12 bank.json.  The first rows of each level are
the puzzles that are new or rewritten in fix round 6 (68 of them), the rest are unchanged puzzles drawn with a fixed seed (6606).
Writes batches/SECOND_READER_ROUND6.md and exits 1 on any disagreement.
"""
import json
import os
import itertools
import math
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))


def solve_all():
    S = {}
    # ------------------------------------------------------------------ LEVEL 1
    S['L1-craneboard'] = max(zip([23, 19, 28, 35], ['siti', 'raj', 'mei', 'jun']))[1]
    S['L1-noticeboard'] = (5 * 9 + 1) // 2                                  # 45 cards, the corner colour has the extra one
    S['L1-swimturn'] = 20 + 2 - 4
    S['L1-lockerdigits'] = sum(len(str(n)) for n in range(1, 30))
    S['L1-bakerywalk'] = abs(12 - 5) + 9                                    # 7 blocks east, 9 blocks north
    S['L1-stonehops'] = 34 + 12 - 7 + 20
    mei, kai = 18 - 4, 11 + 4 - 3
    S['L1-marbleswap'] = 'mei' if mei > kai else 'kai'
    S['L1-stickersheets'] = 9 * 7 - (9 // 3) * 18
    S['L1-threefifty'] = sum('3' in str(n) for n in range(1, 51))
    S['L1-bikesigns'] = (8 - 2) * 10
    S['L1-paperchain'] = 6 * 12 - 5 * 2
    sticks = {'1': 2, '2': 5, '3': 5, '4': 4, '5': 5}                       # the table printed in the question
    S['L1-matchhouse'] = sum(sticks[c] for n in range(41, 46) for c in str(n))
    bibs = sorted([12, 41, 26, 63, 38], key=lambda b: sum(int(c) for c in str(b)))
    S['L1-bibscores'] = bibs[2]
    S['L1-queuebus'] = 28 - 5 + 1
    S['L1-counterbox'] = (18 + 2) // 2
    S['L1-bigtwo'] = max(10 * a + b for a, b in itertools.permutations([6, 2, 8, 4], 2))
    # sudoku: rows and columns each hold 1, 2, 3 once; top-left 1, middle 3
    sol = None
    for g in itertools.permutations(itertools.permutations([1, 2, 3]), 3):
        if all(len({g[r][c] for r in range(3)}) == 3 for c in range(3)) and g[0][0] == 1 and g[1][1] == 3:
            sol = g
    S['L1-sudoku3'] = sol[2][0]
    # ------------------------------------------------------------------ LEVEL 2
    S['L2-blocknumber'] = [100 * a + 10 * b + c for a in range(1, 10) for b in range(10) for c in range(10)
                           if a == 2 * c and a + b + c == 12 and 3 in (a, b, c)][0]
    S['L2-ferrybenches'] = (75 - 1) // 6 + 1
    older = ['hana', 'zack', 'siti', 'dev']                                  # Hana > Zack > Siti > Dev
    S['L2-cousinages'] = older[0]
    lin = (96 - 12 + 9) // 3                                                 # Kai = lin + 12, Mei = lin - 9
    S['L2-runlaps'] = lin - 9
    S['L2-tilescore'] = [min(t) for t in itertools.combinations([14, 23, 31, 38, 45, 52], 3) if sum(t) == 135][0]
    beads = [50, 60, 30, 40, 10, 20]
    S['L2-beadsticks'] = sum(1 for i in range(6) for j in range(i + 1, 6) if beads[i] > beads[j])
    reach = {0}
    for t in range(1, 28):
        if (t - 3) in reach or (t - 5) in reach:
            reach.add(t)
    S['L2-ticketstrips'] = sum(1 for t in range(1, 28) if t in reach)
    words = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
             14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty'}
    az = sorted(range(1, 15), key=lambda n: words[n])
    S['L2-numbershelf'] = az[8]
    S['L2-schoolwalks'] = 'park' if 7 + 8 < 4 + 5 + 7 else 'shop'
    S['L2-hosepieces'] = [n for n in range(1, 30) if n * 30 - (n - 1) * 4 == 238][0]
    scores = {'hana': 64, 'kai': 58, 'lin': 71, 'dev': 67}
    S['L2-quizscores'] = sorted(scores, key=lambda k: -scores[k])[1]
    S['L2-windowsolids'] = (4 + 3) * 8
    S['L2-walletmoney'] = 3 * 100 + 6 * 10 + 8
    costs = {'shop a': 12 * 4, 'shop b': (12 // 3) * 10, 'shop c': (12 // 6) * 19}
    S['L2-markershops'] = min(costs, key=costs.get)
    S['L2-hairclips'] = min(16 * 3, (16 // 4) * 10)
    kai2, lin2 = 35 - 5, 28 + 5 + 4
    S['L2-cardgame'] = 'kai' if kai2 > lin2 else 'lin'
    S['L2-duedate'] = 25 + 17 - 31                                           # October has 31 days
    # ------------------------------------------------------------------ LEVEL 3
    S['L3-missednumber'] = sum(range(1, 17)) - 124
    S['L3-petvotes'] = max([19, 8, 26, 13, 22]) - min([19, 8, 26, 13, 22])
    S['L3-pairproduct'] = [x for x in range(1, 27) if x * (53 - x) == 282][0]
    S['L3-raffledigits'] = sum(1 for n in range(100, 200) if sum(int(c) for c in str(n)) == 7)
    S['L3-posterribbon'] = 2 * (38 + 27)
    S['L3-kitegusts'] = 20 + 6 - 10 + 9 - 3
    S['L3-ropepieces'] = sum(1 for a in range(4, 34) if 33 - a >= a)
    S['L3-stallminutes'] = (13 * 60 + 45) - (7 * 60 + 15)
    S['L3-barpieces'] = 2 * 15 // 3
    S['L3-harbourcruise'] = (16 * 60 + 25 + 2 * 60 + 50) // 60 * 100 + (16 * 60 + 25 + 2 * 60 + 50) % 60
    roads = {('home', 'library'): 8, ('home', 'park'): 12, ('library', 'park'): 3, ('library', 'pool'): 13, ('park', 'pool'): 9, ('park', 'school'): 17, ('pool', 'school'): 7}
    S['L3-mapshort'] = shortest(roads, 'home', 'school')
    S['L3-kopitiam'] = (450 + 86) // 2
    S['L3-cryptsum'] = [a for a in range(1, 10) for b in range(10) for c in range(10)
                        if len({a, b, c}) == 3 and a > 0 and c > 0 and (10 * a + b) + (10 * c + b) == 100 * b + 10 * b + c][0]
    S['L3-eights'] = sum(1 for n in range(50, 201) if n % 8 == 0)
    S['L3-mealset'] = 2 * 5 * 4
    S['L3-cuboidclue'] = 'cuboid'                                            # 6 faces, 8 corners, rectangles that are not squares
    S['L3-solidedges'] = 12 + 8                                              # cube 12, square pyramid 4 + 4
    # ------------------------------------------------------------------ LEVEL 4
    ravi, sue = 85 - 20 - 12, 62 + 20 - 35
    S['L4-moneypurse'] = 'ravi' if ravi > sue else 'sue'
    S['L4-bluelockers'] = [x for x in [45, 63, 81, 99, 112] if any(all(y % d == 0 for y in [45, 63, 81, 99, 112] if y != x) for d in range(2, 10))][0]
    S['L4-stageline'] = 7 * 6 * 5
    parks = {('house', 'bridge'): 150, ('house', 'pool'): 90, ('pool', 'temple'): 140, ('bridge', 'temple'): 60, ('bridge', 'market'): 240, ('temple', 'market'): 110}
    S['L4-parkpaths'] = first_stop(parks, 'house', 'market')
    S['L4-airportshuttle'] = (22 * 60 + 20) - (6 * 60 + 40) - 75
    floor = 26
    lowest = floor
    for d in (-6, 9, -15, 5):
        floor += d
        lowest = min(lowest, floor)
    S['L4-liftfloors'] = lowest
    S['L4-ferrypier'] = 2 * 2840 - 1250
    S['L4-gluesticks'] = min((18 // 6) * 21, 18 * 4)
    az20 = sorted(range(1, 21), key=lambda n: words[n])
    S['L4-spellingbee'] = az20[15]
    can = {0}
    for t in range(1, 51):
        if (t - 5) in can or (t - 9) in can:
            can.add(t)
    S['L4-pencilpacks'] = sum(1 for t in range(1, 51) if t in can)
    ann = (540 - 70 - 110) // 3
    S['L4-grandchildren'] = ann + 110
    S['L4-cupcaketray'] = 12 * 17 // 2
    S['L4-reachtotal'] = 59 % 7                                              # leave a multiple of 7 (1 + 6) for the other player
    S['L4-symmetry'] = 4 + 2 + 3 + 1
    S['L4-fivechildren'] = ['priya', 'ben', 'mei ling', 'ravi', 'sam'][2]
    names = ['kumar', 'priya', 'wei jie', 'siti']
    ate = []
    for who in names:
        claims = [who != 'kumar', who == 'siti', who == 'siti', who == 'wei jie']
        if claims.count(False) == 1:
            ate.append(who)
    S['L4-fourclaims'] = ate[0]
    h = [4, 7, 15, 18, 30]
    S['L4-sunflower'] = max(b - a for a, b in zip(h, h[1:]))
    # ------------------------------------------------------------------ LEVEL 5
    S['L5-nametagpacks'] = min((60 // 12) * 34, (60 // 15) * 41, (60 // 20) * 55)
    S['L5-shapelines'] = 4 + 2 + 2 + 0                                       # square, rectangle, rhombus, parallelogram
    S['L5-codelock'] = sum(1 for a in range(1, 23) if 1 <= 30 - a <= 22)
    S['L5-postalscale'] = sum(1 for m in range(4000, 4700) if (m + 5) // 10 * 10 == 4350)
    x = 25 - 7
    y = 22 + 9 - 11
    S['L5-dronepaths'] = abs(x) + abs(y)
    rates = {'pip': F(96, 12), 'gus': F(135, 15), 'rex': F(210, 25)}
    S['L5-snailrace'] = max(rates, key=rates.get)
    bars = {'0': 6, '1': 2, '2': 5, '3': 5, '4': 4, '5': 5, '6': 6, '7': 3, '8': 7, '9': 6}
    S['L5-scoreboard'] = sum(bars[c] for n in range(98, 106) for c in str(n))
    S['L5-bakeryprices'] = 34 - 23
    S['L5-shoptakings'] = 5070 - 2960
    S['L5-sailheight'] = F(9 * 12, 15)
    S['L5-rhombuscut'] = (180 - 52) // 2
    v = [95, 88, 76, 70, 49, 46]
    S['L5-pondlevel'] = max(a - b for a, b in zip(v, v[1:]))
    S['L5-ladybirdgrid'] = grid_paths(5, 4, {(1, 1)})
    S['L5-sportsbibs'] = sum(len(str(n)) for n in range(85, 125))
    num = 13 * 27 + 9
    S['L5-divquotient'] = (num + 50) // 13
    S['L5-sixpages'] = (255 - 15) // 6
    S['L5-town'] = round(3486215 / 100000) * 100000
    # ------------------------------------------------------------------ LEVEL 6
    S['L6-helmetsale'] = F(63 * 100, 70)
    S['L6-fishtank'] = 75 * 40 * 60 // 1000
    belt = [35, 12, 48, 41, 20, 9, 27]
    S['L6-parcelbelt'] = sum(1 for i in range(7) for j in range(i + 1, 7) if belt[i] > belt[j])
    S['L6-parkvisitors'] = round(1386725 / 1000) * 1000
    c = [412, 380, 395, 331, 348, 366]
    S['L6-coffeecups'] = max(a - b for a, b in zip(c, c[1:]))
    S['L6-lettercodes'] = 8 * 7 * 6 * 5
    harbour = {('pier', 'cove'): 14, ('pier', 'reef'): 10, ('cove', 'dock'): 8, ('reef', 'dock'): 18, ('reef', 'bay'): 12, ('dock', 'town'): 16, ('bay', 'town'): 14}
    S['L6-islandroutes'] = last_stop(harbour, 'pier', 'town')
    isp = lambda n: n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))
    S['L6-goldbach'] = sum(1 for p in range(2, 68) if isp(p) and isp(134 - p))
    S['L6-leftright'] = (31 + 17) // 6 * 9
    S['L6-bin45'] = int('101101', 2)
    S['L6-jarcoins'] = 5 * 2 ** 8                                            # day 1 has $5, day 9 is eight doublings later
    S['L6-sweettin'] = F(6 + 9 + 5 + 4 - 6, 24)
    S['L6-pearltray'] = 3 ** 6
    S['L6-walkers'] = 2400 // (70 + 90)
    S['L6-balance'] = (62 + 10) // (6 - 2)
    S['L6-testmean'] = F(72 + 85 + 64 + 91 + 88, 5)
    S['L6-gamepay'] = sum(range(4, 121, 4))
    return S


def adj(roads):
    g = {}
    for (a, b), w in roads.items():
        g.setdefault(a, []).append((b, w))
        g.setdefault(b, []).append((a, w))
    return g


def all_routes(roads, start, end):
    g = adj(roads)
    out = []

    def walk(at, seen, total, path):
        if at == end:
            out.append((total, path))
            return
        for nxt, w in g[at]:
            if nxt not in seen:
                walk(nxt, seen | {nxt}, total + w, path + [nxt])
    walk(start, {start}, 0, [start])
    return sorted(out)


def shortest(roads, start, end):
    r = all_routes(roads, start, end)
    assert r[0][0] < r[1][0]
    return r[0][0]


def first_stop(roads, start, end):
    r = all_routes(roads, start, end)
    assert r[0][0] < r[1][0]
    return r[0][1][1]


def last_stop(roads, start, end):
    r = all_routes(roads, start, end)
    assert r[0][0] < r[1][0]
    return r[0][1][-2]


def grid_paths(w, h, blocked):
    ways = {(0, 0): 1}
    for i in range(w + 1):
        for j in range(h + 1):
            if (i, j) == (0, 0):
                continue
            ways[(i, j)] = 0 if (i, j) in blocked else ways.get((i - 1, j), 0) + ways.get((i, j - 1), 0)
    return ways[(w, h)]


def canon(v):
    if isinstance(v, str):
        return v.lower()
    v = F(v)
    return str(v.numerator) if v.denominator == 1 else ('%s' % float(v) if (v.denominator in (2, 4, 5, 8, 10, 20, 25, 50)) and False else '%d/%d' % (v.numerator, v.denominator))


def bank_value(e):
    if e['type'] == 's':
        return e['ans'].lower()
    a = F(e['ans'])
    return str(a.numerator) if a.denominator == 1 else '%d/%d' % (a.numerator, a.denominator)


def main():
    bank = {}
    for mm in ('11', '12'):
        for lv, items in json.load(open(os.path.join(HERE, 'batches', 'm%s' % mm, 'bank.json'), encoding='utf-8'))['levels'].items():
            for e in items:
                bank[e['id']] = e
    mine = solve_all()
    rows, bad = [], 0
    per = {}
    for pid, val in mine.items():
        e = bank[pid]
        mv = canon(val) if isinstance(val, str) else canon(F(val))
        bv = bank_value(e)
        ok = mv == bv
        bad += not ok
        per.setdefault(e['level'], []).append((pid, mv, bv, ok))
    lines = ['# Second reader, fix round 6 (condition G6)', '',
             'Script: `second_reader_round6.py` (imports none of the generator, checker, builder or verifier code). Every puzzle was solved from its printed question; the bank answer was opened afterwards.', '',
             '| Level | Puzzles | Agree | New or rewritten in round 6 among them |', '|---|---|---|---|']
    new_ids = set(json.load(open(os.path.join(HERE, 'batches', 'ROUND6_CHANGED.json'))) ) if os.path.exists(os.path.join(HERE, 'batches', 'ROUND6_CHANGED.json')) else set()
    for lv in sorted(per):
        rs = per[lv]
        lines.append('| %d | %d | %d | %d |' % (lv, len(rs), sum(r[3] for r in rs), sum(1 for r in rs if r[0] in new_ids)))
    lines += ['', '| Puzzle | Second reader | Bank | |', '|---|---|---|---|']
    for lv in sorted(per):
        for pid, mv, bv, ok in per[lv]:
            lines.append('| %s | %s | %s | %s |' % (pid, mv, bv, 'agree' if ok else '**DIFFERENT**'))
    open(os.path.join(HERE, 'batches', 'SECOND_READER_ROUND6.md'), 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
    for lv in sorted(per):
        print('Level %d: %d puzzles, %d agree' % (lv, len(per[lv]), sum(r[3] for r in per[lv])))
        for pid, mv, bv, ok in per[lv]:
            if not ok:
                print('   DIFFERENT', pid, 'second reader', mv, 'bank', bv)
    print('total %d puzzles, %d disagreements' % (sum(len(v) for v in per.values()), bad))
    return 1 if bad else 0


if __name__ == '__main__':
    raise SystemExit(main())
