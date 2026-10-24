#!/usr/bin/env python3
"""Second reader, January 2027 batch, Levels 1 and 2: all 31 puzzles of each level (62 in all) solved from the QUESTION TEXT ONLY.

    python3 website/teasers/second_reader_jan_l1l2.py

Written from the printed questions of batches/m01/bank.json (field "q", and "code" for the one table) with the answers, the parameters and the generator
files closed: it imports none of kinds*.py, brute*.py, build_bank.py, verify_bank.py, taxonomy.py or defs/.  The numbers below are copied from the printed
wording (so a mismatch between a question and the data behind it shows up as a disagreement), and the arithmetic is written out in plain Python, mostly by
simulating or enumerating what the question says.  Only after all 62 solutions were fixed were they compared with the bank.
Writes batches/m01/SECOND_READER_JAN_L1L2.md and exits 1 on any disagreement.
"""
import itertools
import json
import os
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
WORDS = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
         13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty'}


def reachable(coins, top):
    """Which totals 0..top can be paid exactly with unlimited coins of these sizes."""
    ok = [True] + [False] * top
    for t in range(1, top + 1):
        ok[t] = any(t >= c and ok[t - c] for c in coins)
    return ok


def solve_all():
    S = {}
    # ------------------------------------------------------------------ LEVEL 1
    S['L1-tagtiles'] = min(10 * a + b for a, b in itertools.permutations([8, 6, 9, 7], 2))
    S['L1-partyclinks'] = sum(1 for a in range(7) for b in range(a + 1, 7))
    mins = (5 + 35) % 60                                                   # 5 past 6 and 35 minutes: 40 past
    S['L1-noodlepot'] = mins // 5
    ok = reachable([2, 5], 40)
    S['L1-prizecorner'] = sum(ok[1:])
    S['L1-puffsleft'] = 85 - 23 - 19
    fri = {'farid': 41, 'lena': 36, 'hakim': 29, 'aminah': 44}
    S['L1-skipropes'] = min(fri, key=fri.get)
    S['L1-grapeplates'] = len({tuple(sorted((a, 26 - a))) for a in range(1, 26)})
    S['L1-tartrows'] = sum(1 for r in range(3) for c in range(5) if r in (0, 2) or c in (0, 4))
    S['L1-dumplingboxes'] = 88 // 2
    S['L1-bikelock'] = [10 * t + o for t in range(1, 10) for o in range(10) if t + o == 11 and t == o + 5][0]
    S['L1-pegline'] = 25 + (3 - 1) * (85 - 25) // (4 - 1)
    times = {'9 pm': 21, '3 pm': 15, '8 am': 8, '11 am': 11}
    S['L1-busdepart'] = min(times, key=times.get)
    S['L1-applegraph'] = (9 - 2) * 10
    S['L1-pagefives'] = sum('5' in str(n) for n in range(1, 60))
    sticks = {'1': 2, '2': 5, '3': 5, '4': 4, '5': 5, '6': 6}               # the table printed with the question
    S['L1-busplates'] = sum(sticks[c] for n in range(61, 66) for c in str(n))
    n = 4
    for _ in range(4):                                                       # Monday 4, then Tue, Wed, Thu, Fri
        n *= 2
    S['L1-fireflies'] = n
    az = sorted(range(1, 21), key=lambda k: WORDS[k])
    S['L1-flagcards'] = az[2]
    gaps = 3 - 1
    S['L1-lighthouse'] = 12 // gaps * (8 - 1)
    grid = [['g' if (r + c) % 2 == 0 else 'y' for c in range(9)] for r in range(7)]
    S['L1-floormat'] = sum(row.count('y') for row in grid)
    place = 33 + 6 - 2
    S['L1-sackrace'] = place
    rank = ['yusof', 'xavier', 'rina']                                     # heavier to lighter
    S['L1-lightestbag'] = rank[-1]
    S['L1-busseats'] = (9 - 1) * 4 + 2
    S['L1-cousinstay'] = len(set(range(2, 28)) & set(range(5, 31)))
    S['L1-photoline'] = 90 - 14 + 1
    S['L1-beanbags'] = [min(t) for t in itertools.combinations([6, 16, 17, 24, 32, 44], 3) if sum(t) == 73][0]
    tickets = sorted([63, 42, 82, 68, 29], key=lambda t: sum(int(c) for c in str(t)))
    S['L1-rafflepicks'] = tickets[2]
    S['L1-buildweeks'] = 6 * 7 + 4
    S['L1-borrowedbooks'] = 20 + 14 + 13 + 24
    dirs = ['north', 'east', 'south', 'west']
    i = dirs.index('east')
    for turn in 'LLLR':
        i = (i + (1 if turn == 'R' else -1)) % 4
    S['L1-robotturns'] = dirs[i]
    S['L1-hatscarf'] = sum(1 for h in range(6) for s in range(9))
    S['L1-coveredbit'] = [d for d in range(10) if int('5%d' % d) - 18 == 36][0]
    # ------------------------------------------------------------------ LEVEL 2
    S['L2-padlockcode'] = [100 * a + 10 * b + c for a in range(1, 10) for b in range(10) for c in range(10) if a + b + c == 14 and b == 4 and a == c + 2][0]
    S['L2-footballmatch'] = (6 * 60 + 10) - (4 * 60 + 35)
    S['L2-satayleft'] = 800 - 235 - 310
    S['L2-hallchairs'] = (123 - 1) % 12 + 1
    S['L2-fieldparts'] = F(9 - 2 - 3, 9)
    tall = ['kumar', 'aminah', 'farid', 'xin yi']                         # Kumar > Aminah > Farid > Xin Yi
    S['L2-tallestfour'] = tall[1]
    aina = (192 - 15 - 24) // 3
    S['L2-paperstars'] = aina + 24
    S['L2-pencilsodd'] = 'odd' if (4 * 1 + 2 * 0) % 2 else 'even'          # only the four odd tubes can change the parity
    ways = [[1] * 5 for _ in range(5)]
    for r in range(1, 5):
        for c in range(1, 5):
            ways[r][c] = ways[r - 1][c] + ways[r][c - 1]
    S['L2-boardroutes'] = ways[4][4]
    S['L2-ferryhours'] = (24 - 16) + 7
    S['L2-carparkbays'] = sum(1 for r in range(9) for c in range(14) if r in (0, 8) or c in (0, 13))
    S['L2-bookcase'] = 25 + (5 - 1) * ((165 - 25) // (8 - 1))
    S['L2-dartring'] = [sorted(t)[1] for t in itertools.combinations([14, 20, 24, 48, 54, 59], 3) if sum(t) == 103][0]
    S['L2-canrecycle'] = max([138, 254, 96, 187]) - min([138, 254, 96, 187])
    S['L2-penspacks'] = 6 * 4 + 5 * 7
    S['L2-smudgesum'] = [d for d in range(10) if int('3%d6' % d) + 428 == 744][0]
    bits = {'emily': F(1, 6), 'jiayi': F(1, 3), 'hakim': F(1, 8)}
    S['L2-breadshare'] = max(bits, key=bits.get)
    tags = [60, 70, 40, 30, 90, 20, 50]                                    # bubble sort counts the neighbour swaps
    swaps = 0
    arr = tags[:]
    done = False
    while not done:
        done = True
        for k in range(len(arr) - 1):
            if arr[k] > arr[k + 1]:
                arr[k], arr[k + 1] = arr[k + 1], arr[k]
                swaps += 1
                done = False
    S['L2-bookswaps'] = swaps
    S['L2-marathon'] = 34 + 7 - 4 - 8
    S['L2-netballleague'] = 13 * 12 // 2
    S['L2-roomstickers'] = min(100 * a + 10 * b + c for a, b, c in itertools.permutations([8, 3, 6, 1, 4], 3) if c % 2 == 1)
    ok = reachable([4, 7], 40)
    S['L2-topupvouchers'] = sum(ok[1:])
    S['L2-kitedrum'] = [k for k in range(1, 70) for d in range(1, 70) if 2 * k + d == 65 and k + 2 * d == 46][0]
    az = sorted(range(1, 19), key=lambda k: WORDS[k])
    S['L2-cardstack'] = az[6]
    edges = {('gate', 'pool'): 6, ('gate', 'canteen'): 4, ('canteen', 'field'): 3, ('pool', 'hall'): 9, ('field', 'hall'): 7}
    best, via = 10 ** 9, None
    for mid in ('pool', 'canteen', 'field'):                               # every route is gate -> (canteen ->) mid -> hall, so try the three ways
        if mid == 'pool':
            t = edges[('gate', 'pool')] + edges[('pool', 'hall')]
        elif mid == 'field':
            t = edges[('gate', 'canteen')] + edges[('canteen', 'field')] + edges[('field', 'hall')]
        else:
            continue                                                        # canteen is never next to the hall
        if t < best:
            best, via = t, mid
    S['L2-gatetohall'] = via
    S['L2-shoegraph'] = (11 - 4) * 25
    S['L2-bunboxes6'] = 14 * 6 + 5
    new = int('753')                                                        # 573 with the hundreds and tens digits swapped
    S['L2-phoneswap'] = new - 573
    S['L2-festivalshows'] = len(set(range(18, 73)) & set(range(41, 77)))
    S['L2-beanflower'] = 28 + 28 - 31                                       # March has 31 days
    S['L2-kuehroll'] = 10 // (3 - 1) * (11 - 1)
    return S


def canon(v):
    if isinstance(v, str):
        return v.lower()
    v = F(v)
    return str(v.numerator) if v.denominator == 1 else '%d/%d' % (v.numerator, v.denominator)


def bank_value(e):
    if e['type'] == 's':
        s = e['ans'].lower()
        return s
    a = F(e['ans'])
    return str(a.numerator) if a.denominator == 1 else '%d/%d' % (a.numerator, a.denominator)


def main():
    bank = {}
    for lv, items in json.load(open(os.path.join(HERE, 'batches', 'm01', 'bank.json'), encoding='utf-8'))['levels'].items():
        for e in items:
            bank[e['id']] = e
    mine = solve_all()
    rows, bad, per = [], 0, {}
    for pid, val in mine.items():
        e = bank[pid]
        mv, bv = canon(val), bank_value(e)
        ok = mv == bv
        bad += not ok
        per.setdefault(e['level'], []).append((pid, e['date'], mv, bv, ok))
    missing = sorted(set(bank) - set(mine))
    lines = ['# Second reader, January 2027 batch, Levels 1 and 2', '',
             'Script: `second_reader_jan_l1l2.py`. It imports none of the generator, checker, builder, verifier, taxonomy or defs code; every puzzle was solved from its printed '
             'question (numbers copied from the wording, arithmetic by enumeration or simulation in plain Python) and the bank answer was opened afterwards. '
             'All 31 puzzles of each level were read, so every one of the 15 or more per level the owner asks for is covered.', '',
             '| Level | Puzzles | Agree | Not read |', '|---|---|---|---|']
    for lv in sorted(per):
        rs = per[lv]
        lines.append('| %d | %d | %d | %d |' % (lv, len(rs), sum(r[4] for r in rs), 31 - len(rs)))
    lines += ['', '| Puzzle | Date | Second reader | Bank | |', '|---|---|---|---|---|']
    for lv in sorted(per):
        for pid, date, mv, bv, ok in per[lv]:
            lines.append('| %s | %s | %s | %s | %s |' % (pid, date, mv, bv, 'agree' if ok else '**DIFFERENT**'))
    if missing:
        lines += ['', 'Not read: %s' % ', '.join(missing)]
    open(os.path.join(HERE, 'batches', 'm01', 'SECOND_READER_JAN_L1L2.md'), 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
    for lv in sorted(per):
        print('Level %d: %d puzzles, %d agree' % (lv, len(per[lv]), sum(r[4] for r in per[lv])))
        for pid, date, mv, bv, ok in per[lv]:
            if not ok:
                print('   DIFFERENT', pid, 'second reader', mv, 'bank', bv)
    print('total %d puzzles, %d disagreements, %d not read' % (sum(len(v) for v in per.values()), bad, len(missing)))
    return 1 if (bad or missing) else 0


if __name__ == '__main__':
    raise SystemExit(main())
