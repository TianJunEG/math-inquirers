# Original Go further practice problems for Level 2 (ages 7-9)

**Draft, not yet in the program.** Written for the gaps and high-frequency types found in `g2_analysis.md`. Every problem is new (new context, new numbers, written from the skill and not from any contest problem). Every answer was checked by hand and by a short script (every "find all" and "exactly one answer" claim was brute-forced). They have not been tried with children or reviewed by a tutor, so check reading load and difficulty first. Suggested homes are lessons where the idea fits; none is a change to Start here.

Level 2 rules kept: multiplication and division only from the 2, 3, 4, 5 and 10 tables; numbers within 1000; no decimals; no negative numbers; leftovers are said in words ("2 left over"), never written as remainders. Where a calendar is used, children count days on a printed calendar page, not from a times-table.

## 1. Sequences with a changing rule (L4)

**1.1** In a game, level 1 is worth 4 points and level 2 is worth 5 points. From level 3 on, each level is worth the two levels before it added together. How many points is level 7 worth?
Answer: 60. Solution: 4, 5, 9, 14, 23, 37, 60.

**1.2** 5, 6, 8, 11, 15, 20, __, __. Write the next two numbers. Will the pattern ever say 40?
Answer: 26 and 33; no. Solution: the steps are 1, 2, 3, 4, 5, then 6 and 7, so it goes 26, 33, 41 and jumps over 40.

**1.3** Two rules are mixed together: 10, 3, 20, 6, 30, 9, __, __. Write the next two numbers. What is the 14th number?
Answer: 40 and 12; the 14th number is 21. Solution: places 1, 3, 5, 7 go up by 10 and places 2, 4, 6, 8 go up by 3; the 14th place is the 7th number of the "3" rule: 3, 6, 9, 12, 15, 18, 21.

## 2. Ages (L5, beside the before-and-after bars)

**2.1** Ben is 7 years old and his cousin Nur is 12. How old will Nur be when Ben is 20?
Answer: 25. Solution: Nur is always 5 years older than Ben, and 20 + 5 = 25.

**2.2** In 4 years' time, Mei and her brother will be 30 years old altogether. Mei is 2 years older than her brother. How old are they now?
Answer: Mei 12, her brother 10. Solution: in 4 years each is 4 older, so now they add up to 30 − 8 = 22; take away the extra 2 (20), share (10 and 10), give the 2 back to Mei (12). Check: 16 + 14 = 30.

**2.3** Mum is 32 and Mei is 8. In how many years will Mum be 3 times as old as Mei?
Answer: 4 years. Solution: Mum is always 24 years older; Mum is 3 times Mei only when 24 is 2 times Mei's age, so Mei is 12 and Mum is 36.

**2.4** (bonus) Ana says to Raj: "When I was as old as you are now, you were only 6." Ana is 22. How old is Raj?
Answer: 14. Solution: the age gap is the same now and back then. Try Raj's age and make a table: Raj 12, gap 10, back then 2; Raj 13, gap 9, back then 4; Raj 14, gap 8, back then 6, which is right.

## 3. Calendar and time units (L9)

**3.1** Today is Friday. A school trip is 30 days from today. On which day of the week is the trip?
Answer: Sunday. Solution: 30 days is 4 weeks and 2 days, so go 2 days on from Friday.

**3.2** A month has 31 days and the 1st is a Wednesday. Which days of the week happen 5 times in that month? What day is the 1st of the next month?
Answer: Wednesday, Thursday and Friday happen 5 times; the next month starts on a Saturday. Solution: 31 days is 4 weeks and 3 days, so the first 3 weekdays (Wed, Thu, Fri) are used 5 times, and day 32 is 3 days after a Wednesday.

**3.3** Siti waters a plant every 3 days. She waters it on a Monday first. List the days of the week for her first 8 waterings. When does she water on a Monday again?
Answer: Monday, Thursday, Sunday, Wednesday, Saturday, Tuesday, Friday, Monday; so on the 8th watering, 21 days later. Solution: count 3 days on each time from Monday and write the day name each time.

## 4. Clever adding: pairing numbers (L2)

**4.1** Mei stacks cans: 1 can in the top row, 2 in the next row, and so on, up to 20 cans in the bottom row. How many cans are there altogether?
Answer: 210. Solution: pair the rows 1 and 20, 2 and 19, 3 and 18 ...: each pair makes 21 and there are 10 pairs, so 21 × 10 = 210.

**4.2** Add: 12 + 18 + 25 + 32 + 38 + 45.
Answer: 170. Solution: 12 + 38 = 50, 18 + 32 = 50, 25 + 45 = 70, and 50 + 50 + 70 = 170.

**4.3** Add all the numbers in the 5 times table from 5 to 50: 5 + 10 + 15 + ... + 50.
Answer: 275. Solution: pair the first and last: 5 + 50, 10 + 45, ... make 55 five times, and 55 × 5 = 275.

## 5. Worst case: how many must I take to be sure? (L10, act it out with a bag of counters)

**5.1** A bag has 6 red, 5 blue and 4 green counters. Without looking, how many counters must you take out to be sure you have 2 of the same colour?
Answer: 4. Solution: in the worst case you take one of each colour (3 counters) and the 4th must match one of them.

**5.2** A box has 7 red, 7 yellow and 3 green cubes. Without looking, how many cubes must you take to be sure you have 3 of the same colour?
Answer: 7. Solution: the worst case is 2 red, 2 yellow and 2 green (6 cubes), and the 7th cube makes 3 of one colour.

**5.3** A jar has 9 mint, 6 lemon and 5 cherry sweets. Without looking, how many must Mei take to be sure she has at least one of each of the 3 flavours?
Answer: 16. Solution: the worst case is all 9 mint and all 6 lemon first (15 sweets), so the 16th must be cherry.

## 6. Doing things together: rate (L3 or L9)

**6.1** A small oven bakes 3 cookies at a time and each batch takes 10 minutes. How long does it take to bake 9 cookies? How long for 10 cookies?
Answer: 30 minutes; 40 minutes. Solution: 9 cookies is 3 batches (3 × 10), and the 10th cookie needs a 4th batch.

**6.2** 4 painters, all working at the same speed, paint a hall in 6 hours. How long would 2 of the painters take?
Answer: 12 hours. Solution: half as many painters take twice as long.

**6.3** One tap fills a tank in 12 minutes. How long do 3 of the same taps take together to fill it?
Answer: 4 minutes. Solution: 3 taps share the work, so 12 minutes is cut into 3 equal parts of 4.

## 7. Picture and symbol equations (L5 or L9, beside the balance puzzles)

**7.1** ★ + ★ + ● = 17 and ★ + ● + ● = 16. What is ★ + ●? What is ★?
Answer: ★ + ● = 11 and ★ = 6 (● = 5). Solution: add the two lines to get 3 stars and 3 dots = 33, so 1 star and 1 dot = 11; then ★ + ● + ★ = 17 means ★ = 17 − 11 = 6.

**7.2** At a fair, 2 stickers can be traded for 1 badge, and 3 badges can be traded for 2 pins. How many stickers are worth 4 pins?
Answer: 12 stickers. Solution: 4 pins is 2 lots of "3 badges for 2 pins" = 6 badges, and 6 badges = 6 × 2 = 12 stickers.

**7.3** ■ × 4 − ■ + 2 = 17. What number is ■?
Answer: 5. Solution: 4 of something take away 1 of it is 3 of it, so 3 × ■ + 2 = 17, 3 × ■ = 15 and ■ = 5. Check: 20 − 5 + 2 = 17.

**7.4** (bonus) In a number game, ○ doubles a number, ▲ takes away 3, and ■ adds 5. Ravi puts a number through ○, then ▲, then ■ and gets 22. What number did he start with?
Answer: 10. Solution: undo from the end: 22 − 5 = 17, 17 + 3 = 20, 20 ÷ 2 = 10. Check: 10 → 20 → 17 → 22.

## 8. Counting figures and ways (L8)

**8.1** Dots make a hollow square: each side of the square has 8 dots, and the corner dots belong to two sides. How many dots are there?
Answer: 28. Solution: 4 sides of 8 is 32, but the 4 corners were counted twice, so 32 − 4 = 28.

**8.2** Ali walks from Home to School on a grid of paths. He may only go right or down. The trip is 3 steps right and 2 steps down (5 steps). How many different routes are there?
Answer: 10. Solution: write the number of ways to reach each corner; each corner is the sum of the one above and the one to its left: row 1 is 1, 1, 1, 1; row 2 is 1, 2, 3, 4; row 3 is 1, 3, 6, 10.

**8.3** Five dots are drawn as shown: 3 in a bottom row and 2 in a top row, no other 3 dots in a straight line.
```
  •   •
•   •   •
```
(The top dots sit above the gaps between the bottom dots.) How many triangles can you make by joining 3 of the dots?
Answer: 9. Solution: there are 10 ways to choose 3 dots from 5, but the 3 dots in the bottom row are in one straight line, so that choice makes no triangle: 10 − 1 = 9.

**8.4** Five children each shake hands once with every other child. How many handshakes are there? What if there are 6 children?
Answer: 10; 15. Solution: the first child shakes 4 hands, the next 3 new ones, then 2, then 1: 4 + 3 + 2 + 1 = 10; with 6 children, 5 + 4 + 3 + 2 + 1 = 15.

## 9. Spatial thinking (L8)

**9.1** The numbers show how many cubes are stacked in each place of a 3 by 3 floor plan (0 means no cubes):
```
 3  1  2
 2  2  1
 1  0  3
```
(a) How many cubes are there altogether? (b) How many places have a stack exactly 3 cubes tall? (c) How many more cubes would make every one of the 9 places 3 cubes tall?
Answer: (a) 15 (b) 2 (c) 12. Solution: 3 + 1 + 2 + 2 + 2 + 1 + 1 + 0 + 3 = 15; the 3s are in the top-left and bottom-right; 9 places of 3 is 27 cubes, and 27 − 15 = 12.

**9.2** On a normal die, opposite faces add up to 7. A die sits on the table with 2 on top, 3 facing you and 1 on the right. What numbers are on the bottom, at the back and on the left?
Answer: bottom 5, back 4, left 6. Solution: each hidden face is 7 minus the face opposite it: 7 − 2, 7 − 3, 7 − 1.

**9.3** Use the die from 9.2 (2 on top, 3 facing you, 1 on the right). It is rolled once to the right, over its right-hand bottom edge. What number is on top now? What is on top after it is rolled to the right again?
Answer: 6, then 5. Solution: rolling right brings the left face to the top (the left face is 6), then again brings the new left face to the top (the 5, which was the bottom). Hold a real die to check.

## 10. Mirrors (L9 warm-up; only if a mirror idea is wanted, this type is low priority)

**10.1** Mei sees a clock in a mirror. In the mirror it looks like 8:20. What time is it really?
Answer: 3:40. Solution: a mirror swaps left and right, so the time on the mirror clock and the real time add up to 12:00: 12:00 − 8:20 = 3:40. (Check by drawing both clocks.)

**10.2** Which o'clock times look exactly the same in a mirror?
Answer: 6 o'clock and 12 o'clock. Solution: only when both hands lie on the line between 12 and 6 does the mirror change nothing.

## 11. Grids with rules (L10)

**11.1** A strip has 8 boxes in a row. Some boxes hide a gem. A box with a number has no gem; the number tells how many gems are in the boxes next to it (left and right). The numbers are: box 1 shows 1, box 3 shows 2, box 5 shows 1, box 7 shows 1. Where are the gems?
Answer: boxes 2, 4 and 8. Solution: box 1 has only one neighbour, so box 2 has a gem; box 3 shows 2, so boxes 2 and 4 are gems; box 5 shows 1 and box 4 is a gem, so box 6 is empty; box 7 shows 1 and box 6 is empty, so box 8 is a gem. This is the only way.

**11.2** Put the numbers 1, 2, 3 and 4 in the 4 by 4 grid so that each row and each column has each number once. Five boxes are already filled in: row 1 box 3 is 3, row 2 box 4 is 2, row 3 box 2 is 4, row 4 box 2 is 2 and row 4 box 4 is 1.
Answer:
```
 2 1 3 4
 4 3 1 2
 1 4 2 3
 3 2 4 1
```
Solution: row 4 already has 2 and 1, so it needs 3 and 4 in boxes 1 and 3; column 3 already has a 3, so row 4 box 3 is 4 and box 1 is 3. Then fill column by column. A computer check found that this is the only grid that fits the five clues.

**11.3** Put the numbers 1, 2, 3, 4 and 5 in the five boxes of a cross (one in the middle, one above, one below, one left, one right) so that the three numbers going across add up to the same total as the three numbers going down. Which numbers can go in the middle?
Answer: 1, 3 or 5 only. Solution: the middle number is in both lines, so the other four numbers must split into two pairs with the same sum. With 1 in the middle: 2 + 5 and 3 + 4 (totals 8). With 3: 1 + 5 and 2 + 4 (total 9). With 5: 1 + 4 and 2 + 3 (total 10). With 2 or 4 in the middle, the four other numbers add to 13 or 11 (an odd number), which cannot be split into two equal pair sums.

**11.4** A number pyramid: each block is the sum of the two blocks under it. The bottom row is 20, ?, ?, 30. The middle block of the second row is 70. What is the top block?
Answer: 260. Solution: the middle block 70 = the two unknown numbers added; the second row is (20 + first), 70, (second + 30); the top is the sum of the second row: 20 + 30 + 3 × 70 = 260 (the 70 is counted 3 times). You do not need the two missing numbers.

## 12. Logic: tracking and truth (L10)

**12.1** Ali, Ben and Cai each start with 6 counters. Ali gives 2 to Ben. Then Ben gives 3 to Cai. Then Cai gives 1 to Ali. Who has the most counters now? Who has the same number?
Answer: Cai has the most (8). Ali and Ben have the same number (5 each). Solution: Ali 6 − 2 + 1 = 5, Ben 6 + 2 − 3 = 5, Cai 6 + 3 − 1 = 8 (total still 18).

**12.2** Someone ate the last cake: Ali, Ben or Cai. Ali says "It was Cai." Ben says "It was not Ali." Cai says "It was not me." Exactly one of the three is telling the truth. Who ate the cake?
Answer: Ali. Solution: test each person. If Ali did it, only Cai tells the truth (one truth). If Ben did it, Ben and Cai tell the truth (two). If Cai did it, Ali and Ben tell the truth (two). So it was Ali.

**12.3** Four boxes P, Q, R and S. Box P fits inside box Q. Box R fits inside box P. Boxes Q and S are the same size. Which must be true? (a) R fits inside S. (b) S fits inside P. (c) Q fits inside R.
Answer: only (a). Solution: R is smaller than P, P is smaller than Q, and S is as big as Q, so R is the smallest and fits inside S; S is bigger than P and Q is bigger than R, so (b) and (c) are false.

## 13. Growth that grows (L4)

**13.1** Tiles are laid in a staircase. Figure 1 has 1 tile. Figure 2 has 3 tiles (a row of 1 on top of a row of 2). Figure 3 has 6 tiles (rows of 1, 2 and 3). How many tiles are in Figure 8? Which figure is the first to use more than 50 tiles?
Answer: 36 tiles; Figure 10 (55 tiles). Solution: each new figure adds a new bottom row: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55.

**13.2** Cubes are stacked in square layers: the top layer has 1 cube, the next has 4 cubes (2 by 2), the next 9 cubes (3 by 3), then 16 and 25. How many cubes are in all 5 layers?
Answer: 55. Solution: 1 + 4 + 9 + 16 + 25 = 55.

**13.3** Triangles of dots: row 1 has 1 dot, row 2 has 2 dots, row 3 has 3 dots, and so on. How many dots are in a triangle with 10 rows?
Answer: 55. Solution: pair the rows 1 and 10, 2 and 9 ...: 5 pairs of 11 = 55.

## 14. Multiples and leftovers (L3 and L4)

**14.1** What is the biggest 2-digit number that is in both the 4 times table and the 5 times table?
Answer: 80. Solution: numbers in both tables are 20, 40, 60, 80 (and 100 is not a 2-digit number).

**14.2** Find every number between 30 and 50 that is in the 3 times table and leaves 1 left over when put into groups of 4.
Answer: 33 and 45. Solution: the 3 times table gives 33, 36, 39, 42, 45, 48; 33 = 8 groups of 4 and 1, 45 = 11 groups of 4 and 1; the others leave 0, 3, 2 or 0.

**14.3** Nur has 350 beads. She makes bracelets of 4 beads each. How many bracelets can she make? How many beads are left over?
Answer: 87 bracelets and 2 beads left over. Solution: 300 beads make 75 bracelets (100 beads make 25), 50 beads make 12 bracelets with 2 left over: 75 + 12 = 87.

## 15. Bar-model extensions (L2, L5, L7)

**15.1** Ali, Ben and Cai have 86 stickers altogether. Ben has twice as many as Ali. Cai has 6 more than Ben. How many stickers does each have?
Answer: Ali 16, Ben 32, Cai 38. Solution: draw Ali as 1 bar, Ben as 2 bars, Cai as 2 bars and 6 more; take away the 6 to get 80 for 5 equal bars, so one bar is 16. Check: 16 + 32 + 38 = 86.

**15.2** Mei has some stickers to give to her friends. If she gives each friend 3 stickers, she has 8 left over. If she tries to give each friend 5 stickers, she is 2 stickers short. How many friends and how many stickers?
Answer: 5 friends and 23 stickers. Solution: giving 2 more to each friend takes the 8 left over and 2 more, which is 10 stickers, so 10 ÷ 2 = 5 friends; 5 × 3 + 8 = 23. Check: 5 × 5 = 25, which is 2 more than 23.

**15.3** A rope is cut into 2 pieces. The long piece is 3 times as long as the short piece, and it is 90 cm longer than the short piece. How long was the rope?
Answer: 180 cm. Solution: the long piece is 3 bars and the short piece is 1 bar, so the 90 cm is 2 bars and 1 bar is 45 cm; 45 + 135 = 180.

## 16. Fence posts, circles and queues (L9)

**16.1** A snail takes 15 minutes to crawl from the 1st fence post to the 4th post. The posts are equally spaced. How long to crawl from the 1st post to the 10th?
Answer: 45 minutes. Solution: from post 1 to post 4 is 3 gaps, so 15 ÷ 3 = 5 minutes a gap; post 1 to post 10 is 9 gaps, 9 × 5 = 45.

**16.2** 12 lamps are placed equally spaced round a pond. The gap between 2 lamps next to each other is 5 m. How far is it round the pond?
Answer: 60 m. Solution: on a ring there are as many gaps as lamps, so 12 gaps of 5 m, and 12 × 5 = 60 (6 × 10).

**16.3** Mei is 4th from the front and 6th from the back of a queue. How many children are in the queue? How many children must join at the front so that Mei is exactly in the middle?
Answer: 9 children; 2 more at the front. Solution: 3 in front, Mei, 5 behind: 3 + 1 + 5 = 9. To be in the middle she needs the same number in front as behind (5), so 2 more join the front. Then there are 11 children and Mei is 6th from each end.

## 17. Letter sums (L2)

Different letters stand for different digits, and a 2-digit or 3-digit number does not start with 0.

**17.1** AB + AB = BCC. Find A, B and C.
Answer: A = 6, B = 1, C = 2 (61 + 61 = 122). Solution: two 2-digit numbers add to at most 198, so the 3-digit answer starts with 1 and B = 1. Ones: B + B = 2, so C = 2. Tens: A + A must make 12 (the 2 in the tens place and a carry of 1 to the hundreds), so A = 6. Check: 61 + 61 = 122.

**17.2** AA + BB = CBC. Find A, B and C.
Answer: A = 9, B = 2, C = 1 (99 + 22 = 121). Solution: the answer is 3-digit and at most 198, so C = 1. The ones digit of A + B is 1, so A + B = 11 and the sum is 121; its middle digit is B = 2, so A = 9. Check: 99 + 22 = 121.

**17.3** AB + BA = CDC. Find every way to do it. What do C and D always turn out to be?
Answer: 6 ways: 38 + 83, 83 + 38, 47 + 74, 74 + 47, 56 + 65, 65 + 56. C is always 1 and D is always 2 (every total is 121). Solution: the ones and the tens both add A + B, so the total is 11 × (A + B). It must look like 1D1, so A + B = 11 and the total is 121 (C = 1, D = 2). The pairs that make 11 are 2 + 9, 3 + 8, 4 + 7 and 5 + 6 (each in 2 orders), but the pair 2 + 9 is not allowed because D is already 2 and different letters need different digits. That leaves 6 ways (a computer search agrees).

## 18. Patterns that move (L4)

**18.1** Five letters stand in a row: A B C D E. Every step, all letters move one place to the right and the letter on the end jumps to the front (after step 1 the row is E A B C D). What is the row after 23 steps? What is the first time the row is A B C D E again?
Answer: C D E A B after 23 steps; after 5 steps. Solution: the row repeats every 5 steps, 23 is 4 groups of 5 plus 3, so it is the same as after 3 steps (C D E A B).

**18.2** Each tile has a shape and a colour. Each row and each column has each of the 3 shapes (circle, square, triangle) once and each of the 3 colours (red, green, blue) once.
```
 circle-red     square-blue   triangle-green
 square-green   triangle-red  circle-blue
 triangle-blue  ?             ?
```
Which two tiles go in the empty places?
Answer: circle-green, then square-red. Solution: column 2 has square and triangle and blue and red, so the empty tile is circle-green; column 3 has triangle and circle and green and blue, so it is square-red. Check row 3: triangle-blue, circle-green, square-red.

**18.3** An arrow points up. Every step it turns a quarter turn clockwise (to the right). Which way does it point after 30 steps?
Answer: down. Solution: 4 steps bring it back to up; 30 is 7 groups of 4 and 2 more, so 2 quarter turns: down.

## 19. One-stroke drawings (optional puzzle, very low frequency)

**19.1** Can you draw each picture without lifting your pencil and without going over a line twice? (a) a square with ONE diagonal drawn in it, (b) a square with BOTH diagonals drawn in it.
Answer: (a) yes, (b) no. Solution: count the corners where an odd number of lines meet; a picture can be drawn in one stroke only if there are 0 or 2 such corners. (a) has 2 (the ends of the diagonal, 3 lines each); (b) has 4 corners where 3 lines meet.
