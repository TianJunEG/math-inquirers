"""Online practice for Level 1 (Primary 1, ages 6-8) holiday lesson 8: Logic and Sorting ("Logic Lab").

Questions as printed in the Level 1 holiday workbook (hp/workbook_html.js lesson 8, Q1 to Q6; hp/qbank.json lesson 8 stretch[0:4] for Think harder and challenge[-3:] for Go further, as the
workbook builder slices them; hp/gaps.json lesson 8 for the Investigation and the extra Think harder T5).  Every answer is recomputed by an independent checker that tries ALL possibilities:
all orders of the children / things are listed and only those that obey every clue are kept (there must be exactly one); numbers are sorted by testing each one against each loop's rule; riddles
are solved by testing every number.  The build stops if a checker and the printed answer (Tutor Guide answer key) differ.
"""
import itertools, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from p1lib import *      # noqa: E402,F401

META = dict(level=1, lesson=8, key='p1', title='Logic Lab', workbook_title='LOGIC LAB', topic='Logic and Sorting',
            strand='Logic: ordering and sorting',
            sources=['hp/workbook_html.js', 'hp/qbank.json', 'hp/gaps.json'],
            intro=['Use the clues one at a time. Rule out what cannot be true. Every clue helps you find the answer.',
                   'Some questions ask you to write a list or make up a puzzle. Do those on paper, then check against the answer shown on screen.'])

S = 'Logic: ordering and sorting'


def D(**k):
    return dict(strand=S, **k)


# ---- independent checkers
def orders(things, ok):
    """Every order of `things` (first to last) that obeys the clues `ok(order)`."""
    return [list(o) for o in itertools.permutations(things) if ok(list(o))]


def only(things, ok):
    got = orders(things, ok)
    return got[0] if len(got) == 1 else None


def before(o, a, b):
    return o.index(a) < o.index(b)


def hand_out(people, things, ok):
    """Every way to give each person a different thing that obeys the clues ok(dict person -> thing); there must be exactly one."""
    got = [dict(zip(people, p)) for p in itertools.permutations(things) if ok(dict(zip(people, p)))]
    return got[0] if len(got) == 1 else None


def says(k, n):
    """Is n said when counting in k's from k (k, 2k, 3k ...)?  Counted forwards, not by division."""
    x = k
    while x < n:
        x += k
    return x == n


def region(a, b, nums):
    """Sort numbers into the two loops: counting in a's and counting in b's (or any two tests)."""
    return dict(left=[n for n in nums if a(n) and not b(n)], right=[n for n in nums if b(n) and not a(n)], both=[n for n in nums if a(n) and b(n)], out=[n for n in nums if not a(n) and not b(n)])


TEN = list(range(1, 11))
LESS6 = lambda n: n < 6
ODD = lambda n: n % 2 == 1
Q2 = region(LESS6, ODD, TEN)


def digit_sum(n):
    return sum(int(c) for c in str(n))


def unique(vals):
    return vals[0] if len(vals) == 1 else None


def reasons(nums):
    """For each number, the true reasons (from a list of tests) that only that number has: used for 'which does not belong'."""
    tests = {'it is not in the 3 times table': lambda n: not says(3, n), 'it is the only even number': lambda n: n % 2 == 0, 'it is the only number with two digits': lambda n: n >= 10}
    out = {}
    for n in nums:
        out[n] = [t for t, f in tests.items() if f(n) and sum(1 for m in nums if f(m)) == 1]
    return out


def orders_fig(lst, caption=''):
    body = ''
    for k, o in enumerate(lst):
        body += T(8, 22 + k * 28, f'{k + 1}.  ' + ',  '.join(o), 17, 'start', 800)
    return svg(300, 12 + 28 * len(lst), body, caption or 'All the orders')


KIDS = ['Ali', 'Mei', 'Ben']
VEN = lambda a, b: venn(a, b)

# ======================================================================== the items
ITEMS = [
    # ================= Start here
    D(id='1at', tier='core', no='1(a) tallest', label='1(a) tall', type='choice', skill='ordering from clues', options=['Ali', 'Ben', 'Mei'], answer='Ali',
      q='Ali is taller than Ben. Ben is taller than Mei. Who is the tallest?',
      check=lambda: only(KIDS, lambda o: before(o, 'Ali', 'Ben') and before(o, 'Ben', 'Mei'))[0],
      hint='Think about who is taller than someone. Is anyone taller than the tallest child?',
      steps=['Ali is taller than Ben, and Ben is taller than Mei.', 'The order from tallest is Ali, Ben, Mei.', 'Ali is the tallest.'],
      src=['Ali is taller than Ben. Ben is taller than Mei.']),
    D(id='1as', tier='core', no='1(a) shortest', label='1(a) short', type='choice', skill='ordering from clues', options=['Ali', 'Ben', 'Mei'], answer='Mei',
      q='Ali is taller than Ben. Ben is taller than Mei. Who is the shortest?',
      check=lambda: only(KIDS, lambda o: before(o, 'Ali', 'Ben') and before(o, 'Ben', 'Mei'))[-1],
      hint='Draw the three children in a line, tallest first. Who is at the end?',
      steps=['The order from tallest is Ali, Ben, Mei.', 'The last child is the shortest.', 'Mei is the shortest.'],
      src=['Ali is taller than Ben. Ben is taller than Mei.']),
    D(id='1bh', tier='core', no='1(b) heaviest', label='1(b) heavy', type='choice', skill='ordering from clues', options=['Cat', 'Dog', 'Hen'], answer='Cat',
      q='The cat is heavier than the dog. The hen is lighter than the dog. Which is the heaviest?',
      check=lambda: only(['Cat', 'Dog', 'Hen'], lambda o: before(o, 'Cat', 'Dog') and before(o, 'Dog', 'Hen'))[0],
      hint='Lighter is the opposite of heavier. Put the animals in a line, heaviest first.',
      steps=['The cat is heavier than the dog. The hen is lighter than the dog, so the dog is heavier than the hen.', 'The order from heaviest is cat, dog, hen.', 'The cat is the heaviest.'],
      src=['The cat is heavier than the dog. The hen is lighter than the dog.']),
    D(id='1bl', tier='core', no='1(b) lightest', label='1(b) light', type='choice', skill='ordering from clues', options=['Cat', 'Dog', 'Hen'], answer='Hen',
      q='The cat is heavier than the dog. The hen is lighter than the dog. Which is the lightest?',
      check=lambda: only(['Cat', 'Dog', 'Hen'], lambda o: before(o, 'Cat', 'Dog') and before(o, 'Dog', 'Hen'))[-1],
      hint='Put the animals in a line, heaviest first. Who is at the end?',
      steps=['The order from heaviest is cat, dog, hen.', 'The last animal is the lightest.', 'The hen is the lightest.'],
      src=['The cat is heavier than the dog. The hen is lighter than the dog.']),
    D(id='1c', tier='core', no='1(c)', label='1(c)', type='choice', skill='ordering from clues', answer='Yellow, red, blue, green',
      options=['Red, yellow, blue, green', 'Yellow, red, blue, green', 'Yellow, red, green, blue', 'Green, blue, red, yellow'],
      q='The red ribbon is longer than the blue one. The green one is shorter than the blue one. The yellow one is longer than the red one. Which list goes from longest to shortest?',
      check=lambda: ', '.join(x.capitalize() if i == 0 else x for i, x in enumerate(only(['red', 'blue', 'green', 'yellow'], lambda o: before(o, 'red', 'blue') and before(o, 'blue', 'green') and before(o, 'yellow', 'red')))),
      hint='Take one clue at a time. Put two ribbons in a line, then fit the next ribbon in.',
      steps=['Red is longer than blue, and blue is longer than green: red, blue, green.', 'Yellow is longer than red, so yellow goes first.', 'Longest to shortest: yellow, red, blue, green.'],
      src=['The red ribbon is longer than the blue one.', 'Write them from longest to shortest']),

    D(id='2L', tier='core', no='2 left', label='2 left', type='set', ordered=False, skill='sorting in two loops', answer=Q2['left'],
      q='Write the numbers 1 to 10 in the loops. Which numbers go only in the loop "Numbers less than 6"? Odd numbers end in 1, 3, 5, 7 or 9.',
      svg=venn('Numbers less than 6', 'Odd numbers'), check=lambda: region(LESS6, ODD, TEN)['left'],
      hint='Test each number from 1 to 10 against both loops. This card is for numbers that pass only the first test.',
      steps=['Numbers less than 6: 1, 2, 3, 4, 5. Odd numbers: 1, 3, 5, 7, 9.', 'Only less than 6 (not odd): 2 and 4.'],
      src=['Write 1 to 10 in the loops “Numbers less than 6” and “Odd numbers”.']),
    D(id='2R', tier='core', no='2 right', label='2 right', type='set', ordered=False, skill='sorting in two loops', answer=Q2['right'],
      q='Write the numbers 1 to 10 in the loops. Which numbers go only in the loop "Odd numbers"? Odd numbers end in 1, 3, 5, 7 or 9.',
      svg=venn('Numbers less than 6', 'Odd numbers'), check=lambda: region(LESS6, ODD, TEN)['right'],
      hint='Test each number from 1 to 10 against both loops. This card is for numbers that pass only the second test.',
      steps=['Odd numbers: 1, 3, 5, 7, 9. Numbers less than 6: 1, 2, 3, 4, 5.', 'Only odd (not less than 6): 7 and 9.'],
      src=['Write 1 to 10 in the loops “Numbers less than 6” and “Odd numbers”.']),
    D(id='2O', tier='core', no='2 outside', label='2 outside', type='set', ordered=False, skill='sorting in two loops', answer=Q2['out'],
      q='Write the numbers 1 to 10 in the loops. Which numbers go in the box but outside both loops? Odd numbers end in 1, 3, 5, 7 or 9.',
      svg=venn('Numbers less than 6', 'Odd numbers'), check=lambda: region(LESS6, ODD, TEN)['out'],
      hint='Test each number from 1 to 10 against both loops. Which numbers pass neither test?',
      steps=['A number outside both loops is not less than 6 and not odd.', 'The numbers 1 to 10 that are 6 or more and even are 6, 8 and 10.'],
      src=['Write 1 to 10 in the loops “Numbers less than 6” and “Odd numbers”.']),
    D(id='2a', tier='core', no='2(a)', label='2(a)', type='set', ordered=False, skill='sorting in two loops', answer=Q2['both'],
      q='Numbers in BOTH circles: type them with a comma between. Odd numbers end in 1, 3, 5, 7 or 9.', svg=venn('Numbers less than 6', 'Odd numbers'),
      check=lambda: region(LESS6, ODD, TEN)['both'],
      hint='A number in both circles passes both tests. Test each number from 1 to 10.',
      steps=['Numbers less than 6: 1, 2, 3, 4, 5. Odd numbers: 1, 3, 5, 7, 9.', 'The numbers in both lists are 1, 3 and 5.'],
      src=['Numbers in BOTH circles:']),
    D(id='2b', tier='core', no='2(b)', label='2(b)', type='selfcheck', open=False, marking_mode='self', skill='explaining a sort',
      q='Some numbers go in the middle, where the two loops overlap. Why do they go there?', svg=venn('Numbers less than 6', 'Odd numbers'),
      check=lambda: region(LESS6, ODD, TEN)['both'],
      sol_fig=lambda f: venn('Numbers less than 6', 'Odd numbers', groups=dict(Q2)),
      hint='Look at the two loop names. What must a number be to belong to both?',
      steps=['The left loop is for numbers less than 6. The right loop is for odd numbers.', 'The middle is where the loops overlap, so a number there belongs to both loops.', 'Numbers 1, 3 and 5 are less than 6 AND odd.'],
      src=['Why are they in the middle?']),

    D(id='3A', tier='core', no='3 Ali', label='3 Ali', type='choice', skill='logic grid', options=['Cat', 'Dog', 'Fish'], answer='Fish',
      q='Ali, Mei and Ben each have a different pet: cat, dog or fish. Clue 1: Ali has no cat and no dog. Clue 2: Mei does not have a dog. Which pet does Ali have?', svg=pets_grid(),
      check=lambda: hand_out(KIDS, ['Cat', 'Dog', 'Fish'], lambda h: h['Ali'] not in ('Cat', 'Dog') and h['Mei'] != 'Dog')['Ali'],
      hint='Use the crosses in the grid. Which pet is left for Ali?',
      steps=['Clue 1: Ali has no cat and no dog.', 'The only pet left for Ali is the fish.'],
      src=['Who has which pet? Ali, Mei and Ben each have a different pet: cat, dog or fish.', 'Clue 1: Ali has no cat and no dog.']),
    D(id='3M', tier='core', no='3 Mei', label='3 Mei', type='choice', skill='logic grid', options=['Cat', 'Dog', 'Fish'], answer='Cat',
      q='Ali, Mei and Ben each have a different pet: cat, dog or fish. Clue 1: Ali has no cat and no dog. Clue 2: Mei does not have a dog. Which pet does Mei have?', svg=pets_grid(),
      check=lambda: hand_out(KIDS, ['Cat', 'Dog', 'Fish'], lambda h: h['Ali'] not in ('Cat', 'Dog') and h['Mei'] != 'Dog')['Mei'],
      hint='Rule out what cannot be true. Which pet has Ali got, and which pet can Mei not have?',
      steps=['Ali has the fish (clue 1).', 'Mei does not have a dog (clue 2) and the fish is taken, so Mei has the cat.'],
      src=['Clue 2: Mei does not have a dog.']),
    D(id='3B', tier='core', no='3 Ben', label='3 Ben', type='choice', skill='logic grid', options=['Cat', 'Dog', 'Fish'], answer='Dog',
      q='Ali, Mei and Ben each have a different pet: cat, dog or fish. Clue 1: Ali has no cat and no dog. Clue 2: Mei does not have a dog. Which pet does Ben have?', svg=pets_grid(),
      check=lambda: hand_out(KIDS, ['Cat', 'Dog', 'Fish'], lambda h: h['Ali'] not in ('Cat', 'Dog') and h['Mei'] != 'Dog')['Ben'],
      hint='Find the pets of Ali and Mei first. Which pet is left?',
      steps=['Ali has the fish and Mei has the cat.', 'The dog is the only pet left, so Ben has the dog.'],
      src=['Ali has the ______.   Mei has the ______.   Ben has the ______.']),

    D(id='4a', tier='core', no='4 2nd', label='4 2nd', type='choice', skill='ordering from clues', options=['Ali', 'Ben', 'Mei', 'Sam'], answer='Ali', svg=line_boxes(),
      q='Four children stand in a line: Ali, Ben, Mei and Sam. Mei is first. Ali is in front of Ben. Ben is in front of Sam. Who is 2nd?',
      check=lambda: only(['Ali', 'Ben', 'Mei', 'Sam'], lambda o: o[0] == 'Mei' and before(o, 'Ali', 'Ben') and before(o, 'Ben', 'Sam'))[1],
      hint='Mei takes the first place. Then put Ali, Ben and Sam in the order of the clues.',
      steps=['Mei is 1st.', 'Ali is in front of Ben, and Ben is in front of Sam: Ali, Ben, Sam.', 'Ali is 2nd.'],
      src=['Four children stand in a line: Ali, Ben, Mei and Sam.', 'Mei is first. Ali is in front of Ben. Ben is in front of Sam. Who stands where?']),
    D(id='4b', tier='core', no='4 3rd', label='4 3rd', type='choice', skill='ordering from clues', options=['Ali', 'Ben', 'Mei', 'Sam'], answer='Ben', svg=line_boxes(),
      q='Four children stand in a line: Ali, Ben, Mei and Sam. Mei is first. Ali is in front of Ben. Ben is in front of Sam. Who is 3rd?',
      check=lambda: only(['Ali', 'Ben', 'Mei', 'Sam'], lambda o: o[0] == 'Mei' and before(o, 'Ali', 'Ben') and before(o, 'Ben', 'Sam'))[2],
      hint='Mei is 1st. Put the other three children in the order of the clues.',
      steps=['Mei is 1st, then Ali, then Ben, then Sam.', 'Ben is 3rd.'],
      src=['Mei is first. Ali is in front of Ben. Ben is in front of Sam. Who stands where?']),
    D(id='4c', tier='core', no='4 4th', label='4 4th', type='choice', skill='ordering from clues', options=['Ali', 'Ben', 'Mei', 'Sam'], answer='Sam', svg=line_boxes(),
      q='Four children stand in a line: Ali, Ben, Mei and Sam. Mei is first. Ali is in front of Ben. Ben is in front of Sam. Who is 4th?',
      check=lambda: only(['Ali', 'Ben', 'Mei', 'Sam'], lambda o: o[0] == 'Mei' and before(o, 'Ali', 'Ben') and before(o, 'Ben', 'Sam'))[3],
      hint='Who has to be behind everybody else?',
      steps=['Mei is 1st, then Ali, then Ben, then Sam.', 'Sam is 4th.'],
      src=['Mei is first. Ali is in front of Ben. Ben is in front of Sam. Who stands where?']),

    D(id='5', tier='core', no='5', label='5', type='number', skill='number riddle', answer=15,
      q='Number riddle. I am between 10 and 20. I am odd. You say me counting in 5s. What number am I?',
      check=lambda: unique([n for n in range(11, 20) if ODD(n) and says(5, n)]),
      hint='Count in 5s: which of those numbers are between 10 and 20? Then check which one is odd.',
      steps=['Counting in 5s we say 5, 10, 15, 20, 25 ...', 'Between 10 and 20 there is only 15.', '15 is odd. I am 15.'],
      src=['I am between 10 and 20. I am odd. You say me counting in 5s.']),
    D(id='6', tier='core', no='6', label='6', type='selfcheck', open=False, marking_mode='self', skill='odd one out', svg=tiles([3, 6, 9, 11]),
      q='Which one does NOT belong: 3, 6, 9, 11? Explain why. Find a second reason.',
      check=lambda: reasons([3, 6, 9, 11]), facts={3: [], 6: ['it is the only even number'], 9: [], 11: ['it is not in the 3 times table', 'it is the only number with two digits']},
      hint='Look at the numbers: are they odd or even? Do we say them counting in 3s? How many digits do they have?',
      steps=['11 does not belong: we do not say 11 when counting in 3s (3, 6, 9, 12 ...). A second reason: 11 is the only number with two digits.',
             '6 can also be the one that does not belong: it is the only even number.', 'Any true reason is good.'],
      src=['which one does NOT belong?']),

    # ================= Investigation
    D(id='I1', tier='invest', no='Investigation 1', label='Inv 1', type='selfcheck', open=True, marking_mode='open', skill='listing orders',
      q='Ali, Mei and Ben stand in a line. Write one order they can stand in. Now write a different order.',
      hint='Pick who stands first, then who stands second. For a different order, change places.',
      steps=['One order: Ali, Mei, Ben.', 'A different order: Mei, Ali, Ben.', 'Any two different orders of the three children are good.'],
      src=['Ali, Mei and Ben stand in a line. Write one order they can stand in. Now write a different order.']),
    D(id='I2', tier='invest', no='Investigation 2', label='Inv 2', type='number', skill='listing orders', answer=6,
      q='Ali, Mei and Ben stand in a line. How many different orders can they stand in?', check=lambda: len(orders(KIDS, lambda o: True)),
      hint='Fix who is first. Then list the ways the other two can stand. Do that for each child.',
      steps=['If Ali is first, the others can stand in 2 ways. The same is true when Mei is first, and when Ben is first.', '2 + 2 + 2 = 6.', 'There are 6 orders.'],
      src=['Write ALL the different orders they can stand in.']),
    D(id='I3', tier='invest', no='Investigation 3', label='Inv 3', type='selfcheck', paper=True, skill='listing orders',
      q='Write ALL the different orders that Ali, Mei and Ben can stand in. Do this on paper.', facts=6, check=lambda: len(orders(KIDS, lambda o: True)),
      sol_fig=lambda f: orders_fig([o for o in orders(KIDS, lambda o: True)], 'All 6 orders'),
      hint='Fix who is first, then list the other two both ways. Then change the first child.',
      steps=['Ali first: Ali, Mei, Ben and Ali, Ben, Mei.', 'Mei first: Mei, Ali, Ben and Mei, Ben, Ali. Ben first: Ben, Ali, Mei and Ben, Mei, Ali.', 'That is 6 orders.'],
      src=['Write ALL the different orders they can stand in.']),
    D(id='I4', tier='invest', no='Investigation 4', label='Inv 4', type='selfcheck', open=False, marking_mode='self', skill='explaining a search',
      q='How do you know you have found all the orders?', facts=6, check=lambda: len(orders(KIDS, lambda o: True)),
      hint='Did you do the lists in a careful way, one child first at a time?',
      steps=['Each of the 3 children can be first. After that, the other two can stand in 2 ways.', 'Listing one first child at a time means no order is missed or repeated.', 'Any answer that explains a careful way to list is good.'],
      src=['Look for: a systematic list']),
    D(id='I5', tier='invest', no='Investigation 5', label='Inv 5', type='number', skill='using a clue', answer=4,
      q='Now add a clue: "Ali is not first." How many orders are left?', check=lambda: len(orders(KIDS, lambda o: o[0] != 'Ali')),
      hint='Leave out the orders with Ali in first place. Count the ones that are left.',
      steps=['Leave out the orders that start with Ali: there are 2 of them.', '6 - 2 = 4.', '4 orders are left.'],
      src=['Now add a clue: "Ali is not first." How many orders are left?']),
    D(id='I6', tier='invest', no='Investigation 6', label='Inv 6', type='selfcheck', open=True, marking_mode='open', skill='making a clue',
      q='Make up your own clue so that only ONE order is left. Test your clue on all the orders.',
      hint='Think about who is in front of whom. A clue can use two children or three.',
      steps=['One example: "Ali is in front of Ben and Ben is in front of Mei." Only Ali, Ben, Mei fits.', 'Another example: "Mei is first and Ali is not last." Only Mei, Ali, Ben fits.', 'Any clue that leaves exactly one order after you test it is good.'],
      src=['Make up your own clue so that only ONE order is left.']),

    # ================= Think harder
    D(id='T1', tier='stretch', no='T1', label='T1', type='choice', skill='ordering from clues', options=['Mei', 'Sam', 'Tia', 'Raj'], answer='Tia',
      q='In a race, Sam is ahead of Tia. Tia is ahead of Raj. Mei is ahead of Sam. Who is third?',
      check=lambda: only(['Mei', 'Sam', 'Tia', 'Raj'], lambda o: before(o, 'Sam', 'Tia') and before(o, 'Tia', 'Raj') and before(o, 'Mei', 'Sam'))[2],
      hint='Write the runners in a line, first place first. Put in the clues one at a time.',
      steps=['Mei is ahead of Sam, Sam is ahead of Tia, and Tia is ahead of Raj.', 'The order is Mei, Sam, Tia, Raj.', 'Tia is third.'],
      src=['In a race, Sam is ahead of Tia. Tia is ahead of Raj. Mei is ahead of Sam. Who is third?']),
    D(id='T2a', tier='stretch', no='T2 Bo', label='T2 Bo', type='choice', skill='logic grid', options=['Ball', 'Kite', 'Yo-yo'], answer='Yo-yo',
      q='Ana, Bo and Cy each have a different toy: a ball, a kite or a yo-yo. Bo does not have the kite. Cy has the ball. What toy does Bo have?',
      check=lambda: hand_out(['Ana', 'Bo', 'Cy'], ['Ball', 'Kite', 'Yo-yo'], lambda h: h['Bo'] != 'Kite' and h['Cy'] == 'Ball')['Bo'],
      hint='Cy has the ball. Which two toys are left? Which one can Bo not have?',
      steps=['Cy has the ball, so the kite and the yo-yo are left for Ana and Bo.', 'Bo does not have the kite, so Bo has the yo-yo.'],
      src=['Ana, Bo and Cy each have a different toy: a ball, a kite or a yo-yo. Bo does not have the kite. Cy has the ball. Who has which toy?']),
    D(id='T2b', tier='stretch', no='T2 Ana', label='T2 Ana', type='choice', skill='logic grid', options=['Ball', 'Kite', 'Yo-yo'], answer='Kite',
      q='Ana, Bo and Cy each have a different toy: a ball, a kite or a yo-yo. Bo does not have the kite. Cy has the ball. What toy does Ana have?',
      check=lambda: hand_out(['Ana', 'Bo', 'Cy'], ['Ball', 'Kite', 'Yo-yo'], lambda h: h['Bo'] != 'Kite' and h['Cy'] == 'Ball')['Ana'],
      hint='Find the toys of Cy and Bo first. Which toy is left?',
      steps=['Cy has the ball and Bo has the yo-yo.', 'The kite is left, so Ana has the kite.'],
      src=['Who has which toy?']),
    D(id='T3a', tier='stretch', no='T3 2s', label='T3 2s', type='set', ordered=False, skill='counting in 2s and 3s', answer=[2, 4, 6, 8, 10, 12],
      q='Numbers 1 to 12. Which numbers do we say when counting in 2s?', check=lambda: [n for n in range(1, 13) if says(2, n)],
      hint='Start at 2 and keep adding 2 until you pass 12.',
      steps=['Count in 2s: 2, 4, 6, 8, 10, 12.'],
      src=['Numbers 1 to 12. Which do we say when counting in 2s? Which when counting in 3s? Which in both?']),
    D(id='T3b', tier='stretch', no='T3 3s', label='T3 3s', type='set', ordered=False, skill='counting in 2s and 3s', answer=[3, 6, 9, 12],
      q='Numbers 1 to 12. Which numbers do we say when counting in 3s?', check=lambda: [n for n in range(1, 13) if says(3, n)],
      hint='Start at 3 and keep adding 3 until you pass 12.',
      steps=['Count in 3s: 3, 6, 9, 12.'],
      src=['Which when counting in 3s?']),
    D(id='T3c', tier='stretch', no='T3 both', label='T3 both', type='set', ordered=False, skill='counting in 2s and 3s', answer=[6, 12],
      q='Numbers 1 to 12. Which numbers do we say when counting in 2s AND when counting in 3s?', check=lambda: [n for n in range(1, 13) if says(2, n) and says(3, n)],
      hint='Write the numbers you say counting in 2s. Write the numbers you say counting in 3s. Which are on both lists?',
      steps=['Counting in 2s: 2, 4, 6, 8, 10, 12. Counting in 3s: 3, 6, 9, 12.', 'The numbers on both lists are 6 and 12.'],
      src=['Which in both?']),
    D(id='T4', tier='stretch', no='T4', label='T4', type='set', ordered=False, skill='counting in 2s and 3s', answer=[1, 5, 7, 11],
      q='Numbers 1 to 12. Which numbers do we NOT say when counting in 2s or when counting in 3s?', check=lambda: [n for n in range(1, 13) if not says(2, n) and not says(3, n)],
      hint='Write the numbers you say counting in 2s and counting in 3s. Which numbers from 1 to 12 are not on either list?',
      steps=['In 2s: 2, 4, 6, 8, 10, 12. In 3s: 3, 6, 9, 12.', 'The numbers 1 to 12 on neither list are 1, 5, 7 and 11.'],
      src=['Numbers 1 to 12. Which do we NOT say when counting in 2s or when counting in 3s?']),
    D(id='T5a', tier='stretch', no='T5(a)', label='T5(a)', type='number', skill='number riddle', answer=30,
      q='Number riddle. I am between 20 and 40. When you count in 2s you say me. When you count in 5s you say me too. What number am I?',
      check=lambda: unique([n for n in range(21, 40) if says(2, n) and says(5, n)]),
      hint='Which numbers between 20 and 40 do you say counting in 5s? Which of them do you say counting in 2s?',
      steps=['Counting in 5s between 20 and 40: 25, 30, 35.', 'We say 30 counting in 2s, but not 25 or 35.', 'I am 30.'],
      src=['I am between 20 and 40. When you count in 2s you say me. When you count in 5s you say me too.']),
    D(id='T5b', tier='stretch', no='T5(b)', label='T5(b)', type='number', skill='number riddle', answer=14,
      q='Number riddle. I have 2 digits. When I add my two digits I get 5. I am less than 20. What number am I?',
      check=lambda: unique([n for n in range(10, 20) if digit_sum(n) == 5]),
      hint='Numbers less than 20 with 2 digits start with 1. What must the other digit be?',
      steps=['A 2-digit number less than 20 has 1 tens.', '1 + 4 = 5, so the number is 14.', 'I am 14.'],
      src=['I have 2 digits. When I add my two digits I get 5. I am less than 20.']),

    # ================= Go further
    D(id='C1', tier='challenge', no='Go further 1', label='G1', type='number', skill='number riddle', answer=12,
      q='A secret number is between 10 and 30. It is even, and you say it when counting in 3s. It is 2 more than a number you say when counting in 5s. What is it?',
      check=lambda: unique([n for n in range(11, 30) if n % 2 == 0 and says(3, n) and says(5, n - 2)]),
      hint='First list the even numbers between 10 and 30 that you say counting in 3s. Then test each one against the last clue.',
      steps=['Even numbers you say counting in 3s, between 10 and 30: 12, 18, 24.', 'Take away 2 from each: 10, 16, 22. Only 10 is said when counting in 5s.', 'The secret number is 12.'],
      src=['A secret number is between 10 and 30. It is even, and you say it when counting in 3s. It is 2 more than a number you say when counting in 5s. What is it?']),
    D(id='C2a', tier='challenge', no='Go further 2(a)', label='G2(a)', type='fields', skill='sorting in two loops', answer=[7, 3, 3, 7],
      q='Numbers 1 to 20. Sort them in two loops: "I say it counting in 2s" and "I say it counting in 3s". How many numbers go in each part?',
      frame='2s only: {f1}   3s only: {f2}\nBoth: {f3}   Neither: {f4}', svg=venn('Counting in 2s', 'Counting in 3s'),
      check=lambda: (lambda r: [len(r['left']), len(r['right']), len(r['both']), len(r['out'])])(region(lambda n: says(2, n), lambda n: says(3, n), range(1, 21))),
      hint='List the numbers you say counting in 2s, then in 3s. Sort each number from 1 to 20 into one of the four parts.',
      steps=['Counting in 2s: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20. Counting in 3s: 3, 6, 9, 12, 15, 18.', 'Both: 6, 12, 18 (3 numbers). Only 2s: 7 numbers. Only 3s: 3, 9, 15 (3 numbers).', 'Neither: 20 - 7 - 3 - 3 = 7 numbers.'],
      src=['Numbers 1 to 20. Sort them in a two-loop picture with the loops "I say it counting in 2s" and "I say it counting in 3s". How many numbers go in each part?']),
    D(id='C2b', tier='challenge', no='Go further 2(b)', label='G2(b)', type='fields', skill='sorting in two loops', answer=[5, 0, 5, 10],
      q='Numbers 1 to 20. Now use the loops "counting in 2s" and "counting in 4s". How many numbers go in each part?',
      frame='2s only: {f1}   4s only: {f2}\nBoth: {f3}   Neither: {f4}', svg=venn('Counting in 2s', 'Counting in 4s'),
      check=lambda: (lambda r: [len(r['left']), len(r['right']), len(r['both']), len(r['out'])])(region(lambda n: says(2, n), lambda n: says(4, n), range(1, 21))),
      hint='List the numbers you say counting in 2s, then in 4s. Sort each number from 1 to 20 into one of the four parts.',
      steps=['Counting in 2s: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20. Counting in 4s: 4, 8, 12, 16, 20.', 'Both: 4, 8, 12, 16, 20 (5 numbers). Only 2s: 5 numbers. Only 4s: none.', 'Neither: 20 - 5 - 5 = 10 numbers.'],
      src=['Then use the loops "counting in 2s" and "counting in 4s".']),
    D(id='C2c', tier='challenge', no='Go further 2(c)', label='G2(c)', type='selfcheck', open=False, marking_mode='self', skill='explaining a sort',
      q='You sorted the numbers 1 to 20 two ways: with 2s and 3s, and with 2s and 4s. What is different in the two pictures, and why?',
      check=lambda: (lambda r: len(r['right']))(region(lambda n: says(2, n), lambda n: says(4, n), range(1, 21))), facts=0,
      hint='Look at the part for only one kind of counting. Is anything different? Think about why.',
      steps=['In the 2s and 4s picture no number goes in "4s only". In the 2s and 3s picture, 3, 9 and 15 do.', 'Every number we say counting in 4s we also say counting in 2s, so the 4s loop sits completely inside the 2s loop.', 'Any answer that gives this reason is good.'],
      src=['What is different, and why?']),
    D(id='C3', tier='challenge', no='Go further 3', label='G3', type='selfcheck', open=True, marking_mode='open', skill='making a logic puzzle',
      q='Make up your own "Who has which pet?" puzzle with three friends and three pets. Write clues so that there is only ONE answer. Ask a friend or a grown-up to solve it.',
      hint='Pick the answer first. Then write clues that rule out the other ways, one at a time.',
      steps=['One example: Ana, Bo and Cy have a cat, a dog and a fish. Ana does not have the cat. Bo does not have the dog or the fish. Cy does not have the fish.',
             'Answer: Ana has the fish, Bo has the cat and Cy has the dog. Check by trying all 6 ways to give out the pets.', 'Your own puzzle needs clues that leave exactly one way.'],
      src=['Make up your own "Who has which pet?" puzzle with three friends and three pets. Write clues so that there is only ONE answer. Swap with a partner and check that they find your answer.']),
]

VARIANTS = {
    '5': dict(base=dict(a=10),
              tpl=dict(vars=dict(a=[10, 20, 30, 40, 50]), derive=dict(b='a+10'), q='Number riddle. I am between {a} and {b}. I am odd. You say me counting in 5s. What number am I?', answer='a+5',
                       hint='Count in 5s: which of those numbers are between {a} and {b}? Then check which one is odd.',
                       steps=['Count in 5s from {a}: only one number is between {a} and {b}.', 'I am {ans}.']),
              oracle=lambda e: unique([n for n in range(e['a'] + 1, e['a'] + 10) if ODD(n) and says(5, n)])),
    'T5b': dict(base=dict(s=5),
                tpl=dict(vars=dict(s=[3, 4, 6, 7, 8, 9]), q='Number riddle. I have 2 digits. When I add my two digits I get {s}. I am less than 20. What number am I?', answer='10+s-1',
                         hint='Numbers less than 20 with 2 digits start with 1. What must the other digit be?',
                         steps=['A 2-digit number less than 20 has 1 tens.', 'The other digit makes the digits add to {s}.', 'I am {ans}.']),
                oracle=lambda e: unique([n for n in range(10, 20) if digit_sum(n) == e['s']])),
}
