"""Level 2 (P2) holiday lesson 5: MYSTERY NUMBER MACHINES (Working backwards), week 3, first lesson.  Online mirror of the printed workbook pages.

The questions are the ones printed in the Level 2 holiday workbook (p2/content/l5.js `workbook()` = Start here, p2/gaps.json lesson 5 `invest` = Investigation,
p2/content/l5.js `qbank.stretch` first four = Think harder 1 to 4, `qbank.challenge` last three = Go further 5 to 7, as built by p2/workbook_html.js, and the
"Make up your own" line).  Every answer is recomputed by an INDEPENDENT checker (the machine is run forwards, and the unknown is found by trying numbers until the
story comes out right; no "undo" rule is used by the checker); build_holiday.py stops if a checker and the printed answer differ.
Figures: the printed bar models (benBars, sitiBars, marbleBars, the bags of sweets, the two-bar story) redrawn for a phone, and number machines drawn as boxes.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from hlib import *          # noqa: E402,F401
from p2lib import *         # noqa: E402,F401

STRAND = 'Working backwards'
META = dict(level=2, lesson=5, key='p2', title='Mystery number machines', workbook_title='MYSTERY NUMBER MACHINES', topic='Working backwards', strand=STRAND,
            sources=['p2/content/l5.js', 'p2/gaps.json', 'p2/workbook_html.js'],
            intro=['IN is what goes into a machine. OUT is what comes out. To undo a step, do the opposite. Draw the machine or a bar on paper if it helps.',
                   'Type numbers with a comma between them when a question asks for a list. Some questions ask you to explain: write your idea in the box, then read the worked solution after you submit and compare.'])


# ---------------------------------------------------------------- independent checkers: run the machine FORWARDS and try numbers (no "undo" rule)
def run(steps, x):
    """Run a machine on x.  steps: [('*', 2), ('+', 7)] = multiply by 2, then add 7.  A division must come out whole, or the machine stops (None)."""
    for op, n in steps:
        if op == '+':
            x = x + n
        elif op == '-':
            x = x - n
        elif op == '*':
            x = x * n
        elif op == '/':
            if x % n:
                return None
            x = x // n
    return x


def find_in(steps, out, hi=3000):
    """The one number that goes IN to give `out`, found by trying 0, 1, 2 ... through the machine."""
    got = [x for x in range(0, hi) if run(steps, x) == out]
    if len(got) != 1:
        raise ValueError(f'{steps} {out}: {len(got)} answers {got[:5]}, expected exactly 1')
    return got[0]


def one(lst, what):
    if len(lst) != 1:
        raise ValueError(f'{what}: {len(lst)} answers, expected exactly 1')
    return lst[0]


def machine_rule(pairs, hi=30):
    """The machine 'multiply by m, then add a' that gives every (IN, OUT) pair, found by trying every m and a."""
    got = [(m, a) for m in range(1, hi) for a in range(0, 3 * hi) if all(i * m + a == o for i, o in pairs)]
    return one(got, 'machine rule')


M1A = machine_fig(['× 2', '+ 7'], '?', 27, 'A number machine: IN is a mystery number, then × 2, then + 7, and OUT is 27')
M1B = machine_fig(['− 8', '× 5'], '?', 40, 'A number machine: IN is a mystery number, then − 8, then × 5, and OUT is 40')
M1C = machine_fig(['÷ 3', '+ 12'], '?', 20, 'A number machine: IN is a mystery number, then ÷ 3, then + 12, and OUT is 20')
M1D = machine_fig(['× 4', '− 15'], '?', 21, 'A number machine: IN is a mystery number, then × 4, then − 15, and OUT is 21')
TABLE2A = grid_table([('IN', [4, 10, '', '']), ('OUT', ['', '', 17, 29])], caption='The table for the machine × 3, then + 2. IN: 4, 10, empty, empty. OUT: empty, empty, 17, 29.')
TABLE2B = grid_table([('IN', [3, 5, 10, 20]), ('OUT', ['', '', '', ''])], caption='The table for the machine × 2, then + 1. IN: 3, 5, 10, 20. OUT: four empty boxes.')
STICKER_BARS = bar_fig([dict(label='At first', segs=[(5.9, '?', 'w')]), dict(label='After\ngiving 24', segs=[(3.5, '?', 'w')]), dict(label='Now', segs=[(5.0, '50', 'a')])],
                       label_w=92, caption='Three bars: Siti at first (unknown), after giving 24 stickers away (unknown), and now (50 stickers). She gave 24 away, then got 15 more.')
BAGS = bags_fig()
TRICK = machine_fig(['+ 5', '× 2', '− 10', '÷ 2'], '?', '?', 'The magic trick: think of a number, add 5, double it (× 2), take away 10, halve it (÷ 2)')
T1_FIG = combine([machine_fig(['× ?', '+ ?'], '?', '?', 'A machine: IN, then multiply by a number, then add a number, OUT'),
                  grid_table([('IN', [2, 5]), ('OUT', [11, 20])], caption='IN 2 gives OUT 11. IN 5 gives OUT 20.')],
                 'A machine that multiplies by a number, then adds a number. IN 2 gives OUT 11 and IN 5 gives OUT 20.', gap=12)
T2_FIG = bar_fig([dict(label='At first', segs=[(1.43, '$15 book', 'h'), (2, 'left', 'a')], brace=(0, 3.43, '? at first', 'top')),
                  dict(label='After\nthe gift', segs=[(2, 'left', 'a'), (2, 'gift', 'b')], brace=(0, 4, '$42 now', 'bottom'))],
                 label_w=80, caption='Bars for Ben’s money: at first, a $15 book and the money left; after the gift, the money left and a gift of the same size, $42 in all')
T3_FIG = bar_fig([dict(label='At first', segs=[(2, 'half', 'a'), (2, 'half', 'w')], brace=(0, 4, '? beads', 'top')),
                  dict(label='Now', segs=[(2, 'half', 'a'), (1.33, '12', 'h')], brace=(0, 3.33, '30 beads', 'bottom'))],
                 label_w=60, caption='Bars for Siti’s beads: at first two halves; now one half and 12 more, 30 beads in all')
T4_FIG = bar_fig([dict(label='Ali', segs=[(3, '?', 'a')]), dict(label='Ben', segs=[(3, '?', 'a'), (0.9, '5', 'h')]), dict(label='Siti', segs=[(3, '?', 'a'), (1.4, '8', 'h')])],
                 label_w=50, right=64, vbrace=(0, 2, '40\nin all'), row_h=30, gap=12, caption='Three bars: Ben has 5 more than Ali, Siti has 8 more than Ali, 40 in all')

ITEMS = [
    # ================= Start here (workbook lesson 5, No.1 to No.5)
    dict(id='1a', tier='core', no='1(a)', type='number', skill='undoing a two-step machine', answer=10,
         q='A mystery machine. I multiply by 2, then add 7. I get 27. Find the number that went IN. Undo the LAST step first, then check forwards.', svg=M1A,
         check=lambda: find_in([('*', 2), ('+', 7)], 27),
         hint='The last step was + 7. What is the opposite of + 7? Do it to 27 first.',
         steps=['The last step was + 7, so undo it with − 7: 27 − 7 = 20.', 'The step before was × 2, so undo it with ÷ 2: 20 ÷ 2 = 10.', 'Check forwards: 10 × 2 = 20, then 20 + 7 = 27. The number that went IN is 10.'],
         src=['I multiply by 2, then add 7. I get 27.']),
    dict(id='1b', tier='core', no='1(b)', type='number', skill='undoing a two-step machine', answer=16,
         q='A mystery machine. I take away 8, then multiply by 5. I get 40. Find the number that went IN.', svg=M1B,
         check=lambda: find_in([('-', 8), ('*', 5)], 40),
         hint='The last step was × 5. What is the opposite of × 5? Do it to 40 first.',
         steps=['The last step was × 5, so undo it with ÷ 5: 40 ÷ 5 = 8.', 'The step before was − 8, so undo it with + 8: 8 + 8 = 16.', 'Check forwards: 16 − 8 = 8, then 8 × 5 = 40. The number that went IN is 16.'],
         src=['I take away 8, then multiply by 5. I get 40.']),
    dict(id='1c', tier='core', no='1(c)', type='number', skill='undoing a two-step machine', answer=24,
         q='A mystery machine. I divide by 3, then add 12. I get 20. Find the number that went IN.', svg=M1C,
         check=lambda: find_in([('/', 3), ('+', 12)], 20),
         hint='The last step was + 12. Undo it first. Then undo the ÷ 3.',
         steps=['The last step was + 12, so undo it with − 12: 20 − 12 = 8.', 'The step before was ÷ 3, so undo it with × 3: 8 × 3 = 24.', 'Check forwards: 24 ÷ 3 = 8, then 8 + 12 = 20. The number that went IN is 24.'],
         src=['I divide by 3, then add 12. I get 20.']),
    dict(id='1d', tier='core', no='1(d)', type='number', skill='undoing a two-step machine', answer=9,
         q='A mystery machine. I multiply by 4, then take away 15. I get 21. Find the number that went IN.', svg=M1D,
         check=lambda: find_in([('*', 4), ('-', 15)], 21),
         hint='The last step was − 15. Undo it first with its opposite. Then undo the × 4.',
         steps=['The last step was − 15, so undo it with + 15: 21 + 15 = 36.', 'The step before was × 4, so undo it with ÷ 4: 36 ÷ 4 = 9.', 'Check forwards: 9 × 4 = 36, then 36 − 15 = 21. The number that went IN is 9.'],
         src=['I multiply by 4, then take away 15. I get 21.']),

    dict(id='2a', tier='core', no='2(a)', type='fields', skill='machine tables, forwards and backwards', answer=[14, 32, 5, 9],
         q='This machine does × 3, then + 2. Fill in the table.', svg=TABLE2A,
         frame='IN 4 gives OUT {f1}. IN 10 gives OUT {f2}. OUT 17 came from IN {f3}. OUT 29 came from IN {f4}.',
         check=lambda: [run([('*', 3), ('+', 2)], 4), run([('*', 3), ('+', 2)], 10), find_in([('*', 3), ('+', 2)], 17), find_in([('*', 3), ('+', 2)], 29)],
         hint='For an IN number, run the machine forwards. For an OUT number, run it backwards: the last step is undone first.',
         steps=['Forwards, IN 4: 4 × 3 = 12, 12 + 2 = 14. IN 10: 10 × 3 = 30, 30 + 2 = 32.', 'Backwards, OUT 17: 17 − 2 = 15, 15 ÷ 3 = 5. OUT 29: 29 − 2 = 27, 27 ÷ 3 = 9.', 'The boxes are 14, 32, 5 and 9.'],
         src=['This machine does × 3, then + 2. Fill in the table.']),
    dict(id='2b', tier='core', no='2(b)', type='fields', skill='machine tables, forwards and backwards', answer=[7, 11, 21, 41],
         q='This machine does × 2, then + 1. Fill in the table for IN 3, 5, 10 and 20.', svg=TABLE2B,
         frame='OUT for IN 3: {f1}. IN 5: {f2}. IN 10: {f3}. IN 20: {f4}.',
         check=lambda: [run([('*', 2), ('+', 1)], x) for x in (3, 5, 10, 20)],
         hint='Do × 2 first, then + 1, for each IN number.',
         steps=['IN 3: 3 × 2 = 6, 6 + 1 = 7.   IN 5: 5 × 2 = 10, 10 + 1 = 11.', 'IN 10: 10 × 2 = 20, 20 + 1 = 21.   IN 20: 20 × 2 = 40, 40 + 1 = 41.', 'The boxes are 7, 11, 21 and 41.'],
         src=['This machine does × 2, then + 1. Fill in the table for IN 3, 5, 10 and 20.']),

    dict(id='3', tier='core', no='3', type='fields', skill='before-and-after bar model', answer=[35, 59],
         q='Siti had some stickers. She gave 24 stickers to her brother. Then her mother gave her 15 more. Now she has 50 stickers. Fill in the two ? bars, starting from what Siti has now.', svg=STICKER_BARS,
         frame='After giving 24: {f1} stickers. At first: {f2} stickers.',
         check=lambda: (lambda x: [x - 24, x])(one([x for x in range(0, 500) if x - 24 + 15 == 50], 'stickers at first')),
         hint='Start from what Siti has now. The last thing that happened was her mother giving her 15 more.',
         steps=['The last change was + 15, so before it Siti had 50 − 15 = 35 stickers. That is the middle bar.', 'The change before was − 24, so at first she had 35 + 24 = 59 stickers.', 'Check forwards: 59 − 24 = 35, then 35 + 15 = 50.'],
         src=['Siti had some stickers. She gave 24 stickers to her brother. Then her mother gave her 15 more. Now she has 50 stickers. How many stickers did Siti have at first?']),
    dict(id='4', tier='core', no='4', type='number', skill='bars of equal parts', answer=30,
         q='Ravi put all his sweets into 3 bags, with the same number in each bag. He took 4 sweets out of bag 3. Now bag 3 has 6 sweets. How many sweets did Ravi have altogether?', svg=BAGS,
         check=lambda: one([3 * b for b in range(1, 200) if b - 4 == 6], 'sweets altogether'),
         hint='The bags all had the same number at the start. Find how many were in bag 3 before Ravi took some out.',
         steps=['Bag 3 had 6 + 4 = 10 sweets before Ravi took 4 out.', 'All 3 bags have the same number, so each bag has 10 sweets.', '3 bags of 10 sweets: 10 + 10 + 10 = 30. Ravi had 30 sweets altogether.'],
         src=['Ravi put all his sweets into 3 bags, with the same number in each bag. He took 4 sweets out of bag 3. Now bag 3 has 6 sweets. How many sweets did Ravi have altogether?']),

    dict(id='5a', tier='core', no='5(a)', type='number', skill='the order of the steps matters', answer=18,
         q='Mei and Ali both put 5 into a machine. Mei’s machine does + 4, then × 2. What comes out?',
         check=lambda: run([('+', 4), ('*', 2)], 5),
         hint='Do the steps in the order Mei’s machine has them: + 4 first, then × 2.',
         steps=['Start with 5. Mei’s machine adds 4 first: 5 + 4 = 9.', 'Then it multiplies by 2: 9 × 2 = 18.', 'Mei’s machine gives 18.'],
         src=['Mei and Ali both put 5 into a machine.', 'Mei’s machine does + 4, then × 2. What comes out?']),
    dict(id='5b', tier='core', no='5(b)', type='number', skill='the order of the steps matters', answer=14,
         q='Mei and Ali both put 5 into a machine. Ali’s machine does × 2, then + 4. What comes out?',
         check=lambda: run([('*', 2), ('+', 4)], 5),
         hint='Do the steps in the order Ali’s machine has them: × 2 first, then + 4.',
         steps=['Start with 5. Ali’s machine multiplies by 2 first: 5 × 2 = 10.', 'Then it adds 4: 10 + 4 = 14.', 'Ali’s machine gives 14.'],
         src=['Ali’s machine does × 2, then + 4. What comes out?']),
    dict(id='5c', tier='core', no='5(c)', type='choice', options=['Yes', 'No'], answer='No', skill='the order of the steps matters',
         q='Mei’s machine does + 4, then × 2. Ali’s machine does × 2, then + 4. Do the two machines always give the same answer?',
         check=lambda: 'Yes' if all(run([('+', 4), ('*', 2)], x) == run([('*', 2), ('+', 4)], x) for x in range(0, 200)) else 'No',
         hint='Try one or two small IN numbers in both machines and compare what comes out.',
         steps=['Try IN 1. Mei: 1 + 4 = 5, 5 × 2 = 10. Ali: 1 × 2 = 2, 2 + 4 = 6.', '10 and 6 are not the same, so the two machines do not always give the same answer.', 'The order of the steps matters.'],
         src=['Do the two machines always give the same answer?']),
    dict(id='5d', tier='core', no='5(d)', type='number', skill='working backwards to match an OUT', answer=7,
         q='Mei puts 5 into her machine, which does + 4, then × 2. Ali’s machine does × 2, then + 4. What must Ali put IN to get the same OUT as Mei?',
         check=lambda: find_in([('*', 2), ('+', 4)], run([('+', 4), ('*', 2)], 5)),
         hint='First find what comes out of Mei’s machine. Then run Ali’s machine backwards from that OUT.',
         steps=['Mei’s OUT: 5 + 4 = 9, 9 × 2 = 18.', 'Ali’s machine must give 18. Undo + 4: 18 − 4 = 14. Undo × 2: 14 ÷ 2 = 7.', 'Check forwards: 7 × 2 = 14, then 14 + 4 = 18. Ali must put 7 IN.'],
         src=['What must Ali put IN to get the same OUT as Mei?']),

    # ================= Investigation: A magic trick
    dict(id='I1', tier='invest', no='Investigation (a)', label='Inv 1', type='fields', skill='a trick that undoes itself', answer=[3, 10],
         q='A magic trick. Think of a number. Add 5. Double it. Take away 10. Halve it. Do the trick with 3, then with 10. Write down each step on paper if you like.', svg=TRICK,
         frame='Start 3 gives {f1}. Start 10 gives {f2}.',
         check=lambda: [run([('+', 5), ('*', 2), ('-', 10), ('/', 2)], 3), run([('+', 5), ('*', 2), ('-', 10), ('/', 2)], 10)],
         hint='Do one step at a time and write the number you get after each step.',
         steps=['Start 3: 3 + 5 = 8, 8 × 2 = 16, 16 − 10 = 6, 6 ÷ 2 = 3.', 'Start 10: 10 + 5 = 15, 15 × 2 = 30, 30 − 10 = 20, 20 ÷ 2 = 10.', 'The final answers are 3 and 10.'],
         src=['Think of a number. Add 5. Double it. Take away 10. Halve it.', 'do the trick with 3, then with 10']),
    dict(id='I2', tier='invest', no='Investigation (a) more', label='Inv 2', type='fields', skill='a trick that undoes itself', answer=[7, 12, 40],
         q='Try the same trick (add 5, double it, take away 10, halve it) with three more starting numbers.', svg=TRICK,
         frame='Start 7 gives {f1}. Start 12 gives {f2}. Start 40 gives {f3}.',
         check=lambda: [run([('+', 5), ('*', 2), ('-', 10), ('/', 2)], x) for x in (7, 12, 40)],
         hint='Do the four steps for each starting number, one at a time.',
         steps=['Start 7: 7 + 5 = 12, 12 × 2 = 24, 24 − 10 = 14, 14 ÷ 2 = 7.', 'Start 12: 12 + 5 = 17, 17 × 2 = 34, 34 − 10 = 24, 24 ÷ 2 = 12.', 'Start 40: 40 + 5 = 45, 45 × 2 = 90, 90 − 10 = 80, 80 ÷ 2 = 40.'],
         src=['Try 5 different starting numbers.']),
    dict(id='I3', tier='invest', no='Investigation (a) notice', label='Inv 3', type='selfcheck', open=False, skill='a trick that undoes itself',
         q='You tried the trick with five different starting numbers. What do you notice about your final answers? Write your idea in the box.', svg=TRICK,
         facts=dict(final_equals_start_for_1_to_999=True),
         check=lambda: dict(final_equals_start_for_1_to_999=all(run([('+', 5), ('*', 2), ('-', 10), ('/', 2)], x) == x for x in range(1, 1000))),
         hint='Put each starting number next to its final answer. Look at the pairs.',
         steps=['Each final answer is the same as the number you started with: 3 gives 3, 10 gives 10, 7 gives 7.', 'Any idea that says the answer comes back to the start is a good one.'],
         src=['What do you notice about your final answer?']),
    dict(id='I4', tier='invest', no='Investigation (b)', label='Inv 4', type='fields', skill='testing a pattern with small and big numbers', answer=[1, 100],
         q='Is the trick ALWAYS the same? Try a small number and a big number. Add 5, double it, take away 10, halve it.', svg=TRICK,
         frame='Start 1 gives {f1}. Start 100 gives {f2}.',
         check=lambda: [run([('+', 5), ('*', 2), ('-', 10), ('/', 2)], 1), run([('+', 5), ('*', 2), ('-', 10), ('/', 2)], 100)],
         hint='Do the four steps for 1, then for 100. Write the number after each step.',
         steps=['Start 1: 1 + 5 = 6, 6 × 2 = 12, 12 − 10 = 2, 2 ÷ 2 = 1.', 'Start 100: 100 + 5 = 105, 105 × 2 = 210, 210 − 10 = 200, 200 ÷ 2 = 100.', 'The final answers are 1 and 100.'],
         src=['Try a big number and a small number']),
    dict(id='I5', tier='invest', no='Investigation (b) why', label='Inv 5', type='selfcheck', open=False, skill='explaining why a trick always works',
         q='Is it ALWAYS true? Say why. Write your idea in the box.', svg=TRICK,
         facts=dict(add_5_then_double_adds=10, take_away=10, then_halve_gives_start=True),
         check=lambda: dict(add_5_then_double_adds=run([('+', 5), ('*', 2)], 50) - run([('*', 2)], 50), take_away=10, then_halve_gives_start=all(run([('+', 5), ('*', 2), ('-', 10), ('/', 2)], x) == x for x in range(1, 1000))),
         hint='Think about what adding 5 and then doubling does to your number. Then think about what the last two steps do.',
         steps=['Adding 5 and then doubling gives double your number and 10 more (the 5 is doubled).', 'Taking away 10 takes off that extra 10, so you are back at double your number.', 'Halving gives your number again. Any idea like “double and halve undo each other, and the 5 doubled is 10 which I take away” is good.'],
         src=['Is it ALWAYS true? Try a big number and a small number, then say why.']),
    dict(id='I6', tier='invest', no='Investigation (c)', label='Inv 6', type='selfcheck', open=True, skill='making a trick that undoes itself', marking_mode='open',
         q='Make a number trick of your own, with at least 3 steps. Write the steps in the box, then test it on 3 numbers on paper.',
         hint='Choose some steps, like add, double, take away or halve. Test them on a small number. Compare your answer with the number you started with.',
         steps=['Many tricks are right. Example 1: add 3, double it, take away 6, halve it. Test with 4: 7, 14, 8, 4.', 'Example 2: times 4, add 8, divide by 4, take away 2. Test with 5: 20, 28, 7, 5.', 'Check yours: test three different starting numbers. Do you always get your starting number back?'],
         src=['Make your own trick that always gives you back the number you started with. Test it on 3 numbers.']),

    # ================= Think harder
    dict(id='T1a', tier='stretch', no='Think harder 1 (rule)', label='T1a', type='fields', skill='finding a machine from two pairs', answer=[3, 5],
         q='A machine multiplies by a number, then adds a number. IN 2 gives OUT 11 and IN 5 gives OUT 20. Find what the machine does.', svg=T1_FIG,
         frame='The machine does × {f1}, then + {f2}.',
         check=lambda: list(machine_rule([(2, 11), (5, 20)])),
         hint='Start with a small number to multiply by, with IN 2. What would you have to add to get 11? Then test your idea with IN 5.',
         steps=['Try × 2: 2 × 2 = 4, and 4 + 7 = 11. Test IN 5: 5 × 2 = 10, 10 + 7 = 17, not 20. So × 2 does not fit.', 'Try × 3: 2 × 3 = 6, and 6 + 5 = 11. Test IN 5: 5 × 3 = 15, 15 + 5 = 20. It fits.', 'The machine does × 3, then + 5.'],
         src=['A machine multiplies by a number, then adds a number. IN 2 gives OUT 11 and IN 5 gives OUT 20.', 'Find what the machine does']),
    dict(id='T1b', tier='stretch', no='Think harder 1 (IN 10)', label='T1b', type='number', skill='using a machine you found', answer=35,
         q='Look at the machine. What OUT does IN 10 give?', svg=T1_FIG,
         check=lambda: (lambda m, a: 10 * m + a)(*machine_rule([(2, 11), (5, 20)])),
         hint='Find what the machine does first, then run IN 10 through it.',
         steps=['The machine does × 3, then + 5.', 'IN 10: 10 × 3 = 30, then 30 + 5 = 35.', 'IN 10 gives OUT 35.'],
         src=['what OUT does IN 10 give?']),
    dict(id='T1c', tier='stretch', no='Think harder 1 (OUT 26)', label='T1c', type='number', skill='using a machine you found', answer=7,
         q='Look at the machine. Which IN gives OUT 26?', svg=T1_FIG,
         check=lambda: (lambda m, a: one([x for x in range(0, 200) if x * m + a == 26], 'IN for 26'))(*machine_rule([(2, 11), (5, 20)])),
         hint='Find what the machine does first. Then run it backwards from 26.',
         steps=['The machine does × 3, then + 5.', 'Undo + 5: 26 − 5 = 21. Undo × 3: 21 ÷ 3 = 7.', 'Check forwards: 7 × 3 = 21, 21 + 5 = 26. IN 7 gives OUT 26.'],
         src=['Which IN gives OUT 26?']),
    dict(id='T2', tier='stretch', no='Think harder 2', label='T2', type='number', skill='working backwards with bars', answer=36,
         q='Ben had some money. He spent $15 on a book. Then his dad gave him as much as he had left. Now he has $42. How much did Ben have at first?', svg=T2_FIG,
         check=lambda: one([x for x in range(0, 500) if (x - 15) * 2 == 42], 'Ben at first'),
         hint='Start from the end, $42. Look at the bar: what is the last bar made of?',
         steps=['After the gift Ben has $42. The gift was as much as he had left, so $42 is two equal parts: $21 and $21.', 'So after buying the book Ben had $21 left.', 'Before the book he had $21 + $15 = $36. Check forwards: 36 − 15 = 21, 21 + 21 = 42.'],
         src=['Ben had some money. He spent $15 on a book. Then his dad gave him as much as he had left. Now he has $42. How much did Ben have at first?']),
    dict(id='T3', tier='stretch', no='Think harder 3', label='T3', type='number', skill='working backwards with bars', answer=36,
         q='Siti had some beads. She gave half of them to Mei. Then she bought 12 more. Now she has 30 beads. How many beads did Siti have at first?', svg=T3_FIG,
         check=lambda: one([x for x in range(2, 500, 2) if (x - x // 2) + 12 == 30], 'Siti beads at first'),
         hint='Start from 30 and undo buying the 12 beads. What does the number you get stand for in the bars?',
         steps=['Undo buying 12 more: 30 − 12 = 18. That is the half Siti kept.', 'The half she gave Mei is the same size, 18.', 'At first she had 18 + 18 = 36 beads. Check forwards: half of 36 is 18, 18 + 12 = 30.'],
         src=['Siti had some beads. She gave half of them to Mei. Then she bought 12 more. Now she has 30 beads. How many beads did Siti have at first?']),
    dict(id='T4', tier='stretch', no='Think harder 4', label='T4', type='fields', skill='bars with equal and extra parts', answer=[9, 14, 17],
         q='Ali, Ben and Siti have 40 marbles altogether. Ben has 5 more marbles than Ali. Siti has 8 more marbles than Ali. How many marbles does each child have?', svg=T4_FIG,
         frame='Ali {f1}, Ben {f2}, Siti {f3}',
         check=lambda: (lambda a: [a, a + 5, a + 8])(one([a for a in range(0, 41) if a + (a + 5) + (a + 8) == 40], 'Ali marbles')),
         hint='Take the extra marbles away from the 40 first. Then the three bars are the same size.',
         steps=['Take away the extras: 40 − 5 − 8 = 27. Now the three children have the same number.', '27 ÷ 3 = 9, so Ali has 9 marbles.', 'Ben has 9 + 5 = 14 and Siti has 9 + 8 = 17. Check: 9 + 14 + 17 = 40.'],
         src=['Ali, Ben and Siti have 40 marbles altogether. Ben has 5 more marbles than Ali. Siti has 8 more marbles than Ali. How many marbles does each child have?']),

    # ================= Go further
    dict(id='C5', tier='challenge', no='Go further 5', label='G5', type='number', skill='working backwards with halves', answer=16,
         q='Siti had some sweets. She gave Ben 1 more than half of them. Now she has 7 sweets left. How many sweets did she have at first?',
         check=lambda: one([x for x in range(2, 500, 2) if x - (x // 2 + 1) == 7], 'Siti sweets at first'),
         hint='Draw all her sweets as a bar cut in half. Where do the 7 sweets that are left go in your bar?',
         steps=['Ben got half of the sweets and 1 more. So the 7 sweets Siti has left are one half, with 1 sweet missing.', 'One half is 7 + 1 = 8 sweets. The other half is also 8.', 'At first Siti had 8 + 8 = 16 sweets. Check forwards: half of 16 is 8, and Ben got 8 + 1 = 9, so 16 − 9 = 7.'],
         src=['Siti had some sweets. She gave Ben 1 more than half of them. Now she has 7 sweets left. How many sweets did she have at first?']),
    dict(id='C6', tier='challenge', no='Go further 6', label='G6', type='number', skill='running a machine backwards more than once', answer=3,
         q='A machine does × 2, then − 1. Mei puts a number through the machine 3 times in a row (each OUT goes back in). The final OUT is 17. What number did she start with?',
         check=lambda: one([x for x in range(0, 500) if run([('*', 2), ('-', 1)] * 3, x) == 17], 'start number'),
         hint='Run the machine backwards one time at a time. What number went in just before 17 came out?',
         steps=['Back once: 17 + 1 = 18, 18 ÷ 2 = 9.', 'Back again: 9 + 1 = 10, 10 ÷ 2 = 5. Back a third time: 5 + 1 = 6, 6 ÷ 2 = 3.', 'Check forwards: 3 → 5 → 9 → 17. Mei started with 3.'],
         src=['A machine does × 2, then − 1. Mei puts a number through the machine 3 times in a row (each OUT goes back in). The final OUT is 17. What number did she start with?']),
    dict(id='C7', tier='challenge', no='Go further 7', label='G7', type='fields', skill='working backwards with moves', answer=[15, 8, 7],
         q='Three boxes have 30 pens altogether. 5 pens move from box A to box B. Then 3 pens move from box B to box C. Now all three boxes have the same number. How many pens were in each box at first?',
         frame='Box A {f1}, box B {f2}, box C {f3}',
         check=lambda: one([[a, b, 30 - a - b] for a in range(0, 31) for b in range(0, 31 - a) if len({a - 5, b + 5 - 3, 30 - a - b + 3}) == 1], 'pens in A, B and C'),
         hint='How many pens are in each box now? Then undo the moves, starting with the last move.',
         steps=['In the end the three boxes have the same number: 30 ÷ 3 = 10 pens each.', 'Undo the last move (3 pens from B to C): box C had 10 − 3 = 7, box B had 10 + 3 = 13. Undo the first move (5 pens from A to B): box B had 13 − 5 = 8, box A had 10 + 5 = 15.', 'At first A had 15, B had 8 and C had 7. Check: 15 + 8 + 7 = 30.'],
         src=['Three boxes have 30 pens altogether. 5 pens are moved from box A to box B. Then 3 pens are moved from box B to box C. Now all three boxes have the same number of pens. How many pens were in each box at first?']),
    dict(id='M', tier='challenge', no='Make up your own', label='Make', type='selfcheck', open=True, skill='making puzzles', marking_mode='open',
         q='Make a before-and-after story that ends with 40. Can a partner work out the start?',
         hint='Choose what happens first (gives away or gets some), then what happens next. Work out the start by going backwards, then check forwards.',
         steps=['Many answers are right. Example: Ben had some stamps. He gave away 18, then he bought 13 more. Now he has 40.', 'Go backwards: 40 − 13 = 27, then 27 + 18 = 45. He had 45 stamps at first.', 'Check forwards: 45 − 18 = 27, 27 + 13 = 40.'],
         src=['a before-and-after story that ends with 40. Can a partner work out the start?']),
]
for _d in ITEMS:
    _d.setdefault('strand', STRAND)


# ---------------------------------------------------------------- variant families (template + independent oracle over EVERY combination)
VARIANTS = {
    '1a': dict(
        base=dict(m=2, a=7, x=10),
        tpl=dict(vars=dict(m=[2, 3, 4, 5], a=[3, 5, 6, 8, 9], x=[4, 5, 6, 7, 9, 12]), derive=dict(out='m*x+a', r1='m*x'),
                 q='A mystery machine. I multiply by {m}, then add {a}. I get {out}. What number went IN?',
                 answer='x', hint='The last step was + {a}. What is the opposite of + {a}? Do it to {out} first.',
                 steps=['Undo + {a}: {out} − {a} = {r1}.', 'Undo × {m}: {r1} ÷ {m} = {ans}.', 'Check forwards: {ans} × {m} = {r1}, then {r1} + {a} = {out}.']),
        oracle=lambda e: find_in([('*', e['m']), ('+', e['a'])], e['m'] * e['x'] + e['a'])),
    '1b': dict(
        base=dict(s=8, m=5, x=16),
        tpl=dict(vars=dict(s=[3, 5, 6, 8, 9], m=[2, 3, 4, 5], x=[10, 12, 15, 17, 20, 25]), derive=dict(r1='x-s', out='(x-s)*m'),
                 q='A mystery machine. I take away {s}, then multiply by {m}. I get {out}. What number went IN?',
                 answer='x', hint='The last step was × {m}. What is the opposite of × {m}? Do it to {out} first.',
                 steps=['Undo × {m}: {out} ÷ {m} = {r1}.', 'Undo − {s}: {r1} + {s} = {ans}.', 'Check forwards: {ans} − {s} = {r1}, then {r1} × {m} = {out}.']),
        oracle=lambda e: find_in([('-', e['s']), ('*', e['m'])], (e['x'] - e['s']) * e['m'])),
    '1c': dict(
        base=dict(d=3, a=12, q=8),
        tpl=dict(vars=dict(d=[2, 3, 4, 5], a=[4, 7, 9, 12], q=[3, 4, 5, 6, 8, 9]), derive=dict(out='q+a', x='d*q'),
                 q='A mystery machine. I divide by {d}, then add {a}. I get {out}. What number went IN?',
                 answer='d*q', hint='The last step was + {a}. Undo it first. Then undo the ÷ {d}.',
                 steps=['Undo + {a}: {out} − {a} = {q}.', 'Undo ÷ {d}: {q} × {d} = {ans}.', 'Check forwards: {ans} ÷ {d} = {q}, then {q} + {a} = {out}.']),
        oracle=lambda e: find_in([('/', e['d']), ('+', e['a'])], e['q'] + e['a'])),
    '4': dict(
        base=dict(t=4, l=6),
        tpl=dict(vars=dict(t=[2, 3, 4, 5, 6], l=[4, 5, 6, 7, 8, 9]), derive=dict(b='t+l'),
                 q='Ravi put all his sweets into 3 bags, with the same number in each bag. He took {t} sweets out of bag 3. Now bag 3 has {l} sweets. How many sweets did Ravi have altogether?',
                 answer='3*(t+l)', hint='The bags all had the same number at the start. How many were in bag 3 before Ravi took some out?',
                 steps=['Bag 3 had {l} + {t} = {b} sweets before Ravi took {t} out.', 'Each of the 3 bags has {b} sweets.', '3 bags of {b} sweets: {ans} sweets altogether.']),
        oracle=lambda e: one([3 * b for b in range(1, 300) if b - e['t'] == e['l']], 'sweets')),
    'T2': dict(
        base=dict(s=15, h=21),
        tpl=dict(vars=dict(s=[5, 8, 10, 12, 15, 20], h=[6, 8, 9, 10, 12, 15, 18]), derive=dict(t='2*h'),
                 q='Ben had some money. He spent ${s} on a book. Then his dad gave him as much as he had left. Now he has ${t}. How much did Ben have at first?',
                 answer='h+s', hint='Start from the end, ${t}. The last thing that happened was the gift: how big is each equal part?',
                 steps=['After the gift Ben has ${t}. The gift was as much as he had left, so ${t} is two equal parts of ${h}.', 'After buying the book Ben had ${h} left.', 'Before the book he had ${h} + ${s} = ${ans}.']),
        oracle=lambda e: one([x for x in range(0, 600) if (x - e['s']) * 2 == 2 * e['h']], 'Ben at first')),
}

for _d in ITEMS:
    if _d['type'] == 'selfcheck':
        _d.setdefault('marking_mode', 'self')

# ---- inquiry habit (docs/pedagogy/inquiry_skills_explicit.md; levels/habits.json)
ITEMS.insert(max(i for i, x in enumerate(ITEMS) if x['tier'] == 'core') + 1, habit_item('Check',
    'A machine doubles a number and then adds 3. IN 4 gives OUT 11. Work backwards from OUT 11. Then test a second case: IN 6 gives OUT 15. Does the same backwards method find the IN? Write what you did.',
    ['First case: 11 - 3 = 8, then 8 divided by 2 = 4. The IN is 4.', 'Second case: 15 - 3 = 12, then 12 divided by 2 = 6. The IN is 6.', 'It works both times: undo the steps in the opposite order, taking away 3 first and then halving.'],
    'Undo the last step first. The machine added 3 last, so what do you do first?'))
