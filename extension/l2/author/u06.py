import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *

def money(*items, **kw):
    d = {'type': 'l2_money', 'items': list(items)}
    d.update(kw)
    return d

def tags(items, **kw):
    d = {'type': 'l2_tags', 'items': [{'name': n, 'price': p} for n, p in items]}
    d.update(kw)
    return d

learn = {
 'intro': 'Money is written in dollars and cents. $1 is 100¢, so $3.45 is 345¢. To pay exactly with the fewest pieces, take the greatest note or coin that fits, again and again.',
 'example': {
  'problem': 'A cake costs $4.35. Pay the exact amount with as few notes and coins as you can.',
  'figure': money('$2', '$2', '20¢', '10¢', '5¢', width_mm=112), 'side': False,
  'steps': ['Dollars first: $4 is $2 + $2. That is 2 notes.', 'Now the cents: 35¢. The greatest coin that fits is 20¢. 15¢ is left.', 'The greatest coin that fits 15¢ is 10¢. Then 5¢ is left: one 5¢ coin.', 'Check: 4.00 + 0.20 + 0.10 + 0.05 = 4.35. That is 5 pieces.'],
  'answer': '$2, $2, 20¢, 10¢ and 5¢. That is 5 pieces.'},
 'howto': {'title': 'How to pay exactly', 'steps': ['Split the cost into dollars and cents.', 'Take the greatest note or coin that fits.', 'Repeat with what is left.', 'Add to check. Count the pieces.']},
 'facts': {'title': 'Our money', 'lines': ['Coins: 5¢, 10¢, 20¢, 50¢, $1.', 'Notes: $2, $5, $10, $50, $100.', 'There is no $20 note.']},
 'try': {'text': 'Pay exactly $6.85 with as few notes and coins as you can. How many pieces? {b}', 'answer': A('6'),
         'explanation': '$6 is $5 + $1 (2 pieces). 85¢ is 50¢ + 20¢ + 10¢ + 5¢ (4 pieces). 2 + 4 = 6 pieces. Check: 5 + 1 + 0.50 + 0.20 + 0.10 + 0.05 = 6.85.'}}

items = [
 I('start', 1, 'Change dollars and cents.', partsrow=True, parts=[
   P('a', '$3.45 = {b} ¢', '345'), P('b', '275¢ = $ {b}', '2.75'), P('c', '6 dollars and 5 cents = $ {b}', '6.05'), P('d', '1 dollar and 30 cents = {b} ¢', '130')],
   why='$1 is 100¢. (a) 3 dollars is 300¢, and 300 + 45 = 345. (b) 275¢ is 2 dollars and 75 cents: $2.75. (c) 6 dollars and 5 cents is $6.05, not $6.50. (d) 100¢ + 30¢ = 130¢.'),
 I('start', 1, 'Count the money. How much is there altogether?', figure=money('$5', '$2', '$2', '$1', '50¢', '20¢', '10¢', width_mm=150),
   parts=[P('a', 'The total is $ {b}', '10.80')],
   why='Notes and $1: $5 + $2 + $2 + $1 = $10. Coins: 50¢ + 20¢ + 10¢ = 80¢. $10 + $0.80 = $10.80.'),
 I('start', 1, 'Pay the exact amount with as few notes and coins as you can. Write them on the lines. Then count the pieces.', figure=tags([('Marker pen', '$2.85'), ('Kite', '$7.40'), ('Backpack', '$23.65')], width_mm=150),
   partsrow=True, parts=[P('a', 'Marker pen: {b} pieces', '5'), P('b', 'Kite: {b} pieces', '4'), P('c', 'Backpack: {b} pieces', '7')],
   space={'rows': ['Marker pen:', 'Kite:', 'Backpack:']},
   why='Marker pen: $2 + 50¢ + 20¢ + 10¢ + 5¢ is 5 pieces. Kite: $5 + $2 + 20¢ + 20¢ is 4 pieces. Backpack: $10 + $10 + $2 + $1 + 50¢ + 10¢ + 5¢ is 7 pieces (there is no $20 note).'),
 I('start', 2, 'Find EVERY way to pay exactly $7 using $1 coins, $2 notes and $5 notes. Begin with as many $5 notes as you can. Write each way in a row. Some rows may stay empty.',
   figure={'type': 'l2_table', 'cols': ['Way', '$5', '$2', '$1', 'Pieces'], 'rows': [[c, None, None, None, None] for c in 'ABCDEFG'], 'first_bold': True, 'widths': [1, 1.2, 1.2, 1.2, 1.6], 'row_h': 56, 'head_h': 56, 'size': 32, 'width_mm': 132},
   parts=[P('a', 'How many ways are there? {b}', '6'), P('b', 'The way with exactly 4 pieces has {b} $2 notes and {b} $1 coins.', ['3', '1'], '3 $2 notes and 1 $1 coin')],
   why='Ways ($5, $2, $1): 1, 1, 0 / 1, 0, 2 / 0, 3, 1 / 0, 2, 3 / 0, 1, 5 / 0, 0, 7. That is 6 ways. Their pieces are 2, 3, 4, 5, 6 and 7. Only 0, 3, 1 has 4 pieces: three $2 notes and one $1 coin.'),
 I('start', 2, 'Find the change.', partsrow=True, parts=[
   P('a', 'A ruler costs 70¢. Kumar pays with a $1 coin. Change: {b} ¢', '30'), P('b', 'A book costs $4.30. Mei pays with a $10 note. Change: $ {b}', '5.70'), P('c', 'A bag costs $37. Ali pays with a $50 note. Change: $ {b}', '13'),
   P('d', 'The fewest notes and coins for the $13 change: {b} pieces', '3')],
   why='Change is what you pay minus the cost. (a) 100¢ - 70¢ = 30¢. (b) $10 - $4.30 = $5.70. Count on: $4.30 to $5 is 70¢, then $5 more makes $10. (c) $50 - $37 = $13. (d) $13 is $10 + $2 + $1: 3 pieces.'),
 I('start', 3, 'Ravi has $30.', figure=tags([('Shoes', '$17.50'), ('T-shirt', '$9.90'), ('Hat', '$4.60')], width_mm=140),
   parts=[P('a', 'The shoes and the T-shirt cost $ {b} together.', '27.40'), P('b', 'Can Ravi buy all 3 things? {circ:Yes|No}', 'No'), P('c', 'He needs $ {b} more to buy all 3.', '2.00')],
   why='(a) $17.50 + $9.90 = $27.40. (b) All 3 cost $27.40 + $4.60 = $32.00. Ravi has only $30, so no. (c) $32.00 - $30 = $2.00 more.'),
 I('start', 3, 'Aisha spent $3.50 on lunch and $1.25 on a drink. She has $4.75 left. At first she had $ {b}', value='9.50',
   why='Work backwards: put back what she spent. $4.75 + $1.25 = $6.00, and $6.00 + $3.50 = $9.50. Check: 9.50 - 3.50 = 6.00 and 6.00 - 1.25 = 4.75.'),
 I('start', 3, 'Shop deals.', partsrow=True, parts=[
   P('a', '4 pencils cost $1. 12 pencils cost $ {b}', '3'), P('b', '5 stickers cost $2. 20 stickers cost $ {b}', '8'), P('c', '$6 buys {b} stickers.', '15')],
   why='(a) 12 pencils is 3 groups of 4, so 3 × $1 = $3. (b) 20 stickers is 4 groups of 5, so 4 × $2 = $8. (c) $6 is 3 groups of $2, so 3 × 5 = 15 stickers.'),
 I('start', 3, 'Ali buys 2 toys for exactly $12.50. Which 2 toys? {b} and {b}', figure=tags([('Car', '$4.50'), ('Ball', '$6.25'), ('Top', '$8.00'), ('Kite', '$3.75')], width_mm=150), value=['Car', 'Top'], atext='Car and Top', unordered=True,
   why='$4.50 + $8.00 = $12.50. Check the others: Car + Ball = $10.75, Car + Kite = $8.25, Ball + Top = $14.25, Ball + Kite = $10.00, Top + Kite = $11.75. Only Car and Top.'),
 I('start', 3, 'Mei pays exactly 95¢ with 4 coins. Use 5¢, 10¢, 20¢ or 50¢ coins. Write the coins. {b}¢ + {b}¢ + {b}¢ + {b}¢', value=['50', '20', '20', '5'], atext='50¢ + 20¢ + 20¢ + 5¢ (any order)', unordered=True,
   why='Start with 50¢. 45¢ is left for 3 coins. 20¢ + 20¢ = 40¢, and 5¢ makes 45¢. Check: 50 + 20 + 20 + 5 = 95. No other 4 coins make 95¢.'),
 # Think harder
 I('think', 4, 'Pay 35¢ with 5¢, 10¢ and 20¢ coins. List EVERY way in the table.',
   space={'table': {'cols': ['20¢', '10¢', '5¢'], 'rows': 6}},
   parts=[P('a', 'How many ways are there? {b}', '6'), P('b', 'The 5-coin way: {b} coins of 10¢ and {b} of 5¢.', ['2', '3'], '2 coins of 10¢ and 3 coins of 5¢')],
   hint='Try 1 coin of 20¢ first. Then none. Fill the rest with 10¢ and 5¢.',
   why='With one 20¢: 15¢ is 10+5 or 5+5+5. With no 20¢: 35¢ is made of 10¢ and 5¢ coins. Ways (20, 10, 5): 1,1,1 / 1,0,3 / 0,3,1 / 0,2,3 / 0,1,5 / 0,0,7: 6 ways. Only 0, 2, 3 has 5 coins.'),
 I('think', 4, 'Lollipops cost 20¢ each. Cookies cost 50¢ each. Siti buys 7 things and spends exactly $2.60. How many lollipops and how many cookies?', parts=[
   P('a', 'Lollipops: {b}', '3'), P('b', 'Cookies: {b}', '4')],
   hint='Start with 7 lollipops. Swap one for a cookie each time.',
   why='7 lollipops cost $1.40. Each swap of a lollipop for a cookie adds 30¢: $1.70, $2.00, $2.30, $2.60. That is 4 swaps. So 3 lollipops and 4 cookies. Check: 60¢ + $2.00 = $2.60 and 3 + 4 = 7.'),
 I('think', 4, 'A book costs $4 more than a puzzle. Together they cost $13.',
   figure={'type': 'l2_bar', 'rows': [{'label': 'Puzzle', 'segs': [{'w': 5, 'unknown': True, 't': '?'}]}, {'label': 'Book', 'segs': [{'w': 5, 'unknown': True, 't': '?'}, {'w': 2, 't': '$4'}]}], 'brace': {'text': '$13', 'rows': [0, 1]}, 'width_units': 300, 'width_mm': 84},
   partsrow=True, parts=[P('a', 'The puzzle costs $ {b}', '4.50'), P('b', 'The book costs $ {b}', '8.50')],
   hint='Take away the extra $4. Share what is left equally.',
   why='Take away the extra $4: $13 - $4 = $9. Two equal bars share $9, so each is $4.50. The puzzle costs $4.50 and the book costs $4.50 + $4 = $8.50. Check: 4.50 + 8.50 = 13.00.'),
 # Go further
 I('go', 5, 'A shop sign says PAY HALF. You pay half of the amount on the tag.', beyond='Halving money', parts=[
   P('a', 'A ball has a tag of $9.60. You pay $ {b}', '4.80'), P('b', 'A hat has a tag of $14.50. You pay $ {b}', '7.25'), P('c', 'A kite costs $5.80 with PAY HALF. The tag says $ {b}', '11.60')],
   hint='Half of dollars first. Then half of cents. Go back with double.',
   why='(a) Half of $9.60 is $4.80. (b) Half of $14 is $7 and half of 50¢ is 25¢: $7.25. (c) The tag is double: $5.80 + $5.80 = $11.60.'),
 I('go', 5, 'Mei has 5 coins. Each coin is 20¢ or 50¢.', parts=[
   P('a', 'How many different amounts could she have? {b}', '6'), P('b', 'With exactly 3 coins of 50¢, she has $ {b}', '1.90'), P('c', 'Could she have $1.40? {circ:Yes|No}', 'No')],
   hint='Start with 5 coins of 20¢. Swap one for 50¢ each time.',
   why='5 coins of 20¢ is $1.00. Each swap of a 20¢ for a 50¢ adds 30¢: $1.00, $1.30, $1.60, $1.90, $2.20, $2.50. That is 6 amounts. (b) 3 coins of 50¢ and 2 of 20¢: $1.50 + $0.40 = $1.90. (c) $1.40 is not in the list: no.'),
 I('go', 5, 'Make your own coin riddle. Choose 3 coins from 5¢, 10¢, 20¢ and 50¢ (a coin can be used twice). Write how much they are worth, so that only ONE set of 3 coins fits. Many answers are right.', value='open',
   atext='Open. Example: 3 coins are worth 80¢. Only 50¢, 20¢ and 10¢ fit.', space={'rows': ['My riddle:']}, hint='Try all the sets of 3 coins. Does another set make the same total?',
   why='Example: 3 coins worth 80¢. The only set is 50¢ + 20¢ + 10¢. Any other 3 coins make a different total. A riddle is good if no other set fits.'),
 I('go', 5, 'Shop A sells 3 pens for $2. Shop B sells 4 pens for $3. Ben wants 12 pens.', parts=[
   P('a', 'At shop A, 12 pens cost $ {b}', '8'), P('b', 'At shop B, 12 pens cost $ {b}', '9'), P('c', 'Which shop is cheaper? {circ:A|B}', 'A')],
   hint='12 pens is how many groups of 3? Of 4?',
   why='(a) 12 pens is 4 groups of 3, so 4 × $2 = $8. (b) 12 pens is 3 groups of 4, so 3 × $3 = $9. (c) $8 is less than $9, so shop A is cheaper by $1.'),
 # Check yourself
 I('quiz', 0, '$4.05 = {b} ¢', value='405', why='4 dollars is 400¢. 400¢ + 5¢ = 405¢.'),
 I('quiz', 0, 'Pay exactly $6.35 using the fewest pieces. Pieces: {b}', value='5', why='$6 is $5 + $1 (2 pieces). 35¢ is 20¢ + 10¢ + 5¢ (3 pieces). 2 + 3 = 5 pieces.'),
 I('quiz', 0, 'A cake costs $7.40. Ravi pays with a $10 note. Change: $ {b}', value='2.60', why='$10 - $7.40 = $2.60. Count on: $7.40 + 60¢ = $8, then $2 more makes $10.'),
 I('quiz', 0, 'Ali spent $2.40 on a drink and $3.10 on a snack. He has $4.50 left. At first: $ {b}', value='10.00', why='Put back what he spent: $4.50 + $3.10 = $7.60, and $7.60 + $2.40 = $10.00.'),
]
build(6, 'Market day', 'Money', 'I can read and write money in dollars and cents. I can pay exactly, find every way, give change and work backwards.', learn, items, snug=['start1', 'start2', 'start3'])
