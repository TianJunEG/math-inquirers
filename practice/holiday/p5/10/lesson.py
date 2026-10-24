"""Online practice for Level 5 (Primary 5, ages 10 to 12) holiday lesson 10: Mixed Strategies ("Challenge Day").

The questions are the ones printed in the Level 5 holiday workbook, lesson 10: Start here Q1 to Q6 (p5/content/l10.js, workbook()), the Investigation
(p5/content/inv.js), Think harder A1 to A4 (the first four 'stretch' questions of p5/content/l10.js qbank) and Go further B1 to B3 (the last three
'challenge' questions) and the "Make up your own" prompt (gaps.js), in the printed order, exactly as p5/workbook_html.js prints them.  Every answer is recomputed
by an INDEPENDENT checker below: every arrangement of dishes or chairs is tried against every clue, money puzzles are run forwards from every possible start, squares are
counted by position, the liars are found by testing what each child says for every possible culprit, the ways to climb are listed, never by copying the printed answer.
build_holiday.py stops if a checker and the printed answer differ.  The figures are drawn by practice/holiday/p5/p5fig5.py.
"""
import itertools, math, os, sys
HERE_ = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE_, '..', '..'))
sys.path.insert(0, os.path.join(HERE_, '..'))
from hlib import *          # noqa: E402,F401
from p5lib import *         # noqa: E402,F401
import p5fig5 as G          # noqa: E402

META = dict(level=5, lesson=10, key='p5', title='Challenge Day', workbook_title='CHALLENGE DAY', topic='Mixed Strategies', strand='Problem solving',
            sources=['p5/content/l10.js', 'p5/content/inv.js', 'p5/content/gaps.js'],
            intro=['Choose a start: draw a model, list in order, make a table, work backwards, or guess and check. Check your answer against EVERY clue. '
                   'When you work backwards, undo the last step first. In a logic puzzle, find a clue that tells you something for sure.',
                   'Type the number in the box (a unit after the number is fine). Some questions ask you to list or to explain: write your idea, then compare it with the model answer after you submit. '
                   'The tick-and-cross grid of the printed page is not needed here: pick the dish for each child.'])
ST = 'Problem solving'
F = Fraction


def D(**k):
    k.setdefault('strand', ST)
    return k


# ---------------------------------------------------------------- checkers
PEOPLE = ['Ali', 'Ben', 'Mei', 'Siti']
DISHES = ['chicken rice', 'laksa', 'satay', 'roti prata']


def logic_solutions():
    """Every way to give the four dishes to the four children that fits all four clues."""
    out = []
    for p in itertools.permutations(DISHES):
        d = dict(zip(PEOPLE, p))
        girl_prata = [n for n in PEOPLE if d[n] == 'roti prata'][0] in ('Mei', 'Siti')
        if d['Ali'] not in ('laksa', 'satay') and girl_prata and d['Ben'] != 'satay' and d['Mei'] != 'roti prata':
            out.append(d)
    assert len(out) == 1, out
    return out[0]


def forward_money(start, lunch):
    """Spend 1/3 on a book, then `lunch` dollars, then half of what is left on a gift: the money left at the end."""
    m = F(start) - F(start) / 3 - lunch
    return m - m / 2


def start_money(lunch, left):
    found = [s for s in range(1, 2000) if forward_money(s, lunch) == left]
    assert len(found) == 1, (lunch, left)
    return found[0]


def mei_ravi(total, extra):
    """Ravi has `extra` dollars more than 3/4 of Mei's money; together they have `total`.  Try every whole-dollar amount for Mei."""
    found = [m for m in range(1, 2000) if F(m) + F(3 * m, 4) + extra == total]
    assert len(found) == 1, (total, extra)
    return found[0], int(F(3 * found[0], 4) + extra)


def squares_of_size(rows, cols, k):
    """Count the k by k squares by trying every position of the top left corner."""
    return sum(1 for r in range(rows) for c in range(cols) if r + k <= rows and c + k <= cols)


def all_squares(rows, cols):
    return sum(squares_of_size(rows, cols, k) for k in range(1, min(rows, cols) + 1))


def liars(culprit):
    """Ali says 'Ben broke it', Ben says 'Mei broke it', Mei says 'I did not break it': how many of them are lying if `culprit` broke the vase?"""
    said = {'Ali': lambda: culprit == 'Ben', 'Ben': lambda: culprit == 'Mei', 'Mei': lambda: culprit != 'Mei'}
    return sum(1 for n in ('Ali', 'Ben', 'Mei') if not said[n]())


def vase_culprit():
    found = [c for c in ('Ali', 'Ben', 'Mei') if liars(c) == 1]
    assert len(found) == 1
    return found[0]


def years_until(mum, mei, times):
    found = [y for y in range(0, 100) if mum + y == times * (mei + y)]
    assert len(found) == 1, (mum, mei, times)
    return found[0]


def ways(n, parts=(1, 2)):
    if n == 0:
        return [()]
    out = []
    for s in parts:
        if n - s >= 0:
            out += [(s,) + w for w in ways(n - s, parts)]
    return out


def n_ways(n, parts=(1, 2)):
    return len(ways(n, parts))


SEQ = [n_ways(n) for n in range(1, 7)]
assert SEQ == [1, 2, 3, 5, 8, 13]


def siti_start(left):
    """Spend 2/5, then 1/3 of what is left; `left` dollars remain.  Search the start."""
    found = [s for s in range(1, 3000) if F(s) * F(3, 5) * F(2, 3) == left]
    assert len(found) == 1, left
    return found[0]


def three_digit_sum(total):
    return [n for n in range(100, 1000) if sum(int(c) for c in str(n)) == total]


def consecutive(total):
    found = [a for a in range(0, total) if a + a + 1 == total]
    assert len(found) == 1
    return found[0], found[0] + 1


def snail_day(wall, up, down):
    pos, day = 0, 0
    while True:
        day += 1
        pos += up
        if pos >= wall:
            return day
        pos -= down


def tank(added):
    """A tank 1/3 full gets `added` litres and is then 1/2 full; 1/4 of the water is let out.  Returns (litres now, the capacity)."""
    caps = [c for c in range(1, 5000) if F(c, 3) + added == F(c, 2)]
    assert len(caps) == 1
    cap = caps[0]
    now = F(cap, 2) * (1 - F(1, 4))
    return now, cap


def coin_mix():
    """25 coins of 50¢, 10¢ and 20¢ worth 530¢ with twice as many 10¢ coins as 50¢ coins."""
    found = [(a, 2 * a, 25 - 3 * a) for a in range(0, 9) if 25 - 3 * a >= 0 and 50 * a + 10 * 2 * a + 20 * (25 - 3 * a) == 530]
    assert len(found) == 1, found
    return list(found[0])


def row_order():
    """Ali, Ben, Mei and Siti in chairs 1 to 4: Mei not on an end, Ben not next to Mei, Siti left of Ali, Ben not on the left end."""
    out = []
    for p in itertools.permutations(PEOPLE):
        pos = {n: i for i, n in enumerate(p)}
        if pos['Mei'] not in (0, 3) and abs(pos['Ben'] - pos['Mei']) != 1 and pos['Siti'] < pos['Ali'] and pos['Ben'] != 0:
            out.append(list(p))
    assert len(out) == 1, out
    return out[0]


def names_accepts(order):
    out = set()
    for sep in (', ', ',', ' ', ' - ', '-', ' > ', ' then ', ' and ', '; '):
        out.add(sep.join(order))
    out.add(', '.join(order[:-1]) + ' and ' + order[-1])
    out.add(', '.join(order[:-1]) + ', and ' + order[-1])
    return sorted(out)


LOGIC = logic_solutions()
assert LOGIC == {'Ali': 'chicken rice', 'Ben': 'laksa', 'Mei': 'satay', 'Siti': 'roti prata'}

CLUE_Q = 'Logic puzzle. Ali, Ben, Mei and Siti each ordered a different dish at a hawker centre. Use the clues in the card.'
BACK_Q = 'Working backwards. Ali spent 1/3 of his money on a book. He then spent $12 on lunch. He spent half of what was left on a gift. Ali had $15 left at the end.'
MODEL_Q = 'Draw a model. Mei and Ravi have $115 altogether. Ravi has $10 more than 3/4 of Mei’s money.'
VASE_Q = 'Ali, Ben and Mei were playing. One of them broke a vase. Ali says, “Ben broke it.” Ben says, “Mei broke it.” Mei says, “I did not break it.”'
AGE_Q = 'Mum is 41 years old and Mei is 9 years old.'
STAIR_Q = 'Ali climbs a staircase and takes either 1 step or 2 steps at a time.'
SNAIL_Q = 'A snail climbs 3 m up a 10 m wall each day, and slips down 2 m each night.'


def person_item(iid, name, no, label):
    ans = LOGIC[name]
    others = {'Ali': 'Ali is a boy, so he cannot have the roti prata. Clue 1 rules out laksa and satay, so he has chicken rice.',
              'Ben': 'Ali has the chicken rice. Ben is a boy, so he does not have the roti prata; clue 3 rules out satay, so he has laksa.',
              'Mei': 'Roti prata is for a girl, and clue 4 says it is not Mei, so Siti has it. Ali and Ben have chicken rice and laksa, so Mei has the satay.',
              'Siti': 'Clue 2 says a girl ordered the roti prata, so it is Mei or Siti. Clue 4 rules out Mei, so Siti ordered the roti prata.'}[name]
    return D(id=iid, tier='core', no=no, label=label, type='choice', skill='logic grid', options=list(DISHES), answer=ans, q=CLUE_Q + f'\nWhat did {name} order?', svg=G.clue_card(),
             check=lambda: LOGIC[name], hint='Find a clue that tells you something for sure. Cross out what each child cannot have.',
             steps=[others, 'Check every clue: ' + '; '.join(f'{n} {LOGIC[n]}' for n in PEOPLE) + '. All four clues are true.'],
             src=['Logic grid. Ali, Ben, Mei and Siti each ordered a different dish at a hawker centre.', 'Clue 1:  Ali did not order laksa or satay.'])


ITEMS = [
    # ================= Start here (workbook lesson 10: Q1 to Q6)
    person_item('1a', 'Ali', '1 Ali', '1 Ali'),
    person_item('1b', 'Ben', '1 Ben', '1 Ben'),
    person_item('1c', 'Mei', '1 Mei', '1 Mei'),
    person_item('1s', 'Siti', '1 Siti', '1 Siti'),

    D(id='2', tier='core', no='2', label='2', type='number', skill='working backwards', answer=63,
      q=BACK_Q + '\nHow much money did he start with? (Type the number of dollars.)', svg=G.backwards_fig(), sol_fig=lambda f: G.backwards_fig((63, 21, 42, 12, 30, 15)),
      check=lambda: start_money(12, 15), hint='Start here: write the steps in order. Then undo the LAST step first.',
      steps=['Work backwards. He had $15 left after the gift, and the gift was half of what he had before it, so before the gift he had 15 × 2 = $30.', 'Before lunch he had 30 + 12 = $42.',
             '$42 is what was left after the book, 2/3 of his money. So 1/3 is $21 and he started with $63.', 'Check: 63 − 21 = 42, 42 − 12 = 30, and half of 30 is 15, so 15 is left.'],
      src=['Working backwards. Ali spent 1/3 of his money on a book. He then spent $12 on lunch. He spent half of what was left on a gift. Ali had $15 left at the end. How much money did he start with?']),
    D(id='2s', tier='core', no='2 (steps)', label='2 steps', type='fields', skill='working backwards', answer=[30, 42],
      q=BACK_Q + '\nUndo the steps in reverse order, starting from the end. How much did Ali have just before the gift, and just before lunch? (Type the number of dollars.)', svg=G.backwards_fig(),
      frame='Before the gift: $ {f1}     Before lunch: $ {f2}', check=lambda: [2 * 15, 2 * 15 + 12], hint='He spent half of what was left on the gift, so the $15 he had at the end is the other half.',
      steps=['The gift was half of what he had before it, so the other half, $15, is what he had left. Before the gift he had 15 × 2 = $30.', 'Before the gift he had spent $12 on lunch, so before lunch he had 30 + 12 = $42.'],
      src=['write the steps in order. Then undo the LAST step first.']),

    D(id='3', tier='core', no='3', label='3', type='fields', skill='bar model with units', answer=[60, 55],
      q=MODEL_Q + '\nHow much money does each have? (Type the number of dollars.)', svg=G.two_bars_fig(115, 10), sol_fig=lambda f: G.two_bars_fig(115, 10, 15),
      frame='Mei: $ {f1}     Ravi: $ {f2}', check=lambda: list(mei_ravi(115, 10)),
      hint='Start here: Mei is 4 equal units. How many units is 3/4 of Mei’s? Where does the $10 go?',
      steps=['Mei is 4 units. Ravi is 3 of the same units and $10 more.', 'Together: 7 units + $10 = $115, so 7 units = $105 and 1 unit = $15.', 'Mei: 4 × $15 = $60. Ravi: 3 × $15 + $10 = $55.'],
      src=['Draw a model. Mei and Ravi have $115 altogether. Ravi has $10 more than 3/4 of Mei’s money. How much money does each have? Check your answer against BOTH clues.']),
    D(id='3c', tier='core', no='3 (check)', label='3 check', type='selfcheck', open=False, skill='checking against every clue', facts=(60, 55),
      q=MODEL_Q + '\nCheck your two amounts against BOTH clues. Write what you check, then compare it with the model answer.', svg=G.two_bars_fig(115, 10),
      check=lambda: mei_ravi(115, 10), hint='One clue is about the total. The other is about Ravi and 3/4 of Mei’s money.',
      steps=['Clue 1: $60 + $55 = $115, the total.', 'Clue 2: 3/4 of Mei’s $60 is $45, and $45 + $10 = $55, which is Ravi’s money.', 'Both clues are true.'],
      src=['Check your answer against BOTH clues.']),

    D(id='4a', tier='core', no='4(a)', label='4(a)', type='number', skill='counting squares by size', answer=12,
      q='How many squares of ALL sizes can you find in this 3 by 4 grid? Count by size so you do not miss any.\nSquares of size 1 by 1: (Type the number.)', svg=G.grid_fig(3, 4),
      check=lambda: squares_of_size(3, 4, 1), hint='Count the small squares row by row.', steps=['There are 3 rows of 4 small squares.', '3 × 4 = 12 squares of size 1 by 1.'],
      src=['How many squares of ALL sizes can you find in this 3 by 4 grid? Count by size so you do not miss any.', 'Squares of size 1 by 1:']),
    D(id='4b', tier='core', no='4(b)', label='4(b)', type='fields', skill='counting squares by size', answer=[6, 2],
      q='How many squares of ALL sizes can you find in this 3 by 4 grid? Count by size.\nHow many squares of size 2 by 2, and of size 3 by 3? (Type the numbers.)', svg=G.grid_fig(3, 4),
      sol_fig=lambda f: G.squares_in_grid_fig(3, 4, 2), frame='2 by 2: {f1}     3 by 3: {f2}', check=lambda: [squares_of_size(3, 4, 2), squares_of_size(3, 4, 3)],
      hint='A 2 by 2 square covers 4 small squares. Slide it along the grid: in how many places does it fit?',
      steps=['A 2 by 2 square can start in 2 rows and 3 columns: 2 × 3 = 6 squares.', 'A 3 by 3 square can start in 1 row and 2 columns: 1 × 2 = 2 squares.'],
      src=['Squares of size 2 by 2:   ____________    Squares of size 3 by 3:']),
    D(id='4c', tier='core', no='4(c)', label='4(c)', type='number', skill='counting squares by size', answer=20,
      q='How many squares of ALL sizes are there altogether in this 3 by 4 grid? (Type the number.)', svg=G.grid_fig(3, 4), check=lambda: all_squares(3, 4),
      hint='Count by size: all the 1 by 1 squares, then all the 2 by 2 squares, and so on. Add them.', steps=['12 squares of size 1 by 1, 6 of size 2 by 2 and 2 of size 3 by 3.', '12 + 6 + 2 = 20 squares altogether.'],
      src=['How many squares altogether? How do you know there are none bigger?']),
    D(id='4cw', tier='core', no='4(c) why', label='4(c) why', type='selfcheck', open=False, skill='explaining', facts=(20, 3),
      q='This grid has 3 rows of 4 small squares.\nExplain how you know that you have found every square, and that there are none bigger. Write your idea, then compare it with the model answer.', svg=G.grid_fig(3, 4),
      check=lambda: (all_squares(3, 4), min(3, 4)), hint='What is the biggest square that fits in a grid that is only 3 rows tall?',
      steps=['The grid is only 3 rows tall, so no square can be taller than 3. The biggest square is 3 by 3.', 'Counting by size (1 by 1, 2 by 2, 3 by 3) means no size is missed.'],
      src=['How many squares altogether? How do you know there are none bigger?']),

    D(id='5a', tier='core', no='5(a)', label='5(a)', type='fields', skill='trying each possibility', answer=[2, 1, 2],
      q=VASE_Q + '\nTry each child. If that child broke the vase, how many of the three children are lying? (Type the numbers.)',
      frame='If Ali broke it: {f1} liars     If Ben broke it: {f2} liars     If Mei broke it: {f3} liars', check=lambda: [liars('Ali'), liars('Ben'), liars('Mei')],
      hint='For each child in turn, check what Ali, Ben and Mei said: is each sentence true or false if that child broke the vase?',
      steps=['If Ali broke it: Ali says “Ben broke it” (false), Ben says “Mei broke it” (false), Mei says “I did not” (true). 2 liars.',
             'If Ben broke it: Ali (true), Ben (false), Mei (true). 1 liar.', 'If Mei broke it: Ali (false), Ben (true), Mei says “I did not” (false). 2 liars.'],
      src=['Ali, Ben and Mei were playing. One of them broke a vase.', 'Try each child and count the liars.']),
    D(id='5b', tier='core', no='5(b)', label='5(b)', type='choice', skill='logic by cases', options=['Ali', 'Ben', 'Mei'], answer='Ben',
      q=VASE_Q + ' Exactly ONE of the three children is lying.\nWho broke the vase?', check=lambda: vase_culprit(), hint='Which child makes exactly one of the three sentences false?',
      steps=['Only when Ben broke the vase is exactly one child lying (Ben).', 'If Ali or Mei broke it, two children would be lying.'],
      src=['Exactly ONE of the three children is lying. Who broke the vase?']),

    D(id='6a', tier='core', no='6(a)', label='6(a)', type='number', skill='ages and a table', answer=7,
      q=AGE_Q + '\nIn how many years will Mum be exactly 3 times as old as Mei? (Type the number. A table helps.)', check=lambda: years_until(41, 9, 3),
      hint='Make a table: after 1 year, 2 years, 3 years, and so on. Write both ages each time.',
      steps=['After 1 year: 42 and 10. After 2 years: 43 and 11. Carry on in the table.', 'After 7 years: Mum is 48 and Mei is 16, and 3 × 16 = 48.',
             'A quick way: Mum is always 32 years older. When she is 3 times as old, those 32 years are 2 times Mei’s age, so Mei is 16, which is 7 years from now.'],
      src=['Mum is 41 years old and Mei is 9 years old.', 'In how many years will Mum be exactly 3 times as old as Mei?']),
    D(id='6b', tier='core', no='6(b)', label='6(b)', type='selfcheck', open=True, marking_mode='open', skill='choosing a start',
      q='Which start did you use for the last question? Why did you choose it? (A table of ages, the age gap, or guess and check are all good.)',
      hint='Think about what you did first. Could another start also work?',
      steps=['This question is open: many starts are right, for example “I made a table of their ages”, “I used the age gap, which never changes” or “I guessed and checked”.'],
      src=['Which start did you use? Why did you choose it?']),

    # ================= Investigation: Find the pattern
    D(id='C0', tier='invest', no='C (easy first step)', label='C easy', type='number', skill='listing the ways', answer=3,
      q='Find the pattern. ' + STAIR_Q + '\nEasy first step: with 1 step there is 1 way. With 2 steps there are 2 ways (1 + 1, or 2). How many ways are there for 3 steps? (Type the number.)',
      svg=G.stairs_fig(4), check=lambda: n_ways(3), hint='Draw the ways for 3 steps. Different orders count as different ways.',
      steps=['The ways for 3 steps are 1 + 1 + 1, 1 + 2 and 2 + 1.', 'That is 3 ways.'],
      src=['Easy first step: with 1 step there is 1 way. With 2 steps there are 2 ways (1 + 1, or 2). Draw the ways for 3 steps first.']),
    D(id='Cl', tier='invest', no='C(a) list', label='C(a) list', type='selfcheck', open=False, skill='listing every way', facts=tuple(ways(4)),
      q=STAIR_Q + ' List every way for 4 steps. Different orders count as different ways. Then compare your list with the model answer.', svg=G.stairs_fig(4),
      sol_fig=lambda f: G.steps_solution_fig(4), check=lambda: tuple(ways(4)), hint='Start with the ways that begin with 1 step. Then the ways that begin with 2 steps.',
      steps=['The ways for 4 steps are: ' + ', '.join('+'.join(map(str, w)) for w in ways(4)) + '.', 'A good answer is a complete list made in an order, so that no way is missed or written twice.'],
      src=['List every way for 4 steps']),
    D(id='Cn', tier='invest', no='C(a) how many', label='C(a) count', type='number', skill='counting every way', answer=5,
      q=STAIR_Q + ' Do the list question first. How many different ways are there for 4 steps? (Type the number.)', check=lambda: n_ways(4),
      hint='Count the ways in your list.', steps=['There are 5 ways to climb 4 steps: 1+1+1+1, 1+1+2, 1+2+1, 2+1+1 and 2+2.'],
      src=['How many different ways can he climb a staircase with 1 step? 2 steps? 3 steps? 4 steps?']),
    D(id='Cb1', tier='invest', no='C(b)', label='C(b)', type='fields', skill='making a table', answer=[8, 13],
      q=STAIR_Q + '\nMake a table up to 6 steps. How many ways are there for 5 steps and for 6 steps? (Type the numbers.)', frame='5 steps: {f1} ways     6 steps: {f2} ways',
      check=lambda: [n_ways(5), n_ways(6)], hint='Look at the table of 1, 2, 3 and 4 steps. Is there a pattern that tells you the next number?',
      steps=['The ways for 1, 2, 3, 4, 5 and 6 steps are 1, 2, 3, 5, 8 and 13.', 'Each number is the two numbers before it added together: 3 + 5 = 8 and 5 + 8 = 13.'],
      src=['Make a table up to 6 steps. What pattern do you see?']),
    D(id='Cb2', tier='invest', no='C(b) pattern', label='C(b) rule', type='choice', skill='noticing a pattern',
      options=['each number is the two numbers before it added together', 'each number is double the one before', 'each number is 2 more than the one before', 'each number is 1 more than the one before'],
      answer='each number is the two numbers before it added together',
      q=STAIR_Q + '\nLook at your table of the number of ways for 1, 2, 3, 4, 5 and 6 steps. Which pattern do you see?',
      check=lambda: [o for o, ok in {'each number is the two numbers before it added together': lambda s: all(s[i] == s[i - 1] + s[i - 2] for i in range(2, len(s))),
                                     'each number is double the one before': lambda s: all(s[i] == 2 * s[i - 1] for i in range(1, len(s))),
                                     'each number is 2 more than the one before': lambda s: all(s[i] == s[i - 1] + 2 for i in range(1, len(s))),
                                     'each number is 1 more than the one before': lambda s: all(s[i] == s[i - 1] + 1 for i in range(1, len(s)))}.items() if ok(SEQ)][0],
      hint='Test each choice on every number in your table, not just the first few.',
      steps=['The numbers are 1, 2, 3, 5, 8, 13. 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8 and 5 + 8 = 13.', 'They are not doubling (3 is not 4), and the gaps are not all 1 or all 2.'],
      src=['What pattern do you see?']),
    D(id='Cb3', tier='invest', no='C(b) why', label='C(b) why', type='selfcheck', open=False, skill='explaining a pattern', facts=tuple(SEQ),
      q=STAIR_Q + '\nExplain why the pattern in the table works. Think about the LAST jump Ali makes. Write your idea, then compare it with the model answer.',
      check=lambda: tuple(SEQ), hint='The last jump is either 1 step or 2 steps. How many steps did Ali climb before it?',
      steps=['The last jump is 1 step or 2 steps.', 'If it is 1 step, Ali had climbed n − 1 steps before it. If it is 2 steps, he had climbed n − 2 steps before it.',
             'So the ways for n steps = the ways for n − 1 steps + the ways for n − 2 steps.'],
      src=['Explain why it works (hint: think about the LAST jump Ali makes).']),
    D(id='Cc1', tier='invest', no='C(c)', label='C(c)', type='number', skill='using the pattern', answer=34,
      q=STAIR_Q + '\nUse your pattern to predict the number of ways for 8 steps. (Type the number.)', check=lambda: n_ways(8),
      hint='Carry on the table: each new number comes from the numbers before it.', steps=['The table goes 1, 2, 3, 5, 8, 13, 21, 34.', 'For 8 steps there are 34 ways.'],
      src=['Use your pattern to predict the number of ways for 8 steps.']),
    D(id='Cc2', tier='invest', no='C(c) 3 steps', label='C(c) 3', type='fields', skill='what if', answer=[4, 7],
      q='What if Ali could also take 3 steps at a time (1, 2 or 3 steps)?\nHow many ways are there for 3 steps and for 4 steps now? (Type the numbers.)', frame='3 steps: {f1} ways     4 steps: {f2} ways',
      check=lambda: [n_ways(3, (1, 2, 3)), n_ways(4, (1, 2, 3))], hint='List the ways again, and add the ones that use a jump of 3 steps.',
      steps=['3 steps: 1+1+1, 1+2, 2+1 and 3. That is 4 ways.', '4 steps: the 5 old ways, plus 1+3 and 3+1. That is 7 ways.'],
      src=['What if Ali could also take 3 steps? Try 3 and 4 steps again.']),

    # ================= Think harder (A1 to A4)
    D(id='A1', tier='stretch', no='A1', label='A1', type='number', skill='working backwards with fractions', answer=60,
      q='Siti spent 2/5 of her money, then 1/3 of what was left. She had $24 left at the end.\nHow much did she start with? (Type the number of dollars.)', svg=G.siti_fig(24), sol_fig=lambda f: G.siti_fig(24, 12),
      check=lambda: siti_start(24), hint='Work backwards. $24 is what fraction of the money she had after the first spending?',
      steps=['After spending 2/5 she had 3/5 of her money. Then she spent 1/3 of that, so 2/3 of it was left: $24.', '2/3 of what she had is $24, so that was $24 ÷ 2 × 3 = $36.', '$36 is 3/5 of her money, so 1/5 is $12 and she started with $60.', 'Check: 60 − 24 = 36, and 36 − 12 = 24.'],
      src=['Siti spent 2/5 of her money, then 1/3 of what was left. She had $24 left at the end. How much did she start with?']),
    D(id='A2l', tier='stretch', no='A2 list', label='A2 list', type='set', ordered=True, grouped=False, skill='listing in order', answer=three_digit_sum(5),
      q='List all the 3-digit numbers whose digits add up to 5, in order from the smallest. (Type them with commas.)', check=lambda: three_digit_sum(5),
      hint='Start with the smallest hundreds digit and list the numbers for it in order. Then move on to the next hundreds digit.',
      steps=['The numbers are ' + ', '.join(map(str, three_digit_sum(5))) + '.', 'Work through the hundreds digit 1, 2, 3, 4 and 5 in turn.'],
      src=['How many 3-digit numbers have digits that add up to 5? List them all in order.']),
    D(id='A2n', tier='stretch', no='A2 how many', label='A2 count', type='number', skill='counting every case', answer=15,
      q='Do the list question first. How many 3-digit numbers have digits that add up to 5? (Type the number.)', check=lambda: len(three_digit_sum(5)),
      hint='Count the numbers in your list.', steps=['Hundreds digit 1 gives 5 numbers, 2 gives 4, 3 gives 3, 4 gives 2 and 5 gives 1.', '5 + 4 + 3 + 2 + 1 = 15 numbers.'],
      src=['How many 3-digit numbers have digits that add up to 5?']),
    D(id='A3', tier='stretch', no='A3', label='A3', type='fields', skill='consecutive numbers', answer=[72, 73],
      q='The sum of two consecutive numbers (numbers that are next to each other, like 40 and 41) is 145.\nWhat are the two numbers? (Type the smaller number first.)', frame='The numbers are {f1} and {f2}', check=lambda: list(consecutive(145)),
      hint='Two numbers next to each other: one is 1 more than the other. Take the 1 away first and share what is left.',
      steps=['The bigger number is 1 more than the smaller one.', '145 − 1 = 144, and 144 ÷ 2 = 72, so the smaller number is 72.', 'The numbers are 72 and 73. Check: 72 + 73 = 145.'],
      src=['The sum of two consecutive numbers (numbers that are next to each other, like 40 and 41) is 145. What are the two numbers?']),
    D(id='A4', tier='stretch', no='A4', label='A4', type='number', skill='a repeating climb', answer=8,
      q=SNAIL_Q + '\nOn which day does it reach the top? (Type the number.)', check=lambda: snail_day(10, 3, 2),
      hint='Think about the last day: once the snail reaches the top it cannot slip back. Where is it at the start of that day?',
      steps=['Each day and night the snail gains 3 − 2 = 1 m. After 7 days and nights it is at 7 m.', 'On day 8 it climbs 3 m and reaches 10 m before it can slip.', 'It reaches the top on day 8.'],
      src=['A snail climbs 3 m up a 10 m wall each day, and slips down 2 m each night. On which day does it reach the top?']),

    # ================= Go further (B1 to B3)
    D(id='B1l', tier='challenge', no='B1 litres', label='B1 litres', type='number', skill='fractions of a tank', answer=45,
      q='A water tank is 1/3 full. After 20 litres are added it is 1/2 full. Then 1/4 of the water in the tank is let out.\nHow many litres of water are in the tank now? (Type the number.)', check=lambda: int(tank(20)[0]),
      hint='The 20 litres are the difference between 1/2 and 1/3 of the tank. What fraction of the tank is that?',
      steps=['1/2 − 1/3 = 1/6, so 20 litres are 1/6 of the tank and the full tank holds 120 litres.', 'Half full is 60 litres. Letting out 1/4 of it (15 litres) leaves 45 litres.'],
      src=['A water tank is 1/3 full. After 20 litres are added it is 1/2 full. Then 1/4 of the water in the tank is let out. How many litres of water are in the tank now? What fraction of the tank is full?']),
    D(id='B1f', tier='challenge', no='B1 fraction', label='B1 fraction', type='text', skill='fractions of a tank', accept=frac_accepts(F(3, 8)), shown='3/8',
      q='A water tank is 1/3 full. After 20 litres are added it is 1/2 full. Then 1/4 of the water in the tank is let out.\nWhat fraction of the tank is full now? (Type a fraction, like 5/12.)', check=lambda: frac_text(tank(20)[0] / tank(20)[1]),
      hint='Compare the litres of water now with the number of litres the full tank holds.', steps=['The full tank holds 120 litres and 45 litres are in it now.', '45/120 = 3/8 of the tank is full.'],
      src=['What fraction of the tank is full?']),
    D(id='B2', tier='challenge', no='B2', label='B2', type='fields', skill='supposition with three kinds', answer=[3, 6, 16],
      q='25 coins of 50¢, 10¢ and 20¢ are worth $5.30 altogether. There are twice as many 10¢ coins as 50¢ coins.\nHow many coins of each kind are there? (Type the numbers.)', frame='50¢ coins: {f1}     10¢ coins: {f2}     20¢ coins: {f3}',
      check=lambda: coin_mix(), hint='Each 50¢ coin comes with two 10¢ coins. What is a group of 3 coins like that worth?',
      steps=['Suppose all 25 coins were 20¢: that is $5.00.', 'Every 50¢ coin comes with two 10¢ coins. This group of 3 coins is worth 70¢, and replacing three 20¢ coins (60¢) with it adds 10¢.',
             'The extra is 30¢, so there are 3 groups: 3 fifty-cent coins, 6 ten-cent coins and 25 − 9 = 16 twenty-cent coins.', 'Check: 150¢ + 60¢ + 320¢ = 530¢ and 3 + 6 + 16 = 25.'],
      src=['25 coins of 50¢, 10¢ and 20¢ are worth $5.30 altogether. There are twice as many 10¢ coins as 50¢ coins. How many coins of each kind are there?']),
    D(id='B3', tier='challenge', no='B3', label='B3', type='text', skill='logic puzzle with positions', accept=names_accepts(row_order()), shown=', '.join(row_order()),
      q='Ali, Ben, Mei and Siti sit in a row of 4 chairs. Mei is not on either end. Ben does not sit next to Mei. Siti sits somewhere to the left of Ali. Ben is not on the left end.\nIn what order do they sit, from left to right? (Type the four names, with commas.)',
      check=lambda: ', '.join(row_order()), hint='Where can Mei sit? Try each chair for Mei and see what it does to Ben.',
      steps=['Mei is in chair 2 or 3. If Mei is in chair 3, the only chair not next to her is chair 1, but Ben is not on the left end, so that fails.', 'So Mei is in chair 2 and Ben is in chair 4.',
             'Siti and Ali are in chairs 1 and 3, and Siti is on the left: Siti 1, Ali 3.', 'The order is Siti, Mei, Ali, Ben.'],
      src=['Ali, Ben, Mei and Siti sit in a row of 4 chairs. Mei is not on either end. Ben does not sit next to Mei. Siti sits somewhere to the left of Ali. Ben is not on the left end. In what order do they sit, from left to right?']),
    D(id='pose', tier='challenge', no='Make up your own', label='Make up', type='selfcheck', open=True, marking_mode='open', skill='making up a problem',
      q='Make up a logic puzzle with three friends, three snacks and three clues. Check that only one answer fits.',
      hint='Pick the answer first, then write clues that rule out the other choices. Try all 6 ways of giving out the snacks.',
      steps=['This question is open: many puzzles are right.', 'Test your puzzle by trying every way of giving the three snacks to the three friends: exactly one should fit all three clues.',
             'Sample: Ravi, Siti and Ben have a rabbit, a hamster and a bird. Ravi has no bird and no hamster. Siti has no hamster. Then Ravi has the rabbit, Siti the bird and Ben the hamster.'],
      src=['Make up a logic puzzle with three friends, three snacks and three clues. Swap and solve; does only one answer fit?']),
]


# ---------------------------------------------------------------- variants
def _o_2(e):
    return start_money(e['x'], e['y'])


def _o_3(e):
    m, r = mei_ravi(7 * e['u'] + e['e'], e['e'])
    return dict(f1=m, f2=r)


def _o_4c(e):
    return all_squares(e['r'], e['c'])


def _o_6a(e):
    return years_until(3 * (e['c'] + e['y']) - e['y'], e['c'], 3)


def _o_a2n(e):
    return len(three_digit_sum(e['S']))


def _o_a3(e):
    a, b = consecutive(2 * e['a'] + 1)
    return dict(f1=a, f2=b)


def _o_a4(e):
    return snail_day(e['H'], e['c'], e['s'])


def _o_b1l(e):
    return int(tank(e['a'])[0])


finish(ITEMS)

VARIANTS = {
    '2': dict(
        base=dict(x=12, y=15),
        tpl=dict(vars=dict(x=[8, 10, 12, 14, 16], y=[10, 12, 15, 18, 20]),
                 q='Working backwards. Ali spent 1/3 of his money on a book. He then spent ${x} on lunch. He spent half of what was left on a gift. Ali had ${y} left at the end.\nHow much money did he start with? (Type the number of dollars.)',
                 answer='(2 * y + x) * 3 / 2', hint='Start here: write the steps in order. Then undo the LAST step first.',
                 steps=['Work backwards. Before the gift he had 2 × ${y} = ${gift}.', 'Before lunch he had ${gift} + ${x}.', 'That is 2/3 of his money, so work out 1/3 and then all of it. He started with ${ans}.'], derive=dict(gift='2 * y'),
                 ),
        fig=lambda e: G.backwards_fig(None, lunch=e['x'], left=e['y']),
        oracle=_o_2),
    '3': dict(
        base=dict(u=15, e=10),
        tpl=dict(vars=dict(u=[10, 15, 20, 25], e=[5, 10, 15, 20]), derive=dict(T='7 * u + e'),
                 q='Draw a model. Mei and Ravi have ${T} altogether. Ravi has ${e} more than 3/4 of Mei’s money.\nHow much money does each have? (Type the number of dollars.)',
                 frame='Mei: $ {f1}     Ravi: $ {f2}', answers=dict(f1='4 * u', f2='3 * u + e'),
                 hint='Mei is 4 equal units. How many units is 3/4 of Mei’s? Where does the ${e} go?',
                 steps=['Mei is 4 units. Ravi is 3 of the same units and ${e} more.', '7 units + ${e} = ${T}, so find 1 unit.', 'Mei and Ravi have {ans} dollars (Mei first).']),
        fig=lambda e: G.two_bars_fig(7 * e['u'] + e['e'], e['e']),
        oracle=_o_3),
    '4c': dict(
        base=dict(r=3, c=4),
        tpl=dict(vars=dict(r=[2, 3, 4], c=[3, 4, 5, 6]),
                 q='How many squares of ALL sizes are there altogether in this {r} by {c} grid? (Type the number.)',
                 answer='r * c + (r - 1) * (c - 1) + (r - 2) * (c - 2) + (r // 4) * (r - 3) * (c - 3)', hint='Count by size: all the 1 by 1 squares, then all the 2 by 2 squares, and so on. Add them.',
                 steps=['Count by size and add: the 1 by 1 squares, the 2 by 2 squares, and the bigger squares that fit.', 'There are {ans} squares altogether.']),
        fig=lambda e: G.grid_fig(e['r'], e['c']),
        oracle=_o_4c),
}

VARIANTS.update({
    '6a': dict(
        base=dict(c=9, y=7),
        tpl=dict(vars=dict(c=[7, 8, 9, 10, 11], y=[4, 5, 6, 7, 8]), derive=dict(m='3 * (c + y) - y'),
                 q='Mum is {m} years old and Mei is {c} years old.\nIn how many years will Mum be exactly 3 times as old as Mei? (Type the number. A table helps.)', answer='y',
                 hint='Make a table: after 1 year, 2 years, 3 years, and so on. Write both ages each time.',
                 steps=['Make a table of their ages year by year until Mum is 3 times as old.', 'It happens in {ans} years.']),
        oracle=_o_6a),
    'A1': dict(
        base=dict(L=24),
        tpl=dict(vars=dict(L=[12, 18, 24, 30, 36, 42]),
                 q='Siti spent 2/5 of her money, then 1/3 of what was left. She had ${L} left at the end.\nHow much did she start with? (Type the number of dollars.)', answer='L * 5 / 2',
                 hint='Work backwards. ${L} is what fraction of the money she had after the first spending?',
                 steps=['After spending 2/5 she had 3/5 of her money. Then she spent 1/3 of that, so 2/3 of it was left: ${L}.', 'Work backwards to 3/5 of her money, then to all of it. She started with ${ans}.']),
        fig=lambda e: G.siti_fig(e['L']),
        oracle=lambda e: siti_start(e['L'])),
    'A2n': dict(
        base=dict(S=5),
        tpl=dict(vars=dict(S=[3, 4, 5, 6, 7]),
                 q='How many 3-digit numbers have digits that add up to {S}? (Type the number.)', answer='S * (S + 1) / 2',
                 hint='Make a list in order: choose the hundreds digit, then list the numbers for it.',
                 steps=['Choose the hundreds digit from 1 up to {S}. For each choice, count the ways to share what is left between the tens and ones digits.', 'There are {ans} numbers.']),
        oracle=_o_a2n),
    'A3': dict(
        base=dict(a=72),
        tpl=dict(vars=dict(a=[48, 60, 72, 85, 99]), derive=dict(S='2 * a + 1'),
                 q='The sum of two consecutive numbers (numbers that are next to each other) is {S}.\nWhat are the two numbers? (Type the smaller number first.)', frame='The numbers are {f1} and {f2}',
                 answers=dict(f1='a', f2='a + 1'), hint='Two numbers next to each other: one is 1 more than the other. Take the 1 away first and share what is left.',
                 steps=['The bigger number is 1 more than the smaller one.', 'Take 1 away from {S} and share it between two equal numbers. The numbers are {ans}.']),
        oracle=_o_a3),
    'A4': dict(
        base=dict(H=10, c=3, s=2),
        tpl=dict(vars=dict(H=[10, 12, 15, 20], c=[3, 4, 5], s=[1, 2]),
                 q='A snail climbs {c} m up a {H} m wall each day, and slips down {s} m each night.\nOn which day does it reach the top? (Type the number.)', answer='(H - c + c - s - 1) // (c - s) + 1',
                 hint='Think about the last day: once the snail reaches the top it cannot slip back. Where is it at the start of that day?',
                 steps=['Each day and night the snail gains {c} − {s} m.', 'On the last day it climbs {c} m and reaches the top before it can slip. It reaches the top on day {ans}.']),
        oracle=_o_a4),
    'B1l': dict(
        base=dict(a=20),
        tpl=dict(vars=dict(a=[8, 12, 16, 20, 24, 28]),
                 q='A water tank is 1/3 full. After {a} litres are added it is 1/2 full. Then 1/4 of the water in the tank is let out.\nHow many litres of water are in the tank now? (Type the number.)', answer='9 * a / 4',
                 hint='The {a} litres are the difference between 1/2 and 1/3 of the tank. What fraction of the tank is that?',
                 steps=['1/2 − 1/3 = 1/6, so {a} litres are 1/6 of the tank.', 'Find the full tank, then half of it, then take 1/4 of that water out. {ans} litres are left.']),
        oracle=_o_b1l),
})

polish(ITEMS, VARIANTS)
