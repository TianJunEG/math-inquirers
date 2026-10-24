"""Online practice for Level 6 (Primary 6, ages 11-13) holiday lesson 2: Prime Hunters (primes, factors, prime factorisation; if, mod and a counter).

The questions are the ones printed in the Level 6 holiday workbook (p6/content/l2.js: the Start here pages Q1 to Q6; the Finish page: the Investigation and the exit slip;
the Think harder page: the first three Think harder questions of p6/content/l2.js qbank.stretch plus the one that was moved there from Start here Q5; Go further: the last
three p6/content/l2.js qbank.challenge items; the Investigation text is p6/content/gaps.json lesson 2).  Every answer is recomputed by an INDEPENDENT checker below
(plain loops over the numbers in the question, or the block-program interpreter p6lib.run for the code questions; never a copy of the printed answer).
build_holiday.py stops if a checker and the printed answer differ.  Scratch is not run in the page: the code is drawn as blocks and traced on paper or in the head.
"""
import functools, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from hlib import *      # noqa: E402,F401
import p6lib as P       # noqa: E402

META = dict(level=6, lesson=2, key='p6', title='Prime Hunters', workbook_title='PRIME HUNTERS', topic='Primes, Factors and Prime Factorisation',
            strand='Number theory',
            sources=['p6/content/l2.js', 'p6/content/gaps.json'],
            intro=['You do not need Scratch on this page. The code is drawn as blocks: read it, trace it on paper or in your head, and type what the sprite says.',
                   'A prime number has exactly 2 factors: 1 and itself. 1 is not prime.',
                   'When a question asks for a list of numbers, type them with a comma between each one. Some questions ask you to draw or plan code: do those on paper, then check yourself against the picture of the answer.'])
NT, CO = 'Number theory', 'Coding and number theory'
HAT = P.HAT


def table_svg(head, rows, label, colw):
    W, rh = sum(colw) + 8, 30
    b = ''
    for ri, r in enumerate([head] + rows):
        x = 4
        for ci, v in enumerate(r):
            b += (f'<rect x="{x}" y="{4 + ri * rh}" width="{colw[ci]}" height="{rh}" fill="{YEL if ri == 0 else "#fff"}" stroke="{NAVY}" stroke-width="2"/>'
                  + P.T(x + colw[ci] / 2, 4 + ri * rh + 20, v, 15, 'middle', 800 if ri == 0 else 600))
            x += colw[ci]
    H = rh * (len(rows) + 1) + 8
    return (f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{P.esc(label)}" '
            f'style="width:100%;max-width:{W}px;height:auto;display:block;margin:0 auto">{b}</svg>')


# ---------------------------------------------------------------- the programs (as drawn in the workbook)
def count_prog(n, loops=None):
    return [HAT, ['var', 'set count to (0)'], ['var', 'set d to (1)'],
            ['ctl', f'repeat ({loops or n})', [['ctl', f'if ({n} mod d = 0) then', [['var', 'change count by (1)']]], ['var', 'change d by (1)']]], ['look', 'say (count)']]


PAL = [('A', [['look', 'say (d) for (1) seconds']]), ('B', [['ctl', 'repeat (40)', []]]), ('C', [['var', 'set d to (1)']]),
       ('D', [['var', 'change d by (1)']]), ('E', [HAT]), ('F', [['ctl', 'if (40 mod d = 0) then', []]])]
PROG40 = [HAT, ['var', 'set d to (1)'], ['ctl', 'repeat (40)', [['ctl', 'if (40 mod d = 0) then', [['look', 'say (d) for (1) seconds']]], ['var', 'change d by (1)']]]]
CODE6 = 'Code: set count to 0, d to 1; repeat 6: if 6 mod d = 0 then change count by 1; change d by 1; then say count'


def word(k):
    return f'{k} factor' + ('' if k == 1 else 's')


def klass(n):
    return f'{word(len(P.factors(n)))}, ' + ('prime' if P.is_prime(n) else 'not prime')


def opts_for(n):
    c = len(P.factors(n))
    out = [klass(n)]
    for k, lab in ((2, 'prime'), (c, 'prime' if c != 2 else 'not prime'), (c + 1, 'not prime'), (max(1, c - 1), 'not prime')):
        o = f'{word(k)}, {lab}'
        if o not in out:
            out.append(o)
    return sorted(out[:4], key=lambda s: (int(s.split()[0]), s))


def table_items():
    out = []
    for n in (28, 31, 49, 51, 1):
        fl = P.factors(n)
        out.append(dict(id=f'1-{n}', tier='core', no=f'1 ({n}) factors', type='set', strand=NT, skill='factor pairs', answer=fl,
                        q=f'A prime number has exactly 2 factors: 1 and itself. Use factor pairs to list ALL the factors of {n}. Type them with a comma between.',
                        check=(lambda n=n: P.factors(n)),
                        hint=f'Work in pairs: 1 × {n}, then try 2, 3, 4 ... Stop when the pairs meet.',
                        steps=[f'Factor pairs of {n}: ' + ', '.join(f'{a} × {n // a}' for a in fl if a <= n // a) + '.', f'All the factors of {n}: ' + ', '.join(map(str, fl)) + '.'],
                        src=['A prime number has exactly 2 factors: 1 and itself. Use factor pairs to fill in the table.']))
        out.append(dict(id=f'1-{n}c', tier='core', no=f'1 ({n}) prime?', type='choice', strand=NT, skill='prime or not prime', options=opts_for(n), answer=klass(n),
                        q=f'How many factors does {n} have, and is it prime?', check=(lambda n=n: klass(n)),
                        hint='Count the factors you listed. A prime has exactly 2.',
                        steps=[f'{n} has {word(len(fl))}: ' + ', '.join(map(str, fl)) + '.',
                               ('It has exactly 2 factors, so it is prime.' if len(fl) == 2 else 'It does not have exactly 2 factors, so it is not prime.' + (' (1 is not prime: it has only 1 factor.)' if n == 1 else ''))],
                        src=['Number', 'All its factors', 'How many?', 'Prime?']))
    return out


def lockers():
    st = {i: False for i in range(1, 21)}
    for s in range(1, 21):
        for i in range(s, 21, s):
            st[i] = not st[i]
    return [i for i in range(1, 21) if st[i]]


ITEMS = table_items() + [
    dict(id='1a', tier='core', no='1(a)', type='set', strand=NT, skill='testing for primes', answer=[67, 83, 97],
         q='Test with 2, 3, 5 and 7. Which of these numbers are prime? 57, 67, 77, 83, 97, 99. Type the primes with a comma between.',
         check=lambda: [n for n in (57, 67, 77, 83, 97, 99) if P.is_prime(n)],
         hint='Try dividing each number by 2, 3, 5 and 7. If one divides exactly, the number is not prime.',
         steps=['57 = 3 × 19, 77 = 7 × 11 and 99 = 9 × 11, so they are not prime.', '67, 83 and 97 are not divisible by 2, 3, 5 or 7, so they are prime.'],
         src=['Test with 2, 3, 5 and 7. Circle the primes:     57     67     77     83     97     99']),
    dict(id='1b', tier='core', no='1(b)', type='choice', strand=NT, skill='testing for primes', options=['Yes', 'No'], answer='No',
         q='Ali says 87 is prime because it is odd and does not end in 5. Is he right?', check=lambda: 'Yes' if P.is_prime(87) else 'No',
         hint='Being odd and not ending in 5 is not enough. Try dividing 87 by 3.',
         steps=['The digits of 87 add up to 8 + 7 = 15, which is a multiple of 3, so 3 divides 87.', '87 = 3 × 29, so 87 is not prime. Ali is not right.'],
         src=['Ali says 87 is prime because it is odd and does not end in 5. Is he right?']),
    dict(id='1b2', tier='core', no='1(b) test', type='number', strand=NT, skill='testing for primes',
         q='Ali says 87 is prime because it is odd and does not end in 5. What is the smallest number bigger than 1 that divides 87 exactly?', answer=3,
         check=lambda: next(d for d in range(2, 88) if 87 % d == 0), hint='Try 2, then 3, then 5 ...',
         steps=['87 ÷ 2 is not exact. 8 + 7 = 15 is in the 3 times table, so 87 ÷ 3 = 29 exactly.', 'The smallest such number is 3, so 87 = 3 × 29 is not prime.'],
         src=['Ali says 87 is prime because it is odd and does not end in 5. Is he right?']),

    dict(id='2-tree', tier='core', no='2', type='selfcheck', paper=True, strand=NT, skill='factor trees',
         q='Factor trees. Keep splitting until every branch ends in a prime. Draw the factor trees for 72 and 150.', svg=P.trees_fig(),
         facts=[[2, 2, 2, 3, 3], [2, 3, 5, 5]], check=lambda: [P.prime_factors(72), P.prime_factors(150)],
         sol_fig=lambda f: P.compose([P.factor_tree_svg(72, 'Factor tree of 72: 72 = 8 × 9, 8 = 2 × 4, 4 = 2 × 2, 9 = 3 × 3'),
                                      P.factor_tree_svg(150, 'Factor tree of 150: 150 = 10 × 15, 10 = 2 × 5, 15 = 3 × 5')],
                                     'One correct factor tree for 72 and one for 150 (yellow circles are primes)'),
         hint='Split each number into two factors. If a factor is not prime, split it again. Stop when every end is a prime.',
         steps=['72 = 8 × 9, 8 = 2 × 4, 4 = 2 × 2, 9 = 3 × 3. The primes at the ends are 2, 2, 2, 3, 3.', '150 = 10 × 15, 10 = 2 × 5, 15 = 3 × 5. The primes at the ends are 2, 5, 3, 5.',
                'You can split in a different way and still reach the same primes.'],
         src=['Factor trees. Keep splitting until every branch ends in a prime.']),
    dict(id='2a', tier='core', no='2(a)', type='set', strand=NT, skill='prime factorisation', answer=[2, 2, 2, 3, 3],
         q='Write 72 as a product of primes. Type the primes with a comma between (for example 2, 3, 5 means 2 × 3 × 5).', check=lambda: P.prime_factors(72),
         hint='Split 72 into two factors, then keep splitting until every number is prime.', steps=['72 = 8 × 9 = 2 × 2 × 2 × 3 × 3.', 'The primes are 2, 2, 2, 3, 3.'],
         src=['72  =  _______________']),
    dict(id='2b', tier='core', no='2(b)', type='set', strand=NT, skill='prime factorisation', answer=[2, 3, 5, 5],
         q='Write 150 as a product of primes. Type the primes with a comma between.', check=lambda: P.prime_factors(150),
         hint='Split 150 into 10 × 15, then split again.', steps=['150 = 10 × 15 = 2 × 5 × 3 × 5.', 'The primes are 2, 3, 5, 5.'],
         src=['150  =  _______________']),
    dict(id='2c', tier='core', no='2(c)', type='number', strand=NT, skill='prime factorisation',
         q='A number is 2 × 3 × 3 × 7. What is the number?', answer=126, check=lambda: functools.reduce(lambda a, b: a * b, [2, 3, 3, 7]),
         hint='Multiply step by step: 2 × 3 first.', steps=['2 × 3 = 6, 6 × 3 = 18, 18 × 7 = 126.', 'The number is 126.'],
         src=['A number is 2 × 3 × 3 × 7. What is the number?']),

    dict(id='3-mod', tier='core', no='3', type='fields', strand=CO, skill='tracing code with mod',
         q='Predict, then trace. This code counts the factors of 6 (6 mod d = the left over). Fill in the trace table: "6 mod d" for d = 2, 3, 4, 5, 6 (for d = 1 it is 0).',
         frame='6 mod d for d = 2, 3, 4, 5, 6:  {f1},  {f2},  {f3},  {f4},  {f5}', answer=[0, 0, 2, 1, 0], svg=P.blocks(count_prog(6), CODE6, 14),
         check=lambda: [6 % d for d in range(2, 7)], hint='6 mod d is the remainder when 6 is divided by d.',
         steps=['6 mod 2 = 0, 6 mod 3 = 0, 6 mod 4 = 2, 6 mod 5 = 1, 6 mod 6 = 0.'],
         src=['Predict, then trace. This code counts the factors of 6 (6 mod d = left over). Fill in the table.']),
    dict(id='3-count', tier='core', no='3 count', type='fields', strand=CO, skill='tracing code with mod',
         q='Predict, then trace. Fill in the "count after" column for d = 2, 3, 4, 5, 6 (after d = 1 the count is 1).',
         frame='count after d = 2, 3, 4, 5, 6:  {f1},  {f2},  {f3},  {f4},  {f5}', answer=[2, 3, 3, 3, 4], svg=P.blocks(count_prog(6), CODE6, 14),
         check=lambda: [P.run(count_prog(6, loops=k))[1]['count'] for k in range(2, 7)], hint='The count goes up by 1 each time 6 mod d is 0. Otherwise it stays the same.',
         steps=['d = 1: count 1. d = 2: 6 mod 2 = 0, so count 2. d = 3: count 3.', 'd = 4: 6 mod 4 = 2, so the count stays 3. d = 5: stays 3. d = 6: 6 mod 6 = 0, so count 4.'],
         src=['d 6 mod d count after']),
    dict(id='3a', tier='core', no='3(a)', type='number', strand=CO, skill='tracing code with mod',
         q='Predict, then trace. What does the code say at the end?', answer=4, svg=P.blocks(count_prog(6), CODE6, 14),
         check=lambda: P.run(count_prog(6))[0][-1], hint='It counts the factors of 6: the values of d where 6 mod d = 0.',
         steps=['The count goes up for d = 1, 2, 3 and 6.', 'So it says 4. These are the 4 factors of 6: 1, 2, 3, 6.'],
         src=['(a)  What does it say at the end?  ______']),
    dict(id='3b', tier='core', no='3(b)', type='number', strand=CO, skill='tracing code with mod',
         q='Change both 6s to 13 (repeat 13, and 13 mod d). What does the code say?', answer=2, check=lambda: P.run(count_prog(13))[0][-1],
         svg=P.blocks(count_prog(13), 'Code with 13: set count to 0, d to 1; repeat 13: if 13 mod d = 0 then change count by 1; change d by 1; then say count', 14),
         hint='The code counts the factors of 13. Which d make 13 mod d = 0?',
         steps=['13 mod d is 0 only for d = 1 and d = 13.', 'So the count is 2 and it says 2.'],
         src=['(b)  Change both 6s to 13. What does it say? Why?']),
    dict(id='3b-why', tier='core', no='3(b) why', type='selfcheck', strand=CO, skill='explaining with factors',
         q='Change both 6s to 13. Why does the count come out as it does? Use factors in your reason. Write it, then check it against the worked solution.', facts=dict(factors=[1, 13], count=2),
         check=lambda: dict(factors=P.factors(13), count=len(P.factors(13))), hint='What does the count mean? What are the factors of 13?',
         steps=['The count is the number of factors. 13 has only the factors 1 and 13.', 'So the count is 2. A number with exactly 2 factors is prime, so 13 is prime.'],
         src=['(b)  Change both 6s to 13. What does it say? Why?']),

    dict(id='4a', tier='core', no='4(a)', type='set', strand=NT, skill='Goldbach pairs', answer=[5, 7, 11],
         q='Goldbach\'s guess: every even number above 2 is a sum of two primes. Write 24 as a sum of two primes in every way. Type the SMALLER prime of each pair, with commas (for 24 = 5 + 19 you type 5).',
         check=lambda: [p for p, q in P.goldbach_pairs(24)], hint='Try the primes 2, 3, 5, 7, 11. For each, is 24 take away that prime also prime?',
         steps=['24 = 5 + 19 = 7 + 17 = 11 + 13. That is 3 ways.', 'The smaller primes are 5, 7 and 11. (24 = 1 + 23 does not count: 1 is not prime.)'],
         src=['Goldbach’s guess: every even number above 2 is a sum of two primes.', '24 in every way:  ________________________________']),
    dict(id='4b', tier='core', no='4(b)', type='selfcheck', strand=NT, skill='odd and even primes',
         q='Explain why 27 cannot be the sum of two primes. Write your reason, then check it against the worked solution.',
         facts=dict(pairs=[], even_prime=2, rest=25, rest_prime=False),
         check=lambda: dict(pairs=P.goldbach_pairs(27), even_prime=[p for p in P.primes_upto(30) if p % 2 == 0][0], rest=27 - 2, rest_prime=P.is_prime(27 - 2)),
         hint='27 is odd. What do you know about the two numbers that add to an odd number? Which prime is even?',
         steps=['An odd total needs one even number and one odd number.', 'The only even prime is 2, and 27 - 2 = 25 is not prime (5 × 5).', 'So 27 cannot be the sum of two primes.'],
         src=['Explain why 27 cannot be the sum of two primes.']),

    dict(id='5a', tier='core', no='5(a)', type='set', strand=NT, skill='numbers with exactly 3 factors', answer=[4, 9, 25],
         q='Exactly 3 factors. Which numbers from 1 to 30 have exactly 3 factors? (There are 3.) Type them with a comma between.',
         check=lambda: [n for n in range(1, 31) if len(P.factors(n)) == 3], hint='List the factors of the numbers. Numbers with exactly 3 factors are special: look at 4 first.',
         steps=['4 has factors 1, 2, 4. 9 has 1, 3, 9. 25 has 1, 5, 25.', 'No other number up to 30 has exactly 3 factors.'],
         src=['All the numbers from 1 to 30 with exactly 3 factors (there are 3):  ______________']),
    dict(id='5b', tier='core', no='5(b)', type='selfcheck', strand=NT, skill='numbers with exactly 3 factors',
         q='Exactly 3 factors. What do you notice about 4, 9 and 25? Write your idea, then check it against the worked solution.',
         facts=[(4, 2), (9, 3), (25, 5)], check=lambda: [(n, next(p for p in P.primes_upto(n) if p * p == n)) for n in range(1, 31) if len(P.factors(n)) == 3],
         hint='Look at the numbers 2 × 2, 3 × 3 and 5 × 5.',
         steps=['4 = 2 × 2, 9 = 3 × 3, 25 = 5 × 5. They are squares of primes.', 'Their factors are 1, the prime, and the square.'],
         src=['What do you notice?  ______________________________']),

    dict(id='6-plan', tier='core', no='6', type='selfcheck', paper=True, strand=CO, skill='planning code',
         q='Plan your code. Put the blocks in order so the sprite says every factor of 40.',
         svg=P.compose([(l, P.blocks(p, 'Block ' + l, 14)) for l, p in PAL],
                       'The six blocks: A say d for 1 seconds, B repeat 40, C set d to 1, D change d by 1, E when green flag clicked, F if 40 mod d = 0 then', gap=8),
         facts=[1, 2, 4, 5, 8, 10, 20, 40], check=lambda: P.run(PROG40)[0],
         sol_fig=lambda f: P.compose([P.blocks(PROG40, 'The order: E, C, B with F inside B (A inside F) then D', 14)], 'The correct order: E, C, B; inside B: F with A inside it, then D'),
         hint='What must happen first? Then which block repeats? The if goes inside the repeat, and d must change every time round.',
         steps=['Order: E (when green flag clicked), C (set d to 1), B (repeat 40).', 'Inside B: F (if 40 mod d = 0 then) with A (say d) inside F, and then D (change d by 1).', 'It says 1, 2, 4, 5, 8, 10, 20, 40.'],
         src=['Plan your code. Put the blocks in order so the sprite says every factor of 40.']),
    dict(id='6a', tier='core', no='6(a)', type='number', strand=CO, skill='factors by counting', q='Plan your code. How many numbers does it say?', answer=8,
         check=lambda: len(P.run(PROG40)[0]), svg=P.blocks(PROG40, 'The program: when green flag clicked, set d to 1, repeat 40: if 40 mod d = 0 then say d; change d by 1', 14),
         hint='It says every factor of 40. List them in pairs.', steps=['The factors of 40 are 1, 2, 4, 5, 8, 10, 20, 40.', 'It says 8 numbers, one per second.'],
         src=['How many numbers does it say?  ______']),

    # ---- exit slip (printed on the Finish page)
    dict(id='X-a', tier='core', no='Exit slip (a)', type='choice', strand=NT, skill='testing for primes', options=['Yes', 'No'], answer='No',
         q='Exit slip. Is 111 prime? Show your test.', check=lambda: 'Yes' if P.is_prime(111) else 'No', hint='Add the digits: 1 + 1 + 1. Which small number divides 111?',
         steps=['1 + 1 + 1 = 3, so 3 divides 111.', '111 = 3 × 37, so 111 is not prime.'],
         src=['(a) Is 111 prime? Show your test.']),
    dict(id='X-a2', tier='core', no='Exit slip (a) test', type='number', strand=NT, skill='testing for primes',
         q='Exit slip. Is 111 prime? Show your test: what is the smallest number bigger than 1 that divides 111 exactly?', answer=3,
         check=lambda: next(d for d in range(2, 112) if 111 % d == 0), hint='Try 2, then 3.', steps=['111 ÷ 3 = 37 exactly.', 'The smallest factor above 1 is 3, so 111 = 3 × 37 is not prime.'],
         src=['(a) Is 111 prime? Show your test.']),
    dict(id='X-b', tier='core', no='Exit slip (b)', type='set', strand=NT, skill='prime factorisation', answer=[2, 3, 11],
         q='Exit slip. Write 66 as a product of primes. Type the primes with a comma between.', check=lambda: P.prime_factors(66),
         hint='Split 66 into two factors, then split again.', steps=['66 = 6 × 11 = 2 × 3 × 11.'],
         src=['(b) Write 66 as a product of primes.']),
    dict(id='X-c', tier='core', no='Exit slip (c)', type='choice', strand=NT, skill='testing for primes', options=['Yes', 'No'], answer='No',
         q='Exit slip (optional). Is 133 prime?', check=lambda: 'Yes' if P.is_prime(133) else 'No', hint='Test 2, 3, 5, 7 ... 133 is close to 140.',
         steps=['133 ÷ 7 = 19 exactly, so 133 = 7 × 19.', '133 is not prime.'],
         src=['(c) Optional: is 133 prime?']),
    dict(id='X-c2', tier='core', no='Exit slip (c) test', type='number', strand=NT, skill='testing for primes',
         q='Exit slip (optional). What is the smallest number bigger than 1 that divides 133 exactly?', answer=7,
         check=lambda: next(d for d in range(2, 134) if 133 % d == 0), hint='Test 2, 3, 5, 7.', steps=['133 = 7 × 19.', 'The smallest factor above 1 is 7.'],
         src=['(c) Optional: is 133 prime?']),

    # ================= Investigation
    dict(id='I1', tier='invest', no='Investigation', type='selfcheck', paper=True, strand=NT, skill='is it always true',
         q='Is it always true? Ali says: "If you add two different primes, the answer is never a prime." Test him. List every pair of different primes below 20 and add them. '
           'Is Ali right? What do you notice about the pairs that do make a prime? Explain why. First step: write down all the prime numbers below 20.',
         facts=dict(primes=[2, 3, 5, 7, 11, 13, 17, 19], pairs=28, prime_sums=[(2, 3, 5), (2, 5, 7), (2, 11, 13), (2, 17, 19)]),
         check=lambda: (lambda ps: dict(primes=ps, pairs=sum(1 for i, a in enumerate(ps) for b in ps[i + 1:]),
                                        prime_sums=[(a, b, a + b) for i, a in enumerate(ps) for b in ps[i + 1:] if P.is_prime(a + b)]))(P.primes_upto(19)),
         sol_fig=lambda f: table_svg(['Pair', 'Sum', 'Prime?'], [[f'{a} + {b}', c, 'yes'] for a, b, c in f['prime_sums']] + [['all other pairs', '', 'no']],
                                     'The only pairs of different primes below 20 whose sum is prime: 2+3, 2+5, 2+11, 2+17', [130, 70, 80]),
         hint='Write the primes below 20. Then add them in pairs, in order, so you do not miss any. Look for the number 2.',
         steps=['The primes below 20 are 2, 3, 5, 7, 11, 13, 17, 19. That gives 28 pairs.',
                'Ali is wrong. Exactly four sums are prime: 2 + 3 = 5, 2 + 5 = 7, 2 + 11 = 13, 2 + 17 = 19. Every one uses the prime 2.',
                'Why: two odd primes add to an even number bigger than 2, which has 2 as a factor, so it is not prime. 2 is the only even prime, so only a pair with 2 can give an odd sum.',
                'One counter-example is enough to show "never" is false.'],
         src=['Ali says: “If you add two different primes, the answer is never a prime.” Test him. List every pair of different primes below 20 and add them.']),

    # ================= Think harder
    dict(id='T1a', tier='stretch', no='T1(a)', type='number', strand=NT, skill='counting factors',
         q='How many factors does 64 have?', answer=7, check=lambda: len(P.factors(64)), hint='Work in pairs: 1 × 64, then try 2, 3, 4 ... in order. Stop when the pairs meet.',
         steps=['Pairs: 1 × 64, 2 × 32, 4 × 16, 8 × 8.', '8 × 8 counts once, so there are 3 pairs + 1 = 7 factors.'],
         src=['How many factors does 64 have? List them.']),
    dict(id='T1b', tier='stretch', no='T1(b)', type='set', strand=NT, skill='listing factors', answer=P.factors(64),
         q='List all the factors of 64. Type them with a comma between.', check=lambda: P.factors(64), hint='Find the pairs that make 64, trying 1, 2, 3 ... in order, then write the small ones first and the big ones after.',
         steps=['The factors of 64 are 1, 2, 4, 8, 16, 32, 64.'],
         src=['How many factors does 64 have? List them.']),
    dict(id='T2', tier='stretch', no='T2', type='number', strand=NT, skill='counting factors',
         q='Find the smallest number that has exactly 6 factors.', answer=12, check=lambda: next(n for n in range(1, 1000) if len(P.factors(n)) == 6),
         hint='Try 2, 3, 4, ... and count the factors of each. Which is the first with 6?',
         steps=['Every number below 12 has fewer than 6 factors (for example 8 has 1, 2, 4, 8 and 10 has 1, 2, 5, 10).', '12 has 1, 2, 3, 4, 6, 12: exactly 6 factors.'],
         src=['Find the smallest number that has exactly 6 factors.']),
    dict(id='T3', tier='stretch', no='T3', type='set', strand=NT, skill='Goldbach pairs', answer=[3, 11, 17, 29, 41, 47],
         q='Write 100 as the sum of two primes in every possible way. Type the SMALLER prime of each pair, with commas (for 100 = 3 + 97 you type 3).',
         check=lambda: [p for p, q in P.goldbach_pairs(100)], hint='Try the primes 3, 5, 7, 11 ... up to 50. Is 100 take away each one also prime?',
         steps=['100 = 3 + 97 = 11 + 89 = 17 + 83 = 29 + 71 = 41 + 59 = 47 + 53.', 'That is 6 ways, and the smaller primes are 3, 11, 17, 29, 41, 47.'],
         src=['Write 100 as the sum of two primes in every possible way.']),
    dict(id='T4a', tier='stretch', no='T4(a)', type='set', strand=NT, skill='Goldbach pairs', answer=[5, 7, 13, 17],
         q='Write 36 as the sum of two primes in every way. Type the SMALLER prime of each pair, with commas.', check=lambda: [p for p, q in P.goldbach_pairs(36)],
         hint='Try the primes up to 18. Is 36 take away each one also prime?', steps=['36 = 5 + 31 = 7 + 29 = 13 + 23 = 17 + 19. That is 4 ways.', 'The smaller primes are 5, 7, 13, 17.'],
         src=['Write 36 as the sum of two primes in every way. Then find ALL the numbers from 1 to 50 with exactly 3 factors. What is the next one after 50?']),
    dict(id='T4b', tier='stretch', no='T4(b)', type='set', strand=NT, skill='numbers with exactly 3 factors', answer=[4, 9, 25, 49],
         q='Find ALL the numbers from 1 to 50 with exactly 3 factors. Type them with a comma between.', check=lambda: [n for n in range(1, 51) if len(P.factors(n)) == 3],
         hint='Think of what you found in Start here Q5: squares of primes.', steps=['The numbers with exactly 3 factors are the squares of primes: 4, 9, 25, 49.'],
         src=['Then find ALL the numbers from 1 to 50 with exactly 3 factors. What is the next one after 50?']),
    dict(id='T4c', tier='stretch', no='T4(c)', type='number', strand=NT, skill='numbers with exactly 3 factors',
         q='What is the next number after 50 with exactly 3 factors?', answer=121, check=lambda: next(n for n in range(51, 1000) if len(P.factors(n)) == 3),
         hint='These numbers are squares of primes. After 7 × 7 comes the next prime.', steps=['The next prime after 7 is 11.', '11 × 11 = 121, and 121 has exactly 3 factors: 1, 11, 121.'],
         src=['What is the next one after 50?']),

    # ================= Go further
    dict(id='C1', tier='challenge', no='C1', type='selfcheck', strand=NT, skill='making a number puzzle',
         q='Make up a "Who am I?" number puzzle using factors and primes, for example: "I am between 30 and 60 and I have exactly three factors." Write 2 or 3 clues so that only ONE number fits. Swap with a partner, then check that no other number fits.',
         facts=[49], check=lambda: [n for n in range(31, 60) if len(P.factors(n)) == 3],
         hint='Choose your number first. Then write clues that only it fits. Check by listing every number that fits.',
         steps=['Open question. Example: "I am between 30 and 60 and I have exactly 3 factors" fits only 49 (7 × 7).', 'The numbers with exactly 3 factors are the squares of primes: 4, 9, 25, 49, 121, ...',
                'Check a puzzle by listing every number that fits the clues.'],
         src=['Make up a “Who am I?” number puzzle using factors and primes']),
    dict(id='C2', tier='challenge', no='C2', type='number', strand=NT, skill='remainders and multiples',
         q='A farmer counts her eggs in 2s, 3s, 4s, 5s and 6s, and each time there is 1 egg left over. When she counts them in 7s, none are left over. What is the smallest number of eggs she could have?', answer=301,
         check=lambda: next(n for n in range(2, 2000) if all(n % k == 1 for k in (2, 3, 4, 5, 6)) and n % 7 == 0),
         hint='The number is 1 more than a multiple of 2, 3, 4, 5 and 6. Find the smallest such multiple first.',
         steps=['It must be 1 more than a multiple of 60 (60 is the smallest number in the 2, 3, 4, 5 and 6 times tables).', 'The candidates are 61, 121, 181, 241, 301, ...', 'The first one in the 7 times table is 301 = 7 × 43.'],
         src=['A farmer counts her eggs in 2s, 3s, 4s, 5s and 6s, and each time there is 1 egg left over. When she counts them in 7s, none are left over. What is the smallest number of eggs she could have?']),
    dict(id='C3', tier='challenge', no='C3', type='set', strand=NT, skill='square numbers and factors', answer=[1, 4, 9, 16],
         q='20 lockers are closed. Student 1 opens every locker. Student 2 changes every 2nd locker (open to closed, closed to open). Student 3 changes every 3rd locker, and so on up to student 20. Which lockers are open at the end? Type them with a comma between.',
         check=lockers, hint='Locker n is changed once for each factor of n. Which numbers have an odd number of factors?',
         steps=['Locker n is changed once for each factor of n.', 'It ends open only if it was changed an odd number of times, so n has an odd number of factors. Only square numbers do (the middle factor counts once).', 'Open lockers: 1, 4, 9 and 16.'],
         src=['20 lockers are closed. Student 1 opens every locker. Student 2 changes every 2nd locker']),
]

VARIANTS = {
    '2c': dict(base=dict(a=3, b=7),
               tpl=dict(vars=dict(a=[2, 3, 5], b=[3, 5, 7, 11]), q='A number is 2 × 3 × {a} × {b}. What is the number?', answer='2*3*a*b',
                        hint='Multiply step by step: 2 × 3 first.', steps=['2 × 3 = 6, then 6 × {a}, then × {b}.', 'The number is {ans}.']),
               oracle=lambda e: functools.reduce(lambda x, y: x * y, [2, 3, e['a'], e['b']])),
}

# ---- inquiry habit (docs/pedagogy/inquiry_skills_explicit.md; levels/habits.json)
ITEMS.insert(max(i for i, x in enumerate(ITEMS) if x['tier'] == 'core') + 1, habit_item('Explain',
    'Is 51 a prime number? Write one or two sentences. Start: I know because ...',
    ['51 is not a prime number.', 'For example: I know because 51 = 3 x 17, so it has a factor other than 1 and 51. A quick test: 5 + 1 = 6, and 6 is in the 3 times table, so 3 divides 51.'],
    'Try dividing 51 by small numbers such as 2, 3, 5 and 7.'))
