import json, itertools

def cyc(core, pos):
    return core[(pos - 1) % len(core)]

def seqstr(start, step, n, blanks=()):
    out = []
    for i in range(n):
        v = start + i * step
        out.append('__' if i in blanks else str(v))
    return ', '.join(out)

B = {}

# ---------- Lesson 1: number patterns ----------
core = []
for s, d in [(4, 3), (5, 5), (1, 4), (50, -5), (7, 2), (100, -10)]:
    nxt = [s + 4 * d, s + 5 * d]
    rule = 'Add %d.' % d if d > 0 else 'Take away %d.' % (-d)
    core.append(('Write the next two numbers and the rule: ' + seqstr(s, d, 4) + ', __, __', '%d, %d. %s' % (nxt[0], nxt[1], rule)))
stretch = []
for s, d, bl in [(3, 5, (2, 4)), (40, -6, (1, 3))]:
    a = [s + i * d for i in bl]
    rule = 'Add %d.' % d if d > 0 else 'Take away %d.' % (-d)
    stretch.append(('Fill in the missing numbers: ' + seqstr(s, d, 6, bl), '%d and %d. %s' % (a[0], a[1], rule)))
stretch.append(('A pattern starts at 3 and adds 5 each time. What is the 8th number?', str(3 + 7 * 5)))
stretch.append(('A pattern starts at 2 and adds 4 each time. What is the 7th number?', str(2 + 6 * 4)))
stretch.append(('A pattern starts at 60 and takes away 5 each time. What is the 9th number?', str(60 - 8 * 5)))
stretch.append(('Is 30 in the pattern 4, 8, 12, 16 … ? How do you know?', 'No. The pattern goes 28, 32, so it skips 30.'))
stretch.append(('5, 10, 15, 22, 25, 30. Which number does not belong? What should it be?', '22 does not belong. It should be 20.'))
stretch.append(('Start at 50 and take away 7 each time. What is the first number below 20?', '15 (50, 43, 36, 29, 22, 15).'))
chal = [
 ('Frog A jumps in 3s from 0. Frog B jumps in 4s from 0. Which numbers up to 40 do both frogs land on? (Do not count 0.)', '12, 24 and 36.'),
 ('I am in the counting patterns of 3s and of 5s. I am more than 10 and less than 40. Which numbers can I be?', '15 and 30.'),
 ('Ali saves $2 in week 1, $5 in week 2, $8 in week 3 and so on. In which week does he save $29? How much does he save in week 12?', 'Week 10 ($29). Week 12: $35. The rule is add 3.'),
 ('2, 4, 7, 11, 16, __ . What is the next number? Explain the pattern.', '22. The gaps grow: add 2, add 3, add 4, add 5, then add 6.'),
 ('A staircase needs 4 blocks for 1 step, 7 blocks for 2 steps and 10 blocks for 3 steps. How many blocks for 6 steps? How many steps can be built with 31 blocks?', '19 blocks for 6 steps. 31 blocks make 10 steps (add 3 each time).'),
 ('A pattern adds the same number each time. Its 5th number is 20 and it starts at a whole number more than 0. How many different patterns can you make? List the first number and the rule for each.', '4 patterns: start 16 add 1; start 12 add 2; start 8 add 3; start 4 add 4.'),
]
B[1] = (core, stretch, chal)

# ---------- Lesson 2: number bonds ----------
core = [('10 = 3 + __', '7'), ('10 = __ + 8', '2'), ('10 = 6 + __', '4'), ('20 = 5 + __', '15'), ('20 = __ + 12', '8'), ('20 = 17 + __', '3')]
stretch = [('5 + 4 = 6 + __', '3'), ('8 + 2 = 7 + __', '3'), ('9 + 6 = __ + 10', '5'), ('12 + 3 = 10 + __', '5'),
 ('4 + __ + 3 = 10', '3'), ('__ + 6 + 6 = 20', '8'),
 ('6 + 4 = 10, so 16 + 4 = __ and 26 + 4 = __', '20 and 30'),
 ('Write three different ways to make 12 with two numbers.', 'For example 6 + 6, 7 + 5, 9 + 3, 10 + 2, 8 + 4.')]
chal = [
 ('Put 1, 2, 3, 4, 5 and 6 in the triangle so each side adds to 9. Corners 1, 2 and 3. What goes in the middle of each side?', 'Between 1 and 2: 6. Between 2 and 3: 4. Between 3 and 1: 5.'),
 ('Corners 4, 5 and 6, and the numbers 1, 2, 3 in the middles. What do all the sides add to? Where does each middle number go?', 'Each side adds to 12. Between 4 and 5: 3. Between 5 and 6: 1. Between 6 and 4: 2.'),
 ('Two numbers add to 14. One is 2 more than the other. What are they?', '6 and 8.'),
 ('Two numbers add to 20. One is 6 more than the other. What are they?', '7 and 13.'),
 ('Ali has 12 stickers in two hands. The left hand has 4 more than the right. How many in each hand?', 'Left 8, right 4.'),
 ('Three different numbers from 3 to 7 add to 15. What can they be? Find both ways.', '3, 5, 7 and 4, 5, 6.'),
 ('How many different pairs make 8 if the order matters (0 + 8 and 8 + 0 are different)? How many if the order does not matter?', '9 pairs when the order matters; 5 pairs when it does not (0+8, 1+7, 2+6, 3+5, 4+4).'),
]
B[2] = (core, stretch, chal)

# ---------- Lesson 3: picture graphs ----------
G1 = 'A picture graph shows: Apple 7, Banana 5, Orange 9, Grape 4 (1 picture = 1 child).'
core = [(G1 + ' Which fruit got the most votes?', 'Orange'), (G1 + ' Which fruit got the fewest votes?', 'Grape'),
 (G1 + ' How many more children chose orange than grape?', '5 (9 − 4)'), (G1 + ' How many children voted altogether?', '25 (7 + 5 + 9 + 4)'),
 ('Pets: Dog 6, Cat 4, Fish 6, Bird 2. Which two pets got the same number of votes?', 'Dog and fish'),
 ('Pets: Dog 6, Cat 4, Fish 6, Bird 2. How many more children chose dog than bird?', '4 (6 − 2)')]
stretch = [
 ('1 picture = 2 children. Red has 3 pictures, blue has 5 and green has 4. How many children chose blue?', '10'),
 ('1 picture = 2 children. Red has 3 pictures, blue has 5 and green has 4. How many children voted altogether?', '24 (12 pictures × 2)'),
 ('1 picture = 2 children. Red has 3 pictures and blue has 5. How many more children chose blue than red?', '4 (2 more pictures × 2)'),
 ('1 picture = 2 children. Six children chose pizza. How many pictures should we draw?', '3'),
 ('1 picture = 2 children. A half picture means 1 child. Apple has 3 pictures and a half. How many children chose apple?', '7'),
 ('The graph shows Apple 8 and Banana 3. How many children must change from apple to banana so that both have the same number?', '3 children (8 − 3 = 5, half of 5 is not whole, so check: move 3 to get Apple 5 and Banana 6 is not equal). Correct answer: it cannot be done with whole children; only 5.5 each.')]
chal = [
 ('18 children voted. 7 chose apple and 5 chose orange. The rest chose grapes. How many chose grapes?', '6'),
 ('Votes: A 8, B 5, C 6. Then 4 more children join and all choose B. Which fruit wins now, and by how many votes?', 'B wins with 9, which is 1 more than A.'),
 ('12 children voted for three fruits. No two fruits got the same number of votes. The most votes was 5. How many votes did each fruit get?', '5, 4 and 3.'),
 ('Mei says 7 children chose apple. Banana got 4 fewer than apple and orange got 8. How many children voted?', '18 (7 + 3 + 8)'),
 ('Our class chose grapes. Ben says, “So the whole school loves grapes.” Is he right? Give two reasons.', 'No. Only our class voted, and other classes may choose differently. A small group may not match a big group.'),
]
# remove the unsound stretch item
stretch = stretch[:5]
stretch.append(('Banana has 3 pictures and apple has 8 pictures (1 picture = 1 child). How many more children chose apple?', '5'))
B[3] = (core, stretch, chal)

# ---------- Lesson 4: repeating and growing patterns ----------
cores = [(['circle', 'square', 'triangle'], 10), (['star', 'heart'], 9), (['red', 'red', 'blue'], 8), (['A', 'B', 'C', 'D'], 11), (['cat', 'dog', 'dog'], 12), (['sun', 'moon'], 15)]
core = []
for c, p in cores:
    seq = ', '.join((c * 3)[:7])
    core.append(('The pattern is ' + seq + ' … What is the %d%s one?' % (p, 'th'), cyc(c, p)))
stretch = [
 ('Pattern: circle, triangle, triangle, square, circle, triangle, triangle, square … What is the 14th shape?', cyc(['circle', 'triangle', 'triangle', 'square'], 14)),
 ('Same pattern: how many triangles are in the first 20 shapes?', '10 (5 groups of 4, with 2 triangles in each group)'),
 ('Same pattern: in which places do the squares come? Write the first five.', '4, 8, 12, 16, 20'),
 ('Red, blue, blue, red, blue, blue … What colour is the 20th bead?', cyc(['red', 'blue', 'blue'], 20)),
 ('Red, blue, blue, red, blue, blue … How many blue beads are in the first 12 beads?', '8'),
 ('A pattern repeats every 5 shapes. Is the 25th shape the same as the 5th? Why?', 'Yes. 25 is a multiple of 5, so it is the last shape of a group, like the 5th.'),
]
chal = [
 ('Squares in a row use 4 sticks for 1 square, 7 sticks for 2 squares and 10 sticks for 3 squares. How many sticks for 8 squares?', '25 (4 + 3 × 7)'),
 ('Using the same pattern, how many squares can you make with 22 sticks?', '7 (22 − 1 = 21, 21 ÷ 3 = 7)'),
 ('Tiles: the 1st pattern has 3 tiles, the 2nd has 5, the 3rd has 7. How many tiles in the 10th pattern? Which pattern has 31 tiles?', '21 tiles in the 10th. 31 tiles is the 15th.'),
 ('Matchstick triangles in a row use 3, 5, 7 sticks. Ben has 25 sticks. How many triangles can he make? How many sticks are left over?', '12 triangles use 25 sticks exactly (3 + 2 × 11). None left over.'),
 ('A pattern repeats: star, moon, sun, star, moon, sun … What is the 100th shape? Explain how you know without drawing 100 shapes.', 'Star. 99 is a multiple of 3, so the 99th shape ends a group (a sun) and the 100th starts the pattern again: star.'),
]
B[4] = (core, stretch, chal)

# ---------- Lesson 5: working backwards ----------
core = []
for a, b in [(3, 8), (6, 14), (5, 12), (9, 17)]:
    core.append(('I think of a number. I add %d. I get %d. What is my number?' % (a, b), str(b - a)))
for a, b in [(4, 6), (7, 3)]:
    core.append(('I think of a number. I take away %d. I get %d. What is my number?' % (a, b), str(b + a)))
stretch = []
for a, b, c in [(5, 3, 9), (6, 2, 10), (4, 7, 8), (9, 4, 12)]:
    stretch.append(('I think of a number. I add %d, then I take away %d. I get %d. What is my number?' % (a, b, c), str(c + b - a)))
stretch.append(('A number machine adds the same number each time. IN 4 gives OUT 9. What is the rule? What is OUT when IN is 12? What is IN when OUT is 20?', 'Add 5. OUT is 17 when IN is 12. IN is 15 when OUT is 20.'))
stretch.append(('Ben had some marbles. He gave 5 to Mei, then won 3. Now he has 12. How many did he start with?', '14 (12 − 3 + 5)'))
chal = [
 ('I think of a number. I add 6, take away 4, then add 5. I get 17. What is my number?', '10 (17 − 5 + 4 − 6)'),
 ('A number machine has two steps: add 3, then add 4. IN 5 gives OUT 12. What is IN when OUT is 20?', '13 (the same as adding 7)'),
 ('Zoe is 6th from the front of a queue and 6th from the back. How many children are in the queue?', '11'),
 ('Ben is 4th in a queue. There are 3 children behind him. How many children are in the queue?', '7'),
 ('Ali has 8 marbles. Mei has 5 more than Ali. Ben has 6 fewer than Mei. How many marbles do the three have altogether?', '8 + 13 + 7 = 28'),
 ('There are 20 children. 7 are boys. Of the girls, 4 are wearing red. How many girls are not wearing red?', '9 (20 − 7 = 13 girls; 13 − 4 = 9)'),
]
B[5] = (core, stretch, chal)

# ---------- Lesson 6: coins (answers computed) ----------
def two_coin(total, coins):
    out = []
    for a, b in itertools.combinations_with_replacement(coins, 2):
        if a + b == total:
            out.append('%d¢ + %d¢' % (a, b))
    return ' or '.join(out) if out else 'Not possible'
coins = [5, 10, 20, 50]
core = [('Pay exactly %d¢ using two coins from 5¢, 10¢, 20¢ and 50¢.' % t, two_coin(t, coins)) for t in (15, 25, 30, 40, 55, 60)]
def ways(total, cs):
    cnt = 0
    def rec(i, rem):
        nonlocal cnt
        if rem == 0:
            cnt += 1
            return
        if i == len(cs):
            return
        k = 0
        while k * cs[i] <= rem:
            rec(i + 1, rem - k * cs[i])
            k += 1
    rec(0, total)
    return cnt
def fewest(total, cs):
    best = 99
    def rec(i, rem, n):
        nonlocal best
        if rem == 0:
            best = min(best, n)
            return
        if i == len(cs):
            return
        k = 0
        while k * cs[i] <= rem:
            rec(i + 1, rem - k * cs[i], n + k)
            k += 1
    rec(0, total, 0)
    return best
stretch = [
 ('How many ways can you make 25¢ using 20¢, 10¢ and 5¢ coins?', '%d ways. (20+5; 10+10+5; 10+5+5+5; 5×5)' % ways(25, [20, 10, 5])),
 ('How many ways can you make 30¢ using 20¢, 10¢ and 5¢ coins?', '%d ways.' % ways(30, [20, 10, 5])),
 ('How many ways can you make 20¢ using only 10¢ and 5¢ coins?', '%d ways. (10+10; 10+5+5; 5×4)' % ways(20, [10, 5])),
 ('What is the fewest number of coins to make 65¢ from 5¢, 10¢, 20¢ and 50¢?', '%d coins (50¢ + 10¢ + 5¢)' % fewest(65, [50, 20, 10, 5])),
 ('What is the fewest number of coins to make 45¢?', '%d coins (20¢ + 20¢ + 5¢)' % fewest(45, [50, 20, 10, 5])),
 ('Ali buys a ruler for 35¢. He pays with a 50¢ coin. Which coins could he get back as change?', '15¢: 10¢ + 5¢ (or three 5¢ coins).'),
]
def exact(n, total, cs):
    res = []
    for combo in itertools.combinations_with_replacement(sorted(cs, reverse=True), n):
        if sum(combo) == total:
            res.append(' + '.join('%d¢' % c for c in combo))
    return res
r35 = exact(3, 35, coins)
r40 = exact(4, 40, coins)
chal = [
 ('Make 35¢ using exactly 3 coins from 5¢, 10¢, 20¢ and 50¢. How many ways are there?', '%d way: %s' % (len(r35), '; '.join(r35))),
 ('Make 40¢ using exactly 4 coins from 5¢, 10¢, 20¢ and 50¢. Find them all.', '%d ways: %s' % (len(r40), '; '.join(r40))),
 ('You have one 5¢, one 10¢ and one 20¢ coin. How many different totals can you make using one, two or all three coins? List them.', '7 totals: 5, 10, 15, 20, 25, 30, 35.'),
 ('Which amounts from 5¢ to 50¢ cannot be made using only 20¢ and 10¢ coins?', 'Every amount that is not a multiple of 10, so 5, 15, 25, 35 and 45 cannot be made.'),
 ('Why can 35¢ never be made with only two coins from 5¢, 10¢, 20¢ and 50¢?', 'Two coins can make 10, 15, 20, 25, 30, 40, 55, 60, 70 or 100. 35 is not one of them.'),
]
B[6] = (core, stretch, chal)

# ---------- Lesson 7: shapes ----------
core = [('How many sides and corners does a %s have?' % n, '%d sides and %d corners' % (k, k)) for n, k in [('triangle', 3), ('square', 4), ('pentagon', 5), ('hexagon', 6), ('octagon', 8)]]
core.append(('I have no corners and no straight sides. What shape am I?', 'A circle'))
stretch = [
 ('I have 4 sides. All my sides are the same length. What shape am I?', 'A square'),
 ('How many sides do 3 triangles have altogether?', '9'),
 ('How many corners do 5 squares have altogether?', '20'),
 ('A shape has 7 corners. How many sides has it?', '7 sides'),
 ('Fold a square along a diagonal and cut. Which shapes do you get?', '2 triangles of the same size'),
 ('Two same-size triangles can make a square. Can they also make a bigger triangle? Draw how.', 'Yes. Put the two long sides together the other way, or join them along a short side.'),
 ('Which shape has the same number of sides as a rectangle but is not a rectangle? Say why.', 'A parallelogram or a rhombus has 4 sides but its corners are not square.'),
]
sq = lambda n: sum(k * k for k in range(1, n + 1))
tri = lambda n: (n + 1) * (n + 2) // 2
chal = [
 ('A square has both diagonals drawn. How many triangles can you find?', '8 (4 small and 4 made of two small ones)'),
 ('A big triangle has 1 line from the top corner to the bottom. How many triangles? What about 2 lines? 3 lines?', '%d, %d and %d triangles.' % (tri(1), tri(2), tri(3))),
 ('A square is split into a 2 by 2 grid of 4 small squares. How many squares can you find altogether?', '%d (4 small + 1 big)' % sq(2)),
 ('A square is split into a 3 by 3 grid of 9 small squares. How many squares are there altogether?', '%d (9 small + 4 of size 2 by 2 + 1 big)' % sq(3)),
 ('Ali cuts a rectangle along one line and gets two triangles. Where did he cut?', 'From one corner to the opposite corner.'),
 ('I have 6 sides. I can be made from 6 equal triangles. What shape am I?', 'A hexagon'),
]
B[7] = (core, stretch, chal)

# ---------- Lesson 8: logic ----------
def orders(names, clauses):
    res = []
    for p in itertools.permutations(names):
        pos = {n: i for i, n in enumerate(p)}
        if all(c(pos) for c in clauses):
            res.append(p)
    return res
assert len(orders(['Ali', 'Ben', 'Mei'], [lambda p: p['Ali'] < p['Ben'], lambda p: p['Ben'] < p['Mei']])) == 1
core = [
 ('Ali is taller than Ben. Ben is taller than Mei. Who is the tallest? Who is the shortest?', 'Ali is tallest; Mei is shortest.'),
 ('The cat is heavier than the hen. The hen is heavier than the mouse. Who is the lightest?', 'The mouse'),
 ('Red, blue and green ribbons. Red is longer than blue. Green is shorter than blue. Which ribbon is the longest?', 'Red'),
 ('Which number is the odd one out: 2, 4, 6, 9, 10? Why?', '9. It is the only odd number.'),
 ('Sort these numbers into odd and even: 3, 8, 5, 12, 7, 10.', 'Odd: 3, 5, 7. Even: 8, 12, 10.'),
]
o = orders(['Mei', 'Sam', 'Tia', 'Raj'], [lambda p: p['Mei'] < p['Sam'], lambda p: p['Sam'] < p['Tia'], lambda p: p['Tia'] < p['Raj']])
assert len(o) == 1
stretch = [
 ('In a race, Sam is ahead of Tia. Tia is ahead of Raj. Mei is ahead of Sam. Who is third?', 'Tia (order: Mei, Sam, Tia, Raj).'),
 ('Tia does not drink milk. Sam drinks neither milk nor juice. Raj drinks the third drink. The drinks are milk, juice and water. Who drinks what?', 'Sam: water. Tia: juice. Raj: milk.'),
 ('Numbers 1 to 12. Which are multiples of 2? Which are multiples of 3? Which are both?', 'Multiples of 2: 2, 4, 6, 8, 10, 12. Multiples of 3: 3, 6, 9, 12. Both: 6 and 12.'),
 ('Numbers 1 to 12. Which are in neither the 2 times table nor the 3 times table?', '1, 5, 7 and 11'),
 ('Which is the odd one out: 3, 6, 9, 11, 12? Give a reason.', '11. It is not in the 3 times table.'),
 ('Ali, Ben and Mei have a cat, a dog and a fish. Ali has no dog. Mei has no fish. Ben has neither a cat nor a fish. Who has which pet?', 'Ben: dog. Mei: cat. Ali: fish.'),
]
o2 = orders(['Ali', 'Ben', 'Mei', 'Sam'], [lambda p: p['Ali'] != 0, lambda p: p['Ben'] < p['Ali'], lambda p: p['Sam'] == 3, lambda p: p['Mei'] > p['Ali']])
chal = [
 ('Four friends stand in a line. Ali is not first. Ben is ahead of Ali. Sam is last. Mei is behind Ali. In what order do they stand?', ', '.join(o2[0]) + '.' if len(o2) == 1 else 'CHECK'),
 ('Three boxes are labelled “Apples”, “Oranges” and “Mixed”. Every label is wrong. You may take one fruit from one box. Which box should you pick from, and why?', 'Pick from the box labelled “Mixed”. Its label is wrong, so it holds only one kind of fruit. If you take out an apple, that box is Apples. The box labelled “Oranges” cannot be oranges, and apples are taken, so it is Mixed. The box labelled “Apples” must be Oranges.'),
 ('Ali, Ben and Mei are 6, 7 and 8 years old. Ali is older than Mei. Ali is not the oldest. How old is each?', 'Mei 6, Ali 7, Ben 8.'),
 ('A number between 20 and 40 is in the 5 times table and is odd. It is also one less than a number in the 4 times table. What is it?', '35 (35 + 1 = 36, which is in the 4 times table).'),
 ('Draw a Venn diagram for numbers 1 to 10 with the rules “even” and “more than 5”. Which numbers go in the middle? Which go outside both?', 'Middle: 6, 8, 10. Outside both: 1, 3, 5.'),
]
B[8] = (core, stretch, chal)

# ---------- Lesson 9: length ----------
core = [
 ('A pencil is 7 cubes long. A pen is 10 cubes long. How many cubes longer is the pen?', '3'),
 ('A ribbon is 12 cubes long. You cut off 5 cubes. How long is the piece left?', '7 cubes'),
 ('Ali’s book is 9 cubes long and Mei’s book is 6 cubes long. Whose is longer? By how much?', 'Ali’s, by 3 cubes.'),
 ('Which is longer: 8 cubes or 8 paper clips? Why can we not tell?', 'We cannot tell. The units are different sizes.'),
 ('Put in order from shortest: 11 cubes, 7 cubes, 9 cubes, 12 cubes.', '7, 9, 11, 12'),
]
stretch = [
 ('1 clip is as long as 3 cubes. A pen is 12 cubes long. How many clips long is the pen?', '4 clips'),
 ('1 clip is as long as 3 cubes. A ruler is 5 clips long. How many cubes long is the ruler?', '15 cubes'),
 ('Ali’s desk is 6 spans long. Mei’s desk is 9 spans long, but they measured the same desk. Whose hand is bigger?', 'Ali’s. A bigger span needs fewer spans to cover the same desk.'),
 ('A caterpillar is 9 cubes long. It grows 2 cubes each day. How long is it after 3 days?', '15 cubes'),
 ('A string is 15 cubes long. A rope is 8 cubes longer. How long is the rope?', '23 cubes'),
]
chal = [
 ('A rope is 20 cubes long. Ali cuts it into pieces that are each 4 cubes long. How many pieces does he get? How many cuts does he make?', '5 pieces and 4 cuts.'),
 ('A train has 3 carriages. Each is 6 cubes long. There is a gap of 1 cube between carriages. How long is the whole train?', '20 cubes (18 + 2)'),
 ('A caterpillar is 9 cubes long and grows 2 cubes each day. On which day is it 21 cubes long?', 'Day 6 (9 + 2 × 6 = 21).'),
 ('A red ribbon is 5 cubes long. A blue ribbon is 3 cubes longer than red. A green ribbon is 2 cubes shorter than blue. How long are the three ribbons end to end?', '5 + 8 + 6 = 19 cubes'),
 ('1 clip = 2 erasers and 1 pen = 3 clips. How many erasers long is the pen? How many pens are as long as 24 erasers?', '6 erasers per pen; 4 pens.'),
]
B[9] = (core, stretch, chal)

# ---------- Lesson 10: mixed ----------
core = [
 ('Count in 3s: 3, 6, 9, __, __', '12, 15'),
 ('10 = 4 + __ and 20 = 12 + __', '6 and 8'),
 ('Red 4, blue 6, green 3. How many more are blue than green?', '3'),
 ('I think of a number. I add 4. I get 9. What is it?', '5'),
 ('Make 15¢ with two coins from 5¢, 10¢ and 20¢.', '10¢ + 5¢'),
 ('How many sides does a hexagon have?', '6'),
]
stretch = [
 ('A pattern starts at 5 and adds 3 each time. What is the 10th number?', '32'),
 ('Ali has 12 stickers. He gives 5 to Mei and then gets 3 more. How many does he have now?', '10'),
 ('Which three coins from 5¢, 10¢, 20¢ and 50¢ make 45¢?', '20¢ + 20¢ + 5¢'),
 ('A ribbon is 12 cubes. A string is 5 cubes shorter. How long is the string?', '7 cubes'),
 ('Mei is taller than Ben. Ben is taller than Sam. Ali is shorter than Sam. Who is the shortest?', 'Ali'),
]
chal = [
 ('Two numbers add to 12 and differ by 2. What are they?', '5 and 7'),
 ('1 triangle uses 3 sticks, 2 triangles use 5 sticks. How many sticks for 9 triangles? How many triangles with 25 sticks?', '19 sticks for 9; 12 triangles for 25 sticks.'),
 ('How many ways can you make 30¢ using 20¢, 10¢ and 5¢ coins?', '%d ways.' % ways(30, [20, 10, 5])),
 ('Ali, Ben and Mei are first, second and third in a race. Ali is not first. Ben is ahead of Mei. Ali is behind Mei. Who is first?', 'Ben (order: Ben, Mei, Ali).'),
 ('A square has both diagonals drawn. How many triangles are there? Explain how you counted.', '8: 4 small and 4 made of two small ones.'),
 ('Invent a puzzle that needs two steps. Give it to a friend. Write its answer.', 'Open.'),
]
B[10] = (core, stretch, chal)

HARD = {
 1: [('Frog A starts at 3 and jumps 4 each time. Frog B starts at 5 and jumps 3 each time. Which numbers up to 40 do both frogs land on?', '11, 23 and 35.'),
     ('1, 2, 4, 7, 11, 16 … What is the 8th number? Explain how the pattern grows.', '29. The gaps are 1, 2, 3, 4, 5, 6, 7, so the 7th is 22 and the 8th is 29.'),
     ('Ali counts up from 2 in 3s. Mei counts up from 1 in 4s. Which numbers up to 50 are in both patterns?', '5, 17, 29 and 41.')],
 2: [('Three different numbers from 1 to 7 add up to 10. Find every set of three.', '1, 2, 7; 1, 3, 6; 1, 4, 5; 2, 3, 5.'),
     ('Put 1 to 6 in the magic triangle so each side adds to 11. What goes in the corners and middles?', 'Corners 2, 4, 6. Between 2 and 4: 5. Between 4 and 6: 1. Between 6 and 2: 3.'),
     ('Ali has 20 stickers. He keeps 9 and shares the rest between Ben and Mei. Ben gets 3 more than Mei. How many does each get?', 'Ben 7, Mei 4.')],
 3: [('1 picture = 3 children. Apple has 4 pictures, banana 2 and orange 5. Then 7 more children join and all choose banana. Which fruit wins now, and by how many votes?', 'Orange 15, banana 13, apple 12. Orange wins by 2.'),
     ('24 children voted. Apple got 6 votes. Orange got twice as many as banana. How many votes did banana and orange get?', 'Banana 6 and orange 12.'),
     ('1 picture = 4 children. 40 children voted for three fruits. A has 3 pictures. B has 2 more pictures than A. How many children chose C?', '8 children (10 pictures in all; A 3 + B 5 = 8, so C has 2 pictures).')],
 4: [('Squares in a row use 4, 7, 10 … sticks. Ben has 50 sticks. How many squares can he make? How many sticks are left?', '16 squares use 49 sticks. 1 stick is left.'),
     ('Beads repeat in a pattern of 5: red, red, blue, blue, green. How many green beads are in the first 47 beads?', '9 green beads (9 full groups of 5 and 2 red beads left over).'),
     ('Dots: 1, 3, 6, 10, 15 … What are the next two numbers? What is the 10th number?', '21 and 28. The 10th is 55 (add 2, 3, 4, … each time).')],
 5: [('I think of a number. I add 7, take away 3, add 5, then take away 8. I get 14. What is my number?', '13 (the steps are +1 in total, so 14 − 1).'),
     ('Ali is 5 years older than Ben. In 3 years’ time their ages will add up to 25. How old is each now?', 'Ben 7 and Ali 12.'),
     ('A snail climbs 3 cm each day and slides back 1 cm each night. It starts at the bottom of a 9 cm wall. On which day does it reach the top?', 'Day 4 (3, 5, 7, then 9 on the fourth day before it can slide back).')],
 6: [('Ali pays 55¢ with exactly 5 coins. He uses at least one 5¢, one 10¢ and one 20¢ coin. Which coins does he use?', '20¢ + 10¢ + 10¢ + 10¢ + 5¢ (the only way).'),
     ('You have one 5¢, one 10¢, one 20¢ and one 50¢ coin. How many different amounts can you make using any of them?', '15 different amounts.'),
     ('A sweet costs 15¢ and a biscuit costs 20¢. Ben spends exactly 90¢ and buys some of each. How many sweets and biscuits does he buy?', '2 sweets and 3 biscuits.')],
 7: [('Three squares are joined in a row to make a long rectangle. How many rectangles can you find altogether? (A square counts as a rectangle.)', '6 (3 single squares, 2 pairs and 1 whole row).'),
     ('A triangle has 4 lines drawn from the top corner to the bottom. How many triangles are there? Follow the pattern 3, 6, 10 …', '15.'),
     ('A square is cut into 4 equal squares. One of the small squares is cut into 4 even smaller squares. How many squares can you find altogether?', '9 (1 big, 4 medium, 4 tiny).')],
 8: [('Five friends run a race. D is first. E is last. B finishes directly behind A. C is not second. In what order do they finish?', 'D, A, B, C, E.'),
     ('A secret number is between 10 and 30. It is even and in the 3 times table. It is 2 more than a number in the 5 times table. What is it?', '12.'),
     ('Numbers 1 to 20. How many are multiples of 2 only, 3 only, both, and neither?', '2 only: 7. 3 only: 3. Both: 3 (6, 12, 18). Neither: 7.')],
 9: [('A ruler is 12 cubes long. Ali measures a desk by laying the ruler end to end 4 times and then 5 more cubes. How long is the desk in cubes?', '53 cubes.'),
     ('Ali’s pencil is 9 cubes. Mei’s is 2 cubes shorter than Ali’s. Ben’s is 3 cubes longer than Mei’s. How long are all three pencils together?', '9 + 7 + 10 = 26 cubes.'),
     ('A ribbon 30 cubes long is cut into three pieces. The first is 4 cubes longer than the second. The third is 4 cubes shorter than the second. How long is each piece?', '14, 10 and 6 cubes.')],
 10: [('Frog A jumps in 3s from 0 and frog B jumps in 5s from 0. Which numbers up to 60 do both land on?', '15, 30, 45 and 60.'),
      ('Ali has some stickers. Ben has 4 more than Ali. Mei has 3 fewer than Ben. Together they have 29. How many does each have?', 'Ali 8, Ben 12, Mei 9.'),
      ('Make 70¢ using exactly 4 coins from 5¢, 10¢, 20¢ and 50¢. How many ways are there?', '2 ways: 50¢ + 10¢ + 5¢ + 5¢ and 20¢ + 20¢ + 20¢ + 10¢.')],
}
for n, items in HARD.items():
    c, s, ch = B[n]
    B[n] = (c, s, ch + items)
out = {str(n): {'core': [{'q': q, 'a': a} for q, a in c], 'stretch': [{'q': q, 'a': a} for q, a in s], 'challenge': [{'q': q, 'a': a} for q, a in ch]} for n, (c, s, ch) in B.items()}
json.dump(out, open('qbank.json', 'w'), ensure_ascii=False, indent=1)
for n in out:
    print(n, len(out[n]['core']), len(out[n]['stretch']), len(out[n]['challenge']))
print(o2, o)
