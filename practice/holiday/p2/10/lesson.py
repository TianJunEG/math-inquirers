"""Level 2 (P2) holiday lesson 10: PUZZLE DAY (mixed puzzles: how to start a puzzle), week 5, second lesson.  Online mirror of the printed workbook pages.

The questions are the ones printed in the Level 2 holiday workbook (p2/content/l10.js `workbook()` = Start here, p2/gaps.json lesson 10 `invest` = Investigation,
p2/content/l10.js `qbank.stretch` first four = Think harder 1 to 4, `qbank.challenge` last three = Go further 5 to 7, as built by p2/workbook_html.js, and the
"Make up your own" line).  Every answer is recomputed by an INDEPENDENT checker: the pictures of the graph, the cake and the towers are COUNTED from the drawings; the digit-card numbers
are listed by trying every order of the cards; the coin and dish puzzles by trying every number of coins and plates; the logic puzzles by trying every arrangement (exactly one fits);
the stories (the bus, the savings, the picture graph with no key) by trying numbers; the staircase by listing every way.  build_holiday.py stops if a checker and the printed answer differ.
"""
import os, sys
from fractions import Fraction as Fr
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from hlib import *          # noqa: E402,F401
from p2lib import *         # noqa: E402,F401
from p2lib_w4 import list_forms      # noqa: E402,F401
from p2lib_w5 import *      # noqa: E402,F401

STRAND = 'Mixed puzzles: graphs, numbers, money, logic, fractions and patterns'
META = dict(level=2, lesson=10, key='p2', title='Puzzle day', workbook_title='PUZZLE DAY', topic='Mixed Puzzles', strand=STRAND,
            sources=['p2/content/l10.js', 'p2/gaps.json', 'p2/workbook_html.js'],
            intro=['Stuck? Draw it, list it in order, or make a table. Then check your answer against every clue and explain why.',
                   'Some questions ask you to draw or fill in a table on paper. Do that on paper first, then check against the answer shown on screen.'])

# ---------------------------------------------------------------- figures (the picture graph and the towers are redrawn for a phone and counted back from the new drawing)
PRINTED_GRAPH = printed_fig('Picture graph of ice-creams')
DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday']
GRAPH_COUNTS = graph_counts(PRINTED_GRAPH)                                   # [4, 6, 3, 0] counted from the printed picture
KEY = int(re.search(r'=\s*(\d+)\s*ice-creams', ' '.join(re.findall(r'<text[^>]*>([^<]*)</text>', PRINTED_GRAPH))).group(1))
GRAPH = picture_graph_fig([(d, n or None) for d, n in zip(DAYS, GRAPH_COUNTS)], KEY)
assert picture_graph_counts(GRAPH)[:4] == GRAPH_COUNTS
PRINTED_TOWERS = printed_fig('Three towers of cubes. Tower 1')
TOWER_COUNTS = tower_counts(PRINTED_TOWERS)                                  # [4, 8, 12]
TOWERS = towers_fig(TOWER_COUNTS)
assert towers_read(TOWERS) == TOWER_COUNTS
CAKE = printed_fig('A cake cut into 10')
CLUES4 = clue_fig(['Ali, Mei, Siti and Ben each go to', 'school a different way: bus, MRT,', 'car or walking.', 'Clue 1: Siti lives next to the', 'school, so she walks.',
                   'Clue 2: Ben does not go by bus', 'or by car.', 'Clue 3: Mei does not go by car.'])
CLUESG6 = clue_fig(['Ali, Ben, Mei and Siti each have', 'one coin: 10¢, 20¢, 50¢ or $1.', 'Mei has more money than Ali', 'but less than Ben.', 'Ben does not have the $1 coin.'])


# ---------------------------------------------------------------- independent checkers
def thursday_pictures():
    """Pictures Thursday needs: the total minus the ice-creams of the other days, in pictures (counted from the picture)."""
    left = 90 - sum(n * KEY for n in GRAPH_COUNTS[:3])
    return next(p for p in range(0, 50) if p * KEY == left)


def digit_numbers(cards):
    return sorted({int(''.join(p)) for p in itertools.permutations(cards) if p[0] != '0'})


def coin_total(k50, n=6):
    return 50 * k50 + 20 * (n - k50)


WAYS = ['Bus', 'MRT', 'Car', 'Walk']
KIDS = ['Ali', 'Mei', 'Siti', 'Ben']
SCHOOL = assignments(KIDS, WAYS, lambda d: d['Siti'] == 'Walk' and d['Ben'] not in ('Bus', 'Car') and d['Mei'] != 'Car')
assert len(SCHOOL) == 1
SCHOOL = SCHOOL[0]

COINS = ['10¢', '20¢', '50¢', '$1']
VAL = {'10¢': 10, '20¢': 20, '50¢': 50, '$1': 100}
KIDS6 = ['Ali', 'Ben', 'Mei', 'Siti']
COINWAYS = assignments(KIDS6, COINS, lambda d: VAL[d['Mei']] > VAL[d['Ali']] and VAL[d['Mei']] < VAL[d['Ben']] and d['Ben'] != '$1')
assert len(COINWAYS) == 1
COINWAYS = COINWAYS[0]


def cake_eaten():
    n = cake_pieces(CAKE)                      # 10 pieces, counted from the picture
    ali = 3
    mei = ali + 2
    ben = n - ali - mei
    return n, ali, mei, ben


def tower_cubes(t, counts=TOWER_COUNTS):
    """Cubes in tower t by keeping the pattern going: every tower adds the same number of cubes as the one before it did."""
    step = counts[1] - counts[0]
    assert all(counts[i + 1] - counts[i] == step for i in range(len(counts) - 1))
    seq = list(counts)
    while len(seq) < t:
        seq.append(seq[-1] + step)
    return seq[t - 1]


def savings(step_mei, per_ali, days):
    """(Mei's totals, Ali's totals) after each day: Mei saves step, 2 step, 3 step ... ; Ali saves per_ali every day."""
    m, a, tm, ta = 0, 0, [], []
    for d in range(1, days + 1):
        m += step_mei * d
        a += per_ali
        tm.append(m); ta.append(a)
    return tm, ta


def first_day_ahead(step_mei, per_ali, limit=60):
    tm, ta = savings(step_mei, per_ali, limit)
    return next(d + 1 for d in range(limit) if tm[d] > ta[d])


def bus_start(now, got_on):
    """People at the start: half got off, then got_on got on, and now there are `now` (found by trying)."""
    return next(n for n in range(2, 400, 2) if n - n // 2 + got_on == now)


def key_value(f, s, more):
    """Children one picture stands for: football has f pictures, swimming s, and `more` more children chose football (found by trying)."""
    return next(k for k in range(1, 100) if (f - s) * k == more)


def dishes(total):
    return [p for p in range(0, 8) if 4 * p + 3 * (7 - p) == total]


def pattern_has(n, first=5, step=4):
    x = first
    while x < n:
        x += step
    return x == n


ITEMS = [
    # ================= Start here (workbook lesson 10, No.1 to No.6)
    dict(id='1a', tier='core', no='1(a)', label='1(a)', type='number', skill='reading a picture graph with a key', svg=GRAPH, answer=30,
         q='The picture graph shows the ice-creams a stall sold. How many ice-creams were sold on Tuesday?',
         check=lambda: GRAPH_COUNTS[1] * KEY,
         hint='Look at the key under the graph. What is one picture worth?',
         steps=['The key says each picture stands for 5 ice-creams.', 'Tuesday has 6 pictures: 5, 10, 15, 20, 25, 30. So 30 ice-creams were sold on Tuesday.'],
         src=['The picture graph shows the ice-creams a stall sold.', 'How many ice-creams were sold on Tuesday?']),
    dict(id='1b', tier='core', no='1(b) draw', label='1(b) draw', type='selfcheck', paper=True, open=False, skill='making a picture graph', svg=GRAPH,
         q='90 ice-creams were sold in the 4 days. Draw Thursday’s pictures on a copy of the graph, on paper.',
         facts=dict(pictures=5), check=lambda: dict(pictures=thursday_pictures()),
         sol_fig=lambda facts: picture_graph_fig([(d, n or None) for d, n in zip(DAYS, GRAPH_COUNTS[:3] + [facts['pictures']])], KEY),
         hint='Work out how many ice-creams were sold on Monday, Tuesday and Wednesday together. How many are left for Thursday? How many pictures is that?',
         steps=['Monday 4 pictures = 20, Tuesday 6 pictures = 30, Wednesday 3 pictures = 15 ice-creams.', '20 + 30 + 15 = 65, so Thursday sold 90 − 65 = 25 ice-creams.', '25 ice-creams is 5 pictures (25 ÷ 5 = 5). The picture shows Thursday with 5 pictures.'],
         src=['90 ice-creams were sold in the 4 days. Draw Thursday’s pictures on the graph.']),
    dict(id='1b2', tier='core', no='1(b) how many pictures', label='1(b) count', type='number', skill='reading a picture graph with a key', svg=GRAPH, answer=5,
         q='90 ice-creams were sold in the 4 days. How many pictures should Thursday have? Do the drawing question first.',
         check=lambda: thursday_pictures(),
         hint='Add up the ice-creams of the other three days. How many are left? What is one picture worth?',
         steps=['Monday, Tuesday and Wednesday sold 20 + 30 + 15 = 65 ice-creams.', 'Thursday sold 90 − 65 = 25 ice-creams. 25 ÷ 5 = 5 pictures.'],
         src=['90 ice-creams were sold in the 4 days. Draw Thursday’s pictures on the graph.']),
    dict(id='1c', tier='core', no='1(c)', label='1(c)', type='number', skill='using a picture graph with money', svg=GRAPH, answer=30,
         q='Each ice-cream costs $2. How much money did the stall get on Wednesday? Type the number of dollars.',
         check=lambda: GRAPH_COUNTS[2] * KEY * 2,
         hint='First find how many ice-creams were sold on Wednesday. Then think about the money.',
         steps=['Wednesday has 3 pictures: 3 × 5 = 15 ice-creams.', '15 ice-creams at $2 each: 15 × 2 = $30.'],
         src=['Each ice-cream costs $2. How much did the stall get on Wednesday?']),

    dict(id='2a', tier='core', no='2(a)', label='2(a)', type='set', ordered=True, skill='listing numbers in order', answer=[308, 380, 803, 830],
         q='Use the digit cards 3, 0 and 8 once each to make a 3-digit number. Type ALL the numbers you can make, in order, from the smallest to the greatest.',
         check=lambda: digit_numbers('308'),
         hint='Choose the hundreds digit first: a 3-digit number cannot start with 0. Then swap the other two cards.',
         steps=['Hundreds digit 3: 308 and 380. Hundreds digit 8: 803 and 830.', 'A number cannot start with 0, so no number has 0 as its hundreds digit.', 'In order: 308, 380, 803, 830.'],
         src=['Use the digit cards  3,  0  and  8  once each to make a 3-digit number.'.replace('  ', ' '), 'List ALL the numbers in order.']),
    dict(id='2b', tier='core', no='2(b)', label='2(b)', type='fields', skill='greatest and smallest number from digit cards', answer=[830, 308],
         q='Use the digit cards 3, 0 and 8 once each to make 3-digit numbers. What is the greatest number? What is the smallest?',
         frame='Greatest {f1}   Smallest {f2}', check=lambda: [digit_numbers('308')[-1], digit_numbers('308')[0]],
         hint='Think about which digit goes in the hundreds place first. A 3-digit number cannot start with 0.',
         steps=['The greatest number has the biggest digit in the hundreds place: 830.', 'The smallest number cannot start with 0, so it starts with 3: 308.'],
         src=['Use the digit cards 3, 0 and 8 once each to make a 3-digit number.', 'Greatest', 'Smallest']),
    dict(id='2c', tier='core', no='2(c)', label='2(c)', type='set', ordered=False, skill='numbers between two numbers', answer=[308, 380, 803],
         q='Which of the 3-digit numbers made with the digit cards 3, 0 and 8 are between 300 and 810? Type them with commas.',
         check=lambda: [n for n in digit_numbers('308') if 300 < n < 810],
         hint='Make all the numbers first. Then check each one: is it more than 300 and less than 810?',
         steps=['The numbers are 308, 380, 803 and 830.', '830 is more than 810, so it is not between 300 and 810.', '308, 380 and 803 are between 300 and 810.'],
         src=['Which of them are between 300 and 810?']),

    dict(id='3a', tier='core', no='3 table', label='3 table', type='set', ordered=True, skill='making a table of coins', answer=[150, 180, 210],
         q='Ben has 6 coins, all 50¢ and 20¢ coins. With 0 fifty-cent coins the total is 120¢ (six 20¢ coins). Find the total, in cents, with 1, 2 and 3 fifty-cent coins (still 6 coins in all). Type three numbers.',
         check=lambda: [coin_total(k) for k in (1, 2, 3)],
         hint='Each time you swap a 20¢ coin for a 50¢ coin, how much does the total change? Make the table one row at a time.',
         steps=['1 fifty-cent coin and 5 twenty-cent coins: 50 + 100 = 150¢.', '2 fifty-cent coins and 4 twenty-cent coins: 100 + 80 = 180¢.', '3 fifty-cent coins and 3 twenty-cent coins: 150 + 60 = 210¢.'],
         src=['Ben has 6 coins. They are all 50¢ and 20¢ coins. Together they are worth $1.80. How many of each coin does he have? Make a table.']),
    dict(id='3b', tier='core', no='3 how many of each', label='3 coins', type='fields', skill='making a table of coins', answer=[2, 4],
         q='Ben has 6 coins. They are all 50¢ and 20¢ coins. Together they are worth $1.80. How many of each coin does he have?',
         frame='50¢ coins {f1}   20¢ coins {f2}', check=lambda: next([k, 6 - k] for k in range(0, 7) if coin_total(k) == 180),
         hint='Make a table: the number of 50¢ coins, the number of 20¢ coins, and the total. Start with 0 fifty-cent coins and go up one at a time until the total is $1.80.',
         steps=['0 fifty-cent coins: 120¢. 1: 150¢. 2: 180¢. That is $1.80.', 'So Ben has 2 fifty-cent coins and 4 twenty-cent coins. Check: 100¢ + 80¢ = 180¢.'],
         src=['Ben has 6 coins. They are all 50¢ and 20¢ coins. Together they are worth $1.80. How many of each coin does he have? Make a table.']),
]


def _logic_cards(prefix, fig, kids, truth, options, stem, hints, steps, srcs):
    out = []
    for kid in kids:
        out.append(dict(id=f'{prefix}{kid[0].lower()}{kid[1:3]}', tier='core', no=f'{prefix} {kid}', label=f'{prefix} {kid}', type='choice', options=list(options), answer=truth[kid],
                        skill='logic: using clues one at a time', svg=fig, q=stem.format(kid=kid), check=(lambda k=kid: truth[k]), hint=hints[kid], steps=list(steps), src=list(srcs)))
    return out


ITEMS += _logic_cards('4', CLUES4, KIDS, SCHOOL, WAYS, 'Use the clues in the picture. How does {kid} go to school?',
                      dict(Ali='Rule out what the other children cannot do. Start with the clue that tells you a way for sure.', Mei='Clue 3 rules out one way for Mei. Siti already goes one way: that way is not left for Mei either.',
                           Siti='Read clue 1.', Ben='Clue 2 rules out two ways for Ben. Siti already goes one way. What is left?'),
                      ['Clue 1: Siti walks.', 'Clue 2: Ben does not go by bus or by car, and Siti has the walk, so Ben goes by MRT.', 'Clue 3: Mei does not go by car, and the walk and the MRT are taken, so Mei goes by bus.', 'Ali is left with the car. Check: Ali car, Mei bus, Siti walks, Ben MRT: all three clues are true.'],
                      ['Ali, Mei, Siti and Ben each go to school a different way: bus, MRT, car or walking.', 'Clue 1: Siti lives next to the school, so she walks.', 'Clue 2: Ben does not go by bus or by car.', 'Clue 3: Mei does not go by car.'])

ITEMS += [
    dict(id='5a', tier='core', no='5(a)', label='5(a)', type='fields', skill='fractions of a cake', svg=CAKE, answer=[5, 10],
         q='A cake is cut into 10 equal pieces. Ali eats 3/10 of the cake. Mei eats 2 more pieces than Ali. Ben eats the rest. What fraction of the cake does Mei eat? Type it, top number first.',
         frame='{f1}/{f2} of the cake', check=lambda: [cake_eaten()[2], cake_eaten()[0]],
         hint='Ali eats 3 pieces. Mei eats 2 more pieces than that. How many pieces is that, out of 10?',
         steps=['Ali eats 3 pieces. Mei eats 2 more pieces: 3 + 2 = 5 pieces.', 'Mei eats 5 pieces out of 10: 5/10 of the cake.'],
         src=['A cake is cut into 10 equal pieces. Ali eats 3/10 of the cake. Mei eats 2 more pieces than Ali. Ben eats the rest.', 'What fraction of the cake does Mei eat?']),
    dict(id='5b', tier='core', no='5(b)', label='5(b)', type='fields', skill='fractions of a cake', svg=CAKE, answer=[2, 10],
         q='A cake is cut into 10 equal pieces. Ali eats 3/10 of the cake. Mei eats 2 more pieces than Ali. Ben eats the rest. What fraction of the cake does Ben eat? Type it, top number first.',
         frame='{f1}/{f2} of the cake', check=lambda: [cake_eaten()[3], cake_eaten()[0]],
         hint='Count the pieces Ali and Mei eat together. How many of the 10 pieces are left for Ben?',
         steps=['Ali eats 3 pieces and Mei eats 3 + 2 pieces, so together they eat 3 + 5 = 8 pieces.', '10 − 8 = 2 pieces are left for Ben: 2/10 of the cake.'],
         src=['A cake is cut into 10 equal pieces. Ali eats 3/10 of the cake. Mei eats 2 more pieces than Ali. Ben eats the rest.', 'What fraction of the cake does Ben eat?']),
    dict(id='5c', tier='core', no='5(c)', label='5(c)', type='text', skill='ordering fractions of a cake', svg=CAKE, accept=list_forms(['Mei', 'Ali', 'Ben']), shown='Mei, Ali, Ben', equiv_frac=False,
         q='A cake is cut into 10 equal pieces. Ali eats 3/10 of the cake. Mei eats 2 more pieces than Ali. Ben eats the rest. Order the children, the one who eats the most first. Type the three names with commas.',
         check=lambda: ', '.join(n for n, _ in sorted((('Ali', cake_eaten()[1]), ('Mei', cake_eaten()[2]), ('Ben', cake_eaten()[3])), key=lambda p: -p[1])),
         hint='Find how many pieces each child eats. Then put the child with the most pieces first.',
         steps=['Ali eats 3 pieces, Mei eats 5 pieces and Ben eats 2 pieces.', '5 is the most, then 3, then 2: Mei, Ali, Ben.'],
         src=['A cake is cut into 10 equal pieces. Ali eats 3/10 of the cake. Mei eats 2 more pieces than Ali. Ben eats the rest.', 'Order the children, the one who eats the most first.']),

    dict(id='6a', tier='core', no='6 table', label='6 table', type='set', ordered=True, skill='growing patterns', svg=TOWERS, answer=[16, 20, 24],
         q='Ben builds towers with cubes. Tower 1 has 4 cubes, Tower 2 has 8 cubes and Tower 3 has 12 cubes. Keep the pattern going. How many cubes are in Towers 4, 5 and 6? Type three numbers.',
         check=lambda: [tower_cubes(t) for t in (4, 5, 6)],
         hint='How many more cubes does each tower have than the one before it? Keep adding that many.',
         steps=['Each tower has 4 more cubes than the tower before it: 4, 8, 12, 16, 20, 24.', 'Towers 4, 5 and 6 have 16, 20 and 24 cubes.'],
         src=['Ben builds towers with cubes. Tower 1 has 4 cubes, Tower 2 has 8 cubes and Tower 3 has 12 cubes. Keep the pattern going.']),
    dict(id='6b', tier='core', no='6(a)', label='6(a)', type='number', skill='growing patterns', svg=TOWERS, answer=32,
         q='Ben builds towers with cubes. Tower 1 has 4 cubes, Tower 2 has 8 cubes and Tower 3 has 12 cubes. Keep the pattern going. How many cubes are in Tower 8?',
         check=lambda: tower_cubes(8),
         hint='Keep adding the same number of cubes for each new tower, or look for a shortcut with the 4 times table.',
         steps=['Each tower adds 4 cubes: 4, 8, 12, 16, 20, 24, 28, 32.', 'Tower 8 has 32 cubes (the same as 4 × 8).'],
         src=['Ben builds towers with cubes. Tower 1 has 4 cubes, Tower 2 has 8 cubes and Tower 3 has 12 cubes. Keep the pattern going.', 'How many cubes are in Tower 8?']),
    dict(id='6c', tier='core', no='6(b)', label='6(b)', type='number', skill='growing patterns', svg=TOWERS, answer=9,
         q='Ben builds towers with cubes. Tower 1 has 4 cubes, Tower 2 has 8 cubes and Tower 3 has 12 cubes. Keep the pattern going. Which tower has 36 cubes? Type the tower number.',
         check=lambda: next(t for t in range(1, 60) if tower_cubes(t) == 36),
         hint='Keep the pattern going until you reach 36 cubes. Which tower is that?',
         steps=['The towers have 4, 8, 12, 16, 20, 24, 28, 32, 36 cubes.', '36 is the 9th number, so Tower 9 has 36 cubes (4 × 9 = 36).'],
         src=['Ben builds towers with cubes. Tower 1 has 4 cubes, Tower 2 has 8 cubes and Tower 3 has 12 cubes. Keep the pattern going.', 'Which tower has 36 cubes?']),

    # ================= Investigation: Staircase
    dict(id='I1', tier='invest', no='Investigation (a) list', label='Inv 1', type='selfcheck', open=False, skill='listing all the ways in order',
         q='Staircase. Mei climbs a staircase. She can take 1 step or 2 steps at a time. For 3 steps there are 3 ways: 1+1+1, 1+2 and 2+1. Write ALL the ways for 4 steps in the box.',
         facts=dict(ways=ways_text(stair_ways(4))), check=lambda: dict(ways=ways_text(stair_ways(4))),
         hint='Easy first step: draw 3 steps and show the 3 ways. For 4 steps, list the ways in order: start with the way that uses only 1 steps, then swap in a 2.',
         steps=['Example: ' + ways_text(stair_ways(4)) + '.', 'Going in order (all 1s first, then moving a 2 along) makes sure no way is missed or counted twice.'],
         src=['Mei climbs a staircase. She can take 1 step or 2 steps at a time. For 3 steps there are 3 ways: 1+1+1, 1+2 and 2+1.', '(a) Find ALL the ways for 4 steps.']),
    dict(id='I2', tier='invest', no='Investigation (a)', label='Inv 2', type='number', skill='counting all the ways', answer=5,
         q='Mei can take 1 step or 2 steps at a time. How many different ways are there to climb 4 steps? Do the list question first.',
         check=lambda: len(stair_ways(4)),
         hint='Count the ways in your list. Did you write any way twice?',
         steps=['The ways are ' + ways_text(stair_ways(4)) + '.', 'That is 5 ways.'],
         src=['(a) Find ALL the ways for 4 steps.']),
    dict(id='I3', tier='invest', no='Investigation (b) list', label='Inv 3', type='selfcheck', open=False, skill='listing all the ways in order',
         q='Mei can take 1 step or 2 steps at a time. Write ALL the ways to climb 5 steps in the box.',
         facts=dict(ways=ways_text(stair_ways(5))), check=lambda: dict(ways=ways_text(stair_ways(5))),
         hint='Go in order, as you did for 4 steps: start with the way that uses only 1 steps, then swap in a 2.',
         steps=['Example: ' + ways_text(stair_ways(5)) + '.', 'Working in order makes sure no way is missed or counted twice.'],
         src=['(b) Find ALL the ways for 5 steps.']),
    dict(id='I4', tier='invest', no='Investigation (b)', label='Inv 4', type='number', skill='counting all the ways', answer=8,
         q='Mei can take 1 step or 2 steps at a time. How many different ways are there to climb 5 steps? Do the list question first.',
         check=lambda: len(stair_ways(5)),
         hint='Count the ways in your list. Did you write any way twice?',
         steps=['The ways are ' + ways_text(stair_ways(5)) + '.', 'That is 8 ways.'],
         src=['(b) Find ALL the ways for 5 steps.']),
    dict(id='I5', tier='invest', no='Investigation (c) table', label='Inv 5', type='set', ordered=True, grouped=False, skill='making a table of ways', answer=[1, 2, 3, 5, 8],
         q='Mei can take 1 step or 2 steps at a time. Fill in a table: how many ways are there for 1 step, 2 steps, 3 steps, 4 steps and 5 steps? Type the five numbers in order.',
         check=lambda: [len(stair_ways(n)) for n in range(1, 6)],
         hint='For 3 steps there are 3 ways (it is in the question). Use your lists for 4 steps and 5 steps. What about 1 step and 2 steps?',
         steps=['1 step: 1 way. 2 steps: 1+1 and 2, so 2 ways. 3 steps: 3 ways.', '4 steps: 5 ways. 5 steps: 8 ways.'],
         src=['(c) Fill in a table for 1, 2, 3, 4 and 5 steps. What pattern do you see? Can you guess the number of ways for 6 steps?']),
    dict(id='I6', tier='invest', no='Investigation (c) pattern', label='Inv 6', type='selfcheck', open=False, skill='noticing a pattern',
         q='Look at your table of the number of ways for 1, 2, 3, 4 and 5 steps. What pattern do you see? Write your idea in the box.',
         facts=dict(each_is_sum_of_the_two_before=True),
         check=lambda: dict(each_is_sum_of_the_two_before=all(len(stair_ways(n)) == len(stair_ways(n - 1)) + len(stair_ways(n - 2)) for n in range(3, 8))),
         hint='Look at how each number in the table is made from the numbers before it. Try adding.',
         steps=['Example: each number is the sum of the two numbers before it: 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8.', 'Any idea that notices how the numbers grow is good.'],
         src=['(c) Fill in a table for 1, 2, 3, 4 and 5 steps. What pattern do you see? Can you guess the number of ways for 6 steps?']),
    dict(id='I7', tier='invest', no='Investigation (c) guess', label='Inv 7', type='number', skill='using a pattern to predict', answer=13,
         q='Mei can take 1 step or 2 steps at a time. Use the pattern in your table to work out how many ways there are for 6 steps.',
         check=lambda: len(stair_ways(6)),
         hint='Look at how each number in your table is made from the numbers before it. Use the same idea for 6 steps.',
         steps=['Each number is the sum of the two before it: 5 + 8 = 13.', 'So there are 13 ways to climb 6 steps. (Listing every way for 6 steps also gives 13.)'],
         src=['(c) Fill in a table for 1, 2, 3, 4 and 5 steps. What pattern do you see? Can you guess the number of ways for 6 steps?']),

    # ================= Think harder
    dict(id='T1', tier='stretch', no='Think harder 1', label='T1', type='number', skill='reading a picture graph with a key', answer=1,
         q='30 children chose a fruit. In the picture graph each picture stands for 5 children. Apple has 2 pictures and banana has 3 pictures. The mango row is missing. How many pictures should the mango row have?',
         check=lambda: next(p for p in range(0, 20) if 5 * (2 + 3 + p) == 30),
         hint='How many children are in the apple row and the banana row together? How many of the 30 children are left for mango?',
         steps=['Apple: 2 × 5 = 10 children. Banana: 3 × 5 = 15 children.', '10 + 15 = 25, so 30 − 25 = 5 children chose mango.', '5 children is 1 picture.'],
         src=['30 children chose a fruit. In the picture graph each picture stands for 5 children. Apple has 2 pictures and banana has 3 pictures. The mango row is missing. How many pictures should the mango row have?']),
    dict(id='T2a', tier='stretch', no='Think harder 2 (Mei)', label='T2 Mei', type='set', ordered=True, skill='making a table of savings', answer=[3, 9, 18, 30, 45, 63, 84],
         q='Mei saves $3 on day 1, $6 on day 2, $9 on day 3, and so on. How much has she saved altogether after each of days 1 to 7? Type the seven totals in dollars.',
         check=lambda: savings(3, 10, 7)[0],
         hint='Make a table. Add each day’s saving to the total of the day before.',
         steps=['Day 1: $3. Day 2: 3 + 6 = $9. Day 3: 9 + 9 = $18. Day 4: 18 + 12 = $30.', 'Day 5: 30 + 15 = $45. Day 6: 45 + 18 = $63. Day 7: 63 + 21 = $84.'],
         src=['Mei saves $3 on day 1, $6 on day 2, $9 on day 3, and so on ($3 more each day). Ali saves $10 every day. Make a table of how much each child has saved altogether after each day. On which day does Mei FIRST have more than Ali?']),
    dict(id='T2b', tier='stretch', no='Think harder 2 (Ali)', label='T2 Ali', type='set', ordered=True, skill='making a table of savings', answer=[10, 20, 30, 40, 50, 60, 70],
         q='Ali saves $10 every day. How much has he saved altogether after each of days 1 to 7? Type the seven totals in dollars.',
         check=lambda: savings(3, 10, 7)[1],
         hint='Make a table. Add $10 to the total of the day before.',
         steps=['Ali saves $10 every day: $10, $20, $30, $40, $50, $60, $70.'],
         src=['Mei saves $3 on day 1, $6 on day 2, $9 on day 3, and so on ($3 more each day). Ali saves $10 every day. Make a table of how much each child has saved altogether after each day. On which day does Mei FIRST have more than Ali?']),
    dict(id='T2c', tier='stretch', no='Think harder 2 (which day)', label='T2 day', type='number', skill='comparing two tables', answer=6,
         q='Mei saves $3 on day 1, $6 on day 2, $9 on day 3, and so on ($3 more each day). Ali saves $10 every day. On which day does Mei FIRST have more than Ali altogether? Type the day number.',
         check=lambda: first_day_ahead(3, 10),
         hint='Make a table of what each child has saved altogether after each day. Look for the first day when Mei’s total is bigger than Ali’s.',
         steps=['Mei’s totals: $3, $9, $18, $30, $45, $63. Ali’s totals: $10, $20, $30, $40, $50, $60.', 'On day 5 Mei has $45 and Ali has $50, so Mei is still behind. On day 6 Mei has $63 and Ali has $60.', 'Mei first has more than Ali on day 6.'],
         src=['Mei saves $3 on day 1, $6 on day 2, $9 on day 3, and so on ($3 more each day). Ali saves $10 every day. Make a table of how much each child has saved altogether after each day. On which day does Mei FIRST have more than Ali?']),
    dict(id='T3', tier='stretch', no='Think harder 3', label='T3', type='number', skill='working backwards with a bar', answer=16,
         q='A bus had some people on it. At the first stop half of the people got off. At the second stop 6 people got on. Now there are 14 people on the bus. How many people were on the bus at the start?',
         check=lambda: bus_start(14, 6),
         hint='Draw a bar on paper if it helps. Work backwards from 14: first undo the people who got on at the second stop. What is left is half of the start.',
         steps=['At the second stop 6 people got on, so before that there were 14 − 6 = 8 people.', '8 people is what was left after half got off, so 8 is half of the start.', '8 + 8 = 16 people were on the bus at the start. Check: half of 16 is 8, 8 + 6 = 14.'],
         src=['A bus had some people on it. At the first stop half of the people got off. At the second stop 6 people got on. Now there are 14 people on the bus. How many people were on the bus at the start? Draw a bar to start.']),
    dict(id='T4a', tier='stretch', no='Think harder 4 (49)', label='T4 49', type='choice', options=['Yes', 'No'], answer='Yes', skill='number patterns',
         q='Look at the pattern 5, 9, 13, 17, ... Will 49 be in this pattern?',
         check=lambda: 'Yes' if pattern_has(49) else 'No',
         hint='What is added each time? Keep going, or look for a shortcut with a times table.',
         steps=['The pattern adds 4 each time: 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, ...', '49 is in the list, so 49 will be in the pattern.'],
         src=['5, 9, 13, 17, … Will 49 be in this pattern? Will 50? How do you know?']),
    dict(id='T4b', tier='stretch', no='Think harder 4 (50)', label='T4 50', type='choice', options=['Yes', 'No'], answer='No', skill='number patterns',
         q='Look at the pattern 5, 9, 13, 17, ... Will 50 be in this pattern?',
         check=lambda: 'Yes' if pattern_has(50) else 'No',
         hint='What is added each time? Keep going, or look for a shortcut with a times table.',
         steps=['The pattern adds 4 each time: ..., 41, 45, 49, 53, ...', '49 and then 53: the pattern jumps over 50, so 50 will not be in the pattern.'],
         src=['5, 9, 13, 17, … Will 49 be in this pattern? Will 50? How do you know?']),
    dict(id='T4c', tier='stretch', no='Think harder 4 explain', label='T4 why', type='selfcheck', open=False, skill='explaining a number pattern',
         q='Look at the pattern 5, 9, 13, 17, ... Explain how you can tell whether a number is in this pattern. Write your idea in the box.',
         facts=dict(in_pattern=[pattern_has(49), pattern_has(50)]), check=lambda: dict(in_pattern=[pattern_has(49), pattern_has(50)]),
         hint='What is added each time? What do you notice about each number in the pattern when you compare it with the 4 times table?',
         steps=['Example: every number in the pattern is 1 more than a number in the 4 times table: 5 = 4 + 1, 9 = 8 + 1, 13 = 12 + 1.', '49 = 48 + 1, and 48 is in the 4 times table, so 49 is in the pattern. 50 is 2 more than 48, so it is not.', 'Any idea that follows the pattern is good.'],
         src=['5, 9, 13, 17, … Will 49 be in this pattern? Will 50? How do you know?']),

    # ================= Go further
    dict(id='C5', tier='challenge', no='Go further 5', label='G5', type='fields', skill='picture graph with no key', answer=[20, 30],
         q='A picture graph has lost its key. Football has 6 pictures and swimming has 4 pictures. 10 more children chose football than swimming. How many children chose swimming? How many chose football?',
         frame='Swimming {f1}   Football {f2}', check=lambda: (lambda k: [4 * k, 6 * k])(key_value(6, 4, 10)),
         hint='How many more pictures does football have than swimming? Those pictures stand for 10 children. What is one picture worth?',
         steps=['Football has 6 − 4 = 2 more pictures than swimming, and these 2 pictures are 10 children.', 'So 1 picture is 10 ÷ 2 = 5 children.', 'Swimming: 4 × 5 = 20 children. Football: 6 × 5 = 30 children (30 − 20 = 10 more).'],
         src=['A picture graph has lost its key. Football has 6 pictures and swimming has 4 pictures. 10 more children chose football than swimming. How many children chose swimming? Football?']),
    dict(id='C6', tier='challenge', no='Go further 6', label='G6', type='fields', skill='logic: ordering coins', svg=CLUESG6, answer=[10, 50, 20, 100],
         q='Use the clues in the picture. Who has which coin? Type each child’s coin in cents ($1 is 100¢).',
         frame='Ali {f1}   Ben {f2}   Mei {f3}   Siti {f4}', check=lambda: [VAL[COINWAYS[k]] for k in ('Ali', 'Ben', 'Mei', 'Siti')],
         hint='Mei has more than Ali and less than Ben. Put Ali, Mei and Ben in order from the smallest coin. Which coin is left over?',
         steps=['Ali has less than Mei and Mei has less than Ben, so Ali < Mei < Ben: three different coins in order.', 'The $1 coin is the biggest. Ben has more than Mei and Ali but does not have the $1 coin, so none of Ali, Mei and Ben has it: Siti has the $1 coin.', 'The other three coins in order: Ali 10¢, Mei 20¢, Ben 50¢. Check: Mei has more than Ali and less than Ben, and Ben does not have the $1 coin.'],
         src=['Ali, Ben, Mei and Siti each have one coin: 10¢, 20¢, 50¢ or $1. Mei has more money than Ali but less than Ben. Ben does not have the $1 coin. Who has which coin?']),
    dict(id='C7a', tier='challenge', no='Go further 7 (plates)', label='G7 plates', type='number', skill='mixing two prices', answer=4,
         q='At a hawker centre, chicken rice costs $4 a plate and noodles cost $3 a bowl. Ravi’s family buys 7 dishes for $25. How many plates of chicken rice do they buy?',
         check=lambda: dishes(25)[0],
         hint='Make a table: the number of plates of chicken rice, the number of bowls of noodles (7 dishes in all), and the total cost. Try 0 plates, 1 plate, 2 plates ...',
         steps=['0 plates and 7 bowls: $21. 1 plate and 6 bowls: $22. 2 plates: $23. 3 plates: $24. 4 plates and 3 bowls: $25.', '4 plates of chicken rice cost $16 and 3 bowls of noodles cost $9: $16 + $9 = $25.'],
         src=['At a hawker centre, chicken rice costs $4 a plate and noodles cost $3 a bowl. Ravi’s family buys 7 dishes for $25. How many plates of chicken rice do they buy? What is the smallest total 7 dishes can cost? The biggest? Can 7 dishes cost $30? Can they cost EVERY whole-dollar amount in between?']),
    dict(id='C7b', tier='challenge', no='Go further 7 (smallest, biggest)', label='G7 range', type='fields', skill='mixing two prices', answer=[21, 28],
         q='Chicken rice costs $4 a plate and noodles cost $3 a bowl. Ravi’s family buys 7 dishes. What is the smallest total 7 dishes can cost? What is the biggest? Type the amounts in dollars.',
         frame='Smallest ${f1}   Biggest ${f2}', check=lambda: [min(4 * p + 3 * (7 - p) for p in range(0, 8)), max(4 * p + 3 * (7 - p) for p in range(0, 8))],
         hint='What if all 7 dishes are noodles? What if all 7 dishes are chicken rice?',
         steps=['All noodles: 7 × $3 = $21. This is the smallest total.', 'All chicken rice: 7 × $4 = $28. This is the biggest total.'],
         src=['At a hawker centre, chicken rice costs $4 a plate and noodles cost $3 a bowl. Ravi’s family buys 7 dishes for $25. How many plates of chicken rice do they buy? What is the smallest total 7 dishes can cost? The biggest? Can 7 dishes cost $30? Can they cost EVERY whole-dollar amount in between?']),
    dict(id='C7c', tier='challenge', no='Go further 7 ($30)', label='G7 cost 30', type='choice', options=['Yes', 'No'], answer='No', skill='mixing two prices',
         q='Chicken rice costs $4 a plate and noodles cost $3 a bowl. Can 7 dishes cost $30?',
         check=lambda: 'Yes' if dishes(30) else 'No',
         hint='Think about the most that 7 dishes can cost.',
         steps=['The most that 7 dishes can cost is 7 × $4 = $28.', '$30 is more than $28, so 7 dishes cannot cost $30.'],
         src=['At a hawker centre, chicken rice costs $4 a plate and noodles cost $3 a bowl. Ravi’s family buys 7 dishes for $25. How many plates of chicken rice do they buy? What is the smallest total 7 dishes can cost? The biggest? Can 7 dishes cost $30? Can they cost EVERY whole-dollar amount in between?']),
    dict(id='C7d', tier='challenge', no='Go further 7 (every amount)', label='G7 every', type='choice', options=['Yes', 'No'], answer='Yes', skill='mixing two prices',
         q='Chicken rice costs $4 a plate and noodles cost $3 a bowl. Can 7 dishes cost EVERY whole-dollar amount from the smallest total to the biggest total?',
         check=lambda: 'Yes' if all(dishes(t) for t in range(min(4 * p + 3 * (7 - p) for p in range(8)), max(4 * p + 3 * (7 - p) for p in range(8)) + 1)) else 'No',
         hint='Swap one bowl of noodles for one plate of chicken rice. How much does the total change?',
         steps=['Start with 7 bowls of noodles: $21. Each time you swap one bowl of noodles for one plate of chicken rice, the total goes up by exactly $1.', 'After 1, 2, 3, ... 7 swaps the totals are $22, $23, ... $28. So 7 dishes can cost every whole-dollar amount from $21 to $28.'],
         src=['At a hawker centre, chicken rice costs $4 a plate and noodles cost $3 a bowl. Ravi’s family buys 7 dishes for $25. How many plates of chicken rice do they buy? What is the smallest total 7 dishes can cost? The biggest? Can 7 dishes cost $30? Can they cost EVERY whole-dollar amount in between?']),
    dict(id='M', tier='challenge', no='Make up your own', label='Make', type='selfcheck', open=True, skill='making puzzles', marking_mode='open',
         q='Make up a puzzle for next year’s group. Write the puzzle and its answer in the box.',
         hint='Choose a puzzle you liked today. Change the numbers, solve it yourself, and check that your answer is right and that no other answer fits.',
         steps=['Many puzzles are good. Example: “Ali has 5 coins, all 10¢ or 20¢, worth 90¢. How many of each?” The answer is one 10¢ coin and four 20¢ coins (10 + 80 = 90).',
                'It has only this one answer: each time you swap a 10¢ coin for a 20¢ coin the total goes up by exactly 10¢, so 90¢ can be made in only one way.'],
         src=['a puzzle for next year', 'group. Write the answer on the back.']),
]
for _d in ITEMS:
    _d.setdefault('strand', STRAND)
    if _d['type'] == 'selfcheck':
        _d.setdefault('marking_mode', 'self')


# ---------------------------------------------------------------- variant families (template + independent oracle over EVERY combination)
VARIANTS = {
    '1a': dict(
        base=dict(k=5, n=6),
        tpl=dict(vars=dict(k=[2, 5, 10], n=[3, 4, 5, 6, 7, 8]), answer='k*n',
                 q='In a picture graph each picture stands for {k} ice-creams. Tuesday has {n} pictures. How many ice-creams were sold on Tuesday?',
                 hint='Look at the key. What is one picture worth? Count on in that number.',
                 steps=['Each picture stands for {k} ice-creams and Tuesday has {n} pictures.', '{n} × {k} = {ans} ice-creams were sold on Tuesday.']),
        oracle=lambda e: sum(e['k'] for _ in range(e['n']))),
    '3b': dict(
        base=dict(n=6, a=50, b=20, k=2),
        tpl=dict(vars=dict(n=[5, 6, 7], a=[50, 20], b=[10, 5], k=[1, 2, 3, 4]), derive=dict(t='k*a+(n-k)*b', m='n-k'),
                 answers=dict(f1='k', f2='n-k'), frame='{a}¢ coins {f1}   {b}¢ coins {f2}',
                 q='Ben has {n} coins. They are all {a}¢ and {b}¢ coins. Together they are worth {t} cents. How many of each coin does he have?',
                 hint='Make a table: the number of {a}¢ coins, the number of {b}¢ coins, and the total. Start with 0 of the {a}¢ coins and go up one at a time.',
                 steps=['Try 0, 1, 2, ... of the {a}¢ coins and find the total each time, until you reach {t} cents.', 'With {k} coins of {a}¢ and {m} coins of {b}¢ the total is {t} cents.']),
        oracle=lambda e: next(dict(f1=k, f2=e['n'] - k) for k in range(0, e['n'] + 1) if k * e['a'] + (e['n'] - k) * e['b'] == e['k'] * e['a'] + (e['n'] - e['k']) * e['b'])),
    '6b': dict(
        base=dict(s=4, t=8),
        tpl=dict(vars=dict(s=[3, 4, 5, 6], t=[5, 6, 7, 8, 9, 10]), derive=dict(s2='2*s', s3='3*s'), answer='s*t',
                 q='Ben builds towers with cubes. Tower 1 has {s} cubes, Tower 2 has {s2} cubes and Tower 3 has {s3} cubes. Keep the pattern going. How many cubes are in Tower {t}?',
                 hint='Keep adding the same number of cubes for each new tower, or look for a shortcut with a times table.',
                 steps=['Each tower adds {s} cubes: {s}, {s2}, {s3}, and so on.', 'Tower {t} has {t} × {s} = {ans} cubes.']),
        oracle=lambda e: tower_cubes(e['t'], [e['s'], 2 * e['s'], 3 * e['s']])),
    'T1': dict(
        base=dict(k=5, a=2, b=3, m=1),
        tpl=dict(vars=dict(k=[5, 10], a=[1, 2, 3], b=[2, 3, 4], m=[1, 2, 3]), derive=dict(t='k*(a+b+m)', c='k*a', d='k*b', e='k*(a+b)', r='m*k'), answer='m',
                 q='{t} children chose a fruit. In the picture graph each picture stands for {k} children. Apple has {a} pictures and banana has {b} pictures. The mango row is missing. How many pictures should the mango row have?',
                 hint='How many children are in the apple row and the banana row together? How many of the {t} children are left for mango?',
                 steps=['Apple: {a} × {k} = {c} children. Banana: {b} × {k} = {d} children.', '{c} + {d} = {e}, so {t} − {e} = {r} children chose mango.', '{r} children is {ans} picture(s) ({r} ÷ {k}).']),
        oracle=lambda e: (lambda left: next(p for p in range(0, 30) if p * e['k'] == left))(e['k'] * (e['a'] + e['b'] + e['m']) - e['k'] * e['a'] - e['k'] * e['b'])),
    'T2c': dict(
        base=dict(a=3, b=10),
        tpl=dict(vars=dict(a=[2, 3, 4, 5], b=[6, 8, 10, 12]), derive=dict(a2='2*a', a3='3*a'), answer='2*b//a',
                 q='Mei saves ${a} on day 1, ${a2} on day 2, ${a3} on day 3, and so on (${a} more each day). Ali saves ${b} every day. On which day does Mei FIRST have more than Ali altogether? Type the day number.',
                 hint='Make a table of what each child has saved altogether after each day. Look for the first day when Mei’s total is bigger than Ali’s.',
                 steps=['Keep adding each day’s saving to the total so far, for both children.', 'Mei first has more than Ali altogether on day {ans}.']),
        oracle=lambda e: first_day_ahead(e['a'], e['b'])),
    'T3': dict(
        base=dict(c=14, a=6),
        tpl=dict(vars=dict(c=[12, 14, 16, 18, 20], a=[2, 4, 6, 8]), derive=dict(h='c-a'), answer='2*(c-a)',
                 q='A bus had some people on it. At the first stop half of the people got off. At the second stop {a} people got on. Now there are {c} people on the bus. How many people were on the bus at the start?',
                 hint='Draw a bar on paper if it helps. Work backwards from {c}: first undo the people who got on at the second stop. What is left is half of the start.',
                 steps=['At the second stop {a} people got on, so before that there were {c} − {a} = {h} people.', '{h} people is half of the start, so the start was {h} + {h} = {ans} people.']),
        oracle=lambda e: bus_start(e['c'], e['a'])),
    'C5': dict(
        base=dict(f=6, s=4, k=5),
        tpl=dict(vars=dict(f=[5, 6, 7, 8], s=[2, 3, 4], k=[2, 5, 10]), derive=dict(d='(f-s)*k', g='f-s'), answers=dict(f1='s*k', f2='f*k'), frame='Swimming {f1}   Football {f2}',
                 q='A picture graph has lost its key. Football has {f} pictures and swimming has {s} pictures. {d} more children chose football than swimming. How many children chose swimming? How many chose football?',
                 hint='How many more pictures does football have than swimming? Those pictures stand for {d} children. What is one picture worth?',
                 steps=['Football has {g} more pictures than swimming, and these {g} pictures are {d} children, so 1 picture is {k} children.', 'Swimming: {s} × {k} children. Football: {f} × {k} children.']),
        oracle=lambda e: (lambda k: dict(f1=e['s'] * k, f2=e['f'] * k))(key_value(e['f'], e['s'], (e['f'] - e['s']) * e['k']))),
}
