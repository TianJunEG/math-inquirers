# Level 4 pre-flight (lessons 1 to 40, four terms, ages 9 to 11, Primary 4)

Status: planning only, written 23 Oct 2026. No lesson, tool, template or output file was edited, built or run (the only things run were scratch verification scripts, section 14). This document tells the people who will write the 40 Level 4 term lessons what each lesson is, which holiday and school-paper items it must not repeat, what the shared templates must learn first, what went wrong at Level 1 and must not be repeated, which decisions the owner must make, and in which order to build. It is modelled on `docs/terms/l1_term2_preflight.md`, `docs/terms/l1_term3_term4_preflight.md` and `docs/terms/l2_preflight.md`. Every default is marked **[Default]**.

Sources read in full: `docs/terms/owner_decisions.md` (all entries), `docs/terms/level_4_year_plan.md` (all four terms, both revision blocks, the verified-against-MOE block, the "Non-routine assignments" section, the matrix and the paper notes), `docs/books/p4_school_paper_patterns.md`, `docs/books/p4_non_routine_catalogue.md`, `docs/moe/syllabus_by_level.md` (P4 pp. 37 to 40, P3, P5 and the year index), `docs/sasmo/g4_analysis.md` and `g4_original_problems_draft.md`, the holiday program of the same level (`p4/SPEC.md` and `p4/content/l1.js` to `l10.js`: all 239 question-bank items, 60 core, 89 stretch and 90 challenge, and every lesson's objective, warm-up, explore and extension line were extracted and read), `docs/terms/l1_term2_preflight.md`, `docs/terms/l1_term3_term4_preflight.md`, `docs/terms/l2_preflight.md`, `docs/terms/l3_preflight.md` (first 130 lines; the file is still being written by another agent), `term/l1/AUTHORING.md`, `WORDING_GUIDE.md`, `audit/TERM_WIDE_AUDIT.md`, `audit/CUTOUT_AUDIT.md`, `audit/FINAL_AUDIT_T1.md`, `audit/FINAL_AUDIT_T2.md` (finding tables), and the Level 1 tool inventory (`term/l1/tools/figs2.py`, `figs3.py`, `svg.py`, `b_quest.py`). The word-problem analyses (`docs/books/word_problems_g1_g2_*`) cover Grades 1 and 2 only and were not used. I did not re-read the holiday workbooks, slides or tutor guides, only the question banks and lesson metadata.

Numbers marked "verified" were recomputed by brute force in the verification script at the end of this document (section 14): **249 checks, all passed**. Check ids (`V3.2`, `W1.8`, `X7.1`, `Y9.3`, `Q2.4`) point to it: V is Term 1, W Term 2, X Term 3, Y Term 4, Q the Quest gates. Lesson authors must still write their own `verify/lNN_checks.py`; nothing here replaces it.

## 0. Headline findings

1. **The holiday course already teaches every strand that the Level 4 term plan calls new, and many plan items repeat holiday items.** The ten holiday lessons (H1 Factor Hunters, H2 Big Number Puzzles, H3 Operation Detectives, H4 Fraction Frontier, H5 Decimal Detectives, H6 Angle Turns, H7 Area Architects II, H8 Symmetry and Nets, H9 Data Detectives, H10 Puzzle Day) match the term plan almost one for one by topic, and at the level of the question the overlap is large. Worst cases: plan 3.2 Angle Detectives is H6 (clock-hand angles, 8-point compass turns, reversing a turn, angles in a fan, minute-hand degrees); plan 3.3 Rectangle Rules is H7 (all rectangles with area 30, perimeter 20, 24 m of fencing, area 40 and perimeter 26); plan 1.3 Divisibility Detectives is H1 (odd number of factors, "a multiple of 4 and 6 must be a multiple of 24", buses that meet again, multiples of 4 or 6 to 100); plan 4.1 Data Detectives is H9 (misleading scales, two lines that cross, steady rises); plan 4.6 and 4.7 are H3 and H10 (work backwards, heads and legs, half-and-two-more); plan 3.1 is H8 (the 11 nets, 5 in a row cannot fold, opposite faces add to 7). Owner decision 4 sends holiday graduates to Term 1, so a graduate would meet these twice. Section 13 is a lesson-by-lesson register with "do not reuse" lists and a verdict (Change, Second visit, New). The plan's claim "Term 1 is new content" is true by title and false by item.
2. **Five plan items are close copies of contest or other in-house items and are replaced here.** (a) 1.2 Think harder, "smallest 3-digit number whose digits multiply to a 3-digit number", is SASMO 19-18 word for word; replaced by a digit product of 168 and a 4-digit follow-up (V2.4, V2.6). (b) 1.3, "a digit in 2_4 so it is divisible by 6" (the draft's form) is SASMO 19-3; replaced by 6 _ 8 in the 9 table and 417 _ in the 6 table (V3.2). (c) 1.3 Go further EXP uses catalogue example EX-EXP-3, which is holiday H1 challenge 5 ("a multiple of 4 and of 6 must be a multiple of 24"); replaced by "digits add to 12, so it is in the 12 table" (counterexample 39, V3.7). (d) 4.3 Think harder, "the sum of the numbers 31 to 41", is SASMO 19-16 with the same range; replaced by 47 to 59 (689, Y3.3). (e) 4.9 and the 8-digit date idea is SASMO 19-22; replaced by the digits of dates written dd/mm in 2027 (Y9.3). The plan itself lists each as a contest-style Think harder idea; the copy check (7-word overlap) would not catch an idea copied with new wording, so the authors must start from the replacements in section 1.
3. **One plan Go further item is impossible.** Plan 1.6 Go further asks for "a figure with exactly two parallel pairs and one perpendicular pair". Two parallel pairs in a quadrilateral force a parallelogram, which has 0 or 4 perpendicular pairs; a search of every simple quadrilateral on a 5 by 5 dot grid and every pentagon on a 4 by 4 grid found none (V6.1). Hexagons exist but are awkward non-convex shapes. Replaced by "a quadrilateral with exactly one right angle and no parallel sides" (exists, V6.2) and "can a quadrilateral have exactly three right angles?" (no, V6.3).
4. **The plan's non-routine section assigns the same example to several lessons.** EX-PAT-3 (alternating decimal steps) is in 1.5 and 4.3; EX-GC-1 (two sharing rules) in 1.8 and 4.7; EX-EQ-4 (decimal unit chain) in 2.8 and 4.7; EX-CTX-1 (pack prices) in 1.2, 1.3 and 2.7; EX-BACK-1 (tank) in 2.5 and 4.6; EX-POSE-1 in 1.8 and 4.8. This pre-flight gives each lesson its own context and numbers (section 1), so no two lessons share an item, and none repeats a catalogue example (the catalogue is the project's own original text, but the lessons must not paste it).
5. **Lessons 10, 20, 30 and 40 are Quest lessons and the plan's "Challenge Day plus 30-minute check" no longer fits.** The plan (section 5) puts a 10-question check of about 30 minutes in x.10; the owner replaced the check by Mi's Challenge Quest, 20 minutes after the break, with eight gates and a cave. That leaves about 19 minutes of Explore and Mini-lesson in the Challenge Day. Each x.10 is therefore a short Challenge Day (one move taught, three tiers kept short) plus the Quest. The contest moves the plan lists for x.10 (guess and check, backwards, hints puzzle, routes) are mostly in the holiday course (H10), so the Term 1 Challenge Day is rebuilt around new contexts and the gates, not around H10 items.
6. **Level 1's tools cover about half of Level 4's figures.** `number_line`, `hundred`, `table`, `bar_model`, `clock`, `money`, `calendar`, `grid`, `cube_stack`, `panel`, `network`, `picture_graph`, `objects`, `groups`, `array`, `balance` (not yet) and the kit pages exist; Level 4 also needs vertical column and area-model figures, stacked fractions and mixed numbers, a stronger `bar_model` (up to 16 units, decimals, before and after), an angle and compass family, dimensioned shapes with joined and folded pieces, solids and nets with a fold check, line graphs, bar graphs without a scale, pie charts, a logic grid, figure sequences, spinners and dice, and a balance. Section 3 lists 27 items; the Level 4 share is about 118 hours of template engineering (about 100 with deferrals), on top of the shared Level 2 and 3 items (parametrisation M1, validator M15, fraction renderer M2) that are built once.
7. **Printed books are black and white and scaled to 94.3 percent; Level 4 measures things.** Protractor, ruler and set-square tasks are the P4 syllabus (angles in degrees, drawing rectangles and squares, perpendicular and parallel lines), but a printed length is wrong in the book (CUTOUT_AUDIT F4, FINAL_AUDIT_T1 finding 2). Angles survive uniform scaling; lengths do not. Rule: every length is given in words or labels, the child draws to real size on squared pages with a real ruler, "All diagrams are not drawn to scale" appears on figure pages, and no task asks a child to measure a printed length. Children need a ruler, a protractor and a set square at home (decision D5). Pie charts, graphs and fractions must use hatch patterns (M18).
8. **Older children change the workbook, not just the numbers.** The P4 papers print Section C items with (a) and (b), "Ans:" lines with units, working space, and up to 4 marks (no marks are printed on our child pages). Level 1's workbook geometry (36 px answer boxes, 8 mm lines, 18.5 px text) is built for age 6 to 8; a Level 4 page needs a "Working" box, an "Ans:" frame, smaller writing lines and pages that stay 85 percent full without the large type (N6). The shared validator fills and thresholds assume the Level 1 geometry.
9. **Cutting load is light: 51 pieces a year** (Term 1 23, Term 2 0, Term 3 22, Term 4 6). Level 4 is mostly paper and pencil with real instruments; the kits are digit cards, a fraction wall, nets, a tangram, eight identical rectangles and a set of 1 to 6 cards. The Level 1 audit objected to 203 pieces in one term. Section 4 gives the kit contract for every lesson.
10. **Six lessons have no school-paper evidence** (the P4 papers read have no item of these kinds): 1.9 Count by Size, 3.7 Cube Stacks and Views, 4.4 Solve a Smaller Problem, 4.5 chance, 4.8 Looking Ahead to P5, 4.9 Count Place by Place. They are the right lessons to make up first in an exam period and the right place to trial wording. About 45 mostly 2021 and 2022 P4 PDFs were not read and the pictures were lost in OCR, so every item that depends on a figure (joined rectangles, folded paper, pie charts, graphs, nets, protractors) is marked "wording unverified" until the owner supplies a picture (decision D21).
11. **Unit chains are 27 percent of the non-routine paper and the plan teaches them in two lessons.** The plan's own notes say unit-chain Think harder items go into 1.2, 2.1, 2.7, 2.8, 4.6 and more; this pre-flight places an EQ item in 10 lessons (matrix, section 13) and gives each its own context. The `bar_model` figure caps at 10 cells and 3 bars, which is too small for "5 small jars and 3 big jars" style models (F4).
12. **Estimate:** about 330 agent-hours for the 40 lessons (write, wording review, independent audit, fix pass, four term-wide audits and a consistency sweep) and about 118 hours of Level 4 template engineering, so roughly 450 hours; at the Level 1 pace (eight to ten writers, three engineers) about 8 to 10 working days from Sprint A to an audited Term 4 (section 11). Hours are estimates from the Level 1 documents, not measurements.

## 0.1 Assumptions made (change them if wrong)

- **Format.** 40 lessons of 90 minutes (owner decision of 23 Oct, "work with 90 mins"), groups of up to 8, online. Files are `term/l4/lessons/l01.json` to `l40.json` (global numbers 1 to 40, the plan's numbering written Term.Lesson); `level` 4, `term` 1 to 4, `lesson` 1 to 40, `lesson_in_term` 1 to 10, `id` `l4-t1-01` ... `l4-t4-40`, practice keys `l4t1l01` ... `l4t4l40` (the level prefix is new, because the shared runner already holds `t1l01` for Level 1 and the Level 2 pre-flight proposes `l2t1l01`). Family pages print "Level 4 Term 3 Lesson 4", never "Lesson 24 of 10". The leak check allows "Lesson 1" only where `lesson_in_term` is 1. Taglines: Term 1 "Notice it", Term 2 "Test it", Term 3 "Explain why", Term 4 "Create and connect" (the year arc, as at Levels 1 to 3).
- **The 11-part skeleton as built at Level 1:** Opening 2, Remember 6, Sneak-peek 4, Explore 14, Mini-lesson 10, Break 4, Workbook 28, Talk 6, Exit 6, Look-back 3, Flex 5 (Opening may be 4 with Explore 12). Quest lessons (10, 20, 30, 40): Opening 2, Remember 6, Sneak-peek 4, Explore 10, Mini-lesson 9, Break 4, **Quest 20 at minutes 35 to 55**, Workbook 25, Talk 4, Look-back 2, Flex 4 = 90; the exit ticket is not live. **[Default]** The Level 4 break stays 4 minutes (decision D17 offers 5 for ages 9 to 11).
- **Tiers.** Start here 6 questions (workbook pages 1 and 2, at most 20 modelled minutes for a middle child), Think harder 4 (page 3), Go further exactly 3 (page 4), one Investigation (page 5) with an easy first step, kit page 6 only where a kit exists. Start here is a P4 school skill (the syllabus outcome in the plan) with scaffolding; Think harder carries a taught idea in a new setting **and every contest-style item** (owner decision 6); Go further is extension. No non-routine item at Start here (owner rule of 23 Oct). Labels are neutral and never shown as ranks. The papers' typical Section C part (a) is Think harder; the hardest paper item is Go further (`p4_school_paper_patterns.md` section 2).
- **A named beyond-syllabus item in every lesson** (owner rule, 23 Oct): one named puzzle at Think harder or Go further, never Start here, original, with a tutor-only `beyond` field `{name, where, text, parent}` and a one-line level note (for example "Primary 5 idea"). It takes one of the Think harder or Go further slots; it is not an extra question. Child-visible puzzle titles never carry the word "beyond" or "challenge" (D20).
- **Mi's Challenge Quest** in lessons 10, 20, 30, 40 (owner decisions of 22 Oct): a game, no scores, marks, ranking or visible timer, no word "test" or "exam" on any child or parent page (`BAN_FAMILY` in `b_quest.py`), private paper, the tutor keeps private notes for one line per parent, photos returned by the parent to the business WhatsApp (+65 9880 5962, never on slides). Eight gates and one optional cave (section 6). The plan's old 30-minute check (plan section 5) is superseded.
- **Books.** Printed black-and-white 5-lesson books issued on payment: Book k holds lessons 5k-4 to 5k (eight books). The Quest Log sits in Books 2, 4, 6 and 8. Kit pages are on a front page with a blank back; soft copies stay colour. **[Default]** both books of a term are issued with the first payment (D11 at Level 1).
- **Wording** follows `WORDING_GUIDE.md` with the Primary 4 changes in section 1.1: "Ans:" frames with the unit after the line, a "Working" box on multi-step items, options numbered (1) to (4), "true, false or not possible to tell" tick tables, time as 3:20 pm and 24-hour as 1850 (accept 18 50), money as $4.75, "identical", "divided into", "joined to form", no marks printed, no hint naming the tool at Go further, and a hint at Think harder only for a type that is new to the term.
- **Cast.** Mei, Ali, Ben, Siti, Ravi, Kumar, Aisha, Wei, Jenny, Lily, Jamie, Ray, Amelia, Jason, plus Zoe, Kai, Maya, Dev, Hana, Tom, Rani, Lena (the names the P4 papers and the catalogue use), and the shop and place names the papers use (hawker centre, MRT). Wrong working is attributed to "a child" or "a child in another class", never to a cast name (Level 1 audit).
- **Calculators.** None in any lesson; Mi never shows one (P4 pupils do not use calculators; the images with a calculator are replaced).
- **Instruments.** **[Default]** every child has a 30 cm ruler, a protractor and a set square (a P4 school kit); lessons 1.6 and 3.2 say "no protractor? tell your tutor" and the kit supplies a right-angle checker (D5). A grown-up cuts every kit before the lesson; nobody cuts during a lesson (Level 1 rule). Scissors, glue and tape are for the grown-up.
- **Holiday graduates** start Term 1 (December), Term 3 (June) or Term 2 (March) (owner decision 4). Holiday topics return in Remember warm-ups only (owner decision of 22 Oct, "Term 1 is written as new lessons"). This pre-flight adds a stricter rule: **no holiday question is reused in a term lesson at all** (section 13), because the owner's rule is about lessons and the graduate meets questions.

## 0.2 What exists to be reused (checked in the working tree on 23 Oct)

`term/l1/tools/` already renders, for any level, once parametrised: `number_line` (labels, prefix, suffix, jumps, hide, highlight), `hundred` (0 to 99, shade, arrows), `seq`, `ruler` (true scale, not usable in the printed book), `table` (text, boxes, circles, tick boxes, icons), `objects` (55 icons), `groups`, `array`, `bar_model` (compare, part-whole, units, transfer, brace, gap; at most 10 cells and 3 bars), `picture_equation`, `line_up`, `round_table`, two-colour `ten_frame`, `domino`, `clock` (any minute, digital readout, mirror, sector), `money`, `price_tag`, `calendar`, `stick_pattern`, `shapes2d` (circle, half and quarter circle, fold lines; parts 1, 2 or 4), `grid` (dots or squares, polygon, route, counts, mirror), `cube_stack` (iso, top, views; base to 3 by 3, heights to 3), `fold_punch`, `panel`, `network`, `picture_graph`. Kits: `base_ten`, `hundred`, `number_strip`, `cards`, `shapes`, `groups_mat`, `unit_strips`, `array_mat`, `people`, `clock_kit`, `play_money`, `price_tags`, `grid_tiles`, `mistake_cards`, `fold_shapes`, `shape_pieces`, `pair_cards`, `grid_mat`, `graph_mat`, `tool_cards`, `event_cards`, `stick_strips`, `calendar_cards`. Question forms: `visuals`, `tf`, `mcq`, `steps`, `draw`, `choices`, tokens `___`, `[]`, `[2]`, `[3]`, `()`, `[ ]`, `{eq}`. Runner v2: `fig`, `fields`, `ordered`, templated choice, `multiples`, `common`, `divisors`, formatters `{n|ord}`, `{n|word}`, `{n|usd}`, `{n|c}`, `{n|hour}`, `{n|min}`, `pad`. Quest builder `b_quest.py` (gates may name `lesson` as a number, a list or "beyond"; `scope: "year"`; `BAN_FAMILY` words). Lesson fields `beyond`, `materials.kit_contract` (the validator fails if supplied is less than max used), `home_practice[].rewind_of`. `print/make_term_books.py` accepts `--level N --size 5 --per-term 10`.

What does **not** exist (and Level 4 needs): `balance`, `spinner`, `solid`, `net`, `place_value`, `column_sum`, `area_model`, `fraction`, `scale_dial` and `jug` (the Level 2 and 3 pre-flights propose these; none is built), any graph other than the picture graph, any angle figure, and any figure with dimension labels. The Level 2 and 3 pre-flight codes are quoted as "L2 M5" and so on where Level 4 shares an item; Level 4's own items are N1 to N19, F1 to F19 and K1 to K7 in section 3.

Level 1 term lessons 1 to 30 exist; `l31.json` onward are not written (other agents are writing Level 1 Term 4 and are not touched). No `term/l2`, `term/l3` or `term/l4` folder exists yet.

---

## 1. Lesson specs

### 1.0 Field order and conventions

Every spec uses this order: big idea, strand and page references (MOE P4 pp. 37 to 40, PDF pages), objective, Remember warm-up (three items, each re-taught with objects or a picture so a cold joiner can follow), Start here / Think harder / Go further outline with question counts, the **Beyond (named)** item, **Non-routine** work (type code, tier T or G, check id), **Holiday overlap** (what the holiday course did and what the term lesson must not repeat), number ranges, home materials, kit with piece counts (the kit contract: supplied against the most any one task may use), figures, misconceptions, template needs (codes from section 3), and whether the lesson is safe to miss.

**Non-routine work (owner decision of 23 Oct).** Each spec carries the `NR:` line from the plan's "Non-routine assignments" section (type code, tier T or G, never Start here), with the changes this pre-flight makes. Type codes (16): EQ unit and equal-share model, GEO geometry chain, LOG logic or number riddle, CTX unfamiliar context, LIST systematic list or bounds, MULTI multi-step, BACK work backwards, CHAL build or complete from data, EXP explain or true-false, TAB table or graph reading, GC guess and check or two scenarios, PAT pattern, DIAG draw or read a model, CMP comparison, sum and difference, WAYS how many ways, POSE judge or pose a statement. Hints naming the tool ("Hint: draw a model.") may appear in Think harder stems for a type that is new to the term, never in Go further (`p4_school_paper_patterns.md` section 5).

**Examples are original.** Every number and context below differs from the catalogue examples (EX- ids), from the draft problems and from the holiday banks. Authors write their own items of the same kind and their own `verify/lNN_checks.py`; the values here are the ones the pre-flight verified, offered as the model, not as text to paste. The copy check runs against the school and contest sources and, from M15, against `p4/content` (5-word overlap).

**Mid-year entry.** Every Remember re-teaches from nothing the one earlier idea the lesson leans on and uses no word that only an earlier lesson defined. A holiday graduate has met every Level 4 strand once (as a puzzle course); a school-only child has met them in class, usually a term or more earlier or later than our order (the plan's note 7, decision D15). Warm-ups name holiday topics in the guide ("you may know this from the holiday course") but never depend on them.

### 1.1 Level 4 wording deltas from the Level 1 guide (from `p4_school_paper_patterns.md` sections 1 and 5)

Rules 1 to 25 of `WORDING_GUIDE.md` still apply except rule 25 (tests numbers to 40), which becomes: the P4 papers test numbers to 100 000, four operations inside unit chains, fractions with denominators to 12, decimals to 3 places, and 2 to 4 mark Section C problems with (a) and (b); "explain why" prompts stay out of Start here and the exit ticket. Changes: (a) children read their own questions; the tutor reads a stem aloud only for Think harder items; (b) section instructions in paper style ("Show your working clearly." "Write your answers in the units stated."); (c) options (1) to (4) with a bracket at the right, never A to D; (d) an "Ans:" frame with the unit after the line and a "Working" box on every multi-step item; (e) fixed words: "how many more ... than", "times as many", "the same number ... in the end", "after giving away", "Find the sum of", "Find the difference between", "Find the product of", "greater", "smaller" (never "bigger" for numbers), "rounded to the nearest hundred", "smallest possible", "greatest possible"; (f) time written 3:20 pm (accept 3.20 p.m.), 24-hour as 1850 (accept 18 50), durations "2 h 35 min"; (g) money written $4.75 and 475¢, "gave the cashier", "How much change?"; (h) units km, m, cm, kg, g, l, ml; (i) the tick table "Each statement below is true, false or not possible to tell. Put a tick in the correct column."; (j) "More than ... and less than ..." riddles keep both words in the stem; (k) geometry words "identical", "divided into", "joined to form", "turns clockwise", "anticlockwise", "facing"; (l) "All diagrams are not drawn to scale." on figure pages (also the honest answer to the 94.3 percent print scale); (m) no stem names its tool at Start here; (n) part (b) uses part (a); a third part may appear at Go further.

---

## Term 1: Notice it (lessons 1 to 10)

Cold joining: yes. The Remember warm-ups carry place value to 10 000, the times tables to 10 x 10, fractions as equal parts, and a protractor-free idea of a right angle. A holiday graduate has met every topic once as a puzzle (H1 to H10) and must not meet an item again (section 13). **Safest to skip or make up (recording, or a holiday class): lesson 9** (the added lesson; nothing later leans on it except one Remember item in lesson 10); hardest to miss: 1, 2, 3 and 8. Lesson 10 hosts the Quest and cannot be skipped lightly (the make-up route is the Quest at the make-up slot).

### Lesson 1. Across the Zeros (T1.1)

- **Big idea.** Regrouping is place value at work, and a quick estimate tells you whether an answer can be right.
- **Strand.** MOE P4 Whole Numbers 1.1 to 1.6 (numbers to 100 000, rounding to the nearest 10, 100 or 1000, the sign for "is about", p. 37); adding and subtracting to five digits extends the P3 algorithm (p. 35). Contest tags (tutor only): bounds and digit cards (SASMO number sense, 19-18 family).
- **Objective.** Read, order and round numbers to 100 000; add and subtract with regrouping across zeros; estimate first, then check. Think harder: take 10 000 minus a number two ways; spot the slip in a worked subtraction; bounds on a rounded number inside a difference. Go further: a closest-pair digit-card puzzle; a three-step story with a difference of 10 000.
- **Remember (6 min).** (1) The value of the 8 in 83 062 and in 38 062 on a Th H T O chart (new numbers; H2 used 64 205). (2) Round 4 750 and 4 749 to the nearest 100 on a drawn line. (3) Regroup one thousand as ten hundreds with counters (the move the lesson uses).
- **Start here (6).** (1) Words for 48 070 as a choice item, options (1) to (4). (2) Arrange 62 305, 62 053, 62 350 and 62 035. Begin with the smallest. (3) 46 385 + 27 748 = 74 133 with a carry (V1.1a). (4) 70 000 - 24 316 = 45 684, regrouping across four zeros, with a worked partner step (V1.1b). (5) Estimate 59 802 - 38 195 by rounding each to the nearest thousand (60 000 - 38 000 = 22 000), then find the exact 21 607 (V1.1c, V1.1d). (6) Round 47 658 to the nearest 10, 100 and 1000: 47 660, 47 700, 48 000 (V1.1e).
- **Think harder (4).** (1) 10 000 - 3 785 two ways (renaming; counting up from 3 785): 6 215 (V1.2a). (2) A child works 50 003 - 28 479 and writes 22 524; find the step that is wrong; correct answer 21 524 (V1.2b). (3) **LIST/bounds.** A rounds to 7 400 and B rounds to 2 600, both to the nearest 100. What are the greatest and the smallest possible differences? 4 899 and 4 701 (V1.3a, V1.3b). The twist is rounding bounds inside an operation. (4) **LOG.** Use the cards 2, 4, 5, 7 and 9 once each. Make the smallest number that rounds to 60 000 to the nearest ten thousand: 57 249 (V1.4).
- **Go further (3).** G1 **Beyond (named): "Close Neighbours".** Use the cards 1, 3, 4, 6, 7 and 9 once each to make two 3-digit numbers with the smallest possible difference: 19, from 416 - 397 or 713 - 694 (two ways, V1.5). Level note: contest-style digit arrangement; the arithmetic is Primary 4. G2 **EQ.** Class A raised $18 460; class B raised $3 975 less than class A; class C raised $10 000 more than class B. How much did the three classes raise altogether? $57 430 (V1.6a). G3 A car counter shows 79 996 km; the car then travels 2 307 km. How far is it from 100 000 km? 17 697 km (V1.6b).
- **Non-routine.** EQ G (G2), LIST T (rounding bounds, T3), LOG T (T4). The plan's greatest and smallest rounding item is moved from a bare "A number rounds to ..." to the difference form because H2 holds the bare form.
- **Holiday overlap: HIGH (H2).** H2 did rounding with a number line, smallest and largest that round to 38 000, 5 350 and 5 400, 45 000 and 50 000, palindromes, 99 990 to 100 000, digit cards closest to 70 000, counting on in 1000s from 3 456, the largest odd 5-digit number rounding to 90 000. Do not reuse any of these. The bare bounds item is replaced by bounds inside a difference (second visit with a new twist).
- **Numbers.** 0 to 100 000; sums and differences to 100 000; rounding to 10, 100, 1000.
- **Home materials.** Pencil, squared paper (the book has a place-value mat page).
- **Kit (K1 digit cards).** One set of cards 0 to 9 (10 pieces). Max used by a task 6 (G1) and 5 (T4); Explore lays out all 10. Tasks never need a repeated digit. Keep for lessons 2, 3, 10, 12 and 39.
- **Figures.** `place_value` chart to 5 digits (F5), `column` with borrow marks (F1), `number_line` with an unmarked scale (F6).
- **Misconceptions.** Borrowing from a zero (the zero stays 0); rounding 47 658 to 47 000 when asked for the hundreds; an estimate that rounds both numbers down; reading 48 070 as 48 700.
- **Needs.** F1, F5, F6, K1, N6, N7.
- **Safe to miss?** No. Lessons 2 and 8 lean on the written methods; their warm-ups re-teach the carry.

### Lesson 2. Multiply It Many Ways (T1.2)

- **Big idea.** A product can be split, rounded or doubled and halved, and the choice of way depends on the numbers.
- **Strand.** MOE P4 multiplication algorithm up to 4 digits by 1 digit (Four Operations 3.1, p. 37). Contest tag: digit products (19-18 family). Unit chains with a product total (plan note, EQ).
- **Objective.** Multiply 2-, 3- and 4-digit numbers by one digit by splitting, round-and-adjust, halve-and-double and the column method, with an estimate. Think harder: a unit-chain total with a product; a digit product of 168; a "times as many" chain. Go further: a 4-digit digit product; whole packs; missing digits in a product.
- **Remember (6 min).** (1) 6 x 7, 8 x 9 and 12 x 4 from the table square. (2) 300 x 4 = 12 hundreds = 1 200. (3) Split 346 into 300 + 40 + 6 on an area grid (the model the lesson uses; no answer given).
- **Start here (6).** (1) 346 x 4 by splitting: 1 200 + 160 + 24 = 1 384 (V2.1). (2) 2 508 x 6 in a column: 15 048. (3) 78 x 5 as half of 78 x 10: 390. (4) Estimate 612 x 7 (600 x 7 = 4 200) then 4 284. (5) 6 boxes of 235 pencils: 1 410. (6) 4 tablets at $385 each: $1 540.
- **Think harder (4).** (1) Round and adjust: 49 x 6 = 294, 398 x 5 = 1 990; halve and double: 35 x 18 = 70 x 9 = 630 (V2.2). (2) **EQ.** 8 equal crates and 36 loose tins make 1 580 tins altogether. How many tins in a crate? 193 (V2.3). (3) **LOG.** The digits of a 3-digit number multiply to 168. Find the smallest such number: 378 (the digit sets are {3, 7, 8} and {4, 6, 7}; the largest is 873, V2.4). (4) **MULTI.** A shop has 3 times as many pens as rulers and twice as many rulers as erasers. There are 342 erasers. How many more pens than erasers? 1 710 (V2.5).
- **Go further (3).** G1 **Beyond (named): "Product Bounds".** What is the smallest 4-digit number whose digits multiply to a 4-digit number? 2 789 (product 1 008, V2.6). Level note: contest-style; the idea of the plan's 3-digit item (19-18) is kept only at this larger size, with different numbers and wording. G2 **CTX.** Mugs are sold in boxes of 6 for $27. A café needs 20 mugs. How many boxes, how much, and how many mugs are left over? 4 boxes, $108, 4 left (V2.7). G3 **LOG.** 3 [ ] 4 x 7 = 2 [ ] 1 8: the missing digits are 7 and 6 (374 x 7 = 2 618, unique, V2.8).
- **Non-routine.** MULTI T (T4), EQ T (T2), CTX G (G2), LOG T (T3).
- **Holiday overlap: LOW (H3).** H3 had 2 345 x 3 (routine) and the "times as many" bar. Do not reuse 2 345 x 3, 4 236 / 6 or the 2 340 beads. New.
- **Numbers.** 2- to 4-digit by 1-digit; products to 20 000 in stories.
- **Home materials.** Pencil, squared paper.
- **Kit.** Reuse K1 (max used 4).
- **Figures.** `area_model` (F2), `column` multiply (F1), `bar_model` units with a loose part (F4).
- **Misconceptions.** Forgetting the carry from the tens; 49 x 6 as 49 x 5 + 6; treating "times as many" as "more"; a 0 lost in a middle digit.
- **Needs.** F1, F2, F4, K1.
- **Safe to miss?** Fairly safe (lesson 11 re-teaches the area model).

### Lesson 3. Divisibility Detectives (T1.3)

- **Big idea.** Multiples have patterns you can test, and the test can be explained.
- **Strand.** MOE P4 factors and multiples (2.1 to 2.5, p. 37): tests for 2, 5, 10 (last digit), 3, 6, 9 (digit sum), common multiples, common factors. Digit-sum tests are Think harder (owner decision 6). Contest tag: divisibility tests (19-3), meet-again cycles.
- **Objective.** Colour multiples on a chart and write the last-digit patterns; test numbers within 100 for a 1-digit factor; list common factors and common multiples. Think harder: the digit-sum test for 3 and 9; "in the 2 and 3 tables means the 6 table"; a missing digit; two cycles that start at different times. Go further: a swap-and-subtract pattern; a pack-price problem; counting common multiples in a range.
- **Remember (6 min).** (1) Count in 4s and 6s to 48 on a strip. (2) 7 x 8 and 9 x 6. (3) List the pairs of numbers that multiply to 24 (the factor pairs, re-taught; H1 used 12, 20, 24 and 72, so this is a spiral only).
- **Start here (6).** (1) A hundred chart: colour the 2s, 3s and 5s differently and write what the last digits of the 5s and the 10s look like. (2) Which numbers from 1 to 50 are in both the 3 table and the 5 table? 15, 30, 45 (V3.8). (3) Is 7 a factor of 91, 84, 78? Yes, yes, no (V3.8). (4) The first five common multiples of 4 and 6: 12, 24, 36, 48, 60 (V3.9). (5) The common factors of 18 and 30: 1, 2, 3, 6 (V3.9). (6) A story: Aisha packs 36 stickers in bags of 4; how many bags, and do any remain?
- **Think harder (4).** (1) **The digit-sum test.** Circle the numbers in the 3 table: 4 521, 7 806, 9 134, 5 838. The digit sums 12, 21, 17 and 24 give 4 521, 7 806 and 5 838 (V3.1). Then circle the numbers in the 6 table: 138, 366 and 450 (V3.1). (2) **LOG/missing digit.** 6 [ ] 8 is in the 9 table: the digit is 4 (648, V3.2). 4 1 7 [ ] is in the 6 table: the digit is 0 or 6 (V3.2). (3) **LOG.** I am a 2-digit number in the 6 table and in the 4 table. My digits add to 9 and my tens digit is smaller than my ones digit. What am I? 36 (V3.2). Plus an **EXP** tick table: true, false or not possible to tell about multiples. (4) **Two cycles.** A bell rings at 9:00 and then every 8 minutes. A drum sounds at 9:04 and then every 12 minutes. When do they first sound together? 9:16, then every 24 minutes (V3.3).
- **Go further (3).** G1 **Beyond (named): "Swap and Subtract".** Take a 2-digit number, swap its digits and subtract the smaller from the larger. Show that the answer is always in the 9 table, and that it equals 9 times the difference of the digits (V3.4). Level note: an algebra idea shown by cases; the 9 table is Primary 4. G2 **CTX.** Pencils are sold 4 for $3 and erasers 6 for $5. Hana wants the same number of each and as few as possible. How much does she pay? 12 of each, $19 (V3.5). The papers set pack prices at 2 to 4 marks. G3 Count the numbers from 300 to 400 that are multiples of both 6 and 8: 312, 336, 360, 384, so 4 (V3.6). **EXP** counterexample: Mei says "if the digits add to 12 the number is in the 12 table". Find a counterexample: 39 (V3.7).
- **Non-routine.** LOG T, CTX G (pack prices), EXP T (tick table) and EXP G (counterexample). The plan's EX-EXP-3 is replaced.
- **Holiday overlap: HIGH (H1).** H1 had factor lists of 12, 28 and 72, common factors of 24 and 36, lighthouses 6 and 9, buses 6 and 9, the digit sum of a multiple of 7, "exactly 3 factors", numbers with 1 left over (41, 61), multiples of 4 or 6 to 100, 6s and 8s to 100 (24, 48, 72, 96), the lockers, the claim about 24, a 4-factor odd number. Do not reuse any, and the plan's G items "an odd number of factors" and "count multiples of 6 not 4" are replaced. Verdict: Change.
- **Numbers.** Within 100 for the factor test, to 9 999 for the digit-sum test, ranges to 400.
- **Home materials.** Coloured pencils or a pencil for hatching (the book prints in black and white; "colour" means "hatch"), the hundred chart is in the book.
- **Kit.** Reuse K1.
- **Figures.** `hundred` with three hatch patterns and an overlap pattern (F-exists with M18), `table` tick table.
- **Misconceptions.** "Digits add to 9" read as "ends in 9"; the digit-sum test used for 4; 2 and 4 together taken to mean the 8 table; counting 0 as a multiple in the list.
- **Needs.** M18, N7 (list answers), `tf` (exists).
- **Safe to miss?** No: lesson 12 (remainders) and lesson 31 (patterns) lean on the tests.

### Lesson 4. Fraction Walls (T1.4)

- **Big idea.** The same amount has different names, and a common denominator makes two fractions comparable.
- **Strand.** Equivalent fractions are P3 (p. 35); simplifying and comparing by a common denominator are used in P4 add and subtract (Fractions 3.1, p. 37). Contest tag: comparing shaded areas with half squares (19-14).
- **Objective.** Build a fraction wall to twelfths; find equivalent fractions; simplify; compare two fractions by a common denominator. Think harder: compare shaded fractions of two grids that contain half squares; "which is greater, with a reason"; a stars-to-shade item. Go further: split a fraction into two unit fractions; which is nearer a half; count fractions between two.
- **Remember (6 min).** (1) Fold a strip in halves and quarters and name a quarter. (2) 3 x 4 and 12 divided by 3. (3) Which is greater, 3/8 or 3/5? Same numerator, compare the parts (re-taught with strips; H4 used 3/7 against 3/5).
- **Start here (6).** (1) On the wall, 2/3 = [ ]/12: 8 (V4.1). (2) 3/5 = [ ]/20: 12. (3) Simplify 18/24 (3/4) and 20/45 (4/9) (V4.1). (4) Which is greater, 5/8 or 3/4? 3/4 (V4.1). (5) Arrange 2/3, 3/4 and 5/12. Begin with the smallest: 5/12, 2/3, 3/4 (V4.2). (6) A bar of 12 equal parts has 5 shaded. How many more must be shaded so that 3/4 of the bar is shaded? 4 (V4.6).
- **Think harder (4).** (1) Simplify 36/48 and 28/42 using the greatest common factor. (2) **LIST/CMP.** Grid A has 12 squares, 7 of them shaded (5 whole squares and 4 half squares). Grid B has 16 squares, 9 of them shaded (8 whole and 2 half). Which grid has the greater fraction shaded? A, because 28/48 is more than 27/48 (V4.3). (3) **EXP.** Which is greater, 4/9 or 3/7? 4/9, by 28/63 against 27/63 (V4.4). (4) **LIST.** 24 stars are in 4 rows of 6, and 7 are shaded. How many more must be shaded so that 5/8 of the stars are shaded? 8 (V4.5).
- **Go further (3).** G1 **Beyond (named): "Split a Fraction".** Write 2/5 as the sum of two different unit fractions: 1/3 + 1/15, the only way (V4.7). Level note: unit-fraction sums are secondary school; the equivalent fractions are Primary 3 and 4. G2 **CMP.** Which of 4/7 and 5/12 is nearer to one half, and by how much? 4/7, by 1/14 against 1/12 (V4.8). G3 How many fractions with denominator 24 lie between 1/3 and 1/2? 9/24, 10/24 and 11/24, so 3 (V4.9).
- **Non-routine.** LIST T (T4), EXP T (T3), CMP G (G2). The plan's EX-LIST-3 is used with new numbers.
- **Holiday overlap: MED-HIGH (H4).** H4 ordered 1/2, 7/12, 2/3 and 5/6, compared 3/8 with 3/5 and 5/6 with 2/3, found fractions with denominator 10 between 1/5 and 1/2 (3/10 and 4/10), 12/16 from a numerator and denominator sum of 28. Do not reuse these fractions. Grids with half squares are new (19-14 idea).
- **Numbers.** Denominators to 12, products of two denominators to 63 in comparisons.
- **Home materials.** Pencil, the wall strips from the kit.
- **Kit (K2 fraction wall).** 12 strips (1/1 to 1/12), one page. Max used by a task 12 (Explore builds the whole wall); tasks 6 or fewer. Cut 12. Keep for lessons 5, 14, 15 and 16.
- **Figures.** `fraction` (wall, bar, grid with half squares, number line; L2 M2/M3 shared, F3 here).
- **Misconceptions.** Comparing numerators only; adding 4 to both parts to keep a fraction equal; a half square counted as a whole.
- **Needs.** F3, K2, M18 (hatch).
- **Safe to miss?** No: lessons 5, 14, 15 and 16 lean on the wall.

### Lesson 5. Fractions and Decimals Are Twins (T1.5)

- **Big idea.** Tenths and hundredths have two writings, a fraction and a decimal, and each is easy to read from a hundred grid.
- **Strand.** MOE P4 Decimals to 3 places and decimal-fraction conversion both ways when the denominator is a factor of 10 or 100 (Decimals 1.3, 1.4, p. 38). 1/8 is a denominator that is not a factor of 100 and is beyond P4.
- **Objective.** Shade a hundred grid, write the fraction and the decimal; convert halves, quarters, fifths, twentieths and twenty-fifths; order a mixed list. Think harder: a 2-decimal number that rounds to a given tenth; a decimal digit riddle. Go further: eighths; alternating decimal steps; a fraction from a decimal clue.
- **Remember (6 min).** (1) 3/10 on a tenths bar. (2) 7 tenths and 4 hundredths written as a decimal. (3) 100 divided by 4, 5 and 20.
- **Start here (6).** (1) Shade 0.37 on a hundred grid and write the fraction 37/100. (2) 7/10 = 0.7; 3/20 = 0.15 (V5.1). (3) 0.6 = 3/5; 0.25 = 1/4 (V5.1). (4) Arrange 0.5, 3/10, 0.45 and 2/5. Begin with the smallest: 3/10, 2/5, 0.45, 0.5 (V5.2). (5) 4 3/10 as a decimal: 4.3 (V5.3). (6) 3/4 of $1 is $0.75.
- **Think harder (4).** (1) 9/20 = 0.45 and 13/25 = 0.52 (V5.1). (2) Order five numbers, mixing fractions, decimals and one mixed number. (3) **LIST.** A number with 2 decimal places rounds to 4.8 to the nearest tenth. What are the smallest and the greatest it can be? 4.75 and 4.84 (V5.4). (4) **LOG.** I have 2 decimal places and lie between 3 and 4. My tenths digit is twice my hundredths digit and my digits add to 12. What am I? 3.63 (V5.5).
- **Go further (3).** G1 **Beyond (named): "Eighths".** 1/8 is 125 thousandths, 0.125. Find 3/8, 5/8 and 7/8: 0.375, 0.625, 0.875 (V5.6). Level note: denominators that are not factors of 10 or 100 are Primary 5 (p. 41). G2 **PAT.** The pattern 7.50, 7.65, 7.60, 7.75, 7.70, ... adds 0.15 and takes away 0.05 in turn. What is the 10th number? 8.05 (V5.7). G3 **LOG.** I am a fraction with denominator 25 equal to a decimal between 0.5 and 0.6 whose hundredths digit is 2. What fraction am I? 13/25 (V5.8).
- **Non-routine.** LIST T, LOG T, PAT G. EX-PAT-3 is used here only (4.3 gets a different Go further).
- **Holiday overlap: MED (H5).** H5 read decimals to 3 places, ordered them, rounded, used $3.47, 90 and 89 cents, 3.69/3.96 digit cards, a rounding bound for 10 and for 7.4. Do not reuse 7.4, 10, 2.46 or the digit cards 3, 6, 9. Fraction-decimal conversion is new. Verdict: second visit.
- **Numbers.** To 3 decimal places; denominators 2, 4, 5, 10, 20, 25, 100.
- **Home materials.** Pencil and hatching, the hundred-grid page.
- **Kit.** None cut: a printed page with two hundred grids (uncut).
- **Figures.** `hundred_grid` (a 10 by 10 grid with shading; the existing `hundred` is a numbered chart, so a plain grid is F20), `number_line` with decimal labels (F6).
- **Misconceptions.** 3/20 = 0.20; 0.6 read as 6 hundredths; ordering 0.45 above 0.5 because 45 is greater than 5; rounding 4.75 down.
- **Needs.** F20, F6, M18, N7.
- **Safe to miss?** Fairly safe (lesson 15 re-teaches the pairs in context).

### Lesson 6. Lines That Behave (T1.6)

- **Big idea.** Perpendicular and parallel are rules, and a drawn rectangle must obey them.
- **Strand.** MOE P4 perpendicular and parallel lines, properties of rectangles and squares (excluding diagonals), drawing them with a ruler and set square (Geometry 2.2, p. 39). Diagonal properties are explicitly excluded at P4 and are the beyond item.
- **Objective.** Identify perpendicular and parallel lines; draw a perpendicular and a parallel with a set square; draw a rectangle or a square from given sides; decide which properties belong to which shape. Think harder: true, false or not possible to tell; a shape from clues. Go further: diagonals; a quadrilateral with exactly one right angle; can a quadrilateral have exactly three right angles?
- **Remember (6 min).** (1) A right angle is the corner of a page. (2) Name the shapes with 4 sides. (3) Lines that never meet (parallel rails) and lines that cross at a corner.
- **Start here (6).** (1) Which pairs of lines in a picture are perpendicular? (2) Which pairs are parallel? (3) Draw a line through P perpendicular to AB with a set square. (4) Draw a rectangle 7 cm by 4 cm. (5) Draw a square of side 5 cm. (6) How many pairs of parallel sides do a rectangle and a square each have? 2 and 2.
- **Think harder (4).** (1) **EXP.** Each statement is true, false or not possible to tell: a square is a rectangle (true); a rectangle has 4 equal sides (false); two lines perpendicular to the same line are parallel (true, in a flat page); a figure with 4 right angles is a square (false). (2) Draw rectangle ABCD with AB = 8 cm and BC = 3 cm, then a line through C parallel to AB. (3) **LOG.** A 4-sided figure has four right angles and two pairs of parallel sides, and two of its sides are 5 cm and 9 cm. What shape is it, and what is its area? A rectangle, 45 cm2. (4) In a figure drawn on a grid (a flag with a staircase edge), count the pairs of perpendicular sides and the pairs of parallel sides.
- **Go further (3).** G1 **Beyond (named): "Diagonal Detectives".** Draw the diagonals of a 6 cm by 4 cm rectangle and a 4 cm square on squared paper. The rectangle's diagonals are equal in length; the square's cross at a right angle (V6.4). Level note: diagonal properties are excluded from the Primary 4 syllabus (p. 39). G2 **GEO.** Draw a quadrilateral on a dot grid with exactly one right angle and no parallel sides: one exists, for example with corners (0, 0), (0, 1), (1, 1), (3, 2) (V6.2). The plan's "two parallel pairs and one perpendicular pair" is impossible for a quadrilateral (V6.1). G3 Can a quadrilateral have exactly three right angles? No: tried on every simple quadrilateral of a 5 by 5 dot grid, counts of right angles are 0, 1, 2 or 4, never 3 (V6.3).
- **Non-routine.** EXP T (shape properties), LOG T, GEO G. The plan's EX-EXP-1 is replaced by the tick table.
- **Holiday overlap: NONE (H7 touched rectangles by area only).** New.
- **Numbers.** Sides 2 to 12 cm.
- **Home materials.** Ruler, set square, pencil, dot paper (in the book). Protractor not needed.
- **Kit (K3 right-angle checker).** 1 piece (a cut-out right angle). Max used 1. Cut 1. Keep for lesson 22. "No set square? Use the checker." The checker is also the answer to the 94.3 percent print scale: a right angle does not scale.
- **Figures.** `shape2d` with right-angle marks and parallel arrows (F8), `grid` dots (exists).
- **Misconceptions.** "Perpendicular" taken to mean vertical; parallel lines drawn to converge; a square not accepted as a rectangle; measuring a printed line.
- **Needs.** F8, K3, N6.
- **Safe to miss?** Yes for the beyond item; the rest is needed by lessons 22 and 25.

### Lesson 7. Sort It Out (T1.7)

- **Big idea.** There are two ways to sort the same group, and a table with its totals can be completed from a few numbers.
- **Strand.** MOE P4 tables: complete a table from data, read and interpret tables (p. 40). Logic grids are not on the syllabus (enrichment).
- **Objective.** Fill a table from a tally; complete a two-way table with row and column totals; solve a logic puzzle by elimination. Think harder: missing entries given as letters; a 3-person logic puzzle. Go further: a 4-person logic grid; complete a table from clues and a total.
- **Remember (6 min).** (1) Make a tally for 13. (2) Add three numbers to make a total. (3) Which numbers are in a table row and which in a column.
- **Start here (6).** (1) Complete a tally table of favourite fruit. (2) The total of each row. (3) A two-way table with one blank total. (4) A sorting diagram of 12 numbers into "multiple of 3" and "not". (5) Read a value off a two-way table. (6) A story: how many more girls than boys.
- **Think harder (4).** (1) **TAB.** Class 4C has 40 pupils. A two-way table gives boys 22 and girls 18; 14 boys swim; 9 girls do not swim. Find the missing entries A, B, C and D: 8, 9, 18, 17, and the total who swim, 23 (V7.1). (2) **LOG.** Ali, Mei and Ravi have a cat, a dog and a fish. Ali does not have the dog. Mei has neither the fish nor the dog. Ravi does not have the cat. Who has what? Ali fish, Mei cat, Ravi dog (V7.2). (3) A table with ink blots on two cells. (4) A half-finished sorting diagram with a true or false check.
- **Go further (3).** G1 **Beyond (named): "Four Friends, Four Clubs".** Ali, Mei, Ravi and Siti belong to swimming, chess, art and football. Five clues fix the answer: Ali swimming, Mei art, Ravi football, Siti chess (V7.3). Level note: logic grids are not on the syllabus. G2 **CHAL.** Complete a table from three clues and a total. G3 Pose a clue set that has exactly one answer.
- **Non-routine.** TAB T, LOG T, CHAL G. The plan's EX-TAB-2 is used with new numbers.
- **Holiday overlap: LOW (H9 S1 had a boys-and-girls table).** Do not reuse Classes 4A and 4B with 28 boys and 63 pupils. New.
- **Numbers.** Totals to 100.
- **Home materials.** Pencil. No kit: the logic grid is printed.
- **Kit.** None.
- **Figures.** `table` with letters in cells (exists), `logic_grid` (F11).
- **Misconceptions.** Adding a row total to a column total; leaving a cell empty when a clue says "not"; using a clue twice.
- **Needs.** F11, N7.
- **Safe to miss?** Yes: nothing later needs the logic grid; lessons 16 and 30 revisit tables.

### Lesson 8. Share It Out (T1.8)

- **Big idea.** Division is fair sharing with leftovers, and what the leftover means depends on the story.
- **Strand.** MOE P4 division algorithm up to 4 digits by 1 digit (Four Operations 3.2, p. 37).
- **Objective.** Divide 3- and 4-digit numbers by one digit, with and without a remainder and a zero in the quotient; decide when to round up; check by multiplying. Think harder: round up for boxes; two sharing rules. Go further: find the number from a quotient and a remainder; biggest and smallest numbers with a given remainder; why a fraction of a class cannot be right.
- **Remember (6 min).** (1) 56 divided by 7 and 72 divided by 8. (2) Share 3 hundreds, 5 tens and 7 ones among 3 with counters. (3) 4 x 23 + 1.
- **Start here (6).** (1) 756 / 3 = 252. (2) 861 / 7 = 123. (3) 925 / 4 = 231 remainder 1 (V8.1). (4) Check 925 / 4 by multiplying back and adding the remainder. (5) 1 000 sweets are shared among 8 bags: 125. (6) A story where the remainder is thrown away.
- **Think harder (4).** (1) 6 408 / 8 = 801, with a zero in the quotient (V8.1). (2) **CTX.** 1 245 eggs are packed 8 to a box. How many boxes are needed? 155 full boxes and 5 eggs over, so 156 (V8.2). (3) **GC.** Sweets are shared among some friends. If each gets 6, there are 5 left over; if each gets 8, there are 7 short. How many friends and sweets? 6 friends, 41 sweets (V8.3). (4) A story with a hidden extra step (the sharer counts).
- **Go further (3).** G1 **Beyond (named): "Biggest and Smallest Left-Overs".** The smallest and greatest 4-digit numbers that leave 3 when divided by 7: 1 004 and 9 999 (V8.5). Level note: bounds on a remainder condition are contest-style. G2 **BACK.** A number divided by 8 gives quotient 135 and remainder 6: 1 086 (V8.4). G3 **POSE.** Amir says 2/3 of the 40 pupils in the choir are boys, so there are 26 boys. Why cannot that be right? 40 is not a multiple of 3 (V8.6). The plan's EX-POSE-1 is replaced.
- **Non-routine.** GC T, CTX T, BACK G, POSE G.
- **Holiday overlap: LOW-MED (H3 C6, H1 C3).** Do not reuse 4 236 / 6, 52 stickers among 4. The two-scenario sharing item is new.
- **Numbers.** Dividends to 9 999; divisors 2 to 9.
- **Home materials.** Pencil; 30 small things for the Explore.
- **Kit.** None.
- **Figures.** `column` short division (F1), `bar_model` (F4).
- **Misconceptions.** A remainder larger than the divisor; dropping the zero in 801; rounding down when boxes are needed; the sharer left out.
- **Needs.** F1, F4.
- **Safe to miss?** No: lesson 12 and lesson 19 lean on division.

### Lesson 9. Count by Size (T1.9, added)

- **Big idea.** Count each size separately, then add; a table shows the pattern.
- **Strand.** Heuristics (process, p. 13); not an outcome. Contest tag: counting figures (19-2), squares in a grid. **No school-paper evidence.**
- **Objective.** Count unit squares and small triangles; count squares of every size; count rectangles; find a pattern from a table. Think harder: a triangle with lines from one corner; a table of figure number against count. Go further: a larger grid; triangles in a triangular grid.
- **Remember (6 min).** (1) Count the squares in a 3 by 4 grid: 12. (2) Name a triangle and a rectangle. (3) 1 + 4 + 9 (the squares of 1, 2, 3, re-taught).
- **Start here (6).** (1) A 2 by 2 grid: 4 small squares and 1 large, 5 in all (V9.1). (2) A 3 by 3 grid: 9 + 4 + 1 = 14 (V9.1). (3) Count the small triangles in a figure. (4) A grid of 3 by 4 unit squares: how many in all? (5) Count 2 by 2 squares in a 3 by 3 grid: 4. (6) A story with a chessboard row.
- **Think harder (4).** (1) **PAT.** A triangle has 3 lines drawn from its top corner to its base, so the base is cut into 4 parts. How many triangles of every size? 10 (V9.3). (2) How many rectangles in a 2 by 3 grid? 18 (V9.2, T). (3) **TAB.** Complete a table of grid size (1 by 1 to 4 by 4) against the number of squares: 1, 5, 14, 30 (V9.1, V9.6). (4) A figure of two overlapping squares: count the squares.
- **Go further (3).** G1 **Beyond (named): "Triangles Everywhere".** A triangular grid of side 4 holds 27 triangles of all sizes; sides 1 to 5 give 1, 5, 13, 27, 48 (V9.4). Level note: contest-style counting; the counting is Primary 4 arithmetic. G2 **GEO.** Squares in a 5 by 5 grid: 55 (V9.1). G3 Rectangles in a 4 by 4 grid: 100 (V9.2).
- **Non-routine.** PAT T, TAB T, GEO G.
- **Holiday overlap: LOW (H6 counted angles in a fan, H7 S6 tile perimeters).** Do not reuse the fan of 25, 40 and 25 degrees or 10 angles. New.
- **Numbers.** Grids to 5 by 5.
- **Home materials.** Pencil, a ruler for lines.
- **Kit.** None; figures are printed (tracing paper optional).
- **Figures.** `grid` with square outlines (exists), `triangular_grid` (F19).
- **Misconceptions.** Missing the bigger squares; counting the same rectangle twice; thinking the triangle count is the number of lines.
- **Needs.** F19, F12.
- **Safe to miss?** Yes, the safest of Term 1 (the plan's added lesson); one Remember item in lesson 10.

### Lesson 10. Challenge Day 1, with Mi's Challenge Quest (T1.10)

- **Big idea.** Choose a way in: a table, a picture, working backwards, or a set of hints.
- **Strand.** Heuristics (process, p. 13): guess and check with a table, work backwards, hints puzzle. The Quest follows the lesson (section 6).
- **Objective.** Solve a guess-and-check problem with a table, undo a chain, and solve a hints puzzle. The Quest carries a gate for each of lessons 1 to 9.
- **Remember (6 min).** (1) Two numbers add to 10; which pairs? (2) Undo "add 6" and "times 3". (3) A table with columns and a total (lesson 7).
- **Start here (5).** (1) **Table.** Ravi buys 12 notebooks, some at $2 and some at $3, and pays $29. How many $3 notebooks? 5 (V10.1). (2) Two more table items. (3) A picture-drawing item. (4) A one-step backwards item. (5) Reading a clue list.
- **Think harder (3).** (1) **BACK.** I think of a number, multiply it by 3, take away 8 and divide by 2. The answer is 17. What was my number? 14 (V10.2). (2) **GC.** Two numbers add to 25 and multiply to 144: 9 and 16 (V10.3). (3) A working-backwards story with a table.
- **Go further (3).** G1 **Beyond (named): "Four Numbers, Three Hints".** Use the digits 2 to 7 once each to make three 2-digit numbers. The smallest is a multiple of 5, the digits of the middle one add to 9, and the biggest is 22 more than the smallest. Find them: 25, 36, 47 (V10.4). The Quest cave also carries one unseen puzzle. G2 **MULTI.** A mixed contest set. G3 **CHAL.** Make up a hints puzzle with exactly one answer.
- **Non-routine.** GC T, BACK T, MULTI G, CHAL G. The Term 1 check of the plan is replaced by the Quest.
- **Holiday overlap: HIGH (H10).** H10 had next-door numbers (90, 624, 783), chickens and rabbits, double and add 7 (43), 6th from front and back, ages 8 to 11, spiders and ants, the 7 table riddle (91), the hens and goats legs. Do not reuse any. Verdict: Change (new contexts, new numbers).
- **Numbers.** Within 100.
- **Home materials.** Pencil and the K1 digit cards; a quest partner (a grown-up, sibling or friend); the Quest Log stays closed in Book 2 until the lesson.
- **Kit.** Reuse K1 (max used 6).
- **Figures.** `table` (exists), `logic_grid` (F11).
- **Misconceptions.** Stopping at the first answer that fits one clue; undoing the steps in the wrong order.
- **Needs.** Quest block (section 6), N3.
- **Safe to miss?** Yes for the body (Quest sits here and is the part to protect).

---

## Term 2: Test it (lessons 11 to 20)

Cold joining: yes. The Remember warm-ups carry a 3-digit by 1-digit product, a division with a remainder, equivalent fractions from strips, and decimals as tenths and hundredths. A child who missed Term 1 is caught by these. **Safest to skip or make up: lesson 19** (the added lesson; a stand-alone application of lesson 18); hardest to miss: 13 (bars carry lessons 15 and 20), 14, 15 and 17. Lesson 20 hosts the Quest.

### Lesson 11. The Area Model of Multiplying (T2.1)

- **Big idea.** Break a product into rectangles, and let a letter stand for a missing digit.
- **Strand.** MOE P4 multiplication algorithm up to 3 digits by 2 digits (Four Operations 3.1, p. 37); 2 digits by 4 digits is beyond P4 and stays out. Contest tag (tutor only): letter-digit sums (SASMO Section B, 8 of the 10 Grade 2, 3 and 4 papers read), owner decision 7 (the plan holds them, the holiday course does not).
- **Objective.** Multiply by an area model and by the column method with an estimate; find missing digits in sums; solve letter-digit sums by the ones column first. Think harder: spot an error in a worked product; a first letter sum; a unit total with a product. Go further: letter sums with two carries and with two answers; digit-swap and last-digit patterns.
- **Remember (6 min).** (1) 6 x 70 and 40 x 30. (2) Split 47 into 40 and 7. (3) Add 3 numbers in a column with a carry. All re-taught on a grid.
- **Start here (6).** (1) 47 x 36 on an area grid: 1 200 + 240 + 210 + 42 = 1 692 (W1.1). (2) 238 x 24 = 5 712 in a column. (3) Estimate 39 x 52 (about 2 000), exact 2 028 (W1.1). (4) Missing digit, no carry: 3 [ ] 4 + 2 5 3 = 5 8 7; the digit is 3 (W1.2). (5) Missing digits with carries: 4 [ ] 7 + [ ] 6 8 = 7 0 5; the digits are 3 and 2 (W1.3). (6) 24 boxes of 135 crayons: 3 240.
- **Think harder (4).** (1) A child works 35 x 46 with partial products 1 200, 180, 200 and 36, and gets 1 616; which product is wrong and what is the answer? 5 x 6 = 30, so 1 610 (W1.4). (2) **Letter sum (new type, hint allowed).** Different letters stand for different digits and no number starts with 0. AB + BC = ADA. Work from the ones column. A = 1, B = 8, C = 3, D = 0 (18 + 83 = 101, unique, W1.6). (3) **EQ.** 15 adult tickets and 24 child tickets cost $822. A child ticket is $13. How much is an adult ticket? $34 (W1.5). (4) **LOG.** [ ] 8 x 3 [ ] = 1 728 with the missing digits 4 and 6 (48 x 36, W1.7).
- **Go further (3).** G1 **Beyond (named): "Two Answers".** ABC + ACD = BEBA has exactly two answers, 619 + 697 = 1 316 and 719 + 798 = 1 517 (W1.8). Level note: contest-style; the column addition is Primary 3. G2 ABC + CBA = BBAB has one answer, 318 + 813 = 1 131, with two carries (W1.9). G3 (a) A 2-digit number plus the number with its digits swapped is always 11 times the digit sum (W1.10); (b) the product of 25 threes ends in 3, because the last digits cycle 3, 9, 7, 1 (W1.11).
- **Non-routine.** EQ T, LOG T, EXP G (the swap claim). The plan's "EXP G, which step of a worked product is wrong" is moved to Think harder (1) because the error-spotting is the lesson's check.
- **Holiday overlap: LOW.** The holiday course has no letter sum (owner decision 7) and no 3-digit by 2-digit work. H3 C5 and C6 (2 345 x 3, 4 236 / 6) are routine items not to reuse. Verdict: New. The Level 2 and 3 pre-flights use "AA + BB = CAC", "AB + AC = BCA" and the draft's BB + CB = CDA; Level 4 uses none of these.
- **Numbers.** 3 digits by 2 digits (to 999 x 99); letter sums with 2 or 3 digits and at most two carries.
- **Home materials.** Pencil, squared paper.
- **Kit.** Reuse K1 (max used 6 as trial digits).
- **Figures.** `area_model` (F2), `column` multiply and letter sums (F1).
- **Misconceptions.** Dropping the zero in the second partial product (shifting); treating two letters as one digit; a leading zero.
- **Needs.** F1, F2, N7 (digit-by-digit answers).
- **Safe to miss?** The Think harder and Go further letter sums yes (the Quest cave in lesson 20 is optional); the area model is repeated in the Remember of lesson 18.

### Lesson 12. Remainder Riddles (T2.2)

- **Big idea.** What is left over tells you where you are in a cycle.
- **Strand.** MOE P4 division with remainders (Four Operations 3.2, p. 37) and multiples (2.4). Cycles and days of the week are enrichment. Contest tag: remainders and cycles (19-19, 19-4).
- **Objective.** Find the nth item of a repeating pattern by the remainder; find a day of the week after n days; find a number from two remainder conditions. Think harder: 100 days later; two conditions; the nth letter. Go further: remainders one short of the divisor; a calendar year; three conditions.
- **Remember (6 min).** (1) 53 divided by 6 with counters. (2) The days of the week in order. (3) Skip-count in 5s to 50.
- **Start here (6).** (1) A bead pattern red, blue, blue, green, yellow repeats. What colour is the 20th bead? Yellow (W2.1). (2) The 47th bead: blue (W2.1). (3) Today is Friday: what day is it 10 days later? Monday. (4) 53 / 6 = 8 remainder 5. (5) The 3rd day of the month is a Monday: what day is the 24th? (6) The remainder when 100 is divided by 7: 2.
- **Think harder (4).** (1) **CTX.** It is Tuesday. What day will it be 100 days from now? Thursday (W2.2). (2) **LOG.** A number leaves remainder 2 when divided by 5 and remainder 3 when divided by 4. It is between 30 and 50. What is it? 47 (W2.3). (3) **PAT.** The letters of SINGAPORE are written again and again. Which letter is the 100th? S (W2.4). (4) The 1st of a month is a Wednesday: what day is the 29th? Wednesday.
- **Go further (3).** G1 **Beyond (named): "One Short Every Time".** A number leaves remainder 3 when divided by 4, 4 when divided by 5 and 5 when divided by 6. The smallest is 59, then every 60 (W2.5). Level note: contest-style (a common multiple minus 1). G2 **CTX.** 1 January 2027 is a Friday. What day is 1 January 2028? Saturday, because 2027 has 365 days, which is 52 weeks and 1 day (W2.6). G3 **LOG.** A number under 100 leaves 1 when divided by 3, 2 when divided by 4 and 3 when divided by 5: 58 (W2.7).
- **Non-routine.** PAT T, LOG T, CTX G.
- **Holiday overlap: HIGH (H1, H6).** H1 had eggs with 1 left over in 4s and 5s (41), the number 61 with 1 left for 2 to 6, the lockers; H6 had a robot turning 45 degrees (8 turns, 30 turns). Do not reuse 41, 61, "4s and 5s with 1 over" or the 30th turn. Second visit with new numbers and the calendar context.
- **Numbers.** Cycles of 3 to 9; days to 400; numbers under 200.
- **Home materials.** Pencil; a calendar page (in the book).
- **Kit.** None.
- **Figures.** `calendar` (exists), `seq` / bead row (`objects`, exists).
- **Misconceptions.** Counting the starting day as day 1 of the cycle; a remainder of 0 read as "the first item" rather than the last.
- **Needs.** none beyond the calendar.
- **Safe to miss?** Yes, fairly (lesson 30 and lesson 38 revisit cycles).

### Lesson 13. Bar Model Builder I (T2.3)

- **Big idea.** A picture of the story shows what is the same, what is more, and how many units there are.
- **Strand.** MOE P4 whole numbers and the problem-solving process (representing, pp. 13 to 14); the bar model is not named in the syllabus (Singapore schools teach it). The papers' spine: 214 of 807 non-routine items are unit chains (`p4_school_paper_patterns.md` section 0).
- **Objective.** Draw bars for "more than", "times as many", total and difference; find one unit; solve sum-and-difference. Think harder: unit chains with a total (twice as many, more than); sum and difference. Go further: make equal by transfers; a chain of three; "times as many" after a change.
- **Remember (6 min).** (1) 38 + 45. (2) One bar and its half. (3) 4 x 15 as four equal bars.
- **Start here (6).** (1) Ali has 38 stickers. Mei has 45 more than Ali. How many does Mei have, and how many altogether? 83 and 121 (W3.1). (2) The total is 154 and A has 28 more than B: B 63, A 91 (W3.1). (3) Ben has 3 times as many marbles as Kai. Together they have 248: Kai 62, Ben 186 (W3.1). (4) Mina has 52 and Ben 28: how many must Mina give for them to be equal? 12, and each then has 40. (5) A bar graph with no scale: 5 squares are 35 pupils; how many pupils is 1 square? 7. (6) Two prices and a difference.
- **Think harder (4).** (1) **EQ.** 3 small jars and 2 big jars hold 322 sweets, and a big jar holds twice as many as a small jar. How many sweets in a big jar? 92 (W3.2). (2) **EQ.** A sofa and 3 cushions cost $480. The sofa costs $120 more than a cushion. Find the cost of a cushion: $90, so the sofa is $210 (W3.3). (3) **CMP.** The sum of two numbers is 190 and their difference is 46. Find them: 118 and 72 (W3.4). (4) One more unit chain with money.
- **Go further (3).** G1 **Beyond (named): "Same in the End".** Three friends have $840 altogether. Ali spends $60, Bee earns $45 and Cy gives away $15, and then all three have the same. How much did each have at first? $330, $225, $285 (W3.5). Level note: unit equations are Primary 5 (p. 41); the bar picture is Primary 4. G2 **CMP.** 4A, 4B and 4C collected 1 245 cans. 4A collected 55 more than 4B and 4C collected 40 fewer than 4B: 465, 410, 370 (W3.6). G3 **EQ.** Mia has 4 times as many cards as Raj. After Mia gives Raj 36 cards, she has twice as many as he has. How many did each have at first? Raj 54 and Mia 216 (W3.7).
- **Non-routine.** EQ T x2, CMP T, CMP G, EQ G. This is the plan's one dedicated model lesson; the papers need more (lessons 11, 15, 17, 18, 27 to 29, 37 carry EQ items).
- **Holiday overlap: HIGH (H3, H5, H9, H10).** Do not reuse: 2 340 red and blue beads (4 times), 1 236 plates (3 times), Ali $56 more than Ben with $300, Ravi 3 times Siti gives 20, the pen $0.85 more than a pencil, Ali Ben Siti sharing $9.20, Class 4A and 4B boys and girls, four teams scoring 100, a cake $3 more than a drink with $40, Ben's uncle 4 times as old. Second visit: new contexts, one new structure (after a change).
- **Numbers.** Totals to 1 500; multipliers 2 to 5; money to $900.
- **Home materials.** Pencil, a ruler, squared paper.
- **Kit.** None cut; the book has bar-drawing grids.
- **Figures.** `bar_model` v2 (F4: up to 16 units, 4 bars, unknown labels, before and after).
- **Misconceptions.** Unequal bars for equal quantities; taking the difference as the total; halving the total when the bars are in a 1 : 3 ratio; forgetting the extra part in "$120 more".
- **Needs.** F4.
- **Safe to miss?** No: lessons 15, 17, 18, 20, 27, 28, 29 and 37 lean on the bar.

### Lesson 14. Fractions with Different Names (T2.4)

- **Big idea.** Make the denominators match, then add or subtract the parts.
- **Strand.** MOE P4 add and subtract fractions with denominators not above 12 and not more than two different denominators (Fractions 3.1, p. 37).
- **Objective.** Add and subtract like and related fractions on strips; add and subtract thirds and quarters by a common denominator; fill gaps in sums. Think harder: unlike fractions; a missing fraction; which two add to 1; complete a model. Go further: three unit fractions that make 1; two fractions from their sum and difference; three fractions in a story.
- **Remember (6 min).** (1) 1/2 and 2/4 on the wall. (2) 12 divided by 3 and by 4. (3) 3/5 + 1/5.
- **Start here (6).** (1) 1/2 + 1/4 = 3/4 on strips (W4.1). (2) 2/3 + 1/6 = 5/6 (W4.1). (3) 5/6 - 1/3 = 1/2 (W4.1). (4) 7/8 - 3/4 = 1/8 (W4.1). (5) 5/12 + 1/3 = 3/4 (W4.1). (6) Aisha ate 1/3 of a cake and Ben ate 1/6. What fraction did they eat? 1/2. Related denominators only here.
- **Think harder (4).** (1) 2/3 + 3/4 = 17/12 = 1 5/12 (W4.2). (2) **Fill the gap.** 5/6 - [ ] = 1/4: 7/12 (W4.2). (3) **LIST.** Which two of 1/3, 2/5, 3/4, 1/4, 3/5 and 7/12 add to 1? 3/4 and 1/4; 2/5 and 3/5 (W4.3). (4) **DIAG.** A half-drawn model for 3/4 - 1/6: complete and label it: 7/12 (W4.7).
- **Go further (3).** G1 **Beyond (named): "One in Three Pieces".** Which three different unit fractions with denominators up to 12 make 1? 1/2 + 1/3 + 1/6, the only way (W4.4). Level note: unit-fraction sums are secondary school; the arithmetic is Primary 4. G2 Two fractions add to 7/12 and differ by 1/12: 1/3 and 1/4 (W4.5). G3 **MULTI.** Ben read 1/3 of a book on Monday, 1/4 on Tuesday and 1/6 on Wednesday. He has 15 pages left. How many pages are in the book? 60 (W4.6). Three denominators is beyond the Primary 4 limit of two.
- **Non-routine.** LIST T, DIAG T, MULTI G.
- **Holiday overlap: HIGH (H4).** H4 had the "two fractions taken, the rest is a number" structure three times (C2 $25, C5 10 marbles, C7 5 sweets, C9 45 pages), 3/4 as 12/16, the tank. Do not reuse $25, 10 green, 5 left, 45 pages. G3 is the same structure with three fractions and three denominators: second visit with a twist.
- **Numbers.** Denominators to 12; answers to 1 7/12.
- **Home materials.** The K2 wall strips.
- **Kit.** Reuse K2 (max used 4 strips at once).
- **Figures.** `fraction` (F3).
- **Misconceptions.** Adding the denominators; keeping the old denominator after converting; subtracting the smaller from the larger part; forgetting to simplify.
- **Needs.** F3, K2.
- **Safe to miss?** No: lessons 15, 16 and 18 lean on adding fractions.

### Lesson 15. What Is Left? (T2.5)

- **Big idea.** A fraction of what remains is a fraction of a smaller whole, and a part tells you the whole.
- **Strand.** MOE P4 fraction as part of a set (Fractions 2.1, p. 37); "whole from a part" and "of the rest" are word-problem types the syllabus does not name (on level).
- **Objective.** Find a fraction of a set; find a whole from a part; find a fraction of the rest; work backwards through fraction steps. Think harder: tank problems; fraction of the rest then a difference; a backwards story. Go further: repeated fractions; a three-step chain.
- **Remember (6 min).** (1) 1/4 of 20 with counters. (2) 3/5 of 20. (3) A bar split into 5 equal parts with 2 labelled.
- **Start here (6).** (1) 3/8 of 72 = 27 (W5.1). (2) A shop sold 2/5 of 45 books; 27 are left (W5.1). (3) One bar: 3/4 of the class are 21 pupils; how many in the class? 28. (4) 1/3 of the ribbon is 8 m; the whole is 24 m. (5) A bar with the rest. (6) A story with a remainder as a fraction.
- **Think harder (4).** (1) **BACK.** A tank is 3/7 full. 84 more litres fill it. What is the capacity? 147 l (W5.1). (2) **MULTI.** A shop had 480 books. It sold 3/8 on Monday and 2/5 of the rest on Tuesday. How many more were sold on Monday than on Tuesday? 60 (W5.2). (3) **BACK.** Aisha spent 1/3 of her money on a book and $8 on pens. She had $24 left. How much had she at first? $48 (W5.6). (4) A fraction story with a bar and a table.
- **Go further (3).** G1 **Beyond (named): "Every Day a Third".** Each day Mei eats 1/3 of the cake that is left. After 3 days 40 pieces are left. How many pieces were there? 135 (W5.4). Level note: repeated fractions foreshadow powers (secondary). G2 **BACK.** A farmer sold 1/3 of his mangoes on Monday, 1/4 of the rest on Tuesday and 20 on Wednesday, leaving 40. How many mangoes at first? 120 (W5.3). G3 **BACK.** Wei gave 1/4 of his cards to Ali and 1/3 of the rest to Ben, and had 36 left. How many at first? 72 (W5.5).
- **Non-routine.** BACK T, MULTI T, BACK G. SASMO 19-25 (the Lego pieces) is prepared by G2 and G3; those two are original contexts.
- **Holiday overlap: HIGH (H4, H3, H10).** Do not reuse 40 beads with 3/8 blue, "2/5 of a number is 16", Siti's 150-page book (2/5 and half the rest, 45 left), a tank 3/8 to 3/4, half and $6 and half and $9 (48), half and 2 more stickers (32). Second visit.
- **Numbers.** Denominators 2 to 12; totals to 500.
- **Home materials.** Pencil, squared paper.
- **Kit.** None cut (bar grids are printed).
- **Figures.** `bar_model` (F4), `fraction` strip (F3).
- **Misconceptions.** Taking the fraction of the whole instead of the rest; adding the fractions when one is "of the rest"; answering the wrong end of a backwards chain.
- **Needs.** F3, F4.
- **Safe to miss?** No: lesson 27 (4.6) leans on backwards chains.

### Lesson 16. Mixed Numbers on the Line (T2.6)

- **Big idea.** Count in pieces past the whole, and a number line shows where the wholes are.
- **Strand.** MOE P4 mixed numbers and improper fractions and their relationship (Fractions 1.1, p. 37). Adding and subtracting mixed numbers is **Primary 5** (Fractions, Four Operations 2.1, p. 41) and is labelled a preview.
- **Objective.** Write an improper fraction as a mixed number and back; place mixed numbers on a line; (preview) add and subtract mixed numbers with related denominators. Think harder: the preview with borrowing; steps along a line; find the start. Go further: a gap between two mixed numbers; a magic square of halves; counting mixed numbers.
- **Remember (6 min).** (1) 7/4 as one whole and 3 quarters on a strip. (2) 3 wholes as thirds. (3) Count in quarters from 0 to 2.
- **Start here (6).** (1) Place 2 3/4 on a line marked in quarters. (2) 17/5 = 3 2/5 (W6.1). (3) 4 1/3 = 13/3 (W6.1). (4) Jumps along a line: 1 3/4 + 1/2 (2 1/4). (5) Which is greater, 9/4 or 2 1/3? (6) Mixed numbers in a measurement story (2 1/2 m of ribbon).
- **Think harder (4).** (1) **Preview.** 2 5/8 + 1 3/4 = 4 3/8 (W6.1). (2) 5 1/4 - 2 3/4 = 2 1/2, borrowing a whole (W6.1). (3) **PAT.** A number line starts at 1 1/2 and jumps 3/4 each time. The 5th number is 4 1/2 (W6.2). (4) **BACK.** After adding 2 3/4 and taking away 1 1/2, the answer is 6 1/4. What was the start? 5 (W6.5).
- **Go further (3).** G1 **Beyond (named): "Half-Step Magic Square".** Fill the missing cells of a 3 by 3 square using 1/2, 1, 1 1/2 up to 4 1/2 so that every row, column and diagonal totals 7 1/2 (W6.3, W6.4). Level note: contest-style; mixed-number addition is Primary 5. G2 **CMP.** What is the gap between 7 1/6 and 3 2/3? 3 1/2 (W6.2). G3 How many mixed numbers with denominator 8 lie strictly between 2 3/8 and 3 1/4? 6 (W6.6).
- **Non-routine.** PAT T, CMP G, BACK T.
- **Holiday overlap: HIGH (H4).** H4 converted 11 slices into thirds (3 2/3), 11 quarters (2 3/4), 7/4 against 1 5/8, 4 3/4 m ribbon in quarters. Do not reuse 11 slices, 7/4, 4 3/4 m. Second visit; the addition and subtraction of mixed numbers is new.
- **Numbers.** Denominators 2 to 8 and 12; sums to 8.
- **Home materials.** The K2 wall strips; the number-line page.
- **Kit.** Reuse K2 (max used 8).
- **Figures.** `number_line` with mixed labels (F6), `fraction` (F3).
- **Misconceptions.** Writing 3 2/5 as 3 + 2 + 5; borrowing 1 as 1/4 instead of 4/4; placing 2 3/4 at 2.3.
- **Needs.** F3, F6, K2.
- **Safe to miss?** Yes for the preview; the conversion is repeated in lesson 25.

### Lesson 17. Decimals in Money and Measures (T2.7)

- **Big idea.** The same decimal does two jobs, money and measure, and the cheapest buy is found by the cost of one.
- **Strand.** MOE P4 add and subtract decimals to 2 places (Decimals 2.1, p. 38); money in dollars and cents; converting m, kg and l to cm, g and ml **in decimal form is Primary 5** (Decimals 1.2, p. 41) and is the beyond item.
- **Objective.** Add and subtract money and measures; find the cost of one and compare packs; solve a decimal bar model; draw a mass diagram. Think harder: best buy; pack prices; a decimal total with a difference; a mass diagram with units. Go further: conversions; whole packs only; pay by the hour; litres from jugs and bottles.
- **Remember (6 min).** (1) $3.45 as 345 cents. (2) 4.75 + 2.9 aligned on the decimal point. (3) 1 000 g in 1 kg.
- **Start here (6).** (1) $3.45 + $2.80 = $6.25 (W7.1). (2) $10 - $6.35 = $3.65 (W7.1). (3) 4.75 kg + 2.9 kg = 7.65 kg (W7.1). (4) 5 l - 2.36 l = 2.64 l (W7.1). (5) Which is greater, $2.09 or $2.9? (6) A shopping story with three items and change.
- **Think harder (4).** (1) **CTX best buy.** Juice is sold 6 for $4.80, 4 for $3.40 and 10 for $7.50. Which is the best buy? 10 for $7.50 at $0.75 each against $0.80 and $0.85 (W7.2). (2) **CTX pack prices.** Notebooks are 3 for $4.50 and rulers 4 for $3.20. Zoe buys the same number of each, as few as she can. How much? 12 of each, $27.60 (W7.3). (3) **EQ.** 2 books and a pen cost $23.30. A book costs $5.20 more than the pen. Find the price of the pen: $4.30, and the book is $9.50 (W7.5). (4) **DIAG.** A bag of rice and 3 identical tins weigh 4.2 kg. The rice is 3 times as heavy as one tin. How heavy is the rice? 2.1 kg (W7.4).
- **Go further (3).** G1 **Beyond (named): "Unit Switch".** 2.35 m is 235 cm, 7.5 kg is 7 500 g, 3.04 l is 3 040 ml, and 4 kg 70 g is 4.07 kg (W7.6). Level note: Primary 5 (p. 41). G2 **CTX.** Cans are sold in packs of 6 for $5.40 and 8 for $6.80. Kai needs exactly 24 cans and buys whole packs only. The only ways are 4 packs of 6 or 3 packs of 8; the cheaper is $20.40 (W7.7, W7.8). G3 **CTX.** Lena works from 8:20 am to 5:05 pm at $12 for every hour, break time included. How much does she earn? 8.75 hours, $105 (W7.9). **DIAG** option: a 3.6 l jug fills 4 cups exactly; 6 cups and 2 jugs hold 12.6 l (W7.10).
- **Non-routine.** CTX T x2, EQ T, DIAG T, CTX G x2.
- **Holiday overlap: HIGH (H5).** Do not reuse $3.47, 3 pens at $1.25, 4 notebooks and $2.60 change, the pen $0.85 more than a pencil, $9.20 shared three ways, Mei 1.38 m and Ben 0.15 m taller, the jug 1.45 kg and 0.85 kg, 3 apples and a pear 0.95 kg. Second visit; best buy, conversion and hourly pay are new.
- **Numbers.** Amounts to $30; masses to 10 kg; 2 decimal places.
- **Home materials.** Pencil; no play money.
- **Kit.** None cut.
- **Figures.** `bar_model` with money labels (F4), `scale_dial` / mass diagram (F18).
- **Misconceptions.** Aligning the right-hand digits; $0.75 recorded as 75; the cheapest pack taken as the one with the lowest price; hours and minutes subtracted as decimals.
- **Needs.** F4, F18, N7.
- **Safe to miss?** Not the first half; the beyond conversions are repeated in lesson 30.

### Lesson 18. Decimals Times and Shares (T2.8)

- **Big idea.** A decimal times a whole number is a product of tenths or hundredths, and a share of a decimal is a decimal.
- **Strand.** MOE P4 multiply and divide decimals (to 2 places) by a 1-digit whole number (Decimals 2.2, p. 38). A decimal times a decimal is **Primary 5** (the beyond item).
- **Objective.** Multiply and divide decimals by a whole number; check by estimating; solve a decimal unit chain. Think harder: share a decimal then a fraction. Go further: a decimal unit chain with a change; a missing digit.
- **Remember (6 min).** (1) 3 x 245 = 735. (2) 72 divided by 4. (3) $9.60 as 960 cents.
- **Start here (6).** (1) 3 x $2.45 = $7.35 (W8.1). (2) 4 x 0.75 = 3 (W8.1). (3) 7.2 / 4 = 1.8 (W8.1). (4) $9.60 shared by 4 is $2.40 (W8.1). (5) Estimate 6 x 3.9 (about 24), exact 23.4. (6) A story with a price per item.
- **Think harder (4).** (1) **MULTI.** Mrs Tan has 6.4 kg of flour. She uses 1/4 of it and packs the rest into 3 equal bags. How much flour in a bag? 1.6 kg used, 4.8 kg left, 1.6 kg in each bag (W8.2). (2) A share of money with a fraction. (3) A decimal division with a zero in the quotient. (4) A unit chain with whole numbers.
- **Go further (3).** G1 **Beyond (named): "A Tenth of a Tenth".** 0.3 x 0.4 = 0.12, shown on a hundred grid (W8.4). Level note: decimal by decimal is Primary 5. G2 **EQ.** Mr Ong has 3.6 l more paint than Mr Pang. He uses 5.4 l. Then Mr Pang has twice as much as Mr Ong has left. How much paint did Mr Ong have at first? 7.2 l (and Mr Pang 3.6 l, W8.3). G3 **LIST.** 3 . [ ] 6 x 7 = 2 [ ] . 1 2: the digits are 1 and 2 (3.16 x 7 = 22.12, W8.5).
- **Non-routine.** MULTI T, EQ G, LIST G. The plan's EX-EQ-4 is replaced (the Term 4 version has different numbers).
- **Holiday overlap: MED (H5).** Do not reuse the 4.8 m ribbon in 6 pieces, $9.20 shared, $1.25 each, 3.69 digit cards. Second visit.
- **Numbers.** Decimals to 2 places times 2 to 9; shares by 2 to 9.
- **Home materials.** Pencil, squared paper.
- **Kit.** None cut; hundred grids printed.
- **Figures.** `grid_100` (F20), `bar_model` (F4), `column` (F1).
- **Misconceptions.** Dropping the decimal point; 4 x 0.75 = 0.300; carrying the point wrongly in a share; thinking "share" always divides by the larger number.
- **Needs.** F1, F4, F20.
- **Safe to miss?** No: lesson 19 leans on division of decimals.

### Lesson 19. When Division Doesn't Come Out Even (T2.9, added)

- **Big idea.** Keep dividing, then round sensibly for the purpose.
- **Strand.** MOE P4 a whole number divided by a whole number with a decimal quotient (Decimals 3.2) and rounding answers to a stated accuracy (3.3), both p. 38.
- **Objective.** Divide a whole number by a whole number to a decimal quotient; round to the nearest 10 cents, 1 decimal place or whole number; decide when to round up. Think harder: bounds of a rounded number; round up for buses and packs. Go further: a never-ending decimal; does the answer make sense?
- **Remember (6 min).** (1) 7 divided by 4 with coins. (2) 0.5 as 50 cents. (3) Round 6.28 to 1 decimal place.
- **Start here (6).** (1) 7 / 4 = 1.75 (W9.1). (2) 9 / 5 = 1.8 (W9.1). (3) 3 / 8 = 0.375 (W9.1). (4) Share $7 among 3 and round to the nearest cent: $2.33 (W9.1). (5) 2 / 3 to 2 decimal places: 0.67 (W9.1). (6) Round 9 / 8 = 1.125 to 1 decimal place: 1.1 (W9.6).
- **Think harder (4).** (1) **LIST.** A number with 2 decimal places rounds to 6.3 to the nearest tenth. What are the smallest and the greatest? 6.25 and 6.34 (W9.2). (2) **CTX.** 1 000 pupils go on a trip in buses of 45. How many buses? 22.2 means 23 buses (W9.3). (3) Round $2.33 to the nearest 10 cents ($2.30) and to the nearest dollar ($2). (4) A pack story that needs rounding up.
- **Go further (3).** G1 **Beyond (named): "Never-Ending Decimals".** 1/7 = 0.142857 142857 ...; the digits repeat in blocks of 6, so the 20th digit is 4 (W9.4). Level note: recurring decimals are secondary school. G2 Two different shares can round to the same price: $5 shared by 3 and $5.02 shared by 3 are both $1.67 to the nearest cent (W9.5). Why does 5 / 3 never come out exactly? G3 **POSE.** Rani says 100 / 8 = 12.5 buses so 12 buses are enough. Is she right? No: 13 buses.
- **Non-routine.** LIST T, CTX T, POSE G. Verified: W9.1 to W9.5.
- **Holiday overlap: LOW (H5 S2, S10, C4 round to the nearest whole number and 1 decimal place).** New topic (division with a decimal quotient). Do not reuse 9.50 and 10.49 or 7.35 and 7.44.
- **Numbers.** Dividends to 1 000, divisors to 9 and 45; quotients to 3 decimal places.
- **Home materials.** Pencil.
- **Kit.** None.
- **Figures.** `column` long division (F1).
- **Misconceptions.** Stopping at the remainder; rounding 22.2 buses down; writing 1.75 as 1.7.
- **Needs.** F1.
- **Safe to miss?** Yes, the safest of Term 2 (the plan's added lesson).

### Lesson 20. Challenge Day 2, with Mi's Challenge Quest (T2.10)

- **Big idea.** Choose a model: a bar, a fraction strip or a riddle table.
- **Strand.** Heuristics (p. 13). The Quest follows (section 6).
- **Objective.** Solve a bar-model story, a fraction-of-the-rest chain and a decimal riddle. The Quest carries a gate for each of lessons 11 to 19.
- **Remember (6 min).** (1) A bar with 3 units. (2) 1/4 of 120. (3) 1.55 and 1.64 to the nearest tenth.
- **Start here (5).** (1) A scarf costs $13 more than a hat, and together they cost $59: hat $23, scarf $36 (W10.4). (2) A bar-model story with a total. (3) A one-step fraction of a quantity. (4) A decimal sum. (5) A division with a remainder.
- **Think harder (3).** (1) **MULTI.** 180 sweets: 1/3 are eaten and 1/4 of the rest are given away. How many are left? 90 (Q2.5). (2) **EQ.** Dev has 5 times as many cards as Eva. After Dev gives Eva 24 cards they have the same number. How many did Dev have? 60 (and Eva 12, W10.5). (3) A fraction story with a table.
- **Go further (3).** G1 **Beyond (named): "Two Clues, Two Answers".** I have 2 decimal places and I am between 1 and 2. I round to 1.6 to the nearest tenth and my digits add to 11. Find all the numbers: 1.55 and 1.64 (W10.6). G2 **CHAL.** Make up a decimal riddle that has exactly two answers. G3 **MULTI.** A mixed contest set.
- **Non-routine.** MULTI T, EQ T, CHAL G. The plan's check is replaced by the Quest.
- **Holiday overlap: HIGH (H10).** Same as lesson 10; a new context is the rule.
- **Numbers.** Totals to 300; decimals to 2 places.
- **Home materials.** Pencil; a quest partner; the Quest Log stays closed in Book 4.
- **Kit.** None.
- **Figures.** `bar_model` (F4).
- **Needs.** Quest block (section 6), N3.
- **Safe to miss?** The body yes; the Quest is the part to protect.

---

## Term 3: Explain why (lessons 21 to 30)

Cold joining: yes. The Remember warm-ups carry naming a cube and a cuboid, the area of a rectangle by counting squares, and a line of symmetry on a folded page. Angles are met once (lesson 22), so lesson 22 does not assume an earlier angle lesson. A child who has done only the June holiday course (H1 to H10) arrives here at lesson 21 and has met every topic as a puzzle. **Safest to skip or make up: lesson 29** (the added lesson); then lessons 25 and 27; hardest to miss: 22, 23 and 24. Lesson 30 hosts the Quest. This is the term where the plan's lessons collide hardest with the holiday course (H6, H7, H8): section 13.

### Lesson 21. Solids and Their Nets (T3.1)

- **Big idea.** Build, then flatten: a net shows every face of a solid once.
- **Strand.** MOE P4 nets of cube, cuboid, cone, cylinder, prism and pyramid; identify the solid a net makes; 2D drawings of solids (Geometry 4.1 to 4.4, p. 39).
- **Objective.** Name faces, edges and vertices; match a solid to its net; decide which net folds; use faces, edges and vertices in a table. Think harder: take one square away to leave a cube net; a table for prisms and pyramids; which nets fold. Go further: Euler's check; opposite faces on a lettered net; a cuboid's net as a count of squares.
- **Remember (6 min).** (1) A cube has 6 faces; count them on a real box. (2) A square, a rectangle and a triangle. (3) Fold a paper rectangle into a tube.
- **Start here (6).** (1) Name the solid and count its faces, edges and vertices: a cuboid has 6, 12 and 8. (2) A triangular prism has 5, 9 and 6 (X1.4). (3) Match four solids to four nets. (4) Which solid has a net of 4 triangles and 1 square? A square pyramid. (5) The net of a cylinder has 2 circles and 1 rectangle. (6) How many unit squares does the net of a 4 by 2 by 1 cuboid cover? 28 (X1.6).
- **Think harder (4).** (1) **EXP.** Seven squares are drawn in a cross-like shape. Cross out one square so that the rest folds into a cube. Find two different squares you could cross out (exactly two work, X1.3). (2) **TAB.** Complete a table of faces, edges and vertices for a triangular prism, a pentagonal prism, a square pyramid and a hexagonal pyramid: 5, 9, 6; 7, 15, 10; 5, 8, 5; 7, 12, 7 (X1.4, X1.5). (3) Which of four 6-square shapes is a net of a cube? (The 11 nets among the 35 six-square shapes were counted, X1.1; the author fixes the four shapes and checks them with the fold function.) (4) A net of a triangular prism: which drawing has 2 triangles and 3 rectangles in the right places?
- **Go further (3).** G1 **Beyond (named): "Euler's Check".** For every solid in the table, faces + vertices - edges = 2 (X1.4). Level note: secondary school. G2 **DIAG.** A net of a cube has six squares lettered A to F in a staircase (A and B side by side, then C and D one row down, then E and F one more). Which letter is opposite A, B and C? D, E and F (X1.2). Letters are used so the answer is not "the faces add to 7". G3 The net of a 5 by 3 by 2 cuboid covers how many unit squares? 62 (X1.6).
- **Non-routine.** EXP T, TAB T, DIAG G.
- **Holiday overlap: HIGH (H8).** H8 did the 11 nets of a cube, "five in a row cannot fold", a 2 by 3 block, opposite faces on a dice (sum 7), glued and stacked dice, the open box (8 of 12), a 3 by 2 by 1 cuboid (22 squares). Do not reuse any, and the plan's T "which six-square shapes fold into a cube (find all)" and G "opposite faces on a dice net" are replaced. Verdict: Change.
- **Numbers.** Solids up to 12 edges and 7 faces in the table.
- **Home materials.** Pencil, glue stick or tape (grown-up), the cut nets.
- **Kit (K4 nets).** 4 nets on 2 pages: cube (the lettered staircase), cuboid 4 by 2 by 1, triangular prism, square pyramid, each with tabs. Supplied 4; max used 4. Cut 4. Net edges scale with the page (94.3 percent), which does not matter for folding.
- **Figures.** `solid` and `net` (F9).
- **Misconceptions.** Counting tabs as faces; counting only visible edges; thinking any 6 squares fold; opposite faces taken as neighbours.
- **Needs.** F9, K4.
- **Safe to miss?** Fairly safe; lesson 27 uses the vocabulary.

### Lesson 22. Angle Detectives (T3.2)

- **Big idea.** An angle measures turning, and a protractor and a compass are two ways to read a turn.
- **Strand.** MOE P4 angles: notation, measure in degrees, draw an angle of given size (Geometry 1.1 to 1.3, p. 39). Missing angles in a fan, on a line and around a point are **Primary 5** (Angles 1.1 to 1.4, p. 42) and are labelled previews. Compass turns are enrichment (the syllabus names no compass or turns outcome).
- **Objective.** Name angles with ∠ABC; estimate, measure and draw angles to the nearest 5 degrees; find missing angles (preview); follow and reverse turns on an 8-point compass. Think harder: draw 125 degrees; missing angles; reverse a turn; three turns in a row. Go further: triangle total; a turn that ends facing a stated way; angles in a ratio.
- **Remember (6 min).** (1) The corner of a page is a right angle, 90 degrees. (2) A half turn is 180 degrees. (3) The four main compass points (re-taught with a card).
- **Start here (6).** (1) Write the name of an angle with three letters, ∠ABC. (2) Estimate, then measure, three angles (about 35, 110 and 65 degrees). (3) Draw ∠PQR = 65 degrees with a ruler and a protractor. (4) Circle the acute and the obtuse angles. (5) Ali faces east and turns a quarter turn clockwise: south. (6) How many degrees is 3 right angles? 270.
- **Think harder (4).** (1) Draw an angle of 125 degrees with one ray pointing left. (2) **GEO (preview).** Missing angles: 90 - (35 + 28) = 27 in a right angle; 180 - (65 + 45) = 70 on a line; 360 - (130 + 95 + 60) = 75 around a point (X2.5). (3) **BACK.** After turning 225 degrees anticlockwise Ravi faces south-east. Which way did he face at first? North (X2.2). (4) **GEO.** Ben faces north-west, turns 135 degrees clockwise and then 90 degrees anticlockwise. Which way does he face? North (X2.1). A longer chain: starting north, turn 225 degrees clockwise, 90 degrees anticlockwise, 45 degrees clockwise: south (X2.8).
- **Go further (3).** G1 **Beyond (named): "Triangle Total".** Measure the three angles of any drawn triangle and add them: about 180 degrees every time, for example 50 + 60 + 70 (X2.6). Level note: a Primary 5 and secondary idea. G2 **BACK/LOG.** Kai faces east and turns 135 degrees clockwise. Then he turns anticlockwise to face north. How many degrees is his second turn? 225 (X2.9). G3 Angle ABC is 48 degrees. Ray BD makes angle ABD three times angle DBC. Find both: 36 and 12 (X2.10).
- **Non-routine.** BACK T, GEO T, LOG G (replaced by a turn chain). The plan's "two clock hands" (LOG G) is H6.
- **Holiday overlap: HIGH, nearly total (H6).** H6 did robot turns, clock angles at o'clock, half past and ten past times, 6 degrees a minute, 30 degrees a gap, the compass with SE and 225, mirror times (2 and 10), fan angles (25, 40 and 25), a square corner cut (64 and 26, 4 times, 15 30 45), two squares overlapping (160). Do not reuse any. The plan's "turns of the minute hand" and "two clock hands" are H6 and are dropped. This lesson is built on the protractor skill (measure and draw), notation and new compass chains. Verdict: Change.
- **Numbers.** Angles to 180 degrees in steps of 5; turns in multiples of 45 degrees.
- **Home materials.** Protractor, ruler, pencil. No protractor? tell the tutor; the lesson then uses the compass card and the right-angle checker.
- **Kit (K5 compass).** A compass rose card and a loose arrow: 2 pieces. Max used 2. Cut 2. Reuse K3 from lesson 6.
- **Figures.** `angle`, `compass`, `fan` (F7). A drawn protractor is shown only in worked examples, never to be measured on paper.
- **Misconceptions.** Reading the wrong scale of the protractor; a 5-degree error counted as wrong; turning clockwise when told anticlockwise.
- **Needs.** F7, K5.
- **Safe to miss?** No: this is the only angle lesson of the year.

### Lesson 23. Rectangle Rules (T3.3)

- **Big idea.** Fix one thing and vary another: the same area can have different perimeters.
- **Strand.** MOE P4 find a missing side of a rectangle from its area or perimeter; the side of a square from its area or perimeter (Area and Perimeter, p. 39).
- **Objective.** Find a missing side; list rectangles of a given area; compare perimeters; use identical squares in a row. Think harder: identical squares from a perimeter; all rectangles of an area; a table at fixed perimeter. Go further: area and perimeter given; an area with a length difference.
- **Remember (6 min).** (1) Area of a 6 by 5 rectangle. (2) Perimeter of a 6 by 5 rectangle. (3) 8 x 8.
- **Start here (6).** (1) Area 84 cm2 and width 7 cm: length 12 cm (X3.1). (2) Perimeter 54 cm and length 16 cm: width 11 cm (X3.1). (3) A square has area 64 cm2: side 8 cm (X3.1). (4) A square has perimeter 36 cm: side 9 cm (X3.1). (5) List the rectangles with whole-cm sides and area 18 cm2: 1 by 18, 2 by 9, 3 by 6. (6) Their perimeters: 38, 22, 18.
- **Think harder (4).** (1) **GEO.** 7 identical squares in a row make a rectangle of perimeter 144 cm. Find its length and area. 63 cm and 567 cm2 (X3.2). (2) **LIST.** List all rectangles with whole-cm sides and area 72 cm2. Which has the smallest perimeter? 8 by 9, 34 cm (X3.3). (3) A table of the rectangles with perimeter 36 cm (1 by 17 to 9 by 9) and their areas: 17, 32, 45, 56, 65, 72, 77, 80, 81 (X3.5). (4) A rectangle is twice as long as it is wide and its perimeter is 54 cm: 9 cm by 18 cm (X3.8).
- **Go further (3).** G1 **Beyond (named): "Squares Win".** For perimeter 36 cm the area is 81 minus a square number: 81, 80, 77, 72, ... (81 - 0, 81 - 1, 81 - 4, 81 - 9, ...), so the square is the largest (X3.5). Level note: an algebra identity, secondary school. G2 **GC.** A rectangle has area 135 cm2 and perimeter 48 cm. Find its sides: 9 cm and 15 cm (X3.4). G3 A rectangle is 4 cm longer than it is wide and has area 117 cm2. Find its perimeter: 44 cm (X3.6, X3.7).
- **Non-routine.** GEO T, LIST T, GC G.
- **Holiday overlap: HIGH, nearly total (H7).** H7 did 12 tiles, all rectangles of area 30, perimeter 20 (largest 25), area 40 and perimeter 26, area 36 (six rectangles, 24 smallest), 8 tiles (12 to 18), area 56 and length 8, 24 m of fencing with and without a wall. Do not reuse these numbers. The plan's S, T, G (area 24, smallest perimeter, perimeter 20) are H7's explore, S1 and S2. Verdict: Change.
- **Numbers.** Sides 1 to 72 cm, areas to 600 cm2.
- **Home materials.** Pencil, squared paper (in the book).
- **Kit.** None (squared paper pages).
- **Figures.** `shape2d` with side labels (F8).
- **Misconceptions.** Adding length and width and calling it the area; halving the perimeter and forgetting to subtract the other side; a rectangle 9 by 8 counted different from 8 by 9.
- **Needs.** F8.
- **Safe to miss?** No: lessons 24 and 29 lean on it.

### Lesson 24. Frames and Paths (T3.4)

- **Big idea.** Subtract the hole: a frame is the big minus the small.
- **Strand.** MOE P4 area and perimeter of composite figures made of rectangles and squares (Area and Perimeter, p. 39).
- **Objective.** Find the area of an L-shape two ways; the perimeter by pushing the steps out; the area of a frame or a path; joined and folded identical pieces. Think harder: three identical rectangles; a border; a folded paper. Go further: border counts; a square folded twice.
- **Remember (6 min).** (1) 12 x 9 and 5 x 4. (2) 108 - 20. (3) Perimeter of a 12 by 9 rectangle.
- **Start here (6).** (1) An L-shape is a 12 cm by 9 cm rectangle with a 5 cm by 4 cm corner cut out. Its area is 88 cm2 (X4.1). (2) The same area by adding two rectangles. (3) Its perimeter is the same as the rectangle: 42 cm (X4.1). (4) A photo 20 cm by 15 cm has a frame 3 cm wide. The frame's area is 246 cm2 (X4.1). (5) A path 1 m wide goes round a lawn 12 m by 8 m: the path's area is 44 m2 (X4.7). (6) Find a missing length in a composite figure.
- **Think harder (4).** (1) **GEO.** Three identical rectangles are placed side by side, long sides touching, to form a square. Each rectangle has perimeter 40 cm. Find the rectangle and the square's perimeter and area: 15 cm by 5 cm; 60 cm; 225 cm2 (X4.2, X4.3). (2) **CTX.** A pool 18 m by 10 m has a path 3 m wide all round. Find the area of the path: 204 m2 (X4.7). (3) **DIAG.** A rectangular sheet is folded in half so that its longer side, 30 cm, becomes 15 cm. The folded piece has perimeter 62 cm. Find the shorter side of the sheet: 16 cm (X4.4). (4) A composite figure with two missing lengths.
- **Go further (3).** G1 **Beyond (named): "Border Count".** The border of an n by n square has 4n - 4 unit squares, and this equals n x n - (n - 2) x (n - 2) (X4.6). Level note: an algebra pattern, secondary school. G2 **DIAG.** A square paper of side 24 cm is folded in half and in half again. What are the area (144 cm2) and perimeter (48 cm) of the folded square, and what fraction of the original area is it? 1/4 (X4.5). G3 A frame problem with two different widths.
- **Non-routine.** GEO T, CTX T, DIAG G.
- **Holiday overlap: HIGH (H7).** H7 had squares 3 cm cut from the corners of a 12 by 8 rectangle, three squares side by side, a path 2 m round a 10 by 6 lawn, a 2 by 4 gap in a 10 by 6 rectangle, a plus shape, two crossing paths in a 10 by 8 garden. Do not reuse these figures. Verdict: Change (new figures; joined and folded pieces are the paper's pattern).
- **Numbers.** Sides to 30 cm; areas to 700 cm2.
- **Home materials.** Pencil, squared paper, a sheet of paper to fold.
- **Kit.** None.
- **Figures.** `shape2d` composite with dimension labels, `joined` pieces, `folded` (F8).
- **Misconceptions.** Subtracting widths instead of areas; counting the inner perimeter of a frame; a fold treated as a cut.
- **Needs.** F8.
- **Safe to miss?** No: lesson 29 leans on joined pieces.

### Lesson 25. Cut and Rebuild (T3.5)

- **Big idea.** Area does not change when pieces move; perimeter can.
- **Strand.** MOE P4 composite figures (p. 39); dissection and tangram are enrichment (Intl: HK P4).
- **Objective.** Use the seven tangram pieces to build shapes; compare area and perimeter before and after a cut; decide true or false. Think harder: cut a rectangle and rebuild it; same area or same perimeter. Go further: a paradox of areas; two cuts, three pieces.
- **Remember (6 min).** (1) Area of a 8 by 3 rectangle: 24. (2) Perimeter of the same: 22. (3) Name the tangram pieces by shape.
- **Start here (6).** (1) The tangram pieces, in units where the small triangle is 1: two large triangles of 4, a medium triangle of 2, two small triangles of 1, a square of 2 and a parallelogram of 2, so 16 in all (X5.1). (2) Make the big square from all 7 pieces. (3) Make the same square from 5 pieces. (4) Which pieces have the same area? (5) Cover a rectangle of area 8. (6) Colour-free: hatch the pieces that make half the square.
- **Think harder (4).** (1) **GEO.** An 8 cm by 3 cm rectangle is cut into two 4 by 3 pieces which are put together to make a 4 by 6 rectangle. The area stays 24 cm2; the perimeter goes from 22 cm to 20 cm (X5.3). (2) **EXP.** Same area means same perimeter: true, false or not possible to tell? False (X5.3). (3) Cut an L-shape into two identical pieces. (4) A shape made from the tangram with a given perimeter.
- **Go further (3).** G1 **Beyond (named): "Where Did the Square Go?".** An 8 by 8 square (64) is cut into four pieces that seem to make a 5 by 13 rectangle (65). Explain why the extra square cannot exist: the pieces leave a thin gap along the diagonal (X5.2, X5.4 Fibonacci numbers). Level note: secondary school (Fibonacci). G2 **GEO.** Make two straight cuts in an 8 by 3 rectangle to get three pieces that rebuild a 6 by 4 rectangle (6 by 3 and two 1 by 3 strips, X5.5). G3 Pose a cut-and-rebuild puzzle for a partner.
- **Non-routine.** GEO T, EXP T, GEO G.
- **Holiday overlap: MED (H7 C9, S7).** H7 had a 9 by 4 rectangle cut into a 6 by 6 square, and a 6 by 4 rectangle restacked as 12 by 2 (8 cm more perimeter). Do not reuse these. Verdict: Change.
- **Numbers.** Areas to 64.
- **Home materials.** Scissors for the grown-up; pencil; the tangram.
- **Kit (K6 tangram).** 7 pieces from one 10 cm square. Supplied 7; max used 7. Cut 7.
- **Figures.** `tangram` and `dissection` (F17).
- **Misconceptions.** Believing a longer perimeter means more area; counting the gap-free paradox as a trick of the eyes.
- **Needs.** F17, K6.
- **Safe to miss?** Yes (the plan's enrichment).

### Lesson 26. Mirror Patterns (T3.6)

- **Big idea.** A line of symmetry is a fold that makes two halves match.
- **Strand.** MOE P4 line symmetry: identify symmetric figures, decide if a line is a line of symmetry, complete a symmetric figure on a square grid (Geometry 3.1 to 3.3, p. 39).
- **Objective.** Find lines of symmetry of polygons and flags; complete a figure about a vertical, horizontal or diagonal line; count lines of symmetry. Think harder: how many lines, and why; a diagonal mirror; complete a pattern. Go further: a shape with a half-turn but no line; several lines.
- **Remember (6 min).** (1) Fold a square in half. (2) A rectangle has 2 lines and a square has 4. (3) Reflect a point across a line.
- **Start here (6).** (1) Is the dashed line a line of symmetry? (2) Complete a figure about a vertical line on a 6 by 6 grid. (3) Complete about a horizontal line. (4) Flags: which flag has exactly one line? (5) How many lines does an equilateral triangle have? 3. (6) A kite has 1; a parallelogram has none.
- **Think harder (4).** (1) **EXP.** How many lines of symmetry has a regular pentagon, and why? 5, one through each corner and the middle of the opposite side. (2) Complete a figure about a diagonal line. (3) **PAT.** Complete the tile pattern on a 4 by 4 grid; a given pattern of 8 shaded squares has 4 lines (X6.3). (4) A figure with one line, completed to have two.
- **Go further (3).** G1 **Beyond (named): "Turn It Half".** The S-shaped tetromino looks the same after a half turn but has no line of symmetry (X6.1, X6.2). Level note: rotational symmetry is secondary school. G2 **DIAG.** Design a 4 by 4 pattern with exactly 2 lines of symmetry. G3 How many lines of symmetry does a 3-square L-tromino on a grid have? 1, a diagonal (X6.4).
- **Non-routine.** EXP T, PAT T, DIAG G.
- **Holiday overlap: HIGH (H8).** H8 did capital letters A, B, F, H, L, T, the 5 four-square shapes (T has 1), 3 by 3 shading with 1 and 2 lines, 2 squares on the up-down line (6 ways), 5 squares with 4 lines (X and plus). Do not reuse. This lesson uses polygons, flags and 4 by 4 and 6 by 6 grids. Verdict: Second visit.
- **Numbers.** Grids to 6 by 6.
- **Home materials.** Pencil, tracing paper, a small mirror (optional).
- **Kit.** None.
- **Figures.** `grid` with a mirror line (exists, `mirror` option), `panel` (exists).
- **Misconceptions.** A diagonal of a rectangle is a line of symmetry; counting 2 for the same line; reflecting the wrong distance.
- **Needs.** none beyond M18 (hatch).
- **Safe to miss?** Fairly safe.

### Lesson 27. Cube Stacks and Views (T3.7)

- **Big idea.** See it from every side: three views fix a stack, and sometimes only a range of stacks.
- **Strand.** Enrichment: building with unit cubes is Primary 5 (Volume 2.1, p. 42) and views of stacks are not named in the syllabus. **No school-paper evidence.**
- **Objective.** Count cubes in a stack; draw the front, side and top views; build a stack from views; say which cubes are hidden. Think harder: count by layer into a table; which view cannot be right. Go further: the most and the fewest cubes that fit two views.
- **Remember (6 min).** (1) Count 12 blocks in 3 rows of 4. (2) A tower of 3. (3) Look at a box from the front, side and top.
- **Start here (6).** (1) Count the cubes in a stack drawn on a 3 by 3 base (heights 2, 1, 0 / 3, 2, 1 / 1, 1, 0): 11 (Q3.3). (2) The top view with numbers on each square. (3) Draw the front view. (4) Count 14 cubes in a table of three layers (X7.3). (5) Which stack has more cubes? (6) Build the stack with blocks and check.
- **Think harder (4).** (1) **TAB.** Count the cubes layer by layer into a table: layer 1, 2, 3 and the total 14 (X7.3). (2) **EXP.** A stack has a front view with a tallest column of 3 and a side view with a tallest column of 2. Can both be right? No: both views show the tallest column (X7.2). (3) The top view and the side view fix a stack: build it. (4) Which of three drawings is the front view of a given stack?
- **Go further (3).** G1 **Beyond (named): "Most and Fewest".** On a 3 by 3 base, the front view has columns 3, 1, 2 and the right view has rows 2, 3, 1. What are the fewest and the most cubes the stack can have? 6 and 14, from 275 possible stacks (X7.1). Level note: contest-style. G2 **LOG.** Build a stack from three views; check it matches all three. G3 Draw a stack whose three views are all the same.
- **Non-routine.** TAB T, EXP T, LOG G.
- **Holiday overlap: MED (H8 dice and glued dice).** Different content. New.
- **Numbers.** Bases to 3 by 3, heights to 4.
- **Home materials.** 14 same-size blocks or small boxes. **Fallback (D13):** every task is also set as a drawn stack with numbers on the squares of the top view; the drawn path is a complete lesson, not a degraded one.
- **Kit.** None cut. Isometric dot paper printed.
- **Figures.** `cube_stack` heights to 4 (F9 extension).
- **Misconceptions.** Hidden cubes forgotten; reading the front view as the top view; a view seen from the right drawn mirrored.
- **Needs.** F9.
- **Safe to miss?** Yes (the plan's enrichment).

### Lesson 28. Time Travellers (T3.8)

- **Big idea.** Time is a number line: add and subtract on the line, and use both 12-hour and 24-hour times.
- **Strand.** MOE P4 has no time outcome; the 24-hour clock is **P3** (Time 2.3, p. 36). This lesson revises P3 time with the school-paper moves (duration across noon, start from the end, timetable). Contest tags: two-event timetables (19-13), weekdays (19-4).
- **Objective.** Find an end time or a duration; read 24-hour times; find the start from the end; use a timetable with a break; try both orders of two events. Think harder: start from the end; a timetable with a break; two shows in either order. Go further: time zones; pay by the hour in 24-hour time; across midnight.
- **Remember (6 min).** (1) 60 minutes in an hour. (2) 1850 is 6:50 pm. (3) Noon and midnight.
- **Start here (6).** (1) 9:40 am + 2 h 35 min = 12:15 pm (X8.1). (2) 7:50 am to 11:20 am is 3 h 30 min (X8.1). (3) 1850 is 6:50 pm (X8.5). (4) Day after tomorrow and day before yesterday. (5) 0905 is 9:05 am. (6) A timeline story across noon.
- **Think harder (4).** (1) **BACK.** A show that lasts 1 h 55 min ends at 12:10 pm. When did it start? 10:15 am (X8.2). (2) **TAB.** A workshop runs 13:20 to 16:05 with a 25-minute break. How long is it, and how long without the break? 2 h 45 min and 2 h 20 min (X8.2). (3) **Both orders.** A class arrives at 10:00. The Dolphin Show lasts 40 minutes (10:10, 11:00, 12:30, 14:00) and the Magic Show lasts 55 minutes (10:30, 11:45, 13:20, 14:30). They watch both with no walking time. Earliest finish? Dolphin then Magic ends 12:40; Magic then Dolphin ends 13:10, so 12:40 (X8.3). (4) A duration across noon.
- **Go further (3).** G1 **Beyond (named): "Flight Time".** A flight leaves Singapore at 2340 and lasts 13 h 20 min. It lands at 1300 the next day Singapore time. London is 8 hours behind Singapore in winter, so the local time is 0500 (X8.4). Level note: time zones are not on the syllabus. G2 **CTX.** Dev works from 0845 to 1715 for $11 for every hour, break included. How much does he earn? 8.5 hours, $93.50 (X8.6). G3 **BACK.** A film of 2 h 50 min ends at 0015 the next day. When did it start? 2125 (X8.6).
- **Non-routine.** BACK T, TAB T, CTX G. The plan's EX-BACK-2 is replaced.
- **Holiday overlap: LOW (H1 buses only).** The holiday course has no duration, timetable or calendar item. New. This is the school-paper lesson the holiday course lacks (`g4_analysis.md` section 5, item 5).
- **Numbers.** Times to the minute; durations to 14 hours.
- **Home materials.** Pencil. A real clock if there is one.
- **Kit.** None (timeline strips are printed).
- **Figures.** `clock` with 24-hour readout, `number_line` as a time line (exist), `table` for timetables (F16 small).
- **Misconceptions.** Subtracting 8:50 from 11:20 as 3.30 hours; crossing noon with 12 as 0; adding 55 minutes to 11:45 as 11:100.
- **Needs.** F16, N7 (time formats).
- **Safe to miss?** No for the first half; the Quest gate 7 asks a time item.

### Lesson 29. Shape Studio: Hidden Lengths (T3.9, added)

- **Big idea.** Label every piece, then compare.
- **Strand.** MOE P4 area and perimeter (p. 39); a problem-solving studio (heuristic: label and compare, p. 13). Contest tag: frames of equal pieces (19-17).
- **Objective.** Find a missing side from equal pieces; find the side of a pinwheel square; count posts at equal distances. Think harder: a pinwheel of four identical rectangles; posts round a rectangle. Go further: two arrangements, two unknowns; design a frame puzzle.
- **Remember (6 min).** (1) Perimeter of a 12 by 8 rectangle. (2) Area of the same. (3) The difference of 12 and 8.
- **Start here (6).** (1) A rectangle is made of 3 identical squares in a row, perimeter 32 cm: side 4 cm. (2) Two identical rectangles joined make an L: find one side. (3) A picture in which a small square sits in the corner of a rectangle: find its side. (4) Label each side of a figure of equal pieces. (5) Perimeter of the figure. (6) Area of the figure.
- **Think harder (4).** (1) **GEO.** Four identical rectangles are placed round a small square to form a big square of side 20 cm. The small square has side 4 cm. Find the rectangle: 12 cm by 8 cm (area 96 cm2; the whole is 4 x 96 + 16 = 400, X9.1). (2) **CTX.** 36 posts stand at equal distances round a rectangular park, one at every corner. A longer side has 11 posts, counting both corners. How many posts are on a shorter side? 9 (X9.2). (3) The big square's area from the small square's side. (4) An L-shape of equal pieces: find a missing side and the perimeter.
- **Go further (3).** G1 **Beyond (named): "Pinwheel Square".** The side of the big square times itself equals four rectangles plus the small square: (a + b) x (a + b) = 4 x a x b + (a - b) x (a - b) (X9.4). Level note: an algebra identity. G2 **GEO.** Four identical rectangles are put end to end in a row: perimeter 80 cm. The same four make a 2 by 2 block: perimeter 52 cm. Find the rectangle: 9 cm by 4 cm (X9.3). G3 **CHAL.** Design a frame puzzle with exactly one answer and give it to a partner.
- **Non-routine.** GEO T, CTX T, CHAL G.
- **Holiday overlap: MED (H7 C1).** H7 had a square cut into two identical rectangles each with perimeter 24 (area 64). Do not reuse. SASMO 19-17 (a frame of 8 equal rectangles) is not copied; the pinwheel of 4 and the row-versus-block pair are original. Verdict: Second visit.
- **Numbers.** Sides to 30 cm; posts to 60.
- **Home materials.** The kit rectangles; pencil.
- **Kit (K7 identical rectangles).** 8 identical rectangles (3 by 2 units) and 1 small square (1 by 1): 9 pieces. Max used 8 rectangles (Explore tiles a 6 by 8 rectangle with 8 rectangles) and 1 square. Cut 9.
- **Figures.** `shape2d` with dimension labels and `joined` pieces (F8).
- **Misconceptions.** Using the outer perimeter as the rectangle's; counting corner posts twice; assuming the small square equals the rectangle's width.
- **Needs.** F8, K7.
- **Safe to miss?** Yes: the safest of Term 3.

### Lesson 30. Challenge Day 3, with Mi's Challenge Quest (T3.10)

- **Big idea.** A map can be traced once if you start and stop in the right places.
- **Strand.** Heuristics (p. 13); routes and networks (Intl: HK P4 enrichment). The Quest follows (section 6).
- **Objective.** Count shapes in a grid; find a route that uses every road once; decide why some maps cannot be traced. The Quest carries a gate for each of lessons 21 to 29.
- **Remember (6 min).** (1) Trace a shape without lifting the pencil. (2) Count the lines at a corner. (3) Odd and even numbers.
- **Start here (5).** (1) Count the squares in a 3 by 3 grid. (2) Count the roads at each town on a small map. (3) Trace a square with a diagonal. (4) Mark the towns with an odd number of roads. (5) Trace a simple map.
- **Think harder (3).** (1) **LOG.** A map has five towns A to E and seven roads: AB, AC, BC, BD, CD, CE, DE. Find a route that uses every road once. It must start at B and end at D (or the reverse), the only two towns with an odd number of roads (X10.1). (2) Why can a map with four odd towns not be traced? (X10.2). (3) A table of towns against roads.
- **Go further (3).** G1 **Beyond (named): "Seven Bridges".** Four places are joined by seven bridges: A to N twice, A to C twice, A to I once, N to I once and C to I once. Nobody can cross every bridge once (A has 5, and N, C and I have 3 each, X10.2). Add one bridge between two odd places and a route exists (X10.3). Level note: graph theory, secondary school. G2 **GEO.** Design a map of 6 towns that can be traced. G3 **CHAL.** A puzzle that cannot work: fix it with one extra road.
- **Non-routine.** LOG T, GEO G, CHAL G.
- **Holiday overlap: NONE.** New.
- **Numbers.** Maps of up to 7 towns and 9 roads.
- **Home materials.** Pencil; a quest partner; the Quest Log stays closed in Book 6.
- **Kit.** None.
- **Figures.** `network` (exists), with curved roads (F15).
- **Needs.** Quest block (section 6), N3, F15.
- **Safe to miss?** The body yes; the Quest is the part to protect.

---

## Term 4: Create and connect (lessons 31 to 40)

Cold joining: yes. The Remember warm-ups carry a fraction of a quantity, reading a bar chart, and finding the rule in a short list; every move taught in lessons 33 to 37 is taught from scratch. A December joiner of Term 1 and a school-only child both enter here on equal terms. **Safest to skip or make up: lesson 39** (the added lesson); then lessons 34, 35 and 38 (no school-paper evidence); hardest to miss: 31, 32 and 36. Lesson 40 hosts the Year Quest and the showcase.

### Lesson 31. Data Detectives: Line Graphs (T4.1)

- **Big idea.** A graph can be read, and a graph can be misread.
- **Strand.** MOE P4 tables, line graphs and pie charts: read and interpret (Statistics, p. 40). Contest tag: reading a graph (19-20).
- **Objective.** Read values, periods and rises from a line graph; compare two lines; judge a scale; estimate a missing reading from the trend. Think harder: the greatest rise; a misleading scale; two lines. Go further: fill a gap from the trend; build a graph from clues; the steepest climb.
- **Remember (6 min).** (1) Read a bar chart with a scale of 5. (2) 35 - 28. (3) Mark 4.5 halfway between 4 and 5 on a line.
- **Start here (6).** (1) Read the value at a point on a graph with a scale of 2 per line. (2) At which hour was the value highest? (3) How much did it rise between 2 pm and 4 pm? (4) Complete a table from the graph. (5) Read a value halfway between two lines. (6) How many more at hour 5 than at hour 2?
- **Think harder (4).** (1) **TAB.** The temperatures at hours 1 to 6 are 21, 24, 26, 33, 31 and 35 degrees. Between which two hours was the greatest rise? Hours 3 and 4, a rise of 7 (Y1.1). (2) Two lines on one graph: at which hour do they meet? (3) **EXP.** The sales 120, 126, 132 and 138 are drawn twice: once with a scale starting at 110 and each line worth 2, once starting at 0 with each line worth 50. Which graph makes the rise look larger, and which is fairer? (4) A scale that does not start at 0: a point at 220 is not twice a point at 160.
- **Go further (3).** G1 **Beyond (named): "Fill the Gap".** The reading at hour 2 is 12 and at hour 6 is 24, and the line is steady. What is the reading at hour 4? 18 (Y1.2). Level note: estimating between readings is not named in the syllabus. G2 **CHAL.** Build a line graph from four clues. G3 Which interval has the steepest climb, and how much per hour?
- **Non-routine.** TAB T, EXP T, CHAL G. The plan's EX-CHAL-2 is used with new data.
- **Holiday overlap: HIGH (H9).** H9 did a chicken-rice queue (4, 9, 18, 22, 15, 7, 3), matching four stories to four graphs, 45 to 60 bowls, steady rises (40, 55, 70), a scale starting at 40 or 100, Shops A and B (cakes), two tanks crossing at 4 hours, swimmers (50), nasi lemak 400, 52 54 56 58 on two scales. Do not reuse any, and the plan's "spot a misleading scale" is H9's C9; this lesson uses a different pair of scales and starts from a given misleading graph rather than asking the child to choose a scale. Verdict: Change.
- **Numbers.** Values to 500; scales of 1, 2, 5, 10, 20, 50.
- **Home materials.** Pencil, ruler, graph paper (in the book).
- **Kit.** None.
- **Figures.** `line_graph` (F10): scale, broken axis, one or two lines, a shaded period, hatch patterns for two lines.
- **Misconceptions.** Reading the grid line instead of the point; the height of a point read as the rise; a line graph read as a bar graph.
- **Needs.** F10, M18.
- **Safe to miss?** No (lesson 32 and the Quest use graphs).

### Lesson 32. Pie Charts (T4.2)

- **Big idea.** The whole circle is the whole, and each sector is a fraction of it.
- **Strand.** MOE P4 read and interpret pie charts (Statistics, p. 40); a sector as a fraction of the whole. Angle-based construction is beyond P4.
- **Objective.** Read a pie chart as fractions of a total; find the amount for a sector; find a missing sector; compare a pie chart and a bar graph without a scale. Think harder: build from fractions and one count. Go further: true, false or not possible to tell; angles of sectors.
- **Remember (6 min).** (1) 1/4 of 120. (2) Add 1/3 and 1/6. (3) A bar split into 8 equal parts.
- **Start here (6).** (1) A pie chart of 80 pupils is half bus, a quarter MRT and a quarter walking: 20 walk. (2) How many take the bus? 40. (3) Which sector is the greatest? (4) Total 240: a sector of 1/3 is 80 pupils (Y2.1). (5) A sector of 1/4 is 60 (Y2.1). (6) What fraction does the remaining sector show?
- **Think harder (4).** (1) Total 240: sectors 1/3, 1/4 and 5/12 are 80, 60 and 100 pupils, adding to 240 (Y2.1). (2) **CHAL.** A is 3/8 of the pupils. A and B together are 5/8. C is as many as B. D is the rest. 30 pupils chose C. How many pupils are there, and how many chose D? 120 and 15 (Y2.2). (3) **CMP.** A bar graph has no scale. The red bar is 9 squares tall and the blue bar is 5 squares tall, and there are 28 more in red. How many pupils in all? 98 (Y2.3). (4) The missing sector of a chart.
- **Go further (3).** G1 **Beyond (named): "Angle of a Sector".** A sector of 1/3 turns 120 degrees, 1/4 is 90, 5/12 is 150 and 1/8 is 45; they add to 360 for the whole circle (Y2.4). Level note: pie-chart angles are Primary 6. G2 **EXP.** Each statement about a pie chart is true, false or not possible to tell. G3 Build a pie chart from data with a protractor and check the angles add to 360.
- **Non-routine.** CHAL T, CMP T, EXP G.
- **Holiday overlap: NONE.** New. The P4 papers carry the missing-sector item (`p4_school_paper_patterns.md` section 4).
- **Numbers.** Totals to 360; fractions with denominators 2 to 12.
- **Home materials.** Protractor, ruler, pencil. The circle template with 12 marks is printed.
- **Kit.** None cut; the pie circle is a printed page.
- **Figures.** `pie_chart` (F10) with hatch patterns; sectors may be hidden.
- **Misconceptions.** Reading a sector as a count rather than a fraction; adding fractions with different denominators without converting; treating bar heights as values.
- **Needs.** F10, M18, F3.
- **Safe to miss?** No.

### Lesson 33. Patterns and Rules in Words (T4.3)

- **Big idea.** Find the rule, test it on every case, and say it in words.
- **Strand.** MOE P1 to P4 number sequences and patterns (p. 31 to 37). Pairing sums and mixed numbers that pair into wholes are beyond P4 (the second is Primary 5). Contest tags: gaps that grow (19-1), pairing (19-16, 19-11), rule from diagrams (19-10).
- **Objective.** Continue a pattern; write the gaps; find the nth figure of a dot pattern; sum a list by pairing. Think harder: the nth figure and its inverse; two interleaved lists; gaps that grow; pairing. Go further: a rule found from four diagrams; mixed numbers that pair.
- **Remember (6 min).** (1) Continue 4, 7, 10, 13. (2) 3 + 4 + 5 as 3 x 4. (3) The difference between neighbours.
- **Start here (6).** (1) Continue 5, 9, 13, 17 and write the gaps. (2) Write the gaps of 2, 3, 5, 8, 12 and continue. (3) Add 1 + 2 + 3 + 4 + 5 by adding in order: 15. (4) Draw Figure 4 of a dot pattern. (5) Which figure comes after Figure 3? (6) Is 41 in the list 5, 9, 13, ...?
- **Think harder (4).** (1) **PAT/TAB.** Figure 1 has 4 dots, Figure 2 has 7, Figure 3 has 10, Figure 4 has 13. How many in Figure 25, and which figure has 100? 76 and Figure 33 (Y3.1). Complete the table. (2) Two lists are shared: 3, 50, 6, 46, 9, 42, ... What is the 10th number? 34 (Y3.6). (3) The numbers 3, 4, 6, 9, 13, ... have gaps 1, 2, 3, 4. What is the 20th? 193 (Y3.2). (4) Pair 1 to 10 to get 55, then sum 47 to 59 by pairing the first and last: 689 (Y3.3). The plan's 31 to 41 is SASMO 19-16 and is not used.
- **Go further (3).** G1 **Beyond (named): "Gauss's Trick".** 1 + 2 + ... + 100 is 50 pairs of 101, 5 050 (Y3.3). Level note: arithmetic series are secondary school. G2 **PAT.** Four boxes show a left number, a right number and a top number: (3, 2, 10), (4, 1, 9), (5, 4, 26), (2, 3, 13). One rule works for all four. Find the top number for 6 and 5: 37, the rule being twice the left plus the right times itself (Y3.5). G3 **Preview.** 3 1/4 + 2 2/5 + 1 3/4 + 4 3/5 = 12, because the fractions pair into 2 wholes (Y3.4). Level note: Primary 5.
- **Non-routine.** PAT T, TAB T, PAT G. The plan's second PAT G (EX-PAT-3, alternating decimals) stays in lesson 5.
- **Holiday overlap: MED (H9, H3).** H9 had steady rises (35, 45, 60, 85 toys, 60 plates a day) and H3 had the sum chain 3, 7, 10, 17, 27 and the chain with the 5th number 30. Do not reuse. Verdict: Second visit.
- **Numbers.** Terms to the 25th; sums to 5 050.
- **Home materials.** Pencil, squared paper.
- **Kit.** None.
- **Figures.** `figure_sequence` (dot or square patterns with Figure labels, F12), `table` (exists).
- **Misconceptions.** The rule from the first gap only; the nth figure given as n + 3 when the gap is 3; pairing an odd list without the middle number.
- **Needs.** F12.
- **Safe to miss?** Fairly safe.

### Lesson 34. Solve a Smaller Problem (T4.4)

- **Big idea.** Try 3 before 100: solve small cases, spot the pattern, then use it.
- **Strand.** Heuristics (p. 13); counting. **No school-paper evidence.** Contest tag: simplify and look for a pattern.
- **Objective.** Solve a problem for small numbers, record them in a table, find the rule and use it for a large case. Think harder: handshakes; digits in page numbers; pages facing each other. Go further: a large handshake case; posts round a pond.
- **Remember (6 min).** (1) 1 + 2 + 3. (2) Count the digits of 99 and 100. (3) The gap between 7 and 12.
- **Start here (6).** (1) 3 people shake hands once with each other: 3 handshakes. (2) 4 people: 6 (Y4.1). (3) 5 people: 10 (Y4.1). (4) Record the numbers in a table. (5) Do you see a pattern? (6) How many digits to number pages 1 to 9?
- **Think harder (4).** (1) **PAT.** 6 people: 15 handshakes (Y4.1); find the rule from the table. (2) How many digits are needed to number pages 1 to 250? 9 + 180 + 453 = 642 (V9.5). (3) A table for the pages, 1 to 99 and 100 to 250. (4) A smaller case first for a line of 20 trees with a post between each.
- **Go further (3).** G1 **Beyond (named): "Handshake Triangle".** 30 people shake hands once each with everyone: 435 (Y4.1). Level note: triangular numbers, secondary school. G2 **LOG.** The two pages facing you in a book have numbers that add to 509. What is the smaller page number? 254 (Y4.2). G3 **CTX.** A square pond has perimeter 80 m. A post is put every 4 m round it, one at each corner. How many posts? 20 (Y4.3).
- **Non-routine.** PAT T, LOG G, CTX G.
- **Holiday overlap: LOW (H10 C4, S5: 6th from front and back).** Do not reuse the queue items. New.
- **Numbers.** Up to 30 people, pages to 250.
- **Home materials.** Counters or coins (12) for acting out; pencil.
- **Kit.** None.
- **Figures.** `network` (complete graph of 4, 5, 6 points, exists), `table`.
- **Misconceptions.** Counting each handshake twice; counting the first digit only; posts counted as gaps.
- **Needs.** F15 (small).
- **Safe to miss?** Yes (no paper evidence).

### Lesson 35. Make a Systematic List (T4.5)

- **Big idea.** Do not miss one: list in order, remove repeats, or multiply the choices.
- **Strand.** Heuristics (p. 13); counting. **Chance is not on the MOE primary syllabus** (probability appears nowhere, `syllabus_by_level.md` p. 16) and is a labelled extension. No school-paper evidence for chance (WAYS has 2 items).
- **Objective.** List ways in order; remove repeats in pairs; multiply the choices for two or three stages with one pairing not allowed; order events on a spinner by chance; find the smallest and largest total of dice. Think harder: outfits; pairs with a total; chance. Go further: a fair game; coin ways; count without listing.
- **Remember (6 min).** (1) 2 x 3 x 4. (2) Ways to make 6 with two numbers. (3) A coin has two sides.
- **Start here (6).** (1) List all the ways to pay 60 cents with 10-cent and 20-cent coins: 0 twenties and 6 tens, 1 and 4, 2 and 2, 3 and 0 in the form (tens, twenties): (6, 0), (4, 1), (2, 2), (0, 3) (Y5.8). (2) 3 shirts and 2 hats: 6 outfits. (3) List the pairs of 1 to 5 that add to 6. (4) How many 2-digit numbers can be made from the cards 2, 4, 7 if digits may repeat? 9. (5) A tree diagram for 2 coins. (6) Draw a table for 3 by 4 choices.
- **Think harder (4).** (1) **WAYS.** Ravi has 3 tops, 5 pairs of trousers and 2 hats. He never wears the yellow top with the blue trousers. How many outfits? 30 - 2 = 28 (Y5.1). (2) **LIST.** How many different pairs of numbers from 1 to 9 add to 12? 3: 3 and 9, 4 and 8, 5 and 7 (Y5.3). (3) **Chance (extension).** A fair spinner has the numbers 1 to 10. Put these in order from least to most likely: a multiple of 4 (2), a number less than 4 (3), an even number (5), a number that is not 10 (9) (Y5.6). With three dice, which total is impossible: 2, 3, 18 or 19? 2 and 19 (Y5.4b). (4) Remove repeats from a list of pairs.
- **Go further (3).** G1 **Beyond (named): "Fair Spinner Game".** Two spinners, one with 1 to 4 and one with 1 to 6, are spun and added. 4 of the 24 results make 7 (Y5.5). Design a game that is fair for two players. Level note: probability is secondary school. G2 **WAYS.** Pay $2.40 with 20-cent and 50-cent coins, at least one of each. How many ways? 2, which are 7 twenties with 2 fifties and 2 twenties with 4 fifties (Y5.2). G3 Count without listing: 4 shirts, 3 shorts, 2 caps and 3 pairs of socks make 72 outfits (Y5.7).
- **Non-routine.** WAYS T, LIST T, WAYS G. The plan's EX-WAYS examples are replaced.
- **Holiday overlap: LOW (H8 C8, C9 ways to shade; H10 C6 coins).** Do not reuse the 10-cent and 50-cent coin item. New.
- **Numbers.** Up to 72 outcomes.
- **Home materials.** Pencil; the K8 cards; two dice or a coin if available (the cards replace dice); a paper clip and pencil for the spinner.
- **Kit (K8).** A set of cards 1 to 6 (6 cards, drawn with replacement in place of a die) and 2 printed spinner discs (not cut). Max used 6 cards and 2 spinners. Cut 6.
- **Figures.** `spinner` and `dice` (F13), `table` (exists).
- **Misconceptions.** Counting (3, 9) and (9, 3) as two pairs when the order does not matter; treating every outcome as equally likely when the spinner sectors are unequal; subtracting the forbidden outfit once instead of once per hat.
- **Needs.** F13, K8.
- **Safe to miss?** Yes.

### Lesson 36. Working Backwards (T4.6)

- **Big idea.** Undo the story: start from the end and reverse every step.
- **Strand.** Heuristics (p. 13). Contest tag: work backwards with fractions (19-25).
- **Objective.** Reverse a chain of operations; undo a money story with a fraction; make equal and find the start. Think harder: money chains; make equal, then find the start. Go further: a tank chain with fractions; a number that reverses to four times itself.
- **Remember (6 min).** (1) What undoes + 8? (2) What undoes x 3? (3) 3/5 of 45.
- **Start here (6).** (1) Ravi had some stickers. He gave away 15, got 8 more, and now has 30. How many at first? 37 (Y6.1). (2) A number is multiplied by 4 and 6 is taken away, giving 30: 9 (Q4.1). (3) Reverse one step in each of four stories. (4) A table with the steps and the reverse steps. (5) Check forwards. (6) A story with the answer at the end of the chain.
- **Think harder (4).** (1) **BACK.** Wei spent $18 on a gift and then 2/5 of what was left on lunch. He had $27 left. How much had he at first? $63 (Y6.2). (2) **EQ.** Ali gives Ben $9 and then both have $50. How much had each at first? Ali $59 and Ben $41 (Y6.3). (3) A money chain with a half. (4) An age story reversed.
- **Go further (3).** G1 **Beyond (named): "Mirror Number".** Find a 4-digit number that becomes four times itself when its digits are reversed: 2 178 (2 178 x 4 = 8 712, the only one, Y6.4); and 1 089 x 9 = 9 801 (Y6.5). Level note: contest-style digit puzzle. G2 **BACK.** A tank of water loses 1/5 on Monday, 1/2 of what is left on Tuesday and 30 litres on Wednesday, leaving 90 litres. How much was there at first? 300 litres (Y6.6, Y6.7). G3 **CHAL.** Make up a backwards puzzle with a unique answer.
- **Non-routine.** BACK T, EQ T, BACK G.
- **Holiday overlap: HIGH (H3, H10).** H3 had x 8 - 15 = 425, half of the money on a book then $6 then half (48), 5 x then + 35; H10 had double and add 7 (43), half and 2 more twice (32), $15 on a book then half (51), the swap machine (47 and 74). Do not reuse. Verdict: Change.
- **Numbers.** Totals to 500; fractions with denominators 2 to 6.
- **Home materials.** Pencil, squared paper.
- **Kit.** None.
- **Figures.** `bar_model` before-and-after (F4), `table`.
- **Misconceptions.** Undoing the steps in the same order; reversing "2/5 of the rest" as "2/5 of the total"; stopping at the first reversed step.
- **Needs.** F4.
- **Safe to miss?** No: the Year Quest gate 5.

### Lesson 37. Suppose and Compare (T4.7)

- **Big idea.** Make them all the same, then see what is left.
- **Strand.** Heuristics (p. 13): supposition, guess and check done well, balance chains. Contest tag: balance scales (19-15).
- **Objective.** Solve two-kind problems by a table and by supposing; solve three-kind and two-scenario problems; chain balance scales. Think harder: tickets; three kinds; a balance chain; left over and short. Go further: a fruit order; coins; a decimal unit chain.
- **Remember (6 min).** (1) 6 x 30 and 9 x 80. (2) The difference between 80 and 30. (3) A balance with 2 cubes on each side.
- **Start here (6).** (1) Ali buys 15 stamps, some at 30 cents and some at 80 cents, and pays $7.50. How many 80-cent stamps? 6 (Y7.1). (2) Make a table of guesses. (3) Check the answer. (4) Two more table items. (5) A picture of the supposition: all 30-cent stamps. (6) A story with a table.
- **Think harder (4).** (1) **GC.** Adult tickets cost $9 and child tickets $5. 18 tickets cost $122. How many adult tickets? 8 (Y7.2). (2) **GC three kinds.** Zoe buys 12 books at $3, $5 or $8. She buys the same number of $5 and $8 books and pays $64. How many of each? 4, 4 and 4 (Y7.3). (3) **Balance chain.** A pear balances 3 plums, a melon balances 2 pears and a pumpkin balances 3 melons. How many plums balance a pumpkin? 18 (Y7.4). (4) **GC two scenarios.** Chairs are put in rows. 9 in a row leaves 4 chairs over; 11 in a row is 6 chairs short. How many rows and chairs? 5 rows, 49 chairs (Y7.5).
- **Go further (3).** G1 **Beyond (named): "Balance Chain Order".** A mango balances 3 plums, a papaya balances a mango and 2 plums, and a melon balances a papaya and a mango. Put the four fruits in order from heaviest to lightest and say how many plums balance the melon: melon, papaya, mango, plum; 8 plums (Y7.8). G2 **GC.** 21 coins, all 5-cent and 20-cent, make $2.70. How many 20-cent coins? 11 (Y7.6). G3 **EQ.** Mr Chen has 4.8 kg more rice than Mr Dass. Mr Chen uses 6.4 kg, and then Mr Dass has 3 times as much as Mr Chen has left. How much rice did Mr Dass have at first? 2.4 kg, and Mr Chen 7.2 kg (Y7.7).
- **Non-routine.** GC T x3, GC G, EQ G. The plan's EX-GC and EX-EQ examples are replaced; the two-scenario sharing in lesson 8 uses different numbers.
- **Holiday overlap: HIGH (H10, H5).** H10 had bicycles and tricycles (47 wheels), spiders and ants (82 legs), farm legs, tables of 4 and 6 (76 seats), cake and drink ($40), a coin puzzle (6 coins, 10 and 50 cents); H5 had 10 coins of 20 and 50 cents ($3.80). Do not reuse legs, wheels, seats or those coin pairs. Verdict: Second visit.
- **Numbers.** Totals to $200; decimals to 1 place.
- **Home materials.** Pencil, squared paper.
- **Kit.** None.
- **Figures.** `balance` (F14), `table`, `bar_model` (F4).
- **Misconceptions.** Stopping at the first guess that fits one fact; supposing all one kind and not adjusting by the difference; reading "balances" as "equals".
- **Needs.** F14, F4.
- **Safe to miss?** No: the Year Quest gate 6.

### Lesson 38. Looking Ahead to Primary 5 (T4.8)

- **Big idea.** A taste of next year: a fraction is a division, and a box holds layers of cubes.
- **Strand.** Preview, labelled Primary 5 (fraction as division of whole numbers, Fractions, p. 41; volume of cuboids, Volume 2.1, p. 42). **No school-paper evidence.**
- **Objective.** Write a division of whole numbers as a fraction or mixed number; count the cubes of a cuboid layer by layer; compare which of two boxes holds more. Think harder: a box layer by layer; which box holds more. Go further: the formula; why a claim is wrong.
- **Remember (6 min).** (1) 3/4 of a pizza. (2) 4 x 3 x 2. (3) Share 6 sweets among 3.
- **Start here (6).** (1) Share 3 pizzas equally among 4 children: each gets 3/4 of a pizza (Y8.1). (2) 5 divided by 8 is 5/8 (Y8.1). (3) A 2 m ribbon cut into 5 equal pieces: 2/5 m each (Y8.1). (4) A box 4 by 3 by 2 has 24 cubes (Y8.1). (5) Count the cubes in the first layer. (6) How many layers?
- **Think harder (4).** (1) **DIAG.** A box is 5 cubes long, 4 wide and 3 high. How many cubes? 20 in a layer, 3 layers, 60 (Y8.1). (2) **CMP.** Box A is 5 by 4 by 3, box B is 6 by 3 by 3 and box C is 7 by 2 by 4. Which holds the most cubes? A, 60 against 54 and 56 (Y8.1). (3) 7 divided by 4 as a mixed number, 1 3/4. (4) A box with a missing height.
- **Go further (3).** G1 **Beyond (named): "Cubes in a Box".** The number of cubes is length times width times height. Level note: Primary 5. G2 **POSE.** Kai says a box 5 by 4 by 3 holds 45 cubes. Why cannot that be right? A layer has 20, so three layers are 60 (Y8.1). G3 **CMP.** Which holds more, a box 6 by 3 by 3 or a box 7 by 2 by 4, and by how much? The second by 2.
- **Non-routine.** DIAG T, POSE G, CMP G. The plan's EX-POSE-1 is replaced.
- **Holiday overlap: LOW (H8 S1 counted squares in a net).** New.
- **Numbers.** Boxes to 8 by 8 by 8; fractions with denominators to 12.
- **Home materials.** 24 same-size blocks (optional; fallback drawn layers, D13).
- **Kit.** None cut: printed layer mats.
- **Figures.** `cube_stack` layers (F9).
- **Misconceptions.** Multiplying only two sides; confusing area with volume; reading 3/4 as 3 and 4.
- **Needs.** F9.
- **Safe to miss?** Yes.

### Lesson 39. Count Place by Place (T4.9, added)

- **Big idea.** Count each place on its own, then add or multiply.
- **Strand.** Heuristics (p. 13); counting. **No school-paper evidence.** Contest tags: dates containing a digit (19-22), factorials (19-7).
- **Objective.** Count the numbers in a range that contain a digit, by listing and by place; count dates written dd/mm; use factorial notation for arrangements. Think harder: dates of a year with a given digit. Go further: other digits; factorials grow quickly.
- **Remember (6 min).** (1) Numbers from 1 to 20 with a 1. (2) Days in each month. (3) 3 x 2 x 1.
- **Start here (6).** (1) How many of the days of a 30-day month contain the digit 2? 12 (Y9.1). (2) List them: 2, 12 and 20 to 29. (3) Which month has all of its days with a 5? (4) A table of tens and ones for 1 to 40. (5) Count the 3s in 1 to 40: 13 (Q4.2 gate). (6) How many days in the month have no 2?
- **Think harder (4).** (1) **LIST.** In 2027 a date is written dd/mm, for example 05/09. How many dates have a 5 anywhere? The days 05, 15 and 25 occur in each of 11 months (33) and every day of May counts (31), so 64 (Y9.2, Y9.3). (2) Fill a table of month, days with a 5 and total. (3) **WAYS.** 5 children stand in a line: 5 x 4 x 3 x 2 x 1 = 120 ways, written 5! (Y9.4). (4) 4 children: 24.
- **Go further (3).** G1 **Beyond (named): "How Fast Factorials Grow".** 6! = 720, 10! = 3 628 800 and 10! ends in 2 zeros; 20! is the first to end in four zeros (Y9.4, Y9.5). Level note: factorials are secondary school. G2 **LIST.** In 2027 how many dates dd/mm contain a 3? 80, which is all of March plus the days 3, 13, 23, 30 and 31 of the other months (Y9.6). The draft's "no digit 1" version (142) is not used. G3 **LOG.** Number clues with place value (a 3-digit number whose tens digit is double its ones digit).
- **Non-routine.** LIST T, WAYS G, LOG G.
- **Holiday overlap: MED (H10 C1, H2 C7).** H10 counted the numbers from 1 to 100 with a 7 (19); H2 counted 5-digit numbers with a digit sum of 3. Do not reuse. Second visit.
- **Numbers.** Ranges to 365.
- **Home materials.** A calendar page (in the book), pencil.
- **Kit.** None.
- **Figures.** `calendar` (exists), `table`.
- **Misconceptions.** Counting 55 and 25 twice; treating May as 5 only for the month digit; computing 5! as 5 x 4.
- **Needs.** none.
- **Safe to miss?** Yes: the safest of Term 4.

### Lesson 40. Year-End Challenge, with Mi's Year Quest and the Showcase (T4.10)

- **Big idea.** Show what you can do: choose a move, solve, and pose.
- **Strand.** Heuristics (p. 13). The Year Quest (`scope: "year"`) follows, with the showcase.
- **Objective.** Solve a mixed set in which the child chooses the move; pose a puzzle. The Year Quest carries a gate for each of lessons 31 to 39 and a year-mix gate.
- **Remember (6 min).** (1) Pick the move: table, model, list or backwards. (2) 3/8 of 64. (3) A puzzle you liked this year.
- **Start here (5).** (1) A table or a model for a two-kind story. (2) A one-fraction question. (3) A counting question. (4) A backwards question. (5) A graph reading.
- **Think harder (3).** (1) **MULTI.** A two-move problem. (2) **GC.** Tickets or coins with a table. (3) A pie chart or a line graph to use.
- **Go further (3).** G1 **Beyond (named): "Pose a Puzzle".** Write a puzzle with exactly one answer and check it by listing every case. G2 **CHAL.** An open contest-style problem the child must set up alone. G3 **EQ.** A unit chain with a change.
- **Non-routine.** MULTI T, GC T, CHAL G, EQ G. The plan's Term 4 check is replaced by the Year Quest.
- **Holiday overlap: HIGH (H10, mixed).** Same rule as lesson 10.
- **Numbers.** As the year.
- **Home materials.** Pencil; a quest partner; plain paper for the showcase puzzle; a favourite page from the year. The Quest Log stays closed in Book 8.
- **Kit.** None.
- **Figures.** As needed.
- **Safeguarding.** The showcase is voluntary, a pass is always allowed, no ranking, no votes, no "best", nothing leaves the group without a grown-up's agreement, presentations are recorded under the existing recording statement (D9 at Level 1).
- **Needs.** Quest block (section 6), N3.
- **Safe to miss?** The body yes; the Year Quest is the part to protect.

