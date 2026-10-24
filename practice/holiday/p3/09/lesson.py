"""Online practice for Level 3 (Primary 3, ages 8-10) holiday lesson 9: Measure and Money Masters (Length, mass, volume, money and time).

The questions are the ones printed in the Level 3 holiday workbook (p3/workbook_html.js builds it from p3/content/l9.js: Start here = the lesson's workbook() pages;
Think harder 1 to 4 and Go further 5 to 7 = qbank stretch[0..3] and challenge[-3:]; the Extra questions = deck.takeHome (printed as "Take-home"); the Investigation =
p3/gifted.json lesson 9).  Every answer is recomputed by an INDEPENDENT checker below (changing units by adding and taking away, minutes since midnight for every time sum,
every set of three things from the price list, every way of paying 50 cents tried one coin at a time, the buses listed 25 minutes apart), never a copy of the printed answer;
build_holiday.py stops if a checker and the printed answer differ.  The figures are the workbook's own data (the ribbon, the 24-hour strip, the time lines, the bus line, the bar
models of Think harder 3 and Go further 5 and 6, the five item prices), drawn larger for a phone; the checks just below stop the build if the data here differs from the printed figures.
"""
import itertools, os, re, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from hlib import *          # noqa: E402,F401
from p3lib import *         # noqa: E402,F401
from p3lib_w5 import *      # noqa: E402,F401

META = dict(level=3, lesson=9, key='p3', title='Measure and Money Masters', workbook_title='MEASURE AND MONEY MASTERS', topic='Length, Mass, Volume, Money and Time', strand='Measurement, money and time',
            sources=['p3/content/l9.js', 'p3/gifted.json'],
            intro=['Change to ONE unit before you compare, add or take away: 1 m = 100 cm, 1 kg = 1000 g, 1 ℓ = 1000 ml and $1 = 100¢. For time, use a time line and jump to the next o’clock.',
                   'Type the answers here. Where a question asks you to draw, do it on paper and then compare with the picture shown after you submit.'])
FIG = figs5()['figs']
SK = 'Measurement, money and time'
EXTRA = 'Extra practice. '
SRC9 = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..', 'p3', 'content', 'l9.js'), encoding='utf-8').read()


def I(**kw):
    kw.setdefault('strand', SK)
    return kw


def texts(svg_text):
    return re.findall(r'<text[^>]*>([^<]*)</text>', svg_text)


# ---------------------------------------------------------------- the data of the figures equals the printed workbook figures
assert texts(FIG['l9_ribbon']) == ['3 m', '65', '65', '65', '65', '?', '3 m = 300 cm']
assert all(x in texts(FIG['l9_strip']) for x in ['00:00', '12:00', '15:00', '18:00', '21:00', '24:00', 'am', 'pm', 'noon'])
assert set(texts(FIG['l9_q5a'])) >= {'3:45 pm', '4:00', '5:00', '5:10 pm', '? min', '? h'}
assert set(texts(FIG['l9_q5b'])) >= {'4:35 pm', '5:00', '?', '? min'} and set(texts(FIG['l9_q5c'])) >= {'7:00', '8:00', '9:00', '9:15 pm', '? min'}
assert set(texts(FIG['l9_q6'])) >= {'06:40', '08:15', 'Ravi arrives'} and FIG['l9_q6'].count('<line') >= 8
assert [x for x in texts(FIG['l9_t2']) if x] == ['09:30', '12:00', '15:00', '18:00', '21:00']
assert set(texts(FIG['l9_t3'])) >= {'box', '1 kg 50 g', 'Box + 4 books'} and set(texts(FIG['l9_c5'])) >= {'1 kg 200 g', '750 g', 'bottle', 'water', 'Full', 'Half poured out'}
assert set(texts(FIG['l9_c6'])) >= {'$9.20', '60¢', '3 pens', '2 files'}
PRICES = [('Book', '$7.85'), ('Pen set', '$4.60'), ('Puzzle', '$6.90'), ('Stickers', '$2.35'), ('Water bottle', '$5.50')]
assert "['$7.85', '$4.60', '$6.90', '$2.35', '$5.50']" in SRC9 and "['Book', 'Pen set', 'Puzzle', 'Stickers', 'Water bottle']" in SRC9
PRICE = {n: cents(p) for n, p in PRICES}
BUDGET = 2000

# ---------------------------------------------------------------- helpers for the checkers
BAGS = {'A': g_of(1, 300), 'B': 1030, 'C': g_of(1), 'D': g_of(1, 3)}          # Q2: 1 kg 300 g, 1030 g, 1 kg, 1 kg 3 g


def dollars(c):
    return f'${c // 100}.{c % 100:02d}'


def sets_of_three():
    """Every set of 3 different things from the price list, with its cost."""
    return [(combo, sum(PRICE[n] for n in combo)) for combo in itertools.combinations([n for n, _ in PRICES], 3)]


def best_sets():
    ok = [(c, cost) for c, cost in sets_of_three() if cost <= BUDGET]
    top = max(cost for _, cost in ok)
    return [c for c, cost in ok if cost == top], top


def to24(h, m, ispm):
    return (h % 12 + (12 if ispm else 0), m)


def to12(h, m):
    return (h % 12 or 12, m, 'pm' if h >= 12 else 'am')


BUSES = hourly_from(mins(6, 40), 25, 6)          # 06:40, 07:05, ... the first six buses
assert [tm(t) for t in BUSES] == ['06:40', '07:05', '07:30', '07:55', '08:20', '08:45']
RAVI = mins(8, 15)


def next_bus(after):
    return min(t for t in BUSES if t >= after)


def latest_bus(ride, deadline):
    return max(t for t in BUSES if t + ride <= deadline)


def ways_50():
    return sorted(pay_ways(50, [20, 10, 5]), reverse=True)          # the printed order: 2,1,0; 2,0,2; 1,3,0 ... 0,0,10


def coins_used(w):
    return sum(w)


ITEMS = [
    # ================= Start here (workbook lesson 9, No.1 to No.6)
    I(id='1a', tier='core', no='1(a)', label='1(a)', type='number', skill='changing units', answer=200,
      q='Change to ONE unit. 1 m = 100 cm. How many cm is 2 m? Type the number.', check=lambda: cm_of(2),
      hint='1 m is 100 cm. How many hundreds are there in 2 m?',
      steps=['1 m is 100 cm.', '2 m is two hundreds: 100 + 100 = 200.', '2 m = 200 cm.'],
      src=['Trick 1: change to ONE unit.', '2 m  =  ________ cm']),
    I(id='1b', tier='core', no='1(b)', label='1(b)', type='number', skill='changing units', answer=3000,
      q='Change to ONE unit. 1 kg = 1000 g. How many g is 3 kg? Type the number.', check=lambda: g_of(3),
      hint='1 kg is 1000 g. How many thousands are there in 3 kg?',
      steps=['1 kg is 1000 g.', '3 kg is three thousands: 1000 + 1000 + 1000 = 3000.', '3 kg = 3000 g.'],
      src=['3 kg  =  ________ g']),
    I(id='1c', tier='core', no='1(c)', label='1(c)', type='number', skill='changing units', answer=306,
      q='Change to ONE unit. 1 m = 100 cm. How many cm is 3 m 6 cm? Type the number.', check=lambda: cm_of(3, 6),
      hint='Write 3 m as 300 cm first.',
      steps=['Write 3 m as 300 cm.', 'Then add the 6 cm: 300 + 6 = 306.', '3 m 6 cm = 306 cm. (It is not 36 cm: the 3 m is 300 cm, so the 6 goes in the ones place.)'],
      src=['3 m 6 cm  =  ________ cm', 'Hint for (c): write 3 m as 300 cm first.']),
    I(id='1d', tier='core', no='1(d)', label='1(d)', type='number', skill='changing units', answer=2450,
      q='Change to ONE unit. 1 kg = 1000 g. How many g is 2 kg 450 g? Type the number.', check=lambda: g_of(2, 450),
      hint='Write 2 kg as grams first. Then add the 450 g.',
      steps=['2 kg = 2000 g.', '2000 + 450 = 2450.', '2 kg 450 g = 2450 g.'],
      src=['2 kg 450 g  =  ________ g']),
    I(id='1e', tier='core', no='1(e)', label='1(e)', type='fields', skill='changing units', answer=[4, 80], frame='4080 ml = {f1} ℓ {f2} ml',
      q='Change 4080 ml into litres and millilitres. (1 ℓ = 1000 ml.) Fill in the boxes.', check=lambda: list(count_in(4080, 1000)),
      hint='How many whole 1000 ml fit into 4080 ml? How much is left over?',
      steps=['4 thousands fit into 4080: 4000 ml is 4 ℓ.', '4080 - 4000 = 80 ml are left over.', '4080 ml = 4 ℓ 80 ml.'],
      src=['4080 ml  =  ____ ℓ  ____ ml']),
    I(id='1f', tier='core', no='1(f)', label='1(f)', type='number', skill='changing units', answer=40, svg=ribbon_fig(),
      q='Mei cuts 4 pieces, each 65 cm long, from a ribbon 3 m long. How many cm of ribbon are left? Type the number.', check=lambda: cm_of(3) - 4 * 65,
      hint='Change 3 m to cm first. How much do the 4 pieces use?',
      steps=['The ribbon is 3 m = 300 cm long.', 'Four pieces of 65 cm: 65 + 65 + 65 + 65 = 260 cm.', '300 - 260 = 40, so 40 cm of ribbon are left.'],
      sol_fig=lambda g: ribbon_fig(solved=True),
      src=['Mei cuts 4 pieces, each 65 cm long, from a ribbon 3 m long. How much ribbon is left?']),

    I(id='2-order', tier='core', no='2(a)', label='2(a)', type='text', skill='comparing masses', accept=order_forms(['C', 'D', 'B', 'A']), shown='C, D, B, A',
      q='Four bags of rice are weighed.\nBag A: 1 kg 300 g. Bag B: 1030 g.\nBag C: 1 kg. Bag D: 1 kg 3 g.\nPut the bags in order, lightest first. Type the four letters.',
      check=lambda: ', '.join(sorted(BAGS, key=BAGS.get)),
      hint='Change every mass to grams first. 1 kg is 1000 g.',
      steps=['Change every mass to grams: A is 1300 g, B is 1030 g, C is 1000 g and D is 1003 g.', 'Put the numbers in order, smallest first: 1000, 1003, 1030, 1300.', 'Lightest first: C, D, B, A (1 kg, 1 kg 3 g, 1030 g, 1 kg 300 g).'],
      src=['Four bags of rice are weighed:', 'Order them, lightest first:']),
    I(id='2b-g', tier='core', no='2(b)', label='2(b) grams', type='number', skill='changing units', answer=1030,
      q='How many grams is 1 kg 30 g? Type the number.', check=lambda: g_of(1, 30),
      hint='Change the 1 kg to grams first. Then add the 30 g.',
      steps=['1 kg = 1000 g.', '1000 + 30 = 1030.', '1 kg 30 g = 1030 g.'],
      src=['Ben says, “1 kg 30 g is the same as 130 g.” Explain his mistake.']),
    I(id='2b-why', tier='core', no='2(b)', label='2(b) explain', type='selfcheck', open=True, marking_mode='self', skill='explaining a mistake',
      q='Ben says, “1 kg 30 g is the same as 130 g.” Explain his mistake. Write your idea, then compare with the answer shown.', check=lambda: g_of(1, 30),
      hint='How many grams are there in 1 kg?',
      steps=['1 kg is 1000 g, not 100 g.', 'So 1 kg 30 g = 1000 g + 30 g = 1030 g.', 'Ben wrote 130 g. He put the 30 straight after the 1 and forgot the 1000. 130 g is much less than 1 kg.'],
      src=['Ben says, “1 kg 30 g is the same as 130 g.” Explain his mistake.']),

    I(id='3a-yn', tier='core', no='3(a)', label='3(a) yes/no', type='choice', skill='money and budgets', options=['Yes', 'No'], answer='No', svg=price_list_fig(PRICES, 'Prices'),
      q='Siti has $20. She wants to buy 3 different things from the list. Can she buy the book, the puzzle and the water bottle?',
      check=lambda: 'Yes' if sum(PRICE[n] for n in ['Book', 'Puzzle', 'Water bottle']) <= BUDGET else 'No',
      hint='Find the cost of the three things together. Is it more than $20?',
      steps=['Add the prices: $7.85 + $6.90 = $14.75.', '$14.75 + $5.50 = $20.25.', '$20.25 is more than $20, so she cannot buy all three.'],
      src=['Siti has $20. She wants to buy 3 different things from this list.', 'Can she buy the book, the puzzle and the water bottle? Show how you know.']),
    I(id='3a-total', tier='core', no='3(a)', label='3(a) total', type='text', skill='adding money', accept=money_forms(2025), shown='$20.25', svg=price_list_fig(PRICES, 'Prices'),
      q='How much do the book, the puzzle and the water bottle cost together? Type the amount in dollars.', check=lambda: dollars(sum(PRICE[n] for n in ['Book', 'Puzzle', 'Water bottle'])),
      hint='Add the dollars first and then the cents, or change every price to cents.',
      steps=['$7.85 + $6.90 = $14.75.', '$14.75 + $5.50 = $20.25.', 'Together they cost $20.25.'],
      src=['Can she buy the book, the puzzle and the water bottle? Show how you know.']),
    I(id='3b-things', tier='core', no='3(b)', label='3(b) things', type='text', skill='money and budgets', accept=name_list_forms([['Book'], ['Pen set', 'pen sets', 'pens', 'pen'], ['Puzzle']]), shown='Book, Pen set, Puzzle',
      svg=price_list_fig(PRICES, 'Prices'),
      q='Siti has $20 and buys 3 different things. Which 3 things spend as much of her $20 as she can, without going over? Type the three names.',
      check=lambda: ', '.join(n for n, _ in PRICES if n in best_sets()[0][0]) if len(best_sets()[0]) == 1 else None,
      hint='Try different sets of 3 things. Which set costs the most without going over $20?',
      steps=['Add the prices of different sets of 3. The book, the puzzle and the water bottle cost $20.25: too much.', 'The book, the pen set and the puzzle cost $7.85 + $4.60 + $6.90 = $19.35.', 'Every other set that fits in $20 costs less (the next best is the book, the pen set and the water bottle at $17.95). So she should buy the book, the pen set and the puzzle.'],
      src=['Which 3 things should she buy to spend as much of her $20 as she can? How much change will she get?']),
    I(id='3b-change', tier='core', no='3(b)', label='3(b) change', type='number', skill='money and budgets', answer=65, dollars_ok=True, svg=price_list_fig(PRICES, 'Prices'),
      q='Siti buys the 3 things that spend as much of her $20 as she can, without going over. How many cents change does she get? Type the number.',
      check=lambda: BUDGET - best_sets()[1],
      hint='Find which 3 things first. Then take their cost away from $20.',
      steps=['The best 3 things are the book, the pen set and the puzzle: $7.85 + $4.60 + $6.90 = $19.35.', '$20 - $19.35 = 65¢.', 'She gets 65¢ change.'],
      src=['How much change will she get?']),

    I(id='4a-715', tier='core', no='4(a)', label='4(a) 7:15', type='fields', skill='the 24-hour clock', answer=[7, 15], frame='Hours: {f1}   Minutes: {f2}', svg=strip_fig(),
      q='The 24-hour clock. Write 7:15 am in 24-hour time. Type the hours and the minutes.', check=lambda: list(to24(7, 15, False)),
      hint='Find 7:15 am on the am row of the strip.',
      steps=['The morning (am) hours are on the top row of the strip.', '7:15 am is 07:15 on the 24-hour clock.', 'The answer is 07:15.'],
      src=['(if time) The 24-hour clock. After 12 noon, add 12 to the hour.', 'Fill in the table. The top row is 12-hour time; the bottom row is 24-hour time.']),
    I(id='4a-340', tier='core', no='4(a)', label='4(a) 3:40', type='fields', skill='the 24-hour clock', answer=[15, 40], frame='Hours: {f1}   Minutes: {f2}', svg=strip_fig(),
      q='Write 3:40 pm in 24-hour time. Type the hours and the minutes.', check=lambda: list(to24(3, 40, True)),
      hint='After noon the 24-hour clock keeps counting past 12: 1 pm is 13:00. Use the strip.',
      steps=['After 12 noon, add 12 to the hour: 3 + 12 = 15.', '3:40 pm is 15:40 on the 24-hour clock.', 'The answer is 15:40.'],
      src=['Fill in the table. The top row is 12-hour time; the bottom row is 24-hour time.']),
    I(id='4a-2005', tier='core', no='4(a)', label='4(a) 20:05', type='text', skill='the 24-hour clock', accept=twelve_forms(8, 5), shown='8:05 pm', svg=strip_fig(),
      q='Write 20:05 in 12-hour time. Say am or pm. Type the time.', check=lambda: (lambda h, m, ap: f'{h}:{m:02d} {ap}')(*to12(20, 5)),
      hint='20:05 is after 12 noon. How many hours is it after 12:00?',
      steps=['20:05 is after noon, so it is pm.', 'Take 12 away from the hour: 20 - 12 = 8.', '20:05 is 8:05 pm.'],
      src=['Fill in the table. The top row is 12-hour time; the bottom row is 24-hour time.']),
    I(id='4a-1230', tier='core', no='4(a)', label='4(a) 12:30', type='fields', skill='the 24-hour clock', answer=[12, 30], frame='Hours: {f1}   Minutes: {f2}', svg=strip_fig(),
      q='Write 12:30 pm in 24-hour time. Type the hours and the minutes.', check=lambda: list(to24(12, 30, True)),
      hint='Find 12:30 pm on the pm row of the strip. It is just after noon.',
      steps=['12:30 pm is half an hour after noon.', 'It stays 12:30 on the 24-hour clock. (Add 12 to the hour only for 1 pm and later.)', 'The answer is 12:30.'],
      src=['Fill in the table. The top row is 12-hour time; the bottom row is 24-hour time.']),
    I(id='4b-yn', tier='core', no='4(b)', label='4(b) yes/no', type='choice', skill='the 24-hour clock', options=['Yes', 'No'], answer='No', svg=strip_fig(),
      q='Siti says, “17:00 is 7 pm.” Is she right?', check=lambda: 'Yes' if to12(17, 0)[:2] == (7, 0) else 'No',
      hint='On the strip, how many hours after 12:00 is 17:00?',
      steps=['After noon the hours carry on: 13:00 is 1 pm, 14:00 is 2 pm, 15:00 is 3 pm.', '17 - 12 = 5, so 17:00 is 5 pm.', 'Siti is not right.'],
      src=['Siti says, “17:00 is 7 pm.” Is she right? Explain.']),
    I(id='4b-why', tier='core', no='4(b)', label='4(b) explain', type='selfcheck', open=True, marking_mode='self', skill='explaining the 24-hour clock', svg=strip_fig(),
      q='Explain how to change 17:00 into a 12-hour time. Write your idea, then compare with the answer shown.', check=lambda: list(to12(17, 0)),
      hint='Look at the pm row of the strip. How many hours is 17:00 after 12:00?',
      steps=['After 12 noon the 24-hour clock keeps counting: 13:00 is 1 pm, 14:00 is 2 pm, and so on.', 'To change 17:00, take 12 away from 17: 17 - 12 = 5.', '17:00 is 5 pm.'],
      src=['Siti says, “17:00 is 7 pm.” Is she right? Explain.']),

    I(id='5a', tier='core', no='5(a)', label='5(a)', type='fields', skill='time lines and duration', answer=[1, 25], frame='{f1} h {f2} min',
      svg=time_line(933, 1042, [(pm(3, 45), '3:45 pm', 0), (pm(4, 0), '4:00', 1), (pm(5, 0), '5:00', 0), (pm(5, 10), '5:10 pm', 1)], [(pm(3, 45), pm(4, 0), '? min'), (pm(4, 0), pm(5, 0), '? h'), (pm(5, 0), pm(5, 10), '? min')],
                    label='A time line from 3:45 pm to 5:10 pm with the o’clock times 4:00 and 5:00 marked'),
      q='Trick 2: use a time line and jump to the next o’clock. Ali’s swimming lesson starts at 3:45 pm and ends at 5:10 pm. How long is it?',
      check=lambda: list(hm(pm(5, 10) - pm(3, 45))),
      hint='Jump from 3:45 pm to 4:00. How many minutes is that? Then jump to 5:00, then to 5:10.',
      steps=['3:45 pm to 4:00 pm is 15 minutes.', '4:00 pm to 5:00 pm is 1 hour.', '5:00 pm to 5:10 pm is 10 minutes.', '15 min + 1 h + 10 min = 1 h 25 min.'],
      src=['Ali’s swimming lesson starts at 3:45 pm and ends at 5:10 pm. How long is it?']),
    I(id='5b', tier='core', no='5(b)', label='5(b)', type='fields', skill='time lines and end times', answer=[5, 25], frame='Ends at   Hours: {f1}   Minutes: {f2}   (pm)',
      svg=time_line(983, 1057, [(pm(4, 35), '4:35 pm', 0), (pm(5, 0), '5:00', 0), (pm(5, 25), '?', 0)], [(pm(4, 35), pm(5, 0), '? min'), (pm(5, 0), pm(5, 25), '? min')],
                    label='A time line starting at 4:35 pm with 5:00 marked and a question mark at the end of the lesson'),
      q='Mei’s piano lesson starts at 4:35 pm and lasts 50 minutes. When does it end? Type the time.',
      check=lambda: [(pm(4, 35) + 50) // 60 - 12, (pm(4, 35) + 50) % 60],
      hint='Jump from 4:35 pm to 5:00. How many minutes is that? How many of the 50 minutes are left?',
      steps=['4:35 pm to 5:00 pm is 25 minutes.', '50 - 25 = 25 minutes are left to jump.', '5:00 pm + 25 minutes = 5:25 pm. The lesson ends at 5:25 pm.'],
      src=['Mei’s piano lesson starts at 4:35 pm and lasts 50 minutes. When does it end?']),
    I(id='5c', tier='core', no='5(c)', label='5(c)', type='fields', skill='time lines and start times', answer=[7, 25], frame='Started at   Hours: {f1}   Minutes: {f2}   (pm)',
      svg=time_line(1128, 1290, [(pm(7, 0), '7:00', 0), (pm(8, 0), '8:00', 0), (pm(9, 0), '9:00', 0), (pm(9, 15), '9:15 pm', 1)], [(pm(9, 0), pm(9, 15), '? min')],
                    label='A time line ending at 9:15 pm with 7:00, 8:00 and 9:00 marked'),
      q='A film lasts 1 h 50 min. It ends at 9:15 pm. When did it start? Type the time.',
      check=lambda: [(pm(9, 15) - 110) // 60 - 12, (pm(9, 15) - 110) % 60],
      hint='Jump back from 9:15 pm to 9:00 pm, then back 1 hour. How much of the 1 h 50 min is still left to go back?',
      steps=['Go back 15 minutes from 9:15 pm to 9:00 pm.', 'Go back 1 hour to 8:00 pm. That is 1 h 15 min so far, and 1 h 50 min - 1 h 15 min = 35 minutes more to go back.', '8:00 pm - 35 minutes = 7:25 pm. The film started at 7:25 pm.'],
      src=['A film lasts 1 h 50 min. It ends at 9:15 pm. When did it start?']),

    I(id='6-table', tier='core', no='6', label='6 buses', type='text', skill='time lines and timetables', accept=time_list_forms(BUSES[1:]), shown='07:05, 07:30, 07:55, 08:20, 08:45',
      svg=time_line(385, 540, [(BUSES[0], '06:40', 0), (RAVI, '08:15', 0)], [], minor=BUSES[1:], marks=[(RAVI, 'Ravi arrives')], label='A time line from 06:40 with a mark every 25 minutes for the buses and Ravi arriving at 08:15'),
      q='Buses leave the interchange every 25 minutes. The first bus leaves at 06:40. Write the times of the 2nd, 3rd, 4th, 5th and 6th bus, with commas.',
      check=lambda: ', '.join(tm(t) for t in hourly_from(mins(6, 40), 25, 6)[1:]),
      hint='Add 25 minutes each time. It can help to jump to the next o\u2019clock first, then add the minutes that are left.',
      steps=['06:40 + 25 minutes = 07:05 (the 2nd bus).', '07:05 + 25 = 07:30, then 07:30 + 25 = 07:55, then 07:55 + 25 = 08:20, then 08:20 + 25 = 08:45.', 'The buses are at 06:40, 07:05, 07:30, 07:55, 08:20 and 08:45.'],
      src=['Buses leave the interchange every 25 minutes. The first bus leaves at 06:40.']),
    I(id='6a-next', tier='core', no='6(a)', label='6(a) next', type='fields', skill='time lines and timetables', answer=[8, 20], frame='Next bus at   Hours: {f1}   Minutes: {f2}',
      svg=time_line(385, 540, [(BUSES[0], '06:40', 0), (RAVI, '08:15', 0)], [], minor=BUSES[1:], marks=[(RAVI, 'Ravi arrives')], label='A time line from 06:40 with a mark every 25 minutes for the buses and Ravi arriving at 08:15'),
      q='Buses leave the interchange every 25 minutes. The first bus leaves at 06:40. Ravi reaches the interchange at 08:15. When is the next bus?',
      check=lambda: [next_bus(RAVI) // 60, next_bus(RAVI) % 60],
      hint='List the bus times. Which is the first one after 08:15?',
      steps=['The buses leave at 06:40, 07:05, 07:30, 07:55, 08:20 and 08:45.', '08:15 is just before 08:20.', 'The next bus is at 08:20.'],
      src=['Ravi reaches the interchange at 08:15. When is the next bus? How long does he wait?']),
    I(id='6a-wait', tier='core', no='6(a)', label='6(a) wait', type='number', skill='time lines and timetables', answer=5,
      q='Buses leave the interchange every 25 minutes. The first bus leaves at 06:40. Ravi reaches the interchange at 08:15. How many minutes does he wait for the next bus? Type the number.',
      check=lambda: next_bus(RAVI) - RAVI,
      hint='Find the next bus time first. How many minutes is it after 08:15?',
      steps=['The next bus after 08:15 is at 08:20.', '08:15 to 08:20 is 5 minutes.', 'Ravi waits 5 minutes.'],
      src=['Ravi reaches the interchange at 08:15. When is the next bus? How long does he wait?']),
    I(id='6b', tier='core', no='6(b)', label='6(b)', type='fields', skill='time lines and timetables', answer=[8, 55], frame='Reaches school at   Hours: {f1}   Minutes: {f2}',
      q='Ravi takes the next bus after 08:15. The bus ride to school takes 35 minutes. When does Ravi reach school? (The buses leave every 25 minutes from 06:40.)',
      check=lambda: [(next_bus(RAVI) + 35) // 60, (next_bus(RAVI) + 35) % 60],
      hint='Find the bus Ravi takes first. Then jump 35 minutes: to the next o’clock, then the minutes that are left.',
      steps=['Ravi takes the 08:20 bus.', '08:20 + 35 minutes: 08:20 + 40 minutes would be 09:00, so 08:20 + 35 minutes is 5 minutes before 09:00.', 'He reaches school at 08:55.'],
      src=['The bus ride to school takes 35 minutes. When does Ravi reach school?']),

    # ================= Investigation (Investigation and look back page, No.8: Find all the ways to pay)
    I(id='I8-swap', tier='invest', no='8 (easy step)', label='Inv easy', type='fields', skill='making a list in order', answer=[2, 4], frame='10¢ = {f1} five-cent coins      20¢ = {f2} five-cent coins',
      q='Ali can swap some five-cent coins for bigger coins. How many five-cent coins is one 10-cent coin worth? How many is one 20-cent coin worth?',
      check=lambda: [count_in(10, 5)[0], count_in(20, 5)[0]],
      hint='Count in 5s up to 10, then up to 20.',
      steps=['Count in 5s: 5, 10. So one 10-cent coin is worth two five-cent coins.', 'Count in 5s: 5, 10, 15, 20. So one 20-cent coin is worth four five-cent coins.', 'The numbers are 2 and 4.'],
      src=['Easy first step: pay 50 cents with ten 5-cent coins. Then swap some of them for 10-cent coins.']),
    I(id='I8a', tier='invest', no='8(a)', label='Inv 8(a)', type='selfcheck', open=False, marking_mode='self', skill='making a list in order',
      sol_fig=lambda g: ways_table_fig(g, 'Every way of paying exactly 50 cents with 20-cent, 10-cent and 5-cent coins: 12 ways'),
      q='Ali pays exactly 50 cents using only 5-cent, 10-cent and 20-cent coins, as many of each as he likes. Find ALL the ways. For each way, write how many 20-cent, 10-cent and 5-cent coins. Then compare with the table shown.',
      check=ways_50,
      hint='Pay 50 cents with ten 5-cent coins. Then swap some of them for 10-cent coins or 20-cent coins. Keep a list so you do not repeat a way.',
      steps=['Go in order: first fix the number of 20-cent coins (two, then one, then none), then the number of 10-cent coins, then fill up with 5-cent coins.', 'The same coins in a different order are the same way.', 'There are 12 ways. They are shown in the table (20-cent, 10-cent, 5-cent): 2, 1, 0; 2, 0, 2; 1, 3, 0; 1, 2, 2; 1, 1, 4; 1, 0, 6; 0, 5, 0; 0, 4, 2; 0, 3, 4; 0, 2, 6; 0, 1, 8; 0, 0, 10.'],
      src=['Ali pays exactly 50 cents using only 5-cent, 10-cent and 20-cent coins. He can use as many of each coin as he likes.', 'Find all the ways. Write each way in the table (how many of each coin).']),
    I(id='I8a-sort', tier='invest', no='8(a)', label='Inv sort', type='fields', skill='making a list in order', answer=[2, 4, 6],
      frame='Two 20-cent coins: {f1} ways      One 20-cent coin: {f2} ways      No 20-cent coins: {f3} ways',
      q='Ali pays exactly 50 cents using only 5-cent, 10-cent and 20-cent coins. Sort the ways by how many 20-cent coins he uses. How many ways use two 20-cent coins? One? None? (Do the list question first.)',
      check=lambda: [len([w for w in ways_50() if w[0] == k]) for k in (2, 1, 0)],
      hint='Take two 20-cent coins first. How much is left to pay? Then try one 20-cent coin, then none.',
      steps=['Two 20-cent coins leave 10 cents: one 10-cent coin, or two 5-cent coins. That is 2 ways.', 'One 20-cent coin leaves 30 cents: three 10-cent coins, two 10-cent coins and two 5-cent coins, one 10-cent coin and four 5-cent coins, or six 5-cent coins. That is 4 ways.', 'No 20-cent coins leave 50 cents: five, four, three, two, one or no 10-cent coins, with 5-cent coins for the rest. That is 6 ways.'],
      src=['Find all the ways. Write each way in the table (how many of each coin).']),
    I(id='I8a-total', tier='invest', no='8(a)', label='Inv total', type='number', skill='making a list in order', answer=12,
      q='Ali pays exactly 50 cents using only 5-cent, 10-cent and 20-cent coins. How many different ways are there altogether? (Do the list question first.) Type the number.',
      check=lambda: len(ways_50()),
      hint='Count your list. The same coins in a different order are one way, so count them once.',
      steps=['The ways with two, one and no 20-cent coins are 2, 4 and 6.', '2 + 4 + 6 = 12.', 'There are 12 different ways.'],
      src=['Find all the ways. Write each way in the table (how many of each coin).']),
    I(id='I8b-few', tier='invest', no='8(b)', label='Inv fewest', type='fields', skill='comparing ways', answer=[2, 1, 0],
      frame=grp('20-cent coins: {f1}      10-cent coins: {f2}      5-cent coins: {f3}'),
      q='Which way of paying 50 cents uses the FEWEST coins? Fill in how many of each coin.',
      check=lambda: list(min(ways_50(), key=coins_used)) if len([w for w in ways_50() if coins_used(w) == min(map(coins_used, ways_50()))]) == 1 else None,
      hint='Big coins use fewer coins. Use as many 20-cent coins as you can first.',
      steps=['Count the coins in each way. Two 20-cent coins and one 10-cent coin make 20 + 20 + 10 = 50 cents with only 3 coins.', 'No other way uses 3 coins or fewer.', 'The fewest is two 20-cent coins, one 10-cent coin and no 5-cent coins.'],
      src=['Which way uses the FEWEST coins? Which uses the MOST?']),
    I(id='I8b-most', tier='invest', no='8(b)', label='Inv most', type='fields', skill='comparing ways', answer=[0, 0, 10],
      frame=grp('20-cent coins: {f1}      10-cent coins: {f2}      5-cent coins: {f3}'),
      q='Which way of paying 50 cents uses the MOST coins? Fill in how many of each coin.',
      check=lambda: list(max(ways_50(), key=coins_used)) if len([w for w in ways_50() if coins_used(w) == max(map(coins_used, ways_50()))]) == 1 else None,
      hint='Small coins use more coins. Which coin is the smallest?',
      steps=['Count the coins in each way. Using only 5-cent coins needs 10 of them.', 'Every other way swaps some 5-cent coins for bigger coins, so it uses fewer than 10 coins.', 'The most is ten 5-cent coins.'],
      src=['Which way uses the FEWEST coins? Which uses the MOST?']),
    I(id='I8c', tier='invest', no='8(c)', label='Inv 8(c)', type='selfcheck', open=True, marking_mode='self', skill='explaining a method',
      q='How do you know you have found all the ways to pay exactly 50 cents? Write your idea, then compare with the answer shown.',
      check=lambda: [len([w for w in ways_50() if w[0] == k]) for k in (2, 1, 0)],
      hint='Did you keep your list in an order, such as by the number of 20-cent coins?',
      steps=['Be organised: fix the number of 20-cent coins first (two, one, then none), then the number of 10-cent coins, then fill up with 5-cent coins.', 'Two 20-cent coins give 2 ways, one 20-cent coin gives 4 ways and no 20-cent coins give 6 ways. That is 12 ways.', 'The same coins in a different order are not a new way, so you never count one twice.'],
      src=['How do you know you have found them all?']),

    # ================= Think harder (workbook Think harder, No.1 to No.4)
    I(id='T1', tier='stretch', no='T1', label='T1', type='fields', skill='volume', answer=[6, 200], frame=grp('{f1} cups      {f2} ml left over'),
      q='A 2 ℓ bottle of juice is poured into cups. Each cup holds 300 ml. How many cups can be filled? How much juice is left over? (1 ℓ = 1000 ml.)',
      check=lambda: list(count_in(ml_of(2), 300)),
      hint='Change 2 ℓ to ml. Then count in 300s: 300, 600, 900 ... Stop before you pass the total.',
      steps=['2 ℓ = 2000 ml.', 'Count in 300s: 300, 600, 900, 1200, 1500, 1800. That is 6 cups. The next one, 2100, is too much.', '2000 - 1800 = 200 ml is left over.'],
      src=['A 2 ℓ bottle of juice is poured into cups. Each cup holds 300 ml. How many cups can be filled? How much juice is left over?']),
    I(id='T2', tier='stretch', no='T2', label='T2', type='fields', skill='time lines and duration', answer=[11, 30], frame='{f1} h {f2} min',
      svg=time_line(520, 1290, [(mins(9, 30), '09:30', 0), (mins(12), '12:00', 0), (mins(15), '15:00', 0), (mins(18), '18:00', 0), (mins(21), '21:00', 0)], [], label='A time line from 09:30 to 21:00'),
      q='A shop opens at 09:30 and closes at 21:00. How long is it open?', check=lambda: list(hm(mins(21) - mins(9, 30))),
      hint='Jump from 09:30 to 10:00. Then count whole hours up to 21:00.',
      steps=['09:30 to 10:00 is 30 minutes.', '10:00 to 21:00 is 11 hours.', '30 min + 11 h = 11 h 30 min.'],
      src=['A shop opens at 09:30 and closes at 21:00. How long is it open?']),
    I(id='T3', tier='stretch', no='T3', label='T3', type='number', skill='mass', answer=200, svg=box_books_fig(),
      q='A box with 4 books weighs 1 kg 50 g. The empty box weighs 250 g. All the books weigh the same. How many g does one book weigh? Type the number.',
      check=lambda: (lambda books: count_in(books, 4)[0] if count_in(books, 4)[1] == 0 else None)(g_of(1, 50) - 250),
      hint='Change 1 kg 50 g to grams. Take the box away. Then share what is left between the 4 books.',
      steps=['1 kg 50 g = 1050 g.', 'Take the empty box away: 1050 - 250 = 800 g for the 4 books.', '800 ÷ 4 = 200, so one book weighs 200 g.'],
      src=['A box with 4 books weighs 1 kg 50 g. The empty box weighs 250 g. All the books weigh the same. How heavy is one book?']),
    I(id='T4', tier='stretch', no='T4', label='T4', type='fields', skill='time and timetables', answer=[7, 55], frame='Bus leaves at   Hours: {f1}   Minutes: {f2}',
      q='Buses leave the interchange every 25 minutes. The first bus leaves at 06:40. The ride to school takes 35 minutes. Ravi must reach school by 08:30. Which is the latest bus he can take? Type the time it leaves.',
      check=lambda: [latest_bus(35, mins(8, 30)) // 60, latest_bus(35, mins(8, 30)) % 60],
      hint='List the bus times, 25 minutes apart. Add 35 minutes to each one. Which is the last that gets him there by 08:30?',
      steps=['The buses leave at 06:40, 07:05, 07:30, 07:55, 08:20 and so on.', 'Add 35 minutes to each: the 07:55 bus arrives at 08:30 (07:55 + 5 min = 08:00, + 30 min = 08:30). The 08:20 bus arrives at 08:55: too late.', 'The latest bus is the 07:55 bus.'],
      src=['Buses leave the interchange every 25 minutes. The first bus leaves at 06:40. The ride to school takes 35 minutes.']),

    # ================= Go further (workbook Go further, No.5 to No.7) and the Extra questions (printed as "Take-home")
    I(id='G5', tier='challenge', no='G5', label='G5', type='number', skill='mass', answer=300, svg=bottle_fig(),
      q='A bottle full of water weighs 1 kg 200 g. After half of the water is poured out, it weighs 750 g. How many g does the empty bottle weigh? Type the number.',
      check=lambda: (lambda half_water: g_of(1, 200) - 2 * half_water)(g_of(1, 200) - 750),
      hint='How much lighter did the bottle get when half of the water was poured out? That is half of the water.',
      steps=['The bottle got lighter by 1200 - 750 = 450 g. That is half of the water.', 'All the water weighs 450 + 450 = 900 g.', 'The empty bottle weighs 1200 - 900 = 300 g.'],
      src=['A bottle full of water weighs 1 kg 200 g. After half of the water is poured out, it weighs 750 g. How heavy is the empty bottle?']),
    I(id='G6', tier='challenge', no='G6', label='G6', type='text', skill='money', accept=money_forms(160), shown='$1.60', svg=pens_files_fig(),
      q='Mei buys 3 pens and 2 files for $9.20. Each file costs 60¢ more than each pen. How much does one pen cost? Type the amount.',
      check=lambda: dollars([p for p in range(1, 920) if 3 * p + 2 * (p + 60) == 920][0]),
      hint='Take away the extra 60¢ for each file. Then all 5 things cost the same as a pen.',
      steps=['Each file costs 60¢ more than a pen, so the 2 files have 2 × 60¢ = $1.20 extra.', '$9.20 - $1.20 = $8.00 pays for 5 things that each cost the same as a pen.', '$8.00 ÷ 5 = $1.60. One pen costs $1.60. (A file costs $2.20.)'],
      src=['Mei buys 3 pens and 2 files for $9.20. Each file costs 60¢ more than each pen. How much does one pen cost?']),
    I(id='G7', tier='challenge', no='G7', label='G7', type='selfcheck', open=True, marking_mode='open', skill='making up a problem',
      q='Make up your own problem about money or time that needs at least 2 steps. Write it, solve it and check it. Then change ONE number and solve it again. What changes in the answer, and why? Swap with a partner.',
      hint='Pick a story you know, like a party or a bus. Write the numbers first, then the question.',
      steps=['Answers vary. Check that the problem needs 2 or more steps, the answer is right, and you can say what changed.', 'Example: "Mei has $20. She buys a $7.85 book and a $5.50 water bottle. Can she also buy 3 stickers at $2.35 each?" She has $20 - $13.35 = $6.65 left, but 3 stickers cost $7.05, so she is 40¢ short.', 'Change one number: if Mei had $25 she would have $11.65 left, enough for the stickers, with $4.60 change.'],
      src=['Make up your own problem about money or time that needs at least 2 steps. Write it, solve it and check it. Then change ONE number and solve it again.']),
    I(id='TH-a', tier='challenge', no='Extra (a)', label='Extra (a)', type='number', skill='changing units', answer=80,
      q=EXTRA + '1 hour 20 minutes = ? minutes. Type the number.', check=lambda: mins(1, 20),
      hint='How many minutes are in 1 hour?',
      steps=['1 hour = 60 minutes.', '60 + 20 = 80.', '1 hour 20 minutes = 80 minutes.'],
      src=['1 hour 20 minutes = __ minutes']),
    I(id='TH-b', tier='challenge', no='Extra (b)', label='Extra (b)', type='text', skill='the 24-hour clock', accept=twentyfour_forms(14, 0), shown='14:00',
      q=EXTRA + 'Write 2:00 pm in 24-hour time.', check=lambda: (lambda h, m: f'{h:02d}:{m:02d}')(*to24(2, 0, True)),
      hint='After 12 noon, the 24-hour clock keeps counting: 1 pm is 13:00.',
      steps=['2:00 pm is after noon, so add 12 to the hour: 2 + 12 = 14.', '2:00 pm is 14:00.'],
      src=['2:00 pm in 24-hour time is __']),
]

for _d in ITEMS:
    if _d['type'] == 'selfcheck' and 'marking_mode' not in _d:
        _d['marking_mode'] = 'self'
assert best_sets() == ([('Book', 'Pen set', 'Puzzle')], 1935)
assert sum(PRICE[n] for n in ['Book', 'Puzzle', 'Water bottle']) == 2025 and sorted(c for _, c in sets_of_three() if c <= BUDGET)[-2] == 1795
assert len(ways_50()) == 12 and min(map(coins_used, ways_50())) == 3 and max(map(coins_used, ways_50())) == 10

# the 12 ways equal the printed model in p3/gifted.json (lesson 9) and the checker found no other
import json as _json
_G = _json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..', 'p3', 'gifted.json'), encoding='utf-8'))
_model = _G['9']['inv']['model']
_printed = [tuple(int(x) for x in m.split(',')) for m in re.findall(r'\b(\d,\d,\d{1,2})\b', _model.split('Fewest')[0])]
assert _printed == ways_50(), (_printed, ways_50())


# ---------------------------------------------------------------- variant families (template + independent oracle over EVERY combination)
def _tt(env):
    return env['bx'] + env['b'] * env['bk']


for _bx in (150, 250, 350):                    # the box variants: every total is a whole number of kg plus a non-zero number of g, at least 1 kg
    for _b in (4, 5):
        for _bk in (250, 300, 400):
            assert _bx + _b * _bk >= 1000 and (_bx + _b * _bk) % 1000 != 0


def _hm_fields(t):
    return dict(f1=t // 60, f2=t % 60)


VARIANTS = {
    '1a': dict(
        base=dict(a=2),
        tpl=dict(vars=dict(a=[3, 4, 5, 6, 7, 8, 9]), q='Change to ONE unit. 1 m = 100 cm. How many cm is {a} m? Type the number.', answer='100*a',
                 hint='1 m is 100 cm. How many hundreds are there in {a} m?', steps=['1 m is 100 cm.', '{a} m is {a} hundreds.', '{a} m = {ans} cm.']),
        oracle=lambda e: cm_of(e['a'])),
    '1b': dict(
        base=dict(a=3),
        tpl=dict(vars=dict(a=[2, 4, 5, 6, 7, 8, 9]), q='Change to ONE unit. 1 kg = 1000 g. How many g is {a} kg? Type the number.', answer='1000*a',
                 hint='1 kg is 1000 g. How many thousands are there in {a} kg?', steps=['1 kg is 1000 g.', '{a} kg is {a} thousands.', '{a} kg = {ans} g.']),
        oracle=lambda e: g_of(e['a'])),
    '1c': dict(
        base=dict(a=3, b=6),
        tpl=dict(vars=dict(a=[2, 4, 5, 6, 7, 8, 9], b=[4, 5, 8, 25, 40, 75]), q='Change to ONE unit. 1 m = 100 cm. How many cm is {a} m {b} cm? Type the number.', answer='100*a+b',
                 hint='Write {a} m as cm first. Then add the {b} cm.', steps=['{a} m = {a} hundreds of cm.', 'Add the {b} cm.', '{a} m {b} cm = {ans} cm.']),
        oracle=lambda e: cm_of(e['a'], e['b'])),
    '1d': dict(
        base=dict(a=2, b=450),
        tpl=dict(vars=dict(a=[3, 4, 5, 6, 7], b=[25, 50, 75, 450, 800]), q='Change to ONE unit. 1 kg = 1000 g. How many g is {a} kg {b} g? Type the number.', answer='1000*a+b',
                 hint='Write {a} kg as grams first. Then add the {b} g.', steps=['{a} kg = {a} thousands of g.', 'Add the {b} g.', '{a} kg {b} g = {ans} g.']),
        oracle=lambda e: g_of(e['a'], e['b'])),
    '1e': dict(
        base=dict(l=4, m=80),
        tpl=dict(vars=dict(l=[2, 3, 5, 6, 7, 9], m=[5, 40, 80, 250, 600]), derive=dict(N='1000*l+m'),
                 q='Change {N} ml into litres and millilitres. (1 ℓ = 1000 ml.) Fill in the boxes.', frame='{N} ml = {f1} ℓ {f2} ml', answers=dict(f1='l', f2='m'),
                 hint='How many whole 1000 ml fit into {N} ml? How much is left over?', steps=['Take out the whole thousands: that is the litres.', 'What is left over is the millilitres.', 'The numbers are {ans}.']),
        oracle=lambda e: dict(zip(('f1', 'f2'), count_in(ml_of(e['l'], e['m']), 1000)))),
    '1f': dict(
        base=dict(R=3, k=4, L=65),
        tpl=dict(vars=dict(R=[3, 4, 5], k=[2, 3, 4], L=[35, 45, 65, 70]),
                 q='Mei cuts {k} pieces, each {L} cm long, from a ribbon {R} m long. How many cm of ribbon are left? Type the number.', answer='100*R-k*L',
                 hint='Change {R} m to cm first. How much do the {k} pieces use?', steps=['The ribbon is {R} m long. Change it to cm.', 'Add the lengths of the {k} pieces.', 'Take that away from the ribbon: {ans} cm are left.']),
        oracle=lambda e: cm_of(e['R']) - e['k'] * e['L']),
    '4a-715': dict(
        base=dict(hh=7, mm=15),
        tpl=dict(vars=dict(hh=[5, 6, 8, 9, 10, 11], mm=[10, 20, 35, 45, 50]), q='Write {hh}:{mm} am in 24-hour time. Type the hours and the minutes.', frame='Hours: {f1}   Minutes: {f2}', answers=dict(f1='hh', f2='mm'),
                 hint='Find the time on the am row of the strip.', steps=['The morning (am) hours are on the top row of the strip.', 'In the morning the 24-hour time shows the same hour and minutes.', 'The numbers are {ans}.']),
        oracle=lambda e: dict(zip(('f1', 'f2'), to24(e['hh'], e['mm'], False)))),
    '4a-340': dict(
        base=dict(hh=3, mm=40),
        tpl=dict(vars=dict(hh=[1, 2, 4, 5, 6, 7, 8, 9, 10, 11], mm=[10, 15, 20, 45, 50, 55]), q='Write {hh}:{mm} pm in 24-hour time. Type the hours and the minutes.', frame='Hours: {f1}   Minutes: {f2}', answers=dict(f1='hh+12', f2='mm'),
                 hint='After noon the 24-hour clock keeps counting past 12: 1 pm is 13:00.', steps=['After 12 noon, add 12 to the hour.', 'The minutes stay the same.', 'The numbers are {ans}.']),
        oracle=lambda e: dict(zip(('f1', 'f2'), to24(e['hh'], e['mm'], True)))),
    '5a': dict(
        base=dict(sh=3, sm=45, ha=2, em=10),
        tpl=dict(vars=dict(sh=[2, 3, 4], sm=[15, 25, 40, 45, 50], ha=[2, 3], em=[10, 20, 35, 45, 55]), derive=dict(eh='sh+ha', Tt='ha*60+em-sm'),
                 q='Trick 2: use a time line and jump to the next o’clock. A lesson starts at {sh}:{sm} pm and ends at {eh}:{em} pm. How long is it?', frame='{f1} h {f2} min', answers=dict(f1='Tt//60', f2='Tt%60'),
                 hint='Jump from {sh}:{sm} pm to the next o’clock. How many minutes is that? Then jump the whole hours, then the minutes left.',
                 steps=['Jump to the next o’clock, then jump the whole hours, then jump the minutes that are left.', 'Add the jumps.', 'The lesson is {ans} (hours, then minutes).']),
        oracle=lambda e: _hm_fields(pm(e['sh'] + e['ha'], e['em']) - pm(e['sh'], e['sm']))),
    '5b': dict(
        base=dict(sh=4, sm=35, dm=50),
        tpl=dict(vars=dict(sh=[2, 3, 4, 5], sm=[15, 20, 35, 40, 50], dm=[40, 45, 50, 55, 65, 70]),
                 q='A piano lesson starts at {sh}:{sm} pm and lasts {dm} minutes. When does it end? Type the time.', frame='Ends at   Hours: {f1}   Minutes: {f2}   (pm)', answers=dict(f1='(sh*60+sm+dm)//60', f2='(sh*60+sm+dm)%60'),
                 hint='Jump from {sh}:{sm} pm to the next o’clock. How many of the {dm} minutes are left after that?',
                 steps=['Jump to the next o’clock first.', 'Then jump the minutes that are left.', 'The lesson ends at {ans} (hours, then minutes) pm.']),
        oracle=lambda e: _hm_fields(pm(e['sh'], e['sm']) + e['dm'] - 12 * 60)),
    '5c': dict(
        base=dict(eh=9, em=15, dh=1, dm=50),
        tpl=dict(vars=dict(eh=[8, 9, 10], em=[15, 20, 35, 40, 45], dh=[1, 2], dm=[20, 35, 50, 55]),
                 q='A film lasts {dh} h {dm} min. It ends at {eh}:{em} pm. When did it start? Type the time.', frame='Started at   Hours: {f1}   Minutes: {f2}   (pm)', answers=dict(f1='(eh*60+em-dh*60-dm)//60', f2='(eh*60+em-dh*60-dm)%60'),
                 hint='Jump back from {eh}:{em} pm to the o’clock. How much of the {dh} h {dm} min is still left to go back?',
                 steps=['Jump back to the o’clock first, then back the whole hours, then the minutes that are left.', 'Check by counting on from the start.', 'The film started at {ans} (hours, then minutes) pm.']),
        oracle=lambda e: _hm_fields(pm(e['eh'], e['em']) - e['dh'] * 60 - e['dm'] - 12 * 60)),
    'T1': dict(
        base=dict(V=2, c=300),
        tpl=dict(vars=dict(V=[2, 3], c=[350, 700, 900]), derive=dict(N='V*1000'),
                 q='A {V} ℓ bottle of juice is poured into cups. Each cup holds {c} ml. How many cups can be filled? How much juice is left over? (1 ℓ = 1000 ml.)', frame='{f1} cups and {f2} ml left over', answers=dict(f1='N//c', f2='N%c'),
                 hint='Change {V} ℓ to ml. Then count in {c}s. Stop before you pass the total.', steps=['{V} ℓ = {N} ml.', 'Count in {c}s as far as you can without passing {N}.', 'The numbers are {ans}.']),
        oracle=lambda e: dict(zip(('f1', 'f2'), count_in(ml_of(e['V']), e['c'])))),
    'T2': dict(
        base=dict(oh=9, om=30, ch=21, cm=0),
        tpl=dict(vars=dict(oh=[9, 10, 11], om=[15, 30, 45], ch=[18, 19, 20, 21], cm=[10, 20, 40, 50]),
                 q='A shop opens at {oh}:{om} and closes at {ch}:{cm} (24-hour time). How long is it open?', frame='{f1} h {f2} min', answers=dict(f1='((ch*60+cm)-(oh*60+om))//60', f2='((ch*60+cm)-(oh*60+om))%60'),
                 hint='Jump from {oh}:{om} to the next o’clock. Then count whole hours to {ch}:00. Then add the {cm} minutes.', steps=['Jump to the next o’clock.', 'Count the whole hours, then add the minutes after the last o’clock.', 'The shop is open {ans} (hours, then minutes).']),
        oracle=lambda e: _hm_fields(mins(e['ch'], e['cm']) - mins(e['oh'], e['om']))),
    'T3': dict(
        base=dict(b=4, bk=200, bx=250),
        tpl=dict(vars=dict(b=[4, 5], bk=[250, 300, 400], bx=[150, 250, 350]), derive=dict(Tt='bx+b*bk', kg='Tt//1000', g='Tt%1000'),
                 q='A box with {b} books weighs {kg} kg {g} g. The empty box weighs {bx} g. All the books weigh the same. How many g does one book weigh? Type the number.', answer='bk',
                 hint='Change {kg} kg {g} g to grams. Take the box away. Then share what is left between the {b} books.', steps=['{kg} kg {g} g = {Tt} g.', 'Take the empty box away: {Tt} - {bx} g for the books.', 'Share that between {b} books: one book weighs {ans} g.']),
        oracle=lambda e: (lambda books: books // e['b'] if books % e['b'] == 0 else None)(_tt(e) - e['bx'])),
    'G5': dict(
        base=dict(b=300, w=900),
        tpl=dict(vars=dict(b=[200, 300, 400], w=[600, 800, 1000]), derive=dict(F='b+w', H='b+w//2'),
                 q='A bottle full of water weighs {F} g. After half of the water is poured out, it weighs {H} g. How many g does the empty bottle weigh? Type the number.', answer='b',
                 hint='How much lighter did the bottle get when half of the water was poured out? That is half of the water.', steps=['The bottle got lighter by {F} - {H} g. That is half of the water.', 'Double it to find all the water, then take it from {F} g.', 'The empty bottle weighs {ans} g.']),
        oracle=lambda e: (e['b'] + e['w']) - 2 * ((e['b'] + e['w']) - (e['b'] + e['w'] // 2))),
    'TH-a': dict(
        base=dict(h=1, m=20),
        tpl=dict(vars=dict(h=[1, 2, 3, 4], m=[10, 15, 25, 30, 35, 45, 50]), q=EXTRA + '{h} h {m} min = ? minutes. Type the number.', answer='60*h+m',
                 hint='How many minutes are in 1 hour? Count that {h} times.', steps=['1 hour = 60 minutes.', '{h} hours is {h} lots of 60 minutes, then add the {m} minutes.', '{h} h {m} min = {ans} minutes.']),
        oracle=lambda e: mins(e['h'], e['m'])),
}
