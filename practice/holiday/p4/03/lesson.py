"""Online practice for Level 4 (Primary 4, ages 9-11) holiday lesson 3: Operation Detectives (Four operations).

The questions are the ones printed in the Level 4 holiday workbook, built by p4/workbook_html.js from p4/content/l3.js:
  Start here  = l3.js workbook() Q1 to Q7;   Investigation = l3.js gaps.invest (Make the target);
  Think harder = l3.js qbank.stretch[0:4];     Go further = l3.js qbank.challenge[-3:]  (printed as Q5 to Q7).
Every answer is recomputed by an INDEPENDENT checker (Python's own order of operations, a search over the numbers in the question, never a copy of the
printed answer); build_holiday.py stops if a checker and the printed answer differ.  The printed answers are the l3.js `key`, `gaps.invest.key` and `qbank` answers.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from p4lib import *      # noqa: E402,F401

META = dict(level=4, lesson=3, key='p4', title='Operation Detectives', workbook_title='OPERATION DETECTIVES', topic='Four operations',
            strand='Whole numbers: four operations',
            sources=['p4/content/l3.js'],
            intro=['Type numbers as plain digits. Where a question asks for signs or a number sentence, you may type x or * for ×, / for ÷ and - for −. Spaces do not matter.',
                   'Some questions ask you to explain, or to finish a bar model. Do those in your head or on paper, then compare with the answer after you submit.'])
S3 = 'Whole numbers: four operations'
NUMS = [2, 3, 4, 5]


def D(**k):
    return dict(strand=S3, **k)


def val(s):
    return int(value(s))


def exact(s):
    v = value(s)
    assert v.denominator == 1
    return int(v)


def sign_item(iid, no, nums, total, q, hint, steps, src, example):
    sols = sign_solutions(nums, total)
    assert len(sols) == 1, (iid, sols)          # the workbook key says each puzzle has only one answer
    signs = sols[0]
    return D(id=iid, tier='core', no=no, type='text', skill='missing signs', accept=sign_accepts(nums, signs, total), shown=' '.join(signs),
             svg=signs_figure(nums, total), check=lambda: ' '.join(sign_solutions(nums, total)[0]),
             q=q + f' Type the signs in order, for example: {example}', hint=hint, steps=steps, src=src)


def bracket_item(iid, tier, no, nums, ops, target, q, hint, steps, src, skill='brackets change the answer'):
    sols = one_pair_solutions(nums, ops, target)
    assert len(sols) == 1, (iid, sols)          # exactly one place for the brackets
    return D(id=iid, tier=tier, no=no, type='text', skill=skill, accept=[sols[0], f'{sols[0]} = {target}'], shown=sols[0],
             check=lambda: one_pair_solutions(nums, ops, target)[0], q=q, hint=hint, steps=steps, src=src)


def target_item(iid, tier, no, target, q, hint, steps, src, ops='+-*/', skill='making a target number', model=None):
    acc = sentences_for(NUMS, target, ops)
    assert acc and all(sentence_uses(s, NUMS) for s in acc)
    sample = min(acc, key=lambda s: (len(s), s))
    if model:
        assert model in acc, (iid, model)
        assert exact(model) == target
    return D(id=iid, tier=tier, no=no, type='text', skill=skill, accept=acc, shown=sample, check=lambda: sample if sentences_for(NUMS, target, ops) else None,
             q=q, hint=hint, steps=steps, src=src)


def trick(n, add=35):
    a = n * 5
    b = a + add
    c = b // 5
    assert c * 5 == b
    return [a, b, c, c - n]


def laksa_chicken(total, times=3):
    """Plates of laksa such that laksa + times * laksa = total (found by trying 1, 2, 3 ...)."""
    for lak in range(1, total + 1):
        if lak + times * lak == total:
            return lak, times * lak
    return None


def ways_accepts(ways):
    """Every way as its signs ('− + + − +'), all ways in either order, separated by a comma, semicolon, space or 'and'; or as whole number sentences (with or without '= 7')."""
    out = {', '.join(' '.join(w) for w in ways)}
    for ords in (ways, ways[::-1]):
        for sp in (',', ';', ' ', ' and '):
            out.add(sp.join(''.join(w) for w in ords))
        for sp in (', ', '; ', ' and '):
            out.add(sp.join(' '.join(w) for w in ords))
            for e1 in ('', ' = 7'):
                for e2 in ('', ' = 7'):
                    out.add(sp.join(sign_sentence([1, 2, 3, 4, 5, 6], w) + e for w, e in zip(ords, (e1, e2))))
    return sorted(out)


def mei_left(money):
    """Mei spends half on a book, $6 on lunch, then half of what is left on a gift. Returns what she has left (exact)."""
    m = Fr(money) / 2
    m = m - 6
    return m - m / 2


# the numbers of sentences that make each target 1 to 12, to say which targets are the hardest to find (counted by search)
COUNTS = {t: len(sentences_for(NUMS, t)) for t in range(1, 13)}
HARDEST = sorted(COUNTS, key=lambda t: COUNTS[t])[:3]
EASIEST = max(COUNTS, key=lambda t: COUNTS[t])

ITEMS = [
    # ================= Start here (workbook lesson 3, Q1 to Q7)
    D(id='1a', tier='core', no='1(a)', type='number', skill='order of operations', answer=106,
      check=lambda: (lambda packs: packs(36, 14, 5))(lambda start, size, n: sum([size] * n) + start),
      q='Work out. A story helps: 36 + 14 × 5 means 36 stickers and then 5 more packs of 14 stickers. Think about which part you do first.\n36 + 14 × 5',
      hint='Picture the 5 packs of 14 stickers (or count in 14s), then add the 36.',
      steps=['Multiplication comes before addition, so work out the 5 packs of 14 first: 14 × 5 = 70.', 'Then add the 36 stickers: 36 + 70 = 106.'],
      src=['Work out. A story helps: 36 + 14 × 5 means 36 stickers and then 5 more packs of 14 stickers.']),
    D(id='1b', tier='core', no='1(b)', type='number', skill='order of operations', answer=250, check=lambda: exact('(36 + 14) × 5'),
      q='Work out.\n(36 + 14) × 5', hint='The brackets tell you which part to do first.',
      steps=['Brackets first: 36 + 14 = 50.', 'Then 50 × 5 = 250.'], src=['(36 + 14) × 5']),
    D(id='1c', tier='core', no='1(c)', type='number', skill='order of operations', answer=27, check=lambda: exact('72 ÷ 8 × 3'),
      q='Work out.\n72 ÷ 8 × 3', hint='There are no brackets. When a sentence has only × and ÷, work from left to right.',
      steps=['There are only × and ÷, so work from left to right.', '72 ÷ 8 = 9.', '9 × 3 = 27.'], src=['72 ÷ 8 × 3']),
    D(id='1d', tier='core', no='1(d)', type='number', skill='order of operations', answer=98, check=lambda: exact('100 − 45 ÷ 5 + 7'),
      q='Work out.\n100 − 45 ÷ 5 + 7', hint='Divide first. Then work from left to right with − and +.',
      steps=['Division comes before subtraction and addition: 45 ÷ 5 = 9.', 'Now 100 − 9 + 7, from left to right: 100 − 9 = 91.', '91 + 7 = 98.'], src=['100 − 45 ÷ 5 + 7']),
    D(id='1e', tier='core', no='1(e)', type='number', skill='order of operations', answer=12, check=lambda: exact('6 × (25 − 17) ÷ 4'),
      q='Work out.\n6 × (25 − 17) ÷ 4', hint='Brackets first. Then × and ÷ from left to right.',
      steps=['Brackets first: 25 − 17 = 8.', 'Now 6 × 8 ÷ 4, from left to right: 6 × 8 = 48.', '48 ÷ 4 = 12.'], src=['6 × (25 − 17) ÷ 4']),

    sign_item('2a', '2(a)', [7, 6, 4], 38,
              'Missing signs. Find the sign for each circle to make the number sentence true. You may use a sign more than once.',
              'Estimate first. Is 38 big or small next to 7, 6 and 4? Then test a sign and work it out in the right order.',
              ['38 is much bigger than 7 + 6 + 4 = 17, so a × is needed.', '7 × 6 = 42, and 42 − 4 = 38. Checked in the right order: 7 × 6 − 4 = 38.', 'The signs are × and −. (Every other pair of signs was tested: none of them works.)'],
              ['Missing signs. Write +, −, × or ÷ in each circle to make the number sentence true. You may use a sign more than once.'], '− +'),
    sign_item('2b', '2(b)', [48, 6, 2], 16,
              'Missing signs. Find the sign for each circle to make the number sentence true.',
              'Start with 48 and 6. Which signs make a number much smaller? Test your idea in the right order.',
              ['Try ÷ in the first circle: 48 ÷ 6 = 8.', 'Then 8 needs to become 16 with the 2: 8 × 2 = 16.', 'The signs are ÷ and ×: 48 ÷ 6 × 2 = 16. (Every other pair of signs was tested: none of them works.)'],
              ['Missing signs. Write +, −, × or ÷ in each circle'], '+ −'),
    sign_item('2c', '2(c)', [9, 3, 5], 8,
              'Missing signs. Find the sign for each circle to make the number sentence true.',
              'Try a sign in the first circle, then find the sign that makes the whole sentence work out to the total. Remember the order of operations.',
              ['Try ÷ in the first circle: 9 ÷ 3 = 3.', 'Then 3 + 5 = 8.', 'The signs are ÷ and +: 9 ÷ 3 + 5 = 8. (Every other pair of signs was tested: none of them works.)'],
              ['Missing signs. Write +, −, × or ÷ in each circle'], '− ×'),
    sign_item('2d', '2(d)', [12, 3, 2, 5], 14,
              'Missing signs. Find the sign for each circle to make the number sentence true. There are three circles this time.',
              'Guess and check. Pick three signs, work the sentence out in the right order, then change one sign if it is too big or too small.',
              ['12 ÷ 3 = 4 is a good start, because the other numbers can then make 14.', 'Then 2 × 5 = 10 comes before the +: 4 + 10 = 14.', 'The signs are ÷, + and ×: 12 ÷ 3 + 2 × 5 = 14. (Every other set of three signs was tested: none of them works.)'],
              ['Missing signs. Write +, −, × or ÷ in each circle'], '− + −'),

    D(id='3a', tier='core', no='3(a)', type='number', skill='order of operations', answer=41, check=lambda: exact('4 + 8 × 5 − 3'),
      q='Brackets change the answer. Look at 4 + 8 × 5 − 3.\nWith no brackets, work out 4 + 8 × 5 − 3.',
      hint='With no brackets, which operation do you do first?',
      steps=['× comes before + and −: 8 × 5 = 40.', 'Now 4 + 40 − 3 from left to right: 4 + 40 = 44.', '44 − 3 = 41.'], src=['Brackets change the answer. Look at', '4 + 8 × 5 − 3']),
    bracket_item('3b', 'core', '3(b)', [4, 8, 5, 3], ['+', '×', '−'], 57,
                 'Put in ONE pair of brackets to make 57: 4 + 8 × 5 − 3 = 57. Type the whole sentence with its brackets, for example 2 × (3 + 1) − 5.',
                 'Try brackets round 4 + 8, then round 5 − 3, then round 8 × 5 − 3. Work each one out.',
                 ['The brackets have to make a part of the sentence do its work earlier, so that the answer gets bigger.', 'Put the brackets round 4 + 8: (4 + 8) = 12.', '12 × 5 = 60, and 60 − 3 = 57. It works.', 'The sentence is (4 + 8) × 5 − 3 = 57.'],
                 ['Put in ONE pair of brackets to make 57', '4  +  8  ×  5  −  3  =  57']),
    bracket_item('3c', 'core', '3(c)', [4, 8, 5, 3], ['+', '×', '−'], 20,
                 'Put in ONE pair of brackets to make 20: 4 + 8 × 5 − 3 = 20. Type the whole sentence with its brackets.',
                 'Try brackets round 4 + 8, then round 5 − 3, then round 8 × 5 − 3. Work each one out.',
                 ['The answer 20 is much smaller than 41, so the brackets must make the multiplication smaller.', 'Put the brackets round 5 − 3: (5 − 3) = 2.', '8 × 2 = 16, and 4 + 16 = 20. It works.', 'The sentence is 4 + 8 × (5 − 3) = 20.'],
                 ['Put in ONE pair of brackets to make 20', '4  +  8  ×  5  −  3  =  20']),

    D(id='4a', tier='core', no='4(a)', type='number', skill='working backwards', answer=23, svg=machine_figure(),
      check=lambda: [x for x in range(1, 1000) if Fr(x * 6 - 18, 4) == 30][0],
      q='A number goes into this machine chain. 30 comes out. Work backwards. What number went in?',
      hint='Start at the end, 30. Undo each step with its opposite: the opposite of × is ÷, and the opposite of − is +.',
      steps=['Start at 30 and undo the last step, ÷ 4, with × 4: 30 × 4 = 120.', 'Undo − 18 with + 18: 120 + 18 = 138.', 'Undo × 6 with ÷ 6: 138 ÷ 6 = 23.', 'The number that went in was 23.'],
      src=['A number goes into this machine chain. 30 comes out.', 'Work backwards. What number went in?']),
    D(id='4b', tier='core', no='4(b)', type='selfcheck', open=False, skill='checking by going forwards', svg=machine_figure(),
      facts=(138, 120, 30), check=lambda: (lambda x: (x * 6, x * 6 - 18, (x * 6 - 18) // 4))([x for x in range(1, 1000) if Fr(x * 6 - 18, 4) == 30][0]),
      q='Check it going forwards. Put the number you found in (a) into the machine and write down what you get after each step.',
      hint='Do one step at a time: × 6, then − 18, then ÷ 4. Does 30 come out?',
      steps=['Put 23 into the machine and go forwards.', '× 6: 23 × 6 = 138.', '− 18: 138 − 18 = 120.', '÷ 4: 120 ÷ 4 = 30. Thirty comes out, so 23 is right.'],
      src=['Check it going forwards.']),

    D(id='5a-try1', tier='core', no='5(a) try 6', type='fields', skill='a number trick', frame='My number 6:  × 5 → {f1}   + 35 → {f2}   ÷ 5 → {f3}   − my number → {f4}',
      answer=[30, 65, 13, 7], check=lambda: trick(6),
      q='Number trick. Think of a number. Multiply it by 5. Add 35. Divide by 5. Take away the number you started with. Try it with 6. Type the number you get after each step.',
      hint='Do one step at a time, and use the answer from the step before.',
      steps=['6 × 5 = 30.', '30 + 35 = 65.', '65 ÷ 5 = 13.', '13 − 6 = 7 (take away the number you started with).'],
      src=['Number trick. Think of a number. Multiply it by 5. Add 35. Divide by 5. Take away the number you started with. Try it with two different numbers.']),
    D(id='5a-try2', tier='core', no='5(a) try 20', type='fields', skill='a number trick', frame='My number 20:  × 5 → {f1}   + 35 → {f2}   ÷ 5 → {f3}   − my number → {f4}',
      answer=[100, 135, 27, 7], check=lambda: trick(20),
      q='Number trick, with a different number. Same steps: × 5, + 35, ÷ 5, then take away the number you started with. Try it with 20.',
      hint='Do one step at a time, and use the answer from the step before.',
      steps=['20 × 5 = 100.', '100 + 35 = 135.', '135 ÷ 5 = 27.', '27 − 20 = 7.'],
      src=['Try it with two different numbers.']),
    D(id='5a-notice', tier='core', no='5(a) notice', type='selfcheck', open=False, skill='a number trick', facts=7,
      check=lambda: (lambda ends: ends.pop() if len(ends) == 1 else None)({trick(n)[3] for n in range(1, 500)}),
      q='What do you notice about your last numbers in the two tries?',
      hint='Look at the number you ended with each time. Try a third number of your own to test your idea.',
      steps=['Both tries ended with 7.', 'Try any other starting number: the last number is 7 every time. (This was tested for every number from 1 to 499.)', 'Notice it, test it, then explain why. The next question helps.'],
      src=['What do you notice?']),
    D(id='5b-back', tier='core', no='5(b) 1', type='choice', options=['35', 'my number', '7'], answer='my number', skill='explaining a number trick',
      check=lambda: 'my number' if all(trick(n)[2] - 7 == n for n in range(1, 200)) else None,
      q='Fill in the blanks. × 5 and then ÷ 5 gives back my ____.', hint='Multiplying and then dividing by the same number undoes itself.',
      steps=['Multiplying by 5 and then dividing by 5 gets you back to where you started: your own number.', 'So only the + 35 is left to work out.'],
      src=['Fill in the blanks.', 'gives back my']),
    D(id='5b-rest', tier='core', no='5(b) 2', type='fields', skill='explaining a number trick', frame='The 35 ÷ 5 adds {f1}.   Taking away my number leaves {f2}.',
      answer=[7, 7], check=lambda: [35 // 5, trick(11)[3]],
      q='Fill in the blanks. The 35 ÷ 5 adds ____. Taking away my number leaves ____.',
      hint='What is 35 ÷ 5? When you take away your own number, what is left?',
      steps=['The 35 is also divided by 5: 35 ÷ 5 = 7. So the trick adds 7 to your number.', 'Taking away your number leaves just the 7.', 'That is why the last number is the same every time.'],
      src=['The 35 ÷ 5 adds', 'Taking away my number leaves']),

    D(id='6a', tier='core', no='6(a)', type='selfcheck', paper=True, skill='drawing a bar model', svg=bar_pair('Laksa', 1, 'Chicken rice', 3, '124 plates'),
      facts=(1, 3, 4), check=lambda: (lambda lak, chk: (1, chk // lak, (lak + chk) // lak))(*laksa_chicken(124)),
      sol_fig=lambda f: bar_pair('Laksa', 1, 'Chicken rice', 3, '124 plates|= 4 units', labels_top={0: '1 unit'}, labels_bot={0: '1 unit', 1: '1 unit', 2: '1 unit'}),
      q='A hawker stall sold 3 times as many plates of chicken rice as plates of laksa. It sold 124 plates altogether. Finish the bar model: write what each box stands for. You will use it for the next two questions.',
      hint='Laksa is 1 box. How many boxes of the same size are there for chicken rice? How many boxes altogether?',
      steps=['Laksa is 1 unit (1 box). Chicken rice is 3 times as many, so 3 units (3 boxes of the same size).', 'Altogether there are 1 + 3 = 4 units, and the 4 units stand for the 124 plates.'],
      src=['A hawker stall sold 3 times as many plates of chicken rice as plates of laksa. It sold 124 plates altogether.', 'Finish the bar model: write what each bar stands for']),
    D(id='6b', tier='core', no='6(b)', type='number', skill='bar model: times as many', answer=93, check=lambda: laksa_chicken(124)[1],
      svg=bar_pair('Laksa', 1, 'Chicken rice', 3, '124 plates'),
      q='A hawker stall sold 3 times as many plates of chicken rice as plates of laksa. It sold 124 plates altogether. How many plates of chicken rice did it sell?',
      hint='Use the bar model. 4 equal units stand for 124 plates. How many plates are in 1 unit?',
      steps=['The model has 1 + 3 = 4 equal units, and 4 units = 124 plates.', '1 unit = 124 ÷ 4 = 31 plates (that is the laksa).', 'Chicken rice is 3 units: 3 × 31 = 93 plates.'],
      src=['How many plates of chicken rice did it sell?']),
    D(id='6c', tier='core', no='6(c)', type='number', skill='bar model: times as many', answer=62, check=lambda: (lambda lak, chk: chk - lak)(*laksa_chicken(124)),
      svg=bar_pair('Laksa', 1, 'Chicken rice', 3, '124 plates'),
      q='A hawker stall sold 3 times as many plates of chicken rice as plates of laksa. It sold 124 plates altogether. How many more plates of chicken rice than laksa did it sell?',
      hint='How many more units does chicken rice have than laksa? How many plates is one unit?',
      steps=['Chicken rice is 3 units and laksa is 1 unit, so chicken rice has 2 units more.', '1 unit = 124 ÷ 4 = 31 plates, so 2 units = 62 plates.', 'Check: 93 − 31 = 62.'],
      src=['How many more plates of chicken rice than laksa?']),

    D(id='7a', tier='core', no='7(a)', type='fields', skill='number chains', frame='{f1},  {f2},  13,  21,  {f3}', answer=[5, 8, 34],
      check=lambda: [(lambda s: [s[0], s[1], s[4]])(chain_terms(a, b, 5)) for a in range(0, 40) for b in range(0, 40) if chain_terms(a, b, 5)[2:4] == [13, 21]][0],
      q='★ Choice question. Number chains. After the first two numbers, each number is the sum of the two numbers before it. Example: 2, 5, 7, 12, 19. Chain (a): work backwards from 13 and 21 to fill in the missing numbers.',
      hint='Work backwards. The 4th number is the 2nd and 3rd numbers added. Which step takes you from 13 to 21?',
      steps=['The 4th number, 21, is the 2nd + the 3rd, so the 2nd number is 21 − 13 = 8.', 'The 3rd number, 13, is the 1st + the 2nd, so the 1st number is 13 − 8 = 5.', 'The 5th number is 13 + 21 = 34.', 'The chain is 5, 8, 13, 21, 34.'],
      src=['Number chains. After the first two numbers, each number is the sum of the two numbers before it. Example: 2, 5, 7, 12, 19. Fill in the missing numbers.', 'Chain (a): work backwards from 13 and 21.']),
    D(id='7b', tier='core', no='7(b)', type='fields', skill='number chains', frame='4,  {f1},  {f2},  18,  {f3}', answer=[7, 11, 29],
      check=lambda: [(lambda s: [s[1], s[2], s[4]])(chain_terms(4, b, 5)) for b in range(0, 40) if chain_terms(4, b, 5)[3] == 18][0],
      q='★ Choice question. Number chains. Each number after the first two is the sum of the two numbers before it. Chain (b): guess the 2nd number, then check.',
      hint='Guess the 2nd number and build the chain. Is the 4th number 18? If it is too big or too small, change your guess.',
      steps=['Guess the 2nd number, for example 5: the chain is 4, 5, 9, 14. The 4th number is too small (it should be 18).', 'Try 7: the chain is 4, 7, 11, 18. The 4th number is 18, so 7 is right.', 'The 5th number is 11 + 18 = 29.', 'The chain is 4, 7, 11, 18, 29.'],
      src=['Chain (b): guess the 2nd number, then check.']),

    # ================= Investigation: Make the target
    target_item('I1', 'invest', 'Investigation (easy step) 6', 6,
                'Make the target. Use ALL four numbers 2, 3, 4 and 5, once each, in a number sentence. One is done for you: 2 + 3 + 4 − 5 = 4. '
                'Easy first step: use only + and −. Make 6. Type your number sentence.',
                'Try the four numbers in a different order, or change a sign. Work each sentence out from left to right.',
                ['Many sentences work. One is 2 + 3 − 4 + 5: 2 + 3 = 5, 5 − 4 = 1, 1 + 5 = 6.', 'Any sentence that uses 2, 3, 4 and 5 once each, with only + and −, and works out to 6 is right.'],
                ['Use ALL four numbers 2, 3, 4 and 5, once each.', 'One is done for you: 2 + 3 + 4 − 5 = 4.'], ops='+-', model='2 + 3 − 4 + 5'),
    target_item('I2', 'invest', 'Investigation (easy step) 8', 8,
                'Using 2, 3, 4 and 5 once each, with only + and −, make 8. Type your number sentence.',
                'Think about which number you could take away so that the others still add up to 8.',
                ['One way is 5 + 4 + 2 − 3: 5 + 4 = 9, 9 + 2 = 11, 11 − 3 = 8.', 'Any sentence that uses 2, 3, 4 and 5 once each, with only + and −, and works out to 8 is right.'],
                ['With 2, 3, 4 and 5 (each once) can you make 6? 8? 10?'], ops='+-', model='5 + 4 + 2 − 3'),
    target_item('I3', 'invest', 'Investigation (easy step) 10', 10,
                'Using 2, 3, 4 and 5 once each, with only + and −, make 10. Type your number sentence.',
                'Add all four numbers first. Is the total too big or too small for 10? What happens when you take a number away instead of adding it?',
                ['The four numbers add up to 14. Taking away a number instead of adding it takes off twice that number, so we need to take off 4 in all: the number 2 is taken away.', '3 + 4 + 5 − 2 = 10 (3 + 4 = 7, 7 + 5 = 12, 12 − 2 = 10).', 'Any sentence that uses 2, 3, 4 and 5 once each, with only + and −, and works out to 10 is right.'],
                ['With 2, 3, 4 and 5 (each once) can you make 6? 8? 10?'], ops='+-', model='3 + 4 + 5 − 2'),
    target_item('I4', 'invest', 'Investigation (a) 1', 1,
                'Make as many of the target numbers from 1 to 12 as you can. Use ALL of 2, 3, 4 and 5, once each, with +, −, × and ÷ and brackets. Make 1. Type your number sentence.',
                'A small target often needs a − or a ÷, or brackets that make a part equal to 1. Work your sentence out in the right order.',
                ['One sentence is (5 − 4) × (3 − 2): 5 − 4 = 1 and 3 − 2 = 1, and 1 × 1 = 1.', 'Other sentences work too. Any sentence that uses 2, 3, 4 and 5 once each and works out to 1 is right.'],
                ['Use ALL four numbers 2, 3, 4 and 5, once each. You may use +, −, ×, ÷ and brackets.', 'Make as many of the target numbers from 1 to 12 as you can.'], model='(5 − 4) × (3 − 2)'),
    target_item('I5', 'invest', 'Investigation (a) 7', 7,
                'Using 2, 3, 4 and 5 once each, with +, −, × and ÷ and brackets, make 7. Type your number sentence.',
                'Estimate first: is 7 big or small next to the four numbers? Try a sentence, work it out in the right order, then change a sign or add brackets.',
                ['One sentence is 2 + (4 − 3) × 5. Brackets first: 4 − 3 = 1. Then × : 1 × 5 = 5. Then + : 2 + 5 = 7.', 'Other sentences work too. Any sentence that uses 2, 3, 4 and 5 once each and works out to 7 is right.'],
                ['Make as many of the target numbers from 1 to 12 as you can.'], model='2 + (4 − 3) × 5'),
    target_item('I6', 'invest', 'Investigation (a) 9', 9,
                'Using 2, 3, 4 and 5 once each, with +, −, × and ÷ and brackets, make 9. Type your number sentence.',
                'Try one × in your sentence and see what the other numbers must do.',
                ['One sentence is 2 + 3 × 4 − 5. × first: 3 × 4 = 12. Then from left to right: 2 + 12 = 14, 14 − 5 = 9.', 'Other sentences work too. Any sentence that uses 2, 3, 4 and 5 once each and works out to 9 is right.'],
                ['Make as many of the target numbers from 1 to 12 as you can.'], model='2 + 3 × 4 − 5'),
    target_item('I7', 'invest', 'Investigation (a) 12', 12,
                'Using 2, 3, 4 and 5 once each, with +, −, × and ÷ and brackets, make 12. Type your number sentence.',
                'Some targets are harder than others. Try brackets round two numbers that add up to something you can multiply.',
                ['One sentence is 2 × (3 + 5) − 4. Brackets first: 3 + 5 = 8. Then × : 2 × 8 = 16. Then − : 16 − 4 = 12.', 'Other sentences work too. Any sentence that uses 2, 3, 4 and 5 once each and works out to 12 is right.'],
                ['Make as many of the target numbers from 1 to 12 as you can.'], model='2 × (3 + 5) − 4'),
    D(id='I8', tier='invest', no='Investigation (b) can all be made?', type='choice', options=['Yes', 'No'], answer='No', skill='testing a claim about targets',
      check=lambda: 'No' if all(sentences_for(NUMS, t) for t in range(1, 13)) else 'Yes',
      q='Is there a target from 1 to 12 that cannot be made with 2, 3, 4 and 5 (once each, with +, −, × and ÷ and brackets)?',
      hint='Think about the targets you made, and the ones you did not. Can you find a sentence for each of the others?',
      steps=['Every target from 1 to 12 can be made, so the answer is No. (A computer search tried every sentence, and it found a way for every target from 1 to 20.)',
             'Checked examples: ' + '; '.join(f'{t} = {min(sentences_for(NUMS, t), key=lambda s: (len(s), s))}' for t in (2, 3, 5, 11)) + '.'],
      src=['Is there a target from 1 to 12 that you think cannot be made? Say why.']),
    D(id='I9', tier='invest', no='Investigation (b) hardest', type='selfcheck', open=True, marking_mode='open', skill='testing a claim about targets',
      q='Which target from 1 to 12 was the hardest for you to make? Why do you think it was hard?',
      hint='Think about which target took you the most tries.',
      steps=[f'Answers will vary. A computer counted the number sentences for each target: the targets {HARDEST[0]}, {HARDEST[1]} and {HARDEST[2]} have the fewest sentences, so they are usually the hardest to find. '
             f'The target {EASIEST} has the most.', 'A good answer says what you tried first and what you changed.'],
      src=['Which target was hardest?']),
    D(id='I10', tier='invest', no='Investigation (c)', type='selfcheck', open=True, marking_mode='open', skill='checking a classmate\'s number sentence',
      q='Swap: choose a target from 1 to 20 for a partner or a grown-up. Ask them for a number sentence that uses 2, 3, 4 and 5 once each. Check it by working it out in the right order. Write the target and the sentence here.',
      hint='Work the sentence out step by step: brackets first, then × and ÷, then + and −.',
      steps=['Work out the sentence step by step: brackets first, then × and ÷ from left to right, then + and − from left to right.', 'Every target from 1 to 20 can be made with 2, 3, 4 and 5 once each (a computer search found one for each). For example ' +
             '; '.join(f'{t} = {min(sentences_for(NUMS, t), key=lambda s: (len(s), s))}' for t in (13, 18, 20)) + '.'],
      src=['Swap: write a target from 1 to 20 for a partner. Check their number sentence by working it out.']),

    # ================= Think harder (qbank.stretch[0:4])
    D(id='T1', tier='stretch', no='Think harder 1', type='number', skill='bar model: times as many', answer=468, svg=bar_pair('Red', 1, 'Blue', 4, '2 340 beads'),
      check=lambda: [r for r in range(1, 2341) if r + 4 * r == 2340][0],
      q='There are 2 340 red and blue beads. There are 4 times as many blue beads as red beads. How many red beads are there?',
      hint='How many equal units are there in the whole bar model? Share the 2 340 beads between them.',
      steps=['Red is 1 unit and blue is 4 units, so there are 1 + 4 = 5 units altogether.', '5 units = 2 340 beads, so 1 unit = 2 340 ÷ 5 = 468.', 'Red is 1 unit: 468 beads. (Check: blue = 4 × 468 = 1 872, and 468 + 1 872 = 2 340.)'],
      src=['There are 2 340 red and blue beads. There are 4 times as many blue beads as red beads. How many red beads are there?']),
    bracket_item('T2', 'stretch', 'Think harder 2', [3, 5, 6, 2], ['+', '×', '−'], 46,
                 'Put ONE pair of brackets in 3 + 5 × 6 − 2 to make the answer 46. Type the whole sentence with its brackets.',
                 'Work the sentence out with no brackets first. Is 46 bigger or smaller? Then try brackets in different places.',
                 ['With no brackets: 5 × 6 = 30, then 3 + 30 − 2 = 31. That is too small.', 'Brackets round 3 + 5 make the number that is multiplied bigger: 3 + 5 = 8.', '8 × 6 = 48, and 48 − 2 = 46. It works.', 'The sentence is (3 + 5) × 6 − 2 = 46.'],
                 ['Put ONE pair of brackets in 3 + 5 × 6 − 2 to make the answer 46.'], skill='brackets change the answer'),
    sign_item('T3', 'Think harder 3', [12, 4, 5], 15,
              'Find the sign for each gap to make this true.',
              'Guess and check. Work each guess out in the right order (× and ÷ before + and −), and change one sign at a time.',
              ['Try ÷ in the first gap: 12 ÷ 4 = 3.', 'Then 3 × 5 = 15. It works: 12 ÷ 4 × 5 = 15.', 'No other pair of signs works (every pair was tested).'],
              ['Write +, −, × or ÷ in each gap to make this true:', '12 __ 4 __ 5 = 15'], '+ +') | dict(tier='stretch'),
    D(id='T4', tier='stretch', no='Think harder 4', type='selfcheck', open=True, marking_mode='self', skill='explaining a number trick',
      q='Think of a number. Multiply it by 5. Add 35. Divide by 5. Take away the number you started with. Try it with two or three different numbers. What do you notice about the last number? Explain why it happens. A bar model can help.',
      hint='Show your number as a bar and follow each step of the trick on the bar. What is left at the end?',
      steps=['Multiplying by 5 and then dividing by 5 gets back your number.', 'The 35 is divided by 5 as well, so it adds 35 ÷ 5 = 7.', 'Taking away your number then leaves the 7. So the answer is always 7, whatever number you start with.', 'A bar model: draw your number as a bar. × 5 makes 5 bars, + 35 adds a piece, ÷ 5 shares it into 5 equal parts: one bar and a piece of 7.'],
      src=['Think of a number. Multiply it by 5. Add 35. Divide by 5. Take away the number you started with.']),

    # ================= Go further (qbank.challenge[-3:], printed Q5 to Q7)
    D(id='G5', tier='challenge', no='Go further 5', type='text', skill='finding all the ways with + and −',
      accept=ways_accepts(sign_solutions([1, 2, 3, 4, 5, 6], 7, '+−')),
      shown=' and '.join(' '.join(w) for w in sign_solutions([1, 2, 3, 4, 5, 6], 7, '+−')[::-1]),
      check=lambda: ', '.join(' '.join(w) for w in sign_solutions([1, 2, 3, 4, 5, 6], 7, '+−')),
      q='Put + or − in each gap so that the answer is 7: 1 __ 2 __ 3 __ 4 __ 5 __ 6 = 7. Find ALL the ways. Type each way as its five signs in order, with a comma between the ways. Write the signs like this: + + − + − (that one does not make 7).',
      hint='If every gap is +, the total is 21. How much too big is that? What happens to the total when you change one + to a −?',
      steps=['If all the signs are +, then 1 + 2 + 3 + 4 + 5 + 6 = 21. That is 14 too many.', 'Changing a + to a − takes that number away twice. So the numbers that we change to − must add up to 14 ÷ 2 = 7.',
             'Numbers from 2 to 6 that add to 7: 2 and 5, or 3 and 4. (The 1 has no sign in front of it, so it cannot change.)', '2 and 5 taken away: 1 − 2 + 3 + 4 − 5 + 6 = 7, the signs are − + + − +.', '3 and 4 taken away: 1 + 2 − 3 − 4 + 5 + 6 = 7, the signs are + − − + +.', 'There are 2 ways.'],
      src=['Put + or − in each gap so that the answer is 7:', 'Find ALL the ways.']),
    D(id='G6', tier='challenge', no='Go further 6', type='number', skill='working backwards with a bar model', answer=48, svg=money_model(),
      check=lambda: [m for m in range(12, 1000) if mei_left(m) == 9][0],
      q='Mei spent half of her money on a book. Then she spent $6 on lunch. Then she spent half of what was left on a gift. She had $9 left. How much money did she have at first?',
      hint='Work backwards from the $9 left. What did she have just before she bought the gift?',
      steps=['Work backwards. The $9 left is the other half of what she had before the gift, so before the gift she had 2 × $9 = $18.', 'Before lunch she had $18 + $6 = $24.', '$24 was half of her money, so at first she had 2 × $24 = $48.', 'Check: half of $48 is $24 for the book; $24 − $6 = $18; half of $18 is $9 for the gift and $9 left.'],
      src=['Mei spent half of her money on a book. Then she spent $6 on lunch. Then she spent half of what was left on a gift. She had $9 left. How much money did she have at first?']),
    D(id='G7a', tier='challenge', no='Go further 7(a)', type='number', skill='explaining a number trick', answer=50,
      check=lambda: [x for x in range(0, 300) if all(Fr(5 * n + x, 5) - n == 10 for n in range(1, 60))][0],
      q='The number trick: think of a number, multiply by 5, add 35, divide by 5, take away your number. '
        'What must you change so that it always ends with 10? Change the "add 35" step to "add ____". Type the number.',
      hint='Try the trick with a number of your own. What does the added number turn into at the end?',
      steps=['× 5 and then ÷ 5 get back your own number, so only the added number matters at the end.', 'The added number is divided by 5. With 35 you are left with 35 ÷ 5 = 7.', 'To be left with 10 you need a number that divides by 5 to make 10: 5 × 10 = 50. Change the + 35 to + 50.', 'Check with 4: 4 × 5 = 20, 20 + 50 = 70, 70 ÷ 5 = 14, 14 − 4 = 10.'],
      src=['The number trick: think of a number, multiply by 5, add 35, divide by 5, take away your number.', '(a) What must you change so that it always ends with 10?']),
    D(id='G7b', tier='challenge', no='Go further 7(b)', type='selfcheck', open=True, marking_mode='open', skill='making up a number trick',
      q='Make up your own number trick with four steps that always ends with 3. Test it with two numbers and explain why it works.',
      hint='Use the same plan as the trick above: a × and a ÷ that cancel, an added number, and taking away your number at the end.',
      steps=['Tricks will vary. Test yours with two numbers, then explain why the end number is always the same.', 'Model trick: × 4, + 12, ÷ 4, − your number. Start with 5: 20, 32, 8, 3. Start with 9: 36, 48, 12, 3.',
             'Why it works: × 4 and then ÷ 4 get your number back. The 12 is divided by 4 too, so it adds 3. Taking away your number leaves the 3.'],
      src=['(b) Make up your own number trick with four steps that always ends with 3. Test it with two numbers and explain why it works.']),
]

finish(ITEMS)

VARIANTS = {
    '1a': dict(
        base=dict(a=36, b=14, c=5),
        tpl=dict(vars=dict(a=[18, 24, 36, 45, 52], b=[12, 14, 15, 16], c=[3, 4, 5, 6]), derive=dict(p='b*c'),
                 q='Work out. A story helps: {a} + {b} × {c} means {a} stickers and then {c} more packs of {b} stickers. Think about which part you do first.\n{a} + {b} × {c}',
                 answer='a+b*c', hint='Picture the {c} packs of {b} stickers (or count in {b}s), then add the {a}.',
                 steps=['Multiplication comes before addition, so work out the {c} packs of {b} first: {b} × {c} = {p}.', 'Then add the {a} stickers: {a} + {p} = {ans}.']),
        oracle=lambda e: sum([e['b']] * e['c']) + e['a']),
    '6b': dict(
        base=dict(k=3, u=31),
        tpl=dict(vars=dict(k=[2, 3, 4, 5], u=[12, 15, 18, 24, 31, 40]), derive=dict(total='(k+1)*u'),
                 q='A stall sold {k} times as many plates of chicken rice as plates of laksa. It sold {total} plates altogether. How many plates of chicken rice did it sell?',
                 answer='k*u', hint='Use a bar model. How many equal units stand for {total} plates? How many plates are in 1 unit?',
                 steps=['The model has 1 + {k} equal units, and they stand for {total} plates.', '1 unit is the laksa: {total} divided into 1 + {k} equal units gives {u} plates.', 'Chicken rice is {k} units: {k} × {u} = {ans} plates.']),
        oracle=lambda e: laksa_chicken((e['k'] + 1) * e['u'], e['k'])[1]),
}
