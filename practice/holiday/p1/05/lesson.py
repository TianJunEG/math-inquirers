"""Online practice for Level 1 (Primary 1, ages 6-8) holiday lesson 5: Working Backwards ("Mystery number").

Questions as printed in the Level 1 holiday workbook (hp/workbook_html.js lesson 5, Q1 to Q5 with the take-home; hp/qbank.json lesson 5 stretch[0:4] for Think harder and
challenge[-3:] for Go further, as the workbook builder slices them; hp/gaps.json lesson 5 for the Investigation).  The pictures are redrawn from the printed ones
(hp/figs_l1_3_l1.js mT1, mT2, queue20, snailWall).  Every answer is recomputed by an independent checker: the mystery number is FOUND by trying every number and running the
steps forwards; machine rules are found from the pairs; queues are counted child by child; the snail is simulated day by day.  The build stops if a checker and the printed
answer (Tutor Guide answer key) differ.
"""
import itertools, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from p1lib import *      # noqa: E402,F401

META = dict(level=1, lesson=5, key='p1', title='Mystery number', workbook_title='MYSTERY NUMBER', topic='Working Backwards',
            strand='Number: working backwards',
            sources=['hp/workbook_html.js', 'hp/qbank.json', 'hp/gaps.json'],
            intro=['Find each mystery number. Try a number and check it. You can also work backwards: start at the end and undo each step.',
                   'Use counters, cups or a drawing on paper if you like.'])

S = 'Number: working backwards'


def D(**k):
    return dict(strand=S, **k)


# ---- independent checkers
def run(steps, x):
    """Do the steps forwards from x: steps are ('+', k) or ('-', k)."""
    for op, k in steps:
        x = x + k if op == '+' else x - k
    return x


def find_start(steps, result, hi=300):
    """The mystery number: try every number from 0 and keep the ones that give `result` when the steps are done forwards. Must be exactly one."""
    found = [x for x in range(0, hi) if run(steps, x) == result]
    return found[0] if len(found) == 1 else None


def machine_gap(pairs):
    """The one number a machine adds (negative = takes away), from the known (IN, OUT) pairs; None if the pairs disagree."""
    d = {o - i for i, o in pairs}
    return d.pop() if len(d) == 1 else None


def add_name(d):
    return f'Add {d}' if d > 0 else f'Take away {-d}'


def queue_behind(n, place):
    """Children behind the child who is `place` from the front, counted one by one in a queue of n."""
    return sum(1 for k in range(1, n + 1) if k > place)


def queue_length(front, back):
    """Smallest queue where the same child is `front` from the front and `back` from the back (tried for every length)."""
    ok = []
    for n in range(1, 60):
        behind = sum(1 for k in range(1, n + 1) if k > front)          # children behind the child who is `front` from the front
        if front <= n and behind + 1 == back:                          # that child is then (behind + 1) from the back
            ok.append(n)
    return ok[0] if len(ok) == 1 else None


def snail_day(wall, up, back):
    """The day on which the snail's top reaches the top of the wall: climb in the day, check, slide back in the night."""
    h, day = 0, 0
    while True:
        day += 1
        h += up
        if h >= wall:
            return day
        h -= back


MARBLES = dict(ali=8, more=5, fewer=6)

ITEMS = [
    # ================= Start here
    D(id='1a', tier='core', no='1(a)', type='number', skill='undoing one step', answer=7,
      q='I think of a number. I add 5. I get 12. Find my number.', svg=machine([('?', 'q'), ('+ 5', 'op'), ('12', 'out')]), check=lambda: find_start([('+', 5)], 12),
      hint='Start at 12 and go backwards. What undoes adding 5?',
      steps=['The machine adds 5 and gives 12.', 'Go backwards: take away 5 from 12. 12 - 5 = 7.', 'Check: 7 + 5 = 12. The mystery number is 7.'],
      src=['I think of a number. I add 5. I get 12.', 'I think of a number. Find it and write it in the yellow box.']),
    D(id='1b', tier='core', no='1(b)', type='number', skill='undoing one step', answer=12,
      q='I think of a number. I take away 3. I get 9. Find my number.', svg=machine([('?', 'q'), ('- 3', 'op'), ('9', 'out')]), check=lambda: find_start([('-', 3)], 9),
      hint='Start at 9 and go backwards. What undoes taking away 3?',
      steps=['The machine takes away 3 and gives 9.', 'Go backwards: add 3 to 9. 9 + 3 = 12.', 'Check: 12 - 3 = 9. The mystery number is 12.'],
      src=['I take away 3. I get 9.']),
    D(id='1c', tier='core', no='1(c)', type='number', skill='undoing two steps', answer=8,
      q='I think of a number. I add 4. Then I take away 2. I get 10. Find my number.', svg=machine([('?', 'q'), ('+ 4', 'op'), ('- 2', 'op'), ('10', 'out')]),
      check=lambda: find_start([('+', 4), ('-', 2)], 10),
      hint='Start at 10. Which step happened last? Undo that one first, then undo the one before it.',
      steps=['The last step was take away 2. Undo it: 10 + 2 = 12.', 'The step before was add 4. Undo it: 12 - 4 = 8.', 'Check going forwards: 8 + 4 = 12, then 12 - 2 = 10. The mystery number is 8.'],
      src=['I add 4. Then I take away 2. I get 10.']),

    D(id='2a', tier='core', no='2(a)', type='fields', skill='number machine table', answer=[15, 8],
      q='A number machine adds the same number every time. It adds 6. Fill in the two missing numbers in the table.',
      frame='IN 9 gives OUT {f1}.      OUT 14 comes from IN {f2}.', svg=in_out_table([2, 5, 9, None], [8, 11, None, 14]),
      check=lambda: (lambda d: [9 + d, 14 - d])(machine_gap([(2, 8), (5, 11)])),
      hint='Use what the machine does to every number. Go forwards for OUT. For the IN, go backwards from 14.',
      steps=['The machine adds 6 to every number: 2 gives 8 and 5 gives 11.', 'IN 9 gives OUT 9 + 6 = 15.', 'OUT 14 came from IN 14 - 6 = 8.'],
      src=['A number machine adds the same number every time.', 'It adds 6. Fill in the table.']),
    D(id='2b', tier='core', no='2(b) rule', label='2(b) rule', type='choice', skill='finding a machine rule', options=['Add 3', 'Add 4', 'Add 7', 'Take away 4'], answer='Add 4',
      q='A different machine. IN 3 gives OUT 7, IN 6 gives OUT 10 and IN 10 gives OUT 14. What does the machine do?',
      svg=in_out_table([3, 6, 10, 15], [7, 10, 14, None]), check=lambda: add_name(machine_gap([(3, 7), (6, 10), (10, 14)])),
      hint='Look at IN 3 and OUT 7. What did the machine do to get from 3 to 7? Test it on IN 6.',
      steps=['IN 3 gives OUT 7, and 7 is 4 more than 3.', 'Test it: 6 + 4 = 10 and 10 + 4 = 14. It works for every pair.', 'The machine adds 4.'],
      src=['A different machine. What does it do?']),
    D(id='2c', tier='core', no='2(b) OUT 15', label='2(b) OUT', type='number', skill='using a machine rule', answer=19,
      q='A machine follows one rule for every number. IN 3 gives OUT 7 and IN 6 gives OUT 10. What is OUT when IN is 15?',
      svg=in_out_table([3, 6, 10, 15], [7, 10, 14, None]), check=lambda: 15 + machine_gap([(3, 7), (6, 10), (10, 14)]),
      hint='Find what the machine does to 3 to make 7. Then do the same to 15.',
      steps=['IN 3 gives OUT 7, so the machine adds 4.', 'IN 15 gives OUT 15 + 4 = 19.'],
      src=['A different machine. What does it do?']),
    D(id='2d', tier='core', no='2(b) IN 30', label='2(b) IN', type='number', skill='working backwards through a machine', answer=26,
      q='If you have time: the same machine gives IN 3 OUT 7 and IN 6 OUT 10. OUT 30 means IN is what number?',
      check=lambda: [i for i in range(0, 200) if i + machine_gap([(3, 7), (6, 10)]) == 30][0],
      hint='The machine got OUT from IN. Go backwards from 30 to find the IN.',
      steps=['The machine adds 4: 3 gives 7 and 6 gives 10.', 'To go backwards from OUT 30, take away 4: 30 - 4 = 26.', 'Check: 26 + 4 = 30. IN is 26.'],
      src=['If you have time: OUT 30 means IN']),

    D(id='3a', tier='core', no='3(a)', type='number', skill='more than', answer=13,
      q='Ali has 8 marbles. Mei has 5 more marbles than Ali. How many marbles does Mei have?', svg=marble_bars(),
      check=lambda: sum(1 for _ in range(MARBLES['ali'])) + sum(1 for _ in range(MARBLES['more'])),
      hint='Mei has all of Ali\'s marbles and some more. You can colour boxes on paper to help.',
      steps=['Ali has 8 marbles. Mei has 5 more than Ali.', '8 + 5 = 13.', 'Mei has 13 marbles.'],
      src=['Ali has 8 marbles. Mei has 5 more marbles than Ali.', 'How many marbles does Mei have?']),
    D(id='3b', tier='core', no='3(b)', type='number', skill='fewer than', answer=7,
      q='Ali has 8 marbles. Mei has 5 more than Ali. Ben has 6 fewer marbles than Mei. How many marbles does Ben have?', svg=marble_bars(),
      check=lambda: MARBLES['ali'] + MARBLES['more'] - MARBLES['fewer'],
      hint='First find how many Mei has. Then Ben has fewer than Mei.',
      steps=['Mei has 8 + 5 = 13 marbles.', 'Ben has 6 fewer than Mei: 13 - 6 = 7.', 'Ben has 7 marbles.'],
      src=['Ben has 6 fewer marbles than Mei.', 'How many marbles does Ben have?']),
    D(id='3c', tier='core', no='3(c)', type='number', skill='comparing', answer=6,
      q='Mei has 5 more marbles than Ali, who has 8. Ben has 6 fewer marbles than Mei. How many more marbles does Mei have than Ben?', svg=marble_bars(),
      check=lambda: (MARBLES['ali'] + MARBLES['more']) - (MARBLES['ali'] + MARBLES['more'] - MARBLES['fewer']),
      hint='Find how many marbles Mei has and how many Ben has. Then find how many more Mei has.',
      steps=['Mei has 8 + 5 = 13 marbles and Ben has 13 - 6 = 7 marbles.', '13 - 7 = 6.', 'Mei has 6 more marbles than Ben.'],
      src=['How many more marbles does Mei have than Ben?']),
    D(id='3d', tier='core', no='3(d)', type='number', skill='adding three numbers', answer=28,
      q='If you have time: Ali has 8 marbles, Mei has 5 more than Ali and Ben has 6 fewer than Mei. How many marbles do they have altogether?', svg=marble_bars(),
      check=lambda: MARBLES['ali'] + (MARBLES['ali'] + MARBLES['more']) + (MARBLES['ali'] + MARBLES['more'] - MARBLES['fewer']),
      hint='Find how many marbles each child has. Then put all three numbers together.',
      steps=['Ali has 8, Mei has 13 and Ben has 7.', '8 + 13 = 21, and 21 + 7 = 28.', 'They have 28 marbles altogether.'],
      src=['If you have time: how many marbles do they have altogether?']),

    D(id='4a', tier='core', no='4(a)', type='number', skill='queue puzzles', answer=13,
      q='There are 20 children in a queue. Mei is 7th from the front. How many children are behind her?', svg=queue_fig(20, 7), check=lambda: queue_behind(20, 7),
      hint='Count only the children behind Mei. Is Mei one of them?',
      steps=['Children 1 to 6 are in front of Mei, and Mei is number 7.', 'The children behind her are numbers 8 to 20. 20 - 7 = 13.', '13 children are behind Mei.'],
      src=['There are 20 children in a queue. Mei is 7th from the front. How many children are behind her?']),
    D(id='4b', tier='core', no='4(b)', type='number', skill='queue puzzles', answer=5,
      q='Ali is 3rd from the front AND 3rd from the back. How many children are in the queue? Draw the children as dots on paper first.', check=lambda: queue_length(3, 3),
      hint='Draw dots on paper. Put Ali 3rd from the front. Then count how many are behind him.',
      steps=['Ali is 3rd from the front, so 2 children are in front of him.', 'Ali is 3rd from the back, so 2 children are behind him.', '2 + Ali + 2 = 5. Do not count Ali twice. There are 5 children.'],
      src=['Ali is 3rd from the front AND 3rd from the back. How many children are in the queue?', 'Draw the children as circles first.']),
    D(id='5', tier='core', no='Take-home', label='Take-home', type='selfcheck', open=True, marking_mode='open', skill='making up a story',
      q='If you have time, or at home: make your own mystery number story. Give it to a friend to solve!',
      hint='Pick a mystery number first. Add or take away to make a story. Write the story and keep the answer secret.',
      steps=['Here is one example: I think of a number. I add 7. I get 23. What is my number?', 'To solve it, go backwards: 23 - 7 = 16.', 'Your own story gives its own answer. Any story that a friend can solve by working backwards is good.'],
      src=['make your own mystery number story. Give it to a friend to solve!']),

    # ================= Investigation
    D(id='I1', tier='invest', no='Investigation 1', type='fields', skill='undoing steps', answer=[3, 10, 25],
      q='A number machine adds 6 and then takes away 6. Try IN = 3, 10 and 25. What comes OUT each time?', frame='IN 3 gives OUT {f1}.   IN 10 gives OUT {f2}.   IN 25 gives OUT {f3}.',
      svg=machine([('IN', 'q'), ('+ 6', 'op'), ('- 6', 'op'), ('OUT', 'out')]), check=lambda: [run([('+', 6), ('-', 6)], x) for x in (3, 10, 25)],
      hint='Do the two steps one at a time. Start with IN 3: add 6, then take away 6.',
      steps=['IN 3: 3 + 6 = 9, then 9 - 6 = 3.', 'IN 10: 10 + 6 = 16, then 16 - 6 = 10. IN 25: 25 + 6 = 31, then 31 - 6 = 25.', 'OUT is 3, 10 and 25.'],
      src=['A number machine adds 6 and then takes away 6. Try IN = 3, 10 and 25. What comes OUT each time?']),
    D(id='I2', tier='invest', no='Investigation 2', type='choice', skill='noticing a pattern', answer='OUT is always the same as IN',
      options=['OUT is always the same as IN', 'OUT is always 6 more than IN', 'OUT is always 6 less than IN', 'OUT is always 12 more than IN'],
      q='Mei tests the machine that adds 6 and then takes away 6 on any number she likes. What does she find?',
      check=lambda: (lambda diffs: {0: 'OUT is always the same as IN', 6: 'OUT is always 6 more than IN', -6: 'OUT is always 6 less than IN', 12: 'OUT is always 12 more than IN'}[diffs.pop()] if len(diffs) == 1 else None)(
          {run([('+', 6), ('-', 6)], x) - x for x in range(0, 100)}),
      hint='Test one number you choose. Then test a different number. What do you see each time?',
      steps=['Try 4: 4 + 6 = 10, then 10 - 6 = 4. Try 20: 20 + 6 = 26, then 26 - 6 = 20.', 'The second step takes away what the first step added, so every number comes back.', 'OUT is always the same as IN.'],
      src=['Test one number you choose.']),
    D(id='I3', tier='invest', no='Investigation 3', type='choice', skill='noticing a pattern', answer='OUT is always 2 more than IN',
      options=['OUT is always 2 more than IN', 'OUT is always 2 less than IN', 'OUT is always 10 more than IN', 'OUT is always the same as IN'],
      q='Now change the machine: add 6, then take away 4. What happens to every number that goes IN?',
      check=lambda: (lambda diffs: {2: 'OUT is always 2 more than IN', -2: 'OUT is always 2 less than IN', 10: 'OUT is always 10 more than IN', 0: 'OUT is always the same as IN'}[diffs.pop()] if len(diffs) == 1 else None)(
          {run([('+', 6), ('-', 4)], x) - x for x in range(0, 100)}),
      hint='Try IN = 3, then IN = 10, then IN = 25. Compare each OUT with its IN.',
      steps=['IN 3: 3 + 6 = 9, then 9 - 4 = 5. IN 10 gives 12, and IN 25 gives 27.', 'Each OUT is 2 more than its IN.', 'OUT is always 2 more than IN.'],
      src=['Now change the machine: add 6, then take away 4.']),
    D(id='I4', tier='invest', no='Investigation 4', type='selfcheck', open=False, marking_mode='self', skill='explaining a pattern',
      q='The machine adds 6 and then takes away 4. Explain why this does the same thing to every number.',
      facts=2, check=lambda: run([('+', 6), ('-', 4)], 0),
      hint='What are the two steps worth together? Think about how many you add and how many you take away.',
      steps=['The machine adds 6, but then takes 4 of them away again.', 'It keeps 6 - 4 = 2 of what it added, so it really adds 2 to every number.', 'Any answer that says the two steps together add 2 (or that 4 of the 6 are taken back) is good.'],
      src=['What happens to every number? Why?']),

    # ================= Think harder
    D(id='T1', tier='stretch', no='T1', type='number', skill='undoing two steps', answer=14,
      q='Ben had some marbles. He gave 5 to Mei, then won 3. Now he has 12. How many did he start with?', svg=machine([('?', 'q'), ('- 5', 'op'), ('+ 3', 'op'), ('12', 'out')]),
      check=lambda: find_start([('-', 5), ('+', 3)], 12),
      hint='Start at 12. Undo what happened last, then undo what happened before that.',
      steps=['Ben gave away 5, then won 3, and now has 12.', 'Undo winning 3: 12 - 3 = 9.', 'Undo giving away 5: 9 + 5 = 14.', 'Check: 14 - 5 = 9, then 9 + 3 = 12. Ben started with 14 marbles.'],
      src=['Ben had some marbles. He gave 5 to Mei, then won 3. Now he has 12. How many did he start with?']),
    D(id='T2', tier='stretch', no='T2', type='number', skill='undoing three steps', answer=15,
      q='Ben had some stickers. He gave away 6, got 4, then gave away 3. Now he has 10. How many did he have at first?',
      svg=machine([('?', 'q'), ('- 6', 'op'), ('+ 4', 'op'), ('- 3', 'op'), ('10', 'out')]), check=lambda: find_start([('-', 6), ('+', 4), ('-', 3)], 10),
      hint='Work backwards one step at a time, starting from the 10. Write each number you get.',
      steps=['Undo the last step (gave away 3): 10 + 3 = 13.', 'Undo getting 4: 13 - 4 = 9.', 'Undo giving away 6: 9 + 6 = 15.', 'Check: 15 - 6 = 9, 9 + 4 = 13, 13 - 3 = 10. Ben had 15 stickers.'],
      src=['Ben had some stickers. He gave away 6, got 4, then gave away 3. Now he has 10. How many did he have at first?']),
    D(id='T3a', tier='stretch', no='T3 rule', label='T3 rule', type='choice', skill='finding a machine rule', options=['Add 4', 'Add 5', 'Add 9', 'Take away 5'], answer='Add 5',
      q='A number machine adds the same number each time. IN 4 gives OUT 9. What is the rule?', check=lambda: add_name(machine_gap([(4, 9)])),
      hint='How much more is 9 than 4?',
      steps=['The machine adds the same number each time.', 'IN 4 gives OUT 9, and 9 - 4 = 5.', 'The rule is add 5.'],
      src=['A number machine adds the same number each time. IN 4 gives OUT 9. What is the rule?']),
    D(id='T3b', tier='stretch', no='T3 find', label='T3 find', type='fields', skill='using a machine rule', answer=[17, 15],
      q='A number machine adds the same number each time. IN 4 gives OUT 9. What is OUT when IN is 12? What is IN when OUT is 20?',
      frame='OUT when IN is 12: {f1}      IN when OUT is 20: {f2}', check=lambda: (lambda d: [12 + d, 20 - d])(machine_gap([(4, 9)])),
      hint='First find what the machine does to 4 to make 9. Go forwards from IN 12. Go backwards from OUT 20.',
      steps=['IN 4 gives OUT 9, so the machine adds 5.', 'IN 12 gives OUT 12 + 5 = 17.', 'OUT 20 came from IN 20 - 5 = 15.'],
      src=['What is OUT when IN is 12? What is IN when OUT is 20?']),
    D(id='T4', tier='stretch', no='T4', type='number', skill='undoing two steps', answer=11,
      q='I think of a number. I add 4, then I take away 7. I get 8. What is my number?', check=lambda: find_start([('+', 4), ('-', 7)], 8),
      hint='Undo the last step first. Then undo the step before it. Check by going forwards.',
      steps=['Undo take away 7: 8 + 7 = 15.', 'Undo add 4: 15 - 4 = 11.', 'Check: 11 + 4 = 15, then 15 - 7 = 8. My number is 11.'],
      src=['I think of a number. I add 4, then I take away 7. I get 8. What is my number?']),

    # ================= Go further
    D(id='C1a', tier='challenge', no='Go further 1(a)', label='G1(a)', type='number', skill='undoing two steps', answer=13,
      q='A number machine has two steps: add 3, then add 4. IN 5 gives OUT 12. What goes IN to give OUT 20?', check=lambda: find_start([('+', 3), ('+', 4)], 20),
      hint='Start at 20. Undo the last step first, then the step before it.',
      steps=['Undo add 4: 20 - 4 = 16.', 'Undo add 3: 16 - 3 = 13.', 'Check: 13 + 3 = 16, then 16 + 4 = 20. IN is 13.'],
      src=['A number machine has two steps: add 3, then add 4. IN 5 gives OUT 12. What goes IN to give OUT 20?']),
    D(id='C1b', tier='challenge', no='Go further 1(b)', label='G1(b)', type='number', skill='one step instead of two', answer=7,
      q='A machine adds 3, then adds 4. Can one step do the same job? What number does a one-step machine add?',
      check=lambda: (lambda ks: ks[0] if len(ks) == 1 else None)([k for k in range(0, 30) if all(x + k == run([('+', 3), ('+', 4)], x) for x in range(0, 50))]),
      hint='Try IN 5 in the two-step machine. What one step takes 5 to the same OUT?',
      steps=['Add 3 and then add 4 is 3 + 4 = 7 altogether.', 'Check with IN 5: 5 + 7 = 12, the same as the two-step machine.', 'A one-step machine that adds 7 does the same job.'],
      src=['Can you make a one-step machine that does the same job?']),
    D(id='C2', tier='challenge', no='Go further 2', label='G2', type='number', skill='day and night puzzles', answer=4,
      q='A snail climbs 3 cm each day and slides back 1 cm each night. It starts at the bottom of a 9 cm wall. On which day does it reach the top? Type the day number.',
      svg=snail_wall(9, 3, 1), check=lambda: snail_day(9, 3, 1),
      hint='Count the height at the end of each day, then the end of each night. Does it reach the top before the night?',
      steps=['Day 1: up to 3 cm, night: back to 2 cm. Day 2: up to 5 cm, night: back to 4 cm.', 'Day 3: up to 7 cm, night: back to 6 cm.', 'Day 4: up to 9 cm. It reaches the top on day 4, before it can slide back.'],
      src=['A snail climbs 3 cm each day and slides back 1 cm each night. It starts at the bottom of a 9 cm wall. On which day does it reach the top?']),
    D(id='C3', tier='challenge', no='Go further 3', label='G3', type='selfcheck', open=True, marking_mode='open', skill='making up a story',
      q='Make up a mystery number story with THREE steps whose answer is 10. Write the story. Show how a partner can work backwards to find 10, and how they can check by going forwards.',
      hint='Start with 10. Add or take away three times and write down where you end. Then write the story that goes with it.',
      steps=['Here is one example: I think of a number. I add 5, I take away 3, then I add 4. I get 16.', 'To go backwards: 16 - 4 = 12, then 12 + 3 = 15, then 15 - 5 = 10. My number is 10.', 'To check forwards: 10 + 5 = 15, 15 - 3 = 12, 12 + 4 = 16.',
             'Your own story needs three steps and must give 10 when the steps are undone in the opposite order.'],
      src=['Make up a mystery number story with THREE steps whose answer is 10. Write the story. Show how a partner can work backwards to find 10, and how they can check by going forwards.']),
]


# ---- variant families (every combination is run against the oracle by the build)
VARIANTS = {
    '1a': dict(base=dict(a=5, r=12),
               tpl=dict(vars=dict(a=[3, 4, 5, 6, 7, 8, 9], r=[11, 12, 13, 14, 15, 16, 17]), q='I think of a number. I add {a}. I get {r}. Find my number.', answer='r-a',
                        hint='Start at {r} and go backwards. What undoes adding {a}?',
                        steps=['The machine adds {a} and gives {r}.', 'Go backwards: take away {a} from {r}.', 'Check: your number + {a} must be {r}. The mystery number is {ans}.']),
               oracle=lambda e: find_start([('+', e['a'])], e['r'])),
    '1b': dict(base=dict(t=3, r=9),
               tpl=dict(vars=dict(t=[2, 3, 4, 5, 6, 7], r=[6, 8, 9, 10, 12, 14]), q='I think of a number. I take away {t}. I get {r}. Find my number.', answer='r+t',
                        hint='Start at {r} and go backwards. What undoes taking away {t}?',
                        steps=['The machine takes away {t} and gives {r}.', 'Go backwards: add {t} to {r}.', 'Check: your number - {t} must be {r}. The mystery number is {ans}.']),
               oracle=lambda e: find_start([('-', e['t'])], e['r'])),
    '1c': dict(base=dict(a=4, b=2, r=10),
               tpl=dict(vars=dict(a=[3, 4, 5, 6], b=[1, 2, 3], r=[8, 9, 10, 11, 12]), q='I think of a number. I add {a}. Then I take away {b}. I get {r}. Find my number.', answer='r+b-a',
                        hint='Start at {r}. Undo the last step first, then undo the step before it.',
                        steps=['Undo take away {b}: {r} + {b}.', 'Then undo add {a}: take {a} away from that.', 'Check going forwards. The mystery number is {ans}.']),
               oracle=lambda e: find_start([('+', e['a']), ('-', e['b'])], e['r'])),
    'T4': dict(base=dict(a=4, b=7, r=8),
               tpl=dict(vars=dict(a=[2, 3, 4, 5], b=[5, 6, 7, 8, 9], r=[6, 8, 10, 12]), q='I think of a number. I add {a}, then I take away {b}. I get {r}. What is my number?', answer='r+b-a',
                        hint='Undo the last step first. Then undo the step before it. Check by going forwards.',
                        steps=['Undo take away {b}: {r} + {b}.', 'Undo add {a}: take {a} away from that.', 'Check going forwards. My number is {ans}.']),
               oracle=lambda e: find_start([('+', e['a']), ('-', e['b'])], e['r'])),
    '3b': dict(base=dict(a=8, m=5, f=6),
               tpl=dict(vars=dict(a=[6, 7, 8, 9, 10], m=[3, 4, 5, 6, 7], f=[2, 3, 4, 5]),
                        q='Ali has {a} marbles. Mei has {m} more than Ali. Ben has {f} fewer marbles than Mei. How many marbles does Ben have?', answer='a+m-f',
                        hint='First find how many Mei has. Then Ben has fewer than Mei.',
                        steps=['Mei has {a} + {m} marbles.', 'Ben has {f} fewer than Mei.', 'Ben has {ans} marbles.']),
               oracle=lambda e: e['a'] + e['m'] - e['f']),
    '4a': dict(base=dict(n=20, k=7),
               tpl=dict(vars=dict(n=[15, 16, 18, 20, 22, 24], k=[4, 5, 6, 7, 8, 9]), q='There are {n} children in a queue. Mei is number {k} from the front. How many children are behind her?', answer='n-k',
                        hint='Count only the children behind Mei. Is Mei one of them?',
                        steps=['Mei is child number {k}, so {k} children are Mei or in front of her.', 'Take them away from {n}.', '{ans} children are behind Mei.']),
               oracle=lambda e: queue_behind(e['n'], e['k'])),
    '4b': dict(base=dict(k=3),
               tpl=dict(vars=dict(k=[2, 3, 4, 5, 6, 7]), q='Ali is number {k} from the front AND number {k} from the back. How many children are in the queue? Draw dots on paper first.', answer='2*k-1',
                        hint='Draw dots on paper. Put Ali in place {k} from the front. Then count how many are behind him.',
                        steps=['Ali has {k} - 1 children in front of him and {k} - 1 behind him.', 'Count Ali once, not twice.', 'There are {ans} children in the queue.']),
               oracle=lambda e: queue_length(e['k'], e['k'])),
    'T3b': dict(base=dict(a=4, b=9, c=12, d=20),
                tpl=dict(vars=dict(a=[3, 4, 5], b=[8, 9, 10, 11], c=[10, 12, 14], d=[18, 20, 22]),
                         q='A number machine adds the same number each time. IN {a} gives OUT {b}. What is OUT when IN is {c}? What is IN when OUT is {d}?',
                         frame='OUT when IN is {c}: {f1}      IN when OUT is {d}: {f2}', answers=dict(f1='c+(b-a)', f2='d-(b-a)'),
                         hint='First find what the machine does to {a} to make {b}. Go forwards from IN {c}. Go backwards from OUT {d}.',
                         steps=['IN {a} gives OUT {b}, so the machine adds {b} - {a}.', 'Go forwards from IN {c}, and backwards from OUT {d}.', 'The answers are {ans}.']),
                oracle=lambda e: dict(f1=e['c'] + machine_gap([(e['a'], e['b'])]), f2=e['d'] - machine_gap([(e['a'], e['b'])]))),
    'C2': dict(base=dict(w=9),
               tpl=dict(vars=dict(w=[7, 9, 11, 13, 15]),
                        q='A snail climbs 3 cm each day and slides back 1 cm each night. It starts at the bottom of a {w} cm wall. On which day does it reach the top? Type the day number.',
                        answer='(w-1)//2', hint='Count the height at the end of each day, then the end of each night. Does it reach the top before the night?',
                        steps=['Each whole day and night the snail gets 3 - 1 = 2 cm higher.', 'On the last day it climbs 3 cm and reaches the top before it can slide back.', 'It reaches the top on day {ans}.']),
               oracle=lambda e: snail_day(e['w'], 3, 1)),
}

for _d in ITEMS:
    if _d['type'] == 'selfcheck' and not _d.get('open') and 'marking_mode' not in _d:
        _d['marking_mode'] = 'self'
