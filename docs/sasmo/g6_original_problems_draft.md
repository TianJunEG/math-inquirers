# Original Go further practice problems for Level 6 (ages 11-13)

**Draft, not yet in the program.** Written for the gaps and high-frequency types found in `g6_analysis.md` (sections 4 and 5). Every problem is new (own context, numbers and wording; none is a copy or light rewording of a contest problem, and none repeats a contest's numbers). Every answer was worked by hand and then confirmed by a short brute-force script (exhaustive search for the packing and cryptarithm items, simulation for the die and the counting items). They have not been tried with children or reviewed by a tutor, so check reading load and difficulty first. They follow the level rules in `p6/SPEC.md` (plain English, no surds, no index notation beyond squares; powers are written as repeated products). The lesson numbers in brackets are suggestions from the term plan (`docs/terms/level_6_year_plan.md`); no lesson file or plan was changed.

Items that need a drawing in the program (the height grid, the sheet and cards, the die, the figure with points on a line) are given as text so the designer can draw them. The code idea after an item is optional (Scratch or Python); the maths comes first.

## 1. Divisibility tests and digit conditions [draft, not yet in the program] (suggested for L2 or L25)

**1.1** Ravi's locker code is a 4-digit number of the form 4 _ 7 _. The two missing digits are the same digit, and the code can be divided exactly by 9. What is the code?
Answer: 4878. Solution: the digits add to 11 plus twice the missing digit; that must be 18 or 27, so twice the digit is 7 (not possible) or 16, giving digit 8.

**1.2** How many 3-digit numbers can be divided exactly by 6 and have digits that add up to 12?
Answer: 34. Solution: a digit sum of 12 already makes the number a multiple of 3, so it only has to be even: count the 3-digit numbers with digit sum 12 that end in 0, 2, 4, 6 or 8 (checked by listing all 900 numbers by program). Code idea: a loop with "mod" and a digit-sum counter.

**1.3** Use each of the digits 1, 2, 3, 4, 5 and 6 exactly once to make the largest 6-digit number that can be divided exactly by 12.
Answer: 654312. Solution: the digits add to 21, so every arrangement is in the 3s; the number must also be in the 4s, so its last two digits must be a multiple of 4. Start with 6543 and the best two digits left are 1 and 2, in the order 12.

## 2. Last digits, zeros at the end, remainders [draft, not yet in the program] (suggested for L8, L24 or L25)

**2.1** Work out how many zeros are at the end of the product 12 x 15 x 20 x 25 x 35 x 48.
Answer: 5. Solution: a zero needs one factor 2 and one factor 5. There are 8 twos (12, 20 and 48 give 2, 2 and 4) and 5 fives (15, 20, 35 give 1 each and 25 gives 2), so 5 pairs.

**2.2** Multiply 7 by itself 45 times to get a very big number. Multiply 3 by itself 30 times to get another. What is the last digit of the sum of the two big numbers?
Answer: 6. Solution: the last digits of the 7s go 7, 9, 3, 1 and repeat; 45 is one more than 44, so the last digit is 7. The last digits of the 3s go 3, 9, 7, 1; 30 is two more than 28, so it is 9. Then 7 + 9 = 16, last digit 6.

**2.3** What are the last two digits of 1234 x 5678 x 9101?
Answer: 52. Solution: only the last two digits of each number matter: 34 x 78 = 2652, which ends in 52, and 52 x 01 ends in 52.

## 3. Cryptarithms [draft, not yet in the program] (suggested for L34, or a recurring warm-up)

In each puzzle, different letters stand for different digits, and no number starts with 0.

**3.1** AB x AB = CAB. Find the 2-digit number AB.
Answer: 25 (25 x 25 = 625). Solution: AB squared ends in B, so B is 0, 1, 5 or 6; the square is 3-digit and ends in AB, which cuts the list down to 25 (B = 0, 1 and 6 give no number that ends in AB). Confirmed it is the only answer by checking all assignments.

**3.2** ABC x 3 = DBA. Find every possible 3-digit number ABC.
Answer: 197 (197 x 3 = 591) and 301 (301 x 3 = 903). Solution: the ones digit of 3 x C is A, and A x 3 plus a carry is D; trying C from 0 to 9 and checking the other two columns leaves just these two. (The answer has exactly two; checked by program.)

**3.3** AA + BB + CC = ABC. Find the 3-digit number ABC.
Answer: 198 (11 + 99 + 88 = 198). Solution: AA + BB + CC = 11 x (A + B + C), so ABC is a multiple of 11 below 300, and A is 1 or 2. With A = 1: 100 + 10B + C = 11 + 11B + 11C, so 89 = B + 10C, which gives C = 8 and B = 9. With A = 2 it would need 178 = B + 10C, which is impossible. Confirmed unique by program.

## 4. Spatial thinking [draft, not yet in the program] (suggested for L15)

**4.1** A 5 by 5 by 2 block of cheese is made of 50 small cubes. Its whole outside, including the top and the bottom, is painted blue. It is then cut into the 50 small cubes. How many small cubes have (a) 3 blue faces, (b) 2 blue faces, (c) 1 blue face?
Answer: 8, 24, 18. Solution: every cube touches the top or the bottom (one face). Corners also touch two sides: 8 cubes (3 faces). Cubes along an edge but not a corner touch one side: 3 per side per layer x 4 sides x 2 layers = 24 (2 faces). The rest have only the top or bottom: 3 x 3 x 2 = 18 (1 face). 8 + 24 + 18 = 50.

**4.2** Mei builds a block city on a 3 by 3 floor. The numbers show how many cubes are stacked on each square (front row first):

| | left | middle | right |
|---|---|---|---|
| front row | 3 | 1 | 0 |
| middle row | 2 | 2 | 1 |
| back row | 0 | 4 | 1 |

(a) How many cubes are there? Looking from (b) above, (c) the front, (d) the right, how many cube faces can she see?
Answer: (a) 14, (b) 7, (c) 8, (d) 9. Solution: rows add to 4, 5, 5; seven squares have a stack; from the front, each column shows its tallest stack: 3, 4, 1; from the right, each row shows its tallest stack: 3, 2, 4.

**4.3** A die has opposite faces adding to 7. It starts with 1 on top, 2 facing you and 3 on the right. It is rolled across the table: 3 times away from you ("forward"), then 2 times to the right, then once forward, then once to the right (each roll tips it a quarter turn onto the next face). What number is on top at the end, and what number is on the bottom?
Answer: top 3, bottom 4. Solution: write top, front, right after each roll and update (a forward roll sends top to front, front to bottom, bottom to back, back to top; a right roll sends top to right, right to bottom, bottom to left, left to top). Checked by simulating the 7 rolls.

## 5. Worst case, pigeonhole and unattainable totals [draft, not yet in the program] (suggested for L34 or L33)

**5.1** A drawer holds 8 red, 6 blue, 5 green and 4 yellow socks. In the dark, what is the smallest number of socks you must take out to be sure of (a) 3 socks of the same colour, (b) 2 yellow socks?
Answer: (a) 9, (b) 21. Solution: (a) the worst case is 2 of each of the 4 colours, 8 socks, and the 9th gives 3 of a kind. (b) the worst case is taking all 19 other socks and 1 yellow first; the 21st sock must be the second yellow.

**5.2** The post office has only 5-cent and 8-cent stamps. What is the largest postage that cannot be made exactly?
Answer: 27 cents. Solution: all the totals from 28 to 32 can be made (28 = 5 x 4 + 8, 29 = 5 x 1 + 8 x 3, 30 = 5 x 6, 31 = 5 x 3 + 8 x 2, 32 = 8 x 4); then add 5 more each time to reach every bigger total. 27 cannot: taking away 0, 1, 2 or 3 eight-cent stamps leaves 27, 19, 11 or 3, and none of those is a multiple of 5. Confirmed by listing totals to 100.

**5.3** Ben picks some of the numbers from 1 to 20. What is the smallest number of numbers he must pick to be sure that one of his numbers is exactly double another of his numbers?
Answer: 15. Solution: split 1 to 20 into chains where each number is double the one before: {1, 2, 4, 8, 16}, {3, 6, 12}, {5, 10, 20}, {7, 14}, {9, 18}, and 11, 13, 15, 17, 19 alone. He can pick at most 3 + 2 + 2 + 1 + 1 + 5 = 14 numbers without a double; the 15th forces one. Confirmed by checking every subset.

## 6. Packing and cutting [draft, not yet in the program] (suggested for L34 or L18)

**6.1** A sheet of card is 9 cm wide and 7 cm tall. Zara cuts cards that are 4 cm by 5 cm (a card can be turned either way) from it. What is the largest number of cards she can cut?
Answer: 2. Solution: area 63 is more than 3 cards (60), so the area test says "up to 3", but two cards cannot be one above the other because 4 + 4 = 8 is more than 7. So any two cards are side by side, each at least 4 cm wide, and three of them need at least 12 cm of the 9 cm. Two fit (4 wide plus 5 wide). Confirmed by exhaustive search.

**6.2** A floor is 9 m by 9 m. How many tiles of 2 m by 5 m (turned either way) can be laid with no overlap?
Answer: 8. Solution: the area is 81 and each tile is 10, so at most 8. To fit 8, make four blocks of 4 by 5 (each holds 2 tiles) in a pinwheel round a 1 m square in the middle: 4 + 5 = 9. Confirmed by exhaustive search.

**6.3** A chessboard (8 by 8 squares) has two opposite corner squares cut off. Can the other 62 squares be covered exactly by 31 dominoes (each covers 2 touching squares)?
Answer: No. Solution: colour the board in two colours as a chessboard; opposite corners have the same colour, so after removing them there are 30 squares of one colour and 32 of the other, and every domino covers one of each.

## 7. Nested fractions and telescoping sums [draft, not yet in the program] (suggested for L11)

**7.1** Work out 1 / (3 + 1 / (2 + 1 / (4 + 1/2))). Give the answer as a fraction.
Answer: 20/69. Solution: from the bottom up: 4 + 1/2 = 9/2; 2 + 2/9 = 20/9; 3 + 9/20 = 69/20; and 1 divided by 69/20 is 20/69.

**7.2** Work out 1/(3 x 5) + 1/(5 x 7) + 1/(7 x 9) + ... + 1/(49 x 51). Give the answer as a fraction.
Answer: 8/51. Solution: each term 1/(n x (n + 2)) equals half of (1/n - 1/(n + 2)), so everything cancels in the middle: half of (1/3 - 1/51) = half of 16/51 = 8/51.

**7.3** Put the digits 1, 2, 3 and 4 into the four boxes, each once, to make a + 1/(b + 1/(c + 1/d)). (a) What is the largest possible value? (b) What is the smallest?
Answer: (a) 43/9 with a = 4, b = 1, c = 3, d = 2; (b) 38/31 with a = 1, b = 4, c = 2, d = 3. Solution: a is the whole part, so it is biggest (or smallest) first; a larger b makes the fraction smaller, so b is smallest (or largest); and so on in alternating order. Confirmed by trying all 24 orders.

## 8. Rate, work and passing [draft, not yet in the program] (suggested for L13)

**8.1** Lina can paint a fence in 10 hours and Ben can paint the same fence in 15 hours. Lina starts alone and paints for 2 hours; then Ben joins her. How many hours do they take altogether?
Answer: 6.8 hours (6 hours 48 minutes). Solution: Lina does 2/10 = 1/5 alone; in 1 hour together they do 1/10 + 1/15 = 1/6; the remaining 4/5 takes 4/5 divided by 1/6 = 4.8 hours; add the first 2 hours.

**8.2** A train 180 m long runs at 15 m/s. A second train 120 m long runs at 10 m/s on the next track. How long do they take to pass each other completely (from the front of one meeting the front of the other, until the back of one passes the back of the other) when they go (a) in opposite directions, (b) in the same direction with the faster one catching the slower one?
Answer: (a) 12 seconds, (b) 60 seconds. Solution: together they must cover 180 + 120 = 300 m; opposite directions the gap closes at 15 + 10 = 25 m/s, same direction at 15 - 10 = 5 m/s.

**8.3** Two cyclists start together at the same point on a circular track 400 m round and go in opposite directions at 5 m/s and 7 m/s. How many times do they meet in 10 minutes, counting a meeting at exactly 10 minutes but not the start?
Answer: 18. Solution: they close 12 m each second, so they meet every 400 / 12 = 33 1/3 seconds; 600 / (100/3) = 18.

## 9. Triangles with the same height, and dissections [draft, not yet in the program] (suggested for L18 or L14)

**9.1** ABCD is a rectangle 12 cm long (AB) and 8 cm tall (BC). M is the middle of BC and N is the middle of CD. What is the area of triangle AMN?
Answer: 36 cm squared. Solution: take the three corner triangles away from the rectangle (area 96): ABM = 12 x 4 / 2 = 24, ADN = 8 x 6 / 2 = 24, MCN = 4 x 6 / 2 = 12; 96 - 60 = 36.

**9.2** In triangle ABC (area 90 cm squared), D is on side BC so that BD is 2/5 of BC. E is the middle of line AD. What is the area of triangle EBD?
Answer: 18 cm squared. Solution: ABD and ABC share the same height from A, so ABD is 2/5 of 90 = 36; E is the middle of AD, so triangle EBD has the same base BD and half the height of ABD: 18.

**9.3** P is a point inside parallelogram ABCD, which has area 84 cm squared. Triangle PAB has area 19 cm squared and triangle PBC has area 25 cm squared. Find the areas of triangles PCD and PDA.
Answer: PCD = 23 cm squared, PDA = 17 cm squared. Solution: the heights of PAB and PCD from P add up to the height of the parallelogram, so together they are half the area: 42, giving 42 - 19 = 23; the same for PBC and PDA: 42 - 25 = 17.

## 10. Counting by size and rearrangements [draft, not yet in the program] (suggested for L31 or L5)

**10.1** How many rectangles of any size (squares included) are in a grid 3 squares tall and 5 squares wide?
Answer: 90. Solution: a rectangle is a choice of 2 of the 4 horizontal lines (6 ways) and 2 of the 6 vertical lines (15 ways): 6 x 15 = 90.

**10.2** A triangle has a base with 6 points on it (the two corners and 4 more between them). Every point on the base is joined to the top corner. How many triangles are in the figure?
Answer: 15. Solution: each triangle has the top corner and two of the 6 base points: 6 x 5 / 2 = 15.

**10.3** Each child in a group brings one gift and the gifts are mixed up and handed out, one to each child, so that nobody gets their own gift. In how many ways can this happen for (a) 4 children, (b) 6 children?
Answer: (a) 9, (b) 265. Solution: for 4 children list the 9 ways that leave no child fixed (3 pairs of swaps plus 6 four-cycles); for 6 children use a program that tries all 720 orders. Confirmed by program.

## 11. Clever computation [draft, not yet in the program] (suggested for L19)

**11.1** Work out 4005 x 4005 - 4003 x 4007 without a calculator.
Answer: 4. Solution: 4003 x 4007 = (4005 - 2) x (4005 + 2) = 4005 x 4005 - 4, so the difference is 4. Draw it as a rectangle with a strip cut off.

**11.2** Work out 6.3 x 7.2 + 3.7 x 7.2 + 7.2 x 90.
Answer: 720. Solution: every part has 7.2: 7.2 x (6.3 + 3.7 + 90) = 7.2 x 100.

**11.3** Work out 1 - 2 + 3 - 4 + 5 - 6 + ... + 99 - 100.
Answer: -50. Solution: group in pairs: (1 - 2), (3 - 4), ..., (99 - 100), 50 pairs each worth -1.

## Notes for the owner

- 33 problems, 11 types. Single-occurrence contest types (clock hands, rounding intervals, consecutive sums, the number-pyramid and picture-rule puzzles, equal sharing of a total) are left out on purpose: the evidence is too thin.
- Items 3.1 and 3.2 are good places for a "find all" statement (3.2 has two answers). Items 5.2, 6.1 and 6.2 end with an argument that is more important than the answer; ask for the argument.
- Item 4.3 and 4.2 need a real die and real cubes to be fair to children who cannot yet picture it.
- Item 10.3(b) and 1.2 are meant to be solved with a short program; that is the coding bridge.
