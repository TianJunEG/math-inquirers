"""Level 2 (P2) holiday lesson 6: MARKET DAY (Money), week 3, second lesson.  Online mirror of the printed workbook pages.

The questions are the ones printed in the Level 2 holiday workbook (p2/content/l6.js `workbook()` = Start here, p2/gaps.json lesson 6 `invest` = Investigation,
p2/content/l6.js `qbank.stretch` first four = Think harder 1 to 4, `qbank.challenge` last three = Go further 5 to 7, as built by p2/workbook_html.js, and the
"Make up your own" line).  Every answer is recomputed by an INDEPENDENT checker: the fewest pieces of money by counting up from 0 (dynamic programming) and every way
listed by trying every combination (no "biggest first" rule); stories by trying numbers until the story comes out right.  build_holiday.py stops if a checker
and the printed answer differ.  Figures: price tags, the two change number lines, the bar of Mei's money, the half-money bar and the sticker/eraser prices, all redrawn
for a phone.  No coin or note pictures: the coins and notes are listed in plain text.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from hlib import *          # noqa: E402,F401
from p2lib import *         # noqa: E402,F401

STRAND = 'Money'
META = dict(level=2, lesson=6, key='p2', title='Market Day', workbook_title='MARKET DAY', topic='Money', strand=STRAND,
            sources=['p2/content/l6.js', 'p2/gaps.json', 'p2/workbook_html.js'],
            intro=['Coins: 5¢, 10¢, 20¢, 50¢, $1. Notes: $2, $5, $10, $50, $100. There is no $20 note. 100¢ = $1. Careful: 50¢ is a coin, $50 is a note.',
                   'Type just the number when a box asks for cents (35, not 35¢). Type numbers with a comma between them when a question asks for a list. Some questions ask you to explain: write your idea in the box, then read the worked solution after you submit and compare.'])

ALL = COINS + NOTES


def one(lst, what):
    if len(lst) != 1:
        raise ValueError(f'{what}: {len(lst)} answers, expected exactly 1')
    return lst[0]


def pieces_of(cents, dens=ALL):
    return fewest_pieces(cents, dens)[0]


def the_way(cents, dens=ALL):
    """The one way that uses the fewest pieces (biggest piece first)."""
    return one(fewest_pieces(cents, dens)[1], f'fewest-piece way for {cents}')


def say(way):
    return ' + '.join(money_name(c) for c in way)


TAG_PRICES = [9, 3, 14, 8]            # book, pen, bag, cap


def pairs_costing(total):
    """Every pair of DIFFERENT things on the tags that costs `total` dollars, each pair smaller price first, pairs in order of their smaller price."""
    out = [tuple(sorted((a, b))) for a, b in itertools.combinations(TAG_PRICES, 2) if a + b == total]
    return sorted(out)


def three_kinds(total_cents):
    """Every way to pay `total` with $5 notes, $2 notes and $1 coins, as (fives, twos, ones), most $5 notes first, then most $2 notes (all combinations tried)."""
    out = [(a, b, c) for a in range(0, total_cents // 500 + 1) for b in range(0, total_cents // 200 + 1) for c in range(0, total_cents // 100 + 1) if a * 500 + b * 200 + c * 100 == total_cents]
    return sorted(out, key=lambda w: (-w[0], -w[1]))


WAYS8 = three_kinds(800)
FOUR_PIECES = [w for w in WAYS8 if sum(w) == 4]

MONEY = money_list_fig()
CHANGE_A = count_line(65, 100, 5, 5, fmt='{}¢', caption='Count up from 65¢ to $1 (100¢)')
CHANGE_B = count_line(26, 50, 4, 1, fmt='${}', caption='Count up from $26 to $50')
TAGS = tags_fig([('Book', '$9'), ('Pen', '$3'), ('Bag', '$14'), ('Cap', '$8')])
MEI_BAR = bar_fig([dict(label='Mei', segs=[(1.6, '45¢', 'a'), (1.2, '30¢', 'b'), (1.0, '25¢ left', 'w')], brace=(0, 3.8, '? at first', 'bottom'))], label_w=50, row_h=40,
                  caption='A bar for Mei’s money: 45 cents spent on a sweet, 30 cents spent on a pencil, 25 cents left, and ? at first')
STICKERS = price_chips([('Sticker', '20¢ each'), ('Eraser', '50¢ each')], 'A sticker costs 20 cents and an eraser costs 50 cents')
KITE_BAR = bar_fig([dict(label='Ben’s\nmoney', segs=[(2, 'kite (half)', 'a'), (0.8, '$4', 'h'), (1.2, '$6 left', 'b')], brace=(0, 4, '? at first', 'top'))], label_w=70, row_h=38,
                   caption='A bar for Ben’s money cut in half: the first half is the kite, then $4 for a ball and $6 left, and ? at first')

ROWS = [('a', 'Curry puff', 165, '$1.65'), ('b', 'Notebook', 430, '$4.30'), ('c', 'Umbrella', 1875, '$18.75'), ('d', 'Bicycle', 7600, '$76')]
Q1_STEPS = {
    'a': ['$1.65 is $1 and 65¢.', '65¢ is 50¢ + 10¢ + 5¢, so the fewest pieces are $1, 50¢, 10¢ and 5¢.', 'That is 4 pieces of money.'],
    'b': ['$4.30 is $4 and 30¢. $4 is $2 + $2 (there is no $4 note).', '30¢ is 20¢ + 10¢, so the fewest pieces are $2, $2, 20¢ and 10¢.', 'That is 4 pieces of money.'],
    'c': ['$18.75 is $18 and 75¢. $18 is $10 + $5 + $2 + $1 (4 pieces).', '75¢ is 50¢ + 20¢ + 5¢ (3 pieces).', 'Together: $10, $5, $2, $1, 50¢, 20¢ and 5¢, which is 7 pieces of money.'],
    'd': ['$76 is $50 and $26. There is no $20 note, so $26 is $10 + $10 + $5 + $1.', 'The fewest pieces are $50, $10, $10, $5 and $1.', 'That is 5 pieces of money.'],
}
Q1_HINT = {'a': 'Start with the biggest note or coin that is not more than $1.65. What is left to pay? Then do it again.',
           'b': 'Start with the biggest note or coin that is not more than $4.30. What is left to pay? Then do it again.',
           'c': 'Pay the dollars first, then the cents. Use the biggest note or coin that fits each time. What is left to pay?',
           'd': 'Start with the biggest note that is not more than $76. What is left to pay? Remember there is no $20 note.'}

SETS4 = sorted({w for w in all_multisets(100, [5, 10, 20, 50], max_pieces=4) if len(w) == 4}, reverse=True)
EX_SETS = ', '.join(say(w) for w in SETS4)

ITEMS = []
for _k, _name, _c, _price in ROWS:
    ITEMS.append(dict(id=f'1{_k}l', tier='core', no=f'1({_k}) notes and coins', label=f'1({_k}) list', type='selfcheck', open=False, skill='paying exactly with the fewest pieces',
                      q=f'Pay exactly {_price} for the {_name.lower()} with the FEWEST notes and coins you can. Write the notes and coins you use in the box.', svg=MONEY,
                      facts=dict(pieces=pieces_of(_c), way=[money_name(x) for x in the_way(_c)]),
                      check=lambda c=_c: dict(pieces=pieces_of(c), way=[money_name(x) for x in the_way(c)]),
                      hint=Q1_HINT[_k], steps=Q1_STEPS[_k] + ['Check: ' + say(the_way(_c)) + ' makes ' + _price + '.'],
                      src=['Pay exactly. Use the FEWEST notes and coins you can.', _name, _price]))
    ITEMS.append(dict(id=f'1{_k}', tier='core', no=f'1({_k}) pieces', label=f'1({_k})', type='number', skill='paying exactly with the fewest pieces', answer=pieces_of(_c),
                      q=f'Pay exactly {_price} for the {_name.lower()} with the FEWEST notes and coins you can. How many pieces of money is that?', svg=MONEY,
                      check=lambda c=_c: pieces_of(c),
                      hint='Work out which notes and coins you would use, on paper if you like. Then count them.', steps=Q1_STEPS[_k],
                      src=['Pay exactly. Use the FEWEST notes and coins you can.', _name, _price]))
# the "pieces" card of each row first is printed order (notes and coins, then pieces): the list cards are already placed before their number card above

ITEMS += [
    dict(id='2a', tier='core', no='2(a)', type='number', skill='listing every way in order', answer=7,
         q='Find EVERY way to pay exactly $8 using $5 notes, $2 notes and $1 coins. Make a list in order: start with the most $5 notes. How many ways are there?',
         check=lambda: len(three_kinds(800)),
         hint='List the ways in order. First all the ways with one $5 note, then all the ways with no $5 note.',
         steps=['One $5 note leaves $3: that is $2 + $1, or three $1 coins. 2 ways.', 'No $5 note: use 4, 3, 2, 1 or 0 $2 notes and fill up with $1 coins. 5 ways.', '2 + 5 = 7 ways.'],
         src=['Find EVERY way to pay exactly $8 using $5 notes, $2 notes and $1 coins.', 'How many ways are there?']),
    dict(id='2list', tier='core', no='2 pieces altogether', label='2 list', type='set', ordered=True, skill='listing every way in order', answer=[3, 4, 4, 5, 6, 7, 8],
         q='List every way to pay exactly $8 with $5 notes, $2 notes and $1 coins. Put the ways in order: most $5 notes first, then most $2 notes. '
           'Type the pieces altogether (notes and coins) for each way.',
         check=lambda: [sum(w) for w in three_kinds(800)],
         hint='Write the ways as three numbers: how many $5, how many $2, how many $1. Then add the three numbers.',
         steps=['The ways ($5, $2, $1): 1, 1, 1 / 1, 0, 3 / 0, 4, 0 / 0, 3, 2 / 0, 2, 4 / 0, 1, 6 / 0, 0, 8.', 'Pieces altogether for each way: 3, 4, 4, 5, 6, 7, 8.'],
         src=['Find EVERY way to pay exactly $8 using $5 notes, $2 notes and $1 coins. Make a list in order: start with the most $5 notes.', 'Pieces altogether']),
    dict(id='2b', tier='core', no='2(b)', type='fields', skill='listing every way in order', answer=[1, 0, 3, 0, 4, 0],
         q='Paying exactly $8 with $5 notes, $2 notes and $1 coins: find the two ways that use the same number of pieces of money. Put the way with more $5 notes first.',
         frame='Way 1: {f1} $5 notes, {f2} $2 notes, {f3} $1 coins. Way 2: {f4} $5 notes, {f5} $2 notes, {f6} $1 coins.',
         check=lambda: [x for w in FOUR_PIECES for x in w] if len(FOUR_PIECES) == 2 else None,
         hint='Write each way and count its pieces. Which two ways have the same number of pieces?',
         steps=['Pieces for each way: 3, 4, 4, 5, 6, 7, 8. Two ways have 4 pieces.', 'One $5 note and three $1 coins: $5 + $1 + $1 + $1 = $8, 4 pieces.', 'Four $2 notes: $2 + $2 + $2 + $2 = $8, 4 pieces.'],
         src=['Two ways use exactly 4 pieces of money. What are they?']),

    dict(id='3a', tier='core', no='3(a)', type='text', skill='change by counting up', accept=money_accept(35), shown='35¢',
         q='Mei buys an eraser for 65¢. She pays with a $1 coin. How much change does she get? Type the number of cents.', svg=CHANGE_A,
         check=lambda: f'{100 - 65}¢',
         hint='Count up from 65¢ to $1, like a shopkeeper, in hops you choose.',
         steps=['Count up from 65¢ to 70¢: 5¢. Then from 70¢ to $1: 30¢.', '5¢ + 30¢ = 35¢. Check: 100¢ − 65¢ = 35¢.', 'Mei gets 35¢ change.'],
         src=['Mei buys an eraser for 65¢. She pays with a $1 coin. How much change does she get?']),
    dict(id='3b', tier='core', no='3(b)', type='number', skill='change by counting up', answer=24, unit=True,
         q='Ali buys a game for $26. He pays with a $50 note. How much change does he get?', svg=CHANGE_B,
         check=lambda: (5000 - 2600) // 100,
         hint='Count up from $26 to $50 in hops. Add up the hops.',
         steps=['Count up from $26 to $30: $4. Then from $30 to $50: $20.', '$4 + $20 = $24. Check: $50 − $26 = $24.', 'Ali gets $24 change.'],
         src=['Ali buys a game for $26. He pays with a $50 note. How much change does he get?']),
    dict(id='3bn', tier='core', no='3(b) notes', label='3(b) notes', type='fields', skill='paying with the fewest notes', answer=[2, 0, 2],
         q='Ali buys a game for $26 and pays with a $50 note. Which notes give his change with the fewest notes? Type how many of each (notes only).', svg=MONEY,
         frame='$10 notes: {f1}  $5 notes: {f2}  $2 notes: {f3}',
         check=lambda: (lambda w: [w.count(1000), w.count(500), w.count(200)])(the_way(5000 - 2600, NOTES)),
         hint='First find the change. Then use the biggest note that fits, and see what is left. Remember there is no $20 note.',
         steps=['The change is $50 − $26 = $24.', 'Two $10 notes make $20. The last $4 is $2 + $2.', 'The fewest notes are $10, $10, $2 and $2: 4 notes.'],
         src=['Which notes give this change with the fewest notes?']),

    dict(id='4a', tier='core', no='4(a)', type='choice', options=['Yes', 'No'], answer='No', skill='is there enough money?',
         q='Siti has $20 to spend. Can Siti buy the bag and the cap?', svg=TAGS,
         check=lambda: 'Yes' if 14 + 8 <= 20 else 'No',
         hint='Add the price of the bag and the price of the cap. Compare with $20.',
         steps=['The bag costs $14 and the cap costs $8: $14 + $8 = $22.', 'Siti has $20, and $22 is more than $20. She is $2 short.', 'No, she cannot buy both.'],
         src=['Siti has $20 to spend.', 'Can Siti buy the bag and the cap? Explain.']),
    dict(id='4w', tier='core', no='4(a) explain', label='4(a) why', type='selfcheck', open=False, skill='is there enough money?',
         q='Explain how you know whether Siti can buy the bag and the cap with her $20. Write your idea in the box.', svg=TAGS,
         facts=dict(total=22, money=20, short=2), check=lambda: dict(total=14 + 8, money=20, short=14 + 8 - 20),
         hint='Use the prices on the tags. What do the two things cost together?',
         steps=['The bag and the cap cost $14 + $8 = $22 together.', 'Siti has $20, so she is $22 − $20 = $2 short.', 'Any answer that adds the two prices and compares with $20 is a good one.'],
         src=['Can Siti buy the bag and the cap? Explain.']),
    dict(id='4b', tier='core', no='4(b)', type='set', ordered=True, skill='finding all the pairs', answer=[3, 14, 8, 9],
         q='Siti has $20. She buys two different things and gets exactly $3 change. Find ALL the pairs she could buy. Type the prices of each pair, smaller price first, one pair after another. '
           'Start with the pair that has the smaller first price.', svg=TAGS,
         check=lambda: [x for pr in pairs_costing(17) for x in pr],
         hint='How much does Siti spend in all? Which two prices on the tags make that?',
         steps=['Siti spends $20 − $3 = $17.', '$9 + $8 = $17 (book and cap). $14 + $3 = $17 (bag and pen).', 'The other pairs cost $12, $23, $11 and $22, so these are the only two pairs. In order: 3, 14, then 8, 9.'],
         src=['Siti buys two different things and gets exactly $3 change. Find ALL the pairs she could buy.']),

    dict(id='5', tier='core', no='5(a)', type='text', skill='working backwards with money', accept=money_accept(100), shown='$1.00',
         q='Mei spent 45¢ on a sweet and 30¢ on a pencil. She has 25¢ left. How much money did she have at first? Write it in dollars and cents.', svg=MEI_BAR,
         check=lambda: '$1.00' if one([x for x in range(0, 1000) if x - 45 - 30 == 25], 'Mei at first') == 100 else None,
         hint='Add back what she spent to the money she has left. Then write the total in dollars and cents.',
         steps=['She spent 45¢ + 30¢ = 75¢.', '75¢ spent + 25¢ left = 100¢ at first.', '100¢ is $1.00.'],
         src=['Mei spent 45¢ on a sweet and 30¢ on a pencil. She has 25¢ left. How much money did she have at first? Write it in dollars and cents.']),

    dict(id='6a', tier='core', no='6(a) stickers', label='6 stickers', type='set', ordered=True, skill='finding all the ways', answer=[10, 5, 0],
         q='Stickers cost 20¢ each. Erasers cost 50¢ each. Siti spends exactly $2. Find ALL the ways (she might buy only one kind). Put the ways in order, most stickers first. '
           'Type the number of stickers in each way.', svg=STICKERS,
         check=lambda: [s for s, e in sorted(((s, e) for s in range(0, 11) for e in range(0, 5) if 20 * s + 50 * e == 200), reverse=True)],
         hint='Try 0 erasers, then 1 eraser, then 2 ... How much is left each time? Can the 20¢ stickers make it exactly?',
         steps=['She spends 200¢. Try the number of erasers: 0 erasers leaves 200¢ = 10 stickers. 1 eraser leaves 150¢, which 20¢ stickers cannot make exactly.',
                '2 erasers leave 100¢ = 5 stickers. 3 erasers leave 50¢, which stickers cannot make. 4 erasers leave 0¢ = 0 stickers.', 'The ways (stickers, erasers) are 10 and 0, 5 and 2, 0 and 4. Stickers, most first: 10, 5, 0.'],
         src=['Stickers cost 20¢ each. Erasers cost 50¢ each. Siti spends exactly $2.', 'Find ALL the ways.']),
    dict(id='6b', tier='core', no='6(b) erasers', label='6 erasers', type='set', ordered=True, skill='finding all the ways', answer=[0, 2, 4],
         q='Stickers cost 20¢ each. Erasers cost 50¢ each. Siti spends exactly $2 (she might buy only one kind). Put all the ways in order, most stickers first. Type the number of erasers in each way.', svg=STICKERS,
         check=lambda: [e for s, e in sorted(((s, e) for s in range(0, 11) for e in range(0, 5) if 20 * s + 50 * e == 200), reverse=True)],
         hint='For each way, how many 50¢ erasers go with the stickers?',
         steps=['The ways (stickers, erasers) are 10 and 0, 5 and 2, 0 and 4.', 'With the most stickers first, the erasers are 0, 2, 4.', 'Check: 5 stickers and 2 erasers cost 100¢ + 100¢ = 200¢ = $2.'],
         src=['How many stickers and erasers could she buy?']),

    # ================= Investigation: Most coins
    dict(id='I1', tier='invest', no='Investigation (a)', label='Inv 1', type='number', skill='fewest coins', answer=3,
         q='Use only 5¢, 10¢, 20¢ and 50¢ coins. Pay 35¢ using the fewest coins. How many coins is that?',
         check=lambda: pieces_of(35, [5, 10, 20, 50]),
         hint='Easy first step: pay 35¢ with the biggest coin that fits, then see what is left.',
         steps=['35¢ = 20¢ + 10¢ + 5¢.', 'That is 3 coins, and no 2 coins make 35¢.'],
         src=['Pay 35¢ using the fewest coins. How many coins is that?', 'Use only 5¢, 10¢, 20¢ and 50¢ coins.']),
    dict(id='I2', tier='invest', no='Investigation (b) 5¢ to 30¢', label='Inv 2', type='set', ordered=True, skill='fewest coins',
         answer=[1, 1, 2, 1, 2, 2],
         q='Use only 5¢, 10¢, 20¢ and 50¢ coins. Make a table of how many coins each amount needs (use the fewest). Type the fewest coins for 5¢, 10¢, 15¢, 20¢, 25¢ and 30¢.',
         check=lambda: [pieces_of(a, [5, 10, 20, 50]) for a in range(5, 31, 5)],
         hint='Do each amount in turn. Use the biggest coin that fits, then see what is left.',
         steps=['5¢: 1 coin. 10¢: 1 coin. 15¢ = 10¢ + 5¢: 2 coins.', '20¢: 1 coin. 25¢ = 20¢ + 5¢: 2 coins. 30¢ = 20¢ + 10¢: 2 coins.', 'The fewest coins are 1, 1, 2, 1, 2, 2.'],
         src=['Try the other amounts from 5¢ to 95¢ (in steps of 5¢) and make a table of how many coins each needs.']),
    dict(id='I3', tier='invest', no='Investigation (b) 35¢ to 60¢', label='Inv 3', type='set', ordered=True, skill='fewest coins',
         answer=[3, 2, 3, 1, 2, 2],
         q='Use only 5¢, 10¢, 20¢ and 50¢ coins. Type the fewest coins for 35¢, 40¢, 45¢, 50¢, 55¢ and 60¢.',
         check=lambda: [pieces_of(a, [5, 10, 20, 50]) for a in range(35, 61, 5)],
         hint='Do each amount in turn. For 55¢ and 60¢, which coin is the biggest you can use?',
         steps=['35¢ = 20¢ + 10¢ + 5¢: 3 coins. 40¢ = 20¢ + 20¢: 2 coins. 45¢ = 20¢ + 20¢ + 5¢: 3 coins.', '50¢: 1 coin. 55¢ = 50¢ + 5¢: 2 coins. 60¢ = 50¢ + 10¢: 2 coins.', 'The fewest coins are 3, 2, 3, 1, 2, 2.'],
         src=['Try the other amounts from 5¢ to 95¢ (in steps of 5¢) and make a table of how many coins each needs.']),
    dict(id='I4', tier='invest', no='Investigation (b) 65¢ to 95¢', label='Inv 4', type='set', ordered=True, skill='fewest coins',
         answer=[3, 2, 3, 3, 4, 3, 4],
         q='Use only 5¢, 10¢, 20¢ and 50¢ coins. Type the fewest coins for 65¢, 70¢, 75¢, 80¢, 85¢, 90¢ and 95¢.',
         check=lambda: [pieces_of(a, [5, 10, 20, 50]) for a in range(65, 96, 5)],
         hint='Do each amount in turn. Start each one with the 50¢ coin, then see what is left.',
         steps=['65¢ = 50¢ + 10¢ + 5¢: 3 coins. 70¢ = 50¢ + 20¢: 2 coins. 75¢ = 50¢ + 20¢ + 5¢: 3 coins.', '80¢ = 50¢ + 20¢ + 10¢: 3 coins. 85¢ = 50¢ + 20¢ + 10¢ + 5¢: 4 coins.',
                '90¢ = 50¢ + 20¢ + 20¢: 3 coins. 95¢ = 50¢ + 20¢ + 20¢ + 5¢: 4 coins.', 'The fewest coins are 3, 2, 3, 3, 4, 3, 4.'],
         src=['Try the other amounts from 5¢ to 95¢ (in steps of 5¢) and make a table of how many coins each needs.']),
    dict(id='I5', tier='invest', no='Investigation (c)', label='Inv 5', type='set', ordered=False, skill='fewest coins', answer=[85, 95],
         q='Use only 5¢, 10¢, 20¢ and 50¢ coins. Look at the amounts from 5¢ to 95¢. Which amounts need the MOST coins, even when you use the fewest possible? '
           'Type the amounts in cents, with a comma between.',
         check=lambda: (lambda t: [a for a, n in t if n == max(n for _, n in t)])([(a, pieces_of(a, [5, 10, 20, 50])) for a in range(5, 96, 5)]),
         hint='Look at your table of the fewest coins. Which amounts have the biggest number?',
         steps=['The most coins needed is 4. That is for 85¢ and 95¢.', '85¢ = 50¢ + 20¢ + 10¢ + 5¢ and 95¢ = 50¢ + 20¢ + 20¢ + 5¢.', 'No amount from 5¢ to 95¢ needs 5 coins.'],
         src=['Which amount needs the MOST coins, even when you use the fewest possible?']),

    # ================= Think harder
    dict(id='T1', tier='stretch', no='Think harder 1', label='T1', type='number', skill='working backwards with halves', answer=20, unit=True,
         q='Ben spent half of his money on a kite. Then he spent $4 on a ball. He had $6 left. How much money did Ben have at first? Tip: draw his money as a bar cut in half.', svg=KITE_BAR,
         check=lambda: one([x for x in range(2, 1000, 2) if x - x // 2 - 4 == 6], 'Ben at first'),
         hint='Start from the $6 left. Put back what he spent on the ball. What does that amount stand for in the bar?',
         steps=['After the kite, Ben still had $4 + $6 = $10. That is the other half of his money.', 'The half he spent on the kite is also $10.', '$10 + $10 = $20. Check: half of $20 is $10 for the kite, $10 − $4 = $6 left.'],
         src=['Ben spent half of his money on a kite. Then he spent $4 on a ball. He had $6 left. How much money did Ben have at first? Tip: draw his money as a bar cut in half.']),
    dict(id='T2', tier='stretch', no='Think harder 2', label='T2', type='number', skill='listing every way in order', answer=10,
         q='How many ways can you pay exactly $10 using $5 notes, $2 notes and $1 coins?',
         check=lambda: len(three_kinds(1000)),
         hint='Make a list in order, like in Start here 2. Start with the most $5 notes.',
         steps=['Two $5 notes make $10 with nothing left: 1 way.', 'One $5 note leaves $5: use 0, 1 or 2 $2 notes and fill up with $1 coins: 3 ways.', 'No $5 note: use 0, 1, 2, 3, 4 or 5 $2 notes and fill up with $1 coins: 6 ways. 1 + 3 + 6 = 10 ways.'],
         src=['How many ways can you pay exactly $10 using $5 notes, $2 notes and $1 coins?']),
    dict(id='T3', tier='stretch', no='Think harder 3', label='T3', type='set', ordered=True, skill='finding all the sets of coins', answer=[100, 10, 10, 5, 50, 50, 20, 5],
         q='Ali has 4 coins. They are worth $1.25 altogether. Find ALL the sets of 4 coins he could have. Type each set as 4 numbers in cents (a $1 coin is 100), biggest coin first. '
           'Put the set with the biggest coin first.',
         check=lambda: [x for w in sorted({w for w in all_multisets(125, COINS, max_pieces=4) if len(w) == 4}, reverse=True) for x in w],
         hint='Try the biggest coin first. What is left, and can 3 coins make it?',
         steps=['With a $1 coin, 25¢ is left for 3 coins: 10¢ + 10¢ + 5¢.', 'With no $1 coin, try two 50¢ coins: 25¢ is left for 2 coins: 20¢ + 5¢.',
                'The two sets are $1 + 10¢ + 10¢ + 5¢ and 50¢ + 50¢ + 20¢ + 5¢. In cents: 100, 10, 10, 5 and 50, 50, 20, 5. No other 4 coins make $1.25.'],
         src=['Ali has 4 coins. They are worth $1.25 altogether. Find all the sets of 4 coins he could have.']),
    dict(id='T4', tier='stretch', no='Think harder 4', label='T4', type='number', skill='listing every way in order', answer=9,
         q='How many different ways can you pay exactly 40¢ using 5¢, 10¢ and 20¢ coins? Make a list in order, starting with the most 20¢ coins.',
         check=lambda: len(all_multisets(40, [5, 10, 20])),
         hint='Start with two 20¢ coins. Then one 20¢ coin. Then none. How many ways does each give?',
         steps=['Two 20¢ coins: 1 way.', 'One 20¢ coin and 20¢ more from 10¢ and 5¢ coins (10 + 10, 10 + 5 + 5, or four 5¢): 3 ways.',
                'No 20¢ coin, 40¢ from 10¢ and 5¢ coins (four 10¢ down to none): 5 ways. 1 + 3 + 5 = 9 ways.'],
         src=['How many different ways can you pay exactly 40¢ using 5¢, 10¢ and 20¢ coins? Make a list in order, starting with the most 20¢ coins.']),

    # ================= Go further
    dict(id='C5', tier='challenge', no='Go further 5', label='G5', type='number', skill='working backwards with halves', answer=20, unit=True,
         q='Siti had some money. She spent half of it on a book. Then she spent half of what was left on a pen. She had $5 left. How much money did she have at first?',
         check=lambda: one([x for x in range(4, 1000, 4) if (x // 2) - (x // 2) // 2 == 5], 'Siti at first'),
         hint='Draw a bar for her money. Go backwards from the $5 left: the pen took half of what was left after the book.',
         steps=['The pen took half of what was left after the book. So the $5 she has left is the other half.', 'After the book she had $5 + $5 = $10. The book took half of all her money, so she spent $10 on the book too.', '$10 + $10 = $20. Check: half of $20 is $10 on the book, half of $10 is $5 on the pen, and $5 is left.'],
         src=['Siti had some money. She spent half of it on a book. Then she spent half of what was left on a pen. She had $5 left. How much money did she have at first?']),
    dict(id='C6a', tier='challenge', no='Go further 6 (Mei)', label='G6a', type='choice', options=['Yes', 'No'], answer='Yes', skill='all the amounts you can make',
         q='Sweets cost 5¢ and lollipops cost 20¢. Ben buys 8 things, at least one of each kind. Mei says he spent $1.00. Could she be right?',
         check=lambda: 'Yes' if any(5 * s + 20 * l == 100 for s in range(1, 8) for l in range(1, 8) if s + l == 8) else 'No',
         hint='Try some numbers of sweets and lollipops that make 8 things. How much does each try cost?',
         steps=['Try 4 sweets and 4 lollipops: 4 × 5¢ = 20¢ and 4 × 20¢ = 80¢.', '20¢ + 80¢ = 100¢ = $1.00.', 'So Mei could be right.'],
         src=['Sweets cost 5¢ and lollipops cost 20¢. Ben buys 8 things, at least one of each kind. Mei says he spent $1.00.']),
    dict(id='C6b', tier='challenge', no='Go further 6 (Siti)', label='G6b', type='choice', options=['Yes', 'No'], answer='No', skill='all the amounts you can make',
         q='Sweets cost 5¢ and lollipops cost 20¢. Ben buys 8 things, at least one of each kind. Siti says he spent $1.50. Could she be right?',
         check=lambda: 'Yes' if any(5 * s + 20 * l == 150 for s in range(1, 8) for l in range(1, 8) if s + l == 8) else 'No',
         hint='Try some numbers of sweets and lollipops that make 8 things. Can any of them cost $1.50?',
         steps=['The most Ben can spend is with 7 lollipops and 1 sweet: 7 × 20¢ + 5¢ = 145¢.', '$1.50 is 150¢, which is more than 145¢.', 'So Siti cannot be right.'],
         src=['Siti says he spent $1.50. Could either of them be right?']),
    dict(id='C6c', tier='challenge', no='Go further 6 (amounts)', label='G6c', type='set', ordered=False, skill='all the amounts you can make', answer=[55, 70, 85, 100, 115, 130, 145],
         q='Sweets cost 5¢ and lollipops cost 20¢. Ben buys 8 things, at least one of each kind. Find ALL the amounts Ben could have spent. Type the amounts in cents, with a comma between.',
         check=lambda: sorted(5 * s + 20 * l for s in range(1, 8) for l in range(1, 8) if s + l == 8),
         hint='Try 1 lollipop and 7 sweets. Then 2 lollipops and 6 sweets. Keep going. What does each try cost?',
         steps=['1 lollipop and 7 sweets: 20¢ + 35¢ = 55¢. 2 and 6: 40¢ + 30¢ = 70¢. 3 and 5: 60¢ + 25¢ = 85¢.', '4 and 4: 80¢ + 20¢ = 100¢. 5 and 3: 100¢ + 15¢ = 115¢. 6 and 2: 120¢ + 10¢ = 130¢. 7 and 1: 140¢ + 5¢ = 145¢.', 'The amounts are 55, 70, 85, 100, 115, 130 and 145 cents.'],
         src=['Find ALL the amounts Ben could have spent.']),
    dict(id='C6d', tier='challenge', no='Go further 6 (notice)', label='G6d', type='selfcheck', open=False, skill='all the amounts you can make',
         q='Sweets cost 5¢ and lollipops cost 20¢. Ben buys 8 things, at least one of each kind. What do you notice about the amounts he could have spent, and why? Write your idea in the box.',
         facts=dict(go_up_by=15, how_many=7),
         check=lambda: (lambda a: dict(go_up_by=one(sorted({y - x for x, y in zip(a, a[1:])}), 'step'), how_many=len(a)))(sorted(5 * s + 20 * l for s in range(1, 8) for l in range(1, 8) if s + l == 8)),
         hint='Look at how far apart the amounts are. What changes when you swap one sweet for one lollipop?',
         steps=['The amounts go up by 15¢ each time: 55¢, 70¢, 85¢ ...', 'Swapping one sweet for one lollipop makes the cost 20¢ − 5¢ = 15¢ more.', 'Any answer that talks about the jumps of 15¢ is a good one.'],
         src=['What do you notice about the amounts, and why?']),
    dict(id='C7', tier='challenge', no='Go further 7', label='G7', type='number', skill='counting all the amounts', answer=15,
         q='Mei has one $10 note, one $5 note, one $2 note and one $1 coin. How many different amounts can she pay exactly, using one or more of them?',
         check=lambda: len({sum(c for k, c in zip(mask, (10, 5, 2, 1)) if k) for mask in itertools.product((0, 1), repeat=4) if any(mask)}),
         hint='Make a list in order: use the $10 note or not, then the $5 note or not, and so on. Add each one up.',
         steps=['The amounts, in order: $1, $2, $3, $5, $6, $7, $8, $10, $11, $12, $13, $15, $16, $17, $18.', 'All 15 are different, and they use each choice of one or more pieces once.', 'Mei can pay 15 different amounts.'],
         src=['Mei has one $10 note, one $5 note, one $2 note and one $1 coin. How many different amounts can she pay exactly, using one or more of them?']),
    dict(id='M', tier='challenge', no='Make up your own', label='Make', type='selfcheck', open=True, marking_mode='open', skill='making puzzles',
         q='Make a coin puzzle about paying exactly $1. Solve it, then swap with a partner.',
         hint='Pick the coins you may use and how many coins to use. Then list every way and check each one makes $1.',
         steps=['Many answers are right. Example: Ben pays exactly $1 using 4 coins from 5¢, 10¢, 20¢ and 50¢. Find all the sets.',
                'The sets are: ' + EX_SETS + '. Check each one adds to 100¢.', 'Swap with a partner. Do you both find the same sets?'],
         src=['a coin puzzle about paying exactly $1. Solve it, then swap with a partner.']),
]
for _d in ITEMS:
    _d.setdefault('strand', STRAND)


# ---------------------------------------------------------------- variant families (template + independent oracle over EVERY combination)
VARIANTS = {
    '3b': dict(
        base=dict(p=26),
        tpl=dict(vars=dict(p=[17, 23, 26, 31, 34, 38, 42, 45]), derive=dict(a='50-p'),
                 q='Ali buys a game for ${p}. He pays with a $50 note. How much change does he get?',
                 answer='50-p', hint='Count up from ${p} to $50 in hops. Add up the hops.',
                 steps=['Count up from ${p} to $50 in hops, or work out $50 − ${p}.', '$50 − ${p} = ${a}.', 'Ali gets ${ans} change.']),
        oracle=lambda e: (5000 - e['p'] * 100) // 100),
    'T1': dict(
        base=dict(b=4, l=6),
        tpl=dict(vars=dict(b=[2, 3, 4, 5, 6], l=[3, 4, 5, 6, 7, 8]), derive=dict(h='b+l'),
                 q='Ben spent half of his money on a kite. Then he spent ${b} on a ball. He had ${l} left. How much money did Ben have at first?',
                 answer='2*(b+l)', hint='Start from the ${l} left. Put back what he spent on the ball. What does that amount stand for in the bar?',
                 steps=['After the kite, Ben still had ${b} + ${l} = ${h}. That is the other half of his money.', 'The half he spent on the kite is also ${h}.', '${h} + ${h} = ${ans}.']),
        oracle=lambda e: one([x for x in range(2, 1000, 2) if x - x // 2 - e['b'] == e['l']], 'Ben at first')),
    'C5': dict(
        base=dict(k=5),
        tpl=dict(vars=dict(k=[2, 3, 4, 5, 6, 8, 10]), derive=dict(r='2*k'),
                 q='Siti had some money. She spent half of it on a book. Then she spent half of what was left on a pen. She had ${k} left. How much money did she have at first?',
                 answer='4*k', hint='Draw a bar for her money. Go backwards from the ${k} left: the pen took half of what was left after the book.',
                 steps=['The pen took half of what was left after the book, so the ${k} she has left is the other half.', 'After the book she had ${k} + ${k} = ${r}. The book took the other half of her money, so she spent ${r} on the book.', '${r} + ${r} = ${ans}.']),
        oracle=lambda e: one([x for x in range(4, 2000, 4) if (x // 2) - (x // 2) // 2 == e['k']], 'Siti at first')),
}

for _d in ITEMS:
    if _d['type'] == 'selfcheck':
        _d.setdefault('marking_mode', 'self')
