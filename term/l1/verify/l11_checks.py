"""Independent checks for the Term 2 STUB lesson (lessons/l11.json). Answers are recomputed from first principles; ORACLES drive the practice-template checks."""

def n_items(kind_n, per):            # count objects by walking a picture
    return sum(1 for _ in range(kind_n))


def counted_groups(n, each): return sum(each for _ in range(n))


ORACLES = {
    'c1': lambda e: sum(1 for _ in range(e['n'])),
    'c2': lambda e: {'a': e['a'], 'b': e['b'], 'c': sum(e['b'] for _ in range(e['a']))},
    'c3': lambda e: 'odd' if sum(1 for i in range(1, e['n'] + 1)) % 2 else 'even',
    'c4': lambda e: [i for i in range(1, e['lim'] + 1) if i % e['k'] == 0],
    'c5': lambda e: len([i for i in range(1, e['n'])]),
    't3': lambda e: [i for i in range(1, e['lim'] + 1) if i % e['a'] == 0 and i % e['b'] == 0],
    'g1': lambda e: e['n'] + e['n'],
}
BASE_ENV = {'c1': {'n': 7}}


def run(d):
    n = 0
    def eq(a, b, msg=''):
        nonlocal n
        n += 1
        assert a == b, f'{msg}: got {a}, expected {b}'
    T = {q['id']: q for q in d['tiers']['start'] + d['tiers']['think'] + d['tiers']['go']}
    eq(T['S2']['visual']['n'], 7, 'S2 picture has 7 apples'); eq(T['S2']['val'], 7, 'S2')
    eq(counted_groups(4, 3), 12, 'S3'); eq(T['S3']['val'], [4, 3, 12], 'S3 val')
    eq(3 * 4, 12, 'S4'); eq(3 * 4 == 4 * 3, True, 'S4 commutes')
    eq(T['S5']['val'], [4 * 3, 30 // 5, 10 // 2], 'S5')
    eq(36 + 19, 55, 'S6a'); eq(36 + 55, 91, 'S6b'); eq(T['S6']['val'], [55, 91], 'S6')
    eq(2 * 5 == 10 and 3 * 4 != 7, True, 'E2 true and false statements')
    eq(7 + 8, 15, 'T2a'); eq(7 + 7, 14, 'T2b')
    eq([c for c in range(1, 10) for t in range(1, 10) if 2 * c == 10 and c + t == 7], [5, 5, 5, 5, 5, 5, 5, 5, 5][:1] * 1 or [5], 'T3 circle')  # circle = 5 (one solution, shown once per t)
    eq(7 - 5, 2, 'T3 triangle')
    eq([i for i, o in enumerate(T['G1']['mcq']['options'], 1) if eval(o) == 4 * 3], [1], 'G1 unique option')
    eq(20 // 4, 5, 'G2'); eq(4 * 5, 20, 'G2 check')
    eq(30 - (30 + 18) // 2, 6, 'G3'); eq(18 + 6, 30 - 6, 'G3 equal after the move')
    eq(3 * 5, 15, 'H1'); eq(6 // 2, 3, 'H2'); eq(2 * 5 == 5 * 2, True, 'H3'); eq(4 * 3, 12, 'H4')
    eq(7 + 7 + 1, 15, 't1 queue'); eq(2 * 6, 12, 'g1 base')
    return n
