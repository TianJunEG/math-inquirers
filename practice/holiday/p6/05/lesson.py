"""Online practice for Level 6 (Primary 6, ages 11-13) holiday lesson 5: Every Possible Way (counting; the multiplication rule; nested loops that list every case).

The questions are the ones printed in the Level 6 holiday workbook (p6/content/l5.js workbook(): Start here Q1 to Q6; the Finish page: the Investigation
(p6/content/gaps.json lesson 5) and the exit slip (l5.js lesson.exit); Think harder = the first three l5.js qbank.stretch questions plus the one moved there from Start here
(l5.js moved); Go further = the last three l5.js qbank.challenge questions).  Every answer is recomputed by an INDEPENDENT checker below: loops and itertools over the cases in
the question, a walk over every route on the grid, and the block-program interpreter w3lib.run for the code questions (the program that is drawn is the very list that is run).
build_holiday.py stops if a checker and the printed answer differ.  Scratch is not run in the page: the code is drawn as blocks and traced on paper or in the head.
"""
import itertools, os, sys
HERE_ = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE_, '..'))
sys.path.insert(0, os.path.join(HERE_, '..', '..'))
from hlib import *      # noqa: E402,F401
import p6lib as P       # noqa: E402
import w3lib as W       # noqa: E402

M = W.MINUS
META = dict(level=6, lesson=5, key='p6', title='Every Possible Way', workbook_title='EVERY POSSIBLE WAY', topic='Counting',
            strand='Counting and coding',
            sources=['p6/content/l5.js', 'p6/content/gaps.json'],
            intro=['You do not need Scratch on this page. The code is drawn as blocks: read it, trace it on paper or in your head, and type what the sprite says. '
                   'The block "join a b" writes the value of a next to the value of b (a is 7 and b is 5 gives 75).',
                   'Counting questions are easiest with an organised list: fix the first choice, then run through every second choice.',
                   'Lists of numbers are typed with commas. A few questions ask for a list or a plan: use paper if you want to, then type the answer.'])
CT, CO = 'Counting', 'Coding and counting'

LIST = W.program('l5', 'listCode')          # set a to 1; repeat 3 { set b to 1; repeat 4 { say join a b; change b by 1 }; change a by 1 }
PLAN = W.program('l5', 'planCode')          # count handshakes; three gaps: repeat [?], repeat [?], if [?] then
CODE_LABEL = 'Code: set a to 1. Repeat 3 times: set b to 1, then repeat 4 times: say join a b, change b by 1. After the inner loop, change a by 1.'
PLAN_LABEL = 'Plan with three gaps: set count to 0, set a to 1, repeat a gap: set b to 1, repeat a gap: if a gap then change count by 1; change b by 1; change a by 1. At the end say count.'


def code_fig():
    return W.blocks('l5', LIST, CODE_LABEL)


def plan_fig():
    return W.blocks('l5', PLAN, PLAN_LABEL)


def cards_fig(ds):
    return W.cards(ds)


def grid_fig():
    return W.street_grid()


def with_repeat(prog, n):
    """The listCode program with its outer repeat changed to n."""
    p = [list(x) for x in prog]
    for x in p:
        if x[0] == 'ctrl':
            x[1] = f'repeat [{n}]'
    return p


# ---------------------------------------------------------------- independent counting
def handshakes(n):
    return len(list(itertools.combinations(range(n), 2)))


def numbers_from(cards, k, first_nonzero=True):
    out = []
    for p in itertools.permutations(cards, k):
        if first_nonzero and p[0] == 0:
            continue
        out.append(int(''.join(map(str, p))))
    return sorted(out)


def choices_per_place(cards, k):
    """For k-digit numbers from the cards (each at most once, no 0 first): the number of cards that can go in each place, found by grouping the numbers by their start."""
    nums = [tuple(map(int, str(x))) for x in numbers_from(cards, k)]
    per = []
    for pos in range(k):
        sizes = {}
        for pre in {n[:pos] for n in nums}:
            sizes[pre] = len({n[pos] for n in nums if n[:pos] == pre})
        assert len(set(sizes.values())) == 1, 'the number of choices is not the same for every start'
        per.append(sizes[next(iter(sizes))])
    return per


def pay(total, coins):
    """Every way to pay `total` cents with the coins (as many of each as you like): a tuple of counts, one per coin, found by looping."""
    ways = []
    for counts in itertools.product(*[range(total // c + 1) for c in coins]):
        if sum(n * c for n, c in zip(counts, coins)) == total:
            ways.append(counts)
    return ways


def loop_needed(friends):
    """How many times a loop that counts 1, 2, 3 ... must repeat so that it visits every friend 1 to `friends`."""
    return next(r for r in range(1, 100) if set(range(1, r + 1)) >= set(range(1, friends + 1)))


def three_digit_sum(total):
    return [n for n in range(100, 1000) if sum(int(d) for d in str(n)) == total]


def ways_fig(ways, with50=False):
    rows = [[str(w[0]), str(w[1]), str(w[2])] for w in sorted(ways, key=lambda w: (-w[0], -w[1]))]
    return W.table_svg(['20-cent', '10-cent', '5-cent'], rows, 'The 12 ways to pay 50 cents with 5-cent, 10-cent and 20-cent coins, sorted by the number of 20-cent coins: '
                       + '; '.join(f'{r[0]} twenties, {r[1]} tens, {r[2]} fives' for r in rows), [90, 90, 90], 16, 28)


ROUTES_A = W.corner_counts(3)
ROUTES_B = W.corner_counts(3, [(1, 1)])
COND_OK = ['a<b', 'a < b', 'b>a', 'b > a', 'a>b', 'a > b', 'b<a', 'b < a']


def cond_works(c):
    return W.run(W.fill(PLAN, [7, 7, c]))[0] == [handshakes(7)]


ITEMS = [
    # ================= Start here (workbook Lesson 5, Q1 to Q6)
    dict(id='1a', tier='core', no='1(a)', type='number', strand=CT, skill='multiplication rule', answer=12,
         q='Mei packs 4 T-shirts, 3 pairs of shorts and 2 caps for camp. How many outfits of 1 T-shirt and 1 pair of shorts can she make?',
         check=lambda: len(list(itertools.product(range(4), range(3)))),
         hint='Take one T-shirt. How many pairs of shorts can go with it? Then think about the other T-shirts.',
         steps=['Fix one T-shirt: it can go with any of the 3 pairs of shorts, so that is 3 outfits.', 'There are 4 T-shirts, and each one has 3 outfits: 4 × 3 = 12.', 'Mei can make 12 outfits.'],
         src=['Mei packs 4 T-shirts, 3 pairs of shorts and 2 caps for camp.', 'Outfits of 1 T-shirt and 1 pair of shorts: how many?']),
    dict(id='1b', tier='core', no='1(b)', type='number', strand=CT, skill='multiplication rule', answer=24,
         q='Mei packs 4 T-shirts, 3 pairs of shorts and 2 caps for camp. An outfit is now a T-shirt, a pair of shorts and a cap. How many outfits can she make?',
         check=lambda: len(list(itertools.product(range(4), range(3), range(2)))),
         hint='Think about the T-shirt-and-shorts outfits first. How many caps can go with each one?',
         steps=['Each T-shirt and shorts outfit can go with either of the 2 caps.', 'So the choices multiply: 4 × 3 × 2 = 24.', 'Mei can make 24 outfits. (4 × 3 = 12 outfits of T-shirt and shorts, each with 2 caps.)'],
         src=['With a cap too?']),

    dict(id='2a', tier='core', no='2(a)', type='number', strand=CT, skill='counting digit numbers', answer=9, svg=cards_fig([0, 3, 5, 8]),
         q='Digit cards 0, 3, 5 and 8. Use each card at most once in a number. A number cannot start with 0. How many 2-digit numbers can you make?',
         check=lambda: len(numbers_from([0, 3, 5, 8], 2)),
         hint='Which cards can go in the tens place? Then, for each of them, how many cards are left for the ones place?',
         steps=['The tens digit cannot be 0, so it is 3, 5 or 8: 3 choices.', 'For each of them, the other 3 cards (0 is allowed in the ones place) are left: 3 choices.', '3 × 3 = 9 numbers.'],
         src=['How many 2-digit numbers can you make?']),
    dict(id='2a-list', tier='core', no='2(a) list', type='set', ordered=True, strand=CT, skill='listing in order', answer=numbers_from([0, 3, 5, 8], 2), svg=cards_fig([0, 3, 5, 8]),
         q='Digit cards 0, 3, 5 and 8. Use each card at most once, and a number cannot start with 0. List all the 2-digit numbers from smallest to largest. Type them with commas.',
         check=lambda: numbers_from([0, 3, 5, 8], 2), label='2(a) list',
         hint='Fix the tens digit, go through every ones digit in order, then move to the next tens digit.',
         steps=['Tens digit 3: 30, 35, 38.', 'Tens digit 5: 50, 53, 58.', 'Tens digit 8: 80, 83, 85.', 'In order: 30, 35, 38, 50, 53, 58, 80, 83, 85.'],
         src=['List them from smallest to largest']),
    dict(id='2b', tier='core', no='2(b)', type='fields', strand=CT, skill='multiplication rule', svg=cards_fig([0, 3, 5, 8]),
         q='Digit cards 0, 3, 5 and 8. Use each card at most once, and a number cannot start with 0. How many 3-digit numbers can you make? Write the multiplication: how many cards can go in each place?',
         frame='Choices for the 1st digit: {f1}   2nd digit: {f2}   3rd digit: {f3}   numbers altogether: {f4}', answer=[3, 3, 2, 18],
         check=lambda: choices_per_place([0, 3, 5, 8], 3) + [len(numbers_from([0, 3, 5, 8], 3))],
         hint='The first digit cannot be 0. Choose it first. How many cards are left for the 2nd place, and then for the 3rd place?',
         steps=['1st digit: not 0, so 3, 5 or 8: 3 choices.', '2nd digit: 3 cards are left, and 0 is allowed here: 3 choices.', '3rd digit: 2 cards are left: 2 choices.', '3 × 3 × 2 = 18 numbers.'],
         src=['How many 3-digit numbers? Write the multiplication.']),

    dict(id='3a1', tier='core', no='3(a) rows 1-2', type='fields', strand=CO, skill='tracing nested loops', svg=code_fig(), label='3(a) 1-2',
         q='Trace the code. Fill in a, b and what the sprite says, for the 1st and 2nd things it says.',
         frame='1st thing: a is {f1}   b is {f2}   it says {f3}      2nd thing: a is {f4}   b is {f5}   it says {f6}',
         answer=[1, 1, 11, 1, 2, 12],
         check=lambda: (lambda tr, sd: [x for k in (0, 1) for x in (tr[k]['a'], tr[k]['b'], sd[k])])(*(lambda t: (t, W.run(LIST, trace=t)[0]))([])),
         hint='The sprite says join a b: the value of a, then the value of b. The inside loop changes b after each say.',
         steps=['The program sets a to 1 and b to 1, then says join a b: a is 1, b is 1, so it says 11.', 'Then b goes up by 1. The next say has a = 1 and b = 2: it says 12.'],
         src=['Fill in a, b and what the sprite says, for the first 6 things it says.']),
    dict(id='3a2', tier='core', no='3(a) rows 3-4', type='fields', strand=CO, skill='tracing nested loops', svg=code_fig(), label='3(a) 3-4',
         q='Trace the code. Fill in a, b and what the sprite says, for the 3rd and 4th things it says.',
         frame='3rd thing: a is {f1}   b is {f2}   it says {f3}      4th thing: a is {f4}   b is {f5}   it says {f6}',
         answer=[1, 3, 13, 1, 4, 14],
         check=lambda: (lambda tr, sd: [x for k in (2, 3) for x in (tr[k]['a'], tr[k]['b'], sd[k])])(*(lambda t: (t, W.run(LIST, trace=t)[0]))([])),
         hint='Keep following b: it goes up by 1 after each say. How many times does the inside loop go round before a changes?',
         steps=['b keeps going up by 1 while a stays the same: a = 1, b = 3 says 13, and a = 1, b = 4 says 14.', 'The inside loop repeats 4 times for each value of a.'],
         src=['Fill in a, b and what the sprite says, for the first 6 things it says.']),
    dict(id='3a3', tier='core', no='3(a) rows 5-6', type='fields', strand=CO, skill='tracing nested loops', svg=code_fig(), label='3(a) 5-6',
         q='Trace the code. Fill in a, b and what the sprite says, for the 5th and 6th things it says.',
         frame='5th thing: a is {f1}   b is {f2}   it says {f3}      6th thing: a is {f4}   b is {f5}   it says {f6}',
         answer=[2, 1, 21, 2, 2, 22],
         check=lambda: (lambda tr, sd: [x for k in (4, 5) for x in (tr[k]['a'], tr[k]['b'], sd[k])])(*(lambda t: (t, W.run(LIST, trace=t)[0]))([])),
         hint='After the inside loop has gone round 4 times, a goes up by 1. What happens to b at the start of the next turn of the outside loop?',
         steps=['After 4 says, the inside loop has finished and a goes up by 1: a is now 2.', 'The outside loop starts again and sets b back to 1: a = 2, b = 1 says 21. Then a = 2, b = 2 says 22.'],
         src=['Fill in a, b and what the sprite says, for the first 6 things it says.']),
    dict(id='3b', tier='core', no='3(b)', type='number', strand=CO, skill='counting loop repeats', answer=12, svg=code_fig(),
         q='Trace the code. How many things does it say altogether?', check=lambda: len(W.run(LIST)[0]),
         hint='How many things does the inside loop say in one full turn? How many times does the outside loop go round?',
         steps=['Each turn of the outside loop, the inside loop says 4 things.', 'The outside loop goes round 3 times: 3 × 4 = 12.', 'It says 12 things altogether.'],
         src=['How many things does it say altogether?']),
    dict(id='3c', tier='core', no='3(c)', type='number', strand=CO, skill='tracing nested loops', answer=34, svg=code_fig(),
         q='Trace the code. What is the last thing it says?', check=lambda: W.run(LIST)[0][-1],
         hint='The last thing is said in the last turn of both loops. What are a and b then?',
         steps=['In the last turn of the outside loop, a is 3.', 'In the last turn of the inside loop, b is 4.', 'The last thing it says is join 3 4, which is 34.'],
         src=['The last thing it says?']),
    dict(id='3d', tier='core', no='3(d)', type='number', strand=CO, skill='counting loop repeats', answer=20, svg=code_fig(),
         q='Trace the code. If "repeat 3" (the outside loop) becomes "repeat 5", how many things will it say?', check=lambda: len(W.run(with_repeat(LIST, 5))[0]),
         hint='The inside loop still says the same number of things each turn. Only the number of turns of the outside loop changes.',
         steps=['The inside loop still says 4 things each turn.', 'The outside loop now goes round 5 times: 5 × 4 = 20.', 'It will say 20 things.'],
         src=['If “repeat 3” becomes “repeat 5”, how many things will it say?']),

    dict(id='4a', tier='core', no='4(a)', type='number', strand=CT, skill='counting pairs', answer=21,
         q='Seven friends meet. Every pair of friends shakes hands once. How many handshakes are there?', check=lambda: handshakes(7),
         hint='Friend 1 shakes hands with 6 friends. Friend 2 has already shaken hands with friend 1: how many new handshakes does friend 2 make?',
         steps=['Friend 1 shakes hands with the other 6 friends.', 'Friend 2 has already shaken hands with friend 1, so makes 5 new handshakes. Then 4, 3, 2, 1 new ones.', '6 + 5 + 4 + 3 + 2 + 1 = 21 handshakes.'],
         src=['Seven friends meet. Every pair of friends shakes hands once.']),
    dict(id='4b', tier='core', no='4(b)', type='selfcheck', strand=CT, skill='avoiding double counting',
         q='Ali says, “7 × 6 = 42 handshakes.” What is wrong? Fix it. Write what is wrong and the right number of handshakes, then check yourself against the worked solution.',
         facts=dict(ali=42, right=21, twice=True), check=lambda: dict(ali=7 * 6, right=handshakes(7), twice=(7 * 6 == 2 * handshakes(7))),
         hint='Look at the handshake between friend 1 and friend 2. How many times does 7 × 6 count it?',
         steps=['Each of the 7 friends shakes hands with 6 others, so 7 × 6 = 42 counts every handshake twice: once for each of the two friends in it.', 'Fix: halve it. 42 ÷ 2 = 21 handshakes.', 'This is the same as 6 + 5 + 4 + 3 + 2 + 1 = 21.'],
         src=['Ali says, “7 × 6 = 42 handshakes.” What is wrong? Fix it.']),

    dict(id='5r1', tier='core', no='Bonus 5 row 1', type='fields', strand=CT, skill='adding as you go (grid routes)', svg=grid_fig(), label='Bonus 5 r1',
         q='Bonus question: routes on a grid. Walk along the lines from A to B, going only right or up. The number in each circle is the number of routes from A to it. A gets 1. '
           'Each other circle = the number on its left + the number below it (a missing neighbour counts as 0). Ignore the puddle P for now. '
           'The bottom row, the row of A, is 1, 1, 1, 1. Fill in the next row up.',
         frame='Next row up, left to right: 1, {f1}, {f2}, {f3}', answer=[ROUTES_A[(x, 1)] for x in (1, 2, 3)],
         check=lambda: [W.corner_counts(3)[(x, 1)] for x in (1, 2, 3)],
         hint='Each circle = the circle on its left + the circle below it. Start at the left of this row.',
         steps=['The circle one along and one up has 1 on its left and 1 below it: 1 + 1 = 2.', 'The next one has 2 on its left and 1 below: 2 + 1 = 3.', 'The next one has 3 on its left and 1 below: 3 + 1 = 4.', 'The row is 1, 2, 3, 4.'],
         src=['Write in each circle the number of routes from A to it.']),
    dict(id='5r2', tier='core', no='Bonus 5 row 2', type='fields', strand=CT, skill='adding as you go (grid routes)', svg=grid_fig(), label='Bonus 5 r2',
         q='Bonus question: routes on a grid. Each circle = the number on its left + the number below it. Ignore the puddle P for now. The bottom row is 1, 1, 1, 1. Fill in the row two up from the bottom.',
         frame='Row two up, left to right: 1, {f1}, {f2}, {f3}', answer=[ROUTES_A[(x, 2)] for x in (1, 2, 3)],
         check=lambda: [W.corner_counts(3)[(x, 2)] for x in (1, 2, 3)],
         hint='You need the row below this one first. Then each circle = its left neighbour + the circle below it.',
         steps=['The row below is 1, 2, 3, 4. The left circle of this row is 1.', 'Next: 1 on its left + 2 below = 3. Next: 3 + 3 = 6. Next: 6 + 4 = 10.', 'The row is 1, 3, 6, 10.'],
         src=['Write in each circle the number of routes from A to it.']),
    dict(id='5r3', tier='core', no='Bonus 5 row 3', type='fields', strand=CT, skill='adding as you go (grid routes)', svg=grid_fig(), label='Bonus 5 r3',
         q='Bonus question: routes on a grid. Each circle = the number on its left + the number below it. Ignore the puddle P for now. Fill in the top row, except for B.',
         frame='Top row, left to right: 1, {f1}, {f2}, then B', answer=[ROUTES_A[(1, 3)], ROUTES_A[(2, 3)]],
         check=lambda: [W.corner_counts(3)[(x, 3)] for x in (1, 2)],
         hint='Work up the grid one row at a time. Each circle = its left neighbour + the circle below it.',
         steps=['The row below is 1, 3, 6, 10. The left circle of the top row is 1.', 'Next: 1 on its left + 3 below = 4. Next: 4 + 6 = 10.', 'Then B is 10 + 10, which is the answer to 5(a).'],
         src=['Write in each circle the number of routes from A to it.']),
    dict(id='5a', tier='core', no='Bonus 5(a)', type='number', strand=CT, skill='adding as you go (grid routes)', answer=20, svg=grid_fig(), label='Bonus 5(a)',
         q='Bonus question: routes on a grid. Going only right or up, how many routes go from A to B? (Ignore the puddle P for now.)',
         check=lambda: W.routes(3, 3),
         hint='Write the number of routes in each circle, row by row, starting at A.',
         steps=['The circles hold: bottom row 1, 1, 1, 1; next 1, 2, 3, 4; next 1, 3, 6, 10; top 1, 4, 10, and B.', 'B = 10 + 10 = 20.', 'There are 20 routes from A to B.'],
         sol_fig=lambda f: W.routes_fig(3, (), 'The number of routes from A to every circle: bottom row 1, 1, 1, 1; then 1, 2, 3, 4; then 1, 3, 6, 10; top row 1, 4, 10, 20 at B'),
         src=['How many routes go from A to B?']),
    dict(id='5b', tier='core', no='Bonus 5(b)', type='number', strand=CT, skill='counting routes that avoid a point', answer=8, svg=grid_fig(), label='Bonus 5(b)',
         q='Bonus question: routes on a grid. A puddle covers the hatched circle marked P. Do it again with 0 at P. How many routes avoid P?',
         check=lambda: W.routes(3, 3, [(1, 1)]),
         hint='Put 0 in the circle P. Then work out the circles to its right and above it again. Which circles do not change?',
         steps=['Put 0 at P. The rest of the bottom row and the left column stay 1.', 'Next row up: 1, 0, 1, 2. Row above: 1, 1, 2, 4. Top row: 1, 2, 4, 8.', 'So 8 routes avoid the puddle. (The other 12 routes go through P.)'],
         sol_fig=lambda f: W.routes_fig(3, [(1, 1)], 'The number of routes from A to every circle with 0 at P: bottom row 1, 1, 1, 1; then 1, 0, 1, 2; then 1, 1, 2, 4; top row 1, 2, 4, 8 at B'),
         src=['A puddle covers the hatched circle marked P. Do it again with 0 at P. How many routes avoid P?']),

    dict(id='6-gaps', tier='core', no='6 repeats', type='fields', strand=CO, skill='planning nested loops', svg=plan_fig(), label='6 repeats',
         q='Plan your code. Fill the 3 gaps so it counts the handshakes of the 7 friends in Q4. The variables a and b are friend numbers. First, the two repeats: how many times does each go round?',
         frame='First repeat (outside): {f1}   second repeat (inside it): {f2}', answer=[7, 7],
         check=lambda: [loop_needed(7), loop_needed(7)] if cond_works('a < b') else None,
         hint='a is the first friend of a pair and b is the second. Which friends must each loop visit?',
         steps=['Both a and b must be able to be any of the 7 friends, so each loop repeats 7 times.', 'The outside loop sets a to 1, 2, ... 7. The inside loop sets b to 1, 2, ... 7 for each a.'],
         src=['Plan your code. Fill the 3 gaps so it counts the handshakes of the 7 friends in Q4.']),
    dict(id='6-test', tier='core', no='6 test', type='text', strand=CO, skill='planning nested loops', svg=plan_fig(), label='6 test',
         q='Plan your code. Fill the 3 gaps so it counts the handshakes of the 7 friends in Q4. A handshake between friend 2 and friend 5 is the same as one between 5 and 2, so count each pair once. '
           'Type the test for the last gap, the one after "if". (Type it like this: a + b = 10, which is a different test.)',
         accept=COND_OK, shown='a < b', check=lambda: COND_OK[0] if all(cond_works(c) for c in COND_OK) and not cond_works('a = b') and not cond_works('a <= b') else None,
         hint='Which test lets the pair (2, 5) through but not (5, 2)?',
         steps=['The test must be true for (2, 5) and false for (5, 2), so each pair is counted once.', 'a < b works. (a > b works too.)', 'The program then counts the pairs with a smaller than b: 21.'],
         src=['Plan your code. Fill the 3 gaps so it counts the handshakes of the 7 friends in Q4.']),
    dict(id='6a', tier='core', no='6(a)', type='number', strand=CO, skill='predicting what code says', answer=21, svg=plan_fig(),
         q='Plan your code. With the 3 gaps filled in correctly, what will the program say at the end?', check=lambda: W.run(W.fill(PLAN, [7, 7, 'a < b']))[0][-1],
         hint='The program adds 1 to count for each pair it keeps. How many pairs does it keep?',
         steps=['The program counts each pair of friends once.', 'That is the number of handshakes from Q4(a).', 'It says 21.'],
         src=['What will the program say?']),
    dict(id='6agree', tier='core', no='6(a) agree', type='choice', strand=CO, skill='checking an answer another way', options=['Yes', 'No'], answer='Yes', svg=plan_fig(),
         q='Plan your code. Does the answer of the finished program agree with your answer to Q4(a)?',
         check=lambda: 'Yes' if W.run(W.fill(PLAN, [7, 7, 'a < b']))[0][-1] == handshakes(7) else 'No', label='6(a) agree',
         hint='Compare the number of pairs the program counts with the number of handshakes of 7 friends.',
         steps=['Both count every pair of friends once.', 'So the program and Q4(a) give the same answer.'],
         src=['Does it agree with Q4(a)?']),
    dict(id='6b', tier='core', no='6(b)', type='number', strand=CO, skill='changing a test', answer=7, svg=plan_fig(),
         q='Plan your code. If the test is changed to a = b, what will the program say?', check=lambda: W.run(W.fill(PLAN, [7, 7, 'a = b']))[0][-1],
         hint='When is a equal to b? Write down the pairs (a, b) that pass this test.',
         steps=['The pairs that pass are (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6) and (7, 7).', 'That is 7 pairs.', 'The program says 7.'],
         src=['If the test is changed to']),
    dict(id='6b-why', tier='core', no='6(b) what', type='selfcheck', strand=CO, skill='explaining what code counts', svg=plan_fig(), label='6(b) what',
         q='Plan your code. With the test a = b, what is it counting now? Write your answer, then check it against the worked solution.',
         facts=dict(count=7), check=lambda: dict(count=len([(a, b) for a in range(1, 8) for b in range(1, 8) if a == b])),
         hint='Which pairs (a, b) pass the test a = b? What do those pairs have in common?',
         steps=['It counts the pairs where a and b are the same friend: (1, 1), (2, 2), ... (7, 7).', 'That is each friend paired with themselves, so it counts the 7 friends, not any handshakes (nobody shakes their own hand).'],
         src=['What is it counting now?']),

    dict(id='X', tier='core', no='Exit slip', type='number', strand=CT, skill='counting pairs', answer=15,
         q='Six friends meet. Every pair of friends shakes hands once. How many handshakes are there?', check=lambda: handshakes(6),
         hint='Friend 1 shakes hands with 5 friends. How many new handshakes does friend 2 make? Then friend 3?',
         steps=['Friend 1: 5 handshakes. Friend 2 (not counting friend 1): 4. Then 3, 2 and 1.', '5 + 4 + 3 + 2 + 1 = 15.', 'Or: 6 × 5 = 30 counts every handshake twice, and 30 ÷ 2 = 15.'],
         src=['Six friends meet. Every pair of friends shakes hands once.']),

    # ================= Investigation (printed on the Finish page)
    dict(id='I1', tier='invest', no='Investigation 1', type='number', strand=CT, skill='listing in order', answer=2, label='Inv 1',
         q='Find all the ways. Pay exactly 50 cents using only 5-cent, 10-cent and 20-cent coins (as many of each as you like). First step: how many ways are there to pay 50 cents that use two 20-cent coins?',
         check=lambda: len([w for w in pay(50, [20, 10, 5]) if w[0] == 2]),
         hint='Two 20-cent coins make 40 cents. How can you pay the other 10 cents with 10-cent and 5-cent coins?',
         steps=['Two 20-cent coins make 40 cents. The other 10 cents is paid with one 10-cent coin, or with two 5-cent coins.', 'So 2 ways: 20 + 20 + 10, and 20 + 20 + 5 + 5.'],
         src=['First step: list every way to pay 50 cents that uses two 20-cent coins.']),
    dict(id='I2', tier='invest', no='Investigation 2', type='number', strand=CT, skill='listing in order', answer=12, label='Inv 2',
         q='Find all the ways. Pay exactly 50 cents using only 5-cent, 10-cent and 20-cent coins (as many of each as you like). Keep an organised list. How many ways are there altogether?',
         check=lambda: len(pay(50, [20, 10, 5])),
         hint='Sort your list by the number of 20-cent coins. For each number of 20-cent coins, list the ways to pay the rest.',
         steps=['Two 20-cent coins: 2 ways.', 'One 20-cent coin (30 cents left for 10-cent and 5-cent coins): 4 ways.', 'No 20-cent coin (50 cents with 10-cent and 5-cent coins): 6 ways.', '2 + 4 + 6 = 12 ways.'],
         src=['Find ALL the ways.']),
    dict(id='I3', tier='invest', no='Investigation 3', type='number', strand=CT, skill='extending a count', answer=13, label='Inv 3',
         q='Find all the ways. Pay exactly 50 cents using 5-cent, 10-cent and 20-cent coins, and now there is also a 50-cent coin (as many of each as you like). How many ways are there now?',
         check=lambda: len(pay(50, [50, 20, 10, 5])),
         hint='Which of your ways use the new coin? What else can be paid with it?',
         steps=['The ways that do not use the 50-cent coin are the ones you already had.', 'With the 50-cent coin, one coin pays the whole 50 cents. That adds exactly 1 new way.', 'The total is now 13.'],
         src=['What if there is also a 50-cent coin?']),
    dict(id='I4', tier='invest', no='Investigation 4', type='selfcheck', strand=CT, skill='organised listing', label='Inv 4',
         q='Find all the ways to pay 50 cents with 5-cent, 10-cent and 20-cent coins. Show how you made sure you did not miss one or count one twice. Write your method (for example, what you fixed first), then check it against the worked solution.',
         facts=sorted(pay(50, [20, 10, 5]), key=lambda w: (-w[0], -w[1])), check=lambda: sorted(pay(50, [20, 10, 5]), key=lambda w: (-w[0], -w[1])),
         sol_fig=lambda f: ways_fig(f),
         hint='Fix the biggest coin first. Write all the ways for two of them, then one, then none. Is any way in your list twice?',
         steps=['An organised list: fix the number of 20-cent coins (2, then 1, then 0).', 'Then fix the number of 10-cent coins and fill the rest with 5-cent coins. Every way appears once, in order, so none is missed or repeated.', 'The 12 ways are in the table: 2 + 4 + 6.', 'A good answer says what was fixed first and checks the count (for example by adding the groups).'],
         src=['Show how you made sure you did not miss one or count one twice.']),

    # ================= Think harder (first three Think harder questions, then the one moved from Start here)
    dict(id='T1', tier='stretch', no='T1', type='number', strand=CT, skill='multiplication rule backwards', answer=5,
         q='A set lunch is 1 main, 1 drink and 1 dessert. There are 4 mains and 3 drinks. There are 60 different set lunches. How many desserts are there?',
         check=lambda: next(d for d in range(1, 100) if len(list(itertools.product(range(4), range(3), range(d)))) == 60),
         hint='How many set lunches are there with just a main and a drink? How many dessert choices go with each of them?',
         steps=['A main and a drink can be chosen in 4 × 3 = 12 ways.', 'Each of the 12 goes with every dessert, so 12 × (number of desserts) = 60.', '60 ÷ 12 = 5 desserts. (Check: 4 × 3 × 5 = 60.)'],
         src=['A set lunch is 1 main, 1 drink and 1 dessert.']),
    dict(id='T2a', tier='stretch', no='T2(a)', type='number', strand=CT, skill='counting digit numbers', answer=24,
         q='How many 3-digit numbers can you make from the cards 1, 2, 3 and 4, using each card at most once?', check=lambda: len(numbers_from([1, 2, 3, 4], 3)),
         hint='How many cards can go in the 1st place? Then in the 2nd place? Then in the 3rd place?',
         steps=['1st digit: 4 choices. 2nd digit: 3 cards left. 3rd digit: 2 cards left.', '4 × 3 × 2 = 24 numbers.'],
         src=['How many 3-digit numbers can you make from the cards 1, 2, 3 and 4, using each card at most once?']),
    dict(id='T2b', tier='stretch', no='T2(b)', type='number', strand=CT, skill='counting with a condition', answer=12,
         q='You make every 3-digit number from the cards 1, 2, 3 and 4, using each card at most once. How many of them are even?',
         check=lambda: len([n for n in numbers_from([1, 2, 3, 4], 3) if n % 2 == 0]),
         hint='An even number ends in an even digit. Choose the last digit first. Then fill the other places.',
         steps=['The last digit must be 2 or 4: 2 choices.', 'Then 3 cards are left for the 1st place and 2 cards for the 2nd place: 3 × 2.', '2 × 3 × 2 = 12 even numbers.'],
         src=['How many of them are even?']),
    dict(id='T3', tier='stretch', no='T3', type='number', strand=CT, skill='counting ordered pairs', answer=30,
         q='In a league of 6 teams, every team plays every other team twice (once at home, once away). How many matches are played?',
         check=lambda: len(list(itertools.permutations(range(6), 2))),
         hint='Choose the home team, then the away team. How many choices for each?',
         steps=['The home team can be any of the 6 teams.', 'The away team can be any of the other 5 teams.', '6 × 5 = 30 matches. (Each pair of teams plays twice: 15 pairs × 2 = 30.)'],
         src=['In a league of 6 teams, every team plays every other team twice']),
    dict(id='T4a', tier='stretch', no='T4(a)', type='number', strand=CT, skill='multiplication rule backwards', answer=2,
         q='Mei packs 4 T-shirts, 3 pairs of shorts and 2 caps. She wants at least 40 outfits with a cap. What is the fewest number of extra pairs of shorts she must buy?',
         check=lambda: next(k for k in range(0, 50) if len(list(itertools.product(range(4), range(3 + k), range(2)))) >= 40),
         hint='How many outfits does each pair of shorts make with the 4 T-shirts and the 2 caps? How many pairs of shorts does she need for 40?',
         steps=['Each pair of shorts makes 4 × 2 = 8 outfits with the T-shirts and caps.', '40 ÷ 8 = 5, so she needs at least 5 pairs of shorts. She has 3.', 'She must buy 5 − 3 = 2 more pairs. (Check: 4 × 5 × 2 = 40.)'],
         src=['She wants at least 40 outfits with a cap.']),
    dict(id='T4b', tier='stretch', no='T4(b)', type='number', strand=CT, skill='counting pairs backwards', answer=10,
         q='At a party every pair of people shakes hands once. There are 45 handshakes. How many people are there?',
         check=lambda: next(n for n in range(2, 200) if handshakes(n) == 45),
         hint='Try small parties: how many handshakes for 3 people, 4 people, 5 people? Look at how the number grows.',
         steps=['For n people the handshakes are 1 + 2 + ... + (n − 1).', '1 + 2 + ... + 9 = 45, so n − 1 = 9.', 'There are 10 people. (Check: 10 × 9 ÷ 2 = 45.)'],
         src=['A party has 45 handshakes. How many people are there?']),

    # ================= Go further (last three Go further questions)
    dict(id='C1', tier='challenge', no='C1', type='selfcheck', open=True, marking_mode='open', strand=CT, skill='making a counting puzzle',
         q='Make up your own "how many ways" puzzle whose answer is exactly 24. Write the puzzle, show how you counted, and check with a list or a tree. Write it here, then compare with the examples in the worked solution.',
         hint='Start from an idea in this lesson (outfits, digit cards, a line of children). Then choose the numbers so that the count comes to 24.',
         steps=['Open: many puzzles work. Three examples:', '4 children stand in a line: 4 × 3 × 2 × 1 = 24 orders.', '2 shirts, 3 pairs of shorts and 4 caps: 2 × 3 × 4 = 24 outfits.',
                '3-digit numbers from the cards 1, 2, 3, 4 using each card at most once: 4 × 3 × 2 = 24.', 'Check that every case is counted once, with a list or a tree.'],
         src=['Make up your own “how many ways” puzzle whose answer is exactly 24.']),
    dict(id='C2', tier='challenge', no='C2', type='number', strand=CT, skill='counting unordered pairs with repeats', answer=28,
         q='A set of dominoes has one domino for every pair of spot numbers from 0 to 6, including doubles such as 3 | 3. How many dominoes are in the set?',
         check=lambda: len(list(itertools.combinations_with_replacement(range(7), 2))),
         hint='List the dominoes in order: 0|0, 0|1, 0|2 ... Then start again from 1|1. Is 1|0 a new domino?',
         steps=['The 7 doubles: 0|0, 1|1, ..., 6|6.', 'The dominoes with two different numbers: 6 + 5 + 4 + 3 + 2 + 1 = 21 (0|1 and 1|0 are the same domino).', '7 + 21 = 28 dominoes.'],
         src=['A set of dominoes has one domino for every pair of spot numbers from 0 to 6']),
    dict(id='C3', tier='challenge', no='C3', type='number', strand=CT, skill='counting with a digit sum', answer=15,
         q='How many 3-digit numbers have digits that add up to 5? (For example, 203.)', check=lambda: len(three_digit_sum(5)),
         hint='Fix the first digit (it cannot be 0). Then list the pairs of digits for the other two places that make up the rest.',
         steps=['First digit 1: the other two digits add to 4: 5 numbers. First digit 2: add to 3: 4 numbers.', 'First digit 3: 3 numbers. First digit 4: 2 numbers. First digit 5: 1 number.', '5 + 4 + 3 + 2 + 1 = 15 numbers.'],
         src=['How many 3-digit numbers have digits that add up to 5?']),
]

# the examples in C1 and the stated facts are checked here, not trusted
assert 4 * 3 * 2 * 1 == 24 and 2 * 3 * 4 == 24 and len(numbers_from([1, 2, 3, 4], 3)) == 24
assert sorted(ROUTES_A[(x, 1)] for x in range(4)) == [1, 2, 3, 4] and ROUTES_A[(3, 3)] == 20 and [ROUTES_B[(x, 1)] for x in range(4)] == [1, 0, 1, 2]
assert [ROUTES_B[(x, 2)] for x in range(4)] == [1, 1, 2, 4] and [ROUTES_B[(x, 3)] for x in range(4)] == [1, 2, 4, 8] and ROUTES_A[(3, 3)] - ROUTES_B[(3, 3)] == 12
assert [len([w for w in pay(50, [20, 10, 5]) if w[0] == k]) for k in (2, 1, 0)] == [2, 4, 6]

for _it in ITEMS:
    if _it.get('frame'):
        _it['frame'] = W.nb(_it['frame'])

P.finish(ITEMS)

# ---------------------------------------------------------------- variant families (every combination is run against an independent oracle at build time)
VARIANTS = {
    '1b': dict(base=dict(t=4, s=3, c=2),
               tpl=dict(vars=dict(t=[3, 4, 5, 6], s=[2, 3, 4, 5], c=[2, 3, 4]),
                        q='Mei packs {t} T-shirts, {s} pairs of shorts and {c} caps for camp. An outfit is a T-shirt, a pair of shorts and a cap. How many outfits can she make?', answer='t*s*c',
                        hint='Think about the T-shirt-and-shorts outfits first. How many caps can go with each one?',
                        steps=['Each T-shirt can go with {s} pairs of shorts, so {t} T-shirts make {t} × {s} outfits of T-shirt and shorts.', 'Each of those can go with any of the {c} caps.', '{t} × {s} × {c} = {ans}.']),
               oracle=lambda e: len(list(itertools.product(range(e['t']), range(e['s']), range(e['c']))))),
    '4a': dict(base=dict(n=7),
               tpl=dict(vars=dict(n=[4, 5, 6, 8, 9, 10, 12]),
                        q='{n} friends meet. Every pair of friends shakes hands once. How many handshakes are there?', answer='n*(n-1)//2',
                        hint='Friend 1 shakes hands with all the others. Friend 2 has already shaken hands with friend 1. Keep going down the list.',
                        steps=['Friend 1 shakes hands with the other {n} - 1 friends, friend 2 makes one fewer new handshake, and so on down to 1.', '{n} × ({n} - 1) counts every handshake twice, so halve it.', 'The answer is {ans}.']),
               oracle=lambda e: handshakes(e['n'])),
    'X': dict(base=dict(n=6),
              tpl=dict(vars=dict(n=[4, 5, 6, 8, 9, 10, 11]),
                       q='{n} friends meet. Every pair of friends shakes hands once. How many handshakes are there?', answer='n*(n-1)//2',
                       hint='Friend 1 shakes hands with all the others. Friend 2 has already shaken hands with friend 1. Keep going down the list.',
                       steps=['Friend 1 shakes hands with the other {n} - 1 friends, friend 2 makes one fewer new handshake, and so on down to 1.', '{n} × ({n} - 1) counts every handshake twice, so halve it.', 'The answer is {ans}.']),
              oracle=lambda e: handshakes(e['n'])),
    'T3': dict(base=dict(n=6),
               tpl=dict(vars=dict(n=[4, 5, 6, 7, 8, 9, 10, 12]),
                        q='In a league of {n} teams, every team plays every other team twice (once at home, once away). How many matches are played?', answer='n*(n-1)',
                        hint='Choose the home team, then the away team. How many choices for each?',
                        steps=['The home team can be any of the {n} teams.', 'The away team can be any of the other {n} - 1 teams.', '{n} × ({n} - 1) = {ans} matches.']),
               oracle=lambda e: len(list(itertools.permutations(range(e['n']), 2)))),
    'C2': dict(base=dict(k=6),
               tpl=dict(vars=dict(k=[3, 4, 5, 6, 8, 9]),
                        q='A set of dominoes has one domino for every pair of spot numbers from 0 to {k}, including doubles such as 3 | 3. How many dominoes are in the set?', answer='(k+1)*(k+2)//2',
                        hint='List the dominoes in order: 0|0, 0|1, 0|2 ... Then start again from 1|1. Is 1|0 a new domino?',
                        steps=['There are {k} + 1 doubles. The dominoes with two different numbers are counted by adding {k} + ({k} - 1) + ... + 1.', 'Add the doubles and the other dominoes.', 'The answer is {ans}.']),
               oracle=lambda e: len(list(itertools.combinations_with_replacement(range(e['k'] + 1), 2)))),
}
