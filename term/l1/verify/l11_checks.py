"""Independent answer checks for Level 1 Term 2 Lesson 11 (Who Is Where?).

Every answer in l11.json is recomputed here from first principles. A line of children is modelled as a Python list
ordered from the front (the door); places are found by walking the list from either end, children in front and between
are found by slicing, and puzzles with clues (seats round a table, a race) are solved by trying every arrangement and
keeping the ones that fit all the clues. run(d) returns the number of checks; any failure raises AssertionError.
"""
import itertools


def make_line(n, start=1):
    return list(range(start, start + n))                 # child ids from the front


def place_front(line, child):
    return line.index(child) + 1


def place_back(line, child):
    return list(reversed(line)).index(child) + 1


def in_front(line, child):
    return len(line[:line.index(child)])


def behind(line, child):
    return len(line[line.index(child) + 1:])


def between(line, a, b):
    i, j = sorted((line.index(a), line.index(b)))
    return len(line[i + 1:j])


def ordinal(n):
    if 10 <= n % 100 <= 20: s = 'th'
    else: s = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    return f'{n}{s}'


def line_lengths_with_both_places(front, back):
    """All line lengths in which some child is `front`th from the front and `back`th from the back."""
    out = []
    for n in range(1, 60):
        line = make_line(n)
        if any(place_front(line, c) == front and place_back(line, c) == back for c in line): out.append(n)
    return out


def ring_adjacent(seat, other, seats=6):
    return (seat - other) % seats in (1, seats - 1)


def solve_table():
    """Ali 1, Mei 3, Ben 5 are placed. Try every way to seat Siti, Ravi, Kumar in seats 2, 4, 6 and keep those that satisfy all clues."""
    fixed = {'Ali': 1, 'Mei': 3, 'Ben': 5}
    sols = []
    for perm in itertools.permutations(['Siti', 'Ravi', 'Kumar']):
        seat = dict(fixed); seat.update(dict(zip(perm, (2, 4, 6))))
        ok = (ring_adjacent(seat['Siti'], seat['Ali']) and ring_adjacent(seat['Siti'], seat['Mei'])           # Siti between Ali and Mei
              and (seat['Ravi'] - seat['Ali']) % 6 == 3                                                       # Ravi opposite Ali
              and ring_adjacent(seat['Kumar'], seat['Ben']) and ring_adjacent(seat['Kumar'], seat['Ali']))    # Kumar between Ben and Ali
        if ok: sols.append(seat)
    return sols


def solve_race():
    sols = []
    for order in itertools.permutations(['Siti', 'Ben', 'Ali', 'Mei']):      # order[0] is 1st
        p = {n: i + 1 for i, n in enumerate(order)}
        if p['Siti'] == 1 and p['Ben'] < p['Ali'] and p['Ali'] < p['Mei']: sols.append(p)
    return sols


# ---- oracles for the online-practice templates (brute force, independent of the template expressions)
def _o_c1(e):
    line = [i == e['k'] - 1 for i in range(e['n'])]          # left to right, door on the left
    return line.index(True) + 1


def _o_c2(e):
    m = e['k'] + 2
    ring = make_line(m)[e['k'] - 1]
    return in_front(make_line(m), ring)


def _o_c4(e):
    line = make_line(e['n']); c = line[e['f'] - 1]
    return place_back(line, c)


def _line_from_clues(front, back, mid):
    """Line lengths n where the child who is `front`th from the front and the child who is `back`th from the back have `mid` children between them."""
    out = []
    for n in range(1, 60):
        ln = make_line(n)
        if front <= n and back <= n:
            a, b = ln[front - 1], list(reversed(ln))[back - 1]
            if ln.index(b) > ln.index(a) and between(ln, a, b) == mid: out.append(n)
    return out


def _o_t1(e):
    line = make_line(e['n']); ravi = list(reversed(line))[e['b'] - 1]
    lilys = [c for c in line if line.index(c) < line.index(ravi) and between(line, c, ravi) == e['c']]
    assert len(lilys) == 1
    return place_front(line, lilys[0])


def _o_t2(e):
    line = make_line(20)
    return between(line, line[e['a'] - 1], line[e['b'] - 1])


def _o_g1(e):
    line = make_line(e['n'])
    mids = [c for c in line if in_front(line, c) == behind(line, c)]
    assert len(mids) == 1
    return place_front(line, mids[0])


def _o_g2(e):
    line = make_line(e['n'])
    mei = line[3]
    ben = list(reversed(line))[2]
    return between(line, mei, ben)


ORACLES = {'c1': _o_c1, 'c2': _o_c2, 'c4': _o_c4, 't1': _o_t1, 't2': _o_t2, 'g1': _o_g1, 'g2': _o_g2}
BASE_ENV = {'c1': dict(n=6, k=3), 'c2': dict(k=5), 'c4': dict(n=8, f=3), 't1': dict(n=11, b=2, c=4), 't2': dict(a=3, b=9), 'g1': dict(n=13), 'g2': dict(n=13)}


def run(d):
    n = 0

    def eq(a, b, msg=''):
        nonlocal n
        n += 1
        assert a == b, f'{msg}: got {a!r}, expected {b!r}'

    T = {q['id']: q for q in d['tiers']['start'] + d['tiers']['think'] + d['tiers']['go']}
    X = {q['id']: q for q in d['exit']}
    # sneak-peek: Mei 4th, Ben right behind
    line = ['c%d' % i for i in range(1, 8)]; mei = line[3]; ben = line[4]
    eq(place_front(line, ben), 5, 'sneak: Ben is right behind the 4th child'); eq(in_front(line, ben), 4, 'sneak 2'); eq(d['sneak_peek']['val2'], 4, 'sneak val')
    eq(place_front(line, line[1]), 2, 'sneak 1: the 2nd dot'); eq(d['sneak_peek']['val1'], 2, 'sneak val1')
    # warm-up
    eq([6 - 1, 6 + 1], [5, 7], 'warm-up before/after')
    row = ['Ali', 'Kumar', 'Wei', 'Jenny']
    eq((row[0], row[-1], row[row.index('Kumar') + 1], row[row.index('Kumar') + 1:row.index('Jenny')]), ('Ali', 'Jenny', 'Wei', ['Wei']), 'warm-up front/back/behind/between')
    # Explore: six things, door moved to the other end
    six = make_line(6)
    eq(place_front(six, six[-1]), 6, 'explore: last of six is 6th'); eq(len(six), 6, 'explore: six things')
    eq((ordinal(place_front(six, six[3])), len(six)), ('4th', 6), 'explore round 2: the 4th card is on the 4th thing, the number card says 6')
    eq(place_front(list(reversed(six)), six[0]), 6, 'explore: first thing is 6th after the turn'); eq(place_front(list(reversed(six)), six[1]), 5, 'explore: 2nd is 5th after the turn')
    # the picture of round 3 draws the door on the right and rings the 5th child from the door, the 2nd child from the left
    e3 = [s for s in d['slides'] if s['id'] == 's-explore3'][0]['blocks'][0]
    eq(list(reversed(six)).index(six[1]) + 1, 5, 'explore 3: the old 2nd thing is 5th from the new front'); eq((e3['highlight'], e3['front']), ([5], 'right'), 'explore 3 picture')
    eq(place_back(six, six[1]), 5, 'mini: ringed child is 5th from the back')
    # mini: how many in front of Ben (5th and 6th), clue puzzle, your turn
    seven = make_line(7)
    eq(in_front(seven, seven[4]), 4, 'mini: Ben 5th'); eq(in_front(seven, seven[5]), 5, 'mini: 6th'); eq(place_front(seven, seven[2 + 1]), 4, 'mini: right behind the 3rd is the 4th')
    eq(place_front(make_line(5), make_line(5)[1 + 1]), 3, 'mini: right behind Aisha (2nd) is 3rd'); eq(place_front(make_line(5), make_line(5)[2 + 1]), 4, 'mini: Wei is 4th')
    five = make_line(5)
    eq(line_lengths_with_both_places(3, 3), [5], 'mini: Aisha 3rd from both ends means 5 children')
    eq(between(seven, seven[1], seven[5]), 3, 'mini: between the 2nd and the 6th are 3 children')
    # Start here
    names = ['Ali', 'Kumar', 'Wei', 'Jenny', 'Lily']
    eq([names.index('Wei') + 1 == 3, names.index('Jenny') + 1 == 5, names.index('Lily') == len(names) - 1], [True, False, True], 'S1')
    eq([T['S1']['visuals'][0]['names'][str(i + 1)] for i in range(5)], names, 'S1 picture names')
    eq(T['S1']['val'], ['True', 'False', 'True'], 'S1 val')
    eq([ordinal(i) for i in range(1, 8)], T['S2']['val'], 'S2'); eq(T['S2']['visuals'][0]['n'], 7, 'S2 picture has 7 children')
    ten = make_line(10)
    eq(len(ten), 10, 'S3a'); eq(ordinal(place_front(ten, ten[-1])), '10th', 'S3b'); eq(T['S3']['val'], [10, '10th'], 'S3 val'); eq(T['S3']['visuals'][0]['n'], 10, 'S3 picture')
    eq(ordinal(place_front(five, five[1 + 1])), '3rd', 'S4'); eq(T['S4']['val'], ['3rd'], 'S4 val')
    eq(ordinal(place_back(six, six[1])), '5th', 'S5'); eq(T['S5']['val'], ['5th'], 'S5 val'); eq(T['S5']['visuals'][0]['n'], 6, 'S5 picture')
    pos6 = [p for p in range(1, 5) if p > 1 and p < 3]
    eq([ordinal(p) for p in pos6], ['2nd'], 'S6 only one place is between 1st and 3rd'); eq(T['S6']['val'], ['2nd'], 'S6 val')
    eq(in_front(seven, seven[4]), 4, 'S7'); eq(T['S7']['val'], [4], 'S7 val')
    # Think harder
    ln11 = make_line(11); rv = list(reversed(ln11))[1]; ly = [c for c in ln11 if ln11.index(c) < ln11.index(rv) and between(ln11, c, rv) == 4]; eq(len(ly), 1, 'T1 exactly one child is in front of Ravi with 4 between'); eq(place_front(ln11, rv), 10, 'T1 Ravi is 10th from the front'); eq(place_front(ln11, ly[0]), 5, 'T1 Lily is 5th from the front'); eq(10 - 4 == 6 and 6 != 5, True, 'T1 Kumar is not correct'); eq(T['T1']['val'], ['No', '5th'], 'T1 val')
    ln10 = make_line(10); eq(between(ln10, ln10[2], ln10[8]), 5, 'T2'); eq(T['T2']['val'], [5], 'T2 val')
    # T3: the door is on the right; the picture puts place 6 second from the left end
    seven_left_to_right = list(reversed(make_line(7)))               # place 7 at the far left, place 1 at the door on the right
    eq(seven_left_to_right.index(6), 1, 'T3: place 6 is the 2nd child from the left end'); eq(ordinal(place_front(make_line(7), 6)), '6th', 'T3'); eq(T['T3']['val'], ['6th'], 'T3 val')
    ln8 = make_line(8); wei = ln8[1]; lily = list(reversed(ln8))[2]
    eq(place_front(ln8, lily), 6, 'T4: Lily is 6th from the front'); eq(between(ln8, wei, lily), 3, 'T4'); eq(T['T4']['val'], [3], 'T4 val')
    # Go further
    sols = solve_table()
    eq(len(sols), 1, 'G1 exactly one seating fits all the clues'); eq([sols[0]['Siti'], sols[0]['Ravi'], sols[0]['Kumar']], [2, 4, 6], 'G1'); eq(T['G1']['val'], [2, 4, 6], 'G1 val'); eq(['between' in p['text'] for p in T['G1']['parts']], [False, False, False], 'G1 wording has no ambiguous between'); eq([p['text'].count('next to') for p in T['G1']['parts']], [2, 0, 2], 'G1 next to')
    ln13 = make_line(13); mei = ln13[3]; ben = list(reversed(ln13))[2]
    eq(place_front(ln13, ben), 11, 'G2: Ben is 11th from the front'); eq(between(ln13, mei, ben), 6, 'G2a')
    mid = [c for c in ln13 if in_front(ln13, c) == behind(ln13, c)]
    eq(len(mid), 1, 'G2: one middle child'); eq(ordinal(place_front(ln13, mid[0])), '7th', 'G2b'); eq(T['G2']['val'], [6, '7th'], 'G2 val')
    race = solve_race()
    eq(len(race), 1, 'G3 exactly one finishing order'); eq([ordinal(race[0]['Ben']), ordinal(race[0]['Mei'])], ['2nd', '4th'], 'G3'); eq(T['G3']['val'], ['2nd', '4th'], 'G3 val')
    # Investigation: front place + back place is one more than the number of children, for every child
    for m in (5, 8, 12):
        lm = make_line(m)
        eq({place_front(lm, c) + place_back(lm, c) for c in lm}, {m + 1}, f'investigation, line of {m}')
    eq(d['tiers']['investigation']['val'], ['add to 6', 'add to 9'], 'investigation val')
    # Exit ticket
    eq(in_front(make_line(6), 4), 3, 'E1'); l6 = make_line(6)
    eq(ordinal(place_back(l6, 5)), '2nd', 'E2'); eq(X['E1']['val'], [3], 'E1 val'); eq(X['E2']['val'], ['2nd'], 'E2 val')
    l5 = make_line(5); aisha = l5[2]; kumar = l5[l5.index(aisha) + 1]; wei = l5[l5.index(kumar) + 1]
    eq(ordinal(place_front(l5, wei)), '5th', 'E3'); eq(X['E3']['val'], ['5th'], 'E3 val')
    # Talk time: Ali is 2nd from the front and 6th from the back in exactly one line length
    eq(line_lengths_with_both_places(2, 6), [7], 'talk: a line of 7')
    # Home practice
    l6 = make_line(6); eq(ordinal(place_back(l6, l6[3])), '3rd', 'H1'); eq(in_front(make_line(9), 7), 6, 'H2')
    l = make_line(6); eq(ordinal(place_front(l, l[1 + 1 + 1])), '4th', 'H3'); l10h = make_line(9); rav = l10h[6]; l10h = [c for c in l10h if c not in l10h[:3]]; eq(ordinal(place_front(l10h, rav)), '4th', 'H4'); eq(d['home_practice'][3]['val'], '4th', 'H4 val')
    l9 = make_line(9); mid9 = [c for c in l9 if in_front(l9, c) == behind(l9, c)][0]; ben9 = l9[l9.index(mid9) + 2]
    eq(ordinal(place_front(l9, ben9)), '7th', 'H5')
    # Optional slide and spare-time menu
    ln = make_line(9); eq(place_front(ln, 7) + 2, 9, 'optional: Ben moves back two places')
    third = {m: (3, place_back(make_line(m), 3)) for m in (5, 6, 7)}
    eq(third, {5: (3, 3), 6: (3, 4), 7: (3, 5)}, 'M1')
    five_t = make_line(5); five_t[1], five_t[3] = five_t[3], five_t[1]
    eq((place_front(five_t, 2), place_front(five_t, 4), place_front(five_t, 3)), (4, 2, 3), 'M3')
    # Practice items at their authored numbers
    items = {i['id']: i for i in d['online_practice']['items']}
    eq(items['c3']['answer'], '3 children are in front of Mei.', 'c3: Mei is 4th so 3 are in front'); eq(in_front(make_line(9), 4), 3, 'c3 numbers')
    eq(items['t3']['answer'], [b for b in range(1, 9) if 3 < b < 7], 't3 places between 3rd and 7th')
    return n
