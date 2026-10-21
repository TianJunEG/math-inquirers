# P1 audit fixes: what was applied

Source: `docs/audit/audit_p1.md`. Date: 2026-10-22. Nothing was published or committed.

## Issue by issue

| # | Status | What was done |
|---|--------|---------------|
| 1 | Applied | L10 explore rewritten: ONE puzzle card per pair for 10 minutes, swap for a 4-minute second round, 30-second report-backs. The four cards now exist: `lessons.js` L10 `cards`, a "Puzzle cards" page in the workbook (docx and designed PDF, before the certificate), a new slide `l10-cards` (11-21), `l10-explore1` 10-11, `l10-explore2` 21-25. L10 materials, online text, `scripts.js` L10 hook/predict/hints/think/talk and `deck/data.js` / `deck/gen.js` updated. Card answers (45c = 20+20+5, 10th term 32, Mei/Ben/Sam/Ali, 16 cubes) verified in Python. |
| 2 | Applied (partly) | L9 workbook Q6 replaced by the ruler question (a 12 cm, b 5 cm, c own pencil); slides `l9-ws2`, `l9-ws2ans`, `lessons.js` key and `qbank.json` updated; "Each child needs a cm ruler" added to online materials. There is no printable ruler strip in the kit, so none was added (tutors ask for a real ruler). |
| 3 | Applied | L6 page 2 cut to Q3, Q4 (35c with two coins) and Q5 (dollars); old Q4 (70c in 4 coins) and Q6 (Sam 90c) are now Think Harder T2 and T3. `l6-ws2`/`l6-ws2ans` rows, `lessons.js` key, qbank stretch order ($34 change, 70c, Sam, fewest 45c first) updated. |
| 4 | Applied | `l6-teachexact` and `l6-teachswap` moved after the stretch slide, marked "Optional: if you finish early", notes point to T2 / T3. |
| 5 | Applied | L7 mini-lesson now squares in grids only (`l7-teach1` 25-28, `l7-we1` 28-31, `l7-try1` 31-34). `l7-we2`, `l7-try2`, `l7-we3` moved after the stretch slide as optional. New workbook Q6 (2x2 grid, answer 5) with `grid2x2.png`; slide previews and answers, `lessons.js` and guide updated. `deck/data.js` L7 mini replaced. |
| 6 | Applied | `qbank.json` L7 stretch reordered (diagonal fold, two triangles, 3x2 grid = 8, four squares = 5 shapes first). Items added from the slide notes. |
| 7 | Applied | L7 core 3-5 now give the name and number of sides; stretch 7 replaced by the open "4-sided shape that is not a square" item; `l7-we2` has the printed line "In this puzzle only, count squares as rectangles too."; `l7-key` has the card "On the house picture, a square goes in the Square column only." |
| 8 | Applied | Page 2 windows are 58-68 in L1-L10. L2: `l2-teachtri` + `l2-teachtwo` merged into one slide `l2-teachpage2` (56-58). L10: Q9 moved to Talk time (workbook line says so). Other lessons' pre-teaching windows re-timed (see timing table). |
| 9 | Applied | All `challenge`, `chdiag`, `chwalk`, `stretch` slides labelled "Optional: if you finish early" (no clock time). Check-together 68-72, Talk 72-80, Exit 80-90, in slides, speaker notes, title-slide time plan, `lessons.js`, guide routine table and segments, and the scheme of work. |
| 10 | Applied | L3 challenge Q1 now "6 more votes than banana" (banana 6, orange 12); Q2 uses a key of 2 (20 children, answer 4). `qbank.json`, `l3-challenge`, rebuilt `l3-chdiag` (bars, picture graph) and `l3-chwalk`. |
| 11 | Applied | L7 Q3a and stretch 1, L10 Q5a: "4 sides, all the same length, and 4 square corners. What shape am I?" |
| 12 | Applied | L9 core 4 reworded (rope/string) and a new ribbon core item (2 cm to 7 cm = 5 cm). |
| 13 | Applied | L9 stretch reordered (caterpillar, rope, ribbon 3-11 cm, desk 24 erasers, ...) so it no longer repeats the main worksheet and Talk slide. |
| 14 | Applied | L9 challenge[5] says "stick" (53) instead of "ruler". |
| 15 | Applied | L9 Q2 header "Difference (guess and measure)", note "Write how far off your guess was." |
| 16 | Applied | L5 challenge[7] replaced by the 20-marbles puzzle (Ben 8, Ali 12); stretch reordered to [marbles 14, stickers 15, machine rule, ...]. |
| 17 | Applied | L1 challenge[5] reworded ("bigger than 0"), answer 4 kept. `l1-chwalk` already lists both lists. |
| 18 | Applied | L6 challenge[3] reworded (5c steps, 5c to 50c); answer unchanged (5, 15, 25, 35, 45). |
| 19 | Applied | L8 Q1c split into three lines; odd/even reminder printed on `l8-ws1` tip and Q2; "two-loop picture" used in child-facing text (workbook, `l8-we2`, `l8-key`, `l8-ws1`, title, `lessons.js`), "Venn diagram" kept in tutor notes. |
| 20 | Applied | L8 Q4 reworded to "in front of" (order Mei, Ali, Ben, Sam, checked); slide notes `l8-ws2`, `l8-ws2ans` updated. |
| 21 | Applied | L7 exit ticket now a 3x3 grid (14); extension 4x2 (11) then 4x3 (20). Slide `l7-exit`, `lessons.js` updated. |
| 22 | Applied | `qbank.json` "an octagon"; `qbank.py` template fixed and a NOTE added that the JSON was edited directly and the script must not be re-run. |
| 23 | Applied | L7 Q2 column "Straight sides" (circle 0). `lessons.js` mistake text reworded. |
| 24 | Applied | `l8-ws2` stale note replaced. |
| 25 | Applied | Covered by issue 2 (Q6 replaced, no "exactly 10 cubes"). |
| 26 | Applied | L4: "straws, lolly sticks or paper strips (never real matches)" in `lessons.js`, guide, `scripts`/`deck` text, slides (`sub_all` in `gen_l4.py`), and "stick pattern" instead of "matchstick pattern". |
| 27 | Applied | "Stand up and stretch first!" chip and a note line on every `l*-ws2ans` slide (68-72). |
| 28 | Applied | Workbook `extra()` numbers Think Harder T1-T4 and Challenge C1-C3 (docx and designed PDF); "Finished early? Start Think Harder T1 ... or try the Stretch slide" replaces the old tip on all slides; guide labels updated. |
| 29 | Applied (option b) | Slide Stretch answers are printed as a "Stretch slide" row in the `lessons.js` key for L1-L5 and L8 (and L6, L7, L9, L10 via their key edits), so they appear in the tutor guide. |
| P-6 | Partly applied | Coverage note (no time, multiplication/division, 2-digit +/- within 100) added to the P1 scheme of work only. The sign-up page (`website/lp_build.py`) was not touched. |

## New timing (all lessons)

Warm-up 0-10, explore 10-25 (L10: cards 11-21, report-back 21-25), teaching 25-35, break 35-40, worksheet 40-72 (page 1 check-together ends at 52-56, page 2 is 58-68), check page 2 with stand-up stretch 68-72, Talk time 72-80, exit ticket 80-90. Page-1/page-2 pre-teaching slides per lesson: L1 55-58, L2 56-58, L3 54-58, L4 none, L5 54-58, L6 54-58, L7 40-42 and 54-58, L8 54-58, L9 52-58, L10 55-58.

## Files changed

- Content: `hp/lessons.js`, `hp/qbank.json`, `hp/qbank.py` (note and template only), `hp/scripts.js`, `deck/data.js`, `deck/gen.js`.
- Printed material: `hp/workbook.js`, `hp/workbook_html.js`, `hp/guide.js`, `hp/weekly.py` (Puzzle cards page added to week 5), new `hp/grid2x2.png`.
- Generators: `rebuild/gen_l1.py` to `rebuild/gen_l10.py`, new `rebuild/p1fix.py` (P1-only helpers: relabel, patch, sub_all, stretch chip, `finish()`).
- Shared file (minimal, backward compatible): `levels/scheme.py`. Added `ROUT` and `COVER` text that apply only when level is `p1`; other levels keep the original text.

## Rebuilt

- Decks regenerated and restyled: `split/l1` to `split/l10` (gen_l1..gen_l10, then `levels/restyle.py` for each). No overflow in `rebuild/preview.py` after fixes (l7-exit and l3-chdiag were resized).
- Student workbook docx and designed PDF (49 pages), tutor guide docx and PDF (60 pages), question bank docx and PDF (29 pages), weekly PDFs zip, Weekly Dose of Thinking Math, P1 scheme of work.
- Output locations: `outputs/workbook/`, `outputs/designed/`, `outputs/schemes/`.

## Notes for the lead

- Not republished: the P1 deck artifacts need republishing from `split/l1..l10` (lead's step).
- `hp/qbank.py` is stale relative to `qbank.json`; do not regenerate the JSON from it.
- Original files are backed up in the session scratchpad (`work/qbank.orig.json` and `orig_split_l1..10`).
