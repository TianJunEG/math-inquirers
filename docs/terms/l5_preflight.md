# Level 5 pre-flight (lessons 1 to 40, ages 10 to 12, Primary 5)

Status: planning only, written 23 Oct 2026. No lesson, tool, template or output file was edited, and no shared file was touched. Level 1 (`term/l1/`: lessons 1 to 30 built, 31 to 40 in progress) is the model; no Level 5 term lesson is written and nothing has been tried with children. This document tells the people who will write the 40 Level 5 term lessons what each lesson is, what the templates must learn first, which holiday items must not be repeated, what went wrong at Level 1 and must not be repeated, which decisions the owner must make, and in which order to build. Every default is marked **[Default]**.

Sources read in full: `docs/terms/owner_decisions.md` (all entries), `docs/terms/l1_term2_preflight.md` and `docs/terms/l1_term3_term4_preflight.md` (the models), `docs/terms/l3_preflight.md` and the template, kit and Quest sections of `l2_preflight.md` and `l4_preflight.md` (for cross-level reuse of figure codes), `docs/terms/level_5_year_plan.md` (all four terms, the revision blocks, the SASMO table, the MOE verification block, the "Non-routine assignments" section, the matrix and the notes), `docs/books/p5_school_paper_patterns.md` and `p5_non_routine_catalogue.md` (wording, ranges, pictures, marks, 49 original examples), `docs/moe/syllabus_by_level.md` (P1 to P6, the year index and the "not in the syllabus anywhere" row), `docs/sasmo/g5_analysis.md` and `g5_original_problems_draft.md`, `term/l1/AUTHORING.md` (all passes, Terms 3 and 4 section), `WORDING_GUIDE.md`, `audit/TERM_WIDE_AUDIT.md`, `CUTOUT_AUDIT.md`, `FINAL_AUDIT_T1.md`, `FINAL_AUDIT_T2.md`, the Level 1 tool inventory (`term/l1/tools/figs2.py`, `figs3.py`, `svg.py` signatures, `b_quest.py` bans), and the holiday Level 5 content `p5/SPEC.md` and `p5/content/l1.js` to `l10.js` (every Start here, Think harder and Go further question of the ten holiday lessons was extracted and read). The word-problem analyses (`word_problems_g1_g2_*`) cover Grades 1 and 2 only and were not used.

Numbers quoted as "verified" were recomputed by brute force in `verify_l5_preflight.py` (appendix): **265 checks, all passed**. Lesson authors must still write their own `verify/lNN_checks.py`; nothing here replaces it. Check ids (`V7.2` and so on) point to the appendix; `Q` ids are Quest gate items; `K` ids are kit arithmetic.

## 0. Headline findings

1. **The holiday course already holds many of the year plan's own contest items, so "no reuse" is true by title and false by item.** The holiday course (H1 Million Puzzles to H10 Challenge Day) is the same ten strands as Term 1 to 3, and its question banks contain: the telescoping product 1/2 x 2/3 x ... x 99/100 and the digit-card fraction sums (H2), father-and-son ages and "give half and 4 more" chains (H3), a point on the top side of a rectangle (H4), painted cubes, a block stood in a tank and pouring back until the depths are equal (H5), a car park charged "for every half hour or part of it" and three shops with pack deals (H6), discount then GST, "find the whole after a discount" and 30% of 70 against 70% of 30 (H7), isosceles cases and angle chases (H8), matchstick squares, repeating beads, heads and legs, quiz scoring and digits used in page numbers (H9), and working backwards, counting rectangles in a grid, digits written and logic seating (H10). The plan's lesson 5 telescoping product, lesson 27 page-number digits, lesson 28 heads and legs and quiz points, lesson 30 quiz scoring, lesson 21 "40% of 60 against 60% of 40" and lesson 26 matchstick and bead patterns are therefore replaced here with new items of the same move. Section 3 is a lesson-by-lesson register of the closest holiday items, what each term lesson is barred from reusing and what is new. 19 of 40 lessons are Heavy overlaps. Owner decision D2.
2. **Four parts of the year plan are superseded by later owner decisions.** (a) Plan section 5 describes a 30-minute, 10-question check in lessons 10, 20 and 30 and in lesson 37 or 38 for Term 4; the owner replaced it on 22 Oct with Mi's Challenge Quest, a 20-minute game after the break, in lessons 10, 20, 30 **and 40**. (b) The plan titles lessons 10, 20 and 30 "Review and Challenge"; the validator bans the bare word "challenge" on child pages (only "Mi's Challenge Quest" is allowed), so the titles become "Term N Review and Mi's Challenge Quest" (D3). (c) The plan's "Review lessons choose a heuristic" content must now fit a 10-minute Explore and 9-minute Mini-lesson. (d) Plan open question 10 (is a term-end check acceptable to parents) is answered: it is a game with no paper marks.
3. **The plan's Think harder and Go further rows lean on SASMO ideas; the replacements below are new in context and numbers.** Candidates in `g5_original_problems_draft.md` are used as ideas only: stamps that cannot be made (lesson 28 uses 5c and 8c, then 7c, 10c and 12c, not the draft's 4c and 9c), pair rates of work (lesson 16 uses 12, 15 and 20 days, not the draft's 10, 15 and 12), digit cryptarithms (lesson 34 uses `ABC + BBB = DCCE` and `ABACD + CAEF = CFFCC`), and so on. The existing 7-word copy check against the SASMO files stays.
4. **Level 1's tools cover less than half of Level 5's figures.** Checked in `figs2.py`, `figs3.py` and `svg.py`: `number_line`, `bar_model`, `table`, `clock`, `calendar`, `grid` (dot polygons, mirror line), `cube_stack` (heights to 3), `network`, `picture_graph`, `hundred`, `objects` and `picture_equation` exist. Level 5 needs 22 figure items that do not (section 5): stacked fractions and mixed numbers in text and answer boxes (needed in at least 14 lessons), a geometry figure with equal-side ticks and angle arcs (GEO is 17 percent of the school items), dice and painted cubes, isometric dot paper, a tank with a divider, block or step, line, bar and pie graphs, growing pattern figures, a balance, colouring graphs and a few more. About 150 hours of Level 5 share if built from scratch; much of it is shared with the Level 2, 3 and 4 plans (section 5.6).
5. **42 percent of the school items need a picture and no picture was seen.** 965 of the 2279 recorded Primary 5 items were flagged as picture-dependent and the true share is higher because the OCR dropped figures silently (`p5_non_routine_catalogue.md` section 2). Every figure-dependent item in this plan is marked "wording unverified" until the owner supplies the pictures (D21). Angle diagrams, overlapping shapes on a grid, line graphs, views of cubes and tanks with dimensions are the five families.
6. **Printed workbooks are black and white; the books print every page at 94.3 percent.** Level 5 depends on pictures more than Level 1: shaded fractions, hatched bar models, graphs, solids, tiles, colouring puzzles. Every figure must carry its meaning in shape, label or hatch; colour is decoration for the soft copy. Colouring puzzles use letters (A to D), not colours, in the printed book. Everything that depends on a printed length (a ruler picture, a protractor, an area counted in squares of a stated size) must say "not drawn to scale" or give the numbers in text (CUTOUT_AUDIT F4).
7. **Words and topics that the MOE syllabus lacks anywhere.** The syllabus summary lists "prime numbers, negative numbers, probability, coordinates, speed, surface area, median/mode, pentagon/hexagon" as absent from the whole primary syllabus. Level 5 uses some of them (a number with exactly two factors, surface area of a cuboid, pentagon and hexagon angle sums, grid points). They are allowed only as Think harder or Go further items or inside the named Beyond item, with a one-line level note, and never at Start here (D12). Start here uses "numbers with exactly two factors" and "dots across and up", not "prime" and "coordinates".
8. **Level 1's recurring defects are known and must be designed out from lesson 1:** kit pieces that do not match the tasks, false "next lesson" materials lines, workbook numbers repeated from class, answers on the slide while the question is asked, paper hold-ups to the camera, family pages that print the global lesson number, a validator that fails on our own catalogue text. Sections 6, 7 and 10 turn each into a rule with a check.
9. **Cutting load is small: 146 pieces a year** (T1 29, T2 12, T3 59, T4 46; section 6) against 271 at Level 3, because children aged 10 to 12 draw and write more than they cut and the plan keeps most manipulatives at home. The heaviest pages are lesson 28 (21 play coins) and lesson 1 (13 tiles). Two books, 4 and 8, have no cutting.
10. **Seven lessons and half of an eighth have little or no school-paper evidence** (patterns section 3): 9 Two Groups and the Overlap, 33 Clocks and Calendars (durations only), 34 Logic Grids and Digit Puzzles, 35 Odd, Even, Remainders and Extremes, 38 Children Set the Problem, 39 Colouring, Cycles and Choices, 40 Year Showcase, and the isometric half of 19. They stay as the plan says, labelled beyond school, each with a named swap candidate (D13). Lesson 35 is still the most overloaded (KIV) and lesson 39 the thinnest.
11. **Year-end exams fall in Term 4.** P5 pupils sit end-of-year papers in late Oct and Nov, so Term 4 attendance dips (plan open question 9). The plan's Term 4 is the lightest in new content; lesson 39 is the safest to skip, 37 next, and lesson 40 holds the Quest and the showcase, which a recording cannot replace (make-up route, section 8).
12. **Estimate:** about 391 agent-hours for the 40 lessons (write, wording review, independent audit, fix pass, four term-wide audits and one 40-lesson sweep) and 141 to 193 hours of template engineering, so roughly 532 to 584 hours; at the Level 1 pace (eight to ten writers, three engineers) about 9 to 11 working days from Sprint A to an audited Term 4 (section 13). Hours are estimates from Level 1 documents, not measurements.

## 0.1 Assumptions made (change them if wrong)

- **Format.** 40 lessons of 90 minutes (owner decision of 23 Oct, "then work with 90mins"), groups of up to 8, online, ages 10 to 12, Primary 5 Standard track. The Foundation track (MOE pp. 45 to 50) is not covered and is not claimed. Files are `term/l5/lessons/l01.json` to `l40.json`; `level` 5, `term` 1 to 4, `lesson` 1 to 40, `lesson_in_term` 1 to 10, `id` `l5-t1-01` ... `l5-t4-40`, practice keys `l5t1l01` ... `l5t4l40` (the level prefix is new because the shared runner already holds `t1l01` for Level 1). Family pages print "Level 5 Term 2 Lesson 4", never "Lesson 14 of 10". The leak check allows "Lesson 1" only where `lesson_in_term` is 1.
- **The 11-part skeleton as built at Level 1:** Opening 2, Remember 6, Sneak-peek 4, Explore 16, Mini-lesson 10, Break 4, Workbook 28, Talk 6, Exit 6, Look-back 3, Flex 5 (Opening may be 4 with Explore 14). Quest lessons (10, 20, 30, 40): Opening 2, Remember 6, Sneak-peek 4, Explore 10, Mini-lesson 9, Break 4, **Quest 20 at minutes 35 to 55**, Workbook 25, Talk 4, Look-back 2, Flex 4 = 90; the exit ticket is not live.
- **Tiers.** Start here 6 questions (workbook pages 1 and 2, at most 20 modelled minutes for a middle child), Think harder 4 (page 3), Go further exactly 3 (page 4), one Investigation (page 5) with an easy first step, kit page 6. Start here is a Primary 5 skill (or earlier) with scaffolding wherever the school teaches it later; Think harder carries the taught idea in a new setting **and every contest-style item** (owner decision 6); Go further is extension and the labelled P6 previews. No non-routine item at Start here (owner rule of 23 Oct). Labels are neutral and never shown as ranks. Part labels (a), (b): at Think harder and Go further part (b) uses part (a), as in the school papers.
- **Named beyond-syllabus item in every lesson** (owner rule, 23 Oct): one named puzzle at Think harder or Go further, never Start here, original, with a tutor-only `beyond` field `{name, where, text, parent}` and a one-line level note ("Primary 6 idea", "secondary idea", "not a syllabus topic"). It takes one of the Think harder or Go further slots; it is not an extra question. The child-facing name is a puzzle title and never carries the word "challenge".
- **Mi's Challenge Quest** in lessons 10, 20, 30, 40 (owner decisions of 22 Oct): a game, no scores, marks, ranking or visible timer, no word "test" or "exam" on any child or parent page (`BAN_FAMILY` in `b_quest.py`), private paper, the tutor keeps private notes for one line per parent, photos returned by the parent to the business WhatsApp (+65 9880 5962, never on slides). Eight gates and one optional cave (section 8). Ten- to twelve-year-olds know what a test looks like, so the Quest page uses a map-and-gates story and pairs; the tutor never says "check".
- **Books.** Printed black-and-white 5-lesson books issued on payment: Book k holds lessons 5k-4 to 5k (eight books). The Quest Log (4 pages) sits in Books 2, 4, 6, 8 (lessons 10, 20, 30, 40 are the last lesson of those books). Kit pages are on a front page with a blank back; soft copies stay colour. [Default] both books of a term are issued with the first payment (D11 at Level 1).
- **Wording** follows `WORDING_GUIDE.md` with the Primary 5 changes in section 1.1.
- **Cast.** Mei, Ali, Ben, Siti, Ravi, Kumar, Aisha, Wei, Jenny, Lily, Jamie, Ray, Amelia, Jason, plus Zoe, Kai, Maya, Talib, Dev, Cara, Hana, Rui, Dina. Wrong working is attributed to "a child" or "a child in another class", never to a cast name (Level 1 audit).
- **Calculators.** None in any lesson, and Mi never shows one. The holiday explore (H1) asks every child to have a calculator, and the P5 end-of-year Paper 2 allows one in 2020 to 2024, so this is a real choice (D8).
- **Scissors.** [Default] a grown-up, or the child with a grown-up, cuts the kit before the lesson; nobody cuts during a lesson, with one exception: lesson 15 (Cut and Rearrange), where the child cuts a paper parallelogram and trapezium in the Explore (D5).
- **Ruler, protractor, tape.** [Default] a 30 cm ruler is listed from lesson 7 on and a protractor from lesson 8 (every Primary 5 child has both); tasks are written so that the scale of the printed page does not matter, and every figure page says "not drawn to scale" where it is not.
- **Mi on the page.** [Default] Mi appears on the title and goodbye slides, the Quest and the parent page only (older children, Level 1 rules otherwise: no numbers or answers in Mi's speech, no calculator image once `mi_dolphin_nocalc.png` is supplied).

## 1. Lesson specs

### 1.0 Field order, holiday codes and the named beyond item

Every spec uses this order: big idea, strand and page references with the **holiday boundary**, objective, prerequisites, Remember warm-up (three items, re-taught with objects or pictures), Start here / Think harder / Go further outline with question counts, the **Beyond (named)** puzzle, non-routine work (type, tier, check id), number ranges, home materials, kit with piece counts, figures, misconceptions, template needs (codes from sections 5 and 6). "Beyond P5" labels follow `docs/moe/syllabus_by_level.md` (page numbers are PDF pages).

Holiday codes used throughout: **H1** Million Puzzles, **H2** Fraction Feats, **H3** Before and After, **H4** Triangle Areas, **H5** Volume Vault, **H6** Rate Racers, **H7** Percentage Puzzles, **H8** Angle Chasers, **H9** Pattern Generalisers, **H10** Challenge Day. Holiday graduates start Term 1, 2 or 3 (owner decision 4), so a graduate must not meet an item from `p5/content/lN.js` again; the Remember warm-up may revisit a holiday topic once (owner rule: spiral in warm-ups only). In item references, the core, stretch and challenge banks of each holiday are written as "H5 core 4", "H5 stretch 9", "H5 challenge 9" in the register in section 3.

Check ids `Vn.k` are in the appendix. Examples are original: the numbers differ from the catalogue examples (`EX-...`), from the SASMO drafts and from the holiday banks. The owner's private file of school questions (`docs/books/private_p5_papers/`) was not copied from.

### 1.1 Level 5 wording deltas from the Level 1 guide (from `p5_school_paper_patterns.md` section 5)

Rules 1 to 25 of `WORDING_GUIDE.md` still apply; Primary 1 rule 25 (the papers test numbers to 40, "say why" is enrichment) is replaced by: the papers test numbers to 7 digits, 3 to 5 mark multi-step problems with parts (a) and (b), "true, false or not possible to tell", and a few drawing tasks. Explain-why prompts stay out of Start here and the exit ticket. Changes: (a) children read their own questions; the tutor reads a stem aloud only for a Think harder item with a new word and for every Quest gate once; (b) section instructions in paper style ("Show your working clearly." "Write your answers in the units stated."); (c) two-part items: a short stem, then (a) and (b), where (b) uses (a); (d) fixed phrases: "Express your answer in the simplest form." "correct to the nearest tenth", "Give your answer in kg and g", "How many more", "altogether", "times as many", "of the remainder", "What fraction of the ...", "What percentage of the ..."; (e) money $4.75 and 80¢, GST 9 percent (an older-paper practice item may say 7 percent and must say so), "inclusive of GST"; (f) time 3:20 pm and 24-hour 2150, accept 3.20 p.m. and 2150 hours; (g) geometry: "identical", "divided into", "joined to form", "ABCD is a rectangle", angles written angle ABC and 114°, "Find angle ...", and the line "The figure is not drawn to scale." on every figure page; (h) the statement item: "Each statement is either true, false or not possible to tell. Tick one box for each." with all three choices in the stem; (i) no stem names its tool at Go further; a Think harder stem may say "Draw a model" for a type that is new in that term (the papers almost never do); (j) no marks printed on child pages; an "Ans:" frame with the unit after the line and a "Working" box on two-step items; (k) fractions are stacked and mixed numbers have a whole-number box and a fraction; (l) the words "prime", "coordinates" and "pentagon" are not used at Start here (finding 7).

### 1.2 Term 1: Number and Fractions (lessons 1 to 10)

Can a new child join cold? Yes: the warm-ups cover Primary 4 recall (place value to 100 000, factors and multiples of 1-digit numbers, mixed numbers and improper fractions, decimals to 3 places, base and height, angle notation). Holiday graduates meet the holiday topics only in the first six minutes (H1 place value, H2 fraction as division, H3 fraction of a remainder, H4 half base times height, H8 angle facts, H10 choose a start). Lessons 4 and 5 should be made up, not skipped, because Terms 2 and 3 use fractions; **lesson 9 is the safest to skip** (nothing later needs it); hardest to miss: 1, 4, 5, 8. Lesson 10 hosts the Quest and cannot be skipped lightly (the make-up route is the Quest at the make-up slot, section 8).

#### Lesson 1. Shifting Places

- **Big idea.** Multiplying by 10 moves every digit one place to the left; "add a zero" is a shortcut for that, not the reason.
- **Strand.** MOE P5 Whole Numbers: numbers to 10 million; multiply and divide by 10, 100, 1000 and their multiples without a calculator (p. 41). P4 place value to 100 000 and rounding (p. 37). Contest tag: digit puzzles. **Holiday boundary (H1):** H1 built 7-digit numbers from digit cards (closest to a target, greatest and smallest), digit-sum riddles, rounding to the nearest thousand with ranges, estimates by rounding and bracket targets. Lesson 1 sets none of: closest to a target, greatest or smallest 7-digit number from seven cards, 7-digit digit-sum riddles, palindromes, 1 000 000 as a product of numbers without zeros, a heart beating a million times, the digits written from 1 to 1000. The bracket half of H1 returns in lesson 3.
- **Objective.** Read, write, compare and order numbers to 10 million; multiply and divide by 10, 100, 1000 by shifting digits on a mat; multiply and divide by multiples of powers of ten (x 200, / 500, x 300, / 4000); round to the nearest ten thousand. Think harder: multiples of powers of ten in a chain; "times as many" with a change; smallest even number from digit cards. Go further: the Beyond puzzle; pose a number.
- **Prerequisites.** Primary 4: place value to 100 000.
- **Remember (6 min).** (1) Say 3 408 050 in words and give the value of the 4 (P4). (2) Round 46 380 to the nearest thousand (P4). (3) Spiral from H1: is every 7-digit number greater than every 6-digit number (one line, yes).
- **Start here (6).** (1) Write 6 305 040 in words and numerals (new numbers). (2) Put five numbers to 10 million in order, smallest first. (3) Slide the digit tiles to find 4 207 x 100 and 530 000 / 1000 (V1.1). (4) Multiples of powers of ten: 36 x 200 = 7 200 as 36 x 2 x 100; 45 000 / 500 = 90 (V1.1). (5) Round 2 748 316 to the nearest ten thousand and to the nearest hundred thousand. (6) A story: a school prints 2 500 sheets a day; how many in 40 days (100 000, V1.8).
- **Think harder (4).** (1) 18 x 3 000 = 54 000 and 7 200 000 / 4 000 = 1 800 (V1.1), with a missing-number box: 7 200 000 / [ ] = 24 000 (V1.7). (2) The stadium has 5 times as many seats as the hall and together they have 36 000; seats are added to the hall until the stadium has 3 times as many as the hall; how many were added (hall 6 000, stadium 30 000, 4 000 added, V1.3). (3) Use each of the digits 6, 0, 9, 4 once to make the smallest even 4-digit number (4 096, V1.4). (4) True, false or not possible to tell: "multiplying by 1 000 moves every digit three places to the left".
- **Go further (3).** G1 **Beyond (named): "Cross Out a Digit".** Sam crosses out the last digit of a number and the number is now 2 826 smaller; find the number (two answers: 3 139 and 3 140, V1.2). Level note: place-value reasoning with a hidden digit; the same idea as 9 units and a digit, not a syllabus topic. G2 Write one number that rounds to 400 000 to the nearest ten thousand, has digit sum 13 and ends in 7 (for example 400 117, V1.5); many answers are right. G3 A number is multiplied by 300 and the answer is 7 200 000; find the number and check it by shifting (24 000, V1.7).
- **Non-routine.** LIST T (V1.4), EQ T (V1.3), POSE G (V1.5), LOG G (V1.2).
- **Numbers.** Whole numbers to 10 000 000; multipliers 10, 100, 1 000, 20, 200, 300, 4 000; no decimals (they are shifted in lesson 6). Numbers are written with spaces: 4 030 205.
- **Home materials.** Pencil, plain paper. The shift mat is in the book; no printer: write digits on scraps of paper.
- **Kit (KT1 `shift_tiles`, one page, 13 pieces to cut).** 13 digit tiles (0 four times, 1 to 9 once each); the 8-column shift mat is printed, not cut. Contract: a task uses at most 8 tiles with at most four zeros and no repeated non-zero digit; supplied 13, maximum used 8. 6 and 9 are underlined.
- **Figures.** `place_mat` (Y1) with shift arrows; numbers in text need no figure.
- **Misconceptions.** Writing 3 000 040 as 300 040 (lost place-holding zeros); dividing by 1 000 by deleting three digits instead of moving the point; reading 36 x 200 as 36 x 2 + 100; saying the 4 in 4 207 "is 4" rather than 4 000; in the cross-out puzzle forgetting that the crossed-out digit can be 0.
- **Needs.** Y1, KT1, RN10 (numbers with spaces accepted as 3 600 000 or 3600000).

#### Lesson 2. Factor Finders

- **Big idea.** Factors and multiples explain why a calculation works and how things pack.
- **Strand.** MOE P4 Factors and multiples: test whether a 1-digit number is a factor of a number within 100, common factors, multiples of 1-digit numbers, common multiples of two 1-digit numbers (2.1 to 2.5, p. 37). Divisibility tests are not a named outcome: digit sums for 3 and 9 and last digits for 2, 4, 5 are taught as enrichment. Contest tag: divisibility, remainders (SASMO 6 of 75, two a year). **Holiday boundary:** there is no holiday factors lesson; touched only by H5 core 2 (the rectangles made from 12 cubes), H10 stretch 6 (the smallest number above 1 with remainder 1 when divided by 2 to 6) and the digit-sum clues in H1. Barred: rectangles from 12 or 60 or 64 cubes, "remainder 1 when divided by 2, 3, 4, 5 and 6", 7-digit digit-sum riddles.
- **Objective.** List factors and multiples in order; find common factors and common multiples; solve packing and sharing stories (the greatest number of bags, the smallest number shared); use digit sums for 3 and 9. Think harder: missing digit; multiples in a range; packing; true, false or not possible to tell. Go further: Locker Parade; riddle; counterexample.
- **Prerequisites.** Primary 4 factors and multiples; tables to 12.
- **Remember (6 min).** (1) Write all the factors of 24 in pairs (P4). (2) The first five multiples of 6 and of 8 and the first number in both. (3) Spiral from H1: the digit sum of 7 346 (20).
- **Start here (6).** (1) List all the factors of 36 (nine) and of 48 (ten) (V2.1). (2) Common factors of 24 and 36 (1, 2, 3, 4, 6, 12); the greatest is 12 (V2.1). (3) The first three common multiples of 4 and 6 (12, 24, 36, V2.1). (4) Is 7 482 a multiple of 3? Of 9? Use the digit sum (21: yes and no, V2.10). (5) Multiples of 7 up to 70. (6) A story: 12 pupils sit in equal rows; list every way (six).
- **Think harder (4).** (1) Find the missing digit so that 5 [ ] 7 2 is a multiple of 9 (4, V2.9); which digits make 3 [ ] 4 8 a multiple of 12 (0, 3, 6, 9, V2.9). (2) (a) 48 mangoes and 72 apples are packed into identical bags with none left over: the greatest number of bags (24) and what is in each bag (2 and 3, V2.3). (b) Sweets can be shared equally among 9 children or among 12 children: the smallest number above 200 (216, V2.4). (3) How many multiples of 7 are there from 100 to 500 (57)? How many of them are not multiples of 14 (29)? (V2.6). (4) A whole number has exactly five factors. True, false or not possible to tell: it is a square number (true); it is even (not possible to tell); it is less than 100 (not possible to tell) (V2.2).
- **Go further (3).** G1 **Beyond (named): "Locker Parade".** 100 lockers are shut. Pupil 1 opens every locker, pupil 2 changes every 2nd locker (open becomes shut, shut becomes open), pupil 3 every 3rd, and so on to pupil 100. Which lockers are open at the end (the 10 square numbers, V2.7)? Why? Level note: factor pairs and square numbers; the proof that factors come in pairs is a secondary idea. G2 I am a 2-digit multiple of 8, my digits add up to 10 and dividing by 7 leaves 1 (64, V2.5). G3 Tom says a number that is a multiple of 4 and of 6 must be a multiple of 24. Find a counterexample (12, V2.8).
- **Non-routine.** LIST T (V2.3), LIST G (V2.4), LOG T (V2.2), LOG G (V2.5), EXP G (V2.8), PAT G Beyond (V2.7).
- **Numbers.** Factors of numbers to 100; packing numbers to 100; multiples in ranges to 500; digit tests on 4- and 5-digit numbers. The word "prime" is not used at Start here (it is absent from the syllabus); "a number with exactly two factors" is used at Think harder.
- **Home materials.** Pencil; up to 36 buttons or counters for arrays (optional); squared paper is in the book.
- **Kit.** None cut. A printed factor-pair sheet.
- **Figures.** `table` (factor pairs) exists; no new figure.
- **Misconceptions.** Leaving out 1 and the number itself; swapping factor and multiple; using the digit sum of 9 as a test for 3 only; counting 0 as a multiple; an off-by-one when counting multiples in a range; thinking the greatest number of bags is the smallest common multiple.
- **Needs.** RN13 (list answers in any order), RN10.

#### Lesson 3. Smart Calculation

- **Big idea.** Rearranging a calculation keeps its value, and the order of operations is a rule everyone agrees to.
- **Strand.** MOE P5 Whole Numbers: order of operations without brackets (2.2) and with brackets (2.3), new at P5 and not a P4 spiral (p. 41). Contest tag: computation and parity (SASMO 5 of 75: 19-1, 19-2, 20-1, 21-1, 21-2). **Holiday boundary (H1):** H1 stretch 2, 8, 9 and challenge 5, 7 put brackets to hit targets (2 + 3 x 4 + 5 to make 25 and 29; digits 2, 3, 5, 7 to make 29, 31, 100; four 4s; 1 2 3 4 5 to make 100; the biggest value of 1 + 2 x 3 + 4 x 5 + 6). Barred: those stems and digits. New: regrouping and cancelling, parity of a result, choosing the expression for a story, counting the values of all bracketings.
- **Objective.** Find the value with and without brackets; regroup to a round number or a common factor; say whether a result is odd or even without calculating; write one expression for a story. Think harder: regroup, choose the expression, parity. Go further: Bracket Bonanza; make 24.
- **Prerequisites.** Primary 4: the four operations on whole numbers; multiplication tables.
- **Remember (6 min).** (1) 24 - 6 / 3 x 2 and the rule: brackets first, then x and / left to right, then + and - (V3.1). (2) 98 x 5 as 100 x 5 - 2 x 5. (3) Spiral from H1: (5 + 3) x 8 and 5 + 3 x 8 are different (64 and 29).
- **Start here (6).** (1) 24 - 6 / 3 x 2 = 20 and (24 - 6) / 3 x 2 = 12 (V3.1). (2) 18 + 6 x 5 - 12 / 4 = 45 (V3.7). (3) 7 + 3 x (12 - 4) = 31 (V3.7). (4) 100 - (35 + 15) / 5 = 90 (V3.7). (5) 48 / 6 x 2 = 16, left to right (V3.7). (6) Three notebooks at $4 and two pens at $2: write one expression and find the cost ($16, V3.7).
- **Think harder (4).** (1) 47 x 36 + 47 x 64 = 4 700 and 99 x 25 = 2 475 (V3.2). (2) (a) Zoe buys 6 cups at $4 and 3 plates at $9 and pays with $60: choose the correct expression for her change from three; (b) the change ($9, V3.5). (3) Without calculating, is (37 x 25) + (18 x 44) odd or even (odd)? And (37 x 25) + (19 x 44) + 3 (even) (V3.3). (4) True, false or not possible to tell: the value of 12 + 18 x 5 is 150 (false: 102).
- **Go further (3).** G1 **Beyond (named): "Bracket Bonanza".** 48 / 6 x 2 + 4 - 1 can be bracketed in 14 ways; how many different values do they give (9, V3.4)? Level note: counting bracketings is Catalan-number territory, a secondary idea; the child only lists and counts. G2 Use each of 3, 4, 6, 9 once, with + - x / and brackets, to make 24 (one way: ((3 + 9) x (6 - 4)); there are several, V3.6); many answers are right. G3 Cancel before you calculate: (45 x 36) / (15 x 12) = 9 (V3.8).
- **Non-routine.** EXP T (V3.5), LOG T (V3.3), POSE G (V3.6), WAYS G Beyond (V3.4).
- **Numbers.** Whole numbers to 5 digits; brackets used once or nested once; no powers, no negative numbers.
- **Home materials.** None; pencil.
- **Kit.** None cut.
- **Figures.** None new (`table` for the bracketing list).
- **Misconceptions.** Working strictly left to right; doing / before x; ignoring brackets; "cancelling" across an addition sign; thinking odd x even is odd.
- **Needs.** None new.

#### Lesson 4. Mixed Numbers and Sharing

- **Big idea.** A fraction is a division, and a share can be a mixed number.
- **Strand.** MOE P5 Fractions: a whole number divided by a whole number gives a fraction (1.1); add and subtract mixed numbers (2.1) (p. 41). P4 mixed numbers and improper fractions, add and subtract fractions with denominators not above 12 (1.1, 3.1, p. 37). **Holiday boundary (H2):** H2 core 1 to 3 (3 bars among 4 friends, 1/2 + 1/4 of a pizza, 12 slices), stretch 4 and 6 (4 l into 6 bottles, 3/4 m into 3), core 4 and 5, stretch 1, 3, 5 to 9, challenge 1 to 9. Barred: all of these, especially sharing 3 bars among 4, 4 litres into 6 bottles, 5 pizzas among 12 children, unit-fraction sums, 1/2 - 1/3 patterns, 5/6 against 6/7, and fractions between 2/5 and 1/2.
- **Objective.** Write a division of whole numbers as a fraction and as a mixed number; convert between mixed numbers and improper fractions; add and subtract mixed numbers, regrouping a whole; hours and minutes as mixed numbers. Think harder: regrouping, a measurement story, fraction of the rest then what is left. Go further: Halves Forever; two quantities related by fractions.
- **Prerequisites.** Primary 4 mixed numbers and improper fractions.
- **Remember (6 min).** (1) 3/4 of 12 (P4). (2) 17/5 as a mixed number (3 2/5, V4.1). (3) Spiral from H2: 3 bars shared among 4 gives 3/4 each.
- **Start here (6).** (1) Share 7 pizzas among 3 children; draw it: 2 1/3 each (V4.1). (2) 17/5 = 3 2/5 and back (V4.1). (3) 3 1/5 + 2 3/5 (no regrouping). (4) 5 4/7 - 2 2/7. (5) 23 / 4 as a mixed number (5 3/4, V4.1). (6) 2 3/4 hours in hours and minutes (2 h 45 min).
- **Think harder (4).** (1) 3 1/4 - 1 3/8 = 1 7/8 (V4.2). (2) 2 5/6 + 1 3/4 = 4 7/12 (V4.2). (3) A shop had 560 tickets. It sold 3/7 of them on Saturday and 3/8 of the rest on Sunday: how many were left (200, V4.3)? (4) A tank held 8 1/4 litres; 2 5/6 litres were used and 1 1/2 litres were added: how much now (6 11/12 litres, V4.7)?
- **Go further (3).** G1 **Beyond (named): "Halves Forever".** Eat half a cake, then half of what is left, then half again: after 5 bites 1/2 + 1/4 + 1/8 + 1/16 + 1/32 = 31/32 has gone (V4.5); how much is left, and will the cake ever be finished? Level note: the idea of a sum that never reaches 1; secondary. G2 3/4 of the red beads equal 2/3 of the blue beads and there are 56 more blue beads than red: how many beads altogether (952; red 448, blue 504, V4.4)? G3 A chain of three mixed numbers with a missing number, solved with a bar model.
- **Non-routine.** MULTI T (V4.3), CTX T (V4.7), EQ G (V4.4), PAT G Beyond (V4.5).
- **Numbers.** Denominators up to 12; mixed numbers up to 10; unit-chain totals up to 1 000.
- **Home materials.** Plain plates or the cut circles; pencil.
- **Kit (KT2 `pizza_circles`, one page, 8 pieces to cut).** 8 circles of 11 cm with fold lines. Contract: the Explore shares 7 pizzas among 3 children; supplied 8, maximum used 7. No printer: paper plates.
- **Figures.** Stacked fractions and mixed numbers (Y2), `bar_model` with fractions (Y3).
- **Misconceptions.** Writing 7 / 3 as 2 R 1 and stopping; adding the denominators; forgetting to regroup (3 1/4 - 1 3/8 as 2 1/8); converting 3 2/5 to 6/5; taking the half of the whole instead of half of what is left.
- **Needs.** Y2, Y3, KT2, RN9 (mixed-number answers).

#### Lesson 5. Fractions of Fractions

- **Big idea.** "Of" means times, and a fraction of a fraction is a smaller part.
- **Strand.** MOE P5 Fractions: multiply a fraction by a whole number (2.2), a proper fraction by a proper or improper fraction (2.3), two improper fractions (2.4), a mixed number by a whole number (2.5) (p. 41); dividing a fraction by a whole number is P6 (p. 43). **Holiday boundary (H2, H3):** H2 core 4 and 5 (3/5 of 15; half of half a cake), stretch 2, 8 (1/3 then 1/4 of the rest; 7/8 of 24), stretch 9 and challenge 5 (digit cards 1, 2, 3, 4 and 1, 3, 5, 7 for sums and differences of fractions), challenge 2 (the product 1/2 x 2/3 x ... x 99/100), challenge 3 (cookies by 1/2, 1/3, 1/4); H3 core 3, stretch 1, challenge 8 (give 1/2 and 4 more, twice). Barred: those items and digits. The plan's Go further telescoping product is H2 challenge 2 and is replaced by Half-Way Squares.
- **Objective.** Multiply fractions with an area model; cancel before multiplying; multiply a mixed number by a whole number; solve fraction-of-a-remainder stories with a bar model. Think harder: unit chain, digit cards for a product, a fraction relation between two bars. Go further: backwards chain; Half-Way Squares.
- **Prerequisites.** Primary 4 fraction of a set; lesson 4 is not assumed.
- **Remember (6 min).** (1) 2/5 of 30 (12). (2) Draw 1/2 of 1/3 of a rectangle: what part of the whole (1/6). (3) Spiral from H2: 5/6 of 12 (10).
- **Start here (6).** (1) 3/4 x 12 = 9. (2) 2/3 of 3/4 on an area model: 1/2 (V5.1). (3) 5/6 x 9/10 with cancelling: 3/4 (V5.1). (4) 4/6 x 3/8 in the simplest form: 1/4 (V5.7). (5) A bar model: 1/3 of $60 is spent, then half of the rest. (6) A story: 2/5 of a 30 m rope is used; how much is left.
- **Think harder (4).** (1) 2 3/4 x 6 = 16 1/2 (V5.1). (2) Use the digits 2, 4, 5, 9 once each to make two proper fractions with the greatest product (5/9 x 2/4 = 5/18) and the least product (2/5 x 4/9 = 8/45) (V5.2). (3) (a) Dina spent 3/5 of her money on a game and 1/4 of the rest on a snack; she had $27 left: how much did she have at first ($90)? (b) How much more did she spend on the game than on the snack ($45) (V5.4)? (4) 3/5 of the red beads equal 3/4 of the blue beads and there are 18 more red than blue: how many of each (red 90, blue 72, V5.6)?
- **Go further (3).** G1 **Beyond (named): "Half-Way Squares".** 2 1/2 x 2 1/2 = 6 1/4 and 7 1/2 x 7 1/2 = 56 1/4: find the pattern n 1/2 squared is n x (n + 1) + 1/4 (V5.3); use it to find 75 x 75 = 5 625 in your head (V5.3). Level note: an algebraic identity shown by examples; secondary. G2 Mei gave away 1/3 of her stickers and 2 more, then half of the rest and 1 more, and had 6 left: how many at first (24, V5.5)? G3 What is 1/2 of 1/3 of 1/4 of 240 (10, V5.8)? Explain with a bar.
- **Non-routine.** MULTI T (V5.4), LIST T (V5.2), EQ T (V5.6), BACK G (V5.5), PAT G Beyond (V5.3).
- **Numbers.** Denominators up to 12; products that cancel; mixed numbers with a whole number multiplier up to 12.
- **Home materials.** Pencil, squared paper.
- **Kit.** None cut. The area-model grid is printed.
- **Figures.** Area-model fractions and stacked fractions (Y2), `bar_model` (Y3).
- **Misconceptions.** Multiplying numerators and adding denominators; multiplying only the whole part of a mixed number; reading "of the remainder" as "of the whole"; cancelling a numerator with a numerator.
- **Needs.** Y2, Y3, RN9.

#### Lesson 6. Decimal Sense

- **Big idea.** A decimal is a fraction written in tenths, hundredths and thousandths.
- **Strand.** MOE P5 Decimals: multiply and divide decimals (to 3 places) by 10, 100, 1000 and multiples (1.1); convert a measure to a larger or smaller unit in decimal form (1.2); Fractions 1.2 express fractions as decimals (p. 41). P4 decimals to 3 places, add and subtract to 2 places (p. 38). **Holiday boundary:** no holiday decimal lesson; decimals appear in H6 core 6 (nuts at $1.50 per 100 g), H7 (GST) and H5 core 6 (2.5 l in ml). Barred: those. Light overlap.
- **Objective.** Compare and order decimals to 3 places; change a fraction to a decimal and back; multiply and divide by 10, 100, 1 000; round to the nearest tenth. Think harder: sum and difference; rounding bounds; a decimal between two others. Go further: Never-Ending Decimals; a decimal unit chain.
- **Prerequisites.** Primary 4 decimals; lesson 1 (shifting) is recalled.
- **Remember (6 min).** (1) 3/4 = 0.75 and 3/8 = 0.375 (V6.2). (2) Order 0.5, 0.45, 0.405. (3) Spiral from H2: 3 / 4 as a fraction and as a decimal.
- **Start here (6).** (1) Order 0.38, 0.308, 0.83, 0.3 from the smallest. (2) 3/8 = 0.375 and 7/20 = 0.35 (V6.2). (3) 3.45 x 100 = 345 (V6.1). (4) 0.078 x 1 000 = 78 (V6.1). (5) 52.6 / 100 = 0.526 (V6.1). (6) A money story with cents: 4 items at $2.45.
- **Think harder (4).** (1) The sum of two numbers is 7.5 and their difference is 2.3: find them (4.9 and 2.6, V6.4). (2) A number is 4.3 correct to the nearest tenth and has 2 decimal places: the least and the greatest it can be (4.25 and 4.34, V6.3). (3) Write one decimal between 0.35 and 0.36 (for example 0.355); many answers are right. (4) Give 2.075 kg in kg and g (2 kg 75 g, V14.1).
- **Go further (3).** G1 **Beyond (named): "Never-Ending Decimals".** Write 1/n as a decimal for n from 2 to 20: seven of them stop (n = 2, 4, 5, 8, 10, 16, 20, V6.6), the others repeat; 1/7 repeats the block 142857 (V6.7). What do 2, 4, 5, 8, 10, 16 and 20 have in common? Level note: terminating and recurring decimals; secondary. G2 Ravi has $9.60 more than Siti. Ravi spends $19.20 and then Siti has 3 times as much as Ravi has left: how much did each have at first (Siti $14.40, Ravi $24.00, V6.5)? G3 5/16 as a decimal (0.3125, V6.2): why does it need four places?
- **Non-routine.** EQ G (V6.5), CMP T (V6.4), LIST T (V6.3), POSE T, PAT G Beyond (V6.6).
- **Numbers.** Decimals to 3 places; money to the cent; one answer to 4 places (G3).
- **Home materials.** Pencil, a ruler marked in mm (optional).
- **Kit.** None cut. Four printed hundred-grids (a task uses at most 3). The 13 digit tiles of lesson 1 are reused on the decimal mat (a task uses at most 8).
- **Figures.** Place mat with decimal columns (Y1), decimal number line (Y4), stacked fractions (Y2).
- **Misconceptions.** 0.45 is greater than 0.5 because 45 > 5; "multiplying by 10 adds a zero" (3.5 x 10 is not 3.50); moving the point the wrong way when dividing; rounding 4.25 down; 0.3125 read as 3 125 thousandths.
- **Needs.** Y1, Y4, Y2, RN10.

#### Lesson 7. Boxed-In Triangles

- **Big idea.** Enclose a triangle in a rectangle, then subtract what you added.
- **Strand.** MOE P5 Area of triangle: base and height, composite figures of rectangles, squares and triangles (p. 42). Contest tag: area (SASMO 7 of 75). **Holiday boundary (H4):** H4 is a whole lesson on 1/2 x base x height, the height outside the triangle, "same base, same height", a point on the top side of a rectangle, midpoints, two squares side by side, a 13-14-15 triangle, a triangle of area 54 split at D. Barred: a rectangle with a point on the top side joined to the bottom corners (core 2 and 4, stretch 6), two squares of side 10 and 6, triangle ABC of area 54 with BD = 4 and DC = 8, the 13-14-15 triangle, a square with a triangle on top, listing base and height pairs for area 6, a triangle of area 42 with base 12. This is the lesson plan open question 5 asks about; the register keeps it with a new angle: tilted triangles on a dot grid and the Pick idea.
- **Objective.** Find the area of a triangle with a horizontal base on a grid; composite figures; a tilted triangle by boxing in; the base or height from the area; true, false or not possible to tell about equal heights. Think harder: tilted triangle, missing base. Go further: ratio of areas, draw a rectangle of twice the area, Dots Inside and Dots on the Edge.
- **Prerequisites.** Primary 4 area of rectangles and composite figures (p. 39).
- **Remember (6 min).** (1) Area of a rectangle 8 cm by 5 cm. (2) The height meets the base at a right angle; name it in a drawn triangle. (3) Spiral from H4: 1/2 x 12 x 7 = 42.
- **Start here (6).** (1) Count squares for a right-angled triangle on a grid with legs 6 and 4 (12). (2) A triangle with a horizontal base of 8 and height 5 on a grid (20). (3) Which segment is the height? (4) A rectangle 9 by 4 with a triangle of base 9 and height 4 on top: the area of the figure. (5) Find the shaded triangle in an L-shaped figure by taking away. (6) A story: a sail with base 7 m and height 6 m (21 m2).
- **Think harder (4).** (1) A tilted triangle with corners at dots (1, 1), (6, 3) and (3, 7), counted as dots across and up: box it in a rectangle of 5 by 6 = 30 and subtract three corner triangles of 5, 6 and 6: 13 (V7.1). (2) A triangle has an area of 54 cm2 and a height of 9 cm: the base (12 cm, V7.6). (3) True, false or not possible to tell: two triangles with the same height have the same area (not possible to tell: the bases may differ). (4) Draw a triangle of area 12 cm2 on a grid in two different ways.
- **Go further (3).** G1 **Beyond (named): "Dots Inside, Dots on the Edge".** On dot paper, a triangle with corners on dots has I dots strictly inside and B dots on its edge. Try ten triangles and find the rule: area = I + B/2 - 1 (checked on every triangle on a 6 by 6 grid, V7.2). On a 4 by 4 grid there are 48 triangles of area 3 (V7.5). Level note: Pick's theorem; secondary. G2 ABCD is a square of side 12 cm and M and N are the midpoints of AB and BC: the area of triangle DMN is 54 cm2, so shaded : whole = 3 : 8 (V7.3). G3 A right-angled triangle has legs 5 and 3: draw a rectangle of twice the area, 15 cm2 (3 by 5, V7.4).
- **Non-routine.** GEO T (V7.1), EXP T, GEO G (V7.3), CHAL G (V7.4), PAT G Beyond (V7.2).
- **Numbers.** Bases and heights to 20; grids to 8 by 8 dots; areas to 150 cm2; half squares allowed. "Coordinates" is not used; points are "dots across and up".
- **Home materials.** 30 cm ruler, pencil; six dot-grid pages are in the book.
- **Kit.** None cut.
- **Figures.** `grid` extension with a boxing-in rectangle and area labels (Y5), labelled triangle (Y6).
- **Misconceptions.** Using a slanted side as the height; leaving out the 1/2; subtracting only two of the three corner triangles; thinking equal area means identical triangles.
- **Needs.** Y5, Y6, RN? (areas in cm2 with units).

#### Lesson 8. Angles and Triangle Families

- **Big idea.** The name of a triangle tells you its angles, and every step of an angle chase needs a reason.
- **Strand.** MOE P5 Geometry: angles on a line, at a point, vertically opposite, unknown angles (1.1 to 1.4); isosceles, equilateral and right-angled triangles, angle sum, unknown angles without extra construction (p. 42). P4 angle notation and measuring (p. 39). Contest tag: none in SASMO except the clock; in the school papers GEO is 17 percent of the items and most are angle chains of two to four steps. **Holiday boundary (H8):** H8 is the whole angle-chase lesson (tear the corners off, 127 on a line, 8 slices, parallelogram with A = 3 x B, an isosceles triangle with 110, with 20 and 30 more, 30-60-90 joined, an angle bisector, D on AC with BD = BC, clock angles). Barred: those items and the "list every case of an isosceles triangle with one angle given" (H8 stretch 2, challenge 4 and 9). New: the exterior angle, the chain with AB = BD and AD = DC, true, false or not possible to tell, the star.
- **Objective.** Name triangles by sides and angles; find a third angle; use the exterior angle; chase an angle through two joined triangles with a reason at each step; judge statements about angles. Think harder: exterior angle, chain. Go further: Five-Point Star; a quadrilateral from its angles.
- **Prerequisites.** Primary 4 angle notation. The angle facts (line 180, point 360, vertically opposite equal) are Geometry 1.1 to 1.3 and are **recalled, not taught** (plan open question 6, D9).
- **Remember (6 min).** (1) An angle facts card: 180 on a line, 360 at a point, vertically opposite equal; find the other angle when 127 is on a line (53). (2) The angle sum of a triangle is 180. (3) Spiral from H8: isosceles base angles are equal.
- **Start here (6).** (1) Name a triangle from its sides: equilateral, isosceles, scalene. (2) The third angle from 48 and 67 (65, Q1.7). (3) An isosceles triangle with a 40 degree angle at the top: the base angles (70, Q1.7). (4) An equilateral triangle: each angle 60. (5) Angles on a line, then a triangle: two steps. (6) Vertically opposite angles, then a triangle: two steps.
- **Think harder (4).** (1) AB = AC and angle BAC = 52 degrees; BC is extended to D: angle ACD = 116 degrees, which is 52 + 64 (V8.1). (2) AB = BD and AD = DC with D on BC; angle ABC = 44 degrees: (a) angle ADB = 68, (b) angle ACB = 34 (V8.2, V8.3, V8.7). (3) True, false or not possible to tell: "an isosceles triangle can have a right angle" (true); "can have two obtuse angles" (false, V8.5); "has one angle of 100 degrees so the other two are equal" (not possible to tell). (4) A figure of two joined triangles with a reason at each step.
- **Go further (3).** G1 **Beyond (named): "Five-Point Star".** The five tips of a star drawn by joining every second point of five points on a circle add up to 180 degrees, whatever the five points (checked for 200 random stars, V8.4). Level note: polygon and star angle sums are not in the syllabus; the proof uses the exterior angle. G2 A chain like Think harder 2 with angle ABC = 60 degrees (angle ACB = 30). G3 A quadrilateral has angles 70, 110, 70, 110 in order: is it a parallelogram (true)? And 70, 110, 110, 70 (false: a trapezium) (V8.6).
- **Non-routine.** GEO T (V8.1), GEO G (V8.2), LOG T (V8.5), EXP G (V8.6), EXP G Beyond (V8.4).
- **Numbers.** Whole degrees; chains of two to four steps; "The figure is not drawn to scale." on every page.
- **Home materials.** Protractor (optional), ruler, pencil.
- **Kit (KT3 `triangle_cards`, one page, 8 pieces to cut).** 8 triangles with tick marks for equal sides and no angle values, for sorting. Contract: supplied 8, maximum used 8.
- **Figures.** `angle_fig` (Y6): equal-side ticks, arcs with values or boxes, extended sides.
- **Misconceptions.** Confusing the apex angle with a base angle; treating the exterior angle as 180 minus the apex; trusting the picture's scale; adding all three angles of a figure to 360.
- **Needs.** Y6, KT3, RN12.

#### Lesson 9. Two Groups and the Overlap

- **Big idea.** Count the overlap once.
- **Strand.** No MOE primary outcome; Venn-style overlap is enrichment (not in p. 42). Contest tag: two overlapping groups (SASMO 21-18, one problem). **Holiday boundary:** there is no holiday Venn lesson; fractions of boys and girls appear in H3 core 5 (40 pupils, 3/8 boys) and percentages of boys and girls in H7 challenge 5 (800 pupils, 45 percent boys). Barred: those two. Fractions of two overlapping groups use lessons 4 and 5.
- **Objective.** Sort into a two-way table and a Venn diagram; find both, neither and at least one from totals; fractions and percentages of a class in two clubs; three pair totals. Think harder: totals, two-way table with a percentage, ordering puzzle. Go further: two groups with different fractions; Squeeze the Overlap.
- **Prerequisites.** Primary 4 tables and fractions of a set.
- **Remember (6 min).** (1) 3/5 of 40 (24). (2) Read a two-way table with a total row. (3) Spiral from H3: 2/5 of a class are boys, so 3/5 are girls.
- **Start here (6).** (1) Sort 12 pupils into a table by two features. (2) Fill a Venn diagram from counts. (3) How many play only swimming. (4) How many play at least one game. (5) How many play neither. (6) A story with a table and a total row.
- **Think harder (4).** (1) (a) In a group of 36 children, 24 swim, 19 cycle and 5 do neither: how many do at least one (31)? (b) How many do both (12, V9.1)? (2) Ann and Ben have $85, Ben and Cara $97, Ann and Cara $102: how much does Ann have ($45; Ben $40, Cara $57, V9.3)? (3) A library table: fiction 84 (boys) and 66 (girls), non-fiction 40 and 30: what percentage of the books are fiction, to the nearest whole number (68, V9.5)? (4) Four children finish a race: B ahead of C, C not last, A not first or last, D directly behind A (B, C, A, D, V9.6).
- **Go further (3).** G1 **Beyond (named): "Squeeze the Overlap".** In a class of 45, 28 play chess and 31 play badminton and nobody plays neither or both is unknown: what is the least number who play both (14) and the greatest (28, V9.2)? Level note: inclusion and exclusion; a secondary idea. G2 2/5 of a class are boys; half of the boys and a third of the girls wear glasses; 18 wear glasses: how many pupils (45, V9.4)? G3 The same with percentages: 60 percent like cats and 70 percent like dogs and everyone likes at least one: at least 30 percent like both, at most 60 percent (V9.7).
- **Non-routine.** CMP T (V9.3), TAB T (V9.5), LOG T (V9.6), MULTI G (V9.4), LIST G Beyond (V9.2).
- **Numbers.** Classes up to 60; money to $200; percentages to the nearest whole number.
- **Home materials.** 20 small things (not food), pencil; the Venn mat is printed.
- **Kit.** None cut.
- **Figures.** `venn` (Y7), `table` with a total row, `bar_model` (Y3).
- **Misconceptions.** Counting the overlap twice; forgetting "neither"; adding 28 + 31 to get the class; adding percentages of different wholes.
- **Needs.** Y7, Y3, RN10, RN13.

#### Lesson 10. Term 1 Review and Mi's Challenge Quest

- **Big idea.** Choose the right start, then say why it works.
- **Strand.** Mixed Term 1 (lessons 1 to 9); the heuristics menu (draw, list, table, work backwards, guess and check, regroup) from the MOE process list (pp. 13 to 14). **Holiday boundary (H10):** H10 is the same idea, "choose a way to start", with 23 items. Barred: every H10 stem and its exit ticket (1/2 on a ticket, $5 on a snack, $7 left). New: a unit chain with a transfer, a fraction then a fixed amount, a repeating pattern, an ordering puzzle, a puzzle with exactly one answer.
- **Objective.** Choose a heuristic from a menu and justify it; solve two-topic problems. Think harder: unit chain, backwards, pattern. Go further: design a puzzle with exactly one answer; four-person ordering.
- **Quest in this lesson.** Mi's Challenge Quest takes minutes 35 to 55 straight after the break. Explore 10 and Mini-lesson 9 minutes: an angle warm-up (plan note) and "choose a start" with three examples; the Start here workbook is 25 minutes (a menu: do any four of six); pages 3 to 5 are for home; the exit ticket is not done live. See section 8.1 for the gates.
- **Prerequisites.** None beyond lessons 1 to 9 through the warm-up.
- **Remember (6 min).** Three recall items, one from each of three Term 1 strands: place value (shift 2 400 x 30), a fraction of a remainder, an isosceles angle.
- **Start here (6, a menu).** One quick item from each of six Term 1 strands (see the Quest gates for the style); the child chooses four.
- **Think harder (4).** (1) Ali has 4 times as many cards as Ben. After Ali gives Ben 36 cards, Ali has twice as many as Ben: how many cards did each have at first (Ben 54, Ali 216, V10.1). (2) Mia spent 2/5 of her money on a book and then $18 on lunch and had $24 left: how much at first ($70, V10.2). (3) The beads repeat 3, 1, 4, 1, 5 in blocks: the 117th term is 1 and the sum of the first 117 is 326 (V10.3). (4) An angle chain from the warm-up.
- **Go further (3).** G1 **Beyond (named): "Exactly One".** Write a number puzzle that has exactly one answer and prove it by listing every case. Example for the tutor: "I am a 2-digit number, my digits add up to 12, I leave 1 when divided by 4 and my tens digit is smaller than my ones digit" has the single answer 57 (V10.5). Level note: designing and proving a unique answer is a secondary idea. G2 Four runners P, Q, R and S: S is not first, P finishes ahead of Q, R finishes directly behind P and Q is not last (order P, R, Q, S, V10.4). G3 Choose a heuristic for a new problem and say why in a sentence.
- **Non-routine.** EQ T (V10.1), BACK T (V10.2), PAT T (V10.3), LOG G (V10.4), CHAL G Beyond (V10.5).
- **Numbers.** Within the Term 1 ranges.
- **Home materials.** Pencil, plain paper; the Quest Log stays closed in the book; a quest partner.
- **Kit.** None cut. The Quest Log (3 pages) is in Book 2.
- **Figures.** As the gates (section 8.1): `place_mat`, `venn`, `angle_fig`.
- **Misconceptions.** Starting every problem by adding; reading "4 times as many" as "4 more"; treating the Quest as a race; choosing a heuristic by habit rather than reason.
- **Needs.** Quest builder (TL3), Y1, Y6, Y7.

### 1.3 Term 2: Measure and Make (lessons 11 to 20)

Can a new child join cold? Yes: the warm-ups recall Primary 4 area, nets, decimals and rounding, and the Term 1 facts used here (x and / by 10, 100, 1 000; half base times height) in six minutes; volume and rate are re-taught from the unit cube and "for one". Holiday graduates meet H5 (volume and tanks), H6 (rate) and H4 (triangle area) only in warm-ups. **Safest to skip in exam weeks: lesson 18 Graph Stories** (a Primary 4 spiral; nothing later builds on it); lesson 19 is the next best; hardest to miss: 12, 13, 16. Lesson 20 hosts the Quest.

#### Lesson 11. Solid Views and Dice

- **Big idea.** A solid can be seen from the top, front and side, and turned in the mind.
- **Strand.** MOE P4 nets of a cube and cuboid (p. 39) are recalled; P5 Volume 2.1 build with unit cubes (p. 42). Views of cube stacks and dice are not named outcomes (enrichment). Contest tag: spatial and dice (SASMO 20-15, 21-7, 21-11: picture-only, all Section A). In the school papers DIAG is 127 items, 49 of them views and 11 isometric. **Holiday boundary (H5):** H5 stretch 4 and challenge 1 and 8 paint the whole outside of a cuboid and count the cubes with 0, 1 and 2 painted faces (3 x 4 x 5; "96 cubes have exactly one painted face"). Barred: those two items. There are no views and no dice in the holiday course. New: numbered top views, three views, dice, and cubes painted on some faces only.
- **Objective.** Count the cubes in a stack from a numbered top view; draw the front and side views; use dice facts (opposite faces add to 7; the net of a die); count painted faces when only two faces are painted. Think harder: three views of one stack; tower and row of dice; partly painted cube. Go further: Hidden Cubes; most cubes that can be added.
- **Prerequisites.** Primary 4 nets of a cube; lesson 12 is not assumed.
- **Remember (6 min).** (1) A cube has 6 faces, 12 edges and 8 corners; which of three nets folds to a cube (P4). (2) The top view of a stack of 3 cubes on 2 cubes. (3) Spiral from H5: a 3 x 2 x 2 box holds 12 cubes.
- **Start here (6).** (1) A numbered top view with counts 2, 1 / 3, 1: how many cubes (7, Q2.1)? (2) Draw the front view from the numbers. (3) Which net folds to a cube (circle). (4) On a die the 1 is opposite the 6: write the face opposite 2, 3, 4. (5) How many faces of one cube show in a stack of two cubes. (6) Match a stack to its top view.
- **Think harder (4).** (1) Top view with counts 2, 0, 1 / 3, 1, 0 / 1, 2, 2: the total is 12 cubes; the front view columns are 3, 2, 2 and the side view rows are 2, 3, 2 (V11.5). (2) (a) Four dice are stacked in a tower and the top shows 5: the sum of all faces you can see is 61 (each die shows 14 on its four sides, V11.2). (b) Three dice stand in a row and touching faces add to 8; the left end shows 2: the right end shows 3 (V11.3). (3) A 5 x 5 x 5 cube has its top and front faces painted and is cut into 125 small cubes: 5 cubes have two painted faces, 40 have one and 80 have none (V11.4). (4) Check that the net of a die has opposite faces adding to 7 (V11.1).
- **Go further (3).** G1 **Beyond (named): "Hidden Cubes".** The front view shows columns of 3, 1, 2 cubes and the side view rows of 2, 3, 1: what is the fewest number of cubes and what is the most (6 and 14, V11.6)? Level note: reconstructing a solid from its views; secondary. G2 With the stack of Think harder 1, what is the greatest number of cubes that can be added without changing the front and side views (7), and without changing any of the three views (3) (V11.7)? G3 Which of four pictures cannot be the top view of a stack with these two views.
- **Non-routine.** DIAG T (V11.5), LOG T (V11.2, V11.3), LIST T (V11.4), LIST G (V11.7), DIAG G Beyond (V11.6).
- **Numbers.** Bases up to 4 by 4, heights up to 5; dice 1 to 6; counts to 125.
- **Home materials.** Tape; a die from a board game (optional); up to 12 small blocks (optional; the drawn fallback is complete).
- **Kit (KT4 `dice_nets`, one page, 4 pieces to cut).** 4 nets of a 3 cm die in the 1-4-1 cross layout, opposite faces adding to 7. Contract: the tower of four dice; supplied 4, maximum used 4.
- **Figures.** `dice`, `net` and `cube_paint` (Y8), `cube_stack` with a 4 by 4 base and heights to 5, numbered top, front and side views (Y9).
- **Misconceptions.** Reading the top-view numbers as the front view; counting only the visible cubes; putting 1 beside 6 on a net; adding the hidden touching faces to the visible total; assuming painted faces are always the outside.
- **Needs.** Y8, Y9, KT4.

#### Lesson 12. Boxes and Bricks

- **Big idea.** Volume counts layers of unit cubes.
- **Strand.** MOE P5 Volume of cube and cuboid: build with unit cubes (2.1), cm3 and m3 with no conversion between them (2.4), volume of a cube or cuboid (p. 42). Surface area is not in the syllabus anywhere. **Holiday boundary (H5):** H5 core 1 to 4 (a 3 x 2 x 2 box; flat rectangles from 12 cubes; a 5 x 4 x 3 box), stretch 1, 3 (2-cm cubes in a 9 x 6 x 5 box; a square base and volume 245), challenge 2, 6, 7 (cuboids from 64 cubes; bricks 2 x 3 x 4 into a cube; faces 12, 15, 20). Barred: those items, and the extension "every cuboid of volume 60". New: every cuboid of volume 72, the greatest number of cubes that fit, "twice as long" stories.
- **Objective.** Find the volume as layers and as length x breadth x height; find a missing edge; fit small cubes in a box; list every cuboid of a given volume. Think harder: greatest number of cubes that fit; a volume story; statements. Go further: Least Wrapping.
- **Prerequisites.** Primary 4 area of rectangles; lesson 7 for "layers" language.
- **Remember (6 min).** (1) Area of a 7 cm by 4 cm rectangle. (2) What 1 cm3 is. (3) Spiral from H5: 5 x 4 x 3 = 60 cubes.
- **Start here (6).** (1) Volume of an 8 x 5 x 3 box from layers (120). (2) A cube of edge 4 cm. (3) A missing edge: 4 x 3 x [ ] = 24 (2). (4) Compare two boxes by volume. (5) Draw the second layer of a 3 x 2 box. (6) The unit m3 on a labelled picture (no conversion).
- **Think harder (4).** (1) The greatest number of 3-cm cubes that fit in a box 25 cm by 17 cm by 13 cm: 8 x 5 x 4 = 160 (V12.2). (2) A box is 12 cm long, 5 cm wide and 4 cm high; a second box has the same width and height and a volume 300 cm3 greater: its length is 27 cm (V12.4). (3) True, false or not possible to tell: two cuboids with the same volume have the same height (not possible to tell). (4) A 6 cm cube is cut into 2 cm cubes: 27 cubes (V12.5).
- **Go further (3).** G1 **Beyond (named): "Least Wrapping".** There are 12 cuboids with whole-number edges and a volume of 72 cm3; which one needs the least paper to wrap (3 x 4 x 6, 108 cm2, V12.1)? Level note: surface area is not a primary syllabus topic; the child counts faces. G2 List every cuboid of volume 72 without repeats (12, V12.1). G3 Bricks 2 cm by 3 cm by 4 cm: how many fill a box 12 by 9 by 8.
- **Non-routine.** LIST T (V12.2), EQ T (V12.4), EXP T, WAYS G Beyond (V12.1).
- **Numbers.** Edges to 30 cm; volumes to 5 000 cm3.
- **Home materials.** Ruler; up to 24 same-size blocks (optional).
- **Kit.** None cut. Six printed layer sheets (a task uses at most 4).
- **Figures.** `cube_stack` isometric cuboids (Y9).
- **Misconceptions.** Adding the edges; counting only the top layer; listing 2 x 6 x 6 and 6 x 2 x 6 as different cuboids; dividing the volumes of box and cube instead of fitting whole cubes along each edge.
- **Needs.** Y9, RN13.

#### Lesson 13. Tank Tales

- **Big idea.** Water keeps its volume when the container changes.
- **Strand.** MOE P5 Volume of liquid in a rectangular tank (2.5), the relation of litre and ml to cm3 (2.6) (p. 42); the new water level from a volume and a base area is P6 (2.3, p. 44), a labelled preview. **Holiday boundary (H5):** H5 holds more than a dozen tank and litre items: 1/3 to 3/5 full with 12 l added, a rock raising the water from 8 to 10 cm in a 30 x 25 tank, buckets for a 60 x 40 x 50 tank, 36 l in a 40 x 30 base, a 20 cm cube poured into a 50 x 32 tank, 3 l and a 500 cm3 stone in a 50 x 20 tank, a stone raising 40 x 25 water by 3 cm, pouring from A into B until equal depth, a 10 cm cube in a 40 x 30 tank with water 6 cm deep, 4 bricks raising 15 to 18 cm, a block stood in a 30 x 20 tank. Barred: all of these. This is the plan's second-heaviest overlap, so Think harder keeps the plan's types (fraction and amount, block, divider) in new settings and the Beyond puzzle is a stepped tank.
- **Objective.** Convert litres, ml and cm3; find the volume of water in a tank; find the new depth after adding water; fractions of a tank backwards; a block laid or stood in the water. Think harder: fraction and amount; depth after pouring; litres from edges. Go further: block in two orientations; Stepped Tank.
- **Prerequisites.** Lesson 12.
- **Remember (6 min).** (1) 1 l = 1 000 ml = 1 000 cm3. (2) Volume of a 40 x 25 x 6 slab (6 000 cm3 = 6 l, Q2.3). (3) Spiral from H5: the rise of water when a 12 cm3 solid sinks in a 4 x 3 base (1 cm).
- **Start here (6).** (1) 2.5 l in ml. (2) A tank 40 cm by 25 cm with water 6 cm deep holds how many litres (6, Q2.3). (3) A bottle holds 1 l: how many cm3. (4) The volume of water in a 30 x 20 base tank 12 cm deep. (5) Half a tank of 48 l. (6) Draw the water level at 3/4.
- **Think harder (4).** (1) A tank is 3/10 full; after 3.5 l are added it is 4/5 full: its capacity is 7 l (V13.2). (2) A tank has a base 50 cm by 30 cm and water 8 cm deep; 4.5 l are poured in: the depth is now 11 cm (V13.4). (3) A tank 60 cm long, 40 cm wide and 35 cm high holds 84 l when full (V13.5). (4) True, false or not possible to tell: if water 5 cm deep fills 2/3 of a tank, the tank is 7.5 cm deep (true).
- **Go further (3).** G1 **Beyond (named): "Stepped Tank".** A tank 60 cm wide and 20 cm from front to back has a fixed step 30 cm wide and 12 cm high along one end of the floor. 9 l of water are poured into the empty tank: how deep is the water over the free floor (13.5 cm, V13.1)? The depth rises faster once the step is covered. Level note: height from volume and base area (P6) with a changing base. G2 A tank 36 cm by 25 cm has water 9 cm deep. A block 10 cm by 9 cm by 18 cm is stood upright: the depth becomes 10 cm (V13.3); laid on its 10 x 18 face it is covered and the water rises to 10.8 cm (V13.3). G3 A tank with a divider: water is poured into one side until it spills over.
- **Non-routine.** BACK T (V13.2), CTX T (V13.4), DIAG G (V13.3), DIAG G Beyond (V13.1), EXP T.
- **Numbers.** Edges 3 to 60 cm; depths 2 to 30 cm; volumes to 90 l; decimals in litres to 1 place.
- **Home materials.** Two containers (a jug and a bottle), water, a ruler.
- **Kit.** None cut.
- **Figures.** `tank` (Y11): water level, dimension labels, a divider, a step or a block, a pour arrow.
- **Misconceptions.** Multiplying the base by the whole height instead of the water depth; 1 l as 100 cm3; forgetting a block takes the room of water; adding the block volume when the water does not cover it.
- **Needs.** Y11, RN1 (compound units).

#### Lesson 14. Decimal Measures

- **Big idea.** Units are a ruler for decimals.
- **Strand.** MOE P5 Decimals: convert a measure to a larger or smaller unit in decimal form (km and m, m and cm, kg and g, l and ml) (1.2, p. 41); four operations with decimals (p. 38). Contest tag: none. **Holiday boundary:** H5 core 6 (2.5 l in ml), H6 core 6 (650 g of nuts), H7 (GST on $20) use decimals. Barred: those. Light overlap.
- **Objective.** Convert units in decimal form and in mixed units; mixed-unit bills and recipes; estimate first, then check by rounding; use a table with a missing value. Think harder: bills, mixed units, a water-bill table. Go further: Rounding Rattle.
- **Prerequisites.** Lesson 6.
- **Remember (6 min).** (1) 3 m 45 cm = 3.45 m (V14.1). (2) 4.06 l = 4 l 60 ml (V14.1). (3) Spiral from H5: 2.5 l = 2 500 ml.
- **Start here (6).** (1) Change 3.45 m to cm (345). (2) 2.075 kg in kg and g (2 kg 75 g, V14.1). (3) Compare 1.5 kg and 1 kg 450 g. (4) 4 l 60 ml in l (4.06). (5) Add 2.4 m and 85 cm. (6) A price per metre story.
- **Think harder (4).** (1) 2.4 m of cloth at $6.50 a metre and 0.75 kg of beads at $12.80 a kilogram cost $25.20 (V14.3). (2) 3.6 kg take away 1 kg 850 g, in kg and g: 1 kg 750 g (V14.4). (3) A water-bill table: May 18 400 l, June 21 650 l, July 2 500 l more than June: the total is 64 200 l (V14.5). (4) Write one possible pair of readings that are both 3.4 correct to the nearest tenth and whose exact sum rounds to 6.8 (for example 3.36 and 3.42); many answers are right.
- **Go further (3).** G1 **Beyond (named): "Rounding Rattle".** Five weights are each 1.4 kg correct to the nearest 0.1 kg; the total is between 6.75 kg and 7.25 kg, not exactly 7 (V14.2). Level note: error bounds; secondary. G2 Estimate 7.96 x 4.02 by rounding, then check with the exact product. G3 A recipe scaled up by 2.5 times in mixed units.
- **Non-routine.** CTX T (V14.3), TAB T (V14.5), POSE G, CMP G Beyond (V14.2).
- **Numbers.** Decimals to 3 places; money to the cent; lengths to km; masses to kg and g.
- **Home materials.** Kitchen scale and measuring jug (optional); ruler.
- **Kit.** None cut.
- **Figures.** Decimal number line (Y4), `table`.
- **Misconceptions.** 3.5 m as 3 m 5 cm; 2.075 kg as 2 kg 750 g; carrying 100 g into kg; assuming "correct to" means exact.
- **Needs.** Y4, RN1, RN10.

#### Lesson 15. Cut and Rearrange

- **Big idea.** Cut a shape up and the area stays the same.
- **Strand.** MOE P5 Area of triangle and composite figures (p. 42); the area of a parallelogram and a trapezium is not in the primary syllabus (confirmed), so those are enrichment by dissection. Contest tag: dissection (SASMO 20-23, 21-22). **Holiday boundary (H4):** same base and same height, a point on a side, midpoints P and Q of a 12 x 8 rectangle (challenge 2), a square cut into three triangles. Barred: P the midpoint of the top side and Q the midpoint of the right side of a 12 by 8 rectangle, a point on the top side of a square. New: the midpoint square, folded paper, parallelogram and trapezium by cutting.
- **Objective.** Cut a parallelogram into a rectangle and a trapezium into a parallelogram; show the square on the midpoints of a square has half the area; find areas of folded paper. Think harder: midpoint square, statements, draw. Go further: folded corner; Midpoint Squares.
- **Prerequisites.** Lesson 7.
- **Remember (6 min).** (1) Area of a triangle is half base times height. (2) A parallelogram has opposite sides parallel. (3) Spiral from H4: same base, same height, same area.
- **Start here (6).** (1) Area by counting squares. (2) A right-angled triangle is half a rectangle. (3) Cut a parallelogram and slide a triangle: rectangle 9 by 5 = 45 (V15.2). (4) A trapezium as two triangles: (7 + 11) / 2 x 4 = 36 (V15.2). (5) A composite figure by adding. (6) A shaded part by taking away.
- **Think harder (4).** (1) A square of side 8 cm: join the midpoints of its sides; the new square has area 32 cm2 (V15.1); show it by cutting. (2) True, false or not possible to tell: a parallelogram and a rectangle on the same base and between the same parallel lines have the same area (true). (3) Draw a parallelogram with the same area as a triangle of base 6 cm and height 5 cm (15 cm2, for example base 5 and height 3). (4) The half of a half: the triangle cut off a rectangle by a diagonal.
- **Go further (3).** G1 **Beyond (named): "Midpoint Squares".** Join the midpoints again and again: the areas are 64, 32, 16, 8, 4 cm2 (V15.1); after how many joinings is the area first below 1 cm2 (seven: 0.5, V15.4)? Level note: halving and geometric patterns; secondary. G2 A rectangle ABCD is 12 cm by 8 cm. C is folded onto P on AB with AP = 8 cm: the part that is two layers thick is 25 cm2 and the folded figure covers 71 cm2 (V15.3). G3 A figure that needs a cut and a swap to find a shaded area.
- **Non-routine.** GEO G (V15.3), EXP T, CHAL T, PAT G Beyond (V15.1).
- **Numbers.** Sides to 20 cm; areas to 150 cm2; half cm2 allowed.
- **Home materials.** Scissors (the child cuts in this lesson), glue or tape, plain paper, ruler.
- **Kit (KT5 `dissection_set`, one page, 8 pieces to cut).** 2 parallelograms, 2 trapeziums, 2 triangles and 2 squares on a printed grid. Contract: the Explore cuts each shape once or twice; supplied 8, maximum used 8. Scissors rule: D5.
- **Figures.** `angle_fig` with a fold line (Y6) and `grid` (Y5).
- **Misconceptions.** Using the slant side as the height; forgetting the half in the trapezium; thinking cutting loses area; counting the two-layer part once.
- **Needs.** Y5, Y6, KT5.

#### Lesson 16. Rate and Working Together

- **Big idea.** A rate says how much per one, and rates add.
- **Strand.** MOE P5 Rate: the amount of one quantity per unit of another; find the rate, the total or the number of units (p. 41); speed is never used. Contest tag: work rates (SASMO 19-19, 20-22); speed (19-10) stays out (KIV: a secondary Go further preview of catching up in lesson 16 is the owner's call, D14). **Holiday boundary (H6):** H6 holds 4 apples for $2, a printer at 24 pages a minute, packs of 3 pens, taps at 2 and 3 l a minute, a tap and a second tap filling in 9 minutes, eggs in boxes of 10 and 6, a car park at $1.50 plus $1 per half hour, plans A and B, 3 machines and 360 masks, shops X and Y, a drain with a tap, a dripping tap, three shops with cans, two printers sharing 900 pages, a crack in a tank, a car park at $1.20 and 60¢, printer P and Q in 6 and 3 minutes, a candle race, a bath with the plug out. Barred: all of these, especially the two car-park items, two printers, three shops with cans, a tap with a drain and a bath with the plug out. The plan puts "every half hour or part thereof" and "greatest distance for a fare" here; they stay, with new contexts (postage and a taxi).
- **Objective.** Find a rate for one and scale up or down; read and fill a rate table; charges in steps ("or part of it"); a tap and a drain together; two or three workers together. Think harder: step charges, rates together. Go further: Three Painters.
- **Prerequisites.** Primary 4 multiplication and division; lesson 6 for decimals.
- **Remember (6 min).** (1) 5 kg of rice cost $12.50: the price of 1 kg. (2) A machine makes 240 cups in 8 minutes: in 5 minutes. (3) Spiral from H6: a tap that fills 8 l a minute fills 120 l in 15 minutes.
- **Start here (6).** (1) 5 kg of rice cost $12.50, so 1 kg costs $2.50. (2) 240 cups in 8 minutes is 30 a minute: 150 cups in 5 minutes. (3) Find the total when the rate is $3.20 a kg and the mass 2.5 kg ($8). (4) Find the time for 270 l at 18 l a minute (15 minutes, Q2.6). (5) Fill a rate table. (6) Read a bill table with a missing line.
- **Think harder (4).** (1) Post charges $0.60 for the first 50 g and $0.25 for each further 50 g or part of it: a letter of 235 g costs $1.60; the greatest mass for $2.10 is 350 g (V16.2). (2) A taxi charges $4.20 for the first kilometre or less and 30¢ for every 400 m or less after that; Rui pays $8.10: the greatest distance she could have gone is 6.2 km (V16.5). (3) A tap fills a tank at 12 l a minute and a drain empties it at 5 l a minute; with both on, a 168 l tank fills in 24 minutes (V16.3). (4) A paints a wall in 12 days and A and B together in 8 days: B alone takes 24 days (V16.6).
- **Go further (3).** G1 **Beyond (named): "Three Painters".** A and B together paint a fence in 12 days, B and C in 15 days and A and C in 20 days. How long do all three take (10 days), and how long does each take alone (A 30, B 20, C 60 days, V16.1)? Level note: adding fractions of a job; not a syllabus topic. G2 Compare two plans with a table: which is cheaper for 5 hours and for 8 hours. G3 Two machines print 240 flyers in 6 minutes together and one prints them alone in 10 minutes: the other takes 15 minutes (V16.7).
- **Non-routine.** CTX T (V16.2, V16.5), CTX G (V16.5), TAB T, GC T (V16.3, V16.6), CMP G Beyond (V16.1).
- **Numbers.** Rates in whole numbers and 1 decimal place; charges in cents and dollars; times to 60 minutes; jobs as fractions with denominators to 60.
- **Home materials.** Pencil; squared paper.
- **Kit.** None cut.
- **Figures.** `table` with a missing line; `tank` for the tap and drain (Y11) is optional.
- **Misconceptions.** Rounding "or part of it" down; adding the days instead of the rates; dividing the wrong way round for "per one"; treating a drain as adding.
- **Needs.** RN10, RN1.

#### Lesson 17. Fair Shares

- **Big idea.** Average is levelling out.
- **Strand.** MOE Statistics: average as total divided by number of data is **P6** (p. 44), so this lesson is a labelled preview; P5 Standard has no Statistics strand. The 2020 to 2024 papers set average at P5 (87 items) and the 2025 papers do not. **Holiday boundary:** none (the holiday course has no average).
- **Objective.** Level out by moving items; average = total / number; total = average x number; the effect of adding or removing a value; the average of two groups. Think harder: add a value; the missing bar; a data table. Go further: Merging Classes.
- **Prerequisites.** Primary 4 bar graphs and tables (p. 40).
- **Remember (6 min).** (1) Four numbers 4, 9, 5, 6, 6 levelled out: each becomes 6 (V17.4). (2) Total and number. (3) Read a bar graph.
- **Start here (6).** (1) Share 24 counters equally among 4 children by moving items. (2) The average of 4, 7, 9, 12 (8, Q2.7). (3) The total from an average and a number. (4) A missing value from a total. (5) A bar graph average by levelling. (6) A story with a table.
- **Think harder (4).** (1) The average of six test scores is 74; what must the seventh be for the average of seven to be 76 (88, V17.1)? (2) A bar graph shows Monday 48, Tuesday 57, Wednesday 45 and Thursday 60 and the average of five days was 52: draw Friday's bar (50, V17.3). (3) Which class is closest to the average on a bar graph. (4) Average of a data table.
- **Go further (3).** G1 **Beyond (named): "Merging Classes".** 12 children have an average mark of 15 and 8 children an average of 20: the average of all 20 children is 17, not 17.5 (V17.2). Level note: a weighted average; secondary. G2 Five numbers 1, 1, 1, 1, 16 have an average of 4 although no number is near 4 (V17.5): explain. G3 The average of 5 consecutive whole numbers is 12: they are 10 to 14 (V17.6).
- **Non-routine.** CMP G (V17.1), CHAL T (V17.3), TAB T, EXP G (V17.5), CMP G Beyond (V17.2).
- **Numbers.** Data sets of 4 to 7 numbers; averages to 100; class sizes to 40.
- **Home materials.** About 30 counters or buttons; squared paper.
- **Kit.** None cut.
- **Figures.** `graph` with an average line and a hidden bar (Y12), `bar_model` (Y3).
- **Misconceptions.** Dividing by the wrong count; averaging two averages; thinking the average must be one of the numbers.
- **Needs.** Y12, Y3.

#### Lesson 18. Graph Stories

- **Big idea.** A graph is a short story about change.
- **Strand.** MOE P4 tables, line graphs and pie charts (p. 40); P5 Standard has no Statistics strand, so this is a spiral. Contest tag: none. **Holiday boundary:** none.
- **Objective.** Read values and rates from a line graph; match a story to a graph; draw a line graph from a table; spot a misleading axis; find a total from a pie chart with one count. Think harder: fastest change, draw, axis, pie chart. Go further: Same Data, Two Stories.
- **Prerequisites.** Primary 4 line graphs and pie charts.
- **Remember (6 min).** (1) Read a value from a line graph. (2) A pie chart's whole circle. (3) A scale on an axis.
- **Start here (6).** (1) Read the water level at 10 am. (2) The difference between two times. (3) Which story matches the graph. (4) Complete a table from a graph. (5) A pie chart fraction. (6) The change per hour.
- **Think harder (4).** (1) A tank holds 60, 48, 36, 36, 14 litres at five hourly readings: it drained fastest in the last hour, 22 l (V18.1, V18.2). (2) Draw the line graph from a table and a story. (3) Spot the misleading axis. (4) A pie chart where the 90-degree sector is 36 pupils: the whole is 144 pupils (V18.3).
- **Go further (3).** G1 **Beyond (named): "Same Data, Two Stories".** The scores 92 and 97 drawn on an axis from 0 look 1.05 times as tall, drawn from 90 they look 3.5 times as tall (V18.4). Which picture is fair, and why? Level note: statistical honesty; secondary. G2 A line graph with two lines: when are they equal. G3 Draw a graph from a story that has a flat part.
- **Non-routine.** TAB G (V18.1), CHAL T, EXP T, TAB T (V18.3), EXP G Beyond (V18.4).
- **Numbers.** Scales 1, 2, 5, 10, 20; up to 8 readings.
- **Home materials.** Ruler, squared paper (the book has grids).
- **Kit.** None cut.
- **Figures.** `graph` (line, bar and pie, Y12).
- **Misconceptions.** Reading between gridlines wrongly; confusing a steep line with a high value; assuming equal axis intervals; reading a pie sector as a count.
- **Needs.** Y12, RN10.

#### Lesson 19. Isometric Builders

- **Big idea.** Build it, draw it, turn it.
- **Strand.** MOE P5 Volume: build solids with unit cubes (2.1) and draw cubes and cuboids on an isometric grid (2.3) (p. 42), both missing from the earlier plan; rotating a block figure, picture matrices and ropes are contest enrichment. Contest tag: spatial (SASMO 19-8, 19-15, 21-7, picture-only). In the 2025 papers isometric drawing is an item (11 items). **Holiday boundary:** none; H5 is flat. Figures must be drawn first (plan note).
- **Objective.** Build a stated solid from cubes and copy it on isometric dot paper; draw a cuboid of given edges; count visible faces; match a turned block figure to its original; find the missing picture in a 3 x 3 matrix by finding the rule. Think harder: drawing and matching. Go further: Complete the Cuboid; most cubes to add; the rope.
- **Prerequisites.** Lessons 11 and 12.
- **Remember (6 min).** (1) A 3 x 2 x 2 block has 12 cubes. (2) The top, front and side views of a stack. (3) Dot paper: a line along the dots.
- **Start here (6).** (1) Build the stack in the picture and count the cubes. (2) Copy a 2 x 2 x 2 cube onto isometric dot paper. (3) Draw the 3 x 2 x 1 cuboid. (4) How many faces of a 4 x 3 x 2 cuboid can you see: the squares on three faces are 12 + 8 + 6 = 26 (V19.1). (5) Which solid has a top view like this. (6) Complete a half-drawn cube.
- **Think harder (4).** (1) Draw a cuboid 4 x 3 x 2 and write the number of unit squares you can see (26, V19.1). (2) Match the turned block figure to its original from four options. (3) Find the missing picture in a 3 x 3 matrix by finding the rule. (4) Draw the top view of the solid you drew.
- **Go further (3).** G1 **Beyond (named): "Complete the Cuboid".** A model made of cubes in a 3 x 3 base has heights 3, 3, 3 / 3, 1, 1 / 3, 1, 1: how many cubes make it a 3 x 3 x 3 cuboid (8, V19.3)? Level note: finding what is missing is a build-up of volume; secondary. G2 For heights 2, 0, 1 / 1, 3, 0 / 0, 1, 2 the greatest number of cubes that can be added without changing the top view and the front view is 4 (V19.2). G3 Which rope forms a knot: trace the crossings (optional figure).
- **Non-routine.** DIAG T (V19.1), LIST G (V19.2), DIAG G (turned figure), LIST G Beyond (V19.3).
- **Numbers.** Cubes up to 4 x 4 x 3; views up to 5 high.
- **Home materials.** Up to 14 small blocks (optional); six isometric sheets are in the book (a task uses at most 4).
- **Kit.** None cut.
- **Figures.** `iso` isometric dot paper, partly drawn cuboids, turned block options (1) to (4), matrix and rope (Y10, rope optional), `cube_stack` (Y9).
- **Misconceptions.** Drawing the hidden faces; confusing horizontal dot lines with edges; counting the same visible square twice; thinking a turned figure has a different number of cubes.
- **Needs.** Y10, Y9, RN7 (options that are pictures).

#### Lesson 20. Term 2 Review and Mi's Challenge Quest

- **Big idea.** Measures combine in real problems.
- **Strand.** Mixed Term 2 (lessons 11 to 19); contest-style units, volume and rate. **Holiday boundary:** H5, H6 and H10 items are barred as for the lessons they mirror.
- **Quest in this lesson.** Minutes 35 to 55 after the break; Explore 10 and Mini-lesson 9 on choosing the model for a measures problem; the Start here workbook is 25 minutes; pages 3 to 5 are for home; the exit ticket is not live. See section 8.2.
- **Objective.** Choose a model for a measures problem and explain why. Think harder: buy-more-get-free; a tank; a volume. Go further: perimeter and area; a bar model with a fraction and a difference; Pour and Measure.
- **Remember (6 min).** Three recall items from three Term 2 strands: a cuboid volume, a rate for one, a triangle area.
- **Start here (6, a menu).** One quick item from each strand (see the gates).
- **Think harder (4).** (1) A class of 31 pupils each needs a pen at $2.50; pens are buy 2, get 1 free: the least cost is $52.50 (21 pens paid, V20.2). (2) A tank problem from lesson 13. (3) A volume problem from lesson 12. (4) A rate with a drain from lesson 16.
- **Go further (3).** G1 **Beyond (named): "Pour and Measure".** With a 7 l jug and an 11 l jug and a tap, measure exactly 2 l: the fewest steps (fill, empty or pour) is 14 (V20.1). Level note: a puzzle of state search; secondary. G2 A composite figure with its perimeter given and its area asked. G3 A bar model with a fraction and a difference.
- **Non-routine.** CTX T (V20.2), GEO G, EQ G, CHAL G Beyond (V20.1).
- **Numbers.** Within the Term 2 ranges.
- **Home materials.** Pencil; the Quest Log stays closed in the book; a quest partner.
- **Kit.** None cut. The Quest Log is in Book 4.
- **Figures.** As the gates: `cube_stack`, `tank`, `graph`, `iso`.
- **Misconceptions.** Using the Term 2 formulas without checking units; treating the Quest as a race.
- **Needs.** Quest builder (TL3), Y8, Y9, Y11, Y12.

### 1.4 Term 3: Parts, Percent and Pattern (lessons 21 to 30)

Can a new child join cold? Yes: the warm-ups recall fraction of a quantity, fraction to decimal, the percent benchmarks and a bar model, so no Term 1 or 2 lesson is assumed; the holiday topics H7 (percentage), H3 (units) and H9 (patterns, supposition) appear only in warm-ups. **Safest to skip in exam weeks: lesson 29 Money Grows** (nothing later builds on it); lessons 23 and 24 should be made up because they are the heart of the term; hardest to miss: 21 to 24. Lesson 30 hosts the Quest.

#### Lesson 21. Percent Sense

- **Big idea.** Percent means out of 100, and a percent, a fraction and a decimal are three names for one amount.
- **Strand.** MOE P5 Percentage: a part of a whole as a percentage, the sign %, a percentage part of a whole, discount, GST and annual interest (1.4) (p. 41); percentage change and finding the whole are P6 (p. 43). **Holiday boundary (H7):** H7 core 1 to 6 (35 shaded squares; 50%, 25%, 10% of $80; 10% off $50; 24 of 40 walk; 25% of $60; GST on $20), stretch 3 (15% as 10% + 5%), stretch 7 and 8 (30% of 70 against 70% of 30; 18 out of 25 against 27 out of 40). Barred: those items and the plan's "40% of 60 against 60% of 40" (EX-EXP-1 is the same move as H7 stretch 7). New: ordering fractions, decimals and percents; why a percentage of a whole number of pupils needs the right class size; "which class collected 40% of all the items"; percent of a percent.
- **Objective.** Change between percent, fraction and decimal; find a percentage of a quantity from the benchmarks 1%, 10%, 25%, 50%; order mixed forms; use the whole-number condition. Think harder: ordering, a class-size condition, a table. Go further: Percent of Percent.
- **Prerequisites.** Primary 4 fractions and decimals; lesson 6 for decimals.
- **Remember (6 min).** (1) 1/2, 1/4, 1/5 and 3/4 as decimals and percents. (2) 10% of 240 (24). (3) Spiral from H7: 35 shaded squares out of 100 is 35%.
- **Start here (6).** (1) 7/20 = 35%, 3/8 = 37.5% (V21.5). (2) 0.4 as a percent (40%). (3) 35% of 80 = 28 (Q3.1). (4) 10% and 5% of $350. (5) Shade 24% of a 10 x 10 grid. (6) A percent of a quantity from a story.
- **Think harder (4).** (1) Put 37%, 3/8, 0.38 and 2/5 in order from the smallest (V21.3). (2) Hana says 35% of her class of 18 wear glasses. Why cannot that be right (35% of 18 = 6.3), and which class sizes up to 100 make 35% a whole number (20, 40, 60, 80, 100, V21.1)? (3) Four classes collected 24, 60, 36 and 30 items: which class collected 40% of all the items (the one with 60, of 150, V21.4)? (4) A percentage from a two-way table to the nearest whole number.
- **Go further (3).** G1 **Beyond (named): "Percent of Percent".** 20% of 50% of $240 is $24 (V21.2): what single percentage of $240 is that (10%)? Is it 70%, 30% or 10% of the whole, and why? Level note: composing percentages, the root of percentage change (P6). G2 A number is increased by 10% and then decreased by 10%: is it back where it started (no: 200 becomes 220 and then 198, V21.6). G3 Write a story whose answer is 12 pupils.
- **Non-routine.** POSE T (V21.1), LOG T (V21.4), EXP T (V21.3), TAB T, EXP G Beyond (V21.2).
- **Numbers.** 1% to 100%, one half-percent (37.5%); quantities to $500; classes to 100.
- **Home materials.** Pencil; six unnumbered hundred-grids are in the book (a task uses at most 4).
- **Kit.** None cut.
- **Figures.** `percent_grid` (Y22), percent number line (Y4), stacked fractions (Y2).
- **Misconceptions.** 0.4 as 4%; 35% means 35 pupils; 5% as 1/5; percent of a percent as the sum.
- **Needs.** Y22, Y4, Y2, RN10.

#### Lesson 22. Shop Smart

- **Big idea.** The best deal needs a calculation, not a feeling.
- **Strand.** MOE P5 Percentage: discount, GST and annual interest (1.4, p. 41). **Holiday boundary (H7, H6):** H7 core 3 and 6, stretch 2, 4, 5, challenge 2, 7, 8 (10% off $50; GST on $20; "buy 3 get 1 free" against 30% off; a $250 bicycle at 12%; an $80 watch with GST; the price before a 20% discount; $109 with GST included; an $80 lamp at 25% against 10% then 15%); H6 stretch 6 and 9 (4 pens for $3 and 1 free; three shops with cans). Barred: all. The order of discount and GST giving the same result is H7's share question, so it is not an item. New: a restaurant bill with a service charge and GST, buy 4 get 1 free for a class, singles and packs, a GST-inclusive price.
- **Objective.** Find a discount and a sale price; add GST at 9 percent; work out an offer; choose the cheapest way to buy for a group; find a price before GST. Think harder: discount then GST; buy-more-get-free; singles and packs; GST included. Go further: Tax on Tax.
- **Prerequisites.** Lesson 21.
- **Remember (6 min).** (1) 20% of $50. (2) 9% as 10% - 1%. (3) Spiral from H7: 1% of $20 is 20¢.
- **Start here (6).** (1) A $50 jacket is 20% off: it costs $40 (Q3.2). (2) 9% GST on $40: $3.60, so $43.60 (Q3.2). (3) The saving on a $120 bag at 15% off. (4) A price list with GST not yet added. (5) Which is cheaper: 10% off $80 or $6 off. (6) "Inclusive of GST" means the tax is already in the price.
- **Think harder (4).** (1) A $360 coat is 25% off and then 9% GST is added: $294.30 (V22.2). (2) Cups cost $2.40 each; buy 4, get 1 free; a club needs 27 cups: it pays for 22, $52.80 (V22.3). (3) Singles cost $3.50, a pack of 4 costs $12 and a pack of 10 costs $27; the least cost for 23 children is $64.50 (V22.4). (4) A price of $54.50 includes 9% GST: $50 before GST and $4.50 of tax (V22.5).
- **Go further (3).** G1 **Beyond (named): "Tax on Tax".** A restaurant adds a 10% service charge to a $80 bill and then 9% GST to the total: $95.92, so the two charges add 19.9% to the bill, not 19% (V22.1). Level note: successive percentages (P6 percentage change). G2 Compare two shops with different pack sizes for 45 pens. G3 "Buy 2 pairs of shoes at $60 and the third pair at half price": 3 pairs cost $150 instead of $180, which is a discount of 16 2/3% (V22.8).
- **Non-routine.** MULTI T (V22.2), CTX T (V22.3), WAYS T (V22.4), CTX G, EXP G Beyond (V22.1).
- **Numbers.** Prices to $500; discounts 5% to 40%; GST 9% (older-paper practice may say 7% and says so); money to the cent.
- **Home materials.** Pencil; a real shopping receipt (optional).
- **Kit (KT6 `shop_cards`, one page, 10 pieces to cut).** 10 cards (item picture, price, offer). Contract: a task uses 8 at once; supplied 10, maximum used 8. Reused in the lesson 29 warm-up.
- **Figures.** `price_tag` (exists), `table`.
- **Misconceptions.** Adding two discounts (15% + 10% = 25%); GST on the original price; "buy 4 get 1 free" as 25% off when not every item is paid; rounding GST wrongly.
- **Needs.** KT6, RN5 (money), RN10.

#### Lesson 23. One Number as a Percent of Another

- **Big idea.** The whole is the number after "of".
- **Strand.** MOE P5 Percentage: a part of a whole as a percentage (p. 41); percentage change and finding the whole are P6 (p. 43) and stay labelled previews. **Holiday boundary (H7):** H7 core 4 (24 of 40 walk), stretch 6 (40% then 50% of the rest), challenge 3, 4, 5, 6, 9 (a tank from 40% to 70%; a score up and down 20%; the bus percentage; 75% red marbles; Mrs Tan's $54). Barred: those. New: nearest whole percent, a statement about "52% of the cars", a juice mixture, percentage of a remainder with a difference.
- **Objective.** Write one number as a percent of another (also to the nearest whole percent); find a percentage of a remainder; judge statements about percents; preview finding the whole. Think harder: nearest percent; statements; percent of a remainder. Go further: find the whole; Juice Mix.
- **Prerequisites.** Lesson 21.
- **Remember (6 min).** (1) 18 out of 24 as a fraction in the simplest form. (2) 30% of $250. (3) Spiral from H7: 24 out of 40 is 60%.
- **Start here (6).** (1) 18 out of 24 is 75% (Q3.3, V23.1). (2) 15 out of 20. (3) 9 out of 12 as a percent. (4) What percent of 50 is 7. (5) A table with a total row. (6) What percent of an hour is 15 minutes.
- **Think harder (4).** (1) 41 out of 60 as a percent to the nearest whole number (68%, V23.1). (2) Ali had $250. He spent 40% on shoes and 30% of the rest on a bag: the bag cost $45 (V23.4). (3) Of the cars in a car park 52% are red. True, false or not possible to tell: more than half are red (true); there are 52 cars (false: the number of cars must be a multiple of 25, V23.3); the number of red cars is even (not possible to tell: 25 cars have 13 red, 50 have 26). (4) A table of marks: the percent that passed.
- **Go further (3).** G1 **Beyond (named): "Juice Mix".** 2 kg of juice that is 20% fruit is mixed with 3 kg that is 40% fruit: the mixture is 32% fruit (V23.2). Level note: weighted percentages; secondary. G2 An amount is 45% of a whole and is 36: the whole is 80 (P6 preview, V23.1). G3 After spending 40% on shoes and 30% of the rest the rest is $105: the money at first.
- **Non-routine.** LOG T (V23.3), MULTI T (V23.4), BACK G (V23.1), CMP G Beyond (V23.2).
- **Numbers.** Percents to the nearest whole number; wholes to 500.
- **Home materials.** Pencil.
- **Kit.** None cut.
- **Figures.** `percent_grid` (Y22), `bar_model` (Y3), `venn` optional (Y7).
- **Misconceptions.** Dividing the whole by the part; using the wrong whole after a first percent; 52% implying 52 cars; mixing 45% of 80 with 80% of 45.
- **Needs.** Y22, Y3, RN10.

#### Lesson 24. Unequal Parts

- **Big idea.** Each part is a number of units, and the units tell the whole story.
- **Strand.** MOE: ratio is **P6 only** in the 2021 syllabus (a : b, a : b : c, whole numbers, p. 43); "times as many" and "for every" are the 2025 wording and are taught at Start here; the notation "a : b read as a units to b units" is a labelled P6 preview at Think harder (owner decision 6). Contest tag: ratio (SASMO 5 of 75). **Holiday boundary (H3):** H3 is a whole lesson on before-and-after models: counters 18 and 6 with a gift, ages in 5 years, 1/4 and 1/3 of $60, stamps made equal, 3/8 boys, red and blue beads, a box of 3/7 red, "3/5 as many cards" with 20 given, the father and son who are 50 in all, 1/5 of an age years ago, giving to make 1/2 or 3/5 as many. Barred: all of these, and the plan's "in how many years will he be 4 times as old" with father-and-son numbers. New: a price model, three children with a chain, a ratio before and after a gift with a total asked, two ratios linked by a shared part.
- **Objective.** Draw a unit model for "times as many", "more than" and "for every"; solve with units; read "a : b"; link two ratios. Think harder: price model, ratio and gift, ages, three quantities. Go further: Shared Part; a chain.
- **Prerequisites.** Primary 4 multiplication and division; lesson 5 recalls fraction bars.
- **Remember (6 min).** (1) 3 times as many as 12. (2) Draw a bar for "Ali has 5 more than Ben". (3) Spiral from H3: a total that stays the same when something moves.
- **Start here (6).** (1) Ali has 3 times as many cards as Ben and together they have 48: 36 and 12 (V24.7). (2) For every 2 red beads there are 3 blue; there are 20 red: 30 blue. (3) A has 5 more than B and together 41. (4) One child gives some to the other and the total stays the same. (5) Draw the bars for a comparison. (6) A story with a total and a difference.
- **Think harder (4).** (1) A pencil case costs $7 more than a ruler; 3 cases and 2 rulers cost $76: a ruler costs $11 and a case $18 (V24.1). (2) Ali and Ben have money in the ratio 5 : 9 (read "5 units to 9 units"); Ben gives Ali $14 and they have the same: together $98 (Ali $35, Ben $63, V24.2). (3) A mother is 33 and her son is 6: in 3 years she will be 4 times as old (V24.5). (4) Three children: A has twice as many stickers as B and C has 10 more than B; together 90: A 40, B 20, C 30 (V24.8).
- **Go further (3).** G1 **Beyond (named): "Shared Part".** Pens to pencils is 3 : 4 and pencils to rubbers is 6 : 5; make the pencils the same (12 units) and the three are 9 : 12 : 10 (V24.3). If there are 18 more pencils than rubbers there are 279 in all (V24.4). Level note: a : b : c with a shared term (P6). G2 A ratio after a gift with a total asked, in two steps. G3 Ages: in 7 years a father aged 35 will be 3 times as old as his son aged 7 (V24.6).
- **Non-routine.** EQ T (V24.1, V24.5), EQ G (V24.2), CMP G (V24.4), CMP G Beyond (V24.3).
- **Numbers.** Totals to 300; ratios with parts to 12; ages to 60.
- **Home materials.** Pencil; paper strips (optional).
- **Kit (KT7 `unit_strips`, one page, 6 pieces to cut).** 6 strips of 12 cells (72 cells). Contract: three bars at once, 38 cells; supplied 72, maximum used 38. Cut between strips, not between cells.
- **Figures.** `bar_model` with unit labels, a "1 unit" bracket and before-and-after pairs (Y3).
- **Misconceptions.** Reading 5 : 9 as 5/9 of the total; dividing the total by 2 for two parts; forgetting the shared part when linking ratios; mixing "more than" with "times as many".
- **Needs.** Y3, KT7, RN11 (ratio answers).

#### Lesson 25. Balance and Undo

- **Big idea.** Do the same to both sides, and undo from the end.
- **Strand.** MOE: letters for unknowns are P6 (p. 43), so boxes and shapes only; balance and working backwards come from the process list (pp. 13 to 14). **Holiday boundary (H10, H3, H9):** H10 core 1 and 2, stretch 1, 7, 8, challenge 1 and 6 (a number times 4 minus 6; Ali's book; Siti's 2/5 and 1/3; "think of a number"; the bus; the monkey and the rambutans), H3 challenge 8 (give half and 4 more, twice), H9 stretch 3 (35 heads and 94 legs). Barred: all of these; the plan's heads-and-legs item moves to lesson 28 with a new context. New: two-step equations with boxes, a worked solution with an error, balance with two shapes, a backwards chain with thirds and fifths, Odd Coin Out.
- **Objective.** Balance a picture; solve one- and two-step equations with boxes; undo in the reverse order; check by putting the answer back; find an error in worked steps. Think harder: two-step equations, shapes, error. Go further: backwards chain; Odd Coin Out.
- **Prerequisites.** Primary 4 the four operations.
- **Remember (6 min).** (1) 8 + [ ] = 15. (2) 3 x [ ] = 24. (3) Spiral from H10: I think of a number, add 5 and double it to make 30.
- **Start here (6).** (1) 3 [ ] + 5 = 29: [ ] = 8 (Q3.5). (2) 5 [ ] - 9 = 26: [ ] = 7 (V25.3). (3) A balance with a shape on each pan. (4) Undo: a number is doubled and 6 is added, the answer is 20. (5) Check an answer by putting it back. (6) Make both sides equal.
- **Think harder (4).** (1) 3 [ ] + 7 = 28 gives 7 and 5 [ ] - 9 = 26 gives 7 (V25.3). (2) A child solves 4 [ ] + 8 = 36 by writing 36 / 4 - 8 = 1; find the error (the 8 must go first: (36 - 8) / 4 = 7, V25.3). (3) Two squares and a circle weigh 27 and a square and two circles weigh 24: a square is 10 and a circle is 7 (V25.5). (4) A chain run backwards with a fixed amount.
- **Go further (3).** G1 **Beyond (named): "Odd Coin Out".** Nine coins look alike but one is heavier; with a pan balance you can find it in 2 weighings; 27 coins need 3 (V25.1, V25.2). Why? Level note: information counting (3 results per weighing); secondary. G2 Mei gave away 2/5 of her stickers and 3 more; then 1/3 of the rest and 2 more; she had 8 left: 30 at first (V25.4). G3 Write a balance puzzle with a unique answer.
- **Non-routine.** EQ T (V25.5), EXP T (V25.3), BACK G (V25.4), LOG G Beyond (V25.1).
- **Numbers.** Boxes with values to 50; shapes with values to 20; weights to 100 g.
- **Home materials.** Pencil; a kitchen balance is not needed.
- **Kit (KT8 `weight_tokens`, one page, 12 pieces to cut).** 12 tokens in four shapes of weight 1, 2, 3 and 4 units and a printed balance mat. Contract: a task uses 9; supplied 12, maximum used 9. The shapes differ by outline, not colour.
- **Figures.** `balance` (Y18), `picture_equation` (exists).
- **Misconceptions.** Undoing in the wrong order; changing one side only; treating "= " as "the answer is"; weighing three coins against three when only two groups are needed.
- **Needs.** Y18, KT8, RN13.

#### Lesson 26. Number Stories

- **Big idea.** A pattern is a rule you can prove, not just see.
- **Strand.** Not a P5 strand: number-sequence patterns are P1 to P4 only; letters are P6 (p. 43). Contest tag: non-constant patterns (SASMO 19-4, 20-7, 20-10). The school papers set matchstick and dot figures with a table, a repeating block with the 100th and 117th term, and savings that grow by a fixed step (PAT 98 items). **Holiday boundary (H9):** H9 is the whole pattern lesson: 5, 9, 13, 17; matchstick squares 4, 7, 10; 2, 6, 10, 14; the rule 3 x n + 2; beads red red blue yellow yellow yellow; 40 tables seating 82; 1 + 3 + 5 + ...; saving $3 and $2 more each week; 3, 8, 13, 18 above 200; a staircase of squares; squares on a 4 x 4 grid; matchstick grids; diamonds of dots; digits of pages; 123456789101112... Barred: all, including the plan's matchstick figures (EX-PAT-1), repeating beads (EX-PAT-2) and the staircase. New: gaps of the gaps, two sequences woven together, a figure with n x n + 4 dots, the first triangle number over 300, and chords on a circle.
- **Objective.** Find the rule of a constant-step pattern; use the gaps of the gaps for a growing step; split a woven sequence; write the number of dots for any figure; prove a rule by pairing. Think harder: the four forms above. Go further: Not Always Doubling; a rule is not unique.
- **Prerequisites.** Primary 4 number patterns.
- **Remember (6 min).** (1) The next two numbers of 7, 12, 17 and the rule in words. (2) A table of figure number and dots. (3) Spiral from H9: 5, 9, 13, 17 has a constant step of 4.
- **Start here (6).** (1) Say the rule in words for 4, 11, 18, 25. (2) The 10th term of 3, 8, 13 (48). (3) Complete a table for a figure pattern of rows. (4) Is 98 in the pattern 3, 8, 13, ... (yes, the 20th). (5) Find the figure number from the dots. (6) Which rule gives the numbers in the table.
- **Think harder (4).** (1) 2, 5, 11, 20, 32: the gaps are 3, 6, 9, 12, so the 8th term is 86 (V26.1). (2) 3, 40, 7, 35, 11, 30, ... is two sequences woven together: the 13th term is 27 and the sum of the first 10 is 205 (V26.2). (3) Figure 1 has 5 dots, figure 2 has 8, figure 3 has 13, figure 4 has 20: figure 10 has 104 dots and 229 dots is figure 15 (V26.6). (4) The triangle numbers 1, 3, 6, 10, ...: pair the numbers to add 1 + 2 + ... + 24 (300); the first triangle number above 300 is the 25th (325, V26.3).
- **Go further (3).** G1 **Beyond (named): "Not Always Doubling".** Put 1, 2, 3, ... points on a circle and join every pair: the regions are 1, 2, 4, 8, 16, but with 6 points there are 31, and with 7 there are 57 (V26.4). Level note: a pattern that is not what it looks like; secondary. G2 An invented rule found from three examples: n x n + 1 gives 5, 10, 17 for n = 2, 3, 4 and so does n x n + 1 + (n - 2)(n - 3)(n - 4); they disagree at n = 5 (26 and 32, V26.5). G3 Prove by pairing why 1 + 2 + ... + n is half of n x (n + 1).
- **Non-routine.** PAT T (V26.1, V26.2, V26.6, V26.3), PAT G (V26.4), TAB T, LOG G (V26.5).
- **Numbers.** Terms to 200; positions to 100; chords for 1 to 7 points.
- **Home materials.** Pencil, squared paper.
- **Kit.** None cut.
- **Figures.** `pattern_fig` (Y13), `chords` (Y14, an extension of `network`).
- **Misconceptions.** Assuming a constant step; off-by-one in the nth term; trusting a pattern after four terms; reading the gaps as the terms.
- **Needs.** Y13, Y14.

#### Lesson 27. Count Without Counting

- **Big idea.** Order the list so nothing is missed or doubled.
- **Strand.** Not in the MOE primary list (counting arrangements, gaps and posts, triangles in a figure are enrichment; a contest and Hong Kong staple). Contest tag: systematic counting (SASMO 7 of 75, 6 in Section B). **Holiday boundary (H9, H10, H1):** squares of all sizes on a 4 x 4 grid (H9 challenge 3), digits needed for pages 1 to 150 (H9 challenge 5), the 100th digit (H9 challenge 9), digits written from 1 to 1000 (H1 challenge 9), rectangles in a 1 x 5 strip and a 3 x 4 grid (H10 challenge 2 and 3), the digit 4 from 1 to 50 (H10 challenge 4), two numbers that multiply to 702 (H9 stretch 7). Barred: all of these. The plan's "digits used when numbering pages" moves to the reverse question. New: gaps and posts, triangles by apex and line, handshakes, a line with two children apart, how many digits make a book, numbers with different digits between two bounds.
- **Objective.** List outfits with a tree or table; use "n posts, n - 1 gaps"; count triangles by choosing two rays and one line; count handshakes; count numbers by cases on the first digit. Think harder: posts and gaps, triangles, the reverse page question, a line of four. Go further: Triangles Hiding; handshakes among 9; numbers between bounds.
- **Prerequisites.** Primary 4 multiplication.
- **Remember (6 min).** (1) 3 tops and 2 bottoms: list all outfits (6). (2) 4 children and handshakes by listing (6). (3) Spiral from H9: the squares of a 2 x 2 grid (5).
- **Start here (6).** (1) List all outfits. (2) A tree diagram of two choices. (3) List all 2-digit numbers from the cards 2, 5, 7. (4) How many pairs from 5 children (10). (5) Match each list with a count. (6) A menu with 3 mains and 2 drinks.
- **Think harder (4).** (1) A fence is 45 m long with a post every 5 m: 10 posts (9 gaps); round a pond of 45 m: 9 posts (V27.1). (2) Triangle ABC has points P, Q, R on BC and lines AP, AQ, AR: 10 triangles (V27.2). (3) A book uses 282 digits to number its pages from 1: it has 130 pages (V27.4). (4) Four children stand in a line and Ann and Ben must not stand next to each other: 12 lines (V27.3).
- **Go further (3).** G1 **Beyond (named): "Triangles Hiding".** Six lines meet at A and cross two parallel lines: there are 30 triangles (2 x 15, V27.2); with five lines and two parallels, 20. Level note: counting by choosing lines; secondary. G2 Nine children each shake hands once with every other child: 36 handshakes (V27.3). G3 How many whole numbers from 2 000 to 3 999 have 4 different digits (1 008, V27.5).
- **Non-routine.** DIAG T (V27.2), WAYS T (V27.3), LIST T (V27.4), WAYS G (V27.3), LIST G (V27.5), DIAG G Beyond (V27.2).
- **Numbers.** Choices to 6; groups of people to 10; digits to 4; lines to 6.
- **Home materials.** Pencil; paper.
- **Kit (KT9 `people_cards`, one page, 10 pieces to cut).** 10 people. Contract: handshakes among 9; supplied 10, maximum used 9. No printer: 9 coins or buttons.
- **Figures.** `rays` (Y19), `network` (exists), `table`.
- **Misconceptions.** n gaps for n posts; counting a handshake twice; counting a triangle by its apex only; forgetting that a number cannot start with 0.
- **Needs.** Y19, KT9.

#### Lesson 28. Supposition Studio

- **Big idea.** Suppose everything is one kind, then adjust.
- **Strand.** Not an MOE outcome (the supposition and guess-and-check heuristics belong to the process list, pp. 13 to 14). Contest tag: whole-number totals, extra and short, largest total that cannot be made (SASMO 19-23, 20-3, 20-9). **Holiday boundary (H9, H10):** bicycles and tricycles with 37 wheels (H9 core 4), chickens and goats with 35 heads and 94 legs (H9 stretch 3), spiders and beetles with 8 and 6 legs (H9 challenge 4), pens at $2 and files at $3 (H9 core 6), a quiz with 3 for a correct answer and -1 for a wrong one (H9 stretch 8), a quiz with 4 and -1 and blanks (H9 challenge 8), 14 coins of 50¢ and 20¢ worth $4.90 (H10 stretch 5), 25 coins worth $5.30 (H10 challenge 8), pens at $2 and pads at $3 (H10 core 6). Barred: all of these, which are the plan's heads and legs and quiz points. New: tickets at $12 and $7, extra and short, a postage problem with 5¢ and 8¢ stamps, three sizes of box, every way to pay $1.20.
- **Objective.** Use a guess-and-check table; suppose all one kind and adjust; solve extra-and-short stories; list every way to make a total; find which totals cannot be made. Think harder: tickets, extra and short, ways to pay, largest total not made. Go further: Nugget Numbers.
- **Prerequisites.** Primary 4 multiplication; lesson 22 for money.
- **Remember (6 min).** (1) 7 items cost $15: pencils $1, pens $3, a guess-and-check table. (2) Total = number x price. (3) Spiral from H9: tricycles and bicycles by a table.
- **Start here (6).** (1) Pencils cost $1 and pens $3: 7 items cost $15, so 4 pens (V28.5). (2) A table of guesses with a better guess each time. (3) 20 stickers in two sizes. (4) Suppose all are cheap and find the difference. (5) A guess-and-check table with a check column. (6) A story with a table to complete.
- **Think harder (4).** (1) Adult tickets cost $12 and child tickets $7; 40 tickets cost $395: 23 adults (V28.1). (2) Pencils are shared among some children: with 6 each there are 9 left, with 8 each 1 is short: 5 bags and 39 pencils (V28.6); with 12 children, 6 each leaves 14 and 8 each is 10 short: 86 pencils (V28.2). (3) The ways to pay exactly $1.20 with 10¢, 20¢ and 50¢ coins: 13 (V28.4). (4) With only 5¢ and 8¢ stamps the largest amount that cannot be made is 27¢ and 14 amounts cannot be made (V28.3).
- **Go further (3).** G1 **Beyond (named): "Nugget Numbers".** Boxes hold 7, 10 or 12 nuggets; the largest number you cannot buy is 25, and 15 numbers cannot be made (V28.3). Level note: a coin problem with three sizes; secondary. G2 Compare the cost of 45 items from two pack sizes with a budget. G3 The same question with boxes of 8, 11 and 15: find the largest amount that cannot be made by a table (36, with 20 amounts that cannot be made, V28.7).
- **Non-routine.** GC T (V28.1, V28.5), GC T (V28.2, V28.6), WAYS T (V28.4), LIST G (V28.3), LIST G Beyond (V28.3).
- **Numbers.** Totals to $500; items to 60; coins 10¢, 20¢, 50¢; stamp sizes to 12.
- **Home materials.** Pencil; real coins from a purse (a grown-up present).
- **Kit (KT10 `play_coins`, two pages, 21 pieces to cut).** 12 ten-cent, 6 twenty-cent and 3 fifty-cent coins marked PLAY MONEY. Contract: the most any task uses is 12, 6 and 2; supplied 12, 6 and 3 (K.5).
- **Figures.** `table`, `money` (exists).
- **Misconceptions.** Stopping at the first fit; forgetting the check column; double counting the same way in a different order; thinking every large total can be made.
- **Needs.** KT10, RN13.

#### Lesson 29. Money Grows

- **Big idea.** Interest is a percent of the money, paid every year.
- **Strand.** MOE P5 Percentage: annual interest (1.4, p. 41), missing from the earlier plan; compound interest is beyond primary. **Holiday boundary (H7):** none on interest; H7 stretch 1 and challenge 4 look at percentage increases and decreases. Barred: those. Light overlap. New: simple interest over several years, two saving plans, a price rise and fewer tickets, a sold-in-packs claim.
- **Objective.** Find the interest for one year and for several years; the amount after n years; compare two plans; the same money after a price rise; judge a claim. Think harder: several years, plans, a price rise. Go further: Doubling Money; compound interest as a preview.
- **Prerequisites.** Lesson 21; lesson 22 for money.
- **Remember (6 min).** (1) 3% of $2 000. (2) The cost of 28 tickets at $3. (3) Spiral from lesson 22: 40% as a fraction.
- **Start here (6).** (1) $2 000 at 3% a year earns $60 in a year. (2) The amount after one year. (3) A savings table. (4) 4% of $5 000. (5) Interest paid at the end of each year. (6) A story with a bank.
- **Think harder (4).** (1) $2 000 at 3% a year for 4 years earns $240 in simple interest (V29.1). (2) $5 000 at 4% for 3 years earns $600, and $5 000 at 3% for 5 years earns $750: the second plan is better (V29.6). (3) $84 buys 28 tickets at $3; after a 40% rise they cost $4.20 and the same money buys 20 (V29.3). (4) Pens are sold only in packs of 4 for $3: Dev says he paid $10; he cannot be right, every amount is a multiple of $3 (V29.5).
- **Go further (3).** G1 **Beyond (named): "Doubling Money".** At 8% simple interest a sum doubles in 12.5 years (V29.4). Why does it take longer than 10 years? Level note: the rule of doubling; secondary. G2 With the interest added in at the end of each year (compound), $1 000 at 5% earns $157.63 in 3 years against $150 simple (V29.2). A labelled preview. G3 Percentage change preview: a price up 25% and then down 25%.
- **Non-routine.** CTX T (V29.1, V29.6), MULTI T, POSE G (V29.5), CMP G Beyond (V29.4).
- **Numbers.** Principal to $10 000; rates 1% to 8%; years to 10.
- **Home materials.** Pencil.
- **Kit.** None cut. The lesson 22 shop cards are reused in the warm-up.
- **Figures.** `table`, `bar_model` (Y3).
- **Misconceptions.** Multiplying the rate by the principal and forgetting the years; adding the rate (3) instead of taking a percent; assuming interest is paid once; reading "4 for $3" as $4 each.
- **Needs.** RN5, RN10.

#### Lesson 30. Term 3 Review and Mi's Challenge Quest

- **Big idea.** Percent, parts and patterns together.
- **Strand.** Mixed Term 3 (lessons 21 to 29). **Holiday boundary:** H7, H9 and H10 stems are barred as for the lessons they mirror.
- **Quest in this lesson.** Minutes 35 to 55 after the break. Explore 10 and Mini-lesson 9 on choosing a plan for a Term 3 problem. See section 8.3 for the gates.
- **Objective.** Choose a model for a percent, unit or pattern problem and say why. Think harder: a fraction-then-percent chain; a quiz with a different scoring rule; a savings pattern. Go further: build a contest-style problem; Cheapest Ten.
- **Remember (6 min).** Three recall items from Term 3 strands: a percent of a quantity, a ratio unit, the gaps of a pattern.
- **Start here (6, a menu).** One quick item from each strand (the gates).
- **Think harder (4).** (1) A shop sold 40% of its pens on Monday and 1/4 of the rest on Tuesday and had 90 left: how many at first (200, V30.2). (2) A test of 20 questions scores 4 for a correct answer and -2 for a wrong one: a pupil who answers all and scores 56 has 16 correct (V30.3). (3) A saving pattern. (4) A percent of a remainder.
- **Go further (3).** G1 **Beyond (named): "Cheapest Ten".** Pens cost $3 each or 3 for $8: the least cost for exactly 10 pens is $27, not $24 + $4 (Q3.9). Level note: optimisation with offers. G2 A contest-style item the child sets up alone. G3 A pattern that grows by a fixed step and the week with a given total.
- **Non-routine.** MULTI T (V30.2), GC T (V30.3), PAT T, CHAL G, WAYS G Beyond (Q3.9).
- **Numbers.** Within the Term 3 ranges.
- **Home materials.** Pencil; the Quest Log stays closed in the book; a quest partner.
- **Kit.** None cut. The Quest Log is in Book 6.
- **Figures.** As the gates: `percent_grid`, `bar_model`, `pattern_fig`.
- **Misconceptions.** Using percent of the wrong whole; treating the Quest as a race.
- **Needs.** Quest builder (TL3).

### 1.5 Term 4: Shape, Logic and Strategy (lessons 31 to 40)

Can a new child join cold? Yes: the warm-ups recall the angle facts and the triangle sum, factors and remainders, balance and undo, and bar models; lessons 31 to 32 and 34 to 35 are stand-alone strands, so only the six minutes are assumed. **Safest to skip in exam weeks: lesson 39** (nothing later builds on it); lesson 37 is the next best; hardest to miss: 31, 36, 40. Year-end school exams fall in late October and November, so Term 4 is the lightest term in new content (plan open question 9). Lesson 40 holds the Year Quest and the showcase.

#### Lesson 31. Angles in Shapes

- **Big idea.** Split a polygon into triangles.
- **Strand.** Polygon angle sums are not in the primary syllabus (only the triangle sum is, p. 42); quadrilateral chains appear in the school papers because the parallelogram, rhombus and trapezium properties are P5 (p. 42). The words pentagon and hexagon are absent from the syllabus. Contest tag: none in SASMO except the clock. **Holiday boundary (H8):** the H8 extension shows that any four-sided shape has angles adding to 360 by tearing the corners or drawing a diagonal; H8 stretch 1, 5, 6, 9 and challenge 6, 8 chase angles in a parallelogram, trapezium, rhombus, a square with an equilateral triangle. Barred: the tearing and the diagonal explanation (they may appear as a recalled fact), a square with an equilateral triangle on a side or inside, a parallelogram with AB = AE. New: the sum for any polygon by triangulation, a regular polygon from its angle, a regular pentagon chain, the turtle walk.
- **Objective.** Use 360 degrees for a quadrilateral; find the sum for a pentagon (540) and hexagon (720) by dividing into triangles; find one angle of a regular polygon; walk round a polygon turning at each corner. Think harder: pentagon and hexagon sums; regular pentagon chain; draw a regular polygon from its angle. Go further: Turtle Walk.
- **Prerequisites.** Lesson 8; Primary 4 angle measuring.
- **Remember (6 min).** (1) The angle sum of a triangle is 180. (2) The angle facts card of lesson 8. (3) Spiral from H8: a quadrilateral has angles adding to 360.
- **Start here (6).** (1) Three angles of a quadrilateral are 95, 110 and 80: the fourth is 75. (2) Opposite angles of a parallelogram. (3) A rhombus with an angle of 70 and the other angles. (4) A trapezium between parallel lines. (5) Draw one diagonal of a quadrilateral and see two triangles. (6) A chain with a parallelogram.
- **Think harder (4).** (1) A pentagon splits into 3 triangles from one corner, so its angles add to 540; a hexagon splits into 4, so 720 (V31.1). (2) In a regular pentagon ABCDE each angle is 108; angle BAC is 36 and angle CAD is 36 (V31.3). (3) Each angle of a regular polygon is 140: it has 9 sides (V31.2). (4) True, false or not possible to tell: a polygon whose angles add to 720 has 6 sides (true).
- **Go further (3).** G1 **Beyond (named): "Turtle Walk".** A turtle walks round a polygon and turns at every corner; the turns add to 360 for any polygon (checked on 100 random polygons, V31.4). If each turn is 24 degrees the polygon has 15 sides (V31.2). Level note: exterior angles; secondary. G2 Each angle of a regular 12-sided polygon is 150 (V31.1). G3 Find the number of sides of a polygon whose angle sum is 1 260 (9, V31.5).
- **Non-routine.** GEO T (V31.3), LOG T, CHAL T (V31.2), PAT G Beyond (V31.4).
- **Numbers.** Whole degrees; polygons up to 12 sides.
- **Home materials.** Protractor (optional), ruler.
- **Kit.** None cut. Four printed polygon sheets (a task uses at most 3).
- **Figures.** `angle_fig` with regular-polygon and diagonal presets (Y6).
- **Misconceptions.** Using 180 x n instead of 180 x (n - 2); thinking the angles of a regular pentagon are 72; reading the turn as the inside angle.
- **Needs.** Y6.

#### Lesson 32. Triangles and Quadrilaterals

- **Big idea.** Properties sort shapes into families.
- **Strand.** MOE P5 Geometry: parallelogram, rhombus, trapezium, properties and unknown angles (p. 42); line symmetry is P4 (p. 39), a spiral and not a preview; diagonal properties are excluded at P4 (2.1, p. 39); tiling is not in the syllabus. **Holiday boundary (H8):** H8 stretch 1 (parallelogram with A = 3 x B), 5 (a trapezium with angles 84 and 97), 6 (a rhombus with diagonal AC), 9, challenge 2, 6. Barred: those numbers, especially 84 and 97 on a trapezium. New: "always, sometimes or never", diagonal families, a symmetric figure to complete about any mirror line.
- **Objective.** Name a shape from its properties; find unknown sides and angles; decide always, sometimes or never; complete a symmetric figure; classify by diagonals. Think harder: always, sometimes, never; which shape am I; complete a figure; a trapezium. Go further: Diagonal Detective; counterexamples.
- **Prerequisites.** Lessons 8 and 31.
- **Remember (6 min).** (1) Opposite angles of a parallelogram are equal. (2) A rhombus has four equal sides. (3) Spiral from H8: the angle sum of a triangle.
- **Start here (6).** (1) Name the shape: four equal sides, no right angles. (2) Find an angle of a rhombus. (3) Find a side of a parallelogram. (4) A trapezium between parallel lines. (5) Sort 12 shapes into families. (6) Complete a symmetric figure on a grid.
- **Think harder (4).** (1) A trapezium ABCD has AB parallel to DC, angle DAB = 72 and angle ABC = 115: angle ADC = 108 and angle BCD = 65 (V32.3). (2) A rhombus has equal diagonals: always, sometimes or never (sometimes: only when it is a square, V32.2). (3) Which shape am I: four equal sides and equal diagonals (a square, V32.1). (4) Complete the figure about a diagonal mirror line.
- **Go further (3).** G1 **Beyond (named): "Diagonal Detective".** Test five shapes on three questions: equal diagonals, perpendicular diagonals, diagonals that cut each other in half. The square says yes to all three, the rectangle to the first and third, the rhombus to the second and third, the parallelogram to the third only and the kite to the second only (V32.1). Level note: diagonal properties are excluded at P4; secondary. G2 A trapezium with a rhombus joined on one side: an angle chain. G3 A counterexample for "every quadrilateral with four equal sides is a square".
- **Non-routine.** EXP T (V32.2), DIAG T, LOG T (V32.1), GEO G, LOG G Beyond (V32.1).
- **Numbers.** Whole degrees; sides to 20 cm.
- **Home materials.** Ruler, small mirror (optional).
- **Kit (KT11 `shape_cards`, one page, 12 pieces to cut).** 12 cards: square, rectangle, rhombus, parallelogram, trapezium and kite, two of each, with equal sides and right angles marked. Contract: supplied 12, maximum used 12.
- **Figures.** `angle_fig` (Y6), `symmetry` grid with a mirror line at any angle (Y20).
- **Misconceptions.** A square is not a rectangle; a trapezium needs exactly one pair of parallel sides (some books say at least one); trusting a drawn figure's scale; reflecting across the wrong line.
- **Needs.** Y6, Y20, KT11.

#### Lesson 33. Clocks and Calendars

- **Big idea.** Time repeats in cycles.
- **Strand.** MOE P3 24-hour clock and finding start, finish or duration (2.1 to 2.3, p. 36) are recalled; angles between clock hands and calendar cycles are enrichment. Contest tag: clocks and calendars (SASMO 20-14, 21-14). **Holiday boundary (H8):** H8 stretch 7 and 8 (the angle between the hands at 5 and 8 o'clock; the turn of the minute hand in 10 and 45 minutes). Barred: those. New: the angle at any time, when the hands first meet after 3:00, how often in 12 hours, the weekday after 150 days, the weekday that occurs 53 times.
- **Objective.** Read the 12-hour and 24-hour clock; find the angle between the hands at any time; find when the hands meet; find the weekday after n days by remainder; find the start from the end across noon. Think harder: angle, meeting time, start from end, weekday. Go further: How Often Do the Hands Meet.
- **Prerequisites.** Lesson 31 (angles); primary clock reading.
- **Remember (6 min).** (1) The minute hand turns 6 degrees a minute. (2) The hour hand turns 30 degrees an hour. (3) Spiral from H8: the angle at 3 o'clock is 90.
- **Start here (6).** (1) Time differences across noon: 3:45 pm to 10:25 pm. (2) Change 2150 hours to 9:50 pm. (3) The angle between the hands at 4:00 is 120 (Q4.3). (4) The weekday after 3 days. (5) The same weekday dates on a calendar. (6) How many days in 3 weeks.
- **Think harder (4).** (1) The angle between the hands at 7:20 is 100 degrees (V33.1). (2) After 3:00 the hands first meet at 3:16 and 4/11 minutes (V33.2). (3) A film ends at 2:10 pm after 3 h 45 min: it began at 10:25 am (V33.5). (4) Today is Tuesday: 150 days later it is Friday (150 = 21 weeks and 3 days, V33.4).
- **Go further (3).** G1 **Beyond (named): "How Often Do the Hands Meet".** In 12 hours the hands meet 11 times and make a right angle 22 times (V33.3). Level note: relative speed of the hands, a secondary idea. G2 A common year of 365 days has one weekday 53 times: the weekday it starts on (V33.6). G3 A 24-hour pay problem: 2150 to 0630 at $9 an hour ($78, V33.7).
- **Non-routine.** GEO T (V33.1), BACK T (V33.5), PAT G (V33.4), LIST G Beyond (V33.3).
- **Numbers.** Times to the minute; days to 365; 24-hour times written 2150.
- **Home materials.** A real clock (optional); a calendar of any year.
- **Kit (KT12 `clock_kit`, one page, 6 pieces to cut).** 2 faces (not cut), 3 hour hands and 3 minute hands. Contract: a task uses 2 faces and 2 + 2 hands; supplied 2 + 3 + 3, maximum used 2 + 2 + 2. Loose hands, no fastener.
- **Figures.** `clock` with an arc between the hands (exists, Y21 check), `calendar` (exists).
- **Misconceptions.** Reading the hour hand on the number at 7:20; measuring the larger angle; counting today as day 1; thinking the hands meet every hour.
- **Needs.** Y21, KT12, RN6.

#### Lesson 34. Logic Grids and Digit Puzzles

- **Big idea.** Eliminate until one answer is left.
- **Strand.** Not an MOE topic. Cryptarithms and digit puzzles are Level 3 enrichment; a new joiner has not seen them. Contest tag: cryptarithms, logic (SASMO 19-22, 20-25, 21-19; 19-14, 19-24, 20-6). **Holiday boundary (H10):** H10 core 4 (three children and three pets), challenge 5 (design a logic puzzle), challenge 9 (four children in a row), stretch 8; the holiday course has no cryptarithm. Barred: pets and seating puzzles with those names and clues. New: a five-runner ordering puzzle, a liar puzzle, a cryptarithm in the ones column first.
- **Objective.** Use a logic grid or a list; solve an ordering puzzle with a unique answer; solve a liar puzzle by testing cases; solve an addition cryptarithm column by column. Think harder: five runners, a liar, a cryptarithm, an error. Go further: a 5-digit cryptarithm with carries.
- **Prerequisites.** Primary 4 addition.
- **Remember (6 min).** (1) Which two statements cannot both be true. (2) Ones digit of a sum. (3) Spiral from H10: three children and three pets by elimination.
- **Start here (6).** (1) A 3 by 3 grid with three clues. (2) Order three children from two clues. (3) Fill the ones column of AB + B = CB. (4) A two-clue number riddle. (5) Tick and cross in a grid. (6) Who is not telling the truth in a pair.
- **Think harder (4).** (1) Five runners V, W, X, Y, Z: V is neither first nor last, W is directly behind V, X is ahead of V, Y is ahead of X and Z is behind W; the order is Y, X, V, W, Z (V34.1). (2) Four children: exactly one lies. Ana: "Ben is lying". Ben: "Cara and Dev both tell the truth". Cara: "Ana is lying". Dev: "Ben and Cara both tell the truth". Ana is the liar (V34.2, and without the rule "exactly one liar" the clues do not decide). (3) ABC + BBB = DCCE has the single solution 562 + 666 = 1228 (V34.3). (4) Find the error in a digit-puzzle solution.
- **Go further (3).** G1 **Beyond (named): "Digit Detective".** ABACD + CAEF = CFFCC has one solution, 64675 + 7602 = 72277; the carry from the thousands column makes C = 7 (V34.4). Level note: cryptarithms with carries; Level 3 enrichment. G2 Several liars among five children. G3 A 5 by 5 square with diagonals (picture needed).
- **Non-routine.** LOG T (V34.1, V34.2), EXP T, LOG G Beyond (V34.4).
- **Numbers.** Letters stand for different digits; no number starts with 0; 3- to 5-digit sums.
- **Home materials.** Pencil.
- **Kit (KT13 `clue_cards`, one page, 12 pieces to cut).** 8 clue cards and 4 name cards; the 4 by 4 grids are printed, not cut. Contract: supplied 12, maximum used 12.
- **Figures.** `logic_grid` (Y16), `crypt` (Y17).
- **Misconceptions.** Letting two letters share a digit; forgetting the carry; testing one liar and stopping; assuming a clue is a name when it is a position.
- **Needs.** Y16, Y17, KT13.

#### Lesson 35. Odd, Even, Remainders and Extremes

- **Big idea.** Parity is an invariant, and the extreme case sets a limit.
- **Strand.** Not in the MOE primary list (remainder reasoning, last digits, worst-case counting, least and greatest possible). KIV: the most overloaded lesson; the plan moves "must be two the same" and "minimise the biggest" up to Think harder. Contest tag: SASMO 19-9, 19-20, 20-17, 21-15, 21-16, 21-24. **Holiday boundary (H10, H9):** H10 stretch 6 (smallest number above 1 leaving 1 when divided by 2 to 6) and H9 challenge 4(c) (135 legs cannot be right: parity). Barred: those. New: a total that must be odd, "n divides the dividend minus the remainder", a last digit of a product of powers, worst-case counting, least and greatest.
- **Objective.** Use odd and even rules; find divisors that leave a given remainder; find a last digit by its cycle; draw in the dark and be sure; find the least possible biggest. Think harder: parity, divisors, last digit, minimise the biggest. Go further: the biggest set with no multiples; a parity cap; In the Dark.
- **Prerequisites.** Lesson 2.
- **Remember (6 min).** (1) odd + even, odd x even, odd + odd. (2) 200 / 12 leaves 8. (3) Spiral from H10: a remainder of 1 is the same as 1 more than a multiple.
- **Start here (6).** (1) Odd or even: the sum of 5 odd numbers. (2) 4 521 is odd. (3) The last digit of 3 x 7. (4) The remainder of 47 / 5. (5) A division that leaves 3. (6) The last digit of 4 x 6 x 8.
- **Think harder (4).** (1) Twelve numbers, 5 odd and 7 even: the sum is odd whichever numbers they are (V35.1). (2) 200 divided by n leaves 8: n divides 192 and is more than 8: 12, 16, 24, 32, 48, 64, 96, 192, which add to 484 (V35.2). (3) The last digit of 3^15 x 7^10 is 3 (V35.3). (4) 40 sweets are shared among 6 children, all different and at least 1: the least the biggest share can be is 10 (V35.5).
- **Go further (3).** G1 **Beyond (named): "In the Dark".** A bag has 16 cards, 4 of each of 4 suits. You draw without looking: 9 draws are enough to be sure of 3 of one suit and 8 are not (V35.4); with socks of 5 colours, 6 draws make a pair. Level note: the pigeonhole principle; secondary. G2 From 1 to 20 the most numbers you can pick so that none is a multiple of another: 10 (V35.6). G3 Eight different whole numbers from 1 to 14; the product of any four is even and the sum is even: the least sum is 46 (V35.7).
- **Non-routine.** LOG T (V35.1), LIST T (V35.2, V35.5), EXP T (counterexample about remainders), LIST G (V35.6, V35.7), LOG G Beyond (V35.4).
- **Numbers.** Dividends to 500; powers to 20; sets from 1 to 20.
- **Home materials.** Pencil; a bag and a pack of playing cards (optional).
- **Kit (KT14 `draw_cards`, one page, 16 pieces to cut).** 16 cards, 4 symbols of 4 each. Contract: supplied 16, maximum used 16. A normal pack of playing cards works.
- **Figures.** `table`.
- **Misconceptions.** Odd + odd is odd; stopping at the first remainder; counting the worst case one short; calling a set with one multiple "no multiples".
- **Needs.** KT14, RN13.

#### Lesson 36. Working Backwards

- **Big idea.** Undo from the end.
- **Strand.** Process skill (pp. 13 to 14). **Holiday boundary (H10, H3, H7):** H10 core 1, 2, stretch 1, 7, challenge 1, 6 and the exit (Ravi's ticket and $5), H3 challenge 8, H7 challenge 2, 7, 9 (price before a discount; GST included; Mrs Tan's $54). Barred: all, including the plan's "fraction then a fixed amount, money at first" (the same move and structure as the H10 exit). New: money passed between three people, a fraction then a transfer, percent chains run backwards.
- **Objective.** Undo each step in reverse order and check by running forward. Think harder: fraction then percent; a transfer; a price. Go further: Doubling Swap.
- **Prerequisites.** Lesson 25.
- **Remember (6 min).** (1) 5 x [ ] - 4 = 21. (2) A number is halved and 3 is added to make 11. (3) Spiral from H10: undo a half.
- **Start here (6).** (1) Undo a two-step number machine. (2) Undo a discount: 20% off made the price $40. (3) A story with one fraction and the end. (4) Run the answer forward to check. (5) A table of steps. (6) A story with a fixed amount.
- **Think harder (4).** (1) A shop sold 30% of its eggs in the morning and 3/7 of the rest in the afternoon; 120 were left: 300 at first (V36.6). (2) Ali gave 1/3 of his money to Ben; Ben then gave 1/4 of his money to Ali; now Ali has $42 and Ben $30: at first Ali $48 and Ben $24 (V36.4). (3) After a 20% discount and 9% GST a bicycle cost $392.40: $450 (V36.5). (4) A chain with a table of steps.
- **Go further (3).** G1 **Beyond (named): "Doubling Swap".** Ali, Ben and Cara have $24 between them. Ali gives Ben and Cara enough to double their money; then Ben does the same for Ali and Cara; then Cara for Ali and Ben. Now they each have $8. Start: Ali $13, Ben $7, Cara $4 (V36.1, V36.2). Level note: working backwards through a symmetric process. G2 Make equal, then find the start. G3 Mixed fractions and money chains.
- **Non-routine.** BACK T (V36.6, V36.5), EQ T (V36.4), BACK G Beyond (V36.2), EQ G.
- **Numbers.** Money to $500; fractions with denominators to 8; percents to 40.
- **Home materials.** 24 counters and three cups for the doubling swap.
- **Kit.** None cut.
- **Figures.** `table`, `bar_model` (Y3).
- **Misconceptions.** Undoing in the original order; applying a percent to the wrong amount; treating a fraction of the remainder as a fraction of the start.
- **Needs.** Y3.

#### Lesson 37. The Long Question

- **Big idea.** Long questions are short ones joined together.
- **Strand.** Multi-step problems combining fractions, percent, rate and area (the Paper 2 question 17 form). **Holiday boundary:** none specific; the pieces repeat H3, H6 and H7 stems, which are barred. New: a three-step story with a fraction and a percent, a decimal unit chain, a charge in steps inside a story, a spare clue.
- **Objective.** Split a long question into parts; mark what is asked; use part (a) for part (b). Think harder: three-step; decimal chain; steps. Go further: Spare Clue; four-step.
- **Prerequisites.** Lessons 22, 24, 28 through the warm-up.
- **Remember (6 min).** (1) 30% of 60. (2) 2/7 of 42. (3) A bar model with a total.
- **Start here (6).** (1) A two-step story with a model. (2) Mark the question asked. (3) Find the missing step. (4) A bar model first, then the sum. (5) A table of steps. (6) Check by estimating.
- **Think harder (4).** (1) A shop had 60 kg of rice, sold 3/10 on Monday and 2/7 of the rest on Tuesday: 30 kg were left (V37.1). (2) A bicycle costs $450; a 20% discount and then 9% GST are added; a deposit of 25% is paid and the rest in 6 equal instalments of $49.05 (V37.5). (3) Ravi has $4.50 more than Siti; both save $3.60 and then Siti has 2/3 of Ravi's money: Siti had $5.40 and Ravi $9.90 at first (V37.2). (4) An audio guide costs $1.50 for the first 30 minutes and $0.80 for every further 15 minutes or part: 2 h 5 min costs $7.10 and $8.70 buys at most 165 minutes (V37.3).
- **Go further (3).** G1 **Beyond (named): "Spare Clue".** A rectangle has a perimeter of 36 cm and its length is 2 cm more than its width, and its area is 80 cm2: the sides are 8 and 10; the area clue was not needed, and with "area 84" no rectangle fits (V37.4). Level note: reading a problem for the clues it needs. G2 A four-step unit chain with decimals. G3 A step charge in a longer story.
- **Non-routine.** MULTI T (V37.1, V37.5), EQ G (V37.2), CTX G (V37.3), EXP G Beyond (V37.4).
- **Numbers.** Totals to $1 000; steps to 6; decimals to 2 places.
- **Home materials.** Pencil.
- **Kit.** None cut.
- **Figures.** `bar_model` (Y3), `table`.
- **Misconceptions.** Answering the first question; using the wrong amount in the second step; ignoring "or part of it".
- **Needs.** Y3, RN14 (two-part items).

#### Lesson 38. Children Set the Problem

- **Big idea.** If you can write one, you understand it.
- **Strand.** Posing and error analysis (pp. 13 to 14). **Holiday boundary:** the last question of every holiday lesson is "make up your own" (H1 challenge 1, H2 challenge 4, H3 challenge 1, H4 challenge 1, H5 challenge 5, H6 challenge 6, H7 challenge 1, H8 challenge 2, H9 challenge 2, H10 challenge 5). The term lesson does not repeat the open prompt; it gives structured posing.
- **Objective.** Change a number in a problem and re-solve; write a question for a given answer; find the error in a classmate's solution; write a puzzle with exactly one answer and show it has one. Think harder: write and check; find the error. Go further: Prove It Unique.
- **Prerequisites.** None beyond the warm-up.
- **Remember (6 min).** A worked solution with one wrong step to find (a warm-up version of the routine).
- **Start here (6).** (1) Change the numbers in a given problem. (2) Solve the new problem. (3) Write a question for the answer 24. (4) Find the wrong step. (5) Write a story for 12 x 5. (6) Swap and check.
- **Think harder (4).** (1) Write a new question with the same model as lesson 24 and check it by a bar. (2) Find the error in a classmate's solution. (3) Change one clue so the answer changes. (4) Write a two-part question where (b) uses (a).
- **Go further (3).** G1 **Beyond (named): "Prove It Unique".** "I am a 3-digit multiple of 7, my digits add up to 12 and my tens digit is 0." The seven numbers with tens digit 0 and digit sum 12 are 309, 408, 507, 606, 705, 804 and 903; only 903 is a multiple of 7 (V38.1, V38.2). Write one of your own and list the cases. Level note: proving an answer is unique. G2 A puzzle with a unique answer and a proof. G3 A puzzle where one clue is spare.
- **Non-routine.** POSE T, EXP T, CHAL G, LOG G Beyond (V38.1, V38.2).
- **Numbers.** Any within Terms 1 to 4.
- **Home materials.** Pencil, paper.
- **Kit.** None cut.
- **Figures.** None new.
- **Misconceptions.** A puzzle with two answers; a clue that contradicts another; the writer cannot solve it.
- **Needs.** None new; a puzzle page layout.

#### Lesson 39. Colouring, Cycles and Choices

- **Big idea.** Try a plan, then prove no smaller plan works.
- **Strand.** Not an MOE topic (graph colouring, repeated cycles); picture-heavy. Contest tag: colouring (SASMO 19-11, 20-24). No school-paper evidence. **Holiday boundary (H9):** H9 stretch 1 (beads red, red, blue, yellow, yellow, yellow, the 50th and the number of yellow in 100). Barred: that colour sequence. The printed book uses letters A to D, not colours.
- **Objective.** Colour a figure of circles joined by lines so joined circles differ; find the fewest colours with a proof; count colourings by choosing one circle at a time; find the nth colour of a repeating cycle. Think harder: count by multiplying; a ring of five; a cycle. Go further: Ten Circles.
- **Prerequisites.** None.
- **Remember (6 min).** (1) 3 x 2 x 2. (2) The 12th term of a cycle of 4. (3) Draw a path of 4 circles.
- **Start here (6).** (1) Colour a small figure with 3 colours (letters A, B, C). (2) Two joined circles: 6 ways with 3 colours. (3) Which figure needs only 2 colours. (4) A path of 4 circles with 3 colours: 24 ways (Q4.8). (5) Spot the wrong colouring. (6) The next circles in a repeating pattern.
- **Think harder (4).** (1) Six circles in a line, 4 colours: 4 x 3^5 = 972 colourings (V39.1). (2) Five circles in a ring: 30 colourings with 3 colours and none with 2 (V39.1). (3) A hub joined to a ring of five circles needs 4 colours (V39.1). (4) The colours repeat A, B, B, C: the 50th is B and there are 25 B's in the first 50 (V39.3).
- **Go further (3).** G1 **Beyond (named): "Ten Circles".** Ten circles form an outer ring of five, an inner five-pointed star and five joining lines (15 lines). 3 colours are enough in 120 ways and 2 colours are impossible because the ring of five needs 3 (V39.2). Level note: graph colouring (secondary). G2 A ring of four circles with 3 colours: 18 ways (V39.4). G3 A figure that needs 4 colours.
- **Non-routine.** WAYS T (V39.1), PAT T (V39.3), LIST G Beyond (V39.2).
- **Numbers.** Figures up to 10 circles; colours up to 4.
- **Home materials.** Pencil; four coloured pencils are not needed (letters).
- **Kit.** None cut. Six printed colouring pages (a task uses at most 4).
- **Figures.** `graph_colour` (Y15): presets path, ring, wheel and the ten-circle figure; labels A to D.
- **Misconceptions.** Using a colour twice next to each other; thinking a ring of five needs 2 colours; multiplying the colour count for every circle.
- **Needs.** Y15.

#### Lesson 40. Year Showcase and Mi's Challenge Quest

- **Big idea.** What would you tell a friend starting this year?
- **Strand.** Look back over the year; communicating (pp. 13 to 14). The Quest of the year.
- **Objective.** Teach one favourite idea or puzzle to the group in about a minute (a pass is always allowed); choose a move for a mixed set and say why; write a puzzle with a rule and a proof. Think harder: choose a move. Go further: Puzzle With a Proof.
- **Prerequisites.** None; a child who joins here does the Quest and the showcase on the ideas they know.
- **Remember (6 min).** Three "I remember" picks from the year, led by the tutor: a pattern, a way to count, a shape fact (volunteers; no one is put on the spot).
- **Start here (5).** Show a favourite page and say one thing about it, using a sentence frame; sort year-cards into "I know it well" and "I am learning it". Not marked.
- **Think harder (3).** (1) Choose a move for each of four problems from the year and say why. (2) Explain why a claim cannot be right. (3) Write a puzzle for a new Level 5 child.
- **Go further (3).** G1 **Beyond (named): "Puzzle With a Proof".** Write a puzzle that has a rule, solve it, and show why the answer must be right (draw it, list every case, or check a second way). The author gives a check list: unique answer, checked twice, no copied puzzle. G2 Check a friend's puzzle and say what is wrong. G3 A showcase problem you set and solve.
- **Quest in this lesson.** Minutes 35 to 55 after the break; the showcase follows (about 20 minutes, volunteers only); the workbook is light and the exit ticket is not live. See section 8.4.
- **Non-routine.** EXP T, POSE G, CHAL G, CHAL G Beyond.
- **Numbers.** Within Terms 1 to 4.
- **Home materials.** One favourite page from the year; plain paper; the Quest Log stays closed in the book; a quest partner.
- **Kit.** None cut. The Quest Log is in Book 8.
- **Safeguarding.** Showing work is voluntary; no "best", no ranking, no votes; puzzles are shared inside the group only unless a grown-up agrees (D9).
- **Figures.** None new; a puzzle-writing page.
- **Misconceptions.** A puzzle with two answers; copying a puzzle from the book; thinking a harder puzzle is better.
- **Needs.** Quest builder (TL3), puzzle page layout, parent report line.

## 2. Terms at a glance

Waves (explained in section 13): **A** = can be written once the stacked-fraction renderer (Y2) and the number-answer fields (RN10) exist, with kit work only; **B** = needs number, fraction or decimal figures (Y1, Y3, Y4, Y7); **C** = needs the geometry figure (Y5, Y6); **D** = needs solids, dice or tanks (Y8 to Y11); **E** = needs graph, pattern, balance, logic or colouring figures (Y12 to Y19); **Q** = a Quest lesson, built last in its term. Codes Y, KT, RN, TL are defined in section 5. Lessons 10, 20, 30 and 40 are retitled "... Review and Mi's Challenge Quest" (finding 2, D3).

### Term 1

| # | Title | Wave | Blocking template items | Beyond (named) | Safe to skip? |
|---|---|---|---|---|---|
| 1 | Shifting Places | B | Y1, KT1, RN10 | Cross Out a Digit | No, 2 and 6 use it |
| 2 | Factor Finders | A | RN13 | Locker Parade | No, 35 uses it |
| 3 | Smart Calculation | A | none | Bracket Bonanza | Fairly safe |
| 4 | Mixed Numbers and Sharing | B | Y2, Y3, KT2, RN9 | Halves Forever | No, 5, 24 and 37 use it |
| 5 | Fractions of Fractions | B | Y2, Y3, RN9 | Half-Way Squares | No, 21 to 24 use it |
| 6 | Decimal Sense | B | Y1, Y4, RN10 | Never-Ending Decimals | No, 14 and 21 use it |
| 7 | Boxed-In Triangles | C | Y5, Y6 | Dots Inside, Dots on the Edge | No, 15 uses it |
| 8 | Angles and Triangle Families | C | Y6, KT3, RN12 | Five-Point Star | No, 31 and 32 use it |
| 9 | Two Groups and the Overlap | B | Y7, Y3, RN13 | Squeeze the Overlap | Yes, safest in Term 1 |
| 10 | Term 1 Review and Mi's Challenge Quest | Q | TL3, Y1, Y6, Y7 | Exactly One | No (holds the Quest) |

### Term 2

| # | Title | Wave | Blocking template items | Beyond (named) | Safe to skip? |
|---|---|---|---|---|---|
| 11 | Solid Views and Dice | D | Y8, Y9, KT4 | Hidden Cubes | Fairly safe |
| 12 | Boxes and Bricks | D | Y9, RN13 | Least Wrapping | No, 13 and 19 use it |
| 13 | Tank Tales | D | Y11, RN1 | Stepped Tank | No, 20 uses it |
| 14 | Decimal Measures | B | Y4, RN1, RN10 | Rounding Rattle | Fairly safe |
| 15 | Cut and Rearrange | C | Y5, Y6, KT5 | Midpoint Squares | Fairly safe |
| 16 | Rate and Working Together | A | RN10, RN1 | Three Painters | No |
| 17 | Fair Shares | E | Y12, Y3 | Merging Classes | Fairly safe |
| 18 | Graph Stories | E | Y12, RN10 | Same Data, Two Stories | Yes, safest in Term 2 |
| 19 | Isometric Builders | D | Y10, Y9, RN7 | Complete the Cuboid | Fairly safe, next best |
| 20 | Term 2 Review and Mi's Challenge Quest | Q | TL3, Y8, Y9, Y11, Y12 | Pour and Measure | No (holds the Quest) |

### Term 3

| # | Title | Wave | Blocking template items | Beyond (named) | Safe to skip? |
|---|---|---|---|---|---|
| 21 | Percent Sense | B | Y22, Y4, Y2, RN10 | Percent of Percent | No, 22 and 23 use it |
| 22 | Shop Smart | A | KT6, RN5, RN10 | Tax on Tax | No |
| 23 | One Number as a Percent of Another | B | Y22, Y3, RN10 | Juice Mix | No |
| 24 | Unequal Parts | B | Y3, KT7, RN11 | Shared Part | No, 25, 36 and 37 use it |
| 25 | Balance and Undo | E | Y18, KT8, RN13 | Odd Coin Out | Fairly safe |
| 26 | Number Stories | E | Y13, Y14 | Not Always Doubling | Fairly safe |
| 27 | Count Without Counting | E | Y19, KT9 | Triangles Hiding | Fairly safe |
| 28 | Supposition Studio | A | KT10, RN13 | Nugget Numbers | Fairly safe |
| 29 | Money Grows | A | RN5, RN10 | Doubling Money | Yes, safest in Term 3 |
| 30 | Term 3 Review and Mi's Challenge Quest | Q | TL3, Y22, Y3, Y13 | Cheapest Ten | No (holds the Quest) |

### Term 4

| # | Title | Wave | Blocking template items | Beyond (named) | Safe to skip? |
|---|---|---|---|---|---|
| 31 | Angles in Shapes | C | Y6 | Turtle Walk | Fairly safe (KIV merge with 32) |
| 32 | Triangles and Quadrilaterals | C | Y6, Y20, KT11 | Diagonal Detective | Fairly safe |
| 33 | Clocks and Calendars | A | Y21, KT12, RN6 | How Often Do the Hands Meet | Fairly safe |
| 34 | Logic Grids and Digit Puzzles | E | Y16, Y17, KT13 | Digit Detective | Fairly safe |
| 35 | Odd, Even, Remainders and Extremes | A | KT14, RN13 | In the Dark | Fairly safe (KIV too full) |
| 36 | Working Backwards | A | Y3 | Doubling Swap | No |
| 37 | The Long Question | A | Y3, RN14 | Spare Clue | Yes, second safest in Term 4 |
| 38 | Children Set the Problem | A | none | Prove It Unique | Fairly safe |
| 39 | Colouring, Cycles and Choices | E | Y15 | Ten Circles | Yes, safest in Term 4 |
| 40 | Year Showcase and Mi's Challenge Quest | Q | TL3 | Puzzle With a Proof | No (holds the Quest and the showcase) |

## 3. Holiday no-repeat register

The rule (owner, 22 Oct): all four terms are new content and holiday lessons are not reused; spiral review of a holiday topic is allowed in the first six-minute warm-up only. A holiday graduate starts Term 1, 2 or 3 and must never meet a holiday item again. Overlap: **Heavy** = the term lesson is the same strand and the same kinds of item as a holiday lesson, so only the barred list and a new angle keep it new; **Medium** = shared strand with a different focus; **Light** = one or two items; **None** = no holiday counterpart. Counts: Heavy 19, Medium 10, Light 7, None 4. The holiday lessons are H1 Million Puzzles, H2 Fraction Feats, H3 Before and After, H4 Triangle Areas, H5 Volume Vault, H6 Rate Racers, H7 Percentage Puzzles, H8 Angle Chasers, H9 Pattern Generalisers, H10 Challenge Day; item references "core", "stretch" and "challenge" are the Start here, Think harder and Go further banks of `p5/content/lN.js`.

The lesson authors must check every item against `p5/content/l1.js` to `l10.js` (the 7-word overlap check against those files is part of TL2) before the wording review. The type of move may recur (a fraction of a remainder run backwards appears in lessons 5, 25, 30 and 36 by design); the stem, context and numbers may not. Holiday graduates will recognise the topic but not the questions, and the tutor guide says so.

| L | Closest holiday lesson and items | Overlap | Barred in the term lesson | What is new |
|---|---|---|---|---|
| 1 | H1 digit cards, rounding, estimates, brackets, digit riddles | Heavy | closest to a target, greatest and smallest 7-digit number, digit-sum riddles, palindromes, 1 000 000 as a product, a heart beating a million times, digits written 1 to 1000 | shift mat, x and / by multiples of powers of ten, Cross Out a Digit, smallest even number |
| 2 | H10 stretch 6, H5 core 2, H1 digit sums | Medium | rectangles from 12, 60 or 64 cubes, remainder 1 for divisors 2 to 6, 7-digit digit riddles | factors, packing, LCM, digit tests, lockers |
| 3 | H1 stretch 2, 8, 9 and challenge 5, 7 (brackets and targets) | Heavy | brackets in 2+3x4+5, digits 2, 3, 5, 7 to 29, 31, 100, four 4s, 1 2 3 4 5 to 100, the biggest value of 1+2x3+4x5+6 | regrouping, cancelling, parity, choose the expression, count the bracketings |
| 4 | H2 core 1 to 6, stretch 1 to 9, challenge 1 to 9 | Heavy | 3 bars among 4, 4 l into 6 bottles, 5 pizzas among 12, unit-fraction sums, 1/2 - 1/3 patterns, 5/6 against 6/7 | mixed-number sums with regrouping, a tank story, tickets by fractions, Halves Forever |
| 5 | H2 core 4, 5, stretch 2, 8, 9, challenge 2, 3, 5; H3 core 3, challenge 8 | Heavy | telescoping product to 99/100, digit cards 1 2 3 4 and 1 3 5 7, cookies by 1/2, 1/3, 1/4, give half and 4 more twice | area-model products, digit cards 2 4 5 9 for a product, 3/5 of red = 3/4 of blue, Half-Way Squares |
| 6 | H6 core 6, H7 GST, H5 core 6 | Light | nuts at $1.50 per 100 g, 2.5 l in ml | decimals by 10, 100, 1 000, rounding bounds, never-ending decimals |
| 7 | H4 whole lesson | Heavy | a point on the top side of a rectangle, two squares 10 and 6, triangle ABC 54 with BD 4 and DC 8, the 13-14-15 triangle, a square with a triangle on top, area 42 with base 12 | tilted triangles by boxing in, Pick's rule, ratio of a square and a triangle |
| 8 | H8 whole lesson | Heavy | tearing corners, 127 on a line, isosceles 110, 20, 30 more, 30-60-90 joined, an angle bisector, D on AC with BD = BC, clock angles | exterior angle, AB = BD and AD = DC chain, true/false/not possible, the star |
| 9 | H3 core 5, H7 challenge 5 | Light | 40 pupils with 3/8 boys, 800 pupils with 45% boys | Venn, at least one, pair totals, least and greatest overlap |
| 10 | H10 whole lesson | Medium | every H10 stem and its exit ticket (1/2 on a ticket, $5 on a snack, $7 left) | unit chain with a transfer, a repeating block, an ordering puzzle, exactly one answer |
| 11 | H5 stretch 4, challenge 1, 8 | Medium | painting the whole outside of a 3 x 4 x 5 cuboid, 96 cubes with one painted face | views, dice and nets, two painted faces, hidden cubes |
| 12 | H5 core 1 to 4, stretch 1, 3, challenge 2, 6, 7 | Heavy | 3 x 2 x 2, 12 cubes into rectangles, 2-cm cubes in 9 x 6 x 5, square base with volume 245, 64 cubes, 2 x 3 x 4 bricks into a cube, faces 12, 15, 20 | volume 72 listed, 3-cm cubes in 25 x 17 x 13, surface for wrapping |
| 13 | H5 more than a dozen tank and litre items | Heavy | 1/3 to 3/5 with 12 l, a rock raising 8 to 10 cm, 60 x 40 x 50 and buckets, 36 l in 40 x 30, a 20 cm cube poured in, 3 l and a stone, A and B equal depth, a 10 cm cube, 4 bricks, a block stood in 30 x 20 | fraction and amount, 4.5 l in 50 x 30, block upright and laid, a stepped floor |
| 14 | H5 core 6, H6 core 6, H7 | Light | 2.5 l in ml, 650 g of nuts, GST on $20 | mixed-unit bills, kg and g answers, water-bill table, rounding bounds |
| 15 | H4 challenge 2, 4 and midpoints | Medium | P and Q midpoints of a 12 x 8 rectangle, a point on the top side of a square | midpoint squares, parallelogram and trapezium cut, folded corner |
| 16 | H6 whole lesson | Heavy | 4 apples for $2, a printer at 24 a minute, car parks at $1.50 + $1 and $1.20 + 60¢, eggs 10 and 6, three shops with cans, two printers sharing 900, a crack in a tank, a bath with the plug out, a candle race | postage steps, a taxi, a tap and drain with new numbers, pair rates of work |
| 17 | none | None | - | average and its effects |
| 18 | none | None | - | line graphs, axes, pie chart total |
| 19 | none (H5 is flat) | None | - | isometric drawing, turned figures, matrix |
| 20 | H5, H6, H10 | Medium | as the lessons it mirrors | buy 2 get 1 free, Pour and Measure |
| 21 | H7 core 1 to 6, stretch 3, 7, 8 | Heavy | 35 of 100 shaded, 50%, 25%, 10% of $80, 10% off $50, 24 of 40, 15% as 10% + 5%, 30% of 70 against 70% of 30, 18/25 against 27/40 | mixed forms in order, class-size condition, which class had 40%, percent of a percent |
| 22 | H7 core 3, 6, stretch 2, 4, 5, challenge 2, 7, 8; H6 stretch 6, 9 | Heavy | 10% off $50, GST on $20, buy 3 get 1 free against 30% off, a $250 bicycle at 12%, an $80 watch, the price before a 20% discount, $109 including GST, an $80 lamp 25% against 10% + 15%, 4 pens for $3 + 1 free, three shops with cans | service charge and GST, buy 4 get 1 free for a club, singles and packs, GST included |
| 23 | H7 core 4, stretch 6, challenge 3, 4, 5, 6, 9 | Heavy | 24 of 40, 40% then 50% of the rest, a tank 40% to 70%, scores up and down 20%, the school bus, 75% red marbles, Mrs Tan's $54 | nearest whole percent, 52% of the cars, juice mixture |
| 24 | H3 whole lesson | Heavy | counters 18 and 6, ages in 5 years, 1/4 and 1/3 of $60, stamps made equal, 3/8 boys, red and blue beads, a box 3/7 red, 3/5 as many cards, a father and son 50 in all, 1/5 of an age years ago, 3/5 and 1/2 as many after giving | price model, ratio and gift, linked ratios, ages with new numbers |
| 25 | H10 core 1, 2, stretch 1, 7, 8, challenge 1, 6; H3 challenge 8; H9 stretch 3 | Heavy | a number times 4 minus 6, Ali's book, think of a number, the bus, the monkey, give half and 4 more twice, 35 heads and 94 legs | two-step equations with boxes, balance shapes, find the error, Odd Coin Out |
| 26 | H9 whole lesson | Heavy | 5 9 13 17, matchstick squares 4 7 10, 2 6 10 14, 3n + 2, beads red red blue yellow yellow yellow, 40 tables, 1 + 3 + 5 + ..., saving $3 and $2 more, 3 8 13 18 above 200, a staircase, squares on 4 x 4, matchstick grids, diamonds, digits of pages | gaps of the gaps, woven sequences, n x n + 4, triangle numbers over 300, chords on a circle |
| 27 | H9 challenge 3, 5, 9; H10 challenge 2, 3, 4; H1 challenge 9 | Heavy | squares on a 4 x 4 grid, digits for pages 1 to 150, the 100th digit, digits 1 to 1000, rectangles in a strip and in 3 x 4, the digit 4 from 1 to 50 | posts and gaps, triangles by rays, handshakes, pages from digits, numbers with different digits |
| 28 | H9 core 4, 6, stretch 3, 8, challenge 4, 8; H10 core 6, stretch 5, challenge 8 | Heavy | bicycles and tricycles, chickens and goats, spiders and beetles, pens $2 and files $3, quiz +3 and -1, quiz +4 and -1 and blanks, 14 coins worth $4.90, 25 coins worth $5.30 | tickets at $12 and $7, extra and short, 5c and 8c stamps, ways to pay $1.20 |
| 29 | H7 stretch 1, challenge 4 | Light | price up then down by a percent | annual interest, plans, price rise, packs |
| 30 | H7, H9, H10 | Medium | as the lessons it mirrors | a fraction-then-percent chain, a different quiz rule, Cheapest Ten |
| 31 | H8 extension, core 6, stretch 1, 5, 6, 9, challenge 6, 8 | Medium | tearing the corners of a four-sided shape, a square with an equilateral triangle, a parallelogram with AB = AE | polygon sums by triangulation, regular polygons, Turtle Walk |
| 32 | H8 stretch 1, 5, 6, 9, challenge 2, 6 | Heavy | A = 3 x B in a parallelogram, a trapezium with angles 84 and 97, a rhombus with diagonal AC | always, sometimes, never, diagonal families, symmetry |
| 33 | H8 stretch 7, 8 | Light | the angle between the hands at 5 and 8 o'clock, the minute hand in 10 and 45 minutes | any time, meeting time, 150 days later, 53 weeks |
| 34 | H10 core 4, stretch 8, challenge 5, 9 | Medium | three children and three pets, four children in a row, designing a logic puzzle | five runners, a liar puzzle, cryptarithms |
| 35 | H10 stretch 6, H9 challenge 4(c) | Light | remainder 1 for 2 to 6, 135 legs cannot be right | parity totals, remainder trick, last digit, worst case, extremes |
| 36 | H10 core 1, 2, stretch 1, 7, challenge 1, 6 and exit; H3 challenge 8; H7 challenge 2, 7, 9 | Heavy | Ravi's ticket and $5, Siti's 2/5 and 1/3, the bus, the monkey, the price before a discount, $109 with GST, Mrs Tan's $54 | money passed among three people, a fraction then a transfer, discount and GST run backwards |
| 37 | H3, H6, H7 stems | Medium | their stems | three-step with a fraction and a percent, a decimal chain, an audio-guide charge, a spare clue |
| 38 | the last question of every holiday lesson (make up your own) | Medium | the open prompt itself | structured posing, change one number, error finding, unique answers |
| 39 | H9 stretch 1 | Light | beads red red blue yellow yellow yellow | graph colouring, ten circles, counting by choices |
| 40 | none | None | - | year review, showcase, Puzzle With a Proof |

## 4. Non-routine assignments (checked against the Primary 5 catalogue and the holiday register)

The owner decided on 23 Oct that every term plan names, for each lesson, the non-routine types it carries, the tier (Think harder or Go further, never Start here) and original examples, with the spiral shown as a type-by-lesson matrix. The Level 5 plan already holds that section (`level_5_year_plan.md`, "Non-routine assignments", checked: it is Level 5 text, 2279 items, 16 types; unlike the Level 3 plan it was not written from another level's catalogue). This section keeps the plan's types, **replaces every item that repeats a holiday item or a SASMO problem** (section 3), adds the check ids, and re-draws the matrix. Source: `docs/books/p5_non_routine_catalogue.md` (2279 non-routine questions from 166 papers, 19 schools, 2020 to 2025; the per-type tables) and `docs/books/p5_school_paper_patterns.md`. Examples are original and script-verified (appendix); no school text is copied. 965 of the 2279 school items need a picture (a floor, not a count), so every picture-dependent item needs a drawn figure on the page (section 5).

How to read it. Types: EQ unit and equal-share models; GEO geometry chains; LOG logic and statements; CTX unfamiliar context; LIST systematic list, greatest and least; MULTI multi-step; BACK work backwards; CHAL draw or design; EXP explain, choose the expression, find the error; TAB table or graph; GC guess and check, supposition; PAT patterns; DIAG diagram, view or solid; CMP sum and difference, average; WAYS most, least and offers; POSE pose or judge a statement. **T** = Think harder, **G** = Go further. Status is N for every entry (planned; no Level 5 term lesson is written). The named Beyond puzzle takes one of the Think harder or Go further slots. Papers do not name the heuristic in the stem: a Think harder item may name the tool for a type that is new in that term, Go further drops it.

### 4.1 Lesson by lesson

| # | Lesson | Non-routine types (tier): what (check) |
|---|---|---|
| 1 | Shifting Places | LIST T: smallest even number from four digit cards (V1.4); EQ T: 5 times as many, then seats added (V1.3); POSE G: a number that rounds to 400 000 with a digit sum clue (V1.5); LOG G: Cross Out a Digit (V1.2) |
| 2 | Factor Finders | LIST T: pack two kinds of fruit into the most identical bags (V2.3); LIST G: smallest number over 200 shared by 9 or 12 (V2.4); LOG T: exactly five factors, true/false/not possible to tell (V2.2); LOG G: a three-condition riddle (V2.5); EXP G: a counterexample about multiples (V2.8); PAT G: Locker Parade (V2.7) |
| 3 | Smart Calculation | EXP T: choose the expression for a shopping story (V3.5); LOG T: odd or even without calculating (V3.3); POSE G: make 24 from 3, 4, 6, 9 (V3.6); WAYS G: count the values of all bracketings (V3.4) |
| 4 | Mixed Numbers and Sharing | MULTI T: 3/7 then 3/8 of the rest (V4.3); CTX T: mixed numbers in a tank story (V4.7); EQ G: 3/4 of red equals 2/3 of blue (V4.4); PAT G: Halves Forever (V4.5) |
| 5 | Fractions of Fractions | MULTI T: 3/5 then 1/4 of the rest, then a difference (V5.4); LIST T: digit cards 2, 4, 5, 9 for fraction products (V5.2); EQ T: 3/5 of red equals 3/4 of blue (V5.6); BACK G: a two-stage chain with thirds and halves (V5.5); PAT G: Half-Way Squares (V5.3) |
| 6 | Decimal Sense | EQ G: a decimal unit chain (V6.5); CMP T: sum and difference of two decimals (V6.4); LIST T: least and greatest 2-decimal numbers that round to 4.3 (V6.3); POSE T: a decimal between two others; PAT G: Never-Ending Decimals (V6.6) |
| 7 | Boxed-In Triangles | GEO T: a tilted triangle by boxing in (V7.1); EXP T: true/false/not possible to tell about equal heights; GEO G: a square and a triangle in the ratio 3 : 8 (V7.3); CHAL G: a rectangle of twice the area on a grid (V7.4); PAT G: Pick's rule (V7.2) |
| 8 | Angles and Triangle Families | GEO T: the exterior angle and a joined-triangles chain (V8.1, V8.2); LOG T: true/false/not possible to tell about angles (V8.5); GEO G: the same chain with new angles; EXP G: is it a parallelogram (V8.6) and Five-Point Star (V8.4) |
| 9 | Two Groups and the Overlap | CMP T: three pair totals (V9.3); TAB T: a two-way table and a percent (V9.5); LOG T: an ordering puzzle (V9.6); MULTI G: two groups with different fractions (V9.4); LIST G: Squeeze the Overlap (V9.2) |
| 10 | Term 1 Review and Mi's Challenge Quest | EQ T: 4 times as many, then a transfer (V10.1); BACK T: 2/5 then a fixed amount (V10.2); PAT T: a repeating block (V10.3); LOG G: four runners (V10.4); CHAL G: Exactly One (V10.5) |
| 11 | Solid Views and Dice | DIAG T: a numbered top view and its three views (V11.5); LOG T: dice towers and rows (V11.2, V11.3); LIST T: two painted faces (V11.4); LIST G: cubes that can be added (V11.7); DIAG G: Hidden Cubes (V11.6) |
| 12 | Boxes and Bricks | LIST T: the most 3-cm cubes in a box (V12.2); EQ T: a longer box with 300 cm3 more (V12.4); EXP T: statement about equal volumes; WAYS G: every cuboid of volume 72 and Least Wrapping (V12.1) |
| 13 | Tank Tales | BACK T: 3/10 full, 3.5 l more (V13.2); CTX T: 4.5 l poured into a tank (V13.4); EXP T: a statement about depth; DIAG G: a block upright and laid (V13.3); DIAG G: Stepped Tank (V13.1) |
| 14 | Decimal Measures | CTX T: a bill in metres and kilograms (V14.3); TAB T: a water-bill table (V14.5); POSE G: two readings that round to 3.4; CMP G: Rounding Rattle (V14.2) |
| 15 | Cut and Rearrange | GEO G: a folded corner, 25 and 71 (V15.3); EXP T: parallelogram and rectangle on a base; CHAL T: draw a parallelogram with the area of a triangle; PAT G: Midpoint Squares (V15.1) |
| 16 | Rate and Working Together | CTX T: postage in steps (V16.2); CTX G: a taxi, greatest distance (V16.5); TAB T: a charge table; GC T: tap and drain, two workers (V16.3, V16.6); CMP G: Three Painters (V16.1) |
| 17 | Fair Shares | CMP G: a seventh score for a new average (V17.1); CHAL T: the missing bar (V17.3); TAB T: closest to the average; EXP G: an average that no number is near (V17.5); CMP G: Merging Classes (V17.2) |
| 18 | Graph Stories | TAB G: in which hour did the water drain fastest (V18.1); CHAL T: draw a line graph from a story; EXP T: a misleading axis; TAB T: a pie chart total (V18.3); EXP G: Same Data, Two Stories (V18.4) |
| 19 | Isometric Builders | DIAG T: faces you can see on an isometric cuboid (V19.1); LIST G: cubes to add keeping two views (V19.2); DIAG G: a turned block figure; LIST G: Complete the Cuboid (V19.3) |
| 20 | Term 2 Review and Mi's Challenge Quest | CTX T: buy 2 get 1 free for a class (V20.2); GEO G: perimeter given, area asked; EQ G: a bar model with a fraction and a difference; CHAL G: Pour and Measure (V20.1) |
| 21 | Percent Sense | POSE T: why 35% of 18 pupils cannot be right (V21.1); EXP T: order mixed forms (V21.3); LOG T: which class had 40% of the items (V21.4); TAB T: a percent from a two-way table; EXP G: Percent of Percent (V21.2) |
| 22 | Shop Smart | MULTI T: discount then GST (V22.2); CTX T: buy 4 get 1 free (V22.3); WAYS T: singles and packs (V22.4); CTX G: two shops; EXP G: Tax on Tax (V22.1) |
| 23 | One Number as a Percent of Another | LOG T: true/false/not possible to tell about 52% red (V23.3); MULTI T: a percent of a remainder (V23.4); BACK G: find the whole (V23.1, P6 preview); CMP G: Juice Mix (V23.2) |
| 24 | Unequal Parts | EQ T: a case costs $7 more than a ruler (V24.1); EQ G: a ratio before and after a gift (V24.2); CMP G: Shared Part (V24.3, V24.4); EQ T: ages (V24.5, V24.6) |
| 25 | Balance and Undo | EQ T: balance with two shapes (V25.5); EXP T: find the error in a worked solution (V25.3); BACK G: a two-stage chain with fifths and thirds (V25.4); LOG G: Odd Coin Out (V25.1) |
| 26 | Number Stories | PAT T: gaps of the gaps, woven, n x n + 4, triangle numbers over 300 (V26.1, V26.2, V26.6, V26.3); TAB T: a table for a growing figure; PAT G: Not Always Doubling (V26.4); LOG G: a rule from three examples (V26.5) |
| 27 | Count Without Counting | DIAG T: triangles by rays (V27.2); WAYS T: a line with two apart (V27.3); LIST T: pages from digits (V27.4); WAYS G: handshakes among 9 (V27.3); LIST G: numbers with different digits (V27.5); DIAG G: Triangles Hiding (V27.2) |
| 28 | Supposition Studio | GC T: tickets at $12 and $7 (V28.1); GC T: extra and short (V28.2, V28.6); WAYS T: ways to pay $1.20 (V28.4); LIST G: stamps that cannot be made, Nugget Numbers (V28.3) |
| 29 | Money Grows | CTX T: simple interest and two plans (V29.1, V29.6); MULTI T: a price rise and fewer tickets (V29.3); POSE G: could he be right (V29.5); CMP G: Doubling Money (V29.4) |
| 30 | Term 3 Review and Mi's Challenge Quest | MULTI T: a fraction then a percent chain (V30.2); GC T: a quiz with +4 and -2 (V30.3); PAT T: a savings pattern; CHAL G: a contest-style item set by the child; WAYS G: Cheapest Ten (Q3.9) |
| 31 | Angles in Shapes | GEO T: a regular pentagon chain (V31.3); LOG T: statements about angle sums; CHAL T: draw a regular polygon from its angle (V31.2); PAT G: Turtle Walk (V31.4) |
| 32 | Triangles and Quadrilaterals | EXP T: always, sometimes or never (V32.2); DIAG T: complete a symmetric figure; LOG T: which shape am I (V32.1); GEO G: a trapezium with a rhombus on one side (V32.3); LOG G: Diagonal Detective (V32.1) |
| 33 | Clocks and Calendars | GEO T: the angle between the hands (V33.1); BACK T: start from the end across noon (V33.5); PAT G: the weekday after 150 days (V33.4); CTX G: pay by the hour across midnight (V33.7); LIST G: How Often Do the Hands Meet (V33.3) |
| 34 | Logic Grids and Digit Puzzles | LOG T: five runners, a liar (V34.1, V34.2); EXP T: the error in a digit puzzle; LOG G: Digit Detective (V34.4) |
| 35 | Odd, Even, Remainders and Extremes | LOG T: a total that must be odd (V35.1); LIST T: divisors with a remainder, minimise the biggest (V35.2, V35.5); EXP T: a counterexample about remainders; LIST G: no multiples, the parity cap (V35.6, V35.7); LOG G: In the Dark (V35.4) |
| 36 | Working Backwards | BACK T: a percent and a fraction run backwards (V36.6, V36.5); EQ T: a fraction transfer (V36.4); BACK G: Doubling Swap (V36.2); EQ G: make equal then find the start |
| 37 | The Long Question | MULTI T: three-step with a fraction and a percent (V37.1, V37.5); EQ G: a decimal unit chain (V37.2); CTX G: a step charge in a story (V37.3); EXP G: Spare Clue (V37.4) |
| 38 | Children Set the Problem | POSE T: write a new question and check it; EXP T: find the error in a classmate's solution; CHAL G: a puzzle with a unique answer; LOG G: Prove It Unique (V38.1, V38.2) |
| 39 | Colouring, Cycles and Choices | WAYS T: count colourings by choosing (V39.1); PAT T: the nth colour of a cycle (V39.3); LIST G: Ten Circles, a proof it cannot be fewer (V39.2) |
| 40 | Year Showcase and Mi's Challenge Quest | EXP T: choose a move for a mixed set and say why; POSE G: explain why a claim cannot be right; CHAL G: Puzzle With a Proof |

### 4.2 Matrix: type by lesson (the spiral across the year)

`T` = Think harder only, `G` = Go further only, `B` = both; `.` = not planned. Lessons 1 to 40 in four groups of ten (one group per term). No type sits at Start here.

```
Lesson   1234567890 1234567890 1234567890 1234567890
Term     1111111111 2222222222 3333333333 4444444444
EQ       T..GTG...T .T.......G ...BT..... .....BG...
GEO      ......BB.. ....G....G .......... TGT.......
LOG      GBT....TTG T......... T.T.GG.... TB.BB..G..
CTX      ...T...... ..TT.B...T .B......T. ..G...G...
LIST     TB..TT..G. BT......G. ......BG.. ..G.B...G.
MULTI    ...TT...G. .......... .TT.....TT ......T...
BACK     ....G....T ..T....... ..G.G..... ..T..B....
CHAL     ......G..G ....T.TT.G .........G T......G.G
EXP      .GT...TG.. .TT.T.GT.. BG..T..... .T.TT.GT.T
TAB      ........T. ...T.TTB.. T....T.... ..........
GC       .......... .....T.... .......T.T ..........
PAT      .G.GGGG..T ....G..... .....B...T G.G.....T.
DIAG     .......... B.G.....B. ......B... .T........
CMP      .....T..T. ...G.GG... ..GG....G. ..........
WAYS     ..G....... .G........ .T....BT.G ........T.
POSE     G.G..T.... ...G...... T.......G. .......T.G
```

| Type | Lessons | Terms with it | School items (2279) |
|---|---|---|---|
| EQ | 11 | T1, T2, T3, T4 | 492 |
| GEO | 7 | T1, T2, T4 | 382 |
| LOG | 16 | T1, T2, T3, T4 | 164 |
| CTX | 9 | T1, T2, T3, T4 | 300 |
| LIST | 13 | T1, T2, T3, T4 | 45 |
| MULTI | 8 | T1, T3, T4 | 80 |
| BACK | 7 | T1, T2, T3, T4 | 193 |
| CHAL | 10 | T1, T2, T3, T4 | 23 |
| EXP | 18 | T1, T2, T3, T4 | 93 |
| TAB | 7 | T1, T2, T3 | 99 |
| GC | 3 | T2, T3 | 30 |
| PAT | 12 | T1, T2, T3, T4 | 98 |
| DIAG | 5 | T2, T3, T4 | 127 |
| CMP | 8 | T1, T2, T3 | 97 |
| WAYS | 7 | T1, T2, T3, T4 | 49 |
| POSE | 8 | T1, T2, T3, T4 | 7 |

### 4.3 Departures from the year plan's own table (and why)

(a) **Lesson 5** keeps the BACK G chain but with new fractions and amounts (the plan's EX-BACK-3 mirrors H3 challenge 8). (b) **Lesson 13** drops the plan's "pour into a second tank until equal" (H5 stretch 10) and uses a fraction-and-amount item and a new depth item. (c) **Lesson 16** keeps the car-park idea as postage and a taxi (H6 stretch 3 and 12 use two car parks). (d) **Lesson 21** drops EXP T "25% of 80 and 80% of 25" (H7 stretch 7) and uses the order of mixed forms. (e) **Lesson 25** drops GC T "heads and legs" (H9 stretch 3) and keeps balance with two shapes. (f) **Lesson 26** drops the matchstick figure, the repeating beads and the staircase (H9) and uses gaps of the gaps, woven sequences, n x n + 4 figures, triangle numbers over 300 and chords on a circle. (g) **Lesson 27** drops "digits used in page numbers" (H9 challenge 5, H1 challenge 9) and asks the reverse. (h) **Lesson 28** keeps GC and WAYS but with tickets, extra and short, stamps and coins that are not in H9 or H10; the plan's "least cost with two pack sizes" moves to lesson 22 (WAYS T). (i) **Lesson 30** keeps a quiz-scoring item as a review of lesson 28's move with a new rule (+4, -2, no blanks). (j) **Lesson 36** drops BACK T "fraction then a fixed amount" (the H10 exit ticket has that structure) for a percent-and-fraction chain. (k) Added to the plan's table: EXP at 3, 12, 17, 21; WAYS at 3, 12; CMP at 14, 16, 24, 29; PAT at 2, 4, 5, 6, 7, 15 (the Beyond puzzles of those lessons are pattern discoveries); POSE at 6, 21; LIST at 5, 6, 9, 11, 19, 27, 28, 33, 35. Types below the plan's lesson counts: TAB (7 against the plan's 8); GC (3 against the plan's 4). All other types meet or exceed them (GEO, LOG, LIST, CHAL, EXP, PAT, DIAG, CMP, WAYS are above). GC is lower because lesson 25's heads-and-legs entry was dropped (H9 stretch 3) and the papers give GC only 30 of 2279 items (D4).

### 4.4 Paper-based changes this plan adopts (from `p5_school_paper_patterns.md` section 4)

1. A unit-chain Think harder item in lessons 4, 5, 6, 9 and 10 (the first weighted assessment already sets them): in the specs above lessons 4 (V4.3), 5 (V5.4, V5.6), 6 (V6.5), 9 (V9.4) and 10 (V10.1). 2. True, false or not possible to tell in lessons 1, 2, 7, 8, 12, 13, 15, 23 and 31 (and the always, sometimes or never form in 32): with all three choices in the stem. 3. Angle chains of two to four steps in lesson 8; quadrilateral chains in 31 and 32; an angle warm-up in each Review lesson (10, 20, 30). 4. Ratio of areas and "any point on a side" in lessons 7 and 15. 5. Charges in steps and "greatest distance" in lesson 16; buy-more-get-free and discount then GST in 22; least cost with two pack sizes in 22 and 28. 6. Packing and sharing with HCF and LCM in lesson 2; the greatest number of cubes in lessons 11, 12 and 19. 7. A block laid in the water in lesson 13. 8. A repeating-pattern item in the Term 1 review. 9. Average (17) and ratio notation (24) stay labelled previews; "times as many" and "for every" are taught at Start here in lesson 24. 10. Lessons 9, 33 to 35, 38 and 39 are labelled optional where the papers show no evidence (finding 10).

## 5. New template capabilities Level 5 needs beyond `term/l1/tools`

Codes: **Y** figure, **KT** kit page, **RN** online runner, **TL** term-level tool. Hours are template-engineer estimates from the Level 1 documents, not measurements. Rule from Level 1: only the template owner edits `svg.py`, `figs2.py`, `figs3.py`, `validate.py`, `b_*.py`; lesson agents write only `lNN.json`, `verify/lNN_checks.py`, `AUDIT_LNN.md` and `out/lNN/`. New figures go in a new file `figs5.py` appended to the `figs2.render` dispatch (Levels 2 to 4 plan `figs4.py`; one file per level avoids collisions), so lesson and engineering work do not collide. Items that the Level 2, 3 and 4 pre-flights already specify are marked "builds on"; build them once for all levels (section 13 orders the work).

### 5.1 What already exists and is reused as it stands (checked in the working tree on 23 Oct 2026)

Figures: `bundles`, `scatter`, `ten_frame`, `number_line` (`marks`, `hide`, `jumps`, `highlight`, `labels`, `prefix`, `suffix`; integer ticks only), `hundred` (numbered), `seq`, `ruler`, `plates`, `objects` (about 55 icons), `groups`, `array`, `line_up`, `round_table`, `bar_model` (compare, part-whole, units, transfer; lengths to scale, brace, gap), `table` (text, boxes, circles, tick boxes, icons), `picture_equation`, `domino`, `clock` (hour hand at h + m/60, `sector`, `mirror`, `digital`, `ampm`), `money`, `price_tag`, `calendar` (any start and length), `stick_pattern`, `shapes2d`, `grid` (dots or squares, `poly` through dots, `route`, `counts`, one vertical `mirror` line, `mark`), `cube_stack` (iso, top and views; heights 0 to 3), `fold_punch`, `panel`, `network` (n dots on a ring, `lines`, `labels`, `count`), `picture_graph`. Kits: `base_ten`, `ten_frame`, `plates`, `hundred`, `number_strip`, `cards` (text labels, optional round), `shapes`, `number_line`, `groups_mat`, `unit_strips`, `array_mat`, `people`, `clock_kit`, `play_money` (with `counts`), `price_tags`, `grid_tiles`, `mistake_cards`, `fold_shapes`, `shape_pieces`, `pair_cards`, `grid_mat`, `graph_mat`, `tool_cards`, `event_cards`, `stick_strips`, `calendar_cards`. Question forms: `visuals`, `tf`, `mcq`, `steps`, `draw`, `choices`; tokens `___`, `[]`, `[2]`, `()`, `[ ]`, `{eq}`. Runner v2: `fig`, `fields`, `ordered`, templated choice, `multiples`/`common`/`divisors`, formatters `{n|ord}`, `{n|word}`, `{n|usd}`, `{n|c}`, `{m|mm}`. Lesson fields: `beyond`, `materials.kit_contract`, `home_practice[].rewind_of`, `challenge_quest.scope`; the hand-off check warns when `next_materials` omits the next kit; `b_quest.py` builds the Quest Log, tutor notes and parent note from a `challenge_quest` block and fails on the banned family words.

Lessons that can be written once Y2 and RN10 exist and with kit work only (wave A): 2, 3, 16, 22, 28, 29, 33, 35, 36, 37, 38. Lesson 2 and lesson 38 need no new item at all.

### 5.2 New figures

| Code | Item | Lessons | Spec in one line | Hours | Builds on |
|---|---|---|---|---|---|
| Y1 | `place_mat` | 1, 6, 10 | Place-value mat with 8 columns (millions to ones) and, for lesson 6, tenths to thousandths; digit tiles that slide; x10 and /10 shift arrows; hidden cells as answer boxes. | 5 | L4 F5 `place_value` if built |
| Y2 | `frac` renderer | 4, 5, 6, 9, 16, 21 to 25, 36, 37 and every lesson that names a fraction | Stacked fractions and mixed numbers in text, slides, workbook, key, home sheet and parent page; plain-text and speech forms; answer boxes `[w n/d]` (a whole-number box and two stacked boxes); fraction bars, an area model for fraction times fraction with nested shading by hatch pattern, a fraction line with a pointer. | 10 | L2 M2 and M3, L3 X4, L4 F3 (one build serves all four levels) |
| Y3 | `bar_model` extension | 4, 5, 9, 10, 17, 23, 24, 30, 36, 37 | Up to 5 bars and 16 cells; fraction and unit labels; a remainder part hatched; a before-and-after pair; a bracket labelled "1 unit" or "?"; a nested brace; the picture must not lie. | 5 | L3 X14, L4 F4 |
| Y4 | `dec_line` | 6, 14, 21 | `number_line` with decimal ticks (tenths, hundredths), a pointer between ticks, hidden labels, a percent suffix. | 4 | L3 X5, L4 F6 |
| Y5 | `grid` extension | 7, 15, 20 | A boxing-in rectangle overlay, edge counts, area labels, shaded corner triangles, interior and edge dots marked by shape (for Pick's rule). | 5 | extends `figs3.grid` |
| Y6 | `angle_fig` | 8, 15, 20, 31, 32, 40 | Labelled points, triangles and quadrilaterals with equal-side ticks, parallel marks, angle arcs with a value or a box, extended sides, a folded flap with its fold line, presets for the recurring figures (isosceles with an extended side, two joined isosceles triangles, parallelogram with a triangle, trapezium with a rhombus, regular polygons with diagonals, a five-point star), and the line "The figure is not drawn to scale." The largest geometry gap: GEO is 17 percent of the school items. | 14 | L4 F7 and F8 share the rendering core |
| Y7 | `venn` | 9, 10, 23 | Two overlapping circles with counts or boxes, a universe box, a total row; paired with the existing `table`. | 3 | L4 F11 is the logic grid, not this |
| Y8 | `dice`, `net`, `cube_paint` | 11, 20 | Die faces with pips, the 1-4-1 net with fold marks, a tower and a row of dice with touching faces labelled; a big cube with named painted faces and a cut-away. | 6 | L4 F13 `dice` |
| Y9 | `cube_stack` extension | 11, 12, 19 | A 4 by 4 base and heights to 5; numbered top, front and side views; a hidden-cube mode; a cuboid in layers. | 5 | L2 M8 and L4 F9 raise the cap from 3 to 4 first |
| Y10 | `iso` | 19 | Isometric dot paper; a cuboid drawn from its edges; a part-drawn cuboid to complete; turned block figures as options (1) to (4); a rope and knot (3 of the 10 hours, deferrable). | 10 | new |
| Y11 | `tank` | 12, 13, 16, 20 | A rectangular tank with water level, edge labels, a divider, a fixed step or a block, a pouring arrow; litre and cm3 labels. | 7 | L2 M7 `jug` is a different object |
| Y12 | `graph` | 17, 18, 20, 21 | A line graph (axes, scale, points, a hidden point, a draw-in grid), a bar graph (scale, hidden bar, average line) and a pie chart (sectors with a hidden count), hatch patterns for series. | 9 | L3 X7, L4 F10 |
| Y13 | `pattern_fig` | 10, 26, 30 | Figures 1 to 4 of dot, tile and stick patterns (squares, L-shapes, staircases) with a count table; extends `stick_pattern`. | 4 | L4 F12 |
| Y14 | `chords` | 26 | A circle with n points and chords, with the regions numbered; an extension of `network` (1 of the hours is deferrable by drawing). | 1 | extends `figs3.network` |
| Y15 | `graph_colour` | 39, 40 | `network` with per-node labels A to D or hatch, presets path, ring, wheel and the ten-circle figure. | 3 | L4 F15 |
| Y16 | `logic_grid` | 34 | A table preset with row and column headers, tick and cross cells and a clue list. | 2 | L4 F11 |
| Y17 | `crypt` | 34 | Vertical letter addition with a carry row and digit boxes, 3 to 5 digits. | 3 | L2 M5, L3 X1, L4 F1 `column` |
| Y18 | `balance` | 25 | A pan balance with identical objects, weight tokens and a tilt; hatch per object. | 4 | L2 M6, L3 X6, L4 F14 |
| Y19 | `rays` | 27 | An apex with rays to lettered points and one or two parallel lines, for counting triangles. | 3 | new, small |
| Y20 | `symmetry` | 32 | `grid` with a mirror line at any column, row or diagonal and the half to complete. | 2 | extends `figs3.grid` (mirror) |
| Y21 | `clock` check | 33 | Check that `clock` with `sector` shows the angle between the hands and a 24-hour readout at any minute; a verify, not a build. | 1 | exists in `figs3.clock` |
| Y22 | `percent_grid` | 21, 23, 30 | An unnumbered 10 by 10 grid with hatch shading and a percent bar; the existing `hundred` is numbered. | 1.5 | L4 F20 `grid_100` |
| | **Total figures (22 items)** | | | **107.5** | |

### 5.3 Kit builders (section 6 lists the pieces)

Existing builders reused with new counts or labels: `play_money` (KT10), `price_tags` (KT6), `people` (KT9), `unit_strips` (KT7), `clock_kit` (KT12), `cards` (KT13, KT14). New: `shift_tiles`, `pizza_circles`, `triangle_cards`, `dice_nets`, `dissection_set`, `weight_tokens`, `shape_cards`. Every builder also prints the standard note (one side only, a grown-up cuts, an envelope with the child's name, tear along the dashed line) and the "no printer" fallback. A check that each page's `kit_contract` matches the tasks is TL2 of Level 1's T2 (the Level 3 list) and is shared.

| Code | Kit builder | Lessons | Hours |
|---|---|---|---|
| KT1 | shift_tiles | 1 | 2 |
| KT2 | pizza_circles | 4 | 1 |
| KT3 | triangle_cards | 8 | 1.5 |
| KT4 | dice_nets | 11 | 2.5 |
| KT5 | dissection_set | 15 | 2 |
| KT6 | shop_cards (uses `price_tags`) | 22, 29 | 0.5 |
| KT7 | unit_strips (exists) | 24 | 0.5 |
| KT8 | weight_tokens | 25 | 1.5 |
| KT9 | people_cards (uses `people`) | 27 | 0.5 |
| KT10 | play_coins (uses `play_money` counts) | 28 | 0.5 |
| KT11 | shape_cards | 32 | 1.5 |
| KT12 | clock_kit (exists) | 33 | 0.5 |
| KT13 | clue_cards (uses `cards`) | 34 | 1 |
| KT14 | draw_cards (uses `cards`) | 35 | 1 |
| KP | printed (not cut) sheets: dot grids, hundred grids, layer sheets, isometric sheets, polygon sheets, Venn mat, balance mat, colouring pages, work paper | 7, 6, 12, 19, 21, 31, 9, 25, 39 | 4 |

### 5.4 Online runner (shared `practice/public/practice.js`; versioned so Levels 1 to 4 keep working)

Shared with Levels 2 to 4 and built by whichever level reaches them first: RN1 compound units, RN3 true/false/not possible to tell as a tick table, RN4 fraction answers, RN5 money, RN6 time (12-hour and 24-hour), RN7 options that are pictures, RN8 registered figures with variables (Level 3 section 5.4: 3 + 2 + 3 + 2 + 2 + 3 + 3 = 18 hours); RN9 builds on RN4. Level 5 additions:

| Code | Item | Lessons | Hours |
|---|---|---|---|
| RN9 | Mixed-number answers: a whole-number box and two stacked boxes, a simplest-form check, an improper fraction accepted only where asked | 4, 5, 24 | 3 |
| RN10 | Decimals and percent: 0.50 = 0.5, "35" and "35%" both accepted for "what percentage", a rounding instruction check (nearest tenth, whole number), numbers with spaces (3 600 000) | 1, 6, 14, 16, 21 to 23, 29 | 2 |
| RN11 | Ratio answers "3 : 5" and "3:5", "times as many" frames | 24 | 1 |
| RN12 | Angle answers with the degree sign (114 and 114° both accepted); a reason in words is self-checked, not auto-marked | 8, 31, 32 | 1 |
| RN13 | List answers in any order with the count checked (all factors, all cuboids, all the ways), helpers `factors`, `cuboids(v)` and `ways(...)` | 2, 9, 12, 25, 28, 35 | 3 |
| RN14 | Two-part items: (b) uses (a), per-part feedback | 37 | 2 |
| RN15 | Drawing items ("draw the missing bar", "complete the figure") are self-checked against a model picture, not auto-marked | 17, 18, 32 | 2 |

Level 5 runner subtotal: 14 hours.

### 5.5 Term-level tools

Shared with Levels 2 to 4: TL1 level parameter 6, TL2 copy-check list 1, TL3 Quest builder 2, TL4 books 3, TL5 hand-off checker 1, TL6 wording linter 2, TL7 entry check 4, TL8 author brief 3, TL9 validator keys 1, TL10 rewind sets 3 (Level 3 section 5.5, 26 hours; Level 2 M1, M15, M17, M18, M19, M20, M21 and Level 4 N1 to N5 cover the same ground). Level 5 additions:

| Code | Item | Hours |
|---|---|---|
| TL11 | Level 5 wording linter rules: GST 9 percent (7 percent only in labelled older-paper practice), the degree sign, "Express your answer in the simplest form", no "prime", "coordinates" or bare "challenge" on child pages, mixed-number format, "The figure is not drawn to scale." on figure pages | 1 |
| TL12 | `verify_lib.py`: shared brute-force helpers (`fractions`, `divisors`, `partitions`, `permutations` with constraints, polygon area, angle and line intersection, cube-stack views) so each `verify/lNN_checks.py` does not rewrite them | 3 |
| TL14 | A required `nonroutine: [{type, tier, item_id}]` field (type from the 16 codes, tier T or G, never Start here) and the validator rule | 2 |
| TL15 | Black-and-white check for the Y figures: hatch patterns, letters A to D for colouring, `print/check_bw.py` on every Level 5 book | 1 |

Level 5 term-tool subtotal: 7 hours.

### 5.6 Totals and what can wait

Figures 107.5 + kit builders 20.5 + runner 14 + term tools 7 = **149.0 hours** of Level 5 specific work if everything is built, plus the shared items (18 runner and 26 tool hours) if no earlier level has built them: **193.0 hours**. Deferrable without blocking a lesson (8 hours): the rope and knot of Y10 (3: drop lesson 19 G3), Y14 (1: draw the chords by hand), RN15 (2: self-check by a printed answer picture), RN11 (1: write ratio answers as text), TL15 (1: check by eye). That leaves about **141.0 hours** (Level 5 share only). Figures that Levels 2 to 4 also need (Y2, Y3, Y4, Y8, Y9, Y12, Y13, Y15, Y16, Y17, Y18, Y22: 56.5 hours) cost Level 5 nothing if those levels build them first; the net Level 5 share is then about **84 hours**. Not needed at Level 5: coins and notes beyond lesson 28, clocks beyond lesson 33, picture graphs, fold and punch, panels, calendars beyond lesson 33.

## 6. Kit contracts: supplied pieces against the most a task may use

The Level 1 cut-out audit found two Reworks (L12 strips, L19 shape cards) because piece counts were never checked against tasks, and 203 pieces in one term. Each row is the contract the lesson author signs: `supplied` is what the page prints; `max used` is the most any task uses; the lesson's `materials.kit_contract` (a field that exists in the Level 1 schema) and its verify script assert supplied >= max used. A grown-up, or the child with a grown-up, cuts before the lesson; nobody cuts during a lesson (lesson 15 excepted, D5). Every kit page carries the standard note: print on its own sheet (the book puts it on a front page with a blank back), keep the pieces in an envelope with the child's name, tear out along the dashed line. All kits are black and white: pieces differ by shape, size, label or fill pattern, never colour alone; digits that can be turned (6, 9) are underlined; cut lines at least 6 mm apart; counters and tiles are squares with rounded corners; a "no printer" fallback is written on every kit page.

| L | Kit | Supplied | Max used by a task | Cut | Notes |
|---|---|---|---|---|---|
| 1 | KT1 shift_tiles | 13 tiles (0 x 4, 1 to 9 once each) | 8 tiles (at most 4 zeros, no repeated non-zero digit) | 13 | Mat printed, not cut; no printer: digits on scraps |
| 2 | none cut; up to 36 small things (optional); factor-pair sheet printed | - | - | 0 | |
| 3 | none | - | - | 0 | |
| 4 | KT2 pizza_circles | 8 circles (11 cm) | 7 circles (7 pizzas shared among 3) | 8 | Fold lines printed; paper plates are the fallback |
| 5 | none cut; area-model grid printed | - | - | 0 | |
| 6 | none cut; four hundred-grids printed (a task uses at most 3) | - | - | 0 | |
| 7 | none cut; six dot-grid pages printed (a task uses at most 4) | - | - | 0 | |
| 8 | KT3 triangle_cards | 8 triangles, sides marked with ticks, no angle values | 8 cards (sorting) | 8 | Not needed again |
| 9 | none cut; Venn mat printed; 20 small things from home (at most 16 used) | - | - | 0 | |
| 10 | none cut; Quest Log (4 pages) in Book 2 | - | - | 0 | |
| 11 | KT4 dice_nets | 4 nets of a 3 cm die, opposite faces add to 7 | 4 dice (a tower of four) | 4 | Tape needed; a board-game die may replace one |
| 12 | none cut; six layer sheets printed (at most 4 used); up to 24 blocks optional (at most 24 used) | - | - | 0 | |
| 13 | none cut; two containers and water from home | - | - | 0 | |
| 14 | none cut; ruler, kitchen scale optional | - | - | 0 | |
| 15 | KT5 dissection_set | 8 paper shapes: 2 parallelograms, 2 trapeziums, 2 triangles, 2 squares | 8 (each cut once or twice in the lesson) | 8 | The child cuts these in the lesson (scissors, D5); the only kit not cut beforehand |
| 16 | none | - | - | 0 | |
| 17 | none cut; 30 counters from home (at most 28 used) | - | - | 0 | |
| 18 | none cut; graph grids printed (at most 3 used) | - | - | 0 | |
| 19 | none cut; six isometric sheets (at most 4 used); up to 14 blocks optional (at most 14 used) | - | - | 0 | |
| 20 | none cut; Quest Log in Book 4 | - | - | 0 | |
| 21 | none cut; six unnumbered hundred-grids (at most 4 used) | - | - | 0 | |
| 22 | KT6 shop_cards | 10 cards (item, price, offer) | 8 cards at once | 10 | Reused in lesson 29 warm-up |
| 23 | none | - | - | 0 | |
| 24 | KT7 unit_strips | 6 strips of 12 cells (72 cells) | 38 cells (three bars at once) | 6 | Cut between strips, not between cells |
| 25 | KT8 weight_tokens | 12 tokens (shapes of weight 1 to 4 units) and a balance mat (not cut) | 9 tokens | 12 | Shapes differ by outline, not colour |
| 26 | none cut; squared paper | - | - | 0 | |
| 27 | KT9 people_cards | 10 people | 9 people (handshakes among 9) | 10 | Fallback: 9 coins or buttons |
| 28 | KT10 play_coins | 10c x 12, 20c x 6, 50c x 3 (21 pieces) | 10c x 12, 20c x 6, 50c x 2 | 21 | Real coins from a purse are better; stylised, marked PLAY MONEY |
| 29 | none cut; the shop cards of lesson 22 reused (at most 6 used) | - | - | 0 | |
| 30 | none cut; Quest Log in Book 6 | - | - | 0 | |
| 31 | none cut; four polygon sheets (at most 3 used) | - | - | 0 | |
| 32 | KT11 shape_cards | 12 cards: square, rectangle, rhombus, parallelogram, trapezium, kite, two of each | 12 (sorting) | 12 | Sides and right angles marked |
| 33 | KT12 clock_kit | 2 faces (not cut), 3 hour hands, 3 minute hands | 2 faces, 2 + 2 hands | 6 | Loose hands, no fastener; a real clock helps |
| 34 | KT13 clue_cards | 12 cards (8 clue, 4 name) | 12 | 12 | 4 by 4 logic grids are printed, not cut |
| 35 | KT14 draw_cards | 16 cards (4 symbols x 4) | 16 (a draw of up to 9 cards, then all 16 to check the claim) | 16 | A normal pack of playing cards also works |
| 36 | none cut; 24 counters and 3 cups from home (24 used) | - | - | 0 | |
| 37 | none | - | - | 0 | |
| 38 | none | - | - | 0 | |
| 39 | none cut; six colouring pages (at most 4 used) | - | - | 0 | |
| 40 | none cut; Quest Log in Book 8 | - | - | 0 | |

Cut per term: Term 1 29, Term 2 12, Term 3 59, Term 4 46; year 146 (K.1, K.2). Per book (5 lessons): Book 1 21; Book 2 8; Book 3 12; Book 4 0; Book 5 28; Book 6 31; Book 7 46; Book 8 0. Books 4 and 8 have nothing to cut.

Book page counts (estimate from the Level 1 pattern, 5 pages per lesson plus kit pages, a Quest Log of 4 pages in Books 2, 4, 6, 8, a cover and contents, and a blank pad so each lesson starts on a right-hand page): about 36 to 40 pages per book. `term_books_spec.json` gives the true counts after a build.

## 7. Hand-off chain: what the family must have ready (truth between all 40 lessons)

The Level 1 rule: `parent.next_materials` of lesson n lists everything lesson n+1 needs that a family has to prepare: the book (issued on payment), any kit page to cut, anything kept from earlier, anything to find at home. The tutor's spoken goodbye, the `s-end` slide and `tutor_prep` carry the same words. Under the print-on-payment decision the wording is "your next workbook is in your book: tear out the kit page along the dashed line, then a grown-up cuts out the pieces" (Level 1 audit F6). The row for lesson n to n+1 is what lesson n+1 needs, copied from the kit contracts, so the two tables cannot disagree. A validator check (TL5) fails a build when a lesson's `next_materials` omits the next lesson's cut-out kit.

| From to | Cut / prepare (a grown-up cuts a week before) and find at home | Keep from before | Check and hazard |
|---|---|---|---|
| before 1 | Book 1 (posted before the lesson); the 13 digit tiles (KT1) cut; pencil; plain paper | - | Term 1 start; no ruler needed yet |
| 1 to 2 | Nothing to cut; up to 36 buttons (optional); squared paper (in the book) | The digit tiles (lesson 6) |  |
| 2 to 3 | Nothing; pencil | The tiles |  |
| 3 to 4 | The 8 pizza circles (KT2) cut, or paper plates; pencil | The tiles | A grown-up cuts a week before |
| 4 to 5 | Nothing new; squared paper (in the book) | The circles (optional) |  |
| 5 to 6 (book) | Book 2 in the house; the hundred-grids are in the book; pencil | The digit tiles (the decimal mat) | Book boundary: if Book 2 arrives with a later instalment this fails (D10) |
| 6 to 7 | A 30 cm ruler; pencil; six dot-grid pages are in the book | - | Ruler hazard: a family without one tells the tutor |
| 7 to 8 | The 8 triangle cards (KT3) cut; a protractor (optional); ruler | - |  |
| 8 to 9 | 20 small things (not food); the Venn mat is in the book | - |  |
| 9 to 10 | The Quest Log stays closed in Book 2; a quest partner; pencil | - | The Quest Log is never opened before the lesson |
| 10 to 11 (term and book) | Book 3; the 4 dice nets (KT4) cut; tape; a die from a board game (optional); up to 12 blocks (optional) | - | Term break; new book |
| 11 to 12 | Up to 24 same-size blocks (optional); ruler; layer sheets are in the book | - | Fallback: drawn layers |
| 12 to 13 | Two containers (a jug and a bottle) and water; ruler | - |  |
| 13 to 14 | Ruler; a kitchen scale and measuring jug (optional) | - |  |
| 14 to 15 | Scissors for the child, glue or tape, plain paper; tear out the kit page (8 shapes) but do not cut it | - | The one lesson where the child cuts (D5) |
| 15 to 16 (book) | Book 4 in the house; pencil; squared paper | - | Book boundary |
| 16 to 17 | About 30 counters or buttons; squared paper | - |  |
| 17 to 18 | Ruler; the graph grids are in the book | - |  |
| 18 to 19 | Up to 14 small blocks (optional); six isometric sheets are in the book; ruler | - | Fallback: drawn stacks |
| 19 to 20 | The Quest Log stays closed in Book 4; a quest partner | - | Same rule as lesson 9 to 10 |
| 20 to 21 (term and book) | Book 5; the unnumbered hundred-grids are in the book; pencil | - | Term break; new book |
| 21 to 22 | The 10 shop cards (KT6) cut; a real shopping receipt (optional) | - |  |
| 22 to 23 | Pencil | The shop cards (lesson 29) |  |
| 23 to 24 | The 6 unit strips (KT7) cut between strips, not between cells; paper strips (optional) | - | Strips cut between cells are the likeliest mistake (Level 1 lessons 12 and 18) |
| 24 to 25 | The 12 weight tokens (KT8) cut; the balance mat is in the book | - |  |
| 25 to 26 (book) | Book 6 in the house; pencil; squared paper | - | Book boundary: if Book 6 arrives late (D10) this fails |
| 26 to 27 | The 10 people cards (KT9) cut; ruler | - | Fallback: 9 coins |
| 27 to 28 | The 21 play coins (KT10) cut, or real coins from a purse with a grown-up present | - | The heaviest cutting of Term 3; give a week |
| 28 to 29 | Pencil | The shop cards (from lesson 22) |  |
| 29 to 30 | The Quest Log stays closed in Book 6; a quest partner | - | Same rule |
| 30 to 31 (term and book) | Book 7; a protractor (optional); ruler; four polygon sheets are in the book | - | Term break; new book |
| 31 to 32 | The 12 shape cards (KT11) cut; ruler; a small mirror (optional) | - |  |
| 32 to 33 | The 6 clock hands (KT12) cut (the 2 faces are not cut); a real clock (optional); a calendar of any year | - | Loose hands, no fastener |
| 33 to 34 | The 12 clue cards (KT13) cut; pencil | - |  |
| 34 to 35 | The 16 draw cards (KT14) cut, or a pack of playing cards; a bag | - |  |
| 35 to 36 (book) | Book 8 in the house; 24 counters and three cups | - | The book boundary falls here: if Book 8 comes with a later instalment it must be posted before lesson 35 ends (D10) |
| 36 to 37 | Pencil | - |  |
| 37 to 38 | Pencil; plain paper | - |  |
| 38 to 39 | Pencil; the six colouring pages are in the book (letters A to D, no coloured pencils needed) | - |  |
| 39 to 40 | The Quest Log stays closed in Book 8; a quest partner; a favourite page from the year; plain paper | - |  |
| 40 to next | The tutor sends the next level's placement note; no materials list is printed here | - | Not a lesson-file concern |

## 8. Mi's Challenge Quest in lessons 10, 20, 30 and 40

The Level 1 Quest (lesson 20) is the model: 20 minutes at minutes 35 to 55 straight after the break; eight short gates and one optional secret cave; a quest partner (answers are written on private paper, each child writes their own); no score, mark, ranking or visible timer; no word "test" or "exam" on any child or parent page (`BAN_FAMILY` in `b_quest.py`); the tutor keeps private notes only, used for one line to each grown-up and for advice on next term's group; the recording is paused for the Quest and a make-up child does the Quest before watching the recording; photos of the Quest Log are returned by the parent to the business WhatsApp (+65 9880 5962, never on a slide). Explore 10 and Mini-lesson 9; the Start here workbook is 25 minutes; pages 3 to 5 are for home; the exit ticket is not live. Three files per Quest: `LNN_Quest_Log.pdf` (**[Default] 4 pages for ages 10 to 12**, as Level 4; 3 at Levels 1 and 3), `LNN_Quest_Tutor_Notes.pdf` (key book), `LNN_Quest_Parent_Note.pdf` (home pack). The Quest Log may carry figures because the Level 1 generator accepts any registered figure (TL3). Rules for authors: every gate is Start here level for its own lesson and "pass" is always allowed; the Quest is never the part that shrinks in a slow class (skip order: Flex, then the optional Go further slide, then Talk); the cave is the only place for a puzzle the children have not met; one item per part; children read the Quest Log themselves and the tutor reads each gate once aloud. **Test-savvy children:** ten- to twelve-year-olds recognise a paper; the Log is framed as Mi's map with gates, pairs may talk through a gate (each writes their own answer), and nothing is added up. Lessons 10, 20 and 30 are also content lessons (Explore 10 and Mini-lesson 9 minutes only), so each is a review of choosing a method, not a new topic.

Lessons share a gate where two neighbouring lessons are small: every lesson of the term is visited by exactly one gate. All answers below were recomputed (check ids in the last column).

### 8.1 Term 1 (lesson 10)

| Gate | Lessons | Item (Start here level) | Figure | Check |
|---|---|---|---|---|
| 1 | 1 | A hall has 4 250 seats; a stadium has 100 times as many: 425 000. And 3 600 000 / 1 000 = 3 600 | `place_mat` | Q1.1 |
| 2 | 2 | Write all the common factors of 18 and 30: 1, 2, 3, 6; the greatest is 6 | none | Q1.2 |
| 3 | 3 | Find the value of 5 + 12 / 4 x 2 - 3: 8 | none | Q1.3 |
| 4 | 4, 5 | 7 / 4 as a mixed number is 1 3/4; 2/3 of 3/5 is 2/5 | `frac` | Q1.4 |
| 5 | 6 | 3/8 as a decimal is 0.375; 4.5 / 1 000 = 0.0045 | `place_mat` | Q1.5 |
| 6 | 7 | A triangle with base 14 cm and height 6 cm has area 42 cm2 | `grid` | Q1.6 |
| 7 | 8 | An isosceles triangle has a 40 degree angle at the top: each base angle is 70; two angles of 48 and 67 leave 65 | `angle_fig` | Q1.7 |
| 8 | 9 | In a group of 30, 18 swim, 15 cycle and 5 do neither: 8 do both | `venn` | Q1.8 |
| Cave | beyond | I am between 40 and 60, a multiple of 7, and my digits add up to 11: 56 | none | Q1.9 |

Lesson 10's Explore (10 minutes) is an angle warm-up and "choose a start" with three examples; the Start here workbook is a menu (do four of six). Gates 4 to 8 carry figures, so Y1, Y2, Y6 and Y7 must exist before lesson 10 is built.

### 8.2 Term 2 (lesson 20)

| Gate | Lessons | Item (Start here level) | Figure | Check |
|---|---|---|---|---|
| 1 | 11 | A numbered top view with counts 2, 1 / 3, 1 has 7 cubes | `cube_stack` | Q2.1 |
| 2 | 12 | A box 5 cm by 4 cm by 3 cm has volume 60 cm3 | `cube_stack` | Q2.2 |
| 3 | 13 | A tank 40 cm by 25 cm with water 6 cm deep holds 6 000 cm3, which is 6 l | `tank` | Q2.3 |
| 4 | 14 | 3 kg 250 g + 1.9 kg = 5.15 kg = 5 kg 150 g | none | Q2.4 |
| 5 | 15 | A parallelogram with base 9 cm and height 5 cm has area 45 cm2 | `grid` | Q2.5 |
| 6 | 16 | A tap fills 18 l a minute: 270 l take 15 minutes | none | Q2.6 |
| 7 | 17, 18 | The average of 4, 7, 9 and 12 is 8; read the 11 am value from the line graph | `graph` | Q2.7 |
| 8 | 19 | On a 3 by 2 by 2 cuboid you can see 3 x 2 + 3 x 2 + 2 x 2 = 16 unit squares | `iso` | Q2.8 |
| Cave | beyond | A tank with a 30 cm by 20 cm base holds water 5 cm deep; 3 l are added: 10 cm deep | `tank` | Q2.9 |

Gate 7 pairs lessons 17 and 18 because Fair Shares and Graph Stories are both small; gate 8 carries the isometric figure, so Y10 must exist before lesson 20 is built. Lesson 20's Think harder holds the Term 2 buy-more-get-free item.

### 8.3 Term 3 (lesson 30)

| Gate | Lessons | Item (Start here level) | Figure | Check |
|---|---|---|---|---|
| 1 | 21 | 35% of 80 is 28; 0.4 is 40% | `percent_grid` | Q3.1 |
| 2 | 22 | A $50 jacket is 20% off: $40; add 9% GST: $43.60 | `price_tag` | Q3.2 |
| 3 | 23 | 18 out of 24 is 75% | none | Q3.3 |
| 4 | 24 | Pens to pencils are 2 to 3 and there are 45 in all: 18 pens | `bar_model` | Q3.4 |
| 5 | 25 | 3 [ ] + 5 = 29: [ ] = 8 | `balance` | Q3.5 |
| 6 | 26 | 2, 5, 8, 11, ...: the 20th number is 59 | `pattern_fig` | Q3.6 |
| 7 | 27, 28 | Nine children shake hands once each: 36; 10 tickets at $4 and $6 cost $48: 4 at $6 | `network` | Q3.7 |
| 8 | 29 | $1 000 at 4% a year for 3 years earns $120 | `table` | Q3.8 |
| Cave | beyond | Pens cost $3 each or 3 for $8: exactly 10 pens cost at least $27 | `table` | Q3.9 |

Gate 7 pairs lessons 27 and 28. The cave is an offer item that uses lesson 22's idea and lesson 28's table.

### 8.4 Year Quest (lesson 40)

| Gate | Lessons | Item (Start here level) | Figure | Check |
|---|---|---|---|---|
| 1 | 31 | Each angle of a regular hexagon is 120 (the angles add to 720) | `angle_fig` | Q4.1 |
| 2 | 32 | Four equal sides and equal diagonals: a square | `angle_fig` | Q4.2 |
| 3 | 33 | The hands at 4:00 make 120 degrees; 100 days after a Monday is a Wednesday | `clock` | Q4.3 |
| 4 | 34 | Mei is not first, Ravi is directly behind Mei and Kai is ahead of Mei: Kai, Mei, Ravi | `logic_grid` | Q4.4 |
| 5 | 35 | The sum of 9 odd numbers is odd; name a number between 10 and 60 that leaves 3 when divided by 7 and 1 when divided by 4 (17 or 45) | none | Q4.5 |
| 6 | 36 | Times 3, take away 4 gives 20: the number is 8 | none | Q4.6 |
| 7 | 37, 38 | A $60 bag is 25% off and 9% GST is added: $49.05; write a question with the answer $49.05 | `table` | Q4.7 |
| 8 | 39 | A path of 4 circles with 3 colours: 24 ways | `graph_colour` | Q4.8 |
| Cave | beyond | How many 3-digit numbers have digits that add up to 5: 15 | none | Q4.9 |

Gate 7 pairs lessons 37 and 38 (the second part is a posing item and has no single answer). Lesson 40's own showcase is the closing part of the Quest lesson and has no gate. A child who joins at lesson 30 or 40 has not met the earlier gates: every gate states its own idea in one line, and the cave may be skipped.

## 9. Spiral review across the year

The Level 1 term-wide audit found no spiral review (warm-ups re-teach only what the lesson needs; home and online practice are current-lesson only), and Level 1 Terms 3 and 4 fixed it with layers that add no minutes to the 90. Level 5 builds them in from lesson 1.

1. **Home sheet slot 5 is "Mi's rewind".** One item from lesson n - 10 (for n of 11 or more), with its answer on the separate answer sheet; lessons 1 to 10 rewind a holiday or Primary 4 topic (the warm-up list). Items are copied from the earlier lesson's home or online bank by id, not rewritten (needs the `rewind_of` tag and the rewind set tool, shared TL10).
2. **Online practice ends with two rewind items** from lesson n - 5 (n of 6 or more) and, from lesson 21, a second pair from lesson n - 20, so every Term 1 and Term 2 idea is visited again at three distances in the year.
3. **The Quest cave** is an unseen puzzle joining two moves; one Remember item per lesson may be a spiral item (the specs mark it "Spiral from H..").
4. **A recurring warm-up bank.** A five-minute "estimate and check" routine from lesson 6 on (so the rounding of lesson 14 is not a first meeting) and a two-minute "angle fact" routine from lesson 8 on (so angle chains in 15, 31, 32 and the Reviews have a base, the plan's note that every Review gets an angle warm-up). Neither costs a lesson.

| Lesson | Home rewind | Online rewind | Lesson | Home rewind | Online rewind |
|---|---|---|---|---|---|
| 1 | H1 place value | - | 21 | 11 Solid Views and Dice | 16 Rate and Working Together; 1 Shifting Places |
| 2 | H1 digit sums | - | 22 | 12 Boxes and Bricks | 17 Fair Shares; 2 Factor Finders |
| 3 | H1 brackets | - | 23 | 13 Tank Tales | 18 Graph Stories; 3 Smart Calculation |
| 4 | H2 fraction as division | - | 24 | 14 Decimal Measures | 19 Isometric Builders; 4 Mixed Numbers and Sharing |
| 5 | H2 fraction of a quantity | - | 25 | 15 Cut and Rearrange | 20 Term 2 Review and Mi's Challenge Quest; 5 Fractions of Fractions |
| 6 | H2 fraction to decimal | 1 Shifting Places | 26 | 16 Rate and Working Together | 21 Percent Sense; 6 Decimal Sense |
| 7 | H4 half base times height | 2 Factor Finders | 27 | 17 Fair Shares | 22 Shop Smart; 7 Boxed-In Triangles |
| 8 | H8 angle facts | 3 Smart Calculation | 28 | 18 Graph Stories | 23 One Number as a Percent of Another; 8 Angles and Triangle Families |
| 9 | H3 a total that stays the same | 4 Mixed Numbers and Sharing | 29 | 19 Isometric Builders | 24 Unequal Parts; 9 Two Groups and the Overlap |
| 10 | H10 choose a start | 5 Fractions of Fractions | 30 | 20 Term 2 Review and Mi's Challenge Quest | 25 Balance and Undo; 10 Term 1 Review and Mi's Challenge Quest |
| 11 | 1 Shifting Places | 6 Decimal Sense | 31 | 21 Percent Sense | 26 Number Stories; 11 Solid Views and Dice |
| 12 | 2 Factor Finders | 7 Boxed-In Triangles | 32 | 22 Shop Smart | 27 Count Without Counting; 12 Boxes and Bricks |
| 13 | 3 Smart Calculation | 8 Angles and Triangle Families | 33 | 23 One Number as a Percent of Another | 28 Supposition Studio; 13 Tank Tales |
| 14 | 4 Mixed Numbers and Sharing | 9 Two Groups and the Overlap | 34 | 24 Unequal Parts | 29 Money Grows; 14 Decimal Measures |
| 15 | 5 Fractions of Fractions | 10 Term 1 Review and Mi's Challenge Quest | 35 | 25 Balance and Undo | 30 Term 3 Review and Mi's Challenge Quest; 15 Cut and Rearrange |
| 16 | 6 Decimal Sense | 11 Solid Views and Dice | 36 | 26 Number Stories | 31 Angles in Shapes; 16 Rate and Working Together |
| 17 | 7 Boxed-In Triangles | 12 Boxes and Bricks | 37 | 27 Count Without Counting | 32 Triangles and Quadrilaterals; 17 Fair Shares |
| 18 | 8 Angles and Triangle Families | 13 Tank Tales | 38 | 28 Supposition Studio | 33 Clocks and Calendars; 18 Graph Stories |
| 19 | 9 Two Groups and the Overlap | 14 Decimal Measures | 39 | 29 Money Grows | 34 Logic Grids and Digit Puzzles; 19 Isometric Builders |
| 20 | 10 Term 1 Review and Mi's Challenge Quest | 15 Cut and Rearrange | 40 | 30 Term 3 Review and Mi's Challenge Quest | 35 Odd, Even, Remainders and Extremes; 20 Term 2 Review and Mi's Challenge Quest |

**Spiral threads across the year** (each strand returns at least twice in a new setting).

| Thread | Term 1 | Term 2 | Term 3 | Term 4 |
|---|---|---|---|---|
| Place value and shifting | 1, 6 | 14 (units in decimal form) | 21 (percent as hundredths) | 35 (last digits) |
| Fractions as parts and operators | 4, 5 | 13 (fraction of a tank), 16 (rates as fractions of a job) | 23, 24, 25 | 36, 37 |
| Unit models | 4, 5, 9 | 17 (levelling) | 24 (full treatment) | 36, 37 |
| Area and angles | 7, 8 | 15, 19 | 26 (figures) | 31, 32, 33 |
| Listing every case | 2, 9 | 12 (cuboids), 19 | 27, 28 | 34, 35, 39 |
| Working backwards | 10 (Review) | 13 | 25 | 36 |
| Percent and money | 6 | 14 | 21, 22, 23, 29 | 36, 37 |
| Patterns and rules | 10 (block) | 19 (matrix) | 26 | 39 (cycles) |

## 10. Known failure patterns from Level 1: the author checklist

Read from `TERM_WIDE_AUDIT`, `CUTOUT_AUDIT`, `FINAL_AUDIT_T1`, `FINAL_AUDIT_T2` and the Level 1 pre-flights. Each line is something the Level 1 fix passes repaired more than once; the Level 5 authors should not write it in the first place, and each has a check. Rows 27 to 32 are Level 5 additions.

| # | Level 1 failure (source) | Level 5 rule | Check |
|---|---|---|---|
| 1 | Kit counts do not match tasks (L12 strips, L19 shape cards, L20 tokens, L13 counters; CUTOUT F1, F2) | Every kit lesson fills `materials.kit_contract`; supplied >= max used; section 6 | `verify/lNN_checks.py` asserts it; validator fails otherwise |
| 2 | False "next lesson" materials lines (7 of 9 in Term 1; L7 to L8, L9 to L10, L10 to L11) | `next_materials` is copied from section 7 and says "tear out the kit page"; the spoken goodbye and `s-end` slide use the same words | TL5 fails a build on a mismatch |
| 3 | Workbook numbers repeat class numbers (WB1 in L15 to L20, L8 T1) | No Start here or Think harder number is used in Explore, Mini-lesson, Sneak-peek or the Quest | verify script scans the slide data |
| 4 | Answers on the slide while the question is asked (G1, every Term 2 deck audit) | `reveal` blocks and answer slides; Explore pictures never carry the count | deck check |
| 5 | Family pages use the global lesson number ("Lesson 14", "Lesson 1 of 10"); mixed numbering in books | "Level 5 Term 2 Lesson 4" on every family page; books print "Term 2 Lesson 4 (lesson 14 of 40)" | leak check keyed on `lesson_in_term`; "the first lesson of Term 4" |
| 6 | Start here too long for the 28 workbook minutes (15.5 to 19 modelled; slow class 3 to 4 minutes over) | Six Start here items, at most 20 modelled minutes; page 1 about 8 minutes, page 2 about 9, choice 3; "Think harder and Go further are for home" on the page | validator timing |
| 7 | Keys accept one order or form (3 x 4 against 4 x 3) | Accept equivalent forms: 2 3/4 and 11/4 where improper is not forbidden; 0.5 and 1/2 and 50%; 114 and 114°; ways in any order; "3:5" and "3 : 5" | RN9 to RN13 |
| 8 | Recording and camera scripts differ across lessons; first names on the recording; "cameras on" beside "may switch off" | Copy the final Level 1 wording (lessons 6 to 10 after the 23 Oct fix) into every Opening: notice first, then start the recording; "the tutor, the shared screen and any unmuted voice are recorded; children may mute and keep cameras off"; no first names on the recording; no paper hold-ups | identical-text check across lessons |
| 9 | "I am still stuck" had no route | Tick on the look-back, the parent photographs the page to the business WhatsApp after class; the number is never on a slide | validator privacy check |
| 10 | Parent page: boilerplate term line, no weekly workload, no "do not teach" line, no practice link | A lesson-specific term line; "Home Practice (15 minutes) if you like; pages 3 to 5 and online practice are optional"; a words list; a when-stuck line; the beyond-Primary-5 sentence from `beyond.parent` | parent-page check |
| 11 | Runner variants: "1 hours", "1 stickers", double full stops, raw placeholders | Plural guards; every variant verified three ways (oracle, runner, validator) | validator |
| 12 | Investigation page overflow | A drawing box, four ruled lines, an easy first step | real-PDF page check |
| 13 | Small pictures on the workbook (tables, number lines, strips; L14 chart cells 6 mm) | Give `size` and column width for each new figure in the first build; chart cells at least 12 mm; angle figures at least 60 mm wide | page view |
| 14 | Wrong working attached to cast names | "A child" or "a child in another class" | text scan |
| 15 | Children cutting in the lesson | A grown-up cuts beforehand; nobody cuts in a lesson (lesson 15 excepted, D5) | guide and materials text |
| 16 | A contest label on a child page; the word "Challenge" used for tiers or in a lesson title | `contest_where` names tiers in tutor text only; "Challenge" only in "Mi's Challenge Quest"; lessons 10, 20, 30, 40 retitled | validator banned words |
| 17 | Colour or glyph reliance (red and yellow counters, stars as marks, symbols that read the same in grey) | Black and white by shape, label and hatch; colouring puzzles use letters; no "colour" instruction on a printed page | `print/check_bw.py` on every book |
| 18 | Slow-class overrun; Quest squeezed | No part OVER in the slow-class model; in lessons 10, 20, 30, 40 the Quest is never the part that shrinks | timing model |
| 19 | Mi's calculator image; stale builds (L3, L10, L11, L17 kept the old Mi because the validator blocked a rebuild) | The no-calculator image everywhere; rebuild every lesson after a template change; rebuild the books after | build log check |
| 20 | Real-size ruler claims false in the books (94.3 percent scale) | No "real size" claim; "The figure is not drawn to scale."; tasks that measure use the child's own ruler or protractor on real objects | text scan |
| 21 | The copy check failed on our own catalogue text (L3, L10, L11, L17) | TL2 excludes our own catalogues (`p*_non_routine_catalogue.md`) and adds the school text and the holiday files `p5/content/l1.js` to `l10.js` | validator |
| 22 | Recording notice said after the recording started (L13 to L20) | Notice first | script check |
| 23 | Quest tutor notes printed wrong part answers (L20 gate 6: 20 and 17 against 15 and 11) | Part answers generated from the values and compared by the verify script (the Q ids of section 8) | verify script |
| 24 | The error-spotter was always the same name | Spread across the cast; "a child" for wrong working | text scan |
| 25 | Investigation tables and drawing boxes missing (Term 1 audits L1, L2, L8, L10) | `table` figure and `visuals` on page 5 where the task needs them | page view |
| 26 | Hand-off omitted what the next lesson cuts (L10 to L11, L7 to L8) | Section 7 is the source for every `next_materials` | TL5 |
| 27 | Plan contamination: another level's lesson list pasted into a plan (the Level 3 plan carried Level 5 text) | Section 4 here is Level 5 text and cites `p5_*`; the Level 5 plan was checked | reviewer reads the first lines of each plan section |
| 28 | Holiday items repeated in the term lesson (the holiday course is the same strands) | Section 3 register; TL2 fails the build on a 7-word overlap with `p5/content/l1.js` to `l10.js`; the audit checks the register | validator and independent audit |
| 29 | Fractions, mixed numbers and percent typeset as plain text; answer boxes for a fraction missing | Y2 stacked fractions and `[w n/d]` fields in the first build; no "3/4" typed by hand in a child sentence | page view; RN9 |
| 30 | Wording drift for money and tax: GST at 7 percent, cents without the sign, "$0.50" beside "50¢" | GST 9 percent; $4.75 for amounts with dollars and 80¢ for cents only; 7 percent only in labelled older-paper practice | TL11 linter |
| 31 | The Quest feels like a test to older children (all L1 audits note private paper but the wording matters more at 10 to 12) | Map-and-gates story; pairs; no "check" word anywhere; the tutor never adds up; the cave is optional | validator banned words; tutor guide |
| 32 | Figure-dependent items with no figure on the page (42 percent of the school items) | Every picture item has its figure in the workbook, not only described; "wording unverified" until the owner supplies a picture (D21) | page view |

## 11. Risks

1. **Holiday overlap (19 Heavy lessons).** The register in section 3 is built from the question stems of the holiday banks; a repeated item is the most likely audit finding. Mitigation: authors read `p5/content/lN.js` for their lesson first; TL2 fails the build on a 7-word overlap; the independent audit checks the register; the plan's own contest items in lessons 5, 21, 26, 27, 28, 30 have been replaced.
2. **Plan contradictions.** Plan section 5 (the 30-minute check), the "Review and Challenge" titles and the Term 4 check in lesson 37 or 38 are superseded (finding 2). Anyone who builds lesson 10 from the plan will write a test. Use sections 1.2 and 8.
3. **Picture dependence.** 42 percent or more of the school items need a figure and 22 figure items do not exist. If figure work slips, drop first the optional ones (the rope of Y10, Y14 chords, Y21), then the picture options of lesson 19, never a Start here item. Lessons 7, 8, 11, 13, 15, 19, 31, 32 cannot start before their figures.
4. **Black and white and the 94.3 percent print scale.** Colour is decoration only; no task may depend on a printed length; "The figure is not drawn to scale." on every figure page; the colouring lesson uses letters.
5. **Reading load.** Primary 5 stems are one to three sentences with (a) and (b); Level 5 children read themselves, but a Think harder item with a new word needs the tutor to read it. New vocabulary per lesson goes in the parent word list ("exterior angle", "simplest form", "GST", "interest", "average").
6. **Tier honesty.** Likeliest slips: an unbracketed order-of-operations item with a hidden trap at lesson 3 Start here; a mixed-number regroup at lesson 4 Start here; the word "ratio" or "a : b" at lesson 24 Start here (it must stay at Think harder); a percent of a remainder at lesson 21 Start here; the exterior angle at lesson 8 Start here; a polygon sum at lesson 31 Start here. An independent reader checks every Start here item against `syllabus_by_level.md`.
7. **Joining cold.** Term 1 Start here uses Primary 4 skills only; later terms re-teach one earlier idea in under five minutes (bar models in 24, angle facts in 8 and 31, volume in 13). A mid-year joiner who never met lesson 24's units meets them again in 36 and 37 through the warm-up only. Lesson 8 recalls the angle facts and does not teach them (D9): a Term 1 joiner who has not done the holiday course may need the catch-up page.
8. **SASMO near-copies and the "no SASMO preparation" claim.** Plan items replaced (finding 3); no contest text; the 7-word check against the SASMO analysis stays. Child and parent pages never say SASMO, MOE-aligned or GEP.
9. **Lessons with little or no school evidence.** Lessons 9, 33 (clock-hand angles), 34, 35, 38, 39, 40 and the isometric half of 19. They are labelled beyond school and each has a named swap candidate (D13).
10. **Quest lessons are tight.** Explore 10 and Mini-lesson 9 minutes. Lessons 10, 20 and 30 are reviews, so the shortened teaching costs no new content; lesson 40 adds a 20-minute showcase after the Quest, so its Explore and Mini-lesson are the shortest of the year.
11. **Timing.** The Level 1 audits found the workbook 3 to 4 minutes over in a slow class in every lesson and the 5-minute buffer consumed. Level 5 children write more per question and the plan keeps six Start here questions. Measure in the trial; if confirmed, cut one warm-up group per lesson.
12. **Cutting load.** 146 pieces a year (section 6); Term 3 about 59, Term 4 about 46. The heaviest are lesson 28 (21 coins) and lesson 1 (13 tiles). Options: real coins for lesson 28, a pack of playing cards for lesson 35, paper plates for lesson 4.
13. **Real coins and play money.** The same open legal question as Level 1 (D1 there) for lesson 28: stylised pieces marked PLAY MONEY. Check before anything realistic is printed (D25).
14. **Wording evidence.** The papers were read from OCR text; no picture was seen in any paper (patterns section 6). Items whose form rests on a picture (angle figures, graphs, views, tanks, isometric drawing) are "wording unverified" until the owner supplies pictures or sample papers (D21).
15. **Two syllabus eras.** The 2020 to 2024 papers set ratio, average and speed at Primary 5; the 2025 papers do not. Level 5 keeps ratio (24) and average (17) as labelled previews and excludes speed (D14, D17). A tutor must not tell a parent that either is on the P5 syllabus.
16. **Books.** Eight books of about 36 to 40 pages (Books 2, 4, 6, 8 carry a 4-page Quest Log); a book boundary falls at lessons 5, 15, 25, 35 mid-term; if a book is late the hand-off fails (D10). The Quest Log must stay closed in its envelope.
17. **Slots and exams.** The 90-minute lessons need slots re-derived from the 2027 grid (owner entry of 23 Oct, still open). P5 children sit school papers in late Oct and Nov, so Term 4 attendance dips (D30); lesson 40 is best attended.
18. **Website, privacy and terms.** Still describe the holiday beta; the Level 1 findings F10 and F11 apply unchanged (no Level 5 term page, the photo return flow unnamed in the privacy notice). Not a lesson-file concern.
19. **Parallel agents on shared files.** Same rule as Level 1: only the template owner edits shared tools; lesson agents write only their own files and commit with explicit `git add`, never `git add -A`.
20. **Authoring documents are Level 1 specific.** `AUTHORING.md` lists Lessons 2 to 10 and Terms 3 and 4; `LESSON_BRIEF.txt` names Lesson 1 as the pilot: a Level 5 brief (TL8) before agents start.
21. **Scissors in lesson 15.** The only lesson where the child cuts. If the owner prefers no scissors, the dissection becomes a folding task and the "cut" wording is removed (D5).
22. **Cross-level build dependencies.** Y2, Y3, Y4, Y8, Y9, Y12, Y13, Y15 to Y18 and Y22 are also planned at Levels 2 to 4. If two levels build the same figure in parallel the code diverges; one owner per figure (section 13).
23. **Hours are estimates.** Taken from Level 1 documents; Level 5 lessons carry more verification (every Beyond item and every Think harder number has a brute-force check) and more figures than Level 1.

## 12. Decisions the owner must make (defaults I chose are marked [Default])

None is irreversible; changing a default after the build costs time, as noted.

- **D1. Plan sections that later decisions supersede.** [Default] Treat plan section 5 (the 30-minute check), the "Review and Challenge" titles and the Term 4 check placement as superseded by Mi's Challenge Quest in lessons 10, 20, 30 and 40. The plan text is not edited here (I was told to touch only my file). Cost of waiting: authors may follow the plan.
- **D2. Holiday overlap policy.** 19 lessons share a strand and kinds of item with a holiday lesson (section 3). [Default] Keep the plan's lesson list (the strands are the school strands), forbid item reuse by the register and TL2, and say in the tutor guide that holiday graduates will recognise the topic but not the questions. [Alternative] Swap the largest overlaps (lessons 13 and 16 with H5 and H6; 24 with H3) for other Primary 5 topics; a swap costs about a day of re-planning each.
- **D3. Titles of lessons 10, 20, 30 and 40.** [Default] "Term N Review and Mi's Challenge Quest" and "Year Showcase and Mi's Challenge Quest" (the validator bans the bare word "challenge" on child pages).
- **D4. Replacements of plan items that repeat the holiday or SASMO.** Dropped or replaced: the telescoping product (5), heads and legs (25, 28), quiz scoring (28, 30), 40% of 60 against 60% of 40 (21), matchstick figures and beads (26), digits in page numbers (27), fraction-then-fixed-amount (36), pour-back until equal (13). [Default] All replaced as in sections 1 and 4. GC has 3 lessons (the papers give 30 of 2279 items).
- **D5. Scissors.** [Default] A grown-up, or the child with a grown-up, cuts before the lesson; scissors never in a lesson, except lesson 15 where the child cuts a paper parallelogram and trapezium (age 10 to 12). [Alternative] Fold instead of cut in lesson 15.
- **D6. Ruler, protractor, tape.** [Default] A 30 cm ruler from lesson 7, a protractor from lesson 8 (optional), tape in lesson 11, scissors and glue in lesson 15; no printed ruler (the Level 1 owner choice) and no real-size claim in the books.
- **D7. Marks on child pages.** [Default] None. The papers print marks; our pages use an "Ans:" frame and a "Working" box, and the Quest has no score.
- **D8. Calculators.** [Default] None in any lesson, and Mi never shows one. The holiday explore (H1) and the school Paper 2 (2020 to 2024) allow one. [Alternative] A calculator-allowed set in lessons 14 and 29 only.
- **D9. Angle facts in lesson 8.** [Default] Recalled in the warm-up with a printed angle-facts card, not taught (plan open question 6); a joiner without the facts uses the catch-up page. [Alternative] Teach lines, points and vertically opposite angles in full, at the cost of the triangle chain.
- **D10. Books and payment.** [Default] Both books of a term are issued with the first payment; a mid-term joiner receives the full book and the books for lessons still to come; hand-off lines say "your book".
- **D11. When to build.** [Default] Build Term 1 now (waves A and B first), start the template work for Terms 2 to 4 in parallel, write Terms 3 and 4 after the first tutor trial of Term 1 reports timing, then run one 40-lesson consistency sweep.
- **D12. Words outside the syllabus.** [Default] "Prime", "coordinates", "pentagon", "hexagon", "surface area", "median", "probability" appear only at Think harder or Go further or inside a Beyond puzzle, with a one-line level note; never at Start here.
- **D13. Weak or no-evidence lessons.** 9, 33 (hand angles), 34, 35, 38, 39 and 40 keep their place as beyond school, each marked "safest to skip" or "fairly safe". Swap candidates: 9 to "Pie charts and averages" (P4 spiral plus the 2020 to 2024 average items), 39 to "Nets and solids revisited", 34 or 35 to a second Review studio. A swap costs about a day.
- **D14. Speed.** [Default] Out of Level 5, as the plan. The KIV secondary preview of catching-up problems in lesson 16 is not included (Level 6 holds speed).
- **D15. Merge 31 and 32.** [Default] Not merged (plan open question 2); with 10-week terms the freed slot is not needed.
- **D16. Lesson 35 is too full (KIV).** [Default] Keep. Tutor-guide skip order: Go further 3, then Go further 2, then Think harder 4. If the trial shows it is too full, move "In the Dark" to lesson 38.
- **D17. Previews.** [Default] Average (17), ratio notation (24), percentage change (21, 29), find the whole (23), fraction division (not used, it is in H2) and compound interest (29) stay at Think harder and Go further as labelled P6 previews.
- **D18. Foundation track.** [Default] Not covered and not claimed (MOE pp. 45 to 50 revisit P1 to P4).
- **D19. Quest Log pages.** [Default] 4 pages for ages 10 to 12 (as Level 4); 3 at Levels 1 and 3.
- **D20. Photo return of the Quest Log.** [Default] The parent sends the Quest Log to the business WhatsApp (+65 9880 5962); tutors never use personal phones; the number is not on slides.
- **D21. Wording evidence.** Please supply (or point to) one Primary 5 paper or quiz that shows each of: an angle-chase figure, a line graph, cube views and isometric drawing, a tank with a block, and a folded-paper figure. [Default] Write with the wording patterns and mark every picture item "wording unverified".
- **D22. Entry check for joiners.** [Default] None at launch. A five-minute eight-question Primary 4 check at sign-up with a catch-up page per result can be built after the first trial (shared TL7).
- **D23. Weekly workload statement.** [Default] "Home Practice (about 15 minutes) if you like; pages 3 to 5 and online practice are optional." Reports use one descriptive line from the tutor's private notes, not a strand profile; the plan's four report lines become the sentence stems.
- **D24. Beyond field.** The beyond-syllabus rule is recorded (owner decisions, 23 Oct). [Default] The tutor-only `beyond` field is required in all 40 lessons from the start; the child-facing name is a puzzle title and never carries the word "challenge".
- **D25. Play money legal check.** [Default] Stylised coins marked PLAY MONEY in lesson 28; real coins from a purse are the first choice. I have not checked Singapore's rules on reproducing coins.
- **D26. Slots.** The 90-minute term slots are not yet re-derived from the 2027 grid (owner entry of 23 Oct). Hand-off lead times assume a week.
- **D27. Runner keys.** [Default] `l5t1l01` ... `l5t4l40` (the level prefix is new).
- **D28. File layout and tools.** [Default] `term/l5/` holds the data; the Level 1 tools are imported through the shared `level` parameter and new figures live in `figs5.py`. Moving the tools to a shared folder is cleaner but disturbs the agents still building Level 1; do it after Level 1 Term 4 is audited.
- **D29. GST rate.** [Default] 9 percent on child pages (the 2025 papers); an older-paper practice item may say 7 percent and says so in the stem.
- **D30. Exam weeks.** [Default] A missed lesson is made up by recording or, if there is a seat, a holiday class. Lesson 40 (Quest and showcase) is the one to attend; its make-up route is the Quest at the make-up slot and the recording of the showcase.
- **D31. Tutor reading aloud.** [Default] The tutor reads every Quest gate once and any Think harder stem with a new word; Start here items are read by the children.
- **D32. Mi on older children's pages.** [Default] Title and goodbye slides, the Quest and the parent page only; no Mi on workbook pages beyond the corner mascot.
- **D33. Lessons 7 and 8 against H4 and H8 (plan open question 5).** [Default] Keep both with the barred lists of section 3 and test them with one holiday graduate before the Term 1 launch. [Alternative] Replace lesson 8 with the construction of triangles (compass and protractor), which the holiday course does not touch.
- **D34. Lesson 19 figures.** [Default] Figures are drawn first (Y10); if they slip, lesson 19 loses its rope item and its matrix item and keeps the isometric drawing and the views.
- **D35. Cross-level build owner.** [Default] One template owner builds each shared figure once (section 13); Level 5 does not start Y2, Y3, Y9 before the earlier level plans say who owns them.

## 13. Build order, effort and cost

### 13.1 Dependencies in the content

Lesson 1 feeds 6 and 14 (shifting); 2 feeds 35; 4 and 5 feed 21 to 25 and 36; 7 feeds 15; 8 feeds 31 to 33; 11 feeds 19; 12 feeds 13 and 19; 13 feeds 20; 16 feeds 29; 21 feeds 22, 23 and 29; 22 feeds 29; 24 feeds 25, 36 and 37; 25 feeds 36; 26 stands alone; 31 feeds 32 and 33; lessons 10, 20, 30 and 40 need every earlier lesson of their term to have passed its fix pass (answers fixed) before the Quest is written. The plan says a lesson does not assume the previous one except through Remember, so these are build-order and wording-consistency dependencies, not content ones. Lesson 36 and 37 use words from 24, 22 and 28 and must match their fixed wording ("unit", "bar", "table", "work backwards").

### 13.2 Waves and sprints

**Sprint A (day 0, one engineer, about half a day):** TL1 (level parameter), TL2 (copy-check list with `p5/content`), TL8 (author brief), TL11 (wording linter), TL12 (`verify_lib.py`), **Y2** (stacked fractions and mixed numbers), RN9 and RN10, Y3 (`bar_model` extension), Y1 and KT1; then write **Lesson 1** (pilot of Level 5 conventions: identity, footers, the Opening script, the hand-off wording). **In parallel, wave A** (Y2 and RN10 exist, kit work only): lessons 2, 3, 16, 22, 28, 29, 33, 35, 36, 37, 38.
**Sprint B (two engineers):** Y4, Y7, RN11, RN12, RN13, KT2, KT3, TL14. **Wave B:** lessons 4, 5, 6, 9, 14, 21, 23, 24.
**Sprint C (the geometry engineer, longest piece):** Y5, Y6 (14 hours), Y20, KT5, KT11. **Wave C:** lessons 7, 8, 15, 31, 32.
**Sprint D:** Y8, Y9, Y10, Y11, KT4. **Wave D:** lessons 11, 12, 13, 19.
**Sprint E:** Y12 to Y19, KT7 to KT10, KT13, KT14, RN14, RN15, TL15. **Wave E:** lessons 17, 18, 25, 26, 27, 34, 39.
**Wave Q:** lessons 10, 20, 30 and 40 last in their term, after TL3 and the Quest Logs; the term books after each term's fix pass.
**Audit and fix per term**, then the three term-wide second-round audits (guide and deck; home, parent and practice; term-wide), as at Level 1. After Term 4: one 40-lesson consistency sweep (rewind items, hand-offs against section 7, beyond table, books, B&W check), the cold-join trial (lessons 1 and 21 with one child who has only done the holiday course) and the holiday-graduate trial of lessons 7 and 8 (D33).
Which lessons can be written first with the tools as they stand plus Y2 and RN10: 2, 3, 38 (nothing to build), then 16, 22, 28, 29, 33, 35, 36, 37 (a kit or a table). Lessons 7, 8, 11, 13, 15, 19, 31, 32 cannot start until their figures exist.

### 13.3 Effort (agent-hours, not measured)

Per lesson, total hours = write and build + wording review + audit + fix pass, the Level 1 split (about 4.5, 0.7, 1.0, 1.3), raised where a lesson needs a new figure or a long verification. Level 1 evidence: lesson totals 6.0 to 9.0, Quest lessons 12.5 to 13.5; Term 2 took about 6.5 hours wall clock from pre-flight to the end of the first fix pass with parallel agents.

| Lesson | Write and build | Wording review | Audit | Fix pass | Total |
|---|---|---|---|---|---|
| 1 Shifting Places | 5.0 | 0.7 | 1.0 | 1.3 | 8.0 |
| 2 Factor Finders | 4.5 | 0.7 | 1.0 | 1.3 | 7.5 |
| 3 Smart Calculation | 4.5 | 0.7 | 1.0 | 1.3 | 7.5 |
| 4 Mixed Numbers and Sharing | 5.0 | 0.8 | 1.2 | 1.5 | 8.5 |
| 5 Fractions of Fractions | 5.0 | 0.8 | 1.2 | 1.5 | 8.5 |
| 6 Decimal Sense | 4.8 | 0.7 | 1.2 | 1.3 | 8.0 |
| 7 Boxed-In Triangles | 5.0 | 0.8 | 1.2 | 1.5 | 8.5 |
| 8 Angles and Triangle Families | 5.5 | 1.0 | 1.5 | 1.5 | 9.5 |
| 9 Two Groups and the Overlap | 4.5 | 0.7 | 1.0 | 1.3 | 7.5 |
| 10 Term 1 Review and Mi's Challenge Quest | 9.5 | 0.7 | 1.5 | 1.8 | 13.5 |
| 11 Solid Views and Dice | 5.5 | 0.8 | 1.5 | 1.7 | 9.5 |
| 12 Boxes and Bricks | 5.0 | 0.8 | 1.2 | 1.5 | 8.5 |
| 13 Tank Tales | 5.2 | 0.8 | 1.5 | 1.5 | 9.0 |
| 14 Decimal Measures | 4.5 | 0.7 | 1.0 | 1.3 | 7.5 |
| 15 Cut and Rearrange | 5.2 | 0.8 | 1.5 | 1.5 | 9.0 |
| 16 Rate and Working Together | 4.8 | 0.7 | 1.2 | 1.3 | 8.0 |
| 17 Fair Shares | 4.5 | 0.7 | 1.0 | 1.3 | 7.5 |
| 18 Graph Stories | 4.5 | 0.7 | 1.0 | 1.3 | 7.5 |
| 19 Isometric Builders | 6.0 | 0.8 | 1.5 | 1.7 | 10.0 |
| 20 Term 2 Review and Mi's Challenge Quest | 9.5 | 0.7 | 1.5 | 1.8 | 13.5 |
| 21 Percent Sense | 4.5 | 0.7 | 1.0 | 1.3 | 7.5 |
| 22 Shop Smart | 4.8 | 0.7 | 1.2 | 1.3 | 8.0 |
| 23 One Number as a Percent of Another | 4.5 | 0.7 | 1.0 | 1.3 | 7.5 |
| 24 Unequal Parts | 5.2 | 0.8 | 1.5 | 1.5 | 9.0 |
| 25 Balance and Undo | 5.2 | 0.8 | 1.5 | 1.5 | 9.0 |
| 26 Number Stories | 5.0 | 0.8 | 1.2 | 1.5 | 8.5 |
| 27 Count Without Counting | 5.0 | 0.8 | 1.2 | 1.5 | 8.5 |
| 28 Supposition Studio | 5.0 | 0.8 | 1.2 | 1.5 | 8.5 |
| 29 Money Grows | 4.2 | 0.7 | 1.0 | 1.1 | 7.0 |
| 30 Term 3 Review and Mi's Challenge Quest | 9.5 | 0.7 | 1.5 | 1.8 | 13.5 |
| 31 Angles in Shapes | 5.0 | 0.8 | 1.2 | 1.5 | 8.5 |
| 32 Triangles and Quadrilaterals | 5.0 | 0.8 | 1.2 | 1.5 | 8.5 |
| 33 Clocks and Calendars | 4.5 | 0.7 | 1.0 | 1.3 | 7.5 |
| 34 Logic Grids and Digit Puzzles | 5.0 | 0.8 | 1.2 | 1.5 | 8.5 |
| 35 Odd, Even, Remainders and Extremes | 5.0 | 0.8 | 1.2 | 1.5 | 8.5 |
| 36 Working Backwards | 4.5 | 0.7 | 1.0 | 1.3 | 7.5 |
| 37 The Long Question | 4.8 | 0.7 | 1.2 | 1.3 | 8.0 |
| 38 Children Set the Problem | 4.2 | 0.7 | 1.0 | 1.1 | 7.0 |
| 39 Colouring, Cycles and Choices | 4.8 | 0.7 | 1.2 | 1.3 | 8.0 |
| 40 Year Showcase and Mi's Challenge Quest | 9.0 | 0.7 | 1.5 | 1.8 | 13.0 |
| **Term 1 / 2 / 3 / 4** | | | | | **87.0 / 90.0 / 87.0 / 85.0** |

Plus four term-wide second-round audits (about 8 hours each, 32) and one 40-lesson consistency sweep (about 10): **about 391 agent-hours** for the lessons. Template engineering (section 5): **193 hours if everything is built from scratch, 141 with the deferrals and with the shared items built by earlier levels, about 84 for the Level 5 share alone**. Together about 532 to 584 hours.

Elapsed time, at the Level 1 pace (eight to ten writing agents and three engineers working as in 13.2): Term 1 about 2 working days including the figure foundations, Term 2 about 2.5 (the solids, tank and isometric figures), Term 3 about 2, Term 4 about 2, plus audits and fixes, so **about 9 to 11 working days** from Sprint A to an audited Term 4; if the template work is done serially before any lesson starts, add about 2 days. Not in these numbers: a tutor trial per term, the cold-join trial, the holiday-graduate trial, the legal check (D25), the owner's paper search (D21), and the owner and tutor review time (allow another 20 to 25 hours across the year).

## 14. What was not checked

- No lesson, tool or output was run or built; the figure inventory was read from the working tree, which holds uncommitted edits to `figs2.py`, `figs3.py` and `svg.py` by other agents, so section 5.1 reflects the tree on 23 Oct, not a commit. Hours are estimates.
- The holiday register compares question stems and objectives of `p5/content/l1.js` to `l10.js` that I extracted by loading the modules (`qbank` core, stretch and challenge, `lesson.extension`, `lesson.share`, `lesson.exit`); it did not read the holiday decks, scripts, workbooks or the enrichment files `gaps.js` and `inv.js` in full (only their headers), so an overlap that exists only there would be missed (TL2 reads the files).
- MOE placements come from `docs/moe/syllabus_by_level.md`; I did not re-open the PDF. The words "prime", "coordinates", "pentagon" and "hexagon" are taken from its "not in the syllabus anywhere" row, which is a text search by an earlier agent.
- No Primary 5 picture was seen in any paper; no angle diagram, graph, cube view, tank or isometric figure could be compared with a school style. The papers were read from OCR text. Counts describe this set of papers, not the country.
- The Level 2, 3 and 4 pre-flights were read for template codes and Quest rules only; their lesson lists were not compared with Level 5 for overlap. The Level 3 pre-flight lists its lesson 36 (brackets) as overlapping Level 4 lesson 1.2 and Level 5 "lesson 1" (the brackets lesson of the Level 5 plan is lesson 3); a child who came through Levels 3 and 4 meets brackets three times (an accepted spiral, D17).
- Singapore's rules on reproducing coins were not checked (D25).
- The Foundation track and the 2013 P6 syllabus were not read.
- The 2027 term slot grid for 90-minute lessons is not re-derived here (owner entry of 23 Oct, still open).
- The "Start here" items in the lesson specs without a check id are trivial arithmetic for the author's own verify script; every id quoted in the specs, the Quest tables and section 4 has a check in the appendix.
- Beyond puzzles are original in numbers and context; several rest on well-known ideas (lockers, Pick's rule, the star angle sum, the chord regions, the pigeonhole principle, Petersen colouring). The 7-word check protects against copied text, not against a famous puzzle; the lesson authors should not present them as invented.

## Appendix: the check script

`verify_l5_preflight.py`, run with `python3 -I verify_l5_preflight.py`. On 23 Oct 2026 it printed `verify_l5_preflight: 265 checks, 265 passed`. Checks are brute force: all digit assignments, all permutations, breadth-first search of jug states, every colouring, every cube arrangement, every bracketing, a geometric region count for the chord circle, a rolling-cube fold of the dice net; they use no formula from the lessons. The script writes no file and prints one summary line when everything passes.

```python
#!/usr/bin/env python3
"""Brute-force checks for every number quoted in docs/terms/l5_preflight.md (run: python3 -I verify_l5_preflight.py)."""


# ======================================================================
# Term 1 (lessons 1 to 10)
# ======================================================================
import itertools, math
from fractions import Fraction as F

R = []
def ck(i, got, exp):
    ok = got == exp
    R.append((i, ok))
    if not ok: print("FAIL", i, "got", got, "expected", exp)

def digsum(n): return sum(int(c) for c in str(n))
def divisors(n): return [d for d in range(1, n + 1) if n % d == 0]

# ---------------- Lesson 1 Shifting Places
ck("V1.1", (4207 * 100, 530000 // 1000, 36 * 200, 45000 // 500, 7200000 // 4000, 18 * 3000), (420700, 530, 7200, 90, 1800, 54000))
# V1.2 Cross Out a Digit: crossing out the last digit makes the number 2826 smaller. Find every number.
sol = [n for n in range(10, 100000) if n - n // 10 == 2826]
ck("V1.2", sol, [3139, 3140])
# V1.3 stadium 5 times the hall, together 36 000; seats added to the hall so the stadium has 3 times as many
sol = [(h, 5 * h) for h in range(1, 36001) if h + 5 * h == 36000]
hall, stad = sol[0]
added = [a for a in range(0, 30000) if stad == 3 * (hall + a)]
ck("V1.3", (hall, stad, added), (6000, 30000, [4000]))
# V1.4 smallest even 4-digit number using each of 6, 0, 9, 4 once
cands = [int("".join(p)) for p in itertools.permutations("6094") if p[0] != "0" and int(p[-1]) % 2 == 0]
ck("V1.4", min(cands), 4096)
# V1.5 rounds to 400 000 to the nearest ten thousand, digit sum 13, ends in 7
ok = [n for n in range(395000, 405000) if digsum(n) == 13 and n % 10 == 7]
ck("V1.5", (400117 in ok, 395000 <= 400117 < 405000, sum(int(c) for c in "400117")), (True, True, 13))
V15_SAMPLE = ok[:6]

# ---------------- Lesson 2 Factor Finders
ck("V2.1", (len(divisors(36)), len(divisors(48)), [d for d in divisors(24) if 36 % d == 0], [m for m in range(1, 40) if m % 4 == 0 and m % 6 == 0]),
   (9, 10, [1, 2, 3, 4, 6, 12], [12, 24, 36]))
five = [n for n in range(1, 20000) if len(divisors(n)) == 5]
ck("V2.2", (five[:4], all(round(n ** 0.5) ** 2 == n for n in five), {n % 2 for n in five[:4]}, [n < 100 for n in five[:4]]),
   ([16, 81, 625, 2401], True, {0, 1}, [True, True, False, False]))
ck("V2.3", (math.gcd(48, 72), 48 // math.gcd(48, 72), 72 // math.gcd(48, 72)), (24, 2, 3))
l = 9 * 12 // math.gcd(9, 12)
ck("V2.4", (l, min(m for m in range(201, 400) if m % 9 == 0 and m % 12 == 0)), (36, 216))
ck("V2.5", [n for n in range(10, 100) if n % 8 == 0 and digsum(n) == 10 and n % 7 == 1], [64])
ck("V2.5b", [n for n in range(10, 100) if n % 8 == 0 and digsum(n) == 10], [64])
ck("V2.6", (len([n for n in range(100, 501) if n % 7 == 0]), len([n for n in range(100, 501) if n % 7 == 0 and n % 14 != 0])), (57, 29))
# lockers: 100 lockers, pupil k flips every k-th
state = [False] * 101
for k in range(1, 101):
    for j in range(k, 101, k): state[j] = not state[j]
ck("V2.7", ([i for i in range(1, 101) if state[i]], all((len(divisors(n)) % 2 == 1) == (round(n ** .5) ** 2 == n) for n in range(1, 2000))),
   ([1, 4, 9, 16, 25, 36, 49, 64, 81, 100], True))
ck("V2.8", min(n for n in range(1, 100) if n % 4 == 0 and n % 6 == 0 and n % 24 != 0), 12)
ck("V2.9", ([d for d in range(10) if (5 + d + 7 + 2) % 9 == 0], [d for d in range(10) if int(f"3{d}48") % 4 == 0 and (3 + d + 4 + 8) % 3 == 0]), ([4], [0, 3, 6, 9]))

# ---------------- Lesson 3 Smart Calculation
ck("V3.1", (24 - 6 // 3 * 2, (24 - 6) // 3 * 2, 2 + 3 * 4 ** 2 // 2), (20, 12, 26))
ck("V3.2", (47 * 36 + 47 * 64, 99 * 25, 125 * 8 * 7 * 4 * 25 == 125 * 8 * 7 * 100), (4700, 2475, True))
a = (37 * 25) + (18 * 44); b = (37 * 25) + (19 * 44) + 3
ck("V3.3", (a % 2, b % 2), (1, 0))
ck("V3.5", 60 - (6 * 4 + 3 * 9), 9)

def values(nums, ops):
    """every value of nums[0] ops[0] nums[1] ... over all bracketings; exact fractions; None if division by zero."""
    if len(nums) == 1: return [F(nums[0])]
    out = []
    for k in range(1, len(nums)):
        for x in values(nums[:k], ops[:k - 1]):
            for y in values(nums[k:], ops[k:]):
                o = ops[k - 1]
                if o == "+": out.append(x + y)
                elif o == "-": out.append(x - y)
                elif o == "*": out.append(x * y)
                elif o == "/":
                    if y != 0: out.append(x / y)
    return out
v = values([48, 6, 2, 4, 1], ["/", "*", "+", "-"])
ck("V3.4", (len(v), len(set(v))), (14, 9))
# POSE: make 24 from 3, 4, 6, 9 using each once, + - x / and brackets
def make(vals):
    # vals: list of (value, expr)
    if len(vals) == 1: return [vals[0]]
    res = []
    for i in range(len(vals)):
        for j in range(i + 1, len(vals)):
            rest = [vals[k] for k in range(len(vals)) if k not in (i, j)]
            (x, ex), (y, ey) = vals[i], vals[j]
            cand = [(x + y, f"({ex}+{ey})"), (x * y, f"({ex}*{ey})"), (x - y, f"({ex}-{ey})"), (y - x, f"({ey}-{ex})")]
            if y != 0: cand.append((x / y, f"({ex}/{ey})"))
            if x != 0: cand.append((y / x, f"({ey}/{ex})"))
            for c in cand: res += make(rest + [c])
    return res
sols = {e for (v_, e) in make([(F(n), str(n)) for n in (3, 4, 6, 9)]) if v_ == 24}
ck("V3.6", len(sols) > 0, True)

# ---------------- Lesson 4 Mixed Numbers and Sharing
ck("V4.1", (F(7, 3) - 2, F(17, 5) - 3, F(23, 4) - 5), (F(1, 3), F(2, 5), F(3, 4)))
ck("V4.2", (F(13, 4) - F(11, 8), F(17, 6) + F(7, 4)), (F(15, 8), F(55, 12)))
left = 560 - F(3, 7) * 560; left -= F(3, 8) * left
ck("V4.3", left, 200)
r = [(R_, B) for B in range(1, 3000) for R_ in [F(8, 9) * B] if R_.denominator == 1 and B - R_ == 56]
ck("V4.4", (r, F(3, 4) * 448, F(2, 3) * 504), ([(448, 504)], 336, 336))
ck("V4.5", sum(F(1, 2 ** k) for k in range(1, 6)), F(31, 32))
ck("V4.6", (F(11, 4) * 60, [F(1, 2) + F(1, 4) + F(1, 8) + F(1, 16) + F(1, 32) < 1]), (165, [True]))

# ---------------- Lesson 5 Fractions of Fractions
ck("V5.1", (F(2, 3) * F(3, 4), F(5, 6) * F(9, 10), F(11, 4) * 6), (F(1, 2), F(3, 4), F(33, 2)))
vals = []
for p in itertools.permutations([2, 4, 5, 9]):
    a_, b_, c_, d_ = p
    if a_ < b_ and c_ < d_:
        vals.append((F(a_, b_) * F(c_, d_), p))
ck("V5.2", (max(vals), min(vals)), ((F(5, 18), (5, 9, 2, 4)), (F(8, 45), (2, 5, 4, 9))))
ck("V5.3", all((F(n) + F(1, 2)) ** 2 == n * (n + 1) + F(1, 4) for n in range(1, 40)), True)
ck("V5.3b", (75 * 75, 7 * 8 * 100 + 25), (5625, 5625))
rest = F(2, 5) * F(3, 4)  # fraction left after 3/5 then 1/4 of rest
start = 27 / rest
ck("V5.4", (start, start * F(3, 5), (start - start * F(3, 5)) / 4), (90, 54, 9))
# backwards: gave 1/3 and 2 more, then half the rest and 1 more, 6 left
sol = [x for x in range(1, 200) if (lambda a: (a - (a // 2 + 1)) == 6 if a % 2 == 0 else False)(x - (x // 3 + 2)) and x % 3 == 0]
ck("V5.5", sol, [24])

# ---------------- Lesson 6 Decimal Sense
ck("V6.1", (F("3.45") * 100, F("0.078") * 1000, F("52.6") / 100), (345, 78, F("0.526")))
ck("V6.2", (float(F(3, 8)), float(F(7, 20)), float(F(5, 16))), (0.375, 0.35, 0.3125))
import decimal
def rnd1(x):  # round half up to 1 d.p.
    return F(math.floor(x * 10 + F(1, 2)), 10)
two = [F(n, 100) for n in range(400, 460)]
ok = [x for x in two if rnd1(x) == F("4.3")]
ck("V6.3", (min(ok), max(ok)), (F("4.25"), F("4.34")))
s, d = F("7.5"), F("2.3")
ck("V6.4", ((s + d) / 2, (s - d) / 2), (F("4.9"), F("2.6")))
# Ravi has 9.60 more than Siti; Ravi spends 19.20; then Siti has 3 times Ravi's left
sol = [(S / 100, R_ / 100) for S in range(0, 10000) for R_ in [S + 960] if S == 3 * (R_ - 1920)]
ck("V6.5", sol, [(14.4, 24.0)])
term = []
for n in range(2, 21):
    m = n
    while m % 2 == 0: m //= 2
    while m % 5 == 0: m //= 5
    if m == 1: term.append(n)
ck("V6.6", (term, len(term)), ([2, 4, 5, 8, 10, 16, 20], 7))
def period(n):
    seen = {}; r = 1; digits = ""; i = 0
    while r and r not in seen:
        seen[r] = i; r *= 10; digits += str(r // n); r %= n; i += 1
    return digits[seen[r]:] if r else ""
ck("V6.7", (period(3), period(7), period(11)), ("3", "142857", "09"))

# ---------------- Lesson 7 Boxed-In Triangles
def shoelace(p):
    n = len(p); s = 0
    for i in range(n):
        x1, y1 = p[i]; x2, y2 = p[(i + 1) % n]; s += x1 * y2 - x2 * y1
    return F(abs(s), 2)
tri = [(1, 1), (6, 3), (3, 7)]
box = 5 * 6   # bounding box of the dots
ck("V7.1", (shoelace(tri), box - (F(5 * 2, 2) + F(3 * 4, 2) + F(2 * 6, 2))), (13, 13))
# Pick's theorem exhaustively on a 6x6 dot grid
def lattice_info(p):
    A = shoelace(p)
    B = sum(math.gcd(abs(p[i][0] - p[(i + 1) % 3][0]), abs(p[i][1] - p[(i + 1) % 3][1])) for i in range(3))
    return A, B
bad = 0; cnt = 0
pts = [(x, y) for x in range(6) for y in range(6)]
for t in itertools.combinations(pts, 3):
    A, B = lattice_info(t)
    if A == 0: continue
    xs = [q[0] for q in t]; ys = [q[1] for q in t]
    I = 0
    for x in range(min(xs), max(xs) + 1):
        for y in range(min(ys), max(ys) + 1):
            # strict inside test with signs
            def sgn(a, b, c): return (a[0] - c[0]) * (b[1] - c[1]) - (b[0] - c[0]) * (a[1] - c[1])
            d1, d2, d3 = sgn((x, y), t[0], t[1]), sgn((x, y), t[1], t[2]), sgn((x, y), t[2], t[0])
            if (d1 > 0 and d2 > 0 and d3 > 0) or (d1 < 0 and d2 < 0 and d3 < 0): I += 1
    cnt += 1
    if A != I + F(B, 2) - 1: bad += 1
ck("V7.2", (bad, cnt > 1000), (0, True))
D, M, N = (0, 12), (6, 0), (12, 6)
ck("V7.3", (shoelace([D, M, N]), F(shoelace([D, M, N]), 144)), (54, F(3, 8)))
ck("V7.4", (F(5 * 3, 2), 2 * F(5 * 3, 2), 3 * 5), (F(15, 2), 15, 15))
ck("V7.5", len([t for t in itertools.combinations([(x, y) for x in range(4) for y in range(4)], 3) if shoelace(t) == 3]), 48)

# ---------------- Lesson 8 Angles and Triangle Families
ck("V8.1", ((180 - 52) / 2, 180 - (180 - 52) / 2, 52 + (180 - 52) / 2), (64.0, 116.0, 116.0))
# AB = BD and AD = DC, angle ABC = 44: find C by construction
import math as m_
def build(x):
    # angle C = x degrees; B = 180 - 4x. Build triangle ABC with C at origin
    xr = m_.radians(x)
    # D on CB with DA = DC: triangle ADC isosceles with base angles x, so angle ADB = 2x
    return 180 - 4 * x
sol = [x for x in range(1, 46) if build(x) == 44]
ck("V8.2", sol, [34])
# numeric check of the construction with coordinates
def check_construction(x):
    xr = m_.radians(x); C = (0.0, 0.0); B = (10.0, 0.0)
    # A such that angle ACB = x and angle ABC = 180-4x
    bang = m_.radians(180 - 4 * x)
    # law of sines
    a = 10.0; Aang = m_.radians(3 * x)
    b = a * m_.sin(bang) / m_.sin(Aang)  # side CA opposite B
    A = (b * m_.cos(xr), b * m_.sin(xr))
    # D on BC: DA = DC -> D = (t,0) with t = b/(2cos x)
    t = b / (2 * m_.cos(xr)); D = (t, 0.0)
    ab = m_.dist(A, B); bd = m_.dist(B, D); ad = m_.dist(A, D); dc = m_.dist(D, C)
    return abs(ab - bd) < 1e-9 and abs(ad - dc) < 1e-9
ck("V8.3", check_construction(34), True)
# star tips sum 180 for random pentagram
import random
random.seed(5)
def tip_sum(pts):
    # pentagram: vertices in order around a circle P0..P4; star lines connect i to i+2; tip at Pi between segments Pi->Pi+2 and Pi->Pi-2
    tot = 0
    for i in range(5):
        a = pts[i]; b = pts[(i + 2) % 5]; c = pts[(i - 2) % 5]
        v1 = (b[0] - a[0], b[1] - a[1]); v2 = (c[0] - a[0], c[1] - a[1])
        cosang = (v1[0] * v2[0] + v1[1] * v2[1]) / (m_.hypot(*v1) * m_.hypot(*v2))
        tot += m_.degrees(m_.acos(cosang))
    return tot
ok = True
for _ in range(200):
    ang = sorted(random.uniform(0, 2 * m_.pi) for _ in range(5))
    pts = [(m_.cos(t), m_.sin(t)) for t in ang]
    if abs(tip_sum(pts) - 180) > 1e-6: ok = False
ck("V8.4", ok, True)
ck("V8.5", [(a_, b_) for a_ in range(1, 180) for b_ in range(1, 180 - a_) if a_ + b_ + (180 - a_ - b_) == 180 and a_ > 90 and b_ > 90], [])

# ---------------- Lesson 9 Two Groups and the Overlap
ck("V9.1", (24 + 19 - (36 - 5), 36 - 5), (12, 31))
ck("V9.2", (28 + 31 - 45, min(28, 31)), (14, 28))
# brute force the least and greatest overlap
ck("V9.2b", (min(k for k in range(0, 29) if 28 + 31 - k <= 45), max(k for k in range(0, 29) if 28 + 31 - k <= 45 and k <= 28)), (14, 28))
p = (85, 97, 102)  # Ann+Ben, Ben+Cara, Ann+Cara
tot = sum(p) // 2
ck("V9.3", (sum(p) % 2, tot - 97, tot - 102, tot - 85), (0, 45, 40, 57))
ck("V9.4", [x for x in range(1, 400) if (F(2, 5) * x * F(1, 2) + F(3, 5) * x * F(1, 3)) == 18 and (F(2, 5) * x).denominator == 1 and (F(3, 5) * x).denominator == 1], [45])
books = {"fic": (84, 66), "non": (40, 30)}   # boys and girls
fic, non = sum(books["fic"]), sum(books["non"])
ck("V9.5", (fic + non, F(fic, fic + non) * 100, round(100 * fic / (fic + non))), (220, F(150 * 100, 220), 68))
# four people finish order: unique
names = "ABCD"
def ordering_ok(o):
    pos = {n: i for i, n in enumerate(o)}
    return pos["A"] not in (0, 3) and pos["D"] == pos["A"] + 1 and pos["B"] < pos["C"] and pos["C"] != 3
sol = ["".join(o) for o in itertools.permutations(names) if ordering_ok(o)]
ck("V9.6", sol, ["BCAD"])

# ---------------- Lesson 10 Term 1 Review
sol = [(b, 4 * b) for b in range(1, 1000) if 4 * b - 36 == 2 * (b + 36)]
ck("V10.1", sol, [(54, 216)])
ck("V10.2", F(24 + 18) / F(3, 5), 70)
block = [3, 1, 4, 1, 5]
seq117 = [block[i % 5] for i in range(117)]
ck("V10.3", (seq117[-1], sum(seq117)), (1, 326))
# four runners P, Q, R, S : exactly one order
def cond(o):
    pos = {n: i for i, n in enumerate(o)}
    return pos["P"] < pos["Q"] and pos["R"] == pos["S"] - 1 and pos["Q"] < pos["S"] and pos["P"] != 0
sol = ["".join(o) for o in itertools.permutations("PQRS") if cond(o)]
# define puzzle: S is not first; P finishes ahead of Q; R finishes directly behind P; Q is not last
def cond2(o):
    pos = {n: i for i, n in enumerate(o)}
    return pos["S"] != 0 and pos["P"] < pos["Q"] and pos["R"] == pos["P"] + 1 and pos["Q"] != 3
sol = ["".join(o) for o in itertools.permutations("PQRS") if cond2(o)]
ck("V10.4", sol, ["PRQS"])
# Beyond "Exactly One": number puzzle with unique answer
nums = [n for n in range(10, 100) if digsum(n) == 12 and n % 4 == 1 and n // 10 < n % 10]
ck("V10.5", nums, [57])

# ======================================================================
# Term 2 (lessons 11 to 20)
# ======================================================================
import itertools, math
from fractions import Fraction as F

# ---------------- Lesson 11 Solid Views and Dice
# fold the 1-4-1 cross net by rolling a cube over it; opposite faces must add to 7
net = {(0, 1): 3, (1, 0): 1, (1, 1): 2, (1, 2): 6, (1, 3): 5, (2, 1): 4}   # (row, col): number printed
def roll(state, d):
    t, b, n, s, e, w = state
    if d == (0, 1):   return (w, e, n, s, t, b)   # roll east
    if d == (0, -1):  return (e, w, n, s, b, t)   # roll west
    if d == (1, 0):   return (n, s, b, t, e, w)   # roll south
    if d == (-1, 0):  return (s, n, t, b, e, w)   # roll north
start = (1, 0, 2, 3, 4, 5)  # physical faces named 0..5 (top, bottom, north, south, east, west)
cell0 = (1, 1)
seen = {cell0: start}; todo = [cell0]
while todo:
    c = todo.pop()
    for d in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        nc = (c[0] + d[0], c[1] + d[1])
        if nc in net and nc not in seen:
            seen[nc] = roll(seen[c], d); todo.append(nc)
label = {seen[c][1]: net[c] for c in net}      # bottom face id -> printed number
opp = {}
for c in net:
    st = seen[c]; opp[net[c]] = label.get(st[0])  # top face id is opposite to bottom face id
ck("V11.1", (len(label), all(opp[k] is not None and k + opp[k] == 7 for k in opp)), (6, True))
# all 24 orientations of a die: the four side faces add to 14
def rotations(die):
    out = {die}; frontier = [die]
    while frontier:
        d_ = frontier.pop()
        for dd in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            r = roll(d_, dd)
            if r not in out: out.add(r); frontier.append(r)
        # quarter turn about the vertical axis
        t, b, n, s, e, w = d_
        q = (t, b, e, w, s, n)
        if q not in out: out.add(q); frontier.append(q)
    return out
die = (1, 6, 2, 5, 3, 4)   # top, bottom, north, south, east, west (opposites add to 7)
rots = rotations(die)
ck("V11.2", (len(rots), {sum(r[2:]) for r in rots}, 4 * 14 + 5), (24, {14}, 61))
# row of three dice, touching faces add to 8, left end 2
sol = []
for L1 in range(1, 7):
    R1 = 7 - L1; L2 = 8 - R1; R2 = 7 - L2; L3 = 8 - R2; R3 = 7 - L3
    if L1 == 2 and 1 <= L2 <= 6 and 1 <= L3 <= 6: sol.append((L1, R1, L2, R2, L3, R3))
ck("V11.3", sol, [(2, 5, 3, 4, 4, 3)])
# painted cubes: 5 x 5 x 5, top and front painted
cnt = {0: 0, 1: 0, 2: 0}
for x in range(5):
    for y in range(5):
        for z in range(5):
            k = (z == 4) + (y == 0)
            cnt[k] += 1
ck("V11.4", cnt, {0: 80, 1: 40, 2: 5})
top = [[2, 0, 1], [3, 1, 0], [1, 2, 2]]
colmax = [max(top[r][c] for r in range(3)) for c in range(3)]
rowmax = [max(top[r]) for r in range(3)]
ck("V11.5", (sum(map(sum, top)), colmax, rowmax), (12, [3, 2, 2], [2, 3, 2]))
# Hidden Cubes: front view column maxima [3,1,2], side view row maxima [2,3,1]
fm = [3, 1, 2]; sm = [2, 3, 1]
tots = []
for g in itertools.product(range(4), repeat=9):
    grid_ = [g[0:3], g[3:6], g[6:9]]
    if [max(grid_[r][c] for r in range(3)) for c in range(3)] == fm and [max(grid_[r]) for r in range(3)] == sm:
        tots.append(sum(g))
ck("V11.6", (min(tots), max(tots)), (6, 14))

# ---------------- Lesson 12 Boxes and Bricks
trip = sorted({tuple(sorted((a, b, 72 // (a * b)))) for a in range(1, 73) for b in range(1, 73) if 72 % (a * b) == 0})
sa = {t: 2 * (t[0] * t[1] + t[0] * t[2] + t[1] * t[2]) for t in trip}
best = min(sa.values())
ck("V12.1", (len(trip), best, [t for t in trip if sa[t] == best]), (12, 108, [(3, 4, 6)]))
ck("V12.2", (25 // 3) * (17 // 3) * (13 // 3), 160)
ck("V12.3", (4 * 3 * 2, 4 * 3 * 2 // 1, 2 * (4 * 3 + 4 * 2 + 3 * 2)), (24, 24, 52))

# ---------------- Lesson 13 Tank Tales
def stepped_depth(vol_cm3, W=60, D=20, step_w=30, step_h=12):
    base_free = (W - step_w) * D
    if vol_cm3 <= base_free * step_h: return F(vol_cm3, base_free)
    return step_h + F(vol_cm3 - base_free * step_h, W * D)
ck("V13.1", (stepped_depth(9000), stepped_depth(5000), stepped_depth(7200)), (F(27, 2), F(25, 3), 12))
ck("V13.2", F(7, 2) / (F(4, 5) - F(3, 10)), 7)
water = 36 * 25 * 9
up = F(water, 36 * 25 - 10 * 9)            # upright block, base 10 x 9
laid_h = F(water + 10 * 18 * 9, 36 * 25)    # lying on the 10 x 18 face (9 high): rise to cover it
ck("V13.3", (water, up, up < 18, laid_h, laid_h >= 9), (8100, 10, True, F(54, 5), True))

# ---------------- Lesson 14 Decimal Measures
ck("V14.1", (F("3.45") * 100, 3 * 1000 + 450 - 3450 == 0, F("2.075") * 1000, F("4.06") * 1000 - 4000), (345, True, 2075, 60))
lo = 5 * F("1.35"); hi = 5 * F("1.45")
ck("V14.2", (lo, hi), (F("6.75"), F("7.25")))
ck("V14.3", (F("2.4") * F("6.50") + F("0.75") * F("12.80")), F("25.20"))

# ---------------- Lesson 15 Cut and Rearrange
ck("V15.1", [64 // 2 ** k for k in range(5)], [64, 32, 16, 8, 4])
ck("V15.2", (9 * 5, F(1, 2) * 9 * 5, F(1, 2) * (7 + 11) * 4), (45, F(45, 2), 36))
# folded corner: rectangle 12 x 8, corner C(12,8) folded onto P(8,0)
C = F(12), F(8); P = F(8), F(0)
mid = ((C[0] + P[0]) / 2, (C[1] + P[1]) / 2); nx, ny = C[0] - P[0], C[1] - P[1]
def refl(pt):
    d = ((pt[0] - mid[0]) * nx + (pt[1] - mid[1]) * ny) / (nx * nx + ny * ny)
    return pt[0] - 2 * d * nx, pt[1] - 2 * d * ny
E = (F(12), F(3)); G = (F(2), F(8))
on_line = lambda pt: (pt[0] - mid[0]) * nx + (pt[1] - mid[1]) * ny == 0
flap = shoelace([C, E, G])
ck("V15.3", (on_line(E), on_line(G), refl(C) == P, flap, 96 - flap, all(0 <= q[0] <= 12 and 0 <= q[1] <= 8 for q in (refl(C), E, G))), (True, True, True, 25, 71, True))

# ---------------- Lesson 16 Rate and Working Together
ab, bc, ac = F(1, 12), F(1, 15), F(1, 20)   # pair rates: A+B, B+C, A+C ... pairs given in days 12, 15, 20
allt = (ab + bc + ac) / 2
A_ = allt - bc; B_ = allt - ac; C_ = allt - ab
ck("V16.1", (1 / allt, 1 / A_, 1 / B_, 1 / C_), (10, 30, 20, 60))
def postage(g, first=F("0.60"), step=F("0.25")):
    return first if g <= 50 else first + step * math.ceil(F(g - 50, 50))
ck("V16.2", (postage(235), max(g for g in range(1, 1000) if postage(g) <= F("2.10"))), (F("1.60"), 350))
ck("V16.3", (F(168, 12 - 5)), 24)

# ---------------- Lesson 17 Fair Shares
ck("V17.1", (7 * 76 - 6 * 74), 88)
ck("V17.2", (F(12 * 15 + 8 * 20, 20)), 17)
ck("V17.3", (5 * 52 - (48 + 57 + 45 + 60)), 50)
ck("V17.4", (F(sum([4, 9, 5, 6, 6]), 5), sorted([4, 9, 5, 6, 6])[2]), (F(6), 6))

# ---------------- Lesson 18 Graph Stories
tank = [60, 48, 36, 36, 14]
drops = [tank[i] - tank[i + 1] for i in range(4)]
ck("V18.1", (drops, drops.index(max(drops))), ([12, 12, 0, 22], 3))
ck("V18.2", (F(22, 1), 36 / 12), (22, 3))

# ---------------- Lesson 19 Isometric Builders
ck("V19.1", (4 * 3 + 4 * 2 + 3 * 2, 5 * 3 + 5 * 2 + 3 * 2), (26, 31))
H = [[2, 0, 1], [1, 3, 0], [0, 1, 2]]
colm = [max(H[r][c] for r in range(3)) for c in range(3)]
cells = [(r, c) for r in range(3) for c in range(3) if H[r][c] > 0]
best = 0
for add in itertools.product(range(4), repeat=len(cells)):
    G = [row[:] for row in H]
    for (r, c), a in zip(cells, add): G[r][c] += a
    if [max(G[r][c] for r in range(3)) for c in range(3)] == colm and all((G[r][c] > 0) == (H[r][c] > 0) for r in range(3) for c in range(3)):
        best = max(best, sum(map(sum, G)) - sum(map(sum, H)))
ck("V19.2", best, 4)
ck("V19.3", (27 - (3 + 3 + 3 + 3 + 1 + 1 + 3 + 1 + 1)), 8)

# ======================================================================
# Term 3 (lessons 21 to 30)
# ======================================================================
import itertools, math, random
from fractions import Fraction as F
from functools import lru_cache

# ---------------- Lesson 21 Percent Sense
ck("V21.1", (F(35, 100) * 18, [n for n in range(1, 101) if (F(35, 100) * n).denominator == 1][:5]), (F(63, 10), [20, 40, 60, 80, 100]))
ck("V21.2", (F(20, 100) * F(50, 100) * 240, F(20, 100) * F(50, 100)), (24, F(1, 10)))
vals = {"37%": F(37, 100), "3/8": F(3, 8), "0.38": F(38, 100), "2/5": F(2, 5)}
ck("V21.3", sorted(vals, key=vals.get), ["37%", "3/8", "0.38", "2/5"])
items = {"A": 24, "B": 60, "C": 36, "D": 30}
ck("V21.4", ([k for k, v in items.items() if F(v, sum(items.values())) == F(40, 100)], sum(items.values())), (["B"], 150))
ck("V21.5", (F(7, 20) * 100, F(3, 8) * 100, F(9, 25) * 100), (35, F(75, 2), 36))

# ---------------- Lesson 22 Shop Smart
ck("V22.1", (F(80) * F(11, 10) * F(109, 100), F(80) * F(11, 10), F(80) * F(109, 100) * F(11, 10)), (F("95.92"), F(88), F("95.92")))
ck("V22.2", (F(360) * F(75, 100) * F(109, 100), F(360) * F(109, 100) * F(75, 100)), (F("294.30"), F("294.30")))
def free_every(n, price, k):
    # buy m items, every k-th is free (so pay m - m//k); need at least n items; least cost
    return min((m - m // k) * price for m in range(n, n + 2 * k))
ck("V22.3", (free_every(27, F("2.40"), 5), free_every(30, F("2.40"), 5)), (F("52.80"), F("57.60")))
def mincost(n, items):
    INF = 10 ** 9; best = [INF] * (n + 40); best[0] = 0
    for k in range(1, n + 40):
        for (sz, c) in items:
            if k >= sz and best[k - sz] + c < best[k]: best[k] = best[k - sz] + c
    return min(best[n:n + 40])
ck("V22.4", mincost(23, [(1, F("3.5")), (4, F(12)), (10, F(27))]), F("64.5"))
ck("V22.5", (F("54.50") / F("1.09"), F("54.50") - F("54.50") / F("1.09")), (F(50), F("4.50")))

# ---------------- Lesson 23 One Number as a Percent of Another
ck("V23.1", (F(18, 24) * 100, round(41 / 60 * 100), F(36, 80) * 100), (75, 68, F(45)))
ck("V23.2", (F(20 * 2 + 40 * 3, 100) / 5 * 100, (F(2) * F(20, 100) + F(3) * F(40, 100)) / 5), (32, F(8, 25)))
tots = [n for n in range(1, 201) if (F(52, 100) * n).denominator == 1]
ck("V23.3", (tots[:4], {(52 * n // 100) % 2 for n in tots}, 52 in tots), ([25, 50, 75, 100], {0, 1}, False))
ck("V23.4", (F(250) * F(60, 100) , F(250) * F(60, 100) * F(30, 100)), (150, 45))

# ---------------- Lesson 24 Unequal Parts
sol = [(r, c) for r in range(1, 100) for c in range(1, 100) if c == r + 7 and 3 * c + 2 * r == 76]
ck("V24.1", sol, [(11, 18)])
sol = [(a, b) for a in range(1, 300) for b in range(1, 300) if 9 * a == 5 * b and b - 14 == a + 14]
# Ali : Ben = 5 : 9, Ben gives Ali 14 and they are equal  (Ali 35, Ben 63)
sol = [(a, b) for a in range(1, 300) for b in range(1, 300) if 9 * a == 5 * b and b - 14 == a + 14]
ck("V24.2", (sol, sum(sol[0])), ([(35, 63)], 98))
# pens : pencils = 3 : 4 and pencils : rubbers = 6 : 5  ->  pens : pencils : rubbers
lcm = 4 * 6 // math.gcd(4, 6)
pens, pencils, rubbers = 3 * lcm // 4, lcm, 5 * lcm // 6
ck("V24.3", (pens, pencils, rubbers), (9, 12, 10))
unit = F(18, pencils - rubbers)
ck("V24.4", (unit, unit * (pens + pencils + rubbers)), (9, 279))
sol = [x for x in range(0, 50) if 33 + x == 4 * (6 + x)]
ck("V24.5", sol, [3])
sol = [x for x in range(0, 50) if 35 + x == 3 * (7 + x)]
ck("V24.6", sol, [7])

# ---------------- Lesson 25 Balance and Undo
@lru_cache(None)
def weighings(n):
    if n <= 1: return 0
    return 1 + min(max(weighings(a), weighings(n - 2 * a)) for a in range(1, n // 2 + 1))
ck("V25.1", (weighings(9), weighings(27), weighings(10), weighings(3), weighings(4)), (2, 3, 3, 1, 2))
# simulate the 9-coin strategy against every possible heavy coin
def find_heavy(heavy):
    cnt = 0
    def weigh(L, Rr):
        nonlocal cnt; cnt += 1
        wl = sum(1 for c in L if c == heavy); wr = sum(1 for c in Rr if c == heavy)
        return 0 if wl == wr else (-1 if wl > wr else 1)
    cands = list(range(9))
    for _ in range(2):
        k = len(cands) // 3
        a, b, c = cands[:k], cands[k:2 * k], cands[2 * k:]
        r = weigh(a, b)
        cands = a if r == -1 else (b if r == 1 else c)
    return cands, cnt
ck("V25.2", all(find_heavy(h) == ([h], 2) for h in range(9)), True)
ck("V25.3", ([x for x in range(1, 60) if 3 * x + 7 == 28], [x for x in range(1, 60) if 5 * x - 9 == 26], (36 - 8) / 4), ([7], [7], 7.0))
# backwards: gave 2/5 and 3 more, then 1/3 of the rest and 2 more, 8 left
sol = [x for x in range(1, 500) if x % 5 == 0 and (lambda a: a % 3 == 0 and a - (a // 3 + 2) == 8)(x - (2 * x // 5 + 3))]
ck("V25.4", sol, [30])

# ---------------- Lesson 26 Number Stories
s = [2]
g = 3
while len(s) < 8:          # gaps 3, 6, 9, 12, ... (the gaps of the gaps are all 3)
    s.append(s[-1] + g); g += 3
ck("V26.1", s, [2, 5, 11, 20, 32, 47, 65, 86])
w = [3 + 4 * (i // 2) if i % 2 == 0 else 40 - 5 * (i // 2) for i in range(20)]
ck("V26.2", (w[:6], w[12], sum(w[:10])), ([3, 40, 7, 35, 11, 30], 27, 205))
ck("V26.3", (min(n for n in range(1, 100) if n * (n + 1) // 2 > 300), 24 * 25 // 2), (25, 300))
# Not Always Doubling: chords joining n points on a circle, count regions by Euler's formula using geometric crossing tests
def seg_intersect(p1, p2, p3, p4):
    d = (p2[0] - p1[0]) * (p4[1] - p3[1]) - (p2[1] - p1[1]) * (p4[0] - p3[0])
    if abs(d) < 1e-12: return None
    t = ((p3[0] - p1[0]) * (p4[1] - p3[1]) - (p3[1] - p1[1]) * (p4[0] - p3[0])) / d
    u = ((p3[0] - p1[0]) * (p2[1] - p1[1]) - (p3[1] - p1[1]) * (p2[0] - p1[0])) / d
    if 1e-9 < t < 1 - 1e-9 and 1e-9 < u < 1 - 1e-9: return (p1[0] + t * (p2[0] - p1[0]), p1[1] + t * (p2[1] - p1[1]))
    return None
def regions(n, seed=3):
    rnd = random.Random(seed)
    ang = sorted(rnd.uniform(0, 2 * math.pi) for _ in range(n))
    P = [(math.cos(a), math.sin(a)) for a in ang]
    chords = [(i, j) for i in range(n) for j in range(i + 1, n)]   # every pair of points is joined
    cross = []
    for (a, b), (c, d) in itertools.combinations(chords, 2):
        if len({a, b, c, d}) < 4: continue
        pt = seg_intersect(P[a], P[b], P[c], P[d])
        if pt: cross.append(pt)
    X = len(cross)
    V = n + X
    E = n + len(chords) + 2 * X   # arcs on the circle (n), chords cut into pieces (chords + 2X more)
    return E - V + 1 if n > 1 else 1
ck("V26.4", [1 if n == 1 else (2 if n == 2 else regions(n)) for n in range(1, 8)], [1, 2, 4, 8, 16, 31, 57])
# a rule found from three examples is not unique
f1 = lambda n: n * n + 1
f2 = lambda n: n * n + 1 + (n - 2) * (n - 3) * (n - 4)
ck("V26.5", ([f1(n) for n in (2, 3, 4)], [f2(n) for n in (2, 3, 4)], f1(5), f2(5)), ([5, 10, 17], [5, 10, 17], 26, 32))

# ---------------- Lesson 27 Count Without Counting
ck("V27.1", (45 // 5 + 1, 45 // 5, 40 // 8 + 1), (10, 9, 6))
def rays_transversals(rays, trans):
    # triples of lines forming a triangle: two rays and one transversal (transversals are parallel)
    return trans * math.comb(rays, 2)
ck("V27.2", (rays_transversals(5, 1), rays_transversals(5, 2), rays_transversals(6, 2)), (10, 20, 30))
ck("V27.3", (math.comb(9, 2), len([p for p in itertools.permutations(range(4)) if abs(p.index(0) - p.index(1)) != 1])), (36, 12))
def digits_to(N): return sum(len(str(k)) for k in range(1, N + 1))
ck("V27.4", (digits_to(130), min(N for N in range(1, 400) if digits_to(N) == 282), digits_to(99)), (282, 130, 189))
ck("V27.5", len([n for n in range(2000, 4000) if len(set(str(n))) == 4]), 1008)

# ---------------- Lesson 28 Supposition Studio
sol = [a for a in range(0, 41) if 12 * a + 7 * (40 - a) == 395]
ck("V28.1", sol, [23])
sol = [(c, c * 6 + 14) for c in range(1, 200) if 6 * c + 14 == 8 * c - 10]
ck("V28.2", sol, [(12, 86)])
def unreachable(sizes, lim=400):
    ok = [False] * (lim + 1); ok[0] = True
    for n in range(1, lim + 1): ok[n] = any(n >= s and ok[n - s] for s in sizes)
    return [n for n in range(1, lim + 1) if not ok[n]]
u2 = unreachable((5, 8)); u3 = unreachable((7, 10, 12))
ck("V28.3", (max(u2), len(u2), max(u3), len(u3)), (27, 14, 25, 15))
ck("V28.4", len([(a, b, c) for a in range(13) for b in range(7) for c in range(3) if 10 * a + 20 * b + 50 * c == 120]), 13)

# ---------------- Lesson 29 Money Grows
ck("V29.1", (F(2000) * F(3, 100) * 4, F(5000) * F(4, 100) * 3, F(5000) * F(103, 100) ** 3 - 5000), (240, 600, F("463.6350")))
ck("V29.2", (F(1000) * F(105, 100) ** 3 - 1000), F("157.625"))
ck("V29.3", (84 // 3, 84 // (F(3) * F(14, 10)), F(3) * F(14, 10)), (28, 20, F("4.2")))
ck("V29.4", (F(100, 8), [(1 + t * F(8, 100)) for t in (F(25, 2),)]), (F(25, 2), [2]))
ck("V29.5", ([n for n in range(0, 60, 3) if n == 10], [n for n in range(0, 40, 3)][:4]), ([], [0, 3, 6, 9]))

# ---------------- Lesson 30 Quest gates (Term 3) -- defined with the Quest section

# ======================================================================
# Term 4 (lessons 31 to 40)
# ======================================================================
import itertools, math, random, datetime
from fractions import Fraction as F
from functools import lru_cache

# ---------------- Lesson 31 Angles in Shapes
ck("V31.1", ([(n - 2) * 180 for n in (3, 4, 5, 6, 8)], [F((n - 2) * 180, n) for n in (5, 6, 8, 9, 12)]), ([180, 360, 540, 720, 1080], [108, 120, 135, 140, 150]))
ck("V31.2", ([n for n in range(3, 61) if F((n - 2) * 180, n) == 140], [n for n in range(3, 61) if F(360, n) == 24]), ([9], [15]))
def regular(n): return [(math.cos(2 * math.pi * k / n), math.sin(2 * math.pi * k / n)) for k in range(n)]
def ang(a, b, c):
    v1 = (a[0] - b[0], a[1] - b[1]); v2 = (c[0] - b[0], c[1] - b[1])
    return math.degrees(math.acos((v1[0] * v2[0] + v1[1] * v2[1]) / (math.hypot(*v1) * math.hypot(*v2))))
P5 = regular(5)   # A B C D E
ck("V31.3", (round(ang(P5[1], P5[0], P5[2]), 6), round(ang(P5[2], P5[0], P5[3]), 6), round(ang(P5[4], P5[0], P5[1]), 6)), (36.0, 36.0, 108.0))
# exterior angles of random convex polygons add to 360 (turn at each corner)
random.seed(2)
def exterior_sum(pts):
    n = len(pts); tot = 0
    for i in range(n):
        a, b, c = pts[i - 1], pts[i], pts[(i + 1) % n]
        v1 = (b[0] - a[0], b[1] - a[1]); v2 = (c[0] - b[0], c[1] - b[1])
        cr = v1[0] * v2[1] - v1[1] * v2[0]; dt = v1[0] * v2[0] + v1[1] * v2[1]
        tot += math.degrees(math.atan2(cr, dt))
    return tot
ok = True
for _ in range(100):
    n = random.randint(3, 9)
    angs = sorted(random.uniform(0, 2 * math.pi) for _ in range(n))
    pts = [(math.cos(t), math.sin(t)) for t in angs]
    if abs(abs(exterior_sum(pts)) - 360) > 1e-6: ok = False
ck("V31.4", ok, True)

# ---------------- Lesson 32 Triangles and Quadrilaterals
def diag_info(p):
    A, B, C, D = p
    d1 = (C[0] - A[0], C[1] - A[1]); d2 = (D[0] - B[0], D[1] - B[1])
    eq = d1[0] ** 2 + d1[1] ** 2 == d2[0] ** 2 + d2[1] ** 2
    perp = d1[0] * d2[0] + d1[1] * d2[1] == 0
    mid_ac = (F(A[0] + C[0], 2), F(A[1] + C[1], 2)); mid_bd = (F(B[0] + D[0], 2), F(B[1] + D[1], 2))
    return eq, perp, mid_ac == mid_bd
shapes = {
    "square": [(0, 0), (4, 0), (4, 4), (0, 4)],
    "rectangle": [(0, 0), (6, 0), (6, 4), (0, 4)],
    "rhombus": [(0, 0), (5, 0), (8, 4), (3, 4)],
    "parallelogram": [(0, 0), (6, 0), (8, 3), (2, 3)],
    "kite": [(0, 0), (2, 1), (0, 5), (-2, 1)],
}
info = {k: diag_info(v) for k, v in shapes.items()}
ck("V32.1", info, {"square": (True, True, True), "rectangle": (True, False, True), "rhombus": (False, True, True), "parallelogram": (False, False, True), "kite": (False, True, False)})
# always / sometimes / never: "a rhombus has equal diagonals" -> only when it is a square
sq = diag_info(shapes["square"])[0]; rh = diag_info(shapes["rhombus"])[0]
ck("V32.2", (sq, rh), (True, False))
# trapezium ABCD with AB parallel to DC: angles on the same leg add to 180
ck("V32.3", (180 - 72, 180 - 115, 72 + 115 + (180 - 72) + (180 - 115)), (108, 65, 360))

# ---------------- Lesson 33 Clocks and Calendars
def hand_angle(h, m):
    a = abs((h % 12) * 30 + F(m) / 2 - F(m) * 6) % 360
    return min(a, 360 - a)
ck("V33.1", (hand_angle(7, 20), hand_angle(4, 10), hand_angle(9, 15)), (100, 65, F(345, 2)))
# first time after 3:00 when the hands coincide: hour hand 90 + 0.5t, minute hand 6t
t = F(90, F(11, 2))
ck("V33.2", (t, t.numerator // t.denominator, F(t - 16) * 60), (F(180, 11), 16, F(240, 11)))
# count coincidences and right angles in 12 hours, from 12:00 (inclusive) to 12:00 (exclusive)
coin = sorted({F(720 * k, 11) for k in range(0, 11)})
rt = sorted({F(720 * k + 180, 11) for k in range(0, 11)} | {F(720 * k + 540, 11) for k in range(0, 11)})
ck("V33.3", (len([x for x in coin if x < 720]), len([x for x in rt if x < 720])), (11, 22))
d0 = datetime.date(2026, 10, 6)
ck("V33.4", (d0.strftime("%A"), (d0 + datetime.timedelta(days=150)).strftime("%A"), 150 % 7, d0.replace(year=2027, month=1, day=5).strftime("%A")), ("Tuesday", "Friday", 3, "Tuesday"))
ck("V33.5", (14 * 60 + 10 - (3 * 60 + 45), divmod(14 * 60 + 10 - (3 * 60 + 45), 60)), (625, (10, 25)))
# a year of 365 days has one weekday 53 times (the weekday it starts on)
d1 = datetime.date(2027, 1, 1)
cnt = {}
for k in range(365):
    wd = (d1 + datetime.timedelta(days=k)).strftime("%A"); cnt[wd] = cnt.get(wd, 0) + 1
ck("V33.6", (max(cnt, key=cnt.get), max(cnt.values()), sorted(cnt.values())[0]), (d1.strftime("%A"), 53, 52))

# ---------------- Lesson 34 Logic Grids and Digit Puzzles
# five runners; clues: V is neither first nor last; W finished directly after V; X is ahead of V; Y is ahead of X; Z is behind W
def run5c(o):
    pos = {n: i for i, n in enumerate(o)}
    return pos["V"] not in (0, 4) and pos["W"] == pos["V"] + 1 and pos["X"] < pos["V"] and pos["Y"] < pos["X"] and pos["Z"] > pos["W"]
sol = ["".join(o) for o in itertools.permutations("VWXYZ") if run5c(o)]
ck("V34.1", sol, ["YXVWZ"])
# exactly one liar among four. Ana: "Ben is lying." Ben: "Cara and Dev both tell the truth." Cara: "Ana is lying." Dev: "Ben and Cara both tell the truth."
def statements(t):
    A, B, C, D = t   # True = tells the truth
    return (A == (not B), B == (C and D), C == (not A), D == (B and C))
sol = [t for t in itertools.product([True, False], repeat=4) if sum(1 for x in t if not x) == 1 and all(statements(t))]
ck("V34.2", sol, [(False, True, True, True)])
# without the "exactly one liar" rule the clues do not fix the answer
free = [t for t in itertools.product([True, False], repeat=4) if all(statements(t))]
ck("V34.2b", len(free) > 1, True)
def crypt(words, result, limit=3):
    letters = sorted(set("".join(words) + result)); n = len(letters); idx = {c: i for i, c in enumerate(letters)}
    cw = [[idx[c] for c in w] for w in words + [result]]; out = []
    for p in itertools.permutations(range(10), n):
        if any(p[w[0]] == 0 for w in cw): continue
        vals = []
        for w in cw:
            v = 0
            for i in w: v = v * 10 + p[i]
            vals.append(v)
        if sum(vals[:-1]) == vals[-1]:
            out.append(dict(zip(letters, p)))
            if len(out) >= limit: break
    return out
s1 = crypt(["ABC", "BBB"], "DCCE")
ck("V34.3", (len(s1), s1[0]), (1, {"A": 5, "B": 6, "C": 2, "D": 1, "E": 8}))
s2 = crypt(["ABACD", "CAEF"], "CFFCC")
ck("V34.4", (len(s2), s2[0]), (1, {"A": 6, "B": 4, "C": 7, "D": 5, "E": 0, "F": 2}))

# ---------------- Lesson 35 Odd, Even, Remainders and Extremes
# twelve numbers, five odd and seven even: the total is odd, whichever numbers they are
import random as _r
_r.seed(4)
tot_par = {sum([_r.randrange(1, 100, 2) for _ in range(5)] + [_r.randrange(2, 100, 2) for _ in range(7)]) % 2 for _ in range(500)}
ck("V35.1", tot_par, {1})
n_ok = [n for n in range(9, 400) if 200 % n == 8]
ck("V35.2", (n_ok, sum(n_ok)), ([12, 16, 24, 32, 48, 64, 96, 192], 484))
ck("V35.3", ((3 ** 15 * 7 ** 10) % 10, [7 ** k % 10 for k in range(1, 9)]), (3, [7, 9, 3, 1, 7, 9, 3, 1]))
# worst case: how many to draw to be sure of k of one suit (4 suits) or a pair among c colours
def worst(suits, k):
    # largest draw with no suit reaching k, plus one
    return suits * (k - 1) + 1
best = 0
for dist in itertools.product(range(3), repeat=4):    # at most 2 of each suit
    best = max(best, sum(dist))
ck("V35.4", (worst(4, 3), best + 1, worst(5, 2)), (9, 9, 6))
# 40 sweets among 6 children, all different and at least 1: least possible biggest share
def parts(total, k, minv=1):
    if k == 1:
        if total >= minv: yield (total,)
        return
    for a in range(minv, total):
        for rest in parts(total - a, k - 1, a + 1): yield (a,) + rest
mins = min(max(p) for p in parts(40, 6))
ck("V35.5", mins, 10)
# no number is a multiple of another: biggest set from 1..20
best = 0
nums = list(range(1, 21))
def search(i, chosen):
    global best
    if len(chosen) + (20 - i + 1) <= best: return
    if i > 20:
        best = max(best, len(chosen)); return
    if all(i % c for c in chosen):
        search(i + 1, chosen + [i])
    search(i + 1, chosen)
search(1, [])
ck("V35.6", best, 10)
# eight different numbers from 1..14, product of any four is even, sum is even: least sum
bestsum = None
for S in itertools.combinations(range(1, 15), 8):
    odd = sum(1 for x in S if x % 2)
    if all(any(x % 2 == 0 for x in q) for q in itertools.combinations(S, 4)) and sum(S) % 2 == 0:
        if bestsum is None or sum(S) < bestsum[0]: bestsum = (sum(S), S)
ck("V35.7", bestsum, (46, (1, 2, 3, 4, 6, 8, 10, 12)))

# ---------------- Lesson 36 Working Backwards
a, b, c = 13, 7, 4
a, b, c = a - b - c, 2 * b, 2 * c
b, a, c = b - a - c, 2 * a, 2 * c
c, a, b = c - a - b, 2 * a, 2 * b
ck("V36.1", (a, b, c), (8, 8, 8))
def swap_round(state, giver):
    # the giver hands each of the other two children enough money to double what that child has
    st = list(state)
    for j in range(3):
        if j != giver:
            st[giver] -= st[j]; st[j] *= 2
    return tuple(st)
sol = []
for a0 in range(1, 24):
    for b0 in range(1, 24):
        c0 = 24 - a0 - b0
        if c0 < 1: continue
        st = (a0, b0, c0)
        ok_ = True
        for giver in (0, 1, 2):
            st = swap_round(st, giver)
            if min(st) < 0: ok_ = False; break
        if ok_ and st == (8, 8, 8): sol.append((a0, b0, c0))
ck("V36.2", sol, [(13, 7, 4)])
ck("V37.5", (F(450) * F(80, 100) * F(109, 100), F(450) * F(80, 100) * F(109, 100) * F(25, 100), F(450) * F(80, 100) * F(109, 100) * F(75, 100) / 6), (F("392.40"), F("98.10"), F("49.05")))
# Ali gave 1/3 of his money to Ben, then Ben gave 1/4 of his money to Ali; now Ali has 42 and Ben 30
sol = []
for x in range(3, 300, 3):
    for y in range(1, 300):
        a1, b1 = x - x // 3, y + x // 3
        if b1 % 4: continue
        a2, b2 = a1 + b1 // 4, b1 - b1 // 4
        if (a2, b2) == (42, 30): sol.append((x, y))
ck("V36.4", sol, [(48, 24)])

# ---------------- Lesson 37 The Long Question
ck("V37.1", (F(60) * F(3, 10), F(60) * F(7, 10), F(60) * F(7, 10) * F(2, 7)), (18, 42, 12))
# four-step unit chain with decimals: Ravi has $4.50 more than Siti; both save $3.60; then Siti has 2/3 of Ravi
sol = [(s_ / 100, (s_ + 450) / 100) for s_ in range(0, 5000) if F(s_ + 360, 1) * 3 == 2 * (s_ + 450 + 360)]
ck("V37.2", sol, [(5.4, 9.9)])
# stepped charge inside a story: $1.50 for the first 30 min then $0.80 per 15 min or part; 2 h 5 min
def park(minutes, first=F("1.50"), step=F("0.80")):
    return first if minutes <= 30 else first + step * math.ceil(F(minutes - 30, 15))
ck("V37.3", (park(125), max(m for m in range(1, 600) if park(m) <= F("8.70"))), (F("1.50") + F("0.80") * 7, 30 + 15 * 9))

# Spare Clue: a rectangle with perimeter 36 cm and length 2 cm more than the width; "area 80 cm2" is a spare clue
sol = [(w, w + 2) for w in range(1, 50) if 2 * (2 * w + 2) == 36]
ck("V37.4", (sol, sol[0][0] * sol[0][1], [w * (w + 2) for w in range(1, 50) if 2 * (2 * w + 2) == 36 and w * (w + 2) == 84]), ([(8, 10)], 80, []))

# ---------------- Lesson 38 Children Set the Problem
cands = [n for n in range(100, 1000) if n % 7 == 0 and digsum(n) == 12 and (n // 10) % 10 == 0]
ck("V38.1", cands, [903])
ck("V38.2", [n for n in range(100, 1000) if digsum(n) == 12 and (n // 10) % 10 == 0], [309, 408, 507, 606, 705, 804, 903])

# ---------------- Lesson 39 Colouring, Cycles and Choices
def colourings(n, edges, k):
    return sum(1 for col in itertools.product(range(k), repeat=n) if all(col[a] != col[b] for a, b in edges))
path6 = [(i, i + 1) for i in range(5)]
cyc5 = [(i, (i + 1) % 5) for i in range(5)]
wheel = cyc5 + [(i, 5) for i in range(5)]
pet = [(i, (i + 1) % 5) for i in range(5)] + [(i, i + 5) for i in range(5)] + [(5 + i, 5 + (i + 2) % 5) for i in range(5)]
ck("V39.1", (colourings(6, path6, 4), colourings(5, cyc5, 3), colourings(5, cyc5, 2), colourings(6, wheel, 3), colourings(6, wheel, 4) > 0), (972, 30, 0, 0, True))
ck("V39.2", (colourings(10, pet, 2), colourings(10, pet, 3), len(pet)), (0, 120, 15))
cycle = ["R", "B", "B", "G"]
ck("V39.3", (cycle[(50 - 1) % 4], sum(1 for i in range(50) if cycle[i % 4] == "B")), ("B", 25))
sq = [(0, 1), (1, 2), (2, 3), (3, 0)]
ck("V39.4", (colourings(4, sq, 3), colourings(4, sq, 2)), (18, 2))

# ======================================================================
# Quest gates, kit contracts, jug search
# ======================================================================
import itertools, math, datetime
from fractions import Fraction as F

# ---------------- Term 1 Quest (lesson 10)
ck("Q1.1", (4250 * 100, 3600000 // 1000), (425000, 3600))
ck("Q1.2", ([d for d in divisors(18) if 30 % d == 0], max(d for d in divisors(18) if 30 % d == 0)), ([1, 2, 3, 6], 6))
ck("Q1.3", 5 + 12 // 4 * 2 - 3, 8)
ck("Q1.4", (F(7, 4) - 1, F(2, 3) * F(3, 5)), (F(3, 4), F(2, 5)))
ck("Q1.5", (float(F(3, 8)), F("4.5") / 1000), (0.375, F("0.0045")))
ck("Q1.6", F(14 * 6, 2), 42)
ck("Q1.7", ((180 - 40) / 2, 180 - 48 - 67), (70.0, 65))
ck("Q1.8", 18 + 15 - (30 - 5), 8)
ck("Q1.9", [n for n in range(41, 60) if n % 7 == 0 and digsum(n) == 11], [56])

# ---------------- Term 2 Quest (lesson 20)
top = [[2, 1], [3, 1]]
ck("Q2.1", sum(map(sum, top)), 7)
ck("Q2.2", 5 * 4 * 3, 60)
ck("Q2.3", (40 * 25 * 6, 40 * 25 * 6 // 1000), (6000, 6))
ck("Q2.4", (F(3250, 1000) + F("1.9"), divmod(int((F(3250, 1000) + F("1.9")) * 1000), 1000)), (F("5.15"), (5, 150)))
ck("Q2.5", 9 * 5, 45)
ck("Q2.6", (18 * 15, F(270, 18)), (270, 15))
ck("Q2.7", (F(4 + 7 + 9 + 12, 4), 8), (8, 8))
ck("Q2.8", 3 * 2 + 3 * 2 + 2 * 2, 16)
ck("Q2.9", (30 * 20, F(3000, 600), 5 + F(3000, 600)), (600, 5, 10))

# ---------------- Term 3 Quest (lesson 30)
ck("Q3.1", (F(35, 100) * 80, F(40, 100)), (28, F(2, 5)))
ck("Q3.2", (50 * F(8, 10), 50 * F(8, 10) * F(109, 100)), (40, F("43.60")))
ck("Q3.3", F(18, 24) * 100, 75)
ck("Q3.4", [p for p in range(1, 45) if p * 3 == (45 - p) * 2], [18])
ck("Q3.5", [x for x in range(30) if 3 * x + 5 == 29], [8])
ck("Q3.6", 2 + 3 * 19, 59)
ck("Q3.7", (math.comb(9, 2), [x for x in range(11) if 4 * (10 - x) + 6 * x == 48]), (36, [4]))
ck("Q3.8", F(1000) * F(4, 100) * 3, 120)
def cost(n):  # pens $3 each or 3 for $8
    return min(8 * k + 3 * max(0, n - 3 * k) for k in range(0, n // 3 + 2))
ck("Q3.9", (cost(10), cost(9), cost(12)), (27, 24, 32))

# ---------------- Term 4 Quest (lesson 40)
ck("Q4.1", (F((6 - 2) * 180, 6), (6 - 2) * 180), (120, 720))
sq = [(0, 0), (4, 0), (4, 4), (0, 4)]
def sides_equal(p):
    d = [(p[(i + 1) % 4][0] - p[i][0]) ** 2 + (p[(i + 1) % 4][1] - p[i][1]) ** 2 for i in range(4)]
    return len(set(d)) == 1
def diag_equal(p): return (p[2][0] - p[0][0]) ** 2 + (p[2][1] - p[0][1]) ** 2 == (p[3][0] - p[1][0]) ** 2 + (p[3][1] - p[1][1]) ** 2
shapes = {"square": sq, "rhombus": [(0, 0), (5, 0), (8, 4), (3, 4)], "kite": [(0, 0), (2, 1), (0, 5), (-2, 1)], "parallelogram": [(0, 0), (6, 0), (8, 3), (2, 3)]}
ck("Q4.2", [k for k, v in shapes.items() if sides_equal(v) and diag_equal(v)], ["square"])
ck("Q4.3", (abs(4 * 30), (datetime.date(2026, 10, 5) + datetime.timedelta(days=100)).strftime("%A"), datetime.date(2026, 10, 5).strftime("%A")), (120, "Wednesday", "Monday"))
def finish(o):
    pos = {n: i for i, n in enumerate(o)}
    return pos["Mei"] != 0 and pos["Ravi"] == pos["Mei"] + 1 and pos["Kai"] < pos["Mei"]
ck("Q4.4", ["".join(n[0] for n in o) for o in itertools.permutations(["Kai", "Mei", "Ravi"]) if finish(o)], ["KMR"])
ck("Q4.5", [n for n in range(10, 60) if n % 7 == 3 and n % 4 == 1], [17, 45])
ck("Q4.6", [x for x in range(1, 60) if x * 3 - 4 == 20], [8])
ck("Q4.7", F(60) * F(75, 100) * F(109, 100), F("49.05"))
def colourings(n, edges, k):
    return sum(1 for col in itertools.product(range(k), repeat=n) if all(col[a] != col[b] for a, b in edges))
ck("Q4.8", colourings(4, [(0, 1), (1, 2), (2, 3)], 3), 24)
# cave: how many 3-digit numbers have digit sum 5 (unseen puzzle joining two moves)
ck("Q4.9", len([n for n in range(100, 1000) if digsum(n) == 5]), 15)

# ---------------- kit contracts (supplied, maximum used, cut) generated from one table
KITS = [
    # (lesson, kit code, name, supplied, max used by a task, cut, note)
    (1, "KT1", "shift_tiles", "13 tiles (0 x 4, 1 to 9 once each)", "8 tiles (at most 4 zeros, no repeated non-zero digit)", 13, "Mat printed, not cut; no printer: digits on scraps"),
    (4, "KT2", "pizza_circles", "8 circles (11 cm)", "7 circles (7 pizzas shared among 3)", 8, "Fold lines printed; paper plates are the fallback"),
    (8, "KT3", "triangle_cards", "8 triangles, sides marked with ticks, no angle values", "8 cards (sorting)", 8, "Not needed again"),
    (11, "KT4", "dice_nets", "4 nets of a 3 cm die, opposite faces add to 7", "4 dice (a tower of four)", 4, "Tape needed; a board-game die may replace one"),
    (15, "KT5", "dissection_set", "8 paper shapes: 2 parallelograms, 2 trapeziums, 2 triangles, 2 squares", "8 (each cut once or twice in the lesson)", 8, "The child cuts these in the lesson (scissors, D5); the only kit not cut beforehand"),
    (22, "KT6", "shop_cards", "10 cards (item, price, offer)", "8 cards at once", 10, "Reused in lesson 29 warm-up"),
    (24, "KT7", "unit_strips", "6 strips of 12 cells (72 cells)", "38 cells (three bars at once)", 6, "Cut between strips, not between cells"),
    (25, "KT8", "weight_tokens", "12 tokens (shapes of weight 1 to 4 units) and a balance mat (not cut)", "9 tokens", 12, "Shapes differ by outline, not colour"),
    (27, "KT9", "people_cards", "10 people", "9 people (handshakes among 9)", 10, "Fallback: 9 coins or buttons"),
    (28, "KT10", "play_coins", "10c x 12, 20c x 6, 50c x 3 (21 pieces)", "10c x 12, 20c x 6, 50c x 2", 21, "Real coins from a purse are better; stylised, marked PLAY MONEY"),
    (32, "KT11", "shape_cards", "12 cards: square, rectangle, rhombus, parallelogram, trapezium, kite, two of each", "12 (sorting)", 12, "Sides and right angles marked"),
    (33, "KT12", "clock_kit", "2 faces (not cut), 3 hour hands, 3 minute hands", "2 faces, 2 + 2 hands", 6, "Loose hands, no fastener; a real clock helps"),
    (34, "KT13", "clue_cards", "12 cards (8 clue, 4 name)", "12", 12, "4 by 4 logic grids are printed, not cut"),
    (35, "KT14", "draw_cards", "16 cards (4 symbols x 4)", "16 (a draw of up to 9 cards, then all 16 to check the claim)", 16, "A normal pack of playing cards also works"),
]
cut_by_lesson = {k[0]: k[5] for k in KITS}
terms = {t: sum(v for l, v in cut_by_lesson.items() if (l - 1) // 10 + 1 == t) for t in (1, 2, 3, 4)}
books = {b: sum(v for l, v in cut_by_lesson.items() if (l - 1) // 5 + 1 == b) for b in range(1, 9)}
ck("K.1", terms, {1: 29, 2: 12, 3: 59, 4: 46})
ck("K.2", (sum(terms.values()), books), (146, {1: 21, 2: 8, 3: 12, 4: 0, 5: 28, 6: 31, 7: 46, 8: 0}))
# supplied >= max used, checked on the numeric parts
def nums(s): return [int(x) for x in __import__('re').findall(r'\d+', s)]
ck("K.3", (6 * 12 >= 38, 12 >= 9, 21 >= 12 + 6 + 2, 13 >= 8, 8 >= 7, 10 >= 9, 16 >= 9), (True,) * 7)
# play coins: the most any task needs of each coin to make $1.20
ways = [(a, b, c) for a in range(13) for b in range(7) for c in range(3) if 10 * a + 20 * b + 50 * c == 120]
ck("K.5", (max(w[0] for w in ways), max(w[1] for w in ways), max(w[2] for w in ways)), (12, 6, 2))
# 9 people shake hands: using the 10 cards
ck("K.6", (math.comb(9, 2), math.comb(10, 2)), (36, 45))
# Seven and Eleven: fewest steps (fill, empty, pour) to measure exactly 2 L with a 7 L and an 11 L jug
from collections import deque
def jug_steps(a, b, target):
    start = (0, 0); dist = {start: 0}; q = deque([start])
    while q:
        s = q.popleft(); x, y = s
        if x == target or y == target: return dist[s]
        t1 = min(x, b - y); t2 = min(y, a - x)
        for n in [(a, y), (x, b), (0, y), (x, 0), (x - t1, y + t1), (x + t2, y - t2)]:
            if n not in dist: dist[n] = dist[s] + 1; q.append(n)
ck("V20.1", (jug_steps(7, 11, 4), jug_steps(7, 11, 2)), (2, 14))

# ======================================================================
# Items quoted in the specs, Terms 1 and 2
# ======================================================================
import itertools, math
from fractions import Fraction as F

# ---- Lesson 1
ck("V1.7", (7200000 // 300, 7200000 // 24000), (24000, 300))
ck("V1.8", 2500 * 40, 100000)
# ---- Lesson 2
n = 7482
ck("V2.10", (digsum(n), n % 3, n % 9, 12 // 1 and len(divisors(12))), (21, 0, 3, 6))
# ---- Lesson 3
ck("V3.7", (18 + 6 * 5 - 12 // 4, 7 + 3 * (12 - 4), 100 - (35 + 15) // 5, 48 // 6 * 2, 3 * 4 + 2 * 2), (45, 31, 90, 16, 16))
ck("V3.8", F(45 * 36, 15 * 12), 9)
ck("V3.2b", 12 + 18 * 5, 102)
# a worked way to 24 from 3, 4, 6, 9
def make(vals):
    if len(vals) == 1: return [vals[0]]
    res = []
    for i in range(len(vals)):
        for j in range(i + 1, len(vals)):
            rest = [vals[k] for k in range(len(vals)) if k not in (i, j)]
            (x, ex), (y, ey) = vals[i], vals[j]
            cand = [(x + y, f"({ex} + {ey})"), (x * y, f"({ex} x {ey})"), (x - y, f"({ex} - {ey})"), (y - x, f"({ey} - {ex})")]
            if y != 0: cand.append((x / y, f"({ex} / {ey})"))
            if x != 0: cand.append((y / x, f"({ey} / {ex})"))
            for c in cand: res += make(rest + [c])
    return res
sols24 = sorted({e for (v_, e) in make([(F(n_), str(n_)) for n_ in (3, 4, 6, 9)]) if v_ == 24})
SAMPLE24 = next(e for e in sols24 if "/" not in e)
ck("V3.9", all(eval(e.replace("x", "*")) == 24 for e in sols24[:20]), True)
# ---- Lesson 4
ck("V4.7", F(33, 4) - F(17, 6) + F(3, 2), F(83, 12))
# ---- Lesson 5
sol = [(r, b) for b in range(1, 400) for r in range(1, 400) if F(3, 5) * r == F(3, 4) * b and r - b == 18]
ck("V5.6", sol, [(90, 72)])
ck("V5.7", F(4, 6) * F(3, 8), F(1, 4))
ck("V5.8", F(1, 2) * F(1, 3) * F(1, 4) * 240, 10)
# ---- Lesson 7
ck("V7.6", F(2 * 54, 9), 12)
# ---- Lesson 8
# triangle with angles from the AB = BD, AD = DC chain: angles at A, B, C, D
x = 34
ck("V8.7", (180 - 4 * x, 2 * x, 2 * x, 3 * x, (180 - 4 * x) + 2 * x + 2 * x), (44, 68, 68, 102, 180))
ck("V8.8", (90 + 45 + 45, any(a > 90 and b > 90 for a in range(91, 180) for b in range(91, 180) if a + b < 180)), (180, False))
def quad_kind(angles):
    A, B, C, D = angles
    par = []
    if A + B == 180 and C + D == 180: par.append("AD || BC")
    if B + C == 180 and D + A == 180: par.append("AB || DC")
    return "parallelogram" if len(par) == 2 else ("trapezium" if par else "other")
ck("V8.6", (quad_kind((70, 110, 70, 110)), quad_kind((70, 110, 110, 70))), ("parallelogram", "trapezium"))
# ---- Lesson 9
# percentages: 60% like cats, 70% like dogs, everyone likes at least one
ck("V9.7", (60 + 70 - 100, min(60, 70) if False else 60), (30, 60))

# ---- Lesson 11
top = [[2, 0, 1], [3, 1, 0], [1, 2, 2]]
colmax = [max(top[r][c] for r in range(3)) for c in range(3)]
rowmax = [max(top[r]) for r in range(3)]
cap = lambda r, c: min(colmax[c], rowmax[r])
A_ = sum(cap(r, c) for r in range(3) for c in range(3)) - 12
B_ = sum(cap(r, c) - top[r][c] for r in range(3) for c in range(3) if top[r][c] > 0)
# brute force check of both
best_a = best_b = 0
for g in itertools.product(range(4), repeat=9):
    G = [g[0:3], g[3:6], g[6:9]]
    if all(G[r][c] >= top[r][c] for r in range(3) for c in range(3)) and [max(G[r][c] for r in range(3)) for c in range(3)] == colmax and [max(G[r]) for r in range(3)] == rowmax:
        best_a = max(best_a, sum(g) - 12)
        if all((G[r][c] > 0) == (top[r][c] > 0) for r in range(3) for c in range(3)): best_b = max(best_b, sum(g) - 12)
ck("V11.7", (A_, B_, best_a, best_b), (A_, B_, A_, B_))
V117 = (best_a, best_b)
# ---- Lesson 12
ck("V12.4", 12 + F(300, 5 * 4), 27)
ck("V12.5", (6 ** 3 // 2 ** 3, (6 // 2) ** 3), (27, 27))
# ---- Lesson 13
ck("V13.4", (50 * 30, 8 + F(4500, 50 * 30)), (1500, 11))
ck("V13.5", 60 * 40 * 35 // 1000, 84)
# ---- Lesson 14
ck("V14.4", (F("3.6") - F("1.85"), F("1.75") * 1000), (F("1.75"), 1750))
ck("V14.5", (18400 + 21650 + (21650 + 2500)), 64200)
# ---- Lesson 15
ck("V15.4", min(k for k in range(0, 20) if F(64, 2 ** k) < 1), 7)
# ---- Lesson 16
ck("V16.5", (F("8.10") - F("4.20")) / F("0.30"), 13)
ck("V16.5b", (1000 + 13 * 400, F(1000 + 13 * 400, 1000)), (6200, F(31, 5)))
ck("V16.6", (F(1, 8) - F(1, 12), 1 / (F(1, 8) - F(1, 12))), (F(1, 24), 24))
# ---- Lesson 17
ck("V17.5", (F(1 + 1 + 1 + 1 + 16, 5), sorted([1, 1, 1, 1, 16])[2]), (4, 1))
ck("V17.6", [s for s in range(1, 30) if F(s + (s + 1) + (s + 2) + (s + 3) + (s + 4), 5) == 12], [10])
# ---- Lesson 18
ck("V18.3", (36 * (360 // 90), F(36, F(90, 360))), (144, 144))
ck("V18.4", (F(97, 92), F(97 - 90, 92 - 90)), (F(97, 92), F(7, 2)))
# ---- Lesson 20
def least_pay(n, price, every):
    return min((m - m // every) * price for m in range(n, n + 3 * every))
ck("V20.2", (least_pay(31, F("2.50"), 3), 31 - 31 // 3), (F("52.50"), 21))

# ======================================================================
# Items quoted in the specs, Terms 3 and 4
# ======================================================================
import itertools, math
from fractions import Fraction as F

ck("V24.7", (48 // 4, 3 * (48 // 4)), (12, 36))
# three children: A twice B, C is 10 more than B, together 90
sol = [(a, b, c) for b in range(1, 90) for a in [2 * b] for c in [b + 10] if a + b + c == 90]
ck("V24.8", sol, [(40, 20, 30)])
# balance with shapes: 2 squares + 1 circle = 27 and 1 square + 2 circles = 24
sol = [(a, b) for a in range(1, 30) for b in range(1, 30) if 2 * a + b == 27 and a + 2 * b == 24]
ck("V25.5", sol, [(10, 7)])
# Figure n has n*n + 4 dots: 5, 8, 13, 20
ck("V26.6", ([n * n + 4 for n in range(1, 5)], 10 * 10 + 4, [n for n in range(1, 100) if n * n + 4 == 229]), ([5, 8, 13, 20], 104, [15]))
# pencils at $1 and pens at $3: 7 items cost $15
ck("V28.5", [x for x in range(8) if (7 - x) * 1 + 3 * x == 15], [4])
# 6 per bag leaves 9, 8 per bag is 1 short
ck("V28.6", [(b, 6 * b + 9) for b in range(1, 100) if 6 * b + 9 == 8 * b - 1], [(5, 39)])
# two simple-interest plans for $5000: 4% for 3 years or 3% for 5 years
ck("V29.6", (F(5000) * F(4, 100) * 3, F(5000) * F(3, 100) * 5), (600, 750))
# Working backwards through a discount and GST: pay $392.40 after 20% off and 9% GST
ck("V36.5", (F("392.40") / F("1.09") / F("0.8")), F(450))

ck("V21.6", (200 * F(11, 10), 200 * F(11, 10) * F(9, 10)), (220, 198))
ck("V22.8", (3 * 60, 60 + 60 + 30, F(30, 180) * 100), (180, 150, F(50, 3)))
ck("V28.7", (max(unreachable((8, 11, 15))), len(unreachable((8, 11, 15)))), (36, 20))
ck("V30.2", F(90) / (F(60, 100) * F(3, 4)), 200)
ck("V30.3", [c for c in range(21) if 4 * c - 2 * (20 - c) == 56], [16])

# eggs: 30% sold in the morning, 3/7 of the rest in the afternoon, 120 left
ck("V36.6", (F(120) / (F(7, 10) * F(4, 7)), 300 * F(3, 10), (300 - 90) * F(3, 7)), (300, 90, 90))
ck("V31.5", [n for n in range(3, 40) if (n - 2) * 180 == 1260], [9])
ck("V33.7", (6 * 60 + 30 + 24 * 60 - (21 * 60 + 50), F(6 * 60 + 30 + 24 * 60 - (21 * 60 + 50), 60) * 9), (520, 78))

ck("V16.7", (F(1, 6) - F(1, 10), 1 / (F(1, 6) - F(1, 10))), (F(1, 15), 15))

# ---------------------------------------------------------------- summary
ids = [i for i, _ in R]
dup = sorted({i for i in ids if ids.count(i) > 1})
assert not dup, "duplicate check ids: %s" % dup
bad = [i for i, ok in R if not ok]
if bad:
    raise SystemExit("verify_l5_preflight: FAILED %s" % bad)
print("verify_l5_preflight: %d checks, %d passed" % (len(R), len(R)))
```
