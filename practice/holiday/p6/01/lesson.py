"""Online practice for Level 6 (Primary 6, ages 11-13) holiday lesson 1: Code the Pattern (sequences and the nth term; a loop and a variable).

The questions are the ones printed in the Level 6 holiday workbook (p6/content/l1.js: the Start here pages; the Finish page: the Investigation and the exit slip;
the Think harder page: the first three Think harder questions of p6/content/l1.js qbank.stretch plus the one that was moved there from Start here Q2; Go further: the last
three p6/content/l1.js qbank.challenge items; the Investigation text is p6/content/gaps.json lesson 1).  Every answer is recomputed by an INDEPENDENT checker below
(loops over the numbers in the question, or the block-program interpreter in p6lib.run for the code questions; never a copy of the printed answer).
build_holiday.py stops if a checker and the printed answer differ.  Scratch is not run in the page: code questions are traced on paper / in the head and the
program is shown as a picture of blocks.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from hlib import *      # noqa: E402,F401
import p6lib as P       # noqa: E402
from fractions import Fraction  # noqa: E402

META = dict(level=6, lesson=1, key='p6', title='Code the Pattern', workbook_title='CODE THE PATTERN', topic='Sequences and the nth Term',
            strand='Patterns and algebra',
            sources=['p6/content/l1.js', 'p6/content/gaps.json'],
            intro=['You do not need Scratch on this page. The code is drawn as blocks: read it, trace it on paper or in your head, and type what the sprite says.',
                   'If the rule for the nth term takes a number away, type that number with a minus sign (for example -4).',
                   'Some questions ask you to plan or fix code or to draw. Do those on paper, then check yourself against the picture of the answer.'])
ST, CO = 'Patterns and algebra', 'Coding and algebra'

# ---------------------------------------------------------------- the programs (as drawn in the workbook)
HAT = P.HAT
PROG4 = [HAT, ['var', 'set x to (2)'], ['ctl', 'repeat (4)', [['var', 'change x by (5)'], ['look', 'say (x) for (1) seconds']]]]
PROG4_100 = [HAT, ['var', 'set x to (2)'], ['ctl', 'repeat (100)', [['var', 'change x by (5)'], ['look', 'say (x) for (1) seconds']]]]
PALETTE5 = [('1', [HAT]), ('2', [['var', 'set n to ( )']]), ('3', [['var', 'change n by ( )']]), ('4', [['ctl', 'repeat ( )', []]]), ('5', [['look', 'say (n) for (1) seconds']])]
MEI = [HAT, ['var', 'set n to (3)'], ['ctl', 'repeat (50)', [['var', 'change n by (4)']]], ['look', 'say (n)']]
MEI_FIXED = [HAT, ['var', 'set n to (3)'], ['ctl', 'repeat (49)', [['var', 'change n by (4)']]], ['look', 'say (n)']]
CH3 = lambda r: [['var', 'set t to (0)'], ['var', 'set k to (0)'], ['ctl', f'repeat ({r})', [['var', 'change k by (1)'], ['var', 'change t by (k)']]], ['look', 'say (t)']]


def program_for(first, diff, count):
    """The program that says the first `count` terms: say, then change (built from the checked first term and difference)."""
    return [HAT, ['var', f'set n to ({first})'], ['ctl', f'repeat ({count})', [['look', 'say (n) for (1) seconds'], ['var', f'change n by ({diff})']]]]


def fig_sticks():
    return P.sticks_fig()


def fig_code(prog, label):
    return P.blocks(prog, label, 15)


def table_svg(head, rows, label, colw=None):
    """A small table drawn as svg (for the correct answer of a selfcheck)."""
    n = len(head)
    colw = colw or [max(54, 9 * max(len(str(r[i])) for r in [head] + rows) + 18) for i in range(n)]
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


# ---------------------------------------------------------------- independent checkers
SQ = [P.sticks_of_squares(k) for k in range(1, 7)]               # 4, 7, 10, 13, 16, 19 counted from the picture
RULE_SQ = P.linear_rule(SQ)                                      # (3, 1)


def rule_row(seq):
    d, c = P.linear_rule(seq)
    return [d, d, c, P.ap(seq[0], d, 100)[-1]]


def half_diff():
    seq = [Fraction(1, 2), Fraction(1), Fraction(3, 2), Fraction(2)]
    d = seq[1] - seq[0]
    assert all(b - a == d for a, b in zip(seq, seq[1:]))
    return d


def in_seq(first, diff, target):
    return target in P.ap(first, diff, 400)


def order_of(first, diff, target):
    return P.ap(first, diff, 400).index(target) + 1


ITEMS = [
    # ================= Start here (workbook Lesson 1, Q1 to Q6)
    dict(id='1-table', tier='core', no='1', type='fields', strand=ST, skill='growing patterns',
         q='Matchstick squares. Each new pattern adds one more square. Fill in the table (pattern 1 is done for you).',
         frame='Pattern 1 to 6, sticks:  4,  {f1},  {f2},  {f3},  {f4},  {f5}', answer=SQ[1:], svg=fig_sticks(), check=lambda: [P.sticks_of_squares(k) for k in range(2, 7)],
         hint='Look at the pictures. Count the sticks in pattern 2, then see how many you add for each new square.',
         steps=['Pattern 1 is one square: 4 sticks. Pattern 2 is two squares joined: 2 on top, 2 on the bottom and 3 upright = 7 sticks.', 'Each new square adds 3 sticks, so the table reads 4, 7, 10, 13, 16, 19.'],
         src=['Matchstick squares. Each new pattern adds one more square. Fill in the table.']),
    dict(id='1a', tier='core', no='1(a)', type='number', strand=ST, skill='growing patterns',
         q='Matchstick squares. Each new square adds ____ sticks. How many sticks does each new square add?', answer=3, svg=fig_sticks(),
         check=lambda: SQ[1] - SQ[0], hint='Look at the table: 4, 7, 10 ... How much more is each pattern than the one before?',
         steps=['4, 7, 10, 13 ... each pattern has 3 more sticks than the one before.', 'So each new square adds 3 sticks.'],
         src=['Each new square adds ____ sticks. Why not 4? __________________']),
    dict(id='1a-why', tier='core', no='1(a) why', type='selfcheck', strand=ST, skill='explaining a pattern',
         q='Why does each new square add 3 sticks and not 4? Write your reason, then check it against the worked solution.', svg=fig_sticks(),
         facts=dict(shared=1, new=3), check=lambda: dict(shared=1, new=P.sticks_of_squares(2) - P.sticks_of_squares(1)),
         hint='A square has 4 sticks. Look at where the new square touches the old one.',
         steps=['A square has 4 sticks, but the new square shares one side with the square before it.', 'That shared stick is already there, so the new square needs only 4 - 1 = 3 new sticks.', 'Any reason about the shared side is a good answer.'],
         src=['Each new square adds ____ sticks. Why not 4? __________________']),
    dict(id='1b', tier='core', no='1(b)', type='fields', strand=ST, skill='rule for the nth term',
         q='Complete the rule for the number of sticks in pattern n.', frame='sticks  =  {f1}  ×  n  +  {f2}', answer=list(RULE_SQ), svg=fig_sticks(),
         check=lambda: list(P.linear_rule(SQ)), hint='The number you add each time is the number in front of n. Then check pattern 1: 4 = ? × 1 + ?',
         steps=['Each new square adds 3 sticks, so the rule starts with 3 × n.', 'For pattern 1: 3 × 1 = 3, but there are 4 sticks, so add 1.', 'The rule is sticks = 3 × n + 1. Check pattern 3: 3 × 3 + 1 = 10.'],
         src=['Complete the rule:   sticks  =  ______ × n  +  ______']),
    dict(id='1c', tier='core', no='1(c)', type='number', strand=ST, skill='finding a far term',
         q='Pattern 100 has ______ sticks. How many sticks does pattern 100 have?', answer=301, svg=fig_sticks(), check=lambda: P.sticks_of_squares(100),
         hint='Use your rule: sticks = 3 × n + 1 with n = 100.',
         steps=['The rule is 3 × n + 1.', '3 × 100 + 1 = 300 + 1 = 301.', 'Pattern 100 has 301 sticks.'],
         src=['Pattern 100 has ______ sticks.    (d)  Which pattern has 61 sticks? ____']),
    dict(id='1d', tier='core', no='1(d)', type='number', strand=ST, skill='working backwards',
         q='Which pattern has 61 sticks?', answer=20, svg=fig_sticks(), check=lambda: next(k for k in range(1, 500) if P.sticks_of_squares(k) == 61),
         hint='Work backwards. Take away the 1, then share the rest into 3s.',
         steps=['The rule is 3 × n + 1 = 61.', '61 - 1 = 60, and 60 ÷ 3 = 20.', 'Pattern 20 has 61 sticks. Check: 3 × 20 + 1 = 61.'],
         src=['Which pattern has 61 sticks? ____']),

    dict(id='2a', tier='core', no='2(a)', type='fields', strand=ST, skill='rule for the nth term',
         q='Write the difference, the rule for the nth term and the 100th term. (Hint: the 100th term is 99 jumps after the 1st term. Use a minus sign for a negative number.)',
         frame='6, 10, 14, 18, ...   difference {f1};   nth term = {f2} × n + {f3};   100th term = {f4}', answer=[4, 4, 2, 402], check=lambda: rule_row([6, 10, 14, 18]),
         hint='The difference is how much you add each time. The number in front of n is the difference. Test the rule on the 1st term.',
         steps=['10 - 6 = 4, 14 - 10 = 4: the difference is 4.', 'The rule starts with 4 × n. For n = 1: 4 × 1 = 4, but the 1st term is 6, so add 2. The rule is 4n + 2.', 'The 100th term is 4 × 100 + 2 = 402. (Check: 6 + 99 × 4 = 402.)'],
         src=['For each sequence, write the difference, the rule for the nth term and the 100th term.', '(a)   6,  10,  14,  18,  …']),
    dict(id='2b', tier='core', no='2(b)', type='fields', strand=ST, skill='rule for the nth term',
         q='Write the difference, the rule for the nth term and the 100th term. (Use a minus sign for a negative number.)',
         frame='1, 6, 11, 16, ...   difference {f1};   nth term = {f2} × n + {f3};   100th term = {f4}', answer=[5, 5, -4, 496], check=lambda: rule_row([1, 6, 11, 16]),
         hint='The difference is how much you add each time. Test 5 × n on the 1st term: is it 1? What must you take away?',
         steps=['6 - 1 = 5, 11 - 6 = 5: the difference is 5.', 'The rule starts with 5 × n. For n = 1: 5 × 1 = 5, but the 1st term is 1, so take away 4. The rule is 5n - 4, which is 5 × n + (-4).', 'The 100th term is 5 × 100 - 4 = 496. (Check: 1 + 99 × 5 = 496.)'],
         src=['(b)   1,  6,  11,  16,  …']),

    dict(id='3a', tier='core', no='3(a)', type='fields', strand=ST, skill='rule for the nth term',
         q='Look at the sequence 5, 9, 13, 17, ... (each term is 4 more than the one before). Write the rule for the nth term.',
         frame='nth term = {f1} × n + {f2}', answer=[4, 1], check=lambda: list(P.linear_rule([5, 9, 13, 17])),
         hint='Think about how much each term grows. Then test your rule on the 1st term, 5: does it give 5?',
         steps=['Each term is 4 more than the one before, so the rule starts with 4 × n.', 'For n = 1: 4 × 1 = 4, but the 1st term is 5, so add 1.', 'The rule is 4n + 1.'],
         src=['Look at the sequence   5,  9,  13,  17,  …   (each term is 4 more than the one before)', 'nth term:  __________']),
    dict(id='3b', tier='core', no='3(b)', type='choice', strand=ST, skill='is it a term of the sequence', options=['Yes', 'No'], answer='Yes',
         q='Look at the sequence 5, 9, 13, 17, ... Is 101 a term?', check=lambda: 'Yes' if in_seq(5, 4, 101) else 'No',
         hint='Use the rule 4n + 1. Is there a whole number n with 4n + 1 = 101?',
         steps=['4n + 1 = 101 means 4n = 100, so n = 25.', 'n = 25 is a whole number, so 101 is a term of the sequence.'],
         src=['Is 101 a term? Which one?  __________']),
    dict(id='3b2', tier='core', no='3(b) which', type='number', strand=ST, skill='is it a term of the sequence',
         q='Look at the sequence 5, 9, 13, 17, ... If 101 is a term, which term is it? Type its position (the 1st term is 1). If 101 is not a term, type 0.', answer=25, check=lambda: order_of(5, 4, 101),
         hint='Work backwards: 101 - 1 = 100. How many 4s make 100?',
         steps=['The rule is 4n + 1, so 4n = 101 - 1 = 100.', '100 ÷ 4 = 25.', '101 is the 25th term.'],
         src=['Is 101 a term? Which one?  __________']),
    dict(id='3c', tier='core', no='3(c)', type='choice', strand=ST, skill='is it a term of the sequence', options=['Yes', 'No'], answer='No',
         q='Look at the sequence 5, 9, 13, 17, ... Is 150 in the sequence?', check=lambda: 'Yes' if in_seq(5, 4, 150) else 'No',
         hint='Every term is 1 more than a multiple of 4. Is 150 - 1 a multiple of 4?',
         steps=['Every term is 4n + 1, so one less than a term is a multiple of 4.', '150 - 1 = 149, and 149 ÷ 4 = 37 remainder 1. It is not a multiple of 4.', 'So 150 is not a term.'],
         src=['Is 150 in the sequence? Explain.  ____________________________']),
    dict(id='3c-why', tier='core', no='3(c) explain', type='selfcheck', strand=ST, skill='explaining with the rule',
         q='Look at the sequence 5, 9, 13, 17, ... Explain how you know whether 150 is in the sequence. Write your reason, then check it against the worked solution.',
         facts=dict(minus1=149, remainder=1, even=True), check=lambda: dict(minus1=149, remainder=(150 - 1) % 4, even=(150 % 2 == 0)),
         hint='Use the rule 4n + 1, or notice something about every term of the sequence.',
         steps=['Every term is 1 more than a multiple of 4. 150 - 1 = 149 is not a multiple of 4 (149 = 4 × 37 + 1).', 'Another reason: 4n is even, so 4n + 1 is always odd. Every term is odd, and 150 is even.', 'Either reason shows 150 is not a term.'],
         src=['Is 150 in the sequence? Explain.  ____________________________']),

    dict(id='4-trace', tier='core', no='4', type='fields', strand=CO, skill='tracing code',
         q='Predict, then trace. What does this code make the sprite say? Fill in the trace table: the value of x after "change" in loops 1, 2, 3 and 4.',
         frame='x after loop 1: {f1};   loop 2: {f2};   loop 3: {f3};   loop 4: {f4}', answer=[7, 12, 17, 22], svg=fig_code(PROG4, 'Code: set x to 2, repeat 4: change x by 5, say x'),
         check=lambda: P.run(PROG4)[0], hint='x starts at 2. Each loop adds 5, then the sprite says x.',
         steps=['x starts at 2.', 'Loop 1: 2 + 5 = 7. Loop 2: 7 + 5 = 12. Loop 3: 12 + 5 = 17. Loop 4: 17 + 5 = 22.', 'The sprite says 7, 12, 17, 22.'],
         src=['Predict, then trace. What does this code make the sprite say? Fill in the trace table.']),
    dict(id='4a', tier='core', no='4(a)', type='number', strand=CO, skill='tracing code',
         q='Predict, then trace. What is the last number the sprite says?', answer=22, svg=fig_code(PROG4, 'Code: set x to 2, repeat 4: change x by 5, say x'),
         check=lambda: P.run(PROG4)[0][-1], hint='Trace the loops one at a time. The last number is what x is after loop 4.',
         steps=['The sprite says 7, 12, 17 and 22.', 'The last number it says is 22.'],
         src=['(a)  The last number it says:  ________']),
    dict(id='4b', tier='core', no='4(b)', type='number', strand=CO, skill='predicting without running',
         q='With repeat 100, what is the last number? Work it out without running the code. (How many jumps of 5 are added to the 2?)', answer=502,
         svg=fig_code(PROG4, 'Code: set x to 2, repeat 4: change x by 5, say x'), check=lambda: P.run(PROG4_100)[0][-1],
         hint='x starts at 2 and 100 jumps of 5 are added. What is 100 × 5?',
         steps=['x starts at 2.', 'With repeat 100, the code adds 5 a hundred times: 100 × 5 = 500.', '2 + 500 = 502. The last number is 502.'],
         src=['With repeat 100, what is the last number? Explain without running it.']),

    dict(id='5-plan', tier='core', no='5', type='selfcheck', paper=True, strand=CO, skill='planning code',
         q='Plan your code with these five blocks to say the first 20 terms of 4, 10, 16, 22, ...',
         svg=P.compose([(l, P.blocks(p, 'Block ' + l, 14)) for l, p in PALETTE5], 'The five blocks: 1 when green flag clicked, 2 set n to, 3 change n by, 4 repeat, 5 say n for 1 seconds', gap=8),
         facts=[4 + 6 * k for k in range(20)], check=lambda: P.run(program_for(4, 6, 20))[0],
         sol_fig=lambda f: P.compose([P.blocks(program_for(f[0], f[1] - f[0], len(f)), 'The program: set n to 4, repeat 20: say n, change n by 6')], 'The program that says the first 20 terms of 4, 10, 16, 22, ...'),
         hint='Which number does the first term need to be set to? How many terms are there? Say the number first, then change it.',
         steps=['Order: when green flag clicked, set n to 4, repeat 20 [say n for 1 seconds, change n by 6].', 'Say must come before change, because the first term (4) must be said before the first jump. (Or start n at -2 and change first.)', 'The sprite says 4, 10, 16, 22, ... and the last number is 118.'],
         src=['Take-home. Plan your code with these blocks to say the first 20 terms of  4, 10, 16, 22, …']),
    dict(id='5a', tier='core', no='5(a)', type='number', strand=CO, skill='tracing code',
         q='Your program says the first 20 terms of 4, 10, 16, 22, ... What is the last number it says?', answer=118, check=lambda: P.run(program_for(4, 6, 20))[0][-1],
         hint='It is the 20th term. The rule is 6n - 2.',
         steps=['The sequence is 4, 10, 16, 22, ... with difference 6.', 'The rule is 6n - 2, so the 20th term is 6 × 20 - 2 = 118.', 'Check: 4 + 19 × 6 = 118.'],
         src=['(a)  The last number it says:  ________']),

    dict(id='6a', tier='core', no='6(a)', type='number', strand=CO, skill='debugging code',
         q='Spot the bug. Mei wants her sprite to say the 50th term of 3, 7, 11, 15, ... Here is her code. What does her code say?', answer=203,
         svg=fig_code(MEI, 'Mei\'s code: set n to 3, repeat 50: change n by 4, then say n'), check=lambda: P.run(MEI)[0][-1],
         hint='n starts at 3 and the loop adds 4 a total of 50 times.',
         steps=['n starts at 3.', 'The loop adds 4 fifty times: 50 × 4 = 200.', '3 + 200 = 203. Her code says 203.'],
         src=['Spot the bug. Mei wants her sprite to say the 50th term of   3,  7,  11,  15,  …   Here is her code.', '(a)  Her code says:   ________']),
    dict(id='6b', tier='core', no='6(b)', type='number', strand=CO, skill='rule for the nth term',
         q='Use the rule for the nth term. The 50th term of 3, 7, 11, 15, ... is really: ______', answer=199, svg=fig_code(MEI, 'Mei\'s code: set n to 3, repeat 50: change n by 4, then say n'),
         check=lambda: P.ap(3, 4, 50)[-1], hint='Find the rule first: the difference is 4, and 4 × 1 = 4 but the first term is 3.',
         steps=['The difference is 4, so the rule is 4n - 1 (check: 4 × 1 - 1 = 3).', 'The 50th term is 4 × 50 - 1 = 199.', 'So Mei\'s 203 is too big.'],
         src=['(b)  Use the rule for the nth term.', 'The 50th term is really:   ________']),
    dict(id='6c', tier='core', no='6(c)', type='selfcheck', paper=True, strand=CO, skill='debugging code',
         q='Fix her code. Explain the bug in one sentence.', svg=fig_code(MEI, 'Mei\'s code: set n to 3, repeat 50: change n by 4, then say n'),
         facts=199, check=lambda: P.run(MEI_FIXED)[0][-1],
         sol_fig=lambda f: P.compose([P.blocks(MEI_FIXED, 'Fixed code: set n to 3, repeat 49: change n by 4, then say n')], 'Mei\'s code fixed: repeat 49'),
         hint='The 1st term is already in n before the loop starts. How many jumps are there from the 1st term to the 50th term?',
         steps=['Change repeat 50 to repeat 49.', 'The 1st term (3) is already there before the loop starts, so the 50th term is only 49 jumps away.', 'With repeat 49 the code says 3 + 49 × 4 = 199, which matches the rule.'],
         src=['Fix her code. Explain the bug in one sentence.']),

    # ---- exit slip (printed on the Finish page)
    dict(id='X-a', tier='core', no='Exit slip (a)', type='fields', strand=ST, skill='rule for the nth term',
         q='Exit slip. The sequence 8, 11, 14, 17, ... Write the rule for the nth term.', frame='nth term = {f1} × n + {f2}', answer=[3, 5], check=lambda: list(P.linear_rule([8, 11, 14, 17])),
         hint='The difference is 3. Test 3 × 1 against the 1st term, 8.',
         steps=['The difference is 3, so the rule starts with 3 × n.', '3 × 1 = 3 but the 1st term is 8, so add 5.', 'The rule is 3n + 5.'],
         src=['The sequence 8, 11, 14, 17, … (a) Write the rule for the nth term.']),
    dict(id='X-b', tier='core', no='Exit slip (b)', type='number', strand=ST, skill='finding a far term',
         q='Exit slip. The sequence 8, 11, 14, 17, ... Find the 100th term.', answer=305, check=lambda: P.ap(8, 3, 100)[-1],
         hint='Use the rule 3n + 5 with n = 100.',
         steps=['The rule is 3n + 5.', '3 × 100 + 5 = 305.', 'Check: 8 + 99 × 3 = 305.'],
         src=['(b) Find the 100th term.']),
    dict(id='X-c', tier='core', no='Exit slip (c)', type='number', strand=CO, skill='loops and jumps',
         q='Exit slip. A loop starts at the 1st term, 8. How many times must it repeat "change by 3" to reach the 100th term?', answer=99,
         check=lambda: len(P.ap(8, 3, 100)) - 1, hint='How many jumps are there from the 1st term to the 100th term?',
         steps=['The 1st term is already there before the loop starts.', 'From the 1st term to the 100th term there are 100 - 1 = 99 jumps.', 'The loop must repeat 99 times.'],
         src=['(c) A loop starts at the 1st term. How many times must it repeat "change by 3" to reach the 100th term?']),

    # ================= Investigation (printed on the Finish page)
    dict(id='I1', tier='invest', no='Investigation', type='selfcheck', paper=True, strand=ST, skill='what changes, what stays the same',
         q='What if we change the shape? Triangles in a row use 3, 5, 7, ... sticks (the rule is 2n + 1). What if we join squares in a row, or pentagons, or hexagons, sharing one side each time? '
           'Pick a shape. Draw patterns 1, 2 and 3, make a table and find the rule. What changed? What stayed the same? First step: draw 3 squares in a row and count the sticks.',
         facts={3: (2, 1), 4: (3, 1), 5: (4, 1), 6: (5, 1)},
         check=lambda: {k: (lambda s1, s2: (s2 - s1, s1 - (s2 - s1)))(P.sticks_of_polygons(k, 1), P.sticks_of_polygons(k, 2)) for k in (3, 4, 5, 6)},
         sol_fig=lambda f: table_svg(['Shape', 'Pattern 1', 'Pattern 2', 'Pattern 3', 'Rule'],
                                     [[nm, *[P.sticks_of_polygons(k, n) for n in (1, 2, 3)], f'{f[k][0]}n + {f[k][1]}'] for k, nm in ((3, 'triangle'), (4, 'square'), (5, 'pentagon'), (6, 'hexagon'))],
                                     'Sticks in a row of shapes sharing one side: triangle 2n + 1, square 3n + 1, pentagon 4n + 1, hexagon 5n + 1', [82, 72, 72, 72, 66]),
         hint='Draw pattern 1, 2 and 3 for the shape you pick. Count the sticks each time and look at how much you add.',
         steps=['Any shape you choose is fine. Here are all four: triangles 2n + 1, squares 3n + 1, pentagons 4n + 1, hexagons 5n + 1.', 'What changes: the number added each time. It is always one less than the number of sides, because a side is shared.',
                'What stays the same: the rule has the form (something) × n + 1, and pattern 1 is the single shape (k sticks).', 'A good answer has a table, names the difference, and checks the rule on pattern 1 and one more pattern.'],
         src=['What if we change the shape?', 'Triangles in a row use 3, 5, 7, … sticks (the rule is 2n + 1).']),

    # ================= Think harder
    dict(id='T1', tier='stretch', no='T1', type='number', strand=ST, skill='finding a far term',
         q='Find the 100th term of 12, 19, 26, 33, ...', answer=705, check=lambda: P.ap(12, 7, 100)[-1],
         hint='The difference is 7. Find the rule, then use n = 100.',
         steps=['The difference is 7, so the rule starts with 7n.', '7 × 1 = 7 but the 1st term is 12, so add 5. The rule is 7n + 5.', '7 × 100 + 5 = 705.'],
         src=['Find the 100th term of 12, 19, 26, 33, …']),
    dict(id='T2', tier='stretch', no='T2', type='choice', strand=ST, skill='is it a term of the sequence', options=['Yes', 'No'], answer='No',
         q='Is 200 a term of 2, 9, 16, 23, ...?', check=lambda: 'Yes' if in_seq(2, 7, 200) else 'No',
         hint='Find the rule (the difference is 7). Is there a whole number n that gives 200?',
         steps=['The rule is 7n - 5.', '7n - 5 = 200 means 7n = 205, and 205 ÷ 7 is not a whole number.', 'So 200 is not a term.'],
         src=['Is 200 a term of 2, 9, 16, 23, …? Explain.']),
    dict(id='T2-why', tier='stretch', no='T2 explain', type='selfcheck', strand=ST, skill='explaining with the rule',
         q='Is 200 a term of 2, 9, 16, 23, ...? Explain how you know. Write your reason, then check it against the worked solution.',
         facts=dict(before=(29, 198), after=(30, 205)),
         check=lambda: (lambda s: dict(before=(max(i for i, v in enumerate(s, 1) if v < 200), max(v for v in s if v < 200)), after=(min(i for i, v in enumerate(s, 1) if v > 200), min(v for v in s if v > 200))))(P.ap(2, 7, 100)),
         hint='Find the rule 7n - 5, then find which terms are just below and just above 200.',
         steps=['The rule is 7n - 5.', 'The 29th term is 7 × 29 - 5 = 198 and the 30th term is 7 × 30 - 5 = 205.', '200 is between them, so 200 is skipped. It is not a term.'],
         src=['Is 200 a term of 2, 9, 16, 23, …? Explain.']),
    dict(id='T3', tier='stretch', no='T3', type='number', strand=ST, skill='working backwards',
         q='Matchstick houses in a row: 1 house uses 6 sticks, 2 houses use 11, 3 houses use 16. How many houses can you make with 100 sticks?', answer=19,
         check=lambda: (lambda d, c: max(n for n in range(1, 200) if d * n + c <= 100))(*P.linear_rule([6, 11, 16])),
         hint='Find the rule (sticks = ? × n + ?), then find the biggest n with at most 100 sticks.',
         steps=['The difference is 5 and the rule is 5n + 1.', '19 houses use 5 × 19 + 1 = 96 sticks (4 left over).', '20 houses would need 101 sticks, which is too many. So 19 houses.'],
         src=['Matchstick houses in a row: 1 house uses 6 sticks, 2 houses use 11, 3 houses use 16. How many houses can you make with 100 sticks?']),
    dict(id='T4a', tier='stretch', no='T4(a)', type='fields', strand=ST, skill='rule for the nth term',
         q='Write the difference, the rule for the nth term and the 100th term of 9, 11, 13, 15, ...', frame='difference {f1};   nth term = {f2} × n + {f3};   100th term = {f4}',
         answer=[2, 2, 7, 207], check=lambda: rule_row([9, 11, 13, 15]),
         hint='The difference is how much you add each time. Test 2 × 1 against the 1st term, 9.',
         steps=['The difference is 2.', '2 × 1 = 2 but the 1st term is 9, so add 7. The rule is 2n + 7.', 'The 100th term is 2 × 100 + 7 = 207.'],
         src=['Write the difference, the rule for the nth term and the 100th term of (a) 9, 11, 13, 15, … and (b) 0.5, 1, 1.5, 2, …']),
    dict(id='T4b-diff', tier='stretch', no='T4(b) difference', type='text', strand=ST, skill='rule for the nth term',
         q='Write the difference of 0.5, 1, 1.5, 2, ... (a number such as 3)', accept=['0.5', '.5', '0.50', '1/2', 'half'], shown='0.5',
         check=lambda: str(float(half_diff())), hint='How much do you add to get from 0.5 to 1?',
         steps=['1 - 0.5 = 0.5, 1.5 - 1 = 0.5: the difference is 0.5.'],
         src=['(b) 0.5, 1, 1.5, 2, …']),
    dict(id='T4b-rule', tier='stretch', no='T4(b) rule', type='text', strand=ST, skill='rule for the nth term',
         q='Write the rule for the nth term of 0.5, 1, 1.5, 2, ... (for example 3n)',
         accept=['0.5n', '0.5 n', '0.5 × n', '0.5 x n', '0.5*n', 'n × 0.5', 'n x 0.5', 'n*0.5', '.5n', '0.50n', 'n/2', 'n ÷ 2', 'n / 2', '1/2 n', '1/2n', '1/2 × n', 'half of n', 'n × 1/2', 'n÷2', '0.5xn'],
         shown='0.5n', check=lambda: f'{float(half_diff())}n' if all(half_diff() * n == [Fraction(1, 2), Fraction(1), Fraction(3, 2), Fraction(2)][n - 1] for n in range(1, 5)) else None,
         hint='The 1st term is 0.5, the 2nd is 1, the 3rd is 1.5. What do you multiply n by?',
         steps=['The difference is 0.5, so the rule starts with 0.5 × n.', 'For n = 1: 0.5 × 1 = 0.5, which is the 1st term, so nothing is added.', 'The rule is 0.5n (or n ÷ 2).'],
         src=['(b) 0.5, 1, 1.5, 2, …']),
    dict(id='T4b-100', tier='stretch', no='T4(b) 100th', type='number', strand=ST, skill='finding a far term',
         q='Find the 100th term of 0.5, 1, 1.5, 2, ...', answer=50, check=lambda: int(Fraction(1, 2) * 100),
         hint='Use the rule 0.5n with n = 100.', steps=['The rule is 0.5n.', '0.5 × 100 = 50.'],
         src=['(b) 0.5, 1, 1.5, 2, …']),

    # ================= Go further
    dict(id='C1', tier='challenge', no='C1', type='selfcheck', strand=ST, skill='making a sequence puzzle',
         q='Make up your own sequence puzzle. Choose a first term and a difference, write the first four terms, then ask: "Is ___ a term?" Pick a number that is NOT a term but is close to one. Swap with a partner and explain how you know.',
         facts=dict(terms=[6, 11, 16, 21], hundred_is_term=False, nearby=(96, 101)),
         check=lambda: dict(terms=P.ap(6, 5, 4), hundred_is_term=in_seq(6, 5, 100), nearby=(max(v for v in P.ap(6, 5, 100) if v < 100), min(v for v in P.ap(6, 5, 100) if v > 100))),
         hint='Choose a first term and a difference. Write four terms. Then pick a number between two terms.',
         steps=['Open question. Example: 6, 11, 16, 21, ... (rule 5n + 1). Is 100 a term?', 'No: 100 - 1 = 99 is not a multiple of 5. The 19th term is 96 and the 20th is 101.', 'A good puzzle gives a reason from the rule or from counting jumps, not just a list.'],
         src=['Make up your own sequence puzzle. Choose a first term and a difference, write the first four terms']),
    dict(id='C2', tier='challenge', no='C2', type='set', strand=ST, skill='common terms of two sequences',
         q='Which numbers below 60 are in BOTH sequences 2, 5, 8, 11, ... and 4, 9, 14, 19, ...? Find them all and type them with a comma between.', answer=[14, 29, 44, 59],
         check=lambda: [v for v in P.ap(2, 3, 60) if v < 60 and v in P.ap(4, 5, 60)],
         hint='Write both sequences up to 59. Which numbers appear in both lists?',
         steps=['First sequence (add 3): 2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 53, 56, 59.', 'Second sequence (add 5): 4, 9, 14, 19, 24, 29, 34, 39, 44, 49, 54, 59.', 'Both have 14, 29, 44 and 59. One more than each is a multiple of both 3 and 5, so a multiple of 15.'],
         src=['Which numbers below 60 are in BOTH sequences 2, 5, 8, 11, … and 4, 9, 14, 19, …? Find them all.']),
    dict(id='C3a', tier='challenge', no='C3(a)', type='number', strand=CO, skill='tracing code',
         q='What does this code say? set t to 0, set k to 0, then repeat 5 [change k by 1, change t by k], then say t.', answer=15,
         svg=fig_code(CH3(5), 'Code: set t to 0, set k to 0, repeat 5: change k by 1, change t by k; then say t'), check=lambda: P.run(CH3(5))[0][-1],
         hint='Trace it: k goes 1, 2, 3, 4, 5, and t adds k each time.',
         steps=['t after each loop: 1, 3, 6, 10, 15.', 'It says 15 (1 + 2 + 3 + 4 + 5).'],
         src=['What does this code say?  set t to 0, set k to 0, then repeat 5 [change k by 1, change t by k], then say t. What would it say with repeat 100?']),
    dict(id='C3b', tier='challenge', no='C3(b)', type='number', strand=CO, skill='predicting without running',
         q='What would that code say with repeat 100? (set t to 0, set k to 0, then repeat 100 [change k by 1, change t by k], then say t.)', answer=5050,
         svg=fig_code(CH3(100), 'Code: set t to 0, set k to 0, repeat 100: change k by 1, change t by k; then say t'), check=lambda: P.run(CH3(100))[0][-1],
         hint='It adds 1 + 2 + 3 + ... + 100. Pair 1 with 100, 2 with 99, and so on.',
         steps=['The code adds 1 + 2 + 3 + ... + 100.', 'Pair 1 + 100, 2 + 99, ... to make 50 pairs, each adding up to 101.', '50 × 101 = 5050.'],
         src=['What would it say with repeat 100?']),
]

# ---------------------------------------------------------------- variant families (every combination is run against an independent oracle at build time)
VARIANTS = {
    '1c': dict(base=dict(n=100),
               tpl=dict(vars=dict(n=[10, 20, 25, 30, 40, 50, 100, 200]),
                        q='Matchstick squares in a row: pattern 1 has 4 sticks, pattern 2 has 7 sticks, pattern 3 has 10 sticks. How many sticks does pattern {n} have?',
                        answer='3*n+1', hint='Each new square adds 3 sticks. Use sticks = 3 × n + 1.',
                        steps=['The rule is sticks = 3 × n + 1.', '3 × {n} + 1 = {ans}.']),
               oracle=lambda e: P.sticks_of_squares(e['n'])),
    'T1': dict(base=dict(a=12, d=7),
               tpl=dict(vars=dict(a=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], d=[3, 4, 5, 6, 7, 8, 9]), derive=dict(b='a+d', c='a+2*d', e='a+3*d'),
                        q='Find the 100th term of {a}, {b}, {c}, {e}, ...', answer='a+99*d',
                        hint='The difference is {d}. The 100th term is 99 jumps after the 1st term.',
                        steps=['The difference is {d}. There are 99 jumps from the 1st term to the 100th term.', '{a} + 99 × {d} = {ans}.']),
               oracle=lambda e: P.ap(e['a'], e['d'], 100)[-1]),
    '3a': dict(base=dict(a=5, d=4),
               tpl=dict(vars=dict(a=[6, 7, 8, 9, 10, 11, 12, 13], d=[2, 3, 4, 5]), derive=dict(b='a+d', c='a+2*d', e='a+3*d'),
                        q='Look at the sequence {a}, {b}, {c}, {e}, ... (each term is {d} more than the one before). Write the rule for the nth term.',
                        frame='nth term = {f1} × n + {f2}', answers=dict(f1='d', f2='a-d'),
                        hint='The number in front of n is {d}. Test the rule on the 1st term, {a}.',
                        steps=['Each term is {d} more than the one before, so the rule starts with {d} × n.', 'For n = 1: {d} × 1 is {d}, but the 1st term is {a}, so add {a} - {d}.', 'The answers are {ans}.']),
               oracle=lambda e: dict(zip(('f1', 'f2'), P.linear_rule(P.ap(e['a'], e['d'], 4))))),
}
