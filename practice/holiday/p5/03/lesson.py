"""Online practice for Level 5 (Primary 5, ages 10 to 12) holiday lesson 3: Fraction Word Problems ("Before and After").

The questions are the ones printed in the Level 5 holiday workbook, lesson 3: Start here Q1 to Q5 (p5/content/l3.js, workbook()), the Investigation
(p5/content/inv.js), Think harder A1 to A4 (the first four 'stretch' questions of p5/content/l3.js qbank) and Go further B1 to B3 (the last three
'challenge' questions) and the "Make up your own" prompt (gaps.js), in the printed order, exactly as p5/workbook_html.js prints them.  Every answer is recomputed by
an INDEPENDENT checker below (a search over the numbers of the story with exact fractions, or a forward simulation, never a copy of the printed answer);
build_holiday.py stops if a checker and the printed answer differ.
"""
import os, sys
HERE_ = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE_, '..', '..'))
sys.path.insert(0, os.path.join(HERE_, '..'))
from hlib import *          # noqa: E402,F401
from p5lib import *         # noqa: E402,F401
import p5fig2 as G          # noqa: E402

META = dict(level=5, lesson=3, key='p5', title='Before and After', workbook_title='BEFORE AND AFTER', topic='Fraction Word Problems', strand='Fractions',
            sources=['p5/content/l3.js', 'p5/content/inv.js', 'p5/content/gaps.js'],
            intro=['Ask first: what stays the same? It can be the total (one person gives to the other), the difference (both get or spend the same amount) or one amount that does not change. '
                   'Fraction of a remainder: cut the parts that are left into equal units, so every part is the same size.',
                   'Type your answer into the box. You can draw a bar model on paper if you like. Some questions ask you to explain: write your idea, then compare it with the model answer after you submit.'])
ST = 'Fractions'
F = Fraction


def D(**k):
    k.setdefault('strand', ST)
    return k


def fr_item(iid, tier, no, skill, f, q, check, hint, steps, src, units=(), simplest=False, also=(), svg=None):
    return D(id=iid, tier=tier, no=no, type='text', skill=skill, accept=frac_accepts(f, simplest=simplest, units=units, also=also), shown=frac_text(f),
             q=q, check=check, hint=hint, steps=steps, src=src, **({'svg': svg} if svg else {}))


# ---------------------------------------------------------------- checkers (searches with exact fractions: no formula from the printed answer)
def ravi1(total):
    """He spends 1/3 of his money on a book and 1/4 of the remainder on a pen: (book, pen, left) as exact fractions."""
    total = F(total)
    book = total / 3
    rest = total - book
    pen = rest / 4
    return book, pen, rest - pen


def ints(vals):
    out = []
    for v in vals:
        v = F(v)
        assert v.denominator == 1, v
        out.append(int(v))
    return out


def ravi_start(left):
    found = [t for t in range(1, 3000) if ravi1(t)[2] == left]
    assert len(found) == 1
    return found[0]


def swap_start(total, gift, a, b):
    """Siti and Mei have `total` stickers; Siti gives Mei `gift`; then Siti has a/b as many as Mei.  Returns (Siti before, Mei before)."""
    found = [s for s in range(0, total + 1) if (s - gift) * b == (total - s + gift) * a]
    assert len(found) == 1
    return found[0], total - found[0]


def mother_gift(ravi, ali):
    """The same gift for both so that Ali has 2/3 as much as Ravi."""
    found = [g for g in range(0, 2000) if (ali + g) * 3 == (ravi + g) * 2]
    assert len(found) == 1
    return found[0]


def can_double(total):
    """Can Ali (who starts with more than Mei) give Mei at least 1 sticker so that Ali ends with exactly twice as many as Mei?"""
    for ali in range(total // 2 + 1, total + 1):
        mei = total - ali
        for gift in range(1, ali + 1):
            if ali - gift == 2 * (mei + gift):
                return True
    return False


def monday_tuesday():
    found = [t for t in range(1, 3000) if F(t, 4) + F(2, 5) * (t - F(t, 4)) == 66]
    assert len(found) == 1
    return found[0]


def beads():
    found = [n for n in range(7, 2000, 7) if F(3 * n, 7) + 30 > 0 and (F(3 * n, 7) + 30) * 5 == (n + 30) * 3]
    assert len(found) == 1
    return found[0], found[0] + 30


def years_ago():
    found = [y for y in range(0, 9) if (9 - y) * 5 == 41 - y]
    assert len(found) == 1
    return found[0]


def ben_siti():
    found = [b for b in range(1, 140) if F(b, 2) == (140 - b) - 20]
    assert len(found) == 1
    return found[0]


def mei_siti(mei=200, siti=80):
    found = [s for s in range(0, siti + 1) if mei - 3 * s == siti - s]
    assert len(found) == 1
    return found[0]


def ravi_stickers():
    for n in range(1, 2000):
        after1 = n - (F(n, 2) + 4)
        after2 = after1 - (F(after1, 2) + 4)
        if after2 == 4:
            return n


def stamps():
    found = []
    for a in range(1, 140):
        b = 140 - a
        if F(2 * a, 3) == F(b, 2):
            found.append((a, b))
    assert len(found) == 1
    a, b = found[0]
    return int(F(b, 2))


def gift_to_equal(ali=50, ben=30):
    found = [g for g in range(0, ali + 1) if ali - g == ben + g]
    assert len(found) == 1
    return found[0]


SRC_RAVI = 'Ravi had some money. He spent 1/3 of it on a book and 1/4 of the remainder on a pen. He had $36 left.'
Q_RAVI = 'Ravi had some money. He spent 1/3 of it on a book and 1/4 of the remainder on a pen. He had $36 left.'
Q_SWAP = 'Siti and Mei had 84 stickers altogether. Siti gave Mei 12 stickers. Then Siti had 3/4 as many stickers as Mei.'
SRC_SWAP = 'Siti and Mei had 84 stickers altogether. Siti gave Mei 12 stickers. Then Siti had 3/4 as many stickers as Mei.'
Q_MARB = 'Ali has 50 marbles and Ben has 30 marbles. Ali gives some of his marbles to Ben (Ali has fewer afterwards and Ben has more).'
Q_GIFT = 'Ravi had $50 and Ali had $26. Their mother gave each of them the same amount of money. Then Ali had 2/3 as much money as Ravi.'
Q_JAR = 'A jar has 12 red beads and 8 blue beads. Then 10 more red beads are put in.'

SIT, MEI = swap_start(84, 12, 3, 4)

ITEMS = [
    # ================= Start here (workbook lesson 3: Q1 to Q5)
    D(id='1a', tier='core', no='1(a)', type='fields', skill='fraction of a remainder', answer=[20, 10, 30],
      q=Q_RAVI + '\nTry $60 first.', frame='The book costs ${f1}, the pen costs ${f2}, and ${f3} is left.',
      check=lambda: ints(ravi1(60)),
      hint='Find the book first: 1/3 of $60. What is the remainder? The pen is 1/4 of the remainder, not of $60.',
      steps=['The book costs 1/3 of $60 = $20.', 'The remainder is $60 − $20 = $40.', 'The pen costs 1/4 of the remainder: $40 ÷ 4 = $10.', 'Money left: $40 − $10 = $30.'],
      src=[SRC_RAVI, 'Try $60 first. The book costs $______, the pen costs $______, and $______ is left.']),
    D(id='1b', tier='core', no='1(b)', type='choice', skill='fraction of a remainder', options=['Too much', 'Too little'], answer='Too little',
      q=Q_RAVI + '\nWas $60 too much or too little for Ravi to start with? (Work out how much money $60 would leave him.)',
      check=lambda: 'Too little' if ravi1(60)[2] < 36 else 'Too much',
      hint='Work out how much money is left when Ravi starts with $60. Is that more or less than the $36 he really had left?',
      steps=['Starting with $60, the book costs $20, the pen costs $10 and Ravi would have $30 left.', 'He really had $36 left, which is more than $30.', 'So Ravi must have started with more than $60: $60 was too little.'],
      src=['Was $60 too much or too little?']),
    D(id='1bn', tier='core', no='1(b) amount', type='number', skill='fraction of a remainder', answer=72,
      q=Q_RAVI + '\nHow much money did Ravi have at first?', check=lambda: ravi_start(36),
      hint='Think of a bar for his money. The book takes 1 of 3 equal parts. Cut every part in half so that the pen is easy to find.',
      steps=['Cut the bar into 3 equal parts: the book is 1 part and the remainder is 2 parts.', 'Cut every part in half: now there are 6 equal units. The book is 2 units and the remainder is 4 units.',
             'The pen is 1/4 of the remainder: 1 unit. So 3 units are left.', '3 units = $36, so 1 unit = $12.', 'Ravi had 6 units: 6 × $12 = $72.'],
      sol_fig=lambda got: G.sol_ravi(got, *ints(ravi1(got))),
      src=['How much money did Ravi have at first?']),
    D(id='1c', tier='core', no='1(c)', type='number', skill='fraction of a remainder', answer=12,
      q=Q_RAVI + '\nHow much more did the book cost than the pen?', check=lambda: int(ravi1(ravi_start(36))[0] - ravi1(ravi_start(36))[1]),
      hint='Find how much money Ravi had at first. Then work out what the book cost and what the pen cost.',
      steps=['Ravi had 6 units of $12 = $72 at first.', 'The book costs 2 units = $24 and the pen costs 1 unit = $12.', 'The book cost $24 − $12 = $12 more than the pen.'],
      src=['How much more did the book cost than the pen?']),

    D(id='2a', tier='core', no='2(a)', type='number', skill='total stays the same', answer=84,
      q=Q_SWAP + '\nHow many stickers did they have altogether after the swap?', svg=G.after_model(), check=lambda: (SIT - 12) + (MEI + 12),
      hint='Siti gave some of her stickers to Mei. Were any stickers lost, or made?',
      steps=['The 12 stickers only moved from Siti to Mei. Nobody lost any and nobody got new ones.', 'The total stays the same: 84 stickers.'],
      src=[SRC_SWAP, 'How many stickers did they have altogether after the swap?']),
    D(id='2b', tier='core', no='2(b)', type='fields', skill='total stays the same', answer=[48, 36],
      q=Q_SWAP + '\nTip: “3/4 as many” means that for every 3 stickers Siti has, Mei has 4. Try 3 and 4, then 6 and 8, then 9 and 12 … until the total is 84.\n'
        'How many stickers did Siti have at first? How many did Mei have at first?',
      frame='Siti: {f1}     Mei: {f2}', svg=G.after_model(), check=lambda: [SIT, MEI],
      hint='First find how many each had AFTER the swap (use the tip). Then undo the swap: who gave 12 away, and who got 12?',
      steps=['After the swap Siti has 3 units and Mei has 4 units. 7 units = 84, so 1 unit = 12.', 'After the swap Siti has 3 × 12 = 36 and Mei has 4 × 12 = 48.',
             'Undo the swap: Siti gave 12 away, so at first she had 36 + 12 = 48. Mei got 12, so at first she had 48 − 12 = 36.', 'Check: 48 + 36 = 84, and after the swap 36 is 3/4 of 48.'],
      sol_fig=lambda got: G.sol_swap(got[0], got[1], 12),
      src=[SRC_SWAP, 'How many stickers did Siti have at first? How many did Mei have at first?', '“3/4 as many” means that for every 3 stickers Siti has, Mei has 4.']),

    D(id='3a', tier='core', no='3(a)', type='fields', skill='what stays the same', answer=[30, 50],
      q=Q_MARB + '\nBen says, “If Ali gives me 20 marbles, we will have the same number, because Ali has 20 more than me.” Test it: Ali gives Ben 20 marbles. How many does each boy have now?',
      frame='Ali has {f1} and Ben has {f2}.', check=lambda: [50 - 20, 30 + 20],
      hint='Ali loses the 20 marbles he gives away and Ben gains them.',
      steps=['Ali has 50 − 20 = 30 marbles.', 'Ben has 30 + 20 = 50 marbles.'],
      src=[Q_MARB, 'Ben says, “If Ali gives me 20 marbles, we will have the same number, because Ali has 20 more than me.” Test it: after Ali gives 20, Ali has ______ and Ben has ______.']),
    D(id='3b', tier='core', no='3(a) is Ben right?', type='choice', skill='what stays the same', options=['Yes, Ben is right', 'No, Ben is not right'], answer='No, Ben is not right',
      q=Q_MARB + '\nBen says, “If Ali gives me 20 marbles, we will have the same number, because Ali has 20 more than me.”\nIs Ben right?',
      check=lambda: 'Yes, Ben is right' if 50 - 20 == 30 + 20 else 'No, Ben is not right',
      hint='Work out how many marbles each boy has after the gift. Are the two numbers the same?',
      steps=['After the gift Ali has 30 marbles and Ben has 50 marbles.', 'The numbers are not the same, so Ben is not right.'],
      src=['Is Ben right? Explain.']),
    D(id='3c', tier='core', no='3(a) explain', type='selfcheck', open=False, skill='what stays the same', facts=10,
      q='Is Ben right? Explain how you know. (Ali has 50 marbles and Ben has 30. Ben says that if Ali gives him 20 marbles they will have the same number.) Write your explanation, then compare it with the model answer.',
      check=gift_to_equal,
      hint='Try some different gifts and write down what each boy has each time. When are the two numbers the same?',
      steps=['If Ali gives 20 marbles, Ali has 30 and Ben has 50. Ben now has 20 MORE than Ali, so they do not have the same number.',
             'Every marble Ali gives takes 1 from Ali AND adds 1 to Ben, so each marble closes the gap by 2.', 'To close a gap of 20, Ali only needs to give 10 marbles. Then they have 40 each.',
             'A good explanation says why 20 is too many: Ali loses 10 and Ben gains 10, so the gap of 20 closes by 20.'],
      src=['Is Ben right? Explain.']),

    D(id='4s', tier='core', no='4 (start here)', type='fields', skill='what stays the same', answer=[60, 36],
      q=Q_GIFT + '\nStart here: try a gift of $10 each. How much does each boy have now?', frame='Ravi has ${f1} and Ali has ${f2}.', check=lambda: [50 + 10, 26 + 10],
      hint='Each boy gets $10 more than he had.',
      steps=['Ravi has $50 + $10 = $60.', 'Ali has $26 + $10 = $36.'],
      src=['try a gift of $10 each. How much does each boy have now?']),
    D(id='4s2', tier='core', no='4 (start here, too big or too small)', type='choice', skill='what stays the same', options=['Too small', 'Too big', 'Just right'], answer='Too small',
      q=Q_GIFT + '\nStart here: try a gift of $10 each. Is Ali’s money 2/3 of Ravi’s now? Is the gift too big or too small?',
      check=lambda: 'Too small' if 10 < mother_gift(50, 26) else ('Too big' if 10 > mother_gift(50, 26) else 'Just right'),
      hint='Work out each boy’s money after the gift. What is 2/3 of Ravi’s money? Is Ali’s money more or less than that?',
      steps=['After a gift of $10, Ravi has $60 and Ali has $36.', '2/3 of $60 is $40, but Ali has only $36. Ali’s money is not 2/3 of Ravi’s yet.', 'Ali needs more money, so the gift is too small.'],
      src=['Is Ali’s money 2/3 of Ravi’s? Is the gift too big or too small?']),
    D(id='4a', tier='core', no='4(a)', type='choice', skill='what stays the same', options=['The total: $76', 'The difference: $24'], answer='The difference: $24',
      q=Q_GIFT + '\nWhat stays the same: the total or the difference? How much is it?',
      check=lambda: ('The difference: $%d' % (50 - 26)) if (50 + 5) - (26 + 5) == 50 - 26 and (50 + 5) + (26 + 5) != 50 + 26 else None,
      hint='Pick a gift, say $5 each. Does the total of their money change? Does the gap between their money change?',
      steps=['Both boys get the same amount, so the total goes up. The total does NOT stay the same.', 'The difference stays the same: $50 − $26 = $24 before the gift, and still $24 after it.', 'The difference stays the same: $24.'],
      src=['What stays the same: the total or the difference? How much is it?']),
    D(id='4b', tier='core', no='4(b)', type='number', skill='what stays the same', answer=22,
      q=Q_GIFT + '\nHow much money did their mother give each boy?', check=lambda: mother_gift(50, 26),
      hint='After the gift Ali has 2 units and Ravi has 3 units. The difference between them is how many units? And how many dollars is that?',
      steps=['The difference stays $24. After the gift Ali has 2 units and Ravi has 3 units, so the difference is 1 unit.', '1 unit = $24, so Ali has 2 × $24 = $48 and Ravi has 3 × $24 = $72 after the gift.',
             'Ali had $26, so the gift is $48 − $26 = $22.', 'Check: Ravi has $50 + $22 = $72, and $48 is 2/3 of $72.'],
      src=['Then Ali had 2/3 as much money as Ravi.', 'How much money did their mother give each boy?']),

    D(id='5a', tier='core', no='5(a)', type='choice', skill='one amount does not change', options=['Red', 'Blue'], answer='Blue',
      q=Q_JAR + '\nWhich colour did not change?', check=lambda: 'Blue' if 8 == 8 and 12 + 10 != 12 else 'Red',
      hint='Which beads were put in? Which beads were not touched?',
      steps=['10 more red beads were put in, so the number of red beads changed: 12 became 22.', 'No blue beads were put in or taken out: there are still 8 blue beads.', 'Blue did not change.'],
      src=['A jar has 12 red beads and 8 blue beads. Then 10 more red beads are put in.', 'Which colour did not change?']),
    fr_item('5b1', 'core', '5(b)', 'fractions of a whole', F(2, 5), 'A jar has 12 red beads and 8 blue beads.\nAt first, 8 of the 20 beads were blue. What fraction is that, in its simplest form? Type a fraction.',
            lambda: frac_text(F(8, 20)), 'Write 8 out of 20 as 8/20. Then divide the top and the bottom by the same number to make it simpler.',
            ['8 out of 20 beads are blue: 8/20.', 'Divide the top and the bottom by 4: 8/20 = 2/5.'],
            ['At first, 8 of the 20 beads were blue. What fraction is that, in its simplest form?'], simplest=True),
    D(id='5b2', tier='core', no='5(b) beads now', type='number', skill='one amount does not change', answer=30,
      q=Q_JAR + '\nNow, how many beads are in the jar?', check=lambda: 12 + 8 + 10,
      hint='Start with the beads that were in the jar. Then add the ones that were put in.',
      steps=['At first there were 12 + 8 = 20 beads.', '10 more red beads were put in: 20 + 10 = 30 beads.'],
      src=['Now, how many beads are in the jar?']),
    fr_item('5b3', 'core', '5(b) fraction now', 'fractions of a whole', F(4, 15), Q_JAR + '\nWhat fraction of the beads in the jar are blue now? Type a fraction (the simplest form is best).',
            lambda: frac_text(F(8, 12 + 8 + 10)), 'The blue beads are still the same 8. How many beads are in the whole jar now?',
            ['Now there are 30 beads in the jar and 8 of them are blue.', '8/30 = 4/15 in its simplest form.'],
            ['What fraction are blue now?']),
    D(id='5c', tier='core', no='5(c)', type='selfcheck', open=False, skill='one amount does not change', facts='smaller',
      q='The blue beads did not change, but the blue FRACTION did. Why? Write your idea, then compare it with the model answer.',
      check=lambda: 'smaller' if F(8, 30) < F(8, 20) else 'bigger',
      hint='Look at the bottom number of each fraction. What happened to the number of beads in the whole jar?',
      steps=['The 8 blue beads did not change, but the whole jar has more beads in it: 30 instead of 20.', 'The same 8 blue beads are now a smaller part of a bigger whole, so the fraction gets smaller: 2/5 became 4/15.',
             'A good answer says that the blue beads stayed the same but the whole changed, and that the fraction compares the blue beads with ALL the beads.'],
      src=['The blue beads did not change, but the blue FRACTION did. Why?']),

    # ================= Investigation: What if we change the total?
    D(id='C0', tier='invest', no='C (easy first step)', type='number', skill='the total stays the same', answer=20,
      q='What if we change the total?\nEasy first step: the total is 48 + 12 = 60. Think of one bar for 60 cut into 3 equal parts. How many stickers is one part?', check=lambda: (48 + 12) // 3,
      hint='Think of cutting 60 into 3 equal parts. Which operation is that?',
      steps=['60 ÷ 3 = 20.', 'One part is 20 stickers.'],
      src=['Easy first step: the total is 48 + 12 = 60.', 'cut it into 3 equal parts. How many stickers is one part?']),
    D(id='Ca', tier='invest', no='C(a)', type='number', skill='the total stays the same', answer=8,
      q='Ali has 48 stickers and Mei has 12. Ali gives Mei some stickers. Afterwards Ali has exactly twice as many as Mei. How many does Ali give?',
      check=lambda: [g for g in range(0, 49) if 48 - g == 2 * (12 + g)][0],
      hint='The total stays the same when Ali gives stickers to Mei. After the giving, Ali has 2 equal parts and Mei has 1.',
      steps=['The total is 48 + 12 = 60 and it does not change.', 'After the giving Ali has 2 units and Mei has 1 unit, so 3 units = 60 and 1 unit = 20.', 'Ali has 40 and Mei has 20 after. Ali had 48, so he gives 48 − 40 = 8.',
             'Check: Mei has 12 + 8 = 20, and 40 is twice 20.'],
      src=['Ali has 48 stickers and Mei has 12. Ali gives Mei some stickers. Afterwards Ali has exactly twice as many as Mei. How many does Ali give?']),
    D(id='Cb', tier='invest', no='C(b)', type='set', ordered=False, grouped=False, skill='multiples and units', answer=[30, 45, 60],
      q='What if the total is different? Ali has more than Mei to start. Try the totals 45, 50, 30 and 60 in any way you like.\nFor which of these totals can Ali end up with exactly TWICE as many as Mei, with whole stickers? Type those totals.',
      check=lambda: [t for t in (45, 50, 30, 60) if can_double(t)],
      hint='Try each total in turn. After the giving, can you share the total so that Ali has twice as many as Mei, with whole stickers?',
      steps=['After the giving, Ali has 2 units and Mei has 1 unit, so the total is 3 units. Each unit must be a whole number of stickers.', 'Total 60: 1 unit = 20 (Ali 40, Mei 20). Yes.',
             'Total 45: 1 unit = 15 (Ali 30, Mei 15). Yes. Total 30: 1 unit = 10 (Ali 20, Mei 10). Yes.', 'Total 50: 50 ÷ 3 is not a whole number, so it cannot be done.', 'The totals that work are 30, 45 and 60.'],
      src=['What if the total is different? Try the totals 45, 50, 30 and 60 in any way you like (Ali has more than Mei to start). For which totals can Ali end up with exactly TWICE as many as Mei, with whole stickers? For which can it NOT be done?']),
    D(id='Cc', tier='invest', no='C(c)', type='selfcheck', open=False, skill='explaining a rule', facts=True,
      q='What stays the same? Write a rule that tells you which totals work, and explain with a bar. Write your idea, then compare it with the model answer.',
      check=lambda: all(can_double(t) == (t % 3 == 0) for t in range(6, 101)),
      hint='Look at what you found in (b). What do the totals that work have in common?',
      steps=['What stays the same: the total. When one child gives to the other, the total never changes.', 'After the giving there are 3 equal units (Ali 2, Mei 1), so the total must be a multiple of 3. (This was checked for every total from 6 to 100.)',
             'Bar: one bar for the total cut into 3 equal parts. If the total is not a multiple of 3 (like 50), the parts cannot all be whole stickers.',
             'A good answer says what stays the same, gives the rule in words (the total must be a multiple of 3) and shows a bar cut into 3 equal parts. It also tests a total that fails.'],
      src=['What stays the same? Write a rule that tells you which totals work, and explain with a bar.']),

    # ================= Think harder (A1 to A4)
    D(id='A1', tier='stretch', no='A1', type='number', skill='fraction of a remainder', answer=120,
      q='Ravi spent 1/4 of his money on Monday and 2/5 of the remainder on Tuesday. He spent $66 altogether.\nHow much money did he have at first?', svg=G.fig_a1(), check=monday_tuesday,
      hint='Monday takes 1/4. Tuesday takes 2/5 of what is LEFT, not of the whole. Cut the bar so that every part is the same size.',
      steps=['After Monday, 3/4 is left: the remainder is 3 parts out of 4.', 'Cut each of the 4 parts into 5: the whole bar is 20 equal units. Monday is 5 units and the remainder is 15 units.', 'Tuesday is 2/5 of 15 units = 6 units.',
             'Spent: 5 + 6 = 11 units = $66, so 1 unit = $6.', 'At first: 20 units = 20 × $6 = $120.'],
      sol_fig=lambda got: G.sol_a1(got, 5, 6, 9, 66),
      src=['Ravi spent 1/4 of his money on Monday and 2/5 of the remainder on Tuesday. He spent $66 altogether. How much money did he have at first?']),
    D(id='A2', tier='stretch', no='A2', type='fields', skill='one amount does not change', answer=[70, 100],
      q='A box had red beads and blue beads. 3/7 of the beads were red. Then 30 red beads were added. Now 3/5 of the beads are red.\nHow many beads were in the box at first? How many are in the box now?',
      frame='At first: {f1}     Now: {f2}', check=lambda: list(beads()),
      hint='Which beads did NOT change when the red ones were added? Write what fraction of the box those beads were at first and what fraction they are now.',
      steps=['The blue beads did not change. At first blue is 4/7 of the box. Now blue is 2/5 of the box.', 'Make the blue the same size: 4 units of blue at first. Now 4 units of blue are 2 out of 5 parts of the box, so the whole box is 10 units.',
             'So the box is 7 units at first and 10 units now. The red grew from 3 units to 6 units, so 3 units = 30 and 1 unit = 10.', 'At first: 7 × 10 = 70 beads. Now: 10 × 10 = 100 beads.'],
      src=['A box had red beads and blue beads. 3/7 of the beads were red. Then 30 red beads were added. Now 3/5 of the beads are red. How many beads were in the box at first? How many are in the box now?']),
    D(id='A3', tier='stretch', no='A3', type='number', skill='the difference stays the same', answer=1,
      q='Mrs Tan is 41 years old and her son is 9. How many years ago was her son’s age 1/5 of her age?', check=years_ago,
      hint='The difference between their ages never changes. How many units is that difference when the son is 1/5 of her age?',
      steps=['The age difference stays the same: 41 − 9 = 32 years.', 'When the son is 1/5 of her age, he is 1 unit and she is 5 units, so the difference is 4 units.', '4 units = 32, so 1 unit = 8: the son was 8 and Mrs Tan was 40.',
             'The son is 9 now, so that was 9 − 8 = 1 year ago.'],
      src=['Mrs Tan is 41 years old and her son is 9. How many years ago was her son’s age 1/5 of her age?']),
    D(id='A4', tier='stretch', no='A4', type='number', skill='one amount does not change', answer=80,
      q='Ben and Siti had $140 altogether. Ben spent 1/2 of his money and Siti spent $20. Then they had the same amount left.\nHow much did Ben have at first?', svg=G.fig_a4(), check=ben_siti,
      hint='Cut Ben’s bar in 2 equal parts: one part spent, one part left. Siti has the same amount left. What was Siti’s money at first, in terms of that part?',
      steps=['Ben spent half, so he has 1 unit left and had 2 units at first.', 'Siti has the same amount left (1 unit) and spent $20, so she had 1 unit + $20 at first.', 'Together: 2 units + 1 unit + $20 = $140, so 3 units = $120 and 1 unit = $40.',
             'Ben had 2 units = $80. Check: Ben has $40 left, and Siti has $60 − $20 = $40 left.'],
      src=['Ben and Siti had $140 altogether. Ben spent 1/2 of his money and Siti spent $20. Then they had the same amount left. How much did Ben have at first?']),

    # ================= Go further (B1 to B3)
    D(id='B1', tier='challenge', no='B1', type='number', skill='the difference stays the same', answer=60,
      q='Mei had $200 and Siti had $80. Mei spent 3 times as much money as Siti. Then they had the same amount left.\nHow much money did Siti spend?', svg=G.fig_b1(), check=mei_siti,
      hint='Mei spent 3 parts and Siti spent 1 part. How many parts MORE did Mei spend? Where does that extra money come from?',
      steps=['Mei had $200 − $80 = $120 more than Siti at the start.', 'They ended with the same amount, so Mei must have spent $120 more than Siti.', 'Mei spent 3 parts and Siti 1 part: that is 2 parts more, so 2 parts = $120 and 1 part = $60.',
             'Siti spent 1 part = $60. Check: Mei has $200 − $180 = $20 left and Siti has $80 − $60 = $20 left.'],
      src=['Mei had $200 and Siti had $80. Mei spent 3 times as much money as Siti. Then they had the same amount left. How much money did Siti spend?']),
    D(id='B2', tier='challenge', no='B2', type='number', skill='working backwards', answer=40,
      q='Ravi had some stickers. He gave 1/2 of them and 4 more to Ali. Then he gave 1/2 of the stickers he had left and 4 more to Ben. He had 4 stickers left.\nHow many stickers did he have at first?', check=ravi_stickers,
      hint='Work backwards from the 4 stickers he had left. Undo the last gift first.',
      steps=['Work backwards. At the end he had 4 left after giving Ben 4 more and half of what he had.', 'Before the 4 more he had 4 + 4 = 8. That was half of what he had before Ben’s gift, so he had 8 × 2 = 16.',
             'The same way for Ali’s gift: 16 + 4 = 20 was half, so he had 20 × 2 = 40 at first.', 'Check: 40 − (20 + 4) = 16, then 16 − (8 + 4) = 4.'],
      src=['Ravi had some stickers. He gave 1/2 of them and 4 more to Ali. Then he gave 1/2 of the stickers he had left and 4 more to Ben. He had 4 stickers left. How many stickers did he have at first?']),
    D(id='B3', tier='challenge', no='B3', type='number', skill='one amount does not change', answer=40,
      q='Ali and Ben had 140 stamps altogether. Ali gave away 1/3 of his stamps and Ben gave away 1/2 of his. Then they had the same number of stamps left.\nHow many stamps did Ben give away?', check=stamps,
      hint='Ali keeps 2 of 3 equal parts. Ben keeps 1 of 2 equal parts. The two amounts kept are equal: make them the same size in your model.',
      steps=['Ali keeps 2 out of 3 parts of his stamps. Ben keeps 1 out of 2 parts of his.', 'Make the kept amounts equal: each keeps 2 units. Then Ali had 3 units (2 kept, 1 given away) and Ben had 4 units (2 kept, 2 given away).',
             'Together 3 + 4 = 7 units = 140 stamps, so 1 unit = 20.', 'Ben gave away 2 units = 40 stamps. Check: Ali had 60 and keeps 40; Ben had 80 and keeps 40.'],
      src=['Ali and Ben had 140 stamps altogether. Ali gave away 1/3 of his stamps and Ben gave away 1/2 of his. Then they had the same number of stamps left. How many stamps did Ben give away?']),
    D(id='pose', tier='challenge', no='Make up your own', type='selfcheck', open=True, marking_mode='open', skill='making up a problem',
      q='Make up a before-and-after story in which the total stays the same. Draw its model, then swap with a partner. (Think for 30 seconds before anyone speaks.)',
      hint='Pick the total and the amount that moves first. Then say what fraction one person has afterwards, like “Ali has 1/2 as many as Ben”.',
      steps=['This question is open: many stories are right.', 'Check your story: after the giving, the two parts must add up to the total. Draw the After bars with equal units, then work back to the Before.',
             'Sample: Ali and Ben have 108 stickers altogether. Ali gives Ben 24 stickers. Then Ali has 1/2 as many as Ben. After: 3 units = 108, so Ali has 36 and Ben has 72. At first Ali had 36 + 24 = 60 and Ben had 48.'],
      src=['Make up a before-and-after story in which the total stays the same. Draw its model, then swap with a partner.']),
]


# ---------------------------------------------------------------- variants: a template with an oracle (the same search as above) for number and box items with readable numbers
def _ravi_oracle(e):
    return ravi_start(e['L'])


def _swap_oracle(e):
    s, m = swap_start(e['T'], e['g'], 3, 4)
    return dict(f1=s, f2=m)


def _gift_oracle(e):
    return mother_gift(e['A'] + e['d'], e['A'])


def _mei_oracle(e):
    return mei_siti(e['S'] + e['dd'], e['S'])


finish(ITEMS)

VARIANTS = {
    '1bn': dict(
        base=dict(L=36),
        tpl=dict(vars=dict(L=[24, 30, 36, 42, 48, 60]), q='Ravi had some money. He spent 1/3 of it on a book and 1/4 of the remainder on a pen. He had ${L} left.\nHow much money did Ravi have at first?', answer='2 * L',
                 hint='Cut the bar into 6 equal units. How many units are the book and the pen? How many units are left?',
                 steps=['Cut the bar into 6 equal units: the book is 2 units, the pen is 1 unit and 3 units are left.', '3 units = ${L}, so 1 unit = ${L} ÷ 3.', 'Ravi had 6 units, which is ${ans}.']),
        oracle=_ravi_oracle),
    '2b': dict(
        base=dict(T=84, g=12),
        tpl=dict(vars=dict(T=[56, 70, 84, 98, 112], g=[6, 8, 10, 12]),
                 q='Siti and Mei had {T} stickers altogether. Siti gave Mei {g} stickers. Then Siti had 3/4 as many stickers as Mei.\nHow many stickers did Siti have at first? How many did Mei have at first?',
                 frame='Siti: {f1}     Mei: {f2}', answers=dict(f1='3 * T / 7 + g', f2='4 * T / 7 - g'),
                 hint='Find how many each had AFTER the swap (3 units and 4 units). Then undo the swap.',
                 steps=['After the swap Siti has 3 units and Mei has 4 units, so 7 units = {T}.', 'Work out 1 unit, then Siti and Mei after the swap.', 'Undo the swap: Siti gave {g} away and Mei got {g}. The two numbers are {ans}.']),
        oracle=_swap_oracle),
    '4b': dict(
        base=dict(A=26, d=24),
        tpl=dict(vars=dict(A=[20, 24, 26, 30], d=[24, 30, 36, 40]), derive=dict(R='A + d'),
                 q='Ravi had ${R} and Ali had ${A}. Their mother gave each of them the same amount of money. Then Ali had 2/3 as much money as Ravi.\nHow much money did their mother give each boy?', answer='2 * d - A',
                 hint='The difference stays the same. After the gift Ali has 2 units and Ravi has 3 units, so the difference is 1 unit.',
                 steps=['The difference is ${R} − ${A} = ${d}, and it stays the same.', 'After the gift Ali has 2 units and Ravi has 3 units, so 1 unit = ${d}.', 'Ali then has 2 × ${d}. The gift is that amount take away ${A}: ${ans}.']),
        oracle=_gift_oracle),
    'B1': dict(
        base=dict(S=80, dd=120),
        tpl=dict(vars=dict(S=[80, 100, 120], dd=[100, 120, 140, 150]), derive=dict(M='S + dd'),
                 q='Mei had ${M} and Siti had ${S}. Mei spent 3 times as much money as Siti. Then they had the same amount left.\nHow much money did Siti spend?', answer='dd / 2',
                 hint='Mei spent 3 parts and Siti spent 1 part. How many parts MORE did Mei spend, and how much money is that?',
                 steps=['Mei had ${M} − ${S} = ${dd} more than Siti at the start.', 'They ended with the same amount, so Mei spent ${dd} more than Siti: that is 2 parts.', '1 part = ${dd} ÷ 2 = ${ans}. Siti spent ${ans}.']),
        oracle=_mei_oracle),
}


polish(ITEMS, VARIANTS)

# ---- inquiry habit (docs/pedagogy/inquiry_skills_explicit.md; levels/habits.json)
ITEMS.insert(max(i for i, x in enumerate(ITEMS) if x['tier'] == 'core') + 1, habit_item('Notice',
    'Before: Ali has 20 cards and Mei has 12. After Ali gives Mei 4 cards, they have the same number. What stays the same? What changes? Write one or two sentences.',
    ['The total stays the same: 20 + 12 = 32 and 16 + 16 = 32.', "What changes: each child's cards (Ali 20 to 16, Mei 12 to 16) and the difference (8 before, 0 after)."],
    'Add the cards before and after. Which number is the same both times?'))
