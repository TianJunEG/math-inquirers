"""Level 2 (P2) holiday lesson 4: PATTERN MACHINES (Patterns with multiplication), week 2, second lesson.  Online mirror of the printed workbook pages.

The questions are the ones printed in the Level 2 holiday workbook (p2/content/l4.js `workbook()` = Start here, p2/gaps.json lesson 4 `invest` = Investigation,
p2/content/l4.js `qbank.stretch` first four = Think harder 1 to 4, `qbank.challenge` last three = Go further 5 to 7, as built by p2/workbook_html.js, and the
"Make up your own" line).  Every answer is recomputed by an INDEPENDENT checker (the pattern is built place by place, the tables are counted by their open sides,
the pictures are read); build_holiday.py stops if a checker and the printed answer differ.  Figures are the printed ones (p2/workbook_body.html) or redrawn for a phone.
"""
import os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from hlib import *          # noqa: E402,F401
from p2lib import *         # noqa: E402,F401

STRAND = 'Patterns with multiplication'
META = dict(level=2, lesson=4, key='p2', title='Pattern machines', workbook_title='PATTERN MACHINES', topic='Patterns with multiplication', strand=STRAND,
            sources=['p2/content/l4.js', 'p2/gaps.json', 'p2/workbook_html.js'],
            intro=['Use the pictures, counters or a drawing if they help you. Type numbers with a comma between them when a question asks for a list.',
                   'Some questions ask you to explain. Write your idea in the box, then read the worked solution after you submit and compare.'])


# ---------------------------------------------------------------- independent checkers (build the pattern place by place)
def one(lst, what):
    if len(lst) != 1:
        raise ValueError(f'{what}: {len(lst)} answers, expected exactly 1')
    return lst[0]


def build(group, places):
    """The pattern written out place by place: the group repeated until there are `places` shapes."""
    out = []
    while len(out) < places:
        out.extend(group)
    return out[:places]


def at(group, place):
    return build(group, place)[place - 1]


def places_of(group, what, upto):
    return [i + 1 for i, x in enumerate(build(group, upto)) if x == what]


def seats(tables):
    """Children round a row of square tables, one at each open side: count the sides of the squares that are not touching another square."""
    open_sides = 0
    for t in range(tables):
        open_sides += 2                                   # top and bottom of every square
        open_sides += 1 if t == 0 else 0                  # left end
        open_sides += 1 if t == tables - 1 else 0         # right end
    return open_sides


def sticks(houses):
    """Sticks in a row of houses: a post at each side, a floor stick under each house and two roof sticks on each house."""
    return (houses + 1) + houses + 2 * houses


def climb(start, step, count):
    return ap(start, step, count)


def both(a_start, a_step, b_start, b_step, limit):
    a = set(count_up_to(a_step, limit, a_start))
    b = set(count_up_to(b_step, limit, b_start))
    return sorted(a & b)


SHAPE_FIG = printed_fig('Shape pattern, places 1 to 10')
SHAPES = [w.strip() for w in re.search(r'places 1 to 10: (.*?)"', SHAPE_FIG).group(1).split(',')][:5]           # read from the picture
LETTER_FIG = printed_fig('Letter tiles')
LETTERS = re.search(r'Letter tiles ([A-Z ]+) in places', LETTER_FIG).group(1).split()[:4]
BEAD_FIG = printed_fig('A bead string')
FLOWER_FIG = printed_fig('A flower with 5 petals')
PETALS = FLOWER_FIG.count('<ellipse')
TABLES_FIG = printed_fig('Square tables in a row')
HOUSES_FIG = printed_fig('Houses made of sticks')
TOWERS_FIG = printed_fig('Towers of cubes')
BEADS = ['red'] * 2 + ['yellow'] * 3
FROG_A = number_line(0, 30, hops=[(0, 4)], circled=(0,), caption='Frog A starts at 0. Its first jump is 4.')
FROG_B = number_line(0, 30, hops=[(2, 5)], circled=(2,), caption='Frog B starts at 2. Its first jump is 3.')
FLOWER_TABLE = grid_table([('Petals', [5, '', '', '', '', ''])], head=('Flowers', [1, 2, 3, 4, 5, 6]),
                          caption='The flower table. Flowers 1, 2, 3, 4, 5, 6. Petals: 5 for 1 flower, then five empty boxes.')
TABLE_TABLE = grid_table([('Children', [4, 6, '', '', '', ''])], head=('Tables', [1, 2, 3, 4, 5, 6]),
                         caption='The tables table. Tables 1, 2, 3, 4, 5, 6. Children: 4 for 1 table, 6 for 2 tables, then four empty boxes.')
ALI, MEI = count_up_to(3, 36), count_up_to(4, 36)

ITEMS = [
    # ================= Start here (workbook lesson 4, No.1 to No.6)
    dict(id='1a', tier='core', no='1(a)', type='choice', options=['triangle', 'circle', 'square'], answer='square', skill='far places in a repeating pattern',
         q='This pattern keeps going in the same way. Here are places 1 to 10. What shape is in place 20?', svg=SHAPE_FIG,
         check=lambda: at(SHAPES, 20),
         hint='The pattern repeats in groups. How many shapes are in one group? Draw a line after the last shape of each group.',
         steps=['The pattern repeats every 5 shapes: triangle, circle, circle, square, square.', 'Each group ends at place 5, 10, 15, 20 ...', 'Place 20 is the last shape of a group, so it is a square.'],
         src=['This pattern keeps going in the same way. Here are places 1 to 10.', 'What shape is in place 20?']),
    dict(id='1b', tier='core', no='1(b)', type='choice', options=['triangle', 'circle', 'square'], answer='circle', skill='far places in a repeating pattern',
         q='Look at the same pattern. What shape is in place 23?', svg=SHAPE_FIG,
         check=lambda: at(SHAPES, 23),
         hint='Find the last place of a group that is close to 23. Then count on from there.',
         steps=['Place 20 is the last shape of a group.', 'Place 21 is a triangle, place 22 is a circle and place 23 is a circle.', 'Place 23 is a circle.'],
         src=['In place 23?']),
    dict(id='1c', tier='core', no='1(c)', type='choice', options=['triangle', 'circle', 'square'], answer='triangle', skill='far places in a repeating pattern',
         q='Look at the same pattern. What shape is in place 41?', svg=SHAPE_FIG,
         check=lambda: at(SHAPES, 41),
         hint='Find the last place of a group that is close to 41. Then count on from there.',
         steps=['Place 40 is the last shape of a group (8 groups of 5).', 'Place 41 starts a new group, and each group starts with a triangle.', 'Place 41 is a triangle.'],
         src=['What shape is in place 41?']),
    dict(id='1d', tier='core', no='1(c) how do you know', type='selfcheck', open=False, skill='far places in a repeating pattern',
         q='How do you know the shape in place 41? Write your idea in the box.', svg=SHAPE_FIG,
         facts=dict(group_length=5, place_40='square', place_41='triangle'),
         check=lambda: dict(group_length=len(SHAPES), place_40=at(SHAPES, 40), place_41=at(SHAPES, 41)),
         hint='Think about where a group ends, close to 41.',
         steps=['The pattern repeats every 5 shapes, so a group ends at 5, 10, 15 ... 40.', 'Place 40 is the end of a group (a square), so place 41 starts the next group with a triangle.', 'Any idea that uses the groups of 5 is a good one.'],
         src=['How do you know?']),

    dict(id='2a', tier='core', no='2(a)', type='choice', options=['M', 'A', 'T', 'H'], answer='A', skill='far places in a repeating pattern',
         q='Ali writes the letters M, A, T, H again and again. What is the 18th letter?', svg=LETTER_FIG,
         check=lambda: at(LETTERS, 18),
         hint='Keep writing M, A, T, H ... and count the places. Or find a place close to 18 where a group of letters ends.',
         steps=['A group is 4 letters: M, A, T, H. Groups end at places 4, 8, 12, 16.', 'Place 16 is an H. Then place 17 is M and place 18 is A.', 'The 18th letter is A.'],
         src=['Ali writes the letters M, A, T, H again and again.', 'What is the 18th letter?']),
    dict(id='2b', tier='core', no='2(b)', type='number', skill='far places in a repeating pattern', answer=40,
         q='Ali writes the letters M, A, T, H again and again. In which place is the 10th letter H?', svg=LETTER_FIG,
         check=lambda: places_of(LETTERS, 'H', 60)[9],
         hint='Write down the places of the first few Hs. What do you notice about them?',
         steps=['The Hs are in places 4, 8, 12, 16, 20, 24, 28, 32, 36, 40.', 'The 10th H is in place 40.'],
         src=['Where is the 10th letter H?']),
    dict(id='2c', tier='core', no='2(c)', type='number', skill='counting parts of a pattern', answer=7,
         q='Ali writes M, A, T, H again and again until he has written 30 letters. How many Ts does he write?', svg=LETTER_FIG,
         check=lambda: build(LETTERS, 30).count('T'),
         hint='How many whole groups of M, A, T, H are there in 30 letters? Is there a T in the letters left over?',
         steps=['A group has 4 letters. 7 groups use 28 letters and each group has 1 T: 7 Ts.', 'The last 2 letters are M and A. There is no T in them.', 'Ali writes 7 Ts.'],
         src=['Ali writes 30 letters. How many Ts does he write?']),
    dict(id='2d', tier='core', no='2(c) show how', type='selfcheck', open=False, skill='counting parts of a pattern',
         q='Show how you know how many Ts Ali writes in 30 letters. Write your idea in the box.', svg=LETTER_FIG,
         facts=dict(whole_groups=7, letters_left=2, ts=7),
         check=lambda: dict(whole_groups=len(build(LETTERS, 30)) // len(LETTERS), letters_left=len(build(LETTERS, 30)) % len(LETTERS), ts=build(LETTERS, 30).count('T')),
         hint='Draw a line after every group of 4 letters. Count the groups, then look at any letters left over.',
         steps=['30 letters make 7 whole groups of 4 and 2 letters left over (28 + 2 = 30).', 'Every whole group has one T. The 2 extra letters are M and A.', 'So there are 7 Ts.'],
         src=['Show how you know.']),

    dict(id='3a', tier='core', no='3(a)', type='number', skill='groups in a bead pattern', answer=18,
         q='Siti\'s bead string goes 2 red, 3 yellow, 2 red, 3 yellow ... It has 12 red beads and ends with yellow beads. How many yellow beads are there?', svg=BEAD_FIG,
         check=lambda: (lambda s: s.count('yellow'))(next(build(BEADS, n) for n in range(5, 100, 5) if build(BEADS, n).count('red') == 12)),
         hint='Draw one group. How many red beads are in one group? How many groups have 12 red beads?',
         steps=['One group is 2 red and 3 yellow. 12 red beads is 6 groups of 2 red (2, 4, 6, 8, 10, 12).', '6 groups have 6 × 3 = 18 yellow beads.'],
         src=['Siti’s bead string goes 2 red, 3 yellow, 2 red, 3 yellow … It has 12 red beads and ends with yellow beads.', 'How many yellow beads?']),
    dict(id='3b', tier='core', no='3(b)', type='number', skill='groups in a bead pattern', answer=30,
         q='Siti\'s bead string goes 2 red, 3 yellow, 2 red, 3 yellow ... It has 12 red beads and ends with yellow beads. How many beads are there altogether?', svg=BEAD_FIG,
         check=lambda: next(n for n in range(5, 100, 5) if build(BEADS, n).count('red') == 12),
         hint='How many beads are in one group? How many groups are there?',
         steps=['One group has 2 + 3 = 5 beads. There are 6 groups.', '6 groups of 5 beads: 5, 10, 15, 20, 25, 30.', 'There are 30 beads altogether.'],
         src=['How many beads altogether?']),

    dict(id='4t', tier='core', no='4(a)', type='fields', skill='multiplication tables as a pattern', answer=[10, 15, 20, 25, 30],
         q='Each flower has 5 petals. Fill in the Petals row of the table.', svg=stack(FLOWER_FIG, FLOWER_TABLE),
         frame='Petals: 5, {f1}, {f2}, {f3}, {f4}, {f5}', check=lambda: ap(5, 5, 6)[1:],
         hint='Each flower adds the same number of petals. What number do you add each time?',
         steps=['Each new flower adds 5 petals.', 'Counting in 5s: 5, 10, 15, 20, 25, 30.', 'The empty boxes are 10, 15, 20, 25 and 30.'],
         src=['Each flower has 5 petals.', 'Fill in the table.']),
    dict(id='4b', tier='core', no='4(b)', type='number', skill='multiplication tables as a pattern', answer=50,
         q='Each flower has 5 petals. How many petals are on 10 flowers?', svg=FLOWER_FIG,
         check=lambda: sum(PETALS for _ in range(10)),
         hint='Keep counting in 5s. How many 5s do you need?',
         steps=['Counting in 5s ten times: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50.', '10 flowers have 50 petals.'],
         src=['Petals on 10 flowers?']),
    dict(id='4c', tier='core', no='4(c)', type='number', skill='multiplication tables as a pattern', answer=7,
         q='Each flower has 5 petals. 35 petals make how many flowers?', svg=FLOWER_FIG,
         check=lambda: len(count_up_to(PETALS, 35)),
         hint='Count in 5s until you reach 35. How many 5s did you count?',
         steps=['Counting in 5s: 5, 10, 15, 20, 25, 30, 35.', 'That is 7 numbers, so 7 flowers.'],
         src=['35 petals make how many flowers?']),
    dict(id='4d', tier='core', no='4(d)', type='fields', skill='multiplication tables as a pattern', answer=[4, 3],
         q='Each flower has 5 petals. Mei has 23 petals. How many whole flowers can she make, and how many petals are left over?', svg=FLOWER_FIG,
         frame='{f1} flowers and {f2} petals left over', check=lambda: (lambda c: [len(c), 23 - c[-1]])(count_up_to(PETALS, 23)),
         hint='Count in 5s and stop before you pass 23. Then see how many petals are not used.',
         steps=['Counting in 5s: 5, 10, 15, 20. The next number, 25, is more than 23.', 'So Mei can make 4 flowers with 20 petals.', '23 - 20 = 3 petals are left over.'],
         src=['Mei has 23 petals. How many flowers?']),

    dict(id='5t', tier='core', no='5(a)', type='fields', skill='growing patterns', answer=[8, 10, 12, 14],
         q='Square tables are pushed together in a row. One child sits at each open side. Fill in the Children row of the table.', svg=stack(TABLES_FIG, TABLE_TABLE),
         frame='Children: 4, 6, {f1}, {f2}, {f3}, {f4}', check=lambda: [seats(n) for n in (3, 4, 5, 6)],
         hint='Look at the pictures. How many more children can sit when one more table is added?',
         steps=['1 table seats 4, 2 tables seat 6, 3 tables seat 8. Each new table adds 2 children.', '4, 6, 8, 10, 12, 14.', 'The empty boxes are 8, 10, 12 and 14.'],
         src=['Square tables are pushed together in a row. One child sits at each open side.', 'Fill in the table.']),
    dict(id='5b', tier='core', no='5(b)', type='number', skill='growing patterns', answer=22,
         q='Square tables are pushed together in a row, with one child at each open side. How many children sit at 10 tables?', svg=TABLES_FIG,
         check=lambda: seats(10),
         hint='Keep going with your table, or use the rule: how many more children for each new table?',
         steps=['Each new table adds 2 children: 4, 6, 8, 10, 12, 14, 16, 18, 20, 22.', '10 tables seat 22 children.'],
         src=['Children at 10 tables?']),
    dict(id='5c', tier='core', no='5(c)', type='number', skill='growing patterns', answer=9,
         q='Square tables are pushed together in a row, with one child at each open side. How many tables are needed for 20 children?', svg=TABLES_FIG,
         check=lambda: one([n for n in range(1, 30) if seats(n) == 20], 'tables'),
         hint='Keep adding to your table until you reach 20 children. Which table number is that?',
         steps=['Children: 4, 6, 8, 10, 12, 14, 16, 18, 20.', '20 is the 9th number, so 9 tables seat 20 children.'],
         src=['Tables for 20 children?']),
    dict(id='5d', tier='core', no='5(d)', type='selfcheck', open=False, skill='growing patterns',
         q='Why does the number of children go up by 2 each time? Write your idea in the box.', svg=TABLES_FIG,
         facts=dict(each_new_table_adds=2), check=lambda: dict(each_new_table_adds=one(sorted({seats(n + 1) - seats(n) for n in range(1, 15)}), 'step')),
         hint='Look at where the new table is joined on. Which sides have children, and which sides are joined together?',
         steps=['A new table is joined at one end. The end child has to move, but the top and bottom sides of the new table each have a child.', 'So every new table adds 2 children, one at the top and one at the bottom.',
                'Any answer that talks about the top and bottom of each table is a good one.'],
         src=['Why does the number of children go up by 2 each time?']),

    dict(id='6a', tier='core', no='6(a)', type='set', ordered=True, skill='numbers in two times tables', answer=[12, 15, 18, 21, 24, 27, 30, 33, 36],
         q='Ali counts in 3s: 3, 6, 9 ... Type the rest of Ali\'s numbers, up to 36, with a comma between.',
         check=lambda: ALI[3:], hint='Keep adding 3 each time. Stop at 36.',
         steps=['Add 3 each time: 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36.', 'After 9 the numbers are 12, 15, 18, 21, 24, 27, 30, 33, 36.'],
         src=['Ali counts in 3s: 3, 6, 9 … Mei counts in 4s: 4, 8, 12 …']),
    dict(id='6b', tier='core', no='6(b)', type='set', ordered=True, skill='numbers in two times tables', answer=[16, 20, 24, 28, 32, 36],
         q='Mei counts in 4s: 4, 8, 12 ... Type the rest of Mei\'s numbers, up to 36, with a comma between.',
         check=lambda: MEI[3:], hint='Keep adding 4 each time. Stop at 36.',
         steps=['Add 4 each time: 4, 8, 12, 16, 20, 24, 28, 32, 36.', 'After 12 the numbers are 16, 20, 24, 28, 32, 36.'],
         src=['Mei counts in 4s: 4, 8, 12 …']),
    dict(id='6c', tier='core', no='6(c)', type='set', ordered=False, skill='numbers in two times tables', answer=[12, 24, 36],
         q='Ali counts in 3s from 3 and Mei counts in 4s from 4, both up to 36. Which numbers do they BOTH say? Type them with a comma between.',
         check=lambda: sorted(set(ALI) & set(MEI)), hint='Make the two lists and look at them side by side. Which numbers are in both lists?',
         steps=['Ali: 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36.', 'Mei: 4, 8, 12, 16, 20, 24, 28, 32, 36.', 'The numbers in both lists are 12, 24 and 36.'],
         src=['Which numbers from 1 to 36 do they BOTH say?', 'Both say:']),
    dict(id='6d', tier='core', no='6(c) notice', type='selfcheck', open=False, skill='numbers in two times tables',
         q='What do you notice about the numbers they both say? Write your idea in the box.',
         facts=dict(both=[12, 24, 36], jump=12), check=lambda: dict(both=sorted(set(ALI) & set(MEI)), jump=one(sorted({b - a for a, b in zip(sorted(set(ALI) & set(MEI)), sorted(set(ALI) & set(MEI))[1:])}), 'jump')),
         hint='Look at how far apart the numbers are.',
         steps=['The numbers they both say are 12, 24 and 36. They go up by 12 each time.', '12 is in the 3 times table and in the 4 times table, and so are 24 and 36.', 'Any answer that talks about the jump of 12 is a good one.'],
         src=['What do you notice?']),

    # ================= Investigation: Three counting patterns
    dict(id='I1', tier='invest', no='Investigation (a) A', type='set', ordered=True, skill='three counting patterns', answer=[13, 16, 19, 22, 25, 28],
         q='Three counting patterns. Pattern A: 1, 4, 7, 10 ... (add 3 each time). Pattern B: 2, 5, 8, 11 ... Pattern C: 3, 6, 9, 12 ... '
           'Write each pattern up to 30. First pattern A: type the numbers after 10, up to 30, with a comma between.',
         check=lambda: [x for x in ap(1, 3, 12) if 10 < x <= 30],
         hint='Easy first step: write pattern A, 1, 4, 7, 10 ..., up to 30.',
         steps=['Add 3 each time: 1, 4, 7, 10, 13, 16, 19, 22, 25, 28.', 'The next number would be 31, which is more than 30.', 'After 10 the numbers are 13, 16, 19, 22, 25, 28.'],
         src=['Pattern A: 1, 4, 7, 10 ... (add 3 each time). Pattern B: 2, 5, 8, 11 ... Pattern C: 3, 6, 9, 12 ...']),
    dict(id='I2', tier='invest', no='Investigation (a) B', type='set', ordered=True, skill='three counting patterns', answer=[14, 17, 20, 23, 26, 29],
         q='Pattern B goes 2, 5, 8, 11 ... Type the numbers after 11, up to 30, with a comma between.',
         check=lambda: [x for x in ap(2, 3, 12) if 11 < x <= 30],
         hint='Pattern B also adds 3 each time. Keep going until the next number would be more than 30.',
         steps=['Add 3 each time: 2, 5, 8, 11, 14, 17, 20, 23, 26, 29.', 'The next number would be 32, which is more than 30.', 'After 11 the numbers are 14, 17, 20, 23, 26, 29.'],
         src=['Pattern B: 2, 5, 8, 11 ...']),
    dict(id='I3', tier='invest', no='Investigation (a) C', type='set', ordered=True, skill='three counting patterns', answer=[15, 18, 21, 24, 27, 30],
         q='Pattern C goes 3, 6, 9, 12 ... Type the numbers after 12, up to 30, with a comma between.',
         check=lambda: [x for x in ap(3, 3, 12) if 12 < x <= 30],
         hint='Pattern C also adds 3 each time. Keep going until the next number would be more than 30.',
         steps=['Add 3 each time: 3, 6, 9, 12, 15, 18, 21, 24, 27, 30.', 'After 12 the numbers are 15, 18, 21, 24, 27, 30.'],
         src=['Pattern C: 3, 6, 9, 12 ...']),
    dict(id='I4', tier='invest', no='Investigation (b) which', type='choice', options=['A', 'B', 'C'], answer='B', skill='three counting patterns',
         q='Pick a number from 1 to 30. Which of the patterns A, B or C is the number 26 in?',
         check=lambda: one([name for name, start in (('A', 1), ('B', 2), ('C', 3)) if 26 in ap(start, 3, 11)], 'pattern of 26'),
         hint='Look at your lists for A, B and C. Which one has 26?',
         steps=['Pattern B is 2, 5, 8, 11, 14, 17, 20, 23, 26, 29.', '26 is in pattern B.'],
         src=['Pick any number from 1 to 30. Which pattern is it in?']),
    dict(id='I5', tier='invest', no='Investigation (b) two', type='choice', options=['Yes', 'No'], answer='No', skill='three counting patterns',
         q='Can a number from 1 to 30 be in two of the patterns A, B and C?',
         check=lambda: 'Yes' if any(sum(n in ap(s, 3, 30) for s in (1, 2, 3)) > 1 for n in range(1, 100)) else 'No',
         hint='Look at your three lists side by side. Does any number appear in more than one list?',
         steps=['The three lists are A: 1, 4, 7 ... 28, B: 2, 5, 8 ... 29 and C: 3, 6, 9 ... 30.', 'No number is in two lists.'],
         src=['Can a number be in two patterns?']),
    dict(id='I6', tier='invest', no='Investigation (b) none', type='choice', options=['Yes', 'No'], answer='No', skill='three counting patterns',
         q='Can a number from 1 to 30 be in none of the patterns A, B and C?',
         check=lambda: 'Yes' if any(sum(n in ap(s, 3, 40) for s in (1, 2, 3)) == 0 for n in range(1, 31)) else 'No',
         hint='Go through the numbers from 1 to 30 one at a time. Is each one in a list?',
         steps=['Check the numbers 1, 2, 3, 4, 5, 6 ...: 1 is in A, 2 is in B, 3 is in C, 4 is in A ...', 'Every number from 1 to 30 is in one of the lists. No number is left out.'],
         src=['Can a number be in none?']),
    dict(id='I7', tier='invest', no='Investigation (c)', type='selfcheck', open=False, skill='three counting patterns',
         q='Why does this happen? Why is every number in exactly one of the patterns? Write your idea in the box.',
         facts=dict(each_number_in_exactly_one=True),
         check=lambda: dict(each_number_in_exactly_one=all(sum(n in ap(s, 3, 40) for s in (1, 2, 3)) == 1 for n in range(1, 100))),
         hint='Think about counting in 3s. A number is on the 3s, or just after a number on the 3s, or two after.',
         steps=['Counting in 3s: a number is either on the 3s (pattern C), or 1 more than a number on the 3s (pattern A), or 2 more (pattern B).', 'There is no other choice, so every number is in exactly one pattern.', 'Any answer that uses the 3 times table is a good one.'],
         src=['(c) Why does this happen?']),

    # ================= Think harder
    dict(id='T1a', tier='stretch', no='Think harder 1', type='number', skill='counting parts of a pattern', answer=12,
         q='Look at the shape pattern again (places 1 to 10). How many circles are there in the first 30 shapes?', svg=SHAPE_FIG,
         check=lambda: build(SHAPES, 30).count('circle'),
         hint='How many shapes are in one group? How many circles are in one group? How many groups are in 30 shapes?',
         steps=['A group is 5 shapes: triangle, circle, circle, square, square. It has 2 circles.', '30 shapes make 6 groups: 6 × 2 = 12.', 'There are 12 circles.'],
         src=['Look at the shape pattern in the Start here page again (places 1 to 10). How many circles are there in the first 30 shapes?']),
    dict(id='T1b', tier='stretch', no='Think harder 1 (how do you know)', type='selfcheck', open=False, skill='counting parts of a pattern',
         q='How do you know how many circles there are in the first 30 shapes? Write your idea in the box.', svg=SHAPE_FIG,
         facts=dict(groups=6, circles_per_group=2), check=lambda: dict(groups=len(build(SHAPES, 30)) // len(SHAPES), circles_per_group=SHAPES.count('circle')),
         hint='Draw a model or a table: groups, and circles in each group.',
         steps=['30 shapes is 6 groups of 5, and each group has 2 circles.', '6 groups of 2 circles: 2, 4, 6, 8, 10, 12.', 'Any idea that uses the groups is a good one.'],
         src=['How many circles are there in the first 30 shapes? How do you know?']),
    dict(id='T2a', tier='stretch', no='Think harder 2', type='choice', options=['Yes', 'No'], answer='No', skill='far places in a repeating pattern',
         q='Beads go red, red, blue, green, red, red, blue, green ... Mei says the 30th bead is blue. Is she right?',
         check=lambda: 'Yes' if at(['red', 'red', 'blue', 'green'], 30) == 'blue' else 'No',
         hint='How many beads are in one group? Find the place where a group ends, close to 30.',
         steps=['A group has 4 beads. Groups end at 4, 8, 12 ... 28.', 'Place 29 is red and place 30 is red.', 'The 30th bead is red, not blue. Mei is not right.'],
         src=['Beads go red, red, blue, green, red, red, blue, green … Mei says the 30th bead is blue. Is she right?']),
    dict(id='T2b', tier='stretch', no='Think harder 2 (green)', type='set', ordered=False, skill='far places in a repeating pattern', answer=[4, 8, 12, 16, 20, 24, 28],
         q='Beads go red, red, blue, green, red, red, blue, green ... Which places up to 30 have a green bead? Type them with a comma between.',
         check=lambda: places_of(['red', 'red', 'blue', 'green'], 'green', 30),
         hint='Where is the green bead in the first group? Then in the next group?',
         steps=['A group has 4 beads and the green bead is the last one in each group.', 'The green beads are in places 4, 8, 12, 16, 20, 24 and 28.'],
         src=['Which places up to 30 have a green bead?']),
    dict(id='T3', tier='stretch', no='Think harder 3', type='number', skill='counting parts of a pattern', answer=12,
         q='Beads go red, yellow, yellow, red, yellow, yellow ... How many yellow beads are in the first 18 beads?',
         check=lambda: build(['red', 'yellow', 'yellow'], 18).count('yellow'),
         hint='How many beads are in one group? How many of them are yellow? How many groups are there in 18 beads?',
         steps=['A group has 3 beads: red, yellow, yellow. It has 2 yellow beads.', '18 beads make 6 groups: 6 × 2 = 12.', 'There are 12 yellow beads.'],
         src=['Beads go red, yellow, yellow, red, yellow, yellow … How many yellow beads are in the first 18 beads?']),
    dict(id='T4', tier='stretch', no='Think harder 4', type='number', skill='growing patterns', answer=25,
         q='Houses are made of sticks in a row. 1 house uses 5 sticks, 2 houses use 9 sticks, 3 houses use 13 sticks. How many sticks are needed for 6 houses?', svg=HOUSES_FIG,
         check=lambda: sticks(6) if [sticks(1), sticks(2), sticks(3)] == [5, 9, 13] else None,
         hint='How many more sticks does each new house need? Keep going with the pattern.',
         steps=['5, 9, 13: each new house adds 4 sticks.', '5, 9, 13, 17, 21, 25.', '6 houses need 25 sticks.'],
         src=['Houses are made of sticks in a row. 1 house uses 5 sticks, 2 houses use 9 sticks, 3 houses use 13 sticks. How many sticks are needed for 6 houses?']),

    # ================= Go further
    dict(id='C5a', tier='challenge', no='Go further 5', type='number', skill='numbers in two times tables', answer=24,
         q='Ali counts in 3s from 3. Mei counts in 4s from 4. They both say 12. What is the next number they will BOTH say? Predict first, then test your idea.',
         check=lambda: both(3, 3, 4, 4, 100)[1],
         hint='Predict it, then write the first few numbers of each of their lists and look for the next number in both.',
         steps=['Ali: 3, 6, 9, 12, 15, 18, 21, 24 ...', 'Mei: 4, 8, 12, 16, 20, 24 ...', 'The next number in both lists is 24.'],
         src=['Ali counts in 3s from 3. Mei counts in 4s from 4. They both say 12. Predict the next number they will BOTH say.']),
    dict(id='C5b', tier='challenge', no='Go further 5 (list)', type='set', ordered=False, skill='numbers in two times tables', answer=[12, 24, 36, 48, 60, 72, 84, 96],
         q='Ali counts in 3s from 3. Mei counts in 4s from 4. List every number up to 100 that they both say. Type them with a comma between.',
         check=lambda: both(3, 3, 4, 4, 100),
         hint='Look for a quick way. If you know the first number they both say, what is the jump to the next one?',
         steps=['They both say 12, 24, 36, 48, 60, 72, 84 and 96.', 'The numbers go up by 12 each time. The next one, 108, is more than 100.'],
         src=['list every number up to 100 that they both say.']),
    dict(id='C5c', tier='challenge', no='Go further 5 (why)', type='selfcheck', open=False, skill='numbers in two times tables',
         q='What do you notice about the numbers they both say? Why does this happen? Write your idea in the box.',
         facts=dict(jump=12), check=lambda: dict(jump=one(sorted({b - a for a, b in zip(both(3, 3, 4, 4, 100), both(3, 3, 4, 4, 100)[1:])}), 'jump')),
         hint='Look at how far apart the numbers are. Which numbers are in both the 3 times table and the 4 times table?',
         steps=['The numbers go up by 12 each time.', '12 is the first number in both the 3 and 4 times tables, and each next one is 12 more.', 'Any answer that says the numbers are in the 12 times table is a good one.'],
         src=['What do you notice? Why?']),
    dict(id='C6a', tier='challenge', no='Go further 6', type='number', skill='growing patterns', answer=10,
         q='Siti builds towers of cubes. Tower 1 has 2 cubes, tower 2 has 5 cubes, tower 3 has 8 cubes. The towers keep growing in the same way. Which tower has 29 cubes?', svg=TOWERS_FIG,
         check=lambda: ap(2, 3, 40).index(29) + 1,
         hint='How many more cubes does each tower have than the one before? Keep the pattern going.',
         steps=['Each tower has 3 more cubes: 2, 5, 8, 11, 14, 17, 20, 23, 26, 29.', '29 is the 10th number, so tower 10 has 29 cubes.'],
         src=['Siti builds towers of cubes. Tower 1 has 2 cubes, tower 2 has 5 cubes, tower 3 has 8 cubes.', 'Which tower has 29 cubes?']),
    dict(id='C6b', tier='challenge', no='Go further 6 (50)', type='choice', options=['Yes', 'No'], answer='Yes', skill='growing patterns',
         q='Siti\'s towers have 2, 5, 8 ... cubes and keep growing in the same way. Is there a tower with exactly 50 cubes?', svg=TOWERS_FIG,
         check=lambda: 'Yes' if 50 in ap(2, 3, 60) else 'No',
         hint='Keep the pattern going: add 3 each time. Do you land on 50?',
         steps=['2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50.', '50 is in the pattern. It is tower 17.'],
         src=['Is there a tower with exactly 50 cubes?']),
    dict(id='C6c', tier='challenge', no='Go further 6 (100)', type='choice', options=['Yes', 'No'], answer='No', skill='growing patterns',
         q='Siti\'s towers have 2, 5, 8 ... cubes and keep growing in the same way. Is there a tower with exactly 100 cubes?', svg=TOWERS_FIG,
         check=lambda: 'Yes' if 100 in ap(2, 3, 60) else 'No',
         hint='Keep the pattern going, adding 3 each time, until you are near 100. Do you land on 100?',
         steps=['Counting on in 3s from 2: 2, 5, 8 ... 95, 98, 101.', '100 is not in the pattern, so there is no tower with exactly 100 cubes.'],
         src=['With exactly 100 cubes?']),
    dict(id='C6d', tier='challenge', no='Go further 6 (explain)', type='selfcheck', open=False, skill='growing patterns',
         q='Explain how you know whether a tower has 50 cubes and whether a tower has 100 cubes. Write your idea in the box.', svg=TOWERS_FIG,
         facts=dict(tower_for_50=17, in_pattern_100=False),
         check=lambda: dict(tower_for_50=ap(2, 3, 60).index(50) + 1, in_pattern_100=100 in ap(2, 3, 60)),
         hint='Compare 2, 5, 8, 11 ... with the 3 times table: 3, 6, 9, 12 ... What do you notice?',
         steps=['Each tower has 1 less than a number in the 3 times table: 3 - 1 = 2, 6 - 1 = 5, 9 - 1 = 8.', '50 + 1 = 51 is in the 3 times table (3 × 17), so 50 is in the pattern.', '100 + 1 = 101 is not in the 3 times table (99 and 102 are), so 100 is not in the pattern.'],
         src=['Explain how you know.']),
    dict(id='C7', tier='challenge', no='Go further 7', type='set', ordered=False, skill='numbers in two times tables', answer=[8, 20],
         q='Frog A starts at 0 and jumps 4 each time: 4, 8, 12 ... Frog B starts at 2 and jumps 3 each time: 5, 8, 11 ... Which numbers up to 30 do both frogs land on? Type them with a comma between.',
         svg=stack(FROG_A, FROG_B),
         check=lambda: both(4, 4, 5, 3, 30),
         hint='Write the numbers each frog lands on, up to 30. Which numbers are in both lists?',
         steps=['Frog A lands on 4, 8, 12, 16, 20, 24, 28.', 'Frog B lands on 5, 8, 11, 14, 17, 20, 23, 26, 29.', 'Both frogs land on 8 and 20.'],
         src=['Frog A starts at 0 and jumps 4 each time: 4, 8, 12 … Frog B starts at 2 and jumps 3 each time: 5, 8, 11 …']),
    dict(id='M', tier='challenge', no='Make up your own', type='selfcheck', open=False, skill='making puzzles',
         q='Make up your own: a pattern of 4 shapes. Write a question about the 30th shape for a partner.',
         facts='circle', check=lambda: at(['square', 'circle', 'circle', 'triangle'], 30),
         hint='Pick 4 shapes. Think about where the groups of 4 end. Then choose a far place for your question.',
         steps=['Many answers are right. Here is one example: square, circle, circle, triangle, and then it repeats.', 'Question: what is the 30th shape? 28 is the end of a group (4 × 7), so place 29 is a square and place 30 is a circle.',
                'Check yours: find the end of a group close to your place, then count on.'],
         src=['a pattern of 4 shapes. Write a question about the 30th shape for a partner.']),
]
for _d in ITEMS:
    _d.setdefault('strand', STRAND)


# ---------------------------------------------------------------- variant families (template + independent oracle over EVERY combination)
VARIANTS = {
    '2c': dict(
        base=dict(n=30),
        tpl=dict(vars=dict(n=[22, 23, 26, 27, 30, 33, 34, 38, 40]), q='Ali writes the letters M, A, T, H again and again until he has written {n} letters. How many Ts does he write?',
                 answer='(n+1)//4', hint='How many whole groups of M, A, T, H are there in {n} letters? Is there a T in the letters left over?',
                 steps=['A group has 4 letters and one T. Count the whole groups in {n} letters.', 'Look at the letters left over: is the T among them?', 'Ali writes {ans} Ts.']),
        oracle=lambda e: build(LETTERS, e['n']).count('T')),
    '3a': dict(
        base=dict(r=12),
        tpl=dict(vars=dict(r=[8, 10, 12, 14, 16, 18]), q='A bead string goes 2 red, 3 yellow, 2 red, 3 yellow ... It has {r} red beads and ends with yellow beads. How many yellow beads are there?',
                 answer='(r//2)*3', hint='Draw one group. How many groups have {r} red beads?',
                 steps=['One group has 2 red and 3 yellow beads. Count the groups that have {r} red beads.', 'Each group has 3 yellow beads. There are {ans} yellow beads.']),
        oracle=lambda e: next(build(BEADS, n) for n in range(5, 200, 5) if build(BEADS, n).count('red') == e['r']).count('yellow')),
    '4b': dict(
        base=dict(p=5, n=10),
        tpl=dict(vars=dict(p=[2, 3, 4, 5, 10], n=[6, 7, 8, 9, 10, 12]), q='Each flower has {p} petals. How many petals are on {n} flowers?',
                 answer='p*n', hint='Keep counting in {p}s. How many {p}s do you need?',
                 steps=['Count in {p}s, {n} times.', '{n} flowers have {ans} petals.']),
        oracle=lambda e: sum(e['p'] for _ in range(e['n']))),
    '4c': dict(
        base=dict(p=5, k=7),
        tpl=dict(vars=dict(p=[2, 3, 4, 5, 10], k=[3, 4, 6, 7, 8, 9]), derive=dict(t='p*k'), q='Each flower has {p} petals. {t} petals make how many flowers?',
                 answer='t//p', hint='Count in {p}s until you reach {t}. How many {p}s did you count?',
                 steps=['Count in {p}s until you reach {t}.', 'The number of {p}s you counted is the number of flowers: {ans}.']),
        oracle=lambda e: len(count_up_to(e['p'], e['p'] * e['k']))),
    '5b': dict(
        base=dict(n=10),
        tpl=dict(vars=dict(n=[6, 7, 8, 9, 10, 11, 12, 15]), q='Square tables are pushed together in a row, with one child at each open side. 1 table seats 4, 2 tables seat 6, 3 tables seat 8. How many children sit at {n} tables?',
                 answer='2*n+2', hint='How many more children for each new table? Keep going with the pattern.',
                 steps=['4, 6, 8: each new table adds 2 children.', 'Keep adding 2 until you reach {n} tables: {ans} children.']),
        oracle=lambda e: seats(e['n'])),
    'T3': dict(
        base=dict(m=18),
        tpl=dict(vars=dict(m=[12, 15, 21, 24, 27, 30]), q='Beads go red, yellow, yellow, red, yellow, yellow ... How many yellow beads are in the first {m} beads?',
                 answer='(m//3)*2', hint='How many beads are in one group? How many are yellow? How many groups are there in {m} beads?',
                 steps=['A group has 3 beads and 2 of them are yellow.', 'Count the groups in {m} beads. Then count the yellow beads: {ans}.']),
        oracle=lambda e: build(['red', 'yellow', 'yellow'], e['m']).count('yellow')),
    'C6a': dict(
        base=dict(k=10),
        tpl=dict(vars=dict(k=[6, 7, 8, 9, 10, 12, 14, 15]), derive=dict(x='3*k-1'), q='Siti builds towers of cubes. Tower 1 has 2 cubes, tower 2 has 5 cubes, tower 3 has 8 cubes. The towers keep growing in the same way. Which tower has {x} cubes?',
                 answer='(x+1)//3', hint='How many more cubes does each tower have than the one before? Keep the pattern going.',
                 steps=['Each tower has 3 more cubes: 2, 5, 8, 11 ...', 'Keep adding 3 until you reach {x}. It is tower {ans}.']),
        oracle=lambda e: ap(2, 3, 60).index(3 * e['k'] - 1) + 1),
}
