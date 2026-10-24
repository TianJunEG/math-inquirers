"""Online practice for Level 1 (Primary 1, ages 6-8) holiday lesson 10: Mixed Puzzles ("Puzzle Day").

Questions as printed in the Level 1 holiday workbook (hp/workbook_html.js lesson 10, Q1 to Q9, and the Puzzle cards page, whose cards are in hp/lessons.js; hp/qbank.json lesson 10
stretch[0:4] for Think harder and challenge[-3:] for Go further, as the workbook builder slices them; hp/gaps.json lesson 10 for the Investigation).  Every answer is recomputed by an
independent checker: patterns are built by adding step by step, coins are chosen by trying every set, shapes are told apart from their sides and corners, triangles are counted from the
drawn lines, orders are found by trying every order, and number puzzles are solved by trying numbers.  The build stops if a checker and the printed answer (Tutor Guide answer key) differ.
"""
import itertools, os, sys
from fractions import Fraction
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from p1lib import *      # noqa: E402,F401

META = dict(level=1, lesson=10, key='p1', title='Puzzle Day', workbook_title='PUZZLE DAY!', topic='Mixed Puzzles',
            strand='Mixed puzzles',
            sources=['hp/workbook_html.js', 'hp/qbank.json', 'hp/gaps.json', 'hp/lessons.js'],
            intro=['Show how you know. Remember the inquirer rules: notice the pattern, test it, check your answer, explain why.',
                   'Some questions ask you to make up a puzzle or to write a list. Do those on paper, then check against the answer shown on screen.'])

S = 'Mixed puzzles'


def D(**k):
    return dict(strand=S, **k)


# ---- independent checkers
def ap_list(start, step, count):
    out, v = [], start
    for _ in range(count):
        out.append(v)
        v += step
    return out


def rule_name(seq):
    ds = {b - a for a, b in zip(seq, seq[1:])}
    d = ds.pop() if len(ds) == 1 else None
    return None if d is None else (f'Add {d}' if d > 0 else f'Take away {-d}')


def uniq(vals):
    return vals[0] if len(vals) == 1 else None


def pair_with_gap(total, gap):
    return uniq([(a, b) for a in range(total + 1) for b in range(total + 1) if a + b == total and b - a == gap])


PETS = [('Dog', 4), ('Cat', 7), ('Fish', 3), ('Bird', 5)]
PET = dict(PETS)
PET_FIG = lambda: pets_street_fig(PETS, 'The picture graph shows pets in a street: one picture for each pet')


def pairs_making(total):
    return [f'{a} and {b}' for (a, x), (b, y) in itertools.combinations(PETS, 2) if x + y == total]


COINS_HELD = [20, 10, 10, 5, 5]


def subsets_value(coins, total):
    """Every different set of coin values (as a sorted tuple) that adds to total, taking each coin held at most once."""
    got = set()
    for r in range(1, len(coins) + 1):
        for c in itertools.combinations(coins, r):
            if sum(c) == total:
                got.add(tuple(sorted(c, reverse=True)))
    return sorted(got)


def coins_exactly(n, total, kinds=(5, 10, 20, 50)):
    return sorted({tuple(sorted(c, reverse=True)) for c in itertools.combinations_with_replacement(kinds, n) if sum(c) == total})


# shapes told apart by (number of sides, all sides the same, number of square corners)
SHAPES = {'Square': (4, True, 4), 'Rectangle': (4, False, 4), 'Rhombus': (4, True, 0), 'Triangle': (3, False, 0), 'Circle': (0, True, 0), 'Hexagon': (6, True, 0)}


def who(test):
    return uniq([nm for nm, v in SHAPES.items() if test(v)])


def _pt(p):
    return (Fraction(p[0]), Fraction(p[1]))


def on_seg(p, s):
    (x1, y1), (x2, y2) = s
    if (x2 - x1) * (p[1] - y1) - (y2 - y1) * (p[0] - x1) != 0:
        return False
    return min(x1, x2) <= p[0] <= max(x1, x2) and min(y1, y2) <= p[1] <= max(y1, y2)


def seg_cross(s, t):
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = s[0], s[1], t[0], t[1]
    d = (x2 - x1) * (y4 - y3) - (y2 - y1) * (x4 - x3)
    if d == 0:
        return None
    a = Fraction((x3 - x1) * (y4 - y3) - (y3 - y1) * (x4 - x3), 1) / d
    b = Fraction((x3 - x1) * (y2 - y1) - (y3 - y1) * (x2 - x1), 1) / d
    return (x1 + a * (x2 - x1), y1 + a * (y2 - y1)) if 0 <= a <= 1 and 0 <= b <= 1 else None


def count_triangles(segs):
    """Triangles in a figure of drawn segments: every triple of the figure's points (ends of lines and where lines cross) joined in pairs by drawn lines and not on one line."""
    segs = [(_pt(a), _pt(b)) for a, b in segs]
    pts = {p for s in segs for p in s}
    for s, t in itertools.combinations(segs, 2):
        c = seg_cross(s, t)
        if c is not None:
            pts.add(c)
    pts = sorted(pts)
    joined = lambda p, q: any(on_seg(p, s) and on_seg(q, s) for s in segs)
    n = 0
    for p, q, r in itertools.combinations(pts, 3):
        if (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0]) != 0 and joined(p, q) and joined(q, r) and joined(p, r):
            n += 1
    return n


TRI = [((0, 0), (4, 0)), ((0, 0), (2, 3)), ((4, 0), (2, 3)), ((2, 3), (2, 0))]          # a triangle with a line from the top corner straight down to the bottom
TRI_FIG = lambda: seg_svg(TRI, 4, 3, 44, 'A triangle with a line drawn from the top corner down to the bottom side', fills=[[(0, 0), (4, 0), (2, 3)]])


def orders(things, ok):
    return [list(o) for o in itertools.permutations(things) if ok(list(o))]


def before(o, a, b):
    return o.index(a) < o.index(b)


def think_number(add, take, result):
    return uniq([n for n in range(0, 100) if n + add - take == result])


def sticks_up_to(first, step, limit):
    out, v = [], first
    while v <= limit:
        out.append(v)
        v += step
    return out


def ways_of(amount, coins):
    out = []
    for counts in itertools.product(*[range(amount // c + 1) for c in coins]):
        if sum(n * c for n, c in zip(counts, coins)) == amount:
            out.append(counts)
    return sorted(out, reverse=True)


def total_three(start, jump):
    return sum(ap_list(start, jump, 3))


ITEMS = [
    # ================= Start here
    D(id='1n', tier='core', no='1 next', label='1 next', type='fields', skill='number patterns', answer=[23, 28],
      q='Pattern. Find the next two numbers.', frame='3,  8,  13,  18,  {f1},  {f2}', check=lambda: ap_list(3, 5, 6)[4:],
      hint='Look at how much each number is bigger than the one before it.',
      steps=['8 - 3 = 5, 13 - 8 = 5 and 18 - 13 = 5, so the numbers go up by 5 each time.', '18 + 5 = 23 and 23 + 5 = 28.', 'The next two numbers are 23 and 28.'],
      src=['Pattern:   3,   8,   13,   18,   ____,   ____']),
    D(id='1r', tier='core', no='1 rule', label='1 rule', type='choice', skill='number patterns', options=['Add 3', 'Add 5', 'Add 8', 'Take away 5'], answer='Add 5',
      q='What is the rule of the pattern 3, 8, 13, 18?', check=lambda: rule_name([3, 8, 13, 18]),
      hint='Look at how much each number changes to get the next one. Is it always the same?',
      steps=['8 - 3 = 5, 13 - 8 = 5 and 18 - 13 = 5.', 'Every number is 5 more than the one before.', 'The rule is add 5.'],
      src=['Rule: ______________']),
    D(id='2', tier='core', no='2', label='Q2', type='fields', skill='two numbers puzzle', answer=[5, 7],
      q='Two numbers add up to 12. One is 2 more than the other. What are the two numbers?', frame='Smaller number: {f1}     Bigger number: {f2}', check=lambda: pair_with_gap(12, 2),
      hint='Try a pair that adds to 12. Is one of them 2 more than the other? If not, change the pair.',
      steps=['Try pairs that add to 12: 6 and 6 (no gap), 5 and 7 (the gap is 2).', '5 + 7 = 12 and 7 is 2 more than 5.', 'The numbers are 5 and 7.'],
      src=['Two numbers add up to 12. One is 2 more than the other. What are they?']),

    D(id='3a', tier='core', no='3(a)', label='3(a)', type='number', skill='reading a picture graph', answer=2, svg=PET_FIG(),
      q='The graph shows pets in a street. How many more cats than birds are there?', check=lambda: PET['Cat'] - PET['Bird'],
      hint='Count the cat pictures and the bird pictures. How many more cat pictures are there?',
      steps=['Count the pictures: there are 7 cats and 5 birds.', '7 - 5 = 2.', 'There are 2 more cats than birds.'],
      src=['The graph shows pets in a street.', 'How many more cats than birds?']),
    D(id='3b', tier='core', no='3(b)', label='3(b)', type='number', skill='reading a picture graph', answer=19, svg=PET_FIG(),
      q='The graph shows pets in a street. How many pets are there altogether?', check=lambda: sum(PET.values()),
      hint='Count every picture in every row. Each picture is one pet.',
      steps=['The pets are 4 dogs, 7 cats, 3 fish and 5 birds.', '4 + 7 = 11, 11 + 3 = 14 and 14 + 5 = 19.', 'There are 19 pets altogether.'],
      src=['How many pets altogether?']),
    D(id='3c', tier='core', no='3(c)', label='3(c)', type='choice', skill='reading a picture graph', answer='Cat and Fish', svg=PET_FIG(),
      options=['Dog and Cat', 'Dog and Bird', 'Cat and Fish', 'Fish and Bird', 'Cat and Bird'],
      q='The graph shows pets in a street. Which two kinds of pet together make exactly 10 pets?', check=lambda: uniq([p for p in pairs_making(10) if p in ('Dog and Cat', 'Dog and Bird', 'Cat and Fish', 'Fish and Bird', 'Cat and Bird')]),
      hint='Count each row. Then try two rows at a time and add. Do they make 10?',
      steps=['Count the rows: dog 4, cat 7, fish 3, bird 5.', 'Try pairs: cat and fish is 7 + 3 = 10. The other pairs make 11, 9, 8 or 12.', 'Cat and fish together make exactly 10 pets.'],
      src=['Which two kinds of pet together make exactly 10?']),

    D(id='4a', tier='core', no='4(a)', label='4(a)', type='number', skill='adding coins', answer=50,
      q='You have one 20¢ coin, two 10¢ coins and two 5¢ coins. How much money do you have altogether?', check=lambda: sum(COINS_HELD),
      hint='Add the coins one at a time. Start with the biggest coin.',
      steps=['The coins are 20¢, 10¢, 10¢, 5¢ and 5¢.', '20 + 10 = 30, 30 + 10 = 40, 40 + 5 = 45 and 45 + 5 = 50.', 'You have 50¢.'],
      src=['You have one 20¢ coin, two 10¢ coins and two 5¢ coins.', 'How much money do you have?']),
    D(id='4b', tier='core', no='4(b)', label='4(b)', type='set', ordered=False, skill='making an amount', answer=[20, 10, 5],
      q='You have one 20¢ coin, two 10¢ coins and two 5¢ coins. Which coins make exactly 35¢? Type their values with commas, like 10, 5.',
      check=lambda: list(uniq(subsets_value(COINS_HELD, 35))),
      hint='Try some of the coins and add them up. Is the total 35¢? If not, change one coin and try again.',
      steps=['Take the 20¢ coin. 35 - 20 = 15¢ more is needed.', '10¢ + 5¢ = 15¢.', 'The coins are 20¢, 10¢ and 5¢. No other set of these coins makes 35¢.'],
      src=['Which coins make exactly 35¢?']),

    D(id='5a', tier='core', no='5(a)', label='5(a)', type='choice', skill='naming shapes', options=['Square', 'Rectangle', 'Triangle', 'Circle'], answer='Square',
      q='I have 4 sides, all the same length, and 4 square corners. What shape am I?', check=lambda: who(lambda v: v == (4, True, 4)),
      hint='Count the sides. Then think: are all the sides the same length? Do the corners look like the corner of a piece of paper?',
      steps=['4 sides and 4 square corners: a square or a rectangle.', 'All the sides are the same length, and a rectangle does not have that.', 'I am a square.'],
      src=['I have 4 sides, all the same length, and 4 square corners. What am I?']),
    D(id='5b', tier='core', no='5(b)', label='5(b)', type='number', skill='counting triangles', answer=3, svg=TRI_FIG(),
      q='How many triangles are in this picture?', check=lambda: count_triangles(TRI),
      hint='Count the small triangles first. Then look for a bigger triangle made of small ones.',
      steps=['The line cuts the big triangle into 2 small triangles: 1 on the left and 1 on the right.', 'The 2 small triangles together make the big triangle.', '2 + 1 = 3 triangles.'],
      src=['How many triangles are in this picture?']),

    D(id='6', tier='core', no='6', label='Q6', type='choice', skill='ordering from clues', options=['Ali', 'Ben', 'Mei'], answer='Mei',
      q='Ali is older than Ben. Mei is younger than Ben. Who is the youngest?',
      check=lambda: uniq(orders(['Ali', 'Ben', 'Mei'], lambda o: before(o, 'Ali', 'Ben') and before(o, 'Ben', 'Mei')))[-1],
      hint='Write the three children in a line, oldest first. Who is at the end?',
      steps=['Ali is older than Ben. Ben is older than Mei (Mei is younger than Ben).', 'The order from oldest is Ali, Ben, Mei.', 'Mei is the youngest.'],
      src=['Ali is older than Ben. Mei is younger than Ben. Who is the youngest?']),

    D(id='7', tier='core', no='7', label='Q7', type='number', skill='working backwards', answer=5,
      q='I think of a number. I add 9, then take away 4. I get 10. What is my number? Try a number and check.', check=lambda: think_number(9, 4, 10),
      hint='Pick a number and do the two steps. Is the answer 10? If it is too big or too small, change your number.',
      steps=['Try 5: 5 + 9 = 14, and 14 - 4 = 10. It works.', 'Try 6: 6 + 9 = 15, and 15 - 4 = 11. That is too big.', 'My number is 5.'],
      src=['I think of a number. I add 9, then take away 4. I get 10. What is it?']),

    D(id='8a', tier='core', no='8(a)', label='8(a)', type='number', skill='comparing lengths', answer=10,
      q='A pencil is 6 cubes long. A pen is 4 cubes longer than the pencil. How many cubes long is the pen?', check=lambda: 6 + 4,
      hint="The pen is as long as the pencil and then some more. How many more cubes?",
      steps=['The pencil is 6 cubes long.', 'The pen is 4 cubes longer: 6 + 4 = 10.', 'The pen is 10 cubes long.'],
      src=['A pencil is 6 cubes long. A pen is 4 cubes longer than the pencil.', 'How long is the pen?']),
    D(id='8b', tier='core', no='8(b)', label='8(b)', type='number', skill='joining lengths', answer=16,
      q='A pencil is 6 cubes long. A pen is 4 cubes longer than the pencil. The pen and the pencil are put end to end. How many cubes long are they together?', check=lambda: 6 + (6 + 4),
      hint='Find how long the pen is first. Then add the two lengths.',
      steps=['The pencil is 6 cubes and the pen is 6 + 4 = 10 cubes.', '6 + 10 = 16.', 'Together they are 16 cubes long.'],
      src=['Put the pen and the pencil end to end. How long are they together?']),

    D(id='9', tier='core', no='9', label='Q9', type='selfcheck', open=True, marking_mode='open', skill='making a puzzle',
      q='Make a puzzle for a friend. Write the puzzle and its answer on paper. Swap puzzles with a friend or a grown-up and solve each other\'s.',
      hint='Pick the answer first. Then write a story or some clues that lead to it.',
      steps=['One example: I think of a number. I add 6. I get 11. What is my number? Answer: 5.', 'Another example: Ali has 3 stickers and Mei has 4 more. How many do they have together? Answer: 10.', 'Any puzzle that can be solved and has a right answer is good. Check your own answer first.'],
      src=['Make a puzzle for a friend. Write the puzzle and the answer here.']),
    D(id='9b', tier='core', no='9(b)', label='Q9 best', type='selfcheck', open=True, marking_mode='open', skill='looking back',
      q='Which puzzle did you like best today, and why?',
      hint='Think about a puzzle that made you stop and think, or one that felt like a win.',
      steps=['There is no right or wrong answer here.', 'Any puzzle and any reason is good.'],
      src=['The puzzle I liked best today was']),

    # ---- the puzzle cards (printed on the Puzzle cards page)
    D(id='PC1', tier='core', no='Puzzle card 1: Coins', label='Card 1', type='set', ordered=False, skill='making an amount', answer=[20, 20, 5],
      q='Puzzle card: Coins. Make 45¢ with exactly 3 coins. You can use 5¢, 10¢, 20¢ and 50¢ coins. Type the coin values with commas.', check=lambda: list(uniq(coins_exactly(3, 45))),
      hint='Three coins make 45¢. Think about which big coin could be in the set, then which two coins make the rest.',
      steps=['Try the 20¢ coin. 45 - 20 = 25¢ is needed from 2 coins.', '20¢ + 5¢ = 25¢.', 'The coins are 20¢, 20¢ and 5¢. It is the only way to make 45¢ with exactly 3 coins.'],
      src=['Make 45¢ with exactly 3 coins from 5¢, 10¢, 20¢ and 50¢.']),
    D(id='PC2', tier='core', no='Puzzle card 2: Patterns', label='Card 2', type='number', skill='number patterns', answer=32,
      q='Puzzle card: Patterns. 5, 8, 11, 14 ... What is the 10th number?', check=lambda: ap_list(5, 3, 10)[-1],
      hint='Find the rule first. Then keep the pattern going and number each place as you go.',
      steps=['The numbers go up by 3 each time.', '5, 8, 11, 14, 17, 20, 23, 26, 29, 32: the 10th number is the last one.', 'The 10th number is 32.'],
      src=['5, 8, 11, 14 … What is the 10th number? Show how you know.']),
    D(id='PC2b', tier='core', no='Puzzle card 2: how', label='Card 2 how', type='selfcheck', open=False, marking_mode='self', skill='explaining a pattern',
      q='Puzzle card: Patterns. 5, 8, 11, 14 ... Show how you know the 10th number.', check=lambda: ap_list(5, 3, 10),
      hint='Write the numbers in a row and put a number under each place: 1st, 2nd, 3rd ...',
      steps=['Find the rule: each number is 3 more than the one before.', 'Write the pattern place by place: 5, 8, 11, 14, 17, 20, 23, 26, 29, 32.', 'Count to the 10th place to find the 10th number. Any clear way of showing this is good.'],
      src=['Show how you know.']),
    D(id='PC3', tier='core', no='Puzzle card 3: Logic', label='Card 3', type='choice', skill='ordering from clues',
      options=['Mei, Ben, Sam, Ali', 'Mei, Ben, Ali, Sam', 'Ali, Sam, Ben, Mei', 'Ben, Mei, Sam, Ali'], answer='Mei, Ben, Sam, Ali',
      q='Puzzle card: Logic. Mei is taller than Ben. Ben is taller than Sam. Ali is shorter than Sam. Which list goes from tallest to shortest?',
      check=lambda: ', '.join(uniq(orders(['Mei', 'Ben', 'Sam', 'Ali'], lambda o: before(o, 'Mei', 'Ben') and before(o, 'Ben', 'Sam') and before(o, 'Sam', 'Ali')))),
      hint='Take the clues one at a time. Put two children in a line, then fit the next child in.',
      steps=['Mei is taller than Ben, and Ben is taller than Sam: Mei, Ben, Sam.', 'Ali is shorter than Sam, so Ali goes at the end.', 'Tallest first: Mei, Ben, Sam, Ali.'],
      src=['Mei is taller than Ben. Ben is taller than Sam. Ali is shorter than Sam. Put them in order, tallest first.']),

    # ================= Investigation: What if we change the jump?
    D(id='I1', tier='invest', no='Investigation 1', label='Inv 1', type='number', skill='patterns and totals', answer=24,
      q='Three numbers in a row start at 5 and jump by 3: 5, 8, 11. Add them up. What is the total?', check=lambda: total_three(5, 3),
      hint='Add the three numbers one after the other.',
      steps=['The numbers are 5, 8 and 11.', '5 + 8 = 13 and 13 + 11 = 24.', 'The total is 24.'],
      src=['Three numbers in a row start at 5 and jump by 3: 5, 8, 11. Add them up. What is the total?']),
    D(id='I2', tier='invest', no='Investigation 2', label='Inv 2', type='fields', skill='patterns and totals', answer=[18, 21, 27, 30],
      q='Three numbers in a row start at 5. Now change the jump to 1, 2, 4 and 5 and find each total.',
      frame='Jump 1: {f1}   Jump 2: {f2}\nJump 4: {f3}   Jump 5: {f4}', check=lambda: [total_three(5, j) for j in (1, 2, 4, 5)],
      hint='For each jump, write the three numbers and add them. For a jump of 1 the numbers are 5, 6 and 7.',
      steps=['Jump 1: 5, 6, 7 add to 18. Jump 2: 5, 7, 9 add to 21.', 'Jump 4: 5, 9, 13 add to 27. Jump 5: 5, 10, 15 add to 30.', 'The totals are 18, 21, 27 and 30.'],
      src=['Now change the jump to 1, 2, 4 and 5 and find each total.']),
    D(id='I3', tier='invest', no='Investigation 3', label='Inv 3', type='selfcheck', open=False, marking_mode='self', skill='patterns and totals',
      q='Look at your totals for the jumps 1, 2, 3, 4 and 5. What stays the same? What changes?', check=lambda: [total_three(5, j) for j in (1, 2, 3, 4, 5)],
      hint='Put the jumps and the totals in a table. Look at the totals from top to bottom.',
      steps=['The first number is still 5, and there are still 3 numbers.', 'The totals are 18, 21, 24, 27 and 30. The total goes up by 3 each time the jump goes up by 1.', 'Any answer that notices these things is good.'],
      src=['What stays the same? What changes?']),
    D(id='I4', tier='invest', no='Investigation 4', label='Inv 4', type='selfcheck', open=False, marking_mode='self', skill='finding a shortcut',
      q='Can you find a shortcut for the total of three numbers in a row that start at 5?', check=lambda: [total_three(5, j) == 3 * (5 + j) == 15 + 3 * j for j in range(0, 11)],
      hint='Look at your table of jumps and totals. Is there a quick way to get a total without adding every time?',
      steps=['The total is 3 times the middle number: for a jump of 3 the numbers are 5, 8, 11 and 3 x 8 = 24.', 'Another shortcut: 15 plus 3 jumps. For a jump of 3: 15 + 9 = 24.', 'Any shortcut that works for every jump is good. Test yours on a jump of 4.'],
      src=['Can you find a shortcut for the total?']),

    # ================= Think harder
    D(id='T1a', tier='stretch', no='T1 8th', label='T1 8th', type='number', skill='number patterns', answer=46,
      q='A pattern starts at 4 and adds 6 each time. What is the 8th number?', check=lambda: ap_list(4, 6, 8)[-1],
      hint='Write the pattern in a row, one place at a time. Count the places as you go.',
      steps=['Start at 4 and add 6 each time: 4, 10, 16, 22, 28, 34, 40, 46.', 'The 8th number is the last one.', 'The 8th number is 46.'],
      src=['A pattern starts at 4 and adds 6 each time. What is the 8th number?']),
    D(id='T1b', tier='stretch', no='T1 50', label='T1 is 50', type='choice', skill='number patterns', options=['Yes', 'No'], answer='No',
      q='A pattern starts at 4 and adds 6 each time. Is the number 50 in the pattern?', check=lambda: 'Yes' if 50 in sticks_up_to(4, 6, 50) else 'No',
      hint='Keep adding 6 from 4. Watch the numbers as you get near 50.',
      steps=['The pattern goes 4, 10, 16, 22, 28, 34, 40, 46, 52.', 'It goes from 46 to 52, so it skips 50.', 'No, 50 is not in the pattern.'],
      src=['Is 50 in the pattern?']),
    D(id='T2', tier='stretch', no='T2', label='T2', type='number', skill='working backwards', answer=6,
      q='Mei thinks of a number, adds 7, takes away 2 and gets 19. Ben does the same and gets 25. How much bigger is Ben\'s number than Mei\'s?',
      check=lambda: think_number(7, 2, 25) - think_number(7, 2, 19),
      hint='Work backwards for each child. Undo the steps in the other order. What number did each start with?',
      steps=['Work backwards for Mei: 19 + 2 = 21, then 21 - 7 = 14.', 'Work backwards for Ben: 25 + 2 = 27, then 27 - 7 = 20.', "20 - 14 = 6, so Ben's number is 6 bigger."],
      src=['Mei thinks of a number, adds 7, takes away 2 and gets 19. Ben does the same and gets 25. How much bigger is Ben\'s number?']),
    D(id='T3a', tier='stretch', no='T3 list', label='T3 list', type='selfcheck', paper=True, skill='finding every set of coins',
      q='Ali has 5 coins worth 60¢ altogether. He has only 5¢, 10¢ and 20¢ coins. Write every possible set of 5 coins. Use a table if you like.',
      facts=[(2, 1, 2), (1, 4, 0)], check=lambda: [w for w in ways_of(60, (20, 10, 5)) if sum(w) == 5],
      sol_fig=lambda f: ways_table(f, (20, 10, 5), 'The sets of 5 coins that make 60 cents'),
      hint='Make a table by the number of 20¢ coins. For each number, how much is left for the other coins?',
      steps=['One 20¢ coin leaves 40¢ for 4 coins: four 10¢ coins. So 20¢ + 10¢ + 10¢ + 10¢ + 10¢.', 'Two 20¢ coins leave 20¢ for 3 coins: 10¢ + 5¢ + 5¢. So 20¢ + 20¢ + 10¢ + 5¢ + 5¢.',
             'No 20¢ coin gives at most 50¢ with 5 coins. Three 20¢ coins make 60¢ with only 3 coins. So there are two sets.'],
      src=['Ali has 5 coins worth 60¢. He has only 5¢, 10¢ and 20¢ coins. Find every possible set.']),
    D(id='T3b', tier='stretch', no='T3 count', label='T3 count', type='number', skill='finding every set of coins', answer=2,
      q='Do the list question first. How many different sets of 5 coins make exactly 60¢, using only 5¢, 10¢ and 20¢ coins?', check=lambda: len([w for w in ways_of(60, (20, 10, 5)) if sum(w) == 5]),
      hint='Count the sets you wrote in your list. Check that no two sets are the same.',
      steps=['The sets are 20¢ + 10¢ + 10¢ + 10¢ + 10¢ and 20¢ + 20¢ + 10¢ + 5¢ + 5¢.', 'There are no others.', 'There are 2 sets.'],
      src=['Find every possible set.']),
    D(id='T4a', tier='stretch', no='T4 wins', label='T4 wins', type='choice', skill='comparing votes', options=['Apple', 'Banana', 'Orange'], answer='Apple',
      q='Votes: apple 6, banana 9, orange 7. Then 5 more children vote and all of them choose apple. Which fruit wins now?',
      check=lambda: (lambda v: max(v, key=v.get))({'Apple': 6 + 5, 'Banana': 9, 'Orange': 7}),
      hint='Add the 5 new votes to the right fruit. Then compare all three totals.',
      steps=['Apple now has 6 + 5 = 11 votes.', 'Banana has 9 votes and orange has 7 votes.', '11 is the most, so apple wins.'],
      src=['Votes: Apple 6, Banana 9, Orange 7. Then 5 more children vote and all choose apple. Which fruit wins now?']),
    D(id='T4b', tier='stretch', no='T4 by', label='T4 by', type='number', skill='comparing votes', answer=2,
      q='Votes: apple 6, banana 9, orange 7. Then 5 more children all vote for apple. How many more votes does the winner have than the fruit in second place?',
      check=lambda: (lambda v: sorted(v.values())[-1] - sorted(v.values())[-2])({'Apple': 6 + 5, 'Banana': 9, 'Orange': 7}),
      hint='Find the total for each fruit. Which fruit is first and which is second? What is the difference?',
      steps=['Apple has 6 + 5 = 11 votes, banana has 9 and orange has 7.', 'The winner is apple. Second place is banana with 9.', '11 - 9 = 2. Apple has 2 more votes.'],
      src=['By how many votes?']),

    # ================= Go further
    D(id='C1a', tier='challenge', no='Go further 1', label='G1 list', type='set', ordered=False, skill='two patterns', answer=[7, 13, 19, 25, 31],
      q='Triangles in a row use 3, 5, 7 ... sticks. Squares in a row use 4, 7, 10 ... sticks. Which numbers of sticks, up to 31, can make a row of triangles AND a row of squares, with none left over? Type the numbers with commas.',
      check=lambda: sorted(set(sticks_up_to(3, 2, 31)) & set(sticks_up_to(4, 3, 31))),
      hint='Write the numbers of sticks for the triangles, up to 31. Write them for the squares too. Which numbers are on both lists?',
      steps=['Triangles: 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31.', 'Squares: 4, 7, 10, 13, 16, 19, 22, 25, 28, 31.', 'The numbers on both lists are 7, 13, 19, 25 and 31. For example 7 sticks make 3 triangles or 2 squares.'],
      src=['Triangles in a row use 3, 5, 7 … sticks. Squares in a row use 4, 7, 10 … sticks.']),
    D(id='C1b', tier='challenge', no='Go further 1 (notice)', label='G1 notice', type='selfcheck', open=False, marking_mode='self', skill='two patterns',
      q='Look at your list of stick numbers from the last question. What do you notice?', check=lambda: (lambda l: {b - a for a, b in zip(l, l[1:])})(sorted(set(sticks_up_to(3, 2, 31)) & set(sticks_up_to(4, 3, 31)))),
      hint='Look at how far apart the numbers on your list are.',
      steps=['The numbers go up by 6 each time: 7, 13, 19, 25, 31.', 'The triangle numbers go up by 2 and the square numbers go up by 3, and they meet again every 6 sticks.', 'Any true thing you notice is good.'],
      src=['What do you notice?']),
    D(id='C2', tier='challenge', no='Go further 2', label='G2', type='fields', skill='finding parts of a total', answer=[8, 12, 9],
      q='Ali has some stickers. Ben has 4 more than Ali. Mei has 3 fewer than Ben. Together they have 29 stickers. How many stickers does each child have?',
      frame='Ali: {f1}   Ben: {f2}   Mei: {f3}', check=lambda: list(uniq([(a, a + 4, a + 4 - 3) for a in range(1, 30) if a + (a + 4) + (a + 4 - 3) == 29])),
      hint='Try a number for Ali. Work out Ben and Mei. Do the three add up to 29?',
      steps=['Try Ali = 8: Ben has 8 + 4 = 12 and Mei has 12 - 3 = 9.', '8 + 12 + 9 = 29, so it works.', 'Ali has 8, Ben has 12 and Mei has 9.'],
      src=['Ali has some stickers. Ben has 4 more than Ali. Mei has 3 fewer than Ben. Together they have 29. How many does each have?']),
    D(id='C3', tier='challenge', no='Go further 3', label='G3', type='selfcheck', open=True, marking_mode='open', skill='changing a puzzle',
      q='Pick any puzzle from today. Change ONE thing about it (a number, a rule or a condition) to make a new puzzle. Solve your new puzzle and say what changed in the answer, and why.',
      facts=[(20, 10, 10, 5)], check=lambda: coins_exactly(4, 45),
      hint='Pick a puzzle you liked. Change one number, then solve it again.',
      steps=['An example: change "Make 45¢ with exactly 3 coins" to "Make 45¢ with exactly 4 coins".', 'With 3 coins the only way is 20¢ + 20¢ + 5¢. With 4 coins the only way is 20¢ + 10¢ + 10¢ + 5¢. One 20¢ coin was swapped for two 10¢ coins, because we needed one more coin.',
             'Your own puzzle needs to be solvable, and you should say how the change made the answer change.'],
      src=['Pick any puzzle from today']),
]


VARIANTS = {
    '1n': dict(base=dict(a=3, d=5),
               tpl=dict(vars=dict(a=[2, 3, 4, 5, 6, 7], d=[3, 4, 5, 6, 7, 8]), derive=dict(b='a+d', c='a+2*d', e='a+3*d'), q='Pattern. Find the next two numbers.',
                        frame='{a},  {b},  {c},  {e},  {f1},  {f2}', answers=dict(f1='a+4*d', f2='a+5*d'),
                        hint='Look at how much each number is bigger than the one before it.',
                        steps=['Each number is {d} more than the one before.', 'Add {d} to the last number, and then add {d} again.', 'The next two numbers are {ans}.']),
               oracle=lambda e: dict(zip(('f1', 'f2'), ap_list(e['a'], e['d'], 6)[4:]))),
    '2': dict(base=dict(s=12, g=2),
              tpl=dict(vars=dict(s=[10, 12, 14, 16, 18, 20], g=[2, 4]), derive=dict(lo='(s-g)//2', hi='(s+g)//2'),
                       q='Two numbers add up to {s}. One is {g} more than the other. What are the two numbers?', frame='Smaller number: {f1}     Bigger number: {f2}', answers=dict(f1='(s-g)//2', f2='(s+g)//2'),
                       hint='Try a pair that adds to {s}. Is one of them {g} more than the other? If not, change the pair.',
                       steps=['Try pairs that add to {s} and look at the gap between the two numbers.', 'You need a gap of {g}.', 'The numbers are {ans}.']),
              oracle=lambda e: dict(zip(('f1', 'f2'), pair_with_gap(e['s'], e['g'])))),
    '7': dict(base=dict(n=5, a=9, t=4),
              tpl=dict(vars=dict(n=[3, 4, 5, 6, 7, 8], a=[6, 7, 8, 9, 12], t=[2, 3, 4, 5]), derive=dict(r='n+a-t'), q='I think of a number. I add {a}, then take away {t}. I get {r}. What is my number?', answer='n',
                       hint='Pick a number and do the two steps. Is the answer {r}? If it is too big or too small, change your number.',
                       steps=['Try a number and do the two steps. Change it until you get {r}.', 'Or work backwards: add {t}, then take away {a}.', 'My number is {ans}.']),
              oracle=lambda e: think_number(e['a'], e['t'], e['n'] + e['a'] - e['t'])),
    '8a': dict(base=dict(p=6, d=4),
               tpl=dict(vars=dict(p=[5, 6, 7, 8, 9], d=[2, 3, 4, 5]), q='A pencil is {p} cubes long. A pen is {d} cubes longer than the pencil. How many cubes long is the pen?', answer='p+d',
                        hint='The pen is as long as the pencil and then some more. How many more cubes?',
                        steps=['The pencil is {p} cubes long.', 'The pen is {d} cubes longer.', 'The pen is {ans} cubes long.']),
               oracle=lambda e: e['p'] + e['d']),
    '8b': dict(base=dict(p=6, d=4),
               tpl=dict(vars=dict(p=[5, 6, 7, 8, 9], d=[2, 3, 4, 5]), q='A pencil is {p} cubes long. A pen is {d} cubes longer than the pencil. The pen and the pencil are put end to end. How many cubes long are they together?', answer='p+p+d',
                        hint='Find how long the pen is first. Then add the two lengths.',
                        steps=['The pencil is {p} cubes and the pen is {p} and {d} more.', 'Add the two lengths.', 'Together they are {ans} cubes long.']),
               oracle=lambda e: e['p'] + (e['p'] + e['d'])),
    'PC2': dict(base=dict(a=5, d=3),
                tpl=dict(vars=dict(a=[3, 4, 5, 6, 7], d=[2, 3, 4, 5]), derive=dict(b='a+d', c='a+2*d', e='a+3*d'), q='Puzzle card: Patterns. {a}, {b}, {c}, {e} ... What is the 10th number?', answer='a+9*d',
                         hint='Find the rule first. Then keep the pattern going and number each place as you go.',
                         steps=['The numbers go up by {d} each time.', 'Write the pattern place by place until you reach the 10th place.', 'The 10th number is {ans}.']),
                oracle=lambda e: ap_list(e['a'], e['d'], 10)[-1]),
    'I1': dict(base=dict(s=5, j=3),
               tpl=dict(vars=dict(s=[3, 4, 5, 6, 7], j=[1, 2, 3, 4, 5]), derive=dict(m='s+j', t='s+2*j'), q='Three numbers in a row start at {s} and jump by {j}: {s}, {m}, {t}. Add them up. What is the total?', answer='3*s+3*j',
                        hint='Add the three numbers one after the other.',
                        steps=['The numbers are {s}, {m} and {t}.', 'Add them up.', 'The total is {ans}.']),
               oracle=lambda e: total_three(e['s'], e['j'])),
    'T1a': dict(base=dict(a=4, d=6, n=8),
                tpl=dict(vars=dict(a=[3, 4, 5, 6], d=[3, 4, 5, 6], n=[6, 7, 8, 9]), q='A pattern starts at {a} and adds {d} each time. What is the number in place {n}?', answer='a+(n-1)*d',
                         hint='Write the pattern in a row, one place at a time. Count the places as you go.',
                         steps=['Start at {a} and add {d} each time.', 'Write the numbers place by place until you reach place {n}.', 'The number in place {n} is {ans}.']),
                oracle=lambda e: ap_list(e['a'], e['d'], e['n'])[-1]),
    'T2': dict(base=dict(a=7, t=2, r1=19, r2=25),
               tpl=dict(vars=dict(a=[5, 6, 7, 8], t=[2, 3, 4], r1=[15, 17, 19, 21], r2=[22, 24, 25, 27]), derive=dict(),
                        q="Mei thinks of a number, adds {a}, takes away {t} and gets {r1}. Ben does the same and gets {r2}. How much bigger is Ben's number than Mei's?", answer='r2-r1',
                        hint='Work backwards for each child. Undo the steps in the other order. What number did each start with?',
                        steps=['Work backwards for each child: add {t}, then take away {a}.', "Compare the two numbers you find."," Ben's number is {ans} bigger."]),
               oracle=lambda e: think_number(e['a'], e['t'], e['r2']) - think_number(e['a'], e['t'], e['r1'])),
    'C2': dict(base=dict(a=8, d=4, e=3),
               tpl=dict(vars=dict(a=[5, 6, 7, 8, 9, 10], d=[2, 3, 4, 5], e=[1, 2, 3]), derive=dict(t='3*a+2*d-e'),
                        q='Ali has some stickers. Ben has {d} more than Ali. Mei has {e} fewer than Ben. Together they have {t} stickers. How many stickers does each child have?',
                        frame='Ali: {f1}   Ben: {f2}   Mei: {f3}', answers=dict(f1='a', f2='a+d', f3='a+d-e'),
                        hint='Try a number for Ali. Work out Ben and Mei. Do the three add up to {t}?',
                        steps=['Try a number for Ali, then find Ben (more) and Mei (fewer).', 'Change Ali until the three add up to {t}.', 'The stickers are {ans}.']),
               oracle=lambda e: dict(zip(('f1', 'f2', 'f3'), uniq([(x, x + e['d'], x + e['d'] - e['e']) for x in range(1, 80) if x + (x + e['d']) + (x + e['d'] - e['e']) == 3 * e['a'] + 2 * e['d'] - e['e']])))),
}

for _d in ITEMS:
    if _d['type'] == 'selfcheck' and not _d.get('open') and 'marking_mode' not in _d:
        _d['marking_mode'] = 'self'
