"""Independent answer checks for Lesson 6 (Tens Jump, Ones Hop).

Every answer in l06.json is recomputed here by walking along the number path one step at a time (a jump is ten single steps,
a hop is one), not by re-using the lesson's own expressions. run(d) returns the number of checks; any failure raises AssertionError.
"""
import re
from collections import deque


def walk(start, moves):
    """moves: list of ('jump', +/-k tens) or ('hop', +/-k ones). Walk one single step at a time; return the landing number."""
    pos = start
    for kind, k in moves:
        step = 1 if k > 0 else -1
        for _ in range(abs(k) * (10 if kind == 'jump' else 1)):
            pos += step
    return pos


def no_renaming(start, moves):
    """True if every hop stays inside the same ten (the lesson never passes nine ones) and the path stays between 0 and 99."""
    pos = start
    for kind, k in moves:
        before = pos
        pos = walk(pos, [(kind, k)])
        if not 0 <= pos <= 99:
            return False
        if kind == 'hop' and before // 10 != pos // 10:
            return False
    return True


def digits(n):
    return divmod(n, 10)


def fewest_jumps(dist, sizes=(10, 20)):
    """Breadth-first search: fewest jumps (sizes allowed) that travel exactly dist."""
    seen = {0: 0}
    q = deque([0])
    while q:
        x = q.popleft()
        for s in sizes:
            y = x + s
            if y <= dist and y not in seen:
                seen[y] = seen[x] + 1
                q.append(y)
    return seen.get(dist)


def jumps_between(a, b):
    n = 0
    while a < b:
        a = walk(a, [('jump', 1)])
        n += 1
    assert a == b
    return n


# ---- oracles for the online-practice templates (brute force walks, independent of the template expressions)
def _chk(start, moves):
    assert no_renaming(start, moves), (start, moves)
    return walk(start, moves)

ORACLES = {
    'c1': lambda e: _chk(e['t'] * 10 + e['o'], [('jump', e['m'])]),
    'c2': lambda e: _chk(e['t'] * 10 + e['o'], [('jump', -e['m'])]),
    'c3': lambda e: _chk(e['t'] * 10 + e['o'], [('hop', e['p'])]),
    'c4': lambda e: _chk(e['t'] * 10 + e['o'], [('hop', -e['p'])]),
    'c6': lambda e: _chk(e['t'] * 10 + e['o'], [('jump', e['m'])]),
    't1': lambda e: _chk(e['t'] * 10 + e['o'], [('hop', e['p']), ('jump', e['m'])]),            # hop first: the order must not matter
    't2': lambda e: _chk(e['t'] * 10 + e['o'], [('hop', -e['p']), ('jump', -e['m'])]),
    't4': lambda e: walk(e['t'] * 10 + e['o'], [('jump', -e['m'])]),                      # undo the forward jumps
    'g1': lambda e: jumps_between(e['a'], e['a'] + 10 * e['t']),
    'g2': lambda e: fewest_jumps(10 * e['t']),
    'g3': lambda e: _chk(e['s'], [('jump', e['a']), ('jump', -e['b']), ('hop', e['c'])]),
}
BASE_ENV = {'c1': dict(t=3, o=4, m=2), 'c2': dict(t=5, o=8, m=2), 'c3': dict(t=3, o=4, p=3), 'c4': dict(t=4, o=7, p=3),
            'c6': dict(t=3, o=4, m=2), 't1': dict(t=3, o=4, m=2, p=5), 't2': dict(t=6, o=8, m=2, p=4), 't4': dict(t=7, o=8, m=3),
            'g1': dict(a=7, t=9), 'g2': dict(a=7, t=9), 'g3': dict(s=25, a=3, b=1, c=4)}


def strips_ok(blocks, eq):
    """Every numrow shaped number, '+10', number, '-5', number ... must add up."""
    for b in blocks:
        if b['t'] == 'numrow':
            it = b['items']
            if len(it) >= 3 and all(isinstance(x, int) for x in it[0::2]) and all(isinstance(x, str) and re.fullmatch(r'[+-]\d+', x) for x in it[1::2]):
                for i in range(0, len(it) - 2, 2):
                    eq(int(it[i]) + int(it[i + 1]), it[i + 2], 'jump strip ' + str(it))
            else:
                for x in it:
                    m = re.fullmatch(r'(\d+) ([+-]) (\d+)( = (\d+))?', str(x))
                    if m and m.group(5):
                        a, op, c, r = int(m.group(1)), m.group(2), int(m.group(3)), int(m.group(5))
                        eq(a + c if op == '+' else a - c, r, 'sum tile ' + str(x))
        if b['t'] == 'visual' and b['type'] == 'number_line':
            for a, z, lab in b['jumps']:
                eq(a + int(lab), z, 'number line arc ' + lab)
                eq(b['start'] <= min(a, z) and max(a, z) <= b['end'], True, 'arc on the line')
        if b['t'] == 'cols':
            for c in b['cols']:
                strips_ok(c, eq)


def run(d):
    n = 0

    def eq(a, b, msg=''):
        nonlocal n
        n += 1
        assert a == b, f'{msg}: got {a}, expected {b}'
    T = {q['id']: q for q in d['tiers']['start'] + d['tiers']['think'] + d['tiers']['go']}
    X = {q['id']: q for q in d['exit']}
    H = {h['id']: h for h in d['home_practice']}

    # whole-number facts the lesson relies on: over every 2-digit number, a jump changes only the tens digit, a hop only the ones digit
    for k in range(10, 90):
        eq(digits(walk(k, [('jump', 1)]))[1], digits(k)[1], 'jump keeps ones digit ' + str(k))
        eq(digits(walk(k, [('jump', 1)]))[0], digits(k)[0] + 1, 'jump adds one ten ' + str(k))
    for k in range(10, 99):
        if k % 10 < 9:
            eq(digits(walk(k, [('hop', 1)]))[0], digits(k)[0], 'hop keeps tens digit ' + str(k))

    # sneak-peek
    eq(walk(26, [('jump', 1)]), 36, 'sneak 1'); eq(d['sneak_peek']['val1'], 36, 'sneak val1')
    eq(walk(43, [('jump', 2)]), 63, 'sneak 2'); eq(63 == 45, False, 'sneak 2: Ravi is wrong'); eq(walk(43, [('hop', 2)]), 45, 'sneak 2: his answer is a hop')
    sk = [s for s in d['slides'] if s['id'] == 's-sneak'][0]
    def find(blocks):
        for b in blocks:
            if b['t'] == 'visual' and b['type'] == 'bundles': return b
            if b['t'] == 'cols':
                for c in b['cols']:
                    r = find(c)
                    if r: return r
    v = find(sk['blocks'])
    eq(v['tens'] * 10 + v['ones'], 26, 'sneak picture shows 26')

    # every strip and sum tile drawn on a slide
    for s in d['slides']:
        strips_ok(s['blocks'], eq)

    # Start here
    eq(T['S1']['val'], [3, 7, walk(27, [('jump', 1)])], 'S1')
    eq(T['S1']['visual']['tens'] * 10 + T['S1']['visual']['ones'], 27, 'S1 picture')
    eq(T['S2']['val'], [walk(34, [('jump', 2)])], 'S2')
    eq(T['S3']['val'], [walk(23, [('jump', 1)]), walk(23, [('jump', 4)]), walk(51, [('jump', 3)]), walk(7, [('jump', 6)])], 'S3')
    eq(T['S4']['val'], [walk(34, [('jump', -1)]), walk(58, [('jump', -2)]), walk(58, [('hop', -3)]), walk(62, [('hop', 7)])], 'S4')
    eq(T['S5']['val'], [walk(68, [('jump', -3)])], 'S5')
    eq(T['S6']['val'], [walk(45, [('jump', 2)])], 'S6'); eq(walk(45, [('hop', 2)]), 47, 'S6 Ben hopped'); eq(47 == 65, False, 'S6 Ben is wrong')
    eq(T['S7']['val'], [walk(36, [('jump', 1), ('jump', 1)])], 'S7')
    # Think harder
    eq(T['T1']['val'], [walk(23, [('jump', 4), ('hop', 5)])], 'T1');
    eq([x['val'] for x in T['T1']['parts']], [[40, walk(23, [('jump', 4)])], [walk(23, [('jump', 4)]), 5, 68], 68], 'T1 frames'); eq(walk(23, [('hop', 5), ('jump', 4)]), 68, 'T1 other order'); eq(23 + 45, 68, 'T1 plain sum')
    eq(T['T2']['val'], [walk(79, [('jump', -3), ('hop', -5)])], 'T2');
    eq([x['val'] for x in T['T2']['parts']], [[30, walk(79, [('jump', -3)])], [walk(79, [('jump', -3)]), 5, 44], 44], 'T2 frames'); eq(79 - 35, 44, 'T2 plain')
    a = walk(12, [('jump', 3), ('hop', 4)]); b = walk(12, [('hop', 4), ('jump', 3)])
    eq(a, b, 'T3 same landing'); eq(T['T3']['val'], ['same', a], 'T3'); eq(a, 46, 'T3 value')
    eq(T['T4']['val'], [walk(78, [('jump', -3)])], 'T4'); eq(walk(48, [('jump', 3)]), 78, 'T4 check')
    # Go further
    path = [7]
    while path[-1] < 97: path.append(walk(path[-1], [('jump', 1)]))
    eq(path, [7, 17, 27, 37, 47, 57, 67, 77, 87, 97], 'G1 example route of tens')
    route2 = [7]
    for j in (2, 2, 2, 2, 1): route2.append(walk(route2[-1], [('jump', j)]))
    eq(route2, [7, 27, 47, 67, 87, 97], 'G1 example route with 20s'); eq(route2 != path, True, 'G1 two routes differ')
    eq(sum(1 for a, b in zip(route2, route2[1:]) if b - a in (10, 20)), len(route2) - 1, 'G1 every jump is 10 or 20')
    eq(T['G1']['val'], ['open'], 'G1 open')
    eq(fewest_jumps(90), 5, 'G2 by search'); eq(T['G2']['val'], [5], 'G2'); eq(T['G2']['parts'][0]['val'], fewest_jumps(90), 'G2 part a'); eq(walk(7, [('jump', 8)]), 87, 'G2 four jumps of 20 only reach 87')
    eq(fewest_jumps(90) == 4, False, 'G2: 4 jumps are not enough'); eq(max(20 * 4, 0), 80, 'G2 four jumps travel at most 80')
    g3 = walk(25, [('jump', 3), ('jump', -1), ('jump', 2)])
    eq(g3, 65, 'G3 before the hop'); eq(walk(g3, [('hop', 4)]), 69, 'G3 lands on 69'); eq(T['G3']['parts'][1]['val'], 69 - g3, 'G3 hop')
    eq(walk(25, [('jump', 3)]), 55, 'G3 step 1'); eq(walk(55, [('jump', -1)]), 45, 'G3 step 2'); eq(walk(45, [('jump', 2)]), 65, 'G3 step 3')
    eq(T['G3']['parts'][2]['val'], (g3 - 25) // 10, 'G3 net tens'); eq(walk(25, [('jump', 4)]), g3, 'G3 one jump of 4 tens')
    eq(T['G3']['val'], [4, 4], 'G3')
    # Investigation: jumps of ten from a start never change the ones digit; which starts can land exactly on 50
    reach = [s for s in range(0, 100) if 50 in [walk(s, [('jump', j)]) for j in range(0, 11) if walk(s, [('jump', j)]) <= 99]]
    eq(reach, [0, 10, 20, 30, 40, 50], 'I1 starts that land on 50 (50 itself counts as zero jumps)')
    eq(all(x % 10 == 6 for x in [walk(6, [('jump', j)]) for j in range(0, 10)]), True, 'I1 from 6 every landing ends in 6')
    eq(50 in [walk(6, [('jump', j)]) for j in range(0, 10)], False, 'I1 never 50 from 6')
    # Talk, exit
    eq(digits(walk(34, [('jump', 2)])), (5, 4), 'talk: tens digit changed, ones digit stayed')
    eq(X['E1']['val'], [walk(46, [('jump', 3)])], 'E1')
    eq(X['E2']['val'], [walk(74, [('jump', -3)]), walk(74, [('hop', -3)])], 'E2')
    eq(X['E3']['val'], [walk(52, [('jump', 2)]), walk(52, [('jump', 2), ('hop', 3)])], 'E3')
    # Home practice
    eq(H['H1']['val'], walk(45, [('jump', 3)]), 'H1')
    eq(H['H2']['val'], [walk(86, [('jump', -4)]), walk(86, [('hop', -4)])], 'H2')
    eq(H['H3']['val'], [walk(53, [('hop', -3)]), walk(53, [('jump', -3)])], 'H3')
    eq(H['H4']['val'], walk(36, [('jump', 2), ('hop', 3)]), 'H4'); eq(walk(36, [('hop', 3), ('jump', 2)]), 59, 'H4 other order')
    # Optional slide and spare-time menu
    p = 5
    jumps = 0
    while p + 10 < 100: p += 10; jumps += 1
    eq((p, jumps), (95, 9), 'optional slide: last landing before 100 from 5')
    eq(digits(walk(34, [('jump', 1)])), (4, 4), 'M1 34 + 10'); eq(digits(walk(67, [('jump', 1)])), (7, 7), 'M1 67 + 10'); eq(walk(90, [('jump', 1)]), 100, 'M1 90 + 10 is a hundred')
    eq(walk(23, [('jump', 3), ('hop', 4)]), 57, 'M2 example'); eq(walk(52, [('jump', 3), ('hop', 1)]), 83, 'M3 52 + 31')
    # Online practice authored answers
    O = {i['id']: i for i in d['online_practice']['items']}
    for k in ('c1', 'c2', 'c3', 'c4', 'c6', 't1', 't2', 't4', 'g1', 'g2', 'g3'):
        eq(O[k]['answer'], ORACLES[k](BASE_ENV[k]), 'online ' + k)
    eq(O['c5']['answer'], '45 + 30', 'c5'); eq(walk(45, [('jump', 3)]) - 45, 30, 'c5 the jump is 30')
    eq(O['t3']['answer'], 'They land on the same number', 't3'); eq(walk(12, [('jump', 3), ('hop', 4)]), walk(12, [('hop', 4), ('jump', 3)]), 't3 oracle')
    eq(walk(23, [('jump', 3), ('hop', 4)]), 57, 'g4 example')
    return n
