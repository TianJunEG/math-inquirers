# Close gaps: Primary 1 (reflection, warm-up check / fast track, open investigation)

Work done 2026-10-22. Nothing committed. Data for all three additions is in `hp/gaps.json`; brute-force checks are in `docs/audit/verify_close_gaps_p1.py` (41 checks, all pass).

## What was added to every lesson (L1 to L10)

- **(a) Reflection "What was hard?"**: a boxed look-back with three prompts (hardest part: 3 lesson-specific ticks + "something else"; got unstuck by: counters / drawing / asking / trying again; next time I will try: one line plus three drawn tick faces easy / OK / hard). Workbook: end of the last core page (designed PDF); closing slide `lN-reflect` (88 to 90 min, exit ticket moved to 80 to 88); tutor guide: 2 SAY lines and a DO line (1 minute, share one, never grade, praise strategy not speed).
- **(b) Warm-up check and fast track**: slide `lN-warmcheck` (7 to 10 min, 2 new-setting questions, click-reveal answers; the quick-questions slide is now 5 to 7 min, "take questions 1 to 3 if short"); tutor guide block with SAY/DO and answers; printed "Fast track" note at the top of each lesson's first workbook page. Run as the program runs: whiteboards shown to camera on three, a "How do you know?" check, private message at minute 40, groups of 8 online where each child already holds up their own page; fast-track children still join Explore and Mini-lesson and return for talk time and exit ticket; nobody is labelled; any child can drop back.
- **(c) Open investigation**: last task on each printed Challenge page (banner plus a `?` item with 5 to 7 writing lines); model answer and what to look for in the tutor key.

| L | Warm-up check (new setting) | Open investigation |
|---|---|---|
| 1 | bunny hops 1,4,7: lands on 20? ; 2nd=12, 3rd=18, find 1st | What if we change the hops? (2s frog vs 3,4,5,6 frog) |
| 2 | 20 sweets, 12 red; true/false 7+5=6+6 | Is it always true? pairs making 10 and 20 are both odd or both even |
| 3 | how many more red than green; will the whole school choose red | What if we change the key? (key 2 works, key 3 does not) |
| 4 | 12th bead; sticks for 4 squares | Is it always true? place 30 matches place 3 in a 3-shape pattern |
| 5 | marbles in a bag; take 2 then add 7 | Is it always true? add 6 then take away 6; then add 6 take away 4 |
| 6 | which of 25/30/40 with 20+10+5; 25 with 3 coins | What if we take a coin away? (no 5c: cannot make 5,15,25,35,45) |
| 7 | 9 corners, how many sides; rectangle cut on a diagonal | Find all the shapes from 3 squares (2) and 4 squares (5) |
| 8 | second tallest of four; odd one out 4,8,12,15 | Find all the orders of 3 children (6), clue leaves 4, make a clue leaving 1 |
| 9 | ribbon from 4 cm to 11 cm; shorter pencil counts more or fewer | Is it always true? shorter unit gives bigger number |
| 10 | 7th of 4,9,14,19 ; 35c with 3 coins | What if we change the jump? three-number totals 18,21,24,27,30 (3 times middle) |

## Verification
Every answer, "find all" and "always true" claim above was brute-forced in Python (all pairs for 10/20; every 3-shape and 4-shape pattern; every coin combination to 10 of each; free polyominoes of 3 and 4 squares; all 6 orders; ranges of IN values; totals for jumps 1 to 5). The fast-track rule only asks a child to explain why: no claim needs more than the checks above.

## Page counts (before / after, rebuilt from the same sources)
| File | Before | After |
|---|---|---|
| Student workbook, designed PDF (`hp/`) | 49 | 48 |
| Student workbook, Word (`hp/P1_Holiday_Program_Student_Workbook.docx`, as PDF) | 51 | 63 |
| Tutor guide PDF | 61 | 72 |
| Decks (slides each) | 26,23,24,22,25,24,26,25,26,27 | each +2 (28,25,26,24,27,26,28,27,28,29) |

The designed workbook fits every addition inside existing pages (every lesson stays 4 pages); L3 drops one page because the drawn pictograph rows are shorter than the old text-glyph rows. The Word workbook adds one page per lesson: the Open investigation and the "What was hard?" box sit together on a final page (the Word pages are too full to fit them). Slide overflow was checked by rendering all 10 decks (no new slide reaches the footer area; only `routine` changed height, still well inside). `levels/build_level.sh 1` was not run: it targets `p1/` (older set) and fails for P1; the `hp/` commands from README were used instead and `levels/mkextras.py` skipped (P2-P6 only). `restyle.py` was run on every deck.

## Unicode shape glyphs replaced (coordinator rule)
- Pictograph key and rows (workbook pet graph and fruit graph, Word and PDF): drawn circles (CSS in the PDF, PNG `hp/dots_*.png` made by `hp/gapkit.py` in Word).
- `hp/qbank.json` (rebuilt keys intact): "□ + □ + 4 = 20" became "A + A + 4 = 20 ... What number is A?"; the key-of-2 picture item now says "Each picture stands for 2 children. Apple has 3 pictures ...". Same fix in `rebuild/gen_l2.py`; `gen_l5.py` worked example uses letter B; `gen_l10.py` key drawn as a circle.
- Slide text (L3 keys, L10 key): glyphs become drawn dot / triangle shapes via `rebuild/p1gaps.cleanup` (the L3 generator source still contains the characters but the built slides do not). L1 frog figure: red crosses drawn as lines, legend now "red crosses" / "blue circles" (`diag/explore.py` and the built slide).
- `hp/mk_pack.py`: star glyph replaced by the word "star".
- Left alone as tick marks, not shapes: check marks in worked-example slides. Scissors icon on the L7 slide untouched.

## Files changed
`hp/gaps.json`, `hp/gapkit.py` (+ `gap_*.png`, `dots_*.png`), `hp/workbook_html.js`, `hp/workbook.js`, `hp/common.js`, `hp/common_html.js`, `hp/guide.js`, `hp/qbank.json`, `hp/mk_pack.py`, `rebuild/p1gaps.py`, `rebuild/gen_l1.py` to `gen_l10.py`, `diag/explore.py`, `split/l1` to `split/l10`, rebuilt PDFs/Word files in `hp/` and copies in `outputs/workbook`, `outputs/designed`.
