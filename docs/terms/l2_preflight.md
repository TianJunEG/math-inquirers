# Level 2 pre-flight (lessons 1 to 40, four terms, ages 7 to 9, Primary 2)

Status: planning only, written 23 Oct 2026. No lesson, tool, template or output file was edited or built. This document tells the people who will write Level 2 what each of the 40 lessons is, what the shared templates must learn first, which holiday items must not be repeated, what went wrong in Level 1 Terms 1 and 2, which decisions the owner must make, and in which order to build. It is modelled on `docs/terms/l1_term2_preflight.md` and `docs/terms/l1_term3_term4_preflight.md`.

Sources read: `docs/terms/owner_decisions.md` (all entries), `docs/terms/level_2_year_plan.md` (all four terms, the revision blocks, the "Non-routine assignments" section, the type-by-lesson matrix and the paper notes), `docs/books/p2_school_paper_patterns.md` (wording, ranges, pictures, marks, fit/gap table), `docs/books/p2_non_routine_catalogue.md` (types, original examples with scripted answers), `docs/moe/syllabus_by_level.md` (P2 pp. 33 to 34, P1 pp. 31 to 32, P3 pp. 35 to 36, P4 and P6 flags), `docs/sasmo/g2_analysis.md` (catalogue, verdicts, mapping), the holiday program of the same level (`p2/SPEC.md`, `p2/content/l1.js` to `l10.js`: every Start here, Think harder and Go further question of the ten holiday lessons was extracted and read), `docs/terms/l1_term2_preflight.md`, `docs/terms/l1_term3_term4_preflight.md`, `term/l1/AUTHORING.md` (all passes, Terms 3 and 4 section), `term/l1/WORDING_GUIDE.md`, `term/l1/audit/TERM_WIDE_AUDIT.md`, `CUTOUT_AUDIT.md`, `FINAL_AUDIT_T1.md`, `FINAL_AUDIT_T2.md`, the Level 1 tools (`term/l1/tools/figs2.py`, `figs3.py`, `svg.py`, `validate.py`, `common.py`, `b_*.py`) and `print/make_term_books.py`. Not re-read in full: the word-problem book analysis (`docs/books/word_problems_g1_g2_analysis.md`), cited through the plan.

Numbers marked "verified" were recomputed by brute-force scripts during this pre-flight (a scratch script, not committed). The lesson authors must still write their own `verify/lNN_checks.py`; nothing here replaces it.

## 0. Headline findings

1. **The holiday course already teaches most of what the Level 2 plan calls "new", and the plan's contest items collide with it.** I extracted all 237 holiday question-bank items (60 core, 87 stretch and 90 challenge, which the holiday workbook shows as Start here, Think harder and Go further). The plan says the term lessons do not repeat the holiday course (owner decision of 22 Oct); at the level of the topic that is mostly true, but at the level of the question it is not. Examples: Lesson 1 Think harder (digits add to 5, the digit 3 from 300 to 399) is the same pair of items as holiday Lesson 1's challenge section; Lesson 7 Go further (squares and triangles in a grid) repeats holiday Lesson 8's counting items; Lesson 15 (find the start from the end and the length) repeats holiday Lesson 9; Lesson 18 Think harder (a 4 by 4 grid) is a holiday Lesson 10 challenge item; Lesson 23 (exchange chains) is a holiday Lesson 9 stretch item; Lessons 6 and 22 (like fractions that make 1) are holiday Lesson 7 challenge items. A holiday graduate who starts Term 1 (owner decision 4) would meet these twice. Section 13 is a register of every overlap, with a rule for each lesson ("second visit allowed with new numbers and one new twist", or "must change the item"). This is the largest content risk and was not visible in the plan.
2. **Level 2 needs a fraction renderer and a decimal-money renderer that Level 1 deliberately never built.** Level 1 deliberately avoided `1/2` and `$1.50` (decisions D16 and D2 of the Terms 3 and 4 pre-flight: both are P2 content). Nothing in `term/l1/tools` renders stacked fractions in text, in answer boxes, in the runner or in the PDF text checks; the holiday decks have their own `rich()` helper that the term tools do not share. Fractions (Lessons 6, 22, 33), money in decimal notation (Lesson 5 and every money story) and time to the minute (Lesson 15) are core Level 2 Start here content. This blocks 9 lessons (section 3, M2, M3, M14).
3. **The Level 1 tools are hard-wired to Level 1 in several places** (`term/l1/` paths, "Level 1" in the guide footer in `b_guide.py`, practice keys `t1l01` that would collide with Level 2 Term 1 Lesson 1, `AUDIT_L01.md` paths, the leak check keyed on Level 1 titles). A Level 2 lesson built today would carry the wrong level footer and share a practice key with Level 1. One parametrisation task (M1) comes before any lesson.
4. **Seven new figure families are needed beyond what the Level 1 engine has** (base-ten and place-value pictures, vertical column sums with missing digits, fraction shapes and a 0-to-1 line, balance and kitchen-scale and jug pictures, solids and cube nets, spinners and tally tables, matchstick digits and magic rings). Everything else (clock to the minute, money, calendar, grid, cube stack, picture graph, bar model, table, panel, network, stick pattern, picture equation, ten-frame, hundred chart) exists in `figs2.py` and `figs3.py` and is reused. Section 3 checks each against the tools.
5. **Black-and-white print is now a design constraint for Level 2 from the first figure.** Fractions, picture graphs, balance objects, coins, tile patterns, mirror pictures and bar models are all colour-coded in the colour PDFs; the printed books are 1-bit. Every Level 2 figure must be specified with a hatch pattern, label or shape per category, and each lesson's "shade" instruction must say "shade or hatch" (children use pencils). Section 3.1 (M18).
6. **Five lessons have no school-paper evidence at all** (30 Robot Recipes, 31 Chance and Fair Games, 36 Grid Treasure Hunt, 38 Problem Posers, 39 Look Again) and two more are "Above" (32 Tables Bridge, 34 Big Numbers Expedition). They are the right lessons to make up first in an exam period (the plan already says so) and the right place to trial wording.
7. **The plan treats some school work as a preview.** Time to the minute, durations, start-from-end (Lesson 15) and money in decimal notation with conversions (Lesson 5) are school work by 2022 to 2025 papers, but decimal addition is P3 on the syllabus (p. 35). The pre-flight keeps both truths: conversions and cents arithmetic at Start here and Think harder, decimal addition only at Go further (decision D2).
8. **Estimate:** about 330 agent-hours for the 40 lessons including wording review, independent audit, fix pass, four term-wide audits and a consistency sweep, plus about 125 hours of template engineering (about 109 if optional items are deferred). Level 1 Terms 3 and 4 were estimated at 172 + 112 to 135 for 20 lessons; Level 2 is about twice that scale plus a Level 2 parametrisation. With the Level 1 process (8 to 10 writing agents, 3 engineers) that is about 8 to 10 working days from the start of Sprint A to four audited terms (section 11).

## 0.1 Assumptions made (change them if wrong)

- Files: `term/l2/lessons/l01.json` to `l40.json` (global numbers 1 to 40, the plan's numbering); `term` 1 to 4; `lesson_in_term` 1 to 10; `id` `l2-t1-01` to `l2-t4-40`; practice keys `l2t1l01` to `l2t4l40` (the Level prefix is new, to avoid a clash with Level 1 keys). Family pages print "Level 2 • Term 3 • Lesson 4", never "Lesson 24 of 10". Taglines: Term 1 "Notice it", Term 2 "Test it", Term 3 "Explain why", Term 4 "Create and connect" (the plan's year arc). "Lesson 1" is only allowed where `lesson_in_term` is 1; the next lesson of Lesson 10 is "the first lesson of Term 2", and so on.
- Same 11-part 90-minute timing as Level 1 (owner decision of 23 Oct, supersedes 75), Mi the dolphin (no calculator image), private-paper safeguarding without any paper held to the camera, the standard recording sentence, the "I am still stuck" mark on the look-back that the parent photographs to the business WhatsApp, tier labels Start here / Think harder / Go further / Investigation only, 6-minute Remember with three items, a spare-time menu, and no "MOE-aligned", "SASMO" or "GEP" on any child or parent page.
- Tier counts as built in Level 1: Start here 5 to 7 (default 6), Think harder 3 to 5 (default 4), Go further exactly 3, Investigation on page 5 with an easy first step. The named beyond item takes one of those slots; it is not an extra question. Contest-style items are at Think harder or Go further only, never Start here (owner decisions 6 and the beyond-syllabus rule of 23 Oct).
- Lessons 10, 20, 30 and 40 host Mi's Challenge Quest: 20 minutes at minutes 35 to 55 straight after the brain break, 8 gates and one optional cave, no score, rank, visible timer or the words test or exam on any child or parent page. Timing of those four lessons: Opening 2, Remember 6, Sneak-peek 4, Explore 10, Mini-lesson 9, Break 4, Quest 20, Workbook 25, Talk 4, Look-back 2, Flex 4 = 90 (as built in Level 1 Lessons 20 and 30).
- Books (owner decision of 22 Oct): printed black-and-white workbooks come with payment as 5-lesson books: Book 1 = lessons 1 to 5, Book 2 = 6 to 10 (holds the Term 1 Quest Log), Book 3 = 11 to 15, Book 4 = 16 to 20 (Quest Log), Book 5 = 21 to 25, Book 6 = 26 to 30 (Quest Log), Book 7 = 31 to 35, Book 8 = 36 to 40 (Quest Log). Colour soft copies of the same files stay in colour.
- Names: Ali, Mei, Siti, Ben, Kumar, Aisha, Wei, Ravi, Jenny, Lily, Jamie, Ray, Amelia, Jason (WORDING_GUIDE rule 21; the P2 papers add Sam, Jane, Raj). Wrong working is attributed to "a child" or "a child in another class", never to a cast name (Level 1 audit; Level 1 pre-flight D18).
- Multiplication reading order follows the Level 1 default ("3 groups of 4" is 3 x 4, either order accepted, frames use groups x each). Division uses the sign from Lesson 3 (P2 syllabus, p. 33).
- Money is written with both notations from Lesson 5: $3.05 and 305¢ (P2 syllabus; the P2 papers write both). The cent sign ¢ is used, never "c". There is no $20 note. Notes in play money: $2, $5, $10, $50, $100.
- Fractions are written stacked in all print and slides (three eighths over a bar), never as a slash in child text. Denominators to 12 (syllabus p. 33), like fractions only; the words remainder, equivalent, decimal point and letters for unknowns stay out of child pages (the plan, audit M1, M4, M5).
- Holiday graduates start Term 1 (December), Term 3 (June) or Term 2 (March) (owner decision 4). Holiday topics return in Remember warm-ups only (owner decision of 22 Oct, "Term 1 is written as new lessons"). The pre-flight adds a stricter rule: no holiday question is reused in a term lesson at all (section 13).

## 0.2 What exists to be reused (checked in the working tree on 23 Oct)

`term/l1/tools/` already renders, for any level, once parametrised: `clock` (any minute, digital readout, mirror, sector), `money` (play coins 5¢ to $1 and notes $2 to $100, totals), `price_tag`, `calendar`, `stick_pattern` (triangles, squares), `shapes2d` (circle, half and quarter circle, fold lines; parts 1, 2 or 4 only), `grid` (dots or squares, polygon, route, counts, mirror), `cube_stack` (iso, top, views; base to 3 by 3, heights to 3), `fold_punch`, `panel` (shape tiles with colour, pattern, size and turn), `network`, `picture_graph` (any `each`, tally, key), `number_line` (labels, prefix, suffix, jumps, hide), `hundred` (0 to 99, shade, arrows), `seq`, `ruler` (true scale), `table` (text, boxes, circles, tick boxes, icons), `objects` (55 icons), `groups`, `array`, `bar_model` (compare, part-whole, units, transfer, brace, gap), `picture_equation` (six symbols), `line_up`, `round_table`, two-colour `ten_frame`, `domino`. Kits: `base_ten` (tens bars and ones squares only), `hundred`, `number_strip`, `cards`, `shapes`, `groups_mat`, `unit_strips`, `array_mat`, `people`, `clock_kit`, `play_money`, `price_tags`, `grid_tiles`, `mistake_cards`, `fold_shapes`, `shape_pieces`, `pair_cards`, `grid_mat`, `graph_mat`, `tool_cards`, `event_cards`, `stick_strips`, `calendar_cards`. Question forms: `visuals`, `tf`, `mcq`, `steps`, `draw`, `choices`, tokens `___`, `[]`, `[2]`, `[3]`, `()`, `[ ]`, `{eq}`. Runner v2: `fig`, `fields`, `ordered`, templated choice, `multiples`, `common`, `divisors`, formatters `{n|ord}`, `{n|word}`, `{n|usd}`, `{n|c}`, `{n|hour}`, `{n|min}`, `pad`. Quest builder `b_quest.py` (gates may name `lesson` as a number, a list or "beyond"; `scope: "year"`). Lesson fields `beyond`, `materials.kit_contract` (validator fails if supplied is less than max used), `home_practice[].rewind_of`. `print/make_term_books.py` already accepts `--level 2 --size 4 --per-term 10` (use `--size 5`).

Level 1 term lessons 1 to 30 exist; `l31.json` onward are not written (Level 1 Term 4 is in progress by other agents and is not touched).

---

## 1. Lesson specs

### 1.0 Field order and conventions

Every spec uses this order: big idea, strand and page refs, objective, Remember warm-up (three items, each re-taught with objects or a picture so a cold joiner can follow), Start here / Think harder / Go further outline with question counts, the **Beyond (named)** item (a puzzle title the child sees, never labelled "challenge" or "stretch"), **Holiday overlap** (what the holiday course already did and what the term lesson must not repeat), number ranges, home materials, kit with piece counts (the kit contract: supplied against the most any one task may use), figures, misconceptions, template needs (codes from section 3), and whether the lesson is safe to miss.

**Non-routine work (owner decision of 23 Oct).** Each spec carries the `NR:` line from the plan's "Non-routine assignments" section (type code, tier T or G, never Start here) plus the changes this pre-flight makes. Type codes: LOG logical reasoning, CMP comparison, BACK work backwards, CTX unfamiliar context or hidden fact, LIST systematic list, EXP explain or true-false, GC guess and check, PAT pattern, DIAG draw a model, MULTI multi-step, TAB table, EQ make equal, WAYS how many ways, CHAL build from clues. Hints naming the tool ("Hint: Make a table.") may appear in Think harder stems, never in Go further (paper pattern, `p2_school_paper_patterns.md` section 7).

**Wording.** Use `WORDING_GUIDE.md` rules 1 to 25 plus the P2 paper patterns: story first, picture between, the question last; "Choose the correct answer and write its number in the brackets" with options (1) to (4); "Show all your workings clearly" at the end of a multi-step stem; part (b) built on (a); "am" and "pm" without full stops, times as 9:30; "more than", "fewer than", "heavier than", "greater", "smaller" (never "bigger" for numbers); "n groups of m". Rule 25 changes at P2: three-digit numbers, two steps and a model are ordinary Start here; three steps, rounding words and "explain why" prompts stay in Think harder and Go further.

**Mid-year entry.** Every Remember re-teaches from nothing the one earlier idea the lesson leans on and uses no word that only an earlier lesson defined. A holiday graduate is a likely entrant at Terms 1, 2 or 3 and has met bars, money in cents, fractions to twelfths, time to 5 minutes, picture graphs with a key and cube stacks; a school-only child has not. Warm-ups therefore use the holiday topic names in the guide ("you may know this from the holiday course") but never depend on them.

---

## Term 1: Notice it (lessons 1 to 10)

Cold joining: yes. Safest to skip: Lesson 10 (a new context of ideas taught elsewhere; nothing later needs it), then Lesson 7. Hardest to miss: Lessons 1, 3 and 5.

### Lesson 1. Where Does It Live? (T1.1)

- **Big idea.** A number has a place on a line, and its digits tell you where.
- **Strand.** MOE P2 Whole Numbers 1.1 to 1.4 (count in tens and hundreds, place value to hundreds, words, compare and order, p. 33). Contest tag (tutor only): number sense, riddles with digits (SASMO number sense, 10 of 110 problems).
- **Objective.** Place a 3-digit number on a line marked in 100s or 10s; read and write numbers to 999 in words; compare and order. Think harder: an unmarked line and its midpoint; a number riddle; every number from three cards. Go further: halfway numbers; a number built from regrouped parts.
- **Remember (6 min).** (1) Count on in tens and hundreds from a 3-digit number along a strip (holiday Lesson 1 chart, re-taught). (2) Build a number from hundreds, tens and ones cards. (3) Which is greater, 273 or 237? Compare the hundreds first. New numbers only: the holiday examples 538, 914, 409 and 490 are not reused.
- **Start here (6).** Put 270 on a line from 200 to 300 marked in tens; read the number an arrow points to; write 407 and 560 in words (one written, one multiple choice); write "six hundred and five" in digits (the zero holds the tens place); "Arrange the numbers. Begin with the smallest." (three numbers, 100 apart in the hundreds only); name the number between two marked numbers. Words are accepted with or without "and" and with or without a hyphen.
- **Think harder (4).** **NR (plan):** LOG (find the number from clues), LIST (every number from three cards), with the plan's digit-sum idea replaced (see overlap). (i) An unmarked line with 300 and 500 marked: halfway is 400, then place 450. (ii) "I am a number from 300 to 399. My tens digit is twice my ones digit and my ones digit is not 0. I am odd. My digits add up to 12." Answer 363; the first two clues alone leave 321, 342, 363 and 384; odd leaves 321 and 363; the digit sum leaves 363 only (verified). (iii) "Use the cards 0, 2 and 5 once each. List every 3-digit number you can make (0 cannot be first)": 205, 250, 502, 520; which are greater than 300: 502 and 520 (verified; the holiday sets were 4, 4, 7 and 0, 3, 8). (iv) A line marked every 50 from 0 to 1000: place 650 and read the number an arrow points to (a scale of 50, new to the child).
- **Go further (3).** G1 **Beyond (named): "Halfway Numbers".** The halfway number of 240 and 480 is 360; of 130 and 570 it is 350 (verified); find the halfway number of two numbers whose sum is odd and say why it is not a whole number (e.g. 250 and 455: the halfway point sits exactly between 352 and 353 on the line; no decimal is written). Level note: the midpoint is not a P2 outcome (averages start at P4 and midpoint as halving is a P3 mental-calculation habit); say "halfway" never "average". G2 CTX: 4 hundreds, 13 tens and 25 ones make 555 (verified; the holiday item was tens alone). G3 Make up a three-clue riddle for 363 so that no other number fits.
- **Holiday overlap: HIGH.** Holiday Lesson 1 already did digit cards (3, 6, 1; 2, 6, 9; 4, 4, 7; 5, 1, 9; 2, 5, 9), digit sums 4, 5 and 6, the digit 3 from 300 to 399 (120), pages 1 to 120 (252), 46 ten-blocks, and 700 to 790. Do not reuse any of these. The plan's Think harder (digit sum 5 and the digit 3) is replaced here; if the owner wants one digit-sum item it must use a new setting, for example "digits all different and no zero, sum 9" (decision D1).
- **Numbers.** 100 to 1000; words to 999.
- **Home materials.** A paper strip for the line, pencil, ten small objects.
- **Kit (KA place-value arrow cards).** Supplied 27 cards (hundreds 100 to 900, tens 10 to 90, ones 1 to 9, one each). Max used by any task 9 (three 3-digit numbers built at once in Explore). Cut 27. Keep for Lessons 2, 13 and 34 (34 adds the thousands cards).
- **Figures.** `number_line` (exists), `place_value` (M4), `table` and `mcq` for words.
- **Misconceptions.** 407 read as 4007 or written 47; "between" includes the ends; the last digit decides which number is greater; "halfway" found by halving each digit; spelling.
- **Needs.** M4, M13, M14 (words as a choice item), KA.
- **Safe to miss?** No: Lessons 2, 13 and 34 lean on place value; the warm-ups of those lessons repeat the build.

### Lesson 2. Mind Maths Moves (T1.2)

- **Big idea.** Split a number to make a friendly sum.
- **Strand.** MOE P2 Addition and Subtraction 2.1 to 2.2, mental calculation with a 3-digit number and ones, tens or hundreds (p. 33). Beyond MOE (enrichment): pairing sums and letter sums. Contest tags: number sense and clever computing (10 problems, pairing sums a real gap), letter-digit sums (3 problems, Section B, always the last questions).
- **Objective.** Add and take away tens and hundreds mentally, count up to find a difference, bridge 100 by splitting, pair numbers to make tens; Think harder: a shape-code sum with no carry; Go further: pairing sums and a letter sum with a carry.
- **Remember (6 min).** (1) Make 100 from a 2-digit number (holiday Lesson 2 spiral, new numbers). (2) Add 30 and 200 to a 3-digit number on a line. (3) Count up from 478 to 503 in three hops (2, then 20, then 3) to find the gap, 25 (verified).
- **Start here (6).** 346 + 200; 508 - 30; 700 - 400 as "7 hundreds take away 4 hundreds"; count up to find 503 - 478; "Fill in the missing number: 375 + [ ] = 400"; one story with a tens jump.
- **Think harder (4).** **NR (plan):** BACK (undo two jumps to find the start, then check forwards), EQ (a missing number that makes two sums equal without adding). (i) Bridge 100: 68 + 47 is 68 + 32 + 15 = 115; and BACK: "I think of a number, add 38, then take away 15, and get 99" is 76 (verified: 76 + 38 - 15 = 99), checked forwards. (ii) Pair a short list to make tens: 17 + 3 + 14 + 6 + 9 + 1. (iii) A shape-code sum with no carry (pattern in section 3, M10): one clue given so the answer is unique. (iv) EQ in subtraction form: 746 - 298 = 748 - [ ] gives 300 (verified: both equal 448); the holiday item was the addition form 400 + 250 = 300 + [ ].
- **Go further (3).** G1 **Beyond (named): "Pairs Add Up".** 3 + 6 + 9 + ... + 30 has 10 terms, which make 5 pairs that each total 33 (3 + 30, 6 + 27, ...), so the sum is 165 (verified); 1 + 2 + ... + 20 is 10 pairs of 21, which is 210 (verified); 5 + 10 + 15 + ... + 50 is 5 pairs of 55, which is 275 (verified). Level note: arithmetic series are not in primary syllabus; the move is pairing, which is the P2 make-ten idea in a long list. G2 LIST: choose two numbers from a list that make 1000 (answer unique in the list the author writes; EX-LIST-2 gives the pattern). G3 a letter sum with a carry, ones column first: "AA + BB = CAC" has exactly one answer, A = 2, B = 9, C = 1 (22 + 99 = 121, verified). A second form, "AB + AC = BCA", also has exactly one answer (91 + 98 = 189, verified).
- **Holiday overlap: MEDIUM.** Holiday Lesson 2 did missing digits in column sums, compensation (299 + 101 = 300 + 100), magic squares and triangles, and the digit-card largest and smallest difference (531 and 47). The term plan correctly leaves magic squares and smallest difference to Lesson 20. Avoid 299 + 101 and 346 + 199; the subtraction-form EQ item is new.
- **Numbers.** Sums to 1000; the pairing lists to 50; letter sums are two-digit with at most one carry.
- **Home materials.** Paper, pencil; a deck-of-cards style 1 to 10 set is optional.
- **Kit.** None new; reuse KA (max used 6 cards).
- **Figures.** `number_line` with jumps, `table`, `column_sum` (M5) for the shape-code and letter sums.
- **Misconceptions.** Pairing the wrong ends; forgetting to keep the carry; different letters taking the same digit; counting hops instead of summing them.
- **Needs.** M5, M10, M14 (equation frames), `()` circle sign token (exists).
- **Safe to miss?** Yes for the pairing item (Lesson 20 revisits letter sums and pairs).

### Lesson 3. Share It or Group It? (T1.3)

- **Big idea.** Division is sharing or grouping, and the sharer counts.
- **Strand.** MOE P2 Multiplication and Division 3.1 to 3.4: tables 2, 3, 4, 5, 10, the sign ÷, related facts (p. 33). "Left over" never "remainder" (P3, p. 35). Contest tags: multiples and remainders (7 problems, well prepared), bar-model leftovers.
- **Objective.** Share a set equally and group a set; write the sentence with ÷; read "shares with her 3 cousins" as 4 people; decide what a left-over means. Think harder: true or false statements; leftovers in a real setting. Go further: a story with groups, a take-away and a share.
- **Remember (6 min).** (1) Skip count in 3s, 4s and 5s on a line (holiday Lesson 3/4 spiral). (2) Deal 12 counters onto 3 plates. (3) Draw 4 groups of 5.
- **Start here (6).** Share 12 counters among 3; make groups of 4 from 20 and write the sentence; "Write a division equation for the picture" (circled groups); write two multiplication and two division sentences for an array (4 rows of 5; do not use the holiday's 2 rows of 10); one picture with the sharer counted ("Mei shares 8 stickers with 1 friend": 2 people), required at Start here by the papers (14 papers use it); one fill-in "n groups of m".
- **Think harder (4).** **NR (plan):** CTX (the sharer counts), EXP (true or false). (i) "Mei shares 24 stickers equally with her 3 cousins. How many stickers does each person get?" 6 (4 people; verified). (ii) True or false: (a) 6 groups of 4 is the same as 4 groups of 6 (true); (b) 20 sweets can be shared equally among 6 friends with none left (false, 2 are left over); (c) 20 sweets packed 5 to a bag fill 4 bags with none left (true). (iii) 20 cookies, 3 each: the most number of friends she can give to is 6 with 2 left over (paper wording "the most number of friends"). (iv) Buses or tables for N children with M seats: "one more is needed". Context is not boats or buses (the holiday item was 27 children and boats of 4).
- **Go further (3).** G1 **Beyond (named): "Always One Left".** The smallest number over 1 that leaves 1 when put in groups of 3, of 4 and of 5 is 61 (verified). Level note: remainders and common multiples are P3 and P4; the child checks by listing and the word remainder is not used. G2 MULTI (EX-MULTI-1 pattern): 7 bags of 6 sweets, 12 given away, the rest shared among 5 friends: 6 each (verified: 42, 30, 6). G3 find one first: "5 books cost $20; how much do 3 books cost?" ($12).
- **Holiday overlap: HIGH.** Holiday Lesson 3 did arrays with two multiplication and two division sentences, legs and wheels (all the "how many of each" puzzles), leftovers with boats and cupcake boxes, "numbers in two tables", and a 27-sweet leftover riddle (CRT). The term lesson is the division concept lesson; it must not reuse legs and wheels, boats, Mr Lim's sweets, or Ali's "every number from 4 to 30 makes an array".
- **Numbers.** Dividends to 50; divisors 2, 3, 4, 5, 10; left over at Think harder only.
- **Home materials.** 30 counters (buttons, beans or pasta, not sweets), five plates or cups.
- **Kit.** `groups_mat` (6 plates, not cut; exists). Contract: supplied 6 plates, max used 5. Cut 0.
- **Figures.** `groups`, `array`, `objects`, `tf` table (exist), `table`.
- **Misconceptions.** Forgetting the sharer; confusing the number of groups with the number in each group; sharing the left-over; ÷ as -; "none left" assumed.
- **Needs.** B1 slot widths (exist), `tf` and `mcq` (exist), R2 ordered fields (exist); ÷ glyph check on all PDFs.
- **Safe to miss?** No; Lessons 16, 17, 32 and 33 lean on it.

### Lesson 4. Chart Patterns (T1.4)

- **Big idea.** A chart shows the rule at a glance.
- **Strand.** MOE P2 Whole Numbers 1.5, counting patterns on a chart to 100, multiples of 2, 5, 10 (p. 33). Contest tags: repeating and moving patterns (4 problems), the grid format being the extension case.
- **Objective.** Shade the 2s, 5s and 10s on a hundred chart and say what you see; Think harder: a counter that moves round a 2 by 2 grid; numbers in two counting patterns; a two-step alternating rule; Go further: a 3 by 3 grid where each feature cycles.
- **Remember (6 min).** (1) Count in 2s, 5s and 10s on a hundred chart (holiday spiral). (2) Which number is below 34 on a chart with rows of 10? (3) A rule from a number string: 5, 10, 15, 20, next?
- **Start here (6).** Shade or hatch the 2s, 5s and 10s on a chart (two different hatch patterns, readable in black and white); say the last digits; fill a missing number in a counting pattern; "Which number does not belong?" (papers); the rule of 3, 7, 11, 15; will 60 be said when counting in 5s from 5.
- **Think harder (4).** **NR (plan):** PAT (a two-step alternating rule), LOG (odd numbers between two limits, count both ends). (i) A counter moves clockwise round the corners of a 2 by 2 grid, one corner per move: where is it after 30 moves? (30 = 7 laps and 2 left: the opposite corner; verified). (ii) Start at 100: add 100, take away 20, add 100, take away 20 ...; the 9th number is 420 (verified: 100, 200, 180, 280, 260, 360, 340, 440, 420). (iii) How many odd numbers are there from 302 to 312, counting both ends? 5 (verified). (iv) Numbers up to 100 that are in both the count by 5s and the count by 4s: 20, 40, 60, 80, 100 (verified; the holiday pairs were 4 and 10, 3 and 4, and the two frogs).
- **Go further (3).** G1 **Beyond (named): "Round and Round".** A counter reads the 9 squares of a 3 by 3 grid in order (left to right, then the next row) and goes back to the first square after the last; after 30 moves it is on square 4, the first square of the second row (30 is 3 laps of 9 and 3 more; verified). Moving-pattern grids are the SASMO "extension" case. G2 LIST: a 3 by 3 grid where each row cycles shape, size and pattern (attribute cycles); G3 write your own cycle with a question about the 40th place.
- **Holiday overlap: HIGH.** Holiday Lesson 4 did far places in repeating patterns (9th shape, 30th bead), growing sticks (5, 9, 13), frog jumps and shared counts of two patterns, tower cubes and the +5/+1 alternating pattern to 50. Do not reuse "houses of 5, 9, 13 sticks", the frog and tower items, "will 50 / 51 be said", or "3s and 4s both say 12".
- **Numbers.** Charts to 100; counts to 120 in Go further.
- **Home materials.** Two pencils or pens for two hatch patterns, 12 counters.
- **Kit.** `hundred` chart numbered (not cut; exists) plus the 2 by 2 and 3 by 3 move grids printed on the page. Contract: 1 chart, max used 1; counters from home, max used 12. Cut 0.
- **Figures.** `hundred` (shade, shade2), `grid` (route, marks), `panel` (attribute cycles), `seq`.
- **Misconceptions.** Starting the count at the starting square; skipping the last partial lap; a "diagonal rule"; shading by colour only (B&W print).
- **Needs.** M13 (chart offset such as 101 to 200 for Go further), hatch patterns (M18).
- **Safe to miss?** Yes (the plan's safest after Lesson 10).

### Lesson 5. Shop Bills and Change (T1.5)

- **Big idea.** A bill is a sum of dollars and cents, and change is counting up.
- **Strand.** MOE P2 Money: dollars and cents, decimal notation, compare two or three amounts, convert between decimal notation and cents only (p. 33). Adding and subtracting money in decimal notation is P3 (p. 35): see D2. Contest tag: money (2 problems).
- **Objective.** Read and write $3.05 and 305¢; convert both ways; total a bill by converting to cents; find change by counting up; compare three prices to the cent. Think harder: which two items make exactly an amount; paid and change given, find one price. Go further: a group price and a best buy.
- **Remember (6 min).** (1) Count a handful of coins and notes (holiday Lesson 6 spiral). (2) $1 is 100¢; write 35¢ as a part of a dollar. (3) Count up from 85¢ to $1.
- **Start here (6).** Convert $3.65 to 365¢ and 405¢ to $4.05; "Arrange the amounts from greatest to smallest" ($14.50, $14.05, $15.00 style); total two whole-dollar prices; read the money shown in a picture of coins and notes; "How much change did he receive?" (pay $10 for a $6 item); write the cent amount for a bill of three items by adding in cents (240¢ + 85¢ + 135¢ = 460¢ = $4.60, change from $10 is $5.40; verified).
- **Think harder (4).** **NR (plan):** BACK (paid, change given, find one price), GC (which two prices make exactly the amount). (i) 3 pens cost the same; she pays $20 and gets $5 change: one pen $5 (verified). (ii) Prices $2.30, $3.20, $1.75, $4.10 and $3.25: the only two that make $5.50 are $2.30 and $3.20 (verified). (iii) 7 coins make exactly 110¢ using 5¢, 10¢, 20¢ and 50¢ coins: there are exactly 5 ways (verified: 50+20+20+5+5+5+5; 50+20+10+10+10+5+5; 50 and six 10s; five 20s and two 5s; four 20s and three 10s), so ask for "one way" and put all five in the key. (iv) Compare three prices to the cent.
- **Go further (3).** G1 **Beyond (named): "Best Buy".** 3 for $12 or 5 for $18: to buy 15, the first costs $60 and the second $54 (verified), so 5 for $18 is the better buy. Level note: comparing unit rates is a P4 and P5 idea; say "cost of one" not "ratio". G2 CTX: 4 for $3, how many for $15 (20; EX-CTX-2 pattern, new numbers). G3 decimal sum written out: $2.40 + $1.35 + $0.85 = $4.60 with a place-value check (P3, Go further only).
- **Holiday overlap: HIGH.** Holiday Lesson 6 did 275¢ = $2.75, fewest coins/notes, change from $1, "enough money?", ways to pay $10 and 40¢ and 90¢, 7 amounts from coins, pen/pencil $11 and $3 more, and half-of-money backwards. The term lesson must not repeat fewest-coins, ways-to-pay or the pen/pencil item; its new angle is the receipt (bill), comparison to the cent and the two-notation habit.
- **Numbers.** Prices to $20 at Start here (cents to the 5¢); bills to $100 at Think harder.
- **Home materials.** A real or toy price list, coins in a purse (adult present).
- **Kit (KD play money).** Supplied: coins 5¢ x 4, 10¢ x 6, 20¢ x 4, 50¢ x 4, $1 x 4 (22); notes $2 x 3, $5 x 3, $10 x 3, $50 x 1 (10): 32 pieces. Max used by a task: 5¢ x 2, 10¢ x 4, 20¢ x 3, 50¢ x 2, $1 x 4, $2 x 3, $5 x 3, $10 x 3, $50 x 1. Cut 32. Stylised "PLAY MONEY", not facsimile (Level 1 D1; legal check still open). Keep for Lessons 28 and 40.
- **Figures.** `money`, `price_tag`, `table` (receipt), `number_line` with a $ prefix, `bar_model` for compare.
- **Misconceptions.** 305¢ written $3.5; $0.5 for 50¢; a bigger number of cents is greater money regardless of unit; adding dollars and cents as one number; change counted from the wrong amount.
- **Needs.** M14 (decimal formatter), `price_tag` decimal strings (exists as text), KD.
- **Safe to miss?** No (money returns in Lessons 27 and 28 and the Quest).

### Lesson 6. Cut It Equally (T1.6)

- **Big idea.** Equal parts, whatever the shape; a fraction counts the parts.
- **Strand.** MOE P2 Fractions 1.1 to 1.3 (part of a whole, notation, compare unit and like fractions with denominators up to 12, p. 33). Equivalent fractions are P3 (p. 35): bars and folding only. Contest tags: perception and counting parts.
- **Objective.** Tell equal from unequal parts, name halves, thirds, quarters, sixths, eighths; write the fraction shown; the same fraction in different shapes; shade or hatch parts; Think harder: how many more parts to shade; three like fractions that make 1 whole; Go further: equal parts of an L shape.
- **Remember (6 min).** (1) Fold a strip in half and in half again (holiday Lesson 7 spiral). (2) Count equal parts in a rectangle drawn in 8 parts. (3) 4 quarters make a whole.
- **Start here (6).** "Is it cut into equal parts? Circle Yes or No" (three pictures including a square cut in unequal strips); name the fraction shaded in a bar cut into 6, 8, 10 or 12 equal parts; shade or hatch 3 of 8 parts; "Which does not show one half shaded?" (papers); fold and shade a quarter of a square; a fraction fill-in "[n/d] of the pizza is left" (6 slices, 4 eaten).
- **Think harder (4).** **NR (plan):** LIST (three like fractions that make 1 whole), EXP (which picture is not a half or a third and why). (i) With denominator 8 and tops from 1 to 6, the sets of three different tops that sum to 8 are {1, 2, 5} and {1, 3, 4} (verified). (ii) 2 of 8 parts are shaded; how many more parts to shade so that 5/8 is shaded? 3. (iii) A quarter of a square shown as a rectangle and as a triangle (same area). (iv) Half is two quarters, shown by folding.
- **Go further (3).** G1 **Beyond (named): "Quarter the L".** The L-shaped garden made of three 2 by 2 blocks (12 squares) is cut along grid lines into 4 equal parts of the same size and shape: there is exactly one way using L-shaped parts (verified; 7 ways if the parts may be any connected 3 squares). Level note: dissecting a shape into congruent copies of itself (rep-tiles) is beyond the syllabus. G2 EQ: shade parts so that 7/12 is shaded when 4 are already; G3 "Make a whole strip from three different kinds of pieces" (plan).
- **Holiday overlap: HIGH.** Holiday Lesson 7 did fractions with bottoms to 12, comparing unit fractions, adding like fractions, bars of equal length, cutting 3 squares into 4 equal parts in different ways (the exact "different ways" item), two fractions with bottom 9 that make 1, three children sharing a cake of 10 with different pieces (tops 1,2,7; 1,3,6; 1,4,5; 2,3,5), halving a strip 3 times, and Siti's "bigger bottom number" claim. Avoid those; the term lesson is about equal parts in any shape and the notation, not fraction arithmetic. The three-fractions item uses denominator 8 (and Lesson 22 uses 12).
- **Numbers.** Denominators 2, 3, 4, 6, 8 at Start here; 5, 10, 12 at Think harder; 7, 9, 11 only in "make 1 whole" sets (papers).
- **Home materials.** Paper strips and squares (a grown-up cuts), a pencil for hatching.
- **Kit (KE fraction wall and folding strips).** A fraction wall (whole, halves, thirds, quarters, sixths, eighths, twelfths) printed on one page, not cut; 4 folding strips and 2 folding squares. Contract: supplied 4 strips, 2 squares; max used 4 strips, 2 squares. Cut 6. Keep for Lessons 22 and 33.
- **Figures.** `fraction` (M3): bar, rectangle, circle, grid, with hatching per category, unequal option, fold lines, shade count and "parts to shade" mode; the existing `shapes2d` supports only 1, 2 or 4 parts.
- **Misconceptions.** Any parts are halves; counting the unshaded parts; the bigger bottom number is the bigger fraction; shading by colour only.
- **Needs.** M2, M3, KE.
- **Safe to miss?** No (Lessons 22 and 33 lean on it).

### Lesson 7. Shape Splitters (T1.7)

- **Big idea.** Cut one shape into others, and join pieces to make new ones.
- **Strand.** MOE P1 and P2 shapes: form figures, identify shapes in a figure; P2 patterns with 2D shapes (p. 34). Counting figures and counting squares on a dot grid are Beyond MOE (SASMO counting figures, 7 problems, most "well prepared").
- **Objective.** Name the pieces when a rectangle is cut by one line; count sides and corners of pieces; rejoin pieces to make a new shape; Think harder: count the shapes of a figure into a table; Go further: tilted squares on a dot grid.
- **Remember (6 min).** (1) Name square, rectangle, triangle, semicircle, quarter circle. (2) Count the squares in a 2 by 2 grid by size (5; holiday spiral). (3) Fold a square along a diagonal and name the pieces.
- **Start here (6).** One line splits a 2 by 4 rectangle into two shapes and the child names them; sides and corners of the pieces; join two right triangles into a rectangle; copy a figure on a square grid; name the shapes that make a house; hatch all the triangles in it.
- **Think harder (4).** **NR (plan):** DIAG (draw the cuts and count the pieces), TAB (count each shape in a figure into a table). (i) A table of how many triangles, squares and rectangles in a figure made of 5 pieces. (ii) Count the squares of all sizes in a 3 by 3 grid: 9 + 4 + 1 = 14 (verified; the holiday grids were 2 by 2, 4 by 3 and 5 by 5, so 3 by 3 is new). (iii) Draw 2 lines to cut a square into 4 triangles.
- **Go further (3).** G1 **Beyond (named): "Tilted Squares".** On a 3 by 3 array of dots there are 6 squares (5 upright and 1 tilted); on a 4 by 4 array there are 20 (14 upright and 6 tilted); on a 5 by 5 array there are 50 (all verified by brute force). Level note: tilted squares are not a syllabus idea; children find them by looking for squares whose corners are all dots. G2 LIST: rectangles in a figure listed by size; G3 triangles in a figure with overlapping lines (new figure, not the holiday X or the 3-line triangle).
- **Holiday overlap: HIGH.** Holiday Lesson 8 did squares of all sizes in 2 by 2, 4 by 3 and 5 by 5 grids (5, 20, 55), rectangles in 2 by 2 and a row of 3 (9, 6), triangles in a square with both diagonals (8) and a triangle with 3 lines (20), cube stacks, nets, and painted cubes. This lesson is composing and decomposing, with counting as a second visit on new figures only.
- **Numbers.** Grids to 4 by 4; dot arrays to 5 by 5 at Go further.
- **Home materials.** Square-dotted paper (the page), scissors for a grown-up only.
- **Kit (KF dissection pieces).** 12 pieces on a 2 cm grid: 4 L-shaped trominoes, 4 dominoes (1 by 2) and 4 unit squares. Their total area is 24 squares and they tile a 4 by 6 rectangle (verified by exact-cover search), which is the Explore puzzle (rejoin them into two different rectangles). Contract: supplied 12, max used 12. Cut 12.
- **Figures.** `grid` (dots, squares, poly), `shapes2d` (compose), `table`.
- **Misconceptions.** A square is not a rectangle; counting only the small squares; missing tilted squares; counting a shape twice.
- **Needs.** KF; no new figure beyond `grid` with a tilted-square highlight option (small, M12).
- **Safe to miss?** Yes (second-safest in the term).

### Lesson 8. Read the Scale (T1.8)

- **Big idea.** Work out what one tick is worth before you read anything.
- **Strand.** MOE P2 Measurement: length in m, mass in kg and g, volume in litres, compare and order (p. 34); P1 cm (p. 32). The informal "1 m = 100 cm" is a Go further (formal unit conversion is upper primary, p. 41, to confirm with the owner). Contest tag: none (measurement reading).
- **Objective.** Read a ruler, a kitchen scale and a jug where every tick is labelled; find the value of one tick when only some are labelled; read a ruler that does not start at 0; Think harder: a balance with identical objects; compare in two matching units; Go further: cups, jugs and a tank.
- **Remember (6 min).** (1) Measure a pencil in cm on a ruler (P1 spiral). (2) Count in 50s and 100s along a strip. (3) 1 kg is 1000 g (informal).
- **Start here (6).** Read a ruler where the object starts at 3; read a kitchen scale 0 to 1000 g labelled every 100; read a jug in litres; compare two readings (heavier, lighter, as heavy as); "Draw a line 8 cm long"; one scale where every other tick is labelled.
- **Think harder (4).** **NR (plan):** DIAG (a balance: 3 melons weigh 12 kg, so 2 melons), CMP (how much heavier or more water, in two units that match). (i) Only the 0 and 100 g ticks are labelled on a scale with 4 ticks between: each tick is 20 g, so the pointer at the third tick is 60 g. (ii) 3 identical melons balance 12 kg: 2 melons weigh 8 kg (verified). (iii) 1 jug holds 3 cups; 4 jugs hold how many cups? (iv) Compare a mass in kg with one in g (convert one: informal).
- **Go further (3).** G1 DIAG: a tank, jugs and bottles. G2 **Beyond (named): "Between the Ticks".** A scale marked every 50 g from 0 to 1000 g; the pointer sits halfway between 650 and 700; the mass is 675 g, so estimate to the nearest 25 g (verified arithmetic). Level note: reading between ticks and estimating is a measurement habit, taught as estimating only. G3 a pool fills with 3 buckets, a bucket holds 4 jugs, a jug holds 5 litres: 60 litres (verified); the holiday tank was 4 jugs of 3 bottles of 2 litres.
- **Holiday overlap: MEDIUM.** Holiday Lesson 9 did balance puzzles with fruit, jug pouring (2 and 7 litres), ribbons and cuts, and time. Read-the-scale is not in the holiday course; the balance item must not use the melon/apple/pomelo set or the cube/ball scale.
- **Numbers.** Mass to 1 kg and to 10 kg; volume to 10 litres; ml appears once at Go further (papers from 2020).
- **Home materials.** A cm ruler (assumed; owner decision for Level 1 was no printed ruler, see D14), a kitchen scale and a jug if there is one, a cup.
- **Kit.** None (scales are printed). Cut 0.
- **Figures.** `ruler` (true scale), `scale_dial` (M7), `jug` (M7), `balance` (M6).
- **Misconceptions.** Reading the label as the tick; counting ticks instead of gaps; a ruler read from the end of the ruler, not from 0; forgetting the unit.
- **Needs.** M6, M7, B1 slots.
- **Safe to miss?** Yes (nothing later needs it; Lesson 24 re-teaches the scale).

### Lesson 9. Story Detectives (T1.9)

- **Big idea.** Read twice, then pick the first step.
- **Strand.** MOE P2 Addition and Subtraction and Multiplication and Division word problems (pp. 33 to 34), pictures and strips, one operation per step. Contest tags: bar-model word problems (7 problems, E and W verdicts) and the reading traps of the word-problem book.
- **Objective.** Say what is known and what is asked; solve a one-step story; solve a two-step story with a hidden first step; Think harder: the reversal trap ("58 more than Ali"), "at first / after"; Go further: a three-step story and a two-part question (a) and (b).
- **Remember (6 min).** (1) Draw a bar for one number (holiday Lesson 5 spiral). (2) Which operation does "fewer than" suggest, and does it ever mislead? (3) Add and take away with a 3-digit number.
- **Start here (6).** One-step story with a picture; "What do we know? What do we want to know?" (two blanks); two-step with a hidden first step ("2 boxes of 6 pens and 5 loose pens"); a story with money in dollars and cents; a bar to complete; "which equation matches the story" (papers: tick box).
- **Think harder (4).** **NR (plan):** CMP (the reversal trap), MULTI (two-step, hidden first step), BACK (at first, after selling: find the start). (i) "Ravi has 405 cards. He has 68 more than Sam. How many cards does Sam have?" 337 (verified). (ii) A two-step with a hidden first step. (iii) "At first ... after selling 123 ... 345 left": find the start (123 sold and 345 left: 468). (iv) Hint in the stem: "Draw a model."
- **Go further (3).** G1 **Beyond (named): "The Missing Middle".** Ben has 24 more stickers than Mei; Siti has 15 fewer than Ben; the three have 210 altogether; Mei has 59, Ben 83, Siti 68 (verified; the equation 3x + 33 = 210 has the unique answer 59). Level note: a three-quantity chain with a total is P3 and P4 bar-model work. G2 a three-step story. G3 a two-part question (a) and (b) where (b) uses (a).
- **Holiday overlap: HIGH.** Holiday Lesson 5 did "I think of a number", at-first stories (41 stickers, $15, 36 beads, $36), three children with extras (40 marbles: 9, 14, 17), and before-and-after bars; Lesson 2 did the egg-shop backwards story. The term lesson is about reading; its BACK items must use a different structure (a transfer plus a total, or a time) and must not use the "gave half, bought 12 more" frame.
- **Numbers.** Totals to 1000; money to the cent only in Start here item 4.
- **Home materials.** Paper strips for bars, counters.
- **Kit.** None. Cut 0.
- **Figures.** `bar_model` (compare, part-whole), `table`, `objects`.
- **Misconceptions.** Adding when the sentence says "more than" but the unknown is the smaller number; solving the first step and stopping; unit dropped.
- **Needs.** B4 steps lines (exists), `mcq` (exists).
- **Safe to miss?** No (Lessons 14, 27 and 28 lean on it).

### Lesson 10. Posts, Gaps and Queues (T1.10), with Mi's Challenge Quest

- **Big idea.** Count the gaps, not the posts; count yourself once.
- **Strand.** Beyond MOE (SASMO fence-post and cuts, 5 problems; the word-problem book traps G2-Q26, Q89, Q21). School evidence: some (4 tests: rods apart, queue, odd numbers between).
- **Objective.** Count posts and gaps along a line; find a queue position from the back; count the corners of a plot; Think harder: posts at equal gaps and queue positions; Go further: a circular track and a fence with a gate.
- **Remember (6 min).** (1) Jumps along a number line from 20 to 50 in tens: how many stops, how many jumps. (2) Count the gaps between the 5 fingers of one hand (4). (3) A queue: you are 3rd; say your place from the back if there are 8.
- **Start here (5, a shorter lesson body because of the Quest).** Jumps along a line (6 stops, 5 jumps); posts every 5 m along 20 m from 0 (5 posts, verified 20/5 + 1); a queue where Ali is 4th from the front of 15: 12th from the back (verified: 15 - 4 + 1); one picture of corners; "how many cuts make 4 pieces".
- **Think harder (3).** **NR (plan):** DIAG (posts every 3 m from 0 to 21), LOG (queue positions). (i) Posts every 4 m along 32 m from 0 m: 9 posts (verified). (ii) Third from the back in a queue of 11 is 9th from the front. (iii) Count yourself: "7 children between the first and the last" means 9 children.
- **Go further (3).** G1 **Beyond (named): "Circle of Posts".** On a circular track of 60 m with posts every 5 m there are 12 posts (verified; the gaps equal the posts on a circle, not one more). G2 CTX: a fence with a gate and posts both sides. G3 a ribbon with overlaps (second visit).
- **Holiday overlap: MEDIUM.** Holiday Lessons 9 and 10 did "rope cut into pieces (3 cuts)", "rope 30 m in 5 m pieces (6 pieces, 5 cuts)" and ribbons with overlaps. The term lesson's new ground is posts along a line, queue positions, corners and circles; cuts and pieces are a second visit with new lengths only.
- **Numbers.** Lengths to 100 m; queues to 20.
- **Home materials.** Ten counters or coins to act out posts and a strip of paper.
- **Kit.** None (line mat printed). Cut 0.
- **Figures.** `line_up` (exists), `number_line`, `grid` (corners), `objects`.
- **Misconceptions.** Posts = gaps; counting yourself twice; forgetting the post at 0; circles with one more post.
- **Needs.** none beyond the Quest (section 6).
- **Quest.** Gate mapping in section 6.
- **Safe to miss?** Yes (the plan's safest Term 1 lesson); but the Quest sits here, so the make-up route matters (section 6).

---

## Term 2: Test it (lessons 11 to 20)

Cold joining: yes. Safest to skip: Lesson 20 (a spiral with no new idea) then Lesson 19. Hardest to miss: Lessons 14 and 15.

### Lesson 11. Graphs That Talk (T2.1)

- **Big idea.** A graph answers some questions and not others.
- **Strand.** MOE P2 Statistics: picture graphs with scales (p. 34). Papers use keys of 2, 3, 4, 5 and 10, tally charts that feed a graph, and "twice as many" and "3 times as many". Contest tag: reading picture graphs and tables (3 problems).
- **Objective.** Read a 1-to-1 graph, then a graph with a key; turn a tally chart into a table and a graph; Think harder: true or false statements; build a graph from a tally; Go further: build from clues and a total; say what the graph cannot tell us.
- **Remember (6 min).** (1) Count in 2s, 5s and 10s along a row of icons (holiday Lesson 10 spiral). (2) Make a tally for 13. (3) Read a key: one icon stands for 2.
- **Start here (6).** Read a 1-to-1 graph (title, labels, key); read a graph with a key of 2 and a key of 5, whole pictures only (papers); "How many more children like ... than ...?"; tally to table; a total of a graph; "Each picture stands for 10".
- **Think harder (4).** **NR (plan):** EXP (true or false from a graph with a key of 4), TAB (tally to table to picture graph, key 4). (i) True or false from a key of 4. (ii) Complete the graph from a table. (iii) "Twice as many" read from a graph. (iv) Hint: "Make a table."
- **Go further (3).** G1 **Beyond (named): "Graph From Clues".** Four rows, a key of 4, 40 children in all: Football has twice as many pictures as Swimming, Tennis has 1 more picture than Swimming, Badminton has 1 picture; Football 4, Swimming 2, Tennis 3, Badminton 1 (verified unique). Level note: reading and building graphs from clues is the CHAL type; the 10-picture total comes from 40 / 4. G2 CHAL: complete from a total. G3 "What can this graph NOT tell us?" (plan).
- **Holiday overlap: MEDIUM.** Holiday Lesson 10 did keys of 2, 5 and 10, a missing row from a total of 30, and a lost key (football 6 and swimming 4 pictures, 10 more children: key 5, swimming 20). Do not reuse the lost-key item or the 30-children graph; keys 3 and 4 and tally are new.
- **Numbers.** Keys 2, 3, 4, 5, 10; totals 20 to 60; whole pictures at Start here, half pictures not used (papers).
- **Home materials.** A pencil, squared paper for a home survey (optional).
- **Kit.** `graph_mat` (5 columns by 8 rows, not cut; exists). Cut 0.
- **Figures.** `picture_graph` (rows, `each`, tally, key; exists), `table` with tally cells (M9 needs tally marks in cells).
- **Misconceptions.** Reading the picture count as the number; ignoring the key; double counting a row; comparing rows by length alone.
- **Needs.** M9 (tally cell), B&W icon distinctness.
- **Safe to miss?** No; the Quest reuses a graph gate.

### Lesson 12. Odd, Even, Fair (T2.2)

- **Big idea.** Even means pairs with none left over; test a claim on many examples.
- **Strand.** MOE P2 Whole Numbers 1.6, odd and even numbers (p. 33; the holiday course had none). Sharing between 2. Contest tag: parity.
- **Objective.** Sort numbers into odd and even by pairing; give a rule from the last digit; Think harder: odd + odd, even + odd by testing many examples; Go further: why the pattern is always so.
- **Remember (6 min).** (1) Deal counters onto two plates. (2) Count in 2s. (3) Read the ones digit of 347.
- **Start here (6).** Pair counters to decide odd or even for 1 to 20; hatch the 2s on a chart and say the last digits; odd or even for a number to 100 by the last digit; the number before and after; one picture with a left-over; a fair-share story with 2 people.
- **Think harder (4).** **NR (plan):** EQ (give some to make two shares equal), EXP (always, sometimes, never), LOG (riddle with odd, even and between). (i) Ali has 27 and Ben 13; Ali gives Ben 7 and both have 20 (verified). (ii) "Odd + odd is even": always, sometimes or never, with three tests. (iii) How many odd numbers from 201 to 213, counting both ends? 7 (verified). (iv) A riddle: odd, between 40 and 50, digits add to 9: 45.
- **Go further (3).** G1 **Beyond (named): "Odd Staircase".** 1 + 3 + 5 + 7 = 16 and 1 + 3 + 5 + 7 + 9 = 25: the sum of the first n odd numbers is n times n (verified for n = 4 and 5); explain with a staircase picture. Level note: square numbers are not in the syllabus; no formula is taught, the picture is. G2 EXP: why odd + odd is always even (two left-over singles pair up). G3 "odd x odd" test.
- **Holiday overlap: NONE** (odd and even is not in the holiday course).
- **Numbers.** Counters to 20; last-digit rule to 1000.
- **Home materials.** 20 counters, two plates.
- **Kit.** Number cards 1 to 20 (20 cards, cut 20) and a pairs mat (not cut). Contract: supplied 20, max used 20.
- **Figures.** `array` pairs layout with a left-over ring (exists), `hundred`, `table`.
- **Misconceptions.** One example proves a claim; reading the tens digit; "1 is even"; odd + odd = odd.
- **Needs.** none new.
- **Safe to miss?** No for the reasoning move; yes for the content (Lesson 29 revisits).

### Lesson 13. Jumps, Gaps and Columns (T2.3)

- **Big idea.** Subtraction is a gap; columns are place value in a tidy form.
- **Strand.** MOE P2 Addition and Subtraction 2.1 to 2.2, algorithms to 3 digits (p. 33); taught for understanding, not speed. Contest tag: number sense.
- **Objective.** Jump along a line to find a difference; add and subtract in columns with renaming and say why renaming works; Think harder: missing digit; choose jumps or columns; Go further: a wrong step.
- **Remember (6 min).** (1) Add 30 and 200 on a line. (2) Make a ten from 7 ones and 5 ones. (3) Build 253 from hundreds, tens and ones cards.
- **Start here (6).** Jump from 346 to 500; a column sum with a carry; a column difference with renaming; "which equation matches the story" (tick); find the missing digit in a one-box sum; check a subtraction by adding.
- **Think harder (4).** **NR (plan):** BACK (a missing digit in a column), CMP (the gap between two numbers by jumps). (i) 3[ ]8 + 144 = 482 gives 3 (verified: 482 - 144 = 338). (ii) Choose jumps or columns for 903 - 478 and say which was easier. (iii) The gap between two numbers on a line with two jumps. (iv) Hint: "Work backwards."
- **Go further (3).** G1 **Beyond (named): "The 495 Trick".** Take any 3-digit number whose digits are not all the same; arrange its digits to make the biggest and the smallest numbers, subtract; do it again with the answer. Every such number reaches 495 in at most 6 steps (verified for all 891 three-digit numbers whose digits are not all the same, writing a 0 in front when a difference has only two digits); 742 reaches 495 in one step (742 - 247). Level note: not a syllabus item; it gives column-subtraction practice with a purpose. G2 EXP: which step of a column sum is wrong and why. G3 a missing-digit puzzle with two boxes.
- **Holiday overlap: HIGH.** Holiday Lesson 2 did missing digits in 3-digit sums and differences, Mei's 523 - 267 mistake with the adding-back check, and "[ ] - 150 = 600". The term lesson is the understanding of columns and jumps, and the 495 trick; a plain missing-digit item is a second visit with new numbers.
- **Numbers.** 3-digit with 3-digit, renaming across tens and hundreds, answers under 1000.
- **Home materials.** Squared paper for columns.
- **Kit.** Reuse KA place-value cards (max used 9).
- **Figures.** `column_sum` (M5), `number_line` with jumps, `place_value` (M4).
- **Misconceptions.** Subtracting the smaller digit from the larger whatever the order; forgetting to rename; writing the carry in the wrong column.
- **Needs.** M4, M5.
- **Safe to miss?** No.

### Lesson 14. Bar Model Stories (T2.4)

- **Big idea.** One bar can hold the whole story.
- **Strand.** MOE P2 word problems (a Singapore school tool, not named in the syllabus); contest tag: bar-model word problems (7 problems, six in Section B).
- **Objective.** Draw a bar for part and whole and for a compare story; Think harder: one bar for a sum and a difference; a half-drawn model to complete; Go further: three bars in a chain; make equal by a transfer.
- **Remember (6 min).** (1) Draw two bars and the gap for "Ali has 8, Mei has 3" (teach from nothing). (2) 3-digit add and subtract. (3) Read "more than" and "fewer than".
- **Start here (6).** Draw the bar for one fact; fill in the blanks in a given model; find the total with part-whole; "how many more" with a compare model; pick the model that matches the story (papers: "Look at the model below"); complete and label a half-drawn model.
- **Think harder (4).** **NR (plan):** CMP (one bar for a sum and a difference), DIAG (complete and label a half-drawn model). (i) Total 200 and difference 36: 118 and 82 (verified). (ii) Two bars before and after a transfer. (iii) Fill in the blanks of a model. (iv) Hint: "Draw a model."
- **Go further (3).** G1 **Beyond (named): "Share the Gap".** Ali has 52 and Mei has 28; to make them equal Ali gives Mei 12, and both have 40 (verified); say why the gap of 24 is shared as 12. Level note: transfers with sum-and-difference are ordinary Book 2 school work (plan open question 7); here the named item is the picture of why half the gap moves. G2 CMP: three bars in a chain (more than, then fewer than; EX-CMP-2). G3 EQ: change a number and redraw.
- **Holiday overlap: HIGH.** Holiday Lessons 5 and 6 did bar models for before-and-after, three-children-with-extras, pen/pencil sum-and-difference ($11, $3 more) and three friends sharing a $15 present with $2 steps. This is not new ground in content; the term lesson is the bar as a general tool. Avoid $11/$3, the $15 present, the 40-marbles trio and the 42-stickers trio.
- **Numbers.** Totals to 1000; bars of at most 10 cells in drawings.
- **Home materials.** Paper strips, squared paper.
- **Kit (KG unit strips).** Supplied 8 strips of 10 cells (80 cells); max used by a build task 60 cells; larger bars are drawn, not built. Cut 8. Keep for Lesson 27.
- **Figures.** `bar_model` (compare, part-whole, units, transfer, brace; exists), draw-in empty bar with baseline.
- **Misconceptions.** Bars drawn the same length whatever the numbers; the bracket on the wrong bar; moving the whole gap in a transfer; adding when the sentence says "fewer".
- **Needs.** B4, B5 (exist).
- **Safe to miss?** No (Lessons 27 and 28 build on it).

### Lesson 15. Clock Detectives (T2.5)

- **Big idea.** A day is cut into hours and minutes, and a timeline shows the stages.
- **Strand.** MOE P2 Measurement: time to the minute, hours and minutes, convert hours and minutes to minutes and back (p. 34); durations of one hour or half hour are P1 (p. 32). The plan labels "find the start from the end" a P3 idea; the P2 papers test it from 2018 (nine papers) and durations to the minute from 2022 (decision D3). Seconds, finding a duration in general and the 24-hour clock are P3 (p. 36). Contest tag: calendar and time (5 problems).
- **Objective.** Read a clock to the minute; write the time with am or pm; convert 1 h 45 min to 105 min and back; draw a timeline; Think harder: find the start from the end and the length; durations to the minute; Go further: past midnight.
- **Remember (6 min).** (1) Read a clock to 5 minutes (holiday Lesson 9 spiral). (2) Count on in 5s round the face. (3) 60 minutes in an hour.
- **Start here (6).** Read a clock to the minute where every minute is ticked (e.g. 3:24, 12:10); write the time with am or pm; draw the minute hand for 9:25 (papers); 1 h 45 min is how many minutes (105); a film from 4:15 pm lasting 1 hour ends at 5:15 pm; a timeline with the hour marks to fill in.
- **Think harder (4).** **NR (plan):** BACK (find the start from the end and the time taken), CTX (hours and minutes to minutes and back; draw a timeline). (i) A film starts at 4:20 pm and lasts 1 h 45 min; it ends at 6:05 pm (verified). (ii) From 3:07 pm to 4:39 pm is 92 minutes, 1 h 32 min (verified). (iii) A film ended at 5:50 pm and lasted 2 h 25 min: the start is 3:25 pm (verified; EX-BACK-3 gives the pattern). (iv) 2 h 15 min is 135 minutes (verified). Hint: "Draw a timeline."
- **Go further (3).** G1 **Beyond (named): "Past Midnight".** A night bus leaves at 10:50 pm and arrives at 1:15 am the next day: the trip takes 2 h 25 min (verified). Level note: durations that cross midnight need the 24-hour clock idea (P3, p. 36); say "the next day". G2 CMP: minutes between two times to the minute. G3 a two-stage journey with a waiting time.
- **Holiday overlap: HIGH.** Holiday Lesson 9 did 5-minute reading, am/pm, durations across the hour, find-the-start (piano lesson 3:30, film 10:40), the 15-minute bus, 3 lessons of 35 minutes with breaks, a clock 10 minutes fast and a watch losing 5 minutes an hour (a rate: the plan keeps rates out of this level). The term lesson adds the minute, conversions and timelines; start-from-end is a second visit with new numbers and a timeline.
- **Numbers.** To the minute; durations to 6 h 15 min.
- **Home materials.** A real clock with minute ticks, a printed clock face.
- **Kit (KH clock kit).** 2 faces (13 cm across, all 60 ticks, 1 to 12), 3 hour hands and 3 minute hands (loose, no fastener). Contract: supplied 2 faces, 3 + 3 hands; max used 2 faces, 2 + 2 hands. Cut 6. Keep for Lessons 35 and 39 (mirror).
- **Figures.** `clock` (exists, all minutes), `number_line` with `labels` as the timeline (exists), `table`.
- **Misconceptions.** The hour hand read from the nearest number; 1 h 45 min written 145 min; counting the start as the first minute; am and pm flipped at noon; "past midnight" thought to end the day.
- **Needs.** M14 (time answer fields with pad: exist as R6), KH.
- **Safe to miss?** No.

### Lesson 16. Table Tricks (T2.6)

- **Big idea.** Tables connect: 4 is double 2.
- **Strand.** MOE P2 Multiplication and Division 3.2 to 3.5, tables 2, 3, 4, 5, 10, related facts, mental calculation within the tables (p. 33). Tables 6 to 9 are P3 (p. 35). The papers test only 2, 3, 4, 5 and 10, with statements "n groups of m", true or false, and "which does not describe the pictures".
- **Objective.** Build the 4s from the 2s, the 3s from facts, and fact families; Think harder: a ratio table and true or false statements; Go further: the 4s found without counting; the 8s by doubling.
- **Remember (6 min).** (1) Count in 2s, 5s and 10s. (2) 5 groups of 4 as 4 + 4 + 4 + 4 + 4. (3) Double 7.
- **Start here (6).** 5s and 10s from the 2s; "Write a multiplication equation for the picture"; "Which does not describe the pictures?" (tick); "7 sevens" and "10 fours"; a fact family from one picture; "Multiply 8 by 5".
- **Think harder (4).** **NR (plan):** TAB (a ratio table: 4 stickers for 3 stars), EXP (is 8 x 3 the same as 3 x 8; is it the same as 8 + 3). (i) 4 stickers for every 3 stars: 12 stars need 16 stickers (verified). (ii) 4 x 6 is double 2 x 6 = 24. (iii) true or false statements about 8 x 3. (iv) Hint: "Make a table."
- **Go further (3).** G1 **Beyond (named): "Double Double Double".** 7 x 8 is 7 doubled three times: 14, 28, 56 (verified; and 7 x 5 + 7 x 3 = 35 + 21 = 56). Level note: the 7 and 8 tables are P3; here only as doubling of a known number. G2 PAT: the 4s without counting. G3 a number in three tables.
- **Holiday overlap: MEDIUM.** Holiday Lessons 3 and 4 used tables 2, 3, 4, 5, 10 in arrays, legs, equal groups and patterns; "numbers in two tables" appears in both. Avoid the 5 and 2 table intersection (10, 20, 30, 40) as the headline item.
- **Numbers.** Tables 2, 3, 4, 5, 10 to 10 x; products to 100.
- **Home materials.** A multiplication grid (the page), 40 counters.
- **Kit.** `array_mat` (5 by 8 grid, not cut; exists). Cut 0.
- **Figures.** `array`, `table` (ratio and fact tables), `objects`, `tf`.
- **Misconceptions.** 8 x 3 read as 8 + 3; doubling the wrong factor; counting in 4s from a wrong start.
- **Needs.** none new.
- **Safe to miss?** No (Lessons 32 and 33 lean on it).

### Lesson 17. Find All the Ways (T2.7)

- **Big idea.** Organise so you miss none; use a table or a list in order.
- **Strand.** Beyond MOE (counting ways; SASMO counting ways, and worst case 2 problems, a real gap). Papers: some (outfits 3 x 4, coin combos, digit cards).
- **Objective.** List all outfits from two choices; use a table; Think harder: act out "how many must I take to be sure" with a counter bag; Go further: three colours and a larger case without listing.
- **Remember (6 min).** (1) List every pair from {A, B, C}. (2) Count the cells of a 3 by 4 table. (3) Skip count in 5s.
- **Start here (6).** List 6 outfits from 2 shirts and 3 shorts; a table of outfits; "how many ways to choose a drink and a snack"; list the coins that make 30¢ with 10¢ and 20¢ (new frame: order by 20¢ count); one picture list; check a list for a missing way.
- **Think harder (4).** **NR (plan):** WAYS (outfits and two-stage choices), LIST (pairs from a list with a given total). (i) 3 shirts and 4 shorts make 12 outfits (verified). (ii) Pairs from a list that add to 100. (iii) A bag with 2 red and 3 blue counters: how many must I take to be sure of 2 of the same colour? 3. (iv) Hint: "Make a table."
- **Go further (3).** G1 **Beyond (named): "Be Sure".** A bag holds 5 red, 4 blue and 3 green counters. To be sure of 3 of one colour you must take 7 (worst case 2 + 2 + 2 + 1; verified); to be sure of 2 of one colour from 3 colours: 4 (verified). Level note: the pigeonhole idea is contest-only. G2 WAYS: every way to pay exactly $17 with $2 and $5 notes: 2 ways (one $5 and six $2; three $5 and one $2; verified). G3 how many for a larger case without listing.
- **Holiday overlap: MEDIUM.** Holiday Lessons 1, 3, 6 listed digit-card numbers, hens and goats, and ways to pay ($10 with $5, $2, $1: 10 ways). Avoid those frames; outfits and worst case are new.
- **Numbers.** Up to 4 by 4 products; counts to 12.
- **Home materials.** 12 small items of three kinds in a bag (not food).
- **Kit.** Outfit picture cards: 3 shirts + 4 shorts (7 cards, cut 7). Max used 7.
- **Figures.** `table`, `objects`, `network` is not needed.
- **Misconceptions.** Listing the same way twice; assuming the worst case is the first draw; forgetting "to be sure".
- **Needs.** none new.
- **Safe to miss?** Yes.

### Lesson 18. Who Is Who? (T2.8)

- **Big idea.** Clues rule things out.
- **Strand.** Beyond MOE (logic grids; constraint grids are SASMO's last-question type). Papers: some (balance order, number riddle).
- **Objective.** Solve a 3 by 3 logic grid; Think harder: a 4 by 4 grid, order four boxes by weight, a small constraint grid; Go further: one clue is false; a hexagon grid of counts.
- **Remember (6 min).** (1) Order three heights from clues. (2) A tick table: Ali is not red. (3) Cross out what cannot be.
- **Start here (6).** A 3 by 3 grid (3 children, 3 pets); order three objects by weight from two clues; which clue gave you your first tick?; "who is the tallest" chain; one grid the child completes with one empty row; a check ("is this row possible?").
- **Think harder (4).** **NR (plan):** LOG (order four boxes by weight from three clues; EX-LOG-2). (i) A 4 by 4 grid (a new set of clues; the holiday one was transport to school). (ii) Four boxes P, Q, R, S from three clues. (iii) A constraint grid: eight digits 1 to 8 around a shaded square. (iv) Hint: "Cross out."
- **Go further (3).** G1 **Beyond (named): "The Number Ring".** Put 1 to 8 once each in the eight circles round a square so that every side of three circles adds to 12; with the corner at the top-left set to 1 and the circle next to it set to 5 there is exactly one ring (1, 5, 6, 4, 2, 7, 3, 8 going round; verified); without any clue there are 8 rings, which are the same ring turned and flipped (verified). Level note: constraint grids are the last-question type in SASMO 2017, 2018 and 2022. G2 LOG: one clue is false; which? G3 EXP: which clue was not needed?
- **Holiday overlap: HIGH.** Holiday Lesson 10 did the 3 by 3 and the 4-person grid with exactly one answer, the height chain, and the coin-order puzzle. The 4 by 4 grid is a second visit with a new set of clues; the number ring and the box-weight puzzle are new.
- **Numbers.** Grids to 4 by 4; digits 1 to 8.
- **Home materials.** Pencil, eraser; a printed grid.
- **Kit.** Number tiles 1 to 8 (cut 8) for the ring and weight cards P, Q, R, S (cut 4): cut 12. Keep tiles for Lesson 20.
- **Figures.** `table` (tick grid), `ring` (M10), `network` (optional).
- **Misconceptions.** Guess and rub out; a clue used twice; ticking when the clue says "not".
- **Needs.** M10.
- **Safe to miss?** Yes.

### Lesson 19. Track It (T2.9)

- **Big idea.** Follow what moves, not just what is.
- **Strand.** Beyond MOE (logic by tracking; SASMO logic 14-12, 16-18, 17-14, 20-14, four forms).
- **Objective.** Act out one transfer; follow three transfers in a row; seat children round a table from clues; a first "who can know" puzzle; Go further: card-flip rule checks.
- **Remember (6 min).** (1) Move 3 counters from a cup to another cup. (2) Seat four people round a table: the one opposite Ali. (3) A two-step story with a total.
- **Start here (6).** Act out one transfer with cups and counters; undo it; follow two transfers; a round table with two clues; "who has what" after one move.
- **Think harder (4).** **NR (plan):** EQ (three boxes made equal by moving marbles), BACK (undo a list of transfers), CTX (who ends with what; a hidden fact such as a dozen or a pair). (i) Three children end with 20 marbles each after: Ali gives Ben 5, Ben gives Mei 3, Mei gives Ali 2; at the start Ali had 23, Ben 18, Mei 19 (verified; total 60). (ii) A round table with six seats. (iv) A hidden fact: Siti buys 2 dozen eggs and 5 break; 19 are left (24 - 5). (iii) A first "who can know" puzzle with two children: three hats, 2 red and 1 blue, are shared by Ali and Mei, who each see the other's hat; Ali says "I do not know my colour"; then Mei knows her own hat is red (verified by enumeration: if Mei's hat were blue Ali would know his is red).
- **Go further (3).** G1 **Beyond (named): "I Know My Hat".** Four hats, 2 red and 2 blue, are shared by Ali, Ben and Mei standing in a line; Ali sees Ben and Mei, Ben sees Mei, Mei sees none. Ali says "I do not know my colour." Then Ben knows his: Ben's hat is the opposite of Mei's (verified: after Ali's statement Ben and Mei must have different colours). Level note: reasoning about what others know is a contest form. G2 card-flip rule check. G3 a four-person version.
- **Holiday overlap: LOW.** Holiday Lesson 5 had Ben and Ali "5 marbles" and three boxes "30 pens"; transfers were a backwards item. Avoid those numbers.
- **Numbers.** Totals to 100.
- **Home materials.** Three cups, 60 beans or buttons.
- **Kit.** Four hat cards R, R, B, B marked R and B in letters and a pattern (cut 4). Cut 4.
- **Figures.** `round_table`, `table`, `bar_model` (transfer).
- **Misconceptions.** Updating one child's count and not the other; doubling the transfer; mixing "I know" with "I guessed".
- **Needs.** none new.
- **Safe to miss?** Yes.

### Lesson 20. Puzzle Lab 2 (T2.10), with Mi's Challenge Quest

- **Big idea.** Return, mix and make your own.
- **Strand.** Spiral of Terms 1 and 2; letter sums (SASMO, 3 problems, Section B) and magic squares and triangles (holiday Lesson 2) return; pairing sums return. Beyond MOE.
- **Objective.** Choose a strategy and say why; a letter sum with one carry; make a puzzle with exactly one answer.
- **Remember (6 min).** Each problem in the lesson carries its own mini-reminder card (the plan); Remember uses a three-item mixed warm-up: a pairing sum, a transfer and a table.
- **Start here (5).** A mixed warm-up set (one item per Term 2 idea), each with a reminder card.
- **Think harder (3).** **NR (plan):** MULTI (a two-step mixed set). (i) Choose a toolkit move and say why. (ii) A letter sum with one carry, shapes first. (iii) A pairing sum.
- **Go further (3).** G1 **Beyond (named): "Puzzle Maker".** Write a puzzle with exactly one answer and prove it by listing; the author's check uses brute force, for example "two different numbers from 1 to 9 add to 13 and differ by 3": only 5 and 8 (verified). G2 GC (packs of 5 and 2 in equal numbers, 63 items; EX-GC-3 pattern). G3 magic triangle with side total chosen by the child.
- **Holiday overlap: HIGH.** The magic triangle and square and the smallest-difference digit-card item are holiday Lesson 2; "make up your own puzzle" is in every holiday challenge section. Keep as the plan says (a deliberate spiral), but with new numbers and the letter-sum and tracking items as the new part.
- **Numbers.** Mixed.
- **Home materials.** Pencil.
- **Kit.** Reuse the Lesson 18 tiles (max used 6). Cut 0.
- **Figures.** `column_sum` (letters), `table`, `ring` / magic triangle (M10).
- **Misconceptions.** Different letters sharing a digit; a leading zero; a puzzle with two answers called unique.
- **Needs.** M5, M10, Quest builder (section 6).
- **Quest.** Gate mapping in section 6.
- **Safe to miss?** Yes (the plan's safest); the Quest here means the make-up route matters.

---

## Term 3: Explain why (lessons 21 to 30)

Cold joining: yes (a June holiday graduate enters at Lesson 21). Safest to skip: Lesson 30 (stand-alone, Beyond MOE; but the Quest sits here), then Lesson 24. Hardest to miss: Lessons 27 and 28.

### Lesson 21. Gaps That Grow (T3.1)

- **Big idea.** The rule can itself have a rule.
- **Strand.** MOE P2 Whole Numbers 1.5 (patterns, p. 33); steps of +1, +2, +3 and "add the last two" (SASMO sequence move: 5 problems, all Section A, all gaps). Contest tags: changing-rule sequences (7 of 7 papers), growing patterns (3).
- **Objective.** Continue a sequence whose gaps grow or fall; Think harder: a falling-gap sequence and a first "add the last two"; Go further: the 20th term; the sum of the first ten terms.
- **Remember (6 min).** (1) Continue 2, 4, 6. (2) Count in 5s. (3) Add 1, 2, 3 in turn: 10, 11, 13, 16.
- **Start here (6).** Continue 2, 4, 6; find the rule of 5, 9, 13; continue 2, 3, 5, 8, 12 (gaps 1, 2, 3, 4; next is 17); shade a pattern on a chart; a growing picture of dots; the next picture.
- **Think harder (4).** **NR (plan):** PAT (growing sticks, from 31 sticks how many triangles), TAB (a table for a growing pattern). (i) 90, 89, 87, 84, 80: gaps grow as the numbers fall; next 75 (verified). (ii) A row of 8 squares uses 25 sticks, and 46 sticks make 15 squares (verified: 3n + 1). (iii) Add the last two: 1, 1, 2, 3, 5, 8: the 10th is 55 (verified). (iv) Hint: "Make a table."
- **Go further (3).** G1 **Beyond (named): "Triangle Numbers".** 1, 3, 6, 10, 15: the 20th is 210 (verified) and the sum of the first ten is 220 (verified). Level note: triangular numbers are not syllabus; no formula is taught, only the table and the staircase picture. G2 PAT: the 20th term of a changing-gap sequence (EX-PAT-3). G3 sums of the first ten terms.
- **Holiday overlap: MEDIUM.** Holiday Lesson 4 did sticks (5, 9, 13 for houses; 2, 5, 8 towers), "2, 7, 8, 13, 14 ...", "1, 4, 7, 10" frogs. Avoid those; falling gaps and add-the-last-two are new.
- **Numbers.** Terms to 300; the 20th term to 210.
- **Home materials.** 16 paper strips as sticks (never matchsticks or toothpicks).
- **Kit (KI stick strips).** Supplied 16 strips; max used 16 (5 squares in a row use 16). Cut 16. Keep for Lesson 39 (matchsticks).
- **Figures.** `stick_pattern` (triangles, squares; exists), `seq`, `table`.
- **Misconceptions.** Sticks counted twice at shared sides; "double and add 1" applied to the wrong pattern; testing a rule on one term.
- **Needs.** none new.
- **Safe to miss?** No (a sequence appears in the first seven questions of every contest paper).

### Lesson 22. Fractions on the Line (T3.2)

- **Big idea.** Fractions live between 0 and 1 and can be placed and compared.
- **Strand.** MOE P2 Fractions 1.2 to 1.3, 2.1 (notation, compare and order like and unit fractions, add and subtract like fractions within 1, p. 33). Comparing unlike fractions and equivalent fractions are P3 (p. 35). Papers: strong (about 12 papers on "more parts to shade").
- **Objective.** Place fractions on a line from 0 to 1; compare; add and subtract like fractions within one whole; Think harder: like fractions that add to 1; which fraction is wrong on the line; Go further: which is closer to a half.
- **Remember (6 min).** (1) Fold a strip into 4 equal parts. (2) Name a quarter. (3) Hatch 3 of 8.
- **Start here (6).** Mark thirds, quarters and sixths on a line from 0 to 1; read a fraction at a tick; compare two like fractions; 2/9 + 4/9; 1 - 3/8; arrange three fractions "Begin with the smallest".
- **Think harder (4).** **NR (plan):** LIST (like fractions that add to 1; list every set), EQ (how many more parts to shade), EXP (which fraction is wrong on the line and why). (i) With denominator 12, the sets of three different tops that sum to 12 are 7 (1,2,9; 1,3,8; 1,4,7; 1,5,6; 2,3,7; 2,4,6; 3,4,5; verified; Lesson 6 used denominator 8). (ii) Parts to shade. (iii) One fraction is mislabelled on the line; say which and why. (iv) Hint: "Make a list."
- **Go further (3).** G1 **Beyond (named): "Closer to Half".** Which of 3/8, 5/12, 4/10 and 2/6 is closest to a half? 3/8 is 1/8 away, 5/12 is 1/12 away, 4/10 is 1/10 away and 2/6 is 1/6 away, so 5/12 is closest (verified). Level note: comparing unlike fractions is P3; the child folds a strip and does not use a common denominator. G2 CMP: closer to half, two fractions. G3 a fraction wall puzzle.
- **Holiday overlap: HIGH.** Holiday Lesson 7 is a fractions lesson (see Lesson 6). The new element is the number line from 0 to 1, with fractions placed by folding.
- **Numbers.** Denominators 2 to 12; like fractions only.
- **Home materials.** Folding strips (the kit), pencil.
- **Kit.** 4 folding strips (cut 4; the Lesson 6 strips if kept) and a 0-to-1 line printed 20 cm (not cut). Contract: max used 4.
- **Figures.** `fraction` and `number_line` with fraction labels (M3).
- **Misconceptions.** The bigger bottom number is greater; counting ticks instead of gaps; placing 3/8 at 3 gaps of 10.
- **Needs.** M2, M3, KE.
- **Safe to miss?** No.

### Lesson 23. Shape Equations (T3.3)

- **Big idea.** Same shape, same value.
- **Strand.** Beyond MOE (SASMO picture and symbol equations: 7 problems, at least one every year 2015 to 2018). No letters for unknowns (P6, p. 43).
- **Objective.** Find a shape's value from one line; swap one shape for two; subtract one picture from another; Go further: three scales.
- **Remember (6 min).** (1) Fill the box: 6 + [ ] = 15. (2) Balance two sides with objects. (3) Same shape, same number (state the rule once).
- **Start here (6).** One shape and a number; two shapes of the same kind; a row of shapes totalling a number; a missing number on either side of an equation; the shape value written in the table; a picture of cups on a balance.
- **Think harder (4).** **NR (plan):** EQ (a missing number on either side), CTX (a symbol stands for one number in every line). (i) Two circles and a triangle total 17 and a circle and a triangle total 11, so a circle is 6 and a triangle 5 (verified). (ii) Swap one shape for two. (iii) Exchange chains: 1 jug is 2 pots, 1 pot is 3 cups. (iv) Hint: "Take one line from another."
- **Go further (3).** G1 **Beyond (named): "Three Scales".** Scale 1: two apples and a banana weigh 21; scale 2: an apple and two bananas weigh 18; scale 3: a banana and a cherry weigh 12; an apple is 8, a banana 5 and a cherry 7, the only whole-number answer (verified). Level note: simultaneous equations are beyond primary; shapes only, no letters. G2 a picture hidden in a total. G3 EQ chain.
- **Holiday overlap: HIGH.** Holiday Lesson 9 had balance puzzles including exchange chains (2 apples and 1 lemon balance 1 pomelo; a pomelo is 5 lemons) and "cube/ball" scales; Lesson 5 had machines. The exchange-chain item is the holiday item in a new coat: use pots and cups only as the plan says, and a different structure.
- **Numbers.** Values to 30.
- **Home materials.** Counters in two kinds, cups.
- **Kit.** `shapes` tokens (circle, square, triangle, star, heart; exists): supplied 15 (3 of each, three fill patterns), max used 9. Cut 15.
- **Figures.** `picture_equation` (six symbols, pattern per symbol; exists), `balance` (M6).
- **Misconceptions.** Different shapes must be different values; adding every shape in the picture; subtracting the wrong way.
- **Needs.** M6 (balance picture).
- **Safe to miss?** Yes.

### Lesson 24. Estimate Like a Scientist (T3.4)

- **Big idea.** A good guess is checked.
- **Strand.** MOE P2 Measurement (benchmarks 1 m, 1 kg, 1 l) and reasonable answers; papers: some (door 2 m, scissors).
- **Objective.** Guess then measure; use a benchmark; estimate a count; Go further: how many beans in a cup.
- **Remember (6 min).** (1) Read a ruler. (2) Hold a 1 kg bag (a litre of water). (3) Compare the lengths of two things.
- **Start here (6).** Guess then measure a pencil; "about how long is a door: 2 cm, 2 m or 2 km?"; a benchmark comparison; a litre bottle holds how many cups; choose a reasonable mass for a cat; a cups-to-litres step.
- **Think harder (4).** **NR (plan):** CTX (a benchmark as a hidden fact), MULTI (cups to bottles to litres). (i) Use a door of 2 m to estimate a wall. (ii) cups to bottles to litres. (iii) A reasonable range: is 3 kg too heavy for a school bag? (iv) Two estimates for the same jug: say which is more reasonable and why.
- **Go further (3).** G1 **Beyond (named): "How Many Beans?".** A cup of beans weighs 300 g and 10 beans weigh 5 g; about how many beans fill the cup? 600 (verified). Level note: scaling a sample is a P5 idea; the child writes the sample as a table. G2 CMP: a reasonable range. G3 estimate a count.
- **Holiday overlap: LOW.** Holiday Lesson 9 had measurement puzzles but no estimation; avoid the box-of-4-books and basket-of-apples frames.
- **Numbers.** Lengths to 10 m, mass to 10 kg, volume to 10 litres.
- **Home materials.** A cup, a bag of beans, a kitchen scale (optional), a 1 litre bottle.
- **Kit.** None. Cut 0.
- **Figures.** `scale_dial`, `jug` (M7), `table`.
- **Misconceptions.** Estimate treated as a wrong answer; unit slips; forgetting to check.
- **Needs.** M7.
- **Safe to miss?** Yes (the plan's second safest).

### Lesson 25. Spot the Solid (T3.5)

- **Big idea.** Every solid has a name and a view.
- **Strand.** MOE P2 Geometry: 3D shapes (cube, cuboid, cone, cylinder, sphere, p. 34). Beyond: views of cube stacks (SASMO 3D, 5 problems, room-corner stacks in 3 of 7 papers).
- **Objective.** Sort solids by flat and curved faces; name solids; top view of a stack; Think harder: cubes in a room-corner stack; Go further: build from two views.
- **Remember (6 min).** (1) Name a cube, a ball and a tin. (2) Count the faces of a box. (3) Count the cubes in a stack of 2 layers.
- **Start here (6).** Sort pictures of solids; "How many flat surfaces does it have?"; "I am a solid" with two clues; name the solid a tin of beans looks like; the top view of a stack; count the cubes in a stack.
- **Think harder (4).** **NR (plan):** LOG (I am a solid: clues about faces and rolling), TAB (a table of solids and their faces). (i) A table of faces. (ii) The top view of a stack with numbers. (iii) A room-corner stack: count the cubes seen from two walls and the floor. (iv) Which solids can roll, and why (a curved surface).
- **Go further (3).** G1 **Beyond (named): "Most and Fewest".** A stack on a 3 by 3 base has a front view of heights 3, 2, 1 and a side view of heights 3, 1, 2: at least 6 cubes and at most 14 (verified, 275 possible stacks). Level note: views are a P4 idea. G2 LIST: every solid that fits the clues. G3 build from two views.
- **Holiday overlap: HIGH.** Holiday Lesson 8 did cube stacks by layers (19, 16, 8, 20), the pyramid of 30, painted-cube sorting, nets and naming solids. Avoid the layered counts; the term lesson is names and views.
- **Numbers.** Bases to 3 by 3, heights to 3 (Go further to 4).
- **Home materials.** 14 same-size blocks or boxes (fallback: drawn stacks); a tin, a ball, a box.
- **Kit.** 10 solid picture cards (cut 10); max used 10.
- **Figures.** `solid` (M8), `cube_stack` (iso, top, views; heights to 4 needs M8).
- **Misconceptions.** Counting only visible cubes; a cylinder has 3 faces so it is not curved; a cube is not a cuboid.
- **Needs.** M8.
- **Safe to miss?** Yes.

### Lesson 26. Tiles, Turns and Symmetry (T3.6)

- **Big idea.** Patterns repeat by flipping and turning.
- **Strand.** MOE P2 Geometry 1.1 (patterns with 2D shapes by size, shape, colour, orientation, p. 34). Line symmetry is P4 (p. 39): a preview. Papers: some ("wrong shape", "12th position").
- **Objective.** Continue a tile pattern; say what changed; find the 23rd place in a repeat; Think harder: odd one out; Go further: a symmetric design.
- **Remember (6 min).** (1) Continue a pattern of 3 shapes. (2) Turn a shape a quarter turn. (3) Fold a paper heart.
- **Start here (6).** Continue a tile pattern; "One of the shapes is wrong. Circle it" (papers); name the change (size, shape, orientation); the 12th place in a repeating cycle of 4; colour or hatch by a rule; a turn.
- **Think harder (4).** **NR (plan):** PAT (a repeating cycle: which shape is the 23rd), EXP (odd one out and why). (i) The cycle circle, triangle, triangle repeated: the 23rd shape is a triangle (23 is 7 laps of 3 and 2 more). (ii) Odd one out. (iii) What changed from tile to tile. (iv) A pattern that turns a quarter each time: which turn is the next tile?
- **Go further (3).** G1 **Beyond (named): "Letters in the Mirror".** In a plain capital-letter font, 11 letters look the same with a mirror line down the middle (A H I M O T U V W X Y), 9 look the same with a mirror line across the middle (B C D E H I K O X), and 4 do both (H I O X) (the sets are a definition of the font; the author's verify file lists them). Level note: line symmetry is P4 (p. 39). G2 DIAG: draw the other half. G3 design a pattern with a symmetry.
- **Holiday overlap: NONE.**
- **Numbers.** Cycles of 3 to 5; places to 30.
- **Home materials.** Baking paper or tracing paper, a small mirror (optional).
- **Kit.** 12 pattern tiles (4 each of 3 shapes, cut 12). Contract: max used 12.
- **Figures.** `panel` (tiles with turn and pattern; exists), `grid` (mirror option), `shapes2d`.
- **Misconceptions.** A reflected shape drawn as a turned one; counting the repeat from 0; all letters are symmetric.
- **Needs.** M12 (pattern row with a "which is the nth" ring).
- **Safe to miss?** Yes.

### Lesson 27. Two-Step Bar Models (T3.7)

- **Big idea.** Two bars, one question.
- **Strand.** MOE P2 two-step word problems (pp. 33 to 34), money contexts; ages and "times as many" are Beyond or P3. Contest tags: bar models and ages (5 problems, 4 of them Section A early).
- **Objective.** Compare then total; age problems; Go further: transfers and "times as many".
- **Remember (6 min).** (1) Draw a bar for part and whole. (2) Add and subtract money. (3) "Twice as many".
- **Start here (6).** One more step after a model; compare then total; a money story with a bar; fill in the blanks of a two-step model; "who is correct?" (papers); a reversal repeat.
- **Think harder (4).** **NR (plan):** CMP (compare then total with a bar), MULTI (buy several, pay, find the change), DIAG (fill in a given model). (i) Compare then total. (ii) Buy several items and find the change. (iii) An age problem. (iv) Hint: "Draw a model."
- **Go further (3).** G1 **Beyond (named): "Always the Same Gap".** Dad is 30 years older than Mei; in 5 years their ages add to 56; Mei is 8 and Dad is 38 (verified). Level note: the gap between two ages never changes. G2 transfers. G3 "times as many" with a total.
- **Holiday overlap: HIGH** (see Lesson 14). Avoid all holiday bar items; ages are new.
- **Numbers.** Totals to 1000; ages to 50.
- **Home materials.** Paper strips.
- **Kit.** Reuse KG strips (max used 60 cells).
- **Figures.** `bar_model`, `table`.
- **Misconceptions.** Using today's ages in the future sum; a transfer applied to the wrong bar; "times as many" as plus.
- **Needs.** none new.
- **Safe to miss?** No.

### Lesson 28. Longer Chains (T3.8)

- **Big idea.** A long story is short steps.
- **Strand.** MOE P2 word problems; the word-problem book gaps 1, 2 and 4 (chains of 3 to 5 steps, "find one first", reading traps; about 60 of 101 Grade 2 problems need three or more operations). Papers: strong (3-link chains, unit price).
- **Objective.** Solve a three-link story with a bar and one operation per step; Think harder: four links, unit price, reading traps; Go further: five links and a two-part question.
- **Remember (6 min).** (1) One operation per step. (2) Bar for a total. (3) Price of one.
- **Start here (6).** A three-link story with a bar; steps lines "Step 1, Step 2, Step 3"; find one first with money; one picture; a table for the steps.
- **Think harder (4).** **NR (plan):** MULTI (four-step story), CTX (price of one first: 4 for $3). (i) 4 pens cost $20, so 3 pens cost $15. (ii) "with 2 friends" is 3 people. (iii) A discount on every item. (iv) A four-link story: 9 boxes of 4 pens is 36; 12 sold leaves 24; bags of 3 make 8 bags; at $2 a bag that is $16 (verified).
- **Go further (3).** G1 **Beyond (named): "Five Links".** A shop has 8 boxes of 6 pencils and sells 15 pencils; the rest are packed in bags of 3 and each bag costs $2: (a) how many bags (11), (b) how much money for all the bags ($22) (verified: 48, 33, 11, 22; five links and (b) uses (a)). Level note: five links and a two-part question are the Section C form of the papers. G2 BACK: Mei buys 3 books at the same price and a $5 pen, pays $50 and gets $12 change; one book costs $11 (verified). G3 CMP: three people in a chain then a total.
- **Holiday overlap: MEDIUM.** Holiday Lessons 3, 5 and 6 had the multi-step flavour; the term lesson is the discipline of steps.
- **Numbers.** Totals to 1000; products within the tables.
- **Home materials.** Pencil, price cards.
- **Kit.** Reuse KD play money.
- **Figures.** `bar_model`, `table`, `price_tag`.
- **Misconceptions.** Dropping a step; using the first answer as the final answer; the wrong unit.
- **Needs.** B4 steps.
- **Safe to miss?** No.

### Lesson 29. Always, Sometimes, Never (T3.9)

- **Big idea.** One counterexample beats a hundred examples.
- **Strand.** Reasoning claims across strands (odd and even, shapes, sums). Papers: some ("Who is correct?", true or false).
- **Objective.** Sort claims; find a counterexample; explain why a claim is always true.
- **Remember (6 min).** (1) Odd + odd. (2) A square is a rectangle. (3) A number that is in the 5s table.
- **Start here (6).** Sort six claims into always, sometimes, never using the "which is correct" format (papers); test with two examples; a counter that is a counterexample.
- **Think harder (4).** **NR (plan):** EXP (find the counterexample), LOG (number claims with two conditions). (i) "Every number in the 5s table ends in 5." Never always. (ii) "A rectangle has 4 equal sides." (iii) A claim with two conditions. (iv) "Which is correct?" with four statements about multiples of 4 (the papers' format).
- **Go further (3).** G1 **Beyond (named): "Product Parity".** The product of two odd numbers is always odd; the product of any number with an even number is always even (verified for all pairs up to 50); explain with a pairs picture. G2 EXP: why a claim is always true. G3 write a false claim and a counterexample.
- **Holiday overlap: LOW.** Holiday Lesson 1 had Mei's swap claim and Lesson 3 Ali's "every number makes an array".
- **Numbers.** Claims within 100.
- **Home materials.** Pencil.
- **Kit.** 12 claim cards (cut 12) and a three-pocket mat (not cut). Max used 12.
- **Figures.** `table`, `array`.
- **Misconceptions.** One example proves it; a counterexample of the wrong kind.
- **Needs.** none new.
- **Safe to miss?** Yes.

### Lesson 30. Robot Recipes (T3.10), with Mi's Challenge Quest

- **Big idea.** A recipe must be exact.
- **Strand.** Beyond MOE (algorithms, sequences and loops; Ontario and Australian curricula). No school-paper evidence.
- **Objective.** Write and follow 4 steps; use a loop; fix a buggy recipe.
- **Remember (6 min).** (1) Turn left, turn right. (2) Count steps on a grid. (3) Repeat a pattern 3 times.
- **Start here (5).** Follow a recipe on a grid; write 4 steps; a short loop; check the end square; fix one wrong step.
- **Think harder (3).** **NR (plan):** BACK (undo a robot recipe to find the start), PAT (a loop makes a repeating pattern). (i) Repeat 4 times: forward 3, turn right: the robot returns to the start (verified; forward 2 does too). (ii) Undo a recipe to find the start square. (iii) Write the shortest recipe, using a loop, that walks round a square 2 squares across.
- **Go further (3).** G1 **Beyond (named): "Shortest Recipe".** A staircase of three steps: forward 2, turn right, forward 1, turn left, repeated 3 times ends at 3 across and 6 up (verified); find the shortest recipe using a loop for any pattern. G2 LOG: what does the robot do first? G3 fix a buggy recipe.
- **Holiday overlap: NONE.**
- **Numbers.** Grids to 8 by 8.
- **Home materials.** A counter.
- **Kit.** 12 command cards (forward 1, 2, 3, turn left, turn right, repeat 2, repeat 3; cut 12) and a grid mat (not cut). Max used 12.
- **Figures.** `grid` (route), `table`.
- **Misconceptions.** Turning left and right swapped; a loop that includes the wrong steps; counting the starting square.
- **Needs.** Quest builder (section 6).
- **Quest.** Section 6.
- **Safe to miss?** Yes (the plan's safest of Term 3), but the Quest sits here.

---

## Term 4: Create and connect (lessons 31 to 40)

Cold joining: yes. Safest to skip: Lesson 40 (no new content; make it up recorded), then Lesson 38. Hardest to miss: Lessons 33 and 34.

### Lesson 31. Chance and Fair Games (T4.1)

- **Big idea.** Some things are likelier; test it.
- **Strand.** Beyond MOE (probability starts at Australian Year 3). Tally is school work (P2 Statistics); no school-paper evidence for chance. Owner decision 6: the words likely and unlikely are Think harder, never Start here.
- **Objective.** Tally 20 spins or tosses and say which came most; Think harder: sort events as likely, unlikely or certain; is the spinner fair?; Go further: design a fair game.
- **Remember (6 min).** (1) Tally 13. (2) Read a picture graph. (3) Equal parts of a spinner.
- **Start here (6).** Toss a coin 20 times and tally; which came most; a table of results; "What happened?" (a data task, not a probability task); read a tally; compare two tallies.
- **Think harder (4).** **NR (plan):** WAYS (list every outcome of two spins or coins), EXP (is the game fair, true or false). (i) Two coins have 4 outcomes (verified). (ii) Sort events. (iii) Is the spinner with 3 red and 1 blue fair? No. (iv) Hint: "Make a table."
- **Go further (3).** G1 **Beyond (named): "Which Total Wins?".** Two spinners each numbered 1 to 4: the total 5 comes up in 4 of the 16 equally likely pairs, more than any other total (totals 2 to 8 occur 1, 2, 3, 4, 3, 2, 1 times; verified); with two dice the total 7 occurs 6 times in 36 (verified). Level note: sample-space counting is beyond the primary syllabus. G2 TAB: tally 20 trials into a table. G3 design a fair game.
- **Holiday overlap: NONE.**
- **Numbers.** Up to 20 trials; 16 outcomes.
- **Home materials.** A coin, a paper clip, a pencil, spinners printed on the page.
- **Kit.** Three printed spinner discs (not cut); a paper clip and pencil (home). Cut 0.
- **Figures.** `spinner` (M9), `table` with tally cells, `picture_graph`.
- **Misconceptions.** "Due" results; confusing likely with certain; the spinner order matters.
- **Needs.** M9.
- **Safe to miss?** Yes.

### Lesson 32. Tables Bridge (T4.2)

- **Big idea.** Build new facts from known ones.
- **Strand.** Tables 6 to 9 are P3 (p. 35): a preview (Beyond MOE). Papers: none test tables 6 to 9; "n groups of m" statements are in the papers every year.
- **Objective.** Build the 6s from 5s and 1 more group; build 7 and 9; Go further: 7 and 9.
- **Remember (6 min).** (1) 5 x 4 and 2 x 4. (2) Double 3. (3) Skip count in 10s.
- **Start here (6).** A mix of 2, 3, 4, 5, 10; "Write a multiplication equation for the picture"; groups of 6 as 5 groups and 1 more.
- **Think harder (4).** **NR (plan):** TAB (build the 6s from the 5s), EXP (8 x 3 and 3 x 8, 6 x 4 and 4 x 6). (i) A table of the 6s built from the 5s and one more group each time (6, 12, 18, ... 60). (ii) True or false: 6 x 4 = 4 x 6 and 8 x 3 = 3 x 8 (both true). (iii) Numbers up to 50 in both the 4s and 6s tables: 12, 24, 36, 48 (verified). (iv) Hint: "Make a table."
- **Go further (3).** G1 **Beyond (named): "Nine Pattern".** The digits of 9, 18, 27, ..., 90 each add up to 9 (verified for 9 x 1 to 9 x 10), and 99 adds up to 18. Level note: the 9 table is P3. G2 GC (two packs in equal numbers; EX-GC-3). G3 7 x 8 as 35 + 21 = 56 (verified).
- **Holiday overlap: LOW.**
- **Numbers.** Products to 100.
- **Home materials.** 60 counters.
- **Kit.** Reuse the array mat (Lesson 16). Cut 0.
- **Figures.** `array`, `table`.
- **Misconceptions.** 6 x 4 as 6 + 4; a pattern assumed for 11.
- **Needs.** none new.
- **Safe to miss?** Yes.

### Lesson 33. Halves and Quarters of Things (T4.3)

- **Big idea.** Part of a whole, then part of an amount.
- **Strand.** MOE P2 Fractions 1.1, 2.1; fraction of a set is P4 (p. 37): Go further only. Papers: strong ("quarters in 3 wholes", pizza left).
- **Objective.** Fold and cut halves and quarters; fraction of a bar; half of an amount; Go further: part of a pile.
- **Remember (6 min).** (1) Fold a strip in half. (2) 4 quarters make 1. (3) Half of 8.
- **Start here (6).** Fold and cut; halves and quarters of a bar; the pizza left; quarters in 3 wholes (12); half of a number; shade a bar.
- **Think harder (4).** **NR (plan):** CTX (sharing with friends and cousins: the sharer counts), EQ (make three shares equal). (i) A cake shared among Mei and 3 friends: quarters. (ii) Three boxes with 15, 9 and 6 sweets are made equal: 10 each, so the first box gives away 5 (verified: 30 in all). (iii) Quarters in 3 wholes: 12. (iv) Half of a half.
- **Go further (3).** G1 **Beyond (named): "Half Then a Third".** Ali spends half of $48, then a third of what is left; he has $16 left (verified). Level note: fractions of an amount are P4. G2 CMP: Mei eats half of a cake and Ali a quarter of the same cake; a quarter is left (verified). G3 2/3 of 24 is 16 (verified).
- **Holiday overlap: MEDIUM.** Holiday Lesson 7 did the pizza and cake. Avoid cutting 3 squares in 4 ways (a Lesson 6 holiday item).
- **Numbers.** Amounts to 60.
- **Home materials.** 36 counters.
- **Kit.** 2 circles and 2 squares to fold (cut 4). Reuse the fraction wall.
- **Figures.** `fraction` (M3), `bar_model`.
- **Misconceptions.** Half of 8 as 4 of 8 shared unfairly; a third of 24 as 3.
- **Needs.** M2, M3.
- **Safe to miss?** No.

### Lesson 34. Big Numbers Expedition (T4.4)

- **Big idea.** A thousand is ten hundreds.
- **Strand.** MOE P2 numbers to 1000; four-digit numbers are P3 (p. 35): a preview. Papers: some (1000 itself).
- **Objective.** Read 3-digit numbers in words; 1000 as ten hundreds; Go further: biggest and smallest 4-digit from cards.
- **Remember (6 min).** (1) Build 253 from cards. (2) Count in 100s. (3) Compare 3 numbers.
- **Start here (6).** Words; 100 more than 906; 1000 as ten hundreds; order; write 3405 in words; place value of the 4.
- **Think harder (4).** **NR (plan):** LIST (form the greatest and smallest numbers from cards), LOG (number clue puzzle with even, odd and twice as many). (i) Greatest and smallest from 0, 3, 5, 8: 8530 and 3058 (verified). (ii) "I am a number from 4000 to 4999. My hundreds digit is 2, my tens digit is 3 more than my hundreds digit, my ones digit is even and my digits add up to 15": 4254, the only one (verified). (iii) How many hundreds are in 3400 (34). (iv) Hint: "Cross out."
- **Go further (3).** G1 **Beyond (named): "Four Card Count".** The cards 1, 2, 3, 4 once each make 24 four-digit numbers (verified), 12 greater than 3000 and 12 even (verified); the cards 0, 3, 5, 8 make 18. Level note: arrangements are P5 ideas. G2 CHAL: build a number from five clues. G3 how many.
- **Holiday overlap: HIGH.** Holiday Lesson 1 was a numbers lesson with digit cards. The term lesson is the 4-digit preview.
- **Numbers.** To 9999.
- **Home materials.** Digit cards 0 to 9.
- **Kit.** Thousands arrow cards 1000 to 9000 (9) + digit cards 0 to 9 (10): cut 19; reuse KA.
- **Figures.** `place_value` (M4).
- **Misconceptions.** 3405 written 345; zero as nothing; reading thousand as hundred.
- **Needs.** M4.
- **Safe to miss?** Yes (the plan's "stretch").

### Lesson 35. Calendar and Timetable Puzzles (T4.5)

- **Big idea.** Time repeats in cycles.
- **Strand.** MOE P2 time and calendar; weekday cycles are Beyond (SASMO calendar 5 problems, all gaps). Papers: some (TV guide, "saves $2 a day").
- **Objective.** Day after 10 days; read a timetable; "30 days from today" with weeks and left-over days; Go further: constraints.
- **Remember (6 min).** (1) Days of the week. (2) Count in 7s. (3) Read a clock.
- **Start here (6).** The day after 10 days; read a timetable; weeks in a month; a calendar page; leave at what time.
- **Think harder (4).** **NR (plan):** CTX (which day is it after $3 a day for 6 days), BACK (timetable: leave at what time to arrive by). (i) Wei saves $3 each day starting on Monday: $18 on Saturday (verified). (ii) 30 days from Tuesday is Thursday (verified). (iii) A bus leaves every 20 minutes from 7:05 am and the ride takes 25 minutes: to arrive by 8:00 am the child must catch the 7:25 bus (the buses are 7:05, 7:25, 7:45, ...; 7:45 arrives at 8:10; verified). (iv) Hint: "Draw a timeline."
- **Go further (3).** G1 **Beyond (named): "Same Date, Next Year".** A year of 365 days is 52 weeks and 1 day, so the same date next year is one weekday later; a leap year of 366 days is two weekdays later (verified). G2 CMP: gap between two clock times. G3 a month starting on a given day.
- **Holiday overlap: LOW** (Lesson 9 timetable).
- **Numbers.** Months of 28 to 31 days.
- **Home materials.** A calendar page.
- **Kit.** 7 day cards (cut 7) and a month page (not cut). Reuse KH.
- **Figures.** `calendar` (exists; needs 28 and 30 day months), `table`.
- **Misconceptions.** Counting today as day 1; a month as 30 days always; Sunday to Monday not wrapping.
- **Needs.** none new (calendar already takes `days`).
- **Safe to miss?** No.

### Lesson 36. Grid Treasure Hunt (T4.6)

- **Big idea.** Words can name places.
- **Strand.** Beyond MOE P1 to P3 (position and direction; Ontario Grade 2 spatial sense, to confirm). No school-paper evidence.
- **Objective.** Follow arrows; write directions; Go further: count routes.
- **Remember (6 min).** (1) Left and right. (2) Rows and columns. (3) Count squares on a path.
- **Start here (6).** Follow arrows from A to B; name a square by its column letter and row number (C3); draw a path from a list of directions ("2 right, 3 up"); write the directions for a path of 4 moves; find the treasure square from one clue; count the squares a path crosses.
- **Think harder (4).** **NR (plan):** PAT (continue a path from its directions), LOG (where is the treasure from three clues). (i) Right 1, up 1, right 2, up 2, right 3 ...: the next move is up 3. (ii) On a grid with columns A to D and rows 1 to 4: the treasure is not in an edge column, not in an edge row, and is on the same row as, and next to, the rock at D3: it is at C3. (iii) Write the directions for a path drawn on the grid. (iv) Hint: "Draw it."
- **Go further (3).** G1 **Beyond (named): "How Many Routes?".** Moving only right or up, a 2 by 2 grid of squares has 6 routes and a 3 by 3 grid has 20 (verified). G2 WAYS: if the middle crossing of the 2 by 2 grid is blocked, 2 routes remain (verified). G3 the shortest route round two rocks.
- **Holiday overlap: NONE.**
- **Numbers.** Grids to 5 by 5.
- **Home materials.** A counter.
- **Kit.** Grid mat (not cut). Cut 0.
- **Figures.** `grid` (route, start, end, counts; exists).
- **Misconceptions.** Counting the starting square; left and right swapped.
- **Needs.** none new.
- **Safe to miss?** Yes.

### Lesson 37. Spot the Mistake (T4.7)

- **Big idea.** A good solver finds the error.
- **Strand.** Error analysis across strands. Papers: some ("Who is correct?").
- **Objective.** Check a sum; find the wrong step; explain why a wrong method fails.
- **Remember (6 min).** (1) Check a subtraction by adding. (2) 3-digit column. (3) A tick/cross.
- **Start here (6).** Six worked sums with one wrong step; Right or Wrong; which step; check by adding back.
- **Think harder (4).** **NR (plan):** EXP (find the wrong step and say why). (i) 478 + 256 written as 724: the carry from the ones was forgotten, the right answer is 734 (verified). (ii) 603 - 278 = 435: check by adding back, 435 + 278 = 713, not 603, so it is wrong (the right answer is 325; verified). (iii) Does it make sense? 387 + 295 = 582 is too small, since 400 + 300 is already 700 (the right answer is 682; verified). (iv) Hint: "Check a different way."
- **Go further (3).** G1 **Beyond (named): "Nine Check".** Add the digits of each number; the digits of the two parts add up to the digits of the answer, until one digit remains: 478 + 356 = 834 passes (478 gives 19, then 1; 356 gives 14, then 5; 1 + 5 is 6; 834 gives 15, then 6); it catches a wrong digit but misses a swap of two digits and a change between 0 and 9 (verified: swapping any two digits is always missed, and 0 and 9 are the only single-digit changes that are missed). Level note: casting out nines is not a syllabus idea; it is a check, not a proof. G2 BACK: a child forgot the ones carry in 478 + [ ] and wrote 724; the right answer is 734, so the other number is 256 (verified). G3 CHAL: a puzzle that cannot work: fix it.
- **Holiday overlap: LOW** (Lesson 2 Mei's mistake).
- **Numbers.** 3-digit.
- **Home materials.** Pencil.
- **Kit.** 8 worked-sum cards (4 right, 4 wrong; cut 8), mat (not cut).
- **Figures.** `column_sum` (M5), `steps`.
- **Misconceptions.** A neat answer is right; fixing the step but not the later steps.
- **Needs.** M5.
- **Safe to miss?** Yes.

### Lesson 38. Problem Posers (T4.8)

- **Big idea.** Making a problem shows you know it.
- **Strand.** Problem posing (Beyond MOE). No school-paper evidence.
- **Objective.** Add a question to a picture; change numbers to change the answer; write a puzzle with one answer.
- **Remember (6 min).** (1) A story from a number sentence. (2) The three words that signal an operation. (3) Check a puzzle by listing.
- **Start here (6).** Add a question to a picture; change one number; a question that needs two steps.
- **Think harder (4).** **NR (plan):** CMP (change the numbers so the answer changes). (i) Change one number in a story so that the answer changes from 12 to 15. (ii) Choose the questions that can be answered from the picture graph (a question that cannot is marked). (iii) Write a story for 7 x 4. (iv) Hint: "Check by listing."
- **Go further (3).** G1 **Beyond (named): "Puzzle Doctor".** Two numbers add to 15 and differ by 4: impossible, since a sum and a difference must both be odd or both even (verified); fix the puzzle by changing the difference to 3 (answer 6 and 9; verified). G2 CHAL: write a graph problem from a picture, with a check. G3 MULTI: pose a two-step problem whose answer is 24 (the author's key checks the child's example by hand).
- **Holiday overlap: LOW.**
- **Numbers.** Mixed.
- **Home materials.** Pencil.
- **Kit.** 6 scene cards (cut 6).
- **Figures.** `objects`, `picture_graph`.
- **Misconceptions.** A puzzle with two answers; a question with no information.
- **Needs.** none new.
- **Safe to miss?** Yes (second safest of the term).

### Lesson 39. Look Again (T4.9)

- **Big idea.** Look closely, then check.
- **Strand.** Beyond MOE (visual perception: SASMO 5 problems, all Section A; nets are P4, p. 39, kept only here at Go further). No school-paper evidence.
- **Objective.** Same after turning?; mirror-flip a shape on tracing paper; Think harder: mirror clocks and digits, match a shadow, matchsticks; Go further: nets.
- **Remember (6 min).** (1) Turn a shape a quarter. (2) Fold a paper and open. (3) Read a clock.
- **Start here (6).** Is it the same picture after turning?; mirror-flip on tracing paper; which of four pictures is the mirror image; copy a figure; a shadow match.
- **Think harder (4).** **NR (plan):** LOG (mirror, turn and shadow clues), PAT (which turn comes next). (i) The mirror of 4:10 shows 7:50 (verified). (ii) In a plain font the digits 0, 1 and 8 look the same in a mirror (the author's verify file lists the font). (iii) The largest number from exactly 11 matchsticks is 71111 (verified; the smallest is 20). (iv) Match the shadow of a cone, a cylinder and a ball.
- **Go further (3).** G1 **Beyond (named): "Cube Nets".** Of the 35 shapes made of 6 joined squares, exactly 11 fold into a cube (verified); find 4 of them. Level note: nets are P4. G2 DIAG: nets and stacks drawn from two views. G3 turn a block picture.
- **Holiday overlap: MEDIUM.** Holiday Lesson 8 did nets E and F, a six-in-a-line net that cannot fold, and a 3 x 3 x 3 painted cube. The term lesson must not repeat the six-in-a-line item.
- **Numbers.** Seven-segment digit costs 0:6, 1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6.
- **Home materials.** Tracing paper, 11 paper strips (kept from Lesson 21), scissors for a grown-up.
- **Kit.** 4 net cards (cut 4). Reuse the Lesson 21 stick strips (KI) and the clock kit (KH).
- **Figures.** `clock` (mirror), `matchstick` (M11), `net` (M8), `grid` mirror.
- **Misconceptions.** A mirror turns left to right but not top to bottom; the net with a row of four always folds.
- **Needs.** M8, M11.
- **Safe to miss?** Yes (weakest evidence; open question 5 in the plan).

### Lesson 40. Year Challenge Day (T4.10), with Mi's Challenge Quest

- **Big idea.** Show what you can do.
- **Strand.** Mixed, contest-style, new problems; spiral of all four terms.
- **Objective.** Select a strategy; solve a two-step problem; end with a letter sum or a "be sure" question; present one's own puzzle.
- **Remember (6 min).** A mixed three-item warm-up (a pairing sum, a fraction and a table).
- **Start here (5).** A mixed set with reminder cards.
- **Think harder (3).** **NR (plan):** MULTI (a two-step mixed set), GC (coins for an exact amount). The last question is a letter sum or a "be sure" item.
- **Go further (3).** G1 **Beyond (named): "Showcase Puzzle".** Write a checked puzzle with one answer and present it; the group solves one other child's puzzle (shared inside the group only; Level 1 D9). G2 WAYS: how many ways without listing. G3 CHAL.
- **Holiday overlap: MEDIUM.** Holiday Lesson 10 Puzzle Day is a mixed lesson (the name "Puzzle Day" is kept for the holiday; this lesson is "Year Challenge Day" and the Quest).
- **Numbers.** Mixed.
- **Home materials.** A favourite page from the year, plain paper.
- **Kit.** None. Cut 0.
- **Figures.** Whatever the item needs.
- **Misconceptions.** Racing; ranking.
- **Needs.** Year Quest (section 6).
- **Quest.** Section 6.
- **Safe to miss?** Yes (the plan's safest), with the make-up Quest route.

---

## 2. Level 2 at a glance

"Holiday overlap" is the section 13 verdict: **High** = the holiday course has several questions of the same type and range (the term lesson must change its items), **Med** = some, **Low/None** = little or none. "Wave" is the build wave of section 11. The Quest lessons (10, 20, 30, 40) are Wave D for the Quest block; their lesson body can be written in an earlier wave.

| # | Title | Holiday overlap | Blocking template items | Wave | Safest to skip? |
|---|---|---|---|---|---|
| 1 | Where Does It Live? | High | M4, M13, M14, KA | B | No |
| 2 | Mind Maths Moves | Med | M5, M10 | B | Yes |
| 3 | Share It or Group It? | High | none (exists) | A | No |
| 4 | Chart Patterns | High | M18 (hatch); M13 for Go further | A | Yes |
| 5 | Shop Bills and Change | High | M14, KD | B | No |
| 6 | Cut It Equally | High | M2, M3, KE | B | No |
| 7 | Shape Splitters | High | KF, M12 | C | Second safest of T1 |
| 8 | Read the Scale | Med | M6, M7 | C | Yes |
| 9 | Story Detectives | High | none | A | No |
| 10 | Posts, Gaps and Queues | Med | Quest (section 6) | D | Yes, safest of T1 (Quest sits here) |
| 11 | Graphs That Talk | Med | M9 | C | No |
| 12 | Odd, Even, Fair | None | none (number cards) | A | Yes |
| 13 | Jumps, Gaps and Columns | High | M4, M5 | B | No |
| 14 | Bar Model Stories | High | none (KG) | A | No |
| 15 | Clock Detectives | High | KH, time fields (exist) | A | No |
| 16 | Table Tricks | Med | none | A | No |
| 17 | Find All the Ways | Med | none | A | Yes |
| 18 | Who Is Who? | High | M10 | C | Yes |
| 19 | Track It | Low | none | A | Second safest of T2 |
| 20 | Puzzle Lab 2 | High | M5, M10, Quest | D | Yes (Quest sits here) |
| 21 | Gaps That Grow | Med | none (KI) | A | No |
| 22 | Fractions on the Line | High | M2, M3 | B | No |
| 23 | Shape Equations | High | M6 | C | Yes |
| 24 | Estimate Like a Scientist | Low | M7 | C | Second safest of T3 |
| 25 | Spot the Solid | High | M8 | C | Yes |
| 26 | Tiles, Turns and Symmetry | None | M12 | C | Yes |
| 27 | Two-Step Bar Models | High | none | A | No |
| 28 | Longer Chains | Med | none | A | No |
| 29 | Always, Sometimes, Never | Low | none | A | Yes |
| 30 | Robot Recipes | None | Quest | D | Yes (Quest sits here) |
| 31 | Chance and Fair Games | None | M9 | C | Yes |
| 32 | Tables Bridge | Low | none | A | Yes |
| 33 | Halves and Quarters of Things | Med | M2, M3 | B | No |
| 34 | Big Numbers Expedition | High | M4 | B | Yes |
| 35 | Calendar and Timetable Puzzles | Low | none (calendar 28/30 days exist) | A | No |
| 36 | Grid Treasure Hunt | None | none | A | Yes |
| 37 | Spot the Mistake | Low | M5 | B | Yes |
| 38 | Problem Posers | Low | none | A | Second safest of T4 |
| 39 | Look Again | Med | M8, M11 | C | Yes |
| 40 | Year Challenge Day | Med | Quest | D | Yes (Quest sits here) |

## 3. New template capabilities Level 2 needs

Codes: **M** shared tool, figure or runner item; **K** kit page; hours are template-engineer estimates, not measured. Nothing here edits the Level 1 tool files today; the template owner does it, one owner per file (Level 1 rule 13/17: lesson agents write only `lNN.json`, `verify/lNN_checks.py`, `AUDIT_LNN.md` and `out/lNN/`; new figures go in a new `figs4.py` appended to `figs2.render`).

### 3.1 Tool-level items

**M1. Level parametrisation (all 40 lessons, about 6 h).** `term/l1/tools` reads `term/l1/` through `common.L1`, prints "Level 1" in the guide footer (`b_guide.py` line 198 and the cover), builds practice keys `t{term}l{NN}` and `AUDIT_LNN.md` paths from the level 1 folder, and the leak check knows only Level 1 titles. Add `LEVEL` (env or argument, default 1), a lesson folder `term/l2/` with its own `lessons/`, `verify/`, `out/`, `runner/` data, practice key prefix `l2t1l01`, "Level 2 • Term 1 • Lesson 4" on every family page, and a Level 2 title list for the leak check. [Default] The shared tools stay in `term/l1/tools` until Level 2 is built, then move to `term/tools` (a rename, not a copy: two copies of `validate.py` would drift). Acceptance: `bash term/l2/build.sh 01` builds a stub with a Level 2 footer on guide, deck, workbook, key, home sheet, parent page and Quest files, with a clean leak check.

**M2. Fraction and decimal text renderer (Lessons 6, 22, 33 and every lesson that names a fraction; about 8 h).** A token such as `{3/8}` renders stacked on slides, workbook, key, guide, home sheet and parent page, and prints as "3/8" in the plain-text and speech lines; answer tokens `[n/d]` print two stacked boxes; the PDF text checks (glyph check) accept the stack; the validator's wording and glyph checks must accept the token (Level 1 never used fractions; decision D16 of the Terms 3 and 4 pre-flight kept `1/2` out of Level 1). The holiday decks already have this `rich()` helper (`p2/content/l7.js`); port it, do not rewrite it. Decimal money `$3.05` needs no renderer, only the formatter in M14.

**M14. Runner and formatter additions (about 8 h).** (a) `{n|dec}` prints cents as dollars and cents (305 as $3.05) and `{n|cents}` the reverse; guard "1 dollars"; mixed forms `$4.60` accepted as `4.6` and `4.60` by number items. (b) Fraction answers through `fields` with a stacked layout (`[n/d]`). (c) Number words as a multiple-choice item, never a typed answer (spelling is an unfair marking trap: "four hundred and seven" versus "four hundred seven"). (d) Duration fields "[h] h [mm] min" and the pad map (exist as R6 in Level 1; confirm for minutes above 59). (e) A holiday-free practice bank: variants never reuse a holiday item (M15). (f) Ordered list answers for "list every number" (exist).

**M15. Validator and authoring updates (about 6 h).** Level 2 banned and allowed lists: the words remainder, equivalent, decimal point and letters for unknowns are banned on child and parent pages; "Hint:" stems allowed at Think harder only; a required tutor-only field `nonroutine: [{type, tier, item_id}]` (type from the 14 codes, tier T or G, never Start here) with the `contest_moves` plain-words line; `beyond` required (never Start here); a **holiday-copy check**: extract the 237 holiday question-bank items and the workbook questions to a text file at build time and warn on any 5-word overlap with a term question (the Level 1 7-word check already runs against the books and the catalogue; the holiday program is not in its source list); the `÷`, `×` and `¢` glyphs survive in every PDF; question forms for the P2 paper style ("Choose the correct answer and write its number in the brackets", options (1) to (4)); kit contract and `next_materials` checks as in Level 1.

**M17. Quest adaptation (about 3 h).** `b_quest.py` already takes gates naming one lesson, a list or "beyond", and `scope: "year"`; Level 2 needs four Quest definitions (section 6) and figures in gates (fractions, scales, solids), which depend on M3, M7, M8.

**M18. Black-and-white compliance (about 4 h).** Define hatch patterns for fraction shading, picture-graph rows, balance objects, tiles, bar-model segments and mirror pictures so nothing depends on colour (owner decision of 23 Oct); run `print/check_bw.py` on every Level 2 workbook, key and home sheet; every "colour" instruction in the lessons becomes "shade or hatch"; a coloured-pencil note on the kit pages. Stylised money and clock hands already differ by size, label and shape.

**M19. Books (about 2 h).** `print/make_term_books.py --level 2 --first 1 --last 40 --size 5 --per-term 10` (the script's own help says `--size 4`; use 5 per the owner's rule) with the Quest Log in Books 2, 4, 6 and 8, the tutor notes in the key books and the grown-up note in the home pack; confirm page counts after a build (`term_books_spec.json`). Estimated pages per book (workbook only): about 36 to 40.

**M20. Home-sheet rewind (about 4 h).** `home_practice[].rewind_of` exists; the runner rewind sets (RW) are deferred in Level 1. Level 2 rule in section 7.

**M21. Authoring documents (about 3 h).** A Level 2 brief (copy of `LESSON2_BRIEF.txt` plus this file's section 1 and 13) and a Level 2 wording brief (the P2 paper wording, section 1.0) before any agent starts; `AUTHORING.md` has a Level 1 Terms 1 to 4 section only.

### 3.2 Figures (new `type` values for slides, workbook, home sheet, key and practice)

| Code | Figure | Lessons | One-line spec | Hours |
|---|---|---|---|---|
| M3 | `fraction` | 6, 22, 33, Quests | Rectangle, circle, bar and grid cut into n equal parts (n to 12) with k parts hatched (no colour dependence); unequal option; fold lines; a fraction wall; a 0-to-1 number line with fraction labels and hidden ticks; a "parts to shade" mode; the existing `shapes2d` has parts 1, 2 and 4 only | 10 |
| M4 | `place_value` | 1, 13, 34 | Base-ten drawing (flat, rod, unit; thousand cube), place-value chart with counters, regroup arrow; a row of arrow cards that overlap | 6 |
| M5 | `column_sum` | 2, 13, 20, 37 | Vertical add and subtract with carry marks, empty digit boxes, shape-code and letter versions; one answer slot per box | 5 |
| M6 | `balance` | 8, 23 | Two pans with identical objects and weights in g or kg; hidden weights as boxes; hatch per object | 6 |
| M7 | `scale_dial`, `jug` | 8, 24, Quest | Kitchen scale dial 0 to 1 kg, 0 to 5 kg and 0 to 10 kg with ticks labelled every n; pointer at any value; jug, bottle and cup with litre, ml and cup marks and a fill level; the existing `ruler` (true scale) is reused | 8 |
| M8 | `solid`, `net`, `cube_stack` extension | 25, 39, Quest | Cube, cuboid, cone, cylinder, sphere, prism, pyramid in perspective with flat and curved faces marked; nets of 6 squares with fold marks; `cube_stack` heights to 4 and bases to 3 by 3 with a room-corner mode (the Level 1 engine caps at 3) | 9 |
| M9 | `spinner`, tally cell | 11, 31 | Disc with n sectors (equal or unequal) and a pointer; a `table` cell token for tally marks (four strokes and a bar) | 5 |
| M10 | `ring`, magic triangle, constraint grids | 2, 18, 20 | Eight circles round a square, magic triangle (6 circles), a hexagon grid of counts (optional) | 6 |
| M11 | `matchstick` | 39 | Seven-segment digits and shapes made of sticks, with a stick-cost table | 4 |
| M12 | `pattern_row`, tilted-square highlight | 7, 26 | A row of tiles with a ring on "the nth" and a hidden tile; `grid` option to outline a tilted square | 4 |
| M13 | Number line and chart modes | 1, 4 | Unmarked line with two labelled points and optional fraction labels; a hundred-chart offset (101 to 200) | 3 |
| | **Figures subtotal** | | | **66** |

The new figures build on the existing ones in `figs2.py` and `figs3.py` (objects, groups, array, bar_model, table, clock, money, grid, panel, picture_graph, cube_stack, stick_pattern, number_line, hundred) and follow the Level 1 rule that the picture must not lie (lengths, angles and sectors proportional).

### 3.3 Kit pages (see section 4 for piece counts)

| Code | Kit | Lessons | Hours |
|---|---|---|---|
| KA | `place_value_cards`: arrow cards, ones, tens, hundreds (27); thousands (9) | 1, 2, 13, 34 | 3 |
| KD | `play_money` (reuse; confirm the $100 note and 5¢ to $1 coins; PLAY MONEY mark) | 5, 28, 40 | 1 |
| KE | `fraction_wall` plus folding strips and squares | 6, 22, 33 | 3 |
| KF | `dissection_pieces` (4 L-trominoes, 4 dominoes, 4 unit squares) | 7 | 2 |
| KG | `unit_strips` (exists) | 14, 27 | 0.5 |
| KH | `clock_kit` (exists; check all 60 ticks) | 15, 35, 39 | 1 |
| KI | `stick_strips` (exists, n = 16) | 21, 39 | 0.5 |
| Cards | `cards` kit for number cards 1 to 20, tiles 1 to 8, weight cards, outfit cards, hat cards, shape tokens, solid cards, pattern tiles, claim cards, command cards, day cards, worked-sum cards, scene cards, net cards, digit cards 0 to 9 | 12, 17, 18, 19, 23, 25, 26, 29, 30, 34, 35, 37, 38, 39 | 4 |
| | **Kits subtotal** | | **15** |

### 3.4 Totals

M1 6 + M2 8 + M3 10 + M4 6 + M5 5 + M6 6 + M7 8 + M8 9 + M9 5 + M10 6 + M11 4 + M12 4 + M13 3 + M14 8 + M15 6 + kits 15 + M17 3 + M18 4 + M19 2 + M20 4 + M21 3 = **125 hours** if everything is built. **Deferrable without blocking a lesson (about 16 hours):** M11 (Lesson 39 can use drawn sticks), the hexagon grid inside M10 (2), M12 (Lesson 26 can use `panel` and `table`, 3), the net part of M8 (3; Lesson 39 G1 can show nets as `grid` polygons), M20 (4), and the `cube_stack` room-corner mode (Lesson 25 can use views). That leaves about **109 hours**.

### 3.5 What the engine already does for Level 2 (do not rebuild)

Clock to any minute with digital readout and mirror; money with $100 notes; calendar with any `days`; timelines through `number_line` labels; the bar model in all four modes; table with tick boxes and icons; tally in `picture_graph`; panel tiles with turn and pattern; grid routes and counts; the Quest builder with year scope; stick patterns; stacks to 3 by 3.


## 4. Kit contracts: supplied pieces against the most a task may use

The Level 1 cut-out audit found two Reworks (strips and shape cards) because piece counts were never checked against the tasks, and objected to 203 pieces in a term. `materials.kit_contract` makes the validator fail when supplied is less than max used. "Cut" is the number of pieces a grown-up cuts; nobody cuts in the lesson. Every kit page carries the standard note: one side only or its own sheet, a grown-up cuts a week before, pieces go in an envelope with the child's name, tear out along the dashed line, "no printer? use paper scraps / buttons". Cut lines at least 6 mm apart; counters and tiles are rounded squares, not small discs; colour never carries meaning alone; digits that can be turned (6, 9) are underlined.

| L | Kit | Supplied | Max used by a task | Cut | Reuse and notes |
|---|---|---|---|---|---|
| 1 | KA place-value arrow cards | 27 | 9 | 27 | keep for 2, 13, 34 |
| 2 | reuse KA | 0 | 6 | 0 |  |
| 3 | plates mat (printed, not cut) | 6 | 5 | 0 | counters from home |
| 4 | numbered hundred chart (printed, not cut) | 1 | 1 | 0 | 12 counters from home |
| 5 | KD play money | 32 | 25 (5¢ x 2, 10¢ x 4, 20¢ x 3, 50¢ x 2, $1 x 4, $2 x 3, $5 x 3, $10 x 3, $50 x 1) | 32 | keep for 28, 40 |
| 6 | KE fraction wall (not cut) + 4 folding strips + 2 folding squares | 6 | 6 | 6 | keep for 22, 33 |
| 7 | KF dissection pieces (4 L-trominoes, 4 dominoes, 4 unit squares) | 12 | 12 | 12 |  |
| 8 | none (scales printed) | 0 | 0 | 0 |  |
| 9 | none | 0 | 0 | 0 |  |
| 10 | none (line mat printed) | 0 | 0 | 0 | 12 counters from home |
| 11 | graph mat (printed, not cut) | 1 | 1 | 0 |  |
| 12 | number cards 1 to 20 + pairs mat (mat not cut) | 20 | 20 | 20 |  |
| 13 | reuse KA | 0 | 9 | 0 |  |
| 14 | KG unit strips (8 strips of 10 cells) | 8 | 6 | 8 | keep for 27 |
| 15 | KH clock kit (2 faces, 3 + 3 hands) | 6 | 4 | 6 | keep for 35, 39 |
| 16 | array mat 5 by 8 (printed, not cut) | 1 | 1 | 0 |  |
| 17 | outfit cards (3 shirts, 4 shorts) | 7 | 7 | 7 |  |
| 18 | number tiles 1 to 8 + weight cards P, Q, R, S | 12 | 12 | 12 | keep tiles for 20 |
| 19 | hat cards R, R, B, B | 4 | 4 | 4 |  |
| 20 | reuse tiles | 0 | 6 | 0 |  |
| 21 | KI stick strips | 16 | 16 | 16 | keep for 39 |
| 22 | 4 folding strips + 0-to-1 line (line not cut) | 4 | 4 | 4 | may reuse KE |
| 23 | shape tokens (5 shapes x 3) | 15 | 9 | 15 |  |
| 24 | none | 0 | 0 | 0 |  |
| 25 | solid picture cards | 10 | 10 | 10 |  |
| 26 | pattern tiles (3 shapes x 4) | 12 | 12 | 12 |  |
| 27 | reuse KG | 0 | 6 | 0 |  |
| 28 | reuse KD | 0 | as Lesson 5 | 0 |  |
| 29 | claim cards + 3-pocket mat (mat not cut) | 12 | 12 | 12 |  |
| 30 | command cards + grid mat (mat not cut) | 12 | 12 | 12 |  |
| 31 | 3 spinner discs (printed, not cut) | 3 | 3 | 0 | paper clip and pencil from home |
| 32 | reuse array mat | 0 | 1 | 0 |  |
| 33 | 2 fold circles + 2 fold squares | 4 | 4 | 4 | reuse fraction wall |
| 34 | thousands arrow cards 1000 to 9000 + digit cards 0 to 9 | 19 | 5 | 19 | reuse KA |
| 35 | 7 day cards + month page (page not cut) | 7 | 7 | 7 | reuse KH |
| 36 | grid mat (printed, not cut) | 1 | 1 | 0 |  |
| 37 | worked-sum cards (4 right, 4 wrong) + RIGHT/WRONG mat | 8 | 8 | 8 |  |
| 38 | scene cards | 6 | 6 | 6 |  |
| 39 | net cards (2 fold, 2 do not) | 4 | 4 | 4 | reuse KI strips, KH |
| 40 | none | 0 | 0 | 0 |  |

Cut per book: Book 1 (1 to 5) 59, Book 2 (6 to 10) 18, Book 3 (11 to 15) 34, Book 4 (16 to 20) 23, Book 5 (21 to 25) 45, Book 6 (26 to 30) 36, Book 7 (31 to 35) 30, Book 8 (36 to 40) 18. Per term: Term 1 77, Term 2 57, Term 3 81, Term 4 48; year 263. The Level 1 audit's complaint was 203 pieces in one term; Terms 1 and 3 of Level 2 are the heavy ones (77 and 81), and Lessons 5 (32 pieces), 1 (27), 12 (20) and 34 (19) are the heavy single kits. Mitigations: print the money and the arrow cards on card stock (D12), say "a grown-up cuts a week before" in the hand-off of the lesson before, one envelope per kit, and keep the "no printer" line on every page.

The home-materials rule: **a "Level 2 home box"** (named once in the welcome note and the Lesson 1 hand-off) holds 30 counters or buttons or beans (never sweets), two pencils or pens (hatching), a cm ruler, scissors for the grown-up only, 14 same-size blocks or small boxes (Lessons 25 and 39 only; drawn stacks are the fallback), a cup and a 1 litre bottle (Lessons 8 and 24), baking paper or tracing paper (Lessons 26 and 39), a coin and a paper clip (Lesson 31), 11 paper strips (never matchsticks or toothpicks), a calendar page. A cm ruler is a Level 2 assumption (P1 outcome); the Level 1 decision "no printed ruler" stands, so Lesson 8 and the Quest gate that needs a ruler must say "no ruler? tell your tutor" (D14).


## 5. Hand-off materials chain

The Level 1 audits found 7 of 9 "pencil and paper only" lines false, and a missed L10-to-L11 kit. Rule: `parent.next_materials` of lesson n lists everything lesson n+1 needs that a family must prepare: the book (given on payment), any kit page to cut, anything kept from earlier, anything to find at home. Under the owner's decision the wording is "your next workbook is in your book; tear out the kit page along the dashed line, then a grown-up cuts out the pieces" (never "print it a week before"). Books: 1 = lessons 1 to 5, 2 = 6 to 10, 3 = 11 to 15, 4 = 16 to 20, 5 = 21 to 25, 6 = 26 to 30, 7 = 31 to 35, 8 = 36 to 40. Term breaks fall at 10 to 11, 20 to 21 and 30 to 31; book boundaries at 5 to 6, 10 to 11, 15 to 16, 20 to 21, 25 to 26, 30 to 31 and 35 to 36.

| From to | The family must have ready | Keep from before | Check and hazard |
|---|---|---|---|
| Welcome to 1 | Book 1; the Level 2 home box; pencil; the Lesson 1 arrow cards cut (27 pieces, a grown-up cuts a week before) |  | Nothing in the welcome note is a purchase except a ruler if the family has none |
| 1 to 2 | Nothing new to cut; pencil, paper | The place-value arrow cards (Lessons 2, 13, 34) |  |
| 2 to 3 | 30 counters; five plates or cups; the plates mat is printed, no cutting | The arrow cards |  |
| 3 to 4 | Two pencils or pens for two hatch patterns; 12 counters; the numbered hundred chart is in the book |  | B&W print: the child hatches, never 'colours' |
| 4 to 5 | The play-money pages cut (32 pieces over two pages) |  | The heaviest cutting of Term 1; give a week's notice; print on card if the owner agrees (D12) |
| 5 to 6 (book) | Book 2 in the house; 4 folding strips and 2 folding squares cut (6 pieces); two pencils | Play money (Lessons 28 and 40) | Book boundary: if Book 2 arrives with a later instalment this fails (D11) |
| 6 to 7 | The 12 dissection pieces cut; an envelope | The fraction strips (Lessons 22, 33) |  |
| 7 to 8 | A cm ruler; a jug or cup; a kitchen scale if there is one; nothing to cut |  | Ruler hazard (D14) |
| 8 to 9 | Paper strips for bars; counters | |  |
| 9 to 10 | 12 counters or coins for posts; a quest partner; the Quest Log stays closed in Book 2 |  | Same rule as Level 1 Lesson 19 to 20: the Quest Log is never opened before the lesson |
| 10 to 11 (term and book) | Book 3; pencil; a tally from a home survey is optional; nothing to cut | The arrow cards (Lesson 13), the play money | Term break; new book |
| 11 to 12 | The 20 number cards cut; two plates |  |  |
| 12 to 13 | Nothing new; squared paper | The arrow cards from Lesson 1 (must be found) | Likeliest lost kit of Term 2 |
| 13 to 14 | 8 unit strips cut (a grown-up cuts a week before); paper strips |  |  |
| 14 to 15 | The clock kit cut (2 faces are not cut; 6 hands cut); a real clock if there is one | The unit strips (Lesson 27) | Hands are loose, no fastener |
| 15 to 16 (book) | Book 4; 40 counters; the multiplication grid is printed | The clock kit (Lessons 35, 39) | Book boundary |
| 16 to 17 | The 7 outfit cards cut; a bag of 12 small things of 3 kinds (not food) |  |  |
| 17 to 18 | The 8 number tiles and 4 weight cards cut (12 pieces); pencil and eraser |  |  |
| 18 to 19 | The 4 hat cards cut; three cups; 60 beans or buttons | The tiles (Lesson 20) |  |
| 19 to 20 | The Quest Log stays closed in Book 4; a quest partner | The tiles (6 needed) |  |
| 20 to 21 (term and book) | Book 5; the 16 stick strips cut; pencil | The clock kit (Lessons 35, 39), the unit strips (Lesson 27) | Term break; new book |
| 21 to 22 | The 4 folding strips cut (or the Lesson 6 strips); a 20 cm 0-to-1 line is printed |  |  |
| 22 to 23 | The 15 shape tokens cut; two kinds of counters; cups |  |  |
| 23 to 24 | A cup; a bag of beans (about 300 g in a cup); a 1 litre bottle; a ruler; a kitchen scale if any |  | Beans are a measuring material, not food |
| 24 to 25 | 14 same-size blocks or small boxes; the 10 solid cards cut; a tin, a ball, a box |  | Fallback: drawn stacks (D13) |
| 25 to 26 (book) | Book 6; the 12 pattern tiles cut; baking paper; a small mirror if there is one |  | Book boundary |
| 26 to 27 | Paper strips | The unit strips from Lesson 14 |  |
| 27 to 28 | Nothing to cut | The play money |  |
| 28 to 29 | The 12 claim cards cut |  |  |
| 29 to 30 | The Quest Log stays closed in Book 6; a quest partner; the 12 command cards cut; a counter |  |  |
| 30 to 31 (term and book) | Book 7; a coin; a paper clip; a pencil; the spinner pages are in the book |  | Term break; new book |
| 31 to 32 | 60 counters; nothing to cut | The array mat page |  |
| 32 to 33 | The 4 fold shapes cut; 36 counters | The fraction wall |  |
| 33 to 34 | The 19 cards cut (9 thousands arrow cards, 10 digit cards) | The arrow cards from Lesson 1 | Lost-kit hazard |
| 34 to 35 | The 7 day cards cut; a calendar page | The clock kit |  |
| 35 to 36 (book) | Book 8; a counter; the grid mat is in the book |  | The book boundary falls here: if Book 8 comes with a later instalment it must be posted before Lesson 35 ends, or this hand-off line is false (D11) |
| 36 to 37 | The 8 worked-sum cards cut |  |  |
| 37 to 38 | The 6 scene cards cut |  |  |
| 38 to 39 | Baking paper; the 4 net cards cut; the 11 stick strips from Lesson 21; the clock kit |  | Strips kept from Lesson 21: the likeliest lost kit of Term 4 |
| 39 to 40 | The Quest Log stays closed in Book 8; a quest partner; a favourite page from the year; plain paper |  |  |
| 40 to next | The tutor sends the Level 3 or next-term placement note; no list is printed here |  | Not a lesson-file concern |

## 6. Mi's Challenge Quest in lessons 10, 20, 30 and 40

The Level 1 Quest (Lesson 20) is the model: 20 minutes at minutes 35 to 55 straight after the brain break; 8 short gates and one optional secret cave; a quest partner (a sibling, a grown-up or a friend; the tutor pairs a solo child with the tutor's example); private paper; no score, no mark, no ranking, no visible timer, no "test" or "exam" on any child or parent page; the tutor keeps private notes only (for one parent line and next-term group advice); the Quest is never the part that shrinks in a slow class; the cave is the only place for a puzzle the children have not met; a child may pass any gate. Timing: Opening 2, Remember 6, Sneak-peek 4, Explore 10, Mini-lesson 9, Break 4, Quest 20, Workbook 25 (Start here only, about 16 minutes for a middle child; pages 3 to 5 for home), Talk 4, Look-back 2, Flex 4. The exit ticket is an optional item at home. Three files per Quest: `LNN_Quest_Log.pdf` (3 pages, in Books 2, 4, 6 and 8), `LNN_Quest_Tutor_Notes.pdf` (key book), `LNN_Quest_Parent_Note.pdf` (home pack). Recording is paused for the Quest and the make-up child does the Quest before watching the recording (`rec_pause_say`).

Every lesson of the term is visited by exactly one gate; two gates per Quest cover two lessons each (one short item from each, written as parts (a) and (b)), so ten lessons fit eight gates. The pairing differs by term as the tables show (Term 1: lessons 1 and 2, 8 and 9; Term 2: 11 and 12, 18 and 19; Term 3: 21 and 22, 27 and 28; Term 4: 31 and 32, 37 and 38). Every gate item is at Start here level for its own lesson; every answer below was recomputed. The Quest Log may carry figures (clock, fraction, scale) once M3, M7 and M8 exist; until then the gate states the picture in words and the author checks `b_quest.py` draws it.

**Gates for the Term 1 Quest (Lesson 10).**

| Gate | Lessons | Item (answer) | Figure |
|---|---|---|---|
| 1 | 1, 2 | Write 508 in words (choose (1) to (4)); 76 + 49 (125) | none |
| 2 | 3 | Ben shares 20 stickers equally with his 4 cousins: how many does each person get (4: 5 people) | `groups` |
| 3 | 4 | Counting in 5s from 5: will 60 be said (yes); will 62 (no) | `hundred` |
| 4 | 5 | A pen costs 240¢ and a ruler 85¢: total in cents 325¢, write $3.25; change from $5 is $1.75 | `money` |
| 5 | 6 | A bar is cut into 8 equal parts and 5 are hatched: write the fraction (5/8); hatch 2 more (7/8) | `fraction` |
| 6 | 7 | Cut a 2 by 3 rectangle into two equal parts along grid lines: how many squares in each (3) | `grid` |
| 7 | 8, 9 | A scale marked every 100 g to 1000 g, the pointer at the 7th tick (700 g); Ali has 250 stickers and Mei has 80 more than Ali (330) | `scale_dial` |
| 8 | 10 | Posts 5 m apart along a 20 m fence from 0 m: how many posts (5) | `number_line` |
| Cave | beyond | I am a number from 400 to 499. My ones digit is 3 more than my hundreds digit and my digits add up to 13 (427; unique, verified) | none |

**Gates for the Term 2 Quest (Lesson 20).**

| Gate | Lessons | Item (answer) | Figure |
|---|---|---|---|
| 1 | 11, 12 | One picture stands for 4 children and a row has 6 pictures (24); is 7 + 9 odd or even (even) | `picture_graph` |
| 2 | 13 | 4[ ]7 + 235 = 672: the missing digit (3; 437 + 235 = 672) | `column_sum` |
| 3 | 14 | Ali has 45 stickers and Mei has 28 more: draw the bars and find Mei's (73) | `bar_model` |
| 4 | 15 | A film starts at 5:35 pm and lasts 1 h 50 min: when does it end (7:25 pm; verified) | `clock` |
| 5 | 16 | True or false: 5 groups of 3 is the same as 3 groups of 5 (true); 4 x 7 is double 2 x 7 (28) | `array` |
| 6 | 17 | 2 drinks and 4 snacks: how many different meals of one drink and one snack (8) | `table` |
| 7 | 18, 19 | Box A is heavier than B and C is lighter than B: the lightest (C); Ali gives Mei 6 marbles and now both have 20: Ali had 26, Mei 14 | `table`, `bar_model` |
| 8 | 20 | Pair the numbers to make tens: 16 + 4 + 13 + 7 + 8 + 2 (50) | none |
| Cave | beyond | Seven children each have an odd number of sweets: is the total odd or even (odd; seven odd numbers add to an odd number, checked for random sets) | none |

**Gates for the Term 3 Quest (Lesson 30).**

| Gate | Lessons | Item (answer) | Figure |
|---|---|---|---|
| 1 | 21, 22 | Next in 4, 6, 9, 13, 18 (24: the gaps are 2, 3, 4, 5, so the next gap is 6); which is greater, 5/12 or 7/12 (7/12) | `fraction` |
| 2 | 23 | Two circles total 14, a circle and a triangle total 11: circle 7, triangle 4 | `picture_equation` |
| 3 | 24 | Which is about right for the mass of a pencil case: 5 g, 500 g or 50 kg (500 g) | `scale_dial` |
| 4 | 25 | A ball is which solid (sphere); how many faces does a cuboid have (6) | `solid` |
| 5 | 26 | Circle, triangle, triangle repeated: the 14th shape (triangle; 14 is 4 laps of 3 and 2 more) | `pattern_row` |
| 6 | 27, 28 | Siti has 60 stamps and Ali has twice as many: together 180; 5 books cost $30, so 2 books cost $12 | `bar_model` |
| 7 | 29 | Always, sometimes or never: even + even is even (always) | none |
| 8 | 30 | The robot faces north: forward 2, turn right, forward 3: it ends 2 squares north and 3 squares east | `grid` |
| Cave | beyond | Mei is 8 and Dad is 38: in how many years will their ages total 66 (10; the total is 46 now and grows by 2 a year) | none |

**Gates for the Year Quest (Lesson 40; `scope: "year"`).**

| Gate | Lessons | Item (answer) | Figure |
|---|---|---|---|
| 1 | 31, 32 | A spinner has 4 equal parts, 3 red and 1 blue: is blue likely, unlikely or certain (unlikely); 4 x 6 (24) | `spinner` |
| 2 | 33 | A bar of 8 equal parts: hatch a quarter (2 parts) | `fraction` |
| 3 | 34 | How many hundreds make 1000 (10) | `place_value` |
| 4 | 35 | Today is Wednesday: what day is it 12 days later (Monday; verified) | `calendar` |
| 5 | 36 | A counter starts at A and moves 2 right and 1 up: which square (the author sets the grid) | `grid` |
| 6 | 37, 38 | 45 + 38 = 73: right or wrong (wrong; 83); write one question for a picture graph | `picture_graph` |
| 7 | 39 | Which capital letter looks the same in a mirror held beside it: A, B, C or D (A) | none |
| 8 | 40 | 3 boxes with 4 pens in each box and 5 loose pens: how many pens in all (17) | none |
| Cave | beyond | The largest number made with exactly 8 matchsticks (1111; verified: 7111 uses 9) | `matchstick` |

Quest rules for authors: wording from `BAN_FAMILY` in `b_quest.py`; "pass is always allowed"; the paired gates are two-part gates (a, b), so the Quest Log stays at 8 gates; the cave never repeats a lesson item; Lessons 10, 20, 30 and 40 each lose 20 minutes, so Explore and Mini-lesson are shortened to 10 and 9 and the Start here workbook becomes 25 minutes (5 Start here questions, 3 Think harder); the Quest and the Look-back never both run live in a slow class (Look-back is dropped first, then the optional slide, never the Quest); a child who joins at Lesson 10, 20, 30 or 40 has not met earlier gates, so every gate is Start here level for its own lesson and "pass" is always allowed (Level 1 Lesson 20 wording).


## 7. Spiral review across the year

The Level 1 Term 1 audit (F4) found no spiral review; Level 1 Terms 3 and 4 added "Mi's rewind". The Level 2 rule differs because of owner decision 22 Oct: holiday lessons are not reused, and holiday topics return in warm-ups only. Three layers, none of which adds minutes to the 90:

1. **Home sheet slot 5 is "Mi's rewind" (M20).** For lessons 11 to 40 the item comes from lesson n - 10 (so Term 2 revisits Term 1, Term 3 revisits Term 2, Term 4 revisits Term 3). For lessons 5 to 10 it comes from lesson n - 4 (inside Term 1). Lessons 1 to 4 have no earlier lesson: slot 5 is "try it at home with real things". Items are copied by id from the earlier lesson's home or online bank, never rewritten, and the answer is on the separate answer sheet.
2. **Online practice ends with two rewind items from lesson n - 5** (lessons 6 to 40).
3. **The Quest cave and the Remember warm-up.** The third Remember item may be a spiral item when the prerequisite allows (marked in section 1).

**Spiral threads (the lessons that carry each).**

| Thread | Term 1 | Term 2 | Term 3 | Term 4 |
|---|---|---|---|---|
| Place value and number lines | 1, 2 | 13 | 21 (sequences to 300) | 34 (to 4 digits) |
| Fractions | 6 | (warm-up) | 22 | 33 |
| Money | 5 | (Quest) | 28 (price of one) | 33 (half then a third), 40 |
| Bars and word problems | 9 | 14, 19 | 27, 28 | 38 |
| Time and calendar | none | 15 | none | 35, 39 (mirror clocks) |
| Patterns and rules | 4 | 16 | 21, 26, 30 | 32, 36 |
| Listing and ways | 1, 6, 10 | 17, 18 | 22 | 31, 36 |
| Logic and reasoning | 10 | 18, 19 | 29 | 37, 39 |
| Equality and balance | 2 | 12, 19 | 23 | 38 |
| Shapes and solids | 7 | (none) | 25, 26 | 39 |
| Measures | 8 | (none) | 24 | (none) |

Gaps this table shows: Term 2 has no shapes, fractions, money or length-mass-volume lesson (the plan's design; the Term 2 Quest therefore has no shape, fraction or money gate); Term 4 has no length-mass-volume lesson. Mi's rewind items from Term 1 fill part of this in Terms 2 and 3. The holiday topics that Level 2 warm-ups revisit (never as the lesson): T2 number line, equal groups, dollars and cents, halves and quarters; T3 patterns, odd and even, one bar, the clock, doubling; T4 bars, tally and graphs, tables, the calendar (plan section 3).

**Remember warm-ups that spiral (third item).** 11: count in 5s (Lesson 4). 12: counters in pairs (Lesson 3). 13: hundreds, tens, ones (Lesson 1). 14: more than and fewer than (Lesson 9). 15: 60 minutes in an hour (the scales of Lesson 8). 16: equal groups (Lesson 3). 17: pairs (Lesson 12). 18: ordering heights (Lesson 10 queue). 19: transfers (Lesson 14). 21: the 100 chart (Lesson 4). 22: equal parts (Lesson 6). 23: balance (Lesson 12). 24: reading a scale (Lesson 8). 25: layers of cubes (holiday topic). 26: patterns (Lesson 21). 27: bar (Lesson 14). 28: price of one (Lesson 5). 29: odd and even (Lesson 12). 30: grid directions (Lesson 10). 31: tally (Lesson 11). 32: arrays (Lesson 16). 33: fractions (Lesson 22). 34: place value (Lesson 1). 35: clock (Lesson 15). 36: counting squares (Lesson 7). 37: columns (Lesson 13). 38: a graph (Lesson 11). 39: turns (Lesson 26). 40: tutor-led picks.


## 8. Known failure patterns from Level 1: author checklist

Read from `TERM_WIDE_AUDIT`, `CUTOUT_AUDIT`, `FINAL_AUDIT_T1`, `FINAL_AUDIT_T2` and `FIXES_L11` to `FIXES_L20`. Each line is something the Level 1 fix passes repaired more than once, so Level 2 authors should not write it in the first place.

1. **Kit counts do not match tasks** (strips, shape cards, tokens, counters). Fixed by the kit contract (section 4); the verify script asserts it.
2. **Hand-offs are false** ("pencil and paper only", a missing kit, "Lesson 3" meaning two things). Section 5; a hand-off check (`next_materials` against the next lesson's kit and keep list) as in Level 1.
3. **Workbook questions repeat class numbers.** No Start here or Think harder number is used in Explore, Mini-lesson, the sneak-peek or the Quest; the verify script asserts it.
4. **Answers printed on the slide while the question is asked.** Use `reveal` blocks and answer slides; Explore pictures never carry the count.
5. **Family pages use the global number.** Write "Term 3 Lesson 4"; the leak check rejects "Lesson 1" outside `lesson_in_term` 1; the next lesson of Lesson 10 is "the first lesson of Term 2".
6. **Start here too long for the 28 workbook minutes.** Six Start here items (page 1 about 8 minutes, page 2 about 9, a choice about 3); say on the page that Think harder and Go further are for home. In the four Quest lessons: 5 Start here items in 25 minutes.
7. **Keys that accept one order only** (3 x 4 and 4 x 3). Accept both orders; fractions equal to the same value accepted as given only (equivalence is P3); money in either notation; times with or without a leading zero; "ways" lists in any order.
8. **Recording and camera script.** Greet by name first, then start recording; no papers held to the camera; ticks not stars; the same mic routine in every lesson; the make-up child's route; the recording sentence before anything is recorded (Level 1 FINAL_AUDIT_T2 finding 4 found six lessons that said it after).
9. **"I am still stuck" route.** The look-back page the grown-up photographs to the business WhatsApp; no number on slides or in recordings.
10. **Parent page.** A "do not teach" line, a words list that explains each new term, a "when stuck" line, the beyond statement, and the term line. New at Level 2: the words list explains "equal parts", "fraction", "tally", "key", "net" and "left over".
11. **Runner variants.** "1 hours", "1 stickers", double full stop, raw placeholders in frames (found again in Level 1 Term 2: "1 stickers" in L17, "1 sweets" in L19). Guard variable ranges, add a plural guard, verify every variant three ways. Level 2 adds: decimal money variants never produce $3.5, and fraction variants never print an unsimplified item that is not asked.
12. **Investigation page overflow.** A drawing box, 4 lines, an easy first step; tables did not fit page 5 in four Level 1 lessons.
13. **Small pictures on the workbook.** Give `size` and column width for the new figures in the first build (fractions, balance, scale, jug, solid, net, ring).
14. **Wrong working attached to cast names.** "A child" or "a child in another class".
15. **Children cutting with scissors in the lesson.** A grown-up cuts beforehand.
16. **Contest label on a child page.** `contest_where` names the tiers; "Challenge" appears only in "Mi's Challenge Quest"; "Beyond" is a tutor-only word.
17. **Colour or glyph reliance.** Hatch, label or shape per category (M18); fractions and graphs are the new risk.
18. **Slow-class overrun.** No part OVER in the slow-class model; the Quest is never the part that shrinks.
19. **Mi's calculator image.** Builders use `mi_dolphin_nocalc.png` once supplied; stale builds still carried the old Mi in Level 1 Lessons 11 and 17 (FINAL_AUDIT_T2 finding 1): rebuild after any asset change and compare the mascot hash.
20. **A failing validator blocks rebuilds** (Level 1 Lessons 3, 10, 11 and 17 failed the 7-word copy check against the in-house catalogue). Fix: write the item in your own words from the start; the validator excludes "original" and "catalogue" files; the catalogue examples (EX-...) are patterns, not text to paste, and a Level 2 item that mirrors an EX item word for word will fail.
21. **New at Level 2: the holiday overlap** (section 13). Run the holiday-copy check (M15) before the audit, not after.
22. **New at Level 2: scope of notation.** Fractions stacked (M2); $ and ¢ both; no decimal addition before Go further; no "remainder", "equivalent", "decimal point", "average", "ratio" on child pages.
23. **New at Level 2: uniqueness claims.** Any "exactly one answer" or "exactly N ways" statement in a key must be checked by brute force in `verify/lNN_checks.py` (several in this document: 5 ways to make 110¢ with 7 coins, 7 sets of three tops that sum to 12, 11 nets of a cube, 1 ring).


## 9. Risks

1. **Holiday repeat (High).** A holiday graduate starts Term 1 and would meet the same question types, sometimes the same numbers (section 13). Mitigation: the register, the holiday-copy check (M15), and a rule that every shared type needs new numbers and one new twist. Residual: a child who did the holiday course will still find Lessons 5 (money), 6 (fractions) and 15 (time) partly familiar; the guide must say so honestly ("you may know some of this from the holiday course; today we go further").
2. **Tier honesty.** The likeliest repeats from Level 1: a contest move at Start here ("the sharer counts", a letter sum, pairing sums, "odd + odd", a chance word), a written reason at Start here, a three-step story at Start here (Lesson 28 is the one lesson that can slip), tilted squares in Lesson 7. Keep Start here to P2 school content with scaffolding; every beyond puzzle is Think harder or Go further.
3. **Scope of P2 versus P3.** Decimal addition (Lesson 5), finding a start or a duration in general (Lesson 15), fractions of an amount (Lesson 33), four-digit numbers (Lesson 34), tables 6 to 9 (Lesson 32), unlike fractions (Lesson 22 beyond item) are P3 or P4 on the syllabus (pp. 35, 37); each is a labelled beyond item or Go further, never Start here, and the tutor guide and parent page say so plainly with no "MOE-aligned" wording (owner decision of 22 Oct, carried over).
4. **Fractions and decimal notation tooling.** Nothing in the term tools renders them (M2, M14); a first build without M2 prints "3/8" as plain text and the Level 1 validator rejects it. Lessons 6, 22, 33 cannot start until M2 and M3 exist.
5. **School-paper evidence is missing or thin for 7 lessons** (30, 31, 36, 38, 39; 32 and 34 are Above). The wording of those items is the author's, matched to the closest paper style; the plan already marks them "optional".
6. **Papers I could not read.** The 2019 zip (58.9 MB) and the 2021 zip (7 MB) were never opened, so 2019 and 2021 patterns may be under-counted (2019 still dominates the counts); the four rendered scans were read at about 45 dpi. The money, time and fraction ranges in section 1 are the papers' and are unverified for items lost in OCR.
7. **Colour reliance in B&W print.** Fractions, graphs, balance objects, tile patterns, mirror pictures: see M18. A Level 2 figure that passes in colour and fails in `check_bw.py` is not finished.
8. **Cutting load.** Terms 1 and 3 are 77 and 81 pieces; Lesson 5 alone is 32. Print on card if the owner agrees (D12).
9. **Blocks at home (Lessons 25 and 39).** 14 same-size blocks may not exist in every house; the drawn-stack fallback must be a complete lesson, not a degraded one (Level 1 D14).
10. **A cm ruler (Lessons 8, 10, the Term 1 Quest).** Level 1 decided against a printed ruler; at Level 2 the ruler is a P1 outcome, so a family without one is a problem. D14.
11. **Mid-year entry.** June holiday graduates enter at Lesson 21 with the holiday course only; they know bars, fractions, money and time, so Lessons 21 to 30 are reachable; Lessons 27 and 28 draw the bar from scratch in Start here (plan section 3). A school-only child joining at Lesson 21 may not know Lesson 14's bar: Remember re-teaches it. A cold joiner at Lesson 5 may not know tables: Lesson 5 does not use them. Trial Lesson 5 and Lesson 21 with one cold joiner before launch (D19).
12. **Quest for a cold joiner.** Every gate is Start here level for its own lesson and "pass" is always allowed; the cave is optional.
13. **Reading load.** Ages 7 to 9 read more than Level 1 children, but P2 papers already carry three-sentence stems. Child-facing strings stay under 40 words (validator warning); the tutor reads each question aloud the first time.
14. **Safeguarding in Lesson 40.** Children present puzzles on camera: voluntary, pass allowed, no ranking, no votes, no "best", nothing shared outside the group without a grown-up's agreement (Level 1 D9); presentations are recorded under the existing recording statement.
15. **Print and post.** Eight books of about 36 to 40 pages; Books 2, 4, 6 and 8 contain a Quest Log (kept closed). Posting both books of a term with the first payment avoids a missing book in mid-term (D11).
16. **Parallel agents on shared files.** Same rule as Level 1: only the template owner edits `figs*.py`, `validate.py`, `common.py`, `b_*.py`; lesson agents write only their own files.
17. **Authoring documents are Level 1 specific.** `AUTHORING.md` and the lesson briefs name Level 1; M21.
18. **Level 1 Term 4 is still being written** by other agents; Level 2 reuses the same tools, so any Level 1 Term 4 tool change (a new figure) lands in the same files. Coordinate through the template owner and rebase Level 2 template work onto it.
19. **The 90-minute slot problem is not a Level 2 matter but it blocks the launch.** The 2027 grid has 75-minute slots; the owner said 90 minutes and the slots must be recomputed (owner decisions of 23 Oct). A 7-to-9-year-old after school for 90 minutes is longer than a 6-year-old's: the break is 4 minutes; consider 5 for Level 2 (D17).


## 10. Decisions the owner must make (defaults I chose are marked [Default])

None is irreversible. Changing a default after the build costs time, as noted.

- **D1. Holiday overlap policy.** [Default] A term lesson may use the same question type as a holiday lesson (the papers set them) but never the same numbers, context or structure, and each shared type needs one new twist; the plan's Lesson 1 digit-sum item is replaced by a riddle and the plan's Lesson 7 counting grids by dissection and tilted squares. Alternative: remove all contest-type overlap and leave those slots to new types. Changing after the build means rewriting Think harder and Go further of the 17 High-overlap lessons (section 2).
- **D2. Money scope.** [Default] $3.05 and 305¢ both from Lesson 5 (P2 syllabus); totals computed by converting to cents; decimal addition ($2.40 + $1.35) only at Go further (P3, p. 35). Alternative: teach decimal addition at Think harder because the papers do it (story prices are whole dollars or whole cents in the papers read).
- **D3. Time to the minute and start-from-end.** [Default] The plan's Start here (5 minutes) becomes "to the minute" on a clock with all 60 ticks; durations and start-from-end at Think harder; "past midnight" at Go further. This re-levels a plan item that the P2 papers justify (nine papers from 2018 test start-from-end).
- **D4. Fractions.** [Default] Stacked fractions on every page (M2), denominators to 12, hatch not colour, no equivalence; fraction of an amount only in Lesson 33 Go further.
- **D5. Cryptarithms.** [Default] Keep letter sums in Lessons 2 and 20 and 40 (owner decision 7 left Level 4 without them; the plan keeps them at Level 2). The only brute-force-unique forms I found are "AA + BB = CAC" and "AB + AC = BCA".
- **D6. Reading order of multiplication.** [Default] As Level 1: "3 groups of 4" is 3 x 4, either order accepted.
- **D7. Hints in stems.** [Default] "(Hint: Make a table.)" at Think harder only, matching the papers; Go further asks the child to choose.
- **D8. Lessons without paper evidence (30, 31, 36, 38, 39).** [Default] Keep as the plan has them, marked "safest to skip", Beyond MOE named in the tutor guide. Alternative: replace Lessons 36 and 38 with the plan's open-question alternatives (routes and points; fractions of an amount of money).
- **D9. Tables 6 to 9 (Lesson 32).** [Default] Keep as a labelled P3 preview, with the 6s from the 5s and 1 more group; the papers read test only 2, 3, 4, 5, 10.
- **D10. Four-digit numbers (Lesson 34).** [Default] Keep as a preview (Go further), with the 4-digit card items.
- **D11. Books and payments.** [Default] Both 5-lesson books of a term come with the first payment (including the first instalment); a mid-term joiner receives the books for the lessons still to come; hand-off lines say "your book". Alternative: post each book separately (adds the 5-to-6 and 15-to-16 failure cases of section 5).
- **D12. Paper and print.** [Default] Print the play money (Lesson 5), the arrow cards (Lesson 1) and the heavy kit pages on the same paper; recommend thicker paper in the kit note. Alternative: card stock for Lessons 1 and 5 and the fraction strips.
- **D13. Blocks for Lessons 25 and 39.** [Default] 14 same-size blocks as home materials with a drawn-stack fallback. If the owner prefers, make cubes Explore-only.
- **D14. Ruler.** [Default] Level 2 assumes a cm ruler (a P1 outcome); the Quest gate and Lesson 8 say "no ruler? tell your tutor". Alternative: a printed ruler on the kit page (Level 1 D decision was no).
- **D15. Play money pictures.** [Default] Stylised play money as in Level 1 (rounded squares for coins, rectangles for notes, PLAY MONEY printed, not facsimile). The legal check of reproducing notes and coins is still open (nobody has checked).
- **D16. Quest slot.** [Default] Minutes 35 to 55 after the brain break in Lessons 10, 20, 30, 40, as in Level 1 (the owner left placement to the assistant).
- **D17. Break length.** [Default] 4 minutes as in Level 1. Alternative: 5 minutes for Level 2 with 1 minute taken from Flex.
- **D18. Names for wrong working.** [Default] "A child" or "a child in another class"; the error-spotter role never goes to a cast name.
- **D19. Cold-join trial.** [Default] Test Lesson 5 and Lesson 21 with one child who has done only the holiday course, and Lesson 1 with one school-only child, before launch.
- **D20. Child-visible puzzle names.** [Default] The named beyond puzzles (Halfway Numbers, Quarter the L, Tilted Squares, Circle of Posts, Odd Staircase, The 495 Trick, Past Midnight, I Know My Hat and so on) are shown to children as puzzle titles, never as "beyond" or "challenge". Alternative: tutor-only names.
- **D21. Papers.** [Default] Write with the P2 paper patterns. Please supply the 2019 and 2021 P2 zips as individual files (each under 10 MB) so the missing patterns can be read.
- **D22. Mi poses.** [Default] Use the current poses in the same places as Level 1; the owner supplies more poses later (decision of 23 Oct).
- **D23. Who builds and when.** [Default] After Level 1 Term 4 passes its fix pass (the shared tools settle), build M1 and the tool items, then Term 1 first (holiday graduates start there), then Terms 2, 3 and 4 as in section 11. Changing the order costs rework of figures only.
- **D24. Term price and start dates.** Not decided in `owner_decisions.md` (the website still shows S$65 a lesson); nothing in Level 2 depends on it except the payment note and prorating.
- **D25. Level 2 books on the website shop.** Not part of this document; the extension workbook (Level 2) is a separate product built from the holiday question types and must not reuse term items (section 13).


## 11. Build order, effort and cost estimate

### 11.1 Dependencies in the content

- Place-value chain 1, 2, 13, 34 (one kit, one figure); fractions 6, 22, 33 (one figure, one renderer, one kit); bars 9, 14, 27, 28, 38; time 15 and 35 (one kit); money 5 and 28 (one kit); sequences 4 and 21; solids and views 25 and 39; the Quest in Lesson 10 needs 1 to 9 fixed, Lesson 20 needs 11 to 19, Lesson 30 needs 21 to 29, Lesson 40 needs 31 to 39.
- Lesson 28 uses the words of Lessons 9, 14 and 27 ("find one first", "strip", "table"); Lesson 38 uses Lesson 20's "exactly one answer" and Lesson 37's check. Wording must match the fixed wording of the earlier lesson.
- The plan says a lesson must not assume the previous one except through Remember, so the chains are a build-order and wording-consistency dependency, not a content one.

### 11.2 Waves

**Sprint A (day 0, one engineer, about a day):** M1 Level parametrisation, M15 validator (Level 2 lists, holiday-copy check, `nonroutine`), M21 authoring brief, M2 fraction and decimal text renderer, M14 runner formatters, M4 `place_value`, M5 `column_sum`, kit KA. Then write **Lesson 1** (pilot for Level 2 conventions: first place-value figure, first term parameters, first words-as-choice item).
**Sprint B (in parallel with Lesson 1, two engineers):** M3 `fraction`, M6 `balance`, M7 `scale_dial` and `jug`, M13, M18 hatch patterns, kits KD and KE.
**Wave A (existing tools after M1; start on day 0):** Lessons 3, 4, 9, 12, 14, 15, 16, 17, 19, 21, 27, 28, 29, 32, 35, 36, 38 (17 lessons). Of these, 3 and 14 are the best pilots for the discipline (division, bars).
**Wave B (after Sprint A and B):** Lessons 1, 2, 5, 6, 13, 22, 33, 34, 37.
**Wave C (after the figure batches):** Lessons 7, 8, 11, 18, 23, 24, 25, 26, 31, 39 (M9, M10, M12, M8, M11 come in this sprint).
**Wave D:** the Quest blocks of 10, 20, 30, 40, written after the term's other nine lessons have passed their fix pass (M17).
**Audit and fix per term**, then a term-wide second-round audit (guide and deck, home and parent and practice, term-wide) as for Level 1, then **one 40-lesson consistency sweep** (rewind items, hand-offs, the beyond table, the holiday-overlap register, books).

Which can be written first with the existing tools: Lessons 3, 4, 9, 12, 14, 15, 16, 17, 19, 21, 27, 28, 29, 32, 35, 36 and 38 need no new figure (Lesson 15 needs only the Level 2 time fields; Lesson 4 needs the hatch patterns of M18 and, for its Go further only, the chart offset of M13). The ones that cannot start without a new figure: 1 (M4), 2 and 20 and 37 (M5), 6 and 22 and 33 (M2, M3), 8 and 23 (M6), 24 (M7), 25 and 39 (M8).

**Suggested term order:** Term 1 first (holiday graduates and new joiners start there, and it has the most new figures), but do not wait for all of Term 1 before starting Wave A of Terms 2 to 4; the Term 2 and Term 4 lessons with no new figure can run in parallel with Term 1 template work.

### 11.3 Effort (agent-hours, not measured)

Per-lesson figures include write (data, checks, build, view every page), wording review, independent audit and fix pass. Level 1 evidence for scale: Term 2 was about 6.5 hours of wall clock from pre-flight to the end of the first fix pass with parallel agents and template foundations first; the Level 1 Terms 3 and 4 estimate was 172 hours for 20 lessons.

| L | Title | Write and build | Wording | Audit | Fix | Total | Why |
|---|---|---|---|---|---|---|---|
| 1 | Where Does It Live? | 4.5 | 0.6 | 1.0 | 1.3 | 7.4 | place-value figure, words |
| 2 | Mind Maths Moves | 4.0 | 0.6 | 1.0 | 1.3 | 6.9 | column letter sums, new figure M5 |
| 3 | Share It or Group It? | 4.0 | 0.7 | 1.0 | 1.3 | 7.0 | division wording, sharer counted |
| 4 | Chart Patterns | 3.5 | 0.5 | 1.0 | 1.0 | 6.0 | existing figures |
| 5 | Shop Bills and Change | 5.0 | 0.7 | 1.2 | 1.6 | 8.5 | decimal money, 32-piece kit, scope of P2 versus P3 |
| 6 | Cut It Equally | 5.5 | 0.7 | 1.2 | 1.6 | 9.0 | first fraction figure and notation |
| 7 | Shape Splitters | 4.0 | 0.5 | 1.0 | 1.3 | 6.8 | dissection kit, tilted-square check |
| 8 | Read the Scale | 4.5 | 0.6 | 1.0 | 1.3 | 7.4 | scale and balance figures |
| 9 | Story Detectives | 4.0 | 0.7 | 1.0 | 1.3 | 7.0 | reading traps, BACK items |
| 10 | Posts, Gaps and Queues | 3.5 + 4.0 Quest | 0.5 | 1.5 | 1.8 | 11.3 | Quest, short lesson body |
| | **Term 1** | | | | | **77.3** | |
| 11 | Graphs That Talk | 4.0 | 0.6 | 1.0 | 1.3 | 6.9 | tally cells, keys 3 and 4 |
| 12 | Odd, Even, Fair | 3.5 | 0.6 | 1.0 | 1.0 | 6.1 | light |
| 13 | Jumps, Gaps and Columns | 4.0 | 0.6 | 1.0 | 1.3 | 6.9 | column figure, 495 check over 900 numbers |
| 14 | Bar Model Stories | 4.5 | 0.7 | 1.0 | 1.3 | 7.5 | bar model tier risk |
| 15 | Clock Detectives | 5.0 | 0.7 | 1.2 | 1.5 | 8.4 | clock to the minute, timelines |
| 16 | Table Tricks | 3.5 | 0.5 | 1.0 | 1.0 | 6.0 | existing figures |
| 17 | Find All the Ways | 3.5 | 0.6 | 1.0 | 1.0 | 6.1 | worst-case wording |
| 18 | Who Is Who? | 4.5 | 0.6 | 1.0 | 1.3 | 7.4 | ring figure, uniqueness proofs |
| 19 | Track It | 4.0 | 0.6 | 1.0 | 1.3 | 6.9 | tracking, hats puzzle |
| 20 | Puzzle Lab 2 | 3.5 + 4.0 Quest | 0.7 | 1.5 | 1.8 | 11.5 | Quest plus mixed spiral |
| | **Term 2** | | | | | **73.7** | |
| 21 | Gaps That Grow | 4.0 | 0.6 | 1.0 | 1.3 | 6.9 | stick strips, sequences |
| 22 | Fractions on the Line | 5.0 | 0.7 | 1.0 | 1.3 | 8.0 | 0-to-1 line with fractions |
| 23 | Shape Equations | 4.5 | 0.7 | 1.0 | 1.3 | 7.5 | balance figure, three-scale proof |
| 24 | Estimate Like a Scientist | 3.5 | 0.5 | 1.0 | 1.0 | 6.0 | light |
| 25 | Spot the Solid | 5.0 | 0.6 | 1.2 | 1.5 | 8.3 | solid and view figures |
| 26 | Tiles, Turns and Symmetry | 4.0 | 0.6 | 1.0 | 1.3 | 6.9 | pattern row, mirror |
| 27 | Two-Step Bar Models | 3.5 | 0.6 | 1.0 | 1.0 | 6.1 | reuse bars |
| 28 | Longer Chains | 4.0 | 0.7 | 1.0 | 1.3 | 7.0 | five-link chains |
| 29 | Always, Sometimes, Never | 3.5 | 0.6 | 1.0 | 1.0 | 6.1 | claim wording |
| 30 | Robot Recipes | 4.0 + 4.0 Quest | 0.6 | 1.5 | 1.8 | 11.9 | Quest plus robot |
| | **Term 3** | | | | | **74.7** | |
| 31 | Chance and Fair Games | 4.0 | 0.6 | 1.0 | 1.3 | 6.9 | spinner figure |
| 32 | Tables Bridge | 3.5 | 0.5 | 1.0 | 1.0 | 6.0 | light |
| 33 | Halves and Quarters of Things | 4.5 | 0.7 | 1.0 | 1.3 | 7.5 | fraction of a set |
| 34 | Big Numbers Expedition | 4.0 | 0.6 | 1.0 | 1.3 | 6.9 | place-value figure to 4 digits |
| 35 | Calendar and Timetable Puzzles | 4.0 | 0.6 | 1.0 | 1.3 | 6.9 | calendar and timetable |
| 36 | Grid Treasure Hunt | 3.5 | 0.5 | 1.0 | 1.0 | 6.0 | existing grid |
| 37 | Spot the Mistake | 4.0 | 0.6 | 1.0 | 1.3 | 6.9 | column figure, nine check proof |
| 38 | Problem Posers | 3.5 | 0.6 | 1.0 | 1.0 | 6.1 | posing |
| 39 | Look Again | 5.0 | 0.7 | 1.2 | 1.5 | 8.4 | nets, matchsticks, mirrors |
| 40 | Year Challenge Day | 3.5 + 4.5 Quest | 0.7 | 1.5 | 1.8 | 12.0 | Year Quest and showcase |
| | **Term 4** | | | | | **73.6** | |
| | **Year** | | | | | **299.3** | plus about 30 for four term-wide second-round audits (4 each), the holiday-overlap pass (6) and the 40-lesson consistency sweep (8): about **330** |

Template engineering (section 3): **125 hours** if everything is built, about **109** with the deferrals. Not in these numbers: the tutor trials (one per term and a cold-joiner trial), the legal check on play money (D15), the owner's re-supply of the 2019 and 2021 papers (D21), and the Level 1 Term 4 tool changes that Level 2 must absorb.

**Cost to the owner in practical terms.** About 330 plus 109 to 125, so 440 to 455 agent-hours. At the Level 1 pace (eight to ten writing agents and three engineers in parallel) that is about 8 to 10 working days from the start of Sprint A to four audited terms, of which about 1.5 days is template engineering before the first Wave B lesson can be built. If template work is done serially before any lesson starts, add about 1.5 days. Printing is unchanged in kind from Level 1: eight 5-lesson books of about 36 to 40 pages, four Quest Logs, and 48 to 81 pieces a term for a grown-up to cut.

**Page budget per book (estimate from the Level 1 pattern):** 5 lessons x 5 pages, plus 1 to 3 kit pages per lesson that has a kit, a cover, contents, a blank pad so each lesson starts on a right-hand page, and a Quest Log of 3 pages in Books 2, 4, 6 and 8: about 36 to 42 pages. `term_books_spec.json` gives the true counts after a build.

## 12. What was not checked

- No lesson, tool or output file was run, built or validated; the tool inventory was read from the working tree, which holds uncommitted Level 1 edits by other agents (`figs2.py`, `figs3.py`, `b_*.py`, `validate.py`), so a Level 1 Term 4 change may already have added some Level 2 figure.
- Hours are estimates from the Level 1 documents and commit times, not measurements.
- MOE placements come from `docs/moe/syllabus_by_level.md` (P2 pp. 33 to 34), not re-read against the PDF; the plan itself says the new Term 1 lessons were not re-read page by page (plan, "Not yet re-checked"). Whether "1 m = 100 cm", comparing unlike fractions as a beyond item, and the order of school topics are inside P2 or P3 needs the owner's or a tutor's check.
- The 2019 and 2021 P2 paper zips were not opened by the paper analysis; the four rendered scans were read at about 45 dpi; school mark schemes were not seen.
- The holiday overlap was found from the holiday question banks (`qbank`) and lesson objectives in `p2/content/l1.js` to `l10.js`, not from the holiday slides, scripts or workbook pages one by one; section 13 is the register to confirm against those pages in the first audit.
- Items marked "verified" were recomputed by brute-force scripts (not committed): midpoints, riddles, cards, arithmetic series sums, letter sums, the 7-coin count, three-top sets, tilings and partitions, tilted-square counts, Kaprekar steps, worst case, number rings, hats, sequences, scales, views, mirror clocks, matchsticks, nets, routes, nine-check detection. Figures that depend on a font (the mirror-letter sets) are listed as definitions, not as facts about the world.
- Wording of Lessons 30, 31, 36, 38 and 39 is unverified against any school paper (no evidence exists).
- Singapore rules on reproducing banknotes and coins in play money were not checked.
- No child was observed; no timing was measured (the Level 1 trial has not reported yet).

## 13. Holiday overlap register (and non-routine check)

Source: the 237 question-bank items (60 core, 87 stretch, 90 challenge) in `p2/content/l1.js` to `l10.js`, plus each lesson's objective. "Do not reuse" lists the numbers, contexts and structures to avoid; "Verdict" is **Change** (the plan's item collides with a holiday item and is replaced here), **Second visit** (same type allowed with new numbers and one new twist) or **New** (no holiday counterpart).

| L | Holiday lesson touched | Do not reuse | Verdict |
|---|---|---|---|
| 1 | 1 Digit Detectives | Digit sums 4, 5, 6 and the odd all-different sum 6; the digit 3 in 300 to 399; pages 1 to 120; cards 3,6,1 / 2,6,9 / 4,4,7 / 5,1,9 / 2,5,9 / 0,3,8 / 1,3,5,7; 46 ten-blocks; the numbers 700 to 790; 495 and 505 on a 1000 chart; 538, 914, 409 and 490 | Change (digit sums, digit 3); Second visit (cards, regrouping with ones added) |
| 2 | 2 Missing Digit Mysteries | Compensation 299 + 101, 346 + 199, 270 + 130; magic triangle with 110 to 160; magic square 20 to 180; digit-card 531 and 47; 507 + 493 pairs to 1000; Mei 523 - 267 | Second visit (EQ in subtraction form); New (pairing, letter sums) |
| 3 | 3 Legs, Wheels and Arrays | Bicycles and tricycles (17 wheels); hens and goats (25, 26 legs; 22 legs); boats of 4 for 27; cupcake boxes 24; 34 marbles among 4; tables and stools 17 legs; 21 to 49 in two tables; Mr Lim 20 to 30 sweets; "every number 4 to 30 makes an array" | Second visit (division wording, leftovers); New (sharer counted, true or false, "most friends") |
| 4 | 4 Pattern Machines | Beads red-red-blue-green; houses 5, 9, 13 sticks; 2, 7, 8, 13, 14 alternating; frog 1, 5, 9; frogs A and B; towers 2, 5, 8; counting in 3s and 4s (12, 24); 5-shape star pattern 13, 23, 30, 48 | Second visit (two counts: use 5 and 4); New (2 by 2 and 3 by 3 move grids) |
| 5 | 6 Market Day; 5 Machines | 275¢ = $2.75; 65¢ fewest coins; $17 fewest notes; ways to pay $10 ($5, $2, $1); ways to pay 40¢ and 90¢; 4 coins $1.25; 5 coins $1.60; pen and pencil $11 and $3 more; half-of-money backwards; Mei $1 at the snack stall; 15 amounts from four notes | Second visit (change, enough money); New (the receipt, two-notation habit, best buy) |
| 6 | 7 Fair Shares | Bottoms to 12; 1/3 vs 1/6; 3/10 + 4/10; 3/8 vs 3/5; Siti 3/8 + 2/8; Ali pizza halves; 3 squares cut into 4 equal parts; two fractions with bottom 9 making 1; three children sharing 10 pieces (1,2,7; 1,3,6; 1,4,5; 2,3,5); folding a strip three times; 1/5 and 1/6 between 1/4 and 1/7 | Change (three-that-make-1 uses denominator 8, then 12 in Lesson 22); New (equal parts in any shape, parts to shade, Quarter the L) |
| 7 | 8 Shape Builders | Squares in 2 by 2, 4 by 3, 5 by 5 grids (5, 20, 55); rectangles in 2 by 2 and 3 in a row (9, 6); triangles in a diagonal square (8); 3-line triangle (20); half circles and quarter circles; cube stacks 19, 16, 8, 20, 30; 3 x 3 x 3 painted; nets E and F; six in a line | Change (counting grids are a second visit on new figures only); New (dissection, tilted squares) |
| 8 | 9 Measure Masters | Apple, lemon and pomelo balances; cube and ball scales; basket 700 g and 500 g; box 1000 g with 4 books; ribbons with overlaps (86 cm); 90 cm ribbon; jugs 2 and 7 (3 l, 5 l); bucket of 10 l | New (reading a scale, ticks, a ruler not from 0); Second visit (balance, with different objects) |
| 9 | 5 Machines; 2 Missing Digits | At first / gave away: 41 stickers; $36 Ben; 36 beads; bus with 35; Ali, Ben, Siti 40 marbles (9, 14, 17); 42 stickers (10, 12, 20); eggs 905; "add 199 take away 99" | Second visit (BACK with new structure); New (reversal "58 more than", hidden first step) |
| 10 | 9 Measure Masters; 10 Puzzle Day | Rope 40 cm in 10 cm pieces (6 min); rope 30 m in 5 m pieces (6 pieces, 5 cuts); three ribbons with overlaps | Second visit (cuts and pieces); New (posts, queue positions, corners, circular track) |
| 11 | 10 Puzzle Day | Keys of 2, 5 and 10; mango row from a total of 30 (5 children each); lost key (football 6, swimming 4, 10 more: 30 and 20); each picture 2 children | Second visit (keys 2, 5, 10); New (keys 3 and 4, tally, from clues) |
| 12 | (none) |  | New |
| 13 | 2 Missing Digit Mysteries | 3[ ]5 + 214 = 579; 6[ ]8 - 205 = 433; [ ] - 150 = 600; 5[ ] + [ ]7 + 38 = 132; Mei 523 - 267 = 266 and the adding-back check; [ ][ ]7 + 4[ ][ ] = 1000 (10 ways) | Second visit (missing digit with new numbers); New (jumps, the 495 trick) |
| 14 | 5 Machines; 6 Market Day; 7 Fair Shares | Before-and-after bars; three children with extras (40 marbles; 42 stickers); pen and pencil $11, $3 more; $15 present with $2 steps (3, 5, 7); cake 12 slices Mei Ali Ben; Ali 150 Ben 100 Box C 250 (sum of pairs) | Second visit (bar as a general tool); New (transfers with a picture, half the gap) |
| 15 | 9 Measure Masters | Cartoon 5:40 pm + 30 min; lunch 12:30 pm; minute hand on 7; 10:45 am to 12:10 pm; piano lesson ends 4:15 pm lasted 45 min; film 1 h 40 ends 12:20 pm; buses every 15 min; tap 5 l every 10 min; 3 lessons of 35 min with 10 min breaks from 8:15; clock 10 minutes fast; watch loses 5 minutes an hour | Second visit (start-from-end with a timeline); New (to the minute, conversions, past midnight) |
| 16 | 3 and 4 | Counting in 4s; fingers on 6 hands; 5 groups of 4; numbers in the 3 and 4 tables | Second visit; New (ratio table, doubling, true or false) |
| 17 | 1, 3, 6 | Ways to pay $10, 40¢, 90¢; hens and goats; digit-card lists | New (outfits, worst case); Second visit (ways to pay: use $2 and $5) |
| 18 | 10 Puzzle Day | 3 by 3 logic grid (colours), 4-person grid (school transport), height chain, coin order puzzle | Second visit (4 by 4 grid with new clues); New (weight order, number ring) |
| 19 | 5 Machines | Ben gives Ali 5 marbles (20 each; Ben 25, Ali 15); three boxes of 30 pens (A 15, B 8, C 7) | New (three transfers, hats) |
| 20 | 2 Missing Digit Mysteries; 10 Puzzle Day | Magic triangle with 110 to 160; magic square; "make up your own" puzzle in every challenge section | Second visit by design (the plan); New (letter sum with one carry, uniqueness proof) |
| 21 | 4 Pattern Machines; 10 Puzzle Day | Sticks 5, 9, 13; towers; 5, 9, 13, 17 pattern (49 and 50); Mei and Ali savings with a growing rise | Second visit; New (falling gaps, add the last two, triangle numbers) |
| 22 | 7 Fair Shares | As Lesson 6; 1/3, 1/12, 1/2, 1/5 in order; Ravi 3/8 and Ben 2/8 | Second visit; New (the 0-to-1 line, closer to half) |
| 23 | 9 Measure Masters; 5 Machines | Apples, lemons and pomelo exchange chain; cube and ball scales; "x2 then -3" machines | Change (the exchange chain is the holiday item; use pots and cups); New (picture equations, Three Scales) |
| 24 | 9 Measure Masters | Box of 4 books 1000 g; basket of apples; jugs | New |
| 25 | 8 Shape Builders | Stacks 19, 16, 8, 20; pyramid 30; painted cubes; solids (cylinder) | Second visit (names); New (views, Most and Fewest) |
| 26 | (none) |  | New |
| 27 | 5, 6, 7 (bars) | As Lesson 14 | Second visit; New (ages) |
| 28 | 6 Market Day; 10 Puzzle Day | Hawker centre chicken rice $4 and noodles $3 (7 dishes, $25) | Second visit; New (five-link chain) |
| 29 | 1 and 3 | Mei swap claim; Ali every number makes an array; Mei hens-and-goats 9 legs | New |
| 30 | (none) |  | New |
| 31 | (none) |  | New |
| 32 | 3 and 4 | Tables 2, 3, 4, 5, 10 only | New (tables 6 to 9 are P3) |
| 33 | 7 Fair Shares | Pizza halves; cake 12 slices; Siti eats half then Ravi half of the rest (1/4); strip folded three times | Second visit; New (part of a pile, half then a third) |
| 34 | 1 Digit Detectives | All the card items of Lesson 1; 1000 chart | Second visit; New (4-digit numbers, arrow cards) |
| 35 | 9 Measure Masters | Buses every 15 minutes; savings per day (Mei $3 a day, Ali $10) | Second visit; New (weekday cycle, same date next year) |
| 36 | (none) |  | New |
| 37 | 2 Missing Digit Mysteries | Mei 523 - 267 = 266 and the check by adding back | Second visit; New (nine check) |
| 38 | (none; "make up your own" in every holiday challenge) |  | New (Puzzle Doctor) |
| 39 | 8 Shape Builders | Nets E and F; six in a line cannot fold | Second visit (nets); New (mirror clocks, matchsticks, shadows) |
| 40 | 10 Puzzle Day | Mixed puzzle day: graphs, logic grids, hens and cows, chicken rice | Second visit by design; New (Showcase Puzzle) |

**Count.** Verdict "Change": Lessons 1, 6, 7 and 23 (4 lessons where the plan's own item collides). "Second visit": 26 lessons (2, 3, 4, 5, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 20, 21, 22, 25, 27, 28, 33, 34, 35, 37, 39, 40). "New": 10 lessons (12, 19, 24, 26, 29, 30, 31, 32, 36, 38). The plan's section "Non-routine assignments" is not reduced by this register: every type and tier in it is kept; only the instance changes.

**Rule for the extension workbook (owner decision 23 Oct).** The Level 2 extension workbook is built from the holiday question types and extends the holiday program. It must not reuse term-lesson items either: the holiday-copy check (M15) should also run against `term/l2/lessons` when the workbook is written.

**Non-routine check added to every audit.** (a) Every lesson 1 to 40 names at least one catalogue type in `contest_moves` and in the `nonroutine` field with its tier. (b) No non-routine item sits at Start here. (c) No sentence overlaps a school or contest question by 7 words and no holiday question by 5 words. (d) Items needing a picture (290 of the 556 school items depend on one) have the picture in the workbook. (e) Every "exactly one answer" or "exactly N ways" claim is brute-forced in `verify/lNN_checks.py`. (f) The four types the papers use most (CTX 107, CMP 97, BACK 74, MULTI 58) are not dropped when time is short; the first cuts are the Go further parts of Lessons 30, 31, 36 and 38.
