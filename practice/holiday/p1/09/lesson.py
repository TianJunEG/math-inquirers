"""Online practice for Level 1 (Primary 1, ages 6-8) holiday lesson 9: Length ("Measure It!").

Questions as printed in the Level 1 holiday workbook (hp/workbook_html.js lesson 9, Q1 to Q6; hp/qbank.json lesson 9 stretch[0:4] for Think harder and challenge[-3:] for Go further, as the
workbook builder slices them; hp/gaps.json lesson 9 for the Investigation).  Every answer is recomputed by an independent checker: squares are counted from the drawn cells, units are laid
end to end one at a time, ruler lengths are found by hopping from mark to mark, and puzzles are solved by trying numbers.  The build stops if a checker and the printed answer (Tutor Guide
answer key) differ.
"""
import os, sys
from fractions import Fraction
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from p1lib import *      # noqa: E402,F401

META = dict(level=1, lesson=9, key='p1', title='Measure It!', workbook_title='MEASURE IT!', topic='Length',
            strand='Length and measuring',
            sources=['hp/workbook_html.js', 'hp/qbank.json', 'hp/gaps.json'],
            intro=['Measure with equal units, with no gaps and no overlaps. Start at one end. On a ruler, count the spaces.',
                   'Some questions need your own pencil, a cube strip or a ruler. Do those at home, then check against the answer shown on screen.'])

S = 'Length and measuring'


def D(**k):
    return dict(strand=S, **k)


# ---- independent checkers
def lay(length, unit):
    """How many units laid end to end, one at a time, to cover `length` exactly (the length is a whole number of units)."""
    n, covered = 0, Fraction(0)
    while covered < length:
        covered += unit
        n += 1
    return n


def hop(a, b):
    """Hop from mark a to mark b on a ruler, counting each space."""
    n, x = 0, a
    while x < b:
        x += 1
        n += 1
    return n


def uniq(vals):
    return vals[0] if len(vals) == 1 else None


def n_clips(erasers, per):
    """Group erasers `per` at a time: how many whole clips."""
    n, left = 0, erasers
    while left >= per:
        left -= per
        n += 1
    return n if left == 0 else None


def n_erasers(clips, per):
    t = 0
    for _ in range(clips):
        t += per
    return t


def train_length(n, car, gap):
    t = 0
    for i in range(n):
        t += car
        if i < n - 1:
            t += gap
    return t


def three_pieces(total, d):
    """A ribbon cut in three: first d longer than the second, third d shorter than the second."""
    return uniq([(s + d, s, s - d) for s in range(d + 1, total) if (s + d) + s + (s - d) == total])


RIB = dict(A=7, B=5, C=9)
CELLS = ribbon_cells(RIB)
SIZE = {nm: len(cs) for nm, cs in CELLS.items()}          # squares counted from the drawn cells
RIBBON_OPTS = ['Ribbon A', 'Ribbon B', 'Ribbon C']
RIB_FIG = lambda: ribbons_fig(RIB, 28, 'Three ribbons made of equal squares: A, B and C')

CLIPS, ERASERS, PER = 5, 12, 2
CLIP_FIG = lambda: clip_eraser_fig(CLIPS, ERASERS, PER)
MEI, ALI_MORE, BEN_LESS = 8, 3, 2
CUBE_FIG = lambda: pencil_cubes_fig(MEI, ALI_MORE, BEN_LESS)
RULER6 = [(3, 8, 'crayon'), (0, 12, 'pencil')]
RULER_FIG = lambda: ruler_fig([RULER6[1], RULER6[0]], 0, 12, 26, 'A ruler from 0 to 12 centimetres. The pencil lies from 0 to 12 and the crayon from 3 to 8.')
DESK = 48                                                  # any desk length: the same desk for both children

ITEMS = [
    # ================= Start here
    D(id='1a', tier='core', no='1(a)', label='1(a)', type='choice', skill='comparing lengths', options=RIBBON_OPTS, answer='Ribbon C', svg=RIB_FIG(),
      q='Three ribbons are made of equal squares. Which ribbon is the longest?',
      check=lambda: 'Ribbon ' + uniq([nm for nm in SIZE if SIZE[nm] == max(SIZE.values())]),
      hint='Count the squares in each ribbon. Or look at which ribbon reaches furthest to the right.',
      steps=['Count the squares: ribbon A has 7, ribbon B has 5 and ribbon C has 9.', '9 is the biggest number.', 'Ribbon C is the longest.'],
      src=['Three ribbons are made of equal squares.', 'Which ribbon is the longest?']),
    D(id='1b', tier='core', no='1(b)', label='1(b)', type='choice', skill='comparing lengths', options=RIBBON_OPTS, answer='Ribbon B', svg=RIB_FIG(),
      q='Three ribbons are made of equal squares. Which ribbon is the shortest?',
      check=lambda: 'Ribbon ' + uniq([nm for nm in SIZE if SIZE[nm] == min(SIZE.values())]),
      hint='All three ribbons start at the same place. Which one stops first? Count the squares to check.',
      steps=['Count the squares: ribbon A has 7, ribbon B has 5 and ribbon C has 9.', '5 is the smallest number.', 'Ribbon B is the shortest.'],
      src=['Which is the shortest?']),
    D(id='1c', tier='core', no='1(c)', label='1(c)', type='number', skill='comparing lengths', answer=2, svg=RIB_FIG(),
      q='How many squares longer is ribbon A than ribbon B?', check=lambda: SIZE['A'] - SIZE['B'],
      hint='Count the squares of ribbon A and of ribbon B. How many squares does A have that B does not have?',
      steps=['Ribbon A has 7 squares and ribbon B has 5 squares.', 'The first 5 squares are the same. A has 2 squares more.', 'Ribbon A is 2 squares longer.'],
      src=['How many squares longer is ribbon A than ribbon B?']),
    D(id='1d', tier='core', no='1(d)', label='1(d)', type='number', skill='joining lengths', answer=12, svg=RIB_FIG(),
      q='Ribbon A and ribbon B are put end to end. How many squares long is that?', check=lambda: SIZE['A'] + SIZE['B'],
      hint='End to end means one ribbon after the other. How many squares are there in all?',
      steps=['Ribbon A has 7 squares and ribbon B has 5 squares.', '7 + 5 = 12.', 'The two ribbons together are 12 squares long.'],
      src=['Ribbon A and ribbon B are put end to end. How many squares long is that?']),
    D(id='1e', tier='core', no='1(e)', label='1(e)', type='choice', skill='comparing lengths', options=['Ribbon A', 'Ribbon B', 'No ribbon'], answer='Ribbon A', svg=RIB_FIG(),
      q='Ribbon C is cut shorter by 2 squares. Which ribbon is it now the same length as?',
      check=lambda: (lambda n: 'Ribbon ' + n if n else 'No ribbon')(uniq([nm for nm in SIZE if nm != 'C' and SIZE[nm] == SIZE['C'] - 2])),
      hint='Take 2 squares off ribbon C. Count the squares that are left. Is there a ribbon with that many?',
      steps=['Ribbon C has 9 squares. Cut 2 squares off: 9 - 2 = 7 squares.', 'Ribbon A has 7 squares.', 'Ribbon C is now the same length as ribbon A.'],
      src=['Ribbon C is cut shorter by 2 squares. Which ribbon is it now the same length as?']),

    D(id='2', tier='core', no='2', label='Q2', type='selfcheck', paper=True, open=True, skill='estimating and measuring',
      q='Measure with the cube strip from the back of the workbook. Guess first, then measure: a pencil, a book, a shoe and one thing you choose. Write your guess, what you measured, and how far off your guess was.',
      sol_fig=lambda f: example_table([['Object', 'Guess', 'Measured', 'How far off'], *[[nm, str(g), str(m), str(max(g, m) - min(g, m))] for nm, g, m in (('Pencil', 12, 14), ('Book', 20, 18), ('Shoe', 15, 15))]],
                                      'Example only: a pencil guessed 12 and measured 14 is 2 off; a book guessed 20 and measured 18 is 2 off; a shoe guessed 15 and measured 15 is 0 off'),
      hint='Guess before you measure. Lay the cubes along the object from one end, with no gaps and no overlaps, and count them.',
      steps=['Guess first. Then lay the cube strip along the object, starting at one end, with no gaps and no overlaps. Count the cubes.', 'How far off = the bigger of your two numbers take away the smaller. A guess of 12 and a measure of 14 is 2 off.',
             'The table above is only an example. Your numbers will be different, and that is fine.'],
      src=['Write what you guessed, what you measured, and how far off your guess was.']),
    D(id='2a', tier='core', no='2(a)', label='2(a)', type='selfcheck', open=False, marking_mode='self', skill='equal units',
      q='Why must every cube be the same size?', check=lambda: lay(Fraction(12), Fraction(2)) != lay(Fraction(12), Fraction(3)),
      hint='Imagine measuring a book with some big cubes and some tiny cubes. Could you compare it fairly with a shoe?',
      steps=['If the cubes are different sizes, the number of cubes does not tell you the real length.', 'With cubes that are all the same size, the numbers for different things can be compared fairly.', 'Any answer like this is good.'],
      src=['Why must every cube be the same size?']),

    D(id='3a', tier='core', no='3(a)', label='3(a)', type='choice', skill='units and counts', options=['Ali', 'Mei'], answer='Ali', svg=desk_fig(6, 8),
      q="Ali's desk is 6 spans long. Mei measures the same desk and gets 8 spans. Whose span is longer?",
      check=lambda: 'Ali' if Fraction(DESK, 6) > Fraction(DESK, 8) else 'Mei',
      hint='Both children measured the same desk. Look at the picture: whose spans are wider?',
      steps=['Both children measured the same desk.', 'Ali needed 6 spans and Mei needed 8 spans.', "Ali's span is longer."],
      src=['Ali’s desk is 6 spans long. Mei measures the same desk: 8 spans.', 'Whose span is longer?']),
    D(id='3b', tier='core', no='3(b)', label='3(b)', type='selfcheck', open=False, marking_mode='self', skill='units and counts', svg=desk_fig(6, 8),
      q='Explain how you know whose span is longer.', check=lambda: 'Ali' if Fraction(DESK, 6) > Fraction(DESK, 8) else 'Mei',
      hint='Both children measured the same desk. What does it mean that one child needed more spans than the other?',
      steps=['Both children measured the same desk, so the total length is the same.', 'A longer span covers more of the desk, so you need fewer of them.', 'Any answer that says this in your own words is good.'],
      src=['How do you know?']),

    D(id='4a', tier='core', no='4(a)', label='4(a)', type='number', skill='changing units', answer=10, svg=CLIP_FIG(),
      q='1 clip is as long as 2 erasers. A desk is 5 clips long. How many erasers long is the desk? Draw it on paper or count in 2s.', check=lambda: n_erasers(CLIPS, PER),
      hint='Each clip is 2 erasers. Count the erasers one clip at a time.',
      steps=['1 clip is 2 erasers.', 'Count in 2s, one clip at a time, 5 times: 2, 4, 6, 8, 10.', 'The desk is 10 erasers long.'],
      src=['1 clip = 2 erasers.', 'A desk is 5 clips. How many erasers?']),
    D(id='4b', tier='core', no='4(b)', label='4(b)', type='number', skill='changing units', answer=6, svg=CLIP_FIG(),
      q='1 clip is as long as 2 erasers. A pencil is 12 erasers long. How many clips long is the pencil?', check=lambda: n_clips(ERASERS, PER),
      hint='Put the erasers into pairs. Each pair is one clip. How many pairs?',
      steps=['1 clip is 2 erasers, so take the 12 erasers 2 at a time.', '2, 4, 6, 8, 10, 12 is 6 pairs.', 'The pencil is 6 clips long.'],
      src=['A pencil is 12 erasers long. How many clips?']),

    D(id='5a', tier='core', no='5(a)', label='5(a)', type='number', skill='comparing lengths', answer=11, svg=CUBE_FIG(),
      q="Mei's pencil is 8 cubes long. Ali's pencil is 3 cubes longer than Mei's. How many cubes long is Ali's pencil?", check=lambda: MEI + ALI_MORE,
      hint="Ali's pencil is as long as Mei's and then some more. How many more?",
      steps=["Mei's pencil is 8 cubes.", "Ali's is 3 cubes longer: 8 + 3 = 11.", "Ali's pencil is 11 cubes long."],
      src=['Mei’s pencil is 8 cubes. Ali’s is 3 cubes longer. Ben’s is 2 cubes shorter.', 'How long is Ali’s pencil?']),
    D(id='5b', tier='core', no='5(b)', label='5(b)', type='number', skill='comparing lengths', answer=6, svg=CUBE_FIG(),
      q="Mei's pencil is 8 cubes long. Ben's pencil is 2 cubes shorter than Mei's. How many cubes long is Ben's pencil?", check=lambda: MEI - BEN_LESS,
      hint="Ben's pencil is shorter than Mei's. Take away the cubes that it is shorter by.",
      steps=["Mei's pencil is 8 cubes.", "Ben's is 2 cubes shorter: 8 - 2 = 6.", "Ben's pencil is 6 cubes long."],
      src=['How long is Ben’s pencil?']),
    D(id='5c', tier='core', no='5(c)', label='5(c)', type='number', skill='joining lengths', answer=25, svg=CUBE_FIG(),
      q="Mei's pencil is 8 cubes long. Ali's is 3 cubes longer. Ben's is 2 cubes shorter. All three pencils are put end to end. How many cubes long is that?",
      check=lambda: MEI + (MEI + ALI_MORE) + (MEI - BEN_LESS),
      hint="Find the length of each of the three pencils first. Then add them up.",
      steps=["Mei's pencil is 8 cubes, Ali's is 11 cubes and Ben's is 6 cubes.", '8 + 11 = 19, and 19 + 6 = 25.', 'The three pencils end to end are 25 cubes long.'],
      src=['All three end to end: ____ cubes?']),

    D(id='6a', tier='core', no='6(a)', label='6(a)', type='number', skill='reading a ruler', answer=12, svg=RULER_FIG(),
      q='Read the ruler. The pencil goes from 0 to 12. How many cm long is it?', check=lambda: hop(RULER6[1][0], RULER6[1][1]),
      hint='Start at the 0 mark. Count the spaces between the marks as you go along the ruler.',
      steps=['The pencil starts at 0 and ends at 12.', 'Count the spaces from 0 to 12: there are 12.', 'The pencil is 12 cm long.'],
      src=['Read the ruler.', 'The pencil goes from 0 to 12 cm. How long?']),
    D(id='6b', tier='core', no='6(b)', label='6(b)', type='number', skill='reading a ruler', answer=5, svg=RULER_FIG(),
      q='Read the ruler. The crayon goes from 3 to 8. How many cm long is it? Hop from 3 to 8, counting each space.', check=lambda: hop(RULER6[0][0], RULER6[0][1]),
      hint='The crayon does not start at 0. Put a finger on 3 and hop along to 8, counting each space.',
      steps=['The crayon starts at the 3 mark and ends at the 8 mark.', 'Hop from 3 to 8: 4, 5, 6, 7, 8. That is 5 hops.', 'The crayon is 5 cm long.'],
      src=['The crayon goes from 3 to 8 cm. How long? (Hop from 3 to 8.)']),
    D(id='6c', tier='core', no='6(c)', label='6(c)', type='selfcheck', paper=True, open=True, skill='reading a ruler',
      q='Measure your own pencil with a ruler. How many cm long is it? Is it longer or shorter than 10 cm?',
      hint='Put the 0 mark of the ruler at one end of your pencil. Read the number at the other end.',
      steps=['Put the 0 mark of the ruler at one end of your pencil.', 'Read the number at the other end of the pencil. That is its length in cm.', 'Compare it with 10: it is longer than 10 cm, shorter than 10 cm, or exactly 10 cm. The answer depends on your pencil.'],
      src=['My pencil: ____ cm. Longer or shorter than 10 cm?']),

    # ================= Investigation: Is it always true?
    D(id='I1', tier='invest', no='Investigation 1', label='Inv 1', type='selfcheck', paper=True, open=True, skill='measuring with two units',
      q='Measure your pencil with the cube strip and write the number. Then measure the same pencil with a paper clip (or your finger width) and write that number.',
      hint='Lay the unit end to end along the pencil, again and again, with no gaps. Start at one end of the pencil.',
      steps=['Lay the cube strip along the pencil from one end, with no gaps. Count the cubes and write the number.', 'Do the same with a paper clip (or your finger width): lay it end to end, again and again, and count.',
             'Write both numbers. Keep them for the next questions. Your numbers will not be the same as an example, and that is fine.'],
      src=['Measure your pencil with the cube strip. Write the number. Then measure it with a paper clip (or your finger width). Write the number.']),
    D(id='I2', tier='invest', no='Investigation 2', label='Inv 2', type='choice', skill='units and counts', options=['Ali', 'Mei'], answer='Ali',
      q='A pencil is 12 cm long. Ali measures it with units that are 2 cm long. Mei measures it with units that are 3 cm long. Who gets the bigger number?',
      check=lambda: 'Ali' if lay(12, 2) > lay(12, 3) else 'Mei',
      hint='Lay the units end to end along the pencil. Which child lays more units?',
      steps=['Ali lays 2 cm units: 2, 4, 6, 8, 10, 12. That is 6 units.', 'Mei lays 3 cm units: 3, 6, 9, 12. That is 4 units.', '6 is bigger than 4, so Ali gets the bigger number.'],
      src=['Which unit is shorter? Which one gave the bigger number?']),
    D(id='I3', tier='invest', no='Investigation 3', label='Inv 3', type='choice', skill='units and counts', options=['Yes', 'No'], answer='Yes',
      q='Ben says: "If I measure the same thing with a SHORTER unit, I always get a BIGGER number." Is Ben right?',
      check=lambda: 'Yes' if all(Fraction(L) / u > Fraction(L) / v for L in range(1, 41) for u in range(1, 11) for v in range(u + 1, 12)) else 'No',
      hint='Think about covering the same path with small steps and with big steps. Which needs more steps?',
      steps=['To cover the same length you need more of a shorter unit.', 'For example, a 12 cm pencil is 6 units of 2 cm but only 4 units of 3 cm.', 'So Ben is right. A shorter unit always gives a bigger number (counting part of a unit too).'],
      src=['Ben says: "If I measure the same thing with a SHORTER unit, I always get a BIGGER number."']),
    D(id='I4', tier='invest', no='Investigation 4', label='Inv 4', type='number', skill='units and counts', answer=24,
      q='Your pencil is 12 cubes long. A new unit is half as long as a cube. How many of the new units long is the pencil?', check=lambda: lay(Fraction(12), Fraction(1, 2)),
      hint='Two of the new units make one cube. How many cubes are there in the pencil?',
      steps=['One cube is 2 of the new half-cube units.', 'The pencil is 12 cubes long, so it is 12 groups of 2 units: 2 + 2 + ... (12 times).', '12 x 2 = 24, so the pencil is 24 of the new units long.'],
      src=['Guess: if a unit is half as long as a cube, what number would you get for your pencil?']),
    D(id='I5', tier='invest', no='Investigation 5', label='Inv 5', type='selfcheck', open=False, marking_mode='self', skill='explaining units',
      q='You measure the same thing with a longer unit and with a shorter unit. What do you notice about the two numbers?', check=lambda: (lay(12, 2), lay(12, 3)),
      hint='Think about walking along the same path with big steps and with tiny steps.',
      steps=['The shorter unit gives the bigger number, because you need more of them to cover the same length.', 'A unit half as long gives twice the number. A pencil of 12 cubes is 24 half cubes.', 'Any answer that says "shorter unit, more of them" is good.'],
      src=['Look for: units laid end to end with no gaps']),

    # ================= Think harder
    D(id='T1', tier='stretch', no='T1', label='T1', type='number', skill='reading a ruler', answer=8, svg=ruler_fig([(3, 11, 'ribbon')], 0, 12, 26, 'A ruler with a ribbon from the 3 cm mark to the 11 cm mark'),
      q='A ribbon lies from the 3 cm mark to the 11 cm mark on a ruler. How many cm long is it?', check=lambda: hop(3, 11),
      hint='The ribbon does not start at 0. Hop from the 3 mark to the 11 mark and count the spaces.',
      steps=['The ribbon starts at 3 and ends at 11.', 'Hop from 3 to 11 counting each space: 4, 5, 6, 7, 8, 9, 10, 11. That is 8 hops.', 'The ribbon is 8 cm long.'],
      src=['A ribbon lies from the 3 cm mark to the 11 cm mark on a ruler. How long is it?']),
    D(id='T2a', tier='stretch', no='T2 which', label='T2 which', type='choice', skill='comparing on a ruler', options=['Red', 'Blue'], answer='Red',
      svg=ruler_fig([(2, 9, 'red'), (5, 11, 'blue')], 0, 12, 26, 'A ruler with a red ribbon from 2 to 9 and a blue ribbon from 5 to 11'),
      q='A red ribbon lies from the 2 cm mark to the 9 cm mark. A blue ribbon lies from the 5 cm mark to the 11 cm mark. Which ribbon is longer?',
      check=lambda: 'Red' if hop(2, 9) > hop(5, 11) else 'Blue',
      hint='The ribbons start at different marks. Work out how many cm long each ribbon is. Then compare.',
      steps=['The red ribbon goes from 2 to 9, so it is 7 cm long.', 'The blue ribbon goes from 5 to 11, so it is 6 cm long.', 'The red ribbon is longer.'],
      src=['A red ribbon lies from the 2 cm mark to the 9 cm mark. A blue ribbon lies from the 5 cm mark to the 11 cm mark. Which ribbon is longer? By how many cm?']),
    D(id='T2b', tier='stretch', no='T2 by', label='T2 by', type='number', skill='comparing on a ruler', answer=1,
      svg=ruler_fig([(2, 9, 'red'), (5, 11, 'blue')], 0, 12, 26, 'A ruler with a red ribbon from 2 to 9 and a blue ribbon from 5 to 11'),
      q='A red ribbon lies from the 2 cm mark to the 9 cm mark. A blue ribbon lies from the 5 cm mark to the 11 cm mark. How many cm longer is the longer ribbon?',
      check=lambda: abs(hop(2, 9) - hop(5, 11)),
      hint='Find the length of each ribbon in cm. Then find the difference.',
      steps=['The red ribbon is 7 cm long and the blue ribbon is 6 cm long.', '7 - 6 = 1.', 'The longer ribbon is 1 cm longer.'],
      src=['By how many cm?']),
    D(id='T3a', tier='stretch', no='T3 pen', label='T3 pen', type='number', skill='changing units', answer=4,
      q='1 clip is as long as 3 cubes. A pen is 12 cubes long. How many clips long is the pen?', check=lambda: n_clips(12, 3),
      hint='Put the cubes into groups of 3. Each group is one clip.',
      steps=['1 clip is 3 cubes, so take the 12 cubes 3 at a time.', '3, 6, 9, 12 is 4 groups.', 'The pen is 4 clips long.'],
      src=['1 clip is as long as 3 cubes. A pen is 12 cubes long. How many clips long is the pen?']),
    D(id='T3b', tier='stretch', no='T3 ruler', label='T3 ruler', type='number', skill='changing units', answer=15,
      q='1 clip is as long as 3 cubes. A ruler is 5 clips long. How many cubes long is the ruler?', check=lambda: n_erasers(5, 3),
      hint='Each clip is 3 cubes. Count the cubes one clip at a time.',
      steps=['1 clip is 3 cubes.', 'Count in 3s, 5 times: 3, 6, 9, 12, 15.', 'The ruler is 15 cubes long.'],
      src=['A ruler is 5 clips long. How many cubes long is the ruler?']),
    D(id='T4', tier='stretch', no='T4', label='T4', type='number', skill='changing units', answer=24,
      q='A pencil is 3 erasers long. A ruler is 2 pencils long. A desk is 4 rulers long. How many erasers long is the desk?',
      check=lambda: n_erasers(4, n_erasers(2, 3)),
      hint='Work out how many erasers long one ruler is first. Then think about the desk.',
      steps=['A pencil is 3 erasers. A ruler is 2 pencils: 3 + 3 = 6 erasers.', 'A desk is 4 rulers: 6 + 6 + 6 + 6 = 24 erasers.', 'The desk is 24 erasers long.'],
      src=['A pencil is 3 erasers long. A ruler is 2 pencils long. A desk is 4 rulers long. How many erasers long is the desk?']),

    # ================= Go further
    D(id='C1a', tier='challenge', no='Go further 1(a)', label='G1(a)', type='number', skill='lengths with gaps', answer=20,
      q='A train has 3 carriages. Each carriage is 6 cubes long. There is a gap of 1 cube between one carriage and the next. How many cubes long is the whole train?',
      check=lambda: train_length(3, 6, 1),
      hint='Draw the carriages in a row, with a gap between each two carriages. Count the cubes in the carriages and in the gaps.',
      steps=['The 3 carriages are 6 + 6 + 6 = 18 cubes.', 'There is a gap between the first and second carriage, and between the second and third: 2 gaps of 1 cube.', '18 + 2 = 20, so the train is 20 cubes long.'],
      src=['A train has 3 carriages. Each is 6 cubes long. There is a gap of 1 cube between carriages. How long is the whole train? What if there are 5 carriages?']),
    D(id='C1b', tier='challenge', no='Go further 1(b)', label='G1(b)', type='number', skill='lengths with gaps', answer=34,
      q='A train has 5 carriages. Each carriage is 6 cubes long. There is a gap of 1 cube between one carriage and the next. How many cubes long is the whole train?',
      check=lambda: train_length(5, 6, 1),
      hint='Draw the carriages in a row, with a gap between each two carriages. Count the cubes in the carriages and in the gaps.',
      steps=['The 5 carriages are 6 + 6 + 6 + 6 + 6 = 30 cubes.', 'Between 5 carriages in a row there are 4 gaps of 1 cube.', '30 + 4 = 34, so the train is 34 cubes long.'],
      src=['What if there are 5 carriages?']),
    D(id='C2', tier='challenge', no='Go further 2', label='G2', type='fields', skill='finding parts of a length', answer=[14, 10, 6],
      q='A ribbon 30 cubes long is cut into three pieces. The first piece is 4 cubes longer than the second. The third piece is 4 cubes shorter than the second. How long is each piece?',
      frame='First: {f1}   Second: {f2}   Third: {f3}', check=lambda: list(three_pieces(30, 4)),
      hint='Try a length for the second piece. Work out the other two pieces and add all three. Is the total 30?',
      steps=['Try the second piece = 10: the first is 14 and the third is 6.', '14 + 10 + 6 = 30, so it works.', 'The pieces are 14, 10 and 6 cubes long.'],
      src=['A ribbon 30 cubes long is cut into three pieces. The first is 4 cubes longer than the second. The third is 4 cubes shorter than the second. How long is each piece?']),
    D(id='C3', tier='challenge', no='Go further 3', label='G3', type='selfcheck', open=True, marking_mode='open', skill='making a measuring puzzle',
      q='Make up your own measuring puzzle that uses TWO different units (for example clips and cubes). Write the puzzle and its answer. Ask a friend or a grown-up to solve it and check their answer.',
      hint='Pick the link between the two units first, like 1 clip is as long as 4 cubes. Then make a question that uses both units.',
      steps=['One example: 1 clip is as long as 4 cubes. A snake is 5 clips long. How many cubes long is it?', 'Answer: 5 clips of 4 cubes is 4 + 4 + 4 + 4 + 4 = 20 cubes.', 'Your puzzle needs the link between the units, a question and an answer that works.'],
      src=['Make up your own measuring puzzle that uses TWO different units']),
]


def _ruler_fig(e):
    return ruler_fig([(e['a'], e['a'] + e['n'], 'ribbon')], 0, 12, 26, f'A ruler with a ribbon from the {e["a"]} cm mark to the {e["a"] + e["n"]} cm mark')


_ruler = dict(vars=dict(a=[1, 2, 3, 4, 5], n=[3, 4, 5, 6, 7]), derive=dict(b='a+n'), q='A ribbon lies from the {a} cm mark to the {b} cm mark on a ruler. How many cm long is it?', answer='n',
              hint='The ribbon does not start at 0. Hop from the {a} mark to the {b} mark and count the spaces.',
              steps=['The ribbon starts at {a} and ends at {b}.', 'Hop from {a} to {b}, counting each space.', 'The ribbon is {ans} cm long.'])

VARIANTS = {
    '1c': dict(base=dict(a=7, b=5),
               tpl=dict(vars=dict(a=[6, 7, 8, 9, 10, 11], b=[3, 4, 5]), q='Ribbon A is {a} squares long. Ribbon B is {b} squares long. How many squares longer is ribbon A than ribbon B?', answer='a-b',
                        hint='Think about how many squares ribbon A has that ribbon B does not have.',
                        steps=['Ribbon A has {a} squares and ribbon B has {b} squares.', 'The first {b} squares are the same. A has some more.', 'Ribbon A is {ans} squares longer.']),
               oracle=lambda e: lay(e['a'], 1) - lay(e['b'], 1)),
    '1d': dict(base=dict(a=7, b=5),
               tpl=dict(vars=dict(a=[6, 7, 8, 9, 10, 11], b=[3, 4, 5, 6]), q='Ribbon A is {a} squares long. Ribbon B is {b} squares long. They are put end to end. How many squares long is that?', answer='a+b',
                        hint='End to end means one ribbon after the other. How many squares are there in all?',
                        steps=['Ribbon A has {a} squares and ribbon B has {b} squares.', 'Add them: {a} + {b}.', 'The two ribbons are {ans} squares long.']),
               oracle=lambda e: lay(e['a'], 1) + lay(e['b'], 1)),
    '4a': dict(base=dict(k=2, n=5),
               tpl=dict(vars=dict(k=[2, 3, 4, 5], n=[3, 4, 5, 6, 7]), q='1 clip is as long as {k} erasers. A desk is {n} clips long. How many erasers long is the desk?', answer='k*n',
                        hint='Each clip is {k} erasers. Count the erasers one clip at a time.',
                        steps=['1 clip is {k} erasers.', 'Count in {k}s, {n} times.', 'The desk is {ans} erasers long.']),
               oracle=lambda e: n_erasers(e['n'], e['k'])),
    '4b': dict(base=dict(k=2, n=6),
               tpl=dict(vars=dict(k=[2, 3, 4, 5], n=[3, 4, 5, 6, 7]), derive=dict(m='k*n'), q='1 clip is as long as {k} erasers. A pencil is {m} erasers long. How many clips long is the pencil?', answer='n',
                        hint='Put the erasers into groups of {k}. Each group is one clip. How many groups?',
                        steps=['1 clip is {k} erasers, so take the {m} erasers {k} at a time.', 'Count the groups.', 'The pencil is {ans} clips long.']),
               oracle=lambda e: n_clips(e['k'] * e['n'], e['k'])),
    '5c': dict(base=dict(m=8, a=3, b=2),
               tpl=dict(vars=dict(m=[6, 7, 8, 9, 10], a=[2, 3, 4, 5], b=[1, 2, 3]), q="Mei's pencil is {m} cubes long. Ali's is {a} cubes longer. Ben's is {b} cubes shorter. All three pencils are put end to end. How many cubes long is that?",
                        answer='m+(m+a)+(m-b)',
                        hint="Find the length of each of the three pencils first. Then add them up.",
                        steps=["Mei's pencil is {m} cubes. Ali's is {m} and {a} more. Ben's is {m} take away {b}.", 'Add the three lengths.', 'The three pencils end to end are {ans} cubes long.']),
               oracle=lambda e: e['m'] + (e['m'] + e['a']) + (e['m'] - e['b'])),
    '6b': dict(base=dict(a=3, n=5),
               tpl=dict(_ruler), fig=_ruler_fig,
               oracle=lambda e: hop(e['a'], e['a'] + e['n'])),
    'T1': dict(base=dict(a=3, n=8),
               tpl=dict(vars=dict(a=[1, 2, 3, 4], n=[5, 6, 7, 8]), derive=dict(b='a+n'), q='A ribbon lies from the {a} cm mark to the {b} cm mark on a ruler. How many cm long is it?', answer='n',
                        hint='The ribbon does not start at 0. Hop from the {a} mark to the {b} mark and count the spaces.',
                        steps=['The ribbon starts at {a} and ends at {b}.', 'Hop from {a} to {b}, counting each space.', 'The ribbon is {ans} cm long.']),
               fig=_ruler_fig,
               oracle=lambda e: hop(e['a'], e['a'] + e['n'])),
    'I4': dict(base=dict(n=12),
               tpl=dict(vars=dict(n=[6, 8, 9, 10, 12, 14, 15]), q='Your pencil is {n} cubes long. A new unit is half as long as a cube. How many of the new units long is the pencil?', answer='2*n',
                        hint='Two of the new units make one cube. How many cubes are there in the pencil?',
                        steps=['One cube is 2 of the new half-cube units.', 'The pencil is {n} cubes long, so it is {n} groups of 2 units.', 'The pencil is {ans} of the new units long.']),
               oracle=lambda e: lay(Fraction(e['n']), Fraction(1, 2))),
    'T3a': dict(base=dict(k=3, n=4),
                tpl=dict(vars=dict(k=[2, 3, 4, 5], n=[3, 4, 5, 6]), derive=dict(m='k*n'), q='1 clip is as long as {k} cubes. A pen is {m} cubes long. How many clips long is the pen?', answer='n',
                         hint='Put the cubes into groups of {k}. Each group is one clip.',
                         steps=['1 clip is {k} cubes, so take the {m} cubes {k} at a time.', 'Count the groups.', 'The pen is {ans} clips long.']),
                oracle=lambda e: n_clips(e['k'] * e['n'], e['k'])),
    'T4': dict(base=dict(p=3, r=2, d=4),
               tpl=dict(vars=dict(p=[2, 3, 4], r=[2, 3], d=[2, 3, 4, 5]), q='A pencil is {p} erasers long. A ruler is {r} pencils long. A desk is {d} rulers long. How many erasers long is the desk?', answer='p*r*d',
                        hint='Work out how many erasers long one ruler is first. Then think about the desk.',
                        steps=['A ruler is {r} pencils of {p} erasers each.', 'A desk is {d} rulers. Add the rulers up.', 'The desk is {ans} erasers long.']),
               oracle=lambda e: n_erasers(e['d'], n_erasers(e['r'], e['p']))),
    'C1a': dict(base=dict(n=3, c=6),
                tpl=dict(vars=dict(n=[2, 3, 4, 5, 6, 7], c=[3, 4, 5, 6, 8, 10]), q='A train has {n} carriages. Each carriage is {c} cubes long. There is a gap of 1 cube between one carriage and the next. How many cubes long is the whole train?',
                         answer='n*c+n-1',
                         hint='Draw the carriages in a row, with a gap between each two carriages. Count the cubes in the carriages and in the gaps.',
                         steps=['The {n} carriages add up to {n} lots of {c} cubes.', 'Count the gaps between the carriages and add them on.', 'The train is {ans} cubes long.']),
                oracle=lambda e: train_length(e['n'], e['c'], 1)),
    'C2': dict(base=dict(t=30, d=4),
               tpl=dict(vars=dict(t=[24, 30, 36, 42, 48], d=[2, 3, 4, 5]), derive=dict(s='t//3'),
                        q='A ribbon {t} cubes long is cut into three pieces. The first piece is {d} cubes longer than the second. The third piece is {d} cubes shorter than the second. How long is each piece?',
                        frame='First: {f1}   Second: {f2}   Third: {f3}', answers=dict(f1='t//3+d', f2='t//3', f3='t//3-d'),
                        hint='Try a length for the second piece. Work out the other two pieces and add all three. Is the total {t}?',
                        steps=['The second piece is {s} cubes long.', 'The first piece is {d} more and the third piece is {d} less.', 'The pieces are {ans} cubes long.']),
               oracle=lambda e: dict(zip(('f1', 'f2', 'f3'), three_pieces(e['t'], e['d'])))),
}

for _d in ITEMS:
    if _d['type'] == 'selfcheck' and not _d.get('open') and 'marking_mode' not in _d:
        _d['marking_mode'] = 'self'
