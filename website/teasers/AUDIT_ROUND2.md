# Independent audit, round 2: daily website teasers after fix round 1

Auditor: independent reviewer (did not trust `FIXES_ROUND1.md` or `AUDIT_SELF.md`; re-derived everything below). Date 24 Oct 2026.
Branch `claude/great-fermi-1hv4vc`. Scope: `website/teasers` (Nov and Dec 2026 banks, 366 puzzles, `taxonomy.json` 195 sub-structures, `verify_bank.py`, `teasers.js`).
Read-only except this file. Builds were made in scratch copies of the repo (`git archive HEAD`), never in `website/dist`.
Owner rules applied: TEASER-STRICT (a structure or sub-structure may repeat in a level at most once a quarter, with a different structure; new story AND new frame) and the later
owner decision L1L2-GAP60 (Levels 1 and 2 only: a sub-structure may return after at least 60 days with a new story and new numbers; Levels 3 to 6 keep TEASER-STRICT).

## Verdict

**The November and December bank is mathematically sound and the site code is safe, but it is not yet releasable on originality; and the plan for January to October does not work as written.**

| Area | Result |
|---|---|
| 1. Round 1 High and Medium items | **Mostly closed.** All five named near-copies are gone, brand, 2-cent coins, "years years", contrast, fetch behaviour, accessibility are fixed (verified). **Not closed**: the verifier's similarity test is too weak, and about 12 other puzzles are still near-copies of our own holiday, extension, catalogue or sasmo items (H-1 below). Some level-fit items remain (M-3). |
| 2. Hand-solved sample (106 puzzles, 15 to 19 per level, from the question text only; 82 of them are kinds from `kinds_more.py`; Nov 48, Dec 58) | **106 of 106 agree** with the stored answer (5 differ only in the display of money or a mixed number); every one has a single answer; worked explanations correct and kind. |
| 3. Taxonomy | **Not 195 distinct structures in a parent's eyes.** Many sub-structures are siblings (see section 3). My estimate of what a parent would call distinct: about 40 to 45 of Level 1's 61, 55 to 60 of Level 2's 80. Some level ranges are too generous. |
| 4. Similarity | The verifier shows 0 FAIL, yet my own read finds **5 puzzles that repeat our own item's story and frame** and about 8 more at Medium. |
| 5. Browser | **Pass.** 431 of 431 builder checks reproduced; my own 70 checks plus 438 layout checks: no failure of the site. Flag-off pages byte-identical, `website/dist` untouched. Low items only. |
| 6. Capacity | **High.** The capacity table in `STRUCTURE_REPORT.md` overstates every level, and the "no answer repeated inside a level" rule makes 365 puzzles impossible at Level 1. Details and a proposal in sections 6 and 7. |

Severity counts: High 3, Medium 9, Low 10.

---

## 1. Round 1 items: really closed?

Spot checks (my own greps on the bank text, hint and explanation of all 366 entries, plus reading the replacements):

| Round 1 item | Status | Evidence |
|---|---|---|
| H-2 `L3-riddle21`, `L4-riddle52`, `L1-marbles`, `L3-uncle`, `L6-dice10` | **Closed** | None of these ids exists. Replacements: 12-01 L3 `L3-ricebag` (unit conversion), 11-29 L4 `L4-evens4` (four consecutive evens), 11-10 L1 `L1-think8`, 11-04 L3 `L3-fatherage`, 12-25 L6 `L6-quizmean`. **But** `L1-think8` ("I double it, then I add 3") is the same operation pair as the P6 parent text "I think of a number, double it, add 3 and get 17" (`p6/parent_side.json`) and `L3-fatherage` is the sasmo draft frame "father is 4 times as old" (Low). |
| H-1 December re-uses November's kinds | **Closed for the two months**: every level has 61 distinct `sub` ids; max 3 of a family. The "3 per family per quarter" cap is itself questionable (M-1). |
| M-1 "years years" | Closed (no doubled word in any text; `0 0` in a binary string is the only regex hit). |
| M-2 Milo | Closed (`L1-toast` is now "hot chocolate"). The only trademarks left are "Scratch" and "Python" in `L6-codingclub`, the Level 6 page's own subject (Low). |
| M-3 2-cent coins | Closed. Only 5, 10, 20, 50 cent and $1; `L3-round350` says "1 cent" as a price, not a coin (Low). |
| M-4 level fit | **Partly closed**, see M-3 below. |
| M-5 close to our own drafts | **Not closed**: the old list is gone, but new ones appeared (H-1). |
| M-6 7-word rule | Closed (verifier uses 7). Reproduced: 0 FAIL, 38 and 28 REVIEW lines. |
| M-8 contrast | Closed. Measured by me: light hint 5.36:1, light worked answer 5.77:1, dark hint 5.04:1, dark box 11.3:1. |
| M-9 fetch | Closed: two newest months are built into the page; others fetched; late reply used. |
| L-1 to L-8, L-10, L-12 | Closed (hints no longer contain answers by regex; the only regex hit is `L3-round350`, where "10" is a rounding unit, not the answer). L-9 (no early hint) and L-11 (device clock) remain open by design. |

### H-1 (High) Near-copies of our own material that the verifier does not catch

`verify_bank.py` compares *masked skeletons* (every content word becomes `_`) and needs score 0.6 with 2 or more shared numbers. So a puzzle with the **same story and same frame** but different numbers passes.
I compared the content words of every question with 20,515 source question chunks (the verifier's own file list, including the private papers and `school/`). The 20 closest, with my judgement:

| # | Teaser | Source | Judgement |
|---|---|---|---|
| 1 | `L2-trirow` (11-02) "row of triangles with lolly sticks. One triangle uses 3 sticks. Two triangles joined side by side use 5. How many sticks do **8** triangles use?" | `docs/books/p2_non_routine_catalogue.md` EX-PAT-1 "Sticks make triangles in a row. 1 triangle uses 3 sticks, 2 triangles use 5 ... How many sticks do 8 triangles need?" (answer 17) | **High: same question, same numbers, same answer.** (`L1-sticks`, squares 4 and 7, is the same frame at L1: Medium.) |
| 2 | `L2-snailwall` (11-10) snail, 20 cm wall, up 5 down 2, which day | `hp/Math_Inquirers_P1_Question_Bank.html` G5: snail, 9 cm wall, up 3 down 1, which day | **High: same story and structure.** |
| 3 | `L6-clockhours` (12-11) "It is 8 o'clock. What time will the clock show 103 hours from now?" | `p6/content/l10.js` "It is 9 o'clock. What time will a 12-hour clock show 100 hours from now?" | **High: same stem.** |
| 4 | `L4-yearlater` (12-16) "Today is Wednesday. What day of the week will it be 365 days from today?" | `p6/content/gaps.json` "Today is Wednesday. What day of the week will it be in 100 days?" | **High: same stem and day.** Also `L3-friday100`, `L6-days500` use "Today is <day> ... N days" (sasmo g2 "Today is Friday ... 30 days"). |
| 5 | `L5-jacket` (11-28) "A jacket costs $120 ... 15% off. What is the sale price?" | `p5/content/l7.js` "A fan costs $120 ... sold at 15% off" | **High: same price and rate, same frame.** |
| 6 | `L3-cartons` (12-04), `L2-penboxes` (11-18), `L4-stationery` (12-20) "A shop has 2 cartons of 1000 ..., boxes of 100 ..., loose ..." | `extension/data/l3_u01.json` "A shop has 3 boxes of 1000 pins, 14 packs of 100 pins and 6 loose pins" | Medium: same story and frame at three levels. |
| 7 | `L3-froginwell` (frog at the bottom of a well, up 4 down 3) | `extension/data/l1_u05.json` frog in a well, 12 steps, up 4 down 2 | Medium: same story. |
| 8 | `L1-fewestcoins`, `L2-fewestcoins`, `L3-fewestdollar` ("pay exactly N cents ... 5, 10, 20, 50 cent coins, fewest") | `extension/data/l1_u06.json` "Ben wants to pay exactly 75c ... 5c, 10c, 20c, 50c ... fewest coins" | Medium: same frame at three levels. |
| 9 | `L4-fivecards` (smallest odd number from 4,0,7,2,9), `L3-cards3096` (smallest even) | catalogue EX-LIST-1 "cards 0,5,7,8 ... smallest 4-digit odd number" | Medium. |
| 10 | `L3-ropestring` "rope 3 times as long as a string, 84 cm longer" | `docs/sasmo/g2_original_problems_draft.md` 15.3 "long piece 3 times ... 90 cm longer" | Medium: same structure, nearly the same numbers. |
| 11 | `L3-pizzaeaten` (Mei Ling 1/4 + Ben 3/8 of a pizza) | `p5/content/l2.js` "Siti ate 1/2 of a pizza and Ben ate 1/4" | Low to Medium. |
| 12 | `L1-outfits` (3 T-shirts, 2 shorts) | sasmo g4 10.2 "3 shirts ... 4 pairs ..." | Low to Medium. |
| 13 | `L1-reading` "starts reading at half past 3 ..." | `hp/qbank_skills.json` "Mei starts reading at 4:00 and stops at half past 4" | Low. |
| 14 | `L2-squares33`, `L1-squares22` (squares of every size) | catalogue "A big square is made of 2 rows of 2 small squares" | Low. |
| 15 | `L1-pyramid` (bottom 3, 8, 9) | sasmo g2 11.4 number pyramid | Low (generic). |
| 16 | `L5-rects43` (rectangles in a grid) | `p3/qbank_skills.json` "window 3 panes across" | Low. |
| 17 | `L5-frogsteps` (1, 2 or 3 steps) | `p5/content/inv.js` "Ali climbs a staircase ... 1 step or 2" | Low. |
| 18 | `L4-clockfive` (angle between clock hands) | `p6/qbank_skills.json` same skill | Low. |
| 19 | `L1-think8` | `p6/parent_side.json` (see above) | Low to Medium. |
| 20 | `L6-sixfactors` | private paper "exactly six factors, 3 and 9" | Low. |

Rows 1 to 5 break "new story AND new frame" outright. Fix: replace them with new stories on structures the sources do not use, and add a **content-word check** to `verify_bank.py` (share of the teaser's content words found in one source chunk of 0.8 or more with one shared number, or a shared noun-plus-verb story such as "snail ... wall", "frog ... well", "lolly sticks ... triangles") listing hits for review.

---

## 2. Hand-solved sample (106 puzzles, none looked at before solving)

I picked 81 puzzles first (14 per level, 11 at Level 6; about 10 per level from `kinds_more.py`), solved each from the question text and shown code, then compared; then a second sample of 25 of the new kinds (4 to 5 per level). Level counts: L1 18, L2 19, L3 18, L4 18, L5 18, L6 15. By month: November 48, December 58.
Kinds included, among others: group counting, number pyramids (L1 to L5), solid faces, edges and vertices, climb-and-slip (L2, L4, L5), digit-card extremes, Venn counts (L1, L2, L4, L5, L6), turns and directions, line-ups and queues, equalising two amounts (L1, L2, L4, L5), cubes painted, time across midnight (L3, L4), permutations (L3, L4, L6), choose-k (L6), mean with a missing value, last digit of a power, while loops, Fibonacci-type rules, successive growth, ratio, integer sums, lock-code counting, regrouping bundles.

Result: **106 of 106 agree.** Uniqueness checked by enumeration where it is not obvious (drink logic `L2-drinks`: Ben only; `L3-petshop`: Dina only; `L5-queue5`: a total order, middle is Arjun; lock code 328 split by last digit; fewest coins 4 by exhausting 3-coin sets; climb and slip: first day or minute reached, not "after slipping"; `L4-robotramp` 9; `L5-wormpole` 14). The explanations are arithmetically right and kind ("Not yet", "Now ask: how do you know?").
Only wording points (Low): `L3-lanes5` (5 factorial, 120) is heavy for 8 years; `L4-podium` and `L6-podium10` are the same structure at two levels (allowed); the money answers show as `$6.80` while the stored plain answer is `6.8` (both accepted).

---

## 3. Taxonomy: distinct structures, level ranges

### 3a. Are the 195 sub-structures genuinely distinct?

195 is the number of sub-structure ids; per level only 61 (L1), 80 (L2), 102, 108, 109, 105 apply (many ids span levels). I read the Level 1 and Level 2 list in full and 42 pairs of puzzles from the bank (7 per level) that belong to the same family but to **different sub-structures**, which is exactly what the verifier treats as "different":

* **5 of 42 a parent would call the same puzzle**: `L1-ribbon` vs `L1-orangebags` and vs `L1-cupcakes` (three division stories), `L3-tables47` vs `L3-fivedollarnotes` (how many groups of 6 or of $5), `L4-bracketcalc` vs `L4-divcalc` (calculate a bracket expression), `L5-gstbill` vs `L5-jacket` (add or take off a percentage).
* **11 of 42 borderline** (same topic, small twist): `L1-ends37` vs `L1-samedigits`, `L2-stickershare` vs `L2-howmanymore`, `L2-tarts` vs `L2-sweetshare`, `L2-tarttray` vs `L2-jugs`, `L3-cartons` vs `L3-digitvalue6482`, `L4-grass` vs `L4-noticeboard`, `L5-sail` vs `L5-house`, `L5-juicesum` vs `L5-bottleshare`, `L6-upthendown` vs `L6-savingspct`, `L6-quizmean` vs `L6-removed`, `L6-program` vs `L6-whileloop`.
* 26 of 42 clearly different.

Sibling groups the taxonomy counts as separate sub-structures but a parent will see as one idea (my judgement):
Level 1: division (equal share, boxes needed, groups count), backwards and missing number (two_step, undo_double, missing_addend), pairs (pairs_to_total, pairs_with_sum, handshakes), bar-model comparison (sum_difference, equalise, compare, chain_more_than), digit cards (three), digit-counting (four), coins (coin_total, coin_ways, fewest), perimeter (two), money (change, total_cost), counting inclusive and exclusive, repeating pattern (cycle_at, cycle_count), time (clock_hours_on, elapsed).
Level 2 adds: `division` with leftover (4 subs), `digit_puzzles` (5 subs), `perimeter_area`, `moves`, `fractions`.
Level 3 to 6: `perimeter_area` (six subs, four of them swap area and perimeter), `order_ops` (five), `digit_cards` (five), `decimals` (four operations), `cubes.one_face` vs `cubes.unpainted_inside`, `percentage.gst` vs `percentage.discount`, `time.elapsed` vs `time.across_midnight`.
Counted that way, the number of ideas a child perceives as different is about **40 to 45 at L1 and 55 to 60 at L2**; at Levels 3 to 6 it is roughly 70 to 85. The verifier's family cap of 3 only partly offsets this.

Cross-level: the same frame appears at several levels in the same weeks (number pyramid at L1, L3, L4, L5; solid shapes at L2 to L5; fewest coins at L1, L2, L3; equalise at L1, L2, L4, L5; growing gaps at L1 to L6; digit-value gap at L1 to L5). TEASER-STRICT is "in a level", so this is allowed, but a child who moves up a level meets the same idea; note for the owner (Low).

### 3b. Level ranges against the MOE files

Checked against `docs/moe/syllabus_by_level.md`, `website/data/level_lessons.json` and the six level pages' blurbs. The `levels` list in `taxonomy.json` often names four levels for one idea (for example `[3,4,5,6]`), which is generous. Topics above the level in the **bank** (not only in the taxonomy):

* L1 (builds on P1; ages 6 to 8): perimeter of a rectangle or a regular shape (`L1-card42`, `L1-tile`; P3), squares of every size in a grid (`L1-squares22`), number of line-ups (`L1-lineup`), elapsed minutes across 90 minutes (`L1-reading`; P1 has only 1 hour or half hour), weekday arithmetic (`L1-lesson`), sum 1 to n (`L1-chairs`).
* L2 (builds on P2): fraction **of a set** (`L2-tarts`, `L2-sweetshare`, `L2-marbleswhole`; MOE puts it at P4), area with a corner cut out (`L2-floorplan`; P3), grid routes, arithmetic series.
* L3: rounding to the nearest ten or a hundred (`L3-round350`; MOE P4), permutations (`L3-lanes5`), rectangles in a grid and stair-step counting (enrichment, not syllabus).
* L4: order of operations with brackets (five subs; the MOE file puts it at P5, but the Level 4 page lists it), permutations (`L4-podium`), painted-cube counting (`L4-unpainted`).
* L5: matches the page list and P5 (percentage, rate, triangle area, volume, angle facts). 
* L6: primes, negative numbers, probability, binary, polygon angles are not primary syllabus, but the Level 6 page lists them, so they are on-page.
Fix round 1 correctly removed median, mode, ratio at L5 and polygon angles at L4/L5. The L1 and L2 items above remain. **Medium (M-3)**: the owner should confirm "up to one school year above the page list is acceptable for ages 6 to 9 daily puzzles", or L1 and L2 should drop perimeter, fraction-of-a-set, 90-minute durations and area cut-outs.

---

## 4. Similarity to holiday, term, extension, booklet and private sources

* Verifier (`verify_bank.py`, reproduced): November 0 FAIL, 38 REVIEW; December 0 FAIL, 28 REVIEW; structure rules 0 FAIL; `--selftest` runs.
* My own method (content words, all 20,515 chunks the verifier indexes, including `docs/books/private_*` and `school/`): the 20 closest are in section 1, with 5 High.
* Seven fixed website puzzles: the bank avoids their sub-structures (no `sequence.which_term` etc. in the bank). 
* Why the verifier missed them: the skeleton masks nouns and verbs, so the same story with other numbers does not score 0.6. A shared number is also required; changed numbers defeat it. There is no story-noun check.

---

## 5. Browser (Chromium via Playwright 1.56, scratch build with `MI_TEASERS=1`)

* `test_site.py` (builder): **431 checks, 0 failed**, reproduced on my scratch build.
* **Midnight rollover, 5 time zones** (Singapore, Honolulu, Kiritimati UTC+14, Kolkata UTC+5:30, New York), Levels 1 and 6, instants 30 Nov 23:59:59, 1 Dec 00:00:00, 31 Dec 23:59:59, 1 Jan 00:00:00, 31 Oct 23:59:59 and 1 Nov 00:00:00 SGT: **60 of 60 correct** (the puzzle id and date equal the Singapore date's bank entry; dates with no released month show the page's fixed puzzle with no date label). The label shows the Singapore date to a Los Angeles visitor. A page left open past midnight keeps the old puzzle and takes the new one on the next focus event.
* **Slow fetch / failure** (page rebuilt without its built-in months so the file must be fetched): late reply at 3 s is used; reply at 9.5 s is still used (after the 8 s wait, if the fixed puzzle is untouched); abort, 404, malformed JSON and an HTML 200 body each leave the fixed puzzle, no blank box, no error. (Low) the internal `data-teaser-state` attribute stays `loading` for the full 8 s after an immediate failure; not visible.
* **No JavaScript**: the fixed puzzle is on the page (home: the frog puzzle; Level 3: the remainder riddle).
* **Answer formats, all 366**: the stored answer and the shown form are accepted for every puzzle; 13 "wrong" hits were only trailing zeros (`9.10` = `9.1`), which is correct. Not accepted (Low, L-1): "It is 14" and "The answer is 14" for numeric puzzles (334 and 366 puzzles), `an odd number`, `odd number`, `the sum is odd`, `an even number` for the odd or even puzzles, `facing west`, `w`, `Ben orders the juice`, and `four and three eighths`; `0.75%` is accepted for 75%. A 6-year-old who writes "odd number" reads "Not yet".
* **Keyboard and screen reader**: Tab reaches the input and "Check" in 15 steps, Enter submits; 3 px focus ring on the input; `Your answer` label tied to the input; the message region is `role=status`, `aria-live=polite`; after "Show me how" focus moves to the explanation. Buttons 44 px high.
* **Contrast**: see section 1 (all at least 5.04:1, light and dark). 
* **Layout**: all 366 puzzles at 390 px plus 72 at 1280 px, in each case the right puzzle for its date, no horizontal scroll and nothing outside the box (438 loads, 0 bad). Screenshots read (390 light/dark, 1280): tidy.
* **Flag off**: `lp_build.py` and `level_pages.py` without `MI_TEASERS` reproduce `website/mi_signup.html` and all six `website/level_pages/*.html` byte for byte; `build_site.py` equals the committed `website/dist` (`diff -rq`: identical); `git status` clean for `website/dist` and `git diff origin/claude/great-fermi-1hv4vc -- website/dist` is empty. `site_enabled` is `false` in the manifest.
* Noted for release: from 1 Jan until January's batch exists every visitor sees the fixed puzzle (honest, no label); the bank recycles by date, so each child sees the same puzzle on the same date next year (state this to the owner).

---

## 6. Capacity, and the rule changes the owner decision needs

### 6a. The capacity table is wrong (High, H-2)

`verify_bank.py::capacity_lines` computes `min(subs, 3 x families)`. The true number of puzzles one level can show in a quarter with 1 per sub and 3 per family is `sum over families of min(3, subs in family)`:

| Level | Subs | Families | Builder's "can fill" | **True, cap 3/family** | **True, if "repeat at most once" means cap 2/family** | Days in a quarter |
|---|---|---|---|---|---|---|
| 1 | 61 | 33 | 61 | **61** | 55 | 90 to 92 |
| 2 | 80 | 35 | 80 | **77** | 64 | |
| 3 | 102 | 41 | 102 | **88** | 73 | |
| 4 | 108 | 44 | 108 | **90** | 76 | |
| 5 | 109 | 46 | 109 | **94** | 79 | |
| 6 | 105 | 50 | 105 | **99** | 81 | |

So under the builder's own rules Levels 3 and 4 are also short (88 and 90 against 91 or 92 days in Q2 to Q4); only L5 and L6 fit. `FIXES_ROUND1.md` says "Levels 3 to 6 can cover a quarter". It cannot.

**M-1 (Medium) Interpretation of TEASER-STRICT.** "A maths structure/sub-structure may repeat in a level at most once a quarter, and only with a different structure" can be read as: a **family** appears at most twice a quarter (the original and one repeat), the repeat being a different sub-structure. The builder allows a family 3 times per quarter. Ask the owner which reading is meant; under the stricter reading every level is short (table, last column).

**M-2 (Medium) Quarter boundary loophole.** The cap is per calendar quarter, so a sub-structure used on 31 Dec may be used again on 1 Jan, 31 Mar and 1 Apr, and so on. Add a minimum gap across quarters (for example 30 days) for Levels 3 to 6.

### 6b. A second rule makes 365 puzzles impossible at Level 1 (High, H-3)

`structure_rules` fails any non-single-digit answer that repeats **anywhere in the level** (all released months), and a single-digit answer more than 4 times. At Level 1 (numbers to 100, many answers 2 to 9) that bound is about 8 x 4 = 32 single-digit answers plus roughly 90 values from 10 to 100 plus some text answers: **about 150 distinct answers in all, against 365 puzzles.** In Nov and Dec already 26 of the 61 L1 answers are single-digit (43%); a year at that rate needs 157 against a limit of 32. Level 2 is tighter than it looks too (15 of 61 single digit, most below 700). So the answer-uniqueness rule must become windowed (see 7), or L1 cannot be completed. (This also shows why a plan "write 31 more L1 sub-structures" would not by itself have worked.)

### 6c. Judging the GAP60 decision for Levels 1 and 2

Arithmetic: on a circle of 365 days (the bank recycles by calendar date, so the gap between 31 Oct and 1 Nov of the next year counts) a sub-structure with at least 60 days between uses can appear at most floor(365/60) = **6 times a year**. 365 puzzles therefore need at least ceil(365/6) = **61 sub-structures**.
* **Level 1 has exactly 61: zero slack.** The only feasible calendar is a rigid rotation: the Nov to Dec order of 61 structures repeated every 61 days (Jan 1 must reuse Nov 1 or Nov 2's structure, etc.), six cycles minus one day. Remove one sub-structure for syllabus reasons (for example perimeter, line-up, squares in a grid, elapsed minutes, which section 3b recommends) and 365 days cannot be filled. Every L1 structure then returns every 61 days, six times a year.
* **Level 2 has 80: 19 spare**, enough, but the family cap must be re-set (below).
* "Honest and acceptable for 6 to 8 year olds?" Spaced return of the core ideas (counting on, groups, change, pairs, odd and even) every two months, each time in a new story with new numbers and a new answer, is sound practice for that age and not something a parent should object to **if it is described truthfully**. What a parent would perceive is different: because L1 has only about 40 to 45 ideas they would call different (section 3a), a returning child meets "a number of equal pieces cut from a ribbon, boxes, bags" three times a month and the same *order* of ideas every two months. That is acceptable only when (a) wording on the site says "a new puzzle every day", never "a new kind of puzzle every day", (b) no two sibling sub-structures fall within 20 days of each other, and (c) the story and the numbers really differ (the answer must not repeat within 60 days either).
* The 60-day gap alone does not stop twins: `division.equal_share`, `division.boxes_needed` and `division.groups_count` can sit on consecutive days under it. The gap must also apply to **families** (a family at most 3 times in any 60-day window; consecutive days never from one family).

### Exact rule change for the fixer (do not apply from this audit)

In `taxonomy.json` / `taxonomy.py` / `verify_bank.py::structure_rules`:

1. `rules`: add `"min_gap_days": {"1": 60, "2": 60}`; for levels 1 and 2 **do not** apply `max_per_sub_per_quarter` (it would contradict the decision); for levels 3 to 6 keep `max_per_sub_per_quarter` = 1 and add `"min_gap_days_across_quarters": 30`.
2. For L1 and L2, for each sub, collect every use as a day number from `MM-DD`. Fail if two uses are closer than 60 days **circularly**, using both the 366-day (leap) and the 365-day (no 29 Feb) year: `d = abs(a-b); d = min(d, N-d); d >= 60` for N = 365 and N = 366, so 28 Feb to 1 Mar of a non-leap year is counted.
3. Replace `max_per_family_per_quarter` for L1 and L2 with: at most 3 uses of a family in any 60 consecutive days (circular), and no family on two consecutive days; keep 3 per quarter for L3 to L6 (or 2 if the owner reads TEASER-STRICT strictly).
4. Answers: replace "a non-single-digit answer may not repeat in the level" by "an answer may not repeat within 60 days (circular), and a single-digit answer at most twice in 60 days", for L1 and L2 (the full-year rule is infeasible, see 6b). For L3 to L6 keep the full-year rule but compute feasibility (see 5).
5. `capacity_lines`: replace `min(len(subs), 3*len(fams))` by `sum(min(cap, n_f))` over families; report for each level `floor(365/gap)` uses per sub, the required `ceil(365/uses)`, and the slack; print FAIL when slack is below 10 (L1 needs 71 or more sub-structures).
6. `--selftest`: add probes: a sub at day d and d+59 fails, d+60 passes, 31 Oct and 1 Nov of the next year (circular) fails if 59 apart, 28 Feb and 1 Mar (365-day year) is counted; a family twice on consecutive days fails; the same answer 59 days apart fails and 60 passes.
7. `build_bank.py` must place structures with the gap in mind (a 61-cycle at L1), and the number of new L1 sub-structures must be at least 10 to give slack.
8. Add the content-word story check from section 1 (H-1) to the verifier.

---

## 7. How to fill January to October for L1 and L2 most honestly

Under TEASER-STRICT as first written (1 per quarter) L1 needs about 31 more sub-structures and L2 about 15 (the true shortfall; 12 in the builder's table). The owner has chosen the gap rule instead. My recommendation, in order of how well it keeps quality:

1. **Add genuinely new sub-structures from the MOE P1 to P3 lists, not twins.** Aim for at least 10 more at L1 (so 71 or more, slack 10) and 10 more at L2. Candidates not yet in the taxonomy (each is a different idea, from the cited syllabus): L1: ordinal position "first to tenth", compare two sets (more, fewer), number line count on and back, fact families (3 + 5 = 8, so 8 - 3), adding three one-digit numbers, tell time to 5 minutes, am and pm, compare and order lengths in cm, which shapes make this figure, form a shape from pieces, one-to-one picture graph, skip counting by 2, 5, 10, odd or even number sentence, halves and quarters of a shape, days of the week and months in order. L2: classify 3D shapes (cube, cuboid, cone, cylinder, sphere), halves, thirds and quarters of a whole, compare unit fractions, add like fractions within a whole, compare three money amounts, mass in kg and g, volume in litres, convert hours and minutes to minutes (exists) and back, skip counting in 3s and 4s, multiplication facts for 2, 3, 4, 5, 10, number patterns with a multiplication rule. Several are easy; keep each as a puzzle with a twist (a trap or two steps), not drill, and have each pass the same hand-solve and brute-force checks.
2. **Let L1 borrow from L2 only for age-8 ideas that are within P3** (for example the 3D-shape facts and multiplication of 3 and 4), and remove the above-level L1 subs only if replacements exist; do not remove first.
3. **Apply GAP60 plus the family and answer-window rules in section 6** and a hard 71 or more sub-structures at L1, never 61.
4. **Do not pad with renamed twins.** A sub-structure that differs from an existing one only in the question word (for example a fourth division story) should not be counted toward capacity.
5. **Tell the owner plainly**: at L1 a structure will come back six times a year with a new story; the site should not claim "never repeats". Optionally publish L1 and L2 with a lower density (for example puzzles on weekdays only, and a different "this week's idea" label on weekends), which also halves the structure need, but that changes the promise of "every day" and is for the owner.
6. Keep the order of work: taxonomy entry with citation first, then `defs`, then `brute_more.py` checker, then the verifier; each month passes its own independent audit before release.

---

## 8. Findings list

| ID | Severity | Item |
|---|---|---|
| H-1 | High | Story and frame near-copies of our own items remain and the verifier cannot see them (`L2-trirow`, `L2-snailwall`, `L6-clockhours`, `L4-yearlater`, `L5-jacket`; Medium: cartons, froginwell, fewest coins, cards, ropestring); add a content-word check |
| H-2 | High | Capacity table overstates every level (true L3 88, L4 90, L2 77 with cap 3 per family); `FIXES_ROUND1.md` claim "L3 to L6 enough" is false |
| H-3 | High | Full-year "no repeated answer in a level" rule makes 365 puzzles impossible at L1 (about 150 distinct answers available) and tight at L2; must be windowed |
| M-1 | Medium | TEASER-STRICT reading: family cap 3 per quarter vs "repeat at most once"; needs owner confirmation |
| M-2 | Medium | Quarter-boundary loophole (31 Dec to 1 Jan) |
| M-3 | Medium | L1 and L2 puzzles above the syllabus (L1 perimeter, line-up, 90-minute duration; L2 fraction of a set, area cut-out); L3 rounding; owner policy needed |
| M-4 | Medium | Sibling sub-structures counted as distinct (perceived distinct about 40 to 45 at L1, 55 to 60 at L2); 5 of 42 sampled pairs are the same puzzle to a parent |
| M-5 | Medium | GAP60 at L1 has zero slack (61 of 61); one removed sub breaks 365 days; add 10 or more genuine sub-structures; gap must also bind families and answers |
| M-6 | Medium | `L1-think8` shares its operation pair with a P6 parent text; `L3-fatherage` and `L3-ropestring` close to sasmo drafts |
| M-7 | Medium | Verifier's skeleton check is blind to story (explains H-1); `verify_bank.py` capacity text still says one use per quarter |
| M-8 | Medium | The bank recycles by date: the same puzzle on the same date every year; state in the owner decision |
| M-9 | Medium | Ages 6 to 8 "Ages" scope: Jan to Oct 2027 dates show the fixed puzzle until written; the home page has no level picker (always Ages 6 to 8) |
| L-1 | Low | Answer formats not accepted: "It is 14", "The answer is 14", "odd number", "an even number", "facing west", "w"; `0.75%` accepted for 75% |
| L-2 | Low | `data-teaser-state` stays `loading` 8 s after an immediate fetch failure (not visible) |
| L-3 | Low | Late reply after 8 s is still used (README says up to 8 s); harmless, document it |
| L-4 | Low | Trademarks "Scratch" and "Python" in `L6-codingclub` (subject of the level page) |
| L-5 | Low | `L3-lanes5` 120 orderings heavy for age 8; `L4-podium` and `L6-podium10` repeat the idea across levels |
| L-6 | Low | Same idea at many levels in the same weeks (pyramid L1, L3, L4, L5; equalise L1, L2, L4, L5; fewest coins L1 to L3) |
| L-7 | Low | `L3-round350` says "1 cent" (price, not a coin); fine but use "a price of 1 cent" wording check |
| L-8 | Low | `L1-chairs` and `L2-stickerbook` sum structures above the level |
| L-9 | Low | No early "Need a hint?" button (carry-over L-9 of round 1) |
| L-10 | Low | Device clock decides the day (carry-over L-11) |

Not found: any wrong answer, any non-unique answer in the 106 solved, any cookie or storage, any third-party request, any change to `website/dist`, any coin or note image, any American spelling in the bank, any brand name beyond Scratch and Python.

Note: while working I overwrote a leftover scratch file `/tmp/claude-0/s/sim.py` (a temp folder, not part of the repo).
