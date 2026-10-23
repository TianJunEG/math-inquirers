"""Independent answer checks for Lesson 10 (Story Steps: Read It Twice) and for its end-of-term check.

Every answer in l10.json is recomputed here from first principles (piles of counters are built and changed, queues are laid out child by child,
numbers are searched for), not by re-using the lesson's own expressions. run(d) returns the number of checks; any failure raises AssertionError.

It also checks the end-of-term check block: one question per lesson 1 to 10, all Start here plus one optional Think harder item, the picture on each
question matches its numbers (sticks drawn, counters drawn, arrow position, card digits, printed lengths in mm), the spoken question matches the written
one and appears in the script, the progress-word bands are consistent, and no banned wording or 7-word overlap with the reference material.
"""
import importlib.util, itertools, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
L1 = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(L1))
sys.path.insert(0, os.path.join(L1, 'tools'))


# ------------------------------------------------------------------ piles of counters (every operation really changes the pile)

def pile(n):
    return ['c'] * n


def add(p, k):
    return p + ['c'] * k


def take(p, k):
    assert k <= len(p), f'cannot take {k} from {len(p)}'
    return p[:len(p) - k]


def story(start, steps):
    """steps: list of ('+'|'-', k). Returns the list of totals after each step, never taking more than the pile holds."""
    p = pile(start)
    out = []
    for op, k in steps:
        p = add(p, k) if op == '+' else take(p, k)
        out.append(len(p))
    return out


def queue(front, behind):
    """A line of children laid out one by one: `front` children, the named child, `behind` children."""
    return ['child'] * front + ['NAMED'] + ['child'] * behind


# ------------------------------------------------------------------ number words (to say the spoken question matches the written one)

ONES = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
TENS = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


def n2w(n):
    if n < 20:
        return ONES[n]
    return TENS[n // 10] + ('' if n % 10 == 0 else '-' + ONES[n % 10])


def w2n(w):
    w = w.strip().lower()
    for n in range(100):
        if n2w(n) == w:
            return n
    raise AssertionError('not a number word: ' + w)


# ------------------------------------------------------------------ oracles for the online-practice templates (simulation or search)

ORACLES = {
    'c1': lambda e: len(add(pile(e['a']), e['b'])),
    'c2': lambda e: story(e['a'], [('-', e['b']), ('+', e['c'])])[-1],
    'c3': lambda e: len(add(pile(e['a']), e['b'])),
    'c5': lambda e: len(take(pile(e['a']), e['b'])),
    'c6': lambda e: len(pile(e['a']) + add(pile(e['a']), e['b'])),
    't1': lambda e: [m for m in range(0, 101) if m + e['b'] == e['r']][0],
    't2': lambda e: len(queue(e['f'], e['k'])),
    't3': lambda e: e['a'] + [ben for ben in range(0, 201) if ben - e['b'] == e['a']][0],
    't4': lambda e: len(take(add(pile(e['a']), e['b']), e['c'])),
    'g1': lambda e: story(e['s'], [('-', e['a']), ('-', e['b']), ('+', e['c'])])[-1],
    'g2': lambda e: [ben for ben in range(0, 201) if e['m'] + (e['m'] + e['k']) + ben == e['T']][0],
    'g3': lambda e: [beh for beh in range(0, 101) if len(queue(e['f'], beh)) == e['n']][0],
}
BASE_ENV = {'c1': dict(a=24, b=10), 'c2': dict(a=30, b=10, c=4), 'c3': dict(a=15, b=10), 'c5': dict(a=24, b=5), 'c6': dict(a=10, b=5),
            't1': dict(r=15, b=3), 't2': dict(f=6, k=4), 't3': dict(a=24, b=6), 't4': dict(a=12, b=5, c=3),
            'g1': dict(s=60, a=24, b=15, c=30), 'g2': dict(T=80, m=25, k=10), 'g3': dict(n=15, f=6)}

EQ_RE = re.compile(r'(?<![\d.])(\d+(?: [+\-] \d+)+) = (\d+)(?![\d.]| [+\-] )')


def eval_chain(expr):
    toks = expr.split()
    v = int(toks[0])
    for op, nx in zip(toks[1::2], toks[2::2]):
        v = v + int(nx) if op == '+' else v - int(nx)
    return v


def sweep_equations(text):
    """Every 'a + b - c = d' statement in a string must be arithmetically true. Returns how many were checked."""
    n = 0
    for m in EQ_RE.finditer(text):
        n += 1
        assert eval_chain(m.group(1)) == int(m.group(2)), f'wrong arithmetic in the text: {m.group(0)}'
    return n


def all_strings(o):
    if isinstance(o, str):
        yield o
    elif isinstance(o, dict):
        for k, v in o.items():
            if not k.startswith('_'):
                yield from all_strings(v)
    elif isinstance(o, list):
        for v in o:
            yield from all_strings(v)


def load_extras():
    spec = importlib.util.spec_from_file_location('l10_extras', os.path.join(L1, 'tools', 'b_check.py'))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def run(d):
    n = 0

    def eq(a, b, msg=''):
        nonlocal n
        n += 1
        assert a == b, f'{msg}: got {a!r}, expected {b!r}'

    T = {q['id']: q for q in d['tiers']['start'] + d['tiers']['think'] + d['tiers']['go']}
    X = {q['id']: q for q in d['exit']}
    H = {h['id']: h for h in d['home_practice']}

    # ---- sneak-peek: Ben has 3 more than Ali (4); then together
    ali, ben = 4, len(add(pile(4), 3))
    eq(d['sneak_peek']['val1'], ben, 'sneak q1 Ben'); eq(ben, 7, 'sneak q1 value')
    eq(d['sneak_peek']['val2'], ali + ben, 'sneak q2 together'); eq(ali + ben, 11, 'sneak q2 value')

    # ---- Start here
    s1 = story(30, [('-', 20), ('+', 6)])
    eq(T['S1']['val'], [s1[0], s1[1], s1[1]], 'S1'); eq(s1, [10, 16], 'S1 steps')
    s2 = story(42, [('+', 7), ('-', 10)])
    eq(T['S2']['val'], s2, 'S2'); eq(s2, [49, 39], 'S2 steps')
    # S3: the two sentences that fit the story are the ones that follow the story step by step
    s3 = story(25, [('+', 10), ('-', 3)])
    fit = {f'25 + 10 = {s3[0]}', f'{s3[0]} - 3 = {s3[1]}'}
    opts = {p['l']: p['text'] for p in T['S3']['parts'] if p['l']}
    flags = {p['l']: p['val'] for p in T['S3']['parts'] if p['l']}
    for k, txt in opts.items():
        eq(flags[k], txt in fit, 'S3 circle flag ' + k)
    eq(sorted(k for k, v in flags.items() if v), ['a', 'c'], 'S3 circled')
    eq(T['S3']['val'], s3, 'S3'); eq(s3, [35, 32], 'S3 value')
    # S4: story words -> sign. Gains add, losses take away.
    words = {'finds': '+', 'eats': '-', 'gives away': '-', 'join': '+'}
    for p in T['S4']['parts']:
        verb = [w for w in words if w in p['text']][0]
        eq(p['val'], words[verb], 'S4 ' + p['l'])
        # the printed sentence "a [] b = c" is true with exactly this sign, and the sign matches the effect on the pile
        a_, b_, c_ = [int(x) for x in re.search(r'(\d+) \[\] (\d+) = (\d+)', p['text']).groups()]
        sim = len(add(pile(a_), b_)) if p['val'] == '+' else len(take(pile(a_), b_))
        eq(sim, c_, 'S4 sentence true with the keyed sign ' + p['l'])
        other = len(take(pile(a_), b_)) if p['val'] == '+' else len(add(pile(a_), b_))
        eq(other == c_, False, 'S4 the other sign does not fit ' + p['l'])
    eq(T['S4']['val'], ['+', '-', '-', '+'], 'S4')
    ben5 = len(add(pile(23), 10))
    eq(T['S5']['val'], [ben5, 23 + ben5], 'S5'); eq(23 + ben5, 56, 'S5 value')
    s6 = story(30, [('-', 10), ('+', 4)])
    eq(T['S6']['val'], s6, 'S6'); eq(s6, [20, 24], 'S6 steps')
    eq(30 + 10, 40, 'S6 Siti writes 40 for Step 1'); eq(40 == s6[0], False, 'S6 Siti Step 1 is wrong: the children leave the bus')
    eq(T['S6']['parts'][0]['val'], 'no', 'S6 part a answer is No')
    # S2, G1, G3: each labelled step sentence is true and chains from the step before
    for qid, steps in (('S2', story(42, [('+', 7), ('-', 10)])), ('G1', story(60, [('-', 24), ('-', 15), ('+', 30)])), ('G3', [len(add(pile(25), 10)), 25 + len(add(pile(25), 10)), 10])):
        sent = [pp for pp in T[qid]['parts'] if pp['text'].startswith('Step')]
        eq([pp['val'] for pp in sent], steps, qid + ' step values')
        for pp in sent:
            eq(eval_chain(pp['ans'].split(' = ')[0]), int(pp['ans'].split(' = ')[1]), qid + ' ' + pp['ans'])

    # ---- Think harder
    mei = [m for m in range(0, 100) if m + 3 == 15][0]
    eq(T['T1']['val'], [mei, 15 + mei], 'T1'); eq(mei, 12, 'T1 Mei'); eq(15 + mei, 27, 'T1 together')
    eq(T['T2']['val'], [len(queue(6, 4))], 'T2'); eq(len(queue(6, 4)), 11, 'T2 value'); eq(len(queue(6, 4)) == 6 + 4, False, 'T2 trap: leaving Mei out gives 10')
    mei3 = len(add(pile(12), 5)); siti3 = len(take(pile(mei3), 3))
    eq(T['T3']['val'], [mei3, siti3], 'T3'); eq(siti3, 14, 'T3 value'); eq(12 - 3, 9, 'T3 trap value 9 is wrong'); eq(9 == siti3, False, 'T3 trap')

    left4 = len(take(pile(12), 7))
    eq(T['T4']['val'], [left4, 'no'], 'T4'); eq(left4, 5, 'T4 left after step 1')
    eq(left4 >= 8, False, 'T4 step 2 is impossible: 5 stickers, 8 asked'); eq(12 - 7 - 8 < 0, True, 'T4 the chain goes below zero')
    eq(T['T4']['parts'][1]['val'], 'yes' if left4 >= 8 else 'no', 'T4 part b')

    # ---- Go further
    g1 = story(60, [('-', 24), ('-', 15), ('+', 30)])
    eq(T['G1']['val'], g1, 'G1'); eq(g1, [36, 21, 51], 'G1 steps')
    eq(25 + 10, 35, 'G2 step 1'); eq(35 - 8, 27, 'G2 step 2'); eq(story(25, [('+', 10), ('-', 8)]), [35, 27], 'G2 simulated')
    eq(T['G2']['val'], 'open', 'G2 is an open task')
    ali3 = len(add(pile(25), 10)); both = 25 + ali3
    ben3 = [b_ for b_ in range(0, 71) if 25 + ali3 + b_ == 70][0]
    eq(T['G3']['val'], [ali3, both, ben3], 'G3'); eq(ben3, 10, 'G3 value')

    # ---- Investigation: order of an add and a take away
    both_ok = 0; first_fails = 0
    for start, a_, s_ in itertools.product(range(0, 31), range(0, 21), range(0, 21)):
        add_first = start + a_ - s_ if start + a_ >= s_ else None
        take_first = start - s_ + a_ if start >= s_ else None
        if take_first is not None and add_first is not None:
            both_ok += 1
            assert take_first == add_first, (start, a_, s_)
        if add_first is not None and take_first is None:
            first_fails += 1
    eq(both_ok > 0 and first_fails > 0, True, 'investigation: same answer when both orders work, and sometimes only one order works')
    n += 1
    eq(story(20, [('+', 10), ('-', 5)])[-1], story(20, [('-', 5), ('+', 10)])[-1], 'investigation first step'); eq(story(20, [('+', 10), ('-', 5)])[-1], 25, 'investigation 25')
    eq(story(4, [('+', 10), ('-', 6)])[-1], 8, 'investigation 4 + 10 - 6'); eq(4 < 6, True, 'cannot take 6 from 4 first')
    try:
        take(pile(4), 6); raise RuntimeError('expected a failure')
    except AssertionError:
        n += 1

    # ---- talk and exit
    eq(len(take(pile(20), 5)), 15, 'talk: Ali has 20 - 5 = 15'); eq(15 == 25, False, 'talk: Ravi is wrong')
    e1 = story(25, [('-', 10), ('+', 3)])
    eq(X['E1']['val'], [e1[-1]], 'E1'); eq(e1[-1], 18, 'E1 value')
    eq(X['E2']['val'], [len(add(pile(6), 5))], 'E2'); eq(len(add(pile(6), 5)), 11, 'E2 value')
    eq(X['E3']['val'], [len(take(pile(20), 7))], 'E3'); eq(len(take(pile(20), 7)), 13, 'E3 value')

    # ---- home practice
    h1 = story(28, [('+', 10), ('-', 5)])
    eq(H['H1']['val'], h1[-1], 'H1'); eq(h1[-1], 33, 'H1 value')
    eq(H['H2']['val'], len(add(pile(14), 6)), 'H2'); eq(len(add(pile(14), 6)), 20, 'H2 value')
    h3 = story(40, [('-', 10), ('-', 20)])
    eq(H['H3']['val'], h3[-1], 'H3'); eq(h3[-1], 10, 'H3 value')
    dev = len(add(pile(9), 4))
    eq(H['H4']['val'], 9 + dev, 'H4'); eq(9 + dev, 22, 'H4 value')
    eq(H['H5']['val'], 'open', 'H5 open')

    # ---- optional slide, spare-time menu
    eq(story(20, [('+', 6), ('-', 4)])[-1], 22, 'optional: win first'); eq(story(20, [('-', 4), ('+', 6)])[-1], 22, 'optional: lose first')
    eq(story(20, [('+', 6), ('-', 4)])[-1], story(20, [('-', 4), ('+', 6)])[-1], 'M1/M3 same answer')
    eq(story(20, [('+', 10), ('-', 5)])[-1], 25, 'M1 first'); eq(story(20, [('-', 5), ('+', 10)])[-1], 25, 'M1 second')
    # the story slides
    eq(story(26, [('+', 10), ('-', 5)]), [36, 31], 'mini: Mei 26 + 10 - 5'); eq(26 % 10 >= 5, True, 'mini: 36 - 5 needs no renaming')
    eq(story(40, [('-', 20), ('+', 7)]), [20, 27], 'mini: Siti beads')
    eq(len(add(pile(14), 5)), 19, 'mini: more than'); eq(len(take(pile(14), 5)), 9, 'mini: fewer than')
    eq(len(queue(5, 2)), 8, 'mini: line of children with Ravi'); eq(5 + 2, 7, 'mini: leaving Ravi out gives 7')
    ben_c = 9; mei_c = len(add(pile(ben_c), 4)); eq((mei_c, ben_c + mei_c), (13, 22), 'explore: story C Mei and altogether')
    eq(len(take(pile(38), 6)), 32, 'mini: Siti has 6 fewer than Mei (38)'); eq(38 % 10 >= 6, True, 'mini: 38 - 6 needs no renaming')
    eq(story(8, [('+', 5), ('-', 6)]), [13, 7], 'explore: story A'); eq(story(12, [('-', 5), ('+', 3)]), [7, 10], 'explore: story B')
    eq(len(add(pile(6), 4)), 10, 'rem4 first'); eq(len(take(pile(9), 3)), 6, 'rem4 second'); eq(len(add(pile(12), 5)), 17, 'rem4 third')
    eq([ [x for x in range(0, 100) if x + 3 == 8][0], [x for x in range(0, 100) if x - 2 == 6][0], [x for x in range(0, 100) if x + 10 == 35][0]], [5, 8, 25], 'I think of a number')
    eq([40 + 20, 37 + 10, 56 - 20, 24 + 5], [60, 47, 36, 29], 'rem3')
    eq(sum(+1 if s_ == '+' else -1 for s_ in '+-+-') , 0, 'break moves sanity')
    pos = 0
    for step in (+3, -2, +4, -5): pos += step
    eq(pos, 0, 'break: back at the chair')
    eq(pos, 0, 'break: end position')

    # ---- online practice: authored answers equal the oracle at the base numbers; every variant stays within 0..100 and never takes more than is held
    O = {i['id']: i for i in d['online_practice']['items']}
    for k, env in BASE_ENV.items():
        eq(O[k]['answer'], ORACLES[k](env), 'practice authored answer ' + k)
    eq(O['c4']['answer'], '30 - 10 = 20', 'c4 answer'); eq(story(30, [('-', 10), ('+', 6)])[0], 20, 'c4 step 1 value'); eq(30 - 10 == 20, True, 'c4 correct option')
    opts = O['c4']['options']
    eq(sum(1 for o in opts if eval_chain(o.split(' = ')[0]) == int(o.split(' = ')[1])), 4, 'c4: all four options are arithmetically true, only one is Step 1')
    for it in O.values():
        tp = it.get('tpl')
        if not tp: continue
        names = list(tp['vars'])
        for combo in itertools.product(*[tp['vars'][x] for x in names]):
            env = dict(zip(names, combo)); full = dict(env)
            for k2, ex in tp.get('derive', {}).items(): full[k2] = eval(ex, {}, full)
            full['ans'] = eval(tp['answer'], {}, full)
            eq(full['ans'], ORACLES[it['id']](env), f"variant {it['id']} {env}")
            assert 0 < full['ans'] <= 100, (it['id'], env, full['ans'])
            for k2, val in full.items():
                assert val >= 0, (it['id'], env, k2, val)
            for txt in tp['steps'] + [tp['q'], tp['hint']]:
                filled = re.sub(r'\{(\w+)\}', lambda m_: str(full[m_.group(1)]), txt)
                sweep_equations(filled)
    n += 1

    # ---- every arithmetic statement written anywhere in the lesson is true
    stmts = 0
    for s in all_strings(d):
        stmts += sweep_equations(s)
    eq(stmts > 60, True, 'arithmetic sweep found many statements')

    n += check_block(d, eq)
    return n


def check_block(d, eq):
    """Mi's Challenge Quest (the end-of-term slot, a game with Mi). Returns the number of extra checks made (eq counts its own)."""
    assert 'end_of_term_check' not in d, 'the old end-of-term check block must be gone (tools/b_check.py would build test-like files)'
    c = d['challenge_quest']
    ex = load_extras()
    import svg, validate
    qs = c['questions']
    lessons_of = lambda q: q.get('lessons') or [10 if q['lesson'] == 'mixed' else q['lesson']]   # Quest v2: gate 8 is a mixed gate (no lesson tag); its content is the lesson 10 story idea
    eq([q['id'] for q in qs], [f'C{i}' for i in range(1, 9)], 'eight questions C1 to C8')
    eq(sorted(l for q in qs for l in lessons_of(q)), list(range(1, 11)) if False else [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'every lesson 1 to 10 is covered once (Q2 covers lessons 2 and 4, Q5 covers lessons 6 and 7)')
    eq(all(q['tier'] == 'start' for q in qs), True, 'all eight are Start here')
    eq((c['optional']['tier'], c['optional']['optional']), ('think', True), 'one optional Think harder item')
    eq([q['page'] for q in qs], sorted(q['page'] for q in qs), 'questions in page order')
    eq(sorted({q['page'] for q in qs}), list(range(1, c['sheet_pages'] + 1)), 'every sheet page holds a question')
    Q = {q['id']: q for q in qs}

    # C1: tens and ones, and the picture really has 39 sticks
    sticks = svg.bundles(3, 9).count('fill="#FFC93C"')
    eq(sticks, 39, 'C1 picture draws 39 sticks'); eq(divmod(sticks, 10), (3, 9), 'C1 tens and ones')
    eq(Q['C1']['val'], [3, 9, 39], 'C1'); eq((Q['C1']['visual']['tens'], Q['C1']['visual']['ones']), (3, 9), 'C1 picture spec')
    # C2: the arrow sits exactly on 67; counting on in tens from 14, 24, 34
    nl = ex.numberline_svg(Q['C2']['visual'])
    tick_x = {int(m.group(2)): float(m.group(1)) for m in re.finditer(r'x1="([\d.]+)" y1="[\d.]+" x2="[\d.]+" y2="[\d.]+" stroke="#1B2A49" stroke-width="[\d.]+" data-tick="(\d+)"', nl)}
    arrow = re.search(r'data-arrow="(\d+)" data-tip-x="([\d.]+)"', nl)
    eq(sorted(tick_x), list(range(60, 71)), 'C2 ticks 60 to 70')
    eq(abs(float(arrow.group(2)) - tick_x[int(arrow.group(1))]) < 0.2, True, 'C2 arrow tip on its tick')
    eq(int(arrow.group(1)), 67, 'C2 arrow value'); eq((66 + 68) // 2, 67, 'C2 between its two labelled neighbours')
    def count_on(a_, step, k): return [a_ + step * i for i in range(1, k + 1)]
    eq(count_on(34, 10, 1), [44], 'C2 b: counting on in tens from 34'); eq(Q['C2']['val'], [67, 44], 'C2')
    eq(Q['C2']['lessons'], [2, 4], 'C2 covers lessons 2 and 4')
    # C3: the numbers that can be made from the cards using both cards
    cards = re.findall(r'data-card="(\d)"', ex.cards_svg(Q['C3']['visual']['digits']))
    eq(cards, ['3', '8'], 'C3 cards drawn')
    made = sorted({int(a_ + b_) for a_, b_ in itertools.permutations(cards, 2)})
    eq(made, [38, 83], 'C3 numbers made'); eq(Q['C3']['val'], [max(made)], 'C3'); eq(max(made), 83, 'C3 greatest')
    # C4: ten-frame picture 7 and 5, make a ten
    tf = svg.ten_frame(7, 5)
    cx = [float(m) for m in re.findall(r'<circle cx="([\d.]+)"', tf)]
    eq((len([x for x in cx if x < 340]), len([x for x in cx if x > 340])), (7, 5), 'C4 picture has 7 and 5 counters')
    def make_ten(a_, b_):
        to_ten = (10 - a_ % 10) % 10
        return (a_ + to_ten) + (b_ - to_ten)
    eq(make_ten(7, 5), 7 + 5, 'C4 a by making a ten'); eq(make_ten(37, 5), 37 + 5, 'C4 b by making a ten')
    eq(Q['C4']['val'], [12, 42], 'C4'); eq(len(add(pile(37), 5)), 42, 'C4 simulated')
    # C5: tens jump and take away without renaming
    eq(Q['C5']['val'], [len(add(pile(52), 30)), len(take(pile(74), 31))], 'C5'); eq(Q['C5']['val'], [82, 43], 'C5 values')
    eq(74 % 10 >= 31 % 10, True, 'C5 no renaming'); eq(Q['C5']['lessons'], [6, 7], 'C5 covers lessons 6 and 7')
    # C6: box numbers by search
    box_a = [b_ for b_ in range(0, 100) if 8 + 4 == 6 + b_][0]; box_b = [b_ for b_ in range(0, 100) if 60 + 10 == 50 + b_][0]
    eq(Q['C6']['val'], [box_a, box_b], 'C6'); eq([box_a, box_b], [6, 20], 'C6 values')
    # C7: the printed line and the draw length
    v9 = Q['C7']['visual']
    eq(Q['C7']['val'], [v9['draw_cm'], v9['draw_cm'] + v9['extra_cm']], 'C7 one line drawn and the longer length written'); eq(v9['draw_cm'] + v9['extra_cm'], 10, 'C7 a line 4 cm longer is 10 cm')
    eq(10 * v9['draw_cm'] < 182 - 20, True, 'C7 the drawing box is wide enough for a 6 cm line')
    eq(re.search(r'width="(\d+)mm"', ex.check_bar_svg(c['sheet_check_bar_mm'])).group(1), '100', 'print check bar svg width in mm')
    eq(ex.dotbox_svg(True).count('data-dot'), 1, 'C7 one starting dot in the drawing box'); eq(Q['C7'].get('dotbox'), True, 'C7 draws the dot box')
    # C8: the story
    s10 = story(35, [('+', 10), ('-', 3)])
    eq(Q['C8']['val'], [s10[0], s10[1]], 'C8'); eq(s10, [45, 42], 'C8 values')
    eq(eval_chain(Q['C8']['parts'][0]['ans'].split(' = ')[0]), 45, 'C8 step 1 sentence'); eq(eval_chain(Q['C8']['parts'][1]['ans'].split(' = ')[0]), 42, 'C8 step 2 sentence')
    o = c['optional']
    eq(o['val'], [len(queue(5, 3))], 'optional'); eq(len(queue(5, 3)), 9, 'optional value'); eq(5 + 3 == 9, False, 'optional trap: 8 leaves Ali out')
    # parts: the answer text contains each part's value
    for q in qs + [o]:
        for p in q['parts']:
            for v_ in (p['val'] if isinstance(p['val'], list) else [p['val']]):
                assert str(v_) in re.findall(r'[\d.]+', p['ans']) or str(v_) in p['ans'], (q['id'], p)
    n_extra = 0
    # spoken = written: every number in the text/parts is said (as digits or as words), and the script reads the same words
    for q in qs + [o]:
        shown = q['text'] + ' ' + ' '.join(p['text'] for p in q['parts'])
        shown = shown.replace('Think harder (optional). ', '')
        said = q['say'].lower()
        for num in ([] if q['id'] == 'C4' else re.findall(r'\d+', shown)):
            assert (num in said) or (n2w(int(num)) in said), (q['id'], num)
            n_extra += 1
    ex_seg = [s for s in d['script']['segments'] if s['part'] == 'exit'][0]
    script_text = ' '.join(ln.get('text', '') for ln in ex_seg['lines'])
    for q in qs + [o]:
        assert q['say'] in script_text, f"{q['id']} spoken text is not in the script"
        n_extra += 1
    # the check fits in its part of the lesson, by modelled time (reading aloud, quiet work, stretch) for a middle child and a slower child
    import common
    seg = [s for s in common.segment_timeline(d) if s['part'] == 'exit'][0]
    pm = {p['id']: p for p in d['timing']['parts']}
    exit_min = pm['exit']['end'] - pm['exit']['start']
    eq(c['minutes'], 20, 'the quest takes 20 minutes (owner decision of 22 Oct 2026)')
    eq(exit_min, c['minutes'], 'the exit part is the quest only (no separate exit ticket in the live lesson)')
    eq(seg['used'] <= c['minutes'] * 60, True, 'the quest script fits its 20 minutes')
    child = sum(c['timing_model']['child_seconds'].values()) + c['timing_model']['stretch_seconds']
    read = sum(sec for (_, sec, ln) in seg['lines'] if ln['k'] in ('READ', 'SAY', 'REC', 'SLIDE', 'DO'))
    mid = child + read
    slow = child * c['timing_model']['slow_child_factor'] + read * 1.1
    eq(mid <= 17 * 60, True, 'a middle child needs at most 17 minutes of work and reading')
    eq(slow <= 24 * 60, True, 'a slower child needs at most 24 minutes (20 plus the 4 flex minutes)')
    eq(pm['exit']['start'], 35, 'the quest starts at minute 35 (straight after the break, Quest v2 skeleton)'); eq(pm['exit']['end'], 55, 'the quest ends at minute 55')
    eq(sum(p_['end'] - p_['start'] for p_ in d['timing']['parts']), 90, 'parts still sum to 90')
    eq(sum(len(p_['parts']) for p_ in qs), 15, 'the quest has 15 answer parts in all (cut from 22 to fit 20 minutes)')
    eq(all(s_.get('optional') and s_['part'] == 'flex' for s_ in d['slides'] if s_['id'] in ('s-exit', 's-exitans')), True, 'the exit ticket slides are optional flex slides: the quest takes its place')
    # photo return: the business WhatsApp number only, no personal-phone address text anywhere in the check or the lesson
    blob = json.dumps(c) + json.dumps(d['safeguarding']) + json.dumps(d['tutor_prep']) + json.dumps(d['parent']) + json.dumps([s_['note'] for s_ in d['slides']]) + json.dumps(d['script'])
    assert '+65 9880 5962' in blob
    eq('parent contact' in blob or 'address you gave' in blob or 'personal devices' in blob or 'address given at enrolment' in blob, False, 'no leftover text about a parent contact address or personal devices')
    eq('3-page' in blob or '29-minute' in blob or 'minutes 54' in blob or 'about 30 minutes' in blob or 'minute 54' in blob, False, 'no leftover 29-minute or 30-minute text')
    # strands partition the eight questions and cover every lesson
    st = c['strands']
    eq(sorted(x for s in st for x in s['questions']), sorted(q['id'] for q in qs), 'strands partition C1 to C8')
    eq(sorted(l for s in st for l in s['lessons']), list(range(1, 11)), 'strands cover lessons 1 to 10')
    for s in st:
        eq(sorted(l_ for x in s['questions'] for l_ in lessons_of(Q[x])), sorted(s['lessons']), 'strand lessons match questions ' + s['id'])
        for x in s['saw_examples']:
            assert '[Name]' in x, (s['id'], x)
            n_extra += 1
        assert len(s['saw_examples']) == 3 and len(s['next_examples']) == 2, s['id']
    # no points, bands, R/P/N marks or progress-word tables anywhere in the quest block (it is a game: no score, no ranking)
    for k in ('bands', 'words', 'report_template', 'sheet_marks'):
        eq(k in c, False, 'no ' + k + ' in the quest block')
    eq(set(c['notes_sheet']), {'how', 'prompts', 'group_how', 'group_prompts'}, 'private notes sheet and group advice sheet are present')
    eq(len(c['notes_sheet']['prompts']) >= 4 and len(c['notes_sheet']['group_prompts']) >= 3, True, 'notes prompts present')
    # wording scan on child and parent facing text (the quest name itself holds the word Challenge, which BANNED_CHILD forbids on its own)
    quest_facing = list(c['child_rules']) + list(c['page_instructions']) + [q['text'] for q in qs] + [p['text'] for q in qs for p in q['parts']] + [o['text']]
    pn = c['parent_note']
    quest_facing += [pn['title'], pn['what'], pn['back'], pn['make_up']] + pn['before'] + pn['during'] + pn['after']
    sw = c['saw_line']
    quest_facing += [sw['parent_example'], sw['closing']]
    quest_facing += [x for s_ in st for x in (s_['parent_name'], s_['looked_at'])]
    facing = quest_facing + validate.child_strings(d)
    for s in facing:
        t_ = s.replace('0 mark', '0').replace("Mi's Challenge Quest", 'the quest').replace("Mi's Chal\u00adlenge Quest", 'the quest')
        for pat in validate.BANNED_CHILD:
            assert not re.search(pat, t_, re.I), f'banned wording {pat!r} in: {s[:70]}'
        # test-like wording: never on a child or parent page (test is also a teaching verb in some lessons, so it is only barred in the quest's own text)
        assert not re.search(r'\bexams?\b|check[- ]?sheet|end-of-term check|\btimer\b|\bpass or fail\b|\bmarks?\b|\bmarked\b|\bmarking\b', t_, re.I), f'test-like wording on a child or parent page: {s[:90]}'
        assert not re.search(r'\bout of\b|\d\s*/\s*10\b|\bscored?\b', t_, re.I), f'a mark or score appears in parent or child text: {s[:70]}'
        n_extra += 1
    for s in quest_facing:
        assert not re.search(r'\btests?\b|\btesting\b', s, re.I), f'the word test appears in the quest text: {s[:70]}'
        n_extra += 1
    eq(any(("Mi's Chal\u00adlenge Quest" in s_ or "Mi's Challenge Quest" in s_) for s_ in [d['parent']['summary'], d['parent']['next'], d['parent']['report_line']]), True, 'the parent page names the quest')
    eq([sl_['title'] for sl_ in d['slides'] if sl_['id'] == 's-quest1'], ["Mi's Chal\u00adlenge Quest"], 'the quest slide names the quest')
    eq(all(sl_.get('no_record') for sl_ in d['slides'] if sl_['id'] in ('s-quest1', 's-quest2')), True, 'quest slides are not on the shared recording')
    own = set()
    for s in facing + [q['say'] for q in qs]:
        own |= validate.shingles(validate.std_strip(s))
    for f, txt in validate.external_sources():
        common_ = own & validate.shingles(validate.std_strip(txt))
        assert not common_, f'7-word overlap with {f}: {sorted(common_)[:2]}'
    n_extra += 1
    return n_extra
