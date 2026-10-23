# Level 4 pre-flight (lessons 1 to 40, four terms, ages 9 to 11, Primary 4)

Status: planning only, written 23 Oct 2026. No lesson, tool, template or output file was edited, built or run (the only things run were scratch verification scripts, section 14). This document tells the people who will write the 40 Level 4 term lessons what each lesson is, which holiday and school-paper items it must not repeat, what the shared templates must learn first, what went wrong at Level 1 and must not be repeated, which decisions the owner must make, and in which order to build. It is modelled on `docs/terms/l1_term2_preflight.md`, `docs/terms/l1_term3_term4_preflight.md` and `docs/terms/l2_preflight.md`. Every default is marked **[Default]**.

Sources read in full: `docs/terms/owner_decisions.md` (all entries), `docs/terms/level_4_year_plan.md` (all four terms, both revision blocks, the verified-against-MOE block, the "Non-routine assignments" section, the matrix and the paper notes), `docs/books/p4_school_paper_patterns.md`, `docs/books/p4_non_routine_catalogue.md`, `docs/moe/syllabus_by_level.md` (P4 pp. 37 to 40, P3, P5 and the year index), `docs/sasmo/g4_analysis.md` and `g4_original_problems_draft.md`, the holiday program of the same level (`p4/SPEC.md` and `p4/content/l1.js` to `l10.js`: all 239 question-bank items, 60 core, 89 stretch and 90 challenge, and every lesson's objective, warm-up, explore and extension line were extracted and read), `docs/terms/l1_term2_preflight.md`, `docs/terms/l1_term3_term4_preflight.md`, `docs/terms/l2_preflight.md`, `docs/terms/l3_preflight.md` (first 130 lines; the file is still being written by another agent), `term/l1/AUTHORING.md`, `WORDING_GUIDE.md`, `audit/TERM_WIDE_AUDIT.md`, `audit/CUTOUT_AUDIT.md`, `audit/FINAL_AUDIT_T1.md`, `audit/FINAL_AUDIT_T2.md` (finding tables), and the Level 1 tool inventory (`term/l1/tools/figs2.py`, `figs3.py`, `svg.py`, `b_quest.py`). The word-problem analyses (`docs/books/word_problems_g1_g2_*`) cover Grades 1 and 2 only and were not used. I did not re-read the holiday workbooks, slides or tutor guides, only the question banks and lesson metadata.

Numbers marked "verified" were recomputed by brute force in the verification script at the end of this document (section 14): **273 checks, all passed**. Check ids (`V3.2a`, `W1.8`, `X7.1`, `Y9.3`, `Q2.4`) point to it: V is Term 1, W Term 2, X Term 3, Y Term 4, Q the Quest gates. Lesson authors must still write their own `verify/lNN_checks.py`; nothing here replaces it.

## 0. Headline findings

1. **The holiday course already teaches every strand that the Level 4 term plan calls new, and many plan items repeat holiday items.** The ten holiday lessons (H1 Factor Hunters, H2 Big Number Puzzles, H3 Operation Detectives, H4 Fraction Frontier, H5 Decimal Detectives, H6 Angle Turns, H7 Area Architects II, H8 Symmetry and Nets, H9 Data Detectives, H10 Puzzle Day) match the term plan almost one for one by topic, and at the level of the question the overlap is large. Worst cases: plan 3.2 Angle Detectives is H6 (clock-hand angles, 8-point compass turns, reversing a turn, angles in a fan, minute-hand degrees); plan 3.3 Rectangle Rules is H7 (all rectangles with area 30, perimeter 20, 24 m of fencing, area 40 and perimeter 26); plan 1.3 Divisibility Detectives is H1 (odd number of factors, "a multiple of 4 and 6 must be a multiple of 24", buses that meet again, multiples of 4 or 6 to 100); plan 4.1 Data Detectives is H9 (misleading scales, two lines that cross, steady rises); plan 4.6 and 4.7 are H3 and H10 (work backwards, heads and legs, half-and-two-more); plan 3.1 is H8 (the 11 nets, 5 in a row cannot fold, opposite faces add to 7). Owner decision 4 sends holiday graduates to Term 1, so a graduate would meet these twice. Section 13 is a lesson-by-lesson register with "do not reuse" lists and a verdict (Change, Second visit, New). The plan's claim "Term 1 is new content" is true by title and false by item.
2. **Four plan items are close copies of contest or holiday items and are replaced here.** (a) 1.2 Think harder, "smallest 3-digit number whose digits multiply to a 3-digit number", is SASMO 19-18 word for word; replaced by a digit product of 168 and a 4-digit follow-up (V2.4, V2.6). (b) 1.3 Go further EXP uses catalogue example EX-EXP-3, which is holiday H1 challenge 5 ("a multiple of 4 and of 6 must be a multiple of 24"); replaced by "digits add to 12, so it is in the 12 table" (counterexample 39, V3.7). (c) 4.3 Think harder, "the sum of the numbers 31 to 41", is SASMO 19-16 with the same range; replaced by 47 to 59 (689, Y3.3). (d) 4.9's "dates of a year with a given digit" is the idea of SASMO 19-22 (an 8-digit date); replaced by dates written dd/mm in 2027, a different count with a different method (Y9.3). A fifth risk was avoided: the plan's 1.3 "fill a missing digit" would be SASMO 19-3 if written as "2 _ 4 in the 6 table", so the lesson uses 6 _ 8 in the 9 table and 417 _ in the 6 table (V3.2a, V3.2b). The plan itself lists each as a contest-style idea; the copy check (7-word overlap) would not catch an idea copied with new wording, so the authors must start from the replacements in section 1.
3. **One plan Go further item is impossible.** Plan 1.6 Go further asks for "a figure with exactly two parallel pairs and one perpendicular pair". Two parallel pairs in a quadrilateral force a parallelogram, which has 0 or 4 perpendicular pairs; a search of every simple quadrilateral on a 5 by 5 dot grid and every pentagon on a 4 by 4 grid found none (V6.1). Hexagons exist but are awkward non-convex shapes. Replaced by "a quadrilateral with exactly one right angle and no parallel sides" (exists, V6.2) and "can a quadrilateral have exactly three right angles?" (no, V6.3).
4. **The plan's non-routine section assigns the same example to several lessons.** EX-PAT-3 (alternating decimal steps) is in 1.5 and 4.3; EX-GC-1 (two sharing rules) in 1.8 and 4.7; EX-EQ-4 (decimal unit chain) in 2.8 and 4.7; EX-CTX-1 (pack prices) in 1.2, 1.3 and 2.7; EX-BACK-1 (tank) in 2.5 and 4.6; EX-POSE-1 in 1.8 and 4.8. This pre-flight gives each lesson its own context and numbers (section 1), so no two lessons share an item, and none repeats a catalogue example (the catalogue is the project's own original text, but the lessons must not paste it).
5. **Lessons 10, 20, 30 and 40 are Quest lessons and the plan's "Challenge Day plus 30-minute check" no longer fits.** The plan (section 5) puts a 10-question check of about 30 minutes in x.10; the owner replaced the check by Mi's Challenge Quest, 20 minutes after the break, with eight gates and a cave. That leaves about 19 minutes of Explore and Mini-lesson in the Challenge Day. Each x.10 is therefore a short Challenge Day (one move taught, three tiers kept short) plus the Quest. The contest moves the plan lists for x.10 (guess and check, backwards, hints puzzle, routes) are mostly in the holiday course (H10), so the Term 1 Challenge Day is rebuilt around new contexts and the gates, not around H10 items.
6. **Level 1's tools cover about half of Level 4's figures.** `number_line`, `hundred`, `table`, `bar_model`, `clock`, `money`, `calendar`, `grid`, `cube_stack`, `panel`, `network`, `picture_graph`, `objects`, `groups`, `array` and the kit pages exist; Level 4 also needs vertical column and area-model figures, stacked fractions and mixed numbers, a stronger `bar_model` (up to 16 units, decimals, before and after), an angle and compass family, dimensioned shapes with joined and folded pieces, solids and nets with a fold check, line graphs, bar graphs without a scale, pie charts, a logic grid, figure sequences, spinners and dice, and a balance. Section 3 lists 35 items (7 tool-level, 20 figure families, 8 kits); the Level 4 share is about 136 hours of template engineering (about 118 with deferrals), on top of the shared Level 2 and 3 items (parametrisation M1, validator M15, fraction renderer M2) that are built once.
7. **Printed books are black and white and scaled to 94.3 percent; Level 4 measures things.** Protractor, ruler and set-square tasks are the P4 syllabus (angles in degrees, drawing rectangles and squares, perpendicular and parallel lines), but a printed length is wrong in the book (CUTOUT_AUDIT F4, FINAL_AUDIT_T1 finding 2). Angles survive uniform scaling; lengths do not. Rule: every length is given in words or labels, the child draws to real size on squared pages with a real ruler, "All diagrams are not drawn to scale" appears on figure pages, and no task asks a child to measure a printed length. Children need a ruler, a protractor and a set square at home (decision D5). Pie charts, graphs and fractions must use hatch patterns (M18).
8. **Older children change the workbook, not just the numbers.** The P4 papers print Section C items with (a) and (b), "Ans:" lines with units, working space, and up to 4 marks (no marks are printed on our child pages). Level 1's workbook geometry (36 px answer boxes, 8 mm lines, 18.5 px text) is built for age 6 to 8; a Level 4 page needs a "Working" box, an "Ans:" frame, smaller writing lines and pages that stay 85 percent full without the large type (N6). The shared validator fills and thresholds assume the Level 1 geometry.
9. **Cutting load is light: 52 pieces a year** (Term 1 23, Term 2 0, Term 3 23, Term 4 6). Level 4 is mostly paper and pencil with real instruments; the kits are digit cards, a fraction wall, nets, a tangram, eight identical rectangles and a set of 1 to 6 cards. The Level 1 audit objected to 203 pieces in one term. Section 4 gives the kit contract for every lesson.
10. **Six lessons have no school-paper evidence** (the P4 papers read have no item of these kinds): 1.9 Count by Size, 3.7 Cube Stacks and Views, 4.4 Solve a Smaller Problem, 4.5 chance, 4.8 Looking Ahead to P5, 4.9 Count Place by Place. They are the right lessons to make up first in an exam period and the right place to trial wording. About 45 mostly 2021 and 2022 P4 PDFs were not read and the pictures were lost in OCR, so every item that depends on a figure (joined rectangles, folded paper, pie charts, graphs, nets, protractors) is marked "wording unverified" until the owner supplies a picture (decision D21).
11. **Unit chains are 27 percent of the non-routine paper and the plan teaches them in two lessons.** The plan's own notes say unit-chain Think harder items go into 1.2, 2.1, 2.7, 2.8, 4.6 and more; this pre-flight places an EQ item in 10 lessons (matrix, section 13) and gives each its own context. The `bar_model` figure caps at 10 cells and 3 bars, which is too small for "5 small jars and 3 big jars" style models (F4).
12. **Estimate:** about 335 agent-hours for the 40 lessons (write, wording review, independent audit, fix pass, four term-wide audits, the holiday-overlap pass and a consistency sweep) and about 136 hours of Level 4 template engineering (118 with deferrals), so roughly 470 hours (453 with deferrals); at the Level 1 pace (eight to ten writers, three engineers) about 8 to 10 working days from Sprint A to an audited Term 4 (section 11). Hours are estimates from the Level 1 documents, not measurements.

## 0.1 Assumptions made (change them if wrong)

- **Format.** 40 lessons of 90 minutes (owner decision of 23 Oct, "work with 90 mins"), groups of up to 8, online. Files are `term/l4/lessons/l01.json` to `l40.json` (global numbers 1 to 40, the plan's numbering written Term.Lesson); `level` 4, `term` 1 to 4, `lesson` 1 to 40, `lesson_in_term` 1 to 10, `id` `l4-t1-01` ... `l4-t4-40`, practice keys `l4t1l01` ... `l4t4l40` (the level prefix is new, because the shared runner already holds `t1l01` for Level 1 and the Level 2 pre-flight proposes `l2t1l01`). Family pages print "Level 4 Term 3 Lesson 4", never "Lesson 24 of 10". The leak check allows "Lesson 1" only where `lesson_in_term` is 1. Taglines: Term 1 "Notice it", Term 2 "Test it", Term 3 "Explain why", Term 4 "Create and connect" (the year arc, as at Levels 1 to 3).
- **The 11-part skeleton as built at Level 1:** Opening 2, Remember 6, Sneak-peek 4, Explore 14, Mini-lesson 10, Break 4, Workbook 28, Talk 6, Exit 6, Look-back 3, Flex 5 (Opening may be 4 with Explore 12). Quest lessons (10, 20, 30, 40): Opening 2, Remember 6, Sneak-peek 4, Explore 10, Mini-lesson 9, Break 4, **Quest 20 at minutes 35 to 55**, Workbook 25, Talk 4, Look-back 2, Flex 4 = 90; the exit ticket is not live. **[Default]** The Level 4 break stays 4 minutes (decision D16 offers 5 for ages 9 to 11).
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

What does **not** exist (and Level 4 needs): `balance`, `spinner`, `solid`, `net`, `place_value`, `column_sum`, `area_model`, `fraction`, `scale_dial` and `jug` (the Level 2 and 3 pre-flights propose these; none is built), any graph other than the picture graph, any angle figure, and any figure with dimension labels. The Level 2 and 3 pre-flight codes are quoted as "L2 M5" and so on where Level 4 shares an item; Level 4's own items are N1 to N7, F1 to F20 and K1 to K8 in section 3.

Level 1 term lessons 1 to 30 exist; `l31.json` onward are not written (other agents are writing Level 1 Term 4 and are not touched). No `term/l2`, `term/l3` or `term/l4` folder exists yet.

---

## 1. Lesson specs

### 1.0 Field order and conventions

Every spec uses this order: big idea, strand and page references (MOE P4 pp. 37 to 40, PDF pages), objective, Remember warm-up (three items, each re-taught with objects or a picture so a cold joiner can follow), Start here / Think harder / Go further outline with question counts, the **Beyond (named)** item, **Non-routine** work (type code, tier T or G, check id), **Holiday overlap** (what the holiday course did and what the term lesson must not repeat), number ranges, home materials, kit with piece counts (the kit contract: supplied against the most any one task may use), figures, misconceptions, template needs (codes from section 3), and whether the lesson is safe to miss.

**Non-routine work (owner decision of 23 Oct).** Each spec carries the `NR:` line from the plan's "Non-routine assignments" section (type code, tier T or G, never Start here), with the changes this pre-flight makes. Type codes (16): EQ unit and equal-share model, GEO geometry chain, LOG logic or number riddle, CTX unfamiliar context, LIST systematic list or bounds, MULTI multi-step, BACK work backwards, CHAL build or complete from data, EXP explain or true-false, TAB table or graph reading, GC guess and check or two scenarios, PAT pattern, DIAG draw or read a model, CMP comparison, sum and difference, WAYS how many ways, POSE judge or pose a statement. Hints naming the tool ("Hint: draw a model.") may appear in Think harder stems for a type that is new to the term, never in Go further (`p4_school_paper_patterns.md` section 5).

**Examples are original.** Every number and context below differs from the catalogue examples (EX- ids), from the draft problems and from the holiday banks. Authors write their own items of the same kind and their own `verify/lNN_checks.py`; the values here are the ones the pre-flight verified, offered as the model, not as text to paste. The copy check runs against the school and contest sources and, from M15, against `p4/content` (5-word overlap).

**Mid-year entry.** Every Remember re-teaches from nothing the one earlier idea the lesson leans on and uses no word that only an earlier lesson defined. A holiday graduate has met every Level 4 strand once (as a puzzle course); a school-only child has met them in class, usually a term or more earlier or later than our order (the plan's open question 7, decision D15). Warm-ups name holiday topics in the guide ("you may know this from the holiday course") but never depend on them.

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
- **Think harder (4).** (1) 10 000 - 3 785 two ways (renaming; counting up from 3 785): 6 215 (V1.2a). (2) A child works 50 003 - 28 479 and writes 22 524; find the step that is wrong; correct answer 21 524 (V1.2b). (3) **LIST/bounds.** Two numbers round to 7 400 and 2 600 to the nearest 100. Give the greatest and the smallest difference they can have: 4 899 and 4 701 (V1.3a, V1.3b). The twist is rounding bounds inside an operation. (4) **LOG.** Use the cards 1, 3, 6, 8 and 9 once each. Make the smallest number that rounds to 60 000 to the nearest ten thousand: 61 389 (V1.4).
- **Go further (3).** G1 **Beyond (named): "Close Neighbours".** Use the cards 2, 3, 5, 6, 8 and 9 once each to make two 3-digit numbers with the smallest possible difference: 25, from 623 - 598 (the only way, V1.5). Level note: contest-style digit arrangement; the arithmetic is Primary 4. G2 **EQ.** Class A raised $18 460; class B raised $3 975 less than class A; class C raised $10 000 more than class B. How much did the three classes raise altogether? $57 430 (V1.6a). G3 A car counter shows 79 996 km; the car then travels 2 307 km. How far is it from 100 000 km? 17 697 km (V1.6b).
- **Non-routine.** EQ G (G2), LIST T (rounding bounds, T3), LOG T (T4). The plan's greatest and smallest rounding item is moved from a bare "A number rounds to ..." to the difference form because H2 holds the bare form.
- **Holiday overlap: HIGH (H2).** H2 did rounding with a number line, smallest and largest that round to 38 000, 5 350 and 5 400, 45 000 and 50 000, palindromes, 99 990 to 100 000, digit cards closest to 70 000, counting on in 1000s from 3 456, the largest odd 5-digit number rounding to 90 000. Do not reuse any of these. The bare bounds item is replaced by bounds inside a difference (second visit with a new twist).
- **Numbers.** 0 to 100 000; sums and differences to 100 000; rounding to 10, 100, 1000.
- **Home materials.** Pencil, squared paper (the book has a place-value mat page).
- **Kit (K1 digit cards).** One set of cards 0 to 9 (10 pieces). Max used by a task 6 (G1) and 5 (T4); Explore lays out all 10. Tasks never need a repeated digit. Keep for lessons 2, 3, 10 and 11.
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
- **Go further (3).** G1 **Beyond (named): "Product Bounds".** Find the smallest number with four digits for which the product of the digits also has four digits: 2 789 (product 1 008, V2.6). Level note: contest-style; the idea of the plan's 3-digit item (19-18) is kept only at this larger size, with different numbers and wording. G2 **CTX.** A box of 6 mugs costs $27. A café needs 20 mugs and buys whole boxes only. Find the number of boxes, the cost and the mugs left over. 4 boxes, $108, 4 left (V2.7). G3 **LOG.** 3 [ ] 4 x 7 = 2 [ ] 1 8: the missing digits are 7 and 6 (374 x 7 = 2 618, unique, V2.8).
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
- **Think harder (4).** (1) **The digit-sum test.** Circle the numbers in the 3 table: 4 521, 7 806, 9 134, 5 838. The digit sums 12, 21, 17 and 24 give 4 521, 7 806 and 5 838 (V3.1). Then circle the numbers in the 6 table: 138, 366 and 450 (V3.1). (2) **LOG/missing digit.** 6 [ ] 8 is in the 9 table: the digit is 4 (648, V3.2b). 4 1 7 [ ] is in the 6 table: the digit is 0 or 6 (V3.2a). (3) **LOG.** I am a 2-digit number in the 6 table and in the 4 table. My digits add to 9 and my tens digit is smaller than my ones digit. What am I? 36 (V3.2c). Plus an **EXP** tick table: true, false or not possible to tell about multiples. (4) **Two cycles.** A bell rings at 9:00 and then every 8 minutes. A drum sounds at 9:04 and then every 12 minutes. When do they first sound together? 9:16, then every 24 minutes (V3.3).
- **Go further (3).** G1 **Beyond (named): "Swap and Subtract".** Take a 2-digit number, swap its digits and subtract the smaller from the larger. Show that the answer is always in the 9 table, and that it equals 9 times the difference of the digits (V3.4). Level note: an algebra idea shown by cases; the 9 table is Primary 4. G2 **CTX.** Pencils are sold 4 for $3 and erasers 6 for $5. Hana wants the same number of each and as few as possible. How much does she pay? 12 of each, $19 (V3.5). The papers set pack prices at 2 to 4 marks. G3 (a) Count the numbers from 300 to 400 that are multiples of both 6 and 8: 312, 336, 360, 384, so 4 (V3.6). (b) **EXP.** Mei says "if the digits add to 12 the number is in the 12 table". Find a counterexample: 39 (V3.7).
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
- **Start here (6).** (1) On the wall, 2/3 = [ ]/12: 8 (V4.1). (2) 3/5 = [ ]/20: 12. (3) Simplify 18/24 (3/4) and 20/45 (4/9) (V4.1). (4) Which is greater, 5/8 or 3/4? 3/4 (V4.1). (5) Arrange 2/3, 3/4 and 5/12. Begin with the smallest: 5/12, 2/3, 3/4 (V4.2). (6) A bar of 12 equal parts has 5 shaded. For 3/4 of the bar to be shaded, how many more parts need shading? 4 (V4.6).
- **Think harder (4).** (1) Simplify 36/48 and 28/42 using the greatest common factor. (2) **LIST/CMP.** Grid A has 12 squares, 7 of them shaded (5 whole squares and 4 half squares). Grid B has 16 squares, 9 of them shaded (8 whole and 2 half). Which grid has the greater fraction shaded? A, because 28/48 is more than 27/48 (V4.3). (3) **EXP.** Which is greater, 4/9 or 3/7? 4/9, by 28/63 against 27/63 (V4.4). (4) **LIST.** 24 stars are in 4 rows of 6, and 7 are shaded. For 5/8 of the stars to be shaded, how many more need shading? 8 (V4.5).
- **Go further (3).** G1 **Beyond (named): "Split a Fraction".** Write 2/5 as the sum of two different unit fractions: 1/3 + 1/15, the only way (V4.7). Level note: unit-fraction sums are secondary school; the equivalent fractions are Primary 3 and 4. G2 **CMP.** Which of 4/7 and 5/12 is nearer to one half, and by how much? 4/7, by 1/14 against 1/12 (V4.8). G3 How many fractions with denominator 24 lie between 1/3 and 1/2? 9/24, 10/24 and 11/24, so 3 (V4.9).
- **Non-routine.** LIST T (T4), EXP T (T3), CMP G (G2). The plan's EX-LIST-3 is used with new numbers.
- **Holiday overlap: MED-HIGH (H4).** H4 ordered 1/2, 7/12, 2/3 and 5/6, compared 3/7 with 3/5, 5/6 with 2/3 and 7/4 with 1 5/8, found fractions with denominator 10 between 1/5 and 1/2 (3/10 and 4/10), 12/16 from a numerator and denominator sum of 28. Do not reuse these fractions. Grids with half squares are new (19-14 idea).
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
- **Think harder (4).** (1) 9/20 = 0.45 and 13/25 = 0.52 (V5.1). (2) Order five numbers, mixing fractions, decimals and one mixed number. (3) **LIST.** A decimal with two places rounds to 4.8 to the nearest tenth. Give the smallest and the greatest value it can have: 4.75 and 4.84 (V5.4). (4) **LOG.** I have 2 decimal places and lie between 3 and 4. My tenths digit is twice my hundredths digit and my digits add to 12. What am I? 3.63 (V5.5).
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
- **Think harder (4).** (1) 6 408 / 8 = 801, with a zero in the quotient (V8.1). (2) **CTX.** 1 245 eggs are packed 8 to a box. How many boxes are needed? 155 full boxes and 5 eggs over, so 156 (V8.2). (3) **GC.** Sweets are shared among some friends. If each gets 6, there are 5 left over; if each gets 8, there are 7 short. Find the number of friends and the number of sweets: 6 friends, 41 sweets (V8.3). (4) A story with a hidden extra step (the sharer counts).
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
- **Think harder (3).** (1) **BACK.** A bus has some passengers. At the first stop 7 get off and 12 get on. At the second stop half of the passengers get off, and 18 remain. How many passengers were on the bus at the start? 31 (V10.2). (2) **GC.** Two numbers add to 25 and multiply to 144: 9 and 16 (V10.3). (3) A working-backwards story with a table.
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
- **Think harder (4).** (1) **EQ.** 3 small jars and 2 big jars hold 322 sweets. Each big jar holds double the sweets of a small jar. How many sweets does a big jar hold? 92 (W3.2). (2) **EQ.** A sofa and 3 cushions cost $480. The sofa costs $120 more than a cushion. Find the cost of a cushion: $90, so the sofa is $210 (W3.3). (3) **CMP.** The sum of two numbers is 190 and their difference is 46. Find them: 118 and 72 (W3.4). (4) One more unit chain with money.
- **Go further (3).** G1 **Beyond (named): "Same in the End".** Three friends have $840 altogether. Ali spends $60, Bee earns $45 and Cy gives away $15, and now each has exactly the same amount. How much did each have at first? $330, $225, $285 (W3.5). Level note: unit equations are Primary 5 (p. 41); the bar picture is Primary 4. G2 **CMP.** 4A, 4B and 4C collected 1 245 cans. 4A collected 55 more than 4B and 4C collected 40 fewer than 4B: 465, 410, 370 (W3.6). G3 **EQ.** Mia has 4 times as many cards as Raj. After Mia gives Raj 36 cards, she has twice as many as he has. How many did each have at first? Raj 54 and Mia 216 (W3.7).
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
- **Think harder (4).** (1) **BACK.** A tank is 3/7 full. It needs 84 more litres to be full. How much does the tank hold when full? 147 l (W5.1). (2) **MULTI.** A shop had 480 books. It sold 3/8 on Monday and 2/5 of the rest on Tuesday. How many more were sold on Monday than on Tuesday? 60 (W5.2). (3) **BACK.** Aisha used 1/3 of her savings for a book and $8 for pens, and $24 was left. How much were her savings at first? $48 (W5.6). (4) A fraction story with a bar and a table.
- **Go further (3).** G1 **Beyond (named): "Every Day a Third".** Each day Mei eats 1/3 of the cake that is left. After 3 days 40 pieces are left. How many pieces were there? 135 (W5.4). Level note: repeated fractions foreshadow powers (secondary). G2 **BACK.** A farmer sold 1/3 of his mangoes on Monday, 1/4 of the rest on Tuesday and 20 more on Thursday, leaving 40. How many mangoes at first? 120 (W5.3). G3 **BACK.** Wei gave 1/4 of his cards to Ali and 1/3 of the rest to Ben, and had 36 left. How many at first? 72 (W5.5).
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
- **Think harder (4).** (1) **CTX best buy.** Juice is sold 6 for $4.80, 4 for $3.40 and 10 for $7.50. Which is the best buy? 10 for $7.50 at $0.75 each against $0.80 and $0.85 (W7.2). (2) **CTX pack prices.** Notebooks are 3 for $4.50 and rulers 4 for $3.20. Zoe buys the same number of each, the smallest number possible. What does she pay? 12 of each, $27.60 (W7.3). (3) **EQ.** 2 books and a pen cost $23.30. A book costs $5.20 more than the pen. Find the price of the pen: $4.30, and the book is $9.50 (W7.5). (4) **DIAG.** A bag of rice and 3 identical tins weigh 4.2 kg. The rice is 3 times as heavy as one tin. How heavy is the rice? 2.1 kg (W7.4).
- **Go further (3).** G1 **Beyond (named): "Unit Switch".** 2.35 m is 235 cm, 7.5 kg is 7 500 g, 3.04 l is 3 040 ml, and 4 kg 70 g is 4.07 kg (W7.6). Level note: Primary 5 (p. 41). G2 **CTX.** Cans are sold in packs of 6 for $5.40 and 8 for $6.80. Kai needs exactly 24 cans and buys whole packs only. The only ways are 4 packs of 6 or 3 packs of 8; the cheaper is $20.40 (W7.7, W7.8). G3 **CTX.** Lena is paid $12 for every hour she is at work, her break included. She works from 8:20 am to 5:05 pm. What does she earn? 8.75 hours, $105 (W7.9). **DIAG** option: a 3.6 l jug fills 4 cups exactly; 6 cups and 2 jugs hold 12.6 l (W7.10).
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
- **Strand.** MOE P4 multiply and divide decimals (to 2 places) by a 1-digit whole number (Decimals, p. 38). A decimal times a decimal is **Primary 5** (the beyond item).
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
- **Think harder (4).** (1) **LIST.** A decimal with two places rounds to 6.3 to the nearest tenth. Give its smallest and greatest value: 6.25 and 6.34 (W9.2). (2) **CTX.** 1 000 pupils go on a trip in buses of 45. How many buses? 22.2 means 23 buses (W9.3). (3) Round $2.33 to the nearest 10 cents ($2.30) and to the nearest dollar ($2). (4) A pack story that needs rounding up.
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
- **Think harder (3).** (1) **MULTI.** 180 sweets: 1/3 are eaten and 1/4 of the rest are given away. How many are left? 90 (Q2.5). (2) **EQ.** Dev has 5 times as many cards as Eva. Dev gives Eva 24 cards and they end with equal numbers. Find how many cards Dev had at first: 60 (and Eva 12, W10.5). (3) A fraction story with a table.
- **Go further (3).** G1 **Beyond (named): "Two Clues, Two Answers".** My number lies between 1 and 2 and has two decimal places. It rounds to 1.6 to the nearest tenth, and its digits add up to 11. Find every such number: 1.55 and 1.64 (W10.6). G2 **CHAL.** Make up a decimal riddle that has exactly two answers. G3 **MULTI.** A mixed contest set.
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
- **Strand.** MOE P4 angles: notation, measure in degrees, draw an angle of given size (Geometry, angles, p. 39). Missing angles in a fan, on a line and around a point are **Primary 5** (Angles 1.1 to 1.4, p. 42) and are labelled previews. Compass turns are enrichment (the syllabus names no compass or turns outcome).
- **Objective.** Name angles with ∠ABC; estimate, measure and draw angles to the nearest 5 degrees; find missing angles (preview); follow and reverse turns on an 8-point compass. Think harder: draw 125 degrees; missing angles; reverse a turn; three turns in a row. Go further: triangle total; a turn that ends facing a stated way; angles in a ratio.
- **Remember (6 min).** (1) A square corner is a right angle, 90 degrees. (2) A half turn is 180 degrees. (3) The four main compass points (re-taught with a card).
- **Start here (6).** (1) Write the name of an angle with three letters, ∠ABC. (2) Estimate, then measure, three angles (about 35, 110 and 65 degrees). (3) Draw ∠PQR = 65 degrees with a ruler and a protractor. (4) Circle the acute and the obtuse angles. (5) Ali faces east and turns a quarter turn clockwise: south. (6) How many degrees is 3 right angles? 270.
- **Think harder (4).** (1) Draw an angle of 125 degrees with one ray pointing left. (2) **GEO (preview).** Missing angles: 90 - (35 + 28) = 27 in a right angle; 180 - (65 + 45) = 70 on a line; 360 - (130 + 95 + 60) = 75 around a point (X2.5). (3) **BACK.** After turning 225 degrees anticlockwise Ravi faces south-east. Which way did he face at first? North (X2.2). (4) **GEO.** Ben faces north-west, turns 135 degrees clockwise and then 90 degrees anticlockwise. Which way does he face? North (X2.1). A longer chain: starting north, turn 225 degrees clockwise, 90 degrees anticlockwise, 45 degrees clockwise: south (X2.8).
- **Go further (3).** G1 **Beyond (named): "Triangle Total".** Measure the three angles of any drawn triangle and add them: about 180 degrees every time, for example 50 + 60 + 70 (X2.6). Level note: a Primary 5 and secondary idea. G2 **BACK/LOG.** Kai faces east and turns 135 degrees clockwise. Then he turns anticlockwise to face north. How many degrees is his second turn? 225 (X2.9). G3 Angle ABC is 48 degrees. Ray BD makes angle ABD three times angle DBC. Find both: 36 and 12 (X2.10).
- **Non-routine.** BACK T, GEO T, LOG G (replaced by a turn chain). The plan's "two clock hands" (LOG G) is H6.
- **Holiday overlap: HIGH, nearly total (H6).** H6 did robot turns, clock angles at o'clock, half past and ten past times, 6 degrees a minute, 30 degrees a gap, the compass with SE and 225, mirror times (2 and 10), fan angles (25, 40 and 25), a square corner cut (64 and 26, 4 times, 15 30 45), two squares overlapping (160). Do not reuse any. The plan's "turns of the minute hand" and "two clock hands" are H6 and are dropped. This lesson is built on the protractor skill (measure and draw), notation and new compass chains. Verdict: Change.
- **Numbers.** Angles to 180 degrees in steps of 5; turns in multiples of 45 degrees.
- **Home materials.** Protractor, ruler, pencil. No protractor? tell the tutor; the lesson then uses the compass card and the right-angle checker.
- **Kit (K5 compass).** A compass rose card, a loose arrow and a spare right-angle checker (in case the lesson 6 piece is lost): 3 pieces. Max used 2 (rose and arrow) plus the checker. Cut 3. Reuse K3 from lesson 6 if it is found.
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
- **Think harder (4).** (1) **GEO.** 7 identical squares are placed side by side in one row. The rectangle they form has perimeter 144 cm. Find its length and its area: 63 cm and 567 cm2 (X3.2). (2) **LIST.** List all rectangles with whole-cm sides and area 72 cm2. Which has the smallest perimeter? 8 by 9, 34 cm (X3.3). (3) A table of the rectangles with perimeter 36 cm (1 by 17 to 9 by 9) and their areas: 17, 32, 45, 56, 65, 72, 77, 80, 81 (X3.5). (4) A rectangle is twice as long as it is wide and its perimeter is 54 cm: 9 cm by 18 cm (X3.8).
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
- **Strand.** MOE P4 line symmetry: identify symmetric figures, decide if a line is a line of symmetry, complete a symmetric figure on a square grid (Geometry, line symmetry, p. 39).
- **Objective.** Find lines of symmetry of polygons and flags; complete a figure about a vertical, horizontal or diagonal line; count lines of symmetry. Think harder: how many lines, and why; a diagonal mirror; complete a pattern. Go further: a shape with a half-turn but no line; several lines.
- **Remember (6 min).** (1) Fold a square in half. (2) A rectangle has 2 lines and a square has 4. (3) Reflect a point across a line.
- **Start here (6).** (1) Is the dashed line a line of symmetry? (2) Complete a figure about a vertical line on a 6 by 6 grid. (3) Complete about a horizontal line. (4) Flags: which flag has exactly one line? (5) How many lines does an equilateral triangle have? 3. (6) A kite has 1; a parallelogram has none.
- **Think harder (4).** (1) **EXP.** How many lines of symmetry has a regular pentagon, and why? 5, one through each corner and the middle of the opposite side. (2) Complete a figure about a diagonal line. (3) **PAT.** Complete the tile pattern on a 4 by 4 grid; a given pattern of 8 shaded squares has 4 lines (X6.3). (4) A figure with one line, completed to have two.
- **Go further (3).** G1 **Beyond (named): "Turn It Half".** The S-shaped tetromino looks the same after a half turn but has no line of symmetry (X6.1, X6.2). Level note: rotational symmetry is secondary school. G2 **DIAG.** Design a 4 by 4 pattern that has two lines of symmetry and no more. G3 How many lines of symmetry does a 3-square L-tromino on a grid have? 1, a diagonal (X6.4).
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
- **Think harder (4).** (1) **BACK.** A show that lasts 1 h 55 min ends at 12:10 pm. When did it start? 10:15 am (X8.2). (2) **TAB.** A workshop runs from 13:20 to 16:05 and includes a 25-minute break. Give its length with and without the break: 2 h 45 min and 2 h 20 min (X8.2). (3) **Both orders.** A class arrives at 10:00. The Dolphin Show lasts 40 minutes (10:10, 11:00, 12:30, 14:00) and the Magic Show lasts 55 minutes (10:30, 11:45, 13:20, 14:30). They watch both with no walking time. Earliest finish? Dolphin then Magic ends 12:40; Magic then Dolphin ends 13:10, so 12:40 (X8.3). (4) A duration across noon.
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
- **Think harder (4).** (1) **GEO.** Four identical rectangles are placed round a small square to form a big square of side 21 cm. The small square has side 5 cm. Find the rectangle: 13 cm by 8 cm (area 104 cm2; the whole is 4 x 104 + 25 = 441, X9.1). (2) **CTX.** 36 posts stand at equal distances round a rectangular park, with one post at every corner. A longer side has 11 posts including the two at its ends. How many posts are on a shorter side? 9 (X9.2). (3) The big square's area from the small square's side. (4) An L-shape of equal pieces: find a missing side and the perimeter.
- **Go further (3).** G1 **Beyond (named): "Pinwheel Square".** The side of the big square times itself equals four rectangles plus the small square: (a + b) x (a + b) = 4 x a x b + (a - b) x (a - b) (X9.4). Level note: an algebra identity. G2 **GEO.** Four identical rectangles are put end to end in a row with perimeter 86 cm. The same four rectangles make a 2 by 2 block with perimeter 52 cm. Find the rectangle: 10 cm by 3 cm (X9.3). G3 **CHAL.** Design a frame puzzle with exactly one answer and give it to a partner.
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
- **Think harder (4).** (1) **TAB.** The temperatures at hours 1 to 6 are 21, 24, 26, 33, 31 and 35 degrees. Between which two hours was the greatest rise? Hours 3 and 4, a rise of 7 (Y1.1). (2) Two lines show the sales of two shops over 6 weeks: in which weeks was shop A ahead? (3) **EXP.** The sales 120, 126, 132 and 138 are drawn twice: once with a scale starting at 110 and each line worth 2, once starting at 0 with each line worth 50 (the second graph is nearly flat). Which graph makes the rise look larger, and which is fairer? (4) A scale that does not start at 0: a point at 220 is not twice a point at 160.
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
- **Think harder (4).** (1) Total 240: sectors 1/3, 1/4 and 5/12 are 80, 60 and 100 pupils, adding to 240 (Y2.1). (2) **CHAL.** A is 3/8 of the pupils. A and B together are 5/8. C is as many as B. D is the rest. 30 pupils chose C. How many pupils are there, and how many chose D? 120 and 15 (Y2.2). (3) **CMP.** A bar graph has no numbers on its axis. The red bar is 9 squares tall and the blue bar is 5 squares tall, and red has 28 more pupils. How many pupils are there in all? 98 (Y2.3). (4) The missing sector of a chart.
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
- **Go further (3).** G1 **Beyond (named): "Handshake Triangle".** 30 people shake hands once each with everyone: 435 (Y4.1). Level note: triangular numbers, secondary school. G2 **LOG.** The page numbers of two facing pages in a book add up to 509. Find the smaller page number: 254 (Y4.2). G3 **CTX.** A square pond has perimeter 80 m. A post is put every 4 m round it, one at each corner. How many posts? 20 (Y4.3).
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
- **Start here (6).** (1) List all the ways to pay 60 cents with 10-cent and 20-cent coins: 6 tens and 0 twenties, 4 tens and 1 twenty, 2 tens and 2 twenties, 0 tens and 3 twenties, so 4 ways (Y5.8). (2) 3 shirts and 2 hats: 6 outfits. (3) List the pairs of 1 to 5 that add to 6. (4) How many 2-digit numbers can be made from the cards 2, 4, 7 if digits may repeat? 9. (5) A tree diagram for 2 coins. (6) Draw a table for 3 by 4 choices.
- **Think harder (4).** (1) **WAYS.** Ravi has 3 tops, 5 pairs of trousers and 2 hats. He never wears the yellow top with the blue trousers. How many outfits? 30 - 2 = 28 (Y5.1). (2) **LIST.** How many different pairs of numbers from 1 to 9 add to 12? 3: 3 and 9, 4 and 8, 5 and 7 (Y5.3). (3) **Chance (extension).** A fair spinner has the numbers 1 to 10. Put these in order from least to most likely: a multiple of 4 (2), a number less than 4 (3), an even number (5), a number that is not 10 (9) (Y5.6). With three dice, which total is impossible: 2, 3, 18 or 19? 2 and 19 (Y5.4b). (4) Remove repeats from a list of pairs.
- **Go further (3).** G1 **Beyond (named): "Fair Spinner Game".** Two spinners, one with 1 to 4 and one with 1 to 6, are spun and added. 4 of the 24 results make 7 (Y5.5). Design a game that is fair for two players. Level note: probability is secondary school. G2 **WAYS.** Pay $2.40 using only 20-cent and 50-cent coins, with some of each kind. How many ways are there? 2: 7 twenties with 2 fifties, or 2 twenties with 4 fifties (Y5.2). G3 Count without listing: 4 shirts, 3 shorts, 2 caps and 3 pairs of socks make 72 outfits (Y5.7).
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
- **Start here (6).** (1) Ravi had some stickers. He gave away 15, got 8 more, and now has 30. How many at first? 37 (Y6.1). (2) A rope is cut in half, then 3 m is cut off one half, and 9 m is left. How long was the rope? 24 m (Q4.1). (3) Reverse one step in each of four stories. (4) A table with the steps and the reverse steps. (5) Check forwards. (6) A story with the answer at the end of the chain.
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
- **Start here (6).** (1) How many of the days of a 30-day month contain the digit 2? 12 (Y9.1). (2) List them: 2, 12 and 20 to 29. (3) Which month number contains a 5? May, which is 05. (4) A table of tens and ones for 1 to 40. (5) How many of the numbers 1 to 40 contain the digit 3? 13 (Q4.2). (6) How many days in the month have no 2?
- **Think harder (4).** (1) **LIST.** In 2027 a date is written dd/mm, for example 05/09. How many dates have a 5 anywhere? The days 05, 15 and 25 occur in each of 11 months (33) and every day of May counts (31), so 64 (Y9.2, Y9.3). (2) Fill a table of month, days with a 5 and total. (3) **WAYS.** 5 children stand in a line: 5 x 4 x 3 x 2 x 1 = 120 ways, written 5! (Y9.4). (4) 4 children: 24.
- **Go further (3).** G1 **Beyond (named): "How Fast Factorials Grow".** 6! = 720, 10! = 3 628 800 and 10! ends in 2 zeros; 20! is the first to end in four zeros (Y9.4, Y9.5). Level note: factorials are secondary school. G2 **LIST.** In 2027 how many dates dd/mm contain a 3? 80, which is all of March plus the days 3, 13, 23, 30 and 31 of the other months (Y9.6). The draft's "no digit 1" version (142) is not used. G3 **LOG.** A 3-digit number has hundreds digit 4, its tens digit is double its ones digit and its digits add to 13: 463 (Y9.7).
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

---

## 2. Level 4 at a glance

"Holiday overlap" is the section 13 verdict: **High** = the holiday course has several questions of the same type and range (the term lesson must change its items), **Med** = some, **Low/None** = little or none. "Change" in section 13 means the plan's own items collide and are replaced here. "Wave" is the build wave of section 11. The Quest lessons (10, 20, 30, 40) are Wave Q for the Quest block; their lesson body can be written in an earlier wave. "Blocking template items" are the codes of section 3 (and M18 hatching for any shaded figure).

| # | Title | Holiday overlap | Blocking template items | Wave | Safest to skip? |
|---|---|---|---|---|---|
| 1 | Across the Zeros | High | F1, F5, F6, K1, N6, N7 | B | No |
| 2 | Multiply It Many Ways | Low | F1, F2, F4, K1 | B | Fairly |
| 3 | Divisibility Detectives | High (Change) | M18, N7, K1 | B | No |
| 4 | Fraction Walls | Med | F3, K2, M18 | C | No |
| 5 | Fractions and Decimals Are Twins | Med | F20, F6, M18, N7 | B | Fairly |
| 6 | Lines That Behave | None | F8, K3, N6 | C | Beyond item only |
| 7 | Sort It Out | Low | F11, N7 | C | Yes |
| 8 | Share It Out | Low | F1, F4 | B | No |
| 9 | Count by Size | Low | F19, F12 | C | Yes, the safest of T1 |
| 10 | Challenge Day 1 and Quest | High (Change) | N3, F11 | Q | Body yes, Quest no |
| 11 | The Area Model of Multiplying | Low | F1, F2, N7 | B | Letter sums only |
| 12 | Remainder Riddles | High | none (calendar exists) | A | Fairly |
| 13 | Bar Model Builder I | High | F4 | C | No |
| 14 | Fractions with Different Names | High | F3, K2 | C | No |
| 15 | What Is Left? | High | F3, F4 | C | No |
| 16 | Mixed Numbers on the Line | High | F3, F6, K2 | C | Preview only |
| 17 | Decimals in Money and Measures | High | F4, F18, N7 | C | First half no |
| 18 | Decimals Times and Shares | Med | F1, F4, F20 | B | No |
| 19 | When Division Does Not Come Out Even | Low | F1 | B | Yes, the safest of T2 |
| 20 | Challenge Day 2 and Quest | High | N3 | Q | Body yes, Quest no |
| 21 | Solids and Their Nets | High (Change) | F9, K4 | D | Fairly |
| 22 | Angle Detectives | High (Change) | F7, K5 | C | No |
| 23 | Rectangle Rules | High (Change) | F8 | C | No |
| 24 | Frames and Paths | High (Change) | F8 | C | No |
| 25 | Cut and Rebuild | Med (Change) | F17, K6 | D | Yes |
| 26 | Mirror Patterns | High | M18 | A | Fairly |
| 27 | Cube Stacks and Views | Med | F9 | D | Yes |
| 28 | Time Travellers | Low | F16, N7 | A | First half no |
| 29 | Shape Studio: Hidden Lengths | Med | F8, K7 | C | Yes, the safest of T3 |
| 30 | Challenge Day 3 and Quest | None | N3, F15 | Q | Body yes, Quest no |
| 31 | Data Detectives: Line Graphs | High (Change) | F10, M18 | D | No |
| 32 | Pie Charts | None | F10, M18, F3 | D | No |
| 33 | Patterns and Rules in Words | Med | F12 | C | Fairly |
| 34 | Solve a Smaller Problem | Low | F15 | A | Yes |
| 35 | Make a Systematic List | Low | F13, K8 | D | Yes |
| 36 | Working Backwards | High (Change) | F4 | C | No |
| 37 | Suppose and Compare | High | F14, F4 | D | No |
| 38 | Looking Ahead to Primary 5 | Low | F9 | D | Yes |
| 39 | Count Place by Place | Med | none | A | Yes, the safest of T4 |
| 40 | Year-End Challenge and Year Quest | High | N3 | Q | Body yes, Quest no |

Counts (from section 13): "Change" lessons are 1.3, 1.10, 3.1, 3.2, 3.3, 3.4, 3.5, 4.1 and 4.6 (nine lessons where the plan's items collide with a holiday item and are replaced); the overlap column is High for 19 lessons, Med for 8, Low for 10, None for 3.

## 3. New template capabilities Level 4 needs

Codes: **N** tool-level item, **F** figure family, **K** kit page, **M** an item the Level 2 pre-flight already specifies and Level 4 shares (M1 level parametrisation, M2/M3 fraction renderer, M15 validator, M17 Quest adaptation, M18 black-and-white hatching, M19 books, M20 rewind, M21 authoring documents). Hours are template-engineer estimates, not measurements, for the Level 4 share only: where Levels 2 and 3 build the same figure first, Level 4 pays only for its extension. Nothing here edits a Level 1 tool file today; the template owner does it, one owner per file (Level 1 rule: lesson agents write only `lNN.json`, `verify/lNN_checks.py`, `AUDIT_LNN.md` and `out/lNN/`; new figures go in `figs4.py` appended to `figs2.render`).

### 3.1 Tool-level items

| Code | Item | Lessons | Hours |
|---|---|---|---|
| M1 | Level parametrisation (shared with Levels 2 and 3: `LEVEL`, a `term/l4/` folder, `l4t1l01` practice keys, "Level 4 Term 1 Lesson 4" footers, a Level 4 title list for the leak check) | all 40 | 0 extra |
| N1 | Level 4 validator lists: fractions, decimals and "÷", "×", "¢" allowed; "ratio", "percent", "average", "prime", "negative" banned on child pages; letters allowed only in the lesson 11 letter sums; "probability" and "chance" only at lesson 35 (tutor label); required `nonroutine` and `beyond` fields (M15); copy check against the P4 catalogue (own originals excluded) and a **holiday-copy check**: extract the 239 holiday question-bank items to a text file at build time and warn on a 5-word overlap with any term question | all 40 | 4 |
| N2 | Authoring briefs: a Level 4 lesson brief (the Level 1 `LESSON2_BRIEF` plus section 1 and section 13 of this document) and a Level 4 wording brief (section 1.1) before any agent starts | all 40 | 3 |
| N3 | Quest adaptation (M17): figures in gates (fractions, graphs, angles, shapes, nets), Quest Log of 4 pages for ages 9 to 11, the year scope for lesson 40, the gate-pair rule | 10, 20, 30, 40 | 5 |
| N4 | Black-and-white compliance (M18): hatch patterns for pie sectors, fraction shading, bar-model segments, line-graph series, grid shading, tangram pieces; `print/check_bw.py` on every Level 4 workbook, key and home sheet; "colour" in lesson text becomes "hatch" | all | 5 |
| N5 | Books: `print/make_term_books.py --level 4 --first 1 --last 40 --size 5 --per-term 10`, Quest Log in Books 2, 4, 6, 8, tutor notes in the key book, grown-up note in the home pack (M19) | all | 2 |
| N6 | Workbook geometry for ages 9 to 11: a "Working" box and an "Ans:" frame with the unit after the line, section instruction lines in paper style, answer lines 6 to 7 mm, body text 16 to 17 px, page-fill thresholds recalibrated so pages stay 85 percent full without the large type, "All diagrams are not drawn to scale" line on figure pages | all | 8 |
| N7 | Runner additions (shared with Levels 2 and 3 where they overlap): fraction and mixed-number fields (stacked), decimals accepted as 2.5 or 2.50, units on answers, rounding-pair answers (smallest and greatest), 24-hour time with or without a space, three-way true/false/not possible to tell, list answers in any order, degrees, formatters `{n\|dec2}`, `{n\|kg}`, `{n\|cm2}` | most | 10 |
| | **Tool-level subtotal** | | **37** |

### 3.2 Figures (new `type` values for slides, workbook, home sheet, key and practice)

| Code | Figure | Lessons | One-line spec | Hours |
|---|---|---|---|---|
| F1 | `column` | 1, 2, 8, 11, 18, 19 | Vertical add and subtract with carry and borrow marks and borrow across zeros; multiply 3 digits by 1 and 2 digits with partial products; short division of 4 digits with a remainder; empty digit boxes; letter-digit sums; one answer slot per box (extends L2 M5 and L3 X1) | 5 |
| F2 | `area_model` | 2, 11 | A grid of partial products with the factors split into place values; empty cells (shared with L3 X3) | 2 |
| F3 | `fraction` | 4, 14, 15, 16, 32 | Stacked fractions and mixed numbers in text and boxes; a wall to twelfths; bar, grid with half squares, strip; number line with fraction labels; decimal twin labels (extends L2 M2 and M3) | 6 |
| F4 | `bar_model` v2 | 2, 13, 15, 17, 18, 36, 37 | Up to 16 cells and 4 bars; unknown unit labels; money and decimal labels; before-and-after pairs; a "times as many" mode; the picture must not lie | 6 |
| F5 | `place_value` | 1 | Th H T O chart to 5 digits and decimals to 3 places with counters (extends L2 M4) | 3 |
| F6 | `number_line` modes | 1, 5, 16 | Unmarked line with two labelled points, an axis break for a non-zero start, decimal and mixed labels (L3 X5 shared) | 3 |
| F7 | `angle`, `compass`, `fan` | 22 | Rays with an arc and an angle name; a protractor drawn only in worked examples; an 8-point compass with turn arrows; a fan of rays | 8 |
| F8 | `shape2d` | 6, 23, 24, 29 | Rectangle, square and composite rectilinear figures with side labels, right-angle and parallel marks, hatched regions, a frame or path, identical pieces joined in rows or as a pinwheel, folded paper with the fold line; labels in text so the printed scale does not matter | 10 |
| F9 | `solid`, `net`, `cube_stack` | 21, 27, 38 | Cube, cuboid, prisms, pyramids, cone and cylinder with hidden edges dashed; nets on a grid with fold marks and tabs; `cube_stack` heights to 4 and a layer mode (L2 M8 shared) | 8 |
| F10 | `line_graph`, `bar_graph`, `pie_chart` | 31, 32 | Axes with a scale and an optional broken axis; one or two lines with hatch; a shaded period; a bar graph with no scale; pie chart sectors with fractions, hatch patterns and hidden sectors | 10 |
| F11 | `logic_grid` | 7, 10 | Names against items with tick and cross cells and clue lines | 3 |
| F12 | `figure_sequence` | 9, 33 | Figure 1 to 4 of a dot or square pattern with a table beside it | 3 |
| F13 | `spinner`, `dice` | 35 | A disc of n sectors, equal or unequal, with a pointer; dice faces with pips | 3 |
| F14 | `balance` | 37 | Two pans with fruit and weights, a chain of three, hatch per object (L2 M6 shared) | 3 |
| F15 | `network` extension | 30, 34 | Curved roads, labelled towns, complete graphs of 4 to 6 points | 2 |
| F16 | `timetable` and 24-hour readout | 28 | A timetable table, a timeline with am and pm and 24-hour labels | 2 |
| F17 | `tangram` and `dissection` | 25 | The seven pieces with unit areas, a rectangle cut into pieces and rebuilt | 3 |
| F18 | `scale_dial`, `jug`, mass diagram | 17 | A kitchen scale dial, a jug or bottle with a fill level, a diagram of bag and tins with units (L2 M7 shared) | 4 |
| F19 | `triangular_grid` | 9 | A triangular grid of side n with triangles outlined by size | 3 |
| F20 | `grid_100` | 5, 18 | A plain 10 by 10 grid for shading hundredths (the existing `hundred` is a numbered chart) | 1 |
| | **Figure subtotal** | | | **88** |

### 3.3 Kit pages (see section 4 for piece counts)

| Code | Kit | Lessons | Hours |
|---|---|---|---|
| K1 | `digit_cards`: 0 to 9, one set | 1, 2, 3, 10, 11 | 1 |
| K2 | `fraction_wall`: 12 strips | 4, 14, 16 | 2 |
| K3 | `right_angle`: one cut-out checker | 6, 22 | 1 |
| K4 | `nets`: cube (lettered staircase), cuboid, triangular prism, square pyramid | 21 | 3 |
| K5 | `compass`: rose card, loose arrow and a spare right-angle checker | 22 | 1 |
| K6 | `tangram`: 7 pieces | 25 | 1 |
| K7 | `rectangles`: 8 identical rectangles and 1 small square | 29 | 1 |
| K8 | `cards_1_6` and two spinner discs (discs not cut) | 35 | 1 |
| | **Kit subtotal** | | **11** |

### 3.4 Totals

Tool-level 37 + figures 88 + kits 11 = **136 hours** if everything is built (35 items). **Deferrable without blocking a lesson (18 hours):** F13 (3; lesson 35 can use drawn spinners), F14 (3; lesson 37 can describe the balance chain in words and a table), F16 (2), F17 (3; lesson 25 is the plan's enrichment and can use `shape_pieces`), F18 (4; lesson 17 can use `bar_model` for the mass diagram), F19 (3; lesson 9's Go further can draw the grid). That leaves about **118 hours**. The shared Level 2 and Level 3 items (M1, M2/M3, M5, M8, M15) are built once; if Level 4 is built first they add about 40 hours here.

### 3.5 What the engine already does for Level 4 (do not rebuild)

`number_line` with jumps, `hundred` with hatch, `table` with boxes, circles and tick boxes (two-way tables with letters need no new figure), `bar_model` in its four modes (up to the cap), `clock` with digital readout, `calendar` with any `days` (lessons 12 and 39), `grid` with polygons, squares and mirror (lessons 6, 26), `cube_stack` to height 3, `network`, `picture_graph`, `objects`, and the Quest builder with year scope.

---

## 4. Kit contracts: supplied pieces against the most a task may use

The Level 1 cut-out audit found two Reworks because piece counts were never checked against the tasks, and objected to 203 pieces in one term. `materials.kit_contract` makes the validator fail when supplied is less than max used. "Cut" is the number of pieces a grown-up cuts. Every kit page carries the standard note: one side only or its own sheet, a grown-up cuts a week before, pieces go in an envelope with the child's name, tear out along the dashed line, "no printer? use paper scraps". Cut lines at least 6 mm apart; digits that can be turned (6, 9) are underlined; nothing depends on colour. Level 4 is light because the children use real instruments and paper.

| L | Kit | Supplied | Max used by a task | Cut | Reuse and notes |
|---|---|---|---|---|---|
| 1 | K1 digit cards 0 to 9 | 10 | 10 (Explore lays them all out); tasks 6 | 10 | keep for 2, 3, 10, 11; tasks never need a repeated digit |
| 2 | reuse K1 | 0 | 4 | 0 | |
| 3 | reuse K1 | 0 | 4 | 0 | hundred chart printed, not cut |
| 4 | K2 fraction wall | 12 | 12 (Explore); tasks 6 | 12 | keep for 14, 15, 16 |
| 5 | none (two hundred grids printed, not cut) | 0 | 0 | 0 | |
| 6 | K3 right-angle checker | 1 | 1 | 1 | keep for 22; dot paper printed |
| 7 | none (logic grid printed) | 0 | 0 | 0 | |
| 8 | none | 0 | 0 | 0 | 30 small things from home |
| 9 | none (figures printed) | 0 | 0 | 0 | |
| 10 | reuse K1 | 0 | 6 | 0 | quest partner from home |
| 11 | reuse K1 | 0 | 6 | 0 | trial digits for letter sums |
| 12 | none (calendar page printed) | 0 | 0 | 0 | |
| 13 | none (bar grids printed) | 0 | 0 | 0 | |
| 14 | reuse K2 | 0 | 4 | 0 | |
| 15 | none | 0 | 0 | 0 | |
| 16 | reuse K2 | 0 | 8 | 0 | number-line page printed |
| 17 | none | 0 | 0 | 0 | |
| 18 | none (hundred grids printed) | 0 | 0 | 0 | |
| 19 | none | 0 | 0 | 0 | |
| 20 | none | 0 | 0 | 0 | quest partner from home |
| 21 | K4 nets | 4 | 4 | 4 | glue stick or tape for the grown-up |
| 22 | K5 compass card, arrow and a spare checker (reuse K3) | 3 | 2 plus the checker | 3 | protractor from home |
| 23 | none | 0 | 0 | 0 | |
| 24 | none | 0 | 0 | 0 | a sheet of paper to fold from home |
| 25 | K6 tangram | 7 | 7 | 7 | |
| 26 | none (tracing paper from home) | 0 | 0 | 0 | |
| 27 | none (14 same-size blocks from home) | 0 | 14 blocks | 0 | drawn fallback is a complete lesson (D13) |
| 28 | none (timeline strips printed) | 0 | 0 | 0 | |
| 29 | K7 identical rectangles and a small square | 9 | 9 (8 rectangles and 1 square) | 9 | |
| 30 | none | 0 | 0 | 0 | quest partner from home |
| 31 | none | 0 | 0 | 0 | |
| 32 | none (pie circle printed) | 0 | 0 | 0 | protractor from home |
| 33 | none | 0 | 0 | 0 | |
| 34 | none | 0 | 0 | 0 | 12 counters or coins from home |
| 35 | K8 cards 1 to 6 and two spinner discs (discs not cut) | 6 cards | 6 cards, 2 discs | 6 | a paper clip and a coin from home |
| 36 | none | 0 | 0 | 0 | |
| 37 | none | 0 | 0 | 0 | |
| 38 | none (layer mats printed) | 0 | 24 blocks (optional) | 0 | drawn fallback (D13) |
| 39 | none (calendar page printed) | 0 | 0 | 0 | |
| 40 | none | 0 | 0 | 0 | quest partner from home |

Cut per book: Book 1 (1 to 5) 22, Book 2 (6 to 10) 1, Book 3 (11 to 15) 0, Book 4 (16 to 20) 0, Book 5 (21 to 25) 14, Book 6 (26 to 30) 9, Book 7 (31 to 35) 6, Book 8 (36 to 40) 0. Per term: Term 1 23, Term 2 0, Term 3 23, Term 4 6; **year 52**. The heaviest single kits are the fraction wall (12) and the digit cards (10).

**The Level 4 home box** (named once in the welcome note and the lesson 1 hand-off): 30 counters or buttons or beans (never sweets), two pencils (one for hatching), an eraser, a 30 cm ruler, a protractor, a set square, scissors and tape or a glue stick for the grown-up, baking paper or tracing paper (lesson 26), 14 same-size blocks or small boxes (lessons 27 and 38 only; drawn stacks are the fallback), a coin and a paper clip (lesson 35), a calendar page (in the book), a quest partner (lessons 10, 20, 30, 40). A ruler, protractor and set square are P4 school items (decision D5). The Level 1 decision "no printed ruler" stands; lessons that need one say "no ruler? tell your tutor".

---

## 5. Hand-off materials chain

The Level 1 audits found 7 of 9 "pencil and paper only" lines false, and a missed kit between lessons 10 and 11. Rule: `parent.next_materials` of lesson n lists everything lesson n+1 needs that a family must prepare: the book (given on payment), any kit page to cut, anything kept from earlier, anything to find at home. Under the owner's decision the wording is "your next workbook is in your book; tear out the kit page along the dashed line, then a grown-up cuts out the pieces" (never "print it a week before"). Books: 1 = lessons 1 to 5, 2 = 6 to 10, 3 = 11 to 15, 4 = 16 to 20, 5 = 21 to 25, 6 = 26 to 30, 7 = 31 to 35, 8 = 36 to 40. Term breaks fall at 10 to 11, 20 to 21 and 30 to 31; book boundaries at 5 to 6, 10 to 11, 15 to 16, 20 to 21, 25 to 26, 30 to 31 and 35 to 36.

| From to | The family must have ready | Keep from before | Check and hazard |
|---|---|---|---|
| Welcome to 1 | Book 1; the Level 4 home box; the 10 digit cards cut (a grown-up cuts a week before) | | Nothing in the welcome note is a purchase except a protractor or set square if the family has none |
| 1 to 2 | Pencil, squared paper | The digit cards (lessons 2, 3, 10, 11) | |
| 2 to 3 | A pencil to hatch with; the hundred chart is in the book | The digit cards | |
| 3 to 4 | The 12 fraction-wall strips cut (a grown-up cuts a week before) | | The heaviest cut of Term 1 |
| 4 to 5 | Pencil; the hundred-grid page is in the book | The wall strips (lessons 14, 15, 16) | |
| 5 to 6 (book) | Book 2; a ruler, set square and pencil; the right-angle checker cut (1 piece) | The wall strips | Book boundary: if Book 2 arrives with a later instalment this fails (D11) |
| 6 to 7 | Pencil | The right-angle checker (lesson 22) | |
| 7 to 8 | Pencil; 30 small things | | |
| 8 to 9 | Pencil, ruler, squared paper | | |
| 9 to 10 | A quest partner (a grown-up, a sibling or a friend); the digit cards found | The digit cards | The Quest Log stays closed in Book 2 (same rule as Level 1 lesson 19 to 20) |
| 10 to 11 (term and book) | Book 3; pencil; squared paper | The digit cards (lesson 11) | Term break; new book |
| 11 to 12 | A calendar page (in the book) | | |
| 12 to 13 | Pencil, ruler, squared paper | | |
| 13 to 14 | The wall strips found | The wall strips from lesson 4 | The likeliest lost kit of Term 2 (a gap of one term break) |
| 14 to 15 | Pencil | | |
| 15 to 16 (book) | Book 4; the wall strips again; the number-line page is in the book | The wall strips | Book boundary |
| 16 to 17 | Pencil | | |
| 17 to 18 | Pencil; the hundred-grid pages are in the book | | |
| 18 to 19 | Pencil | | |
| 19 to 20 | A quest partner; the Quest Log stays closed in Book 4 | | |
| 20 to 21 (term and book) | Book 5; the 4 nets cut; tape or glue for the grown-up | | Term break; new book |
| 21 to 22 | A protractor; ruler; the compass card, arrow and spare checker cut (3 pieces) | The right-angle checker from lesson 6 | Lost-kit hazard: the checker is 16 lessons old; a spare is printed on the compass page |
| 22 to 23 | Pencil, ruler, squared paper | | |
| 23 to 24 | A sheet of paper to fold; squared paper | | |
| 24 to 25 | The 7 tangram pieces cut | | |
| 25 to 26 (book) | Book 6; tracing paper or baking paper; a small mirror if there is one | | Book boundary |
| 26 to 27 | 14 same-size blocks or small boxes (or use the drawn path) | | Fallback is a full lesson (D13) |
| 27 to 28 | A real clock if there is one; pencil | | |
| 28 to 29 | The 9 identical-rectangle pieces cut; ruler | | |
| 29 to 30 | A quest partner; the Quest Log stays closed in Book 6 | | |
| 30 to 31 (term and book) | Book 7; ruler, pencil; graph pages are in the book | | Term break; new book |
| 31 to 32 | A protractor; the pie circle is in the book | | |
| 32 to 33 | Pencil, squared paper | | |
| 33 to 34 | 12 counters or coins | | |
| 34 to 35 | The 6 cards cut; a coin and a paper clip; two dice if there are any | | |
| 35 to 36 (book) | Book 8 | | The book boundary falls here: if Book 8 comes with a later instalment it must be posted before lesson 35 ends, or this line is false (D11) |
| 36 to 37 | Pencil, squared paper | | |
| 37 to 38 | 24 same-size blocks (optional); layer mats are in the book | | Fallback drawn (D13) |
| 38 to 39 | A calendar page (in the book) | | |
| 39 to 40 | A quest partner; plain paper for the showcase puzzle; a favourite page from the year; the Quest Log stays closed in Book 8 | | |
| 40 to next | The tutor sends the next-level or next-term placement note | | Not a lesson-file concern |

---

## 6. Mi's Challenge Quest in lessons 10, 20, 30 and 40

The Level 1 Quest (lesson 20) is the model: 20 minutes at minutes 35 to 55 straight after the brain break; 8 short gates and one optional secret cave; a quest partner (a sibling, a grown-up or a friend; the tutor pairs a solo child with the tutor's example); private paper; no score, no mark, no ranking, no visible timer, no "test" or "exam" on any child or parent page; the tutor keeps private notes only (one parent line and next-term group advice); the Quest is never the part that shrinks in a slow class; the cave is the only place for a puzzle the children have not met; a child may pass any gate. Timing: Opening 2, Remember 6, Sneak-peek 4, Explore 10, Mini-lesson 9, Break 4, Quest 20, Workbook 25 (Start here only, five items, about 16 minutes for a middle child; pages 3 to 5 for home), Talk 4, Look-back 2, Flex 4. The exit ticket is an optional item at home. Three files per Quest: `LNN_Quest_Log.pdf` (**4 pages for ages 9 to 11**, in Books 2, 4, 6 and 8; D10), `LNN_Quest_Tutor_Notes.pdf` (key book), `LNN_Quest_Parent_Note.pdf` (home pack). Recording is paused for the Quest and a make-up child does the Quest before watching the recording (`rec_pause_say`).

Every lesson of the term is visited by exactly one gate. Two gates cover two lessons each (one short item from each, written as parts (a) and (b)), so ten lessons fit eight gates; the tenth lesson, the Challenge Day, has its own gate. Every gate item is at Start here level for its own lesson (so a joiner can attempt it) and every answer below was recomputed. The pairing differs by term as the tables show (Term 1: lessons 1 and 2, 4 and 5; Term 2: 11 and 12, 18 and 19; Term 3: 23 and 24, 25 and 26; Term 4: 31 and 32, 38 and 39). The Quest Log may carry figures (fractions, angles, graphs) once F3, F7 and F10 exist; until then the gate states the picture in words and the author checks that `b_quest.py` draws it.

**Gates for the Term 1 Quest (lesson 10).**

| Gate | Lessons | Item (answer) | Figure |
|---|---|---|---|
| 1 | 1, 2 | Round 36 482 to the nearest 100 (36 500); 342 x 6 (2 052) | none |
| 2 | 3 | Circle the multiples of 9: 3 504, 4 716, 5 138 (4 716) | none |
| 3 | 4, 5 | 5/6 = [ ]/18 (15); write 0.35 as a fraction in its simplest form (7/20) | `fraction` |
| 4 | 6 | In rectangle ABCD name a side parallel to AB (DC) and a side perpendicular to AB (BC or AD) | `shape2d` |
| 5 | 7 | A class of 30 has 17 girls. 12 pupils wear glasses, 5 of them girls. How many boys do not wear glasses? (13 boys, 7 with glasses, so 6) | `table` |
| 6 | 8 | 7 524 / 6 (1 254); 1 245 eggs are packed 8 to a box: how many boxes are needed? (156) | none |
| 7 | 9 | How many squares of all sizes are in a 3 by 3 grid? (14) | `grid` |
| 8 | 10 | Two numbers add to 17 and multiply to 60 (5 and 12) | none |
| Cave | beyond | The greatest multiple of 9 that rounds to 5 400 to the nearest hundred (5 445) | none |

**Gates for the Term 2 Quest (lesson 20).**

| Gate | Lessons | Item (answer) | Figure |
|---|---|---|---|
| 1 | 11, 12 | 36 x 25 (900); a bead pattern red, blue, blue, green, yellow repeats: the 23rd bead (blue) | `objects` |
| 2 | 13 | Ali has 45 more stickers than Mei and they have 189 together: Mei 72, Ali 117 | `bar_model` |
| 3 | 14 | 3/4 - 1/6 (7/12) | `fraction` |
| 4 | 15 | 3/5 of a number is 36 (60) | `bar_model` |
| 5 | 16 | Write 17/4 as a mixed number (4 1/4) | `number_line` |
| 6 | 17 | $20 - $13.65 ($6.35); 3 for $2.10 or 5 for $3.25, which is the better buy? (5 for $3.25, $0.65 each against $0.70) | none |
| 7 | 18, 19 | 4 x 1.35 (5.40); 9 / 4 (2.25) | none |
| 8 | 20 | 180 sweets: 1/3 are eaten and 1/4 of the rest are given away: how many are left? (90) | `bar_model` |
| Cave | beyond | AB + CA = ADD, different letters different digits (19 + 81 = 100, unique) | none |

**Gates for the Term 3 Quest (lesson 30).**

| Gate | Lessons | Item (answer) | Figure |
|---|---|---|---|
| 1 | 21 | How many faces, edges and vertices has a triangular prism? (5, 9, 6) | `solid` |
| 2 | 22 | Ali faces east and turns 135 degrees anticlockwise: which way? (north-west) | `compass` |
| 3 | 23, 24 | A rectangle has area 96 cm2 and length 12 cm: its width (8 cm) and perimeter (40 cm) | `shape2d` |
| 4 | 25, 26 | An 8 by 3 rectangle is cut and rebuilt as 4 by 6: the new perimeter (20 cm); lines of symmetry of a rectangle that is not a square (2) | `shape2d` |
| 5 | 27 | A stack on a 3 by 3 base has heights 2, 1, 0 / 3, 2, 1 / 1, 1, 0: how many cubes? (11) | `cube_stack` |
| 6 | 28 | A film starts at 2:50 pm and lasts 1 h 45 min: when does it end? (4:35 pm); 1920 as pm time (7:20 pm) | `clock` |
| 7 | 29 | 24 posts stand round a rectangle, 8 on a long side counting both corners: how many on a short side? (6) | `shape2d` |
| 8 | 30 | A map has towns with 3, 2, 4, 3 and 2 roads: can every road be used once? (yes, starting at a town with 3) | `network` |
| Cave | beyond | On the lettered staircase net, which letter is opposite C? (F) | `net` |

**Gates for the Year Quest (lesson 40; `scope: "year"`).**

| Gate | Lessons | Item (answer) | Figure |
|---|---|---|---|
| 1 | 31, 32 | A line graph reads 21, 24, 26, 33, 31, 35 at hours 1 to 6: between which hours was the greatest rise? (hours 3 and 4); a pie chart sector of 1/4 is 30 pupils: how many pupils in all? (120) | `line_graph`, `pie_chart` |
| 2 | 33 | Figure n has 5 x n + 2 dots: how many dots in Figure 10? (52) | `figure_sequence` |
| 3 | 34 | 6 people shake hands once with each other: how many handshakes? (15) | `network` |
| 4 | 35 | 3 shirts and 4 pairs of trousers: how many outfits? (12) | none |
| 5 | 36 | A rope is cut in half, then 3 m is cut off one half, leaving 9 m: how long was the rope? (24 m) | none |
| 6 | 37 | 10 tickets at $6 and $4 cost $52: how many $6 tickets? (6) | none |
| 7 | 38, 39 | A box 4 by 3 by 2: how many cubes? (24); how many of the numbers 1 to 40 contain the digit 3? (13) | none |
| 8 | 40 | A mix of the year: 3/4 + 1/6 (11/12); the perimeter of a 12 cm by 7 cm rectangle (38 cm) | `fraction`, `shape2d` |
| Cave | beyond | The smallest multiple of 12 that rounds to 500 to the nearest hundred (456) | none |

Quest rules for authors: wording from `BAN_FAMILY` in `b_quest.py`; "pass is always allowed"; the paired gates are two-part gates (a, b), so the Quest Log stays at 8 gates; the cave never repeats a lesson item; lessons 10, 20, 30 and 40 each lose 20 minutes, so Explore and Mini-lesson shrink to 10 and 9 and the Start here workbook becomes 25 minutes (5 Start here, 3 Think harder); the Quest and the Look-back never both run live in a slow class (Look-back is dropped first, then the optional slide, never the Quest); a child who joins at lesson 10, 20, 30 or 40 has not met earlier gates, so every gate is Start here level for its own lesson. Verified gate answers: V10.5 to V10.10, Q1.1, Q2.1 to Q2.6, Q3.1 to Q3.4, Q4.1 to Q4.3, X1.2, X10.1.

---

## 7. Spiral review across the year

The Level 1 Term 1 audit (F4) found no spiral review; Level 1 Terms 3 and 4 added "Mi's rewind". The Level 4 rule follows Level 2: holiday lessons are not reused, and holiday topics return in warm-ups only. Three layers, none of which adds minutes to the 90:

1. **Home sheet slot 5 is "Mi's rewind" (M20).** For lessons 11 to 40 the item comes from lesson n - 10 (Term 2 revisits Term 1, Term 3 revisits Term 2, Term 4 revisits Term 3). For lessons 6 to 10 it comes from lesson n - 4 (inside Term 1). Lessons 1 to 5 have no earlier lesson: slot 5 is "try it at home with real things". Items are copied by id from the earlier lesson's home or online bank, never rewritten; the answer is on the separate answer sheet.
2. **Online practice ends with two rewind items from lesson n - 5** (lessons 6 to 40).
3. **The Quest cave and the Remember warm-up.** The third Remember item is a spiral item when the prerequisite allows.

**Spiral threads (the lessons that carry each).**

| Thread | Term 1 | Term 2 | Term 3 | Term 4 |
|---|---|---|---|---|
| Place value, rounding, written methods | 1, 2, 8 | 11, 19 | none | 39 (place by place) |
| Factors, multiples, cycles | 3 | 12 | 28 (days and cycles) | 34, 39 |
| Fractions | 4, 5 | 14, 15, 16 | none | 32, 38 |
| Decimals and money | 5 | 17, 18, 19 | none | 37 (decimal unit chain) |
| Bars and unit chains | none | 13, 15, 17, 20 | 29 | 36, 37 |
| Geometry and measure | 6 | none | 21 to 29 | 38 |
| Data and tables | 7 | none | none | 31, 32 |
| Logic and heuristics | 7, 10 | 20 | 30 | 33 to 37, 40 |
| Time | none | none | 28 | 39 |

Gaps this table shows: Term 2 has no geometry or data lesson; Term 3 has no number lesson (fractions and decimals vanish for ten lessons, so the Term 3 Remember warm-ups and Mi's rewind carry them); Term 1 has no bar-model lesson (the paper spine arrives in lesson 13); Term 4 has little geometry. Mi's rewind items from Term 2 fill the Term 3 number gap. The holiday topics that Level 4 warm-ups revisit (never as the lesson): T1 rounding, bars, factor pairs, fractions, decimals, right angles, line graphs, operations, counting, guess and check (the plan's section 3); T3 and T4 draw on Terms 1 to 3, not on the holiday course, because a mid-year joiner may not have done either.

**Remember warm-ups that spiral (third item).** 11: place value (lesson 1). 12: division with a remainder (lesson 8). 13: a product as four equal bars (lesson 2). 14: the wall (lesson 4). 15: a fraction of a set (lesson 14). 16: improper fractions on a strip (lesson 4). 17: hundredths (lesson 5). 18: the area model (lesson 11). 19: division with a remainder (lesson 8). 21: faces of a box (none, a fresh start). 22: the right angle (lesson 6). 23: area of a rectangle. 24: perimeter and area (lesson 23). 25: area and perimeter (lesson 23). 26: reflection of a point. 27: cubes counted in rows. 28: 60 minutes in an hour. 29: perimeter and area (lesson 23). 31: reading a bar chart. 32: a fraction of a quantity (lesson 15). 33: the gaps of a list. 34: the sum of three numbers. 35: a table of choices (lesson 7). 36: undoing a step. 37: the difference of two prices (lesson 13). 38: fraction of a pizza (lesson 14). 39: days of the month. 40: tutor-led picks.

---

## 8. Known failure patterns from Level 1: author checklist

Read from `TERM_WIDE_AUDIT`, `CUTOUT_AUDIT`, `FINAL_AUDIT_T1`, `FINAL_AUDIT_T2` and the Level 1 fix files. Each line is something the Level 1 fix passes repaired more than once, so Level 4 authors should not write it in the first place.

1. **Kit counts do not match tasks** (strips, shape cards, tokens, counters). Fixed by the kit contract (section 4); the verify script asserts it.
2. **Hand-offs are false** ("pencil and paper only", a missing kit, "Lesson 3" meaning two things). Section 5; a hand-off check (`next_materials` against the next lesson's kit and keep list) as in Level 1.
3. **Workbook questions repeat class numbers.** No Start here or Think harder number is used in Explore, Mini-lesson, the sneak-peek or the Quest; the verify script asserts it.
4. **Answers printed on the slide while the question is asked.** Use `reveal` blocks and answer slides; Explore pictures never carry the count.
5. **Family pages use the global number.** Write "Term 3 Lesson 4"; the leak check rejects "Lesson 1" outside `lesson_in_term` 1; the next lesson of lesson 10 is "the first lesson of Term 2".
6. **Start here too long for the 28 workbook minutes.** Six Start here items (page 1 about 8 minutes, page 2 about 9, a choice about 3); say on the page that Think harder and Go further are for home. In the four Quest lessons: 5 Start here items in 25 minutes. Level 4 items are longer than Level 1 items; the modelled minutes must be re-measured with the older-child geometry (N6).
7. **Keys that accept one order only** (3 x 4 and 4 x 3). Accept both orders; "ways" lists in any order; time as 3:20 pm or 1520 or 15 20; money as $4.75; fractions equal to the same value accepted only when the key says so (simplest form is asked where it matters).
8. **Recording and camera script.** Greet by name first, then start recording; no papers held to the camera; ticks not stars; the same mic routine in every lesson; the recording sentence before anything is recorded (FINAL_AUDIT_T2 finding 4 found six lessons that said it after).
9. **"I am still stuck" route.** The look-back page the grown-up photographs to the business WhatsApp; no number on slides or in recordings.
10. **Parent page.** A "do not teach" line, a words list that explains each new term, a "when stuck" line, the beyond statement, the term line. New at Level 4: the words list explains "perpendicular", "parallel", "net", "denominator", "mixed number", "bar model", "pie chart".
11. **Runner variants.** "1 hours", "1 stickers", double full stop, raw placeholders in frames. Guard variable ranges, add a plural guard, verify every variant three ways. Level 4 adds: decimal variants never print $3.5 or 3.50 as a different answer from 3.5; fraction variants never print an unsimplified item that was not asked; mixed numbers never show a whole part of 0.
12. **Investigation page overflow.** A drawing box, 4 lines, an easy first step; tables did not fit page 5 in four Level 1 lessons.
13. **Small pictures on the workbook.** Give `size` and column width for the new figures in the first build (fractions, bars, angles, graphs, pie charts, nets).
14. **Wrong working attached to cast names.** "A child" or "a child in another class".
15. **Children cutting with scissors in the lesson.** A grown-up cuts beforehand.
16. **Contest label on a child page.** `contest_where` names the tiers; "Challenge" appears only in "Mi's Challenge Quest"; "Beyond" is a tutor-only word.
17. **Colour or glyph reliance.** Hatch, label or shape per category (M18); pie charts, graphs, fractions and tangram pieces are the new risk at Level 4.
18. **Slow-class overrun.** No part OVER in the slow-class model; the Quest is never the part that shrinks.
19. **Mi's calculator image.** Builders use `mi_dolphin_nocalc.png` once supplied; stale builds still carried the old Mi in Level 1 lessons 11 and 17 (FINAL_AUDIT_T2 finding 1): rebuild after any asset change and compare the mascot hash.
20. **A failing validator blocks rebuilds** (Level 1 lessons 3, 10, 11 and 17 failed the 7-word copy check against the in-house catalogue). Write the item in your own words from the start; the catalogue examples (EX-...) are patterns, not text; a Level 4 item that mirrors an EX item word for word will fail.
21. **The holiday overlap** (section 13). Run the holiday-copy check (N1) before the audit, not after.
22. **Scope of notation.** Stacked fractions (M2); $ and ¢ both; decimals to 3 places; "÷" allowed from lesson 8; no "ratio", "percent", "average", "prime", "negative" on child pages; letters for digits only in the lesson 11 sums.
23. **Uniqueness claims.** Any "exactly one answer" or "exactly N ways" statement in a key must be checked by brute force in `verify/lNN_checks.py` (several in this document: the digit sets of 168, 61 389, 1 004 and 9 999, the letter sums, the 11 cube nets, the two stacks views, 2 178).
24. **New at Level 4: printed scale.** Never ask a child to measure a printed length; give lengths in words; the child draws to real size with a real ruler on squared pages; angle tasks are unaffected by scale.
25. **New at Level 4: figure-dependent items.** Many P4 school items depend on a picture (`p4_non_routine_catalogue.md` section 2: the OCR text kept a bracketed note for only 62 of them, so the true share is higher); every picture-dependent item needs the drawn figure on the page and a text alternative for the key and the guide.

---

## 9. Risks

1. **Holiday repeat (High).** A holiday graduate starts Term 1 and would meet the same question types, sometimes the same numbers (section 13). Nineteen lessons rate High. Mitigation: the register, the holiday-copy check (N1), and a rule that every shared type needs new numbers and one new twist. Residual: a child who did the holiday course will still find lessons 12, 14, 15, 17, 22 and 24 partly familiar; the guide must say so honestly ("you may know some of this from the holiday course; today we go further"). The plan's own statement that Term 1 is new content must be corrected for the families.
2. **Tier honesty.** The likeliest repeats from Level 1: a contest move at Start here (digit-sum test, letter sum, pairing, "two answers", chance, a three-step chain), a written reason at Start here, a preview at Start here (mixed-number addition in lesson 16, angles on a line in lesson 22, division of a whole number to a decimal in lesson 19). Keep Start here to P4 school content with scaffolding; every beyond puzzle is Think harder or Go further.
3. **Scope of P4 versus P5.** Order of operations is P5 (owner decision, plan block 3), mixed-number addition, angles on a line and at a point, volume, decimal by decimal, fraction as division, conversions in decimal form are P5 (pp. 41 and 42); each is a labelled preview at Think harder or Go further, never Start here, and the tutor guide and parent page say so plainly with no "MOE-aligned" wording (owner decision of 22 Oct, carried over). Lesson 38 is a deliberate preview lesson.
4. **Fractions, mixed numbers and decimal notation tooling.** Nothing in the term tools renders them (M2, N7); a first build without M2 prints "3/8" as plain text and the Level 1 validator rejects it. Lessons 4, 5, 14, 15, 16, 32 and 40 cannot start until M2 and F3 exist.
5. **Evidence is missing or thin for 6 lessons** (1.9, 3.7, 4.4, 4.5 for chance, 4.8, 4.9) and for every picture-dependent item (OCR lost the pictures). The wording of those items is the author's, matched to the closest paper style. The 45 unread 2021 to 2022 papers may change the picture-heavy lessons 21 to 25 and 31 and 32.
6. **Instruments.** Lessons 6, 22 and 32 need a ruler, a set square and a protractor. A family without a protractor cannot do lesson 22 properly. D5 [Default]: assume them, list them in the welcome note, and supply a cut-out right-angle checker and a compass card as partial fallbacks.
7. **Printed scale (94.3 percent).** See headline 7 and checklist 24. A Level 4 task that asks a child to measure a printed line is wrong in the book.
8. **Colour reliance in B&W print.** Pie charts, fractions, line graphs, tangram pieces, balance objects. See M18. A figure that passes in colour and fails `check_bw.py` is not finished.
9. **Blocks at home (lessons 27 and 38).** 14 or 24 same-size blocks may not exist in every house; the drawn path must be a complete lesson (D13).
10. **Cold joiners in Terms 2 and 3.** Lesson 13 (bars) is the base of 15, 17, 18 and 36, 37; a joiner at lesson 15 may not know bars, so the Remember re-teaches one bar; trial lessons 5, 13, 21 and 31 with one cold joiner before launch (D18). A December-holiday graduate and a school-only child enter Term 1 at lesson 1 on equal terms.
11. **Reading load.** Ages 9 to 11 read more than Level 1 children, and P4 papers carry stems of three or four sentences. Child-facing strings stay under 40 words (validator warning); the tutor reads each Think harder question aloud the first time.
12. **Quest for a cold joiner.** Every gate is Start here level for its own lesson and "pass" is always allowed; the cave is optional. A child who joins at lesson 30 has not met lessons 21 to 29 and may find several gates unfamiliar; the tutor note says so.
13. **Safeguarding in lesson 40.** Children present puzzles on camera: voluntary, pass allowed, no ranking, no votes, no "best", nothing shared outside the group without a grown-up's agreement (D9 at Level 1); presentations are recorded under the existing recording statement.
14. **Print and post.** Eight books of about 38 to 44 pages; Books 2, 4, 6 and 8 contain a 4-page Quest Log (kept closed). Posting both books of a term with the first payment avoids a missing book in mid-term (D11). Level 4 workbooks may need more writing space than Level 1 pages, which raises the page count (N6).
15. **Parallel agents on shared files.** Same rule as Level 1: only the template owner edits `figs*.py`, `validate.py`, `common.py`, `b_*.py`; lesson agents write only their own files. Several agents are writing Level 1 Term 4 and Levels 2 and 3 now; a Level 1 tool change lands in the same files, so Level 4 template work rebases onto it.
16. **Authoring documents are Level 1 specific.** `AUTHORING.md` and the lesson briefs name Level 1; N2.
17. **Contest copies hidden in the plan.** Four plan items copy contest or holiday problems (headline 2); the validator's 7-word check would not catch an idea copied with new wording. A second human read of every beyond item against `docs/sasmo/g4_analysis.md` is part of the fix pass.
18. **Chance in lesson 35 is not on the MOE syllabus.** It is a labelled extension (plan open question 4); if the owner drops it, the lesson keeps listing and counting and loses the spinner (D3).
19. **The 90-minute slot problem blocks the launch.** The 2027 grid has 75-minute slots; the owner said 90 minutes and the slots must be recomputed (owner decisions of 23 Oct). A 9-to-11-year-old after school for 90 minutes is shorter than a 6-year-old's lesson in relative terms but still long; the break is 4 minutes; consider 5 (D16).
20. **Exam periods.** The plan's x.9 lessons are the safest to skip, but the P4 weighted assessments fall in Terms 1 to 3; the make-up route (recording, or a holiday class) must be written once in the parent welcome note.

---

## 10. Decisions the owner must make (defaults I chose are marked [Default])

None is irreversible. Changing a default after the build costs time, as noted.

- **D1. Holiday overlap policy.** [Default] A term lesson may use the same question type as a holiday lesson (the papers set them) but never the same numbers, context or structure, and each shared type needs one new twist; the nine "Change" lessons (1.3, 1.10, 3.1 to 3.5, 4.1, 4.6) replace the plan's items outright. Alternative: remove all contest-type overlap and leave those slots to new types. Changing after the build means rewriting Think harder and Go further of the 19 High-overlap lessons.
- **D2. Replaced contest items.** [Default] Replace the four plan items that copy contest or holiday problems (headline 2) and the impossible 1.6 item. Alternative: keep the plan's items, accepting that they are SASMO problems.
- **D3. Chance (lesson 35).** [Default] Keep as a labelled extension with a short routine (spinner order, impossible dice totals, a fair game). Alternative: drop it (plan open question 4).
- **D4. Letter sums (lesson 11).** [Default] Keep letter-digit sums at Think harder and Go further, with the note that the capital letters stand for digits and are not the "algebra letters" the holiday SPEC bans. The brute-force-unique forms used here are AB + BC = ADA, ABC + ABB = DBCB, ABC + CBA = BBAB, AB + CA = ADD and the two-answer ABC + ACD = BEBA. Alternative: no letter sums at Level 4.
- **D5. Instruments.** [Default] Every child has a ruler, a protractor and a set square; the kit supplies a right-angle checker and a compass card; "no protractor? tell your tutor". Alternative: a cut-out protractor (flimsy, and the printed scale does not affect angles).
- **D6. Previews (lessons 16, 22, 38).** [Default] Keep the P5 previews at Think harder, Go further, and lesson 38 whole, labelled "Primary 5 idea" in the guide and parent page. Alternative: make lesson 38 more contest practice (plan open question 5).
- **D7. Hints in stems.** [Default] "(Hint: draw a model.)" at Think harder for a type that is new to the term, never at Go further (paper pattern).
- **D8. Lessons without paper evidence (1.9, 3.7, 4.4, 4.5, 4.8, 4.9).** [Default] Keep as the plan has them, marked "safest to skip", the beyond item named in the tutor guide. Alternative: replace two of them with more unit-chain lessons (the paper's spine, headline 11).
- **D9. More bar-model lessons.** [Default] One dedicated lesson (13) plus an EQ item in 10 lessons. Alternative: convert lesson 9 or lesson 34 into "Bar Model Builder II" because EQ is 27 percent of the non-routine paper and there is none in Term 3 (the matrix, section 13).
- **D10. Quest Log length.** [Default] 4 pages for ages 9 to 11 (more working space), against 3 at Levels 1 to 3. Alternative: 3 pages.
- **D11. Books and payments.** [Default] Both 5-lesson books of a term come with the first payment (including the first instalment); a mid-term joiner receives the books for the lessons still to come; hand-off lines say "your book". Alternative: post each book separately (adds the book-boundary failure cases of section 5).
- **D12. Paper and print.** [Default] Print the fraction wall and the tangram on the same paper as the book; recommend thicker paper in the kit note. Alternative: card stock for lessons 4 and 25.
- **D13. Blocks for lessons 27 and 38.** [Default] 14 and 24 same-size blocks as home materials with a drawn-stack fallback that is a complete lesson. If the owner prefers, make cubes Explore-only.
- **D14. Hatch instead of colour.** [Default] Every figure carries meaning by pattern, label or shape; lesson text says "shade or hatch"; colour is optional in soft copies (owner decision of 23 Oct).
- **D15. Order of the plan.** [Default] Keep the plan's order. Graphs (Term 4) and nets (Term 3) arrive later than at most schools, and angles and symmetry are one lesson each. A child who starts at Term 1 from school meets angles only in lesson 22 (plan open question 7). Alternative: move lesson 31 to Term 1.
- **D16. Break length.** [Default] 4 minutes as in Level 1. Alternative: 5 minutes for Level 4 with 1 minute taken from Flex (as proposed for Level 2).
- **D17. Quest slot.** [Default] Minutes 35 to 55 after the brain break in lessons 10, 20, 30, 40, as in Level 1 (the owner left placement to the assistant).
- **D18. Cold-join trial.** [Default] Test lessons 5, 13, 21 and 31 with one child who has done only the holiday course, and lesson 1 with one school-only child, before launch.
- **D19. Names for wrong working.** [Default] "A child" or "a child in another class"; the error-spotter role never goes to a cast name.
- **D20. Child-visible puzzle names.** [Default] The named beyond puzzles (Close Neighbours, Swap and Subtract, Diagonal Detectives, Same in the End, Triangle Total, Squares Win, Where Did the Square Go, Pinwheel Square, Seven Bridges, Gauss's Trick, Fair Spinner Game, Mirror Number and so on) are shown to children as puzzle titles, never as "beyond" or "challenge". Alternative: tutor-only names.
- **D21. Papers.** [Default] Write with the P4 paper patterns. Please supply the roughly 45 unread 2021 and 2022 P4 papers and page images of picture-dependent items (joined rectangles, folded paper, graphs, pie charts, nets) so the wording marked "unverified" can be checked.
- **D22. Mi poses.** [Default] Use the current poses in the same places as Level 1; the owner supplies more poses later (decision of 23 Oct).
- **D23. Who builds and when.** [Default] After Level 1 Term 4 and the Level 2 and 3 shared tools settle, build N1 to N7 and the shared items, then Term 1 first (holiday graduates start there), then Terms 2, 3 and 4 as in section 11. Changing the order costs rework of figures only.
- **D24. Term price and start dates.** Not decided in `owner_decisions.md` (the website still shows S$65 a lesson); nothing in Level 4 depends on it except the payment note and prorating.
- **D25. Level 4 extension workbook.** Not part of this document. The extension workbook (Level 4) is a separate product built from the holiday question types and must not reuse term items (section 13).
- **D26. Exam-period make-up.** [Default] The x.9 lessons are the first to skip; a skipped x.9 lesson comes with a recording and no home pack. Alternative: a short home pack (plan open question 9).

---

## 11. Build order, effort and cost estimate

### 11.1 Dependencies in the content

- Written-method chain 1, 2, 8, 11, 18, 19 (one column figure); fractions 4, 14, 15, 16, 32, 38 (one figure, one renderer, one kit); bars 13, 15, 17, 18, 36, 37 (one figure); decimals 5, 17, 18, 19; geometry 6, 21 to 25, 29 (shapes, nets, tangram, rectangles); angles 22 (once); time 28 and 39; heuristics 10, 20, 30, 33 to 37, 40. The Quest in lesson 10 needs 1 to 9 fixed, lesson 20 needs 11 to 19, lesson 30 needs 21 to 29, lesson 40 needs 31 to 39.
- Lesson 37 uses the wording of lessons 13 ("units") and 36 ("undo"); lesson 29 uses lessons 23 and 24 (perimeter and area words). Wording must match the fixed wording of the earlier lesson.
- The plan says a lesson must not assume the previous one except through Remember, so the chains are a build-order and wording-consistency dependency, not a content one.

### 11.2 Waves

**Sprint A (day 0, one engineer, about a day):** M1 (shared), N1 validator and holiday-copy check, N2 briefs, N6 workbook geometry, N7 runner basics, F1 `column`, F2 `area_model`, F5 `place_value`, F6 number-line modes, F20 plain grid, K1 digit cards. Then write **lesson 1** (the pilot for Level 4 conventions: first older-child workbook, first bounds item, first term parameters).
**Sprint B (in parallel with lesson 1, two engineers):** F3 `fraction` (with L2 M2/M3), F4 `bar_model` v2, F8 `shape2d`, F7 `angle`, N4 hatch patterns, K2, K3, K5, K7.
**Wave A (existing tools after M1; start on day 0):** lessons 12, 26, 28, 34, 39 (five lessons; 26 needs only hatch patterns, 28 the small F16, 34 the small F15).
**Wave B (after Sprint A):** lessons 1, 2, 3, 5, 8, 11, 18, 19.
**Wave C (after Sprint B):** lessons 4, 6, 7, 9, 13, 14, 15, 16, 17, 22, 23, 24, 29, 33, 36.
**Sprint C (during Wave C):** F9 solids and nets, F10 graphs, F11 `logic_grid`, F12, F13, F14, F17, F18, F19, K4, K6, K8.
**Wave D (after Sprint C):** lessons 21, 25, 27, 31, 32, 35, 37, 38.
**Wave Q:** the Quest blocks of 10, 20, 30, 40, written after the term's other nine lessons have passed their fix pass (N3).
**Audit and fix per term**, then a term-wide second-round audit (guide and deck, home and parent and practice, term-wide) as for Level 1, then **one 40-lesson consistency sweep** (rewind items, hand-offs, the beyond table, the holiday-overlap register, books).

Which can be written first with the existing tools: lessons 12, 26, 28, 34 and 39 need no new figure beyond a small one; lessons 1, 2, 3, 5, 8, 11, 18 and 19 need only the Sprint A column, area model, place-value and grid figures; the ones that cannot start without a new figure family: 4, 14, 15, 16 and 32 (F3), 13 and 36 and 37 (F4), 6, 23, 24 and 29 (F8), 22 (F7), 21 and 27 and 38 (F9), 31 (F10).

**Suggested term order:** Term 1 first (holiday graduates and new joiners start there), but do not wait for all of Term 1 before starting Wave A of Terms 2 to 4; the Term 2 and Term 4 lessons with no new figure can run in parallel with Term 1 template work.

### 11.3 Effort (agent-hours, not measured)

Per-lesson figures include write (data, checks, build, view every page), wording review, independent audit and fix pass. Level 1 evidence for scale: Term 2 was about 6.5 hours of wall clock from pre-flight to the end of the first fix pass with parallel agents and template foundations first; the Level 1 Terms 3 and 4 estimate was 172 hours for 20 lessons; the Level 2 estimate is 330 for 40. Level 4 is rated slightly higher per lesson because the figures are larger and the verification (unique answers, uniqueness proofs) is heavier.

| L | Title | Write and build | Wording | Audit | Fix | Total | Why |
|---|---|---|---|---|---|---|---|
| 1 | Across the Zeros | 4.5 | 0.6 | 1.0 | 1.3 | 7.4 | place-value and column figures, bounds items |
| 2 | Multiply It Many Ways | 4.0 | 0.6 | 1.0 | 1.2 | 6.8 | area model, product puzzles |
| 3 | Divisibility Detectives | 4.5 | 0.7 | 1.0 | 1.4 | 7.6 | hatched charts, replaced contest items |
| 4 | Fraction Walls | 5.0 | 0.7 | 1.2 | 1.5 | 8.4 | first fraction figures, 12-strip kit |
| 5 | Fractions and Decimals Are Twins | 4.5 | 0.6 | 1.0 | 1.3 | 7.4 | plain hundred grid, decimal labels |
| 6 | Lines That Behave | 4.5 | 0.7 | 1.0 | 1.4 | 7.6 | instruments, real-size drawing, right-angle checker |
| 7 | Sort It Out | 3.5 | 0.5 | 1.0 | 1.0 | 6.0 | logic grid figure |
| 8 | Share It Out | 4.0 | 0.6 | 1.0 | 1.2 | 6.8 | short division figure, two scenarios |
| 9 | Count by Size | 4.0 | 0.5 | 1.0 | 1.2 | 6.7 | triangular grid, counts verified |
| 10 | Challenge Day 1 and Quest | 3.5 + 4.0 Quest | 0.6 | 1.5 | 1.8 | 11.4 | Quest plus short body |
| | **Term 1** | | | | | **76.1** | |
| 11 | The Area Model of Multiplying | 4.5 | 0.7 | 1.0 | 1.4 | 7.6 | letter-sum uniqueness |
| 12 | Remainder Riddles | 3.5 | 0.5 | 1.0 | 1.0 | 6.0 | existing figures |
| 13 | Bar Model Builder I | 5.0 | 0.8 | 1.2 | 1.6 | 8.6 | bar model v2, the paper spine |
| 14 | Fractions with Different Names | 4.5 | 0.7 | 1.0 | 1.4 | 7.6 | fraction figure, three-denominator item |
| 15 | What Is Left? | 4.5 | 0.7 | 1.0 | 1.3 | 7.5 | backwards fraction chains |
| 16 | Mixed Numbers on the Line | 4.5 | 0.7 | 1.0 | 1.4 | 7.6 | mixed-number labels, P5 preview |
| 17 | Decimals in Money and Measures | 5.0 | 0.8 | 1.2 | 1.6 | 8.6 | best buy, mass diagrams, conversions |
| 18 | Decimals Times and Shares | 4.0 | 0.6 | 1.0 | 1.3 | 6.9 | decimal columns |
| 19 | When Division Does Not Come Out Even | 3.5 | 0.5 | 1.0 | 1.0 | 6.0 | light |
| 20 | Challenge Day 2 and Quest | 3.5 + 4.0 Quest | 0.6 | 1.5 | 1.8 | 11.4 | Quest plus short body |
| | **Term 2** | | | | | **77.8** | |
| 21 | Solids and Their Nets | 5.0 | 0.7 | 1.2 | 1.5 | 8.4 | solid and net figures, fold check |
| 22 | Angle Detectives | 5.0 | 0.8 | 1.2 | 1.6 | 8.6 | angle and compass figures, protractor wording |
| 23 | Rectangle Rules | 4.0 | 0.6 | 1.0 | 1.2 | 6.8 | replaced items, dimensioned figures |
| 24 | Frames and Paths | 4.5 | 0.7 | 1.0 | 1.4 | 7.6 | composite and folded figures |
| 25 | Cut and Rebuild | 4.0 | 0.6 | 1.0 | 1.2 | 6.8 | tangram kit, paradox |
| 26 | Mirror Patterns | 4.0 | 0.6 | 1.0 | 1.2 | 6.8 | mirror grids, hatch |
| 27 | Cube Stacks and Views | 4.5 | 0.6 | 1.0 | 1.4 | 7.5 | stack figure to height 4, drawn fallback |
| 28 | Time Travellers | 4.5 | 0.7 | 1.0 | 1.4 | 7.6 | 24-hour formats, timetable |
| 29 | Shape Studio: Hidden Lengths | 4.0 | 0.6 | 1.0 | 1.3 | 6.9 | joined pieces, 9-piece kit |
| 30 | Challenge Day 3 and Quest | 3.5 + 4.0 Quest | 0.6 | 1.5 | 1.8 | 11.4 | Quest plus networks |
| | **Term 3** | | | | | **78.4** | |
| 31 | Data Detectives: Line Graphs | 4.5 | 0.7 | 1.0 | 1.4 | 7.6 | line graph figure, scales |
| 32 | Pie Charts | 4.5 | 0.7 | 1.0 | 1.4 | 7.6 | pie figure with hatch |
| 33 | Patterns and Rules in Words | 4.0 | 0.6 | 1.0 | 1.2 | 6.8 | figure sequences |
| 34 | Solve a Smaller Problem | 3.5 | 0.5 | 1.0 | 1.0 | 6.0 | light |
| 35 | Make a Systematic List | 4.0 | 0.6 | 1.0 | 1.2 | 6.8 | spinner and dice, chance wording |
| 36 | Working Backwards | 3.5 | 0.6 | 1.0 | 1.2 | 6.3 | before and after bars |
| 37 | Suppose and Compare | 4.5 | 0.7 | 1.0 | 1.4 | 7.6 | balance figure, many items |
| 38 | Looking Ahead to Primary 5 | 3.5 | 0.5 | 1.0 | 1.0 | 6.0 | layer figure |
| 39 | Count Place by Place | 3.5 | 0.5 | 1.0 | 1.0 | 6.0 | calendar counts |
| 40 | Year-End Challenge and Year Quest | 3.5 + 4.5 Quest | 0.7 | 1.5 | 1.8 | 12.0 | Year Quest and showcase |
| | **Term 4** | | | | | **72.7** | |
| | **Year** | | | | | **305.0** | plus 30 for four term-wide second-round audits (4 each), the holiday-overlap pass (6) and the 40-lesson consistency sweep (8): about **335** |

Template engineering (section 3): **136 hours** if everything is built, about **118** with the deferrals. Not in these numbers: the tutor trials (one per term and the cold-joiner trials), the owner's re-supply of the unread P4 papers (D21), and the Level 1 Term 4 tool changes that Level 4 must absorb.

**Cost to the owner in practical terms.** About 335 plus 118 to 136, so 453 to 471 agent-hours. At the Level 1 pace (eight to ten writing agents and three engineers in parallel) that is about 8 to 10 working days from the start of Sprint A to four audited terms, of which about 1.5 days is template engineering before the first Wave C lesson can be built. If template work is done serially before any lesson starts, add about 1.5 days. Printing is unchanged in kind from Level 1: eight 5-lesson books of about 38 to 44 pages, four Quest Logs, and 0 to 23 pieces a term for a grown-up to cut.

**Page budget per book (estimate from the Level 1 pattern):** 5 lessons x 5 pages, plus 1 to 2 kit pages per lesson that has a kit, a cover, contents, a blank pad so each lesson starts on a right-hand page, and a Quest Log of 4 pages in Books 2, 4, 6 and 8: about 38 to 44 pages. `term_books_spec.json` gives the true counts after a build.

---

## 12. What was not checked

- No lesson, tool or output file was run, built or validated; the tool inventory was read from the working tree, which holds uncommitted Level 1 edits by other agents (`figs2.py`, `figs3.py`, `b_*.py`, `validate.py`), so a Level 1 Term 4 change may already have added some Level 4 figure. `docs/terms/l3_preflight.md` is still being written by another agent; only its first 130 lines were read.
- Hours are estimates from the Level 1 documents and commit times, not measurements.
- MOE placements come from `docs/moe/syllabus_by_level.md` (P4 pp. 37 to 40, P5 pp. 41 and 42), not re-read against the PDF; the plan itself says its new Term 1 lessons were not re-read page by page. Whether "decimal quotient" and "rounding to a stated accuracy" are exactly as described, and the order in which schools teach topics, needs the owner's or a tutor's check.
- About 45 mostly 2021 and 2022 P4 papers and one image-only 2017 paper were not read by the paper analysis; pictures were not seen; answer keys were partly illegible. Every item that depends on a picture is "wording unverified".
- The holiday overlap was found from the holiday question banks (`qbank`), warm-ups, explore and extension lines in `p4/content/l1.js` to `l10.js`, not from the holiday slides, scripts or workbook pages one by one; section 13 is the register to confirm against those pages in the first audit.
- Items marked "verified" were recomputed by the brute-force script in section 14, not by an independent person. Figures that depend on a font or an image (the lettered net, the dot-grid quadrilateral, the pie chart) are listed as definitions, not as facts about the page.
- The 7-word copy check against the private verbatim school questions (`docs/books/private_p4_papers/`, gitignored) was **not** run: that folder was not read for this document, and the examples are original, but the first validator run should include it.
- The wording of lessons 1.9, 3.7, 4.4, 4.5 (chance), 4.8 and 4.9 is unverified against any school paper (no evidence exists).
- No child was observed; no timing was measured (the Level 1 trial has not reported yet), so the Start here modelled minutes are Level 1 numbers carried over.

---

## 13. Holiday overlap register (and non-routine check)

Source: the 239 question-bank items (60 core, 89 stretch, 90 challenge) in `p4/content/l1.js` to `l10.js`, plus each lesson's objective, warm-up, explore and extension lines. "Do not reuse" lists the numbers, contexts and structures to avoid; "Verdict" is **Change** (the plan's item collides with a holiday item and is replaced here), **Second visit** (same type allowed with new numbers and one new twist) or **New** (no holiday counterpart). The holiday lessons are H1 Factor Hunters, H2 Big Number Puzzles, H3 Operation Detectives, H4 Fraction Frontier, H5 Decimal Detectives, H6 Angle Turns, H7 Area Architects II, H8 Symmetry and Nets, H9 Data Detectives, H10 Puzzle Day.

| L | Holiday lesson touched | Do not reuse | Verdict |
|---|---|---|---|
| 1 | H2 | Rounding with a line, smallest and largest for 38 000, 5 350 and 5 400, 45 000 and 50 000, palindromes, 99 990 to 100 000, cards closest to 70 000, counting on 3 456 by 1000s, largest odd 5-digit number rounding to 90 000, 17 250 + 2 250, 3 500 | Second visit (bounds inside a difference; closest-pair cards) |
| 2 | H3 C5, C6 | 2 345 x 3, 4 236 / 6, 2 340 beads 4 times as many | New |
| 3 | H1 | Factors of 12, 28, 72; common factors of 24 and 36; lighthouses 6 and 9; buses 6 and 9; the digit sum of a multiple of 7; "exactly 3 factors"; 41 and 61 (1 left over); multiples of 4 or 6 to 100; 6s and 8s to 100; lockers; the 24 claim; an odd 4-factor number | Change (odd number of factors, 4-and-6 claim and "count multiples not of 4" replaced) |
| 4 | H4 | 1/2, 7/12, 2/3, 5/6 in order; 3/7 against 3/5; 5/6 against 2/3; 3/10 and 4/10; 12/16 from a sum of 28; 2/3 against 5/6 strips | Second visit (grids with half squares are new) |
| 5 | H5 | $3.47; 90 and 89 cents; 7.46 and 7.4; 2.46; digit cards 2, 5, 8 and 3, 6, 9; the number rounding to 10; 9.50 and 10.49 | Second visit (fraction and decimal twins are new) |
| 6 | H7 (rectangles by area only) | 9 by 7 and 15 by 4 rectangles | New |
| 7 | H9 S1 | Classes 4A and 4B with 28 boys and 63 pupils | New |
| 8 | H3 C6, H1 C3 | 4 236 / 6; 52 stickers among 4 | New (two-scenario sharing is new) |
| 9 | H6, H7 S6 | The fan of 25, 40 and 25 degrees (6 angles, 10 angles); 8 tiles with perimeter 12 to 18 | New |
| 10 | H10 | Next-door numbers 90, 624, 783; chickens and rabbits; spiders and ants; double and add 7 (43); 6th from front and back; ages 8 to 11; the 7 table riddle (91); hens and goats legs | Change (new contexts and numbers) |
| 11 | none (H3 routine items) | 2 345 x 3 | New (no cryptarithm in the holiday course) |
| 12 | H1 C2, C8, H6 C3 | Eggs with 1 left in 4s and 5s (41); 61 with 1 left for 2 to 6; the robot with 8 turns and 30 turns | Second visit |
| 13 | H3, H5, H9, H10 | 2 340 beads; 1 236 plates; Ali $56 more than Ben with $300; Ravi 3 times Siti gives 20; pen $0.85 more than pencil; $9.20 shared; Class 4A and 4B; four teams scoring 100; a cake $3 more than a drink with $40; Ben's uncle 4 times as old | Second visit (after-a-change structure) |
| 14 | H4 | The "two fractions taken, the rest is a number" structure (C2 $25, C5 10 marbles, C7 5 sweets, C9 45 pages); 3/4 as 12/16; the tank 3/8 to 3/4 | Second visit (three fractions and three denominators) |
| 15 | H4, H3, H10 | 40 beads 3/8 blue; "2/5 of a number is 16"; Siti's 150 pages; half and $6 and half (48); half and 2 more twice (32); $15 on a book then half (51) | Second visit |
| 16 | H4 | 11 slices in thirds (3 2/3); 11 quarters (2 3/4); 7/4 against 1 5/8; the 4 3/4 m ribbon in quarters | Second visit (mixed-number sums are new) |
| 17 | H5 | $3.47; 3 pens at $1.25; 4 notebooks and $2.60 change; pen $0.85 more than pencil; $9.20 shared; 1.38 m and 0.15 m taller; jug 1.45 kg and 0.85 kg; 3 apples and a pear 0.95 kg | Second visit (best buy, conversions and hourly pay are new) |
| 18 | H5 | 4.8 m ribbon in 6 pieces; $9.20 shared; $1.25 each; digit cards 3, 6, 9 | Second visit |
| 19 | H5 S2, S10, C4 | 9.50 and 10.49; 7.35 to 7.44; the number rounding to 6 and 5.5 | New (decimal quotient is new) |
| 20 | H10 | As lesson 10 | Second visit by design (new contexts) |
| 21 | H8 | The 11 nets; five in a row cannot fold; a 2 by 3 block; opposite faces on a dice (sum 7); glued and stacked dice; the open box (8 of 12); a 3 by 2 by 1 net (22 squares) | Change |
| 22 | H6 | Robot turns; clock angles at o'clock, half past and ten past; 6 degrees a minute; 30 degrees a gap; SE and 225; mirror times 2 and 10; the fan; a square corner cut 64 and 26, 4 times, 15 30 45; two squares overlapping 160 | Change |
| 23 | H7 | 12 tiles; area 30 (and 20 perimeter); area 40 and perimeter 26; area 36; 8 tiles; area 56 and length 8; 24 m fencing with and without a wall | Change |
| 24 | H7 | Corner squares from 12 by 8; three squares 2, 3, 4 side by side; a 2 m path round a 10 by 6 lawn; a 2 by 4 gap in 10 by 6; the plus shape; two crossing paths in 10 by 8 | Change |
| 25 | H7 C9, S7 | 9 by 4 into a 6 by 6 square; 6 by 4 restacked as 12 by 2 | Change |
| 26 | H8 | Letters A, B, F, H, L, T; the five 4-square shapes; 3 by 3 shading with 1 and 2 lines; 2 squares on the up-down line; 5 squares with 4 lines | Second visit (polygons, flags, 4 by 4 and 6 by 6 grids) |
| 27 | H8 | Dice and glued dice | New (stacks are absent from the holiday course) |
| 28 | H1 (buses only) | Buses 6 and 9 minutes | New |
| 29 | H7 C1 | A square cut into two rectangles each of perimeter 24 | Second visit |
| 30 | none | | New |
| 31 | H9 | The chicken-rice queue (4, 9, 18, 22, 15, 7, 3); four stories to four graphs; 45 and 60 bowls; 40, 55, 70; a scale from 40 or 100; Shops A and B; two tanks crossing at 4 hours; swimmers (50); 400 plates; 52, 54, 56, 58 on two scales | Change |
| 32 | none | | New |
| 33 | H9, H3 | Steady rises (35, 45, 60, 85); 60 plates a day; 3, 7, 10, 17, 27; the chain with the 5th number 30 | Second visit |
| 34 | H10 C4, S5 | 6th from front and back queues | New |
| 35 | H8 C8, C9, H10 C6 | Ways to shade 3 by 3; 6 coins of 10 and 50 cents | New |
| 36 | H3, H10 | x 8 - 15 = 425; half, $6, half (48); x 5 + 35 then / 5; double and add 7 (43); half and 2 twice (32); $15 on a book then half (51); the swap machine (47) | Change |
| 37 | H10, H5 | Bicycles and tricycles (47 wheels); spiders and ants (82 legs); farm legs; 15 tables seating 4 or 6 (76); cake and drink ($40); 10 coins of 20 and 50 cents ($3.80) | Second visit |
| 38 | H8 S1 | Squares in a net | New |
| 39 | H10 C1, H2 C7 | Digit 7 in 1 to 100 (19); 5-digit numbers with a digit sum of 3 | Second visit |
| 40 | H10 | As lesson 10 | Second visit by design |

**Count.** Verdict "Change": 1.3, 1.10, 3.1, 3.2, 3.3, 3.4, 3.5, 4.1 and 4.6 (global 3, 10, 21, 22, 23, 24, 25, 31, 36; nine lessons where the plan's own item collides). "Second visit": 1, 4, 5, 12, 13, 14, 15, 16, 17, 18, 20, 26, 29, 33, 37, 39, 40 (17 lessons). "New": 2, 6, 7, 8, 9, 11, 19, 27, 28, 30, 32, 34, 35, 38 (14 lessons). The plan's section "Non-routine assignments" is not reduced by this register: every type and tier in it is kept; only the instance changes.

**Rule for the extension workbook (owner decision 23 Oct).** The Level 4 extension workbook is built from the holiday question types and extends the holiday program. It must not reuse term-lesson items either: the holiday-copy check (N1) should also run against `term/l4/lessons` when the workbook is written.

**Non-routine check added to every audit.** (a) Every lesson 1 to 40 names at least one catalogue type in `contest_moves` and in the `nonroutine` field with its tier (all 40 do here). (b) No non-routine item sits at Start here (none does here). (c) No sentence overlaps a school or contest question by 7 words and no holiday question by 5 words. (d) Items needing a picture have the picture in the workbook. (e) Every "exactly one answer" or "exactly N ways" claim is brute-forced in `verify/lNN_checks.py`. (f) The four types the papers use most (EQ 214, GEO 83, LOG 70, CTX 63) are not dropped when time is short; the first cuts are the Go further parts of lessons 25, 27, 34 and 38.

**Type-by-lesson matrix as assigned here** (N = planned, `.` = not planned; lessons 1 to 40 in four groups of ten). It matches the plan's matrix in type counts; the difference is the instances, not the placement.

```
Lesson   1234567890 1234567890 1234567890 1234567890
Term     1111111111 2222222222 3333333333 4444444444
EQ       NN........ N.N...NN.N .......... .....NN..N
GEO      .....N..N. .......... .NNNN...NN ..........
LOG      NNN.NNN... NN........ .N....N..N ...N....N.
CTX      .NN....N.. .N....N.N. ...N...NN. ...N......
LIST     N..NN..... ...N...NN. ..N....... ....N...N.
MULTI    .N.......N ...NN..N.N .......... .........N
BACK     .......N.N ....NN.... .N.....N.. .....N....
CHAL     ......N..N .........N ........NN NN.......N
EXP      ..NN.N.... N......... N...NNN... NN........
TAB      ......N.N. .......... N.....NN.. N.N.......
GC       .......N.N .......... ..N....... ......N..N
PAT      ....N...N. .N...N.... .....N.... ..NN......
DIAG     .......... ...N..N... N..N.N.... .......N..
CMP      ...N...... ..N..N.... .......... .N.....N..
WAYS     .......... .......... .......... ....N...N.
POSE     .......N.. ........N. .......... .......N..
```

| Type | Lessons | Terms with it | School items (807) |
|---|---|---|---|
| EQ | 10 | T1, T2, T4 | 214 |
| GEO | 8 | T1, T3 | 83 |
| LOG | 13 | T1, T2, T3, T4 | 70 |
| CTX | 10 | T1, T2, T3, T4 | 63 |
| LIST | 9 | T1, T2, T3, T4 | 63 |
| MULTI | 7 | T1, T2, T4 | 59 |
| BACK | 7 | T1, T2, T3, T4 | 52 |
| CHAL | 8 | T1, T2, T3, T4 | 36 |
| EXP | 10 | T1, T2, T3, T4 | 35 |
| TAB | 7 | T1, T3, T4 | 31 |
| GC | 5 | T1, T3, T4 | 31 |
| PAT | 7 | T1, T2, T3, T4 | 26 |
| DIAG | 6 | T2, T3, T4 | 20 |
| CMP | 5 | T1, T2, T4 | 19 |
| WAYS | 2 | T4 | 2 |
| POSE | 3 | T1, T2, T4 | 2 |

Two observations for the owner. (1) EQ, the largest school type (27 percent of the non-routine items), is placed in Terms 1, 2 and 4 and nowhere in Term 3, the plan's own note. An EQ item can be added to lesson 23 or 24 (identical pieces in a total) at no structural cost (D9). (2) GEO (83 items) has eight lessons but only in Terms 1 and 3; the papers set joined and folded pieces in Term 3 and Term 4 weighted assessments alike. Unit chains and geometry chains are 37 percent of the paper between them.

---

## 14. Appendix: verification script

The script below is the one run for this document (standard library only, a few seconds). It prints `TOTAL checks: 273 failed: 0`. Each check id appears next to the claim it supports in the lesson specs and the Quest tables. What the id families cover:

| Ids | Lesson or section | What was recomputed |
|---|---|---|
| V1.1 to V1.6 | 1 Across the Zeros | sums, differences, rounding, rounding bounds in a difference, the smallest number from five cards that rounds to 60 000, the smallest difference from six cards, the three-step story |
| V2.1 to V2.8 | 2 Multiply It Many Ways | products, the digit sets of 168, the 4-digit digit-product bound, packs, the unique missing-digit product |
| V3.1 to V3.9 | 3 Divisibility Detectives | digit-sum tests, missing digits, the unique riddle, the two cycles, the swap-and-subtract identity, pack prices, common multiples |
| V4.1 to V4.9 | 4 Fraction Walls | equivalents, orderings, grids with half squares, the unique unit-fraction split, the nearer-to-a-half comparison |
| V5.1 to V5.8 | 5 Fractions and Decimals | conversions, rounding bounds, the unique decimal riddle, eighths, the alternating pattern |
| V6.1 to V6.4 | 6 Lines That Behave | search of simple quadrilaterals (5 by 5 dots) and pentagons (4 by 4) for the plan's impossible item; no quadrilateral with exactly three right angles; diagonals |
| V7.1 to V7.3 | 7 Sort It Out | the two-way table, the 3-person and 4-person logic puzzles (unique) |
| V8.1 to V8.6 | 8 Share It Out | divisions, round-up boxes, the two-scenario sharing, remainder bounds |
| V9.1 to V9.6 | 9 Count by Size | squares, rectangles, fan triangles, triangular-grid triangles (by coordinates), digits in page numbers |
| V10.1 to V10.10 | 10 Challenge Day 1 and the Term 1 Quest | the table and backwards items, the hints puzzle (unique), every gate answer |
| W1.1 to W1.12 | 11 The Area Model | products, unique letter sums by exhaustive search, the two-answer sum, swap sums, last digits |
| W2.1 to W2.9 | 12 Remainder Riddles | cycles, weekday arithmetic by the calendar library, remainder riddles |
| W3.1 to W3.8 | 13 Bar Model Builder I | every unit-chain answer solved by search |
| W4.1 to W4.7 | 14 Fractions with Different Names | sums and differences, unit-fraction sums (unique), sum-and-difference pairs |
| W5.1 to W5.6 | 15 What Is Left? | fraction chains forwards and backwards |
| W6.1 to W6.6 | 16 Mixed Numbers | conversions, the magic square, counts |
| W7.1 to W7.10 | 17 Decimals in Money and Measures | totals, best buy, pack prices, whole packs, hourly pay |
| W8.1 to W8.5 | 18 Decimals Times and Shares | products, shares, the paint chain, the unique missing digits |
| W9.1 to W9.6 | 19 Division with a Decimal Quotient | decimal quotients, rounding bounds, the 20th digit of 1/7 |
| W10.1 to W10.6 | 20 Challenge Day 2 and the Term 2 Quest | the bar, fraction and decimal-riddle answers and every gate |
| X1.1 to X1.6 | 21 Solids and Their Nets | folding by rolling a die over the net: 35 six-square shapes, 11 cube nets, the lettered staircase net, the two removable squares, Euler's check |
| X2.1 to X2.10 | 22 Angle Detectives | compass turn chains and missing angles |
| X3.1 to X3.8 | 23 Rectangle Rules | missing sides, 7 squares in a row, rectangles of area 72, the 81 minus a square pattern |
| X4.1 to X4.7 | 24 Frames and Paths | L-shape, frame, path, identical rectangles, folded paper, border count |
| X5.1 to X5.5 | 25 Cut and Rebuild | tangram units, the 64 and 65 paradox, Fibonacci products, two cuts and three pieces |
| X6.1 to X6.4 | 26 Mirror Patterns | half-turn symmetry of the S shape, lines of symmetry on grids |
| X7.1 to X7.3 | 27 Cube Stacks | the fewest and the most cubes for two views (275 stacks searched) |
| X8.1 to X8.6 | 28 Time Travellers | durations, both orders of two shows, the flight, hourly pay |
| X9.1 to X9.5 | 29 Shape Studio | the pinwheel, posts round a rectangle, the row-and-block pair |
| X10.1 to X10.4 | 30 Challenge Day 3 | routes through a map by exhaustive search, seven bridges |
| Y1.1 to Y10.2 | 31 to 40 | graph readings, pie fractions, pattern terms, handshakes, outfits, coin ways, backwards chains, the 2 178 number, suppositions, the balance chain, cubes in boxes, dates in 2027 containing a 5 or a 3, factorials, the Year Quest gates |
| Q1.1 to Q4.3 | Quest gates | answers not covered above |

```python
#!/usr/bin/env python3
"""verify_l4_preflight.py: brute-force checks for docs/terms/l4_preflight.md (Level 4 pre-flight).
Run with:  python3 -I verify_l4_preflight.py      (a few seconds; standard library only)
Ids: V = Term 1, W = Term 2, X = Term 3, Y = Term 4, Q = Quest gates. Every quoted answer in the document has an id here.
"""
import itertools, math, string, datetime, calendar, random, time
from fractions import Fraction as F

# ---------- helpers: letter-sum solver and dot-grid polygon search
def solve(tmpl, cap=3):
    lhs, rhs = tmpl.split('='); terms = lhs.split('+'); letters = sorted(set(tmpl) - set('+='))
    lead = {t[0] for t in terms} | {rhs[0]}
    idx = {l: i for i, l in enumerate(letters)}
    ct = [[idx[c] for c in t] for t in terms]; cr = [idx[c] for c in rhs]
    sols = []
    for perm in itertools.permutations(range(10), len(letters)):
        if any(perm[idx[l]] == 0 for l in lead): continue
        tot = 0
        for t in ct:
            v = 0
            for i in t: v = v * 10 + perm[i]
            tot += v
        r = 0
        for i in cr: r = r * 10 + perm[i]
        if tot == r:
            sols.append(dict(zip(letters, perm)))
            if len(sols) >= cap: break
    return sols

def cross(o,a,b): return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
def seg_inter(p1,p2,p3,p4):
    d1=cross(p3,p4,p1); d2=cross(p3,p4,p2); d3=cross(p1,p2,p3); d4=cross(p1,p2,p4)
    return ((d1>0)!=(d2>0)) and ((d3>0)!=(d4>0)) and d1!=0 and d2!=0 and d3!=0 and d4!=0
def simple(poly):
    n=len(poly)
    for i in range(n):
        for j in range(i+1,n):
            if j==i+1 or (i==0 and j==n-1): 
                continue
            if seg_inter(poly[i],poly[(i+1)%n],poly[j],poly[(j+1)%n]): return False
    # no three consecutive collinear
    for i in range(n):
        if cross(poly[i-1],poly[i],poly[(i+1)%n])==0: return False
    return True
def sides(poly):
    n=len(poly); return [((poly[(i+1)%n][0]-poly[i][0]),(poly[(i+1)%n][1]-poly[i][1])) for i in range(n)]
def counts(poly):
    s=sides(poly); par=perp=0
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            c=s[i][0]*s[j][1]-s[i][1]*s[j][0]; d=s[i][0]*s[j][0]+s[i][1]*s[j][1]
            if c==0: par+=1
            if d==0: perp+=1
    return par,perp
def search(k,N,want):
    pts=[(x,y) for x in range(N) for y in range(N)]
    found=[]; seen=set()
    for combo in itertools.permutations(pts,k):
        if combo[0]!=min(combo): continue
        if not simple(list(combo)): continue
        pc=counts(combo)
        if pc==want:
            key=frozenset(combo)
            if key not in seen:
                seen.add(key); found.append(combo)
                if len(found)>=3: break
    return found

class gs:                                           # namespace used by the lesson 6 checks
    simple = staticmethod(simple); search = staticmethod(search)

# Level 4 pre-flight verification, part 1 (Term 1). Every claim quoted in docs/terms/l4_preflight.md carries an id.
RESULTS = []
def check(cid, cond, note=''):
    RESULTS.append((cid, bool(cond), note))
    if not cond: print('FAIL', cid, note)
def eq(cid, got, want, note=''):
    ok = (got == want)
    RESULTS.append((cid, ok, note or f'{got!r}'))
    if not ok: print('FAIL', cid, 'got', got, 'want', want, note)

def rnd(n, base):
    return (n + base // 2) // base * base          # round half up to nearest base

# ---------------- 1.1 Across the Zeros
eq('V1.1a', 46385 + 27748, 74133); eq('V1.1b', 70000 - 24316, 45684); eq('V1.1c', 59802 - 38195, 21607)
eq('V1.1d', abs(60000 - 38000), 22000, 'estimate 60 000 - 38 000')
eq('V1.1e', (rnd(47658, 10), rnd(47658, 100), rnd(47658, 1000)), (47660, 47700, 48000))
eq('V1.2a', 10000 - 3785, 6215); eq('V1.2b', 50003 - 28479, 21524)
# T3 bounds on a difference: A rounds to 7400 and B to 2600 (nearest 100)
A = [n for n in range(0, 20000) if rnd(n, 100) == 7400]; B = [n for n in range(0, 20000) if rnd(n, 100) == 2600]
eq('V1.3a', (min(A), max(A), min(B), max(B)), (7350, 7449, 2550, 2649))
eq('V1.3b', (max(A) - min(B), min(A) - max(B)), (4899, 4701), 'greatest and smallest difference')
# T4 smallest 5-digit number from cards 1,3,6,8,9 that rounds to 60 000 (nearest ten thousand)
cands = [int(''.join(p)) for p in itertools.permutations('13689') if rnd(int(''.join(p)), 10000) == 60000]
eq('V1.4', (min(cands), len(cands)), (61389, 12))
# G1 Close Neighbours: cards 2,3,5,6,8,9 -> two 3-digit numbers, smallest positive difference
diffs = {}
for p_ in itertools.permutations('235689'):
    a = int(''.join(p_[:3])); b = int(''.join(p_[3:]))
    if a > b: diffs.setdefault(a - b, set()).add((a, b))
m = min(diffs)
eq('V1.5', (m, sorted(diffs[m])), (25, [(623, 598)]), 'smallest difference 25, one pair')
eq('V1.6a', (18460 - 3975, 18460 - 3975 + 10000, 18460 + (18460 - 3975) + (18460 - 3975 + 10000)), (14485, 24485, 57430))
eq('V1.6b', 100000 - (79996 + 2307), 17697)

# ---------------- 1.2 Multiply It Many Ways
eq('V2.1', (346 * 4, 300 * 4 + 40 * 4 + 6 * 4, 2508 * 6, 78 * 5, 612 * 7, 6 * 235, 4 * 385), (1384, 1384, 15048, 390, 4284, 1410, 1540))
eq('V2.2', (49 * 6, 50 * 6 - 6, 398 * 5, 400 * 5 - 10, 35 * 18, 70 * 9), (294, 294, 1990, 1990, 630, 630))
# T: crates: 8 equal crates and 36 loose tins = 1580 tins
eq('V2.3', (1580 - 36) / 8, 193.0)
# T: digit product 168, smallest 3-digit number
sets = sorted({tuple(sorted(d)) for d in itertools.product(range(1, 10), repeat=3) if d[0] * d[1] * d[2] == 168})
nums = sorted(int(''.join(map(str, p))) for s in sets for p in set(itertools.permutations(s)))
eq('V2.4', (sets, nums[0], nums[-1]), ([(3, 7, 8), (4, 6, 7)], 378, 873))
# T: multiplicative chain: erasers 342, rulers twice, pens 3x rulers
e = 342; r = 2 * e; p = 3 * r
eq('V2.5', (r, p, p - e), (684, 2052, 1710))
# G1 smallest 4-digit number whose digits multiply to a 4-digit number
g = next(n for n in range(1000, 10000) if math.prod(map(int, str(n))) >= 1000)
eq('V2.6', g, 2789)
all_ge = [n for n in range(1000, 10000) if math.prod(map(int, str(n))) >= 1000]
eq('V2.6b', (len(all_ge) > 0, math.prod(map(int, '2789'))), (True, 1008))
# G2 pack: 20 mugs, boxes of 6 at $27
eq('V2.7', (-(-20 // 6), -(-20 // 6) * 27, -(-20 // 6) * 6 - 20), (4, 108, 4))
eq('V2.8', [(a, b) for a in range(10) for b in range(10) if (300 + 10 * a + 4) * 7 == 2000 + 100 * b + 18], [(7, 6)], '3[a]4 x 7 = 2[b]18: 374 x 7 = 2618')

# ---------------- 1.3 Divisibility Detectives
eq('V3.1', [(n, sum(map(int, str(n))), n % 3 == 0, n % 9 == 0) for n in (4521, 7806, 9134, 5838)],
   [(4521, 12, True, False), (7806, 21, True, False), (9134, 17, False, False), (5838, 24, True, False)])
eq('V3.1b', [n for n in (138, 242, 366, 450, 5128) if n % 6 == 0], [138, 366, 450])
eq('V3.2a', [n for n in range(4170 - 4170 % 10, 4170 - 4170 % 10 + 10) if str(n).startswith('417') and n % 6 == 0], [4170, 4176])
eq('V3.2b', [n for n in range(100, 1000) if str(n)[0] == '6' and str(n)[2] == '8' and n % 9 == 0], [648])
eq('V3.2c', [n for n in range(10, 100) if n % 12 == 0 and sum(map(int, str(n))) == 9 and int(str(n)[0]) < int(str(n)[1])], [36])
# bells: bell from 9:00 every 8 min, drum from 9:04 every 12 min; first time together
bell = {8 * k for k in range(0, 40)}; drum = {4 + 12 * k for k in range(0, 40)}
tog = sorted(bell & drum)
eq('V3.3', tog[:3], [16, 40, 64], 'first together 9:16, then every 24 min')
# swap and subtract is always 9 x difference of digits
eq('V3.4', all(((10 * a + b) - (10 * b + a)) % 9 == 0 and ((10 * a + b) - (10 * b + a)) == 9 * (a - b) for a in range(1, 10) for b in range(0, 10)), True)
eq('V3.5', (math.lcm(4, 6), 12 // 4 * 3 + 12 // 6 * 5), (12, 19), 'pencils 4 for $3, erasers 6 for $5: 12 of each costs $19')
eq('V3.6', [n for n in range(300, 400) if n % 6 == 0 and n % 8 == 0], [312, 336, 360, 384])
cx = [n for n in range(10, 1000) if sum(map(int, str(n))) == 12 and n % 12 != 0]
eq('V3.7', (39 in cx, 48 % 12 == 0), (True, True), 'digit sum 12 does not make a multiple of 12: 39')
# 7 a factor of 91? 84? 78?
eq('V3.8', (91 % 7, 84 % 7, 78 % 7, [n for n in range(1, 51) if n % 3 == 0 and n % 5 == 0]), (0, 0, 1, [15, 30, 45]))
eq('V3.9', ([f for f in range(1, 19) if 18 % f == 0 and 30 % f == 0], [n for n in range(1, 61) if n % 4 == 0 and n % 6 == 0]), ([1, 2, 3, 6], [12, 24, 36, 48, 60]))

# ---------------- 1.4 Fraction Walls
eq('V4.1', (F(2, 3) == F(8, 12), F(3, 5) == F(12, 20), F(18, 24), F(20, 45), F(5, 8) < F(3, 4)), (True, True, F(3, 4), F(4, 9), True))
eq('V4.2', sorted([F(2, 3), F(3, 4), F(5, 12)]), [F(5, 12), F(2, 3), F(3, 4)])
eq('V4.3', (F(7, 12), F(9, 16), F(7, 12) > F(9, 16), F(28, 48), F(27, 48)), (F(7, 12), F(9, 16), True, F(7, 12), F(9, 16)), 'grid A 7/12 vs grid B 9/16: common denominator 48: 28/48 and 27/48')
eq('V4.4', (F(4, 9) > F(3, 7), 4 * 7, 3 * 9), (True, 28, 27))
eq('V4.5', (24 * F(5, 8), 24 * F(5, 8) - 7), (15, 8), '24 stars, 7 shaded, 5/8 needs 8 more')
eq('V4.6', (F(3, 4) * 12, 9 - 5), (9, 4), 'bar of 12 parts, 5 shaded, 3/4 needs 4 more')
# G1: unit fractions summing to 2/5 (different) and to 1/2
sol = [(a, b) for a in range(1, 200) for b in range(a + 1, 400) if F(1, a) + F(1, b) == F(2, 5)]
eq('V4.7', sol, [(3, 15)])
sol2 = [(a, b) for a in range(1, 200) for b in range(a + 1, 400) if F(1, a) + F(1, b) == F(1, 2)]
eq('V4.7b', sol2, [(3, 6)])
# G2 nearer to a half: 4/7 vs 5/12
eq('V4.8', (abs(F(4, 7) - F(1, 2)), abs(F(5, 12) - F(1, 2)), abs(F(4, 7) - F(1, 2)) < abs(F(5, 12) - F(1, 2))), (F(1, 14), F(1, 12), True))
eq('V4.9', [k for k in range(1, 24) if F(1, 3) < F(k, 24) < F(1, 2)], [9, 10, 11])

# ---------------- 1.5 Fractions and Decimals
eq('V5.1', (F(7, 10) == F(7, 10), float(F(3, 20)), float(F(3, 5)), float(F(1, 4)), float(F(9, 20)), float(F(13, 25)), float(F(3, 4))), (True, 0.15, 0.6, 0.25, 0.45, 0.52, 0.75))
eq('V5.2', sorted([F(1, 2), F(3, 10), F(45, 100), F(2, 5)]), [F(3, 10), F(2, 5), F(45, 100), F(1, 2)])
eq('V5.3', (F(43, 10), 4.3), (F(43, 10), 4.3), '4 3/10 = 4.3')
two_dp = [n for n in range(0, 1000) if rnd(n, 10) == 480]     # in hundredths: rounds to 4.8 to nearest tenth
eq('V5.4', (min(two_dp) / 100, max(two_dp) / 100), (4.75, 4.84))
dec = [n / 100 for n in range(300, 400) if (n // 10) % 10 == 2 * (n % 10) and sum(map(int, str(n))) == 12]
eq('V5.5', dec, [3.63])
eq('V5.6', (125 / 1000 == 1 / 8, 3 / 8, 5 / 8, 7 / 8), (True, 0.375, 0.625, 0.875))
seq = [7.50]
for i in range(9): seq.append(round(seq[-1] + (0.15 if i % 2 == 0 else -0.05), 2))
eq('V5.7', seq, [7.5, 7.65, 7.6, 7.75, 7.7, 7.85, 7.8, 7.95, 7.9, 8.05])
c25 = [k for k in range(1, 100) if 0.5 < k / 25 < 0.6 and round(k / 25 * 100) % 10 == 2]
eq('V5.8', c25, [13], '13/25 = 0.52')

# ---------------- 1.6 Lines That Behave
eq('V6.1', gs.search(4, 5, (2, 1)), [], 'no quadrilateral on a 5x5 dot grid has exactly 2 parallel pairs and 1 perpendicular pair (plan G item impossible)')
eq('V6.2', len(gs.search(4, 4, (0, 1))) >= 1, True, 'a quadrilateral with exactly one right angle (one perpendicular pair) and no parallel sides exists')
# exactly three right angles in a quadrilateral on a 6x6 grid? (simple quadrilaterals)
def right_angles(poly):
    n = len(poly); r = 0
    for i in range(n):
        a, b, c = poly[i - 1], poly[i], poly[(i + 1) % n]
        if (a[0] - b[0]) * (c[0] - b[0]) + (a[1] - b[1]) * (c[1] - b[1]) == 0: r += 1
    return r
pts = [(x, y) for x in range(5) for y in range(5)]
cnt = {}
for combo in itertools.permutations(pts, 4):
    if combo[0] != min(combo) or not gs.simple(list(combo)): continue
    k = right_angles(combo); cnt[k] = cnt.get(k, 0) + 1
check('V6.3', cnt.get(3, 0) == 0 and cnt.get(4, 0) > 0 and cnt.get(1, 0) > 0, f'right-angle counts of simple quadrilaterals on 5x5 grid: {sorted(cnt.items())}')
# diagonals: rectangle diagonals equal; square diagonals perpendicular (6 by 4 rectangle)
check('V6.4', math.hypot(6, 4) == math.hypot(-6, 4) and (6 * -6 + 4 * 4) != 0 and (4 * -4 + 4 * 4) == 0, 'diagonals of a 6x4 rectangle are equal and not perpendicular; of a 4x4 square they are perpendicular')

# ---------------- 1.7 Sort It Out
# two-way table: boys 22 (14 swim), girls 18 (9 not swim), total 40
boys, girls, boys_sw = 22, 18, 14; girls_not = 9
A = boys - boys_sw; B = girls - girls_not; C = girls; D = A + girls_not
eq('V7.1', (A, B, C, D, boys_sw + B, A + girls_not + boys_sw + B), (8, 9, 18, 17, 23, 40))
# logic puzzle T: 3 people, 3 pets
people = ['Ali', 'Mei', 'Ravi']; pets = ['cat', 'dog', 'fish']
sol = []
for p in itertools.permutations(pets):
    a = dict(zip(people, p))
    if a['Ali'] != 'dog' and a['Mei'] != 'fish' and a['Ravi'] != 'cat' and a['Mei'] != 'dog':   # Ali not dog; Mei not fish, not dog; Ravi not cat
        sol.append(a)
eq('V7.2', sol, [{'Ali': 'fish', 'Mei': 'cat', 'Ravi': 'dog'}])
# logic puzzle G: 4 people, 4 sports; five clues
P4 = ['Ali', 'Mei', 'Ravi', 'Siti']; S4 = ['swimming', 'chess', 'art', 'football']
sols = []
for p_ in itertools.permutations(S4):
    a = dict(zip(P4, p_))
    if (a['Ali'] not in ('art', 'chess') and a['Mei'] not in ('swimming', 'football') and a['Siti'] not in ('swimming', 'art')
            and a['Ravi'] not in ('art', 'chess') and a['Ali'] != 'football'):
        sols.append(a)
eq('V7.3', sols, [{'Ali': 'swimming', 'Mei': 'art', 'Ravi': 'football', 'Siti': 'chess'}])

# ---------------- 1.8 Share It Out
eq('V8.1', (756 // 3, 861 // 7, divmod(925, 4), 6408 // 8, 6408 % 8, 4836 // 6), (252, 123, (231, 1), 801, 0, 806))
eq('V8.2', divmod(1245, 8), (155, 5), '1 245 eggs, 8 to a box: 155 full boxes and 5 over, so 156 boxes needed')
ns = [n for n in range(1, 200) if 6 * n + 5 == 8 * n - 7]
eq('V8.3', (ns, 6 * ns[0] + 5), ([6], 41))
eq('V8.4', (8 * 135 + 6, 9 * 47 + 6), (1086, 429))
rem3 = [n for n in range(1000, 10000) if n % 7 == 3]
eq('V8.5', (rem3[0], rem3[-1]), (1004, 9999))
check('V8.6', 40 % 3 != 0 and 28 % 5 != 0, '2/3 of 40 and 3/5 of 28 are not whole numbers')

# ---------------- 1.9 Count by Size
def squares(n): return sum((n - k + 1) ** 2 for k in range(1, n + 1))
def rects(m, n): return (m * (m + 1) // 2) * (n * (n + 1) // 2)
eq('V9.1', [squares(n) for n in range(1, 7)], [1, 5, 14, 30, 55, 91])
eq('V9.2', (rects(2, 3), rects(2, 4), rects(3, 3), rects(4, 4)), (18, 30, 36, 100))
eq('V9.3', (math.comb(5, 2), math.comb(6, 2)), (10, 15), 'fan: base cut into 4 parts: 10 triangles')
def brute_tri(n):
    pts = {(i, j) for i in range(n + 1) for j in range(i + 1)}
    cnt = 0
    for (i, j) in pts:
        for k in range(1, n + 1):
            if (i + k, j) in pts and (i + k, j + k) in pts: cnt += 1
            if (i, j + k) in pts and (i + k, j + k) in pts: cnt += 1
    return cnt
eq('V9.4', [brute_tri(n) for n in range(1, 6)], [1, 5, 13, 27, 48], 'triangles of all sizes in a triangular grid of side 1..5')
eq('V9.5', sum(len(str(p)) for p in range(1, 251)), 642)
# squares by brute force on a 4x4 grid of cells
def brute_sq(n):
    c = 0
    for x in range(n):
        for y in range(n):
            for k in range(1, n + 1):
                if x + k <= n and y + k <= n: c += 1
    return c
eq('V9.6', [brute_sq(n) for n in range(1, 6)], [1, 5, 14, 30, 55])

# ---------------- 1.10 Challenge Day 1 and the Term 1 Quest
eq('V10.1', [x for x in range(0, 13) if 2 * (12 - x) + 3 * x == 29], [5], '12 notebooks, $2 and $3, $29: five $3 notebooks')
eq('V10.2', [n for n in range(1, 200) if (n - 7 + 12) % 2 == 0 and (n - 7 + 12) // 2 == 18], [31], 'bus: 7 off and 12 on, then half off, 18 remain: 31 at the start')
eq('V10.3', [(a, 25 - a) for a in range(1, 13) if a * (25 - a) == 144], [(9, 16)])
# G hints puzzle: digits 2..7 each once make three 2-digit numbers A<B<C; clues
digs = '234567'; found = []
for p_ in itertools.permutations(digs):
    nums = sorted([int(p_[0] + p_[1]), int(p_[2] + p_[3]), int(p_[4] + p_[5])])
    a, b, c = nums
    if a % 5 == 0 and sum(map(int, str(b))) == 9 and c - a == 22:
        found.append(tuple(nums))
found = sorted(set(found))
eq('V10.4', found, [(25, 36, 47)])
# Quest Term 1 gates
eq('V10.5', (rnd(36482, 100), 342 * 6), (36500, 2052))
eq('V10.6', [n for n in (3504, 4716, 5138) if n % 9 == 0], [4716])
eq('V10.7', (F(5, 6) == F(15, 18), F(35, 100)), (True, F(7, 20)))
eq('V10.8', (7524 // 6, 7524 % 6, squares(3), 17), (1254, 0, 14, 17))
eq('V10.9', [(a, 17 - a) for a in range(1, 9) if a * (17 - a) == 60], [(5, 12)])
cave = [n for n in range(5350, 5450) if n % 9 == 0]
eq('V10.10', (rnd(5445, 100), cave[-1]), (5400, 5445), 'greatest multiple of 9 that rounds to 5 400')


# Level 4 pre-flight verification, part 2 (Term 2)
lsolve = solve
import datetime
# ---------------- 2.1 Area Model of Multiplying
eq('W1.1', (40 * 30 + 40 * 6 + 7 * 30 + 7 * 6, 47 * 36, 238 * 24, 39 * 52, 40 * 50, 24 * 135), (1692, 1692, 5712, 2028, 2000, 3240))
eq('W1.2', [a for a in range(10) if 300 + 10 * a + 4 + 253 == 587], [3])
eq('W1.3', [(a, b) for a in range(10) for b in range(1, 10) if 400 + 10 * a + 7 + 100 * b + 68 == 705], [(3, 2)])
eq('W1.4', (30 * 40 + 30 * 6 + 5 * 40 + 5 * 6, 35 * 46), (1610, 1610), 'child wrote 5 x 6 = 36 and got 1616: correct total 1610')
eq('W1.5', (822 - 24 * 13, (822 - 24 * 13) / 15), (510, 34.0), 'adult ticket $34')
eq('W1.6', len(lsolve('AB+BC=ADA')), 1); eq('W1.6b', lsolve('AB+BC=ADA')[0], {'A': 1, 'B': 8, 'C': 3, 'D': 0})
eq('W1.7', [(a, b) for a in range(1, 10) for b in range(10) if int(f'{a}8') * int(f'3{b}') == 1728], [(4, 6)], '[ ]8 x 3[ ] = 1728: 48 x 36')
s2 = lsolve('ABC+ACD=BEBA', cap=10)
eq('W1.8', sorted((int(''.join(str(m[c]) for c in 'ABC')), int(''.join(str(m[c]) for c in 'ACD'))) for m in s2), [(619, 697), (719, 798)], 'two answers: 619+697=1316 and 719+798=1517')
eq('W1.9', [(318, 813, 1131)] == [(int(''.join(str(m[c]) for c in 'ABC')), int(''.join(str(m[c]) for c in 'CBA')), 1131) for m in lsolve('ABC+CBA=BBAB')], True)
eq('W1.10', all((10 * a + b) + (10 * b + a) == 11 * (a + b) for a in range(1, 10) for b in range(0, 10)), True)
eq('W1.11', (pow(3, 25, 10), pow(7, 12, 10)), (3, 1))

# ---------------- 2.2 Remainder Riddles
pat = ['R', 'B', 'B', 'G', 'Y']
eq('W2.1', (pat[(20 - 1) % 5], pat[(47 - 1) % 5]), ('Y', 'B'))
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
eq('W2.2', days[(days.index('Tue') + 100) % 7], 'Thu')
eq('W2.3', [n for n in range(30, 51) if n % 5 == 2 and n % 4 == 3], [47])
w = 'SINGAPORE'
eq('W2.4', (w[(100 - 1) % 9], len(w)), ('S', 9))
eq('W2.5', [n for n in range(1, 200) if n % 4 == 3 and n % 5 == 4 and n % 6 == 5], [59, 119, 179], 'one short each time: 59, then every 60')
eq('W2.6', (datetime.date(2027, 1, 1).strftime('%A'), datetime.date(2028, 1, 1).strftime('%A'), (datetime.date(2028, 1, 1) - datetime.date(2027, 1, 1)).days), ('Friday', 'Saturday', 365))
eq('W2.7', [n for n in range(1, 100) if n % 3 == 1 and n % 4 == 2 and n % 5 == 3], [58])

# ---------------- 2.3 Bar Model Builder I
eq('W3.1', (38 + 45, 38 + 83, (154 - 28) // 2, (154 - 28) // 2 + 28, 248 // 4, 248 // 4 * 3), (83, 121, 63, 91, 62, 186))
eq('W3.2', (322 // 7, 322 // 7 * 2, 3 * 46 + 2 * 92), (46, 92, 322))
eq('W3.3', ((480 - 120) // 4, (480 - 120) // 4 + 120), (90, 210), 'sofa and 3 cushions $480, sofa $120 more')
eq('W3.4', ((190 - 46) // 2, (190 + 46) // 2), (72, 118))
# G1 same in the end
tot = 840; e = (tot - 60 + 45 - 15) // 3
eq('W3.5', (e, e + 60, e - 45, e + 15, (e + 60) + (e - 45) + (e + 15)), (270, 330, 225, 285, 840))
eq('W3.6', (1230 // 3, 410 + 55, 410 - 40, 410 + 465 + 370), (410, 465, 370, 1245))
r = next(r for r in range(1, 1000) if 4 * r - 36 == 2 * (r + 36))
eq('W3.7', (r, 4 * r, 4 * r - 36, r + 36), (54, 216, 180, 90))

# ---------------- 2.4 Fractions with Different Names
eq('W4.1', (F(1, 2) + F(1, 4), F(2, 3) + F(1, 6), F(5, 6) - F(1, 3), F(7, 8) - F(3, 4), F(5, 12) + F(1, 3), F(3, 4) + F(5, 6)), (F(3, 4), F(5, 6), F(1, 2), F(1, 8), F(3, 4), F(19, 12)))
eq('W4.2', (F(2, 3) + F(3, 4), F(5, 6) - F(1, 4)), (F(17, 12), F(7, 12)))
lst = [F(1, 3), F(2, 5), F(3, 4), F(1, 4), F(3, 5), F(7, 12)]
eq('W4.3', sorted((a, b) for a, b in itertools.combinations(lst, 2) if a + b == 1), sorted([(F(3, 4), F(1, 4)), (F(2, 5), F(3, 5))]))
tri = [(a, b, c) for a in range(2, 13) for b in range(a + 1, 13) for c in range(b + 1, 13) if F(1, a) + F(1, b) + F(1, c) == 1]
eq('W4.4', tri, [(2, 3, 6)], 'three different unit fractions with denominators up to 12 that make 1: only 1/2 + 1/3 + 1/6')
eq('W4.5', [(x, y) for x in range(1, 13) for y in range(1, 13) if F(1, x) + F(1, y) == F(7, 12) and F(1, x) - F(1, y) == F(1, 12)], [(3, 4)])
left = 1 - (F(1, 3) + F(1, 4) + F(1, 6))
eq('W4.6', (left, 15 / left), (F(1, 4), 60))

# ---------------- 2.5 What Is Left?
eq('W5.1', (F(3, 8) * 72, 45 - F(2, 5) * 45, 84 / (1 - F(3, 7))), (27, 27, 147))
mon = F(3, 8) * 480; rest = 480 - mon; tue = F(2, 5) * rest
eq('W5.2', (mon, rest, tue, mon - tue), (180, 300, 120, 60))
mang = 120; a = mang - mang // 3; b = a - a // 4; c = b - 20
eq('W5.3', (a, b, c), (80, 60, 40), '120 mangoes: sells 1/3, then 1/4 of the rest, then 20: 40 left')
eq('W5.4', (135 * F(2, 3) ** 3, 40 / F(8, 27)), (40, 135))

# ---------------- 2.6 Mixed Numbers on the Line
eq('W6.1', (F(17, 5), F(13, 3), F(2, 1) + F(5, 8) + F(1) + F(3, 4), F(21, 4) - F(11, 4)), (F(17, 5), F(13, 3), F(35, 8), F(5, 2)))
eq('W6.2', (F(3, 2) + 4 * F(3, 4), F(43, 6) - F(11, 3)), (F(9, 2), F(7, 2)), '5th number 4 1/2; gap 7 1/6 - 3 2/3 = 3 1/2')
# magic square 3x3 with entries 1/2..4 1/2 (steps of 1/2): constant 7 1/2
lo = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
ms = [[F(x, 2) for x in row] for row in lo]
sums = [sum(r) for r in ms] + [sum(ms[i][j] for i in range(3)) for j in range(3)] + [sum(ms[i][i] for i in range(3)), sum(ms[i][2 - i] for i in range(3))]
eq('W6.3', set(sums), {F(15, 2)})
eq('W6.4', sorted(x for row in ms for x in row), [F(k, 2) for k in range(1, 10)])

# ---------------- 2.7 Decimals in Money and Measures
D = lambda s: F(s)
eq('W7.1', (D('3.45') + D('2.80'), 10 - D('6.35'), D('4.75') + D('2.9'), 5 - D('2.36')), (D('6.25'), D('3.65'), D('7.65'), D('2.64')))
per = {'6 for 4.80': D('4.80') / 6, '4 for 3.40': D('3.40') / 4, '10 for 7.50': D('7.50') / 10}
eq('W7.2', (min(per, key=per.get), [float(v) for v in per.values()]), ('10 for 7.50', [0.8, 0.85, 0.75]))
eq('W7.3', (math.lcm(3, 4), math.lcm(3, 4) // 3 * D('4.50'), math.lcm(3, 4) // 4 * D('3.20'), math.lcm(3, 4) // 3 * D('4.50') + math.lcm(3, 4) // 4 * D('3.20')), (12, D('18.00'), D('9.60'), D('27.60')))
eq('W7.4', (D('4.2') / 6, D('4.2') / 6 * 3), (D('0.7'), D('2.1')))
pen = (D('23.30') - 2 * D('5.20')) / 3
eq('W7.5', (pen, pen + D('5.20')), (D('4.30'), D('9.50')))
eq('W7.6', (D('2.35') * 100, D('7.5') * 1000, D('3.04') * 1000, 4 + D('0.07')), (235, 7500, 3040, D('4.07')))
eq('W7.7', [(a, b) for a in range(0, 5) for b in range(0, 4) if 6 * a + 8 * b == 24], [(0, 3), (4, 0)])
eq('W7.8', (4 * D('5.40'), 3 * D('6.80')), (D('21.60'), D('20.40')))
eq('W7.9', ((17 * 60 + 5 - (8 * 60 + 20)) / 60, (17 * 60 + 5 - (8 * 60 + 20)) / 60 * 12), (8.75, 105.0))
eq('W7.10', (D('3.6') / 4, 6 * D('3.6') / 4 + 2 * D('3.6')), (D('0.9'), D('12.6')))

# ---------------- 2.8 Decimals Times and Shares
eq('W8.1', (3 * D('2.45'), 4 * D('0.75'), D('7.2') / 4, D('9.60') / 4), (D('7.35'), D('3.00'), D('1.8'), D('2.40')))
used = D('6.4') / 4
eq('W8.2', (used, (D('6.4') - used) / 3), (D('1.6'), D('1.6')))
sol = [(P, P + D('3.6')) for P in [D(x) / 10 for x in range(1, 200)] if P == 2 * (P + D('3.6') - D('5.4'))]
eq('W8.3', sol, [(D('3.6'), D('7.2'))], 'Ong 7.2 l, Pang 3.6 l')
eq('W8.4', (D('0.3') * D('0.4')), D('0.12'))
eq('W8.5', [(b, x) for b in range(10) for x in [(300 + 10 * b + 6) * 7] if f'{x:04d}'[0:1] == '2' and str(x)[-2:] == '12' and str(x)[:-2][0] == '2'], [(1, 2212)], '3.[ ]6 x 7 = 2[ ].12: b = 1, 3.16 x 7 = 22.12')

# ---------------- 2.9 When Division Doesn't Come Out Even
eq('W9.1', (D(7) / 4, D(9) / 5, D(3) / 8, round(2 / 3, 2), round(7 / 3, 2)), (D('1.75'), D('1.8'), D('0.375'), 0.67, 2.33))
bounds = [n for n in range(0, 2000) if rnd(n, 10) == 630]
eq('W9.2', (min(bounds) / 100, max(bounds) / 100), (6.25, 6.34), '2 d.p. numbers that round to 6.3')
eq('W9.3', (-(-1000 // 45), 1000 / 45), (23, 22.22222222222222), '1000 pupils, 45 to a bus: 23 buses')
dig = []
r_ = 1
for i in range(24):
    r_ *= 10; dig.append(r_ // 7); r_ %= 7
eq('W9.4', (dig[:6], dig[19]), ([1, 4, 2, 8, 5, 7], 4), '1/7 = 0.142857 repeating: 20th digit is 4')
eq('W9.5', (round(1 / 3, 2), [round(x, 2) for x in (5 / 6, 1 / 6)], round(8 / 3, 1)), (0.33, [0.83, 0.17], 2.7))

# ---------------- 2.10 Quest Term 2 gates (answers)
eq('W10.1', (36 * 25, 72 * 15 // 3 * 0 + 13 * 24), (900, 312))
eq('W10.2', (days[(days.index('Fri') + 30) % 7],), ('Sun',))
eq('W10.3', (300 - 78, F(3, 4) - F(1, 3), D('8.40') / 6), (222, F(5, 12), D('1.40')))

# Level 4 pre-flight verification, part 3 (Term 3)

# ---------------- cube-net folding by rolling a die over the net
def fold_labels(cells):
    cells = set(cells); start = min(cells)
    # die faces: B bottom, T top, N, S, E, W ; (r, c): row increases southwards, column eastwards
    def roll(state, d):
        B, T, N, S, E, W = state
        if d == 'E': return (E, W, N, S, T, B)       # tip over east edge: east face becomes bottom
        if d == 'W': return (W, E, N, S, B, T)
        if d == 'N': return (N, S, T, B, E, W)
        if d == 'S': return (S, N, B, T, E, W)
    lab = {}; seen = {start}; stack = [(start, ('B', 'T', 'N', 'S', 'E', 'W'))]
    while stack:
        (r, c), st = stack.pop(); lab[(r, c)] = st[0]
        for d, (dr, dc) in (('E', (0, 1)), ('W', (0, -1)), ('N', (-1, 0)), ('S', (1, 0))):
            nb = (r + dr, c + dc)
            if nb in cells and nb not in seen:
                seen.add(nb); stack.append((nb, roll(st, d)))
    return lab
def is_cube_net(cells):
    if len(cells) != 6: return False
    lab = fold_labels(cells)
    return len(lab) == 6 and len(set(lab.values())) == 6
OPP = {'B': 'T', 'T': 'B', 'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}
def connected(cells):
    cells = set(cells); st = [next(iter(cells))]; seen = {st[0]}
    while st:
        r, c = st.pop()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nb = (r + dr, c + dc)
            if nb in cells and nb not in seen: seen.add(nb); st.append(nb)
    return len(seen) == len(cells)
def norm(cells):
    mr = min(r for r, c in cells); mc = min(c for r, c in cells)
    return frozenset((r - mr, c - mc) for r, c in cells)
def variants(cells):
    out = set(); cur = set(cells)
    for _ in range(2):
        for _ in range(4):
            cur = {(c, -r) for r, c in cur}; out.add(norm(cur))
        cur = {(r, -c) for r, c in cur}
    return out
# enumerate free hexominoes
def grow(polys):
    new = set()
    for p in polys:
        for (r, c) in p:
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                q = (r + dr, c + dc)
                if q not in p: new.add(norm(set(p) | {q}))
    return new
polys = {frozenset([(0, 0)])}
for _ in range(5): polys = grow(polys)
free = {min(sorted(map(sorted, variants(p)))[0:1] and [frozenset(map(tuple, v)) for v in variants(p)], key=lambda f: sorted(f)) for p in polys}
nets = [p for p in free if is_cube_net(p)]
eq('X1.1', (len(free), len(nets)), (35, 11), '35 free hexominoes, 11 fold into a cube')
# G: staircase net A B / C D / E F
st = {(0, 0): 'A', (0, 1): 'B', (1, 1): 'C', (1, 2): 'D', (2, 2): 'E', (2, 3): 'F'}
lab = fold_labels(set(st))
faces = {lab[k]: st[k] for k in st}
opp = sorted(tuple(sorted((faces[f], faces[OPP[f]]))) for f in faces if f < OPP[f])
eq('X1.2', (is_cube_net(set(st)), opp), (True, [('A', 'D'), ('B', 'E'), ('C', 'F')]), 'staircase net: A opposite D, B opposite E, C opposite F')
# T: a 7-square shape that becomes a cube net when one square is removed (and which squares)
seven = {(0, 1), (1, 0), (1, 1), (1, 2), (1, 3), (2, 1), (2, 2)}      # cross-like with two extras
rem = [x for x in sorted(seven) if is_cube_net(seven - {x})]
eq('X1.3', rem, [(2, 1), (2, 2)], 'exactly two squares can be crossed out to leave a cube net')
# solids: Euler
solids = {'cube': (6, 12, 8), 'cuboid': (6, 12, 8), 'triangular prism': (5, 9, 6), 'pentagonal prism': (7, 15, 10), 'square pyramid': (5, 8, 5), 'hexagonal pyramid': (7, 12, 7)}
eq('X1.4', all(f - e + v == 2 for f, e, v in solids.values()), True)
# prism with n-gon base: faces n+2, edges 3n, vertices 2n ; pyramid: faces n+1 edges 2n vertices n+1
eq('X1.5', all((n + 2, 3 * n, 2 * n) == solids[k] for n, k in ((3, 'triangular prism'), (5, 'pentagonal prism'))) and all((n + 1, 2 * n, n + 1) == solids[k] for n, k in ((4, 'square pyramid'), (6, 'hexagonal pyramid'))), True)

# ---------------- 3.2 Angle Detectives
def turn(deg, moves):
    for m in moves: deg = (deg + m) % 360
    return deg
names = {0: 'N', 45: 'NE', 90: 'E', 135: 'SE', 180: 'S', 225: 'SW', 270: 'W', 315: 'NW'}
eq('X2.1', names[turn(315, [135, -90])], 'N', 'facing NW, 135 clockwise then 90 anticlockwise')
eq('X2.2', names[(135 + 225) % 360], 'N', 'after 225 anticlockwise Ravi faces SE: at first he faced N')
eq('X2.3', names[turn(270, [45, -135, 90])], 'W', 'W, 45 cw, 135 acw, 90 cw: W again')
eq('X2.5', (90 - (35 + 28), 180 - (65 + 45), 360 - (130 + 95 + 60)), (27, 70, 75))
eq('X2.6', (50 + 60 + 70, 180), (180, 180))
# T: 3 turns -> direction and total turned
eq('X2.8', names[turn(0, [225, -90, 45])], 'S', 'N, 225 cw, 90 acw, 45 cw: S')

# ---------------- 3.3 Rectangle Rules
eq('X3.1', (84 // 7, (54 // 2) - 16, int(64 ** 0.5), 36 // 4), (12, 11, 8, 9))
s = 144 // (2 * 8)
eq('X3.2', (s, 7 * s, 7 * s * s), (9, 63, 567), '7 identical squares in a row, perimeter 144: side 9 cm')
pairs72 = [(a, 72 // a) for a in range(1, 73) if 72 % a == 0 and a <= 72 // a]
eq('X3.3', (pairs72, [2 * (a + b) for a, b in pairs72]), ([(1, 72), (2, 36), (3, 24), (4, 18), (6, 12), (8, 9)], [146, 76, 54, 44, 36, 34]))
sols = [(a, 24 - a) for a in range(1, 13) if a * (24 - a) == 135]
eq('X3.4', sols, [(9, 15)])
ar = {a: a * (18 - a) for a in range(1, 10)}
eq('X3.5', all(ar[a] == 81 - (9 - a) ** 2 for a in ar) and max(ar.values()) == 81, True, 'perimeter 36: area = 81 - k^2')

# ---------------- 3.4 Frames and Paths
eq('X4.1', (12 * 9 - 5 * 4, 2 * (12 + 9), 26 * 21 - 20 * 15), (88, 42, 246))
eq('X4.2', [(x, 3 * x) for x in range(1, 20) if 2 * (x + 3 * x) == 40], [(5, 15)], 'three identical rectangles side by side make a square: 15 by 5')
check('X4.3', 15 * 15 == 3 * 15 * 5 and 4 * 15 == 60, 'square side 15, perimeter 60, area 225')
eq('X4.4', [w for w in range(1, 60) if 2 * (15 + w) == 62], [16], 'folded rectangle perimeter 62 with side 15: the other side is 16')
eq('X4.5', (24 // 2 // 2, 4 * 12, 12 * 12, 24 * 24 // 4), (6, 48, 144, 144))
eq('X4.6', [(n, 4 * n - 4, n * n - (n - 2) ** 2) for n in range(2, 8)], [(n, 4 * n - 4, 4 * n - 4) for n in range(2, 8)])

# ---------------- 3.5 Cut and Rebuild
eq('X5.1', (2 * 4 + 2 + 2 + 2 + 2, 16), (16, 16), 'tangram pieces in small-triangle units: 2x4 + 2 + 2x1 + 2 + 2 = 16')
eq('X5.2', (8 * 8, 5 * 13, 5 * 13 - 8 * 8), (64, 65, 1))
eq('X5.3', (2 * (8 + 3), 2 * (4 + 6), 8 * 3, 4 * 6), (22, 20, 24, 24), '8 by 3 cut in two and restacked to 4 by 6: area 24, perimeter 22 to 20')
fib = [1, 1, 2, 3, 5, 8, 13]
eq('X5.4', all(fib[i] * fib[i + 2] - fib[i + 1] ** 2 in (1, -1) for i in range(5)), True)

# ---------------- 3.6 Mirror Patterns
def lines_of_symmetry(cells, n):
    cells = set(cells); cnt = []
    tr = {'vertical': lambda r, c: (r, n - 1 - c), 'horizontal': lambda r, c: (n - 1 - r, c), 'diag': lambda r, c: (c, r), 'antidiag': lambda r, c: (n - 1 - c, n - 1 - r)}
    return [k for k, f in tr.items() if {f(r, c) for r, c in cells} == cells]
S = {(0, 0), (0, 1), (1, 1), (1, 2)}
def rot180(cells):
    return {(-r, -c) for r, c in cells}
check('X6.1', norm(rot180(S)) == norm(S), 'S-tetromino looks the same after a half turn')
check('X6.2', all(norm(f(S)) != norm(S) for f in (lambda s: {(r, -c) for r, c in s}, lambda s: {(-r, c) for r, c in s})), 'S tetromino has no vertical or horizontal line')
cs = {(0, 0), (0, 3), (1, 1), (1, 2), (2, 1), (2, 2), (3, 0), (3, 3)}
eq('X6.3', lines_of_symmetry(cs, 4), ['vertical', 'horizontal', 'diag', 'antidiag'])
c2 = {(0, 1), (1, 1), (1, 2), (2, 2)}
eq('X6.4', lines_of_symmetry({(0, 0), (0, 1), (1, 0)}, 3), ['diag'])

# ---------------- 3.7 Cube Stacks and Views
def views_ok(front, right):
    best = []
    for h in itertools.product(range(0, 4), repeat=9):
        g = [h[0:3], h[3:6], h[6:9]]
        if [max(g[r][c] for r in range(3)) for c in range(3)] == list(front) and [max(g[r]) for r in range(3)] == list(right):
            best.append(sum(h))
    return (min(best), max(best), len(best)) if best else None
res = views_ok((3, 1, 2), (2, 3, 1))
eq('X7.1', res[:2], (res[0], res[1]))
check('X7.2', views_ok((3, 1, 2), (2, 2, 1)) is None, 'front max 3 but side max 2: impossible')
eq('X7.3', sum([3, 1, 2, 0, 2, 1, 1, 1, 3]), 14)

# ---------------- 3.8 Time Travellers
def hm(s):
    h, m = map(int, s.split(':')); return h * 60 + m
def fmt(m): return f'{m // 60 % 24}:{m % 60:02d}'
eq('X8.1', (fmt(hm('9:40') + 155), fmt(hm('11:20') - hm('7:50') + 0), ), ('12:15', '3:30'))
eq('X8.2', (fmt(hm('12:10') - 115), hm('16:05') - hm('13:20'), hm('16:05') - hm('13:20') - 25), ('10:15', 165, 140))
A_ = [hm(x) for x in ('10:10', '11:00', '12:30', '14:00')]; dA = 40
B_ = [hm(x) for x in ('10:30', '11:45', '13:20', '14:30')]; dB = 55
def earliest(first_starts, d1, second_starts, d2, arrive):
    best = None
    for s1 in first_starts:
        if s1 >= arrive:
            e1 = s1 + d1
            for s2 in second_starts:
                if s2 >= e1:
                    e2 = s2 + d2
                    if best is None or e2 < best: best = e2
    return best
o1 = earliest(A_, dA, B_, dB, hm('10:00')); o2 = earliest(B_, dB, A_, dA, hm('10:00'))
eq('X8.3', (fmt(o1), fmt(o2), fmt(min(o1, o2))), (fmt(o1), fmt(o2), fmt(min(o1, o2))))
dep = hm('23:40') + 13 * 60 + 20
eq('X8.4', (fmt(dep), fmt(dep - 8 * 60)), ('13:00', '5:00'))
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
eq('X8.5', (1850 // 100 - 12, 1850 % 100), (6, 50))

# ---------------- 3.9 Shape Studio
l, w = [(l, w) for l in range(1, 20) for w in range(1, 20) if l + w == 21 and l - w == 5][0]
eq('X9.1', (l, w, l * w, 4 * l * w + 25, 21 * 21), (13, 8, 104, 441, 441))
eq('X9.2', [b for b in range(2, 30) if 2 * (11 - 1) + 2 * (b - 1) == 36], [9], '36 posts around a rectangle, 11 on a long side: 9 on a short side')
sol = [(a, b) for a in range(1, 30) for b in range(1, 30) if 2 * (4 * a + b) == 86 and 4 * (a + b) == 52]
eq('X9.3', sol, [(10, 3)])
check('X9.4', all(((a + b) ** 2) == 4 * a * b + (a - b) ** 2 for a in range(1, 30) for b in range(1, 30)), 'pinwheel square identity')

# ---------------- 3.10 Challenge Day 3 (Euler paths)
def euler_paths(edges):
    nodes = sorted({x for e in edges for x in e}); res = []
    def dfs(cur, used, path):
        if len(used) == len(edges): res.append(path[:]); return
        for i, (a, b) in enumerate(edges):
            if i in used: continue
            if cur == a: nxt = b
            elif cur == b: nxt = a
            else: continue
            used.add(i); path.append(nxt); dfs(nxt, used, path); path.pop(); used.discard(i)
    for n in nodes: dfs(n, set(), [n])
    return res
E1 = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('C', 'E'), ('D', 'E')]
deg = lambda E: {n: sum((n in e) * (1 + (e[0] == e[1])) for e in E) for n in sorted({x for e in E for x in e})}
paths = euler_paths(E1)
eq('X10.1', (deg(E1), len(paths) > 0, sorted({(p[0], p[-1]) for p in paths})), ({'A': 2, 'B': 3, 'C': 4, 'D': 3, 'E': 2}, True, [('B', 'D'), ('D', 'B')]))
Kon = [('A', 'N'), ('A', 'N'), ('A', 'C'), ('A', 'C'), ('A', 'I'), ('N', 'I'), ('C', 'I')]   # 4 landmasses, 7 bridges (Konigsberg-style, own labels)
eq('X10.2', (deg(Kon), euler_paths(Kon)), ({'A': 5, 'C': 3, 'I': 3, 'N': 3}, []), 'seven bridges, four odd places: no route crosses each once')
Kon2 = Kon + [('N', 'C')]
check('X10.3', len(euler_paths(Kon2)) > 0, 'one extra bridge between two odd places makes a route possible')


# Level 4 pre-flight verification, part 4 (Term 4) and totals
# ---------------- 4.1 Data Detectives: line graphs
temps = [21, 24, 26, 33, 31, 35]
rises = [temps[i + 1] - temps[i] for i in range(5)]
eq('Y1.1', (rises, rises.index(max(rises)) + 1), ([3, 2, 7, -2, 4], 3), 'largest rise between hour 3 and hour 4')
eq('Y1.2', (12 + (24 - 12) * (4 - 2) / (6 - 2),), (18.0,), 'steady trend: hour 2 = 12, hour 6 = 24: hour 4 = 18')
# ---------------- 4.2 Pie charts
tot = 240; eq('Y2.1', (tot // 3, tot // 4, tot * 5 // 12, tot // 3 + tot // 4 + tot * 5 // 12), (80, 60, 100, 240))
a, ab = F(3, 8), F(5, 8); b = ab - a; c = b; d = 1 - a - b - c
eq('Y2.2', (b, c, d, 30 / c, 30 / c * d), (F(1, 4), F(1, 4), F(1, 8), 120, 15))
eq('Y2.3', ((98 - 0) // 14 * 9 - (98 // 14 * 5), 98 // 14, 14 * 7), (28, 7, 98), 'bars 9 and 5 squares, red 28 more: 7 per square, 98 in all')
eq('Y2.4', [F(1, 3) * 360, F(1, 4) * 360, F(5, 12) * 360, F(1, 8) * 360], [120, 90, 150, 45])
# ---------------- 4.3 Patterns and rules
fig = lambda n: 3 * n + 1
eq('Y3.1', ([fig(n) for n in range(1, 5)], fig(25), [n for n in range(1, 100) if fig(n) == 100]), ([4, 7, 10, 13], 76, [33]))
g = lambda n: 3 + n * (n - 1) // 2
seq_ = [3]
for gap in range(1, 20): seq_.append(seq_[-1] + gap)
eq('Y3.2', (seq_[:5], seq_[7], seq_[19], g(20)), ([3, 4, 6, 9, 13], 31, 193, 193))
eq('Y3.3', (sum(range(1, 11)), sum(range(47, 60)), 13 * (47 + 59) // 2, sum(range(1, 101))), (55, 689, 689, 5050))
eq('Y3.4', (3 + 2 + 1 + 4, F(1, 4) + F(3, 4) + F(2, 5) + F(3, 5)), (10, 2), 'mixed numbers 3 1/4 + 2 2/5 + 1 3/4 + 4 3/5 = 12')
# rule from diagrams: top = 2a + b*b
data = [(3, 2, 10), (4, 1, 9), (5, 4, 26), (2, 3, 13)]
eq('Y3.5', all(2 * a + b * b == t for a, b, t in data), True)
fits = []
for c1, c2, c3, c4, c5 in itertools.product(range(-3, 4), repeat=5):
    if all(c1 * a + c2 * b + c3 * a * b + c4 * a * a + c5 * b * b == t for a, b, t in data):
        fits.append((c1, c2, c3, c4, c5, c1 * 6 + c2 * 5 + c3 * 30 + c4 * 36 + c5 * 25))
inter = []
for i in range(1, 13): inter.append(3 * ((i + 1) // 2) if i % 2 else 50 - 4 * (i // 2 - 1))
eq('Y3.6', (inter[:6], inter[9]), ([3, 50, 6, 46, 9, 42], 34))
# ---------------- 4.4 Solve a Smaller Problem
hs = lambda n: n * (n - 1) // 2
eq('Y4.1', ([hs(n) for n in (3, 4, 5, 6)], hs(30)), ([3, 6, 10, 15], 435))
eq('Y4.2', ((509 - 1) // 2, (509 - 1) // 2 + 1), (254, 255))
eq('Y4.3', (80 // 4, 2 * (24 + 16) // 4), (20, 20))
# ---------------- 4.5 Make a Systematic List
eq('Y5.1', (3 * 5 * 2, 3 * 5 * 2 - 1 * 1 * 2), (30, 28))
eq('Y5.2', [(a, b) for b in range(1, 6) for a in range(1, 13) if 20 * a + 50 * b == 240], [(7, 2), (2, 4)])
eq('Y5.3', [(a, 12 - a) for a in range(1, 10) if a < 12 - a and 12 - a <= 9], [(3, 9), (4, 8), (5, 7)])
eq('Y5.4b', [t for t in range(0, 22) if not (3 <= t <= 18)], [0, 1, 2, 19, 20, 21], 'three dice: totals 2 and 19 are impossible')
eq('Y5.5', sum(1 for a in range(1, 5) for b in range(1, 7) if a + b == 7), 4)
eq('Y5.6', [sum(1 for n in range(1, 11) if f(n)) for f in (lambda n: n % 2 == 0, lambda n: n % 4 == 0, lambda n: n < 4, lambda n: n != 10)], [5, 2, 3, 9])
eq('Y5.7', (4 * 3 * 2 * 3,), (72,))
# ---------------- 4.6 Working Backwards
eq('Y6.1', (30 - 8 + 15,), (37,))
eq('Y6.2', (27 / F(3, 5), 27 / F(3, 5) + 18), (45, 63))
eq('Y6.3', ((50 + 9, 50 - 9), 59 - 41), ((59, 41), 18))
rev = [n for n in range(1000, 10000) if int(str(n)[::-1]) == 4 * n]
eq('Y6.4', rev, [2178])
eq('Y6.5', [n for n in range(1000, 10000) if int(str(n)[::-1]) == 9 * n], [1089])
# ---------------- 4.7 Suppose and Compare
eq('Y7.1', [x for x in range(0, 16) if 80 * x + 30 * (15 - x) == 750], [6])
eq('Y7.2', [x for x in range(0, 19) if 9 * x + 5 * (18 - x) == 122], [8])
sol = [(x,) for x in range(0, 7) if 3 * (12 - 2 * x) + 5 * x + 8 * x == 64]
eq('Y7.3', sol, [(4,)])
eq('Y7.4', 3 * 2 * 3, 18)
eq('Y7.5', [r for r in range(1, 100) if 9 * r + 4 == 11 * r - 6], [5]); eq('Y7.5b', 9 * 5 + 4, 49)
eq('Y7.6', [(a, b) for a in range(0, 22) for b in range(0, 22) if a + b == 21 and 5 * a + 20 * b == 270], [(10, 11)])
D_ = lambda s: F(s)
sol = [(Dd, Dd + D_('4.8')) for Dd in [D_(x) / 10 for x in range(1, 200)] if Dd == 3 * (Dd + D_('4.8') - D_('6.4'))]
eq('Y7.7', sol, [(D_('2.4'), D_('7.2'))])
# ---------------- 4.8 Looking ahead to P5
eq('Y8.1', (F(3, 4), F(5, 8), F(2, 5), 4 * 3 * 2, [5 * 4 * 3, 6 * 3 * 3, 7 * 2 * 4]), (F(3, 4), F(5, 8), F(2, 5), 24, [60, 54, 56]))
# ---------------- 4.9 Count Place by Place
days_sep = [d for d in range(1, 31) if '2' in str(d)]
eq('Y9.1', len(days_sep), 12)
d27 = []
d0 = datetime.date(2027, 1, 1)
while d0.year == 2027:
    d27.append(d0); d0 += datetime.timedelta(days=1)
c5 = sum(1 for x in d27 if '5' in f'{x.day:02d}{x.month:02d}')
c0 = sum(1 for x in d27 if '1' not in f'{x.day:02d}{x.month:02d}')
# place by place for the digit 5: day has 5 or month has 5
days_with5 = {m: sum(1 for x in d27 if x.month == m and '5' in f'{x.day:02d}') for m in range(1, 13)}
eq('Y9.2', (sum(1 for x in d27 if x.month == 5), len(d27)), (31, 365))
eq('Y9.3', (c5, 31 + sum(days_with5[m] for m in range(1, 13) if m != 5)), (c5, c5))
eq('Y9.4', (math.factorial(5), math.factorial(6), math.factorial(10), len(str(math.factorial(10))), len(str(math.factorial(10))) - len(str(math.factorial(10)).rstrip('0'))), (120, 720, 3628800, 7, 2))
eq('Y9.5', [n for n in range(1, 40) if math.factorial(n) % 10000 == 0][:1], [20], 'first factorial ending in four zeros is 20!')
# ---------------- 4.10 Year Quest items
eq('Y10.1', (F(3, 8) * 64, 2 * 14 + 5), (24, 33))

# part 5: Quest gate answers, effort and kit totals
# Term 1 Quest
girls, glasses, girls_gl, total = 17, 12, 5, 30
boys = total - girls
eq('Q1.1', (boys, glasses - girls_gl, boys - (glasses - girls_gl)), (13, 7, 6))
# Term 2 Quest
eq('Q2.1', (36 * 25, ['R', 'B', 'B', 'G', 'Y'][(23 - 1) % 5]), (900, 'B'))
eq('Q2.2', ((189 - 45) // 2, (189 - 45) // 2 + 45), (72, 117))
eq('Q2.3', (F(3, 4) - F(1, 6), 36 / F(3, 5), F(17, 4), F(19, 8) + F(15, 8)), (F(7, 12), 60, F(17, 4), F(17, 4)))
eq('Q2.4', (20 - D_('13.65'), D_('2.10') / 3, D_('3.25') / 5, 4 * D_('1.35'), D_(9) / 4), (D_('6.35'), D_('0.70'), D_('0.65'), D_('5.40'), D_('2.25')))
eq('Q2.5', (180 - 60, 120 - 30), (120, 90))
eq('Q2.6', len(lsolve('AB+CA=ADD')), 1)
# Term 3 Quest
eq('Q3.1', (solids['triangular prism'],), ((5, 9, 6),))
eq('Q3.2', (names[turn(90, [-135])], 96 // 12, 2 * (12 + 8)), ('NW', 8, 40))
eq('Q3.3', (sum([2, 1, 0, 3, 2, 1, 1, 1, 0]), fmt(hm('14:50') + 105), 1920 // 100 - 12), (11, '16:35', 7))
eq('Q3.4', [b for b in range(2, 30) if 2 * (8 - 1) + 2 * (b - 1) == 24], [6])
# Term 4 Year Quest
eq('Q4.1', (30 * 4, 5 * 10 + 2, hs(6), 3 * 4, [x for x in range(0, 11) if 6 * x + 4 * (10 - x) == 52], [r * 2 for r in [12] if r - 3 == 9]), (120, 52, 15, 12, [6], [24]))
eq('Q4.2', (len([n for n in range(1, 41) if '3' in str(n)]), rnd(47658, 1000), F(3, 4) + F(1, 6), 2 * (12 + 7)), (13, 48000, F(11, 12), 38))
eq('Q4.3', [n for n in range(450, 550) if n % 12 == 0][:1], [456], 'smallest multiple of 12 that rounds to 500')
# extra checks for Term 2 text
eq('W4.7', F(3, 4) - F(1, 6), F(7, 12))
eq('W5.5', (72 - 72 // 4, (72 - 72 // 4) - (72 - 72 // 4) // 3), (54, 36))
eq('W5.6', (48 - 48 // 3 - 8,), (24,))
eq('W6.5', (F(5) + F(11, 4) - F(3, 2), F(25, 4)), (F(25, 4), F(25, 4)))
eq('W6.6', [k for k in range(8 * 2 + 4, 8 * 4) if F(19, 8) < F(k, 8) < F(13, 4)], [20, 21, 22, 23, 24, 25], 'mixed numbers with denominator 8 between 2 3/8 and 3 1/4: 2 4/8 ... 3 1/8')
eq('W10.4', ((59 - 13) // 2, (59 - 13) // 2 + 13), (23, 36))
eq('W10.5', [(e, 5 * e) for e in range(1, 100) if 5 * e - 24 == e + 24], [(12, 60)])
eq('W10.6', [x / 100 for x in range(100, 200) if rnd(x, 10) == 160 and sum(map(int, f'{x:03d}')) == 11], [1.55, 1.64])
eq('W3.8', ((52 - 28) // 2, 52 - (52 - 28) // 2, 35 // 5), (12, 40, 7))
eq('W2.8', (days[(days.index('Mon') + 21) % 7], days[(days.index('Fri') + 10) % 7], 100 % 7), ('Mon', 'Mon', 2))
eq('W9.6', (round(5 / 3, 2), round(5.02 / 3, 2), rnd(1125, 100) / 1000), (1.67, 1.67, 1.1))
# extra checks for Term 3 text
eq('X1.6', (2 * (4 * 2 + 4 * 1 + 2 * 1), 2 * (5 * 3 + 5 * 2 + 3 * 2)), (28, 62))
eq('X2.9', (turn(90, [135, -225]), names[turn(90, [135, -225])]), (0, 'N'), 'Kai faces E, turns 135 cw, then 225 acw to face N')
eq('X2.10', (48 // 4 * 3, 48 // 4), (36, 12))
eq('X3.6', [w for w in range(1, 40) if w * (w + 4) == 117], [9]); eq('X3.7', (2 * (9 + 13),), (44,))
eq('X3.8', [(w, 2 * w) for w in range(1, 40) if 2 * (w + 2 * w) == 54], [(9, 18)])
eq('X4.7', ((12 + 2) * (8 + 2) - 12 * 8, (18 + 6) * (10 + 6) - 18 * 10), (44, 204))
eq('X5.5', (6 * 3 + 1 * 3 + 1 * 3, 6 * 4, 8 * 3), (24, 24, 24), 'two cuts, three pieces: 8 by 3 rebuilt as 6 by 4')
eq('X8.6', (fmt(hm('8:45') + 8 * 60 + 30 - 0), (17 * 60 + 15 - (8 * 60 + 45)) / 60 * 11, fmt(hm('0:15') + 24 * 60 - 170)), ('17:15', 93.5, '21:25'))
eq('X10.4', (len(E1), sum(deg(E1).values())), (7, 14))
# extra checks for Term 4 text
eq('X9.5', (32 // 8,), (4,), '3 identical squares in a row, perimeter 32: side 4')
eq('Y5.8', sorted((a, b) for b in range(0, 7) for a in range(0, 7) if 10 * a + 20 * b == 60), [(0, 3), (2, 2), (4, 1), (6, 0)], 'ways to pay 60 cents with 10 and 20 cent coins')
# balance chain: plum 1, mango 3 plums, papaya = mango + 2 plums, melon = papaya + mango
pl = 1; ma = 3 * pl; pa = ma + 2 * pl; me = pa + ma
eq('Y7.8', (sorted([('plum', pl), ('mango', ma), ('papaya', pa), ('melon', me)], key=lambda t: -t[1]), me), ([('melon', 8), ('papaya', 5), ('mango', 3), ('plum', 1)], 8))
tank = 300
eq('Y6.6', (tank - tank // 5, (tank - tank // 5) // 2, (tank - tank // 5) // 2 - 30), (240, 120, 90), 'tank: 1/5 Monday, 1/2 of the rest Tuesday, 30 l Wednesday, 90 l left')
eq('Y6.7', [t for t in range(1, 1000) if t - t // 5 - (t - t // 5) // 2 - 30 == 90 and t % 10 == 0], [300])
c3 = sum(1 for x in d27 if '3' in f'{x.day:02d}{x.month:02d}')
nd3 = sum(1 for x in d27 if '3' in f'{x.day:02d}')
import calendar
eq('Y9.6', (c3, 31 + sum(sum(1 for d in range(1, calendar.monthrange(2027, mth)[1] + 1) if '3' in f'{d:02d}') for mth in range(1, 13) if mth != 3)), (80, 80), 'dates in 2027 (dd/mm) containing a 3: all of March plus the days 3, 13, 23, 30 and 31 of the other months')
eq('Y9.7', [100 * 4 + 10 * t + o for t in range(10) for o in range(10) if t == 2 * o and 4 + t + o == 13], [463], 'hundreds 4, tens double the ones, digits add to 13: 463')

tot = len(RESULTS); fails = [r for r in RESULTS if not r[1]]
print('TOTAL checks:', tot, 'failed:', len(fails))
for r in fails: print('FAILED', r)
```

