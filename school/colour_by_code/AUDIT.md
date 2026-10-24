# Colour by Code: independent audit (Primary 1 and Primary 2 galleries)

Audited 23 Oct 2026, branch `claude/great-fermi-1hv4vc`. Scope: 22 worksheets (CBC-01..10, CBC-P2-01..12), 44 pages (pupil and teacher). No file other than this one was edited.

## Method

* Rendered every PDF with `pdftoppm` (100 dpi for reading, 300 dpi crops for clocks, rulers, fractions and graphs, 150 dpi grayscale for the 1-bit test). Read every pupil page; read the teacher pages (the teacher page is the pupil page with answers, so key, picture and fit were compared).
* Re-generated every sheet from the library (`sheet.make_sheet`, deterministic seeds; text spot-matched to the PDFs) and dumped all 319 printed questions. Solved them independently with my own parser (214 by regex: equations, "more/less than", greatest/smallest, place value, patterns, sharing, money, clock arithmetic) and by hand (the other 105: coins, clock faces, rulers, shapes, fractions, tally, graphs, solids), without using `verify.py` or `q.holds`.
* Self-check test by script (not `verify.py`): for every sheet, all single slips (one region wrong colour: 4 x regions cases) and all double slips (every pair of regions, every wrong colour pair, about 1000 to 2200 cases per sheet), asking whether tally, mirror, group or counted-subset check flags it.
* 1-bit test: 150 dpi grayscale, 128 threshold. Mid-grey pixels are 1.4 to 2.0 percent per page (anti-aliasing only), no flat tints, every region is a separate white area. Outline stroke is 0.9 mm throughout (above the 0.5 pt requirement). Only black and white on all pages. The font-size census (pdftotext boxes) found text below the 4.2 mm body size only inside clocks, rulers, coins and the P2-10 graphs.
* Read against `docs/terms/owner_decisions.md` addenda 5-10, `docs/school_books/plan.md`, `docs/books/p1_` and `p2_school_paper_patterns.md`, `term/l1/WORDING_GUIDE.md`, `docs/moe/syllabus_by_level.md`.

## Owner requirements check (all pages)

| requirement | result |
|---|---|
| teacher-facing standalone page, one A4 page, no Mi, no price, no alignment/affiliation wording | Pass on all 44 pages |
| black and white, 0.9 mm solid outlines, no tints, crayon colouring | Pass. Regions are large and well separated; butterfly body, flag, eye dots are solid black (heavy ink but copy well) |
| school-name footer field | Pass (blank line "School name: ____") |
| one/two-star tiers | Present on every page; honesty discussed under F16 |
| self-checking | Tally always present; single slips caught 100 percent; double slips partly (F6) |
| 20 pages per level | NOT met: 10 (P1) and 12 (P2) sheets. plan.md says 3 of 20 P1 pages come from this library; fine if it is a contributor, not the whole book |
| money 50¢ (cent sign) | Pass: all cents written with ¢ |
| time o'clock/half past for P1 | Pass in words; digits 3:30 and 7:30 also used (allowed by the P1 patterns file) |
| wording suited to age | Mostly; see F12, F13, F15 |

## Per-page scores

Ready / Minor fixes / Rework (pupil and teacher page of a sheet get the same score unless noted).

| sheet | topic | score | main points |
|---|---|---|---|
| CBC-01 Rocket bonds 1★ | number bonds to 10 | Ready | all 15 correct; "mirror" word (F12) |
| CBC-02 Fish add 2★ | addition within 20 | Minor | duplicate 8+6+3 twice, 3+6+5 and 6+3+5 (F5); "scales" not identifiable (F4); "Add." covers missing-addend items (F13) |
| CBC-03 Butterfly sub 2★ | subtraction within 20 | Ready | all correct; near-duplicates 17-5-4 / 17-4-5, "7 fewer than" three times |
| CBC-04 House place value 1★ | tens and ones | Minor | "two windows", "6 wall and window parts" cannot be identified (F4) |
| CBC-05 Ice cream counting 2★ | counting in 2s, 5s, 10s | Ready | all correct, unique |
| **CBC-06 Owl compare 2★** | ordering, 1/10 more or less | **Rework** | two wrong items and wrong teacher key (F1) |
| CBC-07 Sailboat money 1★ | coins, cents | Minor | footer says "coins and notes, ¢ and $", page has coins and ¢ only (F11); coin labels about 2.8 mm |
| CBC-08 Fish time 1★ | o'clock, half past | Minor | identical clock pictures twice (2 o'clock x2, 7:30 x2, 3:30 x2 incl. one digital) (F5); clock numerals about 2.5 mm; "Match the time:" wording |
| CBC-09 Ice cream length 1★ | cm | Minor | rulers read from 1 on two items (F14); numerals 2.6 mm; red is 4 regions (fine) |
| CBC-10 House shapes 1★ | corners | Minor | window/wall-part checks unidentifiable (F4); tag says "corners and straight sides" but only corners (F11); circle = 0 corners is unstated |
| CBC-P2-01 Rocket numbers 1★ | numbers to 1000 | Ready | all correct; base-ten block picture is small (hundreds are 10x10 grids about 7 mm) |
| CBC-P2-02 Car addition 2★ | add within 1000 | Minor | all correct; "Sold 170. Left 554. At first:" subjectless (F15); three addends not in P2 syllabus list (F10); wheels overlap body cells |
| CBC-P2-03 Elephant subtraction 2★ | subtract within 1000 | Minor | all correct; picture reads as a balloon, not an elephant (F17); "581 fewer than 828" unnatural |
| CBC-P2-04 House multiplication 1★ | tables 2,3,4,5,10 | Minor | all correct; groups-of-dots pictures small but legible; windows (F4) |
| CBC-P2-05 Castle division 1★ | division | Minor | all correct; "4 ÷ 2" printed twice (F5); instruction "Share or group." does not say divide |
| **CBC-P2-06 Owl fractions 1★** | like fractions | **Rework** | shaded bars solid black, equal parts not visible (F2); slash notation (F7); tag claims "compare", none on page |
| CBC-P2-07 Dinosaur money 2★ | dollars and cents | Minor | all correct; decimal-notation add/subtract beyond the syllabus file (F9); two-step (compare then convert) |
| CBC-P2-08 Fish time 1★ | time | Minor | all correct; clocks 12 mm, hour and minute hands nearly equal (F8); "25 minutes to 9" (F8); tag says "to the minute" |
| **CBC-P2-09 Sailboat measures 1★** | length, mass, volume | **Rework** | arithmetic with units at P1 level; no m, g, scales, comparing; tag claims m and g (F10b) |
| **CBC-P2-10 Car graphs 2★** | picture graphs, tally | **Rework** | key "● = 10" and row labels about 2.5 mm, labels meaningless ("Run", "Cat", "Dog") (F3); single-row "graphs" |
| CBC-P2-11 Butterfly shapes 1★ | 2D/3D | Minor | all correct; tag says "shape patterns", none on page; quarter circle in a "count triangles" row is a small trap |
| CBC-P2-12 Ice cream odd/even 2★ | odd/even | Ready | all unique and correct; key 200, 301, 402, 503, 604 is a visible +101 pattern |

Totals: Ready 5, Minor fixes 13, Rework 4 (CBC-06, P2-06, P2-09, P2-10).

## Findings

Severity: High (wrong content, or the self-check or key cannot be used), Medium (a pupil or teacher is likely to be confused or the page is not on-level), Low (polish).

**F1 (High) CBC-06 Owl: two questions have the wrong answer and the printed teacher key repeats it.** Region `wing_l` prints "10 less than 71, then 1 more" and the key says 60 (red); correct is 71 - 10 + 1 = 62. Region `branch_r` prints "10 less than 76, then 1 more" and the key says 65 (blue); correct is 67. Neither 62 nor 67 is in the key. A pupil who solves it correctly finds no colour; a pupil who slips (stops after "10 less", or does 1 less) gets a key match, a satisfied tally and a pass. Cause: `banks_p1.py` line 186 builds the question from `a + 11` where it needs `a + 9` (a + 11 - 10 + 1 = a + 2, not a). The same sheet's "10 more than 54, then 1 more: 65" is correct (the sibling form at line 184 is right). Why `verify.py` missed it: this form is a `SEM` question (hand-written `holds` lambda, no re-evaluation of the printed text), so the verifier only checks the lambda against itself. Fix: change line 186 to `a + 9` (then wing_l reads "10 less than 69", branch_r "10 less than 74"), regenerate. Add to `qcore.py` a text evaluator for "N more/less than M" and "then 1 more/less" so SEM forms of this kind are re-evaluated from the printed words like `EQ` forms are. Re-check the 2-star key coverage (60 and 65 remain in the key).

**F2 (High) CBC-P2-06 Owl fractions: the shaded part of every bar is solid black, so the equal parts cannot be counted.** In "Shaded:" and "Not shaded:" bars (e.g. 3/4 shaded, 2/3 shaded, "Not shaded" with 2 of 3 black) the black region shows no internal divisions; the pupil must infer the number of parts from the width of the white part. "Not shaded: 1/3" for a bar with a black block and one white box cannot be answered by counting. 300 dpi crop confirms no white separators. Same for circles (half circle shows only one boundary, acceptable). Fix: draw a white 0.5 mm line between every part (or hatch the shaded parts with diagonal lines instead of solid black, which also photocopies lighter). Also see F7.

**F3 (High) CBC-P2-10 Car graphs: the essential information is at about 2.5 mm.** The key "● = 10" and the row label ("Run", "Cat", "Dog") are about 2.5 mm tall in a 12 to 14 mm wide row; the dots are fine. The key is needed for every graph item; a P2 pupil photocopied at 90 percent cannot read it. Row labels "Run", "Cat", "Dog" are not categories a pupil will understand as a graph row (what is being counted?), and "Run ●●● = 10 each" has no title or unit. Each "graph" is one row of 3 to 5 dots, which is a multiplication fact, not a picture graph (no rows to compare, no total, no "how many more"). Tally items are fine (strokes clear, groups of five slashed) but the sheet is 7 tally + 6 one-row graphs. Fix: raise the key to at least 3.5 mm with a picture symbol (a face or a star) not a black dot; label rows with the thing counted ("Cats", "Dogs", "Fish"); give each graph two rows and a question ("How many altogether?", "How many more cats than dogs?"), or relabel the tag "Reading a key and tally marks".

**F4 (Medium) Group and subset checks name parts a pupil cannot find.** House: "the two windows" and "The house has 6 wall and window parts. Exactly N are red/yellow" (CBC-04, CBC-10, P2-04); fish: "The fish has 6 scales" (CBC-02, CBC-08, P2-08); car: "5 body and window parts"; dinosaur: "body has 4 parts". The pictures are plain grids and ovals; nothing is labelled a window or scale, and the page has other regions (bubbles, sand strip) that a child may also count. These sentences are then either skipped or cause wrong "corrections". Fix: show the counted parts with a tiny black dot or the picture could draw the windows with a cross-bar; or rephrase as positional ("the 6 parts inside the oval", "the 6 parts of the wall block"); or drop the sentence and use the tally only.

**F5 (Medium) Duplicate and near-duplicate questions on one page.** The library's `dups` count is 0 because it compares text with line breaks and picture meta. Real duplicates: CBC-02 "8 + 6 + 3" in `tail_up` and `tail_dn` (line break differs), "3 + 6 + 5" and "6 + 3 + 5", "3 + 7 + 6"/"6 + 3 + 4" family; CBC-03 "17 - 5 - 4" and "17 - 4 - 5"; CBC-08 the same 2 o'clock clock twice (`scale_3a`, `scale_1b`), the same 7:30 clock twice (`scale_2a`, `scale_3b`), the same 3:30 clock twice (`fin_top`, `scale_2b`); P2-05 "4 ÷ 2 = ☐" in both door halves; P2-09 "1 l + 5 l" and "5 l + 1 l", "2 cm" family; P2-10 repeated tally 12, 15, 20 and single-row graphs. A pupil sees the same question twice and a teacher sees a padded page. Fix: build the duplicate signature from the evaluated content (sorted operands, clock angles, art meta) and forbid equality.

**F6 (Medium) The tally alone cannot catch a swap, and non-symmetric pictures rely on it.** Single slips: caught 100 percent on all 22 sheets (every wrong colour in every region changes the tally). Random double slips (two regions, any wrong colours): escape rate 0 to 0.5 percent on the 11 mirror-symmetric sheets and 1.6 to 2.6 percent on the 11 sheets with groups/subsets only (CBC-02, 04, 07, 08, 10, P2-02, 04, 07, 08, 09, 10). The exposure is a swap (two regions exchange colours, so the tally is unchanged): 24 to 48 percent of swap pairs go unflagged on those sheets (e.g. CBC-02 41 of 99, P2-02 32 of 67, P2-08 43 of 101), versus 0 to 9 percent on mirror sheets. Also the tally tells the pupil only that something is wrong, not where. Fix: add one more printed check per non-symmetric sheet, e.g. a count per half or per row of the picture ("Top of the fish: yellow 1, red 2 ..."), or a "these four parts are all different colours" sentence; this also localises the error.

**F7 (Medium) P2 fraction notation.** Fractions are typeset 1/2, 2/4 + 1/4, 3/4 with a slash at 4.4 mm. The P2 syllabus asks for fraction notation (1.2) and school papers print stacked fractions. At this size "1/3" and "1/2" are legible but a slash is not the notation being taught. Fix: draw stacked fractions (numerator, bar, denominator) in an `Art` or use the fraction glyph pair; keep slash text only in the page footer if at all. Teacher answers also use the slash.

**F8 (Medium) CBC-P2-08 clocks and wording.** At 12 mm face diameter the hour and minute hands are only slightly different in length, so 10:50 (hands almost together near 10 and 11) and 4:25 are hard to read; the numerals are about 2.5 mm. "25 minutes to 9" and "15 minutes to 7" use spoken-form wording the paper patterns do not show for P1 and do not list for P2 either; digits plus am/pm is the school style. The tag says "Time to the minute" but the sheet is 5-minute times, which is honest for the picture but not for the tag. Fix: make the minute hand clearly longer and thinner, hour hand short and thick, face at least 16 mm (these only fit in the large regions), give "minutes to" an alternative "Which time is 25 minutes before 9:00?", retitle to "Time: hours and minutes".

**F9 (Medium) CBC-P2-07 money syllabus fit.** `syllabus_by_level.md` P2 money: decimal notation, compare two or three amounts, convert between decimal notation and cents only. The page adds and subtracts in decimal notation ("$0.85 + $1.65", "Cost $47.50. Paid $50. Change") and uses $47.50. `docs/books/p2_school_paper_patterns.md` (money section) shows these papers do test change and sums, so this is a conflict between the two docs, not a wrong page; but under the owner's "no content beyond the syllabus" rule it should be resolved by the owner or the question types removed. Also three of the five answers need comparing then converting ("Greatest: $1.45 $1.05 $1.85" answer 185¢) which is two steps under a 2-star tag (acceptable, say so). Notation itself is correct ($0.65 not 0.65 dollars, ¢ after the number).

**F10 (Medium) CBC-P2-09 Sailboat measures is not at Primary 2 level and the tag over-claims.** Every question is an addition or subtraction within 20 with cm, kg or l after it (plus one ruler); there is no m, g, no balance or jug, no comparing or ordering; the first-star key ("5 cm, 9 cm, 4 kg, 8 kg, 6 l") is made by units alone. The footer says "cm, m, g, kg and l". A P1 pupil could do it. Also P2-04's tables and P2-12 are on level. Fix: use the bank's balance, jug and scale forms already described in README (they build on this picture? check `compat.md`: needs a larger picture, e.g. elephant is small) and include at least one m or g item. Also P2-02 "three addends" (77 + 452 + 7, 47 + 329 + 36) are not in the P2 syllabus list (add to 3 digits, two numbers) but are in the papers; Low. Tally marks (P2-10) are not in the P2 syllabus text but appear in the papers; Low.

**F11 (Low to Medium) Footer topic tags overclaim.** CBC-07 "coins and notes, ¢ and $" (coins and ¢ only); CBC-10 "corners and straight sides" (corners only); P2-06 "compare, add and subtract" (no comparison); P2-09 "cm, m, g, kg and l"; P2-11 "and shape patterns" (none); P2-08 "to the minute". A teacher choosing a page by the tag is misled. Fix: derive the tag from the forms actually used on that sheet, or write the tag per gallery entry.

**F12 (Low to Medium) Vocabulary above age.** The check sentence "parts that mirror each other have the same colour" uses "mirror" (symmetry is P4 in the syllabus); P1 pupils also read "tally" (not a P1 word) in "the tally printed" (not printed: the sentence says "Count the parts of each colour" which is fine). Fix: "Parts in the same place on the left and on the right have the same colour." Colour words yellow, red, blue, green, orange are fine for P1; orange and red crayons are the pair pupils most often lack: consider a pupil note ("use a pencil mark for a missing crayon") in the teacher front matter.

**F13 (Low) Instruction lines do not match the item forms.** "Add." (CBC-02) covers "5 + ☐ = 19" and "8 more than 6"; "Take away." (CBC-03) covers "19 - ☐ = 12" and "7 fewer than 16"; the wording guide says "Subtract."; "Share or group." (P2-05) never says divide. Use "Find the missing number." for equation sheets, "Subtract." not "Take away.", "Divide." for P2-05.

**F14 (Low) CBC-09 rulers start at 1 on two items** ("from another mark"). The P2 papers do this ("not always starting at 0") but the P1 syllabus length outcomes are measuring from 0; for P1 keep it only on the 2-star sheet. The object bar floats above the ruler instead of resting on it, so alignment is judged by eye.

**F15 (Low) Wording.** "Sold 170. Left 554. At first:" and "Sold 456, then 197. Altogether" have no subject (who sold what); "581 fewer than 828 is" and "Ann has 493, 246 more than Jane" are unnatural; "Match the time: 6:00" and "Say the time: 3:30" give a time and ask for the words but P1 papers say "Write the time" or "Which time is ...?"; "Smallest: 75 95 87" lists without commas (acceptable). Prefer "A shop had some pens. It sold 170 and has 554 left. How many pens at first?" within the label limits or drop these forms.

**F16 (Low) Tier honesty.** One-star and two-star differ by numbers and one extra step, as the plan allows. Weakest: CBC-05 2★ (counting in 2s/5s/10s at 60-100 is the same skill as 1★), P2-10 2★ (not harder than the P2 1★ graph key), P2-12 2★ (same skills at 200-600). Strongest: CBC-02/03 (three-number and two-step), P2-02/03/07. Within a sheet the colour words are also in a fixed order (yellow, red, blue, green, orange) tied to ascending key values, so the key is a visible sorted list; a guessing pupil can colour by gaps. Fine for early finishers; note for the teacher.

**F17 (Low) Picture quality.** Elephant (P2-03) reads as a balloon with ears (two eye dots sit inside head cells); dinosaur (P2-07) reads as an animal with a head circle; car (P2-02, P2-10) wheels overlap two body regions so the wheel text collides with the body cell; the "sun" and "cloud" ellipses carry no sun/cloud detail. Colourable and legible, but weaker than rocket, house, owl, fish, butterfly. Butterfly body and flags are large solid black areas; fine but ink-heavy.

**F18 (Medium) Topic balance and coverage.** P1 (10 sheets): six number sheets (bonds, add, sub, place value, counting, compare), money, time, length, shapes. Missing against the P1 syllabus: multiplication and division within 40/20, ordinals, addition within 100, picture graphs, 2D shape names (circle, half/quarter circle), and the planned 20 pages. P1 add/sub carry two of the six number sheets while multiplication/division (a whole syllabus outcome) is absent although the plan lists "picture-fill" for it. P2 (12 sheets) covers the strands well (numbers, add, sub, tables, division, fractions, money, time, measure, graph, shapes, odd/even) but measure and graph are thin (F3, F10) and there is no 2-star for tables, division, fractions, measure or shapes. Tiers: P1 has 6 one-star and 4 two-star; P2 has 7 and 5; no sheet pairs the same topic at both tiers.

**F19 (Low) Teacher pages.** Correct and consistent with the pupil pages (every filled answer matches my independent solve apart from F1). Gaps: "Say the time:" / "Match the time:" items show only the colour, not the written answer (CBC-08); no syllabus outcome code per page (addendum 7 asks for the mapping to be visible to the teacher; the footer has only the topic); teacher text shrinks to 2.7 to 3.4 mm in some regions (clock regions, coin regions) and the answer is underlined; the instruction line "Pupils colour their own copy." is fine. No marking guidance for what to do if a pupil's tally is off (one line: "recheck the colours whose count is wrong").

## Independent solve result

319 printed questions: 317 correct and unique; 2 wrong (F1). All picture-based items checked by decoding the drawing: clocks (hour and minute angles agree with the key for 3:30, 7:30, 2:00, 4:25, 6:45, 10:50), rulers (bar length), coins and cash totals, base-ten blocks, shape corner counts (circle 0, triangle 3, square and rectangle 4), solids' flat surfaces (cube/cuboid 6, cylinder 2, cone 1), tally counts, fraction bars, picture graph dots times key. Odd/even and "between 119 and 121" items are unique. No ambiguous second answer found. Key mapping and printed tallies are consistent on every teacher page.

## Ranked top 10

1. F1 CBC-06 wrong items and wrong teacher key (`banks_p1.py` line 186); add printed-text evaluation for SEM forms.
2. F2 P2-06 shaded fractions solid black, parts not countable.
3. F3 P2-10 graph key and labels about 2.5 mm; one-row "graphs".
4. F10 P2-09 not Primary 2 level; tag over-claims.
5. F6 add a localising second check on non-symmetric pictures (swap escapes 24 to 48 percent).
6. F4 group and subset sentences refer to unidentifiable parts (windows, scales).
7. F5 real duplicates not detected by `dups` (clock pictures twice, 8+6+3, 4 ÷ 2).
8. F18 P1 coverage gap (multiplication/division, graphs, ordinals) and 10 and 12 sheets against 20 pages per level.
9. F8 P2-08 clock hands and spoken-form wording.
10. F9 P2-07 decimal-notation add/subtract versus the syllabus file; and F11 tags that over-claim (tie).

## Verdict

The library is close to the owner's brief in format: one A4 page per sheet, pure black outlines at 0.9 mm that photocopy cleanly, no Mi, no prices, no alignment wording, a school-name field, a teacher page, and a tally check that catches every single slip on all 22 sheets (my own script agrees with `verify.py` on that point). Of 319 questions I solved independently, 317 are right and unique, and the two that are wrong (CBC-06) come from a hand-coded semantic form that `verify.py` cannot see and print the wrong answer on the teacher key as well; that sheet must not ship until fixed, and the fix should include a printed-text evaluator so the same class of error cannot recur at P3 to P6. Four sheets need rework (CBC-06, P2-06, P2-09, P2-10) for the wrong answers, uncountable shaded fractions, thin level fit and unreadable graph keys; thirteen need small fixes (identifiable counted parts, real duplicate detection, clock legibility, honest footers, simpler "mirror" wording, instruction lines); five are ready (CBC-01, 03, 05, P2-01, P2-12). The self-check is honest for single slips but swaps (two wrong answers that exchange colours) pass the tally unnoticed on non-symmetric pictures, so those pages want one more localising check. Coverage is a pilot-sized sample (10 and 12 of 20 sheets per level) with P1 missing multiplication/division, picture graphs and ordinals. After the four reworks and the top-10 fixes the P1 set is shippable as a pilot; P2 should follow once P2-09 and P2-10 are on level and the money decimal question (F9) is settled by the owner.
