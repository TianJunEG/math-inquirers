# Fix round 3 (24 Oct 2026): answers to AUDIT_ROUND3.md

Scope: `website/teasers/` and the owner preview (`outputs/owner_review/teasers_preview/`) only. `website/dist` untouched, nothing deployed, `site_enabled` still `false`. January to October are **not** written.
Owner policy applied: TEASER-STRICT (Levels 3 to 6), L1L2-GAP60 (Levels 1 and 2), a new story AND a new frame, honest wording ("a new puzzle every day", never "a new kind" or "a new idea"). Family cap 3 per quarter (Levels 3 to 6) and 3 in 60 days (Levels 1 and 2) is **confirmed by default** (blanket "proceed with the recommendations"). `website/mi_signup.html` and `website/level_pages/*.html` were never modified by this work: every preview build ran in a scratch copy of `website/` under `/dev/shm`, and the new test `test_flag_off.py` fails if they ever differ from the flag-off generator output.

## Closed and not closed

| ID | Item | Status | What was done |
|---|---|---|---|
| H-1 | Four High near-copies (`L3-windowpanes`, `L3-nightbus` and `L4-nighttrain`, `L1-borrowdays`, `L1-coinsets`) and the Mediums | **Closed for every listed item; text rules are heuristic** | All replaced by new stories on new structures (table 1). The frames themselves (coins make an amount, which weekday N days later, growing gaps, number pyramid, number machine, tap and leak, posts and gaps, mirror clock, jug pouring, turtle, last digit, three dice stacked) are **retired in `taxonomy.json`**, so no level can use them again. The widened verifier then found about 45 further near-matches in the rest of the bank (sources it could not see before); each was rewritten (table 2). |
| H-2 | Flag-off pages not byte-identical in the repo | **Closed** | The seven files were restored by the owner before this round and were never touched since. New `test_flag_off.py` (run first by `test_site.py`): generates the pages in a scratch copy WITHOUT `MI_TEASERS`, compares every file byte for byte with the committed one, checks no committed page carries the teaser while `site_enabled` is false, and checks `git status website/dist` is empty. Its `--selftest` proves it fails when a page carries the teaser. |
| H-3 | Level 1 and Level 6 cannot absorb one failure | **Closed on paper** | L1 usable 73 (was 62), L4 slack 25 (capacity 117, was 101), L5 capacity 113 (was 95), L6 capacity 104 (was 92), after retiring 13 frames. Independent year check below: L1 survives 8 lost sub-structures, L6 12. 35 of the 38 new sub-structures are usable and **every one is used by a released puzzle** (so each has had one story verified). |
| M-1 | Family cap 3 or 2 | **Closed (confirmed by default)** | README states it. The year model also reports cap 2: infeasible, because the released Nov and Dec already use families 3 times in Q4. |
| M-2 | Cross-level repeats | **Documented** | README: 50 of 172 sub-structures (202 of 366 puzzles) appeared at three or more levels in the round-2 bank (allowed, per level rules); in the round-3 bank 41 of 196 (161 of 366). Honest wording rule written down. |
| M-3 | Level fit cluster at Level 2 | **Closed** | `L2-mangoes`, `L2-barleycafe`, `L2-mooncakes`, `L2-schoolbus`, `L2-beadswhole`, `L2-cakeparts`, `L2-lampring` replaced (table 3). `money.unitary_price` now starts at Level 3, `fractions.whole_from_part` at Level 4, `counting_pairs.handshakes` stops at Level 5. |
| M-4 | Verifier's "0 FAIL" depended on the checkout | **Closed** | Whole working tree, tracked or not; sorted file list; a content digest in every report; `source_lock.json` makes an incomplete tree exit 2 ("INVALID VERIFICATION"); caches keyed by content, not file times; all tie-breaks sorted (reports identical under different `PYTHONHASHSEED`; the only difference between two runs was the digest, because other agents were editing `practice/` between the runs). |
| M-5 | Family cap | Closed (see M-1) | |
| M-6 | Parameter-poor L1 and L2 sub-structures | **Partly closed** | L1 now has 12 spare sub-structures (was 1) and L2 36; one failed sub-structure can be replaced for all 61 rotation slots at both levels. Several new L1 kinds have a larger parameter space than the old ones (sort by digit sum, race places, sum of ages later, weeks and days, number words in dictionary order). Some (checkerboard, equal marks) are still thin; they are return-six-times-a-year risks for the author, not structure failures. |
| M-7 | Text answers at Levels 3 to 6 not tested for the year | **Not closed** | Still open (about 30 distinct names, weekdays and shapes are needed per level; Nov and Dec use 5 per level). |
| L-1 | "It is X" and "The answer is X" give "Not yet" | **Closed** | `teasers.js` strips "the answer is", "it is", "it's", "answer:" before parsing; `test_site.py` tests all 366 puzzles in both forms (numeric with and without units, text answers) plus 13 edge cases. |
| L-2 | README counts (175 in use, 39 merged subs) | **Closed** | New counts in README. |
| L-3 | Wording slips | **Closed** | `L5-colourdraw` hint says tickets; `L5-sunflowerfall` asks only for the growth; `L2-twonumbers` is 13 and 40 (not 33 and 270). |
| L-4, L-5, L-7, L-8, L-9 | `_headers`, `data-teaser-state`, Scratch and Python in `L6-codingclub`, home page level picker, heavy L2 and L3 items | Not touched | Out of scope or by design (see the report at the end). |
| L-6 | Old numbers in ids (`L3-coins40`, `L4-coins60`) | **Closed** | Those puzzles were replaced. |

## 1. The four High near-copies and the Mediums: replacements

Every replacement is on a different maths sub-structure from the one it replaces (a "new frame"), has its own solver, independent checker, citation and level range, and was solved twice (author solver and independent checker) over the whole search space.

| Replaced | New puzzle (sub-structure) | Why |
|---|---|---|
| `L3-windowpanes` (High) | `L3-pencildrawing` (networks.draw_without_lifting: fewest pencil lifts for a figure of dots and lines) | frame of our Skill Additions L3-RECT1, p3 qbank |
| `L3-nightbus` (High) | `L3-chessboard` (arrays.checkerboard: dark squares on the edge of a chessboard) | `durations.elapsed` story is in p3 l9 (night train 22:40 to 01:15) |
| `L4-nighttrain` (High) | `L4-gainingclock` (clock_reading.faulty_clock) | same story again |
| `L1-borrowdays` (High) | `L1-campdays` (calendar.weeks_and_days) | frame in the L4 Skill Additions sheet, term l1 and every other level; `calendar.weekday_after` retired |
| `L1-coinsets` (High) | `L1-twodice` (counting_pairs.dice_sum_ways) | frame of `docs/audit/mkgifted_p3.py` and holiday P6 week 5; `coins.make_amount` retired; also removed at `L3-coins40` (now `L3-sticksdisplay`, digit_display.segments), `L4-coins60` (`L4-swaphundreds`, place_value.swap_digits) and `L5-fiftycents` (`L5-lostnumber`, series_sum.missing_term) |
| `L5-leak` | `L5-threeclubs` (sorting.three_sets, three overlapping groups) | extension l5_u05; `rate.fill_with_leak` retired |
| `L5-teams16` (verifier FAIL) | `L5-diagline` (counting_grid.diagonal_squares) | holiday P6 week 5 league file |
| `L2-machine4`, `L4-machinefive`, `L1-machine5`, `L5-machinesix` | `L2-fewestswaps` (sorting.fewest_swaps), `L4-cubenet` (shapes.cube_net_opposite), `L1-stripmarks` (number_line.equal_marks), `L5-riverboat` (moves.ferry_trips) | P2 tutor guide, SASMO drafts, P6 Algebra Machines; `function_machine.find_the_rule` retired |
| `L3-stampshare` | `L3-cardsorder` (sorting.order_by_digit_rule) | `docs/books` B3.2 |
| `L6-lastdigit` | `L6-stickerratio` (ratio.ratio_changes) | SASMO g6 draft 2.2; `modular.last_digit_power` retired |
| `L1-ageplus`, `L2-grandpaage` | `L1-siblingsages` (ages.sum_later), `L2-plankcuts` (counting_line.cuts_and_pieces) | `docs/books` B10.1; `ages.age_gap` kept only at Level 3 |
| `L2-pencilcase`, `L6-tokenbox` | `L2-cakeshare` (fractions.unit_compare), `L6-twoclasses` (averages.combined_groups) | p6 qbank and L6 Skill Additions ("how many to be sure of 2 of the same colour") |
| `L6-turtle` | `L6-evenodd` (programs.branching) | p6 content l7; `polygons.turtle_repeat` retired |
| growing gaps: `L1-rungrow`, `L2-shellrows`, `L3-dotgaps`, `L5-tincoins`, `L6-stickersave` | `L1-numpattern` (sequence.alternating_steps), `L2-hallfloor` (arrays.checkerboard), `L3-ricejar` (measurement.container_and_contents), `L5-cornerscard` (triangle_area.cut_corners), `L6-juicecups` (fractions.share_fraction) | holiday P1 lesson 1; `growing_pattern.growing_gaps` retired |
| number pyramids: `L1-boxpyramid`, `L3-stonepyramid`, `L4-canpyramid`, `L5-fivebricks`, `L6-stonepyramid5` | `L1-streetwalk` (spatial.net_displacement), `L3-cardcorners` (perimeter_area.notched_perimeter), `L4-mirrorgrid` (symmetry.complete_figure), `L5-circleout` (spatial.circle_elimination), `L6-cubeedges` (networks.draw_without_lifting) | extension l3_u02; `number_grid.number_pyramid` retired |
| weekday after N days: `L3-poolcourse`, `L4-readchallenge`, `L5-christmas`, `L6-projectdays` | `L3-missednumber` (series_sum.missing_term), `L4-fakecoin` (strategy.fake_coin), `L5-divquotient` (division.reverse_division), `L6-sevencards` (sorting.fewest_swaps) | same frame as `L1-borrowdays` |

## 2. Further near-matches found by the widened verifier (all rewritten)

The new source list (below) and the sentence-level index found these in the rest of the bank; all were reworded or re-based, none is left as a FAIL.
`L1-jarsweets`, `L1-toycars` (term l1 lessons 7 and 25), `L1-hiddensum` (P2 hidden-digit item), `L1-traysame`, `L1-trackflags` and `L2-lampring` (posts and gaps in the Skill Additions: `counting_line.posts_loop` retired, now `L1-racerun`, `L2-swaphana`), `L2-pizzachoice` (extension l6_u05: now `L2-lunchsets`), `L2-sleephours`, `L2-dicetops` (three dice in `levels/gap_items.py`: `cubes.dice_faces` retired, now `L2-wordorder`), `L2-cakeparts`, `L2-schoolbus` (extension l3_u05), `L2-beanleaves` (SASMO g1 draft: now `L2-lilypatch`), `L2-jarcoins`, `L2-bookcase`, `L2-tankwater`, `L3-mirrorclock` (SASMO g1 draft: `clock_reading.mirror_time` retired), `L3-jugs` (P2 lesson 9: `containers.jug_pouring` retired), `L3-clockturn`, `L3-books`, `L3-bakery`, `L3-beadbag`, `L3-lanes5` and `L4-podium` and `L6-podium10` (extension l6_u05 gold, silver, bronze), `L3-floortiles2`, `L4-piechart`, `L4-clockfive`, `L4-puddle` (holiday P6 "8 routes avoid the puddle"), `L4-concert`, `L5-figures` and `L6-tilepattern6` (extension l5_u09 plus-sign tiles: `figure_rule.nth_figure` now Level 4 only), `L5-threesports`, `L5-cornerscard`, `L5-bottleshare`, `L5-fourside` (P5 lesson 8), `L6-twored` (our diag p6.json has the same bag: 4 red, 3 blue, 5 green), `L6-seabird` (p6 l3), `L6-juicecups`, `L6-bannerheight`, `L6-temps`. Each of these comes from a real overlap of words, numbers or both with one of our own sources.

## 3. Level fit (Level 2 cluster, section 6 of the audit)

| Old | New (MOE source) |
|---|---|
| `L2-mangoes` ($7.80 for 6, then 11: decimal money, P4) | `L2-stripchain` (whole-number lengths, overlap: P2 length, tables) |
| `L2-barleycafe` (3 cups at $3.60) | same sub, whole dollars: 3 cups at $3, cake $4, pay $20 (P2/P3 money) |
| `L2-mooncakes` (247 divided by 12) | 87 divided by 5 (P2 table of 5) |
| `L2-schoolbus` (250 divided by 12) | 62 players in teams of 5 (P2 table of 5; story changed because extension l3_u05 had the buses) |
| `L2-beadswhole` (inverse fraction of a set, P4) | `L2-thinknumber` (division with a remainder, divisor 4: P3 3.3) |
| `L2-cakeparts` ("simplest form", P3) | 5/12 of 12 equal beds, no "simplest form" (P2 like fractions) |
| `L2-lampring` (270 divided by 9) | `L2-swaphana` (swap two digits of a 3-digit number: P2 numbers to 1000) |
Also at Level 1: `L1-trackflags` (108 / 3), `L1-bamboo` (84 / 4), `L1-lampbench` (18 and 64) now use smaller numbers (P1 and P2).

## 4. The verifier (`verify_bank.py`), what changed

* **Sources: the whole working tree.** `outputs/` (the six Skill Additions sheets), `docs/**` (md, json, py, html, txt, csv: `docs/audit/*.py`, the books, SASMO drafts, `docs/terms`), `practice/**` (every `lesson.py` and its `dist/data` JSON: holiday weeks 1 to 5 and the term lessons), `school/` booklets (html, py, md), `hp`, `p1` to `p6`, `extension`, `tutor`, `term` lessons, `split/`, `rebuild/`, `levels/`, `diag/`, `deck/`, `portal/`, `website/` (without `teasers/`, `dist/` and the preview), tracked or not. 3,818 files, 70 MB, about 478,000 sentences (round 2: about 21,000 question-ending chunks).
* **Sentence-level index.** Every sentence of every source, in windows of one to three sentences. Round 2 kept only chunks that end in a question mark, so a puzzle stated as a command ("Name the weekday of the return date.") was invisible.
* **The auditor's rules, added.** A (content words: at least 70% of the teaser's story words, at least 4 shared, two rare words), A2 (specific objects and a quantity: "three panes across, two down"), B (three or more of the same numbers, two of them distinctive, with three shared story words), C (three shared four-word runs with numbers masked, at least 30% of the teaser's four-grams). Weekday and month names are no longer story words. The round-2 rules F1, F2, F4, F5 and W are kept (F2 and F5 tightened: a rare word is needed).
* **Reproducible.** Sorted file list, sha256 digest of all paths and contents in every report, content-keyed caches, tie-breaks sorted, `source_lock.json` (minimum files per root and required private sources: the verifier exits 2 instead of printing "0 FAIL" on an incomplete tree). Same bank, same rules, same digest gives the same report; a different digest is a different verdict.
* **Self-test (62 cases, 0 problems).** Replays the round-2 wording of the four Highs and the Mediums: `L3-windowpanes` (rule A2), `L3-nightbus` (F2), `L4-nighttrain` and `L1-borrowdays` (wording rule W), `L5-leak` and `L5-teams16` (rule C), `L2-pencilcase` (F2) are text FAILs; `L1-coinsets` and the retired frames are caught by the taxonomy (the frame is not in the words, so no text rule can see it; the self-test asserts the sub-structure is unusable at every level). Also: the source list contains `outputs/skill_additions/..L3..html`, `docs/audit/mkgifted_p3.py`, `practice/holiday/p6/05/lesson.py`, `school/p3/out/S2_pupil.html`, `levels/gap_items.py`; the lock refuses a tracked-only tree; the same question gives the same verdict twice; 88 kinds agree between solver and checker.
* **Capacity report.** Lists the retired sub-structures with the reason and the number of round-3 sub-structures no released puzzle uses yet (0).

## 5. Capacity and the new sub-structures (section 4 of the audit)

38 new sub-structures, each with `cite` (MOE syllabus page or our own lesson), `levels`, `kinds`, a solver in `kinds_r3.py`, an **independent checker** in `brute_r3.py` (never imports the solver: breadth-first search, exact geometry, dynamic programming over edge subsets, folding a net with exact rotations, simulation) and a sample in `samples_r3.py`:
`counting_line.cuts_and_pieces` (1-6), `fractions.unit_compare` (1-3), `calendar.weeks_and_days` (1-3), `sorting.fewest_swaps` (1-6), `measurement.overlapping_chain` (1-4), `moves.ferry_trips` (1-5), `counting_pairs.dice_sum_ways` (1-5), `arrays.checkerboard` (1-5), `number_line.equal_marks` (1-4), `ages.sum_later` (1-5), `sorting.order_by_digit_rule` (1-4), `number_names.alphabetical` (1-4), `sequence.alternating_steps` (1-5), `counting_line.race_places` (1-5), `spatial.net_displacement` (1-5), `durations.schedule_with_breaks` (2-6), `division.reverse_division` (2-6), `spatial.circle_elimination` (1-6), `digit_display.segments` (1-5), `place_value.swap_digits` (1-6), `strategy.fake_coin` (3-6), `perimeter_area.notched_perimeter` (3-6), `measurement.container_and_contents` (3-6), `series_sum.missing_term` (3-6), `networks.draw_without_lifting` (3-6), `clock_reading.faulty_clock` (3-6), `counting_grid.diagonal_squares` (4-6), `shapes.cube_net_opposite` (4-6), `symmetry.complete_figure` (4-6), `sorting.three_sets` (5-6), `triangle_area.cut_corners` (5-6), `averages.combined_groups` (6), `ratio.ratio_changes` (6), `fractions.share_fraction` (6), `programs.branching` (6); three more (`clock_reading.mirror_time`, `containers.jug_pouring`, `number_arrangement.triangle_sides`) were built, tested, and then retired when the verifier showed our books already tell the same story. No renamed twins: every new idea asks a different question from the old ones in its family (for example, fewest neighbour swaps, not another ordering clue; edge squares of a chessboard, not another tile count).

Retired in round 3 (frame in our own books): `calendar.weekday_after`, `coins.make_amount`, `counting_line.posts_loop`, `cubes.dice_faces`, `function_machine.find_the_rule`, `growing_pattern.growing_gaps`, `modular.last_digit_power`, `number_grid.number_pyramid`, `polygons.turtle_repeat`, `rate.fill_with_leak`, plus the three above. Restricted: `ages.age_gap` to Level 3, `figure_rule.nth_figure` to Level 4, `counting_pairs.handshakes` to Levels 1 to 5, `fractions.whole_from_part` to Levels 4 and 5, `money.unitary_price` to Levels 3 to 6.

| Level | Usable sub-structures (round 2 audit) | Now | Needed | Slack / capacity per quarter (3 to 6) |
|---|---|---|---|---|
| 1 | 62 | **73** (target 71 or more, after removing every frame found in our books) | 61 | 12 spare |
| 2 | 87 | 97 | 61 | 36 spare |
| 3 | 108 (capacity 103) | 126 (capacity 114) | 92 | 22 |
| 4 | 108 (101) | 129 (117) | 92 | **25** (target 10 or more) |
| 5 | 103 (95) | 121 (113) | 92 | 21 (**113**, target 100 or more) |
| 6 | 98 (92) | 109 (104) | 92 | 12 (**104**, target 100 or more) |

## 6. Independent circular year check (`year_model.py`)

Run: `python3 website/teasers/year_model.py --full` (about 12 minutes; it reads only `taxonomy.json`, the two banks and `YEAR_PLAN.md`). **0 problems.**

| Level | Rule | Result |
|---|---|---|
| 1 | L1L2-GAP60 rotation of 61 sub-structures, 366-day and 365-day circular year | minimum circular gap 61 (366-day year) and 60 (365-day year); worst family in 60 days 3; 0 same-family neighbours; plan equals the released bank on all 61 rows. 12 spare sub-structures: one failed sub-structure can be replaced in all 6 of its slots for 61 of 61 rotation slots; 1, 2, 3, 5 and 8 failures absorbed in 500 of 500 random draws, 12 failures in 16 of 500 (round 2: one failure only, two impossible). |
| 2 | same | same gaps and family results; 36 spares; up to 12 simultaneous failures absorbed in 500 of 500 draws. |
| 3 | TEASER-STRICT integer program (366 dates, quarter caps, family cap 3, 30-day circular gap, no family on consecutive days, Nov and Dec fixed) | **feasible** (9 s); losing 1, 3, 5, 8 or 12 random unreleased sub-structures (65 unreleased): a year still exists in 5 of 5 draws each. |
| 4 | same | **feasible** (7 s); 5 of 5 draws at every loss size (68 unreleased). |
| 5 | same | **feasible** (9 s); 5 of 5 draws at every loss size (round 2: 0 of 5 at 8 losses) (60 unreleased). |
| 6 | same | **feasible** (6 s); 5 of 5 draws at every loss size (round 2: 0 of 5 at any loss) (48 unreleased). |

With the stricter family cap 2 the model is infeasible at Levels 3 to 6 at once (1 s): the released Nov and Dec already use some families three times in the fourth quarter. The owner's cap is 3, so this is a statement about the released months, not a defect.


## 7. Results

* `build_bank.py`: November 30 and December 31 puzzles at each of the six levels (366). `build_bank.py --plan`: Levels 1 and 2 plan, 0 violations.
* `verify_bank.py` on the full tree: **November 0 FAIL (106 REVIEW), December 0 FAIL (94 REVIEW), structure rules 0 FAIL, capacity 0 CAPACITY FAIL.** Source digest and file counts are the first lines of every report. Every puzzle has exactly one answer from the independent checker, equal to the bank's. REVIEW lines are read by the author only (mostly three-number coincidences with long prose lines in `docs/`).
* `verify_bank.py --selftest`: 62 cases, 0 problems (88 kinds, solver and checker agree).
* `test_site.py` on a scratch preview build (`/dev/shm`): **446 checks, 0 failed**, including the flag-off checks first, answer formats "It is X" and "The answer is X" for all 366 puzzles, 7 puzzles with a code box at 390 px (no sideways scroll).
* `test_flag_off.py`: 15 checks, 0 failed; `--selftest` passes.
* Committed pages `website/mi_signup.html`, `website/level_pages/*.html` and `website/dist`: not modified.

## 8. What remains open

1. **An independent audit of the round-3 content** is still needed (the author checked with the verifier and two independent solvers, not with a second reader): hand-solve at least 15 per level, a 40-pair parent sample per level range, and the browser. About 70 puzzles are new this round, including 35 uses of new sub-structures.
2. **The verifier's text rules are heuristic.** They fail the four Highs in the self-test, but a frame that is not in the words is caught only through the taxonomy (retired list, maintained by hand). The skeleton check still keeps only question-ending chunks. 200 REVIEW lines are explained only by the author's reading.
3. **New sub-structures have been tested with one story each, at one level each.** The other levels of a multi-level sub-structure (for example `strategy.fake_coin` at Levels 3 to 6) are counted as usable but their stories are not written; the verifier may reject them when they are.
4. **Level 1 is still the thinnest level**: 73 usable (12 spare) after three retirements this round; a fourth or fifth frame found later in our books would still leave 70 or 71. Several L1 kinds are parameter-poor for six returns a year.
5. **M-7** (text answers at Levels 3 to 6 for the whole year), **M-9** (no level picker on the home page), `data-teaser-state` staying `loading` for up to 8 s after an instant failure (invisible), `website/dist/_headers` older than `build_site.py` (not a teaser matter), `L6-codingclub` names Scratch and Python (the level's subject), `L2-twonumbers` and `L3-lanes5` heavy for the age.
6. **The tree moves under the verifier.** Other agents edit `practice/`, `docs/` and the holiday lessons all the time; the digest in each report changes with them. The verifier must run again on the full tree just before each month is released (January first).
7. The year model models structure only (not answers, stories or frames).
8. January to October are not written. GO or NO-GO is the auditor's call after item 1; by the numbers, the structure gate (capacity, slack, flag-off test, widened verifier) is now met at every level.
