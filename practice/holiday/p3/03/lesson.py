"""Online practice for Level 3 (Primary 3, ages 8-10) holiday lesson 3: Times Table Treasure (tables of 6, 7, 8 and 9).

The questions are the ones printed in the Level 3 holiday workbook (p3/workbook_html.js builds it from p3/content/l3.js: Start here = the lesson's
workbook() pages; Think harder 1 to 4 and Go further 5 to 7 = qbank stretch[0..3] and challenge[-3:]; the Investigation = p3/gifted.json lesson 3; the lesson has
no Take-home pair, because deck.takeHome is empty).  Every answer is recomputed by an INDEPENDENT checker below (loops over the numbers of the question, never
a copy of the printed answer); build_holiday.py stops if a checker and the printed answer differ.  The figures are the workbook's own (the array of dots) or
redrawn from the printed tables and grid (times_fig, grid_fig in p3lib.py).
"""
import itertools, os, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from hlib import *      # noqa: E402,F401
from p3lib import *     # noqa: E402,F401

META = dict(level=3, lesson=3, key='p3', title='Times Table Treasure', workbook_title='TIMES TABLE TREASURE', topic='Tables of 6, 7, 8 and 9', strand='Multiplication',
            sources=['p3/content/l3.js', 'p3/gifted.json'],
            intro=['Look for a pattern, test it, and use facts you know to find facts you do not know.',
                   'Use paper for workings and drawings, then type the answers here.',
                   'When a question asks for a list, type the numbers with a comma between them.'])
FIG = figs2()
SK = 'Multiplication'


def I(**kw):
    kw.setdefault('strand', SK)
    return kw


def one(solutions):
    """The only solution, or None if there are none or several (a puzzle must have exactly one answer)."""
    return solutions[0] if len(solutions) == 1 else None


def times(t, upto=10):
    """The t times table built by repeated adding (no formula)."""
    out, v = [], 0
    for _ in range(upto):
        v += t
        out.append(v)
    return out


def last_digits(t, upto=10):
    return [v % 10 for v in times(t, upto)]


def diffs(seq):
    return {b - a for a, b in zip(seq, seq[1:])}


UD = ['They go up by 1 each time', 'They go down by 1 each time', 'They stay the same', 'They go up by 2 each time']
UD_OF = {1: UD[0], -1: UD[1], 0: UD[2], 2: UD[3]}
YN = ['Yes', 'No']

# ---- the grid puzzle (Q4): rows 7, ?, ?  columns ?, ?, ?;  given 56 (row 1, col 1), 81 (row 2, col 3), 48 (row 3, col 1), 36 (row 3, col 2)


def grid_solve():
    out = []
    for r2, r3, c1, c2, c3 in itertools.product(range(1, 11), repeat=5):
        if 7 * c1 == 56 and r2 * c3 == 81 and r3 * c1 == 48 and r3 * c2 == 36:
            out.append([r2, r3, c1, c2, c3])
    return out


GRID = one(grid_solve())            # [r2, r3, c1, c2, c3]
GRID_CELLS = None
if GRID:
    _rows, _cols = [7, GRID[0], GRID[1]], GRID[2:]
    GRID_CELLS = [[r * c for c in _cols] for r in _rows]
GRID_Q = grid_fig([None, None, None], [7, None, None], [[56, None, None], [None, None, 81], [48, 36, None]], 'A grid puzzle: row numbers 7, ? and ?; column numbers ?, ? and ?; some products are given')
GRID_SOL = grid_fig(GRID[2:], [7, GRID[0], GRID[1]], GRID_CELLS, 'The finished grid') if GRID else ''


def chair_ways(total=36):
    """All (rows, chairs in each row) with at least 2 rows and at least 2 chairs in each row, found by trying 2 rows, 3 rows, 4 rows, ..."""
    out = []
    for rows in range(2, total):
        for per in range(2, total):
            if rows * per == total:
                out.append((rows, per))
    return out


def in_both(a, b, lo=10, hi=99):
    """2-digit numbers in both the a and b times tables, found by listing the two tables (no divisibility test)."""
    A, B = set(times(a, 100)), set(times(b, 100))
    return [n for n in range(lo, hi + 1) if n in A and n in B]


T9 = times(9)
T7 = times(7)

ITEMS = [
    # ================= Start here (workbook lesson 3, No.1 to No.6)
    I(id='1-fill', tier='core', no='1', type='fields', skill='patterns in the 9 times table', answer=[27, 36, 45, 54, 63, 72, 81, 90],
      svg=times_fig([('9 ×', [str(i) for i in range(1, 11)]), ('Answer', ['9', '18'] + [None] * 8)], 'The 9 times table: 9 times 1 to 9 times 10, the first two answers are 9 and 18'),
      frame='9 × 3 = {f1}    9 × 4 = {f2}    9 × 5 = {f3}    9 × 6 = {f4}    9 × 7 = {f5}    9 × 8 = {f6}    9 × 9 = {f7}    9 × 10 = {f8}',
      q='Patterns in the 9 times table. Fill in the answers. The first two are done for you: 9 × 1 = 9 and 9 × 2 = 18.',
      check=lambda: times(9)[2:],
      hint='Count on in 9s from 18. Each answer is 9 more than the one before. Check each one against the answer before it.',
      steps=['Count on in 9s: 9, 18, 27, 36, 45, 54, 63, 72, 81, 90.', 'Check: each answer is 9 more than the one before it.', '9 × 3 = 27, 9 × 4 = 36, 9 × 5 = 45, 9 × 6 = 54, 9 × 7 = 63, 9 × 8 = 72, 9 × 9 = 81 and 9 × 10 = 90.'],
      src=['Patterns in the 9 times table. Fill in the answers.']),
    I(id='1a-tens', tier='core', no='1(a) tens', type='choice', skill='patterns in the 9 times table', options=UD, answer=UD[0],
      q='Look at your 9 times table answers: 09, 18, 27, 36 ... (write 9 as 09). Look at the tens digits, the first digit of each answer. How do the tens digits go as you go along the table?',
      check=lambda: UD_OF[diffs([v // 10 for v in times(9)]).pop()] if len(diffs([v // 10 for v in times(9)])) == 1 else None,
      hint='Write down only the tens digit of each answer, one after the other. How much does it change each time?',
      steps=['The tens digits are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 (the answer 9 is 09, so its tens digit is 0).', 'Each tens digit is 1 more than the one before: the tens digits go up by 1 each time.'],
      src=['Look at the tens digits and the ones digits. Finish the sentences.', 'The tens digits go']),
    I(id='1a-ones', tier='core', no='1(a) ones', type='choice', skill='patterns in the 9 times table', options=UD, answer=UD[1],
      q='Look at your 9 times table answers again. Now look at the ones digits, the last digit of each answer. How do the ones digits go as you go along the table?',
      check=lambda: UD_OF[diffs([v % 10 for v in times(9)]).pop()] if len(diffs([v % 10 for v in times(9)])) == 1 else None,
      hint='Write down only the ones digit of each answer, one after the other. How much does it change each time?',
      steps=['The ones digits are 9, 8, 7, 6, 5, 4, 3, 2, 1, 0.', 'Each ones digit is 1 less than the one before: the ones digits go down by 1 each time.'],
      src=['Look at the tens digits and the ones digits. Finish the sentences.', 'The ones digits go']),
    I(id='1b-ans', tier='core', no='1(b) 9 × 8', type='number', skill='patterns in the 9 times table', answer=72,
      q='Ali says 9 × 8 = 81, because 8 + 1 = 9. Ali is wrong. Use the pattern of the tens digits and the ones digits to work out what 9 × 8 really is.',
      check=lambda: sum([9] * 8),
      hint='Look at the answers for 9 × 7 and 9 × 9 in your table. Where does 9 × 8 fit between them?',
      steps=['The tens digit of 9 × 8 is 1 less than 8, so it is 7.', 'The ones digit goes down by 1 each time, so after 9 × 7 = 63 the ones digit is 2.', '9 × 8 = 72. (81 is 9 × 9.)'],
      src=['Ali says 9 × 8 = 81, because 8 + 1 = 9. Use a pattern to explain why he is wrong.']),
    I(id='1b', tier='core', no='1(b) why', type='selfcheck', open=True, skill='explaining a pattern',
      q='Ali says 9 × 8 = 81, because 8 + 1 = 9. Use a pattern in the 9 times table to explain why he is wrong. Write your idea, then compare with the answer shown.',
      check=lambda: [sum([9] * 8), sum([9] * 9), digit_sum(sum([9] * 8)), digit_sum(sum([9] * 9))],
      hint='His check is that the digits of the answer add up to 9. Is that check enough? Look for another number in your table whose digits add up to 9.',
      steps=['In the pattern, the tens digit of 9 × 8 is 1 less than 8, which is 7, and the ones digit goes down by 1 each time, which gives 2. So 9 × 8 = 72.', 'The digits of 72 add up to 9 as well (7 + 2 = 9), and so do the digits of 81 (8 + 1 = 9). Adding to 9 is true for every answer in the table, so it cannot tell you which one is 9 × 8.', '81 is 9 × 9, the next number in the table.'],
      src=['Ali says 9 × 8 = 81, because 8 + 1 = 9. Use a pattern to explain why he is wrong.']),

    I(id='2-fill', tier='core', no='2', type='fields', skill='last digits', answer=[1, 8, 5, 2, 9, 6, 3, 0],
      svg=times_fig([('7 ×', [str(i) for i in range(1, 11)]), ('Answer', [str(v) for v in times(7)]), ('Last digit', ['7', '4'] + [None] * 8)], 'The 7 times table with the last digit of each answer; the first two last digits are 7 and 4'),
      frame='21 ends in {f1}    28 ends in {f2}    35 ends in {f3}    42 ends in {f4}    49 ends in {f5}    56 ends in {f6}    63 ends in {f7}    70 ends in {f8}',
      q='Last digits in the 7 times table. Write only the LAST digit of each answer. The first two are done for you: 7 ends in 7 and 14 ends in 4.',
      check=lambda: [v % 10 for v in times(7)][2:],
      hint='Look only at the ones place of each answer, the digit on the right. For example 14 ends in 4.',
      steps=['The answers are 7, 14, 21, 28, 35, 42, 49, 56, 63, 70.', 'Their last digits are 7, 4, 1, 8, 5, 2, 9, 6, 3, 0.', 'All ten digits from 0 to 9 appear, each once.'],
      src=['Last digits in the 7 times table. Write only the LAST digit of each answer.']),
    I(id='2a', tier='core', no='2(a)', type='set', ordered=False, grouped=False, skill='last digits', answer=[3, 9],
      q='Test the 3, 6 and 9 times tables. Which of them also use all ten last digits, 0 to 9? Type the numbers of the tables you find, with a comma between.',
      check=lambda: [t for t in (3, 6, 9) if len(set(last_digits(t))) == 10],
      hint='For each table, write the answers up to × 10 and look only at the last digit of each. Do you see ten different last digits?',
      steps=['The 3 times table ends 3, 6, 9, 2, 5, 8, 1, 4, 7, 0: all ten digits, each once.', 'The 6 times table ends 6, 2, 8, 4, 0, 6, 2, 8, 4, 0: only five different digits, all even.', 'The 9 times table ends 9, 8, 7, 6, 5, 4, 3, 2, 1, 0: all ten digits, each once.', 'The 3 and the 9 times tables use all ten last digits.'],
      src=['Test the 3, 6 and 9 times tables. Which of them also use all ten last digits?']),
    I(id='2b', tier='core', no='2(b)', type='number', skill='last digits', answer=2,
      q='Without working out 7 × 46, what is its last digit? Type the digit.',
      check=lambda: last_digits(7, 6)[5],
      hint='46 is 40 and 6. What is the last digit of 7 × 40? Then think about 7 × 6.',
      steps=['7 × 40 is a multiple of 10, so it ends in 0. Only 7 × 6 can change the last digit.', '7 × 6 = 42, which ends in 2.', 'So 7 × 46 ends in 2. (Check: 7 × 46 = 322.)'],
      src=['Without working out 7 × 46, what is its last digit? Explain.']),
    I(id='2b-why', tier='core', no='2(b) why', type='selfcheck', open=True, skill='explaining a pattern',
      q='Explain how you know the last digit of 7 × 46 without working out all of 7 × 46. Write your idea, then compare with the answer shown.',
      check=lambda: [last_digits(7, 6)[5], (7 * 40) % 10, (7 * 6) % 10, 7 * 46],
      hint='Split 46 into 40 and 6. Which part can change the last digit?',
      steps=['Split 46 into 40 and 6. 7 × 40 = 280 ends in 0, so it does not change the last digit.', '7 × 6 = 42 ends in 2, so the last digit of 7 × 46 is 2.', 'Only the ones digit of 46 decides the last digit.'],
      src=['Without working out 7 × 46, what is its last digit? Explain.']),

    I(id='3a', tier='core', no='3(a)', type='fields', skill='splitting an array', answer=[40, 16, 56], svg=FIG['l3_array'], frame='5 × 8 = {f1}      2 × 8 = {f2}      so  7 × 8 = {f3}',
      q='Mei does not know 7 × 8. She splits 7 rows of 8 dots into two parts, as in the picture. Fill in the boxes.',
      check=lambda: [sum([8] * 5), sum([8] * 2), sum([8] * 5) + sum([8] * 2)],
      hint='Count the dots in each part. Each part is a fact you know. Then put the two parts together.',
      steps=['The top part is 5 rows of 8: 5 × 8 = 40.', 'The bottom part is 2 rows of 8: 2 × 8 = 16.', 'Put them together: 40 + 16 = 56, so 7 × 8 = 56.'],
      src=['Mei does not know 7 × 8. She splits 7 rows of 8 dots into two parts.', '5 × 8 = ______      2 × 8 = ______      so  7 × 8 = ______']),
    I(id='3b-ans', tier='core', no='3(b) 9 × 6', type='number', skill='splitting an array', answer=54,
      q='Split 9 × 6 into two facts you know. Show your working on paper. What is 9 × 6? Type the answer.',
      check=lambda: 5 * 6 + 4 * 6,
      hint='Think of 9 rows of 6 dots. Where could you split the rows into two parts that you know well? Add the two facts.',
      steps=['Split 9 rows into 5 rows and 4 rows: 5 × 6 = 30 and 4 × 6 = 24.', '30 + 24 = 54.', 'So 9 × 6 = 54.'],
      src=['Split 9 × 6 into two facts you know. Show your working.']),
    I(id='3b', tier='core', no='3(b) split', type='selfcheck', open=True, skill='splitting an array',
      q='Split 9 × 6 into two facts you know. Show your working on paper: write the two facts and add them. Then compare with the answers shown.',
      check=lambda: [5 * 6 + 4 * 6, 10 * 6 - 6, 3 * 6 + 6 * 6, 9 * 6],
      hint='Choose a number of rows that is easy, such as 5 rows or 10 rows. Then think about the rows that are left over, or the row you take away.',
      steps=['One way: 5 × 6 + 4 × 6 = 30 + 24 = 54.', 'Another way: 10 × 6 - 6 = 60 - 6 = 54.', 'Other splits work too, for example 3 × 6 + 6 × 6 = 18 + 36 = 54. Every correct split gives 54.'],
      src=['Split 9 × 6 into two facts you know. Show your working.']),

    I(id='4a', tier='core', no='4(a)', type='fields', skill='grid puzzle', answer=GRID, svg=GRID_Q,
      frame='Row numbers (top to bottom): 7, {f1}, {f2}.      Column numbers (left to right): {f3}, {f4}, {f5}.',
      q='(if time) Grid puzzle. Each number in the grid is the row number × the column number. The row and column numbers are all from 1 to 10. Find the missing row numbers and column numbers. The first row number, 7, is given.',
      check=lambda: grid_solve()[0] if len(grid_solve()) == 1 else None, sol_fig=lambda got: GRID_SOL,
      hint='56 ÷ 7 gives the first column number. For the number 81, which two numbers from 1 to 10 can you multiply to make it?',
      steps=['Row 7 and the number 56: 56 ÷ 7 = 8, so the first column number is 8.', 'The first column has 48 in the third row: 48 ÷ 8 = 6, so the third row number is 6. Then 36 ÷ 6 = 6, so the second column number is 6.', '81 can only be 9 × 9 (with numbers from 1 to 10), so the second row number is 9 and the third column number is 9.', 'Row numbers: 7, 9, 6. Column numbers: 8, 6, 9.'],
      src=['(if time) Grid puzzle. Each number in the grid is the row number × the column number. The row and column numbers are all from 1 to 10.', 'Hint: 56 ÷ 7 = ? gives the first column number.']),
    I(id='4b', tier='core', no='4(b)', type='fields', skill='grid puzzle', answer=[GRID_CELLS[0][1], GRID_CELLS[0][2], GRID_CELLS[1][0], GRID_CELLS[1][1], GRID_CELLS[2][2]] if GRID else None, svg=GRID_Q,
      frame='First row: 56, {f1}, {f2}.      Second row: {f3}, {f4}, 81.      Third row: 48, 36, {f5}.',
      q='(if time) Now fill in the missing numbers inside the grid. Use the row numbers and the column numbers you found.',
      check=lambda: [GRID_CELLS[0][1], GRID_CELLS[0][2], GRID_CELLS[1][0], GRID_CELLS[1][1], GRID_CELLS[2][2]], sol_fig=lambda got: GRID_SOL,
      hint='Each box is its row number times its column number. Find the row number and the column number of each empty box.',
      steps=['First row (7): 7 × 6 = 42 and 7 × 9 = 63.', 'Second row (9): 9 × 8 = 72 and 9 × 6 = 54.', 'Third row (6): 6 × 9 = 54.', 'The finished grid: 7 row: 56, 42, 63. 9 row: 72, 54, 81. 6 row: 48, 36, 54.'],
      src=['(if time) Grid puzzle. Each number in the grid is the row number × the column number.', 'then fill in the grid.']),

    I(id='5a-rows', tier='core', no='5(a) rows', type='set', ordered=True, grouped=False, skill='systematic list', answer=[r for r, _ in chair_ways()],
      q='Ben puts 36 chairs in equal rows (at least 2 rows, at least 2 chairs in each row). Find ALL the ways. Try 2 rows, then 3 rows, then 4 rows, and so on. Type every number of rows that works, smallest first, with a comma between. (A way with 2 rows of 5 is different from a way with 5 rows of 2.)',
      check=lambda: [r for r, _ in chair_ways()],
      hint='Try 2 rows, then 3 rows, then 4 rows. For each, can 36 chairs be shared into that many equal rows with none left over? Keep going in order so you do not miss any.',
      steps=['2 rows: 18 chairs in each row. 3 rows: 12. 4 rows: 9. 5 rows: 36 does not share equally. 6 rows: 6.', '7 rows and 8 rows do not work. 9 rows: 4. 10 and 11 rows do not work. 12 rows: 3.', '13 to 17 rows do not work. 18 rows: 2. More rows would leave fewer than 2 chairs in each row, so stop.', 'The numbers of rows that work are 2, 3, 4, 6, 9, 12 and 18.'],
      src=['Ben puts 36 chairs in equal rows (at least 2 rows, at least 2 chairs in each row). Find ALL the ways. Try 2 rows, then 3 rows, then 4 rows, and so on.', 'Write only the ways that work.']),
    I(id='5a-chairs', tier='core', no='5(a) chairs', type='set', ordered=True, grouped=False, skill='systematic list', answer=[p for _, p in chair_ways()],
      q='For each of your ways in 5(a), how many chairs are in each row? Type them in the same order as your numbers of rows, with a comma between.',
      check=lambda: [p for _, p in chair_ways()],
      hint='Go along your list of numbers of rows. For each one, how many chairs are in every row? 36 chairs shared into that many equal rows.',
      steps=['2 rows have 18 chairs each, 3 rows have 12, 4 rows have 9, 6 rows have 6, 9 rows have 4, 12 rows have 3 and 18 rows have 2.', 'In the same order the chairs in each row are 18, 12, 9, 6, 4, 3, 2.'],
      src=['Ben puts 36 chairs in equal rows (at least 2 rows, at least 2 chairs in each row).', 'Write only the ways that work.']),
    I(id='5b', tier='core', no='5(b)', type='number', skill='systematic list', answer=7,
      q='Ben puts 36 chairs in equal rows (at least 2 rows, at least 2 chairs in each row). How many ways are there? Type the number.',
      check=lambda: len(chair_ways()),
      hint='Count the ways that work when you try 2 rows, then 3 rows, then 4 rows, and so on, in order.',
      steps=['Try the number of rows in order: 2, 3, 4, 6, 9, 12 and 18 work.', 'That is 7 ways.'],
      src=['How many ways are there?']),
    I(id='5c', tier='core', no='5(c)', type='fields', skill='systematic list', answer=[6, 6],
      frame='{f1} rows of {f2} chairs',
      q='Most of the ways to put 36 chairs in rows come in pairs: turn a way round (swap the number of rows and the number of chairs in each row) and you get its partner. Which way has no partner? Fill in the boxes.',
      check=lambda: one([[r, p] for r, p in chair_ways() if (p, r) == (r, p)]),
      hint='Turn each way round, swapping the two numbers. Which way looks exactly the same when it is turned round?',
      steps=['Turned round, 2 rows of 18 becomes 18 rows of 2. Every way has a partner like this ...', '... except 6 rows of 6. Turned round it is still 6 rows of 6.', 'So 6 rows of 6 is the way with no partner.'],
      src=['Most ways come in pairs, like 2 rows of 18 and 18 rows of 2. Which way has no partner? Why?']),
    I(id='5c-why', tier='core', no='5(c) why', type='selfcheck', open=True, skill='explaining a pattern',
      q='Why does that way have no partner? How does that tell you why the number of ways is odd? Write your idea, then compare with the answer shown.',
      check=lambda: [len(chair_ways()), [w for w in chair_ways() if (w[1], w[0]) == w]],
      hint='Think about what happens to 6 rows of 6 when you turn it round. What about the other ways?',
      steps=['Turned round, 6 rows of 6 is the same way, so it has no partner.', 'All the other ways come in pairs, so they make an even number of ways.', 'One way with no partner plus an even number gives an odd number of ways: 7.'],
      src=['Most ways come in pairs, like 2 rows of 18 and 18 rows of 2. Which way has no partner? Why?']),

    I(id='6a', tier='core', no='6(a)', type='set', ordered=False, grouped=False, skill='common multiples', answer=[24, 48, 72, 96],
      q='(if time) Number riddle. Find ALL the 2-digit numbers that can be divided exactly by 6 AND by 8. Here are the 2-digit numbers in the 8 times table: 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96. Type the ones that are also in the 6 times table (6, 12, 18 ...), with a comma between.',
      check=lambda: in_both(6, 8),
      hint='Count in 6s: 6, 12, 18 ... up to 96. Which of the numbers in the 8 times table list do you land on?',
      steps=['Count in 6s up to 96: 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96.', 'The numbers from the 8 times table list that are also here are 24, 48, 72 and 96.', 'These are the 2-digit numbers that can be divided exactly by 6 and by 8.'],
      src=['(if time) Number riddle.', 'Find ALL the 2-digit numbers that can be divided exactly by 6 AND by 8. Here are the 2-digit numbers in the 8 times table: 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96.']),
    I(id='6b', tier='core', no='6(b)', type='number', skill='common multiples', answer=48,
      q='(if time) I am one of your numbers from 6(a), a 2-digit number that can be divided exactly by 6 and by 8. My digits add up to 12. What number am I?',
      check=lambda: one([n for n in in_both(6, 8) if digit_sum(n) == 12]),
      hint='Add the two digits of each of your numbers from 6(a). Which one makes 12?',
      steps=['The digits of 24 add up to 6, of 48 to 12, of 72 to 9 and of 96 to 15.', 'Only 4 + 8 = 12, so the number is 48.'],
      src=['I am one of your numbers. My digits add up to 12. What number am I?']),

    # ================= Investigation (Investigation and look back page, No.8: Is it always true? Digit sums)
    I(id='I8-easy', tier='invest', no='8 easy', type='fields', skill='digit sums', answer=[45, 9, 54, 9], frame='9 × 5 = {f1}, the digits add up to {f2}.      9 × 6 = {f3}, the digits add up to {f4}.',
      q='Investigation: Is it always true? Digit sums. In the 9 times table the digits of each answer add up to 9: 9, 18 (1 + 8), 27 (2 + 7), 36 (3 + 6) ... Easy first step: write the 9 times table up to 9 × 6 and add the digits of each answer. Fill in the last two.',
      check=lambda: [T9[4], digit_sum(T9[4]), T9[5], digit_sum(T9[5])],
      hint='Count on in 9s from 36. Then add the two digits of each answer.',
      steps=['9 × 5 = 45 and 4 + 5 = 9.', '9 × 6 = 54 and 5 + 4 = 9.', 'So far every answer has digits that add up to 9.'],
      src=['In the 9 times table the digits of each answer add up to 9: 9, 18 (1 + 8), 27 (2 + 7), 36 (3 + 6) ...', 'Easy first step: write the 9 times table up to 9 × 6 and add the digits of each answer.']),
    I(id='I8a-fill', tier='invest', no='8(a)', type='fields', skill='digit sums', answer=[99, 18, 108, 9], frame='9 × 11 = {f1}, the digits add up to {f2}.      9 × 12 = {f3}, the digits add up to {f4}.',
      q='Carry on the 9 times table to 9 × 12. Add the digits of each answer.',
      check=lambda: [times(9, 12)[10], digit_sum(times(9, 12)[10]), times(9, 12)[11], digit_sum(times(9, 12)[11])],
      hint='9 × 10 = 90. Count on 9 for 9 × 11, and 9 again for 9 × 12. Then add all the digits of each answer.',
      steps=['9 × 11 = 99. The digits add up to 9 + 9 = 18.', '9 × 12 = 108. The digits add up to 1 + 0 + 8 = 9.'],
      src=['Carry on the 9 times table to 9 × 12. Add the digits of each answer.']),
    I(id='I8a-always', tier='invest', no='8(a) always?', type='choice', skill='digit sums', options=['Yes, it is always 9', 'No, it is not always 9'], answer='No, it is not always 9',
      q='Carry on the 9 times table to 9 × 12. Add the digits of each answer. Is the total ALWAYS 9? Choose your answer.',
      check=lambda: 'Yes, it is always 9' if all(digit_sum(v) == 9 for v in times(9, 12)) else 'No, it is not always 9',
      hint='Work out the digit sum of every answer from 9 × 1 to 9 × 12. Is there any answer where the total is not 9?',
      steps=['The digit sums of 9, 18, 27, ... 90 are all 9.', 'But 9 × 11 = 99, and 9 + 9 = 18. So the total is not always 9.', 'Look again: 18 is in the 9 times table, and its digits add up to 9. So the digit sum of an answer in the 9 times table is 9, or a number that is itself in the 9 times table.'],
      src=['Carry on the 9 times table to 9 × 12. Add the digits of each answer. Is the total ALWAYS 9? Write what you find.']),
    I(id='I8b', tier='invest', no='8(b)', type='choice', skill='digit sums',
      options=['Every digit sum is in the 3 times table (3, 6, 9, 12 ...)', 'Every digit sum is 9', 'Every digit sum is odd', 'The digit sums are all different'],
      answer='Every digit sum is in the 3 times table (3, 6, 9, 12 ...)',
      q='Try the 3 times table and the 6 times table up to × 12. Add the digits of each answer. What do you notice about the digit sums?',
      check=lambda: (lambda s: 'Every digit sum is in the 3 times table (3, 6, 9, 12 ...)' if (all(x in set(times(3, 20)) for x in s) and not all(x == 9 for x in s) and not all(x % 2 == 1 for x in s) and len(set(s)) < len(s)) else None)([digit_sum(v) for v in times(3, 12) + times(6, 12)]),
      hint='Write the 3 times table and the 6 times table up to × 12 and add the digits of each answer. Look at the list of totals you get.',
      steps=['3 times table: 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36 have digit sums 3, 6, 9, 3, 6, 9, 3, 6, 9, 3, 6, 9.', '6 times table: 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72 have digit sums 6, 3, 9, 6, 3, 9, 6, 3, 9, 6, 3, 9.', 'Every digit sum is 3, 6 or 9: a number in the 3 times table.'],
      src=['Try the 3 times table and the 6 times table up to × 12. Add the digits of each answer. What do you notice?']),
    I(id='I8c-fill', tier='invest', no='8(c)', type='fields', skill='digit sums', answer=[4, 8, 3, 7, 2, 6, 10, 5],
      frame='4 → {f1}    8 → {f2}    12 → {f3}    16 → {f4}    20 → {f5}    24 → {f6}    28 → {f7}    32 → {f8}',
      q='Try the 4 times table: 4, 8, 12, 16, 20, 24, 28, 32. Add the digits of each answer and type the total for each one.',
      check=lambda: [digit_sum(v) for v in times(4, 8)],
      hint='Add the digits of each answer. For a 1-digit answer, the digit sum is just that number.',
      steps=['4 → 4, 8 → 8, 12 → 1 + 2 = 3, 16 → 1 + 6 = 7.', '20 → 2 + 0 = 2, 24 → 2 + 4 = 6, 28 → 2 + 8 = 10, 32 → 3 + 2 = 5.', 'The digit sums are 4, 8, 3, 7, 2, 6, 10, 5.'],
      src=['Try the 4 times table. Is it the same?']),
    I(id='I8c-same', tier='invest', no='8(c) same?', type='choice', skill='digit sums', options=['Yes, it is the same', 'No, it is different'], answer='No, it is different',
      q='Try the 4 times table. Is it the same as the 3, 6 and 9 times tables? Look at the digit sums you wrote. Choose your answer.',
      check=lambda: 'Yes, it is the same' if all(digit_sum(v) % 3 == 0 for v in times(4, 12)) else 'No, it is different',
      hint='Look at the digit sums of the 4 times table. Do they follow the same pattern that you noticed for the 3 and 6 times tables?',
      steps=['The digit sums of the 4 times table include 4, 8, 7, 2, 10 and 5. These are not in the 3 times table.', 'So the 4 times table is different from the 3, 6 and 9 times tables.'],
      src=['Try the 4 times table. Is it the same? What can you say about the 3, 6 and 9 times tables?']),
    I(id='I8c-say', tier='invest', no='8(c) say', type='selfcheck', open=True, skill='explaining a pattern',
      q='What can you say about the 3, 6 and 9 times tables? Write your idea, then compare with the answer shown.',
      check=lambda: all(digit_sum(v) % 3 == 0 for t in (3, 6, 9) for v in times(t, 12)),
      hint='Look at your digit sums for the 3, 6 and 9 times tables. What kind of numbers are they?',
      steps=['For the 3, 6 and 9 times tables, the digit sum of every answer is in the 3 times table (3, 6, 9, 12 ...). This is checked for the first 12 answers of each table.', 'For the 9 times table it is even stronger: the digit sum of an answer is 9, or 18 (also in the 9 times table).', 'The 4 times table does not do this, so the pattern belongs to the 3, 6 and 9 times tables.'],
      src=['Try the 4 times table. Is it the same? What can you say about the 3, 6 and 9 times tables?']),

    # ================= Think harder (workbook Think harder, No.1 to No.4)
    I(id='T1', tier='stretch', no='T1', type='set', ordered=False, grouped=False, skill='patterns in the 9 times table', answer=[54, 72],
      q='The digits of every answer in the 9 times table (9 × 1 to 9 × 10) add up to 9. Which of these are in the 9 times table: 54, 65, 72, 83? Type them with a comma between.',
      check=lambda: [n for n in (54, 65, 72, 83) if n in T9],
      hint='Add the digits of each number. Or count in 9s to see which numbers you land on.',
      steps=['54: 5 + 4 = 9. 72: 7 + 2 = 9.', '65: 6 + 5 = 11 and 83: 8 + 3 = 11, so they are not.', '54 = 9 × 6 and 72 = 9 × 8 are in the 9 times table.'],
      src=['The digits of every answer in the 9 times table (9 × 1 to 9 × 10) add up to 9. Which of these are in the 9 times table: 54, 65, 72, 83?']),
    I(id='T2', tier='stretch', no='T2', type='number', skill='last digits', answer=2,
      q='What is the last digit of 8 × 8 × 8? Use last digits only.',
      check=lambda: ((8 * 8 % 10) * 8) % 10,
      hint='Work in two steps. First 8 × 8: keep only its last digit. Then multiply that last digit by 8 and look at the last digit again.',
      steps=['8 × 8 = 64, which ends in 4.', '4 × 8 = 32, which ends in 2.', 'So 8 × 8 × 8 ends in 2. (8 × 8 × 8 = 512.)'],
      src=['What is the last digit of 8 × 8 × 8? Use last digits only.']),
    I(id='T3', tier='stretch', no='T3', type='choice', skill='even numbers in the 6 times table', options=['Yes, he is right', 'No, he is not right'], answer='Yes, he is right',
      q='Ravi says: "Every answer in the 6 times table is even." Is he right? Choose your answer.',
      check=lambda: 'Yes, he is right' if all(v % 2 == 0 for v in times(6, 100)) else 'No, he is not right',
      hint='Write the 6 times table and look at the last digit of each answer.',
      steps=['The 6 times table is 6, 12, 18, 24, 30, 36 ... and every answer ends in 6, 2, 8, 4 or 0.', 'Those are all even digits, so every answer is even. Ravi is right.'],
      src=['Ravi says: "Every answer in the 6 times table is even." Is he right? Explain why.']),
    I(id='T3-why', tier='stretch', no='T3 why', type='selfcheck', open=True, skill='explaining a pattern',
      q='Explain why every answer in the 6 times table is even. Write your idea, then compare with the answer shown.',
      check=lambda: all(v % 2 == 0 for v in times(6, 100)),
      hint='Think of 6 groups. Can you put the groups in pairs, with none left over?',
      steps=['6 groups can always be put into 3 pairs of groups, so nothing is left over.', 'So the answer is always even. For example 6 × 7 = 3 × 14 = 42.'],
      src=['Ravi says: "Every answer in the 6 times table is even." Is he right? Explain why.']),
    I(id='T4', tier='stretch', no='T4', type='set', ordered=False, grouped=False, skill='systematic list', answer=[28, 91],
      q='Find ALL the 2-digit numbers that can be divided exactly by 7 and whose digits add up to 10. Type them with a comma between.',
      check=lambda: [n for n in T7 + times(7, 14)[10:] if 10 <= n <= 99 and digit_sum(n) == 10],
      hint='Write the 7 times table up to 98 in order. Then add the digits of each 2-digit number on your list.',
      steps=['The 2-digit numbers in the 7 times table are 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98.', 'Their digit sums are 5, 3, 10, 8, 6, 13, 11, 9, 7, 14, 12, 10, 17.', 'Only 28 and 91 make 10.'],
      src=['Find ALL the 2-digit numbers that can be divided exactly by 7 and whose digits add up to 10.']),

    # ================= Go further (workbook Go further, No.5 to No.7)
    I(id='G5', tier='challenge', no='G5', type='selfcheck', open=True, skill='making up a riddle',
      q='Make up your own riddle: "I am a 2-digit number in the ___ times table ..." Write 2 or 3 clues (about odd or even, the digits, being between two numbers). Check that only ONE number fits, by listing the table. Swap with a partner. Do this on paper, then compare with the example shown.',
      check=lambda: [n for n in times(7, 14) if 10 <= n <= 99 and n % 2 == 1 and digit_sum(n) == 10],
      hint='Pick a table and write its 2-digit numbers. Choose one as your secret number. Then write clues until only your number is left on the list.',
      steps=['Answers vary. Check that the secret number is in the table, every clue is true, and the list leaves exactly one number.', 'Example: "I am a 2-digit number in the 7 times table. I am odd. My digits add up to 10." The odd 2-digit numbers in the 7 times table are 21, 35, 49, 63, 77 and 91, and only 91 has digits that add up to 10.'],
      src=['Make up your own riddle: "I am a 2-digit number in the ___ times table …" Write 2 or 3 clues (about odd or even, the digits, being between two numbers). Check that only ONE number fits, by listing the table. Swap with a partner.']),
    I(id='G6', tier='challenge', no='G6', type='number', skill='last digits', answer=1,
      q='Ben keeps multiplying by 7: 7, 49, 343 ... He writes only the last digit each time: 7, 9, 3 ... What is the last digit when he has multiplied 8 sevens together? Type the digit.',
      check=lambda: (lambda d: d[7])([(lambda n: n)(0)] and [x for x in (lambda: (lambda seq: seq)(list(itertools.accumulate([7] * 8, lambda a, b: (a * b) % 10))))()])),
      hint='Keep multiplying the last digit by 7 and write down only the new last digit each time. Look for the list to start repeating.',
      steps=['The last digits are 7, 9, 3, 1, then 7, 9, 3, 1 again.', 'The pattern repeats every 4 sevens, so the 4th and the 8th last digits are both 1.', 'The last digit after 8 sevens is 1. (7 × 7 × ... eight times = 5 764 801.)'],
      src=['Ben keeps multiplying by 7: 7, 49, 343 … He writes only the last digit each time: 7, 9, 3 … What is the last digit when he has multiplied 8 sevens together? Explain the pattern.']),
    I(id='G6-why', tier='challenge', no='G6 why', type='selfcheck', open=True, skill='explaining a pattern',
      q='Explain the pattern of the last digits when Ben keeps multiplying by 7. Write your idea, then compare with the answer shown.',
      check=lambda: list(itertools.accumulate([7] * 12, lambda a, b: (a * b) % 10)),
      hint='Write the last digits one after another. When does the list start again?',
      steps=['The last digits go 7, 9, 3, 1 and then repeat: 7, 9, 3, 1, 7, 9, 3, 1.', 'Only the last digit matters, so each new last digit comes from the last one and 7: 7 × 7 = 49 gives 9, 9 × 7 = 63 gives 3, 3 × 7 = 21 gives 1, 1 × 7 = 7 gives 7 again.', 'The list repeats every 4, so the 4th and the 8th are both 1.'],
      src=['Ben keeps multiplying by 7: 7, 49, 343 … He writes only the last digit each time: 7, 9, 3 … What is the last digit when he has multiplied 8 sevens together? Explain the pattern.']),
    I(id='G7', tier='challenge', no='G7', type='number', skill='common multiples', answer=126,
      q='I am a 3-digit number less than 200. I can be divided exactly by 7 and by 9. My digits add up to 9. What number am I?',
      check=lambda: one([n for n in range(100, 200) if n in set(times(7, 30)) and n in set(times(9, 23)) and digit_sum(n) == 9]),
      hint='A number in both the 7 times table and the 9 times table is in the 63 times table. List those numbers up to 200 and add the digits of each.',
      steps=['Numbers in both the 7 and 9 times tables are 63, 126, 189 ...', 'The 3-digit ones less than 200 are 126 and 189.', '1 + 2 + 6 = 9 but 1 + 8 + 9 = 18, so the number is 126.'],
      src=['I am a 3-digit number less than 200. I can be divided exactly by 7 and by 9. My digits add up to 9. What number am I?']),
]


# ---------------------------------------------------------------- variant families (template + independent oracle over EVERY combination)
def _times_n(a, n):
    return sum([a] * n)


VARIANTS = {
    '3a': dict(
        base=dict(m=8),
        tpl=dict(vars=dict(m=[8, 6, 7, 9, 4, 3]), q='Mei does not know 7 × {m}. She splits 7 rows of {m} dots into 5 rows and 2 rows. Fill in the boxes.',
                 frame='5 × {m} = {f1}      2 × {m} = {f2}      so  7 × {m} = {f3}', answers=dict(f1='5*m', f2='2*m', f3='7*m'),
                 hint='Count the dots in each part. Each part is a fact you know. Then put the two parts together.',
                 steps=['5 rows of {m} make the first fact and 2 rows of {m} make the second.', 'Add the two parts to get 7 × {m}.', 'The answers are {ans}.']),
        oracle=lambda e: dict(f1=_times_n(e['m'], 5), f2=_times_n(e['m'], 2), f3=_times_n(e['m'], 5) + _times_n(e['m'], 2))),
    '2b': dict(
        base=dict(t=7, n=46),
        tpl=dict(vars=dict(t=[7, 6, 8, 9, 3, 4], n=[46, 23, 38, 57, 64, 82]), q='Without working out {t} × {n}, what is its last digit? Type the digit.', answer='t*n%10',
                 hint='Split {n} into tens and ones. Which part can change the last digit?',
                 steps=['The tens part gives a multiple of 10, so it ends in 0 and does not change the last digit.', 'Only the ones digit of {n} matters: multiply it by {t} and look at the last digit.', 'The last digit is {ans}.']),
        oracle=lambda e: int(str(_times_n(e['n'], e['t']))[-1])),
    'T2': dict(
        base=dict(a=8),
        tpl=dict(vars=dict(a=[8, 7, 6, 9, 3, 4, 2]), q='What is the last digit of {a} × {a} × {a}? Use last digits only.', answer='(a*a%10)*a%10',
                 hint='Work in two steps. First {a} × {a}: keep only its last digit. Then multiply that last digit by {a} and look at the last digit again.',
                 steps=['Find {a} × {a} and keep its last digit.', 'Multiply that last digit by {a} and keep the last digit.', 'The last digit is {ans}.']),
        oracle=lambda e: (lambda d: ((d * d) % 10 * d) % 10)(e['a'] % 10)),
    '1b-ans': dict(
        base=dict(n=8),
        tpl=dict(vars=dict(n=[8, 7, 6, 4, 9, 3, 5]), q='What is 9 × {n}? Use the pattern of the tens digits and the ones digits in the 9 times table.', answer='9*n',
                 hint='Look at the answers for 9 × {m} and 9 × {p} in your table. Where does 9 × {n} fit between them?',
                 derive=dict(m='n-1', p='n+1'),
                 steps=['The tens digit of 9 × {n} is 1 less than {n}.', 'The ones digit is what makes the digits add up to 9.', '9 × {n} = {ans}.']),
        oracle=lambda e: _times_n(9, e['n'])),
}
