"""Online practice for Level 5 (Primary 5, ages 10 to 12) holiday lesson 1: Numbers to 10 Million ("Million Puzzles").

The questions are the ones printed in the Level 5 holiday workbook, lesson 1: Start here Q1 to Q6 (p5/content/l1.js, workbook()), the Investigation
(p5/content/inv.js), Think harder A1 to A4 (the first four 'stretch' questions of p5/content/l1.js qbank) and Go further B1 to B3
(the last three 'challenge' questions), exactly as p5/workbook_html.js prints them.  Every answer is recomputed by an INDEPENDENT checker below
(search, simulation or a plain loop over the numbers in the question, never a copy of the printed answer); build_holiday.py stops if a checker and the
printed answer differ.
"""
import os, sys
HERE_ = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE_, '..', '..'))
sys.path.insert(0, os.path.join(HERE_, '..'))
from hlib import *          # noqa: E402,F401
from p5lib import *         # noqa: E402,F401

META = dict(level=5, lesson=1, key='p5', title='Million Puzzles', workbook_title='MILLION PUZZLES', topic='Numbers to 10 Million', strand='Whole numbers',
            sources=['p5/content/l1.js', 'p5/content/inv.js', 'p5/content/gaps.js'],
            intro=['Read big numbers in groups of three from the right: 4 | 053 | 200. Test the best number just below AND just above a target. Use the clues in order and check every clue.',
                   'You can use a calculator or write on paper. Type each answer into its box. Some questions ask you to explain: write your idea, then compare it with the model answer after you submit.'])
ST = 'Whole numbers'
CARDS_Q2 = [0, 2, 3, 5, 6, 8, 9]
CARDS_INV = [0, 1, 2, 4, 5, 7, 8]


def D(**k):
    k.setdefault('strand', ST)
    return k


# ---------------------------------------------------------------- the riddle of Q3, solved by searching every number that fits the rounding clue
def riddle_answers():
    out = []
    for n in range(7_250_000, 7_350_000):                       # every number that rounds to 7 300 000 (nearest hundred thousand)
        if round_nearest(n, 100_000) != 7_300_000:
            continue
        d = [int(c) for c in str(n)]                              # M, HTh, TTh, Th, H, T, O
        if len(set(d)) != 7:                                      # clue 1: all different
            continue
        if d[2] != d[1] + 3:                                      # clue 3
            continue
        if d[3] != d[2] - d[1]:                                   # clue 4
            continue
        if d[4] != 2 * d[3] or d[5] != 0:                         # clue 5
            continue
        if sum(d) != 32:                                          # clue 6
            continue
        out.append(n)
    return out


CLUES = ('Clue 1. I am a 7-digit number. My digits are all different.\n'
         'Clue 2. Rounded to the nearest hundred thousand, I am 7 300 000.\n'
         'Clue 3. My ten thousands digit is 3 more than my hundred thousands digit.\n'
         'Clue 4. My thousands digit = my ten thousands digit − my hundred thousands digit.\n'
         'Clue 5. My hundreds digit is twice my thousands digit. My tens digit is 0.\n'
         'Clue 6. My digits add up to 32.')


def start_with_clue2():
    """For each start allowed by clue 2 (7 2 or 7 3): the ten thousands digit from clue 3, the thousands digit from clue 4, and whether all digits are different."""
    res = {}
    for h in (2, 3):
        t = h + 3
        th = t - h
        res[h] = (t, th, len({7, h, t, th}) == 4)
    return res


# ---------------------------------------------------------------- Q4: estimate by rounding
Q4 = [('a', 4987, 21, '×', 104727), ('b', 3004512, 48, '÷', 6259), ('c', 2345678, 3987654, '+', 5333332), ('d', 806, 395, '×', 318370)]


def est_value(x, op, y):
    a, b = sig2(x), sig2(y)
    return a * b if op == '×' else Fraction(a, b) if op == '÷' else a + b


def exact_value(x, op, y):
    return x * y if op == '×' else Fraction(x, y) if op == '÷' else x + y


def could_be_right(x, op, y, ravi):
    """Estimate by rounding both numbers to two digits; the answer could be right if it is within one tenth of the estimate.  Cross-checked with the exact working."""
    est = est_value(x, op, y)
    near = abs(ravi - est) * 10 <= est
    exact = exact_value(x, op, y) == ravi
    assert near == exact, (x, op, y, ravi)                         # the estimate and the exact working agree
    return 'Could be right' if near else 'Must be wrong'


def q4_item(letter, x, y_, op, ravi):
    est = est_value(x, op, y_)
    a, b = sig2(x), sig2(y_)
    ans = could_be_right(x, op, y_, ravi)
    sym = op
    estl = f'{spaced(a)} {sym} {spaced(b)} = {spaced(int(est))}'
    steps = [f'Round both numbers to make an easy estimate: {spaced(x)} is about {spaced(a)} and {spaced(y_)} is about {spaced(b)}.',
             f'The estimate is {estl}.',
             (f"Ravi's answer {spaced(ravi)} is close to the estimate, so it could be right." if ans == 'Could be right'
              else f"Ravi's answer {spaced(ravi)} is far from the estimate {spaced(int(est))}, so it must be wrong.")]
    return D(id=f'4{letter}', tier='core', no=f'4({letter})', type='choice', skill='estimating to check an answer', options=['Could be right', 'Must be wrong'], answer=ans,
             q=f"Ravi used a calculator. Estimate each answer by rounding. Which answers must be wrong?\nRavi says {spaced(x)} {op} {spaced(y_)} = {spaced(ravi)}. Estimate by rounding. Could this be right, or must it be wrong?",
             check=lambda x=x, op=op, y_=y_, ravi=ravi: could_be_right(x, op, y_, ravi),
             hint='Round each number to its first two digits, then work out the easy sum in your head. Is Ravi\'s answer about the same size?', steps=steps,
             src=['Ravi used a calculator. Estimate each answer by rounding. Which answers must be wrong?', f'({letter})  {x} {op} {y_}', spaced(ravi)])


# ---------------------------------------------------------------- Q5 and Think harder: brackets
def bracket_item(iid, tier, no, nums, ops, target, q, src, skill, hint, extra_steps):
    sols = one_pair_solutions(nums, ops, target)
    assert sols, (iid, 'no solution')
    shown = show_tokens(sols[0])
    base = ' '.join([spaced(n) if i == 0 else f'{ops[i - 1]} {spaced(n)}' for i, n in enumerate(nums)])
    return D(id=iid, tier=tier, no=no, type='text', skill=skill, accept=bracket_accepts(sols), shown=shown,
             q=q, check=lambda: show_tokens(one_pair_solutions(nums, ops, target)[0]).replace(' ', ''),
             hint=hint, steps=[f'Brackets are worked out first, then × and ÷, then + and −.'] + extra_steps(shown, base), src=src)


# ---------------------------------------------------------------- the items
CLOSE_INV = {t: closest(t, CARDS_INV) for t in (3_000_000, 4_000_000, 5_000_000, 6_000_000, 7_000_000, 8_000_000)}


def side(t):
    best, below, above = CLOSE_INV[t]
    return 'below' if best < t else 'above'


def inv_a_steps():
    s = ['For each target, find the best number just below it and the best just above it, then compare how far each is from the target.']
    for t in (3_000_000, 4_000_000, 5_000_000, 6_000_000):
        best, below, above = CLOSE_INV[t]
        s.append(f'{spaced(t)}: just below is {spaced(below)} ({spaced(t - below)} away), just above is {spaced(above)} ({spaced(above - t)} away). The closer one is {spaced(best)}.')
    return s


B_TARGET = {n: closest(n, CARDS_INV) for n in range(2_000_000, 9_000_000, 1_000_000)}


def rule_holds():
    """The rule for Investigation (c): the winner is just ABOVE the target exactly when the leading digit of the target is one of the cards."""
    for n, (best, below, above) in B_TARGET.items():
        lead = n // 1_000_000
        if (lead in CARDS_INV) != (best >= n):
            return False
    return True


A3_RANGE = [n for n in range(2_400_000, 2_600_000) if round_nearest(n, 1000) == 2_500_000]
A3_SIX = [n for n in A3_RANGE if digit_sum(n) == 9]
A1_LIST = numbers_with_digit_sum(7, 2)
A4_BEST, A4_BELOW, A4_ABOVE = closest(7_000_000, [1, 2, 5, 6, 7, 8, 9])


def max_bracketing(vals, ops):
    """The biggest value over every way of bracketing vals[0] ops[0] vals[1] ..."""
    best = {}

    def go(i, j):
        if i == j:
            return {Fraction(vals[i])}
        if (i, j) in best:
            return best[(i, j)]
        res = set()
        for k in range(i, j):
            for a in go(i, k):
                for b in go(k + 1, j):
                    o = ops[k]
                    res.add(a + b if o == '+' else a * b)
        best[(i, j)] = res
        return res
    return max(go(0, len(vals) - 1))


def smallest_b2():
    for n in range(6_950_000, 7_050_000):
        d = [int(c) for c in str(n)]
        if n % 2 == 1 and len(set(d)) == 7 and sum(d) == 42 and round_nearest(n, 100_000) == 7_000_000:
            return n


def digits_written(top):
    return sum(len(str(i)) for i in range(1, top + 1))


ITEMS = [
    # ================= Start here (workbook lesson 1: Q1 to Q6)
    D(id='1a', tier='core', no='1(a)', type='number', skill='place value to 10 million', answer=5308040,
      q='Place value. Read big numbers in groups of three from the right:  4 | 053 | 200.\nNumerals for five million, three hundred and eight thousand and forty:',
      check=lambda: words_to_number('five million, three hundred and eight thousand and forty'),
      hint='Write the groups from the left: millions, then thousands, then ones. A group with no hundreds still needs its zero.',
      steps=['Five million is 5 000 000. Three hundred and eight thousand is 308 000. Forty is 40.', 'Put the groups together: 5 | 308 | 040.', 'The numeral is 5 308 040.'],
      src=['Place value. Read big numbers in groups of three from the right', 'Numerals for five million, three hundred and eight thousand and forty']),
    D(id='1b', tier='core', no='1(b)', type='fields', skill='place value to 10 million', answer=[400000, 8],
      q='Place value. In 6 482 315, say what the digit 4 stands for, and which digit is in the ten thousands place.',
      frame='In 6 482 315, the digit 4 stands for {f1}.  The ten thousands digit is {f2}.',
      check=lambda: [int('4') * 10 ** (len('6482315') - 1 - '6482315'.index('4')), int('6482315'[-5])],
      hint='From the right the places are ones, tens, hundreds, thousands, ten thousands, hundred thousands, millions. Which place is the 4 in?',
      steps=['6 482 315: the places from the left are millions 6, hundred thousands 4, ten thousands 8, thousands 2, hundreds 3, tens 1, ones 5.', 'The 4 is in the hundred thousands place, so it stands for 400 000.', 'The ten thousands digit is 8.'],
      src=['In 6 482 315, the digit 4 stands for ________.  The ten thousands digit is ____.']),
    D(id='1c', tier='core', no='1(c)', type='number', skill='place value to 10 million', answer=3250,
      q='Place value. How many thousands make 3 250 000?', check=lambda: len(range(1000, 3_250_000 + 1, 1000)),
      hint='How many thousands are there in one million? Then how many in 3 million, and in 250 000?',
      steps=['1 000 000 is 1000 thousands, so 3 000 000 is 3000 thousands.', '250 000 is 250 thousands.', '3000 + 250 = 3250 thousands. (Cover the last three zeros of 3 250 000.)'],
      src=['How many thousands make 3 250 000?']),

    D(id='2a', tier='core', no='2(a)', type='number', skill='building numbers from digit cards', answer=9865320,
      q='Use ALL seven digit cards, each once, to make a 7-digit number (it cannot start with 0).\nThe greatest number you can make:',
      svg=cards(CARDS_Q2, 'Digit cards 0, 2, 3, 5, 6, 8 and 9'), check=lambda: max(perm_numbers(CARDS_Q2)),
      hint='For the greatest number, put the biggest digit in the millions place, the next biggest after it, and so on.',
      steps=['Put the digits in order from the biggest: 9, 8, 6, 5, 3, 2, 0.', 'The greatest number is 9 865 320.'],
      src=['Use ALL seven digit cards, each once, to make a 7-digit number (it cannot start with 0).', 'Greatest:']),
    D(id='2b', tier='core', no='2(b)', type='number', skill='building numbers from digit cards', answer=2035698,
      q='Use ALL seven digit cards, each once, to make a 7-digit number (it cannot start with 0).\nThe smallest EVEN number you can make:',
      svg=cards(CARDS_Q2, 'Digit cards 0, 2, 3, 5, 6, 8 and 9'), check=lambda: min(n for n in perm_numbers(CARDS_Q2) if n % 2 == 0),
      hint='The first digit cannot be 0. The last digit must be even (0, 2, 6 or 8). Make the front as small as you can, then fix the end.',
      steps=['The number cannot start with 0, so start with the next smallest digit, 2.', 'Then use the smallest digits in order: 0, 3, 5.', 'The digits left are 6, 8 and 9, and the last digit must be even. Put 6 and 9 first and 8 last: 6 9 8 is smaller than 9 8 6 or 8 9 6 or 9 6 8.', 'The smallest even number is 2 035 698.'],
      src=['Use ALL seven digit cards, each once, to make a 7-digit number (it cannot start with 0).', 'Smallest EVEN:']),

    D(id='3a', tier='core', no='3(a)', type='fields', skill='digit riddles', answer=[5, 6],
      q='Digit riddle. Use the clues one at a time. Then check every clue.\n' + CLUES + '\nClue 2 says I start 7 2 … or 7 3 … Clue 3 gives the next digit. Try both.',
      frame='Try both:  7 2 {f1} …   and   7 3 {f2} …',
      check=lambda: [start_with_clue2()[2][0], start_with_clue2()[3][0]],
      hint='Clue 3: the ten thousands digit is 3 more than the hundred thousands digit. If the hundred thousands digit is 2, what is 2 + 3?',
      steps=['A number that rounds to 7 300 000 is between 7 250 000 and 7 349 999, so it starts 7 2 (with a big digit next) or 7 3 (with a small digit next).', 'Clue 3: 3 more than the hundred thousands digit. After 7 2 comes 2 + 3 = 5, so 7 2 5 …', 'After 7 3 comes 3 + 3 = 6, so 7 3 6 …'],
      src=['Digit riddle. Use the clues one at a time. Then check every clue.', 'Clue 2: I start 7 2 … or 7 3 … Clue 3 gives the next digit.  Try both']),
    D(id='3b', tier='core', no='3(b)', type='number', skill='digit riddles', answer=3,
      q='Digit riddle. Use the clues one at a time. Then check every clue.\n' + CLUES + '\nClue 4 gives the next digit. Check Clue 1 (all different): which start breaks it? 7 __ is wrong. Type the digit that goes in the blank.',
      check=lambda: [h for h, (t, th, ok) in start_with_clue2().items() if not ok][0],
      hint='Work out the thousands digit for 7 2 5 … and for 7 3 6 … Does any digit appear twice?',
      steps=['Clue 4: thousands digit = ten thousands digit − hundred thousands digit.', '7 2 5 …: 5 − 2 = 3, so 7 2 5 3 …, and all the digits so far are different.', '7 3 6 …: 6 − 3 = 3, so 7 3 6 3 … The digit 3 is used twice, which breaks Clue 1.', 'So 7 3 is wrong. The answer is 3.'],
      src=['Digit riddle. Use the clues one at a time. Then check every clue.', 'Clue 4 gives the next digit. Check Clue 1 (all different): which start breaks it?']),
    D(id='3c', tier='core', no='3(c)', type='number', skill='digit riddles', answer=7253609,
      q='Digit riddle. Use the clues one at a time. Then check every clue.\n' + CLUES + '\nUse Clues 5 and 6 to finish. I am:',
      check=lambda: (lambda r: r[0] if len(r) == 1 else None)(riddle_answers()),
      hint='So far you have 7 2 5 3. Clue 5 gives the hundreds and tens digits. Clue 6: add the digits you have and see what is missing from 32.',
      steps=['So far: 7 2 5 3 …', 'Clue 5: the hundreds digit is twice the thousands digit, 2 × 3 = 6, and the tens digit is 0. Now 7 2 5 3 6 0 …', 'Clue 6: the digits add up to 32. 7 + 2 + 5 + 3 + 6 + 0 = 23, so the ones digit is 32 − 23 = 9.', 'Check every clue: 7 253 609 has seven different digits, rounds to 7 300 000, 5 = 2 + 3, 3 = 5 − 2, 6 = 2 × 3, tens 0, digits add to 32.'],
      src=['Digit riddle. Use the clues one at a time. Then check every clue.', 'Use Clues 5 and 6 to finish.   I am']),

    q4_item(*Q4[0]), q4_item(*Q4[1]), q4_item(*Q4[2]), q4_item(*Q4[3]),

    bracket_item('5a', 'core', '5(a)', [6, 4, 5, 2], ['+', '×', '−'], 48,
                 'Brackets first, then × and ÷, then + and −. Put in ONE pair of brackets to make the statement true.\n6 + 4 × 5 − 2 = 48\nType the whole sum with the brackets in, for example (2 + 3) × 4.',
                 ['Brackets first, then × and ÷, then + and −. Put in ONE pair of brackets to make each statement true.', '6  +  4  ×  5  −  2  =  48'],
                 'order of operations and brackets', 'Try the brackets round different neighbours. Which pair gives 48? Work it out with brackets first.',
                 lambda shown, base: [f'(6 + 4) × 5 − 2: 6 + 4 = 10, then 10 × 5 = 50, then 50 − 2 = 48.', 'The other places do not give 48. For example 6 + 4 × (5 − 2) = 18, and 6 + (4 × 5) − 2 = 24.']),
    bracket_item('5b', 'core', '5(b)', [6, 4, 5, 2], ['+', '×', '−'], 18,
                 'Brackets first, then × and ÷, then + and −. Put in ONE pair of brackets to make the statement true.\n6 + 4 × 5 − 2 = 18\nType the whole sum with the brackets in.',
                 ['Brackets first, then × and ÷, then + and −. Put in ONE pair of brackets to make each statement true.', '6  +  4  ×  5  −  2  =  18'],
                 'order of operations and brackets', 'Brackets first. If 5 − 2 is in the brackets, what is 4 × 3?',
                 lambda shown, base: ['6 + 4 × (5 − 2): 5 − 2 = 3, then 4 × 3 = 12, then 6 + 12 = 18.', 'Without brackets, 6 + 4 × 5 − 2 = 6 + 20 − 2 = 24, so the brackets change the answer.']),
    bracket_item('5c', 'core', '5(c)', [1000000, 200, 300, 2], ['÷', '+', '×'], 4000,
                 'Brackets first, then × and ÷, then + and −. Put in ONE pair of brackets to make the statement true.\n1 000 000 ÷ 200 + 300 × 2 = 4000\nType the whole sum with the brackets in.',
                 ['Brackets first, then × and ÷, then + and −. Put in ONE pair of brackets to make each statement true.', '1 000 000  ÷  200  +  300  ×  2  =  4000'],
                 'order of operations and brackets', '1 000 000 divided by what makes 2000? Then ×2 gives 4000.',
                 lambda shown, base: ['1 000 000 ÷ (200 + 300) × 2: the brackets first, 200 + 300 = 500.', 'Then × and ÷ from the left: 1 000 000 ÷ 500 = 2000, and 2000 × 2 = 4000.']),

    D(id='6a', tier='core', no='6(a)', type='text', skill='rounding to the nearest thousand', shown='2 499 500, 2 500 000, 2 500 499',
      accept=numlist_accepts([2499500, 2500000, 2500499]),
      q='A 7-digit number is rounded to the nearest thousand. Which of these numbers become 2 500 000?\nNumbers: 2 499 499,  2 499 500,  2 500 000,  2 500 499,  2 500 500\nType each one that rounds to 2 500 000, with a comma between (for example 2499500, 2500000).',
      svg=round_line(),
      check=lambda: ','.join(str(x) for x in [2499499, 2499500, 2500000, 2500499, 2500500] if round_nearest(x, 1000) == 2500000),
      hint='Look at the hundreds digit. 5 or more rounds the thousands UP, 4 or less leaves them.',
      steps=['2 499 499: the hundreds digit is 4, so it rounds down to 2 499 000.', '2 499 500: the hundreds digit is 5, so it rounds up to 2 500 000. Yes.', '2 500 000 is already 2 500 000. Yes.', '2 500 499: the hundreds digit is 4, so it rounds down to 2 500 000. Yes.', '2 500 500: the hundreds digit is 5, so it rounds up to 2 501 000.', 'The numbers that become 2 500 000 are 2 499 500, 2 500 000 and 2 500 499.'],
      src=['A 7-digit number is rounded to the nearest thousand. Which of these numbers become 2 500 000?', 'Circle each one that rounds to 2 500 000:      2 499 499      2 499 500      2 500 000      2 500 499      2 500 500']),
    D(id='6b', tier='core', no='6(b)', type='fields', skill='rounding to the nearest thousand', answer=[2499500, 2500499],
      q='A 7-digit number is rounded to the nearest thousand. Find the smallest and the greatest number that become 2 500 000.',
      frame='The smallest number that rounds to 2 500 000 is {f1} and the greatest is {f2}.',
      check=lambda: [min(A3_RANGE), max(A3_RANGE)],
      hint='Look at your answers to part (a). 2 499 499 rounded down and 2 499 500 rounded up. What about at the top end?',
      steps=['Going down: 2 499 499 rounds to 2 499 000 but 2 499 500 rounds up to 2 500 000, so the smallest is 2 499 500.', 'Going up: 2 500 499 rounds down to 2 500 000 but 2 500 500 rounds up to 2 501 000, so the greatest is 2 500 499.'],
      src=['The smallest number that rounds to 2 500 000 is ____________ and the greatest is ____________.']),

    # ================= Investigation: What if we change the target?
    D(id='C0', tier='invest', no='C (easy first step)', type='choice', skill='closest number to a target', options=['The number just below 4 000 000', 'The number just above 4 000 000'],
      answer='The number just above 4 000 000',
      q='What if we change the target?\nEasy first step: use the cards 0, 1, 2, 4, 5, 7, 8 for just ONE target, 4 000 000. Write one number from just below it and one from just above it. Which is closer?',
      svg=cards(CARDS_INV, 'Digit cards 0, 1, 2, 4, 5, 7 and 8'),
      check=lambda: 'The number just below 4 000 000' if CLOSE_INV[4_000_000][0] < 4_000_000 else 'The number just above 4 000 000',
      hint='There is no 3 card, so the best number below starts with 2. A number above can start with the 4 card and be small after it.',
      steps=[f'Just below 4 000 000: the best number starts with 2 (there is no card 3) and is as big as possible: {spaced(CLOSE_INV[4_000_000][1])}, which is {spaced(4_000_000 - CLOSE_INV[4_000_000][1])} away.',
             f'Just above: start with 4 and make the rest as small as possible: {spaced(CLOSE_INV[4_000_000][2])}, which is only {spaced(CLOSE_INV[4_000_000][2] - 4_000_000)} away.', 'The number just above is closer.'],
      src=['Easy first step: use the cards 0, 1, 2, 4, 5, 7, 8 for just ONE target, 4 000 000. Write one number from just below it and one from just above it. Which is closer?']),
    D(id='Ca', tier='invest', no='C(a)', type='fields', skill='closest number to a target', answer=[CLOSE_INV[t][0] for t in (3_000_000, 4_000_000, 5_000_000, 6_000_000)],
      q='Use the digit cards 0, 1, 2, 4, 5, 7, 8, each once, to make the 7-digit number closest to a TARGET. Find the closest number for the targets 3 000 000, 4 000 000, 5 000 000 and 6 000 000.',
      svg=cards(CARDS_INV, 'Digit cards 0, 1, 2, 4, 5, 7 and 8'),
      frame='3 000 000:  {f1}     4 000 000:  {f2}     5 000 000:  {f3}     6 000 000:  {f4}',
      check=lambda: [closest(t, CARDS_INV)[0] for t in (3_000_000, 4_000_000, 5_000_000, 6_000_000)],
      hint='For each target find the best number just below and the best just above, and see which is closer.', steps=inv_a_steps(),
      src=['Use the digit cards 0, 1, 2, 4, 5, 7, 8, each once, to make the 7-digit number closest to a TARGET. Find the closest number for the targets 3 000 000, 4 000 000, 5 000 000 and 6 000 000.']),
    D(id='Cb7', tier='invest', no='C(b) 7 000 000', type='choice', skill='closest number to a target', options=['Just below the target', 'Just above the target'],
      answer='Just above the target',
      q='For each target, does the winner come from just BELOW the target or just ABOVE it? Try 7 000 000 with the cards 0, 1, 2, 4, 5, 7, 8. Where does the closest number come from?',
      check=lambda: 'Just below the target' if side(7_000_000) == 'below' else 'Just above the target',
      hint='Is there a 7 card? What is the smallest number you can make that starts with 7?',
      steps=[f'There is a 7 card. Start with 7 and make the rest as small as possible: {spaced(CLOSE_INV[7_000_000][2])}, only {spaced(CLOSE_INV[7_000_000][2] - 7_000_000)} above 7 000 000.',
             f'The best number below starts with 5: {spaced(CLOSE_INV[7_000_000][1])}, which is {spaced(7_000_000 - CLOSE_INV[7_000_000][1])} below. So the winner is just above the target.'],
      src=['For each target, does the winner come from just BELOW the target or just ABOVE it? What do you notice? Try 7 000 000 and 8 000 000 to test your idea.']),
    D(id='Cb8', tier='invest', no='C(b) 8 000 000', type='choice', skill='closest number to a target', options=['Just below the target', 'Just above the target'],
      answer='Just above the target',
      q='Now try 8 000 000 with the cards 0, 1, 2, 4, 5, 7, 8. Where does the closest number come from?',
      check=lambda: 'Just below the target' if side(8_000_000) == 'below' else 'Just above the target',
      hint='Is there an 8 card? What is the smallest number you can make that starts with 8?',
      steps=[f'There is an 8 card. Start with 8 and make the rest as small as possible: {spaced(CLOSE_INV[8_000_000][2])}, only {spaced(CLOSE_INV[8_000_000][2] - 8_000_000)} above 8 000 000.',
             f'The best number below starts with 7: {spaced(CLOSE_INV[8_000_000][1])}, which is {spaced(8_000_000 - CLOSE_INV[8_000_000][1])} below. So the winner is just above the target.'],
      src=['Try 7 000 000 and 8 000 000 to test your idea.']),
    D(id='Cbn', tier='invest', no='C(b) what do you notice', type='selfcheck', open=False, skill='noticing patterns',
      q='What do you notice? For the targets 3 000 000, 4 000 000, 5 000 000, 6 000 000, 7 000 000 and 8 000 000, which side wins each time? Write your idea in words.',
      facts=[side(t) for t in (3_000_000, 4_000_000, 5_000_000, 6_000_000, 7_000_000, 8_000_000)],
      check=lambda: [side(t) for t in (3_000_000, 4_000_000, 5_000_000, 6_000_000, 7_000_000, 8_000_000)],
      hint='Make a list: 3 million, 4 million, and so on, with the word below or above next to each. Look at which targets are different from the others.',
      steps=['The winners: 3 000 000 from below, 4 000 000 from above, 5 000 000 from above, 6 000 000 from below, 7 000 000 from above, 8 000 000 from above.',
             'Two targets (3 and 6 million) are won from below. The other four are won from above.',
             'The cards are 0, 1, 2, 4, 5, 7, 8. There is no 3 card and no 6 card. Those are the two targets that are won from below.'],
      src=['For each target, does the winner come from just BELOW the target or just ABOVE it? What do you notice?']),
    D(id='Cc', tier='invest', no='C(c)', type='selfcheck', open=False, skill='explaining a rule',
      q='What stays the same in every case? Write a rule that tells someone which side wins.',
      facts=True, check=rule_holds,
      hint='Look at the first digit of each target. Is that digit one of the cards or not?',
      steps=['Rule: if the first digit of the target (4, 5, 7 or 8) is one of the cards, start with that card and make the rest as small as possible. The winner is just ABOVE the target.',
             'If the first digit of the target is NOT one of the cards (3 or 6), you cannot start with it. The winner comes from just BELOW: start with the next smaller card and make the rest as big as possible.',
             'A good answer says that both sides were tested every time, the gaps were compared by subtracting, and the rule is written in words.'],
      src=['What stays the same in every case? Write a rule that tells someone which side wins.']),

    # ================= Think harder (A1 to A4)
    D(id='A1n', tier='stretch', no='A1', type='number', skill='digit sums and place value', answer=7,
      q='How many 7-digit numbers have digits that add up to 2?', check=lambda: len(A1_LIST),
      hint='The digits add to only 2. Where can the 1s and 2 go? A 7-digit number cannot start with 0.',
      steps=['Digits that add to 2 are either one 2 and zeros, or two 1s and zeros.', 'One 2: the 2 must be first, so only 2 000 000.', 'Two 1s: the first digit is 1 and the other 1 is in one of the other 6 places. That is 6 numbers.', '1 + 6 = 7 numbers.'],
      src=['How many 7-digit numbers have digits that add up to 2? List them all.']),
    D(id='A1l', tier='stretch', no='A1 (list)', type='set', ordered=False, skill='digit sums and place value', answer=A1_LIST,
      q='List them all: the 7-digit numbers whose digits add up to 2. Type each one with no spaces inside it, with a comma between.', check=lambda: numbers_with_digit_sum(7, 2),
      hint='Start with the 2 000 000. Then slide the second 1 along: 1 000 001, 1 000 010, ...',
      steps=['With the first digit 1 and one more 1: 1 000 001, 1 000 010, 1 000 100, 1 001 000, 1 010 000, 1 100 000.', 'With a 2 first: 2 000 000.', 'All seven: 1 000 001, 1 000 010, 1 000 100, 1 001 000, 1 010 000, 1 100 000 and 2 000 000.'],
      src=['How many 7-digit numbers have digits that add up to 2? List them all.']),
    bracket_item('A2a', 'stretch', 'A2(a)', [2, 3, 4, 5], ['+', '×', '+'], 25,
                 'Put ONE pair of brackets into 2 + 3 × 4 + 5 to make 25. Type the whole sum with the brackets in.',
                 ['Put ONE pair of brackets into 2 + 3 × 4 + 5 to make 25. Then put one pair in a different place to make 29.'],
                 'order of operations and brackets', 'Try the brackets round 2 + 3 first. What do you get?',
                 lambda shown, base: ['(2 + 3) × 4 + 5: 2 + 3 = 5, then 5 × 4 = 20, then 20 + 5 = 25.']),
    bracket_item('A2b', 'stretch', 'A2(b)', [2, 3, 4, 5], ['+', '×', '+'], 29,
                 'Now put one pair of brackets in a DIFFERENT place in 2 + 3 × 4 + 5 to make 29. Type the whole sum with the brackets in.',
                 ['Put ONE pair of brackets into 2 + 3 × 4 + 5 to make 25. Then put one pair in a different place to make 29.'],
                 'order of operations and brackets', 'Try the brackets round 4 + 5 this time.',
                 lambda shown, base: ['2 + 3 × (4 + 5): 4 + 5 = 9, then 3 × 9 = 27, then 2 + 27 = 29. (29 is the biggest you can make with one pair.)']),
    D(id='A3a', tier='stretch', no='A3(a)', type='fields', skill='rounding to the nearest thousand', answer=[2499500, 2500499],
      q='A 7-digit number rounded to the nearest thousand is 2 500 000. Its digits add up to 9. Write the range first: the smallest and the greatest number that round to 2 500 000.',
      frame='The smallest is {f1} and the greatest is {f2}.', check=lambda: [min(A3_RANGE), max(A3_RANGE)],
      hint='Think about the hundreds digit: 5 or more rounds up, 4 or less rounds down.',
      steps=['Smallest: 2 499 500 rounds up to 2 500 000, but 2 499 499 rounds down.', 'Greatest: 2 500 499 rounds down to 2 500 000, but 2 500 500 rounds up.', 'The range is 2 499 500 to 2 500 499.'],
      src=['A 7-digit number rounded to the nearest thousand is 2 500 000. Its digits add up to 9. Write the range first (the smallest and the greatest number that round to 2 500 000). Then find ALL the numbers that fit. How do you know you have them all?']),
    D(id='A3b', tier='stretch', no='A3(b)', type='set', ordered=False, skill='rounding and digit sums', answer=A3_SIX,
      q='Now find ALL the numbers in that range whose digits add up to 9. Type each one with no spaces inside it, with a comma between.', check=lambda: [n for n in A3_RANGE if digit_sum(n) == 9],
      hint='In the range, the numbers start 2 500 ___ or 2 499 5__. What do the first digits add to? How much is left for the last three digits?',
      steps=['From 2 500 000 to 2 500 499 the first four digits 2, 5, 0, 0 add to 7, so the last three digits must add to 2, with the hundreds digit 4 or less.', 'The last three digits can be 002, 011, 020, 101, 110 and 200.', 'The numbers are 2 500 002, 2 500 011, 2 500 020, 2 500 101, 2 500 110 and 2 500 200.'],
      src=['A 7-digit number rounded to the nearest thousand is 2 500 000. Its digits add up to 9.']),
    D(id='A3c', tier='stretch', no='A3(c)', type='selfcheck', open=False, skill='explaining why a list is complete',
      q='How do you know you have all the numbers? Think about the numbers from 2 499 500 up to 2 499 999.',
      facts=min(digit_sum(n) for n in range(2_499_500, 2_500_000)),
      check=lambda: min(digit_sum(n) for n in range(2_499_500, 2_500_000)),
      hint='Add the digits of 2 499 5__. How big is the sum already, before the last two digits?',
      steps=['The numbers 2 499 500 to 2 499 999 start 2 4 9 9 and then 5 or more. The first digits already add to 2 + 4 + 9 + 9 = 24, and the hundreds digit adds at least 5 more, so the digit sum is at least 29.', 'That is much more than 9, so there are none below 2 500 000.', 'The numbers from 2 500 000 to 2 500 499 were all checked by the last three digits. So the six numbers are all of them.'],
      src=['How do you know you have them all?']),
    D(id='A4', tier='stretch', no='A4', type='number', skill='closest number to a target', answer=6987521,
      q='Use the seven digit cards 1, 2, 5, 6, 7, 8, 9 once each to make the 7-digit number closest to 7 000 000. Test both sides of the target.',
      svg=cards([1, 2, 5, 6, 7, 8, 9], 'Digit cards 1, 2, 5, 6, 7, 8 and 9'),
      check=lambda: closest(7_000_000, [1, 2, 5, 6, 7, 8, 9])[0],
      hint='Make the best number that starts with 7 (as small as possible after it) and the best that starts with 6 (as big as possible after it). Compare the gaps.',
      steps=[f'Just above: start with 7 and make the rest as small as possible: {spaced(A4_ABOVE)}, which is {spaced(A4_ABOVE - 7_000_000)} away.', f'Just below: start with 6 and make the rest as big as possible: {spaced(A4_BELOW)}, which is {spaced(7_000_000 - A4_BELOW)} away.', f'{spaced(7_000_000 - A4_BELOW)} is smaller, so {spaced(A4_BEST)} is the closest.'],
      src=['Use the seven digit cards 1, 2, 5, 6, 7, 8, 9 once each to make the 7-digit number closest to 7 000 000. Test both sides of the target.']),

    # ================= Go further (B1 to B3)
    D(id='B1', tier='challenge', no='B1', type='number', skill='order of operations and brackets', answer=231,
      q='Put brackets into 1 + 2 × 3 + 4 × 5 + 6 to make the answer as big as possible. You may use more than one pair. What is the biggest answer?',
      check=lambda: int(max_bracketing([1, 2, 3, 4, 5, 6], ['+', '×', '+', '×', '+'])),
      hint='Multiplying big numbers gives big answers. How can you make the sums bigger first and then multiply?',
      steps=['With no brackets: 1 + 2 × 3 + 4 × 5 + 6 = 1 + 6 + 20 + 6 = 33.', 'Add first and then multiply: (1 + 2) × (3 + 4) × (5 + 6) = 3 × 7 × 11.', '3 × 7 = 21 and 21 × 11 = 231.', 'No other way of bracketing gives more, so the biggest answer is 231.'],
      src=['Put brackets into 1 + 2 × 3 + 4 × 5 + 6 to make the answer as big as possible. You may use more than one pair. What is the biggest answer?']),
    D(id='B2', tier='challenge', no='B2', type='number', skill='digit riddles', answer=6953487,
      q='I am a 7-digit odd number. My digits are all different and add up to 42. Rounded to the nearest hundred thousand, I am 7 000 000. I am the smallest number that fits. Who am I?',
      check=smallest_b2,
      hint='Seven different digits that add up to 42: which seven digits could they be? Then what must the first digits be?',
      steps=['The biggest seven digits, 9, 8, 7, 6, 5, 4 and 3, add up to exactly 42. So the digits must be 3, 4, 5, 6, 7, 8, 9, with no 0.', 'Rounded to the nearest hundred thousand it is 7 000 000, so the number is from 6 950 000 to 7 049 999. The digits have no 0, so it starts 6 9 and then 5, 7 or 8 next. The smallest is 6 9 5.', 'Use the smallest digits left in order: 3, 4, then the last digit must be odd, so 8 7 (not 7 8).', 'I am 6 953 487.'],
      src=['I am a 7-digit odd number. My digits are all different and add up to 42. Rounded to the nearest hundred thousand, I am 7 000 000. I am the smallest number that fits. Who am I?']),
    D(id='B3a', tier='challenge', no='B3(a)', type='number', skill='counting digits', answer=2893,
      q='Ali writes all the whole numbers from 1 to 1000. How many digits does he write?', check=lambda: digits_written(1000),
      hint='Count the 1-digit numbers, the 2-digit numbers, the 3-digit numbers and the last number, 1000, separately.',
      steps=['1 to 9: 9 numbers with 1 digit, 9 digits.', '10 to 99: 90 numbers with 2 digits, 180 digits.', '100 to 999: 900 numbers with 3 digits, 2700 digits.', '1000 has 4 digits.', '9 + 180 + 2700 + 4 = 2893.'],
      src=['Ali writes all the whole numbers from 1 to 1000. How many digits does he write? (Go further: how many if he writes all the numbers from 1 to 1 000 000?)']),
    D(id='B3b', tier='challenge', no='B3(b)', type='number', skill='counting digits', answer=5888896,
      q='Go further: how many digits does Ali write if he writes all the whole numbers from 1 to 1 000 000?', check=lambda: digits_written(1_000_000),
      hint='Use the same plan: 1-digit, 2-digit, 3-digit, 4-digit, 5-digit and 6-digit numbers, then the last number.',
      steps=['1-digit: 9 × 1 = 9.', '2-digit: 90 × 2 = 180.', '3-digit: 900 × 3 = 2700.', '4-digit: 9000 × 4 = 36 000.', '5-digit: 90 000 × 5 = 450 000.', '6-digit: 900 000 × 6 = 5 400 000.', '1 000 000 has 7 digits.', '9 + 180 + 2700 + 36 000 + 450 000 + 5 400 000 + 7 = 5 888 896.'],
      src=['Go further: how many if he writes all the numbers from 1 to 1 000 000?']),
    D(id='pose', tier='challenge', no='Make up your own', type='selfcheck', open=True, skill='making up a puzzle',
      q='Make up your own. Write your own 7-digit number riddle with three clues. Swap with a partner and solve each other\'s riddles. (Think for 30 seconds before anyone speaks.)',
      hint='Pick a 7-digit number first. Then write clues that only that number fits: a rounding clue, a clue that compares two digits and a digit sum are good.',
      steps=['This question is open: many riddles are right.', 'Check your riddle: list every number that fits your rounding clue first, then see which of them also fit the other clues.', 'A good riddle has exactly one answer. Ask a partner to solve it and see if you get the same number.'],
      src=['Write your own 7-digit number riddle with three clues. Swap with a partner and solve each other’s riddles.']),
]


# ---------------------------------------------------------------- variants: a template with an oracle for the number items that have small, readable numbers
def _round_range(n):
    target = n * 1_000_000 + 500_000
    ok = [x for x in range(target - 2000, target + 2000) if round_nearest(x, 1000) == target]
    return dict(f1=min(ok), f2=max(ok))


VARIANTS = {
    '1c': dict(
        base=dict(n=3),
        tpl=dict(vars=dict(n=[1, 2, 3, 4, 5, 6, 7, 8, 9]), q='Place value. How many thousands make {n} 250 000?', answer='n*1000+250',
                 hint='How many thousands are in one million? Then add the thousands in 250 000.',
                 steps=['{n} 000 000 is {n}000 thousands, and 250 000 is 250 thousands.', '{n}000 + 250 = {ans} thousands. (Cover the last three zeros of {n} 250 000.)']),
        oracle=lambda e: len(range(1000, e['n'] * 1_000_000 + 250_000 + 1, 1000))),
    '6b': dict(
        base=dict(n=2),
        tpl=dict(vars=dict(n=[1, 2, 3, 4, 5, 6, 7, 8, 9]), q='A 7-digit number is rounded to the nearest thousand. Find the smallest and the greatest number that become {n} 500 000.',
                 frame='The smallest number that rounds to {n} 500 000 is {f1} and the greatest is {f2}.',
                 answers=dict(f1='n*1000000+499500', f2='n*1000000+500499'),
                 hint='5 or more in the hundreds place rounds up, 4 or less rounds down. Find the first number that rounds up to {n} 500 000 and the last that rounds down to it.',
                 steps=['Going down: {n} 499 499 rounds down to {n} 499 000, but {n} 499 500 rounds up to {n} 500 000.', 'Going up: {n} 500 499 rounds down to {n} 500 000, but {n} 500 500 rounds up to {n} 501 000.', 'The smallest is the first number and the greatest is the second: the answers are {ans}.']),
        oracle=lambda e: _round_range(e['n'])),
}
