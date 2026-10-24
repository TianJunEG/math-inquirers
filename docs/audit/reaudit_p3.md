# Re-audit of Level 3 (P3, ages 8-10): independent re-score against the earlier audits

Read-only desk review by a model; no real children. Snapshot: repo HEAD `9ae1a31` (22 Oct 2026) plus the working tree. Arithmetic and every table of deltas come from `docs/audit/reaudit_p3.py` (run `python3 docs/audit/reaudit_p3.py`).

## 0. How this was done, and what to trust

**Order of work.** Phase 1 (blind): I read the instrument files (`docs/gifted_research.md` section 2-3, the two brief templates, `diag/build_diag.py`), then the current material, and wrote my scores into `reaudit_p3.py` before opening any earlier audit. Phase 2: I then opened `gifted_p3.md`, `gifted_fixes_p3.md`, `journey_p3.md`, `fixpass_p3.md`, `close_gaps_p3.md`, `fixes_p3.md` and compared.

**What "current" means here.** Text read: `p3/content/l1..l10.js` (all five parts), `p3/data.js`, `p3/workbook_html.js` and `p3/gifted.json`; the printed workbook (58 pages, text extracted from the rebuilt PDF, all 10 lessons); all 10 decks `split/p3l1..10` (every slide's visible text and presenter notes, in `deck.json` order); the Tutor Guide PDF (81 pp, lesson routine, materials, look-back and choice blocks, Lesson 1 script), Question Bank, Taster, Weekly Email Pack, Weekly Dose and What-Learners-Get PDFs (labels and wording); `diag/content/p3.json`, `diag/build_diag.py` and the rebuilt Level 3 Placement Check and Tutor Key PDFs. I did not credit anything that exists only in a fix log: each "fixed" claim below was checked in the content or PDF.

**Answer keys.** About 75 numeric, "find all" and "only one answer" claims were brute-forced or recomputed in Python (L1 digit-sum counts 20/35, 6842, 9810/3012, 252 digits; L2 all letter puzzles, 3087, 247, 981, 168 sums with digit-sum 18; L3, L4, L5, L6, L7, L8, L9 (including 15 exact-$20 party plans), L10 items). No wrong key found.

**Where the two audits differ in strictness (read deltas with this in mind).**
1. *Same rubric, different rater.* A 0/1/2 score is a judgement. The earlier audit scored the content before the rework and wrote "after" estimates for only criteria 6 and 9; the close-gaps and fix passes came later and were never re-scored. So "claimed after" is a stale estimate of a weaker state, not a promise. My higher total is partly real design change (criteria 6, 9, 10) and partly rater difference (criterion 7: +0.4, and 3/4/8 in a few lessons).
2. *"If time" stars.* The earlier tier audit counted starred (if time) worksheet parts with their question. I count a whole starred question that is Think-harder demand as a borderline violation (strict) and also give a like-for-like figure that counts it as the earlier audit did.
3. *Journey "difficulty fit".* The brief says 3 = just right; the earlier scores do not follow that (L1 HIGH fit = 3 with "bored", L2 HIGH fit = 4 with "good fit"). Both audits in practice treat higher as better fit. I use 5 = best fit. Fit deltas are the least reliable numbers in this report.
4. *MIDDLE participation.* I scored 4 where the earlier review gave 5 in five lessons (breakout-room pairs with no adult presence, 10 pairs-minutes). That is stricter, not a content regression.
5. *Syllabus blind spot, shared.* Both audits give criterion 12 (extension without acceleration) a 2 in most lessons. `docs/audit/moe_alignment_p1_p3.md` (not one of the two instruments) flags common multiples (L3, L5), letters for unknowns (L2), three-denominator sums and fractions between (L6), composite perimeter (L7) and angle counting (L8) as above P3. If that audit is accepted, criterion 12 drops to 1 in about four lessons and my mean falls by about 0.4 (20.3 to 19.9). I have not done that adjustment in the tables.
6. *Diagnostic probabilities are assumptions.* The earlier audit and I use different per-item pass probabilities. To compare like with like I re-ran the OLD cut scores and the NEW rule on MY probabilities (section 5).
7. **One disclosed non-blind correction.** My blind score for L7 criterion 5 was 1. While comparing I re-read slide `p3l7-teach3` ("Find the area of this L-shape in two ways ... Two ways agree, so we can trust our answer") and the push-out slide `teach2`, and corrected it to 2. I then grepped all 10 decks for "two ways / another way / Way 1" for every other criterion-5 score of 1: no further change. Blind L7 total was 21; reported is 22.

---

## 1. Instrument A: gifted-style rubric (12 criteria, 0/1/2, /24)

### 1.1 Per-lesson totals: before, earlier-claimed-after, re-audit now

| L | Title | Before (orig. audit) | Claimed after (rework) | Re-audit now | now - before | now - claimed | Band now |
|---|---|---|---|---|---|---|---|
| 1 | Number Sleuths | 16 | 18 | 20 | +4 | +2 | gifted-style (edge) |
| 2 | Cryptarithm Crackers | 15 | 17 | 20 | +5 | +3 | gifted-style (edge) |
| 3 | Times Table Treasure | 17 | 19 | 21 | +4 | +2 | gifted-style |
| 4 | Model Makers | 16 | 18 | 19 | +3 | +1 | partly (top) |
| 5 | Remainder Riddles | 16 | 18 | 20 | +4 | +2 | gifted-style (edge) |
| 6 | Fraction Walls | 15 | 17 | 20 | +5 | +3 | gifted-style (edge) |
| 7 | Area Architects | 17 | 19 | 22 | +5 | +3 | gifted-style |
| 8 | Angle and Line Detectives | 14 | 16 | 20 | +6 | +4 | gifted-style (edge) |
| 9 | Measure and Money Masters | 15 | 17 | 20 | +5 | +3 | gifted-style (edge) |
| 10 | Challenge Day | 16 | 18 | 21 | +5 | +3 | gifted-style |
| | **Level mean** | **15.7** | **17.7** | **20.3** | **+4.6** | **+2.6** | |

Bands (research note, a suggestion not a source): 20-24 genuinely depth-oriented, 12-19 enrichment-flavoured with gaps. Eight of ten lessons sit exactly at 20 or 21, so a single stricter reading of criterion 10 or 12 pulls them back into the 12-19 band. My honest verdict is **at the lower edge of "depth-oriented"**, not comfortably inside it.

### 1.2 Per-criterion scores now, with delta against the ORIGINAL score in brackets

| L | 1 LFHC | 2 Depth | 3 Gen. | 4 Just. | 5 Paths | 6 Ladder | 7 Led | 8 Cmplx | 9 Posing | 10 Meta | 11 Pace | 12 Ext. | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2 | 1 | 2 | 2 | 1 | 2 (+1) | 2 | 1 | 2 (+2) | 2 (+1) | 1 | 2 | 20 (+4) |
| 2 | 2 | 1 | 2 | 2 | 1 | 2 (+1) | 2 (+1) | 1 | 2 (+2) | 2 (+1) | 1 | 2 | 20 (+5) |
| 3 | 2 | 1 | 2 | 2 | 2 | 2 (+1) | 2 | 1 | 2 (+2) | 2 (+1) | 1 | 2 | 21 (+4) |
| 4 | 2 | 1 | 2 | 2 | 1 | 2 (+1) | 2 (+1) | 1 | 2 (+1) | 2 (+1) | 1 | 1 (-1) | 19 (+3) |
| 5 | 2 | 1 | 2 | 2 | 1 | 2 (+1) | 2 | 1 | 2 (+2) | 2 (+1) | 1 | 2 | 20 (+4) |
| 6 | 2 | 1 | 2 | 2 | 1 | 2 (+1) | 2 (+1) | 1 | 2 (+2) | 2 (+1) | 1 | 2 | 20 (+5) |
| 7 | 2 | 1 | 2 | 2 | 2 | 2 (+1) | 2 | 2 (+1) | 2 (+2) | 2 (+1) | 1 | 2 | 22 (+5) |
| 8 | 2 | 1 | 2 (+1) | 2 (+1) | 1 | 2 (+1) | 2 | 1 | 2 (+2) | 2 (+1) | 1 | 2 | 20 (+6) |
| 9 | 2 | 1 | 1 | 2 | 1 | 2 (+1) | 2 (+1) | 2 | 2 (+1) | 2 (+1) | 1 | 2 (+1) | 20 (+5) |
| 10 | 2 | 1 | 2 (+1) | 2 (+1) | 2 | 2 (+1) | 2 | 1 | 2 (+1) | 2 (+1) | 1 | 2 | 21 (+5) |

### 1.3 Per-criterion level means: before, claimed, now

| Criterion | Before | Claimed after | Now | now - before | now - claimed | Real change or rater difference? |
|---|---|---|---|---|---|---|
| 1 Low floor, high ceiling | 2.0 | 2.0 | 2.0 | 0 | 0 | unchanged, already strong |
| 2 Depth over speed | 1.0 | 1.0 | 1.0 | 0 | 0 | **not fixed** |
| 3 Generalisation | 1.7 | 1.7 | 1.9 | +0.2 | +0.2 | real in L8, L10 (investigation "Is it always true?" pages) |
| 4 Justification | 1.8 | 1.8 | 2.0 | +0.2 | +0.2 | real in L8, L10 (Mei/Ben claim items, investigation part c) |
| 5 Multiple paths | 1.3 | 1.3 | 1.3 | 0 | 0 | not fixed (L3, L7, L10 only) |
| 6 Challenge ladder | 1.0 | 2.0 | 2.0 | +1.0 | 0 | **real, matches the claim** |
| 7 Student-led inquiry | 1.6 | 1.6 | 2.0 | +0.4 | +0.4 | mostly rater difference (talk-time starters and pass are real, mini-lessons still tutor-led) |
| 8 Complexity | 1.1 | 1.1 | 1.2 | +0.1 | +0.1 | L7 only (garden/fence optimisation, now credited) |
| 9 Problem posing | 0.3 | 1.3 | 2.0 | +1.7 | +0.7 | **real**: a printed "make up your own / change ONE number" item in all 10 Go-further pages, plus "What if we change it?" investigations |
| 10 Reflection | 1.0 | 1.0 | 2.0 | +1.0 | +1.0 | **real**: Look back box on the last page of every lesson, slide at 86-88 min |
| 11 Pacing / compacting | 1.0 | 1.0 | 1.0 | 0 | 0 | **not fixed**; the fast-track that would have moved it was removed on safeguarding grounds |
| 12 Extension, not acceleration | 1.9 | 1.9 | 1.9 | 0 | 0 | L4 -1 (my judgement), L9 +1; see strictness note 5 |

### 1.4 One-line evidence for each criterion (shared across lessons; lesson exceptions after the table)

| # | Evidence in the current material |
|---|---|
| 1 | Sneak-peek puzzle 1 is an access puzzle in every deck (L1 cards 4, 0, 9; L5 13 sweets in bags of 4; L6 shade one quarter); Explore 10-25 min is open or "list all" with a "Go further, any time" what-if on the slide (L1 cards 2, 4, 5, 8; L9 12 friends and $30); each investigation page prints an "Easy first step"; slide notes give the hint ladder and expected answers. |
| 2 | Explore has 15 min and Talk 10 min, but Start-here is 6 questions and 12-20 sub-parts in about 22 min (page 1 in pairs 10-12 min, page 2 alone 7 min), and Think harder, Go further and its two help slides all sit on the 67-70 min slot (3 minutes). Success is still finishing the set; "(if time)" labels soften it. |
| 3 | Every lesson ends with an investigation ("Is it always true?" L2, L3, L5; "What if we change it?" L1, L7; "What stays the same?" L4; "Find the pattern" L8, L10) with a table that leads to a rule; Go-further items ask for rules (L8 c2 staircase, L10 c1 queue). |
| 4 | "Mei/Ben/Ali says ... do you agree?" items and "explain" prompts are printed in every lesson (L1 Q4c, L3 Q1b, L4 Q5b, L5 Q1c, L8 c5/c6); Talk time asks for reasons; sentence starters "I noticed / I tested it by / I know because". |
| 5 | Two methods on slides in L3 (`we2`: 9 x 7 two ways, "two ways agree is a strong check"; TH s8) and L7 (`teach3`: L-shape area "in two ways"); L10 teaches "draw it, list it or make a table" and Talk asks which helped most. Elsewhere one taught method, alternatives only in notes. |
| 6 | Neutral tiers by choice: "Start here" -> after Q3 "carry on or try Think harder" -> Go further -> Investigation with easy first step; explore Go-further any time; no public labels (checked: no "fast track / early finisher / strong thinker" in any workbook, deck or guide). |
| 7 | Predict-first, pairs in breakout rooms, hint ladders, talk time 2 min in pairs then volunteers; teach slides before each worksheet page are tutor-led but short (1-3 min), 10 min main mini-lesson. |
| 8 | Mostly thin contexts (word problems, number puzzles). Real interacting variables in L7 (18 m fence, which garden is biggest) and L9 (party: >= 2 l punch, one food, close to $20, 15 exact plans). |
| 9 | Go-further page prints a posing item: L1 c7 "What number am I?" with unique-answer check, L2 c7 missing-digit sum, L3 c7, L4 c7 before/after story + change one number, L5 c7, L6 c7 ("always going to work?"), L7 c7, L8 c7, L9 c9, L10 c7; investigations vary conditions. |
| 10 | Look back: "Something I did well" / "The hardest part was" (lesson-specific ticks) / "What helped me" (strategy ticks + "I asked for help" + "I am still stuck"); pass allowed; page is the child's. No "what I will try next" line, so a strict reader could hold this at 1 (not done). |
| 11 | Same slide sequence for every group; sneak-peek answers are not used to skip anything; only choice-after-Q3 and Go-further-any-time provide flexibility. |
| 12 | Topics are P3 topics explored through puzzles; some items import ideas flagged above P3 elsewhere (strictness note 5). L4 scored 1 because Go-further c1 (3:1 -> 2:1 after a gift) and TH s6 are before-and-after ratio problems beyond P3 model work. |

Lesson exceptions: L9 c3 = 1 (investigation is enumeration, "find all the ways to pay"; only the posing item changes a number, no rule); L7 c8 = 2 and L9 c8 = 2 as above; L3 c5 = 2, L7 c5 = 2, L10 c5 = 2 as above; L4 c12 = 1.

### 1.5 Strengths and gaps (level)

Strengths: low-floor access every lesson; a real challenge ladder by choice with no labels; posing and investigation in all ten; reflection built in; strong "Notice it, test it, explain why" justification habit.
Gaps (rubric order of cost): criterion 2 depth/speed (1 in all ten); criterion 11 compacting (1 in all ten); criterion 5 several methods (1 in seven); criterion 8 complexity (1 in eight); criterion 12 syllabus caution.

---

## 2. Tier compliance (Core / Think harder / Challenge)

### 2.1 Rule used
Core: startable by a child who has not been taught the topic (objects, drawing, counting, guess-and-check, patterns, skills from the level below, no unexplained notation); an in-item scaffold (picture, hint, worked start) counts. Think harder: needs the taught idea in a new setting. Challenge: mastery plus extension (multi-step, generalise, justify, combine, open-ended, posing). Printed Start-here pages are post-teaching practice by design, so I apply the Core test to whether the item offers an entry route, not whether the topic was taught. B = borderline = counted as a violation in the strict figure.

### 2.2 Items audited
Question bank: 60 Core + 84 Think harder ("stretch") + 90 Challenge = 234. Printed workbook Start-here Q1-Q6 x 10 = 60. Slide-only Think-harder items (L5-L8, 3 each, not in the bank) = 12. Total 306 (the earlier audit had 305). Printed Think-harder (T1-T4) and Go-further (X7-X9) pages are subsets of the bank (70 items, 0 violations). Investigation pages (10) each have an easy first step.

### 2.3 Result

| | Before (orig.) | Claimed after | Now, strict | Now, like-for-like (stars with their question) |
|---|---|---|---|---|
| Items compliant | 236 / 305 | 305 / 305 | 295 / 306 | 301 / 306 |
| **Compliance** | **77.4%** | **100%** | **96.4%** | **98.4%** |
| Bank Core (60) | n/a | | 60 / 60 | 60 / 60 |
| Printed Start-here (60) | | | 53 / 60 | 59 / 60 |

By lesson (before -> strict -> like-for-like): L1 83% -> 97% -> 100%; L2 83% -> 93% -> 97%; L3 83% -> 90% -> 97%; L4 73% -> 100% -> 100%; L5 84% -> 94% -> 97%; L6 73% -> 97% -> 97%; L7 69% -> 97% -> 97%; L8 62% -> 100% -> 100%; L9 83% -> 100% -> 100%; L10 83% -> 97% -> 100%.

The earlier "100% after" was self-assessed and is not reproduced: 11 items still fail the strict test, 5 on the like-for-like test.

### 2.4 The 11 strict violations (all borderline, none a Core item in the bank)

| Item | Reason |
|---|---|
| L2 bank T5 | smallest/greatest 4-digit number with digit sum 30: an L1 place-value idea, not the L2 taught idea (tier fit, not difficulty) |
| L3 bank X6 | 40-60 sweets shared among 6 and 9 friends: list-and-test, one step of the taught method (Think-harder level) |
| L5 bank X2 | 30-50 chocolates shared by 2, 3, 4, 6: same list-and-test as Think-harder s7 |
| L7 bank X4 | square perimeter 20 -> side 5 -> big square 10 -> 40: three routine steps, no extension |
| L6 Start-here Q4 | six sums with unlike denominators (1/4 + 3/8, 1/3 + 5/12 ...): needs the taught equal-parts method, no reference to the wall in the item (the only non-star one) |
| L1 Q6, L2 Q6, L3 Q4, L3 Q6, L5 Q6, L10 Q6 | whole questions marked "(if time)" that are Think-harder demand sitting on the Start-here page |

### 2.5 Ledger (compact; "C" = compliant)
- **L1** Core C1-C6 C (sweets boxes, chart given, cards, counting back, pattern, ordering); TH T1-T8 C; Challenge X1-X9 C; Start-here Q1-Q5 C (cards are manipulable, Q4 has a "draw a box for each" hint), Q6 B.
- **L2** Core C1-C6 C (Th H T O grid, number-line hint, "try 5, 6, 7"); TH T5 B, rest C; Challenge C; Start-here Q1 C (worked example inside the item), Q2-Q5 C, Q6 B.
- **L3** Core C (5 x 9 -> 6 x 9, draw 6 rows of 8, count in 7s); TH C; Challenge X6 B, rest C; Start-here Q1-Q3, Q5 C (row pre-filled, split example), Q4 B, Q6 B.
- **L4** all C (bars drawn in the item, "draw 1 box for Ali and 4 for Ben"); Start-here Q1-Q6 C (hints, "try Ben = 50").
- **L5** Core C (counters or drawing named); TH C; Challenge X2 B; Start-here Q1-Q5 C (drawn 6 plates, "draw 12 bags of 8"), Q6 B; slide-only TH (3) C.
- **L6** Core C (bar drawn, shade parts); TH, Challenge C; Start-here Q1-Q3, Q5, Q6 C, Q4 B; slide-only (3) C.
- **L7** Core C (walk round the edge, 6 rows of 7); TH C; Challenge X4 B; Start-here Q1-Q6 C (missing sides given as a hint); slide-only (3) C.
- **L8** all C ("corner of a page" as the right-angle reference, definitions in the stems); Q5c is labelled "Think harder (if you have time)" inside Q5, counted with Q5; slide-only (3) C.
- **L9** all C (conversion facts printed in the item, time line hint); Start-here Q1-Q6 C.
- **L10** Core C (draw the queue, guess-and-check); TH, Challenge C; Start-here Q1-Q5 C, Q6 B.

---

## 3. Instrument B: student journey (LOW / MIDDLE / HIGH)

Scores: P participate, F fit (5 = best, see note 3), U fun, C confidence, M motivation, S social/online.

### 3.1 Shared structure that drives most scores (checked in decks, workbook and guide)
- Minutes 2-5 sneak-peek: puzzle 1 an access puzzle (objects, drawing, counting), puzzle 2 a thinking puzzle, "Nobody is marked", answers on own paper shown to the tutor only. Good for LOW. Weak spots: L7 puzzle 1 uses "area" and "perimeter" undefined; L2 puzzle 1 still needs 3-digit carrying.
- Minutes 5-10: game then five quick questions (whiteboards up together, visible to the gallery). Fixed since the earlier review: Buzz is now only the 7s to 40 with an open palm and a kind-miss line (L3 `warm1`); the relay chain is tutor-read, volunteer-answered, pass allowed (L10 `warm1`).
- Explore 10-25 in pairs in breakout rooms. No statement that the tutor visits each room (guide: "pairs work in one breakout room for 10 minutes").
- Start-here: page 1 in pairs (3 questions, about 12 sub-parts, 10-12 min), page 2 alone (7 min). First item is a win for LOW in L1, L3, L4(Q3), L5(Q1 drawn), L6, L7, L8, L9 (Q1 now "2 m = __ cm"), L10; **not** in L2 (Q1a still a 4-digit sum with carries).
- Think harder / Go further: separate printed pages, chosen by anyone after Q3; slide slot is 3 minutes.
- Talk time: volunteers first, pass or share with partner, no cold calls; exit ticket on own paper shown to tutor; Look back two minutes, page never collected.
- Reading load: Start-here pages run about 190-470 words per lesson including hints and labels (L5 heaviest). Not materially lighter than before; scaffolds added words.

### 3.2 Per-lesson scores and evidence

| L | Persona | P F U C M S | Mean | Evidence (slide/page/item) |
|---|---|---|---|---|
| 1 | LOW | 4 3 4 3 3 3 | 3.33 | Warmcheck P1 (cards 4, 0, 9) and `warm1` "Biggest number wins" are concrete wins; wb p1 Q1a a win. Risk: Q2 (list 9 numbers from 2, 0, 5, 5 incl. repeated 5s) and Q3c in a 10-12 min pairs slot; Q4a "15 hundreds" has only a drawing hint; exit needs the 0-first rule. Q5b, Q6 are "(if time)". |
| 1 | MIDDLE | 4 4 4 4 4 4 | 4.00 | Explore (2, 4, 6, 8, list in order) feeds Q1-Q3 directly; Q2 is the productive struggle. |
| 1 | HIGH | 5 3 4 5 4 4 | 4.17 | Warm2 and teach1/we1/we2 (25-31 min) are known; ceiling from warmcheck P2 (smallest odd), explore1 Go further (2, 4, 5, 8), TH s5/s6/s8, GF c7 make-up puzzle, investigation "What if one card changes?". Waits if the pair is slow. |
| 2 | LOW | 3 2 3 2 3 3 | 2.67 | wb Q1a two missing digits with carries (a worked "3_2 + 115" example and Q1b hint were added); explore with cards 1-9 needs 3-digit carry sums; `teach1` shows letters A-D. No early win on page 1. |
| 2 | MIDDLE | 4 3 4 3 4 4 | 3.67 | Magic square Q3 and pyramids Q4 are fun; Q1b subtraction and Q4b stretch. |
| 2 | HIGH | 5 4 5 5 4 4 | 4.50 | Explore (168 sums, digit sum always 18), TH s6/s8 letter puzzles, GF c7 and c9, investigation "reverse trick". |
| 3 | LOW | 4 3 4 3 3 3 | 3.33 | Warmcheck P1 gives the 7 table on screen; Buzz = 7s to 40, open palm; wb Q2 row pre-filled, Q1 starts 9, 18. Still: 6-9 tables themselves, Q3 split needs 5-facts, Q4/Q6 "(if time)", round-the-group counting is semi-public. |
| 3 | MIDDLE | 4 4 5 4 4 4 | 4.17 | Digit-circle stars (explore), Q3 split array, Q5 chairs with a table. Best MIDDLE fun. |
| 3 | HIGH | 5 3 4 5 5 4 | 4.33 | Star shapes, "why is the 6 table even?", digit-sum investigation (9 x 11 = 99), GF c8 7^8 last digit. |
| 4 | LOW | 4 3 4 3 3 3 | 3.33 | Cubes (`explore1`) and arm bars (`warm1`) concrete; Q3 units drawn (a win, but third); Q1 1250 - 486 - 378 over a zero and Q2's three sentences soft, hints added; Q4 "Try Ben = 50". |
| 4 | MIDDLE | 4 4 4 4 4 4 | 4.00 | Models taught before use; page 2 well scaffolded ("try giving 10"). |
| 4 | HIGH | 5 3 4 5 4 4 | 4.17 | Bar models familiar; TH s2/s6/s7, GF c1 and posing "change ONE number"; investigation age table. |
| 5 | LOW | 4 3 4 3 3 3 | 3.33 | Counters/cups; warmcheck P1 (13 sweets in 4s) and P2 (Ali's "6 left over") are good; Q1 has a drawn 6-plate figure; Q2 split a-d. But 47 / 6 and 75 / 9 need division facts; Q4 list-and-test; heaviest reading load (about 470 words). |
| 5 | MIDDLE | 4 4 4 4 4 4 | 4.00 | Explore 25 counters, Q1c error-spotting, Q2 "what does the leftover mean". |
| 5 | HIGH | 5 3 5 5 5 4 | 4.50 | GF c8 (100 days from Monday), c9 pens, investigation "three in a row", TH s6 50th shape. |
| 6 | LOW | 3 2 3 2 3 3 | 2.67 | Strips and wall Q1 are an on-ramp, but Q2 has 7 parts (incl. ordering 5/12, 1/2, 1/3, 3/4), Q4 six unlike-denominator sums with no wall in the item, Q6 ten cards; seven strips to cut or print; page 1 in 10 min. |
| 6 | MIDDLE | 4 3 4 3 4 4 | 3.67 | Wall makes equivalence visible; Q4 is the hard part. |
| 6 | HIGH | 5 3 4 5 4 4 | 4.17 | TH s9 (Mei's 2/3 vs 3/4), GF c6 (5 pieces, find all) and c9, investigation "find all the ways". |
| 7 | LOW | 4 3 4 3 3 4 | 3.50 | `warm1` area/perimeter gestures and 12-square explore concrete; Q1 counting squares a win. Warmcheck P1 uses "area" and "perimeter" undefined; Q4 missing sides (hint 10 - 6, 7 - 4 given). |
| 7 | MIDDLE | 4 4 4 4 4 4 | 4.00 | Right size; push-out vs dent discovery (`teach2`, `try2`). |
| 7 | HIGH | 5 3 4 5 5 4 | 4.33 | Q2 gardens (18 m fence), `talk` same perimeter different area, GF c7 two-clue puzzle, investigation (n+1) x (n-1). |
| 8 | LOW | 4 3 4 3 3 3 | 3.33 | Fold-a-checker and clock-arms are tactile; Q1 sort and Q2 "A is done for you" are wins; Q3 counts angles from 6 lines (example given), warmcheck P2 diagonal-triangle question is hard. |
| 8 | MIDDLE | 4 4 4 4 4 4 | 4.00 | Checker makes counting tangible; Q3 and Q6 are the work. |
| 8 | HIGH | 5 3 5 5 5 4 | 4.50 | Staircase-corners investigation (rule: steps + 3), TH # sign, GF c7 own riddle, c9 six-sided shape. |
| 9 | LOW | 3 2 4 2 3 3 | 2.83 | Better: Q1 opens "2 m = __ cm", menu in whole/half dollars, mini-lesson one idea. Still heavy: Q3 adds three decimal prices from a 5-item list, Q4 24-hour table, Q5 three time-line parts, Q6 timetable; five topics. Weakest LOW cell. |
| 9 | MIDDLE | 4 3 5 3 4 4 | 3.83 | Party planner is the best fun in the level; Q3-Q5 overload on page 2. |
| 9 | HIGH | 5 3 5 5 5 4 | 4.50 | Open party planner (15 exact plans), GF c9 pose a problem, TH s8 cheapest milk, investigation ways to pay 50c (12 ways). |
| 10 | LOW | 4 2 4 3 3 3 | 3.17 | Q1 bar graph start and Q3 queues "draw it" are wins; two 7-minute stations with a visible timer (`explore1`), Q2 logic grid with three text clues and ticks/crosses, relay chain (pass allowed). |
| 10 | MIDDLE | 4 3 4 4 4 4 | 3.83 | One theme (how to start) across stations; Q2 and Q6 harder. |
| 10 | HIGH | 5 4 5 5 4 4 | 4.50 | Handshake investigation, GF c7 own logic puzzle, TH s7 snail, c4 liar puzzle in the bank. |

### 3.3 Heatmap: mean of the six, before (original review) -> now

| Lesson | LOW | MIDDLE | HIGH | Lesson mean |
|---|---|---|---|---|
| L1 Number Sleuths | 3.33 -> 3.33 | 4.17 -> 4.00 | 4.00 -> 4.17 | 3.83 -> 3.83 |
| L2 Cryptarithm Crackers | 2.67 -> 2.67 | 3.67 -> 3.67 | 4.50 -> 4.50 | 3.61 -> 3.61 |
| L3 Times Table Treasure | 2.33 -> 3.33 | 3.67 -> 4.17 | 4.67 -> 4.33 | 3.56 -> 3.94 |
| L4 Model Makers | 3.33 -> 3.33 | 4.17 -> 4.00 | 4.00 -> 4.17 | 3.83 -> 3.83 |
| L5 Remainder Riddles | 2.67 -> 3.33 | 3.83 -> 4.00 | 4.33 -> 4.50 | 3.61 -> 3.94 |
| L6 Fraction Walls | 3.17 -> 2.67 | 4.17 -> 3.67 | 4.00 -> 4.17 | 3.78 -> 3.50 |
| L7 Area Architects | 3.17 -> 3.50 | 4.00 -> 4.00 | 4.33 -> 4.33 | 3.83 -> 3.94 |
| L8 Angle and Line Detectives | 2.83 -> 3.33 | 3.83 -> 4.00 | 4.50 -> 4.50 | 3.72 -> 3.94 |
| L9 Measure and Money Masters | 2.17 -> 2.83 | 3.33 -> 3.83 | 4.50 -> 4.50 | 3.33 -> 3.72 |
| L10 Challenge Day | 3.67 -> 3.17 | 4.50 -> 3.83 | 4.00 -> 4.50 | 4.06 -> 3.83 |
| **Persona mean** | **2.93 -> 3.15 (+0.22)** | **3.93 -> 3.92 (-0.01)** | **4.28 -> 4.37 (+0.09)** | |

Biggest real moves up: L3 LOW +1.00 (table on screen in the check, Buzz reduced, pre-filled row), L9 LOW +0.67, L5 LOW +0.67 (access puzzles, drawn sharing figure, Q2 split), L8 LOW +0.50 (Q2 hint and example, Q3 example). Biggest moves down: L10 MIDDLE -0.67, L6 MIDDLE and LOW -0.50, L10 LOW -0.50. Section 6 says which of these are content and which are my stricter scoring.

### 3.4 Dimension means (over 10 lessons), before -> now

| Persona | Participate | Fit | Fun | Confidence | Motivation | Social/online |
|---|---|---|---|---|---|---|
| LOW | 3.2 -> 3.7 | 2.4 -> 2.6 | 3.4 -> 3.8 | 2.7 -> 2.7 | 3.1 -> 3.0 | 2.8 -> 3.1 |
| MIDDLE | 4.3 -> 4.0 | 3.5 -> 3.6 | 4.1 -> 4.2 | 3.8 -> 3.7 | 4.1 -> 4.0 | 3.8 -> 4.0 |
| HIGH | 5.0 -> 5.0 | 3.5 -> 3.2 | 4.5 -> 4.5 | 4.1 -> 5.0 | 4.6 -> 4.5 | 4.0 -> 4.0 |

Read-across: the fixes help LOW on participation, fun and the social/online dimension (Buzz, talk-time pass, relay, public labels gone). They do not yet lift LOW's fit (2.6) or confidence (2.7), which depend on prerequisite fluency and reading load. HIGH confidence 5.0 is my most generous number (the earlier review's 4.1 reflected the public fast-track label that has since gone, but my uniform 5 ignores rushing errors); treat it as plus or minus 0.5.

### 3.5 Flagged moments (still present)
1. **Rushed pairs slot.** Page 1 is 3 questions and 10-20 sub-parts in 10-12 minutes (L1, L2, L6, L9 worst); the LOW child finishes none and sees the partner move on.
2. **"I am still stuck (my tutor will check in with me)"** is printed on a page that "your tutor does not read out or collect". The tutor cannot know who ticked; the promise only works if the child signals. The earlier contradiction is replaced by a quieter one.
3. **Breakout pairs** for 10 minutes with no instruction that the tutor visits each room; a LOW child paired with a fast partner can be talked over.
4. **Whiteboards up together** in the quick questions: everyone's answer is visible in the gallery view (copying, comparing).
5. **L10 timer.** Two 7-minute stations on a visible timer is the one new time-pressure device introduced by the fix pass.
6. **Undefined "area / perimeter"** in L7's access puzzle; **three-price decimal sum** in L9 Q3(a).
7. HIGH child: about 30 minutes (warm-up, teach slides at 25-35, 40-42, 54-58) is pitched below them; relief comes from the choice menu and investigations, not from compacting.

---

## 4. Improvements that are real (verified in the content)

| Improvement | Evidence |
|---|---|
| Public labels removed | No "fast track", "early finisher", "strong thinker", "genius" in any workbook page, deck (visible text and notes) or guide; tiers are "Start here / Think harder / Go further / Investigation" with a whole-group invitation wording (guide p.4, repeated in each lesson). |
| Tier principle largely met | 60/60 bank Core items carry an entry route (drawing, objects, hint or printed rule); 70/70 printed Think-harder and Go-further items comply; 98% of 306 items on the like-for-like test (77% before). |
| Posing and investigation in all ten lessons | Printed Go-further item "make up your own ..." (L1 c7 ... L10 c7, L9 c9) and one investigation page per lesson with "Easy first step" and a model answer. |
| Reflection | Look back box on the last page of each lesson; slide at 86-88 min; lesson-specific "hardest part" ticks; pass allowed; page stays with the child. |
| Safer social moments | L3 Buzz (7s to 40, open palm, kind miss), L10 relay (tutor reads, pass fine), talk time volunteers/pass/partner share on every talk slide, exit and sneak-peek answers shown to tutor only. |
| Weak-lesson on-ramps | L9 Q1 now "2 m = __ cm", menu in whole and half dollars; L3 Q2 row pre-filled and Q1 first answers given; L8 Q2 hint and "A is done for you"; L2 Q1 worked example and Q1b hint; L5 drawn sharing figure and Q2 split a-d; L4 hints under Q1, Q2. |
| Answer keys are right | About 75 claims brute-forced or recomputed; none wrong, including all unique-answer claims. |
| Diagnostic mechanics | Scored on the six main questions; M3 now a single-box "left over" question; area marked on 36 with any unit; stretch S2 replaced (9 numbers); "guess and check is fine" in the key; separate tutor-key PDF so the child sheet carries no answers; the word "failure" is gone. |

---

## 5. Part 2: the diagnostic (Level 3 Placement Check, current rule)

### 5.1 The rule as built (`diag/build_diag.py`, result page)
Score the 6 main questions (0-6). 4-6: join Level 3 (if at least 1 of 2 stretchers, "you could try the Level 4 check"). 2-3: tutor chat and taster, "Level 3 with a little support suits many"; if warm-up is 2 or less, "Level 2 may be the more comfortable start". 0-1: "We suggest Ages 7-9 (Level 2)". The 4 warm-up questions (level below) and 2 stretchers are not added into the score.

### 5.2 Did the earlier findings get fixed?

| Earlier finding | Status | Evidence |
|---|---|---|
| Noisy 8-item cut scores (typical child gets a clean "join" only about 39%, resit lands in a different band up to 60%) | **Partly fixed** | Cut now on 6 items with a wide middle "chat" band. Same assumptions, old cuts vs new rule: typical child joins 19% -> 65%; chance a child with true p = 0.75 lands in a different band on resit 45% -> 28%. Still a coin toss within one mark of a line (resit-different-band 18-57% across p = 0.5-0.8). |
| Discouraging wording ("not a failure") | **Mostly fixed** | "Failure" gone; "Found it hard? ... says nothing about how clever your child is" (still introduces "clever"); 0-1 row still reads "We suggest ... Level 2". "Ticked 'not learnt yet' ... do not count against the child" contradicts scoring them 0 in the main total. |
| Younger-strong, older-weak and rushing children mis-placed to Level 2 | **Partly fixed** | Outright or "may be more comfortable" Level 2 recommendation, old cuts vs new rule on my inputs: younger strong 48% -> 20%, older weak 84% -> 37%, rusher 59% -> 17%. Not fixed: no age rule (a 10-year-old can still be pointed to "Ages 7-9"), no warm-up condition in the 0-1 band, "Open to a year either side" still printed. |
| Item fairness (two-part M3, unit trap on area, easy S2, "Weak: guess and check" label) | **Fixed** | M3 "52 children in rows of 7 ... left over" = 3; key awards 36 with any unit; S2 = digits 2, 5, 8, 0 -> 9 numbers (brute-forced); M1 key "guess and check is fine". |
| Tutor key boilerplate ("2.05 and $2.05") | **Not fixed** | Still printed in the Level 3 Tutor Key. |
| Coverage gaps (4-digit numbers, tables 6/8/9, angles, measures, graphs) | **Not fixed** | Main questions: missing digit, times as many, 52 / 7, 3/4 = ?/12, area 9 x 4, 2:45 + 1 h 50. M3 now exercises the 7 table; nothing tests 6/8/9 tables, L1, L8, L9 (beyond time) or L10 skills. |
| Rule documented consistently | **Regression** | `docs/levels_and_placement.md` and the website (`lp_build.py`, `index.html`) still say 70% / 40-69% / under 40% / 90%+. At 4/6 (67%) the site says "40-69%: enrol, support may help or go one level down" but the sheet says "Join"; at 2/6 (33%) the site says one level down, the sheet says tutor chat. |

Items verified: warm-up 47 + 38 = 85, 305 - 128 = 177, 4 x 8 = 32, 24 / 3 = 8 are genuinely level-below (Level 2); main answers 8, 36, 3, 9, 36, 4:35 p.m.; stretch 7 and 9 recomputed. Main items are fair for "builds on Primary 3 maths" at the end of the year; early in the year fractions, area and remainders may not be taught.

### 5.3 Re-run of the six pretend children on the current rule
Per-item pass probabilities are my assumptions (listed in `reaudit_p3.py`); outcomes are exact distributions from them. "Old" = the earlier 8-item cuts (6-8 join, 4-5 support, 0-3 down) applied to today's 12 items.

| Profile | Typical result (warm / main / stretch) | Current-rule recommendation | P(join) / P(chat) / P(L2 outright) | Old cuts: P(L2 recommended) | Right level for the lessons? |
|---|---|---|---|---|---|
| A strong-for-age (9) | 4 / 5 / 1 | Join L3, try the L4 check | 0.97 / 0.03 / 0.00 | 0.01 | Yes. L4 check offer is reasonable |
| B typical (9) | 4 / 4 / 0 | Join L3 | 0.65 / 0.33 / 0.02 | 0.27 | Yes, and mostly a clean "join" now |
| C weak-for-age (9) | 3 / 1 / 0 | Suggest L2 | 0.03 / 0.40 / 0.57 | 0.98 | Mostly yes; 40% get "chat, L3 with support" |
| D younger strong (7, end of P2) | 4 / 3 / 1 | Chat, L3 with support | 0.19 / 0.64 / 0.17 | 0.48 | Mostly yes (17% still told L2 despite 4/4 warm-up) |
| E older weak (10, P4) | 3 / 2 / 0 | Chat, L3 with support | 0.15 / 0.59 / 0.26 | 0.84 | Mostly; 26% outright and 11% "may be more comfortable" still point a 10-year-old at ages 7-9 |
| F rushes/guesses (9) | 3 / 3 / 0 | Chat, L3 with support | 0.39 / 0.53 / 0.08 | 0.59 | Mostly; lands in chat band, not demoted |

Guessing cannot pass: every main answer is open (not multiple choice). The risk remains careless slips, which the wide middle band now absorbs.

### 5.4 Verdict
Before: **mostly** (decent first filter, noisy cuts, wrong-way pushes for three profiles, wording issue). Now: **mostly yes, clearly better**: strong and typical children land right with high probability, the worst age and rushing mis-placements fall by half to two thirds, and a soft middle band does the hedging. It is still a guide, not a placement test, and the site/doc rule contradiction, coverage gaps and age blindness are open.

Recommended exact fixes not yet applied: (1) delete "Open to a year either side" and "Choose the level that fits the score, not the school year" (they contradict each other and the table); (2) in the 0-1 row add "If your child is 10 or older, please talk to us first: Ages 7-9 may not be the right fit"; (3) remove the "2.05 and $2.05" line from the Level 3 key; (4) change "do not count against the child" to "they score 0 but tell the tutor what to teach first; a tutor chat comes before any decision"; (5) update `docs/levels_and_placement.md` and `website/lp_build.py` to the 4-6 / 2-3 / 0-1 rule; (6) add one 6/8/9-table item (e.g. "I am in the 7 times table, between 40 and 60, digits add up to 11: 56") as a second stretcher.

---

## 6. Regressions, and logs that claim more than the content shows

**A. Things that got worse or were newly introduced**
1. L10 explore now runs two 7-minute stations against a visible timer (fix #4 in `fixes_p3.md`). New time pressure; L10 LOW 3.67 -> 3.17, MIDDLE 4.50 -> 3.83. Part of that fall is my stricter scoring; the timer is real. The fix did cut materials and reading.
2. Look-back box tells the child "my tutor will check in with me" while the tutor cannot see the page (`fixpass_p3.md` calls the contradiction resolved). It is only half resolved.
3. Level labels diverge. The rebuilt diagnostic and docs say "Builds on Primary 3 maths" (commit `9ae1a31`) but the Question Bank, Taster, Weekly Email Pack (6 times), What-Learners-Get and the Tutor Guide ("Level: Children finishing Primary 3 (ages 9 to 10), going into P4, who are ready for more thinking than standard practice") still say "(finishing P3)" and ages 9-10, against the stated band 8-10.
4. The website and `levels_and_placement.md` state a placement rule that disagrees with the printed sheet (section 5.2).
5. Weekly Dose still headed "Challenge" on every lesson and says "keep the weekend for the Challenge questions"; the Weekly Email Pack says "we may invite them to a short challenge session in the next holiday". Disclosed as a known limit in `fixpass_p3.md`, but it is a sorting signal to parents that survives the "no public labels" fix.

**B. Logs that over-claim**
- `gifted_fixes_p3.md`: "after rework 100% compliant" -> 96.4% strict, 98.4% like-for-like (11 and 5 items).
- `gifted_p3.md` "after" rubric 17.7: now 20.3, but criteria 2 and 11 (and 5, 8) are exactly where the original audit said the three biggest gaps were, and they have not moved.
- `fixpass_p3.md` build changes still marked "needed in `diag/build_diag.py`": "Open to a year either side" not deleted, 2.05 boilerplate not removed, within-one-mark and retest lines absent, age and warm-up conditions for the low band absent.
- `close_gaps_p3.md` introduced a printed fast-track box; `fixpass_p3.md` removed it (verified gone). Fine, but the close-gaps compacting idea (skip mastered material) was dropped, so criterion 11 stays at 1.
- `fixpass_p3.md` says the guide, notes and packs carry one consistent wording. True for the tier names; not for the level label (3 above) and the Weekly Dose heading.

**C. Score falls that are mostly rater difference, not content change**
L6 LOW and MIDDLE (-0.50): the L6 pages are essentially unchanged since the earlier review except Q7 moved to Think harder and the strip note; I score Q2 (7 parts) and Q4 (6 unlike sums) harder than the earlier review did. L3 HIGH (-0.33), L1/L4 MIDDLE (-0.17): fit and participation set one point lower by me. No evidence of a content regression behind them.

---

## 7. Remaining gaps (ranked)
1. **Depth over speed and compacting (criteria 2, 11, both 1 in all ten lessons).** Start-here is still 6 questions and 12-20 parts in about 22 minutes, Think harder and Go further share a 3-minute slide slot, every group follows the same slides, and the sneak-peek never lets anyone skip anything.
2. **LOW persona still 3.15 (fit 2.6, confidence 2.7).** Weakest: L2 (no page-1 win), L6 (Q2/Q4 load), L9 (decimal sums, 24-hour, five topics), L3 (6-9 table fluency). Reading load unchanged.
3. **Tier residuals.** 11 strict items (seven whole Think-harder-level questions on the Start-here page, L6 Q4, four bank items) and the structural point that printed Start-here pages are post-teaching practice, so true low-floor-without-teaching is delivered by the sneak-peek and by hints, not by the page itself.
4. **Online and safeguarding details.** Unvisited breakout rooms, the "still stuck" promise, whiteboards visible to the gallery, parent-facing "challenge session" invite.
5. **Diagnostic.** Rule contradicted by the website and docs; no age or warm-up logic in the low bands; coverage skips tables 6/8/9, L1, L8, L9, L10; "not learnt yet" ticks score 0.
6. Housekeeping: stale "(finishing P3)" labels, Weekly Dose "Challenge" heading, Tutor Key "2.05" line, slide-only Think-harder items in L5-L8 that are not in the bank, guide or parent packs.

---

## 8. Summary

1. Rubric (Instrument A) level mean: 15.7 before / 17.7 claimed after / **20.3 now** (lessons 19-22, eight of ten at 20-21: lower edge of "depth-oriented"). Real gains: criteria 6, 9, 10. Unmoved: 2 depth, 5 paths, 8 complexity, 11 pacing.
2. Journey (Instrument B) persona means before -> now: LOW 2.93 -> 3.15, MIDDLE 3.93 -> 3.92, HIGH 4.28 -> 4.37. LOW gains in L3, L5, L8, L9; LOW fit (2.6) and confidence (2.7) still lowest.
3. Tier compliance: 77% before, 100% claimed, **96.4% now strict (11 of 306 fail), 98.4% like-for-like**; bank Core 60/60.
4. Diagnostic: before "mostly"; now "mostly yes, clearly better" (typical child clean join 19% -> 65%, wrong-way Level 2 pushes down by half to two thirds), with the site/docs rule, coverage and age logic still open.
5. Top gaps: (a) pacing/depth and no compacting (criteria 2, 11); (b) LOW child in L2, L6, L9, L3; (c) 11 residual tier items plus post-teaching Start-here pages; (d) online safeguards (unvisited breakout rooms, "still stuck" promise); (e) diagnostic rule contradicted by website, no age/warm-up logic, tables 6/8/9 untested.
6. Regressions/new problems: L10 visible 7-minute timer; stale "(finishing P3)" and ages 9-10 labels in six P3 documents; website and `levels_and_placement.md` still show the 70/40/90% rule; Weekly Dose "Challenge" heading and "challenge session" invite.
