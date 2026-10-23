"""Original skill-gap items for the HOLIDAY program, Levels 1 to 3 (owner decision GAPS-SLIDES-NOW, 23 Oct 2026).
Every item is an ADDITION: an optional early-finisher slide or a tutor-bank item. Nothing here changes a printed page.
Skills are named generically; contexts and numbers are our own. Machine-checked by rebuild/skill_items_check.py (independent brute force).

Fields
  id      L<level>-<code>        lesson  host lesson 1..10        slot  'slide' | 'bank'      group  slide group on that lesson (slide items)
  skill   plain skill name       tool    key of levels/spine.json (pattern list draw table backwards guess simpler actout)
  stem    text (read aloud)      parts   list of 'a) ...' lines    fig   (name, kwargs) drawn by gen_skill_slides.py, or None
  a       worked answer (text)   p      parameters the checker recomputes from      ans   canonical answers the checker must reproduce
  say / ask / listen  tutor notes
"""

TOOLS = {'pattern': 'Spot the pattern', 'list': 'List every way', 'draw': 'Draw it', 'table': 'Make a table',
         'backwards': 'Work backwards', 'guess': 'Guess and check', 'simpler': 'Try something simpler', 'actout': 'Act it out'}

# slide titles (level, lesson, group) -> (title, minutes note)
GROUPS = {
    (1, 1, 'g1'): 'Think harder: what comes next?',
    (1, 2, 'g1'): 'Think harder: tens and ones',
    (1, 2, 'g2'): 'Think harder: add in your head',
    (1, 2, 'g3'): 'Think harder: shapes that stand for numbers',
    (1, 3, 'g1'): 'Think harder: twice as many',
    (1, 4, 'g1'): 'Think harder: days of the week',
    (1, 5, 'g1'): 'Think harder: ages',
    (1, 7, 'g1'): 'Think harder: count all the cubes',
    (1, 9, 'g1'): 'Think harder: the clock',
    (2, 2, 'g1'): 'Think harder: add in clever ways',
    (2, 4, 'g1'): 'Think harder: gaps that change',
    (2, 5, 'g1'): 'Think harder: ages and the gap',
    (2, 8, 'g1'): 'Think harder: cubes in a corner',
    (2, 9, 'g1'): 'Think harder: pictures that stand for numbers',
    (2, 9, 'g2'): 'Think harder: what day is it?',
    (2, 10, 'g1'): 'Think harder: posts and places',
    (2, 10, 'g2'): 'Think harder: how many to be sure?',
    (3, 2, 'g1'): 'Think harder: add by pairing',
    (3, 3, 'g1'): 'Think harder: is it in the 3 table?',
    (3, 3, 'g2'): 'Think harder: count the multiples',
    (3, 7, 'g1'): 'Think harder: the top view',
    (3, 10, 'g1'): 'Think harder: faces that repeat',
    (3, 10, 'g2'): 'Think harder: posts and rectangles',
}

ITEMS = []


def add(**k):
    k.setdefault('fig', None); k.setdefault('parts', []); k.setdefault('group', None)
    ITEMS.append(k)


# =====================================================================  LEVEL 1
add(id='L1-SEQ1', level=1, lesson=1, slot='slide', group='g1', skill='Sequences: each number is made from the two before', tool='pattern',
    stem='Mei writes a pattern: 1, 2, 3, 5, 8, __, __',
    parts=['a) Fill in the gap row. What do you notice?', 'b) Write the next two numbers.'],
    fig=('seq', dict(terms=[1, 2, 3, 5, 8, 0, 0], gaps=[1, 1, 2, 3, None, None], blanks_from=5)),
    a='a) The gaps are 1, 1, 2, 3, 5: they are the pattern numbers again. Each number is the two numbers before it added together (3 + 5 = 8). b) 13 and 21.',
    p=dict(start=[1, 2], n=7), ans=[13, 21],
    say='Some patterns do not add the same number each time. Look at the gaps.',
    ask='What is the gap between 1 and 2? Between 2 and 3? Does the gap stay the same? What do you notice about the gaps and the numbers?',
    listen='"The gaps are the numbers again" or "5 is 2 + 3". Accept "add the last two". Children who only say "it goes up more" need the gap row filled in first.')
add(id='L1-SEQ2', level=1, lesson=1, slot='bank', skill='Sequences: two rules take turns', tool='pattern',
    stem='Start at 2. Add 3, then add 1, then add 3, then add 1, and keep going.',
    parts=['a) Write the first 7 numbers.', 'b) Is 20 in the pattern? Tick Yes or No.'],
    a='a) 2, 5, 6, 9, 10, 13, 14. b) No: the pattern goes ..., 18, 21, 22 and jumps over 20.',
    p=dict(start=2, rules=[3, 1], n=7, test=20), ans=['2 5 6 9 10 13 14', 'no'],
    say='Two rules take turns. Say the rules in order as you write: add 3, add 1, add 3.',
    ask='After 14, what comes next? How do you know 20 will not be there?', listen='Notice that every 2 steps the number goes up by 4, so the pattern climbs 2, 6, 10, 14, 18, 22 on its own.')
add(id='L1-SEQ3', level=1, lesson=1, slot='bank', skill='Sequences: gaps get smaller', tool='table',
    stem='Ravi counts down: 50, 40, 31, 23, 16, __, __',
    parts=['a) Write the next two numbers.', 'b) How much does the number go down each time?'],
    a='a) 10 and 5. b) It goes down 10, then 9, then 8, then 7, then 6, then 5: one less each time.',
    p=dict(start=50, first_gap=10, shrink=1, n=7), ans=[10, 5],
    say='Make a table with a gap row. Write how far each number falls.', ask='What are the gaps? What will the next gap be?', listen='"The gap goes down by 1 each time."')

add(id='L1-PV1', level=1, lesson=2, slot='slide', group='g1', skill='Place value: tens and ones', tool='actout',
    stem='Ben packs 10 pencils in each box. He has 4 full boxes and 6 loose pencils.',
    parts=['a) Find the total number of pencils.', 'b) Siti has 52 pencils packed the same way. Fill in: ___ full boxes and ___ loose pencils.'],
    a='a) 46 pencils (4 tens and 6 ones). b) 5 full boxes and 2 loose pencils.',
    p=dict(tens=4, ones=6, n=52), ans=[46, 5, 2],
    say='Use bundles of 10 sticks and single sticks, or draw a stick for a ten and a dot for a one.',
    ask='How many tens in 46? How many ones? Where do you see the 4 and the 6 in the number?', listen='"4 tens and 6 ones is 46", "the 5 in 52 means 5 boxes of ten". A child who says 52 is "5 and 2" should count the sticks.')
add(id='L1-PV2', level=1, lesson=2, slot='slide', group='g1', skill='Place value: digit cards', tool='list',
    stem='Ali lays two digit cards side by side: 3 and 8. The two cards show a 2-digit number.',
    parts=['a) Write every number the cards can show.', 'b) Circle the greater number.', 'c) Which number is closer to 50?'],
    fig=('cards', dict(nums=[3, 8])),
    a='a) 38 and 83. b) 83 is greater (8 tens is more than 3 tens). c) 38 (it is 12 away from 50; 83 is 33 away).',
    p=dict(cards=[3, 8], target=50), ans=['38 83', 83, 38],
    say='Put the cards on the table and swap them. Write each number you make.', ask='How many different numbers? How do you know you have found them all? Which digit is the tens digit in 38?',
    listen='"Swap the cards and I get a new number." The tens card matters most when comparing.')
add(id='L1-PV3', level=1, lesson=2, slot='bank', skill='Place value: three digit cards', tool='list',
    stem='Aisha has three digit cards: 2, 5 and 7. She picks two of the cards and lays them side by side.',
    parts=['a) Count the different 2-digit numbers she can lay down.', 'b) Write them from the smallest to the greatest.', 'c) Which of them is closest to 60?'],
    a='a) 6 numbers. b) 25, 27, 52, 57, 72, 75. c) 57 (3 away; 52 is 8 away and 72 is 12 away).',
    p=dict(cards=[2, 5, 7], target=60), ans=[6, '25 27 52 57 72 75', 57],
    say='Fix one card as the tens card, then list the numbers. Then fix the next card.', ask='What do you notice about the list when the tens card stays the same?', listen='A systematic list: 25, 27 / 52, 57 / 72, 75.')
add(id='L1-PV4', level=1, lesson=2, slot='bank', skill='Place value: odd and even digits, clues', tool='list',
    stem='Read each clue. Many answers may be right.',
    parts=['a) I am a 2-digit number. My tens digit is 3. My ones digit is odd and greater than 5. What numbers can I be?', 'b) I am a 2-digit number. My two digits are the same. My digits make a total of 12. What is my number?'],
    a='a) 37 and 39. b) 66.', p=dict(tens=3, lo=5, total=12), ans=['37 39', 66],
    say='Cross out the numbers that break a clue.', ask='Which clue helps most? Why did you stop at 39?', listen='Children check each clue in turn.')
add(id='L1-PV5', level=1, lesson=2, slot='bank', skill='Place value: compare by tens', tool='table',
    stem='Siti has 3 tens and 9 ones. Kumar has 4 tens and 2 ones.',
    parts=['a) Who has the greater number?', 'b) Write Kumar\'s number with a digit in each box: [ ][ ].'],
    a='a) Kumar (42 is greater than 39). b) 4 and 2.', p=dict(a=(3, 9), b=(4, 2)), ans=['Kumar', 42],
    say='Compare the tens first.', ask='Why does 1 more ten beat 9 ones?', listen='"Tens are worth more than ones, so look at the tens first."')

add(id='L1-MA1', level=1, lesson=2, slot='slide', group='g2', skill='Mental addition: pair numbers to make 10', tool='simpler',
    stem='Add in your head. Look for numbers that make 10.',
    parts=['a) Four jars hold 8, 3, 2 and 7 marbles. Find the total number of marbles.', 'b) 9 + 6 + 1 + 4 + 10 = [ ]'],
    a='a) 8 + 2 = 10 and 3 + 7 = 10, so 20 marbles. b) 9 + 1 = 10 and 6 + 4 = 10, so 10 + 10 + 10 = 30.',
    p=dict(a=[8, 3, 2, 7], b=[9, 6, 1, 4, 10]), ans=[20, 30],
    say='Do not add from left to right. Hunt for two numbers that make 10.', ask='Which two numbers did you join first? Is there another pair?', listen='"8 and 2 make 10." Accept any order that works.')
add(id='L1-MA2', level=1, lesson=2, slot='slide', group='g2', skill='Mental addition: add 9 by adding 10', tool='simpler',
    stem='Mei has 35 stickers. She gets 9 more.',
    parts=['a) 35 + 10 = [ ]', 'b) So 35 + 9 = [ ]', 'c) Find 52 + 19.'],
    a='a) 45. b) 44 (10 is 1 too many, so take 1 away). c) 52 + 20 = 72, then take away 1: 71.',
    p=dict(base=35, add=9, base2=52, add2=19), ans=[45, 44, 71],
    say='Adding 10 is easy. Then fix it.', ask='Why do we take 1 away? What is 19 close to?', listen='"9 is 1 less than 10" and "19 is 1 less than 20".')
add(id='L1-MA3', level=1, lesson=2, slot='bank', skill='Mental addition: make the next ten', tool='simpler',
    stem='Fill in the missing number.',
    parts=['a) 8 + 7 = 10 + [ ]', 'b) 38 + 5 = 40 + [ ]', 'c) 46 + 8 = 50 + [ ]'],
    a='a) 5. b) 3. c) 4.', p=dict(rows=[(8, 7, 10), (38, 5, 40), (46, 8, 50)]), ans=[5, 3, 4],
    say='Both sides of the equals sign must be the same.', ask='How many did you give to the first number to reach the next ten?', listen='"Take 2 from the 5 to make 40, 3 are left."')
add(id='L1-SYM1', level=1, lesson=2, slot='slide', group='g3', skill='Picture equations with two symbols', tool='guess',
    stem='Each shape stands for a number. The same shape is the same number.',
    parts=['a) Take line 2 away from line 1. What number is the triangle?', 'b) What number is the circle?'],
    fig=('sym', dict(lines=[['tri', '+', 'tri', '+', 'circ', '= 11'], ['tri', '+', 'circ', '= 8']])),
    a='a) Line 1 has one more triangle than line 2, and 11 is 3 more than 8, so triangle = 3. b) 3 + circle = 8, so circle = 5. Check: 3 + 3 + 5 = 11.',
    p=dict(l1=(2, 1, 11), l2=(1, 1, 8)), ans=[3, 5],
    say='Look for what is the same in both lines and what is different.', ask='What is the extra thing in line 1? How much extra is the total?', listen='"One more triangle, 3 more". Guess-and-check is fine: ask them to check both lines.')
add(id='L1-SYM2', level=1, lesson=2, slot='bank', skill='Picture equations with three symbols', tool='backwards',
    stem='Each shape stands for a number. Circle, square and star are three different numbers.',
    parts=['Line 1: circle + circle + square = 12', 'Line 2: circle + square = 7', 'Line 3: square + star = 5', 'a) circle = [ ]  b) square = [ ]  c) star = [ ]'],
    a='a) 5 (12 minus 7). b) 2 (5 + square = 7). c) 3 (2 + star = 5).', p=dict(c=5, s=2, t=3), ans=[5, 2, 3],
    say='Start with the two lines that look almost the same.', ask='Which line do you use first? Why?', listen='Line 1 minus line 2 gives the circle.')

add(id='L1-TWICE1', level=1, lesson=3, slot='slide', group='g1', skill='Bar model: twice as many', tool='draw',
    stem='Mei has 4 stickers. Ben has twice as many stickers as Mei.',
    parts=['a) How many stickers does Ben have?', 'b) How many stickers do Mei and Ben have in all?', 'c) Kumar has 3 more than Ben. How many does Kumar have?'],
    fig=('bars', dict(rows=[('Mei', 4, '#FFE49A'), ('Ben', 8, '#CFE3F5')])),
    a='a) 8 stickers. b) 12 stickers. c) 11 stickers.', p=dict(mei=4, times=2, more=3), ans=[8, 12, 11],
    say='Draw one block for each sticker. Ben has two rows of Mei\'s blocks.', ask='How did you show "twice as many" in your drawing?', listen='Two equal groups of 4. Ask for the number sentence: 4 + 4 = 8.')

add(id='L1-CAL1', level=1, lesson=4, slot='slide', group='g1', skill='Calendar: the week repeats every 7 days', tool='pattern',
    stem='Today is Wednesday.',
    parts=['a) What day will it be in 2 days?', 'b) What day will it be in 7 days?', 'c) What day will it be in 9 days?'],
    fig=('week', dict(start_idx=2)),
    a='a) Friday. b) Wednesday (a whole week later). c) Friday (7 days brings you back to Wednesday, then 2 more days).',
    p=dict(today=2, jumps=[2, 7, 9]), ans=['Friday', 'Wednesday', 'Friday'],
    say='The days of the week are a repeating pattern, like our colour patterns. The core has 7 days.', ask='What happens after Sunday? What does 7 days later always give?', listen='"It comes back to the same day." Children who count 9 one by one are fine; then ask them to find a shortcut.')
add(id='L1-CAL2', level=1, lesson=4, slot='bank', skill='Calendar: days later and days before', tool='pattern',
    stem='Mei goes to the library on Saturday.',
    parts=['a) How many days is it from one Saturday to the next Saturday?', 'b) Her friend goes 4 days after Mei. Which day is that?', 'c) Which day is 5 days before Sunday?'],
    a='a) 7 days. b) Wednesday. c) Tuesday.', p=dict(day=5, after=4, sunday=6, before=5), ans=[7, 'Wednesday', 'Tuesday'],
    say='Say the days as you count: Sunday, Monday, Tuesday, Wednesday.', ask='How do you count days before? Which way do you go?', listen='Counting backwards along the week.')

add(id='L1-AGE1', level=1, lesson=5, slot='slide', group='g1', skill='Ages: the gap between ages stays the same', tool='draw',
    stem='Ali is 6 years old. His sister is 9 years old.',
    parts=['a) How many years older is his sister?', 'b) In 3 years, Ali will be ___ years old. His sister will be ___ years old.', 'c) How many years older is his sister then?'],
    a='a) 3 years. b) Ali 9 years, sister 12 years. c) 3 years. The gap between their ages never changes.', p=dict(ali=6, sis=9, years=3), ans=[3, 9, 12, 3],
    say='Draw two bars for their ages. Both bars grow by the same amount.', ask='What stayed the same? What changed?', listen='"They both get 3 years older, so the gap stays 3."')
add(id='L1-AGE2', level=1, lesson=5, slot='bank', skill='Ages: work out an age from a gap', tool='backwards',
    stem='Siti is 5 years old. Her mum is 30 years old.',
    parts=['a) How old will Mum be when Siti is 8 years old?', 'b) How old was Mum when Siti was born?'],
    a='a) 33 years old (Siti is 3 years older, so Mum is too). b) 25 years old (Siti was 0, 5 years ago).', p=dict(siti=5, mum=30, siti_later=8), ans=[33, 25],
    say='Siti gets older by some years. So does Mum.', ask='How many years until Siti is 8? What happens to Mum\'s age in those years?', listen='Same number of years added to both.')

add(id='L1-CUBE1', level=1, lesson=7, slot='slide', group='g1', skill='Counting cubes in stacks, including hidden ones', tool='actout',
    stem='Cubes are stacked on a mat in two rows. There are no gaps under any stack.',
    parts=['a) How many cubes are in the back row?', 'b) How many cubes are in the front row?', 'c) How many cubes are there in all, including the ones you cannot see?'],
    fig=('iso', dict(heights=[[3, 2], [2, 1], [1, 1]], label='Three columns of cubes in two rows')),
    a='Back row: stacks of 3, 2 and 1 = 6 cubes. Front row: stacks of 2, 1 and 1 = 4 cubes. In all: 10 cubes.', p=dict(heights=[[3, 2], [2, 1], [1, 1]], back_j=0), ans=[6, 4, 10],
    say='Build it with real cubes if you can: stack by stack.', ask='Which cubes can you not see? How do you know they are there?', listen='"The stack at the back is 3 high, so there are cubes under the top one."')
add(id='L1-CUBE2', level=1, lesson=7, slot='bank', skill='Counting cubes: a staircase', tool='draw',
    stem='Ravi builds a staircase with cubes. The first step is 1 cube high, the next step is 2 cubes high, then 3, then 4.',
    parts=['a) Count the cubes in the staircase.', 'b) He builds a fifth step that is 5 cubes tall. How many extra cubes does he need?'],
    a='a) 10 cubes (1 + 2 + 3 + 4). b) 5 more cubes (15 in all).', p=dict(steps=4), ans=[10, 5],
    say='Draw the steps and count by columns.', ask='How can you add 1, 2, 3 and 4 quickly? Which pairs make 5?', listen='"1 + 4 and 2 + 3 both make 5."')

add(id='L1-CLK1', level=1, lesson=9, slot='slide', group='g1', skill='Time: o\'clock, half past and minutes in fives', tool='actout',
    stem='Look at the clock.',
    parts=['a) Write the time.', 'b) What time is it 1 hour later?', 'c) The minute hand moves from the 12 to the 4. Count in 5s. How many minutes pass?'],
    fig=('clock', dict(hour=7, minute=30)),
    a='a) 7:30 (half past 7). b) 8:30. c) 20 minutes (5, 10, 15, 20).', p=dict(h=7, m=30, to=4), ans=['7:30', '8:30', 20],
    say='Use a paper clock. Move the minute hand and count in fives.', ask='Where is the minute hand at half past? How many minutes from the 12 to the 6?', listen='Each number on the clock is 5 minutes.')
add(id='L1-CLK2', level=1, lesson=9, slot='bank', skill='Time: how long and when it ends', tool='table',
    stem='Read each question. Write the times like this: 2:45.',
    parts=['a) PE starts at 2:00 and lasts 45 minutes. When does it end?', 'b) Art starts at 9:30 and lasts 1 hour. When does it end?', 'c) Mei starts reading at 4:00 and stops at half past 4. How many minutes does she read?'],
    a='a) 2:45. b) 10:30. c) 30 minutes.', p=dict(start=(2, 0), minutes=45, start2=(9, 30), hours=1, start3=(4, 0), end3=(4, 30)), ans=['2:45', '10:30', 30],
    say='Draw a time line with the start and the end.', ask='Where is the hour hand at half past?', listen='Counting on from the start in chunks (30 minutes, then 15).')

# =====================================================================  LEVEL 2
add(id='L2-PAIR1', level=2, lesson=2, slot='slide', group='g1', skill='Pairing sums: first and last make the same total', tool='simpler',
    stem='Add these numbers. Look for pairs that make the same total.',
    parts=['a) 4 + 9 + 14 + 19 + 24 + 29 + 34 + 39 = [ ]', 'b) Add all the whole numbers from 11 to 20.'],
    a='a) 4 + 39 = 43, 9 + 34 = 43, 14 + 29 = 43, 19 + 24 = 43: four pairs of 43 = 172. b) 11 + 20 = 31, and there are 5 pairs: 155.',
    p=dict(a=dict(start=4, step=5, n=8), b=dict(start=11, step=1, n=10)), ans=[172, 155],
    say='Write the list forwards, then write it again backwards underneath. Add the two numbers that sit on top of each other.', ask='What do you notice about the first and the last? And the second and the second last? How many pairs are there?', listen='"Every pair makes the same total." Check that they count the pairs, not the numbers.')
add(id='L2-PAIR2', level=2, lesson=2, slot='bank', skill='Pairing sums: save every day', tool='simpler',
    stem='Add the numbers.',
    parts=['a) 40 + 80 + 120 + 160 + 200 + 240 = [ ]', 'b) Mei saves $5 on day 1, $10 on day 2, $15 on day 3, and so on, up to $50 on day 10. How much has she saved after 10 days?'],
    a='a) 40 + 240 = 280 and there are 3 pairs: 840. b) 5 + 50 = 55 and there are 5 pairs: $275.', p=dict(a=dict(start=40, step=40, n=6), b=dict(start=5, step=5, n=10)), ans=[840, 275],
    say='Try something simpler: do 4 numbers first.', ask='How many pairs? Does it still work if there is an odd number of numbers?', listen='Pairs times total.')
add(id='L2-LETTER1', level=2, lesson=2, slot='slide', group='g1', skill='Letter-digit sums', tool='guess',
    stem='Each letter stands for one digit. Different letters stand for different digits. Find A, B and C.',
    fig=('letters', dict(top='A8', bot='C9', res='BC')),
    parts=['A = [ ]    B = [ ]    C = [ ]'],
    a='A = 1, B = 9, C = 7 (18 + 79 = 97). Ones: 8 + 9 = 17, so C = 7 and carry 1. Tens: A + 7 + 1 = B, so A + 8 = B. A digit stops at 9, so only A = 1 and B = 9 fit.', p=dict(top='A8', bot='C9', res='BC'), ans=[1, 9, 7],
    say='Start with the ones column, just like the missing-digit sums.', ask='What must 8 + 9 make in the ones? What is the carry? Which letter is it?', listen='The ones column shows C = 7 and a carry. Then test the tens. Ask them to check the whole sum.')
add(id='L2-SEQ1', level=2, lesson=4, slot='slide', group='g1', skill='Sequences: the gap grows by 1 each time', tool='table',
    stem='Ali writes a pattern: 6, 7, 9, 12, 16, __, __',
    parts=['a) Write the next two numbers.', 'b) Will 40 be in the pattern?'],
    fig=('seq', dict(terms=[6, 7, 9, 12, 16, 0, 0], gaps=[1, 2, 3, 4, None, None], blanks_from=5)),
    a='a) 21 and 27 (the gaps are 1, 2, 3, 4, 5, 6). b) No: the pattern goes 27, 34, 42 and jumps over 40.', p=dict(start=6, first_gap=1, grow=1, n=9, test=40), ans=[21, 27, 'no'],
    say='This pattern does not add the same number. Make a table and put the gaps in a row of their own.', ask='What are the gaps? How does the gap change? What is the next gap?', listen='"The gap goes up by 1."')
add(id='L2-SEQ2', level=2, lesson=4, slot='slide', group='g1', skill='Sequences: add the two numbers before', tool='pattern',
    stem='Mei writes a pattern: 2, 4, 6, 10, 16, __, __',
    parts=['a) Write the next two numbers.', 'b) What is the 9th number?'],
    a='a) 26 and 42 (6 + 10 = 16, 10 + 16 = 26, 16 + 26 = 42). b) 110: the numbers are 2, 4, 6, 10, 16, 26, 42, 68, 110.', p=dict(start=[2, 4], n=9), ans=[26, 42, 110],
    say='Try the gap row. Does it look like the numbers?', ask='What is 2 + 4? What is 4 + 6? What would the next number be?', listen='"Add the two numbers before." Ask them to write the whole list to the 9th number.')
add(id='L2-SEQ3', level=2, lesson=4, slot='bank', skill='Sequences: two rules take turns', tool='pattern',
    stem='Start at 20. Add 10, then take away 4, then add 10, then take away 4, and keep going.',
    parts=['a) Write the first 7 numbers.', 'b) What is the 9th number?'],
    a='a) 20, 30, 26, 36, 32, 42, 38. b) 44.', p=dict(start=20, rules=[10, -4], n=9), ans=['20 30 26 36 32 42 38', 44],
    say='Treat each pair of steps as one jump of 6.', ask='What do the numbers in odd places do? In even places?', listen='"Every two steps it goes up 6."')
add(id='L2-SEQ4', level=2, lesson=4, slot='bank', skill='Sequences: the gap gets smaller', tool='table',
    stem='Siti counts down: 100, 90, 81, 73, 66, __, __',
    parts=['a) Write the next two numbers.', 'b) What is the gap each time?'],
    a='a) 60 and 55. b) The gaps are 10, 9, 8, 7, 6, 5: each gap is 1 less than the one before.', p=dict(start=100, first_gap=10, shrink=1, n=7), ans=[60, 55],
    say='Draw a table with a row for the gap.', ask='What is the next gap? How do you know?', listen='"The gaps go down 1 each time."')

add(id='L2-AGE1', level=2, lesson=5, slot='slide', group='g1', skill='Ages: the gap never changes', tool='draw',
    stem='Read each story. Draw a bar for each person.',
    parts=['a) Ali is 4 years older than his sister. Their ages add up to 20. How old is each?', 'b) Mum is 28 years older than Mei. Mei is 7 now. How old will each be in 5 years?'],
    a='a) Take away the 4 extra years: 16 left, shared equally is 8. Sister 8, Ali 12 (8 + 12 = 20). b) Mei will be 12; Mum is 35 now, so 40 in 5 years. The gap is still 28.',
    p=dict(gap=4, total=20, mgap=28, mei=7, years=5), ans=[8, 12, 12, 40],
    say='For part a, take away the extra years first, then share what is left. The same take-away-the-extra idea as the worksheet.', ask='Which person is older? By how many years? What do you do with the extra 4?', listen='"Both get older at the same speed, so the gap stays." For a), a Guess and check that tests both clues is also fine.')
add(id='L2-AGE2', level=2, lesson=5, slot='bank', skill='Ages: when will it happen?', tool='table',
    stem='Ravi is 9 years old. Mei is 5 years old.',
    parts=['a) Ravi will be 12 years old in ___ years.', 'b) Mei will be ___ years old then.', 'c) Ravi was ___ years old when Mei was born.'],
    a='a) 3 years. b) 8 years old. c) 4 years old.', p=dict(ravi=9, mei=5, ravi_later=12), ans=[3, 8, 4],
    say='Make a small table: year, Ravi, Mei.', ask='What number stays the same in every row?', listen='The gap of 4.')

add(id='L2-CORNER1', level=2, lesson=8, slot='slide', group='g1', skill='Cubes in the corner of a room', tool='actout',
    stem='Cubes are stacked in the corner of a room, touching both walls. The bottom layer is 3 rows of 3. The next layer is 2 rows of 2. The top layer is 1 cube.',
    parts=['a) The bottom layer has ___ cubes.', 'b) The whole stack has ___ cubes.', 'c) ___ cubes touch the left wall.'],
    fig=('iso', dict(s=52, heights=[[3, 2, 1], [2, 2, 1], [1, 1, 1]], walls=True, label='Cubes stacked in the corner of a room')),
    a='a) 9. b) 14 (9 + 4 + 1). c) 6 (3 in the bottom layer, 2 in the next and 1 on top).', p=dict(layers=[3, 2, 1]), ans=[9, 14, 6],
    say='Build it layer by layer with cubes, then look at one wall.', ask='Which cubes touch the wall in the bottom layer? In the next layer?', listen='"3, then 2, then 1."')
add(id='L2-CORNER2', level=2, lesson=8, slot='bank', skill='Cubes in a corner: bigger', tool='table',
    stem='A cube corner has layers of 4 by 4, 3 by 3, 2 by 2 and 1 cube.',
    parts=['a) How many cubes are there in all?', 'b) How many cubes touch the floor?'],
    a='a) 30 (16 + 9 + 4 + 1). b) 16.', p=dict(layers=[4, 3, 2, 1]), ans=[30, 16],
    say='Make a table: layer, size, cubes.', ask='What pattern do the layer numbers make?', listen='Square numbers: 16, 9, 4, 1.')

add(id='L2-PIC1', level=2, lesson=9, slot='slide', group='g1', skill='Picture equations: shapes stand for numbers', tool='guess',
    stem='Each shape stands for a number. The same shape is the same number.',
    parts=['a) triangle = [ ]    b) circle = [ ]    c) square = [ ]', 'd) triangle + circle + square = [ ]'],
    fig=('sym', dict(lines=[['tri', '+', 'tri', '+', 'tri', '= 27'], ['tri', '+', 'circ', '+', 'circ', '= 21'], ['circ', '+', 'sq', '= 13']])),
    a='a) 9 (27 split into 3 equal parts). b) 6 (21 - 9 = 12, shared by 2). c) 7 (13 - 6). d) 22.', p=dict(l1=(3, 0, 0, 27), l2=(1, 2, 0, 21), l3=(0, 1, 1, 13)), ans=[9, 6, 7, 22],
    say='Find the line that tells you the most. Which shape can you find first?', ask='Which line did you use first and why? How can you check?', listen='Three triangles = 27 is the start. Then use it in line 2.')
add(id='L2-PIC2', level=2, lesson=9, slot='bank', skill='Picture equations: exchange chain', tool='table',
    stem='2 apples weigh the same as 1 melon. 3 melons weigh the same as 1 pumpkin.',
    parts=['a) How many apples weigh the same as 1 pumpkin?', 'b) 1 pumpkin and 2 melons weigh the same as how many apples?'],
    a='a) 6 apples (3 melons, each 2 apples). b) 10 apples (6 + 4).', p=dict(apples_per_melon=2, melons_per_pumpkin=3, extra_melons=2), ans=[6, 10],
    say='Draw it as a chain: apple, melon, pumpkin.', ask='How many apples for one melon? For three melons?', listen='"Multiply along the chain."')
add(id='L2-CAL1', level=2, lesson=9, slot='slide', group='g2', skill='Calendar: weeks and days', tool='pattern',
    stem='Today is Thursday.',
    parts=['a) What day will it be in 3 weeks?', 'b) What day will it be in 25 days?', 'c) What day will it be in 30 days?'],
    fig=('week', dict(start_idx=3)),
    a='a) Thursday (3 weeks is 21 days, 3 full cycles). b) Monday (25 = 3 weeks and 4 days; Thursday + 4 days is Monday). c) Saturday (30 = 4 weeks and 2 days).', p=dict(today=3, jumps=[21, 25, 30]), ans=['Thursday', 'Monday', 'Saturday'],
    say='The week is a repeating pattern of 7. Take out whole weeks first.', ask='How many whole weeks fit into 25 days? How many days are left over?', listen='"Remainder" language: 25 days is 3 weeks and 4 days.')
add(id='L2-CAL2', level=2, lesson=9, slot='bank', skill='Calendar: dates in a month', tool='table',
    stem='A month has 30 days. The 1st of the month is a Tuesday.',
    parts=['a) Which dates are Tuesdays?', 'b) What day is the 30th?', 'c) What day is the 1st of next month?'],
    a='a) 1, 8, 15, 22 and 29. b) Wednesday. c) Thursday.', p=dict(first=1, days=30), ans=['1 8 15 22 29', 'Wednesday', 'Thursday'],
    say='Write the dates in rows of 7 under the days of the week.', ask='What do you notice about the Tuesday dates?', listen='They go up by 7.')

add(id='L2-POST1', level=2, lesson=10, slot='slide', group='g1', skill='Posts and gaps', tool='draw',
    stem='A straight path is 20 m long. A lamp post stands at the start, at the end, and every 5 m in between.',
    parts=['a) How many lamp posts are there?', 'b) A fence has 7 posts in a straight line, 3 m apart. How long is the fence?'],
    a='a) 5 posts (4 gaps of 5 m). b) 18 m (6 gaps of 3 m).', p=dict(length=20, step=5, posts=7, step2=3), ans=[5, 18],
    say='Draw a dot for each post and a line for each gap.', ask='Are there more posts or more gaps? Why?', listen='"One more post than gaps" in a line.')
add(id='L2-QUEUE1', level=2, lesson=10, slot='slide', group='g1', skill='Places in a queue', tool='draw',
    stem='Counting from the front of a queue, Ravi is number 5. Counting from the back, he is number 4.',
    parts=['Find the number of children in the queue.'],
    a='8 children. Ravi is counted twice (5 + 4 = 9), so take 1 away.', p=dict(front=5, back=4), ans=[8],
    say='Draw the queue and mark Ravi.', ask='Who is in front of Ravi? Behind him? Did you count Ravi twice?', listen='"Ravi is counted in both numbers."')
add(id='L2-POST2', level=2, lesson=10, slot='bank', skill='Posts and gaps: round a pond', tool='draw',
    stem='8 lamps stand round a pond, the same distance apart. It is 4 m from one lamp to the next.',
    parts=['a) How many gaps are there?', 'b) How long is the path all the way round?'],
    a='a) 8 gaps. b) 32 m.', p=dict(lamps=8, step=4), ans=[8, 32],
    say='In a ring there is no end post.', ask='Is it the same as a straight path? Why not?', listen='Gaps equal lamps in a ring.')
add(id='L2-WORST1', level=2, lesson=10, slot='slide', group='g2', skill='Worst case: how many to be sure?', tool='actout',
    stem='A bag has 6 red counters and 4 blue counters. You take counters out without looking.',
    parts=['a) How many must you take to be sure you have 2 red counters?', 'b) How many must you take to be sure you have one counter of each colour?'],
    a='a) 6 (the worst case is 4 blue first, then 2 red). b) 7 (the worst case is all 6 red first, then 1 blue).', p=dict(red=6, blue=4, need_red=2), ans=[6, 7],
    say='Be unlucky on purpose. What is the worst that can happen?', ask='What is the unluckiest draw? What counter must come next?', listen='"The unlucky draw is all of the other colour first."')
add(id='L2-WORST2', level=2, lesson=10, slot='bank', skill='Worst case: socks', tool='actout',
    stem='A drawer has 4 black socks, 4 white socks and 4 grey socks. You take socks out without looking.',
    parts=['a) How many socks must you take to be sure you have a matching pair?', 'b) How many socks must you take to be sure you have 2 black socks?'],
    a='a) 4 (one of each colour is 3 socks; the 4th must match). b) 10 (4 white and 4 grey first, then 2 black).', p=dict(counts=[4, 4, 4]), ans=[4, 10],
    say='Act it out with coloured counters.', ask='What is the most socks you can take with no pair?', listen='"One of each colour, then one more."')

# =====================================================================  LEVEL 3
add(id='L3-PAIR1', level=3, lesson=2, slot='slide', group='g1', skill='Pairing: make tens and hundreds', tool='simpler',
    stem='Add these in your head. Look for pairs that make a ten or a hundred.',
    parts=['a) 8 + 7 + 2 + 3 + 6 + 4 + 9 + 1 = [ ]', 'b) 260 + 140 + 380 + 120 + 410 + 90 = [ ]'],
    a='a) 8 + 2, 7 + 3, 6 + 4 and 9 + 1 each make 10, so 40. b) 260 + 140 = 400, 380 + 120 = 500, 410 + 90 = 500, so 1400.', p=dict(a=[8, 7, 2, 3, 6, 4, 9, 1], b=[260, 140, 380, 120, 410, 90]), ans=[40, 1400],
    say='Do not add left to right. Hunt for partners.', ask='Which numbers are partners? How did you find the partner of 260?', listen='"260 + 140 = 400, because 60 + 40 = 100."')
add(id='L3-SERIES1', level=3, lesson=2, slot='slide', group='g1', skill='Series sums: first plus last', tool='pattern',
    stem='Ali adds a list of numbers that go up by the same step: 3 + 10 + 17 + 24 + 31 + 38 + 45 + 52',
    parts=['a) What is the first number plus the last number?', 'b) How many pairs are there?', 'c) What is the total?'],
    a='a) 3 + 52 = 55. b) 4 pairs (8 numbers). c) 4 x 55 = 220.', p=dict(start=3, step=7, n=8), ans=[55, 4, 220],
    say='Write the list twice: forwards, then backwards underneath.', ask='What is the second number plus the second last? What do you notice?', listen='"Every pair makes 55."')
add(id='L3-PAIR2', level=3, lesson=2, slot='bank', skill='Series sums: a long list', tool='simpler',
    stem='Add the numbers.',
    parts=['a) 1 + 2 + 3 + ... + 40 = [ ]', 'b) Kumar reads 4 pages on day 1, then 3 more pages each day than the day before: 4, 7, 10 and so on. How many pages has he read after 7 days?'],
    a='a) 1 + 40 = 41, 20 pairs, 820. b) The days read 4, 7, 10, 13, 16, 19, 22. First plus last is 26; 3 pairs and a middle number 13: 78 + 13 = 91.', p=dict(a=dict(start=1, step=1, n=40), b=dict(start=4, step=3, n=7)), ans=[820, 91],
    say='If there is an odd number of numbers, one number is left in the middle.', ask='How many pairs? What is left over?', listen='The middle number is half of first plus last.')
add(id='L3-DIV3', level=3, lesson=3, slot='slide', group='g1', skill='Divisibility: the digit sum test for 3', tool='pattern',
    stem='Write the first ten numbers in the 3 table, from 3 up to 30.',
    parts=['a) Add the digits of each number. What do you notice?', 'b) Is 483 in the 3 table? Is 725?'],
    a='a) The digit sums are 3, 6, 9, 3, 6, 9, 3, 6, 9, 3: always a number from the 3 table. b) 483: 4 + 8 + 3 = 15, which is in the 3 table, so yes (3 x 161). 725: 7 + 2 + 5 = 14, which is not, so no.', p=dict(tests=[483, 725]), ans=['yes', 'no'],
    say='Last lesson we looked at the digit sums of the 9 table. Do the same for the 3 table.', ask='What do the digit sums have in common? Does the test work for 30? For 483?', listen='"The digit sum is in the 3 table". Check by dividing: 483 / 3.')
add(id='L3-DIV6', level=3, lesson=3, slot='slide', group='g1', skill='Divisibility: 2 and 3 means 6', tool='table',
    stem='A number is in the 2 table and in the 3 table.',
    parts=['a) Which other table is it in?', 'b) Is 534 in the 6 table? Is 357?'],
    a='a) The 6 table. b) 534 is even and its digit sum is 12, so yes (6 x 89). 357 is odd, so no.', p=dict(tests=[534, 357]), ans=[6, 'yes', 'no'],
    say='List the first multiples of 2 and of 3 and circle the numbers in both.', ask='What do 6, 12, 18 have in common? Why must a number in both tables be in the 6 table?', listen='"Even and in the 3 table".')
add(id='L3-RANGE1', level=3, lesson=3, slot='slide', group='g2', skill='Counting multiples in a range', tool='simpler',
    stem='Ali counts the numbers in the 4 table from 50 to 150.',
    parts=['a) How many numbers in the 4 table are there up to 150?', 'b) How many are there up to 49?', 'c) How many are there from 50 to 150?'],
    a='a) 37 (150 / 4 is 37 remainder 2). b) 12 (49 / 4 is 12 remainder 1). c) 37 - 12 = 25.', p=dict(k=4, lo=50, hi=150), ans=[37, 12, 25],
    say='Count to the top, then take away the ones that come too early.', ask='How do you find how many 4s fit into 150? Which numbers did you take away?', listen='"Divide by 4, ignore the remainder".')
add(id='L3-RANGE2', level=3, lesson=3, slot='bank', skill='Counting multiples in a range', tool='simpler',
    stem='Answer each question.',
    parts=['a) Count the numbers in the 3 table from 100 to 200.', 'b) Count the numbers in the 6 table up to 100.', 'c) Up to 60, count the numbers that are in both the 2 table and the 5 table.'],
    a='a) 33 (102 to 198). b) 16. c) 6 (10, 20, 30, 40, 50, 60: the 10 table).', p=dict(q=[(3, 100, 200), (6, 1, 100), (10, 1, 60)]), ans=[33, 16, 6],
    say='Count up to the top, then take away.', ask='Why is c the 10 table?', listen='2 and 5 together make 10.')

add(id='L3-TOP1', level=3, lesson=7, slot='slide', group='g1', skill='Spatial: reading a top view with heights', tool='actout',
    stem='Cubes are stacked on squares. Each number shows how many cubes are stacked on that square.',
    parts=['a) How many cubes are there in all?', 'b) Look from the front. In each column you see the tallest stack. How many squares make the front view?'],
    fig=('heights', dict(rows=[[2, 3, 1], [1, 2, 2]])),
    a='a) 11 cubes. b) 7 squares (the tallest stacks in the columns are 2, 3 and 2).', p=dict(rows=[[2, 3, 1], [1, 2, 2]]), ans=[11, 7],
    say='Build it with cubes, then look at it from the front, at table level.', ask='Which cubes do you not see from the front? What do you look for in each column?', listen='"Only the tallest stack in each column matters from the front."')
add(id='L3-TOP2', level=3, lesson=7, slot='bank', skill='Spatial: side view', tool='actout',
    stem='A top view has 3 rows and 2 columns. The rows, from the back to the front, are 3 2, then 1 1, then 2 3.',
    parts=['a) How many cubes are there in all?', 'b) Look from the right side. You see the tallest stack in each row. How many squares make the side view?'],
    a='a) 12 cubes. b) 7 squares (3, 1 and 3).', p=dict(rows=[[3, 2], [1, 1], [2, 3]]), ans=[12, 7],
    say='Draw the top view as a grid.', ask='Which way are you looking?', listen='Rows, not columns, from the side.')

add(id='L3-FACE1', level=3, lesson=10, slot='slide', group='g1', skill='Picture patterns: each feature has its own cycle', tool='table',
    stem='The faces keep going in the same way.',
    parts=['a) What does face 9 look like?', 'b) What does face 14 look like?', 'c) What is the first face after face 1 that looks exactly like face 1?'],
    fig=('faces', dict(n=6)),
    a='The eyes repeat every 2 faces (open, closed). The mouth repeats every 3 faces (smile, flat, open). a) Face 9: open eyes, open mouth. b) Face 14: closed eyes, flat mouth. c) Face 7 (6 is the first place where both cycles start again).', p=dict(eyes=['open', 'closed'], mouth=['smile', 'flat', 'open'], q=[9, 14]), ans=['open open', 'closed flat', 7],
    say='Name each feature. Make a table with a row for the eyes and a row for the mouth.', ask='How often do the eyes repeat? The mouth? When do they both start again?', listen='"Two cycles at the same time."')
add(id='L3-POSTS1', level=3, lesson=10, slot='slide', group='g2', skill='Gaps and posts, both sides of a path', tool='draw',
    stem='A path is 24 m long. Lanterns stand on both sides of the path, one every 3 m. There is a lantern at both ends of each side.',
    parts=['How many lanterns are there altogether?'],
    fig=('path', dict(length_label='24 m', gap_label='3 m')),
    a='24 / 3 = 8 gaps, so 9 lanterns on one side. Two sides: 18 lanterns.', p=dict(length=24, step=3, sides=2), ans=[18],
    say='Do one side first. Count the gaps, then the lanterns.', ask='How many gaps on one side? One more lantern than gaps, so how many? Then what?', listen='"8 gaps, 9 lanterns, doubled."')
add(id='L3-RECT1', level=3, lesson=10, slot='slide', group='g2', skill='Counting rectangles by size', tool='list',
    stem='A window has 3 panes across and 2 panes up and down. Count every rectangle you can find (squares count too).',
    parts=['How many rectangles are there? Count them by size.'],
    fig=('window', dict(cols=3, rows=2)),
    a='1 by 1: 6. 2 across by 1: 4. 3 across by 1: 2. 1 across by 2 up: 3. 2 by 2: 2. 3 across by 2 up: 1. In all: 18.', p=dict(cols=3, rows=2), ans=[18],
    say='Count by size. Make a table: size, how many.', ask='How many of the smallest size? Of the next size? How do you know you have not missed any?', listen='A table by size.')
add(id='L3-CHAIN1', level=3, lesson=4, slot='bank', skill='Balance chains', tool='draw',
    stem='1 melon balances 3 pears. 1 pear balances 4 plums.',
    parts=['a) How many plums balance 1 melon?', 'b) How many plums balance 2 melons?', 'c) Which is the heaviest, and which is the lightest: melon, pear or plum?'],
    a='a) 12 plums. b) 24 plums. c) The melon is the heaviest and the plum is the lightest.', p=dict(pears=3, plums=4, melons=2), ans=[12, 24, 'melon plum'],
    say='Draw a balance for each sentence.', ask='How many plums for 3 pears?', listen='Multiply along the chain.')
add(id='L3-SHARE1', level=3, lesson=2, slot='bank', skill='Shape sums: a shared centre', tool='guess',
    stem='Draw 3 lines that cross in the middle. Each line has 3 circles: one at each end and one in the centre. The centre circle is shared by all 3 lines (7 circles in all).',
    parts=['Use the numbers 1 to 7 once each so that each line adds up to 12. 4 goes in the centre. 7 is at one end of a line. What number is at the other end of that line?'],
    a='1 (7 + 4 + 1 = 12). The other lines use 2 and 6, and 3 and 5.', p=dict(centre=4, total=12, end=7), ans=[1],
    say='The centre counts for every line. How much is left for the two ends of each line?', ask='What do the two ends of a line add up to?', listen='"8 for the ends": the pairs are 1 and 7, 2 and 6, 3 and 5.')
add(id='L3-OP1', level=3, lesson=10, slot='bank', skill='Number patterns: find a secret rule', tool='table',
    stem='A machine uses a secret rule for the star sign. 2 star 3 = 8. 4 star 1 = 8. 5 star 2 = 15. 3 star 3 = 12.',
    parts=['Find 6 star 4.'],
    a='30. The rule is: multiply the first number by one more than the second number (2 x 4 = 8, 4 x 2 = 8, 5 x 3 = 15, 3 x 4 = 12, so 6 x 5 = 30).', p=dict(rows=[(2, 3, 8), (4, 1, 8), (5, 2, 15), (3, 3, 12)], q=(6, 4)), ans=[30],
    say='Make a table of the numbers going in and the number coming out.', ask='What do you try first? Does your rule work for every row?', listen='Test the rule on all four examples.')
add(id='L3-BOUND1', level=3, lesson=10, slot='bank', skill='Smallest and greatest possible; impossible totals', tool='list',
    stem='Mei picks 3 different number cards from 1 to 9 and adds them.',
    parts=['a) Find her smallest possible total.', 'b) Find her greatest possible total.', 'c) Can she make a total of 25? How do you know?'],
    a='a) 6 (1 + 2 + 3). b) 24 (7 + 8 + 9). c) No, 25 is greater than the greatest total, 24.', p=dict(lo=1, hi=9, k=3, test=25), ans=[6, 24, 'no'],
    say='Think about the smallest cards and then the greatest cards.', ask='How do you know you cannot go higher than 24?', listen='Reasoning with the greatest three cards.')
add(id='L3-STICK1', level=3, lesson=10, slot='bank', skill='Most digits from a fixed number of sticks', tool='list',
    stem='Ravi makes digits from sticks. Sticks needed for each digit: 1 needs 2; 7 needs 3; 4 needs 4; 2, 3 and 5 need 5 each; 0, 6 and 9 need 6 each; 8 needs 7. Ravi has exactly 7 sticks.',
    parts=['a) What is the most digits he can make?', 'b) What is the greatest number he can make with that many digits?'],
    a='a) 3 digits (each digit needs at least 2 sticks, and 4 digits need at least 8). b) 711 (the only way to use exactly 7 sticks with 3 digits is 2 + 2 + 3: the digits 1, 1 and 7).', p=dict(sticks=7, cost={'1': 2, '7': 3, '4': 4, '2': 5, '3': 5, '5': 5, '0': 6, '6': 6, '9': 6, '8': 7}), ans=[3, 711],
    say='Which digit costs the least? Start there.', ask='Why can he not make 4 digits? Which digits fit in 7 sticks with 3 digits?', listen='A systematic check of costs.')

if __name__ == '__main__':
    from collections import Counter
    print(len(ITEMS), Counter((i['level'], i['slot']) for i in ITEMS))
