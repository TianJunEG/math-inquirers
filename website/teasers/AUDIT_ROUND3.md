# Independent audit, round 3: daily website teasers after fix round 2

Auditor: independent reviewer (did not trust `FIXES_ROUND2.md`, `AUDIT_SELF.md` section 7 or the verifier's "0 FAIL"). Date 24 Oct 2026. Branch `claude/great-fermi-1hv4vc`, HEAD `2b438c1`.
Scope: `website/teasers` (Nov and Dec 2026 banks, 366 puzzles, `taxonomy.json` 184 sub-structures, `verify_bank.py`, `batches/YEAR_PLAN.md`, `teasers.js`).
Read-only except this file. All builds, the verifier run and the solver models ran in scratch copies under `/dev/shm` (a full copy of the working tree, including git-ignored private sources). `website/dist` was never touched.
Owner rules applied: TEASER-STRICT (L3 to L6), L1L2-GAP60 (L1, L2), TEASERS-365-MONTHLY (a year per level, released monthly, each month audited before release).

## Verdict

**NO-GO today for writing January to October. Conditional GO for Levels 2, 3 and 4 once the Highs below are fixed; Levels 1, 5 and 6 first need more sub-structures.**

| Area | Result |
|---|---|
| 1. AUDIT_ROUND2 High and Medium items | **Not all closed.** The five named near-copies are gone and the capacity numbers are now true. But the replacements contain **four new High near-copies of our own books** that the verifier does not see (H-1), the flag-off promise is broken in the repo (H-2), and Level 1 and Level 6 cannot absorb one failed sub-structure (H-3). |
| 2. Hand-solved sample | **133 puzzles solved from the question text only, 133 agree** (96 stratified, at least 16 per level, plus all 37 remaining puzzles of the 50 new sub-structures, so all 78 new-sub puzzles are covered; 184 of the 366 ids differ from the bank at commit 3ebccf0, which round 2 read). Every one has one answer; explanations are right and kind. Only wording slips (Low). |
| 3. Taxonomy honesty | Better than round 2: of 120 same-family pairs a parent would see **3 as the same puzzle, 38 as the same topic with a twist, 79 as different**. Counted strictly, L1 has about 61.5 distinct ideas (62 listed, 61 needed) and L6 about 97 (98 listed). The capacity table is honest only on that strict reading. |
| 4. Year plan | My own circular 365 and 366 day check: **0 violations** at L1 and L2. The L1 rotation survives **one** failed sub-structure (59 of 61 slots are rule-safe with the one spare) and **cannot survive two**. A solver model of the quarter rules shows **L6 fails if any single unreleased sub-structure is lost**. |
| 5. Level fit | Moved items are now placed correctly. A cluster at Level 2 is still one to two school years above (decimal money, division by 12, fraction of a set inverse). |
| 6. Browser | **Pass** for the site code (rollover 144 of 144, fallback, no-JS, contrast, 390 px). **Fail** for flag-off: the committed `mi_signup.html` and `level_pages/*.html` carry the teaser build (H-2). `git diff` of `website/dist` against origin is empty. |

Severity counts: High 3, Medium 7, Low 9.

---

## 1. AUDIT_ROUND2 items: really closed?

| Round 2 item | Status | Evidence |
|---|---|---|
| H-1 five named near-copies (`L2-trirow`, `L2-snailwall`, `L6-clockhours`, `L4-yearlater`, `L5-jacket`) and the 8 Medium | **Ids closed, problem not closed** | None of the ids named in AUDIT_ROUND2 section 1 (36 checked, with the Round 1 ones) is still in the bank, except `L5-rects43`, `L5-frogsteps`, `L4-clockfive`, `L6-sixfactors` (all Low there). **New** near-copies were written instead (H-1 below). |
| H-2 capacity table | **Closed** | I recomputed `sum over families of min(3, n_f)`: L1 62, L2 87, L3 103, L4 101, L5 95, L6 92. Same as `STRUCTURE_REPORT.md`. |
| H-3 full-year answer rule at L1 | **Closed** | Windowed rule is in `gap_rules`; L1 and L2 pass it. (L3 to L6 text answers are not tested for the year, M-7.) |
| M-1 family cap 3 or 2 | **Not closed** | Owner has not answered. With cap 2 the solver model is infeasible at L3, L4, L5 and L6 (section 5b). |
| M-2 quarter boundary | **Closed** | 30-day circular gap is in `quarter_rules` and my model enforces it. |
| M-3 level fit | **Partly closed** | Section 6. |
| M-4 sibling subs | **Closed in substance** | Section 4. (Doc says 39 merged subs absorbing 100 ids; the taxonomy has 41 and 102. Low.) |
| M-5 L1 slack | **Not closed** | Slack 1. The builder's own threshold is 10. `verify_bank.py` prints `CAPACITY FAIL Level 1`. |
| M-6 `L1-think8`, `L3-fatherage`, `L3-ropestring` | **Closed** | Ids gone. |
| M-7 verifier blind to story | **Partly closed** | A story check exists but misses four High items and its result depends on the repo state (M-4 below). |
| M-8 same date next year | **Closed** as documentation | README states it. |
| M-9 no level picker on home page | Not closed (out of scope) | Home page still shows the Ages 6-8 set. |

---

## 2. HIGH findings

### H-1 (High) New near-copies of our own books that the verifier does not catch

Method (my own, independent of `verify_bank.py`): I indexed **1.65 million one-to-three-sentence windows from 3,600 files**: holiday (`hp`, `practice`), term (`term`), extension (`extension/data`), school booklets (`school`, `p1` to `p6`), catalogue and book drafts (`docs/books`, `docs/sasmo`, `docs/audit`, `docs/terms`), private sources (`docs/books/private_*`), `tutor`, `taster`, `review`, `outputs`, `split`, `rebuild` and `website`. For each of the 366 questions I compared (a) stemmed content words with names and function words removed (shared fraction, shared rare words, shared numbers), (b) shared non-trivial numbers regardless of words, (c) four-word runs with numbers masked. I then read every hit.

**Same numbers (3 or more shared numbers with 2 or more shared story words): none.** The hits below are all "same story skeleton and same frame, other numbers" except the first two, which are the same numbers or the same answer.

| # | Teaser | Source | Judgement |
|---|---|---|---|
| 1 | `L3-windowpanes` (12-15) "A window has panes in a grid 3 panes across and 2 panes down. Count every rectangle ... " answer 18 | `p3/qbank_skills.json` and `outputs/skill_additions/Math_Inquirers_L3_Skill_Additions_Tutor_Sheet.html` (L3-RECT1): "A window has 3 panes across and 2 panes up and down. Count every rectangle you can find ... " answer 18 | **High: same story, same 3 by 2 grid, same answer.** |
| 2 | `L3-nightbus` (11-06) "A night bus leaves at 22:45 and arrives at 01:20 the next morning" answer 155 | `p3/content/l9.js` "A night train leaves at 22:40 and arrives at 01:15 the next morning. How long is the trip?" answer 2 h 35 min = 155 min | **High: same story, times moved by 5 minutes, same answer.** `L4-nighttrain` (12-13, 21:50 to 02:15) is the same story again: Medium. |
| 3 | `L1-borrowdays` (11-08) "Siti borrows a library book on a Monday and must return it 12 days later. Which weekday?" | L4 Skill Additions tutor sheet (L4-WEEKDAY): "Ben borrows a library book on a Monday and must return it 45 days later. Name the weekday." | **High: same stem, same start day.** |
| 4 | `L1-coinsets` (12-05) "Zack pays exactly 45 cents using 5-cent, 10-cent and 20-cent coins ... how many different sets" | `docs/audit/mkgifted_p3.py` (holiday P3 investigation "Find all the ways to pay": "Ali pays exactly 50 cents using only 5-cent, 10-cent and 20-cent coins") and `practice/holiday/p6/05/lesson.py` ("Find all the ways to pay 50 cents with 5-cent, 10-cent and 20-cent coins") | **High: same coins, same frame, our own sub-structure `coins.make_amount`.** The same sentence is then used at L3 (11-30, 110 cents), L4 (12-08, 80 cents) and L5 (12-23, 120 cents) with a fourth coin added: four levels in four weeks. Round 2 retired three subs for exactly this reason. |

Why the verifier did not see them: its source list stops at `docs/books`, `docs/sasmo`, `practice/**/*.json|js` and similar, so `outputs/` (the six Skill Additions tutor sheets), `docs/audit/*.py`, `practice/**/*.py`, `split/`, `rebuild/` and `website/` are not searched, and its thresholds need about 0.8 coverage plus shared numbers.

**Medium (same story skeleton, other numbers, or same frame in a source at the same level):**

| Teaser | Source |
|---|---|
| `L5-leak` (11-13) tap pours 25 L, leak 5 L, 600 L tank, minutes until full | `extension/data/l5_u05.json` "A tap pours in 9 litres each minute. A leak loses 1 litre each minute. After how many minutes is the tank full?" (our Level 5 extension book). The verifier lists this only as REVIEW against a different source in the full tree. |
| `L5-teams16` (12-09) 15 teams, every team plays every other once | `practice/holiday/p6/05/dist/data/p6l05.json` "In a league of 6 teams, every team plays every other team twice". **`verify_bank.py` now FAILS this on the current tree** (see M-4). |
| `L2-machine4` (11-09), `L4-machinefive` (12-26) | P2 tutor guide "A machine multiplies by a number, then adds a number. IN 2 gives OUT 11 and IN 5 gives OUT 20" (shares IN 5 and OUT 11); `docs/sasmo/g3_original_problems_draft.md` 10.2 "multiplies by 4 and takes away 1" |
| `L3-stampshare` (11-18) "Aisha has 4 times as many stamps as Ben. Together 65" | `docs/books/word_problems_g1_g2_original_draft.md` B3.2 "Raj has 3 times as many stamps as Dev. Together they have 84" |
| `L6-lastdigit` (12-11) "multiply 7 by itself 2026 times" | `docs/sasmo/g6_original_problems_draft.md` 2.2 "Multiply 7 by itself 45 times ... last digit" |
| `L1-ageplus` (L1) and `L2-grandpaage` (11-24) | `docs/books/word_problems_g1_g2_original_draft.md` B10.1 "Ali is 9 ... his aunt is 34 ... how old will she be when ..." (the verifier shows the REVIEW for `L2-grandpaage`) |
| `L2-pencilcase` (12-28), `L6-tokenbox` (12-10) | `p6/qbank_skills.json` and L6 Skill Additions "A box has 7 black pens, 5 blue ... how many to be sure of 2 of the same colour" (same objects, `L2-pencilcase` also has 7 black pens) |
| `L6-turtle` (11-13) | `p6/content/l7.js` "Walk a square: walk forward, turn on the spot ... until back at the start" |
| `L1-rungrow`, `L2-shellrows`, `L3-dotgaps`, `L5-tincoins`, `L6-stickersave` | `practice/holiday/p1/01` lesson 1 "The gaps are 1, 2, 3, 4, 5 ... the next gaps are 6 and 7" (growing gaps; the same sub-structure appears at all six levels in Nov and Dec) |
| `L1-boxpyramid`, `L3-stonepyramid`, `L4-canpyramid`, `L5-fivebricks`, `L6-stonepyramid5` | `extension/data/l3_u02.json` "Pyramids with a hidden number". `L3-stonepyramid` and `L4-canpyramid` both have the answer 33. |

**Fix:** replace items 1 to 4 with new stories on structures our books do not use; widen the verifier's source list to `outputs/`, `docs/**` (md, json, py), `practice/**/*.py`, `split/`, `rebuild/`, `website/**` and the six `Skill_Additions` sheets; add my content-word and four-gram rules; re-run on the full tree at every release (see M-4).

### H-2 (High) Flag-off pages are not byte-identical in the repo; one build step from going live

Round 2 reported that the generators without `MI_TEASERS` reproduce `website/mi_signup.html` and the six `website/level_pages/*.html` byte for byte. That is **no longer true of the committed files**:

* Commit `fbb4690` ("WIP: agents in progress", after the round 2 audit) committed `mi_signup.html` and all six `level_pages/*.html` **as the teaser-on build** (they contain `MiTeaser.init`, the `pzdaily` CSS and `id="pzBox"`; about 315 added lines each). `git show fbb4690^:website/mi_signup.html` has none of it. README itself warns to `git checkout mi_signup.html level_pages` after a preview build.
* My run of `lp_build.py`, `level_pages.py`, `shop_build.py` and `hub/build.py` **without** the flag on a scratch copy: all seven files **differ from the committed files**, and the three I compared (`mi_signup.html`, `ages-6-8`, `ages-11-13`) are **byte-identical to the pre-`fbb4690` versions** (so the generator code and the flag itself are correct).
* `build_site.py` reads those committed files directly. A build from the committed sources puts `MiTeaser` into `index.html` and all six level pages (checked). `website/DEPLOY.md` gives the build command `cd website && python3 lp_build.py && python3 build_site.py`, which regenerates only `mi_signup.html`; **the six level pages would go live with the teaser** although `site_enabled` is `false`. This contradicts "going live is a separate step".
* Good news: a fresh flag-off site build equals `website/dist` file for file except `_headers` (dist is older than `build_site.py`, not a teaser matter, Low), and `git diff origin/claude/great-fermi-1hv4vc -- website/dist` is **empty**. Nothing is deployed.

**Fix:** restore the seven files from `fbb4690^` (or re-run the generators flag-off), and add a test to `test_site.py`: committed pages equal flag-off generator output while `site_enabled` is false.

### H-3 (High) Level 1 and Level 6 cannot absorb one failure; the capacity table is thin on the strictest honest reading

* **Level 1:** 62 sub-structures, 61 needed. My own solver on the 366-date plan (section 5a): one failure is absorbable only by the single spare, `calendar.nth_weekday_date` (weak for ages 6 to 8: "date of the 4th Sunday"), and for 2 of the 61 slots even that breaks the family rule (`division.share`, `counting_range.days_in_common`: two `calendar` puzzles on consecutive days). **Two failures cannot be absorbed**: 60 subs x floor(366/60) = 360 < 366. This audit alone found at least two L1 sub-structures whose *frame* is in our own books (`coins.make_amount`, H-1 item 4; `growing_pattern.growing_gaps`, the holiday P1 lesson 1 pattern) plus a third whose story is (`calendar.weekday_after`). By the standard round 2 used to retire three subs, L1 is already at 59 to 61.
* **Level 6:** capacity is exactly 92 and Q3 and Q4 have 92 days. A solver model (section 5b) that includes the released Nov and Dec subs finds a feasible year, but it becomes **infeasible when any one unreleased sub-structure is removed (0 of 5 random trials feasible, then 0 of 5 at every size up to 8)**. Level 5 survives 3 removals and fails at 5; L3 and L4 survive 8.
* The builder's own minimum slack is 10, enforced only at L1 and L2. L4 slack is 9, L5 3, L6 0 and reported as "ok".

**Fix:** add sub-structures before writing: L1 to at least 71 (the verifier's own number), L6 to at least 100 usable and 100 or more capacity, L5 to at least 100 capacity; and apply the slack rule to all levels.

---

## 3. Hand-solved sample (item 2)

* **96 stratified puzzles** (16 per level, fixed seed): L1 11 new-sub + 5 replaced; L2 9 + 6 + 1 old; L3 7 + 6 + 3; L4 5 + 8 + 3; L5 6 + 4 + 6; L6 3 + 7 + 6. Plus **37 more** so that all 78 puzzles of the 50 new sub-structures are solved (L1 23, L2 26, L3 13, L4 6, L5 7, L6 3). **133 solved from the question text before looking at any answer; 133 agree** (the stored plain answer or the displayed form).
* Uniqueness by hand: sudoku 3 by 3 and 4 by 4 (one grid each), knockout (always one fewer), coin totals (all 15 and 31 subset sums differ), drinks machine and ticket notes (only 10 and 30, or 1 and 3, cannot be paid), triples of cards (one set each), shortest route (28 against 27 and 34), tetrominoes (5), take-away game (leave a multiple of 4), pigeonhole (13, 19, 23, 41), palindromes (900), page digits (38), 7 steps and 9 steps (Fibonacci).
* Explanations read for all 96 of the first sample: arithmetic right, kind wording, one idea per step.
* Wording points (Low): `L5-colourdraw` hint says "cards" for raffle tickets; `L5-sunflowerfall` asks for the year and the growth but accepts only the growth; `L2-twonumbers` (sum 33, product 270) is heavy for 7 to 9 trial and error; `L6-foldsix` and `L6-roundtrip` hint ("The answer is not 45 km/h") are fine but picture-free for Level 6.
* Wrong-answer list: 2,919 stored wrong answers tested with `MiTeaser.check`: **0 accepted**.

---

## 4. Taxonomy honesty (item 3)

### 4a. Same-family pairs: would a parent see the same puzzle?

I drew **40 pairs per level range (L1-2, L3-4, L5-6) = 120 pairs** of puzzles in the bank that share a family but have different sub-structures, same level, fixed seed, and read each pair.

| Range | Same puzzle | Same topic, small twist | Different |
|---|---|---|---|
| L1 and L2 (40) | 0 | 14 | 26 |
| L3 and L4 (40) | 1 (`L4-rects33` rectangles in a grid next to `L4-chesssquares` squares in a grid) | 15 | 24 |
| L5 and L6 (40) | 2 (`L5-fishtank` against `L5-cubes`: volume of a cuboid; `L6-nested` against `L6-program`: read a program, what does x hold) | 9 | 29 |
| All (120) | **3 (2.5%)** | **38 (32%)** | **79 (66%)** |

Round 2 found 5 of 42 (12%) the same. The merges worked. The borderline kind is mostly: time (`elapsed`, `hours_to_minutes`, `timetable_wait`), coins (three subs), unit conversion, percentage (GST, interest, of a quantity), two-line "how many more" bar models, counting shapes in a grid.

### 4b. Distinct-to-a-parent recount against the capacity table

Method: for each level the usable sub-structures in each family, parents' "same puzzle" probability per sibling pair (strict, from the sample: 0.02; with half of the borderline pairs: 0.15; with all borderline pairs: 0.35), 400 random clusterings.

| Level | Listed | Needed | Strict (p 0.02) distinct / capacity | p 0.15 | p 0.35 (every borderline pair merged) |
|---|---|---|---|---|---|
| 1 | 62 | 61 | **61.5** / 61.5 | 57.8 | 52.5 |
| 2 | 87 | 61 | 86 / 86 | 80 | 71 |
| 3 | 108 | 92 | 106 / 102 | 96 / 94 | 82 / 81 |
| 4 | 108 | 92 | 106 / 100 | 96 / 93 | 82 / 82 |
| 5 | 103 | 92 | 102 / 94 | 92 / 89 | 79 / 78 |
| 6 | 98 | 92 | 97 / **91.3** | 88 / 86 | 76 / 76 |

So on the strict reading **L1 has zero slack (61.5 against 61) and L6 is already about 0.7 puzzles short of 92 in Q3 and Q4**; if a parent treats the "same topic" pairs as repeats, L3 to L6 are 10 to 16 short and L1 is 8 short. The table in `STRUCTURE_REPORT.md` is arithmetically right and honest only if "different sub-structure" is read strictly.

Cross-level: in Nov and Dec **50 of the 172 sub-structures used appear at three or more levels (202 of 366 puzzles)**, `growing_gaps` at all six levels, the "pays exactly N cents" sentence at four, "faces west, turns right" at four, number pyramid at five, grid robot routes at five (M-2).

---

## 5. Year plan (item 4)

### 5a. Levels 1 and 2 (GAP60)

I parsed the 61-row tables of `YEAR_PLAN.md`, built the 366 dates from 1 Nov (including 29 Feb), and checked a 366-day and a 365-day (29 Feb removed) circular year myself:

| Check | L1 | L2 |
|---|---|---|
| Subs in the rotation / uses a year | 61 / 6 (5 in a 365-day year for some) | 61 / 6 |
| Minimum circular gap, 366 and 365 | **61 and 60** | **61 and 60** |
| Family in any 60 consecutive days (cap 3) | worst 3 | worst 3 |
| Same family on consecutive days | 0 | 0 |
| Bank subs equal the plan's subs on all 61 Nov and Dec dates | yes (0 mismatches) | yes |

So the plan is correct. L2 has 26 spare subs, so L2 is realistic. **L1 rigid rotation:**

* Spare subs: one (`calendar.nth_weekday_date`). Replacing a failed sub in all 6 of its slots is rule-safe for **59 of 61** subs and **not** for `division.share` and `counting_range.days_in_common`. Two failures are impossible without a second spare.
* Realism of 6 returns a year: several L1 subs have a very small parameter space (3 by 3 Latin square, "name the shape from clues", "which way do I face", odd or even sum, am and pm, fan of triangles, letters in number words, knockout counts). Six "new story and new numbers" versions of them in a year will look like one puzzle. The answer window (same value at most twice in 60 days at single digits) does not hurt, since 9 single digits x 2 = 18 per window; the author must still plan answers across the whole year.
* If a sub fails after release, every one of its 6 dates has to be rewritten, including the two already published (Nov and Dec).

### 5b. Levels 3 to 6 (TEASER-STRICT)

Own model: integer program (HiGHS via scipy) with one sub-structure per day, the 366-day leap calendar, quarter caps (1 per sub, 3 per family), the 30-day circular gap across all four quarter boundaries (windows of 30 days spanning a boundary, including 31 Dec to 1 Jan), the released Nov and Dec subs fixed, optionally no family on consecutive days. It models structure only, not answers, stories or frames.

| Test | L3 | L4 | L5 | L6 |
|---|---|---|---|---|
| Feasible with cap 3 (and with no consecutive family) | yes | yes | yes | yes |
| Feasible with cap 2 (the stricter reading of TEASER-STRICT) | **no** | **no** | **no** | **no** |
| Random unreleased subs removed: 1, 2, 3, 5, 8 (5 trials each) | 5/5 at all | 5/5 at all | 5/5, 5/5, 5/5, **1/5, 0/5** | **0/5 at all** |

L6 is feasible only because every family is used exactly `min(3, n_f)` times in Q3 and Q4. Quarters have 90, 91, 91, 92 and 92 days in a leap year.

### 5c. Answer rule at L3 to L6

The verifier checks only single-digit repeats for the full year. Text answers (names, weekdays, directions, shape names) must also be unique in a level for the year at L3 to L6. Nov and Dec have 5 of 61 text answers per level, so a year needs about 30 distinct text values per level (names, 7 weekdays, 4 directions): feasible but tight and unchecked (M-7).

---

## 6. Level fit against the MOE syllabus files (item 5)

Checked against `docs/moe/syllabus_by_level.md` (L1 builds on P1 and ages 6 to 8, so up to P3 is defensible; L2 on P2, ages 7 to 9; and so on).

Moved or replaced items, as built:

| Item | Where it is now | Verdict |
|---|---|---|
| Perimeter of a rectangle (P3) | `perimeter_basic` L2 to L5; `L2-gardenfence` | Closed at L1; one year above at L2 (Low) |
| Line-up counting | folded into `counting_choices.orders` L3 to L6 | Closed |
| Durations over one hour | `durations.elapsed` from L2 (`L2-swimlesson` 85 minutes) | Closed (P2 hours and minutes, P3 duration) |
| Squares in a grid | L3 to L6 (`L3-grid33`, `L4-chesssquares`) | Closed (enrichment) |
| Fraction of a set (P4 2.1) | `fractions.of_set` L4 and L5 | Closed for the named sub, **but `fractions.whole_from_part` is still allowed at L2** and `L2-beadswhole` ("gave 1/3 ... kept 30; find the whole") is the inverse of fraction of a set: Medium |
| Area with a cut-out (P3/P4) | removed from L2 | Closed |
| Rounding (P4) | `rounding.*` L4 to L6 (`L4-roundprices`) | Closed |
| New L1 and L2 subs | citations present for all 50 | Closed |

Still above level (round 2 called M-3 closed; it is not):

* **L2:** `L2-mangoes` ($7.80 for 6, then 11: decimal money divide and multiply, P4), `L2-barleycafe` (3 cups at $3.60, P4), `L2-mooncakes` (247 divided by 12) and `L2-schoolbus` (250 divided by 12; division by a 2-digit number is beyond P4), `L2-cakeparts` ("simplest form", P3), `L2-lampring` (270 divided by 9, P3). Medium.
* **L4:** `L4-calc` and the bracket subs use order of operations (P5 in the MOE file; on the Level 4 page list). Low.
* **L1:** `L1-trackflags` (108 divided by 3), `L1-bamboo` (84 divided by 4), `L1-lampbench` (halfway between 18 and 64) are P2 to P3 work; defensible for ages 6 to 8 but the owner's "up to one year above" rule is still unconfirmed. Low.
* L6 primes, negative numbers, probability, binary, Caesar shifts are not primary syllabus; the Level 6 page lists them (on-page, as in round 2).

---

## 7. Browser spot check (item 6)

Scratch build: `MI_TEASERS=1 lp_build.py && level_pages.py && build_site.py --out /dev/shm/site_on` in a copy of the repo, served by `http.server`; Chromium via Playwright. `website/dist` untouched.

| Check | Result |
|---|---|
| Builder's `test_site.py` on my scratch build | 431 checks, 0 failed |
| **Midnight rollover** from 6 time zones (Singapore, Los Angeles, Kiritimati UTC+14, Kolkata, Honolulu, London), 8 instants (59 s before and at midnight Singapore on 31 Oct/1 Nov, 30 Nov/1 Dec and 31 Dec/1 Jan; midnight into 1 Mar 2027; and 14 Nov 2027), levels 1, 3 and 6 | **144 of 144 correct**: the puzzle id equals the bank entry of the Singapore date; unreleased dates show the fixed puzzle with no label; the same date next year shows the same puzzle |
| Fallback: fetch aborted, 404, HTML 200 body, malformed JSON, empty JSON (page built without its inline months) | fixed puzzle kept in all five, no blank box |
| Late reply: 3 s and 9.5 s | puzzle swapped in both |
| No JavaScript (home, L1, L3, L6) | fixed puzzle is on the page; no daily markup |
| **Answer formats, all 366** | stored, shown, upper case, trailing full stop, spaces, "= X": **366 of 366 accepted**. **"It is X": 335 of 366 rejected (all numeric); "The answer is X": 366 of 366 rejected** with "Not yet" (Low, L-1 from round 2, still open) |
| Contrast (light and dark, L1 and L6) | hint 5.36 and 5.04, worked answer 5.77 and 5.96, label 5.35 and 5.90, text on boxes 11.3 to 14.3, Check button 9.28: all at least 5.04:1 |
| 390 px | no horizontal scroll at L1 and L6 (390 = 390); the 39 longest question, explanation and code-box puzzles (all six levels) stay inside the viewport, 0 bad |
| Flag off | See H-2: **committed** pages differ from flag-off output; a fresh flag-off build equals `website/dist` except `_headers`; `git diff origin/claude/great-fermi-1hv4vc -- website/dist` is **empty**; `site_enabled` is `false` |

---

## 8. Medium and Low findings

**Medium**

* **M-1** Medium near-copies in H-1 (14 rows).
* **M-2** Cross-level repeats: 50 sub-structures at three or more levels in Nov and Dec (202 of 366 puzzles). Allowed by TEASER-STRICT (per level), but a family with two children sees the same frame in the same weeks. The README promise "a new puzzle every day" is true per level; it must not be read as "a new idea". Owner note.
* **M-3** Level fit cluster at L2 (section 6).
* **M-4** **The verifier's "0 FAIL" is not reproducible and depends on the checkout.** On a tracked-only `git archive` it gives November 3 FAIL (`L5-leak`, `L6-turtle` and a false positive `L3-parrotsrabbits`); on the full working tree (with git-ignored private sources) November 0 FAIL, **December 1 FAIL (`L5-teams16`) against a holiday P6 file that was added after the builder's run**. Holiday and term books keep growing, so every release must re-run the verifier on the full tree, with the source list widened (H-1).
* **M-5** Owner has not confirmed the family cap (3 or 2); cap 2 makes L3 to L6 impossible (5b).
* **M-6** Parameter-poor L1 and L2 subs (5a).
* **M-7** Text answers at L3 to L6 are not tested for the year (5c).

**Low**

* L-1 Answer formats "It is X" and "The answer is X" give "Not yet".
* L-2 `README.md` says "175 in use"; 172 are used, 175 are usable. It says 39 merged subs and 100 ids; the taxonomy has 41 and 102.
* L-3 Hint and wording slips (`L5-colourdraw`, `L5-sunflowerfall`).
* L-4 `website/dist/_headers` is older than `build_site.py`'s output (not a teaser matter).
* L-5 `data-teaser-state` stays `loading` up to 8 s after an instant failure (invisible).
* L-6 `L3-coins40` and `L4-coins60` carry old numbers in their ids (110 and 80 cents in the text).
* L-7 `L6-codingclub` names Scratch and Python (the level's subject).
* L-8 Home page still has no level picker.
* L-9 `L2-twonumbers`, `L3-lanes5` heavy for the age.

---

## 9. GO or NO-GO for writing January to October

**NO-GO now.** Writing 305 more puzzles per level on this base repeats the round 2 pattern: the structure passes the builder's checks, the first independent read finds copies of our own books. Reasons: H-1 (four new High near-copies and 14 Medium, with a verifier that does not search the places they came from), H-2 (the repo as committed can publish the teaser by the documented build), H-3 (L1 and L6 have no room for one failure).

**It becomes GO per level when:**

| Gate | Needed |
|---|---|
| All levels | (a) the four High near-copies replaced and the Medium ones rewritten; (b) the seven site files restored and a test that committed pages equal flag-off output; (c) the verifier's source list widened (`outputs/`, `docs/**`, `practice/**/*.py`, `split/`, `rebuild/`, `website/`) and my content-word and four-gram rules added, run on the **full** tree before each month is released; (d) owner confirms family cap 3. |
| **L2, L3, L4** | After (a) to (d): **GO**, January first. L2 has 26 spare subs, L3 11 and L4 9 (add 1 or more to L4 to meet the slack 10 the builder already set). |
| **L5** | GO after capacity grows from 95 to at least 100 (survives 5 failures). |
| **L1** | GO only after usable sub-structures reach **71 or more** (genuinely different MOE P1 to P3 ideas, not twins), the 6 returns of thin subs have enough variety, and the plan is rebuilt with those. |
| **L6** | GO only after capacity exceeds 92 by at least 8 (any one lost sub breaks the year today). |

Process for each month once the gate is open: the author writes the month, the verifier runs on the full tree, an independent audit repeats sections 1 (content words), 2 (hand-solve at least 15 per level), 3 (sample 40 pairs per range) and 6 (browser), and the month is released only after that audit.
