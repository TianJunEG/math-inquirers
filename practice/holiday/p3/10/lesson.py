"""Online practice for Level 3 (Primary 3, ages 8-10) holiday lesson 10: Puzzle Day (Mixed puzzles: bar graphs and logic).

The questions are the ones printed in the Level 3 holiday workbook (p3/workbook_html.js builds it from p3/content/l10.js: Start here = the lesson's workbook() pages;
Think harder 1 to 4 and Go further 5 to 7 = qbank stretch[0..3] and challenge[-3:]; the Extra questions = deck.takeHome (printed as "Take-home"); the Investigation =
p3/gifted.json lesson 10).  Every answer is recomputed by an INDEPENDENT checker below (the cups from the total, every way of giving the four CCAs, a queue built child by child,
every number made from the digit cards, every amount made from the coins, every way of giving the pets, every group of friends counted pair by pair), never a copy of the printed
answer; build_holiday.py stops if a checker and the printed answer differ.  The figures are the workbook's own data (the drinks bar graph, the queues, the digit cards, the matchstick
squares), drawn larger for a phone; the checks just below stop the build if the data here differs from the printed figures.  Lesson 10 is the showcase lesson: the paper tasks (the
tick-and-cross grid, drawing the Lime juice bar, making up a puzzle) are self-check or open cards with a model answer.
"""
import itertools, os, re, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from hlib import *          # noqa: E402,F401
from p3lib import *         # noqa: E402,F401
from p3lib_w5 import *      # noqa: E402,F401

META = dict(level=3, lesson=10, key='p3', title='Puzzle Day', workbook_title='PUZZLE DAY', topic='Mixed Puzzles: Bar Graphs and Logic', strand='Puzzles and reasoning',
            sources=['p3/content/l10.js', 'p3/gifted.json'],
            intro=['Today is Puzzle Day. There is no new topic: stuck? Draw it, list it in order, or make a table. Then check every clue.',
                   'Type the answers here. Where a question asks you to draw, do it on paper and then compare with the picture shown after you submit. Take your time: there is no rush.'])
FIG = figs5()['figs']
SK = 'Puzzles and reasoning'
EXTRA = 'Extra practice. '
SRC10 = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..', 'p3', 'content', 'l10.js'), encoding='utf-8').read()


def I(**kw):
    kw.setdefault('strand', SK)
    return kw


def texts(svg_text):
    return re.findall(r'<text[^>]*>([^<]*)</text>', svg_text)


# ---------------------------------------------------------------- the data of the figures equals the printed workbook figures
assert [(n, v) for n, v in DRINKS] == [('Milo', 45), ('Teh', 30), ('Kopi', 55), ('Bandung', 20)]
assert all(f'height="{v * 4}"' in FIG['l10_graph'] and f'>{v}<' in FIG['l10_graph'] for _, v in DRINKS) and 'Lime juice' in FIG['l10_graph'] and '>?<' in FIG['l10_graph']
assert "const data = [['Milo', 45, 'hz'], ['Teh', 30, 'dt'], ['Kopi', 55, 'hx'], ['Bandung', 20, 'hh'], ['Lime juice', null]]" in SRC10
assert texts(FIG['l10_cards']) == ['2', '5', '8']
assert set(texts(FIG['l10_q3a'])) >= {'Ben', '3rd', '5th', '1st', '2nd', '4th', 'last'} and set(texts(FIG['l10_q3b'])) >= {'Ali', 'Siti', '3 people between'}
assert "['Sticks', '4', '7', '10', '', '', '']" in SRC10 and texts(FIG['l10_sticks']) == ['1 square', '2 squares', '3 squares']
for _clue in ['Ali is not in the choir and does not play chess.', 'Mei and Ravi are not in the choir.', 'The swimmer’s name has 4 letters.', 'Ali’s pet has no fur. Ben does not have the dog.']:
    assert _clue in SRC10, _clue
assert 'Siti is 6th from the front and Ravi is 4th from the back. There are 3 children between them' in SRC10


# ---------------------------------------------------------------- helpers for the checkers
SOLD = dict(DRINKS)
TOTAL_CUPS = 200


def lime_cups():
    return TOTAL_CUPS - sum(SOLD.values())


def all_drinks():
    d = dict(SOLD)
    d['Lime juice'] = lime_cups()
    return d


CHILDREN = ['Ali', 'Mei', 'Ravi', 'Siti']
CCAS = ['Chess', 'Choir', 'Football', 'Swimming']


def cca_solutions():
    """Every way to give the four CCAs to the four children that fits all three clues."""
    out = []
    for p in itertools.permutations(CCAS):
        a = dict(zip(CHILDREN, p))
        if a['Ali'] not in ('Choir', 'Chess') and a['Mei'] != 'Choir' and a['Ravi'] != 'Choir':
            swimmer = [c for c in CHILDREN if a[c] == 'Swimming'][0]
            if len(swimmer) == 4:
                out.append(a)
    return out


def one(sols):
    return sols[0] if len(sols) == 1 else None


PETS = ['Cat', 'Dog', 'Fish']
PEOPLE3 = ['Ali', 'Ben', 'Siti']


def pet_solutions():
    out = []
    for p in itertools.permutations(PETS):
        a = dict(zip(PEOPLE3, p))
        if a['Ali'] == 'Fish' and a['Ben'] != 'Dog':          # a fish is the pet with no fur
            out.append(a)
    return out


def sticks_row(n):
    """Sticks for n squares in a row: 2 for the top and bottom of every square, and n + 1 standing sticks."""
    return 2 * n + (n + 1)


def triangle_sticks(n):
    """Sticks for n triangles in a row: the zigzag has n + 1 sticks and the n sticks across (every other point) close the triangles."""
    return (n + 1) + n


def ordinal_free_queue(front, back):
    return queue_total(front, back)


def odd_numbers(cards):
    return numbers_from_digits(cards, lambda n: n % 2 == 1)


def riddle_numbers():
    return [n for n in range(100, 1000) if n % 2 == 1 and sum(map(int, str(n))) == 6 and '0' not in str(n) and str(n)[0] > str(n)[1]]


def coin_amounts():
    return amounts([10, 20, 50])


def friends_more(n):
    return handshakes(n) - handshakes(n - 1)


def classes_solution():
    """3P1 = 3P2 + 10, 3P3 = 3P1, 3P4 = 3P2 - 5, altogether 135: try every kg for 3P2."""
    out = []
    for p2 in range(6, 135):
        p1 = p2 + 10
        p3 = p1
        p4 = p2 - 5
        if p1 + p2 + p3 + p4 == 135:
            out.append([p1, p2, p3, p4])
    return out


def puzzle_solutions(clues):
    out = []
    for p in itertools.permutations(['red', 'blue', 'green']):
        a = dict(zip(['Sam', 'Lee', 'Mei'], p))
        if all(a[who] != col for who, col in clues):
            out.append(a)
    return out


_EXAMPLE_CLUES = [('Sam', 'red'), ('Lee', 'blue'), ('Mei', 'green'), ('Sam', 'blue')]
assert puzzle_solutions(_EXAMPLE_CLUES) == [dict(Sam='green', Lee='red', Mei='blue')] and len(puzzle_solutions(_EXAMPLE_CLUES[:2] + _EXAMPLE_CLUES[3:])) == 1       # the model puzzle, and the clue about Mei can be taken away

CCA_CARD = clue_fig(['Ali, Mei, Ravi and Siti are each in a different CCA: chess, choir, football and swimming.'],
                    ['Ali is not in the choir and does not play chess.', 'Mei and Ravi are not in the choir.', 'The swimmer’s name has 4 letters.'], 'The three clues about the four children and their CCAs')
PET_CARD = clue_fig(['Ali, Ben and Siti each have a different pet: a cat, a dog and a fish.'], ['Ali’s pet has no fur.', 'Ben does not have the dog.'], 'The two clues about the three children and their pets')
CCA_STEPS = ['Clue 1: Ali is not in the choir. Clue 2: Mei and Ravi are not in the choir. So the choir is Siti.',
             'Clue 3: the swimmer’s name has 4 letters. Siti is in the choir, so the swimmer is Ravi (Ali and Mei have 3 letters).',
             'Clue 1: Ali does not play chess, and swimming is taken, so Ali plays football. Mei is left with chess.']


def cca_item(who, hint, tail):
    return I(id=f'2-{who}', tier='core', no=f'2 ({who})', label=f'2 {who}', type='choice', skill='logic grid', options=CCAS, answer=cca_solutions()[0][who] if len(cca_solutions()) == 1 else None, svg=CCA_CARD,
             q=f'Use the clues in the picture. Which CCA is {who} in?', check=lambda: one(cca_solutions())[who], hint=hint, steps=CCA_STEPS + [tail],
             src=['Ali, Mei, Ravi and Siti are each in a different CCA. Use the clues: put a ✓ or a cross in each box, then write each child’s CCA in the last column.'])


def pet_item(who, hint, tail):
    return I(id=f'T2-{who}', tier='stretch', no=f'T2 ({who})', label=f'T2 {who}', type='choice', skill='logic', options=PETS, answer=pet_solutions()[0][who], svg=PET_CARD,
             q=f'Use the clues in the picture. Which pet does {who} have?', check=lambda: one(pet_solutions())[who], hint=hint,
             steps=['Clue 1: a cat and a dog have fur, so the pet with no fur is the fish. Ali has the fish.', 'Clue 2: Ben does not have the dog, and the fish is taken, so Ben has the cat.', 'Siti has the pet that is left: the dog.', tail],
             src=['Ali, Ben and Siti each have a different pet: a cat, a dog and a fish. Ali’s pet has no fur. Ben does not have the dog. Who has which pet?'])


ITEMS = [
    # ================= Start here (workbook lesson 10, No.1 to No.6)
    I(id='1a', tier='core', no='1(a)', label='1(a) most', type='choice', skill='reading a bar graph', options=[n for n, _ in DRINKS], answer='Kopi', svg=drinks_fig(),
      q='A drinks stall sold 200 cups of drinks on Monday. The bar graph shows the cups sold, but the bar for Lime juice is missing. Which drink shown sold the most?',
      check=lambda: max(SOLD, key=SOLD.get),
      hint='Look at the numbers on top of the bars. Which is the biggest?',
      steps=['The bars show Milo 45, Teh 30, Kopi 55 and Bandung 20 cups.', '55 is the biggest number.', 'Kopi sold the most.'],
      src=['A drinks stall sold 200 cups of drinks on Monday. The bar graph shows the cups sold, but the bar for Lime juice is missing.', 'Which drink shown sold the most?']),
    I(id='1b', tier='core', no='1(b)', label='1(b)', type='number', skill='reading a bar graph', answer=25, svg=drinks_fig(),
      q='Look at the bar graph. How many more cups of Kopi than Teh were sold? Type the number.', check=lambda: SOLD['Kopi'] - SOLD['Teh'],
      hint='Read the numbers on top of the Kopi bar and the Teh bar. Then find the difference.',
      steps=['The Kopi bar shows 55 cups and the Teh bar shows 30 cups.', '55 - 30 = 25.', '25 more cups of Kopi than Teh were sold.'],
      src=['How many more cups of Kopi than Teh?']),
    I(id='1c', tier='core', no='1(c)', label='1(c)', type='number', skill='reading a bar graph', answer=50, svg=drinks_fig(),
      q='The stall sold 200 cups on Monday. How many cups of Lime juice were sold? Type the number.', check=lambda: lime_cups(),
      hint='How many cups do the four bars show altogether? How many of the 200 are left?',
      steps=['The four bars show 45 + 30 + 55 + 20 = 150 cups.', '200 - 150 = 50.', '50 cups of Lime juice were sold.'],
      src=['How many cups of Lime juice were sold?']),
    I(id='1c-draw', tier='core', no='1(c)', label='1(c) draw', type='selfcheck', paper=True, marking_mode='self', skill='drawing a bar graph', svg=drinks_fig(),
      sol_fig=lambda g: drinks_fig(lime=g),
      q='Now draw the bar for Lime juice on the graph, as high as the number of cups you found.', check=lambda: lime_cups(),
      hint='Find the number of cups on the left side. Draw the bar up to that line, like the other bars.',
      steps=['Lime juice sold 50 cups.', 'The bar goes up to the 50 line.', 'The bar is drawn in the picture.'],
      src=['Now draw its bar on the graph.']),
    I(id='1d', tier='core', no='1(d)', label='1(d)', type='text', skill='reading a bar graph', accept=name_list_forms([['Milo'], ['Kopi']]), shown='Milo and Kopi', svg=drinks_fig(),
      q='Which two drinks together sold exactly 100 cups? Type the two names.',
      check=lambda: ' and '.join(one([pair for pair in itertools.combinations(['Milo', 'Teh', 'Kopi', 'Bandung', 'Lime juice'], 2) if sum(all_drinks()[x] for x in pair) == 100])),
      hint='Try pairs of bars. Which two numbers add to 100?',
      steps=['Try pairs: 45 + 30 = 75, 45 + 55 = 100, 30 + 55 = 85 ...', 'Milo (45) and Kopi (55) make exactly 100. No other pair of drinks does.', 'The drinks are Milo and Kopi.'],
      src=['Which two drinks together sold exactly 100 cups?']),

    cca_item('Ali', 'Use clue 1: which CCAs is Ali not in? Which are left?', 'So Ali is in football.'),
    cca_item('Mei', 'Find out who is in the choir first (clues 1 and 2). Then see which CCAs are left for Ali, Mei and Ravi.', 'So Mei is in chess.'),
    cca_item('Ravi', 'Use clue 3: which names have 4 letters? Think about who is in the choir too.', 'So Ravi is in swimming.'),
    cca_item('Siti', 'Use clues 1 and 2: which children are not in the choir? Who is left?', 'So Siti is in the choir.'),

    I(id='3a', tier='core', no='3(a)', label='3(a)', type='number', skill='queues (draw it)', answer=7, svg=queue_fig(3, 5),
      q='Draw it! Queues. Ben is number 3 from the front and number 5 from the back. How many children are in the queue? Type the number.', check=lambda: queue_total(3, 5),
      hint='Ben is counted both from the front and from the back. Draw circles for the children in front of Ben, Ben, and the children behind him.',
      steps=['There are 2 children in front of Ben (he is 3rd) and 4 children behind him (he is 5th from the back).', '2 + 1 (Ben) + 4 = 7.', 'There are 7 children in the queue. (3 + 5 = 8 counts Ben twice, so take 1 away.)'],
      src=['Draw it! Queues.', 'Ben is 3rd from the front and 5th from the back. How many in the queue?']),
    I(id='3b', tier='core', no='3(b)', label='3(b)', type='number', skill='queues (draw it)', answer=6, svg=queue_between_fig(),
      q='Ali is number 2 from the front, Siti is last, and 3 people are between them. How many children are in the queue? Type the number.', check=lambda: len(['someone in front of Ali', 'Ali'] + ['between'] * 3 + ['Siti']),
      hint='Draw circles in order: the child in front of Ali, Ali, the 3 people between, then Siti.',
      steps=['In front of Ali there is 1 child (Ali is 2nd).', '1 + Ali + 3 between + Siti = 1 + 1 + 3 + 1.', 'There are 6 children in the queue.'],
      src=['Ali is 2nd from the front, Siti is last, 3 people are between them. How many in all?']),

    I(id='4a', tier='core', no='4(a)', label='4(a)', type='set', ordered=True, skill='making a list in order', answer=[258, 285, 528, 582, 825, 852], svg=cards_fig([2, 5, 8]),
      q='List it! Make 3-digit numbers with these cards. Use each card once in every number. List ALL the numbers, from smallest to largest. Type them with commas.', check=lambda: numbers_from_digits([2, 5, 8]),
      hint='Put the smallest card in the hundreds place first. How many numbers can you make with it? Then the next card.',
      steps=['Hundreds digit 2: 258 and 285. Hundreds digit 5: 528 and 582. Hundreds digit 8: 825 and 852.', 'Each card goes first twice, and the numbers are already in order.', 'The list is 258, 285, 528, 582, 825, 852.'],
      src=['List it! Make 3-digit numbers with these cards. Use each card once in every number.', 'List ALL the numbers, in order from smallest to largest.']),
    I(id='4b', tier='core', no='4(b)', label='4(b)', type='number', skill='making a list in order', answer=2, svg=cards_fig([2, 5, 8]),
      q='Use the cards 2, 5 and 8 once each in every 3-digit number. How many of the numbers you can make are odd? Type the number.', check=lambda: len(odd_numbers([2, 5, 8])),
      hint='Which digit must be in the ones place for an odd number? Which card is that?',
      steps=['A number is odd when its last digit is odd. Only the card 5 is odd.', 'With 5 in the ones place the other two cards can go either way round: 285 and 825.', 'There are 2 odd numbers.'],
      src=['How many of them are odd numbers?']),
    I(id='4c', tier='core', no='4(c)', label='4(c)', type='number', skill='making a list in order', answer=582, svg=cards_fig([2, 5, 8]),
      q='Use the cards 2, 5 and 8 once each in every 3-digit number. Which of the numbers is closest to 600? Type the number.',
      check=lambda: one([n for n in numbers_from_digits([2, 5, 8]) if abs(n - 600) == min(abs(m - 600) for m in numbers_from_digits([2, 5, 8]))]),
      hint='Make a list of the numbers. How far is each one from 600?',
      steps=['The numbers are 258, 285, 528, 582, 825 and 852.', 'Their distances from 600 are 342, 315, 72, 18, 225 and 252.', '582 is only 18 away from 600, so it is the closest.'],
      src=['Which number is closest to 600?']),

    I(id='5-table', tier='core', no='5', label='5 table', type='fields', skill='patterns and tables', answer=[13, 16, 19], frame='4 squares: {f1} sticks      5 squares: {f2} sticks      6 squares: {f3} sticks', svg=sticks_fig(),
      sol_fig=lambda g: sticks_fig(solved=[4, 7, 10] + list(g)),
      q='Make a table! Squares are made in a row with sticks, like the picture. Fill in the table: how many sticks are needed for 4, 5 and 6 squares?', check=lambda: [sticks_row(n) for n in (4, 5, 6)],
      hint='Look at the sticks for 1, 2 and 3 squares. How many more sticks does each new square need?',
      steps=['1 square uses 4 sticks, 2 squares use 7 sticks and 3 squares use 10 sticks. Each new square adds 3 sticks.', '4 squares: 10 + 3 = 13. 5 squares: 13 + 3 = 16. 6 squares: 16 + 3 = 19.', 'The numbers are 13, 16 and 19.'],
      src=['Make a table! Squares are made in a row with sticks. Fill in the table.']),
    I(id='5a', tier='core', no='5(a)', label='5(a)', type='number', skill='patterns and tables', answer=25, svg=sticks_fig(),
      q='Squares are made in a row with sticks, like the picture. How many sticks are needed for 8 squares? Type the number.', check=lambda: sticks_row(8),
      hint='Keep the table going: each new square needs the same number of extra sticks.',
      steps=['Each new square adds 3 sticks, and 1 square uses 4 sticks.', 'Keep adding 3: 13, 16, 19, 22, 25 (for 4, 5, 6, 7 and 8 squares).', '8 squares need 25 sticks.'],
      src=['How many sticks are needed for 8 squares?']),
    I(id='5b', tier='core', no='5(b)', label='5(b)', type='number', skill='patterns and tables', answer=10, svg=sticks_fig(),
      q='Squares are made in a row with sticks, like the picture. Ben uses 31 sticks. How many squares does he make? Type the number.', check=lambda: one([n for n in range(1, 60) if sticks_row(n) == 31]),
      hint='Keep the table going until you reach 31 sticks.',
      steps=['Keep adding 3 sticks for each new square: 25 sticks for 8 squares, 28 for 9 squares, 31 for 10 squares.', 'Ben makes 10 squares.'],
      src=['Ben uses 31 sticks. How many squares does he make?']),

    I(id='6', tier='core', no='6', label='6', type='set', skill='logic and listing', answer=[213, 321, 411],
      q='I am a 3-digit odd number. My digits add up to 6. My hundreds digit is bigger than my tens digit. None of my digits is 0. What could I be? Find ALL the answers. Type them with commas.', check=riddle_numbers,
      hint='Hint: three digits, none 0, that add up to 6, are 1, 1, 4 or 1, 2, 3 or 2, 2, 2. Try to arrange each set so that the number is odd and the hundreds digit is bigger than the tens digit.',
      steps=['The digits (none 0) add to 6 only as 1, 1, 4 or 1, 2, 3 or 2, 2, 2.', 'The number is odd, so the last digit is odd. 1, 1, 4 gives 411 (141 has the hundreds digit smaller than the tens digit). 1, 2, 3 gives 321 and 213 (231 and 123 have the hundreds digit smaller than the tens digit). 2, 2, 2 gives 222, which is even.', 'The numbers are 213, 321 and 411.'],
      src=['I am a 3-digit odd number. My digits add up to 6. My hundreds digit is bigger than my tens digit. None of my digits is 0. What could I be? Find ALL the answers.']),

    # ================= Investigation (Investigation and look back page, No.8: Handshakes)
    I(id='I8a', tier='invest', no='8(a)', label='Inv 8(a)', type='fields', skill='patterns and tables', answer=[3, 6, 10, 15],
      frame=grp('3 friends: {f1}      4 friends: {f2}      5 friends: {f3}      6 friends: {f4}'),
      q='Some friends meet. Everyone shakes hands with every other friend once. Two friends make 1 handshake. How many handshakes are there for 3, 4, 5 and 6 friends? Draw dots and lines on paper if it helps.',
      check=lambda: [handshakes(n) for n in (3, 4, 5, 6)],
      hint='Easy first step: draw 3 dots and join every pair. Count the lines. Then try 4 dots.',
      steps=['Draw a dot for each friend and join every pair with a line: each line is a handshake.', '3 friends: 3 lines. 4 friends: 6 lines. 5 friends: 10 lines. 6 friends: 15 lines.', 'The numbers are 3, 6, 10 and 15.'],
      src=['Some friends meet. Everyone shakes hands with every other friend once. Two friends make 1 handshake.', 'Find the number of handshakes for 3, 4, 5 and 6 friends.']),
    I(id='I8a-more', tier='invest', no='8(a)', label='Inv more', type='fields', skill='patterns and tables', answer=[2, 3, 4, 5],
      frame='3 friends: {f1} more      4 friends: {f2} more      5 friends: {f3} more      6 friends: {f4} more',
      q='Look at the handshakes for 2, 3, 4, 5 and 6 friends (2 friends make 1 handshake). How many MORE handshakes does each row have than the row above it? (Do the handshake question first.)',
      check=lambda: [friends_more(n) for n in (3, 4, 5, 6)],
      hint='Subtract each number of handshakes from the one below it.',
      steps=['3 friends have 3 handshakes and 2 friends have 1: 3 - 1 = 2 more.', '4 friends: 6 - 3 = 3 more. 5 friends: 10 - 6 = 4 more. 6 friends: 15 - 10 = 5 more.', 'The numbers are 2, 3, 4 and 5.'],
      src=['How many more than the row above?']),
    I(id='I8b-pattern', tier='invest', no='8(b)', label='Inv pattern', type='selfcheck', open=True, marking_mode='self', skill='noticing a pattern',
      q='What pattern do you see in the number of handshakes? Write your idea, then compare with the answer shown.', check=lambda: [friends_more(n) for n in (3, 4, 5, 6, 7)],
      hint='Look at how much more each row has than the row above.',
      steps=['The extra amount goes up by 1 each time: 2, 3, 4, 5 ...', 'Why: each new friend shakes hands with everyone who is already there. The 3rd friend shakes 2 hands, the 4th shakes 3, the 5th shakes 4.', 'So 7 friends have 5 + 1 = 6 more handshakes than 6 friends.'],
      src=['What pattern do you see? Use it to find the handshakes for 10 friends.']),
    I(id='I8b-10', tier='invest', no='8(b)', label='Inv 10', type='number', skill='patterns and tables', answer=45,
      q='Use the pattern to find the number of handshakes for 10 friends. Type the number.', check=lambda: handshakes(10),
      hint='Keep the table going down to 10 friends. Each row has one more than the last extra amount.',
      steps=['Keep going: 7 friends have 15 + 6 = 21, 8 friends have 21 + 7 = 28, 9 friends have 28 + 8 = 36, 10 friends have 36 + 9 = 45.', 'Or: the 10th friend shakes 9 hands, the 9th shakes 8, ... so 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 = 45.', '10 friends make 45 handshakes.'],
      src=['What pattern do you see? Use it to find the handshakes for 10 friends.']),
    I(id='I8c', tier='invest', no='8(c)', label='Inv 8(c)', type='choice', skill='noticing a pattern', options=['Yes', 'No'], answer='No',
      q='Could there ever be exactly 20 handshakes?', check=lambda: 'Yes' if any(handshakes(n) == 20 for n in range(2, 200)) else 'No',
      hint='Look at your table. Which numbers of handshakes come just before and just after 20?',
      steps=['6 friends make 15 handshakes and 7 friends make 21.', '20 is in between, and no number of friends gives it.', 'So there can never be exactly 20 handshakes.'],
      src=['Could there ever be exactly 20 handshakes? Explain.']),
    I(id='I8c-why', tier='invest', no='8(c)', label='Inv explain', type='selfcheck', open=True, marking_mode='self', skill='explaining why',
      q='Explain how you know whether there could ever be exactly 20 handshakes. Write your idea, then compare with the answer shown.', check=lambda: [handshakes(6), handshakes(7)],
      hint='Use your table or the pattern. Where would 20 have to be?',
      steps=['6 friends make 15 handshakes and 7 friends make 21 handshakes.', 'Every new friend adds more handshakes, so the number only goes up: 15, then 21, then more. It jumps over 20.', 'More friends only give more than 21, so 20 handshakes can never happen.'],
      src=['Could there ever be exactly 20 handshakes? Explain.']),

    # ================= Think harder (workbook Think harder, No.1 to No.4)
    I(id='T1-list', tier='stretch', no='T1', label='T1 list', type='set', ordered=True, skill='making a list in order', answer=[10, 20, 30, 50, 60, 70, 80],
      q='Ali has three coins: 10¢, 20¢ and 50¢. He picks one coin, or two coins, or all three. List every different amount of money he can make, in cents, smallest first. Type the amounts with commas.', check=coin_amounts,
      hint='List by the number of coins: first one coin, then two coins, then all three. Then put the amounts in order.',
      steps=['One coin: 10¢, 20¢, 50¢. Two coins: 10 + 20 = 30¢, 10 + 50 = 60¢, 20 + 50 = 70¢. All three: 80¢.', 'Put the amounts in order, smallest first.', 'The list is 10, 20, 30, 50, 60, 70, 80.'],
      src=['Ali has three coins: 10¢, 20¢ and 50¢. He picks one coin, or two coins, or all three. List every different amount of money he can make, in order. How many amounts are there?']),
    I(id='T1-count', tier='stretch', no='T1', label='T1 count', type='number', skill='making a list in order', answer=7,
      q='Ali has three coins: 10¢, 20¢ and 50¢. He picks one coin, or two coins, or all three. How many different amounts of money can he make? (Do the list question first.) Type the number.', check=lambda: len(coin_amounts()),
      hint='Count the amounts in your list.',
      steps=['The amounts are 10, 20, 30, 50, 60, 70 and 80 cents.', 'Count them: there are 7 different amounts.'],
      src=['How many amounts are there?']),
    pet_item('Ali', 'Which of a cat, a dog and a fish has no fur?', 'So Ali has the fish.'),
    pet_item('Ben', 'Ali has one of the pets. Which pets are left for Ben? Which one is he not allowed?', 'So Ben has the cat.'),
    pet_item('Siti', 'Work out the pets of Ali and Ben first. Which pet is left?', 'So Siti has the dog.'),
    I(id='T3', tier='stretch', no='T3', label='T3', type='number', skill='patterns and tables', answer=25, svg=triangles_fig(),
      q='Triangles are made in a row with sticks: 1 triangle uses 3 sticks, 2 triangles use 5 sticks, 3 triangles use 7 sticks. How many sticks are needed for 12 triangles? Type the number.', check=lambda: triangle_sticks(12),
      hint='Make a table: 1 triangle, 3 sticks; 2 triangles, 5 sticks ... How many sticks does each new triangle add?',
      steps=['Each new triangle adds 2 sticks: 3, 5, 7, 9, ...', 'The first triangle uses 3 sticks, then 11 more triangles add 2 sticks each: 3 + 11 × 2 = 3 + 22 = 25.', '12 triangles need 25 sticks.'],
      src=['Triangles are made in a row with sticks: 1 triangle uses 3 sticks, 2 triangles use 5 sticks, 3 triangles use 7 sticks. How many sticks are needed for 12 triangles?']),
    I(id='T4', tier='stretch', no='T4', label='T4', type='fields', skill='making a list in order', answer=[9630, 3069], frame=grp('Largest even: {f1}      Smallest odd: {f2}'),
      q='Use the digits 3, 0, 6 and 9 once each. Make the largest even 4-digit number and the smallest odd 4-digit number. Fill in the boxes.',
      check=lambda: [max(numbers_from_digits([3, 0, 6, 9], lambda n: n % 2 == 0)), min(numbers_from_digits([3, 0, 6, 9], lambda n: n % 2 == 1))],
      hint='An even number ends in 0, 2, 4, 6 or 8. An odd number ends in 1, 3, 5, 7 or 9. A 4-digit number cannot start with 0.',
      steps=['Even numbers end in 0 or 6. For the largest, put 9, 6, 3 in front and end with 0: 9630.', 'Odd numbers end in 3 or 9. For the smallest, put the smallest digits at the front: 3, then 0, then 6, then 9: 3069 (it ends in 9, so it is odd).', 'The numbers are 9630 and 3069.'],
      src=['Use the digits 3, 0, 6 and 9 once each. Make the largest even 4-digit number and the smallest odd 4-digit number.']),

    # ================= Go further (workbook Go further, No.5 to No.7) and the Extra questions (printed as "Take-home")
    I(id='G5', tier='challenge', no='G5', label='G5', type='selfcheck', open=True, marking_mode='open', skill='making up a puzzle',
      q='Make up your own logic puzzle with 3 people and 3 things (colours, pets or sports). Write 3 or 4 clues. Test it on a partner: does it have exactly ONE answer? Is there a clue you could take away and still have only one answer?',
      hint='Pick the answer first: who has which thing. Then write clues that rule out the other ways, one at a time.',
      steps=['Answers vary. Check that the clues fit one arrangement only (try every arrangement of the 3 things).', 'Example: Sam, Lee and Mei wear red, blue and green. Clues: Sam is not wearing red. Lee is not wearing blue. Mei is not wearing green. Sam is not wearing blue. The only answer is Sam green, Lee red, Mei blue.', 'The clue "Mei is not wearing green" could be taken away and there is still only one answer.'],
      src=['Make up your own logic puzzle with 3 people and 3 things (colours, pets or sports).']),
    I(id='G6', tier='challenge', no='G6', label='G6', type='number', skill='queues (draw it)', answer=13,
      q='In a queue, Siti is 6th from the front and Ravi is 4th from the back. There are 3 children between them, and Siti is in front of Ravi. How many children are in the queue? Type the number.',
      check=lambda: (lambda ravi_front: ravi_front + 4 - 1)(6 + 3 + 1),
      hint='Draw circles. Siti is the 6th. Count the 3 children between, then Ravi. Then add the children behind Ravi.',
      steps=['Siti is 6th. The 3 children between are 7th, 8th and 9th, so Ravi is 10th from the front.', 'Ravi is 4th from the back, so there are 3 children behind him.', '10 + 3 = 13 children in the queue.'],
      src=['In a queue, Siti is 6th from the front and Ravi is 4th from the back. There are 3 children between them, and Siti is in front of Ravi. How many children are in the queue?']),
    I(id='G7', tier='challenge', no='G7', label='G7', type='fields', skill='logic with bar graphs', answer=[40, 30, 40, 25], frame=grp('3P1: {f1} kg      3P2: {f2} kg      3P3: {f3} kg      3P4: {f4} kg'),
      q='A bar graph shows the paper collected by 4 classes. 3P1 collected 10 kg more than 3P2. 3P3 collected the same as 3P1. 3P4 collected 5 kg less than 3P2. Altogether they collected 135 kg. How much did each class collect? Fill in the boxes.',
      check=lambda: one(classes_solution()),
      hint='Call the amount of 3P2 one unit. Draw four bars and take away the extras.',
      steps=['Take away the extras: 3P1 has 10 more and 3P3 has 10 more, and 3P4 has 5 less (add 5 back to match). The extras are 10 + 10 - 5 = 15 kg.', '135 - 15 = 120 kg is four equal bars, so 3P2 is 120 ÷ 4 = 30 kg.', '3P1 is 40 kg, 3P3 is 40 kg and 3P4 is 25 kg. Check: 40 + 30 + 40 + 25 = 135.'],
      src=['A bar graph shows the paper collected by 4 classes. 3P1 collected 10 kg more than 3P2. 3P3 collected the same as 3P1. 3P4 collected 5 kg less than 3P2. Altogether they collected 135 kg. How much did each class collect?']),
    I(id='TH-a', tier='challenge', no='Extra (a)', label='Extra (a)', type='number', skill='perimeter', answer=20,
      q=EXTRA + 'A rectangle is 6 cm by 4 cm. What is its perimeter? Type the number of cm.', check=lambda: 6 + 4 + 6 + 4,
      hint='Walk all the way round the rectangle and add the four sides.',
      steps=['The sides are 6, 4, 6 and 4 cm.', '6 + 4 + 6 + 4 = 20.', 'The perimeter is 20 cm.'],
      src=['A rectangle is 6 cm by 4 cm. What is its perimeter?']),
    I(id='TH-b', tier='challenge', no='Extra (b)', label='Extra (b)', type='number', skill='changing units', answer=2050,
      q=EXTRA + '2 kg 50 g = ? g. Type the number.', check=lambda: g_of(2, 50),
      hint='1 kg is 1000 g. Write 2 kg as grams first.',
      steps=['2 kg = 2000 g.', '2000 + 50 = 2050.', '2 kg 50 g = 2050 g.'],
      src=['2 kg 50 g = __ g']),
]

for _d in ITEMS:
    if _d['type'] == 'selfcheck' and 'marking_mode' not in _d:
        _d['marking_mode'] = 'self'
assert cca_solutions() == [dict(Ali='Football', Mei='Chess', Ravi='Swimming', Siti='Choir')] and pet_solutions() == [dict(Ali='Fish', Ben='Cat', Siti='Dog')]
assert riddle_numbers() == [213, 321, 411] and coin_amounts() == [10, 20, 30, 50, 60, 70, 80] and classes_solution() == [[40, 30, 40, 25]]
assert [handshakes(n) for n in range(2, 11)] == [1, 3, 6, 10, 15, 21, 28, 36, 45] and 20 not in [handshakes(n) for n in range(2, 200)]


# ---------------------------------------------------------------- variant families (template + independent oracle over EVERY combination)
VARIANTS = {
    '3a': dict(
        base=dict(f=3, b=5),
        tpl=dict(vars=dict(f=[2, 3, 4, 5, 6, 7], b=[3, 4, 5, 6, 8]), q='Draw it! Queues. A child is number {f} from the front and number {b} from the back of a queue. How many children are in the queue? Type the number.', answer='f+b-1',
                 hint='The child is counted both from the front and from the back. Draw circles for the children in front, the child, and the children behind.',
                 steps=['There are {f} - 1 children in front of the child.', 'There are {b} - 1 children behind the child.', 'Add them and the child: {ans} children altogether.'], paper=True),
        oracle=lambda e: queue_total(e['f'], e['b'])),
    '3b': dict(
        base=dict(p=2, k=3),
        tpl=dict(vars=dict(p=[2, 3, 4], k=[2, 3, 4, 5]), q='Ali is number {p} from the front, Siti is last, and {k} people are between them. How many children are in the queue? Type the number.', answer='p+k+1',
                 hint='Draw circles in order: the children in front of Ali, Ali, the {k} people between, then Siti.', steps=['In front of Ali there are {p} - 1 children.', 'Add Ali, the {k} people between, and Siti.', 'There are {ans} children in the queue.'], paper=True),
        oracle=lambda e: len(['x'] * (e['p'] - 1) + ['Ali'] + ['between'] * e['k'] + ['Siti'])),
    '4b': dict(
        base=dict(a=2, b=5, c=8),
        tpl=dict(vars=dict(a=[1, 2, 4], b=[3, 5, 7], c=[6, 8, 9]), q='Use the cards {a}, {b} and {c} once each in every 3-digit number. How many of the numbers you can make are odd? Type the number.', answer='2*(a%2+b%2+c%2)',
                 hint='Which digit must be in the ones place for an odd number? Which of the cards are odd?', steps=['A number is odd when its last digit is odd.', 'For each odd card, the other two cards can go either way round.', 'There are {ans} odd numbers.']),
        oracle=lambda e: len(odd_numbers([e['a'], e['b'], e['c']]))),
    '5a': dict(
        base=dict(n=8),
        tpl=dict(vars=dict(n=[7, 9, 10, 12, 15]), q='Squares are made in a row with sticks. 1 square uses 4 sticks, 2 squares use 7 sticks and 3 squares use 10 sticks. How many sticks are needed for {n} squares? Type the number.', answer='3*n+1',
                 hint='Each new square adds the same number of sticks. Keep the table going.', steps=['Each new square adds 3 sticks, and 1 square uses 4 sticks.', 'Keep adding 3 up to {n} squares.', '{n} squares need {ans} sticks.'], paper=True),
        oracle=lambda e: sticks_row(e['n'])),
    '5b': dict(
        base=dict(n=10),
        tpl=dict(vars=dict(n=[7, 9, 11, 12, 15]), derive=dict(S='3*n+1'), q='Squares are made in a row with sticks. 1 square uses 4 sticks, 2 squares use 7 sticks and 3 squares use 10 sticks. Ben uses {S} sticks. How many squares does he make? Type the number.', answer='n',
                 hint='Keep the table going until you reach {S} sticks.', steps=['Each new square adds 3 sticks, and 1 square uses 4 sticks.', 'Keep adding 3 until you reach {S}.', 'Ben makes {ans} squares.'], paper=True),
        oracle=lambda e: [n for n in range(1, 80) if sticks_row(n) == 3 * e['n'] + 1][0]),
    'T3': dict(
        base=dict(n=12),
        tpl=dict(vars=dict(n=[8, 10, 15, 20, 25]), q='Triangles are made in a row with sticks: 1 triangle uses 3 sticks, 2 triangles use 5 sticks, 3 triangles use 7 sticks. How many sticks are needed for {n} triangles? Type the number.', answer='2*n+1',
                 hint='Make a table. How many sticks does each new triangle add?', steps=['Each new triangle adds 2 sticks, and 1 triangle uses 3 sticks.', 'So {n} triangles need 3 + ({n} - 1) × 2 sticks.', '{n} triangles need {ans} sticks.'], paper=True),
        oracle=lambda e: triangle_sticks(e['n'])),
    'TH-a': dict(
        base=dict(l=6, w=4),
        tpl=dict(vars=dict(l=[5, 7, 8, 9], w=[3, 4, 6]), q=EXTRA + 'A rectangle is {l} cm by {w} cm. What is its perimeter? Type the number of cm.', answer='2*(l+w)',
                 hint='Walk all the way round the rectangle and add the four sides.', steps=['The sides are {l}, {w}, {l} and {w} cm.', 'Add the four sides.', 'The perimeter is {ans} cm.']),
        oracle=lambda e: e['l'] + e['w'] + e['l'] + e['w']),
    'TH-b': dict(
        base=dict(kg=2, g=50),
        tpl=dict(vars=dict(kg=[1, 3, 4, 5], g=[20, 30, 50, 75, 80, 150, 450]), q=EXTRA + '{kg} kg {g} g = ? g. Type the number.', answer='1000*kg+g',
                 hint='1 kg is 1000 g. Write {kg} kg as grams first.', steps=['{kg} kg = {kg} thousands of g.', 'Add the {g} g.', '{kg} kg {g} g = {ans} g.']),
        oracle=lambda e: g_of(e['kg'], e['g'])),
}
