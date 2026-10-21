# Audit: Math Inquirers P6 (Maths + coding bridge), suitability and difficulty

Date: 2026-10-22. Scope: `p6/content/l1.js` to `l10.js`, `p6/data.js`, `p6/SPEC.md`, slides in `split/p6l1` to `split/p6l10`, and the generators in `rebuild/gen_p6l*.py`. Read-only audit; no content files were edited.

## How this audit was done

- Every lesson's `lesson`, `script`, `deck`, `qbank` and workbook text was dumped with a Node script (workbook helpers stubbed) and read in full. Every slide's visible text and speaker notes were read for the code slides, the explore slides, the title notes (time plans) and the worked examples.
- Every numerical answer in the keys and the qbanks (about 400 items) was rechecked by hand and in Python: Goldbach pairs and counts, 3-factor numbers, magic-square count, probability tables, Caesar shifts, star and tiling angles, mean problems, grid routes, digit counts and so on. **I found no wrong maths answer in any key, qbank item, slide answer or exit ticket.** The weaknesses are about Scratch, timing, scaffolding and level, not arithmetic.
- All 20 Python snippets in the slide notes and the workbook "Python corner" boxes were run with python3 (the turtle one with a stub). All run and give the stated output (see section 4).
- The Scratch drawings in code slides and the workbook were checked against the Scratch 3 editor as I know it.
- **Limitation (please read):** I tried to confirm the Scratch 3 block labels and colours against the Scratch Wiki, but `WebFetch` was denied and `WebSearch` returned link lists with no page text. Anything in "Scratch accuracy" below is therefore from my own knowledge of the Scratch 3.0 interface, not from a fetched page. I am confident about items 1, 3, 4, 5 and 6 below. Do a 10-minute check in the real editor of the items in the "verify in the editor" checklist at the end of section 3.
- Same limitation for the MOE syllabus: the search returned only links. The syllabus comments in section 2 come from my knowledge of the 2020/2021 secondary syllabus (SEAB 4052 / MOE G3). Treat the exact level labels as "believed, please verify"; they affect positioning, not correctness.

## 1. Summary table

| Lesson | Verdict | One-line reason |
|---|---|---|
| 1 Code the Pattern | minor fix | Maths excellent; Q5 uses plain `say` in a loop so the child never sees the 20 terms; worksheet pages too long for the time slots. |
| 2 Prime Hunters | minor fix | All maths correct; Q6 has the same `say`-in-a-loop problem; worksheet 2 has about 35 answers for a 6-minute slot; lots of new coding (if + mod + counter + if/else) in lesson 2. |
| 3 Below Zero | OK | Right level and best-paced lesson; only nits (U+2212 minus typed into Scratch, challenge 9 changes the floor-numbering convention). |
| 4 Algebra Machines | minor fix | Good lesson; tutor note says Sensing is "purple" (it is light blue); Q1(c) steps IN by 2 which contradicts the "per 1" hint; worksheet 2 tight. |
| 5 Every Possible Way | minor fix | Uses a hat block that does not exist ("when start clicked"); starter project "Every Order" says 1, 2, 3 not milk/green/taro; worksheet 2 about 25 answers in 7 minutes. |
| 6 Fair or Unfair? | minor fix | Same non-existent "when start clicked" hat; Q4 36-cell table plus Q5 in 8 minutes; probability is beyond Sec 1 so it is enrichment (fine, but say so). |
| 7 Turtle Geometry | needs rework (scoped) | Several programs as written draw off the 480 x 360 stage; "turn right" is not a Scratch 3 label; worksheet 2 is overloaded; two Think Harder items are abstract or ambiguous. |
| 8 Secret Codes | needs rework (coding part) | Maths is good, but the Scratch cipher machine is not specified (only 3 of about 8 blocks shown), spaces in the message are coded to wrong letters, and the "starter project" does not exist in the repo. |
| 9 Data Detectives | minor fix | Mean, total and missing-value work is PSLE content, so the maths is too familiar; the list/loop coding is the real new part. Footer says "P6 Holiday Program" (L1 to L8 do not). |
| 10 Showcase Challenge | needs rework (timing and scaffolding) | Plan, build, test and present own program is planned in about 13 minutes; 8 showcases in 24 minutes with no switch time; three starter projects are not provided. |

Overall: the programme is well pitched for 12 to 13 year olds who have just finished the PSLE, the maths is accurate, and the "predict, test in code, explain" routine is coherent. The main risks are (1) coding scaffolding that assumes more Scratch than a typical P6 child has, (2) worksheet pages that cannot be finished in the minutes allotted, (3) a handful of Scratch labelling errors, and (4) the tutor-side Scratch assets (starter projects) that exist only as descriptions.

## 2. Suitability and difficulty, lesson by lesson

Syllabus note: Sec 1 content in the current MOE syllabus includes negative numbers, primes/factors/HCF/LCM, algebraic expressions and linear equations, and angle properties of polygons including exterior angles. Mean, median and mode appear in the lower-secondary statistics strand. Probability of single events is, as far as I know, taught later (around Sec 3, Elementary Maths), so L6 is genuine enrichment rather than a Sec 1 preview. Sequences and the nth term, counting (combinatorics) and modular arithmetic are not Sec 1 content at all, so L1, L5 and L8 are enrichment too. That is fine for a "post-PSLE bridge", but the parent-facing wording should not claim they are Sec 1 topics (the SPEC table's column "Maths (Sec 1 bridge)" and the L10 `talkAns` "all of these appear in Secondary 1" overstate this).

Typical P6 coding exposure in Singapore: most children have met Scratch-style block coding through school enrichment (for example MOE Code for Fun), typically sequence, repeat/forever, simple if, events and sometimes a variable. Lists, `mod`, nested loops, `ask`/`answer`, `repeat until`, operator blocks nested inside operator blocks, the Pen extension and tracing a loop in a table are usually new. Some children will have had no Scratch at all. The programme assumes "met block coding in school" but then, in lesson 2, uses if + mod + a counter + if/else together. See issue 15 for a recommended pre-lesson primer.

### Lesson 1: Code the Pattern (minor fix)
- (a) Suitability: good. Sequences are familiar from primary, the nth-term step is new but concrete (compare with the times table). Not babyish. Challenge items (square-number tiles, 2, 6, 18, 54, Fibonacci leapfrog, triangular-number code) are good stretches.
- (b) Difficulty: Core (6) are easy; Think Harder items 1 to 4 are mid; Challenge is hard but fair. Q2 has four sequences x 3 answers and Q1 has 4 sub-parts plus a table, which is a lot for 10 minutes.
- (c) Coding: block names are right (`set term to`, `repeat`, `change term by`, `say`, `when green flag clicked`). The "99 jumps, not 100" fence-post point is excellent and well taught. Problem: workbook Q5 gives a plain `say (n)` block and asks the sprite to "say the first 20 terms". In Scratch a plain `say` inside a loop is overwritten every frame, so the child only ever sees the last term. The slide `teachplan` correctly uses `say n for 1 seconds`; the workbook does not. See issue 2.
- (d) Answers: all correct.
- (e) Timing: ws1 44 to 54 (10 min) for about 24 answers; ws2 59 to 67 (8 min) for a trace, a program plan and a bug. Tight. Stretch and challenge slides have no time slot.
- (f) Online: matchsticks work with drawn lines; sending "four starter blocks" in chat is not possible (blocks are not text), see issue 7.

### Lesson 2: Prime Hunters (minor fix)
- (a) Suitability: good. Primes and prime factorisation are genuinely Sec 1. Sieve by hand is a nice anchor. Goldbach, twin primes, "exactly 3 factors" are good enrichment. Not babyish.
- (b) Difficulty: Core easy; Think Harder 1 to 4 includes "100 as a sum of two primes in every way" (needs testing about 25 primes; about 5 minutes, fine); Challenge includes the 20-lockers problem and the 301 eggs problem, both hard but labelled challenge.
- (c) Coding: `if <(6) mod (d) = 0> then`, `change count by`, `if ... else` are all valid Scratch 3. The prime checker in the `we3` slide is 9 blocks, within the 15-block rule. Problem: workbook Q6 block A is plain `say (d)` inside a loop with `if`; the child would see only "40" at the end although the key says it "says" 8 numbers (issue 2). The `teachplan` slide has the same flaw ("It says 1, 2, 4, 5, 10, 20" is not what Scratch displays).
- (d) Answers: all correct (rechecked: 25 primes, twin pairs, factor counts, 48 has 5 Goldbach pairs, 121 and 169, 301, lockers).
- (e) Timing: ws2 is 61 to 67 (6 min) for Q3 (6-row trace), Q4 (3 parts), Q5 (3 parts) and Q6 (order blocks): about 35 answers. Not feasible; it needs about 12 minutes.
- (f) Python corner uses a list comprehension (`[d for d in range(1, n + 1) if n % d == 0]`), which is above the "10 to 20 lines, simple" level of the other snippets; fine for optional.

### Lesson 3: Below Zero (OK)
- (a) Suitability: right level. Negative numbers are the headline Sec 1 topic; thermometers, lifts and sea level are well chosen. The "a - b is the jump from b to a" idea is a strong bridge.
- (b) Difficulty: Core easy, Q4 mid (includes `5 - (-3)` and `-1 - (-7)`), challenge 1 (magic square with -4 to 4) is hard but I verified it has exactly 8 solutions (the key's claim is right).
- (c) Coding: `set x to`, `change x by` and `x position` are valid Motion blocks; the stage really is -240 to 240. `repeat`, `say for secs` correct. Teaching note "there is no decrease block" is right. A child can follow this with school-level Scratch. Nit: the minus sign in the slides and workbook is the Unicode minus U+2212; a child typing it from the keyboard will use a hyphen, which is fine, but a child who copies "-3" from a slide or chat into a Scratch number field may get 0 (issue 9).
- (d) Answers: all correct. Challenge 9 (Singapore level 1 = ground, B1 below) conflicts with the lesson's own convention (workbook Q6 says 0 = ground floor, warm-up uses B1 = -1) and "why is 4 - (-3) = 7 not the answer" never defines what B3 maps to. Ambiguous (issue 14).
- (e) Timing: ws2 57 to 67 (10 min) for about 20 answers; tight but workable.
- (f) Online: fine.

### Lesson 4: Algebra Machines (minor fix)
- (a) Suitability: good. Function machines are the right bridge to "n" algebra; PSLE children have used letters for unknowns. Running the machine backwards is exactly the Sec 1 equation method.
- (b) Difficulty: Core easy; Think Harder 3 introduces `(n + 5) x 2 = 2n + 10` (bracket expansion, a Sec 1 skill, appropriately sign-posted); challenge includes equations with n on both sides (5n - 3 = 2n + 15) and the age problem; hard but fine.
- (c) Coding: `ask IN? and wait`, `answer`, `*`, `+`, `repeat until`, `set out to` are all correct Scratch 3. Slide notes say "ask is in Sensing (purple)": Sensing is light blue; purple is Looks (issue 6). `repeat until (n * 8) - 5 = 91` is correct; the note about an infinite loop when there is no whole-number answer is a nice touch.
- (d) Answers: all correct. Workbook Q1(c) has IN 2, 4, 6, 8 (step 2) while the teaching hint is "how much does OUT go up when IN goes up by 1?"; a child following the hint literally gets 8. Intended as a step-up but unsignposted (issue 12).
- (e) Timing: ws2 57 to 67 (10 min) for Q4 to Q7 (about 20 answers); tight.
- (f) Fine online; breakout rooms with screen-sharing for the "secret rule" game are a good fit.

### Lesson 5: Every Possible Way (minor fix)
- (a) Suitability: good, concrete, not babyish (bubble tea, handshakes, grid routes, digit cards).
- (b) Difficulty: Core easy; stretch includes hexagon diagonals, league matches, rectangles in a strip; challenge includes 70 routes on a 4 x 4 grid, dominoes (28), 15 three-digit numbers with digit sum 5; all hard-but-fair.
- (c) Coding: nested loops, `join`, `say for secs` are correct and the nested-loop idea is well taught (trace first, then build). Errors: the hat block is drawn as **"when start clicked"** (workbook Q3 and Q6, slides `explore1`, `teachcode`, `teachhandcode`): there is no such block in Scratch 3 (it is "when green flag clicked"). The "Every Order" starter project does not exist in the repo and, as described (`set tea to 1, repeat 3: say tea ...`), says 1, 2, 3, not milk/green/taro; the explore asks for "every order" but never says how to turn numbers into names. Slide note for `teachcode` says that if `set shorts to 1` were outside the outer loop "shirt 2 would start at shorts 3 and say nothing new"; it would actually say "23, 24" (not real outfits). Fix wording (issue 17).
- (d) Answers: all correct (grid P at (1,1): 8 routes avoid P, 12 pass through P; 3 x 3 magic counts; 252 digits).
- (e) Timing: ws2 is 61 to 68 (7 min) for Q4 (3 parts), Q5 (16-circle grid + 2 answers) and Q6 (3 gaps + 2 answers); not feasible.
- (f) Fine online.

### Lesson 6: Fair or Unfair? (minor fix)
- (a) Suitability: good and engaging (Dice Race is a great hook). Probability is above Sec 1, so label as enrichment. The "close, not exact" message is exactly right.
- (b) Difficulty: Core easy; Think Harder includes "at least one 6" (11/36) and the fair-points question; challenge includes unreplaced draws and the 3 x 4 spinner game. All checked.
- (c) Coding: `pick random 1 to 2`, `if ... then`, `repeat 1000`, `and`, `else` all correct. The slides use `say A for 2 seconds` then `say B`: good. Error: hat drawn as "when start clicked" in Q2, Q5 and the `teachcode` and `teachplan` slides (issue 1). Good teaching note: two separate `pick random` blocks, not `pick random 2 to 12`.
- (d) Answers: all correct (176/1024, 12 vs 24 of 36, difference table 6/10/8/6/4/2, "19 runs in 20" ranges 345 to 405 and 145 to 190 hold: 2 standard deviations give 344 to 406 and 143 to 190; exactly 500 heads in 1000 flips is 2.5%, i.e. about 1 in 40).
- (e) Timing: ws2 59 to 67 (8 min): Q4 has a 6 x 6 table (21 empty cells), four sub-questions and a Python box; Q5 plan. Too much for 8 minutes.
- (f) Children need two dice at home; fallback is a shared dice program, which is not in the repo.

### Lesson 7: Turtle Geometry (needs rework, scoped)
- (a) Suitability: the best "maths and code" pairing in the course and genuinely Sec 1 (exterior and interior angles of polygons, angle sum). Stars are great enrichment. Warm-up "Turtle says" with body turns and brain-break "Turtle dance" are a little young for cameras-on 12 to 13 year olds, but short.
- (b) Difficulty: Core easy; Think Harder items are good except the last three challenge items, which are what prints on the Think Harder page: (i) three polygons around a point (open-ended, needs a table of interior angles up to 42-gons), (ii) 1800 degrees (fine), (iii) "why can a turtle not draw a 6-point star in one go" which is abstract and its answer relies on the unstated idea of "visits 6 points" (issue 13).
- (c) Coding: `pen down`, `move 100 steps`, Pen extension are right and the note "add erase all and go to x:0 y:0" is good. Problems: (1) Scratch 3's turn blocks are labelled `turn ↻ (15) degrees` and `turn ↺ (15) degrees` with arrow icons, not "turn right/left"; the slides draw "turn right 90 degrees" (issue 5). (2) Stage size: the stage is 480 x 360 and the sprite starts at (0,0) heading 90. I simulated each program (issue 4): octagon with move 80 reaches y = -193 and a 10-gon with move 80 reaches y = -246 (both below the bottom edge at -180); the 20-point star in Q4 (no move size given) reaches y = -310 at move 150; the 9-point star at move 150 reaches y = -199. Sprites are fenced at the stage edge, so lines kink and the drawing is wrong, which will look like a maths error to a child. (3) `point in direction 90` is not mentioned; non-closing wrong programs (turn 60 triangle) leave the sprite facing a different way, so re-runs start rotated.
- (d) Answers: all correct (checked every star, tiling and turn).
- (e) Timing: ws1 40 to 50 (10 min) includes a 5-row table, two Scratch tests, Ben's nonagon and its fix; ws2 55 to 66 (11 min) has a 9-row trace, two star plans (6 cells), a 10-cell table and a rule. About 45 answers. Not feasible (issue 10).
- (f) Python turtle needs a window (`turtle.done()`), so it will not run in a plain console or some browser editors; and it prints `144.0 720.0` (floats), which is mentioned in the notes but not in the workbook.

### Lesson 8: Secret Codes (needs rework, coding part)
- (a) Suitability: good. Clock arithmetic and Caesar ciphers are exactly the kind of enrichment 12 to 13 year olds enjoy; mod is a Sec 3+ idea but is introduced as "remainder" which P6 children know. Not babyish. Warm-up "9 o'clock + 4 hours" is very easy but short.
- (b) Difficulty: Core easy; Think Harder includes decoding BYFFI (shift 20) and mod properties; challenge includes multiplicative ciphers (non-invertible `x2`), a crack with a hint, and clock-jump orbits; all fine.
- (c) Coding: the three displayed blocks are valid (`item # of (letter) in [alphabet]`, `mod`, `join`, `item (m + 1) of [alphabet]`). But (1) a child cannot build the machine from the 3 blocks shown: the loop that walks through the message (`set i`, `repeat length of answer`, `letter i of answer`, `set letter`, `change i`) and `set code to ""` are never shown; the notes say only "for each letter is a repeat loop" (issue 3). (2) The `alphabet` list must be created and filled with 26 letters (the notes mention list import, which is fiddly for children). (3) A space is not in the list, so `item # of` returns 0, `n = -1`, and a space is "coded" as the letter at index `shift - 1` (for shift 10 it decodes to P; for shift 3 it codes to C). Workbook Q2(b) `MYNO SC PEX` and the explore message `PDWK LV IXQ` contain spaces, and Q2 says "Test your answers in Scratch", so the Scratch machine will output a wrong letter at each space unless the extension is done first. (4) The slide note says list blocks are "dark-blue"; Scratch 3 list blocks are red-orange (issue 6). (5) Scratch `mod` with a negative number returns a non-negative result like maths mod, so `(-4) mod 26 = 22`, which is correct and worth telling tutors (it makes "add 26" unnecessary in code).
- (d) Answers: all correct (rechecked every cipher, `X ADKT BPIWH` is I LOVE MATHS with shift 15, 1000 days after Monday is Sunday, etc.). Python runs and gives `PHHW DW WKH PUW`; with `shift = -3` it decodes correctly.
- (e) Timing: ws sizes are fine; the problem is the coding scaffold, not minutes.
- (f) Online safeguarding: the warm-up says "coded names are sent privately in the chat to a partner". Private chat between minors is switched off in many tutoring policies; use the tutor-moderated chat or breakout room voice instead (issue 18).

### Lesson 9: Data Detectives (minor fix)
- (a) Suitability: the weakest topic fit. Mean, "total = mean x number", and finding a missing value are core PSLE Paper 2 skills (Core Q1 to Q3 and Think Harder 1 to 2 are textbook PSLE average problems). Median and mode are the only new maths; the "misleading mean" idea (outlier) is the real value. The list-and-loop coding is the genuinely new part.
- (b) Difficulty: Core trivial for this audience; Challenge items (mean of 1 to 99 by pairing, five numbers with mean, median and unique mode) are good but are the only items that stretch the strongest children.
- (c) Coding: `item (i) of [scores]`, `length of [list]`, `change total by`, `say (total / 4)` are all correct Scratch 3. Good teaching idea: using `length of` instead of typing 5. Starter project (empty list `data`) is not in the repo. Footer reads "Math Inquirers P6 Holiday Program" on all 26 slides of L9 and L10, but "Math Inquirers P6" on L1 to L8.
- (d) Answers: all correct. `talkAns` is awkward ("the mean of 3, 0, 4, 1, 2 is 2 (that one is in the list, but it does not have to be)"); rewrite (issue 19).
- (e) Timing: ws1 42 to 53 and ws2 58 to 66; slightly tight. Challenge slide is labelled "65-80 MIN" which overlaps ws2 and talk.
- (f) "Everyone posts the number of letters in their full name" is a nice data source and avoids sharing names.

### Lesson 10: Showcase Challenge (needs rework, timing and scaffolding)
- (a) Suitability: excellent idea (own program, explained). Matches the "Notice it. Test it. Explain why." slogan. Not babyish.
- (b) Difficulty: the mixed challenge round (hexagon chain, 2-digit number with exactly 3 factors and digit sum 13, quick-fire) is well pitched. Q3(e)(f) (digit cards, probability) is a fun cross-lesson link.
- (c) Coding: all shown blocks are valid (starter A: `ask (join "OUT: " ((n * 3) + 4)) and wait`, `if answer = n then ... else`; starter C; Clock Jumper). However the three starter projects, which the lesson depends on, exist only as slide drawings; the "Python version" of starter B prints "1 factors" for n = 1 (cosmetic). A P6 child with school-level Scratch needs the starters as files, not as redrawn pictures (issue 7).
- (d) Answers: all correct (Q1 to Q4 rechecked).
- (e) Timing is the main problem (issue 11): "plan and build" runs 42 to 60 but includes 2 teaching slides, a worked example, and workbook Q4 to Q6, leaving about 8 to 10 minutes to actually build and test. Showcase 60 to 84 is 24 minutes for up to 8 children at 3 minutes each, with no time for changing screen-share, questions, or a late joiner.
- (f) Online: screen-share switching between 8 children costs 20 to 40 seconds each if not rehearsed; plan for it.

## 3. Numbered issues, ranked by severity

Severity: **High** = a child will get stuck or conclude the maths is wrong; **Medium** = confusing or wrong tutor guidance, or time plan unrealistic; **Low** = polish.

### High

**1. "when start clicked" is not a Scratch 3 block (L5, L6).**
- Where: `p6/content/l5.js` lines 78 and 79 (`listCode`, `planCode`); `p6/content/l6.js` lines 76 and 77 (`coinCode`, `planCode`); `rebuild/gen_p6l5.py` lines 115, 164, 231; `rebuild/gen_p6l6.py` lines 193 and 277; therefore the slides `p6l5-explore1`, `p6l5-teachcode`, `p6l5-teachhandcode`, `p6l6-teachcode`, `p6l6-teachplan` and workbook L5 Q3 and Q6, L6 Q2 and Q5 (9 occurrences).
- Why: the hat block is "when green flag clicked" (drawn "when [flag] clicked" in Scratch). L1 to L4, L7 and L8 already use `when green flag clicked`; these two lessons are inconsistent. A child will search the Events palette for "start" and not find it.
- Fix: replace every `'when start clicked'` with `'when green flag clicked'`. Regenerate the L5 and L6 slides and the workbooks.

**2. Plain `say` inside a loop shows only the last value (L1 Q5, L2 Q6, L2 `teachplan` slide).**
- Where: `p6/content/l1.js` line 221 (Q5 palette has `say (n)`); `p6/content/l2.js` line 217 (Q6 block A is `say (d)`); slide `p6l2-teachplan` ("It says 1, 2, 4, 5, 10, 20"); L1 Q5 text "say the first 20 terms".
- Why: in Scratch 3, each `say` replaces the previous bubble and the loop does not wait, so the child sees only the final bubble (118 in L1, 40 in L2) and cannot observe the 20 terms or the 8 factors the key says the program "says". The L1 `teachplan` slide and L3 to L5 workbook pages correctly use `say ... for 1 seconds`; these items are inconsistent with them.
- Fix: L1 Q5: change the palette block to `say (n) for (1) seconds` and add to the question: "(If you only want to see the last number, use plain say.)" Alternatively keep plain `say` and change the question to "Use only these blocks so that n ends on the 20th term; what does it say at the end?" L2 Q6: change block A to `say (d) for (1) seconds`; change the question to "...so the sprite says every factor of 40, one per second" and the key to "It says 1, 2, 4, 5, 8, 10, 20, 40 (8 numbers, one per second)". L2 `teachplan`: change the drawing to `say (d) for (1) seconds` and the notes line to the same.

**3. L8: the Scratch cipher machine is not buildable from what is shown, and spaces break it.**
- Where: slide `p6l8-we3` and `p6l8-teachtrace` (3 blocks only); workbook Q2 "Test your answers in Scratch"; explore message `PDWK LV IXQ`; materials text in `p6/content/l8.js`.
- Why: missing blocks are `set code to ""`, `set i to 1`, `repeat (length of (answer))`, `set letter to (letter (i) of (answer))`, the three shown blocks, and `change i by 1`. `item # of ( ) in [alphabet]` returns 0 for a space, so n = -1 and the space is replaced by the letter at index `shift - 1`. The notes expect the tutor to supply a "starter project", but none exists in the repo.
- Fix: (a) Add one slide `p6l8-teachloop` (before ws1) drawing the full machine (10 blocks: when flag clicked; ask "Message?" and wait; set code to (empty); set i to 1; repeat (length of (answer)): [set letter to (letter (i) of (answer)); set n to ((item # of (letter) in [alphabet]) - 1); set m to ((n + shift) mod 26); set code to (join (code) (item (m + 1) of [alphabet])); change i by 1]; say (code)). That is more than 15 blocks, so say in the notes: "Tutor gives the loop part pre-built in the starter; children add only the three cipher blocks." (b) Make the starter handle spaces from day one: wrap the three cipher blocks in `if <(item # of (letter) in [alphabet]) > 0> then ... else set code to (join (code) (letter))`. (c) Add this exact sentence to `lesson.online` in `l8.js`: "Starter project: the tutor shares an .sb3 file (not a link only) containing the list alphabet with A to Z already filled in, and the loop already built; children add the three cipher blocks." (d) Move the extension "keep spaces" into the starter and delete it from the extension text.

**4. L7: several programs, as specified, draw off the 480 x 360 stage.**
- Where: slide `p6l7-we1` (octagon, `move 80`), `p6l7-explore1` finished-early 10-gon, `p6l7-we3`/workbook Q3 (9-point star, `move 150`), workbook Q4 rows 2 and 3 (9 points x 4, 20 points x 3; no side length given), L7 `extension` rosette.
- Why: the sprite starts at (0, 0) heading 90 (right) and turns right, so shapes grow down and right. Simulated extents (y below the -180 stage edge is lost or kinked by sprite fencing): octagon move 80 reaches y = -193; 10-gon move 80 reaches y = -246; {9/2} star move 150 reaches y = -199; {20/3} star move 150 reaches y = -310.
- Fix: add one standard set-up to every drawing slide, to the L7 explore notes and to the workbook header: `erase all`, `go to x: (-50) y: (100)`, `point in direction (90)`, `pen down` (4 blocks, in addition to the loop). Then specify sizes in Q4: "Use move 100 for the 20-point star, move 120 for the 9-point star." Verified fits from (-50, 100): octagon move 80, 10-gon move 80, {9/2} move 150, {9/4} move 150, {20/3} move 100, all inside the stage. Also tell children "36 sides: use move 10".

**5. L7: "turn right 90 degrees" is not the Scratch 3 label.**
- Where: all L7 slides and workbook blocks; `SPEC.md`.
- Why: Scratch 3 has `turn ↻ (15) degrees` (clockwise) and `turn ↺ (15) degrees` (anticlockwise); there are no "right/left" words on the blocks.
- Fix: in the L7 block drawings write `turn ↻ (90) degrees`, and add to `p6l7-explore1` notes: "Use the clockwise arrow block (turn right = clockwise)". Keep "turn right" in the speech.

### Medium

**6. Colour and category errors in tutor notes; our block colours do not match Scratch's.**
- Where: `p6l4-explore1` notes: "ask is in Sensing (purple)" -> Sensing is light blue; purple is Looks. `p6l8-title` notes: "Dark-blue Scratch blocks for lists" -> list blocks are red-orange; variables are orange. Our drawn colours (hats yellow, variable blocks red, looks sky blue, control teal) differ from Scratch (events yellow, variables orange, looks purple, control gold, operators green, sensing light blue, motion blue, pen green).
- Fix: change both notes ("Sensing (light blue)", "list blocks are red-orange, in the Variables palette"). Add to the L1 title notes and to each lesson's "online" text: "Block colours on our slides are simplified; in Scratch, find blocks by the category name on the left, not by colour." Optionally add a one-page "Where is each block?" cheat sheet (Motion: move, turn, go to, set x, change x; Looks: say; Events: when green flag clicked; Control: repeat, repeat until, if, if else; Sensing: ask and wait, answer; Operators: + - * / mod pick random join letter of length of =, <, >, and; Variables: set, change, and the list blocks `item #`, `item of`, `length of`). Add the Pen extension note once in L7.

**7. Starter projects and tutor files exist only as descriptions (L1, L5, L6, L8, L9, L10).**
- Where: L1 online text "Send the four starter blocks ... in the chat" (blocks cannot be sent as text); L5 "Every Order"; L6 dice program for children without dice; L8 alphabet list; L9 `data` list; L10 starters A, B and C. No `.sb3` file is in the repo.
- Fix: build the eight .sb3 files once and keep them in `p6/starters/` (names: `L5_EveryOrder.sb3`, `L6_DiceRace.sb3`, `L8_CodeMachine.sb3`, `L9_MeanMachine.sb3`, `L10_A_Mystery.sb3`, `L10_B_PrimeOrNot.sb3`, `L10_C_LuckySeven.sb3`, `L10_D_ClockJumper.sb3`). Tell children to use File > Load from your computer (Scratch needs no account for that) and give shared project links as a backup. Replace the L1 sentence by "Share your Scratch window and build the four blocks together on screen; the blocks are also on the slide." Include the parents' page note: "Scratch is free at scratch.mit.edu; no account is needed in class."

**8. L5 starter says 1, 2, 3, not the tea names.**
- Where: `p6l5-explore1` notes and workbook.
- Fix: replace the explore instruction with: "Teas are numbered 1 = milk, 2 = green, 3 = taro; toppings 1 = pearls, 2 = jelly. The sprite says join tea topping, so 21 means green with pearls." Add the legend to the slide (one line under the menu board).

**9. Unicode minus in block drawings and typed numbers.**
- Where: all L3 to L10 slides and workbook text (U+2212 "−").
- Why: children typing "-3" use the hyphen, which is right; but the text in the chat or Slides copy-pasted into a Scratch number field is the Unicode character, which Scratch will not accept as a number (becomes 0 or is ignored).
- Fix: in the L3 notes add: "Type the minus with the keyboard minus key (hyphen); do not copy-paste from the slide." No content change needed.

**10. Worksheet pages cannot be finished in the minutes allotted (L1, L2, L5, L6, L7; tight in L3, L4, L8, L9).**
- Where: title-note time plans in all lessons. Estimated answer boxes (one box about 20 to 40 seconds when handwriting online, a trace or table row about 1 minute):
  - L1 ws1 about 24 boxes / 10 min; L2 ws2 about 35 / 6 min; L5 ws2 about 25 / 7 min; L6 ws2 about 36 table cells + 7 answers / 8 min; L7 ws1 about 20 + two Scratch runs / 10 min and ws2 about 45 / 11 min.
- Fix (uniform): the unused slack is in "talk time 70-80" (10 min for two spoken questions) and "exit ticket 80-90" (10 min for one short question). Change to: worksheet 40-75 (35 min, with the two short teaching slides and the two check slides inside it), talk 75-82, exit 82-90. Also move one item from each overloaded page to Think Harder: L2 Q5 (3-factor numbers; the answer is already in the `teachsq` slide); L5 Q5(b) puddle; L6 Q4(d) (fair redesign); L7 Q5 (move to a home extension) and trim Q1 table to 4 rows (3, 9, 10 and the two backward rows; drop 36). Update `deck.json`/slide time labels accordingly.

**11. L10 timing and flow.**
- Where: title notes of `p6l10-title` and slide time labels.
- Why: challenge round 10 to 30 (20 min), starters 30 to 37, break, then plan and build 42 to 60 (18 min) which already contains the `teachplan` and `teachtest` slides (3 min) and workbook Q4 to Q6; actual build and test time is 8 to 10 minutes. Showcase 60 to 84 is exactly 8 x 3 min with zero switching time; the rubric asks the tutor to ask questions and collect "two stars and a wish", and `talk` and `exit` follow immediately. A child who builds a working program in 8 minutes is unrealistic.
- Fix: (a) Cut the warm-up to one slide (0-5), challenge round 5-22 (17 min), starters 22-29, break 29-32 (3 min), plan and build 32-62 (30 min), showcase 62-87 at 3 min plus a 20-second switch each, exit and certificates 87-90. (b) Tell children in lesson 9 (the close already hints at it) to choose their puzzle in advance and bring a plan; add a homework line to the L9 `close`: "Decide which starter you will change: A, B, C or Clock Jumper, and what your twist will be." (c) Allow a "no screen-share" option: a child may paste a screenshot into the chat and the tutor runs their file, to remove switching time. (d) Make the build target concrete: "a working copy of one starter with one change" is full marks; own idea is optional.

**12. L4 Q1(c): IN steps by 2 but the hint is "per 1".**
- Where: workbook Q1(c) (IN 2, 4, 6, 8) and the teaching hint.
- Fix: replace Q1(c) IN row with `1  2  3  4  20` (OUT 1, 5, 9, 13, ?) -> rule 4n - 3; OUT for 20 = 77 (same answer as the key). Or keep the table and add to the question: "(IN goes up by 2 each time; how much does OUT go up for each 1 of IN?)".

**13. L7 Think Harder pages: two abstract items.**
- Where: `qbank.challenge` items 8 and 9 in `p6/content/l7.js`, which print as two of the last three Think Harder items.
- Why: "Find two other sets of three regular polygons that fit exactly around a point" needs interior angles of up to 42-gons and the key lists answers of 7, 18 and 24 sides that a child cannot reasonably find; "Why can a turtle not draw a 6-point star in one go?" has a subtle answer ("a hexagram is two triangles, so it needs the pen lifted") the question never hints at.
- Fix: item 8: "Squares, hexagons and 12-sided shapes can fit around a point: 90 + 120 + 150 = 360. Find one other set of three regular polygons whose inside angles add up to 360 (hint: the answer uses a square or a triangle)." Answer: "square + octagon + octagon (90 + 135 + 135) or triangle + 12-gon + 12-gon." Item 9: replace with: "Try turn 120 and turn 60 with repeat 6 and move 100. Which one draws a hexagon? Why does the other not make a 6-point star?" Answer: 60 draws a hexagon; 120 draws a triangle twice round. Keep the 1800-degree item.

**14. L3 challenge 9 changes the floor-numbering convention.**
- Where: `qbank.challenge` item 9 in `p6/content/l3.js`.
- Fix: "In many Singapore buildings there is no level 0: level 1 is the ground floor and B1 is the level below it. A lift goes from level 4 down to B3. How many floors does it go down? (Count the levels one by one; do not use a number line with 0.)" Answer unchanged: 6. Delete the second sentence "Why is 4 - (-3) = 7 not the answer?" or keep as a separate follow-up.

**15. Coding load for children with only school-level Scratch.**
- Where: whole programme; L2 is the first lesson with if + mod + counter + if/else together, L4 adds `ask`/`answer`, L8 adds lists, L9 lists again.
- Fix: send a 10-minute "Scratch warm-up" video or one-page handout before lesson 1 covering: green flag, `repeat`, make a variable, `set`/`change`, `say ... for ... seconds`. In L2 move the `if count = 2 then say prime else say not prime` extension to the last slide of the lesson, so the main program is `if (n mod d) = 0 then change count by 1` only. State in `SPEC.md` which blocks are assumed known (events, repeat, variable set/change, say). In L3 teach "make a variable" (click Make a Variable) in the tutor's screen share.

### Low

**16. L7 `we1` / `extension` details.** Add `erase all` to the first drawing so re-runs do not overlap (the notes mention it, the slide does not). Rosette extension (12 squares, turn 30) draws within the stage (x and y within +-137 from the start at 0,0 with side 100; start at (0,0) is fine).

**17. L5 `teachcode` note wording.** Replace "so shirt 2 would start at shorts 3 and say nothing new" with "so shirt 2 would start at shorts 3 and say 23 and 24, which are not real outfits".

**18. L8 private chat between children.** In `lesson.online` of `l8.js`, replace "Coded names are sent privately in the chat to a partner to decode" with "Children hold up their coded name on paper to the camera, or the tutor reads out the coded names; partners decode on paper." Many tutoring policies disable private chat between minors.

**19. L9 `talkAns` wording.** Replace the sentence "Yes: the mean of 2 and 3 is 2.5, which is not in the list, and the mean of 3, 0, 4, 1, 2 is 2 (that one is in the list, but it does not have to be). No: ..." with "Yes: the mean of 2 and 3 is 2.5, a number nobody in the group has. No: the mean is always between the smallest and the largest value. ..."

**20. L9 and L10 footers.** 52 slides say "Math Inquirers P6 Holiday Program"; L1 to L8 say "Math Inquirers P6". Make L9 and L10 match (edit `rebuild/gen_p6l9.py` and `gen_p6l10.py`). Also `p6/data.js` first comment says "from p2/content" (it reads p6/content): cosmetic.

**21. Brain breaks are on the young side (L1 clap-clap-stomp, L3 Human lift, L4 Jumping machine, L5 Every possible pose, L6 Human dice, L9 Dice jumps).** They are short and the maths link is good, but cameras-on 12 to 13 year olds may feel silly. Offer a silent alternative in the notes ("a 60-second stretch plus one riddle on screen") and let the child pick.

**22. Singular "dice" (L6).** Scripts say "Roll a dice", "one dice". Singapore classrooms often use "dice" for both; if you prefer standard British usage, use "die" for one and "dice" for several. Optional; note the workbook itself says "red die and blue die" once, so be consistent.

**23. Python snippets (optional versions).** All 20 snippets run and print the stated output (see section 4). Minor polish: L10 prime checker prints "1 is not prime. It has 1 factors." (suggest `factor(s)`); L7 prints floats `144.0 720.0` (already in notes, add to workbook box); L2 list comprehension is above the other snippets' level (offer the loop form); L7 needs a graphical Python environment (state "use Trinket or a desktop Python with turtle").

**24. L3 Q7(b) wording.** "After the loop, which number in 'change depth by ___' brings her back to sea level?" is ambiguous because no such block is shown. Rewrite: "After the loop she is at -28 m. She then runs one more block: change depth by ___. What number brings her back to 0 m?"

### Verify in the editor (10 minutes before the programme goes out)
Open scratch.mit.edu and confirm: (1) the hat block text is "when [flag] clicked"; (2) the turn blocks show arrow icons not "right/left"; (3) `item # of ( ) in [list]`, `item ( ) of [list]`, `length of [list]` names; (4) the Sensing category is light blue; (5) the list blocks' colour (red-orange); (6) `( ) mod ( )` with a negative number returns a non-negative result (-4 mod 26 -> 22); (7) the sprite fencing behaviour for the L7 sizes you finally pick.

## 4. Python snippets: run results

All run with python3 (turtle stubbed). Stated output matches actual output.

| Lesson | Snippet | Result |
|---|---|---|
| 1 | `we2` term 5, 99 jumps | 302 as stated |
| 1 | `teachplan` 10 terms 7, 12, ... | 7, 12, ..., 52 as stated |
| 1 | `chwalk` triangular code | 5050 as stated |
| 1 | `explore1` sticks 3 + 9 x 2 | 21 as stated |
| 2 | `we3`, `teachtrace`, `teachplan` | not prime, 3, then 1 2 4 5 10 20 as stated |
| 2 | `chwalk` lcm search | 60 as stated |
| 3 | thermometer (explore notes) | 2, -1, -4, -7, -10, -13 as stated |
| 5 | tea/topping loop, outfits, handshakes | 6 orders, 6 outfits, 10 handshakes as stated |
| 6 | Dice Race simulation | e.g. `321 679` (random; fine) |
| 7 | star/turtle | prints `144.0 720.0`; with n, k = 8, 1 prints `45.0 360.0` as stated |
| 8 | Caesar `MEET AT THE MRT`, shift 3 | `PHHW DW WKH PUW`; negative shift decodes as stated |
| 9 | mean / above-mean | Total 10, Mean 2.0, Above 2 as stated |
| 10 | Mystery Machine, prime checker, Lucky Seven, Clock Jumper | correct (random ones near 167 as stated) |

## 5. What is already strong (do not change)

- The "predict, then test in code, then explain" routine and the fence-post (99 jumps for the 100th term) lesson in L1.
- L2 sieve + factor pairs + "stop when d x d is bigger than n".
- L3 "a - b is the jump from b to a", with "check by adding back".
- L4 "run the machine backwards, then check forwards", plus `repeat until` as brute-force search.
- L5 nested loop = multiplication rule, and the handshake "a < b" trick.
- L6 pooled class tallies and the "close, not exact" language; the 1000-game simulation.
- L7 360-degree turn idea (and the "turn 60 draws half a hexagon" error that children make, anticipated).
- L10 rubric (maths, testing, code, explaining) and the "known-answer + edge-case" testing discipline.
- Plain, diverse names (Ali, Mei, Ravi, Siti, Jun, Ben) and Singapore contexts.
