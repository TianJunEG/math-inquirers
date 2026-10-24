"""Online practice for Level 4 (Primary 4, ages 9-11) holiday lesson 10: Puzzle Day (mixed heuristics).

The questions are the ones printed in the Level 4 holiday workbook, built by p4/workbook_html.js from p4/content/l10.js:
  Start here = l10.js workbook() Q1 to Q6;   Investigation = l10.js gaps.invest (Ring toss scores);
  Think harder = l10.js qbank.stretch[0:4];   Go further = l10.js qbank.challenge[-3:]  (printed as Q5 to Q7).
Every answer is recomputed by an INDEPENDENT checker that never uses the printed answer: next-door numbers and pen/notebook money by trying every number, heads-and-legs by trying every split,
working backwards by running the story forwards, the food puzzle by trying all 24 orders, queues by counting places, ages by trying every age, the ring-toss scores by building every total.
The build stops if a checker and the printed answer differ.
"""
import itertools, os, sys, textwrap
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from p4lib import *      # noqa: E402,F401

META = dict(level=4, lesson=10, key='p4', title='Puzzle Day', workbook_title='PUZZLE DAY', topic='Mixed heuristics',
            strand='Puzzle solving',
            sources=['p4/content/l10.js'],
            intro=['Today there is no new topic: pick a way in. Guess and check, suppose they are all the same, work backwards, or use the clues one at a time. Then check your answer against EVERY fact.',
                   'Type numbers; the food puzzle and some others are choices: tap one. Questions that ask you to explain or to make up your own puzzle are for thinking or writing on paper, then compare.'])
S10 = 'Puzzle solving'


def D(**k):
    return dict(strand=S10, **k)


# ---------------------------------------------------------------- independent checkers (try every possibility)
def next_door(prod, gap=1):
    return [n for n in range(1, 2000) if n * (n + gap) == prod]


def pen_ways(pen, book, total):
    """Every way to buy at least one of each: (pens, notebooks), fewest notebooks first."""
    return sorted(((p, n) for n in range(1, total // book + 1) for p in range(1, total // pen + 1) if pen * p + book * n == total), key=lambda w: w[1])


def heads_legs(heads, legs, a=2, b=4):
    """Number of animals with `b` legs when the rest have `a` legs, by trying every split (None if impossible)."""
    ok = [k for k in range(heads + 1) if a * (heads - k) + b * k == legs]
    return ok[0] if len(ok) == 1 else (None if not ok else ok)


def money_left(total, book, n):
    return total - book * n


DISHES = ['Chicken rice', 'Laksa', 'Prata', 'Nasi lemak']
FRIENDS = ['Ali', 'Ben', 'Mei', 'Siti']
RICE = {'Chicken rice', 'Nasi lemak'}


def food_solutions():
    out = []
    for perm in itertools.permutations(DISHES):
        d = dict(zip(FRIENDS, perm))
        if d['Ali'] in RICE and d['Siti'] in RICE and d['Ali'] != 'Chicken rice' and d['Ben'] != 'Prata':
            out.append(d)
    return out


FOOD = food_solutions()
assert len(FOOD) == 1
FOOD = FOOD[0]


def queue_size(front, back):
    """The queue has n people when the person is `front`th from the front and `back`th from the back."""
    return next(n for n in range(1, 500) if n - front + 1 == back)


def ages_now(total, years, times):
    return next(b for b in range(1, total) if (total - b) + years == times * (b + years))


def ages_puzzle():
    return next(d for d in (dict(zip(FRIENDS, p)) for p in itertools.permutations([8, 9, 10, 11]))
                if d['Ali'] == d['Siti'] + 2 and d['Ben'] > d['Mei'] and d['Siti'] > d['Mei'])


def back_marbles(final, won, lost):
    """Ravi gave away half, then won `won` and lost `lost`: try every starting number."""
    return next(x for x in range(2, 1000, 2) if x // 2 + won - lost == final)


def back_number(mult, take, half_to):
    return next(x for x in range(1, 1000) if (x * mult - take) % 2 == 0 and (x * mult - take) // 2 == half_to)


def stickers_start(final, extra):
    for x in range(2, 2000, 2):
        r1 = x - (x // 2 + extra)
        if r1 % 2:
            continue
        r2 = r1 - (r1 // 2 + extra)
        if r2 == final:
            return x
    raise ValueError


def book_money(spent, left):
    return next(x for x in range(spent, 5000) if (x - spent) % 2 == 0 and (x - spent) // 2 == left)


def wheels_tricycles(vehicles, wheels):
    return next(t for t in range(vehicles + 1) if 2 * (vehicles - t) + 3 * t == wheels)


def tables_with_six(tables, seats):
    return [k for k in range(tables + 1) if 4 * (tables - k) + 6 * k == seats]


RING = possible_scores([3, 5], 60)
RING_NO = [s for s in range(1, 21) if s not in RING]
RING46 = possible_scores([4, 6], 60)
RING46_NO = [s for s in range(1, 21) if s not in RING46]
TWO_RINGS = sorted({a + b for a in (3, 5) for b in (3, 5)})


def clue_fig():
    lines = ['*Ali, Ben, Mei and Siti each ordered a different dish: chicken rice, laksa, prata or nasi lemak. (Chicken rice and nasi lemak are the rice dishes.)']
    lines = [textwrap.wrap(lines[0][1:], 38)]
    wrapped = ['*' + w if i == 0 else w for i, w in enumerate(lines[0])]
    for t in ('Clue 1: Ali and Siti both ordered rice dishes.', 'Clue 2: Ali did not order chicken rice.', 'Clue 3: Ben did not order prata.'):
        wrapped += textwrap.wrap(t, 38)
    return text_lines_fig(wrapped, 14, 22, 330, label='Four friends, Ali, Ben, Mei and Siti, each ordered a different dish: chicken rice, laksa, prata or nasi lemak. Chicken rice and nasi lemak are the rice dishes. '
                          'Clue 1: Ali and Siti both ordered rice dishes. Clue 2: Ali did not order chicken rice. Clue 3: Ben did not order prata.')


def food_item(who, no):
    return D(id='4-' + who.lower(), tier='core', no=no, label='4 ' + who, type='choice', options=DISHES, answer=FOOD[who], skill='a logic puzzle', svg=clue_fig(),
             check=lambda: food_solutions()[0][who],
             q=f'Use the clues. Which dish did {who} order?',
             hint='Use the clues one at a time. Which dishes can you rule out for each friend?',
             steps=['Clue 1: Ali and Siti ordered the two rice dishes, chicken rice and nasi lemak. Clue 2: Ali did not order chicken rice, so Ali ordered nasi lemak and Siti ordered chicken rice.',
                    'Ben and Mei are left with laksa and prata. Clue 3: Ben did not order prata, so Ben ordered laksa and Mei ordered prata.',
                    f'{who} ordered {FOOD[who].lower()}.' if FOOD[who] != 'Chicken rice' else f'{who} ordered chicken rice.'],
             src=['Ali, Ben, Mei and Siti each ordered a different dish: chicken rice, laksa, prata or nasi lemak.', 'Ali: ___________   Ben: ___________   Mei: ___________   Siti: ___________'])


def ages_bars(m=3):
    return bar_pair('Ben', 1, 'Father', m, '? total', caption=f'Bars for their ages in some years from now. Ben has 1 equal part and his father has {m} equal parts of the same size. A brace on the right marks their total age, with a question mark.')


ITEMS = [
    # ================= Start here (workbook lesson 10, Q1 to Q6)
    D(id='1a', tier='core', no='1(a)', label='1(a)', type='set', ordered=False, answer=[23, 24], skill='guess and check', check=lambda: (lambda n: [n[0], n[0] + 1])(next_door(552)),
      q='Guess and check. Make a table of your tries. Two consecutive numbers (next-door numbers, like 7 and 8) multiply to make 552. What are they? Type both numbers, with commas.',
      hint='Make a table of your tries. Is 20 × 21 too big or too small? That tells you which way to go.',
      steps=['20 × 21 = 420 is too small, and 25 × 26 = 650 is too big, so try numbers in between.', '23 × 24 = 552.', 'The numbers are 23 and 24.'],
      src=['Guess and check. Make a table of your tries.', 'Two consecutive numbers (next-door numbers, like 7 and 8) multiply to make 552. What are they?']),
    D(id='1b-table', tier='core', no='Take-home 1(b)', label='TH table', type='set', ordered=True, answer=[36, 29, 22, 15, 8, 1], skill='guess and check with a table',
      check=lambda: [money_left(50, 7, n) for n in range(2, 8)],
      q='Mei buys some $4 pens and some $7 notebooks for exactly $50. Start with a table. If she buys 1 notebook, $43 is left for pens. How much is left for pens if she buys 2, 3, 4, 5, 6 and 7 notebooks? Type the six amounts in order, with commas.',
      hint='Each notebook costs $7. Take it away from the money left each time.',
      steps=['Each extra notebook takes $7 away from $50.', '2 notebooks leave $36, then $29, $22, $15, $8 and $1.'],
      src=['Money left for pens', 'Mei buys some $4 pens and some $7 notebooks for exactly $50. Find ALL the ways.']),
    D(id='1b-nb', tier='core', no='Take-home 1(b)', label='TH notebooks', type='set', ordered=False, answer=[2, 6], skill='guess and check with a table',
      check=lambda: [w[1] for w in pen_ways(4, 7, 50)],
      q='Mei buys some $4 pens and some $7 notebooks for exactly $50. She buys at least 1 of each. Find ALL the ways. First: which numbers of notebooks leave a whole number of $4 pens? Type every number of notebooks that works, with commas.',
      hint='Use your table. The money left for pens must be in the 4 times table.',
      steps=['The money left for pens is $43, $36, $29, $22, $15, $8 and $1 for 1 to 7 notebooks.', 'Only $36 and $8 are in the 4 times table.', 'So Mei buys 2 notebooks or 6 notebooks.'],
      src=['Mei buys some $4 pens and some $7 notebooks for exactly $50. Find ALL the ways.']),
    D(id='1b-pens', tier='core', no='Take-home 1(b)', label='TH pens', type='set', ordered=True, answer=[9, 2], skill='guess and check with a table',
      check=lambda: [w[0] for w in pen_ways(4, 7, 50)],
      q='Mei buys some $4 pens and some $7 notebooks for exactly $50. She buys at least 1 of each. List every way, with the fewest notebooks first. Type the number of pens in each way, with commas.',
      hint='For each number of notebooks that works, divide the money left by $4.',
      steps=['2 notebooks cost $14, leaving $36 for 9 pens ($36 + $14 = $50).', '6 notebooks cost $42, leaving $8 for 2 pens ($8 + $42 = $50).', 'With the fewest notebooks first, the pens are 9, then 2.'],
      src=['Mei buys some $4 pens and some $7 notebooks for exactly $50. Find ALL the ways.', 'Pens?']),

    D(id='2a', tier='core', no='2(a)', label='2(a)', type='fields', frame='Legs: {f1}    Legs short: {f2}', answer=[36, 14], skill='suppose they are all the same',
      check=lambda: (lambda legs: [legs, 50 - legs])(2 * 18),
      q='A farm has chickens and goats. There are 18 heads and 50 legs altogether. Suppose all 18 animals are chickens. How many legs would there be, and how many legs short of 50 is that?',
      hint='How many legs does one chicken have? Then think about 18 of them.',
      steps=['A chicken has 2 legs, so 18 chickens have 18 × 2 = 36 legs.', '50 − 36 = 14 legs short.'],
      src=['A farm has chickens and goats. There are 18 heads and 50 legs altogether.', 'Suppose all 18 are chickens. Legs:  ______    Legs short:  ______']),
    D(id='2b', tier='core', no='2(b)', label='2(b)', type='fields', frame='Each swap to a goat adds {f1} legs. So {f2} goats and {f3} chickens.', answer=[2, 7, 11], skill='suppose they are all the same',
      check=lambda: (lambda g: [4 - 2, g, 18 - g])(heads_legs(18, 50)),
      q='A farm has chickens and goats: 18 heads and 50 legs altogether. Swap chickens for goats until there are 50 legs. Fill in the blanks.',
      hint='A goat has 4 legs and a chicken has 2. How many legs does one swap add? How many swaps fill the gap?',
      steps=['A goat has 2 more legs than a chicken, so each swap adds 2 legs.', 'The gap is 14 legs, and 14 ÷ 2 = 7 swaps. So 7 goats and 18 − 7 = 11 chickens.', 'Check: 11 × 2 + 7 × 4 = 22 + 28 = 50.'],
      src=['Each swap to a goat adds ____ legs. So ____ goats and ____ chickens.']),
    D(id='2c', tier='core', no='2(c)', label='2(c)', type='number', answer=11, skill='suppose they are all the same', check=lambda: 24 - heads_legs(24, 70, 4, 2),
      q='A car park has cars and motorcycles: 24 vehicles and 70 wheels altogether. A car has 4 wheels and a motorcycle has 2. How many cars are there?',
      hint='Suppose all 24 vehicles are motorcycles. How many wheels is that, and how far from 70?',
      steps=['If all 24 were motorcycles there would be 24 × 2 = 48 wheels, which is 22 short.', 'Each swap to a car adds 2 wheels, so 22 ÷ 2 = 11 cars.', 'Check: 11 × 4 + 13 × 2 = 44 + 26 = 70.'],
      src=['A car park has cars and motorcycles: 24 vehicles, 70 wheels. How many cars?']),

    D(id='3a', tier='core', no='3(a)', label='3(a)', type='number', answer=52, skill='work backwards', check=lambda: back_marbles(30, 9, 5),
      q='Work backwards. Start at the end and undo each step, last step first. Ravi gave away half of his marbles. Then he won 9 marbles and lost 5. Now he has 30. How many marbles did he have at first?',
      hint='Start with the 30 that he has now. Undo the last step first.',
      steps=['Undo losing 5: 30 + 5 = 35. Undo winning 9: 35 − 9 = 26.', 'Undo giving away half: 26 × 2 = 52.', 'Check: half of 52 is 26, then 26 + 9 − 5 = 30.'],
      src=['Work backwards. Start at the end and undo each step, last step first.', 'Ravi gave away half of his marbles. Then he won 9 marbles and lost 5. Now he has 30. How many did he have at first?']),
    D(id='3b', tier='core', no='3(b)', label='3(b)', type='number', answer=20, skill='work backwards', check=lambda: back_number(3, 18, 21),
      q='I think of a number. I multiply it by 3, take away 18, then halve the answer. I get 21. What is my number?',
      hint='Start with 21. Undo the halving first.',
      steps=['Undo halving: 21 × 2 = 42. Undo taking away 18: 42 + 18 = 60.', 'Undo multiplying by 3: 60 ÷ 3 = 20.', 'Check: 20 × 3 = 60, 60 − 18 = 42, half of 42 is 21.'],
      src=['I think of a number. I multiply it by 3, take away 18, then halve the answer. I get 21. What is my number?']),

    food_item('Ali', '4(a)'),
    food_item('Ben', '4(b)'),
    food_item('Mei', '4(c)'),
    food_item('Siti', '4(d)'),

    D(id='5a', tier='core', no='5(a)', label='5(a)', type='number', answer=18, skill='counting places in a queue', svg=queue_fig(7, 12), check=lambda: queue_size(7, 12),
      q='Mei is 7th from the front and 12th from the back of a queue at the MRT gantry. How many people are in the queue?',
      hint='Count carefully: is anyone counted twice?',
      steps=['There are 6 people in front of Mei, Mei herself, and 11 people behind her.', '6 + 1 + 11 = 18 people.', 'Adding 7 + 12 = 19 counts Mei twice.'],
      src=['The queue for (a) is drawn for you. Count carefully: who is counted twice?', 'Mei is 7th from the front and 12th from the back of a queue at the MRT gantry. How many people are in the queue?']),
    D(id='5b', tier='core', no='5(b)', label='5(b)', type='number', answer=15, skill='counting places in a queue', check=lambda: next(b for b in range(1, 21) if queue_size(6, b) == 20),
      q='20 people are in a queue. Ben is 6th from the front. What is his place from the back?',
      hint='Draw the queue. How many people are behind Ben?',
      steps=['5 people are in front of Ben and he is 1 more, so 6 people are at the front up to Ben.', '20 − 6 = 14 people are behind him.', 'Ben is 14 + 1 = 15th from the back.'],
      src=['20 people are in a queue. Ben is 6th from the front. What is his place from the back?']),

    D(id='6', tier='core', no='6', label='6', type='number', answer=10, skill='ages with equal parts', svg=ages_bars(3), check=lambda: ages_now(50, 5, 3),
      q='Ben and his father are 50 years old altogether. In 5 years, his father will be 3 times as old as Ben. How old is Ben now? The bars show their ages in 5 years, and the brace shows their total then.',
      hint='Try an age for Ben and check it. Try 1: if Ben is 6, his father is 44. In 5 years: Ben 11, father 49. Is 49 three times 11? No (33). Try again with a different age.',
      steps=['In 5 years each of them is 5 years older, so the total is 50 + 10 = 60.', 'The bars have 4 equal parts, so one part is 60 ÷ 4 = 15. Ben will be 15, so he is 15 − 5 = 10 now.', 'Check: his father is 40 now. In 5 years: Ben 15 and father 45, and 45 is 3 times 15.'],
      src=['Ben and his father are 50 years old altogether. In 5 years, his father will be 3 times as old as Ben. How old is Ben now? The bars show their ages in 5 years.']),

    # ================= Investigation: Ring toss scores
    D(id='Ieasy', tier='invest', no='Investigation (easy step)', label='Inv easy', type='set', ordered=False, answer=TWO_RINGS, skill='listing all the ways',
      check=lambda: sorted({a + b for a in (3, 5) for b in (3, 5)}),
      q='In a ring-toss game, a small ring scores 3 points and a big ring scores 5 points. With exactly TWO rings, which different total scores can you get? Type every total, with commas.',
      hint='Write each pair of rings as an addition, then add.',
      steps=['Two small rings: 3 + 3 = 6. A small and a big: 3 + 5 = 8. Two big rings: 5 + 5 = 10.', 'The totals are 6, 8 and 10.'],
      src=['In a ring-toss game, a small ring scores 3 points and a big ring scores 5 points.', 'List the scores you can get with ONE ring: 3 or 5. Then with TWO rings: 3 + 3, 3 + 5 and 5 + 5. Write each total.']),
    D(id='Ia', tier='invest', no='Investigation (a)', label='Inv (a)', type='set', ordered=False, answer=RING_NO, skill='listing all the ways', grouped=False,
      check=lambda: [s for s in range(1, 21) if s not in possible_scores([3, 5], 20)],
      q='In ring toss, a small ring scores 3 points and a big ring scores 5 points. You can throw as many rings of each kind as you like. Which scores from 1 to 20 can you NOT get? Type them, with commas.',
      hint='Make a list of the scores from 1 to 20 that you CAN get, and show how you get each one.',
      steps=['You can get 3, 5, 6 (3 + 3), 8 (3 + 5), 9 (3 + 3 + 3), 10 (5 + 5), and every score from 8 up to 20.', 'You cannot get 1, 2, 4 or 7.'],
      src=['In a ring-toss game, a small ring scores 3 points and a big ring scores 5 points. You can throw as many rings of each kind as you like. Which total scores are possible?', 'List the scores from 1 to 20 that you CAN get, and show how (for example 8 = 3 + 5). Circle the scores you can NOT get.']),
    D(id='Ib', tier='invest', no='Investigation (b)', label='Inv (b)', type='number', answer=7, skill='a pattern in the scores',
      check=lambda: max(s for s in range(1, 40) if s not in possible_scores([3, 5], 40)),
      q='In ring toss with a 3-point ring and a 5-point ring, after which score can you get EVERY score? Type that score. (Every bigger score can be made.)',
      hint='Look at the scores you cannot get. Which is the biggest?',
      steps=['The scores you cannot get are 1, 2, 4 and 7.', 'After 7, every score can be made: 8, 9, 10, 11, 12 and on.'],
      src=['What do you notice about the scores you cannot get? After which score can you get every number?']),
    D(id='Ib-why', tier='invest', no='Investigation (b)', label='Inv (b) why', type='selfcheck', skill='explaining a pattern', check=lambda: (RING[:5], RING_NO),
      q='What do you notice about the scores you cannot get? How can you be sure that every bigger score can be made?',
      hint='Find three scores in a row that can be made. What happens if you add a 3-point ring to each?',
      steps=['The scores you cannot get are all small: 1, 2, 4 and 7.', '8 (3 + 5), 9 (3 + 3 + 3) and 10 (5 + 5) can all be made.', 'Adding one 3-point ring to 8, 9 and 10 gives 11, 12 and 13, and adding another gives the next three. So every score from 8 up can be made.'],
      src=['What do you notice about the scores you cannot get? After which score can you get every number?']),
    D(id='Ic-list', tier='invest', no='Investigation (c)', label='Inv (c) list', type='selfcheck', paper=True, skill='listing all the ways', check=lambda: RING46_NO, sol_fig=lambda f: text_lines_fig(['*Impossible scores (4 and 6 rings):', '1, 2, 3, 5, 7, 9, 11, 13, 15, 17, 19'], 15, 24, 330,
                                                                                label='The impossible scores from 1 to 20 with rings of 4 and 6 points: 1, 2, 3, 5, 7, 9, 11, 13, 15, 17, 19.'),
      paper_note='Write your list on paper, then check it against the list shown on screen. (There is nothing to type here: the next card is marked.)',
      q='What if the rings score 4 and 6? Write down which scores from 1 to 20 are impossible.',
      hint='List the scores you can make with 4s and 6s, then see which numbers from 1 to 20 are left.',
      steps=['You can make 4, 6, 8 (4 + 4), 10 (4 + 6), 12 and every even score after that, up to 20.', 'The impossible scores are 1, 2 and all the odd numbers: 1, 2, 3, 5, 7, 9, 11, 13, 15, 17, 19.'],
      src=['What if the rings score 4 and 6? Which scores from 1 to 20 are impossible? Explain why.']),
    D(id='Ic', tier='invest', no='Investigation (c)', label='Inv (c)', type='number', answer=len(RING46_NO), skill='listing all the ways',
      check=lambda: len([s for s in range(1, 21) if s not in possible_scores([4, 6], 20)]),
      q='With rings that score 4 and 6, how many of the scores from 1 to 20 are impossible? (Type the number. Your list on the card before helps.)',
      hint='Count the scores in your list.',
      steps=['The impossible scores are 1, 2, 3, 5, 7, 9, 11, 13, 15, 17, 19.', 'That is 11 scores.'],
      src=['What if the rings score 4 and 6? Which scores from 1 to 20 are impossible? Explain why.']),
    D(id='Ic-why', tier='invest', no='Investigation (c)', label='Inv (c) why', type='selfcheck', skill='explaining a pattern', check=lambda: all(s % 2 == 0 for s in RING46),
      q='What if the rings score 4 and 6? Explain why those scores are impossible.',
      hint='Are 4 and 6 odd or even? What do you get when you add numbers like that?',
      steps=['Both rings score even numbers, and even + even is even, so every score you can make is even. That is why no odd score is possible.', '2 is impossible too, because the smallest ring scores 4.', 'Every even score from 4 up can be made: 4, 6, 8 = 4 + 4, 10 = 4 + 6, and add another 4 each time.'],
      src=['What if the rings score 4 and 6? Which scores from 1 to 20 are impossible? Explain why.']),

    # ================= Think harder (qbank.stretch[0:4])
    D(id='T1', tier='stretch', no='Think harder 1', label='T1', type='number', answer=7, skill='suppose they are all the same', check=lambda: wheels_tricycles(20, 47),
      q='There are 20 bicycles and tricycles with 47 wheels altogether. How many tricycles are there?',
      hint='Suppose all 20 are bicycles. How many wheels is that? How far from 47?',
      steps=['All bicycles: 20 × 2 = 40 wheels, which is 7 short.', 'Each swap to a tricycle adds 1 wheel, so 7 swaps.', '7 tricycles and 13 bicycles. Check: 13 × 2 + 7 × 3 = 26 + 21 = 47.'],
      src=['There are 20 bicycles and tricycles with 47 wheels altogether. How many tricycles are there?']),
    D(id='T2', tier='stretch', no='Think harder 2', label='T2', type='set', ordered=False, answer=[24, 26], skill='guess and check', check=lambda: (lambda n: [n[0], n[0] + 2])(next_door(624, 2)),
      q='Two next-door even numbers (like 6 and 8) multiply to make 624. What are they? Type both numbers, with commas.',
      hint='Estimate first: what number times itself is close to 624? Then try even numbers near it.',
      steps=['25 × 25 = 625 is just above 624, so try the even numbers on either side of 25.', '24 × 26 = 624.', 'The numbers are 24 and 26.'],
      src=['Two next-door even numbers (like 6 and 8) multiply to make 624. What are they?']),
    D(id='T3', tier='stretch', no='Think harder 3', label='T3', type='number', answer=51, skill='work backwards', check=lambda: book_money(15, 18),
      q='Ravi spent $15 on a book. Then he spent half of the money left on a bag. He had $18 left. How much money did he have at first?',
      hint='Start with the $18 he has left. Undo the last step first.',
      steps=['After the book, he spent half of what was left on the bag, so the $18 he has left is the other half. Before the bag he had 18 × 2 = $36.', 'Before the book he had 36 + 15 = $51.', 'Check: 51 − 15 = 36, half of 36 is 18, and 36 − 18 = 18 left.'],
      src=['Ravi spent $15 on a book. Then he spent half of the money left on a bag. He had $18 left. How much money did he have at first?']),
    D(id='T4', tier='stretch', no='Think harder 4', label='T4', type='fields', frame='Ali {f1}    Ben {f2}    Mei {f3}    Siti {f4}', answer=[11, 10, 8, 9], skill='a logic puzzle',
      check=lambda: (lambda d: [d['Ali'], d['Ben'], d['Mei'], d['Siti']])(ages_puzzle()),
      q='Ali, Ben, Mei and Siti are 8, 9, 10 and 11 years old, in some order. Ali is 2 years older than Siti. Ben is older than Mei. Siti is older than Mei. How old is each child?',
      hint='Ali is 2 years older than Siti. Which pairs of ages from 8, 9, 10 and 11 differ by 2?',
      steps=['Ali is 2 more than Siti, so (Siti, Ali) is (8, 10) or (9, 11).', 'Mei is younger than both Siti and Ben. If Siti were 8, Mei would have to be younger than 8, which is not possible. So Siti is 9 and Ali is 11, and Mei is 8.', 'Ben is the one left: 10.'],
      src=['Ali, Ben, Mei and Siti are 8, 9, 10 and 11 years old, in some order.']),

    # ================= Go further (qbank.challenge[-3:], printed Q5 to Q7)
    D(id='G5a', tier='challenge', no='Go further 5', label='G5(a)', type='number', answer=8, skill='suppose they are all the same', check=lambda: tables_with_six(15, 76)[0],
      q='A hawker centre has 15 tables. Some seat 4 people and some seat 6 people. There are 76 seats altogether. How many tables seat 6?',
      hint='Suppose all 15 tables seat 4. How many seats is that, and how many more seats do you need?',
      steps=['If all 15 tables seat 4, there are 60 seats. 76 is 16 more.', 'Each table that seats 6 instead of 4 adds 2 seats, so 16 ÷ 2 = 8 tables seat 6.', 'Check: 8 × 6 + 7 × 4 = 48 + 28 = 76.'],
      src=['A hawker centre has 15 tables. Some seat 4 people and some seat 6 people. There are 76 seats altogether. (a) How many tables seat 6?']),
    D(id='G5b', tier='challenge', no='Go further 5', label='G5(b)', type='fields', frame='fewest: {f1}    most: {f2}', answer=[60, 90], skill='the smallest and largest possible', check=lambda: [min(4 * (15 - k) + 6 * k for k in range(16)), max(4 * (15 - k) + 6 * k for k in range(16))],
      q='A hawker centre has 15 tables. Each table seats 4 people or 6 people. What is the fewest and the most seats the centre could have?',
      hint='When are there the fewest seats? When are there the most?',
      steps=['Fewest: every table seats 4, so 15 × 4 = 60 seats.', 'Most: every table seats 6, so 15 × 6 = 90 seats.'],
      src=['(b) What is the fewest and the most seats 15 tables could have?']),
    D(id='G5c', tier='challenge', no='Go further 5', label='G5(c)', type='choice', options=['Yes', 'No'], answer='No', skill='odd and even totals',
      check=lambda: 'Yes' if tables_with_six(15, 77) else 'No',
      q='A hawker centre has 15 tables. Each table seats 4 people or 6 people. Could the centre have 77 seats altogether?',
      hint='Try to make 77 with 15 tables. What do you notice?',
      steps=['We tried every number of 6-seat tables from 0 to 15, and none gives 77 seats.', 'So the centre cannot have 77 seats.'],
      src=['(c) Could the centre have 77 seats? Explain.']),
    D(id='G5c-why', tier='challenge', no='Go further 5', label='G5(c) why', type='selfcheck', skill='odd and even totals', check=lambda: sorted({4 * (15 - k) + 6 * k for k in range(16)}),
      q='Explain how you know whether the centre can have 77 seats.',
      hint='Look at the number of seats at one table. Is it odd or even? What does that tell you about the total?',
      steps=['Every table seats an even number of people (4 or 6), and adding even numbers always gives an even number.', 'So the total number of seats must be even, and 77 is odd. The centre cannot have 77 seats.'],
      src=['(c) Could the centre have 77 seats? Explain.']),
    D(id='G6', tier='challenge', no='Go further 6', label='G6', type='number', answer=32, skill='work backwards', check=lambda: stickers_start(5, 2),
      q='Mei gave Ali half of her stickers and 2 more. Then she gave Ben half of the stickers left and 2 more. She had 5 stickers left. How many did she have at first?',
      hint='Start with the 5 she has left. Undo the last gift first.',
      steps=['Undo the gift to Ben: she had 5 left, so before it she had (5 + 2) × 2 = 14.', 'Undo the gift to Ali: before it she had (14 + 2) × 2 = 32.', 'Check: 32 − (16 + 2) = 14, then 14 − (7 + 2) = 5.'],
      src=['Mei gave Ali half of her stickers and 2 more. Then she gave Ben half of the stickers left and 2 more. She had 5 stickers left. How many did she have at first?']),
    D(id='G7', tier='challenge', no='Go further 7', label='G7', type='choice', options=['Yes, it could', 'No, the farmer counted wrong'], answer='No, the farmer counted wrong', skill='odd and even totals',
      check=lambda: 'Yes, it could' if heads_legs(12, 35) is not None else 'No, the farmer counted wrong',
      q='A farm has only chickens and goats. A farmer counts 12 heads and 35 legs. Could that be right?',
      hint='Try some numbers of goats. What do you notice about the total number of legs?',
      steps=['We tried every number of goats from 0 to 12: the legs are 24, 26, 28 and so on, never 35.', 'So the farmer must have counted wrong.'],
      src=['explain why a farmer who counts 12 heads and 35 legs on a farm with only chickens and goats must have counted wrong']),
    D(id='G7-why', tier='challenge', no='Go further 7', label='G7 why', type='selfcheck', skill='odd and even totals', check=lambda: all((2 * (12 - g) + 4 * g) % 2 == 0 for g in range(13)),
      q='Explain how you know whether 12 heads and 35 legs can happen on a farm with only chickens and goats.',
      hint='How many legs does each chicken have? Each goat? Odd or even?',
      steps=['Every chicken has 2 legs and every goat has 4, so the total number of legs is always even.', '35 is odd, so the farmer must have counted wrong.'],
      src=['explain why a farmer who counts 12 heads and 35 legs on a farm with only chickens and goats must have counted wrong']),
    D(id='G7-make', tier='challenge', no='Go further 7', label='G7 make', type='selfcheck', open=True, marking_mode='open', skill='making up a puzzle',
      check=lambda: [(c, 10 - c) for c in range(11) if 4 * c + 2 * (10 - c) == 32],
      q='Make up your own heads-and-legs puzzle (chickens and goats, or bicycles and cars) that has exactly ONE answer. Check it by trying every number of one animal.',
      hint='Pick the numbers of each animal first, then count the heads and legs. Check that no other split gives the same legs.',
      steps=['Puzzles will vary: check by trying every possible number.', 'Model: 10 vehicles, 32 wheels, cars (4 wheels) and motorcycles (2 wheels): 6 cars and 4 motorcycles is the only way.'],
      src=['Make up your own heads-and-legs puzzle (chickens and goats, or bicycles and cars) that has exactly ONE answer. Check it by trying every number of one animal.']),
]

finish(ITEMS)


# ---------------------------------------------------------------- variants (every combination is run against an oracle that does not use the template's formula)
def _wheels(h, t):
    return heads_legs(h, 2 * h + t, 2, 3)


VARIANTS = {
    '2a': dict(
        base=dict(H=18, g=7),
        tpl=dict(vars=dict(H=[12, 15, 18, 20], g=[4, 5, 7, 9]), derive=dict(L='2*H+2*g'),
                 q='A farm has chickens and goats. There are {H} heads and {L} legs altogether. Suppose all {H} animals are chickens. How many legs would there be, and how many legs short of {L} is that?',
                 frame='Legs: {f1}    Legs short: {f2}', answers=dict(f1='2*H', f2='2*g'),
                 hint='How many legs does one chicken have? Then think about {H} of them.',
                 steps=['A chicken has 2 legs, so {H} chickens have {H} × 2 legs.', 'The legs short are the legs of the farm, {L}, take away those. The answers are {ans}.']),
        oracle=lambda e: dict(f1=2 * e['H'], f2=(2 * e['H'] + 2 * e['g']) - 2 * e['H'])),
    '2c': dict(
        base=dict(V=24, c=11),
        tpl=dict(vars=dict(V=[20, 24, 30], c=[8, 11, 13, 15]), derive=dict(W='4*c+2*(V-c)'),
                 q='A car park has cars and motorcycles: {V} vehicles and {W} wheels altogether. A car has 4 wheels and a motorcycle has 2. How many cars are there?', answer='c',
                 hint='Suppose all {V} vehicles are motorcycles. How many wheels is that, and how far from {W}?',
                 steps=['If all {V} were motorcycles there would be {V} × 2 wheels. The gap to {W} is made up of swaps that add 2 wheels each.', 'The number of cars is {ans}.']),
        oracle=lambda e: next(c for c in range(e['V'] + 1) if 4 * c + 2 * (e['V'] - c) == 4 * e['c'] + 2 * (e['V'] - e['c']))),
    '3a': dict(
        base=dict(F=30, w=9, l=5),
        tpl=dict(vars=dict(F=[20, 24, 30, 36], w=[7, 9, 11, 12], l=[3, 5, 6, 8]),
                 q='Ravi gave away half of his marbles. Then he won {w} marbles and lost {l}. Now he has {F}. How many marbles did he have at first?', answer='2*(F-w+l)',
                 hint='Start with the {F} that he has now. Undo the last step first.',
                 steps=['Undo losing {l}: add {l}. Undo winning {w}: take away {w}.', 'Undo giving away half: double it. He had {ans} marbles at first.']),
        oracle=lambda e: back_marbles(e['F'], e['w'], e['l'])),
    '3b': dict(
        base=dict(n=20, m=3, k=18),
        tpl=dict(vars=dict(n=[12, 14, 16, 18, 20, 22], m=[3, 4, 5], k=[6, 8, 10, 12]), derive=dict(R='(n*m-k)//2'),
                 q='I think of a number. I multiply it by {m}, take away {k}, then halve the answer. I get {R}. What is my number?', answer='n',
                 hint='Start with {R}. Undo the halving first.',
                 steps=['Undo halving: double {R}. Undo taking away {k}: add {k}.', 'Undo multiplying by {m}: divide by {m}. The number is {ans}.']),
        oracle=lambda e: back_number(e['m'], e['k'], (e['n'] * e['m'] - e['k']) // 2)),
    '5a': dict(
        base=dict(f=7, b=12),
        tpl=dict(vars=dict(f=[5, 6, 7, 8], b=[9, 10, 12, 13]),
                 q='Mei is {f}th from the front and {b}th from the back of a queue at the MRT gantry. How many people are in the queue?', answer='f+b-1',
                 hint='Count carefully: is anyone counted twice?',
                 steps=['There are {f} − 1 people in front of Mei, Mei herself, and {b} − 1 people behind her.', 'The queue has {ans} people. Adding {f} + {b} counts Mei twice.']),
        fig=lambda e: queue_fig(e['f'], e['b']),
        oracle=lambda e: queue_size(e['f'], e['b'])),
    '5b': dict(
        base=dict(n=20, f=6),
        tpl=dict(vars=dict(n=[15, 20, 25, 30], f=[4, 6, 8, 9]),
                 q='{n} people are in a queue. Ben is {f}th from the front. What is his place from the back?', answer='n-f+1',
                 hint='Draw the queue. How many people are behind Ben?',
                 steps=['{n} − {f} people are behind Ben.', 'He is that many plus 1 from the back: {ans}th.']),
        oracle=lambda e: next(b for b in range(1, e['n'] + 1) if queue_size(e['f'], b) == e['n'])),
    '6': dict(
        base=dict(b=10, m=3, y=5),
        tpl=dict(vars=dict(b=[6, 7, 8, 9, 10], m=[3, 4], y=[3, 4, 5]), derive=dict(T='b+m*(b+y)-y'),
                 q='Ben and his father are {T} years old altogether. In {y} years, his father will be {m} times as old as Ben. How old is Ben now? The bars show their ages in {y} years, and the brace shows their total then.',
                 answer='b', hint='In {y} years each of them is {y} years older. What is their total age then?',
                 steps=['In {y} years each of them is {y} years older, so the total is {T} + 2 × {y}.', 'The bars have {m} + 1 equal parts. Find one part (Ben\'s age then), and take away {y}. Ben is {ans} now.']),
        fig=lambda e: ages_bars(e['m']),
        oracle=lambda e: ages_now(e['b'] + e['m'] * (e['b'] + e['y']) - e['y'] + e['b'] - e['b'], e['y'], e['m'])),
    'T1': dict(
        base=dict(H=20, t=7),
        tpl=dict(vars=dict(H=[15, 20, 25, 30], t=[5, 7, 9, 12]), derive=dict(W='2*H+t'),
                 q='There are {H} bicycles and tricycles with {W} wheels altogether. How many tricycles are there?', answer='t',
                 hint='Suppose all {H} are bicycles. How many wheels is that? How far from {W}?',
                 steps=['All bicycles: {H} × 2 wheels. The rest of the {W} wheels must come from swaps, each adding 1 wheel.', 'There are {ans} tricycles.']),
        oracle=lambda e: wheels_tricycles(e['H'], 2 * e['H'] + e['t'])),
    'T3': dict(
        base=dict(s=15, L=18),
        tpl=dict(vars=dict(s=[10, 15, 20, 25], L=[12, 18, 24, 30]),
                 q='Ravi spent ${s} on a book. Then he spent half of the money left on a bag. He had ${L} left. How much money did he have at first?', answer='2*L+s',
                 hint='Start with the ${L} he has left. Undo the last step first.',
                 steps=['After the book, the ${L} he has left is half of what was left. Before the bag he had 2 × ${L}.', 'Before the book he had that plus ${s}: ${ans}.']),
        oracle=lambda e: book_money(e['s'], e['L'])),
    'G5a': dict(
        base=dict(N=15, k=8),
        tpl=dict(vars=dict(N=[12, 15, 18, 20], k=[5, 6, 8, 9]), derive=dict(S='4*N+2*k'),
                 q='A hawker centre has {N} tables. Some seat 4 people and some seat 6 people. There are {S} seats altogether. How many tables seat 6?', answer='k',
                 hint='Suppose all {N} tables seat 4. How many seats is that, and how many more seats do you need?',
                 steps=['If all {N} tables seat 4, there are {N} × 4 seats. The rest of the {S} seats come from tables that seat 6 instead, each adding 2.', '{ans} tables seat 6.']),
        oracle=lambda e: tables_with_six(e['N'], 4 * e['N'] + 2 * e['k'])[0]),
    'G6': dict(
        base=dict(f=5, e=2),
        tpl=dict(vars=dict(f=[3, 5, 7, 9], e=[2, 4]),
                 q='Mei gave Ali half of her stickers and {e} more. Then she gave Ben half of the stickers left and {e} more. She had {f} stickers left. How many did she have at first?', answer='((f+e)*2+e)*2',
                 hint='Start with the {f} she has left. Undo the last gift first.',
                 steps=['Undo the gift to Ben: ({f} + {e}) × 2.', 'Undo the gift to Ali: add {e} and double again. She had {ans} stickers at first.']),
        oracle=lambda e: stickers_start(e['f'], e['e'])),
}
