# Level 1 Term 2 pre-flight (lessons 11 to 20, ages 6 to 8, Primary 1)

Status: planning only, written 22 Oct 2026. No lesson content, no edits to shared files. Term 1 (lessons 01 to 10) is built and audited under `term/l1/`. This document tells the people who will write Term 2 what each lesson is, what the templates must learn first, what went wrong in Term 1, and in which order to build.

Sources read: `docs/terms/level_1_year_plan.md` (Term 2 rows, revision section, coverage matrix, SASMO table), `docs/terms/owner_decisions.md`, `docs/moe/syllabus_by_level.md` (P1 pp. 31 to 32, P2 pp. 33 to 34, P3 p. 35, P4 p. 37, P6 p. 43, heuristics pp. 13 to 14), `docs/sasmo/g1_analysis.md` and `g1_original_problems_draft.md`, `docs/books/word_problems_g1_g2_analysis.md` and `word_problems_g1_g2_original_draft.md`, `docs/books/school_paper_wording_patterns.md`, `term/l1/AUTHORING.md`, `WORDING_GUIDE.md`, `LESSON_BRIEF.txt`, `FIX_BRIEF.txt`, `AUDIT2_BRIEF.txt`, `schema/lesson.schema.json`, all of `term/l1/tools/` (`svg.py`, `b_print.py`, `b_deck.py`, `b_guide.py`, `b_practice.py`, `common.py`, `validate.py`, `build.py`), `assets/l10_extras.py`, the runner `practice/public/practice.js`, Term 1 lesson files `l01` to `l10` (objectives, Remember, kits, figures, practice items), `WORKBOOK_AUDIT_L01` to `L10` and `FIXES_L01` to `L10`.

## 0. Headline findings

1. **Term 2 is the first multiplication, sharing and bar-strip term, and the Term 1 template cannot draw any of it.** Term 1 figures are bundles, scatter stars, ten-frame (one colour), number line, 100 square, ruler, number tiles. There is no table, no group or array picture, no bar strip, no object icons, no queue picture, no symbol shapes. Seven of ten lessons are blocked on at least three new figure types (section 2).
2. **The online runner is text only and cannot show a picture.** Nine of the ten Term 2 lessons depend on a picture to be fair to a 6-year-old (queue, strips, groups, arrays, ten-frames, symbol rows). `practice/public/practice.js` also supports only one numeric answer per item in a template variant. This is a change to a shared file (section 2, R1 to R5), which needs an owner decision (question 7).
3. **Term 1 strings are hard-coded in the tools.** `b_guide.py`, `b_print.py` and `common.py` print "Math Inquirers Term 1 • Notice it. Test it. Explain why." on every page, the guide cover prints "LESSON n OF 10" from `lesson_in_term`, and the practice key is `t1lNN`. A Term 2 lesson built today would carry the wrong term footer and, because lesson 11 has `lesson_in_term` 1, would trip the leak check that rejects stray "Lesson 1" text (section 2, X2).
4. **The end-of-term check for Term 2 sits in Lesson 20, and the Term 1 check generator is lesson-specific** (`assets/l10_extras.py`, with a ruler bar check hard-wired in the validator through `line_mm`). It must become a shared tool before Lesson 20 (X1).
5. **Content risks are small and known.** Contest-style items are all at Think harder; odd/even (Lesson 14), division and the 3 and 4 tables (Lessons 16, 17) and "times as many" (Lesson 18) are beyond P1 and must say so plainly in the guide and parent page (owner decision of 22 Oct 2026).
6. **Estimate:** about 85 agent-hours for the ten lessons (write, wording review, independent audit, fix pass) and about 55 to 75 agent-hours of template engineering (55 if optional items are deferred). Term 1 took roughly 6 hours of wall clock (first commit 10:55, last 16:54 on 22 Oct 2026) with the lessons written in parallel. Term 2 should take about 1.5 working days if the template work is staged as in section 4.

## 0.1 Assumptions made (change them if wrong)

- Files are `term/l1/lessons/l11.json` to `l20.json`; `lesson` is 11 to 20 and `lesson_in_term` is 1 to 10, `term` is 2, practice keys `t2l11` to `t2l20`. Printed badges say "Term 2 • Lesson 3" (lesson in term) so a family never sees "Lesson 13 of 10".
- Same 11-part 90-minute timing, same tier rules, Mi the dolphin, private-paper safeguarding, spare-time menu, 6-minute Remember with three items, beyond-P1 statement in the guide and parent page, no "MOE-aligned", "SASMO" or "GEP" on any child or parent page.
- Term 1 owner decision stands: stronger arithmetic than school, but every Start here item is approachable with scaffolding after class exploration. Term 2 has less of this problem: the multiplication, sharing and ordinal lessons are P1 content; the stretch is in 12, 14, 16 (3s and 4s), 18 and 19.
- Names: Mei, Ali, Ben, Siti, Ravi, Kumar, Aisha, Wei, Jenny, Lily. Term 1 used "Siti" as the error-spotter in all ten lessons (school-paper review, item 3 of section 2.1). Spread the error-spotter across the cast in Term 2.
- Multiplication is written with `×` and division in words ("shared by", "groups of"). Check that `×` and `÷` render: the fonts are the Fredoka and Nunito Sans Latin subsets, which include U+00D7 and U+00F7, but no Term 1 lesson has used them, so the first build must check the PDF text. The validator bans only geometric and emoji glyph ranges, so `×` is allowed.

## 1. Lesson specs

Every spec uses this order: big idea, strand and page refs, objective, prerequisites (the exact Term 1 lesson), Remember warm-up (three items, re-taught with objects), tiers in outline, gaps closed, number ranges and what is beyond P1 on purpose, home materials, kit, figures and pictures, misconceptions, template needs (codes from section 2). "Beyond P1" labels follow `docs/moe/syllabus_by_level.md`. Contest-style items are tutor labels only and appear only at Think harder or Go further.

### Lesson 11. Who Is Where?

- **Big idea.** A place in a line has a name (1st, 2nd, 3rd ...) and can be counted from either end.
- **Strand.** MOE P1 Whole Numbers, ordinals "first, second, up to tenth" with 1st, 2nd, 3rd (1.7, p. 31). Position words (front, back, between, behind) are language, not a syllabus item. Contest tag: queue and gap counting at Think harder (SASMO ordering and logic, 7 of 100 papers).
- **Objective.** Say, read and write 1st to 10th. Place a child or object from an ordinal clue. Say a place counted from the front and from the back. At Think harder: find how many are in a line from "8th from the front and 8th from the back", and how many are between two places.
- **Prerequisites.** Lesson 2 (counting on and back along a line; number words, which the ordinal words extend). Lesson 3 (order from smallest, "begin with"). Lesson 7 (a difference is a gap, so "between" is a gap). Lesson 5 (adding to 20 for 8 + 8 − 1).
- **Remember (6 min).** (1) Touch and count a row of up to 10 objects, one touch per object, and say the last number (counting to 20, Lesson 2 line). (2) One before and one after a number (Lesson 2). (3) Front, back, behind, between, using the holiday ordering topic only as spiral (children stand objects in a row).
- **Start here.** Ordinals 1st to 10th in a picture line of up to 8 (circle the 3rd, colour the 5th, write the place of the child with the cap). Single-clue ordering ("Ali is 2nd. Mei is behind Ali. Who is 3rd?") in a line of 5. Five to seven questions, picture first, no more than two clues.
- **Think harder (contest-style).** "Ravi is 8th from the front and 8th from the back. How many children are in the line?" (15). "Ali is 3rd and Mei is 9th. How many children are between them?" (5). Reversed direction (the line faces the other way). Three to five questions.
- **Go further.** Six children sit round a table; clues give next to, opposite; place everyone. A longer queue with two "from the back" clues. Exactly three.
- **Gaps closed.** SASMO ordering and logic (circular seating is not in Term 1). Books: reading traps, "count yourself once" and "the child in the middle of the line" (Grade 2 book, queue items). The two school papers studied do not test ordinals, so there is no paper evidence either way.
- **Numbers.** Ordinals to 10th are core. Lines of up to 20 children only at Think harder and Go further, where the answer is a count, not an ordinal. Beyond P1: none; the gaps-and-posts reasoning (8 + 8 − 1) is contest-style.
- **Home materials.** Ten small toys, shoes, cups or spoons in a row; a coin as a marker; paper people from the kit; a table and six chairs for the Go further picture (or the picture itself).
- **Kit.** K4: ordinal cards 1st to 10th (cut-out, `cards` kit with labels) and a strip of 10 paper people in varied colours.
- **Figures and pictures.** `line_up` queue picture with front marked, ordinal labels or answer boxes under people, optional highlight and bracket for "between" (F6). `round_table` with seats and names (F6). Child icons in six colours (F2). A clue table (F1).
- **Misconceptions.** 4 and 4th are the same thing (cardinal versus ordinal); counting a child twice in "8th from both ends" (8 + 8 = 16); "between" includes both ends; spelling 2th, 3th; counting from the wrong end when the picture faces left; "first" as 0.
- **Needs.** F6, F2, F1, K4, B1, B3 (True/False), R1, R4 (ordinal formatter for practice variants).

### Lesson 12. Bar Strips: More and Fewer

- **Big idea.** A strip shows the story; a longer strip is more, and the extra part is the gap.
- **Strand.** MOE P1 Addition and Subtraction in context (p. 31). Bar models are not named in the 2021 syllabus (heuristics and representing, pp. 13 to 14); tutor label "representing". Contest tag: transfer and sum-and-difference at Think harder (SASMO bar-model word problems, 7 of 100, all in Section B).
- **Objective.** Draw one strip per person for a compare story, bracket the gap, and choose add or subtract from the picture. At Think harder: total and difference given (find each); make two amounts equal by a transfer.
- **Prerequisites.** Lesson 10 (read it twice, one operation per step, reversed wording "fewer than", "who is in the group"). Lesson 7 (a difference is a gap, count up, check by adding back). Lesson 8 (give and take keeps the total, which is the transfer idea). Lesson 1 (a tens bar is ten, so bars from the kit are strips).
- **Remember (6 min).** (1) "I think of a number" and undoing a step (Lesson 10, holiday Mystery Number as spiral). (2) The gap between two numbers by counting up (Lesson 7). (3) Build 36 with 3 bars and 6 squares and see a bar as a strip (Lesson 1).
- **Start here.** Two people, one has more: draw two strips, find the other person's number and the total ("Siti has 36 beads. Dev has 19 more. How many altogether?"); "how many more" as the gap. Reversed wording is Think harder, not here. Five to seven questions.
- **Think harder.** Total and difference given (40 altogether, Ali has 8 more: 24 and 16). Make equal by a transfer (Ali 30, Mei 18: Ali gives 6). Reversed wording ("Hui has 18 fewer than Raj"). Group totals then compare.
- **Go further.** Transfers with a total ("52 books on two shelves; 7 moved and now equal: how many at first?" 33). A compare chain of three with a given total.
- **Gaps closed.** SASMO bar-model, transfer and sum-and-difference. Books: compare then total (8 of 101), compare chain (4), group totals then compare (8), make equal by a transfer (2), reversed wording (G1-Q12 type). Plan note: books treat transfers as ordinary school work.
- **Numbers.** Within 100, totals to 90, even totals for sum-and-difference so halves are whole. Beyond P1 on purpose: the bar model itself and sum-and-difference.
- **Home materials.** Strips cut from a sheet of paper, coloured pencils, counters; or the same tens bars and ones squares as Term 1.
- **Kit.** Reuse the base-ten page (no new kit) or K2 unit strips.
- **Figures.** `bar_model` with modes compare, part-whole, transfer (F3); object icons (F2); a before and after pair for transfer; a two-figure question (B5).
- **Misconceptions.** Strips drawn the same length whatever the numbers; adding when the sentence says "fewer"; the gap bracket attached to the wrong strip; moving the whole gap instead of half in a transfer; forgetting to halve in sum-and-difference; the answer to the first step reported as the final answer.
- **Needs.** F3, F2, F1 (Investigation table), B2, B4, B5, R1, R2.

### Lesson 13. Doubles and Near Doubles (new topic, syllabus check needed)

- **Big idea.** Double, then adjust by one.
- **Strand.** MOE P1 Addition and Subtraction (adding more than two 1-digit numbers, mental calculation within 20, within 100, p. 31). Flagged "new topic" in the plan: owner or tutor syllabus check before build. Links to pairing and the 2 table.
- **Objective.** Recall doubles to 10 + 10 with a picture, double a tens number, add near doubles as a double plus or minus 1 (7 + 8). At Go further: add five almost-equal numbers.
- **Prerequisites.** Lesson 5 (bonds to 10 and 20 on a ten-frame, make a ten, add several numbers). Lesson 8 (give and take: moving 1 across keeps the total, so 7 + 8 = 7 + 7 + 1 = 8 + 8 − 1). Lesson 6 (double a tens number is a tens jump: 3 tens and 3 tens). Lesson 1 (30 is 3 tens).
- **Remember (6 min).** (1) How many more make 10 on a ten-frame, with fingers (Lesson 5). (2) 3 tens and 3 tens is 6 tens (Lessons 1 and 6). (3) = means the same amount on both sides (Lesson 8).
- **Start here.** Doubles 1 + 1 to 10 + 10 from ten-frame and domino pictures; double 10, 20, 30, 40, 50 with tens bars; "double 6 is ___". Five to seven questions.
- **Think harder.** Near doubles (6 + 7, 7 + 8, 9 + 10), choose which double to use; "6 + 6 + 1"; which sum is not near a double. Three to five questions.
- **Go further.** Add five almost-equal numbers (8 + 9 + 8 + 7 + 8 = 40; 19 + 20 + 21 + 20 + 19 = 99); doubling a non-tens two-digit number (double 35) is beyond P1 and appears here only.
- **Gaps closed.** SASMO computation and number sentences (13 of 100, multi-term sums). Books: join three groups (5 of 101, with part of many others). Speed and accuracy of mental facts stays with school (plan).
- **Numbers.** Doubles to 20, tens doubles to 100, near doubles to 19, sums under 100. Beyond P1: doubling two-digit non-tens numbers only at Go further.
- **Home materials.** An egg carton (6 + 6), two plates, 20 counters of two colours (beans, pasta), dominoes if the family has them.
- **Kit.** K3 ten-frame page (four frames, 10 red and 10 yellow counters) which also closes the Lesson 5 gap. Optional K5 dot cards.
- **Figures.** Two-colour ten-frame (F8), domino figure (F8), a double and near-double table (F1), two equal bars for "double" (F3, optional).
- **Misconceptions.** 7 + 8 as 14 or 16 (taking the wrong double); "double" as add 2; double 30 as 600 or 36; adjusting in the wrong direction (8 + 8 = 16, so 7 + 8 is 15); counting on by ones from the larger number.
- **Needs.** F8, K3, F1, B2, B1, R1.

### Lesson 14. Odd + Odd: Always, Sometimes, Never?

- **Big idea.** One test is not a proof; a picture can show why it is always true.
- **Strand.** Odd and even numbers are MOE P2 (Whole Numbers 1.6, p. 33), so the whole topic is beyond P1 on purpose; flagged in the plan. Process strand: reasoning and communicating (pp. 13 to 14). Contest tag: parity (SASMO number sense).
- **Objective.** Sort numbers to 20 as odd or even by pairing, say the rule for the last digit, test whether odd + even, even + even and odd + odd are odd or even, and explain odd + odd with pairs.
- **Prerequisites.** Lesson 4 (the 2s on the 100 square end in 2, 4, 6, 8, 0). Lesson 8 (two plates, fair share, give and take). Lesson 3 (the ones digit of a two-digit number, digit cards). Lesson 1 (a ten is made of pairs, so the ones digit decides).
- **Remember (6 min).** (1) Pair up counters or fingers and see if one is left over (Lesson 8 plates, holiday pairing). (2) Count in 2s on the 100 square (Lesson 4, holiday Frog). (3) Read the ones digit of 47 and say how many tens and ones (Lessons 1 and 3).
- **Start here.** Pair counters to sort 1 to 20 into odd and even; colour the 2s on a 100 square strip and say what the last digits are; write odd or even for numbers up to 20. Five to seven questions, no written reasons (rule 25).
- **Think harder (inquiry).** "What is odd + even?" with three tests and "Always, Sometimes or Never"; "Is 57 odd?" by the last digit; a claim with one test that fails ("odd + odd is odd? try 3 + 5"). Three to five questions.
- **Go further.** Explain with pictures why odd + odd is always even (two left-over singles make a pair); odd + odd + odd. Exactly three.
- **Gaps closed.** SASMO number sense (odd and even sits inside the 14-problem place-value and digit-puzzle category). Sets up Term 3 reasoning (Lessons 27 to 29). No book or school-paper evidence; the plan allows a tutor to swap this lesson (Term 2 note: safest to skip).
- **Numbers.** Counters 1 to 20 (core), last-digit rule to 100 at Think harder. Beyond P1: the whole topic.
- **Home materials.** 20 counters, two paper plates, the 100 square from Lesson 4 if kept.
- **Kit.** `cards` 1 to 20 (existing) and optionally K1 pairs mat.
- **Figures.** `array` in pairs layout with a left-over ring (F5), tick table (F1 and B3), 100 square with the 2s shaded (existing `hundred`), counters (F2).
- **Misconceptions.** One example proves a claim; reading the tens digit; "odd means big or strange"; 1 is even; odd + odd = odd; answering Sometimes when only one pair was tried; unequal pairs counted.
- **Needs.** F5, F2, F1, B3, K1, R5 (choice template for odd and even), B1.

### Lesson 15. Equal Groups

- **Big idea.** Same-size groups can be counted fast: repeated addition and the × sign.
- **Strand.** MOE P1 Multiplication and Division (concept, × sign, multiply within 40; 3.1 to 3.4, p. 31). The holiday course has none.
- **Objective.** Recognise equal groups, write "4 groups of 3 = 12" and 3 + 3 + 3 + 3 = 12, write 4 × 3 = 12, read an array as rows and as columns. Think harder: 3 × 4 = 4 × 3.
- **Prerequisites.** Lesson 4 (skip-count 2, 5, 10 on the 100 square). Lessons 5 and 6 (adding the same number again; jumps on a line). Lesson 1 (bundles of ten are equal groups). Lesson 13 if it comes first (a double is 2 groups).
- **Remember (6 min).** (1) Skip-count 2s, 5s, 10s (Lesson 4). (2) Draw 3 tens and 4 ones (Lesson 1). (3) Add by making a ten (Lesson 5). These are the three items named in the plan's Term 2 note.
- **Start here.** Which pictures show equal groups (circle Yes or No); 4 groups of 3 by drawing and counting; the frame "[] groups of [] = []"; repeated addition for 5 groups of 2. Five to seven questions, products to 20.
- **Think harder.** Array of 3 rows of 4, turn it into 4 rows of 3, "Is 3 × 4 = 4 × 3? Circle Yes or No"; "How many more to make equal groups?" (school-paper type). Three to five questions.
- **Go further.** Legs and wheels: 3 bikes with 2 wheels and 4 cars with 4 wheels (22); a product close to 40 with a missing group.
- **Gaps closed.** SASMO multiplication facts and symbol-equation readiness (about 11 of 100 touch ×). Books: equal groups one step (4 of 101) and plus another step (14). School paper (Henry Park P1 quiz): the frames "[n] groups of [n] = [n]", "2 sevens", "7 groups of 2", True/False on legs, "How many more to make equal groups?".
- **Numbers.** Products within 40, groups of 2, 3, 4, 5 and 10 (more groups of a small size, for example 6 groups of 5, are allowed). Beyond P1: none if products stay within 40.
- **Home materials.** 24 small items, six cups or bowls, an egg carton or muffin tray for arrays.
- **Kit.** K1 groups mat (six plates), optional K6 array mat.
- **Figures.** `groups` (plates, bags, jars) with equal and unequal counts and an empty variant to draw in (F4), `array` (F5), icons (F2), a groups-each-total table (F1).
- **Misconceptions.** Unequal groups counted as equal; the number of groups confused with the number in each group; "3 × 4" read as 3 + 4; miscounting groups in a scattered picture; reading order of "groups of" versus the × sign (see question 1); array rows and columns swapped.
- **Needs.** F4, F5, F2, F1, K1, K6, B1, B2, B3, B5, R1, R2.

### Lesson 16. Skip-Count Tables

- **Big idea.** Tables are skip counts, and the patterns show up in the last digits.
- **Strand.** MOE P1 Multiplication and Division, multiply within 40 (p. 31). Tables of 3 and 4 are P2 (p. 33), so beyond P1 on purpose. Tables of 6 to 9 are P3 (p. 35) and are left out. Common multiples are P4 (p. 37): contest-style, tutor label only, at Think harder.
- **Objective.** Build the 2, 5 and 10 tables by skip counting and colouring, say facts such as "5 × 6 = 30", use the 2s to get the 4s, find numbers in two tables.
- **Prerequisites.** Lesson 4 (100 square, 10s, 5s, 2s, last digits). Lesson 6 and Lesson 2 (jumps with labels on a number line). Lesson 15 (groups, × sign). Lesson 13 (a double, so 4s are doubled 2s).
- **Remember (6 min).** (1) Skip-count 2s, 5s and 10s on a 100 square (Lesson 4, holiday Frog). (2) Jumps of the same size on a line, with the jump labelled (Lessons 2 and 6). (3) "5 groups of 6" as repeated addition (Lesson 15, re-taught).
- **Start here.** Build the 2, 5 and 10 tables in a row of boxes (1 × 5 to 8 × 5), shade them on the 100 square, say "6 fives is 30". Five to seven questions, products to 40.
- **Think harder (contest-style at part).** Use the 2s to find the 4s ("4 × 6 is double 2 × 6"); which numbers are in both the 2s and 5s tables (10, 20, 30, 40); "Is 35 in the 5s table?". Three to five questions.
- **Go further.** Numbers up to 40 in three tables (2, 4 and 5: 20, 40; 2, 3 and 5: 30); build the 3 table and find what it shares with the 2 and 5 tables. Exactly three.
- **Gaps closed.** SASMO multiplication facts and the analysis row "tables of 3 to 8, shared multiples" (marked Gap). Books: equal groups. No school-paper evidence beyond the P1 quiz.
- **Numbers.** The 2, 5 and 10 tables to 10 × as skip counts (to 100), written answers within 40 at Start here. 3 and 4 tables to 40. Beyond P1: the 3 and 4 tables and common multiples.
- **Home materials.** The 100 square from Lesson 4, coloured pencils, 40 counters.
- **Kit.** Existing `hundred` kit page (cell 64) and optional `number_strip`.
- **Figures.** `hundred` with overlap colour for two tables (F9), `number_line` with repeated jumps (exists), `seq` tiles with +5 arcs (exists), a times-table row table (F1), `array` for 4 × 6 (F5).
- **Misconceptions.** Starting at 0 or counting the starting square as the first jump; skipping a jump; assuming every number ending in 5 or 0 is in the 10s table; reciting without meaning; mixing 6 + 5 and 6 × 5; thinking 10 is the only number in two tables.
- **Needs.** F9, F1, F5, B1, B2, B3, B5, R1, R2, R3.

### Lesson 17. Sharing and Grouping

- **Big idea.** Two kinds of division: share equally (how many in each) or put into groups (how many groups).
- **Strand.** MOE P1 Multiplication and Division, divide within 20 (p. 31). Remainder language is P3 (p. 35), so only "left over". The ÷ sign is P2 (p. 33): see question 2.
- **Objective.** Share a set equally by dealing, find how many groups of a given size, check by multiplying, say what is left over.
- **Prerequisites.** Lesson 8 (two plates with the same amount, give and take). Lesson 7 (take away again and again). Lesson 15 (equal groups). Lesson 16 (skip count to find how many groups). Lesson 10 (the "who is in the group" trap).
- **Remember (6 min).** (1) Deal objects one at a time onto two plates (Lesson 8). (2) Skip-count by 3s and 4s on a line (Lessons 6 and 16). (3) An equal-groups picture (Lesson 15, re-taught).
- **Start here.** Share 12 among 3, group 12 into 4s; deal counters onto plates; fill "Each plate has ___." Five to seven questions, within 20, no left over.
- **Think harder.** "How many groups of 4 in 14?" (3, with 2 left over); "Ben shares 20 biscuits with 3 cousins" (4 people share: reading trap); share or group? (circle). Three to five questions.
- **Go further.** All the ways to share 12 equally (1, 2, 3, 4, 6, 12 groups) in a table; one more step after sharing. Exactly three.
- **Gaps closed.** Books: share or group plus another step (6 of 101), division one step (4), "who is in the group" (G1-Q77, G2-Q8). Henry Park P1 quiz: "shares equally with Jim", "packs 6 in a bag", "how many more to make equal groups".
- **Numbers.** Within 20; left over only at Think harder, up to 4 left over; no remainder notation. Beyond P1: the word remainder and the ÷ sign.
- **Home materials.** 20 counters or buttons (not food), five plates or cups.
- **Kit.** K1 groups mat (reuse).
- **Figures.** `groups` with empty plates and a `?` (F4), `array` for grouping (F5), a ways-to-share table (F1), bar strip split into equal parts (F3, optional).
- **Misconceptions.** Unequal shares; confusing 6 groups of 2 with 2 groups of 6; forgetting the sharer; answering the number of groups when asked "each"; thinking the left over gets shared; subtracting instead of dividing.
- **Needs.** F4, F5, F1, K1, B1, B2, B5, R1, R2, R3.

### Lesson 18. Times Stories

- **Big idea.** Draw the story as equal strips, then solve.
- **Strand.** MOE P1 Multiplication and Division and Addition and Subtraction word problems (p. 31). "Times as many" in a bar model is beyond P1 (SASMO-type, Think harder).
- **Objective.** Draw equal units for a story with 3 groups of 5, get the total, add or take away a second step, solve "twice as many as".
- **Prerequisites.** Lesson 12 (compare and transfer strips). Lessons 15 to 17 (groups, tables, sharing). Lesson 10 (one operation per step, number sentence per step). Lesson 13 (twice is double).
- **Remember (6 min).** (1) Draw two strips and the gap for a compare story (Lesson 12). (2) "4 groups of 5" as 4 × 5 (Lesson 15, re-taught). (3) One operation per step (Lesson 10).
- **Start here.** One-step times story with a picture (3 bags with 5 sweets each); the frame "[] groups of [] = []"; story with a total plus one more step. Five to seven questions, products to 20.
- **Think harder (contest-style).** Two-step with a total ("4 boxes of 5 pens and 6 loose pens"); "Ali has twice as many as Mei; Mei has 8; how many do they have together?"; "twice as many" with a transfer. Three to five questions.
- **Go further.** Three groups of different sizes with a hidden start; "3 times as many" with a total.
- **Gaps closed.** SASMO bar-model word problems with "times as many" (7 of 100, Section B). Books: equal groups plus add or take away (14 of 101), the second commonest type.
- **Numbers.** Products within 40, totals with the extra step within 100. Beyond P1: "times as many" comparison and transfer with a ratio.
- **Home materials.** Counters, cups, strips of paper.
- **Kit.** K1 groups mat and K2 unit strips (or the base-ten page).
- **Figures.** `bar_model` equal units with a total brace (F3), `groups` (F4), icons (F2), a step table (F1).
- **Misconceptions.** "Twice as many" as 2 more; "3 times as many" as 3 more; adding the group sizes instead of counting groups; dropping the second step; unequal units in the drawing; wrong unit on the answer.
- **Needs.** F3, F4, F2, F1, K1, K2, B2, B4, R1, R2.

### Lesson 19. Picture Equations

- **Big idea.** A shape is a hidden number, and the same shape is always the same number.
- **Strand.** Beyond P1. Letters for unknowns are P6 (p. 43), so shapes and boxes only. Touches P1 Addition and Subtraction "=" and the inverse relationship (p. 31) and × within 40. Contest tag: symbol equations and substitution (SASMO, 4 of 100, all four marks each in Section B, all using ×).
- **Objective.** Find a shape in a one-unknown equation, solve two-shape equations by taking one line from another, and use a × line.
- **Prerequisites.** Lesson 8 (boxes, balance, give and take, which the Lesson 8 note names as the base of this lesson). Lessons 15 and 16 (× facts). Lesson 12 (strips of equal units). Lesson 5 (bonds).
- **Remember (6 min).** (1) A box in a sentence: 6 + 3 = 5 + [] (Lesson 8). (2) A times fact: 4 groups of 5 (Lesson 15, re-taught). (3) Two lines about the same things (Lesson 8 plates).
- **Start here.** One shape and a box: 4 + ◇ = 10 (drawn shape, not the glyph), ◇ + ◇ = 12, and what a shape stands for in a picture row. Five to seven questions, totals to 20.
- **Think harder (contest-style).** Two different shapes; take one equation from another (○ + ○ + △ = 17 and ○ + △ = 11); check the answer in both lines. Three to five questions.
- **Go further.** Three symbols with a × line (□ × □ = 36; ♡ + □ = 15; ☆ − ♡ = 4, an original of draft item 6.2) and a two-equation puzzle (draft item 6.3). Exactly three.
- **Gaps closed.** SASMO gap 6 (symbol equations plus multiplication facts). No book or school-paper evidence.
- **Numbers.** Each shape up to 20, totals within 40, × facts from the 2, 3, 4, 5 and 10 tables. Beyond P1: the whole idea of substituting and subtracting equations.
- **Home materials.** Counters in three colours or paper shapes, two cups to hide a number, paper.
- **Kit.** Existing `shapes` kit (circle, square, triangle) used as tokens; add a star and a heart (K7).
- **Figures.** `picture_equation` rows with drawn shapes and answer boxes (F7), a "what is each shape" table (F1), plates (F4).
- **Misconceptions.** Different shapes must be different numbers (state the rule once); reading ○○ as the number 55; adding all the shapes to the total; subtracting the wrong way; checking only one line; reading × as +.
- **Needs.** F7, F1, K7, B1, B2, B4, B5, R1, R2.

### Lesson 20. Find One First (added)

- **Big idea.** Find one, then find many.
- **Strand.** MOE P1 Multiplication and Division word problems (p. 31) and Money (count money in dollars up to $100, p. 31). Vocabulary: dozen, each, such.
- **Objective.** Find the price or size of one from a group by dividing, then find another group, then a change step. Draw a strip of equal units for the story.
- **Prerequisites.** Lesson 17 (total shared into equal groups). Lessons 15 and 16 (× tables). Lesson 18 (unit strips, times stories). Lesson 12 (strips). Lesson 10 (steps).
- **Remember (6 min).** (1) 12 shared among 3 (Lesson 17). (2) "Each" and "altogether" (Lessons 15 and 18, re-taught). (3) Draw four equal units (Lesson 18).
- **Start here.** "4 pens cost $20. How much does 1 pen cost?" with a picture and a strip; "1 pen costs $3; 4 pens cost?" Five to seven questions, dollars only.
- **Think harder.** The price of 7 from the price of 3 ("3 books cost $12, so 7 cost $28"); a dozen; "such". Three to five questions.
- **Go further.** Two steps with money left over; "2 mugs cost $14 and 5 spoons cost $10; Ali buys 1 of each" (draft A12.3).
- **Gaps closed.** Books gap 3: price or size of one from a group (6 of 101 in Book 1, 8 in Book 2). Vocabulary gap (a dozen, each, such). Rosyth P2 money frames ("The 3 notebooks cost $___").
- **Numbers.** Whole dollars only, totals within 40 for × and within $100 overall; no cents and no notes or coins (Lesson 24). Beyond P1: none.
- **Home materials.** Beans or buttons as dollars, paper price tags from the kit, a few small items.
- **Kit.** Existing `cards` kit (round cards for $1 tokens, price tags). Optional K2 strips.
- **Figures.** `bar_model` equal units with a total brace (F3), item icons (F2), a price-tag figure (F10, optional), an items and cost table (F1).
- **Misconceptions.** Multiplying 20 × 4 instead of dividing; using the total as the price of one; ignoring "each"; multiplying 7 × 12 for 7 books; forgetting the change step; "dozen" unknown.
- **Also hosts the 20-minute end-of-term check** (10 questions, one per lesson, private paper, photo return to the business WhatsApp), which forces X1 and a second extras build. See risks.
- **Needs.** F3, F2, F1, F10, K2, X1, B1, B2, B4, R1, R2.

### Term 2 at a glance

| # | Title | Wave | Blocking template items | Safest to skip? |
|---|---|---|---|---|
| 11 | Who Is Where? | A | X2, B1, F6, F2, K4 | No |
| 12 | Bar Strips | C (pilot for strips) | F3, F2, B4, B5, R1, R2 | No, 18 and 20 build on it |
| 13 | Doubles and Near Doubles | B | F8, K3, F1, B2 | Fairly safe |
| 14 | Odd + Odd | B | F5, F1, B3, R5 | Yes (plan note) |
| 15 | Equal Groups | B (pilot for groups) | F4, F5, F1, K1, B2, B3 | No, 16 to 18 build on it |
| 16 | Skip-Count Tables | B | F9, F1, F5, R3 | No |
| 17 | Sharing and Grouping | B | F4, F5, F1, K1, R3 | No |
| 18 | Times Stories | C | F3, F4, K2, B4 | No |
| 19 | Picture Equations | C | F7, K7, B4 | Fairly safe |
| 20 | Find One First + check | D | F3, X1, F10 | No (holds the check) |

## 2. New template capabilities Term 2 needs

Ordered by the number of lessons that need each item (lessons in brackets). "Exists" means it is already in the tools and needs no work. Hours are template-engineer estimates, not measured.

### 2.1 Term-level and tool-level (all ten lessons)

**X2. Term parameters instead of hard-coded Term 1 text (all 10, about 2 h).** Add `term_name` and `term_tagline` (Term 2: "Test it") to a lookup used by `b_guide.py` line 102 and 191, `b_print.py` line 179, `common.py` FOOT_PARENT and the deck `FOOT`. The guide cover must print the lesson number in the term out of 10 (it already does, from `lesson_in_term`). Practice key prefix `t2l`. Fix `check_foreign` in `validate.py`: it currently fails any "Lesson 1" in any lesson except 01, so `lesson_in_term` 1 (Lesson 11) must be excepted, and the "title of another lesson" scan must read lessons 11 to 20 only. Add `term` to `build.sh` output names if needed. Acceptance: L11 builds with a Term 2 footer on guide, deck, workbook, key, home sheet, parent page, and the leak check is clean.

**B1. Answer-slot widths (all 10, about 2 h).** Today `___` is one fixed dashed line (`.al` min width 70 px about 18 mm) and `[]` is one 36 px box; Term 1 audits called the dashes "14 mm" and too short for two-digit answers or a word. Define tokens: `___` short (18 mm, one number), `______` medium (30 mm, a number and a unit), `_________` long (45 mm, a word or name), `[]` one box, `[2]` two linked boxes for a two-digit answer (tens box and ones box, 36 px each, 2 px gap), `[3]` for three. Render the same way on workbook, key, guide, deck and home (the home sheet currently shrinks boxes to 26 px). The validator's answer-slot test must count the new tokens.

**X3. Validator updates (all 10, about 3 h).** (a) Register every new figure type so `render_visual` and the deck accept it. (b) Count answer boxes inside new figures (table cells, bar labels, array labels, queue labels) as answer slots; today only `hide` on a picture counts. (c) The draw-stroke estimator reads "N bundles, boxes, tens"; make it read "N groups of M" (strokes are N × M) and "draw N rows of M". (d) Allow `choices:["Always","Sometimes","Never"]` without a "Circle Yes or No" phrase (the circle rule already accepts explicit `choices`, check). (e) Run the 7-word overlap test with the multiplication command phrases on the standard-wording allow list (commit 8052ec5 added one for Term 1) so stock phrases from the Henry Park pattern ("groups of", "in all", "how many more") do not fail. (f) Make `line_mm` and the ruler check optional in the term-check validation (X1).

**B2. Operation-sign circle and equation frames (8: 12, 13, 15, 16, 17, 18, 19, 20; about 2 h).** WORDING_GUIDE rule 17 asks for "box, circle, box = box" when the sign is part of the answer. Add the token `()` which prints an empty 36 px circle for + − × ÷, and a prebuilt frame token `{eq}` meaning `[] () [] = []`. Same circle in the key (filled), guide and deck. Without this, "Write a multiplication sentence" has no honest answer slot.

**R1 to R5. Online practice runner (9 lessons need R1; 7 need R2; about 14 h including validator and oracle work).** The runner (`practice/public/practice.js`, shared by other levels) handles `number`, `choice`, `multi`, `set`, `selfcheck`; the text of a question is a plain string with `{var}` substitution; a template variant is always a single number (`variantOf` returns `type:'number'`). For Term 2:
- **R1 Pictures in items (9: all except 14).** An item may carry `fig` (any figure spec from `svg.render_visual`). `b_practice.py` renders it at build time into `item.svg` (a sanitised inline SVG string with an `aria-label`, at most 12 KB); the runner inserts it above the question. No network, no script in the SVG. Variants may use variables inside the spec (`"rows":"{a}"`).
- **R2 Ordered multi-box answers (7: 12, 15, 16, 17, 18, 19, 20).** New type `fields`: `{"frame":"{a} groups of {b} = {c}","fields":[{"id":"a","answer":4}, ...]}` with one numeric input per field, neutral per-field feedback (the runner's current "Not quite yet" wording), and a template form where each field has an expression. The current `set` type is unordered, so "3 groups of 4" and "4 groups of 3" would both pass.
- **R3 List-valued template answers (2: 16, 17).** Templates may return `set` answers using a whitelist of helpers: `multiples(k, limit)`, `common(a, b, limit)`, `divisors(n)`. Each needs a Python oracle in `verify/lNN_checks.py`; the validator's JavaScript cross-check must run the same helper.
- **R4 Formatters (L11, L20).** `{n|ord}` gives 1st, 2nd, 3rd, 4th to 20th; `{n|word}` gives number words for "a dozen" practice. Display only; arithmetic stays digits.
- **R5 Templated choice (L14).** A `choice` item may have a template with `options` and `answer_index` as an expression (n % 2) so "Is 7 + 9 odd or even?" can vary.
- Keep Level 3's sample page and any other level that uses the runner working: add `"runner":2` in the data and keep v1 behaviour when absent. This is a shared-file change: question 7.

**X1. Shared end-of-term check generator (L20, about 5 h).** Move `end_of_term_check` building from `assets/l10_extras.py` into a tool such as `tools/b_check.py` that takes the lesson, builds the student sheet (3 to 4 pages), tutor key with record sheet and procedure, grown-up note, and runs real-PDF page checks. Parameters: term name, the 10 question sources (one per lesson 11 to 19 plus Lesson 20), the WhatsApp return text from `owner_decisions.md`, optional ruler bar. Remove `line_mm` from the mandatory validator keys. Without this the Term 2 check is a hand-built copy of L10 again.

### 2.2 Figure types (new `type` values for slides, workbook, home sheet, key and practice)

**F1. `table` (9: 11, 12, 13, 14, 15, 16, 17, 19, 20; about 5 h).** A visible table in questions and slides, answer-ready. Spec: `{"type":"table","head":["Groups","In each","Total"],"rows":[["4","3","[]"],["[]","5","30"]],"col_w":[1,1,1],"first_col":"label"}`. Cell tokens: plain text, `[]`/`[2]` answer boxes, `()` circle, `[ ]` tick box (empty square with no text), an icon object `{"icon":"apple","n":3}`. Head row yellow like the existing place-value table (`.pv`), cell height at least 11 mm in print and text at least 34 px on a slide, thick navy borders. The key prints the filled values from an `answers` array. A slide text `table` block already exists (`b_deck.table`) but is not available in workbook questions: share the code. This also gives Investigation pages their table (Term 1 audits L1, L2, L8, L10 asked for it and were told "left to the owner").

**F2. `objects` icon set (8: 11, 12, 14, 15, 17, 18, 19, 20; about 5 h).** One drawing engine for everyday countable things. Spec: `{"type":"objects","icon":"apple","n":7,"per_row":5,"size":"m","cross":[2,3],"hide":[6],"label":"..."}` and `{"items":[{"icon":"pen","n":4},{"icon":"book","n":3}]}` for mixed rows. Icons (about 24, flat palette, 64-unit viewbox, navy outline 2.4 px, one fill): child (six colour variants), apple, cookie, sweet, sticker, ball, marble, pencil, pen, book, cup, plate, bag, jar, flower, fish, bird, spider, ladybird, bike, car, counter (red or yellow dot), coin ($1 round token). No unicode glyphs. Needed for story pictures (school papers pair almost every story with a picture, `school_paper_wording_patterns.md` section 2.1 item 11).

**F3. `bar_model` (3 required: 12, 18, 20; 3 optional: 13, 17, 19; about 6 h).** The strip picture. Spec: `{"type":"bar_model","mode":"compare|part_whole|equal_units|transfer","bars":[{"name":"Ali","len":36,"segments":[{"v":24,"text":"24"},{"v":12,"text":"[]"}],"colour":"yellow"}],"brace":{"text":"[]","over":"all"},"gap":{"between":[0,1],"text":"?"},"units":{"n":4,"text":"5"},"arrow":{"from":0,"to":1,"v":6}}`. Rules: lengths proportional to value (the picture must not lie), unit cells with a visible dividing line and the value or an answer box inside, a name column on the left, a bracket with a label or a `?` shown in grey, a dashed equal-length line for compare mode, before and after pair with a curved arrow for transfer. At most 10 cells per bar and 3 bars. Label text 28 px or more on slides. The key shows the filled version. Also needs a workbook mode where the bar is empty for the child to draw in (a drawing box with a printed baseline of 10 faint cells).

**F4. `groups` (5: 14, 15, 17, 18, 20; about 3 h).** Containers holding items, which also closes the Lesson 8 "plate figure" gap. Spec: `{"type":"groups","container":"plate|bag|box|jar|cup","n":4,"each":3,"icon":"apple","counts":[3,3,2,3],"empty":false,"label_each":"[]","per_row":4}`. `counts` draws unequal groups; `empty:true` draws blank containers for the child to draw in; `label_each` and `total` can be answer boxes. Items placed on a neat grid inside the container, never scattered.

**F5. `array` (5: 14, 15, 16, 17, 18; optional in 13; about 3 h).** Rows and columns of dots, squares or icons. Spec: `{"type":"array","rows":3,"cols":4,"icon":"dot|square|apple","hide":[5],"shade_rows":[1],"pairs":false,"ring_left_over":false,"row_label":"[]","col_label":"[]"}`. `pairs:true` arranges counters two by two and rings the left-over one (Lesson 14). Cell 44 px minimum. Shares code with F4.

**F6. `line_up` and `round_table` (L11 only; about 3 h).** `{"type":"line_up","n":8,"names":{"3":"Ali"},"front":"left","marker":"door","labels":"ordinal|number|box|none","highlight":[3],"between":[3,9]}` draws children in a row with a door or arrow at the front, ordinal labels or answer boxes under them, an optional bracket for "between". `{"type":"round_table","seats":6,"names":{"1":"Ben"},"hide":[4]}` draws seats around a table with names and empty boxes. Direction must be unambiguous (a labelled front).

**F7. `picture_equation` (L19 only; about 4 h).** `{"type":"picture_equation","rows":[{"items":[{"sym":"circle","n":2},{"sym":"triangle","n":1}],"op":"+","total":"17"}],"values":{"circle":"[]"}}`. Symbols drawn as SVG: circle, square, triangle, star, heart, diamond. Each symbol has a distinct fill AND a distinct pattern or outline so it still reads in a grey print and for a colour-blind child. Up to 4 rows, 4 symbols per row, operators + − ×, answer boxes for the symbol values.

**F8. Two-colour ten-frame and dominoes (L13, and retro-fit for L5; about 2 h).** Extend `ten_frame` so counters can be two colours: `{"type":"ten_frame","filled":[7,0],"extra":[0,8]}` or `colours:["red","yellow"]`, plus `{"type":"domino","left":7,"right":7}` with true domino dot patterns.

**F9. 100 square overlap (L16, optional L14; about 1 h).** `hundred` already has `shade` (yellow) and `shade2` (mint); add an automatic third colour where a cell is in both, and a legend. A small two-circle Venn figure `venn2` for sorting (numbers in two tables) is optional.

**F10. `price_tag` (L20, optional; about 1 h).** A tag shape beside icons: `{"type":"price_tag","item":"pen","n":4,"price":"$20","each":"?"}`.

### 2.3 Question layout and blank types

**B3. True/False and multiple-choice question forms (6: 11, 14, 15, 16, 19, plus the check; about 3 h).** School papers use a Statement / True / False table with tick boxes ("put a tick in the correct box") and MCQ options (1) to (4) with a bracket at the right margin (`school_paper_wording_patterns.md` sections 1.2, 1.3; WORDING_GUIDE rule 23). Add question fields `tf:[{"s":"...","ans":"T"}]` and `mcq:{"options":[...],"bracket":true}`; the key lists the answer; the validator counts them as answer slots. Not in Term 1 (the paper review said to add a few MCQ items to home practice or the check).

**B4. Labelled step lines (4: 12, 18, 19, 20; about 1 h).** `steps:["Step 1","Step 2","Step 3"]` prints the labels before ruled lines. Term 1 audits L10 (W4) found that two unlabelled lines are not understood as steps by a 6-year-old.

**B5. Two figures in one question and a page-2 intro line (4: 12, 15, 16, 19; about 2 h).** Term 1 workbook visuals are one picture per question at 270 to 310 px (L3 audit: "S3 cannot show Mei and Ben"). Allow `visuals:[...]` side by side or stacked, and a `workbook.hint_p2` field (Lesson 6 fix list: no page-2 instruction line). Also a second `draw` box (L1 S7).

### 2.4 Cut-out kits (`workbook.kits`)

| Code | Kit type | Lessons | Spec |
|---|---|---|---|
| K1 | `groups_mat` | 14, 15, 17, 18, 20 | One A4 page: 6 large circles (plates, 70 mm) or 4 bags with a dotted cut line; also the missing Lesson 8 plates. Counters come from home. |
| K2 | `unit_strips` | 12, 18, 20 (opt. 17, 19) | Strips of 10 equal cells (17 mm cells so a strip fits the printable width), two colours, with dotted cut lines between cells so a strip can be cut to any length; about 8 strips per page. Alternative with no engineering: reuse the Term 1 tens bars and ones squares. |
| K3 | `ten_frame` | 13 (retro: 5) | Four frames of 2 by 5 and 10 red plus 10 yellow counters, cut lines. Closes the Lesson 5 audit gap. |
| K4 | `cards` + `people` | 11 | Ordinal cards 1st to 10th (the existing `cards` kit with labels, 10 cards) plus a strip of 10 cut-out people in 5 colours. |
| K5 | `dot_cards` | 13 (opt.) | Cards 1 to 10 with ten-frame or dice dot patterns. |
| K6 | `array_mat` | 15, 16 | A blank 5 by 8 grid, 20 mm cells, to lay counters on; reusable as an egg carton substitute. |
| K7 | `shapes` | 19 | Existing kit with a star and a heart added to circle, square, triangle (six of each, three fill patterns). |

Existing and sufficient: `hundred` kit (Lessons 14, 16), `cards` with `round` (dollar tokens and price tags for Lesson 20), `number_strip` (optional in 16), `base_ten` (12, 18).

### 2.5 Capabilities Term 2 does not need (kept for Terms 3 and 4)

Clocks, coins and notes with $ and cents, fractions, half and quarter shapes, 2D and 3D solids, picture graphs, cube stacks, fold and punch, calendars, Latin-square grids. Lesson 20 uses whole dollars only and needs no coin or note picture.

### 2.6 Order by number of lessons that need each item

| Rank | Item | Lessons needing it |
|---|---|---|
| 1 | B1 slot widths | all 10 |
| 1 | X2 term parameters | all 10 |
| 1 | X3 validator updates | all 10 |
| 4 | R1 pictures in practice | 9 |
| 5 | F1 table | 9 |
| 6 | F2 object icons | 8 |
| 6 | B2 sign circle and equation frame | 8 |
| 8 | R2 ordered multi-box answers | 7 |
| 9 | B3 True/False and MCQ | 6 (with the check) |
| 10 | F4 groups and K1 groups mat | 5 |
| 10 | F5 array | 5 |
| 12 | B4 labelled steps, B5 two figures | 4 each |
| 14 | F3 bar model | 3 required, 3 optional |
| 14 | K2 unit strips | 3 required, 2 optional |
| 16 | K6 array mat, R3 list answers | 2 each |
| 18 | F6, F7, F8, F9, F10, K3 to K5, K7, R4, R5, X1 | 1 each (X1 is mandatory for L20) |

## 3. Known Term 1 template gaps still open (checklist)

Status checked against the code as it stands (after commit 2379b77 and 8052ec5). Tick when fixed and re-verified on a Term 2 build.

- [ ] **Ten-frame kit page.** No printable ten-frame exists; Lesson 5's audit (finding 4) asked for one and the fix told families to rule two rows of five by hand. Needed by Lesson 13. Fix: K3. Where: `svg.py` `kit_figure`, new type `ten_frame`.
- [ ] **Plate figure and plates kit.** Lesson 8 audit finding 5: "no plate or balance picture"; the figure tools have no plate type. Needed by Lessons 14, 15, 17, 18, 20. Fix: F4 and K1.
- [ ] **Bracketed part labels.** `b_print.qbox` prints the part label as a bare `a` in a small tag (`.sl` in `hp/wb_style.css`); WORDING_GUIDE rule 18 and the Lesson 4 audit want "(a)". The deck already prints "a)". Fix: print "(a)" in `qbox`, the key and the guide; override `.sl` in `EXTRA` (the holiday course shares `wb_style.css`, do not edit it).
- [ ] **Look-back font size and layout.** `.lbk .r` is 13.5 to 14.5 px and the "I am still stuck" line sits under "Next time I will try" (Lessons 4, 5, 6, 7 and 10 fix lists). Fix: raise to at least 16 px, give "I am still stuck" its own line, and re-check page 5 fill (it is already 99 percent full in several lessons, so the Look-back may need to move to the back of page 4 or onto the exit ticket page's margin).
- [ ] **Variable blank widths.** Fixed 14 to 18 mm dashes (Lessons 4, 5 audits). Fix: B1.
- [ ] **Orphaned key heading.** `key_html` banners have no `break-after:avoid`, so a heading is left at the foot of a page (Lesson 1, 4, 6, 7 and 10 audits). Fix: `.banner{break-after:avoid}` and keep the first `.keybox` with its banner in `EXTRA`.
- [ ] **Box blanks on the home sheet.** `home_html` calls `blanks()` which does print `[]` boxes, and commit 8052ec5 reports box blanks on home, key and guide. Lesson 2's fix list still says home blanks print `___`. Open check: confirm on a rebuilt home sheet that `[]` prints as a box, that the box is not smaller than the workbook's (`.hm .boxb` is 26 px against 36 px), and that lesson texts use `[]` for single digits. Mark as probably fixed, verify on L11.
- [ ] **Mi calculator.** Five Term 1 workbook audits (Lessons 6 to 10) and all ten round-2 guide and deck audits flag that the Mi dolphin image appears to hold a calculator while AUTHORING says the program never shows a calculator. It is an owner-chosen image (never edited) on every workbook page 1, parent page, guide cover and the title slide. Needs an owner decision before the Term 2 build (question 6).

Additional Term 1 findings found while reading the audits, not on the owner's list:

- [ ] Investigation page has no table or grid figure (Lessons 1, 2, 8, 10 workbook audits). Fixed by F1.
- [ ] One picture per question at 270 to 310 px, so a two-person question cannot show both (Lesson 3 audit). Fix: B5.
- [ ] Only one `draw` box per question (Lesson 1 S7). Fix: B5.
- [ ] No page-2 instruction line field (`hint_p2`) (Lessons 6, 7). Fix: B5.
- [ ] Kit page spacing and an empty right quarter (Lesson 1 fix list) and tens bars with no gaps between bars (Lesson 5 fix list). Fix with the K-kit work.
- [ ] Home sheet page 2 only 43 percent full (Lesson 3). Fix: allow the parent "tips" or a second activity on page 2.
- [ ] Key "Watch for" list punctuation (Lesson 4) and the fixed sneak-peek answer wording on key page 3 (Lesson 6). Cosmetic.
- [ ] Bundle picture rendered smaller than the kit pieces (Lesson 7). Fix: width rule in `.vis`.
- [ ] `choice_words` detects only "Circle Yes or No", "Right or Wrong", "True or False"; three-way choices need explicit `choices` (works but easy to forget). Fix: validator message.
- [ ] Draw-stroke estimator is tuned to bundles. Fix: X3.
- [ ] Shared validator expects `line_mm` for the check block (Lesson 10). Fix: X1.
- [ ] The whole-term checks the Term 1 audits recommended (MCQ in the check, Siti as the error-spotter in every lesson, "explain why" prompts in Start here) have not been applied. Apply the MCQ and name-variety advice from the first Term 2 lesson.

### 3.1 Round-2 (guide, deck, safeguarding) issues that are template-wide and still open

The second-round guide and deck audits (`audit/GUIDE_DECK_AUDIT_L01` to `L10`) were committed while this document was written. Their shared items ([ST] in the audits) sit in the guide generator, the deck generator or the term-wide script text, so a Term 2 lesson built today would repeat them. Fix once in the generators or in a shared phrase library, then re-use.

- [ ] **"Papers to the camera so only you see it" is untrue in gallery view** (L4, L5, L8, L9, L10 audits). Needs an owner-approved procedure (spotlight, count of three accepting the group sees it, or fingers) and one wording in every script, guide and parent note.
- [ ] **Recording statement** is incomplete or absent from the spoken script and conflicts with the privacy notice (L4, L5). One shared opening line with the camera-off option.
- [ ] **"I am still stuck" has no route to the tutor** (L4, L5). Needs a shared in-session route (the tutor checks in the open session; no private chat).
- [ ] **Camera and desk logistics** are assumed, not taught (L4, L5, L8): one shared materials and set-up line (tilt the camera or a phone on books).
- [ ] **REC cues are said live with no framing** (L4, L5). Shared framing sentence in the generator.
- [ ] **Goodbye slide comes before the optional and menu slides** (L8, L9, L10). Move the end slide last in the deck builder.
- [ ] **No timer slide**, although the guide lists one in the tutor materials (L8, L10). Add a countdown slide element or remove the line.
- [ ] **Workbook, exit and look-back slides use 26 to 32 px text** (L1, L8), below the 34 px rule; check slide for the number items (L8 s-ws2 omitted the numbers).
- [ ] **Stray words in the script text**, such as "stamp the inquiry journal" (L8) and a Mi speech bubble overlapping the next-lesson card (L10).
- [ ] **Wrong working attached to named characters** ("Siti writes ...", "Ravi says ...") when a real child of that name may be in the group (L8, L10): use "A child writes" or a neutral name in Term 2.
- [ ] **Look-back time** (100 s in the guide, "Three minutes" on the slide) and the make-up recording has no chapter for the check (L10).
- [ ] **Check timing and privacy** (L10, High): see the risks below.

## 4. Risks, effort estimate, build order

### 4.1 Risks and lessons learned from Term 1

1. **Tier honesty.** Term 1 audits moved many items: contest items out of Start here, 3-digit numbers out of Start here (Lesson 3), three-step stories out of the check, explain-why prompts out of Start here and the exit ticket (rule 25). In Term 2 the likeliest repeats: "twice as many" and a hidden start in Lesson 18 Start here, a written reason in Lesson 14 Start here, "price of 7 from 3" in Lesson 20 Start here, the 3 and 4 tables in Lesson 16 Start here. Keep Start here to P1 content.
2. **Beyond-P1 statements.** Lessons 14, 16 (3s and 4s), 17 (remainders, ÷), 18 (times as many), 19 must say plainly in the tutor guide and parent summary that they go past the school Primary 1 syllabus on purpose, with no "MOE-aligned" wording (owner decision, 22 Oct 2026).
3. **Timing.** The Lesson 10 audit (W1) found the workbook part is 16 to 28 minutes, Start here alone is modelled at 15.5 to 19 minutes, so pages 3 to 5 are effectively home work. Term 2 lessons are picture-heavy; budget Start here at 5 or 6 questions and say on the page that Think harder and Go further are for home or next time. Lesson 20 loses 20 minutes to the check: the explore and mini-lesson must shrink and the workbook part becomes a short Start here.
4. **Answer slots and drawing load.** The validator fails a question with no slot and warns above 25 drawing strokes. Multiplication drawing ("draw 6 groups of 5" is 30 strokes) will trigger it; ask for rings and numbers, or give the groups pre-drawn (F4 empty containers).
5. **Wording.** Apply WORDING_GUIDE rules 11 to 25 from the start: story first, question second, picture between; "each", "groups of", "in all", "how many more ... than"; no method in the stem; no teaching sentence in a question; MCQ and True/False in home practice; numerals only for quantities. Run the wording review against the school-paper guide before the audit, as in Term 1, not after. The Henry Park P1 multiplication quiz is the paper to match for Lessons 15 to 18.
6. **Copy check.** The validator rejects any 7-word overlap with the SASMO and book texts. Draft problems in `g1_original_problems_draft.md` and `word_problems_g1_g2_original_draft.md` are for ideas only, and some (A12.1, 9.3) are close enough to textbook stock phrasing that a lightly reworded copy will fail; change context and numbers.
7. **Contest items.** Queue counting (11), transfer and sum-and-difference (12), common multiples (16), "twice as many" with a transfer (18), symbol equations (19) are tutor labels and live at Think harder; the plan's Think harder column already says so. Do not put the label on a child page.
8. **Syllabus flags.** The plan flags Lesson 13 as a new topic and Lesson 14 (odd/even is P2), Lesson 20 (an added lesson) as needing review. Put the review in `moe.note` of each. Odd/even and the 3 and 4 tables are P2, so say so rather than call them enrichment of P1.
9. **Shared runner change.** R1 to R5 edit `practice/public/practice.js`, which the original sample and possibly other levels use. Version the data (`"runner":2`) so nothing regresses, and re-run the Level 3 sample.
10. **Mid-term entrants.** Every Remember must re-teach with objects what it names (bars and squares, skip counting) and must not use a word defined only in Term 1 without defining it again. Lessons 12, 18, 19 and 20 depend on strips, groups and boxes; state the "safe to miss" line honestly (Lessons 15 to 18 build on one another).
11. **Check design.** The plan's section 5 says the check has 4 Start here, 4 Think harder and 2 Go further per term; the Term 1 check as built has 10 Start here items plus one optional Think harder stretch, within 20 minutes, after the audits. Follow what was built (question 5).
12. **Authoring documents are Term 1 specific.** `AUTHORING.md` lists "the 9 remaining lessons" and `LESSON_BRIEF.txt` says Lesson 1 is the pilot. A Term 2 brief (copy of the two plus this document, with the new figure names, the term parameters, the Term 2 check and the audit lessons) must exist before agents start.
13. **Parallel agents on shared files.** In Term 1 several agents wrote in the same folders; the only shared-file edits were by the template owner. Keep that rule. Template engineers should each own distinct files or functions (`svg.py` new functions appended, `b_print.py` EXTRA CSS) and commit small.
14. **Check timing and privacy (from the Lesson 10 round-2 audit, High).** The 20-minute check did not fit: modelled child time 11:40 in the guide against 16 minutes in the key and 22 to 28 minutes by the lessons' own per-question times; the exit ticket duplicated check item 10; the check began at minute 62 after 60 minutes of screen time; the number of the business WhatsApp is on slides and therefore in every recording; the photo marking of a drawn line depends on the family printing at 100 percent. For Term 2 either drop the Lesson 20 exit ticket and start the check earlier, or let children work at their own pace across pages, and re-time before building. The check also needs a recording chapter and a make-up route written once in X1.
15. **Fonts and symbols.** First build must confirm `×` renders in guide, deck, workbook and key PDFs (text extraction check with `pdftotext`), and that the symbol shapes in Lesson 19 are drawn SVG, not glyphs.

### 4.2 Effort estimate (agent-hours, not measured)

Per-lesson figures include write (data, checks, build, view every page), wording review, independent workbook audit and fix pass. Term 1 evidence: the whole term was written, reviewed, audited and fixed in about 6 hours of wall clock with parallel agents; the plan's own guess was 3 to 4 hours per lesson for the writing alone.

| Lesson | Write and build | Wording review | Audit | Fix pass | Total | Why |
|---|---|---|---|---|---|---|
| 11 | 3.5 | 0.5 | 1.0 | 1.0 | 6.0 | New queue figure, light maths; first Term 2 build |
| 12 | 4.5 | 0.7 | 1.0 | 1.3 | 7.5 | First bar strips, tier risk |
| 13 | 3.5 | 0.5 | 1.0 | 1.0 | 6.0 | New topic, syllabus check |
| 14 | 3.5 | 0.7 | 1.0 | 1.3 | 6.5 | Reasoning wording is the main risk |
| 15 | 4.5 | 0.7 | 1.0 | 1.3 | 7.5 | First multiplication, many pictures |
| 16 | 4.0 | 0.5 | 1.0 | 1.0 | 6.5 | Existing figures, contest item |
| 17 | 4.0 | 0.5 | 1.0 | 1.0 | 6.5 | Reading traps, left over |
| 18 | 5.0 | 0.7 | 1.0 | 1.3 | 8.0 | Strip plus groups plus two steps |
| 19 | 5.0 | 0.7 | 1.0 | 1.3 | 8.0 | New figure, original puzzles checked |
| 20 | 5.5 + 4.0 check | 0.7 | 1.5 | 1.8 | 13.5 | Hosts the 20-minute check and its key and note |
| **Total** | | | | | **76** | plus about 8 for term-wide audits and a trial lesson prep: about 85 |

Template engineering (section 2): X2 2, B1 2, X3 3, R1 to R5 14, X1 5, F1 5, F2 5, F3 6, F4 3, F5 3, F6 3, F7 4, F8 2, F9 1, F10 1, B2 2, B3 3, B4 1, B5 2, kits K1 to K7 about 5, Term 1 gap fixes about 4: about 75 hours if every item is built as specified, about 55 hours if optional items (F10, K5, K6, F9 Venn, F3 uses in 13, 17, 19) are deferred.

A Term 2 trial lesson with a tutor, review of the "new topic" flags and the term-wide second-round audit (guide, deck, home, parent, runner) are not in these numbers; allow another 10 to 15 hours.

### 4.3 Dependencies in the content

- Lessons 15, 16, 17, 18 form one chain (groups, tables, sharing, stories). Lesson 12 feeds 18 and 20 (strips). Lesson 8 (Term 1) feeds 14, 17, 19. Lesson 20 needs the answers of Lessons 11 to 19 fixed before the check can be written. The plan says a lesson must not assume the previous one except through Remember, so the chain is a build-order and wording-consistency dependency, not a content one.
- Shared wording to fix once and reuse: "groups of", "each", "in all", "left over", "how many more", the equation frame, the strip names.

### 4.4 Recommended build order and parallelisation

**Sprint A (day 0, about half a day, one engineer):** X2, B1, B2, X3 (a, b, f), bracket labels, orphan key heading, Look-back type size, `hint_p2`, F2 icon engine (first 12 icons), F6, K4. Then immediately write **Lesson 11** (cheapest figures, proves the Term 2 term parameters end to end, is the pilot for Term 2 conventions).

**Sprint B (in parallel with Lesson 11, two engineers):** F1 table, F4 groups, F5 array, K1, K6, F8, K3, F9, R1 (basic pictures) and R2.

**Wave 1 (after Sprint B, run in parallel, up to 5 agents):** Lesson 15 (pilot for groups and arrays; copy its conventions), then Lessons 16, 17, 13 and 14 in parallel as soon as 15's first build exists (they copy file layout and wording, not content). Lessons 13 and 14 do not depend on 15 for content.

**Sprint C (starts day 0 in parallel with B because F3 is the longest piece, one engineer):** F3 bar_model, K2, B4, B5, F7, K7. **Wave 2:** Lesson 12 (pilot for strips), then Lessons 18, 19 in parallel; Lesson 20's lesson body can be written in parallel with 18 once F3 and F10 exist.

**Sprint D (during Wave 2):** R3, R4, R5, X1.

**Wave 3:** after Lessons 11 to 19 have passed their fix pass, write the Term 2 check block and the Lesson 20 extras (X1), then the independent audits of Lesson 20 and the check, then a term-wide second-round audit (guide and deck, home and parent and practice, term-wide) as for Term 1.

**Which can be written first with the existing tools:** Lesson 16 comes closest (100 square, number line jumps, tiles all exist; it needs only a table, the overlap colour and the new blank tokens). Lesson 13 could start with the L5 workaround (families rule the frames) but should wait for K3. Lesson 11 is next if the queue picture is built first. Lessons 12, 18, 19 and 20 cannot start without F3 or F7.

**Expected elapsed time:** with eight to ten writing agents and three template engineers working as above, about 1.5 working days to a first full set of ten built lessons, a second day for audits and fix passes. If template work is done serially before any lesson starts, add about one more day.

## 5. Questions only the owner can answer

1. Multiplication reading order. Is "3 groups of 4" written 3 × 4 or 4 × 3 in your classes (the Henry Park quiz uses both "7 groups of 2" and "2 sevens")? Pick one and we use it in every frame.
2. May Lesson 17 show the ÷ sign (P2) as a label, or keep to words ("shared by", "put into groups of")?
3. Odd/even (Lesson 14, P2 content) and the 3 and 4 tables (Lesson 16, P2): keep them in Term 2 as planned, with the beyond-P1 statement, or make Lesson 14 an optional swap lesson as the plan's Term 2 note and open question 10 suggest?
4. Do we say "bar model" to families and children, or only "strips" (the syllabus never names bar models, schools do)?
5. Term 2 check: follow the built Term 1 pattern (10 Start here items plus one optional Think harder, 20 minutes, WhatsApp photo return) rather than the plan's 4 Start here, 4 Think harder, 2 Go further?
6. Mi: may we ask for an image of the dolphin without the calculator (or crop it) before Term 2 is built?
7. May the shared practice runner (`practice/public/practice.js`) be changed (pictures, ordered boxes, list answers), versioned so other levels keep working, or should Term 2 online practice stay text only?
8. Lesson 20 uses whole dollars before notes and coins are taught in Term 3. Fine as long as it never asks for notes or coins?
9. Papers shown to the camera: which procedure replaces "only you see it" (spotlight, count of three, or fingers), and who holds the business WhatsApp number and its photos? Both are in every Term 1 script and will be copied into Term 2 unless decided.
10. Is 25 minutes acceptable for the Lesson 20 check (the Term 1 audit says 20 does not fit), or should it move to a separate slot?
