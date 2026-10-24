"""Online practice for Level 5 (Primary 5, ages 10 to 12) holiday lesson 7: Percentage ("Percentage Puzzles").

The questions are the ones printed in the Level 5 holiday workbook, lesson 7: Start here Q1 to Q5 (p5/content/l7.js, workbook()), the Investigation
(p5/content/inv.js), Think harder A1 to A4 (the first four 'stretch' questions of p5/content/l7.js qbank) and Go further B1 to B3 (the last three
'challenge' questions) and the "Make up your own" prompt (gaps.js), in the printed order, exactly as p5/workbook_html.js prints them.  Every answer is recomputed
by an INDEPENDENT checker below (a percentage is built by adding 1% over and over, a discount or a rise is applied step by step with exact fractions, a missing
whole is found by a search, the order of two discounts is tried for every pair of whole-number percentages), never by copying the printed answer;
build_holiday.py stops if a checker and the printed answer differ.  Every figure is drawn from the same numbers (practice/holiday/p5/p5fig4.py).
"""
import os, sys
HERE_ = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE_, '..', '..'))
sys.path.insert(0, os.path.join(HERE_, '..'))
from hlib import *          # noqa: E402,F401
from p5lib import *         # noqa: E402,F401
import p5fig3 as G3         # noqa: E402  (decimal answers)
import p5fig4 as G          # noqa: E402

META = dict(level=5, lesson=7, key='p5', title='Percentage Puzzles', workbook_title='PERCENTAGE PUZZLES', topic='Percentage', strand='Percentage',
            sources=['p5/content/l7.js', 'p5/content/inv.js', 'p5/content/gaps.js'],
            intro=['Percent means "out of 100". Find 10% by dividing by 10, 5% by halving that, and 1% by dividing by 100, and build any percentage from them. '
                   'Always ask: percentage of WHAT? After a rise, a cut or a discount, the new amount is the new whole. GST in Singapore is 9% of the price before GST.',
                   'Type the number in the box (a $ sign or a unit after the number is fine; you may type the % sign too). Money can have a decimal point, like 6.5. '
                   'Some questions ask you to explain: write your idea, then compare it with the model answer after you submit.'])
ST = 'Percentage'
F = Fraction


def D(**k):
    k.setdefault('strand', ST)
    return k


# ---------------------------------------------------------------- checkers: step-by-step arithmetic with exact fractions (no formula copied from a printed answer)
def pct(amount, p):
    """p% of an amount, built by adding 1% (one hundredth) p times."""
    one = F(amount) / 100
    t = F(0)
    for _ in range(p):
        t += one
    return t


def whole(v):
    v = F(v)
    assert v.denominator == 1, v
    return int(v)


def after(price, p, up=False):
    """The price after a rise (up=True) or a cut of p%, applied to THAT price."""
    return F(price) + pct(price, p) if up else F(price) - pct(price, p)


def txt(v):
    return G3.dec_text(F(v))


def money(v):
    return G3.dec_accepts(F(v), money=True, places=(2,))


def pct_of_whole(part, whole_):
    """What percentage `part` is of `whole_`: the number of 1% steps of the whole that fit."""
    one = F(whole_) / 100
    n = F(0)
    while one * (n + 1) <= part:
        n += 1
    assert one * n == part, (part, whole_)
    return int(n)


def goods_with_gst(price, rate=9):
    return F(price) + pct(price, rate)


def price_before_gst(total, rate=9):
    found = [x for x in range(1, 2000) if goods_with_gst(x, rate) == total]
    assert len(found) == 1, total
    return found[0]


def order_never_matters():
    """Every pair of whole-number discounts from 1% to 99%: is the price after a then b always equal to the price after b then a?"""
    for a in range(1, 100):
        for b in range(1, 100):
            if after(after(100, a), b) != after(after(100, b), a):
                return False
    return True


def money_at_first(left, p1, p2):
    """Mrs Tan style: spend p1% of the money, then p2% of what is left, and `left` remains.  Search the whole dollars of the money at first."""
    found = [m for m in range(1, 5000) if after(after(m, p1), p2) == left]
    assert len(found) == 1, (left, p1, p2)
    return found[0]


def shop_x_pays(boxes, price, buy, free):
    """'Buy `buy`, get `free` free': the boxes are taken in groups of buy+free; the child pays only for the `buy` boxes of each full group and for any boxes left over."""
    full, extra = divmod(boxes, buy + free)
    return (full * buy + extra) * F(price)


PRICE_A, DISC_A, GST = 160, 20, 9
SALE_A = after(PRICE_A, DISC_A)
GST_A = pct(SALE_A, GST)
PAY_A = SALE_A + GST_A
assert (SALE_A, GST_A, PAY_A) == (128, F(1152, 100), F(13952, 100))

BASE = 'Always ask: percentage of WHAT?'

ITEMS = [
    # ================= Start here (workbook lesson 7: Q1 to Q5)
    D(id='1t1', tier='core', no='1 (10% and 5%)', label='1 10%, 5%', type='fields', skill='building from 10%', answer=[24, 12],
      q='Percent means "out of 100". Build percentages of $240 from 10%, 5% and 1%.\nFirst the 10% and 5% boxes of the table. (Type the number of dollars.)',
      frame='10% of $240: $ {f1}     5% of $240: $ {f2}', check=lambda: [whole(pct(240, 10)), whole(pct(240, 5))],
      hint='10% is one tenth of the amount. 5% is half of 10%.',
      steps=['10% is one tenth: $240 ÷ 10 = $24.', '5% is half of 10%: $24 ÷ 2 = $12.'],
      src=['Percent means "out of 100". Build percentages of $240 from 10%, 5% and 1%. Fill in the table.']),
    D(id='1t2', tier='core', no='1 (1%)', label='1 1%', type='text', skill='building from 1%', accept=G3.dec_accepts(F(240, 100), money=True, places=(2,)), shown='2.40',
      q='Percent means "out of 100". Build percentages of $240 from 10%, 5% and 1%.\nNow the 1% box. (Type the number of dollars, like 3.50.)',
      check=lambda: txt(F(240) / 100),
      hint='1% is one hundredth of the amount.',
      steps=['1% is one hundredth: $240 ÷ 100 = $2.40.'],
      src=['Percent means "out of 100". Build percentages of $240 from 10%, 5% and 1%. Fill in the table.']),
    D(id='1t3', tier='core', no='1 (15% and 35%)', label='1 15%, 35%', type='fields', skill='building from 10%', answer=[36, 84],
      q='Percent means "out of 100". Build percentages of $240 from 10%, 5% and 1%.\nNow the 15% and 35% boxes. (Type the number of dollars.)',
      frame='15% of $240: $ {f1}     35% of $240: $ {f2}', check=lambda: [whole(pct(240, 15)), whole(pct(240, 35))],
      hint='Look at the 10% and 5% boxes you have already filled in. Can you add some of them?',
      steps=['15% = 10% + 5% = $24 + $12 = $36.', '35% = 10% + 10% + 10% + 5% = $72 + $12 = $84.'],
      src=['Percent means "out of 100". Build percentages of $240 from 10%, 5% and 1%. Fill in the table.']),
    D(id='1t4', tier='core', no='1 (99%)', label='1 99%', type='text', skill='building from 1%', accept=G3.dec_accepts(F(23760, 100), money=True, places=(2,)), shown='237.60',
      q='Percent means "out of 100". Build percentages of $240 from 10%, 5% and 1%.\nLast, the 99% box. (Type the number of dollars, like 3.50.)',
      check=lambda: txt(pct(240, 99)),
      hint='Use the boxes you already have.',
      steps=['99% is 100% take away 1%.', '100% of $240 is $240 and 1% is $2.40.', '$240 − $2.40 = $237.60.'],
      src=['Percent means "out of 100". Build percentages of $240 from 10%, 5% and 1%. Fill in the table.']),
    D(id='1a', tier='core', no='1(a)', label='1(a)', type='selfcheck', open=False, skill='explaining a method', facts=(36, 84),
      q='How did you find 35% of $240 from the boxes you already had? Write your idea, then compare it with the model answer.', check=lambda: (whole(pct(240, 15)), whole(pct(240, 35))),
      hint='Think about which boxes can be added together to make 35%.',
      steps=['35% is three 10%s and one 5%: 10% + 10% + 10% + 5%.', '3 × $24 + $12 = $72 + $12 = $84. (Another way: 15% + 10% + 10% = $36 + $24 + $24 = $84.)',
             'A good answer names the boxes you added, and each box is a percentage of the same $240.'],
      src=['How did you find 35% from the boxes you already had?']),
    D(id='1b', tier='core', no='1(b)', label='1(b)', type='selfcheck', open=False, skill='explaining a quick way', facts=(240, 24, 237.6),
      q='What is a quick way to find 99% of $240? Write your idea, then compare it with the model answer.', check=lambda: (240, whole(pct(240, 10)), float(pct(240, 99))),
      hint='How far is 99% from 100%?',
      steps=['99% is only 1% less than the whole. Find 1% and take it away from 100%.', '$240 − $2.40 = $237.60, much quicker than adding nine 10%s and a 5% and four 1%s.',
             'A good answer says "100% minus 1%".'],
      src=['A quick way to find 99% of $240:']),

    D(id='2s', tier='core', no='2 Start here', label='2 start', type='fields', skill='10% and 20%', answer=[16, 32],
      q='Mei wants a rice cooker. Two shops sell the same one. GST is 9%.\nStart here: find 10% of Shop A’s price by dividing by 10. Then 20% is double that. (Type the number of dollars.)', svg=G.shops(),
      frame='10% of $160: $ {f1}     20% of $160: $ {f2}', check=lambda: [whole(pct(160, 10)), whole(pct(160, 20))],
      hint='Divide $160 by 10 to find 10%. Then double it.',
      steps=['10% of $160 is $160 ÷ 10 = $16.', '20% is double that: 2 × $16 = $32.'],
      src=['Mei wants a rice cooker. Two shops sell the same one. GST is 9%.', 'find 10% of Shop A’s price by dividing by 10. Then 20% is double that.']),
    D(id='2a', tier='core', no='2(a)', label='2(a)', type='number', skill='discount', answer=128,
      q='Mei\'s rice cooker (GST is 9%).\nShop A: what is the price after 20% off, before GST? (Type the number of dollars.)', svg=G.shops(),
      check=lambda: whole(SALE_A), hint='Take 20% of $160 off the price. What is left?',
      steps=['20% of $160 is $32 (10% is $16, and double that).', '$160 − $32 = $128. The sale price is $128.'],
      src=['Shop A: the price after 20% off, before GST.']),
    D(id='2b', tier='core', no='2(b)', label='2(b)', type='text', skill='GST on the sale price', accept=money(F(1152, 100)), shown='11.52',
      q='Mei\'s rice cooker (GST is 9%).\nShop A: the GST on the sale price (the price after 20% off). (Type the number of dollars, like 3.50.)', svg=G.shops(),
      check=lambda: txt(GST_A), hint='The 9% GST is worked out on the SALE price, not on $160. Build 9% from 10% and 1% of the sale price.',
      steps=['Work out 9% of the sale price, $128. 10% of $128 is $12.80 and 1% is $1.28.', '9% = 10% − 1% = $12.80 − $1.28 = $11.52.', 'The GST is $11.52.'],
      src=['Shop A: the GST on the sale price.']),
    D(id='2c', tier='core', no='2(c)', label='2(c)', type='text', skill='price with GST', accept=money(F(13952, 100)), shown='139.52',
      q='Mei\'s rice cooker (GST is 9%).\nShop A: the price Mei pays (the sale price with the 9% GST added). (Type the number of dollars, like 3.50.)', svg=G.shops(),
      check=lambda: txt(PAY_A), hint='Add the GST to the sale price.',
      steps=['The sale price is $128 and the GST on it is $11.52.', '$128 + $11.52 = $139.52. Mei pays $139.52 at Shop A.'],
      src=['Shop A: the price Mei pays.']),
    D(id='2d', tier='core', no='2(d) which shop', label='2(d) shop', type='choice', skill='comparing prices', options=['Shop A', 'Shop B'], answer='Shop A',
      q='Mei\'s rice cooker (GST is 9%).\nWhich shop is cheaper for Mei?', svg=G.shops(),
      check=lambda: 'Shop A' if PAY_A < 140 else 'Shop B', hint='Shop B’s price already includes GST. Compare it with what Mei pays at Shop A.',
      steps=['At Shop A Mei pays $139.52 and at Shop B she pays $140.', 'Shop A is cheaper, even though it adds GST at the till.'],
      src=['Which shop is cheaper? By how much?']),
    D(id='2d2', tier='core', no='2(d) by how much', label='2(d) by', type='fields', dollars_ok=True, skill='comparing prices', answer=[48],
      q='Mei\'s rice cooker (GST is 9%).\nHow many cents cheaper is the cheaper shop? (Type just the number of cents.)', svg=G.shops(),
      frame='Cheaper by {f1}¢', check=lambda: [whole((140 - PAY_A) * 100)], hint='Subtract the two prices Mei would pay. A dollar is 100 cents.',
      steps=['Shop A: $139.52. Shop B: $140.', '$140 − $139.52 = $0.48, which is 48 cents.'],
      src=['Which shop is cheaper? By how much?']),

    D(id='3a', tier='core', no='3(a)', label='3(a)', type='number', skill='percentage rise', answer=100,
      q='A T-shirt cost $80. The shop raised its price by 25%. A month later, it cut the new price by 20%.\nWhat is the price after the 25% rise? (Type the number of dollars.)', svg=G.rise_cut_bars(),
      check=lambda: whole(after(80, 25, up=True)), hint='25% is a quarter. How much is a quarter of $80? Add it on.',
      steps=['25% of $80 is $20 (a quarter).', '$80 + $20 = $100.'],
      src=['A T-shirt cost $80. The shop raised its price by 25%. A month later, it cut the new price by 20%.', 'The price after the 25% rise:']),
    D(id='3b', tier='core', no='3(b)', label='3(b)', type='number', skill='percentage cut of the new price', answer=80,
      q='A T-shirt cost $80. The shop raised its price by 25%. A month later, it cut the new price by 20%.\nWhat is the price after the 20% cut? (Type the number of dollars.)', svg=G.rise_cut_bars(),
      sol_fig=lambda f: G.rise_cut_bars((80, 100, 80)),
      check=lambda: whole(after(after(80, 25, up=True), 20)), hint='The 20% is taken off the NEW price. First find the new price, then find 20% of it.',
      steps=['After the rise the price is $100.', '20% of $100 is $20.', '$100 − $20 = $80.'],
      src=['A T-shirt cost $80. The shop raised its price by 25%. A month later, it cut the new price by 20%.', 'The price after the 20% cut:']),
    D(id='3c', tier='core', no='3(c)', label='3(c)', type='choice', skill='spotting a percentage trap', options=['Yes, she is right', 'No, she is not right'], answer='No, she is not right',
      q='A T-shirt cost $80. The shop raised its price by 25% and then cut the new price by 20%.\nSiti says, “Up 25% and then down 20% is the same as up 5%, so the final price is $84.” Is she right?',
      check=lambda: 'Yes, she is right' if after(after(80, 25, up=True), 20) == 84 else 'No, she is not right',
      hint='Work out the final price step by step and compare it with $84.',
      steps=['Up 25%: $80 becomes $100. Down 20% of $100: $100 − $20 = $80.', 'The final price is $80, not $84, so Siti is not right.'],
      src=['Siti says, "Up 25% and then down 20% is the same as up 5%, so the final price is $84." Is she right? Explain.']),
    D(id='3c2', tier='core', no='3(c) explain', label='3(c) why', type='selfcheck', open=False, skill='explaining a percentage trap', facts=(80, 84),
      q='Siti says, “Up 25% and then down 20% is the same as up 5%.” Explain what is true or not true about her idea. Write your idea, then compare it with the model answer.',
      check=lambda: (whole(after(after(80, 25, up=True), 20)), 84), hint='The 25% and the 20% are percentages of different amounts. Which amounts?',
      steps=['The 25% rise is a percentage of the old price, $80. The 20% cut is a percentage of the NEW price, $100.', '20% of $100 is $20, which is exactly the $20 that the rise added, so the price is back to $80.',
             'A good answer says that percentages of different wholes cannot just be added or taken away.'],
      sol_fig=lambda f: G.rise_cut_bars((80, 100, 80)),
      src=['Siti says, "Up 25% and then down 20% is the same as up 5%, so the final price is $84." Is she right? Explain.']),

    D(id='4s', tier='core', no='4 Start here', label='4 start', type='fields', skill='10% and 20%', answer=[12, 24],
      q='Siti had $120. She spent 20% of her money on a bag. Then she spent 25% of the remaining money on a book.\nStart here: 10% of $120 is $__, so 20% of $120 is $__. (Type the numbers.)', svg=G.bag_bar(),
      frame='10% of $120: $ {f1}     20% of $120: $ {f2}', check=lambda: [whole(pct(120, 10)), whole(pct(120, 20))],
      hint='Divide $120 by 10 to find 10%. Then double it for 20%.',
      steps=['10% of $120 is $120 ÷ 10 = $12.', '20% is double that: 2 × $12 = $24.'],
      src=['Siti had $120. She spent 20% of her money on a bag. Then she spent 25% of the remaining money on a book.', '10% of $120 is $______, so 20% of $120 is $______.']),
    D(id='4a', tier='core', no='4(a)', label='4(a)', type='number', skill='percentage of an amount', answer=24,
      q='Siti had $120. She spent 20% of her money on a bag. Then she spent 25% of the remaining money on a book.\nThe bag cost how many dollars?', svg=G.bag_bar(),
      check=lambda: whole(pct(120, 20)), hint='The bag cost 20% of the $120 she had at first.',
      steps=['20% of $120 is $24.', 'The bag cost $24.'],
      src=['The bag cost']),
    D(id='4b', tier='core', no='4(b)', label='4(b)', type='number', skill='percentage of a remainder', answer=24,
      q='Siti had $120. She spent 20% of her money on a bag. Then she spent 25% of the remaining money on a book.\nThe book cost how many dollars?', svg=G.bag_bar(),
      check=lambda: whole(pct(120 - pct(120, 20), 25)), hint='The 25% is of the money that was left after the bag, not of the $120. First find the money left.',
      steps=['After the bag, Siti had $120 − $24 = $96 left.', '25% of $96 is a quarter of $96, which is $24.', 'The book cost $24.'],
      src=['(b)  The book cost']),
    D(id='4c', tier='core', no='4(c)', label='4(c)', type='number', skill='money left', answer=72,
      q='Siti had $120. She spent 20% of her money on a bag. Then she spent 25% of the remaining money on a book.\nHow many dollars did she have left?', svg=G.bag_bar(),
      sol_fig=lambda f: G.bag_bar((24, 24, 72)),
      check=lambda: whole(120 - pct(120, 20) - pct(120 - pct(120, 20), 25)), hint='Take both amounts she spent away from her $120.',
      steps=['The bag cost $24 and the book cost $24.', '$120 − $24 − $24 = $72.', 'Siti had $72 left.'],
      src=['(c)  Money left']),
    D(id='4d', tier='core', no='4(d)', label='4(d)', type='fields', skill='percentage left', answer=[60],
      q='Siti had $120. She spent 20% of her money on a bag. Then she spent 25% of the remaining money on a book.\nBen says, “She spent 20% + 25% = 45%, so 55% of her money is left.” What percentage of her money is really left? (Type just the number.)', svg=G.bag_bar(),
      frame='Really left: {f1}%', check=lambda: [pct_of_whole(120 - pct(120, 20) - pct(120 - pct(120, 20), 25), 120)],
      hint='Write her money left as a part of the $120 she had at first. How many hundredths of $120 is it?',
      steps=['She had $72 left out of $120.', '$72 out of $120 is 60 out of 100, so 60% is left.'],
      src=['Ben says, "She spent 20% + 25% = 45%, so 55% of her money is left." What percentage of her money is really left? Explain.']),
    D(id='4d2', tier='core', no='4(d) explain', label='4(d) why', type='selfcheck', open=False, skill='explaining a percentage trap', facts=(72, 120),
      q='Siti had $120. She spent 20% of it on a bag and then 25% of the remaining money on a book. Ben says, “She spent 20% + 25% = 45%, so 55% is left.” Explain what is wrong with adding the percentages. Write your idea, then compare it with the model answer.',
      check=lambda: (whole(120 - pct(120, 20) - pct(120 - pct(120, 20), 25)), 120), hint='Is the 25% a percentage of the same amount as the 20%?',
      steps=['The 20% is a percentage of the $120. The 25% is a percentage of the $96 left after the bag, a different amount.', 'So the two percentages cannot just be added. She spent $24 + $24 = $48 of $120, which is 40%, so 60% is left.',
             'A good answer says that the 25% is not a percentage of the same whole.'],
      sol_fig=lambda f: G.bag_bar((24, 24, 72)),
      src=['Ben says, "She spent 20% + 25% = 45%, so 55% of her money is left." What percentage of her money is really left? Explain.']),

    D(id='5s', tier='core', no='5 Start here', label='5 start', type='fields', skill='10% of a total', answer=[4, 24],
      q='There are 40 pupils in a class. 60% of them are girls. 25% of the girls and 50% of the boys wear glasses.\nStart here: 10% of 40 pupils is __, so 60% (the girls) is __ pupils. (Type the numbers.)', svg=G.class_table(),
      frame='10% of 40: {f1} pupils     60% of 40: {f2} pupils', check=lambda: [whole(pct(40, 10)), whole(pct(40, 60))],
      hint='Divide 40 by 10 for 10%. How many tens of percent make 60%?',
      steps=['10% of 40 pupils is 40 ÷ 10 = 4 pupils.', '60% is six times that: 6 × 4 = 24 pupils.'],
      src=['There are 40 pupils in a class. 60% of them are girls. 25% of the girls and 50% of the boys wear glasses. Fill in the table.',
           '10% of 40 pupils is ______, so 60% (the girls) is ______ pupils. The rest are boys.']),
    D(id='5t', tier='core', no='5 table: pupils', label='5 pupils', type='fields', skill='table of percentages', answer=[24, 16],
      q='There are 40 pupils in a class. 60% of them are girls. The rest are boys.\nFill in the first row of the table: the number of girls and of boys.', svg=G.class_table(),
      frame='Girls: {f1}     Boys: {f2}', check=lambda: [whole(pct(40, 60)), whole(40 - pct(40, 60))],
      hint='Find 60% of 40 for the girls. The rest of the class are boys.',
      steps=['Girls: 60% of 40 = 24.', 'Boys: 40 − 24 = 16.'],
      src=['There are 40 pupils in a class. 60% of them are girls. 25% of the girls and 50% of the boys wear glasses. Fill in the table.']),
    D(id='5g', tier='core', no='5 table: glasses', label='5 glasses', type='fields', skill='table of percentages', answer=[6, 8, 14],
      q='There are 40 pupils in a class. 60% of them are girls. The rest are boys. 25% of the girls and 50% of the boys wear glasses.\nFill in the last row of the table: how many pupils wear glasses?', svg=G.class_table(),
      sol_fig=lambda f: G.class_table((24, 16, 6, 8)),
      frame='Girls: {f1}     Boys: {f2}     Whole class: {f3}', check=lambda: [whole(pct(pct(40, 60), 25)), whole(pct(40 - pct(40, 60), 50)), whole(pct(pct(40, 60), 25) + pct(40 - pct(40, 60), 50))],
      hint='Find the number of girls and the number of boys first. Each percentage is of its own group.',
      steps=['Girls wearing glasses: 25% of 24 = 6.', 'Boys wearing glasses: 50% of 16 = 8.', 'Whole class: 6 + 8 = 14.'],
      src=['There are 40 pupils in a class. 60% of them are girls. 25% of the girls and 50% of the boys wear glasses. Fill in the table.']),
    D(id='5a', tier='core', no='5(a)', label='5(a)', type='fields', skill='percentage of a whole', answer=[35],
      q='There are 40 pupils in a class. 60% of them are girls. 25% of the girls and 50% of the boys wear glasses.\nWhat percentage of the whole class wear glasses? (Type just the number.)',
      frame='{f1}% of the class', check=lambda: [pct_of_whole(pct(pct(40, 60), 25) + pct(40 - pct(40, 60), 50), 40)],
      hint='First work out how many pupils wear glasses. Then write that number out of 40 as a number out of 100.',
      steps=['Girls wearing glasses: 25% of 24 = 6. Boys wearing glasses: 50% of 16 = 8. In all 6 + 8 = 14 pupils wear glasses.', '10% of 40 pupils is 4 pupils. 14 pupils is 3 tens of percent and a bit: 12 + 2.', '2 pupils is half of 4, which is 5%.', '30% + 5% = 35%. (Check: 35% of 40 = 14.)'],
      src=['What percentage of the whole class wear glasses?']),

    # ================= Investigation: Is it always true? Test and explain
    D(id='C0', tier='invest', no='C (easy first step)', label='C easy', type='fields', skill='discount of a discount', answer=[80, 72],
      q='Is it always true? Test and explain.\nEasy first step: on a $100 bag take 20% off and write the new price. Then take 10% off that new price.',
      frame='After 20% off: $ {f1}     After 10% off that: $ {f2}', check=lambda: [whole(after(100, 20)), whole(after(after(100, 20), 10))],
      hint='Take 20% off $100 first. Then find 10% of the NEW price, not of $100.',
      steps=['20% of $100 is $20, so the new price is $100 − $20 = $80.', '10% of $80 is $8, so $80 − $8 = $72.'],
      src=['Easy first step: on a $100 bag take 20% off (that is $20) and write the new price. Then take 10% off that new price. Then do part (a) the other way round.']),
    D(id='Ca', tier='invest', no='C(a) both prices', label='C(a) prices', type='fields', skill='order of discounts', answer=[72, 72],
      q='A $100 bag is on sale. Shop 1 takes 20% off and then a further 10% off the new price. Shop 2 takes 10% off first and then a further 20% off the new price.\nWork out both prices. (Type the number of dollars.)',
      frame='Shop 1: $ {f1}     Shop 2: $ {f2}', check=lambda: [whole(after(after(100, 20), 10)), whole(after(after(100, 10), 20))],
      hint='Take each discount off the price you have at that moment, one after the other.',
      steps=['Shop 1: $100 → $80 → $72.', 'Shop 2: $100 → $90 → $72.', 'Both bags cost $72.'],
      src=['A $100 bag is on sale. Shop 1 takes 20% off and then a further 10% off the new price. Shop 2 takes 10% off first and then a further 20% off the new price. Work out both prices. Is one cheaper?']),
    D(id='Ca2', tier='invest', no='C(a) is one cheaper', label='C(a) cheaper', type='choice', skill='order of discounts',
      options=['Shop 1 is cheaper', 'Shop 2 is cheaper', 'The two prices are the same'], answer='The two prices are the same',
      q='A $100 bag is on sale. Shop 1 takes 20% off and then a further 10% off the new price. Shop 2 takes 10% off first and then a further 20% off the new price.\nIs one of the shops cheaper?',
      check=lambda: ('The two prices are the same' if after(after(100, 20), 10) == after(after(100, 10), 20) else ('Shop 1 is cheaper' if after(after(100, 20), 10) < after(after(100, 10), 20) else 'Shop 2 is cheaper')),
      hint='Work out the final price in each shop and compare.',
      steps=['Shop 1 ends at $72 and Shop 2 ends at $72.', 'The two prices are the same.'],
      src=['A $100 bag is on sale. Shop 1 takes 20% off and then a further 10% off the new price. Shop 2 takes 10% off first and then a further 20% off the new price. Work out both prices. Is one cheaper?']),
    D(id='Cb1', tier='invest', no='C(b) test 1', label='C(b) test 1', type='fields', skill='testing the order of discounts', answer=[45, 45],
      q='Test a pair of discounts on a $100 bag. Take 50% off and then a further 10% off the new price. Then try it the other way round: 10% off first and then a further 50% off the new price.\n(Type the number of dollars.)',
      frame='50% then 10%: $ {f1}     10% then 50%: $ {f2}', check=lambda: [whole(after(after(100, 50), 10)), whole(after(after(100, 10), 50))],
      hint='Take each discount off the price you have at that moment.',
      steps=['50% then 10%: $100 → $50 → $45.', '10% then 50%: $100 → $90 → $45.'],
      src=['Test two more pairs of discounts of your own (for example 50% and 10%, or 30% and 20%).']),
    D(id='Cb2', tier='invest', no='C(b) test 2', label='C(b) test 2', type='fields', skill='testing the order of discounts', answer=[56, 56],
      q='Test another pair on a $100 bag. Take 30% off and then a further 20% off the new price. Then try it the other way round: 20% off first and then a further 30% off the new price.\n(Type the number of dollars.)',
      frame='30% then 20%: $ {f1}     20% then 30%: $ {f2}', check=lambda: [whole(after(after(100, 30), 20)), whole(after(after(100, 20), 30))],
      hint='Take each discount off the price you have at that moment.',
      steps=['30% then 20%: $100 → $70 → $56.', '20% then 30%: $100 → $80 → $56.'],
      src=['Test two more pairs of discounts of your own (for example 50% and 10%, or 30% and 20%).']),
    D(id='Cbown', tier='invest', no='C(b) your own', label='C(b) own', type='selfcheck', open=True, marking_mode='open', skill='testing with your own numbers',
      q='Test two more pairs of discounts of your own on a $100 bag. Work each pair both ways round. Then compare your tests with the model answer.',
      hint='Choose two discounts that are easy to take off, like 20% or 40%. Take them off in one order, and then in the other order.',
      steps=['This question is open: many pairs are right.', 'Sample: 40% and 25%. 40% then 25%: $100 → $60 → $45. 25% then 40%: $100 → $75 → $45.', 'Check that you took the second discount off the new price each time.'],
      src=['Test two more pairs of discounts of your own (for example 50% and 10%, or 30% and 20%).']),
    D(id='Cb3', tier='invest', no='C(b) always', label='C(b) always', type='choice', skill='order of discounts',
      options=['The order never changes the final price', 'The order sometimes changes the final price'], answer='The order never changes the final price',
      q='Think about two discounts, one taken off after the other. Does the ORDER of the two discounts ever change the final price?',
      check=lambda: 'The order never changes the final price' if order_never_matters() else 'The order sometimes changes the final price',
      hint='Look at the pairs you tested. Did the order ever change a price?',
      steps=['Every pair that we tested gave the same price both ways round.', 'Trying every pair of whole-number percentages from 1% to 99% on a computer shows the same: the order never changes the final price.'],
      src=['Does the ORDER of two discounts ever change the final price? Is it always true?']),
    D(id='Cb4', tier='invest', no='C(b) explain', label='C(b) why', type='selfcheck', open=False, skill='explaining why the order does not matter', facts=(F(4, 5) * F(9, 10), F(9, 10) * F(4, 5)),
      q='Explain what you notice about the order of two discounts. Write your idea, then compare it with the model answer.', check=lambda: (F(4, 5) * F(9, 10), F(9, 10) * F(4, 5)),
      hint='After a discount you still pay a fraction of the price. What fraction do you pay after 20% off? After 10% off?',
      steps=['After 20% off you pay 4/5 of the price. After 10% off you pay 9/10 of the price.', '4/5 of 9/10 and 9/10 of 4/5 are the same amount: 36/50 of the price. Multiplying does not depend on the order.',
             'A good answer says that each discount keeps a fraction of the price, and the same two fractions are used in either order.'],
      src=['Does the ORDER of two discounts ever change the final price? Is it always true?']),
    D(id='Cc1', tier='invest', no='C(c) 30% off', label='C(c) 30%', type='number', skill='one big discount', answer=70,
      q='Take 30% off a $100 bag in one go. What is the price? (Type the number of dollars.)', check=lambda: whole(after(100, 30)),
      hint='30% of $100, then take it away.',
      steps=['30% of $100 is $30.', '$100 − $30 = $70.'],
      src=['Is 20% off then 10% off the same as 30% off? Test and explain.']),
    D(id='Cc2', tier='invest', no='C(c) same?', label='C(c) same', type='choice', skill='combining discounts', options=['Yes, they are the same', 'No, they are not the same'], answer='No, they are not the same',
      q='Is 20% off then 10% off the same as 30% off in one go? Test it on a $100 bag.',
      check=lambda: 'Yes, they are the same' if after(after(100, 20), 10) == after(100, 30) else 'No, they are not the same',
      hint='Work out the final price both ways and compare.',
      steps=['20% off then 10% off the new price: $100 → $80 → $72.', '30% off in one go: $100 → $70.', 'The prices are different, so they are not the same.'],
      src=['Is 20% off then 10% off the same as 30% off? Test and explain. (Hint: after 20% off, you pay 4/5. After 10% off, you pay 9/10.)']),
    D(id='Cc3', tier='invest', no='C(c) explain', label='C(c) why', type='selfcheck', open=False, skill='explaining percentage of what', facts=(72, 70),
      q='Explain what you notice when you compare 20% off then 10% off with 30% off. Write your idea, then compare it with the model answer.',
      check=lambda: (whole(after(after(100, 20), 10)), whole(after(100, 30))),
      hint='Look at your $100 bag again. What is the second discount, 10% off, taken off: $100 or a different price?',
      steps=['The second discount of 10% is taken from the smaller price, $80, so it takes off $8 and not $10.', 'So 20% then 10% takes off $28 in all, which is less than the $30 that 30% takes off.',
             'A good answer mentions "percentage of WHAT": the 10% is of a smaller price.'],
      src=['Is 20% off then 10% off the same as 30% off? Test and explain. (Hint: after 20% off, you pay 4/5. After 10% off, you pay 9/10.)']),

    # ================= Think harder (A1 to A4)
    D(id='A1a', tier='stretch', no='A1(a)', label='A1(a)', type='fields', skill='percentage increase', answer=[25],
      q='At a hawker centre, a plate of chicken rice went up from $4 to $5. A month later, it went back down from $5 to $4.\nFind the percentage increase from $4 to $5. (Type just the number.)',
      frame='Increase: {f1}%', check=lambda: [pct_of_whole(5 - 4, 4)], hint='Percentage change = the change out of the amount you START with. What is the change, and what is the start?',
      steps=['The price went up by $1.', 'It started at $4. $1 out of $4 is 25 out of 100.', 'The increase is 25%.'],
      src=['At a hawker centre, a plate of chicken rice went up from $4 to $5. A month later, it went back down from $5 to $4. (a) Find the percentage increase from $4 to $5.']),
    D(id='A1b', tier='stretch', no='A1(b)', label='A1(b)', type='fields', skill='percentage decrease', answer=[20],
      q='At a hawker centre, a plate of chicken rice went up from $4 to $5. A month later, it went back down from $5 to $4.\nFind the percentage decrease from $5 to $4. (Type just the number.)',
      frame='Decrease: {f1}%', check=lambda: [pct_of_whole(5 - 4, 5)], hint='Percentage change = the change out of the amount you START with. What is the start this time?',
      steps=['The price went down by $1.', 'It started at $5. $1 out of $5 is 20 out of 100.', 'The decrease is 20%.'],
      src=['(b) Find the percentage decrease from $5 to $4.']),
    D(id='A1c', tier='stretch', no='A1(c)', label='A1(c)', type='selfcheck', open=False, skill='explaining percentage change', facts=(25, 20),
      q='Both changes were $1. Explain what you notice about the two percentages. Write your idea, then compare it with the model answer.', check=lambda: (pct_of_whole(1, 4), pct_of_whole(1, 5)),
      hint='Percentage change = the change out of the amount you START with.',
      steps=['A percentage change compares the change with the starting amount.', '$1 out of $4 is a bigger part than $1 out of $5, so the increase is 25% and the decrease is 20%.',
             'A good answer says that the two changes start from different amounts.'],
      src=['(c) Both changes are $1. Why are the two percentages different? Hint: percentage change = the change out of the amount you START with.']),
    D(id='A2a', tier='stretch', no='A2(a) pays', label='A2(a) pay', type='fields', skill='comparing deals', answer=[45, 42],
      q='A box of cereal costs $15 in two shops. Shop X: “Buy 3, get 1 free!” Shop Y: “30% off every box!” Mei buys 4 boxes.\nHow much does she pay at each shop? (Type the number of dollars.)',
      frame='Shop X: $ {f1}     Shop Y: $ {f2}', check=lambda: [whole(shop_x_pays(4, 15, 3, 1)), whole(after(4 * 15, 30))],
      hint='At Shop X she pays for only some of the boxes. At Shop Y the 30% is off the cost of all 4 boxes.',
      steps=['Shop X: she pays for 3 boxes: 3 × $15 = $45.', 'Shop Y: 4 boxes cost $60. 30% of $60 is $18, so she pays $60 − $18 = $42.'],
      src=['A box of cereal costs $15 in two shops. Shop X: "Buy 3, get 1 free!" Shop Y: "30% off every box!" Mei buys 4 boxes. (a) How much does she pay at each shop? Which is the better buy, and by how much?']),
    D(id='A2b', tier='stretch', no='A2(a) better buy', label='A2(a) best', type='choice', skill='comparing deals', options=['Shop X', 'Shop Y'], answer='Shop Y',
      q='A box of cereal costs $15 in two shops. Shop X: “Buy 3, get 1 free!” Shop Y: “30% off every box!” Mei buys 4 boxes.\nWhich shop is the better buy?',
      check=lambda: 'Shop X' if shop_x_pays(4, 15, 3, 1) < after(60, 30) else 'Shop Y', hint='The better buy is the shop where Mei pays less for the 4 boxes.',
      steps=['Mei pays $45 at Shop X and $42 at Shop Y.', 'Shop Y is the better buy.'],
      src=['Which is the better buy, and by how much?']),
    D(id='A2c', tier='stretch', no='A2(a) by how much', label='A2(a) by', type='fields', skill='comparing deals', answer=[3],
      q='A box of cereal costs $15 in two shops. Shop X: “Buy 3, get 1 free!” Shop Y: “30% off every box!” Mei buys 4 boxes.\nThe better buy saves her how many dollars?',
      frame='Saves $ {f1}', check=lambda: [whole(abs(shop_x_pays(4, 15, 3, 1) - after(60, 30)))], hint='Subtract the two prices she would pay.',
      steps=['The two prices are $45 and $42.', '$45 − $42 = $3.'],
      src=['Which is the better buy, and by how much?']),
    D(id='A2d', tier='stretch', no='A2(b)', label='A2(b)', type='fields', skill='free boxes as a percentage', answer=[25],
      q='A box of cereal costs $15. Shop X’s deal is “Buy 3, get 1 free!” For 4 boxes, Shop X’s deal is really how many percent off? (Type just the number.)',
      frame='{f1}% off', check=lambda: [pct_of_whole(60 - shop_x_pays(4, 15, 3, 1), 60)],
      hint='How many dollars does the deal save on the 4 boxes? Write that as a part of the usual price of all 4 boxes.',
      steps=['4 boxes cost $60 at the usual price. With the deal Mei pays $45, so she saves $15.', '$15 out of $60 is 25 out of 100, so the deal is 25% off.'],
      src=["(b) Shop X's deal is really how many percent off?"]),
    D(id='A3a', tier='stretch', no='A3 (method)', label='A3 method', type='selfcheck', open=False, skill='explaining a percentage method', facts=(8, 4),
      q='Siti says, “15% of $80 is $8 + $4 = $12.” Explain her method. Write your idea, then compare it with the model answer.', check=lambda: (whole(pct(80, 10)), whole(pct(80, 5))),
      hint='Where could the $8 and the $4 come from? Think about 10% and 5% of $80.',
      steps=['She found 10% of $80, which is $8.', 'She found 5% of $80, which is half of that, $4.', '15% = 10% + 5%, so she added $8 + $4 = $12.'],
      src=['Siti says, "15% of $80 is $8 + $4 = $12." Explain her method. Use it to find 15% of $46.']),
    D(id='A3b', tier='stretch', no='A3 (15% of 46)', label='A3 15%', type='text', skill='percentage of an amount', accept=money(F(690, 100)), shown='6.90',
      q='Siti says, “15% of $80 is $8 + $4 = $12.” Use her method to find 15% of $46. (Type the number of dollars, like 3.50.)', check=lambda: txt(pct(46, 15)),
      hint='Look at how $8 and $4 come from $80. Do the same steps with $46.',
      steps=['10% of $46 is $4.60.', '5% of $46 is half of that: $2.30.', '$4.60 + $2.30 = $6.90.'],
      src=['Siti says, "15% of $80 is $8 + $4 = $12." Explain her method. Use it to find 15% of $46.']),
    D(id='A4', tier='stretch', no='A4', type='fields', skill='discount', answer=[30, 220],
      q='A $250 bicycle is sold at a 12% discount. How much money is saved? What is the sale price? (Type the number of dollars.)',
      frame='Saved: $ {f1}     Sale price: $ {f2}', check=lambda: [whole(pct(250, 12)), whole(after(250, 12))],
      hint='Build 12% from 10% and 1% of $250, then take the saving off $250.',
      steps=['10% of $250 is $25 and 1% is $2.50, so 2% is $5.', '12% = 10% + 2% = $25 + $5 = $30 saved.', '$250 − $30 = $220.'],
      src=['A $250 bicycle is sold at a 12% discount. How much money is saved? What is the sale price?']),

    # ================= Go further (B1 to B3)
    D(id='B1a', tier='challenge', no='B1 (is he right)', label='B1 right', type='choice', skill='GST included in a price', options=['Yes, Ali is right', 'No, Ali is not right'], answer='No, Ali is not right',
      q='A price tag says $109, GST included. GST is 9%.\nAli says the GST is 9% of $109, which is $9.81. Is he right?',
      check=lambda: 'Yes, Ali is right' if pct(109, 9) == price_before_gst(109) * F(9, 100) else 'No, Ali is not right',
      hint='GST is 9% of the price BEFORE GST. Is $109 the price before GST?',
      steps=['The GST is added to a price. It is 9% of the price before GST.', '$109 is the price after the GST was added, so 9% of $109 is not the GST.', 'Ali is not right.'],
      src=['A price tag says $109, GST included. GST is 9%. Ali says the GST is 9% of $109, which is $9.81. Is he right? How much GST is in the price?']),
    D(id='B1b', tier='challenge', no='B1 (the GST)', label='B1 GST', type='fields', skill='GST included in a price', answer=[9],
      q='A price tag says $109, GST included. GST is 9%.\nHow much GST is in the price? (Type the number of dollars.)',
      frame='GST: $ {f1}', check=lambda: [whole(pct(price_before_gst(109), 9))],
      hint='The GST is 9% of the price before GST. $109 is that price plus the GST: what percentage of the price before GST is $109?',
      steps=['The price before GST is 100%. With 9% GST added, $109 is 109% of it.', '109% is $109, so 1% is $1 and the price before GST is $100.', 'The GST is 9% of $100, which is $9.'],
      src=['A price tag says $109, GST included. GST is 9%. Ali says the GST is 9% of $109, which is $9.81. Is he right? How much GST is in the price?']),
    D(id='B2a', tier='challenge', no='B2 (which shop)', label='B2 shop', type='choice', skill='two ways of discounting', options=['Shop P', 'Shop Q'], answer='Shop P',
      q='An $80 lamp is on sale in two shops. Shop P takes 25% off. Shop Q takes 10% off, and then a further 15% off the new price.\nIn which shop is the lamp cheaper?',
      check=lambda: 'Shop P' if after(80, 25) < after(after(80, 10), 15) else 'Shop Q', hint='Work out the price in each shop. In Shop Q, the 15% is taken off the price after the first discount.',
      steps=['Shop P: 25% of $80 is $20, so the lamp costs $60.', 'Shop Q: 10% of $80 is $8, so $72. Then 15% of $72 is $10.80, so the lamp costs $61.20.', 'Shop P is cheaper.'],
      src=['An $80 lamp is on sale in two shops. Shop P takes 25% off. Shop Q takes 10% off, and then a further 15% off the new price. In which shop is the lamp cheaper, and by how much?']),
    D(id='B2b', tier='challenge', no='B2 (by how much)', label='B2 by', type='text', skill='two ways of discounting', accept=money(F(120, 100)), shown='1.20',
      q='An $80 lamp is on sale in two shops. Shop P takes 25% off. Shop Q takes 10% off, and then a further 15% off the new price.\nThe cheaper shop is cheaper by how many dollars? (Type the number of dollars, like 3.50.)',
      check=lambda: txt(abs(after(80, 25) - after(after(80, 10), 15))), hint='Find both prices, then subtract.',
      steps=['Shop P: $60. Shop Q: $61.20.', '$61.20 − $60 = $1.20.'],
      src=['An $80 lamp is on sale in two shops. Shop P takes 25% off. Shop Q takes 10% off, and then a further 15% off the new price. In which shop is the lamp cheaper, and by how much?']),
    D(id='B3', tier='challenge', no='B3', type='number', skill='working backwards with percentages', answer=120,
      q='Mrs Tan spent 40% of her money on groceries and 25% of the remaining money on a gift. She had $54 left. How much money did she have at first? (Type the number of dollars.)',
      check=lambda: money_at_first(54, 40, 25), hint='Work backwards. $54 is what percentage of the money she had before buying the gift?',
      steps=['After the gift she had $54 left. The gift took 25% of what she had before it, so $54 is 75% of that amount.', '25% is $18 (a third of $54), so the money before the gift was $54 + $18 = $72.',
             '$72 is what was left after the groceries, so it is 60% of her money. 10% is $12, so 100% is $120.'],
      sol_fig=None,
      src=['Mrs Tan spent 40% of her money on groceries and 25% of the remaining money on a gift. She had $54 left. How much money did she have at first?']),
    D(id='pose', tier='challenge', no='Make up your own', label='Make up', type='selfcheck', open=True, marking_mode='open', skill='making up a problem',
      q='Make up a price that goes up by a percentage and then down by the same percentage. Predict the final price, then test it.',
      hint='Choose a starting price that is easy, like $100 or $200, and a percentage like 10% or 50%. Predict first, then work out each step.',
      steps=['This question is open: many puzzles are right.', 'Test it step by step. The percentage down is taken from the NEW, higher price, so you do not get back to the start.',
             'Sample: $100 up 10% is $110. Down 10% of $110 is $11, so the final price is $99, not $100.'],
      src=['Make up a price that goes up by a percentage and then down by the same percentage. Predict the final price, then test it.']),
]


# ---------------------------------------------------------------- variants: a template with an oracle that works the answer out step by step
def _o_t(e):
    return dict(f1=whole(pct(e['A'], 10)), f2=whole(pct(e['A'], 5)))


def _o_2a(e):
    return whole(after(e['P'], e['d']))


def _o_3a(e):
    return whole(after(e['B'], e['p'], up=True))


def _o_4a(e):
    return whole(pct(e['M'], e['p']))


def _o_4c(e):
    return whole(e['M'] - pct(e['M'], e['p1']) - pct(e['M'] - pct(e['M'], e['p1']), e['p2']))


def _o_a1(e):
    b = e['a'] + F(e['a'] * e['p'], 100)
    return pct_of_whole(b - e['a'], e['a'])


def _o_a2d(e):
    boxes = e['n'] + 1
    return pct_of_whole(boxes * 15 - shop_x_pays(boxes, 15, e['n'], 1), boxes * 15)


def _o_a4(e):
    return dict(f1=whole(pct(e['P'], e['d'])), f2=whole(after(e['P'], e['d'])))


finish(ITEMS)

VARIANTS = {
    '1t1': dict(
        base=dict(A=240),
        tpl=dict(vars=dict(A=[120, 160, 200, 240, 300, 360]),
                 q='Percent means "out of 100". Find 10% and 5% of ${A}. (Type the number of dollars.)', frame='10% of ${A}: $ {f1}     5% of ${A}: $ {f2}', answers=dict(f1='A / 10', f2='A / 20'),
                 hint='10% is one tenth of the amount. 5% is half of 10%.',
                 steps=['10% is one tenth: divide ${A} by 10.', '5% is half of 10%.', 'The two amounts are {ans}.']),
        oracle=_o_t),
    '2a': dict(
        base=dict(P=160, d=20),
        tpl=dict(vars=dict(P=[160, 200, 240, 300], d=[10, 20, 25]),
                 q='A rice cooker costs ${P} before GST. The shop takes {d}% off. What is the price after the discount, before GST? (Type the number of dollars.)', answer='P * (100 - d) / 100',
                 hint='Find {d}% of ${P} and take it off the price.',
                 steps=['Find {d}% of ${P}: build it from 10% and 5%, or from 1%.', 'Take that amount off ${P}.', 'The price after the discount is ${ans}.']),
        oracle=_o_2a),
    '3a': dict(
        base=dict(B=80, p=25),
        tpl=dict(vars=dict(B=[80, 120, 200], p=[10, 25, 50]),
                 q='A T-shirt cost ${B}. The shop raised its price by {p}%. What is the new price? (Type the number of dollars.)', answer='B * (100 + p) / 100',
                 hint='Find {p}% of ${B}. Add it on.',
                 steps=['Find {p}% of ${B}.', 'Add it to ${B}.', 'The new price is ${ans}.']),
        oracle=_o_3a),
    '4a': dict(
        base=dict(M=120, p=20),
        tpl=dict(vars=dict(M=[100, 120, 150, 200, 250], p=[10, 20, 30, 40]),
                 q='Siti had ${M}. She spent {p}% of her money on a bag. How many dollars did the bag cost?', answer='M * p / 100',
                 hint='The bag cost {p}% of the ${M} she had at first.',
                 steps=['Find {p}% of ${M}: build it from 10% and 5%, or from 1%.', 'The bag cost ${ans}.']),
        oracle=_o_4a),
    '4c': dict(
        base=dict(M=120, p1=20, p2=25),
        tpl=dict(vars=dict(M=[100, 120, 200, 300], p1=[20, 40], p2=[25, 50]),
                 q='Siti had ${M}. She spent {p1}% of her money on a bag. Then she spent {p2}% of the remaining money on a book. How many dollars did she have left?',
                 answer='M * (100 - p1) * (100 - p2) / 10000', hint='The {p2}% is of the money left after the bag, not of ${M}. Find the money left after the bag first.',
                 steps=['The bag cost {p1}% of ${M}. Take it off to find the money left after the bag.', 'The book cost {p2}% of that money left.', 'Take the book off too. Siti has ${ans} left.']),
        oracle=_o_4c),
    'A1a': dict(
        base=dict(a=4, d=1),
        tpl=dict(vars=dict(a=[20, 40, 50, 100], d=[2, 4, 10, 20]), derive=dict(b='a + d'),
                 q='A price went up from ${a} to ${b}. Find the percentage increase. (Type just the number.)', frame='Increase: {f1}%', answers=dict(f1='d * 100 / a'),
                 hint='Percentage change = the change out of the amount you START with.',
                 steps=['The price went up by ${b} − ${a} = ${d}.', 'Write that change out of the start, ${a}, as a number out of 100.', 'The increase is {ans} percent.']),
        oracle=lambda e: dict(f1=pct_of_whole(e['d'], e['a']))),
    'A2d': dict(
        base=dict(n=3),
        tpl=dict(vars=dict(n=[1, 3, 4, 9]), derive=dict(m='n+1'),
                 q='A box of cereal costs $15. A shop’s deal is “Buy {n}, get 1 free!” For {m} boxes, the deal is really how many percent off? (Type just the number.)', frame='{f1}% off', answers=dict(f1='100 / (n + 1)'),
                 hint='How many dollars does the deal save on the {m} boxes? Write that as a part of the usual price of all those boxes.',
                 steps=['The free box saves $15. The usual price of all the boxes is {m} × $15.', 'Write the saving out of that price as a number out of 100.', 'The deal is {ans} percent off.']),
        oracle=lambda e: dict(f1=_o_a2d(e))),
    'A4': dict(
        base=dict(P=250, d=12),
        tpl=dict(vars=dict(P=[150, 200, 250, 300, 400], d=[8, 12, 20]),
                 q='A ${P} bicycle is sold at a {d}% discount. How much money is saved? What is the sale price? (Type the number of dollars.)', frame='Saved: $ {f1}     Sale price: $ {f2}',
                 answers=dict(f1='P * d / 100', f2='P - P * d / 100'), hint='Find {d}% of ${P}. That is the saving. Take it off the price.',
                 steps=['Find {d}% of ${P}: build it from 10% and 1%.', 'Take the saving off ${P} for the sale price.', 'The two amounts are {ans}.']),
        oracle=_o_a4),
    'B1b': dict(
        base=dict(T=109),
        tpl=dict(vars=dict(T=[109, 218, 327, 436, 545]),
                 q='A price tag says ${T}, GST included. GST is 9%. How much GST is in the price? (Type the number of dollars.)', frame='GST: $ {f1}', answers=dict(f1='T / 109 * 9'),
                 hint='The GST is 9% of the price before GST. ${T} is that price plus the GST: what percentage of the price before GST is ${T}?',
                 steps=['${T} is 109% of the price before GST.', 'Find 1% of the price before GST, then the price before GST, then 9% of it.', 'The GST is ${ans}.']),
        oracle=lambda e: dict(f1=whole(pct(price_before_gst(e['T']), 9)))),
    'B3': dict(
        base=dict(R=54, p1=40, p2=25),
        tpl=dict(vars=dict(R=[54, 72, 90, 126], p1=[20, 40], p2=[25, 50]),
                 q='Mrs Tan spent {p1}% of her money on groceries and {p2}% of the remaining money on a gift. She had ${R} left. How much money did she have at first? (Type the number of dollars.)',
                 answer='R * 10000 / ((100 - p1) * (100 - p2))', hint='Work backwards. ${R} is what percentage of the money she had before buying the gift?',
                 steps=['The gift took {p2}% of the money before it, so ${R} is the rest of that money.', 'Find the money before the gift, then the money at first, working backwards one step at a time.', 'Mrs Tan had ${ans} at first.']),
        oracle=lambda e: money_at_first(e['R'], e['p1'], e['p2'])),
}


polish(ITEMS, VARIANTS)
