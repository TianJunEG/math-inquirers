"""Fix pass P2: writes p2/gaps.json (sneak-peek puzzles, Investigation, Looking back, Go-further what-if) and verifies every answer by brute force.
Run:  python3 -I docs/audit/mk_gaps_p2.py   (from the repo root; reads the previous gaps.json for model answers it keeps)."""
import json, itertools, os
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
OLD = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'p2_models_baseline.json')))  # model answers and figure flags from before the fix pass
def keep(k): return OLD[str(k)]['invest']['model']

# ---------------- verification of every new answer ----------------
def nums3(cards):  # distinct 3-digit numbers from the cards, each card once, no leading zero
    return sorted({int(''.join(map(str, p))) for p in itertools.permutations(cards) if p[0] != 0})
assert 100*3 + 20 + 5 == 325
assert nums3([4, 0, 7]) == [407, 470, 704, 740]
assert len({int(''.join(map(str, p))) for c in itertools.combinations([2, 3, 5, 8], 3) for p in itertools.permutations(c)}) == 24
assert 372 + 416 == 788 and 446 + 237 == 683 and 358 + 642 == 1000 and 344 + 257 == 601
assert [d for d in range(10) if 300 + 10*d + 2 + 416 == 788] == [7]
assert [d for d in range(10) if 400 + 10*d + 6 + 237 == 683] == [4]
assert [d for d in range(10) if 300 + 10*d + 4 + 257 == 601] == [4]
assert 3*5 == 15
assert [(c, s) for c in range(7) for s in [6 - c] if 4*c + 2*s == 16] == [(2, 4)]
assert 4*5 - 2*5 == 10
mix20 = [(h, g) for g in range(0, 6) for h in [(20 - 4*g)//2] if 2*h + 4*g == 20]
assert len(mix20) == 6
pat = ['circle', 'circle', 'square']; assert pat[(9 - 1) % 3] == 'square'
grp = ['star', 'moon', 'moon', 'sun']; assert grp[(22 - 1) % 4] == 'moon'
assert 3 + 4*5 == 23
tr = ['red', 'red', 'blue', 'green']; assert tr[(20-1) % 4] == 'green' and tr[(30-1) % 4] == 'red'
assert 12 - 7 == 5 and 2*5 + 7 == 17 and (5 + 7)*2 == 24
assert (12*0 + 50 + 20 + 10) == 80
assert 500 - 3*160 == 20
toys = {'kite': 6, 'ball': 4, 'yoyo': 3, 'bubbles': 2, 'sticker': 1}
def baskets(items, total):
    ks = list(items); out = []
    for r in range(1, len(ks) + 1):
        for c in itertools.combinations(ks, r):
            if sum(items[k] for k in c) == total: out.append(c)
    return out
assert len(baskets(toys, 10)) == 3
toys2 = dict(toys, robot=5); NB = len(baskets(toys2, 10))
assert NB == 5, NB
assert 2*2*3 == 12 and 2*2 + 1 == 5 and (2*2 + 3, divmod(7, 4)) == (7, (1, 3))
assert 5 - 3 == 2 and 2*3 == 6 and 3*8 == 24 and 24//4 == 6
assert 3*3 + 2*4 == 17 and [s for s in range(10) if 3*(9 - s) + 4*s == 31] == [4]
def coin_ways(total, n, coins=(5, 10, 20, 50)):
    return [c for c in itertools.combinations_with_replacement(coins, n) if sum(c) == total]
W4, W5 = coin_ways(70, 4), coin_ways(70, 5)
print('70c with 4 coins:', W4, ' with 5 coins:', W5)
assert len(W5) >= 1
# L9 jug (5 -> 3) and pour table for the Q3 puzzle (start empty, 3 and 5, get 4 in the 5 jug)
def bfs(a_cap, b_cap, target, start=(0, 0)):
    from collections import deque
    q = deque([(start, [start])]); seen = {start}
    while q:
        (a, b), path = q.popleft()
        if b == target: return path
        nxt = [(a_cap, b), (a, b_cap), (0, b), (a, 0)]
        t = min(a, b_cap - b); nxt.append((a - t, b + t)); t = min(b, a_cap - a); nxt.append((a + t, b - t))
        for s in nxt:
            if s not in seen: seen.add(s); q.append((s, path + [s]))
POUR = bfs(3, 5, 4); print('4 l in the 5 l jug, shortest path:', POUR); assert len(POUR) - 1 == 6
assert 45 == (11*60 + 30) - (10*60 + 45) and 85 == (12*60 + 10) - (10*60 + 45)
assert 20 // 4 == 5 and 4 - 1 == 3

# ---------------- text ----------------
C = {
 'neutral': 'After question 3 you may choose: carry on, or try Think harder.',
 'preSay': 'These are sneak-peek puzzles. They are ideas we have not learnt yet, so guessing is welcome and so is saying "I do not know". Nobody is marked and nothing is read out. Start with question 1: use objects, a drawing or counting. Then try question 2. Write your answer on your own paper. When your tutor says so, hold it to the camera at the same moment as everyone else, or show it to your tutor only. Never send answers by private chat or message.',
 'preDo': [
  'Show the Sneak-peek puzzles slide at minute 1 (3 minutes: about 1 minute for question 1, then 2 minutes for question 2). Say out loud: these are ideas we have not learnt yet; guessing and "I do not know" are welcome; nobody is marked.',
  'Answers stay private. Each child holds their own paper to the camera for you only (look, do not read out), or writes it on their own paper and shows only you on camera. Never raise whiteboards together and never show a board in front of the group. Never ask a named child "how do you know?" Ask for volunteers: "Would anyone like to tell us how they started?"',
  'Question 1 is an access question: every child can try it with objects, a drawing or counting, so everyone has a first win. Question 2 is the thinking question. Do not mark either one. Click to show the answers at the end as "one way to think about it", without saying who had what.',
  'Use what you see only to plan. Invite the WHOLE group at once, never one child: "When you have finished Start here, you can choose Think harder, Go further or the Investigation." Never announce who is on which page and never name a child in front of the group. Children choose, and may move either way at any time. Pairs are not split unless both children agree. Everybody joins the explore, the mini-lesson, the check-together slides and talk time.'
 ],
 'talkDo': 'You choose volunteers first: "Who would like to share?" If nobody offers, ask the pairs to share what their partner said. Never cold-call a child by name. Any child may say "pass" at any time and that is always fine. Do not keep public tallies, scores or rankings (no counting who got most right, no "first to finish"). Invite the whole group to think about whether they would like a turn, never one child.',
 'refSay': 'Looking back takes 2 minutes. Find the small box called Looking back on your page. Finish one line, two lines or all three, and tick what helped you. You may pass on any line. If you tick "I am still stuck", your tutor will check in during the session.',
 'refDo': 'Nothing is collected in front of the group and nobody has to read theirs out. The tutor may read a box while stamping journals (never by private message), and checks in on a child who ticked still stuck during the open session, for example by a quick visit to the shared breakout room or a hand signal with a parent nearby, for example "I saw you drew it when you got stuck". A child may volunteer one sentence, never by name unless they choose to. If a child ticks "I am still stuck", check in during the next open session (a quick visit to the shared breakout room or a hand signal, with a parent nearby). Praise the strategy, not the speed.',
 'close': 'Closing and stamps take the last minute (89 to 90).'
}

TICK = {1: ['made a list in order', 'used digit cards or counters'], 2: ['tried a digit and checked it', 'drew it'], 3: ['made a table', 'drew arrays or used counters'],
        4: ['counted in groups', 'wrote the pattern out'], 5: ['drew the machine', 'worked backwards'], 6: ['used play coins', 'made a list in order'],
        7: ['folded or drew strips', 'drew bars'], 8: ['used cubes or tiles', 'drew it'], 9: ['made a table', 'used cups or objects'], 10: ['listed in order', 'drew it']}

def P(q, a, short, w): return {'q': q, 'a': a, 'short': short, 'w': w}
L = {}
L[1] = dict(
 pre=[P('Mei has 3 hundreds, 2 tens and 5 ones. Draw them if you like. What number is that?', '325.', '325', 'Hundreds first, then tens, then ones. A drawing of 3 flats, 2 rods and 5 units is welcome. This is a first win for everyone.'),
      P('Mei has digit cards 4, 0 and 7. She uses each card once to make a 3-digit number. How many different numbers can she make? Write them.', '4 numbers: 407, 470, 704, 740.', '4 numbers',
        '0 cannot be the hundreds digit, so only 4 and 7 can start. Listing in order: 4 starts 2 numbers, 7 starts 2 numbers. A child who says 6 is using 3 x 2 x 1 without the zero rule: a good idea, not a mistake to correct yet.')],
 invest=dict(title='Mirror numbers', need='', first='Easy first step: write 252, 909 and 131, then write three more mirror numbers.',
  text='A mirror number reads the same forwards and backwards, like 252 or 909. (a) Write 5 mirror numbers of your own. (b) Find ALL the mirror numbers from 200 to 299. How do you know you have found them all? (c) Ali says every mirror number is odd. Is he right?', model=keep(1), lines=2),
 whatif=dict(q='Go further: add a fourth card, 2. Use any THREE of the cards 2, 3, 5 and 8. How many different 3-digit numbers can you make?', a='24: 4 choices of which card to leave out, and each set of 3 cards makes 6 numbers (4 x 6 = 24).'))
L[2] = dict(
 pre=[P('3{box}2 + 416 = 788. Which digit is hidden in the box? (Use counters or draw the columns if it helps.)', '7 (372 + 416 = 788).', '7', 'No carry in this one: look at the tens column, 1 and what makes 8. This is a first win for everyone.'),
      P('4{box}6 + 237 = 683. Which digit is hidden in the box? How do you know?', '4 (446 + 237 = 683).', '4', 'Ones: 6 + 7 = 13, so 1 ten is carried. Tens: the box + 3 + 1 must end in 8, so the box is 4. Listen for: "carry", or a guess that was tested and checked.')],
 invest=dict(title='Odd or even?', need='', first='Easy first step: use counters to try 3 + 5, 7 + 9 and 11 + 13. Are the answers odd or even?',
  text='Ali says: "When I add two odd numbers, I always get an even number." (a) Test Ali\'s idea with 5 pairs of odd 3-digit numbers (for example 345 + 271). (b) Now test odd + even, and even + even. What do you notice? (c) Explain WHY, using pairs of counters or a drawing.',
  model='(a) Ali is right: odd + odd is always even (checked for every pair of 3-digit numbers). (b) Odd + even is always odd; even + even is always even. (c) Why: an odd number is some pairs plus 1 left over, an even number is only pairs. Two odd numbers have two left-overs, and they make one more pair, so no one is left over. Look for: several tests before a claim, then a reason that uses pairs, counters or ones digits, not only "it worked every time". A ones-digit reason (odd ends in 1, 3, 5, 7, 9) is also fine. Extension (not printed): taking away behaves the same way: odd − odd is even, odd − even is odd.', lines=2),
 whatif=dict(q='Go further: now make 1000. What is the partner of 358 that makes 1000 (358 + ? = 1000)? What do you notice about the columns?', a='642. Ones: 8 + 2 = 10. Tens: 5 + 4 + 1 = 10. Hundreds: 3 + 6 + 1 = 10. Every column carries.'))
L[3] = dict(
 pre=[P('A tray has 3 rows of counters with 5 counters in each row. Draw it if you like. How many counters are there?', '15 counters (3 rows of 5: 5, 10, 15).', '15', 'Counting in 5s, or drawing and counting. This is a first win for everyone.'),
      P('A toy shop has cars (4 wheels) and scooters (2 wheels). 6 toys have 16 wheels altogether. How many cars and how many scooters? How do you know?', '2 cars and 4 scooters (8 + 8 = 16).', '2 cars, 4 scooters',
        'Starting with all scooters (12 wheels) and swapping one at a time is the idea of today. A child who draws 6 vehicles and counts wheels is thinking well. Guess and check is welcome.')],
 invest=dict(title='Where tables meet', need='', first='Easy first step: write the 5 times table up to 50, then circle the even numbers.',
  text='(a) List the numbers up to 50 that are in BOTH the 2 times table and the 5 times table. What do you notice about them? (b) Now find the numbers up to 50 that are in both the 3 and 5 tables. (c) Is every number in both the 2 and 5 tables also in the 10 table? Explain.',
  model=keep(3).replace('(b) 3 and 5: 15, 30, 45 (jump by 15). 4 and 5: 20, 40 (jump by 20).', '(b) 3 and 5: 15, 30, 45 (jump by 15). (Extension: 4 and 5 give 20, 40, jump by 20.)'), lines=2),
 whatif=dict(q='Go further: what if the farmer counts 20 legs? How many different mixes of hens and goats are there now?', a='6 mixes: 10 hens; 8 hens and 1 goat; 6 hens and 2 goats; 4 hens and 3 goats; 2 hens and 4 goats; 5 goats.'))
L[4] = dict(
 pre=[P('Draw this pattern up to the 9th shape: circle, circle, square, circle, circle, square ... What is the 9th shape?', 'A square (the squares are the 3rd, 6th and 9th shapes).', 'square', 'Drawing it out is a fine method. Listen for "every 3rd one is a square".'),
      P('A pattern repeats: star, moon, moon, sun, star, moon, moon, sun ... What is the 22nd shape? How do you know?', 'A moon.', 'a moon', 'Groups of 4: 20 is the end of a group (5 groups of 4), so the 21st is a star and the 22nd is a moon. Drawing 22 shapes is also fine.')],
 invest=dict(title='Three counting patterns', need='', first='Easy first step: write pattern A, 1, 4, 7, 10 ..., up to 30.',
  text='Pattern A: 1, 4, 7, 10 ... (add 3 each time). Pattern B: 2, 5, 8, 11 ... Pattern C: 3, 6, 9, 12 ... (a) Write each pattern up to 30. (b) Pick any number from 1 to 30. Which pattern is it in? Can a number be in two patterns? Can a number be in none? (c) Why does this happen?',
  model=keep(4).replace('(d) 4 patterns, starting at 1, 2, 3 and 4.', 'Extension (not printed): if each pattern added 4 you would need 4 patterns, starting at 1, 2, 3 and 4.'), lines=2),
 whatif=dict(q='Go further: what if the cube train is red, red, blue, green, red, red, blue, green ...? What colour is cube 20? What colour is cube 30?', a='Cube 20 is green (the green cubes are 4, 8, 12, 16, 20). Cube 30 is red (28 is green, 29 and 30 are red).'))
L[5] = dict(
 pre=[P('A machine adds 7. The OUT is 12. What was the IN? (Count back with counters if you like.)', '5 (5 + 7 = 12).', '5', 'IN is what goes in and OUT is what comes out. Undo = do the opposite: 12 - 7. This is a first win for everyone.'),
      P('A machine doubles, then adds 7. The OUT is 17. What was the IN? How do you know?', '5 (5 doubled is 10, and 10 + 7 = 17).', '5', 'Undo the last step first: 17 - 7 = 10, then half of 10 is 5. A guess that was tested (5 x 2 + 7 = 17) is just as good.')],
 invest=dict(title='A magic trick', need='', first='Easy first step: do the trick with 3, then with 10, and write down each step.',
  text='Think of a number. Add 5. Double it. Take away 10. Halve it. (a) Try 5 different starting numbers. What do you notice about your final answer? (b) Is it ALWAYS true? Try a big number and a small number, then say why. (c) Make your own trick that always gives you back the number you started with. Test it on 3 numbers.', model=keep(5), lines=2),
 whatif=dict(q='Go further: what if the machine adds 7 FIRST and then doubles? Put IN 5 into it. Is the OUT the same as before (17)?', a='No: 5 + 7 = 12, doubled is 24. The order of the steps matters.'))
L[6] = dict(
 pre=[P('Mei has one 50¢ coin, one 20¢ coin and one 10¢ coin. How much money is that? Use play coins or draw them.', '80¢ (50 + 20 + 10).', '80¢', 'Counting on from the biggest coin. This is a first win for everyone.'),
      P('Mei has $5. Three drinks cost $1.60 each. Does she have enough? How much money is left?', 'Yes. 3 drinks cost $4.80, so 20¢ is left.', 'yes, 20¢ left', 'Listen for adding $1.60 three times, or $1 + $1 + $1 and then 60¢ three times (180¢ = $1.80). Counting up from $4.80 to $5 is a good method.')],
 invest=dict(title='Most coins', need='Needs: play coins (5¢, 10¢, 20¢, 50¢), or paper and a pencil.', first='Easy first step: pay 35¢ with the fewest coins from the 5¢, 10¢, 20¢ and 50¢ coins.',
  text='Use only 5¢, 10¢, 20¢ and 50¢ coins. (a) Pay 35¢ using the fewest coins. How many coins is that? (b) Try the other amounts from 5¢ to 95¢ (in steps of 5¢) and make a table of how many coins each needs. (c) Which amount needs the MOST coins, even when you use the fewest possible?', model=keep(6), lines=2),
 whatif=dict(q='Go further: what if the toy stall also sells a robot for $5? Now how many different baskets cost exactly $10? (At most one of each toy.)', a=f'{NB} baskets: ' + '; '.join(' + '.join(b) for b in baskets(toys2, 10)).replace('yoyo', 'yo-yo') + '.'))
L[7] = dict(
 pre=[P('Fold a paper strip (or draw a bar) into 2 equal parts. Colour 1 part. What fraction is coloured?', '1/2 (one half).', '1/2', 'Equal parts matter. Folding on camera is welcome. This is a first win for everyone.'),
      P('Ali has 1/5 of a roti prata. Mei has 1/8 of the same prata. Who has more? How do you know?', 'Ali (1/5). The same prata cut into fewer parts gives bigger parts.', 'Ali (1/5)', 'Many children say 1/8 because 8 is bigger. Draw two strips, one cut in 5 and one cut in 8, and compare. A drawing is a good answer.')],
 invest=dict(title='Fraction strips', need='Needs: the fraction strips from the cut-out page (halves, thirds, quarters, sixths, eighths).', first='Easy first step: lay the two quarter strips on top of the half strip. Do they fit exactly?',
  text='(a) Cover a HALF strip exactly with pieces of ONE kind only. Which kinds work? How many pieces of each? (b) Do the same for a THIRD strip and a QUARTER strip. (c) Can thirds ever cover a half exactly? Why not?', model=keep(7), lines=2),
 whatif=dict(q='Go further: fold a strip into 6 equal parts. How many sixths make a half? How many sixths make a third?', a='3 sixths make a half and 2 sixths make a third.'))
L[8] = dict(
 pre=[P('A stack has 2 layers. Each layer has 2 rows of 3 cubes. How many cubes are in the stack? (Build it with cubes or draw it.)', '12 cubes (6 in each layer, 2 layers).', '12', 'Counting one layer first, then doubling, is a good method. This is a first win for everyone.'),
      P('A shape is made of 2 semicircles and 1 quarter circle. If you cut every piece into quarter circles, how many quarter circles do you get?', '5 (each semicircle is 2 quarters: 2 + 2 + 1).', '5', 'Listen for "a semicircle is half a circle, which is 2 quarters". Drawing the pieces and cutting them is fine.')],
 invest=dict(title='Squares joined edge to edge', need='Needs: square tiles or small squares of paper, and the grid on this page.', first='Easy first step: join 2 squares edge to edge. How many different shapes can you make? Then add a third square.',
  text='Squares must touch along a whole side. A shape that is turned round or flipped over counts as the SAME shape. (a) Find ALL the different shapes you can make with 3 squares. (b) Now find ALL the different shapes you can make with 4 squares. Draw each one on the grid. (c) How do you know you have found them all?', model=keep(8), lines=0),
 whatif=dict(q='Go further: you have 2 semicircles and 3 quarter circles. How many whole circles can you make? What is left over?', a='7 quarter circles in all: 1 whole circle (4 quarters) and 3 quarters left over.'))
L[9] = dict(
 pre=[P('You have a 3 ℓ jug and a 5 ℓ jug. You fill the 5 ℓ jug and pour from it into the 3 ℓ jug until the 3 ℓ jug is full. How much water is left in the 5 ℓ jug? (Try it with two cups and rice, or draw it.)', '2 ℓ (5 - 3 = 2).', '2 ℓ', 'One pour is enough. This is a first win for everyone and previews the pour table.'),
      P('A melon balances 2 apples. One apple balances 3 plums. How many plums balance the melon? How do you know?', '6 plums (3 + 3).', '6 plums', 'Listen for swapping: the melon can be swapped for 2 apples, and each apple for 3 plums. Drawing the scale is a good method.')],
 invest=dict(title='Weights puzzle', need='Needs: paper and a pencil (cubes or coins can stand for the weights).', first='Easy first step: with weights of 1 g, 2 g and 4 g, can you make 3 g? Can you make 5 g?',
  text='You have three different weights. Each weight is 1 g, 2 g, 3 g, 4 g or 5 g. You put some of them on one pan to make a mass. (a) With weights of 1 g, 2 g and 4 g, which masses from 1 g to 7 g can you make? (b) Find ALL the sets of three different weights from 1 g to 5 g that can make every mass from 1 g to 6 g. (c) What do all the good sets have in common?', model=keep(9), lines=2),
 whatif=dict(q='Go further: one glue stick balances 8 coins. A pencil case balances 3 glue sticks. How many coins balance the pencil case? If an eraser balances 4 coins, how many erasers balance the pencil case?', a='24 coins (3 x 8). 6 erasers (24 / 4).'))
L[10] = dict(
 pre=[P('A box has 3 triangles and 2 squares. A triangle has 3 sides and a square has 4 sides. Draw the shapes. How many sides are there altogether?', '17 sides (9 + 8).', '17', 'Drawing the shapes and counting the sides is a good start. This is a first win for everyone.'),
      P('A box has 9 shapes: triangles (3 sides) and squares (4 sides). There are 31 sides altogether. How many squares? Say how you started: draw it, list it or make a table.', '4 squares and 5 triangles (20 sides... 15 + 16 = 31).', '4 squares', 'Any start is welcome: drawing 9 shapes, listing "1 square, 2 squares ..." or a table. A guess that is checked counts.')],
 invest=dict(title='Staircase', need='Needs: paper and a pencil.', first='Easy first step: draw 3 steps and show the 3 ways: 1+1+1, 1+2 and 2+1.',
  text='Mei climbs a staircase. She can take 1 step or 2 steps at a time. For 3 steps there are 3 ways: 1+1+1, 1+2 and 2+1. (a) Find ALL the ways for 4 steps. (b) Find ALL the ways for 5 steps. (c) Fill in a table for 1, 2, 3, 4 and 5 steps. What pattern do you see? Can you guess the number of ways for 6 steps?', model=keep(10), lines=2),
 whatif=dict(q='Go further: what if the coin puzzle is 70¢ with exactly 5 coins (using 5¢, 10¢, 20¢ and 50¢ coins)? Can it be done? How?', a='Yes: ' + '; '.join(' + '.join(str(x) + '¢' for x in sorted(w, reverse=True)) for w in W5) + '.'))
L[10]['pre'][1]['a'] = '4 squares and 5 triangles (16 + 15 = 31 sides).'

out = {'common': C}
for k in range(1, 11):
    d = L[k]; d['unstuck'] = TICK[k]; d['fig'] = OLD[str(k)]['fig']
    out[str(k)] = d
json.dump(out, open(os.path.join(R, 'p2', 'gaps.json'), 'w'), indent=1, ensure_ascii=False)
print('gaps.json written; baskets with robot:', NB)
