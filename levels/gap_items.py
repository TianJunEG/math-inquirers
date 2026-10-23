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
  ['(a) Ben borrows a library book on a Monday and must return it 45 days later. Name the weekday of the return date.',
   '(b) Kumar starts a trip on a Saturday. Name the weekday that comes 30 days after that Saturday.'],
  ['(a) Thursday.', '(b) Monday.'],
  'A week has 7 days, so the days repeat in a cycle of 7. Write the days across the top of a table, then jump 7 days at a time.',
  'How many whole weeks are in 45 days? What is left over, and what does the leftover tell us?',
  '45 = 6 x 7 + 3, so it is the same as 3 days later. This is the remainder move from today\'s lesson. Listen for "divide by 7 and look at the remainder".',
  '45 days = 6 weeks and 3 days: Monday plus 3 days is Thursday. 30 days = 4 weeks and 2 days: Saturday plus 2 days is Monday.',
  var=('Siti starts swimming lessons on a Tuesday. Name the weekday that comes 100 days after that Tuesday.', 'Thursday (100 = 14 weeks and 2 days).'))

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
  ['Here is a list: 11, 14, 17, 20, ... , 41. The list goes up in steps of 3.',
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
   '(a) Find the least total possible.', '(b) Find the greatest total possible.', '(c) Which of these totals can never happen: 3, 4, 13, 24, 25?'],
  ['(a) 4.', '(b) 24.', '(c) 3 and 25 are impossible.'],
  'Do not roll anything. Ask what the lowest face and the highest face on one die are, then think about 4 dice.',
  'Can she get every total from 4 to 24? How can you tell?',
  'Smallest 1 + 1 + 1 + 1, largest 6 + 6 + 6 + 6. Listen for "change one die by 1 at a time", which gives every total in between.',
  '4 x 1 = 4 and 4 x 6 = 24. Starting at 4 you can raise one die by 1 at a time up to 24, so every total from 4 to 24 can be made. 3 is below 4 and 25 is above 24.',
  var=('Siti rolls 5 dice and adds the scores. Find the least and the greatest total possible.', '5 and 30.'))

I('stages', 4, 10, TH, 'Counting in two stages', 'List every way',
  ['Aisha owns 4 tops, 3 skirts and 2 hats. An outfit is 1 top, 1 skirt and 1 hat.', '(a) Find the number of different outfits.',
   '(b) The red top never goes with the green skirt. Find the number of outfits that are left.'],
  ['(a) 24 outfits.', '(b) 22 outfits.'],
  'Draw 4 boxes for the tops. Under each one, show 3 skirts. How many top-and-skirt pairs is that?',
  'How many outfits use the red top with the green skirt? What do you do with that number?',
  '4 x 3 = 12 pairs, times 2 hats = 24. Listen for "multiply the choices". For (b) the red-green pair has 2 outfits (one for each hat); 24 - 2 = 22.',
  '4 x 3 x 2 = 24. The red top with the green skirt can go with either hat, so 2 outfits are removed: 24 - 2 = 22.',
  var=('A bus route has 3 ways from the depot to the market and 4 ways from the market to the harbour. Find the number of routes from the depot to the harbour through the market.', '12 routes.'))

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
  var=('Find 4 x 29 x 25. Which of 17 + 18 + 19 and 6 x 15 + 1 is even?', '2 900. Only 17 + 18 + 19 = 54 is even, and 6 x 15 + 1 = 91 is odd.'))

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
  ['A tower is made of 3 dice, one on top of another, standing on a table. Opposite faces of each die sum to 7. The upper face of the highest die shows 4.',
   'Find the total number of dots on the hidden faces: the face touching the table, plus each pair of faces that touch each other.'],
  ['17 dots.'],
  'Take a real die if you have one. Turn it and look: which faces are on opposite sides? What do two opposite faces always add up to?',
  'Which hidden faces form pairs that add up to 7? Which one hidden face is left over?',
  'The top and bottom of the bottom die add to 7. The top and bottom of the middle die add to 7. The bottom of the top die is 7 - 4 = 3. Listen for "pairs of opposite faces".',
  'Hidden faces: the bottom die\'s bottom and top (7), the middle die\'s bottom and top (7), and the top die\'s bottom face (7 - 4 = 3). 7 + 7 + 3 = 17. It does not matter how the lower dice are turned.',
  var=('The upper face of the highest die shows 2. Find the hidden total now.', '19 dots.'),
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
  ['The figure is a big triangle with a line from its top corner to each of 2 points on the base, and 1 line cutting across it, parallel to the base.', 'Count all the triangles of every size.'],
  ['12 triangles.'],
  'Count by size. First count the smallest triangles, then the ones made of 2 pieces, and so on. Keep a list.',
  'Which lines do you need to make any triangle? What do all the triangles have in common?',
  'Every triangle uses the top corner and two of the 4 lines from it (6 ways to choose), and then is cut off either by the base or by the line across (2 ways): 6 x 2 = 12. Accept a size-by-size list that totals 12, for example 6 triangles that stop at the line across and 6 that reach the base.',
  'Choose 2 of the 4 lines through the top corner (6 pairs). Each pair makes one triangle cut off by the line across and one cut off by the base. 6 x 2 = 12. No triangle can use both the line across and the base, because they are parallel.',
  fig=('tri12',))

I('bounds', 5, 10, TH, 'Counting numbers in bounds', 'List every way',
  ['How many whole numbers between 300 and 600 have digits that add up to 6?', 'Write them from smallest to greatest.'],
  ['9 numbers: 303, 312, 321, 330, 402, 411, 420, 501, 510.'],
  'Split into cases by the first digit: 3, 4 or 5. For each case, what must the other two digits add up to?',
  'Why is 600 not in the list? How many pairs of digits make 3? Make 2? Make 1?',
  'First digit 3: other digits add to 3, so 4 numbers. First digit 4: add to 2, so 3 numbers. First digit 5: add to 1, so 2 numbers. 4 + 3 + 2 = 9.',
  'First digit 3: 03, 12, 21, 30, so 303, 312, 321, 330. First digit 4: 02, 11, 20. First digit 5: 01, 10. A total of 4 + 3 + 2 = 9.',
  var=('How many whole numbers between 200 and 500 have a digit sum of 5?', '9.'))

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
  ['Kumar and Wei collect marbles in the ratio 7 : 4. Kumar\'s collection is bigger than Wei\'s by 24 marbles.', '(a) How many parts is the difference between the two collections?', '(b) How many marbles is one part?', '(c) Find the number of marbles that each boy has.'],
  ['(a) 3 parts.', '(b) 8 marbles.', '(c) Kumar 56 marbles and Wei 32 marbles.'],
  'Draw two bars: Kumar 7 units, Wei 4 units. The extra 3 units on Kumar\'s bar are the 24 marbles.',
  'How many units is the 24? How many marbles is each unit? Can you check with the 7 : 4 and the difference of 24?',
  '7 - 4 = 3 units is 24 marbles, so 1 unit is 8. Kumar 7 x 8 = 56, Wei 4 x 8 = 32. Check: 56 - 32 = 24 and 56 : 32 = 7 : 4. Listen for "the difference in parts is the difference in marbles".',
  '3 parts = 24 marbles, so 1 part = 8 marbles. Kumar: 7 x 8 = 56. Wei: 4 x 8 = 32. Check: 56 - 32 = 24 and dividing both by 8 gives 7 : 4.',
  var=('Mei and Siti have stickers in the ratio 5 : 2. Mei has 36 more than Siti. How many does each have?', 'Mei 60 stickers, Siti 24 stickers.'),
  fig=('bars', [('Kumar', [(7, '#8EC5F0', '')]), ('Wei', [(4, '#FFE08A', '')])], 'Bars: Kumar 7 parts, Wei 4 parts'), preview=True)

# =============================================================== LEVEL 6  (ratio, percentage, area and rate items are taster size)
I('rate', 6, 1, GF, 'Meeting and catching up', 'Draw it',
  ['(a) Town A and town B are 60 km apart. Ali cycles from A towards B at 15 km/h. At the same time Ben cycles from B towards A at 25 km/h. After how many hours do they meet?',
   '(b) Siti leaves a station at 9:00 and travels at 40 km/h. Kumar leaves the same station at 9:30 on the same road at 60 km/h. At what time does Kumar catch Siti?'],
  ['(a) 1.5 hours.', '(b) 10:30.'],
  'Draw the road as a line. In (a) both children close the gap, so add their speeds. In (b) Kumar closes the gap, so take the speeds away from each other.',
  'How far apart are they at the start, and by how many km does the gap change each hour?',
  '(a) Closing speed 15 + 25 = 40 km/h, so 60 / 40 = 1.5 hours. (b) Siti has a 20 km start, closing speed 60 - 40 = 20 km/h, so 1 hour after 9:30. Listen for "the gap" and "closing speed".',
  '(a) 15 + 25 = 40 km each hour, 60 / 40 = 1.5 hours. (b) At 9:30 Siti is 40 x 0.5 = 20 km ahead. Kumar gains 60 - 40 = 20 km each hour, so he catches her 1 hour later, at 10:30.',
  var=('Two towns are 90 km apart. Mei cycles at 20 km/h and Ravi at 25 km/h towards each other. After how long do they meet?', '2 hours.'))

I('tele', 6, 1, TH, 'Sums that cancel', 'Spot the pattern',
  ['(a) Work out 1/3 - 1/4. Compare it with 1/(3 x 4).', '(b) Find 1/(3 x 4) + 1/(4 x 5) + 1/(5 x 6) + ... + 1/(9 x 10).'],
  ['(a) 1/12. It is the same as 1/(3 x 4).', '(b) 7/30.'],
  'Write each fraction in (b) as a difference, like the one you found in (a). Then write the whole sum out in a line and look at what is left.',
  'Which terms cancel? Which two terms are left at the end?',
  'Each term 1/(n x (n + 1)) = 1/n - 1/(n + 1). The sum is 1/3 - 1/4 + 1/4 - 1/5 + ... + 1/9 - 1/10, so only 1/3 - 1/10 is left. Listen for "the middle cancels". This is Try something simpler: start with two terms.',
  '1/3 - 1/4 = 4/12 - 3/12 = 1/12. The sum telescopes: 1/3 - 1/10 = 10/30 - 3/30 = 7/30.',
  var=('Find 1/(2 x 3) + 1/(3 x 4) + ... + 1/(7 x 8).', '3/8 (this is 1/2 - 1/8).'))

I('d9', 6, 2, TH, 'Digit sums for 3 and 9', 'Spot the pattern',
  ['(a) Use digit sums. Which of 6 372, 5 481 and 7 296 are multiples of 9?', '(b) Which of the three numbers are multiples of 3 but not of 9?'],
  ['(a) 6 372 and 5 481.', '(b) 7 296.'],
  'Add the digits of each number. If the digit sum is in the 9 times table the number is too. What about the 3 times table?',
  'Why does a multiple of 9 always have a digit sum that is a multiple of 9? Is 7 296 in the 3 table?',
  '6 + 3 + 7 + 2 = 18, 5 + 4 + 8 + 1 = 18, 7 + 2 + 9 + 6 = 24. 24 is in the 3 table but not the 9 table. Listen for the reason: 10, 100, 1 000 are each 1 more than a multiple of 9.',
  '6 372 has digit sum 18 and 5 481 has digit sum 18, so both are multiples of 9. 7 296 has digit sum 24, so it is a multiple of 3 and not of 9.',
  var=('Which of 4 536, 8 127 and 3 705 are multiples of 9?', '4 536 and 8 127 (digit sums 18 and 18; 3 705 has digit sum 15).'))

I('d45', 6, 2, GF, 'Tests for 5 and 9 together', 'List every way',
  ['The 4-digit number 6[ ]3[ ] has two empty boxes. Each box holds one digit. The number is a multiple of 45.', 'Find every number that fits.'],
  ['6 030, 6 930 and 6 435.'],
  'A multiple of 45 is in the 5 table and in the 9 table. What does the 5 table tell you about the last digit? What does the 9 table tell you about the digit sum?',
  'How many choices are there for the last digit? For each choice, what must the second digit be?',
  'Last digit 0 or 5. Digit sum 6 + a + 3 + b = 9 + a + b must be in the 9 table, so a + b is 0, 9 or 18. With b = 0: a = 0 or 9. With b = 5: a = 4. Listen for an organised list of the cases.',
  'The last digit is 0 or 5. If it is 0, the second digit a has 9 + a a multiple of 9, so a = 0 or 9: 6 030 and 6 930. If it is 5, 14 + a is a multiple of 9, so a = 4: 6 435. Check: 6 435 = 45 x 143.',
  var=('The 4-digit number 7[ ]2[ ] is a multiple of 45. Find every number that fits.', '7 020, 7 920 and 7 425.'))

I('zero', 6, 2, TH, 'Zeros at the end', 'Try something simpler',
  ['How many zeros are at the end of the product 12 x 15 x 20 x 25 x 35?', 'Do not multiply it all out.'],
  ['4 zeros.'],
  'A zero at the end comes from one 2 and one 5 multiplied together, because 2 x 5 = 10. Break each number into 2s and 5s.',
  'How many 2s are there in all? How many 5s? Which one limits the number of zeros?',
  '2s: 12 has two, 20 has two, so 4. 5s: 15, 20, 25 (two), 35, so 5. There are 4 pairs of 2 and 5, so 4 zeros; the extra 5 does not make a zero without another 2. Check by multiplying: 3 150 000.',
  '12 = 2 x 2 x 3, 15 = 3 x 5, 20 = 2 x 2 x 5, 25 = 5 x 5, 35 = 5 x 7. Four 2s and five 5s: 4 pairs, so 4 zeros. Check: the product is 3 150 000.',
  var=('How many zeros are at the end of 16 x 25 x 35 x 40?', '4 zeros (seven 2s and four 5s).'))

I('pct', 6, 4, TH, 'Percentage change, with units', 'Draw it',
  ['(a) Ravi spends 25% of his money and $60 is left. Find the amount he began with.',
   '(b) Mei has 50 stickers. Ali has 20% more stickers than Mei. Ben has 20% fewer stickers than Mei. Find the difference between Ali\'s and Ben\'s stickers.'],
  ['(a) $80.', '(b) 20 more stickers.'],
  'Draw a bar for the money Ravi had at first. The part he spent is 25%, so 4 units make the whole and 1 unit is spent.',
  'What percentage is left, and how many units is that? How many dollars is one unit? For (b), what are Ali\'s and Ben\'s stickers as percentages of Mei\'s?',
  '(a) 75% is left, 3 units = $60, 1 unit = $20, whole = 4 x $20 = $80. (b) Ali has 120% of 50 = 60 and Ben has 80% of 50 = 40, so 20 more; the gap is 40% of 50. Listen for "percent of what?": the 100% is Mei\'s stickers.',
  '(a) 100% - 25% = 75% = $60, so 25% = $20 and 100% = $80. (b) Ali: 50 + 10 = 60. Ben: 50 - 10 = 40. Difference 60 - 40 = 20.',
  var=('Siti uses up 40% of her savings and $90 remains. How much were her savings at the start?', '$150.'))

I('pipe', 6, 4, TH, 'A rate as an equation', 'Make a table',
  ['A tank holds 360 litres. A tap fills it at 24 litres each minute. A drain at the bottom lets out 4 litres each minute. The tank starts empty and both are open.',
   '(a) How many litres does the tank gain each minute?', '(b) Find the time, in minutes, until the tank is full.', '(c) The tap is then closed and the drain stays open. Find the time in minutes until the tank is empty.'],
  ['(a) 20 litres each minute.', '(b) 18 minutes.', '(c) 90 minutes.'],
  'Make a table of minutes and litres in the tank. Then write the rule as an equation: litres = rate x time.',
  'What is the rate of the tank filling when both are open? What equation can you write, and what operation undoes it?',
  'Net rate 24 - 4 = 20 litres per minute. 20 x t = 360, so t = 18. For (c) 4 x t = 360, so t = 90. Listen for "rate x time = amount" and for undoing it by dividing.',
  'Net fill rate: 24 - 4 = 20 litres each minute. 20 x t = 360 gives t = 360 / 20 = 18 minutes. Emptying: 4 x t = 360 gives t = 90 minutes.',
  var=('A tank holds 500 litres. A tap fills 30 litres each minute and a drain lets out 5 litres each minute. Find the time in minutes until the empty tank is full, with both open.', '20 minutes.'))

I('short', 6, 4, TH, 'Shortcuts before calculating', 'Try something simpler',
  ['Find each answer without a long calculation. Say what you noticed.', '(a) 83 x 83 - 82 x 84', '(b) 0.65 x 27 + 0.65 x 73'],
  ['(a) 1.', '(b) 65.'],
  'Try something simpler first: work out 5 x 5 - 4 x 6 and 6 x 6 - 5 x 7. What do you notice? For (b), look for a number that appears twice.',
  'Why does the answer to (a) always come out the same? What can you take out of both parts in (b)?',
  '(a) n x n - (n - 1) x (n + 1) = 1 for every n. (b) Take out 0.65: 0.65 x (27 + 73) = 0.65 x 100 = 65. Listen for the small cases and the shared factor.',
  '(a) 5 x 5 - 4 x 6 = 1 and 6 x 6 - 5 x 7 = 1, so 83 x 83 - 82 x 84 = 1 (the product of the neighbours is always 1 less than the square). (b) 0.65 x (27 + 73) = 0.65 x 100 = 65.',
  var=('Find 46 x 46 - 45 x 47 and 2.4 x 35 + 2.4 x 65.', '1 and 240.'))

I('votes', 6, 5, GF, 'Worst case: the runner-up', 'Act it out',
  ['Ali, Mei and Ravi stand for class captain. The child with the most votes wins. There are 31 votes in all. After 20 votes are counted, Ali has 9, Mei has 7 and Ravi has 4.',
   'How many more of the remaining 11 votes must Ali get to be sure of winning, whatever happens to the other votes?'],
  ['5 more votes.'],
  'Act it out as the worst case: the votes Ali does not get all go to Mei. Try Ali getting 3 more, then 4 more, then 5 more.',
  'In the worst case who is Ali\'s rival? How do you know that 4 is not enough?',
  'If Ali gets x more, Mei could get all the other 11 - x. Ali needs 9 + x to be more than 7 + (11 - x). With x = 4: Ali 13 and Mei 14. With x = 5: Ali 14 and Mei 13. Listen for "give the worst case to the runner-up".',
  'Ali ends with 9 + x. In the worst case all the other 11 - x votes go to Mei, who ends with 7 + 11 - x = 18 - x. Ali wins for sure when 9 + x is greater than 18 - x, so x = 5 (14 against 13). With x = 4 it is 13 against 14.',
  var=('Ali 12, Mei 9 and Ravi 5 after 26 votes out of 40. How many more of the 14 remaining votes must Ali get to be sure of winning?', '6 more votes (Ali 18 against Mei at most 17).'))

I('socks', 6, 5, TH, 'Worst case: how many to be sure', 'Act it out',
  ['A drawer has 8 red socks, 6 blue socks and 5 green socks. Aisha takes socks out without looking.',
   '(a) How many socks must she take to be sure of a pair of the same colour?', '(b) How many socks must she take to be sure of 3 socks of the same colour?', '(c) How many socks must she take to be sure of 2 blue socks?'],
  ['(a) 4 socks.', '(b) 7 socks.', '(c) 15 socks.'],
  'Act it out as bad luck: how many can she take with no pair? Then one more must make a pair. Use counters of three colours.',
  'What is the worst that can happen in (c)? How many socks is that before the first blue sock arrives, and what then?',
  '(a) 1 of each colour is 3, so 4. (b) 2 of each is 6, so 7. (c) Worst case: all 8 red and all 5 green first (13), then 1 blue is not enough, so 2 blue: she needs 13 + 2 = 15. Listen for "one fewer than the target, in every colour".',
  'The worst case is the longest run with no success. (a) 3 socks (one of each colour), so 4. (b) 6 socks (two of each colour), so 7. (c) all 13 non-blue socks and then 1 blue is 14 socks with only 1 blue, so 15.',
  var=('A box has 7 black pens, 5 blue pens and 4 red pens. How many must you take out to be sure of 2 pens of the same colour?', '4 pens.'))

I('size', 6, 5, TH, 'Squares and rectangles by size', 'List every way',
  ['The grid has 5 columns and 3 rows of small squares.', '(a) How many square shapes, of all sizes, are in the grid?', '(b) How many rectangles of any size are in the grid? A square counts as a rectangle.'],
  ['(a) 26 squares.', '(b) 90 rectangles.'],
  'Try something simpler first: a 1 by 3 strip, then a 2 by 3 grid. Count by size in a table.',
  'How many 1 by 1 squares? 2 by 2? 3 by 3? For rectangles, how many ways can you choose the left and right edges? The top and bottom edges?',
  'Squares: 15 + 8 + 3 = 26. Rectangles: choose 2 of the 6 vertical lines (15 ways) and 2 of the 4 horizontal lines (6 ways): 15 x 6 = 90. Accept a size-by-size table for rectangles too.',
  'Squares: 1 by 1 is 5 x 3 = 15, 2 by 2 is 4 x 2 = 8, 3 by 3 is 3 x 1 = 3, total 26. Rectangles: pairs of vertical lines 6 x 5 / 2 = 15, pairs of horizontal lines 4 x 3 / 2 = 6, so 15 x 6 = 90.',
  var=('In a grid with 4 columns and 3 rows, how many square shapes of all sizes can be found?', '20 (12 + 6 + 2).'),
  fig=('grid', 5, 3, 'A grid with 5 columns and 3 rows of small squares'))

I('derange', 6, 5, GF, 'Nobody in their own place', 'List every way',
  ['Four friends each hang a coat on one of 4 hooks, 1 coat on each hook. Each coat first hangs on its own hook.', 'The coats are shuffled so that no coat is on its own hook.', 'In how many ways can the coats be hung?'],
  ['9 ways.'],
  'Name the coats 1, 2, 3, 4 and the hooks the same. List the ways in order, starting with coat 1 on hook 2.',
  'How many ways start with coat 1 on hook 2? Does the same number work for coat 1 on hook 3 and on hook 4?',
  'Coat 1 on hook 2 gives 3 ways, and the same is true for hook 3 and hook 4. The ordered list is 2143, 2341, 2413, 3142, 3412, 3421, 4123, 4312, 4321. Listen for a systematic list, not guessing.',
  'Write the hook for each coat in order 1, 2, 3, 4. Coat 1 on hook 2: 2143, 2341, 2413. Coat 1 on hook 3: 3142, 3412, 3421. Coat 1 on hook 4: 4123, 4312, 4321. That is 3 + 3 + 3 = 9 ways.',
  var=('Three friends hang 3 coats on 3 hooks so that nobody has their own hook. How many ways?', '2 ways (231 and 312).'))

I('perim', 6, 7, TH, 'Perimeter of a staircase', 'Try something simpler',
  ['The figure is a staircase with 4 steps. Every step is 3 cm high and 3 cm wide. All the corners are right angles.',
   '(a) Find the perimeter of the figure.', '(b) A staircase has 10 steps. Every step is 2 cm high and 2 cm wide. Find its perimeter.'],
  ['(a) 48 cm.', '(b) 80 cm.'],
  'Try something simpler: a staircase with 1 step, then 2 steps. Can you slide the steps to the edges to make a rectangle?',
  'What is the width of the whole figure, and the height? What stays the same when you slide a step sideways?',
  'Sliding the horizontal pieces to the bottom and the vertical pieces to the left makes a rectangle: the perimeter is the same as the rectangle around the whole figure. (a) 12 + 12 + 12 + 12 = 48. (b) 20 + 20 + 20 + 20 = 80.',
  'The horizontal edges add up to the width of the figure (twice: top and bottom) and the vertical edges add up to its height (twice). (a) Width 4 x 3 = 12, height 12, perimeter 2 x (12 + 12) = 48. (b) 2 x (20 + 20) = 80.',
  var=('A staircase has 6 steps, each 5 cm high and 5 cm wide. Find the perimeter.', '120 cm.'),
  fig=('stairs', 4, 'A staircase figure with 4 steps'))

I('quarter', 6, 7, GF, 'A quarter circle in a square', 'Draw it',
  ['A square has sides of 10 cm. A quarter circle of radius 10 cm is drawn from one corner of the square, as in the picture. Use 3.14 for the number pi.',
   'Find the area of the blue part of the square, outside the quarter circle.'],
  ['21.5 cm².'],
  'Find two areas you know: the whole square and the quarter circle. How are they related to the blue part?',
  'What fraction of a full circle with radius 10 cm is the quarter circle? What is the area of the full circle?',
  'Area of the full circle 3.14 x 10 x 10 = 314, the quarter is 314 / 4 = 78.5. Blue = 100 - 78.5 = 21.5. Listen for "subtract the quarter circle from the square".',
  'Square: 10 x 10 = 100 cm². Quarter circle: 3.14 x 10 x 10 / 4 = 78.5 cm². Blue part: 100 - 78.5 = 21.5 cm².',
  var=('A square has sides of 20 cm. A quarter circle of radius 20 cm is drawn from one corner. Use 3.14. Find the area of the part outside the quarter circle.', '86 cm².'),
  fig=('quarter', 'A square with a quarter circle drawn from one corner; the part outside the quarter circle is blue'))

I('clock', 6, 7, TH, 'Angle between the clock hands', 'Draw it',
  ['In one minute the minute hand sweeps 6° and the hour hand sweeps 0.5°.', '(a) At 3:20, how many degrees apart are the two hands?', '(b) At 4:10, how many degrees apart are the two hands?'],
  ['(a) 20°.', '(b) 65°.'],
  'Measure both hands from 12 as angles. Draw a clock and mark where each hand points at the time.',
  'How far has the hour hand moved from the 3 by 3:20? How far from 12 is the minute hand?',
  'At 3:20 the hour hand is at 3 x 30 + 20 x 0.5 = 100 degrees from 12. The minute hand is 20 x 6 = 120 degrees from 12. The difference is 20. At 4:10: 125 and 60, difference 65.',
  '(a) Hour hand: 90 + 10 = 100°. Minute hand: 120°. Angle 20°. (b) Hour hand: 120 + 5 = 125°. Minute hand: 60°. Angle 65°.',
  var=('At 2:40, how many degrees apart are the two hands?', '160° (hour hand at 80°, minute hand at 240°).'))

I('cr1', 6, 8, TH, 'Letters stand for digits', 'Guess and check',
  ['Each letter stands for one digit. Different letters stand for different digits. A letter at the start of a number is not 0.', 'Find D, E, C, A and B.'],
  ['D = 5, E = 7, C = 3, A = 1, B = 4.  Check: 573 + 771 = 1344.'],
  'A cipher replaces letters with other symbols, and so does this puzzle. Start with the column that cannot be wrong: the answer has 4 digits.',
  'What is the first letter of the answer? Which column do you do next, and what do you try?',
  'A = 1. The ones and tens digits of the answer are the same letter, B, which gives two equations to test. Make a table of tries for C and E. This is Guess and check, not Spot the pattern, even though it sits in the Secret Codes lesson.',
  'A = 1 (two 3-digit numbers add to less than 2 000). Ones: C + 1 = B, so there is no carry. Tens: E + E = 10 + B with a carry of 1. Hundreds: D + E + 1 = 10 + C. So B = C + 1 and 2E = 11 + C, which needs C odd. C = 1 is used by A; C = 3 gives E = 7, B = 4 and D = 5; C = 5 gives D = B = 6 and C = 7 gives D = C, which break the rule. Check: 573 + 771 = 1344.',
  fig=('sum', 'DEC', 'EEA', 'ACBB'))

I('cr2', 6, 8, GF, 'Letters stand for digits, a longer one', 'Guess and check',
  ['Each letter stands for one digit. Different letters stand for different digits. A letter at the start of a number is not 0.', 'Find B, D, E, A and C.'],
  ['B = 9, D = 5, E = 6, A = 1, C = 0.  Check: 956 + 105 = 1061.'],
  'What is the first letter of the answer? Then look for a column where a letter added to itself or to a known digit has only a few possible answers.',
  'Which letter must be 0? Why? How do you check your answer against every column?',
  'A = 1 from the size of the sum. Ones: E + D = 11. Tens: D + C + 1 = E. Combine them: 2 x D + C = 10. Children use a table of tries for C and D. Accept any organised method that checks all four columns.',
  'A = 1. Ones: E + D = 10 + A = 11. Tens: D + C + 1 = E. So 2D + C = 10. Hundreds: B + A = 10 + C, so B = 9 + C and C = 0, D = 5, E = 6, B = 9. Check: 956 + 105 = 1061 and ACEA reads 1, 0, 6, 1. This is the only solution (checked by a script).',
  fig=('sum', 'BDE', 'ACD', 'ACEA'))

I('last', 6, 8, TH, 'Last digit of a power', 'Spot the pattern',
  ['(a) Find the last digit of 2⁴⁵ (45 twos multiplied together).', '(b) Find the last digit of 13³⁰ (30 thirteens multiplied together).'],
  ['(a) 2.', '(b) 9.'],
  'Only the last digit matters. Write the last digit of 2, 2 x 2, 2 x 2 x 2, ... and look for the repeat. Then use the clock arithmetic idea: what is 45 on a clock of the cycle length?',
  'How long is the cycle for 2? For 3 (the last digit of 13)? How does a remainder tell you where you land?',
  '2: 2, 4, 8, 6, cycle of 4. 45 = 11 x 4 + 1, so the 1st in the cycle: 2. 3: 3, 9, 7, 1, cycle of 4. 30 = 7 x 4 + 2, so 9. Listen for "remainder after dividing by the cycle length".',
  'Last digits of powers of 2 repeat 2, 4, 8, 6. 45 mod 4 = 1, so 2. Only the last digit of 13 matters, which is 3: 3, 9, 7, 1 repeat. 30 mod 4 = 2, so 9.',
  var=('Find the last digit of 7²⁰²⁶.', '9 (the cycle is 7, 9, 3, 1 and 2 026 mod 4 = 2).'))

I('pct2', 6, 9, TH, 'Percentages from a table', 'Make a table',
  ['80 children each choose one favourite fruit. 36 choose apple, 20 choose banana, 16 choose mango and the rest choose orange.',
   '(a) How many children choose orange?', '(b) What percentage of the children choose apple?', '(c) What percentage of the children choose banana or orange?'],
  ['(a) 8 children.', '(b) 45%.', '(c) 35%.'],
  'Make a table of fruit, number of children and percentage. The total of the number column is 80.',
  'How can you find the percentage for each row? What should the percentage column add up to?',
  'Percentage = children / 80 x 100, or 1 child is 1.25%. Apple 36 / 80 = 45%. Banana 25% and orange 10% add to 35%. Listen for a check that the percentages add to 100%.',
  'Orange: 80 - 36 - 20 - 16 = 8. Apple: 36 / 80 = 45 / 100. Banana 20 / 80 = 25%, orange 8 / 80 = 10%, so 35%. Check: 45% + 25% + 20% + 10% = 100%.',
  var=('60 children choose a sport. 27 choose swimming, 15 choose football, 12 choose running and the rest choose tennis. What percentage choose tennis?', '10%.'),
  fig=('table', ['Fruit', 'Children', '%'], [['Apple', 36, '?'], ['Banana', 20, '?'], ['Mango', 16, '?'], ['Orange', '?', '?']], 'Table of fruit, children and percentage', [150, 160, 100]))

I('pack', 6, 10, GF, 'The greatest total you cannot make', 'Make a table',
  ['Stickers are sold in sheets of 4 and sheets of 9. Mei buys some sheets of each kind, or none of one kind.', 'What is the greatest number of stickers that she cannot buy exactly?'],
  ['23 stickers.'],
  'Write the numbers 1 to 40 in rows of 4. Mark every total you can make. Look for the first row where every number is marked.',
  'Once you have 4 totals in a row, what happens next? How do you know 23 is the last one?',
  'Four in a row is enough because adding 4 reaches everything after. 24 to 27 are all buyable (24 = 4 x 6, 25 = 16 + 9, 26 = 8 + 18, 27 = 3 x 9), so nothing above 23 is missing, and 23 cannot be made. Listen for the argument.',
  'Totals are 4a + 9b. 24, 25, 26 and 27 can all be made, so every number from 24 up can be made by adding 4s. 23 cannot: 23 - 9 = 14, 23 - 18 = 5 are not multiples of 4, and 23 is not a multiple of 4. The greatest total that cannot be made is 23.',
  var=('Sheets come in 5s and 6s. What is the greatest total you cannot make?', '19.'))
