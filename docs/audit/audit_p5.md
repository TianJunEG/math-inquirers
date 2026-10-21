# Audit: Math Inquirers P5 Holiday Program (suitability and difficulty)

Scope: `p5/content/l1.js` to `l10.js` (lesson, script, deck, qbank, workbook), `p5/data.js`, `p5/SPEC.md`, the ten slide decks in `split/p5l1` to `split/p5l10` (all child-facing slide text and every tutor note was read), and the printed workbook `p5/Math_Inquirers_P5_Student_Workbook_Designed.pdf` (page layout).
Audience judged: children aged 11-12 who have just finished Primary 5, going into P6, 10 x 90 min, online, groups of 8, inquiry style.
Date of audit: 2026-10-22. No content files were edited. Nothing was committed.

## How the checks were done

- Every numeric answer in the `key`, `qbank` (core 6, stretch 8, challenge 9 per lesson), `deck.warmQs`, `deck.expAsk`, `mini1/mini2`, the slide-only worked examples ("try" and "teach" slides) and the slide-only stretch and challenge items was recomputed.
- Python with exact `Fraction` arithmetic or brute force was used for: L1 Q3 (digit riddle, unique), Q5 (bracket placements, unique), Q6 (list of 6), the "biggest bracketing" challenge (231 confirmed over all bracketings), the 7-digit odd puzzle, the digit count 1 to 1 000 000 (5 888 896); L2 unit-fraction splits for 7/10, 9/20, 3/8, 7/12, 2/3, 5/12 (all match the keys), "1 as three unit fractions" (only 1/2+1/3+1/6), digit-card sums for L2 Q6 and the challenge (11/2, 5/6, 11/12, 8/35), telescoping sum 5/14; cuboid counts for 24, 36, 60, 64 cubes (6, 8, 10, 7); L6 cheapest 20+ cans ($13.64) and eggs ($9.60); L10 coin puzzles; the 3, 5, 7, 9 to 100 puzzle (only one expression exists).
- Everything else (fraction word problems, areas, tank volumes, rates, percentages, angle chains, patterns, logic) was recomputed by hand with a second method, including re-deriving every figure's numbers from the SVG coordinates in L4 and the `aria-label` data in L5 to L9.
- **Result: no wrong numeric answer was found in any lesson.** Every issue below is about difficulty, syllabus level, spoilers, wording, timing or layout.
- Syllabus sources used (MOE school handbooks and schemes of work that quote the 2021 Standard Mathematics syllabus): Shuqun Primary P5 Mathematics Handbook, Shuqun Primary P6 Mathematics Handbook, Punggol Cove P5 Standard Mathematics parents' handout, Tampines North P5 Standard Math SOW outline.

## Syllabus facts that matter for this audit

| Skill | Where MOE puts it | Used in |
|---|---|---|
| Whole number to whole number division with fraction quotient (3 / 4 = 3/4); multiplying proper fractions | P5 | L2 (fine) |
| **Dividing a proper fraction by a whole number** | **P6** (listed in the P6 handbook; not in the P5 handbook) | L2 objective, teach1, try1, workbook Q1c, qbank core 6, stretch 6 |
| Percentage of a quantity, discount, GST, annual interest | P5 | L7 (fine) |
| **Percentage increase / decrease; finding the whole given a part and the percentage** | **P6** | L7 Q5 and teachchange slide, L7 qbank core 6, challenge 1, 2, 4, 7, 9 and the printed Think Harder Q5, Q7 |
| Rate (amount per unit; find rate, total, or number of units) | P5 and P6 | L6 (fine). Adding two rates / "taps together" is an extension of this |
| Volume of cube/cuboid, liquid in a rectangular tank, ml = cm3 | P5 | L5 (fine) |
| **Finding a missing edge/height from the volume** | listed under **P6** | L5 warm-up (missing edge), rise = volume / base area (natural inverse; judged "reasonably just beyond", acceptable) |
| Unknown angles on a line, at a point, vertically opposite; triangle sum; isosceles and equilateral; parallelogram, rhombus, trapezium (no extra lines) | P5 | L8 (fine; the chains stay inside these facts) |
| Ratio, average | P5 / P6 respectively in the 2021 documents (ratio appears in the Tampines North P5 SOW and Punggol Cove P5 handout) | not used in the program at all |
| Speed, circles, algebra with letters, pie charts, negative numbers | P6 / secondary | **none used by the children** (checked with a text search of all content and slides) |

Note on `SPEC.md`: it says "Do NOT use ... ratio (that is P6)" and lists "dividing a proper fraction by a whole number" as something P5 children know. Both statements are the wrong way round for the 2021 syllabus documents above (ratio is taught at P5; fraction division is P6). This does not harm the children, but the spec should be corrected so later edits do not rely on it.

## Summary table

| Lesson | Verdict | One-line reason |
|---|---|---|
| L1 Million Puzzles | minor fix | All answers correct. Page 2 is too long for 7 minutes; Q3 riddle is Think-Harder-weight on a Core page; Challenge 3 is a very long hand count. |
| L2 Fraction Feats | minor fix (one real defect) | The "look for a pattern" teaching slide gives away workbook Q4a and the key idea of Q4c; fraction division is P6; 18 sub-parts. |
| L3 Before and After | minor fix | Sound and well scaffolded. Page-2 Q5 (bead box, changing denominators) is Think-Harder level but is set to be done alone. |
| L4 Triangle Areas | OK | Best-pitched lesson. Only Think Harder items that need a figure have none; page 2 time. |
| L5 Volume Vault | minor fix | Worksheet runs to 3 printed pages (Q6 alone on page 3); teachlist gets 1 minute; Q1b wording; challenge 1 repeats Q6c. |
| L6 Rate Racers | minor fix | Worksheet runs to 3 printed pages; Q2c is an optimisation search on a Core page; decimal-by-decimal division on the first slide. |
| L7 Percentage Puzzles | needs rework | 7 questions in 2 pages, P6 content (percentage change, reverse percentages) in Core and Think Harder, and no time for any of it. |
| L8 Angle Chasers | minor fix | Content is accurate and level-appropriate; the volume of written reasons (about 12 lines in 7 minutes) is the problem. |
| L9 Pattern Generalisers | OK | Well pitched, well parallelled, light reading load. Minor page-2 timing only. |
| L10 Challenge Day | minor fix | The logic grid depends on guessing who is a girl; Think Harder numbering note is wrong; "4 stations" does not exist online. |

Cross-cutting (all lessons): the 90-minute plan gives page 2 only 7 minutes (issue 1) and the online set-up has several practical traps (issue 12 to 15).

## Issues, ranked by severity

Severity key: **High** = fix before delivery (spoiler, layout break, syllabus mismatch, plan that cannot run). **Medium** = will cause visible trouble in class. **Low** = polish.

### HIGH

**1. All lessons: page 2 gets 7 minutes (60 to 67) and nobody can finish before the "early finisher" window opens at 65.**
Every title slide uses the same plan: warm-up 0 to 10, explore 10 to 25, teaching 25 to 35, break 35 to 40, **ws1 40 to 52 (12 min, in pairs), check 52 to 54, three short teach slides 54 to 60, ws2 60 to 67 (7 min, solo), check 67 to 69**, stretch and challenge from 65, talk 70 to 80, exit 80 to 90. Page 2 has 3 or 4 questions and 4 to 8 sub-parts in every lesson (L2 8, L6 8, L7 7 in four questions, L8 7 with a written reason each, L5 6 with two multi-step tank problems). An 11-year-old working alone online needs about 1.5 to 3 minutes per multi-step sub-part. Seven minutes is realistic only for L9 and L1's easier parts, and "stretch and challenge from 65" is meaningless when page 2 ends at 67.
Proposed fix (same in all ten `rebuild/gen_p5lN.py` plans and the "Time plan" text in each title slide's notes): shorten the explore talk and the break, give page 2 twelve to fifteen minutes, and make stretch/challenge optional (home or only if a child finishes):
`warm-up 0-9, explore 9-21, teaching 21-33, brain break 33-37, worksheet page 1 37-49, check 49-51, short teaching before page 2 51-57, worksheet page 2 57-72, check 72-76, talk time 76-82, exit ticket 82-90 (L10: exit 82-88, certificates 88-90). Stretch and challenge are for children who finish early, or for home.`
Also update the per-slide "NN-NN MIN" badges to match. If the plan cannot be changed, cut each page 2 to its first two questions and move the rest to "If you have time" (see issues 8 and 9 for the lessons where this matters most).

**2. L2 `split/p5l2/project/slides/p5l2-teachpattern.html`: the teaching example gives away workbook Q4 (spoiler against the SPEC rule "teaching examples must NOT give away the workbook answers").**
Workbook Q4a asks for the next two fractions after 1/2, 1/6, 1/12, 1/20 (answer 1/30, 1/42) and Q4c needs the idea "each term is a difference of two unit fractions, so the sum telescopes". The slide shows "1/3 - 1/4 = 1/12 and 1/4 - 1/5 = 1/20. What is 1/5 - 1/6? = 1/30 (5 x 6)", then adds 1/30 + 1/42 as a difference of unit fractions. That is Q4a's answer, Q4b's last line and Q4c's method.
Proposed replacement (slide body, then note). Verified: 1/7 - 1/8 = 1/56, 1/8 - 1/9 = 1/72, 1/10 - 1/11 = 1/110, 1/56 + 1/72 = 2/63.
- Heading: `Look for a pattern`
- Prompt: `1/7 - 1/8 = 1/56 and 1/8 - 1/9 = 1/72. What is 1/10 - 1/11?`
- Step 1: `Bottom numbers: 56 = 7 x 8 and 72 = 8 x 9. So 1/10 - 1/11 = 1/110 (10 x 11).`
- Step 2: `Now add: 1/56 + 1/72 = (1/7 - 1/8) + (1/8 - 1/9).`
- Step 3: `The 1/8 cancels: 1/7 - 1/9 = 9/63 - 7/63 = 2/63.`
- Note check line: `Check: 1/56 + 1/72 = 9/504 + 7/504 = 16/504 = 2/63.` Replace "Next you will meet a different set of fractions with the same trick." by "Next you will meet a set of fractions that starts 1/2, 1/6 ..." only if you still want the link; do not show the terms.
(The same family appears in the printed Think Harder challenge 5 [1/6 + 1/12 + ... + 1/42], which is fine because that is the stretch use of the idea.)

**3. L5 and L6 printed workbook: each lesson's worksheet runs to three pages instead of two.**
In `p5/Math_Inquirers_P5_Student_Workbook_Designed.pdf` (49 pages, every other lesson takes four pages: two worksheet pages, two Think Harder), L5 takes pages 19-23 (Q6 sits alone on page 21) and L6 takes pages 24-28 (Q3 sits alone on page 25, then Q4 starts a new page because of the forced break). The slides ("page 1 = Q1-Q3, page 2 = Q4-Q6") and the 12/7-minute split assume two pages, and a stray one-question page is easy for a child to skip online.
Proposed fix:
- L5: remove the extra vertical space (shrink `figQ4` and `figQ6` display width from 400 to about 330 px, or cut the figure heights), or move Q3's figure beside the text as Q1 already does, so Q4 to Q6 fit on one page. If it still spills, delete Q6(c) and use it as Think Harder.
- L6: reduce `figTaps` (680 x 260 shown at 430 px) to about 330 px width and drop the 90-px table rows in Q6 to 60. The first-page questions then fit; page 2 already starts with `pb:true`.
Re-run `node workbook_html.js && python3 wb_pdf.py` and confirm 4 pages per lesson.

**4. L7: lesson is overloaded and contains P6 content in the Core and Think Harder pages.**
- Count: 7 questions, 15 sub-parts, 346 words, with two tables, a bar figure and a "which deal" comparison, in two pages, page 2 being four questions (Q4 to Q7) in 7 minutes.
- P6 content in Core: **Q5 (percentage increase from $4 to $5, decrease from $5 to $4)** is "percentage increase/decrease", listed at P6; the teaching slide `p5l7-teachchange` teaches it from scratch. Also `qbank.core[5]` ("$20 to $25, what is the percentage increase?").
- P6 content in Think Harder: challenge 1 ("$109 GST included: find the GST") and challenge 3 ("Mrs Tan ... $54 left", finds the whole from 75% and 60%) both need "find the whole given a part and the percentage"; stretch/challenge 2, 4, 7 of the qbank also do. The printed page presents them as ordinary Think Harder items with no warning.
- None of this is unreasonable for strong thinkers, but it must be flagged and it must not sit on the Core pages.
Proposed fix:
  (a) Move Q5 (percentage change) and Q7 (deals) off page 2: keep Q4 (percentage of the remainder, which is P5) and Q6 (class table) on page 2, make Q5 and Q7 the first two Think Harder items (or "If you have time"). 
  (b) Add to the lesson `objective` and the Think Harder banner a one-line flag: `Preview of P6: percentage change and finding the whole.` In `workbook_html.js` the `extra()` banner for L7 could read `Challenge (for strong thinkers: P6 preview)`.
  (c) If Q5 stays in Core, add one scaffolding line under it: `Percentage change = change / the amount you START with.` (this line is the only thing a child needs; it matches the slide).
  (d) In the Q4 text, the three sentences are fine, but Q6 begins "There are 40 pupils in a class. 60% of them are girls. 25% of the girls and 50% of the boys wear glasses." Keep it, and cut Q7's two-part (b) ("really how many percent off") to Think Harder.

**5. L2: fraction divided by a whole number is P6 content presented as P5 Core.**
Objective, `teach1` slide, `try1` (4/5 / 3, 6/7 / 3), workbook Q1c ("3/4 of a cake shared by 6 children"), `qbank.core[5]` (6/7 / 3) and `qbank.stretch[5]` (3/4 m / 3). The teaching is pictorial and good (cut every part again), and the sharing story is natural, so this is "reasonably just beyond", but it is labelled and printed as Core.
Proposed fix: keep the content, change the labelling. In `lesson.objective` write `... and (as a preview of P6) divide a proper fraction by a whole number.` In `teach1` notes add `This is a P6 skill: children who have not met it may need the picture twice.` Make workbook Q1c the last part of Q1 and mark it `(stretch)`: `(c) (stretch) 3/4 of a cake is shared equally among 6 children. Each gets ______ of the whole cake.` Keep `core[5]` but change it to `Work out 3/5 x 1/2 + 1/10.` (or move 6/7 / 3 to stretch) so the Core row is P5-only.

### MEDIUM

**6. L3 Q5 (bead box, 3/7 red, 30 red added, now 3/5 red) is Think Harder in a Core slot, done solo.**
The key is correct (70 at first, 100 now). The "one amount stays the same, fraction changes" model needs the child to re-unit from 7 parts to 5 parts of a different total. The only parallel example (`teachone`) uses 2/5 to 1/2 (3 units to 3 units, no re-uniting) and lasts 2 minutes. Q4 is also solo on the same page.
Proposed fix: add a scaffold under Q5 in the workbook: after sub-part (a) insert `(b) Before: red 3 units, blue ______ units. After: blue is 2 out of every 5, so if blue is still ______ units, the whole box is ______ units.` and renumber b to c and c to d. Or, quicker, move Q5 to the Think Harder challenge list and give Q4 and a second easy before-and-after question (for example qbank core 4) its page-2 slot.
Also, tutor note in `p5l3-ws2ans` uses ratio notation (`red : blue is 3 : 2`). Rewrite as `red is 3 parts out of 5 and blue is 2 parts out of 5`.

**7. L6 Q2(c) is an optimisation search on a Core page.**
"Ben needs at least 20 cans ... whole packs ... least he can pay" with three pack types is a small integer-programming problem. The key (12 + 2 x 4 = 20 cans for $13.64) is correct (confirmed as the true minimum by checking all combinations up to 5 packs), but the slide note justifies only the exact-20 combination, not why 22 or 24 cans cannot be cheaper (they cannot: 22 cans $14.92, 24 cans $15.60). A child who finds 22 cans for $14.92 and stops has done good work but gets marked wrong with no explanation.
Proposed fix: replace (c) with an easier target: `(c) Ben needs exactly 20 cans. He can buy from more than one shop, but only whole packs. Find one way and work out the cost.` (Answer: 1 pack from C and 2 packs from B, $13.64; also 20 = 6 x 2 + 4 x 2 = $8.40 + $5.84 = $14.24, so "compare two ways".) Put the original "least cost, at least 20 cans" into the Think Harder challenge list with the explanation `22 cans: C + A + B = $14.92; 24 cans: 2 x C = $15.60`.

**8. L6 slide `p5l6-teach1`: decimal divided by decimal.**
`$13.30 / $1.90 = 7 kg` is a division of a decimal by a 2-dp decimal, which is not in the primary syllabus. The note says "think 1.90 x 7 = 13.30", which is guess-and-check, not a method.
Proposed fix (slide text, step 3): `Backwards: 1330 cents / 190 cents = 7 kg.` and in the note: `Change dollars to cents first (1330 / 190 = 133 / 19 = 7). Children who prefer can test: 7 x $1.90 = $13.30.` Do the same wherever a decimal quotient appears.

**9. L6 talk question and challenge 1 and 9: "work together" (time-to-fill from two times) is beyond P5.**
The shared `talk` question (Tap A 20 min, tap B 30 min; Ben says 50, Mei says 25) is shown to every child, but the method needs a made-up 60 l tank and the idea of rate from time-to-fill. This is a fair stretch, but the Core `share` prompt should not be one.
Proposed fix: change `lesson.share` and the `talk` slide to the Core-level one already in the script: `Is the biggest pack always the best buy? Give an example with numbers.` and move the two-tap time puzzle to the challenge slide.

**10. L7/L2/L6/L8 page-1 and page-2 writing load for 11-year-olds online (see also issue 1).**
L8 asks for a written reason on 8 separate angles on page 2 (Q3 a to d with "because ____", Q4 d with "show how you found") plus Q5 listing cases, all in 7 minutes. Online, the child must also hold the paper to the camera.
Proposed fix for L8: change the printed Q3 stem to `Write the reason only for the angles marked (b) and (d); for (a) and (c) just write the answer.` and keep 8 lines of reasons for Q1 and Q2 (page 1, in pairs). Alternatively provide a tick-box strip of the six angle facts at the top of page 2 so children write a letter (A to F) instead of a sentence. Add to the L8 workbook header: `Reasons: A straight line 180°. B point 360°. C vertically opposite equal. D triangle 180°. E isosceles base angles equal. F parallelogram/trapezium neighbours 180°.`

**11. L5 Q1(b) wording (the known judgement call) and two small L5 problems.**
- Q1(b): "Mei adds more 1-cm cubes to turn it into a cube. What is the fewest number of cubes she must add?" is readable as "fewest to make any cube" (then 64 - 24 = 40 is correct). It could also be read as adding cubes only on the outside faces, or as "which cube". The interpretation 40 is the natural one, but say it.
  Proposed replacement text: `(b) Mei adds more 1-cm cubes to the solid, without taking any away, until the whole solid is a cube. What is the fewest number of cubes she must add? Explain.`
- `teachlist` (listing every cuboid from 30 cubes, with "your turn: 20 cubes") is scheduled in a single minute (33 to 34, overlapping `try2`). This is the key method for workbook Q2. Give it its own slot (for instance 33 to 35 by moving `key` to 35 to 36 and the break to 36 to 40, which is already how L9 is timed) and drop `try2` or `try1` if time is short.
- Challenge 1 (two tanks, equal depth) repeats the exact method of workbook Q6(c) and the `teachpour` slide with the same tank bases (30 x 20 and 40 x 30). It is not a challenge. Replace with the upright-block idea (already challenge 2) plus a new one: `A tank has a base 40 cm by 30 cm. A cube with edges of 10 cm sits on the bottom, and the water is 6 cm deep around it. How much water is in the tank?` Answer: 40 x 30 x 6 - 10 x 10 x 6 = 7200 - 600 = 6600 cm3 = 6.6 l. (Hand-checked; the cube is taller than the water, so only 6 cm of it is under water.)

**12. Think Harder pages print figure-dependent problems with no figure, and only 3 or 4 answer lines.**
`workbook_html.js` prints `qbank.stretch[0..3]` and `qbank.challenge[-3..]` as text only. Items that cannot be solved without a figure or a careful drawing: L4 challenge 8 (two squares side by side, three named corners), L4 challenge 7/9 (triangle on BC), L8 stretch 3 (trapezium), stretch 4 (square with an equilateral triangle outside), challenge 7 and 8 (isosceles inside an isosceles; equilateral inside a square), L5 challenge 9 (upright block). The printed intro says "Draw a model, make a list or make a table" which helps, but the child must invent the diagram from words, online and alone.
Proposed fix: add a small figure to those eight items (they already exist as SVG in the deck `chdiag` slides, so reuse the same drawing functions in `workbook_html.js`) or, as a minimum, add the line `Draw a big, neat diagram first and label every length or angle you know.` to the Think Harder header in `extra()`.

**13. L10 workbook Q2: the logic grid depends on the child guessing who is a girl.**
Clue 2 is "The roti prata was ordered by a girl." The key assumes Mei and Siti are girls and Ali and Ben are boys, but nothing in the text says so, and "Mei" and "Ali" are used for both genders elsewhere in the program. A child who treats Ali as a girl gets a different (wrong) answer.
Proposed replacement of the clue line: `Clue 2:  The roti prata was ordered by a girl (Mei and Siti are girls; Ali and Ben are boys).` Verified: with this the puzzle has exactly one solution (Ali chicken rice, Ben laksa, Mei satay, Siti roti prata).

**14. L10 slide notes mislabel the Think Harder numbers; "4 stations" does not exist online.**
- `p5l10-challenge` notes say "These are Think Harder Q5 and Q7". The slide shows the monkey puzzle (qbank challenge index 5) and the four-chairs puzzle (index 8). The printed Think Harder prints the last three challenge items, so its Q5 is the water-tank question (index 6), Q6 the coins (index 7), Q7 the chairs. The monkey puzzle is on no printed page. Fix the note: `These are Think Harder Q7 (the chairs); the rambutan puzzle is in the question bank only.` Or print it by making Think Harder Q5 the monkey puzzle.
- `lesson.materials` says `Puzzle cards for 4 stations`, but the lesson (explore, online) is a menu of four cards shared on screen. Change to `Four puzzle cards shown on the slide (or sent as images to each breakout room)`.

**15. L1: three small wording and difficulty points.**
- Q2: nothing tells the child a 7-digit number cannot begin with 0 (0 235 689 is six digits). The key's answers depend on it. Add to the question stem: `A 7-digit number cannot start with 0.`
- Q3 (six-clue riddle, 7 constraints) is a good puzzle but is Think-Harder weight on Core page 1. The slide example `we2` (3 594 208) is very close to it, which rescues most children. Keep it, but allow the extra time: ws1 is 12 minutes for Q1+Q2(a to c)+Q3. Move Q2(b) ("smallest even number") to the stretch list if time is short (the `try2` slide already practises it).
- Challenge 3 (Think Harder Q7, `Ali writes all numbers from 1 to 1 000 000`, answer 5 888 896) requires about six multiplications with 5- and 6-digit numbers by hand. Correct, but it is a calculator-length task for 11-year-olds. Proposed easier text with the same idea: `Ali writes all the whole numbers from 1 to 1000. How many digits does he write?` (answer 9 + 180 + 2700 + 4 = 2893), keep the 1 000 000 version as an optional "go further".

**16. L2 slide `p5l2-stretch`: two of the three "new" stretch items are already printed on the Think Harder page.**
`Ben ate 1/3 of a pizza ...` is workbook Think Harder Q2 and `4 litres of juice ... 6 bottles` is Think Harder Q4 (they are `qbank.stretch[1]` and `[3]`). The deck brief says the stretch slide should have 3 new items. Replace the two with `qbank.stretch[5]` and `[7]` if those are kept in Core as in issue 5, or with new ones: `Find a fraction between 2/5 and 1/2 with 20 as the bottom number.` (Answer 9/20; 2/5 = 8/20, 1/2 = 10/20.) and `Which is bigger, 7/8 of 24 or 5/6 of 30? ` (Answer: 21 and 25, so 5/6 of 30.)

### LOW

**17. Tutor-note vocabulary and notation.** L2 `ws2ans` notes use `1/(n x (n+1)) = 1/n - 1/(n+1)`; L9 `chwalk` notes use `(2n - 1)` and `n x n`. These are notes, not child-facing, so no harm, but the SPEC says no algebra letters. Rewrite in words for tutors who may read them aloud: `a unit fraction 1/n minus the next one is 1 over (n times the next number)`.

**18. Vocabulary load.** Words that appear in child-facing questions and are not taught: `palindrome` (L1 challenge 4, bank only), `consecutive` (L10 stretch 3, Think Harder Q3), `composite figure` (L4 objective only), `supposition` (L9, taught in the lesson), `unit fraction` (taught), `vertically opposite`, `base angles` (taught), `rambutan` (L10 challenge). Add a gloss in brackets in the two printed ones: `consecutive (next to each other, like 40 and 41)`; `palindrome (reads the same forwards and backwards)`. Reading load otherwise is acceptable: longest printed stems are about 45 words (L9 Q5, L10 Q5); the heaviest pages by words are L2 (419 words, 18 sub-parts) and L7 (346).

**19. L5 materials: cubes for every child.** `about 30 one-centimetre cubes` is per child, and L9 asks for about 40 matchsticks per child; with 8 children online a parent must supply these. Add to the pre-programme parent note: `Lesson 5: 24 to 36 small cubes (dice, Lego, sugar cubes) or squared paper; Lesson 9: 20 matchsticks or toothpicks.` Both lessons already allow squared-paper substitutes; say so in the parent note.

**20. Several slides state a time that overlaps the next slide.** L2 `we2` 32-35 overlaps `try2` 32-33; L4 `teach2` 28-31 overlaps `try1` 28-29; L5 `try2` 33-34 and `teachlist` 33-34. Clean up the badges when the plan in issue 1 is rewritten.

## Lesson-by-lesson judgement

### L1 Million Puzzles (verdict: minor fix)

(a) Topic: place value to 10 million, estimation, order of operations: all P5. Rounding to the nearest hundred thousand and thousand is a small stretch beyond the usual "10, 100, 1000" rounding and is taught on the slides. No P6 content.
(b) Difficulty:
- Core (Q1, Q2a-b, Q4, Q5a-c, Q6a): doable by most. Q1c (How many thousands make 3 250 000) and Q5c (a long division with brackets) are the only items with some bite.
- Think Harder items: bracket tasks (stretch 2, 4 fours) are good stretch. The 7-digit odd puzzle (challenge 8) is a strong-thinker puzzle: unique answer 6 953 487 confirmed by brute force.
- Q3 riddle and Q6 find-all are stretch-ish on Core page 1 and page 2; the matching slide examples (`we2`, `teachfind`) make them fair.
(c) Reading load: moderate; the 6-clue table is dense but clear.
(d) Numbers: all verified. Q3 = 7 253 609 unique; Q6 = six numbers; Q4 (a) 104 727 is exactly 4987 x 21 and (d) 318 370 is exactly 806 x 395, so the "could be right" labels are honest; challenge 7 max = 231 over all bracketings.
(e) Timing: page 1 needs about 20 minutes with the riddle, page 2 about 15; 12 and 7 are provided. Fix by issue 1; consider issue 15.
(f) Online: "Million Maker" needs the tutor to turn digit cards; on video use a slide deck or a random generator and say so in the notes. Paper digit cards and a drawn place-value mat must be prepared by the child beforehand (it is stated).

### L2 Fraction Feats (verdict: minor fix, one genuine defect)

(a) Egyptian-fraction splitting needs unlike-denominator subtraction (P4/P5 skill) and is an enrichment topic. Fraction / whole number is P6 (issue 5). Telescoping sum (challenge 7) is clearly beyond but flagged "challenge" with a hint.
(b) Difficulty: the 18 sub-parts on two pages make this the densest worksheet. Core is genuinely doable for Q1a-b, Q3, Q4a-b, Q5. Q2c (two ways for 3/8) and Q6 are Think-Harder-level. Think Harder items are well pitched (telescoping with the hint, 5/12 as two unit fractions).
(c) Reading: moderate; stacked fraction typography in the workbook helps.
(d) Numbers: all verified, including that 7/10, 9/20 and 3/8 have exactly 1, 1 and 2 splits. The stopping rule ("stop when the first part is less than half the fraction") is correct for distinct unit fractions and consistent in the key and slides.
(e) Timing: ws2 solo in 7 minutes with a drawn model (Q5) and digit-card tests (Q6) is not realistic.
(f) Online: paper circles and scissors on camera (6 per child) work, but are fiddly; allow drawing instead.
Real defect: issue 2.

### L3 Before and After (verdict: minor fix)

(a) In syllabus (fractions word problems and models), well within P5/P6 enrichment.
(b) Difficulty: Q1 to Q4 are Core-appropriate with good scaffolds. Q5 is Think Harder (issue 6). Think Harder items span moderate to hard; the printed challenge 7 (Mei $200 and Siti $80) is a classic "same difference" problem and good for strong thinkers.
(c) Reading load: low to moderate; scenarios are named and short.
(d) Numbers: all verified (every one of about 35 items). Q2b Siti 48 / Mei 36; Q4b $22; Q5 70 and 100; slide challenge $48 and 6 years.
(e) Timing: acceptable on page 1; page 2 has two long problems in 7 minutes.
(f) Online: the explore says "camera pointing down at the desk" while counters move; children cannot see the shared slide at the same time unless they have a second device. Proposed text for `lesson.online`: `Children move 18 + 6 paper squares on the desk with the camera up as usual and hold the table up to the camera; or use the interactive version on the slide.` (also applies to L4 where children cut and fit paper pieces.)

### L4 Triangle Areas (verdict: OK)

(a) Entirely P5 (base, height, height outside, composite figures). "Same base, same height" is a standard extension.
(b) Difficulty well pitched: Core is truly easy (Q1, Q2, Q5), Q3 and Q4 are a genuine step up with a fully parallel worked example. Think Harder reasonable.
(c) Reading load: low. Cleanest lesson.
(d) Numbers: verified from the figure coordinates (Q1 triangles 24, 84, 36; Q3 56; Q4 96, 16, 16, 24, 40; the slide's 5-12-13 and 11-12 with sides 13 and 20 are geometrically consistent). Challenge 4 (the square plus extended side) and challenge 8 (two squares: always half the big square) verified.
(e) Timing: page 2 is the only worry.
(f) Online: cutting out pieces is the activity; as for L3, camera position. Printed Think Harder gives no figure for challenge 7/8/9 (issue 12).

### L5 Volume Vault (verdict: minor fix)

(a) Cuboid volume, tank volume, ml and cm3: P5. Rise of water = volume / base area is the inverse and reasonably beyond (the missing-edge type is listed at P6). Painted cubes and "3 faces" are standard enrichment.
(b) Difficulty: Q1, Q3a-b, Q4a-c, Q6a-b Core; Q2 (36 cubes, 8 cuboids) is a Core-plus listing task; Q5 painted cubes with a taught 5 x 5 x 5 example is fine. Challenge 7 (three face areas to volume) is elegant but hard.
(c) Reading: moderate; page 2 is heavy with figures.
(d) Numbers: all verified, including the list of 8 cuboids for 36 and the single fit in a 5 x 5 x 5 box (3 x 3 x 4), 64 cubes giving 7 cuboids, 3 x 4 x 5 painted counts (24 two-face, 22 one-face), tank 1/3 to 3/5 giving 45 l, the upright block giving 12 cm. Q1(b) is a judgement call (issue 11).
(e) Timing and layout: issues 3 and 11.
(f) Online: the live water-rise demo needs a clear box and a stone and works well on camera; it must be set up beforehand (listed under materials).

### L6 Rate Racers (verdict: minor fix)

(a) Rate: P5. "Taps together", "leak", and "price plans" are natural extensions; "work problems" from two times (talk, challenge 1, 9) are beyond (issue 9). Dividing by a decimal (issue 8).
(b) Difficulty: Q1, Q3, Q5, Q6 are Core; Q4(b) (staggered start) and Q2(c) are Think-Harder (issue 7). Printed Think Harder (cats, candles, bath-with-plug-out) is good strong-thinker material; "3 cats 3 fish 3 minutes" is a famous trap with a clean answer (3).
(c) Reading: moderate, with decimal money and time-of-day arithmetic across noon (9.40 a.m. to 1.15 p.m.).
(d) Numbers: all verified (car-park charges with "or part of": 3 h 35 min = $4.80; $3.60 = at most 3 h; gyms equal at 10 visits; shops 70, 73, 65 cents; $13.64; printers 18, 20, 540 pages). Unambiguous.
(e) Timing and layout: issues 1 and 3.
(f) Online: the phone-stopwatch brain break is fine.

### L7 Percentage Puzzles (verdict: needs rework)

(a) Percentage of a quantity, discount, GST, remainder: P5. Percentage change and finding the whole: P6 (issue 4).
(b) Difficulty: Q1, Q2, Q4 Core and good. Q3, Q5, Q6, Q7 are all a step up. Think Harder items 5 and 7 need reverse percentages.
(c) Reading: the heaviest wording after L2: Q2 (rice cooker with two shops), Q6 and Q7 each have four to five sentences of set-up.
(d) Numbers: all verified (Q1 $24, $12, $2.40, $36, $84, $237.60; Q2 $128, $11.52, $139.52, Shop A cheaper by 48 cents; Q4 60% left; Q6 14 of 40 = 35%; Q7 $45 against $42; qbank items including 25.5% bus riders and Shop P cheaper by $1.20). GST at 9% is current (2024 onward). No wrong answers.
(e) Timing: worst in the programme (issue 4 and 1).
(f) Online: calculators "closed until check slides" is a good rule; children may need a way to show percentages as bars: use the annotation tool as planned.

### L8 Angle Chasers (verdict: minor fix)

(a) Straight line, point, vertically opposite, triangle, isosceles, equilateral, parallelogram, rhombus, trapezium: P5 (and P6 chains). The facts used stay inside the syllabus; no alternate or corresponding angle language, which is correct. Clock angles (stretch) use reflex angles briefly.
(b) Difficulty: Q1 and Q2 Core; Q3 and Q4 chains with isosceles triangles are Core-plus because each needs four steps with reasons; Q5 (every case) is a good thinking item. Challenge 7 and 8 are classic hard angle chases; unique answers 30 and 150.
(c) Reading: low; vocabulary heavy but taught (`teach1` card set).
(d) Numbers: all verified, including that every figure's labelled angles are consistent (Q3: BAD 56, DAC 38 so BAC 94 and ACD 24; Q4: DAB 124 less DAE 62 gives EAB 62; trapezium D 70, C 100; rhombus QPR 32).
(e) Timing and writing load: issue 10.
(f) Online: tearing corners off a paper triangle on camera is a good concrete start. Figures are small on the printed page; children need their own print or a clearly shared slide.

### L9 Pattern Generalisers (verdict: OK)

(a) Number patterns with a rule in words, supposition, guess and check: P5 heuristics. No algebra letters (the notes use "n", issue 17).
(b) Difficulty: very well pitched; Core is accessible and the slide examples are tightly parallel. Think Harder items (beads, 40 tables, diamond dots, 100th digit) fine for strong thinkers.
(c) Reading: lowest in the programme.
(d) Numbers: all verified (chairs 2n + 2; houses 5n + 1 with 199 / 5 = 39 r 4; $12/$7 tickets 8 and 7; coins 14 and 16; quiz 15 correct, 80 impossible because 20 is not a multiple of 7; bonus items 435 handshakes, 342 page digits, 61 diamond dots, 5 as the 100th digit).
(e) Timing: page 2 (table, supposition twice) in 7 minutes is the only concern.
(f) Online: 40 matchsticks per child (issue 19).

### L10 Challenge Day (verdict: minor fix)

(a) No new topic; mixed P5 content with heuristics. Fine.
(b) Difficulty: Q1 (backwards with a fraction) and Q4 (count squares by size) Core; Q2 (4 x 4 logic grid) and Q5 (liars) are Core-plus; Q3 and Q6 need the model/age-gap idea and are well supported by `we3` and `teachage`. Think Harder set is varied and fair.
(c) Reading: moderate; Q5 stem is 45 words.
(d) Numbers: all verified (Q1 $63; Q3 Mei $60, Ravi $55; 3 x 4 grid 20 squares; Ben broke the vase, unique; ages 7 years; qbank bus 27, monkey 14, 25 coins 3/6/16 unique, chairs Siti-Mei-Ali-Ben unique). Only the gender assumption in Q2 (issue 13).
(e) Timing: certificates at 88 to 90 are fine; page 2 (three puzzles with working) in 7 minutes is a stretch (issue 1).
(f) Online: breakout rooms with puzzle cards need the cards sent as images or put on separate slides (issue 14).

## Cross-cutting online-delivery risks (apply to several lessons)

**A. Whiteboards held to camera in a group of 8.** Gallery tiles are too small to read; a child's answer is readable only when they are spotlighted. Tell the tutor to say "show me, one at a time" or ask children to use the platform's whiteboard or chat for short numeric answers. Fractions and angles are hard to type; pen-and-paper plus spotlight is right, but it needs a rule in the guide.
**B. Breakout rooms for pairs (page 1 and the explore).** With 8 children that is four rooms and one tutor, so each room gets about 3 minutes of tutor time in 12. Either run page 1 in pairs without breakout (children share one screen thread) or have a co-tutor for the larger groups. State this in `P5_Holiday_Program_Guide.docx` and the tutor guide.
**C. Printed workbook needed.** All worksheet figures live only on the printed A4 pages. The `ws1` / `ws2` slides are previews. A child without a printer cannot see Q1 of L4 or Q3 of L8. Add a parent instruction: `Please print the workbook pages before the lesson`, or put the figures on the slides.
**D. Camera pointing down.** L3 and L4 explore ask for this; the child then cannot watch the shared screen. Use a second device or keep the camera forward and show finished work.
**E. Pre-lesson preparation** (digit cards L1, six paper circles L2, 24 counters L3, grid paper and scissors L4, cubes L5, matchsticks L9). A single parent letter with the list per lesson would reduce lost minutes at the start of each session.

## Items judged fine (no change needed)

- Tone, slogan and Singapore context are consistent and age-appropriate (names, hawker centres, $ and cents, GST at 9%).
- Teaching slides generally give a parallel, not identical, example (L1 `teachfind` uses 5000 and digit sum 6 against the workbook's 2 500 000 and 9; L4 `teachtake` uses 10 x 6 against 12 x 8; L5 `teachpour` uses 20 x 10 x 24 against 30 x 20 x 24; L9 `teachgs/teachsup/teachmarks` use different numbers). L2 `teachpattern` is the exception (issue 2).
- No ratio notation, speed, circles, pie charts, negative numbers or algebra letters appear in any child-facing text. (Tutor notes: issues 6 and 17.)
- Every logic puzzle checked has exactly one solution (L1 Q3, L10 Q2, Q5, qbank chairs and coins, slide warm-ups).
- Every "find all" key lists every case (L1 Q6, L2 Q2c, L5 Q2, L8 Q5).
