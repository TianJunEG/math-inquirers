"""Item data for levels/gap_slides.py: ORIGINAL slide-only additions for the HOLIDAY decks, Levels 4-6 (GAPS-SLIDES-NOW).
No printed workbook, print file or content/*.js is touched. Every item: lv, ln (lesson), kind, skill, tool (one of the 8 strategy names in levels/spine.json),
q (question lines; '(a) ' starts a part), ans (lines shown on the answer click), say / ask / listen (tutor notes), why (worked reasoning for the tutor),
var (optional same-skill variant with its answer), fig (optional drawn figure). Answers are checked by levels/gap_verify.py with independent code.
Wording follows term/l1/WORDING_GUIDE.md scaled to the level (numerals, fixed command words, 'Find', 'How many ... altogether', no teaching inside the question)."""
TOOLS = ['Spot the pattern', 'List every way', 'Draw it', 'Make a table', 'Work backwards', 'Guess and check', 'Try something simpler', 'Act it out']
TH, GF = 'Think harder', 'Go further'
ITEMS = []
def I(id, lv, ln, kind, skill, tool, q, ans, say, ask, listen, why, var=None, fig=None, preview=False):
    assert tool in TOOLS, tool
    it = dict(id=id, lv=lv, ln=ln, kind=kind, skill=skill, tool=tool, q=q, ans=ans, say=say, ask=ask, listen=listen, why=why)
    if var: it['var'] = var
    if fig: it['fig'] = fig
    if preview: it['preview'] = True
    ITEMS.append(it)

# =============================================================== LEVEL 4
I('digit', 4, 1, TH, 'Digit tests for 3 and 6', 'Spot the pattern',
  ['(a) Add the digits of each number. Which of 724 and 618 is a multiple of 3?',
   'A number in the 2 table and in the 3 table is also in the 6 table.',
   '(b) The 3-digit number 58[ ] is a multiple of 6. Which digits can go in the box? Write every answer.'],
  ['(a) 724: digit sum 13, no. 618: digit sum 15, yes.', '(b) The box can be 2 or 8: 582 and 588.'],
  'Look at a multiple of 3 such as 51, 63, 84. Add their digits. What do you notice? Then try 724 and 618.',
  'If a number is in both the 2 table and the 3 table, what must be true about its last digit and its digit sum?',
  'The digit sum of a multiple of 3 is a multiple of 3. Even last digit AND digit sum in the 3 table. Children who test all 10 digits are fine, but ask them to find a faster way.',
  '5 + 8 = 13, so the box digit must make 13 + box a multiple of 3: box = 2, 5 or 8. The number must also be even, so the box is 2 or 8. 582 = 6 x 97 and 588 = 6 x 98.',
  var=('The 3-digit number 73[ ] is a multiple of 6. Which digits can go in the box?', '732 and 738 (box 2 or 8).'))

I('weekday', 4, 1, TH, 'Weekdays and remainders', 'Make a table',
  ['(a) Ben borrows a library book on a Monday. It is due back 45 days later. On which day of the week is it due?',
   '(b) Kumar starts a trip on a Saturday. Which day of the week is it 30 days later?'],
  ['(a) Thursday.', '(b) Monday.'],
  'A week has 7 days, so the days repeat in a cycle of 7. Write the days across the top of a table, then jump 7 days at a time.',
  'How many whole weeks are in 45 days? What is left over, and what does the leftover tell us?',
  '45 = 6 x 7 + 3, so it is the same as 3 days later. This is the remainder move from today\'s lesson. Listen for "divide by 7 and look at the remainder".',
  '45 days = 6 weeks and 3 days: Monday plus 3 days is Thursday. 30 days = 4 weeks and 2 days: Saturday plus 2 days is Monday.',
  var=('Siti starts swimming lessons on a Tuesday. Which day of the week is it 100 days later?', 'Thursday (100 = 14 weeks and 2 days).'))

I('cr1', 4, 2, TH, 'Letter sums', 'Guess and check',
  ['Each letter stands for one digit. Different letters stand for different digits. A letter at the start of a number is not 0.', 'Find P, Q, R and S.'],
  ['P = 5, Q = 1, R = 9, S = 0.  Check: 51 + 59 = 110.'],
  'Two 2-digit numbers cannot add to more than 198. So what can the first digit of the answer be?',
  'Which letter is that digit? What does the tens column then tell you about P?',
  'Q = 1 from the size of the sum, then 2 x P + carry gives a number ending in 1 with a carry, so P = 5. Children who guess P first and test it are using Guess and check well.',
  'The answer has 3 digits, so its first digit is 1 and Q = 1. The tens column gives P + P + carry = 11, so P = 5 and the carry is 1. The ones column gives Q + R = 10 + S, so 1 + R = 10 + S: R = 9 and S = 0.',
  var=('Each letter is a different digit. TT + UT = TVW. Find T, U, V and W.', 'T = 1, U = 9, V = 0, W = 2 (11 + 91 = 102).'),
  fig=('sum', 'PQ', 'PR', 'QQS'))

I('cr2', 4, 2, GF, 'Letter sums, a longer one', 'Guess and check',
  ['Each letter stands for one digit. Different letters stand for different digits. A letter at the start of a number is not 0.', 'Find D, A, E, C and B.'],
  ['D = 8, A = 3, E = 1, C = 4, B = 0.  Check: 883 + 148 = 1031.'],
  'Two 3-digit numbers add to a 4-digit number. What is the biggest the first digit of the answer can be? Start there.',
  'Which letter is the answer\'s first digit, and what must the hundreds column be to make it?',
  'E = 1 first. Then children list possibilities for the hundreds column (D + E + carry) and test with the other columns. A table with one column per letter helps.',
  'E = 1 because 999 + 999 = 1998. Hundreds: D + E + carry makes a number with tens digit B and carry 1, so D + 1 + carry is 10 or more: D = 8 with carry 1 gives 10, so B = 0. The tens column D + C + carry = A + 10 and the ones A + D = E + 10 give A = 3 (3 + 8 = 11) and C = 4.',
  fig=('sum', 'DDA', 'ECD', 'EBAE'))

I('pair', 4, 3, GF, 'Adding a list by pairing', 'Try something simpler',
  ['Here is a list: 11, 14, 17, 20, ... , 41. The numbers go up by 3 each time.',
   '(a) How many numbers are in the list?', '(b) Find the sum of all the numbers.'],
  ['(a) 11 numbers.', '(b) 286.'],
  'Try something simpler: write the first and last number. Add them. Then the second and the second last. What do you see?',
  'What is the same about every pair? How many pairs are there, and what is left over in the middle?',
  'Every pair adds to 52 (11 + 41, 14 + 38, ...). 5 pairs and a middle number 26. Listen for "first plus last, second plus second last".',
  '(41 - 11) / 3 + 1 = 11 numbers. Five pairs of 52 make 260 and the middle number is 26, so the sum is 286. Check: 11 x 52 / 2 = 286.',
  var=('Find the sum of 5, 9, 13, ... , 49.', '324 (12 numbers, 6 pairs of 54).'))

I('gap', 4, 3, TH, 'Gaps that grow', 'Make a table',
  ['Ravi saves coins in a jar. Day 1: 3 coins in the jar. Day 2: 5. Day 3: 8. Day 4: 12. Day 5: 17.',
   'The number he adds goes up by 1 each day.', '(a) How many coins are in the jar on Day 6?', '(b) How many coins are in the jar on Day 10?'],
  ['(a) 23 coins.', '(b) 57 coins.'],
  'Make a table with three columns: the day, the number of coins, and the gap from the day before.',
  'What is the gap on Day 2? On Day 3? What will the gap be on Day 6?',
  'Gaps 2, 3, 4, 5, then 6, 7, 8, 9, 10. Listen for "the gap goes up by 1" and a table that keeps going without skipping a row.',
  'Gaps are 2, 3, 4, 5, so Day 6 adds 6: 23. Then +7 = 30, +8 = 38, +9 = 47, +10 = 57 on Day 10.',
  var=('Mei folds paper stars. Day 1: 4, Day 2: 6, Day 3: 9, Day 4: 13. The number added goes up by 1 each day. How many on Day 8?', '39 (the days go 4, 6, 9, 13, 18, 24, 31, 39).'),
  fig=('table', ['Day', 'Coins', 'Gap'], [[1, 3, ''], [2, 5, 2], [3, 8, 3], [4, 12, 4], [5, 17, 5], [6, '?', '?']], 'Table of days, coins and gaps', [110, 140, 110]))

I('fan', 4, 6, GF, 'Triangles by size', 'List every way',
  ['The top point is joined to 4 points on the base line.', '(a) Count the triangles with 1 small triangle inside, with 2, and with 3.', '(b) How many triangles are there altogether?'],
  ['(a) 3 triangles of size 1, 2 of size 2, 1 of size 3.', '(b) 6 triangles altogether.'],
  'Name the base points B, C, D, E. A triangle needs the top point and two base points. List the pairs in order.',
  'How do you know you have not missed one or counted one twice?',
  'An ordered list BC, BD, BE, CD, CE, DE, or a count by size 1, 2, 3. Listen for a rule such as "choose 2 base points".',
  'Pairs of base points: BC, BD, BE, CD, CE, DE gives 6. By size: 3 + 2 + 1 = 6.',
  var=('The top point is joined to 5 points on the base line. How many triangles?', '10 (4 + 3 + 2 + 1).'),
  fig=('fan', 4))

I('spin', 4, 9, TH, 'Spinners with unequal parts', 'Draw it',
  ['A spinner is split into 3 parts. Yellow takes 1/2 of the circle. Green takes 1/3 of the circle. Blue is the rest.',
   '(a) What fraction of the circle is blue?', '(b) Which colour is the spinner most likely to stop on?', '(c) Mei spins 60 times. About how many times should she expect yellow?'],
  ['(a) 1/6.', '(b) Yellow.', '(c) About 30 times (green about 20, blue about 10).'],
  'The picture is a fair way to see the parts of one whole circle. Think of the whole as 6 equal slices.',
  'How many slices is yellow? Green? How many are left for blue?',
  'Common denominator 6: 3/6, 2/6, 1/6. Listen for "more of the circle means more likely". For (c) accept "about", never "exactly".',
  '1/2 = 3/6 and 1/3 = 2/6, so blue is 1/6. Yellow has the biggest part. 1/2 of 60 = 30, 1/3 of 60 = 20, 1/6 of 60 = 10.',
  fig=('pie', [(0.5, '#FFC93C'), (1 / 3, '#7FC8A9'), (1 / 6, '#8EC5F0')], 'A circle split into three parts: half, a third and a sixth'))

I('time', 4, 10, TH, 'A timetable: try both orders', 'List every way',
  ['Kumar leaves home at 2:40 pm. He must go to the post office and the library, in either order, and then walk home. He stays 10 minutes at each place.',
   'The post office closes at 3:30 pm. The library opens at 3:10 pm. Walking times: home to post office 20 minutes, home to library 30 minutes, post office to library 15 minutes (each way).',
   '(a) Which place should he visit first?', '(b) At what time does he get home?'],
  ['(a) The post office first.', '(b) 4:05 pm.'],
  'There are only two orders. Try the first order, write the clock times down the page, then try the other order.',
  'In the library-first order, what time does he reach the post office? Does it work?',
  'Library first: arrives 3:10, leaves 3:20, reaches the post office at 3:35, too late. Post office first: 3:00, leaves 3:10, library at 3:25, leaves 3:35, home at 4:05.',
  'Post office first: arrive 3:00, leave 3:10, walk 15 minutes to the library at 3:25 (open), leave 3:35, walk 30 minutes home: 4:05 pm. Library first fails because he arrives at the post office at 3:35.',
  var=('Change the post office closing time to 3:40 pm. Which orders work now, and which gets Kumar home sooner?', 'Both orders work. Post office first gets home at 4:05 pm; library first: library 3:10 to 3:20, post office 3:35 to 3:45, home 4:05 pm. They tie at 4:05 pm.'))

I('dice', 4, 10, TH, 'Smallest and largest totals', 'List every way',
  ['Siti rolls 4 ordinary dice (faces 1 to 6) and adds the 4 scores.',
   '(a) What is the smallest total she can get?', '(b) What is the largest total she can get?', '(c) Which of these totals is impossible: 3, 4, 13, 24, 25?'],
  ['(a) 4.', '(b) 24.', '(c) 3 and 25 are impossible.'],
  'Do not roll anything. Ask what the lowest face and the highest face on one die are, then think about 4 dice.',
  'Can she get every total from 4 to 24? How can you tell?',
  'Smallest 1 + 1 + 1 + 1, largest 6 + 6 + 6 + 6. Listen for "change one die by 1 at a time", which gives every total in between.',
  '4 x 1 = 4 and 4 x 6 = 24. Starting at 4 you can raise one die by 1 at a time up to 24, so every total from 4 to 24 can be made. 3 is below 4 and 25 is above 24.',
  var=('Siti rolls 5 dice. What are the smallest and largest totals?', '5 and 30.'))

I('stages', 4, 10, TH, 'Counting in two stages', 'List every way',
  ['Aisha has 4 tops, 3 skirts and 2 hats. She wears 1 top, 1 skirt and 1 hat.', '(a) How many different outfits can she make?',
   '(b) Her red top does not go with her green skirt. How many outfits can she make now?'],
  ['(a) 24 outfits.', '(b) 22 outfits.'],
  'Draw 4 boxes for the tops. Under each one, show 3 skirts. How many top-and-skirt pairs is that?',
  'How many outfits use the red top with the green skirt? What do you do with that number?',
  '4 x 3 = 12 pairs, times 2 hats = 24. Listen for "multiply the choices". For (b) the red-green pair has 2 outfits (one for each hat); 24 - 2 = 22.',
  '4 x 3 x 2 = 24. The red top with the green skirt can go with either hat, so 2 outfits are removed: 24 - 2 = 22.',
  var=('There are 3 paths from home to the park and 4 paths from the park to school. How many routes from home to school through the park?', '12 routes.'))

# =============================================================== LEVEL 5  (the ratio items r1 to r7 are previews, see docs/sasmo/holiday_slide_additions_L4_6.md)
I('digit', 5, 1, TH, 'Digit sums and the greatest number', 'Guess and check',
  ['Wei has 6 digit cards: 2, 4, 5, 7, 8, 9. He chooses 5 different cards and makes a 5-digit number.',
   '(a) What is the digit sum of all 6 cards?', '(b) Find the greatest 5-digit multiple of 9 that Wei can make.'],
  ['(a) 35.', '(b) 97542.'],
  'A number is a multiple of 9 when its digit sum is in the 9 times table. Wei leaves one card out. Which card must he leave out?',
  'How does the total of 35 help you choose the card to leave out? Why is the answer not 98754?',
  '35 - 8 = 27, so the 8 is left out. Then the digits go in order from the largest: 9, 7, 5, 4, 2. Listen for "test both sides of the target" and a digit sum used as a check.',
  '35 minus the left-out card must be a multiple of 9: 35 - 8 = 27 (35 - 17 would need a card 17). So the cards are 2, 4, 5, 7, 9. Largest first gives 97542. Check: 9 + 7 + 5 + 4 + 2 = 27, and 97542 = 9 x 10838.',
  var=('Siti has cards 1, 3, 4, 6, 8, 9 and chooses 5 of them. Find the greatest 5-digit multiple of 3 she can make.', '98643.'))

I('parity', 5, 1, TH, 'Regroup first, then work out', 'Try something simpler',
  ['(a) Find 8 x 17 x 125. Group the numbers first.', '(b) Do not work out the answers. Which of these are odd?',
   '(i) 3 x 7 x 11 x 5      (ii) 13 x 14 + 15      (iii) 25 + 36 + 47      (iv) 1 001 x 2 002 - 3'],
  ['(a) 17 000.', '(b) (i), (ii) and (iv) are odd. (iii) is even.'],
  'Look for two numbers that make a friendly number. Then say whether each part is odd or even before you add.',
  'Which two numbers in (a) make 1 000? What rule do you use for odd times odd, even times anything, and odd plus even?',
  '8 x 125 = 1 000 first. For (b), listen for "odd x odd is odd", "even x anything is even", "even + odd is odd", "odd + odd is even".',
  '8 x 125 = 1 000, then 1 000 x 17 = 17 000. (i) all odd factors: odd. (ii) 13 x 14 is even, plus 15 is odd. (iii) 25 + 36 is odd, plus 47 is even. (iv) 1 001 x 2 002 is even, minus 3 is odd.',
  var=('Find 4 x 29 x 25. Which of 17 + 18 + 19 and 6 x 15 + 1 is even?', '2 900. Only 17 + 18 + 19 = 54 is even; 6 x 15 + 1 = 91 is odd.'))

I('cr1', 5, 1, TH, 'Letter sums', 'Guess and check',
  ['Each letter stands for one digit. Different letters stand for different digits. A letter at the start of a number is not 0.', 'Find A, B, C, D and E.'],
  ['A = 1, B = 0, C = 8, D = 9, E = 3.  Check: 888 + 131 = 1019.'],
  'Three digits plus three digits make 4 digits. What does that tell you about the first letter of the answer?',
  'Which column will you look at second, and why?',
  'A = 1 from the size of the sum. Then the hundreds column (C + E + carry) gives B and a carry. Accept a table of tries.',
  'The sum is less than 2 000, so A = 1. Ones column: C + A = D (8 + 1 = 9, no carry). Tens column: C + E = 10 + A, so C + E = 11 and the carry is 1. Hundreds column: C + A + 1 = 10 + B, so C = 8 and B = 0, and then E = 3. Check: 888 + 131 = 1019.',
  fig=('sum', 'CCC', 'AEA', 'ABAD'))

I('cr2', 5, 1, GF, 'A multiplication in letters', 'Guess and check',
  ['Each letter stands for one digit. Different letters stand for different digits. A letter at the start of a number is not 0.', 'Find K, M, N and P.'],
  ['K = 8, M = 4, N = 3, P = 6.  Check: 84 x 4 = 336.'],
  'The answer has 3 digits and its first two digits are the same. Make a table: choose M, then try different K. What does 10 x M tell you about the smallest M that can work?',
  'Which values of M can you rule out quickly? How do you know when to stop trying K for one M?',
  'M is at least 2 (a 2-digit number times 1 gives at most 2 digits), and the last digit P comes from M x M. Children list tries such as 14 x 4 = 56, 24 x 4 = 96, ... until the first two digits match. Accept an organised table.',
  'Test M = 4: the products 14 x 4, 24 x 4, ... are 56, 96, 136, 176, 216, 256, 296, 336. 336 has first two digits equal (33), and the number is 84 x 4, so K = 8, M = 4, N = 3, P = 6. No other pair of digits gives a 3-digit answer whose first two digits match and whose letters stand for 4 different digits (this was checked by a script).',
  fig=('sum', 'KM', 'M', 'NNP', '×'))

I('r4', 5, 2, TH, 'Ratio and fractions', 'Draw it',
  ['A bag has red and blue counters in the ratio 3 : 5. This means that for every 3 red counters there are 5 blue counters.',
   '(a) What fraction of the counters are red?', '(b) What fraction of the counters are blue?', '(c) There are 40 counters in the bag. How many are red?'],
  ['(a) 3/8.', '(b) 5/8.', '(c) 15 red counters.'],
  'Draw a bar with 3 units for red and 5 units for blue. The whole bar is the whole bag. How many units are in the whole bar?',
  'What fraction of the whole bar is the red part? How many counters is one unit?',
  '3 + 5 = 8 units, red is 3 of the 8, so 3/8. 40 / 8 = 5 counters per unit, 3 x 5 = 15. Listen for the bar model and for the total as 8 units.',
  'The ratio 3 : 5 gives 8 equal units. Red is 3/8 of the bag and blue is 5/8. 40 / 8 = 5, so red is 3 x 5 = 15 and blue is 5 x 5 = 25.',
  var=('A jug has orange juice and water in the ratio 2 : 7. What fraction of the jug is juice? There are 45 cups of liquid altogether: how many are juice?', '2/9; 10 cups.'),
  fig=('bars', [('Red', [(3, '#F2A0A0', '3')]), ('Blue', [(5, '#8EC5F0', '5')])], 'Bars: red 3 units, blue 5 units'), preview=True)

I('r1', 5, 3, 'Preview', 'What is a ratio?', 'Draw it',
  ['Ali mixes paint. For every 2 tins of blue he uses 3 tins of white. We write blue : white = 2 : 3 and say "2 to 3".',
   'The bar model shows 2 units of blue and 3 units of white. Every unit is the same size.',
   '(a) Ali uses 4 tins of blue. How many tins of white does he use?', '(b) Ali mixes 20 tins altogether in the ratio 2 : 3. How many tins of each colour?'],
  ['(a) 6 tins of white, because 4 : 6 is the same ratio as 2 : 3.', '(b) 5 units altogether. One unit is 20 / 5 = 4 tins. Blue 8 tins, white 12 tins.'],
  'A ratio compares two amounts with "for every". 2 : 3 means 2 blue for every 3 white. Draw the bars first, and call each box a unit.',
  'If Ali doubles the mix, what happens to both numbers? How many units are there in all in (b), and how big is one unit?',
  '2 : 3 = 4 : 6 (multiply both numbers by the same number). For (b): 2 + 3 = 5 units, 20 / 5 = 4 per unit, 2 x 4 = 8 and 3 x 4 = 12. Listen for "units" and "the same size". Do not teach more than this on the first meeting.',
  'Worked example for the tutor. Step 1: read the ratio as "for every": 2 blue for every 3 white. Step 2: draw 2 boxes and 3 boxes, equal size. Step 3: total units = 2 + 3 = 5. Step 4: one unit = 20 / 5 = 4. Step 5: blue = 2 x 4 = 8, white = 3 x 4 = 12. Step 6: check 8 + 12 = 20 and 8 : 12 = 2 : 3.',
  fig=('bars', [('Blue', [(2, '#8EC5F0', '')]), ('White', [(3, '#FFFFFF', '')])], 'Bars: blue 2 units, white 3 units'), preview=True)

I('r2', 5, 3, 'Preview', 'Equal ratios and simplest form', 'Make a table',
  ['A fruit punch uses 6 cups of juice for every 9 cups of water.', '(a) Write the ratio of juice to water.', '(b) Write the ratio in its simplest form.',
   '(c) How many cups of water go with 10 cups of juice?', '(d) Fill in the box: 2 : 3 = 12 : [ ]'],
  ['(a) 6 : 9.', '(b) 2 : 3 (divide both numbers by 3).', '(c) 15 cups of water.', '(d) 18.'],
  'Make a table. Juice in the top row, water in the bottom row. Divide both numbers by 3 to get the smallest whole numbers, then multiply up.',
  'What do you do to both numbers to keep the ratio the same? How do you know 2 : 3 is simplest and cannot go smaller?',
  'The same number on both sides (multiply or divide). Simplest form means no whole number other than 1 divides both. 10 cups of juice is 5 groups of 2, so 5 x 3 = 15.',
  '6 : 9 divided by 3 gives 2 : 3. For 10 cups of juice: 10 = 5 x 2, so water is 5 x 3 = 15. For (d): 12 = 6 x 2, so the box is 6 x 3 = 18.',
  var=('A paint mix is 8 tins of red for every 12 tins of yellow. Write the ratio in simplest form. How many tins of yellow go with 14 tins of red?', '2 : 3; 21 tins.'),
  fig=('table', ['Juice', 'Water'], [[2, 3], [4, 6], [6, 9], [10, '?']], 'Table of equal ratios', [140, 140]), preview=True)

I('r3', 5, 3, 'Preview', 'Sharing in a ratio', 'Draw it',
  ['Mei and Siti share 45 stickers in the ratio 4 : 5. Mei gets the 4 and Siti gets the 5.',
   '(a) How many equal parts are there?', '(b) How many stickers is one part?', '(c) How many stickers does each girl get?', '(d) How many more stickers does Siti get than Mei?'],
  ['(a) 9 parts.', '(b) 5 stickers.', '(c) Mei 20 stickers and Siti 25 stickers.', '(d) 5 more stickers.'],
  'Draw a bar for Mei with 4 boxes and a bar for Siti with 5 boxes, the same size. The 45 stickers fill all the boxes.',
  'How can you check your answer? What do you notice about the difference between the two shares and one part?',
  '4 + 5 = 9 parts, 45 / 9 = 5. Mei 4 x 5 = 20, Siti 5 x 5 = 25, total 45. The difference 5 is 1 part because 5 - 4 = 1. Listen for the check: the two shares add up to 45.',
  'One part is 45 / 9 = 5 stickers. Mei: 4 x 5 = 20. Siti: 5 x 5 = 25. The shares add to 45, and their ratio 20 : 25 is 4 : 5 when both are divided by 5.',
  var=('Ravi and Aisha share 56 marbles in the ratio 3 : 5. How many marbles does each get?', 'Ravi 21 marbles, Aisha 35 marbles.'),
  fig=('bars', [('Mei', [(4, '#FFE08A', '')]), ('Siti', [(5, '#8EC5F0', '')])], 'Bars: Mei 4 parts, Siti 5 parts'), preview=True)

I('dice', 5, 5, GF, 'Dice and hidden faces', 'Act it out',
  ['Three dice are stacked in a tower on a table. On every die, opposite faces add up to 7. The top face of the top die shows 4.',
   'Find the total number of dots on the faces you cannot see: the face on the table and every face where two dice touch.'],
  ['17 dots.'],
  'Take a real die if you have one. Turn it and look: which faces are on opposite sides? What do two opposite faces always add up to?',
  'Which hidden faces form pairs that add up to 7? Which one hidden face is left over?',
  'The top and bottom of the bottom die add to 7. The top and bottom of the middle die add to 7. The bottom of the top die is 7 - 4 = 3. Listen for "pairs of opposite faces".',
  'Hidden faces: the bottom die\'s bottom and top (7), the middle die\'s bottom and top (7), and the top die\'s bottom face (7 - 4 = 3). 7 + 7 + 3 = 17. It does not matter how the lower dice are turned.',
  var=('The top die shows 2 on top. What is the hidden total now?', '19 dots.'),
  fig=('dice', 'Three dice stacked in a tower, the top die showing 4 dots on top'))

I('pack', 5, 6, GF, 'Totals you cannot make', 'Make a table',
  ['Cookies are sold in packs of 5 and packs of 8. Aisha may buy several packs of each kind, or none of one kind.',
   '(a) Which totals from 1 to 20 can she buy?', '(b) Find the greatest total she cannot buy.'],
  ['(a) 5, 8, 10, 13, 15, 16, 18, 20.', '(b) 27.'],
  'Write the numbers 1 to 40 in rows of 5. Mark the multiples of 8 and then everything you can reach by adding 5s.',
  'When you have 5 totals in a row that you can buy, what happens after that? Why?',
  'Five in a row can be bought (28 to 32), so adding 5 reaches every larger total. 27 is the last gap. Listen for the argument "five in a row means all the rest".',
  'Totals are 5a + 8b. The first run of 5 buyable totals in a row is 28, 29, 30, 31, 32 (28 = 5 x 4 + 8, 29 = 5 + 8 x 3, 30 = 5 x 6, 31 = 5 x 3 + 8 x 2, 32 = 8 x 4). Adding 5 to any of them reaches all totals after it, and 27 cannot be made.',
  var=('Stickers come in sheets of 4 and sheets of 7. Find the greatest number of stickers you cannot buy.', '17.'))

I('catch', 5, 6, TH, 'Catching up', 'Make a table',
  ['Ali walks 60 m each minute. Ben starts from the same place 5 minutes later and walks 80 m each minute in the same direction.',
   '(a) How far ahead is Ali when Ben starts?', '(b) How many metres does Ben gain on Ali each minute?', '(c) How many minutes after Ben starts does he catch Ali?'],
  ['(a) 300 m.', '(b) 20 m.', '(c) 15 minutes.'],
  'Make a table with the minutes since Ben started. Write how far each of them has walked, and the gap between them.',
  'What happens to the gap each minute? How can you get from 300 m to no gap without listing every minute?',
  'The gap shrinks by 20 m every minute. 300 / 20 = 15. Listen for "the gap closes by the difference in speeds" (this is a preview of an idea met again in later years).',
  'Ali has walked 60 x 5 = 300 m. Each minute Ben walks 20 m more than Ali, so the gap shrinks by 20 m. 300 / 20 = 15 minutes. Check: Ben walks 80 x 15 = 1 200 m and Ali walks 60 x 20 = 1 200 m.',
  var=('Mei walks 50 m each minute. Kumar starts 4 minutes later and walks 70 m each minute. After how many minutes does Kumar catch Mei?', '10 minutes.'))

I('work', 5, 6, GF, 'Three workers', 'Make a table',
  ['Ali lays 10 bricks each minute and Ben lays 14 bricks each minute. They start together. After 5 minutes Kumar joins them and lays 6 bricks each minute.',
   '(a) How many bricks do Ali and Ben lay in the first 5 minutes?', '(b) They must lay 450 bricks. How many minutes do they work altogether?'],
  ['(a) 120 bricks.', '(b) 16 minutes.'],
  'Make a table with two phases: before Kumar joins, and after. In each phase write how many bricks are laid each minute.',
  'How many bricks are left after the first phase? How many bricks each minute do all three lay together?',
  'Phase 1: 24 bricks each minute for 5 minutes. Phase 2: 30 bricks each minute for the rest. 450 - 120 = 330, 330 / 30 = 11. Listen for the two-phase table.',
  'First 5 minutes: (10 + 14) x 5 = 120. All three lay 10 + 14 + 6 = 30 each minute. 450 - 120 = 330 bricks left, 330 / 30 = 11 minutes. In all 5 + 11 = 16 minutes.',
  var=('Ali lays 8 bricks each minute and Ben lays 12. After 3 minutes Kumar joins and lays 10 bricks each minute. How many minutes do they take to lay 300 bricks?', '11 minutes.'))

I('r5', 5, 6, TH, 'Equal ratios and scaling', 'Make a table',
  ['A rice recipe uses 2 cups of rice for every 5 cups of water. The ratio of rice to water is 2 : 5.',
   '(a) How many cups of water go with 6 cups of rice?', '(b) How many cups of rice go with 25 cups of water?', '(c) Wei uses 12 cups of rice. How many cups of rice and water does he use altogether?'],
  ['(a) 15 cups of water.', '(b) 10 cups of rice.', '(c) 12 + 30 = 42 cups altogether.'],
  'Make a table: each column is the same recipe made again. Multiply both numbers by the same number.',
  'How many times bigger is 6 cups of rice than 2? What do you do to the water? How could you start from the water in (b)?',
  'Scale factor: 6 / 2 = 3, so water 5 x 3 = 15. In (b) 25 / 5 = 5 and rice 2 x 5 = 10. In (c) 12 / 2 = 6, water 5 x 6 = 30. A rate is a ratio in disguise: one number is "for every" the other.',
  'The columns are multiples of the recipe: (2, 5), (4, 10), (6, 15), (8, 20), (10, 25), (12, 30). Altogether for 12 cups of rice: 12 + 30 = 42 cups.',
  var=('A drink uses 3 cups of juice for every 4 cups of water. How many cups of water go with 18 cups of juice?', '24 cups.'),
  fig=('table', ['Rice', 'Water'], [[2, 5], [4, 10], [6, '?'], ['?', 25]], 'Table of equal ratios', [140, 140]), preview=True)

I('r6', 5, 7, TH, 'Ratio and percentage', 'Draw it',
  ['In a class the ratio of boys to girls is 3 : 2.', '(a) What fraction of the class are boys?', '(b) What percentage of the class are girls?', '(c) There are 30 children in the class. How many boys are there?'],
  ['(a) 3/5.', '(b) 40%.', '(c) 18 boys.'],
  'Draw a bar of 5 equal units: 3 for boys and 2 for girls. The whole bar is 100%.',
  'What percentage is one unit? How does that help with the girls?',
  'One unit is 100% / 5 = 20%, so girls are 2 x 20% = 40%. For (c) 30 / 5 = 6 children per unit and 3 x 6 = 18. Listen for "the whole is 5 units".',
  '3 + 2 = 5 units. Boys 3/5, girls 2/5 = 40%. 30 / 5 = 6, so boys 18 and girls 12.',
  var=('The ratio of cats to dogs is 1 : 4. What percentage are cats? There are 60 animals: how many dogs?', '20%; 48 dogs.'),
  fig=('bars', [('Boys', [(3, '#8EC5F0', '')]), ('Girls', [(2, '#F2A0A0', '')])], 'Bars: boys 3 units, girls 2 units'), preview=True)

I('year', 5, 8, TH, 'Weekdays in a year', 'Spot the pattern',
  ['A year has 365 days. In one year, 1 January is a Tuesday.', '(a) How many whole weeks are in 365 days, and how many days are left over?',
   '(b) How many Tuesdays are in the year?', '(c) What day of the week is 31 December?', '(d) What day of the week is 1 January of the next year?'],
  ['(a) 52 weeks and 1 day.', '(b) 53 Tuesdays.', '(c) Tuesday.', '(d) Wednesday.'],
  'Divide 365 by 7. The weeks use up every day of the week 52 times. Which day is the one extra day?',
  'Which day of the week is day 365? Is any other day of the week in the year 53 times?',
  '365 = 52 x 7 + 1. The extra day is the same weekday as 1 January, so only Tuesday occurs 53 times. Listen for the remainder idea.',
  '365 / 7 = 52 remainder 1. The 365th day is 364 days after the first day, and 364 = 52 x 7, so it is also a Tuesday. The next day is a Wednesday.',
  var=('In a 365-day year, 1 January is a Friday. Which weekday occurs 53 times?', 'Friday.'))

I('last', 5, 9, TH, 'Last digits of products', 'Spot the pattern',
  ['(a) Multiply 7 by itself 30 times: 7 x 7 x 7 x ... with 30 sevens. What is the last digit of the answer?',
   '(b) Multiply 4 by itself 25 times. What is the last digit of the answer?'],
  ['(a) 9.', '(b) 4.'],
  'Only the last digit matters, so keep only the last digit each time. Write the last digit after 1 seven, 2 sevens, 3 sevens, 4 sevens, and carry on.',
  'When does the list of last digits start to repeat? How long is the cycle, and where does 30 land in it?',
  'Sevens: 7, 9, 3, 1, then repeats (cycle of 4). 30 = 7 x 4 + 2, so the 2nd in the cycle: 9. Fours: 4, 6, 4, 6 (cycle of 2); 25 is odd, so 4.',
  'Last digits of 7, 7x7, ... are 7, 9, 3, 1, 7, 9, 3, 1, ... 30 mod 4 = 2, so the last digit is 9. Fours: 4, 6, 4, 6, ... 25 is an odd position, so 4.',
  var=('Multiply 2 by itself 22 times. What is the last digit?', '4 (the cycle is 2, 4, 8, 6 and 22 mod 4 = 2).'))

I('range', 5, 9, TH, 'Multiples in a range', 'Try something simpler',
  ['(a) How many multiples of 7 are between 100 and 500?', '(b) How many of them are also multiples of 2?'],
  ['(a) 57 multiples of 7.', '(b) 28 multiples of 14.'],
  'Try something simpler first: how many multiples of 7 are there up to 100? Then up to 500? What do you do with the two answers?',
  'Is 100 a multiple of 7? Is 500? Why does that matter? What number do you test for "multiple of 7 and of 2"?',
  '500 / 7 = 71 remainder 3 gives 71 multiples up to 500; 100 / 7 = 14 remainder 2 gives 14 up to 100. 71 - 14 = 57. In (b) in the 2 table and the 7 table means in the 14 table: 500 / 14 = 35, 100 / 14 = 7, 35 - 7 = 28.',
  'Multiples of 7 up to 500: 71. Up to 100: 14. Neither 100 nor 500 is a multiple of 7, so 71 - 14 = 57. Multiples of 14 up to 500: 35, up to 100: 7, so 28.',
  var=('How many multiples of 9 are between 200 and 700?', '55.'))

I('gaps', 5, 9, TH, 'The gap of the gaps', 'Make a table',
  ['Ravi builds block towers. Tower 1 has 2 blocks, Tower 2 has 3, Tower 3 has 6, Tower 4 has 11 and Tower 5 has 18.',
   '(a) Find the gaps between neighbouring towers. By how much do the gaps go up each time?', '(b) How many blocks are in Tower 8?', '(c) How many blocks are in Tower 10?'],
  ['(a) The gaps are 1, 3, 5, 7. They go up by 2 each time.', '(b) 51 blocks.', '(c) 83 blocks.'],
  'Make a table with 3 columns: the tower number, the blocks, and the gap. Then add a fourth column for the gap of the gaps.',
  'What is the gap going to be between Tower 5 and Tower 6? Between Tower 9 and Tower 10?',
  'Gaps 1, 3, 5, 7, 9, 11, 13, 15, 17. Listen for a table that keeps the pattern going row by row. Early finishers may notice each tower is a square number plus 2.',
  'Tower 6: 18 + 9 = 27. Tower 7: 27 + 11 = 38. Tower 8: 38 + 13 = 51. Tower 9: 51 + 15 = 66. Tower 10: 66 + 17 = 83. Pattern check: Tower n has (n - 1) x (n - 1) + 2 blocks, so Tower 10 is 9 x 9 + 2 = 83.',
  var=('Tower 1 has 1 block, Tower 2 has 2, Tower 3 has 5, Tower 4 has 10. The gaps go up by 2 each time. How many blocks in Tower 7?', '37.'),
  fig=('table', ['Tower', 'Blocks', 'Gap'], [[1, 2, ''], [2, 3, 1], [3, 6, 3], [4, 11, 5], [5, 18, 7], [6, '?', '?']], 'Table of tower number, blocks and gap', [120, 140, 110]))

I('woven', 5, 9, TH, 'Two sequences woven together', 'Spot the pattern',
  ['Mei writes this list: 3, 50, 7, 46, 11, 42, 15, ...', '(a) Write the next 2 numbers.', '(b) What is the 15th number in the list?', '(c) What is the 16th number in the list?'],
  ['(a) 38 and 19.', '(b) 31.', '(c) 22.'],
  'Look at every other number. Underline the 1st, 3rd, 5th, 7th. Then underline the 2nd, 4th, 6th. What is each list doing?',
  'Which list does the 15th number belong to? How many steps from the first number of that list is it?',
  'Odd places: 3, 7, 11, 15 (add 4). Even places: 50, 46, 42 (take away 4). 15th is the 8th odd-place number: 3 + 7 x 4 = 31. 16th is the 8th even-place number: 50 - 7 x 4 = 22.',
  'Odd places go up by 4: 3, 7, 11, 15, 19, ... so the 15th number (the 8th odd-place number) is 3 + 4 x 7 = 31. Even places go down by 4: 50, 46, 42, 38, ... so the 16th number (the 8th even-place number) is 50 - 4 x 7 = 22. The list continues 15, 38, 19, 34, ... so the next two numbers are 38 and 19.',
  var=('Siti writes: 5, 80, 9, 74, 13, 68, ... Find the 12th number.', '50.'))

I('op', 5, 9, TH, 'A rule from examples', 'Make a table',
  ['A machine uses the sign ★ for a rule. 2 ★ 3 = 8, 4 ★ 1 = 8, 5 ★ 2 = 15, 3 ★ 3 = 12.',
   '(a) Find 6 ★ 4.', '(b) Find the number x so that x ★ 3 = 28.'],
  ['(a) 30.', '(b) 7.'],
  'Make a table of the pairs. Look at what happens to the first number in each example. Try a rule, then test it on all four.',
  'Does your rule work for all four examples? Why is one example not enough?',
  'Rule: first number x (second number + 1). Listen for children testing a guess on every example and dropping it if it fails (Guess and check inside the table).',
  'The rule is a x (b + 1): 2 x 4 = 8, 4 x 2 = 8, 5 x 3 = 15, 3 x 4 = 12. So 6 x 5 = 30. For x ★ 3: x times 4 = 28, so x = 7.',
  var=('A new machine: 1 ● 4 = 7, 2 ● 5 = 11, 3 ● 2 = 11, 5 ● 1 = 16. Find 4 ● 6.', '18 (the rule is 3 x the first number + the second number).'))

I('tri', 5, 10, TH, 'Triangles by size', 'List every way',
  ['The figure is made of a big triangle, 2 lines from the top corner to the base, and 1 line across the triangle.', 'Count every triangle in the figure. Count the small ones, the middle ones and the big ones.'],
  ['12 triangles.'],
  'Count by size. First count the smallest triangles, then the ones made of 2 pieces, and so on. Keep a list.',
  'Which lines do you need to make any triangle? What do all the triangles have in common?',
  'Every triangle uses the top corner and two of the 4 lines from it (6 ways to choose), and then is cut off either by the base or by the line across (2 ways): 6 x 2 = 12. Accept a size-by-size list that totals 12, for example 6 triangles that stop at the line across and 6 that reach the base.',
  'Choose 2 of the 4 lines through the top corner (6 pairs). Each pair makes one triangle cut off by the line across and one cut off by the base. 6 x 2 = 12. No triangle can use both the line across and the base, because they are parallel.',
  fig=('tri12',))

I('bounds', 5, 10, TH, 'Counting numbers in bounds', 'List every way',
  ['How many whole numbers between 300 and 600 have digits that add up to 6?', 'List them in order so that none is missed.'],
  ['9 numbers: 303, 312, 321, 330, 402, 411, 420, 501, 510.'],
  'Split into cases by the first digit: 3, 4 or 5. For each case, what must the other two digits add up to?',
  'Why is 600 not in the list? How many pairs of digits make 3? Make 2? Make 1?',
  'First digit 3: other digits add to 3, so 4 numbers. First digit 4: add to 2, so 3 numbers. First digit 5: add to 1, so 2 numbers. 4 + 3 + 2 = 9.',
  'First digit 3: 03, 12, 21, 30, so 303, 312, 321, 330. First digit 4: 02, 11, 20. First digit 5: 01, 10. A total of 4 + 3 + 2 = 9.',
  var=('How many whole numbers between 200 and 500 have digits that add up to 5?', '9.'))

I('pile', 5, 10, GF, 'Least possible: the fullest bag', 'Guess and check',
  ['Ravi puts 23 marbles into 4 bags. No two bags hold the same number of marbles, and no bag is empty.',
   'What is the smallest number of marbles that the fullest bag can hold?'],
  ['8 marbles.'],
  'Test a target for the fullest bag. If it holds 7, what is the most the other 3 bags can hold?',
  'Why can the fullest bag not hold 7? Show a way that works for 8.',
  'The test of the target: with 7 the biggest total is 7 + 6 + 5 + 4 = 22, which is less than 23. With 8, one way is 8 + 6 + 5 + 4 = 23. Listen for the argument that 7 is impossible, not only that 8 works.',
  'If the fullest bag had 7 or fewer, the 4 different numbers would add to at most 7 + 6 + 5 + 4 = 22, which is less than 23. With 8 it works: 8 + 6 + 5 + 4 = 23. The answer is 8.',
  var=('Ravi puts 30 marbles into 5 different bags, all different and none empty. What is the smallest the fullest bag can hold?', '8.'))

I('evencap', 5, 10, GF, 'Greatest possible with a rule', 'Guess and check',
  ['Ali chooses 6 different whole numbers from 1 to 12. He wants their total to be even.', 'What is the greatest total he can get?'],
  ['56.'],
  'Start with the 6 biggest numbers and find their total. Is it even? If not, what is the smallest change you can make?',
  'Why does swapping one number change odd to even? How do you know that no total greater than 56 works?',
  '12 + 11 + 10 + 9 + 8 + 7 = 57, odd. Change one number by 1 (replace 7 by 6): 56. Any greater total is 57 only, which is odd. Listen for "the biggest possible is 57 and it is odd, so the next one down".',
  'The greatest total possible is 57, and it is odd. The next total below is 56. Replacing 7 by 6 gives 12 + 11 + 10 + 9 + 8 + 6 = 56, which is even.',
  var=('Mei chooses 5 different whole numbers from 1 to 10. She wants the total to be odd. What is the greatest total?', '39.'))

I('r7', 5, 10, GF, 'Ratio and the difference', 'Draw it',
  ['Ali and Ben have marbles in the ratio 7 : 4. Ali has 24 more marbles than Ben.', '(a) How many parts are the difference between them?', '(b) How many marbles is one part?', '(c) How many marbles does each boy have?'],
  ['(a) 3 parts.', '(b) 8 marbles.', '(c) Ali 56 marbles and Ben 32 marbles.'],
  'Draw two bars: Ali 7 units, Ben 4 units. The extra 3 units on Ali\'s bar are the 24 marbles.',
  'How many units is the 24? How many marbles is each unit? Can you check with the 7 : 4 and the difference of 24?',
  '7 - 4 = 3 units is 24 marbles, so 1 unit is 8. Ali 7 x 8 = 56, Ben 4 x 8 = 32. Check: 56 - 32 = 24 and 56 : 32 = 7 : 4. Listen for "the difference in parts is the difference in marbles".',
  '3 parts = 24 marbles, so 1 part = 8 marbles. Ali: 7 x 8 = 56. Ben: 4 x 8 = 32. Check: 56 - 32 = 24 and dividing both by 8 gives 7 : 4.',
  var=('Mei and Siti have stickers in the ratio 5 : 2. Mei has 36 more than Siti. How many does each have?', 'Mei 60 stickers, Siti 24 stickers.'),
  fig=('bars', [('Ali', [(7, '#8EC5F0', '')]), ('Ben', [(4, '#FFE08A', '')])], 'Bars: Ali 7 parts, Ben 4 parts'), preview=True)
