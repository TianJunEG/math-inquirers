# Original Go further practice problems for Level 5 (ages 10-12)

**Draft, not yet in the program.** Written for the gaps and high-frequency types found in `g5_analysis.md`. Every problem is new (own context, numbers and wording; none is a copy or light rewording of a contest problem). Every answer was worked by hand and then confirmed by a short brute-force script (checked over all cases, not just the answer). They have not been tried with children or reviewed by a tutor, so check reading load and difficulty first. They are written as Go further and flagged draft; a Start here and a Think harder step would need to come before them if the owner adopts a topic.

Level rules from `p5/SPEC.md`: no algebra with letters (the letters in the cryptarithms stand for digits only), no speed, no ratio notation, no percentage change. Two groups below break a rule on purpose and are flagged: section 4 (speed, one problem) and section 5 (ratio written with a colon, which the SPEC avoids). The owner decides whether to use them. Section 5 also gives a way to write each without notation.

Items that need a drawing (the ring and wheel of circles, the triangle figure, the dice) are described in words here so a designer can draw them.

Section 1 is the largest gap (nothing in the holiday course, no lesson in the term plan). Each section says which term-plan lesson it would sit beside.

## 1. Least and greatest possible, and totals that cannot be made [draft, not yet in the program] (suggested for term plan lesson 32 or a Review lesson)

**1.1** Mei's post shop only has 4¢ stamps and 9¢ stamps, as many of each as she likes. An amount is "made" if some of the stamps add up to it exactly (for example 17¢ is made by two 4¢ stamps and one 9¢ stamp). (a) What is the largest amount that cannot be made? (b) How many different amounts cannot be made? (Do not count 0¢.)
Answer: (a) 23¢, (b) 12.
Solution: the amounts that cannot be made are 1, 2, 3, 5, 6, 7, 10, 11, 14, 15, 19 and 23; 24, 25, 26 and 27 can all be made (6 fours, 4 fours and a nine, 2 fours and 2 nines, 3 nines), and adding 4¢ stamps reaches every amount after that.

**1.2** 43 stickers are shared among 5 children. Everyone gets at least 1 sticker and no two children get the same number. What is the biggest number the child with the fewest stickers can have?
Answer: 6.
Solution: if the fewest were 7, the others would need at least 8, 9, 10 and 11, which is 45 in all (too many); with 6 it works, for example 6, 7, 8, 9 and 13.

**1.3** From the whole numbers 1 to 24 pick as many as you can so that none of the numbers you pick is exactly double another number you pick. How many can you pick?
Answer: 16.
Solution: link numbers that double (1, 2, 4, 8, 16; 3, 6, 12, 24; 5, 10, 20; 7, 14; 9, 18; 11, 22; and 13, 15, 17, 19, 21, 23 on their own); you can take at most every other number in a chain: 3 + 2 + 2 + 1 + 1 + 1 + 6 = 16.

**1.4** Ten different positive whole numbers are chosen. The product of any six of them is even, and the sum of all ten is even. What is the smallest the sum can be?
Answer: 58.
Solution: any six numbers must include an even one, so at most 5 are odd; an even sum needs an even count of odd numbers, so at most 4; the smallest list is the odds 1, 3, 5, 7 and the evens 2, 4, 6, 8, 10, 12, which add to 16 + 42 = 58.

## 2. Divisibility, remainders and counting multiples [draft, not yet in the program] (suggested for term plan lesson 2, and 32 for 2.1)

**2.1** When 150 is divided by a whole number n, the remainder is 6. Find the sum of all the possible values of n.
Answer: 387.
Solution: n must divide 150 − 6 = 144 and must be bigger than the remainder 6; those are 8, 9, 12, 16, 18, 24, 36, 48, 72 and 144, which add to 387.

**2.2** How many whole numbers from 1 to 300 are multiples of 6 but not multiples of 9?
Answer: 34.
Solution: there are 50 multiples of 6; the 16 multiples of 18 are the ones that are also multiples of 9, so 50 − 16 = 34.

**2.3** The 5-digit number 4 _ 7 _ 1 has the same digit written in both blanks, and the number can be divided exactly by 9. Which number is it?
Answer: 43731.
Solution: the digits add to 12 + 2 × (the blank digit); that must be a multiple of 9, and only 18 works (blank digit 3).

## 3. Cryptarithms [draft, not yet in the program] (suggested as a weekly puzzle, or in term plan lesson 9 or 31)

In each puzzle different letters stand for different digits, the same letter always stands for the same digit, and no number starts with 0.

**3.1** ABC + DBC = CEAD. Find the 4-digit number CEAD.
Answer: 1082 (A = 8, B = 4, C = 1, D = 2, E = 0, so 841 + 241 = 1082).
Solution: the sum is under 2000, so C = 1; the ones column then gives D = 2; the tens column gives A = 2B; and the hundreds column A + D must reach 10 + E, which leaves only B = 4, A = 8, E = 0.

**3.2** BECA − CBC = BAD. Find the 3-digit number BAD.
Answer: 178 (B = 1, E = 0, C = 9, A = 7, D = 8, so 1097 − 919 = 178).
Solution: rewrite as CBC + BAD = BECA; the sum is under 2000 so B = 1, and the columns then force the rest; a check of every assignment finds this one only.

**3.3** AB × AB = CAAB, where AB is a 2-digit number. Find AB.
Answer: 76 (76 × 76 = 5776, so C = 5).
Solution: a square that ends in the same digit B as its root means B is 0, 1, 5 or 6; trying the 2-digit numbers ending in those digits, only 76 gives the pattern CAAB.

## 4. Working together and catching up [draft, not yet in the program] (suggested for term plan lesson 15; 4.2 uses speed, which the SPEC excludes and Level 6 previews, so use it only if the owner agrees)

**4.1** Mrs Lim and Mr Lee together paint a fence in 10 days. Mrs Lim and Mr Ong together paint it in 15 days. Mr Lee and Mr Ong together paint it in 12 days. (a) How many days do all three take working together? (b) How many days would Mrs Lim take working alone?
Answer: (a) 8 days, (b) 24 days.
Solution: in one day the three pairs do 1/10 + 1/15 + 1/12 = 1/4 of the fence, and that counts each person twice, so all three do 1/8 a day; Mrs Lim alone does 1/8 − 1/12 = 1/24 a day.

**4.2** Mei leaves home at 9:00 a.m. and walks along a straight road at 4 km an hour. Ravi leaves the same house at 9:30 a.m. and cycles along the same road, the same way, at 12 km an hour. At what time does Ravi catch up with Mei, and how far from home are they?
Answer: 9:45 a.m., 3 km from home.
Solution: at 9:30 Mei is 2 km ahead; Ravi gains 12 − 4 = 8 km every hour, so he needs a quarter of an hour; in 45 minutes Mei has walked 3 km.

**4.3** A tap fills an empty pool in 6 hours. A drain empties a full pool in 9 hours. At noon the pool is empty and the tap and the drain are both opened. At 3 p.m. the drain is closed. At what time is the pool full?
Answer: 8 p.m.
Solution: for 3 hours the pool gains 1/6 − 1/9 = 1/18 an hour, so it is 1/6 full at 3 p.m.; the other 5/6 fills in 5 hours with the tap alone.

## 5. Ratios written with a colon [draft, not yet in the program; P6 notation, owner decision] (suggested for term plan lesson 22)

If the owner prefers to keep notation out, write each as "Ben has 5 units and Siti has 3 units" and so on; the answers do not change.

**5.1** Ben and Siti have stamps in the ratio 5 : 3. Ben gives Siti 12 stamps and then they have the same number. How many stamps do they have altogether?
Answer: 96.
Solution: Ben has 5 units and Siti 3 units; after the gift they are equal, so the 2-unit gap is 24 stamps, 1 unit is 12 and 8 units is 96.

**5.2** A bag holds red, blue and green beads in the ratio 2 : 3 : 5. There are 24 more green beads than red beads. How many beads are in the bag?
Answer: 80.
Solution: green minus red is 3 units = 24, so 1 unit is 8 and the 10 units hold 80 beads.

**5.3** A fruit stall has apples, pears and plums. The ratio of apples to pears is 3 : 4 and the ratio of pears to plums is 2 : 5. There are 28 more plums than apples. How many pieces of fruit are there?
Answer: 68.
Solution: make the pears the same in both ratios (4 becomes 8): apples 6, pears 8, plums 20 units; plums minus apples is 14 units = 28, so 1 unit is 2 and 34 units is 68.

## 6. Dice and cubes [draft, not yet in the program] (suggested for term plan lesson 10 or as a recurring warm-up; real dice help)

On every standard die, opposite faces add to 7 (1 and 6, 2 and 5, 3 and 4).

**6.1** Three dice are stacked in a tower on a table. The top face of the top die shows 4. Walk round the tower and add up all the faces you can see: the four side faces of each die and the top of the top die. What is the total?
Answer: 46.
Solution: the four side faces of one die are the faces that are not its top or bottom, so they add to 21 − 7 = 14 whichever way it is turned; 3 × 14 + 4 = 46.

**6.2** Three dice stand in a row, touching end to end. Where two dice touch, the two touching faces add to 9. The left end of the row shows 1. What does the right end show?
Answer: 2.
Solution: the left die's far face is 1, so its touching face is 6; the next die's touching face is 9 − 6 = 3 and its other face is 4; the third die's touching face is 9 − 4 = 5 and its far face is 2.

**6.3** A 4 by 4 by 4 cube is made of 64 small cubes. The top, the front and the left faces (the three faces that meet at one corner) are painted red; the other three faces are not painted. The big cube is then taken apart. How many small cubes have (a) exactly one red face, (b) exactly two red faces, (c) no red face?
Answer: (a) 27, (b) 9, (c) 27 (and 1 cube has three red faces).
Solution: the corner cube has three red faces; the three painted edges have 3 cubes each with two red faces; each painted face has 3 × 3 = 9 cubes with only that face red; the unpainted block is 3 by 3 by 3 = 27; 1 + 9 + 27 + 27 = 64.

## 7. Counting figures and numbers [draft, not yet in the program] (suggested for term plan lesson 25)

**7.1** Triangle ABC has three points P, Q and R marked on side BC between B and C. Lines are drawn from A to P, to Q and to R. A line DE parallel to BC is drawn, with D on AB and E on AC, so that it crosses all three lines. How many triangles of any size are in the picture?
Answer: 20.
Solution: every triangle has corner A; its other two corners are two of the 5 points on BC (B, P, Q, R, C) or two of the 5 points on DE (D and E and the 3 crossings), and each choice gives one triangle: 10 + 10 = 20.

**7.2** How many different even 4-digit numbers bigger than 3000 can be made from the digits 1, 2, 3, 4, 5 and 6, if a digit may be used at most once in a number?
Answer: 120.
Solution: the first digit is 3, 4, 5 or 6; if it is odd (3 or 5) there are 3 choices for the last digit, if it is even (4 or 6) there are 2; the middle two digits come from the 4 left, in 4 × 3 = 12 ways: (2 × 3 + 2 × 2) × 12 = 120.

**7.3** How many whole numbers from 1 to 500 have no digit 5 anywhere in them?
Answer: 404.
Solution: write 000 to 499 as three digits: 5 choices for the hundreds digit (0 to 4) and 9 each for the other two give 5 × 9 × 9 = 405, take away 000 to get 404; 500 itself has a 5.

## 8. Sequences that are not a constant step [draft, not yet in the program] (suggested for term plan lessons 8 and 24)

**8.1** Look at the sequence 3, 4, 7, 12, 19, ... What is the 8th number?
Answer: 52.
Solution: the gaps are 1, 3, 5, 7, so the next gaps are 9, 11, 13: 19 + 9 = 28, 28 + 11 = 39, 39 + 13 = 52.

**8.2** Look at the sequence 2, 50, 5, 44, 8, 38, 11, ... (two sequences woven together). (a) What is the 11th number? (b) What is the sum of the first 10 numbers?
Answer: (a) 17, (b) 230.
Solution: the 1st, 3rd, 5th, ... numbers go up by 3 (2, 5, 8, ...) and the 2nd, 4th, 6th, ... go down by 6 (50, 44, 38, ...); the 11th is the 6th of the first kind, 2 + 5 × 3 = 17; the first 10 are 2 + 5 + 8 + 11 + 14 = 40 and 50 + 44 + 38 + 32 + 26 = 190, so 230.

**8.3** Mei invented a rule for the sign ★: 3 ★ 2 = 10, 5 ★ 1 = 11 and 4 ★ 3 = 17. What is 6 ★ 5?
Answer: 37.
Solution: the rule is "double the first number, then add the second number times itself": 6 + 4 = 10, 10 + 1 = 11, 8 + 9 = 17, so 6 ★ 5 = 12 + 25 = 37. (Checked against every rule made from the first number, the second, their product and their squares with small whole-number multipliers: only this one fits all three lines. A child may find a different rule; the answer to the question then has to be checked.)

## 9. Clock hands [draft, not yet in the program] (suggested for term plan lesson 30)

**9.1** Starting at 12:00 noon and stopping just before 12:00 midnight, how many times do the hour hand and the minute hand lie exactly on top of each other?
Answer: 11 times.
Solution: the minute hand gains 6° − 0.5° = 5.5° a minute on the hour hand and must gain a full 360° each time, so they meet every 720 ÷ 11 minutes; 11 times fit into 12 hours, the first at noon.

**9.2** What is the smaller angle between the hands at 9:15?
Answer: 172.5°.
Solution: the minute hand is at 15 × 6 = 90°; the hour hand has moved 9 × 30 = 270° plus a quarter of 30°, which is 7.5°, so 277.5°; the difference is 187.5°, and the smaller angle is 360° − 187.5° = 172.5°.

**9.3** From 12:00 noon to just before 12:00 midnight, how many times are the hands at a right angle to each other?
Answer: 22 times.
Solution: the gap between the hands grows by 5.5° a minute, turning through 11 complete turns in 12 hours, and in each turn it is 90° once and 270° once, which is a right angle both times: 11 × 2 = 22.

## 10. Overlapping groups, combined percent and averages [draft, not yet in the program] (suggested for term plan lessons 16, 21 and 31; averages are labelled P6 previews in the plan)

**10.1** In a class of 40 children, 27 play football, 22 play netball and 4 play neither. How many play both?
Answer: 13.
Solution: 36 children play at least one game; 27 + 22 = 49 counts the children who play both twice, so 49 − 36 = 13.

**10.2** Every child in a class speaks English or Malay, and some speak both. 31 speak English, 25 speak Malay and 12 speak both. (a) How many children are in the class? (b) How many speak only one of the two languages?
Answer: (a) 44, (b) 32.
Solution: 31 + 25 − 12 = 44; only English is 31 − 12 = 19 and only Malay is 25 − 12 = 13, and 19 + 13 = 32.

**10.3** In a test the boys' average mark was 40 and the girls' average mark was 25. There were twice as many girls as boys. What was the average mark of the whole class?
Answer: 30.
Solution: call the number of boys 1 part: the boys' marks are 40, the girls' marks are 2 × 25 = 50, and there are 3 parts of children: 90 ÷ 3 = 30.

**10.4** Class P has 40 children and 25% of them wear glasses. Class Q has 60 children and half of them wear glasses. What percentage of all the 100 children wear glasses?
Answer: 40%.
Solution: P has 10 and Q has 30 children with glasses, 40 out of 100.

## 11. Whole-number totals, and extra and short [draft, not yet in the program] (suggested for term plan lesson 26)

**11.1** Ravi spends exactly $41 on pens at $3 each and books at $5 each, and buys at least one of each. List every possible number of pens and books. Which choice gives the most items?
Answer: (12 pens, 1 book), (7 pens, 4 books) and (2 pens, 7 books); the most items is 13 (12 pens and 1 book).
Solution: what is left after the books must be a multiple of 3, which happens for 1, 4 and 7 books (36, 21 and 6 dollars of pens).

**11.2** Some sweets are shared among some children. If each child gets 5 sweets there are 17 sweets left over. If each child is to get 7 sweets, 9 sweets are missing. How many children and how many sweets are there?
Answer: 13 children and 82 sweets.
Solution: going from 5 to 7 sweets each needs 17 + 9 = 26 more sweets, which is 2 for each child, so 13 children; 5 × 13 + 17 = 82.

**11.3** Ali pays exactly $50 for cupcakes at $3 each and muffins at $4 each, and buys at least 5 muffins. In how many different ways could he have done it?
Answer: 3 ways: (10 cupcakes, 5 muffins), (6 cupcakes, 8 muffins) or (2 cupcakes, 11 muffins).
Solution: the money left after the muffins must be a multiple of 3, which happens for 5, 8 and 11 muffins; 14 muffins would cost more than $50.

## 12. Colouring circles joined by lines [draft, not yet in the program] (suggested as a weekly puzzle, or term plan lesson 31)

In each picture two circles that are joined by a line must have different colours.

**12.1** Four circles sit at the corners of a square, and each is joined by a line to the two circles next to it (so there are four lines, none across the middle). Using 3 colours, in how many ways can the circles be coloured?
Answer: 18.
Solution: try each case: using two colours the corners alternate, 3 × 2 = 6 ways; using all three colours one pair of opposite corners matches and the other two differ: 3 choices for the colour of the matching pair times 2 positions for it times 2 ways to colour the other two = 12; 6 + 12 = 18.

**12.2** A hub circle is joined to each of five circles that sit in a ring, and each circle in the ring is also joined to the two ring circles next to it. What is the least number of colours needed?
Answer: 4.
Solution: a ring of 5 cannot use only 2 colours (they would have to alternate round an odd ring), so it needs 3; the hub touches all of them, so it needs a fourth.

**12.3** Five circles are in a row, and each is joined to the next one. Using 3 colours, in how many ways can they be coloured?
Answer: 48.
Solution: 3 colours for the first circle and then 2 for each of the other four: 3 × 2 × 2 × 2 × 2 = 48.

## 13. Quick mental computation [draft, not yet in the program] (suggested as a warm-up for term plan lessons 1 and 2)

**13.1** Work out 37 × 63 + 37 × 37 without long multiplication.
Answer: 3700.
Solution: 37 × (63 + 37) = 37 × 100.

**13.2** Work out 1000 − 999 + 998 − 997 + 996 − ... + 4 − 3 + 2 − 1.
Answer: 500.
Solution: pair the numbers as (1000 − 999), (998 − 997), ..., (2 − 1): each pair is 1 and there are 500 pairs.

**13.3** Without long multiplication, find the sum of the digits of 99 999 × 7.
Answer: 45.
Solution: 99 999 × 7 = 700 000 − 7 = 699 993, and 6 + 9 + 9 + 9 + 9 + 3 = 45.

## Notes for the designer

- Not drafted because evidence is thin or the item is a picture: the knot, the matrix of pictures, mental rotation of a block figure, the patterned cube, the 5 by 5 Latin square, the nested fraction (needs dividing by a fraction, a P6 skill) and the repeated-halving process. If the owner wants any of them, they need the picture first.
- Every answer was checked by script over all cases (for example 1.1 by listing every amount to 300, 1.3 by searching every subset of 1 to 24, 1.4 over every set of ten numbers up to 16, 3.1 to 3.3 over all digit assignments, 6.3 and 7.1 by counting, 12.1 to 12.3 by trying every colouring).
