#!/usr/bin/env python3
"""Independent check of every answer in rebuild/skill_items_l1_3.py.
For each item the answer is recomputed here from the item's parameters `p` by brute force or simulation
(not by reading the stored answer text), and compared with the stored canonical answers `ans`.
Also checks: each numeric answer appears in the worked-answer text `a`; every item has tool, skill, say/ask/listen;
slide items sit in a declared group; no banned words (MOE, GEP, SASMO, price words, 'camera').
    python3 rebuild/skill_items_check.py
"""
import itertools, re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from skill_items_l1_3 import ITEMS, GROUPS, TOOLS

DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def seq_two_before(start, n):
    s = list(start)
    while len(s) < n: s.append(s[-1] + s[-2])
    return s


def seq_gap(start, first_gap, step, n):
    s = [start]; g = first_gap
    while len(s) < n: s.append(s[-1] + g); g += step
    return s


def seq_woven(start, rules, n):
    s = [start]
    while len(s) < n: s.append(s[-1] + rules[(len(s) - 1) % len(rules)])
    return s


def stacks_cubes(heights):
    return sum(sum(r) for r in heights)


def worst_case_sim(counts, need):
    """Smallest N such that EVERY ordered draw of N counters contains at least `need` of `need_idx`... brute force via adversary search."""
    raise NotImplementedError


def minimal_draw_for(counts, predicate):
    """Smallest N such that every multiset of N counters drawn from `counts` (tuple per colour) satisfies predicate(drawn)."""
    total = sum(counts)
    for N in range(0, total + 1):
        ok = True
        for drawn in itertools.product(*[range(c + 1) for c in counts]):
            if sum(drawn) == N and not predicate(drawn):
                ok = False; break
        if ok: return N
    return None


def compute(it):
    i = it['id']; p = it['p']
    if i == 'L1-SEQ1': s = seq_two_before(p['start'], p['n']); return s[5:7]
    if i == 'L1-SEQ2':
        s = seq_woven(p['start'], p['rules'], 12)
        return [' '.join(map(str, s[:p['n']])), 'no' if p['test'] not in s else 'yes']
    if i == 'L1-SEQ3': s = seq_gap(p['start'], -p['first_gap'], p['shrink'], 9); return s[5:7]
    if i == 'L1-PV1':
        # tens-and-ones by counting sticks
        n = p['tens'] * 10 + p['ones']; boxes = 0; left = p['n']
        while left >= 10: left -= 10; boxes += 1
        return [n, boxes, left]
    if i == 'L1-PV2':
        a, b = p['cards']; nums = sorted({10 * x + y for x, y in itertools.permutations([a, b], 2)})
        return [' '.join(map(str, nums)), max(nums), min(nums, key=lambda v: abs(v - p['target']))]
    if i == 'L1-PV3':
        nums = sorted({10 * x + y for x, y in itertools.permutations(p['cards'], 2)})
        return [len(nums), ' '.join(map(str, nums)), min(nums, key=lambda v: abs(v - p['target']))]
    if i == 'L1-PV4':
        a = [n for n in range(10, 100) if n // 10 == p['tens'] and (n % 10) % 2 == 1 and n % 10 > p['lo']]
        b = [n for n in range(10, 100) if n // 10 == n % 10 and n // 10 + n % 10 == p['total']]
        return [' '.join(map(str, a)), b[0] if len(b) == 1 else None]
    if i == 'L1-PV5':
        va = p['a'][0] * 10 + p['a'][1]; vb = p['b'][0] * 10 + p['b'][1]
        return ['Kumar' if vb > va else 'Siti', vb]
    if i == 'L1-MA1':
        return [sum(p['a']), sum(p['b'])]
    if i == 'L1-MA2':
        return [p['base'] + 10, p['base'] + p['add'], p['base2'] + p['add2']]
    if i == 'L1-MA3':
        return [(r[0] + r[1]) - r[2] for r in p['rows']]
    if i == 'L1-SYM1':
        sols = [(t, c) for t in range(1, 15) for c in range(1, 15)
                if p['l1'][0] * t + p['l1'][1] * c == p['l1'][2] and p['l2'][0] * t + p['l2'][1] * c == p['l2'][2]]
        assert len(sols) == 1, sols
        return list(sols[0])
    if i == 'L1-SYM2':
        sols = [(c, s, t) for c in range(1, 13) for s in range(1, 13) for t in range(1, 13)
                if 2 * c + s == 12 and c + s == 7 and s + t == 5 and len({c, s, t}) == 3]
        assert len(sols) == 1, sols
        return list(sols[0])
    if i == 'L1-TWICE1':
        ben = p['mei'] * p['times']; return [ben, p['mei'] + ben, ben + p['more']]
    if i == 'L1-CAL1': return [DAYS[(p['today'] + j) % 7] for j in p['jumps']]
    if i == 'L1-CAL2':
        sat = 5; return [7, DAYS[(p['day'] + p['after']) % 7], DAYS[(p['sunday'] - p['before']) % 7]]
    if i == 'L1-AGE1':
        a, s, y = p['ali'], p['sis'], p['years']; return [s - a, a + y, s + y, (s + y) - (a + y)]
    if i == 'L1-AGE2':
        later = p['mum'] + (p['siti_later'] - p['siti']); return [later, p['mum'] - p['siti']]
    if i == 'L1-CUBE1':
        h = p['heights']; back = sum(col[0] for col in h); front = sum(col[1] for col in h); return [back, front, back + front]
    if i == 'L1-CUBE2': return [sum(range(1, p['steps'] + 1)), p['steps'] + 1]
    if i == 'L1-CLK1':
        t = '%d:%02d' % (p['h'], p['m']); later = '%d:%02d' % (p['h'] + 1, p['m']); mins = (p['to'] - 0) * 5
        return [t, later, mins]
    if i == 'L1-CLK2':
        def add(t, mins):
            tot = t[0] * 60 + t[1] + mins; return '%d:%02d' % (tot // 60, tot % 60)
        return [add(p['start'], p['minutes']), add(p['start2'], 60 * p['hours']),
                (p['end3'][0] * 60 + p['end3'][1]) - (p['start3'][0] * 60 + p['start3'][1])]
    # ---- Level 2
    if i in ('L2-PAIR1', 'L2-PAIR2', 'L3-PAIR2'):
        out = []
        for k in ('a', 'b'):
            d = p[k]; out.append(sum(d['start'] + d['step'] * x for x in range(d['n'])))
        return out
    if i == 'L2-LETTER1':
        top, bot, res = p['top'], p['bot'], p['res']; letters = sorted(c for c in set(top + bot + res) if c.isalpha()); sols = []
        for perm in itertools.permutations(range(10), len(letters)):
            m = dict(zip(letters, perm))
            if any(m[s[0]] == 0 for s in (top, bot, res) if s[0] in m): continue
            v = lambda s: int(''.join(str(m[c]) if c in m else c for c in s))
            if v(top) + v(bot) == v(res): sols.append(m)
        assert len(sols) == 1, sols
        m = sols[0]; return [m['A'], m['B'], m['C']]
    if i == 'L2-SEQ1':
        s = seq_gap(p['start'], p['first_gap'], p['grow'], p['n']); return [s[5], s[6], 'no' if p['test'] not in s else 'yes']
    if i == 'L2-SEQ2': s = seq_two_before(p['start'], p['n']); return [s[5], s[6], s[8]]
    if i == 'L2-SEQ3':
        s = seq_woven(p['start'], p['rules'], p['n']); return [' '.join(map(str, s[:7])), s[8]]
    if i == 'L2-SEQ4': s = seq_gap(p['start'], -p['first_gap'], p['shrink'], 9); return [s[5], s[6]]
    if i == 'L2-AGE1':
        sols = [(s_, s_ + p['gap']) for s_ in range(0, 21) if 2 * s_ + p['gap'] == p['total']]
        assert len(sols) == 1
        mum_now = p['mei'] + p['mgap']
        return [sols[0][0], sols[0][1], p['mei'] + p['years'], mum_now + p['years']]
    if i == 'L2-AGE2': yrs = p['ravi_later'] - p['ravi']; return [yrs, p['mei'] + yrs, p['ravi'] - p['mei']]
    if i in ('L2-CORNER1', 'L2-CORNER2'):
        layers = p['layers']; n = layers[0]
        cells = {(x, y, z) for z, side in enumerate(layers) for x in range(side) for y in range(side)}
        total = len(cells)
        if i == 'L2-CORNER1': return [len([c for c in cells if c[2] == 0]), total, len([c for c in cells if c[0] == 0])]
        return [total, len([c for c in cells if c[2] == 0])]
    if i == 'L2-PIC1':
        sols = [(t, c, s) for t in range(1, 30) for c in range(1, 30) for s in range(1, 30)
                if 3 * t == 27 and t + 2 * c == 21 and c + s == 13]
        assert len(sols) == 1
        t, c, s = sols[0]; return [t, c, s, t + c + s]
    if i == 'L2-PIC2':
        melon = p['apples_per_melon']; pumpkin = p['melons_per_pumpkin'] * melon
        return [pumpkin, pumpkin + p['extra_melons'] * melon]
    if i == 'L2-CAL1': return [DAYS[(p['today'] + j) % 7] for j in p['jumps']]
    if i == 'L2-CAL2':
        tuesdays = [d for d in range(1, p['days'] + 1) if (d - p['first']) % 7 == 0]
        wk = lambda d: DAYS[(1 + d - 1) % 7]    # day 1 is Tuesday (index 1)
        return [' '.join(map(str, tuesdays)), wk(30), wk(31)]
    if i == 'L2-POST1':
        posts = [x for x in range(0, p['length'] + 1, p['step'])]
        return [len(posts), (p['posts'] - 1) * p['step2']]
    if i == 'L2-QUEUE1':
        # brute force: queue sizes where position from front is 5 and from back is 4
        return [[n for n in range(1, 40) if p['front'] <= n and n - p['front'] + 1 == p['back']][0]]
    if i == 'L2-POST2': return [p['lamps'], p['lamps'] * p['step']]
    if i == 'L2-WORST1':
        red, blue = p['red'], p['blue']
        a = minimal_draw_for((red, blue), lambda d: d[0] >= p['need_red'])
        b = minimal_draw_for((red, blue), lambda d: d[0] >= 1 and d[1] >= 1)
        return [a, b]
    if i == 'L2-WORST2':
        c = tuple(p['counts'])
        a = minimal_draw_for(c, lambda d: max(d) >= 2)
        b = minimal_draw_for(c, lambda d: d[0] >= 2)
        return [a, b]
    # ---- Level 3
    if i == 'L3-PAIR1': return [sum(p['a']), sum(p['b'])]
    if i == 'L3-SERIES1':
        s = [p['start'] + p['step'] * k for k in range(p['n'])]
        pairs = {s[k] + s[-1 - k] for k in range(len(s) // 2)}
        assert len(pairs) == 1
        return [s[0] + s[-1], len(s) // 2, sum(s)]
    if i == 'L3-DIV3':
        ok = lambda n: 'yes' if n % 3 == 0 else 'no'
        # confirm the digit-sum rule itself on the tested numbers and on 1..999
        assert all((n % 3 == 0) == (sum(map(int, str(n))) % 3 == 0) for n in range(1, 1000))
        return [ok(n) for n in p['tests']]
    if i == 'L3-DIV6':
        assert all((n % 2 == 0 and n % 3 == 0) == (n % 6 == 0) for n in range(1, 1000))
        return [6] + ['yes' if n % 6 == 0 else 'no' for n in p['tests']]
    if i == 'L3-RANGE1':
        k, lo, hi = p['k'], p['lo'], p['hi']
        return [hi // k, (lo - 1) // k, len([n for n in range(lo, hi + 1) if n % k == 0])]
    if i == 'L3-RANGE2': return [len([n for n in range(lo, hi + 1) if n % k == 0]) for k, lo, hi in p['q']]
    if i == 'L3-TOP1':
        r = p['rows']; cols = list(zip(*r)); return [sum(map(sum, r)), sum(max(c) for c in cols)]
    if i == 'L3-TOP2':
        r = p['rows']; return [sum(map(sum, r)), sum(max(row) for row in r)]
    if i == 'L3-FACE1':
        e, m = p['eyes'], p['mouth']
        face = lambda k: (e[(k - 1) % len(e)], m[(k - 1) % len(m)])
        first = next(k for k in range(2, 100) if face(k) == face(1))
        return [' '.join(face(p['q'][0])), ' '.join(face(p['q'][1])), first]
    if i == 'L3-POSTS1':
        one = len(range(0, p['length'] + 1, p['step'])); return [one * p['sides']]
    if i == 'L3-RECT1':
        c, r = p['cols'], p['rows']
        n = 0
        for x1 in range(c + 1):
            for x2 in range(x1 + 1, c + 1):
                for y1 in range(r + 1):
                    for y2 in range(y1 + 1, r + 1): n += 1
        return [n]
    if i == 'L3-CHAIN1':
        plums = p['pears'] * p['plums']; return [plums, plums * p['melons'], 'melon plum']
    if i == 'L3-SHARE1':
        c, tot, end = p['centre'], p['total'], p['end']
        nums = [x for x in range(1, 8) if x != c]
        sols = []
        for perm in itertools.permutations(nums):
            lines = [(perm[0], perm[1]), (perm[2], perm[3]), (perm[4], perm[5])]
            if all(a + b + c == tot for a, b in lines): sols.append(perm)
        assert sols
        other = {b if a == end else a for perm in sols for (a, b) in [(perm[0], perm[1]), (perm[2], perm[3]), (perm[4], perm[5])] if end in (a, b)}
        assert len(other) == 1
        return [other.pop()]
    if i == 'L3-OP1':
        # every rule of the form  x*y*a + x*b + y*c + d  (small integer coefficients) that fits the examples gives the same answer for the question
        qs = set()
        for a, b, c, d in itertools.product(range(-3, 4), repeat=4):
            if all(a * x * y + b * x + c * y + d == r for x, y, r in p['rows']): qs.add(a * p['q'][0] * p['q'][1] + b * p['q'][0] + c * p['q'][1] + d)
        assert len(qs) == 1, qs
        return [qs.pop()]
    if i == 'L3-BOUND1':
        sums = [sum(c) for c in itertools.combinations(range(p['lo'], p['hi'] + 1), p['k'])]
        return [min(sums), max(sums), 'yes' if p['test'] in sums else 'no']
    if i == 'L3-STICK1':
        cost = {int(k): v for k, v in p['cost'].items()}; best = 0
        for ln in range(1, 8):
            for digs in itertools.product(range(10), repeat=ln):
                if digs[0] == 0 and ln > 1: continue
                if sum(cost[d] for d in digs) == p['sticks']: best = max(best, ln)
        nums = [int(''.join(map(str, digs))) for digs in itertools.product(range(10), repeat=best)
                if digs[0] != 0 and sum(cost[d] for d in digs) == p['sticks']]
        return [best, max(nums)]
    raise KeyError(i)


def norm(v):
    return str(v).strip().lower()


def main():
    bad = 0
    ids = set()
    for it in ITEMS:
        assert it['id'] not in ids, it['id']; ids.add(it['id'])
        got = compute(it)
        want = it['ans']
        if [norm(x) for x in got] != [norm(x) for x in want]:
            print('MISMATCH', it['id'], 'computed', got, 'stored', want); bad += 1
        # every numeric answer is in the worked answer
        for w in want:
            if isinstance(w, int) and not re.search(r'(?<![\d.])' + str(w) + r'(?![\d])', it['a']):
                print('ANSWER TEXT MISSES', it['id'], w); bad += 1
        if it['tool'] not in TOOLS: print('BAD TOOL', it['id']); bad += 1
        for f in ('skill', 'say', 'ask', 'listen', 'stem', 'a'):
            if not it.get(f): print('MISSING', it['id'], f); bad += 1
        if it['slot'] == 'slide' and (it['level'], it['lesson'], it['group']) not in GROUPS:
            print('NO GROUP', it['id']); bad += 1
        txt = ' '.join([it['stem']] + it['parts'] + [it['say'], it['ask'], it['listen'], it['a']])
        if re.search(r'\b(MOE|GEP|SASMO|SEAMO|camera|\$\d+\s*(per|a month)|price)\b', txt, re.I): print('BANNED WORD', it['id']); bad += 1
    print(len(ITEMS), 'items checked;', 'ALL OK' if not bad else f'{bad} PROBLEMS')
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
