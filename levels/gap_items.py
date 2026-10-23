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
