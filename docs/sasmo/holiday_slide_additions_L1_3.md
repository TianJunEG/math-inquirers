# Holiday skill additions, Levels 1 to 3 (slides and tutor bank)

Written 23 Oct 2026. Owner decision GAPS-SLIDES-NOW (`docs/terms/owner_decisions.md`, 23 Oct night): close the top SASMO-skill gaps in the HOLIDAY program with slide and tutor-bank items, using `docs/sasmo/holiday_skill_coverage.md` sections 1, 2, 3, 7 and 8 (proposals, host lessons, tier slots, tools). Levels 4 to 6 are done by a sibling job (`docs/sasmo/holiday_slide_additions_L4_6.md`).

## Result in one line

59 new items: Level 1: 22 (11 on slides, 11 bank only); Level 2: 20 (11 + 9); Level 3: 17 (9 + 8). 17 decks changed (23 optional slides added). Nothing printed was touched.

Decks changed (for republishing): Level 1 `split/l1`, `l2`, `l3`, `l4`, `l5`, `l7`, `l9`; Level 2 `split/p2l2`, `p2l4`, `p2l5`, `p2l8`, `p2l9`, `p2l10`; Level 3 `split/p3l2`, `p3l3`, `p3l7`, `p3l10`. All other Level 1 to 3 decks are byte-for-byte unchanged.

## How the additions are delivered (print freeze respected)

- **Slide items**: one optional slide per lesson and topic, id `<deck>-skill1` (and `-skill2`, `-skill3`), placed after the Go further walk-through and before Talk time. The pill reads "Optional, if you finish early", like the Think harder, Go further and walk-through slides, so it has no clock time and no minutes. Answers and SAY / ASK / LISTEN FOR sit only in the speaker notes (the tutor phone). Items are additions: no printed question was swapped, no workbook page, page number or question number changed.
- **Bank items**: not on any slide or page the child holds. They are in `hp/qbank_skills.json`, `p2/qbank_skills.json` and `p3/qbank_skills.json` (all items of the level: id, slot, skill, tool, question, answer, say, ask, listen). `hp/qbank.json` and `pN/content/*.js` were NOT edited (nothing can reach a printed page through them).
- **Tutor sheet** (digital, not printed): `outputs/skill_additions/Math_Inquirers_L1_Skill_Additions_Tutor_Sheet.html` and `.pdf` (same for L2 and L3): every item with question, answer, tool, say, ask, listen for, slide or bank.
- **Minutes**: lesson tutor minutes still total 90 in all 30 lessons (`tutor/build_data.py N`, part minutes summed). The new slides are optional, so they join the Flex part and take no minutes. No warm-up was lengthened. `levels/restyle.py` ran twice on all 30 decks of Levels 1 to 3: the second run changed 0 files. Mi appears only on title, break and the last slide (the new slides carry no image).
- **Wording**: `term/l1/WORDING_GUIDE.md` style: command first, numerals, short sentences, names from the cast, Singapore contexts; no price, no MOE, GEP or SASMO words, no hold-ups to the camera (notes say "say the answer together on three"; nothing is held up).
- **Tool names** are the eight in `levels/spine.json` (Spot the pattern, List every way, Draw it, Make a table, Work backwards, Guess and check, Try something simpler, Act it out). Each item has one tool tag, shown in the notes and in the bank files.

## Checks done on every item (the "Check done" column)

- **A = answer verified by an independent script**: `rebuild/skill_items_check.py` recomputes each answer from the item's parameters by brute force or simulation (digit-card permutations, calendar arithmetic, counting by listing every case, every worst-case draw, unique solution search for the letter sum, picture equations and the shared-centre figure, all rules of a family for the star machine, all stick combinations, and so on) and compares with the stored answer; it also asserts that each numeric answer appears in the worked answer text. Result: 59 of 59 match, uniqueness asserted where the item says "find the number".
- **S = similarity check**: `rebuild/skill_items_dupcheck.py` (same approach as `extension/verify/dup_check.py`: 7-word runs, digits masked for a skeleton review) against the holiday program of all six levels (banks, lessons, scripts, gaps, workbook text, every deck slide), the git-ignored private sources on this machine (`docs/books/private_*`, `docs/sasmo/private_*`, read only to compare, nothing copied into a file) and our own term and extension data. Result: no shared 7-word run with the holiday program or the private sources. Items that did share a run (generic phrases such as "how many children are in the queue", number lists) were reworded until clear. Warnings against our own extension and term files are common stock phrases only ("how many cubes are there in all"). Skeleton lines are stock sentence shapes with different numbers.
- **D = drawing or layout viewed**: all 23 new slides were rendered at 1920 by 1080 and looked at (contact sheets); one overflow (Level 2 lesson 4, Level 3 lesson 10) was fixed; the cube, clock, face, window, path, bar, week-strip and symbol figures were checked by eye.

Original items only: every context and number is our own. Skills are named generically from `holiday_skill_coverage.md`; no SASMO, school-paper or holiday question text was read into any file.

## Level 1 items (22)

| ID | Lesson | Slot | Skill | Tool | Answer(s) | Check done |
|---|---|---|---|---|---|---|
| L1-SEQ1 | L1.1 | slide `l1-skill1` | Sequences: each number is made from the two before | Spot the pattern | 13; 21 | A, S, D |
| L1-SEQ2 | L1.1 | bank only | Sequences: two rules take turns | Spot the pattern | 2 5 6 9 10 13 14; no | A, S, D |
| L1-SEQ3 | L1.1 | bank only | Sequences: gaps get smaller | Make a table | 10; 5 | A, S, D |
| L1-PV1 | L1.2 | slide `l2-skill1` | Place value: tens and ones | Act it out | 46; 5; 2 | A, S, D |
| L1-PV2 | L1.2 | slide `l2-skill1` | Place value: digit cards | List every way | 38 83; 83; 38 | A, S, D |
| L1-PV3 | L1.2 | bank only | Place value: three digit cards | List every way | 6; 25 27 52 57 72 75; 57 | A, S, D |
| L1-PV4 | L1.2 | bank only | Place value: odd and even digits, clues | List every way | 37 39; 66 | A, S, D |
| L1-PV5 | L1.2 | bank only | Place value: compare by tens | Make a table | Kumar; 42 | A, S, D |
| L1-MA1 | L1.2 | slide `l2-skill2` | Mental addition: pair numbers to make 10 | Try something simpler | 20; 30 | A, S, D |
| L1-MA2 | L1.2 | slide `l2-skill2` | Mental addition: add 9 by adding 10 | Try something simpler | 45; 44; 71 | A, S, D |
| L1-MA3 | L1.2 | bank only | Mental addition: make the next ten | Try something simpler | 5; 3; 4 | A, S, D |
| L1-SYM1 | L1.2 | slide `l2-skill3` | Picture equations with two symbols | Guess and check | 3; 5 | A, S, D |
| L1-SYM2 | L1.2 | bank only | Picture equations with three symbols | Work backwards | 5; 2; 3 | A, S, D |
| L1-TWICE1 | L1.3 | slide `l3-skill1` | Bar model: twice as many | Draw it | 8; 12; 11 | A, S, D |
| L1-CAL1 | L1.4 | slide `l4-skill1` | Calendar: the week repeats every 7 days | Spot the pattern | Friday; Wednesday; Friday | A, S, D |
| L1-CAL2 | L1.4 | bank only | Calendar: days later and days before | Spot the pattern | 7; Wednesday; Tuesday | A, S, D |
| L1-AGE1 | L1.5 | slide `l5-skill1` | Ages: the gap between ages stays the same | Draw it | 3; 9; 12; 3 | A, S, D |
| L1-AGE2 | L1.5 | bank only | Ages: work out an age from a gap | Work backwards | 33; 25 | A, S, D |
| L1-CUBE1 | L1.7 | slide `l7-skill1` | Counting cubes in stacks, including hidden ones | Act it out | 6; 4; 10 | A, S, D |
| L1-CUBE2 | L1.7 | bank only | Counting cubes: a staircase | Draw it | 10; 5 | A, S, D |
| L1-CLK1 | L1.9 | slide `l9-skill1` | Time: o'clock, half past and minutes in fives | Act it out | 7:30; 8:30; 20 | A, S, D |
| L1-CLK2 | L1.9 | bank only | Time: how long and when it ends | Make a table | 2:45; 10:30; 30 | A, S, D |

Place value (the top gap, 14 SASMO problems) enters in lesson 2: PV1 and PV2 on the lesson 2 slide "Think harder: tens and ones" (tens and ones with boxes of 10; digit cards, greatest, closest to 50), with PV3, PV4, PV5 as bank items (three cards, clue riddles with odd digits, compare by tens). Two-digit mental addition: MA1 and MA2 (pair to make 10, add 9 by adding 10). Changing-step sequences: SEQ1 on lesson 1 (each number is the sum of the two before, gap row), SEQ2 and SEQ3 bank.

## Level 2 items (20)

| ID | Lesson | Slot | Skill | Tool | Answer(s) | Check done |
|---|---|---|---|---|---|---|
| L2-PAIR1 | L2.2 | slide `p2l2-skill1` | Pairing sums: first and last make the same total | Try something simpler | 172; 155 | A, S, D |
| L2-PAIR2 | L2.2 | bank only | Pairing sums: save every day | Try something simpler | 840; 275 | A, S, D |
| L2-LETTER1 | L2.2 | slide `p2l2-skill1` | Letter-digit sums | Guess and check | 1; 9; 7 | A, S, D |
| L2-SEQ1 | L2.4 | slide `p2l4-skill1` | Sequences: the gap grows by 1 each time | Make a table | 21; 27; no | A, S, D |
| L2-SEQ2 | L2.4 | slide `p2l4-skill1` | Sequences: add the two numbers before | Spot the pattern | 26; 42; 110 | A, S, D |
| L2-SEQ3 | L2.4 | bank only | Sequences: two rules take turns | Spot the pattern | 20 30 26 36 32 42 38; 44 | A, S, D |
| L2-SEQ4 | L2.4 | bank only | Sequences: the gap gets smaller | Make a table | 60; 55 | A, S, D |
| L2-AGE1 | L2.5 | slide `p2l5-skill1` | Ages: the gap never changes | Draw it | 8; 12; 12; 40 | A, S, D |
| L2-AGE2 | L2.5 | bank only | Ages: when will it happen? | Make a table | 3; 8; 4 | A, S, D |
| L2-CORNER1 | L2.8 | slide `p2l8-skill1` | Cubes in the corner of a room | Act it out | 9; 14; 6 | A, S, D |
| L2-CORNER2 | L2.8 | bank only | Cubes in a corner: bigger | Make a table | 30; 16 | A, S, D |
| L2-PIC1 | L2.9 | slide `p2l9-skill1` | Picture equations: shapes stand for numbers | Guess and check | 9; 6; 7; 22 | A, S, D |
| L2-PIC2 | L2.9 | bank only | Picture equations: exchange chain | Make a table | 6; 10 | A, S, D |
| L2-CAL1 | L2.9 | slide `p2l9-skill2` | Calendar: weeks and days | Spot the pattern | Thursday; Monday; Saturday | A, S, D |
| L2-CAL2 | L2.9 | bank only | Calendar: dates in a month | Make a table | 1 8 15 22 29; Wednesday; Thursday | A, S, D |
| L2-POST1 | L2.10 | slide `p2l10-skill1` | Posts and gaps | Draw it | 5; 18 | A, S, D |
| L2-QUEUE1 | L2.10 | slide `p2l10-skill1` | Places in a queue | Draw it | 8 | A, S, D |
| L2-POST2 | L2.10 | bank only | Posts and gaps: round a pond | Draw it | 8; 32 | A, S, D |
| L2-WORST1 | L2.10 | slide `p2l10-skill2` | Worst case: how many to be sure? | Act it out | 6; 7 | A, S, D |
| L2-WORST2 | L2.10 | bank only | Worst case: socks | Act it out | 4; 10 | A, S, D |

## Level 3 items (17)

| ID | Lesson | Slot | Skill | Tool | Answer(s) | Check done |
|---|---|---|---|---|---|---|
| L3-PAIR1 | L3.2 | slide `p3l2-skill1` | Pairing: make tens and hundreds | Try something simpler | 40; 1400 | A, S, D |
| L3-SERIES1 | L3.2 | slide `p3l2-skill1` | Series sums: first plus last | Spot the pattern | 55; 4; 220 | A, S, D |
| L3-PAIR2 | L3.2 | bank only | Series sums: a long list | Try something simpler | 820; 91 | A, S, D |
| L3-DIV3 | L3.3 | slide `p3l3-skill1` | Divisibility: the digit sum test for 3 | Spot the pattern | yes; no | A, S, D |
| L3-DIV6 | L3.3 | slide `p3l3-skill1` | Divisibility: 2 and 3 means 6 | Make a table | 6; yes; no | A, S, D |
| L3-RANGE1 | L3.3 | slide `p3l3-skill2` | Counting multiples in a range | Try something simpler | 37; 12; 25 | A, S, D |
| L3-RANGE2 | L3.3 | bank only | Counting multiples in a range | Try something simpler | 33; 16; 6 | A, S, D |
| L3-TOP1 | L3.7 | slide `p3l7-skill1` | Spatial: reading a top view with heights | Act it out | 11; 7 | A, S, D |
| L3-TOP2 | L3.7 | bank only | Spatial: side view | Act it out | 12; 7 | A, S, D |
| L3-FACE1 | L3.10 | slide `p3l10-skill1` | Picture patterns: each feature has its own cycle | Make a table | open open; closed flat; 7 | A, S, D |
| L3-POSTS1 | L3.10 | slide `p3l10-skill2` | Gaps and posts, both sides of a path | Draw it | 18 | A, S, D |
| L3-RECT1 | L3.10 | slide `p3l10-skill2` | Counting rectangles by size | List every way | 18 | A, S, D |
| L3-CHAIN1 | L3.4 | bank only | Balance chains | Draw it | 12; 24; melon plum | A, S, D |
| L3-SHARE1 | L3.2 | bank only | Shape sums: a shared centre | Guess and check | 1 | A, S, D |
| L3-OP1 | L3.10 | bank only | Number patterns: find a secret rule | Make a table | 30 | A, S, D |
| L3-BOUND1 | L3.10 | bank only | Smallest and greatest possible; impossible totals | List every way | 6; 24; no | A, S, D |
| L3-STICK1 | L3.10 | bank only | Most digits from a fixed number of sticks | List every way | 3; 711 | A, S, D |

## Not done, and why

1. **Printed swaps** (the report's "Go further, print swap" items): not done, by the freeze. Each such skill is delivered as a slide and/or bank item instead (examples: Level 2 pairing sums, ages; Level 3 pairing and series sums, multiples in a range). A printed version stays a v2 item.
2. **Extra warm-up items** (report, Level 1 lesson 2): not added, because a warm-up would change lesson minutes. The place-value entry sits on the optional lesson 2 slide instead.
3. **Visual perception** (L1 spot-the-difference, mirror and shadow at Levels 1 to 3): not built, by design (report 7.3).
4. **Level 1 constraint grids and multiplication facts; Level 2 constraint grids, rate and helpers; Level 3 mirror, pyramid faces**: left to the extension books, as the report advises (thin evidence or picture-heavy).
5. **Level 2 spatial beyond the room corner** (nets, which flat net makes a pyramid, rotation) and **Level 3 spatial beyond the top view with heights** (mirror, pyramid faces, cube stack in a corner): not built. They need many drawings; extension fallback.
6. **Tutor guide PDFs, HTML and docx (`hp/guide.js`, `p2/guide.js`, `p3/guide.js`) were NOT rebuilt.** The guide build also rebuilds the weekly PDFs, which embed the frozen workbook pages and the print files, so a rebuild would risk touching frozen output. Their answer-key sections are unaffected (the new items are not in them). The tutor needs: the speaker notes (tutor phone) and the tutor sheet PDFs above. If the owner wants the items inside the guide itself, add a section from `hp/qbank_skills.json` after the freeze lifts.
7. **Question Bank PDF and docx for Level 1** (`hp/qbank_doc.js`) were not rebuilt for the same reason (it reads `hp/qbank.json`); the new bank is in the separate `qbank_skills.json` files and the tutor sheets.
8. **Tutor console**: bank-only items are not shown in the console (it shows slides and their notes). Tutors read bank items from the tutor sheet.
9. **No child trial**: the items are checked for answers, duplicates and layout, not tried with children. The report's own caveat applies: a tutor should try a few before the first lessons (Tue 24 Nov). Level 1 PV2 uses 38 and 83, above the usual 50 limit of the holiday, as the owner accepted for the place-value entry point (open question (iii) in the report).
10. **Wording lint**: `extension/verify/wording_lint.py` works on extension unit data, so it was not run; wording was reviewed by hand against the guide.
11. Not changed on purpose: `hp/workbook*`, `p2` and `p3` workbook files, `outputs/print/**`, `print_spec.json`, weekly PDFs, `hp/qbank.json`, `pN/content`, `levels/spine.json`.

## How to rebuild

    bash rebuild/skill_pipeline.sh 1      # or 2, 3: checks, slides, restyle twice (second must be 0), tutor data
    python3 rebuild/gen_skill_slides.py all   # then restyle (the generator writes unstyled slides)

Source of the items: `rebuild/skill_items_l1_3.py`. Figures: `rebuild/skillkit.py`. Generator: `rebuild/gen_skill_slides.py`. Checks: `rebuild/skill_items_check.py`, `rebuild/skill_items_dupcheck.py`.
