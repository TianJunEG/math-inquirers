# Fixes applied for the P6 gifted-style audit (docs/audit/gifted_p6.md)

Date: 2026-10-22. Edited: `p6/content/l1.js` to `l10.js` (question banks only), `rebuild/gen_p6l9.py` (Challenge walk-through slide text and notes), `docs/audit/verify_gifted_p6.py` (new). Nothing committed or published. No shared file was edited (`rebuild/slidekit.py`, `hp/levelkit.js`, `levels/*` untouched).

## What was done and how it was checked

- **Tier principle:** Core items were rewritten (wording, context, scaffold such as a picture, table, “use matchsticks”, “draw a thermometer”, a definition inside the question) so a child who has not met the topic can start and usually finish them. Think Harder stayed on the taught idea; two Think Harder items that did not need the idea were replaced. Challenge items that were one step of the taught method were replaced or extended.
- **Problem posing:** every lesson now has one open-ended “make up your own / design / justify” item in Challenge, placed at Challenge 7 so it is printed on the Think Harder page (the printed page shows Challenge 7 to 9 as its items 5 to 7). Lesson 10: “mix two topics”. Lesson 6: design a fair game, then break it. Lesson 7: design your own star.
- **Answers:** every new or changed numeric answer was checked in Python with exact fractions, and every “find all” or “unique answer” claim was brute-forced (magic grid has exactly 8 solutions; Goldbach counts; 3-factor numbers; the nine-point and twelve-point stars; the mean mystery and the 5-number set have one answer each). Run `python3 docs/audit/verify_gifted_p6.py`: 172 checks, all OK. It also re-checks the unchanged answers of lessons whose items moved.
- **Workbook worksheets (core pages):** unchanged. I tried a one-line scaffold on L1 Q2 (“write the times table of the difference first”) and on L2 Q4 (a list of primes to 40); both pushed a page onto an extra page, so both were reverted to keep the page count. They remain caveats in the audit.
- **Slides:** the slides print the Think Harder and Challenge items for early finishers. Lessons 1 to 4 hard-code those items and none of them changed. Lessons 5 to 8 and 10 read the bank by position (`stretch[4:7]`, `challenge[-2:]`, `challenge[:2]`, or a fixed index), and I left those positions on the same items, so their decks are unchanged. Lesson 6 (Think Harder 6) and Lesson 9 (Challenge 1 and 2) changed, so those two decks were regenerated.

## Per lesson: what changed

“Position” is where the item now sits in the bank. Old items are quoted shortly; the new text is in `p6/content/lN.js` and the Question Bank.

### Lesson 1: Code the Pattern

Core is now matchsticks, listing terms, a code trace and a drawn fence; the fence-post item moved down from Challenge because it is a draw-it problem. Challenge keeps the full-rule items and gains a make-up puzzle (printed as Think Harder page, Challenge 5).

- **Core 2 → Core 2** (replaced). Old: Write the rule for the nth term of 3, 5, 7, 9, …  
  New: Matchstick triangles in a row. Pattern 1 is 1 triangle (3 sticks). Pattern 2 is 2 triangles side by side (5 sticks). Pattern 3 is 3 triangles (7 sticks). Use matchsticks or draw them. How many sticks does pattern 4 need?
- **Core 3 → Core 3** (reworded). Old: Find the 10th term of 7, 10, 13, 16, …  
  New: Write out the terms one by one to find the 10th term of 7, 10, 13, 16, …
- **Core 6 → Core 6** (replaced). Old: The rule for the nth term is 4n + 3. Write the first three terms.  
  New: A straight fence is 12 m long with a post every 4 m, including a post at each end. Draw it and count the posts. Then work out how many posts a 60 m fence needs.
- **Think Harder 4 → Think Harder 4** (reworded). Old: What does this code say?  set n to 100, then repeat 8 [change n by −7], then say n.  
  New: set n to 7, then repeat 49 [change n by 6], then say n. What does it say? Which term of 7, 13, 19, … is that? Check with the rule 6n + 1.
- **Challenge 2 → Challenge 7** (replaced). Old: A straight fence is 60 m long. There is a post every 4 m, including one at each end. How many posts are there?  
  New: Make up your own sequence puzzle. Choose a first term and a difference, write the first four terms, then ask: “Is ___ a term?” Pick a number that is NOT a term but is close to one. Swap with a partner and explain how you know. The old fence-post item was reworded and moved down to Core 6 (tier changed: Challenge to Core).
- **Challenge 4 → Challenge 4** (extended). Old: Find the first term of 5, 8, 11, 14, … that is bigger than 1000. Which term is it?  
  New: Find the first term of 5, 8, 11, 14, … that is bigger than 1000. Which term is it? Then find the first term bigger than 1000 that ends in 0.

### Lesson 2: Prime Hunters

Core now defines “prime” inside the question, starts factorisation as “split into as many numbers as you can”, gives the first primes for the sum-of-two-primes item, and sets mod as sweets left over. The listing-primes Challenge item became a “Who am I?” make-up puzzle.

- **Core 1 → Core 1** (extended). Old: List all the factors of 18.  
  New: List all the factors of 18. Hint: find pairs of numbers that multiply to 18.
- **Core 2 → Core 2** (replaced). Old: Is 37 prime? How do you know?  
  New: A number is called prime if it has exactly two factors: 1 and itself. For example, 7 is prime (factors 1 and 7) but 8 is not (factors 1, 2, 4, 8). Is 21 prime? Is 23 prime? List the factors of each.
- **Core 3 → Core 3** (replaced). Old: What is 29 mod 4 (the remainder when 29 is divided by 4)?  
  New: 29 sweets are shared equally among 4 children. How many sweets are left over? (In code, the left-over number is written 29 mod 4.)
- **Core 4 → Core 4** (replaced). Old: Write 30 as a product of primes.  
  New: Write 30 as a multiplication of as many numbers (bigger than 1) as you can. For example, 30 = 5 × 6 uses two numbers. Can you use three? Can you use four?
- **Core 5 → Core 5** (extended). Old: Which of these are prime: 21, 23, 25, 27, 29?  
  New: A prime number has exactly two factors. Which of these are prime: 21, 23, 25, 27, 29? Hint: try dividing each by 2, 3 and 5.
- **Core 6 → Core 6** (reworded). Old: Write 20 as the sum of two primes.  
  New: The primes begin 2, 3, 5, 7, 11, 13, 17, 19. Write 20 as the sum of two of them.
- **Challenge 5 → Challenge 7** (replaced). Old: Mei’s program counts how many numbers from 1 to 30 are prime. What number should it say? List them to check.  
  New: Make up a “Who am I?” number puzzle using factors and primes, for example: “I am between 30 and 60 and I have exactly three factors.” Write 2 or 3 clues so that only ONE number fits. Swap with a partner, then check that no other number fits.

### Lesson 3: Below Zero

Every Core item now says what the minus sign means and asks for a thermometer or number-line drawing. The Moscow Challenge item became a make-up temperature story.

- **Core 1 → Core 1** (replaced). Old: Put in order, smallest first: −4, 2, −10, 0, −1.  
  New: On a thermometer, 0 °C is where water freezes. Colder than that, numbers have a minus sign: −3 °C means 3 degrees below zero. Draw a thermometer or number line and write these in order, coldest first: −4, 2, −10, 0, −1.
- **Core 2 → Core 2** (reworded). Old: It is −3 °C. The temperature rises by 8 degrees. What is it now?  
  New: It is −3 °C (3 degrees below zero). The temperature rises by 8 degrees. What is it now? Count up on a thermometer drawing.
- **Core 3 → Core 3** (extended). Old: It is 2 °C. The temperature falls by 7 degrees. What is it now?  
  New: It is 2 °C. The temperature falls by 7 degrees. What is it now? Count down on a thermometer drawing: 2, 1, 0, then below zero.
- **Core 4 → Core 4** (reworded). Old: Which is colder, −6 °C or −11 °C? By how many degrees?  
  New: Which is colder, −6 °C or −11 °C? By how many degrees? Mark both on a thermometer drawing.
- **Core 5 → Core 5** (extended). Old: In a building the floors are numbered …, −2, −1, 0, 1, 2, … and 0 is the ground floor. A lift is at floor −2. It goes up 6 floors. …  
  New: In a building the floors are numbered …, −2, −1, 0, 1, 2, … where 0 is the ground floor and −1 is the first floor below it. A lift is at floor −2. It goes up 6 floors. Which floor is it on now? Count the floors one by one.
- **Core 6 → Core 6** (reworded). Old: A sprite is at x = 30. It runs "change x by −50". Where is it now?  
  New: In Scratch the stage is a number line. A sprite is at x = 30. It runs “change x by −50” (move 50 steps to the left). Where is it now?
- **Challenge 5 → Challenge 7** (replaced). Old: Tokyo is 6 °C. Seoul is 4 degrees colder than Tokyo. Moscow is 17 degrees colder than Seoul. What is the temperature in Moscow?  
  New: Make up your own temperature story with at least three changes (rises and falls) that starts below zero and ends at exactly −7 °C. Write the story, the working and a number-line sketch. Swap with a partner and check each other’s.

### Lesson 4: Algebra Machines

Core now uses machines in words, a table to spot the pattern, guess-and-check and a stickers table (no letter needed). Challenge 3, which repeated Think Harder 5, became “find two machines for IN 5 giving OUT 18, then the one that also fits IN 2 giving OUT 6”.

- **Core 1 → Core 1** (reworded). Old: The rule is OUT = 4n + 1. What is OUT when n = 6?  
  New: A number machine multiplies IN by 4 and then adds 1. (We write this OUT = 4n + 1.) What comes OUT when 6 goes IN? Try 2 and 3 first.
- **Core 2 → Core 2** (replaced). Old: IN 1, 2, 3, 4 gives OUT 3, 5, 7, 9. Write the rule with n.  
  New: A machine changes IN 1, 2, 3, 4 into OUT 3, 5, 7, 9. Look at how OUT goes up each time. What does the machine do? What will come OUT when 10 goes IN?
- **Core 3 → Core 3** (replaced). Old: Solve 3n = 54.  
  New: I think of a number and multiply it by 3. I get 54. What was my number? (Guess and check, or share 54 into 3 equal groups.)
- **Core 4 → Core 4** (reworded). Old: A machine multiplies by 6, then takes away 4. OUT is 38. What was IN?  
  New: A machine multiplies by 6, then takes away 4. OUT is 38. What was IN? Try some numbers, or undo the steps.
- **Core 5 → Core 5** (replaced). Old: Ali has n stickers. Mei has 5 more than Ali. Write how many they have altogether.  
  New: Ali has some stickers. Mei has 5 more than Ali. Fill in the table: if Ali has 3 stickers, Mei has __ and they have __ altogether. If Ali has 7, they have __ altogether. If Ali has 10, they have __. What do you notice about how the total changes?
- **Core 6 → Core 6** (reworded). Old: A Scratch machine does: set out to (answer * 3) + 4, then say out. You type 7. What does it say?  
  New: A Scratch machine runs: ask for IN, then set out to (answer * 3) + 4, then say out. (* means ×.) You type 7. What does it say?
- **Challenge 3 → Challenge 7** (replaced). Old: A rule is “× a number, then + a number”. IN 2 gives OUT 10 and IN 6 gives OUT 22. What is OUT when IN is 0?  
  New: Find two different machines of the form “× a number, then + or − a number” that both turn IN 5 into OUT 18. Then find the machine of this form that ALSO turns IN 2 into OUT 6. Is there only one?

### Lesson 5: Every Possible Way

Core was already concrete; scaffolds only (draw lines, act it out, draw the grid). Challenge: the two repeat items became a reverse handshake (90 cards) and a make-up puzzle; the digit and triangle items were extended.

- **Core 1 → Core 1** (extended). Old: A shop sells 3 shirts and 5 pairs of trousers. How many different outfits of 1 shirt and 1 pair of trousers can you make?  
  New: A shop sells 3 shirts and 5 pairs of trousers. How many different outfits (1 shirt and 1 pair of trousers) can you make? Draw lines to match each shirt with each pair of trousers.
- **Core 3 → Core 3** (reworded). Old: 4 friends meet. Every pair shakes hands once. How many handshakes?  
  New: Four friends meet. Every pair of friends shakes hands once. How many handshakes are there? Act it out, or draw 4 dots and join every pair.
- **Core 4 → Core 4** (extended). Old: How many times does this say “hi”?  repeat 4 { repeat 6 { say hi } }  
  New: How many times does this say “hi”?  repeat 4 { repeat 6 { say hi } }  (The inner repeat runs all 6 times for each time round the outer repeat.)
- **Core 5 → Core 5** (reworded). Old: A grid is 3 squares wide and 1 square tall. How many routes go from the bottom left corner to the top right corner, going only rig …  
  New: A grid is 3 squares wide and 1 square tall. Draw it. How many routes go from the bottom left corner to the top right corner, going only right or up?
- **Core 6 → Core 6** (extended). Old: A lock has 2 dials. Each dial shows a digit from 0 to 9. How many different codes are there?  
  New: A lock has 2 dials. Each dial shows a digit from 0 to 9. How many different codes are there? Start by counting the codes that begin with 0.
- **Challenge 1 → Challenge 1** (reworded). Old: How many different triangles can you make by joining 3 of the 5 corners of a pentagon?  
  New: How many different triangles can you make by joining 3 of the 5 corners of a pentagon? What about a hexagon?
- **Challenge 2 → Challenge 2** (reworded). Old: How many 2-digit numbers have two different digits?  
  New: How many 3-digit numbers have three different digits? (Remember: a number cannot start with 0.)
- **Challenge 4 → Challenge 7** (replaced). Old: An ice cream shop has 6 flavours. A cup has 2 different flavours, and the order does not matter. How many different cups are there …  
  New: Make up your own “how many ways” puzzle whose answer is exactly 24. Write the puzzle, show how you counted, and check with a list or a tree. Swap with a partner.
- **Challenge 5 → Challenge 5** (reworded). Old: 4 friends each send a card to every other friend. How many cards are sent?  
  New: At a party every friend sends a card to every other friend (A to B and B to A are two cards). 90 cards are sent altogether. How many friends are at the party? Test small parties first.

### Lesson 6: Fair or Unfair?

Core no longer uses the word “probability” cold: it says “chance, __ out of __”, lists the dice results, and asks whether a game is fair by listing outcomes. Think Harder 6 and Challenge 1 replaced (Challenge 1 is now “design a fair game”).

- **Core 1 → Core 1** (replaced). Old: Roll a dice. What is the probability of rolling a 4?  
  New: Roll a dice. Write down every possible result. How many of them are even? So the chance of an even number is __ out of __. Write it as a fraction.
- **Core 2 → Core 2** (replaced). Old: Roll a dice. What is the probability of rolling an even number?  
  New: A bag has 3 red and 7 yellow counters. You pick one without looking. How many counters are there altogether? What is the chance (as a fraction) that you pick yellow?
- **Core 3 → Core 3** (replaced). Old: A bag has 3 red and 7 yellow counters. You pick one without looking. What is the probability it is yellow?  
  New: You flip a coin 200 times. About how many heads do you expect? Will it be exactly that number?
- **Core 4 → Core 4** (replaced). Old: You flip a coin 200 times. About how many heads do you expect?  
  New: A spinner has 4 equal parts: red, red, blue, green. Write the chance of spinning red as a fraction.
- **Core 5 → Core 5** (replaced). Old: A spinner has 4 equal parts: red, red, blue, green. What is the probability of red?  
  New: Roll a normal dice. Can you roll a 9? Choose one: impossible, unlikely, likely or certain.
- **Core 6 → Core 6** (replaced). Old: Roll a normal dice. What is the probability of rolling a 9?  
  New: A game: you win if the dice shows 1 or 2; your friend wins if it shows 3, 4, 5 or 6. Write the six dice results and who wins each one. Is the game fair? Why or why not?
- **Think Harder 6 → Think Harder 6** (reworded). Old: A program rolls a dice 1200 times. About how many even numbers should it roll?  
  New: A program rolls a dice 1200 times and counts the numbers bigger than 4. About how many should it count? The program says 391. Is something wrong? Explain.
- **Challenge 1 → Challenge 7** (replaced). Old: A bag has red and blue counters in the ratio 2 : 3. What is the probability of picking red?  
  New: Design a FAIR game for two players using one dice, two coins or a spinner. Write the rules and show with a list or table that each player has the same chance of winning. Then change ONE rule to make the game unfair, and say who is favoured.

### Lesson 7: Turtle Geometry

Core now states that a full turn is 360° and uses add-up, guess-and-check and straight-line angles instead of 360° ÷ n. Three one-formula Challenge items replaced by a design-your-own-star task, a justify task and a two-step combination.

- **Core 1 → Core 1** (replaced). Old: A turtle draws a regular hexagon. How many degrees does it turn at each corner?  
  New: Walk a square: walk forward, turn on the spot by 90° to the right, and repeat, until you are back at the start facing the way you began. You turn 90° at each of the 4 corners. How many degrees did you turn altogether? (A full turn on the spot is 360°.)
- **Core 2 → Core 2** (replaced). Old: What is each inside angle of a regular hexagon?  
  New: A turtle runs: repeat 6 [move 100, turn ↻ 60]. It draws a hexagon. How many degrees does it turn altogether? What do you notice?
- **Core 3 → Core 3** (replaced). Old: Fill in the turn so the turtle draws a square: repeat 4 [move 100, turn ↻ ___ ]  
  New: A turtle draws an equilateral triangle: repeat 3 [move 100, turn ↻ ___ ]. It turns the same amount each time and ends up facing the way it started (a full turn is 360°). Guess and check, or draw it with a ruler. What number goes in the gap?
- **Core 4 → Core 4** (replaced). Old: A regular polygon has a turn angle of 72°. How many sides does it have?  
  New: A turtle repeats [move 100, turn ↻ 72] again and again. How many repeats until it first faces the way it started? Add up the turns, 72, 144, … until you reach a full turn (360). What shape does it draw?
- **Core 5 → Core 5** (reworded). Old: At a corner the turtle turns 50°. What is the inside angle at that corner?  
  New: Angles on a straight line add up to 180°. At one corner the turtle turns 50° to go along the next side. What is the inside angle at that corner?
- **Core 6 → Core 6** (replaced). Old: A turtle draws any triangle and comes back to the start facing the same way. How many degrees has it turned altogether?  
  New: Each turn of a regular hexagon is 60°. A turn and the inside angle at a corner make a straight line (180°). What is each inside angle of a regular hexagon?
- **Challenge 3 → Challenge 7** (replaced). Old: Each inside angle of a regular polygon is 5 times its turn angle. How many sides does it have?  
  New: Design your own star. Choose the number of points p and how many times it goes round, k, so that the turn angle 360° × k ÷ p is a WHOLE number and p and k share no common factor. Give the turn angle, the point angle (180° − turn) and the code. Explain why your star closes after p repeats.
- **Challenge 6 → Challenge 6** (reworded). Old: Each inside angle of a regular polygon is 20° bigger than each inside angle of a regular hexagon. How many sides does it have?  
  New: Zara says: “The more sides a regular polygon has, the bigger each inside angle is, but an inside angle can never reach 180°.” Is she right? Use the turn angle to explain.
- **Challenge 7 → Challenge 3** (reworded). Old: All the inside angles of a regular polygon add up to 1800°. How many sides does it have, and what is its turn angle?  
  New: The inside angles of a regular polygon add up to 1800°. A second regular polygon has a turn angle exactly half as big as the first one’s. How many sides does the second polygon have, and what do all its inside angles add up to?

### Lesson 8: Secret Codes

Core defines the shift code with an alphabet hint and keeps clocks, remainders and days. The two one-step mod Challenge items became a make-and-crack message and a cross-topic (LCM + weekday) puzzle; the eggs duplicate from Lesson 2 became a new remainders puzzle.

- **Core 2 → Core 2** (replaced). Old: Work out 20 mod 12.  
  New: A clock has 12 numbers. Start at 12 and move 20 hours forward. Where do you stop? (This is written 20 mod 12: the remainder when 20 is divided by 12.)
- **Core 3 → Core 3** (reworded). Old: What is the remainder when 45 is divided by 7?  
  New: What is the remainder when 45 is divided by 7? Hint: count up in 7s.
- **Core 5 → Core 5** (replaced). Old: Code the word DOG with a shift of 1.  
  New: A secret code moves every letter one place along the alphabet: A becomes B, B becomes C, and so on. Code the word DOG. (Write the alphabet out to help you.)
- **Core 6 → Core 6** (replaced). Old: Decode KBN. It was made with a shift of 1.  
  New: Using the same code (every letter moves one place along), decode KBN. Move each letter one place back.
- **Challenge 3 → Challenge 7** (replaced). Old: What day of the week is it 1000 days after a Monday?  
  New: Write your own secret message of at least 8 letters and code it with a shift of your choice. Write clear instructions telling a friend how to decode it, and explain how a friend could crack it without being told the shift. Swap and decode.
- **Challenge 4 → Challenge 4** (reworded). Old: Find the smallest number that leaves a remainder of 1 when it is divided by 2, 3, 4, 5 or 6, and is a multiple of 7.  
  New: Find the smallest number that leaves a remainder of 2 when it is divided by 3, by 4 or by 5, and is a multiple of 7.
- **Challenge 5 → Challenge 5** (replaced). Old: Count 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, … (start again after 7). What is the 2026th number you say?  
  New: Ali goes to the library every 4th day and Mei every 6th day. They are both there on Day 0, a Monday. On which day of the week do they next meet? And on which day of the week is their 5th meeting after Day 0?

### Lesson 9: Data Detectives

Core 5 now defines median and mode. Challenge 1 and 2 (slide items) were extended with a justify part and an upper-bound part instead of being replaced, so the slide diagrams still fit; five Challenge items that only repeated the totals method were replaced by a make-up “mean mystery”, misleading averages, a generalise-and-test task and a chained-totals task.

- **Core 1 → Core 1** (extended). Old: Find the mean of 3, 5, 7 and 9.  
  New: Find the mean of 3, 5, 7 and 9. Hint: share the total equally, or even out the towers.
- **Core 3 → Core 3** (extended). Old: The mean of 5 numbers is 11. What is their total?  
  New: The mean of 5 numbers is 11. What is their total? Think: if the total were shared equally between 5 people, each would get 11.
- **Core 5 → Core 5** (reworded). Old: Find the median and the mode of 4, 9, 2, 9, 6.  
  New: Find the median (the middle number when they are in order) and the mode (the number that appears most often) of 4, 9, 2, 9, 6.
- **Challenge 1 → Challenge 1** (extended). Old: Five numbers have a mean of 8. One number is removed, and the mean of the other four is 7. Which number was removed?  
  New: Five numbers have a mean of 8. One number is removed and the mean of the other four is 7. (a) Which number was removed? (b) Ali says: “Taking a number out always makes the mean go down.” Is he right? Explain, using an example.
- **Challenge 2 → Challenge 2** (extended). Old: A basketball player’s mean score for 9 games is 30 points. How many points must she score in the 10th game to raise her mean to 32 …  
  New: A basketball player’s mean score for 9 games is 30 points. (a) How many points must she score in the 10th game to raise her mean to 32? (b) The most she has ever scored in one game is 60. What is the highest mean she could have after game 10?
- **Challenge 3 → Challenge 7** (replaced). Old: Five whole numbers have a mean of 6, a median of 5 and only one mode, 2. What is the largest the biggest number can be?  
  New: Make up your own “mean mystery” like Think Harder 8: choose five whole numbers, then write clues (any of mean, median, mode, smallest, largest) that give ONLY your numbers. Swap with a partner. Can they find a different set that fits your clues? The old item is kept as Challenge 6.
- **Challenge 4 → Challenge 4** (replaced). Old: Can the mean of 5 whole numbers be bigger than 4 of them? Give an example.  
  New: A shop has 10 staff. Nine earn $2000 a month and the manager earns $11 000. Work out the mean, the median and the mode of their pay. The manager wants an advert saying “our staff are well paid”: which average should she use? Which average would a worker use to say the pay is low?
- **Challenge 5 → Challenge 5** (replaced). Old: The mean of 4 numbers is 15. One of the numbers is changed and the mean becomes 18. By how much was that number changed?  
  New: The numbers 1 and 5 have a mean of 3. Ali says: “If I add 3 to every number, the mean goes up by 3. If I multiply every number by 3, the mean is multiplied by 3. If I square every number, the mean is squared.” Test each of his three claims. Which are true? Explain with totals.
- **Challenge 6 → Challenge 6** (replaced). Old: Jun’s program adds 5 to every item in a list of 10 numbers, then doubles every item. The mean was 7 before. What is the mean now?  
  New: Five whole numbers have a mean of 6, a median of 5 and only one mode, 2. What is the largest the biggest number can be?
- **Challenge 9 → Challenge 9** (extended). Old: A group of 8 children has a mean mass of 41 kg. When their tutor joins, the mean mass of all 9 becomes 44 kg. What is the tutor’s …  
  New: A group of 8 children has a mean mass of 41 kg. When their tutor joins, the mean mass of all 9 becomes 44 kg. Then one more person joins and the mean of all 10 becomes 43 kg. What is the tutor’s mass? What is the mass of the last person to join?

### Lesson 10: Showcase Challenge

Core gains small scaffolds (write terms out, break 60 into smaller products, thermometer). Two one-step Challenge items became a make-up mixed-topic question and a turtle-closing puzzle.

- **Core 1 → Core 1** (extended). Old: Find the 20th term of 5, 8, 11, 14, …  
  New: Find the 20th term of 5, 8, 11, 14, … (Write the terms out, or look for a shortcut.)
- **Core 2 → Core 2** (replaced). Old: Write 60 as a product of prime numbers.  
  New: Break 60 into smaller and smaller multiplications until every number is prime (2, 3, 5, 7, 11, …). Write 60 as a product of primes.
- **Core 3 → Core 3** (reworded). Old: The temperature is −3 °C. It falls by 5 °C. What is it now?  
  New: The temperature is −3 °C (3 degrees below zero). It falls by 5 degrees. What is it now? Count down on a thermometer drawing.
- **Challenge 4 → Challenge 7** (replaced). Old: What is the smallest number with exactly 6 factors?  
  New: Make up a challenge question that mixes TWO topics from the programme (for example primes and the clock, or sequences and negative numbers). Write the question, the answer and the working. Swap with a partner and solve each other’s.
- **Challenge 5 → Challenge 5** (reworded). Old: A turtle draws a star: repeat 5 times (move 100, turn 144°). How many full turns does the turtle make altogether?  
  New: A turtle repeats [move 100, turn ↻ 150]. After how many repeats does it first face the way it started? What does it draw, and how many times does it go round?

## Deck keys regenerated

Regenerated with `python3 rebuild/gen_p6l6.py` and `gen_p6l9.py`, then `python3 levels/restyle.py split/p6l6 split/p6l9`; previews checked for overflow (none). Only the following slide content changed:

- **p6l6-stretch** (early finishers): item 2 is now “1200 rolls, numbers bigger than 4, the program says 391, is something wrong?” with the new answer in the notes (about 400; 391 is close).
- **p6l9-challenge**: items 1 and 2 have the new (b) parts. **p6l9-chwalk**: titles read Q1(a) and Q2(a); the fourth card of each column now shows (b) (above the mean lowers it, below raises it; best case 270 + 60 = 330, 33); notes carry the full (b) answers. `p6l9-chdiag` is unchanged (the diagrams still match part (a)).
- Because the current `levels/restyle.py` adds a `data-deco` marker, every slide file in `split/p6l6` and `split/p6l9` also shows that one-attribute difference against the old files. I regenerated Lessons 5, 7, 8 and 10 as a check (identical slide text) and restored their previous files, so only Lessons 6 and 9 carry the marker.
- Slide answers, workbook keys (`lesson.key`), tutor script notes and exit tickets: unchanged, because none of them quoted a changed item. The tutor guide, weekly pack, question bank and parent pack read the bank, so they follow automatically.

## Final page counts (after `bash levels/build_level.sh 6` and `python3 levels/mkextras.py 6`)

| File | Before | After |
|---|---|---|
| Student workbook (`p6/`) | 45 | 45 |
| Tutor guide (`p6/`) | 68 | 71 |
| Weekly Dose of Thinking Math (`p6/`) | 25 | 25 |
| Question Bank (`outputs/designed/`) | 20 | 28 |
| Weekly Email Pack | 12 | 12 |
| Free Taster | 5 | 5 |
| What Learners Get | 1 | 1 |

Workbook: the page structure is identical to the old file, page for page (2 worksheet pages, 2 Think Harder pages per lesson, cut-outs, certificate). Weekly student/tutor slices: week 1 11/11, week 2 8/11, week 3 8/12, week 4 8/12, week 5 9/12 pages.

**Why the Question Bank grew from 20 to 28 pages:** each lesson has one page in `levels/mkextras.py`; two lessons already spilled in the old file. The new Core items carry their scaffolds, and the problem-posing items are longer, so every lesson now spills a few lines onto a second page. The answer key is still 6 pages. This is a layout cost, not a content problem; trimming it would need shorter scaffolds or a layout change in the shared `mkextras.py`, which I did not edit. The tutor guide grew by 3 pages for the same reason (it prints the Think Harder pages with answers).

## Things the lead may want to do

- `levels/mkextras.py` still describes CORE as “builds fluency with the main idea”. Under the new principle Core is a low-floor entry; a one-line wording change in the shared file would match.
- The Scratch editor check (7 points) and the missing `.sb3` starter files from `fixes_p6.md` are still open and unrelated to this rework.
