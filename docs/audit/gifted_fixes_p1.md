# Gifted-style tier rework: Primary 1

Pairs with `docs/audit/gifted_p1.md`. Work done 2026-10-22. Nothing was committed. Every changed or new numeric answer was checked in Python with exact arithmetic, and every "find all / only one answer" claim was brute-forced (109 checks, all consistent with the keys; one check in my script had a mis-ordered expected tuple, the answer itself was right).

## What changed, in short

- **Question bank** (`hp/qbank.json`) rewritten for all 10 lessons. Core items now start with objects, drawing, counting or guess-and-check; Think Harder items need the lesson idea in a new setting; Challenge items need the finished topic plus an extension. The last three Challenge items are always: a multi-step item (C1), a "find every way / generalise / combine" item (C2) and an open "make up your own / justify / what if" item (C3).
- **Printed Think Harder page** shows `stretch[0:4]` (T1 to T4) and the **Challenge page** shows `challenge[-3:]` (C1 to C3), as before. The **Stretch slide** now shows `stretch[4:7]` (these are now in the bank too) and the **Challenge slide** shows C1 to C3 (Q1 to Q3).
- **Slides**: new P1-only helper `rebuild/p1gifted.py` (called from `gen_l1.py` to `gen_l10.py` just before `p1fix.finish`) rebuilds `lN-stretch`, `lN-challenge` and `lN-chwalk` from the bank, so the slides can no longer drift from the bank. The `lN-chdiag` ("Challenge: see it") picture slide drew the retired Challenge items, so it is dropped from every deck order (its file is kept so the older generator steps still run). Each deck is one slide shorter. This loses the diagrams for the Challenge items: a gap I did not have time to close (new pictures would need `diag/panels.py` work).
- **Printed Core pages**: small scaffolds and label fixes (below). Core page counts did not change.
- **Wording**: the question-bank intro no longer says "GEP-STYLE CHALLENGE" or "ahead of the Primary 1 syllabus"; it describes the three tiers by the new principle and says the programme does not identify gifted children and is not linked to MOE.
- **Readiness Tracker and Screening Set** (`hp/mk_pack.py`): the eight screening items point at new bank indices `(1,0),(3,2),(4,0),(5,0),(6,0),(7,3),(8,2),(10,1)`; extension questions and answers were rewritten and verified.

## Per lesson: what changed

### Lesson 1: Number patterns

**Printed worksheet and keys**

- Q4: added "Write both lists first."
- Keys / slides kept consistent: lessons.js Stretch-slide key row

**Core** (6 before, 8 after): 1 unchanged; the rest rewritten with a concrete route (counters, strip, picture or "keep drawing"). Examples:

| Slot | Old item | New item | Old item's fate |
|---|---|---|---|
| Core 1 | Write the next two numbers and the rule: 4, 7, 10, 13, __, __ | A frog starts on 0 and hops 2 each time. Colour its landing places on a number strip... | moved to core |
| Core 2 | Write the next two numbers and the rule: 5, 10, 15, 20, __, __ | Count in 5s. Fill the gaps: 5, 10, __, 20, __, 30 | replaced |
| Core 3 | Write the next two numbers and the rule: 1, 5, 9, 13, __, __ | 3, 6, 9, 12, __, __. Put a counter on 3 and hop to 6, then to 9. How many steps is e... | replaced |

**Think Harder (printed T1-T4 = stretch 1-4; Stretch slide = stretch 5-7)**

| Slot | Old | New | Fate of old |
|---|---|---|---|
| T1 | unchanged | Fill in the missing numbers: 3, 8, __, 18, __, 28 | - |
| T2 | unchanged | Fill in the missing numbers: 40, __, 28, __, 16, 10 | - |
| T3 | A pattern starts at 3 and adds 5 each time. What is the 8th number? | Is 30 in the pattern 4, 8, 12, 16 … ? How do you know? | old item now in stretch |
| T4 | A pattern starts at 2 and adds 4 each time. What is the 7th number? | Start at 50 and take away 7 each time. What is the first number below 20? | old item retired |
| Slide 1 | unchanged | Ali counts from 3 in 4s: 3, 7, 11, … Will he say 39? Will he say 40? | - |
| Slide 2 | 50, 46, 42, … What is the first number less than 10? | 5, 10, 15, 22, 25, 30. One number is wrong. Which number does not belong? What... | old item retired |
| Slide 3 | unchanged | An add pattern has 11 as its 3rd number and 19 as its 5th number. What is the rule? What is the 1st... | - |

**Challenge (printed C1-C3 = Challenge slide Q1-Q3)**

| Slot | Old | New | Fate of old |
|---|---|---|---|
| C1 | Frog A starts at 3 and jumps 4 each time. Frog B starts at 5 and jumps 3 each t... | 1, 2, 4, 7, 11, 16 … What is the 8th number? Explain how the pattern grows. | old item now in challenge |
| C2 | 1, 2, 4, 7, 11, 16 … What is the 8th number? Explain how the pattern grows. | Ali counts up from 2 in 3s. Mei counts up from 1 in 4s. Which numbers up to 50... | old item now in challenge |
| C3 (open) | Ali counts up from 2 in 3s. Mei counts up from 1 in 4s. Which numbers up to 50... | Make up your own two counting patterns: choose a start and a jump for each, so... | old item retired |

Bank size: core 6 to 8, think harder 8 to 12, challenge 9 to 6.

Regenerated deck: `split/l1` (`rebuild/gen_l1.py`, then `levels/restyle.py split/l1`).

### Lesson 2: Number bonds

**Printed worksheet and keys**

- Q4 (balance sums): added "Use counters or draw dots to make both sides the same."
- Q5b and Q6 part labelled "Challenge" relabelled "Think harder" (they repeat the method)
- Keys / slides kept consistent: gen_l2 ws2ans Q6 note "Challenge" -> "Think harder"

**Core** (6 before, 9 after): 0 unchanged; the rest rewritten with a concrete route (counters, strip, picture or "keep drawing"). Examples:

| Slot | Old item | New item | Old item's fate |
|---|---|---|---|
| Core 1 | 10 = 3 + __ | You have 10 counters. 3 are red and the rest are yellow. How many are yellow? Write... | replaced |
| Core 2 | 10 = __ + 8 | A ten-frame has 6 counters in it. How many more fill it up? Write 10 = 6 + __ | replaced |
| Core 3 | 10 = 6 + __ | A ten-frame has 8 counters in it. How many more fill it up? Write 10 = __ + 8 | replaced |

**Think Harder (printed T1-T4 = stretch 1-4; Stretch slide = stretch 5-7)**

| Slot | Old | New | Fate of old |
|---|---|---|---|
| T1 | unchanged | 5 + 4 = 6 + __ | - |
| T2 | 8 + 2 = 7 + __ | 9 + 6 = __ + 10 | old item now in stretch |
| T3 | 9 + 6 = __ + 10 | 6 + 4 = 10, so 16 + 4 = __ and 26 + 4 = __ | old item now in stretch |
| T4 | 12 + 3 = 10 + __ | Find all the pairs of numbers from 1 to 11 that make 12. (3 + 9 and 9 + 3 count... | old item now in stretch |
| Slide 1 | unchanged | 13 + 7 = 10 + __ = 4 + __ | - |
| Slide 2 | unchanged | □ + □ + 4 = 20, and both boxes are the same number. What is in the box? | - |
| Slide 3 | unchanged | How many pairs make 20 if both numbers are from 5 to 15? (7 + 13 and 13 + 7 count once.) | - |

**Challenge (printed C1-C3 = Challenge slide Q1-Q3)**

| Slot | Old | New | Fate of old |
|---|---|---|---|
| C1 | Three different numbers from 1 to 7 add up to 10. Find every set of three. | Put 1 to 6 in the magic triangle so each side adds to 11. What goes in the corn... | old item now in challenge |
| C2 | Put 1 to 6 in the magic triangle so each side adds to 11. What goes in the corn... | Ali has 20 stickers. He keeps 9 and shares the rest between Ben and Mei. Ben ge... | old item now in challenge |
| C3 (open) | Ali has 20 stickers. He keeps 9 and shares the rest between Ben and Mei. Ben ge... | Change the magic triangle: use the numbers 2, 3, 4, 5, 6 and 7 instead of 1 to... | old item now in challenge |

Bank size: core 6 to 9, think harder 8 to 12, challenge 10 to 7.

Regenerated deck: `split/l2` (`rebuild/gen_l2.py`, then `levels/restyle.py split/l2`).

### Lesson 3: Picture graphs

**Printed worksheet and keys**

- no worksheet change (page count kept at 3 core pages)
- Keys / slides kept consistent: (none)

**Core** (6 before, 7 after): 2 unchanged; the rest rewritten with a concrete route (counters, strip, picture or "keep drawing"). Examples:

| Slot | Old item | New item | Old item's fate |
|---|---|---|---|
| Core 1 | A picture graph shows: Apple 7, Banana 5, Orange 9, Grape 4 (1 picture = 1 child). W... | Draw a picture graph with one dot for each child: Apple 7, Banana 5, Orange 9, Grape... | replaced |
| Core 3 | A picture graph shows: Apple 7, Banana 5, Orange 9, Grape 4 (1 picture = 1 child). H... | A picture graph shows: Apple 7, Banana 5, Orange 9, Grape 4 (1 picture = 1 child). H... | replaced |
| Core 4 | A picture graph shows: Apple 7, Banana 5, Orange 9, Grape 4 (1 picture = 1 child). H... | A picture graph shows: Apple 7, Banana 5, Orange 9, Grape 4 (1 picture = 1 child). H... | replaced |

**Think Harder (printed T1-T4 = stretch 1-4; Stretch slide = stretch 5-7)**

| Slot | Old | New | Fate of old |
|---|---|---|---|
| T1 | unchanged | 1 picture = 2 children. Red has 3 pictures, blue has 5 and green has 4. How many children chose blu... | - |
| T2 | unchanged | 1 picture = 2 children. Red has 3 pictures, blue has 5 and green has 4. How many children voted alt... | - |
| T3 | 1 picture = 2 children. Red has 3 pictures and blue has 5. How many more childr... | 1 picture = 2 children. Six children chose pizza. How many pictures should we d... | old item now in stretch |
| T4 | 1 picture = 2 children. Six children chose pizza. How many pictures should we d... | 1 picture = 2 children. A half picture means 1 child. Apple has 3 pictures and... | old item now in stretch |
| Slide 1 | Key: ● = 2 children. Apple ●●●, Banana ●●●●●, Orange ●●. How many more chose ba... | Key: ● = 2 children. Apple ●●●, Banana ●●●●●, Orange ●●. How many more chose ba... | old item retired |
| Slide 2 | unchanged | 25 children voted: apple 8, banana 6, grape 4, and the rest chose orange. Draw the orange row. Whic... | - |
| Slide 3 | unchanged | The key is missing. Apple has 4 pictures and 12 children chose apple. Banana has 3 pictures. How ma... | - |

**Challenge (printed C1-C3 = Challenge slide Q1-Q3)**

| Slot | Old | New | Fate of old |
|---|---|---|---|
| C1 | 1 picture = 3 children. Apple has 4 pictures, banana 2 and orange 5. Then 7 mor... | 24 children voted. Apple got 6 votes. Orange got 6 more votes than banana. How... | old item now in challenge |
| C2 | 24 children voted. Apple got 6 votes. Orange got 6 more votes than banana. How... | 1 picture = 2 children. 20 children voted for three fruits. A has 3 pictures. B... | old item now in challenge |
| C3 (open) | 1 picture = 2 children. 20 children voted for three fruits. A has 3 pictures. B... | Make up your own: 15 children vote for three fruits. Draw a picture graph where... | old item now in challenge |

Bank size: core 6 to 7, think harder 6 to 8, challenge 8 to 7.

Regenerated deck: `split/l3` (`rebuild/gen_l3.py`, then `levels/restyle.py split/l3`).

### Lesson 4: Repeating and growing patterns

**Printed worksheet and keys**

- Q2c (30th place): added "Keep drawing, or look for a shortcut."
- Q4 "Challenge!" relabelled "Think harder!"
- Keys / slides kept consistent: lessons.js Stretch-slide key row

**Core** (6 before, 7 after): 4 unchanged; the rest rewritten with a concrete route (counters, strip, picture or "keep drawing"). Examples:

| Slot | Old item | New item | Old item's fate |
|---|---|---|---|
| Core 1 | The pattern is circle, square, triangle, circle, square, triangle, circle … What is... | The pattern is circle, square, triangle, circle, square, triangle, circle … What is... | replaced |
| Core 4 | The pattern is A, B, C, D, A, B, C … What is the 11th one? | The pattern is A, B, C, D, A, B, C … What is the 11th one? (Write the letters in a r... | replaced |

**Think Harder (printed T1-T4 = stretch 1-4; Stretch slide = stretch 5-7)**

| Slot | Old | New | Fate of old |
|---|---|---|---|
| T1 | unchanged | Pattern: circle, triangle, triangle, square, circle, triangle, triangle, square … What is the 14th... | - |
| T2 | unchanged | Same pattern: how many triangles are in the first 20 shapes? | - |
| T3 | Same pattern: in which places do the squares come? Write the first five. | Red, blue, blue, red, blue, blue … What colour is the 20th bead? | old item retired |
| T4 | Red, blue, blue, red, blue, blue … What colour is the 20th bead? | Squares in a row need 4, 7, 10, … sticks. With 20 sticks, how many squares can... | old item now in stretch |
| Slide 1 | unchanged | star, circle, circle, triangle, star, circle, circle, triangle … What is the 23rd shape? | - |
| Slide 2 | Squares in a row need 4, 7, 10, … sticks. With 20 sticks, how many squares can... | A, B, B, C, A, B, B, C, … How many Bs are in the first 18 letters? | old item now in stretch |
| Slide 3 | A, B, B, C, A, B, B, C, … How many Bs are in the first 18 letters? | A pattern repeats every 5 shapes. Is the 25th shape the same as the 5th? Why? | old item now in stretch |

**Challenge (printed C1-C3 = Challenge slide Q1-Q3)**

| Slot | Old | New | Fate of old |
|---|---|---|---|
| C1 | Squares in a row use 4, 7, 10 … sticks. Ben has 50 sticks. How many squares can... | Beads repeat in a pattern of 5: red, red, blue, blue, green. How many green bea... | old item now in stretch |
| C2 | Beads repeat in a pattern of 5: red, red, blue, blue, green. How many green bea... | Dots: 1, 3, 6, 10, 15 … What are the next two numbers? What is the 10th number? | old item now in challenge |
| C3 (open) | Dots: 1, 3, 6, 10, 15 … What are the next two numbers? What is the 10th number? | Make up your own repeating pattern with a core of 5 beads (use up to 3 colours)... | old item now in challenge |

Bank size: core 6 to 7, think harder 6 to 13, challenge 8 to 5.

Regenerated deck: `split/l4` (`rebuild/gen_l4.py`, then `levels/restyle.py split/l4`).

### Lesson 5: Working backwards

**Printed worksheet and keys**

- Q4b changed from 8th/8th (answer 15, a Challenge-level trap) to 3rd/3rd (answer 5); 8th from both ends moved to talk time
- Keys / slides kept consistent: lessons.js Q4 key now "(b) 5 children"; talk-time 8th/8th = 15 kept; Stretch-slide row; gen_l5 ws2ans Q4b = 5

**Core** (6 before, 8 after): 5 unchanged; the rest rewritten with a concrete route (counters, strip, picture or "keep drawing"). Examples:

| Slot | Old item | New item | Old item's fate |
|---|---|---|---|
| Core 1 | I think of a number. I add 3. I get 8. What is my number? | I think of a number. I add 3. I get 8. What is my number? (Hide counters under a cup... | replaced |

**Think Harder (printed T1-T4 = stretch 1-4; Stretch slide = stretch 5-7)**

| Slot | Old | New | Fate of old |
|---|---|---|---|
| T1 | unchanged | Ben had some marbles. He gave 5 to Mei, then won 3. Now he has 12. How many did he start with? | - |
| T2 | unchanged | Ben had some stickers. He gave away 6, got 4, then gave away 3. Now he has 10. How many did he have... | - |
| T3 | unchanged | A number machine adds the same number each time. IN 4 gives OUT 9. What is the rule? What is OUT wh... | - |
| T4 | unchanged | I think of a number. I add 4, then I take away 7. I get 8. What is my number? | - |
| Slide 1 | Ali and Ben have 20 marbles together. Ali has 4 more than Ben. How many does ea... | Tom is 5th from the front. There are 4 children between Tom and Sue, who is las... | old item retired |
| Slide 2 | Ben had some stickers. He gave away 6, got 4, then gave away 3. Now he has 10.... | Mei had some sweets. Her mum gave her 6 more. Then she ate 4. Now she has 9. Ho... | old item now in stretch |
| Slide 3 | Tom is 5th from the front. There are 4 children between Tom and Sue, who is las... | I think of a number. I take away 5, then I add 8. I get 14. What is my number? | old item now in stretch |

**Challenge (printed C1-C3 = Challenge slide Q1-Q3)**

| Slot | Old | New | Fate of old |
|---|---|---|---|
| C1 | I think of a number. I add 7, take away 3, add 5, then take away 8. I get 14. W... | A number machine has two steps: add 3, then add 4. IN 5 gives OUT 12. What goes... | old item retired |
| C2 | Ali and Ben have 20 marbles together. Ali has 4 more than Ben. How many marbles... | A snail climbs 3 cm each day and slides back 1 cm each night. It starts at the... | old item now in challenge |
| C3 (open) | A snail climbs 3 cm each day and slides back 1 cm each night. It starts at the... | Make up a mystery number story with THREE steps whose answer is 10. Write the s... | old item now in challenge |

Bank size: core 6 to 8, think harder 7 to 10, challenge 9 to 6.

Regenerated deck: `split/l5` (`rebuild/gen_l5.py`, then `levels/restyle.py split/l5`).

### Lesson 6: Money

**Printed worksheet and keys**

- Q2 "Challenge!" relabelled "Think harder!"
- Keys / slides kept consistent: lessons.js: Think Harder row now T1 to T4 (T1 70c/4 coins, T2 Sam, T3 45c with 3 coins, T4 25c four ways); mistakes line now T1; Stretch-slide row; gen_l6 teachswap note T3 -> T2

**Core** (8 before, 8 after): 2 unchanged; the rest rewritten with a concrete route (counters, strip, picture or "keep drawing"). Examples:

| Slot | Old item | New item | Old item's fate |
|---|---|---|---|
| Core 1 | Pay exactly 15¢ using two coins from 5¢, 10¢, 20¢ and 50¢. | Pay exactly 15¢ using two coins from 5¢, 10¢, 20¢ and 50¢. (Use play coins.) | replaced |
| Core 2 | Pay exactly 25¢ using two coins from 5¢, 10¢, 20¢ and 50¢. | Pay exactly 40¢ using two coins from 5¢, 10¢, 20¢ and 50¢. | replaced |
| Core 3 | Pay exactly $15 with the fewest notes. The notes are $2, $5, $10 and $50. | Pay exactly 55¢ using two coins from 5¢, 10¢, 20¢ and 50¢. | replaced |

**Think Harder (printed T1-T4 = stretch 1-4; Stretch slide = stretch 5-7)**

| Slot | Old | New | Fate of old |
|---|---|---|---|
| T1 | A bag costs $34. Ali pays with a $50 note. How much change does he get? | Make 70¢ using exactly 4 coins from 5¢, 10¢, 20¢ and 50¢. Find every set. | old item now in stretch |
| T2 | Make 70¢ using exactly 4 coins from 5¢, 10¢, 20¢ and 50¢. Find every set. | Sam has only 10¢ and 20¢ coins. He pays exactly 90¢ using 6 coins. How many of... | old item now in stretch |
| T3 | Sam has only 10¢ and 20¢ coins. He pays exactly 90¢ using 6 coins. How many of... | What is the fewest number of coins to make 45¢? | old item now in stretch |
| T4 | What is the fewest number of coins to make 45¢? | How many ways can you make 25¢ using 20¢, 10¢ and 5¢ coins? | old item now in stretch |
| Slide 1 | unchanged | How many ways can you make 40¢ with 20¢, 10¢ and 5¢ coins? | - |
| Slide 2 | Mei has 6 coins, all 5¢ and 10¢, worth 45¢. How many of each? | Pay exactly $12 using exactly 3 notes or coins from $1, $2, $5 and $10. Find ev... | old item retired |
| Slide 3 | What is the fewest number of coins for 95¢ (5¢, 10¢, 20¢, 50¢)? | What is the fewest number of coins for 95¢ (5¢, 10¢, 20¢, 50¢)? How do you know... | old item retired |

**Challenge (printed C1-C3 = Challenge slide Q1-Q3)**

| Slot | Old | New | Fate of old |
|---|---|---|---|
| C1 | Ali pays 55¢ with exactly 5 coins. He uses at least one 5¢, one 10¢ and one 20¢... | You have one 5¢, one 10¢, one 20¢ and one 50¢ coin. How many different amounts... | old item now in challenge |
| C2 | You have one 5¢, one 10¢, one 20¢ and one 50¢ coin. How many different amounts... | A sweet costs 15¢ and a biscuit costs 20¢. Ben spends exactly 90¢ and buys some... | old item retired |
| C3 (open) | A sweet costs 15¢ and a biscuit costs 20¢. Ben spends exactly 90¢ and buys some... | Make up your own coin puzzle that has exactly ONE answer (for example: "exactly... | old item now in challenge |

Bank size: core 8 to 8, think harder 9 to 10, challenge 8 to 6.

Regenerated deck: `split/l6` (`rebuild/gen_l6.py`, then `levels/restyle.py split/l6`).

### Lesson 7: 2D shapes

**Printed worksheet and keys**

- Q2: added the picture strip of six labelled shapes (new `hp/shapes6.png`)
- Q4: now pictures A and B only (new `hp/trifigs_ab.png`); the 8-triangle picture C moved to talk time. Shrank the house picture and the Q2 table rows so the lesson stays on two core pages
- Keys / slides kept consistent: lessons.js Q4 key "A: 3, B: 2" (picture C = 8 is the talk-time picture); mistakes bullet; Stretch-slide row; gen_l7 key and ws2ans notes, ws1 preview Q2

**Core** (6 before, 7 after): 1 unchanged; the rest rewritten with a concrete route (counters, strip, picture or "keep drawing"). Examples:

| Slot | Old item | New item | Old item's fate |
|---|---|---|---|
| Core 1 | How many sides and corners does a triangle have? | How many sides and corners does a triangle have? Draw one and count. | replaced |
| Core 2 | How many sides and corners does a square have? | How many sides and corners does a square have? Draw one and count. | replaced |
| Core 3 | Here is a pentagon (a shape with 5 straight sides). How many corners does it have? | Draw a pentagon (a shape with 5 straight sides). How many corners does it have? | replaced |

**Think Harder (printed T1-T4 = stretch 1-4; Stretch slide = stretch 5-7)**

| Slot | Old | New | Fate of old |
|---|---|---|---|
| T1 | Fold a square along a diagonal and cut. Which shapes do you get? | Two same-size triangles can make a square. Can they also make a bigger triangle... | old item retired |
| T2 | Two same-size triangles can make a square. Can they also make a bigger triangle... | How many squares are in a grid 3 squares long and 2 squares high? | old item now in stretch |
| T3 | How many squares are in a grid 3 squares long and 2 squares high? | A square has both diagonals drawn (lines joining opposite corners). How many tr... | old item now in stretch |
| T4 | Join 4 same-size squares, whole sides touching. How many different shapes can y... | Draw a shape with 4 straight sides that is NOT a square. Is it a rectangle? How... | old item retired |
| Slide 1 | How many squares are in a grid 3 squares long and 2 squares high? | Three squares are joined in a row to make a long rectangle. How many rectangles... | old item now in stretch |
| Slide 2 | unchanged | How many rectangles are in a grid 2 squares long and 2 squares high? (Squares count too.) | - |
| Slide 3 | Join 4 same-size squares, whole sides touching. How many different shapes can y... | Cut a square along both diagonals to get 4 same-size triangles. Can you put all... | old item retired |

**Challenge (printed C1-C3 = Challenge slide Q1-Q3)**

| Slot | Old | New | Fate of old |
|---|---|---|---|
| C1 | Three squares are joined in a row to make a long rectangle. How many rectangles... | A triangle has 4 lines drawn from the top corner to the bottom. How many triang... | old item now in stretch |
| C2 | A triangle has 4 lines drawn from the top corner to the bottom. How many triang... | A square is cut into 4 equal squares. One of the small squares is cut into 4 ev... | old item retired |
| C3 (open) | A square is cut into 4 equal squares. One of the small squares is cut into 4 ev... | Draw your own triangle-counting puzzle: a big triangle with some lines inside.... | old item now in challenge |

Bank size: core 6 to 7, think harder 9 to 9, challenge 9 to 6.

Regenerated deck: `split/l7` (`rebuild/gen_l7.py`, then `levels/restyle.py split/l7`).

### Lesson 8: Logic and sorting

**Printed worksheet and keys**

- Q2: added the tip "write each number on a small paper slip and slide it into the right place first"
- Keys / slides kept consistent: (none)

**Core** (5 before, 7 after): 2 unchanged; the rest rewritten with a concrete route (counters, strip, picture or "keep drawing"). Examples:

| Slot | Old item | New item | Old item's fate |
|---|---|---|---|
| Core 1 | Ali is taller than Ben. Ben is taller than Mei. Who is the tallest? Who is the short... | Ali is taller than Ben. Ben is taller than Mei. Who is the tallest? Who is the short... | replaced |
| Core 4 | Which number is the odd one out: 2, 4, 6, 9, 10? Why? | Ben stands in front of Mei. Mei stands in front of Sam. Who is in the middle? | replaced |
| Core 5 | Sort these numbers into odd and even: 3, 8, 5, 12, 7, 10. | Odd numbers end in 1, 3, 5, 7 or 9. Which number is the odd one out: 2, 4, 6, 9, 10?... | replaced |

**Think Harder (printed T1-T4 = stretch 1-4; Stretch slide = stretch 5-7)**

| Slot | Old | New | Fate of old |
|---|---|---|---|
| T1 | unchanged | In a race, Sam is ahead of Tia. Tia is ahead of Raj. Mei is ahead of Sam. Who is third? | - |
| T2 | unchanged | Ana, Bo and Cy each have a different toy: a ball, a kite or a yo-yo. Bo does not have the kite. Cy... | - |
| T3 | unchanged | Numbers 1 to 12. Which do we say when counting in 2s? Which when counting in 3s? Which in both? | - |
| T4 | unchanged | Numbers 1 to 12. Which do we NOT say when counting in 2s or when counting in 3s? | - |
| Slide 1 | unchanged | Ali, Ben, Cara and Dan each have a different pet: a cat, a dog, a fish or a rabbit. Cara has the do... | - |
| Slide 2 | unchanged | Five children stand in a line. Ali is in the middle. Ben is just in front of Ali. Cara is last. Dan... | - |
| Slide 3 | unchanged | Numbers 1 to 30: which do you say when counting in 2s AND when counting in 5s? | - |

**Challenge (printed C1-C3 = Challenge slide Q1-Q3)**

| Slot | Old | New | Fate of old |
|---|---|---|---|
| C1 | Five friends run a race. D is first. E is last. B finishes directly behind A. C... | A secret number is between 10 and 30. It is even, and you say it when counting... | old item now in stretch |
| C2 | A secret number is between 10 and 30. It is even, and you say it when counting... | Numbers 1 to 20. Sort them in a two-loop picture with the loops "I say it count... | old item now in challenge |
| C3 (open) | Numbers 1 to 20. How many do we say only when counting in 2s, only in 3s, in bo... | Make up your own "Who has which pet?" puzzle with three friends and three pets.... | old item retired |

Bank size: core 5 to 7, think harder 6 to 9, challenge 8 to 6.

Regenerated deck: `split/l8` (`rebuild/gen_l8.py`, then `levels/restyle.py split/l8`).

### Lesson 9: Length

**Printed worksheet and keys**

- Q3b: hint to measure with big paper clips and then small cubes
- Q6b: "Put a finger on 3 and hop to 8, counting each space."
- Keys / slides kept consistent: lessons.js Stretch-slide row; gen_l9 ws2 preview Q3 and Q6

**Core** (6 before, 7 after): 4 unchanged; the rest rewritten with a concrete route (counters, strip, picture or "keep drawing"). Examples:

| Slot | Old item | New item | Old item's fate |
|---|---|---|---|
| Core 4 | A rope is 8 cubes long. A string is 8 paper clips long. Do we know which is longer?... | Put in order from shortest: 11 cubes, 7 cubes, 9 cubes, 12 cubes. | moved to stretch |
| Core 5 | Put in order from shortest: 11 cubes, 7 cubes, 9 cubes, 12 cubes. | A ribbon lies from the 2 cm mark to the 7 cm mark on a ruler. How long is it? (Put a... | moved to core |
| Core 6 | A ribbon lies from the 2 cm mark to the 7 cm mark on a ruler. How long is it? | A string is 9 cubes long. A rope is 4 cubes longer. How long is the rope? | replaced |

**Think Harder (printed T1-T4 = stretch 1-4; Stretch slide = stretch 5-7)**

| Slot | Old | New | Fate of old |
|---|---|---|---|
| T1 | A caterpillar is 9 cubes long. It grows 2 cubes each day. How long is it after... | A ribbon lies from the 3 cm mark to the 11 cm mark on a ruler. How long is it? | old item now in stretch |
| T2 | A string is 15 cubes long. A rope is 8 cubes longer. How long is the rope? | A red ribbon lies from the 2 cm mark to the 9 cm mark. A blue ribbon lies from... | old item retired |
| T3 | A ribbon lies from the 3 cm mark to the 11 cm mark. How long is it? | 1 clip is as long as 3 cubes. A pen is 12 cubes long. How many clips long is th... | old item retired |
| T4 | unchanged | A pencil is 3 erasers long. A ruler is 2 pencils long. A desk is 4 rulers long. How many erasers lo... | - |
| Slide 1 | A crayon lies from the 3 cm mark to the 11 cm mark on a ruler. How long is it? | A ribbon 15 cubes long is cut into 3 equal pieces. How long is each piece? How... | old item retired |
| Slide 2 | A pencil is 3 erasers long. A ruler is 2 pencils long. A desk is 4 rulers long.... | A string is 6 paper clips long. 1 paper clip is as long as 2 cubes. Ben says th... | old item now in stretch |
| Slide 3 | A ribbon 15 cubes long is cut into 3 equal pieces. How long is each piece? How... | A pencil is 8 cm long. It starts at the 3 cm mark on a ruler. At which mark doe... | old item now in stretch |

**Challenge (printed C1-C3 = Challenge slide Q1-Q3)**

| Slot | Old | New | Fate of old |
|---|---|---|---|
| C1 | A stick is 12 cubes long. Ali measures a desk by laying the stick end to end 4... | A train has 3 carriages. Each is 6 cubes long. There is a gap of 1 cube between... | old item now in challenge |
| C2 | Ali’s pencil is 9 cubes. Mei’s is 2 cubes shorter than Ali’s. Ben’s is 3 cubes... | A ribbon 30 cubes long is cut into three pieces. The first is 4 cubes longer th... | old item retired |
| C3 (open) | A ribbon 30 cubes long is cut into three pieces. The first is 4 cubes longer th... | Make up your own measuring puzzle that uses TWO different units (for example cl... | old item now in challenge |

Bank size: core 6 to 7, think harder 7 to 10, challenge 8 to 5.

Regenerated deck: `split/l9` (`rebuild/gen_l9.py`, then `levels/restyle.py split/l9`).

### Lesson 10: Mixed puzzles

**Printed worksheet and keys**

- Q5b: now the one-line triangle (new `hp/tri_one.png`, answer 3); the two-line 6-triangle picture is now only the teaching picture
- Keys / slides kept consistent: lessons.js Q5 key "(b) 3 triangles"; Stretch-slide row; gen_l10 ws2ans and notes

**Core** (6 before, 6 after): 5 unchanged; the rest rewritten with a concrete route (counters, strip, picture or "keep drawing"). Examples:

| Slot | Old item | New item | Old item's fate |
|---|---|---|---|
| Core 6 | How many sides does a hexagon have? | How many sides does a hexagon have? (Draw one if you like.) | replaced |

**Think Harder (printed T1-T4 = stretch 1-4; Stretch slide = stretch 5-7)**

| Slot | Old | New | Fate of old |
|---|---|---|---|
| T1 | A pattern starts at 5 and adds 3 each time. What is the 10th number? | A pattern starts at 4 and adds 6 each time. What is the 8th number? Is 50 in th... | old item retired |
| T2 | Ali has 12 stickers. He gives 5 to Mei and then gets 3 more. How many does he h... | Mei thinks of a number, adds 7, takes away 2 and gets 19. Ben does the same and... | old item now in stretch |
| T3 | Which three coins from 5¢, 10¢, 20¢ and 50¢ make 45¢? | Ali has 5 coins worth 60¢. He has only 5¢, 10¢ and 20¢ coins. Find every possib... | old item retired |
| T4 | A ribbon is 12 cubes. A string is 5 cubes shorter. How long is the string? | Votes: Apple 6, Banana 9, Orange 7. Then 5 more children vote and all choose ap... | old item retired |
| Slide 1 | Mei thinks of a number, adds 7, takes away 2 and gets 19. Ben does the same and... | A ribbon 10 cubes long is cut into pieces that are 2 cubes or 3 cubes long, wit... | old item now in stretch |
| Slide 2 | 4, 9, 14, 19, … Which number in this pattern is closest to 50? | Ben is in front of Mei. Sam is last. Ali is not first. Mei is in front of Ali.... | old item now in stretch |
| Slide 3 | Ali has 5 coins worth 60¢. He has only 5¢, 10¢ and 20¢ coins. Find every possib... | Ali has 7 coins. They are all 10¢ and 5¢ coins and are worth 50¢. How many of e... | old item now in stretch |

**Challenge (printed C1-C3 = Challenge slide Q1-Q3)**

| Slot | Old | New | Fate of old |
|---|---|---|---|
| C1 | Frog A jumps in 3s from 0 and frog B jumps in 5s from 0. Which numbers up to 60... | Triangles in a row use 3, 5, 7 … sticks. Squares in a row use 4, 7, 10 … sticks... | old item retired |
| C2 | Ali has some stickers. Ben has 4 more than Ali. Mei has 3 fewer than Ben. Toget... | Ali has some stickers. Ben has 4 more than Ali. Mei has 3 fewer than Ben. Toget... | unchanged |
| C3 (open) | Make 70¢ using exactly 4 coins from 5¢, 10¢, 20¢ and 50¢. How many ways are the... | Pick any puzzle from today (a puzzle card or a worksheet question). Change ONE... | old item retired |

Bank size: core 6 to 6, think harder 5 to 9, challenge 9 to 4.

Regenerated deck: `split/l10` (`rebuild/gen_l10.py`, then `levels/restyle.py split/l10`).

## Regenerated decks

`split/l1` to `split/l10`, each with `python3 rebuild/gen_lK.py` then `python3 levels/restyle.py split/lK`. `rebuild/preview.py` reported no overflow on the stretch, challenge, chwalk, ws2 and ws2ans slides of any deck. The decks are one slide shorter (chdiag dropped). The published deck artifacts need republishing from `split/l1..l10` (lead's step).

## Final page counts

| File | Before | After |
|---|---|---|
| Student workbook (designed PDF) | 49 | 49 (page map unchanged: L1 p3-6, L2 p7-10, L3 p11-15, L4 p16-19, L5 p20-23, L6 p24-27, L7 p28-31, L8 p32-35, L9 p36-39, L10 p40-43) |
| Tutor guide | 60 | 61 |
| Question bank | 29 | 32 |
| Readiness Tracker and Screening Set | 5 | 6 |
| Weekly Dose of Thinking Math (parent pack) | 24 | 25 |
| Weekly email pack | 7 | 7 |
| Weekly PDFs zip | week 4: 8 and 10 pages, week 5: 11 and 10 | week 4: 8 and 10, week 5: 11 and 11 (student, tutor) |
| P1 scheme of work | 2 | 2 |

The workbook was 50 pages after the first rebuild because the new Lesson 7 picture strip pushed Q2 onto its own page; shrinking the house picture (250 to 200 px wide), the new shapes strip (560 to 440 px) and the Q2 table rows put L7 back on two core pages. The tutor guide, question bank, tracker and parent pack grew by one to three pages because the bank has more items and longer answers. The brief required the workbook page count to be kept; it did, and the growth in the other files is a consequence of more content, not a layout fault.

## Re-audit after the rework

By the same classification as the audit, every item on the printed core pages, the printed Think Harder and Challenge pages, the Stretch and Challenge slides and the bank was designed to pass the tier test, so the after-rework compliance is 100% by construction. That is the designer's reading, not an independent check. Known soft spots:

- L5 Q4b (3rd from the front and the back, answer 5) is now the same case as the worked example on the teaching slide. It is a safe Core item, but a child who watched the slide only copies it.
- Core scaffolds ("use counters", "keep drawing") invite the concrete route; they do not guarantee that a child who has never seen the topic will manage unaided. No pilot has been run.
- Three criteria moved on the rubric (see the summary table in `gifted_p1.md`): low-floor/high-ceiling, challenge ladder and problem posing, by at most one point each. Metacognition, justification, multiple solution paths and student-led inquiry did not change, because the rework did not add routines for them. The level is still "partly gifted-style".

## Files touched

- Content: `hp/qbank.json`, `hp/lessons.js`, `hp/qbank_doc.js`, `hp/mk_pack.py`.
- Printed: `hp/workbook.js`, `hp/workbook_html.js`; new images `hp/shapes6.png`, `hp/trifigs_ab.png`, `hp/tri_one.png`.
- Generators: `rebuild/gen_l1.py` to `rebuild/gen_l10.py`; new P1-only helper `rebuild/p1gifted.py`.
- Shared files (`rebuild/slidekit.py`, `hp/levelkit.js`, `levels/*`): NOT edited. (`levels/scheme.py p1` and `levels/restyle.py` were only run.)
- Outputs refreshed in `outputs/workbook`, `outputs/designed`, `outputs/schemes`. Built printed files also left in `hp/`.

## Notes for the lead

- `hp/qbank.py` is stale relative to `hp/qbank.json`; do not regenerate the JSON from it.
- `hp/mk_pack.py` picks the screening items by bank index, so reordering the Challenge lists silently changes the screening set.
- Republish the P1 deck artifacts from `split/l1..l10`.
- Gaps still open: no diagrams for the new Challenge items (chdiag dropped); no written reflection routine; no pilot with children.
