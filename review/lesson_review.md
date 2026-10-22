# Math Inquirers Level 1: lesson pitch and slide teachability review

Sources reviewed: `deck/data.js`, all 10 lessons' slide HTML (L1, L5 and L8 read in full, the rest read for every mini-lesson, key idea, stretch, challenge, talk and exit slide), `hp/lessons.js`, `hp/scripts.js`, `hp/workbook.js`, `hp/qbank.json` and the Tutor Guide PDF (L5 section in full).

## 1. Overall verdict

**Pitch: uneven.** The Challenge tier is mostly well judged, and it is the best part of the programme. Core is often plain P1 syllabus (bonds of 10, 1:1 picture graphs, sides and corners), which is too easy for a strong child finishing P1. **Think Harder is the weakest tier.** It often repeats the mini-lesson word for word (L5, L6, L8, L10) or is barely harder than Core, so there is a big jump from Think Harder to Challenge. A few Challenge items assume P2+ ideas ("3 times table", "twice as many", ×, ÷) or are P4-style (ages with a time shift).

**Slides: not teachable on their own. You are right, though "simple" is not quite the problem.** The slides are a *running order*: timings, a task, and the answer in the notes. They are not *teaching* slides. Specifically:
- 30 of the 90 minutes (the worksheet) run on two slides that only list question names ("Q1 skip counting, Q2 find the rule"). The tutor never sees the questions on screen.
- Each lesson teaches 1 or 2 question types in two mini-lesson slides (about 8 minutes). The worksheet has 5 or 6 types. Several are never taught anywhere, on the slides or in the Tutor Guide: queue puzzles (L5), the magic triangle and "two numbers add to 10, one is 2 more" (L2), and fixed-number-of-coins problems (L6).
- The good teaching language already exists in `scripts.js` (the think-alouds) and the Tutor Guide, but none of it is on the slides or in the speaker notes. A tutor would have to teach from a 59-page PDF next to the deck.
- The mini-2 speaker notes are the generic lesson text and often **do not match the slide** (details in section 3).

**Errors to fix now:**
- **L2 extension (exit notes and Tutor Guide) is wrong.** It says a side total of 11 "cannot be done with 1 to 6". It can: corners 2, 4, 6 with middles 5, 1, 3. The L2 Challenge slide gives exactly this answer, so the two contradict each other.
- **L8 mini 1 logic grid** never says each child drinks a *different* drink, so "Raj: milk" cannot be deduced.
- **L7 talk:** "a square with two lines across it" is ambiguous (two diagonals give 8 triangles; a + shape gives 0).
- **× and ÷ in answers P1 children cannot follow:** L4 "12 ÷ 2", "6 groups of 3 plus 2"; L10 "5 + 9 × 3"; L3 "12 pictures × 2".
- **"COMMON MISTAKES" box on the child-facing key-idea slide.** It belongs in the notes. Some entries point to items the tutor cannot see ("figure C", "Q4"). L1's "Reading the gap squares instead of the jump size" is unclear.
- **L8 warm-up "quick questions"** ("Is it more than 10?") are tutor prompts, not questions.

## 2. Lesson-by-lesson pitch

| # | Topic | Core | Think Harder | Challenge | Biggest problem | Fix |
|---|---|---|---|---|---|---|
| 1 | Number patterns | About right | Slightly easy | About right | Mini 1 gives the answer away ("Rule: add 6. What is the 5th number?"). Notes call 20, 40 "the 20 times table". | Reveal steps one at a time (section 3). Add "Is 30 in the pattern?" and "find the rule from the 3rd and 5th numbers". |
| 2 | Number bonds | **Too easy** (Q1–Q3 are P1 Term 1 drill) | **Too easy** (Stretch 5 + 4 = 6 + __ repeats Core Q4) | About right | The two genuinely olympiad items (magic triangle Q5, two numbers Q6) are never taught. The extension is wrong. | Cut Q1 to 2 items. Add a "corners count twice" teach slide and a "sum and difference with cubes" slide. Fix the extension. |
| 3 | Picture graphs | **Too easy** (reading a 1:1 graph is the syllabus itself) | About right (key of 2 is P2: good) | About right ("twice as many" needs a drawn model) | No inference: every answer can be read off directly. | Core: key of 2 or 3, a missing row found from the total, a graph that has lost its key. |
| 4 | Repeating and growing patterns | About right (AB/ABC to the 10th place is easy, matchsticks good) | About right | About right | The methods given (÷, "groups of 3 plus 2") are beyond P1. Mini 2 notes say "15 sticks", the slide says 13. | Teach "the end of each core falls on the 3s numbers". Work backwards by extending the table. |
| 5 | Working backwards | About right | **Too easy** (4 near-identical two-step items; #1 is the mini-lesson example) | **Too hard** (ages now and in 3 years is P4/P5 style) | Queue puzzles (Q4 and talk time) and more/fewer bar stories (Q3) are on the worksheet but taught nowhere. | Add a queue teach slide and a bar-model slide. Mix the Think Harder items. Swap the ages item for a plain sum and difference. |
| 6 | Money combinations | About right (85¢, 70¢ with 4 coins and Sam's 6 coins are good) | **Too easy** (#1 = mini 2, #3 = explore) | About right | Fixed-number-of-coins problems (Q4, Q6) are untaught. The stretch repeats the lesson. | Teach a table with a "number of coins" column. New stretch items. |
| 7 | 2D shapes | **Too easy** (sides/corners table, "who am I") | **Too easy** ("4 equal sides" repeats Core Q3a) | About right | The weakest lesson for a strong P1: mostly naming and counting sides. | Rebuild Core around systematic counting (squares in grids, rectangles in strips) and composing (4-square shapes). |
| 8 | Logic and sorting | About right | About right (but #2 = mini 1) | Uneven (the mislabelled-boxes puzzle is hard; "3/4 times table" wording is P2) | The mini 1 grid is missing its key rule. Line-ups and number riddles are untaught. | Add "each has a different one". Teach line-ups with a drawn row. Say "you say it when counting in 3s". |
| 9 | Length | About right (Q1 easy, Q4 and Q5 good) | About right | Slightly hard (30 cubes cut so pieces differ by 4) | No cm or ruler work although P1 measures in cm. Reverse conversion (12 erasers → clips) is untaught. Notes mismatch. | Add "ruler not starting at 0" items. Teach both directions of unit change with a bar picture. |
| 10 | Mixed review | About right | **Too easy** (#1 and #3 copy mini 1; #2 is basic) | About right | The "mini-lessons" are station puzzles with answers; they teach no strategy. | Turn them into "how to start a puzzle" models (draw it, list it, table it). New stretch items. |

## 3. Slide teachability: what is missing

**Missing across all lessons:**
1. **Worked examples revealed one step at a time.** Mini slides either show the whole solution and then ask the question (L6 mini 2 lists all 4 ways, then asks "How many ways?"; L8 mini 2 sorts the whole Venn diagram, then asks "Why does 6 go in the middle?") or give a bare problem (L5 mini 1 "? → add 6 → 14").
2. **The "why".** Key ideas are rules without reasons. "Repeating: use the length of the core" never shows *how*. "A bigger unit gives a smaller number" has no picture.
3. **We-do practice.** After each example there is no similar question for children to try on whiteboards before the worksheet.
4. **Teach-before-the-worksheet slides** for each question type that was not in the mini-lesson.
5. **Worksheet questions on screen**, with a "how to start" tip and an answer reveal for the go-through.
6. **Speaker notes that match the slide** and contain the think-aloud. Mismatches today: L4 (notes "15 sticks", slide 13), L5 (notes "add 5 → 12", slide "add 5, take away 3, get 9"), L7 (notes describe the sides table), L9 (notes "5-clip desk", slide "4-clip pen"), L2 (the "=" slide's notes are about listing bonds).
7. **New items in Stretch.** Today it often repeats the mini-lesson.
8. **Board-work layouts.** Notes say "Build the table on the board" but never show what it should look like.

### Example A: L5 queue puzzles (currently untaught)
Today the only queue content is the talk slide: *"Ali is 8th from the front and 8th from the back. Why is the answer not 16?"* It never says what the question was. Proposed sequence (3 slides, before worksheet page 2):
- **Teach: Draw the queue.** "Mei is 3rd from the front. 2 children are behind her. How many in the queue?" Click 1: draw ○ ○ ●. Click 2: add ○ ○ behind her. Click 3: count 5. Note: "Always draw circles. Never add the numbers straight away."
- **Teach: Count each child once.** "Ali is 3rd from the front and 3rd from the back." Click 1: ○ ○ ● counted from the front. Click 2: ● ○ ○ counted from the back. Click 3: the shared ● is the same child, so the queue is ○ ○ ● ○ ○ = 5. Click 4: "3 + 3 = 6 counts Ali twice. 6 − 1 = 5."
- **We do:** "4th from the front and 4th from the back?" (7). Then "Mei is 7th from the front of 20. How many behind her?" (13: "20 − 7, because Mei is not behind herself").

### Example B: L1 mini 1
Today: *"Start at 2. What do you add each time? Rule: add 6. What is the 5th number?"* The slide answers its own question. Proposed:
- **Slide 1:** show 2, 8, 14, 20, ? with blank jump arcs. Ask: "How far from 2 to 8?" Reveal +6.
- **Slide 2:** reveal all the arcs (+6, +6, +6). "Check every pair of neighbours." Then the rule: add 6, and 20 + 6 = 26.
- **Slide 3, why it matters:** "Is 30 in this pattern?" Children extend it: 26, 32, so no. "A rule lets us test any number."
- **Slide 4, we do:** 5, 9, 13, __, __ (17, 21), then 31, 28, 25, __ (22, take away 3).

### Example C: L4 mini 1, finding far places without division
Today: *"What colour is the 20th?"*, with notes: "20 = 6 groups of 3 plus 2". Proposed:
- **Slide 1:** the beads with place numbers 1–9 under them. Circle places 3, 6, 9: "Every 3rd bead is the end of a core: always blue."
- **Slide 2:** "These are the numbers we say when counting in 3s." Count 3, 6, 9, 12, 15, 18. "18 ends a core. 19 is red (start again). 20 is blue."
- **Slide 3, we do:** the 14th (12 ends a core, so 13 red, 14 blue), then the 30th (we say 30 when counting in 3s, so it is the end of a core: blue).

## 4. Proposed standard lesson structure (about 24 slides, up from 16)

| # | Slide | Content |
|---|---|---|
| 1 | Title | Objective, materials and time plan in the notes (as now) |
| 2 | Warm-up game | As now |
| 3 | Quick questions | Answers revealed on click, not only in the notes |
| 4 | Explore: task | As now, with the diagram |
| 5 | Explore: talk | Notes: "What we want them to notice" and 2 follow-up prompts |
| 6 | **Teach 1: the idea and why** | One picture that explains the concept |
| 7 | **Worked example 1** | Revealed in 3 or 4 steps; think-aloud in the notes, copied from `scripts.js` |
| 8 | **We do 1** | A similar question on whiteboards; answer on click |
| 9 | **Worked example 2** | The second question type, step-by-step |
| 10 | **We do 2** | As above |
| 11 | Key idea | Child-facing summary only. Mistakes move to the notes. |
| 12 | Brain break | As now |
| 13 | **Worksheet page 1 preview** | Thumbnails of Q1–Q3 with a one-line "how to start" for each |
| 14 | **Teach-before: hardest page-1 type** | e.g. magic triangle, fewest coins, line-up |
| 15 | **Page 1 go-through** | Answers on click, with one model explanation |
| 16 | **Worksheet page 2 preview** | As 13 |
| 17 | **Teach-before: hardest page-2 type** | e.g. queue, two numbers, coins with a fixed count |
| 18 | **Page 2 go-through** | As 15 |
| 19 | Stretch | **New** items, never repeats of the mini-lesson |
| 20 | Challenge | As now |
| 21 | Challenge: see it | As now |
| 22 | **Challenge walk-through** | The solution in steps, for after the attempt |
| 23 | Talk time | As now |
| 24 | Exit ticket + close | Answer on click |

That is **8 slides added per lesson** (about 80 in total). Most of the text already exists in `scripts.js` and the Tutor Guide, so this is mainly moving and splitting content, not writing it fresh. Suggested timing: warm-up 0–8, explore 8–20, teach 20–35, break 35–40, worksheet with teach-befores 40–68, talk 68–78, exit 78–90.

## 5. Harder items to add (all answers checked)

**L1 (Think Harder)**
1. Ali counts from 3 in 4s: 3, 7, 11, … Will he say 39? Will he say 40? *Yes, 39 (…, 35, 39, 43). No, 40.*
2. 50, 46, 42, … What is the first number less than 10? *6 (…, 14, 10, 6).*
3. An "add" pattern has 11 as its 3rd number and 19 as its 5th. What is the rule and the 1st number? *Add 4. 11 − 4 − 4 = 3.*

**L2 (replace Core Q1 and the Stretch)**
1. 13 + 7 = 10 + __ = 4 + __ . *10 and 16.*
2. □ + □ + 4 = 20, and both boxes are the same number. *8.*
3. How many pairs make 20 if both numbers are from 5 to 15? (7 + 13 and 13 + 7 count once.) *6: 5+15, 6+14, 7+13, 8+12, 9+11, 10+10.*

**L3 (Core)**
1. Key ● = 2 children. Apple ●●●, Banana ●●●●●, Orange ●●. How many more chose banana than orange? *10 − 4 = 6.*
2. 25 children voted: apple 8, banana 6, grape 4, and the rest chose orange. Draw the orange row. Which fruit won? *Orange 7; apple wins with 8.*
3. The key is missing. Apple has 4 pictures and 12 children chose apple. Banana has 3 pictures. How many chose banana? *1 picture = 3 children, so 9.*

**L4 (Core)**
1. ★ ● ● ▲ ★ ● ● ▲ … What is the 23rd shape? *●. The 20th is ▲ (end of a core), then 21st ★, 22nd ●, 23rd ●.*
2. Matchstick squares in a row need 4, 7, 10, … sticks. With 20 sticks, how many squares, and how many sticks are left over? *6 squares use 19, so 1 is left.*
3. A, B, B, C, A, B, B, C, … How many Bs are in the first 18 letters? *9 (16 letters give 8 Bs; the 17th is A, the 18th is B).*

**L5 (Think Harder; the first item replaces the ages Challenge)**
1. Ali and Ben have 20 marbles together. Ali has 4 more than Ben. How many each? *Ben 8, Ali 12.*
2. Ben had some stickers. He gave away 6, got 4, then gave away 3. Now he has 10. How many at first? *15 (10 + 3 − 4 + 6). Check: 15 − 6 + 4 − 3 = 10.*
3. Tom is 5th from the front. There are 4 children between Tom and Sue, who is last. How many are in the queue? *10.*

**L6 (Think Harder)**
1. How many ways can you make 40¢ with 20¢, 10¢ and 5¢ coins? *9 (two 20¢: 1 way; one 20¢: 3 ways; no 20¢: 5 ways).*
2. Mei has 6 coins, all 5¢ and 10¢, worth 45¢. How many of each? *Three 10¢ and three 5¢.*
3. What is the fewest number of coins for 95¢ (5¢, 10¢, 20¢, 50¢)? *4: 50 + 20 + 20 + 5. Three coins cannot work: you need a 5¢, and no two coins make 90¢.*

**L7 (Core and Think Harder)**
1. How many squares are in a grid 3 squares long and 2 squares high? *8 (6 small + 2 big).*
2. How many rectangles are in a strip of 4 squares in a row? (A square counts.) *10 (4 + 3 + 2 + 1).*
3. Join 4 same-size squares edge to edge. How many different shapes can you make? (Turns and flips count as the same.) *5: a line, a square, an L, a T and an S/zigzag.*

**L8 (Core and Think Harder)**
1. Ali, Ben, Cara and Dan each have a different pet: cat, dog, fish or rabbit. Cara has the dog or the fish. Cara does not have the dog. Dan does not have the cat or the rabbit. Ali does not have the cat. *Cara fish, Dan dog, Ali rabbit, Ben cat.*
2. Five children stand in a line. Ali is in the middle. Ben is just in front of Ali. Cara is last. Dan is not first. Where is Eve? *First (Eve, Ben, Ali, Dan, Cara).*
3. Numbers 1 to 30: which do you say when counting in 2s AND when counting in 5s? *10, 20 and 30.*

**L9 (Core and Think Harder)**
1. A crayon lies from the 3 cm mark to the 11 cm mark on a ruler. How long is it? *8 cm (not 11).*
2. A pencil is 3 erasers long. A ruler is 2 pencils long. A desk is 4 rulers long. How many erasers long is the desk? *24.*
3. A 15-cube ribbon is cut into 3 equal pieces. How long is each piece, and how many cuts? *5 cubes; 2 cuts.*

**L10 (Think Harder)**
1. Mei thinks of a number, adds 7, takes away 2 and gets 19. Ben does the same and gets 25. How much bigger is Ben's number? *Mei 14, Ben 20, so 6.*
2. 4, 9, 14, 19, … Which number in this pattern is closest to 50? *49.*
3. Ali has 5 coins worth 60¢ and no 50¢ coin. Find every possible set. *Two sets: 20 + 10 + 10 + 10 + 10, and 20 + 20 + 10 + 5 + 5.*
