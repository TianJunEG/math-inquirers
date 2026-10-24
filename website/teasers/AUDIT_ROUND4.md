# Audit round 4 of the daily teasers (after fix round 3)

Independent, read-only audit of `website/teasers/` on branch `claude/great-fermi-1hv4vc` (HEAD 4373f86, teaser files unchanged since 8aa6c5b), 24 Oct 2026.
Nothing in the repo was edited except this file. All builds, verifier runs and browser tests ran on copies under `/dev/shm`. `website/dist` was never touched.
Method: my own code (not the builder's) for the near-copy screen, the year check and the browser checks; the builder's verifier and tests were only re-run, never trusted.

## Verdict

**NO-GO to release the current Nov and Dec bank. CONDITIONAL GO to start writing January, but only after conditions C1 to C6 (section 8) are met.**

Why: the structure side is now sound and reproducible (year model, rotation, flag-off, browser, answers: all pass, my own code agrees with the builder).
The originality side is not closed: my own screen found **4 High** near-copies of our own books (identical numbers or identical sentence, answer given in our books) that the widened verifier did not report,
about 15 Medium frame-level overlaps with our books, 11 same-level pairs a parent would call the same puzzle, and 11 items above the MOE level.
All 96 hand-solved puzzles are correct and unique, and the explanations are kind, with one wrong explanation sentence (L6-temps).

## Summary table

| # | Task | Result |
|---|---|---|
| 1 | Near-copy screen, own code, whole tree incl. PDFs and private sources | **4 High, ~15 Medium** missed by the verifier (section 1) |
| 2 | Hand-solve 96 puzzles (16 per level, 60 of them written or rewritten in round 3) | 96/96 agree with the bank, all unique; 1 wrong explanation sentence; 2 identical-number pairs across levels (section 2) |
| 3 | Level fit vs MOE files | 11 items above level, 2 weak citations (section 3) |
| 4 | Taxonomy honesty: 240 same-family pairs, 20 multi-level sub-structures | about 5% "same puzzle", another 10% "very close"; 6 multi-level subs reuse one story at 3 or 4 levels (section 4) |
| 5 | Year model, own circular check | agrees with the builder; L1 survives losing 2 (and 3) sub-structures (section 5) |
| 6 | `verify_bank.py` twice with different `PYTHONHASHSEED`, source lock | reproducible; lock works but is loose (section 6) |
| 7 | Browser spot check on a scratch build | pass (section 7) |
| 8 | GO / NO-GO | section 8 |

## 1. Near-copy screen with my own code

Corpus: every text-like file in `outputs/ docs/** practice/** school/** split/ rebuild/ hp p2..p6 term extension deck diag levels tutor portal website (without teasers, dist, preview)`,
including `docs/books/private_*` (jsonl, tsv, md, py), **and the text of every PDF** (about 6,500 files, 397,000 sentences). The builder's verifier reads only `.md .txt .json .js .py .html .csv` (3,818 files) and so never sees the PDFs.
Rules (own code): content-word skeleton (names, stop words, numbers removed, IDF-weighted overlap of 0.5 or more), shared non-trivial numbers (0.5 or more of the question's numbers), masked four-grams with numbers replaced (3 or more shared), on windows of 1, 2 and 3 sentences.
This flagged 219 of 366 puzzles as candidates; I read the top 130 against their source text. Most are generic (clock angles, "how many factors", perimeter). The real ones are below.

### High (identical numbers or identical sentence to our own books; the verifier gave no FAIL and no REVIEW)

| Puzzle | Source in our own material | Why it is a copy |
|---|---|---|
| `L1-fanlines` (23 Nov, 3 lines, 10 triangles) | `outputs/workbook/Math_Inquirers_P1_Student_Workbook_Designed.pdf` p38 Go further C1 and `split/l7/project/slides/l7-challenge.html`: "A big triangle has lines drawn from its top corner to the bottom. With 1 line there are 3 triangles, with 2 lines 6, with 3 lines 10. How many with 4 lines?" | same figure, same number of lines, same answer (10); `L4-fanten` (9 lines, 55) is the same frame again |
| `L3-grid33` (26 Nov, 3 by 3, every square, answer 14) | `tutor/data/p1l7.notes.json` "Squares 3 across and 3 down ... 9 + 4 + 1 = 14"; frame also in `split/l7`, `split/p2l8` ("squares in a grid 4 long and 3 high") | identical figure and answer |
| `L3-flagstrip` (14 Dec, red, red, blue, green; 30 flags) | `p2/Math_Inquirers_P2_Tutor_Guide.html` Workbook Think harder 2: "Beads go red, red, blue, green ... the 30th bead" | identical colour string and the same 30 |
| `L3-fourtiles` (12 Dec, 4 squares edge to edge, answer 5) | `split/l7/.../l7-key.html` "Turning or flipping a shape does not make a new shape"; P4 Question Bank and P4 workbook "There are 5 different shapes made of 4 squares joined edge to edge" | near-identical sentence and our books state the answer 5 |

### Medium (same frame as our books, other numbers, or the same story repeated across levels)

- `L2-cubestack` (6 layers), `L3-cubetower` (7), `L5-cubetower9` (9): one story at three levels (1 + 4 + 9 + ...), and the frame of `rebuild/skill_items_l1_3.py` and the L2 Skill Additions tutor sheet ("The top layer is 1 cube. The next layer is 2 rows of 2"). The verifier flagged them as REVIEW (rule C) and they were left.
- `L1-fourcoins`, `L2-fivecoins` ("he picks some coins: how many different totals"): frame of `extension/l4/src/u10.py` item S02 and `docs/audit/gifted_p1.md`. `coins.make_amount` was retired for the same reason, `coins.amounts_made` was not.
- `L4-chesssquares`, `L4-rects33`, `L5-rects43`, `L3-ladder`: counting in a grid (`split/l7`, `split/p2l8`, `term/l1/lessons/l36`).
- `L3-mrtsteps`, `L4-floorstrip`, `L5-frogsteps`, `L6-tiles13`: 1-or-2-step stairs frame, which is in the P5 workbook (Ali climbs a staircase 1 or 2 steps) and the L6 extension.
- `L2-deliveryrobot`, `L3-robot`, `L4-puddle`, `L5-blockedroute`, `L6-detour`: grid routes with one blocked point: `term/l1/lessons/l33` "Count the Routes" and the SASMO g2 draft ("3 steps right and 2 steps down"). `L4-puddle` and `L6-detour` are the same puzzle (3 right 3 down, one point closed, answer 11 for both).
- `L5-diagline` (rectangle diagonal), `L4-jellycube`, `L5-cube4`, `L6-hiddencubes` (painted cube): `split/p5l4/.../p5l4-check.html`, `extension/data/l5_u05.json` (L5U05-T01 "A big cube is made of small cubes ... 64 have no paint"), `outputs/extension/L2` and `L5` workbooks.
- `L4-palyears`, `L5-palin5`: palindromes: P4 and P5 Question Banks ("How many 5-digit palindromes between 40 000 and 50 000").
- `L1-machine1`, `L2-machine3`, `L6-machine3`: number-machine frame. Round 3 retired `function_machine.find_the_rule` because of the P2 tutor guide, SASMO drafts and the P6 Algebra Machines book, and replaced four machine puzzles, but these three stay and `L6-machine3` is the Algebra Machines frame.
- `L2-bookcase` (7 drawers of 9, take 5, 58) and `L3-bakery` (7 boxes of 9, 5 thrown away, 58): identical numbers and answer at two levels (and L3-bakery is Primary 2 content).
- `L2-stadiumrows` and `L4-theatrerows`: rows of seats growing by 3, summed; `L4-noticeboard` and `L5-fieldwidth`: perimeter and one side, find the other; `L3-keyholder`, `L4-fourclaims`, `L5-ballholder`, `L6-keyclaims`: one story (who has the key, card, ball) at four levels.
- `L6-sixfactors` (smallest number with exactly 6 factors) is only generic overlap with `practice/holiday/p6/02`; no action.

**Why the verifier missed them (Medium, tooling):** it reads no PDFs; it compares sentence windows only, so a 2 or 3 sentence source (fan with "3 lines is 10") shares few content words with a re-worded stem; and it has no rule that
"all numbers of the question found in one source window plus the same figure". Its `source_lock.json` demands only 36 files from `term` (2,203 text files exist), so a checkout missing most of `term` still passes (section 6).

## 2. Hand-solved sample (96 puzzles, from the question text only)

16 per level, random, stratified; 60 of the 96 are in the 76 puzzles named in FIXES_ROUND3 as written or rewritten in round 3 (L1 10, L2 10, L3 10, L4 10, L5 10, L6 10; above the 35 required). I solved each by hand (a calculator for the larger products) and only then compared with the bank.
Figure items (L3-sticksdisplay, L4-mirrorgrid, L4-cubenet, L6-program, L6-evenodd) were solved from the text figure that the page shows.

- **96 of 96 agree with the bank answer and each has exactly one answer** (including the new structures: pencil lifts 2 and 3, Josephus circle 4, ferry crossings 13, diagonal squares 32, three clubs 16, fewest swaps 6 and 9, chessboard edge 33, net opposite D, mirror grid 5).
- Explanations: all arithmetic is right; hints do not give the answer; the tone is calm and kind ("Not yet", never "wrong").
- **Medium, explanation wrong:** `L6-temps` says "The changes from month to month are 5, 29, 3, 8, 2 (the signs are ignored)" and then asks for the biggest rise. The changes are +5, +29, -3, +8, -2; as written a child can read 3 and 2 as rises. Rewrite.
- Low: `L1-counterbox` and `L1-hiddensum` explanations state the answer before deriving it ("The red counters number 34 ..."; "Check 46 + 25 = 71").
- Low: `L5-sunflowerfall` id says sunflower but the text is a tree (id only).
- Cross-level: see `L2-bookcase` = `L3-bakery` above.

## 3. Level fit against `docs/moe/syllabus_by_level.md` and the 38 new sub-structures

Flag = above the level's MOE content or an unsupported citation. (Enrichment may be a choice, but the README promises topics "only from that level's syllabus".)

| Severity | Item | Problem |
|---|---|---|
| Medium | `L4-calc` (`order_ops.evaluate` at L4 and L5) | MOE: order of operations is P5; the sub allows L4 |
| Medium | `L1-swimbike` (`sorting.overlap_both` at L1) | two-set inclusion-exclusion (50, 45, 40) at ages 6 to 8 |
| Medium | `L5-threeclubs`, `L3-clubs` | three-set and two-set inclusion-exclusion; the cite is "Problem solving" only |
| Medium | `networks.draw_without_lifting` (`L3-pencildrawing`, `L6-cubeedges`) | odd-vertex parity argument at ages 8 to 10; the cite (P2 Geometry) does not support it |
| Medium | `counting_grid.diagonal_squares` (`L5-diagline`) | w + h - gcd is not MOE; the cite (P4 factors) is weak |
| Medium | `strategy.fake_coin` (`L4-fakecoin`, `L5-fakecoin5`, `L6-coinbound`) | powers of 3 by reasoning; the cite is P3 multiplication |
| Low | `L1-campdays` (`calendar.weeks_and_days` at L1) | 4 weeks 5 days needs 7 times 4 (P3 table of 7); `L2-sevens` also counts in 7s |
| Low | `L3-missednumber` (Gauss pairing at L3) | pairing 1 + 24 is a P5 idea; the hint gives it |
| Low | `L4-gainingclock` | a 65 : 60 proportion at ages 9 to 11 |
| Low | `L5-busdistance`, `rate.speed_distance` at L5 | `docs/moe` says speed is not in the syllabus anywhere (fine at L6) |
| Low | `L1-rpsgames` (45 pairs), `L1-whichsun` (three unknown symbols), `L2-stadiumrows` (ten-term sum) | heavy for the level; fine with the hints |

Round-3 level-fit moves checked and fine: rounding starts at L4; `money.unitary_price` from L3 (decimal money); `fractions.whole_from_part` from L4; `counting_pairs.handshakes` stops at L5; perimeter from L2; durations over one hour from L2.
The other new sub-structures cite a real MOE row and sit at or one level above it (fractions.unit_compare, perimeter_area.notched_perimeter, triangle_area.cut_corners, symmetry.complete_figure, shapes.cube_net_opposite, averages.combined_groups, ratio.ratio_changes, fractions.share_fraction, series_sum.missing_term at L5).

## 4. Taxonomy honesty

**240 same-family pairs (40 per level, random seed 11).** Reading both stems, my judgement: "a parent would see the same puzzle" = 11 pairs (about 5%), "very close" = 17 (about 7%), the rest different ideas.
Same puzzle: `L1-cousindays` and `L1-swimcourse` (6 days apart, count the days from the Xth to the Yth); `L2-schoolbus`, `L2-mooncakes`, `L2-thinknumber` (divide by 4 or 5 with a remainder, 11-10, 11-21, 11-29);
`L3-erasers` and `L3-fairtables`; `L4-rects33` and `L4-chesssquares` (and `L4-fanten`, 12-25 and 12-29); `L5-fishtank` and `L5-cubes` (box volume, 4 days apart); `L5-threeclubs` and `L5-schooltwo` (overlap sets);
`L6-stickerratio` and `L6-redblue` (ratio changes when something is added); `L6-nested` and `L6-program` (trace a loop). Very close: `L4-eggtrays30`/`L4-nametags`, `L5-pct35`/`L5-gstbill`, `L6-primes100`/`L6-pfsum`, `L2-flourgrams`/`L2-tworopes`, `L6-testmean`/`L6-quizmean`, and others.
Per level (same puzzle + very close): L1 1+2, L2 1+3, L3 1+2, L4 1+3, L5 2+2, L6 2+3. The family cap (3 per quarter or 60 days) is met, but the families are broader than "a parent's idea", so
the honest wording rule stands: "a new puzzle every day", never "a new idea every day". Division with remainder is still 3 subs (share, leftover, reverse) in one family, although README says the division look-alikes were merged.

**20 multi-level sub-structures (random seed 5), the story at every level it is used.** Fine (new story, new frame at each level): `fractions.arithmetic`, `bar_model.sum_difference`, `networks.shortest_route`, `division.share`, `bonds.part_whole`, `counting_choices.orders`, `perimeter_area.find_unknown` (but L5 is a P3 skill), `moves.ups_and_downs`, `growing_pattern.doubling`, `graphs.line_graph_biggest_change`, `spatial.turns_facing`, `digit_puzzles.count_by_digit_rule`.
Same story reused at the levels (Medium): `logic_truth.truth_tellers` (L3 classroom key, L6 spare classroom key, L4 library card, L5 football: one story at four levels), `series_sum.add_in_pairs` (L2 and L4 seat rows +3), `multiplication.groups` (L2 and L3 identical numbers),
`cubes.painted` (L4, L5, L6 same story), `counting_ways.stairs_steps` (L3 to L6 strip or stairs), `strategy.fake_coin` (L4 to L6 coins and a balance), `repeating_pattern.cycle` (L1 to L3 flags and stripes, with L3 a copy of a P2 item), `backwards.undo_steps` (L1 and L2 machine on the same date, 11-22).
README says 41 of 196 sub-structures appear at three or more levels (161 of 366 puzzles); I recomputed exactly that. It is a documented, allowed rule, but five or six of them are the same puzzle with larger numbers, which a family with two children would notice.

## 5. Year model, own circular check (`/dev/shm/aud/ym.py`, `ym2.py`; independent of `year_model.py`, `taxonomy.py`, `verify_bank.py`)

- **Levels 1 and 2:** I laid the 61 released sub-structures on the 12 calendar years 1 Nov 2026 to 31 Oct 2038 (leap and non-leap, 29 Feb handled by the date key) and checked every pair of uses: minimum gap 60 days, no gap under 60; family at most 3 in any 60 consecutive days; no family on consecutive days. 0 violations at both levels.
- **Survival:** a lost sub-structure must be replaced at all six of its slots by a spare whose family fits. L1 (12 spares) and L2 (36 spares): every single loss, every pair of losses (1,830 of 1,830) and 400 random triples can be re-filled; any 2 of all 73 (2,628 of 2,628) usable L1 sub-structures and any 2 of 97 (4,656 of 4,656) at L2. So **L1 survives losing 2** (and 3). The L1 spare pool is only 12, and it is the thinnest in parameter space: this is structure only, a spare still needs six new stories.
- **Levels 3 to 6:** my own integer program (HiGHS): one sub-structure per day on the 366 dates, once per calendar quarter, any 30 consecutive days at most once (circular, Dec to Jan included), a family at most 3 a quarter and not on consecutive days, released Nov and Dec fixed, the fixed-page sub-structure excluded. Feasible at all four levels. Losing 2, 6, 10 or 14 random unreleased sub-structures: feasible in every trial (36 of 36) except one L6 trial at 14 losses. Cap 2 is infeasible. This matches the builder's numbers.
- Caveats: structure only (not stories, answers, frames); capacity left in Q4 for October after Nov and Dec are fixed is tight at L1 (9 family-capped spares for 31 days, but L1 and L2 use the rotation, not the quarter rule). Text answers at L3 to L6 (about 30 distinct names, weekdays, shapes per level) are still not planned (M-7 open).
- The builder's `year_model.py` re-run in a scratch copy: "0 problem(s)".

## 6. `verify_bank.py` reproducibility and source lock

- Full tree copy under `/dev/shm`, run twice with `PYTHONHASHSEED=1` and `12345`: same digest `836f21d78b796af6`, both `0 FAIL, 106 REVIEW` (Nov) and `0 FAIL, 94 REVIEW` (Dec), `VERIFY_REPORT.md` for both months and `STRUCTURE_REPORT.md` byte-identical across the two runs (cmp). Reproducible.
- Source lock: removing `docs/books/private_p6_papers` gives exit 2 "INVALID VERIFICATION" (required source missing); removing `practice/` gives exit 2; removing `term/l1/lessons` gives exit 2. Works.
- Medium, loose: `source_lock.json` requires only 36 files from `term` and 211 from `practice`; deleting most of `term` (2,203 text files) would still pass. The 200 REVIEW lines are not triaged in any report. No PDFs are read (section 1).
- `test_flag_off.py` run on the real tree: 15 checks, 0 failed; `git status website` is empty; committed `mi_signup.html` and `level_pages/*.html` carry no teaser; `website/dist` untouched.

## 7. Browser spot check (scratch build with `MI_TEASERS=1` in a copy; Chromium via Playwright)

- The builder's `test_site.py` on my scratch build: **446 checks, 0 failed.**
- My own checks: (a) rollover from 4 zones (Pacific/Kiritimati, America/Los_Angeles, Asia/Kolkata, Pacific/Honolulu) at 15:59:50Z and 16:00:05Z on 14 Dec and 15:59:59Z and 16:00:00Z on 30 Nov, all six levels: **96 of 96 show exactly the Singapore-date puzzle**, 0 mismatches.
  (b) a page left open across midnight (3 zones, clock fast-forwarded 40 s): the old puzzle stays until the visibility/focus event, then the new day's puzzle appears. As the README says.
  (c) fallback: January date and a page with no month: fixed puzzle, no date label, no request for an unreleased month. (d) No JavaScript: all six pages show the fixed puzzle with its check or answer button.
  (e) answer formats typed into the real input for 36 puzzles (`60`, `60 bicycles`, `The answer is 60`, `It is 60 bicycles`, `$75.60`, `3,500,000`, `4 3/8 cups`, names): 36 of 36 accepted in all four forms.
  (f) 390 px wide, light and dark: no sideways scroll on any level page (scrollWidth 390), puzzle box 338 px, smallest text contrast 5.35 (light) and 5.9 (dark) against 4.5 needed, buttons and inputs 40 px or taller. Low: the smallest label is 13 px.
- Figures are text blocks (table, mirror grid with a bar, `[A][B]` cube net, code); they fit and scroll inside the box. `L4-cubenet` as a text net is hard for a 9-year-old (Low).

## 8. GO / NO-GO for January (2 batches of about 30 per level, audited before release)

**Recommendation: NO-GO for releasing the current bank; CONDITIONAL GO for writing January.** Writing may start once C1 to C3 are done; release of any month needs all of C1 to C6.

| # | Condition (exact) | Severity it closes |
|---|---|---|
| C1 | Replace `L1-fanlines`, `L3-grid33`, `L3-flagstrip`, `L3-fourtiles` (and `L4-fanten`) with new frames; retire `counting_grid.triangles_in_fan`, and the squares-in-a-grid and tetromino frames or keep them only with a frame our books do not have. Re-screen the whole bank. | High |
| C2 | Add to `verify_bank.py`: PDF text as a source; a rule "every non-trivial number of the question inside one 1 to 3 sentence source window, with 3 or more shared content words" as a FAIL; the "same figure" rule for the frames listed in section 1; raise `source_lock.json` minimums to at least 90% of the current counts (term at least 1,900). Make `--selftest` replay the four High items above. | Medium (tooling) |
| C3 | Owner rule for the cross-level and same-level repeats: no identical numbers at two levels (L2-bookcase/L3-bakery), no identical story at 3 or more levels (cube layers, key claims, machines), and a same-frame cluster (division with remainder, grid counting, box volume, overlap sets, ratio change, trace a loop) at most once per 30 days at a level. Apply to Nov and Dec and to the January plan. | Medium |
| C4 | Fix the level-fit list in section 3: move `order_ops.evaluate` to L5 and L6 only, move `L1-swimbike` to L3 or later, change or honestly cite `networks.draw_without_lifting`, `diagonal_squares`, `fake_coin`, `three_sets`; update `taxonomy.json` levels and the README counts. | Medium |
| C5 | Fix `L6-temps` explanation; give every January explanation a second reader; hand-solve 15 puzzles a level (new items first) before release, as in this audit. | Medium |
| C6 | Before release: re-run the widened verifier on the full tree, twice with different hash seeds; `year_model.py`; `test_flag_off.py`; the browser suite; then an independent screen like section 1 on the January batch. Keep Levels 1 and 2 on `YEAR_PLAN.md` and write the six-return pack (six stories and six number sets) for the thinnest L1 and L2 sub-structures (for example `logic_grid.latin_square`, `spatial.turns_facing`, `number_line.equal_marks`) first. | Medium |

Open and not blocking writing: text-answer planning at Levels 3 to 6 (M-7); the 200 REVIEW lines not individually closed; honest-wording rule for the site stays "a new puzzle every day".

## Severity list

- **High (4):** `L1-fanlines`, `L3-grid33`, `L3-flagstrip`, `L3-fourtiles` (identical numbers or sentence with our books, not reported by the verifier).
- **Medium (about 30 items):** frame-level overlaps with our books (cube layers, coin totals, grid counting, stairs, robot routes, painted cubes, palindromes, machines); identical numbers across levels (`L2-bookcase`/`L3-bakery`); same story at 3 to 4 levels; 11 same-level pairs a parent would see as the same; 11 level-fit items; `L6-temps` explanation; verifier blind spots (PDFs, number rule, lock minimums).
- **Low:** explanations that reveal before deriving (`L1-counterbox`, `L1-hiddensum`), `L5-sunflowerfall` id, 13 px labels, text-net cube diagram, heavy L1 and L2 items, text-answer planning, 200 untriaged REVIEW lines.
