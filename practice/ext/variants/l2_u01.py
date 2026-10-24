"""Variant families and wording overrides for extension Level 2 Unit 1 (the sidecar of data/l2_u01.json).

A variant family is a runner template (`tpl`: variables, arithmetic answer expressions) plus an ORACLE: independent
code (enumeration, digit strings, loops) that must give the same answer for every combination of the variables.
build_ext.py runs the oracle over every combination before it writes anything, so a variant cannot be wrong.
`base` is the authored item's own numbers: the template must reproduce the authored (and independently checked) answer there.
"""
import itertools

# ---- list answers: 'any' = the child may type them in any order, 'ordered' = the order is part of the answer
LIST_POLICY = {
    'L2U01-S04': 'ordered',     # "Begin with the smallest"
    'L2U01-S05': 'any',         # all the numbers the cards can make
    'L2U01-S07-a': 'any',
    'L2U01-S10-a': 'ordered',   # left to right, top to bottom
    'L2U01-S10-b': 'ordered',   # top, left, right, bottom
    'L2U01-T02-a': 'any',
}

# ---- wording that only makes sense on paper (a table to fill, "your list from the question before")
def q_override(checks):
    s05 = ', '.join(checks['L2U01-S05']())
    return {
        'L2U01-S05': 'Use the cards 8, 1 and 5 once each. Type all the 3-digit numbers the cards can make.',
        'L2U01-S06-a': f'The cards 8, 1 and 5 make these numbers: {s05}. Use this list.',
        'L2U01-S06-b': f'The cards 8, 1 and 5 make these numbers: {s05}. Use this list.',
        'L2U01-S06-c': f'The cards 8, 1 and 5 make these numbers: {s05}. Use this list.',
        'L2U01-S10-a': 'Piece A: type the 4 missing numbers, left to right and top to bottom.',
        'L2U01-S10-b': 'Piece B: type the 4 missing numbers in the order top, left, right, bottom.',
        'L2U01-T02-a': 'Find my number. It is odd and has 3 digits. My tens digit is 0. My digits add up to 11. Type all the numbers I could be.',
    }


# ---- oracles (independent of the templates' arithmetic) ----
def _perms_count(cards):
    return len({int(''.join(map(str, p))) for p in itertools.permutations(cards, 3) if p[0] != 0})

def _odd_between(lo, hi):
    return sum(1 for n in range(lo + 1, hi) if n % 2)

def _back(start, k):
    v = start
    for _ in range(k):
        v -= 10
    return v

VARIANTS = {
    # S01 (a): hundreds, tens and ones to a number
    'L2U01-S01-a': dict(
        base=dict(h=3, t=5, o=6),
        tpl=dict(vars=dict(h=[1, 2, 3, 4, 5, 6, 7, 8, 9], t=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], o=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
                 q='Place value. Fill in the blank.', frame='{h} hundreds, {t} tens and {o} ones = {n}', answers=dict(n='h*100+t*10+o'),
                 hint='Write the hundreds digit first, then the tens digit, then the ones digit.',
                 steps=['{h} hundreds is {h}00.', 'Put the tens and the ones after it: the tens digit is {t} and the ones digit is {o}.', 'The number is {ans}.']),
        oracle=lambda e: dict(n=int(str(e['h']) + str(e['t']) + str(e['o'])))),
    # C01: hundreds and a lot of tens
    'L2U01-C01': dict(
        base=dict(h=7, t=13),
        tpl=dict(vars=dict(h=[2, 3, 4, 5, 6, 7, 8], t=[11, 12, 13, 14, 15, 16]),
                 q='{h} hundreds and {t} tens =', answer='h*100+t*10',
                 hint='10 tens make 1 hundred. Change the tens into hundreds and tens first.',
                 steps=['{t} tens is {tt}.', '{h} hundreds is {hh}.', '{hh} + {tt} = {ans}.'], derive=dict(tt='t*10', hh='h*100')),
        oracle=lambda e: sum([100] * e['h'] + [10] * e['t'])),
    # L01 "Your turn": cards with a 0
    'L2U01-L01': dict(
        base=dict(a=9, z=0, c=3),
        tpl=dict(vars=dict(a=[1, 2, 3, 4], z=[0], c=[6, 7, 8, 9]),
                 q='Use the cards {a}, {z} and {c} once each. How many 3-digit numbers can you make?', answer='4',
                 hint='A number cannot start with 0. List the numbers that start with {a}, then the ones that start with {c}.',
                 steps=['Start with {a}: two numbers. Start with {c}: two numbers.', '0 cannot be the hundreds digit.', '2 + 2 = 4 numbers.']),
        oracle=lambda e: _perms_count([e['a'], e['z'], e['c']])),
    # C03: count back in 10s
    'L2U01-C03': dict(
        base=dict(s=312),
        tpl=dict(vars=dict(s=[312, 407, 523, 618, 704, 856, 931]),
                 q='Count back in 10s.', frame='{s},   {a},   {b},   {x},   {y}', answers=dict(x='x', y='y'),
                 derive=dict(a='s-10', b='s-20', x='s-30', y='s-40'),
                 hint='Counting back in 10s makes the tens digit 1 smaller each time.',
                 steps=['{s}, {a}, {b}, ...', 'Take away 10 again: {x}.', 'Take away 10 once more: {y}.']),
        oracle=lambda e: dict(x=_back(e['s'], 3), y=_back(e['s'], 4))),
    # C04: odd numbers between two even numbers
    'L2U01-C04': dict(
        base=dict(lo=530, g=12),
        tpl=dict(vars=dict(lo=[510, 520, 530, 540, 550, 560, 570], g=[8, 10, 12, 14, 16]),
                 q='Count the odd numbers between {lo} and {hi}.', derive=dict(hi='lo+g', f='lo+1'), answer='g/2',
                 hint='Write the first odd number after {lo}. Then count on in 2s.',
                 steps=['The first odd number after {lo} is {f}.', 'Count on in 2s until you reach the number before {hi}.', 'There are {ans} odd numbers.']),
        oracle=lambda e: _odd_between(e['lo'], e['lo'] + e['g'])),
}
