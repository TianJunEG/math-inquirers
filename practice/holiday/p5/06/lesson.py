"""Online practice for Level 5 (Primary 5, ages 10 to 12) holiday lesson 6: Rate ("Rate Racers").

The questions are the ones printed in the Level 5 holiday workbook, lesson 6: Start here Q1 to Q6 (p5/content/l6.js, workbook()), the Investigation
(p5/content/inv.js), Think harder A1 to A4 (the first four 'stretch' questions of p5/content/l6.js qbank) and Go further B1 to B3 (the last three
'challenge' questions) and the "Make up your own" prompt (gaps.js), in the printed order, exactly as p5/workbook_html.js prints them.  Every answer is recomputed
by an INDEPENDENT checker below (a minute-by-minute simulation of the machine, taps, printers and candles; a search over every mix of egg boxes; a count of the
half hours in a car park stay; a search over the minutes of two phone plans; exact fractions for the bath), never by copying the printed answer;
build_holiday.py stops if a checker and the printed answer differ.  Every figure is drawn from the same numbers (practice/holiday/p5/p5fig3.py).
"""
import os, sys
HERE_ = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE_, '..', '..'))
sys.path.insert(0, os.path.join(HERE_, '..'))
from hlib import *          # noqa: E402,F401
from p5lib import *         # noqa: E402,F401
import p5fig3 as G          # noqa: E402

META = dict(level=5, lesson=6, key='p5', title='Rate Racers', workbook_title='RATE RACERS', topic='Rate', strand='Rate',
            sources=['p5/content/l6.js', 'p5/content/inv.js', 'p5/content/gaps.js'],
            intro=['A rate tells how much for 1 unit: for 1 minute, for 1 kg, for 1 can. Find the amount for 1 first. Then you can scale up, or divide to find how long. '
                   'When taps or printers work together, their rates add up; a leak takes its rate away.',
                   'Type the number in the box (a unit after the number is fine). Money and litres can have a decimal point, like 6.5. Some questions ask you to list or to explain: '
                   'write your idea, then compare it with the model answer after you submit.'])
ST = 'Rate'
F = Fraction


def D(**k):
    k.setdefault('strand', ST)
    return k


# ---------------------------------------------------------------- checkers: simulations and searches (no formula copied from a printed answer)
def whole(v):
    v = F(v)
    assert v.denominator == 1, v
    return int(v)


def total_after(rate, minutes):
    """Amount made after a number of minutes at a steady rate, added up minute by minute."""
    t = F(0)
    for _ in range(minutes):
        t += F(rate)
    return t


def minutes_to_reach(rate, target):
    """How many whole minutes at this steady rate until the amount is exactly the target (the build stops if it is never exact)."""
    t, m = F(0), 0
    while t < target:
        t += F(rate); m += 1
    assert t == target, (rate, target)
    return m


def simulate_job(job, rates_by_minute):
    """rates_by_minute(m) = the pages printed in minute number m (1, 2, 3 ...). Returns the minutes until exactly `job` pages are done."""
    t, m = 0, 0
    while t < job:
        m += 1
        t += rates_by_minute(m)
    assert t == job, (job, t)
    return m


def half_hours_after_first(start, end):
    """The car park charges the first hour and then each half hour or part of a half hour: how many of those are used between two times (minutes since midnight)."""
    left, n = (end - start) - 60, 0
    while left > 0:
        n += 1; left -= 30
    return n


def parking_cents(start, end, first, per_half):
    return first + per_half * half_hours_after_first(start, end)


def egg_cheapest(need):
    best = None
    for x in range(0, 12):                      # boxes of 10 at 330 cents
        for y in range(0, 12):                  # boxes of 6 at 210 cents
            if 10 * x + 6 * y >= need:
                c = 330 * x + 210 * y
                if best is None or c < best[0]:
                    best = (c, x, y)
    return best


def gym_cost(join, per, visits):
    t = join
    for _ in range(visits):
        t += per
    return t


def cents_per_can(price_cents, cans):
    return F(price_cents, cans)


def ways_for(total, ra, rb):
    """Every (minutes of tap A, minutes of tap B) with whole numbers of minutes (0 allowed) that put in exactly `total` litres."""
    return [(a, b) for a in range(0, total + 1) for b in range(0, total + 1) if a * ra + b * rb == total]


def candles():
    a, b, h = 20, 14, 0
    while a != b:
        a -= 2; b -= 1; h += 1
        assert a > 0 and b > 0
    return h, a


def cats_needed(cats, fish, minutes, fish2, minutes2):
    """Each cat eats at a steady rate. Find the number of cats that eats fish2 in minutes2 (search, exact fractions)."""
    per_cat = F(fish, cats) / minutes            # fish per cat per minute
    found = [c for c in range(1, 1000) if c * per_cat * minutes2 == fish2]
    assert len(found) == 1
    return found[0]


def bath_minutes():
    net = F(1, 12) - F(1, 20)                    # part of the bath filled each minute
    return whole(1 / net)


def phone_same_minutes():
    found = [m for m in range(0, 3000) if 1500 + 10 * m == 25 * m]
    assert len(found) == 1
    return found[0]


TAP_A, TAP_B, CRACK, TANK = 12, 18, 6, 240
START, LEAVE = 9 * 60 + 40, 13 * 60 + 15
EGGS = egg_cheapest(28)
assert EGGS == (960, 1, 3), EGGS
PARK_A3 = parking_cents(10 * 60 + 15, 14 * 60 + 50, 150, 100)
assert PARK_A3 == 950


def _dec(cents):
    return G.dec_text(F(cents, 100))


MONEY = dict(money=True, places=(2,))

ITEMS = [
    # ================= Start here (workbook lesson 6: Q1 to Q6)
    D(id='1a', tier='core', no='1(a) 1 and 5 minutes', label='1(a) 1, 5', type='fields', skill='rate table', answer=[16, 80],
      q='A machine fills 48 bottles every 3 minutes.\nComplete the rate table. First the 1 minute and 5 minute columns.', svg=G.rate_table(),
      frame='In 1 minute: {f1} bottles     In 5 minutes: {f2} bottles', check=lambda: [whole(total_after(F(48, 3), 1)), whole(total_after(F(48, 3), 5))],
      hint='The machine fills 48 bottles in 3 minutes. How many bottles does it fill in just 1 minute? Then use that for 5 minutes.',
      steps=['48 bottles in 3 minutes means 48 ÷ 3 = 16 bottles in 1 minute.', 'In 5 minutes: 5 × 16 = 80 bottles.'],
      src=['A machine fills 48 bottles every 3 minutes. (a) Complete the rate table.']),
    D(id='1a2', tier='core', no='1(a) 160 and 12', label='1(a) 160, 12', type='fields', skill='rate table', answer=[10, 192],
      q='A machine fills 48 bottles every 3 minutes.\nComplete the rate table. Now the 160 bottles and 12 minute columns.', svg=G.rate_table(),
      frame='Time for 160 bottles (minutes): {f1}     In 12 minutes: {f2} bottles', check=lambda: [minutes_to_reach(F(48, 3), 160), whole(total_after(F(48, 3), 12))],
      hint='Work with the bottles filled in 1 minute. How many minutes fill 160 bottles? How many bottles in 12 minutes?',
      steps=['In 1 minute the machine fills 48 ÷ 3 = 16 bottles.', '160 bottles: 160 ÷ 16 = 10 minutes.', '12 minutes: 12 × 16 = 192 bottles.'],
      sol_fig=lambda f: G.rate_table([(1, 16), (3, 48), (5, 80), (10, 160), (12, 192)]),
      src=['A machine fills 48 bottles every 3 minutes. (a) Complete the rate table.']),
    D(id='1b', tier='core', no='1(b)', type='text', skill='rate and time', accept=['9.25 a.m.', '9.25 am', '9.25am', '9.25 a.m', '9:25 a.m.', '9:25 am', '9:25am', '9:25 a.m', '9.25', '9:25'], shown='9.25 a.m.',
      q='A machine fills 48 bottles every 3 minutes. It starts at 9.00 a.m.\nAt what time has it filled 400 bottles? (Type the time, like 8.05 a.m.)',
      check=lambda: '%d.%02d a.m.' % divmod(9 * 60 + minutes_to_reach(F(48, 3), 400), 60),
      hint='How many minutes does the machine need to fill 400 bottles? Then add those minutes to 9.00 a.m.',
      steps=['The machine fills 16 bottles in 1 minute (48 ÷ 3).', '400 ÷ 16 = 25 minutes.', '25 minutes after 9.00 a.m. is 9.25 a.m.'],
      src=['The machine starts at 9.00 a.m. At what time has it filled 400 bottles?']),

    D(id='2s', tier='core', no='2 Start here', label='2 start', type='fields', skill='price of one', answer=[70],
      q='Three shops sell the same can of drink.\nStart here: Shop A sells 6 cans for $4.20. How many cents does 1 can cost? (Type just the number.)', svg=G.shops(),
      frame='1 can costs $4.20 ÷ 6 = {f1}¢', check=lambda: [whole(cents_per_can(420, 6))],
      hint='Change $4.20 into cents. Then share it equally between the 6 cans.',
      steps=['$4.20 is 420 cents.', '420 ÷ 6 = 70, so 1 can costs 70¢ at Shop A.'],
      src=['Shop A, 6 cans for $4.20, so 1 can costs $4.20 ÷ 6 = ______¢.']),
    D(id='2a', tier='core', no='2(a)', type='fields', skill='price of one', answer=[70, 73, 65],
      q='Three shops sell the same can of drink.\nFind the price of 1 can at each shop, in cents. (Type just the numbers.)', svg=G.shops(),
      frame='Shop A: {f1}¢     Shop B: {f2}¢     Shop C: {f3}¢',
      check=lambda: [whole(cents_per_can(420, 6)), whole(cents_per_can(292, 4)), whole(cents_per_can(780, 10 + 2))],
      hint='Share each price by the number of cans. Some deals give extra cans: count every can you really get.',
      steps=['Shop A: 420 ÷ 6 = 70¢. Shop B: $2.92 is 292¢, and 292 ÷ 4 = 73¢.', 'Shop C: 10 cans and 2 free make 12 cans for $7.80. 780 ÷ 12 = 65¢.', 'So 1 can costs 70¢ at A, 73¢ at B and 65¢ at C.'],
      src=['Price of 1 can:']),
    D(id='2b', tier='core', no='2(b)', type='choice', skill='best buy', options=['Shop A', 'Shop B', 'Shop C'], answer='Shop C',
      q='Three shops sell the same can of drink.\nWhich shop is the best buy?', svg=G.shops(),
      check=lambda: min((('Shop A', cents_per_can(420, 6)), ('Shop B', cents_per_can(292, 4)), ('Shop C', cents_per_can(780, 12))), key=lambda p: p[1])[0],
      hint='The best buy is the shop where 1 can costs the least. Count every can you get.',
      steps=['The price of 1 can is 70¢ at A, 73¢ at B and 65¢ at C.', 'Shop C is the best buy, because 65¢ is the least. The free cans count: the deal gives 12 cans, not 10.'],
      src=['Which shop is the best buy?']),

    D(id='3a', tier='core', no='3(a)', type='number', skill='time to fill with one tap', answer=20,
      q='An empty tank holds 240 ℓ. Only tap A is turned on (ignore the crack).\nHow long does it take to fill the tank? (Type the number of minutes.)', svg=G.tank_taps(),
      check=lambda: minutes_to_reach(TAP_A, TANK),
      hint='Read how many litres tap A puts in each minute. How many of those minutes fill 240 ℓ?',
      steps=['Tap A puts in 12 ℓ a minute.', '240 ÷ 12 = 20.', 'Tap A alone fills the tank in 20 minutes.'],
      src=['An empty tank holds 240 ℓ.', 'Only tap A is turned on. How long does it take to fill the tank?']),
    D(id='3b', tier='core', no='3(b)', type='number', skill='rates add', answer=8,
      q='An empty tank holds 240 ℓ. Both taps are turned on (ignore the crack for this part).\nHow long does it take to fill the tank now? (Type the number of minutes.)', svg=G.tank_taps(),
      check=lambda: minutes_to_reach(TAP_A + TAP_B, TANK),
      hint='Both taps are on, so add what they put in each minute. Then ask how many of those minutes make 240 ℓ.',
      steps=['Together the taps put in 12 + 18 = 30 ℓ a minute.', '240 ÷ 30 = 8.', 'Both taps fill the tank in 8 minutes.'],
      src=['Both taps are turned on. How long does it take now?']),
    D(id='3c', tier='core', no='3(c)', type='number', skill='rates with a leak', answer=10,
      q='An empty tank holds 240 ℓ. Both taps are on, and the crack lets out 6 ℓ a minute.\nHow long does it take to fill the tank? (Type the number of minutes.)', svg=G.tank_taps(),
      check=lambda: minutes_to_reach(TAP_A + TAP_B - CRACK, TANK),
      hint='The crack lets water out. How many litres stay in the tank each minute?',
      steps=['Each minute 12 + 18 = 30 ℓ go in and 6 ℓ go out, so 30 − 6 = 24 ℓ stay in.', '240 ÷ 24 = 10.', 'With the crack, the tank takes 10 minutes to fill.'],
      src=['Both taps are on, and the crack lets out 6 ℓ a minute. How long to fill the tank?']),

    D(id='4a', tier='core', no='4(a)', type='number', skill='printers working together', answer=18,
      q='Printer P prints 30 pages a minute. Printer Q prints 20 pages a minute. A job has 900 pages.\nBoth printers start together. How long do they take to print the job? (Type the number of minutes.)',
      check=lambda: simulate_job(900, lambda m: 30 + 20),
      hint='How many pages do the two printers print together in 1 minute? Then ask how many minutes make 900 pages.',
      steps=['Together they print 30 + 20 = 50 pages a minute.', '900 ÷ 50 = 18.', 'They take 18 minutes.'],
      src=['Printer P prints 30 pages a minute. Printer Q prints 20 pages a minute. A job has 900 pages.', 'Both printers start together. How long do they take to print the job?']),
    D(id='4b', tier='core', no='4(b)', type='number', skill='one printer starts alone', answer=20,
      q='Printer P prints 30 pages a minute. Printer Q prints 20 pages a minute. A job has 900 pages.\nInstead, P starts alone. After 5 minutes, Q joins in. How long does the whole job take from the start? (Type the number of minutes.)',
      svg=G.printer_bar(), check=lambda: simulate_job(900, lambda m: 30 if m <= 5 else 30 + 20),
      sol_fig=lambda t: G.printer_bar((5, 150, 15, 750, t, 900)),
      hint='How many pages has P printed alone in the first 5 minutes? How many pages are left for the two printers together?',
      steps=['In the first 5 minutes P prints 5 × 30 = 150 pages alone.', '900 − 150 = 750 pages are left. Together the printers print 50 pages a minute, so 750 ÷ 50 = 15 minutes.', 'The whole job takes 5 + 15 = 20 minutes from the start.'],
      src=['Instead, P starts alone. After 5 minutes, Q joins in. How long does the whole job take from the start?']),

    D(id='5s', tier='core', no='5 Start here', label='5 start', type='number', skill='half hours or part', answer=6,
      q='Look at the car park sign and the time line. Ali’s car is in the car park from 9.40 a.m. to 1.15 p.m.\nStart here: after the first hour, how many half hours is his car there? A part of a half hour counts. (Type the number.)',
      svg=G.car_park(), check=lambda: half_hours_after_first(START, LEAVE),
      hint='Count the half hours on the time line after the first hour. Does Ali leave exactly at the end of a half hour, or part-way through one?',
      steps=['The first hour is from 9.40 a.m. to 10.40 a.m. After that come the half hours.', 'Ali leaves at 1.15 p.m., which is 5 minutes into the half hour from 1.10 to 1.40. A part of a half hour counts as a whole one.',
             'Count the half hours from 10.40 to 1.40: there are 6.'],
      sol_fig=lambda t: G.car_park(True),
      src=['circle every half hour that Ali’s car is in the car park on the time line (a part of a half hour counts). Count them.']),
    D(id='5a', tier='core', no='5(a)', type='text', skill='car park charges', accept=G.dec_accepts(F(480, 100), **MONEY), shown='4.80',
      q='Look at the car park sign.\nAli parks from 9.40 a.m. to 1.15 p.m. How much does he pay? (Type the number of dollars, like 3.50.)', svg=G.car_park(),
      check=lambda: _dec(parking_cents(START, LEAVE, 120, 60)),
      hint='Pay the first hour, then 60¢ for each half hour or part of a half hour. How many of those did Ali use?',
      steps=['The first hour costs $1.20.', 'After that Ali’s car is there for 6 half hours (the last one only in part), and each costs 60¢: 6 × 60¢ = $3.60.', '$1.20 + $3.60 = $4.80.'],
      src=['Ali parks from 9.40 a.m. to 1.15 p.m. How much does he pay?']),

    D(id='6a1', tier='core', no='6(a) Gym A', label='6(a) A', type='fields', skill='price plan table', answer=[50, 70, 90],
      q='Gym A charges $30 to join and then $4 for each visit.\nComplete the table: how much does Gym A cost for 5, 10 and 15 visits? (Type the number of dollars.)',
      frame='5 visits ($): {f1}     10 visits ($): {f2}     15 visits ($): {f3}', check=lambda: [gym_cost(30, 4, v) for v in (5, 10, 15)],
      hint='Pay the joining fee once. Then add the cost of each visit.',
      steps=['5 visits: $30 + 5 × $4 = $50.', '10 visits: $30 + 10 × $4 = $70.', '15 visits: $30 + 15 × $4 = $90.'],
      src=['Gym A charges $30 to join and then $4 for each visit.', 'Complete the table.']),
    D(id='6a2', tier='core', no='6(a) Gym B', label='6(a) B', type='fields', skill='price plan table', answer=[35, 70, 105],
      q='Gym B has no joining fee and charges $7 for each visit.\nComplete the table: how much does Gym B cost for 5, 10 and 15 visits? (Type the number of dollars.)',
      frame='5 visits ($): {f1}     10 visits ($): {f2}     15 visits ($): {f3}', check=lambda: [gym_cost(0, 7, v) for v in (5, 10, 15)],
      hint='There is nothing to pay to join. Each visit costs the same.',
      steps=['5 visits: 5 × $7 = $35.', '10 visits: 10 × $7 = $70.', '15 visits: 15 × $7 = $105.'],
      src=['Gym B has no joining fee and charges $7 for each visit.', 'Complete the table.']),
    D(id='6b', tier='core', no='6(b)', type='number', skill='comparing plans', answer=10,
      q='Gym A charges $30 to join and then $4 for each visit. Gym B has no joining fee and charges $7 for each visit.\nFor how many visits do the two gyms cost the same?',
      check=lambda: [n for n in range(1, 200) if gym_cost(30, 4, n) == gym_cost(0, 7, n)][0],
      hint='Compare the two costs as the visits go up. One gym costs more to start with, but its cost grows more slowly. When do the two costs meet?',
      steps=['Gym A costs $3 less for each visit (7 − 4 = 3), but it costs $30 to join.', 'The $30 is made up after 30 ÷ 3 = 10 visits.', 'After 10 visits both cost $70.'],
      src=['For how many visits do the two gyms cost the same?']),
    D(id='6c1', tier='core', no='6(c) which gym', label='6(c) which', type='choice', skill='comparing plans', options=['Gym A', 'Gym B'], answer='Gym A',
      q='Gym A charges $30 to join and then $4 for each visit. Gym B has no joining fee and charges $7 for each visit.\nSiti plans to go 14 times. Which gym is cheaper for her?',
      check=lambda: 'Gym A' if gym_cost(30, 4, 14) < gym_cost(0, 7, 14) else 'Gym B',
      hint='Work out what each gym costs for 14 visits. Which is less?',
      steps=['Gym A: $30 + 14 × $4 = $86.', 'Gym B: 14 × $7 = $98.', 'Gym A is cheaper for 14 visits.'],
      src=['Siti plans to go 14 times. Which gym is cheaper for her, and by how much?']),
    D(id='6c2', tier='core', no='6(c) how much', label='6(c) amount', type='number', skill='comparing plans', answer=12,
      q='Gym A charges $30 to join and then $4 for each visit. Gym B has no joining fee and charges $7 for each visit.\nSiti plans to go 14 times. The cheaper gym costs how many dollars less than the other? (Type the number of dollars.)',
      check=lambda: abs(gym_cost(30, 4, 14) - gym_cost(0, 7, 14)),
      hint='Work out what each gym costs for 14 visits. Then find the difference.',
      steps=['Gym A: $30 + 14 × $4 = $86. Gym B: 14 × $7 = $98.', '$98 − $86 = $12.'],
      src=['Siti plans to go 14 times. Which gym is cheaper for her, and by how much?']),

    # ================= Investigation: Find all the ways
    D(id='C0', tier='invest', no='C (easy first step)', label='C easy', type='fields', skill='working out the rest', answer=[12, 12, 4],
      q='Find all the ways.\nTap A puts 2 litres a minute into an empty tank. Tap B puts 3 litres a minute. The tank needs exactly 24 litres.\nEasy first step: tap A runs for 6 minutes.',
      frame='Litres from tap A: {f1}     Litres still needed: {f2}     Minutes of tap B: {f3}',
      check=lambda: [whole(total_after(2, 6)), 24 - whole(total_after(2, 6)), minutes_to_reach(3, 24 - whole(total_after(2, 6)))],
      hint='Tap A puts in 2 litres each minute. How many litres is that in 6 minutes? How many litres does the tank still need, and how many minutes of tap B give that?',
      steps=['Tap A: 6 × 2 = 12 litres go in.', 'The tank needs 24 − 12 = 12 more litres.', 'Tap B puts in 3 litres a minute, so 12 ÷ 3 = 4 minutes.'],
      src=['Easy first step: tap A runs for 6 minutes. How many litres go in? How many litres are still needed, and how many minutes of tap B give that? Then do part (a).']),
    D(id='Ca', tier='invest', no='C(a) list', label='C(a) list', type='selfcheck', open=False, skill='listing all the ways', facts=ways_for(24, 2, 3),
      q='Tap A puts 2 litres a minute into an empty tank and tap B puts 3 litres a minute. The taps are used one at a time, each for a whole number of minutes (0 is allowed).\n'
        'Find ALL the ways to put exactly 24 litres into the tank. Make a table of the minutes on A and on B, then compare it with the model answer.',
      check=lambda: ways_for(24, 2, 3),
      hint='Start with tap A for 12 minutes and tap B for 0. Then change the minutes step by step, keeping the total at 24 litres. What changes each time?',
      steps=['The ways (minutes on tap A, minutes on tap B): ' + ', '.join(f'({a}, {b})' for a, b in ways_for(24, 2, 3)) + '.',
             'Each time tap B runs 2 minutes longer, tap A runs 3 minutes less: 6 litres are swapped.', 'A good answer is a table in order, and says why each way is different.'],
      src=['Tap A puts 2 litres a minute into an empty tank. Tap B puts 3 litres a minute. The taps are used ONE AT A TIME, each for a whole number of minutes (0 is allowed). Find ALL the ways to put exactly 24 litres into the tank. Make a table.']),
    D(id='Ca2', tier='invest', no='C(a) how many', label='C(a) count', type='number', skill='counting all the ways', answer=5,
      q='Tap A puts 2 litres a minute into an empty tank and tap B puts 3 litres a minute. The taps are used one at a time, each for a whole number of minutes (0 is allowed).\nHow many different ways put exactly 24 litres into the tank?',
      check=lambda: len(ways_for(24, 2, 3)),
      hint='Make a table of the minutes on tap A and the minutes on tap B, and count the rows.',
      steps=['The ways are ' + ', '.join(f'({a}, {b})' for a, b in ways_for(24, 2, 3)) + '.', 'That is 5 ways.'],
      src=['Find ALL the ways']),
    D(id='Ca3', tier='invest', no='C(a) one way', label='C(a) B 6', type='number', skill='using the table', answer=3,
      q='Tap A puts 2 litres a minute into an empty tank and tap B puts 3 litres a minute. The taps are used one at a time. Together they put in exactly 24 litres.\n'
        'In one of the ways, tap B runs for 6 minutes. For how many minutes does tap A run? (Type the number of minutes.)',
      check=lambda: [a for a, b in ways_for(24, 2, 3) if b == 6][0],
      hint='How many litres does tap B put in during 6 minutes? How many litres are left for tap A, and how long is that?',
      steps=['Tap B puts in 6 × 3 = 18 litres.', '24 − 18 = 6 litres are left for tap A, which puts in 2 litres a minute.', '6 ÷ 2 = 3, so tap A runs for 3 minutes.'],
      src=['Find ALL the ways']),
    D(id='Cb', tier='invest', no='C(b) shortest', label='C(b) short', type='fields', skill='comparing the ways', answer=[0, 8],
      q='Tap A puts 2 litres a minute and tap B puts 3 litres a minute. The taps are used one at a time to put exactly 24 litres into an empty tank.\nWhich way takes the shortest total time? Type the minutes for each tap.',
      frame='Tap A (minutes): {f1}     Tap B (minutes): {f2}',
      check=lambda: list(min(ways_for(24, 2, 3), key=lambda w: w[0] + w[1])),
      hint='Add the minutes of tap A and tap B for each way in your table. Which total is the least?',
      steps=['The total times are 12, 11, 10, 9 and 8 minutes.', 'The shortest is 0 minutes on tap A and 8 minutes on tap B.'],
      src=['Which way takes the shortest total time?']),
    D(id='Cb2', tier='invest', no='C(b) why', label='C(b) why', type='selfcheck', open=False, skill='explaining why', facts=(2, 3),
      q='Why does the faster tap win? Write your idea, then compare it with the model answer.', check=lambda: (2, 3),
      hint='Think about how many litres each tap puts in during 1 minute. To put in the same 24 litres, which tap needs more minutes?',
      steps=['Tap B puts in 3 litres every minute and tap A only 2. A tap that puts in more litres each minute needs fewer minutes for the same 24 litres.', 'So tap B alone takes 8 minutes and tap A alone takes 12 minutes. Every minute of tap B can do the work of 1 1/2 minutes of tap A.',
             'A good answer says that the tap with the bigger rate takes less time for the same amount.'],
      src=['Why does the faster tap win?']),
    D(id='Cc', tier='invest', no='C(c) 25 litres', label='C(c) 25', type='number', skill='counting all the ways', answer=4,
      q='Tap A puts 2 litres a minute and tap B puts 3 litres a minute, used one at a time for a whole number of minutes. What if the tank needs exactly 25 litres? How many ways are there now?',
      check=lambda: len(ways_for(25, 2, 3)),
      hint='Make a table again. Tap B puts in 3 litres a minute: which numbers of minutes leave an even number of litres for tap A?',
      steps=['The ways for 25 litres (minutes on tap A, minutes on tap B): ' + ', '.join(f'({a}, {b})' for a, b in ways_for(25, 2, 3)) + '.', 'That is 4 ways.'],
      src=['What if the tank needs 25 litres? How many ways now?']),
    D(id='Cc2', tier='invest', no='C(c) what changes', label='C(c) change', type='selfcheck', open=False, skill='explaining what changes', facts=ways_for(25, 2, 3),
      q='What changes and what stays the same when the tank needs 25 litres instead of 24? Write your idea, then compare it with the model answer.', check=lambda: ways_for(25, 2, 3),
      hint='Look at the table for 25 litres next to the table for 24. Look at how the minutes of tap A change when the minutes of tap B go up.',
      steps=['What stays the same: each time tap B runs 2 minutes longer, tap A runs 3 minutes less, so 6 litres are swapped.',
             'What changes: 25 is an odd number. Tap A always puts in an even number of litres, so tap B must put in an odd number of minutes: 1, 3, 5 or 7. Tap A alone and tap B alone no longer work, and there are 4 ways, not 5.',
             'A good answer mentions the swap rule and the odd number of litres.'],
      src=['What if the tank needs 25 litres? How many ways now? What changes and what stays the same?']),

    # ================= Think harder (A1 to A4)
    D(id='A1', tier='stretch', no='A1', type='number', skill='finding a missing rate', answer=5,
      q='A tap fills a tank in 12 minutes at 15 ℓ a minute. When a second tap is also turned on, the tank fills in 9 minutes. How many litres a minute does the second tap fill? (Type the number of litres a minute.)',
      check=lambda: [r for r in range(0, 200) if (15 + r) * 9 == 15 * 12][0] if minutes_to_reach(15, 15 * 12) == 12 else None,
      hint='How many litres does the tank hold? Then ask how many litres a minute both taps must put in to fill it in 9 minutes.',
      steps=['The tank holds 12 × 15 = 180 ℓ.', 'To fill 180 ℓ in 9 minutes, both taps together must put in 180 ÷ 9 = 20 ℓ a minute.', 'The first tap puts in 15 ℓ a minute, so the second tap puts in 20 − 15 = 5 ℓ a minute.'],
      src=['A tap fills a tank in 12 minutes at 15 ℓ a minute. When a second tap is also turned on, the tank fills in 9 minutes. How many litres a minute does the second tap fill?']),
    D(id='A2', tier='stretch', no='A2', type='text', skill='best mix of packs', accept=G.dec_accepts(F(960, 100), **MONEY), shown='9.60',
      q='Eggs are sold in boxes of 10 for $3.30 and boxes of 6 for $2.10. Siti needs at least 28 eggs. What is the least she can pay? (Type the number of dollars.)',
      check=lambda: _dec(egg_cheapest(28)[0]),
      hint='Try different mixes of boxes that give at least 28 eggs. Work out the cost of each mix and compare them.',
      steps=['Some mixes with at least 28 eggs: 3 boxes of 10 cost $9.90; 5 boxes of 6 cost $10.50; 2 boxes of 10 and 2 boxes of 6 cost $10.80.', '1 box of 10 and 3 boxes of 6 make 28 eggs and cost $3.30 + $6.30 = $9.60.',
             'Checking every mix of boxes, none that makes at least 28 eggs costs less. The least she can pay is $9.60.'],
      src=['Eggs are sold in boxes of 10 for $3.30 and boxes of 6 for $2.10. Siti needs at least 28 eggs. What is the least she can pay?']),
    D(id='A3', tier='stretch', no='A3', type='text', skill='car park charges', accept=G.dec_accepts(F(950, 100), **MONEY), shown='9.50',
      q='A car park charges $1.50 for the first hour and $1 for every half hour or part of a half hour after that. How much does it cost to park from 10.15 a.m. to 2.50 p.m.? (Type the number of dollars.)',
      check=lambda: _dec(PARK_A3),
      hint='How long is the car in the car park? Charge the first hour, then count the half hours or parts of half hours after it.',
      steps=['10.15 a.m. to 2.50 p.m. is 4 hours 35 minutes. The first hour costs $1.50.', 'The other 3 hours 35 minutes is 7 half hours and 5 more minutes. A part of a half hour counts as a whole one, so that is 8 half hours.', '8 × $1 = $8, and $1.50 + $8 = $9.50.'],
      src=['A car park charges $1.50 for the first hour and $1 for every half hour or part of a half hour after that. How much does it cost to park from 10.15 a.m. to 2.50 p.m.?']),
    D(id='A4', tier='stretch', no='A4', type='number', skill='comparing two plans', answer=100,
      q='Phone plan A costs $15 a month plus 10¢ a minute. Plan B costs 25¢ a minute with no monthly fee. For how many minutes in a month do the two plans cost the same? (Type the number of minutes.)',
      check=phone_same_minutes,
      hint='Plan B costs more for each minute. How much more? How many minutes of that extra does it take to reach the $15 monthly fee?',
      steps=['Plan B costs 25 − 10 = 15¢ more for each minute. Plan A has the $15 fee, which is 1500¢.', '1500 ÷ 15 = 100, so after 100 minutes the extra cost of plan B has made up the $15 fee.', 'At 100 minutes both plans cost $25 (plan A: $15 + $10; plan B: $25).'],
      src=['Phone plan A costs $15 a month plus 10¢ a minute. Plan B costs 25¢ a minute with no monthly fee. For how many minutes in a month do the two plans cost the same?']),

    # ================= Go further (B1 to B3)
    D(id='B1', tier='challenge', no='B1', type='number', skill='rate puzzle', answer=3,
      q='3 cats eat 3 fish in 3 minutes. At this rate, how many cats are needed to eat 100 fish in 100 minutes? (Type the number of cats.)', check=lambda: cats_needed(3, 3, 3, 100, 100),
      hint='First find how many fish ONE cat eats in 3 minutes. Then think about how many 3-minute turns there are in 100 minutes.',
      steps=['3 cats eat 3 fish in 3 minutes, so each cat eats 1 fish every 3 minutes.', 'In 100 minutes 3 cats together eat 3 × (100 ÷ 3) = 100 fish. (Each cat eats 100 ÷ 3 fish, and 3 cats eat 100.)', 'So 3 cats are enough.'],
      src=['3 cats eat 3 fish in 3 minutes. At this rate, how many cats are needed to eat 100 fish in 100 minutes?']),
    D(id='B2', tier='challenge', no='B2', type='fields', skill='two rates', answer=[6, 8],
      q='Candle A is 20 cm tall and burns down 2 cm every hour. Candle B is 14 cm tall and burns down 1 cm every hour. They are lit at the same time.\nAfter how many hours are they the same height? How tall are they then?',
      frame='Same height after (hours): {f1}     Height then (cm): {f2}', check=lambda: list(candles()),
      hint='Every hour, how much more does candle A burn down than candle B? How many hours close the gap between their heights?',
      steps=['At first candle A is 20 − 14 = 6 cm taller than candle B.', 'Every hour candle A burns 2 cm and candle B burns 1 cm, so the gap closes by 1 cm each hour. The gap of 6 cm closes after 6 hours.', 'After 6 hours: A is 20 − 12 = 8 cm and B is 14 − 6 = 8 cm.'],
      src=['Candle A is 20 cm tall and burns down 2 cm every hour. Candle B is 14 cm tall and burns down 1 cm every hour. They are lit at the same time. After how many hours are they the same height? How tall are they then?']),
    D(id='B3', tier='challenge', no='B3', type='number', skill='fill and empty together', answer=30,
      q='A tap fills an empty bath in 12 minutes. With the plug out, a full bath empties in 20 minutes. Ben turns on the tap but forgets the plug. How long does the bath take to fill? (Type the number of minutes.)',
      check=bath_minutes,
      hint='Pretend the bath holds a number of litres that is easy to share by 12 and by 20. How many litres go in each minute, and how many go out?',
      steps=['Pretend the bath holds 60 litres. The tap puts in 60 ÷ 12 = 5 litres a minute.', 'With the plug out, 60 ÷ 20 = 3 litres a minute drain away. So 5 − 3 = 2 litres stay in each minute.', '60 ÷ 2 = 30, so the bath takes 30 minutes. (The answer is the same for any size of bath.)'],
      src=['A tap fills an empty bath in 12 minutes. With the plug out, a full bath empties in 20 minutes. Ben turns on the tap but forgets the plug. How long does the bath take to fill?']),
    D(id='pose', tier='challenge', no='Make up your own', label='Make up', type='selfcheck', open=True, marking_mode='open', skill='making up a problem',
      q='Make up a better-buy puzzle with three packs of the same thing. Which pack is the best buy? Then check your puzzle by working it out.',
      hint='Choose the number of items and the price of each pack. Then work out the price of 1 item for every pack.',
      steps=['This question is open: many puzzles are right.', 'Check your puzzle by finding the price of 1 item in each pack. The best buy is the pack where 1 item costs the least, and the biggest pack is not always that one.',
             'Sample: 6 for $3.00 (50¢ each), 10 for $5.50 (55¢ each) and 12 for $7.20 (60¢ each): the 6-pack is the best buy.'],
      src=['Make up a better-buy puzzle with three packs of the same thing. Which pack is the best buy? Swap and check.']),
]


# ---------------------------------------------------------------- variants: a template with an oracle that simulates or searches
def _o_1a(e):
    r = F(e['B'], e['M'])
    return dict(f1=whole(total_after(r, 1)), f2=whole(total_after(r, 5)))


def _o_3b(e):
    return minutes_to_reach(e['a'] + (30 - e['a']), e['V'])


def _o_3c(e):
    return minutes_to_reach(e['a'] + (30 - e['a']) - 6, e['V'])


def _o_4a(e):
    return simulate_job(e['J'], lambda m: e['p'] + (50 - e['p']))


def _o_4b(e):
    return simulate_job(e['J'], lambda m: 30 if m <= e['k'] else 50)


def _o_6b(e):
    return [n for n in range(1, 300) if gym_cost(e['F'], 4, n) == gym_cost(0, 7, n)][0]


def _o_a1(e):
    found = [r for r in range(0, 200) if (15 + r) * e['T2'] == 15 * 12]
    assert len(found) == 1
    return found[0]


def _o_a4(e):
    found = [m for m in range(0, 5000) if 100 * e['F'] + e['c1'] * m == (e['c1'] + 15) * m]
    assert len(found) == 1
    return found[0]


def _o_b1(e):
    return cats_needed(e['n'], e['n'], e['n'], e['m'], e['m'])


def _o_b2(e):
    a, b, h = e['a'], e['b'], 0
    while a != b:
        a -= 2; b -= 1; h += 1
        assert a > 0 and b > 0
    return dict(f1=h, f2=a)


finish(ITEMS)

VARIANTS = {
    '1a': dict(
        base=dict(r=16, M=3),
        tpl=dict(vars=dict(r=[12, 16, 18, 20], M=[3, 4, 6]), derive=dict(B='r * M'),
                 q='A machine fills {B} bottles every {M} minutes.\nHow many bottles does it fill in 1 minute? How many in 5 minutes?',
                 frame='In 1 minute: {f1} bottles     In 5 minutes: {f2} bottles', answers=dict(f1='r', f2='5 * r'),
                 hint='How many bottles does the machine fill in just 1 minute? Then use that for 5 minutes.',
                 steps=['Share the bottles equally between the minutes to find the bottles in 1 minute.', 'Multiply that by 5 for 5 minutes.', 'The two numbers are {ans}.']),
        oracle=lambda e: _o_1a(dict(B=e['r'] * e['M'], M=e['M']))),
    '3b': dict(
        base=dict(a=12, V=240),
        tpl=dict(vars=dict(a=[12, 15, 18, 20], V=[240, 300, 360, 420, 480]), derive=dict(b='30 - a'),
                 q='An empty tank holds {V} ℓ. Tap A fills {a} ℓ a minute and tap B fills {b} ℓ a minute. Both taps are turned on (ignore any crack).\nHow long does it take to fill the tank? (Type the number of minutes.)', answer='V / 30',
                 hint='Both taps are on, so add what they put in each minute. Then ask how many of those minutes make {V} ℓ.',
                 steps=['Together the taps put in {a} + {b} = 30 ℓ a minute.', 'Divide {V} by 30.', 'The tank is full after {ans} minutes.']),
        oracle=_o_3b),
    '3c': dict(
        base=dict(a=12, V=240),
        tpl=dict(vars=dict(a=[12, 15, 18], V=[240, 360, 480, 600]), derive=dict(b='30 - a'),
                 q='An empty tank holds {V} ℓ. Tap A fills {a} ℓ a minute and tap B fills {b} ℓ a minute. Both taps are on, and a crack lets out 6 ℓ a minute.\nHow long does it take to fill the tank? (Type the number of minutes.)', answer='V / 24',
                 hint='The crack lets water out. How many litres stay in the tank each minute?',
                 steps=['Each minute {a} + {b} = 30 ℓ go in and 6 ℓ go out, so 24 ℓ stay in.', 'Divide {V} by 24.', 'The tank is full after {ans} minutes.']),
        oracle=_o_3c),
    '4a': dict(
        base=dict(p=30, J=900),
        tpl=dict(vars=dict(p=[20, 25, 30, 35], J=[600, 750, 900, 1000]), derive=dict(Q='50 - p'),
                 q='Printer P prints {p} pages a minute. Printer Q prints {Q} pages a minute. A job has {J} pages.\nBoth printers start together. How long do they take to print the job? (Type the number of minutes.)', answer='J / 50',
                 hint='How many pages do the two printers print together in 1 minute? Then ask how many minutes make {J} pages.',
                 steps=['Together they print {p} + {Q} = 50 pages a minute.', 'Divide {J} by 50.', 'They take {ans} minutes.']),
        oracle=_o_4a),
    '4b': dict(
        base=dict(k=5, J=900),
        tpl=dict(vars=dict(k=[5, 10, 15], J=[900, 1000]),
                 q='Printer P prints 30 pages a minute. Printer Q prints 20 pages a minute. A job has {J} pages.\nP starts alone. After {k} minutes, Q joins in. How long does the whole job take from the start? (Type the number of minutes.)',
                 answer='k + (J - 30 * k) / 50',
                 hint='How many pages has P printed alone in the first {k} minutes? How many pages are left for the two printers together?',
                 steps=['P alone prints 30 × {k} pages in the first {k} minutes.', 'The pages left are printed by both printers at 50 pages a minute.', 'The whole job takes {ans} minutes from the start.']),
        oracle=_o_4b),
    '6b': dict(
        base=dict(F=30),
        tpl=dict(vars=dict(F=[15, 30, 45, 60]),
                 q='Gym A charges ${F} to join and then $4 for each visit. Gym B has no joining fee and charges $7 for each visit.\nFor how many visits do the two gyms cost the same?', answer='F / 3',
                 hint='Gym A starts ${F} higher, but each visit costs $3 less than at Gym B. How many visits close that gap?',
                 steps=['Gym A costs $3 less for each visit (7 − 4 = 3), but it costs ${F} to join.', 'The ${F} is made up after {F} ÷ 3 visits.', 'The two gyms cost the same after {ans} visits.']),
        oracle=_o_6b),
    'A1': dict(
        base=dict(T2=9),
        tpl=dict(vars=dict(T2=[4, 5, 6, 9, 10]),
                 q='A tap fills a tank in 12 minutes at 15 ℓ a minute. When a second tap is also turned on, the tank fills in {T2} minutes. How many litres a minute does the second tap fill? (Type the number of litres a minute.)',
                 answer='180 / T2 - 15', hint='How many litres does the tank hold? Then ask how many litres a minute both taps must put in to fill it in {T2} minutes.',
                 steps=['The tank holds 12 × 15 = 180 ℓ.', 'To fill 180 ℓ in {T2} minutes, both taps together must put in 180 ÷ {T2} ℓ a minute.', 'Take away the 15 ℓ a minute of the first tap. The second tap fills {ans} ℓ a minute.']),
        oracle=_o_a1),
    'A4': dict(
        base=dict(F=15, c1=10),
        tpl=dict(vars=dict(F=[3, 6, 9, 12, 15, 18], c1=[5, 10, 20]), derive=dict(c2='c1 + 15'),
                 q='Phone plan A costs ${F} a month plus {c1}¢ a minute. Plan B costs {c2}¢ a minute with no monthly fee. For how many minutes in a month do the two plans cost the same? (Type the number of minutes.)',
                 answer='100 * F / 15', hint='Plan B costs more for each minute. How much more? How many minutes of that extra does it take to reach the monthly fee of plan A?',
                 steps=['Plan B costs {c2} − {c1} = 15¢ more for each minute.', 'Plan A has a monthly fee of ${F}, which is {F} × 100 cents. Divide it by 15¢.', 'The two plans cost the same for {ans} minutes.']),
        oracle=_o_a4),
    'B1': dict(
        base=dict(n=3, m=100),
        tpl=dict(vars=dict(n=[2, 3, 4, 5, 6], m=[60, 100, 120]),
                 q='{n} cats eat {n} fish in {n} minutes. At this rate, how many cats are needed to eat {m} fish in {m} minutes? (Type the number of cats.)', answer='n',
                 hint='First find how many fish ONE cat eats in {n} minutes. Then think about how many {n}-minute turns there are in {m} minutes.',
                 steps=['{n} cats eat {n} fish in {n} minutes, so each cat eats 1 fish every {n} minutes.', 'In {m} minutes {n} cats together eat {m} fish.', 'So {ans} cats are enough.']),
        oracle=_o_b1),
    'B2': dict(
        base=dict(a=20, b=14),
        tpl=dict(vars=dict(a=[20, 22], b=[14, 15, 16]),
                 q='Candle A is {a} cm tall and burns down 2 cm every hour. Candle B is {b} cm tall and burns down 1 cm every hour. They are lit at the same time.\nAfter how many hours are they the same height? How tall are they then?',
                 frame='Same height after (hours): {f1}     Height then (cm): {f2}', answers=dict(f1='a - b', f2='2 * b - a'),
                 hint='Every hour, how much more does candle A burn down than candle B? How many hours close the gap between their heights?',
                 steps=['At first candle A is {a} − {b} cm taller than candle B.', 'Every hour the gap closes by 1 cm, because A burns 2 cm and B burns 1 cm.', 'The two numbers are {ans}.']),
        oracle=_o_b2),
}


polish(ITEMS, VARIANTS)
