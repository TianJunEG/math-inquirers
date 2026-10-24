"""Independent checks for Level 6 Unit 8 (Secret codes).  Clocks and calendars are walked one step at a time, letters are moved along the alphabet one place at a
time (wrapping by hand), the printed code is run by the l6_lib interpreter and the tables are read from the unit file."""
from common import load_unit
from l6_lib import run, s

CHECKS = {}
U = load_unit(6, 8)
ITEM = {i['id']: i for i in U['items']}
ALPHA = [chr(65 + k) for k in range(26)]
DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


def prog_of(id_):
    return ITEM[id_]['figure']['prog']


def step_letter(ch, k):
    """move a letter k places along the alphabet (k may be negative), wrapping round after Z and before A"""
    i = ALPHA.index(ch)
    for _ in range(abs(k)):
        i += 1 if k > 0 else -1
        if i == 26:
            i = 0
        if i == -1:
            i = 25
    return ALPHA[i]


def code(word, shift):
    return ''.join(step_letter(c, shift) for c in word)


def decode(word, shift):
    return ''.join(step_letter(c, -shift) for c in word)


def clock(h, k, size=12, first=1):
    """hour h on a clock whose hours run first .. first+size-1; move k hours (negative = back) one at a time"""
    for _ in range(abs(k)):
        h += 1 if k > 0 else -1
        if h > first + size - 1:
            h = first
        if h < first:
            h = first + size - 1
    return h


def remainder(n, m):
    while n >= m:
        n -= m
    return n


def day(name, k):
    i = DAYS.index(name)
    for _ in range(abs(k)):
        i += 1 if k > 0 else -1
        if i == 7:
            i = 0
        if i == -1:
            i = 6
    return DAYS[i]


@check('L6U08-L01')
def _():
    return [code('JAB', 12)]


@check('L6U08-S01')
def _():
    assert ITEM['L6U08-S01']['figure']['hand'] == 8
    return {'a': [clock(8, 7)], 'b': [clock(5, -9)], 'c': [clock(7, 50)]}


@check('L6U08-S02')
def _():
    return {'a': [remainder(38, 7)], 'b': [remainder(100, 12)], 'c': [remainder(59, 26)], 'd': [remainder(500, 26)]}


@check('L6U08-S03')
def _():
    strip = ITEM['L6U08-S03']['figure']['rows'][0]
    assert strip[3] == 'Thu'
    return {'a': [day('Thursday', 40)], 'b': [day('Thursday', 100)], 'c': [day('Thursday', -20)]}


@check('L6U08-S04')
def _():
    return {'a': [code('HELP', 3)], 'b': [code('MAZE', 5)]}


@check('L6U08-S05')
def _():
    return {'a': [decode('FXAT', 9)], 'b': [decode('YNZC', 13)]}


@check('L6U08-S06')
def _():
    prog = prog_of('L6U08-S06')
    env, said = run(prog)
    out = said[0]
    prog17 = [['var', 'set letter to (17)']] + prog[1:]
    env17, said17 = run(prog17)
    return {'a': [out], 'b': [ALPHA[out]], 'c': [said17[0]]}


@check('L6U08-S07')
def _():
    shift = [k for k in range(0, 26) if code('THE', k) == 'AOL'][0]
    return {'a': [shift], 'b': [decode('XBPJR', shift)]}


@check('L6U08-S08')
def _():
    word = ''.join(ALPHA)
    one = [k for k in range(0, 26) if code(code(word, 15), 18) == code(word, k)][0]
    undo = [k for k in range(1, 26) if code(code(word, 7), k) == word][0]
    return {'a': [one], 'b': [undo], 'c': ['the same' if code(word, 26) == word else 'reversed']}


@check('L6U08-S09')
def _():
    return {'a': [clock(22, 7, 24, 0)], 'b': [clock(3, -5, 24, 0)], 'c': [clock(9, 100, 24, 0)]}


@check('L6U08-S10')
def _():
    env, said = run(prog_of('L6U08-S10'))
    return {'a': [said[3]], 'b': [said[4]], 'c': [ALPHA[said[2]]]}


@check('L6U08-S11')
def _():
    def visited(jump):
        h, seen = 12, {12}
        while True:
            h = clock(h, jump)
            if h == 12:
                return len(seen)
            seen.add(h)
    return {'a': [visited(7)], 'b': [visited(9)]}


@check('L6U08-T01')
def _():
    hits = [n for n in range(1, 200) if remainder(n, 5) == 3 and remainder(n, 7) == 4]
    return {'a': [hits[0]], 'b': [hits[1]]}


@check('L6U08-T02')
def _():
    days = 31 + 28 + 31            # 10 Jan to 10 Feb, to 10 Mar, to 10 Apr
    return {'a': [days], 'b': [remainder(days, 7)], 'c': [day('Tuesday', days)]}


@check('L6U08-T03')
def _():
    shift = [k for k in range(0, 26) if code('AT', k) == 'EX'][0]
    msg = ' '.join(decode(w, shift) for w in 'QIIX EX RSSR'.split())
    return {'a': [shift], 'b': [msg]}


def vigenere(word, keys, sign=1):
    return ''.join(step_letter(c, sign * keys[i % len(keys)]) for i, c in enumerate(word))


@check('L6U08-G01')
def _():
    keys = [1, 2, 3]
    same_letter_differs = len(set(vigenere('AAA', keys))) > 1
    return {'a': [vigenere('MATHS', keys)], 'b': [vigenere('DQGFU', keys, -1)],
            'c': ['the same letter is coded in different ways' if same_letter_differs else 'every letter moves the same amount']}


@check('L6U08-G02')
def _():
    prog = prog_of('L6U08-G02')
    env, said = run(prog)
    one = run([prog[0], ['ctl', 'repeat (1)', prog[1][2]], prog[2]])[1][0]
    return {'a': [one], 'b': [said[0]]}


@check('L6U08-G03')
def _():
    def check_digit(d3):
        return [d for d in range(10) if remainder(sum(d3) + d, 10) == 0][0]
    valid = remainder(5 + 3 + 6 + 9, 10) == 0
    return {'a': [check_digit([4, 7, 2])], 'b': [check_digit([9, 8, 1])], 'c': ['Yes' if valid else 'No']}


@check('L6U08-C01')
def _():
    return s([clock(9, 40)])


@check('L6U08-C02')
def _():
    return [code('NOW', 6)]


@check('L6U08-C03')
def _():
    return [decode('EVQ', 4)]


@check('L6U08-C04')
def _():
    return [day('Friday', 30)]
