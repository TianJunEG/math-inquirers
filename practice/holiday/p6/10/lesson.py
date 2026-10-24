"""Online practice for Level 6 (Primary 6, ages 11-13) holiday lesson 10: Showcase Challenge (a mixed challenge round, then planning and showing a puzzle program).

The questions are the ones printed in the Level 6 holiday workbook (p6/content/l10.js workbook(): Start here Q1 to Q6; the Finish page: the Investigation (p6/content/gaps.json lesson 10)
and the exit slip (l10.js lesson.exit); Think harder = the first three l10.js qbank.stretch questions plus the one moved there from Start here (l10.js moved: the digit cards);
Go further = the last three l10.js qbank.challenge questions).  Every answer is recomputed by an INDEPENDENT checker below: sticks in a hexagon chain by sharing sides one hexagon at a time,
factor and prime lists by trying every divisor, clock answers by counting on one hour at a time, a regular polygon by its inside angle (n - 2) x 180 / n, a probability by listing every
equally likely outcome (no simulation), and the code of Q1(d) by running the SAME block program that is drawn (w5lib.run).  build_holiday.py stops if a checker and the printed answer differ.
Q5 and Q6 (plan your own puzzle program and tests) are open: a worked example, itself computed, is shown after Submit.  Scratch is not run in the page.
"""
import itertools, os, re, sys
from fractions import Fraction
HERE_ = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE_, '..'))
sys.path.insert(0, os.path.join(HERE_, '..', '..'))
from hlib import *      # noqa: E402,F401
import p6lib as P       # noqa: E402
import w5lib as W       # noqa: E402
import w3lib            # noqa: E402

M = W.MINUS
META = dict(level=6, lesson=10, key='p6', title='Showcase Challenge', workbook_title='SHOWCASE CHALLENGE', topic='Mixed: Maths and Code', strand='Mixed challenge',
            sources=['p6/content/l10.js', 'p6/content/gaps.json'],
            intro=['This is the last lesson. First a challenge round with puzzles from the whole programme, then you plan a small puzzle program of your own and show it. You do not need Scratch on this page.',
                   'Work out the maths by hand first. A program is a test: if it agrees with your hand answer, you are probably both right.',
                   'The planning questions (5 and 6, and the exit slip) have no single right answer. Write your own, then compare with the worked example shown after Submit.'],
            )
SQ, PR, MC, DC, PC = 'Sequences and algebra', 'Primes and factors', 'Number and measures', 'Data and chance', 'Planning and coding'

_src = open(os.path.join(HERE_, '..', '..', '..', '..', 'p6', 'content', 'l10.js'), encoding='utf-8').read()
HEX_PROG = ['set sticks to 6', {'c': 'repeat 14', 'body': ['change sticks by 5']}, 'say sticks']
for _t in ('set sticks to 6', 'repeat 14', 'change sticks by 5', 'say sticks', 'Hexagon chains made of sticks'):
    assert _t in _src, _t
FIG_HEX = W.hexfig()
FIG_CODE = W.blocks('l10', HEX_PROG, 'Code blocks: set sticks to 6, repeat 14 (change sticks by 5), say sticks.', fs=16)


def sticks_seq(n):
    return W.sticks_of_hexagons(n)


# ---- Starter A model program (the worked example of Q5 and Q6): the computer picks n from 1 to 20, shows out = 5n - 2 and checks the guess
MODEL_PROG = ['when green flag clicked', 'set n to (pick random 1 to 20)', 'set out to ((n × 5) − 2)', 'say (join (Out came ) (out))', 'ask (What went in?) and wait',
              {'c': 'if (answer) = (n) then', 'body': ['say (You cracked it!)'], 'else': ['say (join (No, it was ) (n))']}]


def count_blocks(prog):
    n = 0
    for it in prog:
        if isinstance(it, dict):
            n += 1 + count_blocks(it['body']) + count_blocks(it.get('else', []))
        else:
            n += 1
    return n


def machine_out(n):
    return n * 5 - 2


def machine_in(out):
    return next(n for n in range(1, 21) if machine_out(n) == out)


def terms7(limit=100):
    out, n = [], 1
    while 7 * n - 3 <= limit:
        out.append(7 * n - 3)
        n += 1
    return out


TERMS = terms7()
SPIN_PAIRS = [(a, b) for a in range(1, 9) for b in range(1, 9)]
DICE = [(a, b) for a in range(1, 7) for b in range(1, 7)]
CARDS = list(itertools.permutations([1, 2, 3, 4], 2))
FIG_CARDS = w3lib.cards([1, 2, 3, 4])
FIG_GRID = W.table_svg(['spin 1 ↓  spin 2 →'] + [str(c) for c in range(1, 9)], [[str(r)] + [''] * 8 for r in range(1, 9)],
                       'An empty 8 by 8 table: the first spin down the side and the second spin across the top, to work out each total.', [150] + [30] * 8, 15, 28)


def fmt_factors(n):
    return ' × '.join(str(x) for x in W.prime_factors(n))


ITEMS = []
A = ITEMS.append

# ================= Start here (workbook Lesson 10, Q1 to Q6)
A(dict(id='1a', tier='core', no='1(a)', type='number', strand=SQ, skill='counting sticks in a chain', answer=51, svg=FIG_HEX, label='1(a)',
       q='Chains of hexagons are made from sticks. One hexagon uses 6 sticks, two hexagons joined along a side use 11 sticks and three use 16 sticks. How many sticks are used for 10 hexagons?',
       check=lambda: sticks_seq(10),
       hint='How many sticks does each new hexagon add? Look at 6, 11, 16.',
       steps=['Each new hexagon shares one side with the one before it, so it adds 6 − 1 = 5 sticks.', 'The first hexagon uses 6 sticks, and 9 more hexagons add 9 x 5 = 45 sticks.', '6 + 45 = 51.', '10 hexagons use 51 sticks.'],
       src=['Sticks for 10 hexagons?']))
HEX_RULE = ['5n + 1', '5n+1', '1 + 5n', '1+5n', '5 x n + 1', '5 × n + 1', 'n x 5 + 1', '5*n+1']
A(dict(id='1b', tier='core', no='1(b)', type='text', strand=SQ, skill='rule for a pattern', accept=HEX_RULE, shown='5n + 1', svg=FIG_HEX, label='1(b)',
       q='Chains of hexagons are made from sticks. Write the rule for the number of sticks for n hexagons. Type it with n, in the way you would type 3n + 2.',
       check=lambda: (lambda d, c: f'{d}n + {c}')(*P.linear_rule([sticks_seq(k) for k in range(1, 7)])),
       hint='How many sticks does each new hexagon add? Use that to build the rule, then test it on 1, 2 and 3 hexagons.',
       steps=['Each new hexagon adds 5 sticks, so the rule has 5n in it.', '1 hexagon uses 6 sticks: 5 x 1 = 5, and 6 is 1 more.', 'The rule is sticks = 5n + 1. (Check: n = 3 gives 5 x 3 + 1 = 16.)'],
       src=['Rule for n hexagons:']))
A(dict(id='1c', tier='core', no='1(c)', type='number', strand=SQ, skill='working backwards from a rule', answer=20, svg=FIG_HEX, label='1(c)',
       q='Chains of hexagons are made from sticks. One hexagon uses 6 sticks, two use 11 and three use 16. How many hexagons can be made with exactly 101 sticks?',
       check=lambda: next(n for n in range(1, 500) if sticks_seq(n) == 101),
       hint='Use your rule from 1(b), or count on from 6, 11, 16, … until you reach 101.',
       steps=['The rule is 5n + 1 = 101.', '101 − 1 = 100, and 100 ÷ 5 = 20.', '20 hexagons use exactly 101 sticks.'],
       src=['How many hexagons can be made with exactly 101 sticks?']))
A(dict(id='1d1', tier='core', no='1(d) says', type='number', strand=PC, skill='predicting what code says', answer=76, svg=FIG_CODE, label='1(d) says',
       q='Look at the code. Predict what the sprite says at the end.',
       check=lambda: W.whole(W.run(HEX_PROG)[0][-1]),
       hint='Follow the blocks one at a time: where does sticks start, and how many times does the loop run?',
       steps=['The sprite starts with sticks = 6.', 'Then 14 times it adds 5: 14 x 5 = 70.', '6 + 70 = 76.', 'The sprite says 76.'],
       src=['Predict what the code says.']))
A(dict(id='1d2', tier='core', no='1(d) chain', type='number', strand=PC, skill='linking code to a pattern', answer=15, svg=FIG_CODE, label='1(d) chain',
       q='Look at the code. It works out the number of sticks for one chain of hexagons. How many hexagons are in the chain it checks?',
       check=lambda: next(n for n in range(1, 500) if sticks_seq(n) == W.whole(W.run(HEX_PROG)[0][-1])),
       hint='Which number of hexagons gives the same number of sticks as the sprite says? Use your rule, or count on from 6 sticks.',
       steps=['The code starts with 6 sticks, which is 1 hexagon.', 'It adds 5 sticks 14 times, so it adds 14 more hexagons.', '1 + 14 = 15.', 'It checks a chain of 15 hexagons. (Check: 5 x 15 + 1 = 76.)'],
       src=['Which chain does it check?']))

A(dict(id='2a', tier='core', no='2(a)', type='number', strand=PR, skill='factors and primes', answer=49, label='Bonus 2(a)',
       q='Bonus question. Prime hunters. I have 2 digits and exactly 3 factors. My digits add up to 13. What number am I?',
       check=lambda: (lambda c: c[0] if len(c) == 1 else None)([n for n in range(10, 100) if len(W.factors(n)) == 3 and sum(int(d) for d in str(n)) == 13]),
       hint='A number with exactly 3 factors is a prime multiplied by itself. Which two-digit numbers like that are there?',
       steps=['The 2-digit numbers with exactly 3 factors are 25 (1, 5, 25) and 49 (1, 7, 49).', 'The digits of 25 add up to 7. The digits of 49 add up to 4 + 9 = 13.', 'I am 49.'],
       src=['I have 2 digits and exactly 3 factors. My digits add up to 13. What am I?']))
A(dict(id='2b', tier='core', no='2(b)', type='set', strand=PR, skill='prime factorisation', answer=[2, 2, 3, 7], label='Bonus 2(b)',
       q='Bonus question. Write 84 as a product of prime numbers. Type the primes with a comma between (for example 2, 3, 5 means 2 × 3 × 5).',
       check=lambda: W.prime_factors(84),
       hint='Split 84 into two factors, then keep splitting until every number is prime.',
       steps=['84 = 4 x 21 = 2 x 2 x 21, and 21 = 3 x 7.', '84 = 2 × 2 × 3 × 7.', 'The primes are 2, 2, 3 and 7.'],
       src=['Write 84 as a product of prime numbers.']))
A(dict(id='2c', tier='core', no='2(c)', type='set', strand=PR, skill='sums of two primes', answer=[3, 11, 17], label='Bonus 2(c)',
       q='Bonus question. Find ALL the ways to write 40 as two primes added. Type the smaller prime of each way, with commas.',
       check=lambda: [p for p in W.primes_between(2, 20) if W.is_prime(40 - p) and p <= 40 - p],
       hint='Try each prime below 20 as the smaller one. Is 40 minus that prime also a prime?',
       steps=['40 = 3 + 37, 40 = 11 + 29 and 40 = 17 + 23. In each way both numbers are prime.', 'The other primes below 20 do not work: 2, 5, 7, 13 and 19 each leave a number that is not prime.',
              'The smaller primes are 3, 11 and 17.'],
       src=['Find ALL the ways to write 40 as two primes added.']))

A(dict(id='3a', tier='core', no='3(a)', type='number', strand=MC, skill='negative numbers on a thermometer', answer=-7, label='3(a)',
       q=f'Quick-fire round. It is {M}4 °C. It warms up 9 °C, then cools 12 °C. What is it now? Type a minus sign for below zero.',
       check=lambda: -4 + 9 - 12,
       hint='Go up 9 from the start, then down 12 from where you are. Use a thermometer drawing if it helps.',
       steps=[f'{M}4 °C warms up 9 °C: {M}4 + 9 = 5 °C.', f'5 °C cools 12 °C: 5 {M} 12 = {M}7 °C.', f'It is {M}7 °C now.'],
       src=['It is −4 °C. It warms up 9 °C, then cools 12 °C. What is it now?']))
A(dict(id='3b', tier='core', no='3(b)', type='number', strand=SQ, skill='a machine that gives back its input', answer=5, label='3(b)',
       q='Quick-fire round. A machine does × 3, then − 10. Which IN number comes OUT unchanged?',
       check=lambda: next(n for n in range(-100, 101) if n * 3 - 10 == n),
       hint='You want IN x 3, minus 10, to be the same as IN. Try some numbers, or think what IN x 3 must equal.',
       steps=['IN x 3 − 10 must equal IN.', 'Try 5: 5 x 3 = 15, and 15 − 10 = 5. It comes out unchanged.', 'The number is 5.'],
       src=['A machine does × 3, then − 10. Which IN number comes OUT unchanged?']))
A(dict(id='3c', tier='core', no='3(c)', type='number', strand=MC, skill='regular polygon from its turning angle', answer=15, label='3(c)',
       q='Quick-fire round. A turtle draws a regular polygon, turning 24° at each corner. How many sides does it have?',
       check=lambda: next(n for n in range(3, 200) if W.interior_angle(n) == 180 - 24),
       hint='The turtle turns all the way round once, 360°, while it draws the polygon.',
       steps=['The turtle turns 360° altogether, in turns of 24°.', '360 ÷ 24 = 15.', 'The polygon has 15 sides. (Check: the inside angle of a regular 15-sided polygon is 13 x 180 ÷ 15 = 156°, and 180° − 156° = 24°.)'],
       src=['A turtle draws a regular polygon, turning 24° at each corner. Sides?']))
A(dict(id='3d', tier='core', no='3(d)', type='number', strand=MC, skill='clock arithmetic', answer=1, label='3(d)',
       q='Quick-fire round. It is 9 o\'clock. What time will a 12-hour clock show 100 hours from now?',
       check=lambda: W.clock_after(9, 100),
       hint='12 hours later it is the same time. How many hours are left over after you take away whole turns of the clock?',
       steps=['100 = 8 x 12 + 4, so 100 hours is 8 whole turns of the clock and 4 more hours.', '9 + 4 = 13, and 13 − 12 = 1.', 'It will be 1 o\'clock.'],
       src=['It is 9 o’clock. What time will a 12-hour clock show 100 hours from now?']))

A(dict(id='4a1', tier='core', no='4(a) n = 9', type='number', strand=SQ, skill='running a machine forwards', answer=31, label='4(a) n = 9',
       q='Maths first. Starter A, Mystery Machine: the computer picks a number n and shows the result of × 3, then + 4. If n = 9, what does it show?',
       check=lambda: 9 * 3 + 4,
       hint='Do the machine\'s two steps in order, starting with 9.',
       steps=['9 x 3 = 27.', '27 + 4 = 31.', 'It shows 31.'],
       src=['Mystery Machine (× 3, then + 4).  n = 9 gives?']))
A(dict(id='4a2', tier='core', no='4(a) OUT 58', type='number', strand=SQ, skill='running a machine backwards', answer=18, label='4(a) OUT 58',
       q='Maths first. Starter A, Mystery Machine: the computer picks a number n and shows the result of × 3, then + 4. It shows 58. What number n did the computer pick?',
       check=lambda: next(n for n in range(1, 100) if n * 3 + 4 == 58),
       hint='Go backwards through the machine: undo the last step first.',
       steps=['Undo + 4: 58 − 4 = 54.', 'Undo × 3: 54 ÷ 3 = 18.', 'The computer picked 18. (Check: 18 x 3 + 4 = 58.)'],
       src=['OUT 58 came from?']))
A(dict(id='4b1', tier='core', no='4(b) factors', type='number', strand=PR, skill='counting factors', answer=4, label='4(b) factors',
       q='Maths first. Starter B, Prime or Not?: a loop counts the factors of a number n using mod. Exactly 2 factors means prime. How many factors does it count for 91?',
       check=lambda: len(W.factors(91)),
       hint='Try dividing 91 by each number from 1 upwards. Which numbers divide it exactly?',
       steps=['91 ÷ 1 = 91, and 91 = 7 x 13.', 'The factors of 91 are 1, 7, 13 and 91.', 'It counts 4 factors.'],
       src=['How many factors does it count for 91?']))
OPT_P = ['Yes, 91 is prime', 'No, 91 is not prime']
A(dict(id='4b2', tier='core', no='4(b) prime?', type='choice', strand=PR, skill='deciding if a number is prime', options=OPT_P, answer=OPT_P[1], label='4(b) prime',
       q='Maths first. Starter B, Prime or Not?: a loop counts the factors of a number n using mod. Exactly 2 factors means prime. Is 91 a prime number?',
       check=lambda: OPT_P[0] if W.is_prime(91) else OPT_P[1],
       hint='A prime has exactly 2 factors. Can you find a factor of 91 other than 1 and 91?',
       steps=['91 = 7 x 13, so 7 and 13 are factors of 91.', 'A prime has only two factors, 1 and itself, but 91 has more.', '91 is not a prime number.'],
       src=['Prime?']))
EIGHTS = [d for d in DICE if sum(d) == 8]
OPT_L = ['About 83', 'About 91', 'About 125', 'About 139', 'About 167']
A(dict(id='4c', tier='core', no='4(c)', type='choice', strand=DC, skill='expected count from equally likely results', options=OPT_L, answer=OPT_L[3], label='4(c)',
       q='Maths first. Starter C, Lucky Seven: the program rolls two dice 1000 times and counts the 7s. Change it to count the 8s. About how many 8s do you expect in 1000 rolls?',
       check=lambda: f'About {round(1000 * Fraction(len(EIGHTS), len(DICE)))}',
       hint='List the ways two dice can make a total of 8. How many of the 36 equally likely results is that?',
       steps=['Two dice give 6 x 6 = 36 equally likely results.', 'The 5 results that make 8 are 2 + 6, 3 + 5, 4 + 4, 5 + 3 and 6 + 2.', '1000 x 5 ÷ 36 = 138.9, which is about 139.'],
       src=['Lucky Seven, changed to count 8s: about how many 8s in 1000 rolls? Why?']))
A(dict(id='4cw', tier='core', no='4(c) why', type='selfcheck', strand=DC, skill='explaining an expected count', label='4(c) why',
       q='Starter C, Lucky Seven, changed to count the 8s in 1000 rolls of two dice. Explain how you worked out how many 8s to expect, and why a real run will not give exactly that number. '
         'Write your reason, then check it against the worked solution.',
       facts=dict(ways=5, of=36), check=lambda: dict(ways=len(EIGHTS), of=len(DICE)),
       hint='How many different results can two dice give? How many of them make 8?',
       steps=['Two dice give 36 equally likely results, and 5 of them make 8: 2 + 6, 3 + 5, 4 + 4, 5 + 3 and 6 + 2.', 'So we expect 5 out of every 36 rolls to be an 8: about 1000 x 5 ÷ 36, which is about 139.',
              'The rolls are random, so a real run lands near 139 but is very unlikely to be exactly 139.'],
       src=['Lucky Seven, changed to count 8s: about how many 8s in 1000 rolls? Why?']))

# ---- the worked example for Q5, Q6 and the exit slip (Starter A with a twist; every number is computed)
EX_N = 7
EX_OUT = machine_out(EX_N)
EX_TESTS = [(3, machine_out(3)), (EX_N, EX_OUT), (20, machine_out(20))]
assert machine_in(EX_OUT) == EX_N and all(machine_in(o) == n for n, o in EX_TESTS) and count_blocks(MODEL_PROG) < 15
A(dict(id='5', tier='core', no='5', type='selfcheck', open=True, marking_mode='open', strand=PC, skill='planning a puzzle program', label='5',
       q='My puzzle program: the plan. Choose an idea (Starter A, B or C, or your own). Write the maths puzzle your program asks, its answer worked out by hand, and your twist (what you change or add). '
         'Then compare with the worked example.',
       facts=dict(example_in=EX_N, example_out=EX_OUT), check=lambda: dict(example_in=machine_in(machine_out(EX_N)), example_out=machine_out(EX_N)),
       hint='Pick one idea. Work out the answer by hand first, then think about what you will change.',
       steps=['Many plans are good. A good plan has an idea, a maths puzzle, an answer worked out BEFORE you build, and a twist.',
              f'Example. Idea: Starter A, Mystery Machine. Puzzle: the computer shows OUT and the player finds IN. Twist: change the machine to × 5, then {M} 2.',
              f'Answer by hand: n = {EX_N} gives {EX_N} x 5 {M} 2 = {EX_OUT}; going backwards, {EX_OUT} + 2 = {EX_OUT + 2} and {EX_OUT + 2} ÷ 5 = {EX_N}.'],
       src=['My puzzle program: the plan.']))
A(dict(id='6a', tier='core', no='6(a)', type='selfcheck', paper=True, strand=PC, skill='planning blocks for a program', label='6(a)',
       q='Plan your blocks (under 15) on paper for your puzzle program. Sketch each block, from the first to the last. Then check your plan against the worked example shown on screen.',
       facts=dict(blocks=8, under=15), check=lambda: dict(blocks=count_blocks(MODEL_PROG), under=15 if count_blocks(MODEL_PROG) < 15 else None),
       sol_fig=lambda f: W.blocks('l10', MODEL_PROG, f'The worked example, {f["blocks"]} blocks: when green flag clicked, set n to pick random 1 to 20, set out to n times 5 minus 2, say join Out came and out, '
                                                       'ask What went in and wait, if answer = n then say You cracked it, else say join No, it was and n.', fs=14),
       hint='Write one block for each line of your plan: set up, the rule, show the result, check the answer.',
       steps=['The worked example uses 8 blocks: pick n, work out OUT with the rule, say OUT, ask for a guess, then check the guess with if / else.', 'Your blocks will be different. Check there are fewer than 15.'],
       src=['Plan your blocks (under 15) in the box.']))
A(dict(id='6b', tier='core', no='6(b)', type='selfcheck', open=True, marking_mode='open', strand=PC, skill='testing with hand-worked values', label='6(b)',
       q='Plan three tests for your program BEFORE you run it: two ordinary inputs and one edge case (such as the smallest or the biggest number). For each, write the input and what the program should say, worked out by hand. '
         'Then compare with the worked example.',
       facts=dict(tests=EX_TESTS), check=lambda: dict(tests=[(n, machine_out(n)) for n in (3, EX_N, 20)]),
       hint='Pick an input, work out the answer by hand, and write it down before you run anything.',
       steps=['Your tests will depend on your program. A good test is worked out by hand first, and one test uses an edge case.',
              f'Example for the machine × 5, then {M} 2: Test 1, n = 3 should show {EX_TESTS[0][1]}. Test 2, n = {EX_N} should show {EX_TESTS[1][1]}. Edge case, n = 20 (the biggest number it can pick) should show {EX_TESTS[2][1]}.'],
       src=['Fill in each test BEFORE you run it.']))
A(dict(id='X', tier='core', no='Exit slip', type='selfcheck', open=True, marking_mode='open', strand=PC, skill='explaining a program and its test', label='Exit',
       q='Write one thing your program does, one test you did (the input and the answer you expected), and the maths that explains it. Then compare with the worked example.',
       facts=dict(example_in=3, example_out=machine_out(3)), check=lambda: dict(example_in=3, example_out=machine_out(3)),
       hint='Say what the program does in one sentence. Then give one input and the answer you worked out by hand before running it.',
       steps=['Open: look for a test that was worked out by hand before running the program, and a correct reason from the maths.',
              f'Example: "My program picks n and shows n x 5 {M} 2. I tested n = 3: I expected 3 x 5 {M} 2 = {machine_out(3)}. It works because each step of the machine can be undone: add 2, then divide by 5."'],
       src=['Write one thing your program does, one test you did (the input and the answer you expected), and the maths that explains it.']))

# ================= Investigation (printed on the Finish page)
A(dict(id='I1', tier='invest', no='Investigation first step', type='set', ordered=True, strand=SQ, skill='terms of a sequence', answer=[4, 11, 18, 25, 32], label='Inv 1',
       q='Primes in a sequence. The rule of a sequence is 7n − 3. First step: write the first 5 terms of the sequence. Type them in order, with commas.',
       check=lambda: [7 * n - 3 for n in range(1, 6)],
       hint='Put n = 1, 2, 3, 4, 5 into the rule: 7 times n, then take away 3.',
       steps=[f'n = 1: 7 x 1 {M} 3 = 4. n = 2: 7 x 2 {M} 3 = 11. n = 3: 7 x 3 {M} 3 = 18.', f'n = 4: 7 x 4 {M} 3 = 25. n = 5: 7 x 5 {M} 3 = 32.', 'The first 5 terms are 4, 11, 18, 25, 32.'],
       src=['First step: write the first 5 terms of the sequence 7n − 3']))
A(dict(id='I2', tier='invest', no='Investigation 2', type='number', strand=SQ, skill='how many terms are in range', answer=14, label='Inv 2',
       q=f'Primes in a sequence. The rule of a sequence is 7n {M} 3. How many terms of the sequence are 100 or less?',
       check=lambda: len(TERMS),
       hint='Keep going with the rule until a term goes past 100. Then count the terms before it.',
       steps=['The terms are 4, 11, 18, 25, 32, 39, 46, 53, 60, 67, 74, 81, 88, 95.', f'The next term is 7 x 15 {M} 3 = 102, which is more than 100.', '14 terms are 100 or less.'],
       src=['Find ALL the prime numbers in this sequence up to 100.']))


def composite_notes():
    ev = [t for t in TERMS if t % 2 == 0]
    od = [t for t in TERMS if t % 2 == 1 and not W.is_prime(t)]
    return ev, od


EV, OD = composite_notes()
A(dict(id='I3', tier='invest', no='Investigation 3', type='set', strand=PR, skill='finding the primes in a sequence', answer=[11, 53, 67], label='Inv 3',
       q=f'Primes in a sequence. The rule of a sequence is 7n {M} 3. Find ALL the prime numbers in this sequence up to 100. Type them with commas.',
       check=lambda: [t for t in TERMS if W.is_prime(t)],
       hint='Write out every term up to 100. Then test each one: is it even? Does it have a factor of 3, 5, 7 or 11?',
       steps=['The terms up to 100 are 4, 11, 18, 25, 32, 39, 46, 53, 60, 67, 74, 81, 88, 95.',
              f'The even terms are not prime: {", ".join(str(t) for t in EV)}.',
              'The other composite terms: ' + ', '.join(f'{t} = {fmt_factors(t)}' for t in OD) + '.',
              '11, 53 and 67 have no factors except 1 and themselves, so the primes are 11, 53 and 67.'],
       src=['Find ALL the prime numbers in this sequence up to 100.']))
A(dict(id='I4', tier='invest', no='Investigation 4', type='selfcheck', strand=SQ, skill='explaining remainders of a sequence', label='Inv 4',
       q=f'Explain why no term of the sequence with the rule 7n {M} 3 is a multiple of 7. Write your reason, then check it against the worked solution.',
       facts=dict(remainders=[4]), check=lambda: dict(remainders=sorted({t % 7 for t in [7 * n - 3 for n in range(1, 200)]})),
       hint='Divide some of the terms by 7 and look at the remainders.',
       steps=['7n is always a multiple of 7, and each term is 3 less than 7n.', f'So 7n {M} 3 is 4 more than the multiple of 7 just below it: 7n {M} 3 = 7 x (n {M} 1) + 4.',
              'Dividing by 7 always leaves remainder 4, never 0. (Check: 4, 11, 18, 25 and 32 all leave remainder 4.)'],
       src=['Then explain why no term of the sequence is a multiple of 7.']))

# ================= Think harder (the first three qbank.stretch questions, then the one moved from Start here)
A(dict(id='T1', tier='stretch', no='T1', type='number', strand=SQ, skill='finding a pattern number', answer=33, label='T1',
       q='A row of squares uses 4, 7, 10, 13, … matchsticks. Which pattern number uses exactly 100 matchsticks?',
       check=lambda: next(i + 1 for i, t in enumerate(P.ap(4, 3, 200)) if t == 100),
       hint='What is added each time? Find the rule for the nth pattern, then use it to reach 100.',
       steps=['The numbers go up by 3 each time, and the 1st is 4, so the rule is 3n + 1.', '3n + 1 = 100, so 3n = 99 and n = 33.', 'Pattern 33 uses exactly 100 matchsticks. (Check: 3 x 33 + 1 = 100.)'],
       src=['A row of squares uses 4, 7, 10, 13, … matchsticks.']))
A(dict(id='T2', tier='stretch', no='T2', type='set', strand=PR, skill='finding primes in a range', answer=[83, 89, 97], label='T2',
       q='Find all the prime numbers between 80 and 100. Type them with commas.',
       check=lambda: W.primes_between(81, 99),
       hint='Leave out the even numbers and the multiples of 3, 5 and 7. Then test each number that is left.',
       steps=['The even numbers are not prime, and neither are 81, 85, 87, 91, 93, 95 and 99 (each has a factor of 3, 5 or 7 or more).', '83, 89 and 97 have no factors except 1 and themselves.', 'The primes between 80 and 100 are 83, 89 and 97.'],
       src=['Find all the prime numbers between 80 and 100.']))
A(dict(id='T3', tier='stretch', no='T3', type='number', strand=MC, skill='sides of a regular polygon from an inside angle', answer=12, label='T3',
       q='A regular polygon has an angle of 150° inside each corner. How many sides does it have?',
       check=lambda: next(n for n in range(3, 200) if W.interior_angle(n) == 150),
       hint='At each corner the turtle would turn through the angle that goes with the inside angle to make a straight line.',
       steps=['The inside angle and the turn at a corner make a straight line, 180°. So the turn is 180° − 150° = 30°.', 'The turns add up to 360°: 360 ÷ 30 = 12.', 'The polygon has 12 sides.'],
       src=['A regular polygon has an angle of 150° inside each corner. How many sides does it have?']))
A(dict(id='T4a', tier='stretch', no='T4(a) all', type='number', strand=DC, skill='counting arrangements', answer=12, svg=FIG_CARDS, label='T4 (a) all',
       q='Cards 1, 2, 3 and 4 make 2-digit numbers (no card twice). How many different numbers can you make?',
       check=lambda: len(CARDS),
       hint='How many cards can go in the tens place? Then how many are left for the ones place?',
       steps=['4 cards can go in the tens place.', 'Then 3 cards are left for the ones place.', '4 x 3 = 12 numbers.'],
       src=['Cards 1, 2, 3, 4 make 2-digit numbers (no card twice).']))
A(dict(id='T4b', tier='stretch', no='T4(a) even', type='number', strand=DC, skill='counting arrangements', answer=6, svg=FIG_CARDS, label='T4 (a) even',
       q='Cards 1, 2, 3 and 4 make 2-digit numbers (no card twice). How many of the numbers are even?',
       check=lambda: sum(1 for a, b in CARDS if b % 2 == 0),
       hint='Which cards can go in the ones place to make an even number? Then how many cards are left for the tens place?',
       steps=['An even number ends in 2 or 4, so there are 2 choices for the ones place.', 'Then 3 cards are left for the tens place.', '2 x 3 = 6. The even numbers are 12, 32, 42, 14, 24 and 34.'],
       src=['How many are even?']))
A(dict(id='T4c', tier='stretch', no='T4(b)', type='text', strand=DC, skill='probability as a fraction', accept=['1/3', '4/12'], shown='1/3', equiv_frac=True, svg=FIG_CARDS, label='T4 (b)',
       q='Cards 1, 2, 3 and 4 make 2-digit numbers (no card twice). One of the numbers is picked at random. What is the probability that it is a multiple of 3? Type a fraction.',
       check=lambda: str(Fraction(sum(1 for a, b in CARDS if (10 * a + b) % 3 == 0), len(CARDS))),
       hint='Count the numbers that are multiples of 3. Then compare that with the count of all the numbers.',
       steps=['The multiples of 3 are 12, 21, 24 and 42: 4 numbers.', 'All the numbers are equally likely to be picked.', 'The probability is 4 out of 12 = 4/12 = 1/3.'],
       src=['One of the numbers is picked at random. What is the probability it is a multiple of 3?']))

# ================= Go further (the last three qbank.challenge questions)
A(dict(id='C1', tier='challenge', no='C1', type='selfcheck', open=True, marking_mode='open', strand=SQ, skill='writing a question that mixes two topics', label='C1',
       q='Make up a challenge question that mixes TWO topics from the programme (for example primes and the clock, or sequences and negative numbers). Write the question, the answer and the working. '
         'Then compare with the worked example.',
       facts=dict(first_multiple_of_5=(4, 25)), check=lambda: dict(first_multiple_of_5=next((n, 7 * n - 3) for n in range(1, 100) if (7 * n - 3) % 5 == 0)),
       hint='Pick two topics, write the question, then solve it yourself. Check that both topics are really needed.',
       steps=['Open: many questions are good. Check that the answer is right and that both topics are needed.',
              f'Example (sequences and multiples): "The nth term of a sequence is 7n {M} 3. Which is the first term that is a multiple of 5?" The terms are 4, 11, 18, 25, so it is the 4th term, 25.'],
       src=['Make up a challenge question that mixes TWO topics from the programme']))
A(dict(id='C2a', tier='challenge', no='C2(a)', type='text', strand=DC, skill='probability from a table of outcomes', accept=['1/8', '8/64'], shown='1/8', equiv_frac=True, svg=FIG_GRID, label='C2(a)',
       q='A spinner has the numbers 1 to 8, all equally likely. Ravi spins it twice and adds the numbers. What is the probability that the total is 9? Type a fraction.',
       check=lambda: str(Fraction(sum(1 for a, b in SPIN_PAIRS if a + b == 9), len(SPIN_PAIRS))),
       hint='Fill in the table of totals, or list the pairs that make 9. How many pairs are there altogether?',
       steps=['There are 8 x 8 = 64 equally likely pairs.', 'The pairs that make 9 are 1 + 8, 2 + 7, 3 + 6, 4 + 5, 5 + 4, 6 + 3, 7 + 2 and 8 + 1: 8 pairs.', 'The probability is 8/64 = 1/8.'],
       src=['A spinner has the numbers 1 to 8, all equally likely. Ravi spins it twice and adds the numbers. What is the probability that the total is 9?']))
NINES = [
    'when green flag clicked', 'set nines to 0',
    {'c': 'repeat 1000', 'body': ['set a to (pick random 1 to 8)', 'set b to (pick random 1 to 8)', {'c': 'if (a + b) = 9 then', 'body': ['change nines by 1']}]},
    'say nines']
A(dict(id='C2b', tier='challenge', no='C2(b)', type='selfcheck', paper=True, strand=PC, skill='planning a program that tests a probability', label='C2(b)',
       q='A spinner has the numbers 1 to 8, all equally likely. Ravi spins it twice and adds the numbers. Plan a program that tests this 1000 times. Sketch the blocks on paper, then check against the worked example.',
       facts=dict(expected=125), check=lambda: dict(expected=round(1000 * Fraction(sum(1 for a, b in SPIN_PAIRS if a + b == 9), len(SPIN_PAIRS)))),
       sol_fig=lambda f: W.blocks('l10', NINES, 'A program that tests the spinner 1000 times: when green flag clicked, set nines to 0, repeat 1000 (set a to pick random 1 to 8, set b to pick random 1 to 8, '
                                                 'if a + b = 9 then change nines by 1), say nines.', fs=15),
       hint='You need a counter that starts at 0, two random spins, a check for a total of 9, and a loop of 1000.',
       steps=['One plan: set nines to 0. Repeat 1000 times: pick two random numbers a and b from 1 to 8, and if a + b = 9 change nines by 1. At the end say nines.',
              'The program should say about 125 (1000 x 1/8), but not exactly 125, because the spins are random.'],
       src=['Plan a program that tests it 1000 times.']))
A(dict(id='C3a', tier='challenge', no='C3(a)', type='choice', strand=SQ, skill='testing whether a number is in a sequence', options=['Yes', 'No'], answer='Yes', label='C3(a)',
       q=f'The nth term of a sequence is 6n {M} 1. Is 2027 in the sequence?',
       check=lambda: 'Yes' if any(6 * n - 1 == 2027 for n in range(1, 1000)) else 'No',
       hint='If 2027 is a term, then 6n − 1 = 2027 for some whole number n. What would 6n have to be?',
       steps=[f'6n {M} 1 = 2027 means 6n = 2028.', '2028 ÷ 6 = 338, a whole number.', f'So 2027 is the 338th term (6 x 338 {M} 1 = 2027). Yes, it is in the sequence.'],
       src=['Is 2027 in the sequence?']))
A(dict(id='C3b', tier='challenge', no='C3(b)', type='number', strand=SQ, skill='the next term of a sequence', answer=2033, label='C3(b)',
       q=f'The nth term of a sequence is 6n {M} 1. What is the first term of the sequence that is bigger than 2027?',
       check=lambda: next(6 * n - 1 for n in range(1, 1000) if 6 * n - 1 > 2027),
       hint='The terms go up by 6 each time. Find the last term that is not bigger than 2027, then go one term further.',
       steps=['Terms go up by 6 each time, and 2027 is the 338th term.', f'The next term is the 339th: 6 x 339 {M} 1 = 2033.', 'The first term bigger than 2027 is 2033.'],
       src=['Which is the first term bigger than 2027?']))

for _it in ITEMS:
    _it['q'] = re.sub(r'\s{2,}', ' ', _it['q'])
    if _it.get('frame'):
        _it['frame'] = W.nb(_it['frame'])

P.finish(ITEMS)

# ---------------------------------------------------------------- variant families (every combination is run against an independent oracle at build time)
HEXQ = 'One hexagon uses 6 sticks, two hexagons joined along one side use 11 sticks and three use 16 sticks. '
VARIANTS = {
    '1a': dict(base=dict(n=10),
               tpl=dict(vars=dict(n=list(range(4, 31))), derive=dict(more='n-1', add='(n-1)*5'),
                        q='Chains of hexagons are made from sticks. ' + HEXQ + 'How many sticks are used for {n} hexagons?', answer='5*n+1',
                        hint='How many sticks does each new hexagon add? Look at 6, 11, 16.',
                        steps=['Each new hexagon adds 5 sticks, and the first uses 6.', '{more} more hexagons add {more} x 5 = {add} sticks.', '6 + {add} = {ans}.']),
               oracle=lambda e: sticks_seq(e['n'])),
    '1c': dict(base=dict(n=20),
               tpl=dict(vars=dict(n=list(range(8, 41))), derive=dict(S='5*n+1', R='5*n'),
                        q='Chains of hexagons are made from sticks. ' + HEXQ + 'How many hexagons can be made with exactly {S} sticks?', answer='n',
                        hint='Use your rule from 1(b), or count on from 6, 11, 16, … until you reach 101.',
                        steps=['The rule is 5n + 1 = {S}.', '{S} − 1 = {R}, and {R} ÷ 5 = {ans}.', '{ans} hexagons use exactly {S} sticks.']),
               oracle=lambda e: next(k for k in range(1, 500) if sticks_seq(k) == 5 * e['n'] + 1)),
    '3b': dict(base=dict(k=10),
               tpl=dict(vars=dict(k=[4, 6, 8, 10, 12, 14, 16, 18, 20]), derive=dict(t='3*(k/2)'),
                        q='Quick-fire round. A machine does × 3, then − {k}. Which IN number comes OUT unchanged?', answer='k/2',
                        hint='You want IN x 3, minus {k}, to be the same as IN. Try some numbers, or think what IN x 3 must equal.',
                        steps=['Try {ans}: {ans} x 3 = {t}, and {t} − {k} = {ans}. It comes out unchanged.', 'The number is {ans}.']),
               oracle=lambda e: next(n for n in range(-100, 101) if n * 3 - e['k'] == n)),
    '3c': dict(base=dict(t=24),
               tpl=dict(vars=dict(t=[20, 24, 30, 36, 40, 45, 60, 72]),
                        q='Quick-fire round. A turtle draws a regular polygon, turning {t}° at each corner. How many sides does it have?', answer='360/t',
                        hint='The turtle turns all the way round once, 360°, while it draws the polygon.',
                        steps=['The turtle turns 360° altogether, in turns of {t}°.', '360 ÷ {t} = {ans}.', 'The polygon has {ans} sides.']),
               oracle=lambda e: next(n for n in range(3, 400) if W.interior_angle(n) == 180 - e['t'])),
    '3d': dict(base=dict(s=9, h=100),
               tpl=dict(vars=dict(s=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], h=[50, 100, 200, 300, 500, 1000]), derive=dict(tot='s+h'),
                        q="Quick-fire round. It is {s} o'clock. What time will a 12-hour clock show {h} hours from now?", answer='(s+h-1)%12+1',
                        hint='12 hours later it is the same time. How many hours are left over after you take away whole turns of the clock?',
                        steps=['{s} + {h} = {tot}.', 'The clock wraps round after 12, so take away 12 as many times as you can, keeping a number from 1 to 12.', "It will be {ans} o'clock."]),
               oracle=lambda e: W.clock_after(e['s'], e['h'])),
    '4a1': dict(base=dict(n=9),
                tpl=dict(vars=dict(n=list(range(2, 21))), derive=dict(m='n*3'),
                         q='Maths first. Starter A, Mystery Machine: the computer picks a number n and shows the result of × 3, then + 4. If n = {n}, what does it show?', answer='3*n+4',
                         hint='Do the machine\'s two steps in order, starting with {n}.',
                         steps=['{n} x 3 = {m}.', '{m} + 4 = {ans}.', 'It shows {ans}.']),
                oracle=lambda e: e['n'] * 3 + 4),
    '4a2': dict(base=dict(n=18),
                tpl=dict(vars=dict(n=list(range(2, 31))), derive=dict(o='3*n+4', b='3*n'),
                         q='Maths first. Starter A, Mystery Machine: the computer picks a number n and shows the result of × 3, then + 4. It shows {o}. What number n did the computer pick?', answer='n',
                         hint='Go backwards through the machine: undo the last step first.',
                         steps=['Undo + 4: {o} − 4 = {b}.', 'Undo × 3: {b} ÷ 3 = {ans}.', 'The computer picked {ans}.']),
                oracle=lambda e: next(n for n in range(1, 200) if n * 3 + 4 == 3 * e['n'] + 4)),
    'T1': dict(base=dict(n=33),
               tpl=dict(vars=dict(n=[20, 25, 30, 35, 40, 45, 50, 60]), derive=dict(P='3*n+1', R='3*n'),
                        q='A row of squares uses 4, 7, 10, 13, … matchsticks. Which pattern number uses exactly {P} matchsticks?', answer='n',
                        hint='What is added each time? Find the rule for the nth pattern, then use it to reach {P}.',
                        steps=['The numbers go up by 3 each time, and the 1st is 4, so the rule is 3n + 1.', '3n + 1 = {P}, so 3n = {R} and n = {ans}.', 'Pattern {ans} uses exactly {P} matchsticks.']),
               oracle=lambda e: next(i + 1 for i, t in enumerate(P.ap(4, 3, 200)) if t == 3 * e['n'] + 1)),
    'T3': dict(base=dict(a=150),
               tpl=dict(vars=dict(a=[108, 120, 135, 140, 144, 150, 156, 160, 162, 165]), derive=dict(turn='180-a'),
                        q='A regular polygon has an angle of {a}° inside each corner. How many sides does it have?', answer='360/(180-a)',
                        hint='At each corner the turtle would turn through the angle that goes with the inside angle to make a straight line.',
                        steps=['The inside angle and the turn at a corner make a straight line, 180°. So the turn is 180° − {a}° = {turn}°.', 'The turns add up to 360°: 360 ÷ {turn} = {ans}.', 'The polygon has {ans} sides.']),
               oracle=lambda e: next(n for n in range(3, 400) if W.interior_angle(n) == e['a'])),
    'C3b': dict(base=dict(x=2027),
                tpl=dict(vars=dict(x=[100, 250, 500, 999, 1000, 1500, 2027, 3000]), derive=dict(k='(x+1)//6', k1='(x+1)//6+1'),
                         q='The nth term of a sequence is 6n − 1. What is the first term of the sequence that is bigger than {x}?', answer='6*((x+1)//6+1)-1',
                         hint='The terms go up by 6 each time. Find which term number reaches {x} or just below it, then go one term further.',
                         steps=['The terms are 5, 11, 17, … , going up by 6 each time.', 'Term {k} is the last term that is not bigger than {x}, so the next term is term {k1}.', '6 x {k1} − 1 = {ans}.']),
                oracle=lambda e: next(6 * n - 1 for n in range(1, 2000) if 6 * n - 1 > e['x'])),
}
