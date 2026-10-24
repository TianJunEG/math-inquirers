"""Online practice for Level 4 (Primary 4, ages 9-11) holiday lesson 5: Decimal Detectives (Decimals).

The questions are the ones printed in the Level 4 holiday workbook, built by p4/workbook_html.js from p4/content/l5.js:
  Start here = l5.js workbook() Q1 to Q6;   Investigation = l5.js gaps.invest (Between two decimals);
  Think harder = l5.js qbank.stretch[0:4];   Go further = l5.js qbank.challenge[-3:]  (printed as Q5 to Q7).
Every answer is recomputed by an INDEPENDENT checker (exact Decimal arithmetic, a search over every decimal with that many places, every arrangement of the digit cards,
counting in cents), never a copy of the printed answer; text_dec stops the build if a checker and the printed answer (the l5.js `key`, `gaps.invest.key` and `qbank`
answers) differ.  Decimal answers are typed, so every item lists the accepted writings (6.3, 6.30, 6.300, $4.10, 0.4 kg ...).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from p4lib import *      # noqa: E402,F401

META = dict(level=4, lesson=5, key='p4', title='Decimal Detectives', workbook_title='DECIMAL DETECTIVES', topic='Decimals',
            strand='Decimals',
            sources=['p4/content/l5.js'],
            intro=['Type a decimal with the decimal point, like 6.3. Extra zeros are fine: 6.30 is the same number. For money you may type $4.10 or 4.10. '
                   'When a question asks for a list, type the numbers with commas between them. When it asks for a whole number, type just that number.',
                   'Some questions ask you to explain or to make up your own puzzle. Think about them or write on paper, then compare with the answer after you submit.'])
S5 = 'Decimals'


def D(**k):
    return dict(strand=S5, **k)


def text_dec(iid, tier, no, skill, value, compute, q, hint, steps, src, money=False, unit=None, pad=3, svg=None, label=None):
    """A typed decimal. `value` is the printed answer; `compute` is the independent checker (returns a Decimal); the build stops if they differ."""
    v = Dec(str(value))
    got = compute()
    assert Dec(str(got)) == v, (iid, got, v)
    acc = dec_accepts(v, pad=pad, money=money, unit=unit)
    shown = ('$' + dtext(v, 2)) if money else dtext(v) + (f' {unit if isinstance(unit, str) else unit[0]}' if unit else '')
    assert shown in acc, (iid, shown)
    chk = (lambda: '$' + dtext(compute(), 2)) if money else (lambda: dtext(compute()))
    kw = {}
    if svg:
        kw['svg'] = svg
    if label:
        kw['label'] = label
    return D(id=iid, tier=tier, no=no, type='text', skill=skill, accept=acc, shown=shown, check=chk, q=q, hint=hint, steps=steps, src=src, **kw)


def text_dec_list(iid, tier, no, skill, vals, compute, q, hint, steps, src, ordered=True, svg=None, label=None):
    """A typed list of decimals (commas, spaces or 'and' between; trailing zeros allowed). compute() returns the list of Decimals in the right order."""
    want = [Dec(str(v)) for v in vals]
    got = compute()
    assert [Dec(str(g)) for g in got] == want, (iid, got, want)
    acc = dec_list_accepts(want, ordered=ordered)
    shown = ', '.join(dtext(v) for v in want)
    assert shown in acc, (iid, shown)
    kw = {}
    if svg:
        kw['svg'] = svg
    if label:
        kw['label'] = label
    return D(id=iid, tier=tier, no=no, type='text', skill=skill, accept=acc, shown=shown, check=lambda: ', '.join(dtext(v) for v in compute()), q=q, hint=hint, steps=steps, src=src, **kw)


def value_at(lo, hi, steps):
    """The number an arrow points to: it is `steps` small steps after lo on a line from lo to hi cut into 10 equal steps."""
    lo, hi = Dec(str(lo)), Dec(str(hi))
    one = (hi - lo) / 10
    return lo + one * Dec(str(steps))


LINES = {'A': (6, 7, 3), 'B': (6, 7, '8.5'), 'C': ('4.5', '4.6', 3), 'D': ('4.5', '4.6', 8), 'E': ('0.24', '0.25', 7)}
LINE_A = dec_line(6, 7, [('A', 3), ('B', '8.5')])
LINE_B = dec_line('4.5', '4.6', [('C', 3), ('D', 8)])
LINE_C = dec_line('0.24', '0.25', [('E', 7)])
FIG_LINES = combine([LINE_A, LINE_B, LINE_C], 'Three number lines, each cut into 10 equal steps. Line one from 6 to 7 with arrows A and B. Line two from 4.5 to 4.6 with arrows C and D. Line three from 0.24 to 0.25 with arrow E.', gap=0)
STEM_Z = 'Zoom in! This number line has 10 equal steps. Write the number that arrow {} points to. First work out what one small step is worth.'
SRC_Z = ['Zoom in! Write the number that each arrow points to. First work out what one small step is worth.']


def arrow_item(letter, fig, hint, steps):
    lo, hi, st = LINES[letter]
    return text_dec(f'1{letter}', 'core', f'1({letter})', 'reading decimals on a number line', value_at(lo, hi, st), lambda: value_at(lo, hi, st),
                    STEM_Z.format(letter), hint, steps, SRC_Z, svg=fig, label=f'1({letter})')


def cards_numbers(cards):
    """Every number made from the three cards with the point after the FIRST digit, found by trying each card first, second, third."""
    out = []
    for p in itertools.permutations(cards):
        out.append(Dec(f'{p[0]}.{p[1]}{p[2]}'))
    return sorted(out)


CARDS = (3, 6, 9)
CARD_FIG = dec_cards([3, 6, 9, '.'])
NUMS6 = cards_numbers(CARDS)


def betweens(lo, hi, dp):
    return [v for v in grid(lo, hi, dp) if Dec(lo) < v < Dec(hi)]


STEM_CARDS = 'Use the digit cards 3, 6 and 9 and a decimal point card once each, with the point after the FIRST digit. '
SRC_CARDS = ['Use the digit cards 3, 6, 9 and a decimal point card once each.']

# Mei and Siti: found by trying every amount of money for Siti, in cents
MEISITI = [s for s in range(0, 941) if s + (s + 120) == 940][0]
# the box of cans: the mass of one can found by trying every mass in thousandths of a kilogram
CAN = [m for m in grid(0, 3, 3) if 6 * m + Dec('0.45') == Dec('2.85')][0]

ITEMS = [
    # ================= Start here (workbook lesson 5, Q1 to Q6)
    arrow_item('A', LINE_A, 'The line goes from 6 to 7 in 10 equal steps. How much is one step? Then count the steps from 6 to the arrow.',
               ['From 6 to 7 is 1 whole, cut into 10 equal steps, so one step is 0.1.', 'Arrow A is 3 steps after 6: 6 + 0.3 = 6.3.']),
    arrow_item('B', LINE_A, 'Arrow B is not on a mark. Which two marks is it between? What number is halfway between them?',
               ['One step is 0.1, so the marks are 6.7, 6.8, 6.9 ...', 'Arrow B is halfway between the marks 6.8 and 6.9. Halfway between them is 6.85, because half of 0.1 is 0.05.']),
    arrow_item('C', LINE_B, 'First work out how big one step is: the whole line goes from 4.5 to 4.6 in 10 equal steps. Then count the steps from 4.5.',
               ['From 4.5 to 4.6 is 0.1. Cut into 10 equal steps, one step is 0.1 ÷ 10 = 0.01.', 'Arrow C is 3 steps after 4.5: 4.5 + 0.03 = 4.53.']),
    arrow_item('D', LINE_B, 'First work out how big one step is. Then count the steps from 4.5 to the arrow.',
               ['From 4.5 to 4.6 is 0.1. Cut into 10 equal steps, one step is 0.01.', 'Arrow D is 8 steps after 4.5: 4.5 + 0.08 = 4.58.']),
    arrow_item('E', LINE_C, 'The line goes from 0.24 to 0.25. How much is that? Share it into 10 equal steps to find one step, then count from 0.24.',
               ['From 0.24 to 0.25 is 0.01. Cut into 10 equal steps, one step is 0.01 ÷ 10 = 0.001.', 'Arrow E is 7 steps after 0.24: 0.24 + 0.007 = 0.247.']),
    D(id='1f', tier='core', no='1(f)', label='1(f)', type='choice', options=['A', 'B', 'C', 'D', 'E'], answer='B', skill='rounding to the nearest whole number', svg=FIG_LINES,
      check=lambda: [l for l in 'ABCDE' if round_half_up(value_at(*LINES[l]), 0) == 7][0],
      q='Look at the three number lines. Which arrow, A to E, shows a number that rounds to 7 (to the nearest whole number)?',
      hint='Work out the number at each arrow, then round each one to the nearest whole number. Which lands on 7?',
      steps=['The numbers are A 6.3, B 6.85, C 4.53, D 4.58 and E 0.247.', 'Rounded to the nearest whole number: 6.3 is 6, 6.85 is 7, 4.53 is 5, 4.58 is 5 and 0.247 is 0.', 'Only arrow B rounds to 7.'],
      src=['Which arrow, A to E, shows a number that rounds to 7?']),

    text_dec_list('2a', 'core', '2(a)', 'ordering decimals', ['3.045', '3.054', '3.405', '3.45', '3.5'], lambda: sorted(Dec(x) for x in ['3.405', '3.45', '3.054', '3.5', '3.045']),
                  'Order and compare. Write these in order, smallest first: 3.405, 3.45, 3.054, 3.5, 3.045. Type the five numbers with commas between them.',
                  'Write each number with 3 decimal places (like 2.7 is 2.700). Compare the tenths first, then the hundredths.',
                  ['With 3 decimal places the numbers are 3.405, 3.450, 3.054, 3.500 and 3.045.', 'Tenths: 3.045 and 3.054 have 0 tenths, 3.405 and 3.450 have 4 tenths, and 3.500 has 5 tenths.',
                   'Hundredths: 3.045 < 3.054 (4 is less than 5), and 3.405 < 3.450 (0 is less than 5).', 'In order: 3.045, 3.054, 3.405, 3.45, 3.5.'],
                  ['Write in order, smallest first:']),
    D(id='2b', tier='core', no='2(b)', label='2(b)', type='choice', options=['Yes, Ben is right', 'No, Ben is not right'], answer='No, Ben is not right', skill='comparing decimals',
      check=lambda: 'Yes, Ben is right' if Dec('3.405') > Dec('3.45') else 'No, Ben is not right',
      q='Ben says 3.405 is bigger than 3.45 because 405 is bigger than 45. Is Ben right?',
      hint='Line up the decimal points. Which place do you compare first, and what are the two digits there?',
      steps=['Line up the decimal points: 3.405 and 3.450.', 'The ones and the tenths are the same. In the hundredths, 0 is less than 5.', 'So 3.405 is smaller than 3.45. Ben is not right.'],
      src=['Ben says 3.405 is bigger than 3.45 because 405 is bigger than 45. Is he right?']),
    D(id='2b-why', tier='core', no='2(b)', label='2(b) why', type='selfcheck', open=True, marking_mode='self', skill='comparing decimals',
      q='Ben says 3.405 is bigger than 3.45 because 405 is bigger than 45. Explain whether he is right, and why.',
      hint='Think about what each digit is worth: ones, tenths, hundredths, thousandths. Does a number with more digits have to be bigger?',
      steps=['Ben is not right. Line up the decimal points and write 3.45 as 3.450.', 'Compare place by place: the ones and the tenths are the same, but 3.405 has 0 hundredths and 3.450 has 5 hundredths.',
             'So 3.405 is smaller. A decimal with more digits is not always bigger. Any clear reason like this is good.'],
      src=['Is he right? Explain.']),

    text_dec('3small', 'core', '3(a)', 'rounding backwards', '7.35', lambda: min(n for n in grid(7, 8, 2) if round_half_up(n, 1) == Dec('7.4')),
             'The rounding detective. A number has 2 decimal places. Rounded to 1 decimal place, it is 7.4. The number line is marked in hundredths. What is the smallest it can be?',
             'Which marks on the line round to 7.4? Look at the halfway marks on each side of 7.4.',
             ['Halfway between 7.3 and 7.4 is 7.35. A number exactly halfway rounds up, so 7.35 rounds to 7.4.', '7.34 is closer to 7.3, so it rounds down to 7.3.', 'The smallest number is 7.35.'],
             ['The rounding detective. A number has 2 decimal places. Rounded to 1 decimal place, it is 7.4.', 'What is the smallest it can be?'], svg=round_line(), label='3(a) small'),
    text_dec('3large', 'core', '3(a)', 'rounding backwards', '7.44', lambda: max(n for n in grid(7, 8, 2) if round_half_up(n, 1) == Dec('7.4')),
             'The rounding detective. A number has 2 decimal places. Rounded to 1 decimal place, it is 7.4. The number line is marked in hundredths. What is the largest it can be?',
             '7.45 is halfway between 7.4 and 7.5. Does 7.45 round to 7.4 or to 7.5? Which marks near it still round to 7.4?',
             ['Halfway between 7.4 and 7.5 is 7.45. A number exactly halfway rounds up, so 7.45 rounds to 7.5, not 7.4.', '7.44 is closer to 7.4, so it rounds to 7.4.', 'The largest number is 7.44.'],
             ['The rounding detective. A number has 2 decimal places. Rounded to 1 decimal place, it is 7.4.', 'The largest?'], svg=round_line(), label='3(a) large'),

    text_dec_list('4a', 'core', '4(a)', 'ordering decimals made from digit cards', [dtext(v) for v in NUMS6], lambda: cards_numbers(CARDS),
                  STEM_CARDS + 'That makes 6 numbers. Type them all in order, smallest first, with commas between them. (With the cards 1, 4 and 7 you could make 1.47.)',
                  'Put each digit in the ones place in turn. Each one can be followed by the other two digits in two different ways.',
                  ['Put each card first in turn. With 3 first you can make 3.69 and 3.96. With 6 first you can make 6.39 and 6.93. With 9 first you can make 9.36 and 9.63.', 'In order, smallest first: 3.69, 3.96, 6.39, 6.93, 9.36, 9.63.'],
                  ['Use the digit cards 3, 6, 9 and a decimal point card once each.', 'Make all 6 numbers and list them in order, smallest first.'], svg=CARD_FIG),
    text_dec('4b', 'core', '4(b)', 'comparing decimals made from digit cards', '9.63', lambda: max(cards_numbers(CARDS)),
             STEM_CARDS + 'Which is the largest number?', 'Which digit should go in the ones place to make the number as big as possible? Then which digit comes next?',
             ['The biggest digit, 9, goes in the ones place.', 'The next biggest digit, 6, goes in the tenths place.', 'The largest number is 9.63.'],
             ['Which is the largest number?'], svg=CARD_FIG),
    text_dec('4c', 'core', '4(c)', 'finding the closest decimal', '6.93', lambda: min(cards_numbers(CARDS), key=lambda v: abs(7 - v)),
             STEM_CARDS + 'Which of your numbers is closest to 7?', 'Work out how far each of your numbers is from 7. Which distance is the smallest?',
             ['6.93 is 7 − 6.93 = 0.07 away from 7.', '6.39 is 0.61 away and 9.36 is 2.36 away. The other three numbers are even further from 7.', 'The closest number is 6.93.'],
             ['Which of your numbers is closest to 7?'], svg=CARD_FIG),
    text_dec_list('4d', 'core', '4(d)', 'rounding to the nearest whole number', ['3.69', '3.96'], lambda: [v for v in cards_numbers(CARDS) if round_half_up(v, 0) == 4],
                  STEM_CARDS + 'Two of your numbers round to 4 (to the nearest whole number). Which two? Type them with a comma between.',
                  'A number rounds to 4 if it is closer to 4 than to 3 or 5. Which of your numbers are close to 4?',
                  ['Round each number to the nearest whole number: 3.69 is 4, 3.96 is 4, 6.39 is 6, 6.93 is 7, 9.36 is 9 and 9.63 is 10.', 'The two numbers that round to 4 are 3.69 and 3.96.'],
                  ['Two of your numbers round to 4 (to the nearest whole number). Which two?'], ordered=False, svg=CARD_FIG),

    text_dec('5mei', 'core', '5', 'bar model with decimals', '5.30', lambda: Dec(MEISITI + 120) / 100,
             'Mei and Siti have $9.40 altogether. Mei has $1.20 more than Siti. The bar model shows the two girls. How much money does Mei have?',
             'If Mei gave back her extra $1.20, the two girls would have the same amount. How much would they have altogether then?',
             ['Take away Mei\'s extra $1.20: $9.40 − $1.20 = $8.20.', 'Now both girls have the same, so $8.20 ÷ 2 = $4.10 each. That is Siti\'s money.', 'Mei has $1.20 more: $4.10 + $1.20 = $5.30.', 'Check: $4.10 + $5.30 = $9.40.'],
             ['Mei and Siti have $9.40 altogether. Mei has $1.20 more than Siti. How much money does each girl have?'], money=True, pad=2,
             svg=money_bars('Siti', 'Mei', 3, 1, '$1.20 more', '$9.40'), label='5'),
    text_dec('5siti', 'core', '5', 'bar model with decimals', '4.10', lambda: Dec(MEISITI) / 100,
             'Mei and Siti have $9.40 altogether. Mei has $1.20 more than Siti. The bar model shows the two girls. How much money does Siti have?',
             'Take away Mei\'s extra $1.20 first. Then the two girls have the same amount. Share what is left equally.',
             ['Take away Mei\'s extra $1.20: $9.40 − $1.20 = $8.20.', 'Now both girls have the same, so $8.20 ÷ 2 = $4.10.', 'Siti has $4.10. (Mei has $1.20 more, $5.30, and $4.10 + $5.30 = $9.40.)'],
             ['Mei and Siti have $9.40 altogether. Mei has $1.20 more than Siti. How much money does each girl have?'], money=True, pad=2,
             svg=money_bars('Siti', 'Mei', 3, 1, '$1.20 more', '$9.40'), label='5'),

    text_dec('6step1', 'core', '6', 'mass with decimals', '2.4', lambda: Dec('2.85') - Dec('0.45'),
             'A box holds 6 cans that all have the same mass. Step 1: the 6 cans alone. Find their mass. 2.85 − 0.45 = ____ kg.',
             'Take the mass of the empty box away from the mass of the full box. Line up the decimal points.',
             ['The scale with the cans reads 2.85 kg and includes the box. The empty box is 0.45 kg.', '2.85 − 0.45 = 2.40 kg is the mass of the 6 cans alone.'],
             ['A box holds 6 cans that all have the same mass.', 'Step 1: the 6 cans alone.'], unit=('kg', 'kilograms', 'kilogram'), svg=can_scales(), label='6'),
    text_dec('6a', 'core', '6(a)', 'mass with decimals', '0.4', lambda: CAN,
             'A box holds 6 cans that all have the same mass. Look at the picture. What is the mass of one can, in kilograms?',
             'First find the mass of the 6 cans on their own. Then share it equally between the 6 cans.',
             ['The 6 cans alone are 2.85 − 0.45 = 2.40 kg.', 'Share 2.40 kg between 6 cans: 2.40 ÷ 6 = 0.4 kg.', 'Check: 6 × 0.4 = 2.4, and 2.4 + 0.45 = 2.85.'],
             ['What is the mass of one can?'], unit=('kg', 'kilograms', 'kilogram'), svg=combine([can_scales(), can_bar()], 'A box with 6 cans on a scale reads 2.85 kilograms and the empty box reads 0.45 kilograms. Below, a bar cut into 6 equal parts, one for each can.'), label='6(a)'),
    text_dec('6b', 'core', '6(b)', 'mass with decimals', '2.05', lambda: Dec('0.45') + 4 * CAN,
             'All the cans have the same mass. Ali takes 2 cans out of the full box in the picture. What is the mass of the box and the cans now, in kilograms?',
             'How much do 2 cans weigh together? Take that away from the mass of the full box.',
             ['One can is 0.4 kg, so 2 cans are 0.8 kg.', 'The box and cans now: 2.85 − 0.8 = 2.05 kg.', 'Check another way: the box 0.45 kg plus 4 cans (4 × 0.4 = 1.6 kg) is 2.05 kg.'],
             ['Ali takes 2 cans out of the box. What is the mass of the box and cans now?'], unit=('kg', 'kilograms', 'kilogram'), svg=can_scales(), label='6(b)'),

    # ================= Investigation: Between two decimals
    D(id='I1', tier='invest', no='Investigation (easy step)', label='Inv easy', type='text', skill='place value to thousandths',
      accept=['0.350, 0.360', '0.350 0.360', '0.350;0.360', '0.350; 0.360', '0.350 and 0.360', '0.350 < 0.360', '.350, .360'], shown='0.350, 0.360',
      check=lambda: ', '.join(dtext(Dec(x), 3) for x in ('0.35', '0.36')),
      q='Between two decimals. Siti says: "There is no decimal between 0.35 and 0.36, because they are next to each other." Easy first step: write 0.35 with 3 decimal places, and 0.36 with 3 decimal places. Type them with a comma between.',
      hint='Write 0.35 in a place-value chart with ones, tenths, hundredths and thousandths. What goes in the thousandths place?',
      steps=['0.35 has 3 tenths and 5 hundredths and no thousandths, so it can be written 0.350.', 'In the same way 0.36 = 0.360. Adding a 0 in the thousandths place does not change the number.'],
      src=['Siti says: "There is no decimal between 0.35 and 0.36, because they are next to each other."', 'Write 0.35 as 0.350 and 0.36 as 0.360.']),
    D(id='Ia', tier='invest', no='Investigation (a)', label='Inv (a)', type='text', skill='decimals between two decimals', accept=['0.355'] + [x for x in between_forms('0.35', '0.36') if x != '0.355'],
      shown='any decimal between 0.35 and 0.36, for example 0.355', check=lambda: dtext((Dec('0.35') + Dec('0.36')) / 2),
      q='Siti says there is no decimal between 0.35 and 0.36. Find a decimal that is between them. Type one.',
      hint='Try writing both numbers with more decimal places, so that there is room between them.',
      steps=['0.35 = 0.350 and 0.36 = 0.360, so any of 0.351, 0.352 ... 0.359 is between them.', 'For example 0.355: it is more than 0.350 and less than 0.360. (A decimal with more places, such as 0.3505, is also between them.)'],
      src=['Find a decimal between 0.35 and 0.36. Write it.']),
    D(id='Ib-list', tier='invest', no='Investigation (b)', label='Inv (b) list', type='selfcheck', open=False, skill='listing decimals',
      check=lambda: betweens('0.35', '0.36', 3),
      q='Find as many decimals with 3 decimal places as you can between 0.35 and 0.36. Write them in order, then compare your list with the model answer.',
      hint='Write both numbers with 3 decimal places, then count up in thousandths from the first to the second. Do not include the two ends.',
      steps=['Count in thousandths from 0.350 to 0.360, without the two ends: 0.351, 0.352, 0.353, 0.354, 0.355, 0.356, 0.357, 0.358, 0.359.', 'There are 9 of them. Did your list have some of these?'],
      src=['Find as many decimals with 3 decimal places as you can between 0.35 and 0.36. Write them in order.']),
    D(id='Ib-count', tier='invest', no='Investigation (b)', label='Inv (b) count', type='number', skill='counting decimals', answer=9, check=lambda: len(betweens('0.35', '0.36', 3)),
      q='How many decimals with 3 decimal places are between 0.35 and 0.36? (Do not count 0.35 and 0.36.)',
      hint='Write both numbers with 3 decimal places. How many thousandths are there from the first to the second? Do not count the two ends.',
      steps=['0.350 to 0.360 is 10 thousandths, so there are 10 steps of 0.001.', 'The numbers strictly between are 0.351 to 0.359. That is 9 numbers.'],
      src=['How many are there?']),
    D(id='Ic', tier='invest', no='Investigation (c)', label='Inv (c)', type='choice', options=['Yes, Siti is right', 'No, Siti is not right'], answer='No, Siti is not right', skill='density of decimals',
      check=lambda: 'No, Siti is not right' if betweens('0.35', '0.36', 3) else 'Yes, Siti is right',
      q='Siti says there is no decimal between 0.35 and 0.36, because they are next to each other. Is Siti right?',
      hint='Think about what you found in parts (a) and (b).',
      steps=['Siti is not right. There are 9 decimals with 3 decimal places between 0.35 and 0.36, such as 0.355.'],
      src=['Is Siti right?']),
    D(id='Ic-why', tier='invest', no='Investigation (c)', label='Inv (c) why', type='selfcheck', open=True, marking_mode='self', skill='density of decimals',
      check=lambda: (Dec('0.35') < Dec('0.3505') < Dec('0.351'), Dec('0.35') < Dec('0.35025') < Dec('0.3505')),
      q='Take the smallest decimal you found in part (b). Can you find a decimal between 0.35 and that decimal? What do you think happens if you keep going?',
      hint='Write 0.35 with 4 decimal places, and the other number with 4 decimal places too. Then look for a number in between.',
      steps=['Yes. Between 0.35 and 0.351 there is 0.3505, with 4 decimal places. Written with 4 places: 0.3500 < 0.3505 < 0.3510.',
             'Between 0.35 and 0.3505 there is 0.35025, and so on. You can always write more zeros and find another decimal.', 'So there is no "next" decimal after 0.35. Siti is not right: there are always more decimals in between.'],
      src=['Can you find a decimal between 0.35 and your smallest one? What do you think happens if you keep going?']),

    # ================= Think harder (qbank.stretch[0:4])
    D(id='T1', tier='stretch', no='Think harder 1', label='T1', type='set', answer=[0, 1, 2, 3], ordered=False, skill='comparing decimals with a missing digit',
      check=lambda: [d for d in range(10) if Dec(f'3.{d}5') < Dec('3.42')],
      q='A digit goes in the place of the ? in 3.?5 < 3.42. Find ALL the digits that can go there. Type the digits with commas between them.',
      hint='Try the digits 0 to 9 one at a time. Compare the tenths first.',
      steps=['Try each digit: 3.05, 3.15, 3.25 and 3.35 are all less than 3.42.', '3.45 is more than 3.42: the tenths are the same (4) but 5 hundredths is more than 2 hundredths. 3.55 and bigger are more than 3.42 too.', 'The digits are 0, 1, 2 and 3.'],
      src=['Find ALL the digits that can go in the box']),
    text_dec('T2small', 'stretch', 'Think harder 2', 'rounding backwards', '9.5', lambda: min(n for n in grid(9, 11, 2) if round_half_up(n, 0) == 10),
             'A number with 2 decimal places rounds to 10 when rounded to the nearest whole number. What is the smallest it can be?',
             'Think of a number line from 9 to 10. Which numbers round up to 10? Where does that start?',
             ['Halfway between 9 and 10 is 9.5, and a number exactly halfway rounds up. So 9.50 rounds to 10.', '9.49 is closer to 9, so it rounds down to 9.', 'The smallest is 9.50.'],
             ['A number with 2 decimal places rounds to 10 when rounded to the nearest whole number. What is the smallest it can be? The largest?'], label='T2 small'),
    text_dec('T2large', 'stretch', 'Think harder 2', 'rounding backwards', '10.49', lambda: max(n for n in grid(9, 11, 2) if round_half_up(n, 0) == 10),
             'A number with 2 decimal places rounds to 10 when rounded to the nearest whole number. What is the largest it can be?',
             'Which numbers just above 10 still round down to 10? Where does that stop?',
             ['Halfway between 10 and 11 is 10.5, and 10.50 would round up to 11.', '10.49 is closer to 10, so it rounds to 10.', 'The largest is 10.49.'],
             ['A number with 2 decimal places rounds to 10 when rounded to the nearest whole number. What is the smallest it can be? The largest?'], label='T2 large'),
    text_dec('T3a', 'stretch', 'Think harder 3', 'decimals between decimals', '2.65', lambda: (Dec('2.6') + Dec('2.7')) / 2,
             'What number is halfway between 2.6 and 2.7?', 'Write 2.6 and 2.7 with the same number of decimal places. What is in the middle?',
             ['2.6 = 2.60 and 2.7 = 2.70.', 'Halfway between 60 hundredths and 70 hundredths is 65 hundredths, so the number is 2.65.'],
             ['What number is halfway between 2.6 and 2.7?'], label='T3(a)'),
    text_dec('T3b', 'stretch', 'Think harder 3', 'decimals between decimals', '2.605', lambda: (Dec('2.6') + Dec('2.61')) / 2,
             'What number is halfway between 2.6 and 2.61?', 'Write both numbers with 3 decimal places. What is halfway between 2.600 and 2.610?',
             ['2.6 = 2.600 and 2.61 = 2.610.', 'Halfway between 600 thousandths and 610 thousandths is 605 thousandths, so the number is 2.605.'],
             ['What number is halfway between 2.6 and 2.61?'], label='T3(b)'),
    text_dec('T4', 'stretch', 'Think harder 4', 'number riddles with decimals', '4.687',
             lambda: [n for n in grid(4, 5, 3) if 4 < n < 5 and round_half_up(n, 1) == Dec('4.7') and (lambda s: int(s[3]) == int(s[2]) + 2 and sum(map(int, s.replace('.', ''))) == 25)(dtext(n, 3))][0],
             'Mystery decimal. I have 3 decimal places and I am between 4 and 5. Rounded to 1 decimal place, I am 4.7. My hundredths digit is 2 more than my tenths digit. My digits add up to 25. Who am I?',
             'Start with the tenths and hundredths digits. Use the rounding clue to see which tenths digits are possible. Then use the digits that add to 25.',
             ['A number that rounds to 4.7 is from 4.65 up to (but not including) 4.75, so the tenths digit is 6 or 7.', 'If the tenths digit is 7, the hundredths digit would be 9 and the number would be 4.79..., too big. So the tenths digit is 6 and the hundredths digit is 8: 4.68_.',
              'The digits add up to 25: 4 + 6 + 8 + _ = 25, so the last digit is 7.', 'I am 4.687.'],
             ['Mystery decimal. I have 3 decimal places and I am between 4 and 5.'], label='T4'),

    # ================= Go further (qbank.challenge[-3:], printed Q5 to Q7)
    D(id='G5', tier='challenge', no='Go further 5', label='G5', type='selfcheck', open=True, marking_mode='open', skill='making up a closest-to puzzle',
      check=lambda: ((min(DEC4, key=lambda v: abs(40 - v)), min(sorted(DEC4, key=lambda v: abs(40 - v))[1:], key=lambda v: abs(40 - v))), min(DEC4, key=lambda v: abs(50 - v))),
      q='Make up your own "closest to" puzzle. Choose four digit cards and a decimal point (the point goes between two digits). Pick a target number and find the number with 2 decimal places that is closest to it. Then ask: what if the target changes?',
      hint='Pick four digits. List the numbers you can make with 2 decimal places, then see which one is closest to your target.',
      steps=['Puzzles will vary. Check yours by listing every number that can be made.',
             'Model: with the cards 3, 5, 6, 9 and the target 40, the closest number with 2 decimal places is 39.65 (0.35 away). The next closest is 39.56 (0.44 away).',
             'What if the target is 50? Then the closest is 53.69 (3.69 away). Below 50, the closest is 39.65, which is 10.35 away.', 'Show your puzzle to a partner or your tutor and check each other\'s answers.'],
      src=['Make up your own "closest to" puzzle.']),
    text_dec('G6ali', 'challenge', 'Go further 6', 'bar model with decimals', '2.30', lambda: Dec([a for a in range(0, 921) if a + (a + 50) + (a + 50 + 130) == 920][0]) / 100,
             'Ali, Ben and Siti share $9.20. Ben gets $0.50 more than Ali. Siti gets $1.30 more than Ben. How much does Ali get?',
             'Siti has $1.30 more than Ben, and Ben has $0.50 more than Ali. How much more than Ali does Siti have?',
             ['Ben has $0.50 more than Ali. Siti has $1.30 more than Ben, so Siti has $0.50 + $1.30 = $1.80 more than Ali.', 'Take away the extras: $0.50 (Ben) + $1.80 (Siti) = $2.30. $9.20 − $2.30 = $6.90.',
              'Now the three shares are equal: $6.90 ÷ 3 = $2.30. Ali gets $2.30.'],
             ['Ali, Ben and Siti share $9.20. Ben gets $0.50 more than Ali. Siti gets $1.30 more than Ben. How much does each child get?'], money=True, pad=2, svg=three_money_bars(), label='G6 Ali'),
    text_dec('G6ben', 'challenge', 'Go further 6', 'bar model with decimals', '2.80', lambda: Dec([a for a in range(0, 921) if a + (a + 50) + (a + 50 + 130) == 920][0] + 50) / 100,
             'Ali, Ben and Siti share $9.20. Ben gets $0.50 more than Ali. Siti gets $1.30 more than Ben. How much does Ben get?',
             'Find how much Ali gets first. Then Ben has $0.50 more.',
             ['Take away the extras ($0.50 for Ben and $0.50 + $1.30 = $1.80 for Siti): $9.20 − $2.30 = $6.90, and $6.90 ÷ 3 = $2.30 is Ali\'s share.', 'Ben gets $0.50 more than Ali: $2.30 + $0.50 = $2.80.'],
             ['Ali, Ben and Siti share $9.20. Ben gets $0.50 more than Ali. Siti gets $1.30 more than Ben. How much does each child get?'], money=True, pad=2, svg=three_money_bars(), label='G6 Ben'),
    text_dec('G6siti', 'challenge', 'Go further 6', 'bar model with decimals', '4.10', lambda: Dec([a for a in range(0, 921) if a + (a + 50) + (a + 50 + 130) == 920][0] + 180) / 100,
             'Ali, Ben and Siti share $9.20. Ben gets $0.50 more than Ali. Siti gets $1.30 more than Ben. How much does Siti get?',
             'Find how much Ben gets first. Then Siti has $1.30 more than Ben.',
             ['Ali gets $2.30 and Ben gets $2.30 + $0.50 = $2.80.', 'Siti gets $1.30 more than Ben: $2.80 + $1.30 = $4.10.', 'Check: $2.30 + $2.80 + $4.10 = $9.20.'],
             ['Ali, Ben and Siti share $9.20. Ben gets $0.50 more than Ali. Siti gets $1.30 more than Ben. How much does each child get?'], money=True, pad=2, svg=three_money_bars(), label='G6 Siti'),
    text_dec('G7', 'challenge', 'Go further 7', 'mass with decimals', '0.25', lambda: [j for j in grid(0, 1.45, 2) if (Dec('1.45') - j) == 2 * (Dec('0.85') - j)][0],
             'A jug full of water weighs 1.45 kg. When it is half full, it weighs 0.85 kg. What is the mass of the empty jug, in kilograms?',
             'What is the mass of the water that was poured out? What fraction of the water is that?',
             ['The water that was poured out is 1.45 − 0.85 = 0.6 kg. That is half of the water.', 'All the water is 0.6 + 0.6 = 1.2 kg.', 'The empty jug is 1.45 − 1.2 = 0.25 kg.'],
             ['A jug full of water weighs 1.45 kg. When it is half full, it weighs 0.85 kg. What is the mass of the empty jug?'], unit=('kg', 'kilograms', 'kilogram'), svg=jugs(), label='G7'),
]

DEC4 = sorted({Dec(f'{p[0]}{p[1]}.{p[2]}{p[3]}') for p in itertools.permutations((3, 5, 6, 9))})

finish(ITEMS)

# every number combination of the one variant family is run against a brute-force oracle by the builder
VARIANTS = {
    'Ib-count': dict(
        base=dict(x=35, d=1),
        tpl=dict(vars=dict(x=[12, 23, 35, 48, 61, 74], d=[1, 2, 3]), derive=dict(y='x+d'),
                 q='How many decimals with 3 decimal places are between 0.{x} and 0.{y}? (Do not count 0.{x} and 0.{y}.)', answer='10*d-1',
                 hint='Write 0.{x} and 0.{y} with 3 decimal places. How many thousandths from the first to the second? Do not count the two ends.',
                 steps=['0.{x} = 0.{x}0 and 0.{y} = 0.{y}0. From one to the other is {d} hundredths = {d}0 thousandths.', 'That is 10 × {d} = {d}0 steps of 0.001, so there are 10 × {d} − 1 = {ans} numbers strictly between them.']),
        oracle=lambda e: len([v for v in grid(Dec(e['x']) / 100, Dec(e['x'] + e['d']) / 100, 3) if Dec(e['x']) / 100 < v < Dec(e['x'] + e['d']) / 100])),
}
