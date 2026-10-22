# Re-audit: Math Inquirers Level 1 (Primary 1, ages 6-8)

Independent re-score of the CURRENT material on the same two instruments as the earlier audits, then a like-for-like comparison. Desk review by a model: no child was observed, every score is judgement from text and rendered pages. Helper with all numbers: `docs/audit/reaudit_p1.py` (run `python3 docs/audit/reaudit_p1.py`). Nothing else was edited, built or committed.

What was read (current text, not the fix logs): `hp/lessons.js`, `hp/scripts.js`, `hp/qbank.json`, `hp/workbook.js`, `hp/workbook_html.js`; the rebuilt PDFs `hp/Math_Inquirers_P1_Student_Workbook_Designed.pdf` (58 pages, text extracted and 24 pages viewed), `P1_Question_Bank.pdf` (32), `P1_Tutor_Guide.pdf` (74), Weekly Dose, Weekly Email Pack, Readiness Tracker; all 10 decks `split/l1..l10` (about 25-29 slides each, slide text and speaker notes dumped); `outputs/diagnostics/Math_Inquirers_Level1_Placement_Check.pdf` and `..._Tutor_Key.pdf`, `diag/content/p1.json`, `diag/build_diag.py`. The Word workbook was checked for stale labels only. Every numeric answer in the bank, workbook and decks that I touched was re-computed in Python (about 120 checks: magic triangles, coin ways, pattern positions, grids, queues, riddles). All keys are correct; I found no arithmetic error.

Process: Phase 1 scores (sections 1A, 1B) were fixed and saved (`reaudit_p1.py`, parts 1) BEFORE any earlier audit file was opened. Phase 2 (section 2) was done afterwards. I did not change a Phase 1 score after seeing the baselines (one counting error in the tier tally, double-counting workbook items that are also bank items, was corrected mechanically; the item judgements are unchanged).

---

## 1A. BLIND: instrument A (gifted-style rubric), current material

Evidence common to all lessons (the printed workbook is now a four-part page set: Start here / Think harder / Go further / "Choose, then look back" with an Investigation and a Look-back; every deck has a 7-10 min Sneak-peek and a Go-further what-if on `lN-explore1`):

| # | Criterion | Evidence (one line) | L1 | L2 | L3 | L4 | L5 | L6 | L7 | L8 | L9 | L10 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Low floor, high ceiling | Sneak-peek Q1 "anyone can try" (`lN-warmcheck`); explore what-if; Investigation "Easy first step" then "Then:"; guide gives model answer and "Look for" | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 2 | Depth over speed | 10 min explore, "you do not have to finish", but 28-slide timed decks with 6-10 teach/try slides and 5-9 Core items; L1, L4, L6 have 4-5 Core items | 2 | 1 | 1 | 2 | 1 | 2 | 1 | 1 | 1 | 1 |
| 3 | Generalise | "Is it always true?" investigations (L2, L4, L5, L9), "what stays the same" (L1, L10), T/C items; L3, L7, L8 mostly stay at cases | 2 | 2 | 1 | 2 | 2 | 2 | 1 | 1 | 2 | 2 |
| 4 | Justify | "Mei/Ben says ..." claims to test (L2 Q4e, L3 Q6, L4/L5/L9 investigations, L6 Q4); L7 and L10 Core are answer-only | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 1 |
| 5 | Multiple paths | Only L6 contrasts methods (biggest-coin table vs swap 5c for 10c, `l6-teachswap`); elsewhere the tutor shows one method and asks "Is there another way?" (`lN-chwalk`) | 1 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 |
| 6 | Challenge ladder | Neutral "After question 3 you may choose: carry on, or try Think harder. You can swap at any time"; three printed tiers plus Investigation, nobody named | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 7 | Student-led inquiry | Pairs explore 10 min, sentence starters, volunteers first, pass allowed; but 25-35 and 55-58 are tutor-led and L5, L7, L9 have 9-10 teach slides | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 2 | 1 | 2 |
| 8 | Complexity / context | L3 sampling and other factors (Q6, Q7), L6 coin-count constraints, L8 interacting clues, L9 unit choice, L10 C1 combines patterns; others are thin contexts | 1 | 1 | 2 | 1 | 1 | 2 | 1 | 2 | 2 | 2 |
| 9 | Problem posing | Go-further what-if on every explore slide; "Make up your own" as C3 in 9 lessons (L2: "Change the magic triangle") | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 10 | Metacognition | Printed Look-back every lesson (did well / hardest part, lesson-specific ticks / what helped / still stuck / pass). No "what I would try next"; not used in-session | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 11 | Pacing / compacting | Sneak-peek and choice after Q3, but a lockstep timed deck and "Everyone joins Explore and the Mini-lesson"; nothing can be skipped | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 12 | Extension, not acceleration | Grade-level content explored by pattern/logic/combinatorics; L3 key-of-2/3, L5 IN/OUT machines, L9 cm ruler and unit conversion lean on next-year ideas | 2 | 2 | 1 | 2 | 1 | 2 | 2 | 2 | 1 | 2 |
| | **Total /24** | | **21** | **20** | **19** | **21** | **18** | **23** | **17** | **20** | **19** | **20** |

Level mean 19.8/24. Bands (research note): 20-24 depth-oriented: L1, L2, L4, L6, L8, L10. 12-19 enrichment-flavoured with gaps: L3, L5, L7, L9. Sensitivity (see 2.7): strict reading of criterion 10 (needs "what I would try next") gives 18.8; strict 10 plus calibration to the old auditor's strictness gives 17.5.

Lesson-specific notes behind the cells that differ: L6 is the only lesson with contrasting methods and a real constraint puzzle (T1 "exactly 4 coins for 70c, every set", C3 "puzzle with exactly ONE answer"). L7 is the lowest: 10 teach slides, no conjecture-and-test prompt, and C1/C2 are text-only with no figure (see 2.5 item 6). L9 has 340 words on its Core pages and needs five physical objects. L3 is the best-fitting context (vote, then "would Primary 6 choose the same?") but its generalising is weak and its scale-key ideas are P2-ish.

### Tier compliance, current material (Core approachable untaught; Think Harder = taught idea in a new setting; Challenge = mastery plus extension)

Unique items counted: printed Core pages (60) + question bank (74 Core, 102 Think Harder, 58 Challenge) + 1 workbook-only item = 295. The printed Think Harder (T1-T4/5) and Go further (C1-C3) pages are bank items, so they are not counted twice. "Partial" = I could defend either label; counted as a violation in the strict figure.

| Where | Item | Problem |
|---|---|---|
| Core wb | L2 Q5 magic triangle (sum 9) | needs the corner insight; about 720 arrangements by trial; hint only says "small numbers in the corners" |
| Core wb | L5 Q1c, Q2b | two-step undo in Core; rule-finding plus inverse for "OUT 30" is the taught method itself |
| Core wb | L6 Q3a | fewest coins for 85c needs the "biggest coin first" strategy taught the same lesson |
| Core wb | L9 Q3, Q4 | Q3 is the lesson insight (smaller unit, bigger count); Q4 is two-way unit conversion, text only (slide says "draw the bars", page gives none) |
| Core wb | L10 Q7 | two-step backwards in the Core of a review lesson |
| Think Harder | L1 T1, L2 T1, L2 T3, L9 T1, L6 T5 | duplicate a Core item with new numbers, or (T5 dollars) rely on an optional teach slide |
| Challenge | L2 C1 (magic triangle 11), L9 C2 | same task/technique as Core with a new number; one idea only |
| Bank Core | L6 #7, #8 | dollar-note "fewest notes" in Core while the workbook moved dollars to Think Harder |
| Bank Think Harder | L1 #8-9, L2 #1-3 and #8-12, L3 #8, L5 #8-10, L6 #8, L9 #10 (repeats #3b), L10 #9 | routine variants or one-step items; L2's "Think Harder" list has 8 near-Core fill-ins |
| Bank Challenge | L3 #1 (one add then compare), L9 #2 (repeated addition), L2 #5 (= wb Core Q5, new total) | too thin for Challenge |

Result: 262/295 = 89% strict (33 partial); 94% if each partial counts half. By lesson (strict): L1 90, L2 71, L3 94, L4 100, L5 83, L6 83, L7 100, L8 100, L9 79, L10 93. Items I judged clean and well laddered include L1 Q3 (colour frog landings), L3 Q1-Q5 (read a picture graph), L4 Q1/Q3 (draw, build with sticks), L7 T2/T3, L8 Q3 (grid with two crosses supplied), L10 C1 (triangle AND square sticks, 7, 13, 19, 25, 31).

---

## 1B. BLIND: instrument B (student journey), current material

Scores are P (participate), D (difficulty fit, 3 = just right), F (fun), C (confidence), M (motivation), S (social/online). Page numbers are workbook PDF pages; `lN-...` are slides.

| L | Persona | P D F C M S (mean) | Evidence and flagged moments |
|---|---|---|---|
| 1 | LOW | 5 3 4 4 3 3 (3.67) | `l1-warm1` stomp has no wrong answer; sneak Q1 "hop a counter" and p3 Q1 skip-count blanks are guaranteed wins. Load: p3 Q2 must WRITE a rule; p4 Q4 (two lists) and Q5 (10-box table) fill the solo 58-68 slot. `l1-try1` says whiteboards "up together": a wrong board is public. |
| 1 | MIDDLE | 5 4 4 4 4 4 (4.17) | Frog story and prediction (`l1-explore1`), try slides well paced, Q4-Q5 fit the solo page. |
| 1 | HIGH | 5 3 4 4 4 4 (4.00) | Q1-Q5 and `l1-teach1/we1/we2/try1/try2` (25-33) re-teach what sneak Q2 showed. Relief: explore1 "Go further" from minute 10, Investigation p5, C1-C3 p7. |
| 2 | LOW | 5 2 4 3 3 3 (3.33) | Sneak Q1 (10 sweets) and p8 Q1 are wins. p9 packs Q4 (five "=" parts), Q5 magic triangle (Core, trial and error), Q6 into 58-68. |
| 2 | MIDDLE | 5 4 4 4 4 4 (4.17) | Ordered bond list shows a pattern (Q2b); see-saw "=" is memorable. |
| 2 | HIGH | 5 3 4 4 4 4 (4.00) | Q1-Q3 are recall; Q4 and Investigation p10 ("Mei says both odd or both even") and C3 are real but arrive after minute 58 unless chosen. |
| 3 | LOW | 5 4 4 4 4 3 (4.00) | Thumbs vote (no typing), p13 Q1-Q4 immediate wins, Q6/Q7 accept any reason. Part B needs a group to vote. |
| 3 | MIDDLE | 5 4 4 4 4 4 (4.17) | Real purpose (plan the party), own data. |
| 3 | HIGH | 5 3 3 4 3 4 (3.67) | Graph reading is trivial; thinking starts at `l3-try3`, T1-T4 (key of 2), C3 "banana wins by exactly 2, find a second graph" p17. Weakest HIGH cell. |
| 4 | LOW | 5 3 4 3 3 3 (3.50) | Clap-snap-stomp, p18 Q1 draw shapes = win. Q2c 30th place ("keep drawing"), Q3c explain the shared side, 21 straws needed. |
| 4 | MIDDLE | 5 4 5 4 4 4 (4.33) | Predict then build with straws. |
| 4 | HIGH | 5 4 5 4 4 4 (4.33) | explore1 "10 triangles", Investigation p20 ("place 30 = place 3?"), C1-C3 (47 beads, 1,3,6,10, make-up 33rd bead). |
| 5 | LOW | 4 2 4 2 3 3 (3.00) | Cup game good. p23 Q1c (two-step) and Q2b are Core; p24 Q3 four parts, Q4b "3rd from front AND back" is a counting trap; three new ideas at 54-58 (`l5-teachbar`, `l5-teachq1/q2`) minutes before the solo page. |
| 5 | MIDDLE | 5 3 4 3 4 4 (3.83) | IN/OUT vocabulary arrives via three slides; queue traps. |
| 5 | HIGH | 5 4 4 4 4 4 (4.17) | Two- and three-step undo T1-T4, snail C2, 3-step make-up C3, Investigation "is OUT always IN?". |
| 6 | LOW | 4 3 4 3 4 3 (3.50) | `l6-warm1` cents only; sneak Q1 "draw them, can Ben pay 25c"; p28 Q2 "there are 4 ways" is the worked example = win. Q3 85c fewest and Q4 "explain" on the solo page; 25 coins to cut out (pp53-54). |
| 6 | MIDDLE | 5 4 5 4 4 4 (4.33) | Money shop, find-all with a table, 4-row limit stated. |
| 6 | HIGH | 5 4 5 4 5 4 (4.50) | T1 every 4-coin set for 70c, C1 subset amounts, C3 "exactly ONE answer", Investigation p30. |
| 7 | LOW | 4 3 4 3 3 3 (3.33) | Shape hunt, fold-and-cut, p33 Q1 count = win, Q2 table prefilled. 10 teach slides (`l7-teachpic/sides/who/tri` at 40-58); Q3c "hexagon", Q5 name a composed shape; scissors on camera. |
| 7 | MIDDLE | 5 3 4 4 4 4 (4.00) | Sides = corners discovery (Q2). |
| 7 | HIGH | 5 4 5 4 4 4 (4.33) | Hidden squares/triangles T2/T3, Investigation p35 (find all shapes from 3 and 4 squares); C1 p37 is text-only with an unlabelled pattern 3, 6, 10. |
| 8 | LOW | 5 2 3 3 3 3 (3.17) | Sneak Q1 and p38 Q1a are wins. Then four reading-heavy puzzle types: Q1c (four ribbons, three clues), Q2 two-loop with "less than 6", "odd" plus definitions, Q3 grid (two crosses supplied: good), Q4. About 280 words on the Core pages. |
| 8 | MIDDLE | 5 3 4 4 4 4 (4.00) | Clues feel like detective work. |
| 8 | HIGH | 5 4 5 4 5 4 (4.50) | Riddles, "second reason" odd-one-out (Q6), C1-C3, make-up "ONE answer" pet puzzle, Investigation "all orders". |
| 9 | LOW | 4 2 3 3 3 3 (3.00) | Needs cm ruler, cube strip, paper clips, erasers. p43 Q1 wins; p44 Q3 spans (the lesson's insight, wordy), Q4 text-only, Q6 ruler offset. About 340 words on Core pages (highest). |
| 9 | MIDDLE | 5 3 4 4 4 4 (4.00) | Hands-on estimate then measure. |
| 9 | HIGH | 5 4 4 4 4 4 (4.17) | Investigation p45 ("Ben: shorter unit always bigger number"), T3-T4, C1 train-with-gaps, C3 two-unit puzzle. |
| 10 | LOW | 4 2 3 3 3 3 (3.00) | One of four puzzle cards for 10 min (patterns card is gentle) but the Start-here pp48-49 has 9 items (Q4 two parts, Q7 two-step); swap to a new pair at minute 21 online. Whiteboard round "nobody on the spot" is safe. |
| 10 | MIDDLE | 5 3 4 4 4 4 (4.00) | Review through puzzles. |
| 10 | HIGH | 5 4 5 4 5 4 (4.50) | Puzzle cards, C1 cross-topic, C3 "change ONE thing", Investigation "shortcut for the total". |

Level-wide, current: Lia-type guaranteed win in the first 10 min of the worksheet in 10 of 10 lessons (Q1 of every Start-here page; L6 Q1/Q2 and L5 Q1a-b now qualify). Reading load on Core pages is about 150-340 words (L9 340, L8 280, L5 234, L1 210; my counting includes table headings, so it is a bound, not comparable digit-for-digit with the old count). Still unchanged: one 5-min break (35-40) and one 1-min stretch (68) in a 90-min online session; Mini-lesson and 55-58 teach bursts are tutor-led for everybody.

### Diagnostic, blind view
Questions (current): W1 count on from 14, W2 17 vs 12, W3 count in 2s, W4 3-sided shape (K2, fair; not used in placement because Level 1 has no level below). Main: M5 bond 7+?=10, M6 5,10,15,?, M7 40c+30c (tens addition with "cents": fair for P1 term 2+, harder for a K2 child), M8 dot graph 5/3/2 difference (picture now, 17 words gone), M9 12-8 cubes, M10 transitive order (1-in-3 guessable). Stretch: S11 ruler from 2 to 7 (the L9 stumbling block), S12 5 coins 10c/5c = 40c (unique: 3 and 2, verified). Placement rule printed by `build_diag.py`: main 4-6 join (plus "try Level 2 check" if one or more stretch right), 2-3 "chat and free taster, Level 1 with a little support", 0-1 "chat and free taster"; warm-up and "not learnt yet" ticks are not used. Results are in 2.4.

---

## 2. COMPARE with the earlier audits

Baselines opened only now: `gifted_p1.md` (original per-lesson scores, "after" column), `gifted_fixes_p1.md`, `journey_p1.md`, `fixpass_p1.md`, `close_gaps_p1.md`, `fixes_p1.md`. Note which snapshot each baseline describes: the rubric "before" is the content before the tier rework; the rubric "claimed after" (15.8) covers ONLY the first rework, written before the sneak-peek, look-back, Investigation, what-if cards and neutral labels existed. The journey baseline describes the content after the tier rework and close-gaps but before the student-journey fix pass. So "now above claimed after" is expected, not over-delivery.

### 2.1 Rubric per lesson: before / earlier-claimed-after / re-audit now, with per-criterion deltas (now minus before)

Criterion order: 1 LTHC, 2 Depth, 3 Generalise, 4 Justify, 5 Multi-path, 6 Ladder, 7 Inquiry, 8 Complexity, 9 Posing, 10 Metacog, 11 Pacing, 12 Extension.

| L | Before | Claimed after | Now | Delta | Per-criterion delta (1..12) |
|---|---|---|---|---|---|
| 1 Number patterns | 15 | 17 | 21 | +6 | 0 +1 0 +1 0 +1 +1 0 +1 +1 0 0 |
| 2 Number bonds | 15 | 17 | 20 | +5 | 0 0 0 0 0 +1 +1 0 +2 +1 0 0 |
| 3 Picture graphs | 13 | 16 | 19 | +6 | +1 0 0 0 0 +1 +1 0 +1 +2 0 0 |
| 4 Patterns | 12 | 15 | 21 | +9 | +1 +1 0 +1 0 +1 +1 0 +2 +2 0 0 |
| 5 Working backwards | 12 | 15 | 18 | +6 | +1 0 +1 +1 0 +1 0 0 +1 +1 0 0 |
| 6 Money | 13 | 15 | 23 | +10 | 0 +1 +1 0 +1 +1 +1 +1 +2 +2 0 0 |
| 7 2D shapes | 15 | 17 | 17 | +2 | 0 0 -1 0 0 +1 0 0 +1 +1 0 0 |
| 8 Logic | 13 | 16 | 20 | +7 | +1 0 0 0 0 +1 +1 +1 +1 +2 0 0 |
| 9 Length | 11 | 14 | 19 | +8 | +1 0 +1 0 0 +1 0 +1 +2 +2 0 0 |
| 10 Mixed puzzles | 14 | 16 | 20 | +6 | +1 0 +1 0 0 +1 0 +1 0 +1 0 +1 |
| **Mean** | **13.3** | **15.8** | **19.8** | **+6.5** | |

Criterion means before to now: 1 LTHC 1.4 to 2.0; 2 Depth 1.0 to 1.3; 3 Generalise 1.4 to 1.7; 4 Justify 1.5 to 1.8; 5 Multi-path 1.0 to 1.1; 6 Ladder 1.0 to 2.0; 7 Inquiry 1.1 to 1.7; 8 Complexity 1.1 to 1.5; 9 Posing 0.7 to 2.0; 10 Metacognition 0.5 to 2.0; 11 Pacing 1.0 to 1.0; 12 Extension 1.6 to 1.7.

Which gains are real (new material I could find in the content) and which are calibration:
- Real: criterion 6 (neutral ladder is now printed and visible: "Start here / Think harder / Go further / Investigation"), 9 (what-if card on every `lN-explore1`, a "make up your own" C3 in 9 lessons, verified in the PDF), 10 (printed Look-back in every lesson, was oral only), 1 (Investigation with an easy first step on page 3 of every lesson, sneak-peek access question), plus part of 4 and 3 (the "Mei says ... is it always true?" investigations in L2, L4, L5, L9).
- Likely calibration, not content (about 13 points over the level, 1.3 per lesson): 7 (the old auditor's evidence, tutor-led 25-35 and 55-58, is still true; I scored 2 in 8 lessons), 8 (contexts unchanged; I gave 2 in L6, L8, L9, L10), 2 (item counts per page unchanged; I gave 2 in L1, L4, L6 for the "you do not have to finish" framing).
- Unchanged and correctly so: 5 (multiple paths still taught as one method except L6), 11 (compacting: a sneak-peek now exists, but nothing can be skipped), 12.
- Calibrated to the old strictness the level mean is about 18.5; with the strict reading of criterion 10 (no "what I would try next") about 17.5. So the honest range for "now" is 17.5-19.8, against 13.3 before and 15.8 claimed. Real gain about +4 to +6.5; the later passes delivered more than the first rework claimed.

### 2.2 Heatmap, mean of six scores (before = `journey_p1.md`, now = this re-audit)

| Lesson | LOW before | LOW now | MIDDLE before | MIDDLE now | HIGH before | HIGH now |
|---|---|---|---|---|---|---|
| 1 Frog | 2.83 | 3.67 | 3.83 | 4.17 | 3.33 | 4.00 |
| 2 Bonds | 3.00 | 3.33 | 3.67 | 4.17 | 3.33 | 4.00 |
| 3 Fruit party | 4.17 | 4.00 | 4.33 | 4.17 | 3.67 | 3.67 |
| 4 Patterns | 3.50 | 3.50 | 4.17 | 4.33 | 3.17 | 4.33 |
| 5 Mystery number | 2.83 | 3.00 | 3.83 | 3.83 | 3.83 | 4.17 |
| 6 Coin combos | 1.83 | 3.50 | 2.83 | 4.33 | 4.17 | 4.50 |
| 7 Shapes | 3.33 | 3.33 | 4.17 | 4.00 | 4.00 | 4.33 |
| 8 Logic | 2.67 | 3.17 | 3.67 | 4.00 | 4.17 | 4.50 |
| 9 Length | 3.17 | 3.00 | 3.83 | 4.00 | 3.83 | 4.17 |
| 10 Challenge day | 2.83 | 3.00 | 3.67 | 4.00 | 4.33 | 4.50 |
| **Level mean** | **3.02** | **3.35** | **3.80** | **4.10** | **3.78** | **4.22** |

Dimensions (P, D, F, C, M, S) level means, before to now. LOW: 3.9/2.2/3.4/2.6/3.1/2.9 to 4.5/2.6/3.7/3.1/3.2/3.0. MIDDLE: 4.7/3.1/4.1/3.3/3.8/3.8 to 5.0/3.5/4.2/3.9/4.0/4.0. HIGH: 5.0/2.6/4.2/3.8/3.7/3.4 to 5.0/3.7/4.4/4.0/4.2/4.0. Cells below 3.0: six before, none now (L6 LOW 1.83 and L8 LOW 2.67 were the old floor). Cells below 3.5 now: six, all LOW (L5, L9, L10 at 3.00; L8 3.17; L2, L7 3.33). Differences of 0.3 or less are inside the noise of this kind of review (L3 LOW and MIDDLE, L7 MIDDLE and L9 LOW fell by 0.17: I treat them as noise, not regressions).

Biggest real moves: L6 (LOW +1.67, MIDDLE +1.50: cents-only warm-up, Q2 = 25c with "there are 4 ways", dollars moved to Think Harder T5, spare-row note, page break), L4 HIGH (+1.17: what-if card at minute 10, Investigation), L1 LOW (+0.83: printed 0-50 strip, Q4 shortened to 30, sneak Q1 as access), HIGH difficulty-fit (2.6 to 3.7: something to chew from minute 10 and from Q3), MIDDLE/HIGH confidence (+0.6 / +0.2: sneak-peek framing, no public tally, look-back with pass).

### 2.3 Tier compliance

| | Items | Compliant |
|---|---|---|
| Before (gifted_p1.md) | 309 | 227 = 73% (L7 55%, L9 57% worst) |
| Claimed after (gifted_fixes_p1.md) | | 100% "by construction, the designer's reading, not an independent check" |
| Now (this re-audit, unique items) | 295 | 262 = 89% strict; 94% if partial counts half |

Not 100%. 33 partial items, concentrated in L2 (10: eight near-Core "Think Harder" fill-ins in the bank), L9 (6), L5 (5), L6 (5), L1 (3). The Core items that still need the lesson idea are listed in 1A. The earlier log itself flagged "Core scaffolds invite the concrete route; they do not guarantee" and "L5 Q4b is the worked example"; both still hold. The clear improvement is real: Challenge is no longer a repeat of the worksheet method (every lesson has a multi-step item, a find-all/combine item and an open make-up item, all verified), and Core now carries objects/drawing/strip scaffolds on the printed pages (L2 Q4 "use counters", L5 Q3 bars, L8 Q3 crossed grid, L9 Q6 ruler picture, L6 Q1 table).

### 2.4 Diagnostic: were the earlier findings fixed? Six profiles on the CURRENT rule

Method: Poisson-binomial over the 6 main questions (stretch separate), using (a) the old audit's own per-question assumptions, so results are like-for-like, and (b) my own blind assumptions. My simulator reproduces the old audit's numbers for the OLD 8-mark rule (typical 15/62/23 join/support/taster vs the old 15/61/23), which validates the code.

| Profile | E[main] (old / mine) | Old rule (old audit) join / support / taster | CURRENT rule, old assumptions: join (of which "try L2" flag) / chat "support" / chat "taster" | CURRENT rule, my assumptions | Right level, verdict |
|---|---|---|---|---|---|
| Strong for age | 5.4 / 5.6 | 71% (+9% try P2) / 20% / 0 | 99% (67% flagged) / 1% / 0 | 100% (85% flagged) | P1 + Go-further; yes |
| Typical for age | 4.2 / 5.0 | 15 / 61 / 23 | 74% (13% flagged) / 26% / 1% | 93% (38%) / 7% / 0 | P1 plain join; yes |
| Weak for age | 1.8 / 2.6 | 0 / 6 / 94 | 5% / 54% / 41% | 20% / 61% / 19% | P1 with support or readiness first; yes |
| Younger, strong (6) | 4.2 / 4.0 | 16 / 63 / 20 | 75% (20%) / 25% / 1% | 67% (19%) / 31% / 1% | P1; mostly yes, remaining 25-31% hear "chat" mainly because of cents/ruler |
| Older, weak (8) | 3.3 / 5.1 | 3 / 41 / 55 | 42% (4%) / 51% / 7% | 95% (27%) / 5% / 0 | P1 (lowest level); now not over-cautious under my model, still 51% "chat" under the old model |
| Guesser / rusher | 2.8 / 3.2 | 1 / 24 / 72 | 26% (2%) / 61% / 14% | 39% (6%) / 52% / 9% | P1 plain join; paper cannot show rushing; "chat" is the right route but the rushing prompt is missing (below) |

Luck and noise: a child who gets each main question right with p = 0.9 / 0.8 / 0.7 / 0.6 / 0.5 sees "join" (4-6 marks) 98 / 90 / 74 / 54 / 34% of the time and a "chat" outcome (0-3 marks) 2 / 10 / 26 / 46 / 66%. Pure guessing reaches 4 of 6 about 0.2% of the time (M10 is the only guessable item). Lucky placement is not a risk; a single slip (4 to 3) is, and the advice for 2-3 ("chat and taster") is soft, which makes the noise cheap.

Earlier findings, status:

| Earlier finding | Status |
|---|---|
| Cut scores noisy: 84% of typical children told "expect support" or taster | FIXED. Judged on the 6 main questions only, 4-6 join. Typical join 74-93% (was 15%). Residual: a single slip crosses a band; the band label is soft so cost is low. |
| Discouraging wording ("failure", "one level down" for a level that does not exist, "expect some support", "well challenged", fragments) | MOSTLY FIXED. All gone from the printed result page; "Found it hard? ... says nothing about how clever your child is" and "a confident start matters more than a fast one" are good. Residual: key says ticked "not learnt yet" "score 0 but do not count against the child" (they count in the marks); Level-1 "0-1" row still has no concrete place to go (no Level 0; "chat and free taster"). |
| Younger-strong children mis-placed (cents, ruler) | PARTLY. Join rose 17% to 55-67% (+ flagged). "Not learnt yet" ticks are collected but not used, so a K2 child who has not met money still falls to "support" when marks are 2-3. |
| Rushing cannot be seen on paper | NOT FIXED. The sentence "If your child answers very quickly, ask them to check one answer by drawing it" exists only in `diag/content/p1.json`; `diag/build_diag.py` never reads `tutorKey`, `childNote`, `scoring` or `parent`, so it is not in the printed key. |
| Child intro: "Read a question aloud if they ask" (a 6-year-old does not ask) | NOT FIXED. Printed text unchanged; the corrected `childNote` is dead JSON. |
| Key header "(for example 2.05 and $2.05)" copied from upper levels | NOT FIXED (still printed on the Tutor Key). |
| Cross-check "In lessons your child will meet money to $50, reading a ruler and logic puzzles" | NOT FIXED (dead JSON; the printed result page lists "Skills covered" only). A 6/6 still does not warn about L5, L6, L8 difficulty. |
| Brain stretchers should only flag the Level 2 check when the child also did well on main | PARTLY. Printed row for 4-6 says "If the stretchers also went well (1 or more) you could try the Level 2 check", so a 4/6 child with one stretch right is invited to try Level 2 (the JSON says 5 or 6 of main). 13% of typical children would see this. |
| Q4 graph wordy, W3 duplicate of M1, S1 not demanding, no stretch warning, separate key | FIXED (dot graph picture; W3 now "count in 2s"; S1 now the ruler 2 to 7; "Optional... meant to be tricky" line; key in a separate PDF). |
| Placement rule documented in `docs/levels_and_placement.md` | Stale: still says 70%+ / 40-69% / under 40%, which would put 4/6 (67%) in the "support" row, contradicting the printed rule. |

Verdict on the diagnostic: before = mostly (separated strong from weak but sent ~84% of typical 7-year-olds to "support" or a taster); now = mostly yes (about three quarters to nine tenths of typical children get an unqualified join, weak children are routed to a chat and taster, wording is kind). Remaining weaknesses are rushing, the unused "not learnt yet" signal, dead JSON, and that the main six still do not test L1, L5, L6, L8 demands.

### 2.5 REGRESSIONS and items claimed fixed that are not (or not fully)

No content regression with clear evidence. Items where the log and the content disagree, or something got worse in effect:

1. Public whiteboards contradict the private-paper rule. `fixpass_p1.md` claims "never boards" for the Sneak-peek; but every lesson has a "Your turn: whiteboards" mini-lesson slide (7 titled exactly that; 31 "Your turn" slides in all) and six speaker notes say whiteboards go "up together" (`l1-try1`, `l2-try1`, `l3-try1`, `l5-try1`, `l7-try1`, `l9-try1`). A LOW child's wrong board is visible to seven others. The old audit's "most exposed moment" is only moved, not removed. NOT FIXED for the mini-lesson.
2. Neutral labels not complete outside the child pages. `fixpass_p1.md` says "Challenge" and "early finishers" were removed from the question-bank text. The Question Bank PDF still prints ten "CHALLENGE (after the topic...)" headings while its intro calls the tier "GO FURTHER"; the Tutor Guide says "If a child finishes early, use the Challenge or Extension question" and prints "Challenge: 4 and 8" in the L2 key; the Weekly Email Pack tells parents to "try the Challenge questions" and offers "a short challenge session"; the Readiness Tracker still says "Spot children ready for olympiad-style work", "Solved a Challenge question" and "invite to the Challenge Group". This keeps a grouped, ranked "challenge group" alongside the neutral child-facing choice.
3. `close_gaps_p1.md` described a reflection with "next time I will try" plus three tick faces. The current Look-back has neither (it was replaced by the journey fix pass; `hp/gap_face_*.png` are unused). No log notes the removal. Result: criterion 10 lacks "what I would try next".
4. Question Bank / workbook tier language mismatch remains (item 2 above) and the Core dollar items in the bank (`L6 #7, #8`) disagree with the workbook, which moved dollars to Think Harder T5.
5. Tier compliance "100% by construction" is not borne out: 89% strict (section 2.3).
6. L7 Challenge pages lost their pictures: `gifted_fixes_p1.md` admits the `lN-chdiag` slides were dropped. On the printed page (p37) C1 reads "A triangle has 4 lines drawn from the top corner to the bottom... Follow the pattern 3, 6, 10 ... What would 5 lines give?" with no figure; the pattern 3, 6, 10 belongs to 1, 2, 3 lines but the page does not say so, and C2 (squares in a nested figure) is also text-only. Suggested text for C1: "A big triangle has lines drawn from its top corner to the bottom. With 1 line there are 3 triangles, with 2 lines 6, with 3 lines 10. How many with 4 lines? With 5 lines? Draw it to check."
7. Slide and page disagree in L9: `l9-ws2` Q3 says "Measure one line with paper clips, then with cubes" (an experiment with materials) while the workbook Q3 is a word problem with a hint; Q4 on the slide says "Draw the bars" but the page gives no bars or drawing space.
8. Diagnostic dead JSON (see 2.4): the fix pass listed eight `build_diag.py` changes as "needed"; four were later built (visuals, separate key, scoring rows, softer wording), four were not (childNote, tutorKey.accept/rushing/prereq, parent.join cross-check, stretch rule).
9. Unchanged structural items from the old audit: one break in 90 online minutes for ages 6-8, everyone sits through every teach slide (HIGH waits), at-home materials list (straws, cups, scissors, string and buttons, cm ruler, clips, erasers), tutor guide still says both "Never write scores down" and "Quietly note who found question 2 easy".
10. The workbook grew from 48 to 58 pages; the Investigation and Look-back page carries 130-165 words after minute 88 for a 6-year-old (the Look-back box itself about 50 words in a 2-minute slot).

### 2.6 Improvements that are real, with evidence

- Sneak-peek framing (`lN-warmcheck`, 7-10): "ideas we have not learnt yet, a guess is a great start, nobody is marked", Q1 "Anyone can try this one: use counters, draw or count", paper shown only to the tutor, no private chat. Fixes the old hidden pre-test (verified in all 10 decks).
- Neutral choice: the 45-word "Fast track" box and "Challenge (for strong thinkers)" header are gone from workbook (PDF and Word), decks and guide; replaced by "After question 3 you may choose" and "Think harder / Go further". The tutor invites the whole group.
- Investigation page with "Easy first step" (all 10; models checked: L2 parity of bonds, L3 key 2 works and key 3 does not, L4 place 30 = place 3, L5 add 6 take 6 = identity, L6 5/15/25/35/45 impossible without the 5c coin, L7 two shapes from 3 squares and five from 4, L8 six orders and four with a clue, L9 shorter unit bigger number, L10 totals are 3 times the middle).
- Look-back (every lesson) with "I was not stuck", "I am still stuck (my tutor will come and help)" and "I would like to pass"; volunteers-only talk time; check-in via breakout room or hand signal, no direct messages.
- Lesson fixes verified in the PDF: L6 cents-only warm-up, Q2 25c with the 4-way hint, "You may not need every row", 30c and dollars moved to Think Harder; L8 crossed grid and "If you have time" on Q5/Q6; L1 printed 0-50 strip and Q4/Q5 to 30; L5 Q3 split with bar table, "Draw the children as circles first"; L7 and L6 exit tickets made easier (hexagon; 30c any way); L9 ruler question with a picture and "how far off my guess was"; L10 card choice and whiteboard round with nobody on the spot.
- Tutor guide: "Tutor reads Q1-Q2 aloud, then pairs read the rest" (old audit's reading-load fix).
- Diagnostic: rule on the 6 main questions, kind result wording, pictures for the graph and ruler, separate tutor key, "not learnt yet" tick.

### 2.7 Where the two audits differ in strictness (do not over-read the deltas)

- Different model instances with no memory of each other; no inter-rater test was run. Treat plus or minus 1 per criterion and plus or minus 0.3 per heatmap cell as noise. Both are desk reviews; no child was observed.
- Rubric: the old auditor gave 0 or 1 when a feature existed only orally or in tutor notes and gave 2 sparingly (criteria 1, 3, 12 mainly). I credit a feature as 2 when it is printed and enacted for children even if optional and unreviewed (look-back, investigation, make-up). I also scored criteria 2, 7, 8 more generously than the old text supports (about 13 points, see 2.1). I scored 11 (compacting) as strictly as the old auditor, and 10 as 2 although "what I would try next" is missing (sensitivity 18.8). Net: raw 19.8, calibrated 17.5-18.5.
- Tier test: the old audit used a binary ok/VIOLATION on worksheet Core items plus bank items (309 items, 73%). I used ok/partial with strict (partial = violation) and half-credit views, counted unique items (295), and added the "same task as Core" and "routine repeat" categories, so my method is slightly stricter on Think Harder and Challenge than the old pass; the old 100% "after" was a design claim, not a test.
- Journey: the old review named personas (Lia, Max, Zoe) and scored the pre-fix lessons with the public Sneak-peek and Fast-track box in view; my social scores are compressed (3-4) because the fix pass applied the same protocol to every lesson, so I discriminate less on S and more on D. The old reading-load counts (120-290 words) and mine (150-340) use different rules and are not comparable digit for digit; the ranking (L8 and L9 heaviest, L4 lightest) agrees.
- Diagnostic: probabilities are assumptions; two sets are shown. The old audit's assumptions give the more cautious picture for the older-weak child and the rusher.

### 2.8 Remaining gaps, ranked

1. LOW-child load in L5, L8, L9, L10 (and L2, L7): Core pages of 230-340 words, text-only items (L9 Q3/Q4), Core items that need the lesson idea (L2 Q5, L5 Q1c/Q2b, L6 Q3a, L9 Q3/Q4, L10 Q7), plus unchanged 90-minute stamina (one 5-min break). Fix: move those items to "if you have time", add the bar picture to L9 Q4, split L10 Start-here to 5 items.
2. Lockstep pacing: no way to skip mastered content (criterion 11 = 1); HIGH still sits through `lN-teach/we/try` slides (25-33, 55-58); teach slides 9-10 in L5, L7, L9 limit student-led talk. Fix: a standing "puzzle of the lesson" slide on from minute 10 and an explicit "you may start the Go-further card instead of the re-teach slides" line.
3. Safeguarding and label consistency: public "whiteboards up together" in the try slides; "Challenge" headings/"Challenge Group"/"olympiad-style" in the Question Bank, Email Pack and Readiness Tracker.
4. Tier residue: 33 partial items (list in 1A), padded bank Think Harder list in L2 (8 near-Core), L7 C1/C2 without figures or labelled pattern.
5. Diagnostic residue: unused JSON (read-aloud line, rushing prompt, "$2.05" in key, cross-check sentence, stretch rule 4/6 vs 5/6), "not learnt yet" not used, stale `docs/levels_and_placement.md`, and main questions that do not probe L1/L5/L6/L8 demands.
6. Metacognition: add "Next time I will try ..." as an optional tick row and have the tutor use ticks in the next lesson's opening (criterion 10 strict reading).

---

## Summary (<= 12 lines)

1. Rubric level mean: before 13.3, earlier-claimed after 15.8, now 19.8 raw (17.5-18.5 after calibrating strictness); six lessons at 20+ (L6 23), L7 lowest at 17.
2. Journey means before to now: LOW 3.02 to 3.35, MIDDLE 3.80 to 4.10, HIGH 3.78 to 4.22; cells under 3.0 went from 6 to 0 (L6 LOW 1.83 to 3.50).
3. Tier compliance: 73% before, 100% claimed, 89% now (strict, unique items; 94% with half credit).
4. Diagnostic: before "mostly" (84% of typical children told to expect support), now "mostly yes" (typical 74-93% join); rushing prompt, read-aloud line and "$2.05" fix are in dead JSON, not in the PDFs.
5. Remaining gaps: (a) LOW load/stamina in L5, L8, L9, L10; (b) lockstep pacing, HIGH still waits; (c) public whiteboards and "Challenge Group/olympiad" labels outside the workbook; (d) 33 partial tier items and text-only L7 Challenge; (e) diagnostic dead fields and untested L1/L5/L6/L8 demands.
6. Regressions: none with clear evidence; one silent loss (Look-back "next time I will try" from close_gaps) and one rule conflict (private paper vs whiteboards up together).
7. Caveats: desk review, no children, two different raters; deltas under 0.3 (journey) or 1 per criterion (rubric) are noise.
