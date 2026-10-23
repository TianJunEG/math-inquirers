# Level 1 term-time year plan (Primary 1, ages 6-8)

> **Update, 23 Oct 2026 (night), owner decision TERM-ALL-RECOMMENDED (`docs/terms/owner_decisions.md`):** lesson 10 of each term (lessons 10, 20, 30 and 40) is the **choose-the-tool consolidation + Challenge Quest lesson**. Lessons are **not renumbered**: lesson 10 stays lesson 10. Any new idea that this plan places in a lesson 10 moves to an earlier slot when the lesson is built. Tables below are not yet edited. Plan and effort: `docs/pedagogy/lesson_x10_consolidation_plan.md`. Level 1 specifics: Terms 2 to 4 first, Term 1 later. Proposed (not applied): Picture Equations 19 to 13 (Doubles and Near Doubles retired), Find One First 20 to 19, Calendar Detective 30 to 27 (Fill the Grid retired); lessons 20 and 30 become new choose-the-tool lessons; lesson 40 keeps the Showcase. Lesson 10 (Story Steps) stays in place for now (plan option B).

## Revision for 10-week terms and new Term 1 (22 Oct 2026)

Reworked to match `docs/terms/owner_decisions.md`. What changed:

- **40 lessons, not 36.** 4 terms x 10 lessons (a term is about 10 weeks). Lesson numbers are now 1-40 (T1 = 1-10, T2 = 11-20, T3 = 21-30, T4 = 31-40); the old 1-36 numbers are gone, and every lesson reference below uses the new numbers. Exactly one lesson was added per term (the 10th lesson, marked "added" in the tables).
- **Term 1 is all new content.** Holiday graduates start Term 1, so Term 1 no longer adapts the holiday course (it used 9 of 10 holiday lessons). The holiday course (`hp/lessons.js`) stays a standalone foundation course. Nothing is reused; holiday topics come back only as the first 6-minute warm-up (section 3). All 40 lessons are new; none is a holiday lesson.
- **Order.** Number and arithmetic strands first (place value, adding and subtracting within 100, ordinals, length), because a child coming from the holiday course has patterns, bonds, money coins, shapes, length in cubes and graphs but no place value, no 2-digit arithmetic, no multiplication, no time. Old Term 2 lessons moved up into Term 1 (Bundles and Singles, Digit Cards, 100 Square, Make-a-Ten, Take Away, Balance and Swap), old Draw and Measure (was 32) moved to Lesson 9, and the old Term 2 to 4 lessons shifted to fit; nine new-topic lessons (2, 6, 13, 22, 25, 27, 28, 29, 37) replace the nine holiday slots.
- **Contest-style items now at Think harder, not only Go further.** Moved: digit-card clue puzzles (3), changing-step sequences (4), queue counting "8th from the front and back" (11), numbers in two tables (16), make-equal transfers (12), "twice as many" with a transfer (18), routes on a grid (33), spending exactly $20 (26), fold and punch (34), day-of-week cycles (24, 30), Latin squares (27). None is Start here.
- **Mid-year joiners.** Each term has a "can a new child join cold?" line and a safest-to-skip lesson (section 2). No lesson assumes the previous term except through the warm-up.
- **Added 10th lessons (the best remaining gaps):** Lesson 10 Story Steps (multi-step stories, reading traps: books gaps 1 and 2); Lesson 20 Find One First (price or size of one: books gap 3); Lesson 30 Calendar Detective (SASMO time and calendar gap); Lesson 35 Spot It (SASMO visual perception gap).
- **Not changed:** KIV items belong to other levels (Level 5 lessons 28/29 merge, lesson 32 too full, secondary speed preview in lesson 15; Level 3 lessons 22/23 figures); none applies here. No speed work in this primary level.
- **Non-routine work in every lesson (23 Oct 2026, owner decision).** New section 8 at the end lists, for each of the 40 lessons, the non-routine question types from the school-paper analysis (type, Think harder or Go further, written or new) with original catalogue items, plus a type-by-lesson matrix. Lessons 1 to 20 are unchanged; Lessons 21 to 40 carry the new assignments (`docs/terms/l1_term3_term4_preflight.md`, section 13).
- Section 3, 4, 5, 6 and 7 were rewritten for these changes (reuse section, coverage matrix, 10-question checks, effort, open questions).

## Verified against MOE syllabus (Oct 2025)

Lesson numbers below are the new 1-40 numbers (the old 1-36 numbering is retired). Checked against the official PDF (`docs/moe/syllabus_by_level.md`; page numbers are PDF pages). No [check] or [UNVERIFIED] flags were open in this plan, and every P1 strand and beyond-P1 label below was confirmed. Changes made: (1) lesson 16 (was 20), "contest tables 6 to 8 are beyond P1" now says tables of 6 to 9 are P3 (p. 35) while P1 multiplication is within 40 (p. 31); (2) lesson 16 (was 1), common multiples are P4 (p. 37); (3) lessons 8 and 19 (were 2 and 27), letters for unknowns are P6 (p. 43); (4) page references added to the odd/even (P2, p. 33; lesson 14), shape-pattern (P2, p. 34; lesson 28), 3-D shape (P2, p. 34; lesson 34) and fraction (P2, p. 33; lesson 31) labels. Syllabus items the plan touches only lightly: comparing the number of objects in two sets (P1 Whole Numbers 1.4, p. 31; lesson 3) and mental calculation of a 2-digit number plus ones or tens without renaming (2.7; lessons 5 to 7). Nothing in the plan was wrong; the rework below changes lesson numbers and content but no verified placement (new lessons are labelled for review; see the flags in the tables). Source of the verified outcomes: `docs/audit/moe_alignment_p1_p3.md`, section "Verified against MOE syllabus".

Status: plan only, no lessons written. 4 terms x 10 lessons x 90 minutes = 40 lessons, live online, groups of 8 or fewer. A school term is about 10 weeks, so each week has a lesson; the 20-minute end-of-term check is taken inside Lesson 10 of the term (the last 20 minutes, or the make-up slot), not in an extra week. No dates are fixed here.

Sources used: README.md; hp/lessons.js (the 10 holiday lessons; the brief's p1/ folder holds only build scripts); hp/budget.json; docs/levels_and_placement.md; docs/audit/audit_p1.md; docs/audit/moe_alignment_p1_p3.md (the P1 syllabus outcomes and our gaps, read from the 2021 MOE syllabus there); docs/audit/intl_mapping_*.md; docs/gifted_research.md; docs/sasmo/g1_analysis.md; docs/books/word_problems_g1_g2_analysis.md; docs/terms/owner_decisions.md. No p1/SPEC.md, p1/data.js or p1/content/ exists, so the holiday content was read from hp/lessons.js.

Tier labels used throughout: **S** = Start here (core, approachable, not yet taught at school), **T** = Think harder (an idea already taught, in a new setting), **G** = Go further (mastery plus extension). Labels stay neutral; nothing here is a result, a rank or a prediction for any child.

## 1. Design principles

- **The year arcs Notice it, Test it, Explain why, then Choose and create.** Term 1 notices how numbers work (tens and ones, patterns in the 100 square, adding and taking away within 100, measuring and drawing). Term 2 turns stories and groups into bar strips, multiplication and sharing and starts testing claims. Term 3 asks for reasons and generalising (always, sometimes, never). Term 4 asks the child to pick a tool and to write problems for others.
- **Three threads spiral through all four terms, each time in a bigger setting:** (a) rules and patterns (100 square, then times tables, then a table for a growing pattern, then grid paths); (b) balance and "=" (balance and swap, then picture equations, then spot the mistake, then the toolbox); (c) listing every case (digit cards, sharing and grouping, spending exactly an amount, counting routes). Each revisit is labelled "spiral" in the table and is a new context, not a repeat worksheet.
- **Any term can be a first term.** Places open every term (prorated fee). Lessons 2 to 40 open with a 6-minute "remember" warm-up that carries what the lesson needs, so a child who joins cold is not lost and no lesson assumes the previous term except through that warm-up. Term 1 assumes only the holiday course or counting to 20; holiday topics appear only in warm-ups (section 3). Terms are not lockstep with school.
- **Problem solving is taught as a few named moves, one new move a term:** Term 1 draw it, list it, one operation per step; Term 2 bar strips, find one first, work backwards; Term 3 make a table, use cases, spot the mistake; Term 4 choose the move and create a problem. Moves are named in children's words and recorded on a growing "Inquirer's toolbox" page. **Update, 23 Oct 2026 (TERM-YES data fix): the separate growing "Inquirer's toolbox page" is no longer promised.** The toolbox is now delivered by the spine routine adopted by the owner on 23 Oct 2026 (`docs/pedagogy/spine_routine_spec.md`): eight named strategies (spot the pattern, list every way, draw it, make a table, work backwards, guess and check, try something simpler, act it out), a strategy card ("tool of the day") in every lesson, and one common look-back at the end of every lesson; and by the printed Toolbox Card in the Inquirer Kit (`docs/pedagogy/toolbox_card_notes.md`). The spine is built for the holiday program (decks, workbooks, tutor guides) and the Toolbox Card exists; the term lessons are not yet changed, so the term authors carry the same eight names, the strategy card and the common look-back into the Level 1 term lessons instead of writing a toolbox page. Lesson 39 (The Problem-Solving Toolbox) is where the child chooses among the eight.
- **Syllabus first for Start here, contest-type moves at Think harder, a harder follow-up at Go further.** Primary 1 strands that the holiday course never touched (tens and ones, adding within 100, times and sharing, telling time, half and quarter) are taught here as core. Contest-style items (digit-card puzzles, gaps and posts in queues, changing-step sequences, handshakes and pairing, routes, Latin squares, day-of-week cycles) are marked in the table, are never Start here, and are not only Go further (owner decision 6).
- **Every lesson has a talk-and-explain minute and a private paper.** Children explain a reason aloud each lesson. Any paper or end-of-term check is returned privately; no child's score is shown to the group, no ranking, and parents hear progress words, not marks versus other children.

## 2. Term-by-term lessons

Skill column is the key thinking skill. "MOE" names the Primary 1 strand (Whole Numbers, Addition and Subtraction, Multiplication and Division, Money, Length, Time, 2D Shapes, Picture Graphs). "Beyond" marks content past Primary 1; "SASMO-type" marks contest-style moves (these sit at Think harder). Lessons marked **(added)** are the 10th lesson of the term. Lessons marked **(new topic)** replace a holiday lesson slot and are drafted here for tutor review; the syllabus label is the plan's best reading and is flagged where unsure.

Per term, two notes the owner asked for: **Can a new child join cold?** and **Safest lesson to skip or make up** (every lesson is recorded; a make-up can be a holiday class if there is a seat).

### Term 1: Notice it (numbers to 100 and how they work; all new)

**Can a new child join cold?** Yes. The 6-minute warm-up counts in 2s, 5s and 10s to 100 and revisits number bonds for 10 and 20 (holiday topics, spiral only); nothing else is assumed beyond counting to 20. **Safest to skip or make up:** Lesson 4 (The 100 Square Explorer), a pattern lesson that no later lesson depends on; Lessons 1 and 5 to 7 are the hardest to miss.

| # | Title | Big idea | Topics and strands | Start here / Think harder / Go further | Skill |
|---|---|---|---|---|---|
| 1 | Bundles and Singles | A number is tens and ones | MOE Whole Numbers (place value, read and write numerals). Holiday course has no place value. SASMO-type: split into tens and ones | S: build 2-digit numbers with bundles of 10. T: 5 tens 14 ones = ? G: who has most, 6 tens 14 ones or 85 ones? | Structure of numbers |
| 2 | Number Words and the Number Line (new topic) | Every number has a place and a name | MOE Whole Numbers (number words, counting to 100, before/between/after, nearest ten is placed here as a flag: check against the syllabus before building). Spelling load kept small | S: say, read and write numbers to 100 on a line; one before, one after. T: which ten is nearer; numbers between two marks. G: a line with the marks missing | Representing on a scale |
| 3 | Digit Cards | Order of digits changes the number | MOE Whole Numbers (compare and order, comparing sets of objects, 1.4). SASMO-type digit-card puzzles at T; 3-digit numbers are beyond P1 and only at G | S: make and order 2-digit numbers; compare two sets of objects. T: smallest and largest from three cards; find every number fitting two clues. G: three-card clues and a number that fits all | Systematic cases |
| 4 | The 100 Square Explorer | Patterns live in rows and columns | MOE Whole Numbers (patterns, counting to 100). SASMO-type changing-step sequences at T. Revisits the holiday "frog" only as warm-up | S: colour 10s, 2s, 5s and say what you see. T: down one row adds 10; a sequence where the gap grows (+1, +2, +3). G: sum of the two numbers before; two rules interleaved | Pattern generalising |
| 5 | Make-a-Ten Adding | Make tens first | MOE Addition and Subtraction (more than two 1-digit numbers; within 100; algorithm only after the mental method). SASMO-type: add by making tens | S: 8 + 6, then 28 + 6 by making ten. T: add four numbers by finding tens. G: 18 + 7 + 12 + 23 + 3 + 17 | Strategy choice |
| 6 | Tens Jump, Ones Hop (new topic) | Add and take away tens without carrying | MOE Addition and Subtraction (mental 2-digit plus or minus ones or tens without renaming, 2.7). Number line jumps | S: 34 + 10, 34 + 20, 34 - 10. T: 34 + 25 by a tens jump then ones hops. G: how many jumps from 7 to 97, and the shortest way | Chunking |
| 7 | Take Away, Count Up | Difference is a gap | MOE Addition and Subtraction (subtraction within 100, relation to addition) | S: take away 10s and 1s. T: count up to find the difference. G: which is quicker, and why? | Choosing a method |
| 8 | Balance and Swap | Adjust one side, adjust the other | MOE Addition and Subtraction ("=" as balance). Beyond P1: compensation (38 + 25 = 36 + 27); SASMO-type at T. Letters for unknowns are P6 (p. 43), so boxes only. Warm-up revisits holiday bonds | S: box numbers, 27 + 16 = box + 9. T: spot equal sums without adding; compensation. G: a chain of equal sums with two boxes | Reasoning about equality |
| 9 | Draw and Measure | Be exact to the nearest centimetre | MOE Length (draw a line, measure to nearest cm, compare). Deeper than the holiday cubes-and-ruler measuring, which is warm-up only | S: draw 7 cm; compare two drawn lines. T: lines on a bent path; a line that starts at 2 on the ruler. G: three pieces of a 30 cm ribbon | Precision |
| 10 | Story Steps: Read It Twice (added) | One operation per step | MOE Addition and Subtraction (in context, within 100). Gap from `docs/books/word_problems_g1_g2_analysis.md`: multi-step stories (31 of 101) and reading traps (who is in the group, "fewer than"). Bar strips come in Lesson 12 | S: two-step story, write one operation per step. T: reversed wording ("3 fewer than"); a story with a trap (who is in the group). G: three-step story, write it for a partner | Reading and planning |

### Term 2: Test it (stories, groups and claims; all new)

**Can a new child join cold?** Yes. The 6-minute warm-up draws 3 tens and 4 ones, adds by making a ten, and skip-counts 2s, 5s, 10s to build a group picture. Lessons 11 to 20 use only that. **Safest to skip or make up:** Lesson 14 (Odd + Odd), a standalone inquiry; avoid skipping Lessons 15 to 18, which build on one another.

| # | Title | Big idea | Topics and strands | Start here / Think harder / Go further | Skill |
|---|---|---|---|---|---|
| 11 | Who Is Where? | First, second, third... in a line | MOE Whole Numbers (ordinals 1st to 10th, symbols). Position words. SASMO-type queue counting ("8th from the front and the back", a gaps-and-posts idea) at T | S: ordinals and ordering by clue. T: 8th from front and back; how many in the line. G: seats around a table, clues | Deduction |
| 12 | Bar Strips: More and Fewer | A strip shows the story | MOE Addition and Subtraction (in context). Bar models are not named in the 2021 syllabus; school practice uses them. SASMO-type: transfer and compare, now at T (books treat make-equal as ordinary) | S: two groups, how many more. T: total and difference given; make equal by a transfer. G: transfers with a total | Representing |
| 13 | Doubles and Near Doubles (new topic) | Double, then adjust | MOE Addition and Subtraction (doubles, within 20 and 100, a mental strategy). Links to pairing and to the 2 table | S: doubles to 10 + 10; double a tens number. T: near doubles (7 + 8); doubles to find 6 + 6 + 1. G: a sum of five numbers that are almost the same | Strategy choice |
| 14 | Odd + Odd: Always, Sometimes, Never? | One test is not a proof | MOE Whole Numbers (odd/even is P2 content, Whole Numbers 1.6, p. 33; flagged). Inquiry lesson, sets up Term 3 reasons | S: pair counters to sort odd/even. T: what is odd + even? G: explain why odd + odd is always even | Conjecture and test |
| 15 | Equal Groups | Same-size groups, count fast | MOE Multiplication and Division (concept, x sign, within 40). Holiday course has none | S: 4 groups of 3, repeated addition. T: array, 3 x 4 = 4 x 3? G: legs and wheels | Representing multiplication |
| 16 | Skip-Count Tables | Tables are skip counts | MOE Multiplication and Division (2, 5, 10, then 3, 4). Tables of 6 to 9 are P3 (p. 35); P1 stops at within 40 (p. 31). Common multiples are P4 (p. 37) and sit at T as SASMO-type | S: build the 2, 5, 10 tables. T: use 2s to find 4s; which numbers appear in two tables? G: numbers in three tables | Patterns to facts |
| 17 | Sharing and Grouping | Two kinds of division | MOE Multiplication and Division (within 20, sharing and grouping). Remainder language is P3; use "left over" | S: share 12 among 3. T: how many groups of 4 in 14? G: all ways to share 12 equally | Two models of one operation |
| 18 | Times Stories | Draw the story, then solve | MOE Multiplication and Division (word problems). Bar-model "times as many" is SASMO-type, beyond P1, now at T | S: story with 3 groups of 5. T: two-step with a total; "twice as many as" with a transfer. G: three groups with different sizes and a hidden start | Representing (bar strips) |
| 19 | Picture Equations | A shape is a hidden number | Beyond P1 (letters/algebra is P6, p. 43); SASMO-type substitution; uses times and add facts | S: one shape and a box, 4 + shape = 10. T: two different shapes; take one equation from another. G: three symbols with a times sign | Reasoning about equality |
| 20 | Find One First (added) | Find one, then find many | MOE Multiplication and Division (word problems) and Money. Gap from the books analysis: price or size of one from a group (6 of 101); also vocabulary "a dozen", "each", "such" | S: 4 pens cost 20 dollars, one costs? T: price of 7 from the price of 3. G: two-step, price of one then change | Unit method |

### Term 3: Explain why (time, money, tables and reasons; all new)

**Can a new child join cold?** Yes. The 6-minute warm-up skip-counts in 5s (clock face), lists the coins 5, 10, 20, 50 cents and $1 (holiday coin topic, spiral only) and draws a bar strip for "8 and 3". Lessons 21 to 30 need only that. **Safest to skip or make up:** Lesson 27 (Fill the Grid), a standalone puzzle lesson; Lessons 21 to 23 and 24 to 26 are two chained blocks.

| # | Title | Big idea | Topics and strands | Start here / Think harder / Go further | Skill |
|---|---|---|---|---|---|
| 21 | What Time Is It? | The clock counts in 5s | MOE Time (o'clock, half past, quarter past/to). Never touched in the holiday course | S: o'clock and half past. T: quarter past/to. G: a mirror clock | Reading a scale |
| 22 | Five Minutes at a Time (new topic) | Minutes live between the hours | MOE Time (to 5 minutes, am/pm, h/min). Split from the old What Time lesson so time gets two full lessons | S: 5-minute marks on the clock. T: am or pm for daily events; hours and minutes. G: how many minutes from 3:10 to 4:05, by chunks | Reading a scale |
| 23 | Time Passes | Time can be added | MOE Time (durations of 1 hour or half hour) | S: one-hour and half-hour durations. T: finish times. G: a duration that crosses noon | Chunking |
| 24 | Dollars and Change | Notes and coins make a dollar | MOE Money (dollars to $100, change). Warm-up revisits coin combos only | S: count notes and coins to $20. T: pay for two items. G: fewest notes for $73 | Money sense |
| 25 | Price Tags: Compare and Choose (new topic) | Which costs more, and by how much | MOE Money (compare prices, add and subtract money to $100; money stories are 23 of 101 book problems) | S: which is cheaper, by how much. T: three prices, a total and a difference. G: buy two things, change left over | Comparing |
| 26 | The School Shop | A plan within a budget | MOE Money applied. Inquiry: spend exactly $20. Listing all the ways is SASMO-type, now T | S: choose two items for $10. T: three items, change; list all ways to spend exactly $20. G: all ways with three prices | Planning with constraints |
| 27 | Fill the Grid (new topic) | Each row and column has one of each | SASMO-type constraint grids (3 of 100). Not in MOE P1. Label for review | S: complete a grid with one missing cell per row. T: 3 by 3 Latin square with clues. G: 4 by 4 with digit clues | Elimination |
| 28 | Make a Table (new topic) | A table finds the 20th | Growing patterns (not named in any year; shape patterns are P2, p. 34). Move: make a table. Revisits holiday growing sticks only in the warm-up | S: fill a table for a growing stick pattern. T: the 10th and 20th term from the table. G: work back from a total | Prediction from a rule |
| 29 | Spot the Mistake (new topic) | Check with a different method | Cross-strand reasoning: error analysis on adding, taking away, time and money. Not an MOE content item | S: find the mistake in a worked sum. T: say which step is wrong and why. G: write a wrong answer for a partner to catch | Checking and explaining |
| 30 | Calendar Detective (added) | Days and weeks go round | Time (days of the week, weeks; calendar vocabulary "a week", "a fortnight"). Gap: SASMO time and calendar (7 of 100). Day-of-week cycles are SASMO-type, at T | S: days of the week in order; what day is 3 days after? T: "two days after the day before yesterday"; the 10th day from Monday. G: which dates fall on the same weekday | Cycles (mod 7) |

### Term 4: Choose and create (space, shape, data, putting it together; all new)

**Can a new child join cold?** Yes. The 6-minute warm-up names rectangle, square, triangle and circle (holiday shapes, spiral only), reads a 1-to-1 picture graph and measures to the nearest cm. Lessons 31 to 40 need only that. **Safest to skip or make up:** Lesson 35 (Spot It), a standalone perception lesson; Lessons 39 and 40 draw on the whole year and should not be missed.

| # | Title | Big idea | Topics and strands | Start here / Think harder / Go further | Skill |
|---|---|---|---|---|---|
| 31 | Half and Quarter | Equal parts | MOE 2D Shapes (half circle, quarter circle). Fractions proper are P2 (p. 33), so only shapes, not 1/2 | S: fold a circle into halves and quarters. T: halves of a square, several ways. G: is every half the same shape? | Equal parts |
| 32 | Build the Figure | Make big shapes from small | MOE 2D Shapes (forming figures, identifying shapes in a figure). Deeper than the holiday shape naming (warm-up only) | S: build a house from 4 shapes. T: count every triangle. G: same figure, fewest pieces | Decomposing |
| 33 | Copy on the Grid | Grids help us describe | MOE 2D Shapes (copy figures on dot or square grid). Position words; counting routes is SASMO-type, now T | S: copy a figure. T: directions: 2 right, 1 up; count the routes in a small grid. G: routes on a larger grid | Spatial description |
| 34 | Cubes and Views | The same thing, seen differently | Not in MOE P1 (3-D shapes are P2, p. 34). SASMO-type: cube stacks, mirror, fold and punch (fold once is T) | S: build from a picture. T: view from the top; fold once and punch. G: fold twice, punch one hole | Visualising |
| 35 | Spot It: Same, Different, Missing (added) | Compare one feature at a time | SASMO visual perception (8 of 100, Section A). Not an MOE item. Thin evidence and partly a practice effect (analysis says so); no promise of contest results | S: spot the differences between two pictures. T: odd one out, missing piece, shadows. G: build your own odd one out | Perception |
| 36 | Count Everything | Count with a system | Cross-strand: counting figures, ways and routes (SASMO-type) | S: count squares in 2 by 2. T: handshakes in a group of 4 (pairing); count ways. G: two-stage routes | Systematic listing |
| 37 | Make Your Own Graph (new topic) | Ask, sort, then picture it | MOE Picture Graphs (collect, sort and draw with 1 picture = 1; revisits the holiday graph only as warm-up). Tally marks not named: flagged | S: sort and draw a picture graph from a survey. T: choose the question. G: draw with 1 picture = 2 | Data collection |
| 38 | Graph Detectives | Scales save space | MOE Picture Graphs; scales of 2 and 3 are beyond P1 (P2). Critical reading | S: read a 1-to-1 graph. T: 1 picture = 2. G: design a survey, say what it can't show | Critical reading |
| 39 | The Problem-Solving Toolbox | Pick the tool | Mixed: draw, list, work backwards, bar strip, table, find one first. Uses the moves from Terms 1 to 3 | S: the tool is named. T: the tool is not named. G: two ways to solve one problem | Strategy choice |
| 40 | Inquirers' Showcase | Teach what you found | Year look-back; children write a puzzle for a new Level 1 child. The end-of-term check is taken in the last 20 minutes or the make-up slot | S: present a favourite. T: write a puzzle. G: write a puzzle with a rule and a proof | Communicating |

## 3. Reuse of the holiday lessons

**No reuse.** The holiday course (`hp/lessons.js`: Count with the Frog, Number Bond Inquiry, Let's Plan the Fruit Party, Pattern Inquiry, Mystery Number, Coin Combos, Shape Safari, Logic Lab, Measure It!, Challenge Day) is a standalone foundation course. A holiday graduate starts Term 1 (December course) or Term 3 (June) or Term 2 (March) and must never repeat a holiday lesson. No Term 1 lesson, and no lesson in Terms 2 to 4, is adapted from a holiday lesson. Where a Level 1 lesson sits in a strand the holiday course touched (length, shapes, graphs, money, patterns), it is a different topic or a clearly deeper treatment (Draw and Measure, Build the Figure, Make Your Own Graph, Dollars and Change, Make a Table).

Spiral review of holiday topics is allowed only as the first 6-minute warm-up. Holiday topics each term's warm-ups revisit:

- **Term 1:** skip counting in 2s, 5s, 10s (Frog) in Lesson 4; number bonds to 10 and 20 in Lessons 5 and 8; cube/ruler measuring in Lesson 9; "I think of a number" in Lesson 10.
- **Term 2:** skip counting (Frog) in Lesson 16; Logic Lab ordering in Lesson 11; Mystery Number "undo" in Lesson 12.
- **Term 3:** coin values (Coin Combos) in Lessons 24 to 26; growing stick patterns (Pattern Inquiry) in Lesson 28; Logic Lab grid in Lesson 27.
- **Term 4:** shape names (Shape Safari) in Lessons 31, 32, 36; picture graphs (Fruit Party) in Lessons 37, 38; cube/cm measuring in Lesson 35.

Audit fixes in `docs/audit/audit_p1.md` apply to the holiday course itself, not to this plan. Old Challenge Day is not reused; its role is taken by Lesson 39 and 40 and the end-of-term check.

## 4. Coverage check

Strand by term (X = taught as core; p = partial; s = spiral/revisit only). Strand names follow the 2021 MOE syllabus as summarised in docs/audit/moe_alignment_p1_p3.md.

| MOE Primary 1 strand | T1 | T2 | T3 | T4 | Note |
|---|---|---|---|---|---|
| Whole numbers: counting to 100, place value, words | X | s | | | Lessons 1, 2; the holiday gap (place value, words) is closed first |
| Whole numbers: compare/order, patterns | X | s | p | | Lessons 3, 4; patterns again in 16, 28 |
| Whole numbers: ordinals 1st to 10th | | X | | | Lesson 11 |
| Addition and subtraction within 20 and 100, algorithms | X | s | s | | Lessons 5 to 8; gap flag: school will practise the written layout and speed more than we do |
| Addition and subtraction in context (word problems) | p | X | s | s | Lessons 10, 12, 20 |
| Multiplication and division | | X | s | | Lessons 15 to 18, 20; gap in the holiday course, closed in T2 |
| Money | | | X | | Dollars to $100 in T3 (24 to 26); coins are holiday warm-up only |
| Length (cm) | X | | | s | Drawing to the nearest cm in Lesson 9; warm-up in T4 |
| Time | | | X | | Four lessons (21, 22, 23, 30); the holiday course never covered it |
| 2D shapes: rectangle, square, triangle, circle | s | | | X | Lessons 31, 32; Term 1 does not teach shapes |
| 2D shapes: half circle, quarter circle, copying on a grid | | | | X | Lessons 31, 33 |
| Picture graphs | | | | X | Lessons 37, 38; a child who joins in Term 4 needs only the warm-up |

Where school practice outpaces us: speed and accuracy in mental calculation within 100, written algorithms with regrouping, worded problems read independently (reading load), writing number words, assessment practice. We teach the ideas and some practice but do not drill; parents should be told. Primary 1 strands are covered across the year; whether each child is secure is not claimed. A child who joins in Term 3 or Term 4 misses the earlier strand lessons (prorated fee covers only the lessons remaining); recorded lessons are the catch-up.

SASMO-type problem moves worked in (from docs/sasmo/g1_analysis.md; no contest problem copied), each at Think harder and never Start here: digit-card puzzles and place value (Lessons 1, 3); making tens and compensation (5, 8); changing-step and sum-of-previous-two sequences (4); day-of-week cycles and clock chunks (23, 30); symbol equations and substitution (19); bar-model "times as many" and transfer (12, 18); counting ways, handshakes and routes (26, 33, 36); spatial moves and perception (34, 35); constraint grids (27); working backwards (10, 39). The analysis notes real gaps in place value, 2-digit mental arithmetic, changing sequences, visual perception, time and symbol equations; this plan addresses each as a core lesson or a Think harder item. Four papers is a small sample, so no claim of contest readiness; do not market Level 1 as SASMO preparation.

## Revision after SASMO review

Level 1 was written after the SASMO Grade 1 analysis and uses it inline; this block records where each gap now lives in the 1-40 numbering (the old 1-36 numbering is retired).

| SASMO gap (g1_analysis.md section 4) | Home now | Tier |
|---|---|---|
| 1 Place value and digit puzzles (14 of 100) | Lessons 1, 3 | S core, puzzles at T |
| 2 Two-digit mental arithmetic and multi-term sums (13) | Lessons 5, 6, 7, 8, 13 | S core, long sums at G |
| 3 Changing-step sequences (10) | Lesson 4 | T and G |
| 4 Visual perception and 3-D (14) | Lessons 34, 35 | T; S for easy spot-the-difference only |
| 5 Time and calendar (7) | Lessons 21, 22, 23, 30 | S/T |
| 6 Symbol equations and multiplication facts (about 11) | Lessons 15, 16, 19 | S/T |

Books-analysis gaps (docs/books/word_problems_g1_g2_analysis.md): multi-step stories and reading traps in Lesson 10; price or size of one in Lesson 20; vocabulary (week, dozen, such) in Lessons 20 and 30; speed and accuracy of 2-digit regrouping is left to school. Gap left: reading-load for worded problems read independently; no lesson trains silent reading speed.

## 5. Assessment and progress

**Mi's Challenge Quest (replaces the earlier 10-question end-of-term check; owner decision, 22 Oct 2026, `docs/terms/owner_decisions.md`, section "end-of-term check becomes Mi's Challenge Quest").** Lesson 10 of each term keeps a 20-minute slot after the break (and the same slot in lessons 20, 30 and 40), but it is a game, not a test. Eight short gates, each tied to a lesson of the term and written at Start here level (never a contest move, never a repeat of that lesson's own items), and one optional cave. Children work in pairs or as a group quest with Mi, each writing their own answers on private paper. No scores or marks are shown to the child, no ranking, no visible timer, no strand profile or mark out of ten, and the words "test" and "exam" appear on no child or parent page. The tutor keeps private notes only; they feed the one-line parent report and next-term group advice. Photos of the Quest Log are returned by the parent to the business WhatsApp (+65 9880 5962, never printed on a slide). A child who joined late or missed a lesson simply skips the gate of that lesson. Gates are tagged by lesson (`term/l1/tools/b_quest.py` builds them from each lesson's `challenge_quest` block).

*Update, 23 Oct 2026 (TERM-YES data fix): other mentions in this plan of a 10-question or timed end-of-term check (header, term notes, effort table, open questions) are superseded by the Quest; the old check's per-lesson question lists are no longer an assessment, only a possible source of gate topics.*

**Gate topic starting points (from the superseded check, kept as history, one topic per lesson, and any S, T or G marks refer to the old check, not to gates, which are all Start here level; the authors of each Quest choose, recompute and tag the real gates):**

| Term | The 10 questions |
|---|---|
| 1 | Tens and ones; a number word or a number on a line; smallest from three cards; 100-square pattern or a growing-gap sequence; add by making ten; add or take away tens by jumps; subtract by counting up; a box number sentence or compensation; draw and measure to the nearest cm; a two-step story with one operation per step |
| 2 | An ordinal clue (8th from the front); a bar-strip story or a transfer; a double or near double; an odd/even claim and why; equal groups; a table fact; share 12 and group 14; a times story; a picture equation; price of one from a group |
| 3 | Time to the quarter hour; time to 5 minutes and am/pm; a duration; dollars and change; compare two prices; spend exactly $20; a small Latin square; a growing pattern table and the 20th term; find the mistake; a day-of-the-week clue |
| 4 | Half/quarter; shapes in a figure; copy on a grid or count routes; a view or fold and punch; spot the odd one out; count every way; make a picture graph; read a 1-to-2 graph; choose a tool; write a puzzle or explain a mistake |


**Parent report line per term** (what we saw, not a rank): T1 "Your child is learning to see numbers as tens and ones, to notice patterns and to say why." T2 "Your child is learning to draw a story, to use groups and sharing, and to test a claim with an example." T3 "Your child is learning to give a reason, and to read time and money in real life." T4 "Your child is learning to choose a method and write a problem for others." Add one named strength and one next step from the tutor. A mid-year joiner gets a report line only for the lessons attended. No claim of exam outcomes, GEP or SASMO results.

**Parent report lines: replace the generic `term_line` fields (note, 23 Oct 2026).** Every Level 1 lesson JSON carries the same boilerplate `term_line`. It is to be replaced by the parent outcome lines in `docs/pedagogy/term_parent_outcomes_draft.md` (Level 1 blocks). The lesson JSONs are not edited here; the replacement is a later change to `term/l1/lessons/`.

## 6. Work needed to turn the plan into the full set

Per lesson: tutor guide page, slide deck, workbook pages (A + D style) with key, question bank / Weekly Dose practice pages, and the end-of-term check. Existing build tools in hp/, deck/ and split/ are reused as tools; no holiday content is reused.

| Item | Scope | Rough effort (a guess, not measured) |
|---|---|---|
| Terms 1 to 4 | 40 new lessons, none adapted: guide, deck, workbook, practice | 3 to 4 hours each, 120 to 160 hours |
| Diagrams and kit (ten frames, hundred square, number lines, clocks, play money, grids, tens bundles) | New | 15 to 20 hours |
| End-of-term checks and report lines (4) | New, 10 questions each | 8 to 10 hours |
| Tutor review and a trial lesson per term, with extra review for the 9 "new topic" lessons and the flagged syllabus labels | Required | 12 to 16 hours |
| **Year total** | | about 155 to 205 hours, about 4 to 5 working weeks at best and 5 to 7 more comfortably for one full-time person; shorter only if drafted in parallel |

Build order: Term 1 first (it is the first lesson every holiday graduate meets), then the Term 3 time lessons and Term 2 multiplication (largest gaps), then Term 4.

## 7. Open questions for the owner

Answered and dropped (owner decisions of 22 Oct 2026): which term first and how holiday graduates enter (they follow the term calendar), mid-year entry (places open every term, prorated fee), closed cohort or open places, bridge from the holiday course (none: Term 1 is all new), a 5% discount for paying a term in full. KIV items for other levels (Level 5 lessons 28/29 merge, lesson 32 too full, secondary speed preview in lesson 15; Level 3 lessons 22/23 hand-drawn figures) do not touch this plan and stay open there.

1. What is the term price? (The website still says S$65 a lesson, S$650 for 10; 10 lessons per term now.)
2. Is there a placement check for a mid-year joiner, or just the warm-up and a tutor check in the first lesson?
3. May lessons 5 to 7 show the written vertical algorithm, or only mental and place-value methods?
4. Do we say "SASMO" to parents, or only "contest-style"? The analysis says do not market Level 1 as SASMO preparation.
5. Is the second-level age band (ages 7-8, who are in Primary 2) catered for, or is this plan aimed at Primary 1 only?
6. Homework: keep Weekly Dose practice or write a new term practice pack?
7. Who checks the lessons: a tutor trial per term, or the owner? The nine "new topic" lessons (2, 6, 13, 22, 25, 27, 28, 29, 37) and the four added lessons need a syllabus check first.
8. Is the order (numbers and arithmetic in Term 1, shapes and graphs not until Term 4) acceptable for a child whose school teaches shapes and graphs early? A child who joins in Term 4 relies on the warm-up.
9. Make-up slots: how many holiday-class seats can be offered in exam periods, and is the end-of-term check taken inside the 10th lesson or at a separate time?
10. Are the thin-evidence lessons 27 (Latin squares) and 35 (Spot It) worth a full lesson, or should they be an optional enrichment lesson that a tutor may swap for a synthesis lesson?

## 8. Non-routine work in every lesson (owner decision, 23 Oct 2026)

The owner asked that the non-routine question types found in the school papers sit inside the term plan. Source: `docs/books/p1_non_routine_catalogue.md` (text-free summary of 268 non-routine questions in 78 Primary 1 tests from 17 schools, 2018 to 2025; the questions themselves are in a private, gitignored file). **Every one of the 40 lessons now names its non-routine work: a heuristic or reasoning type, the tier where it sits (Think harder or Go further, never Start here), and original example items.**

How to read this section.

- Type codes (the 14 types in the catalogue): LOG logical reasoning; CMP comparison (difference or sum); BACK work backwards; CTX unfamiliar context or hidden fact; LIST systematic list or choose numbers; EXP explain, true or false, odd one out; GC guess and check; PAT pattern; DIAG draw a model; MULTI multi-step; TAB table; EQ make equal; WAYS how many ways; CHAL build from clues.
- **T** = Think harder, **G** = Go further. Status: **W** = already in the written lesson (Lessons 1 to 20; taken from each lesson's `contest_moves` in `term/l1/lessons/`); **F** = in the lesson file that exists now (Lessons 21 and 23; Term 3 writers are working on them); **N** = new assignment for a lesson not yet written. The Beyond (named) item in `docs/terms/l1_term3_term4_preflight.md` is the lesson's contest-style puzzle; the types below are the school-paper question types that sit alongside it.
- Catalogue items are original examples with scripted answers, written for this project. Authors write their own items of the same kind and checks; they never copy a school or contest question.
- Lessons 1 to 20 are built and audited and are **not edited here**. Where a type is thin in them, section 8.3 suggests a retrofit for the owner to decide.

### 8.1 Lesson by lesson

| # | Lesson | Non-routine types (tier, status): what | Catalogue items |
|---|---|---|---|
| 1 | Bundles and Singles | LOG (T, W): digit-clue puzzle: find the number from two clues; CTX (T, W): opening a bundle: 5 tens 14 ones | EX-LOG-3 |
| 2 | Number Words and the Number Line | LOG (G, W): clue puzzle using halfway; DIAG (G, W): two frogs hop towards each other | (the written lesson's own items) |
| 3 | Digit Cards | LIST (T, W): every number that fits two clues; list all cases; LOG (T, W): a number cannot start with 0 | EX-LOG-3, EX-LIST-1 |
| 4 | The 100 Square Explorer | PAT (T, W): changing-step sequence; sum of the two before; LIST (G, W): numbers in two lists (2s and 5s) | EX-PAT-2 |
| 5 | Make-a-Ten Adding | LIST (T, W): reorder to find pairs that make a ten | (the written lesson's own items) |
| 6 | Tens Jump, Ones Hop | GC (G, W): fewest jumps with two jump sizes; BACK (T, W): undo the jumps (light) | (the written lesson's own items) |
| 7 | Take Away, Count Up | CMP (T, W): difference as a gap; EXP (G, W): the gap stays the same when both numbers move | EX-BACK-1 |
| 8 | Balance and Swap | EQ (T, W): give and take between two addends; EXP (T, W): say two sums are equal without adding | EX-LIST-3 |
| 9 | Draw and Measure | DIAG (T, W): a bent path; a ribbon cut into pieces; CMP (T, W): a line that starts at a mark other than 0 | EX-DIAG-3 |
| 10 | Story Steps: Read It Twice | MULTI (T, W): two-step and three-step stories; CMP (T, W): reversed wording (fewer than, more than); CTX (T, W): reading trap: who is in the group | EX-BACK-1, EX-CMP-1, EX-MULTI-1 |
| 11 | Who Is Where? | LOG (T, W): seating and ordering clues; a line that faces the other way; DIAG (T, W): count both ends of a line (count the child once) | EX-LOG-1, EX-LOG-2, EX-DIAG-1 |
| 12 | Bar Strips: More and Fewer | CMP (T, W): sum and difference; a chain of three strips; EQ (T, W): make equal by a transfer; BACK (T, W): an unknown first quantity in a strip story (light) | EX-CMP-2, EX-CMP-3, EX-DIAG-2, EX-EQ-1, EX-EQ-2 |
| 13 | Doubles and Near Doubles | EQ (G, W): the middle number of several almost-equal numbers | EX-EQ-2 |
| 14 | Odd + Odd: Always, Sometimes, Never | EXP (T, W): always, sometimes, never: one failing test breaks a claim | EX-EXP-1 |
| 15 | Equal Groups | WAYS (G, W): list the ways to make equal groups of 24; EXP (T, W): turn an array: 2 x 8 = 8 x 2 | EX-EXP-2, EX-EXP-3, EX-WAYS-1 |
| 16 | Skip-Count Tables | LIST (T, W): numbers that are in two tables; PAT (T, W): the 4s are the 2s doubled | (the written lesson's own items) |
| 17 | Sharing and Grouping | CTX (T, W): who is in the group: shares with 3 cousins means 4 people; WAYS (G, W): every number of friends that can share 12 equally | EX-EXP-2, EX-MULTI-2, EX-WAYS-1 |
| 18 | Times Stories | DIAG (T, W): twice as many is two equal strips; EQ (T, W): a transfer after twice as many; MULTI (G, W): a total with a hidden unit; BACK (T, W): an unknown start in a strip story (light) | EX-EQ-3 |
| 19 | Picture Equations | CTX (T, W): a symbol stands for one number in every line; EXP (T, W): check the answer in every line | EX-CTX-1 |
| 20 | Find One First | MULTI (T, W): price of one first, then of many; CMP (G, W): compare the price of one in two shops | EX-CTX-2, EX-MULTI-3 |
| 21 | What Time Is It? | CTX (G, F): a clock seen in a mirror; the hour-hand trap at half past; LOG (G, F): which times look the same in a mirror | EX-CTX-4 |
| 22 | Five Minutes at a Time | CMP (G, N): minutes between two times by chunks; CTX (T, N): which show is on at a time between start times | EX-CMP-4, EX-CTX-5 |
| 23 | Time Passes | BACK (T, F): count back from the end to find the start; MULTI (G, F): a trip in two stages; CTX (T, N): read a timetable of start times | EX-BACK-3, EX-CTX-5 |
| 24 | Dollars and Change | GC (T, N): coins for an exact amount; the fewest coins; BACK (T, N): paid and change given: find the price | EX-BACK-2, EX-GC-1, EX-GC-3 |
| 25 | Price Tags: Compare and Choose | CMP (T, N): how much more; three prices, a total and a difference; GC (T, N): which two items cost exactly this much; LIST (T, N): choose numbers that add to a total; CHAL (G, N): find three prices from clues | EX-LIST-2, EX-GC-2 |
| 26 | The School Shop | WAYS (T, N): every way to spend exactly $20; LIST (T, N): list with a check that no case is missing | EX-LIST-2, EX-GC-2, EX-WAYS-2 |
| 27 | Fill the Grid | LOG (T, N): elimination in a 3 by 3 grid with clues | EX-LOG-4 |
| 28 | Make a Table | TAB (T, N): a ratio table and a table for a growing pattern; PAT (T, N): the 10th and 20th term of a growing pattern; BACK (G, N): work back from a total | EX-BACK-3, EX-PAT-1, EX-TAB-1, EX-TAB-2 |
| 29 | Spot the Mistake | EXP (T, N): find the wrong step and say why; CMP (T, N): catch a wrong "fewer than" sum; LIST (G, N): spot the wrong digit in a column sum | EX-CMP-1, EX-EXP-1 |
| 30 | Calendar Detective | CTX (T, N): a week has 7 days; a fortnight; PAT (G, N): day-of-the-week cycles; LOG (G, N): two days after the day before yesterday | EX-CTX-2, EX-CTX-3, EX-PAT-3 |
| 31 | Half and Quarter | DIAG (T, N): cut a shape into halves in several ways; LOG (G, N): guess the shape from its clues | EX-DIAG-3 |
| 32 | Build the Figure | TAB (T, N): count each shape in a figure into a table; DIAG (T, N): split a figure into its shapes with a ruler; LIST (G, N): which pieces make this figure | EX-TAB-3 |
| 33 | Copy on the Grid | WAYS (T, N): count the routes in a small grid; PAT (T, N): continue a path from its directions | EX-WAYS-4 |
| 34 | Cubes and Views | LOG (T, N): fold once, punch once; a view from the top; CTX (G, N): fold twice, punch once | EX-LOG-5 |
| 35 | Spot It | LOG (T, N): the odd one out; EXP (G, N): say which feature differs and why; PAT (T, N): a repeating pattern: which is the 11th | EX-LOG-2, EX-EXP-4, EX-PAT-3 |
| 36 | Count Everything | WAYS (T, N): outfits and handshakes; TAB (T, N): a table of pairs that make a total; LIST (T, N): list every pair without repeats | EX-TAB-2, EX-TAB-3, EX-WAYS-3 |
| 37 | Make Your Own Graph | TAB (T, N): tally and table before the graph; CHAL (G, N): build a graph from clues; BACK (T, N): find the missing bar from a total | EX-CHAL-1 |
| 38 | Graph Detectives | CMP (T, N): more and fewer from a graph; BACK (T, N): the missing bar given the total; CHAL (G, N): a graph from clues | EX-CMP-2, EX-CMP-3, EX-CHAL-2 |
| 39 | The Problem-Solving Toolbox | BACK (T, N): tool not named; GC (T, N): guess and check or a table: choose; EQ (G, N): make equal two ways; DIAG (T, N): draw it; TAB (T, N): make a table | EX-BACK-2, EX-CMP-3, EX-EQ-3 |
| 40 | Inquirers' Showcase | CHAL (G, N): write a puzzle with a rule and check it; EXP (G, N): check a friend's puzzle and say what is wrong | EX-CHAL-3 |

### 8.2 Matrix: type by lesson (the spiral across the year)

`o` = already in a written or in-progress lesson (Lessons 1 to 20, and the files for 21 and 23); `N` = new for lessons not yet written; `.` = not planned.

```
Lesson        1234567890 1234567890 1234567890 1234567890
Term          1111111111 2222222222 3333333333 4444444444
LOG           ooo....... o......... o.....N..N N..NN.....
CMP           ......o.oo .o.......o .N..N...N. .......N..
BACK          .....o.... .o.....o.. ..oN...N.. ......NNN.
CTX           o........o ......o.o. oNN......N ...N......
LIST          ..ooo..... .....o.... ....NN..N. .N...N....
EXP           ......oo.. ...oo...o. ........N. ....N....N
GC            .....o.... .......... ...NN..... ........N.
PAT           ...o...... .....o.... .......N.N ..N.N.....
DIAG          .o......o. o......o.. .......... NN......N.
MULTI         .........o .......o.o ..o....... ..........
TAB           .......... .......... .......N.. .N...NN.N.
EQ            .......o.. .oo....o.. .......... ........N.
WAYS          .......... ....o.o... .....N.... ..N..N....
CHAL          .......... .......... ....N..... ......NN.N
```

Count of lessons per type (written or in progress / new / total):

| Type | Written | New | Total | Terms with it |
|---|---|---|---|---|
| LOG | 5 | 5 | 10 | T1, T2, T3, T4 |
| CMP | 5 | 4 | 9 | T1, T2, T3, T4 |
| BACK | 4 | 5 | 9 | T1, T2, T3, T4 |
| CTX | 5 | 4 | 9 | T1, T2, T3, T4 |
| LIST | 4 | 5 | 9 | T1, T2, T3, T4 |
| EXP | 5 | 3 | 8 | T1, T2, T3, T4 |
| GC | 1 | 3 | 4 | T1, T3, T4 |
| PAT | 2 | 4 | 6 | T1, T2, T3, T4 |
| DIAG | 4 | 3 | 7 | T1, T2, T4 |
| MULTI | 4 | 0 | 4 | T1, T2, T3 |
| TAB | 0 | 5 | 5 | T3, T4 |
| EQ | 4 | 1 | 5 | T1, T2, T4 |
| WAYS | 2 | 3 | 5 | T2, T3, T4 |
| CHAL | 0 | 4 | 4 | T3, T4 |

Every type appears in at least two terms. WAYS is absent from Term 1 by design (contest-style, and only 2 school items). BACK, GC, TAB and CHAL are the types the papers use most that the written Terms 1 and 2 use least, and are the main additions in Terms 3 and 4.

### 8.3 Notes and retrofit ideas (not done here)

- **Lessons 21 to 40 are the live assignments.** The Term 3 and 4 authors follow `docs/terms/l1_term3_term4_preflight.md`, section 13. `term/l1/lessons/` and `LESSON3_BRIEF.txt` were not edited.
- **BACK is thin in Lessons 1 to 20** (a light trace in 6, 12 and 18). Suggested Think harder items, for the owner to approve and an author to write: Lesson 7 (a take-away story with the start unknown) and Lesson 10 (an "at first" story, one operation per step). Catalogue items EX-BACK-1 and EX-BACK-2 are the models.
- **LIST (equation from three given numbers) has one home today (Lesson 3).** A fact-family Think harder item fits Lesson 8 (model EX-LIST-3).
- **EXP in multiplication.** True/false statements about packing (a recurring school format) have no lesson item; the models are EX-EXP-2 and EX-EXP-3 for Lessons 15 and 17.
- **Section 5 (end-of-term Quest) and the parent report lines are unchanged.** A non-routine type may appear in the Quest, but no child's score is shown and no type is tested in isolation.
- **Open point for the owner.** None of the 78 papers has a separate challenge section, so the plan does not add one. The non-routine items sit at Think harder and Go further, which matches where the schools put them (ordinary Section B and C questions).
