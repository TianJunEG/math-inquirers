# Independent audit, round 3: Level 5 Extension Workbook

Audited 23 Oct 2026 by a third model in a fresh session. Report only: nothing in the book, data, builders or tools was edited, nothing was pushed, no PR. The only file written is this one.

Checked: `outputs/extension/L5/` print (100 pp, 1-bit), print vector (100 pp), soft copy (99 pp), `build_report.json` (0 problems); `extension/data/l5_u01..u10.json` diffed against commit 6494ed0 (the data audited in round 2) to HEAD 4587e5d; holiday text `p5/content/l1..l10.js`; `README.md`, `PROGRESS.md`, `AUDIT_ROUND2.md`.

## Method

- **Diff.** Item by item (text, parts, answer, hint, Why, figure, Learn) between 6494ed0 and HEAD: **32 items and 2 Learn pages changed** (34 entries, listed in the table). Everything else is unchanged from round 2.
- **Hand solving (from the page text, not the key).** Every changed item solved by hand from the question as printed on the page, then compared with the key and the Why. Brute force of my own for the riddles U1 S12 and T01 (unique: 472 630 and 6 435 708), U10 S12 (45), U10 S06 (all three boxes tried), U10 S03 (orders), U9 G03, U9 S05, U5 G03 (side 5 only), U3 T02. `run_checks.py --level 5`: 416 answers, OK.
- **Answer pages, all of them.** All 244 entries (Try plus numbered items) on pp. 80-99 parsed from the vector PDF and compared in order with the data: Why text equals the explanation of the item in that position for **244 of 244**; the printed "page N" equals the page where the question is for all 244 (the 16 that a text search could not place by a short snippet were checked by page text or image: repeated stems or figure-only items); question numbers on the pages agree (the 8 mismatches the number scan raised are digit cards or number lines on the page, not wrong numbers). Every changed item's Why was also read against its question.
- **Frames.** Each changed item compared with the holiday P5 content (practice, stretch, challenge, workbook, exit tickets, slide narrative and answers) by search on key nouns and numbers plus a similarity scan. "Too close" below means: same story, or same question frame, or a shared key number or answer, with the owner policy (new story AND new frame; "same skills, new numbers" only where README says so).
- **Pages.** All 100 print pages rendered at 100 dpi; changed pages viewed (pp. 9, 10, 15, 18, 22, 24, 27-30, 33, 37, 39, 44, 45, 51-53, 55, 57, 60, 61, 62, 64, 67, 70-72) plus 1-5, 77; 300 dpi crops of the 1-bit file at the changed figures (pp. 28, 33, 55, 57, 60, 61, 64) and p. 56.
- **Not done:** no child trial, no printer proof, no real print, soft copy compared as text only.

## Verdict

**Close, but not sell-ready until about 8 items get a new frame (a few hours of data edits plus a rebuild). Mathematically and structurally the book is ready.**

What is good: 0 wrong keys, 0 unsolvable or ambiguous new items; every Why, answer and page reference on all answer pages matches its question (244 of 244); contents, answer page numbers, pace plan, Welcome, cover, plaque, Beyond badges (14), blank pages and print/soft parity are right; the figure fixes asked for in round 2 are done (U8 S06 rhombus, U8 G03 ticks, U8 Learn Try label, U4 S01 and C01 labels) and the Learn additions (U9 worked supposition example, U8 rhombus) are present.

What blocks "new story and new frame" (owner policy): the round-2 fixes closed R1 to R3 but several R4 rewrites moved to a frame that is the holiday's again, one (U7 T03) was made worse, one (U8 C01) now shares the holiday's answer, and two older items that round 2 passed (U4 S01(b) and U4 S06) are the holiday's own teaching numbers. README line 50 ("every item that shared a key number ... was replaced") is still not true. See "Must fix" below. After those, I would sell on "same skills, new numbers" for the rest.

## Per-item table (all 34 changed entries)

Key: maths = hand solved from the page, agrees with key and Why. Frame = against holiday P5.

| Item | Change | Maths / key / Why | Frame vs holiday | Status |
|---|---|---|---|---|
| U1 S12 | Why only | 472 630 right (brute force); Why now lists (1,2), (2,4) repeat the 2 and (4,8) repeats the 4; (3,6) works | new riddle | **Fixed** (round-2 R7) |
| U1 T01 | Why only | 6 435 708 right (unique); Why has no letter variable now | new riddle | **Fixed** |
| U2 S06 | new frame: 3/8 and 1/6 of the 72 cards | 72 - 27 - 12 = 33 right | holiday has "1/3 then 1/2 of remainder, 60 marbles"; this is both fractions of the whole, new story | **Fixed** |
| U2 G04 | now labelled Beyond | telescoping sum = 1/2 ... key unchanged, correct | holiday hint idea is "1/6 = 1/2 - 1/3" telescoping; label is honest now | OK (README Beyond table still lists U2 G1 only, Low) |
| U3 S06 | R1: counters, 3/4 white of 20, 10 white taken out | 15 W 5 B; black 5; 5/10 = 1/2 right | numbers new; skeleton (which colour did not change, fraction before/after) is still the holiday item's; holiday stretch also has "red/blue pens, 2/3 to 1/2, blue taken out" | **Fixed** (Low: same skeleton) |
| U3 T01 | new frame: rice shop, 3/8 + 1/4 of all, 120 kg left | 5/8 sold, 3/8 = 120, 320 kg right | different from "1/4 then 2/5 of remainder, $66" | **Fixed** |
| U3 T02 | Ben 2/3 of Ali, Ali loses 12, Ben wins 8, level | u = 20, Ali 60 right (brute force 60) | holiday: "Ali 3/5 of Ben, Ben gives 20, same number"; also marbles in l3 warm-ups. Different mechanism, same "fraction then equal" frame | Low |
| U4 S01 | figure redrawn: (a) 12 base, 10 slants, height 8 | (a) 48, (b) 84 right; 6-8-10 fits | **(b) is the holiday's figure exactly** (13, 14, 15, height 12, area 84; l4.js lines 33, 87, 150). (a) is new | **Too close** (M1) |
| U4 S06 | (b) now "rectangle is 2 times the triangle" | 63 and 2 right; both parts now differ | **rectangle 14 by 9 and 63 cm2 is the holiday's worked example** (l4.js line 100). (b) is new | **Too close** (M1) |
| U4 S09 | R3: triangle 15 by 8, rectangle 5 wide | 60 and 12 right | holiday: "triangle and square same area" (l4.js 137) and "P base 8 height 5, Q base 4 same area" (139). Different shapes and numbers, same idea | Low-Med (S1) |
| U4 C01 | right-angle mark smaller, "6 cm" moved | 48 right; figure clean at 300 dpi except "6 cm" sits on the right slant (line has a halo gap) | n/a | **Fixed**; Low: answer 48 equals S01(a) and both are isosceles with slants 10 (S2) |
| U4 C02 | area 49, base twice the height, find the base | h x h = 49, h 7, base 14 right | holiday exit/stretch: "area 45 (42), base 10 (12), find height". Twist added (needs a square), same bare-triangle story; 49 is also the holiday l7 warm-up square | Low-Med (S1) |
| U4 C03 | Why uses only the 4 cm shown | 72 right | n/a | **Fixed** in text; Low: the dashed height is lost in the hatching at 1-bit, the "4 cm" at the apex reads as a label of the point (S3) |
| U5 S13 | two tanks, same water, A 3/5, B 3/4 of 40 | 30 litres, capacity 50 right | holiday tank-capacity items are "added water, 1/3 to 3/5" and "3/4 to 1/2"; this is a different frame, same tank story | **Fixed** |
| U5 G03 | cuboid, square base, height side + 4, V = 225 | side 5 only (checked) | **holiday l5.js 145: "cuboid has a square base and a height of 5 cm, volume 245, side of the base"**: same story and question, twist added | **Too close** (M2) |
| U6 S13 | savings: Ali $60 +$5, Ben $20 +$10, same after how many weeks | 8 weeks, $100 each right | new story; frame is the holiday candle item ("gap closes by x each hour", l6.js 133) and the Why uses the same words | Low |
| U6 T02 | hint only | 12 right (unchanged) | hint now "Try a pool size that suits both hoses" (still a strong hint) | OK |
| U6 T03 | machines and bolts; machines needed for 900 in 3 min | 20 a minute, 300 a minute, 15 right | **holiday l6.js 116: "3 machines make 360 masks in 4 minutes ... 5 machines"**: same story and rate-table frame, question reversed. The round-2 fix moved from workers and boxes to machines, i.e. closer | **Too close** (M3) |
| U7 S13 | pages: 30% of 240, then 25% of the rest | 126 pages right | holiday "$200, 40% shoes, 50% of rest bag" and "Mrs Tan 40% then 25% of remainder": new story, same frame | Low-Med (S1) |
| U7 T02 | plant grows 20%, now 72 cm | 120% = 72, 60 cm right | holiday has the shirt discount and the 20% up-down score; this is a different story and direction | **Fixed** |
| U7 T03 | back to 9% GST, $545 | 545/1.09 = 500, GST $45 right | **holiday l7.js 116: "price tag $109, GST included, GST 9% ... how much GST is in the price"**: same question, same method (109%, 1% = whole dollars). Made worse by this fix | **Too close** (M4) |
| U7 G01 | park visitors 50 to 40 and back | 20% and 25% right | **holiday chicken rice $4 to $5 and back (l7.js 100): same trap, same two answers 25% and 20%** | **Too close** (M4) |
| U7 G02 | bus: 40% children, 50% of children and 20% of adults have a seat | 20 and 30; 10 + 6 = 16; 32% right | **holiday l7.js 114: school with 800 pupils, 45% boys, 20% of boys and 30% of girls take the school bus; what percentage**: same frame, a bus again | **Too close** (M4) |
| U8 Learn | "Rhombus: a parallelogram with 4 equal sides" added; Try label moved | Try 72 right; figure clean at 300 dpi (54 and ? separate) | n/a | **Partly done**: equilateral and a clearer trapezium line still missing (S4) |
| U8 S06 | asks BCD (b); label (b) moved to C | (a) 52, (b) 76 right; angle A in the figure measures 76 | holiday has a rhombus PQRS with diagonal PR (l8.js 68): same skill, new numbers | **Fixed** (figure clean) |
| U8 G03 | ticks on DB and AC removed | 36 right; the figure measures A = 36; AB = AC is stated in the text | n/a | **Fixed** (no false equality) |
| U8 C01 | straight line AOB, AOC is 3 times COB | 45 right; figure measures 45 | **holiday l8.js 179: "parallelogram ABCD, angle A is 3 times angle B ... 4 equal parts of 45"**: same "3 times" idea, same parts method, same answers 45 and 135 | **Too close** (M5) |
| U9 Learn | worked supposition example; intro shortened | "5 cars and bikes, 14 wheels ... 2 cars" right (8 + 6 = 14) | n/a | **Done**; the marks line ("Each wrong loses marks and the penalty") is cryptic (S4) |
| U9 S05 | R2: U shapes, 7 to 12 tiles, rule 5 x figure + 2, figure 12, 92 tiles | 22, 62, 5 and 2, figure 18 right; the figure shows 7 and 12 tiles as the text says | rule shape "x a figure + 2" is common; numbers and picture new | **Fixed** |
| U9 G03 | shots: 20 shots, hit 7, miss -3, 60 points | 12 hits right | holiday marks items are 10 questions 3/-1 and 25 questions 4/-1; new story and numbers, same supposition skill | **Fixed** (Low: hint gives the method) |
| U10 S03 | clue removed | Siti wins (only order with Mei after Siti and Ali not first) right; trivially easy | holiday l10 has no race | **Fixed** |
| U10 S06 | prize boxes, exactly one label true | A 2 true, B 1, C 2: Box B right | holiday l10 "who is lying" is children and a vase; this is a different story, same try-each method | **Fixed** |
| U10 S07 | Dev 8 and sister 14, ages add to 50 | (50 - 22) / 2 = 14, Dev 22 right | holiday ages items are "Mrs Tan 41, son 9" and "Ben 10, father 38" | **Fixed** |
| U10 S12 | count 2-digit numbers whose tens digit beats the ones digit | 1 + 2 + ... + 9 = 45 right (brute force) | holiday digit counting is "digit 4 from 1 to 50" | **Fixed** (Low: "beats" is odd wording for 10-12, "is greater than" is clearer) |

## Round-2 list R1 to R8, status

| R | Status |
|---|---|
| R1 U3 S06 | Fixed (new story and numbers). |
| R2 U9 S05 | Fixed. |
| R3 U4 S09 | Fixed (S1 note). |
| R4 about 20 frames | **Partly.** About 17 changed. Still too close: U6 T03, U7 G02, U7 G01, U5 G03, U7 T03 (new). Unchanged R4 items still "same frame, new numbers": U5 T03 (holiday l5 163 block stood upright in a tank), U3 S12 (shirt 1/5, shoes 3/8 of the rest, $40), U8 S07 (trapezium), U2 C01. |
| R5 figures | U8 S06, U8 G03, U8 Learn Try, U4 S01 and C01: **fixed**. Still open (Low): U8 S01 (p56) three arcs run into a circle round O and (a) (b) (c) cannot be told apart; U8 S05 (p57) the arrow ticks run into the "70 degrees" and "(b)" labels; U4 S01(b) "12 cm" and C01 "6 cm" sit on the slant lines (readable). |
| R6 Learn | U9 worked example **done**; U8 rhombus **done**; equilateral and the cryptic trapezium line **not done**. |
| R7 Whys | U1 S12, U1 T01, U4 C03, U10 S03, U7 T03 (GST 9%) **done**. U2 G04 labelled Beyond. |
| R8 docs | README Beyond table still lists only U2 G1 (G4 is Beyond now); README line 50 still claims no shared key numbers (false, see M1 to M5); the new README section is accurate otherwise. |

## Must fix (before sale)

Each is a data edit; all keys must be re-derived and the Why rewritten.

- **M1. U4 S01(b) and U4 S06 are the holiday's own numbers.** S01(b): triangle 13, 14, 15 with height 12, area 84, "slanting sides are decoys" (l4.js 33, 87 and 150). S06: rectangle 14 by 9 with the shaded triangle on the base, 63 cm2 (l4.js 100). Round 2 passed both. Give (b) new sides (a set that is not 13-14-15 and not the Learn example 10-17-21, for example base 16 with slants 17 and 17, height 15) and S06 another rectangle (for example 16 by 7).
- **M2. U5 G03** (cuboid, square base, volume, find the side) is holiday l5.js 145 with a twist. Use a different story (for example a box with a square lid and a height relation asked as a perimeter or a number of cubes).
- **M3. U6 T03** (machines make N in M minutes, how many machines) is holiday l6.js 116 with the question reversed. Change the story (not machines, masks, bolts or workers on a line) and, ideally, the unit of time.
- **M4. U7 T03, G01, G02.** T03 is "GST included, how much GST" as in holiday 109 (use a different structure, for example the price before GST given the GST amount, or a mark-up that is not GST). G01 has the holiday's trap and its two answers 25% and 20% (use a pair with other whole-number answers, for example 20 to 50 and back: 150% up, 60% down). G02 is the school-bus frame (use two groups with a different question, for example the percentage of a group that has a given property when the total is known).
- **M5. U8 C01** shares "3 times, 4 equal parts, 45 and 135" with the holiday parallelogram stretch. Change to a different relation (for example angle AOC is 20 degrees more than COB, or ratio 2 times) and a different answer.

## Should fix

- **S1.** Same story, new numbers, same frame (class A): U4 S09, U4 C02, U7 S13, U5 T03, U3 S12, U3 T02. If the owner accepts "same skills, new numbers" for these, say so in the README only; do not claim in README line 50 that every shared item was replaced.
- **S2.** U4 C01 has answer 48 and slants 10 like S01(a); the Learn example and S01(b) both have area 84. Change one number in each pair.
- **S3.** U4 C03: show the height of the small triangle with a visible dashed line (not under hatching) or label "height 4 cm" beside it.
- **S4.** U8 Learn Reasons: add "Equilateral: 3 equal sides, 3 angles of 60 degrees" and reword "Trapezium: between parallel sides 180" to "angles between the same two parallel sides add to 180". U9 Learn marks line: "Marks: suppose all are right. Each wrong answer costs its penalty AND the marks it did not score."
- **S5.** U8 S01 (p56) and S05 (p57) figure labels still touch arcs and arrow ticks (readable, Low).
- **S6.** U10 S12 "beats" to "is greater than".

## Other checks

| Check | Result |
|---|---|
| Page count | print 100 (pp. 78 and 100 blank, zero black pixels), soft 99; page numbers 1-99 identical, text identical apart from the page-number side and "printed book" / "soft copy" (48 pages differ only by that). |
| Contents and answer numbers | Unit starts 6, 13, 20, 27, 34, 41, 48, 55, 62, 69 (each has "Learn it" there); progress 76, certificate 77, answers 79; unit answers begin on 80, 82, 84, 86, 88, 90, 92, 94, 96 (foot of the page), 98: all as printed on the Contents. Pace plan pages agree. |
| Welcome | "Every unit has 7 pages", "answers start on page 79", "Beyond Level 5 is ahead of school. You may skip it." all true; "with new numbers and stories" is true for most items, see M1 to M5. |
| Cover, plaque | "Self-study", "Ages 10-12"; certificate plaque is a plain black block, no pseudo-text. |
| Beyond badges | 14 items carry "Beyond Level 5: ..." (pp. 11, 18 x2, 32, 39, 46, 52 x2, 53, 60 x2, 67 x2, 74), none in Start here. |
| 1-bit zoom, changed pages | U4 S01, C01 (labels readable, small halo gaps where "12 cm" and "6 cm" cross a slant), C03 (hatch hides the dashed height), U8 S06, G03, C01, Learn Try, U9 S05 figure: clean, no moire, lines continuous. Text on every changed page is legible at 100 dpi. |
| Known leftovers outside this audit | "DRAFT licence text, for owner and lawyer approval. Not final." on p. 2 and the temporary contact email (shared, owner decisions). |

## Note on the working tree

`git status` shows unstaged changes to `print/make_term_books.py` and `term/l1/tools/b_quest.py`. They are not mine; I did not touch them.
