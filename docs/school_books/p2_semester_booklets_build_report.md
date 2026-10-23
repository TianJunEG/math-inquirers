# Primary 2 semester booklets: build report (running progress note)

Branch `claude/great-fermi-1hv4vc`, started 23 Oct 2026. Pipeline `school/p2/` (copied from `school/p1/`; P1 and `school/colour_by_code` were not edited). Plan: `docs/school_books/p2_semester_booklets_plan.md`. Outcome wording: `docs/school_books/p2_outcome_wording.md`. Not pushed, no PR. The independent audit is the coordinator's separate step and was NOT run by the builder.

## Progress

- [x] (a) Gap analysis and allocation (plan, section 1 and 2); all 30 syllabus outcome lines are practised by at least one page, three of them (WN 1.3 writing words, ME 1.1 measuring with real instruments, GE 1.1 making patterns) only in part, listed in the plan.
- [x] (b) Pipeline parameterised for P2 (outcomes, build, render, validate, kit, art2, css_p2, preview, README).
- [x] Wave 1: P2-01 to P2-08. [x] Wave 2: P2-09 to P2-16. [x] Wave 3: P2-17 to P2-24. [x] Wave 4: P2-25 to P2-32. [x] Wave 5: P2-33 to P2-40 (P2-38 to P2-40 colour by code).
- [x] Front matter x2 and answer keys x2 (built by the same script; DRAFT stamps, annual licence, publisher line, contact, registered office, "Key page n of N").
- [x] validate.py: see "Validation" below.

## What was built

Two booklets of 20 pupil pages each (`school/p2/out/P2_S1_Puzzles.pdf`, `P2_S2_Puzzles.pdf`), front matter of 5 pages each, complete packs of 25, and answer keys (`P2_S1_Answer_Key.pdf`, `P2_S2_Answer_Key.pdf`). Semester 1 is 10 one-star and 10 two-star pages; Semester 2 also 10 and 10. Footers print both numbers (for example `S1-07 (P2-17)`: seventh page of the booklet, 17th of the 40 in build order).

Every page: a generator with its own seed; an independent solver that reads the printed text or drawing (clock hand end points, dial needles, tank levels, symbols in a graph row, faces and ellipses of a solid, coins and notes by their printed numerals, vertical sums by their digits, route cells by their printed expressions) and not the generator's data; the wrong-answer enumeration in `validate.py` (every single slip, and every wrong arrangement on the ordering pages, at 95% or better); the word test (each code word has exactly one real-word arrangement, no single letter put in another slot makes a word, no swap makes a word, every wrong choice or order tested on the choice and ordering pages); a key entry with the answers and the check result; a viewed render.

Page table (code, title, stars, check): see `school/p2/README.md` and the plan, section 2.

## Differences from the first plan

- Titles changed: P2-29 is "Time Taken" (was How Long Did It Take?), P2-40 is a colour-by-code time sheet ("Colour the Butterfly", Time 2.1 to 2.3), not a measurement sheet. The measurement and shapes CBC sheets were tried: the sailboat measurement sheet prints litres as "l" and the shapes sheet leaves some parts with a picture and a box but no label, so the time sheet was used.
- P2-29 has five items (two clock pairs, three digital pairs), a five-letter word: six items did not fit with a readable table.
- P2-35 uses the K3 total (the five counts add to 15) together with a code word, like P1-33.
- P2-37 asks for the number of pictures in a covered row from a printed total, then dependent quantities; the cover-up of two rows and the printed total are the check.
- Code words are 5 or 6 letters, taken from a curated list of about 150 words that pass the stricter test (a letter of the word placed in another slot never makes a word).

## Validation

`validate.py` (full, 40 pages): see the last line of `school/p2/out/validation_report.txt`; the result at the time of the last commit is quoted in the final section below. The key's flat-grey limit was raised from 90 to 130 blocks a page: the keys are dense small print and the blocks are anti-aliased text edges (viewed in 1-bit: legible). The pupil-page limit (40 a page) is unchanged and passes.

## Hand-solved from the rendered image (final builds)

39 of the 40 pages were solved by hand from the rendered page image and compared with the key (97%): P2-01 CLOUDS, 02 DAINTY, 03 route (8 boxes), 04 LENGTH, 05 NUMBER, 06 SAILOR, 07 STRING, 08 GRUNT, 09 route (8), 10 CURFEW, 11 FATHOM, 12 route (8), 13 CREAMY, 14 route (7), 15 FROZEN, 16 PEANUT, 17 VALET, 18 SPONGE, 19 loop (6 circles, closes), 20 WALNUT, 21 BANDIT, 22 ANSWER, 23 BOUNCE, 24 BUCKLE, 25 CRAFTY, 26 FRUITY, 27 GUITAR, 28 MIGHTY, 29 MAIZE, 30 SQUARE, 31 TEACUP, 32 WALRUS, 33 BOTANY, 34 DEVOUR, 35 THIEF (counts 5, 2, 1, 4, 3 and total 15), 36 COUSIN, 37 FIGURE, 38 colour tally (yellow 2, red 2, blue 3, green 4, orange 4) and 40 (yellow 2, red 4, blue 4, green 2, orange 2). P2-39 (colour the dinosaur) was read but not coloured: its questions were checked against the key by the library's evaluator only. Pages that were changed after a hand solve were solved again on the final render (P2-04, P2-29, P2-30, P2-33).

## Weak points (honest list)

1. **Mechanism repetition.** 23 of the 40 pages are code-word pages with a number in a box (P2-35 adds a total); the rest are routes (4), a loop (1), lettered choices or orderings (9, in two forms) and colour by code (3). The pupil sees the same "look it up in the code table" idea often. Variety is in the content, not the mechanism.
2. **Letters of the tables on 3-digit pages.** The table has up to 10 boxes (two rows); the number column is wide. Viewed, no letter touches an edge, but the tables are less tidy than P1's single row.
3. **Coin art.** The word "cents" on the 5¢ and 10¢ coins is about 2.5 mm tall (the value numeral is larger); the original coin motifs (leaf, star, flower, sailboat, sun) and the note design (a bird) are original and should be compared once with real money by the owner (as for P1).
4. **P2-07 clock 6 style.** Two clocks of a set can sit on a five-minute mark; a minute hand exactly on a numeral next to decoy letters for one minute either side is fair but needs a careful pupil.
5. **3D drawings (P2-34, 35).** Oblique drawings, 17 to 25 mm; cube and cuboid differ by proportion only. A pupil trial should confirm the cube/cuboid rows.
6. **Number of ordering pages** (P2-21, 23, 28, 24): the check is a six-letter word; it tells the pupil something is wrong, not what.
7. **Pages whose drawn work is not seen by the check:** none; every answer is written in a box. Making a new pattern or drawing is not asked (see the plan, gap analysis).
8. **P2-29** mixes clock pairs and digital pairs; durations cross the hour and sometimes noon (the am and pm labels are generated and re-read by the solver); a teacher should glance at the five items.
9. **Blank box.** As in P1, a box left empty gives no letter and the check cannot see it; the teacher notes say so.
10. **Colour-by-code pages (P2-38, 39, 40).** Copied library (`school/p2/cbc_vendor`, from `school/colour_by_code` at the time of the build, with the P1 mark fixes: circle and moon marks, no doorknob). The library prints "l" for litres on its measurement sheets (not used). Small-part letter space for pencil copies was not re-measured. The sheets contain the sign ÷ and decimal money only where the bank asks for it; the P2-38 and P2-39 sheets were viewed.
11. **No real photocopier test, no pupil trial.**
12. **ℓ glyph.** The litre sign is not in the two fonts; the browser takes it from a fallback font (embedded in the PDF, viewed). Pupil pages print it on P2-26 and P2-27.
13. Counted objects: arrays at 9 to 10 mm (measured at 300 dpi on P2-04: apples 8.9 x 9.9, boats 9.7 x 9.1 including 0.5 mm of dilation); picture-graph faces 10.5 mm; place-value discs 9 mm; solids 17 mm or more.
14. Another process commits the working tree as "Checkpoint" commits, so some commits contain files of mine earlier than my own commit.

## Items for the owner

- Same open items as P1: licence wording (lawyer), final cover title wording, the one not-affiliated sentence on the licence page, pupil trial, a real photocopier test.
- Whether Semester 1 should carry fractions (some schools teach them in Term 4); the plan puts them in Semester 1 and the notes say to hand out any page when the topic has been taught.
- The terms "like fractions" and "unit fractions" appear on P2-21 because the syllabus uses them.
- Coin and note art comparison with real money (decision D1 in `docs/school_books/coin_reproduction_check.md` stays open).

## Final state

`school/p2/validate.py` (full, 40 pages): 747 checks, 0 failed (about 10 minutes). Page counts: pupil booklets 20 and 20, front matter 5 and 5, complete packs 25 and 25, answer keys as printed in `out/` (see `pdfinfo`). Committed: the PDFs, `verification.json`, `validation_report.txt`; not committed: `out/*.html`, `out/bilevel_check/`.

## Audit round 1: fixes made (after `docs/audit_final/p2_semester_booklets_audit.md`)

validate.py: 747 checks, 0 failed. Page counts unchanged (20 / 5 / 25; keys 11 and 9). Not changed on the coordinator's instruction: the time-duration pages P2-29, P2-31, P2-40 (M3, owner decision) and P2-20's division wording beyond L4.

| Finding | Fix |
|---|---|
| H1 P2-39 | The dinosaur (eye dot = twin mark, unmarked tail, marks on boundaries) was replaced by the house picture (mult bank, tier 2, seed 1): no eye or doorknob decoration, every mark inside its own part and away from boundaries, the check-strip rule holds. Page is now "Colour the House". Coloured by hand: yellow 4, red 3, blue 4, green 3, orange 3; every mark set shares one colour. |
| M1 coins | Coins drawn at 0.78 of real-ratio size x (was 0.70); the word "cents" and "dollar" is 2.7 mm font (cap height about 1.9 mm), placed clear of the dashed ring; value numeral 0.58 r. P2-06 and P2-24 re-laid and viewed. The word "purse" no longer appears on P2-06 (L10). |
| M2 fractions | Shaded parts are black fills separated by a white line 1.1 mm wide drawn on top (survives the audit's 600 dpi gap test far better than 0.17 mm); unshaded parts keep black outlines. Viewed; solved again (FROZEN). |
| M4 colour boxes | Answer box 7.5 mm (was 6) on the three colour pages. P2-38 uses seed 306 (the larger box made seed 301 repeat a question). |
| M5, L3 | P2-10: "Make a 3-digit number." P2-05: "The sharer gets a share too." as the first instruction. |
| L1 | P2-09 key note now says two touching boxes can share the words on top. |
| L4 | P2-20: the "if a x b = p then p / b = a" statement divides by 2, 3, 4 or 5 only (no 9). |
| L5 | "siring" and "jailor" added to the reject list in `gen/kit.py` (P2-07 now spells TEACUP). Word assignments of later pages shifted with it; all 32 words are still distinct. |
| L6 | Plan tables regenerated from the built pages. |
| L7 | validate.py label now reads "budget on average per page"; the real concern (flat tint) was checked by the auditor: zero flat blocks. |
| L11 | Cuboids drawn at least 2 : 1 front face; notes say a cube has six equal faces. |
| M3, L8, L9, L12 | Not changed (M3 awaits the owner; L8 is a library sheet without a unit after two boxes; L9 info; L12 owner: the not-affiliated sentence is also on the P2 licence pages). |

Because the word list changed, several pages got new puzzles or new code words (P2-11, 13 letters, 20, 21 BOTANY, 22, 24 CAMPUS, 25, 27, 28 PEANUT, 30 TONGUE, 31 BANDIT with a new timetable, 32 BEHIND, 33 COBALT, 34 BACKUP, 36, 37 FAMILY with new graph, 38). Re-solved by hand from the final render: P2-04, 06, 07 (TEACUP), 13 (CREAMY), 15, 20 (WIZARD), 21, 24, 28, 30, 31, 32, 33, 34, 37, 38, 39. Pages 11, 22, 25, 27, 36 kept their answers and only the letters changed (their solvers and the word tests pass). The earlier hand-solve list in this report refers to the previous build for those pages.

## Audit round 2: fixes made, and owner decisions

validate.py: 747 checks, 0 failed. Page counts unchanged (20 / 5 / 25; keys 11 and 9).

Owner decisions applied: **P2-REMOVE-P3**, **P2-LOWS-FIX**, **P2-NOTAFFIL-FRONT** (the "Not affiliated with or endorsed by the Ministry of Education, Singapore." sentence is removed from the P2 licence page and printed on the cover instead, small, below the publisher line; the licence page keeps only the sentence that the syllabus is published by the Ministry), **P2-GREY-OK** (the raised key grey limit, 130 blocks a page as a budget, stays) and **P2-FRACTIONS-KEEP** (fractions stay in Semester 1).

| Item | Change |
|---|---|
| Primary 3 duration content | P2-29 is now "Match the Times": six clocks (to the minute) and six digital times, the pupil writes the letter of the clock for each time (letters spell a word; every wrong matching tested). P2-31 Time Detective is a timetable with the start time and how long each lesson lasts (hours and minutes); questions change hours and minutes to minutes, add two lessons, read the minutes past the hour, count lessons starting before 10 am, and give the minutes over 1 h; no question asks for an end, start or duration to be found from the other two. P2-40 is now a money sheet (Colour the Butterfly, money bank tier 2, seed 311) instead of the time sheet. The division by 9 on P2-20 was already replaced in round 1 (divisors 2, 3, 4, 5 only). |
| Outcomes now less covered | Time 2.2 "measuring time in hours and minutes": practised only by P2-31 (reading hours and minutes) and no longer by durations from a start and finish time. Time 2.1 is practised by P2-07, 29 and 31; Time 2.3 by P2-30 and 31. Money gains P2-40. The plan's gap table and "excluded" list say so. |
| 5 cent coin | The dashed inner ring is removed from every coin, so "cents" no longer touches anything. |
| P2-33 key | Internal labels replaced by "shape and colour", "size and colour", "shape and size", "turn"; "half circle" removed from the note (turning rows use triangles only). |
| Colour pages | Answer box 9 mm on P2-38, 39 and 40. |
| P2-40 unit | Moot: the new sheet prints the cent sign after every box. |

Re-solved by hand from the final render: P2-29 SHADOW (9:32 S, 10:26 H, 4:06 A, 6:12 D, 10:34 O, 7:16 W), P2-31 BANDIT (45, 85, 100, 10, 2, 25), P2-40 (yellow 2, red 4, blue 2, green 2, orange 4; every part solved). 1-bit copies of P2-06, 29, 31, 38 and 40 were viewed: legible, coins clean. All other pages have the same answers as the previous build (compared by key text); P2-33 changed only its key labels.

## Audit round 3: Lows fixed

validate.py: 747 checks, 0 failed. Teacher notes: "durations" in the problem-solving sentence is now "lengths of lessons given in hours and minutes" (L-G); the code-word line now says answers in the wrong boxes never make another word and "one or two wrong answers very rarely do" (L-I); the photocopying note says to use normal toner, not a light setting, on the coin pages. The words "cents" and "dollar" on the coins are 2.9 mm font (was 2.7); viewed at 110 dpi on Dollars and Cents: clear of the rim and the numeral. No page content changed.

## Coin and note art: real proportions (owner decision COINS-FIX-SIZE, 23 Oct 2026)

- Specifications and sources: `docs/school_books/coin_note_specs.md` (MAS: 5c 16.75, 10c 18.50, 20c 21.00, 50c 23.00, $1 24.65 mm; notes $2 126 x 63, $5 133 x 66, $10 141 x 69 mm). The earlier art used older-series diameters (16.2 / 18.5 / 21.4 / 24.7 / 24.65 mm), so the 20c and 50c were wrong; now corrected.
- P2 pages (`gen/art2.py`): coin diameter = real x 0.80 (5c 13.4, 10c 14.8, 20c 16.8, 50c 18.4, $1 19.7 mm). Notes are 2:1 and grow with value, real size x 0.215 ($2 27.1 x 13.5, $5 28.6 x 14.2, $10 30.3 x 14.8 mm); the bird and corner numerals scale with the note. "cents" and "dollar" stay at 2.9 mm type (cap height about 2.0 mm). No dashed ring on any coin.
- Purse selection uses the earlier coin widths (`money_width`, kept only for choosing seeded purses), so every seeded puzzle and every answer is unchanged (answer-key text identical to before). The drawn widths (`real_money_width`) were checked by viewing S2-01 and S2-04: nothing overflows.
- Teacher notes (S1 and S2 front matter, Photocopying paragraph): "Pictures are not actual size."
- validate.py: 747 checks, 0 failed.
- Pages that show coin or note pictures (checked by opening each page, colour and 1-bit copy): S2-01 Dollars and Cents (P2-06: notes $2, $5, $10 and coins), S2-04 Purse Match (P2-24: coins, including $1). S2-02 Writing Money, S2-03 Which Costs More? and S2-20 Colour the Butterfly (P2-40) show amounts as text only (no coin or note pictures). The colour-by-code library sheet CBC-P2-07 Dinosaur Money shows small coin and note pictures (library, outside the booklets).

Follow-up to the independent coin check (3 Lows fixed): (1) wording "drawn larger than real" replaced by "not actual size (smaller than real)" in the P2 front matter (S1 and S2) and in the S2-01 and S2-04 teacher notes of the S2 answer key, and in the code comments; (2) P2-24 Purse Match (S2-04): one coin scale for every purse (printed at 0.96 of the S2-01 size, so a $1 coin is 19.0 mm in all six purses; the purses no longer shrink to fit; the page is not scaled for any other reason); (3) every seeded puzzle and answer unchanged (answer-key text identical to the version before the coin work apart from the wording lines).
