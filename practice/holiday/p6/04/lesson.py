"""Online practice for Level 6 (Primary 6, ages 11-13) holiday lesson 4: Algebra Machines (expressions and simple equations; input, rule, output).

The questions are the ones printed in the Level 6 holiday workbook (p6/content/l4.js workbook(): Start here Q1 to Q7; the Finish page: the Investigation
(p6/content/gaps.json lesson 4) and the exit slip (l4.js lesson.exit); Think harder = the first four l4.js qbank.stretch questions; Go further = the last three
l4.js qbank.challenge questions).  Every answer is recomputed by an INDEPENDENT checker below (loops that run the machine on the numbers in the question, the
block-program interpreter w2lib.run for the code questions, and an evaluator that tests every accepted writing of an algebra rule; never a copy of the printed answer).
build_holiday.py stops if a checker and the printed answer differ.  Scratch is not run in the page: the code is drawn as blocks and traced on paper or in the head.
"""
import os, re, sys
HERE_ = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE_, '..'))
sys.path.insert(0, os.path.join(HERE_, '..', '..'))
from hlib import *      # noqa: E402,F401
import p6lib as P       # noqa: E402
import w2lib as W       # noqa: E402

M = W.MINUS
META = dict(level=6, lesson=4, key='p6', title='Algebra Machines', workbook_title='ALGEBRA MACHINES', topic='Expressions and Equations', strand='Patterns and algebra',
            sources=['p6/content/l4.js', 'p6/content/gaps.json'],
            intro=['You do not need Scratch on this page. The code is drawn as blocks: read it, trace it on paper or in your head, and type what the sprite says. In Scratch, * means times.',
                   'A rule such as 3n + 2 means: times 3, then add 2. If a rule takes a number away, type that number with a minus sign (for example -2).',
                   'Write a rule with the letter n. You may type 3n + 2 or 3 x n + 2 or n x 3 + 2.'])
AL, CO = 'Patterns and algebra', 'Coding and algebra'


# ---------------------------------------------------------------- independent machinery
def apply_ops(ops, n):
    """Runs a machine given as steps such as ['+ 3', '× 4'] on the number n."""
    for o in ops:
        sym, val = o.split()
        val = int(val)
        n = {'+': n + val, '-': n - val, '−': n - val, '×': n * val, '÷': n // val}[sym]
    return n


def rule_of(ins, outs):
    """(a, b) with OUT = a * IN + b, checked on every pair given (None entries are the gaps)."""
    pts = [(i, o) for i, o in zip(ins, outs) if o is not None and i is not None]
    (x1, y1), (x2, y2) = pts[0], pts[1]
    a = (y2 - y1) // (x2 - x1)
    b = y1 - a * x1
    assert all(a * i + b == o for i, o in pts), 'the pairs do not fit one rule'
    return a, b


def trick(n):
    """Think of a number. Add 5. Double it. Take away 4. Halve it. Take away the number you first thought of."""
    v = n + 5
    v = v * 2
    v = v - 4
    v = v // 2
    return v - n


HAT = [0, 'event', 'when green flag clicked']
ASK = [HAT, [0, 'looks', 'ask [IN?] and wait'], [0, 'var', 'set out to [(answer * 2) − 7]'], [0, 'looks', 'say [out]']]
LOOP = lambda r, say='(n * 4) + 1': [HAT, [0, 'var', 'set n to [1]'], [0, 'control', f'repeat [{r}]'], [1, 'looks', f'say [{say}] for [1] seconds'], [1, 'var', 'change n by [1]']]
SEARCH = [HAT, [0, 'var', 'set n to [    ]'], [0, 'control', 'repeat until [(n * 8) − 5 = ___]'], [1, 'var', 'change n by [    ]'], [0, 'looks', 'say [n]']]
Q6_TEXT = 'Plan a search. Find n when 8n - 5 = 91 by trying n = 0, 1, 2, 3 ...'


def code(prog, label):
    return W.blocks(prog, label, 17)


def fig_table(ins, outs, label):
    return W.in_out(ins, outs, label)


def trick_fig():
    steps = ['Think of a number', 'Add 5', 'Double it', 'Take away 4', 'Halve it', ['Take away the number', 'you first thought of']]
    b, y = '', 4
    for k, s in enumerate(steps):
        lines = s if isinstance(s, list) else [s]
        h = 18 + 20 * len(lines)
        b += W.rect(8, y, 284, h, W.YEL if k == 0 else '#fff', W.NAVY, 2, 8) + W.T(26, y + h / 2 + 5 - (10 if len(lines) == 2 else 0), str(k + 1) + '.', 16, 'middle', 800, W.TEAL)
        for j, ln in enumerate(lines):
            b += W.T(46, y + 24 + 20 * j, ln, 16, 'start', 700)
        y += h
        if k < len(steps) - 1:
            b += W.line(150, y, 150, y + 12, 2.5) + f'<polygon points="150,{y + 16} 144,{y + 7} 156,{y + 7}" fill="{W.NAVY}"/>'
            y += 16
    return W.wrap(b, 300, y + 6, 'The number trick in six steps: 1 think of a number, 2 add 5, 3 double it, 4 take away 4, 5 halve it, 6 take away the number you first thought of')


def ages_fig():
    return W.age_bars('Not to scale. Bars for the ages now (Mei is 1 part, her mother 3 parts) and in 12 years (each bar has a shaded extra part for 12 years)')


T1_IN, T1_OUT = [1, 2, 3, 4], [1, 7, 13, 19]
MACHINES_PQ = [('Machine P', ['+ 3', '× 4']), ('Machine Q', ['× 4', '+ 3'])]
MACHINES_AB = [('Machine A', ['× 2', '+ 10']), ('Machine B', ['+ 5', '× 2'])]
P_RULE = lambda n: apply_ops(['+ 3', '× 4'], n)
Q_RULE = lambda n: apply_ops(['× 4', '+ 3'], n)
FORMS_P = ['(n+3)×4', '4(n+3)', '4×(n+3)', '(3+n)×4', '4×(3+n)', '4(3+n)', '(n+3)4', '(n+3)*4', '4*(n+3)', '4n+12', '4×n+12', 'n×4+12', '12+4n', '12+4×n', '12+n×4', '4*n+12']
FORMS_Q = ['4n+3', '4×n+3', 'n×4+3', '3+4n', '3+4×n', '3+n×4', '4*n+3', 'n*4+3', '(n×4)+3', '(4×n)+3', '3+(4×n)', '3+(n×4)', '(4n)+3']
FORMS_2N6 = ['2n+6', '2×n+6', 'n×2+6', '6+2n', '6+2×n', '6+n×2', '2*n+6', '(2n)+6', '(2×n)+6', '2(n+3)', '2×(n+3)', '(n+3)×2', '(n+3)2', '2(3+n)', '2×(3+n)', '(3+n)×2']
FORMS_N3 = ['n+3', '3+n', '(n+3)', '(3+n)']

ITEMS = [
    # ================= Start here (workbook Lesson 4, Q1 to Q7)
    dict(id='1a', tier='core', no='1(a)', type='fields', strand=AL, skill='finding a rule from a table',
         q='Guess my rule. Fill in the gaps. Write each rule with n. IN 1, 2, 3, 4 give OUT 4, 5, 6, 7.',
         frame='OUT = n + {f1};   OUT for IN 10 = {f2}', answer=[3, 13], svg=fig_table([1, 2, 3, 4, 10], [4, 5, 6, 7, None], 'Table: IN 1, 2, 3, 4 and 10; OUT 4, 5, 6, 7 and a gap for IN 10'),
         check=lambda: (lambda ab: [ab[1], ab[0] * 10 + ab[1]] if ab[0] == 1 else None)(rule_of([1, 2, 3, 4], [4, 5, 6, 7])),
         hint='How much bigger is each OUT than its IN? Is it the same for every pair?',
         steps=['OUT is 3 more than IN each time: 1 gives 4, 2 gives 5, 3 gives 6, 4 gives 7.', 'The rule is OUT = n + 3.', 'For IN 10: 10 + 3 = 13.'],
         src=['Guess my rule. Fill in the gaps.']),
    dict(id='1b', tier='core', no='1(b)', type='fields', strand=AL, skill='finding a rule from a table',
         q='Guess my rule. Write the rule with n, then find the missing OUT. IN 1, 2, 3, 4 give OUT 6, 9, 12, 15.',
         frame='OUT = {f1} × n + {f2};   OUT for IN 10 = {f3}', answer=[3, 3, 33], svg=fig_table([1, 2, 3, 4, 10], [6, 9, 12, 15, None], 'Table: IN 1, 2, 3, 4 and 10; OUT 6, 9, 12, 15 and a gap for IN 10'),
         check=lambda: (lambda ab: [ab[0], ab[1], ab[0] * 10 + ab[1]])(rule_of([1, 2, 3, 4], [6, 9, 12, 15])),
         hint='How much does OUT go up each time IN goes up by 1? That is the number in front of n. Then test the rule on the first pair.',
         steps=['OUT goes up by 3 each time, so the rule starts with 3 × n.', 'For IN 1: 3 × 1 = 3, but OUT is 6, so add 3. The rule is OUT = 3n + 3.', 'For IN 10: 3 × 10 + 3 = 33.'],
         src=['Guess my rule. Fill in the gaps.']),
    dict(id='1c', tier='core', no='1(c)', type='fields', strand=AL, skill='finding a rule from a table',
         q='Guess my rule. Write the rule with n, then find the missing IN. IN 1, 2, 3, 4 give OUT 3, 8, 13, 18, and some IN gives OUT 48. (Type a minus sign if the rule takes a number away.)',
         frame='OUT = {f1} × n + {f2};   IN for OUT 48 = {f3}', answer=[5, -2, 10], svg=fig_table([1, 2, 3, 4, None], [3, 8, 13, 18, 48], 'Table: IN 1, 2, 3, 4 and a gap; OUT 3, 8, 13, 18 and 48'),
         check=lambda: (lambda ab: [ab[0], ab[1], next(i for i in range(1, 500) if ab[0] * i + ab[1] == 48)])(rule_of([1, 2, 3, 4], [3, 8, 13, 18])),
         hint='Find how much OUT goes up each time IN goes up by 1. Test that times n on the first pair: do you need to add or take away?',
         steps=['OUT goes up by 5 each time, so the rule starts with 5 × n.', f'For IN 1: 5 × 1 = 5, but OUT is 3, so take away 2. The rule is OUT = 5n {M} 2.', f'For OUT 48: 48 + 2 = 50, and 50 ÷ 5 = 10. IN is 10. (Check: 5 × 10 {M} 2 = 48.)'],
         src=['Guess my rule. Fill in the gaps.']),
    dict(id='1d', tier='core', no='1(d)', type='fields', strand=AL, skill='finding a rule from a table',
         q='Guess my rule. Write the rule with n, then find the missing OUT. IN 1, 2, 3, 4 give OUT 1, 5, 9, 13. (Type a minus sign if the rule takes a number away.)',
         frame='OUT = {f1} × n + {f2};   OUT for IN 20 = {f3}', answer=[4, -3, 77], svg=fig_table([1, 2, 3, 4, 20], [1, 5, 9, 13, None], 'Table: IN 1, 2, 3, 4 and 20; OUT 1, 5, 9, 13 and a gap for IN 20'),
         check=lambda: (lambda ab: [ab[0], ab[1], ab[0] * 20 + ab[1]])(rule_of([1, 2, 3, 4], [1, 5, 9, 13])),
         hint='Find how much OUT goes up each time IN goes up by 1. Test that times n on the first pair.',
         steps=['OUT goes up by 4 each time, so the rule starts with 4 × n.', f'For IN 1: 4 × 1 = 4, but OUT is 1, so take away 3. The rule is OUT = 4n {M} 3.', f'For IN 20: 4 × 20 {M} 3 = 77.'],
         src=['Guess my rule. Fill in the gaps.']),

    dict(id='2a', tier='core', no='2(a)', type='fields', strand=AL, skill='order of steps', svg=W.machine_rows(MACHINES_PQ, 'Machine P: n, add 3, times 4, OUT. Machine Q: n, times 4, add 3, OUT.'),
         q='Two machines use the same steps in a different order. Put in 5. What does each machine give?', frame='Machine P gives {f1};   Machine Q gives {f2}', answer=[32, 23],
         check=lambda: [apply_ops(['+ 3', '× 4'], 5), apply_ops(['× 4', '+ 3'], 5)],
         hint='Do the steps in the order of the boxes. Machine P: start with 5 and do its first step, then its second step.',
         steps=['Machine P: 5 + 3 = 8, then 8 × 4 = 32.', 'Machine Q: 5 × 4 = 20, then 20 + 3 = 23.', 'The same steps in a different order give different answers.'],
         src=['Put in 5.']),
    dict(id='2b-P', algebra=True, var='n', tier='core', no='2(b) P', type='text', strand=AL, skill='writing a rule with a letter', svg=W.machine_rows(MACHINES_PQ, 'Machine P: n, add 3, times 4, OUT. Machine Q: n, times 4, add 3, OUT.'),
         q='Write the rule for Machine P with n. Type it like this: OUT = 3n + 2 (that is a different machine).',
         accept=W.verified_forms(FORMS_P, P_RULE), shown='(n + 3) × 4', check=lambda: FORMS_P[0] if all(W._eval_form(f, k) == P_RULE(k) for f in FORMS_P for k in range(-5, 20)) else None,
         hint='Write the steps in order, starting with n. Does the second step work on n, or on the answer of the first step?',
         steps=['Machine P adds 3 to n first: n + 3.', 'Then it multiplies that whole answer by 4, so the first step needs brackets: (n + 3) × 4.', 'The rule is OUT = (n + 3) × 4, which is the same as 4n + 12.'],
         src=['Write each rule with n.']),
    dict(id='2b-Q', algebra=True, var='n', tier='core', no='2(b) Q', type='text', strand=AL, skill='writing a rule with a letter', svg=W.machine_rows(MACHINES_PQ, 'Machine P: n, add 3, times 4, OUT. Machine Q: n, times 4, add 3, OUT.'),
         q='Write the rule for Machine Q with n. Type it like this: OUT = 3n + 2 (that is a different machine).',
         accept=W.verified_forms(FORMS_Q, Q_RULE), shown='4n + 3', check=lambda: FORMS_Q[0] if all(W._eval_form(f, k) == Q_RULE(k) for f in FORMS_Q for k in range(-5, 20)) else None,
         hint='Write the steps in order, starting with n. Which step comes first in Machine Q?',
         steps=['Machine Q multiplies n by 4 first: 4n.', 'Then it adds 3.', 'The rule is OUT = 4n + 3.'],
         src=['Write each rule with n.']),
    dict(id='2c', tier='core', no='2(c)', type='choice', strand=AL, skill='comparing two rules', options=['Yes', 'No'], answer='No', svg=W.machine_rows(MACHINES_PQ, 'Machine P: n, add 3, times 4, OUT. Machine Q: n, times 4, add 3, OUT.'),
         q='Can Machine P and Machine Q ever give the same OUT for the same IN?',
         check=lambda: 'Yes' if any(P_RULE(k / 4) == Q_RULE(k / 4) for k in range(-400, 400)) else 'No',
         hint='Try a few different IN numbers in both machines and compare each pair of answers. Is there a pattern?',
         steps=['Put in 5: P gives 32, Q gives 23. Put in 0: P gives 12, Q gives 3. Put in 10: P gives 52, Q gives 43.', 'The two OUT numbers are never the same: P is always bigger than Q by the same amount.'],
         src=['Can P and Q ever give the same OUT for the same IN?']),
    dict(id='2c-why', tier='core', no='2(c) explain', type='selfcheck', strand=AL, skill='explaining with the rule', svg=W.machine_rows(MACHINES_PQ, 'Machine P: n, add 3, times 4, OUT. Machine Q: n, times 4, add 3, OUT.'),
         q='Explain what you find when you compare the rules of Machine P and Machine Q, and say how that answers 2(c). Write your reason, then check it against the worked solution.',
         facts=dict(gap=9), check=lambda: dict(gap=(lambda g: g.pop() if len(g) == 1 else None)({P_RULE(k) - Q_RULE(k) for k in range(-50, 100)})),
         hint='Write each machine as a rule with n, as in 2(b). Then multiply out any brackets and compare the two rules. What is different?',
         steps=['Machine P is (n + 3) × 4 = 4n + 12 (4 lots of n and 4 lots of 3).', 'Machine Q is 4n + 3.', 'Both have 4n, but P adds 12 and Q adds only 3. So P is always 12 - 3 = 9 more than Q, and they can never be equal.'],
         src=['Explain.']),

    dict(id='3a', tier='core', no='3(a)', type='number', strand=AL, skill='running a machine backwards', answer=8,
         q=f'Run each machine backwards to find n. Then check by going forwards. n → × 6 → {M} 5 → 43. What is n?', check=lambda: next(n for n in range(0, 1000) if n * 6 - 5 == 43),
         hint='Undo the last step first. What is the opposite of taking away 5?',
         steps=[f'The machine did × 6, then {M} 5, and OUT is 43.', 'Undo the last step first: 43 + 5 = 48. Then undo × 6: 48 ÷ 6 = 8.', f'n = 8. Check forwards: 8 × 6 = 48, 48 {M} 5 = 43.'],
         src=['Run each machine backwards to find n.']),
    dict(id='3b', tier='core', no='3(b)', type='number', strand=AL, skill='solving a simple equation', answer=10,
         q='Run the machine backwards to find n. Then check by going forwards. 7n + 4 = 74. What is n?', check=lambda: next(n for n in range(0, 1000) if 7 * n + 4 == 74),
         hint='7n + 4 means times 7, then add 4. Undo the last step first.',
         steps=['7n + 4 = 74 means the machine does × 7, then + 4.', 'Undo + 4 first: 74 - 4 = 70. Then undo × 7: 70 ÷ 7 = 10.', 'n = 10. Check forwards: 7 × 10 + 4 = 74.'],
         src=['Run each machine backwards to find n.']),
    dict(id='3c', tier='core', no='3(c)', type='number', strand=AL, skill='solving a simple equation', answer=12,
         q='Run the machine backwards to find n. Then check by going forwards. (n − 3) × 5 = 45. What is n?', check=lambda: next(n for n in range(0, 1000) if (n - 3) * 5 == 45),
         hint='The brackets mean n − 3 is done first, then × 5. Undo the last step first.',
         steps=[f'(n {M} 3) × 5 = 45 means the machine does {M} 3, then × 5.', f'Undo × 5 first: 45 ÷ 5 = 9. Then undo {M} 3: 9 + 3 = 12.', f'n = 12. Check forwards: (12 {M} 3) × 5 = 9 × 5 = 45.'],
         src=['Run each machine backwards to find n.']),
    dict(id='3d', tier='core', no='3(d)', type='number', strand=AL, skill='solving a simple equation', answer=24,
         q='Run the machine backwards to find n. Then check by going forwards. n ÷ 4 + 9 = 15. What is n?', check=lambda: next(n for n in range(0, 1000) if n / 4 + 9 == 15),
         hint='The machine does ÷ 4, then + 9. Undo the last step first.',
         steps=['n ÷ 4 + 9 = 15 means the machine does ÷ 4, then + 9.', f'Undo + 9 first: 15 {M} 9 = 6. Then undo ÷ 4: 6 × 4 = 24.', 'n = 24. Check forwards: 24 ÷ 4 = 6, 6 + 9 = 15.'],
         src=['Run each machine backwards to find n.']),

    dict(id='4a', tier='core', no='4(a)', type='number', strand=CO, skill='predicting what code says', answer=13, svg=code(ASK, 'Code: ask IN? and wait, set out to answer times 2 minus 7, say out'),
         q='Predict what the code says. (In Scratch, * means ×.) You type 10. What does it say?', check=lambda: W.run(ASK, answer=10)[0][-1],
         hint='"answer" is the number you type. Put it into the block "set out to ( )" and work it out.',
         steps=['answer = 10.', f'out = (10 × 2) {M} 7 = 20 {M} 7 = 13.', 'The sprite says 13.'],
         src=['Predict what the code says.']),
    dict(id='4b', tier='core', no='4(b)', type='number', strand=CO, skill='predicting what code says', answer=-1, svg=code(ASK, 'Code: ask IN? and wait, set out to answer times 2 minus 7, say out'),
         q='Predict what the code says. (In Scratch, * means ×.) You type 3. What does it say?', check=lambda: W.run(ASK, answer=3)[0][-1],
         hint='Put your typed number into the block "set out to ( )". Do the times first, then the take away.',
         steps=['answer = 3.', f'out = (3 × 2) {M} 7 = 6 {M} 7 = {M}1.', f'The sprite says {M}1.'],
         src=['You type 3. It says']),
    dict(id='4c', tier='core', no='4(c)', type='number', strand=CO, skill='running a machine backwards', answer=16, svg=code(ASK, 'Code: ask IN? and wait, set out to answer times 2 minus 7, say out'),
         q='Predict what the code says. (In Scratch, * means ×.) To make it say 25, what number must you type?',
         check=lambda: next(a for a in range(-100, 200) if W.run(ASK, answer=a)[0][-1] == 25),
         hint='Run the machine backwards from 25. Undo the last step first.',
         steps=[f'The machine does × 2, then {M} 7, and the sprite says 25.', f'Undo {M} 7: 25 + 7 = 32. Undo × 2: 32 ÷ 2 = 16.', f'Type 16. Check: 16 × 2 {M} 7 = 25.'],
         src=['To make it say 25, type']),

    dict(id='5-n', tier='core', no='5 table (n)', type='fields', strand=CO, skill='tracing a loop', svg=code(LOOP(4), 'Code: set n to 1, repeat 4: say n times 4 plus 1, change n by 1'),
         q='Trace the code. Fill in the table: the value of n in each repeat (in repeat 1, n is 1).',
         frame='n in repeat 2: {f1};   repeat 3: {f2};   repeat 4: {f3}', answer=[2, 3, 4],
         check=lambda: [W.run(LOOP(4, 'n'))[0][k] for k in (1, 2, 3)],
         hint='The sprite says first, then n goes up by 1. What is n at the start of repeat 2?',
         steps=['n starts at 1 and goes up by 1 after each "say".', 'So n is 1, 2, 3, 4 in repeats 1 to 4.'],
         src=['Trace the code. Fill in the table.']),
    dict(id='5-says', tier='core', no='5 table (says)', type='fields', strand=CO, skill='tracing a loop', svg=code(LOOP(4), 'Code: set n to 1, repeat 4: say n times 4 plus 1, change n by 1'),
         q='Trace the code. Fill in the table: what the sprite says in each repeat.',
         frame='it says in repeat 1: {f1};   repeat 2: {f2};   repeat 3: {f3};   repeat 4: {f4}', answer=[5, 9, 13, 17],
         check=lambda: W.run(LOOP(4))[0],
         hint='In each repeat the sprite says (n × 4) + 1, using the n of that repeat.',
         steps=['The sprite says (n × 4) + 1: 4 × 1 + 1 = 5, 4 × 2 + 1 = 9, 4 × 3 + 1 = 13, 4 × 4 + 1 = 17.', 'The table reads 5, 9, 13, 17.'],
         src=['Trace the code. Fill in the table.']),
    dict(id='5b', tier='core', no='5(b)', type='fields', strand=CO, skill='writing a rule with a letter', svg=code(LOOP(4), 'Code: set n to 1, repeat 4: say n times 4 plus 1, change n by 1'),
         q='Trace the code. What is the rule for what it says? Write it with n.', frame='it says {f1} × n + {f2}', answer=[4, 1],
         check=lambda: list(P.linear_rule(W.run(LOOP(4))[0])), hint='Look at the block "say ( )". It tells you the rule.',
         steps=['The sprite says (n × 4) + 1, which is 4 × n + 1.', 'Check with the table: 4 × 1 + 1 = 5, 4 × 2 + 1 = 9, 4 × 3 + 1 = 13.', 'The rule is 4n + 1.'],
         src=['The rule: it says']),
    dict(id='5c', tier='core', no='5(c)', type='number', strand=CO, skill='predicting without running', answer=41, svg=code(LOOP(4), 'Code: set n to 1, repeat 4: say n times 4 plus 1, change n by 1'),
         q='With repeat 10 instead of repeat 4, what is the last number the sprite says?', check=lambda: W.run(LOOP(10))[0][-1],
         hint='The last number is what it says in repeat 10. Use the rule.',
         steps=['In repeat 10, n is 10.', 'The sprite says (10 × 4) + 1 = 41.', 'The last number is 41.'],
         src=['With repeat 10, the last number is']),

    dict(id='6a', tier='core', no='6(a)', type='fields', strand=CO, skill='planning a search loop', svg=code(SEARCH, 'Search plan with blanks: set n to blank, repeat until n times 8 minus 5 equals blank, change n by blank, say n'),
         q='Plan a search. Find n when 8n − 5 = 91 by trying n = 0, 1, 2, 3 ... Fill in the three blanks of the plan.', frame='set n to {f1};   repeat until (n × 8) − 5 = {f2};   change n by {f3}', answer=[0, 91, 1],
         check=lambda: (lambda t: [0, t, 1] if W.run(W.fill(SEARCH, [0, t, 1]))[1]['n'] * 8 - 5 == t else None)(int(re.search(r'= (\d+)', Q6_TEXT).group(1))),
         hint='You try n = 0 first, then 1, 2, 3 ... What does n start at, and how much does it change each time? What number is the loop looking for?',
         steps=['The search tries n = 0, 1, 2, 3 ..., so set n to 0 and change n by 1.', 'It must stop when 8n − 5 is 91, so repeat until (n × 8) − 5 = 91.', 'The loop stops at the first n that works.'],
         src=['Plan a search.']),
    dict(id='6b', tier='core', no='6(b)', type='number', strand=CO, skill='tracing a search loop', answer=12,
         q='Plan a search. The search tries n = 0, 1, 2, 3 ... and stops at the first n that makes (n × 8) − 5 equal to 91. Then it says n. What will it say?', check=lambda: W.run(W.fill(SEARCH, [0, 91, 1]))[0][-1],
         hint='The loop stops at the first n where (n × 8) − 5 is 91. You do not need to try every n: how could you find it by running the machine backwards?',
         steps=['The loop stops when (n × 8) − 5 = 91.', 'Backwards: 91 + 5 = 96, and 96 ÷ 8 = 12.', 'n = 12, so the sprite says 12.'],
         src=['(b) What will it say?']),
    dict(id='6c', tier='core', no='6(c)', type='fields', strand=CO, skill='running a machine backwards', answer=[96, 12],
         q='Check by running the machine backwards from 91. The machine does × 8, then − 5.', frame='After undoing − 5 you have {f1};   after undoing × 8 you have {f2}',
         check=lambda: (lambda a: [a, a // 8] if a % 8 == 0 else None)(91 + 5),
         hint='Undo the last step first. What is the opposite of taking away 5?',
         steps=[f'Undo {M} 5: 91 + 5 = 96.', 'Undo × 8: 96 ÷ 8 = 12.', 'The answer is the same as the search found.'],
         src=['(c) Check by running the machine']),

    dict(id='7a', tier='core', no='7(a)', type='fields', strand=AL, skill='testing a number trick', svg=trick_fig(),
         q='Bonus question: the number trick. Follow the six steps in the picture. Try it with 7, then try it with 10.', frame='With 7 you get {f1};   with 10 you get {f2}', answer=[3, 3],
         check=lambda: [trick(7), trick(10)], hint='Do the steps one at a time, in order. Write the number you have after each step.',
         steps=['Start with 7: add 5 = 12, double it = 24, take away 4 = 20, halve it = 10, take away 7 = 3.', 'Start with 10: add 5 = 15, double it = 30, take away 4 = 26, halve it = 13, take away 10 = 3.', 'Both give 3.'],
         src=['The number trick.']),
    dict(id='7b1', algebra=True, var='n', tier='core', no='7(b) step 4', type='text', strand=AL, skill='explaining a trick with a letter', svg=trick_fig(),
         q='Now use n for the number you think of. After "add 5" you have n + 5, and after "double it" you have 2n + 10. What do you have after "take away 4"?',
         accept=W.verified_forms(FORMS_2N6, lambda n: 2 * n + 6), shown='2n + 6', check=lambda: FORMS_2N6[0] if all(W._eval_form(f, k) == 2 * k + 10 - 4 for f in FORMS_2N6 for k in range(-5, 20)) else None,
         hint='Start from 2n + 10 and take 4 away. Which part of it changes?',
         steps=['Start from 2n + 10.', 'Take away 4: 2n + 10 − 4 = 2n + 6.'],
         src=['Use n:']),
    dict(id='7b2', algebra=True, var='n', tier='core', no='7(b) step 5', type='text', strand=AL, skill='explaining a trick with a letter', svg=trick_fig(),
         q='Use n for the number you think of. After "add 5" you have n + 5, and after "double it" you have 2n + 10. What do you have after "halve it"? (Do "take away 4" first.)',
         accept=W.verified_forms(FORMS_N3, lambda n: n + 3), shown='n + 3', check=lambda: FORMS_N3[0] if all(W._eval_form(f, k) == (2 * k + 6) // 2 for f in FORMS_N3 for k in range(-5, 20)) else None,
         hint='Halving a sum means halving each part of it.',
         steps=['Halve 2n + 6: half of 2n is n, and half of 6 is 3.', 'You have n + 3.'],
         src=['Use n:']),
    dict(id='7b3', tier='core', no='7(b) step 6', type='number', strand=AL, skill='explaining a trick with a letter', svg=trick_fig(), answer=3,
         q='Use n for the number you think of. After "add 5" you have n + 5, and after "double it" you have 2n + 10. What do you have at the end, after the last step "take away the number you first thought of"?',
         check=lambda: (lambda vals: vals.pop() if len(set(vals)) == 1 else None)([(k + 3) - k for k in range(-10, 40)]),
         hint='Do the steps one at a time with n. At the end, what happens to the n?',
         steps=['Take away n from n + 3: n + 3 − n = 3.', 'You have 3, which does not depend on n.'],
         src=['Use n:']),
    dict(id='7c', tier='core', no='7(c)', type='selfcheck', strand=AL, skill='explaining with algebra', svg=trick_fig(),
         q='Explain why you always get the same answer in the number trick. Write your reason, then check it against the worked solution.',
         facts=dict(always=3), check=lambda: dict(always=(lambda s: s.pop() if len(s) == 1 else None)({trick(k) for k in range(0, 500)})),
         hint='Use your steps with n. What happens to the n at the end?',
         steps=['With n, the steps are n → n + 5 → 2n + 10 → 2n + 6 → n + 3 → 3.', 'The last step takes away the number you started with, so the n disappears.', 'Whatever number you think of, you end up with 3.'],
         src=['Explain why you always get the same answer.']),

    # ---- exit slip (printed on the Finish page)
    dict(id='X-a', tier='core', no='Exit slip (a)', type='number', strand=AL, skill='running a machine', answer=29,
         q='A machine does × 4, then + 5. IN 6: what is OUT?', check=lambda: apply_ops(['× 4', '+ 5'], 6),
         hint='Do the steps in order on 6: first the times, then the add.', steps=['6 × 4 = 24.', '24 + 5 = 29.', 'OUT is 29.'],
         src=['A machine does × 4, then + 5.']),
    dict(id='X-b', tier='core', no='Exit slip (b)', type='number', strand=AL, skill='running a machine backwards', answer=10,
         q='A machine does × 4, then + 5. OUT 45: what was IN?', check=lambda: next(n for n in range(0, 1000) if apply_ops(['× 4', '+ 5'], n) == 45),
         hint='Run the machine backwards. Undo the last step first.', steps=[f'Undo + 5: 45 {M} 5 = 40.', 'Undo × 4: 40 ÷ 4 = 10.', 'IN was 10. Check: 10 × 4 + 5 = 45.'],
         src=['OUT 45: what was IN?']),

    # ================= Investigation (printed on the Finish page)
    dict(id='I1', tier='invest', no='Investigation', type='selfcheck', strand=AL, skill='finding all the machines',
         q='Find all the machines. A machine does "× a number, then + a number". Use whole numbers: the × number is from 1 to 9 and the + number is from 0 to 9. Find ALL the machines that turn IN 4 into OUT 17. What pattern do you spot in your answers? Then try IN 4 and OUT 21. First step: try × 2. Then 4 × 2 = 8. What must be added to 8 to make 17?',
         facts={17: [(2, 9), (3, 5), (4, 1)], 21: [(3, 9), (4, 5), (5, 1)]},
         check=lambda: {out: [(a, out - 4 * a) for a in range(1, 10) if 0 <= out - 4 * a <= 9] for out in (17, 21)},
         sol_fig=lambda f: W.table_svg(['IN 4, OUT', '× number', '+ number'], [[str(o), str(a), str(b)] for o in (17, 21) for a, b in f[o]], 'The machines: OUT 17 from times 2 plus 9, times 3 plus 5, times 4 plus 1; OUT 21 from times 3 plus 9, times 4 plus 5, times 5 plus 1', [100, 100, 100], 16, 32),
         hint='Try the × number 1, then 2, then 3 ... in order. For each, ask what must be added to 4 × that number to make 17. Is that + number allowed?',
         steps=['IN 4, OUT 17: × 2 then + 9, × 3 then + 5, × 4 then + 1. That is exactly three machines. (× 1 would need + 13 and × 5 would need −3: neither is allowed.)', 'IN 4, OUT 21: × 3 then + 9, × 4 then + 5, × 5 then + 1: again three machines.',
                'The pattern: each time the × number goes up by 1, the + number goes down by 4, because IN is 4 and the total must stay the same.', 'A good answer works in order (× 1, × 2, × 3, ...), checks each machine on IN 4, and explains the "down by 4".'],
         src=['Open investigation', 'Find ALL the machines']),

    # ================= Think harder (first four Think harder questions of the workbook)
    dict(id='T1', tier='stretch', no='T1', type='fields', strand=AL, skill='finding a rule from a table', svg=fig_table([1, 2, 3, 4, 20], [1, 7, 13, 19, None], 'Table: IN 1, 2, 3, 4 and 20; OUT 1, 7, 13, 19 and a gap for IN 20'),
         q='IN 1, 2, 3, 4 gives OUT 1, 7, 13, 19. Find the rule. What is OUT when IN is 20? (Type a minus sign if the rule takes a number away.)',
         frame='OUT = {f1} × n + {f2};   OUT for IN 20 = {f3}', answer=[6, -5, 115], check=lambda: (lambda ab: [ab[0], ab[1], ab[0] * 20 + ab[1]])(rule_of(T1_IN, T1_OUT)),
         hint='How much does OUT go up each time IN goes up by 1? Then test that times n on the first pair.',
         steps=['OUT goes up by 6 each time, so the rule starts with 6 × n.', f'For IN 1: 6 × 1 = 6, but OUT is 1, so take away 5. The rule is OUT = 6n {M} 5.', f'For IN 20: 6 × 20 {M} 5 = 115.'],
         src=['IN 1, 2, 3, 4 gives OUT 1, 7, 13, 19.']),
    dict(id='T2', tier='stretch', no='T2', type='number', strand=AL, skill='solving a simple equation', answer=8,
         q=f'Solve 9n {M} 7 = 65. What is n?', check=lambda: next(n for n in range(0, 1000) if 9 * n - 7 == 65),
         hint='9n − 7 means times 9, then take away 7. Undo the last step first.',
         steps=['The machine does × 9, then − 7.', 'Undo − 7: 65 + 7 = 72. Undo × 9: 72 ÷ 9 = 8.', 'n = 8. Check: 9 × 8 − 7 = 65.'],
         src=['Solve 9n']),
    dict(id='T3a', tier='stretch', no='T3', type='fields', strand=AL, skill='order of steps', svg=W.machine_rows(MACHINES_AB, 'Machine A: n, times 2, plus 10, OUT. Machine B: n, plus 5, times 2, OUT.'),
         q='Machine A does × 2, then + 10. Machine B does + 5, then × 2. Put 7 into both. What does each give?', frame='Machine A gives {f1};   Machine B gives {f2}', answer=[24, 24],
         check=lambda: [apply_ops(['× 2', '+ 10'], 7), apply_ops(['+ 5', '× 2'], 7)],
         hint='Do the steps in the order they are written for each machine. Start with 7.',
         steps=['Machine A: 7 × 2 = 14, then 14 + 10 = 24.', 'Machine B: 7 + 5 = 12, then 12 × 2 = 24.'],
         src=['Machine A does']),
    dict(id='T3b', tier='stretch', no='T3 explain', type='selfcheck', strand=AL, skill='explaining with a letter', svg=W.machine_rows(MACHINES_AB, 'Machine A: n, times 2, plus 10, OUT. Machine B: n, plus 5, times 2, OUT.'),
         q='Machine A does × 2, then + 10. Machine B does + 5, then × 2. What do you notice about the two answers? Explain with n. Write your reason, then check it against the worked solution.',
         facts=dict(always_equal=True), check=lambda: dict(always_equal=all(apply_ops(['× 2', '+ 10'], k) == apply_ops(['+ 5', '× 2'], k) for k in range(-30, 100))),
         hint='Write each machine as a rule with n. If a rule has brackets, multiply them out. Then compare the two rules.',
         steps=['Machine A: 2n + 10.', 'Machine B: (n + 5) × 2 = 2n + 10 (2 lots of n and 2 lots of 5).', 'The two rules are the same, so the two machines always give the same OUT, whatever IN is.'],
         src=['Explain with n.']),
    dict(id='T4', tier='stretch', no='T4', type='number', strand=AL, skill='running a machine backwards', answer=36,
         q='I think of a number, divide it by 4, then add 6. I get 15. What is my number?', check=lambda: next(n for n in range(0, 1000) if n / 4 + 6 == 15),
         hint='Undo the last step first, then undo the one before it.',
         steps=['The machine did ÷ 4, then + 6, and OUT is 15.', f'Undo + 6: 15 {M} 6 = 9. Undo ÷ 4: 9 × 4 = 36.', 'My number is 36. Check: 36 ÷ 4 = 9, 9 + 6 = 15.'],
         src=['I think of a number, divide it by 4']),

    # ================= Go further (last three Go further questions of the workbook)
    dict(id='C1a', tier='challenge', no='C1 (a)', type='selfcheck', strand=AL, skill='machines with the same OUT',
         q='Machines of the form "× a number, then + or − a number" can turn IN 5 into OUT 18. Find two different machines that do this. Write your answers, then check them against the worked solution.',
         facts=[(1, 13), (2, 8), (3, 3), (4, -2)], check=lambda: [(a, 18 - 5 * a) for a in range(1, 5)],
         hint='Choose a × number first. Then ask what you must add (or take away) so that 5 times it gives 18.',
         steps=[f'Many machines work: × 1 then + 13, × 2 then + 8, × 3 then + 3, × 4 then {M} 2, and more.', f'For any × number, take 5 times it and add or take away what is needed to reach 18. For example 5 × 3 = 15 and 15 + 3 = 18.'],
         src=['Find two different machines']),
    dict(id='C1b', tier='challenge', no='C1 (b)', type='fields', strand=AL, skill='finding a machine from two pairs',
         q='Which machine of the form "× a number, then + or − a number" turns IN 5 into OUT 18 AND also turns IN 2 into OUT 6? Type the × number and the + number. (Type a minus sign if it takes a number away.)',
         frame='× {f1}, then + {f2}', answer=[4, -2], check=lambda: (lambda hits: list(hits[0]) if len(hits) == 1 else None)([(a, 18 - 5 * a) for a in range(-30, 31) if 2 * a + (18 - 5 * a) == 6]),
         hint='Compare the two pairs: how much does IN change, and how much does OUT change? What does that tell you about the × number?',
         steps=['From IN 2 to IN 5 is 3 more, and OUT goes from 6 to 18, which is 12 more.', f'So the × number is 12 ÷ 3 = 4. Then 4 × 2 = 8, and OUT is 6, so take away 2.', f'The machine is × 4, then {M} 2. Check: 4 × 5 {M} 2 = 18.'],
         src=['Then find the machine of this form that ALSO turns IN 2 into OUT 6.']),
    dict(id='C1c', tier='challenge', no='C1 (c)', type='choice', strand=AL, skill='two pairs fix a rule', options=['Yes', 'No'], answer='Yes',
         q='Is there only one machine of the form "× a number, then + or − a number" that turns IN 5 into OUT 18 AND IN 2 into OUT 6?',
         check=lambda: 'Yes' if len([a for a in range(-30, 31) if 2 * a + (18 - 5 * a) == 6]) == 1 else 'No',
         hint='Think about how much IN and OUT change between the two pairs. Does that decide the × number?',
         steps=['The two pairs fix the × number: it must be 4. Then the + or − number is fixed too.', f'Only × 4 then {M} 2 works. Two pairs of IN and OUT fix the rule.'],
         src=['Is there only one?']),
    dict(id='C2', tier='challenge', no='C2', type='number', strand=AL, skill='forming and solving an equation', answer=12, svg=ages_fig(),
         q='Mei is n years old. Her mother is 3 times as old. In 12 years, her mother will be twice as old as Mei. How old is Mei now? (The bars are not drawn to scale.)',
         check=lambda: next(n for n in range(1, 100) if 3 * n + 12 == 2 * (n + 12)),
         hint='Write both ages in 12 years using n. Then write "mother is twice as old as Mei" as an equation and solve it.',
         steps=[f'Mei now: n. Mother now: 3n. In 12 years: Mei n + 12, mother 3n + 12.', f'Mother = twice Mei: 3n + 12 = 2(n + 12) = 2n + 24.', f'Take 2n away from both sides: n + 12 = 24, so n = 12.', 'Mei is 12 now (mother 36). In 12 years they are 24 and 48.'],
         src=['Mei is n years old.']),
    dict(id='C3', tier='challenge', no='C3', type='fields', strand=AL, skill='finding a machine from two pairs',
         q=f'Ali\'s secret machine does "× a number, then + or − a number". IN 4 gives OUT 9. IN 9 gives OUT 24. What does IN 20 give? Which IN gives OUT 99?',
         frame='IN 20 gives OUT {f1};   OUT 99 comes from IN {f2}', answer=[57, 34],
         check=lambda: (lambda ab: [ab[0] * 20 + ab[1], next(n for n in range(0, 1000) if ab[0] * n + ab[1] == 99)])(rule_of([4, 9], [9, 24])),
         hint='Compare the two pairs: how much does IN change, and how much does OUT change? What does that tell you about the × number? Then fix the + or − number from one pair.',
         steps=[f'From IN 4 to IN 9 is 5 more and OUT goes from 9 to 24, which is 15 more. So the × number is 3.', f'3 × 4 = 12 and OUT is 9, so take away 3. The rule is 3n {M} 3.', f'IN 20: 3 × 20 {M} 3 = 57. OUT 99: 99 + 3 = 102, and 102 ÷ 3 = 34.'],
         src=['Ali']),
]

for _it in ITEMS:
    if _it.get('frame'):
        _it['frame'] = W.nb(_it['frame'])

# ---------------------------------------------------------------- variant families (every combination is run against an independent oracle at build time)
P.finish(ITEMS)

VARIANTS = {
    '1b': dict(base=dict(a=6, d=3),
               tpl=dict(vars=dict(a=[6, 7, 8, 9, 10, 11, 12], d=[2, 3, 4, 5]), derive=dict(b='a+d', c='a+2*d', e='a+3*d'),
                        q='Guess my rule. IN 1, 2, 3, 4 give OUT {a}, {b}, {c}, {e}. Write the rule with n, then find the OUT for IN 10.', frame='OUT = {f1} × n + {f2};   OUT for IN 10 = {f3}', answers=dict(f1='d', f2='a-d', f3='10*d+a-d'),
                        hint='How much does OUT go up each time IN goes up by 1? That is the number in front of n. Then test the rule on the first pair.',
                        steps=['OUT goes up by {d} each time, so the rule starts with {d} × n.', 'For IN 1: {d} × 1 = {d}, but OUT is {a}, so add {a} - {d}.', 'The answers are {ans}.']),
               oracle=lambda e: (lambda ab: dict(f1=ab[0], f2=ab[1], f3=ab[0] * 10 + ab[1]))(rule_of([1, 2, 3, 4], [e['a'] + k * e['d'] for k in range(4)]))),
    '3b': dict(base=dict(n=10, m=7, k=4),
               tpl=dict(vars=dict(n=[3, 5, 8, 10, 12, 15, 20], m=[2, 3, 4, 5, 6, 7, 8, 9], k=[1, 2, 3, 4, 5, 6, 7, 8, 9]), derive=dict(o='m*n+k'),
                        q='Run the machine backwards to find n. {m}n + {k} = {o}. What is n?', answer='n',
                        hint='{m}n + {k} means times {m}, then add {k}. Undo the last step first.',
                        steps=['The machine does × {m}, then + {k}, and OUT is {o}.', 'Undo + {k}: {o} - {k}. Then undo × {m}.', 'n = {ans}.']),
               oracle=lambda e: next(x for x in range(0, 1000) if e['m'] * x + e['k'] == e['m'] * e['n'] + e['k'])),
    'X-a': dict(base=dict(m=4, k=5, x=6),
                tpl=dict(vars=dict(m=[2, 3, 4, 5, 6, 7], k=[1, 2, 3, 4, 5, 6, 7, 8, 9], x=[3, 4, 5, 6, 7, 8, 9]),
                         q='A machine does × {m}, then + {k}. IN {x}: what is OUT?', answer='m*x+k',
                         hint='Do the steps in order on {x}: first the times, then the add.',
                         steps=['{x} × {m}, then add {k}.', 'OUT is {ans}.']),
                oracle=lambda e: apply_ops([f"× {e['m']}", f"+ {e['k']}"], e['x'])),
}

# ---- inquiry habit (docs/pedagogy/inquiry_skills_explicit.md; levels/habits.json)
habit_tag(ITEMS, 'Check', ['2c-why'])
