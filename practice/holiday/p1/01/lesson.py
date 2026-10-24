"""Online practice for Level 1 (Primary 1, ages 6-8) holiday lesson 1: Whole Numbers: Number Patterns ("Count with the frog!").

The questions are the ones printed in the Level 1 holiday workbook (hp/workbook_html.js, lesson 1: Start here; hp/qbank.json lesson 1 stretch/challenge
for Think harder and Go further; hp/gaps.json lesson 1 for the Investigation).  Every answer is recomputed by an INDEPENDENT checker below
(loops over the numbers in the question, never a copy of the printed answer); build_holiday.py stops if a checker and the printed answer differ.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from hlib import *      # noqa: E402,F401

META = dict(level=1, lesson=1, key='p1', title='Count with the frog', workbook_title='COUNT WITH THE FROG!', topic='Whole Numbers: Number Patterns',
            strand='Whole numbers',
            sources=['hp/workbook_html.js', 'hp/qbank.json', 'hp/gaps.json'],
            intro=['There is no paper number strip on the screen. Use the number lines in the pictures, your fingers, or the number strip from the kit at the back of your workbook.',
                   'Some questions ask you to colour or draw. Do those on paper, then look at the picture of the answer on the screen.'])
SK = 'Whole numbers'

# ---------------------------------------------------------------- independent checkers (small, simple, loop-based)
def fill_gaps(seq, shown):
    """Numbers of `seq` that are not in `shown`, in order."""
    return [v for v in seq if v not in shown]


def next_two(seq):
    d = seq[1] - seq[0]
    assert all(b - a == d for a, b in zip(seq, seq[1:]))
    return [seq[-1] + d, seq[-1] + 2 * d]


def both(a, b):
    return [v for v in a if v in b]


def sticker_boxes(first, extra, n):
    out, v = [], first
    for _ in range(n):
        out.append(v); v += extra
    return out


def triangular_gaps(n):
    """1, 2, 4, 7, 11, 16 ... : each gap is 1 bigger than the one before."""
    seq, gap = [1], 1
    while len(seq) < n:
        seq.append(seq[-1] + gap); gap += 1
    return seq


F4 = count_up_to(4, 20)          # frog 1 lands on 4, 8, ... up to 20
F5 = count_up_to(5, 20)          # frog 2 lands on 5, 10, ...

ITEMS = [
    # ================= Start here (workbook lesson 1, No.1 to No.5)
    dict(id='1a', tier='core', no='1(a)', type='fields', skill='skip counting',
         q='Skip counting. Fill in the blanks.', frame='Counting in 2s:  2, 4, 6, {f1}, {f2}, 12, {f3}, 16', answer=[8, 10, 14],
         check=lambda: fill_gaps(count_up_to(2, 16), {2, 4, 6, 12, 16}),
         hint='Each number is 2 more than the one before. After 6 comes 6 + 2.',
         steps=['Counting in 2s means adding 2 each time.', '6 + 2 = 8, and 8 + 2 = 10. So the first two boxes are 8 and 10.', '12 + 2 = 14. The last box is 14.', 'The line reads 2, 4, 6, 8, 10, 12, 14, 16.'],
         src=['Skip counting. Fill in the blanks.', 'Counting in 2s:   2,  4,  6,  ____,  ____,  12,  ____,  16']),
    dict(id='1b', tier='core', no='1(b)', type='fields', skill='skip counting',
         q='Skip counting. Fill in the blanks.', frame='Counting in 5s:  5, 10, {f1}, 20, {f2}, 30, {f3}', answer=[15, 25, 35],
         check=lambda: fill_gaps(count_up_to(5, 35), {5, 10, 20, 30}),
         hint='Each number is 5 more than the one before. Numbers in the 5s end in 5 or 0.',
         steps=['Counting in 5s means adding 5 each time.', '10 + 5 = 15, so the first box is 15.', '20 + 5 = 25 and 30 + 5 = 35.', 'The line reads 5, 10, 15, 20, 25, 30, 35.'],
         src=['Counting in 5s:   5,  10,  ____,  20,  ____,  30,  ____']),
    dict(id='1c', tier='core', no='1(c)', type='fields', skill='skip counting',
         q='Skip counting. Fill in the blanks.', frame='Counting in 3s:  3, 6, {f1}, 12, {f2}, 18', answer=[9, 15],
         check=lambda: fill_gaps(count_up_to(3, 18), {3, 6, 12, 18}),
         hint='Each number is 3 more than the one before. Put a counter on 6 and hop 3 steps.',
         steps=['Counting in 3s means adding 3 each time.', '6 + 3 = 9, so the first box is 9.', '12 + 3 = 15, so the second box is 15.', 'The line reads 3, 6, 9, 12, 15, 18.'],
         src=['Counting in 3s:   3,  6,  ____,  12,  ____,  18']),

    dict(id='2a-next', tier='core', no='2(a)', type='fields', skill='rule of a pattern',
         q='What is the rule? Fill in the rule and the next two numbers. First the next two numbers.', frame='4, 7, 10, 13, {f1}, {f2}', answer=[16, 19],
         check=lambda: next_two([4, 7, 10, 13]),
         hint='Look at how much the number grows each time: from 4 to 7 is how many steps?',
         steps=['From 4 to 7 the number grows by 3. From 7 to 10 and from 10 to 13 it grows by 3 again.', '13 + 3 = 16 and 16 + 3 = 19.', 'The next two numbers are 16 and 19.'],
         src=['What is the rule? Fill in the rule and the next two numbers.', '4,  7,  10,  13,  ____,  ____        Rule: ______________']),
    dict(id='2a-rule', tier='core', no='2(a) rule', type='selfcheck', open=False, skill='rule of a pattern', facts=('add', 3),
         q='What is the rule for 4, 7, 10, 13 ... ? Write it in words, like "add 2" or "take away 5". Compare with the answer after you submit.',
         check=lambda: rule_of([4, 7, 10, 13]),
         hint='The numbers go up. By how many steps does each number grow?',
         steps=['The numbers go up by the same amount each time: 4, 7, 10, 13.', 'Each number is 3 more than the one before.', 'The rule is add 3.'],
         src=['4,  7,  10,  13,  ____,  ____        Rule: ______________']),
    dict(id='2b-next', tier='core', no='2(b)', type='fields', skill='rule of a pattern',
         q='What is the rule? Fill in the rule and the next two numbers. First the next two numbers.', frame='30, 27, 24, 21, {f1}, {f2}', answer=[18, 15],
         check=lambda: next_two([30, 27, 24, 21]),
         hint='The numbers are going down. How much do they go down each time?',
         steps=['From 30 to 27 the number goes down by 3. It goes down by 3 each time.', '21 - 3 = 18 and 18 - 3 = 15.', 'The next two numbers are 18 and 15.'],
         src=['30,  27,  24,  21,  ____,  ____       Rule: ______________']),
    dict(id='2b-rule', tier='core', no='2(b) rule', type='selfcheck', open=False, skill='rule of a pattern', facts=('take away', 3),
         q='What is the rule for 30, 27, 24, 21 ... ? Write it in words, like "add 2" or "take away 5". Compare with the answer after you submit.',
         check=lambda: rule_of([30, 27, 24, 21]),
         hint='The numbers go down. By how many steps does each number get smaller?',
         steps=['The numbers get smaller by the same amount each time: 30, 27, 24, 21.', 'Each number is 3 less than the one before.', 'The rule is take away 3.'],
         src=['30,  27,  24,  21,  ____,  ____       Rule: ______________']),
    dict(id='2c-next', tier='core', no='2(c)', type='fields', skill='rule of a pattern',
         q='What is the rule? Fill in the rule and the next two numbers. First the next two numbers.', frame='2, 6, 10, 14, {f1}, {f2}', answer=[18, 22],
         check=lambda: next_two([2, 6, 10, 14]),
         hint='From 2 to 6 is 4 steps. Does it grow by 4 each time?',
         steps=['From 2 to 6 the number grows by 4, and from 6 to 10, and from 10 to 14.', '14 + 4 = 18 and 18 + 4 = 22.', 'The next two numbers are 18 and 22.'],
         src=['2,  6,  10,  14,  ____,  ____        Rule: ______________']),
    dict(id='2c-rule', tier='core', no='2(c) rule', type='selfcheck', open=False, skill='rule of a pattern', facts=('add', 4),
         q='What is the rule for 2, 6, 10, 14 ... ? Write it in words, like "add 2" or "take away 5". Compare with the answer after you submit.',
         check=lambda: rule_of([2, 6, 10, 14]),
         hint='The numbers go up. By how many steps does each number grow?',
         steps=['The numbers grow by the same amount each time: 2, 6, 10, 14.', 'Each number is 4 more than the one before.', 'The rule is add 4.'],
         src=['2,  6,  10,  14,  ____,  ____        Rule: ______________']),

    dict(id='3', tier='core', no='3', type='selfcheck', paper=True, skill='skip counting on a number line',
         q='A frog starts at 0 and hops 4 steps each time. Circle or colour the numbers where the frog lands. The first hop is drawn for you.',
         svg=number_line(0, 20, hops=[(0, 4)], caption='Frog 1: hops of 4'), facts=F4, check=lambda: count_up_to(4, 20),
         sol_fig=lambda f: number_line(0, 20, hops=list(zip([0] + f[:-1], f)), circled=f, caption='Frog 1 lands on ' + ', '.join(map(str, f))),
         hint='The first hop goes from 0 to 4. Hop 4 more from 4. Where do you land?',
         steps=['The frog hops 4 steps each time, so it lands on 4, 8, 12, 16 and 20.', 'Count the hops: 0 to 4, 4 to 8, 8 to 12, 12 to 16, 16 to 20.', 'These are the numbers in the counting pattern of 4s.'],
         src=['A frog starts at 0 and hops 4 steps each time. Circle or colour the numbers where the frog lands. The first hop is drawn for you.']),
    dict(id='3a', tier='core', no='3(a)', type='selfcheck', paper=True, skill='skip counting on a number line',
         q='A second frog also starts at 0 but hops 5 steps each time. Mark its landing numbers with a cross (X) on the second number line.',
         svg=number_line(0, 20, caption='Frog 2: hops of 5'), facts=F5, check=lambda: count_up_to(5, 20),
         sol_fig=lambda f: number_line(0, 20, hops=list(zip([0] + f[:-1], f)), crosses=f, caption='Frog 2 lands on ' + ', '.join(map(str, f))),
         hint='Hop 5 steps from 0. Then 5 more. Put an X above each place it lands.',
         steps=['The frog hops 5 steps each time, so it lands on 5, 10, 15 and 20.', 'Put a cross above 5, 10, 15 and 20.', 'These are the numbers in the counting pattern of 5s.'],
         src=['A second frog also starts at 0 but hops 5 steps each time. Mark its landing numbers with a cross (X) on the second number line.']),
    dict(id='3b', tier='core', no='3(b)', type='number', skill='common numbers in two patterns', answer=20,
         q='Besides 0, which number do BOTH frogs land on? (The frog that hops 4 and the frog that hops 5, up to 20.)',
         svg=number_line(0, 20, caption='A number line from 0 to 20'),
         check=lambda: (lambda c: c[0] if len(c) == 1 else None)(both(count_up_to(4, 20), count_up_to(5, 20))),
         hint='Write the 4s landings and the 5s landings. Which number is in both lists?',
         steps=['Frog 1 lands on 4, 8, 12, 16, 20.', 'Frog 2 lands on 5, 10, 15, 20.', 'Only 20 is in both lists.'],
         src=['Besides 0, which number do BOTH frogs land on?']),

    dict(id='4-ali', tier='core', no='4 (Ali)', type='selfcheck', open=False, skill='skip counting', facts=count_up_to(2, 30),
         q="Ali counts in 2s from 2 up to 30. Mei counts in 5s from 5 up to 30. On paper, write Ali's list. Compare with the answer after you submit.",
         check=lambda: ap(2, 2, 15),
         hint='Start at 2 and keep adding 2 until you get to 30. How many numbers is that?',
         steps=['Ali adds 2 each time: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30.', 'He says 15 numbers.'],
         src=['Ali counts in 2s from 2 up to 30. Mei counts in 5s from 5 up to 30. Write both lists first.']),
    dict(id='4-mei', tier='core', no='4 (Mei)', type='selfcheck', open=False, skill='skip counting', facts=count_up_to(5, 30),
         q="Ali counts in 2s from 2 up to 30. Mei counts in 5s from 5 up to 30. On paper, write Mei's list. Compare with the answer after you submit.",
         check=lambda: ap(5, 5, 6),
         hint='Start at 5 and keep adding 5 until you get to 30.',
         steps=['Mei adds 5 each time: 5, 10, 15, 20, 25, 30.', 'She says 6 numbers.'],
         src=['Ali counts in 2s from 2 up to 30. Mei counts in 5s from 5 up to 30. Write both lists first.']),
    dict(id='4a', tier='core', no='4(a)', type='set', ordered=False, skill='common numbers in two patterns', answer=[10, 20, 30],
         q='Ali counts in 2s from 2 up to 30. Mei counts in 5s from 5 up to 30. Which numbers will BOTH of them say? Type them with a comma between.',
         check=lambda: both(ap(2, 2, 15), ap(5, 5, 6)),
         hint='Put your two lists next to each other. Which numbers are in both?',
         steps=['Ali: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30.', 'Mei: 5, 10, 15, 20, 25, 30.', 'Both say 10, 20 and 30.'],
         src=['Which numbers will BOTH of them say?']),
    dict(id='4b', tier='core', no='4(b)', type='selfcheck', open=True, skill='noticing patterns',
         q='What do you notice about these numbers? (The numbers that both Ali and Mei say.)',
         facts=dict(end_in=0, gap=10), check=lambda: (lambda c: dict(end_in=c[0] % 10 if len({v % 10 for v in c}) == 1 else None, gap=c[1] - c[0] if len({b - a for a, b in zip(c, c[1:])}) == 1 else None))(both(ap(2, 2, 15), ap(5, 5, 6))),
         hint='Look at the last digit of each number. Look at how far apart they are.',
         steps=['The numbers are 10, 20 and 30.', 'Every one of them ends in 0.', 'They are 10 apart: each is 10 more than the one before. They are the counting pattern of 10s.', 'Any answer like this is good. You could also say they are all even numbers.'],
         src=['What do you notice about these numbers?']),

    dict(id='5', tier='core', no='5', type='fields', skill='growing patterns', answer=[8, 11, 14, 17, 20, 23, 26, 29],
         q='Mei puts stickers in boxes. Box 1 has 2 stickers. Each box after it has 3 more stickers than the box before. Fill in the table. How many stickers are in Box 10?',
         frame='Box 1: 2,  Box 2: 5,  Box 3: {f1},  Box 4: {f2},  Box 5: {f3},  Box 6: {f4},  Box 7: {f5},  Box 8: {f6},  Box 9: {f7},  Box 10: {f8}',
         svg=dot_boxes([2, 5, None, None], caption='Boxes of stickers: Box 1 has 2, Box 2 has 5, boxes 3 and 4 are empty'),
         check=lambda: sticker_boxes(2, 3, 10)[2:],
         hint='Add 3 to the number in the box before. Box 3 is 5 + 3.',
         steps=['Each box has 3 more than the one before.', '5 + 3 = 8, 8 + 3 = 11, 11 + 3 = 14, 14 + 3 = 17.', '17 + 3 = 20, 20 + 3 = 23, 23 + 3 = 26, 26 + 3 = 29.', 'Box 10 has 29 stickers.'],
         src=['Mei puts stickers in boxes. Box 1 has 2 stickers. Each box after it has 3 more stickers than the box before.', 'Fill in the table. How many stickers are in Box 10?']),
    dict(id='5b', tier='core', no='5(b)', type='selfcheck', open=True, skill='noticing patterns',
         q='Look at the numbers of stickers. Are they odd or even? What pattern do you see?',
         facts=dict(parity='even, odd, even, odd'), check=lambda: dict(parity=', '.join('even' if v % 2 == 0 else 'odd' for v in sticker_boxes(2, 3, 4))),
         hint='Look at the first few numbers: 2, 5, 8, 11. Is each one odd or even?',
         steps=['The numbers are 2, 5, 8, 11, 14, 17, 20, 23, 26, 29.', 'They are not all odd and not all even. They go even, odd, even, odd, and so on, taking turns.', 'Why? Each number is 3 more than the one before, and adding 3 turns an even number into an odd number and an odd number into an even number.', 'Any true pattern you saw is a good answer.'],
         src=['Look at the numbers of stickers. Are they odd or even? What pattern do you see?']),

    # ================= Investigation (end of the Start here pages)
    dict(id='I1', tier='invest', no='Investigation 1', type='set', ordered=False, skill='common numbers in two patterns', answer=[6, 12, 18, 24, 30],
         q='Investigation: What if we change the hops? Frog 1 hops in 2s from 0. Frog 2 hops in 3s from 0. Which numbers up to 30 do BOTH frogs land on? (Not 0, where they start.) Type them with a comma between.',
         check=lambda: both(count_up_to(2, 30), count_up_to(3, 30)),
         hint='Write the 2s: 2, 4, 6 ... and the 3s: 3, 6, 9 ... up to 30. Which numbers are in both lists?',
         steps=['Frog 1 lands on 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30.', 'Frog 2 lands on 3, 6, 9, 12, 15, 18, 21, 24, 27, 30.', 'Both land on 6, 12, 18, 24 and 30.'],
         src=['Frog 1 hops in 2s from 0. Frog 2 hops in 3s from 0. Write the numbers up to 30 that BOTH frogs land on.', 'What if we change the hops?']),
    dict(id='I2', tier='invest', no='Investigation 2', type='selfcheck', open=False, skill='noticing patterns',
         q='Then: Now change frog 2 to hops of 4, then 5, then 6, and do it again each time. What stays the same? What changes?',
         facts={4: [4, 8, 12, 16, 20, 24, 28], 5: [10, 20, 30], 6: [6, 12, 18, 24, 30]},
         check=lambda: {d: both(count_up_to(2, 30), count_up_to(d, 30)) for d in (4, 5, 6)},
         hint='Do it one at a time: frog 1 in 2s with frog 2 in 4s, then 5s, then 6s. Write the shared numbers each time.',
         steps=['With frog 2 in 4s: both land on 4, 8, 12, 16, 20, 24 and 28. That is every landing of frog 2, because 4 is two 2s.',
                'With frog 2 in 5s: both land on 10, 20 and 30.', 'With frog 2 in 6s: both land on 6, 12, 18, 24 and 30.',
                'What stays the same: 0 is always shared, and the shared numbers always go up by the same jump each time.',
                'What changes: the size of that jump (4, 10 and 6) and how many numbers are shared.',
                'Any careful noticing is good. A strong answer writes both lists each time and says why the 4s frog shares every landing.'],
         src=['Now change frog 2 to hops of 4, then 5, then 6, and do it again each time. What stays the same? What changes?']),

    # ================= Think harder
    dict(id='T1', tier='stretch', no='T1', type='fields', skill='missing numbers in a pattern', answer=[13, 23],
         q='Fill in the missing numbers.', frame='3, 8, {f1}, 18, {f2}, 28',
         check=lambda: fill_gaps(ap(3, 5, 6), {3, 8, 18, 28}),
         hint='Look at how far it is from 3 to 8. Does the pattern keep that jump?',
         steps=['From 3 to 8 the number grows by 5. The pattern adds 5 each time.', '8 + 5 = 13, so the first missing number is 13.', '18 + 5 = 23, so the second missing number is 23.', 'Check: 23 + 5 = 28.'],
         src=['Fill in the missing numbers: 3, 8, __, 18, __, 28']),
    dict(id='T2', tier='stretch', no='T2', type='fields', skill='missing numbers in a pattern', answer=[34, 22],
         q='Fill in the missing numbers.', frame='40, {f1}, 28, {f2}, 16, 10',
         check=lambda: fill_gaps(ap(40, -6, 6), {40, 28, 16, 10}),
         hint='Use the two numbers next to each other, 16 and 10. How far apart are they?',
         steps=['The two neighbours 16 and 10 are 6 apart, so the pattern takes away 6 each time.', '40 - 6 = 34, so the first missing number is 34.', '28 - 6 = 22, so the second missing number is 22.', 'Check: 34 - 6 = 28 and 22 - 6 = 16.'],
         src=['Fill in the missing numbers: 40, __, 28, __, 16, 10']),
    dict(id='T3a', tier='stretch', no='T3(a)', type='choice', skill='does it belong to the pattern', options=['Yes', 'No'], answer='No',
         q='Is 30 in the pattern 4, 8, 12, 16 ... ?', check=lambda: 'Yes' if 30 in ap(4, 4, 20) else 'No',
         hint='Keep counting in 4s: 4, 8, 12, 16 ... Do you land on 30?',
         steps=['The pattern adds 4 each time: 4, 8, 12, 16, 20, 24, 28, 32.', 'It goes from 28 to 32, so it does not land on 30.', 'No, 30 is not in the pattern.'],
         src=['Is 30 in the pattern 4, 8, 12, 16 … ? How do you know?']),
    dict(id='T3b', tier='stretch', no='T3(b)', type='selfcheck', open=False, skill='does it belong to the pattern',
         q='Is 30 in the pattern 4, 8, 12, 16 ... ? How do you know?', facts=[28, 32],
         check=lambda: (lambda s: [max(v for v in s if v < 30), min(v for v in s if v > 30)])(ap(4, 4, 20)),
         hint='Write the pattern until you pass 30. Which two numbers is 30 between?',
         steps=['The pattern goes 28, 32. It skips 30.', 'Another way: every number in the 4s pattern is in the 4 times table, and 30 is not (4 x 7 = 28 and 4 x 8 = 32).', 'Any reason that shows 30 is jumped over is good.'],
         src=['Is 30 in the pattern 4, 8, 12, 16 … ? How do you know?']),
    dict(id='T4a', tier='stretch', no='T4(a)', type='set', ordered=False, skill='common numbers in two patterns', answer=[10, 20, 30, 40, 50],
         q='Ali counts in 2s from 2 up to 50. Mei counts in 5s from 5 up to 50. Which numbers do both of them say? Type them with a comma between.',
         check=lambda: both(count_up_to(2, 50), count_up_to(5, 50)),
         hint='Mei says fewer numbers, so write Mei\'s list first: 5, 10, 15 ... Then ask which of them Ali also says (they are even).',
         steps=['Mei says 5, 10, 15, 20, 25, 30, 35, 40, 45, 50.', 'Ali says only even numbers, so Mei\'s odd numbers (5, 15, 25, 35, 45) are not in his list.', 'Both say 10, 20, 30, 40 and 50.'],
         src=['Ali counts in 2s from 2 up to 50. Mei counts in 5s from 5 up to 50. Which numbers do both of them say? What do you notice?']),
    dict(id='T4b', tier='stretch', no='T4(b)', type='selfcheck', open=False, skill='noticing patterns',
         q='What do you notice about the numbers that both of them say?', facts=dict(end_in=0, gap=10),
         check=lambda: (lambda c: dict(end_in=c[0] % 10 if len({v % 10 for v in c}) == 1 else None, gap=c[1] - c[0]))(both(count_up_to(2, 50), count_up_to(5, 50))),
         hint='Look at the last digit of 10, 20, 30, 40, 50.',
         steps=['The numbers are 10, 20, 30, 40 and 50.', 'They all end in 0, and each is 10 more than the one before.', 'They are the counting pattern of 10s. Any true noticing is a good answer.'],
         src=['Which numbers do both of them say? What do you notice?']),

    # ================= Go further
    dict(id='C1a', tier='challenge', no='C1(a)', type='number', skill='growing patterns', answer=29,
         q='1, 2, 4, 7, 11, 16 ... What is the 8th number?', check=lambda: triangular_gaps(8)[-1],
         hint='Write the gaps between the numbers: 1, 2, 3, ... What do you notice about the gaps?',
         steps=['The gaps are 1, 2, 3, 4, 5. Each gap is 1 bigger than the one before.', 'The next gaps are 6 and 7.', '16 + 6 = 22 is the 7th number, and 22 + 7 = 29 is the 8th number.'],
         src=['1, 2, 4, 7, 11, 16 … What is the 8th number? Explain how the pattern grows.']),
    dict(id='C1b', tier='challenge', no='C1(b)', type='selfcheck', open=False, skill='growing patterns',
         q='1, 2, 4, 7, 11, 16 ... Explain how the pattern grows.', facts=[1, 2, 3, 4, 5, 6, 7],
         check=lambda: (lambda s: [b - a for a, b in zip(s, s[1:])])(triangular_gaps(8)),
         hint='Look at how much you add to get from each number to the next one.',
         steps=['Look at what is added each time: +1, +2, +3, +4, +5, then +6 and +7.', 'The number you add goes up by 1 each time, so the pattern grows faster and faster.', 'Any explanation that says the gaps get bigger by 1 is good.'],
         src=['1, 2, 4, 7, 11, 16 … What is the 8th number? Explain how the pattern grows.']),
    dict(id='C2a', tier='challenge', no='C2(a)', type='set', ordered=False, skill='common numbers in two patterns', answer=[5, 17, 29, 41],
         q='Ali counts up from 2 in 3s. Mei counts up from 1 in 4s. Which numbers up to 50 are in both patterns? Type them with a comma between.',
         check=lambda: both(count_up_to(3, 50, start=2), count_up_to(4, 50, start=1)),
         hint='Write both patterns up to 50. Ali: 2, 5, 8 ... Mei: 1, 5, 9 ... Which numbers match?',
         steps=['Ali: 2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50.', 'Mei: 1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49.', 'Both patterns have 5, 17, 29 and 41.'],
         src=['Ali counts up from 2 in 3s. Mei counts up from 1 in 4s. Which numbers up to 50 are in both patterns?']),
    dict(id='C2b', tier='challenge', no='C2(b)', type='selfcheck', open=False, skill='noticing patterns',
         q='What do you notice about the gaps between the numbers that are in both patterns?', facts=12,
         check=lambda: (lambda c: c[1] - c[0] if len({b - a for a, b in zip(c, c[1:])}) == 1 else None)(both(count_up_to(3, 50, start=2), count_up_to(4, 50, start=1))),
         hint='Work out how far it is from 5 to 17, from 17 to 29, and from 29 to 41.',
         steps=['5, 17, 29, 41: each one is 12 more than the one before.', 'The gaps are all the same, 12. The shared numbers make a new counting pattern of their own.', 'Why 12? Ali jumps 3 and Mei jumps 4, and 12 is the first number in both the 3s and the 4s.'],
         src=['Which numbers up to 50 are in both patterns? What do you notice about the gaps between them?']),
    dict(id='C3', tier='challenge', no='C3', type='selfcheck', open=False, skill='making patterns',
         q='Make up two counting patterns: choose a start and a jump for each, so that they share some numbers up to 50. Ring the shared numbers on paper. What do you notice about the gaps between them?',
         facts=dict(shared=[6, 18, 30, 42], gap=12),
         check=lambda: (lambda c: dict(shared=c, gap=c[1] - c[0]))(both(count_up_to(4, 50, start=2), count_up_to(3, 50, start=3))),
         hint='Pick two small jumps such as 3 and 4. Write each pattern up to 50 and look for numbers in both.',
         steps=['Many answers are right. Here is one example.', 'Pattern 1: start at 2 and add 4: 2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50.', 'Pattern 2: start at 3 and add 3: 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48.',
                'They share 6, 18, 30 and 42. The gaps between the shared numbers are all 12.', 'Check yours: write both lists, ring the matches, then see whether the gaps between the ringed numbers are all the same.'],
         src=['Make up your own two counting patterns: choose a start and a jump for each, so that they share some numbers up to 50. Write both patterns and ring the shared numbers.']),
]

# ---------------------------------------------------------------- variant families (template + independent oracle over EVERY combination)
def _count(start, step, n):
    out, v = [], start
    for _ in range(n):
        out.append(v); v += step
    return out


VARIANTS = {
    '1a': dict(
        base=dict(d=2),
        tpl=dict(vars=dict(d=[2, 3, 4, 5, 10]), q='Skip counting. Fill in the blanks.',
                 frame='Counting in {d}s:  {a}, {b}, {c}, {f1}, {f2}, {e}, {f3}, {g}', answers=dict(f1='4*d', f2='5*d', f3='7*d'),
                 derive=dict(a='d', b='2*d', c='3*d', e='6*d', g='8*d'),
                 hint='Each number is {d} more than the one before.',
                 steps=['Counting in {d}s means adding {d} each time.', 'After {c} comes {c} + {d}. Keep adding {d}.', 'The line reads {a}, {b}, {c}, then the boxes, then {e}, then the box, then {g}. The answers are {ans}.']),
        oracle=lambda e: (lambda l: dict(f1=l[3], f2=l[4], f3=l[6]))(_count(e['d'], e['d'], 8))),
    'T1': dict(
        base=dict(a=3, d=5),
        tpl=dict(vars=dict(a=[1, 2, 3, 4, 5, 6, 7, 8, 9], d=[2, 3, 4, 5, 6, 7]), q='Fill in the missing numbers.',
                 frame='{a}, {b}, {f1}, {c}, {f2}, {e}', answers=dict(f1='a+2*d', f2='a+4*d'),
                 derive=dict(b='a+d', c='a+3*d', e='a+5*d'),
                 hint='Look at how far it is from {a} to {b}. Does the pattern keep that jump?',
                 steps=['From {a} to {b} the number grows by {d}. The pattern adds {d} each time.', '{b} + {d} is the first missing number, and {c} + {d} is the second.', 'The missing numbers are {ans}.']),
        oracle=lambda e: (lambda l: dict(f1=l[2], f2=l[4]))(_count(e['a'], e['d'], 6))),
    '2a-next': dict(
        base=dict(a=4, d=3),
        tpl=dict(vars=dict(a=[1, 2, 3, 4, 5, 6, 7, 8, 9], d=[2, 3, 4, 5, 6]), q='What is the rule? Find the next two numbers.',
                 frame='{a}, {b}, {c}, {e}, {f1}, {f2}', answers=dict(f1='a+4*d', f2='a+5*d'), derive=dict(b='a+d', c='a+2*d', e='a+3*d'),
                 hint='Look at how much the number grows from {a} to {b}.',
                 steps=['From {a} to {b} the number grows by {d}, and it keeps growing by {d}.', '{e} + {d} is the next number, and then add {d} again.', 'The next two numbers are {ans}.']),
        oracle=lambda e: (lambda l: dict(f1=l[4], f2=l[5]))(_count(e['a'], e['d'], 6))),
}

# ---- inquiry habit (docs/pedagogy/inquiry_skills_explicit.md; levels/habits.json)
habit_tag(ITEMS, 'Notice', ['4b'])
