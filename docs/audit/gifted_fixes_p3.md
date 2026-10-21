# P3 gifted-style rework: what changed

Companion to `docs/audit/gifted_p3.md` (the audit of the content before this rework). Tier principle used: Core approachable without the topic (objects, drawing, counting, guess-and-check, skills from below, no unexplained terms); Think Harder needs the taught idea in a new setting; Challenge needs mastery plus extension (multi-step, generalise, justify, combine, open-ended, pose, what-if). All edits are in P3 source files only. No shared file was changed (`rebuild/slidekit.py`, `hp/levelkit.js`, `levels/*` are untouched). Nothing was committed or published.

## Summary

| L | Title | Violations fixed | Bank items changed | Workbook change | Decks regenerated |
|---|---|---|---|---|---|
| 1 | Number Sleuths | 5 | 4 | hints / star labels | yes (`rebuild/gen_p3l1.py` then `levels/restyle.py split/p3l1`) |
| 2 | Cryptarithm Crackers | 5 | 9 | hints / star labels | yes (`rebuild/gen_p3l2.py` then `levels/restyle.py split/p3l2`) |
| 3 | Times Table Treasure | 5 | 8 | none | yes (`rebuild/gen_p3l3.py` then `levels/restyle.py split/p3l3`) |
| 4 | Model Makers | 8 | 10 | hints / star labels | yes (`rebuild/gen_p3l4.py` then `levels/restyle.py split/p3l4`) |
| 5 | Remainder Riddles | 5 | 6 | hints / star labels | yes (`rebuild/gen_p3l5.py` then `levels/restyle.py split/p3l5`) |
| 6 | Fraction Walls | 9 | 10 | hints / star labels | yes (`rebuild/gen_p3l6.py` then `levels/restyle.py split/p3l6`) |
| 7 | Area Architects | 10 | 9 | hints / star labels | yes (`rebuild/gen_p3l7.py` then `levels/restyle.py split/p3l7`) |
| 8 | Angle and Line Detectives | 12 | 12 | hints / star labels | yes (`rebuild/gen_p3l8.py` then `levels/restyle.py split/p3l8`) |
| 9 | Measure and Money Masters | 5 | 7 | none | yes (`rebuild/gen_p3l9.py` then `levels/restyle.py split/p3l9`) |
| 10 | Challenge Day | 5 | 8 | none | yes (`rebuild/gen_p3l10.py` then `levels/restyle.py split/p3l10`) |

Across the level 69 of 305 audited items broke the tier principle before the rework; the 69 were fixed by 83 bank edits (some are scaffolds added to items that were compliant but thin), 10 workbook hints, definitions and star labels, and slide Stretch or Challenge changes in six lessons (2, 3, 4, 5, 6, 8). A new problem-posing prompt (open-ended / make up your own / change one number) is in every lesson's printed Challenge page.

Slot rule used so slides and printed pages stay in sync: Think Harder T1-T4 and Challenge X7-X9 print on the workbook. The slide Stretch items are bank T5-T7 in Lessons 1 to 4, 9 and 10 (slide-only items in Lessons 5 to 8). The slide Challenge items are bank X8 and X9 (Lessons 1, 2, 5, 6, 7, 8, 10), X7 and X8 (Lesson 9) or X1 and X2 (Lessons 3 and 4). The new posing item is X7 in every lesson except Lesson 9 (X9), so it prints on the workbook Challenge page but never needed a new slide.

## Per lesson

### Lesson 1: Number Sleuths

**Tier moves and removals.** X4 (old: smallest number with digit sum 20, a repeat of T5) is now a prediction task that reuses the old X7 content (digit sum 4, counts 1, 3, 6, 10) as its second stage. X7 (old: list digit sum 4) is the new problem-posing item.

| Item | Old | New | Tier |
|---|---|---|---|
| C1 | Write the number: 6 thousands, 4 tens and 9 ones. | Write the number. Think of 6 big boxes of 1000 sweets, 4 packets of 10 sweets and 9 loose sweets. (There are no boxes of 100.) | Core (same tier; content as described above) |
| C2 | What is the value of the digit 8 in 2837? | Look at the place value chart:  Th 2 / H 8 / T 3 / O 7.  This is the number 2837. How much is the digit 8 worth? | Core (same tier; content as described above) |
| X4 | What is the smallest 4-digit number with all different digits that add up to 20? | 4-digit numbers whose digits add up to 3 can be counted by their first digit: 1, 3, 6. Count the ones whose digits add up to 4 by their first digit too. Use the pattern to predict how many 4-digit numbers have digits that add up to 5, and check by listing the ones that start with 4. | Challenge (same tier; content as described above) |
| X7 | How many 4-digit numbers have digits that add up to 4? Make a list in order. | Make up your own "What number am I?" puzzle. Choose a secret 4-digit number and write 3 or 4 clues about its digits. Check that ONLY ONE number fits all your clues. Then swap with a partner. | Challenge (same tier; content as described above) |

**Workbook (core pages).** Q4 (page 2): added the line 'Hint: 10 hundreds make 1 thousand. You can draw a box for each thousand, hundred, ten and one.'

**Slides.** No slide change (slide Think Harder items T5-T7 and Challenge X8, X9 are unchanged).

### Lesson 2: Cryptarithm Crackers

**Tier moves and removals.** Old X7 (shape sum ◆◆ + ●● + ▲▲) moved to X3 (still Challenge). Old X3 (Mei's number, reverse arithmetic) removed: Think Harder level and no longer fits any tier. X7 is the new posing item.

| Item | Old | New | Tier |
|---|---|---|---|
| C1 | Work out 3999 + 2456. Use a shortcut. | A library has 3999 storybooks and 2456 comic books. How many books are there altogether? Write the numbers in a Th H T O grid and add the ones first. | Core (same tier; content as described above) |
| C2 | 7000 − 2468 = ? | A shop has 7000 stickers and sells 2468 of them. How many are left? Hint: draw a number line from 2468 to 7000 and jump to 2500, then to 3000, then to 7000. Add up the jumps. | Core (same tier; content as described above) |
| C3 | Find the missing digit:  4□27 + 1365 = 5992 | Find the missing digit. Add in columns, starting with the ones, or try the digits one at a time.   4□27 + 1365 = 5992 | Core (same tier; content as described above) |
| C4 | Find the missing digit:  8□50 − 3420 = 5230 | Find the missing digit. Try 5, 6 and 7 and check each one by taking away.   8□50 − 3420 = 5230 | Core (same tier; content as described above) |
| C5 | In a magic square, every row adds up to 2400. One row has 900 and 600 in it. What is the missing number in that row? | A magic square has 3 rows. Every row adds up to the same total, 2400. One row shows 900, 600 and a box. What number goes in the box? | Core (same tier; content as described above) |
| C6 | A shop had 5000 stickers. It sold 1275 on Monday and 1480 on Tuesday. How many stickers are left? | A shop had 5000 stickers. It sold 1275 on Monday and 1480 on Tuesday. Draw a bar for the 5000 stickers and cut it into the two sold parts and the part left. How many stickers are left? | Core (same tier; content as described above) |
| T6 | Use the 9999 trick:  10 000 − 3746 = ? | Siti worked out 9999 − 3746 = 6253 by taking each digit away from 9. Use her answer to work out 10 000 − 3746 and 10 003 − 3746 without a new column subtraction. How do you know? | Think Harder (same tier; content as described above) |
| X3 | Mei thinks of a number. She adds 2500, then takes away 1750, and gets 6000. What was her number? | ◆◆ + ●● + ▲▲ = ◆●▲. Different shapes are different digits. Find them. | Challenge (same tier; content as described above) |
| X7 | ◆◆ + ●● + ▲▲ = ◆●▲. Different shapes are different digits. Find them. | Make up your own missing-digits sum. Write a 4-digit + 4-digit addition that works, then rub out exactly 3 digits in 3 DIFFERENT columns and write boxes instead. Swap with a partner. Does your partner find only one answer? Explain why your sum has only one answer. | Challenge (same tier; content as described above) |

**Workbook (core pages).** Q6 now reads '(if time) Shape puzzle'; the deck's ws2 preview matches.

**Slides.** Stretch slide item 2 (old: 'Use the 9999 trick: 10 000 − 3746') is now T6; the slide notes give 6254 and 6257.

### Lesson 3: Times Table Treasure

**Tier moves and removals.** Old X7 (sweets between 40 and 60, 6 and 9) moved to X6. Old X6 (list the six products) removed. X4 (old: 7 table ends in 3, a repeat of X2) is a new generalisation item. X7 is the new posing item.

| Item | Old | New | Tier |
|---|---|---|---|
| C1 | Find 8 × 6 and 6 × 8. What do you notice? | Draw 6 rows of 8 dots. How many dots are there? Now turn your drawing sideways: it shows 8 rows of 6 dots. How many dots now? What do you notice? | Core (same tier; content as described above) |
| C3 | Fill in the box: 7 × □ = 63 | 63 apples are packed into boxes of 7 apples with none left over. Count in 7s (7, 14, 21, …) to find how many boxes there are. | Core (same tier; content as described above) |
| C5 | Write the last digits of the 6 times table from 6 × 1 to 6 × 10. Which digits appear? | Count in 6s from 6 up to 60 (6, 12, 18, …). Write only the LAST digit of each number. Which last digits do you see? | Core (same tier; content as described above) |
| T5 | Which is more, 7 × 8 or 6 × 9? By how much? | Compare each pair. Which is more, and by how much?  (a) 7 × 7 and 6 × 8   (b) 8 × 8 and 7 × 9   (c) 7 × 8 and 6 × 9.  What do you notice? | Think Harder (same tier; content as described above) |
| T8 | Mei’s age × 6 = 48. Ali’s age × 7 = 63. Who is older, and by how many years? | Find three different ways to work out 8 × 9 using facts you already know (for example 5 × 9 plus something). Write each way and the answer. | Think Harder (same tier; content as described above) |
| X4 | Siti writes the 7 times table from 7 × 1 to 7 × 20. How many answers end in 3? | In the 8 times table, which digits can NEVER be the last digit of an answer? Explain why. Is the same true for the 6 times table? | Challenge (same tier; content as described above) |
| X6 | Mei multiplies two DIFFERENT numbers from 6, 7, 8 and 9. Find all the answers she can get. | Mei has between 40 and 60 sweets. She can share them equally among 6 friends with none left over. She can also share them equally among 9 friends with none left over. How many sweets does she have? | Challenge (same tier; content as described above) |
| X7 | Mei has between 40 and 60 sweets. She can share them equally among 6 friends with none left over. She can also share them equally… | Make up your own riddle: "I am a 2-digit number in the ___ times table …" Write 2 or 3 clues (about odd or even, the digits, being between two numbers). Check that only ONE number fits, by listing the table. Swap with a partner. | Challenge (same tier; content as described above) |

**Workbook (core pages).** No change.

**Slides.** Stretch slide item 1 (old: 7 × 8 or 6 × 9) is now T5 (three pairs, 'what do you notice?'); notes updated. Challenge slide is unchanged (X1, X2).

### Lesson 4: Model Makers

**Tier moves and removals.** Old X1 and X2 (one model plus one step) are no longer in the bank; old X4 and X8 likewise (Think Harder level). Old X7 (ages) moved to X8. X7 is the new posing item.

| Item | Old | New | Tier |
|---|---|---|---|
| C1 | There are 2345 people at a concert. 1180 are adults. How many are children? Draw a part-whole model. | There are 2345 people at a concert. 1180 of them are adults. How many are children? Draw one long bar for all the people and mark off the part for the adults. | Core (same tier; content as described above) |
| C2 | A red ribbon is 145 cm long. A blue ribbon is 68 cm longer. How long is the blue ribbon? | A red ribbon is 145 cm long. A blue ribbon is 68 cm longer. Draw the red ribbon as a bar, then draw a longer bar for the blue ribbon. How long is the blue ribbon? | Core (same tier; content as described above) |
| C3 | Ravi has 512 stamps. Siti has 139 fewer stamps than Ravi. How many stamps do they have altogether? | Ravi has 512 stamps. Siti has 139 fewer stamps than Ravi. Draw a bar for each child. How many stamps does Siti have? How many do they have altogether? | Core (same tier; content as described above) |
| C4 | Ben has 4 times as many cards as Ali. Ali has 23 cards. How many cards does Ben have? How many do they have altogether? | Ali has 23 cards. Ben has 4 times as many cards as Ali. Draw 1 box for Ali and 4 boxes for Ben. How many cards does Ben have? How many do they have altogether? | Core (same tier; content as described above) |
| C6 | A pen costs $3. A bag costs 5 times as much as the pen. How much more does the bag cost than the pen? | A pen costs $3. A bag costs 5 times as much as the pen. Draw 1 box for the pen and 5 boxes for the bag. How much more does the bag cost than the pen? | Core (same tier; content as described above) |
| X1 | Ali and Ben have 120 stickers altogether. Ali has 3 times as many as Ben. Ali gives 20 stickers to Ben. How many stickers does ea… | Ali and Ben have 120 stickers altogether. Ali has 3 times as many as Ben. Ali gives some stickers to Ben, and then Ali has only twice as many as Ben. How many stickers does Ali give to Ben? | Challenge (same tier; content as described above) |
| X2 | A pencil box and 3 pens cost $25 altogether. The pencil box costs $5 more than one pen. How much does one pen cost? | A pencil box and 3 pens cost $25 altogether. A pencil box and 5 pens cost $35 altogether. How much does one pen cost? How much does the pencil box cost? | Challenge (same tier; content as described above) |
| X4 | Siti has 4 times as many beads as Mei. If Siti gives Mei 30 beads, they will have the same number. How many beads do they have al… | Ravi, Mei and Siti have 160 beads altogether. Mei has 3 times as many beads as Siti. Ravi has 20 more beads than Mei. How many beads does each child have? | Challenge (same tier; content as described above) |
| X7 | Ravi is 7 years old and his sister is 3. In how many years will their ages add up to 30? | Make up your own before-and-after story about stickers or money, where one child gives some to another child. Draw its model, solve it and check it. Then change ONE number in your story. What changes in the answer, and what stays the same? Swap with a partner. | Challenge (same tier; content as described above) |
| X8 | A pen costs $3 more than a ruler. Mei buys 2 pens and 2 rulers for $18. How much does one pen cost? | Ravi is 7 years old and his sister is 3. In how many years will their ages add up to 30? Explain how you know. | Challenge (same tier; content as described above) |

**Workbook (core pages).** Q3: 'Each box in the picture is 1 unit (one equal part).' added. Q4 and Q5: one-line guess-and-check hints added; the two 'draw your model' boxes shortened (120 and 110 to 100 px) to keep the page.

**Slides.** Challenge, see-it and walk-through slides rebuilt for the new X1 (before and after bars, ratio changes from 3:1 to 2:1) and X2 (two bills, new SVG). Stretch slide unchanged (T4, T7, T8).

### Lesson 5: Remainder Riddles

**Tier moves and removals.** Old X7 (answer equals remainder) moved to X3; old X3 (MATH letters) removed (a repeat of T6). X7 is the new posing item.

| Item | Old | New | Tier |
|---|---|---|---|
| C1 | Work out 35 ÷ 4. Write the answer and the remainder. | Share 35 counters equally among 4 children. How many counters does each child get? How many counters are left over? (Use counters or draw dots in 4 groups.) | Core (same tier; content as described above) |
| C2 | Work out 58 ÷ 7. Write the answer and the remainder. | Put 58 sweets into bags with 7 sweets in each bag. How many full bags can you fill? How many sweets are left over? (Use counters or draw dots.) | Core (same tier; content as described above) |
| T8 | A pen costs $4. Ravi has $35. How many pens can he buy? How much more money does he need to buy one more pen? | Mei has 29 beads. She puts them into bags of 4. Then she tips them out and puts them into bags of 5. Then into bags of 6. Each time she writes how many beads are left over. Which bag size leaves the most beads over? Which leaves the fewest? | Think Harder (same tier; content as described above) |
| X3 | The letters M A T H M A T H M A T H … go on and on. What is the 75th letter? | A number is divided by 6. The answer and the remainder are the same number, and it is not 0. Find all the numbers it could be. | Challenge (same tier; content as described above) |
| X7 | A number is divided by 6. The answer and the remainder are the same number, and it is not 0. Find all the numbers it could be. | Make up your own remainder riddle: "I am a number between ___ and ___. When I am divided by ___ the remainder is ___. When I am divided by ___ the remainder is ___." Check that only ONE number fits, by listing the numbers for the first clue and testing them. Swap with a partner. | Challenge (same tier; content as described above) |
| X8 | Today is Monday. What day of the week will it be 100 days from today? | Today is Monday. What day of the week will it be 100 days from today? What day of the week was it 100 days ago? Explain how you know. | Challenge (same tier; content as described above) |

**Workbook (core pages).** Q5(a): hint added (share 9, 10, 11 … counters into groups of 8).

**Slides.** Challenge slide item 1 now also asks 'What day of the week was it 100 days ago?'; the see-it, walk-through and notes follow. Stretch slide unchanged (its three items are not in the bank).

### Lesson 6: Fraction Walls

**Tier moves and removals.** Old X7 (equal to 2/3, bottom 4 more than top) moved to X5. Old X4 (ribbon), X5 (twelfths again) and X9 (juice) removed. X7 is the new posing item.

| Item | Old | New | Tier |
|---|---|---|---|
| C1 | Fill in the box: 1/2 = ?/10 | A chocolate bar has 10 equal pieces. Ali eats half of the bar. How many pieces is that? Write it as 1/2 = ?/10. (Draw the bar and cut it in two halves if you like.) | Core (same tier; content as described above) |
| C2 | Which is bigger: 1/6 or 1/9? | Two pizzas are the same size. One is cut into 6 equal slices and the other into 9 equal slices. Which pizza has the bigger slices? So which is bigger, 1/6 of a pizza or 1/9 of a pizza? | Core (same tier; content as described above) |
| C3 | Work out 2/9 + 5/9. | A bar is cut into 9 equal parts. Shade 2 parts. Then shade 5 more parts. What fraction of the bar is shaded now? | Core (same tier; content as described above) |
| C4 | Work out 1 − 3/8. | A bar is cut into 8 equal parts and 3 parts are shaded. What fraction of the bar is NOT shaded? (Draw it and count.) | Core (same tier; content as described above) |
| C6 | Fill in the box: 2/5 = ?/10 | A bar is cut into 5 equal parts and 2 parts are shaded (2/5). Now cut every part into 2 equal pieces. How many small pieces are shaded now, out of how many pieces? Write it as 2/5 = ?/10. | Core (same tier; content as described above) |
| T4 | Write two fractions equal to 4/6: one with a smaller bottom number and one with a bigger bottom number. | Write three different fractions that are all equal to 2/3, each with a different bottom number. How do you know they are equal? | Think Harder (same tier; content as described above) |
| X4 | A ribbon is cut into equal pieces. Ali takes 1/3 of the ribbon and Ben takes 1/6 of it. Mei takes the rest. Who has the most ribb… | Two fractions both have 12 as the bottom number. Together they make 5/6. One of them is 1/6 more than the other. What are the two fractions? | Challenge (same tier; content as described above) |
| X5 | Find all the fractions with bottom number 12 that are bigger than 2/3 but smaller than 1. | A fraction is equal to 2/3. Its bottom number is 4 more than its top number. What is the fraction? | Challenge (same tier; content as described above) |
| X7 | A fraction is equal to 2/3. Its bottom number is 4 more than its top number. What is the fraction? | Make up your own "What fraction am I?" riddle, like: "I am equal to 3/4. My top and bottom numbers add up to ___." Choose the number so that exactly ONE fraction fits. Check it, then swap with a partner. Is your riddle always going to work for any number you choose? Explain. | Challenge (same tier; content as described above) |
| X9 | Siti and Ravi each have the same size bottle of juice. Siti drinks 2/3 of her bottle. Ravi drinks 7/12 of his. Who drinks more? H… | Find a fraction that is bigger than 2/3 but smaller than 3/4. Hint: the fraction wall has no row that helps, so cut every part into smaller equal parts. Can you find another one? | Challenge (same tier; content as described above) |

**Workbook (core pages).** Q7 is now '(if time)' with the hint 'look at the twelfths row of your wall'; the deck's ws2 preview matches.

**Slides.** Challenge slide item 2 (juice) replaced by 'a fraction between 2/3 and 3/4'; see-it SVG, walk-through and notes follow. Stretch slide unchanged.

### Lesson 7: Area Architects

**Tier moves and removals.** Old X1, X5, X6, X7 are replaced by four new items (see table). X7 is the new posing item.

| Item | Old | New | Tier |
|---|---|---|---|
| C1 | Find the perimeter of a rectangle 9 cm long and 4 cm wide. | A rectangle is 9 cm long and 4 cm wide. Walk all the way round its edge: how far is that? (This distance is called the perimeter.) Draw it on squared paper if you like. | Core (same tier; content as described above) |
| C2 | Find the area of a rectangle 7 cm long and 6 cm wide. | Cover a rectangle 7 cm long and 6 cm wide with squares that are 1 cm by 1 cm. There are 6 rows with 7 squares in each row. How many squares cover it? (The number of squares is the area, in cm².) | Core (same tier; content as described above) |
| C3 | A square has a perimeter of 32 cm. How long is each side? | A square has 4 equal sides. The distance all the way round it is 32 cm. How long is each side? | Core (same tier; content as described above) |
| C4 | A square has an area of 36 cm². What is its perimeter? | A square floor is covered with 36 small squares (1 cm by 1 cm), with the same number of squares in each row and each column. How many squares are there along one side? How far is it all the way round the edge? | Core (same tier; content as described above) |
| C5 | A rectangle has an area of 40 cm². Its length is 8 cm. Find its breadth and its perimeter. | A rectangle is covered by 40 small squares (1 cm by 1 cm), with 8 squares in each row. How many rows are there? How far is it all the way round the edge? | Core (same tier; content as described above) |
| X1 | Find all the rectangles with whole-cm sides and a perimeter of 24 cm. Which has the biggest area? | List every rectangle with whole-cm sides and a perimeter of 24 cm, with its area, in a table. What do you notice as the rectangle gets closer to a square? Use what you notice to predict the biggest area for a perimeter of 40 cm, then check. | Challenge (same tier; content as described above) |
| X5 | Each small square is 1 cm by 1 cm. Draw a figure of 7 squares with a perimeter of 12 cm, and another with a perimeter of 16 cm. | A rectangle is 10 m long and 8 m wide. A 4 m by 3 m rectangle is cut out of one corner. Find the area and the perimeter that are left. Then cut the same 4 m by 3 m rectangle out of the MIDDLE of one long side instead. Find the new area and perimeter. What stays the same and what changes? | Challenge (same tier; content as described above) |
| X6 | The area of a rectangle is 36 cm². Its length is 4 times its breadth. Find its perimeter. | A square with sides of 8 cm is cut into four same-size squares. The four small squares are put in a row, touching whole sides. Find the perimeter of the row. Then compare with the perimeter of the big square and with the area of each shape. What stays the same and what changes? | Challenge (same tier; content as described above) |
| X7 | A rectangle is made of 3 same-size squares in a row. Its perimeter is 32 cm. What is its area? | Make up your own rectangle puzzle. Choose a rectangle with whole-cm sides, then give a partner only TWO clues about it (for example its area and its perimeter). Check that only ONE rectangle fits both clues. Which two clues did you choose, and why do they work? | Challenge (same tier; content as described above) |

**Workbook (core pages).** Q3 and Q4: one-line hints added ('first walk round the rectangle'; 'you can cut the figure into two rectangles').

**Slides.** No slide change (Challenge slide uses X8 and X9, unchanged; the three Stretch slide items are not in the bank).

### Lesson 8: Angle and Line Detectives

**Tier moves and removals.** Old X7 (4-sided shape with 3 right angles) moved to X4. Old X2, X4, X5 removed or replaced. X7 is the new posing item.

| Item | Old | New | Tier |
|---|---|---|---|
| C1 | How many right angles does a rectangle have? | A right angle is a square corner, like the corner of a page. How many right angles does a rectangle have? Check with the corner of a piece of paper. | Core (same tier; content as described above) |
| C2 | At 3 o’clock, what angle do the hands of a clock make? | At 3 o’clock the minute hand points at 12 and the hour hand points at 3. Is the angle between the hands smaller than, bigger than, or the same as the corner of a page? | Core (same tier; content as described above) |
| C3 | At 2 o’clock, is the angle between the clock hands smaller or bigger than a right angle? | At 2 o’clock, is the angle between the clock hands smaller or bigger than the corner of a page? | Core (same tier; content as described above) |
| C4 | Name 2 capital letters that have a pair of parallel lines. | Parallel lines are straight lines that stay the same distance apart and never meet, like the two rails of a train track. Name 2 capital letters that have a pair of parallel lines. | Core (same tier; content as described above) |
| C5 | Two straight lines cross like a plus sign (+). How many right angles do they make? | Two straight lines cross like a plus sign (+). Each square corner where they cross is a right angle. How many right angles do they make? | Core (same tier; content as described above) |
| C6 | 3 lines go out from one point, spread out like a fan. How many angles can you find? | 3 lines go out from one point, spread out like a fan. An angle is the space between two lines. How many different angles can you find? (Draw it and count.) | Core (same tier; content as described above) |
| T3 | At which o’clock times do the hands of a clock make a right angle? | Look at a clock face. For each o’clock time from 1 o’clock to 11 o’clock, is the angle between the hands (the short way round) smaller than, the same as, or bigger than a right angle? Put each time in the right group. | Think Harder (same tier; content as described above) |
| T8 | How many pairs of parallel lines does a rectangle have? How many pairs of perpendicular lines? | The letter H is made of 3 straight lines: 2 upright lines and 1 line across. List every pair of lines. Which pairs are parallel and which pairs are perpendicular? | Think Harder (same tier; content as described above) |
| X2 | The minute hand turns from 12 to 3. How many right angles has it turned through? From 12 to 9 (going clockwise)? | A staircase is made of columns of 1, 2 and 3 squares standing side by side (3 steps). It has 6 right angles inside it. How many right angles are inside a staircase with 4 steps? With 5 steps? With 10 steps? Find a rule and explain why it works. | Challenge (same tier; content as described above) |
| X4 | How many right angles are there in the letter F (3 straight lines)? | A 4-sided shape has 3 right angles. Draw it. Test the 4th angle with your checker. Can a 5-sided shape have exactly 3 right angles? Draw one. | Challenge (same tier; content as described above) |
| X5 | The letter E is made of 4 lines. List every pair of lines. How many pairs are there altogether? | Mei says: "Perpendicular lines must be one going straight up and one going straight across." Is she right? On a square grid, draw two perpendicular lines that are both slanted. Check with your checker. How do you know they are perpendicular? | Challenge (same tier; content as described above) |
| X7 | A 4-sided shape has 3 right angles. Draw it. Test the 4th angle with your checker. Can a 5-sided shape have exactly 3 right angle… | Make up your own "Which shape am I?" riddle about a shape on square grid paper. Use words like sides, right angles, parallel and perpendicular, and give 3 clues. Draw the answer. Then check: can a partner draw a DIFFERENT shape that fits your clues? If yes, add a clue. | Challenge (same tier; content as described above) |

**Workbook (core pages).** Q4: the definitions of parallel and perpendicular lines were added to the question stem.

**Slides.** Stretch slide item 3 (old: the 5-line fan) is now 'the letter H: list every pair'; notes updated.

### Lesson 9: Measure and Money Masters

**Tier moves and removals.** Old X9 (clock 10 minutes fast) moved to X3. Old X3 (erasers) removed. X9 is the new posing item (placed at X9 because the Challenge slide shows X7 and X8).

| Item | Old | New | Tier |
|---|---|---|---|
| C1 | 2 m 45 cm = ____ cm | A ribbon is 2 m 45 cm long. (1 m is 100 cm.) How many cm is the ribbon? | Core (same tier; content as described above) |
| C2 | 3060 g = ____ kg ____ g | A bag of rice weighs 3060 g. (1 kg is 1000 g.) Write its mass in kg and g. | Core (same tier; content as described above) |
| C3 | A pail holds 4 ℓ 500 ml. A jug holds 1 ℓ 750 ml. How much more does the pail hold? | A pail holds 4 ℓ 500 ml. A jug holds 1 ℓ 750 ml. (1 ℓ is 1000 ml.) How much more does the pail hold? Hint: write both in ml first. | Core (same tier; content as described above) |
| C5 | Write 6:20 p.m. in 24-hour time. | It is 6:20 p.m. Write the time in 24-hour time. (After 12 noon, add 12 to the hour.) | Core (same tier; content as described above) |
| C6 | A lesson starts at 10:45 a.m. and ends at 12:05 p.m. How long is it? | A lesson starts at 10:45 a.m. and ends at 12:05 p.m. How long is it? Hint: draw a time line and jump to 11:00, then 12:00, then 12:05. | Core (same tier; content as described above) |
| X3 | Ravi has $10. He buys some erasers at 85¢ each and gets $1.50 change. How many erasers does he buy? | The clock at the station is 10 minutes fast. The train leaves when this clock shows 13:05. The trip takes 1 h 40 min. What is the real (correct) time when the train arrives? Give it in 24-hour and 12-hour time. | Challenge (same tier; content as described above) |
| X9 | The clock at the station is 10 minutes fast. The train leaves when this clock shows 13:05. The trip takes 1 h 40 min. What is the… | Make up your own problem about money or time that needs at least 2 steps. Write it, solve it and check it. Then change ONE number and solve it again. What changes in the answer, and why? Swap with a partner. | Challenge (same tier; content as described above) |

**Workbook (core pages).** No change (the unit relations are already printed in the page header of the worksheet).

**Slides.** No slide change (slide items are T6, T7, T8, X7, X8; the Challenge slide is unchanged).

### Lesson 10: Challenge Day

**Tier moves and removals.** Old X7 (kueh truth-teller) moved to X4. Old X1, X5, X6 and the 2-digit-numbers list were replaced. X7 is the new posing item.

| Item | Old | New | Tier |
|---|---|---|---|
| C1 | Mei is 5th from the front and 4th from the back of a queue. How many people are in the queue? | Mei is 5th from the front and 4th from the back of a queue. Draw circles for the children in the queue. How many children are in the queue? | Core (same tier; content as described above) |
| C2 | Two numbers add up to 50. One number is 12 more than the other. What are the numbers? | Two numbers add up to 50. One number is 12 more than the other. Guess a pair, check it, and improve your guess. What are the two numbers? | Core (same tier; content as described above) |
| T1 | In a queue, there are 4 people in front of Ravi and 7 people behind him. How many people are in the queue? | Ali has three coins: 10¢, 20¢ and 50¢. He picks one coin, or two coins, or all three. List every different amount of money he can make, in order. How many amounts are there? | Think Harder (same tier; content as described above) |
| X1 | Mei, Ali and Ravi have 90 stickers altogether. Ali has 10 more than Mei. Ravi has 5 fewer than Ali. How many stickers does each c… | Ben is 3rd from the front and 5th from the back of a queue, so there are 7 children. Add the two numbers: what do you get? Does this always work? Mei is 6th from the front in a queue of 15. Where is she from the back? Write a rule that links "from the front", "from the back" and "how many in the queue". | Challenge (same tier; content as described above) |
| X4 | How many 2-digit numbers have digits that add up to 9? | One of Ali, Ben and Mei ate the last kueh. Ali says, “Ben ate it.” Ben says, “I did not eat it.” Mei says, “I did not eat it.” Only ONE of them is telling the truth. Who ate the kueh? | Challenge (same tier; content as described above) |
| X5 | A bar graph shows the books 4 children read. Ali’s and Ben’s bars are the same height. Mei read 3 more than Ali. Siti read 2 fewe… | Ali, Ben, Mei and Siti read 8, 11, 13 and 15 books (each child a different number). Mei read the most. Siti read more than Ben. Ali read 2 fewer books than Siti. How many books did each child read? Then draw the bar graph. | Challenge (same tier; content as described above) |
| X6 | Siti has 8 coins. They are all 10¢ and 50¢ coins, worth $2 altogether. How many of each coin does she have? | Squares are built from sticks. Figure 1 is 1 square (4 sticks). Figure 2 is a 2 by 2 block of 4 squares (12 sticks). Figure 3 is a 3 by 3 block of 9 squares (24 sticks). How many sticks does Figure 4 need? Make a table and look at the jumps. How many sticks does Figure 10 need? | Challenge (same tier; content as described above) |
| X7 | One of Ali, Ben and Mei ate the last kueh. Ali says, “Ben ate it.” Ben says, “I did not eat it.” Mei says, “I did not eat it.” On… | Make up your own logic puzzle with 3 people and 3 things (colours, pets or sports). Write 3 or 4 clues. Test it on a partner: does it have exactly ONE answer? Is there a clue you could take away and still have only one answer? | Challenge (same tier; content as described above) |

**Workbook (core pages).** No change.

**Slides.** No slide change (slide Think Harder items T5-T7 and Challenge X8, X9 unchanged).

## Regenerated decks and keys

All ten decks were regenerated (`python3 rebuild/gen_p3lK.py`, then `python3 levels/restyle.py split/p3lK`) and re-previewed with `rebuild/preview.py`: no OVERFLOW on any slide, slide counts unchanged (27, 26, 26, 26, 26, 26, 25, 25, 26, 27). Slide answers live in the speaker notes; they were updated wherever a slide item changed (Lessons 2, 3, 4, 5, 6, 8). The workbook keys in `lesson.key` did not change because no worksheet answer changed (workbook edits are hints, definitions and star labels). Tutor guide Think Harder tables, the Question Bank, the Weekly Dose of Thinking Math and the weekly packs are all generated from `qbank`, so they match.

## Final page counts

| File | Before | After |
|---|---|---|
| Student workbook (`p3/Math_Inquirers_P3_Student_Workbook_Designed.pdf`) | 48 | **48** (every lesson still 2 core pages + 2 Think Harder pages; lesson headers on pages 3, 5, 7 … 41) |
| Tutor guide PDF | 60 | **60** (61 on the first build; the Lesson 5 posing answer was shortened to remove a one-line spill) |
| Weekly Dose of Thinking Math | 25 | **25** |
| Weekly PDFs zip | 10 files | 10 files (student pages by week 14 / 8 / 8 / 8 / 9) |
| Question Bank (`outputs/designed`) | 21 | **28** (Core items now carry scaffolds, and each lesson has a posing item with a model answer; most lessons now spill a few lines onto a second page, answer key 6 to 7 pages) |
| Weekly Email Pack / Free Taster / What Learners Get | 12 / 5 / 1 | 12 / 5 / 1 |
| Scheme of work PDF | 2 | 2 |

The Question Bank growth is the one count that moved. Trimming it back would mean dropping the scaffolds this rework added, so it was left; if a 21-page bank matters, the layout in `levels/mkextras.py` (shared, so not touched here) would have to change.

## Verification

Every new or changed numeric answer and every "find all / only one" claim in new items was checked in Python with exact arithmetic (`fractions.Fraction`, brute force over all candidates): 48 checks, 0 failed. Highlights: L1 digit-sum counts 1, 3, 6, 10, 15 (35 numbers for digit sum 5) and the posing example 4326 as the only number fitting four clues; L2 shape sum has the single solution (1, 9, 8) and the posing example has the unique solution 3517 + 2486 = 6003; L3 91 is the only odd 2-digit multiple of 7 with digit sum 10; L4 ratio change 30 to 40 (Ali gives 10), two bills (pen $5, box $10), three children 20 / 60 / 80; L5 remainder example gives 22 only on 20 to 50 (and 22, 52 on 20 to 60) and Monday + 100 days is Wednesday, Monday − 100 days is Saturday (checked with `datetime`); L6 fractions between 2/3 and 3/4 (17/24, 25/36), 6/12 and 4/12; L7 corner cut area 68 and perimeter 36, notch area 68 and perimeter 42, row of four 4 cm squares perimeter 40 (checked by cell-set perimeter code); L8 staircase right angles = steps + 3 for 3, 4, 5, 10 steps; L9 posing example money; L10 seven coin amounts, 18 rectangles in a 2 by 3 grid (item dropped, check kept), the unique book assignment and the unique logic-puzzle example, sticks 4, 12, 24, 40 … 220, and the kueh truth-teller (only Mei).

## Known limits

- Compliance after the rework (100%) is my own re-audit with the same test. A reader may still judge a few scaffolded Core items (for example Lesson 6 C1, C6 and Lesson 7 C5) as only partly low-floor.
- Star ("if time") worksheet parts remain Think Harder level; they are optional and labelled. Lesson 8 Q5(c) was already labelled.
- Slide-only Think Harder items (Lessons 5, 6, 7) were audited and judged compliant, so they were not changed.
- Criterion 9 (problem posing) is one prompt per lesson: still "occasional" on the rubric. Criteria 10 and 11 (reflection, compacting) are not addressed by this rework.
