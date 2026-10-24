# Re-audit of Math Inquirers Level 4 (Primary 4, ages 9-11)

Independent re-score of the CURRENT material on the same two instruments as the earlier audits, then a like-for-like comparison. Desk review by a model: no children were observed, every score is a judgement about written material, and nothing here measures learning. Helper script with all arithmetic: `docs/audit/reaudit_p4.py` (`python3 docs/audit/reaudit_p4.py` prints the answer-key checks, the diagnostic probabilities and every comparison table below). No content, build or output file was edited.

## 0. Headline (read this first)

| Measure | Before (original) | Earlier "after" claim | Re-audit now | Comment |
|---|---|---|---|---|
| Rubric, level mean /24 | 13.9 | 14.5 | **19.6** raw; **18.5** strictness-aligned | The 14.5 claim predates the close-gaps and student-journey passes, which were never re-scored; the gain is real but about 1 point of it is my more lenient reading (section 4.7) |
| Journey heatmap mean, LOW / MIDDLE / HIGH | 2.97 / 3.77 / 3.80 | none | **3.03 / 3.80 / 3.82** | Flat. Gains in participation and social/online are offset by lower fun and motivation scores from my stricter reading of the number-heavy lessons. Differences under about 0.5 per cell are inside the noise of two auditors |
| Tier compliance, original item set | 264/324 = 81.5% | 100% | **293/329 = 89.1%** (about 94% if the workbook core page is judged as leniently as the original did) | Question-bank Core is now clean (60/60); the printed "Start here" pages are the weak part (42/60) |
| Diagnostic | "mostly" places correctly; 1 in 3 correctly placed children shown a step-down or support message; younger-strong, older-weak and rusher mis-placed | all fixed | **mostly; clearly better for three profiles, worse for two** | Wording and noise largely fixed; the older-weak child and the weak child are now more often told to join; three conflicting placement rules remain; much of the "fixed" wording lives only in an unused JSON block |

Top remaining gaps (detail in section 6): (1) depth over speed and pacing are untouched (rubric C2 and C11 still 1/2 everywhere); (2) the printed "Start here" pages are still not low-floor in 18 of 60 questions (worst: L4, L7, L9) and Think harder is too easy in L9 and L10; (3) the LOW child's difficulty fit is exactly as low as before (2.2 / 5) because lessons 3, 4, 5 and 6 still open on the lesson's own skill and page 2 is 18 minutes solo; (4) the diagnostic has three different placement rules in the repo, an unused `placement` block, and no route for an older weak child; (5) parent-facing flyers and tutor notes still carry the old tier language (Challenge Group, "Think harder Q7" on Go further slides, slide Think harder items that are not the printed ones).

Regressions: no lesson content got worse in a way I can evidence. Trade-offs and small regressions are in section 5 (reflection lost its "what I would try next" prompt; diagnostic older-weak and try-up behaviour; the stretch reassurance is printed twice; a few lesson-persona cells fell by 0.3 to 0.5).

---

## 1. Method, coverage and honest limits

- Phase 1 (blind) was written before I opened any earlier audit file. I read `docs/gifted_research.md` section 2 and 3, the two brief templates, then the current material: `p4/content/l1.js` to `l10.js` (lesson, script, deck, qbank, workbook, `gaps`), `p4/data.js`, `p4/workbook_html.js`, `rebuild/gen_p4l*.py`, all 285 built slides and their speaker notes in `split/p4l*/project/slides` (text and notes extracted), the rebuilt PDFs (workbook 64 pp, tutor guide 83 pp, question bank 28 pp, weekly packs), `diag/content/p4.json`, `diag/build_diag.py`, and the built `Math_Inquirers_Level4_Placement_Check.pdf` and `Math_Inquirers_Level4_Tutor_Key.pdf`.
- Coverage limits: I read the lesson 1 tutor script in full and the other nine through their slide notes and the `gaps`/investigation keys, not line by line. I did not render page images; I read the extracted PDF text, so layout problems (overflow, figure clashes) are not assessed beyond what the logs report.
- Answers: 21 answer-key claims (find-all, unique-answer and count claims in all 10 lessons) were re-computed by brute force in `reaudit_p4.py`; all pass. I found no wrong key in what I checked.
- Phase 2 (compare) used `gifted_p4.md`, `gifted_fixes_p4.md`, `journey_p4.md`, `fixpass_p4.md`, `close_gaps_p4.md`, `fixes_p4.md`.
- Journey scale: as in the original review I score difficulty fit as 5 = just right (note says too hard / too easy), so a mean of six works. Persona scores are 1-5, 5 best.

---

## 2. PHASE 1 (blind): instrument A, gifted-style rubric

### 2.1 Evidence behind each criterion (applies to all ten lessons unless an exception is listed)

The programme is built on one template, so most evidence is shared. Lesson clock: sneak-peek 1-4, game 4-6, quick questions 6-8, explore 8-18, mini-lesson 18-30, break 30-34, page 1 in pairs 34-50, check 50-53, teach 53-58, page 2 solo 58-76, check 76-80, talk 80-85, exit 85-88, looking back 88-90.

| # | Criterion | Score | One-line evidence |
|---|---|---|---|
| 1 | Low-floor, high-ceiling | 2 all | Sneak-peek puzzle 1 ("Try it", objects/drawing/counting), explore with objects at 8-13, "Go further (any time)" printed on the explore slide, and an Investigation with an "Easy first step" whose tutor key states the expected range (e.g. L1 "six pairs ... 3 or 4 pairs with an explanation is doing well"). Caveat: the Investigation is not on the clock. |
| 2 | Depth over speed | 1 all | 5-7 multi-part questions per page pair (11-21 sub-items; L7 272 words and 21 sub-items on page 2) in 16 and 18 minute slots; printed caps ("Aim for Q4 and Q5 first. Q6 is a choice") help, but 17 of 90 minutes are tutor-led teaching and 4 are "check together". |
| 3 | Abstraction / generalisation | 2 in L1-5, L7, L8; 1 in L6, L9, L10 | Scheduled talk-time claim ("Ali: bigger numbers always have more factors"; "Mei: double rounding"; "Mei: a row of four always folds") plus Investigation "Is it always true? / What stays the same?". L6, L9, L10 mostly ask for specific answers; generalisation only in an unscheduled Investigation part. |
| 4 | Justification | 2 in L1, L2, L3, L5, L7, L8, L9; 1 in L4, L6, L10 | Counterexample items (L1 Q6b, L2 Investigation 1 449/1 450, L5 Q2b Ben, L7 Q5c Ali and Q6c Mei's error, L8 Q1 "explain why", L9 Q1d/Q5b). L4/L6/L10: "explain" is a description of steps. |
| 5 | Multiple solution paths | 2 in L4, L7, L10; 1 elsewhere | L4 three comparing tools and "which tool is quickest" (`teachcompare2`); L7 area two ways that must agree (`we1`); L10 four ways in and "which way in did you use most?". Elsewhere one taught method, alternatives only as hints. |
| 6 | Challenge ladder inside the lesson | 2 all | Neutral tiers by choice: sneak-peek access question, "Start here", "Think harder", "Go further", "Investigation"; "After question 3 you may choose"; invitation to the whole group; nobody named. Caveat: the first rung is wobbly where "Start here" is not low-floor (L4, L7, L9). |
| 7 | Student-led inquiry and talk | 2 all (lenient) | Pair explore, "talk about it" prompts, sentence starters, volunteers first, no cold calls, answers asked for before they are shown. Against it: 12-minute tutor think-aloud plus 5-minute teach block, answers revealed by click, noticings recorded only in Investigation (b). |
| 8 | Complexity / real-world | 1 in all but L9 (2) | Hawker, bus and MRT contexts are a thin coating on one variable. L9 "Sales have doubled!" asks what the newspaper should add: ambiguity and media literacy. |
| 9 | Creativity and problem posing | 2 in L1, L3, L4, L5, L6, L8, L9, L10; 1 in L2, L7 | Go further "make up your own" in every lesson plus an Investigation that alters conditions ("what if the gap is 9? a straight line? both squares above?", L9 re-scale). L2 and L7 have the single optional posing item and no "what if" Investigation. |
| 10 | Metacognition | 2 all | "Looking back" box on page 3 (something I did well / the hardest part / what helped, with strategy ticks, "still stuck" and "pass"), tutor models it (slide `reflect`, 88-90). Missing: "what I would try next" and it is the last two minutes. |
| 11 | Pacing flexibility / compacting | 1 all | Self-choice after Q3, Go further from minute 8, optional "your turn" slides. But the sneak-peek is explicitly not used to route ("does not decide who is on which page"), the mini-lessons are whole-group lockstep and there is no skip path. A reader who accepts self-choice as compacting would score 2. |
| 12 | Extension, not acceleration | 2 all | Stays inside P4 topics; extends through structure (odd factor counts, double rounding, density of decimals, clock angles, fencing optimisation, cube nets, misleading scales, the 3-and-5 ring-toss coin problem). Minor drift: L5 decimal division by 6, L4 find-the-whole with unlike fractions. |

### 2.2 Scores per lesson (re-audit now, before opening any baseline)

| Lesson | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 | C10 | C11 | C12 | Total /24 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L1 Factor Hunters | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 20 |
| L2 Big Number Puzzles | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 19 |
| L3 Operation Detectives | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 20 |
| L4 Fraction Frontier | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 20 |
| L5 Decimal Detectives | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 20 |
| L6 Angle Turns | 2 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 18 |
| L7 Area Architects II | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 20 |
| L8 Symmetry and Nets | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 20 |
| L9 Data Detectives | 2 | 1 | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 20 |
| L10 Challenge Day | 2 | 1 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 19 |
| **Level mean** | | | | | | | | | | | | | **19.6** |

Sensitivity: scored only on what every child meets on the 90-minute clock (dropping the unscheduled Investigation and Go further), C9 falls by 1 in most lessons and C3 in a few, giving about 18. This is a score of design features, not of delivery.

Lesson-specific notes (strengths / gaps) that explain the 1s and 2s above:

- L1: strong low-floor tile explore, locker problem and six-pair bus Investigation; gap: Q5 and Q6 on the "Start here" pages are Think harder in disguise.
- L2: double-rounding Investigation is the best conjecture-test task in the level; gap: page 1 opens on a rounding table; posing only via optional Q6.
- L3: no race in Target Numbers any more; strong number-trick and make-the-target tasks; gap: Q1 and Q3 need the printed order-of-operations rule.
- L4: only lesson with explicit comparison of three methods; gap: Q4 (five comparisons), Q5, Q6 are not low-floor; "write how you know" is description.
- L5: Siti's "no decimal between 0.35 and 0.36" is a real density idea; gap: densest lesson (thousandths, backward rounding, mass with division by 6).
- L6: hands-on turning and compass; gap: workbook opens on a protractor task, generalisation and justification thin.
- L7: area two ways, push-out perimeter, fencing proof by listing; gap: 21 sub-items, Think harder Q1 and Q2 repeat Core Q2.
- L8: cut-and-fold start, "row of four" Investigation (all 16 placements fold: re-checked), design-your-own dice; gap: Q6 find-all on the Start-here page.
- L9: the only 2 for context ("which graph is honest?"); gap: Think harder Q2, Q3, Q4 are core level.
- L10: four ways in, ring-toss coin problem; gap: Think harder Q4, Q5 and bank Challenge Q7 repeat a taught one-step method; little generalisation.

### 2.3 Tier compliance (Phase 1)

Principle used (template STEP 2): Core must be approachable without prior teaching; Think harder needs the taught idea in a new setting; Challenge needs mastery plus extension. Classified: every question-bank item (Core 60, Think harder 89, Challenge 90), every printed "Start here" question (60), and the three Think harder items on each Think-harder slide (30). The printed Think harder page (items 1-4) and Go further page (items 5-7) are items of the bank, so they are counted once, through the bank. My rule for the printed Start-here page: compliant only if the printed scaffold lets a child who has not met the method make a start by drawing, counting, a table, a grid or guess-and-check; a question that needs the lesson's formal rule or is really find-all / generalise / justify is a violation.

| Lesson | Bank Core | Bank Think harder | Bank Challenge | Printed Start-here | Slide Think harder | Total |
|---|---|---|---|---|---|---|
| L1 | 6/6 | 8/8 | 9/9 | 4/6 | 3/3 | 30/32 |
| L2 | 6/6 | 6/8 | 9/9 | 4/6 | 2/3 | 27/32 |
| L3 | 6/6 | 10/11 | 8/9 | 5/7 | 2/3 | 31/36 |
| L4 | 6/6 | 8/9 | 9/9 | 3/6 | 2/3 | 28/33 |
| L5 | 6/6 | 11/11 | 9/9 | 4/6 | 3/3 | 33/35 |
| L6 | 6/6 | 9/9 | 9/9 | 5/6 | 3/3 | 32/33 |
| L7 | 6/6 | 9/9 | 9/9 | 4/6 | 3/3 | 31/33 |
| L8 | 6/6 | 8/8 | 8/9 | 5/6 | 3/3 | 30/32 |
| L9 | 6/6 | 5/8 | 9/9 | 3/5 | 1/3 | 24/31 |
| L10 | 6/6 | 5/8 | 8/9 | 5/6 | 3/3 | 27/32 |
| **All** | 60/60 (100%) | 79/89 (89%) | 87/90 (97%) | 42/60 (70%) | 25/30 (83%) | **293/329 (89.1%)** |

Violations, with reason:

- Printed Start here (18): L1 Q5 (count factors of six numbers, "exactly 3", predict 49: generalisation), L1 Q6 (riddle plus justify Ravi/Mei: Think harder); L2 Q2 (work backwards smallest/largest, find ALL), L2 Q4 (two-clue riddle; "digits add to 2, find ALL"); L3 Q1 (a-e need the order-of-operations rule printed in the header), L3 Q3 (brackets to hit 57 and 20 need the rule); L4 Q4 (five comparisons with unlike denominators), L4 Q5 (find the whole from a part), L4 Q6 (find ALL twelfths between 1/3 and 3/4); L5 Q2 (three-decimal-place ordering plus a misconception), L5 Q3 (round backwards on a hundredths line); L6 Q1 (protractor measurement first; protractor is "bring from home"); L7 Q4 (staircase push-out insight), L7 Q6 (frame by subtraction plus error analysis); L8 Q6 (shade one more square, find ALL on three grids); L9 Q3 (two-line graph and week-8 extrapolation), L9 Q5 (argue why two graphs look alike); L10 Q6 (ages, "3 times as old in 5 years").
- Bank Think harder (10): L2 S7 (smallest and largest difference of two rounded crowds: Challenge level), L2 S8 (largest odd 5-digit number with different digits: place value only); L3 S5 (120 - 4 x (18 + 7): one step of the taught method); L4 S7 (quarters in 4 3/4: one conversion); L9 S2, S3, S7 (one- or two-step reading and subtraction; S7 repeats the exit ticket); L10 S4, S5, S7 (three ages in order; a queue like Core Q4; three next-door numbers).
- Bank Challenge (3): L3 X2 ($56 more, total $300: one-step bar model), L8 X5 (four side faces add to 14: recall of 7 + 7), L10 X7 (15 tables of 4 or 6 seats: the taught "suppose" method in one step; same item as Go further Q5).
- Slide Think harder (5): L2 item 2 (descending pattern, core level), L3 item 1 (evaluate 7 x (40 - 4 x 8)), L4 item 1 (halves in 6 1/2), L9 items 1 and 2 (biggest change; scale arithmetic).
- Borderline I counted as compliant: bank Core items that name decimals or fractions (L5 Core 5 and 6 use 0.47 m and 3.65 on number lines, L4 Core 1 "11 thirds") because each has a drawing or number-line route.

Printed Think harder pages (4 items x 10) are 37/40 compliant by the same rule, and the Go further pages are 29/30 (the one miss is L10 Q5).

---

## 3. PHASE 1 (blind): instrument B, student journey

Method: I walked the real slides (every slide's text and notes), the workbook pages and the investigation/reflection page for each lesson as three typical children. Scores order: Participate / Difficulty fit / Fun / Confidence / Motivation / Social-online (5 best; fit 5 = just right, note says too easy / too hard). The new items:

- Sneak-peek (1-4): slide says "Ideas we have not learnt yet. Guesses and 'I do not know' are welcome. Nobody is marked. ... Only your tutor looks." Puzzle 1 is an access puzzle (counters, drawing, counting), puzzle 2 a short thinking puzzle. It does not label anyone: it routes nobody ("It does not decide who is on which page"). One wording problem: "Only your tutor looks" while sheets are "held to the camera at the same moment for everyone" on a group call.
- Fast track: absent from workbook, slides and guide (verified by search across all P4 PDFs and decks). Choice is "After question 3 you may choose: carry on, or try Think harder", invited to the whole group, "never announce who is on which page", "do not split the pair unless both agree".
- Looking back: three plain prompts, strategy ticks, "I am still stuck (my tutor will check in with me)", "I pass today (that is fine)", "Nobody marks this. It is not shown to the group." It is safe for a low-confidence child. It is still the last 2 minutes and has no "what I would try next".

### 3.1 Scores and evidence per lesson

Evidence names the slide id (`check`, `warm1`, `explore1`, `we1`, `ws1`, `ws2`, `talk`, `exit`, `reflect`) or workbook item (Q = "Start here" question; TH = Think harder; GF = Go further; Inv = Investigation). Reading load (words): page 1 / page 2 of the Start-here pages.

| Lesson | Persona | P / F / Fun / C / M / S (mean) | Evidence |
|---|---|---|---|
| L1 | LOW | 4/2/4/3/3/3 (3.17) | `check` Q1 12 sweets with counters is a first win; tiles in `explore1`. Fit: p1 (235 words) OK with the 1 x 48 start, but p2 (277 words) Q5 six-number factor table and Q6 four-clue riddle are solo, 18 min, and need 6-9 tables. Fizz-Buzz now "my go again", but it is still counting aloud round the tiles. Q6 is "a choice", which protects confidence. |
| L1 | MIDDLE | 5/4/4/4/4/4 (4.17) | Both `check` puzzles startable; `we1`-`we3` worked examples; Q5 and Q6 are reachable with steps; buses and tiles are concrete. |
| L1 | HIGH | 5/3/4/4/4/3 (3.83) | Q1-Q3 routine for the first 16 min; TH Q1-Q3 same type; GF Q5 (Bus C find ALL, make up a puzzle) and Q7 lockers are the stretch; Inv (c) six pairs. Pair rule keeps the HIGH child with a partner on Q1-Q3. |
| L2 | LOW | 4/2/3/3/3/3 (3.00) | `check` Q1 number line with a dot at 7 500 is drawable. Fit: rounding to the nearest 1 000 of a 5-digit number; Q1 table cut to 47 285 and 63 950 but Q2 "work backwards" and Q4 riddles are on page 2; hint lines ("63 500 is halfway") help. Place It Right (`warm1`) is fun but numbers are read aloud. |
| L2 | MIDDLE | 5/4/3/4/3/4 (3.83) | Digit-card explore is good; Q1 and Q6 are drill-like; no visible progress except the stamp. |
| L2 | HIGH | 5/3/4/4/4/4 (4.00) | Q1, Q3 trivial; Q2b find ALL, Q4b digits add to 2; Inv double rounding (test 1 449 and 1 450) is excellent; GF palindrome odometer. |
| L3 | LOW | 4/2/3/2/3/3 (2.83) | `check` Q1 (2 bags of 4 and 3 loose, draw) is a win; Target Numbers has "no race and no points"; quick questions now 48 / 6, 9 x 6, 4 x 20. Fit/confidence: Q1 a-e need the rule printed in the header, Q1c 72 / 8 x 3 and Q3 brackets are the traps, 7 questions across two pages (231/241 words) reduced by the cap "Aim for Q4, Q5, Q6; Q7 is a choice". |
| L3 | MIDDLE | 5/4/3/4/3/4 (3.83) | Order of operations fits; Q4 machine, Q5 trick with fill-in explanation, Q6 bar model; computation-heavy so fun 3. |
| L3 | HIGH | 5/3/3/4/3/3 (3.50) | Q1-Q3 easy; TH Q2 and Q3 repeat Q3 and Q2; GF Q5 (both ways to make 7) and Q7 (own number trick) are good. |
| L4 | LOW | 3/2/3/2/3/3 (2.67) | `check` Q1 fold-a-strip access is fine, but Q1 header defines improper and mixed in one line, Q1 b-d are number conversions (19/4, 3 2/5, eighths in 5), Q4 has five comparisons with unlike denominators (fraction wall is in the cut-outs), Q4c asks "write how you know". 13 sub-items. |
| L4 | MIDDLE | 4/3/3/3/3/4 (3.33) | Pizza circles/folding are good; `teachcompare`/`teachcompare2` give three tools in 3 minutes; p2 Q4-Q6 dense. |
| L4 | HIGH | 5/3/3/4/3/3 (3.50) | Conversion and comparison quick; GF Q6 (half is 3 more than a third), Q7 (Siti's book) and Inv (60 stickers: common multiple link to L1) are the stretch. |
| L5 | LOW | 3/2/3/2/2/3 (2.50) | `check` Q1 coins; densest number lesson: Q1 reads 0.247 on a zoomed line, Q2 3-place ordering plus Ben's misconception, Q3 rounding backwards, Q6 mass with 2.40 / 6. Motivation 2: no easy early run. |
| L5 | MIDDLE | 4/3/3/3/3/4 (3.33) | Q4 cards 3, 6, 9 and Q5 bar model are fine; thousandths and rounding back are heavy. |
| L5 | HIGH | 5/3/3/4/3/4 (3.67) | Q1 and Q4 routine; TH Q4 mystery decimal (4.687) and GF Q5 (make your own "closest to" puzzle, swap) and Inv (Siti) are the fun. |
| L6 | LOW | 3/2/4/3/3/3 (3.00) | `check` stand-up quarter turns is a win, but the worksheet opens on Q1 protractor measurement (protractor is "bring from home"; inside/outside scale; mirrored self-view note). Compass turns Q4 and corner subtraction Q5 are countable; compass dance (`break`) is fun. |
| L6 | MIDDLE | 4/4/4/3/4/4 (3.83) | Estimate-then-measure, fan Q2, clock and compass fit well. |
| L6 | HIGH | 5/3/4/4/4/4 (4.00) | Q3-Q6 quick; GF Q7 overlapping squares and Q5 pose a clock puzzle; Inv splitting a corner (7 sets). |
| L7 | LOW | 4/2/3/3/3/3 (3.00) | `check` Q1 picture of 5 x 3 with a corner out (count squares); 12 tiles in `explore1`. Fit: p1 Q1 L-shape (missing lengths, area two ways, perimeter), p2 Q4 staircase, Q6 frame; 272 words and 21 sub-items on p2. The grid lets a child count squares first. |
| L7 | MIDDLE | 4/3/4/3/4/4 (3.67) | Tiles, area two ways agreeing is satisfying; p2 dense. |
| L7 | HIGH | 5/3/4/4/4/3 (3.83) | Q2, Q3 routine; TH Q1 and Q2 repeat Q2; GF Q5 fencing (prove by listing) and Q7 are good. |
| L8 | LOW | 5/3/4/4/4/3 (3.83) | Cut and fold six squares, `check` Q1 draw fold lines on an H, no arithmetic; a finished cube. Fit 3: Q3 dice sums and Q6 find ALL are harder; 174 words. Needs scissors and tape at home (squares come from the Square grid page). |
| L8 | MIDDLE | 5/4/5/4/4/4 (4.33) | Best lesson: cut-outs for Q1, dice nets, mirror partner break. |
| L8 | HIGH | 5/3/4/4/4/4 (4.00) | Q1-Q5 easy; TH Q4 tetromino symmetry, GF Q6 (6 ways) and Q7 (2 ways), Inv "row of four" always folds. |
| L9 | LOW | 4/3/3/3/3/3 (3.17) | `check` Q1 three bars; Q1 reads a line graph with a scale of 10 and faint lines at 5; Q2 table totals are doable; p2 Q3 (week 8 extrapolation) and Q5 (two scales) are hard. Graph grids are in the kit. |
| L9 | MIDDLE | 5/4/3/4/3/4 (3.83) | Reading, changes and totals fit. |
| L9 | HIGH | 5/3/3/4/3/3 (3.50) | Q1, Q2 routine; TH Q2, Q3, Q4 are core level; GF Q5-Q7 and Inv "Sales have doubled!" are strong; checks on pages already done. |
| L10 | LOW | 4/2/4/3/3/3 (3.17) | `check` Q1 five ducks (draw); mixed review: Q1b find ALL ($4 pens and $7 books), Q6 ages with bars on page 2; the fill-ins in Q2 a-c scaffold "suppose"; three of four puzzle cards. |
| L10 | MIDDLE | 5/3/4/3/4/4 (3.83) | Puzzle cards and hawker contexts are fun; logic grid and queue fit. |
| L10 | HIGH | 5/4/5/4/4/4 (4.33) | Best fit: GF Q6, Q7 (pose a heads-and-legs puzzle with one answer), Inv ring toss (impossible 1, 2, 4, 7; with 4 and 6 only 2 and odd numbers). |

Heatmap now (mean of six): LOW 3.03, MIDDLE 3.80, HIGH 3.82. Dimension means (LOW / MIDDLE / HIGH): participate 3.8 / 4.6 / 5.0; difficulty fit 2.2 / 3.6 / 3.1; fun 3.4 / 3.6 / 3.7; confidence 2.8 / 3.5 / 4.0; motivation 3.0 / 3.5 / 3.6; social/online 3.0 / 4.0 / 3.5.

Concrete moments (current material):

- Exposed or "stupid": Fizz-Buzz counting round the video tiles (L1, softened to "my go again"); reading digit numbers aloud (L2, L5); sneak-peek puzzle 2 is a cold test of an untaught idea (guessing is explicitly welcome) and "only your tutor looks" is not enforceable on a group call.
- Lost: L3 Q1 relies on a printed rule; L4 Q1 "improper fraction / mixed number" defined in one line; L5 Q1 thousandths; L6 protractor scale and no protractor in the kit.
- Rushed: page 2 is 18 solo minutes with 5-7 questions and 11-21 sub-items; teach-before-page-2 (53-58) packs 3-4 ideas in L4, L5 and L6.
- Waiting (HIGH): about 29 whole-group minutes before the worksheet (check 3, game 2, quick 2, explore 10, mini-lesson 12); Go further is available from minute 8 on the explore slide but the 12-minute mini-lesson is lockstep; a HIGH child who finishes Q3 early may be held by the pair; checks at 50-53 and 76-80 are for everyone.
- Left out: protractor (L6) is the only item not supplied or suggested as a substitute; scissors and tape (L4, L6, L7, L8) are "bring from home" (the six squares for L8 come from the Square grid page); digit cards, signs, brackets, graph grids, paper clock and pizza circles are now printed.
- First win for LOW inside the first 10 worksheet minutes (minutes 34-44): the first part of Q1 is winnable in L1 (1 x 48 given), L2 (47 285 to 10), L3 (36 + 14 x 5 with the stickers story), L4 (count shaded fifths), L5 (6.3 on a tenths line), L7 (grid), L8 (tick shapes that fold), L9 (read Thursday), L10 (table). Doubtful: L6 (protractor first). So 9 of 10, up from the original review's 2 clear and about 4 likely.

### 3.2 PHASE 1 (blind): diagnostic

Current rule, as built (`diag/build_diag.py` page 3, which ignores the `placement` block in `diag/content/p4.json`): main questions (6) decide. 4 to 6: join Level 4, and with 1 or more brain stretchers right "you could try the Ages 10-12 (Level 5) check". 2 or 3: "a short chat with a tutor and the free taster", Level 4 with a little support, and if warm-up is 2 or less Level 3 "may be the more comfortable start". 0 or 1: "We suggest Ages 8-10 (Level 3)". Warm-up never changes the 4-6 row.

Skill demand and fairness of the twelve questions (all arithmetic re-computed): warm-up 9 x 7 = 63, 2/3 = 8/12, 7 x 6 area with units, 5000 - 1346 = 3654 are Primary 3 skills (fair for ages 9-11, ordered easy to hard). Main: factors of 18 (defined in the question, fair), round 48 572 to the nearest thousand = 49 000, 12 + 6 x 3 - 4 = 26, 2 3/5 + 1 4/5 = 4 2/5, 3.7 + 2.85 = 6.55, perimeter 36 with side 11 gives width 7. Q10 (perimeter) is a Primary 3 skill, so the "main" set has five real Primary 4 questions. Stretch: 36, and Ben 36 (unique). The check samples number, fractions, decimals, area and perimeter and says so; angles, symmetry, nets and graphs are not in it.

Six profiles, run on the current rule (exact probabilities, my assumed per-question success rates, in `reaudit_p4.py`):

| Profile | Expected main /6 | Right level | Outcome distribution | Sensible placement |
|---|---|---|---|---|
| 1 strong for age | 5.4 | Level 4 | try-up flag 74%, join 24%, chat 1% | 99% |
| 2 typical for age | 4.6 | Level 4 | join 69%, try-up flag 16%, chat (Level 4 + support) 14%, Level 3 lean 1% | 99% |
| 3 weak for age | 1.8 | Level 3 | down 42%, chat with warm-up 2 or less (Level 3 lean) 32%, chat neutral 20%, join 6% | 73% |
| 4 younger but strong, topics not yet taught | 3.2 | Level 4 with support | chat (Level 4 + support) 55%, join or try-up 38%, down 7% | 93% |
| 5 older but weak (age 11) | 2.5 | Level 3 | Level 3 lean 35%, down 20%, chat neutral 26%, join 19% | 54% |
| 6 rushing / careless but able | 2.9 | Level 4 | chat (Level 4 + support) 45%, join 26%, Level 3 lean 13%, down 13%, try-up 4% | 74% |

Cut-score noise with six main questions: a child who truly gets 70% of items is told "join" 74% of the time, "chat" 24%, "step down" 1%; at 60% it is 54 / 41 / 4%; at 50% it is 34 / 55 / 11%. Free-response answers mean a blind guesser essentially cannot reach 4 of 6, so luck-up is negligible; the risk is slips on a six-item score (SD about 1.2 marks).

Wording of the parent page and key: friendly ("This is a friendly check, not a test", "tick not learnt yet and move on", "Found it hard? That is useful to know, and it says nothing about how clever your child is", "a confident start matters more than a fast one"). Residual issues: "not learnt yet" questions "score 0 but ... do not count against the child" in the key while page 3 sums them; the key does not say "do not mark in front of your child"; the Level 3 row never says older children are welcome; the stretch reassurance appears twice (printed in Q11's own text and again above the section).

---

## 4. PHASE 2 (compare): baselines opened after the above was written

### 4.1 Rubric per lesson: before, earlier claimed after, now

Cells show the re-audit score with the change from the ORIGINAL (pre-fix) score. "Claimed after" is the `gifted_p4.md` estimate after the tier rework only; no later pass re-scored the rubric.

| Lesson | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 | C10 | C11 | C12 | Now | Before | Claimed after | Strictness-aligned |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L1 | 2 | 1 | 2 | 2 | 1 | 2 (+1) | 2 (+1) | 1 | 2 (+2) | 2 (+1) | 1 | 2 | **20** | 15 | 16 | 19 |
| L2 | 2 | 1 | 2 (+1) | 2 (+1) | 1 | 2 (+1) | 2 (+1) | 1 | 1 (+1) | 2 (+1) | 1 | 2 | **19** | 13 | 14 | 18 |
| L3 | 2 | 1 | 2 | 2 (+1) | 1 | 2 (+1) | 2 (+1) | 1 | 2 (+1) | 2 (+1) | 1 | 2 (+1) | **20** | 14 | 14 | 18 |
| L4 | 2 | 1 | 2 (+1) | 1 | 2 | 2 (+1) | 2 (+1) | 1 | 2 (+2) | 2 (+1) | 1 | 2 (+1) | **20** | 13 | 14 | 19 |
| L5 | 2 | 1 | 2 (+1) | 2 (+1) | 1 | 2 (+1) | 2 (+1) | 1 | 2 (+1) | 2 (+1) | 1 | 2 (+1) | **20** | 13 | 13 | 19 |
| L6 | 2 (+1) | 1 | 1 | 1 | 1 | 2 (+1) | 2 (+1) | 1 | 2 (+2) | 2 (+1) | 1 | 2 (+1) | **18** | 11 | 12 | 17 |
| L7 | 2 | 1 | 2 | 2 | 2 | 2 (+1) | 2 (+1) | 1 | 1 (+1) | 2 (+1) | 1 | 2 | **20** | 16 | 17 | 19 |
| L8 | 2 | 1 | 2 (+1) | 2 | 1 | 2 (+1) | 2 (+1) | 1 | 2 (+2) | 2 (+1) | 1 | 2 | **20** | 14 | 15 | 19 |
| L9 | 2 (+1) | 1 | 1 | 2 | 1 | 2 (+1) | 2 (+1) | 2 | 2 (+1) | 2 (+1) | 1 | 2 (+1) | **20** | 14 | 14 | 19 |
| L10 | 2 | 1 | 1 | 1 | 2 | 2 (+1) | 2 | 1 | 2 (+1) | 2 | 1 | 2 (+1) | **19** | 16 | 16 | 18 |
| **Mean** | | | | | | | | | | | | | **19.6** | **13.9** | **14.5** | **18.5** |

Criterion means, before to now: C1 1.8 to 2.0; C2 1.0 to 1.0; C3 1.3 to 1.7; C4 1.4 to 1.7; C5 1.3 to 1.3; **C6 1.0 to 2.0**; C7 1.1 to 2.0; C8 1.1 to 1.1; **C9 0.4 to 1.8**; **C10 1.1 to 2.0**; C11 1.0 to 1.0; C12 1.4 to 2.0.

Verdict bands (research note: 20-24 depth-oriented, 12-19 enrichment-flavoured with gaps): before, every lesson was in or below the 12-19 band (mean 13.9); now six lessons sit at 20 raw but at 17-19 once strictness is aligned. The honest reading is **borderline depth-oriented on design features**: enrichment-flavoured with real depth features, not yet a programme that passes C2, C5, C8 and C11.

What moved, and why I believe it:

- C6 +1 in all ten: the ladder is now a printed, neutral, choose-your-own sequence (Start here, Think harder, Go further, Investigation) with the choice invited after Q3, instead of "Think harder is for early finishers or take-home". Verified in `ws1`/`ws2` slides and the workbook.
- C9 +1 to +2 in nine: a make-up-your-own item in Go further in every lesson (L1 Q5, L2 Q6, L3 Q7b, L4 Q5c, L5 Q5, L6 Q5, L7 Q5, L8 Q5, L10 Q7) and an Investigation that alters conditions in most (L1 bus gaps, L4 other fractions, L6 straight line, L8 both squares above, L9 re-scale, L10 4-and-6 rings). The original scored these as tutor-note-only (0).
- C10 +1 in nine: the "Looking back" box and the tutor model on `reflect`. (L10 already scored 2 originally for "write how you started".)
- C3/C4 +1 where an Investigation tests a claim (L2 double rounding, L5 between two decimals, L4/L8 conjecture parts).
- C1 +1 in L6 and L9 and C12 +1 in L3, L4, L5, L6, L9: the Investigations add number-structure tasks inside P4 content.

What did not move, and should not be claimed: C2 depth over speed (still 5-7 multi-part questions per page; the printed caps help but the clock is unchanged), C5 multiple paths (only L4, L7, L10), C8 context, C11 compacting (the fast track that could have scored was removed on safeguarding grounds, and the check deliberately routes nobody).

### 4.2 Journey heatmap, before and now (mean of six; before = `journey_p4.md`, which scored the 57-page state)

| Lesson | LOW before | LOW now | MIDDLE before | MIDDLE now | HIGH before | HIGH now |
|---|---|---|---|---|---|---|
| L1 | 2.83 | 3.17 (+0.33) | 3.83 | 4.17 (+0.33) | 3.83 | 3.83 (+0.00) |
| L2 | 2.50 | 3.00 (+0.50) | 3.67 | 3.83 (+0.17) | 3.83 | 4.00 (+0.17) |
| L3 | 2.17 | 2.83 (+0.67) | 3.50 | 3.83 (+0.33) | 4.00 | 3.50 (-0.50) |
| L4 | 3.00 | 2.67 (-0.33) | 3.67 | 3.33 (-0.33) | 3.67 | 3.50 (-0.17) |
| L5 | 2.17 | 2.50 (+0.33) | 3.33 | 3.33 (+0.00) | 3.83 | 3.67 (-0.17) |
| L6 | 3.50 | 3.00 (-0.50) | 4.00 | 3.83 (-0.17) | 3.33 | 4.00 (+0.67) |
| L7 | 3.17 | 3.00 (-0.17) | 3.83 | 3.67 (-0.17) | 3.83 | 3.83 (+0.00) |
| L8 | 4.00 | 3.83 (-0.17) | 4.17 | 4.33 (+0.17) | 4.00 | 4.00 (+0.00) |
| L9 | 3.33 | 3.17 (-0.17) | 3.67 | 3.83 (+0.17) | 3.00 | 3.50 (+0.50) |
| L10 | 3.00 | 3.17 (+0.17) | 4.00 | 3.83 (-0.17) | 4.67 | 4.33 (-0.33) |
| **Mean** | **2.97** | **3.03 (+0.07)** | **3.77** | **3.80 (+0.03)** | **3.80** | **3.82 (+0.02)** |

Dimension means across lessons, before to now:

| Dimension | LOW before | LOW now | MIDDLE before | MIDDLE now | HIGH before | HIGH now |
|---|---|---|---|---|---|---|
| Participate | 3.1 | 3.8 (+0.7) | 3.9 | 4.6 (+0.7) | 5.0 | 5.0 (0.0) |
| Difficulty fit | 2.2 | 2.2 (0.0) | 3.4 | 3.6 (+0.2) | 2.9 | 3.1 (+0.2) |
| Fun | 3.4 | 3.4 (0.0) | 4.0 | 3.6 (-0.4) | 4.0 | 3.7 (-0.3) |
| Confidence | 2.9 | 2.8 (-0.1) | 3.6 | 3.5 (-0.1) | 4.0 | 4.0 (0.0) |
| Motivation | 3.4 | 3.0 (-0.4) | 3.9 | 3.5 (-0.4) | 3.8 | 3.6 (-0.2) |
| Social / online | 2.8 | 3.0 (+0.2) | 3.8 | 4.0 (+0.2) | 3.1 | 3.5 (+0.4) |

Reading it: where the fixes changed content the scores moved the expected way. Participation rose (the access puzzle at minute 1, objects in every explore, printed digit/sign/bracket cards, graph grids and paper clock, scaffolds on L2-L5 Start-here items). Social/online rose, most for HIGH (+0.4): the fast-track labelling and the "boards up together" races are gone, `ws1` carries a whole-group choice line, and the pair-loss rule exists. Lessons 1, 2, 3 and 5 for LOW rose by 0.33 to 0.67 (cut tables, a story hint on L3 Q1a, no race, a 124-plate Q6, cut-down L5 Q3/Q4). Difficulty fit for LOW did not move at all (2.2): lessons 3, 4, 5 and 6 still put the lesson's own skill in the first worksheet items, and page 2 is still solo. Fun and motivation fell in my scoring (-0.3 to -0.4): that is mostly a stricter reading of number-drill lessons (L2-L5, L9), not a content change I can point to, and cells that moved by less than 0.5 should be treated as noise between two auditors. The six cells that moved by 0.5 or more are L2 LOW (+0.50), L3 LOW (+0.67), L6 HIGH (+0.67), L9 HIGH (+0.50), L3 HIGH (-0.50) and L6 LOW (-0.50).

### 4.3 Tier compliance, before and now

| Lesson | Before (original, lenient on workbook core) | Claimed after | Now (this audit's rule) |
|---|---|---|---|
| L1 | 24/32 (75%) | 100% | 30/32 (94%) |
| L2 | 27/32 (84%) | 100% | 27/32 (84%) |
| L3 | 25/34 (74%) | 100% | 31/36 (86%) |
| L4 | 24/33 (73%) | 100% | 28/33 (85%) |
| L5 | 25/33 (76%) | 100% | 33/35 (94%) |
| L6 | 25/33 (76%) | 100% | 32/33 (97%) |
| L7 | 29/32 (91%) | 100% | 31/33 (94%) |
| L8 | 25/32 (78%) | 100% | 30/32 (94%) |
| L9 | 30/31 (97%) | 100% | 24/31 (77%) |
| L10 | 30/32 (94%) | 100% | 27/32 (84%) |
| **Level** | **264/324 (81.5%)** | **100%** | **293/329 (89.1%)** |

What is real: bank Core went from 31/60 to 60/60 compliant and the Core bank is now a genuine low-floor set (objects, counters, number lines, folding). L1, L3, L4, L5, L6 and L8 improved by 12 to 21 points.

What is strictness, not regression: L9 and L10 fall (97% to 77%, 94% to 84%) because I flag Think harder items that are core level (L9 S2, S3, S7; L10 S4, S5, S7) and workbook items (L9 Q3, Q5). The original passed these and the tier rework did not touch them. L2 is flat for the same reason (S7, S8, Q2, Q4, slide item 2). The original treated "borderline" Start-here questions as compliant "when a way in exists (a grid, a figure, a table)"; I flag 18 of 60. If I apply the original's leniency to the Start-here page, my figure is about 311/329 = 94.5%. The claim "100% after" is therefore not supported on either reading: about 10 bank items and 5 slide items are outside their tier, and the printed Start-here pages are the weak point.

### 4.4 Diagnostic: were the earlier findings fixed?

| Finding in `journey_p4.md` | Status now | Evidence |
|---|---|---|
| Noisy cut scores: 8-item bands, 1 in 3 correctly placed children shown "support" or "step down"; warm-up of 4 items could send an 80%-skill child down 18% of the time | **Largely fixed** | Main-only rule, step-down only at 0 or 1 of 6. At 70% skill: join 74%, chat 24%, step down 1% (original 8-item table at 70%: 55% join, 39% support, 6% step down). The chat band is a tutor conversation, not a downgrade. The warm-up no longer sends anyone down alone |
| Discouraging wording ("Not yet?" box, "Not a failure", directive 0-3 row, Level 3 age band) | **Mostly fixed** | "Not yet?" gone, "Found it hard? That is useful to know...", "a confident start matters more than a fast one". Remaining: "it says nothing about how clever your child is" frames cleverness; the 0-or-1 row is still a directive; "Skills covered" heading kept |
| Younger-strong child a coin flip | **Fixed** | Now 93% told Level 4 (55% "chat, Level 4 with a little support") because warm-up cannot send a 2-3 main score down |
| Rusher / careless child ~60% sent to Level 3 | **Improved** | 26% Level 3 lean or down (13% + 13%), 74% sensible |
| Older-weak child: right on skill, no route, wrong age band | **Not fixed, now worse** | 19% told to join Level 4 (original: 70-75% sent to Level 3; now 55% lean or step down to Level 3); the line "older children are welcome" exists only in the unused JSON `placement` block |
| Weak child | **Slightly worse** | 73% pointed to Level 3 vs 87-92% before, because 4 of 6 is a lower bar than 6 of 8 and the warm-up cannot veto a join |
| "Try up" check tests untaught content; trigger too rare/odd | **Changed, over-flags** | Trigger is now main 4-6 plus any one brain stretcher right: 74% of strong children but also 16% of typical children are told to try the Level 5 check; the 4-question "from next year" version in the JSON is not on the page |
| Reorder warm-up, define "factor", key leniency (units, 22/5), wrong "6.12" error removed | **Fixed** | All verified in the built PDF and key |
| "Not taught yet" tick and the 2-or-more-ticks rule | **Half done** | Tick box printed ("not learnt yet"); the rule (`notTaughtRule`) is not on any page; the key says ticks "do not count against the child" but they are scored 0 and summed |
| Grey-zone chat, swap to end of lesson 2, "stop when your child is tired", "do not mark in front of your child", "A lower mark tells us where to start" | **Not on the page** | All exist only in `diag/content/p4.json` `placement`; `build_diag.py` never reads that block. The PDF says "change level free of charge before lesson 1" and "About 40 minutes" |
| Coverage gap (angles, symmetry, graphs absent) | **Handled honestly** | Skills list now says the check samples number, fractions, decimals, area and perimeter only |
| Three conflicting rules (doc 70% / 40-69% / under 40%; JSON 6-8 / 4-5 / 0-3 of 8; builder main 4-6 / 2-3 / 0-1) | **Not fixed** | `docs/levels_and_placement.md` still states the percent rule with "90%+ try up"; the JSON block states the 8-item rule; the PDF uses the main-only rule |

Verdict: before **mostly** (right for three of six profiles), now **mostly, better on noise and on the younger-strong and rusher profiles, worse for the weak and older-weak profiles, and with the documentation and the unused JSON block out of step with what is printed**.

### 4.5 Claims in the fix logs checked against the content

Confirmed in the content (spot-checked): neutral labels and no fast track anywhere (workbook, slides, guide, email pack); sneak-peek wording and notes; "Looking back" box with pass and still-stuck options; whole-group invitations and no private messages; Target Numbers without race or points; L3 quick questions 48 / 6, 9 x 6, 4 x 20 and Q6 124 plates; L2 Q1 cut to two numbers with "Try next"; L5 Q4 six numbers; L7 "rows" not "layers"; the printed digit, sign, bracket cards, graph grids, paper clock and pizza circles; page-2 caps; timeline 34-50 / 58-76 / 88-90 (L10 87-89); L9 "Sales have doubled!"; the Go further what-if on every explore slide.

Claimed fixed but not (or only partly) fixed:

1. Diagnostic `placement` block not wired into the build (items 1-8 of the fix pass were later replaced by a unified builder that ignores it). See 4.4.
2. Fix pass says "every 'strong thinkers / early finishers / genius / gifted' label is gone from workbook, slides and guide". True for those files, but `Math_Inquirers_P4_What_Learners_Get.pdf` still says "Readiness tracker: four signs of readiness for harder work" and "a short Challenge Screening Set and Challenge Group for children who show the signs", and the Question Bank intro says "Every child starts with Core, then moves up when they are ready". The fix log itself lists `levels/mkextras.py` as not edited.
3. The seven `challenge` slide notes that say "These are Think harder Q7 and Q6" (and similar) refer to the old numbering; the printed page calls them Go further Q5-Q7.
4. The Think harder slide in every lesson shows three items that are not the items on the printed Think harder page or in the bank (e.g. L1 slide "factors of 64, multiples of 3 and 7, 45 marbles" against printed "factors of 72, lighthouses, common factors, exactly 3 factors"). Answers are in the slide notes, but a tutor showing the slide and a child reading the page see different questions.
5. The close-gaps log says the reflection has a "next time" prompt; the later fix pass removed it. The log is stale; the content has no "what I would try next".
6. Parent packs still say "(finishing P4)"; diagnostics and docs moved to "covers P4 topics".

### 4.6 Improvements that are real, with evidence

- Core bank is now low-floor (60/60): e.g. L1 "12 sweets, use 12 counters", L4 "Cut paper circles into 4 slices", L8 "Fold a square piece of paper", L10 "Draw 8 animals with 2 legs first".
- The tier labels no longer sort children: "Start here / Think harder / Go further / Investigation", choice invited to the whole group; the fast-track box is gone.
- A first-minute win exists in every lesson (sneak-peek puzzle 1), and 9 of 10 Start-here Q1s start with a winnable part.
- Every lesson has an Investigation with an Easy first step, an expected-range key and a conjecture or find-all structure (L2 double rounding, L5 between two decimals, L8 row of four, L10 ring toss; keys re-checked by brute force).
- Reflection is safe and strategy-based ("what helped me" ticks, still stuck, pass, "Nobody marks this").
- Kit gaps closed (digit/sign/bracket cards, graph grids, paper clock, pizza circles, "bring from home" list).
- Answer keys are accurate in everything I recomputed (21 find-all or count claims).
- Diagnostic wording and ordering are friendlier and the younger-strong and rusher profiles are placed better.

### 4.7 Where the two audits differ in strictness (do not over-read the deltas)

- Rubric: my C7 (student-led talk), C12 (extension) and C10 (reflection) are more lenient than the original in places where the content did not change. If C7 stays at the original's 1 (the 12-minute tutor-led block is unchanged), if L3 C4 stays 1 and L10 C12 stays 1, the level mean is 18.5 instead of 19.6. C10 would drop to 1 for a reader who requires "what I would try next". C11 would rise to 2 for a reader who accepts self-choice as compacting. The original gave C9 0 for tutor-note-only prompts; I give 2 where the prompt is printed and an Investigation alters conditions, but 1 where the only prompt is one optional item.
- Tier compliance: the original called a Start-here question compliant when "a way in exists" even if the full solution needs the taught method; I call it a violation unless the printed scaffold lets an untaught child start and plausibly finish. I also flag Think harder items that a Core-level child could solve and Challenge items that are one step of a taught method. My item count is 329 against 324 because I counted every Start-here question by its printed number.
- Journey: I scored the 64-page current state; the original scored the 57-page state before the fix pass. I scored fun and motivation lower for drill-like lessons than the original did. Both audits are simulations; the per-item probabilities in the diagnostic part are assumptions in both, so the profile percentages show direction, not measurement.

---

## 5. Regressions and unfixed items

Regressions or trade-offs (none is a content error):

1. Reflection lost "what I would try next" (close-gaps added it; the fix pass dropped it for a three-prompt version). Safer for a low-confidence child, weaker as Polya look-back.
2. Diagnostic: older-weak child told to join Level 4 19% of the time and pointed to Level 3 55% (original 70-75%); weak child pointed to Level 3 73% vs 87-92%; try-up flag reaches 16% of typical children. All come from the main-only 4-of-6 rule, whose Q10 is a Primary 3 skill and whose warm-up cannot veto a join.
3. Duplicate reassurance text on the child sheet (Q11 prefix and the printed tip) and in the tutor key.
4. Journey cells that fell by 0.3 to 0.5: L6 LOW (-0.50: the workbook opens on a protractor and the protractor is bring-from-home), L3 HIGH (-0.50: Think harder Q2 and Q3 repeat Core), L4 LOW and MIDDLE (-0.33: thirteen sub-items, five comparisons), L10 HIGH (-0.33). I cannot show a content change that caused these; treat them as differences between two auditors until a tutor trial confirms.
5. Workbook grew from 47 to 64 pages; page 2 text is 178-277 words per lesson; this is acceptable but is more paper per child.

Unfixed (still true from the earlier audits): depth over speed and compacting; 18 of 60 Start-here questions not low-floor; HIGH waits about 29 whole-group minutes; page 2 is solo for 18 minutes; thousandths/rounding-back density in L5; no protractor supplied for L6; slide Think harder items differ from the printed page; parent flyers use the old Challenge Group language; docs/levels_and_placement.md disagrees with the builder.

---

## 6. Top remaining gaps and the smallest fixes

1. **Start-here pages not low-floor in L4, L7, L9 (and L1, L2, L3).** Move L4 Q5 and Q6, L7 Q4 and Q6, L9 Q3 and Q5, L1 Q5, L2 Q2 and Q4b to Think harder, and promote the bank Core items (which are already low-floor) into the printed Start-here page.
2. **Depth over speed (C2) and compacting (C11).** Cap Start-here at 4 questions per lesson, schedule the Investigation for the whole group in a fixed slot (talk time is the natural place), and let the sneak-peek route a child to skip the 53-58 teach block only by their own choice.
3. **LOW difficulty fit 2.2.** Give lessons 3, 4, 5 and 6 a physical or pictorial first item (L3 stickers story for every part of Q1, L4 bars already drawn for b-d, L5 tenths line before the zoom, L6 an estimate-only Q1 with the protractor item second) and put a partner on page 2 for the first 8 minutes.
4. **Diagnostic.** Wire the JSON `placement` block into `build_diag.py` or delete it; make one rule (main 4-6 join, 2-3 chat, warm-up 2 or less flags a join with 4 as "chat first"); print the 2-tick rule, "older children are welcome", the swap-through-lesson-2 line and the key note; raise try-up to main 5 or 6 plus a stretcher; update `docs/levels_and_placement.md`.
5. **Language still out of step.** Remove "Challenge Group for children who show the signs" and "moves up when they are ready" from `levels/mkextras.py` outputs; renumber the seven challenge-slide notes; replace the slide Think harder items with the printed ones or label them "extra"; "finishing P4" to "covers P4 topics".

Safe marketing language for this level now (research note section 3): "open-ended investigations with room to go further", "we emphasise explaining why, trying more than one method (L4, L7, L10) and learning from mistakes", "inspired by research-based approaches such as low-floor high-ceiling tasks and Polya's look-back" (the Looking-back box exists), "small groups with differentiated challenge" (the neutral choice ladder exists). Still not supportable: "not a drill programme" (C2 = 1 in every lesson), "gifted programme", acceleration, guaranteed outcomes.
