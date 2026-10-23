"""Independent checks for the Terms 3 and 4 STUB lesson (lessons/l21.json). ORACLES drive the practice-template checks."""

ORACLES = {
    'c1': lambda e: sum(1 for _ in range(e['n'])),
    'c2': lambda e: {'a': e['a'], 'b': e['b'], 'c': sum(e['b'] for _ in range(e['a']))},
    'c3': lambda e: 'odd' if sum(1 for i in range(1, e['n'] + 1)) % 2 else 'even',
    'c4': lambda e: [i for i in range(1, e['lim'] + 1) if i % e['k'] == 0],
    'c5': lambda e: len([i for i in range(1, e['n'])]),
    't3': lambda e: [i for i in range(1, e['lim'] + 1) if i % e['a'] == 0 and i % e['b'] == 0],
    'g1': lambda e: e['n'] + e['n'],
    'c7': lambda e: {'h': e['h'], 'mm': e['m']},
    'c8': lambda e: sum(1 for _ in range(10 - e['p'])),
}
BASE_ENV = {'c1': {'n': 7}}


def run(d):
    n = 0
    assert d.get('stub'), 'l21 is a template stub'
    n += 1
    assert 4 + 6 == 10
    n += 1
    return n
