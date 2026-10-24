"""Level 2 (P2) holiday lesson 9: MEASURE MASTERS (length, mass, volume and time), week 5, first lesson.  Online mirror of the printed workbook pages.

The questions are the ones printed in the Level 2 holiday workbook (p2/content/l9.js `workbook()` = Start here, p2/gaps.json lesson 9 `invest` = Investigation,
p2/content/l9.js `qbank.stretch` first four = Think harder 1 to 4, `qbank.challenge` last three = Go further 5 to 7, as built by p2/workbook_html.js, and the
"Make up your own" line).  Every answer is recomputed by an INDEPENDENT checker that does not use the printed answer or the "undo" rule: the balance scales are solved by TRYING
numbers of grams; the jug puzzles are run step by step in a simulator and the fewest steps come from a search over every state; the clocks are read back from the angles of the
hands in the printed picture; times are counted in minutes; the weights puzzle tries every set; the ribbons are laid on a number line.  build_holiday.py stops if a checker and the
printed answer differ.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from hlib import *          # noqa: E402,F401
from p2lib import *         # noqa: E402,F401
from p2lib_w5 import *      # noqa: E402,F401

STRAND = 'Measurement: mass, volume, length and time'
META = dict(level=2, lesson=9, key='p2', title='Measure masters', workbook_title='MEASURE MASTERS', topic='Length, Mass, Volume and Time', strand=STRAND,
            sources=['p2/content/l9.js', 'p2/gaps.json', 'p2/workbook_html.js'],
            intro=['A level balance means both sides are equally heavy, so you can swap a thing for whatever balances it.',
                   'In a jug puzzle a step is one of these: fill a jug from the tap, empty a jug into the sink, or pour from one jug into the other until one jug is full or the other is empty. '
                   'Write how much is in each jug after every step. You can act it out with two cups and some rice.',
                   'For times, count on to the next o’clock first, then count the rest.'])

# The printed pictures (p2/workbook_body.html) are too small and their labels collide at 390 px, so the scales, the clocks and the jugs are redrawn for a phone with the same
# things on the pans; the clocks' hands are copied from the printed clocks and read back from the new drawing.
PRINTED_CLOCKS = printed_fig('Two clocks. Clock A')
PRINTED_TIMES = read_clocks(PRINTED_CLOCKS)
CLOCKS = clocks_fig(PRINTED_TIMES, [('Ali is eating', 'breakfast.'), ('Ali is at swimming', 'after school.')],
                    'Two clocks. Clock A: Ali is eating breakfast. Clock B: Ali is at swimming after school. The short thick navy hand is the hour hand and the long thin red hand is the minute hand.')
assert read_clocks(CLOCKS) == PRINTED_TIMES
SCALES = scales_fig([('Scale 1', ['melon'], 'melon', ['apple', 'apple'], '2 apples'), ('Scale 2', ['apple'], 'apple', ['w100', 'w100'], '2 × 100 g'),
                     ('Scale 3', ['melon'], 'melon', ['apple', 'lemon', 'lemon', 'lemon', 'lemon'], 'apple, 4 lemons')])
T1_FIG = scales_fig([('Scale 1', ['apple', 'apple', 'lemon'], '2 apples, 1 lemon', ['pomelo'], 'pomelo'), ('Scale 2', ['pomelo'], 'pomelo', ['lemon'] * 5, '5 lemons')])
T3_FIG = scales_fig([('Scale 1', ['apple', 'apple', 'apple'], '3 apples', ['pomelo'], 'pomelo'), ('Scale 2', ['pomelo', 'apple', 'apple'], 'pomelo, 2 apples', ['w500'], '500 g')])
G6_FIG = scales_fig([('Scale 1', ['cube', 'cube', 'ball'], '2 cubes, 1 ball', ['ball', 'ball'], '2 balls'), ('Scale 2', ['ball', 'cube'], '1 ball, 1 cube', ['w300'], '300 g')])
JUGS = jugs_fig(3, 5)
RIBBON = ribbon_fig(64, 18, 5)
T2_FIG = time_line_fig([(34, '10:45 am'), (104, '11:00'), (236, '12:00'), (304, '12:10 pm')], [(0, 1, '? min'), (1, 2, '? h'), (2, 3, '? min')],
                       'A time line from 10:45 am to 12:10 pm with 11:00 and 12:00 marked and three jumps: ? minutes, ? hours, ? minutes')
J27 = jugs_fig(2, 7)
J37 = jugs_fig(3, 7)
JUGTABLE = jug_table_fig([('Start', 'both jugs empty', '0 ℓ', '0 ℓ'), ('1', 'Fill the 5 ℓ jug', '0 ℓ', '5 ℓ'), ('2', 'Pour into 3 ℓ until full', '3 ℓ', '2 ℓ'),
                          ('3', 'Empty the 3 ℓ jug', '0 ℓ', '2 ℓ'), ('4', '', '', ''), ('5', '', '', ''), ('6', '', '', ''), ('7', '', '', '')])


# ---------------------------------------------------------------- independent checkers
def _labels(fig):
    return ' | '.join(re.findall(r'<text[^>]*>([^<]*)</text>', fig))


def scales_q1():
    """(apple, melon, lemon) in grams by TRYING numbers: scale 2 apple = 2 x 100 g; scale 1 melon = 2 apples; scale 3 melon = apple + 4 lemons.  The statements are read from the figure's labels."""
    lab = _labels(SCALES)
    assert '2 apples' in lab and '2 × 100 g' in lab and 'apple, 4 lemons' in lab, lab         # read from the figure the child sees
    for a in range(1, 1001):
        if a != 100 + 100:
            continue
        for m in range(1, 2001):
            if m != a + a:
                continue
            for l in range(1, 2001):
                if m == a + 4 * l:
                    return a, m, l
    raise ValueError('no solution')


def scales_t1():
    """(lemons for 1 apple, lemons for 1 pomelo and 1 apple): lemon = 1; pomelo = 5 lemons; 2 apples + 1 lemon = pomelo; try apples."""
    pomelo = 5
    for a in range(0, 50):
        if 2 * a + 1 == pomelo:
            return a, pomelo + a
    raise ValueError('no solution')


def scales_t3():
    """(apple g, pomelo g): 3 apples = pomelo; pomelo + 2 apples = 500 g; try grams."""
    for a in range(1, 501):
        p = 3 * a
        if p + 2 * a == 500:
            return a, p
    raise ValueError('no solution')


def scales_g6():
    """(cube g, ball g): 2 cubes + 1 ball = 2 balls; 1 ball + 1 cube = 300 g; try grams."""
    for c in range(1, 301):
        for b in range(1, 301):
            if 2 * c + b == 2 * b and b + c == 300:
                return c, b
    raise ValueError('no solution')


def ribbon_joined(red, diff, overlap):
    """Length of the new ribbon: red laid from 0 to red; blue is `diff` shorter; blue starts `overlap` before the end of red."""
    blue = next(x for x in range(0, red + 1) if x + diff == red)
    start = red - overlap
    return max(red, start + blue) - 0


def blue_of(red, diff):
    return next(x for x in range(0, red + 1) if x + diff == red)


def times_of_clocks():
    cl = read_clocks(CLOCKS)
    cap = clock_captions(PRINTED_CLOCKS)
    out = []
    for (h, m), c in zip(cl, cap):
        out.append((h, m, 'am' if 'breakfast' in c else 'pm' if 'after school' in c else None))
    return out


CLK = times_of_clocks()                                      # [(7, 25, 'am'), (4, 50, 'pm')]
CA = CLK[0]
CB = CLK[1]
END_B = clock_text(minutes_of(*CB) + 35)                     # swimming ends


def time_str(h, m, s):
    return f'{h}:{m:02d} {s}'


def lessons_end(start, lesson, brk, n):
    t = start
    for k in range(n):
        t += lesson
        if k < n - 1:
            t += brk
    return t


def trip_minutes(h1, m1, h2, m2):
    """Minutes from h1:m1 to h2:m2 by counting on to the next hour first, then the rest (no subtraction of clock times)."""
    t, n = h1 * 60 + m1, 0
    while t < h2 * 60 + m2:
        t += 1
        n += 1
    return n


def ways_model(caps, moves, goal):
    sts = jug_run(caps, moves)
    assert goal in sts[-1], (caps, moves, goal)
    return sts[-1]


MODEL_2A = [('fill', 1), ('pour', 1, 0)]
MODEL_2B = [('fill', 0), ('pour', 0, 1), ('fill', 0), ('pour', 0, 1)]
MODEL_Q3 = [('fill', 1), ('pour', 1, 0), ('empty', 0), ('pour', 1, 0), ('fill', 1), ('pour', 1, 0)]
MODEL_T4 = [('fill', 1), ('pour', 1, 0), ('empty', 0), ('pour', 1, 0)]
MODEL_G5 = [('fill', 1), ('pour', 1, 0), ('empty', 0), ('pour', 1, 0), ('empty', 0), ('pour', 1, 0), ('fill', 1), ('pour', 1, 0)]

ITEMS = [
    # ================= Start here (workbook lesson 9, No.1 to No.5)
    dict(id='1a', tier='core', no='1(a)', label='1(a)', type='number', skill='balance: swapping equal masses', svg=SCALES, answer=200,
         q='Each scale is level. How heavy is 1 apple? Type the number of grams.',
         check=lambda: scales_q1()[0],
         hint='Find the scale that has a number on it. What does the apple balance there?',
         steps=['Scale 2 is level: 1 apple balances two 100 g weights.', '100 + 100 = 200, so 1 apple is 200 g.'],
         src=['Each scale is level.', 'How heavy is 1 apple?']),
    dict(id='1b', tier='core', no='1(b)', label='1(b)', type='number', skill='balance: swapping equal masses', svg=SCALES, answer=400,
         q='Each scale is level. How heavy is the melon? Type the number of grams.',
         check=lambda: scales_q1()[1],
         hint='Scale 1 shows what balances the melon. You can swap the melon for those fruits.',
         steps=['Scale 1 is level: the melon balances 2 apples.', 'Each apple is 200 g, so the melon is 200 + 200 = 400 g.'],
         src=['Each scale is level.', 'How heavy is the melon?']),
    dict(id='1c', tier='core', no='1(c)', label='1(c)', type='number', skill='balance: swapping equal masses', svg=SCALES, answer=50,
         q='Each scale is level. How heavy is 1 lemon? Tip: on Scale 3, melon = apple + 4 lemons. Type the number of grams.',
         check=lambda: scales_q1()[2],
         hint='On Scale 3 the melon balances an apple and 4 lemons. What do you know about the melon and the apple? So what are the 4 lemons together?',
         steps=['On Scale 3 the melon balances the apple and 4 lemons. The melon is 400 g and the apple is 200 g.', 'So the 4 lemons are 400 − 200 = 200 g together.', '1 lemon is 200 ÷ 4 = 50 g.'],
         src=['How heavy is 1 lemon? Show how you know. Tip: on Scale 3, melon = apple + 4 lemons.']),
    dict(id='1d', tier='core', no='1(c) show how', label='1(c) how', type='selfcheck', open=False, skill='explaining a balance', svg=SCALES,
         q='Each scale is level. Show how you know how heavy 1 lemon is. Write your idea in the box.',
         facts=dict(apple=200, melon=400, lemon=50), check=lambda: dict(zip(('apple', 'melon', 'lemon'), scales_q1())),
         hint='Say it in steps: which scale tells you the apple? Then the melon? Then the lemons?',
         steps=['Example: Scale 2: 1 apple = 100 + 100 = 200 g. Scale 1: the melon = 2 apples = 400 g. Scale 3: melon = apple + 4 lemons, so 4 lemons = 400 − 200 = 200 g and 1 lemon = 50 g.', 'Any clear way of showing it is good.'],
         src=['How heavy is 1 lemon? Show how you know. Tip: on Scale 3, melon = apple + 4 lemons.']),
    dict(id='1e', tier='core', no='1(d)', label='1(d)', type='number', skill='balance: swapping equal masses', svg=SCALES, answer=8,
         q='Each scale is level. How many lemons balance the melon?',
         check=lambda: (lambda a, m, l: next(n for n in range(0, 100) if n * l == m))(*scales_q1()),
         hint='Use how heavy the melon is and how heavy 1 lemon is. How many lemons make that mass?',
         steps=['The melon is 400 g and 1 lemon is 50 g.', '8 lemons are 8 × 50 = 400 g, so 8 lemons balance the melon.'],
         src=['How many lemons balance the melon?']),

    dict(id='2a', tier='core', no='2(a)', label='2(a)', type='selfcheck', open=False, skill='jug puzzles: step by step', svg=JUGS,
         q='You have a 3 ℓ jug and a 5 ℓ jug with no marks. A step is one fill, one empty or one pour (until one jug is full or the other is empty). How can you get exactly 2 ℓ? Write the steps.',
         facts=dict(end=(3, 2)), check=lambda: dict(end=ways_model((3, 5), MODEL_2A, 2)),
         hint='Act it out with two cups of different sizes and some rice, or draw the jugs. Write how much is in each jug after every step.',
         steps=['Example (any correct way is good):'] + jug_text((3, 5), MODEL_2A) + ['2 ℓ is left in the 5 ℓ jug.'],
         src=['You have a 3 ℓ jug and a 5 ℓ jug. You can fill a jug from the tap, empty a jug into the sink, or pour from one jug into the other until one jug is full or the other is empty.', 'How can you get exactly 2 ℓ? Write the steps.']),
    dict(id='2a2', tier='core', no='2(a) fewest steps', label='2(a) fewest', type='number', skill='jug puzzles: step by step', svg=JUGS, answer=2,
         q='A step is one fill, one empty or one pour. What is the fewest number of steps that gets exactly 2 ℓ into one of the jugs? Do the steps question first.',
         check=lambda: jug_fewest((3, 5), 2)[0],
         hint='Count each fill, each empty and each pour as one step. Can you find a way with fewer steps than yours?',
         steps=['The shortest way takes 2 steps:'] + jug_text((3, 5), jug_fewest((3, 5), 2)[1]) + ['A search over every possible state found no way with only 1 step.'],
         src=['How can you get exactly 2 ℓ? Write the steps.']),
    dict(id='2b', tier='core', no='2(b)', label='2(b)', type='selfcheck', open=False, skill='jug puzzles: step by step', svg=JUGS,
         q='Same jugs: 3 ℓ and 5 ℓ, no marks. How can you get exactly 1 ℓ? Write the steps in the box.',
         facts=dict(end=(1, 5)), check=lambda: dict(end=ways_model((3, 5), MODEL_2B, 1)),
         hint='Write down how much is in each jug after every step. If your first try gets stuck, try starting with the other jug.',
         steps=['Example (any correct way is good):'] + jug_text((3, 5), MODEL_2B) + ['1 ℓ is left in the 3 ℓ jug.'],
         src=['How can you get exactly 1 ℓ? Write the steps.']),
    dict(id='2b2', tier='core', no='2(b) fewest steps', label='2(b) fewest', type='number', skill='jug puzzles: step by step', svg=JUGS, answer=4,
         q='A step is one fill, one empty or one pour. What is the fewest number of steps that gets exactly 1 ℓ into one of the jugs? Do the steps question first.',
         check=lambda: jug_fewest((3, 5), 1)[0],
         hint='Count each fill, each empty and each pour as one step. Can you find a way with fewer steps than yours?',
         steps=['The shortest way takes 4 steps:'] + jug_text((3, 5), jug_fewest((3, 5), 1)[1]) + ['A search over every possible state found no way with 3 steps or fewer.'],
         src=['How can you get exactly 1 ℓ? Write the steps.']),

    dict(id='3', tier='core', no='3', label='3 steps', type='selfcheck', open=False, skill='jug puzzles: keeping a table', svg=JUGTABLE,
         q='Get exactly 4 ℓ in the 5 ℓ jug. Both jugs start empty. The table shows the first three steps: now the 5 ℓ jug has 2 ℓ. Where can that 2 ℓ go? Write each new step and how much is in each jug after it.',
         facts=dict(end=(3, 4)), check=lambda: dict(end=ways_model((3, 5), MODEL_Q3, 4)),
         hint='Write how much is in each jug after every step. The 3 ℓ jug is empty now: could the 2 ℓ go into it?',
         steps=['Example (any correct way is good). Steps 1 to 3 are done for you:'] + jug_text((3, 5), MODEL_Q3) + ['4 ℓ is in the 5 ℓ jug after step 6. You may not need every row of the table.'],
         src=['Next puzzle. Get exactly 4 ℓ in the 5 ℓ jug. Start with both jugs empty. The first three steps are done for you: you now have 2 ℓ in the 5 ℓ jug.', 'Where can that 2 ℓ go? Write each step in the table.']),
    dict(id='3b', tier='core', no='3 how many more', label='3 more', type='number', skill='jug puzzles: keeping a table', svg=JUGS, answer=3,
         q='Three steps are done: the 3 ℓ jug is empty and the 5 ℓ jug has 2 ℓ. What is the fewest number of MORE steps that gets exactly 4 ℓ into the 5 ℓ jug? Do the steps question first.',
         check=lambda: jug_fewest((3, 5), 4, start=(0, 2), which=1)[0],
         hint='Do not count the first three steps. Count each fill, each empty and each pour as one step.',
         steps=['From 0 ℓ in the 3 ℓ jug and 2 ℓ in the 5 ℓ jug, the shortest way takes 3 more steps:'] + jug_text((3, 5), jug_fewest((3, 5), 4, start=(0, 2), which=1)[1], start=(0, 2)),
         src=['Where can that 2 ℓ go? Write each step in the table.']),

    dict(id='4a', tier='core', no='4(a)', label='4(a)', type='number', skill='length: comparing in cm', answer=46,
         q='Siti has a red ribbon 64 cm long. Her blue ribbon is 18 cm shorter than the red ribbon. How long is the blue ribbon? Type the number of cm.',
         check=lambda: blue_of(64, 18),
         hint='The blue ribbon is 18 cm shorter than the red one. Should you add 18 or take 18 away?',
         steps=['Shorter means take away: 64 − 18.', '64 − 18 = 46, so the blue ribbon is 46 cm long.'],
         src=['Siti has a red ribbon 64 cm long. Her blue ribbon is 18 cm shorter than the red ribbon.', 'How long is the blue ribbon?']),
    dict(id='4b', tier='core', no='4(b)', label='4(b)', type='number', skill='length: joining with an overlap', svg=RIBBON, answer=105,
         q='Siti’s red ribbon is 64 cm long. Her blue ribbon is 18 cm shorter. She glues them end to end with a 5 cm overlap. How long is the new ribbon? Type the number of cm.',
         check=lambda: ribbon_joined(64, 18, 5),
         hint='Both ribbons added together would count the overlap two times. How can you fix that?',
         steps=['The blue ribbon is 46 cm. Side by side, 64 + 46 = 110 cm.', 'The 5 cm overlap was counted twice, so take it away once: 110 − 5 = 105.', 'The new ribbon is 105 cm long.'],
         src=['Siti has a red ribbon 64 cm long. Her blue ribbon is 18 cm shorter than the red ribbon.', 'She glues them end to end with a 5 cm overlap. The new ribbon is']),

    dict(id='5a', tier='core', no='5(a) clock A', label='5(a) A', type='text', skill='telling the time to 5 minutes', svg=CLOCKS, accept=time_forms(*CA), shown=time_str(*CA), equiv_frac=False,
         q='Read the clocks. The short thick hand is the hour hand. What time is it on clock A, where Ali is eating breakfast? Write it with am or pm, like 9:10 pm.',
         check=lambda: time_str(*CA),
         hint='Look at the long thin hand first and count the minutes in 5s from the 12. Then look at the hour hand: which number has it passed?',
         steps=['The long hand points at 5, so it is 25 minutes past. The short hand is just past the 7, so the hour is 7.', 'Breakfast is in the morning, so it is 7:25 am.'],
         src=['Read the clocks.', 'Write each time with am or pm.']),
    dict(id='5a2', tier='core', no='5(a) clock B', label='5(a) B', type='text', skill='telling the time to 5 minutes', svg=CLOCKS, accept=time_forms(*CB), shown=time_str(*CB), equiv_frac=False,
         q='Read clock B, where Ali is at swimming after school. Hint: its hour hand is almost on the 5. Is it 4 o’clock or 5 o’clock? Write the time with am or pm, like 9:10 pm.',
         check=lambda: time_str(*CB),
         hint='Count the minutes in 5s from the 12 to the long thin hand. Is the hour hand still on its way to the 5, or has it passed it?',
         steps=['The long hand points at 10, so it is 50 minutes past. At 50 minutes past the hour hand is almost at the next number: it is almost on the 5, so the hour is 4.', 'After school is in the afternoon, so it is 4:50 pm.'],
         src=['Read the clocks. Hint: on clock B the hour hand is almost on the 5. Is it 4 o', 'Write each time with am or pm.']),
    dict(id='5b', tier='core', no='5(b)', label='5(b)', type='text', skill='time: finding the end time', svg=CLOCKS, accept=time_forms(*END_B, bare_ok=True), shown=time_str(*END_B), equiv_frac=False,
         q='Swimming starts at the time on clock B and lasts 35 minutes. What time does it end? Write it like 9:10 pm.',
         check=lambda: time_str(*clock_text(minutes_of(*CB) + 35)),
         hint='Count on from the time on clock B. First go to the next o’clock, then add the rest of the 35 minutes.',
         steps=['Clock B shows 4:50 pm. From 4:50 to 5:00 is 10 minutes.', '35 − 10 = 25 minutes more after 5:00, so it ends at 5:25 pm.'],
         src=['Swimming starts at the time on clock B and lasts 35 minutes. It ends at']),
    dict(id='5c', tier='core', no='5(c)', label='5(c)', type='number', skill='time: how long', answer=45,
         q='Mei’s family leaves home at 10:45 am. They reach Grandma’s flat at 11:30 am. How long is the trip? Type the number of minutes.',
         check=lambda: trip_minutes(10, 45, 11, 30),
         hint='Count on from 10:45 to the next o’clock first. Then count the rest of the way to 11:30.',
         steps=['10:45 to 11:00 is 15 minutes.', '11:00 to 11:30 is 30 minutes.', '15 + 30 = 45 minutes.'],
         src=['Mei’s family leaves home at 10:45 am. They reach Grandma’s flat at 11:30 am. How long is the trip?']),

    # ================= Investigation: Weights puzzle
    dict(id='I1', tier='invest', no='Investigation (a)', label='Inv 1', type='set', range=True, ordered=False, skill='making masses from weights', answer=[1, 2, 3, 4, 5, 6, 7],
         q='Weights puzzle. You have three weights: 1 g, 2 g and 4 g. You can put some of them on one pan to make a mass. Type every mass from 1 g to 8 g that you can make.',
         check=lambda: sorted(m for m in masses((1, 2, 4)) if 1 <= m <= 8),
         hint='Easy first step: can you make 3 g? Can you make 5 g? Try putting two weights on the pan together, then all three.',
         steps=['One weight: 1 g, 2 g or 4 g. Two weights: 1 + 2 = 3, 1 + 4 = 5, 2 + 4 = 6.', 'All three: 1 + 2 + 4 = 7.', 'So you can make every mass from 1 g to 7 g. You cannot make 8 g: all three weights together are only 7 g.'],
         src=['You have three different weights. Each weight is 1 g, 2 g, 3 g, 4 g or 5 g. You put some of them on one pan to make a mass.', '(a) With weights of 1 g, 2 g and 4 g, which masses from 1 g to 7 g can you make?']),
    dict(id='I2', tier='invest', no='Investigation (b)', label='Inv 2', type='set', ordered=True, grouped=False, skill='finding all the sets of weights', answer=[1, 2, 3, 1, 2, 4],
         q='Pick three different weights from 1 g to 5 g. Which sets make EVERY mass from 1 g to 6 g? Type each set as three numbers, smallest first, and list the sets in order (2 3 4 comes before 2 3 5).',
         check=lambda: [w for s in good_weight_sets(1, 5, 3, 6) for w in s],
         hint='Try the sets one at a time. For each set check the masses 1 g, 2 g, 3 g, 4 g, 5 g and 6 g: does the set make every one of them?',
         steps=['There are 10 sets of three different weights from 1 g to 5 g. Check each set for every mass from 1 g to 6 g.', 'The sets 1, 2, 3 (makes 1 g to 6 g) and 1, 2, 4 (makes 1 g to 7 g) work.', 'Every other set misses at least one mass from 1 g to 6 g.'],
         src=['(b) Find ALL the sets of three different weights from 1 g to 5 g that can make every mass from 1 g to 6 g.']),
    dict(id='I3', tier='invest', no='Investigation (c)', label='Inv 3', type='selfcheck', open=False, skill='explaining what the good sets share',
         q='Look at the sets of three weights from 1 g to 5 g that make every mass from 1 g to 6 g. What do all the good sets have in common? Write your idea in the box.',
         facts=dict(in_every_good_set=[1, 2]), check=lambda: dict(in_every_good_set=sorted(set.intersection(*[set(s) for s in good_weight_sets(1, 5, 3, 6)]))),
         hint='Look at the weights in each good set. Is there a weight that is in every set?',
         steps=['Example: every good set has the 1 g weight and the 2 g weight.', 'Only a 1 g weight can make 1 g, and with three different weights only a 2 g weight can make 2 g.', 'Any idea that notices the 1 g and 2 g weights is good.'],
         src=['(c) What do all the good sets have in common?']),

    # ================= Think harder
    dict(id='T1a', tier='stretch', no='Think harder 1', label='T1', type='number', skill='balance: swapping equal masses', svg=T1_FIG, answer=2,
         q='2 apples and 1 lemon balance 1 pomelo. 1 pomelo balances 5 lemons. How many lemons balance 1 apple?',
         check=lambda: scales_t1()[0],
         hint='Swap the pomelo on the first scale for what balances it on the second scale. Then take the same thing off both sides.',
         steps=['Swap the pomelo for 5 lemons: 2 apples and 1 lemon balance 5 lemons.', 'Take 1 lemon off both sides: 2 apples balance 4 lemons.', 'So 1 apple balances 2 lemons.'],
         src=['2 apples and 1 lemon balance 1 pomelo. 1 pomelo balances 5 lemons. How many lemons balance 1 apple? How many lemons balance 1 pomelo and 1 apple together?']),
    dict(id='T1b', tier='stretch', no='Think harder 1 (together)', label='T1 both', type='number', skill='balance: swapping equal masses', svg=T1_FIG, answer=7,
         q='2 apples and 1 lemon balance 1 pomelo. 1 pomelo balances 5 lemons. How many lemons balance 1 pomelo and 1 apple together?',
         check=lambda: scales_t1()[1],
         hint='Work out how many lemons balance 1 apple. Then add what the pomelo balances.',
         steps=['1 apple balances 2 lemons and 1 pomelo balances 5 lemons.', '5 + 2 = 7, so 7 lemons balance 1 pomelo and 1 apple together.'],
         src=['2 apples and 1 lemon balance 1 pomelo. 1 pomelo balances 5 lemons. How many lemons balance 1 apple? How many lemons balance 1 pomelo and 1 apple together?']),
    dict(id='T2', tier='stretch', no='Think harder 2', label='T2', type='fields', skill='time: how long across the hour', svg=T2_FIG, answer=[1, 25],
         q='Mei’s family leaves home at 10:45 am. They reach Grandma’s flat at 12:10 pm. How long is the trip? Type the hours and the minutes.',
         frame='{f1} hour   {f2} minutes', check=lambda: list(divmod(trip_minutes(10, 45, 12, 10), 60)), clock=False,
         hint='Count on in steps, as on the time line: from 10:45 to 11:00, then to 12:00, then to 12:10.',
         steps=['10:45 to 11:00 is 15 minutes. 11:00 to 12:00 is 1 hour. 12:00 to 12:10 is 10 minutes.', '15 + 10 = 25 minutes, so the trip is 1 hour 25 minutes.'],
         src=['Mei’s family leaves home at 10:45 am. They reach Grandma’s flat at 12:10 pm. How long is the trip?']),
    dict(id='T3', tier='stretch', no='Think harder 3', label='T3', type='fields', skill='balance: swapping equal masses', svg=T3_FIG, answer=[100, 300],
         q='3 apples balance 1 pomelo. The pomelo and 2 apples together balance a 500 g weight. How heavy is one apple? How heavy is the pomelo?',
         frame='Apple {f1} g   Pomelo {f2} g', check=lambda: list(scales_t3()),
         hint='Swap the pomelo on Scale 2 for what balances it on Scale 1. Then how many apples balance the 500 g weight?',
         steps=['Swap the pomelo for 3 apples: 3 apples and 2 apples balance 500 g, so 5 apples balance 500 g.', '1 apple is 500 ÷ 5 = 100 g.', 'The pomelo balances 3 apples: 3 × 100 = 300 g.'],
         src=['3 apples balance 1 pomelo. The pomelo and 2 apples together balance a 500 g weight. How heavy is one apple? How heavy is the pomelo?']),
    dict(id='T4a', tier='stretch', no='Think harder 4', label='T4', type='selfcheck', open=False, skill='jug puzzles: step by step', svg=J27,
         q='You have a 2 ℓ jug and a 7 ℓ jug with no marks. How can you get exactly 3 ℓ? List each pour in the box.',
         facts=dict(end=(2, 3)), check=lambda: dict(end=ways_model((2, 7), MODEL_T4, 3)),
         hint='Write how much is in each jug after every step. What happens if you keep pouring from the big jug into the small jug?',
         steps=['Example (any correct way is good):'] + jug_text((2, 7), MODEL_T4) + ['3 ℓ is left in the 7 ℓ jug.'],
         src=['You have a 2 ℓ jug and a 7 ℓ jug with no marks. How can you get exactly 3 ℓ? List each pour.']),
    dict(id='T4b', tier='stretch', no='Think harder 4 fewest steps', label='T4 fewest', type='number', skill='jug puzzles: step by step', svg=J27, answer=4,
         q='A step is one fill, one empty or one pour. What is the fewest number of steps that gets exactly 3 ℓ into one of the jugs? Do the list question first.',
         check=lambda: jug_fewest((2, 7), 3)[0],
         hint='Count each fill, each empty and each pour as one step. Can you find a way with fewer steps than yours?',
         steps=['The shortest way takes 4 steps:'] + jug_text((2, 7), jug_fewest((2, 7), 3)[1]) + ['A search over every possible state found no way with 3 steps or fewer.'],
         src=['You have a 2 ℓ jug and a 7 ℓ jug with no marks. How can you get exactly 3 ℓ? List each pour.']),

    # ================= Go further
    dict(id='C5a', tier='challenge', no='Go further 5', label='G5', type='selfcheck', open=False, skill='jug puzzles: step by step', svg=J37,
         q='You have a 3 ℓ jug and a 7 ℓ jug with no marks. How can you get exactly 5 ℓ? List each pour in the box.',
         facts=dict(end=(3, 5)), check=lambda: dict(end=ways_model((3, 7), MODEL_G5, 5)),
         hint='Write how much is in each jug after every step. It may take quite a few steps: keep going and look for 5 ℓ.',
         steps=['Example (any correct way is good):'] + jug_text((3, 7), MODEL_G5) + ['5 ℓ is in the 7 ℓ jug at the end.'],
         src=['You have a 3 ℓ jug and a 7 ℓ jug with no marks. How can you get exactly 5 ℓ? List each pour.']),
    dict(id='C5b', tier='challenge', no='Go further 5 fewest steps', label='G5 fewest', type='number', skill='jug puzzles: step by step', svg=J37, answer=8,
         q='A step is one fill, one empty or one pour. What is the fewest number of steps that gets exactly 5 ℓ into one of the jugs? Do the list question first.',
         check=lambda: jug_fewest((3, 7), 5)[0],
         hint='Count each fill, each empty and each pour as one step. Can you find a way with fewer steps than yours?',
         steps=['The shortest way takes 8 steps:'] + jug_text((3, 7), jug_fewest((3, 7), 5)[1]) + ['A search over every possible state found no way with 7 steps or fewer.'],
         src=['You have a 3 ℓ jug and a 7 ℓ jug with no marks. How can you get exactly 5 ℓ? List each pour.']),
    dict(id='C6', tier='challenge', no='Go further 6', label='G6', type='fields', skill='balance: swapping equal masses', svg=G6_FIG, answer=[100, 200],
         q='Scale 1: 2 cubes and 1 ball balance 2 balls. Scale 2: 1 ball and 1 cube balance a 300 g weight. How heavy is one cube? How heavy is one ball?',
         frame='Cube {f1} g   Ball {f2} g', check=lambda: list(scales_g6()),
         hint='Take 1 ball off both sides of Scale 1. What balances what?',
         steps=['Take 1 ball off both sides of Scale 1: 2 cubes balance 1 ball.', 'On Scale 2 swap the ball for 2 cubes: 3 cubes balance 300 g, so 1 cube is 100 g and 1 ball is 200 g.', 'Check Scale 1: 100 + 100 + 200 = 400 and 200 + 200 = 400.'],
         src=['Scale 1: 2 cubes and 1 ball balance 2 balls. Scale 2: 1 ball and 1 cube balance a 300 g weight. How heavy is one cube? How heavy is one ball?']),
    dict(id='C7', tier='challenge', no='Go further 7', label='G7', type='text', skill='time: lessons and breaks', accept=time_forms(10, 20, 'am', bare_ok=True), shown='10:20 am', equiv_frac=False,
         q='Mei has 3 lessons in a row. Each lesson is 35 minutes long, with a 10-minute break between lessons. The first lesson starts at 8:15 am. What time does the last lesson end? Write it like 9:10 am.',
         check=lambda: time_str(*clock_text(lessons_end(minutes_of(8, 15, 'am'), 35, 10, 3))),
         hint='How many breaks are there between 3 lessons? Count on from 8:15 am, one lesson or break at a time.',
         steps=['Lesson 1: 8:15 to 8:50. Break: 8:50 to 9:00.', 'Lesson 2: 9:00 to 9:35. Break: 9:35 to 9:45.', 'Lesson 3: 9:45 to 10:20. The last lesson ends at 10:20 am.'],
         src=['Mei has 3 lessons in a row. Each lesson is 35 minutes long, with a 10-minute break between lessons. The first lesson starts at 8:15 am. What time does the last lesson end?']),
    dict(id='M', tier='challenge', no='Make up your own', label='Make', type='selfcheck', open=True, skill='making puzzles', marking_mode='open',
         q='Make up a jug puzzle with two jugs and a goal. Check it by writing every pour in a table. Write your puzzle and your steps in the box.',
         hint='Pick two jug sizes and a goal. Try the pours and write how much is in each jug after every step. Can the goal really be made?',
         steps=['Many answers are right. Example: a 4 ℓ jug and a 9 ℓ jug, goal 1 ℓ:'] + jug_text((4, 9), jug_fewest((4, 9), 1)[1]),
         src=['a jug puzzle with two jugs and a goal. Check it by writing every pour in a table.']),
]
for _d in ITEMS:
    _d.setdefault('strand', STRAND)
    if _d['type'] == 'selfcheck':
        _d.setdefault('marking_mode', 'self')


# ---------------------------------------------------------------- variant families (template + independent oracle over EVERY combination)
def trip_oracle(e):
    return trip_minutes(e['h'], e['m'], e['h'] + 1, e['n'])


VARIANTS = {
    '4a': dict(
        base=dict(red=64, diff=18),
        tpl=dict(vars=dict(red=[64, 70, 72, 80, 90, 100], diff=[12, 15, 18, 24]), answer='red-diff',
                 q='Siti has a red ribbon {red} cm long. Her blue ribbon is {diff} cm shorter than the red ribbon. How long is the blue ribbon? Type the number of cm.',
                 hint='The blue ribbon is {diff} cm shorter than the red one. Should you add {diff} or take {diff} away?',
                 steps=['Shorter means take away: {red} − {diff}.', '{red} − {diff} = {ans}, so the blue ribbon is {ans} cm long.']),
        oracle=lambda e: blue_of(e['red'], e['diff'])),
    '4b': dict(
        base=dict(red=64, diff=18, ov=5),
        tpl=dict(vars=dict(red=[64, 70, 72, 80, 90], diff=[12, 15, 18, 24], ov=[3, 4, 5, 6]), derive=dict(blue='red-diff', both='red+red-diff'), answer='red+red-diff-ov',
                 q='Siti’s red ribbon is {red} cm long. Her blue ribbon is {diff} cm shorter. She glues them end to end with a {ov} cm overlap. How long is the new ribbon? Type the number of cm.',
                 hint='Both ribbons added together would count the overlap two times. How can you fix that?',
                 steps=['The blue ribbon is {blue} cm. Side by side, {red} + {blue} = {both} cm.', 'The {ov} cm overlap was counted twice, so take it away once: {both} − {ov} = {ans}.', 'The new ribbon is {ans} cm long.']),
        fig=lambda e: ribbon_fig(e['red'], e['diff'], e['ov']),
        oracle=lambda e: ribbon_joined(e['red'], e['diff'], e['ov'])),
    '5c': dict(
        base=dict(h=10, m=45, n=30),
        tpl=dict(vars=dict(h=[7, 8, 9, 10], m=[30, 40, 45, 50], n=[10, 15, 20, 25, 30]), derive=dict(eh='h+1', first='60-m'), answer='60-m+n',
                 q='Mei’s family leaves home at {h}:{m} am. They reach Grandma’s flat at {eh}:{n} am. How long is the trip? Type the number of minutes.',
                 hint='Count on from {h}:{m} to the next o’clock first. Then count the rest of the way.',
                 steps=['{h}:{m} to {eh}:00 is {first} minutes.', '{eh}:00 to {eh}:{n} is {n} minutes.', '{first} + {n} = {ans} minutes.']),
        oracle=trip_oracle),
    'T3': dict(
        base=dict(k=3, j=2, a=100),
        tpl=dict(vars=dict(k=[3, 4], j=[2, 3], a=[50, 100, 200]), derive=dict(w='(k+j)*a', t='k+j', ap='a', po='k*a'),
                 answers=dict(f1='a', f2='k*a'), frame='Apple {f1} g   Pomelo {f2} g',
                 q='{k} apples balance 1 pomelo. The pomelo and {j} apples together balance a {w} g weight. How heavy is one apple? How heavy is the pomelo?',
                 hint='Swap the pomelo for what balances it. Then how many apples balance the {w} g weight?',
                 steps=['Swap the pomelo for {k} apples: {k} apples and {j} apples balance {w} g, so {t} apples balance {w} g.', '1 apple is {w} ÷ {t} = {ap} g. The pomelo balances {k} apples: {k} × {ap} = {po} g.']),
        oracle=lambda e: (lambda w: (lambda x: dict(f1=x, f2=e['k'] * x))(next(x for x in range(1, 2001) if e['k'] * x + e['j'] * x == w)))((e['k'] + e['j']) * e['a'])),
}

# ---- inquiry habit (docs/pedagogy/inquiry_skills_explicit.md; levels/habits.json)
ITEMS.insert(max(i for i, x in enumerate(ITEMS) if x['tier'] == 'core') + 1, habit_item('Check',
    'Ali pours 2 L and then 3 L of water into a tank. Now test a second case: he pours 3 L and then 2 L. Does the total change when the order changes? Write how you know.',
    ['First case: 2 L + 3 L = 5 L.', 'Second case: 3 L + 2 L = 5 L.', 'The total is 5 L both times. For adding amounts, the order does not change the total. Writing each pour in a table helps me check.'],
    'Work out the first total. Then work out the second one. Are they the same?'))
