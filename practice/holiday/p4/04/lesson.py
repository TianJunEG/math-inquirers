"""Online practice for Level 4 (Primary 4, ages 9-11) holiday lesson 4: Fraction Frontier (Fractions).

The questions are the ones printed in the Level 4 holiday workbook, built by p4/workbook_html.js from p4/content/l4.js:
  Start here  = l4.js workbook() Q1 to Q6;   Investigation = l4.js gaps.invest (Sharing 24 stickers);
  Think harder = l4.js qbank.stretch[0:4];     Go further = l4.js qbank.challenge[-3:]  (printed as Q5 to Q7).
Every answer is recomputed by an INDEPENDENT checker (exact fractions, counting out equal groups, a search over the numbers in the question), never a copy of
the printed answer; build_holiday.py stops if a checker and the printed answer differ.  The printed answers are the l4.js `key`, `gaps.invest.key` and `qbank` answers.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from p4lib import *      # noqa: E402,F401

META = dict(level=4, lesson=4, key='p4', title='Fraction Frontier', workbook_title='FRACTION FRONTIER', topic='Fractions',
            strand='Fractions',
            sources=['p4/content/l4.js'],
            intro=['Type a fraction with a slash, like 3/4, and a mixed number with a space, like 2 3/4. When a question only asks for a number, you may write it as an equal fraction or a mixed number if it is the same size.',
                   'Some questions ask you to explain, to make up your own puzzle, or to mark a number line. Do those in your head or on paper, then compare with the answer after you submit.'])
S4 = 'Fractions'


def D(**k):
    return dict(strand=S4, **k)


def share(total, groups):
    """Items in one group when `total` is shared equally into `groups` groups (found by trying 1, 2, 3 ...)."""
    for g in range(1, total + 1):
        if g * groups == total:
            return g
    return None


def frac_of_set(total, a, d):
    return a * share(total, d)


def text_frac(iid, tier, no, skill, value, q, hint, steps, src, mode='any', svg=None):
    """A typed fraction. mode: 'improper' = only n/d, 'mixed' = only w n/d, 'both' = either, 'any' = any equal fraction, mixed number or decimal."""
    f = Fr(value)
    if mode == 'improper':
        acc, rep = [frac_text(f)], frac_text(f)
    elif mode == 'mixed':
        acc, rep = [mixed_text(f)], mixed_text(f)
    elif mode == 'both':
        acc, rep = sorted({frac_text(f), mixed_text(f)}), frac_text(f)
    else:
        acc, rep = frac_accepts(f), frac_text(f)
    assert rep in acc
    return D(id=iid, tier=tier, no=no, type='text', skill=skill, accept=acc, shown=rep if mode != 'any' else (rep if f.denominator == 1 or f < 1 else f'{rep} (or {mixed_text(f)})'),
             check=lambda: rep, q=q, hint=hint, steps=steps, src=src, **({'svg': svg} if svg else {}))


def cmp_item(iid, no, a, b, q, hint, steps, src, svg=None):
    (an, ad), (bn, bd) = a, b
    sym = '>' if Fr(an, ad) > Fr(bn, bd) else '<'
    opts = [f'{an}/{ad} > {bn}/{bd}', f'{an}/{ad} < {bn}/{bd}']
    return D(id=iid, tier='core', no=no, type='choice', options=opts, answer=f'{an}/{ad} {sym} {bn}/{bd}', skill='comparing fractions',
             check=lambda: f'{an}/{ad} ' + ('>' if Fr(an, ad) > Fr(bn, bd) else '<') + f' {bn}/{bd}', q=q, hint=hint, steps=steps, src=src, **({'svg': svg} if svg else {}))


def fractions_in_order(fracs):
    return ', '.join(f'{f.numerator}/{f.denominator}' for f in sorted(Fr(*x) for x in fracs))


SHADED = [i < 13 for i in range(15)]           # the 3 bars of Q1: 15 fifths, the first 13 shaded
ARROWS = (('A', 3), ('B', 7), ('C', 10))        # arrows of Q2 in quarters

ITEMS = [
    # ================= Start here (workbook lesson 4, Q1 to Q6)
    D(id='1a-count', tier='core', no='1(a)', type='number', skill='counting parts of a whole', answer=13, svg=whole_bars(15, 5, 13), check=lambda: sum(SHADED),
      q='Each bar is one whole, and is cut into fifths. How many fifths are shaded?', hint='Count the shaded parts in each bar, then add them up.',
      steps=['Each bar has 5 equal parts. The first two bars are shaded all the way: 5 + 5 = 10 fifths.', 'The third bar has 3 parts shaded.', '10 + 3 = 13 fifths are shaded.'],
      src=['Each bar is one whole. Draw more bars if you need them.', 'Fifths shaded:']),
    text_frac('1a-impr', 'core', '1(a) improper', 'improper fractions and mixed numbers', Fr(13, 5),
              'Each bar is one whole. Write the shaded part as an improper fraction. (An improper fraction is 1 or more, like 7/4.)',
              'An improper fraction has the number of shaded parts on the top and the number of parts in one whole on the bottom.',
              ['The shaded part is 13 fifths, so the top number is 13.', 'The bottom number is 5, because each whole is cut into fifths.', 'The improper fraction is 13/5.'],
              ['1 or more, like', 'Improper fraction'], mode='improper', svg=whole_bars(15, 5, 13)),
    text_frac('1a-mixed', 'core', '1(a) mixed', 'improper fractions and mixed numbers', Fr(13, 5),
              'Each bar is one whole. Write the shaded part as a mixed number. (A mixed number is a whole number and a fraction, like 1 3/4.)',
              'How many whole bars are shaded? How many fifths are shaded in the bar that is left?',
              ['Two bars are shaded all the way: 2 wholes.', 'The third bar has 3 of its 5 parts shaded: 3/5.', 'The mixed number is 2 3/5.'],
              ['a whole number and a fraction, like', 'Mixed number'], mode='mixed', svg=whole_bars(15, 5, 13)),
    text_frac('1b', 'core', '1(b)', 'improper fractions and mixed numbers', Fr(19, 4), 'Write 19/4 as a mixed number.',
              'Four quarters make one whole. How many whole ones can you make from 19 quarters, and how many quarters are left over?',
              ['4 quarters make 1 whole. 19 ÷ 4 = 4 remainder 3, so there are 4 wholes and 3 quarters left over.', '19/4 = 4 3/4.'],
              ['Write', 'as a mixed number.'], mode='mixed'),
    text_frac('1c', 'core', '1(c)', 'improper fractions and mixed numbers', Fr(17, 5), 'Write 3 2/5 as an improper fraction.',
              'Each whole is 5 fifths. How many fifths are there in 3 wholes? Then add the 2 fifths.',
              ['Each whole is 5 fifths, so 3 wholes are 3 × 5 = 15 fifths.', 'Add the 2 fifths: 15 + 2 = 17 fifths.', '3 2/5 = 17/5.'],
              ['Write', 'as an improper fraction.'], mode='improper'),
    D(id='1d', tier='core', no='1(d)', type='number', skill='counting parts of a whole', answer=40, check=lambda: sum(8 for _ in range(5)),
      q='How many eighths are there in 5 wholes?', hint='How many eighths make 1 whole?',
      steps=['1 whole = 8 eighths.', '5 wholes = 5 × 8 = 40 eighths.'], src=['How many eighths are there in 5 wholes?']),

    text_frac('2a-A', 'core', '2(a) A', 'fractions on a number line', Fr(3, 4), 'This number line is marked in quarters. What number is at arrow A?',
              'Count the small steps from 0 to the arrow. Each small step is one quarter.',
              ['Each small step is 1 quarter, 1/4.', 'Arrow A is 3 small steps after 0, so A = 3/4.'],
              ['This number line is marked in quarters.', 'Write the number at each arrow.'], svg=quarter_line(ARROWS)),
    text_frac('2a-B', 'core', '2(a) B', 'fractions on a number line', Fr(7, 4), 'This number line is marked in quarters. What number is at arrow B?',
              'Count the small steps from 0. Four quarters take you to 1.',
              ['Arrow B is 7 small steps after 0, so B = 7/4.', '4 quarters make 1 whole, so 7/4 = 1 3/4. Both ways of writing it are right.'],
              ['This number line is marked in quarters.', 'Write the number at each arrow.'], svg=quarter_line(ARROWS)),
    text_frac('2a-C', 'core', '2(a) C', 'fractions on a number line', Fr(10, 4), 'This number line is marked in quarters. What number is at arrow C?',
              'Count the small steps from 0. Four quarters take you to 1, and eight take you to 2.',
              ['Arrow C is 10 small steps after 0, so C = 10/4.', '10 quarters = 2 wholes and 2 quarters = 2 2/4, which is the same as 2 1/2. Any of these is right.'],
              ['This number line is marked in quarters.', 'Write the number at each arrow.'], svg=quarter_line(ARROWS)),
    D(id='2b', tier='core', no='2(b)', type='selfcheck', paper=True, skill='fractions on a number line', facts=Fr(9, 4), check=lambda: Fr(2 * 4 + 1, 4),
      svg=quarter_line(), sol_fig=lambda f: quarter_line(cross=float(f)),
      q='Mark 9/4 on the number line with an X.',
      hint='Count quarters from 0. Four quarters take you to 1. How many quarters take you to 2? How many more are left?',
      steps=['9/4 means 9 quarters. 4 quarters make 1 and 8 quarters make 2.', '9/4 = 2 1/4: go to the 2, then one more small step.', 'Put your X on the first small mark after 2.'],
      src=['Mark', 'on the number line with an X.']),

    D(id='3a', tier='core', no='3(a)', type='number', skill='fraction of a set', answer=9, svg=set_bar(8, '24 children'), check=lambda: frac_of_set(24, 3, 8),
      q='Fraction of a set. There are 24 children in a class. 3/8 of them wear glasses. Use the bar model. How many children wear glasses?',
      hint='The bar is cut into 8 equal units that share the 24 children. How many children are in one unit?',
      steps=['8 units = 24 children, so 1 unit = 24 ÷ 8 = 3 children.', '3/8 means 3 units: 3 × 3 = 9 children wear glasses.'],
      src=['Fraction of a set. There are 24 children in a class.', 'of them wear glasses. Use the bar model.']),
    D(id='3b', tier='core', no='3(b)', type='number', skill='fraction of a set', answer=15, svg=set_bar(8, '24 children'), check=lambda: 24 - frac_of_set(24, 3, 8),
      q='There are 24 children in a class. 3/8 of them wear glasses. How many children do NOT wear glasses?',
      hint='The other units are the children without glasses. How many units is that?',
      steps=['3 units wear glasses, so 8 − 3 = 5 units do not.', '5 units = 5 × 3 = 15 children.', 'Check: 9 + 15 = 24.'],
      src=['How many do NOT wear glasses?']),

    D(id='4-start', tier='core', no='4 (start here)', type='number', skill='equal fractions', answer=6, check=lambda: 3 * share(8, 4),
      q='Compare. Start here: a paper strip is folded into quarters, and then each quarter is folded in half. That makes eighths. 3 quarters = ____ eighths.',
      hint='How many eighths make one quarter?',
      steps=['Each quarter is folded in half, so 1 quarter = 2 eighths.', '3 quarters = 3 × 2 = 6 eighths.'],
      src=['Compare.', 'fold a strip into quarters, then fold each quarter in half. 3 quarters =']),
    cmp_item('4a', '4(a)', (3, 4), (5, 8), 'Compare 3/4 and 5/8. Which is true? A drawing helps.',
             'Make the bottom numbers the same. Which of the two fractions can be written with 8 on the bottom?',
             ['Write 3/4 in eighths: 3/4 = 6/8.', '6/8 is more than 5/8, so 3/4 > 5/8.'], ['Compare. Write > or < in each box.']),
    cmp_item('4b', '4(b)', (2, 3), (7, 12), 'Compare 2/3 and 7/12. Which is true?',
             'Make the bottom numbers the same. What can you multiply 3 by to make 12?',
             ['3 × 4 = 12, so write 2/3 in twelfths: 2/3 = 8/12.', '8/12 is more than 7/12, so 2/3 > 7/12.'], ['Compare. Write > or < in each box.']),
    cmp_item('4c', '4(c)', (4, 9), (5, 8), 'Compare 4/9 and 5/8. The bars are the same length. Which is true?',
             'Is each fraction more or less than one half? Look at the bars.',
             ['Half of 9 is 4 1/2. 4 is less than 4 1/2, so 4/9 is less than a half.', 'Half of 8 is 4. 5 is more than 4, so 5/8 is more than a half.', 'So 4/9 < 5/8.'],
             ['In (c), write how you know.'], svg=compare_bars()),
    D(id='4c-why', tier='core', no='4(c) how you know', type='selfcheck', open=True, skill='comparing fractions', svg=compare_bars(),
      q='How do you know which of 4/9 and 5/8 is bigger? The bars are the same length. Write why.',
      hint='Try comparing each fraction with one half, or look at how much of each bar is shaded.',
      steps=['One reason: compare each fraction with one half. 4/9 is less than a half, because 4 is less than half of 9. 5/8 is more than a half, because 5 is more than half of 8.', 'So 5/8 is bigger. Any clear reason is good, for example by looking at the shaded bars, or by making the bottom numbers the same (72).'],
      src=['The bars are the same length. Why?']),
    cmp_item('4d', '4(d)', (3, 5), (3, 7), 'Compare 3/5 and 3/7. Which is true?',
             'Both fractions have 3 pieces. Think about the size of one piece in each.',
             ['Both fractions have 3 pieces, so compare the size of the pieces.', 'A whole cut into 5 equal parts has bigger pieces than a whole cut into 7 equal parts. Fifths are bigger than sevenths.', 'So 3/5 > 3/7.'],
             ['Compare.']),
    D(id='4e', tier='core', no='4(e)', type='text', skill='ordering fractions', accept=joined_forms(['7/12', '2/3', '5/6'], True), shown='7/12, 2/3, 5/6',
      check=lambda: fractions_in_order([(2, 3), (5, 6), (7, 12)]),
      q='Put in order, smallest first: 2/3, 5/6, 7/12. Type the three fractions with commas between them.',
      hint='Change them all into fractions with the same bottom number, then put the top numbers in order.',
      steps=['Make the bottom numbers the same: 12 is a multiple of 3, 6 and 12.', '2/3 = 8/12, 5/6 = 10/12, and 7/12 stays 7/12.', 'The tops in order: 7, 8, 10. So the order is 7/12, 2/3, 5/6.'],
      src=['Put in order, smallest first:']),

    D(id='5-start', tier='core', no='5 (start here)', type='number', skill='finding the whole from a part', answer=9, check=lambda: share(27, 3),
      q='3/5 of the sweets in a jar are red. There are 27 red sweets. Start here: put 27 counters into 3 equal groups. How many counters are in each group?',
      hint='Share the 27 counters equally between the 3 groups.',
      steps=['27 ÷ 3 = 9 counters in each group.', 'The 3 groups are the 3 red parts of the jar, and each part holds 9 sweets.'],
      src=['of the sweets in a jar are red. There are 27 red sweets.', 'put 27 counters into 3 equal groups.']),
    D(id='5a', tier='core', no='5(a)', type='number', skill='finding the whole from a part', answer=45, svg=jar_bar(),
      check=lambda: [n for n in range(1, 500) if n % 5 == 0 and 3 * (n // 5) == 27][0],
      q='3/5 of the sweets in a jar are red. There are 27 red sweets. Use the bar model: the whole jar is cut into 5 equal parts. How many sweets are in the jar?',
      hint='The 3 red parts hold 27 sweets. How many sweets are in one part? Then how many parts make the whole jar?',
      steps=['3 units = 27 sweets, so 1 unit = 27 ÷ 3 = 9 sweets.', 'The whole jar is 5 units: 5 × 9 = 45 sweets.'],
      src=['Use the bar model: the whole jar is cut into 5 equal parts. How many sweets are in the jar?']),
    D(id='5b', tier='core', no='5(b)', type='number', skill='finding the whole from a part', answer=18, svg=jar_bar(),
      check=lambda: [n for n in range(1, 500) if n % 5 == 0 and 3 * (n // 5) == 27][0] - 27,
      q='3/5 of the sweets in a jar are red. There are 27 red sweets. How many sweets are NOT red?',
      hint='How many parts of the jar are not red? How many sweets is one part?',
      steps=['2 parts of the jar are not red (5 − 3 = 2).', '1 part = 9 sweets, so 2 parts = 18 sweets.', 'Check: 27 + 18 = 45, the whole jar.'],
      src=['How many sweets are NOT red?']),

    D(id='6-start', tier='core', no='6 (start here)', type='fields', skill='fractions between two fractions', frame='1/3 of the 12 boxes is {f1} boxes.   3/4 of the 12 boxes is {f2} boxes.',
      answer=[4, 9], svg=twelfths_strip(), check=lambda: [share(12, 3), 3 * share(12, 4)],
      q='Find ALL the fractions with denominator 12 that are bigger than 1/3 but smaller than 3/4. Start here: look at the strip of 12 boxes. How many boxes make 1/3 of the strip, and how many make 3/4 of the strip?',
      hint='Share the 12 boxes equally into 3 groups for 1/3. For 3/4, share into 4 equal groups and take 3.',
      steps=['1/3 of 12: 12 ÷ 3 = 4 boxes.', '3/4 of 12: 12 ÷ 4 = 3 boxes in a group, and 3 groups = 9 boxes.', 'So 1/3 = 4/12 and 3/4 = 9/12.'],
      src=['Find ALL the fractions with denominator 12 that are bigger than', 'on the strip, shade']),
    D(id='6a', tier='core', no='6(a)', type='text', skill='fractions between two fractions', accept=joined_forms(['5/12', '6/12', '7/12', '8/12'], False), shown='5/12, 6/12, 7/12, 8/12',
      svg=twelfths_strip(), check=lambda: ', '.join(f'{k}/12' for k in range(1, 12) if Fr(1, 3) < Fr(k, 12) < Fr(3, 4)),
      q='Find ALL the fractions with denominator 12 that are bigger than 1/3 but smaller than 3/4. Type them with commas between them, like 2/12, 3/12.',
      hint='Change 1/3 and 3/4 into twelfths first (see Start here). Which tops are in between?',
      steps=['1/3 = 4/12 and 3/4 = 9/12.', 'The fractions in between have the tops 5, 6, 7 and 8: 5/12, 6/12, 7/12, 8/12.', '4/12 and 9/12 are equal to 1/3 and 3/4, so they do not count.'],
      src=['Find ALL the fractions with denominator 12 that are bigger than', 'Fractions found, and how many:']),
    D(id='6b', tier='core', no='6(b)', type='number', skill='fractions between two fractions', answer=4, check=lambda: len([k for k in range(1, 12) if Fr(1, 3) < Fr(k, 12) < Fr(3, 4)]),
      q='How many fractions with denominator 12 are bigger than 1/3 but smaller than 3/4?', hint='Count the fractions in your list.',
      steps=['The fractions are 5/12, 6/12, 7/12 and 8/12.', 'That is 4 fractions.'], src=['Fractions found, and how many:']),

    # ================= Investigation: Sharing 24 stickers
    D(id='I1', tier='invest', no='Investigation (easy step)', type='fields', skill='fractions of a set', frame='2 equal groups: {f1} dots in one group.   3 equal groups: {f2} dots in one group.',
      answer=[12, 8], check=lambda: [share(24, 2), share(24, 3)],
      q='Sharing 24 stickers. Mei has 24 stickers. She gives 1/4 of them to Ali. That is 6 stickers. What if she gives a different fraction? '
        'Easy first step: share 24 dots into 2 equal groups. How many dots are in one group? That is 1/2 of 24. Now try 3 equal groups.',
      hint='Deal the dots out one at a time into the groups, or divide 24 by the number of groups.',
      steps=['24 dots in 2 equal groups: 24 ÷ 2 = 12 dots in each group. That is 1/2 of 24.', '24 dots in 3 equal groups: 24 ÷ 3 = 8 dots in each group. That is 1/3 of 24.'],
      src=['Mei has 24 stickers. She gives', 'of them to Ali. That is 6 stickers. What if she gives a different fraction?', 'Draw 24 dots. Circle them in 2 equal groups: how many dots are in one group?']),
    D(id='I2', tier='invest', no='Investigation (a)', type='fields', skill='fractions of a set', frame='1/2: {f1}   1/3: {f2}   1/6: {f3}   1/8: {f4}',
      answer=[12, 8, 4, 3], check=lambda: [share(24, d) for d in (2, 3, 6, 8)],
      q='Mei has 24 stickers. How many stickers does she give if she gives 1/2? 1/3? 1/6? 1/8?',
      hint='For each fraction, share the 24 stickers into equal groups (the bottom number says how many groups) and look at one group.',
      steps=['1/2 of 24 = 24 ÷ 2 = 12.', '1/3 of 24 = 24 ÷ 3 = 8.', '1/6 of 24 = 24 ÷ 6 = 4.', '1/8 of 24 = 24 ÷ 8 = 3.'],
      src=['How many stickers does she give if she gives', 'What do you notice about']),
    D(id='I3', tier='invest', no='Investigation (a) 1/5', type='choice', options=['Yes', 'No'], answer='No', skill='fractions of a set',
      check=lambda: 'Yes' if share(24, 5) is not None else 'No',
      q='What about 1/5 of 24 stickers? Can Mei share 24 stickers into 5 equal groups with none left over? Is 1/5 of 24 a whole number of stickers?',
      hint='Try dealing 24 stickers out into 5 equal groups. Are there any left over?',
      steps=['Share 24 into 5 groups: each group gets 4, and 4 stickers are left over.', 'So 24 does not share equally into 5 groups, and 1/5 of 24 is not a whole number of stickers.'],
      src=['What do you notice about']),
    D(id='I3b', tier='invest', no='Investigation (a) notice', type='selfcheck', open=True, skill='fractions of a set',
      q='What do you notice about 1/5, compared with 1/2, 1/3, 1/6 and 1/8?',
      hint='Think about what is left over when 24 is shared into the groups.',
      steps=['24 shares equally into 2, 3, 6 and 8 groups, but not into 5 groups (4 each, with 4 left over). So 1/5 of 24 is not a whole number: it is 4 4/5.', 'Any answer that says "24 cannot be shared equally into 5" is good.'],
      src=['What do you notice about']),
    D(id='I4', tier='invest', no='Investigation (b)', type='text', skill='fractions of a set',
      accept=joined_forms(['1/2', '1/3', '1/4', '1/6', '1/8', '1/12'], False), shown='1/2, 1/3, 1/4, 1/6, 1/8, 1/12',
      check=lambda: ', '.join(f'1/{d}' for d in range(2, 13) if share(24, d) is not None),
      q='Which of 1/2, 1/3, 1/4, 1/5 ... up to 1/12 of 24 stickers give a whole number of stickers? List ALL of them. Type the fractions with commas between them.',
      hint='Test each fraction: can 24 be shared into that many equal groups with none left over?',
      steps=['Test the bottom numbers 2 to 12. 24 shares equally into 2, 3, 4, 6, 8 and 12 groups.', 'It does not share equally into 5, 7, 9, 10 or 11 groups.', 'The fractions are 1/2, 1/3, 1/4, 1/6, 1/8 and 1/12. They are the ones whose bottom number is a factor of 24.'],
      src=['Which of', 'of 24 stickers give a whole number of stickers? List ALL of them.']),
    D(id='I5', tier='invest', no='Investigation (c)', type='number', skill='common multiples', answer=60,
      check=lambda: [n for n in range(1, 500) if all(share(n, d) is not None for d in (2, 3, 4, 5, 6))][0],
      q='Mei gets more stickers. What is the smallest number of stickers so that 1/2, 1/3, 1/4, 1/5 AND 1/6 of them are all whole numbers?',
      hint='The number of stickers must share equally into 2, 3, 4, 5 and 6 groups. Try a number and test each fraction, then change it.',
      steps=['Test numbers one at a time. 24 fails for 1/5, because 24 does not share into 5 equal groups. 30 fails for 1/4.', '60 works: 1/2 = 30, 1/3 = 20, 1/4 = 15, 1/5 = 12, 1/6 = 10.', 'No smaller number works. 60 is the smallest number that is a multiple of 2, 3, 4, 5 and 6.'],
      src=['Mei gets more stickers. What is the smallest number of stickers so that']),

    # ================= Think harder (qbank.stretch[0:4])
    D(id='T1', tier='stretch', no='Think harder 1', type='choice', options=['Ben', 'Ravi'], answer='Ben', skill='comparing fractions',
      check=lambda: 'Ben' if Fr(7, 4) > Fr(13, 8) else 'Ravi',
      q='Ben ate 7/4 pizzas and Ravi ate 1 5/8 pizzas. Who ate more?',
      hint='Write both amounts in the same way, for example as mixed numbers with eighths, so you can compare.',
      steps=['7/4 = 1 3/4 (4 quarters make 1, and 3 quarters are left). 3/4 = 6/8, so 7/4 = 1 6/8.', '1 6/8 is more than 1 5/8, so Ben ate more.'],
      src=['Ben ate 7/4 pizzas and Ravi ate 1 5/8 pizzas. Who ate more?']),
    D(id='T2', tier='stretch', no='Think harder 2', type='number', skill='fraction of a set', answer=25, svg=beads_eighths(), check=lambda: 40 - frac_of_set(40, 3, 8),
      q='Siti has 40 beads. 3/8 of them are blue. How many beads are NOT blue?',
      hint='The bar has 8 equal parts that share the 40 beads. How many parts are not blue?',
      steps=['8 parts = 40 beads, so 1 part = 40 ÷ 8 = 5 beads.', 'Blue is 3 parts, so the parts that are not blue are 8 − 3 = 5 parts.', '5 parts = 5 × 5 = 25 beads.'],
      src=['Siti has 40 beads.', 'of them are blue. How many beads are NOT blue?']),
    D(id='T3', tier='stretch', no='Think harder 3', type='text', skill='ordering fractions', accept=joined_forms(['1/2', '7/12', '2/3', '5/6'], True), shown='1/2, 7/12, 2/3, 5/6',
      check=lambda: fractions_in_order([(2, 3), (1, 2), (5, 6), (7, 12)]),
      q='Put these fractions in order, smallest first: 2/3, 1/2, 5/6, 7/12. Type the four fractions with commas between them.',
      hint='Change them all into fractions with the same bottom number, then compare the tops.',
      steps=['In twelfths: 2/3 = 8/12, 1/2 = 6/12, 5/6 = 10/12, and 7/12 stays.', 'The tops in order: 6, 7, 8, 10.', 'So the order is 1/2, 7/12, 2/3, 5/6.'],
      src=['Put these fractions in order, smallest first:']),
    D(id='T4', tier='stretch', no='Think harder 4', type='text', skill='number riddles with fractions', accept=['17/6', '2 5/6'], shown='17/6',
      check=lambda: [frac_text(Fr(n, 6)) for n in range(1, 60) if 2 < Fr(n, 6) < 3 and n % 2 == 1 and abs(3 - Fr(n, 6)) < abs(Fr(n, 6) - 2)][0],
      q='Who am I? I am an improper fraction. My denominator is 6. I am between 2 and 3. My numerator is an odd number. I am closer to 3 than to 2. '
        'Make a list of the fractions that fit the first clues, then rule out the ones that do not fit. Type my fraction.',
      hint='Write 2 and 3 as sixths. Which numerators are in between? Then use the other clues one at a time.',
      steps=['2 = 12/6 and 3 = 18/6, so the numerator is between 12 and 18: 13, 14, 15, 16, 17.', 'Odd numerators: 13, 15, 17.', '15/6 = 2 1/2 is exactly in the middle, and 13/6 is closer to 2. Only 17/6 is closer to 3.', 'I am 17/6 (which is 2 5/6).'],
      src=['Who am I? I am an improper fraction. My denominator is 6. I am between 2 and 3.']),

    # ================= Go further (qbank.challenge[-3:], printed Q5 to Q7)
    D(id='G5a', tier='challenge', no='Go further 5(a)', type='number', skill='fractions of a whole taken away', answer=30, svg=jar_halves_thirds(),
      check=lambda: [n for n in range(1, 500) if n % 6 == 0 and n - n // 2 - n // 3 == 5][0],
      q='Mei takes 1/2 of the sweets in a jar. Ali takes 1/3 of the sweets. There are 5 sweets left. How many sweets were in the jar at first?',
      hint='What fraction of the jar did Mei and Ali take altogether? What fraction is left?',
      steps=['Mei and Ali took 1/2 + 1/3 = 3/6 + 2/6 = 5/6 of the sweets.', 'So 1/6 of the sweets are left, and 1/6 = 5 sweets.', 'The whole jar is 6/6: 6 × 5 = 30 sweets.'],
      src=['Mei takes', 'of the sweets in a jar. Ali takes', 'of the sweets. There are 5 sweets left.']),
    D(id='G5b', tier='challenge', no='Go further 5(b)', type='number', skill='fractions of a whole taken away', answer=42, svg=jar_halves_thirds(),
      check=lambda: [n for n in range(1, 500) if n % 6 == 0 and n - n // 2 - n // 3 == 7][0],
      q='What if 7 sweets were left? Mei still takes 1/2 of the sweets in the jar and Ali still takes 1/3. How many sweets were in the jar at first?',
      hint='Which fraction of the jar is left? How many sweets is that fraction now?',
      steps=['As before, 1/6 of the jar is left, but now 1/6 = 7 sweets.', 'The whole jar is 6 × 7 = 42 sweets.', 'The jar always holds 6 times the number of sweets left.'],
      src=['(b) What if 7 sweets were left?']),
    D(id='G5c', tier='challenge', no='Go further 5(c)', type='selfcheck', open=True, skill='making up a fraction puzzle',
      q='Make up your own puzzle with two other fractions taken from a jar and a number of sweets left, and solve it.',
      hint='Pick two fractions that add to less than 1, then pick the number left.',
      steps=['Puzzles will vary. Check that the two fractions you take add to less than 1, and find the fraction that is left first.', 'Then use a bar model: the number left is that fraction of the jar.',
             'Model puzzle: Mei takes 1/4 of the sweets and Ali takes 1/2. There are 6 sweets left. 1/4 + 1/2 = 3/4 is taken, so 1/4 is left. 1/4 = 6, so the jar had 4 × 6 = 24 sweets.'],
      src=['(c) Make up your own puzzle with two other fractions taken from a jar and a number of sweets left, and solve it.']),
    D(id='G6', tier='challenge', no='Go further 6', type='number', skill='fractions of an unknown number', answer=18,
      check=lambda: [n for n in range(1, 1000) if Fr(n, 2) - Fr(n, 3) == 3][0],
      q='Half of a number is 3 more than a third of the number. What is the number?',
      hint='Picture a bar for the number, cut so that you can see both a half and a third.',
      steps=['Cut the number into 6 equal parts (sixths). Half is 3 sixths and a third is 2 sixths.', 'Half is 1 sixth more than a third, so that 1 sixth is 3.', 'The whole number is 6 sixths: 6 × 3 = 18.', 'Check: half of 18 is 9, a third of 18 is 6, and 9 is 3 more than 6.'],
      src=['Half of a number is 3 more than a third of the number. What is the number?']),
    D(id='G7', tier='challenge', no='Go further 7', type='number', skill='fractions of a remainder', answer=150, svg=book_bar(),
      check=lambda: [n for n in range(5, 2000, 5) if (lambda rest: rest - rest / 2 == 45)(n - Fr(2, 5) * n)][0],
      q='Siti read 2/5 of her book on Monday. On Tuesday she read half of the pages that were left. She still has 45 pages to read. How many pages are in the book?',
      hint='After Monday, 3 of the 5 parts are left. Tuesday takes half of those. Cut each part in half to see what is left at the end.',
      steps=['Cut each fifth in half to make tenths. Monday is 2/5 = 4/10, so 6/10 of the book is left.', 'Tuesday reads half of that, 3/10. So 3/10 of the book is still to read.', '3/10 = 45 pages, so 1/10 = 15 pages.', 'The whole book is 10/10: 10 × 15 = 150 pages.'],
      src=['Siti read', 'of her book on Monday. On Tuesday she read half of the pages that were left. She still has 45 pages to read. How many pages are in the book?']),
]

VARIANTS = {
    '3a': dict(
        base=dict(d=8, k=3, a=3),
        tpl=dict(vars=dict(d=[5, 6, 8, 10], k=[3, 4, 5, 6, 7], a=[1, 2, 3, 4]), derive=dict(N='d*k'),
                 q='Fraction of a set. There are {N} children in a class. {a}/{d} of them wear glasses. How many children wear glasses?',
                 answer='a*k', hint='Cut a bar into {d} equal units that share the {N} children. How many children are in one unit?',
                 steps=['{d} units = {N} children, so 1 unit = {N} ÷ {d} = {k} children.', '{a}/{d} means {a} units: {a} × {k} = {ans} children.']),
        oracle=lambda e: frac_of_set(e['d'] * e['k'], e['a'], e['d'])),
    '5a': dict(
        base=dict(d=5, a=3, u=9),
        tpl=dict(vars=dict(d=[5, 7, 8, 9], a=[2, 3, 4], u=[4, 5, 6, 7, 8, 9]), derive=dict(R='a*u'),
                 q='{a}/{d} of the sweets in a jar are red. There are {R} red sweets. How many sweets are in the jar?',
                 answer='d*u', hint='The {a} red parts hold {R} sweets. How many sweets are in one part? How many parts make the whole jar?',
                 steps=['{a} units = {R} sweets, so 1 unit = {R} ÷ {a} = {u} sweets.', 'The whole jar is {d} units: {d} × {u} = {ans} sweets.']),
        oracle=lambda e: [n for n in range(e['d'], 2000, e['d']) if e['a'] * (n // e['d']) == e['a'] * e['u']][0]),
    '1d': dict(
        base=dict(w=5, d=8),
        tpl=dict(vars=dict(w=[2, 3, 4, 5, 6, 7], d=[3, 4, 5, 6, 8, 10]),
                 q='How many pieces of size 1/{d} are there in {w} wholes?', answer='w*d', hint='How many pieces of size 1/{d} make 1 whole?',
                 steps=['1 whole = {d} pieces of size 1/{d}.', '{w} wholes = {w} × {d} = {ans} pieces.']),
        oracle=lambda e: sum(e['d'] for _ in range(e['w']))),
}
