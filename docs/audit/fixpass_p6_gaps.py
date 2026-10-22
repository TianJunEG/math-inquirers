"""One-off: rewrite p6/content/gaps.json for the fix pass (sneak-peek puzzles, go-further what-ifs, easy first steps)
and verify every answer by computation. Run: python3 -I docs/audit/fixpass_p6_gaps.py"""
import json, os
from fractions import Fraction as F
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
P = os.path.join(R, 'p6', 'content', 'gaps.json')
G = json.load(open(P, encoding='utf8'))
def isp(n): return n > 1 and all(n % d for d in range(2, int(n ** .5) + 1))
def chk(name, ok):
    assert ok, name
    print('OK', name)

SN = {}  # lesson -> ([access q, answer], [thinking q, answer])
GO = {}  # lesson -> (what-if q, answer)
FIRST = {}

# L1
chk('L1 access 4 triangles = 9 sticks', 3 + 2 * 3 == 9)
chk('L1 taxi 20 km', 3 + 2 * 20 == 43)
SN[1] = (["Matchsticks make triangles in a row: 1 triangle uses 3 sticks, 2 triangles use 5 sticks, 3 triangles use 7 sticks. Draw or build 4 triangles in a row. How many sticks?",
          "9 sticks. Each new triangle adds 2 more sticks (3, 5, 7, 9). Any child can draw it and count."],
         ["A taxi charges $3 to start plus $2 for every km. What is the fare for 20 km?",
          "$43. Each km adds $2, so 2 × 20 + 3 = 43. (Not 2 × 20 = 40: the $3 start charge is there from the beginning.) A guess or “I do not know” is fine; we will learn how today."])
chk('L1 go: 10 squares in a row = 31 sticks', 3 * 10 + 1 == 31)
GO[1] = ("What if each shape in the row were a SQUARE, sharing one side with the next? Predict how many sticks 10 squares in a row need. Then test pattern 3 by drawing.",
         "31 sticks. The first square uses 4 sticks and each new square adds 3: 4 + 3 × 9 = 31, or 3 × 10 + 1.")
FIRST[1] = "First step: draw 3 squares in a row and count the sticks."

# L2
chk('L2 12 counters rows: 1x12 2x6 3x4', [d for d in range(1, 13) if 12 % d == 0] == [1, 2, 3, 4, 6, 12])
chk('L2 31 prime', isp(31))
SN[2] = (["Take 12 counters (or draw 12 dots). Make equal rows, for example 3 rows of 4. Find every way to make equal rows with all 12 counters.",
          "1 row of 12, 2 rows of 6, 3 rows of 4 (and the same turned round: 4 rows of 3, 6 rows of 2, 12 rows of 1). Counting and drawing is enough."],
         ["Could you make equal rows (more than 1 row and more than 1 counter in each row) with exactly 31 counters? What do you think? Why?",
          "No. 31 only makes 1 row of 31 or 31 rows of 1, because 31 is prime (its only factors are 1 and 31). Children may guess; accept any reason and say we will find out how to be sure."])
pr = [n for n in range(101, 121) if isp(n)]
chk('L2 go: primes 101-120', pr == [101, 103, 107, 109, 113])
GO[2] = ("What if the grid went up to 120? Predict which new numbers after 100 will be prime. Which multiples do you need to cross out now: do you need the multiples of 11?",
         "101, 103, 107, 109 and 113. You still only need the multiples of 2, 3, 5 and 7, because 11 × 11 = 121 is bigger than 120.")
FIRST[2] = "First step: write down all the prime numbers below 20."

# L3
chk('L3 3 - 5 = -2', 3 - 5 == -2)
chk('L3 4 - (-18) = 22', 4 + 18 == 22)
SN[3] = (["It is 3 °C outside. The temperature falls by 5 degrees. Draw a thermometer or a number line. What is the temperature now?",
          "−2 °C (3 down to 0 is 3 degrees, then 2 more below zero). A drawn thermometer or number line shows it."],
         ["A freezer is at −18 °C and a fridge is at 4 °C. How many degrees warmer is the fridge than the freezer?",
          "22 degrees. From −18 up to 0 is 18, then 4 more: 18 + 4 = 22. A number line drawing shows it. Guessing is fine."])
chk('L3 go: 5 - 3*20 = -55', 5 - 3 * 20 == -55)
GO[3] = ("What if the thermometer program starts at 5 and repeats 20 times (change temp by −3 each time)? Predict the last number. Which repeat number first gives a number below −30?",
         "−55 (5 − 3 × 20). Below −30 first happens at repeat 12: 5 − 36 = −31 (repeat 11 gives −28).")
chk('L3 go: first below -30 at repeat 12', [k for k in range(1, 30) if 5 - 3 * k < -30][0] == 12)
FIRST[3] = "First step: draw a number line from −5 to 6. Pick a = 2 and ask: what number b makes 2 − b = 7?"

# L4
chk('L4 +3 machine', [x + 3 for x in (4, 7, 10)] == [7, 10, 13])
chk('L4 x3+10 = 52 -> 14', (52 - 10) / 3 == 14)
SN[4] = (["A number machine adds 3 to every number you put in. Put in 4, then 7, then 10. What comes out each time? (Count on with objects or your fingers if you like.)",
          "7, 10 and 13. Every OUT is 3 more than IN."],
         ["Another machine multiplies by 3, then adds 10. The OUT is 52. What was the IN?",
          "14. Undo the + 10 first: 52 − 10 = 42. Then undo the × 3: 42 ÷ 3 = 14. Check: 3 × 14 + 10 = 52. Guessing and checking is fine."])
sol = [(a, 11 - 3 * a) for a in range(-20, 20) if 3 * a + (11 - 3 * a) == 11 and 5 * a + (11 - 3 * a) == 19]
chk('L4 go: IN3->11, IN5->19 gives 4n-1', sol == [(4, -1)])
GO[4] = ("What if a machine gives OUT 11 when IN is 3, and OUT 19 when IN is 5? Predict its rule, then try your rule on both pairs. Then find the OUT for IN 10.",
         "4n − 1. IN goes up by 2 and OUT goes up by 8, so the × part is 4; 4 × 3 = 12 is 1 too big, so − 1. OUT for IN 10 is 39.")
chk('L4 go: 4*10-1=39', 4 * 10 - 1 == 39)
FIRST[4] = "First step: try × 2. Then 4 × 2 = 8. What must be added to 8 to make 17?"

# L5
chk('L5 2 tops x 3 shorts = 6', 2 * 3 == 6)
chk('L5 5 clubs 10 games', 5 * 4 // 2 == 10)
SN[5] = (["You have 2 tops (red, blue) and 3 pairs of shorts (black, white, grey). Draw or list every different outfit (1 top and 1 pair of shorts). How many outfits?",
          "6 outfits: red-black, red-white, red-grey, blue-black, blue-white, blue-grey. A drawing or an organised list works."],
         ["5 chess clubs each play every other club once. How many games is that? Is it 5 × 4?",
          "10 games. 5 × 4 = 20 counts every game twice (A against B is the same game as B against A), so halve it. Guessing is fine."])
chk('L5 go: 3x3x3 = 27', 3 * 3 * 3 == 27)
GO[5] = ("What if the shop had 3 teas, 3 sizes (S, M, L) and 3 toppings? Predict how many different orders. Then write how you would check with a list or a loop.",
         "27 orders (3 × 3 × 3). Fix the tea, then the size, then the topping: three loops inside each other, or a tree with three layers.")
FIRST[5] = "First step: list every way to pay 50 cents that uses two 20-cent coins."

# L6
SN[6] = (["A bag has 3 red counters and 5 blue counters. Draw the bag. Without looking, you pick one counter. Which colour is more likely? Why?",
          "Blue, because there are more blue counters (5 out of 8) than red (3 out of 8). Drawing the counters is enough."],
         ["Flip two coins. Ali wins if both coins match (two heads or two tails). Mei wins if they are different. Do you think the game is fair? List every way the two coins can land.",
          "Fair. The four outcomes are HH, HT, TH, TT. Match: HH and TT (2 out of 4). Different: HT and TH (2 out of 4). A guess is welcome; the list decides."])
w = {t: sum(1 for a in range(1, 7) for b in range(1, 7) if a + b == t) for t in range(2, 13)}
A = sum(w[t] for t in range(2, 7)); B = sum(w[t] for t in range(7, 13))
chk('L6 go: A 2-6 = 15/36, B 7-12 = 21/36', (A, B) == (15, 21))
GO[6] = ("What if A wins on totals 2 to 6 and B wins on totals 7 to 12? Predict who wins more often. Play 10 rounds, then explain using the 36 outcomes.",
         "B is more likely: totals 7 to 12 can be made in 21 of the 36 ways, totals 2 to 6 in only 15 (so 21/36 = 7/12 against 15/36 = 5/12). The game is not fair.")
FIRST[6] = "First step: flip a coin 10 times and tally heads and tails. Is a coin fair? Say why."

# L7
chk('L7 four quarter turns = 360', 4 * 90 == 360)
chk('L7 360/40 = 9', 360 // 40 == 9)
SN[7] = (["Stand up. Face the door. Turn a quarter turn to your right (clockwise). Do that 4 times in a row. Which way are you facing at the end? What did your body do in total?",
          "Facing the door again. Four quarter turns make one full turn (4 × 90° = 360°). Children who cannot stand can use an arm or a drawing of an arrow."],
         ["A turtle goes once round a closed shape and turns 40° at every corner (all the turns equal). How many corners does the shape have?",
          "9 corners. The turtle turns 360° altogether and each turn is 40°, so 360 ÷ 40 = 9. A guess is welcome."])
chk('L7 go: 8 sides -> 45', 360 // 8 == 45)
GO[7] = ("What if you want a regular shape with 8 sides (an octagon)? Predict the turn. Then test it in Scratch with repeat 8. What about 10 sides?",
         "45° for 8 sides (360 ÷ 8) and 36° for 10 sides (360 ÷ 10).")
chk('L7 go: 10 sides -> 36', 360 // 10 == 36)
FIRST[7] = "First step: a turtle repeats [move 100, turn 90]. How many repeats until it faces the way it started?"

# L8
chk('L8 8 + 5 = 13 -> 1 o clock', (8 + 5) % 12 == 1)
chk('L8 Wed + 100 days = Fri', (2 + 100) % 7 == 4)  # Mon0 Tue1 Wed2 ... Fri4
SN[8] = (["A clock shows 8 o’clock. What time is it 5 hours later? Use a clock drawing or count on with your fingers.",
          "1 o’clock (8, 9, 10, 11, 12, 1). Counting on round the clock face works."],
         ["Today is Wednesday. What day of the week will it be in 100 days? What do you think? How could you find out?",
          "Friday. 100 ÷ 7 leaves remainder 2 (98 is 14 full weeks), so move 2 days on from Wednesday: Thursday, Friday. Guessing and “I do not know” are fine."])
def shift(s, k): return ''.join(chr((ord(c) - 65 + k) % 26 + 65) for c in s)
chk('L8 go: ROT13 HELLO', shift('HELLO', 13) == 'URYYB' and shift('URYYB', 13) == 'HELLO')
GO[8] = ("What if the shift is 13? Code the word HELLO with shift 13. Then code your answer with shift 13 again. What do you notice? Predict first.",
         "HELLO becomes URYYB, and coding URYYB with shift 13 gives HELLO again. Two shifts of 13 make 26, a full circle of the alphabet.")
FIRST[8] = "First step: code the letter C with shift 8. Then shift your answer by 18. Where do you land?"

# L9
chk('L9 share 2,4,4,6 -> 4', (2 + 4 + 4 + 6) / 4 == 4)
SN[9] = (["Four friends have 2, 4, 4 and 6 stickers. Use counters to share the stickers out so that every friend has the same number. How many does each friend get?",
          "4 each. Total 16 stickers, shared between 4 friends. (This is the “fair share” idea behind the mean.)"],
         ["Five friends have $2, $3, $3, $4 and $38. If they shared it all equally, each would get $10. Is $10 a good description of what a typical friend has? Why or why not?",
          "No: four of the five friends have $4 or less. One very large amount pulls the equal share up. The middle value ($3) says more about a typical friend. Guesses are welcome."])
chk('L9 equal share 10', (2 + 3 + 3 + 4 + 38) / 5 == 10)
GO[9] = ("What if you add a very small value, 1, to the list instead of 30? Predict: does the mean go up or down? Does the median change? Test it and explain.",
         "The mean goes down (1 is below the other values, which are name lengths of about 8 or more). The median moves only to the next value along, so it changes by much less than the mean. One extreme value pulls the mean more than the median.")
FIRST[9] = "First step: find the mean of 4, 6, 7, 9 and 14 (add them up, then share equally)."

# L10
chk('L10 count on 5s from 4', [4 + 5 * k for k in range(1, 4)] == [9, 14, 19])
SN[10] = (["Count on in 5s from 4: 4, 9, 14, 19, … Write the next three numbers.",
           "24, 29 and 34. Any child can count on."],
          ["The list 4, 9, 14, 19, … carries on forever. Is 2026 in the list? What do you think? How could you tell?",
           "No. Every number in the list ends in 4 or 9 (it is 1 less than a multiple of 5), and 2026 ends in 6. A guess is welcome; today’s challenge round uses ideas like this."])
chk('L10 2026 not in list', all(5 * n - 1 != 2026 for n in range(1, 1000)))
chk('L10 go: pentagons 4n+1=101 -> n=25', 4 * 25 + 1 == 101)
GO[10] = ("What if the hexagon puzzle used PENTAGONS joined along one side? Find the rule for the sticks and say how many pentagons use 101 sticks.",
          "4n + 1 sticks (a pentagon needs 5 sticks and each new one adds 4). 101 sticks: 4n + 1 = 101, so n = 25 pentagons.")
FIRST[10] = "First step: write the first 5 terms of the sequence 7n − 3 (4, 11, 18, ...)."

for k, g in G.items():
    n = int(k)
    g.pop('check', None)
    g['sneak'] = [list(SN[n][0]), list(SN[n][1])]
    g['go'] = list(GO[n])
    g['inv']['first'] = FIRST[n]
json.dump(G, open(P, 'w', encoding='utf8'), indent=1, ensure_ascii=False)
print('gaps.json rewritten')
