// Shared content for the Math Inquirers Holiday Program (Primary 1)
module.exports = {
  program: 'Math Inquirers Holiday Program',
  slogan: 'Notice it. Test it. Explain why.',
  lessons: [
    {
      n: 1, week: 1, session: 'A', title: 'Count with the Frog', topic: 'Number Patterns',
      objective: 'Skip count in 2s, 3s and 5s; find and state an add or take-away rule; notice numbers that both counting patterns share.',
      skills: 'Pattern spotting, rule finding, generalising',
      materials: 'Paper number strip 0 to 50 (or floor tape), counters, two crayons.',
      online: 'Slide number line the tutor can mark on; each child uses a paper strip and a pencil.',
      warmup: 'Skip-count stomp: count in 2s, 5s and 3s as a class. Stomp on the numbers in the count, whisper the rest.',
      explore: 'Pairs hop a counter along the number strip: frog 1 in 4s, frog 2 in 5s. Mark where each lands. Which numbers do both frogs land on?',
      mini: 'Build the table on the board: jump 1, 2, 3 … and where it lands. Name the rule ("add 4"). Ask what stays the same and what changes.',
      share: 'Why do the numbers both frogs land on all end in 0?',
      exit: { q: 'Next two numbers: 7, 10, 13, 16, __, __. What is the rule?', a: '19, 22. Add 3.' },
      mistakes: ['Counting the numbers in between instead of the hops (4 to 7 counted as 2).', 'Writing "add 3" when the numbers go down (take away 3).', 'Restarting the count instead of adding to the last number.'],
      extension: 'Pupils invent a rule (start at 1, add 6) and swap with a partner to find it.',
      key: [
        ['Q1', '(a) 8, 10, 14  (b) 15, 25, 35  (c) 9, 15'],
        ['Q2', '(a) 16, 19; add 3  (b) 18, 15; take away 3  (c) 18, 22; add 4'],
        ['Q3', 'Frog 1 lands on 4, 8, 12, 16, 20. Frog 2 lands on 5, 10, 15, 20. Both: 20.'],
        ['Q4', '(a) 10, 20, 30, 40, 50  (b) They all end in 0. We say them when we count in 10s.'],
        ['Q5', 'Stickers: 2, 5, 8, 11, 14, 17, 20, 23, 26, 29. (a) Box 10 has 29. (b) Even, odd, even, odd: they alternate.'],
        ['Stretch slide', '1) Yes to 39, no to 40  2) 22 does not belong; it should be 20  3) Add 4; the 1st number is 3']
      ]
    },
    {
      n: 2, week: 1, session: 'B', title: 'Number Bond Inquiry', topic: 'Number Bonds',
      objective: 'Know the bonds of 10, use them to find bonds of 20, balance equations, and reason about missing numbers.',
      skills: 'Structure of numbers, systematic listing, reasoning about equality, guess and check',
      materials: 'Ten-frames, red and yellow counters, a cup, a paper triangle with 6 circles.',
      online: 'Slide ten-frame with a hidden-counter reveal; each child uses 10 coins or paper pieces of two colours.',
      warmup: 'Hidden counters: show 10 counters, hide some under a cup. How many are under the cup? Repeat with new splits.',
      explore: 'Pairs make 10 on a ten-frame with two colours in as many ways as they can and record each pair. Then ask: how do you know you have them all?',
      mini: 'List the pairs in order: 0+10, 1+9, 2+8 … Notice one goes up by 1 as the other goes down by 1. Link to 20: 6+4=10, so 16+4=20.',
      share: 'Mei says 4 + 4 = 8 + 1. How do you check? What does "=" really mean?',
      exit: { q: '10 = 6 + __    20 = 13 + __', a: '4 and 7.' },
      mistakes: ['Reading "=" as "the answer comes next" (5 + 3 = 4 + __ answered 8).', 'Counting 3+7 and 7+3 as different bonds when asked for different pairs.', 'Magic triangle: trying numbers at random instead of looking at the corners.'],
      extension: 'Make every side of the magic triangle total 11 (one way: corners 2, 4, 6 with 5, 1, 3 between them). Then ask: can every side total 13? No: the biggest possible side total is 12, with 4, 5, 6 in the corners.',
      key: [
        ['Q1', '(a) 7  (b) 4  (c) 2  (d) 5  (e) 10'],
        ['Q2', '(a) 2+8, 3+7, 4+6, 5+5  (b) The second number goes down by 1  (c) 6 different bonds'],
        ['Q3', '(a) 20 and 20  (b) 20 and 20  (c) 8, 11, 5'],
        ['Q4', '(a) 4  (b) 4  (c) 6  (d) 2  (e) No. 4 + 4 = 8 but 8 + 1 = 9.'],
        ['Q5', '(a) Sides of 9: corners 1, 2, 3 (any order). Between 1 and 2: 6. Between 2 and 3: 4. Between 3 and 1: 5.  (b) Sides of 10: corners 1, 3, 5. Between 1 and 3: 6. Between 3 and 5: 2. Between 5 and 1: 4.'],
        ['Q6', '4 and 6.  Challenge: 4 and 8.'],
        ['Stretch slide', '1) 10 and 16  2) 8  3) 6 pairs']
      ]
    },
    {
      n: 3, week: 2, session: 'A', title: 'Let’s Plan the Fruit Party', topic: 'Picture Graphs',
      objective: 'Read and build a picture graph, compare and total data, and judge what a class vote can and cannot tell us.',
      skills: 'Data reading, comparing, sampling awareness, weighing other factors',
      materials: 'Sticky dots, 5 fruit pictures on the wall, counters.',
      online: 'Poll on the slide (thumbs and chat) and a shared graph the tutor builds live.',
      warmup: 'Quick vote: each child votes for ONE fruit with a sticky dot (online: type it in chat).',
      explore: 'Pairs turn the class vote into a picture graph with one counter per child, then read it aloud: most, fewest, same, how many more.',
      mini: 'Key = 1 child. Count by 5s to total quickly. If everyone had one vote, the total is the number of children.',
      share: 'Would the Primary 6 pupils choose the same fruit? What else should the teacher think about before buying?',
      exit: { q: 'Dogs 6, cats 4, fish 3. How many pets altogether?', a: '13' },
      mistakes: ['Writing 8 + 3 instead of finding the difference (8 − 3).', 'Naming only one of two tied fruits.', 'Saying "Yes" to the whole school because their class chose it.'],
      extension: 'Draw their own picture graph from the Part B tally using one symbol per child.',
      key: [
        ['Q1', 'Orange'], ['Q2', 'Grape'], ['Q3', '5 more (8 − 3)'], ['Q4', 'Banana and watermelon (5 each)'],
        ['Q5', '27 children (6 + 5 + 8 + 3 + 5)'],
        ['Q6', '(a) No.  (b) Only our class voted. Other classes may like different fruits.'],
        ['Q7', 'Accept sensible ideas: cost, how many are needed, easy to share, keeps fresh, messy to eat, any child who cannot eat it.'],
        ['Part B', 'Depends on the class vote. Q9: different children like different things, and a small group may not match a whole school.'],
        ['Stretch slide', '1) 6 more  2) Orange 7, apple wins with 8  3) 9']
      ]
    },
    {
      n: 4, week: 2, session: 'B', title: 'Pattern Inquiry', topic: 'Repeating and Growing Patterns',
      objective: 'Extend a repeating pattern and predict far places using the pattern core; extend a growing stick pattern and work backwards from a total.',
      skills: 'Core identification, prediction by multiples, tables, working backwards',
      materials: '21 straws, lolly sticks or paper strips per pair (never real matches), shape cut-outs.',
      online: 'Drawing on paper or screen; children use straws, lolly sticks, paper strips or pencils at home (never real matches or toothpicks).',
      warmup: 'Clap-snap-stomp patterns. The tutor starts, the class says what comes next, then what comes in the 10th place.',
      explore: 'Pairs build 1, 2 and 3 triangles in a row with sticks and count. Predict the 4th before building it.',
      mini: 'Table: triangles 1, 2, 3 … and sticks 3, 5, 7 … Each new triangle shares a side, so only 2 new sticks. Show 15 sticks and work backwards.',
      share: 'How can we know the 30th shape without drawing all 30?',
      exit: { q: 'Circle, square, circle, square … What is the 9th shape?', a: 'Circle (odd places are circles).' },
      mistakes: ['Saying 3 more sticks each time because one triangle needs 3.', 'Thinking the 30th shape is a circle because 30 starts with 3.', 'Dividing 15 by 3 to get 5 triangles.'],
      extension: 'Squares in a row (4, 7, 10 …): find the rule and how many sticks for 10 squares (31).',
      key: [
        ['Q1', 'Place 8: triangle. Place 9: square.'],
        ['Q2', '(a) circle  (b) square  (c) square  (d) The pattern repeats every 3 and every 3rd shape is a square. We say 30 when we count in 3s, so the 30th shape ends a core: a square.'],
        ['Q3', '(a) 3, 5, 7, 9, 11, 13, 15, 17, 19, 21  (b) 2 more  (c) The new triangle shares a side with the one before.  (d) 21 sticks'],
        ['Q4', '7 triangles. Continue the table: 3, 5, 7, 9, 11, 13, 15 sticks.'],
        ['Stretch slide', '1) circle  2) 9 Bs  3) Yes: count in 5s, 25 ends a core, like the 5th']
      ]
    },
    {
      n: 5, week: 3, session: 'A', title: 'Mystery Number', topic: 'Working Backwards',
      objective: 'Solve "I think of a number" problems by working backwards, find a number machine rule, and solve more-than and fewer-than stories.',
      skills: 'Inverse operations, rule finding, bar-model thinking, logical reasoning',
      materials: 'Paper cups, counters, number machine cards.',
      online: 'Slide with a cup that hides counters; the tutor reveals the total and the children work back.',
      warmup: 'Think-of-a-number magic: "Think of a number, add 3, the answer is 8. What was it?" Increase the steps.',
      explore: 'Pairs hide a secret number of counters under a cup, add 5 more, and tell their partner the total. The partner works backwards by removing 5.',
      mini: 'Draw the story as a line: start → add 5 → 12. To undo, go the other way: 12 − 5. Introduce the number machine table (IN and OUT).',
      share: 'Ali is 8th from the front and 8th from the back. Why is the answer not 16?',
      exit: { q: 'I think of a number. I add 6. I get 15. What is my number?', a: '9' },
      mistakes: ['Adding again instead of undoing (12 + 5).', 'Two steps: undoing in the wrong order.', 'Queue question: giving 16 because Ali is counted twice.'],
      extension: 'Make a three-step mystery number story for a partner.',
      key: [
        ['Q1', '(a) 7  (b) 12  (c) 8 (undo in reverse order: 10 + 2 = 12, then 12 \u2212 4 = 8)'],
        ['Q2', '(a) 15 and 8  (b) Add 4. IN 15 gives OUT 19. OUT 30 comes from IN 26.'],
        ['Q3', '(a) Mei 13  (b) Ben 7  (c) Mei has 6 more than Ben  (d) 28 altogether'],
        ['Q4', '(a) 13 children (20 − 7)  (b) 5 children (3 + 3 − 1, Ali is counted twice). Talk time: 8th from both ends is 15.'],
        ['Q5', 'Open: check that the story has a clear answer.'],
        ['Stretch slide', '1) 10 children  2) 7 sweets  3) 11']
      ]
    },
    {
      n: 6, week: 3, session: 'B', title: 'Coin Combos', topic: 'Money',
      objective: 'Find all the ways to make an amount, work systematically, use reasoning to rule out cases, and pay in dollars with notes up to $100.',
      skills: 'Systematic listing, comparing, working backwards, justifying "there are no more"',
      materials: 'Play coins (5¢, 10¢, 20¢, 50¢, $1), about 6 of each per pair, play notes ($2, $5, $10, $50), mini whiteboards.',
      online: 'Print the cut-out coins and notes at the back of the workbook, or use real coins and notes at home.',
      warmup: 'Money shop: six items priced from 65¢ to $65. Pay exactly with coins and notes. Who can pay with the fewest?',
      explore: 'Pairs make 20¢ in as many ways as they can with 20¢, 10¢ and 5¢ coins, recording each on a whiteboard.',
      mini: 'Start with the biggest coin and work down. Use a table: how many 20¢, 10¢, 5¢. Show why we know when we have them all.',
      share: 'Why can’t 35¢ be made with only two coins?',
      exit: { q: 'Make 40¢ using exactly three coins from 5¢, 10¢, 20¢, 50¢.', a: '20¢ + 10¢ + 10¢.' },
      mistakes: ['Listing the same way twice in a different order (10+5+5 and 5+10+5).', 'Choosing many small coins instead of looking for the fewest.', 'Stopping at the first set in Think Harder T1 instead of checking for all of them.'],
      extension: 'Make 50¢ in as many ways as possible using 5¢, 10¢, 20¢ and 50¢.',
      key: [
        ['Q1', 'A: one 20¢.  B: two 10¢.  C: one 10¢ and two 5¢.  D: four 5¢.  Row E is spare (only 4 ways).  (a) one 20¢ coin  (b) four 5¢ coins  (c) Start with the biggest coin and work down.'],
        ['Q2', '6 ways: 20+10; 20+5+5; 10+10+10; 10+10+5+5; 10+5+5+5+5; six 5¢.'],
        ['Q3', '(a) 4 coins: 50¢ + 20¢ + 10¢ + 5¢.  (b) e.g. 50¢ + 10¢ + 10¢ + 5¢ + 5¢ + 5¢, or 20¢ + 20¢ + 20¢ + 10¢ + 10¢ + 5¢.'],
        ['Q4', 'No. Two coins can total 10, 15, 20, 25, 30, 40, 55, 60, 70 or 100. 35 is not one of them.'],
        ['Q5', '(a) $10 + $5 + $2 (3 pieces).  (b) Any 3 ways, e.g. $10 + $10; $10 + $5 + $5; $5 + $5 + $5 + $5; $10 + $5 + $2 + $2 + $1. There is no $20 note.  (c) No. She has $50 + $10 + $10 = $70. The bicycle and helmet cost $65 + $8 = $73. She is $3 short.'],
        ['Think Harder T1 to T4', 'T1: two sets, 50¢ + 10¢ + 5¢ + 5¢, and 20¢ + 20¢ + 20¢ + 10¢.  T2: three 10¢ and three 20¢ (30 + 60 = 90); four coins of 20¢ make only 80¢, so 4 coins cannot make 90¢.  T3: 3 coins (20¢ + 20¢ + 5¢); no two coins make 45¢.  T4: 4 ways (20+5; 10+10+5; 10+5+5+5; five 5¢).'],
        ['Stretch slide', '1) 9 ways  2) $10 + $1 + $1 and $5 + $5 + $2  3) 4 coins (50¢ + 20¢ + 20¢ + 5¢)']
      ]
    },
    {
      n: 7, week: 4, session: 'A', title: 'Shape Safari', topic: '2D Shapes',
      objective: 'Name and describe 2D shapes by sides and corners, count shapes in a picture, count triangles in a figure, and compose shapes.',
      skills: 'Classifying, describing, systematic counting, spatial reasoning',
      materials: 'Paper squares, scissors, pattern blocks, 2 shape riddles on cards.',
      online: 'Each child has a paper square to fold and cut on camera; shape hunt at home.',
      warmup: 'Shape hunt: find a circle, a triangle, a square and a rectangle in the room or at home in 2 minutes.',
      explore: 'Fold a paper square along a diagonal and cut: what two shapes do you get? Put them together a different way. What new shapes can you make?',
      mini: 'Count squares in grids by size, smallest first (a 2 by 2 grid, then a 3 by 3 grid). Rectangles in strips and shapes made from 3 squares are for early finishers. Before the worksheet: count shapes in a picture one kind at a time, mark a starting dot when counting sides, cross out shapes for riddles, count triangles small first.',
      share: 'How many triangles are in a square with both diagonals drawn (lines joining opposite corners)? How do you make sure you do not miss any?',
      exit: { q: 'How many squares are in a 3 by 3 grid? (3 squares long and 3 squares high)', a: '14 (9 small + 4 made of 4 small ones + 1 made of all 9)' },
      mistakes: ['Counting only the small triangles in the talk-time picture (4 instead of 8): look for bigger triangles made of 2 small ones.', 'Counting a square window in both the Square and the Rectangle columns in Q1.', 'Thinking a turned or flipped shape is a new one.', 'Thinking a square is not a rectangle, or the opposite, without a reason.', 'Saying a circle has a straight side (it has 0 straight sides).'],
      extension: 'How many squares in a grid 4 long and 2 high? (8 + 3 = 11) Then 4 long and 3 high? (12 + 6 + 2 = 20)',
      key: [
        ['Q1', 'Circle 1, triangle 2, square 3, rectangle 2. (a) Squares. (b) 8 shapes.'],
        ['Q2', 'Straight sides and corners: circle 0 and 0, triangle 3 and 3, square 4 and 4, pentagon 5 and 5, hexagon 6 and 6, octagon 8 and 8. The number of straight sides equals the number of corners. 7 sides means 7 corners.'],
        ['Q3', '(a) square  (b) circle  (c) hexagon'],
        ['Q4', 'A: 3  B: 2. (The square with both diagonals, 8 triangles, is the talk-time question: 4 small + 4 made of two small ones.)'],
        ['Q5', 'Accept any correct shape with its name: rectangle, square, bigger triangle or parallelogram.'],
        ['Q6', '5 squares (4 small + 1 big)'],
        ['Stretch slide', '1) 6  2) 9  3) Yes to both: the square again, and one big triangle with a long side twice as long']
      ]
    },
    {
      n: 8, week: 4, session: 'B', title: 'Logic Lab', topic: 'Logic and Sorting',
      objective: 'Order things from clues, sort using two rules with a Venn diagram, solve a logic grid, and explain an odd one out.',
      skills: 'Deduction, classification, elimination, justifying',
      materials: 'Two loops of string, buttons or small objects (small objects only with a grown-up nearby), clue cards.',
      online: 'Children sort objects from home by a rule shown on the slide and explain the rule on camera. Buttons and other small objects: only with a grown-up nearby.',
      warmup: 'Guess my number: the tutor thinks of a number from 1 to 20. Children ask yes/no questions to find it in as few questions as they can.',
      explore: 'Overlap two string loops. Sort a mixed set of buttons or objects by two rules and find the ones that belong in the middle.',
      mini: 'Model the grid: one tick in each row and column, crosses where it cannot be. Each cross helps another cell. Sort numbers 10 to 20 into a Venn diagram, called a two-loop picture with the children (less than 15, even): ask both questions for every number.',
      share: 'There can be more than one correct odd one out. Can you give a second reason?',
      exit: { q: 'Ben is shorter than Mei. Mei is shorter than Ali. Who is the tallest?', a: 'Ali' },
      mistakes: ['Putting numbers in the overlap that only fit one rule.', 'Giving up on the grid instead of using a cross to rule out.', 'Guessing a line-up without checking all the clues.'],
      extension: 'Create a logic grid puzzle with four friends and four pets.',
      key: [
        ['Q1', '(a) Ali tallest, Mei shortest; order Ali, Ben, Mei  (b) Cat heaviest, hen lightest  (c) Yellow, red, blue, green'],
        ['Q2', 'Both (less than 6 and odd): 1, 3, 5. Only less than 6: 2, 4. Only odd: 7, 9. Outside both: 6, 8, 10. (b) 1, 3, 5: they are less than 6 AND odd.'],
        ['Q3', 'Ali: fish. Mei: cat. Ben: dog.'],
        ['Q4', '1st Mei, 2nd Ali, 3rd Ben, 4th Sam'],
        ['Q5', '(a) 15  (b) 30  (c) 14'],
        ['Q6', 'Accept any reasoned answer: 11, because we do not say it when counting in 3s (it is also the only 2-digit number); or 6, the only even number.'],
        ['Stretch slide', '1) Ben cat, Cara fish, Dan dog, Ali rabbit  2) Eve, Ben, Ali, Dan, Cara  3) 10, 20 and 30']
      ]
    },
    {
      n: 9, week: 5, session: 'A', title: 'Measure It!', topic: 'Length',
      objective: 'Compare and order lengths, measure with equal units and with a centimetre ruler (also when the object does not start at 0), and change a length from one unit to another in both directions.',
      skills: 'Comparing, measuring, unit reasoning, estimating',
      materials: 'Linking cubes or paper cube strips, paper clips, erasers, objects to measure, a cm ruler for each child, mini whiteboards.',
      online: 'Print the cube strip at the back of the workbook; measure household objects. Each child needs a cm ruler.',
      warmup: 'Longer or shorter? Hold up two objects. Predict, then check by laying them side by side. Order three objects.',
      explore: 'Measure a pencil, a book and a shoe with cubes. Estimate first, then measure and compare with the guess. Then measure the same book with hand spans and compare with a partner.',
      mini: 'Equal units, no gaps or overlaps. Compare lengths with bars lined up at one end. Measure in cm with a ruler, also when the object does not start at 0 (count the spaces). Change units both ways with a bar picture (1 clip = 3 erasers: 4 clips = 12 erasers; 6 erasers = 2 clips).',
      share: 'Ali measured 6 spans and Mei measured 8 spans for the same desk. Whose hand is bigger? Why?',
      exit: { q: 'A ribbon lies from the 3 cm mark to the 9 cm mark on a ruler. How long is it?', a: '6 cm' },
      mistakes: ['Leaving gaps or overlapping the cubes.', 'Not starting at zero.', 'Thinking more units means a bigger unit.', 'Reading the end mark when the object does not start at 0.'],
      extension: 'Measure the same object with two different units and find the rule linking the two counts.',
      key: [
        ['Q1', '(a) C  (b) B  (c) 2 more  (d) 12 units  (e) Same as A (9 − 2 = 7)'],
        ['Q2', 'Open. Check guesses are close. The Difference column is how far off the guess was. Equal units are needed so the measures can be compared fairly.'],
        ['Q3', 'Ali. Fewer spans means each span was longer, so Ali’s hand is bigger.'],
        ['Q4', '(a) 10 erasers  (b) 6 clips'],
        ['Q5', 'Ali 11 cubes, Ben 6 cubes. All three together: 25 cubes.'],
        ['Q6', '(a) 12 cm  (b) 5 cm (8 − 3)  (c) Open: check the child started at the 0 mark and compared with 10 cm.'],
        ['Stretch slide', '1) 5 cubes each and 2 cuts  2) Ben: six clips of 2 cubes is 12 cubes  3) The 11 cm mark']
      ]
    },
    {
      n: 10, week: 5, session: 'B', title: 'Challenge Day', topic: 'Mixed Puzzles',
      objective: 'Use patterns, bonds, graphs, money, shapes, logic, working backwards and measuring in new puzzles, and explain the thinking.',
      skills: 'Applying and connecting ideas, perseverance, explaining',
      materials: 'Four puzzle cards (coins, patterns, logic, measuring; printed in the workbook and shown on the Lesson 10 slide), play coins, cubes, certificates, stamps, mini whiteboards.',
      online: 'One puzzle card per breakout room (the tutor pastes the card into the room chat). Pairs swap cards at minute 20 and report back to the group in 30 seconds each.',
      warmup: 'Mental maths relay: a chain of quick questions from all 9 lessons passed around the group.',
      explore: 'Four puzzle cards (coins, patterns, logic, measuring). Pairs get ONE card for 10 minutes, then swap cards with another pair for a second 4-minute round. Online: one card per breakout room; each pair reports in 30 seconds.',
      cards: [
        { title: 'Coins', text: 'Make 45¢ with exactly 3 coins from 5¢, 10¢, 20¢ and 50¢.', answer: '20¢ + 20¢ + 5¢ (the only way).' },
        { title: 'Patterns', text: '5, 8, 11, 14 … What is the 10th number? Show how you know.', answer: '32. Add 3 each time: 5, 8, 11, 14, 17, 20, 23, 26, 29, 32.' },
        { title: 'Logic', text: 'Mei is taller than Ben. Ben is taller than Sam. Ali is shorter than Sam. Put them in order, tallest first.', answer: 'Mei, Ben, Sam, Ali.' },
        { title: 'Measuring', text: 'A pencil is 6 cubes long. A pen is 4 cubes longer than the pencil. Put them end to end. How many cubes long is that?', answer: '16 cubes (the pen is 10 cubes; 6 + 10 = 16).' }
      ],
      mini: 'How to start a puzzle: draw it (people in order, bars, number machines), list it in order (coins, pairs, shapes to count), make a table (patterns, things that grow). Then check and explain.',
      share: 'Pick one puzzle and teach it to the group in two sentences.',
      exit: { q: 'My favourite lesson was ____ because ____.', a: 'Open. Use it to plan next steps.' },
      mistakes: ['Rushing: not checking an answer.', 'Not showing how they know.'],
      extension: 'Write a challenge puzzle for next year’s group.',
      key: [
        ['Q1', '23, 28. Add 5.'],
        ['Q2', '5 and 7 (5 + 7 = 12 and 7 − 5 = 2)'],
        ['Q3', '(a) 2 more cats than birds  (b) 19 pets  (c) Cat and fish (7 + 3 = 10)'],
        ['Q4', '(a) 50¢  (b) 20¢ + 10¢ + 5¢'],
        ['Q5', '(a) square  (b) 3 triangles'],
        ['Q6', 'Mei is youngest, Ali is oldest.'],
        ['Q7', '5 (5 + 9 = 14, 14 − 4 = 10)'],
        ['Q8', 'Pen 10 cubes. End to end 16 cubes.'],
        ['Q9', 'Open. Done at talk time: swap puzzles with a partner and solve each other\u2019s.'],
        ['Puzzle cards', 'Coins: 20¢ + 20¢ + 5¢.  Patterns: 32.  Logic: Mei, Ben, Sam, Ali.  Measuring: 16 cubes.'],
        ['Stretch slide', '1) Two ways: five 2s, or 3 + 3 + 2 + 2  2) Ben, Mei, Ali, Sam  3) Three 10¢ and four 5¢']
      ]
    }
  ]
};
