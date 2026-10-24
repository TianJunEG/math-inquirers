"""Online practice for Level 5 (Primary 5, ages 10 to 12) holiday lesson 2: Fractions: Four Operations ("Fraction Feats").

The questions are the ones printed in the Level 5 holiday workbook, lesson 2: Start here Q1 to Q6 (p5/content/l2.js, workbook()), the Investigation
(p5/content/inv.js), Think harder A1 to A4 (the first four 'stretch' questions of p5/content/l2.js qbank) and Go further B1 to B3 (the last three
'challenge' questions), exactly as p5/workbook_html.js prints them.  Every answer is recomputed by an INDEPENDENT checker below (exact fractions,
search or simulation, never a copy of the printed answer); build_holiday.py stops if a checker and the printed answer differ.
"""
import os, sys
HERE_ = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE_, '..', '..'))
sys.path.insert(0, os.path.join(HERE_, '..'))
from hlib import *          # noqa: E402,F401
from p5lib import *         # noqa: E402,F401

META = dict(level=5, lesson=2, key='p5', title='Fraction Feats', workbook_title='FRACTION FEATS', topic='Fractions: Four Operations', strand='Fractions',
            sources=['p5/content/l2.js', 'p5/content/inv.js', 'p5/content/gaps.js'],
            intro=['a ÷ b = a/b: 3 pizzas shared by 4 friends is 3/4 each. A unit fraction has 1 on top. Draw a bar model when you are stuck, and find the remainder first, then take the fraction of the remainder.',
                   'Type a fraction like 3/4 (you may use a mixed number like 5 1/2 too). Some questions ask you to explain: write your idea, then compare it with the model answer after you submit.'])
ST = 'Fractions'
F = Fraction


def D(**k):
    k.setdefault('strand', ST)
    return k


def unit_pairs_search(f):
    f = F(f)
    out = []
    for a in range(1, 500):
        rest = f - F(1, a)
        if rest > 0 and rest.numerator == 1 and rest.denominator != a and a < rest.denominator:
            out.append((a, rest.denominator))
    return out


def fr_item(iid, tier, no, skill, f, q, check, hint, steps, src, units=(), simplest=False, also=(), svg=None):
    return D(id=iid, tier=tier, no=no, type='text', skill=skill, accept=frac_accepts(f, simplest=simplest, units=units, also=also), shown=frac_text(f),
             q=q, check=check, hint=hint, steps=steps, src=src, **({'svg': svg} if svg else {}))


# ---------------------------------------------------------------- checkers
def sticker_story(total=240):
    ben = total // 4
    rem = total - ben
    ali = rem * 2 // 3
    left = rem - ali
    return dict(ben=ben, rem=rem, ali=ali, left=left, frac=F(left, total))


def ravi_story(left_money):
    """Find the money Ravi had at first: he spends 2/5 on a game, then 1/2 of the remainder on a book, and has `left_money` left."""
    totals = []
    for total in range(1, 2000):
        rest = F(total) - F(2, 5) * total
        book = rest / 2
        if rest - book == left_money:
            totals.append((total, book))
    assert len(totals) == 1
    return totals[0]


def gap_bottoms(first_four, count):
    """Continue the bottom numbers 2, 6, 12, 20 ...: the gaps 4, 6, 8 grow by 2 each time (worked out from the numbers, not from a formula)."""
    b = list(first_four)
    gap = b[-1] - b[-2]
    while len(b) < count:
        gap += 2
        b.append(b[-1] + gap)
    return b


def digit_fraction_sums():
    out = []
    for a, b, c, d in itertools.permutations([1, 2, 3, 4]):
        out.append((F(a, b) + F(c, d), (a, b, c, d)))
    return out


def tank():
    for start in range(1, 500):
        w = F(start); hist = [w]
        for _ in range(3):
            w -= w / 3; hist.append(w)
        if hist[-1] == 16:
            half = next(h for h, x in enumerate(hist) if x < F(start, 2))
            return start, half, start - hist[half]


def egyptian_pairs(f):
    return unit_pairs_search(f)


def flat(pairs):
    return [x for p in pairs for x in p]


# ---------------------------------------------------------------- items
Q4_BOTTOMS = [2, 6, 12, 20]
BARS = F(1, 2) + F(1, 6)

ITEMS = [
    # ================= Start here (workbook lesson 2: Q1 to Q6)
    fr_item('1a', 'core', '1(a)', 'fraction and division', F(5, 8),
            'Sharing. Remember: 3 ÷ 4 = 3/4 (3 pizzas shared by 4 children).\n5 pizzas are shared equally among 8 children. How much of a pizza does each child get? Type a fraction.',
            lambda: frac_text(F((5 * 8) // 8, 8)),
            'Cut every pizza into 8 equal slices. How many slices are there altogether? How many slices does each child get?',
            ['Cut each of the 5 pizzas into 8 equal slices: 5 × 8 = 40 slices.', 'Share 40 slices among 8 children: 5 slices each, and each slice is 1/8 of a pizza.', 'Each child gets 5/8 of a pizza. (5 ÷ 8 = 5/8.)'],
            ['Sharing. Remember: 3 ÷ 4 = 3/4 (3 pizzas shared by 4 children).', '5 pizzas are shared equally among 8 children. Each gets  ______  of a pizza.'], units=['of a pizza', 'pizza']),
    D(id='1b', tier='core', no='1(b)', type='choice', skill='comparing fractions', options=['Group A', 'Group B'], answer='Group A',
      q='Group A shares 2 pizzas among 3 children. Group B shares 3 pizzas among 5 children. In which group does each child get more?',
      svg=share_bars(False), check=lambda: 'Group A' if F(2, 3) > F(3, 5) else 'Group B',
      hint='How much of a whole pizza is each child short of? Compare the two shortfalls.',
      steps=['Group A: each child gets 2/3 of a pizza. Group B: each child gets 3/5 of a pizza.', 'Use the same denominator: 2/3 = 10/15 and 3/5 = 9/15.', '10/15 is more than 9/15, so each child in Group A gets more.'],
      src=['Group A shares 2 pizzas among 3 children. Group B shares 3 pizzas among 5 children. In which group does each child get more? Explain.']),
    D(id='1bx', tier='core', no='1(b) explain', type='selfcheck', open=False, skill='comparing fractions',
      q='Explain your answer to 1(b). Hint: how much of a whole pizza is each child short of? Compare the two shortfalls. Write your explanation, then compare it with the model answer.',
      svg=share_bars(False), facts=dict(A=(2, 3), B=(3, 5)), check=lambda: dict(A=(2, 3), B=(3, 5)), sol_fig=lambda f: share_bars(True),
      hint='A child in Group A is short of 1 whole pizza by how much? And a child in Group B?',
      steps=['Each child in Group A gets 2/3 of a pizza, so is short of a whole pizza by 1/3.', 'Each child in Group B gets 3/5 of a pizza, so is short by 2/5.', 'Compare 1/3 and 2/5: 5/15 and 6/15. 1/3 is the smaller shortfall, so Group A gets more.', 'Or use the same denominator: 2/3 = 10/15 and 3/5 = 9/15.'],
      src=['how much of a whole pizza is each child short of? Compare the two shortfalls.']),

    D(id='2a', tier='core', no='2(a)', type='set', ordered=False, skill='unit fractions', answer=[4, 5],
      q='Write each fraction as the sum of two DIFFERENT unit fractions (1 on top): take away one unit fraction. Is what is left a unit fraction?\nWorked example: 7/10 − 1/2 = 7/10 − 5/10 = 2/10 = 1/5, so 7/10 = 1/2 + 1/5.\n9/20 = 1/□ + 1/□   (try 1/3, 1/4, 1/5 … in turn). Type the two bottom numbers.',
      check=lambda: sorted(unit_pairs_search(F(9, 20))[0]) if len(unit_pairs_search(F(9, 20))) == 1 else None,
      hint='Try 1/3: 9/20 − 1/3 is not a unit fraction. Try 1/4 next: write 1/4 as twentieths.',
      steps=['Try 1/3: 9/20 − 1/3 = 27/60 − 20/60 = 7/60. That is not a unit fraction.', 'Try 1/4: 9/20 − 5/20 = 4/20 = 1/5. Yes!', 'So 9/20 = 1/4 + 1/5. The bottom numbers are 4 and 5.'],
      src=['Write each fraction as the sum of two DIFFERENT unit fractions (1 on top): take away one unit fraction. Is what is left a unit fraction?']),
    D(id='2b', tier='core', no='2(b)', type='set', ordered=False, skill='unit fractions', answer=[2, 6],
      q='Write each fraction as the sum of two DIFFERENT unit fractions (1 on top): take away one unit fraction. Is what is left a unit fraction?\n2/3 = 1/□ + 1/□. Type the two bottom numbers.',
      check=lambda: sorted(unit_pairs_search(F(2, 3))[0]) if len(unit_pairs_search(F(2, 3))) == 1 else None,
      hint='1/2 is the biggest unit fraction that fits in 2/3. Take it away and see what is left.',
      steps=['Try 1/2: 2/3 − 1/2 = 4/6 − 3/6 = 1/6. That is a unit fraction.', 'So 2/3 = 1/2 + 1/6. (1/3 + 1/3 would use the same unit fraction twice, and the question says different.)', 'The bottom numbers are 2 and 6.'],
      src=['Write each fraction as the sum of two DIFFERENT unit fractions (1 on top): take away one unit fraction. Is what is left a unit fraction?']),

    D(id='3a', tier='core', no='3(a)', type='number', skill='fraction of a remainder', answer=120,
      q='Siti had 240 stickers. She gave 1/4 of them to Ben and 2/3 of the REMAINDER to Ali.\nHow many stickers did Ali get?', svg=sticker_bar(), check=lambda: sticker_story()['ali'],
      hint='Find the remainder first (what is left after Ben). Then take 2/3 of the remainder, not of 240.',
      steps=['Ben gets 1/4 of 240 = 60.', 'The remainder is 240 − 60 = 180.', 'Ali gets 2/3 of the remainder: 180 ÷ 3 = 60, and 60 × 2 = 120.'],
      src=['Siti had 240 stickers. She gave', 'of them to Ben and', 'of the REMAINDER to Ali.', 'How many stickers did Ali get?']),
    D(id='3b', tier='core', no='3(b)', type='number', skill='fraction of a remainder', answer=60,
      q='Siti had 240 stickers. She gave 1/4 of them to Ben and 2/3 of the REMAINDER to Ali.\nHow many stickers did Siti have left?', svg=sticker_bar(), check=lambda: sticker_story()['left'],
      hint='The remainder is 180. Ali took 120 of it. How many are left?',
      steps=['After Ben, the remainder is 240 − 60 = 180.', 'Ali gets 120 of the remainder.', 'Siti has 180 − 120 = 60 stickers left. (That is 1/3 of the remainder.)'],
      src=['How many stickers did Siti have left?']),
    fr_item('3c', 'core', '3(c)', 'fraction of a remainder', F(1, 4),
            'Siti had 240 stickers. She gave 1/4 of them to Ben and 2/3 of the REMAINDER to Ali.\nWhat fraction of her 240 stickers did Siti have left? Type a fraction.', lambda: frac_text(sticker_story()['frac']),
            'Siti has 60 stickers left out of 240. Write 60/240 and make it simpler.',
            ['Siti has 60 stickers left out of 240 stickers.', '60/240 = 1/4 (divide the top and the bottom by 60).', 'Or: after Ben 3/4 is left, Ali takes 2/3 of that (1/2 of the whole), so 3/4 − 1/2 = 1/4 is left.'],
            ['What fraction of her 240 stickers did Siti have left?'], also=['60/240'], svg=sticker_bar()),

    D(id='4a', tier='core', no='4(a)', type='fields', skill='patterns in fractions', answer=[30, 42],
      q='Look for a pattern: 1/2, 1/6, 1/12, 1/20, …\nWrite the next two fractions (type the bottom numbers).',
      frame='1/2, 1/6, 1/12, 1/20, 1/{f1}, 1/{f2}', check=lambda: gap_bottoms(Q4_BOTTOMS, 6)[4:],
      hint='Look at the bottom numbers: 2, 6, 12, 20. How much does each grow by? Does the growth change?',
      steps=['The bottom numbers are 2, 6, 12, 20. The gaps are 4, 6, 8: they grow by 2 each time.', 'The next gaps are 10 and 12: 20 + 10 = 30 and 30 + 12 = 42.', 'The next two fractions are 1/30 and 1/42.'],
      src=['Look for a pattern:']),
    D(id='4an', tier='core', no='4(a) notice', type='selfcheck', open=False, skill='patterns in fractions',
      q='What do you notice about the bottom numbers 2, 6, 12, 20, 30, 42? Write your idea.', facts=True,
      check=lambda: all(b == n * (n + 1) for n, b in enumerate([2, 6, 12, 20, 30, 42], 1)),
      hint='Try writing each bottom number as two numbers multiplied together: 2 = 1 × 2, 6 = 2 × 3, ...',
      steps=['The bottom numbers are 1 × 2, 2 × 3, 3 × 4, 4 × 5, 5 × 6 and 6 × 7.', 'Each bottom number is two neighbouring numbers multiplied together.', 'So the next one after 1/42 is 1/(7 × 8) = 1/56.'],
      src=['What do you notice about the bottom numbers?']),
    fr_item('4b1', 'core', '4(b)', 'adding fractions', F(2, 3),
            'Work out the sum. Give the answer in its simplest form.\n1/2 + 1/6 =', lambda: frac_text(F(1, 2) + F(1, 6)),
            'Use sixths: 1/2 = 3/6.', ['1/2 = 3/6, so 1/2 + 1/6 = 3/6 + 1/6 = 4/6.', '4/6 = 2/3 in its simplest form.'],
            ['Work out each sum. Give each answer in its simplest form.'], simplest=True),
    fr_item('4b2', 'core', '4(b)', 'adding fractions', F(3, 4),
            'Work out the sum. Give the answer in its simplest form.\n1/2 + 1/6 + 1/12 =', lambda: frac_text(F(1, 2) + F(1, 6) + F(1, 12)),
            'Use twelfths: 1/2 = 6/12 and 1/6 = 2/12.', ['In twelfths: 6/12 + 2/12 + 1/12 = 9/12.', '9/12 = 3/4 in its simplest form.'],
            ['Work out each sum. Give each answer in its simplest form.'], simplest=True),
    fr_item('4b3', 'core', '4(b)', 'adding fractions', F(4, 5),
            'Work out the sum. Give the answer in its simplest form.\n1/2 + 1/6 + 1/12 + 1/20 =', lambda: frac_text(F(1, 2) + F(1, 6) + F(1, 12) + F(1, 20)),
            'Use sixtieths (60 is a multiple of 2, 6, 12 and 20).', ['In sixtieths: 30/60 + 10/60 + 5/60 + 3/60 = 48/60.', '48/60 = 4/5 in its simplest form.'],
            ['Work out each sum. Give each answer in its simplest form.'], simplest=True),
    fr_item('4c', 'core', '4(c)', 'patterns in fractions', F(9, 10),
            'Predict: 1/2 + 1/6 + 1/12 + … + 1/90 = ?  Explain how you know. Type the answer as a fraction.',
            lambda: frac_text(sum((F(1, b) for b in gap_bottoms(Q4_BOTTOMS, 9)), F(0))) if gap_bottoms(Q4_BOTTOMS, 9)[-1] == 90 else None,
            'Look at your three sums: 2/3, 3/4, 4/5. What is the pattern? How many terms are there up to 1/90?',
            ['The sums so far are 2/3, 3/4 and 4/5. Each is 1 take away the next unit fraction: 1 − 1/3, 1 − 1/4, 1 − 1/5.', '1/90 is the 9th fraction (9 × 10 = 90), so the sum is 1 − 1/10.', 'The answer is 9/10.'],
            ['Predict:', 'Explain how you know.'], also=['1 - 1/10']),

    D(id='5a', tier='core', no='5(a)', type='number', skill='working backwards with a model', answer=120,
      q='Ravi spent 2/5 of his money on a game and 1/2 of the remainder on a book. He had $36 left. Use the model.\nHow much money did Ravi have at first? (Type the number of dollars.)',
      svg=ravi_bar(), check=lambda: ravi_story(36)[0],
      hint='Draw 5 equal parts; the game takes 2. Cut the rest to find half of it. Cut every part in half so all the units are equal.',
      steps=['Cut each of the 5 parts in half: the whole is 10 equal units.', 'The game takes 4 units. The remainder is 6 units. The book is half of the remainder, 3 units, and 3 units are left.', '3 units = $36, so 1 unit = $12.', 'Ravi had 10 units: 10 × $12 = $120.'],
      src=['Ravi spent', 'of his money on a game and', 'of the remainder on a book. He had $36 left. Use the model.', 'How much money did Ravi have at first?']),
    D(id='5b', tier='core', no='5(b)', type='number', skill='working backwards with a model', answer=36,
      q='Ravi spent 2/5 of his money on a game and 1/2 of the remainder on a book. He had $36 left. Use the model.\nHow much did the book cost? (Type the number of dollars.)',
      svg=ravi_bar(), check=lambda: int(ravi_story(36)[1]),
      hint='The book is half of the remainder, and the other half is the $36 he had left.',
      steps=['After the game, the remainder is split into two equal halves: the book and the money left.', 'The money left is $36, so the book also cost $36.', '(Check: the remainder is 3/5 of $120 = $72, and half of $72 is $36.)'],
      src=['How much did the book cost?']),

    D(id='6a', tier='core', no='6(a)', type='text', skill='testing every way', shown='5 1/2',
      accept=frac_accepts(F(11, 2), also=['4/1+3/2', '3/2+4/1', '4+3/2', '3/2+4']),
      q='Use the digit cards 1, 2, 3, 4 once each in the boxes (fractions need not be proper).\nThe largest sum you can make. Type the sum as a fraction or a mixed number, like 5 1/2.',
      svg=box_fractions([1, 2, 3, 4]), check=lambda: frac_text(max(digit_fraction_sums())[0]),
      hint='A big sum needs a big fraction. Put the 4 on top and the 1 on the bottom. Then try the other two cards both ways.',
      steps=['Try them all: there are 24 ways to put the four cards in the boxes.', 'The biggest is 4/1 + 3/2 = 4 + 1 1/2 = 5 1/2.', '5 1/2 is the same as 11/2.'],
      src=['Use the digit cards', 'once each in the boxes (fractions need not be proper).', 'The largest sum:']),
    D(id='6b', tier='core', no='6(b)', type='text', skill='testing every way', shown='5/6',
      accept=frac_accepts(F(5, 6), also=['1/3+2/4', '2/4+1/3']),
      q='Use the digit cards 1, 2, 3, 4 once each in the boxes (fractions need not be proper).\nThe smallest sum you can make. Did you test both ways? Type the sum as a fraction.',
      svg=box_fractions([1, 2, 3, 4]), check=lambda: frac_text(min(digit_fraction_sums())[0]),
      hint='A small sum needs small fractions: put the big digits on the bottom. But test both ways: 1/3 + 2/4 and 1/4 + 2/3.',
      steps=['Put the smaller digits on top and the bigger digits on the bottom.', '1/3 + 2/4 = 4/12 + 6/12 = 10/12 = 5/6. But 1/4 + 2/3 = 3/12 + 8/12 = 11/12 is bigger, so test both ways.', 'The smallest sum is 5/6.'],
      src=['The smallest sum:', 'Did you test both ways?']),

    # ================= Investigation: Is it always true? Test and explain
    D(id='C0', tier='invest', no='C (easy first step)', type='fields', skill='differences of unit fractions', answer=[3, 2, 1],
      q='Is it always true? Test and explain.\nEasy first step: cut a bar into 6 equal parts.',
      frame='1/2 is {f1} parts and 1/3 is {f2} parts, so 1/2 − 1/3 = {f3}/6',
      check=lambda: [int(F(1, 2) * 6), int(F(1, 3) * 6), int((F(1, 2) - F(1, 3)) * 6)],
      hint='A bar cut into 6 equal parts. Half of the bar is how many of the 6 parts? A third of the bar is how many parts?',
      steps=['Half of 6 parts is 3 parts, so 1/2 = 3/6.', 'A third of 6 parts is 2 parts, so 1/3 = 2/6.', '3/6 − 2/6 = 1/6. So 1/2 − 1/3 = 1/6.'],
      src=['Easy first step: cut a bar into 6 equal parts.']),
    D(id='Ca', tier='invest', no='C(a)', type='fields', skill='differences of unit fractions', answer=[12, 20, 30, 90, 420],
      q='Take two unit fractions that are next to each other, such as 1/3 and 1/4. Take the smaller from the bigger and try at least four more pairs. Each answer is a unit fraction: type its bottom number.',
      frame='1/3 − 1/4 = 1/{f1};   1/4 − 1/5 = 1/{f2};   1/5 − 1/6 = 1/{f3};   1/9 − 1/10 = 1/{f4};   1/20 − 1/21 = 1/{f5}',
      check=lambda: [(F(1, a) - F(1, a + 1)).denominator for a in (3, 4, 5, 9, 20)],
      hint='Write both fractions with a common denominator (multiply the two bottom numbers) and subtract the tops.',
      steps=['1/3 − 1/4 = 4/12 − 3/12 = 1/12.', '1/4 − 1/5 = 5/20 − 4/20 = 1/20.', '1/5 − 1/6 = 1/30 and 1/9 − 1/10 = 1/90.', '1/20 − 1/21 = 21/420 − 20/420 = 1/420.'],
      src=['Take two unit fractions that are next to each other, such as 1/3 and 1/4. Take the smaller away from the bigger: 1/3 − 1/4 = ______. Try at least four more pairs (1/4 and 1/5, 1/5 and 1/6, 1/9 and 1/10, 1/20 and 1/21).']),
    D(id='Cb', tier='invest', no='C(b)', type='selfcheck', open=False, skill='explaining a pattern', facts=True,
      q='What do you notice about the answer each time? Write your idea in words. Is it always true? Explain with a drawing (hint: cut a bar into 3 × 4 = 12 equal parts).',
      check=lambda: all(F(1, n) - F(1, n + 1) == F(1, n * (n + 1)) for n in range(1, 2000)), sol_fig=lambda f: twelve_bar(),
      hint='Look at the bottom number of each answer. How is it made from the two bottom numbers of the fractions?',
      steps=['Each answer is a unit fraction whose bottom number is the two bottom numbers multiplied: 3 × 4 = 12, 4 × 5 = 20, 5 × 6 = 30, 9 × 10 = 90 and 20 × 21 = 420.', 'It is always true for neighbouring unit fractions. Cut a bar into n × (n + 1) equal parts: 1/n is (n + 1) parts and 1/(n + 1) is n parts, so the difference is 1 part, which is 1/(n × (n + 1)).', 'The picture shows 1/3 and 1/4 on a bar of 12 parts: 4 parts and 3 parts, a difference of 1 part.'],
      src=['What do you notice about the answer each time? Write your idea in words. Is it always true? Explain with a drawing (hint: cut a bar into 3 × 4 = 12 equal parts).']),
    fr_item('Cc', 'invest', 'C(c)', 'differences of unit fractions', F(3, 10),
            'Use your idea to write 1/6 + 1/12 + 1/20 as one fraction without finding a common denominator. Type the fraction.',
            lambda: frac_text(F(1, 6) + F(1, 12) + F(1, 20)),
            'Write each fraction as a difference: 1/6 = 1/2 − 1/3. What happens to the middle parts?',
            ['1/6 = 1/2 − 1/3, 1/12 = 1/3 − 1/4 and 1/20 = 1/4 − 1/5.', 'Add them: (1/2 − 1/3) + (1/3 − 1/4) + (1/4 − 1/5). The middle parts cancel.', '1/2 − 1/5 = 5/10 − 2/10 = 3/10. Check: 10/60 + 5/60 + 3/60 = 18/60 = 3/10.'],
            ['Use your idea to write 1/6 + 1/12 + 1/20 as one fraction without finding a common denominator.']),

    # ================= Think harder (A1 to A4)
    D(id='A1', tier='stretch', no='A1', type='fields', skill='unit fractions', answer=[3, 24, 4, 8],
      q='Write 3/8 as the sum of two different unit fractions in TWO different ways.\nIn each way write the smaller bottom number first, and write the way with the smaller first bottom number first.',
      frame='Way 1:  3/8 = 1/{f1} + 1/{f2}.     Way 2:  3/8 = 1/{f3} + 1/{f4}.',
      check=lambda: flat(sorted(unit_pairs_search(F(3, 8)))),
      hint='Test 1/3, 1/4, 1/5, … in order. Take each one away from 3/8: is what is left a unit fraction?',
      steps=['1/2 is too big (it is more than 3/8). Try 1/3: 3/8 − 1/3 = 9/24 − 8/24 = 1/24. Yes! 3/8 = 1/3 + 1/24.', 'Try 1/4: 3/8 − 1/4 = 3/8 − 2/8 = 1/8. Yes! 3/8 = 1/4 + 1/8.', 'Try 1/5: 3/8 − 1/5 = 15/40 − 8/40 = 7/40, not a unit fraction.', 'The two ways: 1/3 + 1/24 and 1/4 + 1/8.'],
      src=['Write 3/8 as the sum of two different unit fractions in TWO different ways. How do you know when to stop looking?']),
    D(id='A1s', tier='stretch', no='A1 (stop)', type='selfcheck', open=False, skill='knowing when to stop', facts=[3, 4, 5],
      q='How do you know when to stop looking for ways to write 3/8 as the sum of two different unit fractions? Write your idea.',
      check=lambda: [a for a in range(2, 20) if F(1, a) < F(3, 8) and F(1, a) >= F(3, 8) / 2],
      hint='The first unit fraction is the bigger one of the two. How small can the bigger one be?',
      steps=['The bigger unit fraction must be at least half of 3/8 (two equal halves would be the same fraction twice).', 'Half of 3/8 is 3/16. 1/5 is bigger than 3/16 but 1/6 is smaller. So test 1/3, 1/4 and 1/5 (1/2 is too big) and then stop.', '1/5 leaves 7/40, which is not a unit fraction. After 1/5, the first fraction is less than half of 3/8, so there are no more ways.'],
      src=['How do you know when to stop looking?']),
    fr_item('A2', 'stretch', 'A2', 'fraction of a remainder', F(1, 2),
            'Ben ate 1/3 of a pizza. Ali ate 1/4 of what was left. What fraction of the pizza is left? Type a fraction.', lambda: frac_text(F(1) - F(1, 3) - F(1, 4) * (F(1) - F(1, 3))),
            'After Ben, how much of the pizza is left? Ali ate 1/4 of THAT, not 1/4 of the whole pizza.',
            ['After Ben ate 1/3, 2/3 of the pizza was left.', 'Ali ate 1/4 of what was left: 1/4 of 2/3 = 2/12 = 1/6 of the pizza.', 'Left: 2/3 − 1/6 = 4/6 − 1/6 = 3/6 = 1/2. (Or: 3/4 of 2/3 is left = 1/2.)'],
            ['Ben ate 1/3 of a pizza. Ali ate 1/4 of what was left. What fraction of the pizza is left?']),
    D(id='A3', tier='stretch', no='A3', type='fields', skill='patterns in fractions', answer=[20, 90],
      q='1/2 − 1/3 = 1/6 and 1/3 − 1/4 = 1/12. Use the pattern to work out 1/4 − 1/5 and 1/9 − 1/10. Type the bottom numbers.',
      frame='1/4 − 1/5 = 1/{f1}     1/9 − 1/10 = 1/{f2}', check=lambda: [(F(1, 4) - F(1, 5)).denominator, (F(1, 9) - F(1, 10)).denominator],
      hint='Look at the bottom numbers in the two examples: 2 and 3 gave 6, 3 and 4 gave 12. What did we do to 2 and 3?',
      steps=['1/2 − 1/3 = 1/6 (2 × 3 = 6) and 1/3 − 1/4 = 1/12 (3 × 4 = 12): the new bottom number is the two bottom numbers multiplied.', '1/4 − 1/5 = 1/(4 × 5) = 1/20.', '1/9 − 1/10 = 1/(9 × 10) = 1/90.'],
      src=['1/2 − 1/3 = 1/6 and 1/3 − 1/4 = 1/12. Use the pattern to work out 1/4 − 1/5 and 1/9 − 1/10.']),
    fr_item('A4', 'stretch', 'A4', 'fraction and division', F(2, 3),
            '4 litres of juice are poured equally into 6 bottles. How much juice is in each bottle? Type a fraction of a litre.', lambda: frac_text(F(4, 6)),
            'Cut each litre into 6 equal parts. How many parts of juice are there? How many go in each bottle?',
            ['4 litres ÷ 6 bottles = 4/6 of a litre in each bottle.', '4/6 = 2/3 in its simplest form.'],
            ['4 litres of juice are poured equally into 6 bottles. How much juice is in each bottle?'], units=['litre', 'litres', 'l', 'of a litre']),

    # ================= Go further (B1 to B3)
    fr_item('B1', 'challenge', 'B1', 'differences of unit fractions', F(5, 14),
            'Work out 1/6 + 1/12 + 1/20 + 1/30 + 1/42 without finding a common denominator for all five. (Hint: 1/6 = 1/2 − 1/3.) Type the fraction.',
            lambda: frac_text(sum((F(1, b) for b in (6, 12, 20, 30, 42)), F(0))),
            'Write every fraction as a difference of two neighbouring unit fractions. What cancels?',
            ['1/6 = 1/2 − 1/3, 1/12 = 1/3 − 1/4, 1/20 = 1/4 − 1/5, 1/30 = 1/5 − 1/6 and 1/42 = 1/6 − 1/7.', 'Add them: the middle parts cancel, leaving 1/2 − 1/7.', '1/2 − 1/7 = 7/14 − 2/14 = 5/14.'],
            ['Work out 1/6 + 1/12 + 1/20 + 1/30 + 1/42 without finding a common denominator for all five. (Hint: 1/6 = 1/2 − 1/3.)']),
    D(id='B2', tier='challenge', no='B2', type='fields', skill='unit fractions', answer=[3, 12, 4, 6],
      q='5 pizzas are shared equally among 12 children. Each child must get exactly 2 pieces, and each piece must be a unit fraction of a pizza (like 1/3 or 1/4). Each child gets 5/12. Find the two ways.\nIn each way write the smaller bottom number first, and write the way with the smaller first bottom number first.',
      frame='Way 1:  5/12 = 1/{f1} + 1/{f2}.     Way 2:  5/12 = 1/{f3} + 1/{f4}.',
      check=lambda: flat(sorted(unit_pairs_search(F(5, 12)))),
      hint='Each child gets 5 ÷ 12 = 5/12 of a pizza. Write 5/12 as the sum of two different unit fractions: test 1/3, 1/4, ...',
      steps=['Each child gets 5/12 of a pizza.', 'Try 1/3: 5/12 − 4/12 = 1/12. So 5/12 = 1/3 + 1/12: cut 4 pizzas into thirds (12 thirds) and 1 pizza into twelfths (12 twelfths).', 'Try 1/4: 5/12 − 3/12 = 2/12 = 1/6. So 5/12 = 1/4 + 1/6: cut 3 pizzas into quarters (12 quarters) and 2 pizzas into sixths (12 sixths).', 'Two ways: 1/3 + 1/12 and 1/4 + 1/6.'],
      src=['5 pizzas are shared equally among 12 children. Each child must get exactly 2 pieces, and each piece must be a unit fraction of a pizza (like 1/3 or 1/4). How can the pizzas be cut?']),
    D(id='B3a', tier='challenge', no='B3(a)', type='number', skill='fraction of a remainder', answer=54,
      q='A tank is full of water. Every hour, 1/3 of the water that is in the tank is let out. After 3 hours there are 16 litres left.\nHow much water was in the full tank? (Type the number of litres.)', check=lambda: tank()[0],
      hint='Each hour 2/3 of the water is left. Work backwards from 16 litres: what was there an hour earlier?',
      steps=['Each hour 1/3 is let out, so 2/3 is left.', 'Work backwards: 16 is 2/3 of the water an hour before, so that was 16 ÷ 2 × 3 = 24 litres.', 'Again: 24 ÷ 2 × 3 = 36 litres, and again 36 ÷ 2 × 3 = 54 litres.', 'The full tank held 54 litres (54 → 36 → 24 → 16).'],
      src=['A tank is full of water. Every hour, 1/3 of the water that is in the tank is let out. After 3 hours there are 16 litres left.', '(a) How much water was in the full tank?']),
    D(id='B3b', tier='challenge', no='B3(b)', type='number', skill='fraction of a remainder', answer=2,
      q='The tank held 54 litres at first. Every hour, 1/3 of the water that is in the tank is let out.\nAfter how many hours is less than half of the original water left?', check=lambda: tank()[1],
      hint='Half of 54 litres is 27 litres. Write the amount of water after 1 hour, 2 hours, 3 hours.',
      steps=['Half of 54 is 27 litres.', 'After 1 hour: 36 litres, which is more than 27.', 'After 2 hours: 24 litres, which is less than 27.', 'So after 2 hours there is less than half left.'],
      src=['(b) After how many hours is less than half of the original water left?']),
    D(id='B3c', tier='challenge', no='B3(c)', type='number', skill='fraction of a remainder', answer=30,
      q='The tank held 54 litres at first. How much water has been let out by the time less than half is left? (Type the number of litres.)', check=lambda: int(tank()[2]),
      hint='By then there are 24 litres in the tank. How much has gone?',
      steps=['By then 24 litres are left.', '54 − 24 = 30 litres have been let out.'],
      src=['(c) How much water has been let out by then?']),
    D(id='pose', tier='challenge', no='Make up your own', type='selfcheck', open=True, skill='making up a puzzle',
      q='Make up your own. Pick a fraction and write it as the sum of two different unit fractions. Challenge a partner to find your two. (Think for 30 seconds before anyone speaks.)',
      hint='Pick two different unit fractions, such as 1/3 and 1/8, and add them. The sum is your puzzle.',
      steps=['This question is open: many puzzles are right.', 'To make a puzzle you can be sure about, choose the two unit fractions first, such as 1/3 + 1/8 = 8/24 + 3/24 = 11/24, and then give your partner 11/24.', 'Check by taking away unit fractions in order, as in Q2.'],
      src=['Pick a fraction and write it as the sum of two different unit fractions. Challenge a partner to find your two.']),
]


# ---------------------------------------------------------------- variants: number items with a template and an oracle
def _sticker(e):
    return sticker_story(e['T'])


def _gap_oracle(e):
    s = e['s']
    first = [s * (s + 1), (s + 1) * (s + 2), (s + 2) * (s + 3), (s + 3) * (s + 4)]
    b = gap_bottoms(first, 6)
    return dict(f1=b[4], f2=b[5])


VARIANTS = {
    '3a': dict(
        base=dict(T=240),
        tpl=dict(vars=dict(T=[120, 240, 360, 480, 600, 720]), q='Siti had {T} stickers. She gave 1/4 of them to Ben and 2/3 of the REMAINDER to Ali.\nHow many stickers did Ali get?', answer='(T - T/4) * 2 / 3',
                 hint='Find the remainder first. Then take 2/3 of the remainder, not of {T}.',
                 steps=['Ben gets 1/4 of {T}, and the remainder is the other 3/4.', '2/3 of the remainder goes to Ali. Share the remainder into 3 equal parts and take 2 of them.', 'Ali gets {ans} stickers.']),
        oracle=lambda e: _sticker(e)['ali']),
    '3b': dict(
        base=dict(T=240),
        tpl=dict(vars=dict(T=[120, 240, 360, 480, 600, 720]), q='Siti had {T} stickers. She gave 1/4 of them to Ben and 2/3 of the REMAINDER to Ali.\nHow many stickers did Siti have left?', answer='(T - T/4) / 3',
                 hint='Ali took 2/3 of the remainder. What fraction of the remainder is left?',
                 steps=['Ben gets 1/4 of {T}, and the remainder is 3/4 of {T}.', 'Ali takes 2/3 of the remainder, so 1/3 of the remainder is left.', 'Siti has {ans} stickers left.']),
        oracle=lambda e: _sticker(e)['left']),
    '4a': dict(
        base=dict(s=1),
        tpl=dict(vars=dict(s=[1, 2, 3, 4, 5, 6]), q='Look for a pattern. Write the next two fractions (type the bottom numbers).',
                 frame='1/{a}, 1/{b}, 1/{c}, 1/{d}, 1/{f1}, 1/{f2}', answers=dict(f1='(s+4)*(s+5)', f2='(s+5)*(s+6)'),
                 derive=dict(a='s*(s+1)', b='(s+1)*(s+2)', c='(s+2)*(s+3)', d='(s+3)*(s+4)'),
                 hint='Look at the bottom numbers {a}, {b}, {c}, {d}. How much does each grow by? Does the growth change?',
                 steps=['The bottom numbers are {a}, {b}, {c}, {d}. The gaps between them grow by 2 each time.', 'Keep going with the growing gaps to get the next two bottom numbers.', 'The next two fractions have bottom numbers {ans}.']),
        oracle=_gap_oracle),
    '5a': dict(
        base=dict(L=36),
        tpl=dict(vars=dict(L=[18, 21, 24, 30, 36, 42, 48, 60]), q='Ravi spent 2/5 of his money on a game and 1/2 of the remainder on a book. He had ${L} left.\nHow much money did Ravi have at first? (Type the number of dollars.)', answer='L * 10 / 3',
                 hint='Cut each fifth in half to make 10 equal units. How many units are left?',
                 steps=['With 10 equal units, the game takes 4, the book takes 3 and 3 units are left.', '3 units = ${L}, so 1 unit = ${L} ÷ 3.', 'Ravi had 10 units, which is ${ans}.']),
        oracle=lambda e: ravi_story(e['L'])[0]),
}
