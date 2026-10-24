"""Level 2 (P2) holiday lesson 3: LEGS, WHEELS AND ARRAYS (Multiplication and division), week 2, first lesson.  Online mirror of the printed workbook pages.

The questions are the ones printed in the Level 2 holiday workbook (p2/content/l3.js `workbook()` = Start here, p2/gaps.json lesson 3 `invest` = Investigation,
p2/content/l3.js `qbank.stretch` first four = Think harder 1 to 4, `qbank.challenge` last three = Go further 5 to 7, as built by p2/workbook_html.js, and the
"Make up your own" line).  Every answer is recomputed by an INDEPENDENT checker (loops, dealing out, the picture itself; never a copy of the printed answer);
build_holiday.py stops if a checker and the printed answer differ.  Figures are the printed ones (p2/workbook_body.html) or tables drawn for a phone.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from hlib import *          # noqa: E402,F401
from p2lib import *         # noqa: E402,F401

STRAND = 'Multiplication and division'
META = dict(level=2, lesson=3, key='p2', title='Legs, wheels and arrays', workbook_title='LEGS, WHEELS AND ARRAYS', topic='Multiplication and division', strand=STRAND,
            sources=['p2/content/l3.js', 'p2/gaps.json', 'p2/workbook_html.js'],
            intro=['Use counters, a drawing or a table if they help you. Type numbers with a comma between them when a question asks for a list.',
                   'Some questions ask you to explain. Write your idea in the box, then read the worked solution after you submit and compare.'])


# ---------------------------------------------------------------- independent checkers (dealing out, counting, trying every case)
def one(lst, what):
    if len(lst) != 1:
        raise ValueError(f'{what}: {len(lst)} answers, expected exactly 1')
    return lst[0]


def deal(total, people):
    """Deal `total` things one at a time round the `people`: (each person's share, left over) when everyone gets the same."""
    hand = [0] * people
    left = total
    while left >= people:
        for p in range(people):
            hand[p] += 1
        left -= people
    assert len(set(hand)) == 1
    return hand[0], left


def mix(animals, legs, a_legs=2, b_legs=4):
    """All (a, b) numbers of two kinds of animal (a_legs, b_legs each) with `animals` in all and `legs` legs in all."""
    return [(a, animals - a) for a in range(animals + 1) if a * a_legs + (animals - a) * b_legs == legs]


def vehicles(n, wheels):
    return [(b, n - b) for b in range(n + 1) if 2 * b + 3 * (n - b) == wheels]


def first_to_hold(total, cap):
    """How many containers of size cap are needed to hold `total`: add one at a time."""
    c, held = 0, 0
    while held < total:
        c += 1
        held += cap
    return c, held - total


def rows_that_work(chairs, lo=2, hi=10):
    out = []
    for r in range(lo, hi + 1):
        a = deal(chairs, r)
        if a[1] == 0 and a[0] >= 2:
            out.append((r, a[0]))
    return out


def pieces(step, limit):
    return set(count_up_to(step, limit))


ARRAY = printed_fig('An array of counters')
TRAY = printed_fig('A tray of cups')
HENS7 = printed_fig('A pen with 7 hens')
SHARE23 = printed_fig('Ravi has 23 stickers')
VAN = printed_fig('A van with 5 seats')
CYCLES = printed_fig('A bicycle with 2 wheels')
R_ARR, C_ARR, N_ARR = circles_of(ARRAY)
N_TRAY, SEEN_TRAY = tray_counts(TRAY)
TABLE3 = grid_table([('Hens', [7, '', '', '', '', '']), ('Goats', [0, '', '', '', '', '']), ('Legs', [14, '', '', '', '', ''])],
                    caption='The hens and goats table. The first column says 7 hens, 0 goats, 14 legs. The other five columns are empty.')
LEG_TOTALS = sorted({b * 2 + (12 - b) * 3 for b in range(13)})        # 12 bicycles or tricycles: every possible number of wheels
GOAT_LEGS = sorted({h * 2 + (12 - h) * 4 for h in range(13)})         # 12 hens or goats: every possible number of legs

ITEMS = [
    # ================= Start here (workbook lesson 3, No.1 to No.6)
    dict(id='1a', tier='core', no='1(a)', type='fields', skill='arrays and multiplication', answer=[4, 5, 20, 5, 4, 20],
         q='Mei puts counters in an array. Type two multiplication sentences for it. Type each number in its box.', svg=ARRAY,
         frame='Start with the number of rows: {f1} × {f2} = {f3}.   Then start with the number of counters in each row: {f4} × {f5} = {f6}.',
         check=lambda: [R_ARR, C_ARR, N_ARR, C_ARR, R_ARR, N_ARR],
         hint='Count the rows. Then count the counters in just one row. Rows times the counters in one row gives all the counters.',
         steps=['There are 4 rows with 5 counters in each row.', '4 rows of 5 counters: 4 × 5 = 20.', 'Turn it round. 5 counters in a row, 4 rows: 5 × 4 = 20.'],
         src=['Mei puts counters in an array.', 'Two multiplication sentences']),
    dict(id='1b', tier='core', no='1(b)', type='fields', skill='arrays and division', answer=[20, 4, 5, 20, 5, 4],
         q='Look at Mei\'s array again. Type two division sentences for it. Type each number in its box.', svg=ARRAY,
         frame='Share all the counters equally into the rows: {f1} ÷ {f2} = {f3}.   Then make groups the size of one row: {f4} ÷ {f5} = {f6}.',
         check=lambda: [N_ARR, R_ARR, N_ARR // R_ARR, N_ARR, C_ARR, N_ARR // C_ARR],
         hint='Start with all the counters in the array. First share them out into the rows. Then think about groups that are the size of one row.',
         steps=['There are 20 counters altogether.', 'Share 20 equally into 4 rows: 5 in each row. 20 ÷ 4 = 5.', 'Make groups of 5 (one row each): there are 4 groups. 20 ÷ 5 = 4.'],
         src=['Two division sentences']),

    dict(id='2a', tier='core', no='2(a)', type='number', skill='arrays with a hidden part', answer=30,
         q='A tray has the same number of cups in every row. A cloth covers some of the cups. How many cups are on the tray altogether?', svg=TRAY,
         check=lambda: N_TRAY,
         hint='Look at the top row, which has no cloth on it. How many rows are there?',
         steps=['The top row has 10 cups and the tray has 3 rows.', 'Every row has the same number of cups, so 3 rows of 10 cups: 10, 20, 30.', 'There are 30 cups altogether.'],
         src=['A tray has the same number of cups in every row. A cloth covers some of the cups.', 'How many cups altogether?']),
    dict(id='2b', tier='core', no='2(b)', type='number', skill='arrays with a hidden part', answer=18,
         q='Look at the tray with the cloth. How many cups are under the cloth?', svg=TRAY,
         check=lambda: N_TRAY - SEEN_TRAY,
         hint='Work out how many cups the whole tray holds. Then count only the cups you can see.',
         steps=['The whole tray holds 3 rows of 10 cups: 30 cups.', 'You can see 10 cups in the top row, and 1 cup in each of the other 2 rows: 12 cups.', 'Under the cloth: 30 - 12 = 18 cups.'],
         src=['How many under the cloth?']),
    dict(id='2c', tier='core', no='2(c)', type='selfcheck', open=False, skill='arrays with a hidden part',
         q='How did you work out the number of cups under the cloth without lifting it? Write your idea in the box.', svg=TRAY,
         facts=dict(altogether=30, seen=12, hidden=18),
         check=lambda: dict(altogether=N_TRAY, seen=SEEN_TRAY, hidden=N_TRAY - SEEN_TRAY),
         hint='Think about the whole tray first. Then think about the cups you can see.',
         steps=['One way: the whole tray is 3 rows of 10, which is 30 cups. You can see 12 cups, so 30 - 12 = 18 cups are hidden.', 'Another way: row 2 and row 3 each hide 9 cups, and 9 + 9 = 18.',
                'Any idea that uses the rows and the cups you can see is a good one.'],
         src=['How did you work it out without lifting the cloth?']),

    dict(id='3t', tier='core', no='3 (table)', type='fields', skill='guess and check with a table', answer=[16, 18, 20, 22],
         q='A pen has hens and goats. A hen has 2 legs and a goat has 4 legs. There are 7 animals and 20 legs altogether. Start with all hens: 7 hens have 14 legs. '
           'Then swap one hen for a goat each time. How many legs are there after each swap?',
         svg=stack(HENS7, TABLE3), frame='Legs after 1 swap: {f1}.  After 2 swaps: {f2}.  After 3 swaps: {f3}.  After 4 swaps: {f4}.',
         check=lambda: [(7 - s) * 2 + s * 4 for s in (1, 2, 3, 4)],
         hint='A hen has 2 legs and a goat has 4. What happens to the legs when one hen is swapped for a goat?',
         steps=['Each swap takes away a hen (2 legs) and puts in a goat (4 legs), so the legs go up by 2.', '14, then 16, 18, 20, 22.', 'After 1 swap: 16. After 2 swaps: 18. After 3 swaps: 20. After 4 swaps: 22.'],
         src=['A pen has hens and goats. A hen has 2 legs and a goat has 4 legs. There are 7 animals and 20 legs altogether.']),
    dict(id='3a', tier='core', no='3(a)', type='fields', skill='guess and check with a table', answer=[4, 3],
         q='The pen has 7 animals, all hens (2 legs) or goats (4 legs), and 20 legs altogether. How many hens and how many goats?', svg=HENS7,
         frame='{f1} hens and {f2} goats', check=lambda: list(one(mix(7, 20), 'hens and goats')),
         hint='Look in your table for the swap that gives exactly 20 legs. How many goats are there after that many swaps?',
         steps=['Start with 7 hens (14 legs). Each swap adds 2 legs: 16, 18, 20.', '20 legs is reached after 3 swaps, so there are 3 goats and 7 - 3 = 4 hens.', 'Check: 4 hens have 8 legs and 3 goats have 12 legs. 8 + 12 = 20 legs, and 4 + 3 = 7 animals.'],
         src=['How many hens and how many goats?']),

    dict(id='4a', tier='core', no='4(a)', type='number', skill='sharing with a leftover', answer=5,
         q='Ravi has 23 stickers. He shares them equally among 4 friends, giving each friend as many as he can. How many stickers does each friend get?', svg=SHARE23,
         check=lambda: deal(23, 4)[0],
         hint='Deal the stickers out to the 4 friends one at a time, like dealing cards. Stop when there are not enough for everyone.',
         steps=['Deal 23 stickers one at a time to 4 friends. Each round uses 4 stickers.', '5 rounds use 4 × 5 = 20 stickers. There are not enough for a 6th round.', 'Each friend gets 5 stickers.'],
         src=['Ravi has 23 stickers. He shares them equally among 4 friends, giving each friend as many as he can.', 'How many does each friend get?']),
    dict(id='4b', tier='core', no='4(b)', type='number', skill='sharing with a leftover', answer=3,
         q='Ravi shares 23 stickers equally among 4 friends, giving each friend as many as he can. How many stickers are left over?', svg=SHARE23,
         check=lambda: deal(23, 4)[1],
         hint='When everyone has the same number and there are not enough for another round, count the stickers still in your hand.',
         steps=['Each friend gets 5 stickers. That uses 4 × 5 = 20 stickers.', '23 - 20 = 3 stickers are left over.', '3 is less than 4, so no friend can have one more.'],
         src=['How many are left over?']),
    dict(id='4c', tier='core', no='4(c)', type='number', skill='sharing with a leftover', answer=1,
         q='Ravi has 23 stickers and 4 friends. What is the smallest number of extra stickers he needs so that none are left over?', svg=SHARE23,
         check=lambda: one([e for e in range(1, 10) if deal(23 + e, 4)[1] == 0][:1], 'extra stickers'),
         hint='Count in 4s: 4, 8, 12 ... and see which number you land on near 23.',
         steps=['Counting in 4s: ... 20, 24. 24 is the next number in the 4 times table after 23.', 'With 24 stickers each friend gets 6 and none are left over.', 'Ravi needs 24 - 23 = 1 more sticker.'],
         src=['What is the smallest number of extra stickers Ravi needs so that none are left over?']),

    dict(id='5a', tier='core', no='5(a)', type='number', skill='division with a leftover', answer=6,
         q='28 children go on a trip. Each van holds 5 children. How many vans are needed?', svg=VAN,
         check=lambda: first_to_hold(28, 5)[0],
         hint='Count in 5s. Will 5 vans be enough for all 28 children?',
         steps=['Counting in 5s: 5, 10, 15, 20, 25, 30.', '5 vans hold 25 children. The other 3 children need a van too.', '6 vans are needed.'],
         src=['28 children go on a trip. Each van holds 5 children.', 'How many vans are needed?']),
    dict(id='5b', tier='core', no='5(b)', type='number', skill='division with a leftover', answer=2,
         q='28 children go on a trip in vans that each hold 5 children. How many empty seats are there?', svg=VAN,
         check=lambda: first_to_hold(28, 5)[1],
         hint='Think about all the seats in the vans you need, and how many children sit in them.',
         steps=['6 vans have 6 × 5 = 30 seats.', '28 children sit in them, so 30 - 28 = 2 seats are empty.'],
         src=['How many empty seats?']),

    dict(id='6a', tier='core', no='6(a)', type='set', ordered=False, skill='finding all the arrays', answer=[2, 4, 5, 10],
         q='Mr Tan puts 20 chairs in equal rows. There must be at least 2 rows and at least 2 chairs in each row. Which numbers of rows work, from 2 rows up to 10 rows? '
           'Type every number of rows that works, with a comma between.',
         check=lambda: [r for r, _ in rows_that_work(20)],
         hint='Pick a number of rows and deal the 20 chairs out one at a time. A number of rows works only if every row ends up with the same number of chairs.',
         steps=['Deal 20 chairs into 2 rows: 10 each. It works.', '3 rows leave 2 chairs over, so it does not work. 4 rows: 5 each, it works. 5 rows: 4 each, it works.',
                '6, 7, 8 and 9 rows do not work. 10 rows: 2 each, it works.', 'The numbers of rows that work are 2, 4, 5 and 10.'],
         src=['Mr Tan puts 20 chairs in equal rows. There must be at least 2 rows and at least 2 chairs in each row. Find ALL the ways.']),
    dict(id='6b', tier='core', no='6(b)', type='set', ordered=True, skill='finding all the arrays', answer=[10, 5, 4, 2],
         q='Mr Tan\'s 20 chairs are in equal rows. For each number of rows that works, how many chairs are in each row? Type them in order, starting with the fewest rows.',
         check=lambda: [c for _, c in rows_that_work(20)],
         hint='Start with the smallest number of rows that works. Share the 20 chairs equally into those rows. Then do the next number of rows.',
         steps=['2 rows: 10 chairs in each row.', '4 rows: 5 chairs in each row.', '5 rows: 4 chairs in each row.', '10 rows: 2 chairs in each row.', 'In order: 10, 5, 4, 2.'],
         src=['Chairs in each row']),

    # ================= Investigation: Where tables meet
    dict(id='I1', tier='invest', no='Investigation (a)', type='set', ordered=False, skill='tables that meet', answer=[10, 20, 30, 40, 50],
         q='Where tables meet. Which numbers up to 50 are in BOTH the 2 times table and the 5 times table? Type them with a comma between.',
         check=lambda: sorted(pieces(2, 50) & pieces(5, 50)),
         hint='Easy first step: write the 5 times table up to 50, then circle the even numbers.',
         steps=['The 2 times table up to 50 is 2, 4, 6 ... 50. The 5 times table up to 50 is 5, 10, 15 ... 50.', 'The numbers in both lists are 10, 20, 30, 40 and 50.'],
         src=['List the numbers up to 50 that are in BOTH the 2 times table and the 5 times table.']),
    dict(id='I2', tier='invest', no='Investigation (a) notice', type='selfcheck', open=False, skill='tables that meet',
         q='Look at the numbers that are in both the 2 and the 5 times tables. What do you notice about them? Write your idea in the box.',
         facts=dict(jump=10, all_in_ten_table=True),
         check=lambda: dict(jump=one(sorted({b - a for a, b in zip(sorted(pieces(2, 50) & pieces(5, 50)), sorted(pieces(2, 50) & pieces(5, 50))[1:])}), 'jump'),
                            all_in_ten_table=all(n in pieces(10, 50) for n in pieces(2, 50) & pieces(5, 50))),
         hint='Look at how far apart the numbers are. Do you know a times table with those numbers?',
         steps=['The numbers are 10, 20, 30, 40, 50. They go up by 10 each time.', 'They are the 10 times table. Any answer that says this is a good one.'],
         src=['What do you notice about them?']),
    dict(id='I3', tier='invest', no='Investigation (b)', type='set', ordered=False, skill='tables that meet', answer=[15, 30, 45],
         q='Now find the numbers up to 50 that are in both the 3 times table and the 5 times table. Type them with a comma between.',
         check=lambda: sorted(pieces(3, 50) & pieces(5, 50)),
         hint='Write the 3 times table up to 50 and the 5 times table up to 50. Which numbers are in both lists?',
         steps=['The 3 times table: 3, 6, 9, 12, 15 ... 48. The 5 times table: 5, 10, 15 ... 50.', 'The numbers in both lists are 15, 30 and 45. They go up by 15.'],
         src=['Now find the numbers up to 50 that are in both the 3 and 5 tables.']),
    dict(id='I4', tier='invest', no='Investigation (c)', type='choice', options=['Yes', 'No'], answer='Yes', skill='tables that meet',
         q='Is every number that is in both the 2 and the 5 times tables also in the 10 times table?',
         check=lambda: 'Yes' if all(n in pieces(10, 1000) for n in pieces(2, 1000) & pieces(5, 1000)) else 'No',
         hint='Look at the numbers you found in (a). Then test some bigger numbers that are in both tables.',
         steps=['Numbers in both tables that I tried: 10, 20, 30, 40, 50, 60 ... All of them are in the 10 times table.', 'Yes, every number that is in both the 2 and 5 times tables is also in the 10 times table.'],
         src=['Is every number in both the 2 and 5 tables also in the 10 table? Explain.']),
    dict(id='I5', tier='invest', no='Investigation (c) explain', type='selfcheck', open=False, skill='tables that meet',
         q='Explain why. Why is a number that is in both the 2 and the 5 times tables always in the 10 times table? Write your idea in the box.',
         facts=dict(ends_in_zero=True),
         check=lambda: dict(ends_in_zero=all(n % 10 == 0 for n in range(1, 1000) if n in pieces(2, 1000) and n in pieces(5, 1000))),
         hint='Think about the last digit of a number in the 2 times table, and of a number in the 5 times table.',
         steps=['A number in the 2 times table is even: it ends in 0, 2, 4, 6 or 8.', 'A number in the 5 times table ends in 0 or 5.', 'A number in both must end in 0, and every number that ends in 0 is in the 10 times table.', 'Any clear reason like this is a good answer.'],
         src=['Is every number in both the 2 and 5 tables also in the 10 table? Explain.']),

    # ================= Think harder
    dict(id='T1a', tier='stretch', no='Think harder 1', type='set', ordered=False, skill='two kinds, find all the ways', answer=[1, 3, 5],
         q='A shop has some bicycles (2 wheels) and some tricycles (3 wheels), at least one of each. There are 17 wheels altogether. Find ALL the ways. '
           'Start with 1 tricycle, then 2 tricycles, and so on. How many tricycles can there be? Type every number of tricycles that works, with a comma between.', svg=CYCLES,
         check=lambda: [t for t in range(1, 9) for b in range(1, 9) if 2 * b + 3 * t == 17],
         hint='Start with 1 tricycle (3 wheels). How many wheels are left for the bicycles? Can bicycles use up exactly that many?',
         steps=['1 tricycle: 3 wheels. 14 wheels are left, and 7 bicycles have 14 wheels. It works.', '2 tricycles: 6 wheels. 11 are left, which is odd. Bicycles need an even number, so it does not work.',
                '3 tricycles: 9 wheels. 8 are left: 4 bicycles. It works.', '5 tricycles: 15 wheels. 2 are left: 1 bicycle. It works.', '4 tricycles leave 5 (odd), and 6 tricycles need 18 wheels, which is too many. The numbers of tricycles are 1, 3 and 5.'],
         src=['A shop has some bicycles (2 wheels) and some tricycles (3 wheels), at least one of each.', 'Find ALL the ways.']),
    dict(id='T1b', tier='stretch', no='Think harder 1 (bicycles)', type='set', ordered=True, skill='two kinds, find all the ways', answer=[7, 4, 1],
         q='The shop has bicycles (2 wheels) and tricycles (3 wheels), at least one of each, and 17 wheels altogether. For each way, how many bicycles are there? '
           'Type them in order, starting with the way that has the fewest tricycles.', svg=CYCLES,
         check=lambda: [b for t in range(1, 9) for b in range(1, 9) if 2 * b + 3 * t == 17],
         hint='Take the tricycles\' wheels away from 17. The wheels left are for the bicycles. Do the way with the fewest tricycles first.',
         steps=['1 tricycle: 17 - 3 = 14 wheels, so 7 bicycles.', '3 tricycles: 17 - 9 = 8 wheels, so 4 bicycles.', '5 tricycles: 17 - 15 = 2 wheels, so 1 bicycle.', 'The ways are 7 bicycles and 1 tricycle, 4 and 3, 1 and 5. In order the bicycles are 7, 4, 1.'],
         src=['Find ALL the ways.']),
    dict(id='T1c', tier='stretch', no='Think harder 1 (how do you know)', type='selfcheck', open=False, skill='two kinds, find all the ways',
         q='How do you know you have found all the ways? Write your idea in the box.', svg=CYCLES,
         facts=dict(works=[1, 3, 5], odd_tricycles_only=True),
         check=lambda: dict(works=[t for t in range(1, 9) for b in range(1, 9) if 2 * b + 3 * t == 17],
                            odd_tricycles_only=all(t % 2 == 1 for t in range(1, 9) for b in range(1, 9) if 2 * b + 3 * t == 17)),
         hint='Make a table with 1 tricycle, 2 tricycles, 3 tricycles and so on. When do you run out of wheels?',
         steps=['Try every number of tricycles: 1, 2, 3, 4, 5, 6 ...', '2 and 4 tricycles leave an odd number of wheels, and bicycles can only use an even number of wheels.', '6 or more tricycles need 18 wheels or more, which is too many.',
                'So the only ways are with 1, 3 or 5 tricycles.'],
         src=['How do you know you have found them all?']),

    dict(id='T2a', tier='stretch', no='Think harder 2', type='choice', options=['Mei', 'Siti'], answer='Siti', skill='odd and even totals',
         q='A farm has 9 animals, each a hen (2 legs) or a goat (4 legs). Mei counts 25 legs. Siti counts 26 legs. Only one of them can be right. Who is right?',
         check=lambda: one([w for w, legs in (('Mei', 25), ('Siti', 26)) if mix(9, legs)], 'who is right'),
         hint='Start with 9 hens. How many legs is that? What happens to the legs when you swap one hen for a goat?',
         steps=['9 hens have 18 legs. Each swap of a hen for a goat adds 2 legs: 18, 20, 22, 24, 26.', '26 legs is possible (after 4 swaps). 25 never comes up.', 'Siti is right.'],
         src=['A farm has 9 animals, each a hen (2 legs) or a goat (4 legs). Mei counts 25 legs. Siti counts 26 legs. Only one of them can be right. Who?']),
    dict(id='T2b', tier='stretch', no='Think harder 2 (how many)', type='fields', skill='odd and even totals', answer=[5, 4],
         q='The farm has 9 animals, each a hen (2 legs) or a goat (4 legs). Only one of the two counts, 25 legs (Mei) or 26 legs (Siti), can be right. How many hens and how many goats?',
         frame='{f1} hens and {f2} goats', check=lambda: list(one(mix(9, 26) + mix(9, 25), 'hens and goats')),
         hint='Use the count that can be right. Start with 9 hens and swap one hen for a goat at a time, or try different numbers of goats.',
         steps=['Start with 9 hens: 18 legs. Each swap adds 2 legs.', '4 swaps give 18 + 8 = 26 legs. So 4 goats and 9 - 4 = 5 hens.', 'Check: 5 hens have 10 legs, 4 goats have 16 legs. 10 + 16 = 26, and 5 + 4 = 9 animals.'],
         src=['How many hens and goats?']),
    dict(id='T2c', tier='stretch', no='Think harder 2 (the other)', type='selfcheck', open=False, skill='odd and even totals',
         q='Why can the other person NOT be right? Write your idea in the box.',
         facts=dict(all_totals_even=True),
         check=lambda: dict(all_totals_even=all((h * 2 + (9 - h) * 4) % 2 == 0 for h in range(10))),
         hint='Look at the legs of 9 hens and goats in your table. Are the totals odd or even?',
         steps=['Hens have 2 legs and goats have 4 legs. Both are in the 2 times table.', 'So any group of hens and goats has an even number of legs: 18, 20, 22, 24, 26 ...', '25 is odd, so nobody can count 25 legs. Any answer that says this is a good one.'],
         src=['Only one of them can be right. Who?']),

    dict(id='T3', tier='stretch', no='Think harder 3', type='fields', skill='sharing with a leftover', answer=[8, 2],
         q='Ali shares 34 marbles equally among 4 friends, giving as many as he can.', frame='Each friend gets {f1}. Marbles left over: {f2}.',
         check=lambda: list(deal(34, 4)),
         hint='Deal the marbles one at a time, or count in 4s. Stop before you go past 34.',
         steps=['Counting in 4s: 4, 8, 12, 16, 20, 24, 28, 32. 32 is 4 × 8.', 'Each friend gets 8 marbles. That uses 32 marbles.', '34 - 32 = 2 marbles are left over.'],
         src=['Ali shares 34 marbles equally among 4 friends, giving as many as he can. How many does each friend get? How many are left over?']),
    dict(id='T4', tier='stretch', no='Think harder 4', type='number', skill='arrays with a hidden part', answer=16,
         q='An array of stickers has 4 rows. Ben counts 12 stickers in the first 3 rows. How many stickers are in the whole array?',
         check=lambda: (lambda per: sum(per for _ in range(4)))(one([k for k in range(1, 13) if sum(k for _ in range(3)) == 12], 'per row')),
         hint='Every row has the same number of stickers. How many stickers are in one row?',
         steps=['3 rows have 12 stickers, so each row has 12 ÷ 3 = 4 stickers.', 'The whole array has 4 rows of 4: 4 × 4 = 16 stickers.'],
         src=['An array of stickers has 4 rows. Ben counts 12 stickers in the first 3 rows. How many stickers are in the whole array?']),

    # ================= Go further
    dict(id='C5a', tier='challenge', no='Go further 5', type='choice', options=['Yes', 'No'], answer='Yes', skill='totals that skip or not',
         q='A shop has 12 vehicles. Each one is a bicycle (2 wheels) or a tricycle (3 wheels). Mei says: "Ravi could count 24 wheels, or 25, or 26, or any number of wheels up to 36." Is she right?',
         check=lambda: 'Yes' if LEG_TOTALS == list(range(24, 37)) else 'No',
         hint='Start with 12 bicycles and swap one bicycle for a tricycle at a time. What happens to the number of wheels each time?',
         steps=['12 bicycles have 24 wheels. 12 tricycles have 36 wheels.', 'Each swap of a bicycle for a tricycle adds exactly 1 wheel: 24, 25, 26, 27 ... 36.', 'Every number from 24 to 36 can be counted, so Mei is right.'],
         src=['A shop has 12 vehicles. Each one is a bicycle (2 wheels) or a tricycle (3 wheels). Mei says:']),
    dict(id='C5b', tier='challenge', no='Go further 5 (37)', type='choice', options=['Yes', 'No'], answer='No', skill='totals that skip or not',
         q='The shop has 12 vehicles, each a bicycle (2 wheels) or a tricycle (3 wheels). Could Ravi count 37 wheels?',
         check=lambda: 'Yes' if 37 in LEG_TOTALS else 'No',
         hint='What is the most wheels the shop can have? Think about what happens when every vehicle is a tricycle.',
         steps=['The most wheels is when all 12 vehicles are tricycles: 12 × 3 = 36.', '37 is more than 36, so Ravi could not count 37 wheels.'],
         src=['Could he count 37?']),
    dict(id='C5c', tier='challenge', no='Go further 5 (legs)', type='selfcheck', open=False, skill='totals that skip or not',
         q='Ravi can count 25 wheels on 12 bicycles and tricycles. But with 12 hens (2 legs) and goats (4 legs) he can never count 25 legs. Why? Write your idea in the box.',
         facts=dict(wheels_25=[(11, 1)], legs_25_possible=False),
         check=lambda: dict(wheels_25=vehicles(12, 25), legs_25_possible=25 in GOAT_LEGS),
         hint='Try one swap in the shop: what happens to the wheels? Then try one swap in the pen: what happens to the legs?',
         steps=['Swapping a bicycle for a tricycle adds 1 wheel, so the wheels go up by 1 each time and no number is missed. For example 11 bicycles and 1 tricycle make 22 + 3 = 25 wheels.',
                'Swapping a hen for a goat adds 2 legs, so the legs go 24, 26, 28 ... 48. They are always even.', '25 is odd, so Ravi can never count 25 legs.'],
         src=['why can Ravi count 25 wheels but never 25 legs?']),
    dict(id='C6', tier='challenge', no='Go further 6', type='number', skill='groups with leftovers', answer=27,
         q='Mr Lim has between 20 and 30 sweets. When he puts them in groups of 4, 3 are left over. When he puts them in groups of 5, 2 are left over. How many sweets does he have?',
         check=lambda: one([n for n in range(21, 30) if deal(n, 4)[1] == 3 and deal(n, 5)[1] == 2], 'sweets'),
         hint='Make a list of the numbers between 20 and 30 that leave 3 when put in groups of 4. Then test each one with groups of 5.',
         steps=['Groups of 4 with 3 left over: 23 or 27.', 'Test with groups of 5: 23 leaves 3, but 27 leaves 2.', 'Mr Lim has 27 sweets.'],
         src=['Mr Lim has between 20 and 30 sweets.']),
    dict(id='C7', tier='challenge', no='Go further 7', type='fields', skill='guess and check with a clue', answer=[5, 3],
         q='A pen has hens (2 legs) and goats (4 legs). There are 2 more hens than goats. There are 22 legs altogether. How many hens and how many goats?',
         frame='{f1} hens and {f2} goats', check=lambda: list(one([(h, g) for h in range(12) for g in range(12) if h == g + 2 and 2 * h + 4 * g == 22], 'hens and goats')),
         hint='Guess and check. Try 1 goat: how many hens is that, and how many legs? Then try 2 goats.',
         steps=['1 goat means 3 hens: 6 + 4 = 10 legs. Too few.', '2 goats means 4 hens: 8 + 8 = 16 legs. Still too few.', '3 goats means 5 hens: 10 + 12 = 22 legs. That is right.', 'There are 5 hens and 3 goats.'],
         src=['A pen has hens and goats. There are 2 more hens than goats. There are 22 legs altogether.']),
    dict(id='M', tier='challenge', no='Make up your own', type='selfcheck', open=False, skill='making puzzles',
         q='Make up your own "how many of each" puzzle with two kinds of things, so that there is only ONE answer. Write your clues and solve it. Swap with a partner.',
         facts=[(3, 3)], check=lambda: mix(6, 18),
         hint='Choose two kinds of things with different numbers of legs. Pick how many of each, then work out the total legs for your clues. Check that only one answer fits.',
         steps=['Many answers are right. Here is one example: ducks (2 legs) and cows (4 legs). There are 6 animals and 18 legs altogether. How many of each?',
                'Start with 6 ducks: 12 legs. Each swap adds 2 legs: 14, 16, 18. After 3 swaps there are 3 cows and 3 ducks. Check: 6 + 12 = 18.', 'It is the only answer, because each swap changes the legs by 2 and 18 is reached just once.'],
         src=['puzzle with two kinds of things, so that there is only ONE answer.']),
]
for _d in ITEMS:
    _d.setdefault('strand', STRAND)


# ---------------------------------------------------------------- variant families (template + independent oracle over EVERY combination)
VARIANTS = {
    '4a': dict(
        base=dict(n=23, k=4),
        tpl=dict(vars=dict(n=[17, 19, 23, 29, 31], k=[3, 4, 5]), q='{n} stickers are shared equally among {k} friends, giving each friend as many as possible. How many stickers does each friend get?',
                 answer='n//k', hint='Deal the stickers out one at a time to the {k} friends. Stop when there are not enough for everyone.',
                 steps=['Count in {k}s until you would go past {n}.', 'The number of rounds is the number each friend gets: {ans}.']),
        oracle=lambda e: deal(e['n'], e['k'])[0]),
    '4b': dict(
        base=dict(n=23, k=4),
        tpl=dict(vars=dict(n=[17, 19, 23, 29, 31], k=[3, 4, 5]), q='{n} stickers are shared equally among {k} friends, giving each friend as many as possible. How many stickers are left over?',
                 answer='n%k', hint='Give every friend the same number. Then count the stickers still in your hand.',
                 steps=['Count in {k}s until you would go past {n}.', '{n} take away the last number you counted to is the number left over: {ans}.']),
        oracle=lambda e: deal(e['n'], e['k'])[1]),
    '5a': dict(
        base=dict(n=28, c=5),
        tpl=dict(vars=dict(n=[23, 29, 31, 37], c=[4, 5, 6]), q='{n} children go on a trip. Each van holds {c} children. How many vans are needed?',
                 answer='(n+c-1)//c', hint='Count in {c}s. Will that many vans hold all {n} children?',
                 steps=['Count in {c}s until the number is {n} or more.', 'The last van is only partly full, but it is still needed. {ans} vans are needed.']),
        oracle=lambda e: first_to_hold(e['n'], e['c'])[0]),
    '5b': dict(
        base=dict(n=28, c=5),
        tpl=dict(vars=dict(n=[23, 29, 31, 37], c=[4, 5, 6]), q='{n} children go on a trip in vans that each hold {c} children. How many empty seats are there?',
                 answer='((n+c-1)//c)*c-n', hint='Work out how many vans are needed. Then think about all their seats and how many children sit in them.',
                 steps=['Count in {c}s until the number is {n} or more. That is all the seats.', 'All the seats take away the {n} children is the number of empty seats: {ans}.']),
        oracle=lambda e: first_to_hold(e['n'], e['c'])[1]),
    '3a': dict(
        base=dict(an=7, g=3),
        tpl=dict(vars=dict(an=[6, 7, 8, 9], g=[1, 2, 3, 4]), derive=dict(legs='2*an+2*g'),
                 q='A pen has {an} animals, all hens (2 legs) or goats (4 legs), and {legs} legs altogether. How many hens and how many goats?',
                 frame='{f1} hens and {f2} goats', answers=dict(f1='an-g', f2='g'),
                 hint='Start with all hens, then swap one hen for a goat each time. Count the legs after each swap.',
                 steps=['Start with {an} hens: that is {an} × 2 legs. Each swap adds 2 legs.', 'Keep swapping until you reach {legs} legs.', 'There are {ans} (hens, then goats). Check the legs and the number of animals.']),
        oracle=lambda e: (lambda s: dict(f1=s[0], f2=s[1]))(one(mix(e['an'], 2 * e['an'] + 2 * e['g']), 'hens and goats'))),
}
