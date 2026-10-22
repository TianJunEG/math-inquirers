# Student journey review: Math Inquirers P2 (ages 7-9)

Reviewer: read-only pass over `p2/content/l1..l10.js`, `p2/gaps.json`, `p2/workbook_html.js`, `p2/guide.js`, `p2/SPEC.md`, `diag/content/p2.json`, `diag/build_diag.py`, `docs/gifted_research.md`, `docs/levels_and_placement.md`, and the rendered slide notes in `split/p2l*/project/slides` (precheck, reflect, warm1). Arithmetic and the diagnostic simulations are in `docs/audit/journey_p2.py` (run `python3 -I docs/audit/journey_p2.py`).

Caveats up front. (1) The 1-5 scores are my judgement from reading the real pages, not observed children. (2) The diagnostic simulations use per-question success rates I assumed for each profile; no pilot data was in the files I read. (3) I read the workbook as text (figures only where the source made their content clear), so a few figure-dependent judgements (L4 Q1, L9 Q1, L10 Q1, L2 Q1/Q2) rest on the figure data in the content files.

Personas used: LOW (struggles, slow reader, not fluent with P2 prior skills), MIDDLE (typical), HIGH (fast, curious, bored by repetition, may rush). Scale columns: P = can participate, D = difficulty fit (3 = just right), F = fun, C = confidence/self-esteem, M = motivation, S = social/online.

---

## How a child meets a P2 lesson (the shared machinery)

Timeline from `guide.js`: 0-1 hook; 1-4 Warm-up check (2 untaught questions in a "new setting", whiteboards up together, one child asked "how do you know?"); 4-8 game plus quick questions; 8-20 explore in breakout pairs (debrief from minute 14); 20-32 mini-lesson; 32-36 break; 36-50 page 1 in pairs; 50-52 check; 52-57 short teaching; 57-69 page 2 ALONE (12 minutes); 69-72 check; 72-80 talk time; 80-88 exit ticket (no talking); 88-90 reflection, closing, stamps (certificate on L10).

Things every lesson shares and that drive many scores below:

- The Warm-up check is built to be unfamiliar ("NEW setting, not recall"). So the LOW child meets two untaught puzzles cold at minute 1, with whiteboards raised together on camera. In 7 or 8 of 10 lessons at least one of the two is likely out of reach for LOW (L1 PRE2, L2 both, L3 PRE1, L5 both, L8 PRE1, L9 PRE2, L10 PRE1).
- The fast-track note is PRINTED on every child's page 1, beside the lesson title: "FAST TRACK. Both Warm-up check answers right AND can say why? Go to THINK HARDER + Open investigation. Rejoin for check-together and talk time." (from `workbook_html.js` `fastNote`, text from `gaps.json` `common.fast`). The tutor script says "Nobody is labelled"; the page does the labelling.
- The Open investigation (the richest task in each lesson) is Q8, printed LAST on the second Think Harder page, after S1-S4 and C5-C7. A fast-track child who works in order will meet it last, if at all.
- The reflection box ("What was hard?") is printed at the very bottom of that same Think Harder page 2, under the banner "Challenge (for strong thinkers)". A child who stayed on the core pages has to turn to a page of Challenge questions they never touched to find it.
- Entry wins for LOW exist in all ten lessons (see level-wide patterns); the pain is in the first 4 minutes before the win, and in the middle of page 1 and all of solo page 2.

---

## PART 1: lesson by lesson

### L1 Digit Detectives (numbers to 1000)
| Persona | P | D | F | C | M | S | Mean | Evidence |
|---|---|---|---|---|---|---|---|---|
| LOW | 4 | 3 | 4 | 3 | 3 | 3 | 3.33 | Digit cards are concrete and Q1a (4 hundreds, 0 tens, 7 ones) is a minute-one win; but PRE2 "5 hundreds and 13 tens" is taught only at 20-32, and Q1b "15 tens" plus a six-number list (Q2a table) sit in the same 14-minute pair slot. |
| MIDDLE | 5 | 4 | 4 | 4 | 4 | 4 | 4.17 | Cards 3,5,8 and "how do you know you have them all" is a real discovery; Q3b "why do 0,5,9 make fewer?" is a good reasoning prompt; exit 6,0,2 reachable. |
| HIGH | 4 | 2 | 3 | 3 | 3 | 3 | 3.00 | Place It Right is mostly luck of the card order; warm-up slide asks "biggest 3-digit number? 999"; Q1-Q3 are routine. PRE1 (cards 4,0,7) is a zero trap that catches a hasty child with "6", so the rushing high child is NOT fast-tracked in the very first lesson and does ~45 minutes of easy work. Mirror numbers (Q8) is great but last. |

Flags: "036 is just 36" (script) uses leading-zero notation nobody has explained; "5 hundreds, 12 tens" is new vocabulary; Q4 piece B (a plus-shaped chart piece with one number) relies on the "down is 10 more" idea that is only taught at 52-57; Q5b (532, 522, 512, ...) crosses a hundred; Q2a asks for six numbers in a three-column table with blank pairs (writing load for a slow writer).

### L2 Missing Digit Mysteries (add/subtract within 1000)
| Persona | P | D | F | C | M | S | Mean | Evidence |
|---|---|---|---|---|---|---|---|---|
| LOW | 3 | 2 | 3 | 3 | 2.5 | 3 | 2.75 | Partners-to-999 explore has no carries (nice win, with a prediction); but PRE1 "4A6 + 237 = 683. Which digit is A?" uses a letter and a carry cold, warm-up "125 -> 875" bridges a hundred, Q1b-c and Q2b need carries/borrows, Q5 magic triangle uses six tiles and two totals, exit ticket has two unknowns and two carries. Q1a (2?4 + 35? = 579) and Q2a (7?8 - 32? = 453) are carry-free wins. |
| MIDDLE | 4 | 2.5 | 4 | 3 | 4 | 4 | 3.58 | "Was there a carry?" is the right level of struggle; Q4 magic square (80, 50, 60 ...) is satisfying; Q5(b) and Q6 (total 700, difference 200, draw a model) stretch. |
| HIGH | 5 | 4 | 5 | 4 | 4 | 3 | 4.17 | Odd/even investigation ("does odd + odd ALWAYS make even? explain with counters") is the best reasoning task in the level; C5 "find ALL AB7 + 4CD = 1000" is good. Alone for 33 minutes with one tutor visit at ~minute 40. |

Flags: letters A and B in the check, mini-lesson and exit ticket, but yellow boxes in the workbook (two notations for one idea); Q2 header "the answer plus the number you take away must give the number you started with" is a 20-word sentence of abstract reasoning; Q6 requires a bar model that has not been taught (bars come in L5); "=" as "is the same as" (Q3) is a lovely idea but Q3d asks to "explain without adding" to a LOW child who cannot yet add confidently.

### L3 Legs, Wheels and Arrays
| Persona | P | D | F | C | M | S | Mean | Evidence |
|---|---|---|---|---|---|---|---|---|
| LOW | 4 | 2.5 | 4 | 3 | 3 | 3.5 | 3.33 | Counting legs/wheels in 2s and 4s and the farm explore with counters are concrete and fun; Q3 gives the method ("start with all hens, swap one at a time"). But PRE1 (cars and scooters, 16 wheels) is that same method before it is taught, Q1b needs four sentences with a division sign, and page 2 is four word problems (Q4-Q7) in 12 solo minutes. |
| MIDDLE | 5 | 3.5 | 4.5 | 4 | 4 | 4 | 4.17 | "Swap 2 hens for 1 goat and the legs stay 16" is a real insight; talk question "can the leftover ever be 4 or more?" is excellent. |
| HIGH | 5 | 3 | 4 | 4 | 4 | 3 | 3.83 | Tables are known so Q1-Q2 are quick; "Where tables meet" (2 and 5, 3 and 5) is a strong open task; C6 (27 sweets) is a good puzzle. |

Flags: leftovers (Q4 23 stickers among 4, Q5 28 children, vans of 5) are division with remainder, which the lesson notes itself call a P3 topic; Q6 instruction "Stop when the number of rows is bigger than the number in each row" is 15 words of procedure; Q7 "find ALL the ways, start with 1 tricycle" for a child who has just met the table method.

### L4 Pattern Machines
| Persona | P | D | F | C | M | S | Mean | Evidence |
|---|---|---|---|---|---|---|---|---|
| LOW | 4 | 3 | 4 | 3 | 3 | 3.5 | 3.42 | Clap-clap-stomp and the cube train are hands-on; Q1 pattern has a group of 5 so place 20 (a 5-table number) is an easy win; may draw instead of jumping. Q1c (place 41), Q1d (circles in the first 30), Q3 bead string are wordy. |
| MIDDLE | 5 | 4 | 4 | 4 | 4 | 4 | 4.17 | "Groups end at the times-table numbers" is a clear discovery; Q4 petals table (5s) is a win; Q5 tables and chairs. |
| HIGH | 5 | 3 | 4 | 4 | 4 | 3 | 3.83 | "Three counting patterns" (every number in exactly one of 1,4,7 / 2,5,8 / 3,6,9 and why) is excellent; the core pages are easy. |

Flags: first vs last of a group (the lesson's own listed mistake) is easy to confuse for LOW; Q3 reading load.

### L5 Mystery Number Machines (working backwards)
| Persona | P | D | F | C | M | S | Mean | Evidence |
|---|---|---|---|---|---|---|---|---|
| LOW | 3 | 2 | 3 | 3 | 3 | 3 | 2.83 | Guess-my-machine warm-up is fun, Q1a (x2 then +7 = 27) is a win. But PRE1 "divides by 2, then +7, OUT 12" asks for inverse operations cold; IN/OUT/undo/opposite is new vocabulary; Q1c needs 24 / 3 recall; Q2b (find the machine from a table, two unknowns) is guess-and-test; Q3 asks the child to draw before-and-after bars unaided (3 blank lines). |
| MIDDLE | 4 | 3 | 4 | 3.5 | 4 | 4 | 3.75 | "Undo the LAST step first" plus the shoes-and-socks image lands; Q5 "does the order matter?" is a good surprise. |
| HIGH | 5 | 3.5 | 4.5 | 4 | 4.5 | 3.5 | 4.17 | Magic-trick investigation (add 5, double, take away 10, halve) and C5-C7 (three-step, three boxes) are strong; explore "swap the cards: same OUT?" hooks. |

Flags: explore has one partner "secretly" picking and the other undoing, so a LOW child paired with a HIGH child can be the one always being "solved"; the exit ticket (x4, take away 6, OUT 14) needs 20 / 4 and nothing else, fine.

### L6 Market Day (money)
| Persona | P | D | F | C | M | S | Mean | Evidence |
|---|---|---|---|---|---|---|---|---|
| LOW | 4 | 3 | 4.5 | 4 | 3.5 | 3.5 | 3.75 | Shopping with play money is the most concrete lesson in the level; Q1 (pay exactly) and Q3a (change from $1 for 65 cents) are wins; "Mei says use two $20 notes" is a safe spot-the-mistake. PRE2 (3 drinks at $1.60) is repeated decimal addition cold; Q5b (half, then $4, $6 left) is hard. |
| MIDDLE | 5 | 4 | 5 | 4 | 4.5 | 4 | 4.42 | Best match of difficulty, context and discovery ("list in order, one fewer each time"); Q2 every way to pay $8 (7 ways, verified) is a lovely systematic list. |
| HIGH | 5 | 3 | 4.5 | 4 | 4 | 3.5 | 4.00 | "Most coins" investigation (which amount needs the most coins even when you use the fewest?) is good. |

Flags: depends on printed cut-out coins and notes (no fallback); "50 cents vs $50" and "$3.05 vs $3.50" confusions need careful reading; PRE1 repeats the warm-up 85 cents.

### L7 Fair Shares (fractions)
| Persona | P | D | F | C | M | S | Mean | Evidence |
|---|---|---|---|---|---|---|---|---|
| LOW | 4 | 3 | 4 | 3.5 | 3.5 | 3.5 | 3.58 | Thumbs up/down "fair or not", folding strips, Q1 (circle the quarters) are safe wins; Q3c names the classic error ("1/6 is bigger because 6 > 4") on a fictional child. But "fold a strip into 3 equal parts" can end in visible failure; Q6 (quarter vs three eighths) is hard. |
| MIDDLE | 5 | 4 | 4.5 | 4 | 4 | 4 | 4.25 | Equal-parts check, bar comparison and the cake story (Q5) fit well. |
| HIGH | 5 | 3 | 3.5 | 3.5 | 3.5 | 3 | 3.58 | Core is familiar; the fraction-strips investigation (can thirds ever cover a half?) is good but needs strips cut from the kit page, and it is Q8 last. |

Flags: slash notation "1/3" in the text vs stacked fractions the child sees at school; equivalent fractions are deliberately kept as bar-lining only (good).

### L8 Shape Builders
| Persona | P | D | F | C | M | S | Mean | Evidence |
|---|---|---|---|---|---|---|---|---|
| LOW | 4 | 2 | 4 | 3 | 3 | 3 | 3.17 | Name-the-solid with hands and cutting circles are fun; Q1 (count pieces, tick as you go) is a win. Q2 (count every square AND triangle in one figure), Q3 (hidden cubes from a 2D drawing) and Q4 (nets A-F, cut out and fold) are visual-spatial and each is a whole task in 4 questions. PRE1 (5 x 2 layer plus 3 on top) is cold. |
| MIDDLE | 5 | 3 | 4.5 | 3.5 | 4 | 4 | 4.00 | Folding nets is genuinely engaging; layer-by-layer cube counting is taught well ("cubes cannot float"). |
| HIGH | 5 | 3.5 | 4.5 | 4 | 4 | 3.5 | 4.08 | Squares-joined-edge-to-edge investigation (2 shapes of 3, 5 of 4) is excellent; C6 5x5 grid = 55. |

Flags: nets are outside the P1-P3 syllabus (the lesson says so); needs printing and cutting nets, paper circles, scissors and about 12 cubes per child, with no fallback; "same shape when flipped" is a rule a child could argue with.

### L9 Measure Masters
| Persona | P | D | F | C | M | S | Mean | Evidence |
|---|---|---|---|---|---|---|---|---|
| LOW | 3 | 1.5 | 3.5 | 2 | 2.5 | 3 | 2.58 | Four topics (mass, volume, length, time) in 5 questions and 12 sub-parts, the heaviest reading load in the level (329 words). Needs a home-made coat-hanger balance built before the lesson. PRE2 (5 l and 2 l jug, get exactly 1 l) is a cold multi-step puzzle. Q3 pour table; Q5c "10:45 a.m. to 12:10 p.m." crosses noon and the hour (85 minutes). Q1a (apple = two 100 g weights = 200 g) is a win. |
| MIDDLE | 4 | 2.5 | 4 | 3 | 3.5 | 4 | 3.50 | Swap-on-a-balance is a strong idea; jug table is learnable; page 2 solo is too long. |
| HIGH | 5 | 3.5 | 4.5 | 4 | 4 | 3.5 | 4.08 | Weights puzzle (only 2 sets work: 1,2,3 and 1,2,4; why must 1 g be there?) is excellent. |

Flags: "ℓ" and "g" and "kg" and "a.m./p.m." all in one lesson; online pouring needs rice and two containers; the last line of the close ("bring your best thinking") is fine.

### L10 Challenge Day
| Persona | P | D | F | C | M | S | Mean | Evidence |
|---|---|---|---|---|---|---|---|---|
| LOW | 3.5 | 2.5 | 3.5 | 3.5 | 3.5 | 3 | 3.25 | The "how to START: draw, list, table" message is the most confidence-building idea in the program, and a certificate for all. But the relay warm-up names a child and passes the answer round (cold-calling, "wrong answer gets a friendly try again" is still a public wrong answer); station cards are pasted into breakout chat for a slow reader; Q4 is a 4 x 4 logic grid, a new puzzle type. Q1a (read the graph) and Q2 (digit cards 3,0,8) are wins. |
| MIDDLE | 4 | 3.5 | 4.5 | 4 | 4.5 | 4 | 4.08 | Good review; stations and "teach it in two sentences" give real talk. |
| HIGH | 5 | 3 | 4.5 | 4 | 4.5 | 4 | 4.17 | Staircase investigation (1, 2, 3, 5, 8 ways, guess 13) is the best open task in the program; C7 hawker centre. |

Flags: certificate ceremony plus "say one specific thing each child did well" in the final 2 minutes for up to 8 children; "tutor cannot visit four stations" is acknowledged in the plan.

---

## Summary heatmap (mean of six scores)

| Lesson | LOW | MIDDLE | HIGH | Lesson mean |
|---|---|---|---|---|
| L1 Digit Detectives | 3.33 | 4.17 | **3.00** | 3.50 |
| L2 Missing Digit Mysteries | **2.75** | 3.58 | 4.17 | 3.50 |
| L3 Legs, Wheels, Arrays | 3.33 | 4.17 | 3.83 | 3.78 |
| L4 Pattern Machines | 3.42 | 4.17 | 3.83 | 3.81 |
| L5 Mystery Number Machines | **2.83** | 3.75 | 4.17 | 3.58 |
| L6 Market Day | 3.75 | **4.42** | 4.00 | 4.06 |
| L7 Fair Shares | 3.58 | **4.25** | 3.58 | 3.81 |
| L8 Shape Builders | **3.17** | 4.00 | 4.08 | 3.75 |
| L9 Measure Masters | **2.58** | 3.50 | 4.08 | 3.39 |
| L10 Challenge Day | 3.25 | 4.08 | 4.17 | 3.83 |
| Persona mean | 3.20 | 4.01 | 3.89 | 3.70 |

By dimension (all lessons): LOW P 3.65, D 2.45, F 3.75, C 3.10, M 3.05, S 3.20. MIDDLE P 4.60, D 3.40, F 4.30, C 3.70, M 4.05, S 4.00. HIGH P 4.90, D 3.15, F 4.20, C 3.85, M 3.95, S 3.30. The program is fun and nearly everyone can start; the LOW child's problem is difficulty fit (2.45) and its knock-on to confidence and motivation; the HIGH child's weakest scores are difficulty fit and the social/online column (alone and waiting).

### The 5 weakest lesson-persona cells, with fixes

**1. L9 / LOW (2.58).** Too much, too cold, too many prerequisites.
- PRE2 replace "You have a 5 l jug and a 2 l jug and a tap. How can you get exactly 1 l?" with: "You have a 3 l jug and a 5 l jug. You fill the 5 l jug and pour from it into the 3 l jug until the small jug is full. How much water is left in the 5 l jug?" (answer 2 l: a one-pour win that previews the pour table).
- Q5(c) replace "...leaves home at 10:45 a.m. They reach Grandma's flat at 12:10 p.m." with "...leaves home at 10:45 a.m. They reach Grandma's flat at 11:30 a.m. How long is the trip?" (45 minutes). Move the noon-crossing version to Challenge.
- Q3: print the first two rows of the pour table already filled ("Start: 3 l jug 0, 5 l jug 0" and "Fill the 5 l jug: 0, 5").
- Move Q4(c) (the 20 m rope) to Think Harder so page 2 is Q3, Q4(a)(b), Q5 only.
- Prep note: add "No coat-hanger balance at home? The tutor balances a ruler on a pencil on camera and pairs share one view."

**2. L2 / LOW (2.75).** Notation and carries before any teaching.
- PRE1 replace "4A6 + 237 = 683. Which digit is A? How do you know?" with a two-step ladder. Q1 (everyone's win, no carry): "3 [box] 2 + 4 1 6 = 7 8 8. Which digit is hidden in the box?" (7). Q2 (the real check): "4 [box] 6 + 2 3 7 = 6 8 3. Which digit is hidden?" (4). Use a box, not a letter, to match the workbook.
- Exit ticket replace "4A6 + 37B = 801. Find the digits A and B." with "3 [box] 4 + 2 5 7 = 6 0 1. Which digit is hidden?" (4; two carries, one unknown). Keep the two-unknown version as "Bonus".
- Q2 header replace "the answer plus the number you take away must give the number you started with" with "Check: answer + the number you took away = the number you started with."
- Move Q5(b) (side total 420) to Think Harder.

**3. L5 / LOW (2.83).** Inverse operations with no ramp.
- PRE1 replace with a one-step then two-step ladder: "Q1: A machine adds 7. The OUT is 12. What was the IN? Q2: A machine doubles, then adds 7. The OUT is 17. What was the IN? How do you know?" (5 and 5).
- Add a three-line strip to the top of workbook page 1: "IN = what goes in. OUT = what comes out. Undo = do the opposite."
- Q2(b) ("find what the machine does", two unknowns) move to Think Harder; replace with "This machine does x 2, then + 1. Fill in the table for IN 3, 5 and 10."
- Q3: print a half-drawn bar ("Before: [bar]  gave 24  +15  now 50") so LOW fills it in rather than inventing the model.

**4. L1 / HIGH (3.00).** The very first lesson has the zero trap catching the hasty child, and then 45 minutes of easy work.
- In L1 only, drop the check gating: "Finished Q1-Q3 and checked? Start the Mirror numbers (Q8) now."
- Print Q8 at the TOP of the Think Harder page, not last (this helps every lesson).
- Mini-lesson 20-32: invite a child who already knows it to explain "zero can never go first" in two sentences; give the HIGH child a job, not just a seat.
- Warm-up slide: add a Bonus bubble: "Write the biggest and the smallest 3-digit number whose digits add up to 9." (900 and 108.)

**5. L8 / LOW (3.17).** Spatial tasks stacked, no ramp.
- PRE1 replace "A stack has a bottom layer 5 cubes long and 2 cubes deep. On top sits a row of 3 cubes..." with "A stack has 2 layers. Each layer has 2 rows of 3 cubes. How many cubes are in the stack?" (12).
- Q3 stem add: "Build stack A with your cubes first, then count."
- Q4 add: "Fold net A with your tutor on camera first." Core nets A-D; nets E and F go to Think Harder.
- Q2 add a table with a row for each size ("1 by 1 squares", "2 by 2 squares", "3 by 3 squares", "4 by 4 squares") and the instruction "Colour each 2 by 2 square you find a different colour" so counting is visible and checkable.

(Close sixth: L10 / LOW 3.25. Fix: replace the named-child relay with "Pass the card by choosing a friend who has not had a turn; you may say 'pass'", and print the station card text on the slide, not only in chat.)

### The 3 strongest cells
1. **L6 / MIDDLE (4.42).** Concrete context, a real systematic-list discovery, wins from the first minute, and the "no $20 note" talk question is a safe mistake to find.
2. **L7 / MIDDLE (4.25).** Equal-parts check and bar comparison are exactly pitched, with named misconceptions handled kindly.
3. **L10 / HIGH (4.17)** (tied with L5 / HIGH and L1-L4 / MIDDLE). Staircase investigation and the "how to START" framing give the fast child a real puzzle and a reason. Best LOW cell: L6 (3.75).

---

## Checks requested on the new items

**Warm-up check.** Not safe as written for LOW. The script says "This is not a test", but the same page says a child who gets both right AND can say why changes pages. Children work out the rule by lesson 2. Whiteboards go up together, so a blank board is visible to everyone; one child is then asked "how do you know?" The questions are deliberately unfamiliar, so in about 8 lessons LOW is likely to freeze on one or both. Fixes: (1) two-step ladder, Q1 within reach of everyone, Q2 the real check (examples above); (2) whiteboards face down until "3-2-1", wrong boards never read aloud; (3) the "how do you know?" child is chosen from boards the tutor has already seen were right; (4) the tutor line "Some of you will start on a different page today" is fine, but the printed box must go.

**Fast track.** It labels, in four ways: the printed "FAST TRACK" box on every child's page 1; the breakout room (a child disappears at minute 36, in a group of up to 8 everyone sees who); the unspoken criterion ("both right AND can say why") that children can decode; and the banner "Challenge (for strong thinkers)" over the Q5-Q7/Q8 page. It also strands the child: no pair partner in a "pairs first, talk before you write" lesson, one tutor visit at minute 40 for a 33-minute stretch, and no answer key on the child's side to self-check. And it excludes the hasty-but-able child (L1 HIGH) and admits the child who talks well but is mid-level. Fix: replace the gate with a choice. Print on every page 1: "When you finish Q3, you can choose: Think Harder or Open investigation (Q8)." Tutor invites by private chat. Keep fast-track breakout pairs of two (never one child alone). Rename the banner "Challenge (for brave thinkers)". Keep "Stretch".

**Open investigation.** The tasks themselves are the strongest part of the new work (mirror numbers, odd/even, where tables meet, three counting patterns, the magic trick, most coins, fraction strips, squares joined edge to edge, weights, staircase). All have a low floor and a named ceiling, and the model answers say what to look for. Problems: placed last (Q8); each is 5 lines on one page with 3-4 sub-questions (a)-(d) - too much to read aloud for a 7-year-old; L7 and L8 need cut-out strips/tiles at the moment of use. Fix: Q8 first, trim to (a)(b)(c), print "tiles/strips needed" next to the title.

**Reflection.** Mostly safe but not for LOW as built. Positive: no marks, "tricky" (not "hard"/"bad"), faces, tutor says "praise the strategy, not the speed", never grade. Problems: (1) it is on the Challenge page, under "for strong thinkers", so LOW opens a page of undone work to find it; (2) "I got unstuck by:" assumes the child got unstuck; a child who stayed stuck has no honest option, and "asked my partner" is one of the four choices in all ten lessons, while a fast-track child alone has no partner; (3) 60 seconds for three written sentences is impossible for a slow writer and the last 2 minutes also carry exit-ticket collection, stamping, the close and (L10) a certificate speech; (4) "ask one or two children to share ONE sentence" can single out a low-confidence child. Fix: move it to the exit-ticket slip or journal page; make it "tick a face; circle ONE: [drew it] [made a list] [used objects] [asked] [I am still stuck]; optional sentence"; sharing by volunteers or by private chat only; give it the full 88-90 slot by trimming the exit ticket to 7 minutes.

---

## Level-wide patterns

- **Pacing.** Page 2 is solo for 12 minutes (57-69) and holds the hardest items for LOW in L2, L3, L5, L8, L9. Page 1 packs up to 18 sub-parts into the 14 pair minutes (L1: 18, L4: 15, L9: 12). Talk time is 8 minutes for up to 8 children. The last 2 minutes carry reflection, stamps, close and, on L10, certificates: the reflection will be the first thing dropped.
- **Reading load.** Core workbook text per lesson, words: L1 347, L2 319, L3 315, L4 299, L5 291, L6 284, L7 249, L8 206, L9 329, L10 275 (average 291), before the Think Harder pages. At 60-80 words a minute for a slower reader that is 4-5 minutes of decoding per lesson, and the pair routine says "read each question aloud", which exposes the slow reader. Suggest the tutor reads each question aloud on the screen instead.
- **Wait time for HIGH.** About 40 of 90 minutes are whole-group listening: explore debrief 6, mini-lesson 12, teach-before 5, check-togethers 5, talk time 8, quick warm-up questions about 4. Fast track does not touch these. The HIGH child gets real work only for 33 worksheet minutes (if fast-tracked) and the explore. Fix: give HIGH a job in the mini-lesson (explain the second worked example) and in check-together (write a harder variant).
- **Guaranteed win for LOW in the first 10 worksheet minutes.** Yes in 10 of 10 lessons, which is a real strength: L1 Q1a, L2 Q1a and Q2a, L3 Q1/Q2, L4 Q1 (place 20), L5 Q1a, L6 Q1 and Q3a, L7 Q1, L8 Q1, L9 Q1a, L10 Q1a. The failure is minutes 1-4 (the check) and then the middle and end of the pages.
- **Prior skills assumed.** L3 (tables and the division sign), L6 (decimal money), L7 (fractions), L9 (time to 5 minutes, a.m./p.m.) assume school-taught topics; a LOW child not yet fluent cannot reach the thinking. L3 also uses remainders its own notes call P3; L5, L8 (nets), L9 (durations across noon) are enrichment beyond a typical P2 child.
- **Materials.** L1 digit cards, L6 play money, L7 strips, L8 circles/nets/cubes, L9 balance, jugs and a clock all need printing, cutting or building at home. Only L6 mentions real money as a fallback. Participation barrier falls hardest on the least supported child.
- **Social/online.** "Hold your page up to the camera", "whiteboards up together", relay cold-calling (L10), named children in the relay, breakout rooms the tutor cannot visit. Named-child misconceptions in the scripts ("Ali says 399 is bigger", "Mei says 1/6 is bigger") are a safe, good device.
- **Strategy-based feedback.** Strong: "praise the thinking not the answer", "ask how do you know after right AND wrong answers", "friendly try again, never a groan". Risk: "how do you know?" after every wrong answer can feel like interrogation to a LOW child; add "or say 'I'm not sure yet'".

---

## PART 2: Diagnostic check (P2, 4 warm-up + 6 main + 2 stretch, 30 minutes)

### (a) Question demand and fairness

| # | Question | True skill demand | School year / fair for 7-9? |
|---|---|---|---|
| W1 | 10 more than 64 | Place value to 100, tens digit +1 | P1 skill. Fair, very easy for the band. |
| W2 | Smaller, 58 or 85 | Compare 2-digit numbers | P1. Fair; a 50% guess, so weak information. |
| W3 | 16 - 9 | Subtract within 20 with bridging | P1. Fair; a fact for most 8-year-olds. |
| W4 | 45 + 30 | Add tens to a 2-digit number | P1/early P2. Fair, easy. |
| M1 | Value of 6 in 462 | Digit value in 3 digits | P2. Fair but the easiest main item; skill is also in W1 and S2. |
| M2 | 5_ + 27 = 81 | Missing digit, regroup | P2 skill plus unfamiliar "5_" notation (an underscore after a digit can read as a minus or a blank line). Fair; typeset a box. |
| M3 | 4 rows of 5 stars | Arrays, 5s table or repeat add | P2 (tables 2,3,4,5,10). Fair; low floor. |
| M4 | Double then add 3, input 5 | Two-step machine, order | Enrichment, not syllabus; forward only. Fair; tests reading order. |
| M5 | $1.20 + $0.85 | Decimal money, cents regroup | P2 skill but the hardest main item (105 cents). Fair, with 60% success for a typical child. |
| M6 | 4 equal parts, 3 eaten | Fraction as parts of a whole | P2 (quarters). Fair, easy. |
| S1 | double, +3, = 17 | Reverse two-step | P3/enrichment; guess-and-check is allowed. Fair stretch. |
| S2 | tens 2 more than ones, sum 10 | Two-clue riddle | Enrichment; list pairs. Fair stretch; same skill as L1 Q6. |

Coverage against the 10 lessons: place value (L1) yes; add/subtract (L2) via M2; arrays (L3) M3; machines (L5) M4, S1; money (L6) M5; fractions (L7) M6. Not sampled at all: repeating/growing patterns (L4), shapes and cubes (L8), measure and time (L9), picture graphs and logic (L10) - 4 of 10 lessons, and L8/L9 are where LOW scores lowest. No item asks the child to explain, list "all", or persist, which is what the lessons demand most. The diagnostic measures school-taught P2 competence; the lessons demand enrichment-style reasoning on top of it.

### (b) Six profiles
Per-question success rates are my assumptions (listed in the script). Result = chance of each outcome using the page's rule (6-8 join, 8/8 with 4/4 warm-up may try up; 4-5 join with support, or one level down if warm-up is 2 or less; 0-3 one level down).

| Profile | Expected warm-up / total of 8 | Placement distribution | Right level against the lessons? |
|---|---|---|---|
| Strong for age (8y) | 3.9 / 6.7 | Join 71%, try up 18%, join with support 11% | P2 fits (HIGH persona mean 3.89). The "try up" trigger (8/8 and 4/4) fires only about 18-20%, so most strong children stay at P2: acceptable, but that child is bored in core pages. |
| Typical for age (8y) | 3.8 / 4.9 | Join with support 58%, join 29%, DOWN 11% | P2 is right (MIDDLE mean 4.01). The 11% sent down to "Ages 6-8" are mis-placed, and the 58% told to "expect some support" are told something that undersells them. |
| Weak for age (8y) | 2.8 / 1.9 | Down 92% | Right; LOW persona is marginal at P2 (3.20). |
| Younger, strong (6y9m, P1 finished) | 3.9 / 4.5 | Support 55%, join 22%, down 22% | Down or support is right: L3, L6, L7, L9 assume school-taught tables, decimal money, fractions and time. The 22% who "join" will find L3-L7 hard. |
| Older, weak (9y) | 3.3 / 3.1 | Down 62%, join with support 31%, join 2% | The 31% "join with support" are the children the lessons hurt most (L2, L5, L9 at 2.6-2.8 for LOW). And the 62% "down" get the label "Ages 6-8" for a 9-year-old (see (d)). |
| Guesser/rusher | 2.8 / 2.0 | Down 91% | Right for pure guessing (chance of 4+ by guessing is under 1%), wrong for a capable child who rushes: a careless typical child gets "down". |

### (c) Cut scores and noise
Standard deviation of an 8-item score is about 1.3-1.4 marks; each band is only 1-2 marks wide.

| True per-question success | P(6-8: join) | P(4-5: support) | P(0-3: down) |
|---|---|---|---|
| 0.40 | 5% | 36% | 59% |
| 0.50 | 14% | 49% | 36% |
| 0.60 | 32% | 51% | 17% |
| 0.70 | 55% | 39% | 6% |
| 0.75 | 68% | 29% | 3% |
| 0.80 | 80% | 19% | 1% |
| 0.90 | 96% | 4% | 0% |

So a child who truly gets 75% of this kind of question lands in "support" a third of the time (unlucky); a child at 50% reaches "join" 14% of the time (lucky). The "down" error for a competent child is the worst error (p = 0.7: 6%; typical simulated profile 11%); the "join" error for a weak child (p = 0.5: 14%) is the one the lessons punish. Because 6 of the 8 points are main items, "6-8" in effect means "nearly perfect on the 6 main items or a stretch point", so the join band is narrow and the support band is where most typical children sit. Moving the cut to 5 makes it worse for the children who need help (older weak: only 12% would be told "join" under cut 5 vs 2% now, and younger strong: join rises to 50%); I tested it and do not recommend it. Keep 6 and 4; fix what "support" means and add a tie-break (see (e)).

Warm-up level check: all four warm-up questions are genuinely Primary 1 content (numbers to 100, addition and subtraction to 100/within 20), so they ARE from the level below. But they are very easy and only sample number sense: P(warm-up 2 or less) is about 1-5% for a competent child, so the "warm-up 2 or less goes down" rule almost never fires except for weak children. The P1 program also teaches bonds, patterns, graphs, coins, shapes, logic and length, and none is sampled. The level-up trigger depends on 4/4, which nearly everyone gets, so it adds little.

Consistency with `docs/levels_and_placement.md`: 6-8 of 8 (75%+) matches "70% or more"; 4-5 (50-62.5%) matches 40-69%; 0-3 (under 40%) matches; 8/8 vs "90%+" is slightly stricter and fine. The SPEC says P2 is for children "finishing Primary 2, age 8" while the pages say "Ages 7-9" and "open to a year either side"; a 7-year-old who has only finished P1 sits inside the band label and relies on the diagnostic to be steered down.

### (d) Wording that could discourage a child or parent
- Parent page heading "Not yet?" followed by "That is useful to know, not a failure." Putting the word "failure" in the sentence invites it. "A confident start matters more than a fast one" implies the child is slow.
- Down recommendation names "Ages 6-8 (P1)". For a 9-year-old the label is below their age, in a class of 6-year-olds. The levels doc says Ages 6-8 weak learners start with the free taster and a tutor chat; the 0-3 row on the page does not say that.
- 4-5 row: "expect some support" is not backed by any described support; a parent reads it as "your child will struggle".
- Page 2 of the child sheet gives no warning that the last two "Brain stretchers" are meant to be hard; a child who cannot do them may feel they failed. Only the parent-page card on page 1 says "try your best, or skip".
- Tutor key (page 3) is in the same PDF as the child's pages 1-2. If a parent prints the whole file, the child sees every answer and "Common error: 65", "Common error: guessing 5 or 6" and "Note if counting by ones" - the last invites judging the child's method. Also the "Watch for" column can read as a list of what the child got wrong.
- "Open to a year either side" on the child intro is fine.
- Good: "Try your best, or skip it", "You make the final choice", "free to change before lesson 1", "Prices are the same at every level".

### (e) Recommended changes (exact text)
1. Child sheet, page 2, directly under the heading "Brain stretchers", add: "These two are tricky on purpose. Have a go, and it is fine to skip them."
2. M2: change `5_ + 27 = 81. What digit goes in the blank?` to `5 [box] + 27 = 81. Which digit goes in the box?` (typeset as an empty square, answer 4).
3. Replace M1 (`What is the value of the digit 6 in 462?`, duplicated by W1 and S2) with a pattern item for L4 coverage: `A pattern goes triangle, circle, circle, square, triangle, circle, circle, square ... What is the 10th shape?` (answer: circle; skill: repeating patterns). Option if two items can be added: `A lesson starts at 4:50 p.m. and lasts 25 minutes. What time does it end?` (5:15 p.m.).
4. W2: change `Which is smaller, 58 or 85?` to `Put these in order, smallest first: 58, 85, 49.` (49, 58, 85; removes the 50% guess).
5. Parent page, 4-5 row, replace the text with: "Join **Ages 7-9 (P2)**. Most children here find some of the puzzles tricky; that is what the class is for. Your tutor will check in with you after Lesson 1. If the warm-up score is 2 or less, **Ages 6-8 (P1)** may be a more comfortable start - talk to us first."
6. Parent page, 0-3 row, replace with: "We suggest a chat with your tutor and a free taster before choosing. **Ages 6-8 (P1)** builds the same thinking habits with smaller numbers. If your child is 9 or older, ask us: you do not have to choose a level by age."
7. Parent page, "Not yet?" box: retitle "Want a gentler start?" and replace the text with: "Starting one level down means more wins early on and more joy in class."
8. Tutor key page: add a header `Print pages 1 and 2 for your child. Keep pages 3 and 4 for yourself.` and ship the key and result page as a separate PDF.
9. Tutor key, add a tie-break: "Borderline (5 or 6 marks): ask your child to explain questions 2, 4 and 5 aloud. If they can say why, use the higher band. If a child finishes in under 12 minutes, ask them to check two answers before you mark."
10. Tutor key, add a prerequisites line: "Questions 3, 5 and 6 are topics taught in school (arrays, money, fractions). Missing two or more means those lessons will need extra care (Lessons 3, 6 and 7), even if the total is 6 or more."
11. Keep the cut scores (6 and 4) and the 8/8-with-4/4 level-up rule.

---

## 10-line summary
1. Verdict LOW (mean 3.20): can start every lesson and always has a minute-one win, but difficulty fit is 2.45; L9 (2.58), L2 (2.75), L5 (2.83), L8 (3.17) hurt, and the untaught Warm-up check is a cold start in about 8 lessons.
2. Verdict MIDDLE (mean 4.01): well served; L6 and L7 are the best lessons; page 2 solo is too long in L2 and L9.
3. Verdict HIGH (mean 3.89): the Open investigations are excellent, but about 40 of 90 minutes are whole-group listening, the investigation is last on the page, and the fast-track child works alone.
4. Fix 1: remove the printed "FAST TRACK" box and the check-based gate; offer choice after Q3, put Q8 first, rename "Challenge (for strong thinkers)" to "(for brave thinkers)".
5. Fix 2: make the Warm-up check a two-step ladder with a win in Q1, whiteboards face down, and no pre-teaching of the key technique (L2, L3, L5, L8, L9).
6. Fix 3: cap page 2 for LOW (L2, L5, L8, L9): scaffolded first rows, simpler Q5c, nets/cubes with objects, move extra parts to Think Harder.
7. Fix 4: move the reflection to the exit slip, tick plus choose-one plus optional sentence, volunteers only, and give it a real 2 minutes.
8. Fix 5: diagnostic wording and coverage: "tricky on purpose" line, remove "failure"/"Not yet?", handle the 9-year-old "Ages 6-8" label, separate the answer key, and swap M1 for a pattern or time item.
9. Does the diagnostic place children correctly? **Mostly.** Weak and guessing children go down (92% and 91%) and strong ones join, but about 11% of typical children are sent down, the 4-5 band carries a vague promise of "support" that the lessons do not deliver, and four of ten lessons (patterns, shapes, measure, graphs/logic) are not sampled.
10. Cut scores are not the problem (moving them made weak children worse placed); the item set and the words around the result are.
