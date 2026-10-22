# Math Inquirers P4 (ages 9-11): student journey review and diagnostic check

Read-only review. No content file was edited. Helper script: `docs/audit/journey_p4.py` (`python3 -I docs/audit/journey_p4.py [load|time|diag|heat|lessons|all]`). Every number below that is computed comes from that script.

## Method and honest limits

- Sources read: all ten `p4/content/lN.js` (lesson, script, `gaps` export, Think Harder bank), `p4/data.js`, `workbook_html.js`, `guide.js`, `kit.js`, the real `split/p4lN` slides and notes, the built 57-page workbook PDF (pages rendered and checked), `diag/content/p4.json`, `diag/build_diag.py`, `docs/levels_and_placement.md`, `docs/gifted_research.md`. The placement doc and `build_diag.py` changed on disk while I worked; I used the current versions.
- The three personas are simulated from the written material. Nothing here is observed child data. Scores are my judgement, and the per-item success probabilities in Part 2 are my estimates, not measurements.
- Scale deviation: the brief says difficulty "3 = just right" but also "5 = best". A mean of six scores only works if 5 is good everywhere, so for criterion 2 I score **5 = just right** and put the direction in the note (TOO HARD / TOO EASY / A BIT HARD). The heatmap is a mean of the six scores.
- Template (every lesson, slide labels sum to 89 min): check 1-4, warm game 4-6, quick questions 6-8, explore 8-18, mini-lesson 18-30, brain break 30-34, page 1 in pairs 34-50, check 50-53, teach before page 2 53-58, page 2 solo 58-76, check 76-80, talk 80-85, exit ticket 85-88, reflection 88-90. Lesson 6 is 2 min shorter on page 1.

## The new items: do they label, embarrass or hurt anyone?

**Warm-up check (minute 1-4, two questions, "write your answer AND one sentence that says why").**
- Every check tests the lesson's NEW idea before it is taught (L1 factors/multiples, L2 the halfway rule, L3 order of operations, L5 0.8 vs 0.75). It is a cold test of something the child has not been told. A LOW child gets two questions they cannot yet know in the first 4 minutes, and the written reason doubles the load. The slide carries no "this is not a test, wrong answers help me teach" line; only the tutor script does. Add it to the slide (fix 3 below).
- Reading load of the checks is mostly fine (8-30 words per item), but L4 Q1 (29 words), L7 Q1 (30 words, spoken room dimensions with no picture), L9 Q2 (29 words) and L10 Q2 (23 words) are long for a slow reader in 90 seconds.
- The check feeds the fast track. So a check mark has a consequence, and the children can work that out.

**Fast track.**
- The rule: BOTH check answers right and a reason given. The HIGH child who rushes and writes no reason is excluded, which is the child who most needs the harder pages.
- The tutor note says "label nobody" and "it changes every lesson". But the **student workbook prints the box to every child**, on the same page as the reflection: "Fast track. Got BOTH warm-up check questions right and can say why? Your tutor may send you straight to the Think Harder pages". Page headers also say "Challenge (for strong thinkers)" and "THINK HARDER". A LOW child turning to that page to reflect reads who is fast, and who is not. This is the single biggest labelling risk in the new material. Move it to a tutor-only note.
- The guide says fast-track children "can work on camera beside the group or share a breakout room". A breakout of the same four children every lesson is a visible ability group, whatever the note says.
- No re-pairing rule when a child leaves a pair at minute 34. A LOW child whose partner is sent off is left alone on a pair page at the moment the page starts.
- The fast-track child still joins explore, mini-lesson, page checks, talk and exit ticket, so they are not cut off. But they skip the 5-minute teach-before-page-2 and the page-1 and page-2 checks for pages they never did, so they sit through checks on pages they have not done (HIGH social score 3).

**Open investigation.** Content is the best new material in the level (L2 double rounding, L5 "is there a next decimal", L8 "row of four", L10 ring toss). But it sits on the last worksheet page, behind Think Harder and Challenge, so only fast-track or early finishers meet it. LOW and MIDDLE children never get a low-floor open task in class apart from the explore. The open investigations are good enough to run for the whole group in the 80-85 talk slot for some lessons.

**Reflection ("What was hard?").**
- Wording is kind: "No answer is wrong. Nobody marks this." The prompts are "hardest part was / I got unstuck by [tick boxes] / next time I will try".
- It is mostly safe, but (a) every option presupposes the child got unstuck; there is no "I am still stuck" or "I asked my tutor" tick, so a child who did not get unstuck has to invent an answer or leave a blank; (b) it is not said to be private or voluntary to share; (c) it falls at minute 88-90, after the exit ticket, with about two minutes, when tired children rush; (d) it shares a page with the Fast track box (above) and the Open investigation, so a child who skipped Think Harder opens a page that looks like it was for someone else.
- The model answers in `gaps.reflect` (for example L2 "working out which way a number like 450 rounds") are good: they name a strategy, not a feeling.

## Heatmap (mean of six scores; 5 is best)

| Lesson | LOW | MIDDLE | HIGH |
|---|---|---|---|
| 1 Factor Hunters | 2.83 | 3.83 | 3.83 |
| 2 Big Number Puzzles | 2.50 | 3.67 | 3.83 |
| 3 Operation Detectives | 2.17 | 3.50 | 4.00 |
| 4 Fraction Frontier | 3.00 | 3.67 | 3.67 |
| 5 Decimal Detectives | 2.17 | 3.33 | 3.83 |
| 6 Angle Turns | 3.50 | 4.00 | 3.33 |
| 7 Area Architects II | 3.17 | 3.83 | 3.83 |
| 8 Symmetry and Nets | 4.00 | 4.17 | 4.00 |
| 9 Data Detectives | 3.33 | 3.67 | 3.00 |
| 10 Challenge Day | 3.00 | 4.00 | 4.67 |
| **Level mean** | **2.97** | **3.77** | **3.80** |

Criterion means across the ten lessons (LOW / MIDDLE / HIGH): Participate 3.1 / 3.9 / 5.0; Difficulty fit 2.2 / 3.4 / 2.9; Fun 3.4 / 4.0 / 4.0; Confidence 2.9 / 3.6 / 4.0; Motivation 3.4 / 3.9 / 3.8; Social/online 2.8 / 3.8 / 3.1.

Reading: the program serves MIDDLE well. HIGH is fine on fun and confidence but is under-challenged on core (difficulty fit 2.9). LOW is poorly served: difficulty fit 2.2 is the lowest number in the whole table, and Lessons 1-5 (the number block) are where it breaks. Lessons 6 and 8 (hands-on, low reading) are where LOW recovers.

## Part 1 detail: every lesson, every persona

Evidence notes name the slide, page or item. "Core" = the two workbook core pages. "Ws" = worksheet page.

### Lesson 1: Factor Hunters

**LOW** (mean 2.83)

| Criterion | Score | Evidence |
|---|---|---|
| Participate | 3 | Check Q1 (lifts at every 3rd and 5th floor) can be started by listing; Q2 (Siti's '30, 60, 90') needs the factor/multiple split that is only taught at min 18-20 |
| Difficulty fit | 2 | TOO HARD: ws1 Q1 pairs of 48 (3 x 16, 4 x 12), ws2 Q5 table and Q6a four-clue riddle solo in 18 min; three new ideas in 5 min before page 2 |
| Fun / interest | 3 | 24-tile rectangles (explore) and the bus time line are concrete; Fizz-Buzz is fun until you slip |
| Confidence | 3 | 'Not this one' is modelled (we1, we2) and Q1 gives '1 x 48' plus empty boxes, but the min-1 check is cold and Q6b asks for a written example |
| Motivation | 3 | Buses and bead packs give a purpose; progress is shown only by the end stamp |
| Social / online | 3 | Fizz-Buzz goes round the video tiles and 'a child who slips starts the next round' is public; page-1 partner may be sent to Think Harder at min 34 |

**MIDDLE** (mean 3.83)

| Criterion | Score | Evidence |
|---|---|---|
| Participate | 4 | Both check items can be started; Q2 may get an answer with no reason |
| Difficulty fit | 4 | Page 1 right; page 2 Q5/Q6 stretch but are reachable; reading is easy (329 words over two pages) |
| Fun / interest | 4 | Tiles, Fizz-Buzz, bus puzzle |
| Confidence | 4 | Worked examples, boxes on Q1 and the 'Stuck?' hint line carry them |
| Motivation | 3 | Nothing shows progress inside the lesson except the stamp |
| Social / online | 4 | Pair talk on explore and ws1, sentence starters at talk time |

**HIGH** (mean 3.83)

| Criterion | Score | Evidence |
|---|---|---|
| Participate | 5 | Both check items solved in seconds |
| Difficulty fit | 3 | TOO EASY: quick questions, 12-min mini-lesson and ws1/ws2; Think Harder (Q1-3 same-type, Q4 and locker Q7 good) only starts at min 34 |
| Fun / interest | 4 | Locker problem (Challenge Q7) and 'find ALL pairs of bus gaps' (Open) are the highlights; the warm games are trivial |
| Confidence | 4 | Early wins; risk is skipping the one-sentence reason and missing the fast track |
| Motivation | 4 | Open investigation gives a real goal (six gap pairs, systematic list) |
| Social / online | 3 | 7 min of page checks and 5 min of teach-before-page-2 on pages they skipped; works alone from 34 to 80 |

### Lesson 2: Big Number Puzzles

**LOW** (mean 2.50)

| Criterion | Score | Evidence |
|---|---|---|
| Participate | 2 | Check Q1 ('which could be the real number: 7 499, 7 500, 8 499, 8 500') needs the halfway rule taught at min 18; Q2 asks why both answers are 50 000, so nothing to write at min 1 |
| Difficulty fit | 2 | TOO HARD: ws1 Q1 12-cell rounding table with 63 950, 9049, 80 503 traps; Q2 smallest/largest (62 500 / 63 499); ws2 Q4a riddle has four clues |
| Fun / interest | 3 | Place It Right (irreversible boxes) is a good game; the digit-card explore needs the 'no 0 card so start 49' insight |
| Confidence | 2 | Cold check, then page 1 opens on the carry trap ('Watch out for 9s'); Q2b hint 'Start at 5340 and check each one' is the one kind scaffold |
| Motivation | 3 | Stadium-size numbers and 'what can a rounded number hide' are a fair hook |
| Social / online | 3 | Digit cards 0-9 are not in the workbook cut-outs, so a child without them cannot join the explore; '60 045' on whiteboards is public |

**MIDDLE** (mean 3.67)

| Criterion | Score | Evidence |
|---|---|---|
| Participate | 4 | Check items doable by testing the four numbers |
| Difficulty fit | 3 | Page 1 table plus ws2 Q4-Q6 in 18 min is dense; reading 242 words |
| Fun / interest | 4 | Place It Right, digit cards, stadium hook |
| Confidence | 3 | Trap items (63 950) catch most children once; 'Stuck?' number line helps |
| Motivation | 4 | Finding 'ALL' numbers that round to 50 000 has a clear aim |
| Social / online | 4 | Pair explore and compare-and-argue at talk time (Siti/Ravi) |

**HIGH** (mean 3.83)

| Criterion | Score | Evidence |
|---|---|---|
| Participate | 5 | Both check items quick, but the reason sentence must be written |
| Difficulty fit | 3 | TOO EASY for core pages; we4 (two clues) shown at 25-27 is 'no longer on the worksheet' |
| Fun / interest | 4 | Place It Right and the five-digit riddles; Open investigation 'double rounding' (test 1 449 and 1 450) is excellent |
| Confidence | 4 | Quick wins; the double-rounding conjecture is a real discovery |
| Motivation | 4 | Challenge 'how many 5-digit numbers have digit sum 3' and palindrome puzzle give targets |
| Social / online | 3 | Listens to page checks on traps already avoided; solo 34-80 |

### Lesson 3: Operation Detectives

**LOW** (mean 2.17)

| Criterion | Score | Evidence |
|---|---|---|
| Participate | 3 | Check Q1 (one pair of brackets in 2 + 3 x 4 to make 20) is a try-it puzzle; Q2 (Ravi: 10 - 2 x 3 = 24) needs the order taught at min 18 |
| Difficulty fit | 1 | FAR TOO HARD: quick questions 4 800 / 6, 99 x 6, 45 x 20 on whiteboards; ws2 Q6 1 236 / 4 = 309; four methods in 5 min before page 2 |
| Fun / interest | 2 | Target Numbers is a race ('first child to show a correct number sentence wins a point') that the slow child never wins; quick questions are 'boards up together' |
| Confidence | 2 | ws1 Q1a (36 + 14 x 5) is the very trap, Q1c (72 / 8 x 3) is the second; Q7 guess-and-check chains fail in public |
| Motivation | 3 | Number tricks that always end in 7 are a real hook if the child reaches Q5 |
| Social / online | 2 | Speed race and boards-up under time pressure; ws2 has four multi-part items solo, with the tutor unable to see the page |

**MIDDLE** (mean 3.50)

| Criterion | Score | Evidence |
|---|---|---|
| Participate | 4 | Check items workable; Q2 maybe answered as 24 |
| Difficulty fit | 3 | Page 2 is four different tasks (machine, trick, bar model, chains) in 18 min |
| Fun / interest | 4 | Target Numbers, odd/even stand-crouch break, number trick |
| Confidence | 3 | Worked examples good; the trap (36 + 14 x 5) is hit once and corrected |
| Motivation | 4 | 'Why does the trick always give 7?' is a good puzzle |
| Social / online | 3 | Race element helps some, discourages others |

**HIGH** (mean 4.00)

| Criterion | Score | Evidence |
|---|---|---|
| Participate | 5 | Both check items instant |
| Difficulty fit | 3 | TOO EASY: core pages and the mental-maths questions; Think Harder (Challenge Q5 plus/minus puzzle, Q6 Mei's money) is right |
| Fun / interest | 5 | Target Numbers ('can you make 100?'), four 4s, make-any-target Open investigation are real puzzles |
| Confidence | 4 | Fast wins; rushing risk on left-to-right slips |
| Motivation | 4 | Open investigation 'make targets 1 to 12 from 2, 3, 4, 5' gives an aim |
| Social / online | 3 | Waits through ws1 check and the bar-model teach-before while on Think Harder |

### Lesson 4: Fraction Frontier

**LOW** (mean 3.00)

| Criterion | Score | Evidence |
|---|---|---|
| Participate | 3 | Warm 'more or less than a half?' thumbs are low-floor; check Q1 ('9/4 cups of flour') uses improper fractions that are only named at min 13-18 |
| Difficulty fit | 2 | TOO HARD: quick questions 2/3 = ?/12 and 3/4 + 1/8; ws2 Q4 five comparisons (4/9 vs 5/8) each needing 'how you know'; five ideas in the 5 min before page 2 |
| Fun / interest | 4 | Pizza slices cut from paper circles are tactile and relatable; the fraction wall is in the cut-outs |
| Confidence | 3 | ws1 Q1 (count shaded fifths) is a sure win; Q4 asks for a written reason four times |
| Motivation | 3 | Pizza and sweet-jar contexts are purposeful; progress not visible |
| Social / online | 3 | Three paper circles must be pre-cut at home; a wrong 'bigger denominator' answer is aired in the talk-time Mei/Ravi claims |

**MIDDLE** (mean 3.67)

| Criterion | Score | Evidence |
|---|---|---|
| Participate | 4 | Thumbs and the pizza explore start everyone |
| Difficulty fit | 3 | Four ideas in 12 min plus five in 5 min is heavy; Q4-Q6 solo in 18 min |
| Fun / interest | 4 | Pizza party, fraction wall |
| Confidence | 3 | Q1 bars and Q3 given bar model give early success; comparing is the hard part |
| Motivation | 4 | 'Find ALL the twelfths' and 'is Mei right?' invite reasons |
| Social / online | 4 | Pairs on bars; thumbs warm-up is safe |

**HIGH** (mean 3.67)

| Criterion | Score | Evidence |
|---|---|---|
| Participate | 5 | Check items fast; the 3/8 vs 3/5 reason is one line |
| Difficulty fit | 3 | TOO EASY: Q1-Q5 and the comparing tools; Challenge (half is 3 more than a third; Siti's book) fits |
| Fun / interest | 3 | Fractions of sets are routine; Challenge and 'fraction between 2/3 and 3/4' are the fun parts |
| Confidence | 4 | Quick wins |
| Motivation | 4 | Open investigation 'which fractions of 24 stickers are whole?' links back to Lesson 1 factors |
| Social / online | 3 | Page checks on pages skipped; work alone |

### Lesson 5: Decimal Detectives

**LOW** (mean 2.17)

| Criterion | Score | Evidence |
|---|---|---|
| Participate | 2 | Check Q1 is the classic 0.8 vs 0.75 and Q2 ('a decimal between 3.4 and 3.5, how do you know it fits?') wants place-value reasoning in 90 seconds |
| Difficulty fit | 1 | FAR TOO HARD: thousandths, steps of 0.1/0.01/0.001, rounding to 1 dp and to whole numbers, rounding backwards, 12-number lists, 2.40 / 6; four ideas in 5 min before page 2 |
| Fun / interest | 3 | Target 5 digit-box game and the 2.36 m ruler link are fun; then the abstract run starts at min 18 |
| Confidence | 2 | Warm2 Q3 (0.8 vs 0.75) is deliberately left unsettled in public; Q3b/Q3c rounding detective; ends on the exit 'order 2.8, 2.08, 2.088' |
| Motivation | 3 | Prices and masses (cans, $9.40 bar model) give purpose |
| Social / online | 2 | Digit and decimal-point cards must be cut at home; 3 rounds of irreversible Target 5 in 2 min is rushed |

**MIDDLE** (mean 3.33)

| Criterion | Score | Evidence |
|---|---|---|
| Participate | 3 | Check Q2 open answer is fine; Q1 many say 0.75 |
| Difficulty fit | 3 | Dense: five teaching slides then page 2 Q4 lists 12 numbers and Q6 needs decimal division |
| Fun / interest | 4 | Target 5, zoom-in lines |
| Confidence | 3 | Misconception (more digits = bigger) is met and corrected; page 1 Q1 zoom lines are tricky |
| Motivation | 4 | Detective theme with 'check every clue' |
| Social / online | 3 | Pairs on page 1; solo page 2 is long |

**HIGH** (mean 3.83)

| Criterion | Score | Evidence |
|---|---|---|
| Participate | 5 | Both check items instant |
| Difficulty fit | 3 | TOO EASY: ordering and rounding; Challenge (2.459 clue, apples and pear) and Open 'no decimal between 0.35 and 0.36?' are right |
| Fun / interest | 4 | Open investigation (is there a next decimal?) is the best idea in the lesson |
| Confidence | 4 | Quick wins on core |
| Motivation | 4 | Closest-to puzzles (Think Harder) and 'make your own' Challenge |
| Social / online | 3 | Waits through three slides on place-value chart and page checks |

### Lesson 6: Angle Turns

**LOW** (mean 3.50)

| Criterion | Score | Evidence |
|---|---|---|
| Participate | 4 | Robot turns and the paper clock are physical; check Q2 (90 - 35) is easy and Q1 can be done with fingers on a compass |
| Difficulty fit | 3 | A LITTLE TOO HARD: protractor (inside/outside scale, c and d turned) is the gate; arithmetic is light; page 2 four tasks in 18 min |
| Fun / interest | 4 | Standing turns, compass dance, paper clock hands-on |
| Confidence | 3 | ws1 Q1 'My estimate' can never be wrong and answers within 2 degrees count; Q5 corner sums are quick |
| Motivation | 4 | Clocks and robots are everyday; stamp |
| Social / online | 3 | Protractor, ruler and paper clock must be at home (only right-angle testers are in the workbook); the tutor cannot see protractor placement; mirrored self-view reverses turns |

**MIDDLE** (mean 4.00)

| Criterion | Score | Evidence |
|---|---|---|
| Participate | 4 | Everyone can turn and answer |
| Difficulty fit | 4 | Right pitch; page 1 measuring takes the time |
| Fun / interest | 4 | Standing and moving, clock puzzles |
| Confidence | 4 | Estimate-first routine protects against 140 vs 40 |
| Motivation | 4 | Fan of angles 'find ALL' has an aim |
| Social / online | 4 | Whole-body activity on camera, pairs on fan |

**HIGH** (mean 3.33)

| Criterion | Score | Evidence |
|---|---|---|
| Participate | 5 | Check items instant |
| Difficulty fit | 2 | TOO EASY: protractor, clock spaces, compass; 'What is the angle at 3:30?' (75) is the first real challenge |
| Fun / interest | 3 | Challenge Q1 (3:30) and the two-squares overlap are good; most of the lesson is procedural |
| Confidence | 4 | Early wins |
| Motivation | 3 | Open 'splitting a corner into three angles' (7 sets) has an aim but only for the fast track |
| Social / online | 3 | Stand-and-turn games are shared; waits through measuring checks |

### Lesson 7: Area Architects II

**LOW** (mean 3.17)

| Criterion | Score | Evidence |
|---|---|---|
| Participate | 3 | Check Q1/Q2 are spoken (6 m x 4 m room, 2 m x 1 m cut from a corner) with no picture; Q2 asks 'explain how you know' the perimeter is unchanged |
| Difficulty fit | 2 | TOO HARD: 21 sub-items in 34 min (1.6 min each); missing lengths, area two ways, staircase, frame; 'layers' (Q4b) undefined |
| Fun / interest | 4 | 12 tiles, A/P cards, 'six tiles' (Q3) and the body-shapes break are hands-on |
| Confidence | 3 | Q3 any six-tile shape works; Q2 table fills row by row; Q4a 'show Ravi' needs a written method |
| Motivation | 4 | Architects with fences and carpets is a good hook |
| Social / online | 3 | 24 paper squares and scissors prepared at home; square-grid page is provided |

**MIDDLE** (mean 3.83)

| Criterion | Score | Evidence |
|---|---|---|
| Participate | 4 | Check Q1 workable from the words |
| Difficulty fit | 3 | Dense page 2 (staircase, cut-and-rearrange, frame) |
| Fun / interest | 4 | Tiles and A/P cards |
| Confidence | 4 | Q3 and Q2 give wins; border Q6c is a good 'what did she forget' |
| Motivation | 4 | Same area, different perimeter is a real surprise |
| Social / online | 4 | Pair tile work |

**HIGH** (mean 3.83)

| Criterion | Score | Evidence |
|---|---|---|
| Participate | 5 | Check items instant |
| Difficulty fit | 3 | TOO EASY on core; Challenge (two paths cross the garden; 9 by 4 cut into a square) is right |
| Fun / interest | 4 | Six-tile perimeters, Ravi's fence (extension), paths puzzle |
| Confidence | 4 | Early wins |
| Motivation | 4 | Open 'bigger area, bigger perimeter?' with all six 24 cm rectangles |
| Social / online | 3 | Work alone from 34; page checks on pages skipped |

### Lesson 8: Symmetry and Nets

**LOW** (mean 4.00)

| Criterion | Score | Evidence |
|---|---|---|
| Participate | 4 | Check Q1 (straight row of 6 squares, can fold paper) and Q2 (H and A, fingers) need almost no reading |
| Difficulty fit | 4 | A BIT HARD in places: fold-in-the-head (ws1 Q1 shapes B, D, F) and drawing mirror images (Q4) are spatial, not arithmetic; no calculations |
| Fun / interest | 5 | Paper cube, dice nets, mirror-partner break, letters with fingers |
| Confidence | 4 | Q3 dice nets use the known 7-sum; ws1 mostly ticks and numbers; cube net is in the workbook |
| Motivation | 4 | 'I made a cube' is visible progress |
| Social / online | 3 | 6 paper squares, tape and scissors must be ready; folding on camera is hard to check |

**MIDDLE** (mean 4.17)

| Criterion | Score | Evidence |
|---|---|---|
| Participate | 4 | Everyone can fold or finger-answer |
| Difficulty fit | 4 | Good pitch; coordinate Q6 (A2, D3) is the stretch |
| Fun / interest | 5 | Nets, dice, mirrors |
| Confidence | 4 | Tick/draw rather than write; Q5 diagonal trap is taught first |
| Motivation | 4 | Eleven nets is a good 'find them all' |
| Social / online | 4 | Pair folding, mirror partner on camera |

**HIGH** (mean 4.00)

| Criterion | Score | Evidence |
|---|---|---|
| Participate | 5 | Check items instant |
| Difficulty fit | 3 | TOO EASY on core; Think Harder (22-square cuboid net, two glued dice) fits |
| Fun / interest | 5 | Design your own dice, X and plus symmetry puzzle |
| Confidence | 4 | Quick wins |
| Motivation | 4 | Open 'row of four' (16 cases) is excellent |
| Social / online | 3 | Works alone; checks on skipped pages |

### Lesson 9: Data Detectives

**LOW** (mean 3.33)

| Criterion | Score | Evidence |
|---|---|---|
| Participate | 4 | Warm 'which graph tells the story' has no numbers; check Q1 (halfway between 100 and 150) is easy; Q2 asks for an abstract reason about scales |
| Difficulty fit | 3 | A BIT HARD: scale reading is fine; 85 - 38 and 70 - 29 regrouping, same-jump table, and Q5 'two shops' scale argument are abstract |
| Fun / interest | 3 | Sugarcane juice and money boxes are fine; plotting 7 points with a ruler can drag |
| Confidence | 4 | Q1a (read Thursday = 75) is a sure first win; table totals can be checked two ways |
| Motivation | 3 | Some purpose in 'catch the misleading graph' |
| Social / online | 3 | Printed blank grid, ruler and two pencils must be ready (the workbook has no graph grid for Lesson 9); 'choose a scale' alone is exposing |

**MIDDLE** (mean 3.67)

| Criterion | Score | Evidence |
|---|---|---|
| Participate | 4 | Everyone can match graph to story |
| Difficulty fit | 4 | Right pitch; Q5 is the stretch |
| Fun / interest | 3 | Graphs are only mildly exciting |
| Confidence | 4 | Reading and totals give early wins |
| Motivation | 3 | 'Is the graph telling the truth?' is the one hook |
| Social / online | 4 | Pair plotting |

**HIGH** (mean 3.00)

| Criterion | Score | Evidence |
|---|---|---|
| Participate | 5 | Check items instant |
| Difficulty fit | 2 | TOO EASY: reading values, listing changes, table totals; only Challenge (tanks cross at 4 h) and the scale argument stretch |
| Fun / interest | 3 | Mostly reading; the misleading-graph idea is nice |
| Confidence | 3 | Quick wins but little to be proud of |
| Motivation | 2 | Open 'three plants' is a calculation table; little curiosity |
| Social / online | 3 | Waits through slides on reading and totals |

### Lesson 10: Challenge Day

**LOW** (mean 3.00)

| Criterion | Score | Evidence |
|---|---|---|
| Participate | 3 | Check Q1 (ducks/rabbits, 8 animals, 22 legs) can be guessed or drawn; Q2 (add 7, double, get 30) can be undone; 'Who am I?' grid is easy |
| Difficulty fit | 2 | TOO HARD: four puzzle cards in 5 min; ws1 Q1a (next-door numbers make 552 = 23 x 24), Q1b ($4 pens, $7 notebooks); ws2 Q6 'in 5 years' ages |
| Fun / interest | 3 | Logic and queue puzzles are fun; five puzzle types back to back are not |
| Confidence | 3 | The hook normalises 'you do not know how to start'; the logic grid (Q4) is a likely win; the group 'teach one puzzle' is exposing |
| Motivation | 4 | Certificate, last stamp and a specific thing each child did well |
| Social / online | 3 | Breakout pair per card then report back; talk-time 'teach it in two sentences' |

**MIDDLE** (mean 4.00)

| Criterion | Score | Evidence |
|---|---|---|
| Participate | 4 | Who am I and puzzle cards start everyone |
| Difficulty fit | 3 | Hard but sequenced: four ways in are taught one at a time |
| Fun / interest | 4 | Puzzles are the fun part |
| Confidence | 4 | Strategy names ('suppose', 'work backwards') give hooks; certificate |
| Motivation | 5 | No new topic; certificate; 'tell a specific thing' |
| Social / online | 4 | Pairs and talk time |

**HIGH** (mean 4.67)

| Criterion | Score | Evidence |
|---|---|---|
| Participate | 5 | Cards and Who am I are instant |
| Difficulty fit | 4 | Right: competition-style puzzles; the heads-and-legs suppose method and Challenge are new |
| Fun / interest | 5 | Four puzzle stations, logic grid, make-your-own heads-and-legs |
| Confidence | 5 | Real struggle on real puzzles with a method to try |
| Motivation | 5 | Open 'ring toss scores' (3 and 5 points) find ALL; certificate |
| Social / online | 4 | Breakout pairs, teach to the group |


## Moments where a child would feel stupid, bored, lost, left out, rushed or waiting

| Lesson | Persona | Moment | Feeling |
|---|---|---|---|
| 1 | LOW | Check Q2 (Siti's "30, 60, 90") before factor and multiple are taught | lost |
| 1 | LOW | Fizz-Buzz "a child who slips starts the next round", in front of the video tiles | stupid |
| 1 | LOW | Partner sent to Think Harder at minute 34, no re-pairing rule | left out |
| 2 | LOW | Check Q1 needs the halfway rule taught at minute 18 | lost |
| 2 | LOW | Digit cards 0-9 are not in the cut-out kit | left out |
| 2 | LOW | ws1 Q1 table (12 cells, 63 950, 9049, 80 503 traps) | lost, rushed |
| 3 | LOW | Target Numbers is a race ("first child to show wins a point") | stupid |
| 3 | LOW | Quick questions 4 800 / 6, 99 x 6, 45 x 20 on whiteboards held up together | stupid, rushed |
| 3 | LOW | ws2 Q6 1 236 / 4 and four methods in 5 minutes before page 2 | lost, rushed |
| 4 | LOW | "Bigger denominator = bigger fraction" is aired in public at talk time | stupid |
| 4 | LOW | "Write how you know" four times in Q4 (slow writer) | rushed |
| 4 | LOW | Improper fraction used in check Q1 before it is named | lost |
| 5 | LOW | Warm2 Q3 (0.8 vs 0.75) deliberately left unsettled | lost |
| 5 | LOW | Thousandths, rounding backwards, 12-number list, 2.40 / 6, all in one lesson | lost, rushed |
| 6 | LOW | Protractor inside/outside scale; mirrored self-view reverses turns | lost |
| 7 | LOW | 21 sub-items in 34 min; "layers" (Q4b) never defined; check Q1/Q2 have no picture | lost, rushed |
| 9 | LOW | No graph grid in the kit; "choose a scale" alone is exposing | left out |
| 10 | LOW | Four puzzle cards in 5 min; "teach one puzzle" to the group | rushed, exposed |
| 2-9 | HIGH | 28 whole-group minutes at core level; ws1 and ws2 core pages | bored |
| 3, 6, 9 | HIGH | Core pages and mental-maths questions | bored |
| all | HIGH | Page checks (50-53, 76-80) on pages skipped by the fast track | waiting |
| all | MIDDLE | "Try" slides skipped when time runs short (they are marked optional) | rushed |

## The 5 weakest lesson-persona cells, with fixes

Ties: the fifth place is a three-way tie at 3.00 between LOW L4, LOW L10 and HIGH L9; I took HIGH L9 because it is the only weak cell that is not LOW, and give one-line fixes for the other two.

**1. LOW, Lesson 3 Operation Detectives: 2.17 (difficulty fit 1).**
- Problem: speed race, whiteboards-up mental division, four methods in five minutes, ws2 Q6 1 236 / 4.
- Fix A. Target Numbers slide, replace "The first child to show a correct number sentence wins a point." with: "Everyone writes ONE number sentence that makes the target. Then find a second way. Show your tutor when you have two." (no race; everyone wins).
- Fix B. Quick questions, replace 4 800 / 6, 99 x 6 and 45 x 20 with 48 / 6, 9 x 6 and 4 x 20 on the core slide, and keep the originals as the "Try next" line.
- Fix C. ws2 Q6: replace "1 236 / 4" with "124 / 4" on the core page and move the original to the Think Harder bank.
- Fix D. Teach-before-page-2: cap it at two methods (bar model and bracket order) and move the other two to the optional "try" slides.

**2. LOW, Lesson 5 Decimal Detectives: 2.17 (difficulty fit 1).**
- Problem: the densest lesson (thousandths, steps of 0.1/0.01/0.001, rounding to 1 dp and to whole numbers, rounding backwards, 12-number lists, decimal division 2.40 / 6).
- Fix A. Slide warm2 Q3: after "do not settle it" add a closing line on the next slide: "0.8 is the same as 0.80. 0.80 is bigger than 0.75." so no child is left holding the misconception.
- Fix B. Core page: make Q4 a list of 6 numbers (not 12) and move the 12-number list to Think Harder; take the "rounding backwards" item off the core page.
- Fix C. Q6 (2.40 / 6): replace with "$2.40 shared by 6 children. How much each?" with a bar model already drawn, or move to Think Harder.
- Fix D. Kit: add the decimal-point card and digit cards to the cut-out page.
- Fix E. Longer term: split Lesson 5 into two sessions (place value and ordering, then rounding), or drop rounding to 1 dp from the core.

**3. LOW, Lesson 2 Big Number Puzzles: 2.50.**
- Problem: cold check on the halfway rule; digit cards not in the kit; 12-cell rounding table opens page 1.
- Fix A. Check Q1: add the line "Hint: draw a number line from 7 000 to 9 000." on the check slide.
- Fix B. ws1 Q1: reduce the table to 6 cells (47 285 all three columns, 63 950 hundreds and thousands) so the guaranteed win comes first, and move the rest to the "Try next" box.
- Fix C. Kit: add digit cards 0-9 to the cut-outs (or "Please write the digits on 10 pieces of paper before the lesson" in the pre-lesson text).
- Fix D. Q2a: keep the printed number line, add "63 500 is halfway to 64 000. Does it round up or down?" as the first scaffold.

**4. LOW, Lesson 1 Factor Hunters: 2.83.**
- Problem: factor/multiple check before it is taught, public Fizz-Buzz slip, partner leaves at 34.
- Fix A. Fizz-Buzz slide: replace "A child who slips starts the next round." with "If you slip, no problem: say 'My go again' and pick someone to start the next round."
- Fix B. Guide, fast track: add "If a pair loses a member, join the remaining child to another pair or to the tutor at once. Never leave a child alone on page 1."
- Fix C. Check Q2: add "Hint: a multiple is in the times table. A factor goes INTO the number." to the check slide, or swap Q2 for a prompt that does not need the word.

**5. HIGH, Lesson 9 Data Detectives: 3.00.**
- Problem: reading values, listing changes and table totals on core; the "three plants" open task is a calculation table.
- Fix A. Core slides: after the Thursday = 75 read-off add "Now invent your own 'misleading' version of this graph by changing the scale. How does the story change?" as an early-finisher task on the ws1 slide (finished-early line).
- Fix B. Open investigation: replace the "three plants" table with "A newspaper says 'Sales have doubled!' Draw the graph that would make this true. Draw one that would make it look flat. Which is honest, and why?"
- Fix C. ws1 slide: add "Finished early? Turn to the Think Harder page."
- Other ties: LOW L4: add a bar model for 4/9 vs 5/8 to the core item and cut the written reason to one of the four items; LOW L10: reduce the puzzle-card run from four to three in the teach block and let the child choose which to "teach" at talk time.

## The 3 strongest cells (and why)

1. **HIGH, Lesson 10 Challenge Day: 4.67.** Competition-style puzzles with a method to try, real struggle, a certificate, a specific piece of praise. The only cell where the high child is stretched in the first hour.
2. **MIDDLE, Lesson 8 Symmetry and Nets: 4.17.** Paper cube, dice nets, mirror partner on camera, tick/draw answers, "find all eleven nets".
3. **LOW, Lesson 8: 4.00** (tied with HIGH L8, MIDDLE L6 and MIDDLE L10). The best lesson for the child who struggles: hands-on, almost no reading, no calculation, a finished object ("I made a cube"). Use it as the template for the number lessons: a physical start, a visible product, no abstract run in the first 10 minutes. Caveat: it needs 6 paper squares, tape and scissors at home.

## Level-wide patterns

**Pacing.** The template is identical for every lesson (computed: whole-group core-level content is 28 min, L6 30; page work is 34 min, L6 32). Page-1 and page-2 time is fixed whatever the item count: L7 has 21 sub-items in 34 min (about 1.6 min each) while L8 has 10. Teach-before-page-2 packs 3-4 non-optional ideas into 5 min (1.2-1.7 min per idea; L4 and L5 have four ideas at 1.2 min each). The optional "try" slides (2-4 per lesson, 2-6 min), which are the guided practice LOW needs most, are the first thing a tutor drops under time pressure.

**Reading load (core pages, computed from `workbook_html.js`).**

| L | words | FK grade | main Qs | sub-items | explain prompts | longest item (words) |
|---|---|---|---|---|---|---|
| 1 | 329 | 3.3 | 6 | 14 | 3 | 35 |
| 2 | 242 | 3.5 | 6 | 15 | 1 | 30 |
| 3 | 257 | 2.7 | 7 | 15 | 1 | 25 |
| 4 | 204 | 2.4 | 6 | 13 | 1 | 25 |
| 5 | 230 | 1.8 | 6 | 15 | 1 | 21 |
| 6 | 210 | 3.2 | 6 | 11 | 0 | 22 |
| 7 | 315 | 4.5 | 6 | 21 | 3 | 21 |
| 8 | 187 | 2.6 | 6 | 10 | 3 | 28 |
| 9 | 269 | 3.2 | 5 | 12 | 3 | 28 |
| 10 | 304 | 2.8 | 6 | 13 | 0 | 34 |

The language level is fine (grade 2-4.5). The load is in the number of sub-items, and in the written "explain" prompts for slow writers, not the vocabulary. Think Harder and open pages run about 409-513 words, roughly twice the core pages. Unexplained notation and words: "layers" (L7 Q4b), "improper fraction" (L4 check, before it is named), "factor" in the diagnostic (see Part 2).

**Wait time for HIGH.** About 28 minutes per lesson are whole-group at core level (check, warm game, quick questions, explore, mini-lesson), which is where HIGH waits. The Think Harder pages only start at minute 34 and only for fast-track children; a HIGH child who rushed the check starts at minute 34 with everyone else. ws1 slides carry no "finished early" instruction. HIGH participate scores are all 5, but difficulty fit averages 2.9.

**Guaranteed win for LOW in the first 10 min of the worksheet (minutes 34-44).**
- Clear: L4 (Q1 count shaded fifths), L9 (Q1a read Thursday = 75).
- Likely: L2 (only if digit cards and number line are at hand), L7 (Q1 given shapes).
- Partial: L1 (Q1 gives 1 x 48 and boxes, but pairs of 48 follow at once), L5, L6 (estimate cannot be wrong, but then measuring), L8, L10.
- No: L3 (Q1a is the 36 + 14 x 5 trap, Q1c is the second trap).
So in 2 of 10 lessons a LOW child has a guaranteed win; in about 4 more it is probable.

**Other patterns.**
- Every lesson opens on a cold check of the NEW idea; the slide has no reassurance.
- The pairing rule is unspecified. LOW should be paired with MIDDLE with defined roles (one writes, one speaks, then swap).
- Pre-lesson preparation falls on families (paper circles L4, paper squares L7-8, a protractor, ruler and paper clock L6, graph grid L9, digit cards L2 and L5, sign and bracket cards L3). The kit has only: fraction wall (L4), square grid (L7-8), dot grid (L8), cube net (L8), right-angle testers (L6).
- Reflection and fast track share a page (see New items).
- Strengths worth keeping: strategy-based feedback in scripts, "Stuck?" hint lines, the "Notice it. Test it. Explain why." routine, estimate-first, hands-on starts in L4, L6, L8, the certificate in L10.

---

# PART 2: Diagnostic check (P4: 4 warm-up from P3 + 6 main + 2 stretch, 30 min)

Files: `diag/content/p4.json`, `diag/build_diag.py`. Parent result page rows: 6-8 join P4 (8/8 with 4/4 warm-up may try P5); 4-5 join with support, or P3 if warm-up 2 or less; 0-3 P3. The doc `levels_and_placement.md` states a different rule (70%+ enrol; 40-69% enrol with support or one level down; under 40% one level down; try up at 90%+). The two use different thresholds and are not reconciled.

## (a) Skill demand and age fairness, per question

All arithmetic verified in Python (`journey_p4.py diag`): 5000-1346 = 3654; 9 x 7 = 63; 2/3 = 8/12; 7 x 6 = 42; factors of 18 are 1, 2, 3, 6, 9, 18; 48 572 to the nearest thousand is 49 000; 12 + 6 x 3 - 4 = 26; 2 3/5 + 1 4/5 = 4 2/5 (22/5); 3.7 + 2.85 = 6.55; 36/2 - 11 = 7. Both stretch puzzles have a unique answer (36; Cara 12, Ben 36).

| # | Question | True skill | Fair at age 9-11? | Comment |
|---|---|---|---|---|
| W1 | 5000 - 1346 | 4-digit subtraction across zeros | Yes, P3 | Hardest warm-up yet it is first; a slip gives an anxious start |
| W2 | 9 x 7 | times-table recall (6-9) | Yes, P3 | Easy for most; a gap here is genuine |
| W3 | 2/3 = ?/12 | equivalent fractions | Yes, P3 (P3 spec: core) | Fair |
| W4 | 7 x 6 area, "with units" | area of rectangle | Yes, P3 | "42 square cm" required in the key; a child writing 42 cm or 42 cm2 loses the mark |
| Q1 | factors of 18 | factors (P4 L1) | **Unfair for P3 finishers** | term not defined on the child sheet; a P3 child may never have heard "factor" |
| Q2 | round 48,572 to nearest 1000 | rounding (P4 L2) | Fair | commas here, spaces in lessons: minor |
| Q3 | 12 + 6 x 3 - 4 | order of operations (P4 L3) | Fair; likely not taught before P4 | in the lessons only taught in L3; good diagnostic of a school-taught skill |
| Q4 | 2 3/5 + 1 4/5 mixed number | adding mixed numbers (P4 L4) | Hard for a P3 child; fair for a P4 child | key accepts 22/5 although the question asks for a mixed number |
| Q5 | 3.7 + 2.85 | adding decimals (P4 L5) | Fair | the key's common error "6.12 or 5.82" is not reproducible: aligning wrongly gives 3.22 (37 + 285) or 5.92; I could not get 6.12 |
| Q6 | perimeter 36, length 11, width? | working backwards from perimeter | Fair, some thinking | errors 25 and 14 are reproducible |
| S1 | number 30-50, multiple of 4 and 6, digits add to 9 | multiples and logic | Fair as a stretch | |
| S2 | Ben 3x Cara, gives 12, equal | bar model transfer | Hard; correct as a stretch | no reassurance printed; children may panic |

Verified in the tutor key: 4346 (borrowing error), 50 (left to right), 25 and 14 (perimeter) are reproducible; "6.12 or 5.82" is not, so replace.

**Coverage gap.** The ten lessons include angles (L6), symmetry and nets (L8) and graphs (L9). The diagnostic has no item on any of them. A child who is fine at number but has never met an angle is not detected; this matters less because those lessons start from scratch, but the "Skills covered" list on the parent page reads as the program's coverage.

**Warm-ups truly from the level below?** Mostly yes. Equivalent fractions, area of a rectangle, 4-digit subtraction and the 6-9 tables are in the repo's P3 spec (core level), and the P3 diagnostic itself uses equivalent fractions and area as core items. Caveat: the P1-P6 level definitions are derived from one school's scheme of work and are not verified against MOE, so this is internal consistency, not an external check. W3 (equivalent fractions) is close to P4 L4 content and could be counted as P4-adjacent.

## (b) Six profiles

Method: exact Poisson-binomial distributions plus a Monte Carlo of 20,000 children per profile, with a "day effect" (logit shift, SD 0.6) on top of independent items. Per-item probabilities are my assumptions. Numbers are independent / with day effect.

| Profile | Expected | Result | Placement distribution | Right against lesson demands? |
|---|---|---|---|---|
| A strong-for-age (P4 and above) | warm-up 4/4, main 5-6, stretch 1 | 7-8 | ~95% P4; ~27-29% flagged "try P5" | Yes. But the "try up" check tests P5 content not taught (percent, triangle area, volume): an 8/8 P4 child will likely score 0-3 there and feel it |
| B typical-for-age | warm-up 3, main 4, stretch 0-1 | 5-6 | ~34-36% P4; ~42-51% P4 with support; 11-17% told P3; 3-4% "P3 suggested" | Mostly. Half sit in the 4-5 band, which is correct. One in seven is told P3 by luck, which is the wrong direction for a typical child |
| C weak-for-age | warm-up 1-2, main 2 | 2-3 | ~87-92% P3 | Yes |
| D younger strong (age 9, P3 finishing, strong) | warm-up 4, main 2-3 (unfamiliar topics), stretch 0-1 | 4-5 | ~41-50% P4 with support; ~38-41% P3; ~11-16% P4 | Doubtful. Strong, but has not met factors, mixed numbers or order of operations. The result is a coin flip; both P3 and P4-with-support are defensible, and the program does not say which |
| E older weak (age 11, weak) | warm-up 2, main 2 | 2-4 | ~70-75% sent to P3 | Right on skill, wrong socially: the age band for P3 is 8-10, which excludes an 11-year-old. The result page gives no route for this child |
| F guesser/rusher | warm-up 2-3, main 3 | 3-5 | ~60-62% P3; ~26% P4 with support; 3-7% P4 | Wrong for a bright child who rushes. A blind guesser (mean 1.21/8, P(>=4) 0.8%, P(>=6) ~0) is correctly caught. The rusher is not a guesser; it is a slip-prone, capable child who is mis-placed low |

## (c) Cut scores, luck and warm-ups

Exact binomial for eight equally difficult items (P(6-8), P(4-5), P(0-3)):

| p per item | P(6-8) | P(4-5) | P(0-3) |
|---|---|---|---|
| 0.50 | .145 | .492 | .363 |
| 0.60 | .315 | .511 | .174 |
| 0.70 | .552 | .390 | .058 |
| 0.75 | .679 | .294 | .027 |
| 0.80 | .797 | .193 | .010 |
| 0.90 | .962 | .038 | 0 |

- An 8-item score has an SD of 1.2-1.4 marks. A child who truly gets 75% of items right lands in the "join" band only 68% of the time, and falls into 4-5 about 29%. So **one child in three who is placed correctly on skill is shown a "support" or "step down" message**.
- Luck-proofing: a blind guesser is safe (below 1% reach 4). The risk is not luck upward, it is slips downward, and the narrow band structure.
- The warm-up rule (2 or less of 4 means P3): P(<=2 of 4) = .688 at p=.5, .348 at p=.7, .181 at p=.8, .052 at p=.9. A child with 80% skill on the level below has an 18% chance of being told to step down, from a four-item screen. And W1 (the hardest) is first.
- 8/8 with 4/4 may try the level up: P(12/12) = .069 at p=.8, .28 at p=.9, .54 at p=.95. Rare, mostly right, but the "try up" content (see A) is from next year.
- The program documents and the builder define different bands (percent versus raw marks). Keep one.

## (d) Parent result page and tutor key wording

Things that could discourage a child or parent:
- "Not yet?" heading above a yellow box. The word "Not yet" is a label on the child. Replace with a neutral heading (see e).
- Row "0 to 3: We suggest [P3]. The ideas build step by step, and a confident start matters more than a fast one." A directive, plus a reassurance that reads as a consolation. "Not a failure" plants the word.
- The result page has no age check, no "not taught yet" mechanism, and no route for a child who is old for the lower band.
- "Skills covered" reads as program coverage; it is only the list of things this check touches.
- The child sheet has no stretch reassurance. Two "Brain stretchers" at the end of 30 minutes can look like failure if the child leaves them blank.
- Tutor key: "Common error..." text is helpful but instructs the marker to look for errors; add "Please do not mark in front of your child". Key says "accept equivalent forms" in the header but Q4 requires "square cm" with no leeway.
- The file mixes "ages 9-11" and "Ages 8-10 (P3)", so a parent of an 11-year-old reads the lower level as not for them.

## (e) Recommended exact changes

1. **Reorder the warm-up** so the easiest is first: W2 (9 x 7), W3 (2/3 = ?/12), W4 (area), W1 (5000 - 1346) last.
2. **Q1 text:** "A factor of 18 is a number that divides 18 exactly with nothing left over. Write down all the factors of 18."
3. **Stretch reassurance** above Brain stretchers: "Brain stretchers are hard on purpose. Most children do not finish both, and that is fine. Try one!"
4. **W4 key:** "Accept 42 square cm, 42 sq cm or 42 cm2. If the unit is missing, give the mark and note it."
5. **Q4 key:** "Mixed number preferred: 4 2/5. Accept 22/5 for the mark." (or change the question to "as a mixed number or improper fraction").
6. **Q5 key "Common error":** replace "6.12 or 5.82 (misaligned)" with "3.22 (37 + 285 with the decimal point ignored) or 5.92".
7. **"Not taught yet" box.** Add a tick box next to every main question: "[ ] This has not been taught yet." Rule: 2 or more ticks, tutor chat before the score is used.
8. **Grey-zone chat.** For scores 3-5 (and warm-up 2), "book a free 10-minute chat with the tutor before you decide".
9. **Free swap** between levels through lesson 2, not only before lesson 1.
10. **Result rows, exact wording:**
   - "6 to 8: Join P4 (Ages 9-11). Your child has the foundations and will be well challenged."
   - "4 or 5: Join P4, and expect some support in the first weeks. If the warm-up score is 2 or less, P3 may be a happier start; ask us for a free 10-minute chat."
   - "0 to 3: P3 is likely to be the happier start. Ask us for a free 10-minute chat first. Starting where the ideas feel comfortable is how children get faster later. The age shown for P3 is a guide only: older children are welcome."
11. **"Not yet?" box** becomes: "A lower mark tells us where to start, not what your child can do."
12. **"Skills covered"** becomes "Skills in this check".
13. **Add** "Please do not mark in front of your child." to the key page.
14. **Time:** "Allow up to 40 minutes; stop when your child is tired."
15. **Try-up check:** a 4-question stretch set "from next year", with "It is normal to find these new."
16. **Add** one question each for angles, symmetry/nets and graphs only if the program wants the diagnostic to cover the whole level; otherwise state that it samples number only.
17. **Reconcile** `levels_and_placement.md` with `build_diag.py` (raw-mark bands in one place).

---

# 10-line summary

1. LOW (mean 2.97): not well served by Lessons 1-5; hands-on Lessons 6 and 8 work. Difficulty fit 2.2 is the lowest number in the review.
2. MIDDLE (3.77): well served; the dense page 2 and optional "try" slides are the only worries.
3. HIGH (3.80): safe and engaged but under-challenged until minute 34; Lesson 10 (4.67) is the model.
4. Weakest cells: LOW L3 and L5 (2.17), LOW L2 (2.50), LOW L1 (2.83), then HIGH L9 / LOW L4 / LOW L10 (3.00).
5. Fix 1: remove the child-visible "Fast track" box (and "for strong thinkers") from the workbook; keep a tutor-only note and a re-pairing rule.
6. Fix 2: reflection on its own page with "I am still stuck" and "I asked my tutor" options, voluntary sharing, and not after the exit ticket in the last 2 minutes.
7. Fix 3: put "not a test" on every check slide; add finished-early lines to every ws1 slide; give LOW a guaranteed first win (L2, L3, L5 core pages).
8. Fix 4: move the "try" slides into the teach block, supply digit/sign/decimal cards and a graph grid in the kit, and cut 3-4 ideas in 5 minutes to two.
9. Fix 5 (diagnostic): reorder warm-up, define "factor", add "not taught yet" ticks and a grey-zone chat, rewrite "Not yet?" and the 0-3 row, and allow older children.
10. Does the diagnostic place correctly? **Mostly.** Right for strong, typical and weak profiles (A-C); poor for the younger strong (coin flip), the older weak (age band) and the rusher (about 60% sent down). One in three correctly placed children lands in the support band by 8-item noise.
