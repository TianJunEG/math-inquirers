# Original Go further practice problems for Level 3 (ages 8-10)

**Draft, not yet in the program.** Written for the gaps and high-frequency types found in `g3_analysis.md`. Every problem is new (own context, numbers and wording; none is a copy or light rewording of a contest problem). Every answer was worked by hand and then confirmed by a short brute-force script. They have not been tried with children or reviewed by a tutor, so check reading load and difficulty first. They stay inside the P3 level rules in `p3/SPEC.md` (no decimals except money, no ratio, no multiplier or divisor of 2 digits, no negative numbers). Suggested lessons for each type are in brackets; no lesson file was changed.

Items that need a drawing in the program (the cube grid, the clock, the circle shapes) are given here as text so the designer can draw them.

## 1. Spatial thinking [draft, not yet in the program] (suggested beside L7 or as a recurring warm-up)

**1.1** Siti builds a block city on a 3 by 3 floor. The numbers show how many cubes are stacked on each square (front row first):

| | left | middle | right |
|---|---|---|---|
| front row | 3 | 1 | 2 |
| middle row | 0 | 2 | 1 |
| back row | 1 | 0 | 4 |

(a) How many cubes are there? (b) Looking straight down from above, how many squares can you see? (c) Looking from the front, you see each column as tall as its tallest stack. How many squares do you see?
Answer: (a) 14, (b) 7, (c) 9. Solution: rows total 6 + 3 + 5 = 14; 7 squares are not empty; the tallest stacks in the three columns are 3, 2 and 4.

**1.2** Ali holds a round clock up to a mirror. In the mirror the clock shows 2:20 (the minute hand points at 4). What time is it really?
Answer: 9:40. Solution: a mirror swaps left and right, so a mirror time shows 12:00 minus the real time; 12:00 minus 2:20 is 9:40, and the minute hand really points at 8.

**1.3** A 3 by 3 by 3 cube is made of 27 small cubes. Its outside is painted red and it is broken up into the 27 small cubes. How many small cubes have (a) 3 red faces, (b) 2 red faces, (c) 1 red face, (d) no red face?
Answer: 8, 12, 6, 1. Solution: corners 8, edge middles 12, face centres 6, hidden centre 1, and 8 + 12 + 6 + 1 = 27.

## 2. Divisibility and counting multiples [draft, not yet in the program] (suggested for L3 or L5)

**2.1** Ravi's locker code is a 4-digit number of the form 5 _ _ 2. Both missing digits are the same, and the code can be divided exactly by 3. List every code that could be his.
Answer: 5112, 5442, 5772. Solution: the digits add to 7 plus twice the missing digit, which is a multiple of 3 only for 1, 4 and 7.

**2.2** Mei sticks a star on every page of a 200-page book whose number is in the 8 times table. How many stars are on pages 50 to 200 (both included)?
Answer: 19. Solution: 200 ÷ 8 = 25 stars on pages 1 to 200, and 6 of them (8, 16, ..., 48) are before page 50, so 25 − 6 = 19.

**2.3** How many whole numbers from 1 to 100 can be divided exactly by 4 or by 6 (or by both)?
Answer: 33. Solution: 25 in the 4s, 16 in the 6s, and the 8 numbers in both (the 12s) were counted twice, so 25 + 16 − 8 = 33.

**2.4** Which digits can go in the box so that 4 _ 6 is a 3-digit number that can be divided exactly by 6? List the numbers.
Answer: 426, 456, 486. Solution: it is already even, so it must also be in the 3s, which needs 10 + box to be a multiple of 3: the box is 2, 5 or 8.

## 3. Clever adding [draft, not yet in the program] (suggested for L2)

**3.1** Work out without column addition: 98 + 47 + 2 + 53 + 150 + 250.
Answer: 600. Solution: 98 + 2 = 100, 47 + 53 = 100, 150 + 250 = 400.

**3.2** Work out: 250 + 94 + 36 − 50 − 14 − 6.
Answer: 310. Solution: pair each take-away with its partner: 250 − 50 = 200, 94 − 14 = 80, 36 − 6 = 30.

**3.3** Work out 999 + 1998 + 2997 by thinking of each number as a round number take away something.
Answer: 5994. Solution: 1000 + 2000 + 3000 = 6000, then take away 1 + 2 + 3 = 6.

## 4. Number sentences and undoing a chain [draft, not yet in the program] (suggested for L2 or L5)

**4.1** Mei thinks of a number. She adds 9, multiplies by 4, subtracts 8, divides by 6 and gets 12. What was her number?
Answer: 11. Solution: undo from the end: 12 × 6 = 72, 72 + 8 = 80, 80 ÷ 4 = 20, 20 − 9 = 11.

**4.2** Find the number that goes in both boxes: box × 7 − box = 4 × 9 + 12.
Answer: 8. Solution: 7 boxes take away 1 box leaves 6 boxes; 6 boxes = 36 + 12 = 48, so a box is 8.

## 5. Counting carefully [draft, not yet in the program] (suggested for L10, or beside L8)

**5.1** A straight path is 60 m long. There is a lamp post at both ends and one every 5 m between them. (a) How many lamp posts are there? (b) A round running track is also 60 m long, with a lamp post every 5 m. How many lamp posts does it have?
Answer: (a) 13, (b) 12. Solution: 60 ÷ 5 = 12 gaps; a path has one more post than gaps, but on a ring the last gap ends at the first post.

**5.2** A bell strikes 5 times in 12 seconds, with the same gap between strikes. How long does it take to strike 9 times?
Answer: 24 seconds. Solution: 5 strikes have 4 gaps, so a gap is 3 seconds; 9 strikes have 8 gaps, 8 × 3 = 24.

**5.3** A rectangle is cut into a grid of 2 rows and 3 columns of squares. How many rectangles of any size (squares count) can you find in it?
Answer: 18. Solution: count by shape: 1 by 1: 6, 1 by 2: 4, 1 by 3: 2, 2 by 1: 3, 2 by 2: 2, 2 by 3: 1; total 18.

**5.4** Mei has 4 T-shirts and 3 skirts. She never wears her red T-shirt with her red skirt. How many different outfits can she make?
Answer: 11. Solution: 4 × 3 = 12 outfits, and 1 of them is the red pair.

## 6. Adding a long list by pairing [draft, not yet in the program] (suggested for L2 or L10)

**6.1** (a) How many numbers are in the list 12, 14, 16, ..., 30? (b) Work out their total.
Answer: (a) 10, (b) 210. Solution: 12 up to 30 in steps of 2 is 10 numbers; first plus last is 42 and there are 5 such pairs: 5 × 42 = 210.

**6.2** Ali saves 5¢ on day 1, 10¢ on day 2, 15¢ on day 3, and so on, 5¢ more each day, for 16 days. How much has he saved in all, in dollars?
Answer: $6.80. Solution: day 16 is 80¢; day 1 plus day 16 is 85¢ and there are 8 such pairs: 8 × 85 = 680¢.

**6.3** 1 + 3 + 5 + 7 = 16 and 1 + 3 + 5 + 7 + 9 = 25. Predict the total of the first 10 odd numbers (1 + 3 + ... + 19), then check it by pairing.
Answer: 100. Solution: the totals are 4 × 4 and 5 × 5, so 10 odd numbers give 10 × 10 = 100; pairing: five pairs of 20 (1 + 19, 3 + 17, ...) = 100.

## 7. Optimising with a limit [draft, not yet in the program] (suggested for L9 or L10)

**7.1** An apple costs $3 and a pear costs $5. Siti spends exactly $41 on fewer than 10 fruits. How many apples and how many pears does she buy?
Answer: 2 apples and 7 pears. Solution: the only ways to make $41 are 12 apples and 1 pear (13 fruits), 7 and 4 (11 fruits), or 2 and 7 (9 fruits); only the last has fewer than 10 fruits.

**7.2** A 100 cm rope is cut into pieces that are all 7 cm or 9 cm long, with no rope left over. (a) What is the most pieces you can make? (b) What is the fewest?
Answer: (a) 14, (b) 12. Solution: the only ways are 13 pieces of 7 cm and 1 of 9 cm (14 pieces) or 4 pieces of 7 cm and 8 of 9 cm (12 pieces).

**7.3** Ravi's stamp prints digits using drops of ink: a 1 uses 2 drops, a 7 uses 3 drops, and every other digit uses 5 drops. What is the biggest number he can print using exactly 13 drops?
Answer: 711111. Solution: more digits make a bigger number, and 6 digits (12 drops if all are 1s) is the most; the one spare drop turns one 1 into a 7, and a 7 in front is biggest.

## 8. Shape sums [draft, not yet in the program] (suggested beside L2 magic squares)

**8.1** Put the numbers 1, 2, 3, 4 and 5 once each in the 5 circles of a plus sign (two lines of 3 circles that cross at the middle circle) so that both lines have the same total. Which numbers can go in the middle? What is the biggest total?
Answer: the middle can be 1, 3 or 5; the biggest total is 10. Solution: the two lines together add 15 plus the middle number, and that must be even, so the middle is odd; with 5 in the middle the lines are 1, 5, 4 and 2, 5, 3, both 10.

**8.2** Put the numbers 1 to 6 once each in the 6 circles of a triangle (one circle on each corner and one in the middle of each side) so that the 3 numbers along every side have the same total. What are the smallest and biggest totals you can make?
Answer: smallest 9, biggest 12. Solution: the three sides add to 21 plus the corner total, and that must be a multiple of 3; corners 1, 2, 3 give 9 (side middles 6, 4, 5) and corners 4, 5, 6 give 12 (middles 3, 1, 2); 10 and 11 are also possible.

## 9. Possible or impossible [draft, not yet in the program] (suggested for L10)

**9.1** Ravi picks 4 different cards from cards numbered 1 to 9 and adds them. What is the smallest total he can get, and the biggest? Can he get 36?
Answer: 10 and 30; no. Solution: smallest 1 + 2 + 3 + 4 = 10, biggest 6 + 7 + 8 + 9 = 30, and 36 is bigger than 30.

**9.2** Ben picks 5 different odd numbers between 1 and 19 and adds them. The smallest total he could get is 25 and the biggest is 75. Can his total be 50? Explain.
Answer: No. Solution: 5 odd numbers always add to an odd number (2 odds make an even, so pairs cancel and one odd is left over), and 50 is even.

**9.3** Ali, Ben, Mei and Siti each hold one card: 36, 40, 45 or 52. Ali's number is odd. Mei's number is in the 9 times table. Ben's number is in the 4 times table and is neither the smallest nor the biggest of the four. Who holds which card?
Answer: Ali 45, Mei 36, Ben 40, Siti 52. Solution: Ali has the only odd card, 45; Mei then has 36, the only other card in the 9s; Ben's is in the 4s and not 36 or 52, so 40; Siti has 52.

## 10. Finding the rule [draft, not yet in the program] (suggested for L3 or L10)

**10.1** The sign ♣ works on two numbers: 2 ♣ 3 = 8, 5 ♣ 1 = 10, 4 ♣ 6 = 28, 7 ♣ 2 = 21. What is 6 ♣ 5?
Answer: 36. Solution: each answer is the first number times the second, plus the first number again (2 × 3 + 2 = 8), so 6 × 5 + 6 = 36.

**10.2** A number machine gives these results: 3 in, 11 out; 5 in, 19 out; 8 in, 31 out. (a) What comes out when 20 goes in? (b) What went in if 59 came out?
Answer: (a) 79, (b) 15. Solution: the machine multiplies by 4 and takes away 1; 20 × 4 − 1 = 79, and undoing 59: 59 + 1 = 60, 60 ÷ 4 = 15.

**10.3** Look at 3, 4, 7, 12, 19, 28, ... What are the gaps, and what is the 8th number?
Answer: gaps 1, 3, 5, 7, 9 (up by 2 each time); the 8th number is 52. Solution: the next gaps are 11 and 13, so 28 + 11 = 39 and 39 + 13 = 52.

## 11. Calendar and timetable [draft, not yet in the program] (suggested for L5 or L9)

**11.1** Ali's birthday party is on a Saturday. His school trip was 59 days before the party. On which day of the week was the trip?
Answer: Wednesday. Solution: 59 = 8 weeks and 3 days; 8 weeks back is still Saturday, and 3 days before Saturday is Wednesday.

**11.2** At the zoo the bird show lasts 40 minutes and starts at 10:00, 11:30, 13:15 and 15:00. The seal show lasts 55 minutes and starts at 10:20, 12:10, 14:00 and 15:45. Mei arrives at 10:30 and wants to see both shows, one after the other. She needs 10 minutes to walk between them. What is the earliest time she can finish?
Answer: 13:55. Solution: birds first (11:30 to 12:10) means seals at 14:00 and finishing at 14:55; seals first (12:10 to 13:05), walk to 13:15, then birds 13:15 to 13:55, which is earlier.

**11.3** A red light flashes every 4 seconds and a blue light flashes every 6 seconds. They flash together at the start. How many more times do they flash together in the next 2 minutes, counting a flash exactly at 2 minutes?
Answer: 10. Solution: they meet every 12 seconds (12 is the first number in both the 4s and the 6s), and 120 ÷ 12 = 10.

## 12. Equations from prices and weights [draft, not yet in the program] (suggested for L4)

**12.1** On a balance: 3 kiwis weigh the same as 2 apples; 1 apple weighs the same as 3 cherries; 1 lime weighs the same as 1 kiwi and 3 cherries. (a) Which fruit is the heaviest? (b) How many cherries weigh the same as 1 lime and 1 apple together?
Answer: (a) the lime, (b) 8. Solution: apple 3 cherries, kiwi 2 cherries, lime 2 + 3 = 5 cherries; lime and apple 5 + 3 = 8.

**12.2** A set of 2 mugs and 3 plates costs $22. A set of 2 mugs and 1 plate costs $14. How much does 1 mug cost?
Answer: $5. Solution: the first set has 2 more plates and costs $8 more, so a plate is $4; then 2 mugs cost $14 − $4 = $10.

**12.3** A box with 12 books weighs 5 kg. The same box with 7 of the same books weighs 3 kg 500 g. How heavy is the empty box?
Answer: 1 kg 400 g. Solution: 5 books weigh 1500 g, so a book is 300 g; 12 books are 3600 g, and 5000 − 3600 = 1400 g.

**12.4** Three friends pay $6, $10 and $4 for a box of 100 sweets and share the sweets so everyone gets the same number of sweets for each dollar. How many sweets does the friend who paid $10 get?
Answer: 50. Solution: they pay $20 for 100 sweets, which is 5 sweets for each dollar, and 10 × 5 = 50.

## 13. Counting numbers with rules [draft, not yet in the program] (suggested for L1)

**13.1** In Even Land every counting number is written only with the digits 0, 2, 4, 6 and 8, so the counting numbers go 2, 4, 6, 8, 20, 22, ... (no zero on its own). (a) What is the 15th counting number? (b) How many 2-digit counting numbers are there?
Answer: (a) 60, (b) 20. Solution: 4 one-digit numbers, then 20 to 28 (5), 40 to 48 (5) make 14, so the 15th is 60; a 2-digit number has 4 choices for the tens digit and 5 for the ones, 4 × 5 = 20.

**13.2** How many times is the digit 7 written when you write all the numbers from 1 to 250?
Answer: 45. Solution: in the ones place 7, 17, ..., 247 gives 25; in the tens place 70 to 79 and 170 to 179 gives 20; there is no 7 in the hundreds place.

**13.3** How many 3-digit numbers have three different digits that add up to 6?
Answer: 14. Solution: the digit sets are {1, 2, 3} (6 numbers), {0, 1, 5} (4 numbers, 0 cannot lead) and {0, 2, 4} (4 numbers); 6 + 4 + 4 = 14.

## 14. Perimeter changes [draft, not yet in the program] (suggested for L7)

**14.1** A square's sides are all made 3 cm longer and the new square has a perimeter of 40 cm. What was the area of the original square?
Answer: 49 cm². Solution: the new side is 40 ÷ 4 = 10 cm, so the old side was 7 cm and 7 × 7 = 49.

## Where I did not write problems, and why

- **Cryptarithms**: Level 3 Lesson 2 already has more than enough (Think harder 5 to 8, Go further 3, 4 and 9). No gap.
- **Bar models and bar graphs**: Lessons 4 and 10 already cover them well; the equation and difference items in section 12 are only for the contest's "two weighings" and price-per-item twists.
- **Picture patterns and "which picture matches" items** (19-2, 19-11, 20-3, 19-4 as a drawing, 20-15): these cannot be asked fairly in text. They need hand-drawn figures; I wrote nothing so as not to guess at the drawings.
